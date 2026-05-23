# Composition Pass — v2.3 Stage 3B Authoritative Spec

> ## ⚠️ UNGUARDED FORK OVERRIDE (2026-05-18)
>
> References in this file to **ethical-guard.md** (the file is now a
> stub), **ethical-guard:fictional+canon → Mode + Form default N/A**,
> **Mode-section-suppression rule**, **confidence:speculative drops
> composition to speculative** when triggered by guarded-variant
> auto-downgrade — all NO-OP in this fork.
>
> Composition confidence (最弱链规则) still applies: min of constituent
> finding confidences. But constituent confidences come from actual
> evidence merit, not topic-membership auto-downgrade. A body /
> death / longevity finding with solid ≥2-source basis is High; the
> composition that references it is not auto-dropped to Speculative.
>
> The Mode + Form section of composition is NOT suppressed for any
> topic in this fork — including former extensions.

---

> **v2.3 stub** (2026-05-17 created by practitioner, 10-item review pass applied
> same day) — initial spec for v2.3 Stage 3B composition layer. Sits above
> `rules/chart-finding-index-workflow.md` §2 (Stage 3A registry
> consolidation), producing the "整盘 mouthfeel" layer that chart-finding-
> index.md §D was supposed to carry but in practice produces as 散装
> patterns list. This file is **additive** to existing workflow: Stage 3 =
> 3A (registry, per workflow.md §2 §A-§C; §D = 薄索引层 only) + 3B
> (composition, per this file). Stage 3A §D "整盘 patterns" mouthfeel
> 承载移到 3B `composition.md` chart-level output and per-topic Composition
> 末段.
>
> **2026-05-17 review pass** (10 items P1+P2 applied):
> - P1.1 §1 fate contradiction: 改 "薄索引层保留" replacing
>   "deprecated by this file"
> - P1.2 workflow.md sync: §2 banner + output 列 + file structure block +
>   architecture diagram 3A/3B split (in chart-finding-index-workflow.md)
> - P1.3 method-index.md sync: §1A.v2.3 step 4 → step 4 (3A) + step 5 (3B)
> - P1.4 §7 最弱链规则 inline: composition confidence = MIN of organizing
>   finding confidences
> - P2.5 §2 nested code fence: outer ````markdown (4-backtick) to allow
>   inner ```markdown blocks
> - P2.6 §4 强制覆盖规则: ALL polarity:structural/tension places OR
>   audit-log pruning to §7 Pruned places field
> - P2.7 §3 explicit-N/A 必须 cite Trigger + Citing findings/rule
> - P2.8 §5 Step 3 disambiguation: fictional+canon subjects 用 chart-
>   structural baseline, NOT canon baseline; canon resonance to §6
> - P2.9 §7 复合 verdict precedence rule (强制 enumerate, ascending order)
> - P2.10 §6 mechanism taxonomy `[TBD-case-NN-3B]` marker replacing 模糊 —
>
> Full spec finalized in Phase 3 after example-case first end-to-end test. This
> stub + 10-item review establishes schemas + procedures + cross-references
> so example-case can run end-to-end without ambiguity.
>
> For full architectural context see `v2.3-chart-finding-index-
> architectural-plan.md`. For tag inventory see `rules/chart-finding-
> index-tags.md` v2.1 (canonical). For workflow (Stage 1/2/3A) see `rules/
> chart-finding-index-workflow.md`.

## Purpose

v2.3 Stage 3A (registry) consolidates topic-findings into `chart-finding-
index.md` per workflow.md §2. Audit-chain intact + 35-45 chart-level findings
queryable by tag. But registry alone produces 散装材料感: each finding
stands but reader experiences fragmentation, not 整盘.

Stage 3B (composition) consumes Stage 3A output + produces:

1. **`composition.md`** — chart-level mouthfeel layer (整盘 dominant flavor
   + tension mechanisms + execution handoffs + composite image + do-not-
   flatten)
2. **Per-topic Composition 段** appended to each `topic-findings/<slug>.md`
   末段 (type spectrum + not-fit mechanism + arc shape + mode-form)

decision-maker queries 3A for tag-based lookup, 3B for mouthfeel +
reader-question-shape rendering scaffolding. Reader-facing answer still
hand-composed by practitioner/AI on top of both layers per v2.3 framing.

## §1 Stage 3A vs 3B 分工

| Aspect | 3A Registry (workflow.md §2) | 3B Composition (this file) |
|---|---|---|
| Output | `chart-finding-index.md` (§A-§C) | `composition.md` + topic-findings 末段 |
| Form | finding entries + cross-link graph | role-organized + flavor-named + reader-question-scaffold |
| Purpose | tag-based lookup | mouthfeel + question-shape rendering |
| Audit | full Stage 1 raw embedded per finding | per-sentence footnote refs to finding IDs |
| Frequency | grows with new findings | re-compose only on chart-signature-level changes |
| workflow.md §D | 薄索引层保留 (high-level pattern → finding-ref list only) | mouthfeel + tension + handoff + composite image 全 |

**Trigger to re-compose 3B**:
- chart-signature topic-findings 变更
- 新 finding 被 promoted to chart-level §B 且 lifts to ≥ 2 tension axes
- 复合主味 anchor 之一被 invalidated
- decision-maker 发现 reader output 出现拍平倾向 (调用 do-not-flatten 失效)

非以上情况：3A 追加 finding 不 force 3B re-compose。

## §2 `composition.md` chart-level 7-段 schema

File: `charts/case-NN/composition.md`

````markdown
# Composition — case-NN <subject>

> Stage 3B chart-level mouthfeel layer. Built atop chart-finding-index.md §B
> findings. Per-sentence audit hooks via markdown footnotes `[^F<NNN>]` 
> referring to chart-finding-index.md §B finding IDs.

## §1 Ingredient Register

按 role 锁 (closed enum)，不按 finding ID 顺序。每 role 字段后括号注 finding 
refs。每 role 至少 1 条；可空 (then explicit "N/A — <reason>")。

- **Base spirit** (1, 强制): <承载主结构的 finding 群>
  - finding refs: [F<NNN>, F<NNN>]
  - 一句说明 (≤ 1 句, anti-cookbook subject) [^F<NNN>]
- **Modifiers** (1-3, 强制): <改主味方向的因素>
  - 各自 finding refs + 一句说明
- **Binders** (0-3, 可空): <让冲突得以衔接的因素>
- **Bittering / Edge** (1-3, 强制): <压力 / 切割 / 粗粝感>
- **Dilution / Chill** (0-2, 可空): <缓冲 / 延迟 / 降低直接性>
- **Garnish / Aroma** (0-2, 可空): <读者最先闻到但非底层>

## §2 Dominant Flavor

复合主味允许 (per practitioner anchor 2026-05-17): primary flavor + 可选 structural 
counter-flavor。

- **Primary flavor** (≤ 8 字): <主味命名>
- **Counter-flavor** (≤ 8 字, 可空): <结构性反主味, 仅 split-mandate chart 用>
- **Why this not the loudest**: <一句, 解释为何不是高频 finding>
- **Organizing finding IDs**: 列被这主味 organize 的 finding refs (≥ 60% chart-
  level findings 必须可 frame 为 modifier/binder/edge of 主味, per §5 procedure)
- **Counter-flavor risk**: 一句, 如果选错主味会变成什么

## §3 Tension Mechanisms

每条 tension 用同一 mechanism schema (mechanism type 见 §6 taxonomy):

```
### Tension <#N> — <mechanism type name>

