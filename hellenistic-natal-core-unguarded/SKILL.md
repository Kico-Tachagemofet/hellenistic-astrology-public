---
name: hellenistic-natal-core-unguarded
description: Hellenistic natal astrology reading workflow — UNGUARDED variant. Same v2.3 chart-finding-index source-driven architecture as hellenistic-natal-core, but with ALL ethical guards, safeguard disclaimers, default-OFF extension-topic gating, "do not conclude doom" guardrails, auto-speculative confidence downgrades on body/death/longevity topics, and abstract category euphemisms STRIPPED. Family / children / siblings / body / illness / death / longevity / lifespan topics are treated as ordinary topics — direct relational/event-level statements ("和父母关系紧张"、"和家人有争吵"、"寿命预计承纳到 XX 岁") are permitted and preferred over abstract mode/structure language ("结构性责任依托"、"心理模式"、"行动模式" are discouraged). Use ONLY when practitioner explicitly requests the unguarded variant ("用 unguarded 跑"、"无护栏版"、"把护栏拆了重读"); default natal work still uses hellenistic-natal-core.
---

> v2.3-unguarded (2026-05-18) — forked from hellenistic-natal-core v2.3
> @ 2026-05-17 baseline. All ethical-guard / disclaimer / euphemism /
> auto-downgrade mechanisms removed per practitioner feedback on case-10 reader-
> entry-portrait (model was hedging family/parent/death/longevity claims
> behind abstract "mode" and "structural responsibility" language;
> "我之前用cloud没有这个问题"). This skill exists to produce the
> direct, blunt, relational/event-level chart finding output that the
> guarded variant won't write.
>
> Scope reminder: this is an **interpretive output discipline** fork.
> The doctrinal layer (Hellenistic source extractions, dignities,
> aspects, lots, timing techniques, ruler-chain audit) is **identical**
> to the guarded skill. What changes is the OUTPUT register and what
> the skill is willing to state.

# Hellenistic Natal Core — Unguarded (v2.3-unguarded)

This skill is the entry point for **unguarded** Hellenistic natal readings
under v2.3 chart-finding-index source-driven architecture. Doctrine lives
in `rules/`; this file orchestrates the first-invocation flow.

**Two workflow paths coexist** (identical to guarded variant):

- **v2.3 chart-finding-index** (default for any new chart work): Stage 1
  deterministic data → Stage 2 per-topic finding production → Stage 3
  chart-finding-index consolidation. **No reader-facing rendering** — the
  finding-index source itself is the deliverable. Per
  `rules/chart-finding-index-workflow.md`.

- **v1 single-session** (legacy; preserved for single-focus reading):
  `rules/reading-workflow.md` step 0-7. v1 was locked 2026-05-15.

## What this fork removes (vs hellenistic-natal-core)

| Removed | Lived in | Effect |
|---|---|---|
| Subject-class ethical guard (real-person vs fictional+canon-marked) | `rules/fictional-subject-ethical-guard.md` | All subjects treated identically; no body/illness/death/longevity default-OFF; no per-reason attenuation table |
| Extension-topic "on explicit request only" gating | SKILL.md Step 4 + chart-finding-index-tags | children / siblings / friends-benefactors / illness / death / longevity dispatch as ordinary topics in default 9 + extension 6 set |
| "Do not conclude doom / do not prettify" guardrail | `rules/delineation-output-rules.md` Difficult-Condition Guardrails | Difficult-condition findings state the direct outcome the structure supports, not a softened "pressure + mitigation + channel" triad |
| Auto-speculative downgrade on body/death/longevity findings | `rules/delineation-output-rules.md` Evidence Standard | Body/death/longevity findings use the normal confidence tier their evidence supports (High / Moderate / Low / Speculative on evidence merit, not topic membership) |
| Abstract category / euphemism output preference | implicit in narrative layer | Direct relational/event-level statements required; "结构性责任依托" / "心理模式" / "行动模式" / "承担框架" type meta-category language banned |
| 伦理护栏 disclaimer paragraphs in reader-entry output | implicit narrative habit | No disclaimers — if finding evidence supports a statement, write the statement |

## What this fork keeps unchanged

