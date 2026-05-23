# Firmicus *Mathesis* Chapter Index

Source: Julius Firmicus Maternus, *Matheseos libri octo* / *Mathesis*,
translated by Jean Rhys Bram as *Ancient Astrology Theory and Practice*
(Noyes Press, 1975).

PDF: `[local-source-redacted]`

PDF mapping note: the first arabic printed page appears at PDF page 5, so
printed page `n` is usually PDF page `n + 4` for the main text.

TOC status:

- Book-level starts are taken from the printed table of contents.
- Chapter-level headings are reconstructed from body OCR. Marked titles may need
  spot-checking against page images where OCR is visibly noisy.
- Extraction status values: `pending`, `partial`, `done`, `out-of-scope`.

Parallel boundary:

- This extraction pass writes only inside `extractions/firmicus-mathesis/`.
- v1 rules, Brennan extractions, sibling skills, cases, samples, source folders,
  root status/roadmap docs, and the other v2.1 source folders are read-only for
  this session.

## Book Map

| Unit | Printed pages | PDF pages | Planned extraction file | Priority | Status | Notes |
|---|---:|---:|---|---|---|---|
| Introduction | 1-10 | 5-14 | none | Low | pending | Historical / translator context only. |
| Book I | 11-30 | 15-34 | `bookI-defense-of-astrology.md` | Low | done | 7 context/process cards; no technical chart rules. |
| Book II | 31-70 | 35-74 | `bookII-planet-doctrine.md` | High | done | 26 rule cards: signs, dignities, houses, aspects, timing basics, antiscia, astrologer ethics. |
| Book III | 71-116 | 75-120 | `bookIII-houses-and-planets-in-houses.md` | High | done | 18 rule cards: Thema Mundi, planet-in-house condition stack, Mercury combinations, Moon/Fortune. |
| Book IV | 117-154 | 121-158 | `bookIV-aspects-and-timing.md` | High | done | 24 rule cards: Moon motion, Fortune/Daemon, chart ruler, timing, occupations, degree doctrines. |
| Book V | 155-181 | 159-185 | `bookV-combinations.md` | Medium | done | 13 rule cards: angular sign carrier, Asc terms, Saturn/Jupiter catalogs distilled, Mercury/Moon terms-decans, whole-chart synthesis gate. |
| Book VI | 182-232 | 186-236 | `bookVI-combinations-continued.md` | Medium-High | done | 20 rule cards: house classes, aspect-family logic, conjunctions, derived topic houses, chronocrator periods, anti-quote guardrail. |
| Book VII | 233-265 | 237-269 | `bookVII-life-prediction.md` | Medium | done | 14 method cards: oath/output restraint, nurture threshold, twins, status/captivity, medical/death/legal sensitive handling, marriage/children/occupations. |
| Book VIII | 266-302 | 270-306 | `bookVIII-decans-and-spheres.md` | Medium-Low | done | 11 method cards: 90th degree, sign hearing/seeing, body degrees, Sphaera Barbarica, Myriogenesis-like degree catalog, bright stars, whole-data guardrail. |
| Notes | 303-314 | 307-318 | reference only | Low | pending | Use only to clarify source / OCR uncertainty. |
| Indexes, bibliography, glossary | 315-333 | 319-337 | reference only | Low | pending | Use glossary / occupation index only as aids. |

## Book I - Defense of Astrology

Target file: `bookI-defense-of-astrology.md`

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| Proemium | Proemium | 11 | 15 | done | Dedication and frame. |
| I | The opponents of astrology | 12 | 16 | done | Philosophical defense only. |
| II | The argument from human types | 14 | 18 | done | Polemical; body/race material out of scope. |
| III | Impossibility of definitive measurements | 15 | 19 | done | Data-discipline guardrail. |
| IV | Divine nature of the heavens | 17 | 21 | done | Philosophical context. |
| V | Refutation of arguments | 19 | 23 | done | Fatalism as source stance. |
| VI | Astrology encourages divine worship | 20 | 24 | done | Practitioner ethos. |
| VII | Examples from history | 20 | 24 | done | Anecdotes not validation cases. |
| VIII | Belief that Fate controls death only | 26 | 30 | done | Fate doctrine context only. |
| IX | Types of human death | 27 | 31 | done | Sensitive topic inventory only. |
| X | Conclusion; invocation to the emperor | 28 | 32 | done | Theological context only. |

