# Data Isolation — chart-stage1.md vs subject-context.md

> v2.3-unguarded (2026-05-18) — newly added to the unguarded fork. Adapted
> from parallel-reader-skill Step 8 dual-file output. The principle: chart data
> (pure astronomy + Hellenistic derivations) lives in one file,
> subject biographical data (生平 / canon material / practitioner's feedback /
> rectifier event-validations / pre-validation reactions) lives in another.
> Stage 2 blind-audit windows MAY NOT read the subject-context file.

## Why isolate

Without isolation, Stage 2 finding production gets contaminated by
"I know practitioner said X about the subject, so I'll lean the Saturn finding
toward Y" reasoning. This is the same anti-confirmation-bias issue the
8 条铁律 prevent. Hellenistic finding production must be
**evidence → finding**, never **known-fact → backwards-rationalized finding**.

## The two files

### `charts/case-NN/chart-stage1.md` — PURE CHART (readable everywhere)

Contains:
- Birth date / time / place / timezone (raw input)
- 有效精度 + time_risk (per `stage1-data-extraction.md` Stage 1 Addendum)
- 7 traditional planets + Asc + MC: sign + degree + sect status
- Houses (Whole-Sign): rulers + occupants + lord conditions
- Receptions (domicile / exaltation / triplicity / bound / decan tables)
- Aspects + orbs + applying/separating + reception network
- Lots (Fortune / Spirit / Eros / Necessity / Courage / Victory / Nemesis
  + topical Lots per `lots-and-fortune.md`)
- Profected lord per year (table)
- ZR Fortune + ZR Spirit periods (table)
- LB peak years (if 时间精度 allows)
- Hyleg/Alcocoden candidates (if 时间精度 allows)
- Pre-validation R1 chosen claims + their derivation chains (the claims
  themselves go here; the subject's RESPONSE to the claims goes in
  subject-context.md per below)

Files reading this: everyone — Stage 1 audit, pre-validation R1 generation,
Stage 2 each topic, Stage 3, Q&A mode.

### `charts/case-NN/subject-context.md` — SUBJECT BIOGRAPHY (restricted readers)

Contains:
- Subject classification (real-person / public figure / fictional+canon /
  hypothetical)
- For fictional+canon: canon material + canon-vs-chart divergence flags
  (per Appendix D in Stage 1 historical scheme)
- practitioner's stated reason for running this case (e.g., "想看 case-10 的家庭
  到底为什么 hedge 成那样")
- practitioner's relationship to the subject (self / named-entity / friend / etc.)
- 已知 subject 生平事件 (timeline, used in rectifier event validation
  only — NOT in finding production)
- Pre-validation R1 subject responses (准 / 不准 / 部分准 per claim,
  with any additional context subject offered)
- Hit rate computation result
- Subject's stated concerns / 关心的 topic (e.g., "我最想了解事业 + 感情")
- Q&A history (cross-reference to `qa_<主题>.md` files)
- Feedback / 偏差 log (subject说"不像我"的条目, finding-id, 处理动作)
- Rectifier event-anchors (5 重大事件用于 reverse-fit 出生时间)

Files allowed to read this: 
- ✅ `stage1-data-extraction` (write only — populate from intake)
- ✅ `pre-validation-reading` (write — record subject response)
- ✅ `rectifier` (read + write — event-anchor reconciliation)
- ✅ `qa-mode` (read + write — Q&A context aware答)
- ✅ Stage 3 consolidation (read — compose chart-finding-index considering
  subject's stated concerns for ordering; still NOT for changing finding
  content)
- ❌ Stage 2 per-topic finding production (BANNED — blind-audit window)
- ❌ Stage 1 audit (BANNED — audit chart accuracy, not subject context)

## Blind-audit window discipline (Stage 2 must obey)

