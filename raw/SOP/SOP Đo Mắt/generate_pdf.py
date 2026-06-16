# -*- coding: utf-8 -*-
"""Generate professional Vietnamese SOP Đo Mắt PDF v2 - 10 bước."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, ListFlowable, ListItem, HRFlowable
)
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.frames import Frame
import os

# ─── Fonts ─────────────────────────────────────────────────────
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont('Calibri', os.path.join(FONT_DIR, 'calibri.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-Bold', os.path.join(FONT_DIR, 'calibrib.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-Italic', os.path.join(FONT_DIR, 'calibrii.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-BoldItalic', os.path.join(FONT_DIR, 'calibriz.ttf')))

from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Calibri', normal='Calibri', bold='Calibri-Bold',
                   italic='Calibri-Italic', boldItalic='Calibri-BoldItalic')

# ─── Colors ────────────────────────────────────────────────────
COLOR_PRIMARY = colors.HexColor('#1F6F8B')
COLOR_ACCENT = colors.HexColor('#C00000')
COLOR_SECONDARY = colors.HexColor('#2E75B6')
COLOR_GOLD = colors.HexColor('#BF8F00')
COLOR_GREEN = colors.HexColor('#548235')
COLOR_GREY_BG = colors.HexColor('#F2F2F2')
COLOR_SCRIPT_BG = colors.HexColor('#FFF2CC')
COLOR_NOTE_BG = colors.HexColor('#E2EFDA')
COLOR_WARN_BG = colors.HexColor('#FCE4D6')
COLOR_INFO_BG = colors.HexColor('#DEEBF7')
COLOR_TABLE_HEAD = colors.HexColor('#1F6F8B')

# Group colors
COLOR_GROUP1 = colors.HexColor('#2E75B6')  # blue - chuẩn bị
COLOR_GROUP2 = colors.HexColor('#548235')  # green - đo chính
COLOR_GROUP3 = colors.HexColor('#BF8F00')  # gold - kết thúc

# ─── Styles ───────────────────────────────────────────────────
styles = getSampleStyleSheet()

style_h1 = ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontName='Calibri-Bold', fontSize=20, textColor=COLOR_PRIMARY,
    spaceAfter=10, spaceBefore=4, leading=24,
)
style_h3 = ParagraphStyle(
    'H3', parent=styles['Heading3'],
    fontName='Calibri-Bold', fontSize=13, textColor=COLOR_PRIMARY,
    spaceAfter=6, spaceBefore=10, leading=17,
)
style_h4 = ParagraphStyle(
    'H4', parent=styles['Heading4'],
    fontName='Calibri-Bold', fontSize=11.5, textColor=COLOR_SECONDARY,
    spaceAfter=4, spaceBefore=6, leading=15,
)
style_body = ParagraphStyle(
    'Body', parent=styles['Normal'],
    fontName='Calibri', fontSize=11, leading=15,
    spaceAfter=4, alignment=TA_LEFT,
)
style_script = ParagraphStyle(
    'Script', parent=styles['Normal'],
    fontName='Calibri-Italic', fontSize=11, leading=15,
    textColor=colors.HexColor('#7F6000'),
    leftIndent=10, rightIndent=10, spaceAfter=4, spaceBefore=4,
)
style_cover_title = ParagraphStyle(
    'CoverTitle', parent=styles['Title'],
    fontName='Calibri-Bold', fontSize=34, textColor=COLOR_PRIMARY,
    alignment=TA_CENTER, leading=42, spaceAfter=16,
)
style_cover_sub = ParagraphStyle(
    'CoverSub', parent=styles['Normal'],
    fontName='Calibri', fontSize=16, textColor=COLOR_SECONDARY,
    alignment=TA_CENTER, leading=22, spaceAfter=10,
)
style_cover_meta = ParagraphStyle(
    'CoverMeta', parent=styles['Normal'],
    fontName='Calibri-Italic', fontSize=11, textColor=colors.grey,
    alignment=TA_CENTER, leading=14,
)

# ─── Helper functions ─────────────────────────────────────────
def script_box(text):
    p = Paragraph(f'<font name="Calibri-Italic">{text}</font>', style_script)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_SCRIPT_BG),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def note_box(text, color=COLOR_NOTE_BG, border=COLOR_PRIMARY):
    p = Paragraph(text, style_body)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('BOX', (0,0), (-1,-1), 0.5, border),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def why_box(text):
    p = Paragraph(f'<b>★ TẠI SAO:</b> {text}', style_body)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_INFO_BG),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_SECONDARY),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def warning_box(text):
    p = Paragraph(f'<b>⚠ CẢNH BÁO:</b> {text}', style_body)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_WARN_BG),
        ('BOX', (0,0), (-1,-1), 1, COLOR_ACCENT),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def criteria_box(items):
    body = '<b>✓ Tiêu chí hoàn thành bước này:</b><br/>'
    for it in items:
        body += f'&nbsp;&nbsp;&nbsp;• {it}<br/>'
    p = Paragraph(body, style_body)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_NOTE_BG),
        ('BOX', (0,0), (-1,-1), 0.5, COLOR_GREEN),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def bullets(items, indent=14):
    out = []
    for it in items:
        out.append(Paragraph(f'• {it}', ParagraphStyle(
            'B', parent=style_body, leftIndent=indent, spaceAfter=2,
        )))
    return out

def section_header(num, title, group_color=COLOR_PRIMARY):
    p = Paragraph(f'<font name="Calibri-Bold" size="22">BƯỚC {num}</font><br/>'
                  f'<font name="Calibri-Bold" size="16">{title}</font>',
                  ParagraphStyle('SH', fontName='Calibri-Bold',
                                 textColor=colors.white, leading=28,
                                 alignment=TA_LEFT))
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), group_color),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    return t

def group_divider(title, color):
    """Page divider for each of the 3 groups."""
    p = Paragraph(
        f'<font name="Calibri-Bold" color="white" size="14">{title}</font>',
        ParagraphStyle('GD', alignment=TA_CENTER, leading=18))
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def standard_table(data, col_widths):
    table_data = [[Paragraph(c, style_body) for c in row] for row in data[1:]]
    table_data.insert(0, [Paragraph(f'<font color="white"><b>{c}</b></font>', style_body) for c in data[0]])
    t = Table(table_data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), COLOR_TABLE_HEAD),
        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
    ]))
    return t

# ─── Page templates ───────────────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Calibri', 9)
    canvas.setFillColor(colors.grey)
    canvas.setStrokeColor(COLOR_PRIMARY)
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, 1.5*cm, A4[0]-2*cm, 1.5*cm)
    canvas.drawString(2*cm, 1*cm, 'Cẩm nang Đo Mắt Chuẩn Độ')
    canvas.drawRightString(A4[0]-2*cm, 1*cm, f'Trang {doc.page}')
    canvas.restoreState()

def on_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(COLOR_PRIMARY)
    canvas.rect(0, A4[1]-3*cm, A4[0], 3*cm, fill=1, stroke=0)
    canvas.setFillColor(COLOR_GOLD)
    canvas.rect(0, A4[1]-3.3*cm, A4[0], 0.3*cm, fill=1, stroke=0)
    canvas.setFillColor(COLOR_PRIMARY)
    canvas.rect(0, 0, A4[0], 1.5*cm, fill=1, stroke=0)
    canvas.setFillColor(COLOR_GOLD)
    canvas.rect(0, 1.5*cm, A4[0], 0.3*cm, fill=1, stroke=0)
    canvas.restoreState()

# ─── Build content ────────────────────────────────────────────
story = []

# ── COVER ─────────────────────────────────────────────────────
story.append(Spacer(1, 4*cm))
story.append(Paragraph('TÀI LIỆU ĐÀO TẠO NỘI BỘ', style_cover_sub))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('CẨM NANG<br/>ĐO MẮT', style_cover_title))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('CHUẨN ĐỘ TẠI CỬA HÀNG KÍNH MẮT', style_cover_sub))
story.append(Spacer(1, 2*cm))

quote_p = Paragraph(
    '<font name="Calibri-Italic" size="14" color="#1F6F8B">'
    '"Đo đúng <b>10 bước</b>, không bỏ bước.<br/>'
    'Khi nghi bệnh lý — <b>dừng, chuyển bác sĩ</b>,<br/>'
    'không cố cắt kính."'
    '</font>',
    ParagraphStyle('Q', alignment=TA_CENTER, leading=22))
qt = Table([[quote_p]], colWidths=[14*cm])
qt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), COLOR_SCRIPT_BG),
    ('BOX', (0,0), (-1,-1), 1, COLOR_GOLD),
    ('LEFTPADDING', (0,0), (-1,-1), 16),
    ('RIGHTPADDING', (0,0), (-1,-1), 16),
    ('TOPPADDING', (0,0), (-1,-1), 18),
    ('BOTTOMPADDING', (0,0), (-1,-1), 18),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
]))
story.append(qt)

story.append(Spacer(1, 4*cm))
story.append(Paragraph('Quy trình 10 bước — chia thành 3 nhóm: Chuẩn bị · Đo chính · Kết thúc',
                      style_cover_meta))
story.append(Spacer(1, 0.6*cm))
story.append(Paragraph('Phiên bản 2.0', style_cover_meta))

story.append(PageBreak())

# ── TỔNG QUAN ─────────────────────────────────────────────────
story.append(Paragraph('TỔNG QUAN QUY TRÌNH 10 BƯỚC', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Đo mắt <b>chính xác, an toàn, đồng đều</b> giữa các nhân viên — khách đeo kính dễ chịu, ít phải đổi lại.',
    style_body))
story.append(Spacer(1, 10))

# Nhóm 1
story.append(group_divider('🟦 NHÓM 1 — CHUẨN BỊ', COLOR_GROUP1))
g1_data = [
    ['Bước', 'Tên bước', 'Mục đích'],
    ['1', 'Hỏi tiền sử & Đo kính cũ', 'Hiểu nền của khách, có dữ liệu so sánh'],
    ['2', 'Chụp khúc xạ tự động + Đo PD', 'Có số liệu khởi điểm + PD chuẩn'],
    ['3', 'Thị lực không kính + Kính lỗ', 'Khách có tật khúc xạ thật hay bệnh lý?'],
]
story.append(standard_table(g1_data, [1.5*cm, 7*cm, 7.5*cm]))

story.append(Spacer(1, 10))
# Nhóm 2
story.append(group_divider('🟩 NHÓM 2 — ĐO ĐỘ CHÍNH', COLOR_GROUP2))
g2_data = [
    ['Bước', 'Tên bước', 'Mục đích'],
    ['4', 'Thử kính bằng gá thử (từng mắt)', 'Tìm độ kính chính xác'],
    ['5', 'Cân bằng 2 mắt (Binocular Balance)', '2 mắt phối hợp đều, không lệch'],
    ['6', 'Test đỏ – xanh (Duochrome)', 'Độ đã cân chưa?'],
    ['7', 'Sương mù +1.00 (Fogging)', 'Có đeo quá độ không?'],
    ['8', 'Đo độ nhìn gần — ADD (≥40 tuổi)', 'Khách lão thị có thêm độ đọc gần'],
]
story.append(standard_table(g2_data, [1.5*cm, 7*cm, 7.5*cm]))

story.append(Spacer(1, 10))
# Nhóm 3
story.append(group_divider('🟨 NHÓM 3 — KẾT THÚC', COLOR_GROUP3))
g3_data = [
    ['Bước', 'Tên bước', 'Mục đích'],
    ['9', 'Đi lại + Đọc sách thực tế', 'Khách thực sự thoải mái mới cắt'],
    ['10', 'Thử mù màu + In đơn kính', 'Hoàn tất, ghi nhận sắc giác'],
]
story.append(standard_table(g3_data, [1.5*cm, 7*cm, 7.5*cm]))

story.append(PageBreak())

# ── CHECKLIST TRƯỚC CA ────────────────────────────────────────
story.append(Paragraph('CHECKLIST TRƯỚC CA ĐO (5 phút mỗi sáng)', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
story.append(Spacer(1, 10))

checklist_items = [
    'Máy đo khúc xạ tự động đã bật, đã hiệu chuẩn',
    '<b>Máy đo PD (Pupillometer)</b> đã bật, có pin',
    '<b>Lensmeter</b> (máy đo độ kính cũ) hoạt động bình thường',
    'Bảng thị lực treo đúng vị trí, đèn sáng đều',
    '<b>Bảng đọc gần</b> (Near vision card) ở khoảng cách 40 cm',
    'Bộ kính thử (trial lens) đầy đủ độ cận / viễn / loạn / ADD',
    'Gá thử kính (trial frame) sạch, vít vặn nhẹ tay',
    'Kính lỗ (pinhole) đã có',
    'Vòng tròn thử loạn thị treo đúng vị trí',
    'Bảng thử mù màu (Ishihara) sạch',
    'Test chữ O nền đỏ – xanh (duochrome) hoạt động',
    '<b>Lăng trụ thử Binocular Balance</b> (prism flippers ±0.25)',
    'Khăn lau, cồn vệ sinh kính thử',
]
for it in checklist_items:
    story.append(Paragraph(f'☐&nbsp;&nbsp;{it}', style_body))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
# NHÓM 1 — CHUẨN BỊ
# ═══════════════════════════════════════════════════════════════
story.append(group_divider('🟦 NHÓM 1 — CHUẨN BỊ (Bước 1 – 3)', COLOR_GROUP1))
story.append(Spacer(1, 10))

# ── BƯỚC 1 ──────────────────────────────────────────────────
story.append(section_header(1, 'HỎI TIỀN SỬ & ĐO KÍNH CŨ', COLOR_GROUP1))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Hiểu <b>nền tảng</b> của khách trước khi đo — phát hiện bệnh lý tiềm ẩn + có dữ liệu so sánh với độ kính mới.',
    style_body))

story.append(Spacer(1, 10))
story.append(Paragraph('1.1 — Hỏi tiền sử y khoa', style_h3))
story.append(script_box(
    '"Trước khi đo, em hỏi anh/chị mấy câu để đo cho an toàn và chính xác hơn nhé:"'))

story.append(Spacer(1, 6))
hx_data = [
    ['Câu hỏi', 'Vì sao quan trọng'],
    ['"Anh/chị có bị TIỂU ĐƯỜNG hoặc CAO HUYẾT ÁP không?"',
     'Bệnh ảnh hưởng võng mạc → có thể cần khám bác sĩ'],
    ['"Có đang dùng THUỐC GÌ đặc biệt không? (vd: thuốc nhỏ mắt, steroid)"',
     'Một số thuốc làm đồng tử thay đổi, độ kính không chuẩn'],
    ['"Đã từng PHẪU THUẬT MẮT chưa? (LASIK, đục thuỷ tinh thể, võng mạc)"',
     'Mắt sau mổ có thông số đặc biệt'],
    ['"Có CHẤN THƯƠNG ĐẦU hoặc MẮT gần đây không?"',
     'Có thể làm thay đổi thị lực tạm thời'],
    ['"Trong nhà có ai bị GLAUCOMA (cườm nước) hay bệnh mắt di truyền không?"',
     'Khách có nguy cơ cao cần khám định kỳ'],
    ['"Lần khám mắt gần nhất là khi nào?"',
     'Nếu lâu (>2 năm) → khuyên đi khám bác sĩ trước'],
]
story.append(standard_table(hx_data, [8*cm, 8*cm]))

story.append(Spacer(1, 6))
story.append(note_box(
    'Nếu khách trả lời <b>"có"</b> cho 1 trong các câu trên → đo bình thường nhưng <b>ghi rõ vào hồ sơ</b> và cuối buổi <b>khuyên khách đi khám bác sĩ chuyên khoa định kỳ</b>.',
    color=COLOR_NOTE_BG, border=COLOR_PRIMARY))

story.append(Spacer(1, 10))
story.append(Paragraph('1.2 — Đo kính cũ (nếu khách đang đeo)', style_h3))
story.append(why_box(
    'Có dữ liệu <b>so sánh</b> với máy đo khúc xạ ở Bước 2 và độ kính mới ở Bước 4. '
    'Nếu khách quen với độ cũ, độ mới chênh nhiều quá → khách khó thích nghi.'))

story.append(Spacer(1, 6))
story.append(Paragraph('Cách làm:', style_body))
story.extend(bullets([
    'Mượn kính cũ của khách.',
    'Đặt vào <b>lensmeter</b> (máy đo độ kính).',
    'Ghi vào hồ sơ: <b>OD</b> (SPH | CYL | Axis), <b>OS</b> (SPH | CYL | Axis), <b>PD kính cũ</b>.',
    'Quan sát kính cũ: có xước nhiều? Sai tâm? Lệch trục? Gọng méo?',
]))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Hồ sơ có: tiền sử y khoa + thông số kính cũ (nếu có).',
    'Đã xác định có cần khuyên đi khám bác sĩ hay không.',
]))

story.append(PageBreak())

# ── BƯỚC 2 ──────────────────────────────────────────────────
story.append(section_header(2, 'CHỤP KHÚC XẠ TỰ ĐỘNG + ĐO PD', COLOR_GROUP1))
story.append(Spacer(1, 8))

story.append(Paragraph('<b>Mục đích kép:</b>', style_body))
story.extend(bullets([
    'Có <b>số liệu khởi điểm</b> về độ cận/viễn/loạn.',
    'Đo <b>PD chuẩn</b> — không có PD đúng thì kính cắt lệch tâm → khách nhức đầu dù độ đúng.',
]))

story.append(Spacer(1, 10))
story.append(Paragraph('2.1 — Chụp khúc xạ tự động', style_h3))
story.append(script_box(
    '"Anh/chị ngồi sát ghế, <b>để cằm lên đệm tì cằm</b>, <b>trán áp vào thanh chặn</b>, '
    '<b>mắt nhìn thẳng vào điểm sáng/hình ảnh trong máy</b>. <b>Nhìn tập trung</b>, '
    '<b>không nhắm mắt</b>, em sẽ bấm đo nhé."'))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Khi máy KHÔNG chụp được:</b>', style_body))
story.extend(bullets([
    'Reset máy, thử lại 1 lần.',
    'Vẫn không được → có thể <b>đục thuỷ tinh thể</b>, mắt khô, đồng tử quá nhỏ.',
    'Chuyển sang <b>"đo chay"</b> (đo trực tiếp ở Bước 3 & 4).',
    'Nếu nghi đục thuỷ tinh thể → khuyên đi khám bác sĩ chuyên khoa.',
]))

story.append(Spacer(1, 10))
story.append(Paragraph('2.2 — Đo PD bằng máy Pupillometer', style_h3))
story.append(why_box(
    '<b>PD là gì?</b> Khoảng cách giữa 2 đồng tử mắt (mm). Cắt kính cần đặt tâm 2 mặt kính '
    '<b>đúng vị trí đồng tử</b> — sai PD thì kính dù đúng độ vẫn gây nhức đầu, chóng mặt.'))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Cách làm:</b>', style_body))
story.extend(bullets([
    'Mời khách đặt mắt vào máy đo PD.',
    'Đo <b>2 thông số</b>:',
]))
story.extend(bullets([
    '<b>Distance PD</b> (PD nhìn xa) — máy chỉnh chế độ nhìn xa (≥3m)',
    '<b>Near PD</b> (PD nhìn gần) — máy chỉnh chế độ nhìn gần (40 cm)',
], indent=28))
story.extend(bullets([
    'Ghi vào hồ sơ.',
]))

story.append(Spacer(1, 4))
story.append(note_box(
    '<b>Tham khảo PD chuẩn:</b><br/>'
    '• Người lớn: Distance PD ≈ 60–68 mm; Near PD nhỏ hơn ~3–4 mm<br/>'
    '• Trẻ em: PD nhỏ hơn — đo cẩn thận hơn',
    color=COLOR_NOTE_BG, border=COLOR_GREEN))

story.append(Spacer(1, 6))
story.append(note_box(
    '<b>Khi nào dùng PD nào?</b><br/>'
    '• Kính nhìn xa / kính cận thường ngày → <b>Distance PD</b><br/>'
    '• Kính đọc sách (chỉ dùng nhìn gần) → <b>Near PD</b><br/>'
    '• Kính đa tròng (Progressive) → <b>cả hai</b>',
    color=COLOR_INFO_BG, border=COLOR_PRIMARY))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Có kết quả khúc xạ tự động (hoặc xác nhận "đo chay" + lý do).',
    'Có Distance PD và Near PD (nếu khách >40 tuổi).',
]))

story.append(PageBreak())

# ── BƯỚC 3 ──────────────────────────────────────────────────
story.append(section_header(3, 'THỊ LỰC KHÔNG KÍNH + KÍNH LỖ', COLOR_GROUP1))
story.append(Spacer(1, 8))

story.append(Paragraph('<b>Mục đích kép:</b>', style_body))
story.extend(bullets([
    'Đo thị lực <b>thô</b> (không kính) — biết mức độ mờ.',
    'Kính lỗ → biết tật khúc xạ thật <b>hay</b> bệnh lý.',
]))

story.append(Spacer(1, 8))
story.append(Paragraph('3.1 — Đo thị lực không kính', style_h3))
story.extend(bullets([
    '<b>Che mắt trái, đo mắt phải trước</b>, sau đó đổi mắt.',
    'Ghi mức mấy/10 cho từng mắt.',
]))

story.append(Spacer(1, 8))
story.append(Paragraph('3.2 — Thử kính lỗ (pinhole)', style_h3))
story.append(Paragraph('Đặt kính lỗ trước mắt khách, cho nhìn lại bảng thị lực.', style_body))
story.append(Spacer(1, 4))
story.append(why_box(
    'Khi nhìn qua lỗ nhỏ, ánh sáng đi thẳng vào võng mạc → rõ hơn <b>nếu là tật khúc xạ</b>. '
    'Nếu <b>không rõ hơn</b> → không phải tật khúc xạ → có thể bệnh lý.'))

story.append(Spacer(1, 10))
story.append(Paragraph('3.3 — Đọc kết quả (3 trường hợp)', style_h3))
th_data = [
    ['TH', 'Thị lực không kính', 'Kính lỗ', 'Kết luận'],
    ['TH1', 'Tốt (≥8/10)', 'Rõ lên thêm', 'Tật khúc xạ NHẸ'],
    ['TH2', 'Yếu (2/10–3/10)', 'Rõ lên rõ rệt', 'Tật khúc xạ CAO HƠN'],
    ['TH3', 'Rất yếu (<1/10)', 'Rõ lên', 'Tật khúc xạ RẤT CAO\nhoặc mỏi điều tiết quá mức'],
]
story.append(standard_table(th_data, [1.2*cm, 4.5*cm, 4*cm, 6.3*cm]))

story.append(Spacer(1, 10))
story.append(Paragraph('3.4 — Cảnh báo đặc biệt', style_h3))
story.append(warning_box(
    'Nếu <b>kính lỗ KHÔNG rõ lên</b> → có thể là <b>cận thị giả</b>, <b>cận quá nặng</b>, '
    'hoặc <b>bệnh lý mắt</b> (đục thuỷ tinh thể, võng mạc, dây thần kinh thị giác).<br/><br/>'
    '→ <b>KHÔNG cắt kính ngay</b>. Khuyến cáo khám bác sĩ chuyên khoa.'))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Đã ghi thị lực không kính của từng mắt.',
    'Đã xác định TH1 / TH2 / TH3 hoặc trường hợp nghi bệnh lý.',
]))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
# NHÓM 2 — ĐO ĐỘ CHÍNH
# ═══════════════════════════════════════════════════════════════
story.append(group_divider('🟩 NHÓM 2 — ĐO ĐỘ CHÍNH (Bước 4 – 8)', COLOR_GROUP2))
story.append(Spacer(1, 10))

# ── BƯỚC 4 ──────────────────────────────────────────────────
story.append(section_header(4, 'THỬ KÍNH BẰNG GÁ THỬ (ĐO TỪNG MẮT)', COLOR_GROUP2))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Tìm <b>độ kính chính xác</b> khách đeo thoải mái nhất.', style_body))

story.append(Spacer(1, 10))
story.append(Paragraph('4.1 — Tính độ ST (Số Thử khởi đầu)', style_h3))
story.append(why_box(
    '<b>ST là gì?</b> Là <b>Số Thử khởi đầu</b> — điểm bắt đầu để thử kính, '
    '<b>đã có sẵn fogging +1.00</b> giúp mắt thư giãn không điều tiết quá mức. '
    'ST <b>KHÔNG phải đơn cuối</b> — chỉ là khởi điểm.'))

story.append(Spacer(1, 6))
formula_p = Paragraph(
    '<font name="Calibri-Bold" size="16" color="#1F6F8B">ST = SPH + 1.00 + (CYL / 2)</font>',
    ParagraphStyle('F', alignment=TA_CENTER, leading=22))
ft = Table([[formula_p]], colWidths=[16*cm])
ft.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), COLOR_INFO_BG),
    ('BOX', (0,0), (-1,-1), 1, COLOR_PRIMARY),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(ft)
story.append(Spacer(1, 6))
story.append(Paragraph('Trong đó:', style_body))
story.extend(bullets([
    '<b>SPH</b> = độ cầu (cận hoặc viễn) máy báo',
    '<b>CYL</b> = độ trụ (loạn) máy báo',
    '<b>+1.00</b> = cộng thêm để fogging (sương mù nhẹ) → mắt thư giãn',
]))
story.append(Spacer(1, 4))
story.append(note_box(
    '<b>Ví dụ:</b> Máy báo SPH = -2.00, CYL = -1.00 → ST = -2.00 + 1.00 + (-1.00/2) = <b>-1.50</b>',
    color=COLOR_NOTE_BG, border=COLOR_GREEN))

story.append(Spacer(1, 6))
story.append(warning_box(
    'Đây là <b>công thức nội bộ của cửa hàng</b>, không phải SE chuẩn quốc tế. '
    'Trong tài liệu chuyên ngành, SE = SPH + CYL/2 (không có +1.00). '
    'Nhân viên cần biết để khỏi nhầm khi đọc sách hoặc đi học chỗ khác.'))

story.append(Spacer(1, 10))
story.append(Paragraph('4.2 — Cho khách đeo độ ST bằng cả 2 mắt', style_h3))
story.extend(bullets([
    'Đặt độ ST vào gá thử, cho khách đeo.',
    'Cho nhìn bảng thị lực hoặc <b>nhìn ra xa 1–2 phút</b> (để mắt thư giãn điều tiết).',
]))

story.append(PageBreak())

# Bước 4 tiếp - 4.3 TH1 và TH2
story.append(Paragraph('4.3 — Đo từng mắt: CHE MẮT TRÁI, ĐO MẮT PHẢI TRƯỚC', style_h3))

story.append(Spacer(1, 6))
story.append(Paragraph('TH1 — Máy đo báo có LOẠN THỊ > 0.50', style_h4))

story.append(Paragraph('<b>A — Thử loạn thị trước:</b>', style_body))
story.extend(bullets([
    'Cho khách nhìn <b>vòng tròn loạn thị</b>.',
    'Hỏi: <i>"Đường nào nét và đậm nhất? Đường nào mờ hơn?"</i>',
]))
story.append(note_box(
    '<b>Đọc kết quả:</b><br/>'
    '• Các đường đều nét đậm như nhau → KHÔNG có loạn.<br/>'
    '• 1 đường căng đậm nét, các đường xung quanh mờ → <b>độ loạn cao</b>. '
    'Đường nét nhất = <b>trục loạn</b>.',
    color=COLOR_NOTE_BG, border=COLOR_GREEN))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>B — Thêm độ loạn vào, thử dần:</b>', style_body))
story.extend(bullets([
    'Cho mặt kính loạn <b>≈ 1/2 độ máy báo</b> vào trước.',
    'VD: Máy báo loạn -1.50 → cho mặt thử <b>loạn -0.75</b> vào.',
    'Tăng -0.25 mỗi lần đến khi <b>các đường đều nét như nhau</b> → DỪNG.',
]))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>C — Sau khi xong loạn, đo độ cầu (cận/viễn):</b>', style_body))
story.extend(bullets([
    'Đeo độ <b>ST + độ loạn vừa tìm được</b>, nhìn bảng thị lực.',
    'Hỏi: <i>"Đọc được dòng nào ạ?"</i>',
    '<b>Bước nhảy 0.25 mỗi lần:</b>',
]))
story.extend(bullets([
    'Khách cận → tăng độ cận (-0.25, -0.50…)',
    'Khách viễn → giảm độ viễn',
], indent=28))
story.append(Spacer(1, 4))
story.append(note_box(
    '<b>DỪNG khi:</b> khách <b>chợt đọc được 10/10</b> (dòng nhỏ nhất rõ, không gắng sức).',
    color=COLOR_WARN_BG, border=COLOR_ACCENT))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>D — Đổi mắt:</b> che mắt phải, đo mắt trái y hệt.', style_body))

story.append(Spacer(1, 10))
story.append(Paragraph('TH2 — Máy KHÔNG báo loạn (loạn ≤ 0.50)', style_h4))
story.extend(bullets([
    'Bỏ qua vòng tròn loạn.',
    'Tăng/giảm độ cầu bước nhảy 0.25 đến khi đọc 10/10.',
    'Đổi mắt.',
]))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Mỗi mắt đọc được 10/10 với độ kính đã thử.',
    'Đã ghi đầy đủ: SPH, CYL, Axis của từng mắt.',
]))

story.append(PageBreak())

# ── BƯỚC 5 ──────────────────────────────────────────────────
story.append(section_header(5, 'CÂN BẰNG 2 MẮT (BINOCULAR BALANCE)', COLOR_GROUP2))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Bước 4 đo từng mắt riêng. Nhưng <b>não dùng cả 2 mắt cùng lúc</b> '
    '— phải test cân bằng để khách không bị <b>lệch độ</b> giữa 2 mắt.', style_body))
story.append(Spacer(1, 4))
story.append(why_box(
    'Có khi mắt phải đo ra -2.00, mắt trái -2.25. Nhưng khi đeo cả 2 cùng lúc, '
    '<b>não ưu tiên 1 mắt</b> → mắt còn lại làm việc nặng → <b>nhức 1 bên đầu</b>. '
    'Bước này phát hiện và cân bằng.'))

story.append(Spacer(1, 10))
story.append(Paragraph('5.1 — Kỹ thuật ±0.25 Flip Test', style_h3))
story.append(Paragraph('<b>Cách làm:</b>', style_body))
story.extend(bullets([
    'Cho khách đeo độ vừa đo ở Bước 4 bằng <b>cả 2 mắt</b>.',
    'Cho nhìn bảng thị lực dòng <b>9/10 hoặc 10/10</b>.',
    '<b>Đặt +0.25 trước mắt phải</b> → hỏi: <i>"Rõ hơn hay mờ hơn ạ?"</i>',
]))
story.extend(bullets([
    'Khách nói <b>MỜ hơn</b> → mắt phải OK (đủ độ).',
    'Khách nói <b>RÕ hơn</b> → mắt phải còn <b>dư độ</b> → cần giảm 0.25.',
], indent=28))
story.extend(bullets([
    'Bỏ +0.25 ra. <b>Đặt +0.25 trước mắt trái</b> → hỏi tương tự.',
    'Cả 2 mắt đều phản ứng <b>"mờ hơn"</b> → cân bằng đạt.',
]))

story.append(Spacer(1, 10))
story.append(Paragraph('5.2 — Khi 2 mắt không cân — cách điều chỉnh', style_h3))
bal_data = [
    ['Tình huống', 'Cách xử lý'],
    ['Mắt phải "rõ hơn" khi thêm +0.25', 'Giảm độ cận mắt phải 0.25'],
    ['Mắt trái "rõ hơn" khi thêm +0.25', 'Giảm độ cận mắt trái 0.25'],
    ['Cả 2 mắt đều "rõ hơn"', 'Cả 2 mắt đều dư độ → giảm cả 2 mắt 0.25'],
    ['Cả 2 mắt đều "mờ hơn"', 'Cân bằng tốt → đi tiếp Bước 6'],
]
story.append(standard_table(bal_data, [8*cm, 8*cm]))

story.append(Spacer(1, 6))
story.append(note_box(
    '<b>Mẹo nhớ:</b> Khi thêm +0.25 mà thấy <b>MỜ</b> = OK (đang đủ độ). '
    'Thấy <b>RÕ</b> = đang quá độ.',
    color=COLOR_NOTE_BG, border=COLOR_GREEN))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Cả 2 mắt đều phản ứng "mờ hơn" khi thêm +0.25.',
    'Hoặc đã điều chỉnh để đạt cân bằng.',
]))

story.append(PageBreak())

# ── BƯỚC 6 ──────────────────────────────────────────────────
story.append(section_header(6, 'TEST ĐỎ – XANH (DUOCHROME)', COLOR_GROUP2))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Kiểm tra <b>tiêu cự</b> đã rơi đúng võng mạc chưa.', style_body))
story.append(Spacer(1, 4))
story.append(why_box(
    '<b>Nguyên lý:</b> Ánh sáng đỏ và xanh có tiêu cự khác nhau trong mắt. '
    'So sánh độ rõ chữ O trên 2 nền → biết tiêu cự đang lệch về đâu.'))

story.append(Spacer(1, 10))
story.append(Paragraph('6.1 — Cách thử', style_h3))
story.extend(bullets([
    'Khách đang đeo kính thử ở Bước 4–5.',
    'Cho nhìn bảng có <b>chữ O nền đỏ</b> và <b>chữ O nền xanh</b> cạnh nhau.',
]))
story.append(script_box(
    '"Anh/chị nhìn 2 chữ O, <b>bên nào đậm/rõ hơn</b>? Đỏ hay xanh? Hay 2 bên bằng nhau?"'))

story.append(Spacer(1, 10))
story.append(Paragraph('6.2 — Đọc kết quả', style_h3))
red_data = [
    ['Khách trả lời', 'Ý nghĩa chuyên môn', 'Cách xử lý của cửa hàng'],
    ['2 bên bằng nhau', 'Tiêu cự đúng giữa võng mạc — chuẩn nhất', 'Giữ nguyên, sang Bước 7'],
    ['ĐỎ đậm hơn nhẹ', 'Tiêu cự rơi sau võng mạc nhẹ\n(under-correct nhẹ)', 'Giữ nguyên — cửa hàng chấp nhận'],
    ['XANH đậm hơn', 'Tiêu cự rơi trước võng mạc\n(over-correct, quá độ)', 'Giảm độ cận 0.25 rồi thử lại'],
]
story.append(standard_table(red_data, [4*cm, 5.5*cm, 6.5*cm]))

story.append(Spacer(1, 8))
story.append(why_box(
    '<b>Vì sao cửa hàng chấp nhận "đỏ đậm nhẹ"?</b><br/>'
    'Để hơi <b>dưới mức tối đa</b> giúp khách:<br/>'
    '• Không bị mỏi mắt khi đeo cả ngày<br/>'
    '• Không bị "nghiện độ" (mắt phụ thuộc kính nặng dần)<br/>'
    '• Đeo lâu dài thoải mái hơn<br/>'
    'Đây là <b>chính sách an toàn</b>, không phải lỗi đo.'))

story.append(Spacer(1, 6))
story.append(note_box(
    '<b>Mẹo nhớ:</b> <b>X</b>anh = e<b>X</b>cessive (quá độ) → giảm bớt.',
    color=COLOR_NOTE_BG, border=COLOR_GREEN))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Khách thấy đỏ đậm hơn hoặc 2 bên bằng nhau.',
]))

story.append(PageBreak())

# ── BƯỚC 7 ──────────────────────────────────────────────────
story.append(section_header(7, 'SƯƠNG MÙ +1.00 (FOGGING TEST)', COLOR_GROUP2))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> <b>Phanh an toàn cuối</b> trước khi cắt kính — chắc chắn khách không đeo quá độ.',
    style_body))
story.append(Spacer(1, 4))
story.append(why_box(
    '<b>Nguyên lý:</b> Cộng thêm +1.00 sẽ tạo "sương mù". Nếu vẫn đọc được nhiều dòng → '
    'mắt <b>không cần độ cao đến vậy</b> → đang đeo quá độ.'))

story.append(Spacer(1, 10))
story.append(Paragraph('7.1 — Cách thử', style_h3))
story.extend(bullets([
    'Trên độ kính đã xác định ở Bước 4–6, <b>thêm mặt +1.00</b> vào trước mắt khách.',
    'Cho khách nhìn bảng thị lực.',
    'Hỏi: <i>"Bây giờ đọc được mấy/10 ạ?"</i>',
]))

story.append(Spacer(1, 10))
story.append(Paragraph('7.2 — Đọc kết quả', style_h3))
fog_data = [
    ['Kết quả với +1.00', 'Kết luận', 'Hành động'],
    ['1 mắt đọc dưới 7/10 (vd 5–6/10)', 'Độ kính OK', 'Đi tiếp Bước 8'],
    ['1 mắt đọc ≥ 8/10', 'ĐANG ĐEO QUÁ ĐỘ', 'Giảm độ cận 0.25, đo lại từ Bước 6'],
]
story.append(standard_table(fog_data, [5.5*cm, 4.5*cm, 6*cm]))

story.append(Spacer(1, 10))
story.append(warning_box(
    'Khách đeo quá độ sẽ bị <b>nhức đầu, mỏi mắt, chóng mặt</b> sau vài ngày đeo kính mới. '
    'Bước này giúp tránh lỗi đó. <b>Không được bỏ qua.</b>'))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Với +1.00 sương mù, mỗi mắt đọc dưới 7/10.',
]))

story.append(PageBreak())

# ── BƯỚC 8 ──────────────────────────────────────────────────
story.append(section_header(8, 'ĐO ĐỘ NHÌN GẦN (ADD) — KHÁCH ≥40 TUỔI', COLOR_GROUP2))
story.append(Spacer(1, 8))

story.append(warning_box(
    '<b>Bỏ qua bước này nếu khách dưới 40 tuổi.</b>'))

story.append(Spacer(1, 6))
story.append(Paragraph(
    '<b>Mục đích:</b> Khách từ ~40 tuổi bắt đầu <b>lão thị</b> (thuỷ tinh thể giảm điều tiết → '
    'nhìn gần mờ dù vẫn nhìn xa rõ). Cần thêm độ <b>ADD</b> (additional power) cho kính đọc gần.',
    style_body))

story.append(Spacer(1, 4))
story.append(why_box(
    '<b>Lão thị là gì?</b> Không phải bệnh — là quá trình lão hoá tự nhiên. '
    'Bắt đầu ~40 tuổi, tăng dần đến ~60 tuổi.'))

story.append(Spacer(1, 10))
story.append(Paragraph('8.1 — Cách thử', style_h3))
story.extend(bullets([
    'Khách đeo độ nhìn xa đã đo ở Bước 4–7.',
    'Đưa <b>bảng đọc gần</b> ở khoảng cách <b>40 cm</b> (≈ cánh tay co lại).',
    'Hỏi: <i>"Đọc được dòng nhỏ nhất không ạ?"</i>',
    'Nếu đọc không rõ → thêm độ + vào kính, <b>bước nhảy 0.25</b>:',
]))
story.extend(bullets([
    '+0.50 → +0.75 → +1.00 → +1.25 → +1.50 → +1.75 → +2.00 → +2.25 → +2.50',
], indent=28))
story.append(Spacer(1, 4))
story.append(note_box(
    '<b>DỪNG khi:</b> khách đọc rõ dòng nhỏ nhất <b>thoải mái</b> (không gồng).',
    color=COLOR_WARN_BG, border=COLOR_ACCENT))

story.append(Spacer(1, 10))
story.append(Paragraph('8.2 — Mức ADD tham khảo theo tuổi', style_h3))
add_data = [
    ['Tuổi', 'ADD thường gặp'],
    ['40–44', '+0.75 đến +1.00'],
    ['45–49', '+1.00 đến +1.50'],
    ['50–54', '+1.50 đến +2.00'],
    ['55–59', '+2.00 đến +2.25'],
    ['60 trở lên', '+2.25 đến +2.50'],
]
story.append(standard_table(add_data, [4*cm, 12*cm]))

story.append(Spacer(1, 6))
story.append(note_box(
    'Đây là <b>tham khảo</b>, vẫn phải đo thực tế. Khách 50 tuổi có thể chỉ cần +1.25 nếu mắt còn tốt.',
    color=COLOR_NOTE_BG, border=COLOR_PRIMARY))

story.append(Spacer(1, 10))
story.append(Paragraph('8.3 — Giải pháp kính cho khách lão thị (tư vấn)', style_h3))
sol_data = [
    ['Loại kính', 'Ưu', 'Nhược'],
    ['2 kính riêng (1 xa, 1 gần)', 'Rẻ, đơn giản', 'Phải đổi 2 kính, hay quên'],
    ['Bifocal (2 vùng rõ)', '1 kính, không phải đổi', 'Có đường phân chia rõ, thẩm mỹ kém'],
    ['Progressive (đa tròng)', '1 kính nhìn xa-trung-gần liền mạch, đẹp', 'Đắt hơn, cần thời gian làm quen'],
]
story.append(standard_table(sol_data, [4.5*cm, 6*cm, 5.5*cm]))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Đã ghi mức ADD vào hồ sơ.',
    'Đã tư vấn loại kính phù hợp.',
]))

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════
# NHÓM 3 — KẾT THÚC
# ═══════════════════════════════════════════════════════════════
story.append(group_divider('🟨 NHÓM 3 — KẾT THÚC (Bước 9 – 10)', COLOR_GROUP3))
story.append(Spacer(1, 10))

# ── BƯỚC 9 ──────────────────────────────────────────────────
story.append(section_header(9, 'ĐI LẠI + ĐỌC SÁCH THỰC TẾ', COLOR_GROUP3))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Xác nhận khách thực sự <b>thoải mái</b> trong tình huống dùng thật.',
    style_body))

story.append(Spacer(1, 10))
story.append(Paragraph('9.1 — Cho khách đeo kính thử đi lại', style_h3))
story.extend(bullets([
    'Cho đứng dậy, đi vài bước trong cửa hàng.',
]))
story.append(script_box(
    '"Anh/chị đi có thấy <b>chóng mặt, lảo đảo, nền nhà nghiêng</b> không ạ?"'))

story.append(Spacer(1, 8))
story.append(Paragraph('9.2 — Cho khách đọc sách / điện thoại', style_h3))
story.extend(bullets([
    'Đưa <b>sách hoặc tờ báo</b> cho khách đọc.',
    'Nếu khách >40 tuổi: cho khách thử đeo độ nhìn gần (ADD) khi đọc.',
]))
story.append(script_box(
    '"Đọc có <b>rõ chữ</b> không? Đọc lâu có <b>nhức</b> không?"'))

story.append(Spacer(1, 8))
story.append(Paragraph('9.3 — Nhìn bảng thị lực lần cuối', style_h3))
story.append(Paragraph(
    'Cho khách nhìn lại bảng thị lực để xác nhận độ vẫn rõ.', style_body))

story.append(Spacer(1, 8))
story.append(Paragraph('9.4 — Nếu khách KHÔNG thoải mái', style_h3))
story.append(warning_box(
    'Quay lại Bước 4–5 đo lại — <b>đừng cố cắt kính</b>. '
    'Kính sai gây nhức đầu, đổi lại tốn tiền và mất uy tín.'))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Khách đi lại, đọc bình thường, không chóng mặt, không nhức.',
]))

story.append(PageBreak())

# ── BƯỚC 10 ─────────────────────────────────────────────────
story.append(section_header(10, 'THỬ MÙ MÀU + IN ĐƠN KÍNH', COLOR_GROUP3))
story.append(Spacer(1, 8))

story.append(Paragraph('10.1 — Thử mù màu (Ishihara)', style_h3))
story.append(Paragraph(
    '<b>Mục đích:</b> Phát hiện rối loạn sắc giác — quan trọng với khách làm '
    '<b>lái xe, thiết kế, in ấn, điện</b>.', style_body))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Cách thử:</b>', style_body))
story.extend(bullets([
    'Cho khách nhìn <b>bảng Ishihara</b> (chấm màu, ẩn 1 con số).',
    'Hỏi: <i>"Anh/chị đọc được số gì trên hình này?"</i>',
    'Lật vài trang khác nhau.',
]))

story.append(Spacer(1, 6))
mu_data = [
    ['Kết quả', 'Ghi vào đơn'],
    ['Đọc đúng tất cả', 'Sắc giác: bình thường'],
    ['Đọc sai 1–2 số', 'Sắc giác: yếu nhẹ'],
    ['Đọc sai nhiều / không thấy', 'Nghi mù màu — khuyến nghị khám chuyên khoa'],
]
story.append(standard_table(mu_data, [5*cm, 11*cm]))

story.append(Spacer(1, 12))
story.append(Paragraph('10.2 — In đơn kính', style_h3))
story.append(Paragraph('Đơn kính cuối cùng phải ghi đầy đủ:', style_body))

prx_data = [
    ['Mục', 'Ghi gì'],
    ['Họ tên khách', 'Đầy đủ'],
    ['Ngày đo', 'dd/mm/yyyy'],
    ['Tên nhân viên đo', 'Đầy đủ'],
    ['Mắt phải (OD)', 'SPH | CYL | Axis'],
    ['Mắt trái (OS)', 'SPH | CYL | Axis'],
    ['PD', 'Distance PD (mm), Near PD nếu có'],
    ['ADD (nếu khách ≥40)', 'Độ cộng thêm cho nhìn gần'],
    ['Mục đích dùng', 'Nhìn xa / nhìn gần / cả 2 / kính râm'],
    ['Loại kính tư vấn', 'Đơn tròng / Bifocal / Progressive'],
    ['Sắc giác', 'Bình thường / yếu nhẹ / nghi mù màu'],
    ['Ghi chú', 'Dị ứng, tiền sử, dặn dò riêng'],
]
story.append(standard_table(prx_data, [5*cm, 11*cm]))

story.append(Spacer(1, 12))
story.append(Paragraph('10.3 — Đưa khách xem, xác nhận, ký nhận', style_h3))
story.extend(bullets([
    'Đưa đơn cho khách xem qua.',
    'Khách xác nhận thông tin đúng (tên, ngày tháng, mục đích dùng).',
]))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Đã ghi sắc giác vào hồ sơ.',
    'Đơn kính in xong, khách đã xác nhận.',
]))

story.append(PageBreak())

# ── PHỤ LỤC A: TỪ ĐIỂN ──────────────────────────────────────
story.append(Paragraph('PHỤ LỤC A — TỪ ĐIỂN THUẬT NGỮ', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
story.append(Spacer(1, 10))

dict_data = [
    ['Thuật ngữ', 'VT', 'Nghĩa'],
    ['Spherical', 'SPH', 'Độ cầu — cận (–) hoặc viễn (+)'],
    ['Cylinder', 'CYL', 'Độ trụ — độ loạn thị'],
    ['Axis', 'AX', 'Trục loạn (0° – 180°)'],
    ['Số Thử (nội bộ)', 'ST', 'Công thức: ST = SPH + 1.00 + CYL/2 — điểm khởi đầu thử có fogging'],
    ['Additional Power', 'ADD', 'Độ cộng thêm cho nhìn gần (lão thị)'],
    ['Pupillary Distance', 'PD', 'Khoảng cách 2 đồng tử (mm)'],
    ['Right eye (Oculus Dexter)', 'OD', 'Mắt phải'],
    ['Left eye (Oculus Sinister)', 'OS', 'Mắt trái'],
    ['Kính lỗ (pinhole)', '–', 'Kiểm tra tật khúc xạ'],
    ['Vòng tròn loạn thị', '–', 'Tìm trục loạn'],
    ['Cận thị giả', '–', 'Mắt điều tiết quá mức, không phải cận thật'],
    ['Fogging (sương mù)', '–', 'Cộng +1.00 vào kính để test có đeo quá độ không'],
    ['Duochrome test', '–', 'Test chữ O nền đỏ – xanh'],
    ['Binocular Balance', '–', 'Test cân bằng 2 mắt khi đeo cùng lúc'],
    ['Lão thị (Presbyopia)', '–', 'Mất khả năng điều tiết nhìn gần (từ ~40 tuổi)'],
    ['Lensmeter', '–', 'Máy đo độ kính cũ'],
    ['Pupillometer', '–', 'Máy đo PD'],
    ['Ishihara', '–', 'Bảng test mù màu'],
    ['10/10', '–', 'Đọc được dòng nhỏ nhất ở khoảng cách chuẩn'],
]
story.append(standard_table(dict_data, [5*cm, 1.5*cm, 9.5*cm]))

story.append(PageBreak())

# ── PHỤ LỤC B: KHI NÀO KHÔNG CẮT ──────────────────────────
story.append(Paragraph('PHỤ LỤC B — KHI NÀO KHÔNG CẮT KÍNH, CHUYỂN BÁC SĨ?', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_ACCENT))
story.append(Spacer(1, 10))

story.append(warning_box(
    'Cửa hàng đo kính, <b>KHÔNG phải phòng khám</b>. '
    'Gặp 1 trong các dấu hiệu sau → khuyên khách đi khám bác sĩ chuyên khoa mắt trước.'))

story.append(Spacer(1, 10))
story.append(Paragraph('Các dấu hiệu phải DỪNG đo và khuyến cáo khám:', style_h3))
warning_signs = [
    'Kính lỗ <b>KHÔNG cải thiện</b> thị lực → có thể bệnh lý võng mạc / thần kinh thị giác.',
    'Máy đo không chụp được, nghi <b>đục thuỷ tinh thể</b> (khách lớn tuổi, mắt trắng đục).',
    'Khách kêu <b>nhìn mờ đột ngột</b>, <b>đau nhức mắt</b>, <b>đỏ mắt kéo dài</b>, <b>nhìn có quầng sáng</b> quanh đèn.',
    'Khách kêu <b>mất một phần thị trường</b> (mất 1 nửa hình ảnh).',
    'Khách bị <b>tiểu đường, cao huyết áp</b> lâu năm (Bước 1 đã ghi nhận).',
    '<b>Trẻ em dưới 6 tuổi</b> lần đầu đo kính → khuyên đi bác sĩ chuyên nhi/mắt khám trước.',
    '<b>Hai mắt chênh độ rất lớn</b> (>2.00 diop) → cần bác sĩ xác nhận trước khi cắt.',
    'Có <b>tiền sử glaucoma</b> trong gia đình + chưa khám gần đây.',
]
for s in warning_signs:
    story.append(Paragraph(f'⚠&nbsp;&nbsp;{s}', style_body))

story.append(Spacer(1, 10))
story.append(Paragraph('Script khuyến cáo:', style_h3))
story.append(script_box(
    '"Dạ trường hợp của anh/chị em <b>chưa thể cắt kính ngay</b> được, vì em thấy có '
    '<b>dấu hiệu cần bác sĩ chuyên khoa kiểm tra trước cho an toàn</b>. '
    'Em gợi ý anh/chị qua [tên bệnh viện/phòng khám] khám trước, sau đó em đo lại và '
    'cắt kính cho anh/chị sau cũng được ạ."'))

story.append(PageBreak())

# ── PHỤ LỤC C: 10 NGUYÊN TẮC VÀNG ───────────────────────────
story.append(Paragraph('PHỤ LỤC C — 10 NGUYÊN TẮC VÀNG KHI ĐO MẮT', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_GOLD))
story.append(Spacer(1, 10))

principles = [
    '<b>Hỏi tiền sử trước</b>, đo sau.',
    '<b>Luôn đo từng mắt một</b> (che mắt còn lại).',
    '<b>Đo mắt phải trước</b>, sau đó mắt trái.',
    '<b>Số máy chỉ là gợi ý</b>, không phải đơn kính.',
    '<b>Cho mắt thư giãn 1–2 phút</b> trước khi đo chính xác.',
    'Tăng/giảm độ <b>bước nhảy 0.25</b> — không nhảy 0.50 trở lên.',
    '<b>Thử loạn trước, thử cầu sau</b>.',
    '<b>Luôn làm Binocular Balance + Sương mù +1.00</b> — 2 phanh an toàn.',
    '<b>Đo PD đúng</b> — sai PD = kính nhức đầu dù độ đúng.',
    'Nghi bệnh lý → <b>CHUYỂN BÁC SĨ</b>, không cắt kính bằng mọi giá.',
]
for i, p in enumerate(principles, 1):
    pnum = Paragraph(
        f'<font name="Calibri-Bold" color="#BF8F00" size="20">{i:02d}</font>',
        ParagraphStyle('N', alignment=TA_CENTER, leading=24))
    ptext = Paragraph(p, style_body)
    row = Table([[pnum, ptext]], colWidths=[1.5*cm, 14.5*cm])
    row.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#E0E0E0')),
    ]))
    story.append(row)

story.append(PageBreak())

# ── PHỤ LỤC D: BẢNG TỰ ĐÁNH GIÁ ─────────────────────────────
story.append(Paragraph('PHỤ LỤC D — BẢNG TỰ ĐÁNH GIÁ NHÂN VIÊN MỚI', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
story.append(Spacer(1, 8))

story.append(Paragraph(
    'Sau mỗi ca, tự chấm 1–5 điểm cho từng mục (1 = chưa làm được, 5 = thuần thục):',
    style_body))
story.append(Spacer(1, 8))

eval_items = [
    'Hỏi đủ tiền sử khách trước khi đo?',
    'Đo kính cũ bằng lensmeter?',
    'Hướng dẫn khách ngồi đúng tư thế trên máy chụp?',
    'Đo PD (Distance + Near)?',
    'Đo thị lực không kính + thử kính lỗ?',
    'Tính đúng công thức ST = SPH + 1.00 + CYL/2?',
    'Thử LOẠN trước, CẦU sau đúng thứ tự?',
    'Dùng bước nhảy 0.25 mỗi lần thay độ?',
    'Làm Binocular Balance (±0.25 flip)?',
    'Làm test đỏ – xanh?',
    'Làm test sương mù +1.00?',
    'Khách ≥40 tuổi, đo độ nhìn gần (ADD)?',
    'Cho khách đi lại + đọc sách thử?',
    'Thử mù màu?',
    'Biết khi nào dừng và khuyên khách đi khám bác sĩ?',
]
eval_data = [['STT', 'Tiêu chí', '1', '2', '3', '4', '5']]
for i, it in enumerate(eval_items, 1):
    eval_data.append([str(i), Paragraph(it, style_body), '☐', '☐', '☐', '☐', '☐'])

ev_table = Table(eval_data, colWidths=[1*cm, 10*cm, 1*cm, 1*cm, 1*cm, 1*cm, 1*cm])
ev_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), COLOR_TABLE_HEAD),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Calibri-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Calibri'),
    ('FONTSIZE', (0,0), (-1,-1), 10.5),
    ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ('ALIGN', (2,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('TOPPADDING', (0,0), (-1,-1), 5),
    ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
]))
story.append(ev_table)

story.append(Spacer(1, 12))
story.append(Paragraph('Cách đọc kết quả:', style_h3))
result_data = [
    ['Tổng điểm', 'Nhận xét'],
    ['Dưới 45', 'Cần học lại + đi cùng anh/chị có kinh nghiệm 2 tuần.'],
    ['45 – 60', 'Đang đi đúng hướng, tiếp tục luyện.'],
    ['Trên 60', 'Đã thuần thục — có thể kèm nhân viên mới.'],
]
story.append(standard_table(result_data, [4*cm, 12*cm]))

story.append(Spacer(1, 24))
story.append(HRFlowable(width="100%", thickness=1, color=colors.grey))
story.append(Spacer(1, 8))
story.append(Paragraph(
    '<i>Tài liệu nội bộ — Phiên bản 2.0 — Vui lòng không sao chép ra ngoài.</i>',
    ParagraphStyle('foot', fontName='Calibri-Italic', fontSize=10,
                   textColor=colors.grey, alignment=TA_CENTER)))

# ─── Build document ───────────────────────────────────────────
OUTPUT = r"D:\Sơn Brain\Sơn Brain\raw\SOP\SOP Đo Mắt\Cam-Nang-Do-Mat-v2.pdf"

class MyDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        cover_frame = Frame(2*cm, 2*cm, A4[0]-4*cm, A4[1]-4*cm,
                            id='cover', leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        content_frame = Frame(2.5*cm, 2*cm, A4[0]-5*cm, A4[1]-3.5*cm,
                              id='content', leftPadding=0, rightPadding=0,
                              topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='cover', frames=cover_frame, onPage=on_cover),
            PageTemplate(id='content', frames=content_frame, onPage=on_page),
        ])

doc = MyDocTemplate(OUTPUT, pagesize=A4,
                    title='Cẩm Nang Đo Mắt Chuẩn Độ v2',
                    author='Cửa hàng kính mắt')

from reportlab.platypus import NextPageTemplate
new_story = []
inserted = False
for item in story:
    if not inserted and isinstance(item, PageBreak):
        new_story.append(NextPageTemplate('content'))
        new_story.append(item)
        inserted = True
    else:
        new_story.append(item)

doc.build(new_story)
print("PDF v2 created successfully.")
print("Output:", OUTPUT.encode('utf-8'))
