---
title: Course MOC template
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Course MOC template

## Trước đó

[[05-source-page-template]] — source page schema OK.

---

## MOC là gì

**MOC** = **Map of Content** — page tổng quan 1 chủ đề lớn (1 chương trình đào tạo, 1 dự án), liệt mọi page con liên quan.

Course MOC = MOC cho 1 chương trình đào tạo:
- Định vị khoá học
- Cấu trúc khoá (modules / story / topic)
- Phiên bản đã ingest
- Cases học viên signature
- Tài sản đã sản xuất

Course MOC là **hub** trong graph view — concept page liên kết quanh nó.

Không phải mọi vault cần Course MOC. Vault knowledge cá nhân không có khoá đào tạo → skip section này.

---

## Khi nào tạo Course MOC

- Bạn là coach/trainer có chương trình đào tạo cụ thể
- Bạn dạy 1 khoá nhiều phiên bản qua thời gian
- Bạn muốn track concept nào dùng ở khoá nào

Vd:
- PTL có 34 khoá → 34 Course MOC
- Bạn dạy 1 khoá "Email Marketing Basics" → 1 Course MOC

---

## Template đầy đủ

```markdown
---
type: concept
tags: [chuong-trinh, course/<code>, <theme-tags>]
program_code: <CODE>
parent: "[[Hệ sinh thái đào tạo của bạn]]"
sources: [...]
created: 2026-05-29
updated: 2026-05-29
---

# <CODE> — <Tên đầy đủ>

[1-2 đoạn — định vị khoá: ai cho ai, dạy gì, format]

## Định vị

[3-5 bullet — USP khoá học]

## Vai trò trong hệ sinh thái

[Link upstream/downstream/song-song courses]

- **Upstream** (học trước khoá này): [[Course A]]
- **Downstream** (học sau khoá này): [[Course B]]
- **Song song** (cùng level, đi cặp): [[Course C]]

## Cấu trúc khoá

[3-5 ngày / 12 buổi / 6 module — tuỳ format]

- Ngày 1: ...
- Ngày 2: ...
- Ngày 3: ...

## Modules / Khái niệm cốt lõi

[Wikilink mỗi module/concept dạy trong khoá]

- [[Concept 1]] — vai trò trong khoá
- [[Concept 2]] — ...
- [[Concept N]]

## Stories / Ngụ ngôn dùng

- [[Story 1]] — dùng để illustrate concept X
- [[Story 2]] — ...

## Topics liên quan

- [[Topic 1]]
- [[Topic 2]]

## Cases học viên signature

- [[Học viên A]] — case nổi bật
- [[Học viên B]]

## Tài sản đã sản xuất

- Sale page: <URL>
- Lead page: <URL>
- Video promo: <URL>
- Email sequence: ... emails

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 21 | SSS 21 | 2025-11-28 | [[SSS 21 - Ngày 1 (28-11-2025)]] (+ D2/D3) | Mới nhất |
| 19 | SSS 19 | 2024-10-11 | [[SSS 19 - HN (11-10-2024)]] | Lần đầu pivot LonGPT |
| 10 | SSS 10 | 2020-07-15 | [[SSS 10 - Ngày 1 (15-07-2020)]] | Hệ thống hoá đủ 8+2 |

## Khoá học liên quan

- [[Course X]] — concept overlap
- [[Course Y]]

## Câu hỏi mở

- ?
```

---

## Giải thích từng section

### Frontmatter

```yaml
---
type: concept                                    # MOC type concept (graph view nhìn như hub concept)
tags: [chuong-trinh, course/sss, ban-hang]      # bắt buộc chuong-trinh + course/<code>
program_code: SSS                                # code duy nhất
parent: "[[Hệ sinh thái đào tạo PTL]]"           # link lên root
sources: ["[[SSS 21 - Ngày 1 (28-11-2025)]]", ...] # list source signature
---
```

#### `program_code`

Mã code duy nhất, chữ thường + gạch nối:
- `sss` — Sales Success System
- `ips` — Internet Power System
- `dtsgc` — Đánh Thức Sự Giàu Có
- `ec` — Eagle Camp

Code dùng để:
- Tag `course/<code>` trên concept đa khoá
- Filter graph view
- Filename không gian cho source page

#### Tag `chuong-trinh`

Tag chính của course page. Graph view color group dùng tag này render hub đỏ/cam.

### Tiêu đề H1

Format: `<CODE> — <Tên đầy đủ>`

Vd: `SSS — Sales Success System`

### Định vị

USP của khoá:
- Cho ai (target persona)
- Dạy gì (modules chính)
- Format (online / offline / hybrid, mấy ngày)
- Giá (tuỳ chọn — anh Long không public giá)

Vd:
```
- **Target**: Doanh chủ vừa và nhỏ, đội sales 5-20 người
- **Dạy**: Hệ thống bán hàng 8+2 + 14 chiến lược lead gen + 7 kỹ thuật xử lý từ chối
- **Format**: 3 ngày offline (T2-T4) hội trường Hà Nội/HCM, ~700 attendees
- **Phiên bản hiện tại**: SSS 23 (2026-Q3), giá liên hệ
```

### Vai trò trong hệ sinh thái

