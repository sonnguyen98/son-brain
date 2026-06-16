---
title: Cài Obsidian
type: cai-dat
created: 2026-05-29
updated: 2026-05-29
phan: 01
---

# Cài Obsidian

## Trước đó

[[00-triet-ly/04-3-lop-raw-wiki-schema]] — bạn đã hiểu mô hình 3 lớp.

---

## Tại sao Obsidian

Đây là wiki app **local-first** + **markdown plain text** + **graph view native** + **plugin community sôi nổi**. Không phải SaaS (như Notion) — file của bạn nằm trên ổ cứng, bạn sở hữu 100%.

Alternatives:
- **Notion**: tiện multi-user nhưng không local-first, không markdown plain, AI khó đọc
- **Logseq**: outliner-first (bullet), không phù hợp wiki page-based
- **Roam Research**: outliner + giá cao + không local
- **Foam (VS Code)**: nhẹ nhưng không có graph view tốt

→ Obsidian là lựa chọn tốt nhất cho AI-first wiki concept-first.

---

## Bước 1 — Tải Obsidian

### macOS

1. Vào https://obsidian.md
2. Click **Download for macOS**
3. Mở file `.dmg` đã tải
4. Kéo Obsidian.app vào `Applications/`
5. Mở Launchpad → click Obsidian

### Windows

1. Vào https://obsidian.md
2. Click **Download for Windows**
3. Chạy file `.exe` installer
4. Next → Next → Finish

### Linux

1. Vào https://obsidian.md
2. Tải file `.AppImage` hoặc `.deb` (Ubuntu/Debian) / `.snap`
3. Chạy hoặc `sudo dpkg -i obsidian_*.deb`

---

## Bước 2 — Mở Obsidian lần đầu

Mở Obsidian. Bạn thấy màn hình chào:

```
Quick start
  Create new vault
  Open folder as vault
  Open existing vault
```

Chưa làm gì vội. Chúng ta sẽ tạo vault sau khi setup iCloud xong (file kế tiếp).

---

## Bước 3 — Tài khoản Obsidian (tuỳ chọn)

Obsidian **không bắt buộc tạo account**. Bạn có thể dùng vĩnh viễn miễn phí.

Tạo account chỉ cần khi bạn muốn:
- **Obsidian Sync** ($10/tháng) — sync end-to-end encrypted giữa máy (nhưng chúng ta dùng iCloud thay, free)
- **Obsidian Publish** ($20/tháng) — publish vault thành website
- **Catalyst License** ($25 one-time) — early access plugins

→ Khuyên: **không tạo account** cho người mới. Dùng iCloud sync (file kế tiếp).

---

## Bước 4 — Settings cơ bản

Mở **Settings** (Cmd+, trên Mac / Ctrl+, trên Win):

### General

- **Language**: English (giao diện) hoặc Vietnamese nếu muốn
- **Vim key bindings**: Off (trừ khi bạn dùng Vim)
- **Default editor mode**: **Source mode** (xem markdown plain)

### Editor

- **Show line number**: On
- **Readable line length**: On (giới hạn 80 char dòng dễ đọc)
- **Strict line breaks**: On
- **Use legacy editor**: Off

### Files & links

- **New link format**: **Shortest path when possible** (vd `[[Page]]` thay vì `[[folder/Page]]`)
- **Use [[Wikilinks]]**: On (BẮT BUỘC — chúng ta dùng wikilink)
- **Default location for new attachments**: `In the folder specified below` → set thành `raw/assets/`
- **Detect all file extensions**: On (để thấy PDF, ảnh, PowerPoint trong vault)

### Appearance

- **Theme**: Default (hoặc dark theme nếu thích)
- **Font**: Default
- **Translucent window**: Off (tiết kiệm GPU)

### Hotkeys

Mặc định OK. Sau này tinh chỉnh.

---

## Bước 5 — Hiểu cấu trúc Obsidian

### Vault là gì

Vault = 1 folder trên ổ cứng chứa các file `.md`. Obsidian KHÔNG có database — mỗi page là 1 file markdown plain text.

Vault location: bạn quyết. Anh Long đặt trong iCloud:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Brain/
```

### Hidden folder `.obsidian/`

Mỗi vault có folder `.obsidian/` chứa:
- `app.json` — settings vault
- `community-plugins.json` — danh sách plugin đã cài
- `workspace.json` — layout window
- `graph.json` — settings graph view

Folder này gắn với vault, không share giữa các vault. Đó là lý do mỗi vault có settings riêng.

### File markdown plain

Mỗi page Obsidian là 1 file `.md` đọc được bằng bất kỳ text editor nào (VS Code, Sublime, vim). Không vendor lock-in.

Mở 1 file `.md` bằng VS Code:

```bash
code "Longpt's Brain/wiki/concepts/Bộ não thứ 2.md"
```

Thấy nội dung là markdown plain — đó là điều quan trọng nhất.

---

## Bước 6 — Kiểm tra cài đặt

Tạo 1 vault test:
1. Open Obsidian
2. **Create new vault** → tên `test-vault`, location `~/Documents/test-vault`
3. Tạo file mới: Cmd+N → tên `Hello.md`
4. Gõ nội dung:
   ```markdown
   # Hello
   
   Đây là [[note-2]] đầu tiên của tôi.
   ```
5. Lưu (Cmd+S)
6. Click vào `[[note-2]]` → tạo file mới

Nếu chạy được — Obsidian cài thành công.

Xoá `test-vault` (không cần nữa):

```bash
rm -rf ~/Documents/test-vault
```

---

## Troubleshooting

### Obsidian không mở được trên Mac

Mac báo "App damaged, cannot open":

```bash
xattr -cr /Applications/Obsidian.app
```

Mở lại — OK.

### Vault load chậm

Vault > 1000 file load chậm:
- Tắt plugin không dùng
- Disable "Show file extensions" tạm
- Restart Obsidian

### Graph view rối

Vault > 500 page → graph view rối:
- Settings → Core plugins → Graph view → Filters → exclude `path:.obsidian/`
- Color groups: tag `#framework` → xanh, tag `#chuong-trinh` → đỏ (xem [[02-vault-dau-tien-brain/03-cau-truc-folder]])

---

## Tiếp theo

Đọc tiếp: [[02-cai-icloud-sync]] — Cài iCloud Drive để sync vault giữa Mac + iPhone.