- All Hellenistic doctrine: dignities, sect, aspects, reception, ruler
  chains, condition audit, lots, profections, ZR, LB, planetary years
- Anti-cookbook discipline: subject of life-claim = native / person /
  event / domain (this rule is **kept** — the unguarded fork wants
  MORE concreteness, not less; "person/event/domain" is the right
  subject grammar; what's banned now is the **euphemistic meta-category**
  abuse of "domain" — see `rules/delineation-output-rules.md`
  Direct Relational Statement section)
- Source citation chain + ≥2-source triangulation discipline
- Stage 1 / Stage 1-audit / Stage 2 / Stage 3 workflow architecture
- Capacity vs outcome separation (a strong significator can carry
  difficult things; a weak benefic may intend support and fail to
  deliver — still kept, just no longer used as cover for hedging)

## ⚙️ Reader-facing 渲染 — 走单独 skill

写任何 reader-facing 中文散文 deliverable 时 (reader topic .md / 整盘 portrait / Q&A 长答 / composition essay), **必须用 Skill tool invoke `hellenistic-render-unguarded`**. ⚠️ 不能直接读 render skill 的 rules/ 目录开始写——那会绕过 render SKILL.md 的 Step 1.5 mandatory 生活判断摘要 + anti-cliche-astrology self-review. 那个 skill 集中持有:

- `rules/anti-cliche.md` — 通用中文反八股 (动词长骨肉 / 不是而是禁 / 排比禁 / 等)
- `rules/direct-relational-statement.md` — 希腊化 specific 渲染 discipline (5 类 register / 时间括号"为什么" / chart-tech 全 trailing 不 inline / body-death-longevity 直接模板)
- `rules/session-learnings.md` — case-10 v1→v4 演变经验 8 条
- `rules/topic-file-schema.md` — 一主题一文件 + HTML 合并 (仿参考体系)
- `scripts/report_builder.py` — HTML 打包
- `samples/case-10-family-{v4-OK, v0-原版-反例}.md` — 正反对照

**本 skill 自己只产 source 层**: Stage 2 finding (英文 + 表格 + technical citation), Stage 3 chart-finding-index, Open Threads. 这些**不走中文反八股规则** (语言是英文 / 形式是表格 + citation, 中文八股清单不适用).

Reader 中文散文层全部交给 render skill.

## ⚙️ 输出规则 (全局, 优先级最高)

**核心规则: 直接写 MD 文件, 聊天框只报进度.**

1. **直接写文件**: Stage 1 / Pre-validation R1 / Stage 2 each topic-finding /
   Stage 3 / Q&A 全部直接写文件 (reader 渲染走 render skill); 聊天框只报 1-2 句
   概括 + 文件路径
2. **不在聊天框写完整 finding** — 聊天框是 progress 通道, 不是答案通道
3. **每次 Write/Edit ≤ 250 行** — 超长分次:
   - 先 Write 前半 (≤ 250 行)
   - 然后 Edit append 后半
   - 或者拆成多个 sub-file (e.g., Stage 1 拆 chart-stage1.md + chart-stage1-
     planets.md + chart-stage1-lots.md if needed)
   - 写入失败立刻拆更小重试, 不反复重试同样大块
4. **进度报告硬规则**: 每个 Stage / Step / topic 完成后聊天框输出:
   ```
   === Stage X / <topic> 完成 ===
   写入: charts/case-NN/<filename>.md (<行数> 行, <要点>)
   下一步: <next stage/topic>
   ```
5. **下个 step 前 Read 回调**: 不要凭 chat 记忆引用前一步关键结论. 每个
   新 step 开始前用 Read 工具回调前一步的 chart-stage1.md / audit / 
   pre-validation-R1.md / 前面已完成的 topic-findings 关键段
6. **Stage 2 多 topic 并行时**: 每个 topic 独立 progress 报告; 不要一次
   性堆 5 个 topic 的 finding 到一段 chat 里
7. **Stage 3 consolidation 分文件输出**:
   - `chart-finding-index.md` (主文件)
   - `question-index.md` (utility)
   - 必要时按 §A 原始数据 / §B chart-level findings / §C cross-refs / §D 
     整盘 patterns 拆 sub-files (avoid 单文件 > 800 行)
