---
title: CLAUDE.md template
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# CLAUDE.md template

## Trước đó

[[01-tao-vault-brain]] — vault Brain folder đã tạo.

---

## CLAUDE.md là gì

CLAUDE.md ở root vault = **luật chơi**. Claude đọc đầu mỗi session, biết:
- Vault này là gì
- Schema thế nào
- Bạn muốn AI làm gì

Không có CLAUDE.md → Claude làm mỗi session khác đi → wiki không nhất quán.

---

## Bước 1 — Copy template

Copy nội dung dưới vào `CLAUDE.md` ở root vault `My Brain/`:

```markdown
# CLAUDE.md — Schema Wiki "My Brain"

Vault này là wiki LLM tự duy trì. Kiến thức được biên tập 1 lần khi source vào và giữ cho cập nhật — không tái dựng lại mỗi lần truy vấn.

**Đọc file này đầu mỗi session, trước khi đọc/ghi bất cứ file nào khác.**

## 3 lớp

1. **Raw sources** (`raw/`) — tài liệu input bất biến (bài clip, PDF, ghi chú, transcript, ảnh). Chỉ đọc, không sửa.
2. **Wiki** (`wiki/`) — page markdown do LLM viết: tóm tắt source, page entity, page concept, tổng hợp, so sánh, phân tích. LLM sở hữu lớp này hoàn toàn.
3. **Schema** (file này) — quy ước và quy trình. Tiến hoá cùng người dùng theo thời gian.

Cộng thêm 2 file điều hướng ở root:
- `index.md` — danh mục nội dung (page nào tồn tại, gom theo nhóm)
- `log.md` — sổ ghi chép thời gian, append-only

## Nguyên tắc concept-first

Wiki này concept-centric — không source-centric. Concept là đơn vị lưu trữ kiến thức cuối cùng; mọi thứ khác (source / course / entity) là context để concept có nghĩa.

**Mục tiêu**: khi truy vấn, AI trả lời bằng cách tổng hợp từ các concept page (đã vet, có line ref, cross-link) — KHÔNG đọc lại raw mỗi lần.

### Quy tắc tách nhỏ (Atomicity)

Mỗi khái niệm độc lập = 1 page riêng. KHÔNG gộp 2 khái niệm vào 1 page chỉ vì chúng được dạy cặp đôi.

**Heuristic**:
1. Có cấu trúc riêng → tách
2. Có line ref riêng trong source → tách
3. Có thể link độc lập trong concept khác → tách
4. Là enumeration của 1 framework chung → gộp + page con mỗi mục nếu signature

## Cấu trúc thư mục

```
/
├── CLAUDE.md
├── index.md
├── log.md
├── raw/
│   ├── assets/
│   └── ...
├── wiki/
│   ├── sources/
│   ├── entities/
│   ├── courses/
│   ├── concepts/
│   ├── stories/
│   ├── topics/
│   └── analyses/
```

Subfolder trong `wiki/` là gợi ý. Thêm khi domain đòi hỏi.

## Quy ước file

- **Tên file**: tiêu đề có dấu cách dễ đọc OK (Obsidian xử lý được).
- **Wikilink**: link mạnh tay với `[[Page Name]]`.
- **Frontmatter**: mọi page mở đầu bằng YAML:
  ```yaml
  ---
  type: source | entity | concept | topic | analysis
  tags: [tag1, tag2]
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  sources: ["[[Source A]]"]
  ---
  ```
- **Source page** thêm: `raw_path: raw/...`, `author`, `date`, `url`.
- **Trích dẫn**: trong văn bản, cite source bằng `[[Source Title]]` inline.
- **Ngôn ngữ**: viết mỗi page theo ngôn ngữ của source.

## Workflow: Ingest

Khi user nói "ingest X" hoặc thả file vào `raw/`:

1. Đọc source đầy đủ.
2. Bàn key takeaway với user (3-5 bullet). Hỏi muốn nhấn cái gì trước khi viết.
3. Viết source summary ở `wiki/sources/<Source Title>.md`.
4. Update / tạo entity page cho mỗi entity được tên.
5. Update / tạo concept page tương tự.
6. Ghi mâu thuẫn rõ ràng nếu source mới khác claim cũ.
7. Update `index.md`.
8. Append `log.md` với format `## [YYYY-MM-DD] ingest | <Title>`.

## Workflow: Query

Khi user hỏi:

1. Đọc `index.md` trước để tìm page candidate.
2. Drill vào page liên quan. Theo wikilink để gom context.
3. Tổng hợp câu trả lời có cite.
4. Chọn format đúng: prose, bảng, bullet.
5. Đề nghị lưu lại dưới `wiki/analyses/` nếu là tổng hợp đáng giữ.

## Workflow: Lint

Khi user nói "lint wiki":

