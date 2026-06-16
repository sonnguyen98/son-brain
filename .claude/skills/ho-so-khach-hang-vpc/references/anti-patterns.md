# Anti-patterns — 7 sai lầm PTL hay vấp khi xây Hồ sơ Khách hàng

Đọc file này MỖI khi bắt đầu phiên `ho-so-khach-hang-vpc` để tránh các bẫy lặp lại.

## 1. "Khách của tôi là tất cả chủ doanh nghiệp Việt Nam"

**Vì sao sai**: Câu này thường có nghĩa là *chưa thực sự hiểu ai cả*. Hệ quả: giải pháp lờ mờ, thông điệp không cắn vào ai.

**Cách sửa**: Bắt buộc thu hẹp đến 1 câu cụ thể theo công thức:
> *Người [loại cụ thể] đang ở [bối cảnh cụ thể] muốn [Job cốt lõi cụ thể]*

Ví dụ tốt:
- *"Chủ shop online doanh thu 50-500tr/tháng, có 1-3 nhân viên, đang muốn x2 doanh thu mà không phải tự đứng livestream mỗi tối"*
- *"Người đi làm 30-45 tuổi tại Hà Nội/TP.HCM, đã tích 300-700tr vốn, muốn khởi nghiệp nhưng đang sợ mất vốn dưỡng già"*

Ví dụ xấu:
- *"Chủ doanh nghiệp Việt Nam"*
- *"Người muốn thành công"*
- *"Anh em doanh nhân"*

## 2. Phân khúc theo nhân khẩu học (demographic) mà bỏ qua Jobs

**Vì sao sai**: "Phụ nữ 25-35, thu nhập 20-30tr, sống TP.HCM" không cho biết họ đang *cố làm gì*. Hai phụ nữ cùng nhân khẩu học có thể có Jobs hoàn toàn khác:
- Một người mua DTSGC để khởi nghiệp thoát cảnh làm thuê
- Một người mua LTVM để chữa lành sang chấn từ ly hôn

→ Hai phân khúc, hai hồ sơ khác nhau, không thể gộp.

**Cách sửa**: Đặt câu hỏi gốc *"Khách hàng đang cố làm gì?"* trước câu *"Khách hàng là ai?"*. Demographic chỉ dùng để **mô tả** phân khúc sau khi đã phân khúc theo Jobs — không phải để **định nghĩa** phân khúc.

## 3. Gộp 2 phân khúc khác Jobs vào 1 hồ sơ

**Vì sao sai**: Sẽ ra "giải pháp trung bình" — vừa thừa với phân khúc nhỏ, vừa thiếu với phân khúc lớn. Ví dụ kinh điển: gộp "cá nhân tự học IPS" và "doanh nghiệp mua IPS Coach" vào 1 hồ sơ → sale page chung chung không đánh trúng ai.

**Cách sửa**:
- B2C nhiều phân khúc → mỗi phân khúc 1 file `persona-*.md` riêng.
- B2B nhiều vai trò DMU → MỘT file persona cho B2B với 5 vai trò trong section 6 (Người ảnh hưởng / mua / dùng / phê duyệt / chi trả), KHÔNG tách 5 file.
- Marketplace (Grab, Airbnb mô hình) → mỗi mặt 1 file (vd `persona-grab-tai-xe.md`, `persona-grab-khach.md`, `persona-grab-nha-hang.md`).

## 4. Bỏ qua người *đã hủy đăng ký* (status 6 Pancake)

**Vì sao sai**: Pain mạnh nhất thường nằm ở những người ĐÃ đăng ký rồi hủy — họ đã tiến gần đến quyết định nhưng có cái gì đó cản. Phỏng vấn họ cho insight gold nhất.

**Cách sửa**: Mỗi quarter rút mẫu 20 ca canceled từ Pancake (status=6), phỏng vấn lý do cụ thể bằng cách nhẹ nhàng — "anh/chị từng đăng ký nhưng chưa tham gia được, em muốn hiểu lý do để cải thiện."

## 5. Pain = "không có" Gain (đối lập)

