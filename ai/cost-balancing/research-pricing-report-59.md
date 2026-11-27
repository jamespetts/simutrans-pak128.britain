---
status: draft
verified: New ex-15 @ 81ffb5911 (working tree) + pass 74, 2026-11-27
  engine: simutrans-extended-sources ex-15 @ ebf26cfb9b
---

# Research report 59: the four gap classes

**Covers**: the four cost classes that had no usable target before the 2026-11-27 work - tram
permanent-way maintenance, depot capital, maglev guideway maintenance and station extension
buildings - with the evidence found, the estimate made where no measurement exists, the value
entered in each workbook, and the research that would replace each estimate.

**Companions**: [handoff](handoff.md) (standing rules and the outstanding work),
[research report 16](research-pricing-report-16.md) (depot and tunnel maintenance measurement),
[research report 13](research-pricing-report-13.md) (tram rail price and weight),
[infrastructure-cost-evidence](../infrastructure-cost-evidence.md),
[cost-data-coverage](../cost-data-coverage.md) and
[cost-balancing-register](../cost-balancing-register.md).

**Claim tags**: `[CODE New ex-15 @ 81ffb5911]` for pakset and workbook facts;
`[CODE simutrans-extended-sources ex-15 @ ebf26cfb9b]` for engine facts;
`[LITERATURE:...]` for external sources read in this pass; `[UNVERIFIED]` for an inference that
the stored evidence does not settle. Evidence class is marked MEASURED, STATED, DERIVED,
ESTIMATE or UNAVAILABLE.

**Units.** GBP1900 means pounds of 1900. A raw `.dat` or `config` unit is not money:
capital for a way is raw x 0.00396311 per kilometre, maintenance for a way is raw x 0.09511464 per
kilometre-year, capital for a scaled building is raw x 0.00049539 per object, capital for an
unscaled building or engine setting is raw x 0.00396311 per object, and a building maintenance
field is raw x 0.01188936 per object-year. The canonical table is
[conversion-chains](../conversion-chains.md). One tile is 125 m, so one kilometre is eight tiles.

## 1. What was filled

| Class | Gap before this pass | Value now in the workbook | Basis class |
|---|---|---|---|
| Tram way maintenance, 7 running objects | no target at all | raw 446-526 a km-year; sensitivity range 297-767 on a 25-40 year renewal life | MEASURED charge, DERIVED split, ASSUMED life |
| Tram way capital | measured bind was a per-mile forge rate and produced a negative way-only value; the forge was 2.54 times its own source | bind rejected; forge 225,000 to 89,000 raw | MEASURED |
| Maglev way maintenance, 4 running objects | no target at all | raw 2,019 at grade, 2,492 elevated, band 1,077-4,153 | ESTIMATE, published planning rates |
| Maglev way capital | Munich planning figures with thin provenance | £128,000 at grade and £158,000 elevated per track-km, labour-adjusted; +2.6 and +3.8 per cent | MEASURED estimates, DEFLATED and LABOUR-ADJUSTED |
| Depot capital, 27 objects | the game charged GBP3.96-178.31 a depot; no per-object route | target GBP1,304-25,440; four settings proposed; required level per object stated | MEASURED per unit, DERIVED size |
| Depot maintenance, 27 objects | 1.5 per cent of capital target computed but no route into the game | the route is the depot `.dat` `maintenance` field; raw values 206-4,012 | MEASURED rate |
| Station extension buildings, 8 goods and mail objects | priced as passenger concourses at GBP14.8-25.6 a "place", giving GBP3,700-24,320 for goods sheds | GBP225-1,800 by floor area and function; maintenance cut from 28-228 per cent of capital a year to 1.5-5 per cent | ESTIMATE, measured rate ladder |

No `.dat` file and no `config/simuconf.tab` setting was changed. The workbook is the research
store; the `.dat` pass remains one operation, deferred by the user direction of 2026-11-25
([cost-balancing-register](../cost-balancing-register.md), "The costing pass").

## 2. Tram permanent way: maintenance and the forge double count

### 2.1 What was missing

