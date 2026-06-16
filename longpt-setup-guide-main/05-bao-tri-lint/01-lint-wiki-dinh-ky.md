---
title: Lint wiki định kỳ
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 05
---

# Lint wiki định kỳ

## Trước đó

[[04-agents-skills-memory/05-memory-system]] — bạn đã hiểu memory.

---

## Vì sao lint

Sau 6-12 tháng vault grow, không lint định kỳ → vault mục:

- Link broken (file đã rename / delete)
- Page mồ côi (no inbound link)
- Mâu thuẫn (2 source nói khác nhau, chưa hoà giải)
- Tag không nhất quán (`course/sss` vs `course/SSS`)
- Frontmatter thiếu (page không có `type:`, `tags:`)
- Concept page nhắc trong 3+ source nhưng chưa có page

→ Lint = health check định kỳ. Như developer lint code.

---

## Tần suất lint

- **Weekly** (chủ nhật): lint nhanh — broken link, page mới mồ côi
- **Monthly**: lint sâu — consistency, atomicity, schema drift
- **Quarterly**: lint architecture — vault có nên tách / merge

---

## Bước 1 — Lint weekly

Trong Claude Code, root vault Brain:

```
> Lint wiki weekly. Check:
> 1. Broken wikilink (point tới page không tồn tại)
> 2. Page mới tuần này có frontmatter đầy đủ không
> 3. Source page mới đã update concept page liên quan chưa
> 4. log.md có entry weekly chưa
```

Claude:
- Glob `wiki/**/*.md`
- Grep wikilink `\[\[.*?\]\]`
- Check target tồn tại
- Report:

```
Lint report 2026-W22

## Broken wikilink (3)
- wiki/concepts/X.md → [[Concept Y không tồn tại]]
- wiki/sources/Z.md → [[Old Source đã rename]]
- ...

## Frontmatter thiếu (1)
- wiki/concepts/New-Concept.md thiếu `type:`, `tags:`

## Concept page chưa update (2)
- [[Source mới ingest hôm qua]] nhắc Concept A nhưng A.md chưa update

## Log entry
- W22 đã có 8 entry — OK
```

Bạn duyệt từng issue, fix hoặc skip.

---

## Bước 2 — Lint monthly

Sâu hơn weekly:

```
> Lint wiki monthly. Check:
> 1. Mâu thuẫn giữa concept page và source page
> 2. Concept page atomicity — có concept nào gộp 2 idea không?
> 3. Course MOC 2-chiều — concept page nói "Khoá học sử dụng [[X]]" thì X.md có link ngược không?
> 4. Tag consistency — có tag duplicate khác case (course/SSS vs course/sss)?
> 5. Stale page — page nào > 3 tháng không update?
> 6. Concept page nhắc trong 3+ source nhưng chưa có page riêng → đề xuất tạo
```

Claude:
- Đọc tất cả concept page + source page
- Cross-check
- Report comprehensive

Output dạng:

```
Lint monthly 2026-05

## Mâu thuẫn (2)
- [[Concept Y]] nói "PMF = 40% user buồn nếu mất". 
  [[Source Z]] nói "PMF = retention 90%". 
  → Cần ghi mâu thuẫn / merge / clarify

## Atomicity vi phạm (1)
- [[Concept HD-NT]] gộp 2 khái niệm "Hướng đến" + "Né tránh" — cấu trúc khác nhau
  → Tách thành [[Hướng đến]] + [[Né tránh]]

## Nhất quán 2 chiều (5)
- [[Concept A]] nói "Khoá học sử dụng [[SSS]]" nhưng SSS MOC không link [[A]]
- ...

## Tag inconsistent (2)
- `course/SSS` (uppercase) trong 3 page vs `course/sss` (lowercase) trong 47 page
  → Migrate uppercase → lowercase

## Stale (8)
- 8 page không update > 3 tháng — review hoặc archive

## Concept candidate (4)
- "Founder Mode" nhắc 5 source nhưng chưa có page → tạo
- "Burn Rate" nhắc 3 source → tạo
- ...
```

---

## Bước 3 — Lint quarterly architecture

Mỗi 3 tháng, lint sâu hơn:

```
> Lint architecture. Trả lời:
> 1. Vault hiện tại có schema drift không?
> 2. Có subfolder nào > 200 file → nên split?
> 3. Có archetype nào emerge → nên tách vault?
> 4. CLAUDE.md có rule outdated không?
> 5. Memory có entry stale không?
```

Claude:
- Đánh giá size vault
- Check distribution subfolder
- Suggest restructuring nếu cần

Output:

```
Architecture review 2026-Q2

## Vault size
- 1245 page (raw: 580, wiki: 665)
- Tăng 220 page từ Q1

## Subfolder distribution
- wiki/concepts/ — 312 (vẫn OK)
- wiki/sources/ — 234 (OK)
- wiki/courses/ — 22 (OK)
- wiki/stories/ — 45 (vừa)
- wiki/students/ — 158 (BIG — cân nhắc tách)
  → Đề xuất: tách wiki/students/ thành vault riêng "<Brand> Students" nếu sẽ vượt 300

## Archetype emerge
- 50 page về personal hobby (cá koi, xe, du lịch) lẫn trong wiki/concepts/
  → Đề xuất: tách vault Life

## CLAUDE.md outdated
- Rule "Frontmatter type chỉ có 5 loại" nhưng đã thấy `type: story`, `type: student` không trong list
  → Update CLAUDE.md add 2 type này

## Memory stale
- 3 memory về preference 2025 (đã đổi)
- 1 memory về tool deprecated
  → Cleanup
```

