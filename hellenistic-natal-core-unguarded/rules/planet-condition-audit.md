# Planet Condition Audit

Purpose: determine whether a planet can do what it signifies before using it as evidence.

A planet is judged through three layers:

1. Intrinsic/natural role: what kind of thing this planet signifies.
2. Internal condition: sect, dignity, house, visibility, speed, motion.
3. External testimony: benefic/malefic support or harm, reception, enclosure, overcoming, and close application.

Natural keywords are never enough.

## Audit Order

1. Role in this reading
2. Sect
3. Essential dignity
4. House placement and angularity
5. Visibility and solar condition
6. Speed, station, retrogradation
7. Benefic/malefic testimony
8. Reception and mitigation
9. Role in the current timing period, if any

## Layer 1: Role In The Reading

| Role | Meaning |
|---|---|
| Primary significator | main actor/body of the reading |
| Topic ruler | carries a house topic elsewhere |
| Natural significator | symbolic witness for a topic |
| Tenant | planet located inside a topic house |
| Time lord | temporarily activated planet |
| Witness | planet testifying to another planet/topic |

A planet may hold several roles. List them before judging.

## Layer 2: Internal Condition

| Layer | Question | Output |
|---|---|---|
| Sect | Is the planet of the sect in favor or contrary to sect? | supported / contrary / mixed / undeclared |
| Essential dignity | Does it have authority, support, or debility in its sign/degree? | domicile/exaltation/triplicity/bounds/decan/none/adversity/fall |
| Accidental strength | Can it act visibly and effectively? | angular/succedent/cadent; pivot relationship |
| Visibility | Is it hidden, under beams, combust, or emerging? | visible / under beams / combust / heliacal nuance |
| Motion | Is it moving normally? | direct / retrograde / stationing / slow / fast |

## Sect Notes

- Day chart: Sun, Jupiter, Saturn are of the sect; Moon, Venus, Mars are contrary to sect; Mercury is contextual.
- Night chart: Moon, Venus, Mars are of the sect; Sun, Jupiter, Saturn are contrary to sect; Mercury is contextual.
- Mercury default v1 rule: if Mercury is a visible morning star, rising before the Sun, treat it as joining the diurnal sect; if Mercury is a visible evening star, setting after the Sun, treat it as joining the nocturnal sect. Source: `[Brennan Ch.7]`, printed pp. 190-191 and morning/evening definitions on pp. 205-206.
- To classify Mercury as morning/evening, it must be far enough from the Sun to be visible, not merely earlier/later by zodiacal order. Brennan cites the same fifteen-degree solar-visibility boundary for proper morning/evening rising. Source: `[Brennan Ch.7]`, printed pp. 205-206.
- Brennan notes alternative Mercury sect rules in Valens and the Michigan Papyrus. Use the morning/evening rule as the project default; if a source-specific variant is requested, mark the variant explicitly.
- If Mercury does not meet the visibility boundary for the morning/evening default rule, or if any planet's sect status cannot be determined from available data, output `undeclared` rather than forcing supported/contrary/mixed. `[project heuristic]`
- Sect agreement is a primary condition. Secondary sect conditions should not override the basic day/night assignment.
- Benefics and malefics change expression by sect: a sect-supported malefic can be more constructive; a contrary-to-sect malefic is more likely to damage.

## Essential Dignity Notes

Use `rules/dignities-reference.md` as the deterministic lookup table for:

- domicile rulers;
- adversity/exile opposite domicile;
- exaltation and depression/fall;
- Dorothean triplicity rulers by sect;
- Egyptian bounds;
- Chaldean-order decans/faces.

Audit sequence:

1. Check sign-level dignity: domicile, adversity/exile, exaltation, depression/fall.
2. Check triplicity support according to chart sect.
3. If exact degree is known, check Egyptian bound ruler.
4. If exact degree is known, check decan ruler.
5. Judge dignity evidence with the planet's role, sect, house, visibility, motion, and external testimony.

Guardrails:

- Do not calculate bounds or decans from rounded or missing degree data.
- If software-supplied dignity labels conflict with `dignities-reference.md`, use `dignities-reference.md` as the project canonical value and log the discrepancy under `data_contract.md` Conflict Handling. `[project heuristic]`
- Treat decans/faces as low-weight modifiers unless a technique explicitly foregrounds them.
- Do not use a simple dignity point score unless the scoring method is separately sourced and marked.

## Visibility Notes

- Solar visibility thresholds from `[Brennan Ch.7]`:

| Condition | Distance from Sun | Use |
|---|---:|---|
| Under the beams | within 15 degrees | hidden, obscured, weakened, private, delayed, or obstructed; printed p. 200 |
| Close/severe under the beams, v1 combust bucket | within 9 degrees | stronger impairment; Brennan cites Paulus saying under-beams planets are especially weakened within nine degrees; printed p. 201 |
| In the heart of the Sun / cazimi | within 1 degree | possible amelioration or protection in Rhetorius; printed pp. 204-205 |

- Terminology note: Brennan's Ch. 7 discussion frames the 15-degree range as under the beams and the 9-degree range as a more severe subrange. `combust` is the project's v1 operational label for that 9-degree severe solar condition; if strict historical terminology matters, write "close/severe under the beams" instead.
- Later medieval authors narrowed cazimi to 16 minutes, but v1 uses the one-degree Hellenistic/Rhetorius threshold unless a later source track is explicitly invoked.
- Dignity, sect support, and benefic testimony can mitigate visibility problems.
- Do not call a planet useless solely because it is under the beams.

## Auditing Non-Planet Significators

[project heuristic]

For Ascendant, MC, Lots, and other zodiacal points, do not force a planet-only condition audit onto the point itself.

Use two linked checks instead:

1. Audit the point's domicile ruler or technique-specific ruler with this file.
2. Audit testimony to the point's degree or sign with `aspect-reception-rules.md`.

Record the result as the point's condition proxy. Example output:

```text
Point:
Ruler audit:
Testimony to point:
Condition proxy:
Confidence:
```

## Motion Notes

- Stationing planets are emphasized or at a turning point.
- Retrograde planets require topic-specific interpretation: reversal, return, complication, internalization, delay, or unusual route.
- Motion modifies execution; it does not replace the rest of the audit.

## Layer 3: External Testimony

| Testimony | Working meaning |
|---|---|
| Bonification | benefic testimony improves, protects, opens, or supports the planet/topic |
| Maltreatment | malefic testimony harms, constrains, cuts, delays, burdens, or destabilizes the planet/topic |
| Mixed testimony | both benefic and malefic testimony are present; describe both |
| Reception | host dignity relationship can mitigate harm or strengthen support |
| Overcoming | superior-position testimony acts more forcefully and directionally |
| Enclosure | containment by benefics or malefics; protection or trapping |
| Counteraction | indirect harm through a badly placed malefic ruler |

## Net Judgment Template

```text
Planet:
Role in this reading:
Internal capacity:
External support:
External pressure:
Mitigation/reception:
Net judgment:
Confidence:
```

## Guardrails

- Never use a planet's natural keyword alone.
- Do not flatten difficult condition into doom; identify mitigation and constructive channels.
- Do not beautify damage without evidence.
- Separate capacity from outcome: a strong planet can do difficult things effectively; a weak benefic may want to help but fail to deliver.

## Source Status

Expanded from Brennan chapters 7, 8, and 14, with support from chapters 12-13. Ch. 7 now supplies the default Mercury morning/evening sect rule and solar visibility thresholds. Essential dignity lookup lives in `dignities-reference.md`. Non-planet significator audit proxy is `[project heuristic]`. Needs cross-check against Demetra George Vol. I before final locking.
