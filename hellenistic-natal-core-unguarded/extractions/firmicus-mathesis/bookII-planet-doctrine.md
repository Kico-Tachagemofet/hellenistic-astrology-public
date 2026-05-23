# Firmicus Extraction - Book II Planet Doctrine and Foundations

Source: Julius Firmicus Maternus, *Mathesis*, Book II, translated by Jean
Rhys Bram, *Ancient Astrology Theory and Practice*.

Scope:

- basic training order;
- signs, domiciles, exaltations/falls, decans, bounds/terms;
- sect and solar phase;
- houses, angles, aversion, and house topics;
- aspect families, right/left aspects, and antiscia;
- chronocrator/time allotments;
- astrologer ethics and output restraint.

Copyright note: this file paraphrases method and stores page references. It
does not reproduce long source passages.

## Chapter Range

- Bram printed pp. 31-70.
- PDF pp. 35-74.

## Method Takeaway

Book II repeatedly requires the reader to collect condition data before making
a forecast: sign, degree, term, decan, house, house ruler, sect, benefic/malefic
testimony, and hidden testimony such as antiscia. Its strongest contribution to
the project is not a placement catalog, but a process rule:

```text
Do not judge a planet, house, or topic from the placement alone; inspect its
host, sect, condition, aspects, and hidden relationships before synthesis.
```

## Rule Card 2.1 - Foundations Before Forecasting

Source: [Firmicus *Math.* II.Praef.] Bram printed p. 31.

Use when:

- sequencing extraction or reading workflow;
- deciding whether a method can be applied before the required data is known.

Required chart data:

- Not chart-specific; this is a workflow rule.

Procedure:

1. Establish the foundational schema before forecasting: signs, dignities,
   houses, aspects, timing, and antiscia.
2. Treat advanced judgments as invalid if the basic schema is missing or
   contradicted by source-specific requirements.
3. Keep antiscia in the foundational toolkit, but do not apply it until the
   normal aspect map has been checked.

Guardrail:

Do not use Book II as a shortcut for final delineation. It is mostly a data and
method layer.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]
- [cross-ref: Brennan Ch.9]
- [cross-ref: Brennan Ch.10]

Destination:

- `rules/reading-workflow.md`
- `rules/data_contract.md`

Status: extracted.

## Rule Card 2.2 - Sign Gender and Domicile Symmetry

Source: [Firmicus *Math.* II.1-2] Bram printed p. 32.

Use when:

- checking domicile rulership and sign gender;
- comparing Firmicus with the existing dignity table.

Required chart data:

- sign placements;
- chart sect only if the gender note is being used in a sect-sensitive
  argument.

Procedure:

1. Use the standard twelve signs.
2. Mark masculine signs: Aries, Gemini, Leo, Libra, Sagittarius, Aquarius.
3. Mark feminine signs: Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces.
4. Use standard domiciles:
   - Sun: Leo
   - Moon: Cancer
   - Saturn: Capricorn, Aquarius
   - Jupiter: Sagittarius, Pisces
   - Mars: Aries, Scorpio
   - Venus: Taurus, Libra
   - Mercury: Gemini, Virgo
5. Do not treat sign gender alone as a delineation. It is supporting data.

Guardrail:

Firmicus frames each non-luminary planet as holding one masculine and one
feminine domicile. This supports schema symmetry, not a standalone judgment.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]

Destination:

- `rules/dignities-reference.md`

Status: extracted.

## Rule Card 2.3 - Exaltation and Fall as Exact-Degree Dignity

Source: [Firmicus *Math.* II.3] Bram printed pp. 32-34.

Use when:

- checking exaltation/fall;
- evaluating whether exact degree dignity is being overclaimed.

Required chart data:

- planet sign and exact degree.

Procedure:

1. Mark exaltation/fall by the traditional planet-sign pairing.
2. Firmicus emphasizes the exact exaltation/fall degree as the maximum point of
   strength or loss.
3. If many planets are at their exact exaltation degrees, mark a strong
   prosperity testimony.
