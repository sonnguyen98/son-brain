---
name: trangbanhang
description: Tạo trang bán hàng (landing page) chuyển đổi cao từ thông tin sản phẩm, xuất ra một file HTML hoàn chỉnh tối ưu cho điện thoại. Dùng skill này BẤT CỨ KHI NÀO người dùng muốn tạo/viết/dựng một trang bán hàng, landing page, trang đích, trang sản phẩm, trang chốt đơn, sales page, hoặc gõ "/trangbanhang" — kể cả khi họ chỉ đưa thông tin một sản phẩm mà chưa nói rõ chữ "làm trang". Skill áp dụng cấu trúc thuyết phục theo phễu tâm lý, kể chuyện nỗi đau, neo giá nhiều gói, nút CTA chuẩn chuyển đổi, và nguyên tắc minh bạch (không bịa đánh giá/khan hiếm giả).
---

# Trang bán hàng chuyển đổi cao

Skill này biến thông tin sản phẩm thành một landing page HTML hoàn chỉnh, tối ưu mobile, áp dụng đầy đủ nguyên lý tối ưu chuyển đổi (CRO). Mặc định viết bằng **tiếng Việt**.

## Nguyên lý gốc (luôn ghi nhớ)

Một trang chuyển đổi cao không "thuyết phục" khách mua — nó **gỡ bỏ mọi lý do khiến khách không mua, nhanh hơn tốc độ họ nghĩ ra lý do mới**. Mọi quyết định về nội dung, bố cục, màu, nút đều phục vụ việc dẫn khách từ *nghi ngờ → tin tưởng → hành động* mà không để họ rơi giữa chừng.

Cả trang là chuỗi câu trả lời cho 5 câu hỏi ngầm trong đầu khách, đúng thứ tự:
1. Cái này có dành cho tôi không?
2. Nó giải quyết vấn đề gì của tôi?
3. Tại sao tôi phải tin?
4. Mua xong tôi có rủi ro gì?
5. Tôi cần làm gì tiếp theo, và có dễ không?

**Khẩu quyết:** rõ ràng đánh bại thông minh. Một trang nói rõ "bán gì, cho ai, lợi ích gì, tin được vì sao, làm gì tiếp" luôn thắng một trang đẹp mà mơ hồ.

## Quy trình (làm theo thứ tự)

### Bước 1 — Thu thập thông tin sản phẩm
Cần tối thiểu các thông tin sau. Nếu người dùng đã cung cấp, dùng luôn. Nếu thiếu, hỏi gọn (gộp thành 1 lượt hỏi, đừng tra khảo nhiều lượt):

- **Sản phẩm là gì** và **khách hàng mục tiêu** (ai, đang gặp vấn đề gì)
- **Lợi ích cốt lõi** (kết quả khách nhận được, không phải tính năng)
- **Nỗi đau** khách đang chịu khi chưa có sản phẩm
- **Điểm khác biệt** so với đối thủ / giải pháp cũ
- **Giá** và có **combo/gói** không
- **Bằng chứng có sẵn** (review thật, số liệu, chứng nhận, ảnh) — nếu chưa có thì để placeholder
- **Kênh chốt đơn** (link form, Zalo, hotline, giỏ hàng)
- **Tên thương hiệu** (nếu chưa có, tự đề xuất và đánh dấu là tạm)
- **Tông thương hiệu** mong muốn (nếu không nói, tự chọn theo Bước 3)

Đừng chờ đủ 100% mới làm. Thiếu gì không cốt lõi thì giả định hợp lý và đánh dấu rõ để người dùng sửa.

### Bước 2 — Chẩn đoán sản phẩm để chọn đòn
Đọc `references/chan-doan.md`. Đặt sản phẩm lên 4 trục (mức nhận biết của khách, giá/rủi ro, cảm xúc/lý trí, mua một lần/lặp lại) để quyết định **phần nào nhấn mạnh, phần nào làm nhẹ**. Đây là bước quyết định trang này khác trang khác thế nào — đừng bỏ qua. Cùng một cấu trúc, nhưng cường độ từng phần co giãn theo bản chất quyết định mua.

### Bước 3 — Chọn tông thẩm mỹ & hệ thiết kế
Đọc `references/thiet-ke.md`. **Luôn dùng nền sáng — tuyệt đối không dùng nền tối/dark.** Chọn sắc thái nền sáng + accent phù hợp *kỳ vọng cảm xúc của ngành* (trắng/xám sạch cho công nghệ/thời trang; trắng/xanh nhạt cho y tế/thực phẩm/mẹ&bé; kem ấm cho cao cấp/mỹ phẩm; trắng + điểm ấm rực cho ăn uống/sự kiện). Màu nút CTA luôn là màu tương phản mạnh, ít xuất hiện chỗ khác.

### Bước 4 — Viết copy
Đọc `references/copywriting.md` để lấy các mẫu: tiêu đề hero theo lợi ích, **kể chuyện nỗi đau** (thay vì liệt kê), dịch tính năng → lợi ích, chữ trên nút CTA, FAQ xử lý phản đối. Copy phải cụ thể, đúng giọng khách, không sáo rỗng "AI filler".

