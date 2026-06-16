---
title: Khi nào tách vault
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 03
---

# Khi nào tách vault sibling

## Trước đó

[[02-vault-dau-tien-brain/08-query-wiki-dau-tien]] — vault Brain chạy được, có data ban đầu.

---

## Vấn đề khi vault 1 grows

Vault Brain bạn lớn dần. Sau 3-6 tháng:
- ~300-500 source page
- ~150-300 concept page
- 1000+ wikilink edges
- Mở Obsidian 20 giây
- Graph view rối
- Search trả về kết quả mix nhiều domain

3 lựa chọn:

| Lựa chọn | Khi nào |
|---|---|
| Tiếp tục 1 vault | Domain còn tập trung 1 chủ đề |
| Tách subfolder isolate | 1 sub-domain nhạy cảm hoặc volume cao nhưng vẫn liên quan |
| Tách vault sibling | Domain độc lập hoàn toàn |

---

## 4 tín hiệu cần tách vault

### Tín hiệu 1 — Domain khác hẳn

Vault Brain bạn bắt đầu chứa:
- Knowledge công việc (bán hàng, marketing)
- Cá nhân (sở thích, hobby, lifestyle)
- Sách đọc (book summary)

3 domain này không liên quan logic. Concept "Pareto" không cross "ho-koi". → Tách.

**Khuyên**: tách Life ra khỏi Brain đầu tiên. Đây là tách phổ biến nhất.

### Tín hiệu 2 — Tone + privacy khác

Eagle Club (coaching tier cao nhất của PTL) có info học viên nhạy cảm hơn khoá public.

Nếu để chung Brain:
- Lỡ share Brain ra ngoài → leak Eagle Club
- Search Brain → lẫn Eagle Club info với knowledge công khai

→ Tách subfolder isolate (`wiki/sources/coaching-weekly/`) hoặc tách vault hẳn (`Eagle Coaching/`).

### Tín hiệu 3 — Workflow + cron khác

4DX cần cron đêm CN scan data → generate report. Brain không có cron.

Nếu để chung Brain:
- CLAUDE.md Brain phải mô tả thêm cron workflow → bloat
- Script `scan_4dx.py` lẫn lộn với raw/

→ Tách `4DX/` riêng. Có scripts/ + plist riêng.

### Tín hiệu 4 — Instance lặp lại (cohort)

Mỗi cohort khoá học của bạn có:
- 50-100 học viên
- Assignments theo ngày
- Hồ sơ cá nhân từng người

3 cohort × 100 học viên = 300 student page. Bloat Brain.

→ Tách `<Course> <Cohort>/` riêng cho mỗi instance.

Vd:
- `LTVM 16/` — cohort 16 khoá LTVM
- `Bhtc 07/` — cohort 7 khoá BHTC
- `IPS Coaching 15/` — cohort 15 khoá IPS Coach

---

## Heuristic an toàn

Trước khi tách, áp 3 câu hỏi:

### 1. Vault hiện tại đã > 500 page chưa?

- < 200 page → KHÔNG tách. Quá sớm.
- 200-500 page → có thể tách nếu rõ archetype
- > 500 page → tách 1-2 vault chính

### 2. 2 domain định tách có cross-reference > 5% page không?

Nếu Marketing tham chiếu Brain ở > 50% page → KHÔNG tách. Để chung tiện link.

Nếu Marketing tham chiếu Brain ở < 5% page → tách OK. Cross-vault wikilink absolute là exception, không phải norm.

### 3. Có ít nhất 1 archetype clear chưa?

Archetype rõ:
- Knowledge / Lifestyle / Execution / Production / Instance
- Mỗi cái có CLAUDE.md schema riêng

Nếu chưa rõ archetype → đợi thêm. Tách sớm = phải migrate sau.

---

## Khi nào KHÔNG tách

### Vault còn nhỏ (< 200 file)

Nhỏ → tổ chức bằng subfolder + tag là đủ. Tách vault tốn overhead (N CLAUDE.md, N index.md).

### 2 domain liên quan logic

Vd: "Bán hàng B2B" và "Bán hàng B2C" — vẫn cùng domain "bán hàng". Subfolder thôi.

### Domain mới chỉ là theme cụ thể

Vd: "Marketing cho IPS" là sub của "Marketing tổng" — không tách.

### Bạn chưa biết schema khác nhau

Tách sớm = phải migrate khi schema rõ. Đợi đến khi rõ.

---

## Cách tách an toàn

Nếu quyết tách → quy trình 4 bước:

### Bước 1 — Identify page chuyển

Liệt page nào sẽ chuyển từ Brain → vault mới. Vd tách Life:

```
Brain/wiki/concepts/ca-koi-pH-management.md   → Life/wiki/concepts/
Brain/wiki/entities/ho-koi.md                  → Life/wiki/entities/
Brain/wiki/sources/koi-care-handbook.md        → Life/wiki/sources/
```

