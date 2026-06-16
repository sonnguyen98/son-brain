---
title: 3 lớp raw / wiki / CLAUDE.md
type: triet-ly
created: 2026-05-29
updated: 2026-05-29
phan: 00
---

# 3 lớp raw / wiki / CLAUDE.md

## Trước đó

[[03-tai-sao-multi-vault]] — bạn đã hiểu khi nào tách vault.

---

## Mô hình 3 lớp

Mỗi vault có cấu trúc 3 lớp rõ ràng:

```
Vault/
├── CLAUDE.md         # Lớp 3 — SCHEMA (luật chơi)
├── raw/              # Lớp 1 — INPUT bất biến
└── wiki/             # Lớp 2 — OUTPUT AI sở hữu
```

Mỗi lớp có **chủ sở hữu** và **quyền sửa** khác nhau.

---

## Lớp 1 — `raw/` (bạn sở hữu, AI chỉ đọc)

### Nội dung

Source thô không chỉnh sửa:
- Bài web clipped (Obsidian Web Clipper)
- PDF tải về
- Transcript SRT / TXT từ video
- Ảnh chụp iPhone
- Export CSV/XLSX từ dashboard
- File Word/PDF người khác gửi

### Quy tắc cứng

- **Chỉ ĐỌC, không sửa**. Khi raw vào folder, không bao giờ chỉnh nội dung.
- **Không xoá** trừ khi duplicate exact.
- **Tổ chức theo nguồn / ngày**: `raw/SSS/20251128-SSS-21-HaNoi/` hoặc `raw/photos/2026-05-29/`.

### Tại sao bất biến

Nếu raw bị sửa, AI sẽ confuse (đọc lần 1 thấy text A, lần 2 thấy text B → mâu thuẫn với wiki đã viết). Bất biến = source of truth ổn định.

Nếu cần edit (vd: sửa lỗi OCR PDF) → tạo file mới `raw/<file>-v2-corrected.md`, giữ bản gốc.

---

## Lớp 2 — `wiki/` (AI sở hữu, bạn duyệt)

### Nội dung

Page markdown do AI viết:
- Source summary (tóm tắt 1 source raw)
- Concept page (1 khái niệm)
- Course MOC (Map of Content cho 1 khoá)
- Story page (metaphor / ngụ ngôn)
- Topic synthesis (tổng hợp xuyên source)
- Entity page (PTL, học viên, mentor)

### Quy tắc cứng

- **AI viết, AI cross-link, AI lint**. Bạn chỉ duyệt.
- **Mọi page có frontmatter YAML**.
- **Mọi reference dùng wikilink** `[[Page Name]]`.
- **Mọi claim phải có source** (link về raw hoặc page khác đã link raw).

### Cấu trúc subfolder

Gợi ý ban đầu:

```
wiki/
├── sources/          # 1 page mỗi source đã ingest
├── concepts/         # framework / phương pháp / triết lý
├── stories/          # metaphor / ngụ ngôn / nhân vật ẩn dụ
├── topics/           # tổng hợp xuyên source
├── courses/          # MOC mỗi chương trình đào tạo
├── entities/         # người, công ty, tổ chức
├── students/         # case học viên
├── analyses/         # kết quả query lưu lại
└── index.md          # mục lục
```

Subfolder là gợi ý, không cứng. Thêm khi domain đòi hỏi.

---

## Lớp 3 — `CLAUDE.md` (cả 2 cùng tiến hoá)

### Nội dung

File markdown ở root vault, define:
- **Mục đích vault** (1-2 câu)
- **Cấu trúc thư mục** (raw/ + wiki/ + log.md + index.md)
- **Frontmatter chuẩn** (mọi page bắt buộc gì)
- **Workflow chính** (INGEST, QUERY, LINT)
- **Quy ước tên file**
- **Quy tắc nội dung** (tone, language, độ dài)
- **Edge case** (khi không chắc làm gì)

### Tại sao quan trọng nhất