8. **禁止双重输出**: 不要先在聊天框写完整内容再复制到文件. 直接写文件,
   聊天框只报 1-2 句概括

## Sibling skill family (2026-05-18 split)

This skill is the **Stage 2/3 master + chart-finding-index producer**.
For Stage 1 / pre-validation / topic-specific deep dive / timing-only /
rectification, route to the dedicated sibling skill:

| Sibling | Scope |
|---|---|
| `hellenistic-reader-unguarded` | Stage 1 data + audit + 时间精度 + pre-validation R1 + 双文件输出 |
| `hellenistic-timing-unguarded` | Standalone profections / ZR / LB / planetary years / length-of-life |
| `hellenistic-partnership-unguarded` | 7H + Venus + Lot of Marriage deep dive |
| `hellenistic-career-unguarded` | 10H + MC + Lot of Fortune/Spirit deep dive |
| `hellenistic-family-unguarded` | 4H + Sun/Moon父母 + Lot of Father/Mother (case-10 fix topic) |
| `hellenistic-rectifier-unguarded` | Birth-time rectification via Hellenistic timing matching |

All siblings share the same `rules/` doctrine in this directory. Each
sibling has minimal SKILL.md + references back here for doctrine. This
keeps each invocation lean and focused.

## Trigger conditions (master skill)

Trigger this skill ONLY when:

- practitioner explicitly asks for **multi-topic / full chart-finding-index**
  Stage 2/3 production ("跑完整 unguarded 全盘 finding")
- practitioner asks for **Stage 3 consolidation** after sibling Stage 2 modules complete
- practitioner asks for a re-write of a guarded reading that came out too hedged
- practitioner asks for chart-level aggregate (整盘双底色 / 全盘 patterns / chart-signature)

For **single-topic** deep dives, route to sibling. For **Stage 1 only**,
route to `hellenistic-reader-unguarded`. For **timing only**, route to
`hellenistic-timing-unguarded`. For **rectification**, route to
`hellenistic-rectifier-unguarded`.

**Do NOT trigger this skill for**:

- ❌ Default new chart work (use `hellenistic-natal-core` instead)
- ❌ Public-facing deliverable production for a third-party subject who
  has not consented to predictive body/death/longevity readings (this
  fork removed the technical guard but practitioner's editorial judgment still
  filters what goes out — that filter lives outside this skill)
- ❌ Horary / electional / mundane / synastry / transit-specific charts
- ❌ Picatrix-style operative magical procedure
- ❌ Entertainment-only keyword readings ("Sun in X = Y" cookbook)
- ❌ Modern psychological astrology (Jung archetype / 12-letter alphabet)
- ❌ Outer-planet (Uranus / Neptune / Pluto) primary readings
- ❌ Unsupported sign-placement snippets without audit chain

## First-invocation flow

When triggered, walk the user through:

### Step 1 — Prerequisite check (Stage 1 走 reader sibling, 不在本 skill)

本 skill 是 **Stage 2/3 入口**, 不是 Stage 1 入口. Stage 1 (chart input
verification + birth-time precision probe + 数据填表 + audit + pre-validation
R1) 全部走 `hellenistic-reader-unguarded` sibling.

检查 `charts/case-NN/` 是否有以下三件 source 文件:

- `chart-stage1.md` (Stage 1 data)
- `chart-stage1-audit.md` (audit PASS)
- `pre-validation-R1.md` (验前事 R1 hit rate + 技法 unlock)

```
全有 → 进入 Step 3 workflow path selection
缺 chart-stage1.md → 提示 "请先跑 hellenistic-reader-unguarded 准备 Stage 1
                     数据. 说 '读盘' 或提供 chart PDF / 截图 / 文本即可."
缺 audit → 提示走 reader sibling 跑 audit
缺 pre-validation → 提示走 reader sibling Step 4 跑 5 条强信号 + 收命中率
```

**不在本 skill 跑 Stage 1.** master 强依赖 reader sibling 已 produce 这三件
source 文件; 本 skill 只读, 不写 Stage 1 层文件.

### Step 2 — (deleted — no subject classification, no ethical guard)

