# CLAUDE.md — Wiki Schema

This file defines the structure, conventions, and workflows for maintaining this wiki.
Read it at the start of every session before doing any wiki work.

---

## Directory layout

```
raw/          ← immutable source documents (you write here, LLM reads only)
wiki/         ← LLM-maintained knowledge pages (LLM writes here)
  index.md    ← catalog of all wiki pages
  log.md      ← append-only chronological record
tools/        ← helper scripts
  search.py   ← BM25 search over wiki pages
CLAUDE.md     ← this file
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
  - `entity/` — a person, organization, product, place
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

## Workflow: Ingest

When the user says "ingest [source]":

1. **Read** the source file from `raw/`
2. **Discuss** key takeaways with the user — ask what to emphasize if unclear
3. **Create** `wiki/source/<slug>.md` — a structured summary:
   - Title, author/origin, date
   - 3–5 key claims or findings
   - Notable quotes (if any)
   - Connections to existing wiki pages
   - Open questions this source raises
4. **Update** entity pages — for each named entity (person, org, product) mentioned, update or create `wiki/entity/<name>.md`
5. **Update** concept pages — for each key concept, update or create `wiki/concept/<term>.md`
6. **Update** `wiki/overview.md` if the source shifts the big picture
7. **Update** `wiki/index.md` — add all new/changed pages
8. **Append** to `wiki/log.md`

A single source typically touches 5–15 wiki pages. Err on the side of creating pages — stubs are fine.

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

When the user says "lint the wiki":

1. Read `wiki/index.md` and all pages linked from it
2. Check for and report:
   - Contradictions between pages
   - Claims superseded by newer sources
   - Orphan pages (no inbound wikilinks)
   - Important concepts mentioned but lacking their own page
   - Missing cross-references between related pages
   - Data gaps that could be filled with a web search
3. For each issue: note the page, describe the problem, suggest a fix
4. Ask the user which fixes to apply
5. Append a lint entry to `log.md`

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
