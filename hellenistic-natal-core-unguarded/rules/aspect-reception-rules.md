# Aspect And Reception Rules

> Last v2.x change: 2026-05-16 (v2.2 Plan A.1) — added Reception Detection Procedure section (additive). Existing rules unchanged. Cross-reference gate to `rules/dignities-reference.md` mandatory per audit feedback from `samples/topic-reading-template.md` iteration.

Purpose: determine whether chart factors can see or act upon one another, who has the stronger position, whether the contact is active, and whether reception mitigates or amplifies the contact.

This file is not a modern aspect cookbook. It is the relationship and testimony layer used after significators are selected.

## Core Questions

```text
Are the significators configured by sign?
Are they in aversion?
Is there close degree-based contact?
Which planet has superior position or overcomes?
Is the contact applying, exact, or separating?
Is the acting planet benefic, malefic, or mixed?
Is the acting planet in good condition?
Is there reception?
```

## Witnessing First

In the Hellenistic frame, a configuration first answers whether two planets can witness or testify to one another.

- Configured signs: direct testimony exists.
- Aversion: no direct testimony.
- Degree-based exactness: testimony is sharper, more active, and more operational.

Guardrail: do not blend two planets as a direct relationship if they cannot witness each other, unless another rule supplies the link.

## Sign-Based vs Degree-Based

```text
Sign-based configuration = baseline ability to see/testify.
Degree-based contact = intensified and more precise testimony.
```

Use sign-based relationships for the first chart map. A sign-based configuration remains operative regardless of degree orb; degree closeness intensifies testimony but does not gate whether the configuration is valid. Source: `[Brennan Ch.9]`, printed pp. 296-304.

Sign-based configuration determines aspect family exclusively. If degree-based proximity to a non-sign-aligned aspect is flagged, for example software reports an out-of-sign square or trine, ignore the degree-based family shift and use the sign-based aspect. Treat the degree proximity as background information about angular separation only, not as an aspect classifier. Source: `[Brennan Ch.9]`, printed pp. 296-304.

Do not import a medieval or modern orb gate into the first Hellenistic sign-based map. If the degrees are wide, mark the testimony as sign-based or background-weight, but do not erase it.

## Configuration Types

| Configuration | Basic use |
|---|---|
| Conjunction | co-presence, bodily mixing, shared place |
| Sextile | cooperative contact, weaker than trine |
| Square | conflict, action, pressure; direction matters |
| Trine | support, flow, protection, ease |
| Opposition | confrontation, separation, polarity, externalization |
| Aversion | lack of direct witnessing; weak or absent contact |

## Aversion

Aversion means the planets or places do not directly see one another by the recognized configurations.

When aversion appears between important significators:

1. Mark lack of direct contact.
2. Search for indirect links: domicile rulership, reception, Lot, time lord, translation/collection in horary, or co-activation.
3. If no indirect link exists, keep the conclusion weak or unresolved.

## Overcoming

Do not treat all aspects as symmetrical.

When one planet is in the superior/right-hand position relative to another, it has stronger acting power. A benefic overcoming can strongly support. A malefic overcoming can strongly pressure or maltreat.

v1 implementation boundary: evaluate direction only for hard testimony. For squares, compute overcoming/superior position. For oppositions, record direct confrontation/polarity as hard testimony without assigning a trine/sextile-style superior side. For trine and sextile, record `superiority not evaluated in v1` and judge the testimony by witnessing, degree closeness, planet condition, and reception. `[project heuristic]`

Operational prompt:

```text
Which planet is acting more forcefully on the other?
Is the actor benefic/malefic/neutral?
Is the actor in good condition?
Is there reception?
```

## Bonification / Maltreatment

| Condition | Working reading |
|---|---|
| Benefic configured to significator | support, help, protection, opportunity |
| Malefic configured to significator | pressure, damage, delay, severance, burden |
| Benefic of sect and strong | stronger support |
| Malefic contrary to sect and strong | stronger harm |
| Weak benefic | wants to help but may not deliver fully |
| Mitigated malefic | difficulty becomes structured, useful, or survivable |

## Enclosure

