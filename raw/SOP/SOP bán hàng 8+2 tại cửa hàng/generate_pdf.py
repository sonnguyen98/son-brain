# -*- coding: utf-8 -*-
"""Generate professional Vietnamese SOP PDF for training."""

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

# ─── Register Vietnamese-capable fonts ─────────────────────────
FONT_DIR = r"C:\Windows\Fonts"
pdfmetrics.registerFont(TTFont('Calibri', os.path.join(FONT_DIR, 'calibri.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-Bold', os.path.join(FONT_DIR, 'calibrib.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-Italic', os.path.join(FONT_DIR, 'calibrii.ttf')))
pdfmetrics.registerFont(TTFont('Calibri-BoldItalic', os.path.join(FONT_DIR, 'calibriz.ttf')))

from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily('Calibri', normal='Calibri', bold='Calibri-Bold',
                   italic='Calibri-Italic', boldItalic='Calibri-BoldItalic')

# ─── Brand colors ─────────────────────────────────────────────
COLOR_PRIMARY = colors.HexColor('#1F4E79')      # deep blue
COLOR_ACCENT = colors.HexColor('#C00000')       # red highlight
COLOR_SECONDARY = colors.HexColor('#2E75B6')    # lighter blue
COLOR_GOLD = colors.HexColor('#BF8F00')         # gold for "golden rule"
COLOR_GREY_BG = colors.HexColor('#F2F2F2')
COLOR_SCRIPT_BG = colors.HexColor('#FFF2CC')    # yellow for scripts
COLOR_NOTE_BG = colors.HexColor('#E2EFDA')      # green for notes
COLOR_WARN_BG = colors.HexColor('#FCE4D6')      # orange for warnings
COLOR_TABLE_HEAD = colors.HexColor('#1F4E79')

# ─── Styles ───────────────────────────────────────────────────
styles = getSampleStyleSheet()

style_h1 = ParagraphStyle(
    'H1', parent=styles['Heading1'],
    fontName='Calibri-Bold', fontSize=20, textColor=COLOR_PRIMARY,
    spaceAfter=10, spaceBefore=4, leading=24,
    borderPadding=(8, 0, 8, 0),
)
style_h2 = ParagraphStyle(
    'H2', parent=styles['Heading2'],
    fontName='Calibri-Bold', fontSize=15, textColor=colors.white,
    backColor=COLOR_PRIMARY, spaceAfter=10, spaceBefore=16,
    leading=22, borderPadding=(6, 8, 6, 8), leftIndent=0,
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
style_body_just = ParagraphStyle(
    'BodyJust', parent=style_body, alignment=TA_JUSTIFY,
)
style_bullet = ParagraphStyle(
    'Bullet', parent=style_body, leftIndent=18, bulletIndent=4,
    spaceAfter=2,
)
style_script = ParagraphStyle(
    'Script', parent=styles['Normal'],
    fontName='Calibri-Italic', fontSize=11, leading=15,
    textColor=colors.HexColor('#7F6000'),
    leftIndent=10, rightIndent=10, spaceAfter=4, spaceBefore=4,
)
style_note = ParagraphStyle(
    'Note', parent=style_body, fontName='Calibri-Bold',
    textColor=COLOR_ACCENT, spaceAfter=6,
)
style_golden = ParagraphStyle(
    'Golden', parent=style_body, fontName='Calibri-Bold',
    fontSize=11.5, textColor=COLOR_GOLD,
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
    """Yellow-highlighted box for sample scripts."""
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
    """Colored note/callout box."""
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

def golden_rule(text):
    """Highlighted 'golden rule' callout."""
    p = Paragraph(f'<b>★ NGUYÊN TẮC VÀNG:</b> {text}', style_body)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF2CC')),
        ('BOX', (0,0), (-1,-1), 1, COLOR_GOLD),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def criteria_box(items):
    """Green 'completion criteria' box."""
    body = '<b>✓ Tiêu chí hoàn thành bước này:</b><br/>'
    for it in items:
        body += f'&nbsp;&nbsp;&nbsp;• {it}<br/>'
    p = Paragraph(body, style_body)
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_NOTE_BG),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#548235')),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def bullets(items, indent=14):
    """Bullet list."""
    out = []
    for it in items:
        out.append(Paragraph(f'• {it}', ParagraphStyle(
            'B', parent=style_body, leftIndent=indent, spaceAfter=2,
        )))
    return out

def section_header(num, title):
    """Big colored header for each Bước."""
    p = Paragraph(f'<font name="Calibri-Bold" size="22">BƯỚC {num}</font><br/>'
                  f'<font name="Calibri-Bold" size="16">{title}</font>',
                  ParagraphStyle('SH', fontName='Calibri-Bold',
                                 textColor=colors.white, leading=28,
                                 alignment=TA_LEFT))
    t = Table([[p]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_PRIMARY),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
    ]))
    return t

# ─── Page template with footer ────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Calibri', 9)
    canvas.setFillColor(colors.grey)
    # Footer line
    canvas.setStrokeColor(COLOR_PRIMARY)
    canvas.setLineWidth(0.5)
    canvas.line(2*cm, 1.5*cm, A4[0]-2*cm, 1.5*cm)
    canvas.drawString(2*cm, 1*cm, 'Cẩm nang Bán Hàng tại Cửa Hàng')
    canvas.drawRightString(A4[0]-2*cm, 1*cm, f'Trang {doc.page}')
    canvas.restoreState()

def on_cover(canvas, doc):
    canvas.saveState()
    # Top color band
    canvas.setFillColor(COLOR_PRIMARY)
    canvas.rect(0, A4[1]-3*cm, A4[0], 3*cm, fill=1, stroke=0)
    canvas.setFillColor(COLOR_GOLD)
    canvas.rect(0, A4[1]-3.3*cm, A4[0], 0.3*cm, fill=1, stroke=0)
    # Bottom color band
    canvas.setFillColor(COLOR_PRIMARY)
    canvas.rect(0, 0, A4[0], 1.5*cm, fill=1, stroke=0)
    canvas.setFillColor(COLOR_GOLD)
    canvas.rect(0, 1.5*cm, A4[0], 0.3*cm, fill=1, stroke=0)
    canvas.restoreState()

# ─── Build content ────────────────────────────────────────────
story = []

# ── COVER PAGE ────────────────────────────────────────────────
story.append(Spacer(1, 4*cm))
story.append(Paragraph('TÀI LIỆU ĐÀO TẠO NỘI BỘ', style_cover_sub))
story.append(Spacer(1, 0.5*cm))
story.append(Paragraph('CẨM NANG<br/>BÁN HÀNG', style_cover_title))
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('TẠI CỬA HÀNG KÍNH MẮT', style_cover_sub))
story.append(Spacer(1, 2*cm))

