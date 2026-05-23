# Topic-File Schema — 一主题一文件 + HTML 合并 (仿参考体系)

> 2026-05-18 设计. 仿 parallel-core-skill p2a/p2b/p2c_planets.md + p3_divisional.md +
> p4_houses.md + p5a/p5b_life.md + appendix.md 的分文件模式. 每个 reader topic
> 独立 .md 文件, scripts/report_builder.py 输出 HTML 时合并.

---

## 路径与命名

### 文件路径

```
charts/case-NN/
├── topic-findings/       # source 层 (Stage 2 finding, 已存在)
│   ├── character.md
│   ├── career.md
│   ├── family.md
│   └── ...
├── chart-finding-index.md  # source 层 Stage 3 (已存在)
├── reader/                  # ← reader 层 (本 skill 输出, 新增)
│   ├── 01-character.md
│   ├── 02-career.md
│   ├── 03-wealth.md
│   ├── 04-partnership-marriage.md
│   ├── 05-family.md
│   ├── 06-learning.md
│   ├── 07-divination-spirituality.md
│   ├── 08-body.md
│   ├── 09-children.md         # 仅当跑了该 topic
│   ├── 10-siblings.md         # 仅当跑了该 topic
│   ├── 11-friends-benefactors.md
│   ├── 12-illness.md
│   ├── 13-death.md            # 仅当 用户显式要求
│   ├── 14-longevity.md        # 仅当 用户显式要求
│   ├── 15-chart-signature.md
│   ├── 16-timing.md           # 时机层汇总
│   ├── 00-overview.md         # 整盘开场 + 双底色 + mouthfeel 一句
│   └── 99-citation.md         # 整盘 trailing technical 依据 (可选, 也可分散到各 topic 文件底部)
└── report.html              # report_builder.py 输出
```

### 命名规则

- **数字前缀**: 2 位数字 `NN-` 用于 HTML 合并时排序 (跟参考体系 p2a/p2b/p2c 排序逻辑一致)
- **slug 跟 source 一致**: `family.md` 对 `topic-findings/family.md`, 1:1 mapping
- **数字 = 输出顺序** (不是 topic-findings 抽取顺序). 默认顺序: overview → character → career → wealth → partnership-marriage → family → learning → spirituality → body → children → siblings → friends-benefactors → illness → death → longevity → chart-signature → timing → citation
- **可缺**: 任何一个 topic 没产出就缺号 (跳过即可, report_builder 不会报错)
- **可加自定义 topic**: 比如 `20-synastry-with-XX.md`, `21-transit-snapshot-YYYY.md` 等, 数字 ≥ 20 留给非标准 topic

---

## 每个 topic 文件的 schema

```markdown
# <topic 中文名> — case-NN (subject)

> source: topic-findings/<slug>.md
> 渲染 discipline: render-checklist.md (v1.1+)
> 触发: 2026-MM-DD by <invocation context>

---

**[总结句 — 1-2 句生活体感 distill, 不含 chart 拟人]**

[2-4 段 narrative — 按本 topic 自然的 dimension 拆分. 每段:
- 直接陈述
- 5 类 register 之一 (relational / event / behavioral / material-life / identity-role)
- 重要 claim 带括号 plain-language "为什么"
- 不八股 (按 render-checklist + anti-cliche-astrology.md self-review)
- 不 chart-factor 拟人 (per session-learnings.md #1)
- 时间节点带括号 (per direct-relational-statement.md)]

---

### <可选子段 1 — reader-facing 小标题, 不用 chart-tech>

[内容]

### <可选子段 2>

[内容]

---

## 整体收尾 (optional)

[1 句话 nuance 收口. 不复述, 不"用得好/用过头", 不"读懂...就顺盘". 单句完事.]

---

## 技术依据

[全部 chart-tech / finding-id / Stage 1 row_id 链 / source citation 集中
trailing block. 仅本 topic 用到的部分, 不复制整盘 stage1 数据.]

引用 source finding: TF-<topic>-XX 到 YY + D-NN ...
chart facts: <planet> in <sign> <degree> <house> + <key reception/aspect> + ...

cross-topic anchor (optional): F<NNN> (description) · F<NNN> (description) · ...
   [F-id 从 topic-findings 的 "Lifts to chart-level F<NNN>" 行取.
    如果 topic-findings 写的是 "TBD-Stage-3", 不写 anchor, 宁缺勿错.
    详见 session-learnings.md §9 (revised).]
```