A planet enclosed by benefics is protected or supported. A planet enclosed by malefics is trapped, pressured, or strongly constrained. Mixed enclosure requires a mixed judgment.

Use caution with exact degree standards until cross-checked against additional sources.

## Counteraction

If a planet is ruled by a badly placed malefic, its host can indirectly harm or obstruct it. Audit the domicile lord, not only direct aspects.

## Close Testimony

Close degree-based contact generally matters more than loose sign-based contact, especially in event-like questions.

When judging unfolding events, distinguish:

- applying: contact forming;
- separating: contact already past;
- exact: peak contact;
- no application: no direct perfection unless another technique supplies it.

## Reception

Reception occurs when a planet is in another planet's dignity and that host has a relationship with it.

Use reception to answer:

```text
Is the planet welcomed, hosted, integrated, protected, or at least understood by the other planet?
```

Effects:

- harmful testimony with reception: softened, structured, or made less destructive;
- benefic testimony with reception: strengthened or made more usable;
- no reception: raw contact, less integration;
- hostile or absent support: less mitigation.
- Mutual non-hosting: when each planet sits in the other's adversity/exile sign, treat the pair as configured without positive reception and note the mutual debility. If the configuration is soft, the contact remains soft by configuration but operates without integration in either direction. `[project heuristic]`

## Output Template

```text
Planet A:
Planet B:
Sign-based relationship:
Degree-based closeness:
Witnessing or aversion:
Direction/superiority:
Applying or separating:
Reception:
Benefic/malefic quality:
Result for the topic:
Confidence:
```

## Guardrails

- Do not infer an event from an aspect alone; connect it to significators and topic houses.
- Do not ignore witnessing, aversion, directionality, or reception.
- Do not treat malefic contact as automatically fatal or benefic contact as automatically successful.
- Always return to the chart focus and topic hierarchy.

## Source Status

Initial skeleton distilled from Brennan chapters 9 and 14. v1 is locked after the case-03 sign-based aspect-family clarification; later cross-check against Demetra George and primary sources remains post-v1 source work.

## Reception Detection Procedure (v2.2 additive)

> v2.2 Plan A.1 additive. The existing `## Reception` section above remains the conceptual definition and effects layer; this section adds an explicit deterministic detection procedure so that reception judgment is not produced by implicit / memory-based reasoning. The cascade evidence motivating this section is `cases/case-06.md` (one-way Saturn-hosts-Venus was at risk of being read as mutual reception in downstream narrative, demonstrating that even a single reception mis-detection propagates through topic synthesis).
>
> **Mandatory cross-reference gate**: every dignity lookup inside this procedure — domicile ruler, exaltation ruler, triplicity rulers by sect, Egyptian bound ruler at a degree, decan ruler at a degree — must be performed by directly reading the corresponding table in `rules/dignities-reference.md`. Do **not** rely on memory for any of these lookups. Each step in the procedure below names the specific `dignities-reference.md` table to consult.
>
> **Language convention (v2.2 architecture)**: this procedure's output — the Reception Network table — is part of Stage 1 deterministic data. Stage 1 / Stage 2 (topic modules) / Stage 3 (synthesis) analysis output is **written in English** — internal evidence chaining and technical terminology (reception, dignity, configuration, aversion, etc.) are more precise in English, and avoiding mid-thought Chinese/English switching reduces friction and term ambiguity. The Translation Layer (TL) pass renders the reader-facing deliverable in **full Chinese**, with brief-shot category names (industries / relationship types / scenario classes / study styles / family dynamics) localized; in-prose evidence citations may keep technical terms in English inside parentheses. Existing cases (`case-01` through `case-06a`) retain their historical mixed-language form unchanged. This convention applies to new readings produced under the v2.2 stage-based architecture; the cross-section sticky version lives in AGENTS.md / method-index.md (reserved for a later housekeeping plan).

### Reception Type Taxonomy

Five reception types are recognized. Each type is detected separately; do not collapse them into a single "reception" flag.

**Type 1 — Domicile reception.**

