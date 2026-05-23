# Valens Extraction - Book I Calculation And Combinations

Source: Vettius Valens, `Anthologies`, Book I, Mark Riley translation.

Range: local PDF pp. 8-24.

Brennan cross-ref: `[cross-ref: Brennan Ch.9]`, `[cross-ref: Brennan Ch.14]`, `[cross-ref: Brennan Ch.17]`.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Method Takeaway

The latter half of Book I is largely computational and combinational. It supplies ancient procedures for Ascendant/MC calculation, lunar phase and visibility, nodes, planetary positions, transits, planetary mixtures, and conception. In this project these are mostly data-prep or specialist timing material, not ordinary reading prose.

## Rule Card I.C1 - Ascendant And MC Calculation Are Data-Prep Methods

Source: Book I.4-I.7K;6P, local PDF pp. 8-10.

Use when:

- reconstructing an ancient chart without modern software;
- auditing whether an Ascendant/MC value is internally consistent;
- documenting that a Valens method requires exact time and rising-time tables.

Required chart data:

- birth date and hour;
- solar and lunar positions where required;
- local klima/rising times;
- calculation scheme selected.

Procedure:

1. Treat Valens' Ascendant/MC procedures as computational scaffolding.
2. Prefer modern verified chart data for project readings unless the task is historical reconstruction.
3. If the Valens procedure is used, record the formula path and any table assumptions.
4. Mark output as data-derived, not interpretive testimony.

Guardrail:

Status: needs verification. Do not silently replace chart-calculator Asc/MC data with reconstructed Valens values.

Destination rule file:

- `rules/data_contract.md`

Provenance: `[Valens *Anth.* I.4-I.7K;6P, PDF pp. 8-10]` `[new to Valens]`.

## Rule Card I.C2 - Listening And Beholding Signs Are A Supplemental Relationship Doctrine

Source: Book I.8K;7P, local PDF p. 11.

Use when:

- working specifically in a Valens source layer;
- comparing sign relationships by rising-time affinity;
- investigating whether two signs have a non-aspect relationship in Valens.

Required chart data:

- signs occupied by the planets/points;
- local rising times/klima if needed;
- ordinary sign-based configuration status.

Procedure:

1. First evaluate ordinary sign-based configurations.
2. If Valens' listening/beholding doctrine is relevant, record it separately.
3. Treat it as supplemental testimony, not as a replacement for aspect configuration.
4. Flag it for Phase B review before adding to v1 aspect rules.

Guardrail:

This doctrine is not the same as the current v1 aspect model. Do not blend it into sign-based aspect families without explicit rule update.

Destination rule file:

- `rules/aspect-reception-rules.md`

Provenance: `[Valens *Anth.* I.8K;7P, PDF p. 11]` `[new to Valens]`.

## Rule Card I.C3 - Lunar Phase And Visibility Are Condition Inputs

Source: Book I.9K;8P, I.13K;12P, I.14K;13P, I.15K;14P, local PDF pp. 11-13.

Use when:

- judging Moon condition;
- reconstructing lunar phase or visibility without modern software;
- timing a lunar-day technique.

Required chart data:

- Sun degree;
- Moon degree;
- day count from conjunction/full moon if available;
- sign/rising time values for visibility calculation.

Procedure:

1. Determine the Moon's phase relationship to the Sun.
2. Record visibility or invisibility only if data supports it.
3. Use phase/visibility as a condition layer for the Moon or lunar timing.
4. Keep calculation method and interpretive judgment separate.

Guardrail:

Status: needs verification. Ancient visibility calculations should be cross-checked before automated implementation.

Destination rule file:

- `rules/planet-condition-audit.md`
- `rules/data_contract.md`

Provenance: `[Valens *Anth.* I.9K;8P, I.13K;12P-I.15K;14P, PDF pp. 11-13]` `[cross-ref: Brennan Ch.7]`.

