---
title: Query wiki đầu tiên
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 02
---

# Query wiki đầu tiên

## Trước đó

[[07-ingest-source-dau-tien]] — bạn đã ingest 3-4 source, vault có data ban đầu.

---

## Mục tiêu

Trải nghiệm sức mạnh thật sự của AI-first wiki: **hỏi 1 câu, Claude tổng hợp từ wiki, trả lời cite source**.

Không phải Claude scan lại raw mỗi lần. Claude đọc concept page → tổng hợp → trả lời.

---

## Bước 1 — Khởi động Claude trong vault

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

---

## Bước 2 — Query 1 — Đơn giản

```
> Concept "Product Market Fit" là gì? Trả lời ngắn, cite source.
```

Claude:
1. Đọc `index.md` tìm page "Product Market Fit"
2. Đọc `wiki/concepts/Product Market Fit.md`
3. Tổng hợp định nghĩa
4. Cite `[[Paul Graham — Product Market Fit (2024)]]`

Trả lời mẫu:

```
Theo wiki:

Product Market Fit (PMF) là tình trạng sản phẩm đáp ứng nhu cầu thị trường đủ mạnh để tăng trưởng tự nhiên — không phải state, mà là process.

PG đặc trưng PMF qua 3 dấu hiệu:
1. User retention cao bất thường
2. Tự nhiên có viral
3. Sales cycle ngắn lại

Source: [[Paul Graham — Product Market Fit (2024)]]
```

---

## Bước 3 — Query 2 — Tổng hợp xuyên source

```
> Tổng hợp các insight về PMF từ tất cả source đã ingest. Format bảng.
```

Claude:
1. Tìm concept page "Product Market Fit"
2. Đọc section "Phiên bản dạy concept" → list các source đã touch
3. Đọc từng source page liên quan
4. Pivot bảng

Trả lời mẫu:

```markdown
| Source | Year | Insight chính | Quote |
|---|---|---|---|
| [[Paul Graham — Product Market Fit (2024)]] | 2024 | PMF là process, không state | "PMF is not a destination" |
| [[Sam Altman — Startup Playbook]] | 2022 | PMF = user retention curve flatten | "If retention curve is flat, you have PMF" |
| [[Marc Andreessen — Original PMF Essay]] | 2007 | First mention thuật ngữ, định nghĩa nguyên bản | "the only thing that matters" |

Insight tổng hợp:
- 3 tác giả đồng ý: PMF không phải feature, mà là user behavior
- Khác biệt: PG nhấn process, Sam nhấn retention curve, Marc nhấn priority
- Gap: chưa có ai đưa metric cụ thể (% retention day 30, day 90...)
```

---

## Bước 4 — Query 3 — So sánh

```
> So sánh Paul Graham vs Marc Andreessen về PMF. Họ khác nhau chỗ nào?
```

Claude:
1. Tìm 2 entity page: Paul Graham, Marc Andreessen
2. Tìm concept page liên quan
3. Pivot so sánh

Đây là việc cần concept-first. Nếu source-first → Claude scan 100% raw mỗi entity → chậm.

---

## Bước 5 — Query 4 — Hỏi gap

```
> Khái niệm nào trong wiki bị thiếu source? Liệt 5 concept stub.
```

Claude:
1. Đọc `wiki/concepts/` (Glob hoặc list)
2. Check frontmatter `sources` — nếu rỗng/sparse → stub
3. Liệt 5 concept stub

Trả lời mẫu:

```
5 concept page stub (sources < 2):
1. [[Founder Mode]] — chỉ 1 source mention, chưa có dedicated source
2. [[Lean Startup]] — nhắc nhiều nhưng chưa ingest sách
3. [[Burn Rate]] — định nghĩa stub, chưa case
4. [[Pivot]] — 1 source, cần thêm
5. [[Term Sheet]] — concept legal, chưa ingest source

Đề xuất ingest tiếp:
- Sách "Lean Startup" của Eric Ries (PDF)
- Bài Paul Graham "Founder Mode" (2024-09)
```

---

## Bước 6 — Query 5 — Action insight

```
> Nếu tôi muốn validate PMF cho startup tôi (B2B SaaS, 10 paying customer), tôi nên làm gì? Dựa wiki.
```

Claude:
1. Đọc concept "Product Market Fit"
2. Đọc concept liên quan ("Retention curve", "User interview", "Cohort analysis")
3. Suy luận actionable cho B2B SaaS 10 paying

