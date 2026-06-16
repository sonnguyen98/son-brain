# CLAUDE.md — Wiki Schema

This file defines the structure, conventions, and workflows for maintaining this wiki.
Read it at the start of every session before doing any wiki work.

---

## Mission

This vault is **Sơn's second brain** — không phải knowledge base hẹp về kinh doanh. Mục tiêu: lưu trữ tất cả những gì Sơn **thu thập** (link, tài liệu, idea), **học** (sách, khóa, podcast), **thấy** (quan sát hằng ngày, sự kiện), và **giao tiếp** (cuộc nói chuyện, khách hàng), được sắp xếp bài bản qua cấu trúc page types + cross-link + index + lint định kỳ.

Don't reject content as "off-topic." Mọi thứ Sơn capture đều thuộc phạm vi.

---

## Directory layout

```
raw/                  ← immutable source documents (you write here, LLM reads only)
  audio/              ← drop voice recordings (.mp3, .m4a, .wav, ...) — transcribe.py reads
    processed/        ← audio moves here after transcribe.py runs
  conversations/      ← transcripts produced from raw/audio/
  daily/              ← daily notes (YYYY-MM-DD.md) — quick capture of quan sát/học/idea
  web/                ← articles & YouTube transcripts — output of ingest_url.py
  pdf/                ← extracted text from PDFs + the .pdf files themselves
  images/             ← screenshots / photos — LLM reads directly via vision
wiki/                 ← LLM-maintained knowledge pages (LLM writes here)
  index.md            ← catalog of all wiki pages
  log.md              ← append-only chronological record
  overview.md         ← high-level synthesis of the whole knowledge base
  person/             ← living profiles of people (customers, family, friends)
  source/, entity/, concept/, analysis/
tools/                ← helper scripts
  search.py           ← BM25 search over wiki pages
  transcribe.py       ← Whisper STT: raw/audio/ → raw/conversations/
  new_daily.py        ← create/open today's daily note in raw/daily/
  ingest_url.py       ← fetch URL (article or YouTube) → raw/web/
  ingest_pdf.py       ← extract PDF text → raw/pdf/<slug>.md (--ocr for scanned)
  ocr_image.py        ← batch OCR images in raw/images/ → raw/images/text/
  lint_wiki.py        ← weekly hygiene: broken links, orphans, stubs, missing pages
CLAUDE.md             ← this file
```

## Search tool

`tools/search.py` does BM25 full-text search over all wiki markdown pages.

```
# Find python executable
PYTHON = C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe

# Usage
python tools/search.py <query> [--top N]

# Example
python tools/search.py "reinforcement learning" --top 3
```

When answering a query, prefer running `search.py` over reading `index.md` manually once the wiki has more than ~20 pages.

---

## Capture pipelines (raw/)

Five pipelines feed `raw/`. All produce markdown files Sơn can review before saying "ingest".

### 1. Audio → conversation transcript

```
python tools/transcribe.py                   # transcribe all in raw/audio/
python tools/transcribe.py path/to/file.m4a  # specific file
python tools/transcribe.py --model medium    # smaller/faster
```

Output: `raw/conversations/<YYYY-MM-DD>-<slug>.md` with frontmatter (`participants`, `context` left blank for Sơn to fill). Audio moves to `raw/audio/processed/`. Filename can encode date: `2026-06-16-khach-anh-tuan.m4a` → uses 2026-06-16 + label.

Whisper hallucinates on intro/outro music — when ingesting, skip obvious garbled passages. See `tools/transcribe.py` docstring for model size tradeoffs.

### 2. Daily note → quick capture

```
python tools/new_daily.py                # today, auto-opens in default editor
python tools/new_daily.py 2026-06-15     # specific date
python tools/new_daily.py --no-open      # don't auto-open
```

Creates `raw/daily/YYYY-MM-DD.md` with template sections: Quan sát, Học, Gặp, Idea, TODO, Phản tỉnh. Sơn types freely; when he says "ingest daily" or "ingest 2026-06-16", LLM processes per `## Workflow: Ingest daily note` below.

### 3. URL → web/YouTube article

```
python tools/ingest_url.py https://example.com/article
python tools/ingest_url.py https://youtu.be/abc123 --name custom-slug
```

Auto-detects YouTube vs general web. YouTube → fetches transcript (prefers Vietnamese > English > any). Web → trafilatura extracts main article content as markdown. Output: `raw/web/YYYY-MM-DD-<slug>.md` with `source_url`, `title`, `author`, `site`, `published` (web) or `video_id`, `lang` (youtube).

