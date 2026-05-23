# Brennan Extraction — Chapter 16 Lots

Source: Chris Brennan, `Hellenistic Astrology: The Study of Fate and Fortune`, Chapter 16.

Scope:

- calculation and conceptualization of Lots;
- use of Lots in natal astrology;
- steps in analyzing a Lot;
- Lot of Fortune;
- other Hermetic Lots.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Chapter Range

- Printed pp. 511-533.
- Approx. PDF pp. 538-560.

## Method Takeaway

Lots are not decorative points. They are derived significators that assign additional topics to signs and can function like alternate anchors for specific layers of life.

The Lot of Fortune is especially important because it can be treated as a derived Ascendant for bodily, material, circumstantial, and fortune-related matters. The Lot of Spirit is paired with Fortune and becomes especially important for action, intention, and zodiacal releasing.

## Rule Card 16.1 — Lots As Derived Topic Anchors

Source: Ch. 16, use of Lots section, printed pp. 515-517; PDF pp. 542-544.

Use when:

- a topic needs a derived significator beyond the house ruler;
- cross-checking a topic house;
- building a secondary house system from a Lot;
- preparing timing techniques that release from Fortune or Spirit.

Required chart data:

- Ascendant degree;
- Sun degree;
- Moon degree;
- day/night sect;
- Lot formula used;
- Lot sign and degree;
- domicile ruler of Lot sign;
- planets configured to Lot.

Procedure:

1. Calculate or record the Lot using sect-correct formula.
2. Identify the sign and degree of the Lot.
3. Treat the Lot's sign as a derived anchor for its topic.
4. Audit the Lot's house placement relative to the Ascendant.
5. Audit the Lot ruler using `planet-condition-audit.md`.
6. Record planets co-present with or configured to the Lot.
7. Optionally derive houses from the Lot when the technique requires it.

Guardrail:

Do not interpret a Lot as a planet. It is a mathematical point whose ruler, placement, and witnesses carry the judgment.

Destination rule file:

- `rules/lots-and-fortune.md`
- `rules/data_contract.md`

Formula note:

- Fortune day formula: Ascendant + Moon - Sun.
- Fortune night formula: Ascendant + Sun - Moon.
- Source: Ch. 16, calculation section, printed pp. 512-513; PDF pp. 539-540.

## Rule Card 16.2 — Steps In Analyzing A Lot

Source: Ch. 16, steps in analyzing a Lot, printed p. 517; PDF p. 544.

Use when:

- any Lot is used as evidence.

Procedure:

1. Determine whether the Lot is in a good or difficult place.
2. Check planets co-present with the Lot.
3. Check benefics/malefics configured to the Lot.
4. Identify and audit the Lot ruler.
5. Check the Lot ruler's house placement and configurations.
6. If timing is involved, check whether the Lot, its ruler, or derived houses from the Lot are activated.

Output form:

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

Destination rule file:

- `rules/lots-and-fortune.md`

## Rule Card 16.3 — Lot Of Fortune As Material/Bodily Anchor

Source: Ch. 16, Lot of Fortune section, printed pp. 518-524; PDF pp. 545-551.

Use when:

- reading bodily, material, circumstantial, livelihood, or fortune-related themes;
- building derived houses from Fortune;
- preparing zodiacal releasing or other time-lord work.

Required chart data:

- Lot of Fortune sign and degree;
- Fortune ruler and condition;
- planets co-present/configured to Fortune;
- houses derived from Fortune if needed.

Procedure:

1. Treat Fortune as a major secondary anchor, comparable to a derived Ascendant for fortune/body/circumstance.
2. Judge Fortune's condition by place, ruler, and testimony.
3. Derive places from Fortune when the method calls for it.
4. Compare Fortune testimony with the Ascendant and Ascendant ruler.
5. If Fortune and Ascendant disagree, report the tension rather than forcing a single story.

Supporting evidence:

- Fortune in a strong/good place;
- Fortune ruler dignified, angular, of sect, bonified;
- benefics configured to Fortune;
- repeated testimony from Ascendant ruler or time lord.

Constraining evidence:

- Fortune in difficult place without mitigation;
- Fortune ruler maltreated, hidden, contrary to sect, or poorly placed;
- malefics configured to Fortune without reception.

Destination rule file:

- `rules/lots-and-fortune.md`

## Rule Card 16.4 — Fortune And Spirit Pairing

Source: Ch. 16, Lot calculations and other Lots, printed pp. 512-528; PDF pp. 539-555.

Use when:

- separating material circumstance from intentional action;
- preparing zodiacal releasing;
- reading life direction with both body/fortune and mind/spirit layers.

Procedure:

1. Calculate Fortune and Spirit using the correct day/night formula.
2. Treat Fortune as more bodily, material, circumstantial, and encounter-based.
3. Treat Spirit as more intentional, mental, volitional, and action-based.
4. Compare Fortune and Spirit signs, rulers, and conditions.
5. If they are configured or share rulers, note integration between circumstance and intention.
6. If they are in aversion or have sharply different conditions, mark tension between circumstance and chosen action.

Guardrail:

Do not over-psychologize Spirit or over-materialize Fortune without support from source and chart context. Keep the distinction operational.

Destination rule file:

- `rules/lots-and-fortune.md`
- `rules/timing-techniques.md`

Formula note:

- Fortune: day = Ascendant + Moon - Sun; night = Ascendant + Sun - Moon.
- Spirit: day = Ascendant + Sun - Moon; night = Ascendant + Moon - Sun.
- Source: Ch. 16, Fortune/Spirit calculation rationale and Hermetic Lots, printed pp. 521-522 and 525; PDF pp. 548-549 and 552.

## Rule Card 16.5 — Other Lots Are Topic-Specific Witnesses

Source: Ch. 16, survey of other Lots, printed pp. 524-533; PDF pp. 551-560.

Use when:

- a topic-specific Lot is clearly relevant;
- the chart data includes formulas and calculated positions;
- a source track supports the Lot's use.

Procedure:

1. Identify the Lot and its topic.
2. Record formula and source.
3. Analyze it with the same Lot procedure: place, ruler, co-presence, configurations.
4. Keep secondary Lots below Ascendant, topic house, Fortune/Spirit, and time-lord evidence unless repeatedly supported.

Guardrail:

Do not clutter first-pass readings with many Lots. Use Fortune and Spirit first; add other Lots only when the question demands it.

Destination rule file:

- `rules/lots-and-fortune.md`

## Open Questions

- Resolved for v1: exact Fortune and Spirit formulas have been added to `rules/lots-and-fortune.md`. Other Lots still require formula/source before use.
- Need cross-check with Brennan Chapter 18 before locking Fortune/Spirit use in zodiacal releasing.
- Need decide whether the reader skill computes Lots or requires a chart calculator export.
