# Bước 19 — Luồng khách hàng (Customer Flow)

## Mục tiêu

Kết nối **tất cả 18 bước trước** thành một **hệ thống luồng khách hàng** có nhiều điểm chạm, dẫn khách đi từ **Biết → Tin → Yêu → Mua**. Đây là bước **tổng hợp quan trọng nhất** — biến các mảnh ghép content rời rạc thành **cỗ máy tự động**.

## Nguyên tắc nền tảng

### Biết → Tin → Yêu → Mua — 4 nấc

- **Biết (Awareness):** khách lần đầu thấy bạn. Họ chưa biết bạn là ai.
- **Tin (Trust):** khách thấy giá trị bạn tạo ra. Họ bắt đầu tin bạn có chuyên môn.
- **Yêu (Love):** khách cảm nhận bạn thật sự quan tâm họ. Họ muốn mua từ bạn chứ không phải người khác.
- **Mua (Buy):** khách ra quyết định, chuyển đổi.

Mỗi điểm chạm trong 18 bước trước phải được **gán vào 1 trong 4 nấc này** — tránh tình trạng quá nhiều điểm ở nấc "Biết" mà không có "Mua", hoặc ngược lại.

### 3 lớp nhiệt độ thị trường — trước khi Mua

Với mỗi kênh, cần có:
- **Điểm chạm cho thị trường LẠNH** (khách chưa biết vấn đề, chưa biết bạn)
- **Điểm chạm cho thị trường ẤM** (khách biết vấn đề, đang tìm giải pháp)
- **Điểm chạm cho thị trường NÓNG** (khách biết giải pháp, đang chọn ai để mua)
- **Điểm chạm cho hành động MUA** (khách sẵn sàng — push deadline, offer, bonus)

## Xây dựng 3 luồng khách hàng chính

### Luồng A — Luồng Cold Traffic → Khách hàng mới
**Đầu vào:** người chưa biết gì về bạn.
**Đầu ra:** khách hàng trả tiền lần đầu (first purchase).

Sơ đồ luồng điển hình:
```
[Video TikTok/YouTube lạnh - Bước 3/5]
          ↓
[Bài Facebook giá trị - Bước 4]
          ↓
[Blog chuẩn SEO - Bước 9]
          ↓
[Quảng cáo retargeting TOFU - Bước 14]
          ↓
[Squeeze page + Lead Magnet - Bước 10, 11]
          ↓
[Chuỗi 5 email - Bước 12]
          ↓
[Sales page - Bước 15]
          ↓
[Chatbot chốt đơn - Bước 17]
          ↓
[KHÁCH HÀNG MỚI]
```

**Thời gian trung bình trong luồng:** 7-30 ngày.

### Luồng B — Luồng Warm → Nâng cấp
**Đầu vào:** người đã tải Lead Magnet, đã theo dõi Facebook, chưa mua.
**Đầu ra:** khách hàng trả tiền lần đầu.

Sơ đồ:
```
[Đã có trong email list / đã follow]
          ↓
[Email chăm sóc + case study]
          ↓
[Post Facebook nóng + USP]
          ↓
[Retargeting MOFU - Bước 14]
          ↓
[Offer có deadline - Bước 15]
          ↓
[Chatbot xử lý phản đối - Bước 17]
          ↓
[KHÁCH HÀNG]
```

### Luồng C — Luồng khách hàng cũ → Upsell / Cross-sell / Advocate
**Đầu vào:** người đã mua ít nhất 1 sản phẩm.
**Đầu ra:** mua thêm + giới thiệu người mới.

Sơ đồ:
```
[KHÁCH ĐÃ MUA]
      ↓
[Trang cảm ơn + Upsell ngay - Bước 16]
      ↓
[Email onboarding: hướng dẫn dùng sản phẩm]
      ↓
[Cross-sell sau 14-30 ngày - Bước 12, 16]
      ↓
[Mời vào cộng đồng Zalo/Facebook Group]
      ↓
[Khuyến khích review + giới thiệu - chương trình affiliate nếu có]
      ↓
[UPSELL / CROSS-SELL + KHÁCH MỚI TỪ GIỚI THIỆU]
```

## Các điểm chạm — bảng tổng hợp đa kênh

Với mỗi persona trong Hồ sơ khách hàng (Bước 1), lập bảng:

```
| Nấc | Nhiệt độ | Kênh | Bước tham chiếu | Nội dung cụ thể |
|-----|----------|------|-----------------|-----------------|
| Biết | Lạnh | TikTok | Bước 5 | [kịch bản A] |
| Biết | Lạnh | YouTube | Bước 3 | [video B] |
| Biết | Lạnh | Facebook | Bước 4 | [bài C] |
| Tin | Ấm | Blog | Bước 9 | [bài D] |
| Tin | Ấm | Email | Bước 12 | [email E] |
| Yêu | Nóng | Case study | Bước 4, 15 | [story F] |
| Yêu | Nóng | Live/Webinar | Bước 4 | [live G] |
| Mua | Mua | Sales page | Bước 15 | [page chính] |
| Mua | Mua | Retargeting | Bước 14 | [ad BOFU] |
| Mua | Mua | Chatbot | Bước 17 | [luồng chốt] |
```