# Quote box on cover
quote_p = Paragraph(
    '<font name="Calibri-Italic" size="14" color="#1F4E79">'
    '"Xây niềm tin <b>trước</b>, bán hàng <b>sau</b>.<br/>'
    'Bán bằng <b>câu hỏi</b>, không bán bằng giới thiệu suông."'
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
story.append(Paragraph('Quy trình 6 bước — diễn ra tại cửa hàng', style_cover_meta))
story.append(Spacer(1, 0.6*cm))
story.append(Paragraph('Phiên bản 1.1', style_cover_meta))

story.append(PageBreak())

# ── MỤC LỤC / TỔNG QUAN ──────────────────────────────────────
story.append(Paragraph('TỔNG QUAN QUY TRÌNH 6 BƯỚC', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<b>Mục đích:</b> Quy trình chuẩn để mọi nhân viên (kể cả người mới) đều bán được hàng đồng đều, khách hài lòng và quay lại.',
    style_body))
story.append(Paragraph(
    '<b>Ai đọc:</b> Nhân viên bán hàng tại cửa hàng kính mắt.', style_body))
story.append(Spacer(1, 10))

# Overview table
overview_data = [
    ['Bước', 'Tên bước', 'Diễn ra ở đâu'],
    ['1', 'Đón khách & xây quan hệ tin cậy', 'Tại cửa hàng'],
    ['2', 'Xác định nhu cầu (bằng câu hỏi)', 'Tại cửa hàng'],
    ['3', 'Trình bày Tính năng → Lợi ích', 'Tại cửa hàng'],
    ['4', 'Báo giá & Chốt đơn', 'Tại cửa hàng'],
    ['5', 'Xử lý từ chối', 'Tại cửa hàng'],
    ['6', 'Follow-up & Chăm sóc sau bán', 'Sau khi khách về'],
]
ov_table = Table(overview_data, colWidths=[1.5*cm, 9*cm, 5.5*cm])
ov_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), COLOR_TABLE_HEAD),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Calibri-Bold'),
    ('FONTNAME', (0,1), (-1,-1), 'Calibri'),
    ('FONTSIZE', (0,0), (-1,-1), 11),
    ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('FONTNAME', (1,1), (1,-1), 'Calibri-Bold'),
    ('TOPPADDING', (0,0), (-1,-1), 7),
    ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
]))
story.append(ov_table)

story.append(Spacer(1, 18))

# Checklist trước ca
story.append(Paragraph('CHECKLIST TRƯỚC CA LÀM (5 phút mỗi sáng)', style_h3))
checklist_items = [
    'Đồng phục gọn gàng, bảng tên đeo ngay ngắn',
    'Tủ trưng bày sạch, kính lau bóng',
    'Bàn đo, ghế khách lau sạch',
    'Máy đo mắt bật sẵn, đã hiệu chuẩn',
    'Quà tặng nhỏ (móc khoá / khăn lau / nước rửa kính) đủ số lượng',
    'Bút, sổ ghi hồ sơ khách, máy POS, mã QR thanh toán sẵn sàng',
    'Đã xem lại lịch hẹn khách trong ngày + lịch follow-up cần gọi',
]
for it in checklist_items:
    story.append(Paragraph(f'☐&nbsp;&nbsp;{it}', style_body))

story.append(PageBreak())

# ── BƯỚC 1 ──────────────────────────────────────────────────
story.append(section_header(1, 'ĐÓN KHÁCH & XÂY QUAN HỆ TIN CẬY'))
story.append(Spacer(1, 8))