- **Components** (finding refs): <张力两端的 finding IDs> [^F<NNN>] [^F<NNN>]
- **Mechanism** (一句): 如何运作；不是 "有冲突"，是 "如何运作"
- **Handled as** (closed enum): 绕开 | 抵消 | 调和 | 保留 | 转化
- **Do not flatten**: 一句, 错误的拍平方式
```

至少 1 条 tension; 上限不设。

## §4 Execution Handoffs

按 topic place; 每条用同一 verdict schema (verdict closed taxonomy 见 §7):

```
### Handoff — <topic / WSH place>

- **Promise carrier** (in-house tenant + condition): <Stage 1 T1 + T5 refs>
- **Manager / Ruler** (sign-lord + condition): <Stage 1 T6 refs>
- **Handoff verdict** (closed enum, 7 项): 顺流 | 错位 | 绕路 | 降速 | 技术化 | 间接化 | 卡住
- **Why this verdict**: doctrine refs + finding IDs [^F<NNN>]
- **Mouthfeel description** (一句): 不是 verdict 词，是 "promise 有, 但 manager 接住后 X" 这种描述
```

**强制覆盖规则** (替换原 "relevant" 模糊 quantifier):
- 覆盖 chart-finding-index.md §B 中**所有**带 `polarity:structural` 或
  `polarity:tension` 标的 finding 所触及的 topic places (i.e. WSH-houses
  + 直读的话题宫 e.g. career → 10H + 6H / partnership → 7H + 5H / etc)
- 若某 place 被裁剪 (not-applicable / signal-too-weak / 主体非 relevant),
  **必须 audit-log 该裁剪 + reason**, 写入 §7 Audit Backtrace 新增字段
  `Pruned places`: `[<place>: <reason + finding ref if applicable>]`
- 未 audit-log 的裁剪 = Gate 失败, 退回补足

**理由**: example-case retro 显示 "relevant" 字眼会被实做者 default 为 "我觉得
重要的", 导致系统性遗漏 (e.g. 7H 看似 unimportant 实际承载 partnership
mouthfeel)。强制 enumerate-or-audit 切断这种默认。

## §5 Composite Image

- **整盘 mouthfeel** (≤ 3 句; subject 必须人 / 状态 / 路径 per via negativa 
  铁律, 禁止抽象属性作主语): <调好的整体感> [^F<NNN>] [^F<NNN>]
- **First taste** (≤ 1 句): 读者先尝到什么
- **Last taste / 余味** (≤ 1 句): 走后留下什么
- **What this is NOT** (≤ 2 句): 避免把它误读成什么

## §6 Do-not-flatten Notes

按 chart-level 整盘列错误 simplification:

- **拍平 1**: <错误读法> — Why wrong: <一句> [^F<NNN>]
- **拍平 2**: ...
- **拍平 3**: ...

至少 2 条; 上限不设。

## §7 Audit Backtrace

- **All finding IDs cited**: [F<NNN>, F<NNN>, ...] (complete inventory)
- **Stage 1 row_ids touched**: [T0-..., T1-..., T2-..., ...]
- **chart-finding-index §B 引用 coverage**: <NN / 总数> (≥ 60% 强制)
- **Confidence on composition itself** (per **最弱链规则**: composition confidence = MIN of constituent finding confidences across all findings referenced in §2 Dominant Flavor "Organizing finding IDs" list. e.g. 8 organizing findings of which 6 are `confidence:high` + 2 are `confidence:moderate` → composition confidence = moderate. If any reference is `confidence:speculative`, composition itself drops to speculative regardless of count): high | moderate | low | speculative | mixed
- **Counter-flavor stress test outcome** (per §5 Step 4): <single-flavor | dual-flavor | undefinable>
- **Pruned places** (per §4 强制覆盖规则): `[<place>: <reason + finding ref
  if applicable>]` list of polarity:structural / polarity:tension places
  intentionally not covered in §4 Handoffs. Empty list = full coverage.
  Required field; cannot be omitted even if empty (write `[]` or "无").

[^F001]: chart-finding-index.md §B F001 — <short finding statement>
[^F002]: chart-finding-index.md §B F002 — <short finding statement>
...
````

## §2.5 Per-Planet Portrait (强制, character topic 渲染必需 source)

> Added 2026-05-18 (practitioner anchor): case-10 `reader-entry-portrait.md` 性格 section
> 是 best-practice precedent — per-planet 8 段把整盘从性格角度逐行星过一遍.
> 切到 per-topic reader/ 架构时 case-12 + case-09 regression 到 thematic 散叙,
> 丢了 personality tour. Codify 此节让未来所有 composition.md 默认产 §2.5,
> character render skill 直接消费.

每盘 composition.md **必须**产 §2.5 Per-Planet Portrait 段 (即使该盘不渲染
character topic, 也产, 避免后置渲染时缺 source). 8 行 + 1 optional 收束行,
按以下表格 schema 输出:

```markdown
## §2.5 Per-Planet Portrait

