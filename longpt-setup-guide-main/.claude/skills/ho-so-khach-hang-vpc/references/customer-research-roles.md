# 6 vai trò kiểm chứng — chi tiết khi anh Long muốn upgrade hồ sơ `hypothesis → validated`

Khi anh Long nói "tôi muốn validate persona này", đọc file này để xác định vai trò phù hợp + thiết kế quy trình thu thập bằng chứng.

## Quy tắc validate

- **Tối thiểu 2 vai trò khác nhau** trước khi `status: validated`.
- **Quote nguyên văn** từ ít nhất 3 khách trong section 8 của hồ sơ.
- **Bằng chứng định lượng** từ ít nhất 1 vai trò (Thám tử / Khoa học).
- **`sample_size`** điền vào frontmatter — không bao giờ để null khi validated.

## 1. Thám tử Dữ kiện (Data Detective) — ★

**Mục đích**: Pull từ dữ liệu sẵn có trước khi tốn công phỏng vấn.

**Nguồn cho ecosystem PTL**:

- **Pancake POS** (MCP `pancake`):
  - `manage_orders.list` với filter brand → đếm phân khúc theo địa lý, UTM, marketer, sale.
  - `manage_customers.list` → demographic của người mua khóa.
  - **Status 6 (canceled)** — pain mạnh nhất, ưu tiên pull.
  - **UTM normalize lowercase** trước khi pivot (xem [[entities/pancake-api]] mục 11.5).
- **YouTube Analytics**:
  - Top 50 bình luận của 5 video signature → pain/gain phổ biến.
  - Demographics tab — tuổi/giới/quốc gia thực của subscriber.
- **Facebook Page Insights**:
  - Bình luận top engagement → pain emotional/social.
  - "Audience" tab — nghề nghiệp, vị trí.
- **Google Search Console** (nếu có site PTL):
  - Top 50 query → từ ngữ khách dùng khi tìm PTL.
- **Lead form Pancake** (form sau lead page):
  - Câu hỏi "Anh chị đến từ đâu" / "Vì sao đăng ký" → bối cảnh + Job.

**Output cho hồ sơ**:
- Bảng phân bố nhân khẩu học theo brand
- 10 pain phổ biến nhất từ comment/review (kèm tần suất)
- 10 gain phổ biến nhất (kèm tần suất)
- 5 trigger event xuất hiện trong câu chuyện canceled

**Ngân sách**: 0đ. Thời gian: 4-8h cho 1 brand.

## 2. Phóng viên (Journalist) — ★★

**Mục đích**: Phỏng vấn 1-1 để hiểu *vì sao* sau khi có *cái gì* từ Thám tử Dữ kiện.

**Mẫu khuyến nghị**:
- **5-8 người đã mua khóa gần đây** (status=3 Pancake) — pain dẫn họ tới mua.
- **3-5 người đã đăng ký rồi hủy** (status=6) — pain cản họ chuyển đổi.
- **2-3 người đang xem video PTL nhưng chưa đăng ký** — pain rào cản đầu phễu.

→ Tổng 10-16 cuộc phỏng vấn 45-60 phút mỗi cuộc.

**Dàn bài chuẩn (rút từ 8 nguyên tắc VPD)**:

1. *"Anh chị có thể kể lại lần cuối anh chị cảm thấy [trạng thái của Job cốt lõi]?"* — VD: "lần cuối anh cảm thấy mình đang tụt lại trong việc khởi nghiệp".
2. *"Khi đó anh chị đã thử cái gì?"* — pull các "đã thử" để biết bối cảnh + lựa chọn thay thế.
3. *"Cái gì khiến anh chị thấy bực nhất / sợ nhất?"* — pull pain.
4. *"Tại sao chuyện đó quan trọng?"* — đào sâu Job đằng sau Job.
5. *"Nếu anh chị có 1 cây đũa thần — kết quả lý tưởng sẽ trông như thế nào?"* — pull Gain Khao khát + Bất ngờ.
6. *"Anh chị tìm thấy em qua đâu? Vì sao quyết định đăng ký?"* (cho người mua) / *"Vì sao chưa đăng ký?"* (cho người hủy).
7. *"Có ai khác trong đời ảnh hưởng đến quyết định này không?"* — pull DMU.
8. *"Em nên nói chuyện với ai khác nữa?"* — snowball sampling.

