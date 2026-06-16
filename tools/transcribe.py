"""Transcribe audio files in raw/audio/ to markdown in raw/conversations/.

Usage:
  python tools/transcribe.py                  # transcribe all new files in raw/audio/
  python tools/transcribe.py <path/to/file>   # transcribe a specific file
  python tools/transcribe.py --model medium   # use smaller/faster model
  python tools/transcribe.py --keep-audio     # don't move audio to processed/

Model choices for Vietnamese (CPU, int8):
  large-v3  ~3 GB, best quality, ~0.3x realtime
  medium    ~1.5 GB, good quality, ~0.7x realtime
  small     ~0.5 GB, OK quality, ~1.5x realtime
"""
import argparse
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import imageio_ffmpeg

_ffmpeg_dir = Path(imageio_ffmpeg.get_ffmpeg_exe()).parent
os.environ["PATH"] = str(_ffmpeg_dir) + os.pathsep + os.environ.get("PATH", "")

from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent.parent
AUDIO_DIR = ROOT / "raw" / "audio"
PROCESSED_DIR = AUDIO_DIR / "processed"
OUT_DIR = ROOT / "raw" / "conversations"

AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".flac", ".ogg", ".opus", ".webm", ".aac", ".amr", ".wma"}


def slugify(name: str) -> str:
    # Keep Vietnamese chars out — use ASCII slugs for filenames
    replacements = str.maketrans(
        "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
        "ÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸĐ",
        "aaaaaaaaaaaaaaaaaeeeeeeeeeeeiiiiiooooooooooooooooouuuuuuuuuuuyyyyyd"
        "AAAAAAAAAAAAAAAAAEEEEEEEEEEEIIIIIOOOOOOOOOOOOOOOOOUUUUUUUUUUUYYYYYD",
    )
    name = name.translate(replacements).lower()
    name = re.sub(r"[^a-z0-9\-_\s]", "", name)
    name = re.sub(r"[\s_]+", "-", name).strip("-")
    return name or "untitled"


def parse_date_from_name(stem: str) -> tuple[str, str]:
    """Recognize YYYY-MM-DD, YYYY_MM_DD, YYYYMMDD prefixes. Returns (date_iso, rest)."""
    m = re.match(r"^(\d{4})[-_]?(\d{2})[-_]?(\d{2})[-_\s]*(.*)$", stem)
    if m:
        y, mo, d, rest = m.groups()
        return f"{y}-{mo}-{d}", rest.strip("-_ ")
    return "", stem


def format_ts(seconds: float) -> str:
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def transcribe_one(audio_path: Path, model: WhisperModel) -> Path:
    stem = audio_path.stem
    date_str, label = parse_date_from_name(stem)
    if not date_str:
        date_str = datetime.fromtimestamp(audio_path.stat().st_mtime).strftime("%Y-%m-%d")
        label = stem
    if not label:
        label = "ghi-am"

    # Detect course context from subfolder: raw/audio/<course>/<file>.m4a → course=<course>
    course = None
    try:
        rel = audio_path.relative_to(AUDIO_DIR)
        if len(rel.parts) > 1:
            course = slugify(rel.parts[0])
    except ValueError:
        pass

    out_slug = slugify(label)
    if course:
        # Course: no date prefix; output as raw/conversations/<course>-<slug>.md
        out_path = OUT_DIR / f"{course}-{out_slug}.md"
        type_str = "course-lecture"
    else:
        out_path = OUT_DIR / f"{date_str}-{out_slug}.md"
        type_str = "conversation"

    if out_path.exists():
        print(f"  skip (already transcribed): {out_path.name}")
        return out_path

    print(f"  transcribing {audio_path.name} ...")
    segments, info = model.transcribe(
        str(audio_path),
        language="vi",
        vad_filter=True,
        beam_size=5,
        condition_on_previous_text=False,
        no_repeat_ngram_size=3,
        repetition_penalty=1.2,
        temperature=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        compression_ratio_threshold=2.4,
        log_prob_threshold=-1.0,
        no_speech_threshold=0.6,
    )

    lines_ts = []
    plain_parts = []
    for seg in segments:
        text = seg.text.strip()
        lines_ts.append(f"[{format_ts(seg.start)} → {format_ts(seg.end)}] {text}")
        plain_parts.append(text)

    transcript_ts = "\n".join(lines_ts)
    transcript_plain = " ".join(plain_parts)
    duration = round(info.duration, 1)

    if course:
        fm = f"""---
date: {date_str}
type: {type_str}
course: {course}
source_audio: {audio_path.name}
duration_seconds: {duration}
language: {info.language}
---

# {course.upper()} — {label}

> Nói "ingest {out_path.stem}" để đẩy vào wiki theo workflow khóa học."""
    else:
        fm = f"""---
date: {date_str}
type: {type_str}
source_audio: {audio_path.name}
duration_seconds: {duration}
language: {info.language}
participants: []
context: ""
---

# {date_str} — {label}

> Sau khi điền `participants` và `context` ở frontmatter, nói "ingest [tên-file]" để đẩy vào wiki."""

    body = f"""{fm}

## Transcript có timecode

{transcript_ts}

## Bản plain text

{transcript_plain}
"""
    out_path.write_text(body, encoding="utf-8")
    print(f"  -> {out_path.relative_to(ROOT)}")
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="Specific audio file (optional)")
    ap.add_argument("--model", default="large-v3", help="Whisper model (default: large-v3)")
    ap.add_argument("--device", default="cpu", choices=["cpu", "cuda"])
    ap.add_argument("--compute", default="int8", help="Compute type: int8, int8_float16, float16, float32")
    ap.add_argument("--keep-audio", action="store_true", help="Don't move audio to processed/")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    if args.file:
        p = Path(args.file)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        targets = [p]
    else:
        # Recursive scan, but skip the processed/ subtree
        targets = sorted(
            p for p in AUDIO_DIR.rglob("*")
            if p.is_file() and p.suffix.lower() in AUDIO_EXTS
            and PROCESSED_DIR not in p.parents and p != PROCESSED_DIR
        )

    if not targets:
        print(f"Không có file audio mới trong {AUDIO_DIR}")
        return 0

    print(f"Loading model: {args.model} ({args.device}/{args.compute}) — lần đầu sẽ tải về ~3GB")
    model = WhisperModel(args.model, device=args.device, compute_type=args.compute)
    print(f"Tìm thấy {len(targets)} file audio cần xử lý")

    for audio in targets:
        try:
            transcribe_one(audio, model)
            if not args.keep_audio and audio.is_relative_to(AUDIO_DIR):
                # Preserve relative path under processed/
                rel = audio.relative_to(AUDIO_DIR)
                dest = PROCESSED_DIR / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                if dest.exists():
                    dest = dest.parent / f"{audio.stem}-{int(audio.stat().st_mtime)}{audio.suffix}"
                shutil.move(str(audio), str(dest))
        except Exception as e:
            print(f"  LỖI {audio.name}: {e}")
            continue

    print("Xong.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
