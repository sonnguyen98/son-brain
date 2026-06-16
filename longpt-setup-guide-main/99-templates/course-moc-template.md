---
title: Course MOC template
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# Course MOC template (copy-paste)

Template Course MOC (Map of Content) cho chương trình đào tạo. Copy vào `wiki/courses/<CODE> - <Tên>.md`.

---

## Template đầy đủ

```markdown
---
type: concept
tags: [chuong-trinh, course/<code>, <theme-tags>]
program_code: <CODE>
parent: "[[Hệ sinh thái đào tạo của bạn]]"
sources:
  - "[[<Source signature 1>]]"
  - "[[<Source signature 2>]]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <CODE> — <Tên đầy đủ>

<1-2 đoạn — định vị khoá: ai cho ai, dạy gì, format>

## Định vị

- **Target**: <persona đích>
- **Dạy**: <modules chính>
- **Format**: <online/offline/hybrid, mấy ngày, mấy attendees>
- **Phiên bản hiện tại**: <CODE version> (<date>)

## Vai trò trong hệ sinh thái

- **Upstream** (học trước): [[<Course A>]]
- **Downstream** (học sau): [[<Course B>]]
- **Song song** (cùng level): [[<Course C>]]

## Cấu trúc khoá

- Ngày 1: <main topic>
- Ngày 2: <main topic>
- Ngày 3: <main topic>

(Hoặc theo module nếu format khác)

## Modules / Khái niệm cốt lõi

- [[<Concept 1>]] — vai trò trong khoá
- [[<Concept 2>]] — ...
- [[<Concept N>]]

## Stories / Ngụ ngôn dùng

- [[<Story 1>]] — illustrate concept X
- [[<Story 2>]]

## Topics liên quan

- [[<Topic 1>]]
- [[<Topic 2>]]

## Cases học viên signature

- [[<Học viên A>]] — case nổi bật
- [[<Học viên B>]]

## Tài sản đã sản xuất

- Sale page: <URL>
- Lead page: <URL>
- Video promo: <URL>
- Email sequence: <N> emails

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| <N> | <CODE N> | YYYY-MM-DD | [[<Source>]] | <gì signature> |
| <N-1> | <CODE N-1> | YYYY-MM-DD | [[<Source>]] | <gì signature> |

## Khoá học liên quan

- [[<Course X>]] — concept overlap
- [[<Course Y>]]

## Câu hỏi mở

- ?
```

---

## Variant — Khoá offline 3 ngày

```markdown
---
type: concept
tags: [chuong-trinh, course/sss, ban-hang]
program_code: SSS
parent: "[[Hệ sinh thái đào tạo PTL]]"
sources:
  - "[[BHTC - Phần 1 (Livestream)]]"
  - "[[SSS 10 - Ngày 1 (15-07-2020)]]"
  - "[[SSS 21 - Ngày 1 (28-11-2025)]]"
---

# SSS — Sales Success System

Khoá đào tạo bán hàng B2C cá nhân hoá flagship của Phạm Thành Long. Dạy hệ thống 8+2 + 14 chiến lược lead gen + 7 kỹ thuật xử lý từ chối.

## Định vị

- **Target**: Doanh chủ vừa và nhỏ, đội sales 5-20 người
- **Dạy**: Hệ thống bán hàng 8+2 + 14 chiến lược lead gen + 7 kỹ thuật xử lý từ chối
- **Format**: 3 ngày offline (T2-T4) hội trường Hà Nội/HCM, ~700-900 attendees
- **Phiên bản hiện tại**: SSS 23 (2026-Q3)

## Vai trò trong hệ sinh thái

- **Upstream**: [[DTSGC - Đánh Thức Sự Giàu Có]] — học DTSGC nắm tư duy trước SSS
- **Downstream**: [[IPS - Internet Power System]] — học IPS để scale online sau khi master SSS
- **Song song**: [[MAP - Nha Trang]] — cùng level deep dive

## Cấu trúc khoá

- **Ngày 1**: Hệ thống bán hàng 8+2 (4h) + 14 chiến lược lead gen (3h) + 7 kỹ thuật xử lý từ chối (2h)
- **Ngày 2**: Practice case học viên (hot seat) + REM-30s + REM-60s + Persona Customer Value
- **Ngày 3**: Tích hợp + DMO + commit DMO 90 ngày + bài tập về nhà

## Modules / Khái niệm cốt lõi

- [[Hệ thống bán hàng 8+2]] — module chính (12h)
- [[14 chiến lược lead generation]] — module bổ trợ (3h)
- [[7 kỹ thuật xử lý từ chối]] — practice live (2h)
- [[REM-30s]] — bài thuyết trình 30 giây
- [[Customer Value Canvas]] — tiền đề persona
- [[Hot Seat]] — format coaching ngày 2

## Stories / Ngụ ngôn dùng

- [[Gã ăn mày giàu có]] — illustrate "đầu tư vào bản thân"
- [[Bút chì cùn]] — illustrate "kỹ năng cần mài giũa"

## Topics liên quan

- [[Tâm lý khách hàng B2C]]
- [[Persona doanh chủ Việt Nam]]

## Cases học viên signature

- [[Anna Nguyễn]] — chuyển từ -50% YoY sang +200% sau SSS 19
- [[Mr. T]] — vận hành team 30 sale rep sau SSS 21

## Tài sản đã sản xuất

- Sale page: https://sss.long.vn (current)
- Lead page: https://sss.long.vn/lp/checklist-30s
- Video promo: https://youtu.be/abc123
- Email sequence: 12 emails onboarding

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 21 | SSS 21 | 2025-11-28 | [[SSS 21 - Ngày 1 (28-11-2025)]] + D2/D3 | Mới nhất, +14 lead gen, +7 kỹ thuật xử lý từ chối |
| 19 | SSS 19 | 2024-10-11 | [[SSS 19 - HN (11-10-2024)]] | Lần đầu pivot LonGPT custom GPT |
| 10 | SSS 10 | 2020-07-15 | [[SSS 10 - Ngày 1 (15-07-2020)]] | Hệ thống hoá đủ 8+2 (foundation) |

## Khoá học liên quan

- [[BHTC - Bán Hàng Thành Công]] — tiền thân lịch sử (12/2012), nền tảng 8+2
- [[Eagle Camp]] — concept Hot Seat từ EC dùng trong SSS
- [[RAVING FAN]] — mở rộng after-sales sau SSS

## Câu hỏi mở

- SSS phiên bản 22 chưa ingest — chờ source
- Có version online ngắn 6h thay vì 3 ngày? Confirmed sẽ launch Q3 2026 nhưng chưa có schedule
```

