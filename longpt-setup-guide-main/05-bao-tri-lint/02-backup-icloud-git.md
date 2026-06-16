---
title: Backup iCloud + Git
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 05
---

# Backup iCloud + Git

## Trước đó

[[01-lint-wiki-dinh-ky]] — bạn đã biết lint định kỳ.

---

## iCloud KHÔNG phải backup

iCloud Drive sync file giữa máy. Khi bạn xoá file trên 1 máy → xoá trên cloud → xoá trên máy khác.

30 ngày sau iCloud Trash auto empty → file biến mất vĩnh viễn.

→ iCloud = sync, không phải backup.

---

## Strategy 3-2-1

Quy tắc backup truyền thống:
- **3** copies dữ liệu
- **2** loại media khác nhau
- **1** copy offsite

Cho vault Obsidian:
- Copy 1: iCloud (working)
- Copy 2: Git repo private GitHub (offsite + versioned)
- Copy 3: External SSD / Time Machine (local, offline)

Áp dụng:
- iCloud → daily auto
- Git → weekly manual / cron
- External SSD → monthly hoặc trigger trước thay đổi lớn

---

## Bước 1 — Git backup setup

### Tạo private repo GitHub

1. Mở https://github.com/new
2. Repo name: `my-vaults-backup` (hoặc tên riêng)
3. **Private** (BẮT BUỘC — vault chứa info cá nhân)
4. Init without README

### Init Git trong vault

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
git init
git remote add origin git@github.com:<you>/my-vaults-backup.git
```

### .gitignore

Tạo `.gitignore` ở root vault:

```bash
cat > .gitignore <<EOF
# Obsidian workspace local
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/graph.json

# macOS
.DS_Store

# Claude local settings
.claude/settings.local.json

# Python
__pycache__/
*.pyc
.venv/
bin/.venv/

# Raw bí mật / tạm thời
raw/_pending/
raw/_personal/

# Lock file
.git-lock
EOF
```

### Initial commit

```bash
git add .
git commit -m "Initial vault backup"
git branch -M main
git push -u origin main
```

---

## Bước 2 — Commit cadence

### Daily auto-commit (recommended)

Tạo script `bin/backup.sh`:

```bash
#!/bin/bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
git add .
DATE=$(date +%Y-%m-%d)
git commit -m "Daily backup $DATE" || echo "Nothing to commit"
git push origin main
```

Cron daily 23:00:

```bash
crontab -e
```

Thêm:
```
0 23 * * * /Users/<you>/path/to/bin/backup.sh >> /tmp/vault-backup.log 2>&1
```

Hoặc launchd plist (xem [[03-mo-rong-multi-vault/03-vault-4dx-execution]] pattern).

### Manual commit khi đổi lớn

Trước khi rename folder, refactor architecture, migrate vault:

```bash
git add .
git commit -m "Before major refactor: tách Life ra Brain"
git push
```

→ Rollback dễ.

---

## Bước 3 — Restore từ Git

Nếu vault corrupt hoặc bạn delete nhầm:

### Restore file đơn

```bash
git checkout HEAD -- "wiki/concepts/X.md"
```

### Restore folder

```bash
git checkout HEAD -- "wiki/concepts/"
```

### Restore vault về 1 commit cũ

```bash
git log --oneline    # tìm commit hash
git checkout <hash>  # detached HEAD mode

# Tạo branch mới từ point đó
git checkout -b restore-2026-05-15
```

### Restore vault hoàn toàn

```bash
cd ~
mv "Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain" "Brain-broken-2026-05-29"
git clone git@github.com:<you>/my-vaults-backup.git "Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
```

---

## Bước 4 — Backup external (Time Machine)

### macOS Time Machine

1. Cắm ổ external 1-2TB
2. System Settings → Time Machine → Add Backup Disk
3. Bật **Back Up Automatically**

Time Machine auto backup mỗi giờ. Restore qua app Time Machine.

Ưu: dễ setup, restore UI thân thiện.
Nhược: chỉ macOS, ổ external phải cắm thường xuyên.

### Rsync manual

Nếu không Time Machine, rsync sang external:

```bash
rsync -avu \
  "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/" \
  "/Volumes/External-SSD/obsidian-vaults/"