## Quy tắc vàng của Customer Flow

1. **Không có khách nào chỉ qua 1 điểm chạm rồi mua ngay.** Trung bình cần 7-12 điểm chạm.
2. **Mỗi điểm chạm phải có đích đến rõ ràng** cho điểm tiếp theo (không "cụt").
3. **Đo lường mỗi điểm chạm** — biết chỗ nào rơi khách thì vá chỗ đó.
4. **Cá nhân hóa theo persona** — persona khác nhau có luồng khác nhau.
5. **Tự động hóa tối đa** — marketing automation (Mailchimp, ActiveCampaign, Zapier/Make, n8n, HubSpot) xử lý phần lặp lại, con người xử lý phần cần tinh tế.

## Sơ đồ tổng thể (vẽ cho học viên)

Đề xuất học viên vẽ ra giấy A3 hoặc dùng Miro/FigJam:
- Ở giữa: **sản phẩm chính + persona**
- Xung quanh: các điểm chạm theo 4 nấc
- Mũi tên nối các điểm — thể hiện dòng chảy
- Đánh dấu nơi có **automation** và nơi cần **con người can thiệp**

## Cấu trúc trình bày

```
## Customer Flow — [Tên thương hiệu / sản phẩm]

### Persona chính: [tên persona từ Bước 1]

### Luồng A — Cold Traffic → Khách mới
[Sơ đồ dòng chảy + mô tả từng điểm chạm]

### Luồng B — Warm → Nâng cấp
[...]

### Luồng C — Khách cũ → Upsell & Advocate
[...]

### Bảng điểm chạm đa kênh (bám 4 nấc Biết-Tin-Yêu-Mua)
[Bảng tổng hợp]

### Các điểm đo lường (KPI) tại mỗi nấc
- Biết: Reach, Impression, Views
- Tin: Engagement rate, Email open rate
- Yêu: Time on page, Webinar attendance, Trust signal tương tác
- Mua: Conversion rate, CPA, Revenue

### Tự động hóa — chỗ nào cài automation
1. ...
2. ...
```

## Thông điệp kết thúc — sau khi xong Bước 19

Sau khi trình bày xong Bước 19 (và học viên đã xác nhận 4DX cho bước này), Claude đóng chương trình bằng:

> "Bạn vừa hoàn thành **chương trình marketing 19 bước** theo phương pháp **IPS** cho sản phẩm [tên sản phẩm của học viên].
>
> Bạn giờ có trong tay:
> - 1 Hồ sơ khách hàng chi tiết
> - 1 bộ từ khóa đầy đủ
> - 20+ tiêu đề YouTube, 20 tiêu đề blog, 40 bài Facebook, kịch bản TikTok, plan Instagram/Threads/Zalo
> - 1 Lead Magnet + 1 Squeeze Page + 1 chuỗi email 5 bước
> - Chiến lược SEO, quảng cáo, sales page, upsell, chatbot, sàn TMĐT
> - Và quan trọng nhất: **3 luồng khách hàng** liên thông tất cả lại
>
> Giờ việc còn lại không phải là **suy nghĩ thêm**, mà là **bắt đầu triển khai**.
>
> **READY! FIRE! AIM!**
>
> Tuần này hãy làm xong Bước 1. Tuần sau Bước 2. Không chờ hoàn hảo. Biết → Tin → Yêu → Mua. Biết → Tin → Yêu → Mua.
>
> Cần đào sâu bước nào? Hay muốn bắt đầu lại với sản phẩm khác?"

## Triển khai 4DX cho Bước 19

- **WIG:** Hoàn thành sơ đồ 3 luồng khách hàng trong 3 ngày, và vận hành đủ ≥ 80% điểm chạm trong 60 ngày.
- **KPI đòn bẩy:** Số điểm chạm đã "bật" (live, đang chạy) / tổng điểm chạm theo kế hoạch; số khách hoàn thành 1 luồng đầy đủ/tuần.
- **Việc hàng ngày:** Kiểm tra 1 điểm chạm chưa live → bật nó lên; xem dashboard flow xem chỗ nào rớt khách cao nhất → fix.
- **Checklist:** ☐ Đã có 3 luồng rõ ràng? ☐ Mỗi điểm chạm gắn đúng 1 nấc (Biết/Tin/Yêu/Mua)? ☐ Có đủ 3 nhiệt độ ở giai đoạn trước khi mua? ☐ Có đo lường ở mỗi nấc? ☐ Đã cài automation ở các điểm lặp lại?
- **Bảng điểm:** Tỷ lệ khách đi qua trọn luồng; thời gian trung bình từ "Biết" → "Mua"; cost per customer theo từng luồng.
- **Nhân sự:** Chủ doanh nghiệp (kiến trúc sư luồng) + 1 Marketing Ops (vận hành automation) + từng team chuyên sâu cho từng kênh (ad, content, email, chatbot).
