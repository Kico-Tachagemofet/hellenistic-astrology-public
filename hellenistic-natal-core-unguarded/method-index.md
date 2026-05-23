# Method Index — 希腊化占星 Project

> ## ⚠️ UNGUARDED FORK OVERRIDE (2026-05-18)
>
> Method routing graph identical to guarded variant. Any reference to
> ethical-guard checkpoints / extension-topic gating / canon-resonance
> auto-downgrade in this index is **NO-OP** in this fork. See
> `SKILL.md` "What this fork removes" for the override scope.

---

> 项目根入口。新人 / new session 进项目时第一份要看的文件（在 AGENTS.md +
> STATUS.md 之后、具体工作 plan 之前）。
>
> **形式**：「想做 X，走 Y 文件 + Z 顺序」。不是教程，是 navigation map。
>
> Last v2.x change: 2026-05-16 (v2.2 Plan A.4) — added §1A.v2.2 (stage-based v2.2 architecture workflow). Existing §1A v1 single-session workflow preserved.
>
> Last v2.x change: 2026-05-16 (v2.2 closing housekeeping mega batch Plan A.5 + B.8 + C.6) — §5 module structure tree updated with v2.2 new files (rules/stage1-data-extraction.md / rules/topic-modules.md / rules/brief-shot-discipline.md / handoff-templates/v2.2-stage-handoffs.md / samples/brief-shot-catalog.md / v2.2-stage1-reception-audit-report.md / v2.2-*-plan.md ×3); sibling skills cross-link added (§1B / §1C → prose-normalizer + translation-layer SKILL.md "what next" specs per B.6.4); project-level 语言 convention sticky hoist landed in AGENTS.md §"语言 Convention (v2.2 architecture)" (this file references it; full statement lives there). Additive only; existing §1A v1 workflow + §1A.v2.2 + §2-§7 unchanged.
>
> Last v2.x change: 2026-05-17 (v2.3 Stage 3B integration) — §1A.v2.3 step 4
> 拆为 Stage 3A (chart-finding-index registry) + Stage 3B (composition pass);
> 引用 `rules/composition-pass.md` 为 Stage 3B 权威 spec; 输出形态描述加
> composition.md 双件 (registry + mouthfeel)。Additive only; existing §1A v1
> + §1A.v2.2 + §1A.v2.3 step 1-3 + §2-§7 unchanged.

---

## 0. 项目入口（任何 session 起手）

读取顺序：

1. **`AGENTS.md`** — 项目 SOPs（v1 修改协议 / provenance / 决策日志 /
   audit checklist / 术语等同）
2. **`STATUS.md`** — 当前阶段 + 磁盘实际状态 + 当前任务（顶部「最后更新」
   行 = 项目层 absolute latest snapshot）
3. **`method-index.md`**（本文件） — 按任务类型导航到具体文件 +
   workflow 路径
4. **`pending-verifications.md`** — 中央 verification queue（按需查）
5. 具体任务相关的 plan / case 文件

---

## 1. 任务类型 → workflow / 文件路径

### 1A — 跑一份 natal case reading

**Workflow 顺序**（按 reading-workflow.md step 0-7）：

| step | 文件 | 用途 |
|---|---|---|
| 0 | `rules/reading-workflow.md` | 编排层：硬门禁 + ledger 结构 |
| 1 | `rules/significator-hierarchy.md` | focus 行 + roster + Same-Planet Multi-Role |
| 2 | `rules/dignities-reference.md` | domicile / exaltation / triplicity / bound / decan 确定性表 |
| 3 | `rules/planet-condition-audit.md` | 每星 audit subroutine |
| 4 | `rules/aspect-reception-rules.md` | testimony + aversion + reception |
| 5 | `rules/house-topic-framework.md` | topic chain via WSH |
| 6 | `rules/lots-and-fortune.md` | Lots（若 focus 需要 Lots run） |
| 7 | `rules/timing-techniques.md` | timing（若 focus 需要 timing run） |
| 8 | `rules/delineation-output-rules.md` | 输出层 + Prose Gate + confidence 四档 |