story.append(golden_rule(
    '<b>KHÔNG bán hàng ngay.</b> Phải xây dựng <b>mối quan hệ tin cậy và thân tình</b> với khách hàng.'))
story.append(Spacer(1, 8))

# 1.1
story.append(Paragraph('1.1 — Mở cửa chào hỏi', style_h3))
story.append(Paragraph('Câu mở đầu chuẩn (đọc thuộc):', style_body))
story.append(script_box(
    '"Em chào anh/chị, anh/chị cần <b>đo cắt kính</b> hay cần <b>hỗ trợ gì</b> ạ?"'))
story.append(Paragraph(
    '→ Câu này giúp phân loại nhanh khách thành 2 nhóm để xử lý đúng cách.',
    style_body))

# 1.2 NHÁNH A
story.append(Paragraph('1.2 — Phân nhánh theo loại khách', style_h3))
story.append(Paragraph('NHÁNH A — Khách đo / cắt kính', style_h4))
story.extend(bullets([
    '<b>Mời khách ngồi ghế</b> cho mát, cho mắt nghỉ ngơi 1 lát.',
    '<b>Nếu khách đang đeo kính:</b> Mượn kính và đo độ kính cũ. Kiểm tra: có xước nhiều không? Có sai tâm, lệch trục, loạn không?',
    'Hỏi tiếp: <i>"Anh/chị cắt kính này ở đâu ạ?"</i> — Nếu cắt ở đây thì tra lại hồ sơ. Nếu cắt chỗ khác thì hỏi <i>"Anh/chị cắt lâu chưa ạ?"</i>',
    '<b>Nếu khách chưa đeo kính:</b> Hỏi <i>"Anh/chị có vấn đề gì về mắt mà cần đi kiểm tra ạ?"</i>',
]))

story.append(Spacer(1, 6))
story.append(Paragraph('NHÁNH B — Khách thay gọng / mua kính râm', style_h4))
story.extend(bullets([
    '<b>Mời nước</b> (nếu khách có thời gian — khách vội thì bỏ qua).',
    'Nói chuyện thân mật, tìm điểm chung: <b>nơi ở, vấn đề xã hội, sức khoẻ, công việc</b>.',
    'Sau đó chuyển sang <b>Bước 2</b>.',
]))

# 1.3
story.append(Spacer(1, 8))
story.append(Paragraph('1.3 — Trong lúc chờ đo mắt (1–2 phút) — Tạo gần gũi', style_h3))
story.append(Paragraph(
    '<b>Nguyên tắc:</b> Nói <b>về khách</b>, không nói về mình.', style_body))
story.append(Paragraph('Các chủ đề an toàn để bắt chuyện:', style_body))
story.extend(bullets([
    'Nơi ở (gần đây không, đi xa không...)',
    'Con cái (đi học gần đây không, mấy cháu rồi...)',
    'Sức khoẻ',
    'Sở thích',
    'Công việc (nhưng nhẹ nhàng, không tra hỏi)',
]))
story.append(Spacer(1, 4))
story.append(note_box(
    '<b>Mục tiêu:</b> Tìm <b>1 điểm chung</b> để khách thấy thoải mái như nói chuyện với người quen.',
    color=COLOR_NOTE_BG, border=COLOR_PRIMARY))

# 1.4
story.append(Spacer(1, 8))
story.append(Paragraph('1.4 — Tặng quà nhỏ', style_h3))
story.append(Paragraph(
    'Tặng 1 trong: <b>móc khoá / khăn lau kính / nước rửa kính</b>.', style_body))
story.append(Paragraph(
    '<i>Mục đích:</i> Khách đã cầm "quà" về tay → tâm lý có thiện cảm → dễ tiếp tục câu chuyện.',
    style_body))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Khách đã ngồi ghế, không còn trạng thái "đề phòng".',
    'Đã có ít nhất 1 điểm chung trong câu chuyện.',
    'Khách đã nhận quà nhỏ.',
]))

story.append(PageBreak())

# ── BƯỚC 2 ──────────────────────────────────────────────────
story.append(section_header(2, 'XÁC ĐỊNH NHU CẦU (BẰNG CÂU HỎI)'))
story.append(Spacer(1, 8))

story.append(golden_rule(
    '<b>LUÔN xác định nhu cầu bằng CÂU HỎI.</b> Không tự đoán, không gợi ý sản phẩm khi chưa hỏi.'))
story.append(Spacer(1, 8))

# 2.1
story.append(Paragraph('2.1 — Nếu là khách ĐO / CẮT KÍNH', style_h3))
story.append(Paragraph(
    'Hỏi <b>trước khi lên đo mắt</b>, ghi vào hồ sơ khách hàng.', style_body))
story.append(Spacer(1, 4))
story.append(Paragraph('<b>Bộ 7 câu hỏi tiêu chuẩn:</b>', style_body))

