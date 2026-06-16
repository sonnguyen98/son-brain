---
title: Cài plugins Obsidian
type: cai-dat
created: 2026-05-29
updated: 2026-05-29
phan: 01
---

# Cài plugins Obsidian

## Trước đó

[[04-cai-mcp-servers]] — MCP đã hiểu (cài hoặc skip).

---

## Plugin Obsidian — overview

Obsidian có 2 loại plugin:

1. **Core plugins** — đi kèm app, chỉ cần bật. Vd: Graph view, Backlinks, Tags, Search.
2. **Community plugins** — do dev cộng đồng làm, cài qua marketplace. Vd: Dataview, Excalidraw, Calendar.

Mặc định Obsidian disable Community plugins (security). Phải bật trước.

---

## Bước 1 — Bật Community plugins

**Settings → Community plugins → Turn on community plugins**

Click **Turn on community plugins**. Bỏ qua warning.

→ Bây giờ tab Community plugins active. Click **Browse** để xem marketplace.

---

## Bước 2 — Plugin BẮT BUỘC cho AI-first wiki

### A. Obsidian Web Clipper (extension Chrome/Firefox)

Lưu article web về vault dạng markdown. KHÔNG cài qua Obsidian marketplace — cài extension browser.

Chrome:
1. Vào https://obsidian.md/clipper
2. Click **Add to Chrome**
3. Pin extension lên toolbar

Firefox:
1. Vào Firefox Add-ons → tìm "Obsidian Web Clipper"
2. Add to Firefox

Sau khi cài, click icon Web Clipper trên page bất kỳ → article tải về vault dạng `.md`.

Cài đặt: click icon → Settings:
- **Vault**: chọn vault Brain
- **Folder**: `raw/articles/` (gom 1 chỗ)
- **Template**: default OK
- **Tags**: `clipped`
- **Filename format**: `{title}` (giữ title gốc)

### B. Dataview (community plugin)

Query frontmatter YAML qua DQL/JS.

Cài:
1. Settings → Community plugins → Browse
2. Tìm "Dataview"
3. **Install** → **Enable**

Test: tạo file `wiki/test-dataview.md`:

```markdown
# Test Dataview

\`\`\`dataview
LIST FROM "wiki/concepts"
LIMIT 5
\`\`\`
```

(Bỏ backslash trước backtick — đó là escape cho file này, file thật không cần)

Save → switch sang Reading mode (Cmd+E) → thấy list 5 concept đầu.

Dataview rất mạnh — sau này dùng để build dashboard.

### C. Templater (community)

Cài template tự động khi tạo file mới.

Cài: Settings → Community plugins → Browse → "Templater" → Install → Enable.

Config:
- Settings → Templater → Template folder location: `templates/`
- Settings → Templater → Trigger Templater on new file creation: On

Sau khi cài, mỗi lần tạo file mới trong folder cụ thể, template auto apply.

---

## Bước 3 — Plugin TUỲ CHỌN

### D. Calendar

Sidebar lịch tháng. Click ngày → mở/tạo daily note.

Cài: Browse → "Calendar" → Install → Enable.

### E. Excalidraw

Vẽ sketch / diagram trong Obsidian.

Cài: Browse → "Excalidraw" → Install → Enable.

Tạo file Excalidraw: Cmd+P → "Excalidraw: Create new drawing" → vẽ → save → embed vào page khác bằng `![[<file>.excalidraw]]`.

### F. Advanced Tables

Edit bảng markdown dễ hơn (tab nhảy cột, format auto).

Cài: Browse → "Advanced Tables" → Install → Enable.

### G. Style Settings

Tinh chỉnh CSS theme qua UI (không cần code).

Cài: Browse → "Style Settings" → Install → Enable.

### H. Tasks

Quản lý todo list trong note.

Cài: Browse → "Tasks" → Install → Enable.

---

## Bước 4 — Plugin KHÔNG khuyên

