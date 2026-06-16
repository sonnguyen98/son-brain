"""Lint the wiki — find orphans, broken wikilinks, stubs, missing frontmatter, repeated terms without their own page.

Usage:
  python tools/lint_wiki.py                  # full report
  python tools/lint_wiki.py --section orphans  # one section only
  python tools/lint_wiki.py --quiet           # only summary line
"""
import argparse
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

WIKILINK = re.compile(r"\[\[([a-z0-9\-]+)(?:\|[^\]]*)?\]\]")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]+`")
STUB_THRESHOLD = 300  # chars (excluding frontmatter)

SKIP_PAGES = {"index", "log", "overview", "lint-report"}  # don't lint as content pages


def collect_pages() -> dict[str, dict]:
    """Returns {slug: {path, raw, body, frontmatter_present, outbound_links}}."""
    pages = {}
    for md in WIKI.rglob("*.md"):
        slug = md.stem
        raw = md.read_text(encoding="utf-8", errors="replace")
        m = FRONTMATTER.match(raw)
        if m:
            body = raw[m.end():]
            frontmatter = m.group(1)
        else:
            body = raw
            frontmatter = None
        # Strip code blocks/inline code so wikilinks inside them don't count
        scan = FENCED_CODE.sub("", raw)
        scan = INLINE_CODE.sub("", scan)
        outbound = set(WIKILINK.findall(scan))
        pages[slug] = {
            "path": md.relative_to(ROOT),
            "raw": raw,
            "body": body,
            "frontmatter": frontmatter,
            "outbound": outbound,
            "type_dir": md.parent.name if md.parent != WIKI else "_root",
        }
    return pages


def check_broken_wikilinks(pages: dict) -> list[tuple[str, str]]:
    """Returns list of (source_page, broken_target)."""
    known = set(pages.keys())
    out = []
    for slug, info in pages.items():
        for target in info["outbound"]:
            if target not in known:
                out.append((slug, target))
    return sorted(out)


def check_orphans(pages: dict) -> list[str]:
    """Pages with no inbound wikilinks (excluding index/log/overview)."""
    inbound = Counter()
    for info in pages.values():
        for target in info["outbound"]:
            inbound[target] += 1
    return sorted(
        slug for slug in pages
        if slug not in SKIP_PAGES and inbound[slug] == 0
    )


def check_stubs(pages: dict) -> list[tuple[str, int]]:
    """Pages with body < STUB_THRESHOLD chars."""
    out = []
    for slug, info in pages.items():
        if slug in SKIP_PAGES:
            continue
        body_len = len(info["body"].strip())
        if body_len < STUB_THRESHOLD:
            out.append((slug, body_len))
    return sorted(out, key=lambda x: x[1])


def check_missing_frontmatter(pages: dict) -> list[str]:
    """Pages without YAML frontmatter."""
    return sorted(
        slug for slug, info in pages.items()
        if slug not in SKIP_PAGES and info["frontmatter"] is None
    )


def check_repeated_terms(pages: dict) -> list[tuple[str, int]]:
    """Terms appearing in many pages but having no dedicated page.

    Heuristic: 2+ word capitalized phrases or quoted terms appearing in ≥3 pages
    where no page slug roughly matches them.
    """
    # Collect candidate terms — capitalized 2-3 word phrases (Vietnamese-friendly)
    # Skip common headers like "Tóm tắt", "Bối cảnh", etc.
    HEADER_NOISE = {
        "Tóm Tắt", "Bối Cảnh", "Quan Hệ", "Mốc Thời", "Thời Gian",
        "Open Questions", "Hành Động", "Phong Cách", "Câu Hỏi",
    }
    candidate_counter = Counter()
    candidate_pages = defaultdict(set)
    pattern = re.compile(r"\b([A-ZÀ-Ỹ][a-zà-ỹ]+(?:\s+[A-ZÀ-Ỹ][a-zà-ỹ]+){1,2})\b")
    for slug, info in pages.items():
        if slug in SKIP_PAGES:
            continue
        for m in pattern.finditer(info["body"]):
            term = m.group(1)
            if term in HEADER_NOISE:
                continue
            candidate_counter[term] += 1
            candidate_pages[term].add(slug)

    known_slugs = set(pages.keys())

    def slug_match(term: str) -> bool:
        s = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
        if s in known_slugs:
            return True
        # Partial — any known slug contains all words
        words = s.split("-")
        for k in known_slugs:
            if all(w in k for w in words):
                return True
        return False

    out = []
    for term, count in candidate_counter.most_common():
        if len(candidate_pages[term]) >= 3 and not slug_match(term):
            out.append((term, len(candidate_pages[term])))
    return out[:20]  # top 20


def render_report(pages: dict, sections: set[str]) -> str:
    lines = ["# Wiki Lint Report\n"]
    lines.append(f"Đã quét {len(pages)} pages trong `{WIKI.relative_to(ROOT)}`.\n")

    if "broken" in sections:
        broken = check_broken_wikilinks(pages)
        lines.append(f"\n## Broken wikilinks ({len(broken)})\n")
        if not broken:
            lines.append("Không có. ✓")
        else:
            for src, tgt in broken:
                lines.append(f"- [[{src}]] → `[[{tgt}]]` (target không tồn tại)")

    if "orphans" in sections:
        orphans = check_orphans(pages)
        lines.append(f"\n## Orphan pages — không có ai link tới ({len(orphans)})\n")
        if not orphans:
            lines.append("Không có. ✓")
        else:
            for slug in orphans:
                lines.append(f"- [[{slug}]] ({pages[slug]['path']})")

    if "stubs" in sections:
        stubs = check_stubs(pages)
        lines.append(f"\n## Stub pages — body < {STUB_THRESHOLD} ký tự ({len(stubs)})\n")
        if not stubs:
            lines.append("Không có. ✓")
        else:
            for slug, n in stubs:
                lines.append(f"- [[{slug}]] — {n} ký tự ({pages[slug]['path']})")

    if "frontmatter" in sections:
        missing = check_missing_frontmatter(pages)
        lines.append(f"\n## Thiếu frontmatter ({len(missing)})\n")
        if not missing:
            lines.append("Không có. ✓")
        else:
            for slug in missing:
                lines.append(f"- [[{slug}]] ({pages[slug]['path']})")

    if "terms" in sections:
        terms = check_repeated_terms(pages)
        lines.append(f"\n## Cụm từ xuất hiện ≥3 page mà chưa có page riêng ({len(terms)})\n")
        if not terms:
            lines.append("Không có. ✓")
        else:
            lines.append("(Gợi ý — có thể là entity/concept đáng có page riêng:)\n")
            for term, n in terms:
                lines.append(f"- **{term}** — xuất hiện ở {n} page")

    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--section", choices=["broken", "orphans", "stubs", "frontmatter", "terms", "all"], default="all")
    ap.add_argument("--quiet", action="store_true", help="Chỉ in summary 1 dòng")
    ap.add_argument("--save", action="store_true", help="Lưu report vào wiki/lint-report.md")
    args = ap.parse_args()

    if not WIKI.exists():
        print(f"Không tìm thấy {WIKI}")
        return 1

    pages = collect_pages()
    sections = {"broken", "orphans", "stubs", "frontmatter", "terms"} if args.section == "all" else {args.section}

    if args.quiet:
        b = len(check_broken_wikilinks(pages))
        o = len(check_orphans(pages))
        s = len(check_stubs(pages))
        f = len(check_missing_frontmatter(pages))
        print(f"Lint: {len(pages)} pages | broken={b} orphan={o} stub={s} no-frontmatter={f}")
        return 0

    report = render_report(pages, sections)
    print(report)

    if args.save:
        out = WIKI / "lint-report.md"
        out.write_text(report, encoding="utf-8")
        print(f"\nĐã lưu: {out.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
