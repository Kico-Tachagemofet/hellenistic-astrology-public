# Firmicus Method Targets

This file tracks which parts of Firmicus should feed later v2.1 Phase B rule
updates. Phase A only extracts source material inside this folder; it does not
edit `rules/`, Brennan extractions, sibling skills, or cases.

## Core Rule Modules

### `rules/dignities-reference.md`

Primary Firmicus targets:

- Book II.1-6: signs, domicile rulers, exaltations/falls, decans, terms.
- Book VIII.4 and VIII.18-30: degree doctrines, mostly as historical or
  deferred material unless a condition-based method can be extracted.

Questions to extract:

- Does Firmicus agree with the existing domicile/exaltation/fall table?
- Does Firmicus give decan or term logic that changes audit weighting?
- Which degree doctrines require exact degree data and should remain optional or
  deferred?

Book II notes:

- Domiciles and exaltation/fall degrees align with the current table at the
  planet/sign level.
- Firmicus speaks more strongly about exact exaltation/fall degrees and decans
  than v1 currently does; Phase B should decide whether this changes weighting.
- Terms/bounds in Book II.6 appear to match the current Egyptian bounds table.
- The OCR read for Leo's third decan conflicts with the standard Chaldean-order
  table; verify against page image before using Firmicus as a decan table source.

### `rules/planet-condition-audit.md`

Primary Firmicus targets:

- Book II.7-9: day/night condition, matutine/vespertine status, solar distance.
- Book III: planets in houses and major combinations.
- Book IV.1-16: Moon condition, lunar phase, application, separation, void of
  course.
- Book VI.2: bright stars, if usable.

Questions to extract:

- What conditions increase or decrease a planet's capacity?
- How does Firmicus handle solar phase and visibility?
- How should the Moon's application/separation condition enter the audit?
- Which bright-star or degree claims should remain `[needs verification]` or
  `[new to Firmicus]`?

Book II notes:

- Firmicus assigns Mercury to the nocturnal condition in Book II.7. This is a
  direct Phase B comparison point against v1's visibility-based Mercury handling.
- Firmicus gives planet-specific matutine/vespertine thresholds: Saturn 15
  degrees, Jupiter 12, Mars 8, Venus 8, Mercury 18.
- Nearness to the Sun is generally harmful, with a noted caveat that some
  astrologers treat Mars under solar domination as less malefic.

Book III notes:

- Mercury is described as common in the Thema Mundi argument: morning-rising
  with the Sun by day, evening-rising with the Moon by night.
- Planet chapters repeatedly require a final duodecatemorion check; this remains
  deferred until exact-degree support is added.
- Mars, Saturn, Venus, Jupiter, Sun, Mercury, and Moon were extracted as
  condition patterns rather than house-by-house cookbooks.

### `rules/house-topic-framework.md`

Primary Firmicus targets:

- Book II.14-20: houses, angles, unaspected houses, house names and topics.
- Book III: planets in houses.
- Book VI.32: meanings of houses.
- Book VII: specific life topics by house or condition.

Questions to extract:

- Where does Firmicus agree with Brennan's place meanings?
- Does he add useful topic routing or house strength distinctions?
- Which historical status topics should be kept as source history rather than
  direct modern delineation?

Book II notes:

- Firmicus supports the current split between whole-sign topic houses and
  quadrant angle degrees: MC can fall in the eleventh sign from Ascendant.
- Book II.19 gives a compact house-topic skeleton and repeats aversion from the
  Ascendant as a strength distinction.

Book III notes:

- 6th and 12th house material can still become active when another planet
  occupies the 10th/MC; without MC support, Firmicus often describes hidden,
  servile, or obstructed expression.
- 9th house placements repeatedly trigger sacred, temple, divinatory,
  philosophical, astrological, dream, or magical-role material. Phase B should
  preserve role/aptitude only and exclude operational magical applications.

### `rules/aspect-reception-rules.md`

Primary Firmicus targets:

- Book II.22-23: trine, square, sextile, opposition, unaspected signs.
- Book II.29: antiscia.
- Book IV.2-16 and IV.25: Moon applications, separations, conjunctions, and
  defluctions.
- Book VI.3-31: trine, square, opposition, sextile, conjunction, and complex
  aspect examples.
- Book VIII.3: signs which see and hear each other.