Trả lời mẫu:

```
Dựa wiki + tình huống bạn (B2B SaaS, 10 paying), 5 hành động:

1. **Tính retention curve** (theo [[Sam Altman — Startup Playbook]]):
   - Đo % của 10 customer còn dùng sau 30/60/90 ngày
   - Nếu curve flatten ≥60% sau ngày 30 → có signal PMF early
   - Nếu curve dốc xuống → chưa PMF

2. **User interview định kỳ** (theo [[Lean Startup]] - stub):
   - 10 phỏng vấn / quarter
   - Hỏi: "Nếu mai tôi tắt sản phẩm, bạn buồn cỡ nào?" (PMF signal classic)
   - ≥40% buồn rất nhiều → PMF signal

3. **Trace word of mouth**:
   - 10 customer đến từ đâu? Trực tiếp / referral / paid?
   - Tỷ lệ referral cao → PMF signal

4. **NPS score**:
   - >40 → có PMF
   - <0 → chưa

5. **Sales cycle length**:
   - Giảm dần qua quý → PMF signal (PG)
   - Tăng → chưa

Gap: wiki chưa có concept "[[NPS Score]]". Có muốn em ingest 1 source về NPS?
```

---

## Bước 7 — Lưu query thành analysis page

Khi query trả lời hay, có giá trị giữ lại:

```
> Lưu câu trả lời vừa rồi thành wiki/analyses/Validate-PMF-cho-B2B-SaaS.md. 
> Frontmatter type: analysis, tags: [pmf, b2b, startup]. Update index.md.
```

Claude:
- Tạo file analysis
- Update index
- Append log

Lần sau hỏi lại câu tương tự → analysis page đã có, trả lời nhanh hơn.

---

## Bước 8 — Pattern query hữu ích

5 dạng query bạn nên thử với vault còn nhỏ:

### A. Định nghĩa

```
> X là gì?
```

→ Trả lời từ concept page.

### B. So sánh

```
> So sánh X vs Y
```

→ Tổng hợp xuyên 2 concept page.

### C. Map concept

```
> Concept nào liên quan đến X? Vẽ relationship.
```

→ Theo wikilink "Khái niệm liên quan".

### D. Gap analysis

```
> Wiki có lỗ hổng gì về chủ đề Z?
```

→ Concept stub, source thiếu.

### E. Action insight

```
> Tôi đang ở tình huống M, dựa wiki nên làm gì?
```

→ Apply concept vào case cụ thể.

---

## Bước 9 — Tránh query sai

### Sai 1 — Query mơ hồ

```
> Nói tôi nghe về vault
```

→ Claude không biết bạn hỏi gì. Cụ thể hoá:

```
> Liệt 5 concept quan trọng nhất trong vault (theo rating Tầm quan trọng ≥4)
```

### Sai 2 — Query yêu cầu Claude scan raw

```
> Đọc lại toàn bộ raw/articles/ và summarize
```

→ Phản pattern. Concept page đã có summary. Yêu cầu Claude đọc concept page thay:

```
> Tổng hợp concept page chủ đề startup
```

### Sai 3 — Query không cite

```
> Concept X là gì?
```

(Không yêu cầu cite)

→ Claude trả lời generic. Yêu cầu cite:

```
> Concept X là gì? Cite source page.
```

---

## Bước 10 — Workflow query tổng quát

```
1. Bạn hỏi câu hỏi
   ↓
2. Claude đọc index.md tìm page candidate
   ↓
3. Claude đọc concept page liên quan
   ↓
4. Theo wikilink "Khái niệm liên quan" → drill thêm context nếu cần
   ↓
5. Tổng hợp câu trả lời CITE source
   ↓
6. Đề xuất lưu thành analysis nếu giá trị
   ↓
7. Bạn duyệt — OK → lưu / sai → chỉ chỗ
```

---

## Verify Phần 02 hoàn tất

- [x] Vault Brain folder
- [x] CLAUDE.md schema
- [x] 3 template (concept, source, course)
- [x] 3-4 source ingest
- [x] 5 query test
- [x] 1 analysis page lưu

OK → vault Brain chạy được. Bạn có thể tiếp tục ingest source dần dần.

Sang Phần 03 multi-vault (khi sẵn sàng).

---

## Tiếp theo

Đọc tiếp: [[03-mo-rong-multi-vault/01-khi-nao-tach-vault]] — Khi nào tách vault sibling.