每行代表 reader/01-character.md 一段渲染 source. 段标题 reader-facing 中文
固定 (不可改名, render skill 直接消费), 每段 reading 行写 prose-ready 1-2 句
mouthfeel, 不写 chart-tech. Finding refs 列具体 §B finding ID, render skill
inherit 为段末 trailing.

### §2.5.1 给人的第一印象 (Asc + 1H signature)

- **Condition**: <Asc sign + Asc-lord 位置 + 状态; 1H stack 占主 if any>
- **Multi-role load**: <Asc-lord 兼任的其他 role; 1H tenant 的 multi-role>
- **在话题里出现**: 别人初见时碰到的第一面 (旁人识别该 subject 的入口)
- **Reading** (1-2 句, prose-ready, anti-cliche): <mouthfeel 描述>
- **Finding refs**: [F<NNN>, F<NNN>] / [TF-character-<NN>]

### §2.5.2 这个人的核心 (Sun)

- **Condition**: <Sun sign + house + dignity + sect + 关键 reception/aspect>
- **Multi-role load**: <Sun 兼任的 ruler/sig 角色, e.g. Asc-Lord / sect light / 父 nat-sig>
- **在话题里出现**: 身份 / 公开亮度 / 核心 vitality / 父亲那条线
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.3 感性内核 (Moon)