questions_a = [
    'Công việc của anh/chị có phải nhìn gần nhiều không ạ?',
    'Có phải sử dụng điện thoại, máy tính nhiều không ạ?',
    'Anh/chị có hay nhức mỏi mắt không?',
    'Có hay nằm xem điện thoại, đọc truyện không ạ?',
    'Đi đường có thấy mờ hay loá nhiều không?',
    'Anh/chị muốn sử dụng kính chủ yếu để làm gì ạ? (đi làm / lái xe / đọc sách / nhìn xa…)',
    'Kính cũ ngày trước dùng có vấn đề gì làm anh/chị cảm thấy khó chịu không?',
]
for i, q in enumerate(questions_a, 1):
    story.append(script_box(f'<b>Câu {i}:</b> "{q}"'))
    story.append(Spacer(1, 2))

story.append(Paragraph(
    '→ Sau khi hỏi xong, <b>đo mắt theo SOP đo mắt riêng</b>.', style_note))

# 2.2
story.append(Spacer(1, 10))
story.append(Paragraph('2.2 — Nếu là khách THAY GỌNG / MUA KÍNH RÂM', style_h3))
questions_b = [
    'Anh/chị mua kính cho mình hay tặng ai ạ?',
    'Người dùng là nam hay nữ, khoảng bao nhiêu tuổi?',
    'Anh/chị muốn gọng màu gì? Khuôn mặt như nào ạ?',
    'Anh/chị có muốn đo lại mắt xem có tăng độ không ạ? Bên em đo MIỄN PHÍ.',
]
for i, q in enumerate(questions_b, 1):
    story.append(script_box(f'<b>Câu {i}:</b> "{q}"'))
    story.append(Spacer(1, 2))

story.append(note_box(
    '<b>★ Câu 4 rất quan trọng</b> — đây là <b>cầu nối</b> để chuyển khách thay gọng / kính râm '
    'sang luôn nhánh cắt tròng (tăng giá trị đơn).',
    color=COLOR_WARN_BG, border=COLOR_ACCENT))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Trả lời được: Khách cần kính cho việc gì?',
    'Đã ghi vào hồ sơ khách hàng.',
    'Đã xác định được 2–3 lợi ích khách quan tâm nhất (dùng ở Bước 3).',
]))

story.append(PageBreak())

# ── BƯỚC 3 ──────────────────────────────────────────────────
story.append(section_header(3, 'TRÌNH BÀY TÍNH NĂNG → LỢI ÍCH'))
story.append(Spacer(1, 8))

story.append(golden_rule(
    '<b>Không nói tính năng suông.</b> Mỗi tính năng phải gắn với 1 <b>lợi ích</b> '
    'mà khách quan tâm (xác định ở Bước 2).'))
story.append(Spacer(1, 10))

story.append(Paragraph('3.1 — Tính năng & Lợi ích cần thuộc', style_h3))

# --- TÍNH NĂNG section ---
feat_header = Paragraph(
    '<font name="Calibri-Bold" color="white" size="12">TÍNH NĂNG (sản phẩm có gì)</font>',
    style_body)
feat_header_t = Table([[feat_header]], colWidths=[16*cm])
feat_header_t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), COLOR_TABLE_HEAD),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(feat_header_t)

tinh_nang = [
    'Nhẹ, dẻo, nhíp co dãn',
    'Chắc chắn, chống vỡ',
    'Bền màu, không rỉ',
    'Trong, tròn, mỏng',
    'Chống ánh sáng xanh, chống tia UV / cực tím',
    'Tan hơi nhanh',
    'Đổi màu',
    'Hạn chế xước',
]
feat_body = '<br/>'.join([f'•&nbsp;&nbsp;{x}' for x in tinh_nang])
feat_body_t = Table([[Paragraph(feat_body, style_body)]], colWidths=[16*cm])
feat_body_t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.grey),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(feat_body_t)

story.append(Spacer(1, 8))

# Arrow between sections
arrow = Paragraph(
    '<font name="Calibri-Bold" color="#BF8F00" size="18">↓</font>',
    ParagraphStyle('arr', alignment=TA_CENTER, leading=20))
story.append(arrow)

story.append(Spacer(1, 4))

# --- LỢI ÍCH section ---
loi_header = Paragraph(
    '<font name="Calibri-Bold" color="white" size="12">LỢI ÍCH (khách được gì)</font>',
    style_body)
loi_header_t = Table([[loi_header]], colWidths=[16*cm])
loi_header_t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#548235')),
    ('LEFTPADDING', (0,0), (-1,-1), 12),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
]))
story.append(loi_header_t)

loi_ich = [
    'Đeo không đau tai, dễ chịu khi đeo lâu, nhẹ như không đeo',
    'Nhỡ nằm đè vào không gãy; bị lệch nắn chỉnh dễ về form',
    'Đeo lâu vẫn sáng bóng, ít bị xỉn màu',
    'Kính cắt lên đẹp, ít lộ viền dày, đeo dễ chịu hơn',
    'Nhìn hình ảnh thật và rõ nét, giảm mỏi mắt khi dùng lâu',
    'Đi từ lạnh ra nóng (hoặc ngược lại) kính không bị mờ lâu',
    'Một kính dùng được cả trong nhà và ngoài trời',
    'Lau chùi vệ sinh dễ dàng, lỡ rơi cũng khó vỡ',
]
loi_body = '<br/>'.join([f'•&nbsp;&nbsp;{x}' for x in loi_ich])
loi_body_t = Table([[Paragraph(loi_body, style_body)]], colWidths=[16*cm])
loi_body_t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), COLOR_NOTE_BG),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#548235')),
    ('LEFTPADDING', (0,0), (-1,-1), 14),
    ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ('TOPPADDING', (0,0), (-1,-1), 10),
    ('BOTTOMPADDING', (0,0), (-1,-1), 10),
]))
story.append(loi_body_t)

