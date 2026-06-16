---
title: Vault Life — lifestyle cá nhân
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 03
---

# Vault Life — lifestyle cá nhân

## Trước đó

[[01-khi-nao-tach-vault]] — bạn đã hiểu khi nào tách.

---

## Mục tiêu vault Life

Vault Life lưu **đời sống cá nhân** — sở thích, hobby, gia đình, sức khoẻ, du lịch. KHÔNG ghi công việc.

Tại sao tách:
- Tone khác (đời thường vs công việc)
- Domain khác (cá koi, xe, ảnh chụp vs marketing)
- Privacy khác (lifestyle private hơn)
- Schema khác (event timeline + photo pipeline thay vì concept-first)

---

## Khác biệt Life vs Brain

| Brain | Life |
|---|---|
| Concept-first | Entity + event timeline |
| Raw → wiki summary | Photo pipeline đặc thù |
| Course MOC | Domain page (6-10 hardcoded) |
| 5 loại page chính | 5 loại page + 2 collection (koi/, vehicle/) |
| Tone professional | Tone đời thường |
| Tiếng theo source | Tiếng Việt 100% |

---

## Bước 1 — Tạo vault Life

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My Life"
cd "My Life"
mkdir -p raw/photos raw/articles wiki/{domains,entities,events,concepts,analysis,journal}
```

Mở Obsidian → Open folder as vault → chọn `My Life`.

---

## Bước 2 — Identify domain

Liệt 5-8 mảng đời sống chính của bạn. Vd anh Long:

| Slug | Mảng |
|---|---|
| `xe-may` | Xe máy hàng ngày |
| `o-to-caravan` | Ô tô + du lịch caravan |
| `dien-mat-troi-ha-chau` | Hệ PV + smart home |
| `the-thao-triathlon` | Chạy bộ, đạp xe, bơi |
| `du-lich` | Chuyến đi, địa điểm |
| `ca-koi` | Hồ koi, sức khoẻ cá |

Domain của bạn:
- `the-thao-tennis`
- `lam-vuon`
- `nau-an`
- `du-lich-chau-au`
- `nhiep-anh`
- `gia-dinh`

→ List 5-8 domain. Tên slug = tiếng Việt không dấu kebab-case.

---

## Bước 3 — Tạo Domain page

Mỗi domain 1 file ở `wiki/domains/`:

```bash
cd "wiki/domains"
touch xe-may.md o-to-caravan.md dien-mat-troi-ha-chau.md the-thao-triathlon.md du-lich.md ca-koi.md
```

Mỗi domain page có template:

```markdown
---
title: Xe máy
type: domain
slug: xe-may
updated: 2026-05-29
---

# Xe máy

## Tổng quan

[1-2 đoạn — mảng này gồm gì, vai trò trong đời sống]

## Entities trong mảng

- [[<entity-1>]] — vai trò
- [[<entity-2>]]

## Concepts cần nắm

- [[<concept-1>]]
- [[<concept-2>]]

## Events nổi bật

- [[YYYY-MM-DD-event-1]]
- [[YYYY-MM-DD-event-2]]

## Analysis định kỳ

- [[<analysis-1>]]
```

---

## Bước 4 — CLAUDE.md cho Life

Copy template (khác Brain) — nhấn entity + event + domain thay vì concept-first:

```markdown
# CLAUDE.md — Luật chơi vault "My Life"

## 1. Chủ vault

[Tên bạn] — [năm sinh]. [Ngắn 2 dòng background đời thường].

### Cách xưng hô

- Tự xưng "bạn" / "tôi" trong wiki
- Tiếng Việt 100% nội dung, tên file không dấu kebab-case

## 2. Sáu mảng đời sống

| Slug | Mảng |
|---|---|
| `xe-may` | Xe máy hàng ngày |
| ... |

Quy tắc cứng: mọi entity/event/concept phải neo về ít nhất 1 domain. Domain ghi `domain: [<slug>]` trong frontmatter.

## 3. Năm loại trang

```
wiki/
├── domains/        # 6 trang tổng quan
├── entities/       # Thực thể danh tính riêng
├── events/         # Sự kiện theo timeline: YYYY-MM-DD-mo-ta-ngan.md
├── concepts/       # Khái niệm cần nắm (FTP, MPPT, pH...)
├── analysis/       # Phân tích / so sánh / báo cáo
├── journal/        # Tổng hợp tuần / tháng
```

### Quy ước Event page

Format file: `wiki/events/YYYY-MM-DD-<mo-ta-ngan>.md`

5-10 dòng. Frontmatter:

\`\`\`yaml
---
title: Tiêu đề
type: event
date: YYYY-MM-DD
domain: [<slug>]
entities: [[[entity-1]], [[entity-2]]]
source: raw/photos/YYYY-MM-DD/IMG_xxxx.HEIC
---
\`\`\`

## 4. Xử lý ảnh từ iPhone

Khi thả ảnh vào `raw/photos/YYYY-MM-DD/`:

1. Mở từng ảnh, mô tả nội dung
2. Suy ra event tương ứng
3. Tạo `wiki/events/YYYY-MM-DD-<slug>.md`
4. Update entity liên quan
5. Link ảnh gốc trong frontmatter `source:`
6. Append `log.md`

## 5. Xử lý mâu thuẫn

Khi dữ liệu mới mâu thuẫn cũ — KHÔNG xoá. Dùng callout:

```markdown
> [!contradiction] Mâu thuẫn — 2026-05-29
> Log cũ: pH hồ = 7.2
> Mới: pH = 6.8
> Cần xác minh
```

## 6. Quy tắc nội dung

- Giọng văn: ngắn gọn, đi thẳng vấn đề
- Entity ≤ 1 màn hình
- Event 5-10 dòng
- Dữ kiện > suy đoán

## 7. Quy ước log

`## [YYYY-MM-DD] <action> | <object>`

