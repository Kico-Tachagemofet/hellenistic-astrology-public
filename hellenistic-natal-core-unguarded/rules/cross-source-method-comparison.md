# Cross-Source Method Comparison

> This file is a reference companion, not part of the reading workflow.

This file registers positions held by Brennan, Valens, Firmicus, and Dorotheus
on selected method points where the four sources diverge or where one source
adds material outside v1's Brennan baseline. **It does not modify any v1
rule** — v1 still uses Brennan as baseline. This file is a query aid: when a
reader wants to know what the other three say about a v1 rule, they look here.

Provenance discipline: each position carries section/chapter plus page or
verse reference. `[project heuristic]` marks the cross-source-comparison
form itself as a project heuristic; the underlying source positions are
attributed to their sources.

Created 2026-05-15 as part of v2.1 Phase B; populated initially from B.1
flag decisions and B.0 triage. `reading-workflow.md` is **not modified**
and does not reference this file at runtime.

## Method Comparison Index

1. Mercury sect determination
2. Daemon / Fortune (Spirit) formulas — Firmicus Bram printed anomaly
3. Chart ruler method
4. Dignity weighting order
5. Leo third decan (OCR vs Chaldean order)
6. Triplicity rulers ordering (by sect)
7. Listening / Beholding signs (rising-time affinity)
8. Solar revolutions calculation
9. Monthly / chronocrator lord methods
10. Planet-specific matutine / vespertine thresholds
11. Moon application / separation / void doctrine
12. Fortune ruler stack
13. Saturn-by-sect rulership resonance vs condition weakening
14. Parental house doctrine (4 vs 10 — which place reads father / mother / unified)

---

## 1. Mercury sect determination

**v1 baseline (`planet-condition-audit.md`)**: visibility-based + `undeclared`
boundary (Mercury within ~15° of Sun → likely under-rays; sect leaning by
visibility direction; below visibility threshold → `undeclared`). Source:
`[Brennan Ch.7]`, printed pp. 190-191, 205-206. Case-02 (<15° side) and
case-03 (>15° side) implementation-tested.

**Brennan**: visibility-based; Mercury's sect depends on phase relative to
Sun (morning star → diurnal lean; evening star → nocturnal lean; under
rays → undeclared until visible). `[Brennan Ch.7]`, pp. 190-191, 205-206.

**Valens**: sect-conditioned but not categorical; Mercury participates in
both sect bodies depending on configuration and place. `[Valens *Anth.* I]`
(Mark Riley trans.) — sect language is contextual.

**Firmicus**: directly assigns Mercury to the nocturnal condition.
`[Firmicus *Math.* II.7]` Bram printed.

