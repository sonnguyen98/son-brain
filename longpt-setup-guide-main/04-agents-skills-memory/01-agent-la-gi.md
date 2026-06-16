---
title: Agent là gì
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 04
---

# Agent là gì

## Trước đó

[[03-mo-rong-multi-vault/05-cross-vault-query]] — bạn có multi-vault chạy được.

---

## Vấn đề

Bạn đang dùng Claude Code. Mọi câu hỏi đi qua **main loop** — Claude nghe → tool → trả lời.

Sau 3-6 tháng, bạn phát hiện:
- Có việc lặp đi lặp lại (ingest source, viết blog, audit wiki)
- Mỗi việc cần "set up context" — đọc CLAUDE.md, đọc index, đọc rule
- Tốn token, chậm, error-prone

→ Pivot: **tạo agent** cho mỗi workflow lặp.

---

## Agent là gì

**Agent** = một "sub-Claude" được khai báo trước với:

1. **System prompt riêng** — luật chơi cho agent đó
2. **Tools subset** — chỉ tools agent cần (không phải tất cả)
3. **Description** — khi nào main loop nên gọi agent này

Khi bạn nói "ingest source X" trong main loop:
- Main loop nhận diện: "à có agent `raw-chunk-ingest-pipeline` phù hợp"
- Main loop **launch agent** với prompt cụ thể
- Agent chạy độc lập (separate context window)
- Agent trả về kết quả
- Main loop summarize cho bạn

---

## Agent vs main loop

| Main loop | Agent |
|---|---|
| Context window chung với bạn | Context window riêng |
| Mọi tool available | Tool subset |
| Conversation dài | Single-purpose burst |
| Bạn thấy mọi tool call | Bạn thấy chỉ kết quả cuối |
| Cost: tracked main session | Cost: tracked riêng |

---

## Khi nào dùng agent

3 use case chính:

### A. Workflow lặp lại

Ingest source mới → cùng 1 quy trình mỗi lần. Tạo agent `raw-chunk-ingest-pipeline`.

### B. Việc tốn token nặng

Audit wiki 1000 page → đọc nhiều, tổng hợp dài. Tạo agent `wiki-audit` chạy riêng, không bloat main context.

### C. Domain expertise

Viết blog tâm sự PTL style → cần style guide đặc thù. Tạo agent `blog-writer-PTL-style` chứa system prompt 200 dòng quy tắc.

---

## Khi KHÔNG dùng agent

### Việc đơn giản 1 lần

Hỏi "concept X là gì?" → main loop trả lời trực tiếp, không cần agent.

### Việc cần context của bạn

"Tổng hợp 5 query gần đây tôi đã hỏi" → cần context main loop (agent không thấy).

### Việc nhỏ < 100 token output

Tạo agent overhead lớn hơn việc. Main loop nhanh hơn.

---

## Các agent vault anh Long có

Để tham khảo, anh Long có 6 custom agents:

| Agent | Use case |
|---|---|
| `blog-writer-PTL-style` | Viết blog tâm sự PTL style cho FB/website |
| `longpt-sale-page` | Viết sale page 16 bước Jay Abraham style |
| `raw-chunk-ingest-pipeline` | Pipeline ingest source raw lớn |
| `webcake-pke-builder` | Convert sale page Markdown → Webcake .pke template |
| `youtube-channel-video-exporter` | Export video YouTube channel → Excel |
| `youtube-channel-wiki-builder` | Ingest YouTube channel → wiki YouTube |

Mỗi agent có system prompt 100-500 dòng + lifecycle workflow rõ.

---

## Agent built-in của Claude Code

Ngoài custom agents, Claude Code có agents built-in:

| Agent | Use case |
|---|---|
| `claude` | Default catch-all |
| `general-purpose` | Multi-step research / search |
| `Explore` | Fast read-only search code |
| `Plan` | Design implementation plan |
| `claude-code-guide` | Hỏi về Claude Code/SDK/API |
| `statusline-setup` | Configure status line |

---

## Cách agent hoạt động

Bạn type:

```
> Viết blog cho FB tối nay về concept "Bộ não thứ 2"
```

Main loop Claude:
1. Đọc list agents available
2. Match: "blog-writer-PTL-style" có description "viết blog cho thương hiệu cá nhân PTL"
3. Quyết launch agent với prompt:

```
Spec: blog FB tối nay
Concept: "Bộ não thứ 2"
Audience: doanh nhân (default per memory)
Tone: tâm sự PTL style
Word count: 1500
```

4. Agent chạy:
   - Đọc CLAUDE.md
   - Đọc concept page Bộ não thứ 2
   - Apply 8 nguyên tắc PTL
   - Viết draft
   - Optimize SEO
   - Return blog markdown

5. Main loop nhận kết quả, summarize cho bạn:

```
✅ Viết xong blog 1532 từ "Bộ não thứ 2 — vũ khí thầm lặng của doanh nhân ASEAN"
Lưu vào: blog-drafts/2026-05-29-bo-nao-thu-2.md
```

---

## Agent context isolation

Agent có **context window riêng** — không thấy conversation main loop.

Lợi:
- Agent không bị nhiễu bởi context cũ
- Main loop không tốn token kết quả agent đầy đủ (chỉ summary)

Hại:
- Phải pass đủ context khi launch agent
- Agent không thể tham chiếu "câu hỏi bạn vừa hỏi"

Quy tắc: prompt agent **self-contained** — agent đọc xong là làm được, không cần hỏi lại.

---

## Agent vs Skill

Cả 2 đều là tự động hoá. Khác:

| Agent | Skill |
|---|---|
| Sub-Claude với system prompt | Workflow markdown user định nghĩa |
| Tools subset | Tools full |
| Context isolation | Context chung main loop |
| Heavyweight | Lightweight |
| `.claude/agents/<name>.md` | `.claude/skills/<name>/SKILL.md` |
| Gọi bằng Agent tool | Gọi bằng `/skill-name` |

Chi tiết skill ở [[03-skill-la-gi]].

---

## Agent file structure

Agent định nghĩa ở `.claude/agents/<agent-name>.md`:

```markdown
---
name: my-agent
description: "Use this agent when X. Examples..."
tools: ["Read", "Write", "Edit", "Bash"]
model: sonnet
---

# Agent system prompt

[Mô tả vai trò agent]

## Workflow

[Quy trình agent làm việc]

## Style guide

[Tone, voice, format]

## Constraints

[Rule cứng — KHÔNG được làm gì]
```

Mỗi vault có `.claude/agents/` riêng. User-level: `~/.claude/agents/` global.

---

## Memory cho agent

Mỗi agent có thể có **memory riêng** ở `.claude/agent-memory/<agent-name>/MEMORY.md` + file con.

Memory persist cross-session — agent học từ feedback bạn.

Vd anh Long có:
- `.claude/agent-memory/blog-writer-PTL-style/feedback_blog_style_from_corpus.md`
- `.claude/agent-memory/youtube-channel-wiki-builder/channel_longguru.md`
- `.claude/agent-memory/youtube-channel-wiki-builder/feedback_transcript_fetch.md`

---

## Chi phí agent

Mỗi launch agent = 1 new context window = tốn token riêng.

Quy tắc tiết kiệm:
- Agent prompt ngắn gọn nhưng đủ
- Agent system prompt < 500 dòng
- Không spam agent calls (1 task / 1 agent / 1 run)

---

## Tiếp theo

Đọc tiếp: [[02-tao-agent-dau-tien]] — Build agent đầu tiên.