The maintenance workbook's `Ways - tram` sheet had **no measured and no class figure** for any of
its eight rows: columns Q to Z and AA to AI were empty apart from formulas. The seven running `.dat`
objects carried `maintenance` 450-700 raw, which is GBP42.80-66.58 a kilometre-year, and no
document recorded where those numbers came from. The capital side had a separate defect: the 41 lb
row bound a measured GBP600 (1911) as pounds per kilometre, but the figure is pounds per **mile**
and is a forge rate, so the row's measured way-only value was minus 82,173 raw. `[CODE New
ex-15 @ 81ffb5911]`

### 2.2 The measured charge

The Ministry of Transport annual return for 1930-31 prints the tramway revenue account with
"Maintenance and Renewals out of Revenue" split into its component heads. The permanent-way head
is separate from electrical equipment of line, power, traffic expenses and cars:

| Item, 1930-31 | Local authorities | Companies | Total |
|---|---:|---:|---:|
| Permanent way, maintenance and renewals out of revenue | GBP 1,307,332 | GBP 328,322 | **GBP 1,635,654** |
| Permanent-way capital expenditure, works open for traffic | GBP 30,983,456 | GBP 4,823,894 | **GBP 35,807,350** |

The same return gives 383,378,799 car-miles run. The permanent-way charge is therefore
**1.024d a car-mile**, and **4.568 per cent of permanent-way capital a year**.
`[LITERATURE:Ministry of Transport, Tramways and Light Railways (Street and Road) and Trackless
Trolley Undertakings, Annual Return for 1930-31, summary table Parts I and II]`

Two independent conversions to a kilometre of single track agree within 15 per cent:

- **Through car-miles.** The return does not print route mileage in the summary table. At an
  assumed 2,400 route miles, double track, the charge is GBP211.80 per track-km-year in 1930-31
  money, which is GBP117.70 at 1900 on the general index of 180. A 2,000-2,800 mile range gives
  GBP101-141.
- **Through capital.** 4.568 per cent of the pakset tram class capital, GBP2,486-3,100 a km, is
  GBP113.56-141.61 a km-year. This route is the one entered, because it is the only one that
  scales per rail weight. It assumes the historic capital and the 1930-31 charge are on one price
  basis; they are not exactly, because the capital account is a mixture of vintages, which is why
  the car-mile route is stated as the cross-check rather than discarded.

### 2.3 Splitting renewal from routine

The engine charges renewal separately, through `weg_t::renew()` at the full way value when
`wear_capacity` is exhausted. `[CODE simutrans-extended-sources ex-15 @ ebf26cfb9b]` The
permanent-way head above is gross of renewals out of revenue, so the routine component is the
measured charge less the annualised renewal.

The way object is the whole finished street track less the forge: class capital less GBP352.70 for
the bed. At a 30-year renewal life the annualised renewal is GBP71.11-91.58 a km-year.

There are therefore **one measured quantity and one assumption**. The measured quantity is the
combined permanent-way charge, 4.568 per cent of permanent-way capital a year, or 1.024d a
car-mile. The assumption is the renewal life, which is needed only because the engine charges
renewal separately and because the measured charge is gross of it. The 30-year life is the central
case; the range 25 to 40 years produces the low and high figures in the last two columns. **The band
is not a measured range, and it did not exist in the workbook before this pass.** It is a
sensitivity range on the one assumption that the measurement does not settle.

| Object | Class capital GBP1900/km | Combined charge at 4.568% | Renewal at 30 years | Routine | Raw entered | Low, 25-year life | High, 40-year life |
|---|---:|---:|---:|---:|---:|---:|---:|
| 41 lb/yard | 2,486 | 113.56 | 71.11 | 42.45 | 446 | 297 | 633 |
| 55 lb/yard | 2,637 | 120.46 | 76.14 | 44.32 | 466 | 306 | 666 |
| 75 lb/yard | 2,852 | 130.28 | 83.31 | 46.97 | 494 | 319 | 713 |
| 85 lb/yard | 2,960 | 135.21 | 86.91 | 48.30 | 508 | 325 | 736 |
| 92 lb/yard | 3,036 | 138.68 | 89.44 | 49.24 | 518 | 330 | 753 |
| 98 lb/yard | 3,100 | 141.61 | 91.58 | 50.03 | 526 | 333 | 767 |
| Heavy (rail-compatible) | 2,960 | 135.21 | 86.91 | 48.30 | 508 | 325 | 736 |

The same table is now in the `Ways - tram` sheet at rows 17-29, with the current `.dat` value in
column I, so the comparison can be read without leaving the workbook.

The seven running `.dat` values in force are 450, 450, 525, 485, 600, 700 and 600 raw, with the
mothballed track at 0. Every one of them is **inside the sensitivity range**, and three of the seven
are within 10 per cent of the 30-year central value. The gap here was documentation rather than a
wrong number, but the qualification matters: a different renewal life would put all of them outside
the range, and the `.dat` figures have no recorded basis of their own. The `.dat` pass should
replace them with the central values and record the derivation beside them.

### 2.4 The forge and the measured bind

The audit of 2026-11-26 recorded that `forge_cost_tram` was 225,000 raw, 2.54 times the GBP600 a
mile from which it was derived ([way-cost-audit-2026-11-26](way-cost-audit-2026-11-26.md) §3.4).
GBP600 a mile in 1911 is GBP352.70 a kilometre at 1900, which is **89,000 raw**. The forge is the
trench, concrete bed and reinstatement; the way object carries the rails, fastenings, setts and
paving, which is what the complete street track of GBP5,050 a mile in the same source contains.
`[LITERATURE:Encyclopaedia Britannica, 11th edition (1911), "Tramway", by Emile Garcke;
infrastructure-cost-evidence §6]`

The measured GBP600 on the 41 lb row is rejected: it is the forge rate, not a per-kilometre
capital price. The row now uses its class value, and no way-only value on the tram sheet is
negative. The forge change is in the workbook and the Params sheet; the live `simuconf.tab`
setting is still 225,000 and **the config change is outstanding**.

## 3. Maglev guideway capital and maintenance

### 3.1 What was missing

The maintenance workbook's `Ways - maglev` sheet had no target for any row, and the maintenance
generator returned nothing for the waytype
([way-cost-audit-2026-11-26](way-cost-audit-2026-11-26.md) §4.6). The capital rows carried the Munich
planning figures but the provenance was thin. `[CODE New ex-15 @ 81ffb5911]`

### 3.2 The guideway capital, labour-adjusted

A research subagent was commissioned on 2026-11-27 to price the guideway from overseas systems with
a documented labour adjustment, because no mainline maglev exists in Britain. Its method is:

```
adjusted = source cost x [(1 - L) + L x R]
```

where `L` is the labour share of the works and `R` is United Kingdom construction labour cost per
hour divided by the source country's. The labour share is taken as **0.25, band 0.13-0.40**, from the
Welsh Government's A487 New Dyfi Bridge priced bill of quantities (13.2 per cent site labour) and a
Maine Department of Transportation contractor survey (about 40 per cent including overhead labour).
`R` is **1.09** for Germany (Eurostat `lc_lci_lev`, construction, 2008 and 2016), **6.5, band
5.5-7.5**, for China (National Bureau of Statistics 2024 construction wage, RMB 89,519 a year, and
the Turner & Townsend 2024 survey), **1.72** for Japan and **1.85** for Korea (Turner & Townsend
2024). `[LITERATURE:Eurostat lc_lci_lev; National Bureau of Statistics 2024; Turner & Townsend
International Construction Market Survey 2024]`

The guideway-scope figures, deflated to 1900 on the infrastructure index and then labour-adjusted:

| Source, year | Scope | GBP1900 per track-km before | R | After |
|---|---|---:|---:|---:|
| Hamburg-Berlin study, 1993, at grade | beam, foundations | 129,399 | 1.09 | 132,310 |
| Hamburg-Berlin study, 1993, elevated | beam, foundations, piers | 163,289 | 1.09 | 166,963 |
| Munich Transrapid, 2007, at grade | foundations, deck, piers | 124,195 | 1.09 | 126,990 |
| Munich Transrapid, 2007, elevated | as above | 151,863 | 1.09 | 155,279 |
| Shanghai residual, 2004, central | girders, piers, piles, bearings | 71,595 | 6.5 | 170,038 |
| Changsha unit rate, 2022, viaduct only | superstructure and piers | 38,799 | 6.5 | 92,148 |
| Changsha unit rate, 2022, with track panel | plus F-rail and reaction plate | 54,606 | 6.5 | 129,689 |
| Linimo, 2005, upper bound | piers, girders, station civils, tunnel | 341,200 | 1.72 | 402,616 |
| DLR City Airport viaduct, 2005, UK | elevated light-rail viaduct | 185,619-234,467 | 1.00 | unchanged |

The two German estimates, fourteen years apart and independently derived, agree within 4 per cent at
grade and 7 per cent elevated once both are on one price basis. That is the strongest finding: it
confirms the figures the workbook already carried. The rows and their sources are in
`research-pricing-rows-59b.csv`. The recommendation is:

- **At grade: GBP128,000 per track-km, band GBP105,000-160,000.**
- **Elevated: GBP158,000 per track-km, band GBP130,000-195,000.**
- **Confidence: medium.** The at-grade-to-elevated ratio is 0.81, which the two German sources give
  independently as 0.79 and 0.82.

Against the workbook values of GBP124,786 and GBP152,238, that is +2.6 and +3.8 per cent. The
existing figures were right within the uncertainty of the evidence; the change is a restatement, not
a correction. Two cautions carry into the record: the German figures are engineering estimates from
DB AG bridge-cost tables rather than quantity take-offs, and the at-grade guideway is nearly as
expensive as the elevated one because it is a bridge-type superstructure, not ballasted track on a
formation.

### 3.3 The guideway maintenance rate is about eight times too high

The evidence found for guideway maintenance is far below the figure pass 74 used:

| Source | Per cent of guideway capital a year | Tag |
|---|---:|---|
| Transrapid planning figure, cited 1994 | 0.08 | published |
| CIGGT Los Angeles-Las Vegas study, cited 1994 | 0.12 | published |
| Volpe 1992 model, derived from material and 200 labour-hours a mile-year | 0.215 | derived |
| Morgantown PRT, measured 1987-1992 | 0.008-0.031 | measured |

The recommendation is **0.15 per cent of capital a year on the concrete structure, band 0.08-0.25
per cent**. On the elevated guideway that is **GBP237 a track-km-year, raw 2,492**, against the
GBP1,826.86 (raw 19,207) that pass 74 entered.

The pass 74 figure was not irrational: 1.2 per cent is a defensible rate for stator packs, guidance
rails and line-side equipment. The error was to apply it to a capital base that contains only the
concrete structure. A structure rate of 0.15 per cent plus an equipment rate of 0.5-1.0 per cent is
the coherent treatment **only if the equipment is in the capital**, and in this pakset it is not.
The maintenance field therefore carries the structure alone.

One consequence must be stated. The pakset maglev ways have **no `wear_capacity`**, so the engine
never renews them and this field is the whole recurring charge. The 0.15 per cent is a
planning-study maintenance figure, not a whole-life replacement provision; if a wear capacity is
added later, the renewal should move there. `[CODE New ex-15 @ 81ffb5911]`

| Object | Class capital GBP1900/km | Routine at 0.15% | Raw entered | Band, 0.08-0.25% |
|---|---:|---:|---:|---:|
| Concrete maglev track, at grade | 128,000 | 192.00 | 2,019 | 1,077-3,364 |
| Concrete maglev track, elevated | 158,000 | 237.00 | 2,492 | 1,329-4,153 |
| Lightweight concrete, at grade | 128,000 | 192.00 | 2,019 | 1,077-3,364 |
| Lightweight concrete, elevated | 158,000 | 237.00 | 2,492 | 1,329-4,153 |

### 3.4 The linear motor is charged nowhere

There is no maglev electrification way object in the pakset: no `Obj=wayobj` with
`waytype=maglev_track`. The Munich study prices the parts that are therefore uncharged, per
track-km in 1900 money:

| Munich line item | GBP1900 per track-km |
|---|---:|
| Stator support rail | 10,391 |
| Stator winding cable | 5,656 |
| Substations and line cables | 40,271 |
| Operation control | 24,224 |
| **Total** | **80,542** |

Keeping the way at structure-only scope is correct and consistent with rail ways, which exclude
electrification because a separate way object exists. The maglev way object is a separate task, and
until it exists maglev is under-priced by the linear motor alone (GBP16,047 a track-km, 12.5 per cent
of the at-grade guideway) and by up to GBP80,542 if the line-side power and control are also
attributed to it. `[CODE New ex-15 @ 81ffb5911]`

### 3.5 The rolling-stock rate is coherent, and that is the useful finding

The maglev vehicle maintenance figure was already entered at 0.00010257 GBP a seat-km, from
EUR 0.011 a seat-km at 2009 prices (Almujibah and Preston 2018), applied at an assumed 300,000 km
a vehicle-year ([vehicle-cost/maglev-costs](../vehicle-cost/maglev-costs.md)). The apparent
weakness is that the figure is a rate per seat-kilometre, not a per-year account. The check made
in this pass is whether the resulting annual figures are of a sane order against the other
vehicle ladders.

They are, and remarkably so: every maglev row's annual maintenance is **2.8 per cent of its own
class capital**. The passenger cars carry 54 seats at GBP1,088 a seat, the freight cars are priced
per metre at GBP4,194.60, and in both cases the annual figure is the same share of capital. That
is inside the measured band for aircraft (2.5-5 per cent), ships (2 per cent) and rail carriages
(about 3 per cent). `[CODE New ex-15 @ 81ffb5911]` The vehicle maintenance therefore needs no
change; what it needed was the cross-check that shows the per-seat rate is not producing an
absurd annual figure. The per-seat presentation does, however, apply the rate to payload tonnes on
the box and flat cars, which is conceptually wrong even though the resulting figure passes the
capital test. The research that would settle it is in section 7.

## 4. Depots: capital, maintenance and the engine's price mechanism

### 4.1 The mechanism, as the engine implements it

A depot is a `building` with `type=depot` and `noconstruction=1`. Its `cost` field is never
charged. The build tool charges:

```
price = cost_depot_<waytype> * desc->get_level()
```

`case tram_wt`, `narrowgauge_wt`, `maglev_wt` and `monorail_wt` all take `cost_depot_rail`.
`[CODE simutrans-extended-sources ex-15 @ ebf26cfb9b, simtool.cc 7966-7973 and 7999-8023]`

Two consequences follow. First, the twenty-seven depot objects share four settings. Second, the
price of a depot is the product of a global constant and a per-object integer, `level`, that the
pakset inherited from an older engine in which `level` set the depot price directly. The present
levels are 1 to 16 and bear no relation to the size of the building: a horse stable and a
twelve-road steam shed differ by a factor of twelve in price for that reason alone.

The measured per-unit rates already in `measured_infra.py` are:

| Family | Measured rate, GBP1900 | Evidence |
|---|---:|---|
| Rail running shed | 750 a road | plain running shed GBP558-932 a road, Malton 1853 to Rowsley 1922 |
| Road garage | 187 a bus | GBP800 a bus Coventry 1954, GBP500 a bus 1929 |
| Tram depot | 478 a car | Hyde Road 1915, GBP512 a car; GBP203-357 in 1901 |
| Stable | 208 a horse | GBP117-250 a horse, 1889-95 |
| Shipyard | 1,304 a slip | patent slip GBP450-1,900, 1832 |
| Hangar | 13,812-25,440 a stand | RAF standard hangar GBP25,000, 1938; Grimsby GBP2,526, 1937 |

### 4.2 What the game charges now, and what it should

`cost_depot_rail` is 2,000 raw and `level` is 12 for the steam depot, so the game charges
24,000 raw, **GBP95.11**, against a measured target of GBP3,000. The air hangar is GBP178 against
GBP25,440. Every depot is between 27 and 200 times too cheap. `[CODE New ex-15 @ 81ffb5911]`

The proposal is to make the setting a **measured price per unit of size** and `level` the size:

| Setting | Current raw | Proposed raw | GBP a level | Covers |
|---|---:|---:|---:|---|
| `cost_depot_rail` | 2,000 | **189,245** | 750 | track, narrow gauge, tram, monorail, maglev |
| `cost_depot_road` | 1,000 | **47,185** | 187 | road |
| `cost_depot_ship` | 4,000 | **329,035** | 1,304 | water |
| `cost_depot_air` | 7,500 | **4,729,871** | 18,745 | air |

Every depot object's required level is in column AI of the `Depots` sheet and in section 9 below.
**None of the four settings is applied.** They are stored in savegames and the user decision is
outstanding. `[CODE simutrans-extended-sources ex-15 @ ebf26cfb9b, dataobj/settings.cc 2792-2795]`

The `Depots` sheet now records the actual costs as data, so the decision can be taken from the
workbook rather than from this report: column AK the .dat `level` in force, AL the measured cost per
unit, AM the measured target, AN the charge the game makes today, AO the target-to-current ratio and
AP the constraint wording "cost_depot_<waytype> x level only". The block below the table states the
two possible treatments.

**The choice is between two treatments, and it is a design decision rather than an arithmetic one.**

- **Change the engine** so that a depot with an explicit cost field is charged that cost, falling
  back to `cost_depot_* × level` when it has none. The proposal and the code are in
  [engine-bugs](../engine-bugs.md) §4. Every depot then carries its measured target directly, the
  `level` field returns to meaning a size, and no per-object compromise is needed.
- **Use `level` to represent the whole cost.** Keep the engine as it is, set each of the four
  settings to the measured price per unit, and set each depot's `level` to the quotient that
  reproduces its target. The required level is in section 9. This works arithmetically for every
  object, but `level` then encodes the price rather than the size, so a depot's displayed level no
  longer means anything physical, and one setting still cannot distinguish traction within a
  waytype.

The first option is the better one on every ground except the work involved. The second is the only
option that needs no engine release, and it is the one the workbook currently supports with column
AI. Nothing should be applied until the choice is made.

Two limits must be stated with the proposal.

- **One setting cannot distinguish traction within a waytype.** A rail horse stable and a twelve-road
  steam shed both use `cost_depot_rail`. The required level absorbs the difference, but then
  `level` is a price quotient rather than a size, which is circular. The table in section 9 gives
  the level that reproduces each target; a reader should treat it as a proposed size, not as a
  measurement.
- **The air setting is a compromise.** The 1938 hangar target is GBP13,812 and the modern one
  GBP25,440. The setting entered is their geometric mean, GBP18,745, so each object is 26-36 per
  cent from its target. One value cannot do better.

### 4.3 Depot maintenance

The maintenance workbook already computes 1.5 per cent of capital a year (report 16: Seeley 1 per
cent, light industrial 1.6, BMI 2.5, Midland Railway 0.19-0.39 of department spending). The
column's suggested `.dat` value is 206-4,012 raw. What was missing was the route into the game.

The route is the depot building's own `maintenance` field, and it works: `building_desc_t` sets
`scaled_maintenance = maintenance` when the file is read, and only the station buildings are
rescaled afterwards, so a depot's field is charged **unscaled** at 0.00792622 GBP per raw per
month. `[CODE simutrans-extended-sources ex-15 @ ebf26cfb9b,
descriptor/reader/building_reader.cc 670-671; simworld.cc 3567]`

The engine default that applies when the field is absent is `maintenance_building x level`, which
is a 1990s Standard-era formula (1,800 raw a level) and is not evidence of anything. The present
depots therefore pay 0.5-8.6 per cent of capital a year in maintenance by accident of their
`level`, where the measured rate is 1.5. Setting the field fixes it.

**Caution for the `.dat` pass**: set `level`, the `maintenance` field and the `cost_depot_*`
setting together. Changing `level` alone changes both the capital and the default maintenance.

## 5. Station extension buildings

### 5.1 The error

Eight `type=extension` buildings carry goods or mail capacity: FluidStorageStation,
BulkGoodsBunker, CarYard, GoodsWarehouseOld, GoodsWarehouseModern, LivestockPen, OldPostOffice
and ModernPostOffice. Their `capacity` is a goods or mail capacity (250 units for the goods
buildings, 850 and 950 for the post offices). The workbook priced every one of them at the
**passenger** rate: "station building per passenger-place, standard class at GBP14.8 a place;
times 250 places". That produced GBP3,700 for a goods bunker and GBP24,320 for a modern post
office. `[CODE New ex-15 @ 81ffb5911]`

The **six goods objects** share one `.dat` cost, 1,150,000 raw = **GBP569.70**, and one maintenance,
15,000 raw = **GBP178.34 a year, which is 31 per cent of capital**. The post offices are
GBP421.08 and GBP495.39, at 28 and 228 per cent of capital a year. The capital figures were,
almost by accident, of the right order; the workbook target would have multiplied them by 6.5, and
the maintenance field is the station-maintenance conflict recorded in
[infrastructure-cost-evidence](../infrastructure-cost-evidence.md) §11.

### 5.2 The method

A goods shed is a building, so it is priced as a building: floor area times a measured rate per
square metre for its construction. The area is inferred from the function, using the measured
36 ft (11 m) width of a standard goods shed
`[LITERATURE:Minnis and Hickman, The Railway Goods Shed and Warehouse in England (Historic
England, 2016), design section]`. The rate ladder is measured:

| Building class | GBP1900 a m2 | Evidence |
|---|---:|---|
| Minimal brick store | 1.24-2.00 | Tudwick Road, 21 ft x 15 ft 6 in, GBP40 in 1912, deflated on the general index of 107 |
| Goods shed, brick or timber | 2.50-3.25 | light-industrial shed band GBP2.91-4.60 (Glasgow Larkfield GBP5.45/m2 1929, Lincoln GBP8.61/m2 1928, deflated on 187) |
| Station building with offices and facilities | about 6.00 | Low Street, 1861: one brick building and 200 ft of platform for GBP610 |
| Hangar | 250-750 | measured modern band, for scale only |

The maintenance share is the measured brick share of capital, 0.8-1.5 per cent, raised to 1.5-2.5
for steel and concrete and 4-8 for timber.

| Object | Building | Area m2 | Rate | Capital GBP1900 | Raw entered | Maintenance GBP/yr | Raw entered |
|---|---|---:|---:|---:|---:|---:|---:|
| GoodsWarehouseOld | brick or timber goods shed | 250 | 2.50 | 625 | 1,261,635 | 31.25 | 2,628 |
| GoodsWarehouseModern | steel-framed goods shed | 400 | 3.25 | 1,300 | 2,624,202 | 26.00 | 2,187 |
| BulkGoodsBunker | brick bulk goods bunker | 100 | 5.00 | 500 | 1,009,308 | 7.50 | 631 |
| FluidStorageStation | tank farm | n/a | n/a | 750 | 1,513,963 | 15.00 | 1,262 |
| CarYard | surfaced car yard | 1,000 | 0.50 | 500 | 1,009,308 | 10.00 | 841 |
| LivestockPen | open timber pen | 150 | 1.50 | 225 | 454,189 | 11.25 | 946 |
| OldPostOffice | brick sorting office | 200 | 4.00 | 800 | 1,614,893 | 12.00 | 1,009 |
| ModernPostOffice | concrete or steel sorting office | 400 | 4.50 | 1,800 | 3,633,510 | 36.00 | 3,028 |

The result is that the six goods objects' existing GBP569.70 is close to the derived GBP225-1,300,
and the two post offices are **underpriced** by 2 and 3.6 times. The maintenance is overpriced by
5.7 to 31 times. The passenger station buildings and terminals are unchanged: they really are
passenger buildings and the per-place method fits them.

### 5.3 What is and is not being checked

There is **no measured price for a British goods shed, warehouse, tank farm, car yard, livestock pen
or post office sorting office** in the knowledge base. The `.dat` values therefore cannot be shown
to be right from measurement, and this report does not claim that they are. What can be checked,
and what the workbook now shows in columns AI to AN of `Stations & bus stops`, is:

- **The rate per square metre** against the measured building ladder: a minimal brick store at
  GBP1.24-2.00 a square metre (Tudwick Road, 1912), a light-industrial shed at GBP2.91-4.60
  (Glasgow Larkfield and Lincoln bus garages, 1928-29), a station building with offices at about
  GBP6.00 (Low Street, 1861). The rates assigned, GBP1.50-5.00, sit inside that ladder.
- **The inferred floor area** against the function: a standard goods shed is 36 ft (11 m) wide, and
  the lengths assigned, 18 to 36 m, are those of a country goods shed rather than a city warehouse.
  This is the weakest link: the pakset records no floor area, and the area is inferred from what the
  building is for.
- **The capital against the current `.dat` value**: the ratio is in column AM. It ranges from 0.88
  to 3.63, so the existing values are the same order of magnitude, which is the only test the
  evidence supports.
- **The maintenance share** against the measured brick band of 0.8-1.5 per cent of capital a year,
  and the timber and concrete bands of 4-8 and 1.5-2.5 per cent.

If a measured goods-shed or sorting-office price is found, it should replace the area-times-rate
derivation entirely, and the `.dat` value should be set from it. The routes to one are in section 7.
The eight extension rows are marked `ESTIMATE` in column AN for this reason.

## 6. What was applied and what was not

Applied to `New/cost-balancing-capital.xlsx`:

- `Ways - tram`: forge 225,000 to 89,000 raw on the eight rows; the 41 lb measured bind cleared;
  notes and the rejection stated on the row.
- `Params`: `FORGE_TRAM` 89,000 with the outstanding-config note.
- `Depots`: column AI "Required level", column AJ "Setting implied by the present level", notes on
  every row, and the settings block at rows 35-42.
- `Stations & bus stops`: the eight extension rows re-priced and re-based.
- `Engine settings`: the four `cost_depot_*` rows carry the measured per-unit rate and the
  proposed raw value.
- `Ways - air`: the two paved-runway measured binds cleared. Pass 73 intended this and its
  clearing call did not take effect, because `ws.cell(r, c, None)` is a no-op in openpyxl.

Applied to `New/cost-balancing-maintenance.xlsx`:

- `Ways - tram`: measured and class target 42.45-50.03 GBP a km-year, raw 446-526, band stated.
- `Ways - maglev`: 1,497.43 and 1,826.86 GBP a km-year, raw 15,743 and 19,207, band stated.
- `Depots`: the `.dat` route stated on every row.
- `Stations & bus stops`: the eight extension rows re-based and re-priced.

Applied to neither: any `.dat` `cost` or `maintenance` value, and any `config/simuconf.tab`
setting. The live `forge_cost_tram` remains 225,000. The four `cost_depot_*` settings remain
2,000 / 1,000 / 4,000 / 7,500.

**Pass 75** (`wb_fv_pass75.py`) makes the derivation visible and checkable in the sheets:

- `Ways - tram` (maintenance): columns AR-AS with the 25-year and 40-year values, and a
  derivation block at rows 17-29 showing the class capital, the measured combined charge, the
  annualised renewal, the routine component, the raw value and the current `.dat` value, with the
  measured-assumed distinction stated in three notes.
- `Ways - maglev` (maintenance): columns AR-AS at 0.75 and 2.0 per cent.
- `Depots` (capital): columns AK-AP with the level in force, the measured cost per unit, the target,
  the charge the game makes today, the ratio and the constraint; and a four-line note stating the
  engine-or-level choice.
- `Stations & bus stops` (capital): columns AI-AN with the inferred floor area, the rate, the
  derived capital, the current `.dat` capital, the ratio and the evidence class.

**Pass 76** (`wb_fv_pass76.py`) applies the labour-adjusted maglev research of 2026-11-27:

- `Ways - maglev` (capital): class prices to GBP128,000 at grade and GBP158,000 elevated per
  track-km, with the labour-adjustment basis and the uncharged linear-motor note.
- `Ways - maglev` (maintenance): 0.15 per cent of capital a year, raw 2,019 and 2,492, with the
  0.08-0.25 per cent band in columns AR-AS.

The workbook's maglev rows are now consistent with the text in section 3. The earlier pass 74
figures (1.2 per cent, raw 15,743 and 19,207) are superseded. The evidence rows are in
`research-pricing-rows-59b.csv`.

Verification: the vehicle coherence audit still passes (3,539 vehicles, 3,265 envelopes, 0
failures) and the distance check still reports 1,524 rows with 0 deviations over 10 per cent. The
generosity shading was re-run after the value changes and covers 14,847 cells.

## 7. Further research that would make these figures accurate

Ordered by how much each would change a number, not by how easy it is.

**1. Tram route mileage and car-mileage by undertaking, 1925-1935.** The single largest
uncertainty in the tram maintenance figure is the conversion from pence per car-mile to pounds per
track-kilometre-year, which needs route mileage. The 1930-31 return's Part IV prints "length of
line open for traffic"; the summary table read for this report does not. The volumes are on
archive.org as `railways00609100`, `railways00609133`, `railways00609101` and `railways00590412`,
and the 1930-31 volume is also at `ekeving.se/ext/uk/TW-LR-TT_1931/`. One page (Part IV) would
narrow the band from GBP101-141 to a single figure. `[LITERATURE:MoT return 1930-31, contents
page]`

**2. A tram permanent-way renewal account.** The 30-year renewal life is an inference. A municipal
tramway's renewal fund account would give the actual relaying cycle and the share of the
permanent-way head that was renewal rather than routine. The same returns' Part III prints
"expenditure during the year on renewals charged to Funds", separately from the revenue head; the
full return would give it by undertaking. This would replace the 30-year assumption with a
measured split.

**3. A measured maglev guideway maintenance line.** The 2026-11-27 research replaced the 1.2 per
cent estimate with 0.15 per cent, from Transrapid 0.08, CIGGT 0.12, the Volpe 1992 model 0.215 and
Morgantown's measured 0.008-0.031. What is still missing is an operator account: Shanghai Maglev
Transportation Development offering circulars through the Shanghai Clearing House, the Linimo
Railway Statistics Annual and the Incheon audit breakdown by asset class. A single annual
guideway-maintenance figure against a published route length would replace the whole band. The
routes are in [negative-findings](negative-findings.md).

**3a. A maglev electrification way object.** The pakset has none, so the stator rail and winding
(GBP16,047 a track-km in 1900 money) and the line-side power and control (GBP64,495) are charged
nowhere. This is a modelling task, not a research one: add an `Obj=wayobj` with
`waytype=maglev_track` carrying those costs, in the same way that rail electrification is a way
object. Until it exists maglev is under-priced by at least 12.5 per cent of the guideway cost.

**4. A maglev rolling-stock maintenance line and a freight-tonnage rate.** The 0.00010257 GBP a
seat-km rate passes the capital-share test on passenger cars but is applied to payload tonnes on
the box and flat cars. A per-tonne-km rate from any freight railway with high-speed stock, or the
Shanghai operator's rolling-stock line, would settle it. The Changsha heavy-maintenance
(架修) contract value is the nearest identified route.

**5. A measured depot account with both the maintenance charge and the capital value of the same
building.** Report 16 records the gap: the Midland Railway series and the BTC bus series are
system-level. A single shed or garage account stating both would replace the 1.5 per cent
benchmark with a measurement and would also let the per-unit rates be split between structure and
plant.

**6. Depot sizes, as-built.** The required-level column is a price quotient because the pakset
records no road count, bay count or floor area. Measured shed plans would give the true size of
each object: the Historic England goods-shed study, the Rowsley and Barrow Hill shed records, and
the Glasgow Larkfield and Lincoln garage plans in report 16. With real sizes the per-unit rates
could be applied without the circularity described in section 4.2.

**7. Goods shed and post office construction costs, per square metre.** The extension figures rest
on a rate ladder assembled from one small brick store (GBP40 in 1912), two bus garages and one
station building. A railway company's goods-shed contract prices would be much better. The
Historic England study cites company designs but gives no costs; the surviving candidates are the
Midland Railway station-buildings account book at the Science Museum (object 2013-7027, repair and
maintenance of station buildings, locomotive and goods sheds on the Settle and Carlisle,
1894-1901), the GER Way and Works Committee minutes (Tudwick Road GBP815 in 1905, Tiptree GBP40
in 1912), and the GWR Moor Street goods depot budget of GBP8,800 in 1910. The Science Museum book
is a **maintenance** account and is the closest thing found to a measured goods-shed upkeep
series; it should be read before any further extension-maintenance work.

**8. A post office sorting office cost.** The two post offices are the largest extension error.
Post Office property records or the Office of Works annual reports would give sorting-office
construction costs per square metre for the 1900s and the 1960s.

**9. The engine change that would remove the depot compromise.** Add an optional per-building
`cost` for depots: use `desc->get_price()` in `tool_depot_aux` when `get_base_price()` is not
`PRICE_MAGIC`, defaulting to `cost_depot_* x level` otherwise. That is a small change in
`simtool.cc` and needs no `.pak` format change, because `price` and `maintenance` already exist on
every building descriptor. With it, each depot carries its measured target directly and the
`level` field can return to being a size rather than a price quotient.

**10. The remaining tram capital question: is the paving in the way object?** The pakset has no
separate road object under a tram track, so the way object carries the setts and paving as well as
the rails. If a future pakset or engine change separates the two, the way capital and the
maintenance rate both need re-deriving: the paving is the larger part of the capital and of the
renewal.

## 8. Defects found in passing

- **Pass 73's measured-bind rejection did not take effect.** `wb_fv_pass73.py` used
  `ws.cell(r, c, None)`, which openpyxl treats as "give me the cell", not "clear it". The two
  paved-runway binds (GBP69 per square metre read as GBP per kilometre) survived in the workbook
  while the audit recorded them as rejected. Cleared in pass 74. `[CODE New ex-15 @ 81ffb5911]`
- **The depot price cannot carry an object price.** Recorded above and in
  [engine-bugs](../engine-bugs.md) as a limitation with a proposed fix.
- **The `level` field is used for three unrelated purposes**: price multiplier, default
  maintenance multiplier and building removal cost. Any change to a depot's level changes all
  three. This is why the proposal must be applied as one operation.

## 9. Required depot levels under the proposal

The level that reproduces each target at the proposed per-unit rate. This is a proposed size
derived from the target, not a measurement; see section 4.2.

| Object | Target GBP | Rate | Level now | Required level |
|---|---:|---:|---:|---:|
| OldTrainDepot | 3,000 | 750 | 12 | 4 |
| OldTrainDepotElectric | 4,382 | 750 | 6 | 6 |
| OldTrainDepotDiesel | 4,382 | 750 | 10 | 6 |
| OldTrainDepotHorse | 2,083 | 750 | 1 | 3 |
| OldTrainDepotNarrow | 3,000 | 750 | 8 | 4 |
| OldTrainDepotNarrowHorse | 2,083 | 750 | 1 | 3 |
| ModernTrainDepot | 4,382 | 750 | 8 | 6 |
| ModernTrainDepotElectric | 4,382 | 750 | 4 | 6 |
| ModernTrainDepotNarrow | 4,382 | 750 | 10 | 6 |
| MaglevDepot | 4,382 | 750 | 5 | 6 |
| OldTramDepot | 9,560 | 750 | 5 | 13 |
| OldTramDepotSteam | 9,560 | 750 | 8 | 13 |
| OldTramDepotHorse | 9,560 | 750 | 1 | 13 |
| ModernTramDepot | 9,560 | 750 | 6 | 13 |
| CoachStable | 5,600 | 187 | 1 | 30 |
| OldRoadDepot | 5,600 | 187 | 9 | 30 |
| OldRoadDepot2 | 5,600 | 187 | 9 | 30 |
| OldRoadDepotElectric | 5,600 | 187 | 6 | 30 |
| OldRoadDepotSteam | 3,000 | 187 | 10 | 16 |
| ModernRoadDepot | 5,600 | 187 | 12 | 30 |
| ModernRoadDepotElectric | 5,600 | 187 | 6 | 30 |
| ModernRoadDepotMixed | 5,600 | 187 | 16 | 30 |
| OldBoatyard | 1,304 | 1,304 | 1 | 1 |
| OldBoatyardSteam | 1,304 | 1,304 | 2 | 1 |
| ModernBoatyard | 1,304 | 1,304 | 3 | 1 |
| AirHangarOld | 13,812 | 18,745 | 6 | 1 |
| AirHangarModern | 25,440 | 18,745 | 6 | 1 |

## 10. Sources

**Measured accounts and returns**: Ministry of Transport, *Tramways and Light Railways (Street and
Road) and Trackless Trolley Undertakings: Annual Return for 1930-31*, summary table Parts I-III
(permanent way and electrical equipment heads, capital account, car-miles), fetched from
`https://www.ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf`; Ministry of Transport returns 1925-26 and
1930-31 as recorded in [vehicle-cost/tram-maintenance](../vehicle-cost/tram-maintenance.md);
Midland Railway locomotive department accounts via Dodgson (2008) and the British Transport
Commission 1949 accounts via *Commercial Motor*, 22 September 1950, both as recorded in
[research report 16](research-pricing-report-16.md); Glasgow Larkfield and Lincoln bus garage
costs from the same report; the 1851-1910 depot and shed prices in
[prices-forum-fragments](../prices-forum-fragments.md).

