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

## [2026-06-16] init | Pipeline transcribe ghi âm

Set up Whisper STT pipeline cho hệ thống vault:
- Cài `faster-whisper` + `imageio-ffmpeg` (Python 3.12).
- Tạo cấu trúc `raw/audio/` (drop zone) + `raw/audio/processed/` (đã xử lý) + `raw/conversations/` (transcript md).
- Viết `tools/transcribe.py` — model large-v3, int8 CPU, anti-hallucination params (condition_on_previous_text=False, repetition_penalty=1.2, no_repeat_ngram_size=3, temperature fallback).
- Cập nhật `CLAUDE.md`: thêm convention `wiki/person/` (page type mới, tách khỏi entity/), workflow ingest cho conversation transcript, tips xử lý homophone tiếng Việt.

## [2026-06-16] ingest | xem-tu-vi-le-quang-lang-2019

Nguồn mới (lần đầu type=conversation): ghi âm 5 phút buổi xem tử vi của Sơn với thầy Lê Quang Lăng năm 2019.
Đây cũng là lần đầu wiki có mảng cá nhân/tử vi — trước đó chỉ tập trung kinh doanh kính mắt.

Tạo mới:
- `wiki/source/xem-tu-vi-le-quang-lang-2019.md` — tóm tắt 5 điểm chính
- `wiki/person/son.md` — hồ sơ chính chủ wiki (lần đầu tạo person page)
- `wiki/person/le-quang-lang.md` — hồ sơ thầy
- `wiki/concept/la-so-tu-vi-son.md` — bản tổng hợp các cung và sao trên lá số

Cập nhật: `wiki/overview.md` (thêm đoạn về ngách cá nhân/tử vi), `wiki/index.md` (thêm section Persons mới).

Lưu ý chất lượng: Whisper transcript có nhiều lỗi homophone với thuật ngữ tử vi (Thiên phố→Thiên Phủ, Tiến Hình→Thiên Hình, v.v.) đã sửa silently khi chắc; các chỗ không chắc đánh dấu `(?)` để Sơn review sau. Đoạn 00:00-00:38 và 05:32-06:02 là hallucination (intro/outro nhạc YouTube) đã bỏ qua khi ingest.

## [2026-06-16] init | 4 capture pipelines mới + Mission section trong CLAUDE.md

Mở rộng vault từ knowledge base kinh doanh thành "second brain" tổng quát (theo declaration của Sơn). Tạo:
- `tools/new_daily.py` — daily note pipeline (raw/daily/YYYY-MM-DD.md)
- `tools/ingest_url.py` — web + YouTube ingest (raw/web/) bằng trafilatura + youtube-transcript-api
- `tools/ingest_pdf.py` — PDF text extraction (raw/pdf/) bằng pypdf
- `tools/lint_wiki.py` — automated lint: broken wikilinks, orphans, stubs, missing frontmatter, term suggestions
- raw/daily/, raw/web/, raw/pdf/, raw/images/ folders
- Windows scheduled task `SonBrain_WeeklyLint` chạy lint mỗi Chủ nhật 9 AM

CLAUDE.md: thêm Mission section, Capture pipelines section, Workflow Ingest daily, Workflow Lint 2 layer, tips theo source type, mở rộng directory layout.

## [2026-06-16] lint | First automated lint run

Layer 1 lint phát hiện: 4 broken wikilinks (3 placeholder analysis links + 1 template page-name), 6 stub pages (Obsidian empty notes — leave for Sơn review), 8 capitalized term candidates không có page riêng (chủ yếu thuật ngữ tử vi).

Đã fix: 4 broken wikilinks → 0. Tạo `wiki/concept/tu-vi-dau-so-glossary.md` gom các thuật ngữ tử vi (12 cung + chính tinh + sao phụ + Tuần/Triệt).

## [2026-06-16] ingest | tu-vi-dau-so-wikipedia (test pipeline URL)

Test end-to-end của `ingest_url.py` với bài Wikipedia VN về Tử Vi Đẩu Số. Pipeline: fetch → trafilatura extract → frontmatter + body → raw/web/.

Phát hiện 1 bug: trafilatura `with_metadata=True` gây duplicate frontmatter inside body — đã fix thành `with_metadata=False`.

Tạo `wiki/source/tu-vi-dau-so-wikipedia.md`. Mở rộng `wiki/concept/tu-vi-dau-so-glossary.md` thêm section "Nguồn gốc" (Ngũ thuật, so sánh chiêm tinh phương Tây). Index updated.

## [2026-06-16] init | OCR pipeline (B2)

