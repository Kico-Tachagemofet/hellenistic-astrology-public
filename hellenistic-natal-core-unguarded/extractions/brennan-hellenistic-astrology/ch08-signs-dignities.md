# Brennan Extraction - Chapter 8 Signs and Dignities

Source: Chris Brennan, `Hellenistic Astrology: The Study of Fate and Fortune`, Chapter 8.

Scope:

- signs as structured zodiacal environments;
- masculine/feminine signs, quadruplicities, elements, and triplicities;
- domicile rulership and the host/guest metaphor;
- exaltation and depression/fall;
- adversity/exile opposite domicile;
- Egyptian bounds and Chaldean-order decans;
- planets in signs as condition evidence, not cookbook delineation.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Chapter Range

- Printed pp. 213-288.
- Approx. PDF pp. 240-315.

## Method Takeaway

Chapter 8 should be used as the project's deterministic dignity and sign-condition layer. Signs are not standalone personality paragraphs. A sign describes the environment, host, resources, and subdivisions through which a planet acts.

For the future skill, the rule is:

```text
Planet nature supplies the actor.
Sign and dignity describe the actor's environment and authority.
The sign ruler's condition decides how the environment actually supports or constrains.
```

## Rule Card 8.1 - Sign Properties Are Modifiers, Not Readings

Source: Ch. 8, sign classifications and qualities, printed pp. 224-228 and 253-266; PDF pp. 251-255 and 280-293.

Use when:

- recording a planet's sign environment;
- using masculine/feminine, movable/fixed/double-bodied, or elemental/triplicity properties;
- preventing sign keywords from becoming a full delineation.

Required chart data:

- planet or point by sign;
- topic role of the planet or point;
- whether the property is being used literally, symbolically, or as condition context.

Procedure:

1. Classify the sign by gender/polarity, quadruplicity, and triplicity/element.
2. Treat those classifications as modifiers to the planet's expression.
3. Use literal sign-property claims only when the topic and source logic justify it.
4. Do not infer outcome from sign classification alone.
5. Route any judgment back through the planet's role, dignity, ruler, house, and testimony.

Guardrail:

A sign label is not evidence by itself. It becomes evidence only after it is attached to a planet, point, ruler-chain, Lot, or timing activation.

Destination rule file:

- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

## Rule Card 8.2 - Domicile Rulership As Host And Authority

Source: Ch. 8, Thema Mundi and domicile rulership sections, printed pp. 228-241; PDF pp. 255-268.

Use when:

- determining the ruler of a sign or house;
- judging whether a planet is in its own domicile;
- evaluating reception or host support;
- tracing a topic through its domicile lord.

Required chart data:

- sign occupied by the planet, Lot, house, or point;
- domicile ruler of that sign;
- condition of the domicile ruler;
- whether the planet is host, guest, tenant, topic ruler, or significator.

Procedure:

1. Look up the domicile ruler of the sign.
2. If the planet is in its own domicile, mark strong internal authority.
3. If the planet is in another planet's domicile, treat it as a guest depending on the host.
4. Judge the host's condition before deciding whether the guest receives support or trouble.
5. Use domicile rulership as the first ruler-chain for houses, Lots, and topic fields.

Guardrail:

Do not stop at "planet in sign." The host planet's condition is part of the evidence chain.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`
- `rules/significator-hierarchy.md`
- `rules/aspect-reception-rules.md`

## Rule Card 8.3 - Exaltation And Depression/Fall

Source: Ch. 8, exaltations and depressions section, printed pp. 242-248; PDF pp. 269-275.

Use when:

- judging elevated or lowered planetary condition;
- identifying exaltation reception;
- deciding whether a planet has special honor or loss of standing in a sign.

Required chart data:

- planet and sign;
- degree only if a specific technique uses exaltation degrees;
- other condition factors: sect, house, visibility, aspects, ruler condition.

Procedure:

1. Look up whether the planet is in its exaltation sign.
2. Look up whether the planet is in the opposite sign, its depression/fall.
3. Treat exaltation as raised, honored, or esteemed condition.
4. Treat depression/fall as lowered, reduced, or dejected condition.
5. Use exaltation degrees only for techniques that explicitly require them.

Guardrail:

Exaltation is not automatic success, and fall is not automatic ruin. Both must be judged with sect, house, ruler condition, and testimony.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`
- `rules/aspect-reception-rules.md`

## Rule Card 8.4 - Adversity Or Exile Opposite Domicile

Source: Ch. 8, adversities section, printed pp. 249-252; PDF pp. 276-279.

Use when:

- evaluating a planet in the sign opposite one of its domiciles;
- translating later "detriment" language into the Hellenistic evidence chain;
- distinguishing fall from opposition-to-domicile adversity.

Required chart data:

- planet and sign;
- planet's domicile signs;
- domicile ruler of the occupied sign;
- host condition and other mitigations.

Procedure:

1. Check whether the planet is in a sign opposite one of its own domiciles.
2. If so, mark adversity/exile/debility as a negative internal condition.
3. Read the placement through opposition to the planet's home territory and dependence on a contrary host.
4. Keep the term "detriment" available for compatibility, but prefer "adversity" or "exile" in Hellenistic-facing prose.
5. Use mitigation from sect, house, reception, and benefic testimony before writing final judgment.

Guardrail:

The concept is less consistently defined in early Hellenistic introductions than domicile, exaltation, and depression. Do not import a later scoring system without marking the scoring method as `needs verification`.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`

## Rule Card 8.5 - Triplicity Rulers Are Sect-Dependent Dignity

Source: Ch. 8, triplicities section, printed pp. 256-272, especially pp. 267-268; PDF pp. 283-299, especially pp. 294-295.

Use when:

- assigning triplicity dignity;
- judging whether a planet has sect-dependent support in a sign;
- preparing for triplicity ruler techniques in Chapter 15.

Required chart data:

- sign and triplicity/element;
- day or night chart;
- planet being judged;
- whether the triplicity ruler is primary, secondary, or cooperating.

Procedure:

1. Identify the sign's triplicity: fire, earth, air, or water.
2. Determine chart sect.
3. Use the standard Dorothean scheme by default.
4. Mark the in-sect primary ruler, secondary ruler, and cooperating ruler.
5. Treat triplicity as condition/support evidence, not as a replacement for domicile rulership.

Guardrail:

Do not silently substitute Ptolemy's alternative triplicity scheme. Use it only if a reading explicitly asks for a Ptolemaic variant.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`
- `rules/timing-techniques.md`

## Rule Card 8.6 - Bounds Are Degree-Level Territory

Source: Ch. 8, subdivisions and bounds sections, printed pp. 275-279; PDF pp. 302-306.

Use when:

- exact degree is known;
- identifying the bound ruler of a planet or point;
- adding degree-level dignity or constraint to condition audit;
- preparing for length-of-life or circumambulation techniques later.

Required chart data:

- sign and exact degree within sign;
- Egyptian bounds table;
- bound ruler's natal condition.

Procedure:

1. Use the Egyptian bounds as the default Hellenistic bound table.
2. Locate the planet's degree in the sign's half-open interval.
3. Mark the bound ruler as a localized ruler of that degree territory.
4. Judge whether the planet is in its own bound or under another planet's bound.
5. Use the bound ruler's condition as secondary evidence.

Guardrail:

Do not infer bounds from rounded or missing degree data. Sun and Moon are not bound rulers in the Egyptian scheme.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`
- future circumambulation or length-of-life module

## Rule Card 8.7 - Decans Or Faces Are Subordinate Modifiers

Source: Ch. 8, decans or faces section, printed pp. 279-283; PDF pp. 306-310.

Use when:

- exact degree is known;
- identifying decan/face ruler as a minor dignity or descriptive modifier;
- comparing subdivisions inside a sign.

Required chart data:

- sign and exact degree within sign;
- decan table;
- planet or point being judged.

Procedure:

1. Split each sign into three ten-degree decans: [0,10), [10,20), [20,30).
2. Use the Chaldean-order planetary sequence starting with Mars in the first decan of Aries.
3. Mark the decan ruler as a low-weight modifier.
4. Keep decan evidence below domicile, exaltation, triplicity, bounds, sect, house, and testimony unless a specific technique foregrounds decans.

Guardrail:

Do not confuse decan/face rulership with the separate doctrine of "proper face." Mark proper-face interpretation as out of scope for the first natal core.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`

## Rule Card 8.8 - Planets In Signs Require Ruler And Condition

Source: Ch. 8, interpreting planets in signs section, printed pp. 287-288; PDF pp. 314-315.

Use when:

- writing any planet-in-sign delineation;
- deciding whether a sign placement is helpful, difficult, visible, obscure, strong, or compromised.

Required chart data:

- planet nature;
- sign occupied;
- sign ruler and its condition;
- essential dignity and adversity/fall status;
- house, sect, visibility, motion, and testimony.

Procedure:

1. Start with the planet's natural role.
2. Add the sign environment and dignity state.
3. Judge the domicile lord as host.
4. Add degree-level rulers only if exact degree is available.
5. Convert the result into evidence, not a standalone cookbook paragraph.

Guardrail:

"Planet in sign" is not a complete statement. It must be connected to role, host, dignity, house, and testimony.

Destination rule file:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

## Open Questions

- Need Demetra George cross-check for dignity weighting and whether the first skill should expose any numeric dignity scoring.
- Adversity/exile is usable as a condition flag, but later scoring language should remain `needs verification` until compared with additional sources.
- Decans should stay low-weight in the first natal core unless a future technique explicitly requires them.
