---
name: hellenistic-render-unguarded
description: "Hellenistic reader-facing 中文渲染 skill — UNGUARDED 家族. 把 topic-findings 渲染成中文散文 deliverable. 读 source 后先做 mandatory 生活判断摘要 (Step 1.5), 再按 render-checklist.md (~1500 token) 逐段写叙事, 写后过 anti-cliche-astrology.md 做文体 self-review. 4 份深度 reference (direct-relational-statement / session-learnings / terminology-register / topic-file-schema) 按需查阅. 触发: '渲染 / 写 reader / 整理给盘主看的版本'. 不触发: Stage 1/2/3 source 层."
---

> v1 (2026-05-18) — 从 hellenistic-natal-core-unguarded 抽出来的 reader 渲染
> sibling. 创建动机: cleanup, 把渲染相关散落规则 (反八股 / Direct Relational
> Statement / session 经验 / report_builder / appendix template / 占星师口吻
> 等) 集中到一个 skill, 不丢得到处都是.
>
> v1.1 (2026-05-18 PM) — context 术语污染优化. 诊断: case-09 character 段
> 系统性退回 chart-马甲, 根因是 ~60% context 是术语. 改动: (P0) 砍 composition
> + chart-finding-index 输入, 砍 F-id mandatory verify, 新增 Step 1.5 生活判断
> 摘要; (P1) 5 份 doctrine 压缩为 render-checklist.md, samples 只留正例;
> (P2) character 逐段渲染建议; (P3) report_builder dark mode. 目标: context
> 术语占比从 ~60% 降到 < 30%.
>
> v1.2 (2026-05-18 PM) — 细节损失 + 散文漂移修复. 诊断: v1.1 Step 1.5
> 每个 TF 压成一句话 → 模型拿到模糊中心意象 → 围着它写散文 → 细节丢失
> + 注意力涣散. 改动: Step 1.5 从"每 TF 一句话"改为"每 TF 列出所有可打勾
> 打叉的判断点清单"; render-checklist 加第 11 条 (判断 vs 描写);
> session-learnings 加 §11 (判断点密度 > 散文展开).
>
> v1.3 (2026-05-18 PM) — anti-cliche 占星化 + 放置位置重构. 原 anti-cliche.md
> (通用创意写作规则) 替换为 anti-cliche-astrology.md (占星 reader 场景适配).
> 关键决策: 不塞回 render-checklist (会膨胀 token), 不放 Step 2 (那时 context
> 语言锚干净), 放在 Step 3 每段写完后做文体 self-review. 内容方向已对,
> 规则做微调. 深度 reference 从 5 份减为 4 份 (anti-cliche 归档).

# Hellenistic Render — Unguarded

## 这个 skill 做什么

你拿到的输入是 chart finding（行星在哪、跟谁互容、什么时候被激活）。你的任务是把它翻成**读者能用自己生活经验验证的判断**。

读者读完应该觉得"这个人在说我的生活"——能跟自己经验对照，能当场判断准还是不准。不需要懂占星就能读懂每一句话。

**你不产 chart finding**（那是 natal-core-unguarded 的事），**你产 reader 文本**。一个 topic 一个文件，可选择性渲染，可合并 HTML。

## 合规的文章 vs 不合规的文章

**合规**——每句话都是生活判断：

> 想的多但是想不穿。学东西挑，挑到的学得深，日常琐碎的记不住做不好。逼自己做计划总坚持不过三天。
>
> 你跟父亲关系远——他不来日常贴近，关键时刻你也不会主动找他要意见。
>
> 独处的时候推不动事，对面有个人你才知道自己要往哪走。

读者不需要知道"水星在 6 室果宫"也能对照自己生活说"准"或者"不准"。

**不合规**——chart fact 换了个中文马甲：

> ❌ 想事的通路一开，"精度-平衡纠正"那条线同步启动——你的思考轴自带一条回路，碰什么就触动一次.
>
> ❌ 拿纪律绑住自己、拿规则承重的那条路在你身上到位又不到位.
>
> ❌ 从 2024 年底到 2051 年，身体、物质、生计、现实承担和慢性消耗这一线由状态最差的土星长期扛着.

这三句的问题：读者必须先在脑子里把"通路""回路""那条线""到位又不到位""土星长期扛着"翻译成具体生活场景才能判断准不准。**你替读者做这一步翻译——那是你的工作，不是读者的。**

