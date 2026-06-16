#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
text_to_chunks.py — Cắt mọi loại text dài thành chunk có YAML metadata

Tự động phát hiện 3 loại input:
1. SRT      — có timecode --> 
2. BOOK     — có cấu trúc Chapter/Part/Phần/Chương
3. PLAIN    — text thuần (transcript thô, bài viết)

Output: file txt ~10,000 ký tự có YAML đồng nhất, sẵn sàng cho Vòng 2-3.

Usage:
    python3 text_to_chunks.py input.srt --ngay-giang 2024-08-15
    python3 text_to_chunks.py book.txt --loai BOOK --tieu-de "The System"
    python3 text_to_chunks.py raw.txt --loai PLAIN --nguon "Buổi nói chuyện X"
    python3 text_to_chunks.py file.txt   # tự detect
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH
# ============================================================

CHUNK_SIZE_TARGET = 15000
TIME_MARK_INTERVAL_SEC = 180  # SRT: chèn timecode mỗi 3 phút

# Marker auto-detect (tiếng Việt + một phần tiếng Anh)
MARKER_PATTERNS = {
    'BAI_TAP': [
        r'\b(bài tập|bài thực hành|làm bài|thực hành ngay|lấy giấy ra|viết ra|ghi ra)\b',
        r'\b(anh chị làm|các bạn làm|bây giờ làm)\b',
        r'\b(exercise|practice|write down)\b',
    ],
    'CASE_STUDY': [
        r'\b(ví dụ|case study|câu chuyện|có một (anh|chị|bạn|học viên|người))\b',
        r'\b(kể cho|kể chuyện|chuyện là)\b',
        r'\b(for example|here\'s a story|let me share)\b',
    ],
    'CAU_CHOT': [
        r'\b(nhớ cho|ghi nhớ|chốt lại|kết luận|điều quan trọng nhất|quy luật)\b',
        r'\b(đây là|chính là) (cái|điều|chìa khóa)\b',
        r'\b(key point|remember this|the key idea)\b',
    ],
    'CAU_HOI_HV': [
        r'\b(học viên hỏi|có bạn hỏi|câu hỏi|anh ơi|chị ơi)\b',
    ],
    'BREAK': [
        r'\b(nghỉ giải lao|break|nghỉ \d+ phút|tea break)\b',
    ],
}

MARKER_SYMBOLS = {
    'BAI_TAP':    '>>> BÀI TẬP <<<',
    'CASE_STUDY': '### CASE STUDY ###',
    'CAU_CHOT':   '*** CÂU CHỐT ***',
    'CAU_HOI_HV': '??? CÂU HỎI HỌC VIÊN ???',
    'BREAK':      '--- BREAK ---',
}

# Pattern phát hiện chương (cho BOOK + transcript có cấu trúc)
CHAPTER_PATTERNS = [
    r'^(Chapter|CHAPTER)\s+\d+',
    r'^(Chương|CHƯƠNG)\s+\d+',
    r'^(Part|PART)\s+[IVX]+',
    r'^(Phần|PHẦN)\s+[IVX\d]+',
    r'^(Bài|BÀI)\s+\d+',
    r'^(Section|SECTION)\s+\d+',
    r'^(Ngày|NGÀY|Day|DAY)\s+\d+\s*$',
    r'^(Buổi|BUỔI)\s+\d+',
]

# ============================================================
# PARSE SRT
# ============================================================

def parse_srt_time(ts: str) -> float:
    ts = ts.strip().replace(',', '.')
    h, m, s = ts.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def seconds_to_hms(sec: float) -> str:
    sec = int(sec)
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_srt(content: str):
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    blocks = re.split(r'\n\s*\n', content.strip())
    segments = []
    for block in blocks:
        lines = [l for l in block.split('\n') if l.strip()]
        if len(lines) < 2:
            continue
        ts_idx = None
        for i, line in enumerate(lines):
            if '-->' in line:
                ts_idx = i
                break
        if ts_idx is None:
            continue
        try:
            start_str, end_str = lines[ts_idx].split('-->')
            start = parse_srt_time(start_str)
            end = parse_srt_time(end_str)
        except Exception:
            continue
        text = ' '.join(lines[ts_idx + 1:]).strip()
        if text:
            segments.append({'start': start, 'end': end, 'text': text})
    return segments

# ============================================================
# DETECT LOẠI FILE
# ============================================================

