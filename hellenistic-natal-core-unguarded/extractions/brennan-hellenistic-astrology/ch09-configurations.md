# Brennan Extraction — Chapter 9 Configurations

Source: Chris Brennan, `Hellenistic Astrology: The Study of Fate and Fortune`, Chapter 9.

Scope:

- witnessing/testimony;
- the five configurations;
- sign-based configurations;
- degree-based configurations;
- aversion;
- qualities of configurations;
- right/left and overcoming;
- mitigation and alternative aspect doctrines.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Chapter Range

- Printed pp. 289-317.
- Approx. PDF pp. 316-344.

## Method Takeaway

Configurations are not just modern aspects as psychological dynamics. In the Hellenistic frame, they answer a more basic question first:

```text
Can these planets see, witness, testify to, or act upon one another?
```

Only after establishing witnessing does the reader judge quality, direction, superiority, and exactness.

## Rule Card 9.1 — Witnessing Before Interpretation

Source: Ch. 9, witnessing/testimony section, printed pp. 291-294; PDF pp. 318-321.

Use when:

- evaluating whether two significators are connected;
- deciding whether a planet can modify another planet's significations;
- preventing unsupported blending of two unrelated chart factors.

Required chart data:

- signs and degrees of both planets;
- recognized configuration by sign;
- degree proximity if available.

Procedure:

1. Identify whether the signs are configured by one of the recognized relationships.
2. If configured, mark the planets as able to witness or testify to one another.
3. If not configured, mark aversion or lack of direct witnessing.
4. Do not blend the two factors as a direct relationship unless another linkage exists: rulership, antiscia, Lot, time-lord activation, co-presence by derived topic, etc.

Guardrail:

No witnessing means no direct aspect testimony. Keep unconnected symbols separate unless another rule links them.

Destination rule file:

- `rules/aspect-reception-rules.md`

## Rule Card 9.2 — Sign-Based Configuration Is The Baseline

Source: Ch. 9, sign-based configurations section, printed pp. 296-300; PDF pp. 323-327.

Use when:

- building the first relationship map of the chart;
- finding which planets can see a house or planet.

Procedure:

1. Use whole signs to identify co-presence, sextile, square, trine, opposition, and aversion.
2. Treat sign-based configuration as a real connection even if degrees are not close.
3. Use degree closeness to weight intensity, but do not erase or invalidate the sign-based relationship.
4. Do not let degree proximity to a non-sign-aligned configuration change the aspect family; use the sign-based family and record the degree separation only as secondary intensity/background information.
5. Mark aversion houses/signs as places where direct testimony is absent.

Guardrail:

Do not apply an orb gate to sign-based configuration. Brennan emphasizes that planets begin aspecting each other as soon as they move into configured signs, with closeness to exact degree increasing intensity. Source: Ch. 9, printed pp. 296-304; PDF pp. 323-331.

Output:

```text
Sign-based relationship:
Degree-based closeness:
Witnessing present/absent:
Relationship weight:
```

Destination rule file:

- `rules/aspect-reception-rules.md`
- `rules/data_contract.md`

## Rule Card 9.3 — Degree-Based Contact Intensifies Testimony

Source: Ch. 9, degree-based configurations section, printed pp. 300-305; PDF pp. 327-332.

Use when:

- judging how active or precise an aspect is;
- event-like or timing interpretation depends on perfection/application.

Procedure:

1. Start with sign-based configuration.
2. Check exact degree relationship or closeness.
3. Mark degree-based contact as stronger, more precise, and more active than loose sign-based testimony.
4. For event-like readings, distinguish applying from separating.
5. Avoid using modern orb habits without source-specific justification.

Working distinction:

```text
Sign-based = planets can see/testify.
Degree-based = the testimony is sharper, more exact, and often more operational.
```

Destination rule file:

- `rules/aspect-reception-rules.md`

## Rule Card 9.4 — Configuration Quality Is Structural, Then Contextual

Source: Ch. 9, qualities of configurations section, printed pp. 305-309; PDF pp. 332-336.

Use when:

- deciding whether a configuration supports, strains, blocks, or confronts.

Procedure:

1. Identify configuration type: conjunction, sextile, square, trine, opposition.
2. Apply its baseline quality.
3. Modify by planets involved, sect, dignity, reception, and topic.
4. Do not reduce all squares/oppositions to bad and all trines/sextiles to good without condition context.

Baseline:

- conjunction: co-presence, bodily mixing, shared place;
- sextile: cooperative but weaker connection;
- square: conflict, action, pressure, contest, forcing;
- trine: easy testimony, support, coherence;
- opposition: confrontation, polarity, separation, direct standoff.

Destination rule file:

- `rules/aspect-reception-rules.md`

## Rule Card 9.5 — Right/Left And Overcoming Give Direction

Source: Ch. 9, right/left and overcoming sections, printed pp. 309-315; PDF pp. 336-342.

Use when:

- deciding which planet has superior position and acts more strongly;
- interpreting square/trine/sextile relationships where direction matters;
- adding force/dominance to benefic/malefic testimony.

Procedure:

1. Identify the configuration by sign.
2. Determine which planet is in the superior/right-hand position relative to the other.
3. Mark the superior planet as overcoming the inferior one.
4. If superior planet is benefic and in condition, mark strong support/protection.
5. If superior planet is malefic and especially contrary to sect or damaged, mark stronger pressure/maltreatment.
6. If planets are neutral or mixed, read overcoming as directional influence rather than automatic good/bad.

Guardrail:

Do not treat a square or trine as symmetrical. The direction of testimony changes the judgment.

v1 implementation note:

- `[project heuristic]` For the first natal core, evaluate direction only for hard testimony. For squares, compute overcoming/superior position. For oppositions, record direct confrontation/polarity as hard testimony without assigning a trine/sextile-style superior side. For trine and sextile, record `superiority not evaluated in v1` and continue with witnessing, degree closeness, condition, and reception. This avoids overextending the current rule table before a right/left diagram is added.

Destination rule file:

- `rules/aspect-reception-rules.md`

## Rule Card 9.6 — Aversion As Missing Direct Testimony

Source: Ch. 9, sign-based configurations and alternative doctrines, printed pp. 296-317; PDF pp. 323-344.

Use when:

- two relevant significators are not in a recognized configuration;
- a topic house cannot see the Ascendant or its ruler;
- explaining weak connection or lack of direct coordination.

Procedure:

1. Identify aversion by sign relationship.
2. Mark lack of direct witnessing.
3. Look for indirect links: domicile rulership, reception, translation, collection, time lord, Lots, or co-activation.
4. If no indirect link exists, keep the testimony weak or absent.

Guardrail:

Aversion is not always disaster; it is missing direct sight/contact. Judge by whether indirect links compensate.

Destination rule file:

- `rules/aspect-reception-rules.md`
- `rules/delineation-output-rules.md`

## Open Questions

- Need a diagram/table for right/left overcoming by sign distance.
- Need later comparison with Demetra George for teaching-friendly terminology.
- Need decide whether the skill should require degree-based aspect data or compute it from chart positions.
