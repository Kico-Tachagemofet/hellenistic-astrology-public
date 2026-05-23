# Valens Extraction - Book VIII Tables And Ascendant Rectification

Source: Vettius Valens, `Anthologies`, Book VIII, Mark Riley translation.

Range: local PDF pp. 138-150.

Brennan cross-ref: `[cross-ref: Brennan Ch.11]`, `[cross-ref: Brennan Ch.17]`.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Method Takeaway

Book VIII is primarily computational: constructing tables, fixing the Ascendant degree, handling twins, calculating rising times, and using sample nativities. It is important for data-contract design, but most of it belongs in a future calculation/reference layer rather than interpretive rules.

## Rule Card VIII.1 - Table Construction Belongs In Reference Layer

Source: Book VIII.1-VIII.2, local PDF pp. 138-139.

Use when:

- reconstructing Valens' tables;
- validating table values;
- designing a future timing calculator.

Required data:

- table construction rules;
- rising-time values;
- degree ranges;
- sample checks.

Procedure:

1. Keep table construction separate from interpretive prose.
2. Store deterministic values in a reference file if Phase B approves.
3. Validate table output against examples before use.

Guardrail:

Status: needs verification. Do not hand-enter table values into rule prose.

Destination rule file:

- `rules/data_contract.md`
- `rules/timing-techniques.md`

Provenance: `[Valens *Anth.* VIII.1-VIII.2, PDF pp. 138-139]` `[new to Valens]`.

## Rule Card VIII.2 - Ascendant Rectification Requires Exact Inputs And Method Disclosure

Source: Book VIII.3 and VIII.5, local PDF pp. 139-142.

Use when:

- correcting or fixing an Ascendant degree;
- comparing table-derived Ascendant with supplied chart data;
- documenting historical rectification.

Required chart data:

- birth date and approximate time;
- Sun and Moon positions;
- table values;
- local rising times.

Procedure:

1. Identify the rectification method.
2. Record all input values.
3. Calculate the table-derived Ascendant.
4. Compare with the provided chart, if any.
5. Mark the result as reconstructed unless independently verified.

Guardrail:

Status: needs verification. Do not revise a user's chart data from this method without explicit task scope.

Destination rule file:

- `rules/data_contract.md`

Provenance: `[Valens *Anth.* VIII.3, VIII.5, PDF pp. 139-142]` `[cross-ref: Brennan Ch.11]`.

## Rule Card VIII.3 - Twin Analysis Depends On Small Timing Differences

Source: Book VIII.4, local PDF pp. 140-141.

Use when:

- discussing twin nativities;
- evaluating why close births diverge;
- assessing data sensitivity in ancient methods.

Required chart data:

- birth times of both nativities;
- Ascendant degrees;
- Moon motion and degree;
- table/rising-time values.

Procedure:

1. Compare exact birth times and Ascendant degrees.
2. Check lunar motion and table-derived shifts.
3. Identify which timing/degree change produces interpretive divergence.
4. Avoid broad claims if time data is approximate.

Guardrail:

Small time errors can matter. Do not overstate precision when the input time is rounded.

Destination rule file:

- `rules/data_contract.md`
- `rules/delineation-output-rules.md`

Provenance: `[Valens *Anth.* VIII.4, PDF pp. 140-141]` `[new to Valens]`.

## Rule Card VIII.4 - Rising Times And Three Factors Are Calculation Infrastructure

Source: Book VIII.6, local PDF pp. 142-148.

Use when:

- a method requires the three factors;
- calculating timing from rising times;
- checking Book VII/VIII computational consistency.

Required chart data:

- sign degrees;
- rising-time table;
- Sun/Moon/Ascendant factors required by the method.

Procedure:

1. Name the factors required.
2. Compute them in the order supplied by the source.
3. Use them only inside the relevant timing or rectification method.

Guardrail:

Status: needs verification. This is calculator infrastructure, not ordinary delineation content.

Destination rule file:

- `rules/data_contract.md`
- `rules/timing-techniques.md`

Provenance: `[Valens *Anth.* VIII.6, PDF pp. 142-148]` `[new to Valens]`.

## Rule Card VIII.5 - Sample Nativities Validate Calculation Paths

Source: Book VIII.7P-VIII.8K;9P, local PDF pp. 143-150.

Use when:

- checking table-derived methods;
- comparing computed results to Valens' examples;
- documenting edge cases.

Procedure:

1. Use sample nativities as validation cases.
2. Extract the calculation path, not portable character judgments.
3. Record discrepancies for later verification.

Guardrail:

Examples are not reusable delineation blocks.

Destination rule file:

- `rules/timing-techniques.md`
- `cases/` only in a later Phase C, not this plan

Provenance: `[Valens *Anth.* VIII.7P-VIII.8K;9P, PDF pp. 143-150]` `[project extraction heuristic]`.