- Planet P (in sign S) is **received-by-domicile** by planet Q **if** Q is the domicile ruler of S. (Lookup: `rules/dignities-reference.md` → "Domicile Rulers By Sign" row for S.)
- **Mutual reception by domicile**: P in S (which is Q's domicile) **AND** Q in T (which is P's domicile). Both directions must be true.
- Example: Venus in Pisces (Jupiter's domicile) and Jupiter in Libra (Venus's domicile) = mutual reception by domicile.

**Type 2 — Exaltation reception.**

- Planet P (in S) is **received-by-exaltation** by Q **if** Q is the exaltation ruler of S. (Lookup: `rules/dignities-reference.md` → "Planetary Dignity And Debility By Planet", Exaltation column.)
- Only seven signs have an exaltation ruler (Aries-Sun, Taurus-Moon, Cancer-Jupiter, Virgo-Mercury, Libra-Saturn, Capricorn-Mars, Pisces-Venus); the other five generate no exaltation reception.
- **Mutual reception by exaltation**: P in S (Q's exaltation sign) AND Q in T (P's exaltation sign), both directions.
- **Self-exaltation is NOT a reception relation with another planet.** P in its own exaltation sign (e.g., Venus in Pisces, Sun in Aries, Moon in Taurus) records as a **dignity field** on P's per-planet audit ("Venus has own exaltation"), **not** as a row in the Reception Network. Do not mis-flag self-exaltation as "mutual reception" (see anti-pattern 1 below).

**Type 3 — Triplicity reception.**

- Triplicity rulers vary by chart sect; consult `rules/dignities-reference.md` → "Triplicity Rulers By Sect" with the chart's sect declared explicitly.
- Three rulers per triplicity per sect (primary / secondary / cooperating). When P is in sign S, record each tier separately:
  - "P received-by-triplicity-primary of Q"
  - "P received-by-triplicity-secondary of R"
  - "P received-by-triplicity-cooperating of W"
- Mutual reception by triplicity follows the same reciprocal-direction logic, evaluated **per tier** (primary mutual is distinct from secondary mutual).

**Type 4 — Bound reception.**

- Planet P (in sign S, at degree D) is **received-by-bound** by Q **if** Q rules the Egyptian bound interval `[a,b)` containing D in S. (Lookup: `rules/dignities-reference.md` → "Egyptian Bounds" row for S; identify the half-open interval containing D.)
- Bound reception requires **exact degree**. Do not infer bound reception from sign-only or rounded placements (per `rules/dignities-reference.md` → "Data Conventions").
- Mutual reception by bound is rare; if asked, evaluate by the same reciprocal-direction logic.

**Type 5 — Decan reception.**

- Planet P (in sign S, at degree D) is **received-by-decan** by Q **if** Q rules the decan containing degree D in S. (Lookup: `rules/dignities-reference.md` → "Decans / Faces" row for S; identify which of `[0,10)`, `[10,20)`, `[20,30)` contains D.)
- Same exact-degree requirement as Type 4.
- Decan reception is the lowest-weight tier; treat as background unless a specific technique elevates it.

### Detection Procedure (step-by-step)

**Per-planet pass.** For each planet P in the chart:

1. Read P's sign S and exact degree D from the chart input. If D is missing or sign-only, mark Type 4 (bound) and Type 5 (decan) lookups as `degree-required: skip` for P.
2. Look up all five dignity tiers for P's position by **cross-referencing `rules/dignities-reference.md` directly**:
   - **Domicile ruler of S** → "Domicile Rulers By Sign" row for S. Record as "P received-by-domicile of Q".
   - **Exaltation ruler of S (if any)** → "Planetary Dignity And Debility By Planet", Exaltation column. Record as "P received-by-exaltation of R" (or note "no exaltation ruler for S" for the five signs without one).
   - **Triplicity rulers of S (by chart sect)** → "Triplicity Rulers By Sect" row for S's element; select the day-or-night column matching the chart. Record primary / secondary / cooperating separately, naming the sect used.
   - **Bound ruler at D in S** → "Egyptian Bounds" row for S; locate `[a,b)` containing D. Record as "P received-by-bound of Q".
   - **Decan ruler at D in S** → "Decans / Faces" row for S; locate `[0,10)` / `[10,20)` / `[20,30)` containing D. Record as "P received-by-decan of Q".