**参考**：
- `extractions/brennan-hellenistic-astrology/` — Brennan baseline
- `rules/cross-source-method-comparison.md` — **reference companion，不进
  workflow**；v1 与其他三源差异时查
- `pending-verifications.md` — 知道哪些 verification 排队中

**输出**：
- 主 case：`cases/case-NN-<subject>-<focus>.md`（A.0 Ledger + A.1 Reading
  + B Friction Log + C 对照）
- 可选 reader 渲染（v2.3 unguarded fork）：`charts/case-NN/reader/NN-<slug>.md`
  per topic — 走 `hellenistic-render-unguarded` sibling (用户显式触发, 不
  自动 dispatch). 原本写 "可选 sibling: `cases/case-NN-TL.md` (translation-
  layer 处理过的读者向)" 已 SUPERSEDED — TL pass 弃用, 详 §1C banner.

**范例**：
- `cases/case-04.md`（昼盘 / character / 完整 case）
- `cases/case-05.md`（夜盘 / divinatory / 双 anchor）

### 1A.v2.2 — 跑 stage 化 natal reading (new architecture) [DEPRECATED — superseded by §1A.v2.3]

> **⚠️ DEPRECATED 2026-05-17 (v2.3 reframe)** — 整段 superseded by §1A.v2.3.
> v2.2 narrative-form Stage 2 + 1049-行 portrait + TL pass 全 deprecated 因
> framing 错位 (md 是 source 不是 reader). 新 chart 工作走 §1A.v2.3 chart-
> finding-index 路径; reader 中文渲染走 `hellenistic-render-unguarded` (Wave 4
> SUPERSEDES 原 TL pass). 下面 Workflow 5 步保留作历史 reference, 不要按
> 它 dispatch 新 session.

适用：新 v2.2 stage-based architecture readings；多 topic 覆盖；user 通过
SKILL.md menu 选 mode (a) single / (b) multi / (c) full portrait / (d) custom。

**Workflow**：

1. **Stage 1 deterministic data extraction**（single session）
   - per `rules/stage1-data-extraction.md` 6 表 + 12 步 procedure + 4 gates
   - 产出 `chart-NN-stage1.md`
2. **Stage 1 audit**（independent session）
   - 验证 6 表 accuracy + Reception Detection + Gate 4 checkpoint
   - 产出 `chart-NN-stage1-audit.md`（pass / fail）
3. **Stage 2 topic module sessions**（one per topic, dispatch in parallel
   after audit pass）
   - per `rules/topic-modules.md` per-topic spec
   - 产出 `cases/case-NN-topic-<slug>.md` per topic
4. **Stage 3 synthesis session**（single, after all Stage 2 done）
   - per `rules/topic-modules.md` §"Stage 3 Synthesis Spec"（B.5 deliverable）
   - 产出 `cases/case-NN-portrait.md`
5. **Optional: TL sibling pass** per Stage 2 output
   - per `translation-layer/output-rules.md`（含 brief shot requirement per C.2）
   - 产出 `cases/case-NN-topic-<slug>-TL.md`

既有 §1A（v1 single-session `reading-workflow.md` step 0-7）保留 + 共存；
**§1A.v2.2 整体 deprecated 由 §1A.v2.3 取代**（见下）。

### 1A.v2.3 — 跑 v2.3 chart-finding-index natal reading (DEFAULT for new chart work)

适用：v2.3 reframe 之后所有新 chart 工作。取代 §1A.v2.2 stage-based workflow
（v2.2 narrative-form Stage 2 + 1049-行 portrait + TL × 2 + narrative-
deliverable 全 deprecated 因 framing 错位；见
`v2.3-chart-finding-index-architectural-plan.md` §1 reframe context）。

**Workflow** (per `rules/chart-finding-index-workflow.md`):

