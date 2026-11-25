---
status: draft
verified: New ex-15 @ fcd40c0bc + passes 62-65 (working tree), 2026-11-25
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
and the pass-40 reports in [cost-balancing](../cost-balancing/). Read
[source-composition](source-composition.md) before netting anything from a source figure or
changing the class columns of the maintenance workbook: it records, per source, what the figure
is stated to contain, and the treatment each composition requires. Read
[archive-visit-kew](../cost-balancing/archive-visit-kew.md) when planning or making a physical
archive visit (Kew, library, Chasewater, HMRS) to close one of the maintenance or overhaul gaps
this doc flags: it carries the orderable references, the transcription spec per document and the
what-it-adds table.

**Terms.** The **combined source figure** (the envelope) is one source figure that covers several
cost fields of an asset object; the object's cost fields must together charge it. The
**continuous head** (the head) is the part of that figure left after the components charged
through other fields are removed. A **rung** is one
era value in a class ladder; a **class ladder** is the ordered set of rungs. The **mean annual
distance** is the class and era distance that converts an overhaul interval in years to kilometres
and sets the reference duty for the fixed/per-km split; the table is
[mean-annual-distance](mean-annual-distance.md). A **pass** is one numbered research report or
workbook patch script in [cost-balancing](../cost-balancing/);
[pass-history](../cost-balancing/pass-history.md) records what each pass applied.

## Standing rules

0. **The decomposition rule: complete every cost field and charge no component twice.** Where
   several cost fields for one asset object must be completed from a single data source that
   gives one combined figure covering all of those fields, and no obtainable source provides a
   breakdown, estimate a decomposition from inferences drawn from surrounding evidence, then
   cross-check the result for plausibility and coherency.

   The procedure:

   1. **Establish the scope.** State which cost fields the source figure covers. If a source
      gives a component individually for the object, use that component directly and do not
      decompose the combined figure.
   2. **Deduct only what the source contains and another field charges.** If the source includes
      a component that another field charges, deduct it exactly once (for vehicle upkeep, renewals
      are charged through the purchase price and works overhauls through the overhaul fields). If
      the source gives the component separately, do not deduct it again. Do not deduct a
      component the source has already put outside the figure.
   3. **Estimate the split where it is not measured.** Use the nearest measured anchor (same
      class, same era, or the nearest era), state the evidence and what would replace it, and
      state which part the data constrain. A coherent estimate that keeps the fields summing to
      the source figure is better than a precise figure that does not add up.
   4. **Keep every field complete.** An empty overhaul field means that the vehicle is never
      overhauled in game: its wear never resets, its availability never recovers and it never
      enters works. Every vehicle needs an overhaul figure or a stated reason for zero.
   5. **Test every row.** The fields must sum to the source figure after the components charged
      elsewhere are removed. `wb_audit_coherence.py` checks coverage, a positive target or a
      stated reason for zero, an interval, and the arithmetic. Run it after every pass.

   Where data contradict a decomposition formula for any object or set, reconsider the formula:
   discard it, modify it, or limit it to the range the data support, rather than only flagging the
   row. Treatments by source: [source-composition](source-composition.md). The failures that
   motivated the rule, and the pass records, are in
   [cost-balancing/pass-history](../cost-balancing/pass-history.md).
   `[USER-DIRECTION:2026-11-25]`
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

## The decomposition identity, and when it may be applied

