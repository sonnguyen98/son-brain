---
title: Tạo skill đầu tiên
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 04
---

# Tạo skill đầu tiên

## Trước đó

[[03-skill-la-gi]] — bạn đã hiểu skill.

---

## Use case

Workflow lặp đi lặp lại: bạn ingest 1 source SRT (transcript YouTube hoặc khoá học) → cần chia chunk theo timecode.

Cụ thể:
- File SRT dài 1000-3000 dòng
- Mỗi 3 phút → chunk riêng
- Mỗi chunk có metadata (timecode start, marker auto-detect)
- Output: nhiều file `.txt` nhỏ trong subfolder `chunks/`

Quá nặng để làm tay. Tạo skill `srt-to-chunks`.

(Anh Long có sẵn `text-cat-chunk` và `srt-cat-chunk`. Chúng ta build phiên bản đơn giản hơn để học.)

---

## Bước 1 — Tạo folder skill

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
mkdir -p .claude/skills/srt-to-chunks/scripts
```

---

## Bước 2 — Viết SKILL.md

`.claude/skills/srt-to-chunks/SKILL.md`:

```markdown
---
name: srt-to-chunks
description: "Cắt file SRT (transcript) thành chunk txt nhỏ, mỗi chunk ~3 phút audio + timecode + YAML metadata. Use BẤT CỨ KHI NÀO user nói 'cắt SRT', 'chia chunk SRT', 'xử lý transcript X.srt', 'chunk file Y.srt'. Output: folder chunks/ với file txt + metadata."
---

# SRT → Chunks Skill

## Mục tiêu

Chuyển file SRT 1000-3000 dòng thành nhiều file txt chunk:
- Mỗi chunk = 3 phút audio
- Có YAML metadata (chunk_id, time_start, time_end)
- Output: `<srt_dir>/chunks/chunk-NNN.txt`

## Trigger

User nói:
- "Cắt SRT raw/transcripts/X.srt"
- "Chia chunk transcript Y"
- "Xử lý file Z.srt"

→ Invoke skill.

## Workflow

### 1. Get input

User cung cấp:
- SRT file path (relative hoặc absolute)
- Chunk duration (default: 3 phút = 180 giây)

Nếu thiếu — hỏi user.

### 2. Run script

Chạy:

```bash
python .claude/skills/srt-to-chunks/scripts/chunk_srt.py <srt_path> --duration 180
```

### 3. Verify output

Check folder `<srt_dir>/chunks/` có file:
- `chunk-001.txt`
- `chunk-002.txt`
- ...

### 4. Báo cáo user

- Số chunk tạo
- Tổng duration
- Output path
- Đề xuất bước tiếp: ingest từng chunk vào wiki

## Output format mỗi chunk

```
---
chunk_id: 001
time_start: "00:00:00.000"
time_end: "00:03:00.000"
duration_sec: 180
source_srt: <path>
---

[Text transcript đoạn 3 phút này, đã strip timecode]
```

## Constraint

- KHÔNG sửa file SRT gốc (chỉ đọc)
- Output folder `chunks/` tạo cùng cấp với SRT
- Chunk overlap 5 giây để tránh cắt giữa câu

## Edge case

- SRT < 3 phút → 1 chunk duy nhất
- SRT format malformed → script báo lỗi + skip
- Folder chunks/ đã có file → hỏi overwrite hay skip
```

---

## Bước 3 — Viết script Python

`.claude/skills/srt-to-chunks/scripts/chunk_srt.py`:

```python
#!/usr/bin/env python3
"""Cắt SRT thành chunk txt theo duration."""

import sys
import re
import argparse
import os
from pathlib import Path


def parse_srt(content):
    """Parse SRT, trả list entries [{idx, start, end, text}]."""
    entries = []
    blocks = content.strip().split('\n\n')
    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) < 3:
            continue
        idx = lines[0]
        time_line = lines[1]
        text = '\n'.join(lines[2:])
        m = re.match(r'(\d{2}:\d{2}:\d{2}[,.]\d{3}) --> (\d{2}:\d{2}:\d{2}[,.]\d{3})', time_line)
        if not m:
            continue
        start, end = m.groups()
        entries.append({
            'idx': idx,
            'start': start.replace(',', '.'),
            'end': end.replace(',', '.'),
            'text': text,
        })
    return entries


def time_to_seconds(t):
    """HH:MM:SS.mmm → seconds."""
    h, m, rest = t.split(':')
    s, ms = rest.split('.')
    return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000


def seconds_to_time(seconds):
    """Seconds → HH:MM:SS.mmm."""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}"


def chunk_srt(srt_path, duration_sec=180):
    """Cắt SRT thành chunk."""
    srt_path = Path(srt_path).resolve()
    content = srt_path.read_text(encoding='utf-8')
    entries = parse_srt(content)
    
    if not entries:
        print(f"ERROR: No entries parsed from {srt_path}")
        return
    
    output_dir = srt_path.parent / "chunks"
    output_dir.mkdir(exist_ok=True)
    
    chunk_idx = 1
    chunk_start = 0
    chunk_end = duration_sec
    chunk_text = []
    
    for entry in entries:
        entry_start = time_to_seconds(entry['start'])
        if entry_start >= chunk_end:
            # Save current chunk
            if chunk_text:
                _save_chunk(output_dir, chunk_idx, chunk_start, chunk_end, '\n'.join(chunk_text), str(srt_path))
                chunk_idx += 1
            chunk_start = chunk_end
            chunk_end += duration_sec
            chunk_text = []
        chunk_text.append(entry['text'])
    
    # Save last chunk
    if chunk_text:
        last_end = time_to_seconds(entries[-1]['end'])
        _save_chunk(output_dir, chunk_idx, chunk_start, last_end, '\n'.join(chunk_text), str(srt_path))
    
    print(f"Created {chunk_idx} chunks in {output_dir}")


