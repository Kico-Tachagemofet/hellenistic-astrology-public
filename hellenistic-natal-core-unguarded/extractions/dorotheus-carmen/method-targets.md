# Dorotheus Method Targets

Source: Dorotheus of Sidon, *Carmen Astrologicum: The 'Umar al-Tabari Translation*, trans. Benjamin Dykes, 2017.

Purpose: track which Dorothean extraction cards may later support, clarify, or extend v1/v2 rules. This is not a rule update file. Phase B should decide what enters `rules/`.

## High-Value Phase B Targets

### `rules/timing-techniques.md`

Dorotheus Book IV is the highest-value addition.

Potential support:

- Annual profection by counting one whole sign per year from the Ascendant; lord of the year is the domicile lord of the profected sign. Confirms v1 annual profection core. `[cross-ref: Brennan Ch.17]`
- Solar revolution as the annual return of the Sun to its natal degree/minute. New rule family relative to v1, which currently has no solar revolution procedure. `[new to Dorotheus]`
- Judge the lord of the year by natal root condition plus annual/revolution condition: sect-like phase, visibility, under-rays, retrograde, own/alien place, and benefic/malefic testimony. Confirms and expands v1 lord-of-year audit.
- Activated natal tenants: when the year reaches a natal planet's sign, that planet's promise and current testimony matter. Confirms v1 activated-tenants rule. `[cross-ref: Brennan Ch.17]`
- Monthly and daily lord methods exist but are not ready for v1 without calculator support and source reconciliation. `[needs verification]`
- Transit-to-natal-place logic in IV.4 suggests a specific filter: a planet's transit to a sign it natally opposed/squared/trined/occupied changes quality according to the natal aspect relationship. This is not in v1. `[new to Dorotheus]`

Potential caution:

- Dorotheus Book IV does not supply Zodiacal Releasing; no Ch.18-style ZR support found here.
- Several annual/month/day formulas are transmitted with Dykes cautions. Do not implement without a dedicated timing plan.

### `rules/planet-condition-audit.md`

Potential support:

- Repeated Dorothean emphasis on phase/visibility: eastern/western, under rays, emerging, glow, retrograde, increasing/decreasing in calculation. `[cross-ref: Brennan Ch.7]`
- Sect-conditioned malefic handling: Saturn in day contexts and Mars in night contexts can be less destructive when properly placed; contrary-sect malefic testimony is more harmful. `[cross-ref: Brennan Ch.7]`
- Good/bad place and angularity matter as accidental power before any topic prediction. `[cross-ref: Brennan Ch.10]`
- Planet condition must combine dignity, place, visibility, motion, and testimony; Dorotheus repeatedly refuses a single-factor reading.

Potential caution:

- Dorotheus uses medical and death indications in a way that should not become user-facing diagnosis or fatalistic prediction.

### `rules/house-topic-framework.md`

Potential support:

- Book I.5 provides a place-quality hierarchy: approved places vs worst places, with stakes and their followers emphasized. `[cross-ref: Brennan Ch.10]`
- Book IV.5 maps the four stakes to life-phase/topical anchors: Ascendant/youth/body, MC/work/children, Descendant/marriage/old age, IC/end of life. `[new to Dorotheus]`
- Book I-II use derived places and Lots as secondary topic anchors, but topic houses remain primary.

Potential caution:

- Several Book II placement chapters are cookbook-heavy. Phase B should translate them into reusable condition checks, not house-by-planet recipes.

### `rules/lots-and-fortune.md`

Potential support:

- Dorotheus uses many topic Lots: fathers, mother, siblings, wedding/marriage, children, assets/livelihood, chronic illness, death, and possibly Eros/friendship. `[new to Dorotheus]`
- The repeated procedure is stable: calculate Lot, identify sign, audit its lord, check co-present or configured planets, then compare against the ordinary topic significator.
- Lot of Fortune has a major status/assets role in Book I.28 and is not decorative. `[cross-ref: Brennan Ch.16]`

Potential caution:

- Do not add all Dorothean Lots to v1. Most should remain optional topic modules until formulas are verified and calculator support exists.
- Some Lot formulas in the transmitted text have variant readings; mark exact formula imports with source and verification status.

### `rules/significator-hierarchy.md`

Potential support:

- Dorotheus repeatedly uses stacked significator logic:
  - ordinary topic significator;
  - triplicity lords of that significator;
  - topic house and its lord;
  - relevant Lot and Lot lord;
  - benefic/malefic testimony.
- Same-planet multi-role discipline remains important: a planet can be topic ruler, Lot ruler, and timing lord without automatically multiplying evidence.
- Book I-II topic chapters support explicit hierarchy for parents, marriage, children, siblings, assets, and status.

Potential caution:

- Dorotheus's concrete predictions are often socially/historically specific. Phase B should extract the evidence chain, not the social script.

### `rules/aspect-reception-rules.md`

Potential support:

- Book II.14-II.17 confirms aspect-family differences: trine more supportive, sextile weaker than trine, square/opposition harsher and more conflict-bearing. `[cross-ref: Brennan Ch.9]`
- Square language repeatedly distinguishes right/left or looking-down relations, supporting the existing overcoming/directionality layer. `[cross-ref: Brennan Ch.9]`
- Benefic testimony can ease malefic indications; malefic testimony can corrupt otherwise supportive ones. `[cross-ref: Brennan Ch.14]`
- Book IV.4 extends aspect logic into transit repetition: later arrivals to signs related to natal positions by opposition/square/trine carry different qualities. `[new to Dorotheus]`

Potential caution:

- Do not convert Dorothean aspect paragraphs into planet-pair cookbooks. Extract aspect family + condition + mitigation logic.

## Cross-Validation With v1 Timing

| v1 timing rule | Dorotheus result | Status |
|---|---|---|
| Count annual profections one sign per year from Ascendant | IV.1 explicitly counts one year per sign from Ascendant | confirmed |
| Lord of year = ruler of activated sign | IV.1 explicitly makes the sign lord the year lord | confirmed |
| Audit lord of year natally | IV.1 says to inspect its root/natal condition and phase | confirmed |
| Activated place tenants matter | IV.1 treats years reaching natal planet signs as important | confirmed |
| Transits filter through activated annual topics | IV.1/IV.4 support filtered transit logic | expanded |
| Solar revolutions | Dorotheus uses Sun return to natal degree/minute | new, not implemented in v1 |
| Monthly/daily lords | Dorotheus gives methods but transmitted text is uncertain | needs verification |
| Zodiacal Releasing | not found in Book IV | no Dorotheus support in this pass |

## Batch Metrics

- Rule cards: 54.
- `needs verification`: 18.
- `[new to Dorotheus]`: 33.
- Significant Brennan conflicts: 0 hard conflicts.
- Timing expansion candidates: 5.
- Cookbook/counting deferred clusters: 12.

## Do Not Integrate Yet

- Book III longevity distribution procedures.
- Book IV death and illness methods as user-facing predictive rules.
- Book V horary/inception material.
- Any topic Lot formula that has not been verified against variant readings.
- Planet-in-house cookbook paragraphs as direct delineation recipes.
