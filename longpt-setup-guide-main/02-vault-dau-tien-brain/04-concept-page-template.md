---
title: Concept page template
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Concept page template

## Trước đó

[[03-cau-truc-folder]] — cấu trúc folder OK.

---

## Concept page là gì

Concept page = 1 khái niệm độc lập. Đây là **đơn vị lưu trữ chính** của wiki — bạn nhớ rule "concept-first" ở [[00-triet-ly/02-tai-sao-concept-first]].

Mỗi concept page lưu:
- Định nghĩa
- Cấu trúc lõi
- Ví dụ thực tế
- Khoá / source nào dạy
- Concept liên quan (cha/con/đi cặp/đối lập/tiền đề/kế thừa)
- Câu hỏi mở

---

## Template đầy đủ

```markdown
---
type: concept
tags: [framework, course/<code1>, course/<code2>, <theme-tags>, signature]
created: 2026-05-29
updated: 2026-05-29
sources: ["[[Source A]]", "[[Source B]]"]
---

# Tên concept

[Tóm tắt 2-3 câu — what + why + vai trò trong hệ sinh thái lớn]

## Thông tin module

| Trường | Giá trị |
|---|---|
| Tầm quan trọng | ⭐⭐⭐⭐⭐ (1-5/5) |
| Độ khó | ⭐⭐ (1-5/5) |
| Độ phổ biến | ⭐⭐⭐⭐ (1-5/5 — số lần dạy) |
| Khoá áp dụng | <CODE1>, <CODE2>, ... |
| Module liên quan | [[Concept X]], [[Concept Y]] (top 3-5) |
| Từ khoá | keyword1, keyword2, ... |

[Tuỳ chọn: trích câu signature]

## Định nghĩa

[1-2 đoạn — định nghĩa rõ ràng, không vòng vo]

## Cấu trúc lõi

[Các thành phần / công thức / quy trình áp dụng]

## Ví dụ thực tế

[Case cụ thể minh hoạ — từ source đã ingest]

## Ẩn dụ dễ nhớ

[Metaphor giúp dễ nhớ. Nếu chưa có → stub: *(stub — chưa có metaphor explicit trong source)*]

## Sai lầm phổ biến

5 anti-pattern + cách sửa:
1. **Sai lầm 1**: ...
   → Hậu quả: ...
   → Cách sửa: ...
2. **Sai lầm 2**: ...

## Khoá học sử dụng

- [[Course A]] — vai trò trong khoá (1 dòng)
- [[Course B]] — ...

## Phiên bản dạy concept

- **Lần đầu**: [[Source page]] (~MM/YYYY)
- **Hệ thống hoá**: [[Source page]] (đợt N)
- **Update lớn**: [[Source page]] (đợt M) — thêm gì mới

## Khái niệm liên quan

- **cha** [[Mother concept]] — concept rộng hơn chứa concept này
- **con** [[Sub concept]] — concept hẹp hơn nằm trong concept này
- **đi cặp** [[Sister concept]] — paired
- **đối lập** [[Opposite concept]] — opposite
- **tiền đề** [[Prerequisite concept]] — phải hiểu trước
- **kế thừa** [[Successor concept]] — phải hiểu sau

Mỗi item: `- **<nhãn>** [[Concept X]] — vai trò 1 dòng`

## Nguồn gốc & trích dẫn

[Tham chiếu external nếu có: tác giả/sách/khoá. Phân biệt phần custom vs phần theo source. Stub nếu không: *(stub — concept gốc tự research)*]

## Câu hỏi mở

- Gap cần verify 1
- Gap cần verify 2
```

---

## Giải thích từng section

### Frontmatter

```yaml
---
type: concept                                  # bắt buộc — Dataview query
tags: [framework, course/sss, signature]      # bắt buộc — graph color
created: 2026-05-29                            # bắt buộc
updated: 2026-05-29                            # bắt buộc — track stale
sources: ["[[Source A]]"]                      # bắt buộc — provenance
---
```

Quy tắc:
- `type` luôn là `concept`
- `tags` ít nhất 2: framework + course/<code>
- `sources` list mọi source đã verify concept

### Tiêu đề H1

Tiêu đề concept rõ ràng, ngắn. Có thể trùng tên file (Obsidian auto detect title từ filename).

### Tóm tắt 2-3 câu

What + Why + role:
- **What**: concept này là gì
- **Why**: tại sao quan trọng
- **Role**: vai trò trong hệ thống lớn

Vd:
> "Hệ thống bán hàng 8+2 là framework 8 bước quy trình bán hàng B2C cá nhân hoá kèm 2 nguyên tắc độc lập. Concept lõi của khoá SSS, dạy lần đầu BHTC 2012, hệ thống hoá SSS 10 (2020). Là baseline để mọi khoá bán hàng sau dạy lại hoặc mở rộng."

### Thông tin module (bảng)

Quick reference card. Người đọc lướt qua biết:
- Concept này quan trọng không (Tầm quan trọng)
- Khó học không (Độ khó)
- Tác giả dạy bao nhiêu lần (Độ phổ biến)
- Áp dụng khoá nào
- Module liên quan top 3-5

### Định nghĩa

1-2 đoạn rõ ràng. KHÔNG vòng vo.

### Cấu trúc lõi

Các thành phần cốt lõi. Có thể là:
- Bảng (vd: 8+2 = bảng 10 hàng)
- Bullet list
- Quy trình step-by-step
- Sơ đồ ASCII (nếu cần)

### Ví dụ thực tế

Case cụ thể minh hoạ concept hoạt động. Trích từ source.

Quy tắc:
- Cite source bằng `[[Source page]]`
- Số liệu phải có source
- Không bịa case