A maintenance source figure is money spent on some set of activities, and the engine charges three
of them in different places: routine upkeep through the maintenance fields, a vehicle renewal
through `cost` and `upgrade_price` (the player's replacement decision), and a works overhaul as
an event through the overhaul fields. The identity below therefore applies **only to a head
figure whose source states that it contains routine upkeep, renewals and major works**. For a
class with such a figure (the annual maintenance figure):

```
annual maintenance figure = renewals provision + overhaul provision + routine remainder
overhaul provision = (mean overhaul event cost) / (overhaul interval in years)
routine remainder = 12 x fixed part + per-km part x mean annual distance        
```

- **The renewals provision**: the money per vehicle-year, deducted only where the source states renewals are inside the figure. A vehicle renewal is the player's capital repurchase in-game, so the renewals provision is
  subtracted from the maintenance fields and left to `cost` and the player's replacement
  decision. Measured (report 40 §2): **wagons ≈50% (40-60), carriages ≈35% (25-50), locomotives
  ≈25% (20-30; complete renewals only), multiple units ≈30%, trams 30-50% of the car-only figure; buses,
  lorries and aircraft 0%** — CM, municipal and CAA-style maintenance figures exclude
  depreciation by convention (it is a separate line in the same tables). Lives: wagons 30-35,
  carriages ≈40, locos 25-30, multiple units 25-40, bus 12-15, lorry 6-8, tram 25-35, ship 25-30, aircraft
  20-25 years. Two cautions: Price Williams's "money life" is a payback coefficient, not a
  service life, and his £139.91 an engine-year is a component-renewal schedule (repairs + partial
  renewals), not the capital share; and "Transfer to Renewal Account" provisions sit on top of
  actual renewals in the statutory accounts.
- **The overhaul provision** (the overhaul events), deducted only where the source states that works overhauls are inside
  the figure. They are charged through the overhaul fields, so the overhaul provision is subtracted from the routine remainder. The
  overhaul shares and intervals of the `Overhauls & upgrades` sheet are the current evidence.
- **The routine remainder**, split into the fixed part (`fixed_cost`) and the per-km part (`runningcost`).

### The treatments actually in force

[source-composition](source-composition.md) records, per source, what the figure is stated to
contain and the treatment that follows. The full identity above applies to no source figure in the
current evidence. The treatments in force are: **partial, renewals** (deduct the renewals provision only — the Hill
1895 rail figures and the tram car-only figure state renewals inside and are silent on works
overhauls); **partial, overhauls** (deduct the overhaul provision only — the Commercial Motor road item states major
repairs inside and keeps depreciation outside); **no decomposition** (deduct nothing — horse keep,
horse-vehicle repairs, the FTA trailer line); and **open question** (deduct nothing and split
nothing, because no checked-out source states the composition — the wagon 8-per-cent rule, the
motor-trailer 5-per-cent rule, the water 2-per-cent rule, the aircraft 20-per-cent rule and the
modern tram contract).

Two rules follow and are not negotiable. An element is deducted only where the source says it is
inside the figure; assuming containment is not acceptable, because the assumption moves money
between fields and cannot be checked. Where the composition is unrecorded, the class figure is
written whole and the row records the passage that would resolve it. `[USER-DIRECTION:2026-11-25]`

**Wear-ramp correction.** The engine ramps the charged figures from base toward
`max_running_cost` over the overhaul cycle and the ramp reaches the monthly charge. If the fields
are entered at the fixed part F and the per-km part V, the charged life-average is `m x (12 x F + V x k, F the fixed part and V the per-km part)` where m is the mean ramp
multiplier over the cycle (m = 2 at the default linear 1-to-3 ramp). Therefore either:

- **(a) Enter the mid-cycle level**: base fields = the two parts / m with `max_running_cost` at the
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
2. **Neighbouring-class transfer** with a stated reason (e.g. multiple units from modern light-rail contracts).
3. **Component decomposition**: distance-worn components (wheelsets and tyres, axle bearings,
   brake gear, engine internals) against time-worn components (paint, roof, body and frame decay,
   corrosion), priced as shares of the vehicle and dated by their renewal lives.
4. **Utilisation scaling**: where a per-vehicle-mile and a per-vehicle-year figure both exist for
   the same fleet, the pair identifies the two parts directly (the per-km part is the per-mile figure, the fixed part is the remainder).
5. **Analogical prior** (e.g. aircraft airframe reserves for ships): last resort, labelled as such.

Every estimate states: the rung, the arithmetic, the confidence, and **what would move it and in
which direction** (e.g. "a wagon overhaul invoice would raise the overhaul provision and lower the routine remainder; it would not change
the fixed/per-km split").

## Overhaul values by class

Interval and cost share of the vehicle's new price. The engine's interval field is in kilometres,
so each year-interval converts at the class's mean annual distance: `interval_km = interval_years x mean annual distance`.
The class and era values, their evidence and the rows they apply to are in
[mean-annual-distance](mean-annual-distance.md). Rung and direction for every row: report 40 §1-§1.5.

| Class | Interval | Share (initial -> max) | Basis | What would move it |
|---|---|---|---|---|
| Rail wagons | 6 yr (5-7) | 12% -> 20% | composed (rung 3): 7-year repair-contract terms, the 4-6-year periodic-overhaul (POH) analogue of the Indian Railways wagon manual, reconciled with measured £5-£5 8s 6d a wagon-year contracts (3.2-4% of new a year) | RCH per-job schedules (Chasewater 4778) or a wagon overhaul invoice; share could sit 8-25% |
| Rail carriages | **per era** — see the era-band table below | **share of the measured annual total, not of capital**: 28% / 24% / 19% / 12% / 10% / 8% of A from 1830 to 2026 | research pass 44: two measured events (Lacy & Dow £62 in the 1860s = 1.84 A; the 1982 York Works Mk 1 overhaul = 0.16 A) set the ends, the middle is interpolated | the four missing event prices named in report 44 §8 |
| Steam locomotives | **per class** — see the archetype table below | 5% -> 15% (heavy general measured at 9-14% for GWR 28xx; share likely scales with class size) | GWR 28xx record card (IR yr 2, HO yr 6.5, HG yr 13-14); Fowler 1913 heavy/light scope definitions; Stanier's practice (JILocoE 43); Bond Table IV per-class values | per-class values reported (report 40 §1.8) — to be applied per row |
| Diesel/electric locomotives | 2.75 yr, heavy at 11 yr | 7% -> 20% | Hansard 11 Mar 1996 (measured) intervals; shares provisional | Kew: COAL 101/164, AN 88/108, AN 112 standard charge schedules |
| Multiple units | 8 yr in the workbook (measured C6 cycle); report 45 recommends 5 yr before 1948 and 6 yr to 1999, both ESTIMATE | 15% of A; event 1.2A, first 0.70 of the maximum over three | research pass 45/53: measured 158 C6+ £180,000; 365 £187,500; LU 1996 stock £64,700/car. The provision and the event are a share of the measured annual ladder, not of capital | measured interval for the C6 cycle; a measured pre-2000 interval and a measured annual distance for first-generation stock |
| Buses | 4 yr (220,000 km) | 25% -> 40% | Aldenham £2,000 (1965) = 25-33% of a new double-decker (measured) | further municipal overhaul accounts |
| Lorries | engine exchange 100,000-250,000 mi; complete overhaul 250,000 mi | 10% -> 30% | CM 1960/61/69: Cummins ReCon £394-473, Ford £39 exchange units (measured) | maker overhaul schemes (Gardner scheme unpriced) |
| Trams | 2 yr pre-1950; 3 yr 1950-90; 12 yr modern | Pre-1950 28% of gross A, event 0.35A rising to 0.75A; 1950-90 28% of the repairs-only rung, event 0.54A rising to 1.15A; modern 6%, one event of 0.75A; upgrade 22-50% of the new price by introduction year | research passes 47 and 49: measured municipal car-only returns 1923-33, Sheffield repairs 1938-50, estimate 1950-90; measured 1934 LCC E/1 rebuild and 2026 Supertram life extension for the upgrade | a measured municipal tramcar repairs figure after 1950 and a measured works-overhaul price |
| Ships | 5 yr special survey | 2% -> 5% (bare survey + dock under 1.5%; with steel renewal 3-9%) | US National Academies tanker data; Hellenic Chamber provision (report 40 §1.5); "Earl of Essex" overhauled with new boilers £1,100 against £4,154 new (1877, ≈26%) | Drewry/Lloyd's repair records (paywalled) |
| Aircraft | heavy check in a 6-check cycle; 6-10 yr | 2.5% -> 5% (airframe heavy check 0.8-1.1%; with engines and gear 2-5%) | Aircraft Commerce 777 guide; D-check 50,000+ man-hours (report 40 §1.5) | engine shop-visit prices in lessor filings |
| **Comet 1** (special case) | replacement of the fatigue-doomed airframe ≈1,000 pressurisation cycles | 1,790,000 km = 1,000 cycles × the measured BOAC mean sector 1,790 km (sector-dependent: shorter sectors reach the limit sooner per km) | **67% -> 67%** (band 65-75; engines, avionics and interior are salvaged — user direction 2026-11-24 revised) | measured + estimate: fatigue failures at 903-1,286 pressurisations (C.A.P. 127; FAA ≈1,000; design assumption 10,000); salvage = engines 25-30% + avionics 8-10% + interior 7-10% less 8-12% extraction and refit. **Comet 4 and 1XB excluded** (report 40 §1.10). Direction: a Ghost engine unit price |
| Narrow gauge, maglev | analogue of nearest class | analogue | rung 5 | any measured narrow-gauge overhaul |
| Horses (the animals) | 7 yr (Leeds renewal cadence) | 70,000 km at an assumed 10,000 km/yr | **100% -> 100%** — the overhaul is the replacement at the end of working life | M: renewed about once every 7 years at cost = purchase price (1894-5 accounts, forum 6521 #116) |
| Horse vehicles (carts, omnibuses, coaches, wagons) | 5 yr (estimate) | 50,000 km at an assumed 10,000 km/yr | 15% -> 30% (estimate) | rebuilding wheels, axles, springs, bodywork and paint; Lacy & Dow 25% carriage analogue. Moves: coaching/omnibus accounts |
| Motor trailers and articulated bus sections | 11 yr (440,000 km) for a trailer; lorry cadence for an articulated bus section | trailer refurbishment 0.33 of capital, annual share about 3% | research pass 48; passes 54-55: measured TIP 2025 and Cooks 1988 refurbishments at about one-third of a new trailer | a measured trailer refurbishment price in another era; the unmeasured trailer composition |
| Sailing craft, inshore/coastal (barges, wherries, brigs, schooners) | 5 yr (estimate) | 175,000 km at an assumed 35,000 km/yr (depends on the assumed mean annual distance) | 5% -> 15% (estimate) | hull, rig and spar refits; "Earl of Essex" overhaul 26% at 18 years as the analogue; refit share carved OUT of the Martin 5% provision. Moves: RMG barque accounts |
| Sailing ships, deep-sea (clippers, windjammers, Blackwall frigates, barques) | 5-yr Lloyd's survey cycle (as steamers) | 500,000 km at an assumed 100,000 km/yr ocean-trade duty (depends on the assumed mean annual distance) | 3% -> 10% (estimate) | classed vessels surveyed like motor ships minus the machinery share; between the motor-ship and wooden-refit bands |

Notes:

- The engine's single interval plus the sigmoid (`initial_overhaul_cost` rising to
  `max_overhaul_cost` over `overhauls_before_max_cost`) collapses an event ladder into one field:
  set `overhauls_before_max_cost` to the number of intervals reaching the heavy event (e.g. 4 for
  the diesel 2.75/5.5/11-year cycle).
- **Interval coverage and the km gap.** The engine triggers on **distance only** (zero disables
  overhauls), so every time-basis interval needs a km equivalent. The class and era values are in
  [mean-annual-distance](mean-annual-distance.md): carriages, wagons, locomotives, multiple
  units, trams, buses, lorries, vans, cars, ships and maglev have a table value; aircraft use
  the measured C-check event distance (4,000-6,000 flight hours, about 4.2m km at cruise) and a
  separate heavy-check distance, with `overhauls_before_max_cost` set so the sigmoid reaches the
  heavy share at the heavy check. The ship annual distance (115,000 km) and the aircraft annual
  utilisation are estimates; a measured sea-days or annual-hours figure would replace them. The
  trigger decision below still applies.
- Overhaul cost is booked as vehicle maintenance and indexed on the `vehicle maintenance` series
  (vehicle-cost-model "Overhauls and upgrades").

### Carriage overhaul by era

**Rule (user direction 2026-11-24): no single interval spans 1820-2026.** The 2-year rule is
BR coaching-stock practice, not a universal. The table below is research pass 44 §5, and its
unit is a share of the measured annual maintenance total A, not a share of capital. Two
measured events set the ends of the series: Lacy & Dow's £62 for a Midland composite carriage
"repairing, repainting and retrimming" in the 1860s (1.84 × A) and the 1982 York Works Mk 1
overhaul at "more than £2,000" (0.16 × A). The event stayed roughly flat in real money while A
rose elevenfold, so the share must fall.

| Era / type | Interval (heavy event) | Interval km (reference duty) | Provision, % of A | Event, × A | Basis / direction |
|---|---|---|---|---|---|
| Victorian 4/6-wheel wooden (1830s-90s) | 6 yr (5-8) | 210,000 (35,000 km/yr) | **28%** (15-31) | 1.68 | £62 = 1.84 A (MEASURED event, A proxied by 1892); NER 2.65 works visits a carriage-year and GER 5-year paint cycle bound the interval (ESTIMATE); Hill's envelope forces 6-8 yr for a 25%-of-capital event |
| Late Victorian/Edwardian bogie (1890s-1920s) | 5 yr (4-6) | 180,000 (36,000 km/yr) | **24%** (15-30) | 1.20 | interpolated between the two anchors; GWR 1935's 3.0-year heavy interval as the lower bound |
| Grouping steel-panelled (1920s-40s) | 3.0 yr (2.5-4) | 165,000 (55,000 km/yr) | **19%** (15-25) | 0.57 | interval MEASURED: Swindon 3,000 heavy repairs on 8,948 coaching vehicles, 1935; provision interpolated |
| BR Mk 1/2 (1948-75) | **2 yr** (2-3) | 176,000 (88,000 km/yr) | **12%** (8-18) | 0.24 | Hansard 11 Mar 1996: full overhaul "approximately every two years"; 1965 code renovation at years 9-11 and 19-21; 1982 £2,000 = 0.16 A |
| BR Mk 3+ (1975-2000) | 2 yr (1-4) | 240,000 (120,000 km/yr) | **10%** (7-15) | 0.20 | 1978 HST annual works overhaul; C4 bogie at 600,000-750,000 miles |
| Modern (2000-26) | 2.6 yr (2.6-5) | 294,000 (113,000 km/yr) | **8%** (6-12) | 0.21 | IET heavy overhaul at about 950 days; Sprinter specification 5 years / 350,000 miles |

**How the engine holds it.** The interval field is the heavy event. The first overhaul costs
0.70 of the maximum and the maximum is reached over three events (research pass 44 §6); the
smoothstep is symmetric, so the mean event is (first + max)/2 and the events amortise to the
provision. The light works visits are not a separate charge: they are inside the continuous
head, which is A less renewals less the provision.

**The anchors.** The Victorian £62 overhaul is 24.8-27.6 per cent of the £225-250 composite
price ([report 53](../cost-balancing/research-pricing-report-53.md)); the £450-500 alternative
has no source. The BR Mk 1 £2,000 event is 0.16 × A (£57 in 1900 money); the 8-27 per cent band
in report 36 is not used. The km column is the band's reference duty, stated in every row's
basis.

**Research pass 51 (applied by pass 62).** The 1920 and 1950 points were the weakest in the
series. The measured inputs give 39 GBP a carriage-year at 1920 (band 28-55) and 121 at 1950;
1948 falls at 112 and 1966 at 226 by interpolation. The 1990 rung of 460 stands untested. Pass 62
replaces the previous interpolations (59 at 1920 and 140 at 1950) in the workbook and recomputes A,
the renewals deduction, the provision, the head and the event on every standard-gauge carriage row;
the provision shares, the intervals, the renewals treatment and the 70/30 split are unchanged.
[Report 51](../cost-balancing/research-pricing-report-51.md).

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
| Mixed traffic 4-6-0 (Hall, Black Five, Standard 5) | 210,000-305,000 km | 55,000-90,000 mi | measured + stated: Hall 87,942; Black Five 145-160,000; Standard 5 189,000; Bond Cl5 24-month rule |
| Heavy freight 2-8-0 (28xx, 8F, O1, 4F, WD) | 112,000-170,000 km | 35,000-55,000 mi | measured + computed: 28xx periodical 86,981; 8F 50,361 (0.54 × Class 5); boiler exchanges mean 83,901 |
| Suburban / metro tanks (2-6-4T, L1, V3, 3150, Metropolitan) | 112,000-155,000 km | 35,000-55,000 mi | measured + computed: Bond tanks 55,579-83,155; L1 general ≈70,000; duty ratio 0.72-0.85 of main line |
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

The renewals-share and fixed/per-km values below are the **shares of a source figure**, not amounts to deduct: the renewals share is
deducted only where [source-composition](source-composition.md) records that the source's figure
contains renewals, and the overhaul provision only where it records that the figure contains works overhauls. In the
current workbook that means the renewals share for the Hill rail figures and the tram car-only figure, the overhaul provision for the
Commercial Motor road figures, and neither for the figures recorded there as unrecorded or as
repairs-only. Each section says how its renewals share was derived; whether it applies is the composition
table's decision.

### Rail carriages

- **Renewals provision**: **≈35% (25-50) of the total**; life ≈40 years (Hill App. III Table XXIV: 2.53%
  a year by number; statutory Abstract B coaching shares measured 19-50%). Rung 1.
- **fixed/per-km split of the routine remainder: 70/30** (rung 2/3, low confidence): wage behaviour in Hill
  Table IV/V, passenger wheel turning long-interval (140,000 miles or annual), body/roof/paint/
  upholstery time-based. Direction: post-1911 repairs-vs-renewals columns; car works job-cost
  records; the ORR RSMR final coefficients if published.
- Overhaul: the era table above (share of A, not of capital). Upgrades: brake pairs at 7.7%, structural
  conversions 25-30% (below).

### Rail wagons

- **Renewals provision**: **≈50% (40-60) of Hill's £4 4s**; life 30-35 years (Hill App. III Table XXV:
  3.1% a year by number; statutory Abstract B wagon shares measured 21-68%; rate × price ÷ Hill's
  total = 52-55%). Rung 1. The workbook's wagon head is the measured wagon ladder (research pass
  46): head = 0.8A and the event 1.2A every six years. The composition of the wagon ladder is
  unrecorded, so no separate renewals share is deducted
  ([source-composition](source-composition.md)).
