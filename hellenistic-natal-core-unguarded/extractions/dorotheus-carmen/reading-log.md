# Dorotheus Reading Log

## 2026-05-15 — v2.1 Phase A Dorotheus extraction

Startup checks:

- Read `AGENTS.md`/`CLAUDE.md` contract from the user-provided project instructions.
- Read `STATUS.md` before work.
- Read `extractions/brennan-hellenistic-astrology/chapter-index.md` for extraction form.
- Verified PDF path exists:
  `[local-source-redacted]`.
- Verified target folder was missing, then created only `extractions/dorotheus-carmen/`.
- Honored parallel safety contract: wrote only inside `extractions/dorotheus-carmen/`; did not edit `STATUS.md`, `rules/`, Brennan extractions, sibling skills, cases, samples, or other v2.1 source folders.

Extraction actions:

- Built `chapter-index.md` from the PDF table of contents and checked main-text page mapping.
- Extracted Book I-IV into one file per book:
  - `bookI-births-and-general-delineation.md`
  - `bookII-marriage-parents-children-siblings.md`
  - `bookIII-natal-topics.md`
  - `bookIV-annual-and-continuous.md`
- Created `method-targets.md` to collect Phase B integration candidates.
- Marked Book V as out-of-scope for v3+ horary/inception work.

Rule-card totals:

- Book I cards: 15.
- Book II cards: 13.
- Book III cards: 8.
- Book IV cards: 18.
- Total cards: 54.

Quality notes:

- Book I-III placement/cookbook handling:
  - condition logic extracted: 34 clusters;
  - direct cookbook imports: 0;
  - deferred cookbook/counting clusters: 12.
- `needs verification` markers: 18.
- `[new to Dorotheus]` markers: 33.
- Significant Brennan conflicts: 0 hard conflicts.
- Brennan/v1 timing cross-validation:
  - annual profection one-sign-per-year and lord-of-year logic confirms v1 `timing-techniques.md`;
  - Book IV adds solar revolution chart, month lord, day lord, and transit-to-natal-place layers that v1 does not yet implement;
  - Zodiacal Releasing is not directly cross-validated by Dorotheus Book IV in this pass.

Next:

- Wait for user review of this Dorotheus extraction.
- Phase B should integrate only after the Valens/Firmicus/Dorotheus batch is reviewed together.
- Any update to `rules/source-map.md`, `STATUS.md`, or v1 rules should be done in Phase B or a user-approved non-parallel pass, because this session's write boundary was target-folder-only.
