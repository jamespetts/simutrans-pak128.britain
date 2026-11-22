---
status: draft
verified: none
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
| Rail carriages | no | yes | yes (9 builds, 1846-1980s) | yes | Era-band ladders by vehicle type (bogie third £1,200-1,500 etc.) and the NER build records 1905-34 as matched-model pairs. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Carriages" |
| Rail wagons | no | yes | yes (11 Shildon 1906 builds by capacity) | yes | Price per ton of capacity £6.37-8.40 (mean £7.2); proportional with a modest fixed element. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Wagons" |
| Multiple units | no | partial (modern maintenance only) | no purchase prices | no | Modern per-vehicle-mile maintenance (2013 prices); no purchase ladder. [base-maintenance](vehicle-cost/base-maintenance.md) "Later anchors" |
| Road vehicles (buses, coaches, lorries) | no | yes | partial (2010s bus prices; Commercial Motor tables 1923-1980) | yes | Chassis/vehicle prices by seating and tonnage; maintenance ladders 1928-2016. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Buses, coaches and lorries" |
| Trams and light rail | no | partial (maintenance; tramway track) | partial (system budgets) | partial | MoT statutory returns per car-mile 1913-30; Sheffield Supertram budgets modern. No car purchase ladder. [base-maintenance](vehicle-cost/base-maintenance.md) "Trams" |
| Ships | no | partial (5% of capital a year, mid-life) | yes (Frontenac 1816, SS Great Britain 1843, SS Great Eastern 1858) | no | Three purchase points spanning 42 years cannot carry a ladder; repair evidence is dry-docking and survey, not per-voyage. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Inland boats | no | partial (repair jobs only) | partial (individual repair jobs) | no | No carrying-trade boat figure exists. [vehicle-cost](vehicle-cost/inland-boat-maintenance.md) |
| Aircraft | no | partial (maintenance per flying hour) | no usable prices | no | Explicit: "Aircraft costs should not be calibrated from this evidence"; a procurement-price source is required. [vehicle-cost-evidence](vehicle-cost-evidence.md) "What it does not support" |
| Horses and horse vehicles | no | yes (annual keep £28-60) | partial (two accounts: LGOC 1893, London coal wharf 1830) | yes | Keep is well bracketed; purchase prices in `Horses cost table.ods` only. [base-maintenance](vehicle-cost/base-maintenance.md) "Later anchors" |
| Narrow-gauge vehicles | no | no | no | no | Nothing measured; forge basis is terrain not gauge. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Monorail vehicles | no | no | no | no | "No British historical basis". [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Maglev vehicles | no | no | no | no | Entirely unmeasured. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |

## Way and structure classes

| Class | Balanced | Class data | Item data | Extrapolate | Basis and pointer |
|---|---|---|---|---|---|
| Rail ways (track) | no | yes | yes (L&M 1830 account; Leicester/Leeds/Dewsbury 1877-82; Mills c.1898) | yes | Permanent way £1,300-1,900/km flat 1830-1900; rail weight ladder; whole-line capital £20,300-22,400/km 1858-1902. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §1-2 |
| Road ways | no | yes | partial (2011 motorway yard rates) | yes | Turnpike to motorway: construction and upkeep figures 1819-2021; the motorway object is the decisive 2.5x-too-cheap check. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §3 |
| Canal ways | no | yes | yes (7 named canals 1724-1905; itemised Leeds & Liverpool estimate) | yes | £1,850-5,560/km narrow and barge, £14,750-33,000/km ship; but the pakset's way object and forge meanings are reversed (conflict 7). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §5 |
| Tram ways | no | partial (track £600/mile 1911; forge £600-1,200/km) | no | partial | Street reservation basis. [prices-forum-fragments](prices-forum-fragments.md) "Rails and permanent way" |
| Narrow-gauge ways | no | partial (forge £250-620/km) | no | partial | Terrain-dominated forge basis only. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Monorail / maglev ways | no | no | no | no | Forge recommendation without historical basis. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Bridges and viaducts | no | yes | yes (25 named viaducts 1828-1978) | partial | £/m ladders by material and span class; height and span are deliberately not costed in the data. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §4 |
| Tunnels | no | yes | yes (21 named tunnels 1779-1962) | partial | £/m by ground and method; two table artefacts recorded. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §4 |
| Piers, docks, quays | no | yes (per metre by construction) | partial (Margate 1853; Tilbury works) | yes | Per-metre ladder by construction type; maintenance heuristic 0.8-4% a year. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §5 |
| Signals and signalboxes | no | yes (1912 post prices; mechanical vs colour light) | partial (Spetisbury 1901; Kent Coast; Tilbury 1929; Reading 1963) | partial | Decide what one signal object represents first (a block section, not an arm). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §7 |
| Roadsigns | no | no | no | no | No historical cost data anywhere. |
| Way objects (electrification) | no | yes | partial (Southern 1925; BR 1955 pair; Romford 1986) | yes | £/track-km ladders 1925-2016; pakset era order reversed (750 V DC cheaper than AC). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §8 |
| Crossings (level) | no | no | no | no | Field semantics only ([objects/crossing](objects/crossing.md)); no cost data. |
| Stations, platforms, shelters, bus stops | no | yes (platform £/m of face; canopies; shelters) | yes (25 forum station rows 1851-1984) | yes | Per-metre and per-item ladders by construction; station maintenance conflict unresolved (conflict 2). [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §6 |
| Depots | no | partial (8 named sheds 1851-1969) | partial | partial | No cost line in current settings; suggested 1,000,000 rail / 500,000 road. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §3.5 |
| Airports (runways, terminals, hangars, towers) | no | yes (per m2 ladders; control towers £2.3m-£50m) | partial (Stansted 1991; Luton; Heathrow) | yes | Deflate modern £/m2 on the `buildings` index for pre-1950. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §9 |
| Power lines | no | partial (1959, 2015 anchors) | partial (the two anchors) | partial | Two points only. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §9 |
| Transformers | no | no (as such) | no | no | Engine key coverage only ([prices-config](prices-config.md) "buildings"). |

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
| Crew wages (`config/staff.tab`) | no | yes (1907 grades; 1956-62; ASHE modern) | n/a | n/a | [staff-wages](staff-wages.md); gaps before 1901 and 1908-1955. |
| Revenue rates (fares, mail, goods) | no | yes (statutory schedules; charged-rate series) | n/a | n/a | [goods-rate-evidence](goods-rate-evidence.md); [class](class.md). |

## Cross-cutting status

- Conversion and normalisation method: established and recorded
  ([prices-config](prices-config.md#unit-conversion),
  [infrastructure-base-costs](infrastructure-base-costs.md#the-conversion-chain)); open items M1
  (maintenance display confirmation), M2 (rate for per-month charges) and the workbook x8 trap are
  listed in [balance-synthesis](balance-synthesis.md).
- Class data sufficient to extrapolate, in summary: rail carriages, rail wagons, road vehicles,
  rail ways, road ways, canal ways, piers, stations, airports, electrification, horses, forge
  costs. Partial: locomotives (steam with known weight only), trams, bridges, tunnels, signals,
  depots, land alteration, power lines. No: multiple units, ships, aircraft, inland boats,
  narrow-gauge/monorail/maglev vehicles and ways, roadsigns, crossings, transformers, industry and
  city buildings, trees, ground objects.

## Open questions

- Does the register need a per-item tier below the spreadsheets for items where no spreadsheet row
  can hold the derivation (for example the locomotive per-ton method needs each engine's weight)?
- Should the revenue-side classes (fares, goods rates) remain in this register or move to
  [balancing](balancing.md) once the cost work is under way?
