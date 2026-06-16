---
title: Migrate rename vault
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 05
---

# Migrate / rename vault

## Trước đó

[[02-backup-icloud-git]] — bạn đã có backup.

---

## Tình huống cần migrate

3 use case:

### A. Rename vault

`My Brain` → `Acme Brain`. Đổi tên vì đổi brand / personal name.

### B. Move vault sang location khác

iCloud → Dropbox. Hoặc Documents/ → ~/Vault/.

### C. Split vault

`Brain` quá to → tách Life ra → 2 vault sibling.

### D. Merge vault

2 vault redundant → gộp lại 1.

Mọi case → quy tắc chung: **backup trước, test sau, migrate cuối**.

---

## Quy tắc chung

### Rule 1 — Backup trước

Git commit + push:

```bash
cd "<old vault>"
git add .
git commit -m "Before migration"
git push
```

### Rule 2 — Đóng Obsidian + Claude Code

Tránh write conflict trong khi migrate:
- Quit Obsidian (Cmd+Q)
- Exit Claude Code (`/exit`)

### Rule 3 — Test với vault copy trước

Đừng migrate vault real. Copy ra test:

```bash
cp -R "My Brain" "My Brain-test"
# Migrate trên copy trước
```

Nếu OK → apply real.

### Rule 4 — Verify từng bước

Sau mỗi step:
- Mở Obsidian xem load OK
- Test wikilink random 5-10 cái
- Run lint kiểm broken link

---

## Use case A — Rename vault

`My Brain` → `Acme Brain`.

### Bước 1 — Đóng Obsidian + Claude Code

### Bước 2 — Rename folder

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mv "My Brain" "Acme Brain"
```

### Bước 3 — Update reference trong vault

Wikilink absolute từ vault khác trỏ về vault này:

```bash
# Trong Marketing vault, replace
grep -r "../My Brain/" Marketing/ | wc -l    # count broken
```

Bulk replace với Claude:

```
> Trong Marketing vault, replace "../My Brain/" thành "../Acme Brain/" trong mọi file .md.
```

Hoặc với sed:

```bash
cd "Marketing"
find . -name "*.md" -exec sed -i '' 's|\.\./My Brain/|../Acme Brain/|g' {} +
```

### Bước 4 — Update frontmatter brain_ref

```bash
find . -name "*.md" -exec sed -i '' 's|vault: "My Brain"|vault: "Acme Brain"|g' {} +
```

### Bước 5 — Update CLAUDE.md

Vault CLAUDE.md tự reference tên cũ → update.

```
> Replace "My Brain" với "Acme Brain" trong CLAUDE.md của vault Acme Brain
```

### Bước 6 — Reopen Obsidian

Mở Obsidian → File → Open Vault → chọn folder mới rename.

### Bước 7 — Test

- Cmd+O quick switcher → tìm vài page
- Cmd+G graph view → xem link
- `> Lint wiki` → check broken

---

## Use case B — Move vault

`iCloud/Documents/My Brain` → `~/Documents/Vaults/My Brain`.

Lý do:
- iCloud sync chậm với vault to
- Muốn dùng Dropbox thay
- Local-only, không cloud sync

### Bước 1 — Backup

### Bước 2 — Move folder

```bash
mkdir -p ~/Documents/Vaults
mv "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain" \
   "~/Documents/Vaults/"
```

### Bước 3 — Update vault settings Obsidian

Obsidian → Open Vault → chọn location mới.

### Bước 4 — Cập nhật script reference

Mọi script (cron, agent prompt) ref absolute path → update.

Vd `bin/backup.sh`:

```bash
# old
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"

# new
cd "/Users/$USER/Documents/Vaults/My Brain"
```

### Bước 5 — Update CLAUDE.md cross-vault reference

Nếu Brain CLAUDE.md ref Life/Marketing với path cũ → update.

---

## Use case C — Split vault

Tách Life ra khỏi Brain.

### Bước 1 — Identify page chuyển

Liệt page sẽ chuyển từ Brain → Life:

```
> List concept page có tag "lifestyle" hoặc "ca-koi" hoặc "the-thao". Đó là page cần move.
```

Claude output:

```
30 page move sang Life:
- wiki/concepts/ca-koi-pH.md
- wiki/entities/ho-koi.md
- wiki/sources/koi-care-handbook.md
- ...
```

### Bước 2 — Tạo vault Life

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My Life"
cd "My Life"
mkdir -p raw/{photos,articles,assets} wiki/{domains,entities,events,concepts}
touch CLAUDE.md README.md index.md log.md
```

Setup CLAUDE.md cho Life (xem [[03-mo-rong-multi-vault/02-vault-life-lifestyle]]).

### Bước 3 — Move file

```bash
mv "../My Brain/wiki/concepts/ca-koi-pH.md" "wiki/concepts/"
mv "../My Brain/wiki/entities/ho-koi.md" "wiki/entities/"
mv "../My Brain/wiki/sources/koi-care-handbook.md" "wiki/sources/"
```

Hoặc bulk với Claude:

```
> Move tất cả page có tag "lifestyle"/"ca-koi"/"the-thao" từ Brain sang Life vault.
> Preserve folder structure (concepts/ → concepts/, entities/ → entities/).
```

### Bước 4 — Update wikilink trong page move

Wikilink trong file move trỏ về page trong Brain → broken.

3 chiến lược:

#### Strategy 1 — Rewrite absolute path

```markdown
[[wiki/concepts/Atomic Habits]]  → [[../My Brain/wiki/concepts/Atomic Habits]]
```

#### Strategy 2 — Remove link

Nếu link đó không quan trọng cho Life context:

```markdown
[[wiki/concepts/Atomic Habits]]  → Atomic Habits (concept tham khảo, xem Brain)
```

#### Strategy 3 — Tạo concept stub trong Life

Tạo `Life/wiki/concepts/Atomic Habits-summary.md` 1 đoạn link về Brain:

```markdown
Concept "Atomic Habits" — xem chi tiết ở [[../My Brain/wiki/concepts/Atomic Habits]]
```

→ Khuyên Strategy 1 nếu cross-ref nhiều, Strategy 2 nếu rare.

### Bước 5 — Update Brain wikilink trỏ về page move

Trong Brain, page nào trỏ `[[ca-koi-pH]]` → broken (page đã move).

Bulk fix:

```
> Trong Brain vault, find wikilink trỏ page đã move sang Life.
> Replace với absolute path "[[../My Life/wiki/concepts/ca-koi-pH]]".
```

### Bước 6 — Update CLAUDE.md

Cả 2 vault CLAUDE.md update section "Vault song song":

Brain:
```markdown
## Vault song song

- `../My Life/` — vault anh em chứa lifestyle (cá koi, xe, du lịch). Brain = kiến thức work; Life = personal hobby.
```

Life:
```markdown
## Vault song song

- `../My Brain/` — vault anh em chứa knowledge work. Life đọc Brain concept khi cần.
```

### Bước 7 — Test

- Mở Brain, lint wiki → check broken link
- Mở Life, lint wiki → check broken link
- Mở cả 2 cùng lúc → test cross-vault wikilink

---

## Use case D — Merge vault

2 vault redundant → gộp.

### Bước 1 — Identify overlap

```
> Find page tồn tại cả Vault-A và Vault-B (cùng tên hoặc cùng concept).
```

### Bước 2 — Resolve duplicate

Mỗi cặp duplicate:
- Giữ version mới nhất / đầy đủ nhất
- Merge nội dung 2 page (nếu khác nhau)
- Update wikilink ref

### Bước 3 — Move page từ B sang A

```bash
mv "Vault-B/wiki/concepts/X.md" "Vault-A/wiki/concepts/"
```

### Bước 4 — Verify wikilink

Page move có link trỏ về Vault-B khác → update absolute path hoặc remove.

### Bước 5 — Delete Vault-B (sau verify)

```bash
mv "Vault-B" "Vault-B-archive-2026-05-29"
# Đợi 1 tháng confirm không thiếu gì, rồi delete
rm -rf "Vault-B-archive-2026-05-29"
```

---

## Common pitfall

### Pitfall 1 — Quên backup trước

Migration fail → mất data. ALWAYS Git commit trước.

### Pitfall 2 — Migrate khi Obsidian đang mở

File lock → write conflict. Đóng app trước.

### Pitfall 3 — Wikilink broken massive

Migrate 100 page → 500 wikilink broken. Bulk fix với Claude:

```
> Find all broken wikilink trong vault, đề xuất fix (rewrite path, remove, hoặc create stub).
```

### Pitfall 4 — Encoding lỗi (tiếng Việt có dấu)

`mv` Mac có thể fail với tên file có dấu. Dùng:

```bash
mv "$(echo 'tên có dấu' | iconv -f UTF-8-MAC -t UTF-8)" "tên mới"
```

Hoặc đổi tên không dấu trước, rồi mv.

### Pitfall 5 — iCloud sync chưa hoàn tất

Move file trên Mac → iCloud chưa sync → iPhone vẫn thấy file cũ.

Đợi iCloud sync xong (status icon Finder) trước khi mở Obsidian iPhone.

---

## Verify sau migrate

Checklist:

- [ ] Backup before migrate (Git commit)
- [ ] Folder mới có đầy đủ file expected
- [ ] CLAUDE.md updated
- [ ] index.md updated
- [ ] Wikilink test 10 random — OK
- [ ] Graph view render OK
- [ ] Lint clean (broken link < 5)
- [ ] iCloud sync hoàn tất
- [ ] Obsidian mở vault mới OK
- [ ] Claude Code chạy `claude` trong vault mới OK

---

## Khi migrate fail

Backup is friend. Restore:

```bash
git reset --hard HEAD
```

Hoặc clone fresh:

```bash
rm -rf "Broken vault"
git clone <repo> "Restored vault"
```

Investigate root cause trước khi retry.

---

## Tiếp theo

Đọc tiếp: [[04-khi-nao-pivot-architecture]] — Khi nào đập đi xây lại.