1. **Stage 1 deterministic data extraction** (single session)
   - per `rules/stage1-data-extraction.md` 6 表 + 12 步 procedure + 4 gates
   - 产出 `charts/case-NN/chart-stage1.md` (注: v2.3 charts/case-NN/ 目录结构)
2. **Stage 1 audit** (independent session)
   - 验证 6 表 accuracy + Reception Detection + Gate 4 checkpoint
   - 产出 `charts/case-NN/chart-stage1-audit.md` (pass / fail)
3. **Stage 2 finding production** (per topic, dispatch parallel after audit pass)
   - per `rules/chart-finding-index-workflow.md` §1
   - 产出 `charts/case-NN/topic-findings/<slug>.md` per topic, 按 topic-
     finding 轻 schema (NOT v2.2 800-行 narrative)
   - Slug list (per `rules/chart-finding-index-tags.md` v2.1 canonical topic dim):
     - Default 9: `character` / `career` / `partnership-marriage` / `family` /
       `learning` / `wealth` / `divination-spirituality` / `body` /
       `chart-signature`
     - Extension 6: `children` / `siblings` / `friends-benefactors` /
       `illness` / `death` / `longevity` (user-request only + ethical-guard)
4. **Stage 3A chart-finding-index registry consolidation** (single session,
   after all chosen Stage 2 modules complete)
   - per `rules/chart-finding-index-workflow.md` §2
   - 产出 `charts/case-NN/chart-finding-index.md` (主文件; §A-§D, §D 仅薄
     索引层) + `charts/case-NN/question-index.md` (utility)
5. **Stage 3B composition pass — 整盘 mouthfeel 层** (single session, after
   Stage 3A)
   - per `rules/composition-pass.md`
   - 产出 `charts/case-NN/composition.md` (chart-level 7-段 schema:
     Ingredient Register / Dominant Flavor / Tension Mechanisms / Execution
     Handoffs / Composite Image / Do-not-flatten Notes / Audit Backtrace)
   - 每个 `topic-findings/<slug>.md` 文件追加 "Topic Composition" 末段
     (4 sub-段: Type Spectrum / Not-fit Mechanism / Development Arc / Mode +
     Form; explicit-N/A 允许但必须 cite specific finding/condition)
   - 配套 closed taxonomies: §6 9-类 tension mechanism / §7 7-项 handoff
     verdict / §4 Dry Martini 守门测试 (cocktail vocab 只活在 schema 字段名,
     不进 prose)

**输出形态** (unguarded 家族 2026-05-18 update):

- **source 层** (本 skill + sibling 们): chart-finding-index.md (registry) +
  topic-findings/<slug>.md + composition.md (mouthfeel) — 决策者可直接
  query by tag combinations 自己 compose reader 答复.
- **reader 层** (新 `hellenistic-render-unguarded` sibling): 也可以 dispatch
  render skill 把 source 渲染成中文 deliverable, 一主题一文件
  (`charts/case-NN/reader/NN-<slug>.md`) + 可选 HTML 合并 (仿参考体系
  `report_builder.py`). 含反八股全套规则.

原 v2.3 "不出 reader-facing essay" 政策在 unguarded 家族下被 supersede —
reader essay 现在走 render skill (但形态是 topic-file schema, 不是 v2.2
那种 1000-行 narrative-form portrait).

**关键 reference**:
- Tag inventory: `rules/chart-finding-index-tags.md` v2.1 (canonical; v2.0 + codex v2 regression cleanup)
- Stage 2/3A workflow spec: `rules/chart-finding-index-workflow.md`
- Stage 3B composition spec: `rules/composition-pass.md`
- 完整 plan: `v2.3-chart-finding-index-architectural-plan.md`

§1A.v2.2 (旧 stage-based) 段保留作为 v2.2 historical reference，**新工作走
§1A.v2.3**。

### 1B — 跑 sibling skill: prose-normalizer (DEPRECATED v2.3)

- **触发**：A.1 reading 完成后，需中文语言规范化（compound 谓语拆解 /
  inline 英文整理 / 术语本地化）