### Bước 5 — Dựng trang từ template
Dùng `assets/template.html` làm khung. Đây là file HTML tự chứa (font qua CDN, CSS/JS inline) — chỉ cần thay nội dung trong các vùng đánh dấu `{{...}}` và `<!-- ... -->`. Template đã có sẵn: mobile-first, **thanh CTA cố định đáy màn hình**, **timeline kể chuyện nỗi đau**, neo giá 3 gói, FAQ accordion, hiệu ứng cuộn, tôn trọng reduced-motion.

Cấu trúc trang (giữ đúng thứ tự phễu, có thể bỏ phần không hợp sản phẩm):
1. **Nav** + nút đặt hàng
2. **Hero** — tiêu đề lợi ích, phụ đề, CTA chính + dòng khử ma sát, trust strip
3. **Vấn đề** — kể chuyện nỗi đau (không liệt kê khô khan)
4. **Giải pháp** — tính năng dịch sang lợi ích, mỗi cái gỡ một nỗi đau
5. **Bằng chứng** — review/số liệu/chứng nhận (đánh dấu placeholder nếu chưa có thật)
6. **Khử rủi ro** — bảo hành/đổi trả/hoàn tiền, đảo rủi ro sang người bán
7. **Bảng giá** — neo 3 gói, gói giữa nổi bật "bán chạy nhất"
8. **FAQ** — xử lý phản đối phổ biến
9. **CTA cuối** — chốt mạnh + dòng khử ma sát
10. **Footer**

### Bước 6 — Kiểm tra & giao file
Nếu môi trường cho phép chạy code, chụp ảnh render desktop + mobile (390px) để kiểm tra bố cục, đặc biệt thanh CTA đáy và timeline. Sau đó lưu file vào thư mục outputs và dùng `present_files` để giao. Hậu giao chỉ tóm tắt ngắn gọn các thay đổi và những placeholder người dùng cần thay.

## Nguyên tắc bất di bất dịch

- **Luôn nền sáng.** Mặc định và bắt buộc là nền sáng (trắng/kem/tint nhạt) với chữ tông gần đen. TUYỆT ĐỐI không dùng nền tối/dark/graphite. Tạo nhịp bằng xen kẽ trắng và tint nhạt giữa các section.
- **Mobile-first.** Đa số khách VN mua trên điện thoại. Luôn có thanh CTA cố định đáy màn, nút cao ≥ 54px, chữ đọc tốt trên màn nhỏ, hero gọn để CTA nằm trong màn đầu. Không phụ thuộc hover.
- **Font tiếng Việt.** Chỉ dùng font dễ đọc, thông dụng, hỗ trợ đầy đủ dấu tiếng Việt. Cặp mặc định: **Montserrat (tiêu đề) + Roboto (nội dung)**; thay thế: Poppins, Be Vietnam Pro, Inter. Tránh font display làm hỏng dấu (Anton, Bebas…). Luôn render thử một câu nhiều dấu để kiểm tra.
- **Kể chuyện khuấy nỗi đau.** Phần Vấn đề luôn kể chuyện (không liệt kê ô khô khan). KHÔNG mặc định dùng timeline — chọn phương pháp mạnh nhất theo sản phẩm từ thư viện trong `copywriting.md` (timeline, case story, breaking point, villain reframe, before-after-bridge, failed attempts, cost stacking, future fork), và nên kết hợp vài phương pháp.
- **Lợi ích trước tính năng.** "Không lo hết pin giữa ngày", không phải "pin 5000mAh".
- **CTA chuẩn:** màu tương phản mạnh, chữ theo lợi ích & ngôi thứ nhất ("Tôi muốn thử ngay", "Nhận tư vấn miễn phí" — không phải "Gửi"), lặp lại dọc trang, luôn kèm dòng khử ma sát sát nút.
- **Neo giá:** ưu tiên 3 gói, làm gói giữa thành lựa chọn hiển nhiên nhất.
- **MINH BẠCH — quan trọng nhất:** TUYỆT ĐỐI không bịa đánh giá, tên khách, ảnh, con số, hay rating. Nếu chưa có dữ liệu thật, dựng *cấu trúc* phần đó với placeholder ghi rõ ràng (vd "[Tên khách hàng]") và nhắc người dùng thay bằng dữ liệu thật. Không cài đếm ngược/khan hiếm giả — chỉ dùng cấp bách nếu có cơ chế thật. Đây là yêu cầu đạo đức và cũng để tránh phá vỡ niềm tin.
- **Tự chứa & dễ deploy:** một file HTML, font qua CDN, không phụ thuộc framework, deploy được ngay lên Netlify/Vercel.

## Tệp tham khảo
- `references/chan-doan.md` — 4 trục chẩn đoán sản phẩm và cách co giãn từng phần
- `references/copywriting.md` — mẫu copy tiếng Việt: hero, kể chuyện nỗi đau, CTA, FAQ
- `references/thiet-ke.md` — bảng màu theo ngành, font, vai trò màu, CTA, mobile-first
- `assets/template.html` — khung landing page HTML tự chứa để điền nội dung