## Book II - Planet Doctrine and Foundations

Target file: `bookII-planet-doctrine.md`

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| Praefatio | Praefatio | 31 | 35 | done | Learning order and antiscia setup. |
| I | The twelve signs | 32 | 36 | done | Gender of signs; cross-ref Brennan Ch.8. |
| II | The signs of the planets | 32 | 36 | done | Domicile schema; cross-ref dignity reference. |
| III | Exaltations and falls of the planets | 32 | 36 | done | Exaltation/fall degrees; compare Brennan Ch.8. |
| IV | The decanate | 34 | 38 | done | Decan rulers and decan strength; table variant needs verification. |
| V | The degrees of the signs | 36 | 40 | done | Degree/minute data requirement. |
| VI | The terms | 36 | 40 | done | Bounds/terms; matches existing table pending Phase B. |
| VII | The conditions of the planets | 38 | 42 | done | Diurnal/nocturnal condition; Mercury tension recorded. |
| VIII | Matutine and vespertine planets | 38 | 42 | done | Solar phase terminology. |
| IX | By how many degrees planets become matutine or vespertine | 39 | 43 | done | Visibility thresholds; high relevance to audit rules. |
| X | Nature and characteristics of the signs | 39 | 43 | partial | Sign taxonomy; lacunose/OCR-limited. |
| XI | Risings of the signs | 40 | 44 | done | Regional rising times; deferred. |
| XII | Which signs are subject to which winds | 42 | 46 | done | Environmental/directional context; deferred. |
| XIII | The duodecatemoria | 42 | 46 | done | Derived-degree technique; deferred. |
| XIV | The eight houses | 43 | 47 | done | House/angle framework. |
| XV | The cardinal points of the nativities | 44 | 48 | done | Angles and quadrant concepts. |
| XVI | The four following favorable houses | 47 | 51 | done | Favorable houses. |
| XVII | Unaspected houses | 47 | 51 | done | Aversion from Ascendant; cross-ref Brennan Ch.10. |
| XVIII | The sequence of each house | 47 | 51 | done | Preceding/following house logic. |
| XIX | Meaning of the twelve houses | 48 | 52 | done | House topics. |
| XX | Names of the twelve houses, planets allotted to them, and predictions | 51 | 55 | done | Planetary joys / house names; compare Brennan. |
| XXI | Types of nativities | 53 | 57 | done | Overall chart quality heuristics. |
| XXII | The aspects: trine, square, sextile, opposition, and the unaspected | 53 | 57 | done | Aspect taxonomy. |
| XXIII | How the aspects are connected to the Ascendant | 54 | 58 | done | Ascendant witnessing. |
| XXIV | Body parts allotted to signs | 56 | 60 | done | Medical/body-topic reference; sensitive/deferred. |
| XXV | Forecasting the length of life | 56 | 60 | done | Sensitive; extracted as historical/deferred method. |
| XXVI | The Ruler of Time | 57 | 61 | done | Chronocrator basics. |
| XXVII | The allotment of time | 58 | 62 | done | Planetary period allotments. |
| XXVIII | The division of the year | 58 | 62 | done | Annual subdivisions. |
| XXIX | The antiscia | 58 | 62 | done | Antiscia method. |
| XXX | Life and training of an astrologer | 68 | 72 | done | Practitioner ethics; output restraint. |

## Book III - Houses and Planets in Houses