def detect_input_type(content: str, filename: str = ''):
    """
    Trả về 'SRT' | 'BOOK' | 'PLAIN'
    """
    # Check SRT: có ít nhất 3 dòng timestamp -->
    srt_count = len(re.findall(r'\d{2}:\d{2}:\d{2}[,\.]\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}[,\.]\d{3}', content))
    if srt_count >= 3:
        return 'SRT'
    
    # Check BOOK: có ít nhất 2 chapter/part marker
    chapter_count = 0
    for line in content.split('\n'):
        line_stripped = line.strip()
        for pattern in CHAPTER_PATTERNS:
            if re.match(pattern, line_stripped, re.IGNORECASE):
                chapter_count += 1
                break
        if chapter_count >= 2:
            return 'BOOK'
    
    # Check trên 1 dòng dài (file viết liền không xuống dòng)
    long_line_chapters = 0
    for pattern in CHAPTER_PATTERNS:
        long_line_chapters += len(re.findall(pattern, content, re.IGNORECASE | re.MULTILINE))
    if long_line_chapters >= 2:
        return 'BOOK'
    
    return 'PLAIN'

# ============================================================
# DETECT MARKER
# ============================================================

def detect_markers(text: str):
    text_lower = text.lower()
    detected = []
    for marker_type, patterns in MARKER_PATTERNS.items():
        for p in patterns:
            if re.search(p, text_lower, re.IGNORECASE):
                detected.append(marker_type)
                break
    return detected

# ============================================================
# CHUNK CHO SRT
# ============================================================

def build_chunks_srt(segments, target_size=CHUNK_SIZE_TARGET):
    size_min = int(target_size * 0.8)
    size_max = int(target_size * 1.2)
    chunks = []
    current = {'segments': [], 'char_count': 0, 'start': None, 'end': None}
    for seg in segments:
        if current['start'] is None:
            current['start'] = seg['start']
        current['segments'].append(seg)
        current['char_count'] += len(seg['text']) + 1
        current['end'] = seg['end']
        should_cut = False
        if current['char_count'] >= size_max:
            should_cut = True
        elif current['char_count'] >= size_min:
            text_end = seg['text'].rstrip()
            if text_end and text_end[-1] in '.!?':
                should_cut = True
        if should_cut:
            chunks.append(current)
            current = {'segments': [], 'char_count': 0, 'start': None, 'end': None}
    if current['segments']:
        chunks.append(current)
    return chunks

def render_chunk_srt(chunk, time_mark_interval=TIME_MARK_INTERVAL_SEC):
    lines = []
    last_mark_time = chunk['start'] - time_mark_interval
    last_marker_pos = -1
    buffer_text = []
    for i, seg in enumerate(chunk['segments']):
        if seg['start'] - last_mark_time >= time_mark_interval:
            if buffer_text:
                lines.append(' '.join(buffer_text))
                buffer_text = []
            lines.append('')
            lines.append(f"[{seconds_to_hms(seg['start'])}]")
            last_mark_time = seg['start']
        markers = detect_markers(seg['text'])
        if markers and i - last_marker_pos > 3:
            if buffer_text:
                lines.append(' '.join(buffer_text))
                buffer_text = []
            for m in markers[:1]:
                lines.append(MARKER_SYMBOLS[m])
            last_marker_pos = i
        buffer_text.append(seg['text'])
    if buffer_text:
        lines.append(' '.join(buffer_text))
    return '\n'.join(lines)

# ============================================================
# CHUNK CHO TEXT (BOOK + PLAIN)
# ============================================================

def split_text_into_units(text: str, mode='PLAIN'):
    """
    Chia text thành các 'unit' (đơn vị nhỏ nhất không nên cắt giữa).
    
    Tự phát hiện 3 dạng cấu trúc:
    - PARAGRAPH:  có blank line giữa các đoạn (sách thường, bài viết)
    - ASR:        mỗi dòng = 1 câu ngắn không dấu câu (transcript CapCut/Whisper)
    - CONTINUOUS: 1 dòng dài viết liền (ebook export 1-line)
    """
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Đếm số paragraph (block cách nhau bằng blank line)
    paragraphs = re.split(r'\n\s*\n', text.strip())
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    total_lines = text.count('\n') + 1
    
    # Phát hiện ASR: nhiều dòng (>200), trung bình rất ngắn (<80 ký tự/dòng), ít blank line
    is_asr = (
        total_lines > 200
        and len(paragraphs) < total_lines / 10  # Ít block paragraph so với số dòng
        and (len(text) / total_lines) < 80      # Mỗi dòng trung bình < 80 ký tự
    )
    
    if is_asr:
        return _split_asr_transcript(text)
    
    # Phát hiện CONTINUOUS: 1-3 paragraph nhưng tổng dài
    if len(paragraphs) <= 3 and sum(len(p) for p in paragraphs) > 20000:
        return _split_continuous_text(text)
    
    # PARAGRAPH (default): xử lý theo paragraph
    return _split_by_paragraph(paragraphs)


