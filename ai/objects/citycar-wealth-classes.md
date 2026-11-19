---
status: draft
verified: New ex-15 @ cfd36f1b3
---
# Citycar wealth classes (calibration and coverage)

**Covers**: the passenger-wealth-class calibration for `Obj=citycar` objects — the framework,
the per-model `class=` assignments, and the era coverage check. Field spec:
[citycar](citycar.md). Gaps and the assets needed to fill them:
[citycar-asset-gaps](citycar-asset-gaps.md). Parent: [object-types](../object-types.md).

## The wealth ladder (era-relative ranks)

`[USER-DIRECTION:2026-11-15]` The five classes (0 lowest … 4 highest) are era-relative
social ranks, anchored by the railway defaults: Very low ≈ 4th class, workmen's trains,
excursions, tram fares; Low = 3rd class (the ordinary mass); Medium = 2nd class (the
middling sort); High = 1st class (the prosperous); Very high ≈ beyond ordinary 1st-class
wealth (prestige airliners, Pullman — the latter possibly a calibrational anomaly). The
same rank means the same segment of society in every era; absolute income changes.

| Class | Who | Car implication |
| --- | --- | --- |
| 4 Very high | aristocracy, great industrialists, top fortunes | the most prestigious car money can buy |
| 3 High | gentry, senior professionals, prosperous businessmen | upmarket saloons |
| 2 Medium | clerks, skilled trades, lower middle | the ordinary family car |
| 1 Low | the bulk of working people | the cheapest standard motoring |
| 0 Very low | the poor: casual labourers, lowest paid | the very cheapest available — old bangers, motorcycle and sidecar, or nothing |

## Hard constraint: `New/config/privatecar.tab`

The class pools must be populated wherever `car_ownership[class]` is non-zero, because that
table (indexed by class, 0 lowest) already throttles what share of each class has car
access: Very high is 82% from 1750 and 85–93% later; High reaches 20% by 1920 and 60% by
1950; Medium 21% (1951); Low 5% (1955); Very low 0 before 1945, 2% (1955), 5% (1960).
Marginal access is still access: **keep the pools populated even when the percentage is
small** — frequency is handled by this table and by `citycar_level`, not by the class
lists. `[USER-DIRECTION:2026-11-15]`

## Assignment principles

1. A model lists every class band that plausibly drove it at some point in its road life:
   trim spread at purchase plus downward drift into cheaper hands as it ages (a Ford
   Cortina is Low and Medium for this reason).
2. Genuine cross-class cars list widely (the BMC Mini: 0–3; the Range Rover: 2–4).
3. The cheapest aged models carry band 0 once the class has car access at all — in practice from
   1945, when `privatecar.tab` first gives class 0 a non-zero share. **Before 1945 the Very-low and
   Low classes had no car ownership whatsoever** (`car_ownership[0]` and `[1]` are both zero from
   1750 to 1945, and even in 1935 only Medium at 3% and High at 33% had cars). Pre-war cars
   therefore start at Medium, and the characteristic Very-low vehicle of c. 1920–1965 is the
   **motorcycle and sidecar** — era-specific outfits (BSA 557 combinations, Norton Big Four, BSA M21
   + Watsonian) are listed in [citycar-asset-gaps](citycar-asset-gaps.md) section C1 with classes
   `0,1`. `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-18]`
4. Horse-drawn: private carriages and the park drag are 3–4; the working cart is 0–1.

**Correction, 2026-11-18.** The first calibration put the pre-war cheap cars — Ford T, Austin Seven,
Morris Minor 1928, Ford Model C and Y, Citroën Type C, and the three Edwardian light cars — into
class 0. That contradicted the ownership table, which gives class 0 no car access before 1945. They
are now Medium (2), or Low-and-Medium (1,2) where their road life runs into the 1950s. The pre-war
Very-low pool is the motorcycle outfits, and it is thin because only two pre-war outfits exist
(BSA 557 from 1921 and BSA Sloper from 1930; the Norton Big Four runs 1940–48).

## Assignments (by class list)

