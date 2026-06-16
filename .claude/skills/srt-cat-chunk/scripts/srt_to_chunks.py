#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
srt_to_chunks.py — Vòng 1 pipeline xử lý transcript khóa học PTL

Input:  1 file .srt
Output: N file .txt trong thư mục output/
        Mỗi file ~10,000 ký tự, có YAML + timecode + marker auto-detect

Usage:
    python srt_to_chunks.py input.srt --khoa SSS --ngay 1 --dia-diem "Ha Noi" --ngay-giang 2024-08-15

Hoặc đơn giản nhất (script tự đọc tên file để đoán):
    python srt_to_chunks.py SSS_2024_08_HN_D1.srt
"""

import argparse
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ============================================================
# CẤU HÌNH — anh Long có thể chỉnh
# ============================================================

CHUNK_SIZE_TARGET = 10000      # Ký tự target cho 1 chunk
CHUNK_SIZE_MIN = 8000          # Tối thiểu, không cắt sớm hơn
CHUNK_SIZE_MAX = 12000         # Tối đa, phải cắt trước mức này
TIME_MARK_INTERVAL_SEC = 180   # Chèn timecode mỗi 3 phút

# Từ khóa để auto-detect MARKER trong nội dung
MARKER_PATTERNS = {
    'BAI_TAP': [
        r'\b(bài tập|bài thực hành|làm bài|thực hành ngay|lấy giấy ra|viết ra|ghi ra)\b',
        r'\b(anh chị làm|các bạn làm|bây giờ làm)\b',
    ],
    'CASE_STUDY': [
        r'\b(ví dụ|case study|câu chuyện|có một (anh|chị|bạn|học viên|người))\b',
        r'\b(kể cho|kể chuyện|chuyện là)\b',
    ],
    'CAU_CHOT': [
        r'\b(nhớ cho|ghi nhớ|chốt lại|kết luận|điều quan trọng nhất|quy luật)\b',
        r'\b(đây là|chính là) (cái|điều|chìa khóa)\b',
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

# ============================================================
# PARSE SRT
# ============================================================

def parse_srt_time(ts: str) -> float:
    """'01:23:45,678' -> giây (float)"""
    ts = ts.strip().replace(',', '.')
    h, m, s = ts.split(':')
    return int(h) * 3600 + int(m) * 60 + float(s)

def seconds_to_hms(sec: float) -> str:
    """123.45 -> '00:02:03'"""
    sec = int(sec)
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def parse_srt(content: str):
    """
    Parse SRT thành list các segment:
    [{'idx': 1, 'start': 0.0, 'end': 3.5, 'text': '...'}, ...]
    """
    # Chuẩn hóa line ending
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # Tách block bằng dòng trống
    blocks = re.split(r'\n\s*\n', content.strip())
    segments = []
    
    for block in blocks:
        lines = [l for l in block.split('\n') if l.strip()]
        if len(lines) < 2:
            continue
        
        # Tìm dòng có timestamp (--> )
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
        if not text:
            continue
        
        segments.append({
            'start': start,
            'end': end,
            'text': text,
        })
    
    return segments

# ============================================================
# DETECT MARKER
# ============================================================

def detect_markers(text: str):
    """Trả về list các marker được phát hiện trong đoạn text"""
    text_lower = text.lower()
    detected = []
    for marker_type, patterns in MARKER_PATTERNS.items():
        for p in patterns:
            if re.search(p, text_lower, re.IGNORECASE):
                detected.append(marker_type)
                break
    return detected

# ============================================================
# CHUNKING — chia theo ranh giới câu, không cắt giữa
# ============================================================

def split_into_sentences(text: str):
    """Chia thô theo dấu câu tiếng Việt"""
    # Pattern: kết thúc câu = . ! ? + space + chữ hoa hoặc xuống dòng
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if p.strip()]

def build_chunks(segments, target_size=CHUNK_SIZE_TARGET):
    """
    Gom segment thành chunk ~target_size ký tự.
    Cố gắng cắt ở ranh giới câu (cuối segment có dấu . ! ?).
    """
    size_min = int(target_size * 0.8)
    size_max = int(target_size * 1.2)
    
    chunks = []
    current = {
        'segments': [],
        'char_count': 0,
        'start': None,
        'end': None,
    }
    
    for seg in segments:
        # Khởi tạo chunk mới
        if current['start'] is None:
            current['start'] = seg['start']
        
        current['segments'].append(seg)
        current['char_count'] += len(seg['text']) + 1  # +1 cho space
        current['end'] = seg['end']
        
        # Quyết định có nên cắt chunk không
        should_cut = False
        
        if current['char_count'] >= size_max:
            # Bắt buộc cắt
            should_cut = True
        elif current['char_count'] >= size_min:
            # Đủ ngưỡng tối thiểu, ưu tiên cắt ở cuối câu
            text_end = seg['text'].rstrip()
            if text_end and text_end[-1] in '.!?':
                should_cut = True
        
        if should_cut:
            chunks.append(current)
            current = {
                'segments': [],
                'char_count': 0,
                'start': None,
                'end': None,
            }
    
    # Chunk cuối
    if current['segments']:
        chunks.append(current)
    
    return chunks

# ============================================================
# RENDER CHUNK THÀNH FILE TXT
# ============================================================

def render_chunk_text(chunk, time_mark_interval=TIME_MARK_INTERVAL_SEC):
    """
    Render nội dung chunk: chèn timecode mỗi N giây + marker auto.
    """
    lines = []
    last_mark_time = chunk['start'] - time_mark_interval  # Để mark đầu tiên
    last_marker_pos = -1  # Tránh chèn marker liên tiếp
    
    buffer_text = []
    
    for i, seg in enumerate(chunk['segments']):
        # Chèn timecode nếu đến chu kỳ
        if seg['start'] - last_mark_time >= time_mark_interval:
            if buffer_text:
                lines.append(' '.join(buffer_text))
                buffer_text = []
            lines.append('')
            lines.append(f"[{seconds_to_hms(seg['start'])}]")
            last_mark_time = seg['start']
        
        # Detect marker trong segment này
        markers = detect_markers(seg['text'])
        if markers and i - last_marker_pos > 3:  # Tránh marker dày đặc
            if buffer_text:
                lines.append(' '.join(buffer_text))
                buffer_text = []
            for m in markers[:1]:  # Chỉ lấy marker đầu tiên
                lines.append(MARKER_SYMBOLS[m])
            last_marker_pos = i
        
        buffer_text.append(seg['text'])
    
    if buffer_text:
        lines.append(' '.join(buffer_text))
    
    return '\n'.join(lines)

# ============================================================
# YAML METADATA
# ============================================================

def parse_filename_metadata(filename: str):
    """
    Đoán metadata từ tên file.
    Hỗ trợ format: KHOA_YYYY_MM_DIA-DIEM_DX.srt
    Ví dụ: SSS_2024_08_HN_D1.srt
    """
    name = Path(filename).stem
    parts = name.split('_')
    
    meta = {
        'khoa': None,
        'nam': None,
        'thang': None,
        'dia_diem': None,
        'ngay': None,
    }
    
    # Heuristic đơn giản
    if len(parts) >= 1:
        meta['khoa'] = parts[0]
    if len(parts) >= 2 and parts[1].isdigit() and len(parts[1]) == 4:
        meta['nam'] = parts[1]
    if len(parts) >= 3 and parts[2].isdigit():
        meta['thang'] = parts[2]
    if len(parts) >= 4:
        meta['dia_diem'] = parts[3]
    
    # Tìm Dx (ngày trong khóa)
    for p in parts:
        m = re.match(r'^[Dd](\d+)$', p)
        if m:
            meta['ngay'] = int(m.group(1))
            break
    
    return meta

KHOA_FULL_NAMES = {
    'SSS': 'Sales Success System',
    'IPS': 'Internet Power System',
    'EAGLE': 'Eagle Camp',
    'LTVM': 'Lập Trình Vận Mệnh',
    'DTSGC': 'Đánh Thức Sự Giàu Có',
    'UT': 'Ultimate Trainer',
    'YES': 'YES Summit',
}

def build_yaml(file_id, meta_args, chunk, chunk_idx, total_chunks, file_srt_goc, char_count):
    """Build YAML header cho 1 chunk"""
    khoa = meta_args.get('khoa', 'UNKNOWN')
    ten_day_du = KHOA_FULL_NAMES.get(khoa, khoa)
    
    yaml = f"""---
