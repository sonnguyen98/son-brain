# 🚀 QUICK START — Bạn vừa tải ZIP về, làm gì tiếp?

Chào bạn. Bạn vừa giải nén `longpt-setup-guide-main.zip` (hoặc clone repo). Đây là việc tiếp theo theo **mục đích** của bạn.

---

## ❓ Bạn thuộc nhóm nào?

| Nhóm | Mục đích | Đi tới |
|---|---|---|
| 🅰️ | Chỉ **đọc giáo trình** xem nó nói gì, chưa muốn build | [→ Mục A](#a-chỉ-đọc-giáo-trình-không-cần-cài-gì) |
| 🅱️ | Đọc giáo trình **với trải nghiệm Obsidian** (graph view + wikilink interactive) | [→ Mục B](#b-đọc-với-obsidian-đẹp-hơn-15-phút-cài) |
| 🅲️ | Build **vault Brain của riêng mình** theo giáo trình | [→ Mục C](#c-build-vault-brain-của-bạn-từ-zero-2-3-tuần) |

---

## A — Chỉ đọc giáo trình (không cần cài gì)

**Nhanh nhất**: vào website online thay vì tải ZIP.

→ **https://wwwlongvn.github.io/longpt-setup-guide/**

Có search tiếng Việt, dark mode, mục lục 7 phần.

**Hoặc đọc local từ ZIP**:

1. Giải nén ZIP (double-click trên Mac / chuột phải → Extract All trên Windows)
2. Mở file `README.md` bằng:
   - Trình duyệt (kéo file vào Chrome / Safari — render OK)
   - VS Code (Cmd+Shift+V preview)
   - Text editor bất kỳ (đọc plain text)
3. Đọc theo flow: `README` → `00-triet-ly/01-tai-sao-ai-first-wiki.md` → tuần tự 7 phần

**Lưu ý**: đọc plain markdown không có wikilink interactive — `[[Page Name]]` hiện như text. Muốn click được → đi sang **Mục B** dưới.

---

## B — Đọc với Obsidian (đẹp hơn, 15 phút cài)

### Bước 1 — Cài Obsidian (5 phút, miễn phí)

1. Vào https://obsidian.md → Download cho OS của bạn (macOS / Windows / Linux)
2. Cài như app thường (.dmg trên Mac, .exe trên Windows)
3. Mở Obsidian — màn hình chào hiện ra

### Bước 2 — Đặt folder vault đúng chỗ

Folder ZIP giải nén thường tên `longpt-setup-guide-main/`. Bạn có thể:

**Cách 1 — Đặt trong iCloud Drive (Mac, khuyên — sync iPhone đọc được)**:

```
~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Longpt's Setup-Guide/
```

Trên Mac: mở Finder → Sidebar → **iCloud Drive** → kéo folder vào.

**Cách 2 — Đặt local đâu cũng được**:

Vd: `~/Documents/Longpt's Setup-Guide/` hoặc `~/Vaults/Longpt's Setup-Guide/`.

**Optional rename**: đổi tên folder từ `longpt-setup-guide-main` → `Longpt's Setup-Guide` cho đẹp.

### Bước 3 — Mở vault trong Obsidian

1. Obsidian → click **"Open folder as vault"** (màn hình chào)
2. Chọn folder bạn vừa đặt → **Open**
3. Obsidian hỏi "Trust author?" → click **Trust author and enable plugins**

Obsidian load vault. Bạn thấy sidebar trái có:
- `README.md`, `index.md`, `CLAUDE.md`, `log.md`, `QUICK-START.md` (file này)
- 7 folder: `00-triet-ly/`, `01-cai-dat/`, ..., `99-templates/`

### Bước 4 — Bắt đầu đọc

Click `README.md` → đọc → theo link `→ Tiếp theo` ở cuối mỗi file → đi tuần tự 7 phần.

Hoặc click `index.md` → có mục lục đầy đủ 37 file.

### Bước 5 — Tận dụng features Obsidian

- **Cmd+O** (Mac) / **Ctrl+O** (Win): tìm file nhanh
- **Cmd+G** / **Ctrl+G**: mở Graph view — thấy mạng liên kết
- **Cmd+P**: command palette
- Click vào bất kỳ `[[Wikilink]]` → mở file đó

---

## C — Build vault Brain của bạn (từ zero, 2-3 tuần)

Đây là mục tiêu **chính** của giáo trình. Bạn sẽ:

- Có **vault Brain riêng** lưu kiến thức cá nhân
- Có **AI Claude** đọc raw, viết wiki tự động
- (Optional) Mở rộng thành **multi-vault** (Life, Marketing, 4DX)

### Lộ trình 3 tuần

**Tuần 1 — Học triết lý + cài đặt** (~5 giờ)

1. Làm theo **Mục B** trên để mở vault Setup-Guide trong Obsidian
2. Đọc **[00-triet-ly](00-triet-ly/)** đầy đủ 4 file (~1-2 giờ)
3. Làm theo **[01-cai-dat](01-cai-dat/)** 5 file:
   - Cài Obsidian ✅ (đã làm ở bước trên)
   - Cài iCloud sync
   - Cài Claude Code CLI (yêu cầu tài khoản Anthropic Pro $20/tháng)
   - Cài plugins Obsidian (Dataview, Web Clipper)

**Tuần 2 — Build vault Brain đầu tiên** (~6-10 giờ)

Làm theo **[02-vault-dau-tien-brain](02-vault-dau-tien-brain/)** 8 file:

1. Tạo vault Brain MỚI (KHÔNG sửa Setup-Guide — vault này chỉ là giáo trình)
2. Copy CLAUDE.md template từ `99-templates/claude-md-master-template.md` vào vault Brain mới
3. Tạo folder `raw/`, `wiki/sources/`, `wiki/concepts/`, ...
4. Ingest 3-5 source đầu tiên (article web, transcript YouTube, sách bạn đang đọc)
5. Query wiki đầu tiên — trải nghiệm "AI viết, bạn duyệt"

**Sau Tuần 2** → vault Brain của bạn chạy được. Có thể stop ở đây nếu chỉ cần knowledge wiki.

**Tuần 3 (optional) — Mở rộng** (~5-8 giờ)

Tuỳ nhu cầu:
- Cần tracking lifestyle (cá, xe, sức khoẻ) → làm [03-mo-rong-multi-vault/02-vault-life-lifestyle](03-mo-rong-multi-vault/02-vault-life-lifestyle.md)
- Cần OKR + execution tracking → làm [03-mo-rong-multi-vault/03-vault-4dx-execution](03-mo-rong-multi-vault/03-vault-4dx-execution.md)
- Cần marketing + asset tracking → làm [03-mo-rong-multi-vault/04-vault-marketing](03-mo-rong-multi-vault/04-vault-marketing.md)
- Cần tự động hoá workflow → làm [04-agents-skills-memory](04-agents-skills-memory/)

---

## ⚠️ Lưu ý quan trọng

### Vault Setup-Guide ≠ Vault Brain của bạn

Folder ZIP bạn giải nén là **vault Setup-Guide** — chỉ chứa **giáo trình**. Đây KHÔNG phải vault knowledge bạn sẽ dùng hàng ngày.

Sau khi học xong, bạn tạo **vault MỚI** (vd: `My Brain`, `Acme Brain`) ở folder khác. Vault Setup-Guide chỉ để tham khảo.

So sánh:

| Vault Setup-Guide (folder này) | Vault Brain (bạn sẽ tạo) |
|---|---|
| Chứa giáo trình 37 file | Chứa kiến thức cá nhân bạn |
| Read-only (đừng sửa) | Bạn ingest source vào, AI viết wiki |
| Update khi có version mới (git pull) | Bạn build theo style của bạn |

### Đừng bỏ vault Setup-Guide

Giữ vault Setup-Guide như tài liệu reference. Khi bạn lint vault Brain, refactor schema, hoặc gặp issue — quay lại Setup-Guide tra cứu.

### Cần Pro plan Claude

Giáo trình giả định bạn dùng **Claude Code CLI** với tài khoản Anthropic Pro ($20/tháng). Free plan không đủ.

Chi tiết ở [01-cai-dat/03-cai-claude-code.md](01-cai-dat/03-cai-claude-code.md).

---

## 🆘 Stuck thì làm gì

| Vấn đề | Đi đâu |
|---|---|
| Không hiểu khái niệm | Đọc lại Phần 00 triết lý |
| Lỗi cài đặt | [GitHub Discussions Q&A](https://github.com/wwwlongvn/longpt-setup-guide/discussions/categories/q-a) |
| Đề xuất cải tiến giáo trình | [GitHub Discussions Ideas](https://github.com/wwwlongvn/longpt-setup-guide/discussions/categories/ideas) |
| Bug / typo | [GitHub Issues](https://github.com/wwwlongvn/longpt-setup-guide/issues) |
| Build xong vault → khoe | [Show and tell](https://github.com/wwwlongvn/longpt-setup-guide/discussions/categories/show-and-tell) |

---

## 📋 Checklist 30 phút đầu

Sau khi tải ZIP, làm theo checklist:

- [ ] Giải nén ZIP
- [ ] Mở `QUICK-START.md` (file này) — bạn đang ở đây ✓
- [ ] Quyết nhóm: A / B / C
- [ ] Cài Obsidian (nếu nhóm B hoặc C)
- [ ] Mở vault trong Obsidian (nếu nhóm B hoặc C)
- [ ] Đọc `README.md`
- [ ] Đọc `00-triet-ly/01-tai-sao-ai-first-wiki.md`
- [ ] (Optional) Sign up Anthropic Pro nếu định build vault thật

---

## 👉 Bước tiếp theo

Click một trong các link sau:

- 📖 **[Đọc README đầy đủ](README.md)** — overview giáo trình
- 🧭 **[Mục lục 37 file](index.md)** — tìm topic cụ thể
- 🎯 **[Bắt đầu Phần 00 triết lý](00-triet-ly/01-tai-sao-ai-first-wiki.md)** — đi vào ngay
- 🛠️ **[Phần 99 Templates copy-paste](99-templates/)** — lấy template nhanh

Chúc bạn build vault thành công 🚀