def _split_asr_transcript(text: str):
    """ASR: mỗi dòng = 1 segment ngắn, gom thành 'câu logic' theo nhóm dòng."""
    units = []
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    GROUP_SIZE = 6  # Gộp ~6 dòng thành 1 unit logic (~1 câu hoàn chỉnh)
    
    i = 0
    while i < len(lines):
        # Check chapter marker
        is_chapter = False
        for pattern in CHAPTER_PATTERNS:
            if re.match(pattern, lines[i], re.IGNORECASE):
                is_chapter = True
                break
        
        if is_chapter:
            # Chapter marker đứng riêng 1 unit
            units.append({
                'text': lines[i],
                'is_chapter_start': True,
                'is_paragraph_end': True,
            })
            i += 1
            continue
        
        # Gom GROUP_SIZE dòng thành 1 unit
        group = lines[i:i + GROUP_SIZE]
        # Nhưng dừng sớm nếu gặp chapter marker
        actual_size = 0
        for j, line in enumerate(group):
            stop = False
            for pattern in CHAPTER_PATTERNS:
                if re.match(pattern, line, re.IGNORECASE):
                    stop = True
                    break
            if stop:
                actual_size = j
                break
            actual_size = j + 1
        
        if actual_size > 0:
            grouped_text = ' '.join(lines[i:i + actual_size])
            units.append({
                'text': grouped_text,
                'is_chapter_start': False,
                'is_paragraph_end': True,
            })
            i += actual_size
        else:
            i += 1
    
    return units


def _split_continuous_text(text: str):
    """1-line dài: tách bằng chapter marker rồi tách câu."""
    units = []
    text_with_marker = text
    for p in CHAPTER_PATTERNS:
        text_with_marker = re.sub(
            f'({p})',
            r'\n\n___CHAPTER_BREAK___\1',
            text_with_marker,
            flags=re.IGNORECASE | re.MULTILINE,
        )
    sections = text_with_marker.split('___CHAPTER_BREAK___')
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZĐ"\'])', sec)
        for i, sent in enumerate(sentences):
            sent = sent.strip()
            if sent:
                units.append({
                    'text': sent,
                    'is_chapter_start': i == 0,
                    'is_paragraph_end': True,
                })
    return units


def _split_by_paragraph(paragraphs):
    """Mặc định: theo paragraph có blank line."""
    units = []
    for para in paragraphs:
        is_chapter_start = False
        first_line = para.split('\n')[0].strip()
        for pattern in CHAPTER_PATTERNS:
            if re.match(pattern, first_line, re.IGNORECASE):
                is_chapter_start = True
                break
        
        if len(para) > 5000:
            sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZĐ])', para)
            for i, sent in enumerate(sentences):
                if sent.strip():
                    units.append({
                        'text': sent.strip(),
                        'is_chapter_start': is_chapter_start and i == 0,
                        'is_paragraph_end': i == len(sentences) - 1,
                    })
        else:
            units.append({
                'text': para,
                'is_chapter_start': is_chapter_start,
                'is_paragraph_end': True,
            })
    return units

def build_chunks_text(units, target_size=CHUNK_SIZE_TARGET):
    """
    Gom unit thành chunk.
    Quy tắc:
    - Ưu tiên cắt ở chương (is_chapter_start=True của unit kế tiếp)
    - Nếu trong khoảng [90%, 110%] target → cắt ở cuối paragraph
    - Vượt 110% → bắt buộc cắt
    """
    size_min = int(target_size * 0.90)
    size_max = int(target_size * 1.10)
    chunks = []
    current = {'units': [], 'char_count': 0, 'start_idx': None, 'chapter_marker': None}
    
    for i, unit in enumerate(units):
        # Nếu unit này là start của chapter MỚI và chunk hiện tại đã có nội dung
        # và đã đủ size_min → cắt ở đây
        if (unit['is_chapter_start']
                and current['units']
                and current['char_count'] >= size_min):
            chunks.append(current)
            current = {'units': [], 'char_count': 0, 'start_idx': None, 'chapter_marker': None}
        
        if current['start_idx'] is None:
            current['start_idx'] = i
            if unit['is_chapter_start']:
                # Lấy dòng đầu làm chapter marker
                current['chapter_marker'] = unit['text'].split('\n')[0][:100]
        
        current['units'].append(unit)
        current['char_count'] += len(unit['text']) + 2  # +2 cho \n\n
        
        should_cut = False
        if current['char_count'] >= size_max:
            should_cut = True
        elif current['char_count'] >= size_min and unit['is_paragraph_end']:
            should_cut = True
        
        if should_cut:
            chunks.append(current)
            current = {'units': [], 'char_count': 0, 'start_idx': None, 'chapter_marker': None}
    
    if current['units']:
        chunks.append(current)
    return chunks

