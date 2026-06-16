---
title: Khi nào pivot architecture
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 05
---

# Khi nào pivot architecture

## Trước đó

[[03-migrate-rename-vault]] — bạn biết migrate.

---

## 4 mức can thiệp

Khi vault có vấn đề:

| Mức | Phạm vi | Cost | Risk |
|---|---|---|---|
| **1. Patch** | Fix 1-2 page | Phút | Thấp |
| **2. Refactor schema** | Update CLAUDE.md + apply | Giờ | Vừa |
| **3. Split / merge vault** | Tạo / gộp vault | Ngày | Cao |
| **4. Rebuild** | Đập đi xây lại từ raw | Tuần | Rất cao |

Quy tắc: leo thang chỉ khi mức dưới không work.

---

## Mức 1 — Patch

Vd: 3 wikilink broken sau khi rename file.

→ Fix wikilink trong Obsidian (Cmd+P → Refactor file).

Hoặc: 2 frontmatter sai.

→ Edit từng file, fix.

**Khi nào**: < 10 file affected, vấn đề isolated.

---

## Mức 2 — Refactor schema

Vd: bạn thấy mọi concept page cần section mới "Ứng dụng thực tế" — không có trong template hiện tại.

### Quy trình refactor

1. Update CLAUDE.md template — thêm section
2. Update `99-templates/concept-page-template.md` — thêm section
3. Bulk apply: dùng Claude duyệt mọi concept page → thêm section (stub nếu chưa có data)

Vd:

```
> Update mọi concept page trong wiki/concepts/ để có section "## Ứng dụng thực tế" trước section "## Khoá học sử dụng". Stub nội dung nếu chưa có data.
```

Claude apply 100+ concept page batch.

**Khi nào**: < 200 page affected, schema change là incremental.

---

## Mức 3 — Split / merge vault

Vd: Brain 1500 page, 60% là lifestyle (cá koi, xe). → Split Life.

Quy trình ở [[03-migrate-rename-vault]] use case C.

**Khi nào**:
- Domain emerge rõ rệt > 30% vault
- Workflow vault khác rõ rệt
- Privacy / scale đòi tách

**Risk**:
- Wikilink broken massive (vài trăm)
- Có thể bỏ sót page liên quan
- 2-3 ngày downtime

---

## Mức 4 — Rebuild

Vd: vault 3000 page, schema vỡ nát qua 2 năm, mọi page format khác nhau, không thể refactor incremental.

→ Đập đi xây lại từ raw/.

### Quy trình rebuild

1. **Backup** vault cũ (Git, external SSD)
2. **Tạo vault mới** với CLAUDE.md schema clean
3. **Re-ingest** từ raw/ với agent mới
4. **Migrate** select concept page valuable từ vault cũ (manual)
5. **Verify** vault mới có đủ content
6. **Archive** vault cũ sau 6 tháng (không xoá ngay)

### Khi nào rebuild

Rebuild chỉ khi:

- [ ] Refactor schema (mức 2) đã thử nhưng fail
- [ ] > 50% page có lỗi schema
- [ ] Wikilink broken > 30%
- [ ] CLAUDE.md không còn match thực tế
- [ ] Agent / skill không chạy được do schema cũ

**Cost**: 1-4 tuần. Risk cao mất nội dung quý.

---

## 5 dấu hiệu vault cần pivot

### Dấu hiệu 1 — Search trả về kết quả lẫn nhau

Search "training" → trả 100 page mix triathlon + sales training + ML training. Khó tách.

→ Pivot: tách domain. Split vault hoặc add namespace tag.

### Dấu hiệu 2 — Mỗi session Claude "set up context" lâu

Trước khi Claude làm gì, phải đọc CLAUDE.md + index.md + 5-10 concept page → 50% session là setup.

→ Pivot: thu gọn CLAUDE.md. Tách agent có context riêng cho task lặp.

### Dấu hiệu 3 — Graph view rối như mạng nhện

> 1000 node, edge dense không thấy pattern.

→ Pivot:
- Color groups → cluster theo tag
- Filter `path:wiki` exclude raw
- Tách vault nếu thấy 2-3 cluster độc lập

### Dấu hiệu 4 — Concept duplicate nhiều

Concept page "Bộ não thứ 2" có 3 phiên bản:
- `wiki/concepts/Bộ não thứ 2.md` (cũ)
- `wiki/concepts/Bo-nao-thu-2-v2.md` (mới hơn)
- `wiki/topics/Building-Second-Brain.md` (style khác)

→ Pivot: consolidate. Chọn 1 canonical, link 2 cái khác về.