Questions to extract:

- Does Firmicus support or complicate the existing sign-based witnessing model?
- How does he weight superior/inferior or threatening contacts?
- Are antiscia and sign hearing/seeing usable as secondary testimony?
- Which examples are just placement cookbooks and should be deferred?

Book II notes:

- Book II.22-23 supports sign-based aspect families and Ascendant aversion.
- Book II.29 adds antiscia as hidden testimony after ordinary aspects are
  checked; Phase B needs to decide weighting and output syntax.

Book III notes:

- Moon motion toward/away from planets is a major modifier and should be
  integrated with Book IV before any rule update.
- Benefic aspects repeatedly mitigate Mars/Saturn harms; malefic aspects
  repeatedly reverse or diminish benefic/solar/Jupiter promises.

### `rules/lots-and-fortune.md`

Primary Firmicus targets:

- Book III.14: Moon in the Part of Fortune.
- Book IV.17: Part of Fortune formula and effects.
- Book IV.18: Part of the Daemon / Spirit.
- Book VII.2 and related sections: Fortune used in life-condition rules.

Questions to extract:

- Does Firmicus use the same day/night formulas for Fortune and Spirit?
- How does he treat Fortune as a place to inspect rather than a standalone
  cookbook point?
- What is reusable for v1's Lot audit, and what remains source-specific?

Book II notes:

- Book II does not yet develop Lots, but it prepares the house/audit logic that
  Book IV uses for Fortune and Daemon.

Book III notes:

- Moon in Fortune is condition-sensitive: outcome changes by Moon phase, the
  planet she moves toward or joins, chart sect, and Fortune's house.

### `rules/significator-hierarchy.md`

Primary Firmicus targets:

- Book II.19-20: house topic significators and planetary allotments.
- Book IV.19: ruler of the chart.
- Book VII: topic-specific significator choices.
- Book VIII.32: need for all data before judgment.

Questions to extract:

- Which planet or point gets priority for a topic?
- When does Firmicus require the house ruler, chart ruler, Lot ruler, Moon, or
  angular planets to be inspected first?
- Does he provide process guardrails against single-placement judgment?

Book II notes:

- Book II.14 and II.20 are strong process guards: judge a house by sign, terms,
  occupant/influence, ruler location, ruler condition, and benefic/malefic
  testimony.
- Book II.20's host analogy is a direct support for ruler-chain discipline.

Book III notes:

- Eminence requires stacked evidence in Firmicus: angular luminary/Jupiter,
  dignity/preferred sect, benefic testimony, Moon support, MC/Asc support, and
  sometimes Fortune. Malefics on angles or in 2nd/8th can reverse the promise.
- Mercury-Mars occupation routing by sign/term ruler is a strong example of
  topic manifestation through host/terms rather than planet pair alone.

### `rules/timing-techniques.md`

Primary Firmicus targets:

- Book II.25-28: length of life, ruler of time, allotment of time, division of
  the year.
- Book IV.20: climacteric years.
- Book VI.33-39: planetary rulers of time.

Questions to extract:

- What time-lord periods and sub-periods does Firmicus use?
- Which timing rules require data not currently supported by the v1 skill?
- Which material should remain historical/deferred because it predicts death or
  highly sensitive outcomes?

Book II notes:

- Length-of-life and chronocrator material extracted as historical/deferred.
- Firmicus's time-lord method begins with the Sun in diurnal charts and Moon in
  nocturnal charts, then distributes periods by sign order from the sect light.

Book III notes:

- The third-day Moon check requires postnatal ephemeris data and should remain
  deferred unless supplied.

### `rules/delineation-output-rules.md`

Primary Firmicus targets:

- Book I and Book VII.1: ethics, oath, limits of practice.
- Book II.30: life and training of an astrologer.
- Book VI.40 and Book VIII.32: warnings against quoting isolated rules out of
  context and against judging without all data.

Questions to extract:

- Which warnings reinforce the project's anti-cookbook output discipline?
- What should be transformed into modern process guardrails rather than
  inherited as doctrine?
- How should sensitive Firmicus topics be labeled in outputs?

Book II notes:

- Book II.30 supports output restraint: avoid unsafe questions, do not expose
  vices bluntly, keep responses accountable and non-manipulative.

Book III notes:

- Book III contains many sensitive historical categories: enslavement, sexual
  stigma, illness, punishment, death, and magical/exorcistic material. Extract
  condition logic only; do not copy its social labels into client-facing prose.

## Extraction Rule

Each extracted rule card should include:

```text
Rule name:
Source:
Use when:
Required chart data:
Procedure:
Guardrail:
Brennan cross-ref:
Destination:
Status:
```

Source format:

```text
[Firmicus *Math.* <Book>.<Chapter>] Bram printed p. <n>
```

Use `[new to Firmicus]` when there is no obvious Brennan overlap, and use
`needs verification` when OCR, lacunae, or reconstructed logic make the rule
uncertain.

## Book IV Cross-Module Notes

- `rules/dignities-reference.md`: full/empty degrees and masculine/feminine
  degrees are Firmicus-only degree doctrines and require verification before
  any data-table work.
- `rules/planet-condition-audit.md`: Book IV makes Moon phase, separation,
  application target, and second association required fields in Firmicus lunar
  work.
- `rules/aspect-reception-rules.md`: void-of-course Moon is a natal
  obstruction/depletion rule in Firmicus, not an automatically imported
  electional rule; Moon conjunction/defluction requires terms and sign-boundary
  attention.
- `rules/lots-and-fortune.md`: Fortune has a ruler stack: Fortune sign ruler,
  Fortune terms ruler, sect luminary degree/terms ruler, angularity, aspects,
  and Fortune duodecatemorion. Part of Daemon/Spirit formula in the extracted
  Bram text appears identical to Fortune and is `needs verification`.
- `rules/significator-hierarchy.md`: Firmicus's preferred chart ruler is
  selected from the sign the Moon next enters, skipping luminary domiciles
  because Sun and Moon do not accept individual chart rulership. This differs
  from v1 Ascendant-ruler practice.
- `rules/timing-techniques.md`: Book IV repeats postnatal Moon day checks:
  first, third, seventh, and eleventh. Climacteric years (7/9 cycles,
  especially 63rd year) are historical/deferred lifespan/danger timing.
- `rules/delineation-output-rules.md`: Book IV closes with a whole-data
  requirement: planets, houses, signs, sign nature, house quality, planetary
  condition, courses, phases, conjunctions, and defluctions must be combined
  before a forecast.

## Book V Cross-Module Notes

- `rules/dignities-reference.md`: Book V treats terms and decans as active
  host-routing layers for Ascendant, Mercury, and Moon testimony. Exact degree
  data is required before these can be used.
- `rules/planet-condition-audit.md`: sign nature is operative only when carried
  by an angle or another strong factor; bare-sign cookbook use is unsafe.
  Saturn and Jupiter sign catalogs should feed condition logic, not direct
  placement claims.
- `rules/house-topic-framework.md`: Book V.7 explicitly blocks house-topic
  shortcuts. Jupiter in the 7th is not enough for marriage, and Jupiter in the
  5th is not enough for children, unless the full topic route supports it.
- `rules/aspect-reception-rules.md`: the hospitality rule should feed host and
  reception logic. A benefic in a poor host condition is reduced; a malefic in
  a supportive host condition can be softened or redirected.
- `rules/significator-hierarchy.md`: Book V.7 supports a top-level hierarchy
  rule: topic prediction requires topic house, ruler, occupant/aspector,
  Ascendant witness, sign/degree nature, and timing agreement.
- `rules/timing-techniques.md`: Saturn catalog timing repeatedly invokes first
  Saturn orbit and seventh/ninth-year rhythms; Jupiter material often separates
  early difficulty from later rise through time-lord or transit activation.
- `rules/delineation-output-rules.md`: Book V is the clearest anti-cookbook
  source so far. It contains many sensitive family, illness, death, status, and
  moralized character claims; these were not preserved as client-facing
  statements.

## Book VI Cross-Module Notes

- `rules/house-topic-framework.md`: Book VI.1 repeats house-class precedence:
  first angles, second angles, favorable houses, disconnected houses, and
  dejected houses change the same planetary mixture. Book VI.32 adds computed
  topic houses that supplement ordinary house topics.
- `rules/aspect-reception-rules.md`: Book VI is the strongest source so far for
  superior/right-hand square logic, sextile as reduced trine, conjunction as
  shared hospitality, and benefic/malefic mitigation across square/opposition.