def render_chunk_text(chunk, mode='PLAIN'):
    """Render chunk BOOK/PLAIN với marker auto-detect"""
    lines = []
    
    for i, unit in enumerate(chunk['units']):
        # Detect marker — mỗi paragraph được check độc lập
        # (khác với SRT vì paragraph dài, tự nhiên có khoảng cách)
        markers = detect_markers(unit['text'])
        if markers:
            lines.append('')
            lines.append(MARKER_SYMBOLS[markers[0]])
        lines.append(unit['text'])
        lines.append('')
    
    return '\n'.join(lines).strip()

# ============================================================
# YAML METADATA
# ============================================================

KHOA_FULL_NAMES = {
    'SSS': 'Sales Success System',
    'IPS': 'Internet Power System',
    'EAGLE': 'Eagle Camp',
    'LTVM': 'Lập Trình Vận Mệnh',
    'DTSGC': 'Đánh Thức Sự Giàu Có',
    'UT': 'Ultimate Trainer',
    'YES': 'YES Summit',
}

def parse_filename_metadata(filename: str):
    name = Path(filename).stem
    parts = name.split('_')
    meta = {'khoa': None, 'ngay': None, 'dia_diem': None}
    if len(parts) >= 1:
        first = parts[0].upper()
        if first in KHOA_FULL_NAMES:
            meta['khoa'] = first
    if len(parts) >= 4:
        meta['dia_diem'] = parts[3]
    for p in parts:
        m = re.match(r'^[Dd](\d+)$', p)
        if m:
            meta['ngay'] = int(m.group(1))
            break
    return meta

def build_yaml_srt(file_id, meta, chunk, idx, total, srt_filename, char_count):
    khoa = meta.get('khoa', 'UNKNOWN')
    return f"""---
# === LOẠI INPUT ===
loai_input: SRT

# === METADATA FILE ===
file_id: {file_id}
khoa: {khoa}
ten_day_du: {KHOA_FULL_NAMES.get(khoa, khoa)}
ngay_giang: {meta.get('ngay_giang', 'TODO')}
dia_diem: {meta.get('dia_diem', 'TODO')}
ngay_trong_khoa: {meta.get('ngay', 'TODO')}
chunk_so: {idx + 1}
tong_chunk: {total}
file_goc: {srt_filename}
timecode_chunk:
  bat_dau: "{seconds_to_hms(chunk['start'])}"
  ket_thuc: "{seconds_to_hms(chunk['end'])}"
thoi_luong_phut: {round((chunk['end'] - chunk['start']) / 60, 1)}
so_ky_tu: {char_count}

# === TAG CHỦ ĐỀ (Vòng 2 sẽ điền) ===
chu_de_chinh: []
chu_de_phu: []

# === LIÊN KẾT PHI TUYẾN (Vòng 2 sẽ điền) ===
noi_tiep_tu: null
noi_tiep_sang: null
nhac_lai_o: []
bo_sung_cho: null
la_lan_dau_noi: null

# === TÌNH TRẠNG ===
trang_thai: cleaned
nguoi_xu_ly: auto-script
ngay_xu_ly: {datetime.now().strftime('%Y-%m-%d')}
ghi_chu: ""
---
"""

def build_yaml_book(file_id, meta, chunk, idx, total, src_filename, char_count):
    khoa = meta.get('khoa', '')
    khoa_line = f"khoa: {khoa}\nten_khoa_day_du: {KHOA_FULL_NAMES.get(khoa, khoa) if khoa else ''}\n" if khoa else ""
    return f"""---
# === LOẠI INPUT ===
loai_input: BOOK

# === METADATA FILE ===
file_id: {file_id}
{khoa_line}tieu_de: {meta.get('tieu_de', 'TODO')}
tac_gia: {meta.get('tac_gia', 'TODO')}
the_loai: {meta.get('the_loai', 'sách')}
ngon_ngu: {meta.get('ngon_ngu', 'TODO')}
ngay_giang: {meta.get('ngay_giang', '')}
chunk_so: {idx + 1}
tong_chunk: {total}
file_goc: {src_filename}
chuong_marker: "{chunk.get('chapter_marker') or ''}"
so_ky_tu: {char_count}

# === TAG CHỦ ĐỀ (Vòng 2 sẽ điền) ===
chu_de_chinh: []
chu_de_phu: []

# === LIÊN KẾT PHI TUYẾN (Vòng 2 sẽ điền) ===
noi_tiep_tu: null
noi_tiep_sang: null
nhac_lai_o: []
bo_sung_cho: null
la_lan_dau_noi: null

# === TÌNH TRẠNG ===
trang_thai: cleaned
nguoi_xu_ly: auto-script
ngay_xu_ly: {datetime.now().strftime('%Y-%m-%d')}
ghi_chu: ""
---
"""

