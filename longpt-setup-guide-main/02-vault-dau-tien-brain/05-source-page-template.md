---
title: Source page template
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Source page template

## Trước đó

[[04-concept-page-template]] — concept page schema OK.

---

## Source page là gì

Source page = 1 file tóm tắt cho **1 source raw** đã ingest. Là **snapshot tại thời điểm ingest** — không update theo source mới.

Source page khác concept page:

| Source page | Concept page |
|---|---|
| 1 file mỗi source | 1 file mỗi khái niệm |
| Snapshot, ingest 1 lần | Update liên tục theo source mới |
| Tóm tắt nội dung gốc | Tổng hợp xuyên source |
| Provenance + line ref | Định nghĩa + cấu trúc |

Source page **phụ trợ** concept page. Concept page là chính.

---

## Template đầy đủ

```markdown
---
type: source
tags: [source-<kind>, <theme-tags>]
created: 2026-05-29
updated: 2026-05-29
raw_path: raw/articles/2026-05-29-paul-graham-product-engineer.md
author: "Paul Graham"
date: 2024-10
url: https://paulgraham.com/pmf.html
language: en
duration: (nếu là video/audio)
location: (nếu là khoá học)
program_code: (nếu là khoá học)
version_number: (nếu là khoá học)
version_date: (nếu là khoá học)
parent_course: "[[<Course MOC>]]" (nếu là khoá học)
---

# Tên source — kèm bối cảnh

[1 dòng tóm tắt source là gì + kỳ + tác giả]

## TL;DR

[3-5 bullet — ý chính nhất]

## Nội dung chính

[Tóm tắt 3-5 đoạn theo cấu trúc gốc của source]

## Concept đã touch / dạy

- [[Concept A]] — đoạn line X (~timecode/page)
- [[Concept B]] — đoạn line Y

## Entity nhắc đến

- [[Entity X]] — vai trò trong source
- [[Entity Y]]

## Quote signature

> "Quote nguyên văn từ source"
>
> — Author / location / line ref

## Câu chốt rút ra

[1-2 takeaway lớn nhất từ source này]

## Mâu thuẫn (nếu có)

[Source mới mâu thuẫn source cũ — ghi rõ]

## Câu hỏi mở

- ?
```

---

## Giải thích từng section

### Frontmatter

```yaml
---
type: source                                    # bắt buộc
tags: [source-article, marketing]               # bắt buộc
created: 2026-05-29                             # bắt buộc — ngày ingest
updated: 2026-05-29                             # bắt buộc
raw_path: raw/articles/2026-05-29-paul-graham.md # bắt buộc — link về raw
author: "Paul Graham"                           # bắt buộc khi có
date: 2024-10                                   # ngày source được tạo (khác `created`)
url: https://paulgraham.com/pmf.html            # nếu có
language: en                                    # ngôn ngữ source
---
```

#### Tags `source-<kind>`

`<kind>` là loại source:
- `source-article` — bài web
- `source-transcript` — transcript video
- `source-book` — sách
- `source-podcast` — podcast
- `source-pdf` — PDF
- `source-meeting` — meeting note
- `source-photo` — ảnh đơn lẻ (rare)

#### Frontmatter mở rộng cho khoá đào tạo

```yaml
---
type: source
tags: [source-transcript, version, course/sss]
program_code: SSS
version_number: 21
version_date: 2025-11-28
location: "Hà Nội"
parent_course: "[[SSS - Sales Success System]]"
duration: "8h"
attendees: 700
raw_path: raw/SSS/20251128-SSS-21-HaNoi/D1-chunks/
---
```

Phụ trợ versioning concept theo phiên bản (xem [[02-vault-dau-tien-brain/06-course-moc-template]]).

### Tiêu đề H1

Tên source + bối cảnh:
- Article: `Paul Graham — Product Engineer (2024-10)`
- Transcript khoá: `SSS 21 - Ngày 1 (28-11-2025)`
- Sách: `Atomic Habits — James Clear (2018)`
- Podcast: `Lex Fridman #245 — Sam Altman (2021-09)`

### TL;DR

3-5 bullet ý chính nhất. Đọc TL;DR → biết source nói gì.

Ví dụ:
```
- Product engineer = breed mới: vừa technical vừa product taste
- Khác data engineer (data structure) + designer (UX) ở chỗ build feature end-to-end
- Hiếm vì cần training cả 2 mặt
- Khi tìm được — pay 2-3× lương trung bình
- YC pivot tuyển product engineer thay vì designer + engineer riêng
```

### Nội dung chính

Tóm tắt 3-5 đoạn theo cấu trúc gốc.

Quy tắc:
- KHÔNG copy nguyên văn (bản quyền + token waste)
- Giữ điểm chính, lược bỏ ví dụ thừa
- Cite concept bằng `[[wikilink]]`
- Giữ tone gốc (formal/casual)

### Concept đã touch / dạy

Liệt concept page liên quan + line ref:

```
- [[Product Engineer]] — định nghĩa, đoạn 1-2
- [[Founder DNA]] — bàn về hire pattern, đoạn 4
- [[Y Combinator playbook]] — case study YC W24 batch, đoạn 6
```

