# Bước 17 — Trả lời tin nhắn, chăm sóc khách hàng và triển khai chatbot

## Mục tiêu

Xây dựng hệ thống chăm sóc khách hàng **24/7 tự động** kết hợp **con người** để:
- Trả lời tin nhắn trong **60 giây đầu** — tỷ lệ chốt tăng 7x
- Giải phóng thời gian đội sales cho công việc giá trị cao
- Lưu trữ dữ liệu khách hàng để retargeting, email marketing

## 3 lớp hệ thống CSKH

### Lớp 1 — Chatbot tự động (24/7)
Xử lý **80% câu hỏi lặp lại**:
- Chào hỏi, giới thiệu sản phẩm
- FAQ: giá, lịch học, nội dung, hình thức thanh toán
- Thu thập thông tin (tên, SĐT, email) → chuyển vào CRM/danh sách email
- Đặt lịch tư vấn với con người
- Gửi link quà tặng, brochure, video giới thiệu

### Lớp 2 — Nhân viên CSKH (real-time, giờ hành chính mở rộng)
Xử lý **15-20% câu hỏi phức tạp**:
- Tư vấn theo tình huống riêng
- Xử lý khiếu nại
- Chốt sale đơn lớn
- Follow up khách đã để lại thông tin

### Lớp 3 — Chủ doanh nghiệp / chuyên gia (với khách VIP)
Xử lý **5% khách đặc biệt**:
- Khách doanh nghiệp lớn
- Khách feedback chất lượng cao
- Trường hợp leo thang (escalation)

## Các nền tảng cần setup chatbot

Tối thiểu cần chatbot trên:

### 1. Facebook Messenger
- Công cụ: ManyChat, Chatfuel, Ahachat, Harafunnel, Bizfly, Onet
- Cài chatbot cho: trả lời inbox page, comment under post, broadcast

### 2. Zalo OA
- Công cụ: BotBanHang, Zalo Bot (Zalo official), Harafunnel, Bizfly
- Cài chatbot cho: trả lời tin, broadcast đến subscriber

### 3. Website (Live chat widget)
- Công cụ: Subiz, Tawk.to, Crisp, Intercom, Drift, Tidio, Chatwoot
- Cài chatbot cho: trả lời khách đang ở trên sales page hoặc blog

### 4. WhatsApp / Telegram
- Cho khách hàng quốc tế (nếu có)
- Công cụ: WATI, Respond.io, Telegram Bot API

### 5. Tích hợp AI (GPT-based)
- Cho giai đoạn sau, khi đã có dữ liệu
- Dùng OpenAI, Claude để chatbot tự động trả lời thông minh, dựa trên kiến thức sản phẩm
- Có thể dùng: Voiceflow, Botpress, custom với Make/n8n

## 5 luồng chatbot cần có

### Luồng 1 — Chào mừng (Welcome flow)
Trigger khi khách mới inbox. Các bước:
1. Chào + tự giới thiệu thương hiệu (1 câu)
2. Hỏi: "Bạn đang cần hỗ trợ việc gì?"
3. Menu nhanh: Tư vấn sản phẩm / Hỏi giá / Nhận quà tặng miễn phí / Đặt lịch tư vấn
4. Dẫn sang luồng tương ứng

### Luồng 2 — Giao Lead Magnet (Bước 10)
Thu email/SĐT + gửi link quà ngay. Lưu vào CRM.

### Luồng 3 — Tư vấn sản phẩm
Hỏi 3-5 câu để hiểu nhu cầu → giới thiệu sản phẩm phù hợp → gửi link sales page.

### Luồng 4 — Đặt lịch tư vấn với con người
Cho chọn khung giờ → xác nhận → gửi nhắc trước 1 tiếng.

### Luồng 5 — Follow-up / Remarketing qua chat
Broadcast cho subscriber Messenger/Zalo theo segment:
- Người đã nhận quà tặng: follow-up sau 2 ngày
- Người đã xem sales page không mua: follow-up sau 1 ngày
- Người đã mua: upsell sau 7 ngày

## Nguyên tắc vàng

1. **Giọng chatbot phải nhân văn** — không được máy móc "Xin chào quý khách". Dùng giọng thân thiện như nhân viên thật.
2. **Luôn có đường thoát sang người thật** — "Gặp nhân viên" là nút quan trọng nhất.
3. **Không spam broadcast** — đúng segment, đúng thời điểm, không quá 2-3 lần/tuần.
4. **Phản hồi trong 60 giây đầu** — conversion rate cao nhất lúc khách còn "hot".

## Cấu trúc trình bày

```
## Hệ thống chăm sóc khách hàng

### Phân lớp CSKH
- Lớp 1 (bot): ...
- Lớp 2 (nhân viên): ...
- Lớp 3 (chủ DN/VIP): ...

### Nền tảng cần triển khai (ưu tiên theo thứ tự)
1. Facebook Messenger — công cụ đề xuất: ...
2. Zalo OA — công cụ đề xuất: ...
3. Website live chat — công cụ đề xuất: ...

### 5 luồng chatbot cần có
**Luồng 1 — Welcome**
- Bước 1: ...
- Bước 2: ...

**Luồng 2 — Lead Magnet delivery**
(...)

(Tương tự cho 3-5)
```

## Triển khai 4DX

- **WIG:** Rút thời gian phản hồi trung bình xuống < 60 giây trong 30 ngày; tỷ lệ chuyển đổi inbox → khách hàng ≥ 15%.
- **KPI đòn bẩy:** Số inbox/ngày được xử lý; thời gian phản hồi trung bình; tỷ lệ khách tiếp tục tương tác sau tin nhắn đầu tiên.
- **Việc hàng ngày:** Review 10% cuộc hội thoại xem bot có thoát kịch bản không; trả lời escalation; cập nhật FAQ.
- **Checklist:** ☐ 5 luồng chatbot đã chạy? ☐ Có nút "Gặp người thật"? ☐ Có SLA phản hồi < 60s? ☐ Data sync vào CRM/email list? ☐ Training nhân viên xử lý tin nhắn?
- **Bảng điểm:** Thời gian phản hồi trung bình; số khách đã trả lời đầy đủ luồng; tỷ lệ khách chốt đơn từ chat.
- **Nhân sự:** 1-2 nhân viên CSKH ca sáng/ca chiều + 1 người setup và tối ưu chatbot + chủ doanh nghiệp duyệt kịch bản và tone.
