# CLAUDE.md — Luật chơi vault "Longpt's Setup-Guide"

Vault này là **giáo trình hướng dẫn người mới** xây hệ thống wiki AI-first đa vault giống Phạm Thành Long (anh Long).

**KHÔNG phải knowledge wiki** (Brain). **KHÔNG phải lifestyle** (Life). **KHÔNG phải execution** (4DX). **KHÔNG phải production** (Marketing).

Đây là **lớp META giáo dục** — tài liệu dạy người mới copy mô hình.

## 1. Đối tượng đọc

- Người chưa biết Obsidian + Claude Code
- Người mới biết Obsidian nhưng chưa biết AI-first wiki
- Coach / trainer / founder muốn build hệ knowledge tương tự PTL
- Học viên PTL muốn xây vault cá nhân

**Tone**: dạy từ A-Z, ngôn ngữ phổ thông, không giả định nền tảng kỹ thuật.

## 2. Triết lý guide

Mỗi file trong vault này tuân 3 nguyên tắc:

1. **Why → How → Example**: mỗi mục có 1 đoạn triết lý (tại sao làm thế), command cụ thể (làm thế nào), ví dụ thực từ vault PTL.
2. **Copy-paste được**: template code/markdown trong file 99-templates/ phải paste vào vault mới chạy được ngay, không cần edit.
3. **Tăng dần độ phức tạp**: 00 → 05 đi từ triết lý → cài đặt → vault đầu → multi-vault → agents → bảo trì. Không skip.

## 3. Cấu trúc thư mục

```
Longpt's Setup-Guide/
├── CLAUDE.md              # file này
├── README.md              # cửa vào — đọc đầu tiên
├── index.md               # mục lục đầy đủ
├── log.md                 # nhật ký edit/update
│
├── 00-triet-ly/           # 4 file — tại sao thiết kế thế này
├── 01-cai-dat/            # 5 file — cài Obsidian + Claude + plugins
├── 02-vault-dau-tien-brain/ # 8 file — build vault Brain đầu tiên
├── 03-mo-rong-multi-vault/ # 5 file — khi nào tách + 3 vault sibling
├── 04-agents-skills-memory/ # 5 file — Claude agents + skills + memory
├── 05-bao-tri-lint/       # 4 file — bảo trì wiki dài hạn
└── 99-templates/          # 6 file template copy-paste-able
```

## 4. Quy ước tên file

- Tên file: **tiếng Việt không dấu + kebab-case** (vd: `01-tao-vault-brain.md`)
- Mỗi folder số thứ tự `NN-tieu-de` để Obsidian sort tự nhiên
- File trong folder cũng `NN-tieu-de.md`

## 5. Quy ước nội dung

- Tiếng Việt 100%, xưng "bạn" (gọi người đọc), không xưng "tôi" hay "anh"
- Code block đầy đủ syntax highlight (`bash`, `markdown`, `yaml`, `python`)
- Mỗi command có comment giải thích
- Mỗi step có expected output mẫu

## 6. Quy ước cross-link

Mọi file đều có:
- `## Trước đó` (link file học trước) ở đầu
- `## Tiếp theo` (link file học sau) ở cuối

Để người đọc theo flow tuần tự.

## 7. Quy ước cập nhật

Khi Claude (hoặc anh Long) update vault này:
- Append vào `log.md` với format `## [YYYY-MM-DD] update | <file changed>`
- Update `updated:` trong frontmatter file edit
- Nếu add file mới — update `index.md`

## 8. Không làm gì trong vault này

- KHÔNG ingest source raw (đó là Brain)
- KHÔNG track metric (đó là Marketing)
- KHÔNG log execution (đó là 4DX)
- KHÔNG ghi việc cá nhân (đó là Life)

Vault này CHỈ là tài liệu giáo dục static — viết 1 lần, update khi có version mới.

## 9. Khi không chắc

- Câu hỏi vượt scope guide (vd: detailed Obsidian Dataview query) → link ra docs Obsidian official, không tự viết
- Phần kỹ thuật thay đổi nhanh (Claude Code version) → ghi version snapshot + link release notes
- Step không reproduce được trên máy người đọc → ghi `(môi trường: macOS / Win / Linux)` rõ ràng

## 10. Tự tiến hoá

Khi Claude/anh Long thấy guide thiếu hoặc lỗi thời — propose edit + ask user confirm. Schema drift theo feedback người dùng mới.