## 最常见的失败模式

```
chart fact (水星合报应点)
  ↓
翻成中文 structural-language（"想事的通路一开，精度-平衡纠正那条线同步启动"）
  ↓
交稿 ← 这里错了
```

正确的过程多一步：

```
chart fact (水星合报应点)
  ↓
停下来想：这个配置在这个人生活里具体是什么样子的？
  ↓
写生活判断（"想的多但是想不穿"）
  ↓
交稿
```

**每写完一句话，问自己：读者不懂占星的话，这句话她能用自己的生活经验说"准"或者"不准"吗？** 如果不能，你写的是 structural-language，重写。

## 技术依据怎么放

chart-tech 全部放在每个文件底部的"技术依据" trailing block 里。那个部分是 audit trail——给懂占星的人回查用的，用第一层固定中文译名（per `rules/terminology-register.md`），可以保留术语。读者可以跳过。

叙事段和技术依据之间的关系：叙事段说"想的多但是想不穿"，技术依据说"水星 Ari 10°53' 6H 果宫逆派 + 同度合报应点 0°05'"。两层说的是同一件事，叙事段给生活判断，技术依据给 audit chain。

## 触发条件

用户显式说:
- "渲染 case-NN" / "写 reader" / "整理给盘主看的版本"
- "unguarded 渲染 X 的 family" / "渲染 case-NN 的 career" 等指定 topic
- "重写 case-NN 的 family 段"
- "把 reader-entry-portrait 重新做" / "case-NN 的 reader 版"
- "合并 HTML" (走 scripts/report_builder.py)

**不触发**:
- 跑 Stage 1 / 2 / 3 (走 `hellenistic-natal-core-unguarded` 主 skill 或
  `hellenistic-reader-unguarded` sibling)
- 写 source 层 finding (倾向英文 + 表格, 不走中文反八股规则)
- Q&A 答 (走 `hellenistic-natal-core-unguarded/rules/qa-mode.md`; 但 Q&A 答的
  narrative 子段如果较长且是中文, 应该过 render-checklist +
  anti-cliche-astrology self-review)

## Prerequisite

分两档, 按 practitioner 触发指令决定:

**A. 单 topic 渲染** (e.g., "渲染 case-NN 的 family" / "重写 family 段")

```
必需:
  → charts/case-NN/topic-findings/<指定 topic>.md
     (没有 → "该 topic 还没跑 Stage 2 finding, 先跑 natal-core-unguarded
              或对应 sibling topic skill (-family / -partnership / -career)
              拿到 source. 否则没有 source 可渲染.")

可选 (有则 read 补上下文, 没有不阻塞):
  → charts/case-NN/subject-context.md (subject 关切 / 反馈 — 只读元信息段)
  → charts/case-NN/pre-validation-R1.md (confidence ceiling)
```

**不读** (context 污染代价 > 信息收益):
- `composition.md` — 中间产物, topic-findings 是最终产物, 信息已包含
- `chart-finding-index.md` — 唯一用途是 F-id 验证, 代价太高 (per §9 revised)

**B. 全盘 / 多 topic 合并渲染** (e.g., "整理给盘主看的版本" / "合并 HTML")

```
必需:
  → 涉及的所有 topic-findings/<slug>.md
     (任一缺失 → 列出缺失文件, 让 用户决定是先补还是当前先跳过)

可选:
  → subject-context.md / pre-validation-R1.md (同上)
  → chart-finding-index.md (仅作为 topic 清单查缺, 不灌进写作 context)
```

**timing 渲染**: 暂 defer (per `hellenistic-timing-unguarded` DEFERRED banner —
Stage 1 还没接入流年数据). 接入后再补本 skill 对 timing-snapshot.md 的渲染路径.

## Doctrine reference

**日常渲染读 1 份精简 checklist** (Step 2 引用本节):

- **`rules/render-checklist.md`** (~1500 token) — 从 5 份 doctrine 压缩的纯执行指令. 叙事段 11 条 + trailing 3 条 + 禁词速查 + 中文母语速查. **每次渲染只读这一份.**

**Step 3 self-review** (每段写完后过, 不在 Step 2 读):