Line ref / timecode giúp trace ngược khi cần.

### Entity nhắc đến

```
- [[Paul Graham]] — tác giả
- [[Y Combinator]] — công ty
- [[Sam Altman]] — quote từ tweet, đoạn 5
```

### Quote signature

Quote đáng nhớ. Giữ nguyên văn:

```markdown
> "Product engineer is the new hot title. They're not just engineers and they're not just designers. They build the whole thing."
>
> — Paul Graham, paulgraham.com/pmf.html, paragraph 3
```

### Câu chốt rút ra

1-2 takeaway lớn nhất. Đây là phần **insight personal** từ bạn — không phải từ source.

Vd:
> "PG đúng: company hiện tại tôi hire kiểu ấy cũng không hiệu quả. Cần pivot tuyển product engineer cho 1 vị trí thử."

### Mâu thuẫn (nếu có)

Source mới khác claim source cũ → ghi rõ:

```markdown
## Mâu thuẫn

Source [[Naval Ravikant Almanack]] (2020) cho rằng "specialist > generalist" — opposite quan điểm PG.

Cách dung hoà: specialist trong technical skill, generalist trong product taste.
```

KHÔNG xoá source cũ. Ghi 2 view + suy luận hoà giải.

### Câu hỏi mở

Gap cần verify hoặc follow-up:

```
- PG nói product engineer hiếm — có dataset stats về hiring không?
- Có công ty Việt Nam nào đã pivot tuyển product engineer chưa? — search LinkedIn
```

---

## Source page cho khoá đào tạo

Đặc thù: khoá đào tạo nhiều buổi → 1 buổi 1 source page.

### Naming convention

```
<CODE> <Version> - Ngày N (<DD-MM-YYYY>).md
```

Vd:
- `SSS 21 - Ngày 1 (28-11-2025).md`
- `SSS 21 - Ngày 2 (29-11-2025).md`
- `SSS 21 - Ngày 3 (30-11-2025).md`

### Frontmatter

```yaml
---
type: source
tags: [source-transcript, version, course/sss]
program_code: SSS
version_number: 21
day_number: 1
version_date: 2025-11-28
location: "Hà Nội"
parent_course: "[[SSS - Sales Success System]]"
duration: "8h"
attendees: 700
raw_path: raw/SSS/20251128-SSS-21-HaNoi/D1-chunks/
---
```

### Section đặc thù

Ngoài template chuẩn, thêm:

```markdown
## Modules đã dạy

- [[Hệ thống bán hàng 8+2]] — module chính
- [[14 chiến lược lead generation]] — mới thêm version 21
- [[7 kỹ thuật xử lý từ chối]] — module phụ

## Case học viên / Hot seat

- [[Học viên A]] — tình huống bán hàng B2B
- [[Học viên B]] — pivot industry

## Bài tập trên hội trường

- BT 1: Viết REM-30s cho ngành của bạn (~14:00-15:00)
- BT 2: Practice 7 kỹ thuật xử lý từ chối (~16:00-17:30)

## Câu chốt PTL

> "Quote signature 1"
> 
> — đoạn 14:23

> "Quote signature 2"
>
> — đoạn 16:45
```

---

## Quy tắc cứng source page

1. **Snapshot — không update**. Source page viết 1 lần, không update theo source mới. Concept page mới là cái update.
2. **Cite line ref / timecode / page**. Cite càng cụ thể càng tốt.
3. **Provenance đầy đủ**. `raw_path` trỏ về raw chính xác. Khi raw rename / move → update source page.
4. **Không bịa quote**. Quote phải nguyên văn từ source. Sai dấu → fix lại theo source.
5. **Mâu thuẫn ghi rõ**, không im lặng overwrite.

---

## Khi source quá to (>10k dòng)

Source dài (transcript 8h khoá học, sách 500 trang) → chia chunk trước khi viết source page:

```
raw/SSS/20251128-SSS-21-HaNoi/D1-chunks/
├── chunk-001-mo-dau.txt
├── chunk-002-module-1.txt
├── chunk-003-module-2.txt
└── ...
```

Script chia chunk: dùng skill `text-cat-chunk` (chia file dài thành chunk ~15k char + YAML metadata + marker auto-detect).

Sau khi chia, source page chỉ tóm tắt high-level + link chunk:

```markdown
## Chunks
- [[chunk-001-mo-dau]] — phần mở đầu (~30 phút)
- [[chunk-002-module-1]] — module 1: ...
- ...
```

---

## Test với Claude

```
> Tạo source page cho 1 bài giả Paul Graham — "Founder Mode" (2024-10). 
> Author: Paul Graham. URL: https://paulgraham.com/foundermode.html. 
> Concept chính: Founder Mode (vs Manager Mode). Concept liên quan: Y Combinator, Steve Jobs management style.
> Lưu vào wiki/sources/.
```

Claude tạo file → review template đúng chưa.

---

## Tiếp theo

Đọc tiếp: [[06-course-moc-template]] — Course MOC (Map of Content) cho chương trình đào tạo.
