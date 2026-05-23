# Valens Extraction - Book I Foundations

Source: Vettius Valens, `Anthologies`, Book I, Mark Riley translation.

Range: local PDF pp. 1-8, with later foundational references continuing through Book I.

Brennan cross-ref: `[cross-ref: Brennan Ch.7]`, `[cross-ref: Brennan Ch.8]`, `[cross-ref: Brennan Ch.9]`.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Method Takeaway

Book I opens with a dense catalogue of planetary, sign, degree, and material correspondences. For this project, these are not placement cookbooks. They are source witnesses used to populate audit inputs: natural significator, sect, dignity/term, sign quality, body/material correspondence, and secondary topical witness.

## Rule Card I.1 - Planetary Natures As Natural Significator Inputs

Source: Book I.1, local PDF pp. 1-2.

Use when:

- assigning natural significators;
- checking whether a planet naturally carries a topic;
- interpreting why a planet's condition matters for a topic.

Required chart data:

- planet involved;
- topic under judgment;
- planet's sect, place, dignity, motion/visibility if available;
- configurations to relevant topic rulers or Lots.

Procedure:

1. Record the planet's natural topics from Valens as possible significator material.
2. Audit the planet's condition before using those topics in delineation.
3. Check whether the planet is also a topical ruler, Lot ruler, time lord, or configured witness.
4. Use the planet's natural topics only when supported by role or testimony.

Guardrail:

Do not convert Valens' planetary catalogues into standalone statements. Natural significator status must pass through the evidence chain.

Destination rule file:

- `rules/planet-condition-audit.md`
- `rules/significator-hierarchy.md`

Provenance: `[Valens *Anth.* I.1, PDF pp. 1-2]` `[cross-ref: Brennan Ch.7]`.

## Rule Card I.2 - Sect Belongs Inside Planetary Capacity

Source: Book I.1, local PDF pp. 1-2.

Use when:

- judging whether a planet is operating in a more congenial or contrary environment;
- cross-checking malefic/benefic behavior;
- evaluating a luminary or sect-affiliated planet.

Required chart data:

- day/night chart;
- planet's sect affiliation;
- planet's place and visibility if available.

Procedure:

1. Record the chart sect.
2. Mark whether each sect-relevant planet is aligned with or contrary to that sect.
3. Let sect modify the planet's condition and behavior.
4. Do not let sect override all other testimony; combine with place, dignity, phase, and configurations.

Guardrail:

Sect is not a single verdict. It is one condition layer.

Destination rule file:

- `rules/planet-condition-audit.md`

Provenance: `[Valens *Anth.* I.1, PDF pp. 1-2]` `[cross-ref: Brennan Ch.7]`.

## Rule Card I.3 - Zodiacal Sign Natures Are Background Conditions

Source: Book I.2, local PDF pp. 2-6.

Use when:

- judging the qualitative environment of a planet or Lot;
- explaining why a sign modifies a planet's expression;
- checking sign-based topical testimony.

Required chart data:

- sign occupied by the planet, Lot, or angle;
- domicile ruler and relevant dignity condition;
- topic being read.

Procedure:

1. Record the sign's baseline qualities: gender, element/temperature, modality-like stability, fertility, vocality, upward/downward tendency, and other Valens descriptors.
2. Use those qualities as environmental modifiers.
3. Prioritize domicile ruler, place, and configuration before relying on sign adjectives.
4. Use sign qualities as supporting testimony, not as a main claim.

Guardrail:

Do not make "native is X because planet/sign placement says X" statements without ruler-chain and condition support.

Destination rule file:

- `rules/house-topic-framework.md`
- `rules/planet-condition-audit.md`

Provenance: `[Valens *Anth.* I.2, PDF pp. 2-6]` `[cross-ref: Brennan Ch.8]`.

## Rule Card I.4 - Terms/Bounds Are Degree-Level Condition Data

Source: Book I.3, local PDF pp. 6-8.

Use when:

- exact degree is known;
- a planet, angle, Lot, or aphetic point falls in a specific bound/term;
- later rule integration requires a deterministic term table.

Required chart data:

- exact degree;
- term/bound ruler table selected;
- planet or point being judged.

Procedure:

1. Identify the term/bound ruler for the exact degree.
2. Record whether the term ruler supports, constrains, or complicates the planet/point.
3. If using Valens' qualitative term descriptions, mark them as source-specific testimony.
4. Cross-check against the project's canonical dignity table before rule integration.

Guardrail:

Status: needs verification. Valens' term descriptions should not overwrite `rules/dignities-reference.md` without a table-level comparison.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`

Provenance: `[Valens *Anth.* I.3, PDF pp. 6-8]` `[cross-ref: Brennan Ch.8]`.

## Rule Card I.5 - Degree Classifications Are Specialist Weights

Source: Book I.12K;11P, local PDF p. 12.

Use when:

- a later method explicitly requires masculine/feminine degrees;
- exact degree data is available;
- comparing Valens timing or conception methods.

Required chart data:

- exact degree;
- sign gender;
- degree classification scheme.

Procedure:

1. Use degree gender only when the technique explicitly calls for it.
2. Record the scheme and source.
3. Keep it below sign, ruler, place, Lot, and configuration testimony in ordinary natal readings.

Guardrail:

Status: needs verification. Do not add degree-gender logic to v1 without a specific downstream method requiring it.

Destination rule file:

- `rules/data_contract.md`
- `rules/dignities-reference.md`

Provenance: `[Valens *Anth.* I.12K;11P, PDF p. 12]` `[new to Valens]`.

## Rule Card I.6 - Body, Material, And Regional Correspondences Are Low-Priority Witnesses

Source: Book I.1-I.2, local PDF pp. 1-6.

Use when:

- a topic specifically concerns body parts, materials, regions, or environmental context;
- multiple higher-priority testimonies already point to the same topic.

Required chart data:

- relevant planet/sign;
- topic being investigated;
- supporting ruler, place, Lot, or timing testimony.

Procedure:

1. Treat body/material/regional correspondences as supplementary.
2. Use them to specify the field of manifestation after the main chain has been built.
3. Mark any medical or bodily claim as low confidence unless the project later approves a specialist module.

Guardrail:

Do not use these correspondences to produce medical claims or deterministic geographic claims in ordinary readings.

Destination rule file:

- `rules/delineation-output-rules.md`
- `rules/house-topic-framework.md`

Provenance: `[Valens *Anth.* I.1-I.2, PDF pp. 1-6]` `[new to Valens]`.

## Rule Card I.7 - Foundational Catalogues Must Be Routed Through Evidence Chains

Source: Book I.1-I.3, local PDF pp. 1-8.

Use when:

- extracting any Valens catalogue of planet/sign/degree meaning;
- deciding whether a catalogue item belongs in a functional rule file.

Procedure:

1. Convert catalogued meanings into possible evidence inputs.
2. Assign each input to a rule layer: natural significator, condition, place, Lot, configuration, timing, or specialist topic.
3. Require at least one chart-specific role before using the catalogue in output.
4. Preserve provenance and note whether Brennan overlaps.

Guardrail:

This is the anti-cookbook rule for Valens Book I.

Destination rule file:

- `rules/significator-hierarchy.md`
- `rules/delineation-output-rules.md`

Provenance: `[Valens *Anth.* I.1-I.3, PDF pp. 1-8]` `[project extraction heuristic]`.