**8 nguyên tắc bắt buộc (VPD tr.142-143)**:
1. Tư duy người mới bắt đầu.
2. Lắng nghe nhiều hơn nói.
3. Hỏi dữ kiện, không phải ý kiến — *"Lần cuối..."*, không *"Anh có thường..."*.
4. Hỏi *"tại sao"* nhiều lần.
5. Mục đích là học, không phải bán.
6. Đừng nhắc giải pháp PTL quá sớm.
7. Xin liên hệ để follow-up.
8. Cửa cuối *"Nên nói với ai khác?"*.

**Ngân sách**: 200-500k/buổi cà phê × 10-16 buổi = 2-8tr. Thời gian: 2-3 tuần.

**Output cho hồ sơ**:
- Quote gold (3-5 quote nguyên văn vào section 8).
- Trigger event timeline (5W1H → section 2 — Bối cảnh).
- Pain ranked theo intensity (section 4).
- Gain Khao khát + Bất ngờ thực tế (section 5).

## 3. Nhà Nhân chủng học (Anthropologist) — ★

**Mục đích**: Quan sát hành vi thực, không nghe lời tự khai.

**Cho ecosystem PTL**:
- **Đứng quan sát 1 buổi DTSGC / Eagle Camp / SSS offline** — ghi sổ "Day in the Life":
  - Thời gian — Hoạt động (tôi thấy) — Ghi chú (tôi nghĩ)
  - Khi nào học viên gật gù, lướt điện thoại, hỏi.
  - Học viên ngồi đâu, đi cùng ai, mặc gì.
- **Bóng theo 1 chủ shop online** suốt 1 ngày làm việc — cảm pain "không có hệ thống bán hàng" thực sự là gì.
- **Tham gia BNI / CLB Doanh nhân** mà target persona hay xuất hiện → quan sát họ trò chuyện về cái gì với nhau.

**Quy tắc VPD tr.144-145**:
- "Tư duy người mới bắt đầu" — quên những gì mình nghĩ mình biết.
- Quan sát *cả những gì không được nói ra* — cảm xúc, ngôn ngữ cơ thể.
- Ghi chú chia 2 cột: "Tôi thấy" vs "Tôi nghĩ" — đừng trộn.

**Ngân sách**: 0đ (PTL có sẵn buổi học) — 1-2 tr (BNI fee). Thời gian: 1-2 ngày.

**Output cho hồ sơ**:
- Hành vi thực mà phỏng vấn không bao giờ thu được.
- Bối cảnh chân thực (section 2).
- Pain emotional/social mà khách không tự kể.

## 4. Người Đóng giả (Imposter) — ★★

**Mục đích**: Tự trải nghiệm hành trình khách hàng để cảm pain trực tiếp.

**Cho ecosystem PTL**:
- **Đi end-to-end 1 phễu** — xem video PTL → click bio YouTube → vào lead page → đăng ký → nhận email → mua khóa. Cảm từng điểm chạm:
  - Email mất bao lâu? Tiêu đề có hấp dẫn không?
  - Lead page có rõ value proposition không?
  - Form đăng ký có bao nhiêu trường? Có ngán không?
  - Sale page có giá rõ không?
- **Đăng ký khóa đối thủ** (Trần Việt Quân, Lan Bercu, Hieupc) — trải nghiệm bên kia để biết gap so PTL.

**Quy tắc**:
- KHÔNG nói cho bên trong PTL biết — tránh được "đối xử đặc biệt".
- Ghi nhật ký theo giờ — đừng dựa trí nhớ.

**Ngân sách**: chi phí 1 khóa đối thủ + tiền cà phê. Thời gian: 1 tháng theo phễu.

**Output cho hồ sơ**:
- Friction point cụ thể (section 4 — Pain rào cản).
- Lợi ích Bất ngờ mà đối thủ có nhưng PTL chưa có (gap analysis).

## 5. Người Cùng sáng tạo (Co-creator) — ★★★★

**Mục đích**: Mời khách vào quá trình tạo giá trị → học cùng họ.