Quan trọng nhất. Map khoá vào graph lớn:
- **Upstream**: học trước khoá này (vd: DTSGC trước SSS)
- **Downstream**: học sau (vd: SSS xong → IPS)
- **Song song**: cùng level (vd: SSS song song MAP)

### Cấu trúc khoá

Chia theo format:
- 3 ngày → 3 mục Ngày 1/2/3
- 6 module → 6 mục Module 1-6
- 12 buổi → 12 mục

Mỗi mục liệt main concept dạy.

### Modules / Khái niệm cốt lõi

**Bắt buộc** — link mọi concept dạy trong khoá:

```
- [[Hệ thống bán hàng 8+2]] — module chính, 12 giờ
- [[14 chiến lược lead generation]] — bổ trợ, 4 giờ
- [[7 kỹ thuật xử lý từ chối]] — practice live, 3 giờ
```

Mỗi link concept → course → bắt buộc link ngược concept → course ở concept page section "Khoá học sử dụng".

### Stories / Ngụ ngôn dùng

Link story page (`wiki/stories/`):

```
- [[Gã ăn mày giàu có]] — illustrate "đầu tư vào bản thân"
- [[Cô gái tóc dài]] — illustrate "thay đổi mindset"
```

### Topics liên quan

```
- [[Tâm lý khách hàng B2B]]
- [[Persona doanh chủ Việt Nam]]
```

### Cases học viên signature

```
- [[Anna Nguyễn]] — chuyển từ -50% YoY sang +200%
- [[Mr. T]] — vận hành team 30 sale rep
```

### Tài sản đã sản xuất

Link ra sale page, lead page, video promo, email sequence:

```
- Sale page: https://sss.long.vn (current)
- Sale page cũ: https://sss-2024.long.vn (archived)
- Lead page: https://sss.long.vn/lp/test-30s
- Video promo: https://youtu.be/abc123
- Email sequence: 12 emails (xem [[../Longpt's Marketing/wiki/assets/email/sss-onboarding-sequence]])
```

### Phiên bản đã ingest

Bảng timeline:

```markdown
| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 21 | SSS 21 | 2025-11-28 | [[SSS 21 - Ngày 1]] | Mới nhất, thêm 14 lead gen |
| 19 | SSS 19 | 2024-10-11 | [[SSS 19 - HN]] | Lần đầu pivot LonGPT |
```

Khi ingest source mới → add row mới.

### Khoá học liên quan

Cross-link course khác. Tránh trùng "Vai trò trong hệ sinh thái" — section này list khoá overlap concept, không phải up/down/parallel.

```
- [[BHTC - Bán Hàng Thành Công]] — nền tảng lịch sử (12/2012), tiền thân SSS
- [[Eagle Camp]] — concept Hot Seat từ EC dùng trong SSS
```

### Câu hỏi mở

Gap chưa biết về khoá:

```
- SSS phiên bản 22 có gì khác 21? (chưa ingest)
- Có version online ngắn 6h thay vì 3 ngày? (chưa rõ)
```

---

## Quy tắc 2 chiều (nhất quán)

Mỗi link course → concept (trong "Modules") **phải có** link ngược concept → course (trong "Khoá học sử dụng" của concept page).

Vd:
- `SSS - Sales Success System.md` có `## Modules — [[Hệ thống bán hàng 8+2]]`
- → `Hệ thống bán hàng 8+2.md` phải có `## Khoá học sử dụng — [[SSS - Sales Success System]]`

Lint pass sẽ check và flag bất nhất.

---

## Concept đa khoá

Concept dùng ở **nhiều khoá** → tag `course/<code>` đa khoá:

```yaml
tags: [framework, course/sss, course/bhtc, course/raving-fan, signature]
```

Và section "Khoá học sử dụng" liệt cả 3:

```
## Khoá học sử dụng
- [[SSS - Sales Success System]] — module chính (12h)
- [[BHTC - Bán Hàng Thành Công]] — tiền thân, dạy lần đầu 12/2012
- [[RAVING FAN]] — mở rộng sang giai đoạn after-sales
```

Graph view: concept ngồi giữa 3 course hub → render đẹp.

---

## Course MOC cha — Hệ sinh thái

Nếu bạn có 5+ khoá → tạo MOC cha "Hệ sinh thái đào tạo của bạn":

```markdown
# Hệ sinh thái đào tạo

## Nhóm khoá cốt lõi
- [[SSS]] — bán hàng
- [[IPS]] — marketing online

## Nhóm khoá bổ trợ
- [[VM28]] — video marketing
- [[BHTC]] — bán hàng nền tảng

## Coaching weekly
- [[Eagle Club]] — 1 năm
- [[IPS Coach]] — 6 tháng
```

Mỗi course MOC có frontmatter `parent: "[[Hệ sinh thái đào tạo của bạn]]"` → graph render hierarchy.

---

## Test với Claude

```
> Tạo course MOC giả cho khoá "Email Marketing Mastery" (code: EMM) theo template.
> Định vị: dạy email marketing cho freelancer + agency.
> Format: 4 module online, mỗi module 2h.
> Stub những phần chưa có data.
> Lưu vào wiki/courses/EMM - Email Marketing Mastery.md
```

Claude tạo file → mở Obsidian xem template đúng chưa.

---

## Tiếp theo

Đọc tiếp: [[07-ingest-source-dau-tien]] — Ingest source đầu tiên cùng Claude.