3. **Self-reception filter.** Whenever the ruler identified at any tier is P itself (P in its own domicile / own exaltation / own triplicity tier / own bound / own decan), record this as **"P has own X dignity"** in the dignity field. Do **not** generate a reception **relation** between P and itself; do **not** carry the self-reception forward as a candidate for mutual reception with any other planet.

**Pair pass.** For each unordered pair of planets (P, Q):

4. **Mutual reception check (per dignity tier independently)**:
   - **If** P is received by Q at tier X (P sits in Q's X-dignity) **AND** Q is received by P at tier X (Q sits in P's X-dignity), then **mutual reception by X** holds for the pair (P, Q).
   - Evaluate each of the five tiers separately. Mutual reception in one tier does **not** imply mutual reception in another tier; do not collapse across tiers.
5. **One-way flag.** If P is received by Q at tier X but the reciprocal (Q received by P at tier X) does **not** hold, record as **"one-way reception: P received by Q at tier X"**. Do not describe this as "mutual" and do not invert the direction (see anti-pattern 3 below).
6. **Aversion + reception annotation.** For every reception relation logged in steps 4–5, also note whether the two planets are configured by sign or in aversion (cross-reference the chart's aspect / configuration table). The Reception Network must distinguish reception-WITH-configuration from reception-WITHOUT-configuration (aversion). See §"Aversion + Reception Handling" below for the four-cell matrix.

**Output.** Produce a Reception Network table per `samples/topic-reading-template.md` §2.2 format. Minimum columns:

| From planet (in) | To planet (host of sign) | Reception type | Mutual? | Aversion or aspect? | Notes |

Self-dignities (own-domicile, own-exaltation, etc.) belong on the per-planet audit table (`samples/topic-reading-template.md` §2.1), not in the Reception Network.

### Common Detection Errors (anti-patterns)

The following patterns are **incorrect** detections; each has produced cascade errors in prior reading work and must be guarded against during the procedure above.

**Anti-pattern 1 — Treating self-exaltation as mutual reception.**

> Wrong: "Venus in Pisces and Venus rules Pisces by exaltation, so this is mutual reception by exaltation."
>
> Why wrong: Venus in Pisces = Venus in **its own** exaltation sign. That records as a **dignity field** on Venus's audit row ("Venus has own exaltation"), not as a **reception relation** between Venus and another planet. A reception relation requires **two different planets**, one in the other's dignity. Self-exaltation has no counterparty.
>
> Correct handling: record "Venus has own exaltation in Pisces" on Venus's per-planet audit; do **not** add a row to the Reception Network for this. (See `samples/topic-reading-template.md` §2.2 — Venus's self-exaltation in Pisces is explicitly marked "n/a (self-reception by exaltation = own exaltation status, not reception with another planet)".)

**Anti-pattern 2 — Treating one-way reception as mutual without checking the reciprocal direction.**

> Wrong: "Saturn in Scorpio is in Mars's domicile, so mutual reception between Saturn and Mars."
>
> Why wrong: Mutual reception requires **both** directions. Saturn in Mars's domicile (Scorpio) is reception **only if** Mars is also in Saturn's domicile (Capricorn or Aquarius). If Mars is in Aries (its own house), then Mars is **not** in any of Saturn's houses, so the reception is **one-way** (Mars receives Saturn), not mutual.
>
> Reference cascade case from `cases/case-06.md`: Venus is in Capricorn (Saturn's domicile), so **Saturn hosts / receives Venus by domicile**. Saturn is in Pisces (Jupiter's domicile), so Saturn is in **none of Venus's houses** (Taurus or Libra). The reciprocal therefore fails; the relation is **one-way (Saturn receives Venus by domicile)**, not mutual. Mis-reporting this pair as mutual reception cascades into downstream interpretation that implicitly treats Venus as also hosting Saturn — which the dignity tables do not support — and the error propagates into every topic module that reads Venus-Saturn as a "two-way managerial integration".
>
> Correct handling: always run step 4 (mutual check) explicitly by looking up **both** planets' sign rulerships against the partner; never infer reciprocity from one direction alone.