**Dorotheus**: visibility/phase-conditioned; treats Mercury's day/night
character via eastern/western station and under-rays state.
`[Dorotheus *Carmen* I via 'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). Brennan + Dorothean + Valens cluster around
visibility-based / conditional treatment; Firmicus's direct nocturnal
assignment is single-source. v1 retains visibility-based default.

**Reason**: ≥3 sources support the conditional/visibility model; Firmicus's
categorical assignment is a notable variant but not the majority position.

---

## 2. Daemon / Fortune (Spirit) formulas — Firmicus Bram printed anomaly

**v1 baseline (`lots-and-fortune.md`)**: Fortune and Spirit are distinct
day/night-reversed Lots.

- Fortune: day Asc + Moon − Sun; night Asc + Sun − Moon.
- Spirit: day Asc + Sun − Moon; night Asc + Moon − Sun.

Source: `[Brennan Ch.16]`, printed pp. 521-522, 525.

**Brennan**: day-night reversal; Fortune and Spirit distinct. `[Brennan
Ch.16]`, pp. 521-522, 525.

**Valens**: Fortune and Daimon distinct; both day-night-distinct. Used as
primary derived anchors throughout Bk.IX (Fortune-Daimon-Ascendant
methods). `[Valens *Anth.* IX]`.

**Firmicus**: Fortune in Bk.IV.17 and Daemon/Spirit in Bk.IV.18. The Bram
printed text for Daemon **appears to repeat the Fortune formula**.
`[Firmicus *Math.* IV.17-18]` Bram printed. **`needs verification`**: this
is likely a transmission / OCR artifact, since Brennan + Valens + the
Dorothean tradition all give distinct day/night-reversed formulas. Bram
translator notes and original Latin should be consulted to resolve.

**Dorotheus**: Fortune used as major status/assets anchor, day/night-
reversed per Brennan Ch.16 attribution. `[Dorotheus *Carmen* I.27-28 via
'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). v1 keeps the distinct day/night-reversed
formulas. Phase B.3 added a cross-ref note to `lots-and-fortune.md` flagging
the Firmicus Bram irregularity.

**Reason**: 3 of 4 sources give distinct formulas; the Firmicus anomaly is
flagged for future verification but does not override majority position.

---

## 3. Chart ruler method

**v1 baseline (`significator-hierarchy.md`)**: Ascendant ruler is the
primary chart significator; the Whole-life / character focus row anchors on
Ascendant + Ascendant ruler. Source: `[Brennan Ch.12]`, printed pp. 397-411.

**Brennan**: Ascendant ruler (domicile lord of the rising sign) is the
primary chart significator. `[Brennan Ch.12]`.

**Valens**: uses an Ascendant–Fortune–Lot three-way comparison; no single
"chart ruler" replacement, but multiple anchors evaluated in parallel.
`[Valens *Anth.* I, II, IX]`.

**Firmicus**: selects the chart ruler from the sign the Moon **next**
enters (after natal Moon's sign), **skipping** Sun and Moon's own
domiciles (Leo, Cancer) because luminaries do not accept individual chart
rulership. `[Firmicus *Math.* IV.19]` Bram printed.

**Dorotheus**: relies on stacked topic significators rather than a single
chart ruler; topic-by-topic chains routed through house ruler, triplicity
lords, Lot ruler. `[Dorotheus *Carmen* I-II via 'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). v1 keeps Ascendant ruler as the primary chart
significator. Multi-anchor support (Asc ruler + sect light + Fortune) is
already implicit in v1 focus rows.

**Reason**: Firmicus's Moon-next-entry rule is single-source and effectively
avoids the luminaries rather than replacing the Ascendant-ruler rule. Valens
and Dorotheus use multi-anchor stacking that v1 already accommodates via
focus rows + supporting witnesses.

---

## 4. Dignity weighting order

**v1 baseline (`dignities-reference.md`)**: Brennan Ch.8 deterministic
tables (domicile, exaltation, adversity, triplicity, Egyptian bounds,
decans) without explicit cross-dignity weighting hierarchy.

**Brennan**: no explicit weighting; dignities are inputs to
`planet-condition-audit.md` for combined judgment.

**Valens**: not addressed as an ordered weighting rule; uses dignities
contextually.

**Firmicus**: **explicit weighting** — exaltation first, own terms second,
own houses/domiciles third. `[Firmicus *Math.* VIII.32]` Bram printed.

**Dorotheus**: not addressed as an ordered weighting rule.

**v1 action**: A (no change). v1 keeps Brennan baseline (no weighting).

**Reason**: Firmicus's weighting is single-source explicit; Brennan/Valens/
Dorotheus do not present an ordered hierarchy. v1's combined-audit approach
(via `planet-condition-audit.md`) has tested stable through cases 01-04
without a fixed weighting order.

---

## 5. Leo third decan (OCR vs Chaldean order)

**v1 baseline (`dignities-reference.md`)**: Chaldean order applied
deterministically. Leo first decan = Sun; second = Venus (per Chaldean
sequence Sun-Venus-Mercury-Moon-Saturn-Jupiter-Mars beginning at Leo); **third
decan should be Mars**. Source: `[Brennan Ch.8]`.

**Brennan**: standard Chaldean order. `[Brennan Ch.8]`.

**Valens**: not directly addressed as a decan-table source in extracted
material.

**Firmicus**: Bk.II.4 (Bram printed pp. 34-36, PDF pp. 38-40) gives the
decan table. **Bram printed text for Leo reads**: "Of Leo the first to
Saturn, the second to Jupiter, the third to **Venus**." The surrounding
chain matches the standard Chaldean walking order without exception:
Cancer 3rd = Moon → Leo 1st = Saturn ✓; Leo 1st-2nd = Saturn-Jupiter ✓;
Virgo 1st-3rd = Sun-Venus-Mercury ✓; Libra 1st-3rd = Moon-Saturn-Jupiter ✓
etc. Leo 3rd is the **only** position in Firmicus's table that deviates
from the Chaldean walking order (which gives Mars). `[Firmicus *Math.*
II.4]` Bram printed pp. 34-36.

**Dorotheus**: not directly addressed as a decan-table source.

**v1 action**: A (no change). Bram printed reading flagged `needs
verification` here.

**Reason**: Phase B.6 PDF text extraction (pdftotext on the Bram 1975 scan)
confirmed Bram printed prints "Venus" for Leo 3rd — this is **not** an
OCR error in the Phase A extraction pipeline. However, the isolation of
the deviation (one position out of 36; surrounding chain walks Chaldean
order without break) makes a real Firmican variant unlikely; more
probable causes are (a) Bram typesetting / copying error, (b) Latin
manuscript variant used by Bram. Without consultation of Bram's
translator notes (printed pp. 303-314 in the Notes section) or an
independent Latin edition, the deviation cannot be definitively
classified. v1 retains standard Chaldean order (Leo 3rd = Mars) per
`[Brennan Ch.8]` and Firmicus's own surrounding chain. This entry is
flagged `needs verification` pending Bram translator note review.

---

## 6. Triplicity rulers ordering (by sect)

**v1 baseline (`dignities-reference.md`)**: Dorothean triplicity rulers
by sect (day lord / night lord / participating lord). Source: `[Brennan
Ch.8]`.

**Brennan**: Dorothean order (Dorothean triplicity rulers). `[Brennan Ch.8]`.

**Valens**: includes triplicity/triangle rulers in Bk.I material. Method-
targets flagged that Valens's ordering may differ from the Dorothean table
and should be cross-checked before any v1 update. `[Valens *Anth.* I]`.

**Firmicus**: aligns with the Dorothean ordering at the planet level.
`[Firmicus *Math.* II.1-6]` Bram printed.

**Dorotheus**: source for the Dorothean ordering itself. `[Dorotheus
*Carmen* I via 'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). v1 keeps Brennan/Dorothean ordering.

**Reason**: 3 of 4 sources align; Valens variation noted for v2.x
verification but does not override majority. Phase B does not modify
`dignities-reference.md`.

---

## 7. Listening / Beholding signs (rising-time affinity)

**v1 baseline (`aspect-reception-rules.md`)**: not addressed. v1 uses
standard sign-based aspect families (trine, sextile, square, opposition)
+ aversion; no rising-time-affinity layer.

**Brennan**: not addressed in v1's extracted chapters.

**Valens**: uses listening / beholding signs by rising-time affinity as
secondary configuration testimony. `[Valens *Anth.* I, IX]`.

**Firmicus**: signs that "see" and "hear" each other treated as
secondary doctrine after ordinary sign-based aspects. `[Firmicus *Math.*
VIII.3]` Bram printed.

**Dorotheus**: not directly addressed as a rising-time-affinity layer.

**v1 action**: A (no change). v1 does not add this layer.

**Reason**: 2 sources attest the doctrine, but Brennan baseline and v1's
locked Ch.9 sign-based model do not include it. This is a specialist
supplement; permanent-deferred per v2-roadmap (not v2.x candidate, since
geographic latitude-dependent rising times complicate the doctrine).

---

## 8. Solar revolutions calculation

**v1 baseline (`timing-techniques.md`)**: not implemented. v1 timing
covers annual profections + Zodiacal Releasing; no solar revolution
procedure.

**Brennan**: Ch.17 mentions solar revolutions in passing but does not
extract a procedure into v1. `[Brennan Ch.17]`.

**Valens**: covers solar revolutions material in Bk.IV / Bk.V timing
chapters; not extracted in detail. `[Valens *Anth.* IV, V]`.

**Firmicus**: covers division-of-the-year material via time-lord doctrine.
`[Firmicus *Math.* II.25-28]` Bram printed.

**Dorotheus**: explicit solar return as the annual return of the Sun to its
natal degree/minute, used as the annual frame. `[Dorotheus *Carmen* IV.1
via 'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). Phase B does not modify `timing-techniques.md`.
Solar revolutions deferred to v2.5 per `v2-roadmap.md`.

**Reason**: ≥2 sources support a solar-revolution annual method, but it is
a distinct timing technique requiring its own plan (chart-data contract,
calculator support, audit procedure).

---

## 9. Monthly / chronocrator lord methods

**v1 baseline (`timing-techniques.md`)**: not implemented. v1 timing covers
annual + ZR releasing only.

**Brennan**: Ch.17/18 cover profections + ZR; no monthly/daily lord
extraction. `[Brennan Ch.17, Ch.18]`.

**Valens**: extensive month / day / hour distributions in Bk.III - Bk.VII,
including subdistribution methods. `[Valens *Anth.* III-VII]`.

**Firmicus**: planetary rulers of time with month allotments (Saturn 30,
Jupiter 12, Mars 15, Sun 19, Venus 8, Mercury 20, Moon 25); requires Phase
B verification against Bk.II. `[Firmicus *Math.* VI.33-39]` Bram printed.

**Dorotheus**: monthly and daily lord methods exist but transmitted text is
uncertain. `[Dorotheus *Carmen* IV via 'Umar al-Tabari → Dykes 2017]`,
`needs verification`.

**v1 action**: A (no change). Phase B does not modify `timing-techniques.md`.
Monthly / daily lord methods deferred to v2.x.

**Reason**: ≥3 sources attest monthly/chronocrator methods, but they differ
in mechanism and require dedicated reconciliation. Out of v2.1 scope.

---

## 10. Planet-specific matutine / vespertine thresholds

**v1 baseline (`planet-condition-audit.md`)**: visibility thresholds with
combust band (~9°) and under-rays band (~15°) treated as general; Mercury-
specific 15° boundary handled via the `undeclared` rule. Source: `[Brennan
Ch.7]`, printed pp. 190-191, 205-206.

**Brennan**: general visibility thresholds; not split per planet.
`[Brennan Ch.7]`.

**Valens**: phase / visibility tracked but specific degree thresholds not
extracted in v1. `[Valens *Anth.* I, VI]`.

**Firmicus**: gives planet-specific thresholds — Saturn 15°, Jupiter 12°,
Mars 8°, Venus 8°, Mercury 18°. `[Firmicus *Math.* II.8-9]` Bram printed.

**Dorotheus**: emphasizes phase/visibility (eastern/western, under rays,
emerging, glow) but does not give a per-planet degree table in extracted
material. `[Dorotheus *Carmen* I-IV via 'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). v1 keeps Brennan's general thresholds.

**Reason**: Firmicus's per-planet values are valuable but require their own
verification + integration plan; not within v2.1 scope. Phase B logs them
here for future reference.

---

## 11. Moon application / separation / void doctrine

**v1 baseline (`aspect-reception-rules.md`)**: applying / separating
distinctions noted in event-like questions; void-of-course Moon not
implemented as a natal rule. Source: `[Brennan Ch.9]`.

**Brennan**: applying / separating tracked in event-like questions; less
systematic on Moon-specific application doctrine. `[Brennan Ch.9]`.

**Valens**: not extracted systematically in v1's Brennan-baseline phase.

**Firmicus**: highly systematic — Moon application target, separation,
conjunction, defluction, void-of-course treated as natal obstruction /
depletion (not electional). `[Firmicus *Math.* IV.1-16, IV.25]` Bram
printed.

**Dorotheus**: Moon application logic appears in topical chapters but
without systematic doctrine. `[Dorotheus *Carmen* I-II via 'Umar al-Tabari →
Dykes 2017]`.

**v1 action**: A (no change). v1 keeps Brennan baseline.

**Reason**: Firmicus's Bk.IV doctrine is the most systematic of the four
sources but treats void-of-course Moon as natal obstruction in a way that
diverges from common modern electional usage. Reconciliation requires its
own plan; deferred to v2.x.

---

## 12. Fortune ruler stack

**v1 baseline (`lots-and-fortune.md`)**: Fortune is judged via Fortune
sign/degree + place from Ascendant + Fortune ruler + co-present planets +
configurations + derived houses (when method requires). Source: `[Brennan
Ch.16]`, printed pp. 515-517.

**Brennan**: Fortune ruler + ruler condition + configured benefics/malefics
+ co-presence + derived houses. `[Brennan Ch.16]`.

**Valens**: Fortune ruler audit + Daimon ruler audit + Ascendant
comparison; extensive use in Bk.IX. `[Valens *Anth.* IX]`.

**Firmicus**: extended ruler stack — Fortune sign ruler + Fortune terms
ruler + sect luminary degree/terms ruler + angularity + aspects + Fortune
duodecatemorion. `[Firmicus *Math.* IV.17]` Bram printed.

**Dorotheus**: Fortune used as status/assets anchor with ruler audit
similar to Brennan. `[Dorotheus *Carmen* I.27-28 via 'Umar al-Tabari →
Dykes 2017]`.

**v1 action**: A (no change). v1 keeps Brennan-style ruler audit.

**Reason**: Firmicus's terms/duodecatemorion extensions require exact-
degree support and are mostly degree-doctrine layers; deferred to v2.x.
v1 reader-side combined-audit via `planet-condition-audit.md` is
operationally sufficient.

---

## 13. Saturn-by-sect rulership resonance vs condition weakening

**v1 baseline (`significator-hierarchy.md` + `planet-condition-audit.md`)**:
Divinatory/spiritual aptitude Focus Notes currently treat Saturn by sect as
depth/ordeal capacity when of sect, and obstruction/overload when contrary to
sect. No explicit rule says that Saturn's exaltation relationship to an anchor
sign overrides Saturn's own condition. Source: `[Brennan Ch.7]` (sect),
`[Brennan Ch.8]` (exaltation/fall and host condition), `[Brennan Ch.14]`
(reception).

**Brennan**: sect, dignity, host/ruler condition, and reception are separate
audit axes. Ch.7 makes contrary-to-sect malefics more difficult; Ch.8 treats
fall as lowered/reduced but not automatic ruin; Ch.14 treats reception by
domicile/exaltation as mitigation or structured difficulty when the relevant
planets are configured. No explicit "Saturn in fall but ruling its exaltation
sign as topic anchor" doctrine appears in the extracted material. `[Brennan
Ch.7]`, pp. 190-197; `[Brennan Ch.8]`, pp. 228-248; `[Brennan Ch.14]`, pp.
491-493.

**Valens**: Bk.I-II extractions require planetary condition before using
natural significations, treat sect as one condition layer, and require topic
connections through configuration, rulership, Lot, or timing activation.
Mixed outcomes are preserved when support and instability both appear, but no
Saturn-Aries/Libra exaltation-anchor mixed doctrine appears in the extracted
Bk.I-II material. `[Valens *Anth.* I.1-I.2, I.21K;19P-I.22K;20P,
II.1-II.2, II.16K;17P]`.

**Firmicus**: Firmicus confirms Saturn's exaltation/fall degrees (Libra 21 /
Aries 21) and Saturn as diurnal. Bk.III makes Saturn by night much more
difficult while requiring dignity, terms, Moon, Mars, and benefic testimony;
Bk.IV chart-ruler material judges ruler efficacy by house/sign, dignity, sect,
and benefic/malefic mixture. No explicit doctrine says an exaltation tie to a
separate anchor sign mitigates Saturn's own fall/contrary-sect condition.
`[Firmicus *Math.* II.3, II.7, III.2, III.2-14, IV.19-20]` Bram printed.

**Dorotheus**: Bk.I records domicile/exaltation/fall as condition inputs and
uses cumulative planet condition: dignity, sect, visibility, motion, and
place. Saturn is harsher by night, and mixed testimony is preserved when
dignity conflicts with poor visibility, place, or sect condition. This
supports combination-of-rules handling generally, not the specific
Saturn-fall/exaltation-anchor doctrine. `[Dorotheus *Carmen* I.1-I.2, I.6 via
'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change to `significator-hierarchy.md`). Close pending
verification #10 as Pattern (3): independent axes / no explicit mixed doctrine.
case-05's Saturn-Libra line remains a `[project heuristic]` reading-time
combination: record the rulership/exaltation tie as relevant testimony, then
let Saturn's audit fields (contrary-to-sect, fall, cadent 6th, aspect/reception
context) decide whether the tie can be used cleanly.

**Reason**: No source in the four-source extraction set explicitly supports
Pattern (1) at the required specificity, and Pattern (2) is absent. Dorotheus
and Firmicus are useful witnesses for mixed condition logic generally, while
Brennan and Valens support independent-axis auditing. The result is Pattern
(3), not a sourced Focus Notes rule; no v1 watermark is needed because
`significator-hierarchy.md` is unchanged.

---

## 14. Parental house doctrine (4 vs 10 — which place reads father / mother / unified)

**v1 baseline (`significator-hierarchy.md` 父母 / 家庭关系 focus row,
added v2.2 Plan B.3)**: 4 + 10 read as a **combined parental field**.
The focus row deliberately does **not** commit to a single "4 = mother,
10 = father" or "4 = father" or "4 = both parents (unified)" split.
Instead, natural significators (Sun for father, Moon for mother, per
`[Brennan Ch.7]`) plus sect-light family-channel + audit of 4-ruler
/ 10-ruler decide per-chart which parent reads through which place.
Source: `[Brennan Ch.10]`, printed pp. 340-363; `[Brennan Ch.7]`
planet natural significators.

**Brennan**: 4th = home, parents (unified parental base in the
whole-sign tradition), property, foundations, endings. Sun = father
natural / Moon = mother natural carries the parental differentiation
rather than a 4-vs-10 split. The 10th-as-father reading is noted as a
parallel doctrine but Brennan's baseline treats 4 as the parental
anchor. `[Brennan Ch.7]` (planet natures), `[Brennan Ch.10]` printed
pp. 340-363 (house topics).

**Valens**: Bk.II routes parent material primarily through IV with
selected chapters also routing parental readings through X. Variance
between IV-as-parents-base and X-as-parental-second-reading appears
within Bk.II itself; Valens does not resolve to a single fixed
"4 = mother / 10 = father" split. `[Valens *Anth.* II.5, II.7-8]`
(Mark Riley trans.).

**Firmicus**: Bk.II.19 (Bram printed) treats 4 as parents / property
in the place-topic survey, while other Firmicus material routes a
paternal channel through 10 in parallel. The 4 vs 10 split for
father vs mother is not fixed to one position in Firmicus; mixed
treatment is present. `[Firmicus *Math.* II.19]` Bram printed.

**Dorotheus**: Topic chapters in Bk.I route parent material through
IV primarily with natural-significator differentiation (Sun =
father / Moon = mother) carrying the parental split. Some 'Umar
transmission chapters note a 10-as-father reading as variant but
do not promote it to baseline. `[Dorotheus *Carmen* I via
'Umar al-Tabari → Dykes 2017]`.

**v1 action**: A (no change). v1 retains the **combined 4 + 10
parental field** approach with Sun / Moon as natural-significator
differentiators. Phase B.3 adds this flag (rather than collapsing
the variance to a single split) so the reader knows the source
variance exists and the rule deliberately preserves it.

**Reason**: 4 of 4 sources route parental material through IV as the
primary parental place (with parental-base / parents-unified
treatment in the whole-sign tradition); 3 of 4 sources (Valens,
Firmicus, Dorotheus) include parallel 10-as-paternal material at
varying levels of commitment, but no source commits to a categorical
"4 = mother only / 10 = father only" split as the dominant rule. The
combined-field approach with natural-significator differentiation
accommodates all four sources without forcing a single doctrinal
commitment; per-chart application is delegated to the audit + natural
significators.

---

## Append protocol

New entries added to this file should follow the same template:

```text
## N. <Topic>

**v1 baseline**: <v1 rule + source + page>.

**Brennan**: <position + chapter + page>.
**Valens**: <position + book + chapter or page>.
**Firmicus**: <position + book + chapter + Bram page>.
**Dorotheus**: <position + book + verse + via 'Umar al-Tabari → Dykes 2017>.

**v1 action**: <A: no change / B: additive note / C: change logic / D: defer>.

**Reason**: <brief>.
```

Entries must:

- have ≥2 sources with explicit positions (single-source entries do not enter);
- mark `not addressed` for sources without explicit material; do not pad;
- keep v1 baseline cited; never decide v1 in this file — only register positions;
- preserve `needs verification` flags explicitly.
