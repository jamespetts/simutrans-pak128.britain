---
status: draft
verified: New ex-15 @ cedd39abc (working tree, 2026-11-23)
---
# Citycar wealth classes (calibration and coverage)

**Covers**: the passenger-wealth-class calibration for `Obj=citycar` objects — the framework,
the per-model `class=` assignments, and the era coverage check. Field spec:
[citycar](citycar.md). Gaps and the assets needed to fill them:
[citycar-asset-gaps](citycar-asset-gaps.md). Parent: [object-types](../object-types.md).

**Private cars carry no cost fields.** An `Obj=citycar` object expresses wealth through `class=`
alone; `cost`, `runningcost` and `fixed_cost` are not used, and none of the 435 citycar `.dat`
files sets `runningcost`. Do not add costs to private cars as a balancing device: set the class
list. `[USER-DIRECTION:2026-11-20]`

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
access: Very high is 82% in 1750 and 93% by 1970; High reaches 20% by 1920 and 60% by
1950; Medium 21% (1951); Low 5% (1955); Very low 0 before 1940, 1% (1940), 2% (1955),
5% (1960).
Marginal access is still access: **keep the pools populated even when the percentage is
small** — frequency is handled by this table and by `citycar_level`, not by the class
lists. `[USER-DIRECTION:2026-11-15]`

**Source and basis of the rates.** The rows from 2002 are the five household income
quintiles of National Travel Survey table NTS0703, "Household car availability by household
income quintile: England, 2002 onwards" (DfT, NTS 2025 release, 10 September 2026): class 0
is the lowest quintile and class 4 the highest, and the value is 100 minus the published
"no car or van" percentage. In 2025 that gives 56, 71, 83, 83 and 83. Class 4 is a narrower
group than the highest quintile, so its rate is an approximation. Household access is used
rather than the NTS0704 personal-access measure (2025: 63, 78, 87, 87, 87), because one
household car is one vehicle. The 2030 and 2050 entries continue the measured 2002-2025 trend
with a logarithmically decaying rate: the annual change starts at the measured 2002-2025
average and halves by 2050, giving 2030: 57, 72, 83, 83, 83 and 2050: 60, 76, 83, 83, 83.
The three highest classes are held at their 2025 equality of 83 so that no class passes the
class above it. They are estimates, not measurements. The pre-2002 quintile rows are extrapolations from the
general Great Britain series.
`[CODE New ex-15 @ cedd39abc (working tree, 2026-11-23)]`
`[LITERATURE:https://www.gov.uk/government/statistical-data-sets/nts07-car-ownership-and-access]`

## Assignment principles

1. A model lists every class band that plausibly drove it at some point in its road life:
   trim spread at purchase plus downward drift into cheaper hands as it ages (a Ford
   Cortina is Low and Medium for this reason).
2. Genuine cross-class cars list widely (the Jaguar XF X250: `2,3`; the Range Rover L405:
   `3,4`; the BMC Mini: `0,1`).
3. The cheapest aged models carry band 0 once the class has car access at all — in practice from
   1940, when `privatecar.tab` first gives class 0 a non-zero share. Class 1 has 1% from 1925.
   **Class 0 had no car ownership before 1940, and class 1 none before 1925**
   (`car_ownership[0]` is zero from 1750 to 1940, `[1]` from 1750 to 1925; even in 1935 only
   Medium at 3% and High at 33% had cars). Pre-war cars therefore start at Medium or Low-and-Medium,
   not class 0, and the characteristic Very-low vehicle of c. 1920–1965 is the **motorcycle and
   sidecar** — era-specific outfits (BSA 557 combinations, Norton Big Four, BSA M21 + Watsonian)
   are listed in [citycar-asset-gaps](citycar-asset-gaps.md) section C1 with classes `0,1`.
   `[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-18]`
4. Horse-drawn: private carriages and the park drag are 3–4; the working cart is 0–1.