def build_yaml_plain(file_id, meta, chunk, idx, total, src_filename, char_count):
    return f"""---
# === LOẠI INPUT ===
loai_input: PLAIN

# === METADATA FILE ===
file_id: {file_id}
nguon: {meta.get('nguon', 'TODO')}
mo_ta: {meta.get('mo_ta', '')}
chunk_so: {idx + 1}
tong_chunk: {total}
file_goc: {src_filename}
so_ky_tu: {char_count}

# === TAG CHỦ ĐỀ (Vòng 2 sẽ điền) ===
chu_de_chinh: []
chu_de_phu: []

# === LIÊN KẾT PHI TUYẾN (Vòng 2 sẽ điền) ===
noi_tiep_tu: null
noi_tiep_sang: null
nhac_lai_o: []
bo_sung_cho: null
la_lan_dau_noi: null

# === TÌNH TRẠNG ===
trang_thai: cleaned
nguoi_xu_ly: auto-script
ngay_xu_ly: {datetime.now().strftime('%Y-%m-%d')}
ghi_chu: ""
---
"""

# ============================================================
# MAIN
# ============================================================

def slugify(s: str) -> str:
    """Tạo slug an toàn cho tên file"""
    s = re.sub(r'[^a-zA-Z0-9]+', '_', s.lower())[:30]
    return s.strip('_') or 'file'


# ============================================================
# AUDIT — file phụ giám sát chất lượng
# ============================================================

def write_manifest(output_dir, src_filename, src_input_chars, detected_type,
                   meta, chunk_records):
    """
    Sinh manifest.json — bản đồ toàn bộ chunk.
    AI agents và Obsidian dùng file này để hiểu cấu trúc dataset.
    """
    import json
    
    manifest = {
        'schema_version': '1.0',
        'generated_at': datetime.now().isoformat(),
        'source': {
            'filename': src_filename,
            'detected_type': detected_type,
            'input_chars_total': src_input_chars,
        },
        'metadata': meta,
        'chunks_summary': {
            'total': len(chunk_records),
            'avg_chars': round(sum(c['so_ky_tu'] for c in chunk_records) / len(chunk_records)) if chunk_records else 0,
            'min_chars': min((c['so_ky_tu'] for c in chunk_records), default=0),
            'max_chars': max((c['so_ky_tu'] for c in chunk_records), default=0),
        },
        'chunks': chunk_records,
    }
    
    manifest_path = output_dir / 'manifest.json'
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    return manifest_path


