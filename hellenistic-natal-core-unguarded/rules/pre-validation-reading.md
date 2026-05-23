# Pre-Validation Reading (验前事) — Hellenistic Adaptation

> v2.3-unguarded (2026-05-18) — newly added to the unguarded fork. Adapted
> from parallel-reader-skill Step 5 验前事 mechanism. The principle: before any deep
> chart finding production, do 5 strong-signal chart-derived claims and ask
> practitioner (or the subject themselves) for **准 / 不准 / 部分准** feedback. Hit
> rate gates which Hellenistic timing techniques unlock + sets the default
> confidence-tier ceiling for the rest of the reading.
>
> **Why this matters for the unguarded fork**: without a hit-rate calibration
> step, the unguarded fork still risks the same "over-confident wrong claim"
> failure mode that the guarded fork tried to prevent via blanket hedging.
> Verification at the front replaces hedging at the back.

## Core principle

> **Strong-signal first. Pick claims that have ① short derivation chain
> (≤2 steps), ② multiple Hellenistic source corroboration, ③ are immediately
> falsifiable by the subject. Skip claims that need vibes / character
> projection / unverifiable body marks / health predictions. The point is
> not "5 claims at any cost" — better 3 hits with 0 misses than 5 with 3
> misses.**

## When to run

- **Default for new chart work**: run after Stage 1 + Stage 1 audit PASS,
  before Stage 2 dispatch.