Revised 2026-11-18 across the whole fleet of 247 models, applying principles 1–4 above. Forty-one
models changed. The changes were of three kinds:

1. **Prestige cars widened from `4` to `3,4`** where the model genuinely passed into prosperous
   but not plutocratic hands as it aged: the BMW 7-series, Mercedes S-Class and W116, Audi A8,
   Lexus LS400, Jaguar XJ, Daimler TE30 and Vauxhall 30-98. The Rolls-Royce and Bentley models stay
   at `4` alone, on the ground that their running costs kept them out of ordinary use.
2. **Single-band `3` widened** where the car sat across the High boundary: Argyll 15/30, Daimler
   Fifteen, Jaguar 420, Jaguar S-Type, Rover 8, Rover 20, Rover P4 75, Rover Twelve, Rover 12 P2 and
   14 P2, Sunbeam 12/16, Wolseley 16/20 and 6/80, Humber Hawk VI.
3. **Single-band `2` corrected down or across** where the model was a mainstream car rather than an
   executive one: Ford Mondeo Mk1 and Mk4, Peugeot 206 and the Qashqai J10 dropped to `1,2`;
   Leyland Princess widened to `2,3`; the three early light cars (Star 7 hp, De Dion Type V,
   Peugeot Type 69 Bébé) set to `1,2`.

The distribution after revision:

| Class list | Models |
| --- | --- |
| `0,1` | 21 |
| `0,1,2` | 31 |
| `0,1,2,3` | 2 |
| `1,2` | 69 |
| `1,2,3` | 3 |
| `2,3` | 65 |
| `2,3,4` | 4 |
| `3,4` | 37 |
| `4` | 15 |

## Coverage, 1920–2025

Two changes of method from the earlier object-count table:

1. **Generations of one series count once.** The 247 models collapse to **149 series** (Ford Fiesta
   Mk1–Mk7 is one car, BMW 3-series E21–G20 is one car, Triumph 2000 Mk1/Mk2/2500 is one car). A
   series is present in a year if any of its generations is on the road that year.
2. **Each series is counted once in the main figure**, in its *primary band* — the band that bought
   it new, e.g. Medium for a 3-series, Very high for an S-Class, Low for a Fiesta. The figure in
   [square brackets] is what the column would read if every series were counted in every band it
   belongs to. The gap between the two is the cross-class drift the class lists encode.

### What we have

| Year | 0 Very low | 1 Low | 2 Medium | 3 High | 4 Very high |
| --- | --- | --- | --- | --- | --- |
| 1920 | 0 [1] | 1 [4] | 3 [7] | 4 [10] | 10 [10] |
| 1925 | 0 [2] | 2 [7] | 5 [11] | 6 [10] | 8 [8] |
| 1930 | 0 [3] | 3 [7] | 4 [10] | 6 [10] | 10 [10] |
| 1935 | 0 [2] | 2 [8] | 6 [13] | 7 [12] | 11 [11] |
| 1940 | 0 [3] | 2 [9] | 7 [13] | 6 [10] | 9 [9] |
| 1945 | 0 [3] | 2 [8] | 6 [12] | 6 [9] | 8 [8] |
| 1950 | 0 [5] | 4 [11] | 7 [16] | 9 [12] | 7 [7] |
| 1955 | 0 [7] | 6 [11] | 5 [14] | 9 [12] | 9 [9] |
| 1960 | 0 [9] | 8 [10] | 2 [12] | 10 [13] | 8 [8] |
| 1965 | 0 [12] | 11 [15] | 4 [15] | 11 [12] | 6 [6] |
| 1970 | 0 [10] | 9 [15] | 6 [14] | 8 [13] | 9 [9] |
| 1975 | 0 [11] | 11 [21] | 10 [23] | 13 [19] | 10 [10] |
| 1980 | 0 [12] | 12 [25] | 13 [27] | 14 [21] | 11 [11] |
| 1985 | 0 [12] | 12 [31] | 19 [33] | 14 [21] | 11 [11] |
| 1990 | 0 [11] | 11 [27] | 16 [28] | 12 [17] | 8 [8] |
| 1995 | 0 [13] | 13 [30] | 17 [28] | 11 [15] | 7 [7] |
| 2000 | 0 [10] | 10 [28] | 18 [29] | 11 [15] | 6 [6] |
| 2005 | 0 [9] | 9 [21] | 12 [22] | 10 [16] | 9 [9] |
| 2010 | 0 [8] | 8 [21] | 13 [21] | 8 [14] | 9 [9] |
| 2015 | 0 [7] | 7 [20] | 13 [20] | 7 [13] | 7 [7] |
| 2020 | 0 [6] | 6 [16] | 10 [13] | 3 [8] | 6 [6] |
| 2025 | 0 [3] | 3 [12] | 9 [10] | 1 [4] | 3 [3] |