**Vì sao sai**: Nếu Job là "kiếm nhiều tiền hơn", đừng ghi Pain = "giảm lương" và Gain = "tăng lương". Cách này lười và không cho insight nào.

**Cách sửa**: Tách 2 trục độc lập:

| Pain (đúng) | Gain (đúng) |
|---|---|
| Đã thử 3 lần xây quy trình nhân viên bỏ giữa chừng | Có khung mẫu sẵn copy-paste vào doanh nghiệp mình trong 1 tuần |
| Tự xây hệ thống thì sợ tốn thêm 3-6 tháng test sai | Học viên cũ làm reference live, không phải nghe trên slide |
| Không biết đo lường ROI hệ thống bán hàng | Dashboard mẫu kèm KPI tham chiếu sẵn |

Trong **Pain** ưu tiên thêm **rào cản** ("không có ngân sách 50tr/khóa flagship") và **rủi ro** ("bỏ tiền học rồi không áp dụng được vào lĩnh vực mình"). Đây là 2 loại pain bị bỏ qua nhiều nhất.

## 6. Bỏ qua mức Lợi ích Bất ngờ

**Vì sao sai**: Hồ sơ chỉ liệt kê Gain thiết yếu + kỳ vọng = "đáp ứng kỳ vọng" — không tạo khác biệt cạnh tranh. Đối thủ (Trần Việt Quân, Lan Bercu, các coach 1-1) cũng làm vậy → giá đua đáy.

**Cách sửa**: Bắt buộc ≥ 2 Gain Bất ngờ trong mỗi hồ sơ. PTL có sẵn nhiều "vũ khí":

| Loại Gain Bất ngờ | Ví dụ PTL có sẵn |
|---|---|
| Cộng đồng học viên cũ | Group VIP DTSGC 73 đợt → 74 đợt → 75 đợt connect liên tục |
| AI trợ lý theo phong cách Long | AI Long Bot trả lời 24/7 sau khi học |
| Mentor cấp đầu trực tiếp | Anh Long mentor 1-1 cho top 10% học viên SSS |
| Chứng nhận xã hội | Chứng chỉ học viên Kim Cương, ảnh treo văn phòng |
| Reference live | Học viên thành công 5 năm trước xuất hiện reference trong buổi học |
| Tour offline | Đi thăm doanh nghiệp học viên thành công cũ |
| Ngân hàng nội dung | 30 video signature PTL miễn phí tái sử dụng cho kênh học viên |

→ Liệt 2-4 món vào mục "Bất ngờ" cho mỗi hồ sơ.

## 7. Hồ sơ tĩnh > 6 tháng không refresh

**Vì sao sai**: Bối cảnh khách hàng Việt Nam thay đổi nhanh:
- 2023: hậu COVID, hậu sa thải hàng loạt tech → pain "mất việc"
- 2024-2025: làn sóng AI thay thế → pain "bị AI thay thế, tụt hậu công nghệ"
- 2026: Gen Z lên ngôi quản lý → pain "không biết quản lý nhân viên Gen Z"

Hồ sơ viết 2024 nếu dùng 2026 sẽ nhắm sai pain → CVR drop.

**Cách sửa**:
- Đặt `last_validated` trong frontmatter.
- Lint vault mỗi quý — flag persona `last_validated < (today - 6 tháng)` → status đổi sang `stale`.
- Refresh persona stale trước khi launch đợt khóa mới.

## Quy trình kiểm anti-pattern trong phiên

Sau mỗi bước (1, 3, 4, 5), trước khi qua bước tiếp theo, đọc 1 lần qua 7 anti-pattern này và self-check:

- [ ] Câu phân khúc đã đủ hẹp? (chống AP#1)
- [ ] Có dựa vào Jobs hay chỉ demographic? (chống AP#2)
- [ ] Có gộp 2 Jobs khác nhau không? (chống AP#3)
- [ ] Đã có pain của người canceled chưa? (chống AP#4)
- [ ] Pain có khác Gain không phải đối lập? (chống AP#5)
- [ ] Đã có ≥ 2 Gain Bất ngờ? (chống AP#6)
- [ ] `updated` mới? (chống AP#7)

Nếu fail bất kỳ → quay lại sửa, KHÔNG xuất file.
