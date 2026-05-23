# Dignities Reference

Purpose: deterministic lookup tables for essential dignity and degree-level sign subdivisions.

Source status: `[Brennan Ch.8]`, using the standard Hellenistic/Dorothean triplicity scheme, Egyptian bounds, and Chaldean-order decans described in Chapter 8.

Copyright note: this file stores distilled lookup data and procedural notes. It does not reproduce long source passages.

## Data Conventions

- Degree intervals are half-open: `[0,6)` means 0 degrees 00 minutes through 5 degrees 59 minutes 59 seconds; 6 degrees 00 minutes enters the next interval.
- Do not calculate bounds or decans from rounded, missing, or sign-only placements.
- Whole-sign dignities apply by sign; exaltation degrees are recorded but should only be used in techniques that explicitly call for them.
- Dignity is evidence of capacity, authority, support, or debility. It is not final judgment.

## Domicile Rulers By Sign

Source: `[Brennan Ch.8]`, domicile rulership, printed pp. 228-241.

| Sign | Domicile ruler |
|---|---|
| Aries | Mars |
| Taurus | Venus |
| Gemini | Mercury |
| Cancer | Moon |
| Leo | Sun |
| Virgo | Mercury |
| Libra | Venus |
| Scorpio | Mars |
| Sagittarius | Jupiter |
| Capricorn | Saturn |
| Aquarius | Saturn |
| Pisces | Jupiter |

## Planetary Dignity And Debility By Planet

Source: `[Brennan Ch.8]`, exaltations/depressions and adversities, printed pp. 242-252.

| Planet | Domicile(s) | Adversity / exile opposite domicile | Exaltation | Depression / fall | Exaltation degree |
|---|---|---|---|---|---|
| Sun | Leo | Aquarius | Aries | Libra | 19 Aries |
| Moon | Cancer | Capricorn | Taurus | Scorpio | 3 Taurus |
| Mercury | Gemini, Virgo | Sagittarius, Pisces | Virgo | Pisces | 15 Virgo |
| Venus | Taurus, Libra | Scorpio, Aries | Pisces | Virgo | 27 Pisces |
| Mars | Aries, Scorpio | Libra, Taurus | Capricorn | Cancer | 28 Capricorn |
| Jupiter | Sagittarius, Pisces | Gemini, Virgo | Cancer | Capricorn | 15 Cancer |
| Saturn | Capricorn, Aquarius | Cancer, Leo | Libra | Aries | 21 Libra |

Notes:

- Brennan uses "depression" for what later tradition often calls fall.
- Brennan suggests "adversity," "debility," or "exile" for the sign opposite domicile; "detriment" can be kept for compatibility but should not imply an unexamined later scoring system.
- Exaltation degree variants exist in the textual tradition; use the standard Valens set above unless a source-specific technique requires a variant.

## Triplicity Rulers By Sect

Source: `[Brennan Ch.8]`, standard triplicity rulership scheme, printed pp. 267-268.

Use this Dorothean scheme by default.

| Triplicity | Signs | Day primary | Day secondary | Night primary | Night secondary | Cooperating ruler |
|---|---|---|---|---|---|---|
| Fire | Aries, Leo, Sagittarius | Sun | Jupiter | Jupiter | Sun | Saturn |
| Earth | Taurus, Virgo, Capricorn | Venus | Moon | Moon | Venus | Mars |
| Air | Gemini, Libra, Aquarius | Saturn | Mercury | Mercury | Saturn | Jupiter |
| Water | Cancer, Scorpio, Pisces | Venus | Mars | Mars | Venus | Moon |

Notes:

- The primary and secondary rulers swap by sect; the cooperating ruler stays the same.
- Dorotheus mentions Mercury in relation to the earth triplicity, and Valens treats Mercury as common/assisting. Do not use Mercury as a base earth triplicity ruler in this project unless the specific technique says so; mark such use `needs verification`.
- Ptolemy's alternative triplicity scheme is not the project default.

