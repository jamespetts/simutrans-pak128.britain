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
   of c. 1925–1960 is the **motorcycle and sidecar**, not yet modelled
   `[USER-DIRECTION:2026-11-15]` (see [citycar-asset-gaps](citycar-asset-gaps.md)).
4. Horse-drawn: private carriages and the park drag are 3–4; the working cart is 0–1.

## Assignments (by class list)

- `0,1`: HorseCart, PeelP50, ReliantRobin, FordKa
- `0,1,2,3`: BMCMini; `0,1,2,3` (early bangers): FordT
- `0,1,2`: CitroenTypeC, MorrisMinor1928, FordModelC, AustinSeven, MorrisEight,
  FordPrefectEarly, AustinMetro, VauxhallNova, VauxhallCorsaB–F, FordFiestaMk1–Mk7
- `1,2`: AustinTen, AustinTen1937, FordPrefectLate, MorrisMinor, TriumphHerald,
  FordCortina, FordEscort-mk1/2/3/4, MorrisMarina, AustinMaestro, AustinMontego,
  FordFocus, BMC1100, FordAnglia100E, FordAnglia105E
- `2`: LeylandPrincess, FordMondeoMk1, FordMondeoMk4, NissanQashqai
- `2,3`: Rover8-1919, Rover9, MorrisOxfordBullnose/Flatnose/MO/2/3/4, CitroenTypeA,
  CitroenTypeB2, FordModelA, AustinLightTwelve, AustinTwelve, CitroenLight15,
  StandardVanguard, StandardVanguardVignale, LandRoverSeries, Triumph2000,
  TriumphDolomite, Volvo-240-Estate, RoverSD1, FordGalaxyMk1, FordGalaxyMk3, AudiA4B6,
  NewMini
- `3`: Rover8, Rover20
- `3,4`: DaimlerWagonette, HorseCarriageOpen, HorseCarriageClosed, park-drag, AustinPrincess
- `2,3,4`: RangeRover

## Coverage matrix (5-year points; ✓ = at least one car in the pool)

| Year | 0 VL | 1 L | 2 M | 3 H | 4 VH |
| --- | --- | --- | --- | --- | --- |
| 1920 | ✓ | ✓ | ✓ | ✓ | ✓ (horse carriages) |
| 1925–1945 | ✓ | ✓ | ✓ | ✓ | **GAP** |
| 1950–1985 | ✓ | ✓ | ✓ | ✓ | ✓ (AustinPrincess 1948–69; RangeRover 1970–88) |
| 1990–2025 | ✓ | ✓ | ✓ | ✓ | **GAP** |

Very low is continuous but thin 1955–65 (FordPrefectEarly and PeelP50 only) and is
historically marginal there (2–7% access). The two Very-high gaps are hard failures:
`car_ownership[4]` is 82–93% throughout. Fills required: see
[citycar-asset-gaps](citycar-asset-gaps.md) sections A and B.

## Provenance

Assignments calibrated 2026-11-15 from two Exa research runs (luxury and entry-level
segments, UK, 1920–2025 at 5-year points; per-model figures and sources in
[citycar-asset-gaps](citycar-asset-gaps.md)) and from the class anchors above. Compiled
with the ex-15 makeobj (`class` key, node version 0x8004)
`[CODE simutrans-extended ex-15 @ 6bda048cf]`, 359 objects, zero ignored warnings.

## Open questions

- Whether the RangeRover retire date (1988) is right: the classic remained common through
  the 1990s, and extending it would soften the 1989+ Very-high gap.
- Whether old bangers deserve explicit models (an ageing cheap model kept alive for band 0)
  instead of the current stand-ins.
