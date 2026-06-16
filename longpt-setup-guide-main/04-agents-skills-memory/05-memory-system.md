---
title: Memory system
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 04
---

# Memory system Claude

## Trước đó

[[04-tao-skill-dau-tien]] — bạn đã build skill.

---

## Vấn đề: Claude quên giữa các session

Bạn nói với Claude:

```
> Tôi tên Anna, làm marketing, ưu tiên tiếng Việt 100%
```

Sau khi đóng terminal, bạn mở session mới — Claude **không nhớ** bạn là ai. Phải nói lại.

Sau 6 tháng, bạn lặp lại 1000 lần các info căn bản → tốn token + UX kém.

---

## Memory system — giải pháp

Claude có **persistent memory** file-based:

```
~/.claude/projects/<project-name>/memory/
├── MEMORY.md             # index — auto load mỗi session
├── user_identity.md      # ai là user
├── feedback_X.md         # feedback rule
├── project_Y.md          # project context
└── reference_Z.md        # external reference
```

Mỗi session Claude tự đọc `MEMORY.md` → biết context bạn.

---

## 4 loại memory

### 1. User — bạn là ai

Background, role, preferences, expertise.

Vd:
```markdown
---
name: user-identity
description: User là marketer
metadata:
  type: user
---

User Anna, marketing manager 5 năm experience, làm B2B SaaS, ưu tiên Vietnamese 100% content. 
```

### 2. Feedback — rule từ bạn

Khi bạn correct AI hoặc confirm cách làm.

Vd:
```markdown
---
name: no-emoji-in-blog
description: User KHÔNG dùng emoji trong blog
metadata:
  type: feedback
---

User KHÔNG dùng emoji trong blog content. 

**Why**: blog tone professional, không casual.
**How to apply**: skip emoji khi viết blog, dùng plain text.
```

### 3. Project — context dự án hiện tại

Deadline, stakeholder, motivation.

Vd:
```markdown
---
name: launch-q2-2026
description: Launch khoá EMM Q2 2026
metadata:
  type: project
---

User đang launch khoá Email Marketing Mastery Q2 2026. Deadline ngày 15/06/2026.

**Why**: doanh thu Q2 commit $50k.
**How to apply**: ưu tiên content/sale page liên quan EMM. Flag deadline khi đề xuất task.
```

### 4. Reference — pointer ra external system

URL, tool, repo cần biết.

Vd:
```markdown
---
name: ga4-dashboard
description: GA4 dashboard cho B2B
metadata:
  type: reference
---

Dashboard analytics B2B ở https://analytics.google.com/u/0/p1234567. 
Track lead form opt-in, content engagement.
```

---

## Setup memory directory

Lần đầu, Claude tự tạo:

```
~/.claude/projects/<encoded-project-path>/memory/
```

Path encoding: hash của project path.

Vd vault `My Brain` path `/Users/anna/.../My Brain` → encoded folder name.

Bạn không cần care path. Claude handle.

---

## Khi nào Claude save memory

3 trường hợp:

### A. Bạn explicit nói

```
> Lưu vào memory: tôi prefer markdown, không HTML
```

Claude tạo file memory.

### B. AI nhận diện info cần save

Lúc bạn nói:
```
> Tôi tên Anna, làm marketing
```

Claude tự nhận diện → save user memory.

### C. Bạn correct AI

Bạn:
```
> Đừng dùng emoji trong blog
```

Claude:
- Lưu feedback memory `no-emoji-in-blog.md`
- Apply rule mọi session sau

---

## Khi nào KHÔNG save

KHÔNG save vào memory:

- Pattern code, convention, architecture, file paths (có thể derive từ codebase)
- Git history, recent changes (có git log)
- Debugging solution (đã fix trong code, có commit message)
- Đã document trong CLAUDE.md
- Ephemeral task details (in-progress work, conversation context)

→ Memory dành cho insight NON-OBVIOUS không thể derive từ code/CLAUDE.md.

---

## MEMORY.md — index

`MEMORY.md` là **index**, không phải nội dung memory. Mỗi entry 1 dòng:

```markdown
- [User identity](user_identity.md) — Anna, marketer B2B SaaS
- [No emoji in blog](feedback_no_emoji.md) — blog tone professional
- [Launch Q2 2026](project_launch_q2.md) — EMM launch deadline 15/06
- [GA4 dashboard](reference_ga4_dashboard.md) — analytics URL
```

Auto load mỗi session — tóm tắt cho Claude biết "user thế nào".

Giữ MEMORY.md ngắn (< 150 entry, 1 dòng mỗi entry).

---

## Bước 1 — Xem memory hiện tại

Trong Claude Code:

```
/memory
```

Hiển thị memory directory + list file.

Hoặc `ls` directory:

