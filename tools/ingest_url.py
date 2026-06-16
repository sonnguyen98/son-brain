"""Fetch a URL and save as markdown in raw/web/.

Handles:
  - Articles / blogs / general web pages (via trafilatura)
  - YouTube videos (transcripts via youtube-transcript-api)

Usage:
  python tools/ingest_url.py <url>
  python tools/ingest_url.py <url> --name custom-slug
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, parse_qs

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
WEB_DIR = ROOT / "raw" / "web"


def slugify(name: str, maxlen: int = 60) -> str:
    repl = str.maketrans(
        "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
        "ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ",
        "aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd"
        "AAAAAAAAAAAAAAAAAEEEEEEEEEEEIIIIIOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYD",
    )
    name = name.translate(repl).lower()
    name = re.sub(r"[^a-z0-9\-_\s]", "", name)
    name = re.sub(r"[\s_]+", "-", name).strip("-")
    return (name or "untitled")[:maxlen].strip("-")


def is_youtube(url: str) -> str | None:
    u = urlparse(url)
    if u.netloc in {"www.youtube.com", "youtube.com", "m.youtube.com"}:
        qs = parse_qs(u.query)
        return qs.get("v", [None])[0]
    if u.netloc in {"youtu.be"}:
        return u.path.lstrip("/").split("/")[0] or None
    return None


def fetch_youtube(url: str, video_id: str) -> tuple[str, dict]:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api.formatters import TextFormatter

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        # prefer Vietnamese, then English, then any available
        try:
            t = transcript_list.find_transcript(["vi"])
        except Exception:
            try:
                t = transcript_list.find_transcript(["en"])
            except Exception:
                t = next(iter(transcript_list))
        entries = t.fetch()
        lang = t.language_code
    except Exception as e:
        return "", {"error": f"Không lấy được transcript YouTube: {e}"}

    # Format with timestamps every ~30s
    lines = []
    plain = []
    bucket_end = 30.0
    bucket = []
    for entry in entries:
        plain.append(entry["text"])
        bucket.append(entry["text"])
        if entry["start"] >= bucket_end:
            ts = format_ts(bucket_end - 30)
            lines.append(f"[{ts}] {' '.join(bucket)}")
            bucket = []
            bucket_end += 30.0
    if bucket:
        ts = format_ts(bucket_end - 30)
        lines.append(f"[{ts}] {' '.join(bucket)}")

    body = "\n\n".join(lines)
    plain_text = " ".join(plain)
    return body, {"title": f"YouTube {video_id}", "lang": lang, "video_id": video_id, "plain": plain_text}


def format_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def fetch_web(url: str) -> tuple[str, dict]:
    import trafilatura

    downloaded = trafilatura.fetch_url(url)
    if downloaded is None:
        return "", {"error": "Không tải được URL"}

    result = trafilatura.extract(
        downloaded,
        output_format="markdown",
        include_links=True,
        include_images=False,
        with_metadata=False,
        favor_recall=True,
    )
    if not result:
        return "", {"error": "Không extract được nội dung"}

    meta = trafilatura.extract_metadata(downloaded)
    meta_dict = {
        "title": meta.title if meta else "",
        "author": meta.author if meta else "",
        "site": meta.sitename if meta else urlparse(url).netloc,
        "published": meta.date if meta else "",
    }
    return result, meta_dict


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("url", help="URL to ingest")
    ap.add_argument("--name", help="Custom slug (default: derived from title/URL)")
    args = ap.parse_args()

    WEB_DIR.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()

    video_id = is_youtube(args.url)
    if video_id:
        print(f"YouTube video: {video_id}")
        body, meta = fetch_youtube(args.url, video_id)
        kind = "youtube"
    else:
        print(f"Web article: {args.url}")
        body, meta = fetch_web(args.url)
        kind = "web"

    if "error" in meta:
        print(f"LỖI: {meta['error']}")
        return 1

    title = meta.get("title", "") or args.url
    slug = args.name or slugify(title or video_id or "untitled")
    out_path = WEB_DIR / f"{today}-{slug}.md"

    if out_path.exists():
        print(f"File đã có, ghi đè: {out_path.relative_to(ROOT)}")

    fm_lines = ["---", f"date: {today}", f"type: {kind}", f"source_url: {args.url}"]
    for k in ("title", "author", "site", "published", "lang", "video_id"):
        if meta.get(k):
            fm_lines.append(f"{k}: {meta[k]!r}" if any(c in str(meta[k]) for c in ":#") else f"{k}: {meta[k]}")
    fm_lines.append("---")

    front = "\n".join(fm_lines)
    plain_section = f"\n\n## Bản plain text\n\n{meta['plain']}\n" if meta.get("plain") else ""

    out_path.write_text(f"{front}\n\n# {title}\n\n{body}{plain_section}", encoding="utf-8")
    print(f"-> {out_path.relative_to(ROOT)}  ({len(body)} ký tự)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
