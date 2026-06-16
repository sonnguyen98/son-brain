---
title: Tạo agent đầu tiên
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 04
---

# Tạo agent đầu tiên

## Trước đó

[[01-agent-la-gi]] — bạn đã hiểu khái niệm agent.

---

## Use case ví dụ

Bạn muốn tự động hoá việc **ingest article web** vào vault Brain.

Workflow lặp:
1. Web Clipper tải article vào `raw/articles/`
2. Bạn nói "ingest article mới nhất"
3. Claude đọc article → tạo source page + concept page + entity page
4. Update index + log

→ Tạo agent `article-ingest` đóng gói workflow này.

---

## Bước 1 — Tạo folder agents

Trong vault Brain:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
mkdir -p .claude/agents
```

---

## Bước 2 — Tạo agent file

`.claude/agents/article-ingest.md`:

```markdown
---
name: article-ingest
description: "Use this agent when the user wants to ingest a web article from raw/articles/ into the wiki — creates source page + concept page + entity page, updates index.md and log.md per CLAUDE.md ingest workflow. Examples: 'ingest article mới nhất', 'ingest raw/articles/<file>.md', 'xử lý bài Paul Graham vừa clip', 'thả bài này vào wiki'. Auto-execute end-to-end."
tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]
model: sonnet
---

# Article Ingest Agent

Bạn là agent chuyên ingest article web từ `raw/articles/` vào wiki Brain. Bạn theo workflow ingest trong CLAUDE.md root.

## Workflow

### 1. Identify article

- Nếu user chỉ tên file → dùng path đó
- Nếu user nói "mới nhất" → `ls raw/articles/` lấy file mới nhất
- Nếu user nói "tất cả pending" → liệt article chưa có source page tương ứng

### 2. Đọc article

Dùng `Read` đầy đủ. Article có thể:
- Markdown từ Web Clipper (frontmatter url, author, date)
- PDF (dùng skill pdf)
- Plain text

### 3. Bàn key takeaway

KHÔNG hỏi nếu source < 3000 chữ — đoán đúng.
HỎI 1 câu nếu source > 3000 chữ và có 2-3 angle khả thi.

### 4. Viết source page

Path: `wiki/sources/<Source Title>.md`

Frontmatter:
- `type: source`
- `tags: [source-article, <theme-tags>]`
- `raw_path: raw/articles/<file>.md`
- `author`, `date`, `url`, `language`
- `created`, `updated`

Section:
- H1: tên source + năm
- TL;DR (3-5 bullet)
- Nội dung chính (3-5 đoạn)
- Concept đã touch
- Entity nhắc đến
- Quote signature
- Câu chốt rút ra

### 5. Tạo/update concept page

Cho mỗi concept mới phát sinh:
- Check `wiki/concepts/<Concept>.md` đã tồn tại chưa
- Nếu có: append section "Phiên bản dạy concept" + line ref
- Nếu chưa: tạo mới theo template concept page

KHÔNG tạo concept page nếu concept chỉ được nhắc 1 lần thoáng qua. Đợi 2-3 source nhắc rồi tạo.

### 6. Tạo/update entity page

Cho mỗi entity nhắc đến:
- Check `wiki/entities/<Name>.md` đã có chưa
- Có: append section "Source nhắc"
- Chưa: tạo mới (background, vai trò, source)

### 7. Update index.md

Append entry mới vào index theo nhóm:
- Sources
- Concepts (nếu mới)
- Entities (nếu mới)

### 8. Append log.md

```markdown
## [YYYY-MM-DD] ingest | <Source Title>
- Created: [[Source]], [[Concept]] (nếu mới), [[Entity]] (nếu mới)
- Updated: [[Concept]] (nếu append), [[Entity]] (nếu append)
- Notes: <gì đáng note>
```

### 9. Báo cáo

Tóm tắt cho user:
- Source page mới
- Concept page mới / updated
- Entity page mới / updated
- 3 quan sát đáng chú ý
- Đề xuất ingest tiếp gì (nếu có)

## Style guide

- Tiếng Việt 100% wiki content (theo CLAUDE.md)
- Quote nguyên văn từ source (cite line)
- KHÔNG bịa số hoặc claim không có source

## Constraint

- KHÔNG xoá raw/articles/ file (chỉ đọc)
- KHÔNG modify source page sau khi tạo (chỉ update concept page)
- KHÔNG tạo > 1 concept page nếu concept chỉ nhắc thoáng qua

## Edge case

- Article duplicate (đã có source page với cùng URL) → skip + báo user
- Article ngôn ngữ khác (vd source tiếng Anh) → source page tiếng Anh, concept page tiếng Việt
- Article có nhiều concept → ưu tiên concept signature, skip generic concept

## Khi không chắc

