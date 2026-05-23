# Valens Extraction - Book VII Time-Lord Lifespans

Source: Vettius Valens, `Anthologies`, Book VII, Mark Riley translation.

Range: local PDF pp. 124-137.

Brennan cross-ref: `[cross-ref: Brennan Ch.16]`, `[cross-ref: Brennan Ch.17]`, `[cross-ref: Brennan Ch.18]`.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Method Takeaway

Book VII continues Valens' advanced timing and lifespan methods, combining houseruler, rising times, Ascendant, Fortune, star periods, and fractional periods. It should be stored as source material for future timing architecture, not merged directly into v1 natal-core.

## Rule Card VII.1 - Advanced Timing Requires Method Order

Source: Book VII.1P and VII.1K;2P, local PDF pp. 124-125.

Use when:

- running any advanced Valens time-lord method;
- comparing multiple candidate timing methods;
- preventing cherry-picking from timing tables.

Required chart data:

- selected method;
- starting anchor;
- rising times;
- houseruler or time lord;
- active periods.

Procedure:

1. Name the method.
2. Identify the anchor and required data.
3. Complete the calculation in source order.
4. Only then interpret the resulting active planet/sign.

Guardrail:

Do not mix steps from different Valens methods unless the source explicitly instructs comparison.

Destination rule file:

- `rules/timing-techniques.md`

Provenance: `[Valens *Anth.* VII.1P-VII.1K;2P, PDF pp. 124-125]` `[new to Valens]`.

## Rule Card VII.2 - Rising Times And Star Periods Combine In Time-Lord Work

Source: Book VII.2K;3P, local PDF pp. 125-128.

Use when:

- a distribution uses both sign rising times and planetary period values;
- calculating a period length or transition;
- comparing sign-based and planet-based time allotments.

Required chart data:

- klima/rising times;
- planet period table;
- sign and planet positions;
- active anchor.

Procedure:

1. Identify sign rising time values.
2. Identify the relevant planetary periods.
3. Combine them according to the method.
4. Use the result as timing duration, not as natal interpretation by itself.

Guardrail:

Status: needs verification. Rising-time and star-period calculations need deterministic table support.

Destination rule file:

- `rules/timing-techniques.md`
- `rules/data_contract.md`

Provenance: `[Valens *Anth.* VII.2K;3P, PDF pp. 125-128]` `[new to Valens]`.

## Rule Card VII.3 - Fortune Ruler Can Anchor Lifespan Timing

Source: Book VII.3K;4P, local PDF pp. 128-129.

Use when:

- researching Fortune-based length-of-life methods;
- comparing Fortune ruler with Ascendant ruler and luminaries;
- evaluating whether Fortune participates in timing.

Required chart data:

- Fortune sign/degree;
- Fortune ruler;
- condition and configurations of Fortune ruler;
- period/rising-time data.

Procedure:

1. Locate Fortune and its ruler.
2. Audit Fortune ruler's condition.
3. Apply the period calculation only if data is complete.
4. Compare against other aphetic methods.

Guardrail:

Status: needs verification. This is not ordinary Fortune delineation.

Destination rule file:

- `rules/lots-and-fortune.md`
- `rules/timing-techniques.md`

Provenance: `[Valens *Anth.* VII.3K;4P, PDF pp. 128-129]` `[cross-ref: Brennan Ch.16]`.

## Rule Card VII.4 - Precision Timing Still Requires Natal Context

Source: Book VII.4K;5P, local PDF pp. 129-130.

Use when:

- a method claims precise propitious or impropitious timing;
- exact rising times and star periods are available;
- checking event timing against natal promise.

Required chart data:

- exact positions;
- rising times;
- period table;
- natal condition of active factors.

Procedure:

1. Calculate the precise timing factor.
2. Identify active planet/sign.
3. Return to natal configuration and topic houses.
4. Interpret the period as activation of natal testimony.

Guardrail:

Precision in calculation does not remove interpretive uncertainty.

Destination rule file:

- `rules/timing-techniques.md`
- `rules/delineation-output-rules.md`

Provenance: `[Valens *Anth.* VII.4K;5P, PDF pp. 129-130]` `[cross-ref: Brennan Ch.17]`.

## Rule Card VII.5 - Fractional Periods Multiply Operative Testimony

Source: Book VII.5K;6P, local PDF pp. 130-137.

Use when:

- a method applies one-half, one-third, or two-thirds of rising times or star periods;
- multiple planets become operative together;
- interpreting why a period has blended outcomes.

Required chart data:

- base period;
- fraction used;
- planets/signs included;
- their natal conditions and topics.

Procedure:

1. Determine the base period.
2. Apply the specified fraction.
3. List all planets/signs made operative by the fractional method.
4. Judge the blend by independent condition audits.

Guardrail:

Status: needs verification. Fractional period math must be checked before implementation.

Destination rule file:

- `rules/timing-techniques.md`

Provenance: `[Valens *Anth.* VII.5K;6P, PDF pp. 130-137]` `[new to Valens]`.