# === METADATA FILE ===
file_id: {file_id}
khoa: {khoa}
ten_day_du: {ten_day_du}
ngay_giang: {meta_args.get('ngay_giang', 'TODO')}
dia_diem: {meta_args.get('dia_diem', 'TODO')}
ngay_trong_khoa: {meta_args.get('ngay', 'TODO')}
chunk_so: {chunk_idx + 1}
tong_chunk_ngay: {total_chunks}
file_srt_goc: {file_srt_goc}
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
    return yaml

# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description='Chuyển SRT thành chunk txt có YAML')
    parser.add_argument('input', help='File SRT đầu vào')
    parser.add_argument('--output-dir', default=None, help='Thư mục output (mặc định: ./output/<tên file>/)')
    parser.add_argument('--khoa', default=None, help='Mã khóa: SSS, IPS, EAGLE, LTVM, DTSGC, UT, YES')
    parser.add_argument('--ngay', type=int, default=None, help='Ngày trong khóa (1, 2, 3)')
    parser.add_argument('--dia-diem', default=None, help='Địa điểm tổ chức')
    parser.add_argument('--ngay-giang', default=None, help='Ngày giảng (YYYY-MM-DD)')
    parser.add_argument('--chunk-size', type=int, default=CHUNK_SIZE_TARGET, help='Ký tự/chunk (mặc định 10000)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Không tìm thấy file: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Đọc SRT
    with open(args.input, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📂 Đọc file: {args.input} ({len(content):,} ký tự)")
    
    segments = parse_srt(content)
    print(f"📊 Parse được {len(segments):,} segment")
    
    if not segments:
        print("❌ Không parse được segment nào. File SRT có vấn đề.", file=sys.stderr)
        sys.exit(1)
    
    total_duration = segments[-1]['end'] - segments[0]['start']
    print(f"⏱️  Tổng thời lượng: {total_duration/60:.1f} phút ({total_duration/3600:.2f} giờ)")
    
    # Chia chunk
    chunks = build_chunks(segments, target_size=args.chunk_size)
    print(f"✂️  Chia thành {len(chunks)} chunk")
    
    # Auto-detect metadata từ tên file
    auto_meta = parse_filename_metadata(args.input)
    meta_args = {
        'khoa': args.khoa or auto_meta['khoa'],
        'ngay': args.ngay or auto_meta['ngay'],
        'dia_diem': args.dia_diem or auto_meta['dia_diem'],
        'ngay_giang': args.ngay_giang or 'TODO',
    }
    print(f"🏷️  Metadata: {meta_args}")
    
    # Output dir
    if args.output_dir:
        output_dir = Path(args.output_dir)
    else:
        output_dir = Path('output') / Path(args.input).stem
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Render từng chunk
    file_srt_goc = os.path.basename(args.input)
    khoa = meta_args['khoa'] or 'X'
    ngay = meta_args['ngay'] or 0
    
    for i, chunk in enumerate(chunks):
        chunk_num = i + 1
        file_id = f"{khoa}_D{ngay}_C{chunk_num:02d}"
        
        body = render_chunk_text(chunk)
        char_count = sum(len(s['text']) for s in chunk['segments'])
        
        yaml_header = build_yaml(
            file_id=file_id,
            meta_args=meta_args,
            chunk=chunk,
            chunk_idx=i,
            total_chunks=len(chunks),
            file_srt_goc=file_srt_goc,
            char_count=char_count,
        )
        
        output_file = output_dir / f"{file_id}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(yaml_header)
            f.write('\n')
            f.write(body)
            f.write('\n')
        
        print(f"  ✅ {output_file.name} — {char_count:,} ký tự, {seconds_to_hms(chunk['start'])} → {seconds_to_hms(chunk['end'])}")
    
    print(f"\n🎉 Hoàn tất! {len(chunks)} file txt trong: {output_dir}/")

if __name__ == '__main__':
    main()
