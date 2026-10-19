#!/usr/bin/env python3
"""
Download the full message history of a set of Zulip channels in parallel, and
reshape it into topic-level records ready for LLM summarization.

By default it exports every channel in the chat.zulip.org channel folder whose
name contains "contributor" (case-insensitive), e.g. a "Contributors" folder.

SETUP
  1. pip install requests
  2. In Zulip: Personal settings -> Account & privacy -> API key ->
     "Download zuliprc". Save it as ~/.zuliprc (or pass --zuliprc PATH).

USAGE
  python zulip_export.py --list            # show folders + channels, download nothing
  python zulip_export.py                   # export the "Contributors" folder, 4 channels at a time
  python zulip_export.py --workers 6       # more channels at once (all share one rate-limit budget)
  python zulip_export.py --folder "dev"    # match a different folder name
  python zulip_export.py --channels backend frontend "api design"
  python zulip_export.py --offline         # rebuild topics/ and .md from what's already downloaded

OUTPUT (./zulip-export/ by default)
  <channel>.jsonl          raw API messages, one per line, original Markdown.
                           The complete record; everything else is derived from it.
  topics/<channel>.jsonl   one record per topic: channel, topic, permalink, dates,
                           participants, approx token count, compact transcript.
                           This is the input for an LLM summarization pass.
  <channel>.md             readable transcript grouped by topic, with permalinks.
  stats.json               per-channel message/topic/token counts and topic sizes.
  channels.json            server + metadata for the exported channels.

Re-running is safe: each channel resumes after the last message already saved,
so an interrupted run picks up where it stopped and a later run adds only new
messages. Topic files are rebuilt from the raw files every run.
"""

import argparse
import configparser
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

try:
    import requests
except ImportError:
    sys.exit("This script needs the 'requests' package:  pip install requests")

BATCH = 1000   # messages per request (Zulip recommends <= 1000; hard max is 5000)
PAUSE = 0.2    # seconds each worker waits between its own requests

STOP = threading.Event()
_print_lock = threading.Lock()


class Interrupted(Exception):
    pass


def log(msg, err=False):
    with _print_lock:
        print(msg, file=sys.stderr if err else sys.stdout, flush=True)


# ---------------------------------------------------------------- API client

class RateGate:
    """One rate-limit budget shared by every worker thread.

    Zulip limits each user (default: 200 requests/minute), not each connection,
    so when one worker learns the budget is low or exhausted, all of them wait.
    """

    def __init__(self):
        self._lock = threading.Lock()
        self._resume_at = 0.0

    def wait(self):
        while True:
            if STOP.is_set():
                raise Interrupted()
            with self._lock:
                delay = self._resume_at - time.time()
            if delay <= 0:
                return
            time.sleep(min(delay, 1.0))

    def pause_until(self, t, reason):
        with self._lock:
            if t <= self._resume_at:
                return
            extension = t - max(self._resume_at, time.time())
            self._resume_at = t
        if extension > 1:
            log(f"    {reason}: all workers pausing {t - time.time():.0f}s", err=True)