- **fixed/per-km split of the routine remainder: 65/35** (rung 1-3, low-medium confidence): wages track
  stock almost exactly (+9.6% vs +9.5% over five years) and cost is not mileage-driven (December
  halves +39% on +5% miles — Hill IV/V); wheelset work on 250,000 km cycles is the main distance
  item; the measured modern contract form is a standing fee plus an assumed 50,000 km/wagon-year
  with excess-mileage charges (EUR 0.04/km), and the LL brake-block retrofit publishes the same
  increment as 300-600 EUR/year or 0.01-0.02 EUR/km. Direction: a full-service contract split into
  standing and mileage; a wheelset/brake/body cost-share build.
- Note the utilisation unit: Hill's is goods train-miles per wagon in stock (418-455 a year).
  Overhaul: six years; head 0.8A, event 1.2A (research pass 46). [Report 52](../cost-balancing/research-pricing-report-52.md)
  finds the HMRS 1972-81 repair-cost data are archive-only (SKU ME0354) and no readable measured
  wagon repair cost for that window; the documented seven-year BR cycle for HAA wagons supports
  the six-year band, and the 1.2A event remains an ESTIMATE. Upgrades: brake pairs 10-20% (below).

### Rail locomotives

- **The level: a dated ladder, not one era-blind figure** (research pass 46). 215 / 306 / 800 /
  2,100 / 1,045 / 520 GBP per engine-year in 1900 money at 1900 / 1950 / 1961 / 1977 / 1995 /
  2020, log-linear between and flat outside. Hill's figure is the 1892 nineteen-company average
  (GBP 208 18s.), **not** the GBP 253 the generator had used, which is the Great Western maximum.
  The ladder rises to a 1970s peak and falls about fourfold to the Class 66 generation. A
  straight-electric locomotive of the Class 87 generation takes 0.5 of the rung (Calder's Class 87
  is 52 per cent of the Class 47 on the same duty); the factor is not applied to a post-1995
  dual-mode mixed-traffic locomotive, and the Class 88 takes the Class 68 level of 614.82 (pass
  64). Steam introduced after 61 stays on the 1961 rung, because the modern
  fall is a property of the Class 66 generation, not of steam.
  [research pass 46](../cost-balancing/research-pricing-report-46.md). The measured
  1913-1938 Ministry returns validate the 1900-1950 interpolation within 5 per cent in every
  stable year; the 1920-21 spike is arrears of repairs and is not a rung. The series changes
  composition at 1950: the pre-1950 points are gross of renewals and the 1950 point is repairs
  only. The workbook phases the 25 per cent renewals share out by 1950 and enters the 1950 rung
  net at 306; the 408 gross alternative is not used. The modern series is two class tracks: the
  diesel/freight line is 2,100 (1977)
  to 1,045 (1995) to 520 (2020, Class 66), and the electric line is 1,103 (1977,
  Class 87) to 1,045 (1995, mixed fleet) to 868 (2018, Class 92 sleeper contract). The 868 is a
  class/duty override, not a clean electric-passenger track point: the Class 92 is a
  **mixed-traffic** locomotive (the pakset object has `freight=None`), and the measured contract
  covers 12 locomotives on the Caledonian Sleeper, a low-mileage passenger duty. Pass 63 applies
  the override in the workbook; the rest of the fleet remains on the single time ladder.
  [Research pass 50](../cost-balancing/research-pricing-report-50.md).