- **入口**：`prose-normalizer/SKILL.md` + `prose-normalizer/normalization-rules.md`
- **输出**：在主案件文件加 `A.1' 规范化语言版本` 段（**不动**原 A.1）
- **不做**：重新审盘 / 新增 finding / 改 confidence / plain-language /
  multi-example
- **下一步衔接**（per B.6.4 sibling skill spec'd in SKILL.md）：归一化
  后的 A.1' 通常作为 §1C translation-layer 的输入（也可直接发布作技术中
  文版本）；详 `prose-normalizer/SKILL.md` 末段 "what next" 子段

### 1C — 跑 sibling skill: hellenistic-render-unguarded (SUPERSEDES TL pass)

> **2026-05-18 (Wave 4 routing cleanup)**: 原本本段 dispatch 到
> `translation-layer/` 走 TL pass 出 `cases/case-NN-TL.md` /
> `cases/case-NN-topic-<slug>-TL.md` / `cases/case-NN-portrait-TL.md`.
> v2.3 unguarded fork 把中文 reader 出口整段搬到 `hellenistic-render-
> unguarded` sibling, 路径改 `charts/case-NN/reader/NN-<slug>.md`. TL
> pass 本身**已弃用** (md 是 source 不是 reader; render 是唯一中文
> reader 出口). 现有 `cases/case-04-TL.md` / `case-05-TL.md` /
> `case-06-TL.md` 保留为历史 sample, 不再产新的 `*-TL.md` 文件.
> 上方 §1B (prose-normalizer DEPRECATED v2.3) body 仍 reference "§1C
> translation-layer" 是历史段, 不动 — 1B 整段已 DEPRECATED.

- **触发**：practitioner **显式** 说 "渲染 case-NN" / "写 reader" / "整理给盘主
  看的版本" / "重写 case-NN 的 family 段" / "合并 HTML" 等. **不在 Stage
  2/3 完成后自动 dispatch** — render 是 user-triggered deliverable, 不是
  pipeline 自动一环.
- **入口**：`hellenistic-render-unguarded/SKILL.md` + 4 个 rule 文件
  (session-learnings / direct-relational-statement / anti-cliche /
  topic-file-schema, 按 SKILL.md Doctrine reference 节顺序 read).
- **输出**：单 topic 一个 `charts/case-NN/reader/NN-<slug>.md` 文件;
  practitioner 要 HTML 时跑 `scripts/report_builder.py` 合并出
  `charts/case-NN/report.html`. **不再产 `cases/case-NN-TL.md` 或
  `cases/case-NN-topic-<slug>-TL.md`**.
- **范围**：按 render skill Prerequisite A/B 档判定:
  - **档 A** (单 topic): 只需 `topic-findings/<slug>.md`,
    `chart-finding-index.md` 可选.
  - **档 B** (全盘 / 多 topic 合并): 需 `chart-finding-index.md` + 全部
    涉及的 topic-findings.
- **不做**：重审盘 / 新增 finding / 改 confidence / 重新 derive — 只渲染
  现有 source. (跟原 TL pass 的 "不重审盘" 原则一致.)
- **下一步衔接**：render 输出即终态读者向 deliverable; practitioner 看 + 收反馈;
  必要时回到 source 层重跑某 topic finding (走 natal-core-unguarded 或
  对应 sibling), 再重 render. 详 `hellenistic-render-unguarded/SKILL.md`
  Step 5 "done" 段.

### 2 — 抽取新源（extraction）

**Workflow**：

| step | 内容 |
|---|---|
| 1 | 读 AGENTS.md「Provenance 约定」+「Post-Codex audit checklist」 |
| 2 | 参考 `extractions/brennan-hellenistic-astrology/` 三件套范例 |
| 3 | 建 `extractions/<source-name>/` + chapter-index.md + method-targets.md + reading-log.md |
| 4 | 每章节生成 Rule Card 格式 .md（Use when / Required data / Procedure / Guardrail / Destination） |
| 5 | 出现 cross-source flag → 走 reconciliation plan |
| 6 | 完成后更新 `rules/source-map.md` |

