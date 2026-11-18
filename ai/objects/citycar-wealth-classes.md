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
| 1920 | 1 [1] | 0 [1] | 6 [7] | 6 [12] | 5 [10] |
| 1925 | 2 [2] | 0 [2] | 10 [11] | 5 [12] | 4 [8] |
| 1930 | 3 [3] | 0 [3] | 9 [10] | 5 [12] | 6 [10] |
| 1935 | 2 [3] | 2 [6] | 7 [13] | 9 [14] | 6 [11] |
| 1940 | 2 [3] | 3 [7] | 7 [13] | 7 [11] | 5 [9] |
| 1945 | 2 [3] | 3 [7] | 6 [12] | 6 [10] | 5 [8] |
| 1950 | 3 [5] | 5 [10] | 8 [16] | 7 [12] | 4 [8] |
| 1955 | 4 [6] | 6 [11] | 6 [15] | 7 [12] | 6 [10] |
| 1960 | 5 [6] | 5 [10] | 6 [14] | 7 [13] | 5 [9] |
| 1965 | 6 [10] | 7 [16] | 9 [19] | 5 [12] | 5 [7] |
| 1970 | 4 [8] | 9 [16] | 10 [20] | 5 [13] | 4 [9] |
| 1975 | 5 [10] | 12 [21] | 16 [30] | 6 [20] | 5 [10] |
| 1980 | 6 [14] | 15 [25] | 17 [34] | 7 [22] | 5 [11] |
| 1985 | 6 [15] | 19 [31] | 19 [40] | 7 [22] | 5 [11] |
| 1990 | 6 [13] | 17 [28] | 15 [33] | 4 [19] | 5 [9] |
| 1995 | 6 [14] | 20 [31] | 14 [35] | 3 [17] | 5 [8] |
| 2000 | 4 [12] | 21 [29] | 12 [35] | 4 [17] | 4 [7] |
| 2005 | 4 [9] | 15 [21] | 10 [26] | 5 [18] | 6 [10] |
| 2010 | 4 [8] | 13 [20] | 11 [25] | 5 [17] | 5 [9] |
| 2015 | 4 [8] | 12 [19] | 10 [23] | 5 [16] | 3 [7] |
| 2020 | 3 [6] | 8 [13] | 8 [16] | 3 [12] | 3 [6] |
| 2025 | 1 [3] | 7 [9] | 5 [13] | 2 [7] | 1 [3] |

### With the planned queue added

The queue adds sixteen series: Yaris, Prius and Corolla; Renault 15, 17, 19, 21, 25 and Megane;
Citroën DS and CX; an Aston Martin family; and the four pre-1920 light cars.

| Year | 0 Very low | 1 Low | 2 Medium | 3 High | 4 Very high |
| --- | --- | --- | --- | --- | --- |
| 1920 | 3 [4] | 5 [9] | 3 [9] | 6 [12] | 5 [10] |
| 1925 | 6 [7] | 5 [12] | 5 [13] | 5 [12] | 5 [9] |
| 1930 | 6 [7] | 1 [8] | 4 [10] | 6 [12] | 7 [11] |
| 1935 | 5 [8] | 2 [9] | 3 [12] | 10 [14] | 7 [12] |
| 1940 | 5 [8] | 3 [9] | 4 [12] | 7 [11] | 6 [10] |
| 1945 | 4 [7] | 3 [8] | 4 [11] | 6 [10] | 6 [9] |
| 1950 | 5 [9] | 5 [11] | 6 [15] | 7 [12] | 5 [9] |
| 1955 | 5 [9] | 5 [11] | 6 [14] | 8 [13] | 7 [12] |
| 1960 | 5 [7] | 5 [10] | 6 [14] | 8 [14] | 6 [11] |
| 1965 | 6 [11] | 7 [16] | 9 [19] | 6 [13] | 6 [9] |
| 1970 | 4 [9] | 9 [16] | 10 [20] | 6 [14] | 5 [11] |
| 1975 | 5 [10] | 13 [23] | 18 [33] | 7 [22] | 6 [12] |
| 1980 | 6 [14] | 16 [27] | 19 [37] | 7 [23] | 6 [12] |
| 1985 | 6 [15] | 20 [33] | 22 [44] | 7 [24] | 6 [12] |
| 1990 | 6 [13] | 19 [30] | 17 [37] | 4 [21] | 6 [10] |
| 1995 | 6 [14] | 23 [34] | 16 [40] | 3 [19] | 6 [9] |
| 2000 | 4 [13] | 26 [34] | 14 [42] | 4 [19] | 5 [8] |
| 2005 | 4 [10] | 19 [25] | 11 [31] | 5 [19] | 7 [11] |
| 2010 | 4 [9] | 16 [23] | 12 [29] | 5 [18] | 6 [10] |
| 2015 | 4 [9] | 15 [22] | 11 [27] | 5 [17] | 4 [8] |
| 2020 | 3 [7] | 10 [15] | 9 [19] | 3 [13] | 4 [7] |
| 2025 | 1 [4] | 9 [11] | 6 [16] | 2 [8] | 2 [4] |

### What the table shows

- **Before 1945 the outer bands rest on motorcycles and on very few cars.** Very low is two pre-war
  outfits in 1935 and never more than three series; Low is empty until the Ford Model Y and Model C
  give it two series in 1935. This is correct, not a modelling gap: `privatecar.tab` gives both
  classes zero ownership before 1945.
- **But that same table means the pre-war outfits cannot spawn at all.** Their `.dat` files carry
  `class=0,1`, yet both classes are at 0% until 1945, so the pool is empty and the BSA 557, BSA
  Sloper and Norton Big Four never appear. Making them spawn needs the `privatecar.tab` values for
  classes 0 and 1 to be non-zero before 1945, which is a balancing decision rather than a data one.
- **The whole 2015–2025 block is thin, in every band.** Once each series is counted once, the recent
  fleet is five to ten series per band, falling to one or two in the outer bands by 2025. The
  pakset's modern coverage rests on the 2005–2015 cohort, most of which is near or past its retire
  date.
- **Very low in 2025 is one series** (the Dacia Sandero); **Very high in 2025 is one series** (the
  S-Class), becoming two with the planned Aston. Both outer bands need modern cars far more than the
  middle does.
- **Medium is the consistently strongest band** once generations are collapsed: six to nineteen
  series in every year from 1920, and the largest column throughout the middle of the century.
- The brackets run one to four times the main figure, which is the intended cross-class drift: a
  1985 Medium car is available to three bands, not one.

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

## Open questions

- Whether the RangeRover retire date (1988) is right: the classic remained common through
  the 1990s, and extending it would soften the 1989+ Very-high gap.
- Whether old bangers deserve explicit models (an ageing cheap model kept alive for band 0)
  instead of the current stand-ins.