### With the planned queue added

The queue adds sixteen series: Yaris, Prius and Corolla; Renault 15, 17, 19, 21, 25 and Megane;
Citroën DS and CX; an Aston Martin family; and the four pre-1920 light cars.

| Year | 0 Very low | 1 Low | 2 Medium | 3 High | 4 Very high |
| --- | --- | --- | --- | --- | --- |
| 1920 | 0 [3] | 3 [8] | 5 [9] | 4 [10] | 10 [10] |
| 1925 | 0 [4] | 4 [11] | 7 [13] | 6 [10] | 9 [9] |
| 1930 | 0 [3] | 3 [7] | 4 [10] | 6 [10] | 11 [11] |
| 1935 | 0 [2] | 2 [8] | 6 [13] | 7 [12] | 12 [12] |
| 1940 | 0 [3] | 2 [9] | 7 [13] | 6 [10] | 10 [10] |
| 1945 | 0 [3] | 2 [8] | 6 [12] | 6 [9] | 9 [9] |
| 1950 | 0 [5] | 4 [11] | 7 [16] | 9 [12] | 8 [8] |
| 1955 | 0 [7] | 6 [11] | 5 [14] | 9 [13] | 11 [11] |
| 1960 | 0 [9] | 8 [10] | 2 [12] | 10 [14] | 10 [10] |
| 1965 | 0 [12] | 11 [15] | 4 [15] | 11 [13] | 8 [8] |
| 1970 | 0 [10] | 9 [15] | 6 [14] | 8 [14] | 11 [11] |
| 1975 | 0 [11] | 11 [23] | 12 [26] | 14 [21] | 12 [12] |
| 1980 | 0 [12] | 12 [27] | 15 [30] | 15 [22] | 12 [12] |
| 1985 | 0 [12] | 12 [33] | 21 [37] | 16 [23] | 12 [12] |
| 1990 | 0 [11] | 11 [29] | 18 [32] | 14 [19] | 9 [9] |
| 1995 | 0 [13] | 13 [33] | 20 [33] | 13 [17] | 8 [8] |
| 2000 | 0 [11] | 11 [33] | 22 [35] | 13 [17] | 7 [7] |
| 2005 | 0 [10] | 10 [26] | 16 [26] | 10 [16] | 10 [10] |
| 2010 | 0 [9] | 9 [25] | 16 [24] | 8 [14] | 10 [10] |
| 2015 | 0 [8] | 8 [24] | 16 [23] | 7 [13] | 8 [8] |
| 2020 | 0 [7] | 7 [19] | 12 [15] | 3 [8] | 7 [7] |
| 2025 | 0 [4] | 4 [15] | 11 [12] | 1 [4] | 4 [4] |




The table counts *available models*, not spawning. Whether a pool is actually used depends on
`privatecar.tab`: with the pre-war assumption in place, classes 0 and 1 run at 1% from 1940 and 1925
respectively, so the 1920–35 Very-low and Low figures are models with no traffic until those dates.

### What the table shows

- **The main figure counts each series once, in the band that bought it new.** The classes are now
  uniform two-band lists (purchase band plus one below), so the main figure is the purchase market and
  the bracket is what the fleet can actually carry.
