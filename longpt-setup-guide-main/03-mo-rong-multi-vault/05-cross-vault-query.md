---
title: Cross-vault query
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 03
---

# Cross-vault query

## Trước đó

[[04-vault-marketing]] — bạn có 3-4 vault sibling.

---

## Vấn đề

Bạn có 4 vault: Brain, Life, 4DX, Marketing. Hỏi 1 câu, câu trả lời nằm xuyên 2-3 vault. Vd:

- *"Sale page IPS Q2 thu được bao nhiêu, dùng concept gì từ khoá IPS, ROI so với mục tiêu WIG 2026?"*

Câu này cần:
- Marketing/wiki/reports/2026-Q2-ips-funnel.md (số doanh thu)
- Brain/wiki/courses/IPS - Internet Power System.md (concept)
- 4DX/wig/2026-WIG-4-revenue.md (mục tiêu)

Claude phải đọc 3 vault đồng thời, tổng hợp.

---

## Setup cross-vault — 2 cách

### Cách 1 — Mở Claude ở vault parent

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
claude
```

Claude scope ở folder Documents/ → đọc được mọi vault sibling.

CLAUDE.md vault này (nếu có) sẽ là parent — không có cũng được, Claude vẫn đọc cả 4 vault.

**Khuyên**: tạo `Documents/CLAUDE.md` đơn giản:

```markdown
# CLAUDE.md — Parent of all sibling vaults

Vault list:
- [[My Brain/]] — knowledge
- [[My Life/]] — lifestyle
- [[My 4DX/]] — execution
- [[My Marketing/]] — production

Mỗi vault có CLAUDE.md riêng. Đọc theo schema vault tương ứng khi work.

Cross-vault wikilink: `[[<vault>/<path>/<page>]]`.
```

### Cách 2 — Mở Claude ở vault cụ thể, dùng absolute path

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Claude scope ở Brain. Khi cần đọc vault khác:

```
> Đọc file ../My Marketing/wiki/assets/sale-pages/sp-ips-2026.md
```

Cumbersome hơn, nhưng vẫn work.

---

## Cross-vault wikilink

### Trong file của vault A, link tới vault B

```markdown
Concept này dùng trong [[../My Marketing/wiki/assets/sale-pages/sp-ips-2026]]
```

### Quy tắc absolute path

- Path bắt đầu từ folder cha 2 vault (`Documents/`)
- Format `../<Vault Name>/<path>/<file>`
- Obsidian render link OK nếu mở vault parent
- Obsidian KHÔNG render link nếu mở vault con (chỉ thấy plain text)

### Workaround: frontmatter `brain_ref`

Thay vì wikilink absolute (dễ vỡ khi rename vault), dùng frontmatter reference:

```yaml
---
brain_ref:
  program_code: ips
  course_page: "[[IPS - Internet Power System]]"
  vault: "My Brain"
---
```

Claude đọc frontmatter biết:
- Vault: `My Brain`
- File: `wiki/courses/IPS - Internet Power System.md`

Khi rename vault → chỉ sửa frontmatter `vault:`, không phải rewrite mọi wikilink.

---

## Pattern query phổ biến

### Query 1 — Cross 2 vault (Brain + Marketing)

```
> Sale page nào cho khoá IPS đang chạy? Concept nào IPS dạy chưa được apply vào sale page?
```

Claude:
1. Đọc `Marketing/wiki/assets/sale-pages/` filter brain_ref ips
2. Đọc `Brain/wiki/courses/IPS - Internet Power System.md` lấy danh sách concept
3. Cross-ref: concept nào có wikilink trong sale page, concept nào không
4. Trả lời + đề xuất

### Query 2 — Cross 3 vault (Brain + Marketing + 4DX)

```
> Doanh thu Q2 từ khoá IPS, so với WIG 4 target, dùng concept gì, sale page nào?
```

Claude:
1. 4DX/wig/2026-WIG-4-revenue.md → target Q2
2. Marketing/wiki/reports/2026-Q2-revenue.md → actual
3. Marketing/wiki/assets/sale-pages/ → sale page IPS
4. Brain/wiki/courses/IPS... → concept dạy
5. Tổng hợp

### Query 3 — Brain + Life

```
> Concept "Atomic Habits" từ Brain có ứng dụng nào vào lịch tập Ironman trong Life chưa?
```

Claude:
1. Brain/wiki/concepts/Atomic Habits.md → đọc rule chính
2. Life/wiki/domains/the-thao-triathlon.md → đọc lịch tập
3. So sánh: rule nào đã apply, rule nào chưa
4. Suggest action

### Query 4 — Life + 4DX

```
> Tuần W22 hit bao nhiêu giờ training, có đủ target WIG 2 không?
```

Claude:
1. Life/4dx/actions/2026-W22-actions.md → count training_hours
2. 4DX/wig/2026-WIG-2-ironman.md → target
3. Trả lời + traffic light

---

## Setup ranh giới rõ — quan trọng

Mỗi vault có CLAUDE.md mô tả **vault này** + **mối quan hệ với vault khác**. Vd:

### Brain CLAUDE.md có section

```markdown
## Vault song song

