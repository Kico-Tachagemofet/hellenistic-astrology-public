# Stage 1 — Data Extraction

> ## ⚠️ UNGUARDED FORK OVERRIDE (2026-05-18)
>
> References in this file to **`rules/fictional-subject-ethical-guard.md`**
> (consultation requirements before T1 population, subject-class
> identification gating extension topics, canon-source provenance
> discipline) are **NO-OP** in this fork.
>
> Stage 1 still extracts subject metadata (real-person / fictional+canon
> / synthetic — useful for canon-resonance observation in Stage 2 +
> chart-vs-canon Sun-sign divergence flagging in Appendix D). What
> changes: no Stage 1 step is gated by ethical-guard, no extension
> topics are flagged as off-limits, no `confidence:speculative` is
> mandated by subject-class membership.
>
> `[Source-only candidate]` flag, `confidence:speculative` for thin-
> testimony evidence, and Appendix D canon-source provenance flagging
> all REMAIN — they're data quality discipline, not ethical guard.

## Stage 1 Addendum (unguarded fork, 2026-05-18) — Birth-Time Precision Probe + Technique-Unlock Matrix

仿 parallel-reader-skill Step 3 / Step 3.5 / Step 7. 替换原 4 gate "通过/不通过" 二值。

### 时间精度 probe (Stage 1 必问)

Stage 1 数据 intake 时必须问用户 (或盘主):

```
1. 出生时间精度声明:
   □ 精确到分钟 (出生证 / 医院记录)
   □ 精确到分钟 (家人明确记忆)
   □ 大约 ±15 分钟 (家人大概回忆)
   □ ±1 小时
   □ 不确定

2. 时间来源 (仅当声明"精确到分钟"时追问):
   □ 出生证 / 医院记录 (有效精度 = ±分钟级)
   □ 家人明确记忆 (有效精度 = ±5 分钟)
   □ 家人大概回忆 (有效精度 = ±15 分钟)
```

**有效精度** = 用户声明 ✕ 时间来源修正 (per 上表). 写入 `chart-stage1.md`
元信息段; 后续所有 Stage 2/3 决策用有效精度, 不用声明精度.

### 时间精度 → 技法启用矩阵 (硬约束)

| 有效精度 | profections | planetary years | ZR (Fortune) | ZR (Spirit) | LB-of-life | Hyleg/Alcocoden | Lots (topical placement) | Lots (length-of-life) |
|---|---|---|---|---|---|---|---|---|
| ±分钟级 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ±5 分钟 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| ±15 分钟 | ✅ | ✅ | ⚠️ time-sensitive | ✅ | ⚠️ peak-year ±2y | ⚠️ | ✅ | ❌ |
| ±1 小时 | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ |
| 不确定 | ⚠️ (主年判定可能跨界) | ✅ (粗粒度) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

```
✅ = 正常 production + 正常 confidence tier
⚠️ = 可 produce 但 finding 必须带 [time-cal-X] 标 (X = required precision)
❌ = 不 produce; 该技法相关 finding 进入 Open Threads 注明 "需要 rectifier 升级时间精度"
```

**特殊触发: Lagna 度数在 0-3° 或 27-30°** (临近星座边界, Asc 改判风险):
- 即使有效精度 = ±5 分钟也降为 ⚠️
- 强烈建议 rectifier — Asc 跨星座会改变 Asc 主, 整盘 reading 全推倒重来

### Time-risk 等级 (写入 chart-stage1.md)

```
time_risk = HIGH
  - 有效精度 ≥ ±1 小时, 或
  - 有效精度 ≥ ±15 分钟 AND Lagna 度数在 0-5° 或 25-30°, 或
  - 时间精度声明"不确定"

time_risk = MEDIUM
  - 有效精度 ≥ ±15 分钟 (Lagna 安全), 或
  - 有效精度 ±5 分钟 + Lagna 边界

time_risk = LOW
  - 有效精度 ≤ ±5 分钟 + Lagna 安全
```

`time_risk` 决定:
- 整体 reading 的 confidence-tier 默认天花板
- 是否在 Stage 2 各 finding 加 `[time-risk:HIGH]` 旗标
- pre-validation R1 后是否强烈推荐 rectifier (per `pre-validation-reading.md` hit-rate table 联动)

### Pre-validation 联动 (per pre-validation-reading.md)

时间精度矩阵 + pre-validation R1 hit rate **共同**决定技法启用最终态:

```
最终技法启用 = MIN(时间精度允许的, pre-validation R1 命中率允许的)
```

例:
- 时间精度 = ±分钟级 (全技法可开) + pre-validation R1 hit rate 2/5 →
  最终启用 = profections only (受 R1 拉低)
- 时间精度 = ±15 分钟 (LB-of-life 关 / Lots length-of-life 关) +
  pre-validation R1 hit rate 5/5 → 最终启用 = profections + planetary years
  + ZR Spirit + Lots topical (受时间精度拉低; R1 高也不能解锁 LB)

### Rectifier 触发条件

任一满足即建议 (建议式, 非强制跳转):

- time_risk = HIGH AND 用户关心 timing/career/marriage 等需要精确时间的 topic
- Lagna 度数 0-3° 或 27-30° (Asc 改判风险)
- pre-validation R1 hit rate ≤ 3/5
- 用户主动要求

Rectifier 暂走 parallel-rectifier-skill (现行 hellenistic-rectifier sibling 还没建).
未来 sibling skill 拆分时 (per Task 4) 会建专属 `hellenistic-rectifier`.

---

> v2.2 Plan A.2 (2026-05-16) — newly created. Additive to v1; not part of `reading-workflow.md` step 0-7 (which remains for single-session legacy cases). New architecture uses Stage 1 → Stage 2 sessions via `method-index.md` routing.
>
> Last v2.x change: 2026-05-17 (v2.3 example-case retro — 10-item spec hardening pass, all inline per practitioner decision). Driven by example-case first-end-to-end-test review surfacing 10 spec gaps. Changes (all sections marked **v2.3 addition** inline below):
> 1. **Row_id schema** extended to include `T0-<AngleAbbrev>` for cardinal angles (Asc / MC / Desc / IC); previously angles were not row_id-bearing.
> 2. **Table 0 — Angles** introduced as new mandatory table (Asc / MC / Desc / IC with WSH-degree-vs-WSH-place divergence flags). MC/IC ≠ 10th/4th WSH double-channel warning canonized.
> 3. **Table 4 — Lots schema** extended with `Project status` column; T4 split into T4-canonical (Fortune + Spirit, direct-source per `rules/lots-and-fortune.md` v1 lock) and T4-reference (other Lots, reference-only / deferred per Appendix B template).
> 4. **Required appendices** A-E canonized (Angles source block / Lots formula+source+status / Parans reference-only / Canon-source provenance for fictional+canon subjects / Timing-overlay deferred-data registry).
> 5. **Raw-source artifact + SHA256 checksum** added to mandatory metadata fields.
> 6. **T6 coherence rule**: multi-role tier count enumerates only T4-listed Lots (canonical + reference); orphan citations of non-T4 Lots do not contribute to fold-tier count.
> 7. **Artifact-hygiene final-pass** added to Gate 4: no scratch text, no secondary tables, no inline self-correction notes before frozen artifact declared.
> 8. **Gate 4 checklist** updated items 4-6 to enforce T0 angles population, T4 canonical/reference split, T6 coherence, raw-source + appendices presence.
> 9. **Parans / fixed stars reference-only boundary** rule added to Discipline (specialist data not default Stage 1 evidence).
> 10. **Canon-source provenance discipline** added to Discipline for fictional+canon subjects per `rules/fictional-subject-ethical-guard.md`.
>
> Per project rule (Output format §"row_id schema" line ≈45 — "any future extension (new table, new id pattern) must route through a v2.x plan, not ad-hoc per-reading modification"): this update IS the v2.3 plan inline application, driven by example-case retro task #37; not ad-hoc per-reading. Pre-v2.3-example-case Stage 1 files (case-01..06a) remain valid under their authoring spec; new Stage 1 work from example-case onward follows this updated spec.
>
> Last v2.x change before this: 2026-05-16 (v2.2 Plan A.4) — added Stage 1 → Stage 2 Handoff Protocol section. Additive; existing Procedure / Discipline / Reference / Source sections unchanged.

## Purpose

Convert chart raw data into structured markdown tables that downstream Stage 2 / Stage 3 sessions consume directly. Stage 1 is the **deterministic data layer** of the v2.2 three-stage architecture: pure rule-driven, table-only, no narrative, no interpretation. Stage 1 output is the single source of truth for downstream topic modules (Stage 2) and cross-topic synthesis (Stage 3); those stages must not recompute or re-derive any Stage 1 datum themselves.

Stage 1 contains cascade errors at the **earliest** stage of a reading. 互溶 / reception / dignity / aspect / configuration detection errors caught here never propagate into Stage 2 narrative or Stage 3 synthesis. This file codifies (a) the output format for six required tables, (b) the step-by-step procedure with mandatory cross-reference gates against `rules/dignities-reference.md`, (c) the row-identifier scheme that lets Stage 3 mechanically trace any synthesis claim back to its Stage 1 source row, and (d) the self-audit checkpoint that must pass cleanly before Stage 2 dispatch.

## When to use

- Before any reading begins, after chart input is received and the data gate passes.
- Output is the **only** data source for Stage 2 topic modules and Stage 3 cross-topic synthesis.
- Stage 2 / Stage 3 sessions **MUST NOT** silently recompute dignity / reception / aspect data. If a downstream session detects a gap, inconsistency, or missing field in Stage 1, the only legitimate response is to **file an open thread** and request Stage 1 re-run — never paper over with silent recomputation. (This mirrors the module-independence principle in v2.2 Plan B §4.1.5.)
- Stage 1 is **not** part of `reading-workflow.md` step 0-7. That file remains the v1 single-session legacy workflow; new readings under the v2.2 stage-based architecture are dispatched via `method-index.md` routing.