---

## Character topic — 强制 per-planet 8 段 sub-schema (override)

> Added 2026-05-18 (practitioner anchor): case-10 `reader-entry-portrait.md` 性格 section
> 是 canonical precedent — 整盘从性格角度逐行星过一遍. case-12 + case-09 第一轮
> render 默认走通用 schema "2-4 段按 dimension 拆", regression 到 thematic 散叙,
> 丢了 personality tour 完整性. 此 sub-schema **覆盖通用 schema**, character topic
> 必走 per-planet 8 段.

### 强制结构

`reader/01-character.md` **必须**用 per-planet 8 段固定结构, 不可走通用 2-4 段
thematic 切分. 段标题 reader-facing 中文 **固定不可改** (固定标题表,
原 lift 自 composition.md §2.5, 现为常量不需回查):

```
### 给人的第一印象          (Asc + 1H signature 段)
### 这个人的核心            (Sun 段)
### 感性内核                (Moon 段)
### 思维和学习模式          (Mercury 段)
### 关系里的吸引力与表达方式 (Venus 段)
### 行动力、脾气和冲突处理   (Mars 段)
### 成长、拓展和包容性       (Jupiter 段)
### 责任感和长期承受力       (Saturn 段)
### 收束段 (双底色)          (optional, 只在 composition §2 有 dual-flavor 时产)
```

### 每段内容来源 + 写法

- **Source**: `topic-findings/character.md` 对应行星的 TF 条目（重点看 Statement 末句 + brief shot 类型库 + reader-facing 短描）

- **每段开写前 mandatory**: 先写 `<!-- 生活判断: ______ -->`（per session-learnings §10+§11）。从 Step 1.5 摘要取该行星对应的判断点，可含多条。叙事逐条展开这些判断点。示范：

  ```markdown
  ### 思维和学习模式

  <!-- 生活判断: 想的多但是想不穿；学东西挑，挑到的学得深，日常琐碎的记不住；逼自己做计划总坚持不过三天 -->

  [叙事逐条展开上面的判断点，不飘回 chart structural-language]
  ```

- **每段格式**: 1-3 段散文 (~150-300 字) + 段末 inline **技术依据** trailing
  (而非全文集中末尾)
- **段末 trailing 格式** (per case-10 canonical pattern):

  ```markdown
  技术依据: <chart facts: planet sign degree house + key dignity + sect + reception/aspect>;
  <multi-role load enumeration>; <Stage 2 finding refs: TF-character-<NN> / F<NNN>>。
  ```

- 每段散文符合 render-checklist 11 条, 但**字数 cap 提高**到
  800-1500 字 narrative (8 段 × ~200 字 + 1 收束段), 不受通用 800 字硬上限约束
- topic-findings 对应行星 TF 的 brief shot 类型库 + reader-facing 短描是骨架,
  render 时 expand 到 1-3 段; 不 verbatim copy