- **Skip if**: subject is fictional+canon-marked AND no live subject to
  give feedback (no point — there's no oracle to validate against). For
  fictional+canon, use canon material as the validation oracle instead
  (per `chart-finding-index-tags` v2.1 canon-resonance flow).
- **Re-run if**: rectifier changed the Lagna; old hit rate is voided.

## Output of this step

A single deliverable `charts/case-NN/pre-validation-R1.md` containing:

1. The 5 claims numbered, each with one-line derivation quote (per format
   below)
2. Subject's feedback (准 / 不准 / 部分准) per claim
3. Hit-rate calculation
4. Technique-unlock decision per the gate table (see "Hit rate → technique
   unlock" section)
5. Confidence-tier ceiling for downstream Stage 2 / Stage 3

## Candidate pool (Hellenistic-derivable strong signals)

### Tier A (highest historical hit rate; pick first)

**A.1 Asc lord placement → temperament/embodiment**
- Derivation: Asc lord sign + house + dignity + bonification/maltreatment
- Signal type: "你给人的第一印象是 [X], 你自己内感是 [Y]"
- Example: Leo Asc + Sun in 7H Aquarius → "你给人的感觉是关系性的、需要别人镜映才有方向；不是从自己门口直接长出来的那种自我感"
- Falsifiable: Yes — subject knows their own first-impression vs internal experience

**A.2 Sun placement + condition → father / authority figure pattern**
- Derivation: Sun sign + house + sect status + receptions + aspects
- Signal type: "和父亲的关系结构性是 [近/远/紧张/疏离/严苛/失踪/...]"
- Example: Sun in 7H + Saturn cross-tier reception + Sun-Saturn aversion → "父亲影响是从一段距离照过来的、跟严肃/承担感绑在一起、但你和父亲互相不太能直接对话"
- Falsifiable: Yes — direct fact-of-life claim

**A.3 Moon placement + condition → mother / felt-emotional baseline / body**
- Derivation: Moon sign + house + sect status + receptions + phase
- Signal type: "母亲影响 [近/远/吞噬/缺位/严苛/疏离], 你的情绪 [饱满/空白/急迫/沉重/反复]"
- Example: Moon in 1H tight conjunction Mars → "母亲影响贴得很近、跟你的情绪和动作模式绞合在一起；你情绪默认带摩擦、急迫、容易点火"
- Falsifiable: Yes — subject knows their default emotional register and mother-relationship

**A.4 Saturn placement → 承担 / 重负载领域 / 边界形态**
- Derivation: Saturn sign + house + dignity + sect (of-sect malefic = less
  destructive in day chart) + hosted-by chain
- Signal type: "你在 [X 领域] 长期扛着结构性责任 / 觉得无法逃避的重量"
- Example: Saturn 8H Pisces 3-tier hosted by Jupiter → "你在隐位（深处的、别人看不见的、关于死亡/转化/共同资源/秘密）扛着重大责任，但你扛的方式是住在木星的领地里——靠被一个更大的接纳框架托住"
- Falsifiable: Yes — subject knows what they shoulder

### Tier B (good hit rate; pick when Tier A signals weak)

**B.1 4 lord / IC condition → family root / childhood baseline**
- Derivation: 4H lord + 4H occupants + IC sign + Moon-as-4-significator
- Signal type: "家庭根基 [稳定/破裂/缺席/承担/疏离]"
- Note: 在 unguarded fork 里这条不再 default-OFF；直接陈述

**B.2 10 lord placement → public-life / vocation domain**
- Derivation: 10H lord + 10H occupants + MC sign + Sun-as-10-significator-day
- Signal type: "你的公开生活 [台前/幕后/继承/自力/慢路/快路]"

**B.3 Profected lord activation year → significant life event**
- Derivation: 当前年份 = 主年 N → profected house = (N % 12) + 1H → profected lord = ruler of that house
- Signal type: "在 [profected year 起止] 这段时间, 你的生活在 [profected house topic] 领域有过明显事件 — [profected lord 状态决定方向]"
- Strong window: 主年 N where profected lord is angular + well-dignified OR maltreated
- Example: 主年 30 profect to 7H → 30 岁那年伴侣 / 重大合作关系有事

**B.4 ZR Spirit major-period transition year**
- Derivation: ZR from Lot of Spirit, identify recent / upcoming major period transition (or LB peak)
- Signal type: "在 [年份] 前后，你的人生方向 / 重心有过一次明显的转折"
- Note: 需要时间精度 ≤ ±15分钟 才可用；时间精度差就 skip 这条改用 B.3

### Tier C (条件触发，特定 chart 配置才用)

**C.1 Lot of Fortune topical placement** — 物质生计形态
- Derivation: Lot of Fortune sign + house + ruler condition
- Signal type: "你的生计来路 [稳定/起伏/隐藏/外显/...]"

**C.2 Lot of Spirit topical placement** — 行动志向 / 主动追求形态
- Derivation: Lot of Spirit sign + house + ruler condition
- Signal type: "你主动选的方向 [明确/反复换/隐藏/...]"

**C.3 Mercury phase + condition** — 心智运作节奏
- Derivation: Mercury 晨星/昏星 + retrograde + heliacal phase + dignity
- Signal type: "你的脑子运转 [快/慢/迭代/线性/...]"

### Tier D (硬禁; never use as pre-validation claim)

- ❌ 身体标记 / 痣 / 疤痕的具体位置（不可证伪率高）
- ❌ 疾病具体预测（伦理之外，命中率低）
- ❌ 性格描述（不可证伪 — 谁都觉得自己符合一半）
- ❌ 关于未来的预言（验前事是验 PAST，不是验 FUTURE）

## Selection logic (per session)

```
Step 1: 跑 Tier A 4 个候选；标记每个是「强信号 / 中信号 / 弱信号」
  - 强信号: derivation ≤ 2 步 + 多源证据 + 状态明确（不在边界）
  - 中信号: derivation = 2-3 步 + 1-2 源 + 状态偏一边
  - 弱信号: derivation > 3 步 OR 单源 OR 状态混合

Step 2: 强信号 ≥ 3 → 只用 Tier A 出 4-5 条
  强信号 = 2 → Tier A 2 条 + Tier B 选 2-3 条
  强信号 ≤ 1 → Tier A 1 条 + Tier B 2 条 + Tier C 1-2 条

Step 3: 检查覆盖
  ✅ 至少 1 条 structural (家庭 / 求学 / 公共形象 等结构性事实)
  ✅ 至少 1 条 timing event (B.3 profection 或 B.4 ZR)
  ✅ 不混用同一颗行星 (e.g., 不要 A.1 用 Asc 主, A.4 又用同一颗 — 输出会显得单调)

Step 4: 排序: 结构性事实在前 → 时间事件在后

Step 5: 输出格式 (markdown, NOT 包在代码块里)

Step 6: 等用户给 准 / 不准 / 部分准 反馈
```

## Output format (markdown 直接渲染, 不要包代码块)

```
在进入完整 finding 制作之前，我先用你盘里 5 个最强信号做一次校准——
这一步决定后面 ZR / 流年长度法这些时间技法是否启用 + 整体 confidence
天花板。逐条回复 准 / 不准 / 部分准 即可。

**1.** [结构性事实主推断]

> 推导: [行星 + 宫位 + 状态 + 关键 reception/aspect] → [结论方向]

**2.** [结构性事实/Tier A]

> 推导: [...]

**3.** [结构性事实/Tier A 或 B]

> 推导: [...]

**4.** 在 [YYYY-YYYY 年] 期间, 你 [具体 profected/ZR 事件域]

> 推导: [profection 第 N 年 → profected house X → profected lord Y 状态 Z]

**5.** [可选; 仅信号足够强时]

> 推导: [...]
```

## Hit rate → technique unlock (硬约束)

| Hit rate | 时间技法启用 | Confidence-tier ceiling | 处理 |
|---|---|---|---|
| **≥ 4/5** | ✅ profections + planetary years + ZR (Fortune + Spirit) + LB-of-life + Hyleg/Alcocoden | High 可用 | 继续 Stage 2 全套，正常 confidence assignment per evidence |
| **3/5** | ✅ profections + planetary years + ZR Spirit; ⚠️ ZR Fortune 标 [time-sensitive]; ❌ LB-of-life 时长法关 (或仅作 Open Thread) | High 仅在 ≥3 source triangulation + audit chain 强; 否则 Moderate cap | 继续 Stage 2，长寿 / 死亡时机的 finding 主动 mark `[time-cal-needed]` |
| **2/5** | ✅ profections 仅; ❌ planetary years / ZR / LB / Hyleg-Alc 全关 | Moderate cap; Body/illness/death/longevity 默认 Low cap | 强烈建议 rectifier; Stage 2 可继续但标 `[time-validation-low]` |
| **≤ 1/5** | ❌ 所有时间技法关 | Low cap on relational/event 类 finding; 仅 D1 性格 / Lots 的 topical 结构可用 | 应该走 rectifier；如果跳过就显式声明 reading 是 "structural skeleton only" 不含 timing |

## 反锚定规则（与参考体系 一致）

```
1. 用户回复 "不准" → 直接记录, 不重新解释, 不降精度匹配, 不顺着用户改口
2. 用户回复 "部分准" → 记 0.5 分; 可追问 "哪部分准哪部分不准" 用于理解偏差
3. 用户回复 "准" → 记 1 分; 不延伸解读, 不当成 "进一步分析的突破口"
4. 用户后续在反馈过程中透露的个人信息 → 写入 subject-context.md (per rules/data-isolation.md), Stage 2 盲审阶段禁读
5. 唯一允许的追问: 时间相关的 "这件事大概发生在几年?" (用于 rectifier 入口判断)
```

## 反验前事失败模式

```
❌ "我刚才说 2020 你说不准, 那其实是 2019 的事吧?" — 不许 retrofit
❌ "你说没结婚, 那可能是因为... 让我换个角度..." — 不许重新解释
❌ "5/5 都准, 那你的盘说你应该..." — 不延伸到未确认的新论断
❌ 推导用 "你大概 18 岁上大学" 默认标准年龄假设 — 用 profection/ZR 时间窗口本身说话
❌ "因为我们已经知道你是 X, 所以..." — 验前事是数据→结论, 不是反向 anchor
```

## Source status

`[project heuristic]` adapted from parallel-reader-skill Step 5. Should be validated
against case-10 re-read (running case-10 through pre-validation with the
known reality oracle to check if Tier A signals would have caught the
family-conflict and 心理模式 hedge issues at the front).