4. If many planets are at exact fall degrees, mark a strong debility testimony.
5. Outside exact-degree techniques, retain the existing project convention:
   sign-level exaltation/fall counts, but exact degrees are extra evidence only
   when exact degrees are available.

Data:

| Planet | Exaltation degree | Fall degree |
|---|---|---|
| Sun | Aries 19 | Libra 19 |
| Moon | Taurus 3 | Scorpio 3 |
| Saturn | Libra 21 | Aries 21 |
| Jupiter | Cancer 15 | Capricorn 15 |
| Mars | Capricorn 28 | Cancer 28 |
| Venus | Pisces 27 | Virgo 27 |
| Mercury | Virgo 15 | Pisces 15 |

Guardrail:

Firmicus says exaltations are more favorable than domiciles in this doctrine.
Do not import that as a universal project ranking until Phase B compares it
against Brennan and other v2.1 sources.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]

Destination:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`

Status: extracted; Phase B comparison needed.

## Rule Card 2.4 - Decan as Own-Sign-Like Support

Source: [Firmicus *Math.* II.4] Bram printed pp. 34-36.

Use when:

- exact degree is known;
- evaluating minor dignity or face/decan testimony.

Required chart data:

- planet sign and exact degree;
- decan ruler table.

Procedure:

1. Divide each sign into three 10-degree decans.
2. If a planet is in its own decan, Firmicus treats it as acting similarly to a
   planet in its own sign.
3. Use this as a dignity testimony, not as final judgment.
4. Keep decan spirits / `munifices` deferred; Firmicus says he is not treating
   that layer here.

Guardrail:

Project v1 currently treats decans as low-weight modifiers. Firmicus gives
them stronger language, but Phase B must decide whether this changes weighting.
The OCR read for Leo's third decan conflicts with the standard Chaldean order;
verify against page image before using Firmicus as a table source.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]

Destination:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`

Status: extracted; needs verification for table variants.

## Rule Card 2.5 - Bounds/Terms as Local Dignity

Source: [Firmicus *Math.* II.5-6] Bram printed pp. 36-38.

Use when:

- exact degree is known;
- auditing essential dignity;
- checking whether a planet has local authority even outside its own sign.

Required chart data:

- exact degree of the planet;
- bounds/terms table.

Procedure:

1. Check the planet's term/bound ruler.
2. If a planet is in its own terms, Firmicus treats it as similar to being in
   its own sign.
3. Use term dignity as support for the planet's capacity, especially when
   domicile/exaltation is absent.
4. Do not calculate terms from rounded or sign-only data.

Guardrail:

The table in Firmicus II.6 appears to match the current project Egyptian bounds
table. Preserve this as a cross-source confirmation rather than a new table
unless Phase B finds variants.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]

Destination:

- `rules/dignities-reference.md`
- `rules/planet-condition-audit.md`

Status: extracted.

## Rule Card 2.6 - Sect Rejoicing by Day and Night

Source: [Firmicus *Math.* II.7] Bram printed p. 38.

Use when:

- checking whether a planet is favored by chart sect;
- comparing Firmicus's sect scheme against v1.

Required chart data:

- diurnal/nocturnal chart;
- planet placements and houses.

Procedure:

1. In Firmicus, Sun, Jupiter, and Saturn rejoice by day and follow the Sun.
2. Moon, Venus, Mars, and Mercury rejoice by night and follow the Moon.
3. If planets of the chart's condition are favorably placed, mark prosperity
   testimony.
4. If planets of the contrary condition occupy important places, mark contrary
   or difficult testimony.

Guardrail:

Firmicus assigns Mercury to the nocturnal group here. This differs from the
project's current Mercury handling, which depends on visibility/solar phase.
Mark this as a Phase B comparison point, not an immediate replacement.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]

Destination:

- `rules/planet-condition-audit.md`

Status: extracted; cross-source tension with current Mercury rule.

## Rule Card 2.7 - Moon Phase Modifies Venus/Mars Contacts

Source: [Firmicus *Math.* II.7] Bram printed p. 38.