### Ẩn dụ dễ nhớ

Metaphor giúp người học nhớ. Vd:
- "3 trò chơi = 3 chân máy ảnh" (concept 3 trò chơi cuộc đời)
- "Plank 1000m" (concept kiên trì dài hạn)
- "Mario ăn nấm" (concept level-up bản thân)

Nếu chưa có metaphor → stub `*(stub — chưa có metaphor explicit trong source)*`. Đừng bịa.

### Sai lầm phổ biến

5 anti-pattern + cách sửa. Rút từ source nếu có; stub nếu không.

Format:
```
1. **Sai lầm**: Mô tả sai lầm cụ thể
   → Hậu quả: Người làm sai gặp vấn đề gì
   → Cách sửa: Action chỉnh sửa
```

### Khoá học sử dụng

**BẮT BUỘC** nếu concept dùng trong khoá đào tạo. Tách khỏi "Khái niệm liên quan".

Format:
```
- [[Course A]] — vai trò trong khoá (1 dòng)
- [[Course B]] — ...
```

Quy tắc 2 chiều: mỗi link concept → course phải có link ngược course → concept ở MOC. Lint sẽ check.

### Phiên bản dạy concept

(Nếu concept dạy nhiều version qua thời gian)

Liệt chỉ version signature:
- Lần đầu
- Hệ thống hoá
- Update lớn

Không cần liệt mọi phiên bản.

### Khái niệm liên quan (CÓ NHÃN)

6 nhãn semantic relationships:

| Nhãn | Ý nghĩa |
|---|---|
| **cha** | Concept rộng hơn chứa concept này |
| **con** | Concept hẹp hơn nằm trong concept này |
| **đi cặp** | Paired (đối nghịch hoặc đồng hành) |
| **đối lập** | Opposite |
| **tiền đề** | Phải hiểu trước |
| **kế thừa** | Phải hiểu sau |

Mỗi item:
```
- **<nhãn>** [[Concept X]] — vai trò 1 dòng
```

Tại sao có nhãn? Graph view dùng nhãn để render quan hệ đúng.

### Nguồn gốc & trích dẫn

External reference (Tony Robbins, Stephen Covey, sách...).

Quy tắc PTL: chỉ cite nếu PTL **nhớ rõ học từ ai**. KHÔNG cite pattern match.

Vd:
- Đúng: "PTL học khái niệm 'gán nghĩa' từ Tony Robbins (Awaken the Giant Within, 1991)"
- Sai: "Concept này tương tự cognitive reframing trong CBT" (chỉ match pattern, không phải nguồn gốc)

Stub nếu unknown: `*(stub — concept gốc tự research hoặc nguồn chưa verify)*`.

### Câu hỏi mở

Gap cần verify. Dạng bullet:

```
- Câu hỏi 1: ?
- Câu hỏi 2: ?
```

---

## Rating 3 chỉ số

### Tầm quan trọng (1-5)

| Score | Tiêu chí |
|---|---|
| 5/5 | Cross 5+ khoá hoặc là concept mẹ |
| 4/5 | Cross 3-4 khoá hoặc signature lớn |
| 3/5 | 2-3 khoá hoặc sub-concept quan trọng |
| 2/5 | 1 khoá hoặc concept hẹp |
| 1/5 | Stub hoặc obscure |

### Độ khó (1-5)

| Score | Tiêu chí |
|---|---|
| 5/5 | Cần 2+ khoá nền |
| 4/5 | Cần 1 khoá nền |
| 3/5 | Hiểu trong 1 buổi giảng |
| 2/5 | Hiểu trong 30 phút |
| 1/5 | Hiểu ngay |

### Độ phổ biến (1-5)

| Score | Tiêu chí |
|---|---|
| 5/5 | 10+ lần xuyên mọi khoá |
| 4/5 | 5-9 lần |
| 3/5 | 3-4 lần |
| 2/5 | 2 lần |
| 1/5 | 1 lần signature |

---

## Anti-pattern khi viết concept page

### Sai 1 — Gộp 2 concept vào 1 page

Thấy 2 concept dạy cặp đôi → muốn gộp. KHÔNG.

→ Tách. Áp dụng heuristic atomicity ở [[00-triet-ly/02-tai-sao-concept-first]].

### Sai 2 — Mô tả mơ hồ

"Khái niệm về tâm lý khách hàng". Đó là **topic**, không phải concept.

Concept phải:
- Có tên cụ thể (vd: "Bộ não thứ 2", "Hệ thống 8+2", "AIDA")
- Có cấu trúc xác định
- Áp dụng được

→ Topic chung → tạo `wiki/topics/` page riêng.

### Sai 3 — Cite source không cụ thể

"PTL dạy trong khoá SSS" — quá chung.

→ "PTL dạy trong SSS 21, Ngày 1, đoạn 14:30-16:00, line 1245-1320 transcript [[SSS 21 - Ngày 1 (28-11-2025)]]".

Cite có line ref → trace ngược dễ.

### Sai 4 — Khái niệm liên quan không nhãn

```
## Liên quan
- [[Concept A]]
- [[Concept B]]
```

→ Không biết quan hệ gì. Lint flag.

Đúng:
```
- **cha** [[Concept A]] — concept rộng hơn
- **đi cặp** [[Concept B]] — sister
```

---

## Test với Claude

Tạo concept page test:

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Trong prompt:
```
> Tạo concept page test cho "Pareto Principle" theo template, lưu vào wiki/concepts/. Frontmatter đầy đủ, các section đầy đủ. Stub những phần chưa có data.
```

Claude tạo file. Mở Obsidian xem → đúng template chưa.

---

## Tiếp theo

Đọc tiếp: [[05-source-page-template]] — Source page template chi tiết.