**Cho ecosystem PTL**:
- **Inner Circle SSS** — 30 học viên top làm beta tester cho module mới trước khi launch đại trà.
- **Group VIP DTSGC** — 50 học viên cũ cho feedback về module Eagle Camp tiếp theo.
- **Mời 5 chủ shop online** vào group beta phát triển khóa "Hệ thống Bán hàng Tự động Cho Shop Online" — đồng sáng tạo curriculum.

**Quy tắc**:
- Cam kết minh bạch — họ biết mình là beta, không phải product hoàn chỉnh.
- Đền bù — voucher khóa miễn phí / mentor 1-1 / giảm giá khóa tiếp.
- Cycle ngắn — hỏi feedback mỗi 2 tuần, không 6 tháng.

**Ngân sách**: chi phí mentor / giảm giá — 5-20tr/cohort. Thời gian: 2-3 tháng.

**Output cho hồ sơ**:
- Job + Pain + Gain cập nhật theo iteration.
- Lợi ích Bất ngờ mà chính khách hàng đề xuất.
- Quote signature có thể dùng trong sale page.

## 6. Nhà khoa học (Scientist) — ★★★

**Mục đích**: A/B test biến thể để có bằng chứng định lượng.

**Cho ecosystem PTL**:

**A/B test lead page hook** (bằng chứng pain):
- Biến thể A: hook nhắm Pain Rào cản — "Bạn đang loay hoay 6 tháng không xây nổi 1 sản phẩm bán được?"
- Biến thể B: hook nhắm Pain Rủi ro — "Đừng bỏ việc khởi nghiệp khi bạn chưa biết 3 điều này"
- Đo: CVR, time on page, scroll depth.
- → Pain nào win = pain mạnh hơn trong phân khúc.

**A/B test email hook** (bằng chứng gain):
- Biến thể A: nhắm Gain Thiết yếu — "Hệ thống bán hàng tự động chạy 24/7"
- Biến thể B: nhắm Gain Bất ngờ — "AI Long Bot trả lời câu hỏi của bạn 24/7 sau khi học"
- Đo: open rate, click rate.
- → Gain nào win = gain hấp dẫn hơn.

**Multi-armed bandit test** trên YouTube thumbnail — tự động hóa qua Vidiq / Tubebuddy.

**Ngân sách**: 0đ (nếu chỉ thay copy) — 5-50tr nếu chạy Meta Ads với 2 ad set. Thời gian: 2-4 tuần để có significance.

**Output cho hồ sơ**:
- Bằng chứng định lượng (vd "Hook A: CVR 14.5%, Hook B: CVR 17.0%, p < 0.05 với n=2.220").
- Pain ranking khách quan (section 4).
- Gain ranking khách quan (section 5).
- Quote sample size + ngày test vào frontmatter `sample_size`.

## Bảng tổ hợp khuyến nghị

Tùy giai đoạn của hồ sơ, dùng tổ hợp khác nhau:

| Giai đoạn | Vai trò ưu tiên | Lý do |
|---|---|---|
| **Khóa mới chưa launch** | Thám tử + Phóng viên | Cần insight nhanh từ data sẵn + 10 phỏng vấn |
| **Lead page CVR thấp** | Khoa học + Đóng giả | A/B test hook + cảm friction trực tiếp |
| **Khóa flagship cần refresh** | Phóng viên + Cùng sáng tạo | Hiểu sâu + xây tiếp theo cùng học viên |
| **Mở thị trường mới** | Thám tử + Nhân chủng học | Pull data demographic + quan sát thực tế |
| **Sau khi launch — đo PMF** | Khoa học + Phóng viên | NPS / CSAT định lượng + định tính |

## Quy tắc cập nhật hồ sơ sau validate

Sau khi xong ≥ 2 vai trò:

1. Set `status: validated` trong frontmatter.
2. Set `last_validated: YYYY-MM-DD`.
3. Set `validated_by_roles: ["thám-tử", "phóng-viên"]` — liệt vai trò đã làm.
4. Set `sample_size: 16` — tổng số mẫu (phỏng vấn + data point).
5. Append vào section 7 "Bằng chứng đã thu thập" — bảng với từng vai trò.
6. Append vào section 8 "Quote" — ít nhất 3 quote nguyên văn từ phỏng vấn / comment / form.
7. Append vào section 10 "Lịch sử" — `{{date}} | validated | <vai trò sử dụng>`.

Hết 6 tháng → status tự chuyển `stale` (lint vault flag) → cần re-validate.