Use when:

- judging Moon contact with Venus or Mars;
- checking Firmicus-specific lunar phase doctrine.

Required chart data:

- chart sect;
- Moon phase: waxing/full/waning;
- Moon aspects to Venus and Mars.

Procedure:

1. In a nocturnal chart, if Venus and Mars aspect the waning Moon, Firmicus
   marks prosperity testimony.
2. If the full or waxing Moon comes into contact with Venus or Mars, Firmicus
   marks danger or difficulty testimony.
3. Treat this as a source-specific rule that must be cross-checked with Book IV,
   where lunar application and separation are developed in detail.

Guardrail:

Do not generalize "Venus is harmful to the waxing Moon" into all sources. Keep
it tagged to Firmicus until Phase B comparison.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [new to Firmicus]

Destination:

- `rules/planet-condition-audit.md`
- `rules/aspect-reception-rules.md`

Status: extracted; needs cross-check with Book IV.

## Rule Card 2.8 - Solar Phase and Visibility Thresholds

Source: [Firmicus *Math.* II.8-9] Bram printed pp. 38-39.

Use when:

- auditing visibility, combustion/hidden status, morning/evening rising;
- comparing solar phase thresholds.

Required chart data:

- planet longitude;
- Sun longitude;
- whether planet precedes or follows the Sun zodiacally / by rising order.

Procedure:

1. Classify planets as:
   - matutine: rising before the Sun;
   - vespertine: rising after the Sun;
   - hidden / under the Sun's rays: concealed by the Sun;
   - acronyctal: rising when the Sun sets.
2. Firmicus gives minimum distances for morning or evening classification:
   - Saturn: 15 degrees
   - Jupiter: 12 degrees
   - Mars: 8 degrees
   - Venus: 8 degrees
   - Mercury: 18 degrees
3. Mark nearness to the Sun as generally harmful.
4. Mark morning-rising planets as strengthened in relation to the Sun.
5. Mark evening-rising planets as weakened in Firmicus's summary statement.
6. Record Firmicus's caveat that some astrologers treat Mars under the Sun's
   rays as less malefic because the Sun subdues him.

Guardrail:

Do not collapse these thresholds into the current v1 visibility bins without
Phase B review. Firmicus's thresholds are planet-specific and tied to
matutine/vespertine status.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]

Destination:

- `rules/planet-condition-audit.md`
- `rules/data_contract.md`

Status: extracted.

## Rule Card 2.9 - Sign Nature as Secondary Modifier

Source: [Firmicus *Math.* II.10] Bram printed pp. 39-40.

Use when:

- a Firmicus rule explicitly depends on sign quality, shape, fertility, mutability,
  or elemental character;
- interpreting why an outcome varies by sign.

Required chart data:

- sign placement;
- relevant sign classifications.

Procedure:

1. Use sign nature as a modifier to condition logic, not as a standalone
   delineation.
2. If an outcome changes "according to the quality of the signs," inspect
   whether the sign is tropical, solid/fixed, double-bodied, watery, fertile,
   bestial, etc.
3. Record any missing or lacunose sign descriptions as source limits rather than
   filling the gap from common knowledge.

Guardrail:

The Book II sign-characteristic section is visibly lacunose in the English PDF
OCR. Do not reconstruct the full sign list from elsewhere in this extraction.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]

Destination:

- `rules/house-topic-framework.md`
- `rules/planet-condition-audit.md`

Status: partial; source lacuna / OCR limits.

## Rule Card 2.10 - Regional Rising Times Are Data-Limited

Source: [Firmicus *Math.* II.11] Bram printed pp. 40-42.

Use when:

- evaluating Firmicus's regional rising-time doctrine;
- deciding whether to include sign rising duration in a natal audit.

Required chart data:

- birth region/latitude or a source-specific region table;
- sign rising times.

Procedure:

1. Firmicus says planets reach maximum predictive force when their signs are
   rising.