### 4. PDF → text (with OCR fallback)

```
python tools/ingest_pdf.py                       # all PDFs in raw/pdf/ (text extract)
python tools/ingest_pdf.py path/to/book.pdf      # specific file
python tools/ingest_pdf.py --ocr                 # auto-OCR when text is sparse (<100 chars/page)
python tools/ingest_pdf.py --ocr scanned.pdf     # force OCR on one file
```

Drop PDFs into `raw/pdf/`, run. Output: `raw/pdf/<slug>.md` with page-by-page text. PDF stays in place. `extract_method` in frontmatter shows whether `pypdf` (text layer) or `easyocr` (rasterized + OCR) was used.

For scanned PDFs: re-run with `--ocr`. Uses `pypdfium2` to rasterize 2x DPI + EasyOCR (vi+en). First run downloads ~200MB models. Slow on CPU (~30s/page).

### 5. Image/screenshot → text

Two routes:

- **LLM vision (recommended for ad-hoc)**: drop image into `raw/images/` or paste in chat. Em (LLM) reads it directly via Read tool — best for screenshots, handwriting, mixed visual+text, anything needing context understanding.
- **Batch OCR (for many images)**: `python tools/ocr_image.py` reads all images in `raw/images/` with EasyOCR, writes markdown to `raw/images/text/<slug>.md`. Each output has `avg_confidence` in frontmatter + a "low confidence" section for segments <0.6 that need human verify.

```
python tools/ocr_image.py                      # all new images
python tools/ocr_image.py path/to/img.png      # specific
python tools/ocr_image.py --lang vi,en,ja      # add Japanese
```

---

## Wiki page conventions

- **Filename**: `kebab-case.md` (e.g. `reinforcement-learning.md`, `openai.md`)
- **Title heading**: `# Title` on line 1
- **Frontmatter** (optional but encouraged):
  ```yaml
  ---
  tags: [entity, concept, source, analysis]
  sources: [source-slug-1, source-slug-2]
  updated: YYYY-MM-DD
  ---
  ```
- **Cross-links**: Use Obsidian wikilinks `[[page-name]]` for all internal references. Never use relative paths.
- **Source citations**: Cite source pages as `([[source-slug]])` inline.
- **Page types**:
  - `source/` — one page per ingested source, named by slug
  - `entity/` — an organization, product, place (NOT people — use `person/` for those)
  - `person/` — a living profile of one human, accrues across conversations over time (see below)
  - `concept/` — an idea, method, framework, term
  - `analysis/` — comparisons, syntheses, questions answered
  - `overview.md` — high-level map of the entire knowledge base (update on every ingest)

---

## index.md conventions

`wiki/index.md` is a catalog of every wiki page.
- Organized by category: Overview, Sources, Entities, Concepts, Analyses
- Each entry: `- [[page-name]] — one-line summary`
- Update on every ingest and whenever pages are created or significantly changed
- When answering a query, read `index.md` first to identify relevant pages, then read those pages

---

## log.md conventions

`wiki/log.md` is append-only. Never edit past entries.
- Entry format: `## [YYYY-MM-DD] <operation> | <title>`
- Operations: `ingest`, `query`, `lint`, `init`
- Add one entry per operation at the end of the file
- Include a 2–4 line summary of what was done and what changed

---

## person/ conventions

`wiki/person/<slug>.md` is a living dossier for one human (customer, prospect, family member, friend, colleague). Unlike `source/` pages which are snapshots, person pages **accrue** information across many conversations and ingests.

- Filename: ASCII slug of the most-used name (e.g. `anh-tuan-kinh-mat.md`, `vo.md`, `chi-mai-sale.md`). Disambiguate with a role suffix when needed.
- Sections to maintain (omit empty ones):
  - **Tóm tắt** — 1–3 lines: who they are, relationship to user, current status
  - **Quan hệ** — relationship type, how long, frequency of contact
  - **Bối cảnh cá nhân** — job, family, location, anything stable they've shared
  - **Sở thích & quan điểm** — preferences, opinions, recurring themes
  - **Pain / Gain** (for customers/prospects) — use the [[ho-so-khach-hang-vpc]] taxonomy: Jobs / Pains / Gains, with verbatim quotes when possible
  - **Mốc thời gian** — chronological notes of meaningful interactions, each line: `- YYYY-MM-DD ([[source-slug]]) — what happened, what they said`
  - **Hành động đang chờ** — what the user owes them, or vice versa
- Always cite the source conversation inline: `([[2026-06-16-khach-anh-tuan]])`
- When a person page grows past ~300 lines, propose splitting by topic but keep one canonical page as the index.

