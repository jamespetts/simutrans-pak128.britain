---
status: draft
verified: New ex-15 @ 687347620 (working tree), 2026-11-24
---
# Vehicle maintenance decomposition

**Covers**: how every vehicle class's measured maintenance and upgrade evidence is decomposed
into the engine's money fields — `runningcost` (per km), `fixed_cost` (per month), the overhaul
fields (`max_distance_between_overhauls`, `initial_overhaul_cost`, `max_overhaul_cost`,
`overhauls_before_max_cost`, `overhaul_month_tenths`) and `upgrade_price` — and the estimation
protocol where measurement fails. Read before entering any vehicle maintenance, overhaul or
upgrade figure at the costing pass. Engine mechanics:
[vehicle-cost-model](../vehicle-cost-model.md); evidence:
[base-maintenance](base-maintenance.md), [vehicle-cost-evidence](../vehicle-cost-evidence.md);
the research record: [research-pricing-report-39](../cost-balancing/research-pricing-report-39.md)
and the pass-40 reports in [cost-balancing](../cost-balancing/).

## Standing rules

1. **The current `.dat` values are not a basis for anything.** They are pre-calibration and will be
   replaced wholesale at the costing pass ([cost-balancing-register](../cost-balancing-register.md)
   "How to read"). Whatever the present balance does with a field — including charging carriage
   maintenance as fixed only — sets no precedent for the new values.
   `[USER-DIRECTION:2026-11-24]`
2. **Horses and sailing boats take no per-km figure.** Their upkeep is standing cost (horse keep;
   hull, rig and gear decay): `runningcost` 0, everything in `fixed_cost`. This does **not** exempt
   them from overhauls: a horse's overhaul is its **replacement at the end of its working life, at
   100% of the purchase price** (measured renewal cadence: the Leeds tramway horses were renewed
   about once every 7 years at cost equal to the purchase price, 1894-5 accounts), and horse
   vehicles are rebuilt like any other vehicle. `[USER-DIRECTION:2026-11-24]`
3. **Every estimated figure carries its basis and its directionality**: what evidence would move
   it, and in which direction. Directly measured figures win over estimates whenever both exist.
   `[USER-DIRECTION:2026-11-24]`
4. **Overhaul and maintenance intervals are per class AND per era**, never universal: one class's
   interval is not a default for another (LMS practice, for example, ran long), and one era's is
   not a default for another (a Victorian four-wheeler and a Mk 3 do not share an overhaul cycle).
   Where a class or era has no measured figure, estimate from its archetype and era band with the
   scaling basis recorded. `[USER-DIRECTION:2026-11-24]`

## What the engine charges (summary; full: vehicle-cost-model)

- `runningcost` per whole vehicle-km; `fixed_cost` per game month, whether or not the vehicle
  moves. At the pakset settings the monthly charge is doubled and `runningcost` is not, so the
  split entered in the fields is not the split the player experiences (vehicle-cost-model
  "Consequences for calibration").
- **Wear ramp**: between overhauls the charged running cost rises from the base toward
  `max_running_cost` (default 3x base) as kilometres accumulate, and the ramp reaches the monthly
  charge too. **Obsolescence ramp**: from the retirement date, running and fixed charges rise to
  `increase_maintenance_by_percent` (default 400%) over 20 years.
- **Overhauls**: charged as events when `km_since_last_overhaul` exceeds
  `max_distance_between_overhauls` (0 disables); cost from `initial_overhaul_cost` rising on a
  sigmoid to `max_overhaul_cost` over `overhauls_before_max_cost`; booked as vehicle maintenance.
- **Upgrades**: replacing a vehicle with a newer type charges the TARGET's `upgrade_price` (default
  = the new vehicle's `cost`); the old vehicle is deleted with no resale credit. `upgrade_price` is
  indexed on the `vehicle maintenance` series while `cost` uses `vehicle purchase`
  ([engine-bugs](../engine-bugs.md)).

## The decomposition identity

For a class with measured life-average maintenance **T** per vehicle-year (repairs **and renewals**,
as the accounts state it):

```
T = rho + O + R
O = (overhaul cost share of new price x new price) / overhaul interval in years
R = 12 x F + V x k        (k = class mean annual kilometres)
```

