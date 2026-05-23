# Firmicus Extraction - Book III Houses and Planets in Houses

Source: Julius Firmicus Maternus, *Mathesis*, Book III, translated by Jean
Rhys Bram, *Ancient Astrology Theory and Practice*.

Scope:

- Thema Mundi as teaching model;
- planet-in-house catalogs;
- sect, angularity, dignity, benefic/malefic testimony, Moon motion, and sign
  quality as modifiers;
- Mercury combination chapters;
- Moon in the Part of Fortune and third-day Moon check.

Copyright note: this file paraphrases method and stores page references. It
does not reproduce long source passages.

## Chapter Range

- Bram printed pp. 71-116.
- PDF pp. 75-120.

## Method Takeaway

Book III looks at first like a placement catalog, but its usable method is
conditional. Firmicus repeatedly changes the outcome of a planet-in-house
statement by sect, house strength, dignity, benefic/malefic aspect, Moon phase,
angular support, sign quality, and duodecatemorion. For this project, Book III
should be mined as condition logic, not as a cookbook.

```text
Planet in house -> check sect -> check dignity/host -> check angularity ->
check benefic/malefic testimony -> check Moon motion -> check sign quality ->
check duodecatemorion -> then synthesize.
```

## Rule Card 3.1 - Turn Catalog Prose into Propositions

Source: [Firmicus *Math.* III.Proem.] Bram printed p. 71.

Use when:

- extracting Firmicus placement lists;
- deciding whether a paragraph should become a reusable rule card.

Required chart data:

- Not chart-specific; this is an extraction/workflow rule.

Procedure:

1. Treat Firmicus's stated aim of translating the tradition into propositions as
   permission to distill method from rhetoric.
2. Reduce each placement paragraph to its required conditions.
3. Preserve source citation and uncertainty.
4. Do not preserve vivid event lists as final output language.

Guardrail:

If a paragraph cannot be reduced to condition logic, mark it
`[cookbook: Firmicus *Math.* III.<chapter>, condition-logic TBD]` rather than
turning it into a direct delineation.

Brennan cross-ref:

- [project heuristic]

Destination:

- `rules/delineation-output-rules.md`

Status: extracted.

## Rule Card 3.2 - Thema Mundi as Didactic Schema, Not Historical Chart

Source: [Firmicus *Math.* III.1] Bram printed pp. 71-75.

Use when:

- interpreting Firmicus's Thema Mundi references;
- comparing the Thema Mundi to chart-reading rules.

Required chart data:

- none; this is a model chart.

Procedure:

1. Record the Thema Mundi placements as a teaching schema:
   - Ascendant and Moon: Cancer 15
   - Sun: Leo 15
   - Mercury: Virgo 15
   - Venus: Libra 15
   - Mars: Scorpio 15
   - Jupiter: Sagittarius 15
   - Saturn: Capricorn 15
2. Use the schema to explain planetary relationships to the luminaries and the
   ordering of signs/houses.
3. Do not treat it as an actual historical birth chart of the cosmos. Firmicus
   explicitly says it was invented by wise predecessors as an example.

Guardrail:

The Thema Mundi is a rationale and teaching diagram, not evidence for a natal
judgment by itself.

Brennan cross-ref:

- [cross-ref: Brennan Ch.8]
- [cross-ref: Brennan Ch.10]

Destination:

- `rules/source-map.md`
- source-history notes.

Status: extracted.

## Rule Card 3.3 - Mercury Common by Solar/Lunar Phase

Source: [Firmicus *Math.* III.1] Bram printed p. 72.

Use when:

- comparing Firmicus's Mercury doctrine against Book II and v1;
- auditing Mercury's sect or condition.

Required chart data:

- Mercury's morning/evening rising condition;
- chart sect;
- Mercury relation to Sun/Moon.

Procedure:

1. Firmicus reports the Thema Mundi argument that Mercury is common because it
   is not configured to either luminary in that schema.
2. Mercury rejoices with the Sun by day when morning-rising.
3. Mercury rejoices with the Moon by night when evening-rising.
4. Use this to qualify Book II's simpler statement that Mercury follows the
   nocturnal condition.

Guardrail:

