# Longpt's Setup-Guide — Giáo trình xây hệ thống wiki AI-first

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Obsidian-Vault-purple)](https://obsidian.md)
[![Claude](https://img.shields.io/badge/Claude-Code-orange)](https://claude.com/claude-code)
[![Deploy MkDocs to GitHub Pages](https://github.com/wwwlongvn/longpt-setup-guide/actions/workflows/deploy.yml/badge.svg)](https://github.com/wwwlongvn/longpt-setup-guide/actions/workflows/deploy.yml)
[![Website](https://img.shields.io/badge/Website-Live-brightgreen)](https://wwwlongvn.github.io/longpt-setup-guide/)
[![Discussions](https://img.shields.io/badge/Discussions-Join-blue)](https://github.com/wwwlongvn/longpt-setup-guide/discussions)

Chào mừng bạn đến với giáo trình dạy bạn xây hệ thống wiki cá nhân giống anh Phạm Thành Long — **AI-first**, **concept-first**, **multi-vault**.

> Repo này chính là 1 vault Obsidian. Có 3 cách đọc:
>
> 1. 🌐 **[Đọc online](https://wwwlongvn.github.io/longpt-setup-guide/)** — không cần cài gì
> 2. 📦 **Clone về** mở bằng Obsidian (có graph view + wikilink interactive)
> 3. 💬 **[Vào Discussions](https://github.com/wwwlongvn/longpt-setup-guide/discussions)** hỏi đáp với cộng đồng

## ⚡ Cài đặt nhanh

### Cách 0 — Đọc website (nhanh nhất, không cần cài gì)

→ **[https://wwwlongvn.github.io/longpt-setup-guide/](https://wwwlongvn.github.io/longpt-setup-guide/)**

Có search tiếng Việt, dark mode, responsive mobile. Đọc giáo trình online ngay không cần download.

### Cách 1 — Clone về iCloud Drive (Mac, khuyên cho người làm theo)

```bash
cd "$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents"
git clone https://github.com/wwwlongvn/longpt-setup-guide.git "Longpt's Setup-Guide"
```

Mở Obsidian → **Open folder as vault** → chọn folder `Longpt's Setup-Guide`.

### Cách 2 — Clone về folder bất kỳ

```bash
cd ~/Documents
git clone https://github.com/wwwlongvn/longpt-setup-guide.git
```

Mở Obsidian → **Open folder as vault** → chọn folder `longpt-setup-guide`.

### Cách 3 — Tải ZIP (không cần Git, không cần Obsidian)

**Cách nhanh nhất — click link tải luôn**:

→ [📦 Download ZIP (~150KB)](https://github.com/wwwlongvn/longpt-setup-guide/archive/refs/heads/main.zip)

**Hoặc qua GitHub UI**:

1. Vào https://github.com/wwwlongvn/longpt-setup-guide
2. Tìm nút **xanh `<> Code`** ở góc phải trên list file (KHÔNG phải trên topbar đen)
3. Click → dropdown mở → tab **Local** → cuối dropdown có nút **"Download ZIP"**
4. Click → ZIP tải về (~150KB)

**Sau khi có ZIP — đọc ngay file [QUICK-START.md](QUICK-START.md)** trong folder vừa giải nén. File đó hướng dẫn 3 lộ trình tuỳ mục đích:

- 🅰️ Chỉ đọc giáo trình (không cài gì)
- 🅱️ Đọc với Obsidian (15 phút cài)
- 🅲️ Build vault Brain của bạn từ zero (2-3 tuần)

→ Click `QUICK-START.md` sau khi giải nén — checklist 30 phút đầu giúp bạn không stuck.

**Phiên bản có tag** (nếu cần version stable, không thay đổi):

→ [Releases](https://github.com/wwwlongvn/longpt-setup-guide/releases) — chọn version + download ZIP attachment

---

## Bạn sẽ học được gì

Giáo trình gồm **37 file nội dung** + 4 file root + **7 skills bundled** (sẵn sàng dùng), chia 7 phần.

Sau khi hoàn thành giáo trình này, bạn sẽ có:

- **1 hệ thống multi-vault Obsidian** đồng bộ qua iCloud, được AI Claude quản lý
- **1 vault knowledge "Brain"** kiểu concept-first — AI đọc raw 1 lần, viết wiki, không phải scan lại mỗi khi query
- **3 vault sibling** (Life lifestyle / 4DX execution / Marketing production) tách bạch rõ ràng
- **Agents + skills + memory** Claude tự xử lý workflow lặp đi lặp lại
- **Quy trình lint + backup + migration** để vault sống dài hạn không bị mục
- **7 skills bundled** sẵn sàng dùng: `ips-cmo`, `ho-so-khach-hang-vpc`, `cai-dat-tu-duy`, `tho-ho-xuan-huong`, `text-cat-chunk`, `srt-cat-chunk`, `blog-nau-an` — chi tiết [.claude/skills/](.claude/skills/)

Tổng thời gian học: **15-20 giờ** trải dài 1-2 tuần (không cố ngồi 1 ngày).

## Đối tượng

Giáo trình này viết cho:

- Người **chưa biết Obsidian** (sẽ dạy từ install)
- Người **chưa biết Claude Code** (sẽ dạy từ tạo account, cài CLI)
- Coach / trainer / founder muốn copy mô hình wiki PTL
- Học viên các khoá SSS / IPS / LTVM / Eagle Camp muốn build vault cá nhân

Không cần:
- Biết lập trình
- Biết command line nâng cao (sẽ dạy lệnh cơ bản)
- Có máy Mac (Windows + Linux cũng được, có note riêng)

## Yêu cầu trước khi bắt đầu

- **Máy tính** (macOS / Windows / Linux đều được, hướng dẫn ưu tiên macOS)
- **iCloud Drive** hoặc dịch vụ sync tương đương (Dropbox / Google Drive / OneDrive)
- **Tài khoản Anthropic** (để dùng Claude — có gói trả phí)
- **Tài khoản GitHub** (tuỳ chọn — để backup vault)
- **2-3 giờ tuần đầu** để cài đặt và build vault Brain đầu tiên

## Lộ trình học

Đi tuần tự 6 phần:

| Phần | Nội dung | Thời gian |
|---|---|---|
| [00-triet-ly](00-triet-ly/) | 4 file — Tại sao thiết kế thế này | 1-2h |
| [01-cai-dat](01-cai-dat/) | 5 file — Cài Obsidian + Claude + plugins | 2-3h |
| [02-vault-dau-tien-brain](02-vault-dau-tien-brain/) | 8 file — Build vault Brain đầu tiên | 4-6h |
| [03-mo-rong-multi-vault](03-mo-rong-multi-vault/) | 5 file — Tách sang Life / 4DX / Marketing | 3-4h |
| [04-agents-skills-memory](04-agents-skills-memory/) | 5 file — Claude agents + skills + memory | 3-4h |
| [05-bao-tri-lint](05-bao-tri-lint/) | 4 file — Bảo trì wiki dài hạn | 1-2h |

Sau khi xong 02 → đã chạy được vault Brain cơ bản. 03-05 là mở rộng.

## Cách dùng giáo trình

**Cách 1 — Đọc tuần tự**: theo flow `## Tiếp theo` ở cuối mỗi file.

**Cách 2 — Tra cứu**: dùng [index.md](index.md) để tìm topic cụ thể.

**Cách 3 — Copy template trước**: vào thẳng [99-templates](99-templates/) lấy template, đọc triết lý sau.

## Quy ước trong giáo trình

- Khi thấy `bạn` — là người đọc (bạn)
- Khi thấy `anh Long` — là Phạm Thành Long (tác giả mô hình)
- Khi thấy `Claude` — là AI Claude (sẽ dùng để build vault)
- Khi thấy code block `bash` — copy paste vào terminal
- Khi thấy code block `markdown` — copy paste vào file `.md`

## Khi gặp khó khăn

- Stuck step nào → đọc lại `## Trước đó` để chắc nền tảng
- Lỗi command line → screenshot + hỏi Claude trực tiếp
- Lỗi setup Obsidian → search Obsidian Help (Cmd+H trong app)

## Bắt đầu

**Người mới hoàn toàn**: đọc [QUICK-START.md](QUICK-START.md) trước — checklist 30 phút đầu + 3 lộ trình.

**Sẵn sàng đi luôn**: vào file đầu tiên [00-triet-ly/01-tai-sao-ai-first-wiki.md](00-triet-ly/01-tai-sao-ai-first-wiki.md).

---

## License

[MIT License](LICENSE) — bạn được phép clone, fork, chỉnh sửa, dùng cho mục đích cá nhân + thương mại. Giữ copyright notice là OK.

## Đóng góp

Phát hiện lỗi / typo / unclear step? Mở [Issue](https://github.com/wwwlongvn/longpt-setup-guide/issues) hoặc [Pull Request](https://github.com/wwwlongvn/longpt-setup-guide/pulls).

Đề xuất phần mới / template mới? Discuss trong [Discussions](https://github.com/wwwlongvn/longpt-setup-guide/discussions/categories/ideas) trước khi PR.

Stuck step nào? Hỏi trong [Discussions Q&A](https://github.com/wwwlongvn/longpt-setup-guide/discussions/categories/q-a).

Build xong vault rồi? Khoe trong [Show and tell](https://github.com/wwwlongvn/longpt-setup-guide/discussions/categories/show-and-tell)!

## Tác giả

**Phạm Thành Long** (anh Long) — Founder Sứ Mệnh Lãnh Đạo · Director BNI HN6 · Coach (SSS / IPS / LTVM / Eagle Camp / Ultimate Trainer / DTSGC / MAP).

Giáo trình này được Claude AI co-author dựa trên 14 vault Obsidian thực tế anh Long đã vận hành.

## Liên kết

- Website: https://long.vn
- YouTube: https://youtube.com/@longguru
- Sale page khoá học: https://store.long.vn