---

## Workflow: Ingest

When the user says "ingest [source]":

1. **Read** the source file from `raw/` (including `raw/conversations/` for transcripts)
2. **Discuss** key takeaways with the user — ask what to emphasize if unclear. For conversation transcripts, confirm `participants` and `context` from the frontmatter (ask if blank).
3. **Create** `wiki/source/<slug>.md` — a structured summary:
   - Title, author/origin, date
   - 3–5 key claims or findings (for conversations: key topics discussed, decisions made, emotional beats)
   - Notable quotes (verbatim, especially for customer pain/gain language)
   - Connections to existing wiki pages
   - Open questions this source raises
4. **Update** person pages — for each human in `participants`, update or create `wiki/person/<slug>.md`. Append a timeline entry, update pain/gain if customer, refresh bối cảnh cá nhân with anything new.
5. **Update** entity pages — for each named org/product/place mentioned, update or create `wiki/entity/<name>.md`
6. **Update** concept pages — for each key concept, update or create `wiki/concept/<term>.md`
7. **Update** `wiki/overview.md` if the source shifts the big picture
8. **Update** `wiki/index.md` — add all new/changed pages
9. **Append** to `wiki/log.md`

A single source typically touches 5–15 wiki pages. Err on the side of creating pages — stubs are fine.

### Tips by source type

**Conversation transcripts (`raw/conversations/`)**:
- Whisper errors (homophones, name spellings, dropped words) — clean silently when sure; ask Sơn when phrase is important and ambiguous.
- Transcript doesn't speaker-diarize — use `context` and surrounding cues to attribute. When unclear: "one of the participants".
- Sale/customer calls → run [[ho-so-khach-hang-vpc]] taxonomy: Jobs × Pains × Gains with verbatim quotes.
- Personal/tâm sự → recurring emotional themes go in `wiki/concept/` (e.g. `concept/lo-au-cong-viec.md`), not as person properties.

**Web articles / YouTube (`raw/web/`)**:
- Cite `source_url` from frontmatter in the wiki source page (use markdown link, not wikilink).
- YouTube transcripts have caption errors similar to Whisper — handle the same way.
- If the article is itself a summary of a primary source, note that and link the primary source too.

**PDFs (`raw/pdf/`)**:
- pypdf preserves layout poorly — tables, multi-column, footnotes will be jumbled. Trust paragraph-level extraction, not exact word order in complex layouts.
- For books: ingest may produce multiple source pages, one per chapter, with `parent_source` field cross-linking.

**Images (`raw/images/`)**:
- Read the image with the Read tool (Claude has vision). Describe what's in it as if narrating to a blind reader before extracting structured info.
- For screenshots of UI/dashboards, capture the underlying data, not just the visual.

---

## Workflow: Ingest khóa học (LTTL hoặc bất kỳ khóa nào ghi âm)

**Cấu trúc thư mục**: Sơn tạo subfolder cho mỗi khóa trong `raw/audio/`, slug ASCII ngắn (vd `raw/audio/lttl/`). Mỗi file ghi âm đánh số tăng dần `01.m4a`, `02.m4a`... — không phải bài/buổi rời rạc mà là **mạch ghi liên tục** (Sơn học đến đâu ghi đến đấy; file 02 nối tiếp file 01 theo thời gian).

**Auto behavior của transcribe.py**: khi file ở subfolder, output đặt vào `raw/conversations/<course>-<NN>.md` (không date prefix), frontmatter tự set `type: course-lecture` + `course: <course-slug>`. Audio move sang `raw/audio/processed/<course>/<NN>.m4a` (giữ subfolder).

**Khi Sơn nói "ingest <course>-NN" (vd "ingest lttl-03")**:

1. **Đọc** `raw/conversations/<course>-NN.md` — thêm cả `<course>-(NN-1).md` để có context liền mạch nếu cần
2. **Tạo** `wiki/source/<course>-NN.md` — tóm tắt segment này: 3-5 idea/concept/case mới, câu chốt đáng nhớ, kết nối với segment trước (`<course>-(NN-1)`)
3. **Update** `wiki/entity/khoa-<course-slug>.md` — append vào bảng "Segments đã ingest" (cột: số, link source, ngày ingest, concept chính rút ra)
4. **Tạo/update** concept pages cho mỗi khái niệm/phương pháp mới (mỗi concept page riêng — KHÔNG gom vào source). Concept đã có từ segment trước → append snapshot/bổ sung, không tạo trùng.
5. **KHÔNG** tạo person pages — khóa học chỉ có giảng viên đã có ở [[pham-thanh-long]]
6. **Cross-check** với [[triet-ly-lam-viec-son]] — segment này khớp / không khớp / mâu thuẫn với triết lý SOP + ủy quyền + automation của Sơn? Note thẳng vào source page nếu có tension.
7. **Append** log; cập nhật index nếu có concept page mới.

