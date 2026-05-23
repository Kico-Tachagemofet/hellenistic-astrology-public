# Chart-Finding-Index Workflow — v2.3 Stage 2/3 Authoritative Spec

> ## ⚠️ UNGUARDED FORK OVERRIDE (2026-05-18)
>
> All references in this file to **ethical-guard** / **ethical-guard
> inheritance** / **default-OFF extension topics** / **on user request
> only gating** / **confidence:speculative auto-flag for canon-resonance
> findings** are **NO-OP** in this fork. All 15 topics dispatch as
> ordinary Stage 2 modules per `SKILL.md` Step 4 default 15. See
> `fictional-subject-ethical-guard.md` (stub) and
> `delineation-output-rules.md` Direct Relational Statement section
> for the positive replacement framework.

---

> **v2.3 stub** (2026-05-16) — initial workflow spec for v2.3 chart-finding-
> index architecture. Replaces `handoff-templates/v2.2-stage-handoffs.md`
> (archived) and the `Stage 2 Session Output Format` / `Stage 3 Synthesis
> Spec` / `Orchestration Protocol` sections of `rules/topic-modules.md`
> (marked SUPERSEDED via deprecation banner). Full spec to be finalized in
> Phase 3 of v2.3 architectural plan; this stub establishes the workflow
> shape + slug mapping + cross-references so cleanup can complete safely.
>
> For full architectural context see `v2.3-chart-finding-index-architectural-
> plan.md`. For tag inventory see `rules/chart-finding-index-tags.md` v2.1 (canonical).

## Purpose

Stage 2/3 workflow for v2.3 chart-finding-index source-driven architecture.
Replaces v2.2 narrative-form Stage 2 (800-行 topic modules) + Stage 3 (1049-
行 portrait synthesis essay) with **finding-production** stages whose direct
output is the chart-finding-index source layer.

The downstream consumer is **the decision-maker (practitioner / AI assistant)
querying the finding-index by tag combinations to compose reader-facing
answers** — NOT a reader reading the file directly. No reader-facing
rendering layer exists in v2.3.

## Architecture context

Per `v2.3-chart-finding-index-architectural-plan.md` §2:

```
chart raw data
    ↓
Stage 1 (audit data, 7 tables T0-T6 + 5 appendices A-E, deterministic)
    ↓                                              ← per rules/stage1-data-extraction.md (v2.3)
Stage 2 (per-topic finding production)         ← per §1 of this file
    ↓
Stage 3A (chart-finding-index registry consolidation)  ← per §2 of this file
    ↓
Stage 3B (composition pass — 整盘 mouthfeel)            ← per rules/composition-pass.md
    ↓
chart-finding-index.md + composition.md 完成 → 决策者基于 registry + composition 工作
```

File structure per chart:

```
charts/case-NN/
    chart-finding-index.md          # 主文件 (Stage 3A output)
    composition.md                  # 整盘 mouthfeel 层 (Stage 3B output; per rules/composition-pass.md)
    topic-findings/
        character.md
        career.md
        partnership-marriage.md
        family.md
        learning.md
        wealth.md
        divination-spirituality.md
        body.md (extension; ethical-guard)
        chart-signature.md
        # extension as needed: children / siblings / friends-benefactors /
        #                      illness / death / longevity
        # 注: Stage 3B 在每个 topic-findings file 末追加 "Topic Composition" 段
        #     (per rules/composition-pass.md §3)
    question-index.md               # utility (reader-question → finding refs)
```

## §1 Stage 2 — Per-topic finding production

### Input

1. `chart-NN-stage1.md` (Stage 1 frozen 6 tables, per `rules/stage1-data-
   extraction.md`)