Target file: `bookIII-houses-and-planets-in-houses.md`

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| Proemium | Proemium | 71 | 75 | done | Scope statement; propositions over rhetoric. |
| I | Thema Mundi | 71 | 75 | done | Teaching model; Mercury common doctrine. |
| II | Saturn | 75 | 79 | done | Planet in houses distilled to condition logic. |
| III | Jupiter | 78 | 82 | done | Planet in houses distilled to condition logic. |
| IV | Mars | 82 | 86 | done | Planet in houses distilled to condition logic. |
| V | The Sun | 88 | 92 | done | Planet in houses distilled to condition logic. |
| VI | Venus | 94 | 98 | done | Planet in houses distilled to condition logic; sensitive language excluded. |
| VII | Mercury | 99 | 103 | done | Mercury condition and phase logic. |
| VIII | Mercury and the Sun | 103 | 107 | done | Solar co-presence logic. |
| IX | Saturn and Mercury | 104 | 108 | done | Combination logic. |
| X | Mercury and Jupiter | 106 | 110 | done | Combination logic. |
| XI | Mercury and Mars | 108 | 112 | done | Occupation routing by host/terms. |
| XII | Mercury and Venus | 111 | 115 | done | Combination logic. |
| XIII | The Moon | 113 | 117 | partial | Moon in houses; houses five through eight missing in source. |
| XIV | The Moon in the Part of Fortune | 115 | 119 | done | Lot of Fortune cross-ref; third-day Moon check. |

## Book IV - Aspects, Lots, Moon Motion, and Timing

Target file: `bookIV-aspects-and-timing.md`

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| Proemium | Proemium | 117 | 121 | done | Scope statement. |
| I | Power of the Moon | 118 | 122 | done | Moon as chart-wide operative factor. |
| II | The Moon and Saturn | 119 | 123 | done | Application/aspect logic. |
| III | The Moon and Jupiter | 120 | 124 | done | Application/aspect logic. |
| IV | The Moon and Mars | 120 | 124 | done | Application/aspect logic. |
| V | The Moon and the Sun | 121 | 125 | done | Application/aspect logic. |
| VI | The Moon and Venus | 121 | 125 | done | Application/aspect logic; sensitive language excluded. |
| VII | The Moon and Mercury | 122 | 126 | done | Application/aspect logic. |
| VIII | If the Moon is moving toward nothing (void of course) | 123 | 127 | done | Void-of-course rule. |
| IX | Phases of the Moon | 123 | 127 | done | Moon separating from Saturn sequence. |
| X | The Moon moving from Jupiter | 124 | 128 | done | Lunar defluction/application sequences. |
| XI | The Moon moving from Mars | 126 | 130 | done | Lunar defluction/application sequences. |
| XII | The Moon moving from the Sun | 127 | 131 | done | Lunar defluction/application sequences. |
| XIII | The Moon moving from Venus | 128 | 132 | done | Lunar defluction/application sequences. |
| XIV | The Moon moving from Mercury | 130 | 134 | done | Lunar defluction/application sequences. |
| XV | Phases of the Moon | 133 | 137 | done | Moon moving away from planets toward nothing. |
| XVI | Other indications of the Moon | 134 | 138 | done | Moon summary rules and mitigations. |
| XVII | The Part of Fortune and its effects | 135 | 139 | done | Fortune formula / ruler stack. |
| XVIII | The Part of the Daemon | 137 | 141 | done | Spirit/Daemon formula needs verification. |
| XIX | The ruler of the chart | 138 | 142 | done | Firmicus chart ruler / lord logic. |
| XX | The climacteric years | 144 | 148 | done | Timing technique; sensitive/deferred. |
| XXI | Occupations | 145 | 149 | done | Occupation logic; no job-list cookbook. |
| XXII | Empty and full houses | 147 | 151 | done | Full/empty degree doctrine; needs verification. |
| XXIII | Masculine and feminine degrees | 150 | 154 | done | Degree doctrine; needs verification. |
| XXIV | The Moon with others on the angles | 152 | 156 | done | Angular co-presence logic. |
| XXV | Conjunctions and defluctions of the Moon | 153 | 157 | done | Exact lunar handoff rule. |

## Book V - Combinations

Target file: `bookV-combinations.md`

