# Lots And Fortune

> Last v2.x change: 2026-05-15 (v2.1 Phase B) — added cross-source references
> for Spirit/Fortune formulas (Valens, Firmicus, Dorotheus) + registered
> candidate Lots (Religion, Eros) as deferred. Additive only; existing
> formulas and procedures unchanged.

Purpose: use Lots as derived topic anchors without letting them become vague decorative points.

## Core Principle

A Lot is a calculated point. It is judged through:

```text
Lot sign/degree + place from Ascendant + Lot ruler + co-present planets + configurations + derived houses when method requires.
```

Do not read a Lot as if it were a planet with its own body. Its ruler and witnesses carry the judgment.

## Required Data

| Field | Required when using Lots | Notes |
|---|---|---|
| Sect | yes | formulas can reverse by day/night |
| Ascendant degree | yes | projection point |
| Sun degree | yes | luminary distance |
| Moon degree | yes | luminary distance |
| Lot formula/source | yes | avoid formula drift |
| Lot sign and degree | yes | derived anchor |
| Lot ruler | yes | main significator of Lot |
| Configurations to Lot | important | benefic/malefic testimony |

## Formulas (sourced)

Source: `[Brennan Ch.16]`, printed pp. 512-513, 521-522, 525.

Use zodiacal longitude in degrees and reduce the result modulo 360.

| Lot | Day chart | Night chart | Operational meaning |
|---|---|---|---|
| Fortune | Ascendant + Moon - Sun | Ascendant + Sun - Moon | count from sect light to contrary-to-sect light, then project from Ascendant |
| Spirit | Ascendant + Sun - Moon | Ascendant + Moon - Sun | count from contrary-to-sect light to sect light, then project from Ascendant |

Notes:

- The formula reverses by sect. Do not use a single day formula for both day and night charts unless a source-specific variant is being tested.
- Brennan notes variants and disagreements around Fortune calculation, but uses the standard reversal by day/night as advocated by Dorotheus, Valens, and Paulus.
- v1 only locks Fortune and Spirit. Other Lots still require their own formula/source before use.

Cross-source references (v2.1 Phase B; v1 formulas unchanged):

- `[Valens *Anth.* IX]` (Mark Riley trans.) — Fortune and Daimon are
  distinct day/night Lots; Valens uses them as primary anchors throughout
  Bk.IX (Fortune-Daimon-Ascendant methods).
- `[Firmicus *Math.* IV.17-18]` Bram printed — gives Fortune (IV.17) and
  Daemon/Spirit (IV.18) formulas. **The Bram printed text for Daemon
  appears to repeat the Fortune formula; this is `needs verification`
  (likely transmission/OCR artifact, since the three other sources
  Brennan/Valens/Dorothean-tradition give distinct day-night-reversed
  formulas).** See `cross-source-method-comparison.md` entry "Daemon /
  Fortune 公式".
- `[Dorotheus *Carmen* I.27-28 via 'Umar al-Tabari → Dykes 2017]` —
  Fortune used as major status/assets anchor (consistent with v1
  formula); Bk.I.28 places Fortune in status/wealth significator chains.

In all three sources Spirit/Daimon is named as the chart's intentional /
volitional / action-directed anchor when distinct from Fortune; v1's
existing day/night-reversed Spirit formula (Brennan Ch.16) is the
provisionally locked form. The Firmicus Bram irregularity does not modify
v1; it is logged in the cross-source layer.

## Basic Lot Audit

```text
Lot:
Formula/source:
Sign/degree:
Place from Ascendant:
Lot ruler:
Ruler condition:
Co-present planets:
Configured benefics/malefics:
Derived-place relevance:
Judgment:
Confidence:
```

## Procedure

1. Calculate or record the Lot with a source-labeled formula.
2. Identify sign and whole sign place.
3. Identify the Lot ruler.
4. Audit the Lot ruler using `planet-condition-audit.md`.
5. Check planets co-present with the Lot.
6. Check planets configured to the Lot using `aspect-reception-rules.md`.
7. Use derived houses from the Lot only when the technique requires it.
8. Compare with the relevant natal house and house ruler.

## Lot Of Fortune

Use Fortune as a major derived anchor for:

- body and embodied circumstance;
- material fortune;
- livelihood and events that befall the native;
- circumstantial support or adversity;
- derived houses from Fortune;
- zodiacal releasing from Fortune.

Fortune is not judged alone. Judge:

```text
Fortune place + Fortune ruler condition + testimony to Fortune + relation to Ascendant and sect light.
```

## Lot Of Spirit

Use Spirit as a paired anchor for:

- intention;
- action;
- choice and volition;
- mental or directive principle;
- career/action layers when supported;
- zodiacal releasing from Spirit.

Compare Fortune and Spirit:

| Relationship | Reading stance |
|---|---|
| integrated/configured | circumstance and intention can work together |
| same ruler | common manager or shared life route |
| aversion | circumstance and intention may not directly coordinate |
| one strong, one weak | imbalance between what happens and what is chosen |

## Other Lots

Other Lots are topic-specific witnesses. Use only when:

- the topic demands it;
- formula/source is known;
- chart data includes the Lot;
- it adds evidence rather than noise.

Keep secondary Lots below:

1. chart focus;
2. topic house/ruler;
3. primary significator;
4. Fortune/Spirit when relevant;
5. time-lord activation.

### Candidate Lots (v2.1 Phase B; deferred from v1 default set)

Phase B.0 triage surfaced two Lots that the v2.1 divinatory / spiritual
aptitude focus could optionally use, but **neither meets the v1 threshold
of ≥2 sources providing a single consistent formula**. They are registered
here for traceability; do **not** treat as default supporting Lots.

| Lot | Sources attesting | Status | Routing |
|---|---|---|---|
| Lot of Religion | `[Dorotheus *Carmen* I.9 via 'Umar al-Tabari → Dykes 2017]` candidate; other sources do not give a single distinct formula | `[Source-only candidate, needs verification]` | Deferred to v2-roadmap (formula reconciliation + Brennan/Valens cross-check). Logged in `cross-source-method-comparison.md`. Not used as default v1 Lot. |
| Lot of Eros | `[Brennan Ch.16]` Hermetic Lots survey (printed pp. 524-533, PDF pp. 551-560) covers Eros conceptually; Dorotheus mentions friendship/Eros Lots in Bk.II topic chapters | `[Optional / topic-specific]` | Deferred to v2-roadmap (formula extraction + per-source verification). Used only when the question explicitly involves erotic / affective channel; not a default v1 supporting Lot. |

Other Dorothean / Valentine / Firmican topic Lots (fathers, mother, siblings,
marriage, children, assets/livelihood, chronic illness, death, etc.) are
**not** added to v1. They are registered for later v2.x topic-Lot expansion
in `v2-roadmap.md`.

## Guardrails

- Do not use Lots without reliable birth time.
- Do not use many Lots in a first-pass reading.
- Do not ignore the Lot ruler.
- Do not treat Fortune as automatically good because of the name.
- Do not force Fortune and Spirit into psychological categories without chart evidence.

## Zodiacal Releasing Link

Fortune and Spirit are required for Zodiacal Releasing.

- Release from Spirit for action, career, intention, and life direction.
- Release from Fortune for body, circumstance, health, and material events.
- If Fortune and Spirit are in the same sign, avoid double-counting the same period as independent confirmation.

## Source Status

Distilled from Brennan Chapters 16 and 18. Fortune and Spirit formulas are sourced from Ch. 16 and locked for v1; other Lots still require formula/source before use. Needs cross-check with primary sources and a deterministic calculator before final locking.