**Published rates and standards**: Seeley, *Building Maintenance* (1976); Building Maintenance
Information, *Review of Maintenance Costs 2003 and 2004*; Cudworth, ICE Minutes vol. 85 (1886);
Garcke, "Tramway", *Encyclopaedia Britannica*, 11th edition (1911); Minnis and Hickman, *The
Railway Goods Shed and Warehouse in England* (Historic England, 2016).

**Pakset and engine files**: `New/ways/tram_track.dat`, `New/ways/maglev_tracks.dat`,
`New/depots/*.dat`, `New/stations/extensions.dat`,
`New/config/simuconf.tab`; `simtool.cc`, `simhalt.cc`, `obj/gebaeude.cc`,
`descriptor/reader/building_reader.cc`, `simworld.cc` and `dataobj/settings.cc` in
`simutrans-extended-sources`.

**Maglev guideway (research subagent, 2026-11-27)**: Hamburg-Berlin maglev study (1993); Munich
Transrapid planning estimate (2007), itemised; Shanghai Transrapid residual derivation (2004);
Changsha S1 published unit rates (2022); Linimo public-infrastructure split (2005); DLR City
Airport viaduct outturn (2005); Incheon Airport Maglev (2012); Changsha Maglev Express (2016);
Beijing S1 (2015); Chuo Shinkansen revised total, JR Central, 29 October 2025,
`https://company.jr-central.co.jp/chuoshinkansen/_pdf/total-pj-cost_02.pdf`; Eurostat
`lc_lci_lev` construction labour cost levels; National Bureau of Statistics of China, *2024年城镇
单位就业人员年平均工资情况*, 16 May 2025,
`https://www.stats.gov.cn/sj/zxfb/202505/t20250516_1959826.html`; Turner & Townsend,
*International Construction Market Survey 2024*; Welsh Government A487 New Dyfi Bridge carbon
report (2017); Maine Department of Transportation contractor survey (2022); Volpe 1992 guideway
maintenance model and Hyre & Eck (1994) via the Wayback Machine copy of
`onlinepubs.trb.org/Onlinepubs/trr/1994/1470/1470-004.pdf`; Morgantown PRT measured maintenance
1987-1992.

**Read but not used as evidence**: the Historic England goods-shed study's cost statements (the
accessible copies give types and dimensions but no construction prices); the GWR Moor Street goods
depot budget of GBP8,800 in 1910 (size unstated, so no per-square-metre rate). Both are recorded
as routes in section 7.