Cài `easyocr` 1.7.2 + `pypdfium2`. Tạo `tools/ocr_image.py` (batch OCR images → raw/images/text/). Mở rộng `tools/ingest_pdf.py` thêm `--ocr` flag: detect scanned PDF (<100 chars/page extract) → fallback rasterize pages bằng pypdfium2 + OCR bằng EasyOCR (vi+en). CLAUDE.md updated pipeline 4-5.

## [2026-06-16] ingest | Triết lý làm việc của Sơn (north star)

Sơn declare triết lý làm việc + mục tiêu cuối ("sống tự do = kinh doanh tự vận hành"). Tách thành `wiki/concept/triet-ly-lam-viec-son.md` — north star cho mọi quyết định business của Sơn và mọi recommendation của LLM. Update son.md, he-thong-ban-hang-8-2.md, sop-ban-hang-cua-hang.md, kinh-mat-viet-han.md, overview.md, index.md để cross-link.

Phát hiện 1 tension đáng theo dõi: [[kinh-mat-viet-han]] hiện phụ thuộc nhiều vào Sơn (đo mắt = chuyên môn khúc xạ) → rào cản tự do; đã flag trong page Việt Hàn để Sơn cân nhắc đào tạo nhân viên hoặc tăng tốc pivot sang [[kinh-mat-soni]].

Lưu feedback memory `feedback-collab-style-son.md`: 6 quy tắc collab (nói thẳng, ưu tiên SOP-able, automation, đo được, khách lợi gì, chân thành) áp cho mọi conversation tương lai.

## [2026-06-16] ingest | Personal info enrichment

Sơn cung cấp thông tin cá nhân đầy đủ. Cập nhật:
- `wiki/person/son.md` — overhaul: tên đầy đủ Nguyễn Văn Sơn, sinh 10/07/1998 tại Hợp Lý-Phú Thọ, học Trường Sĩ Quan Thông Tin, chuyên môn khúc xạ nhãn khoa, sở thích (đá bóng, phát triển bản thân, giàu có, tự do, ham học), thêm 3 link tới gia đình
- Tạo `wiki/person/nguyen-hong-thuy.md` (vợ, sinh 15/11/2002)
- Tạo `wiki/person/nguyen-tue-an.md` (con gái, sinh 04/01/2023)
- Tạo `wiki/person/nguyen-tung-anh.md` (con trai, sinh 11/11/2024)
- `wiki/entity/kinh-mat-viet-han.md` — thêm địa chỉ Tổ 11, Gia Tân, Quang Minh, Hà Nội + note Sơn phụ trách đo mắt do có chuyên môn khúc xạ
- `wiki/concept/la-so-tu-vi-son.md` — thêm section "Thông tin lập lá số" (DOB 10/07/1998, nơi sinh; giờ sinh còn thiếu để dựng lại lá số đầy đủ)
- `wiki/index.md` — section Persons có 6 entries
- Memory `user-son-profile.md` refresh với tên đầy đủ, gia đình, profile cá nhân.

## [2026-06-16] lint | Layer 2 sweep

Quét semantic level toàn wiki (29 pages):

Áp dụng:
- Move `wiki/entity/pham-thanh-long.md` → `wiki/person/pham-thanh-long.md` (consistency với convention person/ mới). Mở rộng nội dung: link tới [[chot-don]], [[vpd-hinh-tron-hinh-vuong]], [[sop-ban-hang-cua-hang]], note skill ips-cmo.
- Thêm cross-ref [[pham-thanh-long]] từ `concept/chot-don.md`.
- Đánh dấu date "tính đến 2026-06-15" cho số liệu doanh thu 30tr trong `entity/he-sinh-thai-kinh-mat.md` và `entity/kinh-mat-viet-han.md` để không bị superseded silently.
- Xóa 6 stub source pages (welcome, chao-mung, untitled, affitor, echoes-of-time, silent-film-funny-fails, longpt-setup-guide) — bản gốc Obsidian rỗng, đã xác nhận với Sơn.
- Tạo `wiki/concept/chot-don.md` tách từ Bước 6 của 8+2 (chủ đề riêng, đã xuất hiện 4 page).

Còn lại (cần Sơn quyết):
- Data gap khóa IPS — chưa có nguồn nào, đang chỉ là chú thích trong [[vpd-hinh-tron-hinh-vuong]]
- Data gap tỷ lệ chuyển đổi từng bước 8+2 — [[he-thong-ban-hang-8-2]] liệt kê metric cần đo nhưng chưa có số thực
- "Doctor Eye Health" — channel reference trong [[marketing-content-strategy]], có nên tạo entity stub không?