Action: `ingest`, `update`, `query`, `lint`, `setup`.
```

Tuỳ chỉnh template theo domain của bạn.

---

## Bước 5 — Photo pipeline (tuỳ chọn)

Nếu bạn chụp nhiều ảnh iPhone → setup pipeline auto extract event:

### Cài Python + uv

```bash
brew install python@3.11
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup bin/ folder

```bash
mkdir bin
cd bin
uv venv .venv
source .venv/bin/activate
uv pip install pillow piexif
```

### Script đọc EXIF

Tạo `bin/extract_exif.py`:

```python
#!/usr/bin/env python3
"""Extract date + GPS từ ảnh iPhone JPEG."""
import sys
import json
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif(path):
    img = Image.open(path)
    exif = img._getexif() or {}
    result = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == 'DateTime':
            result['date'] = value
        elif tag == 'GPSInfo':
            gps = {}
            for gps_id, gps_val in value.items():
                gps[GPSTAGS.get(gps_id, gps_id)] = gps_val
            result['gps'] = gps
    return result

if __name__ == '__main__':
    print(json.dumps(get_exif(sys.argv[1]), default=str, indent=2))
```

Test:

```bash
python bin/extract_exif.py raw/photos/2026-05-29/IMG_1234.HEIC
```

Output: date, GPS lat/lon.

Chi tiết hơn — pipeline tự cắt cá koi từ ảnh hồ — xem Life vault anh Long: `bin/koi_extract.py` dùng SAM + rembg + EXIF.

---

## Bước 6 — Slash commands

Tạo `.claude/commands/` để gom workflow phổ biến:

### `.claude/commands/ingest-photos.md`

```markdown
---
description: Ingest ảnh từ raw/photos/<date>/, tạo events + update entities
---

Quy trình:

1. Đọc tất cả ảnh trong `raw/photos/$ARGUMENTS/`
2. Mô tả nội dung từng ảnh (xe gì, ở đâu, làm gì, có ai)
3. Group ảnh theo event (1 ngày có thể nhiều event)
4. Tạo `wiki/events/$ARGUMENTS-<slug>.md` cho mỗi event
5. Update entity page liên quan (block "Lịch sử")
6. Link ảnh gốc trong frontmatter `source:`
7. Append log.md
```

Gọi: `/ingest-photos 2026-05-29`

### `.claude/commands/journal-week.md`

```markdown
---
description: Tổng hợp tuần thành wiki/journal/<YYYY-Www>.md
---

Quy trình:

1. Đọc tất cả `wiki/events/<YYYY-MM-DD>*.md` trong tuần $ARGUMENTS
2. Group theo domain
3. Viết `wiki/journal/$ARGUMENTS.md` với section mỗi domain
4. Highlight 3 event nổi bật nhất
5. Liệt entity mới phát sinh
6. Append log.md
```

Gọi: `/journal-week 2026-W22`

### `.claude/commands/lint.md`

```markdown
---
description: Lint Life vault
---

Scan tìm:

1. Wikilink chết (point tới page không tồn tại)
2. Entity thiếu frontmatter
3. Event thiếu domain tag
4. Callout `[!contradiction]` chưa giải quyết
5. Orphan page (không có inbound link)
6. Concept nhắc nhiều nhưng chưa có page

Output: report dạng checklist.
```

Gọi: `/lint`

---

## Bước 7 — Test ingest photo đầu

Thả 5-10 ảnh vào `raw/photos/2026-05-29/`:

```bash
cp ~/Pictures/iPhone-recent/*.HEIC "raw/photos/2026-05-29/"
```

Trong Claude Code:

```
> /ingest-photos 2026-05-29
```

Claude:
1. Mở từng ảnh
2. Mô tả nội dung (Claude xem ảnh được)
3. Group event (vd: sáng cafe, trưa câu cá, chiều đi xe)
4. Tạo `wiki/events/2026-05-29-cafe-sang.md`, `2026-05-29-cau-ca.md`, `2026-05-29-xe-chieu.md`
5. Update entity page (vd: `[[ca-phe-X]]`, `[[ho-cau-Y]]`)
6. Link ảnh gốc

---

## Bước 8 — Khác biệt với Brain

Quy tắc khi viết Life vs Brain:

| Quy tắc | Brain | Life |
|---|---|---|
| Concept-first | ✅ | ❌ (event-first) |
| Frontmatter `type: concept` | Concept page chính | Domain page có |
| Wikilink mandatory | ✅ | ✅ |
| Source page cite line ref | ✅ | ⚪ (ảnh = source) |
| Course MOC | ✅ | ❌ |
| Story page | ✅ | ❌ |
| Photo pipeline | ❌ | ✅ |
| Journal tuần/tháng | ⚪ | ✅ |

---

## Tiếp theo

Đọc tiếp: [[03-vault-4dx-execution]] — Build vault 4DX với cron pull.