2. He gives region-specific sign rising tables for Alexandria/Babylonia, Rhodes,
   the Hellespont, Athens, Ancona, and Rome.
3. Treat this as a latitude/rising-time technique requiring regional data.

Guardrail:

Do not use these tables in v1-style readings unless the data contract has a
defined latitude/rising-time source. Mark as deferred for Phase B or later.

Brennan cross-ref:

- [cross-ref: Brennan Ch.11]

Destination:

- `rules/data_contract.md`
- `rules/timing-techniques.md`

Status: extracted; deferred.

## Rule Card 2.11 - Wind Allocations Are Environmental Context

Source: [Firmicus *Math.* II.12] Bram printed p. 42.

Use when:

- a later Firmicus rule invokes winds or environmental direction.

Required chart data:

- sign placements;
- environmental forecasting context.

Procedure:

1. Record Firmicus's wind allocation:
   - north: Aries, Leo, Sagittarius;
   - south: Taurus, Virgo, Capricorn;
   - east: Gemini, Libra, Aquarius;
   - southwest: Cancer, Scorpio, Pisces.
2. Use only when the source explicitly needs wind/directional context.

Guardrail:

This is not part of the current natal-core workflow. Do not introduce it into
ordinary delineation without a trigger.

Brennan cross-ref:

- [new to Firmicus]

Destination:

- deferred / source reference.

Status: extracted; deferred.

## Rule Card 2.12 - Duodecatemoria Calculation and Hidden Condition

Source: [Firmicus *Math.* II.13] Bram printed pp. 42-43.

Use when:

- exact degree is available;
- a Firmicus technique calls for hidden subdivisions of a planet's placement.

Required chart data:

- planet sign, degree, and minutes;
- term/bound table for the resulting position.

Procedure:

1. Multiply the planet's degree and minutes within its sign by twelve.
2. Count the resulting distance through the zodiac starting from the planet's
   own sign.
3. The sign/degree where the count lands is the planet's duodecatemorion.
4. Inspect the resulting sign, term, decan, and condition as hidden testimony.

Guardrail:

Exact degree and minute data are required. Do not compute from rounded
placements. Keep this as optional until case-tested.

Brennan cross-ref:

- [new to Firmicus]

Destination:

- `rules/data_contract.md`
- deferred technique notes.

Status: extracted; deferred.

## Rule Card 2.13 - Compound Condition Can Override Simple Benefic/Malefic Labels

Source: [Firmicus *Math.* II.13] Bram printed p. 43.

Use when:

- a benefic seems unable to help;
- a malefic seems especially empowered;
- preventing single-factor benefic/malefic judgment.

Required chart data:

- planet sign, house, term, decan, and condition;
- aspects from malefics/benefics;
- relevant hidden testimony if using duodecatemoria.

Procedure:

1. Check whether Jupiter's helpfulness is hindered by sign weakness, degree,
   decan, condition, house, or malefic attack.
2. Check whether Saturn's harmfulness is intensified by house, terms, decan,
   sign, or condition.
3. Apply the same principle to other planets: natural benefic/malefic status is
   filtered by condition and testimony.

Guardrail:

Do not let "Jupiter is benefic" or "Saturn is malefic" decide the outcome by
itself. Firmicus explicitly treats condition and hostile testimony as capable of
overriding the simple label.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

Status: extracted.

## Rule Card 2.14 - House Audit Before House Judgment

Source: [Firmicus *Math.* II.14] Bram printed pp. 43-44.

Use when:

- interpreting any house topic;
- building the Evidence Ledger for a topic chain.

Required chart data:

- house sign;
- house degree if using quadrant-sensitive technique;
- term ruler of house degree if exact degree is available;
- planets in or aspecting the house;
- domicile ruler of the house sign and its condition.

Procedure:

1. Locate the house/topic.
2. Record the sign of the house.
3. If exact degree method is being used, record terms/bounds.
4. Record planets influencing the house.
5. Identify the ruler of the house sign.
6. Audit the ruler's house, sign, terms, and benefic/malefic testimony.
7. Only then state the house judgment.

