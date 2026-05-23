# CLAUDE.md

希腊化占星 Skill Project。把希腊化/古典占星整理成 Codex skill 可用的结构化
方法论，强制 evidence-chain 工作流，杜绝 placement cookbook 式碎读。

> ## ⚠️ UNGUARDED FORK ARCHITECTURE UPDATE (2026-05-18)
>
> **本文件在 unguarded skill copy 内, 是 unguarded fork doctrine 的一部分**.
>
> **v2.3 source/reader 分层架构, reader 走 sibling skill**:
>
> - **source 层** (本 skill `hellenistic-natal-core-unguarded` + 5 sibling):
>   Stage 2 topic-findings + Stage 3 chart-finding-index. 英文 + 表格 +
>   technical citation. 不是 reader 文本.
> - **reader 层** (新 sibling `hellenistic-render-unguarded` 唯一持有):
>   中文散文 deliverable. 输出 `charts/case-NN/reader/NN-<slug>.md` 一主题
>   一文件 + 可选 HTML 合并. 含反八股全套规则.
>
> **unguarded 8-skill 家族路由**:
> - 起新 chart → `hellenistic-reader-unguarded` (Stage 1 + 验前事)
> - 跑 Stage 2/3 → 本 skill (`hellenistic-natal-core-unguarded`)
> - 写 reader 中文 → `hellenistic-render-unguarded`
> - timing 独立产出 → `hellenistic-timing-unguarded` (⚠️ DEFERRED — Stage 1
>   还没接入流年数据, 当前 inert)
> - topic deep dive (source) → `hellenistic-{family,partnership,career}-unguarded`
> - 校时 → `hellenistic-rectifier-unguarded`

## Provenance 约定

规则与数据分两类标注，混在一起会让单一来源的内容显得过度确定：

- `[Brennan Ch.X]` —— 有书面出处，保留页码引用。
- `[project heuristic]` —— 项目自定的脚手架/启发式，非蒸馏自原文。

`source-map.md` 在文件级登记来源；不确定或重构的规则标 `needs verification`。

## 引用纪律

只做释义和规则蒸馏，不抄长段受版权保护的原文，保留页码引用。

## 模块结构

- `extractions/` —— 按来源、按章节的方法蒸馏（Rule Card 格式）。
- `rules/` —— 功能性可复用规则模块；`reading-workflow.md` 是编排层，
  `delineation-output-rules.md` 是输出层，`planet-condition-audit.md` 是被
  反复调用的子程序。
- `charts/` —— 示例盘数据（已脱敏）。
