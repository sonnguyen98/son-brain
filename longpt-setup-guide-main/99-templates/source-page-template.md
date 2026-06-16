---
title: Source page template
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# Source page template (copy-paste)

Template source page generic. Copy vào `wiki/sources/<Title>.md`.

---

## Template chuẩn

```markdown
---
type: source
tags: [source-<kind>, <theme-tags>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
raw_path: raw/<path>/<file>
author: "<Author>"
date: YYYY-MM
url: https://<url>
language: <en|vi|...>
---

# <Tên source — bối cảnh>

<1 dòng tóm tắt source là gì + kỳ + tác giả>

## TL;DR

- <Ý chính 1>
- <Ý chính 2>
- <Ý chính 3>
- <Ý chính 4>
- <Ý chính 5>

## Nội dung chính

<Đoạn 1 — opening / context>

<Đoạn 2 — main argument / framework>

<Đoạn 3 — conclusion / takeaway>

## Concept đã touch / dạy

- [[<Concept A>]] — đoạn line X (~timecode/page)
- [[<Concept B>]] — đoạn line Y

## Entity nhắc đến

- [[<Entity X>]] — vai trò trong source
- [[<Entity Y>]]

## Quote signature

> "<Quote nguyên văn từ source>"
>
> — Author, location/line ref

## Câu chốt rút ra

<1-2 takeaway lớn nhất — insight personal>

## Mâu thuẫn (nếu có)

<Source mới mâu thuẫn source cũ — ghi rõ>

## Câu hỏi mở

- ?
```

---

## Variant — Article web

```markdown
---
type: source
tags: [source-article, startup, founder-mode]
created: 2026-05-29
updated: 2026-05-29
raw_path: raw/articles/2024-09-paul-graham-founder-mode.md
author: "Paul Graham"
date: 2024-09
url: https://paulgraham.com/foundermode.html
language: en
---

# Paul Graham — Founder Mode (2024-09)

Essay PG mô tả 2 mode quản lý founder vs manager, lý giải sao founder mode không scale qua delegation thuần.

## TL;DR

- 2 mode: Founder Mode (deep, micromanage) vs Manager Mode (delegate, layer)
- Brian Chesky (Airbnb) là exemplar — pivot khỏi Manager Mode, switch về Founder Mode
- Y Combinator W24 batch confirm pattern
- Manager Mode advice ("hire great, delegate, get out of way") fail cho founder
- PG cảnh báo: corporate world push founder vào Manager Mode

## Nội dung chính

PG đặt vấn đề từ Brian Chesky case: Brian followed "conventional wisdom" của Manager Mode (hire great people, let them do their thing) → Airbnb degrade. Pivot về Founder Mode — direct involvement với từng layer → revert tình hình.

PG generalize: Founder Mode cho phép founder skip-level → talk thẳng với engineer 3 cấp dưới, không qua VP. "Skip-level meetings" là tool chính. Manager Mode cấm điều này vì coi như đe doạ VP.

Concluding: PG kêu gọi research Founder Mode chính thức — chưa có sách / framework formal. Mời founders share experience.

## Concept đã touch

- [[Founder Mode]] — concept chính, định nghĩa, signal
- [[Manager Mode]] — opposite
- [[Skip-level meeting]] — tool concrete
- [[Brian Chesky leadership]] — case study

## Entity nhắc đến

- [[Paul Graham]] — author
- [[Brian Chesky]] — Airbnb CEO, exemplar
- [[Y Combinator]] — accelerator
- [[Airbnb]] — case study company

## Quote signature

> "It will probably be some time before we fully understand Founder Mode."
>
> — Paul Graham, paulgraham.com/foundermode.html, paragraph 9

## Câu chốt rút ra

Founder mode = anti-delegation pattern. Áp dụng cho startup tôi → cần pivot từ "hire CTO let them handle" sang "skip-level với engineer hàng tuần".

## Câu hỏi mở

- Founder Mode dùng cho công ty quy mô nào? PG không clarify upper bound.
- Có anti-pattern Founder Mode (over-micromanage)? PG không cảnh báo.
```

---

## Variant — Transcript khoá học

