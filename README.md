# Hellenistic Astrology Skills for Claude Code

An 8-skill set for Hellenistic natal astrology readings, designed as [Claude Code](https://claude.ai/code) skills.

Built on primary-source extractions from Brennan, Valens, Dorotheus, and Firmicus. Evidence-chain workflow — no cookbook readings.

## Skills

| Skill | Role |
|---|---|
| **hellenistic-natal-core-unguarded** | Stage 2/3 finding production + chart-finding-index. Doctrine hub (`rules/`, `extractions/`) |
| **hellenistic-reader-unguarded** | Stage 1 data extraction + audit + pre-validation R1 |
| **hellenistic-render-unguarded** | Reader-facing Chinese prose rendering (anti-cliche rules, session learnings) |
| **hellenistic-career-unguarded** | 10H + MC + Lot of Fortune/Spirit deep dive |
| **hellenistic-family-unguarded** | 4H + Sun/Moon parents + Lot of Father/Mother |
| **hellenistic-partnership-unguarded** | 7H + Venus + Lot of Marriage deep dive |
| **hellenistic-rectifier-unguarded** | Birth-time rectification via Hellenistic timing |
| **hellenistic-timing-unguarded** | Profections / ZR / Loosing of the Bond / planetary years |

## Pipeline

```
reader (Stage 1 + pre-validation)
  → natal-core (Stage 2 per-topic findings + Stage 3 consolidation)
    → render (Chinese prose deliverable + optional HTML)
```

Topic deep dives (career / family / partnership) plug into Stage 2 as sibling dispatches.

## Installation

Copy any skill directory into `~/.claude/skills/`:

```bash
cp -r hellenistic-natal-core-unguarded ~/.claude/skills/
```

Or clone the whole repo and symlink:

```bash
git clone git@github.com:Kico-Tachagemofet/hellenistic-astrology-public.git
ln -s $(pwd)/hellenistic-astrology-public/hellenistic-natal-core-unguarded ~/.claude/skills/
```

## What's inside `natal-core`

```
hellenistic-natal-core-unguarded/
├── SKILL.md                    # Entry point + workflow orchestration
├── CLAUDE.md                   # Project-level instructions
├── method-index.md             # Navigation map
├── extractions/                # Source book distillations (rule-card format)
│   ├── brennan-hellenistic-astrology/   # Brennan — planets, signs, houses, lots, timing
│   ├── valens-anthology/                # Valens — foundations through time-lords
│   ├── dorotheus-carmen/                # Dorotheus — births, marriage, natal topics
│   └── firmicus-mathesis/               # Firmicus — planets, houses, combinations
├── rules/                      # Reusable methodology modules
│   ├── stage1-data-extraction.md        # 6-table deterministic data layer
│   ├── reading-workflow.md              # Step 0-7 orchestration
│   ├── planet-condition-audit.md        # Per-planet audit subroutine
│   ├── dignities-reference.md           # Egyptian bounds, Chaldean decans, triplicity
│   ├── aspect-reception-rules.md        # Testimony, aversion, mutual reception
│   ├── chart-finding-index-workflow.md  # v2.3 finding production spec
│   ├── composition-pass.md             # Stage 3B mouthfeel layer
│   ├── delineation-output-rules.md     # Output register + anti-cookbook
│   └── ...                             # 12 more rule modules
├── samples/                    # Quality benchmarks
│   ├── topic-reading-template.md        # v2.2 worked example (historical)
│   └── brief-shot-catalog.md           # Brief-shot quality reference
└── sources/
    └── source-bibliography.md          # 4-source canon
```

## Key design decisions

- **Whole-sign houses only** (WSH). MC degree tracked separately from 10th place.
- **Egyptian bounds** (Brennan appendix), **Chaldean decans**, **Dorothean triplicity by sect**.
- **Evidence-chain**: every finding cites source rows (T1-T6) + rule modules. No unsupported claims.
- **Anti-cookbook**: subject of every life-claim must be a person, event, domain, or felt-state — never a chart factor.
- **Source/reader separation**: `natal-core` produces English technical findings; `render` produces Chinese reader-facing prose. Two layers, never mixed.
- **Unguarded variant**: all ethical guards, euphemisms, and auto-downgrades stripped. Direct relational/event-level statements preferred over abstract structural language.

## Sources

Distilled (paraphrase + rule extraction, no verbatim copying) from:

- Chris Brennan, *Hellenistic Astrology: The Study of Fate and Fortune*
- Vettius Valens, *Anthology* (Riley translation)
- Dorotheus of Sidon, *Carmen Astrologicum* (Pingree via al-Tabari)
- Julius Firmicus Maternus, *Mathesis* (Bram translation)

## License

No license specified. Source extractions are paraphrased rule distillations with page-number citations, not reproductions of copyrighted text.
