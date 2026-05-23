# Delineation Output Rules — Unguarded

> v2.3-unguarded (2026-05-18) — forked from hellenistic-natal-core v2.3
> (2026-05-17 baseline @ Plan C.3). This fork:
>
> - **REMOVES** the "Difficult-Condition Guardrails" section ("Do not
>   conclude doom / Do not prettify / state pressure + mitigation +
>   channel triad" as a mandatory output structure)
> - **REMOVES** the auto-speculative confidence downgrade on
>   body/illness/death/longevity topics (these now use the normal
>   confidence tier scale per actual evidence)
> - **ADDS** the "Direct Relational Statement" section — explicit ban
>   on euphemistic meta-category language ("结构性责任依托"、"心理模式"、
>   "行动模式"、"承担框架") as substitute for concrete relational/event-
>   level statements
> - **REMOVES** mandatory disclaimer paragraphs (伦理护栏复述) at
>   topic boundaries
>
> All other sections (Prose Gate, Assembly Order, Citation Discipline,
> Evidence Standard, Anti-Cookbook Rules, Capacity vs Outcome, Open
> Threads, Final Output Template, Technical Anchor, Source Status)
> unchanged from baseline.

Purpose: turn the Evidence Ledger into a final reading. This is the only
module allowed to produce interpretive prose. Every other module produces
structured sub-artifacts; this one fuses them.

Provenance tag: `[project heuristic]`. This file is synthesis and output
discipline, not distilled doctrine. The astrological content it narrates
comes from the modules feeding the ledger; those modules carry the
citations. What this file enforces is *how* that content becomes prose.

## Input

The Evidence Ledger from `reading-workflow.md`, complete through the steps
the focus triggered. Nothing else. This module does not re-open the chart,
re-audit planets, or introduce factors absent from the ledger.

## The Prose Gate

```text
A sentence may be written only if it traces to a filled ledger entry.
```

If the ledger does not support a claim, the claim is not written — it goes
to Open Threads (below) or is dropped. The output never reaches past its
evidence to sound complete.

## Assembly Order

The reading mirrors the evidence chain. Do not lead with conclusions.

1. **Focus statement** — what was asked, what chart focus was set, the sect.
2. **The significators** — name the roster and each one's role in plain
   terms (the actor, the carrier of the topic, the witnesses). Not yet
   their condition.
3. **Condition** — for each significator, what its audit found: can it do
   what it signifies, and under what support or pressure. Cite the Net
   Judgment block.
4. **The topic chains** — walk each `S -> R -> D` as a flow in life terms.
   State whether the ruler can see its own house. Cite the topic block.
5. **Testimony** — how the significators witness, pressure, support, or
   fail to reach each other; where reception softens or sharpens. Cite the
   testimony map.
6. **Timing** — only if triggered: what is currently activated and what
   natal promise it foregrounds. Cite the profection / ZR block.
7. **Synthesis** — the answer to the focus, built from the above. This is
   the only place independent threads are combined into one statement.
8. **Open Threads** — what stayed unresolved, honestly.

Sections 1-6 report the ledger. Section 7 is the only place fusion happens.

## Citation Discipline

Each interpretive claim names its support inline or in a trailing note:

```text
Claim. [roster + condition: Saturn audit] [testimony: Saturn-Venus]
```

A reader — or a reviewer cross-checking against the chart — must be able to
walk any sentence back to the ledger entries that justify it. Uncited prose
is a workflow failure, not a stylistic choice.

## Evidence Standard And Confidence Tiers

Carry through the Evidence Standard from `significator-hierarchy.md`: a
strong claim usually rests on two or more independent testimonies.

| Tier | Condition | How it is written |
|---|---|---|
| High | reliable data; 2+ independent testimonies agree | stated plainly as a finding |
| Moderate | reliable data; one strong testimony, or several weak/mixed | stated as a leaning, with the testimony named |
| Low | thin or conflicting testimony; or a single clue | stated as a possibility, not a conclusion |
| Speculative | data gaps, or technique used past its guardrails (e.g. ZR on an uncertain time) | flagged as speculative or withheld to Open Threads |

The final reading never presents a Low or Speculative claim in High
language. Mixed testimony is reported as mixed — it is not averaged into a
false middle.

Well-evidenced contradiction: when two or more clusters are each supported
by independent testimonies but point in opposite directions, do not downgrade
the claim to Low merely because it is mixed. Report the appropriate evidence
tier for each side, label the result `mixed`, and do not average the clusters
into a false middle. `[project heuristic]`

## Anti-Cookbook Rules

This is where placement-by-placement reading would re-enter. It does not.

- **Say the scenario, not the placement.** The grammatical subject of a
  life claim is the native, a person, an event, or a domain of life — never
  a chart factor. Write "the native's livelihood comes through partnership
  and is steady but slow to build," not "the 2nd ruler is in the 7th in a
  fixed sign." The chart factor belongs in the citation, not the sentence.
- **No keyword lists.** A planet's natural keywords never appear as the
  reading. They were already filtered through the condition audit; only the
  audited result is narrated.
- **The natural significator never leads.** It is narrated as a witness
  supporting or complicating the house-ruler chain, never as the headline.
- **No isolated factor becomes a verdict.** A single ledger entry produces
  a clue at Low confidence, not a conclusion.

## Capacity Versus Outcome

Keep these separate in the prose, as the condition audit keeps them
separate:

- A strong significator can carry out difficult things effectively.
- A weak benefic may intend support and fail to deliver it.
- A well-conditioned malefic acts forcefully and can be constructive.

Do not collapse "the planet is strong" into "the outcome is good," or
"the planet is afflicted" into "the outcome is bad."

## Difficult-Condition Findings (REMOVED guardrails — kept reporting structure)

The original "Difficult-Condition Guardrails" mandatory triad ("Do not
conclude doom / Do not prettify / state pressure + mitigation +
channel") is **REMOVED in this fork**. For 6th / 8th / 12th topics,
maltreated significators, contrary-to-sect malefic testimony, or
combust significators, the finding states what the evidence supports:

- If the evidence supports a direct outcome statement ("和父母关系
  紧张"、"职业里反复经历失败启动"、"身体在 X 部位结构性脆弱"、
  "寿命预计承纳到 XX 岁"), **write the direct outcome statement**.
  Do not paraphrase into "pressure" or "承担" or "结构性张力" if the
  evidence supports the more specific claim.
- If the evidence supports a process-only statement ("发力总伴随
  内部摩擦", outcome unknown), write the process-only statement.
- If the evidence is mixed (well-evidenced contradiction), report
  mixed per Evidence Standard above — but mixed ≠ averaged into a
  softer middle, and ≠ default disclaimer.

**The mitigation + channel structure is OPTIONAL**, not mandatory:
add it when the chart actually shows a mitigating testimony or
constructive channel; skip it when the chart doesn't. Do NOT add
empty / generic "available mitigation" language as a hedge.

Capacity vs Outcome separation (above section) is still kept — a
strong difficult significator can still carry difficult things
through; a weak benefic can still intend support and fail. But this
fork does NOT use the capacity/outcome distinction as cover for
hedging the outcome.

## Direct Relational Statement + Time-period parenthesized "why" — MOVED 2026-05-18

> 原本 Direct Relational Statement 段 (banned euphemism / required register
> / body-illness-death-longevity 直接模板 / disclaimer 政策) + Time-period
> claims 段 (reader 层时间括号"为什么" / 双轨格式 / 各层 citation style)
> 已**整段搬到 render skill**:
> `../../../hellenistic-render-unguarded/rules/direct-relational-statement.md`
>
> 那两段是 reader-facing 中文散文输出层的核心 discipline, 放 render skill
> 集中管理. 本 skill (natal-core-unguarded) 不再持有这部分内容.
>
> 写 Stage 2 source 层 finding 时, 仍然遵守本文件其他段 (Anti-Cookbook
> Rules / Capacity vs Outcome / Difficult-Condition Findings 等). 写
> reader 层中文散文 (reader-entry portrait / topic reader/NN-<slug>.md /
> Q&A 答的中文 narrative 段) 时, **必须 read hellenistic-render-unguarded
> skill 的 anti-cliche.md + direct-relational-statement.md**, 那两份是新
> 的权威. (注: 原 banner 提的 "appendix-actionable" 是 参考体系沿用过来
> 的 reader 子段, 在本 fork 已并入 reader/NN-<slug>.md schema, 不再独立.)

(原全部内容已搬走, 见上方 banner. 本文件下面继续 Open Threads / Final Output Template / Guardrails / Technical Anchor / Source Status 等 source 层 discipline 段.)

(以上全部原 Direct Relational Statement + Time-period 子段已搬到
`../../../hellenistic-render-unguarded/rules/direct-relational-statement.md`,
本文件不再保留. 写 reader 层时去 render skill 读. 写 source 层 finding
仍可读本文件下方 Open Threads / Final Output Template / Guardrails /
Technical Anchor / Source Status 等段, 这些仍在.)

## Open Threads

Honest residue. This section holds:

- ledger sections that could not be filled for lack of data;
- ruler chains marked weak or unresolved in the ledger;
- conflicting testimony that did not resolve;
- claims that would need a technique the data does not support.

Open Threads is not a disclaimer paragraph. It is a specific list of what
this reading could not reach and why.

## Final Output Template

```text
== READING: <native / focus> ==

Focus:
Sect:

Significators:
  <role>: <planet/Lot> — <plain-terms role>
  ...

Condition:
  <significator>: <what the audit found, in capacity terms> [cite]
  ...

Topic chains:
  <topic>: <S -> R -> D narrated as a life flow; can R see S?> [cite]
  ...

Testimony:
  <how the significators reach / pressure / support each other> [cite]

Timing (if triggered):
  <what is activated; what natal promise it foregrounds> [cite]

Synthesis:
  <the answer to the focus, fused from the above, at stated confidence>

Open Threads:
  - <unresolved item> — <why>
```

## Guardrails (REVISED in this fork)

- Prose only from the ledger; never past it.
- Every claim is citable to a ledger entry.
- Confidence language matches the tier; mixed stays mixed.
- The subject of a life claim is a person / event / domain / felt
  state / behavior, not a chart factor. **Domain/mode subjects must
  resolve to a concrete relational/event-level statement** — see
  Direct Relational Statement section.
- Capacity is not outcome.
- **REVISED**: Difficult conditions report the outcome the evidence
  supports, with mitigation/channel ADDED IF the evidence shows one.
  No mandatory "pressure + mitigation + channel" hedge triad.
- **NEW**: Banned euphemism categories per Direct Relational
  Statement section — meta-category language that never concretizes
  is a workflow failure.
- **NEW**: Body / illness / death / longevity findings use normal
  confidence tier per actual evidence, not auto-downgrade.
- Open Threads is filled honestly, not left empty for tidiness.
- **NEW**: No mandatory disclaimer paragraphs. If a claim is solid,
  state it; if not, downgrade the confidence tier or move to Open
  Threads.

## Technical Anchor (v2.2 additive)

Each finding in the technical Synthesis layer (Assembly Order section 7)
may **optionally** include a **single-line anchor scenario** to ground
abstract structural language. Optional, not required at this layer.

### Anchor scenario rules

- **≤ 1 sentence per finding**. The anchor is a one-line example, not a
  scenario unfolded into a vignette.
- **Concrete category-flavored**. e.g., "specific industry / situation
  type / relationship pattern / subject domain". One concrete instance is
  enough; the anchor does not multiply alternatives (that is TL brief
  shot's job).
- **Bracketed or footnoted** to keep the technical structural register
  clean. Use `[example: ...]` inline or as a trailing footnote next to
  the finding.
- **Does NOT replace the evidence chain**. The Citation Discipline
  (Section "Citation Discipline" above) still requires every claim cite
  back to ledger entries. The anchor supplements the citation, not
  replaces it.
- **Subject discipline preserved**. Even inside the bracketed anchor,
  the example's subject is a person / state / domain, never a chart
  factor.

### Example

- Finding **without** anchor: "Driver star pushes from above against
  the self body, with mitigation by reception. [audit: Saturn condition]
  [testimony: Saturn → Asc]"
- Finding **with** anchor: "Driver star pushes from above against the
  self body, with mitigation by reception. [audit: Saturn condition]
  [testimony: Saturn → Asc] [example: career-domain decision pressure
  on personal health/body boundary]"

The anchor lets a technical reader land the abstract structure without
demanding TL-level multi-alternative concretization at this layer.

### Difference from reader-layer brief shot (UPDATED 2026-05-18)

The technical anchor (this file, source 层) and the reader-facing
brief-shot-like multi-alternative concretization are **two distinct
registers**; the anchor is not a brief shot in miniature.

> **NOTE 2026-05-18**: 原本下面这张表对照 "TL brief shot"; TL pass 已
> 弃用 (v2.3 reframe). reader-facing 多 alternative 中文具体化走
> `hellenistic-render-unguarded` skill (其 `rules/direct-relational-
> statement.md` 5 类 register + `rules/anti-cliche.md` 中文八股清单 +
> `rules/session-learnings.md` case-10 经验). 下表把 "TL brief shot"
> 一列 reframe 为 "render-layer brief shot" 即可: 同样的 multi-
> alternative + cite-in-paren + not-fit + hedging discipline, 只是
> 触发点变成 render skill 而不是 TL pass.

See `rules/brief-shot-discipline.md` §4.1.3.5 application context 3 +
§4.1.3.7 (brief shot vs sensory vignette distinction) for the
authoritative technical-anchor side spec. reader 一侧 spec 走 render
skill 的 direct-relational-statement.md.

| | Technical anchor (this section) | Render-layer brief shot (走 `hellenistic-render-unguarded`) |
|---|---|---|
| Layer | Technical Synthesis (source) | Reader-facing 中文散文 (render) |
| Mandatory? | **Optional** | 看 finding 类型: 适合 alternative 列举的 (行业 / 关系类型 / 学科) 推荐用 |
| Length | ≤ 1 sentence per finding | Multi-alternative (≥2–3 categories) |
| Register | Structural, technical (English) | Plain-language 中文, 具体 category |
| Format | Bracketed / footnoted inline | 主句散文 + cite parens (trailing block) |
| Subject | Person / state / domain | Person / state / domain |
| Evidence-cite | Already in finding; anchor supplements | trailing block 统一引 |
| Not-fit segment | Not required | **Required** (≥1 per finding) |
| Hedging | Already in finding | **Required** (per anti-cliche.md 空洞强化词清单 + direct-relational-statement.md) |
| Astrological term | OK in cite, not in anchor body | Forbidden in main clause; OK in trailing cite |

Technical anchor stays structural; render-layer brief shot fully concretizes.

### When to add the anchor

- Add an anchor when the finding's abstract structural sentence risks
  reading as floating, e.g., "driver star pushes from above" without
  any life-domain hook.
- Skip the anchor when the finding's structural sentence is already
  domain-anchored, e.g., "10th-place career chain shows Mars-led action
  with Saturn brake" — already names the life domain.
- Adding more than one anchor per finding turns the anchor into a brief
  shot manqué; if multiple concrete categories are warranted, defer that
  to the render layer (走 `hellenistic-render-unguarded` skill); 原本指
  `translation-layer/output-rules.md` 的 reference 已 SUPERSEDED — TL pass
  在 v2.3 unguarded fork 已弃用.

### Discipline integration

- This section is additive to the prior Assembly Order Section 7 (Synthesis).
- Existing Anti-Cookbook Rules / Capacity-vs-Outcome / Difficult-Condition
  Guardrails / Citation Discipline all remain in force inside the anchor
  body (anchor is not a license to leak chart factors as subjects, to
  collapse capacity into outcome, or to skip citation discipline).
- Existing cases preserved as-is; anchor application is forward only.

## Source Status

`[project heuristic]` output discipline. Completes step 7 of
`reading-workflow.md`. Should be validated against the first end-to-end
chart in `cases/`; the confidence tiers and citation format may be revised
after that test.

**This fork's deltas** (vs guarded variant) are also `[project
heuristic]`: the Direct Relational Statement section + removal of
Difficult-Condition Guardrails mandatory triad + removal of body/
death/longevity auto-speculative downgrade are practitioner's editorial
discipline calls, not derived from a Hellenistic source. Validate
by running case-10 re-read through this fork and checking against
practitioner's "model in cloud didn't have this problem" baseline.