- **The per-km rate is derived from the ladder, never added to it.** Hill's per-engine-year and
  per-train-mile figures are the same money (2.51d. x 20,164 miles = the annual figure); a
  separate per-km charge of the annual total would double count it. The per-km rate is the
  variable share of the head over the row's own mean annual distance.
- **Renewals provision**: **≈25% (20-30) of the total** — complete renewals only; 55-65% if partial
  renewals are excluded too — life 25-30 years (Hill App. III Table XXIII 3.6%/yr; statutory
  Abstract B loco shares 5-18% for rebuilders, 13-18% for renewers). Price Williams's "money
  life" (10.81 yr) is a payback coefficient, not a service life (NER ultimate life 25 years; PW
  models 30). His £139.91 an engine-year is a component-renewal schedule (repairs **and partial
  renewals**), not the capital share; netting it would strip boiler, tyre and tube work that
  belongs to maintenance or the overhaul fields. The capital share is net cost ÷ service life,
  about £60-75 an engine-year. Rung 1.
- **fixed/per-km split of the routine remainder: steam 65/35; diesel/electric 60/40** (rung 2/3, low to
  low-medium). Steam: known distance items are only about 12% of the per-train-mile cost (tyres
  0.052pence per mile, boiler 0.24pence per mile) but axle exams (250,000 miles) and tyre lives are mileage-gated
  while painting and boiler-washing are calendar-gated; Hill's text finds little mileage relation.
  Diesel/electric: exam intervals in engine-hours and cleaning hours are time-like, yet ORR's 2026
  result finds mileage highly significant with an acknowledged fixed component. Direction: Price
  Williams-style component tables generalised; TNA RAIL cost-per-train-mile series; ORR RSMR final
  coefficients.
