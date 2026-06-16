---
title: Cài Claude Code CLI
type: cai-dat
created: 2026-05-29
updated: 2026-05-29
phan: 01
---

# Cài Claude Code CLI

## Trước đó

[[02-cai-icloud-sync]] — vault đã sync iCloud.

---

## Tại sao Claude Code CLI

Claude có nhiều entry point:
- **claude.ai** — chat web (không edit file trực tiếp)
- **Claude Desktop** — app desktop (có MCP nhưng giới hạn)
- **Claude Code CLI** — terminal (đầy đủ tools, đọc/ghi file, chạy command)
- **Claude API** — gọi từ code

→ Cho AI-first wiki cần đọc/ghi 1000 file: **Claude Code CLI** là lựa chọn đúng.

---

## Bước 1 — Tài khoản Anthropic

Vào https://claude.ai → Sign up bằng email hoặc Google.

Có 3 gói:
- **Free** — chat web, không đủ cho heavy use
- **Pro $20/tháng** — 5× usage, đủ cho cá nhân
- **Max $100/tháng** — 20× usage, đủ cho người dùng nặng
- **API** — pay-per-token, dùng cho dev

→ Bắt đầu: **Pro $20/tháng** (có thể upgrade lên Max sau).

Claude Code dùng credentials của Pro/Max plan — không tốn token riêng (theo policy hiện tại).

---

## Bước 2 — Cài Node.js (yêu cầu)

Claude Code chạy trên Node.js. Cài Node 18+:

### macOS (Homebrew)

```bash
brew install node
```

### Windows

Tải https://nodejs.org → installer LTS.

### Linux (Ubuntu/Debian)

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Verify

```bash
node --version    # v20.x.x hoặc cao hơn
npm --version     # 10.x.x
```

---

## Bước 3 — Cài Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
```

Nếu lỗi permission trên Mac/Linux:

```bash
sudo npm install -g @anthropic-ai/claude-code
```

Verify:

```bash
claude --version
```

Expected: hiển thị version number.

---

## Bước 4 — Login Claude Code lần đầu

```bash
claude
```

Lần đầu chạy, Claude sẽ:
1. Mở browser → login Anthropic account
2. Authorize Claude Code access
3. Quay về terminal, ready

Sau khi login OK, prompt hiển thị:

```
╭───────────────────────────────────────────────╮
│  Claude Code 1.0.x                            │
│                                               │
│  Type your question or task                   │
╰───────────────────────────────────────────────╯

> _
```

---

## Bước 5 — Test Claude Code

Trong terminal, đang ở folder vault:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Brain"
claude
```

Trong prompt:

```
> List 5 files trong wiki/ folder
```

Claude sẽ:
- Yêu cầu permission dùng tool `Bash` (lần đầu) → bạn approve
- Chạy `ls wiki/`
- Trả về list

OK — Claude Code hoạt động.

Thoát Claude Code: gõ `/exit` hoặc Ctrl+D.

---

## Bước 6 — Hiểu permission system

Claude Code có **permission mode** kiểm soát Claude làm gì:

- **default** — Claude hỏi mỗi tool call
- **acceptEdits** — auto accept Edit/Write
- **bypassPermissions** — auto accept tất cả (danger)
- **plan** — Claude lập plan, không execute

Mặc định **default**. Bạn approve từng action.

Để Claude tự chạy 1 chuỗi action không cần hỏi mỗi bước:
- Approve **per session** (chỉ session hiện tại)
- Approve **forever** (lưu vào `.claude/settings.local.json`)

Khuyên: lần đầu chọn **per session**, sau khi trust → forever.

---

## Bước 7 — Folder `.claude/` trong vault

Khi bạn dùng Claude Code trong 1 folder, Claude tạo `.claude/` để lưu:

```
.claude/
├── settings.json           # settings vault
├── settings.local.json     # settings local (gitignored)
├── agents/                 # custom agents
└── commands/               # slash commands
```

File chính:

### `settings.json`

Cài chung cho mọi user (commit Git):

```json
{
  "permissions": {
    "allow": ["Bash(ls *)", "Read", "Edit", "Write"]
  }
}
```

### `settings.local.json`

Cài cho riêng bạn (gitignored):

```json
{
  "permissions": {
    "allow": ["Bash(rm *)"]
  }
}
```

Quy ước: tool dùng chung → settings.json. Tool risky / personal → settings.local.json.

---

## Bước 8 — CLAUDE.md trong vault

Khi Claude Code chạy trong 1 folder, nó tự đọc `CLAUDE.md` nếu có. Đó là **luật chơi vault**.

Bạn chưa có CLAUDE.md ở Brain — chúng ta sẽ tạo ở [[02-vault-dau-tien-brain/02-claude-md-template]].

---

## Bước 9 — Slash commands hữu ích

Trong Claude Code prompt:

| Lệnh | Tác dụng |
|---|---|
| `/help` | Hiện help |
| `/exit` | Thoát |
| `/clear` | Clear màn hình |
| `/agents` | List agents available |
| `/skills` | List skills available |
| `/memory` | Xem memory |
| `/config` | Cài đặt |

Tạo slash command custom ở [[04-agents-skills-memory/02-tao-agent-dau-tien]].

---

## Bước 10 — Verify đầy đủ

Tóm tắt cần có sau Phần 03:

- [x] Node.js cài
- [x] Claude Code CLI cài
- [x] Login Anthropic OK
- [x] Test Claude trong vault folder OK
- [x] Hiểu permission system
- [x] Hiểu `.claude/` folder

OK → sang file kế.

---

## Troubleshooting

### `claude: command not found`

NPM không add Claude Code vào PATH. Thêm:

```bash
echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Login lặp lại nhiều lần

Xoá credentials cũ:

```bash
rm -rf ~/.claude/credentials.json
claude   # login lại
```

### Claude phản hồi chậm

- Check internet (Claude cần kết nối)
- Pro plan: chờ usage refresh (5h reset)
- Upgrade lên Max nếu hit limit thường

### "Rate limit" error

Đã hit quota của Pro. Đợi 5 giờ hoặc upgrade Max.

---

## Tiếp theo

Đọc tiếp: [[04-cai-mcp-servers]] — Cài MCP servers để Claude truy cập app khác (Gmail, Calendar, Pancake).