## Egyptian Bounds

Source: `[Brennan Ch.8]`, Egyptian bounds, printed pp. 275-279; Table 8.3.

| Sign | Bound 1 | Bound 2 | Bound 3 | Bound 4 | Bound 5 |
|---|---|---|---|---|---|
| Aries | [0,6) Jupiter | [6,12) Venus | [12,20) Mercury | [20,25) Mars | [25,30) Saturn |
| Taurus | [0,8) Venus | [8,14) Mercury | [14,22) Jupiter | [22,27) Saturn | [27,30) Mars |
| Gemini | [0,6) Mercury | [6,12) Jupiter | [12,17) Venus | [17,24) Mars | [24,30) Saturn |
| Cancer | [0,7) Mars | [7,13) Venus | [13,19) Mercury | [19,26) Jupiter | [26,30) Saturn |
| Leo | [0,6) Jupiter | [6,11) Venus | [11,18) Saturn | [18,24) Mercury | [24,30) Mars |
| Virgo | [0,7) Mercury | [7,17) Venus | [17,21) Jupiter | [21,28) Mars | [28,30) Saturn |
| Libra | [0,6) Saturn | [6,14) Mercury | [14,21) Jupiter | [21,28) Venus | [28,30) Mars |
| Scorpio | [0,7) Mars | [7,11) Venus | [11,19) Mercury | [19,24) Jupiter | [24,30) Saturn |
| Sagittarius | [0,12) Jupiter | [12,17) Venus | [17,21) Mercury | [21,26) Saturn | [26,30) Mars |
| Capricorn | [0,7) Mercury | [7,14) Jupiter | [14,22) Venus | [22,26) Saturn | [26,30) Mars |
| Aquarius | [0,7) Mercury | [7,13) Venus | [13,20) Jupiter | [20,25) Mars | [25,30) Saturn |
| Pisces | [0,12) Venus | [12,16) Jupiter | [16,19) Mercury | [19,28) Mars | [28,30) Saturn |

Notes:

- Egyptian bounds use only Mercury, Venus, Mars, Jupiter, and Saturn as bound rulers.
- Use bound ruler condition as secondary evidence in planet condition audit.
- Do not substitute Ptolemy's bounds unless the reading explicitly requests that variant.

## Decans / Faces

Source: `[Brennan Ch.8]`, decans or faces, printed pp. 279-283.

Use the Chaldean-order decan scheme described in Chapter 8.

| Sign | [0,10) | [10,20) | [20,30) |
|---|---|---|---|
| Aries | Mars | Sun | Venus |
| Taurus | Mercury | Moon | Saturn |
| Gemini | Jupiter | Mars | Sun |
| Cancer | Venus | Mercury | Moon |
| Leo | Saturn | Jupiter | Mars |
| Virgo | Sun | Venus | Mercury |
| Libra | Moon | Saturn | Jupiter |
| Scorpio | Mars | Sun | Venus |
| Sagittarius | Mercury | Moon | Saturn |
| Capricorn | Jupiter | Mars | Sun |
| Aquarius | Venus | Mercury | Moon |
| Pisces | Saturn | Jupiter | Mars |

Notes:

- Treat decans/faces as low-weight modifiers in the first natal core.
- Do not confuse this decan/face table with the separate doctrine of proper face.

## Condition Audit Integration

Use this order inside `planet-condition-audit.md`:

1. Check domicile and adversity/exile by sign.
2. Check exaltation and depression/fall by sign.
3. Check triplicity dignity according to chart sect.
4. If exact degree is known, check Egyptian bound ruler.
5. If exact degree is known, check decan ruler.
6. Judge dignity evidence with sect, house, visibility, motion, reception, and benefic/malefic testimony.

Output field:

```text
Essential dignity:
- domicile/adversity:
- exaltation/fall:
- triplicity:
- bound:
- decan:
- dignity note:
```

Guardrail:

Do not convert these tables into a simple point score unless the scoring method is separately sourced and marked.