- Overhaul: the table above (steam 2-3/7-year ladder; diesel 2.75/5.5/11-year). Upgrades:
  reboilering 20-27%, heavy rebuild 30-35%, donor-parts conversion 85-100% (below).

### Multiple units

- **Renewals provision: 0 per cent.** The research pass 45 ladder is a total-maintenance figure
  with vehicle renewal and the capital lease outside it, so no renewals deduction is taken.
- **Fixed/per-km split of the routine remainder: 50/50** at the reference duty. The table gives
  100,000 km a car-year before 1960, 120,000 km from 1960 to 1999 and 161,000 km from 2000
  (100,000 miles); tube, LUL, Underground, DLR, Docklands and Tyne & Wear stock take 120,000 km
  in every era. Modern anchors: ORR RSMR 2026 medians £0.72-1.88 a vehicle-mile
  (£93k-285k a vehicle-year by contract type); LU levels 1-3 £25,700 a car-year standing; the
  lease form is standing + mileage (Porterbrook accounts). Direction: ORR RSMR final
  coefficients; SPARK MR-MEA-005 (Class 150/1 typical maintenance costs).
- Overhaul: 15 per cent of A, event 1.2A every eight years, first event 0.70 of the maximum over
  three. Report 45 recommends five years before 1948 and six years to 1999, both ESTIMATE; the
  workbook uses eight years for the whole fleet. Upgrades: refresh 8-12%, re-tractioning 20-25%
  (below).