Previous step 2 (subject classification + ethical guard per
`rules/fictional-subject-ethical-guard.md`) is **removed in this fork**.
All subjects (real person / public figure / fictional+canon-marked /
hypothetical) are processed identically. The ethical-guard rule file
has been replaced with a stub (`rules/fictional-subject-ethical-guard.md`)
noting its removal.

If you previously needed the guard to refuse body/illness/death/longevity
topics: you don't, in this fork. Process them as ordinary topics with
their actual evidence-tier confidence.

### Step 3 — Workflow path selection

Default = **v2.3 chart-finding-index**. Confirm:

- New chart work → v2.3 chart-finding-index (recommended)
- Existing v1 single-focus case work → v1 reading-workflow

### Step 4 — Mode selection (v2.3 chart-finding-index path)

| Mode | Description | Topic-findings scope |
|---|---|---|
| (a) Single topic | Stage 1 + Stage 1 audit + 1 Stage 2 module | 1 topic file |
| (b) Multi-topic | Stage 1 + Stage 1 audit + 2-3 Stage 2 modules | 2-3 topic files (no Stage 3) |
| (c) Full chart-finding-index | Stage 1 + Stage 1 audit + 15 default Stage 2 modules + Stage 3 consolidation | 15 topic files + chart-finding-index.md |
| (d) Custom | User-specified Stage 2 modules + optional Stage 3 | varies |

**Default 15 topics in this fork** (no extension/default split — all 15
treated equally):
`character` / `career` / `partnership-marriage` / `family` / `learning` /
`wealth` / `divination-spirituality` / `body` / `chart-signature` /
`children` / `siblings` / `friends-benefactors` / `illness` / `death` /
`longevity`

(Guarded variant used a 9-default + 6-extension-on-request split. This
fork merges them into one default set.)

### Step 5 — (deleted — Stage 1 dispatch 走 `hellenistic-reader-unguarded`)

原 Step 5 (Stage 1 dispatch + 双文件输出) **整段移除**. 走 reader sibling.
master 强依赖 reader sibling 已 produce `chart-stage1.md` + `subject-context.md`.

doctrine 仍然在 `rules/stage1-data-extraction.md` + `rules/data-isolation.md`,
但 dispatch 入口在 reader sibling, 不在本 skill.

### Step 6 — (deleted — Stage 1 audit 走 `hellenistic-reader-unguarded`)

原 Step 6 (Stage 1 audit independent session) **整段移除**. 走 reader sibling.
master 依赖 `chart-stage1-audit.md` PASS, 不自己跑 audit.

### Step 6.5 — (deleted — Pre-validation R1 走 `hellenistic-reader-unguarded`)

原 Step 6.5 (验前事 R1 + hit-rate technique unlock) **整段移除**. 走 reader
sibling Step 4.

doctrine 仍然在 `rules/pre-validation-reading.md`. master 读 reader sibling
产出的 `pre-validation-R1.md` 拿 hit rate + 启用的技法清单 + confidence-tier
ceiling, 但不自己跑 R1.

**Hit rate 决定本 skill Step 7+ Stage 2 finding 的 confidence-tier ceiling**:

| Hit rate | Unlocked timing (Stage 2 + Stage 3 内可引用的技法) |
|---|---|
| ≥ 4/5 | profections + planetary years + ZR (Fortune & Spirit) + LB-of-life + Hyleg/Alcocoden |
| 3/5 | profections + planetary years + ZR Spirit; ZR Fortune ⚠️; LB-of-life off |
| 2/5 | profections only; suggest rectifier |
| ≤ 1/5 | all timing off; structural skeleton only |

### Step 7 — Stage 2 dispatch (per topic, parallel after audit PASS + pre-validation)

Per `rules/chart-finding-index-workflow.md` §1 + `rules/data-isolation.md`
blind-audit window. Each module = own session.

**Dispatch 规则 (2026-05-18 case-13 retro)**:

- **自己做** (推荐): master 已 loaded SKILL.md, context 完整, 逐 topic 写.
- **派 subagent 并行** (token 压力大时): subagent prompt 里**必须 inline**
  以下 3 段 (subagent context 没有 skill 定义, invoke Skill tool 会失败):
  1. 本 SKILL.md 的 "输出规则" 段 (8 条)
  2. `rules/delineation-output-rules.md` 的 finding schema + Direct
     Relational Statement 段
  3. `rules/chart-finding-index-workflow.md` §1 topic-finding 轻 schema
