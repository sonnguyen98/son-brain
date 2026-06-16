# Overview

This wiki is a persistent, compounding knowledge base maintained by an LLM.
It is updated incrementally as new sources are ingested.

---

Wiki này tập trung vào [[he-sinh-thai-kinh-mat]] — hệ sinh thái kinh doanh kính mắt do Sơn xây dựng, gồm hai thương hiệu: **Kính Mắt Việt Hàn** ([[kinh-mat-viet-han]]), cửa hàng offline hiện tại với doanh thu ~30 triệu VND/tháng, và **Kính Mắt SONi** ([[kinh-mat-soni]]), mô hình online-first đang xây dựng, dựa trên ba lợi thế: minh bạch (video gia công), AI (thử kính ảo) và giá (giảm 20% so với cửa hàng truyền thống). Funnel cụ thể của SONi — từ website đến AI thử kính, nhắn Zalo, đặt cọc, nhận video gia công, giao hàng — được mô tả ở [[mo-hinh-ban-kinh-online]].

Một mảng lớn mới được bổ sung là khung bán hàng **[[he-thong-ban-hang-8-2]]** của [[pham-thanh-long]] — một phễu 8 bước đo lường được, cộng hai hành động xuyên suốt (xác thực và xin giới thiệu). Khung này thống nhất cách vận hành cả hai thương hiệu: với SONi, bot xử lý Bước 1-2 (danh sách, hẹn gặp) còn tư vấn viên xử lý Bước 3-7 dựa trên khung VPD "Hình Tròn/Hình Vuông" ([[vpd-hinh-tron-hinh-vuong]]) đã có sẵn cho SONi; với Việt Hàn, khách bước vào cửa hàng coi như đã qua Bước 1-2, nhân viên bắt đầu trực tiếp từ Bước 3 theo quy trình chi tiết tại [[sop-ban-hang-cua-hang]] — một SOP 6 bước với script đầy đủ cho từng tình huống (đón khách, xác định nhu cầu, trình bày lợi ích, báo giá, xử lý từ chối, follow-up).

Mảng marketing/content ([[marketing-content-strategy]]) vận hành song song qua Facebook, TikTok/Reels, YouTube và blog, với hai kênh YouTube riêng: [[echoes-of-time]] (storytelling tiếng Việt) và [[silent-film-funny-fails]] (nhằm vào khán giả US/UK 55+, không cần ngôn ngữ). Tech stack content gồm Veo3, Suno AI, CapCut và Claude AI.

Từ 2026-06-16, wiki bắt đầu có mảng **cá nhân** — bắt đầu bằng [[xem-tu-vi-le-quang-lang-2019]], buổi xem tử vi mà [[son]] thực hiện với thầy [[le-quang-lang]] năm 2019. Lời khuyên nghề từ thầy (kinh doanh công nghệ, phần mềm, lập trình, thiết kế) đáng chú ý vì **trùng hướng** với cách Sơn đang xây [[kinh-mat-soni]] (AI thử kính ảo, online-first, công nghệ). Lá số đầy đủ ở [[la-so-tu-vi-son]]. Hồ sơ chính chủ ở [[son]] — bao gồm gia đình ([[nguyen-hong-thuy]], [[nguyen-tue-an]], [[nguyen-tung-anh]]).

**North star** chi phối mọi quyết định business của Sơn được capture ở [[triet-ly-lam-viec-son]]: sống tự do = kinh doanh tự vận hành khi không có Sơn = đóng gói SOP + ủy quyền + automation. Triết lý này giải thích vì sao Sơn chọn [[he-thong-ban-hang-8-2]] (kiến trúc có lớp tự động hóa rõ), vì sao đang pivot sang [[kinh-mat-soni]] (giảm phụ thuộc vào sự có mặt của Sơn ở cửa hàng), và là tiêu chí lọc mọi recommendation mới.

**Câu hỏi mở / việc cần làm tiếp:**
- Chưa có tài liệu chi tiết về khóa IPS (phần "how" của Bước 1 trong 8+2 và cách xây Hình Tròn/Hình Vuông từ đầu).
- Một số file trong `raw/` (Affitor, Untitled, longpt-setup-guide) đang rỗng hoặc chưa rõ mục đích — cần Sơn bổ sung hoặc dọn dẹp.
- Chưa có số liệu thực tế về tỷ lệ chuyển đổi từng bước của phễu 8+2 để đo lường hiệu quả.

*Lưu ý: wiki từng bị reset về trạng thái trống ngày 2026-06-13 (xem `wiki/log.md`); các trang entity/concept hiện tại đã được phục hồi và mở rộng từ các bản sao lưu trong `raw/` cộng với nguồn mới về hệ thống 8+2.*
