# Template — persona-<brand>-<slug>.md

Đây là template **copy-paste**. Mỗi `{{...}}` cần thay bằng nội dung phiên. Mỗi `[ ]` là 1 item — số lượng tối thiểu nêu rõ trong từng section.

```markdown
---
title: "Persona — {{brand-upper}}: {{mô-tả-phân-khúc-ngắn}}"
type: entity
entity_kind: persona
brand: {{brand-code-lowercase}}
pillar: "[[{{pillar-slug}}]]"
audience_type: {{B2C | B2B | marketplace}}
brain_ref:
  program_code: {{brand-code}}
  course_page: "[[../Longpt's Brain/wiki/courses/{{Course full title}}]]"
serves_assets:
  - "[[{{asset-slug-1}}]]"
  - "[[{{asset-slug-2}}]]"
status: {{draft | hypothesis | validated}}
validated_by_roles: []  # ["thám-tử", "phóng-viên", "nhân-chủng-học", "đóng-giả", "cùng-sáng-tạo", "khoa-học"]
last_validated: null  # YYYY-MM-DD khi status=validated
sample_size: null  # số mẫu phỏng vấn / dữ liệu A/B test
extraction_sources: []  # ["[[src-extraction-<brand>-youtube-comments-YYYYMMDD]]", ...] — link đến source extraction files
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
tags: [persona, brand/{{brand-code}}, {{pillar-slug}}, {{audience_type-lower}}]
---

# Persona — {{tiêu đề đầy đủ}}

> {{Câu mô tả phân khúc 1 dòng — quote, italic}}

## 1. Phân khúc (1 câu)

Người **{{loại}}** đang ở **{{bối cảnh}}** muốn **{{Job cốt lõi}}**.

**Kích cỡ thị trường ước lượng (TAM tại Việt Nam)**: {{số ước lượng + nguồn}}

**Lý do chọn phân khúc này** (vs các phân khúc khác mà khóa có thể phục vụ):
- {{lý do 1}}
- {{lý do 2}}

## 2. Bối cảnh (5W1H)

| Trục | Mô tả |
|---|---|
| **When** — khoảnh khắc đời họ | {{...}} |
| **Where** — nơi/kênh gặp PTL | {{...}} |
| **Who** — ai cùng quyết định | {{...}} |
| **What** — đã thử gì khác | {{...}} |
| **Why** — vì sao hành động bây giờ | {{...}} |
| **How** — ràng buộc | {{...}} |

## 3. Việc cần làm (Jobs) — ưu tiên cao trên cùng

Cú pháp: `[ ] <Job> — ref: [r001, r017] {tần suất}` — đính ref về source extraction (nếu Mode B) hoặc `[Mode A]` nếu suy từ trí nhớ.

### Chức năng (Functional — đo được)
- [ ] {{job 1 — định lượng nếu được}} — ref: [{{r###}}] {{count}}
- [ ] {{job 2}} — ref: [{{r###}}]
- [ ] {{job 3}} — ref: [Mode A]

### Xã hội (Social — cách được nhìn nhận)
- [ ] {{job 4}} — ref: [{{r###}}]
- [ ] {{job 5}} — ref: [{{r###}}]

### Cảm xúc (Emotional — trạng thái nội tâm)
- [ ] {{job 6}} — ref: [{{r###}}]
- [ ] {{job 7}} — ref: [{{r###}}]

### Hỗ trợ (Supporting — vòng đời 3 vai trò)
- [ ] **Người mua giá trị**: {{job 8 — so sánh / quyết / thanh toán}} — ref: [{{r###}}]
- [ ] **Người cùng tạo giá trị**: {{job 9 — review / phản hồi / tham gia thiết kế}} — ref: [{{r###}}]
- [ ] **Người chuyển giao giá trị**: {{job 10 — giới thiệu / nhượng / cộng đồng cũ}} — ref: [{{r###}}]

> Tối thiểu **8 Jobs**, đủ 4 loại. Mỗi job 1 dòng, ngắn gọn, có ref về quote gốc nếu lấy từ raw.

## 4. Nỗi đau (Pains) — ưu tiên cao trên cùng

Cú pháp: `[ ] <Pain> — ref: [r###] {count}` — pain có ref thật mạnh hơn pain Mode A.

### Kết quả không mong muốn (Undesired Outcomes)
- [ ] {{pain 1 — định lượng nếu được, vd "đã thử 3 khóa khởi nghiệp khác, không khóa nào ra sản phẩm bán được"}} — ref: [{{r###}}] {{count}}
- [ ] {{pain 2 — emotional/social, vd "xấu hổ khi vợ kiếm nhiều hơn"}} — ref: [{{r###}}]

### Rào cản (Obstacles / Blockers)
- [ ] {{pain 3 — vd "ngân sách học cả năm 20tr, phải cân nhắc 1 flagship hoặc 2-3 nhỏ"}} — ref: [{{r###}}]
- [ ] {{pain 4 — thời gian / địa lý / kiến thức / chưa được phê duyệt}} — ref: [{{r###}}]

### Rủi ro (Risks)
- [ ] {{pain 5 — vd "bỏ tiền học rồi không áp dụng được vào lĩnh vực mình"}} — ref: [{{r###}}]
- [ ] {{pain 6 — financial / career / social risk}} — ref: [{{r###}}]

> Tối thiểu **6 Pains**, đủ 3 loại, ≥ 1 pain cảm xúc/xã hội.
> **Cấm**: viết pain = "không có" gain (vd "không có hệ thống bán hàng"). Thay bằng pain cụ thể.

## 5. Lợi ích (Gains) — 4 mức

Cú pháp: `[ ] <Gain> — ref: [r###] {count}`. Mức Bất ngờ khách hiếm khi tự nói — chấp nhận [Mode A] cho mức này.

### Thiết yếu (Required — phải có)
- [ ] {{gain 1}} — ref: [{{r###}}]
- [ ] {{gain 2}} — ref: [{{r###}}]

### Kỳ vọng (Expected — mặc nhiên)
- [ ] {{gain 3}} — ref: [{{r###}}]
- [ ] {{gain 4}} — ref: [{{r###}}]

### Khao khát (Desired — sẽ nói nếu hỏi)
- [ ] {{gain 5 — vd "được anh Long mentor 1-1"}} — ref: [{{r###}}]
- [ ] {{gain 6}} — ref: [{{r###}}]

### Bất ngờ (Unexpected — không nghĩ ra trước) ⭐ vũ khí cạnh tranh
- [ ] {{gain 7 — vd "AI Long Bot trả lời 24/7 theo phong cách anh Long"}} — ref: [Mode A]
- [ ] {{gain 8 — vd "tour offline gặp 5 học viên thành công 5 năm trước"}} — ref: [Mode A]

> Tối thiểu **6 Gains**, đủ 4 mức, ≥ 2 Bất ngờ.

## 6. Vai trò (chỉ B2B / marketplace) — xóa section này nếu B2C

| Vai trò | Người | Jobs khác biệt | Pain khác biệt | Gain khác biệt |
|---|---|---|---|---|
| **Người ảnh hưởng** | {{vd: TGĐ / cố vấn / BNI mentor}} | | | |
| **Người mua** | {{vd: phòng mua hàng}} | | | |
| **Người dùng** | {{vd: nhân viên sales}} | | | |
| **Người phê duyệt** | {{vd: CEO}} | | | |
| **Người chi trả** | {{vd: phòng kế toán / CFO}} | | | |

## 7. Bằng chứng đã thu thập

| Vai trò nghiên cứu | Ngày | Nguồn / Mẫu (N) | Insight chính | Source file |
|---|---|---|---|---|
| Thám tử Dữ kiện | {{ngày}} | {{vd: 250 comment YouTube DTSGC top — N=250}} | {{...}} | [[src-extraction-dtsgc-youtube-YYYYMMDD]] |
| Phóng viên | {{ngày}} | {{vd: 8 phỏng vấn buyer + 3 canceled — N=11}} | {{...}} | [[src-extraction-dtsgc-phongvan-YYYYMMDD]] |
| Nhà Nhân chủng học | | | | |
| Người Đóng giả | | | | |
| Người Cùng sáng tạo | | | | |
| Nhà khoa học | | | | |

**Tổng N (sample_size)**: {{số tổng}}
**Source extraction files đầy đủ**: liệt kê trong frontmatter `extraction_sources`.

## 8. Quote nguyên văn từ khách (gold)

Tối thiểu 5 quote — 1 cho mỗi mức Pain + 1 cho Gain Khao khát + 1 cho Gain Bất ngờ. Giữ nguyên ngôn ngữ khách (không sửa chính tả, không đẹp hóa).

> "{{quote 1 — minh họa Pain Outcome}}" — *{{ẩn danh / tên (xin phép) — ngày — nguồn}}* [ref: r###]

> "{{quote 2 — minh họa Pain Obstacle}}" — *...* [ref: r###]

> "{{quote 3 — minh họa Pain Risk}}" — *...* [ref: r###]

> "{{quote 4 — minh họa Gain Khao khát}}" — *...* [ref: r###]

> "{{quote 5 — minh họa Gain Bất ngờ (từ buyer đã trải nghiệm)}}" — *...* [ref: r###]

## 9. Liên kết

- **Asset đang phục vụ**: {{liệt kê các lead-page / event / content / ad đã gắn `target_persona` về persona này}}
- **Pillar**: [[{{pillar-slug}}]]
- **Brand**: brand/{{brand-code}}
- **Brain course**: [[../Longpt's Brain/wiki/courses/{{Course full title}}]]
- **Quy trình gốc**: [[quy-trinh-xay-dung-ho-so-khach-hang]]
- **Persona song hành** (cùng khóa, phân khúc khác): {{liệt kê nếu có}}

## 10. Lịch sử

| Ngày | Action | Ghi chú |
|---|---|---|
| {{YYYY-MM-DD}} | created | Phiên `ho-so-khach-hang-vpc` đầu tiên |
```
