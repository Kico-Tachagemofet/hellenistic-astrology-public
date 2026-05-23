---
name: hellenistic-partnership-unguarded
description: Hellenistic partnership / marriage deep-dive — UNGUARDED sibling. SOURCE LAYER ONLY — 只产 Stage 2 topic-findings/partnership-marriage.md source schema (英文 + 表格 + finding-id + Hellenistic basis + audit refs), NOT reader-facing 中文散文. Focused Stage 2 on 7H + Venus + Lot of Marriage + Lot of Eros + DK Lot. Reader 中文渲染走 `hellenistic-render-unguarded` sibling, 不在本 skill. Use when practitioner says "跑 case-NN 的 partnership / marriage source / 看 partnership Stage 2 / 7H deep dive (source 层)". 不触发: "渲染 partnership / 写感情段中文" 那走 render skill.
---

> v2 (2026-05-18 cleanup) — 删原本写在本 skill 的中文 reader prose 例子 +
> 重定义 output 为纯 source schema. Reader 中文渲染走 render sibling.
> Source/reader 双拥有 cleanup, 不再两边产同样路径文件.

# Hellenistic Partnership — Unguarded (SOURCE LAYER)

## Role

Topic-focused Stage 2 source 层 deep dive on 7H + relevant Lots +
relationship significators. **只产 source schema** (英文 + 表格 + finding-id
+ Hellenistic basis + audit refs + Pressure/Mitigation/Channel + brief shot
types + direct_claim_candidate). **不产 reader 中文散文** — 那走 render skill.

## Doctrine reference

source-stage doctrine 全在 `../hellenistic-natal-core-unguarded/rules/`:
- `topic-modules.md` partnership-marriage section
- `significator-hierarchy.md` — 7H lord + Venus-as-natural-significator-day +
  Lot of Marriage + Lot of Eros + DK
- `aspect-reception-rules.md` — 7H lord aspects + receptions
- `timing-techniques.md` — profections to 7H + ZR transitions
- `lots-and-fortune.md` — Lot of Marriage / Eros formulas
- `chart-finding-index-workflow.md` Stage 2 schema
- `chart-finding-index-tags.md` v2.1

reader 渲染走 `../hellenistic-render-unguarded/rules/`, 本 skill 不引用.

## Trigger

- "跑 case-NN 的 partnership / marriage source"
- "unguarded 跑 7H deep dive (source)"
- "Lot of Marriage / Eros 分析 (source)"
- "婚姻时机 source finding"

**不触发**:
- "渲染 partnership / 写感情段中文" → render skill
- "整理给盘主看的婚姻分析" → render skill
- 全盘 Stage 2/3 — 走 master
- Synastry (synastry 走单独 case + project-composite methodology)

## Prerequisite

```
检查 charts/case-NN/chart-stage1.md + audit + pre-validation-R1.md.
缺 → 走 hellenistic-reader-unguarded.
```

## Workflow

### Step 1 — Read source

读 chart-stage1.md + chart-stage1-audit.md + pre-validation-R1.md (chart 部分, 不读 subject 反馈).

### Step 2 — Significator chain

per `topic-modules.md` partnership-marriage + significator-hierarchy.md:

1. 7H lord identification + condition (sign + house + dignity + sect +
   aspects + receptions + bonification/maltreatment)
2. Venus (natural sig day-chart; or Mars night-chart per sect doctrine —
   check actual chart sect)
3. Lot of Marriage (Venus-formula per Valens) + Lot of Marriage ruler condition
4. Lot of Eros + ruler (per Brennan)
5. DK Lot (Descendant Lord projection) if used
6. 7H occupants (none / 1 / multiple — sect/dignity 影响伴侣画像)
7. Cross-aspects from 7H lord to other rulers — 跟哪些 topic 绞合
   (e.g., 7H lord 同位 4H lord → 婚姻和家庭根基绞合)

### Step 3 — Source finding production

per `chart-finding-index-workflow.md` §1 finding schema. 每个 TF-partnership-NN finding 含:

- **Statement** (英文 structural 1-2 句)
- **Polarity**, **Confidence**, **Tags** (per v2.1)
- **Method status**, **Concentrated testimony**, **Audit refs**
- **Hellenistic basis** (≥2-source: Brennan/Valens/Firmicus/Dorotheus)
- **Pressure / Mitigation / Channel** (difficulty findings)
- **Brief shot 类型库** (structural English candidates)
- **direct_claim_candidate** (英文 structural-parsed claim types,
  e.g., "partner-type=Saturnian-mature-distant", "encounter-pattern=
  through-mutual-collaboration", "marriage-window-likelihood=偏 delayed",
  "relationship-cycle=test-withdraw-fuse-test"). render 接管翻中文.

### Step 4 — 必须覆盖的 sub-dimensions (source)

source schema 必须 cover (英文 structural, 不是 reader prose):

- 7H-lord-condition (partner topic 主轴)
- Venus-condition (relational signature)
- Lot of Marriage placement + ruler chain
- Lot of Eros placement + ruler chain (if relevant)
- Partner-type signature (from 7H sign/lord/occupants)
- Encounter-pattern (which axis ts the relationship form takes)
- Cross-domain entanglements (7H lord ↔ other rulers aspects)
- Marriage-timing windows (per profections to 7H + ZR transitions)

### Step 5 — Timing

- Profections — historical + future 5-10y, 7H 主年 (主年 7/19/31/43/55/67)
- ZR Spirit / Fortune — Venus / 7H lord / Lot of Marriage minor period
- LB peaks 涉及 partnership theme (如启用)

source 表格化: `[year YYYY] [trigger] [topic]`. **不在本 skill 出 reader
时间括号"为什么"** (render skill 的事).

### Step 6 — 输出 (source schema)

写入 `charts/case-NN/topic-findings/partnership-marriage.md` per
chart-finding-index-workflow schema. 形态: 英文主体 + 表格 + finding-id
+ citation block + brief shot 类型库 + direct_claim_candidate + Open
threads. **不写中文 reader prose, 不写 ❌/✅ 对照例, 不写 mouthfeel 段.**

进度报告:
```
=== partnership Stage 2 finding 完成 ===
写入: charts/case-NN/topic-findings/partnership-marriage.md (<行数> 行, <N> TF-partnership-marriage findings)
Confidence: <evidence-tier + pre-validation R1 ceiling>
下一步: 触发 render / 或继续其他 topic
```

## Reader 中文渲染走 render sibling

practitioner 要中文感情段时:

```
→ 触发 hellenistic-render-unguarded
→ render 读 topic-findings/partnership-marriage.md + chart-stage1.md
→ 按 topic-file-schema 输出 charts/case-NN/reader/04-partnership-marriage.md
→ 反八股 + direct-relational-statement + session-learnings 全套在 render
→ 整盘 HTML 也走 render
```

样例参考: `hellenistic-render-unguarded/samples/`.

## Q&A 模式

per `../hellenistic-natal-core-unguarded/rules/qa-mode.md`. 短答可在本 skill;
长中文 narrative 走 render.