- `rules/planet-condition-audit.md`: bright-star claims require exact degree,
  Moon phase, angularity, and often Jupiter support; they should wait for Book
  VIII verification.
- `rules/lots-and-fortune.md`: Book VI.32 creates Lot-like topic houses from
  planet-to-planet arcs. Sexual desire and necessity explicitly use Fortune and
  Daemon/Spirit formulas from Book IV.
- `rules/significator-hierarchy.md`: derived topic houses do not bypass the
  evidence chain. They require sign ruler, term ruler, occupants, aspects, and
  benefic/malefic testimony before judgment.
- `rules/timing-techniques.md`: Book VI.33-39 says chronocrator periods
  actualize natal promise. Month allotments are Saturn 30, Jupiter 12, Mars 15,
  Sun 19, Venus 8, Mercury 20, Moon 25, but implementation requires Phase B
  verification against Book II.
- `rules/delineation-output-rules.md`: Book VI.40 forbids quoting individual
  sentences out of context. This should become an explicit output rule for
  time-lord and aspect catalog material.

## Book VII Cross-Module Notes

- `rules/delineation-output-rules.md`: Book VII should mostly remain
  restricted-use source material. Exposed infants, slavery/status, illness,
  disability, parent death, sexual stigma, violent death, court sentences, and
  spouse violence were not preserved as client-facing outcomes.
- `rules/reading-workflow.md`: severe predictions in Book VII require a stack:
  luminary/Asc/Fortune weakness, malefic angular pressure, lack of benefic
  protection, sign/degree/term support, and timing activation.
- `rules/house-topic-framework.md`: Book VII confirms that parent, marriage,
  children, illness, necessity, desire, and occupation topics use computed
  topic houses in addition to ordinary house meanings.
- `rules/lots-and-fortune.md`: Book VII repeatedly uses Part of Fortune and its
  ruler for nurture/survival, status, court/necessity, and occupations.
- `rules/significator-hierarchy.md`: parent topics route through Sun/Moon,
  derived father/mother houses, benefic mitigation, and time-lord activation;
  occupation routes through Fortune, occupation house, both rulers, aspects,
  and Mercury's ruler.
- `rules/timing-techniques.md`: parent-death and marriage-timing material
  explicitly depends on time-lord activation; do not treat natal indications as
  active without timing support.
- `rules/planet-condition-audit.md`: Book VII adds cure/mitigation motifs:
  Jupiter/Venus protection, Mercury involvement, and stronger benefics can
  lessen or redirect even severe medical/body claims in the source.
- `rules/lots-and-fortune.md`: Book VII.25 gives Moon-to-Saturn from the
  Ascendant as a house of desire, while Book VI.32 gives Daemon/Fortune by
  sect. Mark this formula conflict `needs verification` before Phase B.

## Book VIII Cross-Module Notes

- `rules/dignities-reference.md`: Book VIII adds several exact-degree overlays:
  90th degree, body-degree zones, Sphaera Barbarica constellations, Ascendant
  degree catalog, and bright-star degrees. All should remain deferred until
  table verification.
- `rules/aspect-reception-rules.md`: signs that see/hear each other are a
  secondary relationship doctrine, not a replacement for ordinary sign-based
  aspects and aversion.
- `rules/planet-condition-audit.md`: bright-star and Sphaera Barbarica claims
  require exact degree, angularity/rising-setting status, Moon condition, and
  benefic/malefic aspects.
- `rules/reading-workflow.md`: Book VIII.18 makes approximate birth data
  insufficient for degree-catalog use. Book VIII.32 then requires all data
  before interpreting any degree overlay.
- `rules/delineation-output-rules.md`: degree catalogs include death modes,
  illness, disability, sexual stigma, enslavement/status, legal punishment, and
  violent occupations. They remain historical/deferred.
- `rules/significator-hierarchy.md`: the 90th degree from Ascendant and Moon is
  a Firmicus-only derived point candidate, but it should not outrank houses,
  luminaries, Fortune, rulers, or time-lord evidence without Phase B review.
- `rules/planet-condition-audit.md`: VIII.32 gives a dignity weighting order:
  exaltation first, own terms second, own houses/domiciles third. Treat this as
  a Firmicus comparison point, not an immediate v1 rule change.
