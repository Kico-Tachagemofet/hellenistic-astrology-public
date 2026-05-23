# Reading Workflow — Evidence-Chain Orchestration

Purpose: define the order the rule modules run in, the hard gate that blocks
interpretive prose until the evidence chain exists, and how the per-module
output templates nest into one final reading.

This is the orchestration layer. It does not add astrological doctrine; it
sequences the modules that do. `SKILL.md` should be a thin wrapper over this
file.

Provenance tag: most of this file is `[project heuristic]` — it is workflow
scaffolding, not distilled from Brennan. Doctrine lives in the modules it
calls. Where a step encodes a sourced rule, that module carries the citation.

## The Hard Gate

```text
No interpretive prose is produced until the Evidence Ledger (below) is filled.
```

If the chart data is insufficient to fill a required section of the ledger,
the workflow stops at that section and reports what is missing. It does not
fill the gap with cookbook keywords. See `data_contract.md` Unknown Handling
and Output Gate.

## Module Run Order

| Step | Module | Produces |
|---|---|---|
| 0 | `data_contract.md` | validated chart data; Output Gate pass/fail |
| 1 | `significator-hierarchy.md` | chart focus; significator roster with roles |
| 2 | `house-topic-framework.md` | topic house(s); `S -> R -> D` ruler chains |
| 3 (subroutine) | `planet-condition-audit.md` | condition verdict per significator and acting planet |
| 4 | `aspect-reception-rules.md` | witnessing/aversion map; testimony and reception between significators |
| 5 | `lots-and-fortune.md` | Lot anchors and their rulers — only if focus or technique requires Lots |
| 6 | `timing-techniques.md` | activated place/time-lord — only if the question is time-bound |
| 7 | `delineation-output-rules.md` | final reading assembled from the ledger |

Notes:

- Step 3 is not a single pass. `planet-condition-audit.md` is the shared
  subroutine — every significator named in steps 1-2 and every planet acting
  in steps 4-6 is audited through it before it is used as evidence.
- Steps 5 and 6 are conditional. A first-pass natal reading with no
  time-bound question and no Lot-dependent focus skips both. Do not run them
  for completeness; run them because the focus needs them.
- Conditional modules have three allowed states: `run`, `skip`, or `blocked`.
  Use `skip` when the focus does not need the module. Use `blocked` when the
  focus needs it, but required data, formulas, or tool support are missing.
  Blocked modules are recorded in `UNRESOLVED`; they are not silently treated
  as clean skips. `[project heuristic]`
- Step 7 cannot start until steps 0-4 (and 5-6 when triggered) are complete.

## The Evidence Ledger

The single artifact produced before any prose. It collects the per-module
output templates without interpreting them.

```text
== CHART ==
Native / label:
Focus / question:
Sect:
Data Gate (data_contract.md): pass / fail — if fail, missing fields:

== FOCUS & ROSTER (significator-hierarchy.md) ==
Chart focus:
Primary significator:
Topic significator(s):
Natural significator(s):
Supporting witnesses:

== TOPIC CHAINS (house-topic-framework.md) ==
For each topic in focus:
  Topic / source house S:
  Ruler R:
  Destination house D:
  R configured to or averse to S:   <- required field, do not skip
  Local tenants in S:
  Chain note (direct / repeated / weak):

== CONDITION AUDITS (planet-condition-audit.md) ==
One Net Judgment block per significator and per acting planet.

== TESTIMONY MAP (aspect-reception-rules.md) ==
One Output block per significant pair (witnessing, direction, reception).
Aversions between significators explicitly listed.

== LOTS (lots-and-fortune.md) — conditional ==
Status: run / skip / blocked
If run: one Basic Lot Audit block per Lot in use.
If skip: focus does not require Lots.
If blocked: focus requires Lots, but data/formula/tooling is missing; state reason and repeat in UNRESOLVED.

== TIMING (timing-techniques.md) — conditional ==
Status: run / skip / blocked
If run: annual profection block, and ZR block only under its own guardrails.
If skip: focus is not time-bound.
If blocked: focus requires timing, but data/table/tooling is missing; state reason and repeat in UNRESOLVED.

== UNRESOLVED ==
Open threads, missing data, unsupported chains moved out of the answer.
```

## Nesting Rule

Each module owns a sub-artifact (Net Judgment, Topic output, Testimony
output, Lot audit, profection block). The ledger holds them side by side.
`delineation-output-rules.md` is the only module allowed to fuse them into
prose, and it must cite which ledger entries support each claim.

Do not let a module's own template become a mini-reading. A condition audit
ends at "Net judgment / Confidence" — it does not narrate the native's life.

## Evidence Standard Carry-Through

The Evidence Standard from `significator-hierarchy.md` (`[project heuristic]`:
a strong conclusion usually needs two or more independent testimonies)
applies at step 7. A claim in the final reading that rests on a single
ledger entry is reported as a clue, not a verdict.

## Guardrails

- No prose before the ledger. This is the whole point of the project.
- Conditional modules (Lots, timing) use `skip` only when the focus does not
  need them; use `blocked` when the focus needs them but required data,
  formulas, or tooling are unavailable.
- Every planet used as evidence is audited first — no exceptions for
  "obvious" placements.
- A failed Data Gate stops the workflow; it does not downgrade to a
  keyword reading.
- The natural significator never leads. It enters the ledger as a witness
  and is audited like any other planet. (See `significator-hierarchy.md`.)
- Unsupported ruler chains go to `UNRESOLVED`, not the answer.

## Source Status

`[project heuristic]` orchestration scaffolding. Step 7 is supplied by
`delineation-output-rules.md`. Case-01 added the `blocked` state for
conditional modules whose focus is triggered but data/formula/tooling is
missing. Run order may be revised after more end-to-end chart tests.