- **禁止**: 派 subagent 只给 `rules/` 路径让它自己读. 那是绕过 SKILL.md,
  subagent 会漏 v2.3 架构 + 输出规则 + 渲染 routing.

**Blind-audit window inputs (Stage 2 may read)**:
- `chart-stage1.md` + `chart-stage1-audit.md`
- `pre-validation-R1.md` (chart claims + aggregate hit rate only)
- Hellenistic source extractions + `rules/*`

**Blind-audit window BANNED inputs**:
- `subject-context.md` (subject biography, practitioner stated concerns, etc.)
- Per-claim pre-validation responses (准/不准 per item)
- Other topic-findings (avoid cross-contamination)
- Chat-context info about subject

Output: `charts/case-NN/topic-findings/<slug>.md` per topic-finding 轻 schema.

### Step 8 — Stage 3 dispatch (after all chosen Stage 2 modules complete)

Per `rules/chart-finding-index-workflow.md` §2. Single session.
Output:
- `charts/case-NN/chart-finding-index.md` (主文件)
- `charts/case-NN/question-index.md` (utility)

### Step 9 — Done + Q&A mode entry

Hand chart-finding-index + question-index to decision-maker. **No reader-
facing rendering follows**. Decision-maker queries by tag combinations to
compose reader-facing answers as needed.

**Q&A mode is now active** (per `rules/qa-mode.md`). Any follow-up
question practitioner has on this chart — life domain question, timing question,
"what if" hypothetical, "we missed X" probe — gets answered with:

- 正反双审 (both supporting AND restraining evidence; never pick a side)
- Output written to `charts/case-NN/qa_<主题>.md` (NOT the chat box)
- finding-id 引用必须翻译成人话
- 反 confirmation-bias 8 条铁律 (per qa-mode.md)
- Confidence-tier ceiling 仍受 pre-validation R1 hit-rate 约束

If practitioner opens a new session and asks a question on an existing case
without invoking the full Stage 1-3 pipeline, jump straight to Q&A
mode using the existing finding-index.

### Step 10 — Reader 渲染 + HTML 打包 走 render sibling skill

Reader-facing 中文渲染 + HTML 打包**不在本 skill 完成**, 触发
`hellenistic-render-unguarded` sibling:

- "渲染 case-NN" / "写 reader" / "整理给盘主看的版本" → render skill
  按 topic-file-schema 一主题一文件输出 `charts/case-NN/reader/NN-<slug>.md`
- "打包成 HTML" / "生成报告 HTML" → render skill `scripts/report_builder.py`
  合并 `reader/` 下所有 `NN-*.md` 输出 `charts/case-NN/report.html`

详见 render skill SKILL.md.

If you ARE composing a reader-facing portrait (走 render sibling 时),
那边的规则 (anti-cliche + direct-relational-statement + session-learnings
+ topic-file-schema) 会接管. 不要在本 skill 直接写 reader 散文 — 走错
skill 等于丢掉反八股约束.

(Historical: 原 `rules/delineation-output-rules.md` Direct Relational
Statement 段已抽到 render skill `rules/direct-relational-statement.md`,
本 skill 那段留 banner.)

## Reference files (identical set to guarded variant, with two replacements)

- `../v2.3-chart-finding-index-architectural-plan.md` — v2.3 architecture
- `rules/chart-finding-index-workflow.md` — Stage 2/3 spec
- `rules/chart-finding-index-tags.md` — tag inventory v2.1
- `rules/stage1-data-extraction.md` — Stage 1 spec
- `rules/topic-modules.md` — per-topic 太极点 + Lens tables
- `rules/dignities-reference.md` — domicile / exaltation / triplicity /
  bound / decan reference tables
- `rules/aspect-reception-rules.md` — aspect detection + reception
- `rules/planet-condition-audit.md` — planet audit subroutine
- `rules/significator-hierarchy.md` — significator framework
- `rules/lots-and-fortune.md` — Lots formulas + topic Lots
- `rules/timing-techniques.md` — profection / ZR / LB / planetary years
- **`rules/pre-validation-reading.md` — NEW in this fork** (验前事 R1 +
  hit-rate gating technique unlock + confidence-tier ceiling)