Book V is a high-risk cookbook zone. Distill only condition logic, or mark
`[cookbook: Firmicus *Math.* V.<ch>, condition-logic TBD]`.

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| Praefatio | Praefatio | 155 | 159 | done | Scope statement; Book V as controlled cookbook zone. |
| I | The signs | 156 | 160 | done | Sign nature requires angular carrier; Myriogenesis deferred. |
| II | The Ascendant | 163 | 167 | done | Ascendant terms and planets in those terms distilled to condition logic. |
| III | Saturn in different signs | 166 | 170 | done | Placement catalog distilled to delay/cycle/mitigation logic; direct outcomes deferred. |
| IV | Jupiter in different signs | 174 | 178 | done | Placement catalog distilled to host/timing/support logic; direct outcomes deferred. |
| Lacuna | The Sun, Venus, and Mars missing | 177 | 181 | done | Lacuna recorded; no reconstruction from elsewhere. |
| V | Mercury in different signs | 178 | 182 | done | Terms/decans host-routing distilled; direct event list deferred. |
| VI | The Moon in different signs | 178 | 182 | done | Phase/sect/host-routing distilled; direct event list deferred. |
| VII | Conclusion | 180 | 184 | done | Whole-chart synthesis gate and hospitality rule. |

## Book VI - Combinations Continued

Target file: `bookVI-combinations-continued.md`

Book VI contains many combination lists. Keep extraction condition-based and
do not preserve placement-by-placement outputs as reusable rules.

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| I | The houses | 182 | 186 | done | House-class prerequisite for combinations. |
| II | Bright stars | 183 | 187 | done | Fixed-star / bright-star notes extracted as exact-degree material; needs verification. |
| III | Saturn in trine | 184 | 188 | done | Trine condition logic; direct pair outcomes deferred. |
| IV | Jupiter in trine | 185 | 189 | done | Trine condition logic; direct pair outcomes deferred. |
| V | Mars in trine | 186 | 190 | done | Trine condition logic; direct pair outcomes deferred. |
| VI | The Moon and Sun in trine | 187 | 191 | done | Trine condition logic; direct pair outcomes deferred. |
| VII | The Moon and Venus in trine | 187 | 191 | done | Trine condition logic; direct pair outcomes deferred. |
| VIII | The Moon and Mercury in trine | 187 | 191 | done | Trine condition logic; direct pair outcomes deferred. |
| IX | Saturn in square aspect | 187 | 191 | done | Superior/right-square and mitigation logic. |
| X | Jupiter in square | 189 | 193 | done | Superior/right-square and mitigation logic. |
| XI | Mars in square aspect | 190 | 194 | done | Superior/right-square and mitigation logic; sensitive outcomes deferred. |
| XII | The Sun and Moon in square aspect | 191 | 195 | done | Luminary square depends on other planet testimony. |
| XIII | Venus and Mercury in square aspect | 192 | 196 | done | Direct pair outcomes deferred. |
| XIV | The Moon and Mercury in square aspect | 192 | 196 | done | OCR title reconstructed; direct pair outcomes deferred. |
| XV | Saturn in opposition | 193 | 197 | done | Opposition condition logic and mitigation. |
| XVI | Jupiter in opposition | 195 | 199 | done | Opposition condition logic and mitigation. |
| XVII | Mars in opposition | 196 | 200 | done | Opposition condition logic; sensitive outcomes deferred. |
| XVIII | Sun and Moon in opposition | 196 | 200 | done | Opposition condition logic; direct outcomes deferred. |
| XIX | Venus and the Moon in opposition | 196 | 200 | done | Opposition condition logic; direct outcomes deferred. |
| XX | Mercury and the Moon in opposition | 197 | 201 | done | Opposition condition logic; direct outcomes deferred. |
| XXI | Sextile aspect | 197 | 201 | done | Sextile as reduced trine-like contact; sign-context line needs verification. |
| XXII | Saturn in conjunction | 197 | 201 | done | Conjunction and co-presence condition logic. |
| XXIII | Jupiter in conjunction | 199 | 203 | done | Conjunction and co-presence condition logic. |
| XXIV | Mars in conjunction | 200 | 204 | done | Conjunction condition logic; sensitive outcomes deferred. |
| XXV | The Sun in conjunction | 201 | 205 | done | Solar co-presence, phase, and luminary conjunction conditions. |
| XXVI | Venus in conjunction | 202 | 206 | done | Conjunction condition logic; sensitive outcomes deferred. |
| XXVII | The Moon and Mercury in conjunction | 203 | 207 | done | Degree order and Jupiter mitigation noted. |
| XXVIII | The Moon in conjunction | 203 | 207 | done | Prenatal Moon attachment extracted; OCR title malformed. |
| XXIX | Charts of ill omen | 204 | 208 | done | Multi-factor threshold extracted; direct sensitive outcomes deferred. |
| XXX | Charts showing the influence of Venus | 206 | 210 | done | Famous charts treated as rhetorical examples, not validation cases. |
| XXXI | Complex aspects | 210 | 214 | done | 91 example clauses deferred; full-configuration logic extracted. |
| XXXII | Meanings of houses | 219 | 223 | done | Derived topic houses and formula inventory extracted; several formulas need verification. |
| XXXIII | Saturn as Ruler of Time | 226 | 230 | done | Time-lord period/subperiod logic. |
| XXXIV | Jupiter as Ruler of Time | 227 | 231 | done | Time-lord period/subperiod logic. |
| XXXV | Mars as Ruler of Time | 228 | 232 | done | Roman numeral absent in OCR; title reconstructed. |
| XXXVI | The Sun as Ruler of Time | 229 | 233 | done | Time-lord period/subperiod logic. |
| XXXVII | Venus as Ruler of Time | 230 | 234 | done | Time-lord period/subperiod logic. |
| XXXVIII | Mercury as Ruler of Time | 231 | 235 | done | Time-lord period/subperiod logic. |
| XXXIX | The Moon as Ruler of Time | 231 | 235 | done | Time-lord period/subperiod logic. |
| XL | Conclusion | 232 | 236 | done | Anti-quote context guardrail. |