def _save_chunk(output_dir, idx, start_sec, end_sec, text, src):
    """Save 1 chunk."""
    path = output_dir / f"chunk-{idx:03d}.txt"
    content = f"""---
chunk_id: {idx:03d}
time_start: "{seconds_to_time(start_sec)}"
time_end: "{seconds_to_time(end_sec)}"
duration_sec: {int(end_sec - start_sec)}
source_srt: {src}
---

{text}
"""
    path.write_text(content, encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('srt_path', help='Path to SRT file')
    parser.add_argument('--duration', type=int, default=180, help='Chunk duration in seconds (default 180)')
    args = parser.parse_args()
    
    chunk_srt(args.srt_path, args.duration)
```

Make executable:

```bash
chmod +x .claude/skills/srt-to-chunks/scripts/chunk_srt.py
```

---

## Bước 4 — Test script thủ công

Tải 1 SRT mẫu (vd YouTube transcript) vào `raw/transcripts/test.srt`:

```bash
python .claude/skills/srt-to-chunks/scripts/chunk_srt.py raw/transcripts/test.srt --duration 180
```

Output:
```
Created 8 chunks in raw/transcripts/chunks
```

Mở 1 chunk:
```bash
cat raw/transcripts/chunks/chunk-001.txt | head -20
```

Verify format đúng.

---

## Bước 5 — Test skill qua Claude Code

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents/My Brain"
claude
```

Trong prompt:

```
> Cắt SRT raw/transcripts/test.srt
```

Claude:
- Match keyword "Cắt SRT" với skill `srt-to-chunks`
- Invoke skill
- Run script
- Báo cáo: "Created 8 chunks. Path: raw/transcripts/chunks/"

---

## Bước 6 — Iterate skill

Sau lần test, edge case:

### Edge 1 — User nói "chunk 5 phút"

Skill cần parse "5 phút" → 300 giây. Update SKILL.md:

```markdown
### 1. Get input

User cung cấp:
- SRT file path
- Chunk duration (default: 180s = 3 phút)
  - Parse format: "X phút" → X*60, "X giây" → X
```

### Edge 2 — File output đã tồn tại

Update script:

```python
if (output_dir / f"chunk-001.txt").exists():
    confirm = input("Output exists. Overwrite? [y/N]: ")
    if confirm.lower() != 'y':
        print("Skipped")
        return
```

### Edge 3 — User upload file SRT trực tiếp (không có path)

Hỏi user thả file vào folder cụ thể trước:

```
Vui lòng thả file SRT vào raw/transcripts/ trước. Sau đó tôi sẽ xử lý.
```

---

## Bước 7 — Skill chain với agent

Skill `srt-to-chunks` chỉ chia chunk. Để ingest chunk vào wiki → kết hợp với agent:

```
> Cắt SRT raw/transcripts/SSS-21-D1.srt, rồi ingest từng chunk vào wiki
```

Workflow:
1. Skill `srt-to-chunks` → tạo chunks/
2. Agent `article-ingest` (đã build) → ingest từng chunk

Bạn type 1 lệnh → 2 tool chạy tự động.

---

## Bước 8 — Anti-pattern khi viết skill

### Sai 1 — Script bug không handle gracefully

Script panic khi file không exist → user thấy stack trace Python. Bad UX.

Update:

```python
if not srt_path.exists():
    print(f"ERROR: File not found: {srt_path}")
    sys.exit(1)
```

### Sai 2 — Skill hardcode path

```
1. Đọc raw/transcripts/specific-file.srt
```

→ Skill chỉ work cho file đó. Sửa: `Đọc <file user chỉ>`.

### Sai 3 — Skill không cite file output

User không biết output ở đâu sau khi skill chạy.

→ Output report: "Created N files in <path>".

### Sai 4 — Skill phụ thuộc lib chưa cài

Script import package chưa pip install.

→ Document yêu cầu trong SKILL.md:

```markdown
## Yêu cầu

- Python 3.10+
- Không cần package extra (chỉ stdlib)
```

---

## Bước 9 — Best practice viết skill

1. **Single-purpose**: skill làm 1 thứ, làm tốt
2. **Idempotent**: chạy lần 2 với input cũ → output giống (hoặc skip)
3. **Verbose output**: in progress (vd: "Processing chunk 5/10")
4. **Error message rõ**: lỗi gì, làm gì để fix
5. **Documentation trong SKILL.md**: workflow, constraint, edge case

---

## Bước 10 — Khi nào nâng skill lên agent

Skill grow → có dấu hiệu:
- SKILL.md > 200 dòng
- Workflow nhiều step phụ thuộc nhau
- Cần context isolation
- Có rule cứng cần system prompt enforcement

→ Migrate skill → agent. Move logic SKILL.md vào `.claude/agents/<name>.md` system prompt.

Vd: `srt-to-chunks` skill có thể migrate sang `raw-chunk-ingest-pipeline` agent của anh Long khi workflow phức tạp (chunk + chia folder canonical + organize raw + update wiki).

---

## Tiếp theo

Đọc tiếp: [[05-memory-system]] — Memory system Claude.