- **`rules/anti-cliche-astrology.md`** — 占星场景文体打磨: 禁句式 (E) / 抗重复 (F) / 句子纪律 (G) / 抗短句 (H) / 别不是而是 (I). 先过 render-checklist 管内容, 再过这份管文体.

**深度 reference** (首次 onboard / 规则 rationale 回查 / 具体 edge case 时按需查阅, 不灌进日常渲染 context):

1. `rules/session-learnings.md` — 11 条实战经验 + 来源
2. `rules/direct-relational-statement.md` — 5 类 register + body/death 模板 + 时间括号
3. `rules/terminology-register.md` — 三层术语表 + 完整译名
4. `rules/topic-file-schema.md` — 文件结构 + character per-planet 8 段 override

## 工作流

### Step 1 — 读 source

只读一类文件: `topic-findings/<指定 slug>.md`

重点看每个 TF 条目的:
- Statement 最后一句（通常是生活判断方向的总结）
- Brief shot 类型库（已经是接近生活场景的描述）
- Reader-facing 短描（一句话）

trailing 技术依据从同一个文件的 Audit refs 里取。

**不读**: composition.md / chart-finding-index.md (per Prerequisite "不读"节)

- **档 A (单 topic)**: read `topic-findings/<指定 slug>.md` 全.
- **档 B (全盘 / 多 topic)**: 一次性 read 涉及的所有 `topic-findings/<slug>.md`.

### Step 1.5 — 生活判断摘要（mandatory，不可跳过）

读完 topic-findings 后，**在写任何叙事之前**，先输出一份摘要:

```
---
生活判断摘要 — case-NN <topic>

TF-01:
- [判断点 1 — 一个不懂占星的人能直接说准或不准的具体判断]
- [判断点 2]
- [判断点 3]
...

TF-02:
- [判断点 1]
- [判断点 2]
...
---
```

每个 TF 列出它包含的**所有可验证判断点**。source 里每一个独立的
chart fact / dignity / reception / timing 配置，如果能翻成一个
读者可以打勾或打叉的生活判断，就单列一条。

标准:
- 每条判断点必须是具体的，读者能说"准"或"不准"
- 不是对一种感觉的描写（"像背景音乐"），是可验证的事实（"要认出
  自己在感受什么，通常得靠旁人点一句或事后回放"）
- **不丢维度**：一个 TF 如果包含 4 个独立信息，就列 4 条，不压成 1 句

示例（TF-06 金星四层尊贵 + 金木互容 + 宿主链终点 + 灵点）:

```
TF-06:
- 不管前面怎么压，这个人不会真的散架，兜底的根在后方不在台面上
- 对美的判断力天生靠谱，不需要学不需要确认，别人犹豫时你已经知道了
- 审美直觉和信仰/意义感是互相喂养的，不是分开的两件事
- 不管发生什么事最后都会绕回来落到意义/信仰/创造这个域里
- "我主动想要什么"的开关在审美和价值感手里，不是在野心或恐惧手里
```

如果写不出具体判断点 → 这个 finding 你还没真正理解，回去重读 brief shot 类型库。

**这份摘要是后续写叙事的真正 source**。叙事段逐条展开这些判断点，
不围绕一个中心意象写散文。原始 topic-findings 只在写 trailing 技术依据时回看。

### Step 2 — 读 render-checklist.md

read `rules/render-checklist.md` (~1500 token, 纯执行指令).

首次 onboard 或遇到 edge case 时按需查阅 5 份深度 reference (per Doctrine reference 节), 日常渲染不灌进 context.

### Step 3 — 按 topic-file-schema 写每个 topic 文件

per `rules/topic-file-schema.md`:

```
charts/case-NN/reader/NN-<slug>.md
```

每个文件:
- 总结句 (1-2 句生活体感 distill)
- 2-4 段 narrative (按 topic 自然 dimension 拆)
- 可选子段 (reader-facing 小标题)
- 可选 nuance 收尾 (单句)
- 技术依据 trailing block

每段前看 render-checklist 前 3 条。
每段前写 `<!-- 生活判断: ______ -->`（从 Step 1.5 摘要取，可含多条判断点）。
叙事逐条展开摘要里的判断点，不围绕一个中心意象写散文。chart-tech 全塞段末 trailing。

**character topic 专项**: 固定 8+1 段 per-planet 结构 (per topic-file-schema character override). 多轮环境建议拆成逐段独立渲染 (per topic-file-schema 逐段渲染建议).