- **rho — renewals provision** per vehicle-year. A vehicle renewal is the player's capital
  repurchase in-game, so rho is **netted out** of the maintenance fields and left to `cost` and the
  player's replacement decision. Measured (report 40 §2): **wagons ≈50% (40-60), carriages ≈35%
  (25-50), locomotives ≈25% (20-30; complete renewals only), MUs ≈30%, trams 30-50% of the
  car-only head; buses, lorries and aircraft 0%** — CM, municipal and CAA-style maintenance
  figures exclude depreciation by convention (it is a separate line in the same tables). Lives:
  wagons 30-35, carriages ≈40, locos 25-30, MUs 25-40, bus 12-15, lorry 6-8, tram 25-35, ship
  25-30, aircraft 20-25 years. Two cautions: Price Williams's "money life" is a payback
  coefficient, not a service life, and his £139.91 an engine-year is a component-renewal schedule
  (repairs + partial renewals), not the capital share; and "Transfer to Renewal Account" provisions
  sit on top of actual renewals in the statutory accounts.
- **O — overhaul events.** Charged through the overhaul fields, so O is netted out of R. The
  overhaul shares and intervals of the `Overhauls & upgrades` sheet are the current evidence.
- **R — routine remainder**, split into `fixed_cost` (F) and `runningcost` (V).

**Wear-ramp correction.** The engine ramps the charged figures from base toward
`max_running_cost` over the overhaul cycle and the ramp reaches the monthly charge. If the fields
are entered at (F, V), the charged life-average is `m x (12F + V k)` where m is the mean ramp
multiplier over the cycle (m = 2 at the default linear 1-to-3 ramp). Therefore either:

- **(a) Enter the mid-cycle level**: base fields = (F, V) / m with `max_running_cost` at the
  default 3x, keeping the ramp as the in-game deterioration shape; or
- **(b) Enter the life-average and set `max_running_cost = runningcost`** (flat within a cycle),
  leaving all deterioration to the overhaul events and the obsolescence ramp.

Which option a class takes is recorded per class below; where a class has measured intra-cycle
deterioration (locomotives rise sharply into a heavy general), (a) is preferred; where the
intra-cycle shape is unknown, (b) is the conservative choice because it cannot misstate the
average. `[USER-DIRECTION: pending]` — this choice is open for the costing pass.

## Estimation protocol (used when no measured split exists)

In order of preference; each estimate records which rung it rests on:

1. **Measured split** for the class (cost functions, contracts, account heads).
2. **Neighbouring-class transfer** with a stated reason (e.g. MU from modern light-rail contracts).
3. **Component decomposition**: distance-worn components (wheelsets and tyres, axle bearings,
   brake gear, engine internals) against time-worn components (paint, roof, body and frame decay,
   corrosion), priced as shares of the vehicle and dated by their renewal lives.
4. **Utilisation scaling**: where a per-vehicle-mile and a per-vehicle-year figure both exist for
   the same fleet, the pair identifies F and V directly (V = per-mile figure, F = remainder).
5. **Analogical prior** (e.g. aircraft airframe reserves for ships): last resort, labelled as such.