**Correction, 2026-11-18.** The first calibration put the pre-war cheap cars — Ford T, Austin Seven,
Morris Minor 1928, Ford Model C and Y, Citroën Type C, and the three Edwardian light cars — into
class 0. That contradicted the ownership table, which gives class 0 no car access before 1945. They
are now Medium (2), or Low-and-Medium (1,2) where their road life runs into the 1950s. The pre-war
Very-low pool is the motorcycle outfits, and it is thin because only two pre-war outfits exist
(BSA 557 from 1921 and BSA Sloper from 1930; the Norton Big Four runs 1940–48).

## How a class list is calibrated (2026-11-20)

The earlier rule — purchase band plus one band below — assumed that five years of depreciation
always moves a car down exactly one band. That assumption is wrong. Depreciation varies by
segment and era, so the lower band has to be calculated from the actual five-year-old price.

The redo works in six steps for every car:

1. **New-price band.** Put the launch price of the volume trim on the era's earnings ladder.
   407 of the 425 cars now have a model-specific launch price: 194 from the original price
   research and 213 added by the 2026-11-20 verification pass. The other 18 keep the committed
   purchase band and use a representative price inside that band for the five-year calculation;
   `price_source` in `ai/temp/wealth_results.csv` records which is which.
2. **Five-year price.** Multiply the new price by the researched five-year retained value for the
   model or, where no model-specific figure exists, its segment and era. Model-specific values
   override the matrix for the XF, XJ, S-Class, 7-series, A8, Range Rover, Defender, Rolls-Royce,
   Bentley, Tesla, BYD, Jaecoo, Fiesta, Focus, Mondeo, Ka, Mini, Beetle, 2CV, Lada, Yugo, Fiat 126
   and Škoda Estelle.
3. **Five-year band.** Put the five-year price on the earnings ladder using earnings at
   launch + 5, not at launch. This matters in fast-growing or inflationary periods.
4. **Union.** The class list is the contiguous union of the new-price band and the five-year band.
   It can therefore be one, two or three bands. A four-band span is capped at three, dropping the
   lowest band, so that no model blurs the whole ladder.
5. **Running-cost floor.** A cheap used executive or luxury car is not a Low-household car once
   fuel, insurance, tyres and repairs are counted. The floor is a model-level minimum, not a
   segment average. It is derived from the running-cost index described below, which in practice
   reproduces the model-group floors:
   - flagship luxury (Rolls-Royce, Bentley, 7-series, A8, S-Class, LS, XJ from 1980): High (3);
   - full-size executive (5-series, A6, E-Class, XF, S-Type, ES, Rover 800, P5/P6): Medium (2);
   - large luxury SUV (Range Rover P38/L322/L405, X5, Cayenne, Discovery 3–5): High (3);
   - utility SUV and Land Rover (early Range Rover, Discovery 1–2, Series): Medium (2);
   - high-end sports (Aston, Porsche): Medium (2);
   - compact executive (3-series, A4, C-Class), mainstream cars, small SUVs and cheap sports
     cars: no floor.
   The index can add one band where a model's running cost is at least 1.5× its segment median,
   or two at 2.2×, but only for models whose base floor is below High. The floor raises only the
   lower bound; it never raises the top.
6. **Pre-war floor.** Before 1945 the absolute wage ladder is not comparable with the modern
   market: even cheap cars were several times annual earnings and classes 0 and 1 had little or no
   car ownership. Pre-1919 cars therefore start at Medium (2); 1919–44 cars start at Medium (2),
   or Low-and-Medium (1,2) where the model is cheap and its road life runs into the 1950s.

### Class thresholds

Multiples of annual average earnings at the relevant year:

| Era | Class 0 | Class 1 | Class 2 | Class 3 | Class 4 |
| --- | --- | --- | --- | --- | --- |
| pre-1919 | ≤1.0× | ≤2.0× | ≤4.0× | ≤8.0× | >8.0× |
| 1919–1944 | ≤0.5× | ≤1.0× | ≤2.0× | ≤4.0× | >4.0× |
| 1945–1959 | ≤0.35× | ≤1.0× | ≤2.0× | ≤4.0× | >4.0× |
| 1960–2026 | ≤0.25× | ≤0.75× | ≤1.5× | ≤3.0× | >3.0× |

