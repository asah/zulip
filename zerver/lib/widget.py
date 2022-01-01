import json
import logging
import re
from typing import Any, Optional, Tuple, Callable
from urllib.parse import unquote

from zerver.lib.message import SendMessageRequest
from zerver.lib.url_encoding import hash_util_encode
from zerver.models import Message, SubMessage, get_client, get_stream


def get_widget_data(content: str) -> Tuple[Optional[str], Optional[str]]:
    valid_widget_types = ["poll", "todo"]
    tokens = content.split(" ")

    # tokens[0] will always exist
    if tokens[0].startswith("/"):
        widget_type = tokens[0][1:]
        if widget_type in valid_widget_types:
            remaining_content = content.replace(tokens[0], "", 1).strip()
            extra_data = get_extra_data_from_widget_type(remaining_content, widget_type)
            return widget_type, extra_data

    return None, None


def get_extra_data_from_widget_type(content: str, widget_type: Optional[str]) -> Any:
    if widget_type == "poll":
        # This is used to extract the question from the poll command.
        # The command '/poll question' will pre-set the question in the poll
        lines = content.splitlines()
        question = ""
        options = []
        if lines and lines[0]:
            question = lines.pop(0).strip()
        extra_data = {}
        for line in lines:
            print(line)
            grp = re.search(r"promo: (?:.*)?(?:#narrow/)?stream/([0-9]+)-[^/]+/topic/([^/]+)", line.strip())
            if grp:
                extra_data['promo_stream_id'] = int(grp.group(1))
                # see static/js/hash_util.js: decodeHashComponent()
                extra_data['promo_topic'] = unquote(grp.group(2).replace(".", "%"))
                print(f"extra_data: {extra_data}")
                continue
            # If someone is using the list syntax, we remove it
            # before adding an option.
            option = re.sub(r"(\s*[-*]?\s*)", "", line.strip(), 1)
            if len(option) > 0:
                options.append(option)
        extra_data.update({
            "question": question,
            "options": options,
        })
        return extra_data
    return None


def do_widget_post_save_actions(send_request: SendMessageRequest,
                                check_send_message: Callable[..., int]) -> None:
    """
    This code works with the web app; mobile and other
    clients should also start supporting this soon.
    """
    sent_msg = send_request.message
    message_content = sent_msg.content
    sender_id = sent_msg.sender_id
    message_id = sent_msg.id

    widget_type = None
    extra_data = None    

    widget_type, extra_data = get_widget_data(message_content)
    widget_content = send_request.widget_content
    if widget_type:
        if widget_type == 'poll' and 'promo_stream_id' in extra_data:
            print(f"promo_stream_id: {extra_data['promo_stream_id']}")
            polls_stream = get_stream("polls", send_request.realm)
            polls_msg_id = send_request.message.id
            polls_topic = hash_util_encode(send_request.message.subject)
            polls_msg_url=f"/#narrow/stream/{polls_stream.id}/topic/{polls_topic}/near/{polls_msg_id}"
            extra_data['promo_msg_id'] = check_send_message(
                sender=sent_msg.sender,
                client=get_client("Internal"),
                message_type_name="stream",
                message_to=[extra_data['promo_stream_id']],
                topic_name=extra_data['promo_topic'],
                message_content=f"poll's open: [{extra_data['question']}]({polls_msg_url})",
            )
            print(f"saved promo msg id={extra_data['promo_msg_id']}")

        content = dict(
            widget_type=widget_type,
            extra_data=extra_data,
        )
        submessage = SubMessage(
            sender_id=sender_id,
            message_id=message_id,
            msg_type="widget",
            content=json.dumps(content),
        )
        submessage.save()
        send_request.submessages = SubMessage.get_raw_db_rows([message_id])
        
def get_widget_type(*, message_id: int) -> Optional[str]:
    submessage = (
        SubMessage.objects.filter(
            message_id=message_id,
            msg_type="widget",
        )
        .only("content")
        .first()
    )

    if submessage is None:
        return None

    try:
        data = json.loads(submessage.content)
    except Exception:
        return None

    try:
        return data["widget_type"]
    except Exception:
        return None


def is_widget_message(message: Message) -> bool:
    # Right now all messages that are widgetized use submessage, and vice versa.
    return message.submessage_set.exists()