---

## Variant — Khoá online tự học (module-based)

```markdown
---
type: concept
tags: [chuong-trinh, course/emm, email-marketing]
program_code: EMM
parent: "[[Hệ sinh thái đào tạo của bạn]]"
---

# EMM — Email Marketing Mastery

Khoá online tự học 6 module Email Marketing cho freelancer + agency. Mỗi module 2-3h video.

## Định vị

- **Target**: Freelancer marketer + agency owner
- **Dạy**: 6 module Email Marketing — setup → segmentation → automation → optimization → ROI tracking
- **Format**: Online tự học, 6 module, 15h video + bài tập
- **Giá**: $497 lifetime hoặc $49/tháng

## Vai trò trong hệ sinh thái

- **Upstream**: [[Marketing Basics]] — cần biết funnel concept cơ bản
- **Downstream**: [[Marketing Automation Advanced]] — cho người đã master EMM
- **Song song**: [[Content Marketing Pro]] — paired hữu ích

## Cấu trúc khoá (6 module)

- **Module 1**: Email infrastructure + DNS setup (3h)
- **Module 2**: List building + lead magnet (2h)
- **Module 3**: Segmentation + tagging strategy (2h)
- **Module 4**: Automation workflows (Welcome, Re-engagement, Cart abandonment) (3h)
- **Module 5**: Copy + design optimization (2h)
- **Module 6**: ROI tracking + A/B test (3h)

## Modules / Khái niệm cốt lõi

- [[Email DNS setup (SPF, DKIM, DMARC)]]
- [[Lead magnet design]]
- [[Segmentation strategy]]
- [[Email automation workflow]]
- [[Email copy patterns]]
- [[ROI tracking email]]

## Tài sản đã sản xuất

- Sale page: https://acme.com/emm
- Lead page: https://acme.com/lp/emm-checklist
- Video promo: https://youtu.be/xyz789
- Drip sequence sau opt-in: 7 emails

## Phiên bản đã ingest

| # | Phiên bản | Date | Source page | Signature |
|---|---|---|---|---|
| 1 | EMM v1 | 2026-04-15 | [[EMM Module 1-6 (v1)]] | Launch baseline |

## Câu hỏi mở

- Cần add module mới về AI-powered email (GPT, Claude)?
- Pricing $49/tháng vs $497 lifetime — ratio nào convert tốt hơn?
```

---

## Variant — Coaching weekly (Eagle Club pattern)

```markdown
---
type: concept
tags: [chuong-trinh, course/eagle-club, coaching-weekly]
program_code: EAGLE-CLUB
parent: "[[Hệ sinh thái đào tạo PTL]]"
---

# Eagle Club — Coaching 1 năm

Tier cao nhất hệ sinh thái PTL. Coaching weekly 1 năm cho 50-80 thành viên elite. Lifetime relationship.

## Định vị

- **Target**: Doanh chủ đã qua SSS + IPS, sẵn sàng commit 1 năm
- **Format**: 50 buổi weekly (Zoom hoặc offline HN/HCM), 2-3h/buổi
- **Cohort size**: 50-80 thành viên
- **Đầu tư**: Tier cao nhất

## Vai trò trong hệ sinh thái

- **Upstream**: [[SSS]] + [[IPS]] + [[Eagle Camp]] — qua hết mới đủ điều kiện
- **Downstream**: Không có — tier cao nhất

## Format buổi

Mỗi buổi:
- 30 phút check-in chia sẻ
- 1h hot seat (1-2 thành viên được coach deep)
- 30 phút Q&A
- 30 phút commitment tuần mới

## Concept thường dùng

(Không liệt mọi concept — khoá dạy lại + áp dụng concept từ SSS/IPS/Eagle Camp)

- [[Hot Seat format]]
- [[Quarterly Goal Review]]
- [[Accountability Partner]]

## Cohorts đã ingest

| Cohort | Date | Sessions ingested |
|---|---|---|
| 2025 | 2025-01 — 2025-12 | 12 buổi (samples) |
| 2026 | 2026-01 — đang chạy | 22 buổi (partial) |

(Coaching weekly isolate trong `wiki/sources/coaching-weekly/eagle-club/cohort-<year>/` — xem CLAUDE.md pattern coaching weekly)

## Câu hỏi mở

- Có nên migrate Eagle Club sang vault sibling riêng "Coaching" nếu info nhạy cảm vượt ngưỡng?
```

---

## Khi nào không tạo Course MOC

- Bạn không có chương trình đào tạo chính thức
- Vault knowledge cá nhân (không dạy ai)
- 1 khoá < 5 source ingest (chưa đủ data)

Trong những trường hợp đó, knowledge vẫn organize được qua concept page + topic page, không cần Course MOC.

---

## Tiếp theo

[[log-md-format]] — log.md format.