def write_summary_report(output_dir, src_filename, src_input_chars,
                         total_output_chars, detected_type, chunk_records,
                         hard_split_warnings):
    """
    Sinh summary_report.md — phiếu kiểm tra chất lượng.
    Cho người dùng nhìn nhanh xem có lỗi mất dữ liệu không.
    """
    delta = total_output_chars - src_input_chars
    delta_pct = (delta / src_input_chars * 100) if src_input_chars else 0
    
    # Phán định trạng thái
    if abs(delta_pct) < 5:
        status_icon = '✅'
        status_text = 'TỐT — chênh lệch trong ngưỡng cho phép (<5%)'
    elif abs(delta_pct) < 15:
        status_icon = '⚠️'
        status_text = 'CHÚ Ý — chênh lệch trung bình (5-15%), nên kiểm tra'
    else:
        status_icon = '❌'
        status_text = 'LỖI — chênh lệch lớn (>15%), kiểm tra ngay!'
    
    # Top 5 chunk lệch nhất so với target
    target_size = 15000  # default; có thể truyền vào sau
    chunk_records_sorted = sorted(
        chunk_records,
        key=lambda c: abs(c['so_ky_tu'] - target_size),
        reverse=True,
    )[:5]
    
    lines = [
        f"# Báo cáo cắt chunk — {src_filename}",
        f"",
        f"_Sinh tự động lúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_",
        f"",
        f"## Tổng quan",
        f"",
        f"| Chỉ số | Giá trị |",
        f"|---|---|",
        f"| File gốc | `{src_filename}` |",
        f"| Loại đã phát hiện | **{detected_type}** |",
        f"| Số ký tự input (text thuần) | {src_input_chars:,} |",
        f"| Số ký tự output (tổng các chunk) | {total_output_chars:,} |",
        f"| Chênh lệch (delta) | {delta:+,} ({delta_pct:+.2f}%) |",
        f"| Số chunk đã sinh | {len(chunk_records)} |",
        f"| Cảnh báo hard-split | {len(hard_split_warnings)} chunk |",
        f"",
        f"## Trạng thái: {status_icon} {status_text}",
        f"",
        f"## Diễn giải chênh lệch (delta)",
        f"",
    ]
    
    if delta < -src_input_chars * 0.05:
        lines.append(f"⚠️ **Output ÍT HƠN input {abs(delta):,} ký tự ({abs(delta_pct):.2f}%).**")
        lines.append(f"")
        lines.append(f"Nguyên nhân khả nghi:")
        lines.append(f"- Một số segment SRT bị bỏ qua khi parse (timecode lỗi format)")
        lines.append(f"- Đoạn text trùng lặp trong source bị merge khi gom chunk")
        lines.append(f"- Lỗi encoding ở vài đoạn")
        lines.append(f"")
        lines.append(f"**Cần kiểm tra thủ công 1-2 chunk so với SRT gốc.**")
    elif delta > src_input_chars * 0.05:
        lines.append(f"ℹ️ Output NHIỀU HƠN input {delta:,} ký tự ({delta_pct:+.2f}%).")
        lines.append(f"")
        lines.append(f"Đây là bình thường — script đã thêm:")
        lines.append(f"- Dòng timecode `[hh:mm:ss]` mỗi 3 phút")
        lines.append(f"- Marker `>>> BÀI TẬP <<<`, `### CASE STUDY ###`, ...")
        lines.append(f"- Dòng trống phân cách")
        lines.append(f"- YAML header (~600 ký tự/file)")
    else:
        lines.append(f"✅ Output gần bằng input — không có dấu hiệu mất dữ liệu.")
    
    lines.extend([
        f"",
        f"## Thống kê chunk",
        f"",
        f"| Chỉ số | Giá trị |",
        f"|---|---|",
        f"| Trung bình | {round(sum(c['so_ky_tu'] for c in chunk_records) / len(chunk_records)):,} kt |",
        f"| Nhỏ nhất | {min(c['so_ky_tu'] for c in chunk_records):,} kt |",
        f"| Lớn nhất | {max(c['so_ky_tu'] for c in chunk_records):,} kt |",
        f"",
    ])
    
    if hard_split_warnings:
        lines.append(f"## ⚠️ Cảnh báo hard-split ({len(hard_split_warnings)} chunk)")
        lines.append(f"")
        lines.append(f"Các chunk sau bị cắt giữa câu/đoạn (không tìm được ranh giới tự nhiên):")
        lines.append(f"")
        for w in hard_split_warnings:
            lines.append(f"- `{w['file_id']}` — {w['reason']}")
        lines.append(f"")
    
    if chunk_records_sorted:
        lines.append(f"## Top 5 chunk lệch xa target ({target_size} kt)")
        lines.append(f"")
        lines.append(f"| File | Ký tự | Lệch | Ghi chú |")
        lines.append(f"|---|---|---|---|")
        for c in chunk_records_sorted:
            diff = c['so_ky_tu'] - target_size
            note = ''
            if c['so_ky_tu'] < target_size * 0.5:
                note = '⚠️ Quá ngắn'
            elif c['so_ky_tu'] > target_size * 1.5:
                note = '⚠️ Quá dài'
            lines.append(f"| `{c['file_id']}` | {c['so_ky_tu']:,} | {diff:+,} | {note} |")
        lines.append(f"")
    
    lines.extend([
        f"## Hành động đề xuất",
        f"",
    ])
    if abs(delta_pct) > 15:
        lines.append(f"1. **KHÔNG dùng output này cho Vòng 2/3** — kiểm tra lỗi parse trước")
        lines.append(f"2. Mở SRT gốc, đối chiếu với chunk đầu/cuối")
        lines.append(f"3. Nếu là SRT thì kiểm tra format timecode")
    elif abs(delta_pct) > 5:
        lines.append(f"1. Spot-check 2-3 chunk so với source")
        lines.append(f"2. Nếu nội dung khớp → dùng được cho Vòng 2/3")
        lines.append(f"3. Nếu không khớp → báo Claude để debug")
    else:
        lines.append(f"✅ Sẵn sàng cho Vòng 2 (tag chủ đề) và Vòng 3 (viết module)")
    
    report_path = output_dir / 'summary_report.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return report_path

