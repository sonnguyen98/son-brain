---
title: Vault Marketing — production + measurement
type: huong-dan
created: 2026-05-29
updated: 2026-05-29
phan: 03
---

# Vault Marketing — production + measurement

## Trước đó

[[03-vault-4dx-execution]] — bạn đã hiểu 4DX vault.

---

## Mục tiêu vault Marketing

Vault Marketing **vận dụng** kiến thức Brain để **sản xuất, đo lường, tối ưu** content / lead page / sale page.

4 nhiệm vụ:

1. **Lưu trữ marketing data** — content sản xuất, lead/sale page, screenshot dashboard, copy quảng cáo, biến thể A/B
2. **Báo cáo phân tích** — pivot từ raw thô thành insight có hành động
3. **Đo lường số lượng + chất lượng** content theo asset/kênh/tuần
4. **Đo lường lead/sale page + variant** — A/B test, conversion rate, retention

---

## Khi nào setup Marketing vault

Setup Marketing vault nếu:
- Bạn chạy business / coaching / SaaS
- Có > 5 asset cần track (lead page, sale page, email, ad)
- Đang đo metric (traffic, opt-in, CVR)

Skip nếu:
- Cá nhân không chạy business
- Chưa có asset nào đang đo

---

## Khác biệt Marketing vs Brain

| Brain | Marketing |
|---|---|
| Knowledge concept-first | Asset production tracking |
| Raw → wiki summary | Raw = export dashboard |
| Source = article/transcript | Source = data dump |
| Concept = framework | Asset = lead/sale page |
| Course MOC | Event MOC (launch campaign) |
| Stable schema | Variant + metric snapshot timeline |
| Tone formal | Tone marketing operational |

---

## Bước 1 — Tạo vault Marketing

```bash
cd "/Users/$USER/Library/Mobile Documents/iCloud~md~obsidian/Documents"
mkdir "My Marketing"
cd "My Marketing"
mkdir -p raw/{meta-ads,ga4,youtube,pancake,assets} \
         wiki/{sources,assets/{lead-pages,sale-pages,contents,ads,events},reports,concepts,entities,syntheses,comparisons} \
         4dx/actions
touch CLAUDE.md README.md index.md log.md
touch 4dx/1-wig.md 4dx/2-lead-measures.md 4dx/3-scoreboard.md 4dx/4-cadence.md
```

---

## Bước 2 — CLAUDE.md cho Marketing

Template:

```markdown
# CLAUDE.md — Schema vault Marketing

Vault này lưu trữ + đo lường marketing. 4 nhiệm vụ chính:

1. Lưu trữ marketing data
2. Lập báo cáo phân tích
3. Đo lường số lượng + chất lượng content
4. Đo lường lead/sale page + variant

## 1. Cross-vault Brain

- `../My Brain/` — vault anh em chứa kiến thức course / concept / story
- Marketing **chỉ đọc** Brain, không ghi ngược
- Tham chiếu: wikilink absolute `[[../My Brain/wiki/courses/X]]` hoặc frontmatter `brain_ref`

## 2. Hai lớp + 1 schema

### raw/ (input bất biến)

- Export CSV/XLSX từ dashboard
- Screenshot dashboard + post engagement
- Copy lead/sale page các phiên bản
- Tracking spreadsheet thủ công

### wiki/ (output AI sở hữu)

```
wiki/
├── sources/         # 1 page mỗi data dump
├── assets/
│   ├── lead-pages/
│   ├── sale-pages/
│   ├── contents/
│   ├── ads/
│   └── events/
├── reports/         # báo cáo pivot tuần/tháng/quý
├── concepts/        # framework marketing
├── entities/        # brand, persona, kênh
├── syntheses/       # tổng hợp xuyên asset
└── comparisons/     # so sánh variant
```

## 3. Quy ước page

### Frontmatter chuẩn

```yaml
---
title: Lead page Checklist 30s
type: asset
asset_kind: lead-page
brand: <brand>
brain_ref:
  program_code: <code>
  course_page: "[[../My Brain/wiki/courses/X]]"
tags: [lead-page, <brand>, funnel-top]
status: stable
---
```

### Track variant + metric

```yaml
variants:
  - id: v1
    label: Headline "Bí mật"
    url: https://example.com/lp?v=1
    period: "2026-04-15 → 2026-05-01"
    metrics: { traffic: 1240, opt_in: 180, cvr: 14.5 }
  - id: v2
    label: Headline "30 giây"
    period: "2026-05-02 → nay"
    metrics: { traffic: 980, opt_in: 165, cvr: 16.8 }