- **Condition**: <Moon sign + house + dignity + sect + phase + 关键 reception/aspect>
- **Multi-role load**: <Moon 兼任的 ruler/sig 角色, e.g. sect light if night / 母 nat-sig>
- **在话题里出现**: 内里感受 / 情绪默认底色 / 母亲那条线
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.4 思维和学习模式 (Mercury)

- **Condition**: <Mer sign + house + dignity + sect + 位相 (oriental/occidental) + R/D + 关键 reception/aspect>
- **Multi-role load**: <Mer 兼任的 ruler/sig 角色>
- **在话题里出现**: 心智 / 处理 / 表达 / 学习节奏
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.5 关系里的吸引力与表达方式 (Venus)

- **Condition**: <Ven sign + house + dignity + sect + 关键 reception/aspect>
- **Multi-role load**: <Ven 兼任的 ruler/sig 角色>
- **在话题里出现**: 爱 / 美 / 价值 / 关系吸引模式
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.6 行动力、脾气和冲突处理 (Mars)

- **Condition**: <Mar sign + house + dignity + sect + R/D + 关键 reception/aspect>
- **Multi-role load**: <Mar 兼任的 ruler/sig 角色>
- **在话题里出现**: drive / 火气 / 冲突模式 / 启动方式
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.7 成长、拓展和包容性 (Jupiter)

- **Condition**: <Jup sign + house + dignity + sect + 关键 reception/aspect>
- **Multi-role load**: <Jup 兼任的 ruler/sig 角色>
- **在话题里出现**: 扩张 / 信仰 / 兜底 / 整合桥功能
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.8 责任感和长期承受力 (Saturn)

- **Condition**: <Sat sign + house + dignity + sect + 关键 reception/aspect>
- **Multi-role load**: <Sat 兼任的 ruler/sig 角色>
- **在话题里出现**: 承担 / 重负 / 长期持有 / 结构性脊柱
- **Reading** (1-2 句, prose-ready): <mouthfeel>
- **Finding refs**: [F<NNN>, F<NNN>]

### §2.5.9 收束段 / 双底色 (optional)

只在 chart 有 §2 dual-flavor (primary + counter-flavor) 时才产此段; 单一主味盘
跳过, render skill 也跳过最后一段.

- **整盘双底色一句**: 接到 §2 Dominant Flavor primary + counter
- **Finding refs**: [F<NNN>, F<NNN>] (双底色 anchor findings)
```

**强制规则**:

1. **8 段 + 1 optional** 顺序固定 (Asc/1H → Sun → Moon → Mer → Ven → Mar → Jup → Sat → optional 收束), render skill 按此顺序输出, 不可重排
2. 段标题 reader-facing 中文 **固定不可改** (render skill 直接 lift 进 reader output)
3. 每段 `Reading` 字段 **必须 prose-ready** (1-2 句中文 mouthfeel, 可直接进散文), 不写 "Mars combust 4°10' applying" 这种 chart-tech (chart-tech 进 `Condition` + `Multi-role load`, render skill trailing 用)
4. 每段 `Finding refs` 至少 1 条 (从 §B 取); 若该行星该盘几乎没贡献 (e.g. averted to all + neutral condition), 仍产此段, 用 "<行星> 在该盘的角色被结构压低; 性格层显化几乎不出现" 这类 explicit-low 写法, 不可 silently omit
5. Multi-role load 必须 enumerate 完整 (用 Stage 1 T6 multi-role table 校对; 漏 role = Gate 失败)
6. §2.5.9 收束段 only when §2 has Counter-flavor; single-flavor chart 直接跳, 不写空段

**理由**:
- case-10 organic 8 段 precedent 在切到 per-topic reader/ 架构时丢失, codify 防 regression
- character render skill (hellenistic-render-unguarded/rules/topic-file-schema.md 中
  character-specific sub-schema) **依赖此节为 source**, 不再凭 render-skill 自由
  thematic 切分
- 同时把整盘性格层"逐行星过一遍"的 reader experience 保住 — 缺哪段读者立刻感知缺漏

## §3 `topic-findings/<slug>.md` 末段 — Topic Composition sub-schema

每个 topic-findings 文件在原有 "Open threads" 之后追加 "Topic Composition" 末段。
**4 个 sub-段全强制**；若该 topic 该段不适用，必须填 explicit-N/A，且 **N/A
必须 cite 具体 finding ID 或 condition 触发**，不可只写 "not relevant"：

```markdown
### N/A — <reason 一句>
该 topic 不适用此段。
- **Trigger**: <which condition fired N/A>
  e.g. "no timing-activation:* tag on any TF-* finding in this topic"
  e.g. "topic body + ethical-guard:fictional+canon → Mode + Form default N/A"
  e.g. "all findings polarity:neutral; no arc structure derivable"
