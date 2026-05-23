# Q&A Mode — After Chart-Finding-Index Complete

> v2.3-unguarded (2026-05-18) — newly added to the unguarded fork. Adapted
> from parallel-core-skill Q&A mode. The principle: after `chart-finding-index.md`
> and `question-index.md` are in place, the skill stays available for any
> follow-up question practitioner has — life domain question, timing question,
> "what if" hypothetical, comparison to another chart, edge case the
> finding-index didn't pre-enumerate. Each Q&A round produces a small
> `qa_<topic>.md` file in the case folder.

## When to enter Q&A mode

- After Stage 3 (chart-finding-index complete) is the default entry
- After a single-topic Stage 2 finding-set complete (Mode a in SKILL.md
  Step 4) — Q&A scoped to that topic
- When practitioner re-opens a session on an existing case and asks a question
  (no need to re-run pipeline; jump to Q&A)

## When NOT to enter Q&A

- During Stage 1 / Stage 1 audit / Pre-validation R1 / Stage 2 dispatch /
  Stage 3 — these are production steps, not interactive answer steps
- For a question that requires regenerating a topic-finding (e.g., user
  says "redo the partnership finding with X assumption changed") — that's
  a Stage 2 re-dispatch, not Q&A

## Core principle: 正反双审 (most important rule)

**For any judgement question ("适不适合"、"会不会"、"是不是"、"能不能"、
"什么时候"), the answer MUST list both supporting evidence AND restraining
evidence. Picking only the side the user wants to hear is banned.**

```
❌ User: "我能不能在 2027 年换工作?"
   Bad answer: "可以的, 你 2027 年木星大运正在激活 10 宫主..."
   (Only the supporting side; ignored Saturn transit + 6H lord activation)

✅ Good answer: "2027 年这个窗口的盘面是混合信号:
   支持换的: profected lord 进 10H + Jupiter ZR Spirit minor period
   activates career significator + finding F-career-04 已记录该年是
   '事业重定向窗口'
   制约的: 同时 Saturn transit 过 IC 触发 4H lord →
   家庭根基有压力 (finding F-family-02), 换工作如果伴随搬家或
   家庭决策会更难;
   另外 6H lord 大运未结束, 当下工作的 daily-friction 还没释放完
   平衡判断: 换工作的时机本身 OK, 但选'能减少家庭/居住变动'的
   换法、避开同时换工作 + 搬家组合。"
```

## Output discipline (与 Stage 2/3 一致)

- **直接写文件**: 每次 Q&A 回答写入 `charts/case-NN/qa_<主题>.md`，
  聊天框只报 1-2 句概括 + 文件路径
- **不在聊天框写完整回答** — 聊天框是 progress 通道, 不是答案通道
- **每次 Write ≤ 250 行** — 超长分次追加 (per SKILL.md 输出规则)
- **语言风格 (Q&A 答的中文 narrative 子段)**: 走 `hellenistic-render-unguarded` skill 的 `rules/anti-cliche.md` + `rules/direct-relational-statement.md` + `rules/session-learnings.md`. 即: 70% 通俗 + 20% 数据 + 10% 注释; 反 chart-factor 拟人; 时间节点括号"为什么"; trailing citation 不 inline; 别几把不是而是了
- **术语必须当场翻译** (per SKILL.md 术语使用规则)
- **finding-id 引用要翻成人话**:
  ✅ "你的事业重心是结构性走幕后路线 (F-career-02 + F-career-04: MC 主金星
  从 6 宫角落运作 + 唯一直接通道是接到土星)"
  ❌ "per F-career-02 and F-career-04, vocational orientation is structural-
  backstage-trajectory"

## Q&A 文件命名

- 主题相关: `qa_career_change.md` / `qa_marriage_timing.md` / `qa_family_conflict.md`
- 多轮同主题: `qa_career_change-r1.md` / `qa_career_change-r2.md`
- 跨主题综合: `qa_synthesis_2026-05-18.md` (用日期)

## Q&A 文件 schema

```markdown
# Q&A: <主题> — <日期>

## 问题

<原问题或问题概括>

## 直接回答

<2-3 句概括, 正反双审, 不绕弯>

## 支持的证据

- <Finding ID 翻译成人话> — <为什么这条支持>
- <Finding ID> — <为什么>

## 制约 / 反向的证据

- <Finding ID> — <为什么这条制约>
- <Finding ID> — <为什么>

## 时机层 (如问题含时间)

| 窗口 | 启动信号 | 适合度 | 推导 |
|---|---|---|---|
| YYYY-YYYY | profected lord X + ZR Y + transit Z | 顺/逆/混 | <人话> |

## 平衡判断

<2-3 段; 说明在 yes/no 之外的"怎么做才能让支持的一面 actually 发生 +
制约的一面被对冲"的 actionable 指引>

## Open thread (诚实保留)

- <这次问题里未覆盖的边缘>
- <需要追加 Stage 2 重做某 topic 才能完整回答的部分>
```

