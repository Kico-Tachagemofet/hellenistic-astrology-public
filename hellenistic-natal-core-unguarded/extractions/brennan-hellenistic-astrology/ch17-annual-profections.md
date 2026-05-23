# Brennan Extraction — Chapter 17 Annual Profections

Source: Chris Brennan, `Hellenistic Astrology: The Study of Fate and Fortune`, Chapter 17.

Scope:

- time-lord techniques;
- annual profections;
- activation of places;
- lord of the year;
- activation of the place containing the ruler;
- repetitions and transits;
- advanced method in Valens.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Chapter Range

- Printed pp. 535-552.
- Approx. PDF pp. 562-579.

## Method Takeaway

Annual profections are a simple but powerful timing filter. They do not invent events from nothing. They activate a natal place, its ruler, planets in that place, and related natal promises.

For skill purposes:

```text
Natal chart = promise / structure.
Annual profection = which place and ruler are activated this year.
Transits = triggers and repetitions that help time concrete manifestations.
```

## Rule Card 17.1 — Annual Place Activation

Source: Ch. 17, annual profections and activation of places, printed pp. 536-542; PDF pp. 563-569.

Use when:

- user asks about a year, age, or current life period;
- timing a natal topic without using a heavier technique first;
- filtering which houses are currently emphasized.

Required chart data:

- Ascendant sign;
- native's age for the solar year being judged;
- whole sign houses;
- ruler of activated place;
- planets in activated place.

Procedure:

1. Start counting from the rising sign as year 0 / first year of life.
2. Advance one sign/place per year.
3. Reduce age modulo 12 to identify activated place.
4. Mark the activated place's topics as foreground for that year.
5. Identify planets in the activated place as activated tenants.
6. Identify the ruler of the activated place as lord of the year.

Output:

```text
Age/year:
Activated place:
Activated topics:
Planets in activated place:
Lord of the year:
Initial timing hypothesis:
```

Guardrail:

Do not predict an event solely because the house is activated. Activation means the topic becomes available, foregrounded, or sensitive.

Destination rule file:

- `rules/timing-techniques.md`

## Rule Card 17.2 — Lord Of The Year Determines Quality

Source: Ch. 17, condition of lord of the year, printed pp. 543-544; PDF pp. 570-571.

Use when:

- judging whether the year is easier, harder, productive, blocked, hidden, or volatile.

Required chart data:

- lord of the year;
- natal condition of lord;
- current/transiting condition if available;
- place occupied by lord;
- aspects/testimony to lord.

Procedure:

1. Identify lord of the activated place.
2. Audit the lord natally using `planet-condition-audit.md`.
3. Read the lord's natal house placement as a second activated field.
4. Check benefic/malefic testimony to the lord.
5. If transit data is available, check transits to and from the lord.
6. Judge year quality by the lord's condition and topic links.

Guardrail:

The lord of the year is not automatically good or bad. Its condition and role decide how the activated place manifests.

Destination rule file:

- `rules/timing-techniques.md`
- `rules/planet-condition-audit.md`

## Rule Card 17.3 — Place Containing The Lord Is Also Activated

Source: Ch. 17, activation of the place containing the ruler, printed p. 544; PDF p. 571.

Use when:

- the annual lord is placed in another house;
- creating the year's topic flow.

Procedure:

1. Identify activated profection place `P`.
2. Identify lord `L` of P.
3. Identify house `H` where L is placed.
4. Read the year as `P -> L -> H`.
5. Combine the topics of P and H through the condition of L.

Output:

```text
Annual source place:
Lord of year:
Lord's natal place:
Annual topic flow:
```

Destination rule file:

- `rules/timing-techniques.md`
- `rules/house-topic-framework.md`

## Rule Card 17.4 — Repetition And Transit Filtering

Source: Ch. 17, repetitions and transits, printed pp. 545-548; PDF pp. 572-575.

Use when:

- narrowing a broad yearly activation into concrete events;
- deciding which transits matter.

Procedure:

1. Identify the profected place and lord of the year.
2. Look for repetitions of natal themes involving that place/lord.
3. Prioritize transits involving:
   - lord of the year;
   - activated place;
   - planets in activated place;
   - Ascendant ruler;
   - relevant topic ruler;
   - Fortune/Spirit if the topic requires it.
4. Treat unrelated transits as lower priority.
5. Use transits as triggers, not standalone event makers.

Guardrail:

Do not read every transit equally. Annual profection filters the transit field.

Destination rule file:

- `rules/timing-techniques.md`

## Rule Card 17.5 — Advanced Valens Method: Tenants And Ruler Both Matter

Source: Ch. 17, advanced method of profections in Valens, printed pp. 549-552; PDF pp. 576-579.

Use when:

- a profected sign contains planets;
- deciding whether to emphasize the ruler, the tenants, or both.

Procedure:

1. Mark planets in the profected place as activated.
2. Mark the ruler of the profected place as activated.
3. Judge both the tenants and the ruler rather than forcing a single exclusive time lord.
4. If tenants and ruler give conflicting testimony, report the mixed year structure.

Guardrail:

Do not ignore planets in the activated place. They can describe concrete themes or events of the year alongside the lord.

Destination rule file:

- `rules/timing-techniques.md`

## Open Questions

- Need a simple age-to-place table in the final skill.
- Need decide whether the skill computes profection year from birthday-to-birthday or accepts user-provided solar year.
- Need later integrate solar revolutions, but not in first pass.
- Need check whether `lord of year` should include bounds/term ruler in later medieval layers; not for current Hellenistic first pass.