- **Very low is a second-hand band by construction, so its main column is near zero.** Every car that
  a Very-low passenger can drive was bought new by someone in a higher band; the bracket is the
  meaningful number there, and it reaches 31 series in 1985.
- **In the 1930s the fleet is concentrated in High and Very high**, because cars were expensive
  relative to manual wages: the price research puts a £185–245 car at about two years of a manual
  wage, above the Medium ceiling of 1.5. That is the price evidence, not a modelling choice.
- **The modern outer bands remain thin** — Very low 3 and Very high 3 by 2025 — while Medium and High
  are served by the generational overlap of the executive cars.
- **High is no longer artificially weak**: the 5-series, E-Class, A6 and XF carry it from the 1970s
  on, and the top luxury saloons sit one band above them, which matches the price research (a 5-series
  at 1.2–1.5× the manual wage against a 7-series above 3×).

- **The main figure uses a convention: each series is counted in the band that bought it new.** For
  the luxury saloons that is Very high, so the 7-series, A8, LS400 and S-Class all sit in the fourth
  column; the `.dat` files still give them `class=3,4`, because the used market and the company-car
  channel put them in High hands later. The bracketed figure is the one to read when judging
  coverage, because it has no such convention in it.
- **High is the weakest band from 1990 onward.** With the top luxury saloons counted in Very high,
  High falls to three series in 1990 and one by 2025 — the Range Rover. The cars that serve it in the
  bracket are the `2,3` executive saloons (5-series, A4, C-Class, XF-class), which are counted in
  Medium in the main figure.
- **Before 1945 the outer bands rest on motorcycles and on very few cars.** Very low is two pre-war
  outfits in 1935 and never more than three series; Low is empty until the Ford Model Y and Model C
  give it two series in 1935. This is correct, not a modelling gap: `privatecar.tab` gives both
  classes zero ownership before 1945.
- **But that same table means the pre-war outfits cannot spawn at all.** Their `.dat` files carry
  `class=0,1`, yet both classes were at 0% until 1945. That has now been changed to a labelled
  gameplay assumption (below), so they spawn from 1925 in Low and 1940 in Very low.
- **The whole 2015–2025 block is thin, in every band.** Once each series is counted once, the recent
  fleet is five to ten series per band, falling to one or two in the outer bands by 2025. The
  pakset's modern coverage rests on the 2005–2015 cohort, most of which is near or past its retire
  date.
- **Medium is the consistently strongest band** once generations are collapsed: six to nineteen
  series in every year from 1920, and the largest column throughout the middle of the century.

## Provenance

Assignments calibrated 2026-11-15 from two Exa research runs (luxury and entry-level
segments, UK, 1920–2025 at 5-year points; per-model figures and sources in
[citycar-asset-gaps](citycar-asset-gaps.md)) and from the class anchors above.

Revised 2026-11-18 across the full 247-model fleet, adding the BMW, Datsun/Nissan, Toyota Prius,
Triumph and earlier private-car work: 41 models changed and 170 `class=` lines rewritten in the
`.dat` files. The coverage table was generated from each model's `.dat` intro and retire dates and
from the planned queue.

Compiled with the ex-15 makeobj (`class` key, node version 0x8004)
`[CODE simutrans-extended ex-15 @ 6bda048cf]`, 1,018 objects, zero ignored warnings.

## How a class list is calibrated (decision 2026-11-18)

`[USER-DIRECTION:2026-11-18]` A model is eligible for a band if a person in that band could
plausibly afford the car **new, or as a second purchaser at about five years old**. In practice
that bounds almost every list to the purchase band and the one below it, and it removes the deeper
drift bands that some models carried (`0,1,2,3` on the Mini, `2,3,4` on the Range Rover).

The mechanism is the **colourway ladder**: every colourway is a separate object with its own intro,
retire and `class=`, so a colour introduced about five years after launch can carry the wider list
while the launch colours carry the purchase band only. This works where such a colourway exists —
**23 of 255 models have one introduced at least five years after the first** — and where none
exists the wider list simply runs from launch. That is an accepted approximation, not a modelling
error.