### Road vehicles (buses, coaches, lorries, vans)

**Renewals provision: 0 per cent**: CM and municipal "maintenance" figures exclude depreciation by convention — it is a
separate line in the same tables. Lives: bus 12-15 years (8-10 pre-war), lorry 6-8 first life
(report 40 §2). The same figures state that major repairs are inside the maintenance item
("washing, servicing and major repairs"; "repairs and overhauls"), so the annualised overhaul
provision is deducted from them, and only from them
([source-composition](source-composition.md)).

Enter as **absolute standing + per-km, not percentages** (report 40 §5): the fixed share is a
function of duty — 47% → 22% as a bus's weekly mileage goes 200 → 600.

| Sub-class | Standing (fixed_cost basis) | Distance (runningcost basis) | Fixed share at class duty | Rung |
|---|---|---|---|---|
| Bus | ≈ £52-87/vehicle-year (1959: 19s 10d-£1 13s 4d a week) | 1.2-2.2 pence per mile | 22-25% at 31,200 mi/yr; 47-49% at 10,400 | 1 (measured, CM 2 Jan 1959, three duty levels) |
| Coach | bus curve, high-duty end | as bus | 20-30% | 2 |
| Lorry | ≈ £4,400/vehicle-year (2016) | 13.6 pence per mile | 33-39% at 50-65,000 mi/yr | 1 (measured, FTA 2016 bands decomposed) |
| Van | bus/lorry interpolation | as above | 35-45% at ~25,000 km/yr | 3-4 (duty interpolation of the 1959 curve) |