- Mâu thuẫn giữa các page về cùng entity/concept
- Claim cũ đã bị source mới vượt qua
- Page mồ côi (không có inbound link)
- Page thiếu (concept nhắc 3+ source mà chưa có page riêng)
- Cross-ref thiếu

Báo dưới dạng checklist. Đừng tự sửa âm thầm — để user ưu tiên.

## Format `log.md`

Append-only. Mỗi entry:

```markdown
## [2026-04-26] ingest | Article Title
- Created: [[Source Title]]
- Updated: [[Entity A]], [[Concept B]]
- Notes: trái với claim cũ ở [[Entity A]]

## [2026-04-26] query | "X liên hệ Y thế nào?"
- Read: [[Page1]], [[Page2]]
- Output: bảng so sánh

## [2026-04-26] lint
- 3 page mồ côi
- 1 mâu thuẫn
```

Mới nhất ở dưới. Greppable: `grep "^## \[" log.md | tail -10`.

## Tự tiến hoá file này

Khi Claude phát hiện cải tiến workflow, sở thích lặp lại — đề xuất sửa file này và xin xác nhận. Schema drift về phía cái work cho vault.
```

---

## Bước 2 — Customize template

Thay phần sau theo bạn:

### Tên vault

Tìm-thay `My Brain` → `Anna Brain` / `Acme Brain` / tên bạn.

### Domain riêng

Nếu vault có domain cụ thể (vd: vault bán hàng), thêm section đặc thù. Ví dụ:

```markdown
## Bối cảnh — chuyên môn vault

Vault này lưu kiến thức về:
- Phương pháp bán hàng B2B
- Case study deal đã chốt / mất
- Framework đàm phán đã thử

Tránh: chuyện cá nhân, lifestyle, tài chính cá nhân (dùng vault khác).
```

### Ngôn ngữ

Anh Long dùng tiếng Việt 100%. Nếu bạn dùng tiếng Anh hoặc song ngữ — chỉ rõ:

```markdown
## Quy tắc ngôn ngữ

- Mọi nội dung wiki viết bằng tiếng Anh
- Quote nguyên văn từ source giữ ngôn ngữ gốc
- Frontmatter dùng tiếng Anh
```

---

## Bước 3 — Lưu CLAUDE.md

Trong Obsidian:
1. Mở `CLAUDE.md` ở root
2. Paste nội dung template
3. Customize 3 chỗ trên
4. Cmd+S lưu

---

## Bước 4 — Test Claude đọc CLAUDE.md

Mở terminal, `cd` vào vault, chạy `claude`:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Trong prompt:

```
> Đọc CLAUDE.md và tóm tắt schema vault trong 3 dòng
```

Claude phản hồi tóm tắt. Nếu Claude hiểu đúng (kể cả về concept-first, 3 lớp, workflow) → CLAUDE.md hợp lệ.

---

## Bước 5 — Khi nào update CLAUDE.md

3 trường hợp:

1. **AI lặp lại 1 sai** → thêm rule vào CLAUDE.md để AI không lặp
2. **Schema mới phát sinh** (loại page mới, tag mới) → bổ sung
3. **Workflow đổi** (vd: thêm cron, thêm slash command) → mô tả

Không tự AI sửa CLAUDE.md mà không hỏi bạn. Quy tắc cứng.

---

## Bước 6 — Anti-pattern khi viết CLAUDE.md

### Sai 1 — Liệt mọi rule có thể nghĩ ra

CLAUDE.md > 500 dòng → AI mỗi session đọc tốn token, khó nhớ.

→ Giữ CLAUDE.md ≤ 300 dòng. Rule edge case → để memory hoặc agent-specific file.

### Sai 2 — Mô tả Claude bằng giọng third-person

Sai:
> "Claude phải đọc file này. Claude nên viết theo schema..."

Đúng:
> "Đọc file này đầu mỗi session. Viết theo schema..."

Imperative direct. Không Claude-này-Claude-kia.

### Sai 3 — Khoá schema quá chặt

Sai:
> "Concept page BẮT BUỘC có đủ 16 sections, không thiếu cái nào"

Đúng:
> "Concept page có các section bắt buộc: A, B, C. Section khác optional, thêm khi cần."

Schema mềm dẻo, allow stub. Cứng → AI block khi info thiếu.

### Sai 4 — Không có quy ước log

Không có log = không track được history → khó debug khi AI làm sai. Bắt buộc `log.md` format.

---

## Bước 7 — CLAUDE.md template generic

Template đầy đủ generic (không PTL-specific) ở [[99-templates/claude-md-master-template]] — copy thẳng.

---

## Tiếp theo

Đọc tiếp: [[03-cau-truc-folder]] — Cấu trúc folder raw/ + wiki/ chi tiết.
