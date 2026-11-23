---
status: draft
verified: none
---
# Balance synthesis

**Covers**: what the completed cost research implies for balance when every domain is taken together —
the conversion basis, the annual account of a representative British railway of about 1900, the same
railway priced with the pakset's data, both against Acworth, the four standing hypotheses, the joint
effect, the decisions, and the measurements outstanding.

Sources: [vehicle-cost-evidence](vehicle-cost-evidence.md), [base-maintenance](vehicle-cost/base-maintenance.md),
[infrastructure-cost-synthesis](infrastructure-cost-synthesis.md), [balance-conversion-check](balance-conversion-check.md),
[fuel-evidence](fuel-evidence.md), [staff-wages](staff-wages.md), [prices-config](prices-config.md),
[goods-rate-evidence](goods-rate-evidence.md), `New/config/prices.tab`. **No `.dat` or `config` file has
been changed.** Every figure is quoted with a link or is arithmetic shown in the text. `[ASSUMPTION]`
marks a working assumption no source supports; `[UNVERIFIED]` an agent inference.

## 1. The conversion basis

The displayed unit is the **Simucredit**; the engine stores money in **Simucents**, 100 to the
Simucredit. The pakset uses two conversions because the engine has two timescales:

| | One Simucredit | One Simucent |
|---|---|---|
| Revenue | £0.005208 | £0.00005208 |
| Capital | £0.396311 | £0.00396311 |

The ratio between them is 76.0917, the workbook's time compression.
[prices-config](prices-config.md), [balance-conversion-check](balance-conversion-check.md)

**The capital rate is settled by measurement.** [balance-conversion-check](balance-conversion-check.md)
reads the engine's tooltip path: `set_scale` multiplies the `.dat` value by `meters_per_tile / 1000`,
the tooltip multiplies by `base_meters_per_tile / meters_per_tile`, the length factors cancel, and
`money_to_string` divides by 100. Two screenshots of `wssri-intermediate` (`cost=90000`, forge 15,000)
confirm it: (90,000 + 15,000) × 0.00396311 = **£416 a kilometre**. They display 1,974.00 and 1,100.00,
the same object under the `infrastructure` index at 188 (1930) and 104.76 (about 1910).

**Each object type is indexed by its own series.** `.dat` values are 1900 nominal. Vehicle `cost`
is indexed by `vehicle purchase`, vehicle running and fixed by `general`, ways/tunnels/bridges/way
objects/signals by `infrastructure`, and buildings by `buildings`. The series diverge: in 2026
`vehicle purchase` is 0.90 times `general`, `infrastructure` 0.57 and `buildings` 1.35. The
2026-11-22 rebuild of the two cost workbooks uses the type series on both sides of every
comparison; the first version deflated everything with `general`. [prices-config](prices-config.md)
`[USER-DIRECTION:2026-11-22]`

**Per-month charges are doubled.** `calc_adjusted_monthly_figure` = 2^(22-18) / INT(1000/125) = 2 at
the pakset settings, and it applies to vehicle `fixed_cost`, to way/tunnel/bridge/way-object
maintenance (`finance_t::get_maintenance_with_bits`) and to building maintenance. The way tooltip
omits it and under-reports upkeep. [vehicle-cost-model](vehicle-cost-model.md)
`[CODE simutrans-extended ex-15 @ 2ec587a]`

**The revenue rate is pinned by two independent anchors:**

- Passenger fare: `value[1]=50` in `goods-128.dat` is 50 Simucents a kilometre, 0.50 Simucredits, or
  £0.002604 — 1.01d a mile, the 1844 third-class maximum. `[CODE New ex-15 @ 8d0603d81]`,
  [class](class.md)
- Coal: `value[1]=45` is 0.45 Simucredits a tonne-kilometre, £0.002344, or 0.905d a ton-mile against
  the measured 0.910d for coal. [goods-rate-evidence](goods-rate-evidence.md)

**The fare index does no work at 1900.** `passenger fare` is flat at 100 from 1750 to 1914 and `general`
is 100 at 1900, so the **fare-to-general ratio at 1900 is 1.00**: any fare error is in the level, not the
series. (At 2026 the ratio is 7,073 ÷ 16,281 = 0.43.) `New/config/prices.tab`

## 2. The representative railway, 1900, from measured sources