The 75/25 distance/standing rule is the busy-urban-duty check; the entered values are the
absolute forms. What would move these: a second multi-mileage CM table (bus/coach),
FTA originals with more bands (lorry), a 1930s CM van table at multiple mileages (van).

### Trams and light rail

**The measured annual total is the envelope (research passes 47 and 49).** The annual figure A
is in 1900 money a car-year at 48,000 km (90,000 km from 1990). The pre-1950 series is the
Ministry of Transport gross car-only figure: 84 at 1900-13, 131 at 1920, 106 at 1931, 89 at
1939, with renewals inside. The 1950-90 rung is **150 repairs-only** (band 130-210), from the
measured Sheffield 1949-50 repairs line of 147.3; renewals are outside that head
([report 49](../cost-balancing/research-pricing-report-49.md)). The 1990-2026 value is 1,177
from the 2011 Nottingham Express Transit availability contract, a different scope again. The
scope changes at 1950 and 1990 are source changes, not arithmetic errors; each row's note states
which basis it uses. The historic series covers cars and equipment only; permanent way, line
electrical equipment, power, traffic, rates, insurance and general expenses are outside it.

**Deductions and split.** Pre-1950 gross rows deduct renewals at 35 per cent of A (central; the
only measured share is Dewsbury 1885 at 26 per cent, band 26-50) and a works-overhaul provision
of 28 per cent of A at two years; the event is 0.35A for the first overhaul rising to 0.75A
over three, 96,000 km, 0.4 months. The 1950-90 repairs-only rows deduct no renewals and a
28 per cent works-overhaul provision at three years; the event is 0.54A for the first overhaul
rising to 1.15A for the late-life overhaul, a mean of 0.85A, 144,000 km, 0.5 months. Modern
rows deduct no renewals and a 6 per cent provision at twelve years; one event of 0.75A,
1,080,000 km, 0.8 months. The continuous head is A less renewals less the provision, split
50/50 standing and distance (the measured band for the standing share is 40-55 per cent). The
1950-90 rung remains an estimate constrained by the Sheffield measurement; the research route is
the Ministry "Tramways and trolley vehicle undertakings" volumes and the Glasgow, Sheffield and
Blackpool accounts.

**Rebuilds are upgrades, not overhauls.** The 1934 London County Council E/1 rebuild at GBP 400
a car (20-27 per cent of a new car) and the 2026 Supertram life extension at GBP 856,000 a tram
(43-50 per cent of a new tram) are `upgrade_price` events. The workbook uses 0.22 of the new
price for trams introduced up to 1950, rising linearly to 0.50 by 1990 and held at 0.50 after
that. The Metrolink 2004 mid-life refurbishment at GBP 80,000 is the modern works overhaul
(about 8 per cent of a new T68), not an upgrade.

**What would move it.** A measured municipal tramcar repairs figure after 1950; a works order
for a two-yearly complete overhaul at Charlton, Coplawhill or Kirkstall; a measured renewals
share for electric tramcars; a measured modern heavy-exam interval.

### Ships and inland boats (powered)