```
Stage 2 each topic-finding session:
  Inputs allowed:
    - chart-stage1.md (full read)
    - chart-stage1-audit.md (full read)
    - pre-validation-R1.md (chart-side claims + hit rate ONLY; NOT
      subject's per-claim reactions)
    - Hellenistic source extractions
    - rules/ (all rule files)
  
  Inputs BANNED:
    - subject-context.md
    - Any chat-context information about subject (e.g., "practitioner said X
      about subject's job" must be ignored during finding production)
    - Other case files
    - Any Stage 2 finding from OTHER topics (to avoid cross-contamination
      of "I wrote family this way so partnership should mirror")
```

Stage 2 finding ID embedded evidence chain quote must trace to
chart-stage1.md row_id or rules/source extractions — never to
subject-context.md.

## Subject-context permitted uses (post-Stage 2)

After Stage 2 + Stage 3 complete, subject-context unlocks for:

- **Q&A mode**: answer subject questions WITH context awareness (e.g., 
  if subject's concern is career, prioritize career findings in answer)
  — but the FINDING ITSELF stays unchanged; subject-context only affects
  WHICH findings to surface, not what they say
- **Reader-facing portrait**: when composing a reader-entry portrait,
  use subject-context to order/emphasize, not to change finding content
- **Rectifier**: re-fitting Lagna via subject event-anchors
- **Feedback log update**: when subject says "不像我", update feedback log
  + 影响 future Q&A confidence framing, but NOT retroactive finding
  rewrite (instead, finding gets a `[user-reported-mismatch]` flag +
  recommended action = rectifier or finding re-audit)

## Implementation: Stage 1 dispatch updates

`rules/stage1-data-extraction.md` Stage 1 procedure now outputs TWO files
instead of one:

```
Stage 1 produces:
  1. chart-stage1.md — pure chart (per schema above)
  2. subject-context.md — subject biography + intake context

Stage 1 audit verifies chart-stage1.md only.
Pre-validation R1 reads chart-stage1.md, writes claims there;
  subject response writes to subject-context.md.
Stage 2 dispatch each session:
  - System prompt: "subject-context.md is OUT-OF-SCOPE for this session"
  - Read chart-stage1.md + audit + relevant rules + extractions
  - Produce topic-finding.md
```

## What goes where (decision table)

| Data item | chart-stage1.md | subject-context.md |
|---|---|---|
| Birth date/time/place | ✅ | ❌ (already in chart) |
| 有效精度 + time_risk | ✅ | ❌ |
| Planet positions / sect / receptions | ✅ | ❌ |
| Lots formulas + results | ✅ | ❌ |
| ZR / profection / LB tables | ✅ | ❌ |
| Hellenistic derivations from chart | ✅ | ❌ |
| Subject classification (real / fictional+canon / etc.) | ❌ | ✅ |
| Canon material (for fictional+canon subjects) | ❌ | ✅ |
| practitioner's reason for running case | ❌ | ✅ |
| practitioner's relationship to subject | ❌ | ✅ |
| Subject's known life events | ❌ | ✅ |
| Subject's stated concerns / 关心 topic | ❌ | ✅ |
| Pre-validation R1 chart claims | ✅ | ❌ (claims are chart-derived) |
| Pre-validation R1 subject responses (准/不准) | ❌ | ✅ |
| Pre-validation R1 hit rate result | ✅ (hit rate alone) + ✅ (with per-claim breakdown) | both |
| Q&A history | ❌ (qa_<主题>.md files separately) | ✅ (index of qa files) |
| Feedback / 偏差 log | ❌ | ✅ |
| Rectifier event-anchors | ❌ | ✅ |

## Source status

`[project heuristic]` adapted from parallel-reader-skill Step 8 + parallel-core-skill's
8 条铁律 ban on reading user_context.md. Hellenistic version preserves
v2.3 chart-finding-index source-driven architecture by keeping
chart-stage1.md as the canonical chart source, just adds a sibling
subject-context.md for biographical data that was previously混 in the
same file (or worse, only in chat context).