```bash
ls -la ~/.claude/projects/*/memory/
```

---

## Bước 2 — Add memory manual

```
> Lưu vào memory: tôi prefer Markdown plain text, không HTML, không emoji.
```

Claude:
- Tạo file `feedback_markdown_plain.md`
- Update `MEMORY.md` index

---

## Bước 3 — Memory cho agent

Agent có memory riêng ở `.claude/agent-memory/<agent-name>/`:

```
.claude/agent-memory/blog-writer-PTL-style/
├── MEMORY.md
├── feedback_blog_style_from_corpus.md
├── project_blog_output_path.md
└── ...
```

Khi agent run, agent đọc memory của agent đó (không phải user memory chung).

Use case: agent tích luỹ pattern feedback per-agent.

---

## Bước 4 — Update / delete memory

### Update

```
> Update memory: thay đổi preference từ "không emoji" sang "emoji OK trong FB post nhưng không trong blog"
```

Claude:
- Edit `feedback_emoji_policy.md`
- Update description

### Delete

```
> Xoá memory về preference emoji
```

Claude:
- Rm `feedback_emoji_policy.md`
- Remove entry trong `MEMORY.md`

---

## Bước 5 — Memory rules quan trọng

### Rule 1 — Save với "why"

Memory cần WHY để Claude judge edge case sau:

Sai:
```
User không dùng PowerPoint.
```

Đúng:
```
User không dùng PowerPoint.
**Why**: chuyển sang Keynote 2022 sau bị crash mất 50 slide.
**How to apply**: tạo deck → suggest Keynote (.key) hoặc Marp markdown, không .pptx.
```

### Rule 2 — Save absolute date

User nói "thứ Năm" → save "2026-03-05".

Tại sao: 6 tháng sau "thứ Năm" không còn nghĩa.

### Rule 3 — Verify memory still valid

Memory cũ có thể stale. Trước khi recommend từ memory:

- Memory nói "file X tồn tại" → check `ls X` trước
- Memory nói "tool Y still work" → grep code xem còn không

Memory snapshot tại điểm thời gian, không phải current state.

### Rule 4 — KHÔNG save bias / negative judgment

Sai:
```
User chậm hiểu concept marketing.
```

→ Negative judgment, không helpful.

Đúng:
```
User mới học marketing online. Cần explanation step-by-step + ví dụ concrete.
```

→ Helpful context, không judgment.

---

## Bước 6 — Auto memory pattern

Khi nào AI auto save (không cần user yêu cầu):

- User explicit corrects ("không, làm thế này")
- User confirms non-obvious approach ("OK, viết cách đó")
- User reveals identity ("tôi là...")
- User mentions external system ("dashboard ở...")

Bạn không phải lo. Claude tự nhận diện và save.

---

## Bước 7 — Memory cross-session

Test:

Session 1:
```
> Tôi tên Bob, làm developer Backend Python
```

Đóng terminal.

Session 2 (mở lại):
```
> Tôi đang setup project mới. Bắt đầu thế nào?
```

Claude đọc memory → biết bạn là Bob developer Python → đề xuất setup Python project (FastAPI, virtualenv, ...) thay vì JavaScript.

---

## Bước 8 — Memory vs vault CLAUDE.md

| CLAUDE.md vault | Memory |
|---|---|
| Vault-specific rules | User-specific rules |
| Schema + workflow | Identity + preferences + project |
| Shared across user | User only |
| Commit Git | Not commit (private) |

CLAUDE.md = "luật chơi vault". Memory = "luật chơi user".

---

## Bước 9 — Anti-pattern memory

### Sai 1 — Memory bloated

User save mọi câu chuyện vào memory → 500+ file → load chậm.

→ Giữ memory < 200 entry. Cleanup định kỳ.

### Sai 2 — Memory duplicate

3 file cùng nói "user prefer Vietnamese" → consolidate thành 1.

→ `/consolidate-memory` skill (Anthropic built-in) help merge duplicates.

### Sai 3 — Memory false fact

Memory nói "user dùng macOS" nhưng user đã chuyển Windows. Stale.

→ Update khi context đổi.

### Sai 4 — Sensitive info trong memory

Password, API key, info confidential → KHÔNG save memory.

→ Save vào password manager (1Password, Bitwarden) thay.

---

## Bước 10 — Memory tools available

| Tool | Use case |
|---|---|
| `/memory` | List memory files |
| Save memory | "Lưu vào memory: ..." |
| Update | "Update memory về X: Y" |
| Delete | "Xoá memory về X" |
| Consolidate | Skill `/consolidate-memory` |
| Find | "Memory về X nói gì?" |

---

## Tiếp theo

Đọc tiếp: [[05-bao-tri-lint/01-lint-wiki-dinh-ky]] — Lint định kỳ giữ vault sạch.