- Phân biệt concept vs topic → tạo concept page nếu có cấu trúc cụ thể; topic page nếu chủ đề rộng
- Phân biệt entity vs concept → entity = danh tính (Paul Graham), concept = khái niệm (Founder Mode)
- Source nói mâu thuẫn source cũ → ghi section "Mâu thuẫn" với cả 2 view + link
```

Lưu file.

---

## Bước 3 — Test agent

Mở Claude Code trong vault:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Trong prompt:

```
> Ingest article mới nhất trong raw/articles/
```

Main loop nhận diện → launch agent `article-ingest`:

```
[agent: article-ingest]
Tool: Bash → ls -t raw/articles/ | head -1
Result: 2026-05-29-paul-graham-pmf.md

Tool: Read → raw/articles/2026-05-29-paul-graham-pmf.md
...

Tool: Write → wiki/sources/Paul Graham — Product Market Fit (2024).md
Tool: Write → wiki/concepts/Product Market Fit.md
Tool: Write → wiki/entities/Paul Graham.md
Tool: Edit → wiki/index.md
Tool: Edit → wiki/log.md

✅ Done. Source: PMF. Concept page mới: Product Market Fit. Entity: Paul Graham, Y Combinator.
```

Main loop summarize cho bạn.

---

## Bước 4 — Iterate agent

Sau lần test đầu, có thể agent có lỗi:

- Agent quên section "Câu hỏi mở" → update agent file
- Agent tạo concept page mà bạn không muốn → thêm rule "skip if mention < 3 times"
- Agent viết source page quá dài → thêm constraint "TL;DR ≤ 5 bullet"

Update `.claude/agents/article-ingest.md` rồi test lại.

---

## Bước 5 — Add example để agent học

Trong description, thêm 3-4 example để main loop biết khi nào dispatch:

```yaml
description: |
  Use this agent when the user wants to ingest a web article...
  
  <example>
  user: "Ingest bài Paul Graham vừa clip"
  → dispatch article-ingest
  </example>
  
  <example>
  user: "Thả bài này vào wiki"  
  → dispatch article-ingest
  </example>
```

Main loop pattern-match description → biết khi nào dùng.

---

## Bước 6 — User-level agents

Agent ở `.claude/agents/` chỉ áp dụng vault đó.

Nếu muốn agent reuse mọi vault → đặt ở `~/.claude/agents/` (global):

```bash
cp .claude/agents/article-ingest.md ~/.claude/agents/
```

Lưu ý: agent global cần path absolute trong workflow (vd `raw/articles/` không work nếu vault không có folder đó).

→ Khuyên: agent vault-specific để ở `.claude/agents/`. Agent generic (vd `git-helper`) để global.

---

## Bước 7 — Agent memory

Khi agent học từ feedback, nó cần memory persist:

```bash
mkdir -p .claude/agent-memory/article-ingest
touch .claude/agent-memory/article-ingest/MEMORY.md
```

`.claude/agent-memory/article-ingest/MEMORY.md`:

```markdown
# Memory — article-ingest agent

- [Default audience cho summary](feedback_default_audience.md) — user thường ingest cho doanh nhân, không cần hỏi
- [Skip concept obvious](feedback_skip_obvious_concept.md) — concept "MVP" / "startup" đã có rồi, skip
```

`.claude/agent-memory/article-ingest/feedback_default_audience.md`:

```markdown
---
name: default-audience
description: User default ingest cho doanh nhân
metadata:
  type: feedback
---

User mặc định ingest article về business/startup cho audience doanh nhân Việt. Không cần hỏi mỗi lần "audience nào".

**Why**: tránh repetitive question, user feedback "cứ ingest đi".
**How to apply**: skip clarifying question về audience, default doanh nhân.
```

Memory load auto mỗi lần agent run.

---

## Bước 8 — List agents

Trong Claude Code:

```
/agents
```

Hiển thị list agents available (custom + built-in).

Hoặc check file:

```bash
ls .claude/agents/
ls ~/.claude/agents/
```

---

## Bước 9 — Agent test nâng cao

Tạo agent xong, test edge case:

```
> Ingest article không tồn tại
```

Agent should fail graceful: "File không tồn tại, skip".

```
> Ingest 2 article cùng URL
```

Agent should detect duplicate: "Đã có source page X cùng URL — skip".

---

## Bước 10 — Khi cần update agent

Agent file là **luật chơi cứng**. Update khi:

- Workflow đổi (vd: thêm section mới vào concept page)
- Constraint mới (vd: KHÔNG link tới source A vì lý do X)
- Edge case mới phát hiện

Update file → test lại. Agent có history (Git) → revert được nếu update sai.

---

## Tiếp theo

Đọc tiếp: [[03-skill-la-gi]] — Skill khác agent thế nào.