class Zulip:
    def __init__(self, zuliprc, workers=1):
        cfg = configparser.ConfigParser()
        path = os.path.expanduser(zuliprc)
        if not cfg.read(path) or "api" not in cfg:
            sys.exit(
                f"Could not read an [api] section from {path}.\n"
                "Download your zuliprc in Zulip: Personal settings -> "
                "Account & privacy -> API key."
            )
        api = cfg["api"]
        self.site = api.get("site", "https://chat.zulip.org").rstrip("/")
        self._auth = (api["email"], api["key"])
        self._local = threading.local()          # one HTTP session per thread
        self.gate = RateGate()
        self.reserve = max(3, workers * 2)       # stop before the budget hits zero

    def _session(self):
        s = getattr(self._local, "session", None)
        if s is None:
            s = requests.Session()
            s.auth = self._auth
            s.headers["User-Agent"] = "zulip-channel-export/2.0"
            self._local.session = s
        return s

    def _note_budget(self, r):
        try:
            remaining = int(r.headers["X-RateLimit-Remaining"])
            reset = float(r.headers["X-RateLimit-Reset"])
        except (KeyError, ValueError, TypeError):
            return
        if remaining <= self.reserve:
            if reset < 1e9:                      # relative seconds, not a timestamp
                reset += time.time()
            self.gate.pause_until(min(reset, time.time() + 120), "rate-limit budget low")

    def get(self, endpoint, **params):
        # Zulip expects JSON encoding for lists, dicts and booleans.
        params = {
            k: json.dumps(v) if isinstance(v, (list, dict, bool)) else v
            for k, v in params.items()
        }
        url = f"{self.site}/api/v1/{endpoint}"
        failures = 0
        while True:
            self.gate.wait()
            try:
                r = self._session().get(url, params=params, timeout=120)
            except requests.RequestException as e:
                failures += 1
                if failures >= 8:
                    raise RuntimeError(f"{endpoint}: network keeps failing ({e})")
                wait = min(60, 2 ** failures)
                log(f"    network error ({e.__class__.__name__}); retrying in {wait}s", err=True)
                time.sleep(wait)
                continue

            if r.status_code == 429:
                wait = r.headers.get("Retry-After")
                if wait is None:
                    try:
                        wait = r.json().get("retry-after")
                    except ValueError:
                        wait = None
                self.gate.pause_until(time.time() + float(wait or 10) + 1, "rate limited")
                continue

            if r.status_code >= 500:
                failures += 1
                if failures >= 8:
                    raise RuntimeError(f"{endpoint}: server keeps failing ({r.status_code})")
                wait = min(60, 2 ** failures)
                log(f"    server error {r.status_code}; retrying in {wait}s", err=True)
                time.sleep(wait)
                continue

            try:
                data = r.json()
            except ValueError:
                raise RuntimeError(f"{endpoint}: unexpected response ({r.status_code}): {r.text[:200]}")
            if data.get("result") != "success":
                raise RuntimeError(f"{endpoint}: {data.get('msg') or r.status_code}")
            self._note_budget(r)
            return data


# ---------------------------------------------------------------- channels

def get_all_channels(z, include_archived):
    return z.get(
        "streams",
        include_public=True,
        include_web_public=True,
        include_subscribed=True,
        exclude_archived=not include_archived,
    )["streams"]


def get_folders(z):
    try:
        return z.get("channel_folders", include_archived=True)["channel_folders"]
    except RuntimeError as e:
        sys.exit(f"Could not fetch channel folders ({e}). Use --channels to name channels directly.")


def list_everything(z, include_archived):
    folders = {f["id"]: f["name"] for f in get_folders(z)}
    channels = get_all_channels(z, include_archived)
    groups = {}
    for s in channels:
        groups.setdefault(s.get("folder_id"), []).append(s)
    order = [fid for fid in folders if fid in groups] + ([None] if None in groups else [])
    for fid in order:
        print(f"\n{folders.get(fid, '(no folder)')}")
        for s in sorted(groups[fid], key=lambda s: s["name"].lower()):
            traffic = s.get("stream_weekly_traffic")
            extra = f"~{traffic}/week" if traffic is not None else ""
            if s.get("is_archived"):
                extra += " (archived)"
            print(f"   #{s['name']:<40} {extra}")


def pick_channels(z, args):
    channels = get_all_channels(z, not args.skip_archived)

    if args.channels:
        by_name = {s["name"].lower(): s for s in channels}
        wanted = [c.lstrip("#").lower() for c in args.channels]
        missing = [c for c in wanted if c not in by_name]
        if missing:
            sys.exit("Channel(s) not found: " + ", ".join(missing) + "\nRun with --list to see names.")
        return [by_name[c] for c in wanted]

    folders = get_folders(z)
    matches = [f for f in folders if args.folder.lower() in f["name"].lower()]
    if not matches:
        names = ", ".join(f["name"] for f in folders) or "(none)"
        sys.exit(f'No channel folder matches "{args.folder}". Folders on this server: {names}')
    print("Folder(s): " + ", ".join(f["name"] for f in matches))
    ids = {f["id"] for f in matches}
    return [s for s in channels if s.get("folder_id") in ids]


# ---------------------------------------------------------------- download

def safe_name(name):
    return re.sub(r"[^\w.-]+", "_", name).strip("_") or "channel"