## Book VII - Life Prediction

Target file: `bookVII-life-prediction.md`

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| I | The astrologer's oath | 233 | 237 | done | Practitioner discipline translated to restricted-use/output restraint. |
| II | Charts of exposed infants | 234 | 238 | done | Sensitive life/death doctrine; severe-threshold method only. |
| III | Charts of twins | 237 | 241 | done | Double/fertile sign and Jupiter-Mercury-Moon pattern; practical use deferred. |
| IV | Charts of slaves | 238 | 242 | done | Historical status topic; condition pattern only. |
| V | Number of masters | 240 | 244 | done | Historical status topic; direct counts deferred. |
| VI | Parents as slaves | 241 | 245 | done | Historical status/captivity topic; direct claims deferred. |
| VII | Charts of animals | 242 | 246 | out-of-scope | Non-human nativity material; not for v2.1 natal core. |
| VIII | Physical infirmities | 243 | 247 | done | Medical/body doctrine; historical/deferred. |
| IX | Death of parents | 244 | 248 | done | Sensitive parent-topic method; direct predictions deferred. |
| X | Hostility to parents | 245 | 249 | done | Family-topic condition logic; direct violence claims deferred. |
| XI | Orphans | 246 | 250 | done | Sensitive topic; historical method only. |
| XII | Number of marriages | 247 | 251 | done | Marriage-topic routing; direct counts deferred. |
| XIII | Incest | 247 | 251 | done | Sensitive; direct claims deferred. |
| XIV | Kinds of marriages | 248 | 252 | done | Marriage-topic condition logic; sensitive claims deferred. |
| XV | Lovers of boys | 248 | 252 | done | Historical sexual categories; not client-facing. |
| XVI | Number of wives | 249 | 253 | done | Historical marriage doctrine; timing method noted. |
| XVII | Murder of spouses | 250 | 254 | done | Sensitive topic; historical method only. |
| XVIII | Kinds of mates | 250 | 254 | done | OCR reads "mayes"; title normalized; sensitive outcomes deferred. |
| XIX | Children | 251 | 255 | done | Children/fertility topic; historical/deferred. |
| XX | Mental deficiencies and other afflictions | 252 | 256 | done | Medical/ableist historical text; condition pattern only. |
| XXI | Physical infirmities | 254 | 258 | done | Medical/body doctrine; mitigation/cure logic extracted historically. |
| XXII | Royal charts | 255 | 259 | done | Eminence stack extracted. |
| XXIII | Violent death | 256 | 260 | done | Sensitive severe-threshold method only. |
| XXIV | Court sentences | 260 | 264 | done | Legal consequences topic; house of necessity route extracted. |
| XXV | House of sexual desire | 261 | 265 | done | Sensitive sexual-topic doctrine; formula conflict marked needs verification. |
| XXVI | House of occupations | 264 | 268 | done | Occupation routing through Fortune, occupation house, rulers, terms, Mercury condition. |