The 1960+ thresholds follow the earlier 0.75/1.5/3.0 ladder, with 0.25× as the Very-low ceiling.
The earlier thresholds are shifted because car ownership was concentrated: a 1902 light car at
five times average earnings was a Medium car, not a Very-high one.

### Retained values used

The research matrix (five-year retail value, per cent of new list price):

| Segment | pre-1900 | 1900–18 | 1919–39 | 1945–59 | 1960–79 | 1980–99 | 2000–26 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A City / microcar | 8 | 17 | 25 | 105 | 55 | 40 | 45 |
| B Supermini | 8 | 16 | 24 | 100 | 53 | 39 | 44 |
| C Lower medium | 8 | 15 | 22 | 92 | 48 | 35 | 37 |
| D Upper medium | 7 | 14 | 20 | 85 | 44 | 32 | 35 |
| E Executive | 6 | 12 | 18 | 74 | 38 | 28 | 33 |
| F Luxury | 5 | 9 | 14 | 58 | 30 | 24 | 28 |
| Sports | 7 | 14 | 21 | 88 | 48 | 36 | 46 |
| SUV / 4x4 | — | — | — | 96 | 50 | 37 | 44 |
| MPV | — | — | — | — | — | 36 | 41 |

Recent 2021–26 readings are slightly higher for most segments (A 49, B 47, C 40, D 38, E 35,
F 28, Sports 50, SUV 48, MPV 45); they are used for models launched after 2020. The 1945–59
column is above 100 per cent because the controlled post-war new-car market traded above list;
that is measured evidence, not an error. It is why some early post-war cars have a one-band list
(for example the Ford Anglia 100E, new and five-year-old both in Medium).

### Price verification pass (2026-11-20)

The first redo had a model-specific price for 194 cars and kept the committed band for the other
231. A verification pass has now priced 213 of those 231 from period UK sources:

| Result | Models |
| --- | --- |
| Priced, high confidence | 136 |
| Priced, medium confidence | 60 |
| Priced, low confidence | 17 |
| Not found, still on the fallback band | 18 |

The sources are period price lists, launch reports and road tests rather than modern
retrospectives: Motor Sport, Autocar, Motor, The Motor, Financial Times, The Independent,
Commercial Motor, manufacturer press offices, marque clubs and reproduced dealer adverts. The
verified prices are in `ai/temp/price_research_merged.csv`; the six batch files retain the URLs.

The correction that matters most is the removal of the round-number block. The 1972 BMW 520 is
£2,999, not £15,000; the 1974 Golf is £1,294, not £6,000; the 1948 2CV is £400, not £3,000; the
1986 XJ6 2.9 is £17,000, not £70,000. The 2022 Kia Sportage is £26,745, so it is `1,2`, not the
inherited `3,4`. In total 121 class lists changed in the final application.

The 18 cars still on the fallback band are:
Ford Zephyr Mk3, Hillman Minx Arrow, Datsun Cherry F10, Datsun Cherry N10, Datsun Sunny B310,
Nissan Sunny B11, Austin Metro Mk2, Renault 25 Phase 1, Rover 200 SD3, Nissan Bluebird T12,
Citroën CX Series 2, Nissan Sunny N13, Renault 25 Phase 2, Renault 21 Phase 2, Vauxhall Astra Mk3,
Renault 19 Phase 2, Ford Sierra Mk3 and Vauxhall Vectra B. Their lists remain lower-confidence.

### Running-cost index (2026-11-20)

The index is a per-model annual running cost at age five, built from a 9-segment × 6-era matrix
and a model-level adjustment for price position and known outliers.