**范例**：v2.1 Phase A 三本并行 Codex 抽取（Dorotheus / Valens / Firmicus）—
见 `v2.1-phase-a-*-plan.md` 系列。

### 3 — 加 / 修 rule

**v1 已锁（2026-05-15）**，所有改动 **additive only**（per AGENTS.md
v1 修改协议）：

1. 起 plan：`vX.Y-<topic>-plan.md`
2. plan 走 5 步 audit
3. 落地后 + watermark（`> Last v2.x change: YYYY-MM-DD (vX.Y Phase Z) —
   added <what>. Additive only; existing rows unchanged.`）
4. 同步 `STATUS.md` + 相关 `pending-verifications.md` entry

**plan 范例**：
- `v2.1-phase-b-rule-update-plan.md`（多 sub-phase 整合 plan）
- `v2.x-case-05-rule-extension-candidates-plan.md`（case-derived 补丁 plan）

### 4 — 跑 integrated portrait（Path B）

**当前是 plan-based execution（尚未 codify 成 rules workflow）**。

**模板**：`v2.x-integrated-portrait-plan.md`

**Phase 序列**：
- Phase A — rules-side prep（新 focus 行 / roadmap 调整）
- Phase B — 新 focus 单 reading
- Phase C — 多 focus axis 系列 reading
- Phase D — timing layer（profections + ZR）
- Phase E — specialist supplements（Asc degree / fixed star / antiscia）
- Phase F — cross-axis synthesis → 最终 portrait

**TODO（待 codify）**：Phase F 跑通后 → `rules/integrated-portrait-workflow.md`

### 5 — 跑 specialist supplements

**当前 plan-based**（尚未 codify）。

**纪律**：
- Confidence: Speculative（默认）
- Provenance: `[Source-only candidate]` 标
- Frame: character-symbolic resonance，**不**作 predictive
- Out-of-scope: 不 transfer to real-person predictive use
- Ethical guard: 对 fictional figures + creative/practice framing
  attenuated；对 real-person 永久保留

**入口**：`v2.x-integrated-portrait-plan.md` Phase E
**TODO（待 codify）**：Phase E 跑通后 → `rules/specialist-supplements-protocol.md`

### 6 — close pending verification

**Workflow**：

1. 查 `pending-verifications.md` 找议题
2. 起 `vX.Y-<verification-topic>-plan.md`
3. plan 走 5 步 audit
4. 落地后 status: Open → Verified / Closed
5. **不直接改 v1**（即使发现需要改也要走 additive plan）

**范例**：
- `v2.x-case-05-rule-extension-candidates-plan.md`（pending #10 + #11
  closure plan）

### 7 — 跨 phase 项目级决策记录

**位置**（按工作类型）：

| 工作类型 | 决策日志位置 |
|---|---|
| 抽取类（per-source） | `extractions/<source>/reading-log.md` + `method-targets.md` |
| 单 plan 任务 | plan 文件末尾 inline 段（`## X.Y Results` / `## X.Z Decisions` + 每 sub-phase 完成 watermark） |
| 应用类（case 内） | case 文件 Notes 段（Normalization Notes / TL Notes / Run Record） |
| 项目级 | `STATUS.md` 顶部「最后更新」+「当前阶段」段 |

（同 AGENTS.md「决策日志约定」段）

---

## 2. Conventions

- **语言**：中英文混合 OK；技术 term 保 English；散文中文优先
- **引文**：`[Brennan Ch.X]` / `[Valens *Anth.* X.Y]` / `[Firmicus *Math.*
  X.Y]` / `[Dorotheus *Carmen* X.Y.Z via 'Umar al-Tabari → Dykes 2017]`
  / `[project heuristic]` / `[Source-only candidate]` / `needs verification`
