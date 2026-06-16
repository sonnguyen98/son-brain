---
title: Concept page template
type: template
created: 2026-05-29
updated: 2026-05-29
phan: 99
---

# Concept page template (copy-paste)

Template concept page generic. Copy vào `wiki/concepts/<Tên concept>.md` rồi điền.

---

## Template đầy đủ

```markdown
---
type: concept
tags: [framework, course/<code1>, course/<code2>, <theme-tags>, signature]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["[[Source A]]", "[[Source B]]"]
---

# <Tên concept>

<Tóm tắt 2-3 câu — what + why + vai trò trong hệ sinh thái lớn>

## Thông tin module

| Trường | Giá trị |
|---|---|
| Tầm quan trọng | ⭐⭐⭐⭐⭐ (1-5/5) |
| Độ khó | ⭐⭐ (1-5/5) |
| Độ phổ biến | ⭐⭐⭐⭐ (1-5/5 — số lần dạy) |
| Khoá áp dụng | <CODE1>, <CODE2>, ... |
| Module liên quan | [[Concept X]], [[Concept Y]] (top 3-5) |
| Từ khoá | keyword1, keyword2, ... |

<Tuỳ chọn: trích câu signature>

## Định nghĩa

<1-2 đoạn — định nghĩa rõ ràng, không vòng vo>

## Cấu trúc lõi

<Các thành phần / công thức / quy trình áp dụng>

## Ví dụ thực tế

<Case cụ thể minh hoạ — từ source đã ingest>

## Ẩn dụ dễ nhớ

<Metaphor giúp dễ nhớ. Stub nếu chưa có: *(stub — chưa có metaphor explicit trong source)*>

## Sai lầm phổ biến

5 anti-pattern + cách sửa:

1. **<Sai lầm 1>**: <Mô tả>
   → Hậu quả: <gì xấu xảy ra>
   → Cách sửa: <action>

2. **<Sai lầm 2>**: ...

## Khoá học sử dụng

- [[<Course A>]] — vai trò trong khoá (1 dòng)
- [[<Course B>]] — ...

## Phiên bản dạy concept

- **Lần đầu**: [[<Source page>]] (~MM/YYYY)
- **Hệ thống hoá**: [[<Source page>]] (đợt N)
- **Update lớn**: [[<Source page>]] (đợt M) — thêm gì mới

## Khái niệm liên quan

- **cha** [[<Mother>]] — concept rộng hơn
- **con** [[<Sub>]] — concept hẹp hơn
- **đi cặp** [[<Sister>]] — paired
- **đối lập** [[<Opposite>]] — opposite
- **tiền đề** [[<Prereq>]] — phải hiểu trước
- **kế thừa** [[<Successor>]] — phải hiểu sau

## Nguồn gốc & trích dẫn

<External reference nếu có. Phân biệt phần custom vs phần theo source. Stub nếu không: *(stub — concept gốc tự research)*>

## Câu hỏi mở

- ?
```

---

## Variant 1 — Concept đơn giản (≤ 5 section)

Cho concept nhỏ, không cross-version:

```markdown
---
type: concept
tags: [<theme-tag>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: ["[[Source A]]"]
---

# <Tên concept>

<Tóm tắt 2 câu>

## Định nghĩa

<1 đoạn>

## Ví dụ

<1 case>

## Khái niệm liên quan

- [[<Related 1>]]
- [[<Related 2>]]
```

Dùng khi concept là leaf node (không cha/con/đi cặp đầy đủ).

---

## Variant 2 — Concept enumeration (mẹ + con)

Concept là 1 framework có N sub-concept. Vd: "6 Nhu cầu con người".

### Page mẹ

```markdown
---
type: concept
tags: [framework]
---

# 6 Nhu cầu con người

Framework Tony Robbins định nghĩa 6 nhu cầu universal driving human behavior.

## 6 nhu cầu

1. [[Certainty]] — chắc chắn
2. [[Variety]] — đa dạng
3. [[Significance]] — quan trọng
4. [[Connection]] — kết nối
5. [[Growth]] — phát triển
6. [[Contribution]] — đóng góp

## Phân loại

- 4 nhu cầu cá nhân: Certainty, Variety, Significance, Connection
- 2 nhu cầu tâm linh: Growth, Contribution

## Ứng dụng

Identify top 2 driving needs → understand motivation pattern.

## Khái niệm liên quan

- **cha** [[Tâm lý động lực]]
- **con** [[Certainty]], [[Variety]], [[Significance]], [[Connection]], [[Growth]], [[Contribution]]
```

### Page con

