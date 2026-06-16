"""OCR images in raw/images/ to markdown in raw/images/text/.

Uses EasyOCR with Vietnamese + English models. First run downloads ~200MB of model weights.

Usage:
  python tools/ocr_image.py                      # all new images in raw/images/
  python tools/ocr_image.py path/to/image.png    # specific image
  python tools/ocr_image.py --lang vi,en,ja      # custom language set (default: vi,en)
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "raw" / "images"
OUT_DIR = IMG_DIR / "text"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp"}


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


def ocr_one(img_path: Path, reader) -> Path:
    slug = slugify(img_path.stem)
    out_path = OUT_DIR / f"{slug}.md"

    if out_path.exists():
        print(f"  skip (already OCR'd): {out_path.name}")
        return out_path

    print(f"  OCR {img_path.name} ...")
    # EasyOCR returns list of (bbox, text, confidence)
    results = reader.readtext(str(img_path), detail=1, paragraph=False)

    if not results:
        print(f"  CẢNH BÁO: EasyOCR không phát hiện text trong {img_path.name}")
        return out_path

    # Group results by approximate line (y-coordinate)
    # bbox is [[tl], [tr], [br], [bl]] — use top-left y
    lines = []
    last_y = None
    line_buf = []
    for bbox, text, conf in results:
        y = (bbox[0][1] + bbox[3][1]) / 2  # center y
        if last_y is not None and abs(y - last_y) > 15:
            lines.append(line_buf)
            line_buf = []
        line_buf.append((bbox[0][0], text, conf))  # use top-left x for sorting
        last_y = y
    if line_buf:
        lines.append(line_buf)

    # Within each line, sort left-to-right
    text_lines = []
    low_conf = []
    for line in lines:
        line.sort(key=lambda t: t[0])
        line_text = " ".join(t[1] for t in line)
        text_lines.append(line_text)
        for t in line:
            if t[2] < 0.6:
                low_conf.append((t[1], round(t[2], 2)))

    body = "\n\n".join(text_lines)
    avg_conf = sum(r[2] for r in results) / len(results)

    fm = [
        "---",
        f"date: {date.today().isoformat()}",
        "type: ocr-image",
        f"source_image: {img_path.name}",
        f"ocr_engine: easyocr",
        f"avg_confidence: {round(avg_conf, 3)}",
        f"num_segments: {len(results)}",
        "---",
    ]
    out = "\n".join(fm) + f"\n\n# OCR: {img_path.stem}\n\n{body}\n"

    if low_conf:
        out += f"\n\n## Đoạn confidence thấp (<0.6) — cần verify\n\n"
        for txt, c in low_conf[:20]:
            out += f"- `{txt}` ({c})\n"

    out_path.write_text(out, encoding="utf-8")
    print(f"  -> {out_path.relative_to(ROOT)}  (avg conf {avg_conf:.2f}, {len(results)} segments)")
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="Specific image file (optional)")
    ap.add_argument("--lang", default="vi,en", help="Comma-separated EasyOCR langs (default: vi,en)")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.file:
        p = Path(args.file)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        targets = [p]
    else:
        targets = sorted(p for p in IMG_DIR.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTS)

    if not targets:
        print(f"Không có image mới trong {IMG_DIR}")
        return 0

    langs = [s.strip() for s in args.lang.split(",") if s.strip()]
    print(f"Loading EasyOCR ({'+'.join(langs)}) — lần đầu sẽ tải ~200MB model")

    import easyocr
    reader = easyocr.Reader(langs, gpu=False)

    print(f"Tìm thấy {len(targets)} image")
    for img in targets:
        try:
            ocr_one(img, reader)
        except Exception as e:
            print(f"  LỖI {img.name}: {e}")
            continue

    print("Xong.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
