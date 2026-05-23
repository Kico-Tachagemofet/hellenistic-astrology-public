# Source Map

This file maps reusable rules back to source material.

## Brennan: Hellenistic Astrology

| Rule file | Source chapter(s) | Status |
|---|---|---|
| `data_contract.md` | Ch. 10-12, 16-18; appendix chart data | expanded with whole sign/MC distinction from Ch. 10; Fortune/Spirit optionality and software-vs-canonical dignity conflict handling clarified as `[project heuristic]` |
| `significator-hierarchy.md` | Ch. 10, 12, 13, 16, 17 | multi-role roster handling generalized after case-03; Brennan supports separate ruler chains and Lot-ruler audit, while evidence-counting independence is `[project heuristic]`; v2.1 Phase B added Divinatory/spiritual aptitude focus row anchored on Ch.10 9th/12th + sect light material |
| `planet-condition-audit.md` | Ch. 7, 8, 10, 14, 15 | expanded from Ch. 7, Ch. 8, and Ch. 14; includes Mercury sect default and solar visibility thresholds from Ch. 7; `undeclared` sect output and canonical dignity conflict handling are `[project heuristic]` |
| `dignities-reference.md` | Ch. 8 | deterministic dignity tables drafted: domicile, adversity, exaltation/fall, triplicity rulers, Egyptian bounds, decans |
| `house-topic-framework.md` | Ch. 10, 11, 13; Ch. 12 for Asc ruler routing | expanded from Ch. 10 and Ch. 12-13 |
| `aspect-reception-rules.md` | Ch. 9, 14 | expanded from Ch. 9 and Ch. 14; sign-based configuration not orb-gated and not degree-reclassified by out-of-sign aspect family labels clarified from Ch. 9; v1 overcoming boundary and mutual non-hosting are `[project heuristic]` |
| `lots-and-fortune.md` | Ch. 16, 18 | expanded from Ch. 16 and Ch. 18; Fortune/Spirit formulas sourced from Ch. 16; v2.1 Phase B added cross-source references (Valens / Firmicus Bram needs-verification / Dorotheus) plus candidate-Lot register (Religion, Eros) deferred to v2.x |
| `timing-techniques.md` | Ch. 15, 17, 18 | expanded from Ch. 17 and Ch. 18 |
| `reading-workflow.md` | none — `[project heuristic]` orchestration scaffolding | drafted; conditional module `blocked` state added after case-01 |
| `delineation-output-rules.md` | none — `[project heuristic]` output discipline | drafted; well-evidenced mixed testimony clarified after case-01 |
| `cross-source-method-comparison.md` | Brennan baseline + Valens / Firmicus / Dorotheus positions | new file, v2.1 Phase B; reference companion, **not** part of reading workflow; registers four-source positions on 12 method points (Mercury sect, Daemon/Fortune formulas, chart ruler, dignity weighting, Leo decan, triplicity ordering, listening/beholding, solar revolutions, monthly/chronocrator lord, phase thresholds, Moon application doctrine, Fortune ruler stack) |

## Dorotheus: Carmen Astrologicum

**Source**: Dorotheus of Sidon, *Carmen Astrologicum: The 'Umar al-Tabari
Translation*, trans. Benjamin Dykes, 2017 (Cazimi Press).

**Transmission**: Greek original lost; survives via 'Umar al-Tabari's Arabic
translation, then to Latin and into Dykes's 2017 English. All Dorothean
citations carry the chain marker `[via 'Umar al-Tabari → Dykes 2017]`.

**Page-citation style**: `[Dorotheus *Carmen* <Book>.<Verse> via 'Umar
al-Tabari → Dykes 2017]` with Dykes printed page when applicable.

**PDF / book location**: Dykes 2017 printed book (Cazimi Press); page
numbers refer to the printed edition.

**Extraction directory**: `extractions/dorotheus-carmen/` (7 files, 54 rule
cards; chapter-index.md / reading-log.md / method-targets.md + bookI /
bookII / bookIII / bookIV). Book V (horary/inception) out-of-scope for v1
natal-core.