This supports keeping Mercury conditional in the project. Do not flatten
Mercury to purely nocturnal on Book II alone.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]

Destination:

- `rules/planet-condition-audit.md`

Status: extracted; Phase B comparison point.

## Rule Card 3.4 - Planet-In-House Audit Stack

Source: [Firmicus *Math.* III.2-14] Bram printed pp. 75-116.

Use when:

- extracting or applying any Book III planet-in-house material;
- preventing placement-only readings.

Required chart data:

- planet sign, house, exact degree;
- chart sect;
- dignity: domicile, exaltation, terms, decan if exact degree is known;
- aspects from benefics and malefics;
- Moon phase and application/separation when the Moon is involved;
- duodecatemorion and its terms if using Firmicus's full procedure.

Procedure:

1. Start with the planet's house placement.
2. Check whether the house is angular, favorable/configured, or passive/averse.
3. Check whether the planet is acting in its preferred sect.
4. Check whether it is in its own sign, terms, exaltation, or a benefic's house.
5. Check malefic contacts for worsening and benefic contacts for mitigation.
6. If the Moon is involved, check waxing/waning/full and whether she moves
   toward or away from the planet.
7. Check sign quality for the concrete form of the topic.
8. Check the planet's duodecatemorion and its terms for hidden or final power.

Guardrail:

No Book III placement sentence should be used without the audit stack. This is
the central anti-cookbook extraction rule for the book.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.8]
- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.13]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/reading-workflow.md`
- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

Status: extracted.

## Rule Card 3.5 - Saturn: Sect and Benefic Mitigation Decide Severity

Source: [Firmicus *Math.* III.2] Bram printed pp. 75-78.

Use when:

- extracting Saturn-in-house statements;
- judging Saturn's condition in a Firmicus frame.

Required chart data:

- Saturn house and degree;
- chart sect;
- Saturn dignity and terms;
- Moon phase/aspect to Saturn;
- Mars contact;
- benefic contact, especially Jupiter or Venus;
- Saturn duodecatemorion.

Procedure:

1. Saturn by day on angles can produce responsibility, primacy, or delayed
   status, especially when supported.
2. Saturn by night, especially on angles or in bad houses, becomes much more
   difficult.
3. Mars contact, difficult Moon contact, or absence of benefic testimony
   intensifies Saturn's harm.
4. Benefic testimony can return, mitigate, or translate what Saturn denies.
5. Always inspect Saturn's duodecatemorion and its terms before final judgment.

Guardrail:

Do not read Saturn as uniformly harmful. In Firmicus, sect and support sharply
change Saturn's expression.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`

Status: extracted.

## Rule Card 3.6 - Jupiter: Benefic Nature Is Limited by Sect, House, and Attack

Source: [Firmicus *Math.* III.3] Bram printed pp. 78-82.

Use when:

- extracting Jupiter house placements;
- preventing automatic benefic override.

Required chart data:

- Jupiter house and degree;
- chart sect;
- Jupiter dignity;
- malefic aspects;
- Moon phase and aspect;
- Mercury/Venus contacts where relevant;
- Jupiter duodecatemorion.

Procedure:

1. Jupiter on angles or in favorable houses, especially by day and dignified,
   supports rank, prosperity, public responsibility, and protection.
2. Malefic aspects diminish Jupiter's promise.
3. Nocturnal placement can reduce or reverse Jupiter's ease in Firmicus,
   especially when malefics or the waning Moon are involved.
4. A difficult house can overpower Jupiter's natural beneficence; Firmicus
   explicitly treats the 6th as giving any occupant force for difficult outcomes.
5. Favorable Mercury or waxing Moon testimony can redirect Jupiter toward
   administration, learning, accounting, or public office.
6. Inspect Jupiter's duodecatemorion.

Guardrail:

Do not use Jupiter as an unconditional rescue. Firmicus repeatedly shows Jupiter
as conditioned by house, sect, and testimony.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/house-topic-framework.md`

Status: extracted.

## Rule Card 3.7 - Mars: Nocturnal Support and Benefic Testimony Mitigate Heat

Source: [Firmicus *Math.* III.4] Bram printed pp. 82-88.

Use when:

- extracting Mars house placements;
- judging Mars as active, military, dangerous, or mitigated.

Required chart data:

- Mars house, sign, degree;
- chart sect;
- Mars dignity, terms, or exaltation;
- Jupiter/Venus testimony;
- Moon phase/aspect;
- whether Mars holds an angle;
- Mars duodecatemorion.

Procedure:

1. Mars in nocturnal charts can become productive, especially in masculine
   signs, dignities, or with Jupiter.
2. Mars by day on angles is especially dangerous in Firmicus.
3. Jupiter and Venus mitigate Mars's attacks; Firmicus says their aspect should
   be hoped for.
4. Waxing Moon contact to angular Mars intensifies danger; waning Moon and
   Venus can fit Mars's nocturnal condition better.
5. Sign quality determines the concrete form of Mars outcomes, but the sign
   image should remain a modifier, not the main rule.
6. Inspect Mars's duodecatemorion and its terms.

Guardrail:

Do not turn Mars-in-house paragraphs into literal event predictions. Extract the
sect/angle/dignity/testimony pattern.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/aspect-reception-rules.md`

Status: extracted.

## Rule Card 3.8 - Sun: Angular Light, Public Authority, and Malefic Reversal

Source: [Firmicus *Math.* III.5] Bram printed pp. 88-94.

Use when:

- judging the Sun as authority, father, visibility, or public office;
- extracting solar angularity examples.

Required chart data:

- Sun house, dignity, and sect;
- angle placement;
- Jupiter/Venus/Mercury testimony;
- Mars/Saturn testimony;
- Moon position and phase;
- Part of Fortune when invoked;
- Sun duodecatemorion.

Procedure:

1. The Sun on the Ascendant or MC by day, dignified or supported, indicates
   public visibility, authority, and inheritance of status.
2. Jupiter, Venus, and Mercury can strengthen solar authority toward learning,
   office, and public reputation.
3. Mars or Saturn on angles, in the 2nd/8th, or in harsh contact can reverse the
   solar promise into loss, exile, captivity, illness, or removal from office in
   Firmicus's historical vocabulary.
4. Benefic testimony can cure or mitigate the afflictions connected to the Sun,
   Moon, Mars, and Saturn.
5. Inspect the Sun's duodecatemorion and terms.

Guardrail:

Use the pattern "authority plus possible reversal under malefic attack," not the
literal royal or violent examples, unless doing source-historical commentary.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/significator-hierarchy.md`

Status: extracted.

## Rule Card 3.9 - Venus: Nocturnal Strength, Solar Conflict, and Relationship Scandal

Source: [Firmicus *Math.* III.6] Bram printed pp. 94-99.

Use when:

- judging Venus condition in a Firmicus frame;
- extracting relationship, pleasure, art, or patronage topics.

Required chart data:

- Venus house, sign, and degree;
- chart sect;
- morning/evening status relative to the Sun;
- Mars/Saturn contacts;
- Jupiter/Mercury contacts;
- Moon phase/aspect;
- Venus duodecatemorion.

Procedure:

1. Venus is strongest in Firmicus when nocturnal, favorably placed, and in
   supportive contact with the Moon, Mars, Mercury, or Jupiter.
2. Venus by day, especially with difficult Mars/Saturn contact, often becomes
   scandal, disorder, or frustrated relationship testimony in Firmicus.
3. Venus with the Sun is treated as especially difficult; Venus behind the Sun in
   morning rising can increase good fortune.
4. Jupiter can cleanly mitigate Venus-Saturn or Venus-Moon difficulties.
5. Sign quality modifies the concrete expression of Venus topics.
6. Inspect Venus's duodecatemorion and terms.

Guardrail:

Firmicus's sexual categories are historically loaded and often stigmatizing. For
project use, retain only the condition logic and mark sensitive material as
source-historical, not direct client-facing language.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/delineation-output-rules.md`

Status: extracted; sensitive language excluded.

## Rule Card 3.10 - Mercury: Protean Planet Changes With Company and Phase

Source: [Firmicus *Math.* III.7-12] Bram printed pp. 99-113.

Use when:

- judging Mercury condition;
- extracting Mercury combinations with the Sun, Saturn, Jupiter, Mars, or Venus.

Required chart data:

- Mercury house, sign, degree;
- morning/evening status;
- chart sect;
- Mercury's co-present or aspecting planets;
- dignity/terms;
- Moon contact;
- Mercury duodecatemorion.

Procedure:

1. Mercury takes on the quality of its company: favorable with helpful planets
   and difficult with harmful ones.
2. Firmicus explicitly says Mercury with Jupiter and the Sun in favorable
   houses can produce high fortune, while Mercury with Mars by day is highly
   difficult.
3. By night, Mercury can work more favorably with Venus, the Moon, and Mars.
4. Mercury's morning/evening status changes house outcomes, especially in the
   2nd, 4th, 5th, 6th, 8th, 10th, and 12th houses.
5. Benefic aspects redirect Mercury toward learning, administration, medicine,
   sacred skills, records, or public service.
6. Malefic aspects redirect Mercury toward accusation, forgery, imprisonment,
   deception, or bodily affliction in Firmicus's historical idiom.
7. Inspect Mercury's duodecatemorion and terms.

Guardrail:

This supports the project's existing conditional Mercury approach. Do not treat
Mercury as simply benefic, malefic, diurnal, or nocturnal.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/aspect-reception-rules.md`

Status: extracted.

## Rule Card 3.11 - Mercury-Mars Occupation Logic by Host/Terms

Source: [Firmicus *Math.* III.11] Bram printed pp. 108-110.

Use when:

- extracting occupation logic from planet combinations;
- preventing literal occupation cookbook output.

Required chart data:

- Mercury and Mars relationship;
- sign or term ruler of the combination;
- house placement and sect;
- benefic testimony.

Procedure:

1. Treat Mercury-Mars as an activity/skill combination with volatile outcomes.
2. The sign or term ruler redirects the field of activity:
   - Mercury: athletics/gymnasium or skill activity;
   - Mars: arms, fighting, soldiers, hunting, couriers;
   - Venus: textiles, dyes, perfumes, jewelry;
   - Jupiter: offices, regions, states, public authority;
   - Saturn: coercive, destructive, or low-status labor;
   - Sun/Moon: metal, fire, leather, sculpture, hard materials.
3. Use the ruler/terms as a domain selector, not as a literal job title list.

Guardrail:

This is a reusable anti-cookbook pattern: occupation emerges from planet pair
plus host/terms plus house/sect, not from the planet pair alone.

Brennan cross-ref:

- [cross-ref: Brennan Ch.13]
- [new to Firmicus]

Destination:

- `rules/significator-hierarchy.md`
- `rules/house-topic-framework.md`

Status: extracted.

## Rule Card 3.12 - Sixth and Twelfth Need MC/Angle Support

Source: [Firmicus *Math.* III.7-12] Bram printed pp. 99-113.

Use when:

- interpreting planets or combinations in the 6th or 12th;
- evaluating whether difficult houses can still produce visible action.

Required chart data:

- planet/combo in 6th or 12th;
- whether another planet occupies the 10th / MC;
- benefic/malefic testimony.

Procedure:

1. Treat the 6th and 12th as sluggish or difficult houses.
2. If another planet occupies the 10th/MC, the difficult-house combination may
   become active through public work, skill, or service.
3. Without MC support, Firmicus often lowers the outcome into servile,
   hidden, or obstructed activity.
4. Benefic testimony can improve the expression; malefic testimony worsens it.

Guardrail:

Do not treat a difficult house as "nothing happens." Firmicus repeatedly routes
6th/12th material through MC support or lack of support.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.13]

Destination:

- `rules/house-topic-framework.md`
- `rules/significator-hierarchy.md`

Status: extracted.

## Rule Card 3.13 - Ninth House Sacred / Divinatory Aptitude, With Scope Limit

Source: [Firmicus *Math.* III.2-14] Bram printed pp. 77, 81, 86, 93, 96, 102, 108,
112, 114-116.

Use when:

- extracting religion, divination, temple, dream, astrology, magic, or exorcism
  material from Firmicus;
- deciding whether material is in scope.

Required chart data:

- 9th house sign and ruler;
- planets in the 9th;
- dignity, sect, and benefic/malefic testimony;
- Moon/Fortune contacts when relevant.

Procedure:

1. Treat 9th-house planet placements as a repeated Firmicus trigger for sacred,
   temple, divinatory, prophetic, philosophical, astrological, dream, or ritual
   roles.
2. Benefic condition and dignity tend to frame these roles as honorable,
   learned, or socially recognized.
3. Malefic affliction tends to frame them as dangerous, false, impious, or
   socially punished in Firmicus's idiom.
4. For this project, extract only aptitude, role, condition, or social function.

Guardrail:

Do not extract magical procedure, ritual recipe, spirit-command technique, or
operational occult instruction. If such material appears, mark
`[out-of-scope: magical applications, deferred to occult-applications project v3+]`.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]
- [new to Firmicus]

Destination:

- `rules/house-topic-framework.md`
- `rules/delineation-output-rules.md`

Status: extracted; scope-limited.

## Rule Card 3.14 - Eminence Requires Angle, Dignity, Luminary, and Benefic Stack

Source: [Firmicus *Math.* III.3-5, III.13-14] Bram printed pp. 79-82, 88-94,
114-116.

Use when:

- evaluating public rank / eminence claims in Firmicus;
- avoiding single-factor "king" judgments.

Required chart data:

- luminary placements and phase;
- MC/Asc/angle placements;
- Jupiter and Venus testimony;
- planet dignity;
- malefic angular placements;
- Part of Fortune when invoked.

Procedure:

1. Do not infer eminence from one angular planet.
2. Firmicus's strongest eminence examples stack multiple factors:
   - Sun, Moon, or Jupiter in an angle or strong house;
   - dignity or preferred sect;
   - benefic testimony;
   - Moon in strong phase or applying to a benefic;
   - MC/Asc support;
   - sometimes Part of Fortune on an angle.
3. Malefics on angles or in the 2nd/8th can reverse public rise into loss,
   danger, or removal.

Guardrail:

Translate "king/emperor/general" into source-historical eminence. In modern
outputs, report only public authority, visibility, command, or institutional
power when the evidence stack is present.

Brennan cross-ref:

- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/significator-hierarchy.md`
- `rules/delineation-output-rules.md`

