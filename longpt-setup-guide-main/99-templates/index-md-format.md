---
title: index.md format
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# index.md format (copy-paste)

Template + quy ước cho `index.md` ở root vault. File mục lục.

---

## Format chuẩn

```markdown
# Index — <Vault Name>

Mục lục đầy đủ. Gom theo nhóm. Mỗi entry 1 dòng.

## <Group 1>

- [[Page A]] — mô tả 1 dòng (date, author nếu source)
- [[Page B]] — ...

## <Group 2>

- [[Page C]] — ...
```

---

## Group cơ bản

Vault knowledge:

```markdown
## Sources
## Concepts
## Entities
## Courses
## Stories
## Topics
## Analyses
## Reference
```

Vault lifestyle:

```markdown
## Domains
## Entities
## Events
## Concepts
## Analyses
## Journal
```

Vault production:

```markdown
## Sources
## Assets
  - Lead pages
  - Sale pages
  - Contents
  - Ads
  - Events
## Reports
## Concepts
## Entities
```

Vault execution (4DX):

```markdown
## WIG
## Reviews weekly
## Scoreboard
## Cadence
```

---

## Format mỗi entry

```markdown
- [[Page Name]] — <mô tả 1 dòng>
```

Mô tả nên include:
- **Source**: tác giả + date — vd `[[Paul Graham — PMF (2024)]] — bài về PMF process (PG, 09/2024)`
- **Concept**: domain + rating — vd `[[Bộ não thứ 2]] — knowledge management 5/5`
- **Course**: program code + version — vd `[[SSS — Sales Success System]] — Sales B2C, v23 (2026-Q3)`
- **Entity**: vai trò trong vault — vd `[[Paul Graham]] — founder YC, viết essay`

---

## Ví dụ vault knowledge

```markdown
# Index — My Brain

Mục lục.

## Sources

### Articles
- [[Paul Graham — Product Market Fit (2024)]] — bài về PMF process (PG, 09/2024)
- [[Sam Altman — Startup Playbook]] — playbook YC alumni (Sam, 2022)
- [[Naval Ravikant — Specific Knowledge]] — concept "specific knowledge" (Naval, 2018)

### Sách
- [[Atomic Habits — James Clear (2018)]] — 4 law of behavior change
- [[Lean Startup — Eric Ries (2011)]] — build-measure-learn loop

### Transcripts
- [[SSS 21 - Ngày 1 (28-11-2025)]] — khoá SSS phiên bản 21, ngày 1
- [[SSS 21 - Ngày 2 (29-11-2025)]] — khoá SSS phiên bản 21, ngày 2
- [[SSS 21 - Ngày 3 (30-11-2025)]] — khoá SSS phiên bản 21, ngày 3

## Concepts (đa khoá — top 20)

- [[Hệ thống bán hàng 8+2]] — Sales 5/5, dùng SSS + BHTC + RAVING FAN
- [[14 chiến lược lead generation]] — Sales 4/5, dùng SSS (mới v21)
- [[Bộ não thứ 2]] — Knowledge 5/5, dùng SSS + IPS + LTVM
- [[Customer Value Canvas]] — Persona 4/5, dùng SSS + IPS
- [[6 Nhu cầu con người]] — Psychology 4/5, dùng LTVM + DTSGC
- [[Sự gán nghĩa]] — Psychology 4/5, dùng LTVM
- [[Hệ thống niềm tin]] — Psychology 4/5, dùng LTVM
- [[Cài đặt tư duy 5 bước]] — Coaching 5/5, signature PTL
- [[Hot Seat]] — Coaching format 4/5
- [[REM-30s]] — Networking 4/5

## Concepts (single-course)

- [[Founder Mode]] — Startup 3/5, single source PG (2024-09)
- [[Email DNS setup]] — Email 3/5, single course EMM
- ...

## Entities

### Người
- [[Phạm Thành Long]] — founder Sứ Mệnh, trainer
- [[Paul Graham]] — founder YC, essayist
- [[Sam Altman]] — CEO OpenAI, ex-YC
- [[Naval Ravikant]] — angel investor, author

### Tổ chức
- [[Y Combinator]] — accelerator
- [[BNI HN6]] — chapter networking
- [[Sứ Mệnh Lãnh Đạo]] — công ty PTL

## Courses

### Offline lớn
- [[SSS — Sales Success System]] — Sales B2C, 3 ngày, v23 (2026-Q3)
- [[IPS — Internet Power System]] — Marketing online, 3 ngày
- [[DTSGC — Đánh Thức Sự Giàu Có]] — Tư duy doanh chủ
- [[LTVM — Lập Trình Vận Mệnh]] — Coaching cuộc đời

### Camp + Summit
- [[Eagle Camp]] — offline event 3-5 ngày
- [[Yes Summit]] — annual

### Online tự học
- [[EMM — Email Marketing Mastery]] — Email mkt, 6 module

### Coaching weekly
- [[Eagle Club]] — 1 năm, tier cao nhất
- [[IPS Coach]] — 6 tháng

## Stories / Ngụ ngôn

- [[Gã ăn mày giàu có]] — illustrate "đầu tư vào bản thân"
- [[Cô gái tóc dài]] — illustrate "thay đổi mindset"
- [[Bút chì cùn]] — illustrate "kỹ năng cần mài giũa"

## Topics

- [[Tâm lý khách hàng B2C]]
- [[Persona doanh chủ Việt Nam]]
- [[Building Second Brain]]

## Analyses

- [[Validate PMF cho B2B SaaS]] — 5 action recommend (2026-04-29)
- [[So sánh SSS vs IPS]] — pivot point (2026-03-15)
- [[Concept đa khoá xuyên 5 chương trình]] — map concept (2026-02)

## Reference

- [[Schema vault]] — link CLAUDE.md
- [[Workflow ingest]] — link [[02-vault-dau-tien-brain/07-ingest-source-dau-tien]]
```

