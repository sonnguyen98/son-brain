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

## [2026-06-13] reset | Wiki reset to empty state

User reorganized wiki/ pages back into raw/ via Obsidian (manual move), result was nested/messy.
Flattened moved pages into `raw/` as plain files: `echoes-of-time.md`, `he-sinh-thai-kinh-mat.md`,
`marketing-content-strategy.md`, `mo-hinh-ban-kinh-online.md`, `silent-film-funny-fails.md`,
`tong-hop-du-an-son-summary.md`. Reset `wiki/index.md` and `wiki/overview.md` to empty templates.
Wiki is now back to a clean slate, ready for re-ingest.

## [2026-06-15] ingest | He-thong-ban-hang-8+2-tong-hop.md

Nguồn mới: tổng hợp hệ thống bán hàng 8+2 của Phạm Thành Long, áp dụng cho Kính Mắt SONi (online) & Việt Hàn (offline).
Tạo mới: `wiki/source/he-thong-ban-hang-8-2-tong-hop.md`, `wiki/concept/he-thong-ban-hang-8-2.md`,
`wiki/concept/vpd-hinh-tron-hinh-vuong.md`, `wiki/entity/pham-thanh-long.md`, `wiki/entity/kinh-mat-soni.md`, `wiki/entity/kinh-mat-viet-han.md`.
Cập nhật: `wiki/entity/he-sinh-thai-kinh-mat.md` (thêm 2 thương hiệu + liên kết hệ thống 8+2).

## [2026-06-15] ingest | SOP-ban-hang-8cong2-chuan.md

Nguồn mới: cẩm nang/SOP bán hàng 6 bước tại cửa hàng Kính Mắt Việt Hàn (script chi tiết, xử lý từ chối, follow-up).
Tạo mới: `wiki/source/sop-ban-hang-8cong2-chuan.md`, `wiki/concept/sop-ban-hang-cua-hang.md`.
Liên kết với [[he-thong-ban-hang-8-2]] và [[vpd-hinh-tron-hinh-vuong]] (SOP triển khai Bước 3-8 của 8+2).

## [2026-06-15] ingest | tong-hop-du-an-son-summary.md

Bản tóm tắt cô đọng, nội dung trùng với `tong_hop_du_an_son.md` (đã ingest 2026-05-04) — có khả năng là trang wiki cũ lẫn vào raw/ khi reset.
Tạo mới: `wiki/source/tong-hop-du-an-son-summary.md` ghi chú lại quan hệ này, không tạo trùng entity/concept mới.

## [2026-06-15] ingest | echoes-of-time.md, silent-film-funny-fails.md, marketing-content-strategy.md, mo-hinh-ban-kinh-online.md, he-sinh-thai-kinh-mat.md

5 file này là các trang wiki entity/concept cũ bị đưa nhầm vào `raw/` trong lần reset 2026-06-13 (định dạng có frontmatter wiki sẵn).
Phục hồi lại đúng vị trí: `wiki/entity/echoes-of-time.md`, `wiki/entity/silent-film-funny-fails.md`,
`wiki/concept/marketing-content-strategy.md`, `wiki/concept/mo-hinh-ban-kinh-online.md`, `wiki/entity/he-sinh-thai-kinh-mat.md` (có bổ sung).
Mỗi file cũng có 1 trang `wiki/source/<slug>.md` ghi chú việc phục hồi.

## [2026-06-15] ingest | Affitor.md, Untitled.md, longpt-setup-guide.md, Chào mừng.md, Welcome.md

5 file rỗng hoặc ghi chú mặc định của Obsidian, không có nội dung kiến thức.
Tạo stub `wiki/source/affitor.md`, `wiki/source/untitled.md`, `wiki/source/longpt-setup-guide.md`,
`wiki/source/chao-mung.md`, `wiki/source/welcome.md` — đánh dấu cần người dùng review/bổ sung (3 file rỗng) hoặc không cần xử lý (2 ghi chú Obsidian).

## [2026-06-15] ingest | Cập nhật overview.md và index.md

Cập nhật `wiki/overview.md` (viết lại toàn bộ — wiki đã được khôi phục + mở rộng sau reset, thêm mảng hệ thống bán hàng 8+2)
và `wiki/index.md` (catalog đầy đủ 13 trang source, 6 entity, 5 concept).