2. `chart-NN-stage1-audit.md` (PASS verdict from independent audit session)
3. Per-topic 太极点 + Lens reframing tables from `rules/topic-modules.md`
   §"Per-Topic Module Specifications" (still-valid sections marked in that
   file's deprecation banner; v2.2 slugs map 1:1 to v2.3 slugs per below)
4. Tag inventory from `rules/chart-finding-index-tags.md` v2.1 (canonical)

### Slug mapping (v2.2 → v2.3)

`rules/topic-modules.md` uses v2.2 slugs in its per-topic spec sections.
Map to v2.3 chart-finding-index slugs:

| v2.2 (topic-modules.md) | v2.3 (chart-finding-index-tags.md + file naming) |
|---|---|
| character | character |
| career | career |
| love-marriage | partnership-marriage |
| family | family |
| learning | learning |
| wealth | wealth |
| occult | divination-spirituality |
| body | body |
| force-signature | chart-signature |
| (timing-overlay extension) | (NOT a topic-findings/ file; timing-conditional findings carry timing-activation:* tags on findings in other topic files) |

### Output (per module = per Stage 2 session)

One file: `charts/case-NN/topic-findings/<v2.3-slug>.md`

Each file contains:
- **Frame** — subject reference + Stage 1 ref + topic spec ref (with v2.2→v2.3 slug
  note) + ethical-guard inheritance
- **太极点 (relevant factors, applied to this chart)** — per `rules/topic-
  modules.md` per-topic spec (still valid section); cite Stage 1 row_ids
- **Topic-level findings** — list of findings using **topic-finding 轻 schema**
  (see §3 below)
- **Open threads** — unresolved reader-context items deferred to specialist
  supplements / question-index utility

### What NOT to produce (vs v2.2)

- ❌ "Composite reading framework" 800-行 narrative段落
- ❌ "Lens reframing (applied)" 长 prose blocks
- ❌ "Brief shot" multi-example A/B/C/D/E enumeration as reader-facing
  product (brief shots now go into finding's `Concretization (brief shot
  类型库)` field — 2-4 specific scenarios, not 5+ option enumeration for
  reader)
- ❌ TL pass — no `*-TL.md` sibling needed (TL 弃用; 中文 reader 渲染走
  `hellenistic-render-unguarded` skill, 出 `charts/case-NN/reader/NN-<slug>.md`,
  用户显式触发; 不在本 Stage 2 自动产)
- ❌ Provenance per witness as reader-facing — Hellenistic basis goes
  inside each finding entry, not as a standalone "Provenance per witness"
  end section

### Module independence

Per `rules/topic-modules.md` §4.1.5 (still valid section): each module = its
own Stage 2 session; modules dispatch in parallel after Stage 1 audit pass;
modules do NOT write to each other's files.

## §2 Stage 3 — Chart-finding-index consolidation

### Input

All `charts/case-NN/topic-findings/*.md` files from Stage 2 (default 9 +
any requested extensions).

### Output

1. **`charts/case-NN/chart-finding-index.md`** — 主文件; per v2.3 plan §2
   structure:
   - **§A** Stage 1 raw data (T1-T6 tables embedded — not just referenced)
   - **§B** Chart-level findings (≈ 35-45 entries; each per **chart-level
     finding schema** in v2.3 plan §2 / see §3 below)
   - **§C** Cross-finding relationships (`amplifies` / `contrasts` /
     `supports` / `tension-with` graph between findings)
   - **§D** 整盘 patterns 薄索引层 — 仅 "high-level pattern → finding-ref
     list" 形态 (e.g. "外投空 axis → [F021, F037, F042]"). **整盘
     mouthfeel / 复合主味 / tension mechanism / handoff verdict 不在此**,
     移到 Stage 3B `composition.md` per `rules/composition-pass.md`
   
2. **`charts/case-NN/composition.md`** — Stage 3B output; per
   `rules/composition-pass.md` §2 7-段 schema (Ingredient Register /
   Dominant Flavor / Tension Mechanisms / Execution Handoffs / Composite
   Image / Do-not-flatten Notes / Audit Backtrace). 与 chart-finding-
   index.md 同时存在: 3A 为 tag-based lookup registry, 3B 为 mouthfeel +
   reader-question-shape rendering scaffolding.
   
3. **`charts/case-NN/question-index.md`** — utility; reader-question → finding
   refs mapping; incremental (only common questions enumerated; new
   questions added as decision-maker uses the index)

### Consolidation process

1. Read all 9 (or more) `topic-findings/*.md` files
2. Identify chart-level findings: findings appearing in ≥2 modules OR findings
   that are chart-level structural by nature (e.g., Lord-of-geniture / cluster
   patterns / distributed signature)
3. Promote each chart-level finding to a `chart-finding-index.md` §B entry per
   chart-level schema (statement + polarity + confidence + tag annotations +
   audit chain WITH raw data embedded + Hellenistic basis + appears-in-modules
   refs + related findings + concretization + not-fit + reader-facing 短描)
4. Link cross-finding relationships in §C
5. Name 整盘 patterns in §D **薄索引层** (high-level pattern → contributing
   finding ID list only, e.g. "外投空 axis → [F021, F037, F042]")
   
   > **v2.3 Stage 3B banner**: 整盘 mouthfeel / 复合主味 / tension mechanism
   > naming / handoff verdict / composite image 不在 §D, 移到 Stage 3B
   > `composition.md` per `rules/composition-pass.md`. §D 仅保留作为 "pattern
   > → finding refs" tag-style 索引层 (薄). Stage 3A 完后即触发 3B.

### What NOT to produce (vs v2.2 portrait)

- ❌ 1049-行 散文式 "Overall portrait synthesis" essay paragraphs
- ❌ canon-resonance-style reader-facing essay sections (canon
  resonance findings live as `confidence:speculative` finding entries with
  appropriate ethical-guard flags; not as essay)
- ❌ Portrait TL — no portrait-TL.md sibling needed (整盘中文 reader 输出
  走 `hellenistic-render-unguarded` 档 B (全盘合并), 不再产 portrait-TL.md)

## §3 Schema references

See `v2.3-chart-finding-index-architectural-plan.md` §2 for:
- Chart-level finding entry schema (full fields)
- Topic-finding 轻 schema (subset of chart-level fields)
- Question-index entry schema

See `rules/chart-finding-index-tags.md` v2.1 (canonical) for:
- 8 dimensions / 101 tags
- Source status legend (direct-source / source-components / project-composite
  / project-heuristic / project-query / project-output-discipline)
- Cross-tag relationships

## §4 Cross-link / 替代关系

This file **replaces**:
- `handoff-templates/v2.2-stage-handoffs.md` (archived to `archive/v2.2-
  handoffs/`)
- `rules/topic-modules.md` §"Stage 2 Session Output Format" (B.4)
- `rules/topic-modules.md` §"Stage 3 Synthesis Spec" (B.5)
- `rules/topic-modules.md` §"Orchestration Protocol" (B.7)
- `rules/topic-modules.md` §4.1.6 spec template's "Composite reading
  framework" / "Output structure" / "Concrete brief shot expectations" 部分

This file **inherits / depends on**:
- `rules/stage1-data-extraction.md` (Stage 1 spec v2.3 with T0-T6 + 5 appendices)
- `rules/topic-modules.md` §"Concept" + §4.1.3-4.1.5 + §"Per-Topic Module
  Specifications" 中每个 module 的 太极点 + Lens reframing table + Provenance
  per witness (these sections remain authoritative; v2.2 slug names map 1:1
  to v2.3 per §1 slug mapping table)
- `rules/chart-finding-index-tags.md` v2.1 (canonical) (tag inventory)
- `rules/delineation-output-rules.md` (confidence tiers + mixed handling +
  difficulty triad + anti-cookbook)
- `rules/aspect-reception-rules.md` (referenced by Stage 1; 4-cell matrix
  used in `modality:aversion-reception` tag definition)

This file **has Stage 3B sibling spec**:
- `rules/composition-pass.md` (Stage 3B authoritative; consumes 3A output;
  produces `composition.md` + topic-findings 末段 Topic Composition 4 sub-段)

## §5 Status

**Stub完整度**：workflow shape + slug mapping + cross-references established.
Sufficient for cleanup safety (`method-index.md` §1A.v2.3 + `skill-draft/
SKILL.md` can now point here without broken refs after v2.2 handoffs are
archived).

**Phase 3 finalization will add**:
- Concrete step-by-step Stage 2 module session procedure (per-step Gate
  checks; analog to v2.2 Plan B handoff template structure)
- Concrete Stage 3 consolidation procedure (per-step trace-back checks;
  analog to v2.2 Plan B.5 Gate 3 enforcement)
- Worked example reference (produced from example-case first end-to-end test;
  becomes new `samples/chart-finding-index-template.md` to replace v2.2
  `samples/topic-reading-template.md` which is preserved as v2.2-historical)
- Orchestration protocol (mode dispatch / sequential vs parallel boundaries
  / failure-mode dispatch tree; analog to v2.2 Plan B.7)
- Power-user shortcut auto-fill (B.7 open thread; future enhancement)

---

> Stub complete. Cleanup Steps 6-8 (deprecation banner + SKILL.md rewrite +
> method-index.md update) may now safely reference this file. Step 9
> (archive v2.2 handoffs) may proceed after Steps 6-8 complete.