- **Motor/steam ships: 50-65% standing** (rung 2/4): calendar pieces are measured (drydocking
  US$1.2-2.3m per 2.5-5-year cycle; Drewry's annualisation is survey + dock divided by five;
  Kirkaldy 1913 annual overhaul 2% of capital); the usage share is machinery and voyage repair, per
  hour at sea (≈ per km at 9-12 knots). **Renewals provision**: the recorded ship figures exclude depreciation
  (Martin states "maintenance repairs only, paid from a depreciation reserve; excludes
  depreciation itself, insurance and fuel"), so no renewals share is deducted from them, and no
  source states whether works overhauls are inside a ship repairs figure, so no overhaul
  provision is either: the composition table leaves the ship heads undecomposed. Life 25-30
  years. What would move it: Drewry App. 11/12 values (paywalled); P&O repair ledgers (RMG
  archive).
- **Inland motor boats: 60-75% standing** (rung 3): every measured inland figure is per-year or
  per-job (blacking every 2-3 years, BSS every 4, docking every 3); engine wear is the only clear
  usage item. What would move it: GUCCCo account books BW58/3/1/7.
- **Sailing craft: standing only** (rule 2). Level: Martin's 5%-of-capital/yr working figure; the
  one measured component is sheathing £120/yr on a 400-500-ton ship (1862). Measured levels from
  the barque account books at Royal Museums Greenwich (*ELEANOR DODSON* AMS/36; *BURNS* MSS/77/063).

### Aircraft

**Renewals provision: 0 per cent** on CAA-style maintenance figures (lives 20-25 years, depreciated separately — KPMG/
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
wages (staff are charged separately) — measured, rung 1. A pair takes twice the figure, 90 a
year. The overhaul is the replacement at the end of working life, 100 per cent of the purchase
price at 70,000 km (the seven-year Leeds cadence at 10,000 km a year). Horse vehicles: all
repair accounts are per-year (1760s coach £70 a coach-year, about 70% of capital; no horse-drawn
goods repair account exists). Enter the whole maintenance figure in `fixed_cost`, `runningcost`
0. Every animal row uses this rule, including the six horses on the tram sheet.

### Narrow gauge and maglev

**Narrow gauge.** The gauge is not a variable in any carriage, wagon or locomotive
source, so the narrow-gauge vehicles take the class rules unchanged, and all 73 carry both a
continuous head and an overhaul target:

- **34 carriages**: the carriage era bands (28 / 24 / 19 / 12 / 10 / 8 per cent of A at 6 / 5 /
  3 / 2 / 2 / 2.6 years), the measured total as the envelope. Many of these rows had also
  inherited the modern mainline carriage duty of 172,600 km a year as a family default; it is
  corrected to 40,000 km a year, inside the measured 29,000-41,000 km a carriage-year of 1892.
- **14 wagons and vans**: head = 0.8A, overhaul event = 1.2A every six years at the 40,000 km/yr
  reference duty.
- **17 locomotives**: the class profile every other locomotive carries (steam 5 and 15 per cent
  of capital over four events at 150,000 km, the Festiniog archetype; diesel 7 and 20 over three
  at 300,000 km). These are the one rail group still on a capital share rather than a measured
  envelope; see the open question below.
- **3 horses**: the replacement at 100 per cent of the purchase price at 70,000 km (standing
  rule 2). The same correction was applied to the 16 animal rows on the other sheets, which
  pass 40 had given the locomotive, tram or ship overhaul because it keyed on the sheet rather
  than on the animal.
- **5 multi-part sections**: zero, the leading unit carrying the consist.

**Maglev** remains on the overseas-system analogue; see [maglev-costs](maglev-costs.md).

## Upgrade costs

Measured events and the full class-rule table: [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md)
§4. Rules in force (each % is of the TARGET vehicle's price; basis in the report):

- **Unfitted → fitted brake pairs (the 30 carriage/van pairs): 7.7%** — measured £35 a carriage
  against £398-518 (1879); wagons 10-20% (Aspinall £10-20 on a £85-95 wagon; 20-33% after 1922).
- Diesel heavy rebuild 30-35% (Class 47→57, measured); re-engine only 10-15%; steam reboilering
  20-27% (boiler share, measured); steam donor-parts class conversion **85-100% of new** (Grange
  £5,000 — not a cheap conversion); multiple-unit refresh 8-12% / re-tractioning 20-25%; carriage structural
  conversion 25-30%; bus refurb 25-30% / rebuild 50%; lorry rebuild 50%; tram rebuild 22% for
  pre-1950 stock rising linearly to 50% by 1990 (research pass 47; the 1934 LCC E/1 and 2026
  Supertram measured rebuilds); aircraft cabin variants **1-5%** (reject the blanket 50% for
  variant links; P2F is measured at 4-8% of new list).

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
- **Mean annual distance.** The class and era table is in
  [mean-annual-distance](mean-annual-distance.md). The outstanding gaps are road annual
  distances, the ship annual distance and aircraft utilisation. The carriage 1920 and 1950 levels
  were closed by pass 62 on report 51; the locomotive 1914-48 and post-1977 levels were closed by
  pass 63 on report 50 (the Class 92 override; the 1995 rung remains derived).
- Do Hill's repairs contain works overhauls? Until a company repair account (or the post-1911
  "Repairs and partial renewals" column) itemises a heavy general inside the repairs element, the
  rail rows deduct renewals only.
- What composition does each recorded-as-unrecorded head have (the water 2-per-cent rule, the
  aircraft 20-per-cent rule, the modern tram contract, the FTA trailer line)? Each row's note
  names the passage that would settle it; the full list is in
  [source-composition](source-composition.md) "Open questions".
- The trailer refurbishment composition is unmeasured: the FTA line gives no workscope, and the
  0.33-of-capital event is a measured refurbishment price applied to an unmeasured annual total.
