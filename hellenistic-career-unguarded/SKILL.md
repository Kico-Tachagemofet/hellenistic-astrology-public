---
name: hellenistic-career-unguarded
description: Hellenistic career / vocation deep-dive — UNGUARDED sibling. SOURCE LAYER ONLY — 只产 Stage 2 topic-findings/career.md source schema (英文 + 表格 + finding-id + Hellenistic basis + audit refs), NOT reader-facing 中文散文. Focused Stage 2 on 10H + MC + Lot of Fortune + Lot of Spirit + Lot of Reputation. Reader 中文渲染 (actionable 事业建议 / 适合 / 不适合 / 时机表) 走 `hellenistic-render-unguarded` sibling, 不在本 skill. Use when practitioner says "跑 case-NN 的 career source / 看 career Stage 2 / 10H deep dive (source 层)". 不触发: "渲染 career / 写事业方向中文" 那走 render skill.
---

> v2 (2026-05-18 cleanup) — 删原本写在本 skill 的中文 reader prose 例子 +
> 重定义 output 为纯 source schema. Reader 中文渲染走 render sibling.
> Source/reader 双拥有 cleanup.

# Hellenistic Career — Unguarded (SOURCE LAYER)

## Role

Topic-focused Stage 2 source 层 deep dive on 10H + MC + 事业 Lots. **只产
source schema** (英文 + 表格 + finding-id + Hellenistic basis + audit refs +
direct_claim_candidate). **不产 reader 中文散文** — 那走 render skill.

## Doctrine reference

source-stage doctrine 全在 `../hellenistic-natal-core-unguarded/rules/`:
- `topic-modules.md` career section
- `significator-hierarchy.md` — MC lord + 10H lord + Lot of Fortune
  (livelihood) + Lot of Spirit (chosen direction) + AmK 等价物 if used +
  Sun (natural day-significator of authority)
- `lots-and-fortune.md`
- `timing-techniques.md`
- `chart-finding-index-workflow.md` Stage 2 schema
- `chart-finding-index-tags.md` v2.1

reader 渲染走 `../hellenistic-render-unguarded/rules/`, 本 skill 不引用.

## Trigger

- "跑 case-NN 的 career source"
- "unguarded 跑 10H deep dive (source)"
- "MC analysis source" / "Lot of Fortune/Spirit source 分析"
- "事业 source finding"

**不触发**:
- "渲染 career / 写事业方向中文 / actionable 事业建议" → render skill
- "整理给盘主看的事业部分" → render skill
- 全盘 Stage 2/3 — 走 master

## Prerequisite

```
检查 charts/case-NN/chart-stage1.md + audit + pre-validation-R1.md.
缺 → 走 hellenistic-reader-unguarded.
```

## Workflow

### Step 1 — Read source

读 chart-stage1.md + chart-stage1-audit.md + pre-validation-R1.md (chart 部分).

### Step 2 — Significator chain

1. MC lord + 10H lord (same or different per Whole-Sign vs Quadrant 兼用)
2. 10H occupants
3. Lot of Fortune sign + ruler + condition (livelihood 来路)
4. Lot of Spirit sign + ruler + condition (chosen direction)
5. Sun (natural day-significator of authority) + condition
6. Cross-aspects: 10H lord ↔ 2H lord (income wire) / 11H lord (collaborators
   + 流量) / 6H lord (daily-grind 类型) / 9H lord (long-form 求知 / 远方
   方向)
7. Receptions network — 10H lord hosted by malefic / benefic / 谁

### Step 3 — Source finding production

per `chart-finding-index-workflow.md` §1. 每个 TF-career-NN finding 含:

- **Statement** (英文 structural)
- **Polarity / Confidence / Tags** (v2.1)
- **Method status / Concentrated testimony / Audit refs**
- **Hellenistic basis** (≥2-source)
- **Pressure / Mitigation / Channel** (difficulty findings)
- **Brief shot 类型库** (structural English)
- **direct_claim_candidate** (英文 structural-parsed: "vocation-form=
  backstage-discipline-routed", "income-wire=structural-via-Saturn-domain",
  "career-stability=slow-build-multi-role", "unsuitable=台前-broadcast-fast-
  pivot", "key-window=YYYY-YYYY-profect-10H-Mercury-activated"). render
  接管翻中文 actionable claims.

### Step 4 — 必须覆盖的 sub-dimensions (source)

source schema 必须 cover:

- 10H-lord-condition (vocation 主轴)
- MC degree (literal vocation cusp) + 10-WSH split (如 angle-vs-WSH divergence)
- Lot of Fortune (livelihood form)
- Lot of Spirit (chosen direction)
- Income-wire (10H lord ↔ 2H / 11H / 8H cross-aspects)
- Daily-grind 形态 (6H lord interaction)
- Cross-domain entanglements (10H lord ↔ 4H/7H 等)
- 不顺盘的 form (反向 fit signature)
- Career timing windows (profect 10H / ZR Spirit major / LB)

### Step 5 — Timing

- Profections — 10H 主年 10/22/34/46/58 + 2H/11H income windows
- ZR Spirit — 重大方向转折
- ZR Fortune — 物质来路转折 (如启用)
- LB peaks 涉及 career theme (如启用)

source 表格化, 不出 reader 时间括号"为什么".

### Step 6 — 输出 (source schema)

写入 `charts/case-NN/topic-findings/career.md` per workflow schema. 英文主体
+ 表格 + finding-id + citation + brief shot 类型库 + direct_claim_candidate
+ Open threads. **不写中文 reader prose, 不写 ❌/✅, 不写"适合 / 不适合"
list 中文版** (那是 render 的事).

进度报告:
```
=== career Stage 2 finding 完成 ===
写入: charts/case-NN/topic-findings/career.md (<行数> 行, <N> TF-career findings)
Confidence: <evidence-tier + pre-validation R1 ceiling>
下一步: 触发 render / 或继续其他 topic
```

## Reader 中文渲染走 render sibling

practitioner 要中文事业段 / actionable 建议 / 适合不适合 list / 时机表时:

```
→ 触发 hellenistic-render-unguarded
→ render 读 topic-findings/career.md + chart-stage1.md
→ 按 topic-file-schema 输出 charts/case-NN/reader/02-career.md
→ 反八股 + direct-relational-statement + session-learnings 全套在 render
→ render 把 direct_claim_candidate 翻成 actionable 中文 ("适合做 X / 不适合
  做 Y / 关键窗口 YYYY-YYYY")
→ 整盘 HTML 也走 render
```

样例参考: `hellenistic-render-unguarded/samples/`.

## Q&A 模式

per `../hellenistic-natal-core-unguarded/rules/qa-mode.md`. 行业 / 岗位
适配追问短答可在本 skill (引 source finding-id + 1-2 句确认); 长中文
narrative 答走 render.
