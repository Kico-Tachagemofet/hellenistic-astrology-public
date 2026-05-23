# Traditional Astrology Data Contract

This is the minimum chart data needed before a Hellenistic / traditional natal reading can be treated as structured rather than impressionistic.

## Metadata

```text
Native / chart label:
Birth date:
Birth time:
Birth place:
Timezone/source:
Calendar:
House system used for topic layer: Whole Sign Houses by default
Chart calculation source:
Time reliability:
Question / chart focus:
```

## Required Natal Data

| Field | Required | Notes |
|---|---|---|
| Ascendant sign and degree | yes | primary chart anchor; rising sign is entire 1st place in whole sign mode |
| MC degree | yes | public/action witness; may fall outside 10th whole sign place |
| IC/Desc degree | important | angle map and angular triads |
| Planet sign and degree | yes | Sun through Saturn; include visible planets first |
| Planet speed / retrograde | important | needed for condition audit |
| Sect: day or night chart | yes | affects benefic/malefic condition and sect light |
| Whole sign house placement | yes | main place/topic layer |
| Angularity / pivot relationship | important | dynamic strength layer, especially MC and pivots |
| Domicile rulers | yes | ruler-chain reasoning |
| Essential dignity state | important | domicile, exaltation, triplicity, terms/bounds, decans as available |
| Visibility | important | under beams, heliacal phase, morning/evening as available |
| Major aspects/configurations | yes | sign-based first; degree-based when available |
| Aversion map | important | identifies lack of direct witnessing |
| Fortune and Spirit | required for Lots/timing work | optional for first-pass natal, required for zodiacal releasing and derived Lot analysis |
| Other Lots | optional | include formula/source and only use when topic demands it |
| Annual profection place | required for annual timing | age modulo 12 from whole sign Ascendant |
| Lord of the year | required for annual timing | domicile ruler of profected place |
| Time-lord state | optional first pass | required for timing questions |

## Derived Whole Sign Fields

For each planet and Lot, record:

```text
Sign:
Degree:
Whole sign place number:
Domicile ruler:
Configured places/signs:
Averted places/signs:
Angular/succedent/cadent status:
Fortune/Spirit relation if relevant:
```

## Unknown Handling

- Fortune/Spirit optionality is a data-gate rule: first-pass natal can proceed without them. If `significator-hierarchy.md` marks Fortune or Spirit as relevant witnesses for the focus, run, skip, or block the Lots module under `reading-workflow.md` rather than treating the Output Gate as failed.
- Conflict Handling: if software-supplied dignity labels conflict with `dignities-reference.md`, use the project canonical value from `dignities-reference.md` and log the discrepancy in the Evidence Ledger. `[project heuristic]`
- If birth time is missing, do not use houses, Ascendant ruler, Lots, or time-lord techniques that depend on the Ascendant.
- If only sign placements are available, restrict the reading to broad planetary condition and sign-based configurations.
- If house system is uncertain, mark whole sign assumptions explicitly.
- If a method requires degree precision, do not infer it from rounded positions.
- If using a modern chart generated in Placidus or another quadrant system, preserve the original data but create a whole sign topic map before Hellenistic delineation.

## Output Gate

A chart is ready for full natal delineation only when Ascendant, sect, seven traditional planets by sign/degree, and whole sign place placements are known.