**Phase B status**: Phase A extraction complete (2026-05-15). Phase B
integrated:

- Annual profection confirmation (Bk.IV.1) — cross-ref noted; v1 unchanged.
- Lot of Religion `[Source-only candidate, needs verification]` — registered
  in `lots-and-fortune.md` candidate section and `cross-source-method-
  comparison.md`; deferred to v2.x.
- Stacked significator logic + Fortune as status/assets anchor — confirms
  v1 baseline.

## Valens: Anthology

**Source**: Vettius Valens, *Anthologies*, trans. Mark Riley.

**Transmission**: Greek original transmitted through Byzantine manuscripts;
Mark Riley provides an English working translation. Citations use Mark
Riley's translation as the working text.

**Page-citation style**: `[Valens *Anth.* <Book>.<Chapter>]` with PDF local
page + Mark Riley's K (Kroll) / P (Pingree) numbering when relevant. K/P
double numbering is the Valens convention for cross-edition reference.

**PDF / book location**: Mark Riley PDF (Valens Anthology, English working
translation).

**Extraction directory**: `extractions/valens-anthology/` (14 files, 74
rule cards; chapter-index.md / reading-log.md / method-targets.md + bookI-
foundations / bookI-calculation / bookII / bookIII / bookIV / bookV /
bookVI / bookVII / bookVIII / bookIX + appendix-fifth-century-addition.md
preserved separately from Valens core).

**Phase B status**: Phase A extraction complete (2026-05-15). Phase B
integrated:

- IX = God / III = Goddess + planetary divinatory significations — primary
  support for divinatory/spiritual aptitude focus row in
  `significator-hierarchy.md`.
- Daimon distinct from Fortune cross-ref noted in `lots-and-fortune.md`.
- Listening / beholding signs by rising-time affinity — registered in
  cross-source layer; permanent-deferred (specialist supplement, not v1
  core).
- Triplicity ruler ordering possible variation — logged in cross-source
  layer; v2.x verification candidate.

## Firmicus: Mathesis

**Source**: Firmicus Maternus, *Mathesis*, trans. Jean Rhys Bram (1975).

**Transmission**: Latin original survives; Bram 1975 is the standard
English working translation. Citations refer to Bram printed page numbers.

**Page-citation style**: `[Firmicus *Math.* <Book>.<Chapter>]` Bram
printed page <n>. Bram chapter numbering follows the Latin Mathesis books
I-VIII.

**PDF / book location**: `[local-source-redacted]` (Bram 1975 scan).

**Extraction directory**: `extractions/firmicus-mathesis/` (11 files, 133
rule cards; chapter-index.md / reading-log.md / method-targets.md +
bookI - bookVIII).

**Phase B status**: Phase A extraction complete (2026-05-15). Phase B
integrated:

- Mercury sect direct nocturnal (Bk.II.7) — registered in cross-source
  layer; v1 keeps visibility-based baseline.
- Daemon / Fortune Bram printed formula irregularity (Bk.IV.18) —
  `needs verification` flagged in `lots-and-fortune.md` Notes and
  cross-source layer.
- Chart ruler Moon-next-entry method (Bk.IV.19) — registered in
  cross-source layer; v1 keeps Ascendant ruler baseline.
- Dignity weighting order (Bk.VIII.32) — registered in cross-source layer;
  v1 keeps unweighted baseline.
- Leo third decan OCR conflict (Bk.II.4) — Phase B.6 PDF verification.
- 9th-house sacred / temple / divinatory material (Bk.III) — primary
  support for divinatory/spiritual aptitude focus row.
- Sphaera Barbarica / degree catalogs / 90th degree / bright-star degrees
  — permanent-deferred (require ephemeris + historical/sensitive content).

## Citation Policy

- Keep page references and short paraphrases.
- Do not paste long passages from copyrighted books.
- If a rule is uncertain or reconstructed, mark it as `needs verification`.
- Dorothean citations must carry `[via 'Umar al-Tabari → Dykes 2017]` to
  preserve the transmission chain.