story.append(Spacer(1, 12))
story.append(Paragraph('3.2 — Công thức nói', style_h3))
story.append(note_box(
    '<b>"Cái này [TÍNH NĂNG], nên anh/chị sẽ [LỢI ÍCH], rất hợp với việc anh/chị vừa kể là [NHU CẦU KHÁCH NÓI Ở BƯỚC 2]."</b>',
    color=COLOR_WARN_BG, border=COLOR_ACCENT))
story.append(Spacer(1, 6))

story.append(Paragraph(
    '<b>Ví dụ:</b> Khách ở Bước 2 nói <i>"tôi hay nhức mắt khi dùng máy tính"</i> →',
    style_body))
story.append(script_box(
    '"Loại tròng này <b>có chống ánh sáng xanh và tia UV</b>, anh dùng cả ngày sẽ '
    '<b>đỡ mỏi mắt và nhìn rõ nét hơn</b>, rất hợp với việc anh ngồi máy tính nhiều như vừa kể ạ."'))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Đã giới thiệu 2–3 lợi ích ĐÚNG với nhu cầu khách nêu.',
    'Khách gật đầu / hỏi lại / quan tâm rõ rệt.',
]))

story.append(PageBreak())

# ── BƯỚC 4 ──────────────────────────────────────────────────
story.append(section_header(4, 'BÁO GIÁ & CHỐT ĐƠN'))
story.append(Spacer(1, 8))

story.append(Paragraph('4.1 — Hai nguyên tắc bắt buộc', style_h3))
story.extend(bullets([
    '<b>Chỉ nói những lợi ích của tính năng mà khách đang quan tâm</b> — không nói lan man những thứ khách không cần.',
    '<b>Dùng phương pháp "ướm thử" để xem có nâng đơn được không.</b>',
]))
story.append(Spacer(1, 4))
story.append(Paragraph('Script ướm thử mẫu:', style_body))
story.append(script_box(
    '"Anh có thể dùng lên loại tròng <b>960</b> được không ạ? Loại này <b>cắt lên mỏng hơn</b> '
    'mà <b>giảm loá khi đi đường tốt hơn</b> anh ạ."'))

story.append(Spacer(1, 10))
story.append(Paragraph('4.2 — Cách báo giá chuẩn', style_h3))
story.append(Paragraph('Khi báo giá, <b>luôn gói cùng 3 thứ</b>:', style_body))
story.extend(bullets([
    '<b>Chế độ bảo hành</b> (bao lâu, bảo hành gì)',
    '<b>Quà tặng kèm theo</b> (cụ thể, có thật)',
    '<b>Thời gian ưu đãi</b> nếu có (ví dụ: "Giá này áp dụng đến hết tuần này thôi ạ.")',
]))

story.append(Spacer(1, 4))
story.append(Paragraph('Script báo giá mẫu:', style_body))
story.append(script_box(
    '"Tổng bộ gọng + tròng của anh là <b>X đồng</b> ạ. Bên em <b>bảo hành Y tháng</b>, '
    'tặng kèm anh <b>khăn lau + hộp kính cao cấp</b>. Mức này em đang áp dụng đến '
    '<b>hết ngày Z</b> ạ."'))

story.append(Spacer(1, 10))
story.append(Paragraph('4.3 — Câu chốt', style_h3))
story.append(note_box(
    '<b>Sau khi báo giá → IM LẶNG.</b> Để khách phản ứng trước. Ai nói trước là người "thua".',
    color=COLOR_WARN_BG, border=COLOR_ACCENT))
story.append(Spacer(1, 4))
story.append(Paragraph('Nếu khách lưỡng lự, dùng 1 trong 3 câu chốt:', style_body))
story.append(script_box('"Em làm luôn cho anh/chị nhé, khoảng 30 phút là xong ạ?"'))
story.append(Spacer(1, 3))
story.append(script_box('"Anh/chị thanh toán tiền mặt hay chuyển khoản ạ?"'))
story.append(Spacer(1, 3))
story.append(script_box('"Anh/chị muốn nhận hàng hôm nay hay mai em giao ạ?"'))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Khách đồng ý mua → chuyển sang xử lý đơn.',
    'Khách từ chối / lưỡng lự → chuyển sang Bước 5.',
]))

story.append(PageBreak())

# ── BƯỚC 5 ──────────────────────────────────────────────────
story.append(section_header(5, 'XỬ LÝ TỪ CHỐI'))
story.append(Spacer(1, 8))

story.append(golden_rule(
    '<b>Không cãi. Không hạ giá ngay.</b> Trước hết <b>đồng cảm</b> — rồi mới <b>lật câu chuyện</b>.'))
story.append(Spacer(1, 10))