## Rule Card I.C4 - Nodes, Steps, And Winds Are Specialist Condition Data

Source: Book I.16K;15P and I.18K;16P, local PDF pp. 13-14.

Use when:

- a Valens timing or conception method explicitly uses the node;
- a rule requires lunar step/wind information;
- comparing planetary directionality in a historical method.

Required chart data:

- node position;
- Moon position;
- sign and degree;
- method requiring the data.

Procedure:

1. Compute or import the node only when the technique requires it.
2. Record lunar steps/winds as specialist data.
3. Do not infer ordinary natal meaning from these values without a rule that uses them.

Guardrail:

Status: needs verification. Node and wind procedures need separate mathematical validation.

Destination rule file:

- `rules/data_contract.md`
- `rules/timing-techniques.md`

Provenance: `[Valens *Anth.* I.16K;15P, I.18K;16P, PDF pp. 13-14]` `[new to Valens]`.

## Rule Card I.C5 - Ancient Planetary Reckoning Is An Ephemeris Substitute

Source: Book I.19K;17P and I.20K;18P, local PDF pp. 14-17.

Use when:

- reconstructing how Valens calculated positions;
- checking source-historical computation;
- no modern ephemeris is allowed by task scope.

Required chart data:

- era/year/month/day;
- planetary tables or factors;
- calculation method.

Procedure:

1. Treat these procedures as historical computation.
2. For project readings, prefer verified planetary positions from reliable chart data.
3. If using Valens' reckoning, keep a calculation audit trail.

Guardrail:

Status: needs verification. This should not be folded into the skill as a position calculator during Phase A.

Destination rule file:

- `rules/data_contract.md`

Provenance: `[Valens *Anth.* I.19K;17P-I.20K;18P, PDF pp. 14-17]` `[new to Valens]`.

## Rule Card I.C6 - Planetary Combinations Are Mixtures, Not One-Line Outcomes

Source: Book I.21K;19P and I.22K;20P, local PDF pp. 17-22.

Use when:

- multiple planets are co-present or tightly configured;
- a topic chain depends on a planetary pair or triad;
- checking whether a benefic/malefic mixture is internally coherent.

Required chart data:

- planets involved;
- sign relationship and degree closeness;
- sect;
- dignity and place;
- topic chain or Lot connection.

Procedure:

1. Identify whether the planets are actually linked: co-presence, configuration, rulership, or time-lord activation.
2. Read Valens' pair/triad meanings as mixture templates.
3. Modify the mixture by sect, condition, place, and topic.
4. Report mixed outcomes when Valens gives both support and instability.

Guardrail:

Do not paste a pair/triad delineation onto any chart merely because two planets exist. The relationship must be active in the evidence chain.

Destination rule file:

- `rules/aspect-reception-rules.md`
- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

Provenance: `[Valens *Anth.* I.21K;19P-I.22K;20P, PDF pp. 17-22]` `[cross-ref: Brennan Ch.9]`.

## Rule Card I.C7 - Conception And Gestation Methods Are Specialist, Not v1 Core

Source: Book I.23K;21P and I.24K;22P, local PDF pp. 22-24.

Use when:

- researching ancient prenatal techniques;
- a later specialist module requires conception/gestation reconstruction;
- comparing Valens with other lifespan/conception methods.

Required chart data:

- birth date and time;
- Moon position;
- Ascendant/Descendant;
- yearly lunar positions for seven-month method.

Procedure:

1. Keep conception/gestation calculations outside ordinary natal reading.
2. Record the required data and method path.
3. Mark any derived conception chart or viability judgment as specialist.

Guardrail:

Status: needs verification. These methods should not be used for client-facing claims without a separate ethical and computational review.

Destination rule file:

- `rules/timing-techniques.md`
- `rules/data_contract.md`

Provenance: `[Valens *Anth.* I.23K;21P-I.24K;22P, PDF pp. 22-24]` `[new to Valens]`.
