---
name: hellenistic-family-unguarded
description: Hellenistic family / parents / origins deep-dive — UNGUARDED sibling. SOURCE LAYER ONLY — 只产 Stage 2 topic-findings/family.md source schema (英文 + 表格 + finding-id + Hellenistic basis + audit refs), NOT reader-facing 中文散文. Focused Stage 2 on 4H (root/mother/lineage) + 10H-as-father (Hellenistic father convention) + Sun (father day-sig) + Moon (mother nat-sig) + Lot of Father + Lot of Mother. Reader 中文渲染 (避免 case-10 hedge 失败 mode 那种产出) 走 `hellenistic-render-unguarded` sibling, 不在本 skill. Use when practitioner says "跑 case-NN 的 family source / 看 family Stage 2 / family deep dive (source 层)". 不触发: "渲染 family / 写 family reader" 那走 render skill.
---

> v2 (2026-05-18 cleanup) — 删了原本写在本 skill 的中文 reader prose 例子
> + 重定义 output 为纯 source schema. Reader 中文渲染走 render sibling.
> Source/reader 双拥有 cleanup, 不再两边产同样路径文件.

# Hellenistic Family — Unguarded (SOURCE LAYER)

## Role

Topic-focused Stage 2 source 层 deep dive on family / parents / lineage /
siblings significators. **只产 source schema** (英文 + 表格 + finding-id +
Hellenistic basis + audit refs + Pressure/Mitigation/Channel + brief shot
types). **不产 reader 中文散文** — 那走 `hellenistic-render-unguarded`.

跟 master `hellenistic-natal-core-unguarded` Stage 2 family 模块**功能等价**,
区别只在: master 跑 full chart-finding-index 时一并跑所有 topic; 本 sibling
只 focus family 一个 topic + cover 比 master 更深的 family-specific dimensions
(尤其 sub-topics 列表 + Hellenistic father convention 10H 处理).

## Doctrine reference

source-stage doctrine 全在 `../hellenistic-natal-core-unguarded/rules/`:
- `topic-modules.md` family + siblings section
- `significator-hierarchy.md`
- `lots-and-fortune.md` — Lot of Father / Lot of Mother formulas
- `chart-finding-index-workflow.md` Stage 2 finding schema
- `chart-finding-index-tags.md` v2.1 tag inventory

reader 渲染 doctrine (中文散文规则) 全在 `../hellenistic-render-unguarded/rules/`,
本 skill **不引用** (因为本 skill 不写 reader prose):
- `anti-cliche.md` / `direct-relational-statement.md` / `session-learnings.md` /
  `topic-file-schema.md`

## Trigger

- "看 case-NN 的 family Stage 2 / source"
- "unguarded 跑 family deep dive (source)"
- "4H + Sun/Moon 父母 + Lot of Father/Mother analysis"
- "兄弟姐妹 source finding" (虽然本 skill 默认 family, 但 sibling 维度也 cover)
- 派 subagent 跑 single-topic Stage 2 时 (vs master 跑 all-topic Stage 2)

**不触发**:
- "渲染 family / 写 family reader" → 走 render skill
- "整理给盘主看的家庭段" → 走 render skill
- "case-NN 的 family 解读 (中文给我)" → 走 render skill (render skill 会读
  本 skill 产出的 topic-findings/family.md source + 渲染成中文)
- 全盘 Stage 2/3 — 走 master

## Prerequisite

```
检查 charts/case-NN/chart-stage1.md:
  → 不存在 → 提示走 hellenistic-reader-unguarded 准备 Stage 1.

检查 charts/case-NN/chart-stage1-audit.md PASS 状态:
  → 失败/缺 → 跑 audit 再来.

检查 charts/case-NN/pre-validation-R1.md hit rate:
  → ≥ 4/5 → 全 timing 技法可用
  → 3/5 → ZR Spirit + profections OK, ZR Fortune ⚠️
  → ≤ 2/5 → 仅 profections; 建议 rectifier
```

## Workflow

### Step 1 — Read source

读 chart-stage1.md + chart-stage1-audit.md + pre-validation-R1.md (chart 部分,
不读 subject 反馈 — per `../hellenistic-natal-core-unguarded/rules/data-isolation.md`
blind-audit 窗口禁读 subject-context).

### Step 2 — Significator chain (multi-axis)

Hellenistic family 4 条平行 lookup:

1. **Mother**: Moon condition + 4H lord condition + Lot of Mother + Mother-
   as-natural-significator-by-sect (day = Venus, night = Moon doubly emph)
   + Venus condition
2. **Father**: Sun condition + **10H-as-father lord** condition (Hellenistic
   convention — NOT 4H which is modern Western convention; this is doctrine
   point) + Lot of Father + Saturn-as-father-day / Sun-as-father-night
3. **Family root / lineage / origins**: 4H lord + 4H occupants + IC sign +
   Lot of Father if it's "family lineage" reading