**Rejected alternative: explicit second-hand objects.** Duplicating each model with a later intro
and a lower class would be exact in timing and cheap in objects, since the sprites could be reused.
It was rejected because a second-hand object is invisible: the sprite is identical, so a Medium
passenger in a 5-series cannot be distinguished from a High one, and the pakset loses the visual
signal that a distinct model is supposed to give. The player reads wealth from the *shape* on the
road.

**What carries the visual signal instead** is generation overlap. In 2005 the road holds E34s,
E39s and E60s; the older silhouette is the cheaper journey, exactly as on a real street. The class
lists therefore need to be right per generation, because the generation *is* the used-car cue.

**The trade-off, plainly.** We chose legibility over precision. The cost is that a new car's lower
band becomes available in game from launch rather than from its fifth year — at most a five-year
error in when a Medium passenger starts using a High car. The benefit is that every car the player
sees is a car whose wealth band they can read, with no invisible duplicates in the pool. This is a
deliberate compromise, not an oversight.

## Pre-war evidence for the two lowest classes

Research commissioned 2026-11-18 into licensed vehicles and owners before 1945 established the
following. `[LITERATURE:https://assets.publishing.service.gov.uk/media/5a7506feed915d502d6cce89/vehicles-tables-csv.zip]`

| Year | Private cars, etc. | Motorcycles (tax class) | Sidecar outfits |
| --- | --- | --- | --- |
| 1920 | 187,000 | 228,000 (or 287,739; see note) | not established |
| 1925 | 579,901 | 571,552 | not established |
| 1930 | 1,056,000 | 712,000 | not established |
| 1935 | 1,477,000 | 517,000 | **132,309** |
| 1939 | 2,034,000 | 418,000 | not established |
| 1945 | 1,487,000 | 309,000 | not established |

The 1935 sidecar figure is a secondary transcription of Ministry of Transport data whose totals
match the official return, split into 359,347 solo machines, 132,309 combinations and 24,911
tricycles. The 1920 figure is disputed between series (228,000 in the DfT table, 287,739 in
Koerner's transcription of Mitchell), and the 1930 references are a quarter apart, so neither
should be treated as settled.

**What this does not give.** No published source found maps ownership to a social class: not for
motorcycles, not for outfits, not for cars. The strongest class evidence is a 1953 survey reported
by Koerner, which found motorcycle owners "mainly in skilled manual labour occupations, with total
incomes between £200 and £399" — a description of owners, not a rate. O'Connell's interwar work
estimates about 20% of families had access to a car by the late 1930s, notes that only 25% of
households fell inside the industry's potential market, and records that people earning under £250
a year were thought unable to afford a car; his sample of 36 owners was 55% professional or
commercial, 19% lower-middle and 17% working class. Those are proportions of a small sample, not
ownership rates.

**Consequence for the config.** The pre-war zeros are assumptions, not findings of no ownership.
Since no rate is established, any non-zero value entered for classes 0 and 1 to let the outfits
spawn is a **gameplay assumption** and must be labelled as one in `privatecar.tab`, not presented
as historical calibration. The direction is supported — outfits were the cheaper alternative to a
car, £77–88 new in 1925 against £141 for an Austin Seven, and working-class motoring existed by the
late 1930s — but not the magnitude.

## Open questions

- **Pre-war `car_ownership` for classes 0 and 1 is a labelled assumption.** Research on 2026-11-18
  found licensed vehicle counts but no ownership rate by class. On the user's direction, class 1
  runs at 1% from 1925 and 2% by 1945, and class 0 at 1% from 1940, so that the pre-war outfits can
  spawn. `privatecar.tab` carries a comment stating that this is a gameplay assumption, not a
  historical rate, and the direction of the evidence but not the magnitude supports it.
  `[USER-DIRECTION:2026-11-18]`
- Whether the RangeRover retire date (1988) is right: the classic remained common through
  the 1990s, and extending it would soften the 1989+ Very-high gap.
- Whether old bangers deserve explicit models (an ageing cheap model kept alive for band 0)
  instead of the current stand-ins.
