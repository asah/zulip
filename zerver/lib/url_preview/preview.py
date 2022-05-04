import logging
import re
from typing import Any, Callable, Match, Optional
from urllib.parse import urljoin

import magic
import requests
from django.conf import settings
from django.utils.encoding import smart_str
from previewlink import preview_link

from version import ZULIP_VERSION
from zerver.lib.cache import cache_with_key, preview_url_cache_key
from zerver.lib.outgoing_http import OutgoingSession
from zerver.lib.pysa import mark_sanitized
from zerver.lib.url_preview.oembed import get_oembed_data
from zerver.lib.url_preview.parsers import GenericParser, OpenGraphParser
from zerver.lib.url_preview.types import UrlEmbedData, UrlOEmbedData

# Based on django.core.validators.URLValidator, with ftp support removed.
link_regex = re.compile(
    r"^(?:http)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)

# Use Chrome User-Agent, since some sites refuse to work on old browsers
ZULIP_URL_PREVIEW_USER_AGENT = (
    "Mozilla/5.0 (compatible; ZulipURLPreview/{version}; +{external_host})"
).format(version=ZULIP_VERSION, external_host=settings.ROOT_DOMAIN_URI)

# FIXME: This header and timeout are not used by pyoembed, when trying to autodiscover!
HEADERS = {"User-Agent": ZULIP_URL_PREVIEW_USER_AGENT}
TIMEOUT = 15


class PreviewSession(OutgoingSession):
    def __init__(self) -> None:
        super().__init__(role="preview", timeout=TIMEOUT, headers=HEADERS)


def is_link(url: str) -> Optional[Match[str]]:
    return link_regex.match(smart_str(url))


def guess_mimetype_from_content(response: requests.Response) -> str:
    mime_magic = magic.Magic(mime=True)
    try:
        content = next(response.iter_content(1000))
    except StopIteration:
        content = ""
    return mime_magic.from_buffer(content)


def valid_content_type(url: str) -> bool:
    try:
        response = PreviewSession().get(url, stream=True)
    except requests.RequestException:
        return False

    if not response.ok:
        return False

    content_type = response.headers.get("content-type")
    # Be accommodating of bad servers: assume content may be html if no content-type header
    if not content_type or content_type.startswith("text/html"):
        # Verify that the content is actually HTML if the server claims it is
        content_type = guess_mimetype_from_content(response)
    return content_type.startswith("text/html")


def catch_network_errors(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException:
            pass

    return wrapper


@catch_network_errors
@cache_with_key(preview_url_cache_key, with_statsd_key="urlpreview_data")
def get_link_embed_data(
    url: str, maxwidth: int = 640, maxheight: int = 480
) -> Optional[UrlEmbedData]:
    if not is_link(url):
        return None

    if not valid_content_type(url):
        return None

    # The oembed data from pyoembed may be complete enough to return
    # as-is; if so, we use it.  Otherwise, we use it as a _base_ for
    # the other, less sophisticated techniques which we apply as
    # successive fallbacks.
    data = get_oembed_data(url, maxwidth=maxwidth, maxheight=maxheight)
    if data is not None and isinstance(data, UrlOEmbedData):
        return data
    if data is None:
        data = {}

    mark_sanitized_url = mark_sanitized(url)
    response = PreviewSession().get(mark_sanitized_url, stream=True)
    if response.ok:
        og_data = OpenGraphParser(
            response.content, response.headers.get("Content-Type")
        ).extract_data()
        for key in ["title", "description", "image"]:
            if (not data or not data.get(key)) and (og_data and og_data.__dict__.get(key)):
                data[key] = og_data.__dict__[key]

        generic_data = (
            GenericParser(response.content, response.headers.get("Content-Type")).extract_data()
            or {}
        )
        for key in ["title", "description", "image"]:
            if not data.get(key) and generic_data.__dict__.get(key):
                data[key] = generic_data.__dict__[key]
    if "image" in data:
        data["image"] = urljoin(response.url, data["image"])

    if (
        data.get("title") in ["", None]
        or data.get("description") in ["", None]
        or data.get("image") in ["", None]
    ):
        logging.info(
            f"trying preview_link({mark_sanitized_url}) because some field(s) missing: {data}"
        )
        res = preview_link(mark_sanitized_url)
        for key in ["title", "description", "image"]:
            if data.get(key) in ["", None]:
                data[key] = res.get(key, "")

    logging.info(f"found preview data: {data}")

    if "news.ycombinator.com" in mark_sanitized_url:
        data[
            "image"
        ] = "https://image.winudf.com/v2/image1/Y29tLmFsZmlhbmxvc2FyaS5oYWNrZXJuZXdzX2ljb25fMTU0MTY3Nzg4OF8wODA/icon.png?w=&fakeurl=1"

    if data is None:
        data = UrlEmbedData()

    for parser_class in (OpenGraphParser, GenericParser):
        parser = parser_class(response.content, response.headers.get("Content-Type"))
        for key in ["title", "description", "image"]:
            if not data.get(key):
                data[key] = parser.__dict__.get(key)

    if data["image"]:
        data["image"] = urljoin(response.url, data["image"])
    return data
