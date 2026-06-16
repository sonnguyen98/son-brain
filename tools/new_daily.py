"""Create or open today's daily note in raw/daily/YYYY-MM-DD.md.

Usage:
  python tools/new_daily.py              # today's note
  python tools/new_daily.py 2026-06-15   # specific date
  python tools/new_daily.py --no-open    # don't auto-open
"""
import argparse
import os
import sys
from datetime import date, datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = ROOT / "raw" / "daily"

TEMPLATE = """---
date: {date}
type: daily
mood: ""
energy: ""
---

# {date}

## Quan sát / Thấy
<!-- Những gì thấy hôm nay đáng nhớ: sự kiện, hành vi của người khác, hiện tượng -->

## Học / Đọc
<!-- Bài, sách, video, podcast đã tiếp xúc — kèm link nếu có -->

## Gặp / Nói chuyện
<!-- Người đã gặp — tên + 1 dòng nội dung chính. Khi ingest sẽ tự update wiki/person/ -->

## Idea
<!-- Ý tưởng mới — về kinh doanh, content, cá nhân, bất kỳ -->

## TODO mai
<!-- Việc cần làm ngày mai -->

## Cảm xúc / Phản tỉnh
<!-- 1-3 dòng — bỏ trống nếu không có gì cần ghi -->
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("date", nargs="?", help="Date YYYY-MM-DD (default: today)")
    ap.add_argument("--no-open", action="store_true", help="Don't auto-open in default editor")
    args = ap.parse_args()

    if args.date:
        try:
            d = datetime.strptime(args.date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Sai format ngày: {args.date} (cần YYYY-MM-DD)")
            return 1
    else:
        d = date.today()

    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    path = DAILY_DIR / f"{d.isoformat()}.md"

    if path.exists():
        print(f"Daily note đã có: {path.relative_to(ROOT)}")
    else:
        path.write_text(TEMPLATE.format(date=d.isoformat()), encoding="utf-8")
        print(f"Tạo mới: {path.relative_to(ROOT)}")

    if not args.no_open:
        try:
            os.startfile(str(path))
        except Exception as e:
            print(f"(Không mở được editor: {e})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