def fmt_ts(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")


def fmt_day(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def resume_point(path):
    """Return (last_message_id, count) already saved; trim any half-written last line."""
    if not path.exists():
        return None, 0
    last_id, count, good_bytes = None, 0, 0
    with path.open("rb") as f:
        for line in f:
            if not line.endswith(b"\n"):
                break
            try:
                last_id = json.loads(line)["id"]
            except (ValueError, KeyError):
                break
            count += 1
            good_bytes += len(line)
    if good_bytes != path.stat().st_size:
        with path.open("r+b") as f:
            f.truncate(good_bytes)
    return last_id, count


def download_channel(z, stream, out_dir):
    name = stream["name"]
    path = out_dir / f"{safe_name(name)}.jsonl"
    last_id, count = resume_point(path)
    narrow = [{"operator": "channel", "operand": stream["stream_id"]}]

    if last_id is None:
        anchor, include_anchor = "oldest", True
        log(f"  start  #{name}")
    else:
        anchor, include_anchor = last_id, False
        log(f"  resume #{name} after {count:,} saved messages")

    new = batches = 0
    with path.open("a", encoding="utf-8") as out:
        while True:
            data = z.get(
                "messages",
                anchor=anchor,
                include_anchor=include_anchor,
                num_before=0,
                num_after=BATCH,
                narrow=narrow,
                apply_markdown=False,    # keep the original Markdown source
                client_gravatar=True,
            )
            msgs = data["messages"]
            for m in msgs:
                out.write(json.dumps(m, ensure_ascii=False) + "\n")
            out.flush()
            new += len(msgs)
            batches += 1

            if msgs:
                anchor, include_anchor = msgs[-1]["id"], False
                if batches % 25 == 0:
                    log(f"         #{name}: {count + new:,} messages, reached {fmt_day(msgs[-1]['timestamp'])}")
            if data.get("found_newest") or not msgs:
                break
            time.sleep(PAUSE)
    return path, count + new, new


# ---------------------------------------------------------------- topics

# Zulip's quote-and-reply inserts the whole quoted message; in a transcript the
# original is usually right above it, so keep only a short excerpt.
QUOTE_INTRO = re.compile(r"@_\*\*([^*|\n]+?)(?:\|\d+)?\*\* \[said\]\([^)\s]*\):[ \t]*")
QUOTE_BLOCK = re.compile(r"^(`{3,}|~{3,})[ \t]*quote[ \t]*\n(.*?)\n\1[ \t]*$", re.S | re.M)
MENTION = re.compile(r"@_?\*\*([^*|\n]+?)(?:\|\d+)?\*\*")
QUOTE_KEEP = 300


def _short_quote(m):
    text = " ".join(m.group(2).split())
    if len(text) > QUOTE_KEEP:
        text = text[:QUOTE_KEEP].rstrip() + " …"
    return "> " + text


def compact(content, site):
    c = QUOTE_INTRO.sub(lambda m: f"(replying to {m.group(1)})", content)
    c = QUOTE_BLOCK.sub(_short_quote, c)
    c = MENTION.sub(lambda m: "@" + m.group(1), c)
    c = c.replace("](/user_uploads/", f"]({site}/user_uploads/")
    return c.strip()


def zulip_encode(s):
    """Zulip's URL-fragment encoding: percent-encode, then '.'->'.2E' and '%'->'.'."""
    return quote(s, safe="").replace(".", ".2E").replace("%", ".")


def topic_url(site, stream, topic, message_id):
    # /with/<id> keeps the link working if the topic is later renamed or moved.
    slug = f"{stream['stream_id']}-{zulip_encode(stream['name'].replace(' ', '-'))}"
    return f"{site}/#narrow/channel/{slug}/topic/{zulip_encode(topic)}/with/{message_id}"


SIZE_BUCKETS = [(3, "1-3"), (20, "4-20"), (100, "21-100"), (float("inf"), "100+")]


def build_topics(site, stream, jsonl_path, out_dir, markdown):
    """Group a channel's raw messages by topic; write topics/<channel>.jsonl and <channel>.md."""
    topics = {}  # insertion order = order of each topic's first message
    with jsonl_path.open(encoding="utf-8") as f:
        for line in f:
            m = json.loads(line)
            topic = m.get("subject") or "(general chat)"
            topics.setdefault(topic, []).append(
                (m["id"], m["timestamp"], m.get("sender_full_name", "?"), compact(m.get("content", ""), site))
            )

    total_msgs = sum(len(v) for v in topics.values())
    stats = {
        "channel": stream["name"], "messages": total_msgs, "topics": len(topics), "approx_tokens": 0,
        "by_size": {label: {"topics": 0, "approx_tokens": 0} for _, label in SIZE_BUCKETS},
    }

    topics_dir = out_dir / "topics"
    topics_dir.mkdir(exist_ok=True)
    tpath = topics_dir / f"{safe_name(stream['name'])}.jsonl"
    tmp = tpath.with_suffix(".jsonl.tmp")
    md = jsonl_path.with_suffix(".md").open("w", encoding="utf-8") if markdown else None
    try:
        if md:
            md.write(f"# #{stream['name']}\n\n")
            if stream.get("description"):
                md.write(f"> {stream['description']}\n\n")
            md.write(
                f"Exported from {site} on {datetime.now(timezone.utc):%Y-%m-%d}: "
                f"{total_msgs:,} messages in {len(topics):,} topics.\n"
            )
        with tmp.open("w", encoding="utf-8") as tout:
            for topic, msgs in topics.items():
                lines, day, counts = [], None, {}
                for _, ts, sender, content in msgs:
                    d = fmt_day(ts)
                    if d != day:
                        lines.append(f"[{d}]")
                        day = d
                    lines.append(f"{sender}: {content}")
                    counts[sender] = counts.get(sender, 0) + 1
                transcript = "\n".join(lines)
                tokens = len(transcript) // 4    # rough: ~4 characters per token
                url = topic_url(site, stream, topic, msgs[0][0])
                record = {
                    "channel": stream["name"],
                    "channel_id": stream["stream_id"],
                    "topic": topic,
                    "url": url,
                    "first_id": msgs[0][0],
                    "last_id": msgs[-1][0],
                    "start": fmt_day(msgs[0][1]),
                    "end": fmt_day(msgs[-1][1]),
                    "messages": len(msgs),
                    "participants": sorted(counts, key=counts.get, reverse=True),
                    "resolved": topic.startswith("✔ "),
                    "approx_tokens": tokens,
                    "transcript": transcript,
                }
                tout.write(json.dumps(record, ensure_ascii=False) + "\n")

                stats["approx_tokens"] += tokens
                label = next(lbl for limit, lbl in SIZE_BUCKETS if len(msgs) <= limit)
                stats["by_size"][label]["topics"] += 1
                stats["by_size"][label]["approx_tokens"] += tokens

                if md:
                    md.write(f"\n## {topic}\n\n*{record['start']} to {record['end']} · "
                             f"{len(msgs)} messages · [open in Zulip]({url})*\n\n")
                    for _, ts, sender, content in msgs:
                        md.write(f"**{sender}** · {fmt_ts(ts)} UTC\n\n{content}\n\n")
        os.replace(tmp, tpath)
    finally:
        if md:
            md.close()
        if tmp.exists():
            tmp.unlink()
    return stats


def process_channel(z, site, stream, out_dir, markdown, download=True):
    if download:
        path, total, new = download_channel(z, stream, out_dir)
    else:
        path = out_dir / f"{safe_name(stream['name'])}.jsonl"
        if not path.exists():
            raise RuntimeError("no downloaded file to rebuild from")
        new = 0
    if STOP.is_set():
        raise Interrupted()
    stats = build_topics(site, stream, path, out_dir, markdown)
    stats["new"] = new
    return stats


# ---------------------------------------------------------------- summary

def human(n):
    return f"{n / 1e6:.1f}M" if n >= 1e6 else f"{n / 1e3:.0f}k" if n >= 1e3 else str(n)


def report(results, out_dir):
    results.sort(key=lambda s: s["approx_tokens"], reverse=True)
    totals = {"messages": 0, "topics": 0, "approx_tokens": 0}
    by_size = {label: {"topics": 0, "approx_tokens": 0} for _, label in SIZE_BUCKETS}
    for s in results:
        for k in totals:
            totals[k] += s[k]
        for label, v in s["by_size"].items():
            by_size[label]["topics"] += v["topics"]
            by_size[label]["approx_tokens"] += v["approx_tokens"]

    (out_dir / "stats.json").write_text(
        json.dumps({"totals": totals, "by_topic_size": by_size, "channels": results}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print(f"\n{'Channel':<34}{'Messages':>11}{'Topics':>9}{'~Tokens':>9}")
    for s in results:
        print(f"#{s['channel']:<33}{s['messages']:>11,}{s['topics']:>9,}{human(s['approx_tokens']):>9}")
    print(f"{'Total':<34}{totals['messages']:>11,}{totals['topics']:>9,}{human(totals['approx_tokens']):>9}")

    if totals["topics"]:
        print("\nTopic sizes (share of topics / share of tokens):")
        for _, label in SIZE_BUCKETS:
            b = by_size[label]
            pt = 100 * b["topics"] / totals["topics"]
            pk = 100 * b["approx_tokens"] / max(1, totals["approx_tokens"])
            print(f"  {label:>7} messages: {b['topics']:>8,} topics ({pt:4.0f}%)   {human(b['approx_tokens']):>7} tokens ({pk:4.0f}%)")
    print("\nToken counts are estimates (~4 characters per token).")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Export Zulip channel history for LLM processing.")
    ap.add_argument("--zuliprc", default="~/.zuliprc", help="path to your zuliprc (default ~/.zuliprc)")
    ap.add_argument("--folder", default="contributor", help='channel folder to export (substring match, default "contributor")')
    ap.add_argument("--channels", nargs="+", metavar="NAME", help="export these channels instead of a folder")
    ap.add_argument("--out", default="zulip-export", help="output directory (default ./zulip-export)")
    ap.add_argument("--workers", type=int, default=4, help="channels downloaded at the same time (default 4)")
    ap.add_argument("--list", action="store_true", help="list folders and channels, then exit")
    ap.add_argument("--skip-archived", action="store_true", help="leave out archived channels")
    ap.add_argument("--no-markdown", action="store_true", help="skip the readable <channel>.md transcripts")
    ap.add_argument("--offline", action="store_true", help="don't contact the server; rebuild topics/ and .md from existing downloads")
    args = ap.parse_args()
    workers = max(1, args.workers)
    out_dir = Path(args.out)

    if args.offline:
        meta_path = out_dir / "channels.json"
        if not meta_path.exists():
            sys.exit(f"{meta_path} not found; run a normal export first.")
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        site, chosen = meta["site"], meta["channels"]
        z, download = None, False
    else:
        z = Zulip(args.zuliprc, workers)
        if args.list:
            list_everything(z, include_archived=not args.skip_archived)
            return
        chosen = pick_channels(z, args)
        site, download = z.site, True
        if not chosen:
            sys.exit("No channels selected.")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "channels.json").write_text(
            json.dumps({"site": site, "channels": chosen}, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    # Oldest channels first: they usually have the most history, so starting them
    # early keeps the slowest channel from finishing last on its own.
    chosen = sorted(chosen, key=lambda s: s.get("first_message_id") or float("inf"))
    print(f"{len(chosen)} channel(s), {workers} at a time: " + ", ".join("#" + s["name"] for s in chosen) + "\n")

    results, failures = [], []
    ex = ThreadPoolExecutor(max_workers=workers)
    futures = {ex.submit(process_channel, z, site, s, out_dir, not args.no_markdown, download): s for s in chosen}
    try:
        for fut in as_completed(futures):
            s = futures[fut]
            try:
                st = fut.result()
            except Interrupted:
                continue
            except Exception as e:
                failures.append(s["name"])
                log(f"  FAILED #{s['name']}: {e}", err=True)
                continue
            results.append(st)
            log(f"  done   #{s['name']}: {st['messages']:,} messages ({st['new']:,} new), "
                f"{st['topics']:,} topics  [{len(results) + len(failures)}/{len(chosen)}]")
    except KeyboardInterrupt:
        STOP.set()
        log("\nStopping once in-flight requests finish. Run the same command again to resume.", err=True)
        ex.shutdown(wait=True, cancel_futures=True)
        sys.exit(1)
    ex.shutdown()

    if results:
        report(results, out_dir)
    print(f"\nOutput: {out_dir.resolve()}")
    if failures:
        sys.exit(f"{len(failures)} channel(s) failed: {', '.join(failures)}. Re-run to retry them.")


if __name__ == "__main__":
    main()