# 5.1
story.append(Paragraph('5.1 — "Anh thấy đắt quá"', style_h3))
story.append(Paragraph('<b>Cách 1:</b> Hỏi để biết khách so sánh với gì.', style_body))
story.append(script_box('"Anh thấy đắt <b>hơn so với loại nào</b> ạ?"'))
story.append(Spacer(1, 4))
story.append(Paragraph('<b>Cách 2:</b> Lật câu chuyện về giá trị / chia nhỏ chi phí.', style_body))
story.append(script_box(
    '"Loại này <b>bền có khi vài năm mới phải thay</b>, tính ra mỗi ngày cả mắt '
    '<b>có mấy nghìn</b> mà mình lại được <b>dùng loại tốt</b> ạ."'))

# 5.2
story.append(Spacer(1, 10))
story.append(Paragraph('5.2 — "Giảm giá cho anh 20% đi!"', style_h3))
story.append(note_box(
    '<b>Nguyên tắc:</b> KHÔNG hạ giá. Thay vào đó, <b>BÙ ĐẮP BẰNG GIÁ TRỊ THÊM</b>. '
    'Nhân viên tự xử lý, không cần hỏi quản lý.',
    color=COLOR_WARN_BG, border=COLOR_ACCENT))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Cách xử lý 3 bước:</b>', style_body))

story.append(Spacer(1, 4))
story.append(Paragraph('<b>Bước 1 — Đồng cảm, không cãi:</b>', style_h4))
story.append(script_box('"Dạ em hiểu mà anh/chị, ai mua cũng muốn được giá tốt nhất ạ."'))

story.append(Spacer(1, 4))
story.append(Paragraph('<b>Bước 2 — Khẳng định giá đã tốt:</b>', style_h4))
story.append(script_box(
    '"Mức giá em báo đã là giá ưu đãi nhất bên em rồi anh ạ, đã bao gồm '
    '<b>bảo hành dài hạn + quà tặng kèm + dịch vụ chỉnh kính miễn phí trọn đời</b>. '
    'Em không tự ý giảm thêm được."'))

story.append(Spacer(1, 4))
story.append(Paragraph('<b>Bước 3 — Đề xuất giá trị thêm</b> (chọn 1 trong 3):', style_h4))
story.append(script_box(
    '"Nhưng để cảm ơn anh, em xin tặng thêm anh '
    '<b>[1 hộp kính cao cấp / 1 chai nước rửa kính chuyên dụng]</b>."'))
story.append(Spacer(1, 2))
story.append(script_box(
    '"Em sẽ cộng thêm cho anh <b>3 tháng bảo hành</b> không tính phí ạ."'))
story.append(Spacer(1, 2))
story.append(script_box(
    '"Em tặng anh <b>phiếu giảm 20% cho lần đo cắt kính tiếp theo</b> trong vòng 1 năm ạ."'))

story.append(Spacer(1, 6))
story.append(Paragraph('<b>Câu chốt cuối:</b>', style_h4))
story.append(script_box('"Anh thấy thế đã ổn chưa ạ? Em làm luôn cho anh nhé."'))

story.append(Spacer(1, 6))
story.append(note_box(
    '<b>Vì sao cách này hiệu quả:</b> Khách đòi giảm giá thường muốn cảm giác '
    '<b>"được lợi hơn"</b> chứ không hẳn vì thiếu tiền. Tặng thêm giá trị giúp khách '
    '<b>thấy mình thắng</b> — mà cửa hàng vẫn giữ giá gốc, vẫn có lãi.',
    color=COLOR_NOTE_BG, border=COLOR_PRIMARY))

# 5.3
story.append(Spacer(1, 10))
story.append(Paragraph('5.3 — "Thôi anh về có gì anh quay lại sau"', style_h3))
story.append(Paragraph('<b>Không cố giữ.</b> Làm 2 việc:', style_body))
story.extend(bullets([
    '<b>Tôn trọng ý kiến:</b> "Dạ vâng, anh/chị cứ về suy nghĩ thêm ạ."',
    '<b>Tặng cảm xúc + quà nhỏ:</b> Đưa khách card visit + 1 quà nhỏ (khăn lau / móc khoá) + lời nhắn dưới đây.',
]))
story.append(script_box(
    '"Em gửi anh/chị <b>khăn lau kính</b>, dùng kính cũ cũng được ạ. '
    'Khi nào tiện ghé em luôn đo lại mắt miễn phí cho anh/chị nhé."'))

# 5.4
story.append(Spacer(1, 12))
story.append(Paragraph('5.4 — Các từ chối phổ biến khác', style_h3))

obj_data = [
    ['Khách nói', 'Cách phản hồi mẫu'],
    ['"Để tôi về hỏi vợ / chồng / con cái đã."',
     '"Dạ vâng anh chị, hay anh chị gọi điện luôn cho người nhà em trao đổi giúp ạ?" — nếu không thì hẹn lịch quay lại cụ thể.'],
    ['"Tôi đang dùng kính khác vẫn ổn."',
     '"Dạ kính cũ anh dùng được mấy năm rồi ạ? Mắt mình thay đổi theo thời gian, em đo miễn phí cho anh xem đỡ rủi ro về sau ạ."'],
    ['"Bên kia rẻ hơn."',
     '"Dạ anh có thể cho em xem báo giá bên kia được không ạ? Em xem cùng loại tròng / gọng thì giá bên em thế nào để tư vấn cho đúng."'],
    ['"Để tôi tham khảo thêm vài chỗ."',
     '"Dạ tốt anh ạ. Em ghi cho anh đúng thông số mình cần để anh tham khảo cho dễ. Em là [Tên NV], khi nào cần anh nhắn em."'],
]
obj_table_data = [[Paragraph(r[0], style_body), Paragraph(r[1], style_body)] for r in obj_data[1:]]
obj_table_data.insert(0, [Paragraph(f'<font color="white"><b>{obj_data[0][0]}</b></font>', style_body),
                           Paragraph(f'<font color="white"><b>{obj_data[0][1]}</b></font>', style_body)])