| Component | Source and method |
| --- | --- |
| Fuel | UK pump price for the year at launch + 5 (DESNZ *Quarterly Energy Prices* 1954–2025; Hansard petrol answers 1913–1952), annual mileage 6,000–10,000 by era, and the segment/era MPG adjusted by the model's price ratio within its segment |
| Insurance | Parkers insurance-group ranges for 1980–2026, interpolated by the model's price ratio; before 1980 there was no group rating and the matrix uses a small third-party provision |
| Servicing | Kwik Fit engine-band service prices plus the statutory MOT fee, scaled to the era by earnings and a service-frequency multiplier (7 services a year pre-1919, 4 in 1919–39, 2.5 in 1945–59, 2 in 1960–79, 1.5 in 1980–99, 1 now) |
| Tyres | Segment/era tyre cost, scaled the same way |
| Repair risk | 1–4 by segment and era, plus one for flagship luxury, large luxury SUV and exotic sports cars |

The model-level adjustment uses the model's verified price relative to its segment median: a car
priced twice the segment median uses about 18 per cent more fuel, carries a higher insurance
group and costs more to service. Explicit overrides cover the known outliers (Range Rover, X5,
Cayenne, Discovery, 7-series, A8, S-Class, XJ, LS, Rolls-Royce, Bentley, Aston, Porsche, the
2CV/Fiat 126, the small city cars and the EVs).

The result is a dimensionless index, 1.0 = the segment-era median. The distribution is 0.5–2.2,
with most cars at 0.8–1.2. The high end is exactly the expected group: Cayenne 2.02, Range Rover
L322 1.99, Range Rover L405 1.95, X5 E53 1.84, Discovery 3/4/5 and X5 E70/G05 1.74–1.76,
Bentley and Rolls-Royce 1.7–2.2. Every one of those already has a base floor of High, so the
index confirms the floor rather than changing it. The only model the index moves is the Porsche
Macan Electric, from Medium to High (2→3), because its insurance group and tyre costs remain
luxury-SUV levels even though its fuel cost is low.

The weak parts are recorded rather than hidden: all pre-1980 MPG figures are period-typical
estimates marked low confidence; the 1960–79 fuel price uses the 1970 value for an era containing
two oil shocks; service and tyre costs are 2025 references scaled by earnings and a
service-frequency multiplier, not measured period bills; and the index is not applied before
1945, where the ownership floor dominates.

### Examples

| Model | New band | Five-year band | Running floor | Class list |
| --- | --- | --- | --- | --- |
| Jaguar XF X250 (2008) | High (3) | Low (1) | Medium (2) | `2,3` |
| Jaguar XF X260 (2015) | Medium (2) | Low (1) | Medium (2) | `2` |
| BMW 5-series E39 (1995) | High (3) | Low (1) | Medium (2) | `2,3` |
| BMW 5-series G60 (2023) | Medium (2) | Low (1) | Medium (2) | `2` |
| BMW 7-series G70 (2022) | Very high (4) | Medium (2) | High (3) | `3,4` |
| Ford Fiesta Mk7 (2017) | Low (1) | Very low (0) | — | `0,1` |
| Ford Anglia 100E (1953) | Medium (2) | Medium (2) | — | `2` |
| Rolls-Royce Silver Ghost (1907) | Very high (4) | Very high (4) | — | `4` |
| Range Rover L405 (2012) | Very high (4) | Medium (2) | High (3) | `3,4` |
| Kia Sportage 5 (2022) | Medium (2) | Low (1) | — | `1,2` |
| Citroën 2CV (1948) | Medium (2) | Low (1) | — | `1,2` |

The 5-series is the case that prompted the running-cost work. Its five-year purchase price is Low
money, but a Low household cannot carry the fuel, insurance, tyres and repair risk of a 5-series;
the lower bound is therefore Medium. The XF X250 is `2,3` for the same reason; the X260 is Medium
only because its new price was already Medium. The XFR-S halo is not part of the standard XF model
and does not add a fourth band.

### Distribution in the current tree

436 vehicles (425 cars, 7 outfits, 4 horse-drawn):