- chart-tech 严守 trailing 不 inline (per session-learnings.md #3); trailing
  是 per-段 inline 在段末, 不是全文末尾一个大块

### 覆盖通用 schema 的明确点

| 字段 | 通用 schema | character override |
|---|---|---|
| 段数 | 2-4 按 dimension 拆 | **固定 8 + 1 optional** |
| 段标题 | reader-facing 自由命名 | **固定中文 (Asc/Sun/Moon/Mer/Ven/Mar/Jup/Sat)** |
| 字数 | 长 topic 500-1000 字 | **800-1500 字 narrative** |
| trailing | 全文末一个集中 block | **per-段 inline 段末** (case-10 canonical pattern) |
| dimension 划分 | thematic (e.g. "公开表达 / 内里感受 / 关系节奏") | **per-planet** (一颗行星一段) |

### 逐段渲染建议 (P2, 2026-05-18)

8 段一次写完时 cognitive load 最高——模型要同时保持 8 颗行星的 source 理解 + 写作规则 + 前几段已写内容。建议：

**多轮环境（Claude Code 等）**：8 段拆成 8 次独立调用。每次只读当前行星对应的 1-2 个 TF 条目 + render-checklist + 前一段最后两句（保持衔接）。写完一段清一次 context。

**单次 chat**：在 Step 1.5 生活判断摘要之后，按行星顺序逐段写，每段之前重新看一眼 render-checklist 前 3 条。

### Source 缺失处理

- 若 `topic-findings/character.md` 缺对应行星的 TF 条目: **退回 Stage 2**,
  由 natal-core 先补, 不在 render skill 里现编
- 若某行星 TF 条目写 "<行星>该盘角色被结构压低; 性格层几乎不出现":
  render skill 仍输出该段, 用更短 (~80-120 字) explicit-low 写法说明"该行星
  在这个人身上几乎不显化, 是结构事实, 不是缺失", 不可 silently 删段

### 收束段触发条件

- topic-findings/character.md 的 TF 条目集合显示明显双主味对冲
  (如: 最重行星是最弱行星 + 另一颗有多层尊贵; 或 TF 里有显式
  dual-flavor / counter-flavor 标记) → render `### 收束段`
- 单一主味 (无对冲信号) → 跳过, 文件以 Saturn 段结束 (不留空 header)
- 如果不确定 → 问用户

### 字数下限

每段不少于 80 字 narrative (Asc/1H 段 + Saturn 段允许长到 350 字, 其他段
~200 字); 短于 80 字说明 source `Reading` 字段没 expand, 退回重写.

---

## 每个文件长度建议

- **短 topic** (siblings / friends-benefactors / 没特殊配置的): 100-200 字
- **中 topic** (career / partnership / family / wealth): 300-600 字
- **长 topic** (character / chart-signature): 500-1000 字
- **overview**: 200-400 字 (整盘开场 + 双底色 + mouthfeel)
- **timing**: 视 timing 技法启用数, 300-800 字

单文件硬上限 **800 字 narrative + 技术依据另算**, 超了说明分得不够细, 应该拆子 topic 或者裁掉重复.

(参考体系每板块 ≥300 字, 是 source+reader 一体的字数; 希腊化 reader 层是 source-derived narrative, 比参考体系板块短.)

---

## 跟 source 层的关系

| Source 层 | Reader 层 (本 skill) |
|---|---|
| `topic-findings/family.md` (TF-family-01 到 07 + Pressure/Mitigation/Channel + Brief shots + audit refs + Hellenistic basis) | `reader/05-family.md` (一句话 distill + 4 段 reader narrative + 技术依据 trailing) |
| 倾向英文 + 表格 + finding-id schema | 倾向中文散文 + reader-facing 小标题 + trailing citation |
| 写给 decision-maker query by tag | 写给读者/盘主直接看 |
| 不应用反八股 / direct-relational-statement (英文+表格) | 必须过 render-checklist (写前) + anti-cliche-astrology self-review (写后) |
| 一次跑出来不重写 | 同 source 可重渲染多次, 调风格 / 收 用户反馈 / 迭代 |

---

## 工作流

```
Stage 1 (hellenistic-reader-unguarded): chart-stage1.md + audit + pre-validation
        ↓
Stage 2 (hellenistic-natal-core-unguarded): topic-findings/*.md (source)
        ↓
Stage 3 (hellenistic-natal-core-unguarded): chart-finding-index.md (source 汇总)
        ↓
本 skill (hellenistic-render-unguarded):
    1. 只读 topic-findings/*.md (不读 composition / chart-finding-index)
    1.5. 生活判断摘要 (mandatory) — 每个 TF 列出所有可验证判断点
    2. 读 render-checklist.md (~1500 token 精简执行指令)
    3. 按本 topic-file-schema, 一个 topic 一个文件, 写 reader/NN-<slug>.md
    4. (optional) scripts/report_builder.py 合并 HTML
```

---

## 部分渲染

支持选择性渲染 (不必每次跑全 15 topic):

- "只渲染 family + character" → 只写 `reader/01-character.md` + `reader/05-family.md`
- "渲染除 death/longevity 之外的全部" → 跳过 13/14
- "重写 family" → 覆盖 `reader/05-family.md`, 其他不动

每次渲染都是独立 session, 触发 `render-checklist.md` read (深度 reference 按需).

---

## report_builder.py 合并 HTML

`scripts/report_builder.py charts/case-NN [--include character,family,...] [--name <subject>] [--asc <sign degree>]`

合并逻辑:
- 扫 `reader/` 下所有 `NN-*.md` 文件, 按数字前缀排序
- `--include` 不指定就全合并; 指定就只合并选定的
- 每个 .md → HTML section, 内嵌 CSS, mobile-friendly
- TOC 自动生成
- 整盘 trailing block (`99-citation.md` 如存在) 放最后

输出: `charts/case-NN/report.html` (单文件, 无外部依赖, 可直接分享)