Physical definition `[ASSUMPTION]`: one route kilometre, double track (16 way tiles), 17 trains each
way per day, one locomotive and three 80-seat third-class carriages, 45 per cent load (108 passengers),
locomotive and carriage utilisation 37,000 km a year — 23,000 miles, at which Hill's per-mile and
per-engine-year figures reconcile in [base-maintenance](vehicle-cost/base-maintenance.md). Receipts at
the calibrated fare: 108 × 50 Simucents × 12,410 train-km = £3,490 a kilometre a year. The density is
chosen so that receipts land on Acworth's figure: a normalisation, not a measurement.

| Head | £/km | Share of receipts | Source |
|---|---|---|---|
| Way and works maintenance, incl. buildings | 311 | 8.9% | Acworth 1902-03, [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §8 |
| Locomotive running: repairs, renewals, fuel, enginemen | 926 | 26.5% | LNER 1923, [published-maintenance](vehicle-cost/published-maintenance.md) |
| Carriage and wagon repairs, traffic expenses, rates, misc. | 828 | 23.7% | residual |
| General charges: management, legal, audit, office | 175 | 5.0% | [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §9 |
| **Working expenses** | **2,240** | **64.0%** | |
| **Net receipts** | **1,260** | **36.0%** | Acworth: 4.5% on 8× receipts |
| Capital | 28,000 | 8.0 × receipts | see below |

The third head is a residual: the research has not separated carriage and wagon repairs from traffic
expenses and rates. It is the least measured head and the largest gap in section 5.5.

**The two Acworth figures are on different bases.** £175 is 5.0 per cent of £3,500, and £3,500 × 8 =
£28,000, which is 24 per cent above the £22,596 a kilometre Acworth gives for "road and buildings". Road
and buildings is therefore about 81 per cent of total capital, and the 8× test applies to the total.
`[UNVERIFIED]`

**Crew, measured** ([staff-wages](staff-wages.md), 1907 Board of Trade enquiry): driver 45s 11d a week,
fireman 27s 5d, passenger guard 29s 3d — 1,231d a week. At 52 weeks, because it is a full ordinary week
and railway wages of that date carried no paid holiday: 64,012d = **£266.72 a train-year**, or £89.46 a
route kilometre at 0.335 trains a kilometre. `[ASSUMPTION]` one crew-year per train-year, assuming a
diagrammed crew; a roster sharing three men across several turns would reduce it. The ordinary-time
rates give £237.68, 11 per cent lower.

## 3. The same railway priced with the pakset's data

### 3.1 Operating account

Per train-kilometre in Simucents, the unit the player pays and receives. No rate assumption enters this
table.

| Item | Simucents/train-km | Per cent of receipts | Acworth head |
|---|---|---|---|
| Receipts (108 passengers × 50) | 5,400 | 100 | |
| Locomotive repair (`runningcost` 199) | 199 | 3.69 | locomotive, 26.5 |
| Locomotive standing (`fixed_cost` 45,444) | 29.5 | 0.55 | locomotive |
| Crew, driver + fireman + guard, 1907 earnings | 138.4 | 2.56 | locomotive |
| Carriage standing (3 × `fixed_cost` 844) | 1.64 | 0.03 | other working, 23.7 |
| Way and station maintenance | 1.48 | 0.03 | way and works, 8.9 |
| Fuel (14.4 kg/km at `fuel[steam]` 10) | 0.14 | 0.003 | locomotive |
| Traffic expenses, stations, signalmen, clerks | 0 | 0 | other working |
| General charges | 0 | 0 | 5.0 |
| **Total** | **370.2** | **6.85** | **64.0** |

Arithmetic: `runningcost` 199 is per kilometre by definition; standing charges are `fixed_cost × 2` a
month ([vehicle-cost-model](vehicle-cost-model.md)) × 12 ÷ 37,000 km; way maintenance is
550 × 0.125 × 16 × 12 ÷ 12,410 km and station maintenance (11,800 + 2 × 2,700) × 0.125 × 12 ÷ 5 ÷
12,410; crew is £266.72 ÷ 37,000 km at the revenue rate (1907 earnings: driver 45s 11d, fireman
27s 5d, guard 29s 3d).

**The pakset charges crew almost nowhere.** Only two of the 871 train `.dat` files declare any
`staff`, and an undeclared type is absent from the engine's staff map rather than defaulted.
`[CODE New ex-15 @ 8d0603d81]` The 138.4 is the whole crew cost, not an addition. `staff.tab` now
charges the measured 1907 rates, or 123.3 Simucents a train-kilometre (driver £104, fireman
£61.75, guard £71.93; [staff-wages/reconstruction](staff-wages/reconstruction.md)); the remaining
gap is coverage, not the wage level.

**The timescale caveat.** Per-month charges are 76 times smaller in pounds than per-kilometre charges of
the same engine value. Way maintenance therefore reads 0.03 per cent of receipts in engine cash but 1.5
per cent in pounds, and the gap column overstates the pound shortfall for every per-month item. **The
6.85 per cent is the player's ratio; whether it should be 64 per cent depends on M2.** `[UNVERIFIED]`

### 3.2 Capital per route kilometre

At £0.00396311 a Simucent:

| Item | Simucents | £/km |
|---|---|---|
| Way, 16 tiles of WSSR at 55,000 | 110,000 | 436 |
| Forge, 15,000 a route km | 15,000 | 59 |
| Stations, one per 5 km (brick building, 2 brick platforms) | 30,250 | 120 |
| Land, 16 tiles at `cost_buy_land` 1,500 | 24,000 | 95 |
| Signalling, Rapier 1874 model at £315/route km | 79,475 | 315 |
| Locomotives, 0.335 a km at 6,532,500 | 2,190,975 | 8,684 |
| Carriages, 1.006 a km at 709,000 | 713,396 | 2,827 |
| **Total** | **3,163,096** | **12,536** |

Capital is 3.6 × receipts against Acworth's 8.0, and rolling stock is 92 per cent of it — the converse
of the historical position, where road and buildings were about 81 per cent.

## 4. Against Acworth

| Ratio | Acworth | Reconstructed history | Pakset data |
|---|---|---|---|
| Capital ÷ gross receipts | 8.0 | 8.0 | 3.6 |
| Working expenses ÷ receipts | 64% | 64% | 6.85% |
| Net return on capital | 4.5% | 4.5% | 25.9% |

Working expenses are 9.3 times below the historical proportion, so net receipts are 93 per cent of the
total and a 25.9 per cent return follows from that rather than being a separate error. Capital is 2.2
times too small, which pushes the return up again.

## 5. The four standing hypotheses

### 5.1 Infrastructure maintenance is 4 to 100 times too high — **false; the direction is reversed**

At the confirmed rate `wssr` is **£218 a kilometre** of capital with **£52 a kilometre a year** of
maintenance, and `wssri_intermediate` with its forge is £416. The measured permanent-way-only
capital is £1,300-1,900 a kilometre and the measured maintenance excluding renewal £44-334 a
kilometre a year. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §2 So capital
is six to nine times too **low**, while maintenance sits just inside the measured range. The
capital-to-maintenance ratio errs accordingly: the way returns 4.2 years of capital
(55,000 ÷ (550 × 2 × 12)) against Acworth's 72.7, because capital is under-priced and maintenance
is not. The correction is capital about sixfold and maintenance about twofold, which is the
synthesis's recommendation (`wssr` 55,000 → 320,000, maintenance 550 → 1,300). The "maintenance
carries renewal" finding survives and explains why maintenance rises less than
capital: the accounts combine routine maintenance with renewal, and the engine renews separately
through `weg_t::renew()`.

### 5.2 Vehicle capital is too low on one conversion and too high on the other — **supported**

| Class | `.dat` cost | £ at revenue rate | £ at capital rate | Measured, £1900 | Too low (rev) | Too high (cap) |
|---|---|---|---|---|---|---|
| GNR 8 ft single | 3,984,320 | 208 | 15,791 | 1,974 | 9.5 | 8.0 |
| LSWR T9 | 6,532,500 | 340 | 25,889 | 3,333 | 9.8 | 7.8 |
| LNER A4 | 11,088,000 | 577 | 43,943 | 4,885 | 8.5 | 9.0 |

The bracket is real and the upper bound has a cause: the calibration workbook applies the capital
conversion and then multiplies by 8, giving 2,019 Simucents to the pound where the confirmed rate is
252.33. `[CODE New ex-15 @ 8d0603d81]` That 8 is exactly the excess in every steam row, so "no uniform
correction factor" does not hold on the capital rate; the scatter is in the measured prices and the
diesel rows. [balance-conversion-check](balance-conversion-check.md) records the same multiple.

### 5.3 Vehicle running cost is roughly right while fixed cost is too small — **supported**

`runningcost` 199 for the T9 is 2.49d a kilometre against a measured 1.56 to 2.17d for 1892
locomotives, 1.15 to 1.6 times the measured level; as a share of receipts it is 3.7 per cent against
about 3.3, which is right. `fixed_cost` is 0.03 per cent of receipts for a carriage against a measured
£18.6-46.7 a vehicle-year, which at three carriages per 37,000 km is 0.9 per cent: 30 times too small.
Judged in pounds at the capital rate the same figure reads as 1.7 to 4.3 times too *large*. **A charge
paid out of revenue must be tested as a share of revenue**, or the two timescales disagree by 76.09.
`[UNVERIFIED]`

### 5.4 Revenue is too high, costs are too low, or both — **both, and costs dominate**

The fare is 1d a mile, the 1844 statutory maximum, against a measured average third-class fare of about
0.55d — 1.8 times too high ([class](class.md)), and a level error because the fare-to-general ratio at
1900 is 1.00. The coal rate is correctly calibrated at 0.905d against 0.910d.

Working expenses are 6.85 per cent of receipts against 64 per cent, a factor of 9.3. Cutting the fare to
0.55d would take the operating ratio from 6.85 to 12.4 per cent, not to 64. **The cost side is the
dominant error by an order of magnitude.**

### 5.5 The shortfall by component

| Head | Acworth | Pakset | Gap, points | Share of gap |
|---|---|---|---|---|
| Other working: carriage and wagon repairs, traffic, rates | 23.7% | 0.03% | 23.7 | 41% |
| Locomotive running: repairs, renewals, fuel, enginemen | 26.5% | 6.80% | 19.7 | 34% |
| Way and works | 8.9% | 0.03% | 8.9 | 16% |
| General charges | 5.0% | 0 | 5.0 | 9% |
| **Total** | **64.0%** | **6.85%** | **57.2** | **100%** |

Within the locomotive head, crew is now measured at 2.56 per cent and is the one part closed: it
accounts for 2.4 of the 57.2 points, or 4 per cent of the shortfall. The largest gap is the head the
research has least separated: traffic expenses (station staff, signalmen, clerks) have no charging
mechanism, and carriage and wagon repairs are charged at a fortieth of the locomotive repair rate.

## 6. The joint effect

### 6.1 Worked

From 6.85 per cent, closing each head to its Acworth value:

1. **Vehicle capital ÷ 8.** Balance sheet only: the operating ratio stays at 6.85, and capital falls
   from £12,536 to £2,464.
2. **Way and works to 8.9:** +8.9 points, 15.7 per cent.
3. **Locomotive running to 26.5:** +19.7 points, 35.4 per cent.
4. **Other working to 23.7:** +23.7 points, 59.1 per cent.
5. **General charges to 5.0:** +5.0 points, 64.1 per cent.

The cost correction restores Acworth's structure: 64.1 per cent, net receipts 36 per cent.

### 6.2 Capital does not follow

Applying both directions — infrastructure to the synthesis's recommendations, vehicles ÷ 8:

| Case | Capital £/km | ÷ receipts | Return on capital |
|---|---|---|---|
| As written | 12,536 | 3.6 | 26.0% |
| Vehicles ÷ 8 | 2,464 | 0.7 | 132.3% |
| Infrastructure corrected | 19,474 | 5.6 | 16.7% |
| Both | 9,403 | 2.7 | 34.7% |

Components, in Simucents per route kilometre, from the table in section 3.2: way 110,000
corrects to 320,000, forge 15,000 to 76,000, stations 30,250 to 1,510,000; land 24,000 and
signalling 79,475 are unchanged; locomotives and carriages together are 2,904,371 and become
363,046 at ÷ 8. The corrected infrastructure total is therefore 2,009,475 against a baseline of
258,725, a factor of 7.8 rather than the three to nine often quoted, because the station
recommendation is fiftyfold and stations are the second-largest infrastructure item on the line.
Receipts are £3,500 a route kilometre a year, the figure implied by Acworth's eight times and
carried through the account; the return is the operating margin over capital.

**The two corrections do not converge on Acworth; they diverge from it.** Infrastructure is 8 per
cent of this line's capital and several times too cheap, so correcting it adds about £6,900 a
kilometre. Rolling stock is 92 per cent and eight times too dear, so correcting it removes about
£10,100. The net movement is a fall of 1.33 times, from 3.6 to 2.7 against Acworth's 8. To reach
8 the line would need £27,920 a kilometre; corrected road, buildings and stations are £7,963, so
the missing £20,000 is composition the line does not have — urban land, tunnels, viaducts,
terminal stations, multiple track. **A rural line cannot reproduce a national average**, so the
capital test cannot run until an average-mix line exists. Capital, not cost, is where the
remaining unexplained gap sits.

### 6.3 Sensitivity

The operating ratio does not depend on either conversion rate: it is a ratio of engine Simucents. The
capital ratios do. At the revenue rate every capital figure divides by 76.09 and the return multiplies
by 76.09, which is impossible as a level — a way would cost £5.70 a kilometre. Only the capital rate
gives levels within an order of magnitude of history, and it is confirmed by measurement. The residual
uncertainty is the timescale of per-month charges (M2).

## 7. Decisions

1. **D1 — the fare.** Keep 1d a mile or move to the measured 0.55d. At 0.55d corrected receipts are
   2,970 Simucents a train-kilometre against corrected costs of 3,461 (64.1 per cent of 5,400), or
   117 per cent. **The two corrections overshoot unless the fare cut also raises traffic.**
2. **D2 — a mechanism for traffic expenses.** Station staff, signalmen, porters, clerks and carriage
   repairs are the largest gap (23.7 points). Charging them on stations, on convoys or as a standing
   charge decides whether that gap can close.
3. **D3 — the headquarters.** Whether the £175 a route kilometre a year general charge is a standing
   charge or carried by the building price. No free source gives a head office cost, and the overhead is
   annual, so a nominal building plus the standing charge is the more honest mechanism.
4. **D4 — renewals.** [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §4.4 records that
   renewals belong in the revenue account and the engine books them as capital. That change affects every
   cost-to-revenue ratio here and should precede applying any of them.
5. **D5 — the representative line.** Whether the capital ratio is judged on a rural line, which cannot
   reach Acworth's average, or on an average-mix line assembled for the purpose (M6).

## 8. Measurement questions

1. **M1 — the maintenance conversion.** [balance-conversion-check](balance-conversion-check.md) shows the
   screenshots confirm capital and are silent on maintenance: `maintenance=450` should display 72.00 and
   displays 4.21 and 0.00. Until one controlled reading reconciles that, every maintenance figure here is
   provisional.
2. **M2 — kilometres per game month.** Log the distance one vehicle covers in a game month at
   `bits_per_month = 22`, `meters_per_tile = 125`: it fixes the time compression, and therefore whether
   per-month charges use the capital or the revenue rate.
3. **M3 — `fuel[steam]` unit and basis.** Pithead or delivered, and whether consumption is grammes or
   kilograms. The series equals the pithead price in shillings and the file comment says kilograms;
   both cannot be right. [fuel-evidence](fuel-evidence.md)
4. **M4 — the staff domain (resolved 2026-11-23).** `staff.tab` is now compiled as annual old
   pence × 10/3, with twelve grade series: seven land grades from the 1907 Board of Trade rates, the
   1914-1925 Hansard ranges, the 1962 Hansard standard time rates (1914, 1920, 1930, 1940, 1950,
   1961), the 1946 grades, the New Earnings Survey of April 1980 and the ASHE medians 1999-2026;
   three sea grades from the 18th-century rates, the 1912 able seaman, the 1928-1960 National
   Maritime Board series and ASHE; and two air grades from the 1924, 1954 and 1969 anchors and ASHE.
   The reconstruction and its estimates are in
   [staff-wages/reconstruction](staff-wages/reconstruction.md), and the post-1980 evidence and
   the 2026-2050 projection in [staff-wages/post-1980](staff-wages/post-1980.md). Remaining: the
   1926-1968 fireman/guard rates, the 1981-1998 grade series, sea 1938-1966 and 1981-1989, and air
   1909-1998.
5. **M5 — the residual head.** Railway Returns "repairs to carriages and wagons" and the traffic-expense
   columns, divided by stock and by receipts, would separate the largest gap.
6. **M6 — an average-mix line.** Asset counts by line class from a real company's accounts.

**Untraced figures:** the line's physical definition (17 trains each way, three carriages, 45 per cent
load, one crew-year per train-year); the 14.4 kg a train-kilometre of coal, from a forum row for a
345-ton train and an upper bound here; one station per 5 km; 16 way tiles for double track; the £315 a
route kilometre of signalling, the Rapier 1874 heuristic; and the £28,000 a kilometre of whole-line
capital, inferred from Acworth's 8× and the £3,500 receipts implied by the £175 charge.