---

## Quy tắc viết index

### Rule 1 — Mỗi entry 1 dòng

```markdown
- [[Page]] — short description
```

KHÔNG nhiều dòng cho 1 entry.

### Rule 2 — Wikilink mandatory

Mọi entry phải có `[[Page Name]]`. Không paste plain text.

### Rule 3 — Group theo loại / domain

Không sort alphabet (đó là filename rồi). Sort theo nhóm logic.

### Rule 4 — Top N quan trọng

Group "Concepts (đa khoá — top 20)" — chỉ liệt 20 quan trọng. Không liệt 600 concept.

Đầy đủ → dùng Dataview query trong Obsidian (xem dưới).

### Rule 5 — Update khi tạo page mới

Mỗi ingest → AI append entry mới vào group đúng. KHÔNG để page tồn tại mà index không có.

Lint pass sẽ flag drift.

---

## Sub-index thay vì index khổng lồ

Vault > 500 page → index khổng lồ khó dùng. Tách sub-index:

```markdown
## Concepts

- [[index-concepts]] — 600 concept đầy đủ, link đến đây
- Top 20 concept dưới đây:
  - [[Hệ thống bán hàng 8+2]]
  - ...
```

`wiki/index-concepts.md`:

```markdown
# Index — Concepts

Toàn bộ 600 concept page. Sort theo domain.

## Sales (120)
- [[Hệ thống bán hàng 8+2]]
- ...

## Marketing (95)
- ...

## Psychology (88)
- ...
```

---

## Dataview alternative

Obsidian Dataview plugin cho phép query frontmatter — auto generate list:

```markdown
## Concepts (Dataview auto-generated)

\`\`\`dataview
TABLE 
  tags as "Tags",
  rating as "Rating"
FROM "wiki/concepts"
WHERE type = "concept"
SORT rating DESC
LIMIT 20
\`\`\`
```

(Bỏ backslash trước backtick)

Khi cài Dataview, switch sang Reading mode → auto render bảng.

Ưu: auto sync, không phải update index khi tạo page mới.
Nhược: chậm khi > 1000 page.

→ Hybrid: index tay cho top 20 + Dataview cho full list.

---

## Khi index có entry stale

Page đã rename / delete nhưng index vẫn còn entry cũ → broken link.

Fix:
- Lint pass detect
- AI bulk remove entry stale

```
> Lint index.md: tìm entry trỏ page không tồn tại. Remove.
```

---

## Cross-vault index

Nếu multi-vault, có thể tạo `Documents/INDEX.md` ở folder cha:

```markdown
# Index — All Sibling Vaults

## Brain
- 1245 page knowledge — [[My Brain/index]]

## Life
- 320 page lifestyle — [[My Life/index]]

## 4DX
- 45 page execution — [[My 4DX/index]]

## Marketing
- 180 page production — [[My Marketing/index]]
```

Mở Obsidian ở Documents/ → có overview toàn ecosystem.

---

## Tiếp theo

Bạn đã hoàn thành 99-templates. Bạn đã hoàn thành toàn bộ giáo trình.

Quay lại [[../README]] để review hoặc bắt đầu apply.
