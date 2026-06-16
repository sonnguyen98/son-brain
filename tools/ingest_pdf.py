"""Extract text from PDFs in raw/pdf/ to markdown.

Usage:
  python tools/ingest_pdf.py                  # all PDFs in raw/pdf/ (text extract only)
  python tools/ingest_pdf.py <path/to/file>   # specific file (any location)
  python tools/ingest_pdf.py --ocr            # OCR fallback for scanned PDFs (EasyOCR)
  python tools/ingest_pdf.py --ocr <file>     # force OCR on one file

Output: raw/pdf/<slug>.md with frontmatter. PDF stays in place (not moved).

Default behavior: pypdf text extraction. If a PDF has <100 chars/page extracted,
it's likely scanned — re-run with `--ocr` to rasterize pages and OCR with EasyOCR.
First OCR run downloads ~200MB of EasyOCR models.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = ROOT / "raw" / "pdf"


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


def extract_text(pdf_path: Path) -> tuple[list[str], dict, int]:
    reader = PdfReader(str(pdf_path))
    meta = reader.metadata or {}
    pages = []
    total_chars = 0
    for i, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as e:
            text = f"<!-- LỖI extract trang {i}: {e} -->"
        if text.strip():
            pages.append(f"\n\n## Trang {i}\n\n{text.strip()}")
        total_chars += len(text.strip())
    return pages, dict(meta), len(reader.pages)


def ocr_pages(pdf_path: Path) -> tuple[list[str], int]:
    """OCR each page via pypdfium2 + EasyOCR. Returns (page-markdown-list, num_pages)."""
    import pypdfium2 as pdfium
    import easyocr
    import tempfile

    print(f"  loading EasyOCR (vi+en) — chậm lần đầu...")
    reader = easyocr.Reader(["vi", "en"], gpu=False)

    pdf = pdfium.PdfDocument(str(pdf_path))
    n = len(pdf)
    pages = []
    with tempfile.TemporaryDirectory() as td:
        for i in range(n):
            page = pdf[i]
            pil_image = page.render(scale=2.0).to_pil()  # 2x DPI for better OCR
            tmp_img = Path(td) / f"p{i+1}.png"
            pil_image.save(tmp_img)
            results = reader.readtext(str(tmp_img), detail=0, paragraph=True)
            text = "\n\n".join(results).strip()
            if text:
                pages.append(f"\n\n## Trang {i+1}\n\n{text}")
            print(f"    trang {i+1}/{n} — {len(text)} ký tự")
    return pages, n


def extract_one(pdf_path: Path, use_ocr: bool = False) -> Path:
    slug = slugify(pdf_path.stem)
    out_path = PDF_DIR / f"{slug}.md"

    if out_path.exists():
        print(f"  skip (already extracted): {out_path.name}")
        return out_path

    print(f"  reading {pdf_path.name} ...")
    pages, meta, n_pages = extract_text(pdf_path)
    extract_method = "pypdf"

    # Auto-detect scanned: if avg chars/page < 100, try OCR (if --ocr flag or auto)
    avg_chars = sum(len(p) for p in pages) / max(n_pages, 1)
    if not pages or avg_chars < 100:
        if use_ocr:
            print(f"  text extract trống/sparse (avg {avg_chars:.0f} chars/page) — chuyển OCR.")
            pages, _ = ocr_pages(pdf_path)
            extract_method = "easyocr"
        else:
            print(f"  CẢNH BÁO: avg {avg_chars:.0f} chars/page — có thể PDF scan. Chạy lại với --ocr để OCR.")
            if not pages:
                return out_path

    title = meta.get("/Title", pdf_path.stem) or pdf_path.stem
    author = meta.get("/Author", "")
    created = meta.get("/CreationDate", "")

    fm = [
        "---",
        f"date: {date.today().isoformat()}",
        "type: pdf",
        f"source_pdf: {pdf_path.name}",
        f"pages: {n_pages}",
        f"extract_method: {extract_method}",
    ]
    if author:
        fm.append(f"author: {author}")
    if created:
        fm.append(f"pdf_created: {created}")
    fm.append("---")

    body = f"{chr(10).join(fm)}\n\n# {title}\n" + "".join(pages) + "\n"
    out_path.write_text(body, encoding="utf-8")
    print(f"  -> {out_path.relative_to(ROOT)}  ({n_pages} trang, {extract_method})")
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="Specific PDF (optional)")
    ap.add_argument("--ocr", action="store_true", help="OCR fallback when text extract is sparse")
    args = ap.parse_args()

    PDF_DIR.mkdir(parents=True, exist_ok=True)

    if args.file:
        p = Path(args.file)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        targets = [p]
    else:
        targets = sorted(p for p in PDF_DIR.iterdir() if p.is_file() and p.suffix.lower() == ".pdf")

    if not targets:
        print(f"Không có PDF mới trong {PDF_DIR}")
        return 0

    print(f"Tìm thấy {len(targets)} PDF")
    for pdf in targets:
        try:
            extract_one(pdf, use_ocr=args.ocr)
        except Exception as e:
            print(f"  LỖI {pdf.name}: {e}")
            continue

    print("Xong.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
