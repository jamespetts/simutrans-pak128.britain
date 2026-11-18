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
3. The cheapest aged models carry band 0 in earlier eras (Model T, Austin Seven, Morris
   Eight, Ford Prefect Early stand in for old bangers); the characteristic Very-low vehicle
   of c. 1920–1965 is the **motorcycle and sidecar** — era-specific outfits (BSA 557
   combinations, Norton Big Four, BSA M21 + Watsonian) are listed in
   [citycar-asset-gaps](citycar-asset-gaps.md) section C1 with provisional values (classes
   `0,1`; comfort below the BMC Mini). `[USER-DIRECTION:2026-11-15]`
4. Horse-drawn: private carriages and the park drag are 3–4; the working cart is 0–1.

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

Models on the road at each five-year point, by class, counted from the `.dat` intro and retire dates
(road presence, not production). The figure in brackets is the number the planned queue would add.

| Year | 0 Very low | 1 Low | 2 Medium | 3 High | 4 Very high |
| --- | --- | --- | --- | --- | --- |
| 1920 | 2 (+2) | 5 (+4) | 7 (+2) | 12 | 10 |
| 1925 | 5 (+2) | 8 (+4) | 11 (+2) | 12 | 8 (+4) |
| 1930 | 7 | 8 | 11 | 13 | 10 (+4) |
| 1935 | 8 | 9 | 13 | 15 | 11 (+4) |
| 1940 | 8 | 10 | 13 | 11 | 9 (+4) |
| 1945 | 7 | 8 | 11 | 10 | 8 (+4) |
| 1950 | 9 | 11 | 15 | 12 | 8 (+4) |
| 1955 | 9 | 12 | 16 | 13 (+4) | 10 (+2) |
| 1960 | 7 | 12 | 18 | 15 (+4) | 10 (+2) |
| 1965 | 11 | 18 | 21 | 12 (+2) | 8 (+3) |
| 1970 | 8 | 16 | 22 | 15 (+2) | 10 (+3) |
| 1975 | 10 | 22 (+2) | 33 (+3) | 22 (+2) | 11 (+2) |
| 1980 | 15 | 27 (+2) | 39 (+3) | 26 (+4) | 13 (+4) |
| 1985 | 18 | 41 (+2) | 55 (+5) | 28 (+3) | 12 (+4) |
| 1990 | 17 | 44 (+3) | 51 (+6) | 23 (+3) | 11 (+4) |
| 1995 | 20 | 48 (+5) | 58 (+8) | 27 (+3) | 13 (+4) |
| 2000 | 15 (+4) | 43 (+8) | 56 (+10) | 29 (+2) | 12 (+4) |
| 2005 | 12 (+4) | 33 (+7) | 47 (+8) | 33 (+4) | 16 (+4) |
| 2010 | 12 (+2) | 29 (+7) | 43 (+9) | 30 (+2) | 14 (+4) |
| 2015 | 10 (+2) | 26 (+5) | 38 (+7) | 27 (+2) | 12 (+4) |
| 2020 | 9 (+3) | 21 (+5) | 31 (+7) | 21 (+2) | 9 (+4) |
| 2025 | 6 (+2) | 16 (+4) | 25 (+6) | 15 (+2) | 6 (+4) |

### What the table shows

- **Very low before 1945 needs no attention.** `car_ownership[0]` is zero until 1945, so the thin
  early figure is correct rather than a gap. The 1920 pool is the Ford T and the horse cart, and the
  planned Humberette and GWK take it to four.
- **The middle of the century is the thinnest band for class 0** — seven models in 1960, of which
  three are motorcycle combinations. Ownership there is 2–7%, so this is marginal rather than a
  failure, but it is the weakest stretch in the fleet.
- **Class 1 and 2 fall away sharply after 2010**, because the models introduced around 2005 carry
  retire dates in the 2020s. The planned Yaris, Corolla and Megane generations restore about ten
  models in each band from 2000 onward.
- **Class 4 is thin after 2015** — six models in 2025. The planned Aston Martin family adds one; a
  second modern luxury saloon or SUV would be worth more.
- **Class 0 after 2020** falls to six models, and the planned queue adds only one (the Yaris XP210).
  This is the clearest forward gap: modern cheap cars are under-represented.
- The very dense 1985–2005 columns for classes 1–3 reflect the completeness of the mainstream
  ranges, not a surplus; those bands carry most of the parc.

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