Khóa LTTL hiện đang theo → tracker chính ở [[khoa-lien-tuc-tien-len]].

**Đặt tên file**: tối thiểu `NN.m4a` (vd `01.m4a` trong folder `raw/audio/lttl/`). Nếu Sơn nhớ chủ đề chính của segment, thêm vào: `01-tu-duy-mo.m4a` — đỡ phải đoán topic sau.

---

## Workflow: Ingest daily note

When Sơn says "ingest daily" (today) or "ingest 2026-06-15":

1. **Read** `raw/daily/YYYY-MM-DD.md`. Skip empty sections silently.
2. **No source page needed** — daily notes are too granular. Instead, distribute content across existing page types:
   - **Người trong "Gặp / Nói chuyện"** → update or create `wiki/person/<slug>.md` (append a timeline entry: `- YYYY-MM-DD — what Sơn noted`)
   - **Idea** → if novel and substantial, create `wiki/concept/<slug>.md` stub; if related to existing concept, append a "Snapshot YYYY-MM-DD" subsection.
   - **Học / Đọc** with URL → if not already in `raw/web/`, prompt Sơn to run `ingest_url.py` first; otherwise link to the existing source page.
   - **Quan sát** that surfaces a pattern across multiple daily notes → escalate to a `wiki/concept/` page (e.g. `concept/quan-sat-khach-vao-cua-hang.md`).
   - **TODO** → don't put TODOs into wiki (they're ephemeral); summarize them only if they describe a strategic shift.
3. **Append** to `wiki/log.md` as `## [YYYY-MM-DD] ingest | daily <date>` with 2–3 line summary of what was updated.
4. **Do NOT** update `index.md` for every daily — only when a daily ingest creates new person/concept pages.

Daily ingests are cheaper than source ingests. Touch 1–5 pages typically, not 5–15.

---

## Workflow: Query

When the user asks a question:

1. **Read** `wiki/index.md` to identify relevant pages
2. **Read** relevant pages (entity, concept, source, analysis pages as needed)
3. **Synthesize** an answer with inline citations to wiki pages
4. **Decide** whether the answer is worth filing as a new `wiki/analysis/` page
   - If yes: create the page, update `index.md`, append to `log.md`
5. **Suggest** follow-up questions or missing sources if relevant

---

## Workflow: Lint

Two layers of lint:

**Layer 1 — automated (cheap, runnable any time)**:
```
python tools/lint_wiki.py            # full report
python tools/lint_wiki.py --quiet    # one-line summary
python tools/lint_wiki.py --save     # save report to wiki/lint-report.md
```
Detects: broken wikilinks, orphan pages, stubs (<300 chars), missing frontmatter, repeated capitalized terms appearing in ≥3 pages without a dedicated page (concept-page candidates). Runs as plain Python, no LLM call.

**Layer 2 — LLM-assisted (when Sơn says "lint the wiki")**:

1. Run `python tools/lint_wiki.py --save` and read the report
2. Read `wiki/index.md` + pages flagged by Layer 1
3. Additionally check for what Layer 1 cannot detect:
   - **Contradictions** between pages
   - **Claims superseded** by newer sources
   - **Missing cross-references** between related pages (semantic, not syntactic)
   - **Data gaps** that a web search could fill
4. For each issue: note the page, describe the problem, suggest a fix
5. Ask Sơn which fixes to apply
6. Append a lint entry to `log.md`

Suggest running Layer 1 at least weekly. Run Layer 2 after every ~20 ingests or when Sơn requests.

---

## Workflow: Maintain overview

`wiki/overview.md` is a high-level synthesis of the entire knowledge base.
- Written in flowing prose, not bullet points
- Covers: what this wiki is about, the main themes, key entities, open questions
- Updated after every 3–5 ingests, or when a source significantly shifts the picture
- Should be readable as a standalone orientation document

---

## Style guidelines

- Write wiki pages for a reader who has domain knowledge but hasn't read the sources
- Prefer specific, concrete claims over vague generalities
- Flag uncertainty explicitly: "According to [[source-slug]], …" or "This is contested — see [[page-a]] vs [[page-b]]"
- Keep source pages factual and close to the source; put synthesis in concept/analysis pages
- Don't delete content from source pages — mark it as superseded if needed