**Anti-pattern 3 — Confusing the "receives" direction.**

> Wrong: "Venus is in Capricorn, so Venus receives Saturn."
>
> Why wrong: The host of the sign **receives** the guest. P sitting in Q's house means **Q receives P**, not the other way around. The planet in the foreign sign is the **received** party (guest); the dignity ruler of that sign is the **receiver** (host).
>
> Mnemonic: guest in host's house — the **host** is the one doing the receiving. The planet that "is in another planet's house" is the **guest** being hosted, not the host doing the hosting.
>
> Correct phrasing for the Venus-in-Capricorn / Saturn-in-Pisces example (per case-06): "Saturn receives Venus by domicile (Venus is in Saturn's house Capricorn)" and separately "Jupiter receives Saturn by domicile (Saturn is in Jupiter's house Pisces)". Two distinct one-way receptions, two distinct pairs, no mutual reception between any of them.

**Anti-pattern 4 — Skipping the aversion-plus-reception annotation.**

> Wrong: reporting "Venus and Jupiter mutual reception by domicile" without flagging that they are in aversion by sign.
>
> Why wrong: Mutual reception **with** sign-based aspect and mutual reception **without** aspect (aversion) operate differently in synthesis. Without the annotation, downstream readers treat the reception as a direct active channel when it is actually an indirect back-channel relation between the two planets' houses. The synthesis pressure is structurally different in the two cases.
>
> Correct handling: see "Aversion + Reception Handling" immediately below; every reception row must carry the aspect / aversion annotation per step 6.

### Aversion + Reception Handling

Reception and configuration are **independent** axes; both must be evaluated for every reception pair, and the combination must be flagged explicitly in the Reception Network. The four cells are:

| Configuration | Reception | Working reading |
|---|---|---|
| Aspect by sign | Mutual reception | Direct contact integrated on both sides; reception modulates the aspect per the main `## Reception` section above |
| Aspect by sign | One-way reception | Direct contact integrated on the host's side only; guest is welcomed by host but does not reciprocate |
| Aversion | Mutual reception | "Managers know each other but cannot act directly" — back-channel structural support between the two planets' domains, no direct aspect-mediated testimony |
| Aversion | One-way reception | Host's domain provides structural support to guest, but the two cannot see each other directly; lightest of the four cells |

**Canonical example of mutual reception WITHOUT configuration** (per `samples/topic-reading-template.md` §2.2): Venus in Pisces 14° and Jupiter in Libra 28°. Pisces to Libra by sign = 6 inclusive backward = **aversion**. Yet Venus is in Jupiter's domicile (Pisces) and Jupiter is in Venus's domicile (Libra) → **mutual reception by domicile**. The pair is therefore mutual reception **without** configuration — operative as a back-channel hosting between the relevant houses (9 and 4 in that chart), without direct aspect-mediated testimony. Stage 2 / synthesis must treat this distinctly from a mutual reception that is also a sign-based aspect.

**Canonical example of one-way reception WITHOUT configuration** (per `samples/topic-reading-template.md` §2.2): Saturn in Scorpio 12° and Mars in Aries 7°. Aries to Scorpio = 6 inclusive backward = **aversion**. Saturn in Mars's domicile (Scorpio) but Mars in own domicile (Aries, not Saturn's) → one-way: Mars receives Saturn by domicile. Mars hosts Saturn but cannot see Saturn; the host's domain provides background support without direct testimony exchange.

### Provenance

- Reception baseline doctrine: `[Brennan Ch.14]`.
- Reception in audit context: `[Valens *Anth.* II]`.
- Combined planet condition audit including reception application: `[Firmicus *Math.* II.27-29]`.
- Reception in chart judgment: `[Dorotheus *Carmen* I via 'Umar al-Tabari → Dykes 2017]`.
- Step-by-step detection procedure, mandatory cross-reference gate to `rules/dignities-reference.md`, anti-pattern enumeration, and the four-cell aversion+reception matrix: `[project heuristic]` — structural algorithm derived from project audit work (the `cases/case-06.md` cascade analysis and the `samples/topic-reading-template.md` §II.2.2 reception-table iteration), not directly excerpted from any single source.
