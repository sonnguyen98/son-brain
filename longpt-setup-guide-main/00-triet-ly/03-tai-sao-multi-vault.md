---
title: Tại sao multi-vault
type: triet-ly
created: 2026-05-29
updated: 2026-05-29
phan: 00
---

# Tại sao multi-vault

## Trước đó

[[02-tai-sao-concept-first]] — bạn đã hiểu concept là đơn vị lưu trữ.

---

## Vấn đề 1 vault to

Cách thường thấy: bạn có 1 vault Obsidian duy nhất chứa **tất cả** — công việc, cá nhân, sở thích, đọc sách, dự án.

Sau 6-12 tháng:
- Vault có 3000+ file
- Mở Obsidian load 30 giây
- Graph view rối như mạng nhện
- Search trả về kết quả lẫn lộn (tìm "training" → ra Ironman + Sales training + corporate training)
- Tag system vỡ (50+ tag không ai dùng)
- Sync iCloud chậm vì vault to

---

## Pivot multi-vault

Anh Long chạy **14 vault sibling** thay vì 1 vault to:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/
├── Longpt's Brain/           # kiến thức PTL dạy
├── Longpt's Life/            # đời sống cá nhân (cá koi, xe, du lịch)
├── Longpt's 4DX/             # OKR + execution
├── Longpt's Marketing/       # production + đo lường
├── Longguru Youtube/         # production layer kênh YT
├── Longpt' BNI/              # tracking BNI
├── Longpt's Setup-Guide/     # vault này
├── Knowledge/                # đọc sách
├── Nhân sự/                  # HR
├── Bhtc 07/                  # instance khoá BHTC 07
├── LTVM 16/                  # instance khoá LTVM 16
├── IPS Coaching 15/          # instance khoá IPS Coach 15
├── Eagle Club/               # instance Eagle Club
├── Books/                    # sách reference
└── Ngôn ngữ tình yêu/        # dự án quiz
```

Mỗi vault có **mục đích duy nhất, schema riêng, AI workflow riêng**.

---

## Khi nào tách vault — 4 tín hiệu

### Tín hiệu 1 — Domain khác hẳn nhau

Cá koi không liên quan đến SSS. Bài tập Ironman không liên quan đến Hệ thống bán hàng 8+2. Khi 2 chủ đề độc lập về **nội dung**, **người đọc**, **schema** — tách vault.

→ Long tách `Brain` (kiến thức công việc) khỏi `Life` (cá nhân).

### Tín hiệu 2 — Tone + privacy khác

Eagle Club là tier cao nhất → info học viên nhạy cảm hơn. Nếu để chung Brain, lỡ share Brain ra ngoài là leak Eagle Club.

→ Long isolate `wiki/sources/coaching-weekly/` trong Brain (subfolder isolate, chưa tách vault). Tới ngày Eagle Club info nhạy cảm vượt ngưỡng → tách hẳn `Longpt's Coaching/`.

### Tín hiệu 3 — Workflow + cron khác

4DX cần **cron đêm CN** đọc data Life + Marketing → generate report sáng T2. Brain không có cron.

→ Long tách `4DX` thành vault meta-execution riêng, có `scripts/scan_4dx.py` + `launchd plist`.

### Tín hiệu 4 — Instance lặp lại (cohort)

Mỗi cohort khoá có 50-100 học viên, mỗi học viên có assignments, hồ sơ. Chứa chung Brain → bloat.

→ Long tách `LTVM 16`, `Bhtc 07`, `IPS Coaching 15` riêng — mỗi vault chứa 1 cohort.

---

## Pattern liên kết multi-vault

### Cross-vault reference

Khi vault Marketing cần kiến thức concept từ Brain, dùng wikilink absolute path:

```markdown
Lead page IPS dựa trên [[../Longpt's Brain/wiki/courses/IPS - Internet Power System]]
```

Hoặc frontmatter `brain_ref` nhẹ hơn cho query:

```yaml
---
brain_ref:
  program_code: ips
  course_page: "[[../Longpt's Brain/wiki/courses/IPS - Internet Power System]]"
---
```

### Một chiều, không hai chiều

Marketing **chỉ đọc** Brain, KHÔNG ghi ngược. Tránh vòng tròn dependency.

Nếu Marketing phát hiện concept mới chưa có trong Brain → log lại, chờ user xử lý bên Brain sau.

### Cross-vault query

Khi user hỏi câu vắt 2 vault (vd: *"Lead page IPS Q2 thu được bao nhiêu, dùng concept gì từ khoá IPS?"*), Claude:
1. Đọc Marketing/wiki/reports/2026-Q2-ips-funnel.md → lấy số
2. Đọc Brain/wiki/courses/IPS - Internet Power System.md → lấy concept
3. Tổng hợp

Chi tiết quy trình ở [[03-mo-rong-multi-vault/05-cross-vault-query]].

---

## Phân loại vault theo archetype

Vault sibling rơi vào 5 archetype:

| Archetype | Vai trò | Ví dụ |
|---|---|---|
| **Knowledge** | Wiki concept-first, raw → wiki | Brain, Knowledge, Books |
| **Lifestyle** | Tracking cá nhân, photo + entity | Life |
| **Execution** | OKR + cron meta layer | 4DX |
| **Production** | Asset + metric tracking | Marketing, Longguru Youtube |
| **Instance** | 1 cohort / instance domain hẹp | LTVM 16, Bhtc 07, IPS Coaching 15, Nhân sự |

Mỗi archetype có schema khác → CLAUDE.md khác.

---

## Lúc nào KHÔNG tách

Đừng tách nếu:

- Vault < 200 file (chưa đủ lớn)
- Domain mới chỉ là **theme** trong domain cũ (vd: "marketing IPS" là sub của "marketing tổng" — không tách)
- Bạn chưa biết schema khác nhau thế nào (tách sớm = phải migrate khi schema rõ)

**Heuristic an toàn**: build 1 vault to trước. Khi nó vượt 500 file + bắt đầu mệt → tách 1 lần đầu tiên (thường tách Life ra khỏi Brain).

---

## Multi-vault có cost gì

Tradeoff thật:

| Có thêm | Mất đi |
|---|---|
| Vault gọn, schema sạch | Phải maintain N CLAUDE.md |
| Graph view không rối | Cross-vault wikilink khó hơn |
| Sync iCloud nhanh hơn | Mở N vault song song nặng RAM |
| Privacy isolate được | Search xuyên vault phải dùng Mac Spotlight thay vì Obsidian search |

Anh Long chấp nhận tradeoff vì lợi > hại sau khi vault >500 file. Bạn quyết tuỳ scale.

---

## Tiếp theo

Đọc tiếp: [[04-3-lop-raw-wiki-schema]] — Mô hình 3 lớp raw / wiki / CLAUDE.md trong mỗi vault.
