---
title: Cài MCP servers
type: cai-dat
created: 2026-05-29
updated: 2026-05-29
phan: 01
---

# Cài MCP servers

## Trước đó

[[03-cai-claude-code]] — Claude Code chạy được.

---

## MCP là gì

**MCP** = **Model Context Protocol** — chuẩn mở do Anthropic phát hành để LLM (Claude) kết nối với app khác qua server trung gian.

Pattern:
```
Claude ←→ MCP server ←→ External app (Gmail, Calendar, Pancake, GitHub...)
```

Mỗi MCP server expose 1 set tool. Claude dùng tool đó như tool built-in.

---

## MCP cho người mới

Bạn không cần MCP để bắt đầu. Phần này là **tuỳ chọn** — bạn có thể skip và quay lại sau.

Khi nào dùng MCP:
- Cần Claude đọc/ghi Gmail
- Cần Claude xem Calendar
- Cần Claude query database (PostgreSQL, BigQuery)
- Cần Claude điều khiển browser
- Cần Claude integrate với app custom

Skip MCP nếu:
- Bạn chỉ làm Brain (knowledge wiki) — tools built-in đủ
- Bạn không có app cần kết nối ngoài

→ Khuyên: **skip section này** lần đầu đọc. Quay lại sau khi vault Brain chạy ổn.

---

## MCP cho anh Long

Anh Long dùng các MCP server sau (ghi tham khảo):

| Server | Tác dụng |
|---|---|
| **Pancake** | Quản lý đơn hàng, customer CRM |
| **Gmail** | Tự động đọc/gửi email |
| **Google Calendar** | Lịch họp, event |
| **Google Drive** | File sharing |
| **Zoom** | Recording, transcript meeting |
| **Higgsfield AI** | Generate ảnh / video |
| **Canva** | Design |
| **Spotify** | Search nhạc |
| **Meta Ads** | Performance ads |
| **Supermetrics** | Marketing data |
| **Claude Preview** | Preview design real-time |
| **Claude in Chrome** | Browser automation |

Mỗi server tự config riêng. Không phải tất cả đều free.

---

## Bước 1 — Xem MCP servers có sẵn

Trong Claude Code:

```
/mcp
```

Hiển thị danh sách MCP đã connect.

Mặc định Claude Code có một số MCP built-in:
- File system (đọc/ghi local)
- Bash (chạy command)
- Web fetch / web search

---

## Bước 2 — Thêm MCP server qua marketplace

Một số MCP có sẵn trong **Claude marketplace**:

1. Mở https://claude.ai/settings/connectors
2. Chọn MCP muốn cài (vd: Google Calendar)
3. Click **Connect**
4. Authorize quyền truy cập

Sau khi authorize, MCP server xuất hiện trong list `/mcp` của Claude Code.

---

## Bước 3 — Thêm MCP server qua config file

MCP custom (vd: Pancake) cài qua file:

```
~/.claude/mcp.json
```

Format:

```json
{
  "mcpServers": {
    "pancake": {
      "command": "npx",
      "args": ["-y", "@pancake/mcp-server"],
      "env": {
        "PANCAKE_API_KEY": "your-key-here"
      }
    }
  }
}
```

Sau khi save, restart Claude Code → MCP server load.

---

## Bước 4 — Verify MCP

Trong Claude Code:

```
> Có MCP nào kết nối?
```

Claude liệt kê. Hoặc:

```
/mcp
```

Test 1 tool:

```
> Đọc email mới nhất của tôi
```

Claude dùng MCP Gmail (nếu đã connect) trả về.

---

## Bước 5 — Tránh quá nhiều MCP

Mỗi MCP cộng thêm context. Nhiều MCP = Claude chậm + token đắt.

Khuyên:
- Bắt đầu: 0 MCP. Dùng tools built-in.
- Khi cần app cụ thể → add 1 MCP đó.
- Đừng cài cho có.

---

## MCP cho vault setup guide

Vault `Longpt's Setup-Guide` này KHÔNG cần MCP. Tools built-in (Read, Write, Edit, Bash) đủ.

---

## Bước 6 — Disable MCP tạm thời

Nếu MCP gây lỗi, disable qua config:

```json
{
  "mcpServers": {
    "pancake": {
      "disabled": true
    }
  }
}
```

Restart Claude Code.

---

## Khi nào dùng MCP marketplace vs config

| Trường hợp | Cách cài |
|---|---|
| MCP phổ thông (Google, GitHub, Slack) | Marketplace (1 click) |
| MCP custom của bạn (Pancake nội bộ) | Config file |
| MCP đang dev (chưa publish) | Config file |
| Bạn không muốn cài toàn cục, chỉ cho 1 vault | `.claude/mcp.json` trong vault |

---

## Pancake MCP — chi tiết cho anh Long

(Phần này anh Long dùng, người mới skip)

Anh Long có MCP Pancake để quản lý:
- Manage orders (lấy danh sách đơn, status)
- Manage customers (CRM)
- Manage products
- Manage warehouses (kho)
- Analytics

Config trong `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "pancake": {
      "command": "node",
      "args": ["/path/to/pancake-mcp/dist/index.js"],
      "env": {
        "PANCAKE_API_TOKEN": "...",
        "PANCAKE_SHOP_ID": "..."
      }
    }
  }
}
```

Khi vault Marketing query "đơn nào chốt tuần này?", Claude dùng MCP Pancake auto pull data.

Chi tiết quy ước Pancake API ở `Longpt's Marketing/CLAUDE.md` mục 11.

---

## Tiếp theo

Đọc tiếp: [[05-cai-plugins-obsidian]] — Cài plugin Obsidian (Web Clipper, Dataview, Excalidraw).