def main():
    parser = argparse.ArgumentParser(description='Cắt mọi loại text dài thành chunk có YAML')
    parser.add_argument('input', help='File input (.srt hoặc .txt)')
    parser.add_argument('--loai', choices=['SRT', 'BOOK', 'PLAIN', 'AUTO'], default='AUTO',
                        help='Loại file. Mặc định AUTO (tự phát hiện)')
    parser.add_argument('--output-dir', default=None)
    parser.add_argument('--chunk-size', type=int, default=CHUNK_SIZE_TARGET)
    
    # SRT params
    parser.add_argument('--khoa', default=None)
    parser.add_argument('--ngay', type=int, default=None)
    parser.add_argument('--dia-diem', default=None)
    parser.add_argument('--ngay-giang', default=None)
    
    # BOOK params
    parser.add_argument('--tieu-de', default=None)
    parser.add_argument('--tac-gia', default=None)
    parser.add_argument('--the-loai', default=None)
    parser.add_argument('--ngon-ngu', default=None)
    
    # PLAIN params
    parser.add_argument('--nguon', default=None)
    parser.add_argument('--mo-ta', default=None)
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"❌ Không tìm thấy: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📂 File: {args.input} ({len(content):,} ký tự)")
    
    # Detect type
    if args.loai == 'AUTO':
        detected_type = detect_input_type(content, args.input)
        print(f"🔍 Tự phát hiện loại: {detected_type}")
    else:
        detected_type = args.loai
        print(f"🏷️  Loại (theo tham số): {detected_type}")
    
    # Output dir
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path('output') / Path(args.input).stem
    output_dir.mkdir(parents=True, exist_ok=True)
    
    src_filename = os.path.basename(args.input)
    
    # Theo dõi để sinh manifest + summary
    chunk_records = []
    hard_split_warnings = []
    
    # ====== SRT branch ======
    if detected_type == 'SRT':
        segments = parse_srt(content)
        print(f"📊 Parse được {len(segments)} segment SRT")
        if not segments:
            print("❌ File khai báo SRT nhưng không parse được. Thử --loai PLAIN.", file=sys.stderr)
            sys.exit(1)
        total_dur = segments[-1]['end'] - segments[0]['start']
        print(f"⏱️  Tổng thời lượng: {total_dur/60:.1f} phút")
        
        # Tổng ký tự text thuần (input)
        src_text_chars = sum(len(s['text']) for s in segments)
        
        chunks = build_chunks_srt(segments, target_size=args.chunk_size)
        print(f"✂️  Chia thành {len(chunks)} chunk")
        
        auto_meta = parse_filename_metadata(args.input)
        meta = {
            'khoa': args.khoa or auto_meta['khoa'] or 'UNKNOWN',
            'ngay': args.ngay or auto_meta['ngay'] or 0,
            'dia_diem': args.dia_diem or auto_meta['dia_diem'] or 'TODO',
            'ngay_giang': args.ngay_giang or 'TODO',
        }
        print(f"🏷️  Metadata: {meta}")
        
        for i, chunk in enumerate(chunks):
            file_id = f"{meta['khoa']}_D{meta['ngay']}_C{i+1:02d}"
            body = render_chunk_srt(chunk)
            char_count = sum(len(s['text']) for s in chunk['segments'])
            yaml_h = build_yaml_srt(file_id, meta, chunk, i, len(chunks), src_filename, char_count)
            outf = output_dir / f"{file_id}.txt"
            with open(outf, 'w', encoding='utf-8') as f:
                f.write(yaml_h + '\n' + body + '\n')
            
            # Ghi nhận để audit
            chunk_records.append({
                'file_id': file_id,
                'filename': outf.name,
                'chunk_so': i + 1,
                'so_ky_tu': char_count,
                'so_segment': len(chunk['segments']),
                'timecode_bat_dau': seconds_to_hms(chunk['start']),
                'timecode_ket_thuc': seconds_to_hms(chunk['end']),
                'thoi_luong_phut': round((chunk['end'] - chunk['start']) / 60, 1),
            })
            
            # Cảnh báo nếu chunk vượt size_max (= hard split, không tìm được ranh giới)
            if char_count > args.chunk_size * 1.3:
                hard_split_warnings.append({
                    'file_id': file_id,
                    'reason': f'Vượt 30% target ({char_count:,} kt > {int(args.chunk_size * 1.3):,} kt)',
                })
            
            print(f"  ✅ {outf.name} — {char_count:,} kt, {seconds_to_hms(chunk['start'])} → {seconds_to_hms(chunk['end'])}")
        
        # Sinh file phụ
        manifest_meta = {**meta, 'tong_thoi_luong_phut': round(total_dur / 60, 1)}
        manifest_path = write_manifest(output_dir, src_filename, src_text_chars, detected_type, manifest_meta, chunk_records)
        report_path = write_summary_report(output_dir, src_filename, src_text_chars,
                                           sum(c['so_ky_tu'] for c in chunk_records),
                                           detected_type, chunk_records, hard_split_warnings)
    
    # ====== BOOK / PLAIN branch ======
    else:
        # Tổng ký tự input thực tế (text content sau khi strip)
        src_text_chars = len(content.strip())
        
        units = split_text_into_units(content, mode=detected_type)
        print(f"📊 Chia được {len(units)} đơn vị (paragraph/câu)")
        
        chunks = build_chunks_text(units, target_size=args.chunk_size)
        print(f"✂️  Chia thành {len(chunks)} chunk")
        
        if detected_type == 'BOOK':
            slug = slugify(args.tieu_de or Path(args.input).stem)
            meta = {
                'tieu_de': args.tieu_de or Path(args.input).stem,
                'tac_gia': args.tac_gia or 'TODO',
                'the_loai': args.the_loai or 'sách',
                'ngon_ngu': args.ngon_ngu or 'TODO',
                'khoa': args.khoa or '',
                'ngay_giang': args.ngay_giang or '',
            }
        else:  # PLAIN
            slug = slugify(args.nguon or Path(args.input).stem)
            meta = {
                'nguon': args.nguon or Path(args.input).stem,
                'mo_ta': args.mo_ta or '',
            }
        print(f"🏷️  Metadata: {meta}")
        
        for i, chunk in enumerate(chunks):
            prefix = 'BOOK' if detected_type == 'BOOK' else 'TEXT'
            file_id = f"{prefix}_{slug}_C{i+1:03d}"
            body = render_chunk_text(chunk, mode=detected_type)
            char_count = sum(len(u['text']) for u in chunk['units'])
            
            if detected_type == 'BOOK':
                yaml_h = build_yaml_book(file_id, meta, chunk, i, len(chunks), src_filename, char_count)
            else:
                yaml_h = build_yaml_plain(file_id, meta, chunk, i, len(chunks), src_filename, char_count)
            
            outf = output_dir / f"{file_id}.txt"
            with open(outf, 'w', encoding='utf-8') as f:
                f.write(yaml_h + '\n' + body + '\n')
            
            ch_marker = chunk.get('chapter_marker') or ''
            
            # Ghi nhận để audit
            chunk_records.append({
                'file_id': file_id,
                'filename': outf.name,
                'chunk_so': i + 1,
                'so_ky_tu': char_count,
                'so_unit': len(chunk['units']),
                'chuong_marker': ch_marker,
            })
            
            if char_count > args.chunk_size * 1.3:
                hard_split_warnings.append({
                    'file_id': file_id,
                    'reason': f'Vượt 30% target ({char_count:,} kt > {int(args.chunk_size * 1.3):,} kt)',
                })
            
            ch_info = f" [{ch_marker[:40]}]" if ch_marker else ''
            print(f"  ✅ {outf.name} — {char_count:,} kt{ch_info}")
        
        # Sinh file phụ
        manifest_path = write_manifest(output_dir, src_filename, src_text_chars, detected_type, meta, chunk_records)
        report_path = write_summary_report(output_dir, src_filename, src_text_chars,
                                           sum(c['so_ky_tu'] for c in chunk_records),
                                           detected_type, chunk_records, hard_split_warnings)
    
    # In tổng kết audit
    total_output = sum(c['so_ky_tu'] for c in chunk_records)
    delta = total_output - src_text_chars
    delta_pct = (delta / src_text_chars * 100) if src_text_chars else 0
    
    print(f"\n📊 KIỂM TRA CHẤT LƯỢNG")
    print(f"   Input (text thuần):  {src_text_chars:>10,} ký tự")
    print(f"   Output (tổng chunk): {total_output:>10,} ký tự")
    print(f"   Delta:               {delta:>+10,} ({delta_pct:+.2f}%)")
    
    if abs(delta_pct) < 5:
        print(f"   Trạng thái: ✅ TỐT")
    elif abs(delta_pct) < 15:
        print(f"   Trạng thái: ⚠️  CHÚ Ý — kiểm tra summary_report.md")
    else:
        print(f"   Trạng thái: ❌ LỖI — xem summary_report.md ngay!")
    
    if hard_split_warnings:
        print(f"   ⚠️  Cảnh báo hard-split: {len(hard_split_warnings)} chunk")
    
    print(f"\n📁 File phụ:")
    print(f"   manifest.json       — bản đồ chunk (cho AI agents)")
    print(f"   summary_report.md   — báo cáo cho người dùng")
    print(f"\n🎉 Xong! {len(chunks)} chunk + 2 file phụ trong: {output_dir}/")

if __name__ == '__main__':
    main()