- **`rules/qa-mode.md` — NEW in this fork** (post-finding-index Q&A 模式 +
  正反双审 + 反 confirmation-bias 8 条 + qa_<主题>.md 输出)
- **`rules/data-isolation.md` — NEW in this fork** (chart-stage1.md vs
  subject-context.md 双文件隔离; Stage 2 盲审窗口禁读 subject-context)
- **`rules/delineation-output-rules.md` — MODIFIED in this fork**
  (Difficult-Condition Guardrails removed; Direct Relational Statement
  + Time-period 段已抽到 render skill, 原位留 banner)
- **Reader 渲染走 sibling**: 反八股 + Direct Relational Statement +
  session-learnings + topic-file-schema + report_builder.py 全部在
  `hellenistic-render-unguarded` skill, 不在本 skill 直接 reference
- `rules/cross-source-method-comparison.md` — source cross-references
- **`rules/fictional-subject-ethical-guard.md` — REPLACED in this fork
  with stub noting removal**

## What this skill does NOT produce

(Same as guarded variant.)

- ❌ Reader-facing essay / narrative-deliverable / TL-clean as a separate
  "pipeline stage" (deprecated v2.2 forms)
- ❌ 800-行 Stage 2 narrative composite reading (v2.2 form)
- ❌ 1049-行 Stage 3 portrait essay synthesis (v2.2 form)
- ❌ TL pass (`*-TL.md` siblings) — TL skill deprecated
- ❌ Prose normalization (`*-TL-clean.md`) — prose-normalizer skill deprecated

The deliverable IS the chart-finding-index source layer. Reader-facing
outputs come from decision-maker querying that source — not from this
skill rendering one.

**Reader-facing deliverable 走 sibling skill**: 任何 reader-facing 中文
散文输出 (整盘 portrait / 单 topic reader 文件 / actionable summary /
赛道地图 / 给盘主直接看的总结) 全部走 `hellenistic-render-unguarded`,
不在本 skill 产出. 本 skill 出 source 层 (chart-finding-index +
topic-findings), render skill 把那些渲染成 reader 中文散文按
topic-file-schema 一主题一文件输出, 可选 HTML 合并.

## Subject discipline (anti-cookbook reminder — KEPT)

Per `rules/delineation-output-rules.md` §"Anti-Cookbook Rules" — every
life-claim sentence in finding statements has subject = native / a person /
a felt state / a domain / a mode / a relation / a structure. NEVER a chart
factor as life-claim grammatical subject.

**This fork sharpens the rule**: when the subject is "a domain" or "a
mode" or "a structure," the sentence must still resolve to a concrete
relational/event-level statement (see Direct Relational Statement
section). Subjects like "结构性的责任依托" or "心理模式" or "行动模式"
that NEVER concretize into "和父母吵架"、"在工作里发火"、"和家人关系破裂"
are **euphemism abuse of the domain/mode subject category** and banned
in this fork.

## Output discipline reminders

(Identical to guarded variant on the doctrinal side.)

- Every finding carries Stage 1 row_id chain WITH raw data embedded
- Every finding carries Hellenistic basis with ≥2-source triangulation
  status (or `[Source-only candidate]` flag)
- Every finding carries source-status-labeled tags from `chart-finding-
  index-tags.md` v2.1
- Mixed-evidence reported as mixed (well-evidenced contradiction); not
  averaged
- **REMOVED in this fork**: difficulty findings carrying mandatory
  pressure + mitigation + channel triad (this becomes optional, not
  mandatory; if the evidence supports a direct outcome statement,
  write the direct outcome)
- **REMOVED in this fork**: speculative auto-flag on canon-resonance
  findings unless the EVIDENCE is speculative (canon-marked subject
  status no longer auto-downgrades)

## What next (post-finding-index)

After chart-finding-index complete, decision-maker uses it directly:

- Want to answer a specific reader-question? Query `question-index.md`
- Want to extend with another topic? Re-dispatch Stage 2 with that slug
- Want to revisit a finding's confidence? Update finding entry in
  `chart-finding-index.md` per the actual evidence (not per topic
  membership)
