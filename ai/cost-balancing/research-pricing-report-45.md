---
status: draft
verified: New ex-15 @ 70a098c64
---
# Research pass 45 — Multiple-unit maintenance, 1900-2026

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-45.csv`. No workbook, `.dat` or
existing doc was changed.

## 1. What this pass found

1. **A measured modern ladder can be built, but its two modern anchors disagree by a
   factor of 1.4 to 2.2.** RDG's new-EMU rate is £0.44 a vehicle-mile at February 2013
   prices; at 150,000 miles a car-year that is £66,000 nominal, or **£615 in 1900 money**
   (MEASURED). ORR's median passenger-fleet maintenance is **£136,000 a vehicle-year**
   (TSSSA contracts) for 2024-25, or **£888 in 1900 money** (MEASURED). RDG measures new
   stock against a benchmark; ORR measures 87 fleets of all ages, including heavy
   maintenance. The ladder below takes ORR as the fleet average and RDG as the low end.
2. **The recommended ladder, 1900 money per car-year: 66 / 241 / 380 / 510 / 780** at
   1900 / 1950 / 1970 / 1990 / 2020, log-linear between and flat outside. The 1900 point
   is an ESTIMATE (2.0 times the carriage ladder; band 50-66). The 1950, 1970 and 1990
   points are interpolations between the measured anchors at 1961, 2013 and 2024, with the
   1982 Serpell figure used as a weak anchor for 1990. The 2020 point is DERIVED from the
   2013 and 2024 measurements (band 615-888).
3. **The 1961 anchor is £321 a car-year.** The Beeching carrying-unit line (£55.0m for
   46,089 vehicles) with the 1.75 multiple-unit-to-coach factor that report 43 used gives
   £1,771 an MU car-year, or £321 in 1900 money (DERIVED). If DMUs are priced at 1.8 times
   EMUs, the EMU-only figure falls to £290 and the DMU to £522. The 1961 multiple-unit to
   coach ratio (1.75) is therefore below the modern 2.0.
4. **Bente and Roeleveld does not say what the brief says.** The sentence is "With
   loco-hauled trains, traction maintenance is approximately twice as expensive as that
   for coaches." It compares a locomotive with a coach, not a motor car with a trailer
   (STATED). The same article also states "the unit cost for DMUs turned out to be twice
   as high as for EMUs", which is directly usable and agrees with RDG's 1.82
   (£0.80/£0.44). The "traction is twice a coach" ratio is the only published ratio of its
   kind, but it is not a motor-car-to-trailer measurement and this pass does not use it as
   one.
5. **No British source was found that separates motor-car from trailer-car maintenance.**
   Every measured rate found is per vehicle over a whole formation. In the pakset the Class
   158 is formed of three cars, all powered, and the Class 365 of four cars, two of them
   powered. The correct treatment is one ladder per car: the train total is then right,
   while the per-car split is not measured and should not be invented (§5).
6. **The C6 interval is 8 years on Class 158/9, not 5-6.** Northern Trains' contract
   notice of 11 December 2023 states "based on the time between overhaul (8 years)"
   (MEASURED). The 5-6-year figure in the knowledge base has no source found in this pass.
   The 1996 Hansard two-year cycle is loco-hauled coaching stock, not multiple units.
7. **The £180,000 Class 158 and £187,500 Class 365 figures include refurbishment, not
   only the C6.** The Class 365 C6X contract alone was £13m for 160 cars, **£81,250 a
   car** (November 2012, MEASURED); the £30-31m programme added the C4 below the solebar
   and the PRM refresh, giving £187,500 a car. The Inverness Class 158 figure is £9m for
   50 cars, **£180,000 a car**, for "C6+" plus a full interior refit. Using either as the
   routine overhaul price overstates the provision by about 2.3 to 2.5 times.
8. **A 15 per cent, 8-year overhaul rule reproduces the measured C6X.** 0.15 x 8 x £615 =
   £738 against the measured £781 (5 per cent low). The event is 1.2 times the annual
   figure, and the share of the annual figure is 15 per cent. Applying the measured
   £180,000/£187,500 events on a 5-6-year cycle instead implies 47-66 per cent of the
   annual figure: three to four times too high.
9. **The London Underground figure is light maintenance only.** £25,700 (Piccadilly) to
   £52,700 (Central) a car-year in 2009/10 covers cleaning, levels 1-3 and depot equipment
   and excludes programme lift (level 4) and heavy overhaul (levels 5-7) (MEASURED). It is
   a lower bound on that fleet's total maintenance, not on the ladder. The knowledge base's
   "LU 1996 stock £64,700 a car" is a one-off mid-life refurbishment in 2017, not an annual
   cost, and does not belong in a maintenance series.
10. **The generator does not reach most of the multiple units it should.** The
    `is_multiple_unit()` regular expression matches 36 pakset names, mostly pre-1948 EMUs
    and GWR railcars. It does not match `br-158-front`, `BR-365Front`, `BR-465Front` or any
    `*TubeStock*` name. A powered car of those classes takes the locomotive rate of £253 an
    engine-year; an unpowered car takes the carriage ladder. The powered cars of the
    pre-1948 EMUs, by contrast, take the 1892 carriage rate of £32.6. Both results are
    wrong, in opposite directions.
11. **No readable pre-1948 multiple-unit maintenance figure was found.** The named leads
    are in §8. The 1900 point therefore rests on the carriage ladder and a stated ratio,
    not on a measurement of an electric car.

## 2. Method

- **Deflator.** Nominal figures are converted with the `general` series in
  `New/config/prices.tab` (1900 = 100). Checked against the file itself: 1900 100;
  1913 107; 1920 275; 1930 188; 1948 338; 1950 359; 1961 552; 1966 660; 1970 795;
  1982 3,483; 1984 3,824; 1990 5,408; 2009 9,163; 2013 10,725; 2020 12,521; 2024 15,309;
  2025 15,807; 2026 16,281. `prices.tab` states that vehicle maintenance stays on the
  general index (the `vehicle maintenance` line is commented out), so this is the engine's
  own treatment.
- **Three corrections to the deflator list in the brief and in report 43.**
  (i) **1905 is not in the general series** (the series prints 1903 = 101 and 1907 = 102).
  The value 90 at 1905 is the `vehicle purchase` index. A 1905 conversion on the general
  index is an interpolation, about 101.5.
  (ii) **1892 on the general index is 97, not 78.** The value 78 is `vehicle purchase`.
  Report 43's §2 statement "1892 78" is therefore the wrong series, and its 1892 carriage
  value of £42.7 gross / £27.8 net is overstated by about 25 per cent: the correct values are
  **£34.3 gross and £22.3 net** at the 35 per cent renewals share. The workbook's 1900
  carriage point (33) is unaffected because it uses the nominal 1892 figure. Report 43's
  later correction already fixes 1961 from 528 to 552; 552 is correct.
  (iii) **Report 43's §2 list also gives 1920 as 226.** That is `vehicle purchase`; the
  general index is 275. Its 1920 ladder row (61) is an interpolation, so no figure depends
  on it, but the list should not be reused.
- **Grades.** MEASURED = an account, contract or published total with a stated scope.
  STATED = a trade, academic or government statement of a rate without the underlying
  account. DERIVED = my arithmetic from a measured or stated figure, with the chain shown.
  ESTIMATE = my judgement, used only where no measurement exists. UNAVAILABLE = a source
  identified but not readable in this pass.
- **Scope of the ladder.** All maintenance, including routine exams and works overhauls;
  capital, vehicle renewal and capital lease excluded. The modern anchors satisfy this by
  construction: RDG prints maintenance and capital lease as separate lines, and ORR
  collects maintenance cost only (the report is about the maintenance market, not
  leasing). The 1900 point inherits report 43's renewals-excluded carriage basis. No
  renewals deduction is applied anywhere in this ladder. The 30 per cent renewals share in
  `maintenance-decomposition.md` comes from statutory-era "repairs and renewals" heads (the
  Southern EMU figure is from the 1933 accounts) and does not apply to a maintenance
  contract price.
- **Mileage for the per-mile conversions.** 150,000 miles a car-year for the RDG figure,
  the assumption report 43 used; 100,000 miles for the ORR cross-check, close to the
  95,775 miles implied by the ratio of ORR's own medians (£136,000 / £1.42) and to Civity's
  105,000 miles a car for GB commuter fleets. Both conversions are shown wherever the
  answer depends on the choice.
- **Nothing here uses a `.dat` value as a cost.** Pakset names and power ratings are read
  only to describe which branch of the generator a vehicle takes (§6); no price is taken
  from a `.dat` file or used in a ratio.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | Feb 2015 (Feb 2013 price level) | RDG, new EMU | £0.44 a vehicle-mile | "total maintenance costs"; capital lease £0.97, energy and track separate | vehicle-mile | MEASURED | RDG, *LTPRSS* 3rd ed., Table 5; https://www.raildeliverygroup.com/publications/archive/367-2015-03-long-term-passenger-rolling-stock-strategy-3rd-ed/file.html |
| 2 | Feb 2015 (Feb 2013 price level) | RDG, new DMU | £0.80 a vehicle-mile | as row 1; capital lease £1.43 | vehicle-mile | MEASURED | as row 1 |
| 3 | Feb 2015 | RDG, source note | "TOC and ROSCO sources, for new EMU and DMU vehicles, assuming similar annual mileages" | modelled benchmark, not outturn | vehicle-mile | STATED | as row 1 |
| 4 | 2024-25 | ORR, passenger fleets, per vehicle-mile | median £0.72 (TSA first term), £1.42 (TSSSA), £1.73 (in-house), £1.88 (TSA after first term) | maintenance cost incurred by the TOC: labour, spares, materials, depot, technical support, heavy maintenance, overhaul, refurbishment; capital lease out; TARA fleets excluded; 17 TOCs, 87 fleets | vehicle-mile | MEASURED | ORR, *Rolling Stock Maintenance Market Review*, interim, 29 Oct 2026, Figure 4.2; https://www.orr.gov.uk/sites/default/files/2026-10/2026-interim-report-rolling-stock-maintenance-market-review.pdf |
| 5 | 2024-25 | ORR, passenger fleets, per vehicle | median £93,000 (TSA first term), £136,000 (TSSSA), £199,000 (in-house), £285,000 (TSA after first term) | as row 4 | vehicle-year | MEASURED | ORR 2026, Figure 4.3 |
| 6 | 2026 | ORR, cost total | about £1.5bn, 37 per cent of TOC rolling-stock expenditure | maintenance in the year to 31 March 2025 | whole fleet | MEASURED | ORR 2026, para 1.5 |
| 7 | 2009/10 | London Underground, per car | £25,700 (Piccadilly, lowest) to £52,700 (Central, highest); £25,500-£48,100 after normalisation | cleaning and maintenance levels 1, 2 and 3 plus depot equipment; programme lift (level 4) and heavy overhauls (levels 5-7) out; project works out | car-year | MEASURED | TfL Board, 29 June 2011, Item 10, para 189, 194; https://content.tfl.gov.uk/Item10-Board-29-June-2011-RUP-asset-benchmarking.pdf |
| 8 | 2009/10 | London Underground, Northern line | costs include "an annualised proportion of programme lift and heavy overhaul", plus depot track and signal maintenance | not comparable with row 7 | car-year | MEASURED | TfL 2011, para 196 |
| 9 | 2009/10 | London Underground, Piccadilly line | maintenance regime "based on hours operated and not calendar days" | scheduled maintenance trigger | n/a | STATED | TfL 2011, para 199 |
| 10 | 2009/10-2017/18 | London Underground, unit-rate change | -£15,800 a car (BCV), -£10,600 (SSL), +£3,000 (Tube Lines) | levels 1-3 basis | car-year | MEASURED | TfL 2011, Part A para 42-43 |
| 11 | 26 Nov 2012 | Eversholt/Railcare, Class 365 C6X | £13m for 40 four-car units = **£81,250 a car** | C6X overhaul only | per car, one event | MEASURED | https://eversholtrail.co.uk/news/eversholt-rail-awards-13million-contract-to-railcare/ |
| 12 | 5 Jul and 20 Nov 2013 | Eversholt, Class 365 enhancement and heavy maintenance | £31m, then "in excess of £30m", for 40 four-car units = **£187,500 a car** | C6X above the solebar + C4 below it (bogies to Crewe) + interior refresh + PRM works | per car, one event | MEASURED | https://eversholtrail.co.uk/news/eversholt-rail-awards-contract-to-bombardier-transportation/ |
| 13 | 5 Feb 2014 | *RAIL* 741, Class 365 scope | C6X above the solebar and a C4 below it; 20 days a unit | scope confirmation for row 12 | n/a | STATED | https://www.railmagazine.com/news/fleet/first-refurbished-networker-back-in-traffic-with-fcc |
| 14 | 2007-08 | Inverness Class 158 "C6+" | £9m for 25 two-car units = **£180,000 a car** | C6+ classified overhaul plus full interior refit, seating, lighting, toilets, PRM | per car, one event | MEASURED | http://www.scot-rail.co.uk/page/Inverness+Class+158+Refurbishment |
| 15 | 11 Dec 2023 | Northern Trains, Class 158/9 C6 | "based on the time between overhaul (8 years)" | C6 scope: air system, brakes, bodywork, battery, control, flooring, HVAC, interior, fuel, doors, underframe, water and toilet | years | MEASURED | https://www.find-tender.service.gov.uk/Notice/036434-2023 |
| 16 | 11 Mar 1996 | Hansard, coaching-stock overhaul | examinations at 3-4 days, 1, 3, 6 and 12 months; full overhaul "approximately every two years" | loco-hauled coaching stock, not multiple units | vehicle | STATED | https://hansard.parliament.uk/Commons/1996-03-11/debates/3523c0ba-a67a-4c8e-bb28-bb2605561e75/Railways(RollingStockMaintenance) |
| 17 | 2005 (published 1 Apr 2006) | Bente and Roeleveld, DMU against EMU | "the unit cost for DMUs turned out to be twice as high as for EMUs" | daily cleaning to regular light and intermittent heavy maintenance | vehicle-km | STATED | https://www.railwaygazette.com/news/2006/04/01/benchmarking-identifies-good-practice-in-rolling-stock-maintenance/ |
| 18 | 2005 | Bente and Roeleveld, traction against coaches | "With loco-hauled trains, traction maintenance is approximately twice as expensive as that for coaches" | locomotive against coach, not motor car against trailer | vehicle-km | STATED | as row 17 |
| 19 | 2005 | Bente and Roeleveld, sample | 12 operators, about 8,000 vehicles, about 50 types; utilisation "from under 100000 km to well over 200000 km per vehicle per year" | sample description | n/a | STATED | as row 17 |
| 20 | 1961 | Beeching, multiple units, carriages and parcels vans (not re-read in this pass) | £55.0m | "provision, maintenance, stabling and servicing"; capital provision may be inside | 46,089 vehicles, of which 11,032 MU cars (6,958 EMU, 4,074 DMU) | MEASURED (via report 43) | *The Reshaping of British Railways* (1963), p. 6 and Appendix 3; via report 43 rows 4-11 |
| 21 | 1961 | Multiple-unit car at 1.75 times a coach | £1,771 nominal = **£321** in 1900 money | as row 20 | car-year | DERIVED | row 20; report 43 §4 |
| 22 | 1961 | EMU-only and DMU-only at a 1.8 DMU premium | £1,602 EMU = **£290**; £2,884 DMU = **£522** | as row 20, with the DMU premium from row 17 | car-year | DERIVED | rows 17, 20 |
| 23 | 1982 | Serpell, total vehicle maintenance divided by an assumed 50,000 vehicles | £473m / 50,000 = £9,460; x1.75 = £16,555 = **£475** | day-to-day, light, intermediate and general repairs, all vehicle types | car-year | DERIVED | report 43 row 14; *Railway Finances* (1983), para 6.44 |
| 24 | 2013 | RDG EMU converted at 150,000 miles | £66,000 nominal = **£615** | as row 1 | car-year | DERIVED | row 1 |
| 25 | 2013 | RDG EMU converted at 100,000 miles | £44,000 nominal = **£410** | as row 1 | car-year | DERIVED | row 1 |
| 26 | 2024 | ORR medians in 1900 money | £607 to £1,862 a vehicle-year; the per-mile medians convert to £470 to £1,228 a vehicle-year at 100,000 miles | as rows 4-5 | car-year | DERIVED | rows 4-5 |
| 27 | 2009/10 | London Underground in 1900 money | £280 to £575 a car-year, light maintenance only | as row 7 | car-year | DERIVED | row 7 |
| 28 | 2012 | Class 365 C6X in 1900 money | **£781** a car, one event | as row 11 | per event | DERIVED | row 11 |
| 29 | 2008 | Class 158 C6+ in 1900 money | **£1,954** a car, one event | as row 14 | per event | DERIVED | row 14 |
| 30 | 1926-29 | LBSCR overhead AC stock against DC motor coaches | maintenance costs of the AC stock "considerably exceeded those for the DC motor coaches" | qualitative comparison, no figure; tertiary source | n/a | STATED | https://everything.explained.today/Electrification_of_the_London_and_South_Western_Railway/ |
| 31 | 1950 | Warder, *Electric traction prospects for British Railways*, Table VI | two coaching-stock maintenance totals, £21,008,000 and £21,037,000 | Southern Region steam against electric coaching stock; discussion only, paper not readable | n/a | UNAVAILABLE | https://steamindex.com/jile/jile41.htm |
| 32 | 1950 | Barton, *The maintenance of electric rolling stock* | "notes on cost" | London Transport Executive and Great Indian Peninsula Railway | n/a | UNAVAILABLE | https://digital-library.theiet.org/doi/10.1049/pi-1a.1950.0042 |
| 33 | 1933-47 | LPTB annual reports and accounts | working expenses and rolling-stock statistics | not digitally readable in this pass | n/a | UNAVAILABLE | https://tfl-2.access.preservica.com/index.php?name=SO_7a7c172b-5b28-4840-b1aa-8b32ad48c3c3 |
| 34 | 1928-30 | Frank Pick, memoranda on the cost of maintenance of rolling stock | archive series identified | not readable online | n/a | UNAVAILABLE | https://etheses.whiterose.ac.uk/id/eprint/21536/1/20180918-Mind_The_Muncipal_Gap.pdf |

## 4. The series

**1961: what the £55.0m can support.** Beeching's line covers 35,057 coaches and 11,032
multiple-unit cars on one definition. Report 43's 1.75 multiple-unit-to-coach factor gives
£1,771 an MU car-year, or £321 in 1900 money (DERIVED from two measured counts and one
stated factor). Separating the DMU premium (1.8 times EMU) gives £290 EMU and £522 DMU; the
blend scarcely moves, so the split does not matter for a fleet-average ladder.

**1982: a weak anchor, not a measurement.** Serpell's £473m, at an assumed 50,000 vehicles
and 1.75 times the fleet average, gives £475 a car-year in 1900 money. Both assumptions are
report 43's and neither is measured. It is the anchor for 1990 because no multiple-unit
figure exists in that decade; without it, 1990 would interpolate at £460, which would make
a multiple-unit car cost exactly a carriage. It sits 14 per cent above a direct 1961-2013
interpolation (£417 at 1982), so it moves the 1990 point by 10 per cent, not by more.

**The modern anchors.** RDG's £0.44 is a benchmark for new stock at February 2013 prices.
ORR's £136,000 is the median outturn across 87 fleets in 2024-25, including heavy
maintenance and overhaul. Converting both and comparing: at 150,000 miles RDG gives £615
and ORR £888, a ratio of 1.44; at 100,000 miles RDG gives £410 and ORR £928, a ratio of
2.26. The lower the mileage assumption, the wider the disagreement. The ladder's 2020
point of £780 sits between them and closer to ORR, because the pakset's fleet is a fleet
average (ORR's basis), not a fleet of new trains (RDG's basis).

**The series.** Values in 1900 money, per car-year. "Interpolated" rows are log-linear
between the measured anchors and are ESTIMATE.

| Date | Nominal | 1900 money | Grade | Basis |
|---|---|---|---|---|
| 1900 | £66 | 66 | ESTIMATE | 2.0 x the carriage ladder of 33 (band 50-66) |
| 1950 | £865 | 241 | ESTIMATE | interpolation 1900-1961 |
| 1961 | £1,771 | 321 | DERIVED | Beeching; MU at 1.75 x coach |
| 1970 | £3,021 | 380 | ESTIMATE | interpolation 1961-1982 through the weak anchor |
| 1982 | £16,555 | 475 | DERIVED | Serpell, two assumptions (weak anchor) |
| 1990 | £27,581 | 510 | ESTIMATE | interpolation 1982-2013 |
| 2013 | £66,000 at 150,000 miles | 615 | MEASURED input, DERIVED conversion | RDG new EMU |
| 2020 | £97,664 | 780 | DERIVED | interpolation 2013-2024 (band 615-888) |
| 2024 | £136,000 | 888 | MEASURED input, DERIVED conversion | ORR TSSSA median |

**The ladder.**

| Era | Value | Grade | Anchor |
|---|---|---|---|
| 1900 | 66 | ESTIMATE | 2.0 x the carriage 1900 value |
| 1950 | 241 | ESTIMATE | interpolation; the 1961 anchor constrains it |
| 1970 | 380 | ESTIMATE | interpolation between 1961 and the 1982 anchor |
| 1990 | 510 | ESTIMATE | interpolation between the 1982 weak anchor and 2013 |
| 2020 | 780 | DERIVED | 2013 RDG and 2024 ORR medians |

**What the series shows.** The multiple-unit car costs about 1.7 to 2.0 times a carriage
throughout: 2.0 in 1900, 1.75 in 1961, 1.11 against report 43's 1990 carriage value of
460 and 1.77 against its 2020 value of 440. The near-constant multiple is the strongest
internal check available: two independently built ladders agree on the shape, and the
traction premium is roughly constant in real terms. In absolute terms the multiple-unit
car rises 11.8 times between 1900 and 2020, against 13.3 times for the carriage.

**What it does not show.** No point between 1900 and 1961 is measured. The 1900 point is a
ratio, not a measurement. The 1950, 1970 and 1990 points are interpolations with no
independent check except Serpell at 1982. The pre-1948 electric car is therefore the
weakest part of the ladder, and the pakset's stock in that era spans two incompatible
technologies: the LBSCR overhead AC cars, whose maintenance "considerably exceeded" the DC
cars (row 30), and the DC third-rail cars of the LSWR, LOR, MSJ&A, L&Y, NER and Mersey.
One ladder cannot separate them.

## 5. Recommended rule for the workbook

**The ladder, 1900 money per car-year, all maintenance including overhauls, capital and
renewals excluded:**

```python
MU_MAINT_LADDER = ((1900, 66.0), (1950, 241.0), (1970, 380.0), (1990, 510.0), (2020, 780.0))
```

Read with `interp_log()`, flat before 1900 and after 2020.

**Per-vehicle-mile alternative.** Use it only where a per-mile figure is required, and
carry the fixed part separately:

| Date | Figure | Grade | Note |
|---|---|---|---|
| 2013 | £0.44 a vehicle-mile, new EMU; £0.80 new DMU | MEASURED | RDG; capital lease, energy, track excluded |
| 2024-25 | £0.72 / £1.42 / £1.73 / £1.88 a vehicle-mile by contract type | MEASURED | ORR medians, 17 TOCs, 87 fleets |
| 2005 | DMU 2.0 times EMU | STATED | Bente and Roeleveld; RDG implies 1.82 |

The ladder at 100,000 miles is £1.36 a vehicle-mile in 2024 money (£0.00888 in 1900
money), against ORR's £1.42 median: the per-year ladder and the per-mile measurement agree
to 4 per cent at that mileage. A pure per-mile rule undercharges low-mileage fleets
because it drops the fixed part; the ORR report says the same in words ("fixed costs can
make smaller or less intensively utilised fleets appear more expensive per mile").

**Powered car against trailer car.** No split. Apply the ladder to every car of the
formation. This is not a claim that a motor car costs the same as a trailer; it is a
statement that no British source separates them, and that every measured rate found is per
vehicle over a whole formation. Applying the average to all cars gets the train total right
and the per-car distribution wrong. A split would need a measured motor-to-trailer ratio,
which does not exist in the sources read here (UNAVAILABLE). If one is forced, the capital
ratio of about 1.2-1.4 is an ESTIMATE, not evidence.

**DMU premium.** The measured premium is 1.8 (RDG, 2013) to 2.0 (Bente, 2005). If the
workbook distinguishes DMUs by name, multiply the DMU car by **1.8** (band 1.8-2.0) and
leave EMU cars at 1.0. Caution: the 1961 anchor is a blend that already carries a premium
for its 4,074 DMU cars; applying 1.8 on top of the ladder without reducing the EMU side
will overstate a fleet with the 1961 proportion of DMU cars (37 per cent) by about 30 per
cent. If that matters, use the EMU-only 1961 value of £290 as the anchor and apply 1.8 to
DMUs.

**Fixed and per-kilometre split.** The split is not measured. The working rule is **50 per
cent fixed and 50 per cent per kilometre at a reference 100,000 miles (161,000 km) a
car-year**, the knowledge base's existing rung-2 estimate. Its only independent check: at
that mileage a 50/50 split of the 2020 value implies a per-mile rate of £0.488 in 2020
money, 5 per cent below the RDG rate of £0.44 (2013) deflated to 2020 (£0.514). The check
supports the 50/50 split at that mileage and says nothing about other mileages. In the
generator:

```
fixed_gbp_yr = 0.5 * ladder(era)
perkm_gbp   = 0.5 * ladder(era) / 161000
```

The fixed share then falls as mileage rises (62 per cent at 60,000 miles, 40 per cent at
150,000). The engine has one fixed and one per-km field per vehicle, so the split must be
struck at the class's assumed mean annual distance, which is still an open decision in
`maintenance-decomposition.md`.

**Overhaul share and interval.** Recommend **15 per cent of the annual ladder as the
overhaul provision, an event of 1.2 times the annual figure, every 8 years** (1,290,000 km
at 161,000 km a year) for 2000 onwards. Before 2000, use 6 years (966,000 km) and before
1948, 5 years (805,000 km), both ESTIMATE: no measured multiple-unit C6 interval was found
before the 2023 Class 158/9 notice. The 15 per cent / 8-year rule reproduces the only
measured pure C6X price: 1.2 x £615 = £738 against £781 (row 28), 5 per cent low. It is
also consistent with the £180,000 Class 158 event being a refurbishment: that event is 2.8
times a routine C6 at the same date, so about two-thirds of its price is interior work.

**Renewals.** None deducted. The ladder is a maintenance figure; the modern anchors exclude
capital lease and vehicle renewal by construction, and the 1900 point is built on report
43's renewals-excluded carriage basis. The 30 per cent multiple-unit renewals share in
`maintenance-decomposition.md` belongs to statutory-era "repairs and renewals" heads and
must not be applied to this ladder.

**London Underground.** Use the same EMU ladder, with no separate LU factor. The only LU
measurement is light maintenance (£280-£575 in 1900 money, 2009/10), which is 47 to 97 per
cent of the mainline EMU ladder at that date. The top of that range equals the whole
mainline figure, so the LU evidence supports neither a separate level nor a discount: it is
consistent with intensive duty and a depot overhead, and does not justify a different
ladder.

## 6. What this changes in the generator and the workbook

1. **`New/ai/cost-balancing/evidence_data.py` line 775.** `CARRIAGE_MAINT_YR = 32.6` now
   has one reader, line 1264, inside the multiple-unit branch, and the comment already says
   "retained for the multiple-unit branch". Replace line 1264's
   `maint_gbp_yr=CARRIAGE_MAINT_YR` with
   `maint_gbp_yr=round(interp_log(MU_MAINT_LADDER, yi or 1900), 1)`. After that change the
   constant has no reader and can be deleted. Add `MU_MAINT_LADDER` beside
   `CARRIAGE_MAINT_LADDER` and `WAGON_MAINT_LADDER` (lines 783-784).
2. **`evidence_data.py` line 1241, the `is_multiple_unit()` branch.** The predicate
   (lines 463-464) matches `dmu|emu|demu|railcar|apt|multiple.?unit|tyneside-unit`. It
   catches 36 names, almost all pre-1948 EMUs (`LSWR-EMU(front)`, `LOR-EMU(front)`,
   `LMS-EMU-driving-motor`, `Mersey-EMU(front)`, `MSJ&A-EMU-driving-motor`,
   `L&YR-EMU-driving-motor`, `LNER-1937-Tyneside-EMU-front`) and the GWR railcars. It does
   **not** catch `br-158-front`, `BR-365Front`, `BR-465Front`, `1938TubeStockFront`,
   `1903TubeStockFront` or any other `*TubeStock*` name (all of these have a power rating
   above zero). Those cars take the locomotive branch (line 1249 for the power test,
   lines 1318-1321 for the rate) and get `LOCO_MAINT_YR = 253` and `LOCO_REPAIR_PERKM`;
   their unpowered cars (`BR-365Power`, `1938TubeStockTrailer`) fall to the carriage branch
   and get the carriage ladder. The predicate must be widened (for example `tube.?stock` plus the named BR
   classes, or a maintained list) before the new ladder can reach the stock it is for.
   **This is the larger error of the two**: most modern multiple units are currently priced
   as locomotives, while the pre-1948 ones are priced as 1892 carriages.
3. **`evidence_data.py` line 1264-1265, the `perkm_gbp` field.** The multiple-unit branch
   sets only `maint_gbp_yr`; it sets no `perkm_gbp`. Add
   `perkm_gbp=round(0.5 * ladder / 161000.0, 8), perkm_year=1900` so the 50/50 split is
   carried. The carriage branch has the same gap; that is report 43's business, not this
   pass's.
4. **`evidence_data.py` line 1105, `OVERHAUL_PROFILE['multiple-unit']`.** Currently
   `(0.04, 0.20, 3, 300000.0, 0.4, 0.30)`: 4 to 20 per cent of capital, three steps to the
   maximum, 300,000 km between overhauls. Recommended: `(0.08, 0.08, 1, 1290000.0, 0.4,
   0.30)` for 2000 onwards (a flat 8 per cent event, one step, 1.29m km, 0.4 months out of
   service), with 966,000 km before 2000 and 805,000 km before 1948. The 8 per cent is 8.2
   per cent of the generator's multiple-unit capital of £9,500 (its last ladder point,
   1982), which happens to reproduce the measured £781 event. It is fragile: if the
   multiple-unit capital ladder is extended past 1982, the share must be recomputed as
   1.2 x annual maintenance / new capital. The overhaul is better expressed as an absolute
   1.2 x the ladder than as a share of a frozen capital figure. The profile is one tuple for
   all eras, so era-specific intervals need either three keys or a per-vehicle override.
   `overhaul_profile()` at line 1138 uses the same predicate, so the predicate fix in item
   2 also moves `br-158-*`, `BR-365*` and the tube stock from the carriage profile to the
   multiple-unit profile.
5. **`New/cost-balancing-maintenance.xlsx`, sheet "Rail vehicles", multiple-unit rows.**
   Column **Q** ("Measured fixed (GBP/yr)") takes half the ladder; column **AA** ("Class
   fixed (GBP/yr)") follows the class ladder; the derived columns **S** (GBP @1900), **T**
   (SC @1900/month), **U** (suggested .dat fixed) and **AE** (basis) follow. The basis text
   must name RDG Table 5 and ORR Figures 4.2-4.3, not Hill 1892.
6. **`New/cost-balancing-capital.xlsx`, sheet "Overhauls & upgrades", multiple-unit rows.**
   Interval 8 years (1.29m km), share 8 per cent of capital or 1.2 x annual maintenance,
   replacing the 5-6-year/£180,000-£187,500 reading. The two measures in
   `maintenance-decomposition.md` (the "Overhaul values by class" table and the
   "Multiple units" bullet) both need the corrected interval and the corrected event
   scope.

## 7. Error bars and assumptions

| Quantity | Central | Band | Why |
|---|---|---|---|
| 1900 multiple unit | 66 | 50-66 | ratio only; 1.5x or 2.0x the carriage |
| 1950 | 241 | 229-241 | interpolation; insensitive to the 1900 choice (5 per cent) |
| 1961 | 321 | 290-321 | 1.75 factor and the DMU-premium treatment |
| 1970 | 380 | 340-420 | no measurement; the 1982 weak anchor constrains it |
| 1982 weak anchor | 475 | 330-620 | fleet count 40,000-60,000 and MU multiple 1.5-2.0 |
| 1990 | 510 | 460-510 | interpolation; 460 without the 1982 anchor |
| 2013 | 615 | 410-615 | RDG mileage 100,000-150,000 |
| 2020 | 780 | 615-888 | RDG benchmark against ORR outturn |
| overhaul share | 15% | 10-20% | one measured C6X price, one interval |
| fixed share at 100,000 miles | 50% | 35-65% | no measured split; RDG check only |

**Structural assumptions.** (i) The multiple-unit car's maintenance tracks the carriage's,
so the 1900 point inherits every error in report 43's carriage 1900 value (itself a nominal
1892 figure kept at 33, where the deflated value is 34.3 gross and 22.3 net). (ii) The 1961
anchor treats the Beeching line as maintenance, although report 43 shows at most 78 per
cent of the functional total is the maintenance account line; the anchor is therefore an
upper bound. (iii) The modern anchors exclude capital, but ORR's figure includes heavy
maintenance and technical support while RDG's benchmark may not; the 2020 point is
deliberately placed nearer ORR. (iv) The 8-year interval is measured on one fleet (Class
158/9); other fleets may run 5-6 years, at which interval the same 15 per cent share gives
an event of 0.75-0.9 times the annual figure, or the same 1.2-times event gives a share of
20-24 per cent.

## 8. Gaps

- **No measured pre-1948 multiple-unit figure.** Named and not readable in this pass:
  Warder's 1950 Table VI (two Southern Region coaching-stock totals, £21.0m each, with no
  vehicle counts in the discussion); Barton's 1950 IEE paper (paywalled, "notes on cost"
  confirmed in the abstract); the LPTB annual reports 1933-47 (TfL corporate archive,
  Preservica, not retrievable as text); Frank Pick's 1928-30 memoranda on the cost of
  maintenance of rolling stock (TfL archive, identified in a York thesis). The next route
  is the Board of Trade *Returns of Railway Companies*, Abstract B, which itemises repairs
  and renewals and, for some companies, electric traction separately; those volumes were
  not searched in this pass.
- **No measured motor-to-trailer split.** RDG, ORR, LU and the two overhaul contracts are
  all per vehicle over a formation. A works cost sheet separating motor bogies, traction
  equipment and bodywork would close it.
- **No measured BR-era multiple-unit overhaul interval.** The 8-year figure is 2023 Class
  158/9. The 5-6-year figure in the knowledge base has no source. BR's C1-C6 instruction
  cards for multiple-unit stock (1965-66) would give it.
- **The two modern sources disagree by 1.4-2.2 times.** ORR's final report (not yet
  published at the date of this pass) and a published ORR regression coefficient on
  mileage would let the fixed/per-km split be measured rather than assumed.
- **No measured pre-1948 diesel railcar cost.** The GWR railcars are the obvious case; the
  GWR's own cost statements or the *Great Western Railway Magazine* 1936-39 would carry
  it.
- **No multiple-unit capital ladder after 1982.** The overhaul share can only be expressed
  against capital if that ladder is extended; until then the event must be absolute.