Status: extracted.

## Rule Card 3.15 - Moon: Phase, Sect, Angularity, and Application Are Primary

Source: [Firmicus *Math.* III.13] Bram printed pp. 113-115.

Use when:

- judging Moon placements in Firmicus;
- preparing for Book IV lunar application rules.

Required chart data:

- Moon phase;
- chart sect;
- Moon house and dignity;
- Moon application/separation;
- aspects from Mars, Saturn, Jupiter, Venus, Mercury;
- planets on the Ascendant or MC.

Procedure:

1. A full Moon on the Ascendant in a nocturnal chart and in signs where she
   rejoices is a strong fortune testimony.
2. Mars/Saturn on angles or in harsh contact can overwhelm that testimony if no
   benefic aspects intervene.
3. Moon by day often changes or weakens outcomes compared with Moon by
   night.
4. Moon on the MC in a nocturnal chart, waxing and supported by Jupiter, is a
   strong public-power testimony.
5. Moon in the 12th is strongly weakened unless Jupiter or Venus on the
   Ascendant gives support.
6. Inspect the Moon's duodecatemorion and terms.

Guardrail:

Book III has a lacuna for Moon in houses five through eight. Do not reconstruct
those missing house meanings from other sources in this extraction.

Brennan cross-ref:

- [cross-ref: Brennan Ch.7]
- [cross-ref: Brennan Ch.10]
- [cross-ref: Brennan Ch.14]

Destination:

- `rules/planet-condition-audit.md`
- `rules/aspect-reception-rules.md`

Status: extracted; lacuna noted.

## Rule Card 3.16 - Moon in the Part of Fortune

Source: [Firmicus *Math.* III.14] Bram printed pp. 115-116.

Use when:

- the Moon is in the Part of Fortune;
- reading Fortune as a condition amplifier.

Required chart data:

- Part of Fortune sign/degree/house;
- Moon sign/degree/phase;
- Moon application or co-presence with Jupiter, Venus, Mercury, Mars, Saturn,
  or the Sun;
