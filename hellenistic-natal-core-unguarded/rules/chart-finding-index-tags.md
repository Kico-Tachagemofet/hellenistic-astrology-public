# Chart-Finding-Index Tags — Reference Inventory

> ## ⚠️ UNGUARDED FORK OVERRIDE (2026-05-18)
>
> All references in this file to **ethical-guard**, **default OFF**,
> **on user request only**, **extension-on-request**,
> **confidence:speculative auto-flag on body/death/longevity topics**,
> **attenuated ethical guard for fictional subjects**, **symbolic
> framing required**, **pressure + mitigation + channel triad as
> mandatory output structure**, and similar safeguard / guardrail /
> disclaimer mechanisms are **NO-OP** in this fork.
>
> Authority for these topics now lives in:
> - `fictional-subject-ethical-guard.md` (stub explaining removal)
> - `delineation-output-rules.md` Direct Relational Statement section
>   (this fork's positive replacement)
> - `SKILL.md` "What this fork removes" table
>
> Specifically:
> - All 15 topics (default 9 + former extension 6: children / siblings
>   / friends-benefactors / illness / death / longevity / body) are
>   ordinary topics. No request-gating. No default-OFF.
> - `confidence:speculative` is assigned only on actual evidence merit
>   (thin testimony / contradiction / data gap), NEVER on topic-
>   membership grounds.
> - `polarity:difficulty` does NOT require pressure+mitigation+channel
>   triad; the finding states what the evidence supports per Direct
>   Relational Statement section.
> - Operative magical procedure SCOPE-out (Picatrix / Agrippa) is the
>   ONLY safeguard kept; lives in SKILL.md Trigger conditions
>   "Do NOT trigger" list.
>
> Original 2026-05-17 v2.1 baseline preserved below for tag-inventory
> structural reference. Read inline ethical-guard mentions as
> historical doctrine, not as enforced rules in this fork.

---

> **v2.1** (2026-05-17) — metadata / source-status cleanup pass per codex v2
> regression review (`v2.3-tag-inventory-codex-review-v2.md`). Structural
> decisions from v2.0 remain unchanged; this pass fixes count arithmetic,
> normalizes hybrid source-status labels, adds `Implementation status` for
> timing + specialist tags, strengthens weak direct-source citations, and
> qualifies extension-topic Lots as candidate/deferred per source pool truth.
> See §"Codex v2 regression status (v2.1)" below for per-finding trace.
>
> **v2.0** (2026-05-16) — post-codex-review revision (preserved). All v0.1 →
> v2.0 changes per `v2.3-tag-inventory-codex-review.md`:
>
> - **Renames** (source fidelity over reader ergonomics): `topic:love-marriage`
>   → `partnership-marriage`; `topic:occult` → `divination-spirituality`;
>   `topic:force-pattern` → `chart-signature`; `modality:back-channel` →
>   `aversion-reception`
> - **Dimension 4 split** (life-stage was conflating project age-bands with
>   Hellenistic timing doctrine): `life-stage` → `age-band` (5 tags,
>   project-heuristic) + `timing-activation` (17 tags, source-grounded)
> - **Topic dimension**: 10 → 15 (added 6 extension: `children` / `siblings` /
>   `friends-benefactors` / `illness` / `death` / `longevity`; removed `timing`
>   → moved to timing-activation dim)
> - **Modality dimension**: 15 → 30 (added 14 Hellenistic core operations:
>   `ruler-routed` / `lot-routed` / `configured` / `averse` / `received` /
>   `bonified` / `maltreated` / `overcoming` / `enclosed` / `under-beams` /
>   `retrograde` / `stationary` / `sect-supported` / `contrary-sect` — all
>   `direct-source`; plus 1 project shape tag `clustered` as opposite of
>   `distributed`, `project-heuristic`)
> - **Question-type**: 15 → 17 (added `choice-support` / `timing-when`)
> - **Subject-discipline**: 5 → 7 (added `event` / `question`)
> - **Source status legend** added to every tag (`direct-source` /
>   `source-components` / `project-composite` / `project-heuristic` /
>   `project-query` / `project-output-discipline`)
> - **Wording fixes**: `polarity:mixed` clarified as well-evidenced
>   contradiction (NOT average); `confidence:mixed-high` reframed as derived
>   query tag (NOT 5th canonical tier); `visible`/`hidden` mutex relaxed;
>   `modality:timing-conditional` partner must be a **non-`none`**
>   `timing-activation:*` tag (NOT `age-band:*`)
> - Numerous per-tag wording corrections per codex per-tag verification
>   (`topic:career` softened Sun-by-sect; `topic:wealth` Jupiter as supporting
>   not primary; `topic:learning` marked project-composite; `subject-discipline:structure` limited to non-life-claim only; etc.)
>
> **Tag total: 101** (15 topic + 5 polarity + 5 confidence + 5 age-band + 17
> timing-activation + 30 modality + 17 question-type + 7 subject-discipline).
> Note: 99 non-shim/non-derived operational tags if excluding
> `confidence:mixed-high` (derived query tag) and `timing-activation:none`
> (project-output-discipline shim).

## Purpose

Tags are the dimension labels attached to every chart-finding-index finding,
making findings queryable by tag combinations. The decision-maker (practitioner / AI
assistant) facing an arbitrary reader-question composes the answer by:

1. Translating the reader-question into a tag combination
2. Querying the finding-index for findings matching that tag combination
3. Pulling the matched findings (each self-contained with raw audit + Hellenistic
   doctrine basis + concretization library + not-fit + reader-facing 短描)
4. Composing the answer from the pulled findings

Tags must be:
- **Stable** — not invented per chart
- **Doctrine-grounded where claimed** — each `direct-source` tag verifiable
  against Hellenistic source pool; `project-*` tags explicitly labeled
- **Query-shaped** — tag combinations should map cleanly onto common
  reader-question shapes

## Architecture context

The chart-finding-index source layer per v2.3 architectural reframe:

```
charts/case-NN/
    chart-finding-index.md          # 主文件: Stage 1 raw data (T1-T6 embedded)
                                    #   + chart-level findings (≈ 35-45)
                                    #   + cross-finding refs + tag annotations
    topic-findings/
        character.md                # Per-topic findings (lighter schema)
        career.md
        partnership-marriage.md     # renamed (was: love-marriage)
        family.md
        learning.md
        wealth.md
        divination-spirituality.md  # renamed (was: occult)
        body.md                     # (extension, ethical guard)
        chart-signature.md          # renamed (was: force-signature/force-pattern)
        children.md                 # (extension, per codex)
        siblings.md                 # (extension, per codex)
        friends-benefactors.md      # (extension, per codex)
        illness.md                  # (extension, ethical-guard OFF default)
        death.md                    # (extension, ethical-guard OFF default)
        longevity.md                # (extension, ethical-guard OFF default)
    question-index.md               # Reader-question → finding refs utility
```

Each finding entry carries tags from the dimensions below. Required dimensions
(every finding must tag at least one value): `topic` / `polarity` /
`confidence`. Recommended: `modality` / `question-type`. Recommended for
timing-conditional findings: `timing-activation`. Optional: `age-band` /
`subject-discipline`.

## Source status legend (per codex review §"Patch List" item 1)

Every tag carries one of:

| Status | Meaning |
|---|---|
| `direct-source` | Concept named directly in Hellenistic source pool with ≥2-source triangulation met |
| `source-components` | Components are source-grounded with ≥2-source triangulation, but the named integration / composite is project-coined |
| `project-composite` | Project synthesis of multiple Hellenistic components into a named modality/topic; not a single Hellenistic doctrine |
| `project-heuristic` | Interpretive vocabulary or operational label; concept not in source pool but useful for the chart-finding-index workflow |
| `project-query` | Reader-query framework label; not source; supports finding-query workflow |
| `project-output-discipline` | Output discipline label; mirrors existing project rule files (`delineation-output-rules.md` / `aspect-reception-rules.md` / etc.) |

Per-tag `Source mechanism (if rename)`: where a project-facing slug differs
from canonical source terminology, the source mechanism is named explicitly so
peer-astrologer / codex / future review can re-trace.

## Tag dimensions overview

| # | Dimension | Required? | Tag count | Closed / Open | Source basis summary |
|---|---|---|---|---|---|
| 1 | `topic` | ✓ | 15 (9 default + 6 extension) | Closed + extension namespace | 13 direct-source + 1 source-components + 1 project-composite |
| 2 | `polarity` | ✓ | 5 | Closed | 5 project-output-discipline |
| 3 | `confidence` | ✓ | 5 (4 canonical + 1 derived) | Closed mirror | 4 mirror existing rule + 1 project-query |
| 4 | `age-band` | optional | 5 starter | Open (numeric/project) | 5 project-heuristic |
| 5 | `timing-activation` | recommended (for timing-conditional findings) | 17 starter | Open extension allowed | 16 direct-source + 1 project-output-discipline |
| 6 | `modality` | recommended | 30 starter | Open extension allowed | 21 direct-source + 1 source-components + 3 project-composite + 5 project-heuristic |
| 7 | `question-type` | recommended | 17 starter | Open extension allowed | 17 project-query |
| 8 | `subject-discipline` | optional | 7 | Closed | 7 project-output-discipline |

## Tagging mechanics

- **Slug format**: ASCII lowercase letters + hyphens. No underscores, spaces,
  or CJK in tag slugs.
- **Multi-value tags**: a finding may carry multiple tags from the same
  dimension (e.g., a learning + occult finding tags `topic:learning` AND
  `topic:divination-spirituality`).
- **Open extension** (`modality` / `question-type` / `age-band` /
  `timing-activation`): a finding may introduce a new tag slug if no starter
  tag fits — but the new tag must be added to this reference with definition
  + source status + Hellenistic basis pointer (if claimed source-grounded)
  within the same finding-index session (no orphan tags).
- **Required dimensions** (`topic` / `polarity` / `confidence`): every finding
  must carry at least one value from each. Missing required tag = finding
  incomplete.
- **Confidence + polarity interaction**: `polarity:mixed` (well-evidenced
  contradiction) typically pairs with `confidence:mixed-high` (both sides
  high). Per codex — moderate-grade mixed evidence may use
  `confidence:moderate + polarity:mixed`; do not force `mixed-high` label.
- **Tags do not change findings** — tagging is metadata; finding statement /
  audit chain / Hellenistic basis stay primary.
- **Slug ↔ file name correspondence**: where a `topic:*` slug names a Stage 2
  module, the `charts/case-NN/topic-findings/<slug>.md` file uses the same
  slug. Per v2.0 renames, file names updated accordingly.

---

## Dimension 1: topic (15 = 9 default + 6 extension)

Closed default 9 + extension namespace 6. Default 9 are always available;
extension topics gated by user request + ethical-guard discipline.

### Default 9

#### `topic:character`

**Source status**: `direct-source`

**Definition**: Findings describing person-as-whole / 整体 person-shape;
Ascendant + Asc-ruler + sect light + Sun-Moon coordination as the self-anchor.

**Criteria**: tag when the finding's core claim is about who-this-person-is at
the structural level (not about a specific life domain).

**Example**: F002 "网络型不是集中型 — 力量来自 5 个不同位置之间的连接，无单一中心"
tags `topic:character` + `topic:chart-signature`.

**Hellenistic basis**:
- `[Brennan Ch.12-13]` printed pp. 426-484 — Ascendant + significators + ruler
  chain as person anchor
- `[Valens Anth. II.2-3]` (Riley) — planet-as-significator + Asc/Fortune
  comparison
- `[Firmicus Math. II.27-29 / IV.19]` Bram printed — combined-condition
  character + chart-ruler audit

≥2-source: **met** (3 sources).

**Note** (per codex): Do not let `character` absorb `chart-signature`; the
latter is a chart-lord / archetype overlay specifically about Master of
Nativity / oikodespotes.

#### `topic:career`

**Source status**: `direct-source`

**Definition**: Findings about work / vocation / public action; MC + 10 +
10-ruler + Spirit Lot + Spirit-ruler as career anchor; **sect light as
visibility/coherence witness** (per codex — softened from v0.1 "Sun-by-sect as
career anchor", which is not as directly career-specific as MC/10th and
occupation significators); Mars + Mercury + Saturn as work-mode natural sigs.

**Criteria**: tag when the finding's core claim is about what work fits / what
work-mode operates / how vocational identity radiates.

**Example**: F001 "Jupiter 9-fold integration manager" tags `topic:career`
(livelihood/work-channel) + `topic:wealth` + `topic:partnership-marriage` + …

**Hellenistic basis**:
- `[Brennan Ch.10]` printed pp. 340-363 — 10th = action, reputation, occupation
- `[Valens Anth. II]` (Riley) — X place and action/accomplishment material
- `[Firmicus Math. IV.21]` Bram printed — occupation significators (esp. Mars,
  Venus, Mercury) with condition and sign quality
- `[Dorotheus Carmen I-II via 'Umar al-Tabari → Dykes 2017]` — topic chapters

≥2-source: **met** (4 sources).

#### `topic:partnership-marriage`

**Source status**: `direct-source`

**Source mechanism**: renamed from v0.1 `topic:love-marriage` per codex review
— "love" routed through 5th is project-facing modern romance language; the
Hellenistic marriage anchor is **7th + Venus + Marriage Lot**. 5th contributes
pleasure/Venus joy and children (now its own `topic:children` extension).

**Definition**: Findings about partnership / marriage / formally-bonded
relationship; 7th + 7th-ruler + Venus + Marriage Lot + Eros Lot.

**Criteria**: tag when the finding's core claim is about how partnership
forms / what partner type fits / what bonding mode operates.

**Example**: F006 "Pact-form relationship structure — Jupiter spine 7 + Sun-
Venus mutual reception in aversion + Saturn 5 of-sect" tags
`topic:partnership-marriage` + `topic:character`.

**Hellenistic basis**:
- `[Brennan Ch.10]` printed pp. 340-363 — 7th = marriage/partnership
- `[Valens Anth. II.37-38]` (Riley) — marriage/wedlock + marriage Lot material
- `[Dorotheus Carmen II.1-II.6 via 'Umar al-Tabari → Dykes 2017]` — marriage
  uses Venus + Venus triplicity lords + 7th place + marriage/wedding Lots

≥2-source: **met** (3 sources).

#### `topic:family`

**Source status**: `direct-source` (with project-reconciliation of 4+10
parental doctrine per `cross-source-method-comparison.md` Flag 14)

**Definition**: Findings about family of origin / parent images; 4 + 4-ruler +
10 (one-parent doctrine variant per Flag 14) + Sun (father natural sig) + Moon
(mother natural sig) + Father Lot + Mother Lot.

**Criteria**: tag when the finding's core claim is about formative family
field / parent images / inherited structural texture.

**Example**: F015 "Father channel on-channel but off-stage — Sun 9 cadent +
Saturn-Sun tightest trine" tags `topic:family`.

**Hellenistic basis**:
- `[Brennan Ch.10]` — 4th = parents/home/foundations; parallel paternal
  doctrine note for 10th
- `[Valens Anth. II]` — 4th + 10th parents/family material
- `[Firmicus Math. II.19]` — 4th includes parents/property; cross-source
  parallel paternal routing through 10th
- `[Dorotheus Carmen I-II]` — natural significators + topic chapters

≥2-source: **met** (4 sources); 4+10 combined parental field is internally
consistent with `rules/cross-source-method-comparison.md` Flag 14.

#### `topic:learning`

**Source status**: `project-composite`

**Component status**: `direct-source` for each component (Mercury / 3rd / 9th /
sect-light-to-Mercury).

**Source mechanism**: per codex v2 normalization — primary status is one
value (`project-composite`). Components (Mercury / 3rd / 9th /
sect-light-to-Mercury) are each ≥2-source met as Hellenistic doctrine, but
"learning as distinct topic module" is project architecture, not a single
named Hellenistic topic. The composite topic-as-module framing is project-
coined.

**Definition**: Findings about learning style / mind / suitable subjects.
Components: Mercury (mind/language/learning natural sig) + 3rd (lower learning
/ communication) + 9th (higher learning / philosophy / sacred study) +
sect-light-to-Mercury configuration.

**Criteria**: tag when the finding's core claim is about how the mind
processes / learning rhythm / suitable academic domains.

**Example**: F003 "9-anchor cluster + Mercury-Saturn 1°20' tight trine —
学者-实践者深度路径" tags `topic:learning` + `topic:divination-spirituality` +
`topic:character`.

**Hellenistic basis** (components):
- `[Brennan Ch.7]` — Mercury as mind/language/learning (per codex addition)
- `[Brennan Ch.10]` — 3rd / 9th place topics
- `[Valens Anth. I-II]` — Mercury/intellect + 3rd/9th place material
- `[Firmicus Math. III / IV.7]` — Mercury learning, speech, mathematics/music,
  public responsibility when condition supports

Component ≥2-source: **met**; composite framing: **project-composite**.

#### `topic:wealth`

**Source status**: `direct-source`

**Definition**: Findings about livelihood / income channels / resource flow;
2nd + 2nd-ruler + Fortune Lot + Fortune-ruler. **Jupiter as supporting witness**
(per codex — softened from v0.1 "Jupiter as wealth natural sig as primary"
which overstates Jupiter's anchor role; primary anchor remains 2nd + Fortune).

**Criteria**: tag when the finding's core claim is about how money /
livelihood / resource operates structurally.

**Example**: F008 "Wealth via partnership network — Jupiter 2nd-ruler in 7 +
Mercury combust limits direct skill-sale" tags `topic:wealth` +
`topic:career` + `topic:partnership-marriage`.

**Hellenistic basis**:
- `[Brennan Ch.10]` — 2nd place = livelihood/possessions/resources
- `[Brennan Ch.16]` — Fortune as material/bodily/circumstantial anchor
- `[Valens Anth. II, IX]` — Fortune as derived Ascendant; Fortune/Daimon
  timing anchors
- `[Firmicus Math. IV.17]` — Part of Fortune ruler stack + quality of fortune
- `[Dorotheus Carmen I.27-I.28]` — Fortune in status/assets chains

≥2-source: **met** (5 sources).

#### `topic:divination-spirituality`

**Source status**: `direct-source`

**Source mechanism**: renamed from v0.1 `topic:occult` per codex review —
"occult" is modern umbrella term; Hellenistic category is
**sacred / divinatory / religious aptitude**. 9th = god/religion/divination
(Brennan Ch.10); 12th = hidden/isolation/Saturn joy.

**Definition**: Findings about sacred-vocation / divinatory aptitude /
mystical-practice fit; 9 (sacred / divination / religious) + 12 (hidden /
oracular / isolation) + Moon + Mercury + Saturn + Spirit Lot.

**Criteria**: tag when the finding's core claim is about sacred / divinatory /
religious aptitude / mystical-practice fit.

**Example**: F003 "9-anchor cluster + Mercury combust + 12-channel
interrupted — scholar-practitioner not oracular-trance" tags
`topic:divination-spirituality` + `topic:learning`.

**Hellenistic basis**:
- `[Brennan Ch.10]` — 9th = god/religion/divination; 12th = hidden / isolation
  / Saturn joy
- `[Valens Anth. II.5, II.7-8]` — 3rd/9th carry goddess/god + divinatory
  testimony
- `[Firmicus Math. III]` — 9th/12th + Mercury material can route to sacred /
  astrological / dream / interpretive roles
- `[Dorotheus Carmen I.9]` — 9th-house religious/divinatory material; Lot of
  Religion remains `[Source-only candidate]`

≥2-source: **met** (4 sources).

#### `topic:body`

**Source status**: `direct-source`

**Ethical guard**: **HIGH**; default **OFF** for real-person subjects (only
enable with explicit consent + symbolic framing).

**Definition**: Findings about physical vitality / health / body-as-
instrument; Asc + Asc-ruler + 6 + sect light + Mars-Saturn condition + 12.

**Criteria**: tag when the finding's core claim is about physical vitality /
body texture / health pattern.

**Example**: case-07 deferred "Moon angular own fall + sect-light cadent +
vampire-canonical-context" would tag `topic:body` + `topic:character` +
`polarity:mixed` (deferred to body extension module).

**Hellenistic basis**:
- `[Brennan Ch.12]` — Ascendant + Asc-ruler as body/life anchor
- `[Brennan Ch.17-18]` — Fortune / ZR from Fortune (bodily and circumstantial
  when timing involved)
- `[Valens Anth. I, III, VII, IX]` — body/material correspondences +
  Fortune/lifespan/body timing methods
- `[Firmicus Math. IV.1 / II.24 / VII.8, VII.21]` — Moon, Asc/MC, body/medical
  degree material (ethically guarded)
- `[Dorotheus Carmen IV.2]` — illness material via 6th + Lot + body-sign
  mapping + malefic testimony

≥2-source: **met** (5 sources).

#### `topic:chart-signature`

**Source status**: `source-components`

**Component status**: `direct-source` for the underlying concept (chart-lord /
Master of Nativity / oikodespotes).

**Assembly note**: The five-vote Lord-of-the-geniture assembly procedure per
`rules/significator-hierarchy.md` is `project-heuristic` at assembly level.

**Source mechanism**: renamed from v0.1 `topic:force-pattern` per codex review
— "force-pattern" was project-specific language; Hellenistic term is
**chart-lord / Master of Nativity / oikodespotes**. Per codex v2 normalization,
primary status is one value (`source-components`): underlying concept is
direct-source but assembly is project synthesis.

**Definition**: Findings about chart-level archetype / Master of Nativity /
integration manager / dominant force-modality (advisory / charm-coercion /
endurance / sacred-authority 等).

**Criteria**: tag when the finding's core claim is about the chart's
distinctive overall force-signature / chart-lord identity (not a single domain).

**Example**: F002 "网络型不是集中型 + Jupiter 9-fold integration manager" tags
`topic:chart-signature` + `topic:character` + `topic:wealth` + …

**Hellenistic basis**:
- `[Brennan Ch.12-15]` — chart-lord / oikodespotes / Master of Nativity
- `[Valens Anth. IX / II]` — Asc/Fortune/Daimon + planet-as-significator
  weighting supports multi-anchor chart signature
- `[Firmicus Math. IV.19]` — ruler of chart selection + audit
- `rules/significator-hierarchy.md` — five-vote Lord-of-the-geniture procedure
  (project-heuristic at assembly level)

≥2-source: **met** (3 sources for concept) + project-heuristic for assembly.

### Extension 6 (user-request only; per ethical-guard discipline)

Per codex review §"Coverage gaps" — these Hellenistic topics were missing from
v0.1 and are added in v2.0 as extension namespace. Extension topics dispatch
**only on user request** + per ethical-guard discipline (per
`rules/topic-modules.md` §4.1.3 + project ethical-guard policy).

#### `topic:children`

**Source status**: `direct-source`

**Definition**: Findings about children / progeny / 5th-place children
material; 5 + 5-ruler + Jupiter (natural sig) + Lot of Children [Source-only
candidate, formula-deferred pending `lots-and-fortune.md` cross-source
verification].

**Hellenistic basis**:
- `[Brennan Ch.10]` — 5th = children + pleasure + Venus joy
- `[Dorotheus Carmen II via 'Umar → Dykes 2017]` — children chapters
- `[Valens Anth. II]` — 5th place material

≥2-source: **met** (3 sources for 5th-place children topic). Lot of Children:
formula-deferred per project Lot-verification queue.

**Note** (per codex): "children is especially strong in Dorotheus and Brennan
5th-place material; hiding it inside love/5th would blur topic boundaries."
Hence separated from `partnership-marriage` (now 5th-children-pleasure split
from 7th-marriage).

#### `topic:siblings`

**Source status**: `direct-source`

**Definition**: Findings about siblings / 3rd-place siblings material; 3 +
3-ruler + Mercury (natural-sig sibling-channel) + Lot of Siblings [Source-only
candidate, formula-deferred pending `lots-and-fortune.md` cross-source
verification].

**Hellenistic basis**:
- `[Brennan Ch.10]` — 3rd = siblings + lower learning + short journeys
- `[Valens Anth. II]` — 3rd place material
- `[Dorotheus Carmen II]` — siblings chapters

≥2-source: **met** (3 sources for 3rd-place siblings topic). Lot of Siblings:
formula-deferred per project Lot-verification queue.

#### `topic:friends-benefactors`

**Source status**: `direct-source`

**Definition**: Findings about friends / benefactors / hopes / 11th-place
material; **11th place ("Good Spirit" = Joy of Jupiter per Brennan Ch.10
house doctrine) + 11-ruler + Jupiter as natural-significator (friendship /
benefactor / good-fortune)**. Topic-Lot anchor: Lot of Friends [Source-only
candidate, formula-deferred pending `lots-and-fortune.md` cross-source
verification].

**Hellenistic basis**:
- `[Brennan Ch.10]` — 11th place = "Good Spirit" (Agathos Daimon), joy of
  Jupiter, friends + benefactors + hopes (HOUSE meaning, not a separately
  computed Lot)
- `[Valens Anth. II]` — 11th place material
- `[Brennan Ch.7 + Ch.10]` — Jupiter as natural significator of friendship +
  benefactor + good-fortune themes

≥2-source: **met** (3 sources for 11th-place house doctrine + Jupiter natural
significator). Lot of Friends: formula-deferred per project Lot-verification
queue.

**Note** (per codex v1 review): "friends-benefactors / 11th-place support was
absent in v0.1. This is a major Hellenistic topic (Good Spirit, friends,
benefactors, hopes)."

**Note** (v2.1.1 wording fix per example-case Stage 2 cross-rule check, 2026-05-17):
Earlier v2.1 inventory wording claimed "Lot of Good Spirit (direct-source per
Brennan Ch.16 + Valens IX)" as a separately-computed canonical Lot anchor.
This was an over-claim: "Good Spirit" in Hellenistic doctrine names the **11th
HOUSE** (Agathos Daimon, joy of Jupiter, per Brennan Ch.10), not a separately
computed Hermetic Lot in the v1-locked set (Brennan Ch.16 Hermetic Lots =
Fortune / Spirit / Eros / Necessity / Courage / Victory / Nemesis — no
separate "Lot of Good Spirit"). Variant traditions sometimes use a `Asc +
Jupiter − Sun` formula for "Lot of Agathos Daimon" but this is non-v1.
**Resolution**: this entry now correctly anchors on the 11th house + 11-ruler
+ Jupiter natural-sig (all direct-source), removing the spurious Lot claim.
Lot of Friends remains [Source-only candidate, formula-deferred] as before.

#### `topic:illness`

**Source status**: `direct-source`

**Ethical guard**: **HIGH**; default **OFF** for real-person (only enable with
explicit consent + symbolic framing).

**Definition**: Findings about illness / 6th-place affliction material; 6 +
6-ruler + Mars-Saturn condition + body sign mapping + Lot of Illness [Source-
only candidate, formula-deferred pending `lots-and-fortune.md` cross-source
verification — Dorotheus IV.2 names the Lot in illness context but exact
formula is one of the Lot-formula items in queue].

**Hellenistic basis**:
- `[Brennan Ch.10]` — 6th = illness / affliction / slavery / labor
- `[Dorotheus Carmen IV.2]` — illness material uses 6th + Lot + body-sign +
  malefic testimony

≥2-source: **met** (2 sources for 6th-place + body/malefic illness audit).
Lot of Illness: formula-deferred per project Lot-verification queue.

#### `topic:death`

**Source status**: `direct-source`

**Ethical guard**: **HIGH**; default **OFF** for real-person (only enable with
explicit consent + symbolic framing). Per fictional-subject attenuated-guard framing,
applies to fictional + canonically-marked subjects.

**Definition**: Findings about 8th-place death/mortality material; 8 +
8-ruler; natural sigs per source.

**Hellenistic basis**:
- `[Brennan Ch.10]` — 8th = death / inheritance / shared resources
- `[Valens Anth. II.36-37, III, VIII-IX]` — 8th place + death timing material
  (precise extraction pending; current citation is broader than ideal)
- `[Firmicus Math. III, VII]` — 8th-place death material in placement
  cookbook + life-prediction (specialist; ethical-guard preserved)
- `[Dorotheus Carmen III]` — death-related Hyleg/Alcocoden adjacent material
  (specialist; not for ordinary reading)

≥2-source: **met** (4 sources). Note (per codex): broad `[Valens Anth.]`
citation should be tightened to specific book/chapter pointers as extraction
advances; current state is source-record-precise enough for tag-level use,
not yet for finding-level use.

#### `topic:longevity`

**Source status**: `direct-source`

**Ethical guard**: **HIGH**; default **OFF** for real-person.

**Implementation status**: `deferred` (length-of-life methods are specialist
material per `v2-roadmap.md` permanent-specialist Tier; tag may appear in
finding-index as source-record annotation; not run as ordinary procedure in
v2.3 or v1.)

**Definition**: Findings about lifespan / Hyleg / Alcocoden / climacteric /
planetary-years material.

**Hellenistic basis**:
- `[Brennan]` length-of-life discussion (per `rules/topic-modules.md`
  provenance — exact chapter pinning pending; Brennan treats Hyleg/Alcocoden
  in length-of-life context, not Ch.17 alone)
- `[Valens Anth. III]` longevity-critical methods (book extraction present)
- `[Firmicus Math. II.25 / IV.20]` length-of-life + chronocrator material
- `[Dorotheus Carmen III]` length-of-life material

≥2-source: **met** (4 sources). Note (per codex): v2.0 cited Brennan Ch.17
for Hyleg/Alcocoden which was likely miscited; v2.1 cites the topic-modules
provenance chain. Tag remains source-grounded; implementation deferred per
specialist policy.

---

## Dimension 2: polarity (closed, 5)

How the finding sits relative to overall chart promise. Required tag.

### `polarity:strength`

**Source status**: `project-output-discipline` (per `rules/delineation-output-rules.md`)

**Definition**: Finding describes a structurally well-dignified / well-
configured / load-bearing positive feature of the chart.

**Criteria**: dignified planet (own domicile / exaltation / triplicity primary /
of-sect) + angular or supportive configuration + ≥2 module witness.

### `polarity:difficulty`

**Source status**: `project-output-discipline`

**Definition**: Finding describes a structurally受压 / debilitated / out-of-
sect / adversely configured feature. **Must** be paired with pressure +
mitigation + channel triad per `rules/delineation-output-rules.md`
§"Difficult-Condition Guardrails".

**Criteria**: detriment / fall / contrary-to-sect / combust / cadent + hard
configuration + ≥2 module witness.

### `polarity:mixed`

**Source status**: `project-output-discipline`

**Definition**: Finding where two structurally clean testimonies pull opposite
directions **within the same significator or chain** (within-finding scope).

**Per codex** — critical wording fix: `mixed` is **well-evidenced
contradiction, NOT average**. If low/muddy contradiction exists, do NOT use
`mixed`; report as `polarity:structural` + open thread instead.

**Pairing**: typically with `confidence:mixed-high` (both sides high); per
codex — if only moderate-grade mixed evidence exists, use
`confidence:moderate + polarity:mixed` instead of forcing high label.

**Mixed vs tension distinction**: `mixed` is within-finding (one significator
shows both sides); `tension` is cross-finding (2+ independently confident
findings juxtapose).

### `polarity:structural`

**Source status**: `project-output-discipline`

**Definition**: Descriptive finding that doesn't carry strength/difficulty
polarity but describes a structural fact about chart organization (e.g.,
"distributed signature, no cluster" / "Same-Planet Multi-Role density at X").

### `polarity:tension`

**Source status**: `project-output-discipline` (per Stage 3 cross-topic
tension framework)

**Definition**: Cross-finding/cross-topic juxtaposition where 2+ independently
confident findings pull opposite directions or operate on un-coordinated
channels (cross-finding scope; distinguished from `polarity:mixed`).

**Criteria**: requires ≥2 component findings each independently
`confidence:high`; the tension itself emerges from their juxtaposition, not
from either alone.

---

## Dimension 3: confidence (closed, 5 = 4 canonical + 1 derived query tag)

Mirror of existing 4-tier framework per `rules/delineation-output-rules.md`
§"Evidence Standard And Confidence Tiers", plus one derived query convenience
tag (`mixed-high`).

### `confidence:high`

**Source status**: `project-output-discipline` (mirrors existing rule)

≥ 2 Hellenistic sources triangulate + ≥ 2 module witness (cross-topic).
Default register for stable findings.

### `confidence:moderate`

**Source status**: `project-output-discipline` (mirrors existing rule)

≥ 1 source + 1-2 module witness; not yet fully triangulated to High.

### `confidence:low`

**Source status**: `project-output-discipline` (mirrors existing rule)

Single-source candidate; flagged for further triangulation. Marked
`[Source-only candidate]` in finding entry.

### `confidence:speculative`

**Source status**: `project-output-discipline` (mirrors existing rule)

Symbolic resonance / canon-resonance / character-symbolic only. Not predictive.
Attenuated ethical guard required when applied to fictional subjects.

### `confidence:mixed-high`

**Source status**: `project-query` (**derived query tag, NOT a 5th canonical
tier**)

**Per codex** — critical wording fix: `mixed-high` is **not a 5th canonical
tier** in `rules/delineation-output-rules.md`; it is a query convenience tag
for well-evidenced mixed testimony (both sides independently high). Use only
when finding's `polarity:mixed` testimony is structurally clean on both sides.
If only moderate-grade evidence exists on one or both sides, use
`confidence:moderate + polarity:mixed` instead.

---

## Dimension 4: age-band (open, optional, project-heuristic)

**Per codex review §"Recommended structural change 1"**: split from old
Dimension 4 `life-stage`. Age-bands are useful reader-query metadata but
**NOT Hellenistic doctrine**. Use only when reader-query relevance demands;
otherwise leave un-tagged.

Default 5 bands; numeric / project bands open for extension.

### `age-band:age-0-12`

**Source status**: `project-heuristic`

**Definition**: Modern age band 0-12. Project-heuristic; corresponds approximately to
first annual profection cycle (per `[Brennan Ch.17]`), but the age-band tag
itself is metadata, **not** a Hellenistic life-stage doctrine.

### `age-band:age-12-24`

**Source status**: `project-heuristic`

**Definition**: Modern age band 12-24. Project-heuristic.

### `age-band:age-25-40`

**Source status**: `project-heuristic`

**Definition**: Modern age band 25-40. Per codex — "Saturn first square at ~28"
is NOT enough Hellenistic basis; this is project age-band only.

### `age-band:age-40-60`

**Source status**: `project-heuristic`

**Definition**: Modern age band 40-60. Project-heuristic.

### `age-band:age-60-plus`

**Source status**: `project-heuristic`

**Definition**: Modern age band 60+. Project-heuristic.

---

## Dimension 5: timing-activation (open, 17 starter, source-grounded)

**Per codex review §"Recommended structural change 1"**: split from old
Dimension 4 `life-stage`. Timing-activation tags name actual Hellenistic
timing techniques. Used when a finding activates at a specific timing window.

Pair with `modality:timing-conditional` (must be a non-`none` value to satisfy
the modality's required-partner rule). For natal-promise structural findings
that are NOT timing-conditional, use `timing-activation:none`.

**Implementation status field (per codex v2)**: Several timing tags are valid
as source concepts but the project's existing extraction/method-comparison
work has not yet operationalized them. Each tag below carries one of:

| Implementation status | Meaning |
|---|---|
| `implemented` | Method extraction + cross-source comparison sufficient for v2.3 finding-index use |
| `deferred` | Source-grounded but procedure deferred to a future v-roadmap milestone; do not run as ordinary procedure in v2.3 |
| `needs-reconciliation` | Source-grounded but multi-source variance unresolved; see `pending-verifications.md` entry |
| `source-record-only` | Concept exists in source pool; project has no operational procedure; tag may appear in finding-index but only as source-record annotation |

Tags without an explicit field are `implemented`.

### `timing-activation:annual-profection`

**Source status**: `direct-source`

**Definition**: Finding activates via annual profection (yearly place
activation).

**Hellenistic basis**:
- `[Brennan Ch.17]` annual profections
- `[Dorotheus Carmen IV.1]` annual profections + lord of year
- `[Valens Anth. IV]`

### `timing-activation:lord-of-year`

**Source status**: `direct-source`

**Definition**: Finding activates via Lord of Year (annual time-lord).

**Hellenistic basis**:
- `[Brennan Ch.17]` annual profections
- `[Dorotheus Carmen IV.1]` lord of year

### `timing-activation:activated-place`

**Source status**: `direct-source`

**Definition**: Finding activates via profected place activation.

**Hellenistic basis**:
- `[Brennan Ch.17]` annual profections
- `[Valens Anth. IV]` profected place doctrine

### `timing-activation:activated-tenant`

**Source status**: `direct-source`

**Definition**: Finding activates via tenant of profected place.

**Hellenistic basis**:
- `[Brennan Ch.17]`
- `[Valens Anth. IV]`

### `timing-activation:zr-l1`

**Source status**: `direct-source`

**Definition**: Finding activates during a Zodiacal Releasing L1 大段 (period
from Spirit or Fortune; typically 7-25 year arc).

**Hellenistic basis**:
- `[Brennan Ch.18]` ZR L1 periods
- `[Valens Anth. IV]` chronocratorships / distributions from Spirit + Fortune

### `timing-activation:zr-l2`

**Source status**: `direct-source`

**Definition**: Finding activates during a Zodiacal Releasing L2 子窗口
(subperiod; typically months-to-a-year).

**Hellenistic basis**:
- `[Brennan Ch.18]` ZR L2 subperiods
- `[Valens Anth. IV]` distributions / subperiod structure

### `timing-activation:peak-period`

**Source status**: `direct-source`

**Definition**: Finding activates during a ZR Peak Period (high-significance
window in ZR doctrine).

**Hellenistic basis**:
- `[Brennan Ch.18]` Peak Periods
- `[Valens Anth. IV]`

### `timing-activation:loosing-of-bond`

**Source status**: `direct-source`

**Definition**: Finding activates at a Loosing of the Bond (LB) event in ZR
releasing sequence.

**Hellenistic basis**:
- `[Brennan Ch.18]` LB
- `[Valens Anth. IV]` LB methods

**Note**: per codex — LB timing depends on releasing sequence and sign
periods; **not a universal 12-25 doctrine**. v0.1 implicit conflation of LB
with "youth" life-stage was a misstatement; LB-conditional findings now use
this tag explicitly + cite the actual computed LB window.

### `timing-activation:solar-revolution`

**Source status**: `direct-source`

**Implementation status**: `deferred` (per `pending-verifications.md` #5 and
`v2-roadmap.md` — solar revolutions deferred to v2.5; cross-source
comparison says Dorotheus IV + Firmicus need integrated extraction).

**Definition**: Finding activates via solar revolution (return chart).

**Hellenistic basis**:
- `[Brennan Ch.17]` solar revolution material
- `[Dorotheus Carmen IV]` annual computational basis (extraction pending v2.5)
- `[Firmicus Math. II.27-29]` annual chart references (extraction pending v2.5)

### `timing-activation:transit-trigger`

**Source status**: `direct-source`

**Definition**: Finding activates via specific transit trigger.

**Hellenistic basis**:
- `[Brennan Ch.19]` transits
- `[Valens Anth. VII]`

### `timing-activation:monthly-lord`

**Source status**: `direct-source`

**Implementation status**: `needs-reconciliation` (per `pending-
verifications.md` #6 and `cross-source-method-comparison.md` §9 — Brennan
has no monthly/daily extraction and Dorotheus monthly text needs verification;
current Valens VII basis is single-source for v2.3 operational use).

**Definition**: Finding activates via monthly lord (per Valens monthly time-
lord doctrine).

**Hellenistic basis**:
- `[Valens Anth. VII]` monthly time lords (primary)
- `[Dorotheus Carmen IV]` monthly material (needs verification)

### `timing-activation:daily-lord`

**Source status**: `direct-source`

**Implementation status**: `needs-reconciliation` (per `pending-
verifications.md` #6 — same multi-source variance as `monthly-lord`; Brennan
does not extract daily lord, Dorotheus daily text needs verification).

**Definition**: Finding activates via daily lord.

**Hellenistic basis**:
- `[Valens Anth. VII]` daily time lords (primary)
- `[Dorotheus Carmen IV]` daily material (needs verification)

### `timing-activation:chronocrator`

**Source status**: `direct-source`

**Definition**: Finding activates via chronocrator / time-lord assignment.

**Hellenistic basis**:
- `[Valens Anth. IV]` chronocratorships
- `[Firmicus Math. II.26-28 / IV.20]`

### `timing-activation:climacteric`

**Source status**: `direct-source`

**Implementation status**: `source-record-only` (Firmicus climacteric doctrine
exists in source pool but is single-source as written; Valens critical-year
material in Book V can strengthen — extraction pending. Tag may appear in
finding-index as source-record annotation; not run as ordinary procedure in
v2.3.)

**Definition**: Finding activates at climacteric year (per Firmicus
climacteric doctrine).

**Hellenistic basis**:
- `[Firmicus Math. II.26-28]` climacteric years (primary)
- `[Valens Anth. V]` critical-year material (parallel; extraction pending)

### `timing-activation:planetary-years`

**Source status**: `direct-source`

**Implementation status**: `needs-reconciliation` (concept is source-grounded
across the pool but current basis cites only Brennan Ch.19 + broad Valens;
Dorotheus/Firmicus planetary-years extraction can strengthen — pending.)

**Definition**: Finding activates via planetary years doctrine.

**Hellenistic basis**:
- `[Brennan Ch.19]` planetary years (primary)
- `[Valens Anth.]` planetary years (broad citation; needs precise pinning)
- `[Dorotheus Carmen]` + `[Firmicus Math.]` planetary-years material
  (extraction pending)

### `timing-activation:four-stakes`

**Source status**: `direct-source`

**Implementation status**: `source-record-only` (valid as Dorothean
timing/life-phase doctrine but single-source as written; tag may appear in
finding-index as source-record annotation tied to Dorotheus material; not run
as ordinary procedure in v2.3.)

**Definition**: Finding activates via four stakes / angular activation per
Dorotheus.

**Hellenistic basis**:
- `[Dorotheus Carmen IV]` four stakes (primary; single-source)

### `timing-activation:none`

**Source status**: `project-output-discipline`

**Definition**: Finding is natal-promise structural; not timing-conditional.
**Default for most chart-level findings**.

---

## Dimension 6: modality (open, 30 starter)

Describes the **shape / mode** of the finding. Per codex review §"Recommended
structural change 4" — modality is `mixed source status`: some tags
direct-source (Hellenistic operations), some project-composite, some
project-heuristic. Each tag carries explicit source status.

Open extension allowed; new tags must add definition + source status + basis
within same finding-index session.

### Project-derived / composite modality (10)

#### `modality:integration`

**Source status**: `project-composite`

**Definition**: Finding describes the chart's overall integration mechanism /
chart-lord / Master-of-Nativity function.

**Hellenistic basis** (components):
- `[Brennan Ch.12-15]` chart-lord / Master of Nativity
- `[Valens Anth. IX]` Fortune/Daimon/Asc comparative anchor

Composite framing: project-coined (assembly procedure per
`rules/significator-hierarchy.md` is `project-heuristic`).

#### `modality:load-bearing`

**Source status**: `project-heuristic`

**Per codex**: "Good project tag. Do not present 'load-bearing' as a source
term." Hellenistic concept = Same-Planet Multi-Role per
`rules/significator-hierarchy.md` (project heuristic).

**Definition**: Finding is a multi-functional structural carrier (multiple
roles converge on one planet / Lot / place).

**Components**:
- `[Brennan Ch.13]` ruler chains + one planet carrying topics
- `[Brennan Ch.16]` Lot ruler role
- `[Valens Anth. II]` comparing Asc-ruler + Fortune-ruler + Lot holder
- `rules/significator-hierarchy.md` Same-Planet Multi-Role Handling
  (project heuristic)

#### `modality:network`

**Source status**: `project-heuristic`

**Per codex**: "useful for findings with many linked receptions/aspects.
'Network' is a project visualization word, not a Hellenistic category."

**Definition**: Finding's pattern operates as a network (cross-place reception
+ aspect web, not single-point gravity).

**Components**:
- `[Brennan Ch.9, Ch.14]` sign-based configurations + aversion + reception
- `[Valens Anth. II-III]` configuration + reception-like audit
- `rules/aspect-reception-rules.md` reception-network procedure (project
  algorithm)

#### `modality:self-authorized`

**Source status**: `project-heuristic`

**Per codex**: "needs explicit `[project heuristic]` label and should not be
generalized from 'Asc ruler averse to Sun' alone."

**Definition**: Finding describes self-mandated agency / Asc-ruler operating
without external ratify under specific conditions (typically Asc-ruler
contrary-to-sect + Asc-ruler averse to Sun + with reception). **Tag only when
specific structural condition met**; not a generic "Mars in 10" label.

**Components**:
- `[Brennan Ch.12-13]` Asc ruler as native's steering principle
- `[Brennan Ch.7]` sect + luminary condition
- `rules/aspect-reception-rules.md` aversion + reception handling

#### `modality:aversion-reception`

**Source status**: `project-composite`

**Source mechanism**: renamed from v0.1 `modality:back-channel` per codex
review — concept is reception + aversion 4-cell matrix; "back-channel" was
metaphor. Source mechanism = mutual reception in aversion ("managers know
each other but cannot act directly").

**Definition**: Finding describes the four-cell aversion + reception matrix
cell where two planets are mutually receiving but in aversion.

**Hellenistic basis** (components):
- `[Brennan Ch.9, Ch.14]` aversion + reception components
- `[Valens Anth. II-III]` reception/configuration audit
- `rules/aspect-reception-rules.md` four-cell matrix (project heuristic)

#### `modality:depth`

**Source status**: `project-composite`

**Per codex**: "Project-composite tag. Do not claim direct source basis for
'depth-immersion / long-pass / inward revising' as a named Hellenistic
modality."

**Definition**: Finding's mechanism is depth-immersion / long-pass / reflective
/ inward revising. Typically Mercury + Saturn tight configuration + cadent +
water emphasis. **Distinguish from `modality:structured` (Saturnian
endurance/form/constraint alone) — `depth` is Mercury-Saturn composite.**

**Components**:
- `[Brennan Ch.7]` Mercury + Saturn natural significations (separately)
- `[Valens Anth. I]` planetary qualities
- `rules/significator-hierarchy.md` learning + divinatory focus notes
  (project synthesis)

#### `modality:distributed`

**Source status**: `project-heuristic`

**Per codex**: "Useful project tag for chart shape. Mark `[project heuristic]`.
Also add the missing opposite `clustered`."

**Definition**: Finding pattern is distributed across multiple places without
cluster concentration (opposite of `clustered`).

**Components**:
- `rules/stage1-data-extraction.md` T5 cluster check
- `[Valens Anth. II]` multi-planet place treatment (Hellenistic; but inverse
  "distributed across multiple places" is not a Hellenistic doctrine)

#### `modality:clustered`

**Source status**: `project-heuristic`

**Per codex** (added to fill missing opposite of `distributed`):

**Definition**: Finding involves a cluster of planets in one place / sign
(threshold ≥3 per T5 cluster check). Opposite of `distributed`.

**Components**:
- `rules/stage1-data-extraction.md` T5 cluster check threshold
- `[Valens Anth. II]` multi-tenant place treatment

#### `modality:partnership-routed`

**Source status**: `direct-source`

**Definition**: Finding's mechanism operates through the 7th house / Marriage
Lot / partnership axis. **Use only when a non-relationship topic routes
through 7th/partner axis** (per codex — otherwise duplicates
`topic:partnership-marriage`).

**Hellenistic basis**:
- `[Brennan Ch.10]` 7th place
- `[Valens Anth. II]` partnership / Venus
- `[Dorotheus Carmen II]` marriage

#### `modality:timing-conditional`

**Source status**: `source-components`

**Component status**: `direct-source` for the underlying timing techniques
(annual profections / ZR / lord-of-year / transits etc.).

**Source mechanism**: per codex v2 normalization — primary status is one value
(`source-components`). The tag itself is a workflow modality derived from
source timing methods; it is not a single Hellenistic doctrine.

**Per codex**: required partner is a **non-`none`** `timing-activation:*` tag
(NOT an `age-band:*` value, and NOT `timing-activation:none` which marks
non-timing-conditional findings). This is a critical fix from v0.1 which
paired with generic `life-stage:*-conditional`.

**Definition**: Finding only activates within a specific timing window. Tag
together with the specific `timing-activation:*` tag(s) (must be non-`none`).

**Hellenistic basis** (components):
- `[Brennan Ch.17-18]`, `[Valens Anth. IV, VII]`, `[Dorotheus Carmen IV]`
  timing methods generally

### Planet-nature modality (4)

#### `modality:structured`

**Source status**: `direct-source`

**Definition**: Finding's mechanism operates through Saturn / structural
endurance / long-cycle / discipline / weight-bearing.

**Hellenistic basis**:
- `[Brennan Ch.7]` Saturn natural significations + sect-conditioned expression
- `[Valens Anth. I]` Saturn natural quality
- `[Firmicus Math. II.7 / III]` Saturn condition + burden/depth themes

**Note** (per codex): keep condition-dependent; not a raw Saturn keyword.

#### `modality:expansive`

**Source status**: `direct-source`

**Definition**: Finding's mechanism operates through Jupiter / expansion /
breadth / hope / generosity.

**Hellenistic basis**:
- `[Brennan Ch.7]`, `[Valens Anth. I]`, `[Dorotheus Carmen I]` Jupiter natural
  significations

**Note**: use when Jupiter is actually a relevant significator/witness.

#### `modality:charm-driven`

**Source status**: `direct-source`

**Definition**: Finding's mechanism operates through Venus / aesthetic /
attraction / refinement / pleasure.

**Hellenistic basis**:
- `[Brennan Ch.7]`, `[Valens Anth. I]`, `[Dorotheus Carmen I]` Venus natural
  significations

**Note** (per codex): consider `venusian` or `attraction-led` as alternates
if "charm-driven" feels too modern; not required.

#### `modality:drive-led`

**Source status**: `direct-source`

**Definition**: Finding's mechanism operates through Mars / cut / direct
action / friction / martial force.

**Hellenistic basis**:
- `[Brennan Ch.7]`, `[Valens Anth. I]`, `[Firmicus Math. II.7]` Mars as
  action / conflict / cutting

**Note**: use when Mars is audited and relevant; not a raw Mars keyword.

### Place / angularity modality (2)

#### `modality:visible`

**Source status**: `direct-source`

**Per codex** — sub-tags may be added later: `angular`, `public`,
`heliacally-visible`.

**Definition**: Finding operates through visible / angular / public surface
(angular houses 1 / 4 / 7 / 10; visible-phase planets; heliacally visible).

**Hellenistic basis**:
- `[Brennan Ch.10, Ch.13]` angularity / visibility / manifestation
- `[Valens Anth. II]`, `[Firmicus Math. II.14-II.18]` angular vs cadent place
  quality
- `[Brennan Ch.7]` solar visibility / under-beams distinctions

**Per codex — mutex fix**: NOT absolute mutex with `hidden`. A finding can
describe a hidden mechanism manifesting through a visible / angular carrier.
Both tags may apply if mechanism + manifestation differ.

#### `modality:hidden`

**Source status**: `direct-source`

**Definition**: Finding operates through behind-the-curtain / cadent / combust
/ 12th-house register.

**Hellenistic basis**:
- `[Brennan Ch.10]` cadent / 12th / hidden themes
- `[Brennan Ch.7]` under-beams
- `[Firmicus Math. II.25]` antiscia as hidden testimony
- `[Valens Anth. II]` Bad Daimon / hidden / difficult place

**See `visible` for mutex note.**

### NEW Hellenistic operation modality (14, per codex 桶 3.4)

Core Hellenistic operations that v0.1 did not include. All 14 are
`direct-source`. (The 15th tag named in the bucket — `clustered` — is the
project-heuristic shape modality listed above under "Project-derived /
composite modality (10)" as the opposite of `distributed`; it is not a
Hellenistic doctrine and is counted separately.)

#### `modality:ruler-routed`

**Source status**: `direct-source`

**Definition**: Finding routes via topic ruler chain (e.g., 10th-ruler 2nd-
ruler chain; Asc-ruler chain).

**Hellenistic basis**: `[Brennan Ch.12-13]` ruler chains; `[Valens Anth. II]`.

#### `modality:lot-routed`

**Source status**: `direct-source`

**Definition**: Finding routes via Lot / Lot ruler (Fortune / Spirit / topic
Lots).

**Hellenistic basis**: `[Brennan Ch.16]` Lots; `[Valens Anth. IX]`
Fortune/Daimon methods.

#### `modality:configured`

**Source status**: `direct-source`

**Definition**: Finding involves aspect / configuration (sextile / square /
trine / opposition / conjunction). Distinguished from `averse`.

**Hellenistic basis**: `[Brennan Ch.9]` configuration; `[Valens Anth. III]`.

#### `modality:averse`

**Source status**: `direct-source`

**Definition**: Finding involves aversion (no sign-based aspect; 2nd / 6th /
8th / 12th from each other).

**Hellenistic basis**:
- `[Brennan Ch.9]` aversion doctrine
- `[Valens Anth. IV]` aversion in natal-relationship audit (co-presence /
  configuration / aversion / reception / place)

≥2-source: **met** (2 sources). Note: `rules/aspect-reception-rules.md` is
project implementation, not source witness.

#### `modality:received`

**Source status**: `direct-source`

**Definition**: Finding involves reception (host-guest dignity relationship;
mutual or one-way; with or without aspect).

**Hellenistic basis**: `[Brennan Ch.14]` reception doctrine; `[Valens Anth.
II-III]`.

#### `modality:bonified`

**Source status**: `direct-source`

**Definition**: Finding shows benefic bonification of significator.

**Hellenistic basis**:
- `[Brennan Ch.14]` bonification doctrine
- `[Valens Anth. II-III, VII]` benefic-testimony language modifying
  significator behavior (mixed-testimony preservation when benefic + other
  conditions co-occur)
- `[Firmicus Math. II]` benefic testimony in planet-doctrine audit

≥2-source: **met** (3 sources).

#### `modality:maltreated`

**Source status**: `direct-source`

**Definition**: Finding shows malefic maltreatment of significator.

**Hellenistic basis**:
- `[Brennan Ch.14]` maltreatment doctrine
- `[Valens Anth. II-III, VII]` malefic-testimony language harming significator
  (Saturn harshness by night / Mars by day; condition-dependent harm; injure
  / spoil verbs)
- `[Firmicus Math. II]` malefic harm / corruption / injury testimony in
  planet-doctrine audit

≥2-source: **met** (3 sources).

#### `modality:overcoming`

**Source status**: `direct-source`

**Definition**: Finding involves overcoming by sign (superior planet
overcoming inferior by 10th-sign / right-side).

**Hellenistic basis**:
- `[Brennan Ch.14]` overcoming by sign doctrine
- `[Dorotheus Carmen II]` directional looking-down / right-side square material
  (project method-targets: "preserve directionality/overcoming where Dorotheus
  distinguishes looking-down or right/left squares")

≥2-source: **met** (2 sources).

#### `modality:enclosed`

**Source status**: `direct-source`

**Definition**: Finding involves enclosure by malefics (besiegement) or
benefics (positive enclosure).

**Hellenistic basis**:
- `[Brennan Ch.14]` enclosure doctrine
- `[Firmicus Math. VI]` malefic enclosure / attack material (in difficult
  combination clusters)

≥2-source: **met** (2 sources).

#### `modality:under-beams`

**Source status**: `direct-source`

**Definition**: Finding involves planet under-beams / combust / heliacally
invisible (within 15° of Sun typically; cazimi at ≤17').

**Hellenistic basis**:
- `[Brennan Ch.7]` under-beams / combust doctrine
- `[Firmicus Math. II]` solar-phase doctrine (hidden under Sun's rays /
  emerging / eastern / western treatment)
- `[Valens Anth.]` solar-phase / visibility material in planet condition audit

≥2-source: **met** (3 sources).

#### `modality:retrograde`

**Source status**: `direct-source`

**Definition**: Finding involves retrograde planet.

**Hellenistic basis**: `[Brennan Ch.7]`; `[Valens Anth. I]`.

#### `modality:stationary`

**Source status**: `direct-source`

**Definition**: Finding involves stationary planet (station retrograde /
station direct).

**Hellenistic basis**:
- `[Brennan Ch.7]` motion / stationary doctrine
- `[Firmicus Math. II]` planet-motion audit (stationary mentioned within
  planet-doctrine condition material)
- `[Valens Anth. VI]` station / motion treatment in transit/subdistribution
  audit

≥2-source: **met** (3 sources).

#### `modality:sect-supported`

**Source status**: `direct-source`

**Definition**: Finding's planet is of-sect (Sun/Saturn/Jupiter for day chart;
Moon/Venus/Mars for night chart).

**Hellenistic basis**:
- `[Brennan Ch.7]` sect doctrine
- `[Valens Anth. I]` sect affiliation + sect-modified planetary condition
  (Rule Card on judging whether planet is "in a more congenial or contrary
  environment")
- `[Firmicus Math. II]` sect + solar phase audit (Saturn harsher by night /
  Mars harsher by day)
- `[Dorotheus Carmen I]` triplicity rulers by sect; malefics judged by sect
  context

≥2-source: **met** (4 sources).

#### `modality:contrary-sect`

**Source status**: `direct-source`

**Definition**: Finding's planet is contrary-to-sect.

**Hellenistic basis**:
- `[Brennan Ch.7]` sect doctrine (contrary-sect)
- `[Valens Anth. I]` sect-modified condition (contrary-sect planets in less
  congenial environment)
- `[Firmicus Math. II]` sect + harm intensification (Saturn harsher by night /
  Mars by day → contrary-sect harshness pattern)
- `[Dorotheus Carmen I]` malefics judged by sect context

≥2-source: **met** (4 sources).

---

## Dimension 7: question-type (open, 17 starter)

All `project-query` source status. Per codex review §"Internal Consistency" —
"These tags are not in the Hellenistic source pool, but they align with the
chart-finding-index purpose: mapping arbitrary reader questions to findings."

### `question-type:structural-fit`

Finding answers "你适合什么 (角色 / 场域 / 形态)?" Positive structural fit.

### `question-type:not-fit`

Finding answers "你不适合什么?" Specific structural negation.

**Per codex**: aligns with `rules/brief-shot-discipline.md` not-fit gate
(其 §4.1.3.2 #4 "Not-fit segment" criterion 在 technical-anchor 半仍 active;
reader 层中文 not-fit 表达走 `hellenistic-render-unguarded/rules/direct-
relational-statement.md` — 原 `translation-layer/output-rules.md` 引用
SUPERSEDED 2026-05-18 Wave 4, TL pass 已弃用).

### `question-type:direction`

Finding answers "你这阶段该往哪走?" — direction / orientation within a life
stage.

### `question-type:pace`

Finding answers "你的 X 节奏是什么?"

### `question-type:pattern`

Finding answers "你的 X 模式是什么?" **Per codex**: too broad; use as fallback
only.

### `question-type:risk`

Finding answers "你的结构性风险点 / 脆弱面是什么?" **Per codex**: define as
**broad question shape** (vs `pressure-source` which is difficulty triad
subcomponent).

### `question-type:resource-channel`

Finding answers "你的资源 / 支撑从哪里来?"

### `question-type:transformation-window`

Finding answers "什么 (结构) 窗口允许什么转化?" **Structural** window; for
practical "何时" timing queries use `timing-when` instead.

### `question-type:relationship-form`

Finding answers "关系应该是什么形式?"

### `question-type:livelihood-pathway`

Finding answers "生计 / 钱该走什么路径?"

### `question-type:skill-form`

Finding answers "你应该用什么形态的技能?"

### `question-type:self-shape`

Finding answers "你是个什么样的人?"

### `question-type:formative-arc`

Finding answers "你的形成期质感是什么?"

### `question-type:pressure-source`

Finding answers "压力 / 难处的来源是什么?" **Per codex**: difficulty triad
subcomponent (must pair with `polarity:difficulty` finding).

### `question-type:mitigation-channel`

Finding answers "缓解 / 承载困难的通道是什么?" Difficulty triad subcomponent.

### `question-type:choice-support` (NEW per codex)

Finding answers "我该选 X 还是 Y?" — decision-support / choice queries.

### `question-type:timing-when` (NEW per codex)

Finding answers "什么时候?" — practical timing query (distinct from
`transformation-window` which is structural window). Pair with `modality:
timing-conditional` + appropriate `timing-activation:*` tag.

---

## Dimension 8: subject-discipline (closed, 7)

Anti-cookbook discipline: every life-claim sentence's grammatical subject
type. Mirror of `rules/delineation-output-rules.md` §"Anti-Cookbook Rules".

### `subject-discipline:person-state`

**Source status**: `project-output-discipline`

Finding statement subject = the native / a person / a felt state. **Default**;
required for life-claim findings.

### `subject-discipline:domain`

**Source status**: `project-output-discipline`

Finding statement subject = a domain / 场域 / arena.

### `subject-discipline:mode`

**Source status**: `project-output-discipline`

Finding statement subject = a mode / pattern / mechanism.

### `subject-discipline:relation`

**Source status**: `project-output-discipline`

Finding statement subject = a relationship between things.

### `subject-discipline:structure`

**Source status**: `project-output-discipline`

Finding statement subject = a structural fact / 配置 itself.

**Per codex** — critical clarification: this tag is **allowed only for
non-life-claim descriptive findings** (typically `polarity:structural`).
Cannot be used as a loophole to let chart factors be subjects of life claims.

### `subject-discipline:event` (NEW per codex)

**Source status**: `project-output-discipline`

Finding statement subject = a timing event window or event class. Use for
timing-conditional findings that describe events rather than person-states.

### `subject-discipline:question` (NEW per codex)

**Source status**: `project-output-discipline`

Entry subject = unresolved reader-context question (not a finding itself).
For chart-finding-index entries that name a question pending reader life-
context to narrow.

---

## Cross-tag relationships (revised per codex review)

### Co-occurrence patterns (common)

- `polarity:difficulty` + `modality:structured` + `topic:learning` →
  Saturn-on-mind findings
- `polarity:strength` + `modality:integration` + `topic:chart-signature` →
  Lord-of-geniture / integration-manager findings
- `polarity:mixed` + `confidence:mixed-high` + `topic:character` →
  paradox-Moon-type findings (strength + difficulty co-located)
- `modality:aversion-reception` + `topic:partnership-marriage` →
  mutual-reception-in-aversion relational findings
- `modality:timing-conditional` + `timing-activation:zr-l1` → ZR-L1-specific
  findings

### Mutually exclusive (do not co-occur)

- `polarity:strength` + `polarity:difficulty` — use `polarity:mixed` instead
- `confidence:speculative` + `polarity:difficulty` — speculative findings
  symbolic-only, cannot carry difficulty-grade structural impact

### NOT mutually exclusive (per codex revision)

- ~~`modality:visible` + `modality:hidden`~~ — **per codex, NOT absolute
  mutex**. A finding can describe a hidden mechanism manifesting through a
  visible / angular carrier. Both tags may apply when mechanism + manifestation
  differ. If both are central without that interpretation, decompose finding
  into two.

### Required pairings

- `polarity:mixed` typically requires `confidence:mixed-high`; **per codex**:
  if only moderate-grade mixed evidence, use `confidence:moderate +
  polarity:mixed` instead of forcing high label.
- `polarity:tension` requires ≥ 2 component finding refs in
  `related-findings`.
- `polarity:difficulty` requires pressure + mitigation + channel triad in
  finding body.
- `modality:timing-conditional` **requires a non-`none` `timing-activation:*`
  tag** (per codex v2 wording fix — `timing-activation:none` is the schema
  shim marking non-timing-conditional findings, so pairing
  `modality:timing-conditional + timing-activation:none` is contradictory and
  not permitted. Critical fix from v0.1 which paired with generic
  `life-stage:*-conditional`). May additionally carry `age-band:*` for query
  convenience.
- `question-type:pressure-source` and `question-type:mitigation-channel`
  typically pair on the same difficulty finding (two sides of same coin).

---

## Codex verification status (v2.0)

Per codex review (saved at `v2.3-tag-inventory-codex-review.md`):

| Patch list item | Status in v2.0 |
|---|---|
| 1. Add Source status legend per tag | **applied** (every tag carries `Source status` field) |
| 2. Renames (love-marriage / occult / force-pattern / back-channel) | **applied** (full adoption per practitioner decision) |
| 3. Split Dimension 4 (age-band + timing-activation) | **applied** (full split) |
| 4. Split `l2-loy-conditional` | **applied** (now `timing-activation:zr-l2` + `timing-activation:lord-of-year`) |
| 5. Move `topic:timing` out | **applied** (timing now Dim 5 timing-activation; removed from topic) |
| 6. Add missing topic tags (children / siblings / friends-benefactors / illness / death / longevity) | **applied** (6 extension topics added) |
| 7. Add missing modality tags (14 Hellenistic operations + `clustered`) | **applied** (14 direct-source operations added + 1 project-heuristic shape tag `clustered`) |
| Per-tag wording fixes | **applied** (career / wealth / learning / mixed / mixed-high / structure / etc.) |
| Cross-tag relationship fixes | **applied** (visible/hidden mutex relaxed; timing-conditional partner required to be non-`none` timing-activation) |

**Bottom line per codex (v1 review)**: "Once Dimension 4 is split and the
project-composite labels are made explicit, the inventory should be safe to
use as the chart-finding-index tag system." — v2.0 meets both criteria.

## Codex v2 regression status (v2.1)

Per codex v2 regression review (saved at
`v2.3-tag-inventory-codex-review-v2.md`):

| Finding | Status in v2.1 | Trace |
|---|---|---|
| F1: Tag-count arithmetic inconsistent (99 vs 101) | **fixed** | Frontmatter + provenance summary unified to Total = 101 with note "99 non-shim/non-derived operational tags" |
| F2: `clustered` counted in incompatible ways | **fixed** | `clustered` remains `project-heuristic` shape modality (opposite of `distributed`); Hellenistic-operation bucket label and glossary rephrased to "14 direct-source operations + 1 project-heuristic shape tag" |
| F3: Source-status hybrid labels | **fixed** | `topic:learning` → `project-composite`; `topic:chart-signature` → `source-components`; `modality:timing-conditional` → `source-components`. Added Component status / Assembly note fields where applicable. |
| F4: Timing tags mix source existence with implementation readiness | **fixed** | Added `Implementation status` field for timing tags. `solar-revolution` = deferred; `monthly-lord` / `daily-lord` / `planetary-years` = needs-reconciliation; `climacteric` / `four-stakes` = source-record-only. `longevity` topic also carries deferred status. |
| F5: Hellenistic operation modality citations weak | **fixed** | `averse` / `bonified` / `maltreated` / `overcoming` / `enclosed` / `under-beams` / `stationary` / `sect-supported` / `contrary-sect` each strengthened with second/third witness from Valens / Firmicus / Dorotheus extractions. `rules/aspect-reception-rules.md` removed from "Hellenistic basis" lines on direct-source tags (it is project implementation, not source witness). |
| F6: Extension topic Lots phrased too strongly | **fixed** | `children` / `siblings` / `friends-benefactors` / `illness` topics now mark their topic Lots as `[Source-only candidate, formula-deferred]` per `lots-and-fortune.md`. `death` topic citation tightened with specific Valens / Firmicus / Dorotheus pointers. `longevity` topic citation corrected (Brennan Ch.17 miscitation replaced with topic-modules provenance chain). |
| Wording fix: `timing-conditional` requires non-`none` `timing-activation` | **fixed** | Cross-tag relationship wording updated to explicitly require non-`none` partner, preventing contradictory `timing-conditional + timing-activation:none` pair. |

**Per-bucket per codex v2** (not codex v2 blockers but logged for future):

- `counteracted` modality remains absent; `aspect-reception-rules.md`
  Counteraction section exists. Optional future addition.
- `angular` / `cadent` remain folded into `visible` / `hidden`. Acceptable for
  starter; can split if query precision demands.
- `mercurial` / `solar` / `lunar` natural-modality tags remain absent
  (Saturn/Jupiter/Venus/Mars exist). Optional future ergonomic addition.

**Bottom line per codex v2**: "v2.0 ready as canonical after metadata/source-
status cleanup; no structural redesign required." — v2.1 implements that
cleanup.

---

## Provenance summary (v2.1)

Counts use the normalized one-primary-status-per-tag convention from v2.1.

| Dimension | Tag count | direct-source | source-components | project-composite | project-heuristic | project-query | project-output-discipline |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 topic | 15 | 13 | 1 (chart-signature) | 1 (learning) | 0 | 0 | 0 |
| 2 polarity | 5 | 0 | 0 | 0 | 0 | 0 | 5 |
| 3 confidence | 5 | 0 | 0 | 0 | 0 | 1 (mixed-high) | 4 |
| 4 age-band | 5 | 0 | 0 | 0 | 5 | 0 | 0 |
| 5 timing-activation | 17 | 16 | 0 | 0 | 0 | 0 | 1 (none) |
| 6 modality | 30 | 21 | 1 (timing-conditional) | 3 (integration / aversion-reception / depth) | 5 (load-bearing / network / self-authorized / distributed / clustered) | 0 | 0 |
| 7 question-type | 17 | 0 | 0 | 0 | 0 | 17 | 0 |
| 8 subject-discipline | 7 | 0 | 0 | 0 | 0 | 0 | 7 |
| **Total** | **101** | **50 (49.5%)** | **2 (2%)** | **4 (4%)** | **10 (9.9%)** | **18 (17.8%)** | **17 (16.8%)** |

v0.1 → v2.0: total tag count 58 → 101 (+43); 14 new Hellenistic operations as
direct-source; project-* tags more cleanly labeled per source status.

v2.0 → v2.1: structural counts unchanged (still 101); source-status
normalization reduced two hybrid labels to single primary values, moving
`topic:chart-signature` and `modality:timing-conditional` from
`direct-source`/`direct-source-mix` into `source-components`.

---

## Glossary (slug quick-look)

**topic (15)**:
Default 9: `character` / `career` / `partnership-marriage` / `family` /
`learning` / `wealth` / `divination-spirituality` / `body` / `chart-signature`
Extension 6: `children` / `siblings` / `friends-benefactors` / `illness` /
`death` / `longevity`

**polarity (5)**: `strength` / `difficulty` / `mixed` / `structural` /
`tension`

**confidence (5)**: `high` / `moderate` / `low` / `speculative` / `mixed-high`
(derived query tag)

**age-band (5)**: `age-0-12` / `age-12-24` / `age-25-40` / `age-40-60` /
`age-60-plus`

**timing-activation (17)**: `annual-profection` / `lord-of-year` /
`activated-place` / `activated-tenant` / `zr-l1` / `zr-l2` / `peak-period` /
`loosing-of-bond` / `solar-revolution` / `transit-trigger` / `monthly-lord` /
`daily-lord` / `chronocrator` / `climacteric` / `planetary-years` /
`four-stakes` / `none`

**modality (30)**:
Project-derived (10): `integration` / `load-bearing` / `network` /
`self-authorized` / `aversion-reception` / `depth` / `distributed` /
`clustered` / `partnership-routed` / `timing-conditional`
Planet-nature (4): `structured` / `expansive` / `charm-driven` / `drive-led`
Place / angularity (2): `visible` / `hidden`
Hellenistic operation (14): `ruler-routed` / `lot-routed` / `configured` /
`averse` / `received` / `bonified` / `maltreated` / `overcoming` / `enclosed`
/ `under-beams` / `retrograde` / `stationary` / `sect-supported` /
`contrary-sect`

**question-type (17)**: `structural-fit` / `not-fit` / `direction` / `pace` /
`pattern` / `risk` / `resource-channel` / `transformation-window` /
`relationship-form` / `livelihood-pathway` / `skill-form` / `self-shape` /
`formative-arc` / `pressure-source` / `mitigation-channel` / `choice-support`
/ `timing-when`

**subject-discipline (7)**: `person-state` / `domain` / `mode` / `relation` /
`structure` / `event` / `question`

---

> **Inventory v2.1 canonical.** v2.0 (codex-review-applied) was found
> structurally sound by codex v2 regression but flagged 6 metadata/source-
> status issues (F1-F6) + 1 wording fix; v2.1 applies that cleanup. Per codex
> v2 explicit target: "v2.0 ready as canonical after metadata/source-status
> cleanup; no structural redesign required" — v2.1 is the canonical
> chart-finding-index tag vocabulary for v2.3 architecture.
>
> Further codex regression is optional. Future v-bumps should preserve the
> one-primary-status-per-tag convention and the timing tag Implementation
> status field; if structural changes are needed, run another codex pass
> with explicit per-tag verification.