- `../Life/` — vault anh em chứa lifestyle. Brain = kiến thức work; Life = personal hobby. Truy vấn lifestyle → chuyển sang Life.
- `../Marketing/` — vault anh em đọc kiến thức Brain để sản xuất. Marketing **chỉ đọc** Brain, không ghi ngược.
- `../4DX/` — vault execution. 4DX **chỉ đọc** Brain + Life + Marketing actions.
```

### Marketing CLAUDE.md có section

```markdown
## Cross-vault Brain

- `../My Brain/` — đọc kiến thức course / concept
- Marketing chỉ đọc Brain, không ghi ngược
- Reference: frontmatter `brain_ref` hoặc wikilink absolute `[[../My Brain/...]]`
- Phát hiện concept mới chưa có Brain → log, để user xử lý bên Brain
```

→ Mỗi vault có rule "ai đọc ai", "ai ghi ai".

---

## Anti-pattern cross-vault

### Sai 1 — Ghi 2 chiều

Marketing **chỉ đọc** Brain. KHÔNG ghi ngược. Nếu Marketing tự sửa concept page bên Brain → conflict ownership, dễ vỡ.

→ Marketing phát hiện concept mới chưa có → log lại trong `Marketing/log.md`. User vào Brain xử lý.

### Sai 2 — Wikilink absolute lan tràn

Mỗi page Marketing wikilink absolute tới Brain. Sau khi rename Brain → vỡ hết.

→ Dùng frontmatter `brain_ref` (1 chỗ) thay 50 wikilink absolute.

### Sai 3 — Schema duplicate

Concept "Hệ thống bán hàng 8+2" có page ở Brain VÀ Marketing → duplicate.

→ Page ở Brain duy nhất. Marketing chỉ link.

### Sai 4 — Query không clarify vault

```
> Lead page nào CVR cao nhất?
```

(Không nói vault nào)

→ Claude phải hỏi: "Bạn hỏi lead page trong Marketing vault, đúng không?"

Sửa:

```
> Trong Marketing vault, lead page nào CVR cao nhất Q2?
```

---

## MOC cross-vault

Tạo MOC ở Brain `wiki/Hệ sinh thái 4 vault.md`:

```markdown
---
type: meta-moc
tags: [meta, cross-vault]
---

# Hệ sinh thái 4 vault

## Brain (vault hiện tại)

Knowledge concept-first.

## Life

Lifestyle cá nhân. Photo + entity + event.

- Cross-ref: concept "Atomic Habits" từ Brain → apply lịch tập trong Life
- Cross-ref: entity "[[Triathlon Coach]]" từ Life ↔ "[[Tony Robbins]]" mentor Brain

## 4DX

Meta execution. Cron đêm CN.

- Pull Life actions → traffic light WIG 2 (Ironman)
- Pull Marketing actions → traffic light WIG 4 (revenue)

## Marketing

Production + measurement.

- Reference Brain concept → sale page
- Output asset metric → 4DX cron pick up
```

Mở Obsidian Brain → mở MOC → có overview 4 vault.

---

## Workflow query xuyên vault

```
1. Bạn ask câu vắt N vault
   ↓
2. Claude đọc CLAUDE.md các vault liên quan
   ↓
3. Claude identify file cần đọc mỗi vault
   ↓
4. Read các file → tổng hợp
   ↓
5. Cite source theo vault: "Theo Brain: ... Theo Marketing: ... Theo 4DX: ..."
   ↓
6. Đề xuất action cross-vault
   ↓
7. Lưu analysis vào vault phù hợp
```

---

## Verify Phần 03 xong

Sau Phần 03:
- [x] Hiểu khi nào tách vault
- [x] Có Life vault (nếu cần)
- [x] Có 4DX vault (nếu cần)
- [x] Có Marketing vault (nếu cần)
- [x] Query xuyên vault OK

→ Sang Phần 04 agents + skills + memory.

---

## Tiếp theo

Đọc tiếp: [[04-agents-skills-memory/01-agent-la-gi]] — Khái niệm agent.