- **Citing findings**: [TF-<topic>-<NN>, ...] (the findings whose absence
  of relevant tags / arc / mode justifies N/A; can be "全部 TF-<topic>-*")
  OR
- **Citing rule**: `<rule file path + §>` (e.g. `rules/fictional-subject-
  ethical-guard.md §Mode-section-suppression` if a rule-level suppression
  applies)
```

而非 silently omit 或 vague-N/A。Decision-maker 一眼可审:
1. spec compliance (4 sub-段 written / explicitly N/A'd, 无 silent gap)
2. 区分 "已思考过 + 不适用 (cited why)" vs "忘填了 (no citation)"
3. 区分 finding-state-driven N/A (citing finding IDs) vs rule-driven N/A
   (citing rule file) — 这两类未来 spec evolve 时 trace 路径不同

**Gate**: 缺少 Trigger 或 Citing findings/rule = N/A 不合规, 退回补足。

### Sub-段 1 — Type Spectrum (强制)

```markdown
## Topic Composition

### Type Spectrum

Type 数量由该 topic 的 split density 决定 (1-N; example-case career topic 大概率 
3-4 type)。每 type 用同一 schema:

- **Type A — <organizing principle ≤ 12 字>**
  - **Forms / examples**: 具体落地形态 list (≥ 3 条)
  - **Internal reframe** (一句, 反 cookbook 句式 "重点不是 X 而是 Y") [^F<NNN>]
  - **Failure mode** (一句, "如果只做 X 会 ...") [^F<NNN>]
  - **Supporting finding IDs**: [TF-<topic>-<NN>, F<NNN>]

- **Type B — <organizing principle>**
  - ...
```

Organizing principle 命名要通过 Q4 disambiguation test: 能否排除该 topic 的常 
见错误读法。命名抽象到 "成功 / 努力 / 努力工作" 这种 generic 词 = 失败。

### Sub-段 2 — Not-fit Mechanism (强制)

```markdown
### Not-fit Mechanism

- **Surface not-fits** (5-7 条 list, 从 finding 的 Not-fit field 抽):
  1. <not-fit 1> [^F<NNN>]
  2. <not-fit 2> [^F<NNN>]
  3. ...
- **Underlying mechanism name** (一句, e.g. "不能忍受没意义的苦"):
  <mechanism>
- **Why this mechanism** (一句, 说明 5-7 条 not-fits 共同 root cause):
  <说明>
```

Via negativa 的二阶动作：不只是排除 list, 是排除之后命名为何排除。

### Sub-段 3 — Development Arc (强制; N/A 允许)

```markdown
### Development Arc

(若该 topic 无 timing-activation:* finding 且无 arc-shape finding, 填 N/A)

- **Phase 1**: <what + why this phase 对该 subject 特别要紧 + cost of skipping>
  - Timing-activation refs: <e.g. zr-l1, age-band:age-0-12>
  - Supporting finding IDs [^F<NNN>]
- **Phase 2**: <抽象 → 具体 narrowing example 句式: "不是单纯 X, 而是 Y">
- **Phase 3**: ...
```

Arc 不强求 3 阶；可 2 阶 / 4 阶 / 更多, 但每阶必须自带 cost-of-skipping 字段 
(否则只是 description 不是 arc structure)。

### Sub-段 4 — Mode + Form (强制; N/A 允许)

```markdown
### Mode + Form

(若该 topic 不涉及 resource channel / 产出形态 / 主体行动 mode, 填 N/A; 
body / illness / death topic 默认 N/A)

- **Organizing mode** (一句, e.g. "能力复利"): <mode>
- **Specific forms** (≥ 3 条 list, 落地形态):
  - <form 1> [^F<NNN>]
  - <form 2>
  - ...