- **文件命名**：
  - plan = `vX.Y-<topic>-plan.md`
  - case = `case-NN-<subject>-<focus>.md`
  - revision = `case-NN-revision-plan.md`
  - reader 渲染 (v2.3 unguarded fork) = `charts/case-NN/reader/NN-<slug>.md` per topic
  - 历史 TL output = `case-NN-TL.md` (SUPERSEDED 2026-05-18; render skill 接管, 不再产新文件)
- **v1 锁定**：2026-05-15。任何改动 additive + watermark
- **5 步 audit** 完才算 phase done（per AGENTS.md「Post-Codex audit checklist」）
- **Session 间同步**：靠 STATUS.md + plan files + 本文件，**不**靠 chat history

---

## 3. 当前项目状态锚（last updated 2026-05-15）

- v1 `hellenistic-natal-core`：**locked**, stable
- Sibling skills：`prose-normalizer` ✓ / `translation-layer` ✓
- v2.1 collectively complete：Phase A 三源抽取 + Phase B 整合 + Phase C
  case-05
- case-05 衍生 plan：**fully closed**（§A Pattern 3 / §B rare）
- 当前活动 plan：`v2.x-integrated-portrait-plan.md`（Phase A
  执行中 / Phase B-F 待 dispatch）
- 详见 STATUS.md 顶部「最后更新」行 + 「当前阶段」段

---

## 4. 不要做（hard 红线）

- **不要 placement cookbook**（"行星 X 在宫 Y 意味着 Z"）—— per
  `delineation-output-rules.md` Prose Gate
- **不要修 v1 既有内容**（既有 focus 行 / dignities 表 / Lot 公式 /
  workflow 文件）—— v1 locked，additive only
- **不要在 reading 用 chart factor 作生命陈述语法主语**（应是人 / 事 /
  状态）
- **不要把 specialist supplements 应用到 real-person predictive contexts**
- **不要绕过 5 步 audit**——任何 executor 回报必须 5 步全过
- **不要跨 session 靠 chat memory 同步**——用 STATUS.md + plan files
- **不要在 reading 给 doom / catastrophe 框架**——困难条件 guardrail（压力域
  + 缓解 + 通道），per delineation-output-rules

---

## 5. 模块结构（同 AGENTS.md §8）

> **⚠️ Module tree snapshot 2026-05-15** — 下面的 tree 是 v2.2 闭包时
> 的目录快照. v2.3 reframe + unguarded fork + Wave 1-5 cleanup 之后,
> 当前 active module 结构以 **AGENTS.md §8** 为准 (`translation-layer/`
> + `prose-normalizer/` 在本 fork 已 DEPRECATED + 目录不存在;
> `handoff-templates/v2.2-stage-handoffs.md` 内 TL pass 模板已
> SUPERSEDED — 详 AGENTS.md §8 + STATUS.md Round 4/5).

