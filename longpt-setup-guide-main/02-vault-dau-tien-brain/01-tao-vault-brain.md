---
title: Tạo vault Brain
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Tạo vault Brain

## Trước đó

[[01-cai-dat/05-cai-plugins-obsidian]] — bạn đã cài Obsidian, Claude Code, plugins.

---

## Mục tiêu phần 02

Trong 8 file của Phần 02, bạn sẽ:

1. Tạo folder vault Brain
2. Copy CLAUDE.md template
3. Tạo cấu trúc folder raw/ + wiki/
4. Hiểu 3 template page (concept, source, course MOC)
5. Ingest source đầu tiên cùng Claude
6. Query wiki đầu tiên cùng Claude

Sau Phần 02 → bạn có vault Brain chạy được.

---

## Bước 1 — Đặt tên vault

Đặt tên theo pattern: `<Tên bạn>'s Brain` hoặc `<Brand>'s Brain`.

Ví dụ:
- `Longpt's Brain` (anh Long)
- `Anna's Brain`
- `Acme Brain`
- `My Knowledge`

Quy tắc:
- Dùng chữ thường + chữ hoa OK
- Không dùng ký tự đặc biệt (`/`, `\`, `:`)
- Apostrophe `'` OK
- Tên ngắn (≤ 20 ký tự)

Giáo trình này dùng tên giả `My Brain`. Bạn thay bằng tên bạn.

---

## Bước 2 — Tạo folder vault trong iCloud Drive

Mở Finder → đi tới iCloud Drive:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/
```

Tạo folder mới: **My Brain** (hoặc tên bạn chọn).

Hoặc qua terminal:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My Brain"
```

---

## Bước 3 — Tạo cấu trúc folder cơ bản

Bên trong vault `My Brain/`, tạo:

```bash
cd "My Brain"
mkdir -p raw/assets wiki/sources wiki/concepts wiki/entities wiki/courses
```

Cấu trúc:

```
My Brain/
├── raw/
│   └── assets/        # ảnh tải về
├── wiki/
│   ├── sources/       # tóm tắt mỗi source ingest
│   ├── concepts/      # framework / phương pháp
│   ├── entities/      # người, tổ chức, brand
│   └── courses/       # MOC mỗi chương trình đào tạo
```

Sau này thêm subfolder khi cần:
- `wiki/stories/` — metaphor / ngụ ngôn
- `wiki/topics/` — tổng hợp xuyên source
- `wiki/students/` — case học viên (nếu là coach/trainer)
- `wiki/analyses/` — kết quả query lưu lại

---

## Bước 4 — Mở vault trong Obsidian

Mở Obsidian → **Open folder as vault** → chọn `My Brain` vừa tạo.

Obsidian tạo `.obsidian/` ẩn → workspace mở ra trống.

Trust author khi prompt.

---

## Bước 5 — Tạo file root

Tạo 4 file root cơ bản:

### `CLAUDE.md`

Sẽ làm ở [[02-claude-md-template]] (file tiếp theo).

### `index.md`

```markdown
# Index — My Brain

## Sources
- (chưa có)

## Concepts
- (chưa có)

## Entities
- (chưa có)

## Courses
- (chưa có)
```

Lưu.

### `log.md`

```markdown
# Log — My Brain

Nhật ký append-only.

## [2026-05-29] setup | Tạo vault
- Created: CLAUDE.md, index.md, log.md
- Created: folder raw/ + wiki/{sources,concepts,entities,courses}/
```

Lưu.

### `README.md` (tuỳ chọn)

```markdown
# My Brain

Vault knowledge cá nhân theo mô hình AI-first wiki concept-first.

- Schema: [[CLAUDE]]
- Mục lục: [[index]]
- Nhật ký: [[log]]
```

---

## Bước 6 — Verify vault trong terminal

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
ls
```

Expected:
```
CLAUDE.md       index.md        log.md          README.md       raw/            wiki/
```

(`.obsidian/` ẩn — không thấy với `ls`. `ls -la` để thấy.)

---

## Bước 7 — Mở vault với Claude Code

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Trong prompt, gõ:

```
> List file trong vault
```

Claude sẽ chạy `ls` và liệt kê. OK.

Test:
```
> Vault này có CLAUDE.md không? Đọc nó
```

Claude đọc CLAUDE.md (chưa có nội dung — sẽ làm ở file kế).

---

## Bước 8 — Quy ước Git (tuỳ chọn)

Nếu bạn muốn version control vault bằng Git:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
git init
```

Tạo `.gitignore`:

```bash
cat > .gitignore <<EOF
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/graph.json
.DS_Store
.claude/settings.local.json
EOF
```

Initial commit:

```bash
git add .
git commit -m "Initial vault setup"
```

Tạo private repo trên GitHub → push lên. Chi tiết ở [[05-bao-tri-lint/02-backup-icloud-git]].

Khuyên: **chưa cần Git ngay**. Chờ vault có nội dung rồi backup sau.

---

## Bước 9 — Một số lưu ý

### Không gộp 2 brand vào 1 vault

Bạn là coach **vừa** dạy bán hàng **vừa** dạy thiền? → 2 brand độc lập → 2 vault `Sales Brain` + `Meditation Brain`. Đừng nhét vào 1 vault.

### Không quá to ngay

Vault Brain bắt đầu chỉ với raw/ + wiki/. Đừng tạo 20 subfolder ngay từ đầu. Để vault grow tự nhiên — schema drift theo nhu cầu.

### Tên file vault

Anh Long dùng tên dễ đọc có dấu cách (`Longpt's Brain`). Obsidian xử lý tốt. Bạn cũng dùng được.

Tránh:
- Tên có `/`, `\`, `:`, `?`, `*` (filesystem invalid)
- Tên quá dài (> 50 char)

---

## Tiếp theo

Đọc tiếp: [[02-claude-md-template]] — Copy CLAUDE.md template vào vault.
