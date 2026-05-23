# Brennan Extraction — Chapter 7 Planets

Source: Chris Brennan, `Hellenistic Astrology: The Study of Fate and Fortune`, Chapter 7.

Scope:

- natural significations of the seven traditional planets;
- benefic/malefic classification;
- sect;
- under the beams and visibility;
- morning/evening phase;
- speed, retrogradation, and stations;
- lunar nodes as a cautionary extension.

Copyright note: this file paraphrases method and stores page references. It does not reproduce long passages.

## Chapter Range

- Printed pp. 165-211.
- Approx. PDF pp. 192-238.

## Method Takeaway

Chapter 7 should not be used as a simple keyword list. Its main skill value is that planets have a natural symbolic range, but the chart's sect, visibility, speed, and benefic/malefic testimony decide how that range expresses.

For the future skill, the rule is:

```text
Natural meaning is only the raw material.
Planet condition decides expression quality.
Topic role decides where the meaning is applied.
```

## Rule Card 7.1 — Natural Signification Is Not Final Judgment

Source: Ch. 7, significations section, printed pp. 167-184; PDF pp. 194-211.

Use when:

- assigning natural significators to topics;
- explaining why a planet is relevant before judging whether it is helpful or difficult.

Required chart data:

- planet involved;
- chart focus;
- whether the planet is acting as natural significator, house ruler, tenant, time lord, or witness.

Procedure:

1. Identify the planet's natural symbolic domain.
2. Identify its role in this specific reading.
3. Do not infer outcome from the natural domain alone.
4. Run condition audit before converting symbol into judgment.
5. Tie the planet back to the topic house, ruler-chain, Lot, or time-lord activation.

Guardrail:

A planet keyword without topic role and condition is not evidence. It is only vocabulary.

Destination rule file:

- `rules/planet-condition-audit.md`
- `rules/significator-hierarchy.md`

## Rule Card 7.2 — Benefics And Malefics As Quality Modifiers

Source: Ch. 7, benefics and malefics section, printed pp. 184-190; PDF pp. 211-217.

Use when:

- deciding whether an event or topic is supported, denied, intensified, softened, damaged, or made costly;
- weighting testimony to a significator.

Required chart data:

- Jupiter/Venus condition;
- Mars/Saturn condition;
- Mercury role and condition;
- aspects or configurations between benefics/malefics and the topic significator;
- sect.

Procedure:

1. Identify benefic testimony: Jupiter/Venus helping, affirming, smoothing, increasing, or protecting.
2. Identify malefic testimony: Mars/Saturn cutting, delaying, constraining, separating, damaging, or making difficult.
3. Modify testimony by sect: benefic/malefic expression changes depending on whether planet and chart sect agree.
4. Treat Mercury as mixed and dependent on condition, association, and role.
5. Use this layer as quality modification, not as the whole judgment.

Supporting evidence:

- benefic configured to the significator;
- benefic of the sect in favor supporting a relevant place or ruler;
- malefic of the sect in a constructive role with mitigation.

Constraining evidence:

- malefic contrary to sect dominating or striking the significator;
- benefic contrary to sect or weakened, unable to help;
- Mercury tied to a difficult witness or mixed condition.

Destination rule file:

- `rules/planet-condition-audit.md`
- `rules/aspect-reception-rules.md`

## Rule Card 7.3 — Sect Is A Primary Condition, Not Decoration

Source: Ch. 7, sect section, printed pp. 190-197; PDF pp. 217-224.

Use when:

- judging any planet's condition;
- deciding the constructive/destructive expression of benefics and malefics;
- evaluating sect light and chart coherence.

Required chart data:

- whether Sun is above or below horizon;
- sect light: Sun for day, Moon for night;
- planetary sect membership;
- planets' hemisphere placement when using sect rejoicing as a secondary condition.

Procedure:

1. Determine day chart or night chart.
2. Mark sect light.
3. Mark each planet as of the sect, contrary to sect, or neutral/mixed.
4. Prioritize sect agreement before weaker secondary sect conditions.
5. Modify benefic/malefic judgment by sect.

Working rules:

- Day chart: Sun, Jupiter, Saturn are in sect; Moon, Venus, Mars are contrary; Mercury is contextual.
- Night chart: Moon, Venus, Mars are in sect; Sun, Jupiter, Saturn are contrary; Mercury is contextual.
- Default Mercury rule: Mercury joins the diurnal sect when it is a morning star rising before the Sun, and the nocturnal sect when it is an evening star setting after the Sun. Source: Ch. 7, printed pp. 190-191; PDF pp. 217-218.
- Morning/evening classification requires visibility: a planet must be more than fifteen degrees from the Sun to be properly called a morning or evening riser. Source: Ch. 7, printed pp. 205-206; PDF pp. 232-233.
- Brennan records alternative rules for Mercury in Valens and the Michigan Papyrus; the project default is the Ptolemy/Porphyry morning/evening rule unless a source-specific variant is requested.
- A planet in sect tends to express more constructively or appropriately.
- A planet contrary to sect tends to express with more imbalance or difficulty, especially malefics.

Guardrail:

Do not treat all sect subconditions as equal. The first gate is whether the chart itself is day or night and whether the planet belongs to that sect.

Destination rule file:

- `rules/planet-condition-audit.md`

## Rule Card 7.4 — Solar Visibility And Under The Beams

Source: Ch. 7, under the beams section, printed pp. 200-205; PDF pp. 227-232.

Use when:

- judging whether a planet can act openly and effectively;
- explaining hiddenness, obstruction, lack of visibility, or private/internal expression.

Required chart data:

- planet's distance from the Sun;
- whether the planet is applying toward or separating from the Sun;
- planet dignity and mitigating factors;
- morning/evening phase if available.

Procedure:

1. Check if the planet is close enough to the Sun to be hidden or impaired.
2. Distinguish moving into solar obscuration from emerging out of it when data supports it.
3. Check whether dignity or other mitigating conditions reduce the harm.
4. Avoid absolute claims if exact heliacal phase is unknown.

Working thresholds:

- Under the beams: within 15 degrees of the Sun. Source: Ch. 7, printed p. 200; PDF p. 227.
- Close/severe under the beams, used by v1 as the combust bucket: within 9 degrees of the Sun. Brennan cites Paulus that the impairment is especially strong inside this range. Source: Ch. 7, printed p. 201; PDF p. 228.
- In the heart of the Sun / cazimi: within 1 degree of the Sun in Rhetorius; later medieval sources narrow this to 16 minutes, but that is not the v1 default. Source: Ch. 7, printed pp. 204-205; PDF pp. 231-232.

Terminology note:

Ch. 7 does not foreground the later English label "combust" for the 9-degree bucket. For strict Hellenistic wording, call it close/severe under the beams; for v1 operational output, `combust` means the 9-degree severe solar condition above.

Output language:

- hidden, obscured, private, weakened, delayed, obstructed, emerging, recovering.

Guardrail:

Do not equate under beams with total uselessness. It is a visibility and condition problem that must be weighed with dignity, sect, and testimony.

Destination rule file:

- `rules/planet-condition-audit.md`

## Rule Card 7.5 — Motion, Speed, Retrogradation, Stations

Source: Ch. 7, speed/retrograde/stations section, printed pp. 206-208; PDF pp. 233-235.

Use when:

- judging execution speed, instability, reversal, delay, intensification, or turning points.

Required chart data:

- direct/retrograde state;
- speed compared to norm if available;
- station proximity if available;
- applying/separating relationships.

Procedure:

1. Record direct, retrograde, or stationing status.
2. Treat stationing planets as especially emphasized or in transition.
3. Treat retrogradation as a condition requiring interpretation by topic and role, not automatic failure.
4. Combine with house, sect, dignity, and aspect condition.

Destination rule file:

- `rules/planet-condition-audit.md`

## Rule Card 7.6 — Nodes Are Cautionary, Not First-Pass Core

Source: Ch. 7, nodes section, printed pp. 208-211; PDF pp. 235-238.

Use when:

- chart has important planetary conjunctions with nodes;
- eclipses or nodal themes are central;
- later source tracks support nodal use.

Procedure:

1. Record nodal conjunctions and proximity.
2. Do not let nodes outrank the seven visible planets in the first natal core.
3. Mark node interpretation as an extension layer until the rule base is thicker.

Destination rule file:

- future `rules/nodes-and-eclipses.md` or extension section.

## Open Questions

- Need Demetra George cross-check for the exact condition hierarchy and terminology.
- Mercury sect has a v1 default from Brennan Ch. 7: morning star = diurnal, evening star = nocturnal. Later source-specific variants still need comparison before variant mode.
- Need a data field for heliacal phase, but first version may only support under-beams/combust distance.