Tránh các plugin sau cho AI-first wiki:

| Plugin | Lý do tránh |
|---|---|
| **Note Refactor** | AI làm thay |
| **Auto Note Generator** (AI cũ) | Dùng Claude Code thay |
| **GPT plugin** | Outdated, dùng Claude Code |
| **Obsidian Git** trong vault Brain | Vault to → commit chậm. Backup ngoài (xem [[05-bao-tri-lint/02-backup-icloud-git]]) |
| **Sync plugin community** | Conflict với iCloud sync |

---

## Bước 5 — Core plugins essential

Settings → Core plugins. Bật:

| Plugin | Tác dụng |
|---|---|
| **File explorer** | Sidebar folder tree |
| **Search** | Cmd+Shift+F search |
| **Quick switcher** | Cmd+O fuzzy search file |
| **Graph view** | Visualize wikilink |
| **Backlinks** | Xem page nào link tới page hiện tại |
| **Outline** | Sidebar H1/H2/H3 trong file |
| **Tags** | Sidebar danh sách tag |
| **Daily notes** | Note theo ngày (optionally) |
| **Templates** | Template snippet (built-in, ngoài Templater) |
| **Word count** | Đếm từ |
| **Files** | Quản lý attachment |

Tắt nếu không dùng:
- **Audio recorder** (chỉ dùng cho người record voice note)
- **Slides** (Marp tốt hơn)
- **Workspaces** (advanced)

---

## Bước 6 — Cấu hình Graph view

Settings → Core plugins → Graph view (click icon Settings bên cạnh).

### Filters

- **Search**: `path:wiki` (chỉ hiện file trong wiki, exclude raw/)
- **Existing files only**: On
- **Orphans**: On (xem file mồ côi)
- **Attachments**: Off

### Color groups

(Add khi vault > 100 file)

```
tag:#framework           → xanh dương
tag:#chuong-trinh        → đỏ/cam
tag:#storytelling        → xanh lá
tag:#signature-ptl       → vàng
path:wiki/sources/       → xám mờ
```

Click "+" trong Color groups để add.

### Forces

- **Center force**: 0.3
- **Repel force**: 5
- **Link force**: 1
- **Link distance**: 250

Tinh chỉnh sau.

---

## Bước 7 — Hotkey hữu ích

Settings → Hotkeys. Đề xuất:

| Action | Hotkey |
|---|---|
| Open graph view | Cmd+G |
| Toggle reading mode | Cmd+E |
| Switch between notes | Cmd+[, Cmd+] |
| Insert link | Cmd+K |
| Quick switcher | Cmd+O |
| Search | Cmd+Shift+F |
| Search current file | Cmd+F |
| Templater: Insert template | Cmd+Alt+T |

Sửa hotkey: Settings → Hotkeys → tìm action → click pencil icon → gõ hotkey mới.

---

## Bước 8 — Backup config plugins

`.obsidian/community-plugins.json` chứa list plugin đã cài. Khi setup vault mới, copy file này từ vault cũ:

```bash
cp "Longpt's Brain/.obsidian/community-plugins.json" "Longpt's New-Vault/.obsidian/"
```

Sau đó mở vault mới → Obsidian auto download plugin theo list.

Quy tắc: settings layout, hotkey → unique per vault. Plugin list → có thể share.

---

## Bước 9 — Verify setup OK

Sau Phần 01 cài đặt xong:

- [x] Obsidian cài
- [x] iCloud sync OK
- [x] Claude Code CLI cài
- [x] MCP servers (optionally)
- [x] Community plugins bật
- [x] Web Clipper extension cài
- [x] Dataview plugin
- [x] Graph view config

OK → sang Phần 02 build vault Brain.

---

## Tiếp theo

Đọc tiếp: [[02-vault-dau-tien-brain/01-tao-vault-brain]] — Build vault Brain đầu tiên.
