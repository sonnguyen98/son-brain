---
title: Cấu trúc folder
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Cấu trúc folder raw/ + wiki/

## Trước đó

[[02-claude-md-template]] — CLAUDE.md đã setup.

---

## Cấu trúc đầy đủ

```
My Brain/
├── CLAUDE.md
├── README.md
├── index.md
├── log.md
│
├── raw/
│   ├── assets/                # ảnh, PDF đính kèm
│   ├── articles/              # Web Clipper output
│   ├── transcripts/           # SRT, TXT từ video
│   ├── notes/                 # ghi chú thủ công
│   ├── photos/                # ảnh chụp iPhone
│   └── exports/               # CSV/XLSX export
│
├── wiki/
│   ├── sources/               # tóm tắt mỗi source
│   ├── concepts/              # framework / phương pháp / triết lý
│   ├── entities/              # người, tổ chức, brand
│   ├── courses/               # MOC mỗi chương trình
│   ├── stories/               # metaphor, ngụ ngôn, nhân vật ẩn dụ
│   ├── topics/                # tổng hợp xuyên source
│   ├── students/              # case học viên (nếu coach/trainer)
│   ├── analyses/              # query lưu lại
│   └── books/                 # tóm tắt sách (tuỳ chọn)
│
└── .obsidian/                 # ẩn — settings Obsidian
```

---

## raw/ — chi tiết

### `raw/assets/`

Ảnh và file binary đính kèm. Obsidian Web Clipper auto download vào đây.

Ví dụ:
```
raw/assets/article-hubspot-marketing.png
raw/assets/diagram-funnel.svg
raw/assets/founder-photo.jpg
```

### `raw/articles/`

Bài web clipped:

```
raw/articles/2026-05-29-paul-graham-product-engineer.md
raw/articles/2026-05-28-sam-altman-startup-playbook.md
```

Format: ngày + slug + `.md`.

Web Clipper config: Settings → Vault `My Brain` → Folder `raw/articles/`.

### `raw/transcripts/`

SRT, TXT từ video (YouTube transcript, Whisper output):

```
raw/transcripts/youtube-paul-graham-startup.txt
raw/transcripts/keynote-jobs-2007-stanford.srt
```

Nếu là khoá đào tạo nhiều buổi:

```
raw/SSS/20251128-SSS-21-HaNoi/
├── D1-chunks/
│   ├── chunk-001.txt
│   ├── chunk-002.txt
│   └── ...
├── D2-chunks/
└── D3-chunks/
```

Mỗi day 1 subfolder để tránh cross-day leak. Schema folder: `YYYYMMDD-Khoa-Version-Diadiem`.

### `raw/notes/`

Ghi chú thủ công bạn viết tay (vd: meeting note):

```
raw/notes/2026-05-29-call-jay-abraham.md
raw/notes/2026-05-28-brainstorm-launch.md
```

### `raw/photos/`

Ảnh iPhone:

```
raw/photos/2026-05-29/
├── IMG_1234.HEIC
├── IMG_1235.HEIC
└── IMG_1236.HEIC
```

Mỗi ngày 1 subfolder.

### `raw/exports/`

CSV/XLSX từ dashboard:

```
raw/exports/2026-W22-google-analytics.csv
raw/exports/2026-05-shopify-orders.xlsx
```

---

## wiki/ — chi tiết

### `wiki/sources/` — Source summary

1 file mỗi source đã ingest. Tóm tắt nguồn 3-5 đoạn + frontmatter + link concept đã touch.

Format file:
```
wiki/sources/Paul Graham — Product Engineer.md
wiki/sources/SSS 21 - Ngày 1 (28-11-2025).md
```

Template ở [[99-templates/source-page-template]].

### `wiki/concepts/` — Concept page

1 file mỗi khái niệm độc lập. Đây là **đơn vị lưu trữ chính**.

Format file:
```
wiki/concepts/Product Engineer.md
wiki/concepts/Hệ thống bán hàng 8+2.md
wiki/concepts/Bộ não thứ 2.md
```

Template ở [[99-templates/concept-page-template]].

### `wiki/entities/` — Entity page

1 file mỗi entity có danh tính (người, tổ chức, brand, công cụ).

Format file:
```
wiki/entities/Paul Graham.md
wiki/entities/Y Combinator.md
wiki/entities/Phạm Thành Long.md
wiki/entities/BNI HN6.md
```