quality_score: 4
```

## 4. Metric quy ước

- Lead page: traffic, opt-in, CVR, bounce
- Sale page: traffic, ATC, checkout, order, CVR, AOV
- Ad: spend, CTR, CPM, CPA, ROAS
- Email: sent, open rate, click rate, unsubscribe
- Quality score: 1-5 chấm thủ công

Snapshot metric theo tuần trong section `## Metric snapshot`.

## 5. 4 workflow

A. **INGEST** — file mới trong raw/ → source page → asset page update
B. **REPORT** — báo cáo pivot tuần/tháng/quý
C. **QUERY** — hỏi dựa wiki
D. **LINT** — health check

## 6. Quy ước đặt tên

- Source: `src-<nguon>-<phamvi>-<ky>.md`
- Lead page: `lp-<brand>-<slug>.md`
- Sale page: `sp-<brand>-<slug>.md`
- Content: `<kenh>-<yyyy-mm>-<slug>.md`
- Ad: `ad-<platform>-<brand>-<slug>.md`
- Event: `<brand>-<version>.md`
- Report: `<ky>-<scope>.md`

## 7. Log

`## [YYYY-MM-DD] <action> | <subject>` — action: ingest | report | query | lint | manual.
```

---

## Bước 3 — Asset page template

Tạo asset đầu tiên — vd lead page:

`wiki/assets/lead-pages/lp-mybrand-checklist-30s.md`:

```markdown
---
title: Lead page Checklist 30s
type: asset
asset_kind: lead-page
brand: mybrand
brain_ref:
  program_code: emm
  course_page: "[[../My Brain/wiki/courses/EMM - Email Marketing Mastery]]"
tags: [lead-page, mybrand, funnel-top]
url_canonical: https://mybrand.com/lp/checklist-30s
launched: 2026-04-15
status: stable
variants:
  - id: v1
    label: "Headline 'Bí mật email'"
    url: "https://mybrand.com/lp/checklist-30s?v=1"
    period: "2026-04-15 → 2026-05-01"
    metrics: { traffic: 1240, opt_in: 180, cvr: 14.5 }
  - id: v2
    label: "Headline '30 giây'"
    url: "https://mybrand.com/lp/checklist-30s?v=2"
    period: "2026-05-02 → nay"
    metrics: { traffic: 980, opt_in: 165, cvr: 16.8 }
quality_score: 4
created: 2026-04-15
updated: 2026-05-29
sources:
  - "[[sources/src-ga4-2026-w21]]"
  - "[[sources/src-meta-ads-2026-w21]]"
---

# Lead page Checklist 30s

## Tổng quan

Lead page top funnel cho khoá Email Marketing Mastery. Mục tiêu opt-in email lấy "Checklist 30 giây setup email automation".

## Variant đã test

### v1 — Headline "Bí mật email" (15/04 - 01/05)

- Traffic: 1240
- Opt-in: 180
- CVR: 14.5%
- Notes: launch baseline

### v2 — Headline "30 giây" (02/05 - nay)

- Traffic: 980
- Opt-in: 165
- CVR: 16.8%
- Notes: hook "30 giây" mạnh hơn "Bí mật"

## Metric snapshot

| Tuần | Traffic | Opt-in | CVR | Ghi chú |
|---|---:|---:|---:|---|
| 2026-W17 | 320 | 48 | 15.0% | Launch v1 |
| 2026-W18 | 410 | 58 | 14.1% | Boost ads 500k/ngày |
| 2026-W19 | 510 | 75 | 14.7% | — |
| 2026-W20 | 480 | 65 | 13.5% | Drop nhẹ cuối tháng |
| 2026-W21 | 560 | 95 | 17.0% | Launch v2 |

## Chấm chất lượng

**Score: 4/5**

- Hook mạnh, đặc thù (✅)
- CTA rõ (✅)
- Form simple 2 field (email + tên) (✅)
- Thiếu social proof (logo customer, testimonial) — cải tiến v3 (⚠️)

## Insight

1. v2 hit CVR 17% — top quartile cho B2B SaaS lead page
2. Traffic giảm cuối tháng → pattern đáng theo dõi
3. Đề xuất A/B v3: thêm logo customer dưới form

## Liên kết