### Bước 2 — Tạo vault mới

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My Life"
cd "My Life"
mkdir -p raw/assets wiki/concepts wiki/entities wiki/sources
touch CLAUDE.md README.md index.md log.md
```

Copy CLAUDE.md template cho domain mới (lifestyle, photo pipeline...).

### Bước 3 — Move page

```bash
# Move file
mv "../My Brain/wiki/concepts/ca-koi-pH-management.md" "wiki/concepts/"
mv "../My Brain/wiki/entities/ho-koi.md" "wiki/entities/"
mv "../My Brain/wiki/sources/koi-care-handbook.md" "wiki/sources/"

# Update wikilink trong các file move
# (cần thủ công hoặc dùng script)
```

Wikilink trong file move trỏ về page trong Brain → broken. Phải:
- Option A: rewrite link thành absolute path `[[../My Brain/wiki/concepts/X]]`
- Option B: remove link (nếu page không cross-reference)
- Option C: tạo concept page tóm tắt ngắn trong Life trỏ về Brain

### Bước 4 — Lint Brain + Life

Mở Claude trong Brain:

```
> Lint wiki: tìm wikilink broken sau khi move file sang Life vault.
```

Claude scan, báo:

```
3 broken link:
- [[ca-koi-pH-management]] trong wiki/topics/family-hobbies.md
- ...
```

Bạn quyết: rewrite absolute path hoặc remove.

---

## Quy ước tên vault sibling

Pattern phổ biến:

| Pattern | Ví dụ |
|---|---|
| `<Name>'s <Archetype>` | `Longpt's Brain`, `Anna's Life`, `Acme's Marketing` |
| `<Brand> <Domain>` | `Longguru Youtube`, `Acme Coaching` |
| `<Course> <Cohort>` | `LTVM 16`, `Bhtc 07`, `IPS Coaching 15` |
| `<Project Name>` | `Ngôn ngữ tình yêu`, `Nhân sự` |

Tên không quá dài. Có space OK.

---

## 5 archetype phổ biến

Vault sibling thường rơi vào 5 archetype:

### A. Knowledge (Brain, Books, Knowledge)

- Wiki concept-first
- Raw → wiki
- Pure intake + tổng hợp

### B. Lifestyle (Life)

- Entity + event tracking cá nhân
- Photo pipeline
- 6-10 domain hardcoded
- Tone đời thường

### C. Execution (4DX)

- Meta layer trên 2+ vault
- Cron pull data
- Traffic light system
- 4 channel output (md + email + PDF + xlsx)

### D. Production (Marketing, Longguru Youtube)

- Asset + metric tracking
- Variant + A/B test
- Cross-vault reference (đọc Brain)
- Pancake/analytics integration

### E. Instance (cohort khoá)

- 1 cohort 1 vault
- 50-100 student page
- Assignments tracking
- Tone intimate + responsible

---

## Anh Long có 14 vault — pattern

| Vault | Archetype | Lý do tách |
|---|---|---|
| Brain | Knowledge | Master |
| Life | Lifestyle | Personal hobby tách work |
| 4DX | Execution | Cron meta layer |
| Marketing | Production | Tách production khỏi knowledge |
| Longguru Youtube | Production | Tách YT khỏi marketing chung |
| BNI | Domain-specific | BNI có schema riêng |
| Knowledge | Knowledge | Đọc sách technical |
| Books | Knowledge | Sách reference |
| Setup-Guide | Knowledge | Vault này — giáo trình |
| Nhân sự | Domain-specific | HR confidential |
| Bhtc 07 | Instance | Cohort BHTC 07 |
| LTVM 16 | Instance | Cohort LTVM 16 |
| IPS Coaching 15 | Instance | Cohort IPS Coach 15 |
| Eagle Club | Instance | Eagle Club coaching |
| Ngôn ngữ tình yêu | Project | Dự án quiz riêng |

Lưu ý: anh Long mất 1+ năm để evolve đến 14 vault. KHÔNG tách 14 vault ngay từ đầu. Build dần.

---

## Roadmap đề xuất cho người mới

**Tháng 1-3**: Chỉ vault Brain. Build dần, lint kỹ.

**Tháng 4-6**: Tách Life ra khỏi Brain (nếu có nhu cầu lifestyle). 2 vault.

**Tháng 7-9**: Tách Marketing (nếu chạy business). 3 vault.

**Tháng 10-12**: Thêm 4DX (nếu cần OKR/execution). 4 vault.

**Năm 2+**: Mỗi cohort khoá học mới → 1 vault Instance. Tiến tới 8-10 vault.

**Năm 3+**: Tinh chỉnh, refactor schema, có thể merge nếu thấy tách quá xa.

---

## Tiếp theo

Đọc tiếp: [[02-vault-life-lifestyle]] — Build vault Life cho lifestyle cá nhân.
