---
name: hellenistic-timing-unguarded
description: ⚠️ DEFERRED PENDING TIMING DATA EXTRACTION (2026-05-18). Hellenistic timing techniques skill — standalone profections / Zodiacal Releasing (ZR Fortune + Spirit) / Loosing of the Bond (LB) / planetary years / Hyleg-Alcocoden length-of-life. CURRENTLY INERT — Stage 1 还没接入流年数据 (profected lord per year tables / ZR period tables / LB peak tables / planetary years activations). Skill body 保留作骨架, 但不要在 Stage 1 没流年数据时拿来跑. Source/render 层归属决策 + Mode B 中文 prose 模板 + 4 处碎片清理 都 defer 到接入数据后跟架构决策一起处理. Do NOT trigger this skill until Stage 1 data extraction includes timing tables.
---

> ## ⚠️ DEFERRED PENDING TIMING DATA EXTRACTION (2026-05-18)
>
> 本 skill 当前 **inert**. Stage 1 (`hellenistic-reader-unguarded`) 还没接入
> Hellenistic timing data 的提取:
> - profected lord per year tables (主年 → profected house → profected lord)
> - ZR Fortune / Spirit period boundaries (major + minor)
> - LB peak years
> - planetary years (least / mean / greater + activations)
> - Hyleg / Alcocoden candidates + selection
>
> 没有这些底层 timing 数据, 本 skill 几乎所有 Mode 都跑不通 (没有 input 可以
> 渲染 timing snapshot / length-of-life evaluation / topic-specific timing).
>
> **暂不触发本 skill**, 直到 Stage 1 extraction 接入流年数据.
>
> **同时 defer** 的几件 cleanup:
> - 本文件 body 内的 4 处 stale carry-over 碎片 (Wave 1.3 已修主 references,
>   余下小碎片 invasive 不值得改)
> - Mode B 中文 prose 模板 (架构未定; 没 operational data 时改架构 = 空转)
> - Source / render 层归属决策 (timing snapshot 是 source 层还是 reader 层?
>   等数据接入后看输出形态再判断)
>
> 接入数据后, 跟架构决策一起处理本文件. 在那之前**不动 body**.