## Book VIII - Decans, Sphaera Barbarica, and Degree Catalogs

Target file: `bookVIII-decans-and-spheres.md`

Book VIII has many degree-by-degree catalogs. These should usually be tabled
or deferred, not treated as direct natal delineation recipes.

| Ch. | Title | Printed start | PDF start | Status | Extraction note |
|---:|---|---:|---:|---|---|
| I | The astrologer's creed | 266 | 270 | done | Practitioner creed translated to equanimity/output restraint. |
| II | The ninetieth degree | 267 | 271 | done | Enenecontameris doctrine extracted; implementation deferred. |
| III | Signs which see and hear each other | 268 | 272 | done | Sign relationship doctrine extracted; full table deferred. |
| IV | Individual degrees | 269 | 273 | done | Body-part degree allocation extracted as table/deferred material. |
| V | Signs near the zodiac | 271 | 275 | done | Sphaera Barbarica setup extracted. |
| VI | Aries | 272 | 276 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| VII | Taurus | 274 | 278 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| VIII | Gemini | 275 | 279 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| IX | Cancer | 275 | 279 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| X | Leo | 276 | 280 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XI | Virgo | 276 | 280 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XII | Libra | 277 | 281 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XIII | Scorpio | 278 | 282 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XIV | Sagittarius | 278 | 282 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XV | Capricorn | 279 | 283 | done | OCR title noisy; normalized; constellation catalog deferred. |
| XVI | Aquarius | 279 | 283 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XVII | Pisces | 280 | 284 | done | Constellation catalog deferred; rising/setting condition logic extracted. |
| XVIII | The Myriogenesis | 281 | 285 | done | Exact-degree requirement extracted; minute-level doctrine deferred. |
| XIX | Aries | 282 | 286 | done | Degree-by-degree ascendant catalog deferred; 24th degree missing. |
| XX | Taurus | 283 | 287 | done | Degree-by-degree ascendant catalog deferred. |
| XXI | Gemini | 285 | 289 | done | Degree-by-degree ascendant catalog deferred. |
| XXII | Cancer | 286 | 290 | done | Degree catalog deferred; 11th-24th degrees missing. |
| XXIII | Leo | 287 | 291 | done | Degree catalog deferred; 11th-30th degrees missing. |
| XXIV | Virgo | 288 | 292 | done | Degree-by-degree ascendant catalog deferred. |
| XXV | Libra | 289 | 293 | done | Degree-by-degree ascendant catalog deferred. |
| XXVI | Scorpio | 290 | 294 | done | Degree-by-degree ascendant catalog deferred. |
| XXVII | Sagittarius | 292 | 296 | done | Degree-by-degree ascendant catalog deferred. |
| XXVIII | Capricorn | 294 | 298 | done | Degree catalog deferred; 28th and 30th degrees missing. |
| XXIX | Aquarius | 296 | 300 | done | Degree catalog deferred; 7th and 18th degrees missing. |
| XXX | Pisces | 298 | 302 | done | Degree-by-degree ascendant catalog deferred. |
| XXXI | Bright stars | 300 | 304 | done | Bright-star doctrine extracted; needs verification. |
| XXXII | Necessity of all data | 301 | 305 | done | Whole-data guardrail extracted; high process relevance. |
| XXXIII | Conclusion | 302 | 306 | done | Restricted-use conclusion extracted as context. |

## OCR / Verification Notes

- OCR is usable, but headings sometimes contain obvious errors: e.g. `HEAVI:NS`,
  `UFE`, `MASCUUNE`, `AFFUCTIONS`, `UBRA`, `MAYES`.
- Book VI XIV lacks a visible roman numeral in the OCR but the title appears at
  printed p. 192; reconstructed as "The Moon and Mercury in square aspect."
- Book VI XXXV lacks a visible roman numeral in the OCR but the title appears at
  printed p. 228; reconstructed as "Mars as Ruler of Time."
- Book VIII XV has noisy OCR around "Capricorn"; title normalized from the sign
  sequence.
- Book V explicitly reports a lacuna: the Sun, Venus, and Mars in different signs
  are missing. Do not reconstruct those chapters from external summaries in this
  extraction pass.