- **Supporting finding IDs**: [F<NNN>, F<NNN>]
```

适用 topic: career / wealth / partnership-marriage / chart-signature 优先。

## §4 Dry Martini 守门测试

类比只活在 schema 字段名 (Ingredient role enum: base spirit / modifier / 
binder / bittering / dilution / garnish) 和 role taxonomy 层；**不进 prose**。

**守门测试** (composition.md / topic Composition 段写完后强制走一遍):

> 把所有 cocktail vocab 换成占星 / 心理 / 生活语言 (base spirit → 整盘最 
> organizing 的 finding; modifier → 改向 finding; etc.), 能否无信息损失重写？

- ✓ 能 = 类比在 schema 层活着, 没占领内容 → 通过
- ✗ 不能 = 比喻在偷工 (e.g. "this chart has a juniper note") → 必须重写

**禁止出现位置**:
- `Composite image` §5
- `Internal reframe` (Type Spectrum)
- `Mouthfeel description` (Handoff)
- `Reader-facing 短描` (在 finding schema 里, 但 composition 引用时也要守)
- 任何 reader-facing answer 合成层

## §5 主味选择 4-step procedure

写 §2 Dominant Flavor 前必走:

### Step 1 — 列 candidates (不只是高频)

- 高频 chart-level findings (≥ 3 模块出现)
- 高 confidence + structural finding
- `topic:chart-signature` 模块的 TF-* findings 优先 (该模块就是 designed 
  organizer)
- 决策性 tension finding (改一动则整盘 narrative 重写)

### Step 2 — Organizing power test (核心 gate)

暂定 candidate 为主味; 测三轮:

1. 能否把 ≥ 60% chart-level findings 重新 frame 为 "它的 modifier / binder / 
   edge"？
2. 能否解释 ≥ 2 条 tension 为 "它和别的因素的张力" (而非 "它之外的张力")？
3. 能否把 ≥ 1 条 execution handoff 解释为 "它的 routing 决定的"？

三轮全过 = 真主味 (dominant); 仅过 1 = prominent 但非 dominant。

### Step 3 — Disambiguation test

主味命名要能排除该 chart type 的常见错误读法。
- e.g. example-case "recognition without contact" 能排除 "withdrawn / isolated / 
  introverted" 等错误读法。
- 不能排除 = 主味太抽象, 没切到这盘特有的东西, 重命名。

**特例 — fictional+canon-marked subject** (per `rules/fictional-subject-
ethical-guard.md`; e.g. [example case]):

- Disambiguation baseline **必须**用 **chart-structural baseline**, **禁止**
  用 canon character baseline 作 disambiguation 对照
- 错误做法: "X 主味能排除 [fictional-subject] canon 的 'pure-luck-passive' 读法" → 这
  把 canon 当 ground truth, 反 chart-baseline first 的纪律
- 正确做法: "X 主味能排除该 night-chart + Saturn-angular-contrary-sect +
  43%-aversion-density 结构常见的 'paralyzed' / 'fatalistic' 等错误读法"
  → 用 chart 结构 archetype 作 disambiguation 对照
- Canon 共振 (e.g. "X 主味与 [fictional-subject] 'absolute hope through despair' 弧
  resonant") 写入 §6 do-not-flatten 的 **canon-resonance flag** 段, 显式
  标 `[canon-resonance, NOT predictive, NOT disambiguation baseline]`
- 理由: example-case retro 风险: fictional+canon subject 会自然 drift 成 "用
  canon 描述 chart", 这违反 chart-first + character-symbolic-only 双纪律。
  Disambiguation baseline 走 structural 是最强的反 drift gate

### Step 4 — Counter-flavor stress test

反方向选另一 candidate 走 Step 2:
- 反方向也过 ≥ 60% organizing power → split-mandate chart
- 直接在 §2 命名 "primary flavor: X with structural counter-flavor: Y" 
  (复合主味, per practitioner anchor 2026-05-17)
- 反方向只过 < 30% → 单一主味 confirmed

记录 §7 `Counter-flavor stress test outcome`: single-flavor | dual-flavor | 
undefinable。undefinable 状态 (反方向也接近 60% 但本来选的也只勉强 60%) 
要求 composition confidence 降到 low + 在 §6 do-not-flatten 显式标注。

## §6 Tension mechanism taxonomy

Starter set 9 类 (extensible; case-09+ 新出现的 mechanism 在此 extend, 
未来可拆出 `rules/tension-mechanism-taxonomy.md` 单独维护):

| # | Mechanism type | 触发条件 | example-case 例 |
|---|---|---|---|
| 1 | **dignity-vs-sect** | 行星 own dignity + contrary-sect | Saturn own-exalt + contrary-sect |
| 2 | **reception-vs-aspect-channel** | mutual / one-way reception + aversion | Venus-Jupiter mutual + aversion |
| 3 | **load-vs-position** | T6 多角色 / 多 hosting + 宫位弱 / cadent / 12H | Mars 12H + 3-tier Mercury hosting |
| 4 | **visibility-vs-condition** | angular / 主 sig + condition 扭 (debility / contrary-sect) | Saturn 1st + contrary-sect malefic |
| 5 | **promise-vs-execution** | 宫内 sig 与 ruler-handoff verdict 不一致 | (example-case 多处, e.g. 10H promise vs Moon-ruler condition) |
| 6 | **tenant-vs-ruler-quality** | in-house good + manager bad (或反) | `[TBD-example-case-3B]` |
| 7 | **multi-ruler-split** | chart-lord 五票 / topic-lord 多票分裂 | example-case chart-lord TF-02 (Venus / Saturn / Mars 三选) |
| 8 | **inner-vs-outer-projection** | 1H/2H/3H 密 + 9H/10H/11H 空 | example-case TF-07 outer-projection axis 空 |
| 9 | **active-vs-latent-channel** | 双 mutual reception 一动一静 | example-case TF-06 Moon-Mars sextile + Venus-Jupiter aversion |

每条 §3 tension entry 必须指明 mechanism type (从此 taxonomy 选); 若该 
chart 出现 taxonomy 未列的新 mechanism, 加入 taxonomy + 标 "first seen: 
case-NN, YYYY-MM-DD"。

**Example completeness marker** (per row "example-case 例" column):
- 有具体 finding ref / 描述 = stub 阶段已识别该 chart 的实例
- `[TBD-example-case-3B]` = stub 起草时此 mechanism 尚未在 example-case finding pool
  中匹配到具体实例; 待 example-case Stage 3B 实做时再填入; 若 3B 跑完仍未匹配,
  改写为 `[no example-case instance; first-seen pending case-NN+]`
- `—` (em-dash) = **禁用**; 历史 stub 用 — 表示"暂缺", 但模糊性导致 spec
  reader 误以为该 mechanism 不存在; v2.3 起替换为 `[TBD-case-NN-3B]` 形式

## §7 Handoff verdict closed taxonomy

§4 Execution Handoffs 用 closed 7-项 verdict enum:

| Verdict | 判定条件 |
|---|---|
| **顺流** | manager well-placed + 与 tenant 有 aspect channel + 与 topic 别的 sig 不冲突 |
| **错位** | manager 在与 topic 性质不符 place / sect 错 / 主题与 manager 自然性不匹 |
| **绕路** | manager 与 tenant aspect 缺 + 有 reception → back-channel |
| **降速** | manager retrograde / under-beams / stationary / 主动失能 |
| **技术化** | manager hosted by craft planets (Mercury-stack / Saturn-stack / 多 tier hosting) — 执行可走但要求技术化 |
| **间接化** | mutual reception in aversion → 互识不互见 |
| **卡住** | manager detriment / fall + averse to tenant + no reception |

**复合 verdict precedence rule** (强制, 非 permissive):

- 若多个 verdict 条件同时成立, **必须**复合列出 (e.g. "降速+技术化+绕路" 全
  列), **禁止**单选最 dominant 一项 mask 其他
- Verdict 排列顺序按 §7 表行号 ascending (顺流 → 错位 → 绕路 → 降速 →
  技术化 → 间接化 → 卡住), 不按"感觉哪个最重要"
- 例 example-case partnership handoff: Venus-Jupiter mutual reception in aversion
  ⇒ "间接化"; 同时 Jupiter detriment 在 7H ruler 路径 ⇒ "卡住"; 同时
  Jupiter at 1° MOON-exalt degree → 技术化 (Moon-mediated execution). 必须
  写 "技术化+间接化+卡住" 全列, 不可只写最显眼的 "间接化"
- 单 verdict 输出 = 多条件 collapsed → Gate 失败, 退回重测每条件是否成立

**理由**: example-case retro 显示, executor 倾向写最 "dramatic" 单 verdict (e.g.
"卡住"), masking 实际 mouthfeel 的 "卡住 by 绕路 by 间接化" 多层结构。强制
复合切断这种 simplification drift。

可审性: 每 verdict 必须列 finding refs + Stage 1 row_id 回链; 同 procedure 
走两遍 verdict 应一致 (reproducibility gate)。复合 verdict 各条件独立可审。

## §8 Per-sentence audit hook 形态

Per practitioner anchor 2026-05-17: 用 **markdown 脚注 `[^F<NNN>]`**, 不用 inline 
link。理由：deliverable print 场景 link 隐藏在 hover, 脚注作为 footer text 
仍可见。

**使用规则**:

1. 每条 composition claim (organizing principle / mechanism name / phase 
   description / verdict mouthfeel / etc.) 句末挂 `[^F<NNN>]`
2. 脚注定义集中放 §7 Audit Backtrace 末尾, 格式: 
   `[^F<NNN>]: chart-finding-index.md §B F<NNN> — <short statement>`
3. 多 finding 联合支持一条 claim: 句末挂多个脚注 `[^F018] [^F022]`
4. 脚注定义按 finding ID 数字升序排列 (不按出现顺序)
5. Decision-maker 合成 reader-facing answer 时 inherit 脚注层进 reader output

**Print 场景验证**: 把 composition.md 渲染为 PDF (pandoc / markdown 
preview export), 脚注必须出现在文末 footer 区, 不可丢失。

## §9 Cross-link / 替代关系

This file **partially supersedes**:
- `rules/chart-finding-index-workflow.md` §2 step 5 "Name 整盘 patterns in 
  §D" — 整盘 patterns 不再仅以 list of finding refs 形式存在于 chart-
  finding-index.md §D; 改在 `composition.md` 以 mouthfeel + tension + 
  handoff + composite image 形态承载。chart-finding-index.md §D 可保留为 
  "高 level pattern → finding ref" 索引层 (薄), 但 mouthfeel 在 composition.md.
- `rules/topic-modules.md` §B.5 末尾的 "Composite reading" 整盘合成部分 
  (已在 v2.3 reframe 中标 SUPERSEDED; composition pass 是其 v2.3 正解)

This file **depends on**:
- `rules/chart-finding-index-workflow.md` (Stage 1/2/3A workflow)
- `rules/chart-finding-index-tags.md` v2.1 (tag inventory; composition pass 
  本身不引入新 tag, 但 §6 mechanism taxonomy + §7 verdict taxonomy 是 
  composition-internal closed enum, 不进 v2.1 inventory)
- `rules/delineation-output-rules.md` (anti-cookbook / via negativa)
- via negativa referential rule (主语必须人 / 事 / 状态)

**workflow.md update** (✓ applied 2026-05-17):
- §2 step 5 banner added (整盘 mouthfeel 移到 composition.md)
- §2 output 列加 `composition.md` 文件 (as item 2; question-index 顺移至 3)
- File structure block 加 `composition.md` + topic-findings 末段 Topic
  Composition note
- §"Architecture context" diagram 更新为 Stage 3A → Stage 3B 双段

## §10 Status

**Stub完整度**: schemas + procedures + cross-references 立住; 
example-case first end-to-end test 可参照此 stub 走 Stage 3B 实做。

**Phase 3 finalization 将加** (案 example-case 实做后 friction log):
- Concrete worked example (example-case composition.md + 1-2 topic Composition 
  段示范, 成为 `samples/composition-template.md`)
- Mechanism taxonomy 是否拆出独立 `rules/tension-mechanism-taxonomy.md` 
  (若 example-case/09/10 中出现 ≥ 5 新 mechanism type, 拆出)
- Composition 与 chart-finding-index.md §D 边界 finalize (§D 是否完全删除 
  vs 保留薄索引层)
- Per-question deliverable shape recipe library (example-case 实做 1-2 个 
  reader question 之后归纳)
- Composition pass 是否需要独立 Stage 3B audit session (analog to Stage 1 
  audit) — 现 stub 不要求, 但若实做发现 split-mandate / counter-flavor 
  test 误判率高, 加 audit gate

**workflow.md update**: ✓ applied 2026-05-17 (banner + output 列 + file 
structure block + Architecture diagram 3A/3B split).

**method-index.md update**: ✓ applied 2026-05-17 (§1A.v2.3 step 4 拆为 
Stage 3A + Stage 3B; 关键 reference list 加 `rules/composition-pass.md`; 
v2.x change watermark 追加 2026-05-17 v2.3 Stage 3B integration entry).

---

> Stub complete. example-case first end-to-end Stage 3B 实做 may proceed using 
> this spec. workflow.md + method-index.md updates pending separate trigger.
