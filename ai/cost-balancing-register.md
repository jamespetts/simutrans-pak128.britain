---
status: draft
verified: New ex-15 working tree @ 184d0d1d3, 2026-11-24
---
# Cost-balancing register

**Covers**: the coverage status of the cost-balancing project for every class of costed item in the
pakset, and for each class whether (a) cost balancing is complete, (b) class-level historical data
exists, (c) individual-item historical data exists, and (d) whether class data is sufficient to
extrapolate or interpolate items that have none. The per-item rows (every vehicle, way, building and
setting) live in the working spreadsheets `New/cost-balancing-capital.xlsx` and
`New/cost-balancing-maintenance.xlsx`; this doc registers class-level status only. What the data
*is*: [vehicle-cost-evidence](vehicle-cost-evidence.md),
[infrastructure-cost-evidence](infrastructure-cost-evidence.md) and the docs they key.
Data-quality assessment per class: [cost-data-coverage](cost-data-coverage.md).

## How to read

- **Balanced** — the item's or class's costs have been set from historical data and checked in the
  synthesis. At the register's creation nothing has been completed: the `.dat` cost values are
  pre-calibration and are to be replaced, not adjusted
  ([vehicle-cost-model](vehicle-cost-model.md#purpose)).
- **Class data** — measured historical figures for the class (average prices, per-ton or per-metre
  rates, account totals), usable to derive a level for an item with no price of its own.
- **Item data** — a measured historical price or maintenance figure for a named item corresponding
  to a pakset object.
- **Extrapolate** — whether class data can produce a defensible individual figure (yes / partial /
  no), and on what basis.
- Evidence pointers name the doc and section holding the figures; the spreadsheets carry the same
  references row by row.

**The costing pass.** The spreadsheets are the research store; the `.dat` files hold the
pre-calibration values. Copying the spreadsheet values into the `.dat` files is the costing pass:
one operation, run only when the research is complete and the spreadsheets hold the final figures.
Corrections found before then accumulate in the spreadsheets and are not applied piecemeal.
`[USER-DIRECTION:2026-11-24]`

## Continuous brakes

The `Continuous brakes` sheet in each workbook records the fitted and unfitted carriage pairs and
the price and maintenance ratio each should carry. The measured premium is **+7.7 per cent**: an
automatic continuous brake cost about GBP 35 a carriage fitted (Msrs Peel and Makins, HC Deb
13 June 1879, vol 246 cc1840-1842), against carriage prices of GBP 397.86 to GBP 517.50 in the
1870s, and the extra maintenance was about 7.1 per cent a year of the brake capital, against
carriage maintenance of GBP 18.3 to GBP 45.3 a vehicle a year (Hill 1895, Appendix II Table II).

The current `.dat` values do not carry that premium. Cost ratios run from 54.2 to 191.9 per cent,
with six of the thirty fitted vehicles cheaper than the vehicle they upgrade, and maintenance
ratios from 8.9 to 1,818 per cent. In `New/trains/4wheel-1870s.dat` the eight fitted vehicles take
only four distinct prices, so a GBP 185,000 mail van and a GBP 655,000 TPO both become GBP 355,000
fitted. No `.dat` value has been changed; the correction is held in the workbooks for the costing
pass (defined above). `[CODE New ex-15 working tree, 2026-11-23]`

## Cost scope: what the cost fields do and do not hold

- **Vehicles.** `cost`, `runningcost`, `fixed_cost` and `upgrade_cost` cover the vehicle itself
  only: purchase, repair and servicing, and the standing cost of owning it. **Crew wages are not
  in them**: they come from `config/staff.tab` and are charged only for a vehicle that declares
  `staff[i]`. **Fuel and energy are not in them**: they are priced in `config/fuel.tab` and charged
  per unit consumed. The canonical statement is
  [vehicle-cost-model](vehicle-cost-model.md#what-these-costs-exclude).
- **Buildings and infrastructure.** The `maintenance` field (and a vehicle's `fixed_cost`) is the
  upkeep of the object's fabric only. **Station and depot staff, and administrative overhead, are
  or will be simulated separately and are not in it**; the proposed headquarters standing charge is
  the proxy for general administration
  ([infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §9). `[USER-DIRECTION:2026-11-21]`
- The cost-balancing workbooks keep these separate: no staff or fuel figure appears in any fixed
  or per-kilometre column.

## Vehicle classes

| Class | Balanced | Class data | Item data | Extrapolate | Basis and pointer |
|---|---|---|---|---|---|
| Rail locomotives | no | yes | yes (13 classes, 1831-1960) | partial | Price per ton of engine weight (£32-78/ton steam era; diesels above) and £/1,000 dbhp (1951 Hansard); enough to interpolate steam-era items with a known weight, not diesels or pre-1850. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Locomotives", "Price per ton" |
| Rail carriages | no | yes | yes (9 builds, 1846-1980s; 1955 Plan average and 1971 Hansard coach added 2026-11-24) | yes outside 1934-1980; across the gap partial, anchored at 1955 and 1971 | Era-band ladders by vehicle type (bogie third £1,200-1,500 etc.) and the NER build records 1905-34 as matched-model pairs. The 1934-1980 gap is a priority gap (wartime, nationalisation and Mark 1/2/3 across two inflation surges): [cost-data-coverage](cost-data-coverage.md) "Rail carriages". [vehicle-cost-evidence](vehicle-cost-evidence.md) "Carriages" |
| Rail wagons | no | yes | yes (11 Shildon 1906 builds by capacity; 1971 Hansard coal wagon) | yes | Price per ton of capacity £6.37-8.40 (mean £7.2); proportional with a modest fixed element. Maintenance now measured: £4 4s. per wagon-year 1887-92 (Hill 1895 Table III, 19 companies, repairs + renewals) and a 1929 private-owner repair contract at £5; no wagon overhaul price in any era. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Wagons" |
| Multiple units | no | partial (modern maintenance only) | no purchase prices | no | Modern per-vehicle-mile maintenance (2013 prices); no purchase ladder. [base-maintenance](vehicle-cost/base-maintenance.md) "Later anchors" |
| Road vehicles (buses, coaches, lorries) | no | yes | partial (Routemaster, Atlantean, Guy Arab, Bedford OWB, Scammell Crusader) | yes | Complete-vehicle ladders: bus GBP 1,240 at 50 seats, seats^0.67; lorry GBP 162 at 1 ton in 1950, payload^0.30 below 7 tons and 0.75 above, with a 1.8 per cent a year real fall to 1960; steam wagons on their own ladder; battery-electric bus at twice the diesel. Chassis-only and body-only prices are excluded because a body is 42-45 per cent of a complete bus. The real level rises 40 per cent from 1990 to 2026 on measured tender awards. Maintenance from a measured per-km total, split 75/25 between running and standing charges (the standing share is an estimate). [vehicle-cost-evidence](vehicle-cost-evidence.md) "Buses, coaches and lorries" |
| Trams and light rail | no | yes (modern vehicle prices solid 2007-19; historic cars 1901-50) | partial (Metrolink M5000, Croydon CR4000, Edinburgh CAF, Blackpool Flexity 2) | yes | Historic ladder: £670 (1902 car), £904 (1929). Modern: £24,026 (1996) to £24,500 (2026) in 1900 money, from every UK order 2007-19 falling in a £1.80-2.72m band. Maintenance: historic £64 a car-year (MoT 1913-14, car only), modern £1,301 a tram-year (Nottingham 2011 contract). Articulated sections are priced zero on all but the leading section. [cost-balancing/research-pricing-report-35](cost-balancing/research-pricing-report-35.md) |
| Ships | no | yes (76 research rows 1845-1987; 14-vessel passenger fit R² 0.992) | yes (Frontenac 1816, SS Great Britain 1843, SS Great Eastern 1858; 14 measured passenger vessels in pass 25) | yes (per passenger by type, per tonne of cargo) | Passenger ferries £10-66 per passenger by type; cargo £8.5/t; the GT fit is the shape check. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Inland boats | no | yes (motor, steam, horse and sail per-ton prices 1909-37) | partial (individual craft) | yes (per tonne by engine type) | £8/t horse, £11/t sail, £14/t motor, £32/t steam. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Aircraft | no | yes (116 measured purchase prices 1936-2015); partial (maintenance per flying hour) | yes (hedonic fit, R² 0.948) | yes (seats, engines, engine type, wide body, year) | Pressurisation and swept wing are not identifiable and not applied. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Horses and horse vehicles | no | yes (annual keep £28-60) | partial (two accounts: LGOC 1893, London coal wharf 1830) | yes | Keep is well bracketed; purchase prices in `Horses cost table.ods` only. [base-maintenance](vehicle-cost/base-maintenance.md) "Later anchors" |
| Narrow-gauge vehicles | no | no | no | no | Nothing measured; forge basis is terrain not gauge. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 || Monorail vehicles | no | no | no | no | "No British historical basis". [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Maglev vehicles | no | no | no | no | Entirely unmeasured. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Vehicle overhauls and upgrades | no | yes (rail, road, tram, ship and aircraft) | partial (steam locomotives, carriages, buses, trams) | yes | Interval and cost share by class, in the `Overhauls & upgrades` sheet of the capital workbook (3,444 rows). Steam: 200,000 km, 5 per cent first and 15 per cent late. Diesel/electric: 300,000 km, 7 and 20. Carriage: 250,000 km, 8 and 27. Bus: 220,000 km, 25 and 40. Lorry: 160,000 km, 10 and 30. Tram: 600,000 km, 8 and 45. Ship 2 and 5; aircraft 2.5 and 5. Upgrade: 30-35 per cent of the new price for rail, 50 per cent otherwise. Nine vehicles had any overhaul data before this work. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Overhauls and upgrades" |

## Way and structure classes

| Class | Balanced | Class data | Item data | Extrapolate | Basis and pointer |
|---|---|---|---|---|---|
| Rail ways (track) | no | yes | yes (L&M 1830 account; Leicester/Leeds/Dewsbury 1877-82; Mills c.1898) | yes | Permanent way £1,300-1,900/km flat 1830-1900; rail weight ladder; whole-line capital £20,300-22,400/km 1858-1902. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §1-2 |
| Road ways | no | yes | partial (2011 motorway yard rates) | yes | Turnpike to motorway: construction and upkeep figures 1819-2021; the motorway object is the decisive 2.5x-too-cheap check. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §3 |
| Canal ways | no | yes | yes (7 named canals 1724-1905; itemised Leeds & Liverpool estimate) | yes | £1,850-5,560/km narrow and barge, £14,750-33,000/km ship; canals are deliberately zero-forge and unrenewed — for a canal the forging is the building, so the formation is folded into the per-class way cost and `forge_cost_water` goes to 0 at the costing pass (decision 2026-11-24, conflict 7 resolved). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §5 |
| Tram ways | no | partial (track £600/mile 1911; forge £600-1,200/km) | no | partial | Street reservation basis. [prices-forum-fragments](prices-forum-fragments.md) "Rails and permanent way" |
| Narrow-gauge ways | no | partial (forge £250-620/km) | no | partial | Terrain-dominated forge basis only. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Monorail / maglev ways | no | no | no | no | Forge recommendation without historical basis. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Bridges and viaducts | no | yes | yes (25 named viaducts 1828-1978) | partial | £/m ladders by material and span class; height and span are deliberately not costed in the data. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §4 |
| Tunnels | no | yes | yes (21 named tunnels 1779-1962) | partial | £/m by ground and method; two table artefacts recorded. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §4 |
| Piers, docks, quays | no | yes (per metre by construction) | partial (Margate 1853; Tilbury works) | yes | Per-metre ladder by construction type; maintenance heuristic 0.8-4% a year. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §5 |
| Signals and signalboxes | no | yes (1912 post prices; mechanical vs colour light) | partial (Spetisbury 1901; Kent Coast; Tilbury 1929; Reading 1963) | partial | One signal object is one signal in reality (post with its arms or lamps); the general signalling infrastructure is represented by the signalbox cost (settled 2026-11-24). The 168 signal objects are calibrated to the per-post ladder at the costing pass. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §7 |
| Roadsigns | no | no | no | no | No historical cost data anywhere. |
| Way objects (electrification) | no | yes | partial (Southern 1925; BR 1955 pair; Romford 1986) | yes | £/track-km ladders 1925-2016; pakset era order reversed (750 V DC cheaper than AC). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §8 |
| Crossings (level) | no | no | no | no | Field semantics only ([objects/crossing](objects/crossing.md)); no cost data. |
| Stations, platforms, shelters, bus stops | no | yes (platform £/m of face; canopies; shelters) | yes (25 forum station rows 1851-1984) | yes | Per-metre and per-item ladders by construction; station maintenance conflict unresolved (conflict 2). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §6 |
| Depots | no | partial (8 named sheds 1851-1969) | partial | partial | No cost line in current settings; suggested 1,000,000 rail / 500,000 road. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §3.5 |
| Airports (runways, terminals, hangars, towers) | no | yes (per m2 ladders; control towers £2.3m-£50m) | partial (Stansted 1991; Luton; Heathrow) | yes | Deflate modern £/m2 on the `buildings` index for pre-1950. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §9 |
| Power lines | no | yes (132/275 kV 1959; 400 kV 1965, 2012) | partial (the line rates) | yes | 132 kV £10,000/mile and 275 kV £25,000/mile 1959; 400 kV £65,800/mile 1965 and £1.6m/km 2012; maintenance £650/km-year. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §9 |
| Grid substations (engine `cost_transformer`) | no | partial (1933 and 1953 inferred; modern measured) | partial | yes | Modelling choice, 2026-11-24: the game object is a 132 kV grid supply point at each power station and town. £27m for 273 stations in 1933 leaves about £40,000 each, £25,000 at 1900. `cost_transformer` 2,500 → 6,308,177; `cost_maintain_transformer` 100 → 2,628. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §9 |

## Buildings, land and engine-charged actions

| Class | Balanced | Class data | Item data | Extrapolate | Basis and pointer |
|---|---|---|---|---|---|
| Headquarters | no | yes (overhead 3.3-5.8% of receipts = £175/route-km/year) | no (building cost never established) | partial | Standing charge defensible; building cost rests on near anchors only (Derby 1839; training college 1937). [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §9 |
| Industry buildings | no | no | no | no | Whole class unmeasured; `buildings` index gives movement but no base level. |
| City buildings | no | no | no | no | Whole class unmeasured; forum holds no pre-1845 building prices. |
| Land purchase (city and country) | no | yes (Savills farmland; JST house price proxy) | n/a | n/a | 1900 anchors provisional against `meters_per_tile` scaling ([prices-config](prices-config.md)). |
| Land alteration (raise/lower, cuttings, embankments) | no | yes (formation £110-400/km; earthworks 9d-1s 3d a cubic yard; derived cutting-depth table) | partial (L&M 1830; Tring; Grand Junction contracts) | partial | The derived table rests on assumed slopes; "per km for a stated cross-section" not established. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §2 |
| Tree removal | no | no | no | no | Engine key coverage only. |
| Building and field removal | no | no | no | no | Engine key coverage only. |
| Trees (planting) | no | no | no | no | No cost data of any kind. |
| Groundobj, fences, ground | no | no | no | no | No costed groundobj present. |
| Forge costs (`forge_cost_*`) | no | yes (per-km formation ladders per way class) | no | yes | Rail 15,000 -> 76,000-101,000 recommended; tram, narrow, water, air bases each derived. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Engine finance settings (`cost_depot_*`, `cst_*`) | no | partial (per action, from structure ladders) | no | partial | Unscaled by length; receive only inflation adjustment. [infrastructure-base-costs](infrastructure-base-costs.md) |

## Config-driven costs (not object costs, for completeness)

| Class | Balanced | Class data | Item data | Extrapolate | Pointer |
|---|---|---|---|---|---|
| Fuel (`config/fuel.tab`) | no | yes (coal, oil, electricity, jet series) | n/a | n/a | [fuel-evidence](fuel-evidence.md); open M3 (steam unit question). |
| Crew wages (`config/staff.tab`) | no | yes (1907 grades; 1914-61 Hansard; 1946; 1956-68 Table 50; NES 1980; ASHE 1999-2026; sea grades 1912-1960 NMB and ASHE; air grades 1924-1969 and ASHE) | n/a | n/a | [staff-wages](staff-wages.md), [staff-wages/reconstruction](staff-wages/reconstruction.md) and [staff-wages/post-1980](staff-wages/post-1980.md); review workbook `New/staff-wages.xlsx`; gaps 1926-68 by grade, 1981-98, sea 1938-66/1981-89 and air 1909-23/1925-53/1955-68/1970-98. |
| Revenue rates (fares, mail, goods) | no | yes (statutory schedules; charged-rate series) | n/a | n/a | [goods-rate-evidence](goods-rate-evidence.md); [class](class.md). |

## Cross-cutting status

- Conversion and normalisation method: established and recorded
  ([prices-config](prices-config.md#unit-conversion),
  [infrastructure-base-costs](infrastructure-base-costs.md#the-conversion-chain)); open items M1
  (maintenance display confirmation), M2 (rate for per-month charges) and the workbook x8 trap are
  listed in [balance-synthesis](balance-synthesis.md).
- Class data sufficient to extrapolate, in summary: rail carriages, rail wagons, road vehicles,
  rail ways, road ways, canal ways, piers, stations, airports, electrification, power lines,
  grid substations, horses, forge costs. Partial: locomotives (steam with known weight only),
  trams, bridges, tunnels, signals, depots, land alteration. No: multiple units, ships, aircraft,
  inland boats, narrow-gauge/monorail/maglev vehicles and ways, roadsigns, crossings, industry and
  city buildings, trees, ground objects.

## Open questions

- Does the register need a per-item tier below the spreadsheets for items where no spreadsheet row
  can hold the derivation (for example the locomotive per-ton method needs each engine's weight)?
- Should the revenue-side classes (fares, goods rates) remain in this register or move to
  [balancing](balancing.md) once the cost work is under way?