---

## Bước 4 — Tạo skill lint

Để chạy lint nhanh, tạo skill `/lint-wiki`:

```bash
mkdir -p .claude/skills/lint-wiki
```

`.claude/skills/lint-wiki/SKILL.md`:

```markdown
---
name: lint-wiki
description: "Lint wiki vault. Use khi user nói 'lint wiki', 'health check', 'audit wiki'. Mode: weekly | monthly | quarterly."
---

# Lint Wiki Skill

## Trigger

User nói:
- `/lint-wiki weekly`
- `/lint-wiki monthly`  
- `/lint-wiki quarterly`
- "Lint wiki tuần này"
- "Health check vault"

Mode mặc định: weekly.

## Workflow weekly

[Như bước 1 ở trên]

## Workflow monthly

[Như bước 2 ở trên]

## Workflow quarterly

[Như bước 3 ở trên]

## Output

Report markdown lưu vào `wiki/lint-reports/YYYY-MM-DD-<mode>.md`.

## Constraint

- KHÔNG tự fix issue — chỉ report
- User quyết thứ tự fix
- Report ngắn gọn (5-15 bullet, không > 1 page)
```

Gọi:

```
> /lint-wiki monthly
```

Skill tự chạy + tạo report.

---

## Bước 5 — Fix issue từ lint

Sau khi có lint report, fix dần:

### Fix broken link

```
> Fix broken wikilink trong wiki/concepts/X.md — link [[Concept Y]] không tồn tại. 
> Tạo concept page Y dạng stub hoặc rename link.
```

Claude:
- Hỏi: tạo Y hay rename link?
- Apply quyết định

### Fix mâu thuẫn

```
> Concept Y và Source Z mâu thuẫn về PMF. Ghi section "Mâu thuẫn" trong cả 2 page.
```

### Fix atomicity

```
> Tách concept page "HD-NT" thành 2 page "Hướng đến" + "Né tránh".
> Update tất cả wikilink ref.
```

Claude:
- Tạo 2 page mới
- Move nội dung phù hợp
- Update wikilink trong page khác

---

## Bước 6 — Audit log

Sau khi lint xong, log:

```markdown
## [2026-05-29] lint | monthly
- Issues found: 18
- Fixed: 12
- Deferred: 4 (chờ user quyết)
- Skipped: 2 (false positive)
- Report: [[wiki/lint-reports/2026-05-29-monthly]]
```

---

## Bước 7 — Pattern lint hay gặp

5 issue thường nhất:

### Issue 1 — Broken wikilink sau rename file

User rename file `Concept-A.md` → `Concept A.md` (thêm space). Mọi `[[Concept-A]]` cũ vỡ.

Fix: Obsidian "Refactor file" (Cmd+P → Refactor → rename) → tự update wikilink. Hoặc dùng Claude bulk fix.

### Issue 2 — Concept tạo nhưng chưa link course

Concept page có frontmatter `tags: [course/sss]` nhưng SSS MOC không liệt concept đó.

Fix: update SSS MOC, add `## Modules — [[Concept]]`.

### Issue 3 — Source page không cite concept

Source page có nội dung touch concept nhưng quên cite `[[concept]]`.

Fix: Claude scan source page → đề xuất concept liên quan → cite.

### Issue 4 — Frontmatter inconsistent

Page A có `tags: [framework, course/sss]`. Page B có `tag: framework, course/sss` (typo `tag` thiếu `s`).

Fix: standard `tags` (plural). Bulk fix.

### Issue 5 — Stale snapshot

Source page snapshot tại 2024-10. Source raw đã update 2025-06 nhưng wiki không update.

Fix: ingest lại source mới với agent → wiki update.

---

## Bước 8 — Tránh over-engineering lint

Đừng:

- Lint mỗi ngày (overhead, ít issue)
- Auto-fix mọi issue (false positive risk)
- Tạo 100 lint rule (complexity)

Giữ:
- Weekly basic (5 rule)
- Monthly comprehensive (10-15 rule)
- Quarterly architectural (5 question)

---

## Bước 9 — Khi lint phát hiện vấn đề lớn

Vd lint thấy 50% wikilink broken → vault bị corrupt:

- DỪNG ngay
- Kiểm tra Git history (revert nếu cần)
- Restore từ backup gần nhất
- Investigate nguyên nhân (rename script lỗi? Migrate folder sai?)

KHÔNG bulk fix khi có dấu hiệu corruption.

---

## Bước 10 — Lint cross-vault

Nếu có multi-vault, lint cross-vault:

```
> Lint cross-vault: check brain_ref trong Marketing có trỏ page tồn tại trong Brain không?
```

Claude:
- Đọc Marketing/wiki/assets/ frontmatter
- Check brain_ref → file Brain exist
- Report broken cross-ref

---

## Tiếp theo

Đọc tiếp: [[02-backup-icloud-git]] — Backup chiến lược.