CLAUDE.md là **hợp đồng giữa bạn và AI**. AI đọc CLAUDE.md đầu mỗi session, biết:
- Đây là vault gì
- Schema thế nào
- Bạn muốn AI cư xử thế nào

Không có CLAUDE.md → AI mỗi session làm khác đi → wiki không nhất quán.

### Quy tắc cứng

- **Đọc đầu mỗi session**, trước khi đọc bất kỳ file khác
- **OVERRIDE default behavior** của Claude (instruction trong CLAUDE.md thắng instruction default)
- **Append-only về philosophy**: schema chỉ drift theo feedback, không bao giờ đập đi viết lại

### Template

Template đầy đủ ở [[99-templates/claude-md-master-template]].

---

## Cộng thêm 2 file ở root

Ngoài CLAUDE.md, mỗi vault có:

### `index.md` — Catalog

Mục lục content-oriented, gom theo nhóm:

```markdown
# Index — <Tên vault>

## Sources
- [[Source A]] — tóm tắt 1 dòng
- [[Source B]] — ...

## Concepts
- [[Concept 1]]

## Courses
- [[Course X]]
```

Update khi tạo page mới.

### `log.md` — Chronological log

Append-only, mỗi entry 1 action:

```markdown
## [2026-05-29] ingest | Source mới
- Created: [[Source A]]
- Updated: [[Concept 1]], [[Entity B]]
- Notes: mâu thuẫn cũ ở...

## [2026-05-29] query | "X liên hệ Y thế nào?"
- Read: [[Page1]], [[Page2]]
- Output: bảng so sánh
```

Mới nhất ở dưới. Greppable: `grep "^## \[" log.md | tail -10`.

---

## Workflow hoạt động

```
┌──────────────────────────────────────────────────────────────┐
│ 1. Bạn thả source vào raw/                                    │
│    (PDF, bài clip, transcript, ảnh)                           │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 2. Bạn nói "ingest source X" với Claude                       │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 3. Claude:                                                    │
│    - Đọc CLAUDE.md (schema vault)                             │
│    - Đọc index.md (page nào có sẵn)                           │
│    - Đọc source raw                                           │
│    - Bàn key takeaway với bạn (3-5 bullet)                    │
│    - Viết wiki/sources/<Title>.md (source summary)            │
│    - Tạo/update wiki/concepts/<Concept>.md (concept page)     │
│    - Tạo/update wiki/entities/<Name>.md (entity page)         │
│    - Update index.md                                          │
│    - Append log.md                                            │
└────────────────────────┬─────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────┐
│ 4. Bạn duyệt: đúng → OK, sai → chỉ chỗ                        │
└──────────────────────────────────────────────────────────────┘
```

Sau lần ingest đầu, mọi query về source này → Claude đọc concept page trực tiếp, không scan raw.

---

## Quy tắc "AI viết, bạn duyệt" — chi tiết

### Khi AI viết đúng

- Pass, OK, continue
- Optionally: comment "thêm ý X" để AI bổ sung

### Khi AI viết sai

- Chỉ chỗ sai cụ thể (file + section + dòng)
- Cho biết đúng là gì
- AI sửa + update memory để không lặp lại

### Khi AI hỏi clarify

- Trả lời ngắn gọn
- Nếu ambiguous nhiều lần → cập nhật CLAUDE.md để rõ hơn

---

## Khi CLAUDE.md cần update

3 tình huống:

1. **Bạn thấy AI lặp lại 1 sai** → thêm rule vào CLAUDE.md
2. **Bạn thấy schema mới phát sinh** (loại page mới, tag mới) → bổ sung
3. **Workflow đổi** (vd: thêm cron) → mô tả workflow mới

Không tự AI sửa CLAUDE.md mà không hỏi bạn.

---

## Tiếp theo

Bạn đã hiểu triết lý. Sang Phần 01 cài đặt công cụ.

Đọc tiếp: [[01-cai-dat/01-cai-obsidian]] — Cài Obsidian.
