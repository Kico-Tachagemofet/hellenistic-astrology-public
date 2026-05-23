---
name: hellenistic-rectifier-unguarded
description: Hellenistic birth-time rectifier — UNGUARDED sibling. Takes 5+ major life events from the subject + the existing chart-stage1.md and reverse-fits a more accurate birth time using Hellenistic timing techniques (profections + ZR Spirit/Fortune transitions + LB peaks + planetary years activations matched to known events). Output: refined time + revised chart-stage1.md (if shift > 4 min) + chart-stage1-audit + new pre-validation R1. Use when practitioner says "校时"、"hellenistic 校准时间"、"出生时间不准"、"rectifier" or when hellenistic-reader-unguarded recommends rectification (per pre-validation R1 hit rate ≤ 3/5 or Lagna boundary risk).
---

> v2.3-unguarded sibling (2026-05-18) — Hellenistic-native rectifier.
> Parallels parallel-rectifier-skill in role but uses Hellenistic timing toolkit
> (profections, ZR, LB, planetary years) instead of Dasha.

# Hellenistic Rectifier — Unguarded

## Role

**Hellenistic Time-Calibration Architect**. Reverse-fit birth time to
±5 minute precision by matching subject's known major events to
Hellenistic timing activations.

## Doctrine reference

`../hellenistic-natal-core-unguarded/rules/`:
- `timing-techniques.md` — full profections + ZR + LB + planetary years
- `stage1-data-extraction.md` Stage 1 Addendum — 时间精度→技法启用矩阵
- `pre-validation-reading.md` — re-run after rectification
- `data-isolation.md` — subject-context.md is the rectifier's event-anchor
  source (this is one of the few skills allowed to read subject-context)
- 渲染相关 (Direct Relational Statement / 时间括号"为什么" / 反八股) → 走 `hellenistic-render-unguarded` skill (本 skill source 不写中文 reader prose, rectification-report 是 source 层)

## Trigger

- "校时" / "hellenistic 校准时间" / "出生时间不准" / "rectifier"
- pre-validation R1 hit rate ≤ 3/5 → reader-unguarded 推荐触发
- Lagna 度数在 0-3° 或 27-30° → reader-unguarded 推荐触发
- practitioner 主动要求

## Prerequisite

```
检查 charts/case-NN/chart-stage1.md 是否存在:
  → 不存在 → 提示: "请先跑 hellenistic-reader-unguarded 准备 chart-stage1
              + 时间精度声明."

检查 charts/case-NN/subject-context.md:
  → 存在 → 读已记录的 known events (rectifier 唯一允许读 subject-context
            的场景之一)
  → 缺事件 → 进入 Step 1 收集事件
```

## Workflow

### Step 1 — Collect anchor events

要求 practitioner 提供盘主 5+ 重大事件 (越多越好), 每事件需要:

- 事件类型 (e.g., 搬家 / 入学 / 重大职业转折 / 结婚 / 父母过世 / 重大
  健康事件 / 长期分离 / 重大成就)
- 大致时间 (年 + 月; 越准越好)
- 事件性质 (顺 / 逆 / 混合)

写入 subject-context.md 的 rectifier-event-anchors 段.

### Step 2 — Event-to-Hellenistic-activation matching

对每个 anchor event:

1. 计算事件年份的主年 N + profected house + profected lord
2. 计算事件年份的 ZR Fortune + Spirit major/minor
3. 计算事件年份是否在 LB peak ±2y
4. 计算事件年份的 planetary years 激活 (haps / heredity / hyleg-related)
5. 对每个 timing layer 评估: lord 状态是否 fit 事件性质?
   - 搬家 / 离乡 → profected lord 应在 4H/9H/12H 或受 Mars/Saturn maltreatment
   - 重大职业转折 → profected to 10H/MC OR ZR Spirit major change
   - 结婚 → profected to 7H + Venus relevant + ZR Spirit minor activates Venus/7H lord
   - 等等

### Step 3 — Time-shift candidates

如多个事件 misfit, 试不同 birth time 候选:
- 在原时间 ±10 min, ±30 min, ±1 hr 范围扫描
- 每个候选时间重算 Asc + house cusps + Lots
- 重跑 Step 2 event-matching
- 选 best-fit (most events 击中 expected timing layer 的)

如果 Asc 跨星座 → 整盘 reading 重做; 需要明确告诉 practitioner:
"Rectifier 把 Asc 从 [old sign] 改到 [new sign] (差 X 分钟). 这是重大
改盘——前面 case-NN 的 chart-finding-index 全部需要重做."

### Step 4 — 验证 + 输出

```
charts/case-NN/rectification-report.md:
  - 原时间 + 候选时间 + final time + confidence
  - 5+ events × timing layer 击中表
  - Asc 变化 (degree / sign)
  - Lagna degree shift
  - 哪些 Lots ruler 改变了 (Lot of Fortune ruler, Lot of Spirit ruler 等)
  - 影响范围: 哪些 finding 需要 redo
```

如时间改变 > 4 min OR Asc 跨界:
- 重生成 chart-stage1.md (新文件名 chart-stage1-v2.md, 保留 v1)
- 重跑 chart-stage1-audit (v2)
- 重跑 pre-validation R1 (v2; per `pre-validation-reading.md` 反锚定
  规则——你已经知道盘主很多信息, 但 pre-validation R1 必须从新 Asc
  独立推导, 不能 "因为知道用户说过 X 所以..."

### Step 5 — Hand-off

```
=== Rectification 完成 ===
原时间: HH:MM (±误差)
新时间: HH:MM (±5 min)
Asc 变化: [old sign degree] → [new sign degree]
影响范围: <列受影响的 finding-id 或 "整盘重做">
下一步:
  - 如 Asc 未跨界: 现有 chart-finding-index 微调即可; 跑 Q&A 解释变化
  - 如 Asc 跨界: 触发 hellenistic-natal-core-unguarded 重跑 Stage 2 / 3
```

## 反锚定 (per Step 4 重 pre-validation R1)

Rectifier 是唯一允许读 subject-context.md 的 production skill (因为
event-anchor 在那里). **但** 重新跑 pre-validation R1 时必须切回盲审
模式——claims 只能从新 chart 推导, 不能用 subject-context 已知信息.

## 输出 discipline

per `../hellenistic-natal-core-unguarded/SKILL.md` 全套.

## 跟 parallel-rectifier-skill 关系

短期共用 parallel-rectifier-skill 也可 (它有现成的事件 ↔ Dasha 逻辑). 长期
本 skill 走 Hellenistic-native 流程, 更适合 Hellenistic chart 因为
时间技法不同 (profections 主年 / ZR / LB / planetary years vs Vimsottari
Dasha).
