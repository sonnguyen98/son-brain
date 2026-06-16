---
title: Tại sao concept-first
type: triet-ly
created: 2026-05-29
updated: 2026-05-29
phan: 00
---

# Tại sao concept-first

## Trước đó

[[01-tai-sao-ai-first-wiki]] — bạn đã hiểu AI làm thay bạn việc viết wiki.

---

## Câu hỏi cốt lõi

Khi AI đọc 100 source về 1 chủ đề, AI viết ra cái gì?

**Cách 1 — Source-first**: AI viết 100 file tóm tắt, mỗi file = 1 source. Khi query, AI scan 100 file lại.

**Cách 2 — Concept-first**: AI extract khái niệm từ 100 source, viết 50 concept page (mỗi khái niệm 1 page). Source page chỉ là snapshot ghi nhận. Khi query, AI tổng hợp từ concept page.

---

## Tại sao cách 1 thất bại

Bạn ingest 100 video PTL dạy về "bán hàng". Mỗi video AI viết 1 source page tóm tắt 5-10 ý.

Khi bạn hỏi: *"Hệ thống bán hàng 8+2 là gì?"*

AI phải:
1. Scan 100 source page tìm cái nào nhắc "8+2"
2. Đọc lại các đoạn liên quan
3. Tổng hợp thành câu trả lời

→ Mỗi lần hỏi = mỗi lần scan lại. Tốn token. Trùng lặp. Không tận dụng được sức mạnh wiki.

Tệ hơn: khi PTL **dạy lại 8+2 lần thứ 5** với bản mới, AI viết source page mới. Bây giờ có 5 version mô tả 8+2 nằm rải rác trong 5 source page. AI phải merge lại mỗi khi query.

---

## Concept-first — quy tắc

**Concept = đơn vị lưu trữ cuối cùng**. Mọi thứ khác (source / course / student) là context để concept có nghĩa.

Khi AI đọc source mới:
1. Hỏi: *"Concept nào đang nổi lên? Concept nào đã có cần update?"*
2. Tạo concept page mới (nếu chưa có) hoặc update concept page cũ (nếu đã có)
3. Source page chỉ snapshot ngắn (date, raw_path, list concept đã touch)
4. Tuyệt đối KHÔNG viết lại logic concept trong source page

Khi bạn query:
1. AI tổng hợp từ concept page (đã vet, có line ref, cross-link)
2. KHÔNG đọc lại 100 source

---

## Ví dụ cụ thể từ vault PTL

Khái niệm **"Hệ thống bán hàng 8+2"** được PTL dạy trong:
- BHTC livestream 12/2012 (lần đầu)
- SSS 10 (07/2020) — hệ thống hoá đủ 8 bước
- SSS 19 (10/2024) — thêm pivot LonGPT
- SSS 21 (11/2025) — thêm 14 chiến lược lead gen

Theo cách source-first: 4 source page mô tả 8+2, mỗi page 1 version.

Theo cách concept-first: **1 concept page** `Hệ thống bán hàng 8+2.md` có:
- Định nghĩa
- 8 bước cốt lõi + 2 độc lập
- Section "Phiên bản dạy concept": list 4 source page kèm line ref + ghi update gì mới

Khi query *"8+2 mới nhất khác cũ thế nào?"* — AI đọc 1 concept page, trả lời ngay.

---

## Atomicity — quy tắc tách nhỏ

Mỗi **khái niệm độc lập** = 1 page riêng. KHÔNG gộp 2 khái niệm vào 1 page chỉ vì chúng được dạy cặp đôi.

### Ví dụ phải tách

- **Giá trị hướng đến** vs **Giá trị né tránh** → 2 page (đối nghịch ý nghĩa)
- **Quy tắc hướng đến** vs **Quy tắc né tránh** → 2 page (cấu trúc khác: HĐ = "Tôi cảm thấy / mỗi khi / HOẶC" vs NT = "giải pháp đính kèm")

### Ví dụ gộp được

- **Victors vs Victims** → 1 page (dichotomy đơn, PTL không dạy 2 cấu trúc riêng)
- **6 Nhu cầu con người** → 1 page (6 mục là enumeration của 1 framework duy nhất)

### Heuristic quyết định

1. Có **cấu trúc riêng** (công thức / ví dụ / quy trình áp dụng khác)? → tách
2. Có **line ref riêng** trong source (PTL dạy 2 đoạn distinct)? → tách
3. Có thể **link độc lập** từ concept khác? → tách
4. Là **enumeration** của 1 framework chung? → gộp + page con cho mỗi mục nếu signature

---

## Memory cue cho AI

Mỗi session, AI nên nhớ:

> *Wiki này tồn tại để các concept page atomic + cross-link tạo nên 1 graph kiến thức trả lời được mọi truy vấn mà không cần đọc lại raw.*

Mọi quyết định AI phải tối ưu theo mục tiêu này.

---

## Quy ước concept page

Mỗi concept page có sections bắt buộc:

```markdown
---
type: concept
tags: [framework, course/<code>, signature]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["[[Source A]]", "[[Source B]]"]
---

# Tên concept

[Tóm tắt 2-3 câu]

## Khoá học sử dụng        # bắt buộc, link course MOC
- [[Course A]] — vai trò trong khoá

## Phiên bản dạy concept   # bắt buộc nếu cross-version
- **Lần đầu**: [[Source X]] (~MM/YYYY)
- **Hệ thống hoá**: [[Source Y]]
- **Update lớn**: [[Source Z]] — thêm gì mới

## Khái niệm liên quan     # có nhãn semantic
- **cha** [[Concept mẹ]] — concept rộng chứa cái này
- **con** [[Concept con]] — concept hẹp nằm trong cái này
- **đi cặp** [[Sister]] — paired
- **đối lập** [[Opposite]]
- **tiền đề** [[Prereq]]
- **kế thừa** [[Successor]]
```

Template đầy đủ ở [[99-templates/concept-page-template]].

---

## Lợi ích thực tế

Vault PTL có ~600 concept page. Mỗi concept page trung bình link 4-8 concept khác. Tạo ra graph dense 4000+ edge.

Khi bạn query *"trong khoá SSS, concept nào liên quan đến Bộ não thứ 2?"*:
- Source-first: AI scan ~50 source page khoá SSS → mất 30 giây + 100k token
- Concept-first: AI đọc concept page "Bộ não thứ 2" → section "Khái niệm liên quan" → list 5 concept → trả lời trong 5 giây + 20k token

**Tốc độ ×6, chi phí /5.**

---

## Tiếp theo

Đọc tiếp: [[03-tai-sao-multi-vault]] — Tại sao tách thành nhiều vault thay vì 1 vault to.