Every estimate states: the rung, the arithmetic, the confidence, and **what would move it and in
which direction** (e.g. "a wagon overhaul invoice would raise O and lower R; it would not change
the F/V split").

## Overhaul values by class (O)

Interval and cost share of the vehicle's new price. The engine's interval field is in kilometres,
so each year-interval converts at the class's mean annual km: `interval_km = interval_years x k`
(k decision below). Rung and direction for every row: report 40 §1-§1.5.

| Class | Interval | Share (initial -> max) | Basis | What would move it |
|---|---|---|---|---|
| Rail wagons | 6 yr (5-7) | 12% -> 20% | composed (rung 3): 7-year repair-contract terms, 4-6-year POH analogue, reconciled with measured £5-£5 8s 6d a wagon-year contracts (3.2-4% of new a year) | RCH per-job schedules (Chasewater 4778) or a wagon overhaul invoice; share could sit 8-25% |
| Rail carriages | **per era** — see the era-band table below | 8% -> 27% (BR Mk 1 band; Victorian measured at 25%) | Hansard 11 Mar 1996 (2-yr cycle, BR); Mk 1 works overhaul 1982 ≈8%; Lacy & Dow 25% (1850s-60s) | era-band research in flight |
| Steam locomotives | **per class** — see the archetype table below | 5% -> 15% (heavy general measured at 9-14% for GWR 28xx; share likely scales with class size) | GWR 28xx record card (IR yr 2, HO yr 6.5, HG yr 13-14); Fowler 1913 heavy/light scope definitions; Stanier's practice (JILocoE 43); Bond Table IV per-class values | per-class values reported (report 40 §1.8) — to be applied per row |
| Diesel/electric locomotives | 2.75 yr, heavy at 11 yr | 7% -> 20% | Hansard 11 Mar 1996 (M) intervals; shares provisional | Kew: COAL 101/164, AN 88/108, AN 112 standard charge schedules |
| Multiple units | 5-6 yr (classified C6 cycle) | £ measured: 158 C6+ £180,000; 365 £187,500; LU 1996 stock £64,700/car; % awaits the MU purchase ladder | report 40 §1.3 | MU ladder (report 39 §3) gives the denominator |
| Buses | 4 yr (220,000 km) | 25% -> 40% | Aldenham £2,000 (1965) = 25-33% of a new double-decker (M) | further municipal overhaul accounts |
| Lorries | engine exchange 100,000-250,000 mi; complete overhaul 250,000 mi | 10% -> 30% | CM 1960/61/69: Cummins ReCon £394-473, Ford £39 exchange units (M) | maker overhaul schemes (Gardner scheme unpriced) |
| Trams | 12 yr (600,000 km) | 8% -> 45% | Metrolink mid-life £80,000; Supertram life extension £856,000 (KB); E/1 class £400 a tram (1934); Feltham about £300 against a £500 secondhand price (1949) | pre-1950 municipal overhaul accounts |
| Ships | 5 yr special survey | 2% -> 5% (bare survey + dock under 1.5%; with steel renewal 3-9%) | US National Academies tanker data; Hellenic Chamber provision (report 40 §1.5); "Earl of Essex" overhauled with new boilers £1,100 against £4,154 new (1877, ≈26%) | Drewry/Lloyd's repair records (paywalled) |
| Aircraft | heavy check in a 6-check cycle; 6-10 yr | 2.5% -> 5% (airframe heavy check 0.8-1.1%; with engines and gear 2-5%) | Aircraft Commerce 777 guide; D-check 50,000+ man-hours (report 40 §1.5) | engine shop-visit prices in lessor filings |
| **Comet 1** (special case) | replacement of the fatigue-doomed airframe ≈1,000 pressurisation cycles | 1,790,000 km = 1,000 cycles × the measured BOAC mean sector 1,790 km (sector-dependent: shorter sectors reach the limit sooner per km) | **67% -> 67%** (band 65-75; engines, avionics and interior are salvaged — user direction 2026-11-24 revised) | M + EST: fatigue failures at 903-1,286 pressurisations (C.A.P. 127; FAA ≈1,000; design assumption 10,000); salvage = engines 25-30% + avionics 8-10% + interior 7-10% less 8-12% extraction and refit. **Comet 4 and 1XB excluded** (report 40 §1.10). Direction: a Ghost engine unit price |
| Narrow gauge, maglev | analogue of nearest class | analogue | rung 5 | any measured narrow-gauge overhaul |
| Horses (the animals) | 7 yr (Leeds renewal cadence) | 70,000 km at an assumed 10,000 km/yr | **100% -> 100%** — the overhaul is the replacement at the end of working life | M: renewed about once every 7 years at cost = purchase price (1894-5 accounts, forum 6521 #116) |
| Horse vehicles (carts, omnibuses, coaches, wagons) | 5 yr (EST) | 50,000 km at an assumed 10,000 km/yr | 15% -> 30% (EST) | rebuilding wheels, axles, springs, bodywork and paint; Lacy & Dow 25% carriage analogue. Moves: coaching/omnibus accounts |
| Motor trailers and articulated bus sections | lorry cadence | 160,000 km | 10% -> 25% (EST) | the lorry bands without the engine element |
| Sailing craft, inshore/coastal (barges, wherries, brigs, schooners) | 5 yr (EST) | 175,000 km at an assumed 35,000 km/yr (k-dependent) | 5% -> 15% (EST) | hull, rig and spar refits; "Earl of Essex" overhaul 26% at 18 years as the analogue; refit share carved OUT of the Martin 5% provision. Moves: RMG barque accounts |
| Sailing ships, deep-sea (clippers, windjammers, Blackwall frigates, barques) | 5-yr Lloyd's survey cycle (as steamers) | 500,000 km at an assumed 100,000 km/yr ocean-trade duty (k-dependent) | 3% -> 10% (EST) | classed vessels surveyed like motor ships minus the machinery share; between the motor-ship and wooden-refit bands |

Notes:

- The engine's single interval plus the sigmoid (`initial_overhaul_cost` rising to
  `max_overhaul_cost` over `overhauls_before_max_cost`) collapses an event ladder into one field:
  set `overhauls_before_max_cost` to the number of intervals reaching the heavy event (e.g. 4 for
  the diesel 2.75/5.5/11-year cycle).
- **Interval coverage and the km gap.** Time-basis intervals are measured or composed for every
  class above except narrow gauge and maglev (analogues only) and the per-class steam/diesel/MU
  refinement (research in flight). But the engine triggers on **distance only** (zero disables
  overhauls), and ships and aircraft have measured *time* intervals with **no km equivalent** —
  the current sheet's "n/a km" means they would never be overhauled in-game. Estimated km
  equivalents (ESTIMATE, rung 3): ships — 5-year survey at 200-250 sea-days a year at 9-12 knots
  ≈ 100,000-130,000 km a year → **500,000-650,000 km** per cycle; aircraft — C-check every
  4,000-6,000 flight-hours ≈ 3.4-5.1m km at cruise, heavy check (C6/D) at 23,000-35,000 FH ≈
  **20-30m km**, with `overhauls_before_max_cost` set so the sigmoid reaches the heavy share at
  the heavy check. Direction: in-game duty statistics would confirm or rescale both; the open
  trigger decision below applies.
- Overhaul cost is booked as vehicle maintenance and indexed on the `vehicle maintenance` series
  (vehicle-cost-model "Overhauls and upgrades").

### Carriage overhaul by era

**Rule (user direction 2026-11-24): no single interval spans 1820-2026.** The 2-year/8%-27% rule is
BR Mk 1/2 practice, not a universal. Era bands (research in flight: report 40 §1.10):

| Era / type | Interval (heavy event) | Distance | Share (initial -> max) | Basis / direction |
|---|---|---|---|---|
| Victorian 4/6-wheel wooden (1830s-90s) | 4-6 yr (EST) | 130,000-190,000 km | 8-10% -> **25% (M: Lacy & Dow £62 ≈ 25%)** | interval: NER 2.4 light visits/carriage-yr (M+computed); GER varnish cycle; Hill envelope forces a 25% event to ≥5-yr spacing; lives ≈20 yr (Hawkshaw fund arithmetic) |
| Late Victorian/Edwardian bogie (1890s-1920s) | 5-7 yr (EST) | 200,000-280,000 km | 20-25% (EST) | component check: bogies £33 ≈ 4-5% of a £700-900 carriage; steel underframes lengthen cycles. Moves: NER repair entries |
| Grouping steel-panelled (1920s-40s) | 3-4 yr | 100,000-160,000 km | 15-25% (EST) | interval **computed from GWR 1935 capacity** (3,000 heavy repairs on 8,948 vehicles); St Rollox 1945 heavy 36/wk (M); progressive repair cut costs 30% |
| BR Mk 1/2 (1951-75) | **two-speed (M): coded visits ≈2 yr; full renovation at years 9-11 and 19-21** | 80,000-160,000 km per visit | 8% -> 25-27%, rungs ≈5 to the renovation | 1965 Code of Practice M.C.65/80 + 1966 C1-C6 scopes + target days C1 20 / C2 18 / C3 14 / C4 10 (all M); Mk 1 1982 ≈8% |
| BR Mk 3+ (1975-2000s) | balanced ≈2 yr; **heavy structural 10-12 yr (Chiltern)** | 400,000-600,000 km | 5-8% -> 12-15% (EST) | 1978 annual Derby overhaul 15 working days (M); 2016 A/B 15k/30k, balanced 90k, C4 bogie 600-750k mi (M). Moves: HMRS 1993 draft overhaul specification (archive enquiry) |
| Modern (2000s-2026) | heavy ≈950 days (STATED) | 400,000-500,000 km | 8-12% (EST) | IET 10/50/950-day regime (paywall extraction); ORR 2022 exam structure (M); GWR 802 contract £1.67m a train-year all-in |

**The cycle is two-speed in every BR band**: frequent light coded visits plus a decennial full
renovation. The engine's single interval + sigmoid models it with `overhauls_before_max_cost` =
coded visits per renovation (≈5 at 2-year visits; ≈2 at 4-year). Hansard 1996's "2-year full
overhaul" and the 1965 code's "10-year full renovation" are the visit cadence and the top event of
one ladder, not a conflict. The C1-C6 definitions themselves are recovered (railcar.co.uk — the
PDFs are fetchable with a browser-header Referer; the earlier "bot-blocked" note is struck).

### Steam overhaul intervals — per class, by archetype

**Rule (user direction 2026-11-24): no universal steam interval.** Locomotives varied widely in
distance between overhauls by class, duty and company practice (LMS practice was notably long);
each class takes its own `max_distance_between_overhauls`, set from research where a figure exists
and from the archetype estimate below otherwise, with the basis recorded on the row. The per-class
and per-company research is reported: [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md)
§1.8.

Measured archetypes (report 40 §1.8 — general overhaul interval; Bond 1953 Table IV gives the
periodical-repair spacing per class, and named classes take their own measured values):

| Archetype | Interval between generals | Intermediate | Basis / direction |
|---|---|---|---|
| Express pacific (A1-A4, Coronation, Duchess, MN, King) | 160,000-260,000 km | 55,000-70,000 mi | M: Landau NRM boiler record per class (A4 107,257 mi … Duchess 195,993); Stanier 110-130,000; Bond Table IV (A3 83,574, A4 86,614, Coronation 73,188) |
| Express 4-4-0 / Victorian 4-2-2, 2-4-0 | 95,000-160,000 km | 30,000-50,000 mi | ESTIMATE (rung 3): Ahrons 1-2-year shops at ~30,000 mi/yr; Derby 1893 18-24-month slight-repair cycle. Moves: Victorian record cards |
| Mixed traffic 4-6-0 (Hall, Black Five, Standard 5) | 210,000-305,000 km | 55,000-90,000 mi | M/S: Hall 87,942; Black Five 145-160,000; Standard 5 189,000; Bond Cl5 24-month rule |
| Heavy freight 2-8-0 (28xx, 8F, O1, 4F, WD) | 112,000-170,000 km | 35,000-55,000 mi | M+C: 28xx periodical 86,981; 8F 50,361 (0.54 × Class 5); boiler exchanges mean 83,901 |
| Suburban / metro tanks (2-6-4T, L1, V3, 3150, Metropolitan) | 112,000-155,000 km | 35,000-55,000 mi | M+C: Bond tanks 55,579-83,155; L1 general ≈70,000; duty ratio 0.72-0.85 of main line |
| Industrial and shunting | 45,000-80,000 km (5-8 yr at 8-12,000 km/yr) | 1-2 yr (time-gated) | ESTIMATE (rung 3/5). Moves: IRS works histories; Sentinel manual schedules |
| Narrow gauge (Festiniog practice) | 8-12 yr ≈ 120,000-180,000 km | annual review; re-tube ≈10 yr | M (preservation-era): 10-year boiler tickets |

**Per-class measured values override the archetypes** wherever they exist: Bond Table IV
(periodical-repair miles) and the per-class generals (Black Five 145-160,000; BR Standard 5
189,000; the Landau boiler-record classes) are in report 40 §1.8 and go into the Overhauls sheet
row by row. Duty scaling for unmeasured classes (computed from Bond): heavy freight 0.54 × mixed;
light branch 2-6-0 1.83 × mixed; suburban tanks 0.72-0.85 × main line; manganese-steel axlebox
liners ×1.71 (Class 5) / ×1.43 (2-6-4T).

**Ladder mapping**: interval = the class's periodical-repair spacing (Bond Table IV where
measured), `overhauls_before_max_cost` = 2, the sigmoid reaching max at the heavy general /
boiler-exchange event (Hart-Davies: intermediate at the halfway mark of the general cycle;
corrected GWR 2874 ladder: intermediate year 2, heavy overhaul year 6.5, heavy general year 13-14).
`overhaul_month_tenths` ≈ 15-20 (works time 12-53 days; Crewe average 24). Note the call-in rule:
BR practice was **by condition** with mileage a factor, so interval figures are averages with wide
class-to-class scatter (Bond's own caution). **Open decision on the trigger**: the engine triggers
overhauls on distance only, while historical practice mixed mileage-based generals with time-based
intermediates (and BR diesels were wholly time-based). Options: (a) enter the class's historical
distance between overhauls (wear-based; the recommended default), or (b) scale to preserve the
historical year-frequency at in-game duty. Class annual km at the pakset's game speeds is the
unknown in both.

## Per-class decomposition

All five pass-40 research reports are in (report 40 §1-§5): overhaul evidence and per-class
intervals, renewals shares and lives, the rail and non-rail fixed/distance splits, and upgrade
costs. Each class section carries the resulting values with their rung and direction. "k" = mean
annual kilometres per vehicle (measured anchors: TRB 1976-77 — class 87 274,000; 55 226,000;
47 113,000; 86 176,000; 37 81,000 km/yr; Hill's wagons 418-455 goods train-miles a year). All
money at 1900 until the conversion chain is applied at the pass.

### Rail carriages

- **ρ (renewals)**: **≈35% (25-50) of the total**; life ≈40 years (Hill App. III Table XXIV: 2.53%
  a year by number; statutory Abstract B coaching shares measured 19-50%). Rung 1.
- **F/V split of the routine remainder: 70/30** (rung 2/3, low confidence): wage behaviour in Hill
  Table IV/V, passenger wheel turning long-interval (140,000 miles or annual), body/roof/paint/
  upholstery time-based. Direction: post-1911 repairs-vs-renewals columns; car works job-cost
  records; the ORR RSMR final coefficients if published.
- Overhaul: the table above (2 years; 8% -> 27%). Upgrades: brake pairs at 7.7%, structural
  conversions 25-30% (below).

### Rail wagons

- **ρ (renewals)**: **≈50% (40-60) of Hill's £4 4s**; life 30-35 years (Hill App. III Table XXV:
  3.1% a year by number; statutory Abstract B wagon shares measured 21-68%; rate × price ÷ Hill's
  total = 52-55%). Rung 1.
- **F/V split of the routine remainder: 65/35** (rung 1-3, low-medium confidence): wages track
  stock almost exactly (+9.6% vs +9.5% over five years) and cost is not mileage-driven (December
  halves +39% on +5% miles — Hill IV/V); wheelset work on 250,000 km cycles is the main distance
  item; the measured modern contract form is a standing fee plus an assumed 50,000 km/wagon-year
  with excess-mileage charges (EUR 0.04/km), and the LL brake-block retrofit publishes the same
  increment as 300-600 EUR/year or 0.01-0.02 EUR/km. Direction: a full-service contract split into
  standing and mileage; a wheelset/brake/body cost-share build.
- Note the utilisation unit: Hill's is goods train-miles per wagon in stock (418-455 a year).
  Overhaul: the table above (6 years; 12% -> 20%). Upgrades: brake pairs 10-20% (below).

### Rail locomotives

- **ρ (renewals)**: **≈25% (20-30) of the total** — complete renewals only; 55-65% if partial
  renewals are excluded too — life 25-30 years (Hill App. III Table XXIII 3.6%/yr; statutory
  Abstract B loco shares 5-18% for rebuilders, 13-18% for renewers). Two corrections to earlier
  notes: Price Williams's "money life" (10.81 yr) is a payback coefficient, not a service life
  (NER ultimate life 25 years; PW models 30), and his £139.91 an engine-year is a
  component-renewal schedule (repairs **and partial renewals**), not the capital share — netting
  it would strip boiler/tyre/tube work that belongs to maintenance or the overhaul fields. The
  capital share is net cost ÷ service life ≈ £60-75 an engine-year. Rung 1.
- **F/V split of the routine remainder: steam 60/40; diesel/electric 50/50** (rung 2/3, low to
  low-medium). Steam: known distance items are only about 12% of the per-train-mile cost (tyres
  0.052d/mile, boiler 0.24d/mile) but axle exams (250,000 miles) and tyre lives are mileage-gated
  while painting and boiler-washing are calendar-gated; Hill's text finds little mileage relation.
  Diesel/electric: exam intervals in engine-hours and cleaning hours are time-like, yet ORR's 2026
  result finds mileage highly significant with an acknowledged fixed component. Direction: Price
  Williams-style component tables generalised; TNA RAIL cost-per-train-mile series; ORR RSMR final
  coefficients.
- Overhaul: the table above (steam 2-3/7-year ladder; diesel 2.75/5.5/11-year). Upgrades:
  reboilering 20-27%, heavy rebuild 30-35%, donor-parts conversion 85-100% (below).

### Multiple units

- **ρ (renewals)**: **≈30% (25-45)**; life 25-40 years (ROSCO policy 30-35: Angel 2023/25,
  Porterbrook 2024, ORR 2020; Southern EMU measured 32% in the 1933 statutory accounts). Rung 1-2.
- **F/V split of the routine remainder: 50/50** with diesel/electric locomotives (above). Modern
  anchors: ORR RSMR 2026 medians £0.72-1.88 a vehicle-mile (£93k-285k a vehicle-year by contract
  type); LU levels 1-3 £25,700 a car-year standing; the lease form is standing + mileage
  (Porterbrook accounts). Direction: ORR RSMR final coefficients; SPARK MR-MEA-005 (Class 150/1
  typical maintenance costs).
- Overhaul: the table above (C6 cycle; £ measured per vehicle). Upgrades: refresh 8-12%,
  re-tractioning 20-25% (below).

### Road vehicles (buses, coaches, lorries, vans)

**ρ = 0%**: CM and municipal "maintenance" figures exclude depreciation by convention — it is a
separate line in the same tables. Lives: bus 12-15 years (8-10 pre-war), lorry 6-8 first life
(report 40 §2).

Enter as **absolute standing + per-km, not percentages** (report 40 §5): the fixed share is a
function of duty — 47% → 22% as a bus's weekly mileage goes 200 → 600.

| Sub-class | Standing (fixed_cost basis) | Distance (runningcost basis) | Fixed share at class duty | Rung |
|---|---|---|---|---|
| Bus | ≈ £52-87/vehicle-year (1959: 19s 10d-£1 13s 4d a week) | 1.2-2.2 d/mile | 22-25% at 31,200 mi/yr; 47-49% at 10,400 | 1 (measured, CM 2 Jan 1959, three duty levels) |
| Coach | bus curve, high-duty end | as bus | 20-30% | 2 |
| Lorry | ≈ £4,400/vehicle-year (2016) | 13.6 p/mile | 33-39% at 50-65,000 mi/yr | 1 (measured, FTA 2016 bands decomposed) |
| Van | bus/lorry interpolation | as above | 35-45% at ~25,000 km/yr | 3-4 (duty interpolation of the 1959 curve) |

The old 75/25 distance/standing rule is retained only as the busy-urban-duty check; the entered
values are the absolute forms. What would move these: a second multi-mileage CM table (bus/coach),
FTA originals with more bands (lorry), a 1930s CM van table at multiple mileages (van).

### Trams and light rail

**ρ: 30-50% of the car-only head** (estimate — the statutory head is "General Repairs and
Maintenance (or Renewals out of Revenue)", so renewals charged to revenue sit inside it; fund
renewals outside). Life 25-35 years (statutory loan 15; Supertram life-extension at 32-34).

**40-55% standing** (rung 2/5): modern contracts are per vehicle-year availability payments (NET:
£118,657 a tram-year), overhauls are calendar events, and buses at similar duty measure 22-33%
standing. The historic MoT car-only series (1.98 → 1.52d per car-mile, 1923-33) aggregates standing
decay with distance wear and cannot be split from the returns. Fixed level to derive from the
car-only totals at the class duty. What would move it: a municipal abstract separating time-based
from mileage-based car work; CoMET benchmarking data. **ρ note**: the one directly measured renewals share anywhere is a steam
tramway's — Dewsbury 1885 running cost 3.13d per car-mile including **0.8d renewals ≈ 26%** (forum
6521 post #116; report 40 §1.6).

### Ships and inland boats (powered)

- **Motor/steam ships: 50-65% standing** (rung 2/4): calendar pieces are measured (drydocking
  US$1.2-2.3m per 2.5-5-year cycle; Drewry's annualisation is survey + dock divided by five;
  Kirkaldy 1913 annual overhaul 2% of capital); the usage share is machinery and voyage repair, per
  hour at sea (≈ per km at 9-12 knots). **ρ**: net the reserve only where the source's figure
  includes it (Martin's 5%-of-capital covers upkeep as a whole); life 25-30 years. What would move
  it: Drewry App. 11/12 values (paywalled); P&O repair ledgers (RMG archive).
- **Inland motor boats: 60-75% standing** (rung 3): every measured inland figure is per-year or
  per-job (blacking every 2-3 years, BSS every 4, docking every 3); engine wear is the only clear
  usage item. What would move it: GUCCCo account books BW58/3/1/7.
- **Sailing craft: standing only** (rule 2). Level: Martin's 5%-of-capital/yr working figure; the
  one measured component is sheathing £120/yr on a 400-500-ton ship (1862). Measured levels from
  the barque account books at Royal Museums Greenwich (*ELEANOR DODSON* AMS/36; *BURNS* MSS/77/063).

### Aircraft

**ρ = 0%** on CAA-style maintenance figures (lives 20-25 years, depreciated separately — KPMG/
IATA convention). **30-35% calendar at 2,800 flight-hours a year**, rising toward 50%+ at low
utilisation; 65-70% usage per flight hour with a per-flight-cycle element (rung 1 for the
structure, 4 for the budget split: report 40 §5). The measured leasing-reserve structure is the basis: airframe checks per
calendar month, landing gear per cycle with a monthly floor, engine restoration per flight hour,
life-limited parts per cycle, APU per running hour. Mapping note: the engine has no per-cycle
field — per-landing elements convert to per-km at the class's landing-km ratio, or fold into the
per-km rate with the sector-length caveat recorded. What would move it: IATA MCX member tables
(line vs base vs engine shares).

### Horses and horse vehicles

**No per-km figure** (rule 2). Horses: keep £28-60/yr, central £45, excluding the horsekeeper's
wages (staff are charged separately) — measured, rung 1. Horse vehicles: all repair accounts are
per-year (1760s coach £70 a coach-year, about 70% of capital; no horse-drawn goods repair account
exists). Enter the whole maintenance figure in `fixed_cost`, `runningcost` 0.

### Narrow gauge and maglev

*(pending: analogue estimates only)*

## Upgrade costs

Measured events and the full class-rule table: [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md)
§4. Rules in force (each % is of the TARGET vehicle's price; basis in the report):

- **Unfitted → fitted brake pairs (the 30 carriage/van pairs): 7.7%** — measured £35 a carriage
  against £398-518 (1879); wagons 10-20% (Aspinall £10-20 on a £85-95 wagon; 20-33% after 1922).
- Diesel heavy rebuild 30-35% (Class 47→57, measured); re-engine only 10-15%; steam reboilering
  20-27% (boiler share, measured); steam donor-parts class conversion **85-100% of new** (Grange
  £5,000 — not a cheap conversion); MU refresh 8-12% / re-tractioning 20-25%; carriage structural
  conversion 25-30%; bus refurb 25-30% / rebuild 50%; lorry rebuild 50%; tram life extension
  45-50%; aircraft cabin variants **1-5%** (reject the blanket 50% for variant links; P2F is
  measured at 4-8% of new list).

**Mapping to `upgrade_price`** — definitions: C = target's `cost` (the engine's default
`upgrade_price`); B = measured works bill; R = the resale credit the engine withholds on the old
vehicle; V' = value of the vehicle the real rebuild produces; V_old = value of the vehicle
consumed. Equating wealth changes: **U = B + (C − V') + (V_old − R)**. Cases:

1. **Donor-inclusive totals** (Class 47→57 £500k including the donor): the donor purchase is
   V_old — **U = measured total**.
2. **In-place works on an owned vehicle** (brake fitting, reboilering, Greenway, sliding doors,
   re-tractioning): the rebuild consumes the vehicle into the rebuilt asset; with V' ≈ C,
   **U = B**. Fitted brakes: U = £35 = 7.7% of the unfitted price.
3. **Partial-renewal events** (Supertram life extension, Metrolink mid-life): V' < C, so U sits
   above B by (C − V'); where V' is unmeasurable enter **max(B, class rule × C)** and note the
   game grants a full fresh life.
4. **Cap**: U ≤ C — never above buying new.

Reducing U below B by R is **rejected**: it double-counts, since the real rebuild also consumes the
old vehicle into the rebuilt asset. The one semantic gap runs upward — if the engine reissues the
target at age zero while real rebuilds confer partial renewal, U rises by (C − V'). **Open engine
question: does an upgrade reset vehicle age?** `[UNVERIFIED]` `upgrade_price` is indexed on the
`vehicle maintenance` series, not `vehicle purchase` (engine-bugs) — the costing pass must convert
it on the right basis.

## Open questions

- Wear-ramp option (a) or (b) per class (above).
- The upgrade mapping rule's engine behaviour (above).
- `max_running_cost`, `increase_maintenance_by_percent` and
  `years_before_maintenance_max_reached` are engine defaults, not calibrated; should the pakset set
  them per class?
- How is the mean annual km (k) per class to be fixed — from in-game utilisation assumptions, or
  from historical utilisation (Hill's goods train-miles per wagon-year, modern vehicle-mile
  statistics)? The F/V split is sensitive to it whenever a per-year figure is the only evidence.