### Dấu hiệu 5 — Bạn không dùng vault

Vault sống nhưng bạn không query, không ingest source mới 1 tháng+ → schema không serve nhu cầu.

→ Pivot:
- Hỏi tại sao không dùng (workflow rối? Content không relevant?)
- Simplify schema
- Hoặc archive vault, build cái mới mục đích rõ hơn

---

## Khi pivot có thể GIẢI quyết — và khi không

Pivot KHÔNG cứu nếu vấn đề là:

- **Bạn không biết mình muốn gì với vault** → pivot không giúp. Cần clarify goal trước.
- **Content không quality** → schema clean không cứu được content rác.
- **Bạn không có thời gian maintain** → pivot xong vẫn không update → vault chết.

Pivot CỨU được nếu:

- **Schema mismatch nhu cầu** → refactor schema
- **Tổ chức folder vỡ** → reorganize
- **Domain emerge → cần tách** → split vault
- **Vault scale lớn → cần meta layer** → tạo 4DX

---

## Quy tắc khi pivot

### Rule 1 — Đo trước khi pivot

Đếm:
- Số page total
- Số page valid (frontmatter đầy đủ)
- Số wikilink broken
- Số orphan
- Số concept duplicate

Pivot dựa con số, không cảm tính.

### Rule 2 — Patch trước, refactor sau, rebuild cuối

Đừng nhảy thẳng rebuild khi patch + refactor chưa thử.

### Rule 3 — Backup mọi lần

Trước pivot mức 2+ → backup. Always.

### Rule 4 — Test với subset trước

Refactor 200 page → test với 5 page trước. Verify Claude apply đúng schema mới → apply full.

### Rule 5 — Document quyết định

Append vào `log.md`:

```markdown
## [2026-05-29] pivot | Schema refactor — thêm section "Ứng dụng thực tế"

**Why**: 60% concept page user feedback "thiếu actionable insight". 
**What**: Update template + apply 230 concept page.
**Outcome**: ?

(Update outcome sau khi pivot xong)
```

→ 6 tháng sau review log → biết pivot có work không.

---

## Anti-pattern khi pivot

### Anti-pattern 1 — Pivot quá thường xuyên

Mỗi tháng đổi schema → vault không stable. AI confuse. User confuse.

→ Schema drift nhẹ OK. Major change tối đa 1-2 lần/năm.

### Anti-pattern 2 — Pivot mà không có goal

Bạn pivot vì "hứng mới"? KHÔNG. Pivot phải solve problem cụ thể.

### Anti-pattern 3 — Pivot architecture mà chưa fix content

Vault có 200 page rác → pivot architecture không cứu. Fix content trước.

### Anti-pattern 4 — Pivot solo, không hỏi AI

Pivot là quyết định lớn. Hỏi AI:

```
> Tôi đang nghĩ tách Life ra Brain. Đánh giá: vault Brain hiện có bao nhiêu page lifestyle? Có lý do giữ chung không?
```

AI có thể flag insight bạn miss.

### Anti-pattern 5 — Pivot không rollback plan

Pivot fail → mất data. Mọi pivot phải có rollback (Git revert, restore backup).

---

## Khi không pivot

Tránh pivot nếu:

- Vault < 200 page (chưa đủ data)
- Chưa try refactor mức 2
- Không rõ goal pivot
- Đang busy launch, deadline → không có thời gian fix bug
- Lint vừa pass clean → vault healthy

---

## Workflow pivot architecture

```
1. Đo lường vault (lint + count)
   ↓
2. Identify root cause (schema? Content? Workflow?)
   ↓
3. Decide mức can thiệp (1/2/3/4)
   ↓
4. Backup
   ↓
5. Plan + document trong log
   ↓
6. Test với subset
   ↓
7. Apply
   ↓
8. Verify (lint + manual check)
   ↓
9. Document outcome trong log
   ↓
10. Review 1-3 tháng sau → pivot work không?
```

---

## Verify Phần 05 xong

Sau Phần 05:
- [x] Hiểu lint định kỳ
- [x] Có Git backup
- [x] Biết migrate / rename
- [x] Biết khi nào pivot architecture

→ Bạn đã hoàn tất giáo trình. Vault Brain + sibling chạy ổn định, có backup, có quy trình maintain.

---

## Tiếp theo

Sang Phần 99 templates copy-paste. Bạn có thể skip nếu chỉ cần knowledge, hoặc vào template lấy nhanh.

Đọc tiếp: [[99-templates/claude-md-master-template]] — CLAUDE.md template generic.
