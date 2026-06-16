---
title: Tại sao AI-first wiki
type: triet-ly
created: 2026-05-29
updated: 2026-05-29
phan: 00
---

# Tại sao AI-first wiki

## Trước đó

Bạn đang ở file đầu tiên. Không cần đọc gì trước.

---

## Vấn đề wiki truyền thống

Bạn đã từng thử dùng:
- Notion để lưu kiến thức?
- Evernote để lưu bài clip?
- Google Docs để lưu meeting note?
- File Word/Excel rời rạc trên máy?

Sau 6-12 tháng, hầu hết người dùng đều rơi vào 1 trong 3 trạng thái:

### Trạng thái 1 — Bãi rác kỹ thuật số

Hàng trăm note rời rạc, không ai liên kết với ai. Bạn lưu 50 bài về "bán hàng" nhưng khi cần ý cụ thể về *"cách xử lý từ chối khi khách nói đắt"* — bạn không tìm thấy. Search keyword trả về 200 kết quả, scroll mệt nghỉ.

### Trạng thái 2 — Wiki khô, không ai đọc lại

Bạn cẩn thận viết 1 wiki Notion đẹp, có table of contents, có folder. Nhưng sau 3 tháng, không ai (kể cả bạn) đọc lại. Lý do: lúc cần tra cứu, bạn phải nhớ cấu trúc folder bạn đã đặt → quên → search → không ra.

### Trạng thái 3 — Wiki phải duy trì thủ công

Bạn vừa viết wiki vừa phải dọn dẹp: rename file, fix broken link, gộp note trùng, update info cũ. Việc duy trì ngốn thời gian hơn việc viết.

---

## Cách giải truyền thống (và tại sao không đủ)

Người ta thường đề xuất:
- **PARA method** (Projects / Areas / Resources / Archives) — Tiago Forte
- **Zettelkasten** — Niklas Luhmann
- **Building a Second Brain** — Tiago Forte (bài bản hơn)

Các phương pháp này hay, nhưng vẫn yêu cầu **bạn là người vận hành wiki**: bạn quyết tag, bạn cross-link, bạn ngồi reorganize.

Kết quả: 80% người bỏ cuộc sau 3-6 tháng vì gánh nặng duy trì.

---

## AI-first wiki — pivot mindset

Câu hỏi đúng không phải *"phương pháp tổ chức nào tốt nhất?"* mà là:

> *"Ai sở hữu việc viết và duy trì wiki?"*

Cách trả lời truyền thống: **bạn sở hữu**. Bạn viết, bạn cross-link, bạn lint.

Cách AI-first: **AI sở hữu lớp wiki**. Bạn chỉ thả raw vào. AI đọc, tóm tắt, cross-link, lint. Bạn chỉ duyệt và thỉnh thoảng góp ý.

### Ai làm gì

| Việc | Người (bạn) | AI (Claude) |
|---|---|---|
| Thả source raw (article, ghi chú, ảnh, PDF) | ✅ | |
| Đọc source | | ✅ |
| Tóm tắt source thành wiki page | | ✅ |
| Tạo concept page mới | | ✅ |
| Cross-link giữa các page | | ✅ |
| Lint wiki (broken link, orphan, mâu thuẫn) | | ✅ |
| Quyết tổng thể hướng tổ chức | ✅ | (đề xuất) |
| Edit conflict / sửa AI nếu sai | ✅ | |
| Query wiki (hỏi 1 câu, lấy synthesis) | ✅ | (trả lời) |

---

## Vì sao bây giờ làm được mà 5 năm trước không

3 yếu tố cộng hưởng:

1. **LLM context window đủ dài**: Claude Opus 4 có 1 triệu token context — đọc 1 vault 200 page 1 lần là chuyện thường.
2. **LLM hiểu markdown + wikilink native**: AI biết `[[Page Name]]` là wikilink, biết frontmatter YAML, biết cấu trúc Obsidian.
3. **Tool use phổ thông**: Claude Code, MCP servers → AI đọc/ghi file trực tiếp, không cần copy-paste qua chat.

5 năm trước chưa làm được vì:
- Context ngắn (4k token) → AI không đọc nổi 1 file dài
- Không có tool use → mọi tương tác qua chat manual
- LLM không hiểu sâu cấu trúc folder

---

## Lợi ích thực tế

Anh Phạm Thành Long đã chạy mô hình này từ 2026. Sau ~3 tháng:

- **Vault Brain**: ~600+ concept page, 1000+ source page, được liên kết bidirectional. Khi hỏi *"Hệ thống bán hàng 8+2 dùng ở khoá nào?"* — Claude trả lời trong 5 giây, kèm 6 wikilink.
- **Vault Life**: ~40 con cá koi mỗi con 1 hồ sơ, GPS + EXIF auto-extract từ ảnh iPhone. Hỏi *"Tháng 3 có ảnh anh đi caravan ở đâu?"* — Claude liệt 8 event.
- **Vault 4DX**: cron đêm CN tự generate báo cáo tuần, sáng T2 anh có PDF đọc cà phê với vợ — không phải tự tổng hợp.
- **Vault Marketing**: track 30+ lead/sale page variant, A/B test report tự sinh.

Tổng cộng: **14 vault sibling**, hơn 10.000 page wiki. Anh Long *không bao giờ ngồi gõ cross-link thủ công*. AI làm hết.

---

## Quy tắc vàng

> **AI viết. Bạn duyệt.**

Cả mô hình rút gọn về 4 từ đó.

Bạn không phải:
- Là người tổ chức wiki (AI làm)
- Là người dọn dẹp (AI làm)
- Là người cross-link (AI làm)

Bạn phải:
- Quyết chiến lược tổng (vault nào tách, nào gộp)
- Drop raw source vào (article, transcript, ảnh)
- Duyệt output AI (sai thì chỉ chỗ, đúng thì OK)
- Thỉnh thoảng update CLAUDE.md (luật chơi)

---

## Khi nào KHÔNG nên dùng AI-first wiki

- Bạn ghét đọc lại nội dung dài (AI viết wiki dạng prose, không phải bullet ngắn)
- Bạn cần share wiki cho team 10+ người (Obsidian là local-first, không phải multi-user collab)
- Bạn cần real-time editing nhiều người (dùng Notion thì hơn)
- Bạn không có ngân sách Claude trả phí (~$20-200/tháng tuỳ usage)

Nếu 4 điểm trên không sao → tiếp tục giáo trình.

---

## Tiếp theo

Đọc tiếp: [[02-tai-sao-concept-first]] — Tại sao concept là đơn vị lưu trữ, không phải source page.