```

Chạy tuần (manual hoặc cron).

---

## Bước 5 — Backup multi-vault

Nếu có 4 vault sibling (Brain, Life, 4DX, Marketing) — backup all:

### Option A: 1 repo, mọi vault

Tạo repo `my-vaults-backup` root ở Documents/:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
git init
git remote add origin git@github.com:<you>/my-vaults-backup.git
```

Mỗi vault là 1 subfolder. Commit cả 4 cùng lúc.

Ưu: 1 repo dễ manage.
Nhược: Repo to (4 vault gộp), commit time chậm.

### Option B: 1 repo / vault

Mỗi vault có repo riêng:
- `brain-backup`
- `life-backup`
- `marketing-backup`
- `4dx-backup`

Ưu: repo nhỏ, độc lập.
Nhược: 4 lần `git push` mỗi backup cycle.

→ Khuyên Option A cho dưới 5 vault. Option B nếu > 5 vault hoặc vault nhạy cảm cần isolate.

---

## Bước 6 — Backup file binary

raw/ có nhiều file binary (ảnh, PDF) → repo Git phình to nhanh.

3 options:

### Option 1 — Commit binary vào Git LFS

```bash
git lfs install
git lfs track "*.heic" "*.HEIC" "*.jpg" "*.pdf"
git add .gitattributes
```

LFS lưu binary trên Cloud storage. Repo Git chỉ ref.

Ưu: full history binary.
Nhược: trả phí GitHub LFS ($5/tháng cho 50GB).

### Option 2 — Exclude binary, backup riêng

Trong `.gitignore`:

```
raw/photos/
raw/assets/*.pdf
raw/assets/*.HEIC
```

Backup binary qua rsync sang external SSD.

Ưu: repo Git gọn, miễn phí.
Nhược: binary không có history, chỉ snapshot latest.

### Option 3 — Hybrid

Markdown + small assets vào Git, binary lớn vào external + cloud storage (iCloud sync vẫn giữ).

→ Khuyên Option 3 cho người mới.

---

## Bước 7 — Backup secret

Memory + settings.local.json + credentials:

```
~/.claude/credentials.json
~/.claude/projects/*/memory/
.claude/settings.local.json
```

KHÔNG commit vào public/private repo (chứa API key, personal info).

Backup riêng:
- Copy thủ công sang encrypted disk image
- Sync qua iCloud Keychain (Mac native)
- Dropbox/iCloud private folder

---

## Bước 8 — Test restore

Backup quan trọng nhất là **restore work**. Test định kỳ:

### Test 1 — Restore file đơn

```bash
# Xoá thử 1 file
rm "wiki/concepts/Test-File.md"

# Restore
git checkout HEAD -- "wiki/concepts/Test-File.md"

# Verify
cat "wiki/concepts/Test-File.md"
```

### Test 2 — Restore folder

### Test 3 — Restore từ commit cũ

Mỗi quý test 1 lần. Nếu restore fail → backup vô dụng.

---

## Bước 9 — Backup workflow đề xuất

| Tần suất | Action |
|---|---|
| Realtime | iCloud sync (auto) |
| Daily 23:00 | Git commit + push (cron) |
| Weekly | Time Machine auto backup |
| Monthly | Verify Git push success + restore test 1 file |
| Quarterly | Full restore test (clone fresh) |
| Trước thay đổi lớn | Git commit + tag |

---

## Bước 10 — Disaster recovery

Khi worst case:

### Mac chết / mất

1. Mua Mac mới
2. Đăng nhập iCloud → vault sync về sau vài giờ
3. Nếu cần ngay: clone Git repo

### iCloud account bị khoá

1. Apple Support recover account
2. Trong lúc đợi: clone Git repo về Mac
3. Setup vault local, không sync iCloud tạm

### Repo Git bị xoá

1. Tạo repo mới
2. Push từ vault iCloud (local copy)
3. Audit có file nào fail không

### Tất cả 3 phương tiện chết cùng lúc

Cực hiếm. Nếu xảy ra:
- Time Machine có
- Email/Slack/Notion có draft cũ
- AI rebuild từ memory + context (sẽ thiếu nhiều)

→ 3-2-1 strategy giảm risk worst case → < 0.01%.

---

## Tiếp theo

Đọc tiếp: [[03-migrate-rename-vault]] — Migrate khi cần rename.