| Class list | Models |
| --- | --- |
| `0,1` | 75 |
| `0,1,2` | 40 |
| `1` | 11 |
| `1,2` | 96 |
| `1,2,3` | 21 |
| `2` | 25 |
| `2,3` | 70 |
| `2,3,4` | 26 |
| `3` | 16 |
| `3,4` | 44 |
| `4` | 12 |

That is 64 one-band models, 285 two-band models and 87 three-band models. The verified prices
narrowed many lists: the ordinary family cars of the 1970s–90s were cheaper relative to earnings
than the fallback anchors assumed, so they now run `0,1,2` (Medium new, Very low at five years)
rather than a wider spread. The one-band lists are the cars whose new and five-year prices stayed
in the same band (Rolls-Royce, the 1945–59 above-list cars, and the modern Low-only hatchbacks).

## Coverage, 1920–2025

| Year | 0 Very low | 1 Low | 2 Medium | 3 High | 4 Very high |
| --- | --- | --- | --- | --- | --- |
| 1920 | 0 [1] | 1 [1] | 7 [22] | 11 [16] | 7 [7] |
| 1925 | 0 [2] | 2 [3] | 8 [26] | 12 [18] | 8 [8] |
| 1930 | 0 [3] | 3 [4] | 9 [31] | 14 [22] | 12 [12] |
| 1935 | 0 [2] | 3 [8] | 9 [32] | 12 [23] | 15 [15] |
| 1940 | 0 [4] | 5 [17] | 14 [37] | 11 [23] | 16 [16] |
| 1945 | 0 [4] | 5 [17] | 12 [33] | 12 [21] | 13 [13] |
| 1950 | 0 [4] | 5 [19] | 15 [41] | 16 [28] | 16 [16] |
| 1955 | 0 [3] | 4 [17] | 18 [44] | 20 [32] | 15 [15] |
| 1960 | 0 [2] | 2 [10] | 17 [45] | 24 [36] | 16 [16] |
| 1965 | 0 [4] | 4 [21] | 19 [52] | 28 [44] | 19 [19] |
| 1970 | 0 [4] | 2 [29] | 23 [60] | 34 [47] | 15 [15] |
| 1975 | 0 [19] | 7 [47] | 34 [69] | 32 [46] | 16 [16] |
| 1980 | 0 [26] | 8 [57] | 39 [72] | 30 [46] | 16 [16] |
| 1985 | 0 [44] | 15 [73] | 49 [75] | 24 [36] | 12 [12] |
| 1990 | 0 [48] | 19 [68] | 45 [65] | 19 [30] | 12 [12] |
| 1995 | 0 [43] | 20 [70] | 46 [66] | 19 [35] | 17 [17] |
| 2000 | 0 [40] | 22 [72] | 46 [65] | 19 [35] | 17 [17] |
| 2005 | 0 [35] | 25 [68] | 39 [57] | 21 [40] | 21 [21] |
| 2010 | 0 [38] | 32 [70] | 37 [50] | 20 [37] | 20 [20] |
| 2015 | 0 [36] | 36 [70] | 35 [46] | 20 [35] | 17 [17] |
| 2020 | 0 [32] | 35 [63] | 31 [41] | 21 [37] | 18 [18] |
| 2025 | 0 [25] | 30 [62] | 35 [42] | 18 [32] | 16 [16] |

### What the table shows

- **Very low is a large bracket from 1985 onward**, peaking at 48 models in 1990. The verified
  prices put many 1970s–90s family cars at 0.8–1.2× earnings when new, so their five-year-old
  price is below the Very-low ceiling. This is the cheap used-car market the pakset previously
  under-represented.
- **The 2025 bracket is 25 Very low, 30 Low, 35 Medium, 18 High and 16 Very high.** Medium is
  the largest, not Low: the running-cost floor removed the executive and luxury cars from Low,
  while the cheap hatchbacks and crossovers fill Very low.
- **The 1930s fleet is concentrated in Medium/High**, not uniformly Very high: the pre-war price
  method puts the cheap and mid cars in Medium, the luxury cars in High/Very high.
