# Log

Append-only record of ingests, queries, and maintenance passes.
Format: `## [YYYY-MM-DD] <operation> | <title>`

---

## [2026-05-04] init | Wiki initialized

Scaffolded wiki structure: `raw/`, `wiki/`, `CLAUDE.md`, `wiki/index.md`, `wiki/log.md`.

## [2026-05-04] ingest | tong_hop_du_an_son

Ingested: `raw/tong_hop_du_an_son.md` — tài liệu chiến lược tổng hợp toàn bộ dự án Sơn.
Tạo mới: 6 trang wiki (1 source, 2 entity, 2 concept, cập nhật overview + index).
Chủ đề chính: kinh doanh kính mắt online-first, funnel bán hàng, marketing AI, 2 kênh YouTube.

## [2026-05-04] init | Tools installed

Installed Python 3.12.9 + packages: matplotlib, pandas, requests, beautifulsoup4, rank-bm25.
Created `tools/search.py` — BM25 full-text search over wiki pages.
Node.js v20 and ripgrep already available on system.