obj_table = Table(obj_table_data, colWidths=[5.5*cm, 10.5*cm])
obj_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), COLOR_TABLE_HEAD),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
    ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
]))
story.append(obj_table)

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Khách đồng ý mua → quay lại Bước 4 hoàn tất.',
    'Khách về tay không → VẪN lưu thông tin + lên lịch follow-up Bước 6.',
]))

story.append(PageBreak())

# ── BƯỚC 6 ──────────────────────────────────────────────────
story.append(section_header(6, 'FOLLOW-UP & CHĂM SÓC SAU BÁN'))
story.append(Spacer(1, 8))

story.append(golden_rule(
    'Khách đã mua <b>chưa phải là kết thúc</b>. Khách <b>quay lại + giới thiệu khách mới</b> mới là kết thúc.'))
story.append(Spacer(1, 10))

story.append(Paragraph('6.1 — Lịch chăm sóc chuẩn', style_h3))

fu_data = [
    ['Mốc', 'Hành động', 'Script mẫu'],
    ['Sau 1 tuần\n(cắt kính)', 'Nhắn hỏi thăm',
     '"Anh/chị [Tên], em [Tên NV] bên kính [X]. Kính anh/chị dùng được 1 tuần rồi, có gì chưa quen không ạ? Có gì em hỗ trợ chỉnh giúp anh chị nhé."'],
    ['Sau 3 tháng', 'Nhắn hỏi thăm + nhắc lau chùi',
     '"Em gửi anh/chị mẹo vệ sinh kính cho bền ạ. Anh/chị cần lau lại / chỉnh gọng cứ ghé em miễn phí nhé."'],
    ['Sau 6 tháng', 'Nhắc đi đo kiểm tra mắt định kỳ',
     '"Anh/chị, đến lịch kiểm tra mắt định kỳ rồi ạ. Anh/chị tiện ghé hôm nào em sắp xếp đo lại miễn phí kiểm tra độ?"'],
]
fu_table_data = [[Paragraph(r[0], style_body),
                   Paragraph(r[1], style_body),
                   Paragraph(f'<i>{r[2]}</i>', style_body)] for r in fu_data[1:]]
fu_table_data.insert(0, [Paragraph(f'<font color="white"><b>{fu_data[0][0]}</b></font>', style_body),
                          Paragraph(f'<font color="white"><b>{fu_data[0][1]}</b></font>', style_body),
                          Paragraph(f'<font color="white"><b>{fu_data[0][2]}</b></font>', style_body)])

fu_table = Table(fu_table_data, colWidths=[2.5*cm, 4.5*cm, 9*cm])
fu_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), COLOR_TABLE_HEAD),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
    ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
]))
story.append(fu_table)

story.append(Spacer(1, 12))
story.append(Paragraph('6.2 — Với khách "về suy nghĩ" (chưa mua)', style_h3))
story.extend(bullets([
    '<b>Sau 3 ngày:</b> Nhắn 1 tin hỏi thăm + gửi thông tin sản phẩm khách đã xem.',
    '<b>Sau 1 tuần:</b> Mời quay lại nếu có chương trình mới.',
    '<b>Không spam, không gọi liên tục</b> — 2 lần là tối đa nếu khách không phản hồi.',
]))

story.append(Spacer(1, 10))
story.append(Paragraph('6.3 — Cách lưu thông tin', style_h3))
story.append(Paragraph('Mỗi khách phải có hồ sơ ghi:', style_body))
story.extend(bullets([
    'Tên, SĐT',
    'Ngày mua, sản phẩm, số tiền',
    'Độ kính, sở thích gọng, đặc điểm cá nhân (con cái, công việc — để lần sau nhắc cho thân)',
    'Ngày follow-up tiếp theo',
]))

story.append(Spacer(1, 10))
story.append(criteria_box([
    'Đã đặt lịch nhắc 1 tuần / 3 tháng / 6 tháng.',
    'Hồ sơ khách đầy đủ trong CRM / Excel.',
]))

story.append(PageBreak())

# ── 10 NGUYÊN TẮC VÀNG ──────────────────────────────────────
story.append(Paragraph('PHỤ LỤC A — 10 NGUYÊN TẮC VÀNG', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_GOLD))
story.append(Spacer(1, 10))