## Output format

Stage 1 output is **twelve structured markdown tables (T0-T11)** plus required appendices A-E (per subject-class, see Required appendices section below). Tables split into two layers:

- **Structural layer (T0-T6)**: Angles / Per-planet audit / Reception network / Aspect matrix / Lots+rulers / Cluster check / Multi-Role registry. Pure rule-driven, no time-dependency beyond birth chart freeze.
- **Timing layer (T7-T11) — v2.4 addition (2026-05-18)**: T7 Profections / T8 Zodiacal Releasing (Fortune + Spirit) / T9 LB peaks + chapter-end events / T10 Hyleg / Alcocoden / T11 Open Threads. Every numerical value in T7-T10 MUST be generated via `tools/swe_timing.py` canonical (Egyptian-year 360d + 30d-month per Valens / Brennan Ch.18) — see Step 9.6 below. Hand-estimation of ZR chapter lengths from sign-year mapping is **prohibited** (case-09 17→27 yr correction 2026-05-18 surfaced the bug class).

Every row across all twelve tables carries a stable row identifier (`row_id`) for downstream trace-back. Stage 3 synthesis enforcement of trace-back (defined in v2.2 Plan B.5) depends on each Stage 1 row carrying a `row_id` that Stage 3 can mechanically cite and re-check.

(Pre-v2.3 Stage 1 files used six tables T1-T6 only and did not carry T0 or appendices. The v2.3 example-case retro added T0 + appendices as canonical. Pre-v2.4 Stage 1 files had T7-T11 timing tables but they were authored ad-hoc per case rather than spec-mandated; v2.4 codifies the schema and mandates canonical tool computation. Pre-v2.4 files **may carry hand-estimated ZR durations that need swe_timing.py re-verification** — case-09 retro flagged a 17→27 yr Egyptian-year correction.)

### Row identifier (row_id) schema

> **Gate 3 (row_id setup)**: Every row across all seven tables (T0-T6) must carry a stable `row_id` per the schema below. The `row_id` is the durable handle a Stage 3 synthesis cite uses to trace a claim back to its Stage 1 source row. This file defines the schema only; Stage 3 mechanical trace-back enforcement is defined in v2.2 Plan B.5. A missing or non-conforming `row_id` fails Gate 4.

| Table | row_id pattern | Examples |
|---|---|---|
| **T0 — Angles** (v2.3 addition) | `T0-<AngleAbbrev>` | `T0-Asc`, `T0-MC`, `T0-Desc`, `T0-IC` |
| T1 — Per-planet audit | `T1-<Planet>` | `T1-Sun`, `T1-Moon`, `T1-Mercury` |
| T2 — Reception network | `T2-<From>-<To>-<type>-<mutual\|oneway>` | `T2-Venus-Jupiter-domicile-mutual`, `T2-Saturn-Mars-domicile-oneway`, `T2-Sun-Saturn-bound-oneway` |
| T3 — Aspect / configuration | `T3-<P1>-<P2>` (P1, P2 alphabetical) | `T3-Jupiter-Saturn`, `T3-Mars-Venus`, `T3-Mercury-Sun` |
| T4 — Lots + rulers | `T4-<Lot>` | `T4-Fortune`, `T4-Spirit`, `T4-Eros` |
| T5 — Cluster check | `T5-<Sign>-<Place>` | `T5-Sag-6`, `T5-Can-1`, `T5-Pis-9` |
| T6 — Multi-Role registry | `T6-<Planet>` | `T6-Moon`, `T6-Venus`, `T6-Jupiter` |
| **T7 — Profections** (v2.4) | `T7-age<N>` | `T7-age28`, `T7-age33` |
| **T8 — Zodiacal Releasing** (v2.4) | `T8-<Lot>-L<n>-<Sign>` | `T8-Fortune-L1-Cap`, `T8-Spirit-L2-Aqu` |
| **T9 — LB peaks + chapter-end** (v2.4) | `T9-<Lot>-LB<N>` or `T9-<Lot>-L<n>-end` | `T9-Fortune-LB1`, `T9-Fortune-L1-end`, `T9-Spirit-LB1` |
| **T10 — Hyleg / Alcocoden** (v2.4) | `T10-Hyleg-<candidate>` or `T10-Alcocoden-<via-Hyleg>` | `T10-Hyleg-Moon`, `T10-Alcocoden-via-Asc` |
| **T11 — Open Threads** (v2.4) | `T11-OT<N>` | `T11-OT1`, `T11-OT8` |

Conventions for the schema:

- `<Planet>` uses canonical English names: `Sun`, `Moon`, `Mercury`, `Venus`, `Mars`, `Jupiter`, `Saturn`. Outer planets / Nodes are not registered in T1 / T3 / T6 unless a downstream module explicitly requests them.
- For T0 (v2.3 addition), `<AngleAbbrev>` ∈ { `Asc`, `MC`, `Desc`, `IC` }. Four angles per chart; one row each. Earlier project files (pre-v2.3) referenced angles by ad-hoc handles like `A-Asc`; the v2.3 canonical handle is `T0-Asc` (etc.) for Gate 3 trace-back.
- For T3, the pair is sorted alphabetically so each pair has exactly **one** canonical row_id (no `T3-Sun-Mars` vs `T3-Mars-Sun` ambiguity).
- For T2, `<From>` is the **guest** (the planet sitting in another's dignity) and `<To>` is the **host** (the dignity ruler of that sign). Direction discipline per `rules/aspect-reception-rules.md` anti-pattern 3.
- `<type>` for T2 ∈ { `domicile`, `exaltation`, `triplicity-primary`, `triplicity-secondary`, `triplicity-cooperating`, `bound`, `decan` }. Per-tier separation per `rules/aspect-reception-rules.md` §"Reception Type Taxonomy" Type 3 (triplicity tiers are distinct, not collapsed).
- For T5, `<Sign>` uses three-letter abbreviation (Ari / Tau / Gem / Can / Leo / Vir / Lib / Sco / Sag / Cap / Aqu / Pis) and `<Place>` is the WSH place integer (1–12).

`row_id` is the durable handle a Stage 3 cite must use when grounding an evidence chain in a Stage 1 fact. The schema is fixed at the table level by v2.2 Plan A.2 + v2.3 example-case retro (T0 addition); any future extension (new table, new id pattern) must route through a v2.x plan, not ad-hoc per-reading modification.

### Table 0 — Angles (v2.3 addition)

| row_id | Angle | Sign / Degree | WSH place containing degree | WSH place expected by tradition | Divergence flag | Sign-place ruler (audit ref to T1 row_id) | Raw source |

Four rows, one per cardinal angle (Asc / MC / Desc / IC). Field semantics:

- **Angle**: full name (`Ascendant`, `Medium Coeli`, `Descendant`, `Imum Coeli`).
- **Sign / Degree**: exact zodiacal longitude (sign + ° ' ").
- **WSH place containing degree**: which WSH place the angle's degree actually falls in. For Asc this is always the 1st by definition; for MC / Desc / IC it may **differ** from the traditional expected place when the Asc sits late or early in its sign.
- **WSH place expected by tradition**: the WSH place the angle is conceptually associated with: Asc=1st, Desc=7th, MC=10th, IC=4th.
- **Divergence flag**: when "WSH place containing degree" ≠ "WSH place expected by tradition" (typical for MC/IC when Asc is near sign boundary), write **`MC ≠ 10th WSH`** or **`IC ≠ 4th WSH`** etc. Critical for Stage 2 career / family topic dispatch: when divergence flag is set, downstream **must** consult both the WSH-place anchor (e.g., 10th WSH = Cancer in example-case) AND the MC-degree-in-actual-place (e.g., Leo). The two channels are not interchangeable in Hellenistic doctrine.
- **Sign-place ruler**: domicile ruler of the sign containing the angle's degree, with `T1-<Planet>` audit reference.
- **Raw source**: pointer to source artifact (e.g., `source PDF p.1 "Houses Asc."` or `derived: Asc + 180°` for Desc/IC).

Desc and IC are computed (Asc + 180°, MC + 180°) but recorded as separate rows so downstream sessions citing the 7th-cusp angle or the IC-degree can cite a row_id directly rather than re-deriving.

### Table 1 — Per-planet audit table

| row_id | Planet | Sign | Degree | WSH Place | Sect status | Domicile | Exaltation | Triplicity (by sect) | Bound | Decan | Angularity | Visibility / phase | Motion |

Seven rows, one per traditional planet (Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn). Field semantics defined in Procedure step 4.

### Table 2 — Reception network

| row_id | From (guest, in sign) | To (host of sign) | Reception type | Mutual? | Aversion or aspect? | Notes |

Populated per the deterministic procedure in `rules/aspect-reception-rules.md` §"Reception Detection Procedure (v2.2 additive)". One row per reception relation (each per-tier mutual reception is its own row; each one-way reception is its own row). Self-receptions (own-domicile, own-exaltation, etc.) are dignity fields on T1, **not** rows in T2 (anti-pattern 1 of `rules/aspect-reception-rules.md`).

### Table 3 — Aspect / configuration matrix

| row_id | From (P1) | To (P2) | Sign relation | Inclusive count | Element check | Aspect family | Degree distance | Applying / separating | Notes |

P × P matrix flattened to one row per unordered pair. For the seven traditional planets, that is C(7,2) = **21 rows**. Cells must be populated by **double-verification** (inclusive sign count AND element check) per Procedure step 6.

### Table 4 — Lots + rulers (v2.3-updated schema with Project status + canonical/reference split)

| row_id | Lot | Sign / Degree | WSH place | Ruler | Ruler placement (sign / degree / WSH place) | Ruler condition (audit ref to T1 row_id) | Lot-to-ruler aspect (per Gate 2) | **Project status** |

T4 is **split into two subgroups** per `rules/lots-and-fortune.md` v1 lock:

- **T4-canonical** — only `T4-Fortune` and `T4-Spirit` qualify. These are the v1-locked direct-source Lots (4-source triangulated per Brennan Ch.16 + Valens IX + Dorotheus I.27-28 + Firmicus IV.17-18). They are citable as `confidence:high` evidence in downstream Stage 2/3 findings. Project status column reads `direct-source canonical`.
- **T4-reference** — all other Lots (Eros / Necessity / Basis / Father / Mother / Children / Siblings / Marriage / Victory / Courage / Nemesis / Sons / etc.). These are reference-only / deferred per `rules/lots-and-fortune.md` "Candidate Lots" + "Other Lots" sections; computed for completeness but **MUST NOT** anchor `confidence:high` findings. Project status column reads `reference-only: [Source-only candidate]` or `reference-only: [NOT in v1]` per the per-Lot status in Appendix B template. Stage 2/3 citations of T4-reference Lots MUST carry the candidate/NOT-in-v1 flag in finding entry + tag `confidence:speculative` (or `low`) MAX.

Minimum two rows for T4-canonical: Fortune + Spirit (always required). T4-reference Lots are added when the reading scope requests them; each must carry an explicit `Project status` value naming its source-pool support and v1 lock status, with full per-Lot details enumerated in **Appendix B** (see Required appendices below).

Lot formulas per `rules/lots-and-fortune.md`; use the sect-correct direction.

### Table 5 — Cluster check

| row_id | Sign / WSH Place | Planets present | Count | Cluster flag |

One row per sign / WSH place that contains at least one of the seven planets. `Cluster flag` ∈ { `cluster (≥3)`, `co-presence only (2)`, `single tenant (1)` }. Lots, Nodes, and other non-planet factors are **not** counted toward the cluster threshold (per Force Notes discipline + v2.x §A.1 N4 candidate).

### Table 6 — Same-Planet Multi-Role registry

| row_id | Planet | All roles in chart | Multi-role tier |

One row per planet, listing **every** role the planet holds (sign tenant + WSH place ruler(s) + Lot ruler(s) + sect light + Asc ruler + natural significator(s)). Tier = total role count, annotated as `2-fold` / `3-fold` / `4-fold` / `5-fold` etc.

**T6 coherence rule (v2.3 addition)**: Lot rulerships enumerated in a T6 role count must reference **only T4-listed Lots** (canonical or reference). Orphan citations of Lots not in T4 (e.g., topic-specific Lots computed by ephemeris software but not added to T4 for this reading) do **NOT** contribute to the multi-role tier count. If a planet hosts a Lot that exists in source ephemeris but is not in T4, either (a) add the Lot to T4-reference with a Project status row, or (b) note the Lot's existence in T6 as `(out-of-T4 reference, not counted in tier)` without inflating the count. Prevents fold-tier inflation from non-canonical references.

## Required appendices (v2.3 addition)

In addition to the seven T-tables above (T0-T6), every Stage 1 file must include the following appendices when applicable to the chart's subject class. These appendices canonize project-pattern boundaries that were previously ad-hoc and prevent the most common Stage 1 → Stage 2 cascade gaps surfaced by example-case retro.

- **Appendix A — Angles source block** (always required): full enumeration of all 4 cardinal angles per Table 0 schema + 3-5 structural notes on angular dynamics for the chart (e.g., MC-degree-vs-10th-WSH divergence, Asc-degree proximity to angular planets, IC/Desc channel splits). Per Table 0 above plus narrative-level notes. Section header: `## Appendix A — Angles source block`.
- **Appendix B — Lots formula / source / project status** (required if T4-reference contains any Lot): per-Lot table with columns **Lot / Astro formula / Source attestation / Project status per `lots-and-fortune.md` + tag inventory / Stage 2/3 treatment**. Each row makes the canonical-vs-reference distinction visible and prescribes treatment for downstream Stage 2/3 citation. Section header: `## Appendix B — Lots formula / source / project status`.
- **Appendix C — Parans / fixed stars** (required if any paran / bright-star data is present in chart source): reference-only enumeration of planet-at-axis and star-at-axis parans + heliacal events of interest. **Default Stage 2/3 treatment: do NOT cite parans as evidence**. If a Stage 2 topic explicitly invokes specialist bright-star material, this appendix is the source handle; the citation must flag `confidence:speculative` per cross-source specialist tier discipline. Section header: `## Appendix C — Parans / fixed stars (reference-only, NOT default Stage 1 evidence)`.
- **Appendix D — Canon-source provenance** (required if subject is fictional + canon-marked per `rules/fictional-subject-ethical-guard.md`): structured table distinguishing canon facts / NOT canon / PROJECT-ASSIGNED data points. Explicit flag for any divergence between canonical-faithful chart and project-assigned-creative-premise chart (e.g., canonical [fictional-subject] birthday April 28 = Taurus Sun, but example-case uses Sun-Sagittarius project-creative chart). For Stage 2/3: any reading purporting "about canonical [subject]" must carry `confidence:speculative` + canon-resonance discipline. Section header: `## Appendix D — Canon-source provenance`. **NOT required** for real-person subjects (project-assigned provenance is implicit; covered by metadata field instead).
- **Appendix E — Timing overlay data (deferred per question trigger)** (required when timing-conditional findings are expected; recommended for all charts as forward-readiness): per-tag enumeration of what data each `timing-activation:*` tag requires + what source PDF page / on-demand-compute method supplies it. Includes Stage 2 dispatch rule that timing-conditional findings cannot dispatch without explicit target date/age. Section header: `## Appendix E — Timing overlay data (deferred per question trigger)`.

Subject class quick reference:

| Subject class | Appendix A | Appendix B | Appendix C | Appendix D | Appendix E |
|---|---|---|---|---|---|
| Real-person | required | required if T4-reference present | required if source has parans | NOT required | recommended |
| Fictional + canon-marked | required | required | required if source has parans | **required** | recommended |
| Pure synthetic test chart | required | required if T4-reference present | optional | optional | optional |

## Procedure

**Pre-flight.** Verify chart input completeness before any table population: (a) seven traditional planets each with sign + degree; (b) all 4 cardinal angles (Asc / MC / Desc / IC) with sign + degree (Asc + MC required; Desc + IC derivable from Asc/MC + 180°); (c) sect determination data (Sun above / below horizon at birth); (d) **raw-source artifact** (v2.3 addition) — the source PDF / screenshot / data export file must be saved to `charts/case-NN/source/` with a SHA256 checksum recorded in Stage 1 metadata so the artifact can be re-verified later. If any required input is missing, STOP and request input — do not infer or interpolate.

### Step 1 — Read chart input + verify data gate

Confirm:

- All seven traditional planet placements (sign + degree); degree precision is **required** for T1 bound / decan fields and T2 bound / decan reception detection.
- All 4 cardinal angles (Asc + MC required, Desc + IC derivable). Asc sign-and-degree drives all WSH place assignments.
- Sect determination data (Sun above or below the horizon at birth).
- For T3 applying / separating annotations: each planet's motion (direct / retrograde / stationary) and speed where the determination would be material.
- **Raw-source artifact saved locally** with `SHA256` checksum recorded; metadata field `Raw-source artifact:` populated with file path + checksum (v2.3 addition).
- **Subject class identified** (real-person / fictional+canon-marked / pure synthetic) per the Required appendices subject-class quick reference; for fictional+canon-marked subjects, `rules/fictional-subject-ethical-guard.md` must be consulted before T1 population to determine which extension topics (body/illness/death/longevity) are permitted under attenuated guard (v2.3 addition).

### Step 1.5 — Populate Table 0 (Angles) (v2.3 addition)

Populate Table 0 per the schema above. Four rows: Asc, MC, Desc, IC. For each:

1. Record exact sign + degree from chart source.
2. Identify the WSH place containing the angle's degree by counting whole signs from Asc forward.
3. Identify the WSH place expected by tradition (Asc=1st, MC=10th, Desc=7th, IC=4th).
4. **Divergence check**: if WSH-containing ≠ WSH-expected for MC/IC (which happens whenever Asc is past the early-degree zone of its sign), set the divergence flag explicitly (`MC ≠ 10th WSH` / `IC ≠ 4th WSH`). The divergence is a **dual-channel** condition for Stage 2: career / public-action topics consult both 10th-WSH-place (Hellenistic topic anchor) AND MC-degree-in-actual-place (visibility-point witness); family / foundation topics similarly consult 4th-WSH-place AND IC-degree-in-actual-place. The two are **NOT interchangeable**.
5. Identify the sign-place ruler (domicile ruler of the sign containing the angle's degree) and cite its T1 row_id.
6. Cite raw-source pointer (e.g., source PDF p.1 + page anchor).

### Step 2 — Determine sect

Sect = **day chart** if Sun is above the horizon at birth; **night chart** if Sun is below. Sect propagates into:

- T1 triplicity ruler tier assignment (consult `rules/dignities-reference.md` → "Triplicity Rulers By Sect" with the sect column matching).
- T1 sect status field (of-sect vs contrary-to-sect for benefics / malefics; sect light identification).
- T4 Lot formula direction (Fortune and Spirit formulas swap by sect).

### Step 3 — Compute Lots

Minimum: Fortune + Spirit. Add topic-specific Lots if the reading scope requests them. Apply the sect-correct direction per `rules/lots-and-fortune.md`. Each Lot becomes one T4 row in step 7.

### Step 4 — Populate Table 1 (per-planet audit)

For each of the seven planets, fill in every T1 field by **direct lookup against `rules/dignities-reference.md`** — no memory-based fills.

> **Gate 1 (mandatory cross-reference)**: Each T1 cell must be filled by consulting the specific `rules/dignities-reference.md` table named below. Before writing a cell, name the consulted table and row out loud (e.g., "consult `dignities-reference.md` → Egyptian Bounds, row Sagittarius, interval containing 22° = [21,26) → Saturn"). Do **not** rely on memory for any of the following lookups.

Cell-by-cell lookup discipline:

- **Domicile**: consult `rules/dignities-reference.md` → "Domicile Rulers By Sign", row = planet's sign. Record the domicile ruler. If the planet itself rules its sign, record `own domicile` (e.g., Moon in Cancer = `own domicile`).
- **Exaltation**: consult `rules/dignities-reference.md` → "Planetary Dignity And Debility By Planet", "Exaltation" column. Record the exaltation ruler of the planet's sign. If the planet itself is exalted in its sign, record `own exaltation` (and on T1 only — do **not** generate a T2 row for self-exaltation per `rules/aspect-reception-rules.md` anti-pattern 1). For the five signs without an exaltation ruler (Gemini, Leo, Sagittarius, Scorpio, Aquarius — derived from the table), record `no exaltation ruler for this sign`. Note exaltation **degree** separately (Sun 19° Ari, Moon 3° Tau, Mercury 15° Vir, Venus 27° Pis, Mars 28° Cap, Jupiter 15° Can, Saturn 21° Lib) when annotating the exaltation field; "in exaltation sign, not at degree" vs "at exaltation degree" is the distinction.
- **Triplicity (by sect)**: consult `rules/dignities-reference.md` → "Triplicity Rulers By Sect", row = element of planet's sign, columns = chart sect. Record **all three rulers separately**: primary, secondary, cooperating, each tagged with the sect (e.g., `fire @ night: Jupiter primary / Sun secondary / Saturn cooperating`). If the planet itself holds one of its own element's triplicity tiers, annotate that tier explicitly (e.g., `Moon has cooperating-ruler triplicity bonus`).
- **Bound**: consult `rules/dignities-reference.md` → "Egyptian Bounds", row = planet's sign. Identify the half-open interval `[a,b)` containing the planet's exact degree D. Record the bound ruler + the interval (e.g., `Saturn (Sag 22 in Sat bound [21,26))`). If D is missing or sign-only, record `degree-required: skip`.
- **Decan**: consult `rules/dignities-reference.md` → "Decans / Faces", row = planet's sign. Identify whether D falls in `[0,10)`, `[10,20)`, or `[20,30)`. Record the decan ruler + the slot (e.g., `Jupiter (Sag 1st decan [0,10))`). If D is missing or sign-only, record `degree-required: skip`.

Remaining T1 fields (no `dignities-reference.md` lookup; standard Hellenistic conventions):

- **Sect status**: of-sect vs contrary-to-sect. Benefics: Venus is of-sect at night, Jupiter is of-sect by day. Malefics: Mars is of-sect at night, Saturn is of-sect by day. Luminaries: Sun is sect light by day, Moon by night. Mercury aligns with whichever sect its morning-star / evening-star phase places it in (oriental = day-aligned, occidental = night-aligned).
- **WSH Place**: count whole-sign places from Asc (Asc sign = 1, next sign forward = 2, ..., twelfth sign = 12).
- **Angularity**: 1 / 4 / 7 / 10 = angular; 2 / 5 / 8 / 11 = succedent; 3 / 6 / 9 / 12 = cadent.
- **Visibility / phase**: above-horizon vs below-horizon at birth. For Mercury and Venus, also note morning star vs evening star, approximate degrees from Sun, and under-beams vs out-of-beams (rule-of-thumb: under-beams ≤ 15° from Sun, with cazimi at ≤17').
- **Motion**: direct / retrograde / stationary, with speed annotation when material (fast / mean / slow).

### Step 5 — Populate Table 2 (reception network)

Apply the procedure defined in `rules/aspect-reception-rules.md` §"Reception Detection Procedure (v2.2 additive)" **verbatim**. Do **not** re-invent or shortcut the reception detection logic. Specifically:

1. Run the **per-planet pass** (steps 1–3 of that procedure) for each planet — five reception type lookups against `rules/dignities-reference.md` per planet, plus the self-reception filter.
2. Run the **pair pass** (steps 4–6 of that procedure) for every unordered pair (P, Q) — mutual reception check per tier independently, one-way flag, aversion+reception annotation.
3. Apply the **self-reception filter**: self-receptions become T1 dignity fields, never T2 rows.
4. Annotate every T2 row with the **four-cell aversion+reception matrix flag** per `rules/aspect-reception-rules.md` §"Aversion + Reception Handling" (Aspect × Mutual / Aspect × One-way / Aversion × Mutual / Aversion × One-way).
5. Guard against the four anti-patterns enumerated in that file (self-exaltation as mutual; one-way as mutual without reciprocal check; "receives" direction confusion; missing aversion annotation).

This step **must not** re-derive reception logic; it is a thin wrapper around the canonical procedure in `rules/aspect-reception-rules.md`. If the canonical procedure changes, T2 population behavior changes; this spec does not duplicate the logic.

### Step 6 — Populate Table 3 (aspect / configuration matrix)

For each of the 21 unordered planet pairs:

> **Gate 2 (mandatory double-verify)**: Every aspect cell must be verified by **both** Method (a) inclusive sign count **AND** Method (b) element check, independently. Both methods must converge before the aspect family is recorded. Do **not** rely on memory of any aspect family between two specific signs.

**Method (a) — Inclusive sign count.** Count the signs from P1's sign to P2's sign, **inclusive of both endpoints**. Count in the shorter direction (forward or backward) and record which. Mapping:

- 1 inclusive = same sign = **conjunction** (by sign)
- 2 inclusive = adjacent signs = **aversion** (no major aspect; semi-sextile is not a Hellenistic aspect)
- 3 inclusive = **sextile**
- 4 inclusive = **square**
- 5 inclusive = **trine**
- 6 inclusive = **aversion** (quincunx / inconjunct = no testimony in the Hellenistic frame)
- 7 inclusive = **opposition**

**Method (b) — Element check.**

- Same element (fire-fire, earth-earth, air-air, water-water) and inclusive 1 → **conjunction** (always; same sign is same element by definition).
- Same element and inclusive 5 → **trine** (always; trines are always same element).
- Same element and inclusive 7 → **opposition** (impossible: opposed signs are always cross-element complementary, not same element; if you reach this state, recount).
- Complementary element (fire-air or water-earth) and inclusive 3 → **sextile**.
- Complementary element (fire-air or water-earth) and inclusive 7 → **opposition** (e.g., Aries-Libra fire-air, Cancer-Capricorn water-earth).
- Cross-element (fire-water, fire-earth, air-water, air-earth) and inclusive 4 → **square**.
- Cross-element and inclusive 2 or 6 → **aversion**.

Element assignments (standard): fire = Aries / Leo / Sagittarius; earth = Taurus / Virgo / Capricorn; air = Gemini / Libra / Aquarius; water = Cancer / Scorpio / Pisces.

**Discrepancy rule.** If Method (a) and Method (b) disagree (e.g., Method (a) yields "trine" but the two signs are cross-element), **STOP**. Recount the inclusive sign count from scratch; recheck the element of each sign against the standard assignments above; only proceed when both methods converge on the same aspect family. This guardrail catches the common "I remember Sag-Pis is a trine" memory-based error — Sag-Pis is 4 inclusive forward, fire-water cross-element, = **square**, not trine. The `samples/topic-reading-template.md` audit-pass header documents this exact error class recurring 17 times in the original draft before Gate 2 was made explicit.

Cell content for each T3 row:

- `From` (P1), `To` (P2) — alphabetical canonical ordering.
- `Sign relation`: e.g., `Sag-Pis`, `Can-Sco`, `Ari-Lib`.
- `Inclusive count`: integer + direction (e.g., `4 incl. forward`, `5 incl. backward`).
- `Element check`: e.g., `fire-water cross-element`, `water-water same element`, `fire-air complementary`.
- `Aspect family`: conjunction / sextile / square / trine / opposition / aversion. Must agree with both Method (a) and Method (b).
- `Degree distance`: absolute degree gap between the two planet positions (modulo sign-wrap), expressed in degrees (e.g., `8°`, `21°`).
- `Applying / separating`: per the faster planet's motion relative to the slower; `n/a` when either planet is stationary or when the configuration is by sign only without degree-tight contact.
- `Notes`: tight-degree flags (≤3° = `TIGHT`, ≥10° = `WIDE`), reception overlap reminder (cite the relevant T2 row_id if the pair has reception), aversion-with-reception flag (e.g., `aversion despite mutual reception — see T2-Venus-Jupiter-domicile-mutual`).

### Step 7 — Populate Table 4 (Lots + rulers) — v2.3-updated for canonical/reference split

For each Lot computed in step 3:

- Record `Sign / Degree` and `WSH place` (per Asc; one row per Lot).
- Determine `Ruler` by consulting `rules/dignities-reference.md` → "Domicile Rulers By Sign", row = Lot's sign.
- Record the ruler's placement (sign, degree, WSH place) — copy from T1.
- `Ruler condition (audit ref to T1 row_id)`: cite the ruler's T1 row_id (e.g., `audit per T1-Jupiter`) so downstream sessions can trace the ruler's condition back to T1 rather than recompute. Do **not** restate the ruler's dignity / sect / motion in T4 — that is what the T1 row_id reference is for.
- `Lot-to-ruler aspect (per Gate 2)`: compute the sign-based aspect between the Lot's sign and the ruler's sign using the Gate 2 double-verify procedure; record the aspect family + inclusive count + element check, just like a T3 cell.
- **`Project status`** (v2.3 addition): set per `rules/lots-and-fortune.md` v1 lock and tag inventory v2.1 status:
  - Fortune + Spirit → `direct-source canonical` (citable as `confidence:high` evidence).
  - Eros → `reference-only: [Optional / topic-specific]` (deferred per Candidate Lots).
  - Other Hermetic / Dorothean / Valentine topic Lots (Necessity, Basis, Father, Mother, Children, Siblings, Marriage, Victory, Courage, Nemesis, Sons, etc.) → `reference-only: [NOT in v1]` (deferred to v2.x topic-Lot expansion).
  - For each `reference-only` Lot, downstream Stage 2/3 citations **must** carry the `[Source-only candidate]` or `[NOT in v1]` flag in finding entry and tag `confidence:speculative` (or `low`) MAX.

**Split presentation**: render T4 as two distinct sub-tables under headers `### T4-canonical — direct-source Lots (v1 locked per lots-and-fortune.md)` and `### T4-reference — reference-only Lots (deferred per Appendix B; NOT direct-source evidence)`. Keep both under the umbrella `## T4 — Lots + rulers` section. Place a brief intro before the canonical sub-table summarizing the canonical/reference split and its enforcement.

**Appendix B requirement**: when T4 contains any T4-reference Lot, the full per-Lot Appendix B table is required (formula + source attestation + project status + Stage 2/3 treatment — see Required appendices section above for full schema).

### Step 8 — Populate Table 5 (cluster check)

Iterate over signs / WSH places that contain at least one of the seven planets. For each:

- Count planets in that sign/place. **Do not** count Lots, Nodes, or other non-planet factors toward the cluster threshold.
- `Cluster flag`:
  - Count ≥ 3 → `cluster (≥3)`.
  - Count = 2 → `co-presence only (2)` (explicitly "not cluster").
  - Count = 1 → `single tenant (1)`.

Empty signs / places are not registered as T5 rows.

### Step 9 — Populate Table 6 (Same-Planet Multi-Role registry)

For each of the seven planets, enumerate **every** role it holds in this chart:

- **Tenant** of its sign's WSH place (always one role per planet, by definition).
- **Ruler** of any WSH place whose sign it rules. A planet can rule **two** WSH places if it has two domiciles: Saturn (Capricorn + Aquarius), Jupiter (Sagittarius + Pisces), Mars (Aries + Scorpio), Venus (Taurus + Libra), Mercury (Gemini + Virgo). The Sun and Moon each rule only one. Two-domicile cases must be captured explicitly — missing one is a common error.
- **Ruler** of any T4-listed Lot (cross-reference T4; one role per Lot ruled). **T6 coherence rule (v2.3 addition)**: only Lots present in T4 (canonical or reference) contribute to the role count. If a planet rules a Lot that exists in source ephemeris but is **not** in T4, either (a) add the Lot to T4-reference with a Project status row, or (b) note the Lot in the T6 role list as `(out-of-T4 reference, not counted in tier)` — do NOT inflate the tier count with orphan references. Prevents fold-tier inflation surfaced as example-case retro item #9.
- **Sect light** status: Sun if day chart, Moon if night chart.
- **Asc ruler** status if the planet rules the Asc sign (Sun: Asc Leo; Moon: Asc Cancer; etc.). The Asc-ruler role is enumerated **separately** from its WSH 1st-ruler role even though they coincide structurally; Asc-ruler is a distinguished Hellenistic role (steers life direction) and is named separately for traceability.
- **Natural significator** role(s): Sun = vitality / father; Moon = body / mother; Mercury = mind / messenger / siblings; Venus = love / aesthetics / women; Mars = war / cut / action; Jupiter = expansion / wisdom / fortune; Saturn = constraint / depth / endings.

`Multi-role tier` = total roles listed, annotated as `2-fold` / `3-fold` / `4-fold` / `5-fold` etc. When the same planet's roles converge across multiple topics, Same-Planet Multi-Role Handling applies in Stage 2 (deepens a single line of evidence; does not double independent testimony count) — but T6 only records the registry; Stage 2 does the application.

### Step 9.5 — Populate required appendices (v2.3 addition)

Per the Required appendices section above, populate the appendices applicable to the chart's subject class:

- **Appendix A (always)** — full Angles source block expanding on Table 0 with 3-5 narrative angular-dynamics notes (e.g., Asc-degree proximity to angular planets, MC/IC divergence dual-channel implications, Desc empty-sign routing through the 7th-ruler's chain).
- **Appendix B (when T4-reference present)** — full per-Lot table with Astro formula / Source attestation / Project status per `lots-and-fortune.md` + tag inventory v2.1 / Stage 2/3 treatment. Each row makes canonical-vs-reference distinction visible at row level; ends with Stage 2 dispatch rule reminder.
- **Appendix C (when parans / bright-star data in source)** — selected parans I/II + heliacal events of interest, all marked reference-only specialist; explicit "do NOT cite as evidence by default" + source PDF page references.
- **Appendix D (fictional + canon-marked subjects only)** — structured canon / NOT canon / PROJECT-ASSIGNED table + critical provenance flag (e.g., chart's Sun-sign vs canonical Sun-sign mismatch) + canon character facts selection for Stage 2 canon-resonance reference (under `confidence:speculative` discipline).
- **Appendix E (recommended for all charts)** — per-tag enumeration of what data each `timing-activation:*` tag requires + source PDF page / on-demand-compute method + Stage 2 dispatch rule that timing-conditional findings cannot dispatch without explicit target.

Each appendix has a defined section header per the Required appendices section above. Do not stub appendices (e.g., empty Appendix B because "no reference Lots needed yet"); if not applicable, omit entirely. If applicable, populate fully.

### Step 9.6 — Populate timing tables T7-T11 via canonical tool (v2.4 addition, 2026-05-18)

> **Gate 5 (timing canonical-tool mandate)**: T7-T10 numerical values (profected year-lord per age; ZR L1 + L2 dates + signs + rulers; LB peak dates; chapter-end dates; Hyleg-Alcocoden bound-lord assignments) MUST be generated by running `tools/swe_timing.py` against the chart. **Do NOT hand-estimate ZR chapter lengths from sign-year-mapping by memory or by mental arithmetic** — this surfaced the case-09 17→27 yr bug (Cap L1 was modeled as 17 solar years by ad-hoc reasoning when canonical Egyptian-year is 27). The tool is the single source of truth for Hellenistic Egyptian-year (360 d / 30-d month per Valens / Brennan Ch.18) canonical computation; it has been cross-validated against astro-seek archive to arc-second / day-level precision (case-09 verification 2026-05-18).

**Tool invocation** (Windows PowerShell, UTF-8 env):

```powershell
$env:PYTHONIOENCODING='utf-8'
python tools/swe_timing.py `
  --birth-date YYYY-MM-DD `
  --birth-time HH:MM `
  --target-date YYYY-MM-DD `
  --asc-sign <three-letter, e.g. Sco> `
  --fortune-sign <three-letter, e.g. Sco> `
  --spirit-sign <three-letter, e.g. Lib> `
  --max-years 80 `
  --output-format markdown `
  --case-label "case-NN <Subject>"
```

**Arg sourcing** (all from Stage 1 already-computed data):
- `--birth-date` / `--birth-time`: from chart input intake (Step 1). **`--birth-time` is UT** (not local time); apply timezone offset before passing.
- `--target-date`: typically today's date (for "current period" finding); for retrospective audit use the event date.
- `--asc-sign`: from T0 Asc row's sign.
- `--fortune-sign` / `--spirit-sign`: from T4-canonical Lot rows (Fortune sign and Spirit sign).
- `--case-label`: for traceability in the markdown output.

**Output handling**:
- Save full tool output to `charts/case-NN/timing-canonical-YYYY-MM-DD.md` as a separate companion file (canonical block, reusable for any future target-date query).
- Paste relevant slices into `chart-stage1.md` T7-T10 sections. Each pasted block carries the flag `[swe-canonical-Egyptian-year, verified YYYY-MM-DD]` at the table header.
- For findings that cite T8 dates, propagate the `[swe-canonical-Egyptian-year]` flag into the finding's audit-refs section so downstream Stage 2 / Stage 3 readers know the timing is canonically verified.

**T7 — Profections** (always populate; only depends on birth date + Asc sign, time-precision-independent for year-level granularity): table with columns Age / Period start / Period end / Profected place / Profected sign / Year-lord. Default render: current age ± 5 ages (i.e., 10-year window centered on `--target-date`).

**T8 — Zodiacal Releasing (Fortune + Spirit)**: gated by 时间精度 matrix (Addendum line 48; ZR Fortune ≥ ±5 min, ZR Spirit ≥ ±15 min). Two sub-tables:
- **T8-Fortune**: L1 cycle (rows: # / L1 Sign / Start / End / Years (Eg) / Ruler) — show all L1 chapters from birth through `--target-date` + 1 (currently active + next). L2 sub-periods within currently active L1 (rows: # / L2 Sign / Start / End / Months (Eg) / Ruler / Notes — aversion-to-L1 candidates flagged ⚠).
- **T8-Spirit**: same structure, Spirit lot.
- **Distinguish** chapter end (zodiacal sequence transition) from LB pivot (aversion-LB rule jump). The tool currently has LB rule **disabled** pending canonical-source clarification; it flags aversion candidates only. Chapter-end dates come from pure zodiacal sequence (27 Eg yr for Cap, 30 for Aqu, etc.). **Never conflate the two** — case-09 retro caught a "chapter end = LB date" conflation that propagated through 34 files.

**T9 — LB peaks + chapter-end events**: gated by 时间精度 matrix (LB-of-life ≥ ±5 min). Rows for each LB event (per tool aversion-candidate flag + per PDF / astro-seek archive if cross-referenced) + rows for L1 chapter-end transitions (separate from LB events). Columns: Lot / Date / Sign / Age / Event type (LB pivot / L1 chapter end) / Status.

**T10 — Hyleg / Alcocoden**: gated by 时间精度 matrix (Hyleg/Alc ≥ ±5 min). Apply Ptolemy III.11 night-order (Moon → Sun → Fortune → Asc) or day-order; Hyleg-allowed places 1/7/10/11 ± 9; Alcocoden = bound-lord of Hyleg. The tool provides bound-lookup for the Asc / Fortune positions; analyst applies the Hyleg eligibility filter + Alcocoden bonification/maltreatment narrative (not tool-computable).

**T11 — Open Threads**: free-form list of Stage 1 caveats / methodological flags / data-precision warnings. Always include an OT for any technique disabled by 时间精度 matrix.

**Tool-output skipping**: if 时间精度 matrix marks a technique ❌ (disabled), skip generating that table; record reason in T11 instead of populating with cap'd-confidence numbers.

**Re-verification trigger**: if the chart-stage1.md was authored pre-2026-05-18 (pre-v2.4), the timing tables may use hand-estimated ZR durations. Run `tools/swe_timing.py` against the chart and diff against existing T8 — if any chapter length differs by more than ±1 day, replace the T8 block with the canonical output and trigger a downstream propagation pass (case-09 retro template: replace T8 + propagate to all files citing the old number + reframe interpretive findings that anchored on the wrong chapter-end).

---

### Step 10 — Self-audit checkpoint

Before dispatching to Stage 2, verify each of the following items explicitly.

> **Gate 4 (checkpoint enforcement)**: If **any** item below fails or is uncertain, **STOP**. Fix Stage 1 immediately. Do **not** enter Stage 2 with a failing checkpoint. Stage 2 / Stage 3 sessions are forbidden from silently re-computing Stage 1 data; the only legitimate downstream response to a Stage 1 gap is to **file an open thread** and request Stage 1 re-run (this mirrors the module-independence principle in v2.2 Plan B §4.1.5).

Checkpoint items — a **values-lookup-verified** pass, not a fields-present pass:

- [ ] **Raw-source artifact saved + SHA256 in metadata** (v2.3 addition): source PDF / data export saved to `charts/case-NN/source/` with checksum recorded in the chart-stage1 metadata block.
- [ ] **Subject class identified** (real-person / fictional+canon-marked / pure synthetic) and ethical-guard policy per `rules/fictional-subject-ethical-guard.md` consulted where applicable (v2.3 addition).
- [ ] **All 4 cardinal angles in T0** (v2.3 addition): Asc / MC / Desc / IC populated; MC/IC vs 10th/4th-WSH divergence flag set where applicable; sign-place ruler T1 audit ref attached to each angle.
- [ ] All 7 planets have full T1 audit fields, with **each cell's value lookup-verified against the specific `rules/dignities-reference.md` table named in step 4** (not merely "field is non-empty"). Per the audit-pass header on `samples/topic-reading-template.md`, the original draft had every T1 field present but 17 values wrong against `dignities-reference.md`; the values-verified pass is the explicit guardrail against that error class.
- [ ] All T2 reception relations are explicit, with mutual vs one-way distinguished per `rules/aspect-reception-rules.md` procedure (no anti-pattern 2 errors).
- [ ] Every T2 row carries the four-cell aversion+reception matrix annotation (no anti-pattern 4 errors).
- [ ] No T2 row is a self-reception (self-receptions live on T1 as dignity fields per anti-pattern 1).
- [ ] All 21 T3 aspect cells have passed **Gate 2 double-verify** (inclusive sign count AND element check both confirmed; any discrepancy resolved by recount, not by picking one method).
- [ ] **T4 split into T4-canonical (Fortune + Spirit) and T4-reference (other Lots if any)** (v2.3-updated): all Lots have ruler + ruler placement + audit ref to T1 row_id + Lot-to-ruler aspect (Gate 2 applied) + **Project status column populated** per `rules/lots-and-fortune.md` v1 lock (canonical: `direct-source canonical`; reference: `reference-only: [Source-only candidate]` or `reference-only: [NOT in v1]`). Stage 2/3 sessions citing T4-reference Lots are required to carry the candidate/NOT-in-v1 flag.
- [ ] T5 cluster threshold applied correctly (≥3 planets for cluster; Lots / Nodes excluded from count).
- [ ] T6 Multi-Role registry is complete: every planet's roles enumerated; two-house rulership cases (Saturn / Jupiter / Mars / Venus / Mercury) captured explicitly; **T6 coherence rule honored** (v2.3 addition): only T4-listed Lots contribute to role count; orphan non-T4 Lot references either added to T4-reference or noted as `(out-of-T4 reference, not counted in tier)`.
- [ ] Every row across all seven tables (T0-T6) carries a `row_id` conforming to the schema above; T3 pairs are alphabetically ordered (no `T3-Sun-Mars` vs `T3-Mars-Sun` collision); T2 direction is guest→host (no anti-pattern 3 errors).
- [ ] **Required appendices present per subject-class quick reference** (v2.3 addition): A (always) + B (if T4-reference) + C (if parans in source) + D (if fictional+canon-marked) + E (recommended). Each appendix populated per Step 9.5 spec; no stub appendices.
- [ ] **Artifact-hygiene final-pass complete** (v2.3 addition): no scratch text in finalized artifact (no "Let me recount...", no "wait recompute" mid-row notes, no "additional rows" secondary tables left over from authoring). Every T-table is a single consolidated table with all rows in canonical order. Every appendix has a populated body (no `[TBD]` / `[fill in]` placeholders). The frozen artifact must be a clean read-only artifact, not an in-progress draft. This guardrail addresses example-case retro item #8 where first-pass authoring scratch was left in the "frozen" file and caused state inconsistency with appendices.
- [ ] **T7-T11 timing tables populated per Step 9.6 + canonical tool flag attached** (v2.4 addition, 2026-05-18): every T7-T10 numerical value (profected year-lord per age; ZR L1+L2 dates / signs / rulers / Egyptian-year chapter lengths; LB peak dates; chapter-end dates; Hyleg-Alcocoden bound-lord assignments) was generated by `tools/swe_timing.py` — not hand-estimated, not from PDF transcription alone, not from sign-year mental arithmetic. Each T7-T10 table header carries the flag **`[swe-canonical-Egyptian-year, verified YYYY-MM-DD]`**. The companion canonical block is saved to `charts/case-NN/timing-canonical-YYYY-MM-DD.md`. **Chapter end ≠ LB pivot** distinction explicitly preserved in T8 + T9 (case-09 retro 2026-05-18: a chapter-end-vs-LB-date conflation propagated through 34 files; this audit item is the guardrail against repeat). Tables for techniques disabled by 时间精度 matrix (Addendum line 48) are skipped, and the skip-reason is recorded in T11.

### Step 11 — If checkpoint passes

Output the seven tables (T0-T6) plus required appendices A-E (per subject-class) as the complete Stage 1 deliverable, ready for Stage 2 dispatch per `rules/chart-finding-index-workflow.md` §1 (v2.3 chart-finding-index source-driven architecture). Stage 1 is then **frozen** for this reading; Stage 2 / Stage 3 sessions read from this output and do not write back.

### Step 12 — If checkpoint fails

STOP. Fix the failing item(s) in Stage 1. Re-run the affected steps (4, 5, 6, 7, 8, or 9 as relevant) plus the checkpoint. Do not proceed to Stage 2 until the checkpoint passes cleanly. If a failure indicates a deeper structural gap (e.g., reception detection produces contradictory mutual flags across two passes, or a `dignities-reference.md` row is itself ambiguous), escalate to `pending-verifications.md` rather than papering over.

## Stage 1 → Stage 2 Handoff Protocol (v2.3-updated paths + scope)

Stage 1 完成后的 dispatch 流程，防止 unverified Stage 1 cascade 进 Stage 2。Step 10 Gate 4 是 Stage 1 session 内部 self-audit；本 protocol 在其之上再加一层 **independent external audit session**，目的是把 single-pass cognition load 造成的 cascade error 挡在 Stage 2 narrative 之前。两层 audit 不重复：Gate 4 是 author session 自查（结构性 fields-present + values-lookup-verified 的初筛），external audit 是 fresh-eye session 复核（独立的 lookup 重跑 + Reception Detection 重跑 + Gate 4 全项再走一遍）。

1. Stage 1 session 完成 → 产出 `charts/case-NN/chart-stage1.md`（NN = case 编号；v2.3 路径，per chart-finding-index-workflow.md §"Architecture context"）+ 同目录保存 raw-source artifact (`charts/case-NN/source/<source-file>` + SHA256 checksum 记入 chart-stage1.md metadata).
2. **不直接 dispatch Stage 2**。
3. **第一步 — 独立 audit session**：dispatch 一个独立 session 做 Stage 1 audit。Audit session 输入 = `charts/case-NN/chart-stage1.md` + raw-source artifact (`charts/case-NN/source/`) + 项目 rule files (`rules/dignities-reference.md`, `rules/aspect-reception-rules.md`, `rules/stage1-data-extraction.md`, `rules/lots-and-fortune.md`, `rules/fictional-subject-ethical-guard.md` if applicable)。流程 = 验证全 7 表 (T0-T6) + 全 Required appendices (A-E per subject class) + 跨 reference `rules/dignities-reference.md` + run reception detection per `rules/aspect-reception-rules.md` §"Reception Detection Procedure (v2.2 additive)" + check Gate 4 checkpoint 全项 (含 v2.3 加的 source artifact / T0 / T4 split / T6 coherence / appendices / artifact-hygiene 6 items)。Audit session 输出 `charts/case-NN/chart-stage1-audit.md`：`pass` / `fail` / `pass with corrections (cosmetic / structural)` + corrections list。
4. **第二步 (if audit pass)** — dispatch Stage 2 topic sessions per `rules/chart-finding-index-workflow.md` §1 (v2.3 chart-finding-index source-driven architecture). 每个 Stage 2 session 收到：`charts/case-NN/chart-stage1.md` (含全 7 tables + 全 appendices) + 对应 topic-module spec from `rules/topic-modules.md` §"Per-Topic Module Specifications" (still-valid sections per v2.2 → v2.3 slug mapping; partial supersession banner at top of `rules/topic-modules.md` clarifies what's still valid). Stage 2 session **不** recompute Stage 1 数据；read chart-stage1.md as authoritative single source of truth.
5. **第二步 (if audit fail)** — STOP。Fix Stage 1 per audit report；re-audit；只有 audit pass 才能进 Stage 2。
6. Stage 2 sessions 全部完成后 (15 modules max for default 9 + extension 6 per chart-finding-index-tags.md v2.1) → dispatch Stage 3 chart-finding-index consolidation session per `rules/chart-finding-index-workflow.md` §2.

**Why a separate audit session**：single-pass cognition load 是 cascade error 的根因（per `samples/topic-reading-template.md` 上的 17 Stage-1 错误 + 1 Stage-3 cascade，及 example-case retro 显示的 2 轮额外 cleanup 需求）。独立 audit session 给 Stage 1 一个 fresh-eye verification 通道，把 reception / dignity / aspect 错误 + v2.3 spec compliance gaps (T0 / T4 split / appendices) 挡在 Stage 2 narrative 之前。

**Handoff artifact 命名规范 (v2.3)**：

- Stage 1: `charts/case-NN/chart-stage1.md` (含 T0-T6 + appendices A-E)
- Stage 1 raw source: `charts/case-NN/source/<source-file>.pdf|png|json|csv` (+ SHA256 in chart-stage1.md metadata)
- Stage 1 audit report: `charts/case-NN/chart-stage1-audit.md`（pass / fail + corrections list；audit session output）
- Stage 2 per-topic findings: `charts/case-NN/topic-findings/<slug>.md` (slug per chart-finding-index-tags.md v2.1 topic dim; per topic-finding 轻 schema in chart-finding-index-workflow.md §1)
- Stage 3 chart-finding-index: `charts/case-NN/chart-finding-index.md` (含 §A Stage 1 raw embedded + §B chart-level findings + §C cross-finding refs + §D 整盘 patterns per chart-finding-index-workflow.md §2)
- Stage 3 utility: `charts/case-NN/question-index.md` (reader-question → finding refs mapping)

All v2.3 artifacts live under `charts/case-NN/`. **Pre-v2.3 path note**: v2.2-era cases (case-01..06a) used `cases/case-NN-*.md` flat naming + Stage 1 at project root; those files remain in `cases/` per pre-v2.3 convention and are not retroactively moved. Pre-v2.3 cases are also not subject to v2.3 Stage 1 spec (T0 / appendices / Project status column not retrofitted to legacy cases). New work from example-case onward follows v2.3 paths + spec.

Output discipline: NO TL / portrait-essay / reader-deliverable rendering layer exists in v2.3 (deprecated per v2.3 reframe; see `v2.3-chart-finding-index-architectural-plan.md`). The chart-finding-index source layer is the final deliverable; decision-maker queries it directly by tag combination.

## Discipline

- **No narrative in Stage 1.** Stage 1 is data, not story. No "this means", "this suggests", "the chart shows", "the native is" — those belong to Stage 2 / Stage 3.
- **No interpretation.** Do not infer what a configuration "indicates" about character, fate, or topic outcome. Interpretation is Stage 2's job. Stage 1 records facts; Stage 2 reads them.
- **Tables-first; structured-appendix-permitted, no interpretive delineation (v2.3-revised).** Stage 1's primary form is tables (T0-T6) carrying deterministic data. Free-text annotations are permitted **inside** table cells (e.g., a `Notes` cell carrying degree-tightness flags, dignity bonuses, reception-aversion combinations). Free-text paragraphs between tables are limited to procedural notes (table headers, sect declaration, lookup citations). **Required appendices A-E (v2.3 addition) ARE permitted free-text + structured-list content** — angular-dynamics notes (A), Lots formula/source/status tables and notes (B), parans reference-only narrative (C), canon-source provenance tables and flags (D), timing-overlay deferred-data registry (E). These appendices are NOT interpretive delineation; they are **structured provenance / source-discipline content** that supports Gate-3 trace-back and prevents Stage 1 → Stage 2 cascade gaps. **What remains forbidden in Stage 1**: interpretive delineation (no "this means", "this suggests", "the chart shows", "the native is") + Stage 2 narrative + Stage 3 synthesis. Appendix content describes provenance + source-status + structural divergence flags + reference-only boundaries — it does NOT describe the chart's meaning.
- **No memory-based lookups.** All dignity / bound / decan / triplicity assignments (Gate 1) and all aspect family assignments (Gate 2) must trace to a specific table consulted at the time of fill. The audit history on `samples/topic-reading-template.md` documents 17 deterministic Stage-1 errors that propagated past a "fields-present" pass because values were memory-based; Gates 1, 2, and the Gate 4 values-lookup-verified checkpoint exist specifically to block this class of error.
- **No silent recomputation downstream.** Stage 2 / Stage 3 sessions must treat Stage 1 output as the **single source of truth**. If a downstream session sees a Stage 1 gap or inconsistency, the only legitimate response is to file an open thread and request Stage 1 fix — **never** to recompute silently and proceed.
- **Row identifiers are mandatory.** Every row across all seven tables (T0-T6) carries a `row_id` per the schema. Downstream Stage 3 synthesis trace-back enforcement (defined in v2.2 Plan B.5) depends on the `row_id` being present and conforming. A row without a `row_id` fails Gate 4.
- **Direction discipline for T2.** `From` = guest (planet in another's dignity); `To` = host (dignity ruler). Per `rules/aspect-reception-rules.md` anti-pattern 3: the host receives the guest, not the other way around.
- **Per-tier separation for triplicity reception.** Triplicity reception has three independent tiers (primary / secondary / cooperating); each is its own T2 row, never collapsed. A mutual reception in one tier does not imply mutual reception in another tier.
- **Artifact-hygiene final-pass before frozen declaration (v2.3 addition).** A Stage 1 file may only be declared frozen + ready for Gate 4 self-audit when: (a) every T-table is a single consolidated table — no secondary tables left over from authoring (e.g., no "additional rows — completing the matrix" tables); (b) no scratch text — no "Let me recount...", no "wait recompute", no inline self-correction notes that would otherwise be working-draft material; (c) every appendix is fully populated — no `[TBD]` / `[fill in]` / empty placeholders. Authoring sessions may produce scratch during drafting; the final-pass clean-up before Gate 4 declares freeze is the discipline boundary. Case-08 retro item #8 surfaced this rule.
- **T4 canonical / reference discipline (v2.3 addition).** Only Fortune + Spirit qualify as `direct-source canonical` Lots per `rules/lots-and-fortune.md` v1 lock. All other Lots in T4 are `reference-only` — they may be computed for completeness but **must not** anchor `confidence:high` findings in Stage 2/3; their citation requires `[Source-only candidate]` or `[NOT in v1]` flag + `confidence:speculative` (or `low`) MAX. The Project status column in T4 enforces the distinction at row level; the canonical/reference split into two sub-tables (T4-canonical and T4-reference) is mandatory whenever any reference Lot is present.
- **T6 coherence discipline (v2.3 addition).** T6 multi-role tier count enumerates only Lots present in T4 (canonical or reference). Orphan citations of non-T4 Lots inflate the fold-tier count spuriously and must be either added to T4-reference or noted as `(out-of-T4 reference, not counted in tier)`.
- **Parans / fixed stars reference-only boundary (v2.3 addition).** Bright-star parans and degree-catalog astronomical data (when present in chart source) are **specialist material**, not default Stage 1 evidence. They live in Appendix C as reference-only enumeration; Stage 2/3 do NOT cite them as evidence by default. Specialist scope invocation requires explicit citation of Appendix C + `confidence:speculative` tagging per `rules/cross-source-method-comparison.md` specialist tier discipline.
- **Canon-source provenance discipline for fictional + canon-marked subjects (v2.3 addition).** When the subject is fictional + canon-marked per `rules/fictional-subject-ethical-guard.md`, Appendix D is mandatory and must distinguish canon facts / NOT canon / PROJECT-ASSIGNED data points. Any divergence between canonical-faithful birth data and project-assigned creative-premise data (e.g., canonical April-28 = Taurus-Sun vs project-chosen November-24 = Sagittarius-Sun chart) must be explicitly flagged in the provenance table. Stage 2/3 findings purporting "about canonical [subject]" must carry `confidence:speculative` + canon-resonance discipline. The chart is a chart-as-character-symbol exercise, not a canonical-faithful Hellenistic nativity reconstruction.
- **MC / IC ≠ 10th / 4th WSH dual-channel warning (v2.3 addition).** When MC degree falls outside 10th WSH (and/or IC outside 4th WSH) — typical when Asc is past early-degree of its sign — Stage 2 career / public-action topics must consult both 10th-WSH-place (Hellenistic topic anchor) AND MC-degree-in-actual-place (visibility-point witness); 4th / IC topics similarly. The two are not interchangeable. T0 Divergence flag canonizes this warning; downstream sessions read the divergence flag and dispatch dual-channel.
- **English output.** Stage 1 / Stage 2 / Stage 3 internal analysis output is written in **English** per the v2.2 architecture language convention (see `rules/aspect-reception-rules.md` §"Reception Detection Procedure (v2.2 additive)" header note). Stage 1 is technical data with no narrative, so no Translation Layer (TL) pass applies; the reader-facing Chinese deliverable is rendered from Stage 3 synthesis output, not from Stage 1 tables.

## Reference 范文

**v2.3 canonical reference (current)**: `charts/case-NN/chart-stage1.md` — first v2.3-compliant Stage 1 file (fictional + canon-marked subject; 7 tables T0-T6; full appendices A-E; T4 canonical/reference split; T6 coherence rule honored; artifact-hygiene final-pass clean). Mapping:

| This spec | Range in example-case chart-stage1.md |
|---|---|
| T0 — Angles | §"T0 — Angles" (main body, before T1) |
| T1 — Per-planet audit | §"T1 — Per-planet audit table" (7 sub-tables, one per planet) |
| T2 — Reception network | §"T2 — Reception network" (mutual table + per-host sub-tables) |
| T3 — Aspect / configuration matrix | §"T3 — Aspect / configuration matrix" (single consolidated 21-row alphabetical table) |
| T4 — Lots + rulers | §"T4 — Lots + rulers" → §"T4-canonical" + §"T4-reference" sub-tables with Project status column |
| T5 — Cluster check | §"T5 — Cluster check" |
| T6 — Multi-Role registry | §"T6 — Same-Planet Multi-Role registry" (with T6 coherence rule honored: orphan non-T4 Lots noted as out-of-T4-reference) |
| Appendix A — Angles source block | §"Appendix A — Angles source block (narrative-level dynamics expansion)" |
| Appendix B — Lots formula / source / status | §"Appendix B — Lots formula / source / project status" |
| Appendix C — Parans / fixed stars | §"Appendix C — Parans / fixed stars (reference-only, NOT default Stage 1 evidence)" |
| Appendix D — Canon-source provenance | §"Appendix D — Canon-source provenance" (required for fictional + canon-marked subject) |
| Appendix E — Timing overlay (deferred per question trigger) | §"Appendix E — Timing overlay data (deferred per question trigger)" |
| Gate 4 self-audit | §"Audit checkpoint — Gate 4 (self-audit by Stage 1 author session)" (v2.3 14-item checklist) |
| Independent audit report | `charts/case-NN/chart-stage1-audit.md` (sibling artifact; round-2 PASS verdict) |

**Pre-v2.3 legacy partial reference**: `samples/topic-reading-template.md` §II — predates v2.3; covers T1-T6 only (no T0, no Appendices A-E, no T4 split, no Project status column, no T6 coherence rule, no artifact-hygiene final-pass). Mapping (legacy partial):

| This spec | Range in pre-v2.3 范文 |
|---|---|
| T1 — Per-planet audit | §2.1 |
| T2 — Reception network | §2.2 |
| T3 — Aspect / configuration matrix | §2.3 |
| T4 — Lots + rulers | §2.4 (no canonical/reference split; no Project status column — pre-v2.3 shape) |
| T5 — Cluster check | §2.5 |
| T6 — Multi-Role registry | §2.6 (no T6 coherence rule — pre-v2.3 shape) |

**`samples/topic-reading-template.md` is NOT v2.3-canonical**; treat as legacy partial reference suitable for understanding the pre-v2.3 T1-T6 structure and the historical 17-error audit story (below), but follow `charts/case-NN/chart-stage1.md` for v2.3 structure (T0 + appendices + T4 split). Per v2.3 retro task #37, a v2.3-canonical `samples/chart-finding-index-template.md` will be generated after example-case Stage 2/3 complete to fully replace the pre-v2.3 template.

The "Stage 1 → Stage 2 checkpoint" section at the foot of §II in the pre-v2.3 template is the historical form of the step 10 checkpoint output (pre-v2.3 9-item version); the v2.3 14-item Gate 4 checklist supersedes it. See `charts/case-NN/chart-stage1.md` §"Audit checkpoint — Gate 4" for v2.3 canonical Gate 4 output.

> **Audit note from the legacy template**: the audit-pass header on `samples/topic-reading-template.md` records 17 Stage-1 errors detected post-creation (7 bound assignments wrong, 3 decan assignments wrong, 6 triplicity notations wrong) plus 1 cascading Stage-3 error (a non-existent Sun-Moon trine cited as a strength). All errors propagated past the original §VI checklist because that checklist tracked "fields present" only, not "values lookup-verified against `rules/dignities-reference.md`". The Gate 4 values-lookup-verified pass in this procedure is the explicit guardrail to prevent that class of error from recurring. example-case Stage 1 (the v2.3 canonical reference above) returned zero T1 lookup errors in independent audit — a notable improvement attributable to the Gate 1 / Gate 4 discipline.

New Stage 1 sessions should follow the v2.3 canonical reference (example-case) for structure; deviation from the table column ordering or row count (e.g., adding a column without first updating this spec) is **not** permitted — table schema changes route through a v2.x plan, not ad-hoc per-reading modification. (The v2.3 inline spec update itself — which added T0, T4 split, appendices A-E — was the v2.3 example-case retro plan inline application per practitioner decision B 2026-05-17, not ad-hoc; see header watermark.)

## Source

- **Architecture frame** (three-stage Stage 1 / 2 / 3 separation; deterministic data layer with auditable checkpoint between stages; row_id schema and trace-back enforcement design): `[project heuristic]` — derived from `cases/case-06.md` cascade analysis and the v2.2 Plan A scoping document (`v2.2-stage1-data-extraction-architecture-plan.md`).
- **Per-planet dignity / triplicity / bound / decan procedures** (T1, Gate 1): underlying rules sourced from `rules/dignities-reference.md` (`[Brennan Ch.8]`, pp. 228-283).
- **Reception detection procedure** (T2 population logic): `rules/aspect-reception-rules.md` §"Reception Detection Procedure (v2.2 additive)" — `[Brennan Ch.14]` + `[Valens *Anth.* II]` + `[Firmicus *Math.* II.27-29]` + `[Dorotheus *Carmen* I via 'Umar al-Tabari → Dykes 2017]` + `[project heuristic]` for the step-by-step structural algorithm. This spec does not duplicate the reception logic; T2 step 5 is a thin wrapper.
- **Aspect / configuration sign-based geometry** (T3, Gate 2 double-verify): `rules/aspect-reception-rules.md` baseline (sign-based testimony / aversion conventions) + `[project heuristic]` for the explicit Method (a) + Method (b) double-verify procedure (derived from `samples/topic-reading-template.md` audit feedback catching 4+ aspect misassignments).
- **Lots formulas** (T4 step 3 / 7): `rules/lots-and-fortune.md` — sourced per that file's headers.
- **Cluster threshold** (T5 ≥3 planets, Lots / Nodes excluded): per Force Notes discipline + v2.x §A.1 N4 candidate (`[project heuristic]`).
- **Multi-Role registry** (T6): `[project heuristic]` — derived from Same-Planet Multi-Role Handling discussion in prior reading work; canonical form per `samples/topic-reading-template.md` §2.6.
- **Row identifier (row_id) schema and self-audit checkpoint enforcement** (Gate 3 setup, Gate 4 enforcement): `[project heuristic]` — introduced in v2.2 Plan A.2 to support Stage 3 mechanical trace-back enforcement defined in v2.2 Plan B.5.
- **T0 Angles table + MC/IC ≠ 10th/4th WSH dual-channel rule** (v2.3 addition): `[project heuristic]` — derived from `rules/data_contract.md` (Asc + MC required, IC/Desc important) + example-case retro practitioner review (2026-05-17 round 2) surfacing that ad-hoc `A-*` handles in Appendix A were not Gate 3-traceable; canonized as T0 to bring angles under row_id contract.
- **T4 canonical / reference split + Project status column** (v2.3 addition): per `rules/lots-and-fortune.md` v1 lock (Fortune + Spirit canonical; other Lots reference-only / deferred) + `rules/chart-finding-index-tags.md` v2.1 (extension-topic Lots formula-deferred per F6 cleanup) + example-case retro practitioner review item P2 surfacing competing status between T4 main table and Appendix B.
- **T6 coherence rule** (v2.3 addition): `[project heuristic]` — example-case retro practitioner review item P2 surfacing that T6-Mercury counted a non-T4 Sons Lot, inflating tier count.
- **Required appendices A-E** (v2.3 addition): canonized per example-case retro practitioner review round 1 (raw-source ref + Angles block + Lots formula/source/status + parans reference-only + canon provenance + timing overlay) — driven by example-case first-end-to-end-test surfacing 6 procedural gaps not previously documented in Stage 1 spec.
- **Artifact-hygiene final-pass discipline** (v2.3 addition): `[project heuristic]` — example-case retro practitioner review item P2 #2 surfacing T3 scratch text + secondary tables remaining in supposedly-frozen artifact, causing state inconsistency with appendices.
- **Parans / fixed stars reference-only boundary** (v2.3 addition): canonized per `rules/v2-roadmap.md` permanent-specialist deferred tier + `pending-verifications.md` "Permanent Specialist / Deferred" section + example-case retro practitioner review item #4.
- **Canon-source provenance discipline** (v2.3 addition): per `rules/fictional-subject-ethical-guard.md` extracted from v2.x fictional-subject plan §1.2-1.3 + example-case retro practitioner review item #5 surfacing fictional+canon-marked subject provenance gaps (chart Sun-sign vs canonical Sun-sign divergence).