```markdown
---
type: concept
tags: [framework, 6-nhu-cau-con]
---

# Certainty

1 trong 6 nhu cầu con người (Tony Robbins). 

## Định nghĩa

Nhu cầu cảm thấy chắc chắn — biết điều gì sẽ xảy ra tiếp theo.

## Biểu hiện

- Tìm pattern, rule, structure
- Tránh rủi ro
- Lập kế hoạch chi tiết

## Khái niệm liên quan

- **cha** [[6 Nhu cầu con người]]
- **đi cặp** [[Variety]] — opposite balancing
```

---

## Variant 3 — Concept cross-version (PTL pattern)

Concept dạy qua nhiều phiên bản khoá học:

```markdown
---
type: concept
tags: [framework, course/sss, course/bhtc, course/raving-fan, signature]
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[BHTC - Phần 1 (Livestream)]]"
  - "[[SSS 10 - Ngày 1 (15-07-2020)]]"
  - "[[SSS 21 - Ngày 1 (28-11-2025)]]"
---

# Hệ thống bán hàng 8+2

Framework 8 bước quy trình bán hàng B2C cá nhân hoá kèm 2 nguyên tắc độc lập. Concept lõi của khoá SSS.

## Thông tin module

| Trường | Giá trị |
|---|---|
| Tầm quan trọng | ⭐⭐⭐⭐⭐ |
| Độ khó | ⭐⭐⭐ |
| Độ phổ biến | ⭐⭐⭐⭐⭐ (>10 lần) |
| Khoá áp dụng | SSS, BHTC, RAVING FAN |
| Module liên quan | [[14 chiến lược lead generation]], [[7 kỹ thuật xử lý từ chối]] |
| Từ khoá | bán hàng, B2C, sales process, 8 bước |

## 8 bước cốt lõi

| # | Bước | Vai trò |
|---|---|---|
| 1 | <Bước 1> | <vai trò> |
| ... |

## 2 nguyên tắc độc lập

| # | Nguyên tắc | Vai trò |
|---|---|---|
| 1 | <Nguyên tắc 1> | ... |
| 2 | <Nguyên tắc 2> | ... |

## Khoá học sử dụng

- [[SSS - Sales Success System]] — module chính (12h dạy live)
- [[BHTC - Bán Hàng Thành Công]] — tiền thân lịch sử (12/2012)
- [[RAVING FAN]] — mở rộng giai đoạn after-sales

## Phiên bản dạy concept

- **Lần đầu**: [[BHTC - Phần 1 (Livestream)]] (~12/2012, livestream)
- **Hệ thống hoá**: [[SSS 10 - Ngày 1 (15-07-2020)]] (đợt 10) — full 8 bước + 2 độc lập
- **Update lớn**: [[SSS 21 - Ngày 1 (28-11-2025)]] (đợt 21) — thêm 14 lead gen, 7 kỹ thuật xử lý từ chối

## Khái niệm liên quan

- **cha** [[Hệ thống bán hàng chung]]
- **con** [[8 bước cá nhân hoá]], [[2 nguyên tắc độc lập]]
- **đi cặp** [[14 chiến lược lead generation]]
- **tiền đề** [[Customer Value Canvas]]

## Nguồn gốc & trích dẫn

*(stub — concept gốc Phạm Thành Long tự research, kết tinh 25 năm điều hành Luật Gia Phạm)*

## Câu hỏi mở

- Phiên bản 22 (chưa ingest) có gì khác 21?
- Có version online ngắn 6h thay vì 3 ngày?
```

---

## Quy tắc rating

### Tầm quan trọng

| Score | Tiêu chí |
|---|---|
| 5/5 | Cross 5+ khoá hoặc concept mẹ |
| 4/5 | Cross 3-4 khoá hoặc signature lớn |
| 3/5 | 2-3 khoá hoặc sub-concept |
| 2/5 | 1 khoá hoặc concept hẹp |
| 1/5 | Stub hoặc obscure |

### Độ khó

| Score | Tiêu chí |
|---|---|
| 5/5 | Cần 2+ khoá nền |
| 4/5 | Cần 1 khoá nền |
| 3/5 | Hiểu trong 1 buổi giảng |
| 2/5 | Hiểu trong 30 phút |
| 1/5 | Hiểu ngay |

### Độ phổ biến

| Score | Tiêu chí |
|---|---|
| 5/5 | 10+ lần xuyên mọi khoá |
| 4/5 | 5-9 lần |
| 3/5 | 3-4 lần |
| 2/5 | 2 lần |
| 1/5 | 1 lần signature |

---

## Tiếp theo

[[source-page-template]] — Source page template.