```text
项目根/
├── AGENTS.md                # 项目 SOPs（v1 协议 / provenance / audit）
├── STATUS.md                # 磁盘权威快照
├── method-index.md          # 本文件（导航 map）
├── pending-verifications.md # 中央 verification queue
├── v2-roadmap.md            # v2.x 候选 + 排除分类
│
├── rules/                   # v1 + v2.x additive；reading workflow 核心
│   ├── reading-workflow.md       (编排层 — v1 single-session)
│   ├── delineation-output-rules.md (输出层 + C.3 technical anchor section)
│   ├── significator-hierarchy.md  (focus / roster)
│   ├── planet-condition-audit.md  (audit subroutine)
│   ├── aspect-reception-rules.md  (testimony + A.1 Reception Detection Procedure)
│   ├── house-topic-framework.md   (topic chain)
│   ├── lots-and-fortune.md        (Lots)
│   ├── timing-techniques.md       (profections / ZR / etc)
│   ├── dignities-reference.md     (确定性表)
│   ├── data_contract.md           (input gate)
│   ├── source-map.md              (source registration)
│   ├── cross-source-method-comparison.md (reference companion)
│   ├── stage1-data-extraction.md  ← v2.2 A.2/A.4 (Stage 1 deterministic 6 表 + 12 步 + 4 gates + handoff)
│   ├── topic-modules.md           ← v2.2 B.1/B.2/B.4/B.5/B.7 (太极点 model / 7+6 modules / Stage 2/3 specs / orchestration)
│   └── brief-shot-discipline.md   ← v2.2 C.1/C.5 (8 criteria + register hygiene + 范文 maintenance policy)
│
├── extractions/             # 按源抽取
│   ├── brennan-hellenistic-astrology/  # baseline
│   ├── dorotheus-carmen/              # v2.1 Phase A
│   ├── valens-anthology/              # v2.1 Phase A
│   └── firmicus-mathesis/             # v2.1 Phase A
│
├── skill-draft/             # hellenistic-natal-core 薄入口
│   └── SKILL.md
│
├── prose-normalizer/        # sibling skill
│   ├── SKILL.md
│   ├── terminology-map.md
│   └── normalization-rules.md
│
├── translation-layer/       # sibling skill (TL pass; full Chinese reader-facing)
│   ├── SKILL.md                    (+ B.6.4 "what next" sibling cross-link)
│   └── output-rules.md             (+ C.2 Brief Shot Requirement + 8th rubric)
│
├── handoff-templates/       ← v2.2 B.7 (paste-ready handoff prompts)
│   └── v2.2-stage-handoffs.md      (5 templates: Stage 1 dispatch / audit / Stage 2 per-topic / Stage 3 portrait / TL pass)
│
├── cases/                   # case reading 落地
│   ├── case-01.md          (whole life / 夜盘)
│   ├── case-02.md      (wealth / 昼盘)
│   ├── case-03.md          (annual / 昼盘)
│   ├── case-04.md  (character + A.1' / 昼盘; v2.2.x post-A.3 audit revisions applied)
│   ├── case-04-TL.md                  (TL pass)
│   ├── case-05.md     (divinatory / 夜盘)
│   ├── case-05-TL.md                  (TL pass, privacy-untracked)
│   ├── case-06a.md (fictional-subject plan Phase B)
│   ├── case-06.md        (skill performance blind test, privacy-untracked)
│   └── case-06-TL.md                  (TL pass, privacy-untracked)
│
├── samples/                 # 手写目标参照 + v2.2 deliverables
│   ├── case-04-TL-target.md
│   ├── topic-reading-template.md       ← v2.2 范文 (technical canonical §I-§IV+§VI + TL §V brief shot catalog seed)
│   └── brief-shot-catalog.md           ← v2.2 C.4 (per-topic 3–5 finding themes + anti-pattern 独立段)
│
├── v2.2-stage1-reception-audit-report.md ← v2.2 A.3 (case-01..06 reception audit pass per A.1 procedure)
│
└── v*.x-*-plan.md           # plan 文件（多个）
    ├── v2.0-translation-layer-plan.md  (closed)
    ├── v2.1-phase-a-*-plan.md          (closed, 多个)
    ├── v2.1-phase-b-rule-update-plan.md (closed)
    ├── v2.1-phase-c-practitioner-divinatory-case-plan.md (closed)
    ├── v2.x-case-05-rule-extension-candidates-plan.md (closed)
    ├── v2.x-integrated-portrait-plan.md (active; Phase A+B done, Phase C-F superseded by v2.2 stage-based — see plan top supersession note)
    ├── v2.2-stage1-data-extraction-architecture-plan.md (closed; Plan A 5/5)
    ├── v2.2-topic-module-composite-reading-plan.md      (closed; Plan B 8/8)
    └── v2.2-output-concreteness-plan.md                 (closed; Plan C 6/6)
```

---

## 6. 何时该更新本文件

- 加新 sibling skill / 新顶层 workflow（如 integrated-portrait-workflow.md
  / specialist-supplements-protocol.md）
- 加新 rule 文件
- 改变 case 命名约定 / file naming convention
- 项目阶段 milestone 切换（v2.1 → v2.2 等）
- 模块结构调整

**不要**：每次 commit 都 update（本文件是稳定 navigation；详细 status
在 STATUS.md）。