- chart sect;
- Fortune's house, especially MC/10th or 11th.

Procedure:

1. If the Moon is in Fortune and moving toward or with Jupiter, mark leadership,
   public standing, and good-fortune testimony.
2. If the Moon is in Fortune and moving toward or with Venus, mark charm,
   grace, and relational/favor testimony.
3. If waxing Moon in Fortune moves toward or joins Mercury, mark intelligence,
   honors, and possessions; if waning, mark affliction/difficulty testimony.
4. If Moon in Fortune moves toward or joins Mars, judge by sect: by day more
   difficult; by night more martial/competitive/commanding.
5. If waxing Moon in Fortune moves toward or joins Saturn, mark early burden
   with later improvement; if waning by day, mark strong difficulty.
6. If Fortune is at the MC/10th or 11th and other luminary/angle supports are
   present, the testimony can become public eminence.

Guardrail:

This is not a standalone Lot rule. It depends on Moon phase, application,
co-presence, sect, and Fortune's house.

Brennan cross-ref:

- [cross-ref: Brennan Ch.16]
- [new to Firmicus]

Destination:

- `rules/lots-and-fortune.md`
- `rules/planet-condition-audit.md`

Status: extracted.

## Rule Card 3.17 - Third-Day Moon Check

Source: [Firmicus *Math.* III.14] Bram printed p. 116.

Use when:

- cataloging Firmicus's neonatal/lunar follow-up doctrine;
- deciding data requirements for advanced Firmicus practice.

Required chart data:

- natal Moon condition;
- Moon's condition on the third day after birth;
- Moon phase and aspects to benefics/malefics on that third day.

Procedure:

1. Record the natal Moon's first-day course.
2. Also inspect the Moon on the third day after birth.
3. Note which planet the Moon attaches to, from whom she separates, and by what
   aspect.
4. Note whether the Moon is waxing/waning/full and benefic/malefic testimony
   on that third day.

Guardrail:

This requires postnatal ephemeris computation and is not supported in v1. Mark
as deferred unless the user supplies computed third-day Moon data.

Brennan cross-ref:

- [new to Firmicus]

Destination:

- `rules/data_contract.md`
- `rules/timing-techniques.md`

Status: extracted; deferred.

## Rule Card 3.18 - Duodecatemorion as Planet-Specific Final Check

Source: [Firmicus *Math.* III.2-7, III.13] Bram printed pp. 78, 82, 88, 94, 99,
103, 115.

Use when:

- a Book III planet chapter ends by requiring the duodecatemorion;
- exact degree data is available.

Required chart data:

- planet exact degree and minutes;
- computed duodecatemorion;
- terms of the duodecatemorion.

Procedure:

1. After judging the ordinary house/sign/aspect condition of a planet, compute
   its duodecatemorion.
2. Inspect the house and terms of that derived point.
3. Treat the derived point as revealing hidden or final power of the planet in
   Firmicus's method.

Guardrail:

Do not compute this from rounded placements. This is an advanced Firmicus
overlay and should remain optional/deferred until Phase B.

Brennan cross-ref:

- [new to Firmicus]

Destination:

- `rules/data_contract.md`
- deferred technique notes.

Status: extracted; deferred.

## Book III Extraction Notes

- Total rule cards: 18.
- Placement catalog handling:
  - Saturn, Jupiter, Mars, Sun, Venus, Mercury, and Moon chapters were distilled
    into condition patterns.
  - Mercury combination chapters were distilled into "Mercury changes with
    company" and occupation-routing rules.
  - No placement-by-placement event paragraph was promoted directly into a
    reusable rule.
- `needs verification` / Phase B comparison points:
  - Mercury common / morning-evening doctrine versus Book II and v1;
  - exact weight of duodecatemoria;
  - third-day Moon data requirement;
  - Book III Moon lacuna for houses five through eight.
- Scope-limited material:
  - 9th-house magic/exorcism/divination passages retained only as role/aptitude
    material, not operative magical instruction.
  - Sensitive sexual, medical, enslavement, death, and punishment language was
    not preserved as client-facing delineation.