```markdown
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
created: 2025-11-29
updated: 2025-11-29
---

# SSS 21 - Ngày 1 (28-11-2025)

Ngày 1 khoá SSS 21, Hà Nội. PTL dạy 8 bước hệ thống bán hàng + intro 14 chiến lược lead gen mới.

## TL;DR

- Module chính: Hệ thống bán hàng 8+2 (8h dạy live, có case bài tập)
- Mới phiên bản 21: 14 chiến lược lead generation (~3h, lần đầu)
- 7 kỹ thuật xử lý từ chối: dạy practice với học viên real (hot seat)
- Câu chốt: "Bán hàng là gọi đúng người, đúng thời điểm, đúng cách"
- 700 attendees, sold out

## Nội dung chính

<Đoạn 1 — module 8+2 deep dive>

<Đoạn 2 — 14 lead gen overview>

<Đoạn 3 — 7 kỹ thuật xử lý từ chối practice>

## Modules đã dạy

- [[Hệ thống bán hàng 8+2]] — module chính (12:00-16:00, 4h)
- [[14 chiến lược lead generation]] — module mới (16:30-19:30, 3h)
- [[7 kỹ thuật xử lý từ chối]] — practice (20:00-22:00, 2h)

## Case học viên / Hot seat

- [[Anna Nguyễn]] — chia sẻ case B2B SaaS bị stuck, PTL coach 30 phút
- [[Mr. T]] — case team 30 sales rep, hệ thống lead nuôi

## Bài tập trên hội trường

- BT 1: Viết REM-30s cho ngành của bạn (14:30-15:30)
- BT 2: Practice 7 kỹ thuật xử lý từ chối — paired (20:30-21:30)

## Câu chốt PTL

> "Bán hàng là gọi đúng người, đúng thời điểm, đúng cách. Sai 1 trong 3 là hỏng deal."
>
> — đoạn 14:23 chunk-005

> "Lead không tự đến. Bạn phải đi tìm. 14 chiến lược, mỗi cái pick 2-3 phù hợp ngành."
>
> — đoạn 17:15 chunk-008

## Concept liên quan

- [[Hệ thống bán hàng 8+2]] — concept chính
- [[Customer Value Canvas]] — tiền đề
- [[Hot Seat]] — format coaching

## Entity nhắc đến

- [[Phạm Thành Long]] — trainer
- [[BNI HN6]] — community
- [[Anna Nguyễn]] — học viên case

## Câu hỏi mở

- Bảng 14 lead gen chi tiết bằng tiếng Việt? Cần xác minh từ chunk-008 vs chunk-009.
- "Hot Seat" format ai phát minh? PTL custom hay từ Tony Robbins?
```

---

## Variant — Sách

```markdown
---
type: source
tags: [source-book, behavioral-economics]
created: 2026-05-29
updated: 2026-05-29
raw_path: raw/books/atomic-habits-james-clear.pdf
author: "James Clear"
date: 2018
publisher: "Avery"
isbn: 978-0735211292
url: https://jamesclear.com/atomic-habits
language: en
pages: 320
---

# Atomic Habits — James Clear (2018)

Sách phổ biến về xây thói quen — 4 law of behavior change, identity-based habit.

## TL;DR

- Habit = compound interest of self-improvement
- 4 Laws: Cue-Craving-Response-Reward
- Identity-based: "I am X" thay "I want to do X"
- 1% improvement / day → 37× / year
- Environment design thay willpower

## Nội dung chính

<Phần 1 — Fundamentals (chương 1-4)>

<Phần 2 — Make it Obvious (chương 5-7) — 1st Law>

<Phần 3 — Make it Attractive (chương 8-10) — 2nd Law>

<Phần 4 — Make it Easy (chương 11-14) — 3rd Law>

<Phần 5 — Make it Satisfying (chương 15-17) — 4th Law>

<Phần 6 — Advanced Tactics (chương 18-20)>

## Concept đã touch

- [[Habit loop — Cue-Craving-Response-Reward]] — framework chính
- [[1% improvement]] — compounding principle
- [[Identity-based habit]] — vs outcome-based
- [[Environment design]] — leverage point
- [[Habit stacking]] — tool

## Entity nhắc đến

- [[James Clear]] — author
- [[BJ Fogg]] — Tiny Habits, cite
- [[Charles Duhigg]] — Power of Habit, cite

## Quote signature

> "You do not rise to the level of your goals. You fall to the level of your systems."
>
> — James Clear, p27

> "Every action you take is a vote for the type of person you wish to become."
>
> — p36

## Câu chốt rút ra

Identity-based shift quan trọng hơn outcome. Áp dụng cho tôi: "tôi là runner" (identity) thay "tôi muốn chạy marathon" (outcome). Decision daily theo identity → consistent.

## Câu hỏi mở

- 1% / day có scale với mọi domain không? Skill phức tạp (toán cao cấp) không 1% được — cần insight.
- Habit stacking conflict với deep work? Cần thử case cụ thể.
```

---

## Tiếp theo

[[course-moc-template]] — Course MOC template.
