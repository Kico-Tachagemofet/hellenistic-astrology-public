# Timing Techniques

> **v2.4 canonical-tool mandate (2026-05-18)**: All numerical computation for profections / ZR Fortune / ZR Spirit / LB pivots / chapter-end dates / Hyleg-Alcocoden bound-lord assignments goes through **`tools/swe_timing.py`** (Swiss Ephemeris + Hellenistic Egyptian-year canonical: 360 d / 30 d-month per Valens / Brennan Ch.18). Cross-validated against astro-seek archive to arc-second / day-level precision (case-09 verification 2026-05-18). **Do NOT hand-estimate ZR chapter lengths from sign-year mapping by memory or mental arithmetic** — this is the bug class that produced the case-09 17→27 yr error and propagated through 34 files before catch. See `rules/stage1-data-extraction.md` Step 9.6 for tool invocation spec; this file (`timing-techniques.md`) covers Hellenistic doctrine + reading discipline only, not numerical computation.

Purpose: add time activation without inventing events beyond the natal chart.

First-pass timing technique: annual profections.

Advanced timing technique: zodiacal releasing, added as a guarded advanced layer after annual profections.

## Core Principle

```text
Natal chart = promise and structure.
Time lord = activated part of the natal promise.
Transits = triggers and repetitions.
```

Do not use timing techniques to create topics unsupported by the natal chart.

## Annual Profections

Annual profections move one whole sign place per year from the Ascendant.

```text
Age 0 = 1st place
Age 1 = 2nd place
Age 2 = 3rd place
...
Age 11 = 12th place
Age 12 = 1st place again
```

Use age modulo 12 to identify the activated place.

## Annual Profection Procedure

1. Confirm birth time and Ascendant are reliable.
2. Determine native's age for the solar year being judged.
3. Count one whole sign place per year from the Ascendant.
4. Identify activated place and its topics.
5. Identify planets in the activated place.
6. Identify lord of the year: domicile ruler of activated place.
7. Audit lord of the year natally.
8. Identify the natal place occupied by lord of the year.
9. Build annual topic flow: `activated place -> lord -> lord's place`.
10. Filter transits through activated place, lord, tenants, and relevant topic rulers.

## Annual Output Template

```text
Year / age:
Activated place:
Activated topics:
Planets in activated place:
Lord of the year:
Lord's natal condition:
Lord's natal place:
Annual topic flow:
Relevant transits/repetitions:
Supporting evidence:
Constraining evidence:
Year judgment:
Confidence:
```

## Lord Of The Year

The lord of the year determines much of the quality of the year.

Judge:

- sect status;
- dignity;
- house placement;
- visibility;
- motion;
- benefic/malefic testimony;
- reception;
- relation to current topic.

If the lord is strong, supported, and connected to the activated topic, the year is more capable of constructive manifestation.

If the lord is damaged, hidden, contrary to sect, maltreated, or in a difficult place without mitigation, the year may still be important but with pressure, delay, loss, or constraint.

## Activated Tenants

Planets in the activated place are also activated.

Read both:

```text
Activated place tenant planets
+
Lord of the year
```

If they agree, the yearly theme is reinforced.
If they conflict, preserve the mixed testimony.

## Transit Filtering

Annual profections filter which transits matter most.

Prioritize transits to/from:

- lord of the year;
- activated place;
- planets in activated place;
- Ascendant ruler;
- topic ruler for user's question;
- Fortune/Spirit when the topic or technique uses Lots.

Do not treat every transit as equally important.

## Guardrails

- Annual activation foregrounds topics; it does not guarantee a specific event.
- Do not ignore natal promise.
- Do not ignore the condition of lord of the year.
- Do not use profections without reliable Ascendant.
- Use whole sign places for profection counting.

## Source Status

Initial skeleton distilled from Brennan Chapter 17. Needs Chapter 18 zodiacal releasing and future solar revolution rules before advanced timing skill draft.

---

## Zodiacal Releasing

Zodiacal Releasing is an advanced time-lord technique based on Lots, especially Spirit and Fortune.

Use only when:

- birth time is reliable;
- Fortune and Spirit are known;
- period tables are calculated or supplied;
- the question genuinely needs life chapter timing.

## Releasing Anchor

| Releasing from | Use for |
|---|---|
| Spirit | action, career, intention, life direction, praxis |
| Fortune | body, circumstance, health, material events, things that befall the native |

Do not mix Spirit and Fortune without explaining why.

## Zodiacal Releasing Procedure

1. Define timing question.
2. Choose releasing Lot: Spirit or Fortune.
3. Generate or receive period table.
4. Identify active L1 and L2 signs.
5. Identify rulers of active signs.
6. Audit rulers natally.
7. Check planets in active signs.
8. Check active signs relative to Fortune and its angular triads.
9. Mark peak periods and Loosing of the Bond if present.
10. Cross-check with annual profections and transits before concrete event claims.

## Period Output Template

```text
Question/topic:
Releasing Lot:
Active L1:
Active L2:
Period ruler(s):
Prominence / peak status:
Loosing of the Bond:
Ruler condition:
Benefic/malefic testimony:
Annual profection cross-check:
Transit trigger cross-check:
Judgment:
Confidence:
```

## Peak Periods

Peak periods indicate prominence, salience, or visibility. They are not automatically good.

Judge quality through:

- ruler condition;
- benefic/malefic testimony;
- relation to Ascendant, MC, Fortune, Spirit;
- annual profection and transit repetitions.

## Loosing Of The Bond

Loosing of the Bond marks a major turning point, release, reversal, break, or redirection in the topic of the releasing Lot.

It does not describe the event by itself. Use natal promise and other timing triggers to specify content.

## Fortune Angularity Frame

In Zodiacal Releasing, angularity relative to Fortune is its own frame.

Do not confuse:

```text
whole sign houses from Ascendant
with
angular triads relative to Fortune
```

## Guardrails

- **MANDATORY: use `tools/swe_timing.py` for all ZR period-table computation** (v2.4, 2026-05-18). Manual / mental-arithmetic ZR is **prohibited** in production readings. The hand-estimate failure mode: a sign's "minor years" mapping (Cap 27, Aqu 30, etc.) gets silently converted from Egyptian-year (360 d) to solar-year (365.2425 d) when the analyst translates "27 years" into "ends around 2042" by mental arithmetic — drift is ~5% / ~6 months per chapter from astro-seek canonical, compounding to multi-year errors over L1. Case-09 retro 2026-05-18 caught Cap L1 modeled as 17 yr when canonical is 27 Eg yr.
- Do not use ZR with uncertain birth times.
- Do not make concrete event claims from ZR alone.
- Use ZR to describe chapters and turning points; use profections/transits to help time manifestations.
- **Distinguish chapter end (zodiacal sequence transition) from LB pivot (aversion-to-L1 jump)**: they are two different event classes and may co-occur or fall years apart inside the same L1. The case-09 retro caught a conflation where one PDF-attested LB date was misread as chapter-end and propagated through 34 files.

## Source Status

Initial skeleton distilled from Brennan Chapter 18.

**v2.4 status (2026-05-18)**: deterministic calculator support **RESOLVED** via `tools/swe_timing.py` (Swiss Ephemeris + Egyptian-year canonical). Case validation: case-09 cross-verified against astro-seek archive (arc-second / day-level match on profections + ZR Fortune L1+L2 + ZR Spirit L1+L2). LB rule remains DISABLED in tool pending canonical-source clarification of exact rule mechanics; aversion-to-L1 sign candidates are flagged for cross-reference but LB-target-sign jump is preserved from PDF / astro-seek archive rather than tool-computed.
