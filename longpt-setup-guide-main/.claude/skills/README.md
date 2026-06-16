---
title: Skills bundled
type: skills-index
created: 2026-05-31
updated: 2026-05-31
---

# 🛠️ Skills bundled trong vault

Vault Setup-Guide đi kèm **7 skill** thật của Phạm Thành Long — sau khi clone về, anh có thể dùng ngay với Claude Code.

## 7 skill có sẵn

### 🎯 Skill signature (method coaching / marketing chuẩn hoá)

| Skill | Dùng để | Loại |
|---|---|---|
| [ips-cmo](ips-cmo/) | Đóng vai CMO cá nhân theo IPS 19 bước, dẫn chủ doanh nghiệp xây hệ marketing online tự động | Signature |
| [ho-so-khach-hang-vpc](ho-so-khach-hang-vpc/) | Build hồ sơ khách hàng theo Value Proposition Canvas của Strategyzer (mode A xây từ trí nhớ, mode B trích từ raw comment/review) | Signature |
| [cai-dat-tu-duy](cai-dat-tu-duy/) | Dẫn dắt cài đặt tư duy chuyển từ tư duy cản trở sang tư duy hỗ trợ qua 5 bước | Signature |
| [tho-ho-xuan-huong](tho-ho-xuan-huong/) | Viết thơ theo style Hồ Xuân Hương (đa nghĩa, ẩn dụ, dí dỏm) | Content signature |

### 🛠️ Skill technical (xử lý dữ liệu, content)

| Skill | Dùng để | Loại |
|---|---|---|
| [text-cat-chunk](text-cat-chunk/) | Cắt mọi file text dài (SRT có timecode, sách txt có chương, transcript thô) thành chunk ~15000 ký tự có YAML metadata + marker auto-detect | Technical |
| [srt-cat-chunk](srt-cat-chunk/) | Cắt file SRT (transcript khoá học) thành các file txt nhỏ ~10000 ký tự có YAML + timecode + marker | Technical |
| [blog-nau-an](blog-nau-an/) | Viết blog nấu ăn chuẩn SEO tiếng Việt — mỗi món có TÊN THÔNG THƯỜNG + TÊN RIÊNG ĐỘC ĐÁO HÀI HƯỚC | Content |

## 🚀 Cách dùng skills này

### Sau khi clone repo về

1. **Đảm bảo đã cài Claude Code CLI** (xem [01-cai-dat/03-cai-claude-code](../../01-cai-dat/03-cai-claude-code.md))
2. Mở terminal, `cd` vào folder vault Setup-Guide
3. Chạy `claude` — Claude Code auto detect `.claude/skills/` folder
4. Gọi skill qua slash command hoặc trigger keyword

### Ví dụ gọi skill

```
# Trong Claude Code prompt:

> /ips-cmo
[Skill ips-cmo dẫn dắt 19 bước]

> Phân tích hồ sơ khách hàng cho khoá Email Marketing của tôi
[Skill ho-so-khach-hang-vpc auto trigger]

> Cắt SRT raw/transcripts/khoa-X.srt
[Skill srt-cat-chunk chạy script chia chunk]

> Viết blog cho món "canh chua cá lóc"
[Skill blog-nau-an viết blog SEO]
```

### Hoặc copy sang vault Brain của anh

Nếu anh đã có vault Brain riêng (theo giáo trình [02-vault-dau-tien-brain](../../02-vault-dau-tien-brain/)):

```bash
cp -R "Longpt's Setup-Guide/.claude/skills" "My Brain/.claude/"
```

Skills sẽ work trong vault Brain của anh.

### Hoặc cài global (mọi vault)

```bash
mkdir -p ~/.claude/skills
cp -R "Longpt's Setup-Guide/.claude/skills/"* ~/.claude/skills/
```

Skills available ở mọi terminal Claude Code, không bị giới hạn vault.

## ⚠️ Lưu ý quan trọng

### License skills

Skills này **MIT licensed** (same as repo). Anh được:
- ✅ Dùng cho cá nhân + thương mại
- ✅ Modify theo nhu cầu
- ✅ Share + fork

Chỉ yêu cầu: **giữ copyright notice** + **attribution Phạm Thành Long** trong derivative works.

### Update skills

Skills evolve theo thời gian. Khi anh `git pull` repo Setup-Guide, skills auto cập nhật version mới.

Nếu anh đã modify local — Git sẽ flag conflict. Resolve theo workflow Git thường.

### Skills phụ thuộc tools

Một số skill cần tool external:

| Skill | Tool yêu cầu |
|---|---|
| `text-cat-chunk` | Python 3.10+ (scripts/) |
| `srt-cat-chunk` | Python 3.10+ (scripts/) |

Skills khác (`ips-cmo`, `ho-so-khach-hang-vpc`, `cai-dat-tu-duy`, `tho-ho-xuan-huong`, `blog-nau-an`) chỉ dùng Claude LLM, không cần dependency.

### Reference content trong skills

Một số skill có folder `references/` chứa knowledge base (vd `ips-cmo/references/` có 16 file framework IPS, `ho-so-khach-hang-vpc/references/` có 5 file VPC). Skills auto đọc khi run.

## 📚 Liên kết

- [Skill là gì — khái niệm](../../04-agents-skills-memory/03-skill-la-gi.md)
- [Tạo skill đầu tiên — hands-on](../../04-agents-skills-memory/04-tao-skill-dau-tien.md)
- [Memory system Claude](../../04-agents-skills-memory/05-memory-system.md)
- Source upstream: skills này cũng có ở repo riêng [github.com/wwwlongvn/ptl-skills](https://github.com/wwwlongvn/ptl-skills) (anh Long maintain)

## 🤝 Đóng góp

Phát hiện bug skill? Đề xuất cải tiến?

→ [GitHub Issues](https://github.com/wwwlongvn/longpt-setup-guide/issues) hoặc [Discussions](https://github.com/wwwlongvn/longpt-setup-guide/discussions)