Guardrail:

This is a direct anti-cookbook rule. A house topic is not judged by house name
or occupant alone.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.13]

Destination:

- `rules/reading-workflow.md`
- `rules/significator-hierarchy.md`
- `rules/house-topic-framework.md`

Status: extracted.

## Rule Card 2.15 - Angles and Quadrant Degree Handling

Source: [Firmicus *Math.* II.15] Bram printed pp. 44-47.

Use when:

- distinguishing whole-sign topics from quadrant angles;
- interpreting MC/IC/Asc/Dsc strength.

Required chart data:

- exact Ascendant degree;
- quadrant MC and IC degrees if available;
- whole-sign house positions.

Procedure:

1. Mark the four cardines: Ascendant, Descendant, Medium Caelum, Imum
   Caelum.
2. Compute Descendant as the point opposite the Ascendant.
3. Compute MC and IC by degree, not merely by counting whole signs.
4. Firmicus notes that the MC can sometimes fall in the eleventh sign from the
   Ascendant.
5. Treat angles as strength points that may not always coincide with the
   corresponding whole-sign topic house.

Guardrail:

This supports the existing project split between whole-sign topic placement and
quadrant angle degree. Do not force the MC into the 10th whole sign when the
data places it elsewhere.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.11]

Destination:

- `rules/data_contract.md`
- `rules/house-topic-framework.md`

Status: extracted.

## Rule Card 2.16 - Favorable Houses and Ascendant Aversion

Source: [Firmicus *Math.* II.16-17] Bram printed p. 47.

Use when:

- classifying houses by relationship to the Ascendant;
- checking why some houses are supportive or weak.

Required chart data:

- whole-sign house positions from Ascendant.

Procedure:

1. Mark the four angles as primary strength points.
2. Mark the following favorable houses:
   - 3rd: Dea
   - 9th: Deus
   - 5th: Bona Fortuna
   - 11th: Bonus Daemon
3. Mark the remaining four houses as weak/passive because they do not aspect
   the Ascendant:
   - 2nd: Anafora / Gate of Hell
   - 8th: Epicatafora
   - 6th: Mala Fortuna
   - 12th: Malus Daemon / Cacodaemon
4. Use aversion from Ascendant as a core house-strength concept.

Guardrail:

Firmicus treats the 2nd and 8th as passive because they do not aspect the
Ascendant even though the 2nd can still concern resources. Keep strength and
topic separate.

Brennan cross-ref:

- [cross-ref: Brennan Ch.9]
- [cross-ref: Brennan Ch.10]

Destination:

- `rules/house-topic-framework.md`
- `rules/aspect-reception-rules.md`

Status: extracted.

## Rule Card 2.17 - House Precedence Sequence

Source: [Firmicus *Math.* II.18] Bram printed pp. 47-48.

Use when:

- comparing paired houses and directional order;
- interpreting "preceding" versus "following" houses in Firmicus.

Required chart data:

- whole-sign houses from Ascendant.

Procedure:

1. Record Firmicus's precedence pairs:
   - Ascendant before Descendant;
   - MC before IC;
   - 11th before 5th;
   - 9th before 3rd;
   - 2nd before 8th;
   - 6th before 12th.
2. Use this only when a Firmicus rule depends on house sequence or
   right/left/directional framing.

Guardrail:

This is not yet an independent v1 rule. Keep it source-specific until Phase B
tests whether it changes judgments.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]

Destination:

- `rules/house-topic-framework.md`

Status: extracted; Phase B review needed.

## Rule Card 2.18 - House Topic Skeleton

Source: [Firmicus *Math.* II.19-20] Bram printed pp. 48-52.

Use when:

- comparing Firmicus house topics with the current house-topic framework;
- interpreting Book III, VI, or VII house-based examples.

Required chart data:

- whole-sign houses from Ascendant;
- quadrant angles if angle strength is relevant.

Procedure:

Use Firmicus's topic skeleton as a source comparison:

| House | Firmicus name / frame | Topics |
|---:|---|---|
| 1 | Life / Ascendant | life, vital spirit, basic character |
| 2 | Hope / Gate of Hell / Anafora | hopes, material possessions, resources; passive to Asc |
| 3 | Dea | siblings, friends, travelers; weak sextile to Asc |
| 4 | IMC | parents, family property, substance, hidden/recovered wealth |
| 5 | Bona Fortuna / house of Venus | children; powerful trine to Asc |
| 6 | Mala Fortuna / house of Mars | illness, bodily afflictions; passive to Asc |
| 7 | Descendant | spouse/marriage; opposition to Asc |
| 8 | Epicatafora | death; passive to Asc; Moon rejoices here only in nocturnal charts under good conditions |
| 9 | Deus / Sun God | social class, religion, foreign travel; trine to Asc |
| 10 | MC | life/actions, country, home, public dealings, career, mind infirmities |
| 11 | Bonus Daemon / house of Jupiter | good daemon, often near MC |
| 12 | Malus Daemon / house of Saturn | enemies, slaves, defects, illnesses; passive to Asc |

Guardrail:

Do not flatten Firmicus's house list into modern keywords. Preserve strength,
aspect to Ascendant, and planetary allotment where the source gives them.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]

Destination:

- `rules/house-topic-framework.md`

Status: extracted.

## Rule Card 2.19 - House Judgment by Testimony and Host Condition

Source: [Firmicus *Math.* II.20] Bram printed pp. 51-52.

Use when:

- judging a house topic;
- determining whether an occupant benefits or suffers from its sign host;
- preventing isolated house interpretation.

Required chart data:

- planets in/aspecting the house;
- benefic/malefic status;
- chart sect;
- domicile ruler of the sign and its condition;
- occupant's dignity/debility and house placement.

Procedure:

1. Identify which planets rule the individual houses.
2. Check whether benefics aspect the house by conjunction, trine, or sextile.
   If so, mark supportive testimony.
3. If malefics alone contact the house by conjunction, square, or opposition,
   mark danger or difficulty testimony.
4. If both benefics and malefics testify, mark mixed testimony: good is
   diminished and bad is mitigated.
5. If a planet is in another planet's sign, inspect the sign ruler's condition.
6. If the host is well placed, the guest shares in the host's prosperity.
7. If the host is dejected, the guest is hindered even if the guest is in an
   otherwise fortunate house.

Guardrail:

This is one of the strongest Firmicus anti-cookbook rules. A planet in a house
does not speak alone; its host and testimonies change what it can deliver.

Brennan cross-ref:

- [cross-ref: Brennan Ch.13]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/significator-hierarchy.md`
- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

Status: extracted.

## Rule Card 2.20 - Own-Sign Count as Coarse Chart Quality

Source: [Firmicus *Math.* II.21] Bram printed p. 53.

Use when:

- evaluating Firmicus's coarse chart-quality heuristic;
- comparing dignity abundance across sources.

Required chart data:

- planets in signs;
- whether the planets are in important houses.

Procedure:

1. Count planets in their own signs and in important houses.
2. Treat one such planet as average, two as moderately fortunate, three as
   unusually fortunate, and four as exceptional in Firmicus's schema.
3. Treat no planets in own signs as a strong deficiency testimony in Firmicus.

Guardrail:

Do not use this count as a standalone chart judgment. It ignores sect,
visibility, house ruler condition, and testimony. Phase B should decide whether
it becomes an optional dignity-density note or remains source history.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]

Destination:

- `rules/planet-condition-audit.md`

Status: extracted; low priority.

## Rule Card 2.21 - Sign-Based Aspect Families and Right/Left Direction

Source: [Firmicus *Math.* II.22-23] Bram printed pp. 53-56.

Use when:

- classifying sign-based relationships;
- identifying right/left configurations in Firmicus;
- explaining why some houses are unable to testify to the Ascendant.

Required chart data:

- sign positions from the reference sign or point.

Procedure:

1. Opposition is the seventh sign from the starting sign and is threatening.
2. Trine is the fifth sign from the starting sign and is prosperous.
3. Square is the fourth sign from the starting sign and is threatening.
4. Sextile is the third sign from the starting sign and is similar to trine but
   weaker.
5. For right/left framing, what is "behind" the starting sign is right; what is
   ahead is left.
6. Signs whose relationships do not divide the 360-degree circle by 2, 3, 4, or
   6 are not configured to the Ascendant and are called passive / unable to see.
7. Firmicus adds that sextiles separated through tropical or bicorporeal signs
   are stronger than those separated through solid signs.

Guardrail:

Do not let degree proximity change aspect family. This supports the project's
sign-based relationship baseline, though Firmicus also explains the geometry by
degree divisions.

Brennan cross-ref:

- [cross-ref: Brennan Ch.9]

Destination:

- `rules/aspect-reception-rules.md`
- `rules/house-topic-framework.md`

Status: extracted.

## Rule Card 2.22 - Body Parts by Sign for Health Topics

Source: [Firmicus *Math.* II.24] Bram printed p. 56.

Use when:

- a source-specific health or bodily-affliction rule requires sign-body mapping.

Required chart data:

- relevant sign placements;
- health-topic trigger.

Procedure:

Use this mapping only inside a triggered medical/body topic:

| Sign | Body part |
|---|---|
| Aries | head |
| Taurus | neck |
| Gemini | shoulders |
| Cancer | heart |
| Leo | breast and stomach |
| Virgo | belly |
| Libra | kidneys and vertebrae |
| Scorpio | sex organs |
| Sagittarius | thighs |
| Capricorn | knees |
| Aquarius | legs |
| Pisces | feet |

Guardrail:

Do not use this to make medical claims in client-facing output. If retained at
all, it belongs to source history or carefully caveated traditional-body-topic
analysis.

Brennan cross-ref:

- [new to Firmicus]

Destination:

- deferred / medical-topic notes.

Status: extracted; sensitive.

## Rule Card 2.23 - Length-of-Life Method Is Historical and Deferred

Source: [Firmicus *Math.* II.25] Bram printed pp. 56-57.

Use when:

- cataloging Firmicus's timing/life-span doctrine;
- deciding what not to operationalize in v1.

Required chart data:

- Life-Giver / ruler of chart;
- its house, sign, degree, dignity, and ruler;
- aspects from Sun, Moon, Jupiter, Venus, and other planets.

Procedure:

1. Firmicus instructs the reader to inspect the Giver of Life / ruler of the
   nativity.
2. Inspect its house, sign, degree, and the ruler of that sign.
3. Inspect benefic testimony to the Life-Giver, especially Jupiter by day and
   Venus by night.
4. Firmicus provides planet-specific year/month/day/hour allotments depending
   on whether the Life-Giver is favorable or unfavorable.

Guardrail:

Do not implement this as a modern prediction rule. Treat as historical method
only unless the user explicitly requests source-historical analysis and safety
language is maintained.

Brennan cross-ref:

- [cross-ref: Brennan Ch.15]
- [new to Firmicus]

Destination:

- `rules/timing-techniques.md`
- deferred / sensitive methods.

Status: extracted; deferred.

## Rule Card 2.24 - Chronocrator Starts from Sect Light

Source: [Firmicus *Math.* II.26-28] Bram printed pp. 57-58.

Use when:

- cataloging Firmicus time-lord procedures;
- comparing against annual profections or other timing systems.

Required chart data:

- chart sect;
- Sun and Moon signs;
- planet order by sign from the sect light;
- period allotments.

Procedure:

1. In diurnal charts, begin with the Sun as ruler of time.
2. In nocturnal charts, begin with the Moon as ruler of time.
3. After the sect light, distribute time to planets in sign order from that
   luminary.
4. When a planet holds a ten-year/nine-month period, subdivide the period
   among planets in chart order.
5. Firmicus also gives month allotments and day allotments for planetary
   subdivisions:
   - Months: Sun 19, Moon 25, Saturn 30, Jupiter 12, Mars 15, Venus 8,
     Mercury 20.
   - Days: Sun 53, Moon 71, Saturn 85, Jupiter 30, Mars 42, Venus 23,
     Mercury 57.
6. Judge the period by the planet's sign, house, and condition.

Guardrail:

This is not the same as the current annual profection workflow. Keep it as a
Firmicus time-lord method pending Phase B and case validation.

Brennan cross-ref:

- [cross-ref: Brennan Ch.15]
- [cross-ref: Brennan Ch.17]

Destination:

- `rules/timing-techniques.md`

Status: extracted; deferred.

## Rule Card 2.25 - Antiscia as Hidden Testimony

Source: [Firmicus *Math.* II.29] Bram printed pp. 58-68.

Use when:

- normal aspect testimony does not explain a chart factor;
- a Firmicus method explicitly asks for antiscia;
- checking hidden relationships between planets, angles, or houses.

Required chart data:

- exact sign and degree of planets/points;
- normal aspect map;
- antiscia sign-pair map.

Procedure:

1. Compute antiscia by sign pair:
   - Gemini <-> Cancer
   - Leo <-> Taurus
   - Virgo <-> Aries
   - Pisces <-> Libra
   - Aquarius <-> Scorpio
   - Sagittarius <-> Capricorn
2. Mirror degrees across the pair: degree 1 maps to 29, 2 to 28, and so on;
   degree 15 maps to 15.
3. Firmicus states that the 30th degree does not send antiscia.
4. If two planets are not normally configured, check whether antiscia create a
   trine, square, sextile, or opposition relationship.
5. If antiscia connect the factors, treat the resulting testimony as if the
   planets were so related in ordinary configuration, while marking it as hidden
   testimony.
6. Use examples such as the chart of Albinus as demonstrations of method, not
   as reusable event recipes.

Guardrail:

Antiscia should not replace the normal aspect map. Run the ordinary
relationship map first, then add antiscia as a secondary hidden-testimony layer.

Brennan cross-ref:

- [cross-ref: Brennan Ch.9]
- [new to Firmicus]

Destination:

- `rules/aspect-reception-rules.md`
- `rules/data_contract.md`

Status: extracted; Phase B weighting needed.

## Rule Card 2.26 - Astrologer Ethics and Output Restraint

Source: [Firmicus *Math.* II.30] Bram printed pp. 68-70.

Use when:

- drafting output discipline rules;
- handling sensitive topics;
- defining what the skill should refuse, soften, or bracket.

Required chart data:

- Not chart-specific.

Procedure:

1. Keep responses public, clear, and accountable rather than secretive or
   manipulative.
2. Avoid forbidden or politically dangerous inquiries in Firmicus's context,
   especially the emperor's fate; translate this into modern high-stakes caution.
3. Do not expose a client's vices too bluntly. When a difficult topic appears,
   answer with restraint rather than sensationalism.
4. Avoid greed, coercion, false witness, and using the art to intensify conflict.
5. Treat the practitioner as responsible for the effect of the response, not just
   for technical correctness.

Guardrail:

Do not import Firmicus's imperial theology literally. Extract the usable process
rule: sensitive topics require restraint, transparency, and refusal when the
question itself is unsafe.

Brennan cross-ref:

- [cross-ref: Brennan Ch.6]
- [new to Firmicus]

Destination:

- `rules/delineation-output-rules.md`
- `skill-draft/SKILL.md`

Status: extracted.

## Book II Extraction Notes

- Total rule cards: 26.
- `needs verification` / Phase B comparison points:
  - decan table OCR around Leo's third decan;
  - Mercury sect assignment as nocturnal in Firmicus versus current conditional
    Mercury handling;
  - exact status of Firmicus's stronger decan weighting;
  - integration weight for antiscia;
  - whether duodecatemoria and regional rising-time tables remain deferred.
- Sensitive/deferred material:
  - length-of-life allotments;
  - health/body mapping;
  - some timing outcomes by month/day;
  - ethics around forbidden questions translated only as modern output
    restraint.
