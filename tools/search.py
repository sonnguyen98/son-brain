#!/usr/bin/env python3
"""BM25 search over wiki/ markdown pages. Usage: search.py <query> [--top N]"""

import sys
import os
import re
import argparse
from pathlib import Path
from rank_bm25 import BM25Okapi

WIKI_DIR = Path(__file__).parent.parent / "wiki"


def tokenize(text: str) -> list[str]:
    text = text.lower()
    text = re.sub(r"[#\[\]\(\)\*\_\-\>\`\|]", " ", text)
    return [t for t in text.split() if len(t) > 1]


def load_pages() -> list[dict]:
    pages = []
    for md in sorted(WIKI_DIR.rglob("*.md")):
        rel = md.relative_to(WIKI_DIR)
        content = md.read_text(encoding="utf-8", errors="ignore")
        title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else rel.stem
        pages.append({"path": str(rel), "title": title, "content": content})
    return pages


def search(query: str, top_n: int = 5) -> list[dict]:
    pages = load_pages()
    if not pages:
        return []
    corpus = [tokenize(p["content"]) for p in pages]
    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(tokenize(query))
    ranked = sorted(zip(scores, pages), key=lambda x: x[0], reverse=True)
    results = []
    for score, page in ranked[:top_n]:
        if score > 0:
            snippet = _snippet(page["content"], query)
            results.append({"score": round(score, 3), "path": page["path"],
                            "title": page["title"], "snippet": snippet})
    return results


def _snippet(content: str, query: str, window: int = 200) -> str:
    lower = content.lower()
    words = query.lower().split()
    best_pos = 0
    best_hits = 0
    for i in range(0, len(lower), 50):
        chunk = lower[i:i + window]
        hits = sum(1 for w in words if w in chunk)
        if hits > best_hits:
            best_hits = hits
            best_pos = i
    raw = content[best_pos:best_pos + window].replace("\n", " ").strip()
    return raw + ("…" if best_pos + window < len(content) else "")


def main():
    parser = argparse.ArgumentParser(description="Search wiki pages")
    parser.add_argument("query", nargs="+", help="Search terms")
    parser.add_argument("--top", type=int, default=5, metavar="N",
                        help="Number of results (default 5)")
    args = parser.parse_args()

    query = " ".join(args.query)
    results = search(query, args.top)

    if not results:
        print(f"No results for: {query}")
        return

    print(f"Results for: \"{query}\"\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. [{r['title']}] (wiki/{r['path']})  score={r['score']}")
        print(f"   {r['snippet']}")
        print()


if __name__ == "__main__":
    main()