- **One-band and three-band lists are real, not rounding errors.** The Rolls-Royce new and used
  prices both stay in Very high; the XF X250 new price is High but its five-year price is Low, so
  it spans `2,3`; the 7-series G70 spans `3,4` once the running-cost floor is applied.
- **The main figure counts each model once in its upper band**, the purchase band; the bracket
  counts it in every band its list allows. The bracket is the coverage measure.

## Provenance

The 2026-11-20 redo replaces the earlier one-band rule. It uses:
- model-specific launch prices for 407 of the 425 cars. 194 came from the original price research
  and 213 from the verification pass (136 high, 60 medium, 17 low confidence; 18 not found).
  The price files are `ai/temp/price_research_a.csv` to `f.csv` and the merged
  `ai/temp/price_research_merged.csv`, with the source URL on every row;
- the committed purchase band for the other 18 cars, with a representative price inside that
  band for the five-year calculation;
- the retained-value matrix and model exceptions in `ai/temp/retained-values.csv`, researched on
  2026-11-20 from Auto Express/VIP Data, Auto Express/CDL, cap hpi, Glass's via Motor Trader,
  Parkers via The Times, Motor Sport, Offer (2007) and Hansard;
- the running-cost matrix in `ai/temp/running-cost-matrix.csv` and the per-model index in
  `ai/temp/running-index.csv`, built from DESNZ *Quarterly Energy Prices*, Hansard petrol answers,
  Parkers insurance groups, Kwik Fit servicing and the AA/RAC/Confused.com cross-checks recorded
  in `ai/temp/running-cost-notes.md`;
- the class thresholds above and the union rule.

The full evidence and source register for retained values are in
`ai/temp/depreciation-research.md`. The previous one-band pass and its 54 changes are superseded.


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

- **New prices are model-specific for 407 of the 425 cars.** 194 came from the original research
  and 213 from the 2026-11-20 verification pass. The 18 still on the fallback band are listed in
  the price-verification section; their class lists remain lower-confidence.
- **The running-cost index is built, but its early-era inputs are weak.** All pre-1980 MPG figures
  are period-typical estimates marked low confidence; the 1960–79 fuel price uses the 1970 value
  for an era containing two oil shocks; service and tyre costs are 2025 references scaled by
  earnings and a service-frequency multiplier, not measured period bills; and the index is not
  applied before 1945, where the ownership floor dominates. A later pass should replace those
  inputs with period road-test MPG and garage bills.
- **Desirability is not applied as a band adjustment.** Cult cheap cars (Mini, Beetle, 2CV, Fiat
  500) and undesirable cheap cars (Lada, Yugo, Fiat 126, Škoda Estelle) are treated as neutral in
  this pass. The earlier colourway profile for the BMC Mini was lost when the price-only pass
  overwrote it; if it is restored, it should follow the colourway-profile rules in
  `ai/temp/analysis-wealth-factors.md`.
- **The pre-1919 and 1919–44 class thresholds are a calibration judgement.** They are set to fit
  the pre-war ownership evidence (even cheap cars were several times annual earnings and classes
  0/1 had little or no car ownership), not to a measured price distribution. Review them if a
  pre-war price series is assembled.
- **Pre-war `car_ownership` for classes 0 and 1 is a labelled assumption.** Research on 2026-11-18
  found licensed vehicle counts but no ownership rate by class. On the user's direction, class 1
  runs at 1% from 1925 and 2% by 1945, and class 0 at 1% from 1940, so that the pre-war outfits can
  spawn. `privatecar.tab` carries a comment stating that this is a gameplay assumption, not a
  historical rate, and the direction of the evidence but not the magnitude supports it.
  `[USER-DIRECTION:2026-11-18]`
- The Range Rover retire date is settled as of 2026-11-20: all five colourways now carry a
  staggered road tail of 1998–2005, replacing the single 1988 date on the Blue colourway. The
  classic remained common through the 1990s.
- Whether old bangers deserve explicit models (an ageing cheap model kept alive for band 0)
  instead of the current stand-ins.