4. **Siblings**: 3H lord + 3H occupants + Mars-as-sibling-significator
5. Cross-aspects: Sun-Moon aspect + Sun/Moon receptions + Saturn relation
   to 4H lord

### Step 3 — Source finding production

per `chart-finding-index-workflow.md` §1 finding schema. 每个 TF-family-NN
finding 含:

- **Statement** (英文 1-2 句 structural fact, 不是 reader prose)
- **Polarity** (structural / difficulty / spectrum)
- **Confidence** (high / mixed-high / moderate / low / speculative)
- **Tags** (per chart-finding-index-tags v2.1)
- **Method status** (full-source / specialist-supplement / project-composite /
  project-heuristic)
- **Concentrated testimony** (yes/no + carrier/cap if yes)
- **Audit refs** (T0/T1/T2/T3/T4/T6 row_ids)
- **Hellenistic basis** (≥2-source citations: Brennan/Valens/Firmicus/Dorotheus)
- **Pressure / Mitigation / Channel** (per difficulty findings)
- **Brief shot 类型库** (structural English 一句话 candidates — supply 给 render
  skill 当 reader 渲染原料; **本 skill 不出中文 prose**)
- **direct_claim_candidate** (NEW field, optional): 1-2 个英文 structural-
  parsed claim 类型 (e.g., "father=remote-with-weight", "mother=fused-on-self-
  axis-driver-bound", "parents=tightest-opp-cross-host", "lineage-burden=
  Saturn-8H-hosted-by-Jupiter-5H"). render skill 接管时把这些翻成中文人话.

### Step 4 — 必须覆盖的 sub-dimensions (source 层必出)

source schema 必须含 finding 覆盖以下维度 (英文 structural, 不是 reader prose):

- Mother-axis (per Moon + 4H + Venus + Lot of Mother)
- Father-axis (per Sun + 10H-as-father + Saturn + Lot of Father)
- Parents-coordination (Sun-Moon aspect + receptions)
- Lineage / ancestral weight (Saturn + Lot of Mother 8H-tenancy if applicable)
- Family-root stability (4H tenants + 4H lord condition + transit/profection
  history if pre-validation R1 allows)
- Native's role in family system (which significator carries which role)
- Siblings (3H + Mars) if not extension-OFF
- Domestic events 重大 turning points (profected to 4H/10H/3H 主年, ZR
  transitions on Saturn / Sun-Moon-axis)

### Step 5 — Timing (per pre-validation hit-rate ceiling)

- Profections to 4H (主年 4/16/28/40/52/64/76) — 家庭根基激活窗口
- Profections to 10H (Hellenistic father convention) — 父系激活
- Profections to 3H — 兄弟姐妹相关
- ZR transitions 涉及 Saturn / Sun-Moon aspects 的窗口
- 关键过去年份 retro-validation (per pre-validation R1 hit rate allowed)

每个 timing 窗口在 source 用 `[year YYYY] [trigger: profected lord X / ZR Y /
LB peak] [topic: Z]` 表格化 — **不在本 skill 出 reader 时间括号"为什么"**,
那是 render skill 的事.

### Step 6 — 输出 (source schema)

写入 `charts/case-NN/topic-findings/family.md` per `chart-finding-index-
workflow.md` schema. 输出形态:

- 英文 (主体)
- 表格 + finding-id schema
- citation block (Brennan/Valens/Firmicus/Dorotheus refs + Stage 1 row_id)
- brief shot 类型库 (structural English)
- direct_claim_candidate 字段 (structural English, render 接管翻中文)
- Open threads (诚实保留)

**不在本 skill 写**: 中文 reader prose, ❌/✅ 对照例, 整盘 mouthfeel 段,
narrative essay 段.

进度报告:
```
=== family Stage 2 finding 完成 ===
写入: charts/case-NN/topic-findings/family.md (<行数> 行, <N> TF-family
findings)
Confidence: <evidence-tier + pre-validation R1 ceiling>
下一步: 触发 render 渲染 family 中文 deliverable / 或继续其他 topic
```

## Reader 中文渲染走 render sibling

practitioner 要中文 family 段时:

```
→ 触发 hellenistic-render-unguarded
→ render skill 读 topic-findings/family.md (本 skill 产出) + chart-stage1.md
→ 按 topic-file-schema 输出 charts/case-NN/reader/05-family.md (中文)
→ 反八股 + direct-relational-statement + session-learnings 全套规则在那 skill
→ 整盘 HTML 合并 也走 render skill scripts/report_builder.py
```

case-10 family 反例 + v4 好范例: `hellenistic-render-unguarded/samples/`.

## Q&A 模式

per `../hellenistic-natal-core-unguarded/rules/qa-mode.md`. 短答 (1-2 句确认 + 引 finding-id 翻人话) 可在本 skill 答; 长中文 narrative 答走 render skill.