Section tiêu chuẩn:
- Background
- Vai trò trong vault
- Quote signature
- Source nhắc đến

### `wiki/courses/` — Course MOC

Map of Content cho mỗi chương trình đào tạo / khoá học.

Format file:
```
wiki/courses/SSS - Sales Success System.md
wiki/courses/IPS - Internet Power System.md
```

Template ở [[99-templates/course-moc-template]].

### `wiki/stories/` — Story page

Metaphor, ngụ ngôn, nhân vật ẩn dụ signature của tác giả.

Ví dụ vault PTL:
```
wiki/stories/Gã ăn mày giàu có.md
wiki/stories/Cô gái tóc dài.md
wiki/stories/Bút chì cùn.md
```

Tag: `storytelling`, `nhan-vat-an-du`.

### `wiki/topics/` — Topic synthesis

Tổng hợp xuyên source về 1 chủ đề rộng.

Format file:
```
wiki/topics/Tâm lý khách hàng B2B.md
wiki/topics/Founder journey.md
```

### `wiki/students/` — Case học viên

(Nếu vault dành cho coach/trainer)

```
wiki/students/Anna Nguyễn.md
wiki/students/Mr. T.md
```

Section: background, lý do tham gia khoá, mục tiêu, kết quả.

### `wiki/analyses/` — Query lưu lại

Tổng hợp query đáng giữ:

```
wiki/analyses/So sánh SSS vs IPS.md
wiki/analyses/Concept đa khoá xuyên 5 chương trình.md
```

### `wiki/books/` — Tóm tắt sách (tuỳ chọn)

Nếu vault tách Books riêng → skip. Nếu gộp:

```
wiki/books/Atomic Habits.md
wiki/books/Influence.md
```

---

## Khi nào thêm subfolder mới

3 tín hiệu:

### Tín hiệu 1 — 1 loại page xuất hiện 10+ lần

Vault PTL có 10 source weekly coaching → tạo `wiki/sources/coaching-weekly/`.

### Tín hiệu 2 — Loại page có schema riêng

Page koi cá có frontmatter riêng (`size_cm`, `loai_koi`, `arrived`) khác entity thường → tách `wiki/koi/`.

### Tín hiệu 3 — Group nhằm graph view dễ đọc

Settings → Graph view → Color groups: tag `path:wiki/courses/` → đỏ → tạo cluster course dễ nhìn.

---

## Quy ước tên subfolder

- Tiếng Anh số ít hoặc số nhiều OK (chọn nhất quán)
- Số ít: `wiki/source/`, `wiki/concept/` — ít phổ thông
- Số nhiều: `wiki/sources/`, `wiki/concepts/` — Long dùng, phổ thông hơn
- Tránh viết hoa folder (`Wiki/Sources` khó type)

---

## Quy ước tên file

Mỗi loại page có pattern riêng:

| Loại | Pattern | Ví dụ |
|---|---|---|
| Source | Tiêu đề gốc | `Paul Graham — Product Engineer.md` |
| Concept | Tên concept | `Hệ thống bán hàng 8+2.md` |
| Entity | Tên đầy đủ | `Phạm Thành Long.md` |
| Course | `<CODE> - <Tên đầy đủ>.md` | `SSS - Sales Success System.md` |
| Story | Tên ngụ ngôn | `Gã ăn mày giàu có.md` |
| Analysis | Chủ đề + so sánh | `So sánh SSS vs IPS.md` |

Wikilink luôn dùng tên file: `[[Hệ thống bán hàng 8+2]]`.

---

## Cleanup khi subfolder bừa

Sau 6 tháng, có thể subfolder mất tổ chức:
- `wiki/concepts/` có 50+ concept, không phân loại
- `wiki/entities/` lẫn người + tổ chức + công cụ

Lúc đó:
- **Không refactor sớm**. Chờ pattern rõ ràng (vd: thấy rõ 20 entity là "mentor", 30 là "đối tác") rồi tách
- Tách subfolder mới: `wiki/entities/mentors/`, `wiki/entities/partners/`
- Cập nhật CLAUDE.md schema
- Lint pass để check link không vỡ

Chi tiết refactor ở [[05-bao-tri-lint/03-migrate-rename-vault]].

---

## Tiếp theo

Đọc tiếp: [[04-concept-page-template]] — Concept page template chi tiết.
