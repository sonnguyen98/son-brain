# Thiết kế & trình bày

Thẩm mỹ trong trang bán hàng không phục vụ cái đẹp — nó phục vụ **sự dẫn dắt**. Mỗi lựa chọn màu/font/nút phải trả lời: cái này giúp khách đọc dễ hơn, tin hơn, biết bấm vào đâu — hay nó cản trở?

Kiểm tra nhanh: nheo mắt cho mờ trang lại. Nếu vẫn thấy ngay đâu là nút CTA và tiêu đề chính → hệ thị giác đang dẫn dắt đúng.

## Màu sắc — nghĩ theo vai trò, không phải "màu đẹp"
**BẮT BUỘC: luôn dùng NỀN SÁNG (trắng/kem/tint nhạt). TUYỆT ĐỐI không dùng nền tối (dark/graphite/đen).** Đây là yêu cầu cố định của chủ thương hiệu.

Chỉ cần 3 nhóm:
1. **Nền + màu thương hiệu** (~90% diện tích) — luôn là nền sáng. Tạo nhịp bằng cách xen kẽ trắng và tint nhạt giữa các section, dùng một section nền accent nhạt để nhấn. Sắc thái nền chọn theo ngành:
   - Trắng/xám nhạt sạch: công nghệ, thời trang, sản phẩm phổ thông (mặc định template)
   - Trắng/xanh nhạt: y tế, thực phẩm, mẹ & bé (cảm giác đáng tin, sạch)
   - Kem/be ấm: cao cấp, mỹ phẩm, thủ công (ấm, sang)
   - Trắng + điểm màu ấm rực (đỏ/cam/vàng): ăn uống, sự kiện, giải trí, direct-response năng động (phong cách nhiều trang bán hàng VN dùng)
2. **Màu nhấn (accent)** — dùng cực tiết kiệm, chủ yếu cho CTA. **Phải tương phản mạnh trên nền sáng và ít xuất hiện chỗ khác** — mắt bị hút về điểm khác biệt. Chọn accent gắn với *lợi ích/định vị* sản phẩm (vd xanh dương = tin cậy/hành động; xanh lá = tự nhiên; đỏ-cam = năng động/giảm giá; vàng-đồng = cao cấp). Mặc định template là xanh dương `#2563EB`, đổi qua biến `--accent`.
3. **Trung tính** cho chữ phụ, viền. Trên nền sáng, dùng đổ bóng nhẹ để tạo độ sâu cho thẻ (template đã có).

Lưu ý kỹ thuật: đảm bảo tương phản chữ/nền đủ cao để đọc trên mobile ngoài nắng. Chữ xám nhạt trên nền trắng trông sang trong Figma nhưng khách thật không đọc nổi — chữ thân luôn dùng tông gần đen.

## Font chữ
**BẮT BUỘC: chỉ dùng font dễ đọc, thông dụng và hỗ trợ đầy đủ dấu tiếng Việt.** Nhiều font display/condensed (vd Anton, Bebas Neue, Oswald ở một số biến thể) hiển thị dấu tiếng Việt sai hoặc thiếu — TUYỆT ĐỐI tránh. Luôn kiểm tra render thật với một câu nhiều dấu (vd "HIỆP ĐẦU ĐẾN PHÚT BÙ GIỜ") trước khi chốt.

Font Google an toàn cho tiếng Việt, nên dùng:
- **Roboto** — cực phổ thông, dễ đọc, hỗ trợ tiếng Việt đầy đủ; lý tưởng cho nội dung. (Lưu ý: Roboto không có weight 800 — dùng 700 hoặc 900.)
- **Montserrat** — đậm, hiện đại, hợp tiêu đề/số lớn (weight 800/900); hỗ trợ tiếng Việt tốt.
- **Poppins** — tròn trịa, hiện đại, hợp tiêu đề; thay được Montserrat.
- **Be Vietnam Pro** — thiết kế riêng cho tiếng Việt, rất dễ đọc; thay được Roboto cho phần thân.
- Khác: Inter, Open Sans, Nunito Sans, Lora (serif), Bricolage Grotesque.

**Cặp mặc định của template: Montserrat (tiêu đề + số lớn, weight 800) + Roboto (nội dung)** — đây là cặp font các trang chuyển đổi cao của VN hay dùng. Thay thế hợp lệ: Poppins thay Montserrat, hoặc Be Vietnam Pro thay Roboto.

Quy tắc còn lại:
- Tối đa 1–2 font. Hơn nữa trông nghiệp dư.
- Chữ nội dung ≥ 16px (mobile có thể hơn). Dòng không quá dài. Khoảng cách dòng thoáng.
- Phân cấp rõ: tiêu đề lớn đậm, phụ đề vừa, nội dung thường — để khách *lướt* vẫn nắm ý chính.
- Font mang tính cách: serif → uy tín/cổ điển/xa xỉ; sans-serif → hiện đại/sạch/công nghệ.

## Nút CTA — chi tiết đáng đầu tư nhất
- **Màu** tương phản mạnh (xem trên).
- **Kích thước**: đủ lớn để bấm bằng ngón tay trên mobile (cao ≥ 54px), có khoảng trống quanh nút.
- **Trạng thái**: trông "bấm được" — nổi khối nhẹ, đổi màu khi hover, phản hồi khi bấm.
- **Vị trí & số lượng**: lặp lại dọc trang vì khách "chín" ở các điểm khác nhau.
- Chữ trên nút & dòng khử ma sát: xem `copywriting.md`.

## Mobile-first (ưu tiên hàng đầu)
Đa số traffic VN là điện thoại. Thiết kế cho màn 390px trước, desktop sau.
- **Thanh CTA cố định đáy màn** — đòn nâng chuyển đổi mobile mạnh nhất. Hiện sau khi khách lướt qua hero, ẩn khi tới bảng giá để khỏi trùng. Template đã có sẵn (`#mobileCta`).
- Nút cao ≥ 54px, full-width trên mobile; vùng chạm rộng; không phụ thuộc hover.
- Hero gọn để CTA chính nằm trong màn đầu. Trust strip xếp dọc. Các lưới về 1 cột.
- Chữ đọc tốt; chừa `padding-bottom` cho body để thanh CTA đáy không che nội dung.
- Tôn trọng `prefers-reduced-motion`.

## Hiệu ứng (tiết chế)
Một khoảnh khắc dàn dựng tốt (reveal khi cuộn, hover nhẹ trên nút) hơn nhiều hiệu ứng rải rác. Lạm dụng animation làm trang giống "AI tạo". Dồn sự nổi bật vào một điểm — phần còn lại giữ yên tĩnh, kỷ luật.

## Template
`assets/template.html` đã hiện thực mặc định **nền sáng** (trắng + tint nhạt) với accent đổi được qua biến CSS ở đầu file (`:root`). Đổi tông cho ngành khác: chỉnh `--accent` (và `--bg-2` nếu muốn sắc nền khác). Giữ nguyên nền sáng — không chuyển sang nền tối. Mọi màu trong trang đều tham chiếu biến — đổi ở một chỗ là đổi cả trang.
