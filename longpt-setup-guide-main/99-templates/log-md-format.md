---
title: log.md format
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# log.md format (copy-paste)

Template + quy ước cho `log.md` ở root vault. File append-only chronological.

---

## Format chuẩn

```markdown
# Log — <Vault Name>

Nhật ký append-only. Mới nhất ở dưới.

## [YYYY-MM-DD] <action> | <subject>

- <Detail 1>
- <Detail 2>
- Notes: <ghi chú>
```

Mỗi entry mở đầu bằng `## [YYYY-MM-DD] <action> | <subject>` để greppable.

---

## 5 action chính

| Action | Khi nào |
|---|---|
| `ingest` | Ingest source mới vào vault |
| `query` | User hỏi câu phức tạp, lưu lại |
| `lint` | Lint pass định kỳ |
| `setup` | Setup vault, plugin, agent, skill |
| `refactor` | Đổi schema, rename, migrate |
| `manual` | User tự sửa, không qua AI |

---

## Ví dụ thực tế

```markdown
# Log — My Brain

Nhật ký append-only.

## [2026-04-26] setup | Tạo vault
- Created: CLAUDE.md, index.md, log.md, README.md
- Created: folder raw/ + wiki/{sources,concepts,entities,courses}/

## [2026-04-27] ingest | Paul Graham — Product Market Fit (2024)
- Created: [[Paul Graham — Product Market Fit (2024)]]
- Created: [[Product Market Fit]] (concept mới)
- Created: [[Paul Graham]], [[Y Combinator]] (entity mới)
- Updated: [[index]]
- Notes: PMF khái niệm mới, chưa có concept page → tạo mới. Concept "Founder Mode" nhắc cuối bài → chưa tạo, đợi 2 source nữa.

## [2026-04-28] ingest | Sam Altman — Startup Playbook
- Created: [[Sam Altman — Startup Playbook]]
- Updated: [[Product Market Fit]] (append insight retention curve)
- Created: [[Sam Altman]] (entity mới)
- Notes: Sam khác PG về PMF — Sam nhấn retention curve flatten. Ghi vào section "Mâu thuẫn" của [[Product Market Fit]].

## [2026-04-29] query | "PMF cho B2B SaaS 10 customer nên làm gì?"
- Read: [[Product Market Fit]], [[Sam Altman — Startup Playbook]], [[Paul Graham — Product Market Fit (2024)]]
- Output: 5 action recommend, save thành [[wiki/analyses/Validate-PMF-cho-B2B-SaaS]]

## [2026-05-01] lint | weekly
- Issues: 3 broken wikilink, 2 page thiếu frontmatter
- Fixed: 3 broken wikilink (rename target)
- Deferred: 2 page frontmatter (đợi user duyệt)

## [2026-05-03] refactor | Tách wiki/courses/ subfolder
- Old: wiki/courses/<file>.md
- New: wiki/courses/<format>/<file>.md (format: offline-camp / online-self-study / coaching-weekly)
- Affected: 15 course page move
- Updated: CLAUDE.md schema, 23 wikilink
- Backup: Git commit "Before courses subfolder refactor"
```

---

## Quy tắc viết log

### Rule 1 — Mới nhất ở dưới

Append vào cuối file, không insert đầu.

### Rule 2 — Format date ISO

`2026-04-26` (YYYY-MM-DD). Không `26/4/2026` hay `Apr 26, 2026`.

→ Sort theo date tự nhiên + greppable.

### Rule 3 — Action lowercase

`ingest`, không `INGEST` hoặc `Ingest`.

### Rule 4 — Subject ngắn

≤ 60 chars. Long → cắt + chi tiết ở bullet.

### Rule 5 — Cite wikilink

Mọi page touch → wikilink. Vd:

```markdown
- Created: [[Page A]]
- Updated: [[Page B]]
```

→ Graph view track inbound link từ log → page.

### Rule 6 — Notes có "Why"

Quan trọng nhất. Notes không phải "what" (wikilink đã cover) mà là "why" + insight:

```markdown
- Notes: Sam khác PG về PMF — Sam nhấn retention curve flatten. Ghi vào section "Mâu thuẫn".
```

→ 6 tháng sau đọc log biết why quyết định.

---

## Greppable patterns

### Tìm ingest tuần này

```bash
grep "^## \[2026-04-2.\] ingest" log.md
```

### Tìm 10 entry gần nhất

```bash
grep "^## \[" log.md | tail -10
```

### Tìm refactor lịch sử

```bash
grep "^## \[.*\] refactor" log.md
```

### Tìm mọi entry liên quan PMF

```bash
grep -B0 -A5 "PMF" log.md
```

---

## Đếm số entry mỗi action

```bash
awk -F'|' '/^## \[/{print $1}' log.md | grep -oE 'ingest|query|lint|refactor|setup|manual' | sort | uniq -c
```

Vd output:

```
  47 ingest
  12 lint
   5 query
   3 refactor
   1 setup
```

→ Track tỷ lệ ingest vs query — bạn ingest nhiều mà query ít → đang accumulate without using.

---

## Khi log quá dài

Sau 1-2 năm, log.md có thể > 10000 dòng → load chậm.

### Option A — Archive theo năm

```bash
# Cuối năm
mv log.md log-2025.md
echo "# Log — 2026" > log.md
```

Index trong `index.md`:

```markdown
## Logs

- [[log]] — 2026 (current)
- [[log-2025]]
- [[log-2024]]
```

### Option B — Archive theo quý

Cho vault rất active.

### Option C — Không archive, dùng tail

`log.md` giữ nguyên, dùng tail/grep để check recent. Obsidian search vẫn fast nếu file < 50000 dòng.

→ Khuyên Option A. Archive cuối năm. Đủ đơn giản.

---

## Log entry cho 4 workflow chính

### Ingest

```markdown
## [YYYY-MM-DD] ingest | <Source Title>
- Created: [[Source]], [[Concept mới]] (nếu mới)
- Updated: [[Concept cũ]] (nếu append)
- Notes: <insight đáng nhớ>
```

### Query

```markdown
## [YYYY-MM-DD] query | "<câu hỏi>"
- Read: [[Page 1]], [[Page 2]], [[Page 3]]
- Output: <format>, save thành [[wiki/analyses/<file>]] (nếu lưu)
```

### Lint

```markdown
## [YYYY-MM-DD] lint | <mode>
- Issues: <số issue>
- Fixed: <số fix>
- Deferred: <số deferred>
- Report: [[wiki/lint-reports/<file>]]
```

### Refactor

```markdown
## [YYYY-MM-DD] refactor | <subject>
- Old: <state cũ>
- New: <state mới>
- Affected: <số file>
- Updated: <thứ gì update>
- Backup: <commit hash>
```

---

## Log format cho agent

Agent (vd `article-ingest`) auto append log khi run. Format:

```markdown
## [YYYY-MM-DD] ingest | <Title> [agent: article-ingest]
- Created: ...
- Updated: ...
- Notes: ...
```

Suffix `[agent: <name>]` để track entry nào AI làm, entry nào user làm thủ công.

---

## Khi log entry không cần

KHÔNG log:

- Edit nhỏ (typo fix) — trivial, không cần track
- Action repeat (vd: mỗi 5 phút run `lint quick` → đừng log mỗi lần, gộp daily)
- Action không thay đổi vault (vd: query không lưu output)

Log entry là quyền lợi, không phải obligation. Quá nhiều log → noise.

---

## Tiếp theo

[[index-md-format]] — index.md format.