## 几种常见问题类型的处理

### A. 行业 / 岗位适配问题 ("我做 X 行业 / 岗位适合吗?")

- 引用 10H lord + MC + AmK (如果跑了 D10-style 配合 OR 10H 主审计) +
  career-related finding
- 给"顺盘 / 逆盘 / 混合"三分判断, 不只挑 yes
- 如果 finding-index 没覆盖该具体岗位维度 → Open thread, 不编造

### B. 时机问题 ("XX 年/时段适合 做 Y 吗?")

- 引用 profection lord (主年) + ZR (Fortune / Spirit per topic) +
  major transit 大象
- 必须基于 pre-validation R1 命中率允许的技法层 (per `pre-validation-
  reading.md` hit-rate table) — 如果时间技法被关, 直接说"该问题需要
  时间精度升级，建议跑 rectifier"
- 时间窗口表格化呈现 (per qa_schema.md template above)

### C. 假设推演 ("如果我选 X 会怎样?")

- 列利弊, 不做价值判断
- 引用 finding-index 现有 finding 推导, 不编造新 finding
- 如果假设要触发 finding-index 没覆盖的维度 → Open thread

### D. 跟另一个人比较 / synastry 类问题

- ❌ 不在 hellenistic-natal-core-unguarded 处理 — synastry 不是本 skill scope
- 提示 practitioner: "synastry 走单独 case (per case-09×11 synastry state methodology)"

### E. 用户说"不像我 / 不准 / 偏差大"

- 不辩解, 不重新解释, 不顺着改口
- 直接确认: "记下了。如果是多个 topic 都感觉偏差, 建议跑 rectifier
  确认出生时间精度。说'校准时间'触发 `hellenistic-rectifier-unguarded`
  (Hellenistic-native, 走 profections + ZR + LB + planetary years 事件
  反推)。"
- 如果是单条 finding 偏差 → 进入 finding-update 流程: `chart-finding-
  index.md` 里该 finding 的 confidence 降级或加 [time-cal-needed] 标

## 反 confirmation-bias (与 parallel-core-skill 8 条铁律同源)

```
1. 禁止从用户在 Q&A 中透露的新信息反推 finding 含义
   ❌ "你说你抑郁过 → 把 8 宫 finding 往抑郁方向重新解"
   ✅ "8 宫的 finding 已经在 chart-finding-index 里，我引用现有的"

2. 不同盘主同样数据 → 同样答案
   ❌ "考虑到你是 [富/贫/某背景], 我建议..."
   ✅ "盘面证据指向 [方向], 你的具体背景影响怎么落地不影响方向本身"

3. 用户说"准" 不当突破口
   ❌ "太好了, 这说明你的盘进一步表明..."
   ✅ "记下了" (然后继续答原问题)

4. 用户说"不准" 直接接受
   ❌ "其实从另一个角度可以说..."
   ✅ "记下了, 这条标 [偏差]"

5. 经历 ≠ 天赋
   ❌ "你经历过痛苦 → 适合做心理咨询"
   ✅ "适合什么方向 from L10 + chart-signature finding, 不 from
      生平事件"

6. 不读 subject-context.md 来"装作"独立推论
   - subject-context 是反馈/偏差记录, 不是 finding 来源
   - Q&A 答案的 finding-id 引用必须出自 chart-finding-index / 
     topic-findings / pre-validation 这些 source 文件

7. Dasha / Time-period 回顾必须双向
   - 已发生时段 = 同时列出正面 + 负面表达
   - 不能因为知道 "用户那段时间过得苦" 就只写负面
   - 不能因为 "那段时间过得好" 就只写正面

8. Q&A 引用的 finding 仍受 pre-validation hit-rate 的 confidence-tier
   ceiling 约束 — 如 hit rate 2/5, 任何引用 body/illness/death/longevity
   finding 的答案需要打 Low cap, 不要在 Q&A 里偷偷升回 High
```

## 跨语言

- 用户用中文问 → 中文答, 术语翻译
- 用户用英文问 → 英文答, finding-id 引用保留原文
- finding-index 是 source layer 不翻译 — Q&A 是 reader 层 才翻译

## Source status

`[project heuristic]` adapted from parallel-core-skill Q&A mode.
Hellenistic version drops the references to D9/D10 specifics and adds
finding-id 引用 + ZR/profection 时机表格层。
