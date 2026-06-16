---
title: Cài iCloud sync
type: cai-dat
created: 2026-05-29
updated: 2026-05-29
phan: 01
---

# Cài iCloud sync

## Trước đó

[[01-cai-obsidian]] — bạn đã cài Obsidian.

---

## Tại sao iCloud Drive

Bạn muốn vault truy cập được từ:
- Mac (chính)
- iPhone (đọc nhanh trên đường)
- iPad (optionally)

3 lựa chọn:

| Phương án | Chi phí | Ưu | Nhược |
|---|---|---|---|
| **iCloud Drive** | Free 5GB / $1/tháng 50GB / $3/tháng 200GB | Native macOS + iOS, không config | Chỉ user Apple |
| **Obsidian Sync** | $10/tháng | E2E encrypted, multi-device | Trả phí cao |
| **Dropbox / Google Drive** | Free 2GB / $10/tháng | Cross-platform | Conflict file phổ biến |

→ Người dùng Apple: **iCloud Drive** ($1-3/tháng cho 50-200GB) là rẻ + ổn nhất.

→ Không Apple: dùng **Dropbox** (config kỹ tránh conflict).

Giáo trình này hướng dẫn **iCloud Drive**. Phương án khác — bạn tự adapt.

---

## Bước 1 — Bật iCloud Drive trên Mac

System Settings → iCloud → iCloud Drive → **On**

→ Bật **Sync this Mac**.
→ Optionally bật **Optimize Mac storage** (file ít dùng auto offload).

---

## Bước 2 — Bật iCloud Drive trên iPhone

Settings → [Tên bạn] → iCloud → iCloud Drive → **On**.

---

## Bước 3 — Cài Obsidian iOS

App Store → tìm "Obsidian" → cài.

Mở app → cho phép Obsidian truy cập iCloud Drive khi prompt.

---

## Bước 4 — Tạo folder vault trong iCloud Drive

Mở Finder → vào **iCloud Drive**:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/
```

Path này dài. Để truy cập nhanh, drag folder `iCloud~md~obsidian/Documents/` vào Sidebar Finder.

Tạo folder mới:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Brain/
```

(Tên `Longpt's Brain` chỉ là ví dụ — bạn đặt tên vault riêng. Anh Long dùng `<Tên>'s Brain`. Bạn có thể đặt `My Brain`, `Acme Wiki`, etc.)

---

## Bước 5 — Mở vault trong Obsidian

Mở Obsidian → **Open folder as vault** → chọn folder `Longpt's Brain` vừa tạo.

Obsidian sẽ:
- Tạo folder `.obsidian/` ẩn trong vault
- Index nội dung (tạm thời trống)
- Mở workspace

Khi mở folder lần đầu, Obsidian hỏi "Trust author?" → **Trust** (vì là vault bạn tạo).

---

## Bước 6 — Mở vault trên iPhone

Mở Obsidian iOS → **Create new vault** → **Open folder from iCloud Drive** → chọn `Longpt's Brain`.

Sau vài giây, iPhone sync xong → mở được nội dung.

Test: tạo 1 file trên Mac → sau 5-30 giây thấy file đó trên iPhone.

---

## Bước 7 — Quy ước path vault

Khi đề cập path trong terminal hoặc CLAUDE.md, dùng absolute path:

```
/Users/<username>/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Brain/
```

Lưu ý:
- `Mobile Documents` có space → terminal cần quote `"..."` khi cd
- `iCloud~md~obsidian` có `~` ở giữa (không phải home) → giữ nguyên

Test cd:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Brain"
pwd
```

Output:
```
/Users/longpt/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Brain
```

OK.

---

## Bước 8 — Tránh conflict file

iCloud Drive đôi khi tạo file conflict khi 2 máy edit cùng lúc:

```
Concept page (Mac vs iPhone-2026-05-29).md
```

Để tránh:
- **Edit 1 máy 1 lúc**. Không edit cùng file trên Mac + iPhone.
- Trên iPhone, đóng app trước khi mở Mac edit.
- Bật **Settings → iCloud → Optimize Storage** trên Mac để tiết kiệm dung lượng.

Nếu có conflict file:
- Mở 2 file so sánh
- Merge thủ công vào file gốc
- Xoá file conflict

---

## Bước 9 — Backup ngoài iCloud

iCloud không phải backup chính thức. Khi xoá file trên 1 máy → xoá trên cloud → 30 ngày sau biến mất.

**Phải có backup riêng**:

### Option A — Time Machine (Mac)

Cắm ổ cứng external → System Settings → Time Machine → Add backup disk. Auto backup mỗi giờ.

### Option B — Git repo private (khuyên)

Tạo private GitHub repo `longpt-vault-backup` → push vault lên hàng tuần. Chi tiết ở [[05-bao-tri-lint/02-backup-icloud-git]].

### Option C — rsync sang ổ cứng external

```bash
rsync -avu "/Users/longpt/Library/Mobile Documents/iCloud~md~obsidian/Documents/" /Volumes/Backup/obsidian-vaults/
```

Chạy hàng tuần (cron job).

---

## Bước 10 — Verify sync OK

Test cuối:

1. Mac: tạo file `wiki/test-sync.md` với nội dung "Hello from Mac"
2. Đợi 30 giây
3. iPhone: mở Obsidian → tìm `test-sync.md` → thấy "Hello from Mac" → OK
4. Xoá `test-sync.md` trên cả 2 máy

---

## Troubleshooting

### iCloud sync không hoạt động

Mac: Apple menu → System Settings → iCloud → status "Pause" → Resume.

Hoặc force sync:

```bash
killall bird   # iCloud Drive daemon
```

Sau 30 giây, bird auto restart và sync.

### File không hiện trên iPhone

Settings → iCloud → iCloud Drive → check Obsidian app có trong list. Nếu không → uninstall + reinstall app.

### Dung lượng iCloud hết

System Settings → iCloud → Manage Account Storage. Mua thêm: 50GB ($1/tháng), 200GB ($3), 2TB ($10).

Anh Long dùng gói 2TB cho 14 vault (~3-5GB).

---

## Tiếp theo

Đọc tiếp: [[03-cai-claude-code]] — Cài Claude Code CLI.