**每段写完后 self-review (两层)**:
1. 过 render-checklist 11 条（内容层: 准不准 / chart-tech 下沉 / 判断 vs 描写...）
2. 过 `rules/anti-cliche-astrology.md` E/F/G/H/I（文体层: 禁句式 / 抗重复 / 句子纪律 / 抗短句 / 别不是而是）
3. 有问题当场改, 不累积到全文写完

anti-cliche-astrology **不在 Step 2 读**——Step 2 时 Step 1.5 的生活判断摘要刚写完, context 语言锚是干净的, 不需要文体规则干扰. 文体打磨在叙事落地后做, 顺水推舟.

**每写完一个 topic 文件, 进度报告**:
```
=== reader/NN-<slug>.md 写完 ===
字数: N 字 narrative + M 字 trailing technical
applied: render-checklist 11 条 + anti-cliche-astrology self-review
```

### Step 4 — (optional) HTML 合并

只在 用户显式要求 "合并 HTML" 时跑:

```
python scripts/report_builder.py charts/case-NN [--include character,family,...] [--name <subject>] [--asc <sign degree>]
```

输出: `charts/case-NN/report.html`

### Step 5 — done

```
=== 渲染完成 ===
已写文件: charts/case-NN/reader/01-character.md (N 字), reader/05-family.md (M 字), ...
HTML: charts/case-NN/report.html (如跑了 report_builder)
下一步: 给用户 看 / 收反馈 / 必要时重写某 topic
```

## checklist 分层

**写之前** (Step 2) — 过 `rules/render-checklist.md`:
- 叙事段 11 条 (准不准测试 / chart-tech 下沉 / 禁句式 / 禁词 / 时间括号 / 收尾 / 判断 vs 描写等)
- trailing 3 条 (audit refs / 固定译名 / anchor optional)
- 禁词速查 + 中文母语速查

**写之后** (Step 3 self-review) — 过 `rules/anti-cliche-astrology.md`:
- E: 禁刚性句式 (不是而是 / 解释尾巴 / 假对立 / 排比列举)
- F: 抗重复 (同 chart fact 换说法 / 段落模板化 / 跨段短语复用)
- G: 句子纪律 (每句做工 / 不堆砌 / 因果链清晰)
- H: 抗短句碎片化
- I: 别不是而是了 (最高优先级全文搜)

## Samples (reference 案例)

`samples/` 下:

- **`case-14-multi-topic-OK.md`** (**唯一 active 正例**) — 4 段节选 (body / friends / family / career), 每段附 subject 真实反馈 + "为什么这段好" 分析. Subject 原话: "ChatGPT 不太讲人话, 但你这个就特别讲人话, 就听一听就懂." 这是"讲人话"目标的最佳验证样本. 写新 topic 前扫一眼.

(旧正例 `case-10-family-v4-OK.md` 已归档到 `samples/archived/`——case-10 当时是 "acceptable", case-14 是 "比真人占星师还详细 + 特别讲人话", 标尺已升级. v0 反例同在 archived/, 不读.)

## 跟其他 unguarded skill 的关系

| Skill | 角色 |
|---|---|
| `hellenistic-reader-unguarded` | Stage 1 数据 + 验前事 (输入层) |
| `hellenistic-natal-core-unguarded` | Stage 2/3 source finding + chart-finding-index (中间层) |
| **`hellenistic-render-unguarded` (本 skill)** | reader 层中文散文渲染 (输出层) |
| `hellenistic-timing-unguarded` | timing 技法独立产出 (可作为 render 输入或单独跑) |
| `hellenistic-partnership / -career / -family / -rectifier` | sibling topic deep dive (Stage 2 替代路径) |

工作流标准链:
```
reader (Stage 1) → natal-core (Stage 2/3) → render (中文 deliverable) → (可选 HTML)
```

## 输出语言

- 默认中文 (practitioner 主要场景)
- 如 practitioner 要英文 reader 输出: 仅 read `direct-relational-statement.md` 的 5 类 register
  + body/death/longevity 模板 + 时间括号"为什么"; **跳过 anti-cliche-astrology.md**
  (那是中文文体打磨, 英文不适用)
- 中英混用: 主体语言一致, 术语可保留另一语言 + 当场翻译