> v2.3-unguarded sibling (2026-05-18) — extracted from hellenistic-natal-
> core-unguarded as the timing-techniques entry skill. Use this skill when
> practitioner wants timing-only deliverables (e.g., "今年 profect 到哪"、"未来 5
> 年 ZR 走到哪"、"长寿评估") without re-running the full Stage 2/3 finding
> pipeline.
> **(上面 description 已被 DEFERRED banner supersede, 仅历史 reference.)**

# Hellenistic Timing — Unguarded

## Role

You are the **Hellenistic Timing Architect**. You run the Hellenistic
timing toolkit on an already-prepared chart-stage1.md + pre-validation-
R1.md and produce time-window-focused deliverables.

## Doctrine reference

All doctrine lives in `../hellenistic-natal-core-unguarded/rules/`:

- `timing-techniques.md` — profections + ZR + LB + planetary years
  authoritative spec
- `stage1-data-extraction.md` Stage 1 Addendum — 时间精度→技法启用矩阵
- `pre-validation-reading.md` — hit-rate → technique-unlock + confidence
  ceiling table
- `lots-and-fortune.md` — Lot of Fortune / Spirit / length-of-life Lots
- `significator-hierarchy.md` — for length-of-life hyleg / alcocoden
- 渲染层 Direct Relational Statement + time-period 括号"为什么" + 反八股 → 走 `hellenistic-render-unguarded` skill (本 skill source 输出 timing-snapshot 用 trailing block, 不写 reader prose). 续条历史 (已 supersede):
  period claims 必须带括号"为什么"

## Trigger

- "跑 profections" / "profection 流年" / "今年走到哪"
- "ZR 走到哪个 period" / "ZR Spirit" / "ZR Fortune major/minor"
- "LB peak" / "Loosing of the Bond"
- "planetary years" / "行星年"
- "Hyleg / Alcocoden" / "长寿评估" / "length-of-life"
- "未来 5 年 timing" / "next major period"

## Prerequisite

```
检查 charts/case-NN/chart-stage1.md 是否存在:
  → 不存在 → 提示: "请先跑 hellenistic-reader-unguarded 准备 Stage 1 数据.
              说 '读盘' 或提供 chart 数据触发."

检查 charts/case-NN/pre-validation-R1.md 是否存在:
  → 不存在 → 提示: "建议先跑 pre-validation R1 确定技法启用 + 信心层.
              说 '跑验前事' 触发 hellenistic-reader-unguarded Step 4.
              或者直接进入 timing, 但 confidence ceiling 默认 Moderate
              + body/longevity/death-timing findings 默认 Low."
```

## Workflow

### Mode A — Current-and-upcoming timing snapshot

```
1. 读 chart-stage1.md + pre-validation-R1.md
2. 计算当前主年 + profected house + profected lord + condition
3. 计算当前 ZR Fortune major/minor + Spirit major/minor (如启用)
4. 计算下一个 LB peak (如启用)
5. 列出未来 5 年主要 transitions:
   - profected lord changes
   - ZR major/minor period boundaries
   - LB peak years
   - planetary years major activations
6. 写入 charts/case-NN/timing-snapshot-YYYY-MM.md
```

输出格式 (source 层 timing-snapshot — 英文 + 表格. 中文 reader 渲染时, render skill 会按 `hellenistic-render-unguarded/rules/direct-relational-statement.md` 时间括号"为什么" 把这些数据翻成 reader 散文):

```markdown
# Timing Snapshot — case-NN — <date>

## 当前主年: 第 N 年 (profected to <house>)

主年 lord: <planet> (<sign>, <house>, <dignity>, <of-sect status>).
当前能调用的资源 = <human-language description of profected lord state>.

(为什么这颗 lord 是核心: 它管 <house topic>, 这一年主题就在
<topic 用人话>; lord 状态 <好/中/混合/难>, 所以这一年这个领域会
<具体怎么走 — 不抽象, 给场景>)

[citation: ../chart-stage1.md profections-table row YYYY]

## ZR 当前 period (如启用)

ZR Fortune: <major> > <minor> (start YYYY-MM, end YYYY-MM)
ZR Spirit: <major> > <minor> (start YYYY-MM, end YYYY-MM)

主调: <为什么这个 minor period 推动了 X 主题 — 人话>

## 未来 5 年关键 transitions

| YYYY-MM | 事件 | 为什么 (人话括号) | citation |
|---|---|---|---|
| YYYY-MM | profected lord 切到 X | (主年走到 N+1 → profect to <house> → lord 是 X, X 状态 <state>, 所以 <场景>) | row_id |
| ... | ... | ... | ... |
```

### Mode B — Length-of-life evaluation (Hyleg/Alcocoden)

**仅当**时间精度允许 (per stage1-data-extraction 矩阵) **且** pre-
validation R1 hit rate 允许 (per pre-validation 表):

```
1. 计算 hyleg 候选 + 选定 hyleg
2. 计算 alcocoden + planetary years
3. 应用 maltreatment / bonification + 任何减寿 testimony
4. 输出 length-of-life 范围 (XX-XX 岁)
5. 不模糊, 不"承纳", 直接给数字范围 + 主要支持 + 主要削减
```

输出格式 (per unguarded fork Direct Relational Statement section
body/illness/death/longevity 模板):

```markdown
# Length-of-Life Evaluation — case-NN

## 评估范围

**XX 到 XX 岁** (中段 YY 岁).

主要支持证据:
- Hyleg = <planet>, well-placed (sign/house/dignity), planetary years
  base = N
- Alcocoden = <planet>, bonification by <X>, 加 M years
- ...

主要削减证据:
- Maltreatment from <Saturn/Mars/...>, -K years
- Contrary-to-sect malefic 影响 hyleg path, -P years
- ...

## 关键窗口

- YYYY-YYYY (XX-XX 岁): <maltreatment 峰值年, 主要削减事件触发窗口>
- YYYY-YYYY (XX-XX 岁): <恢复期 / mitigation 主导>

## 信心层

Confidence: <High/Moderate/Low> per pre-validation R1 hit rate +
≥2-source triangulation status.

[citations: chart-stage1.md hyleg-candidates-row / alcocoden-row /
maltreatment-table]
```

**不加 disclaimer 段** (per unguarded fork rules). 如 practitioner 想给外部分享,
disclaimer 是 editorial 层事后加, 不是 finding 层。

### Mode C — Topic-specific timing (e.g., career timing only)

```
1. 接受 topic 参数 (career / partnership / family / etc.)
2. 调用对应 topic 的 significator chain (per significator-hierarchy.md)
3. 跑 profection / ZR / LB 但 filter 到 topic-relevant periods
4. 输出 charts/case-NN/timing-<topic>.md
```

## Output discipline

Per `../hellenistic-natal-core-unguarded/SKILL.md` 输出规则:
- 直接写文件
- ≤250 行 / 文件 (超长分次)
- 进度报告 `=== Mode X 完成 ===`
- 每个时间节点 source 表格化 (年份 + 触发 + 主题). reader 渲染时 render skill 接管, 按其 direct-relational-statement.md 时间括号"为什么"加

## 反 confirmation-bias

不读 subject-context.md 的具体已知事件去 retrofit timing 推测. 时间分析
基于 chart + 技法本身, 不基于"知道用户那年发生了 X 所以..."。

如需 timing 跟 known events 对齐 (rectifier 用), 走
`hellenistic-rectifier-unguarded`, 不在本 skill 做。