- Brain concept: [[../My Brain/wiki/concepts/Email Marketing Mastery]]
- Sale page sau lead: [[sp-mybrand-emm-2026]]
- Email sequence sau opt-in: [[../My Brain/wiki/courses/EMM - Email Marketing Mastery]]
```

---

## Bước 4 — Workflow INGEST data

Khi bạn export Meta Ads tuần này:

1. Tải CSV: `raw/meta-ads/2026-W22-spending.csv`
2. Trong Claude Code:

```
> Ingest raw/meta-ads/2026-W22-spending.csv. Pivot theo asset (lead/sale page).
```

Claude:
- Đọc CSV (skill xlsx)
- Tạo `wiki/sources/src-meta-ads-2026-w22.md` (summary)
- Update asset page liên quan → append metric snapshot row mới
- Update index + log
- Báo cáo 3-5 insight đáng chú ý

---

## Bước 5 — Workflow REPORT

Hàng tuần:

```
> Báo cáo tuần W22: tất cả lead page + sale page. Pivot CVR, spend, ROAS.
```

Claude:
- Đọc tất cả asset page
- Filter scope W22
- Pivot bảng + insight
- Tạo `wiki/reports/2026-W22-content-quality.md` với:
  - Bối cảnh
  - Số liệu chính
  - Insight (3-5 bullet)
  - Hành động đề xuất (kill v1 nếu CVR < 10%, scale v2 nếu ROAS > 3)
  - Nguồn

---

## Bước 6 — Workflow QUERY

```
> Lead page nào CVR cao nhất Q2? Vì sao?
```

Claude:
- Lọc asset_kind: lead-page
- Sort theo CVR latest snapshot
- Trả lời top + giải thích pattern (cross-ref Brain concept "Hook strength")

---

## Bước 7 — Cross-vault Brain query

```
> Sale page IPS đã optimize concept "Bộ não thứ 2" chưa?
```

Claude:
- Đọc `wiki/assets/sale-pages/sp-ips-*.md`
- Tham chiếu `../My Brain/wiki/concepts/Bộ não thứ 2.md`
- So sánh: sale page có dùng pattern từ concept không
- Suggest improvement

---

## Bước 8 — Variant tracking pattern

Mỗi asset có thể có 3-10 variant qua thời gian. Track:

```yaml
variants:
  - id: v1
    label: "Original"
    period: "2026-01-15 → 2026-03-15"
    metrics: { ... }
    status: killed       # killed | live | paused
  
  - id: v2
    label: "Headline test"
    period: "2026-03-16 → 2026-04-30"
    metrics: { ... }
    status: killed
    
  - id: v3
    label: "Form simplified"
    period: "2026-05-01 → nay"
    metrics: { ... }
    status: live
```

Variant status:
- `live` — đang chạy
- `paused` — tạm dừng
- `killed` — đã kill (metric thấp / off pattern)

---

## Bước 9 — Quality score

Chấm 1-5 mỗi asset:

| Score | Ý nghĩa |
|---|---|
| 5 | Xuất sắc — top quartile metric |
| 4 | Tốt — đúng pattern |
| 3 | Trung bình — chạy được |
| 2 | Yếu — sai pattern hoặc thiếu thành phần |
| 1 | Hỏng — cần viết lại |

Chấm thủ công khi bạn review hoặc Claude đề xuất kèm giải thích.

Section `## Chấm chất lượng`:

```markdown
## Chấm chất lượng

**Score: 4/5**

- Hook mạnh (✅)
- CTA rõ (✅)
- Thiếu social proof (⚠️) — cải tiến v3
```

---

## Bước 10 — Lint Marketing

```
> Lint Marketing wiki.
```

Claude scan:

**Trong `wiki/assets/`**:
- Asset có snapshot metric > 2 tuần không update → flag stale
- Asset `status: stable` không có metric → flag chưa đo
- Asset 2+ variant không có comparison report → gợi ý
- Variant CVR < trung bình ≥30% trong ≥2 tuần → gợi ý kill

**Trong `wiki/reports/`**:
- Report > 1 tháng số liệu không match asset hiện tại → stale
- Report tuần bị nhảy kỳ → flag

**Cross-link**:
- Asset reference course nhưng `brain_ref` trỏ sai → flag
- Concept Brain có page nhưng asset chưa link → gợi ý
- Source page chưa được asset nào reference → flag bỏ rơi

---

## Tiếp theo

Đọc tiếp: [[05-cross-vault-query]] — Query xuyên 2+ vault.