principles = [
    'Khách đến — <b>KHÔNG bán ngay</b>. Xây quan hệ tin cậy trước.',
    'Bán bằng <b>câu hỏi</b>, không bán bằng giới thiệu.',
    'Nói <b>lợi ích</b>, không nói tính năng suông.',
    '<b>Chỉ nói</b> những lợi ích khách quan tâm.',
    '<b>Quà nhỏ luôn có trong tay</b> — móc khoá, khăn lau, nước rửa kính.',
    '<b>Im lặng sau khi báo giá</b> — để khách phản ứng trước.',
    'Bị chê đắt → <b>không hạ giá ngay</b> — phải hỏi "đắt so với gì?".',
    'Khách về tay không → <b>vẫn tặng quà + giữ thông tin</b> + lịch follow-up.',
    '<b>Hồ sơ khách hàng</b> là tài sản — phải ghi ngay, không nhớ vo.',
    'Follow-up đều: <b>1 tuần / 3 tháng / 6 tháng</b>.',
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

# ── BẢNG TỰ ĐÁNH GIÁ ────────────────────────────────────────
story.append(Paragraph('PHỤ LỤC B — BẢNG TỰ ĐÁNH GIÁ DÀNH CHO NHÂN VIÊN MỚI', style_h1))
story.append(HRFlowable(width="100%", thickness=2, color=COLOR_PRIMARY))
story.append(Spacer(1, 8))

story.append(Paragraph(
    'Sau mỗi ca, tự chấm 1–5 điểm cho từng mục (1 = chưa làm được, 5 = thuần thục):',
    style_body))
story.append(Spacer(1, 8))

eval_items = [
    'Tôi chào khách đúng script chưa?',
    'Tôi đã mời khách ngồi, tặng quà nhỏ chưa?',
    'Tôi đã hỏi đủ bộ câu hỏi xác định nhu cầu chưa?',
    'Tôi có nói tính năng kèm lợi ích không, hay chỉ kể tính năng suông?',
    'Tôi đã ướm thử nâng đơn chưa?',
    'Tôi đã báo giá kèm bảo hành + quà tặng + ưu đãi chưa?',
    'Tôi xử lý từ chối có theo đúng nguyên tắc "đồng cảm trước, lật sau" không?',
    'Tôi đã lưu hồ sơ + đặt lịch follow-up chưa?',
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
    ('FONTSIZE', (0,0), (-1,-1), 11),
    ('ALIGN', (0,0), (0,-1), 'CENTER'),
    ('ALIGN', (2,0), (-1,-1), 'CENTER'),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8F9FA')]),
]))
story.append(ev_table)

story.append(Spacer(1, 16))
story.append(Paragraph('Cách đọc kết quả:', style_h3))

result_data = [
    ['Tổng điểm', 'Nhận xét'],
    ['Dưới 25', 'Cần đọc lại cẩm nang + đi cùng anh/chị có kinh nghiệm trong 1 tuần.'],
    ['25 – 32', 'Đang đi đúng hướng, tiếp tục luyện.'],
    ['Trên 32', 'Đã thuần thục — bắt đầu kèm nhân viên mới.'],
]
result_table_data = [[Paragraph(r[0], style_body), Paragraph(r[1], style_body)] for r in result_data[1:]]
result_table_data.insert(0, [Paragraph(f'<font color="white"><b>{result_data[0][0]}</b></font>', style_body),
                              Paragraph(f'<font color="white"><b>{result_data[0][1]}</b></font>', style_body)])
res_table = Table(result_table_data, colWidths=[4*cm, 12*cm])
res_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), COLOR_TABLE_HEAD),
    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 8),
    ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ('LEFTPADDING', (0,0), (-1,-1), 10),
]))
story.append(res_table)

story.append(Spacer(1, 30))
story.append(HRFlowable(width="100%", thickness=1, color=colors.grey))
story.append(Spacer(1, 8))
story.append(Paragraph(
    '<i>Tài liệu nội bộ — Phiên bản 1.1 — Vui lòng không sao chép ra ngoài.</i>',
    ParagraphStyle('foot', fontName='Calibri-Italic', fontSize=10,
                   textColor=colors.grey, alignment=TA_CENTER)))

# ─── Build document ───────────────────────────────────────────
OUTPUT = r"D:\Sơn Brain\Sơn Brain\raw\SOP\SOP bán hàng 8+2 tại cửa hàng\Cam-Nang-Ban-Hang-v3.pdf"

class MyDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        # Cover frame (full page)
        cover_frame = Frame(2*cm, 2*cm, A4[0]-4*cm, A4[1]-4*cm,
                            id='cover', leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        # Content frame
        content_frame = Frame(2.5*cm, 2*cm, A4[0]-5*cm, A4[1]-3.5*cm,
                              id='content', leftPadding=0, rightPadding=0,
                              topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id='cover', frames=cover_frame, onPage=on_cover),
            PageTemplate(id='content', frames=content_frame, onPage=on_page),
        ])

doc = MyDocTemplate(OUTPUT, pagesize=A4,
                    title='Cẩm Nang Bán Hàng tại Cửa Hàng',
                    author='Cửa hàng kính mắt')

# Insert NextPageTemplate marker before page 2
from reportlab.platypus import NextPageTemplate
# Find first PageBreak and insert NextPageTemplate before it
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
import sys
print("PDF created successfully.")
print("Output path bytes:", OUTPUT.encode('utf-8'))
