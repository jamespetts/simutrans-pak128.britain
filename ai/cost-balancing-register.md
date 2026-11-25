---
status: draft
verified: New ex-15 @ fcd40c0bc + passes 62-65 (working tree), 2026-11-25
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
| Rail locomotives | no | yes | yes (13 classes, 1831-1960) | partial | Price per ton of engine weight (£32-78/ton steam era; diesels above) and £/1,000 dbhp (1951 Hansard); enough to interpolate steam-era items with a known weight, not diesels or pre-1850. Maintenance uses the 215 / 306 / 800 / 2,100 / 1,045 / 520 GBP ladder at 1900-2020; pass 63 applies the measured Class 92 override of 868 at 2018 (mixed traffic on the Caledonian Sleeper), pass 64 withdraws the 0.5 electric factor for the Class 88 (614.82, the Class 68 level), pass 66 puts Classes 89, 90 and 91 on the measured electric-locomotive track (1,476 / 1,103 / 1,045 / 868 at 1950 / 1977 / 1995 / 2018), and the 2020 rung of 520 remains the Class 66 freight-diesel line ([research-pricing-report-46](cost-balancing/research-pricing-report-46.md); [research-pricing-report-50](cost-balancing/research-pricing-report-50.md)). Pass 69 puts the per-km charge and the overhaul interval on the class and era distance table, keeping the measured class duties of Classes 37, 47, 55, 86 and 87. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Locomotives", "Price per ton" |
| Rail carriages | no | yes | yes (9 builds, 1846-1980s; 1955 Plan average and 1971 Hansard coach) | yes outside 1934-1980; across the gap partial, anchored at 1955 and 1971 | Era-band ladders by vehicle type (bogie third £1,200-1,500 etc.) and the NER build records 1905-34 as matched-model pairs. The 1934-1980 gap is a priority gap (wartime, nationalisation and Mark 1/2/3 across two inflation surges): [cost-data-coverage](cost-data-coverage.md) "Rail carriages". Maintenance uses the measured era ladder 33 / 39 / 121 / 265 / 460 / 440 GBP a vehicle-year at 1900 / 1920 / 1950 / 1970 / 1990 / 2020, re-based by pass 62 on [report 51](cost-balancing/research-pricing-report-51.md); the 1948 and 1966 points are 112 and 226 by interpolation ([research-pricing-report-43](cost-balancing/research-pricing-report-43.md)). [vehicle-cost-evidence](vehicle-cost-evidence.md) "Carriages" |
| Rail wagons | no | yes | yes (11 Shildon 1906 builds by capacity; 1971 Hansard coal wagon) | yes | Price per ton of capacity £6.37-8.40 (mean £7.2); proportional with a modest fixed element. Maintenance uses the measured era ladder 4.2 / 8.7 / 14.3 / 24.8 / 23.8 GBP per 10-tonne wagon-year at 1900 / 1950 / 1970 / 1990 / 2020, scaled by (payload/10)^0.4, replacing the 8-per-cent-of-capital rule ([research-pricing-report-43](cost-balancing/research-pricing-report-43.md)). The 1961 wagon level is £54.3 nominal (£9.84 in 1900 money), and the standard-gauge rows split head = 0.8A and overhaul event = 1.2A every six years at the 40,000 km/yr reference duty, so the head plus the annualised event equals the measured total ([wagon-overhaul-source-analysis](cost-balancing/wagon-overhaul-source-analysis.md)). [vehicle-cost-evidence](vehicle-cost-evidence.md) "Wagons" |
| Multiple units | no | yes (maintenance ladder 1900-2026) | no purchase prices | partial (maintenance only; no capital ladder) | Research pass 45 gives a ladder of 66 / 241 / 380 / 510 / 780 GBP a car-year at 1900 / 1950 / 1970 / 1990 / 2020, an overhaul provision of 15 per cent of A with a 1.2A event every eight years, and 50/50 fixed/per-km at a 100,000-mile reference duty; the 1900-1950 span rests on an estimate because no pre-1948 per-car measurement was found. Applied to 707 cars; `is_multiple_unit()` catches the fleet and the distance table sets the 100,000 / 120,000 / 161,000 km reference duties. [research-pricing-report-45](cost-balancing/research-pricing-report-45.md); [vehicle-cost/mean-annual-distance](vehicle-cost/mean-annual-distance.md) |
| Road vehicles (buses, coaches, lorries) | no | yes | partial (Routemaster, Atlantean, Guy Arab, Bedford OWB, Scammell Crusader) | yes | Complete-vehicle ladders: bus GBP 1,240 at 50 seats, seats^0.67; lorry GBP 162 at 1 ton in 1950, payload^0.30 below 7 tons and 0.75 above, with a 1.8 per cent a year real fall to 1960; steam wagons on their own ladder; battery-electric bus at twice the diesel. Chassis-only and body-only prices are excluded because a body is 42-45 per cent of a complete bus. The real level rises 40 per cent from 1990 to 2026 on measured tender awards. Maintenance from a measured per-km total, split 75/25 between running and standing charges (the standing share is an estimate). [vehicle-cost-evidence](vehicle-cost-evidence.md) "Buses, coaches and lorries" |
| Trams and light rail | no | yes (modern vehicle prices solid 2007-19; historic cars 1901-50) | partial (Metrolink M5000, Croydon CR4000, Edinburgh CAF, Blackpool Flexity 2) | yes | Historic ladder: £670 (1902 car), £904 (1929). Modern: £24,026 (1996) to £24,500 (2026) in 1900 money, from every UK order 2007-19 falling in a £1.80-2.72m band. Maintenance: pre-1950 gross car-only 84 / 131 / 106 / 89 GBP a car-year at 1900 / 1920 / 1931 / 1939 (35 per cent renewals inside); the 1950-90 rung is 150 repairs-only (band 130-210), with no renewals and a 28 per cent works-overhaul provision at three years; the modern value is 1,177 from 1990 (Nottingham 2011 contract), with no renewals and a 6 per cent provision at twelve years. The rebuild is an upgrade at 22-50 per cent of the new price ([research-pricing-report-47](cost-balancing/research-pricing-report-47.md); [research-pricing-report-49](cost-balancing/research-pricing-report-49.md)). The 1950-90 rung is an estimate. Articulated sections are priced zero on all but the leading section. [cost-balancing/research-pricing-report-35](cost-balancing/research-pricing-report-35.md) |
| Ships | no | yes (76 research rows 1845-1987; 14-vessel passenger fit R² 0.992) | yes (Frontenac 1816, SS Great Britain 1843, SS Great Eastern 1858; 14 measured passenger vessels in pass 25) | yes (per passenger by type, per tonne of cargo) | Passenger ferries £10-66 per passenger by type; cargo £8.5/t. Research report 56 shows the three per-gross-ton rates are the capital prices themselves, not annual repair: 84.1 x GT^0.90 is the report 25 purchase fit deflated to 1900 money, GBP 17/GT is Cambria's 1906 price and GBP 35/GT is the BR 1950-53 cargo price. The GT fit is therefore a price check, not only a shape check, and the per-capacity ladder's own rates are an unstated conversion of it at an assumed gross tonnage per capacity unit. The workbook keeps the capacity ladder and charges repair at 2 per cent of capital, inside report 56's 2-5 per cent band; adopting the per-GT capital ladder is an open decision. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Inland boats | no | yes (motor, steam, horse and sail per-ton prices 1909-37) | partial (individual craft) | yes (per tonne by engine type) | £8/t horse, £11/t sail, £14/t motor, £32/t steam. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Aircraft | no | yes (116 measured purchase prices 1936-2015); partial (maintenance per flying hour) | yes (hedonic fit, R² 0.948) | yes (seats, engines, engine type, wide body, year) | Pressurisation and swept wing are not identifiable and not applied. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Ships and aircraft" |
| Horses and horse vehicles | no | yes (annual keep £28-60) | partial (two accounts: LGOC 1893, London coal wharf 1830) | yes | Keep is well bracketed; purchase prices in `Horses cost table.ods` only. [base-maintenance](vehicle-cost/base-maintenance.md) "Later anchors" |
| Narrow-gauge vehicles | no | no | no | no | Nothing measured; forge basis is terrain not gauge. The 34 narrow-gauge carriage rows take the standard-gauge carriage ladder because no source distinguishes gauge in carriage maintenance, re-based on report 51 by pass 67; the 14 wagon rows keep the wagon ladder. [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Monorail vehicles | no | no | no | no | "No British historical basis". [infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5 |
| Maglev vehicles | no | no (no British maglev exists) | yes (Shanghai imported-car acquisition at 1,088 GBP a seat; maintenance EUR 0.011 a seat-km at 2009 prices, 0.00010257 GBP) | yes (seats, or car length for non-passenger stock) | The overseas-system rule and the conversion: [vehicle-cost/maglev-costs](vehicle-cost/maglev-costs.md); [research-pricing-report-55](cost-balancing/research-pricing-report-55.md). No mainline maglev in Britain, so British evidence cannot exist. |
| Vehicle overhauls and upgrades | no | yes (rail, road, tram, ship and aircraft) | partial (steam locomotives, carriages, buses, trams) | yes | Interval and cost share by class, in the `Overhauls & upgrades` sheet of the capital workbook (3,539 vehicles). Steam and diesel/electric: the intervals and provision shares are in the handoff table and [maintenance-decomposition](vehicle-cost/maintenance-decomposition.md) "Rail locomotives"; the measured annual total is the envelope, not a capital share (pass 49), and the Class 92 takes the measured 868 GBP override (pass 63). Carriage: the measured annual maintenance total is the envelope — the works overhaul is 28 / 24 / 19 / 12 / 10 / 8 per cent of A at 6 / 5 / 3 / 2 / 2 / 2.6-year intervals (210,000 / 180,000 / 165,000 / 176,000 / 240,000 / 294,000 km), the first event 0.70 of the maximum over three ([research-pricing-report-44](cost-balancing/research-pricing-report-44.md)); A is the report 51 series 33 / 39 / 121 / 265 / 460 / 440 at 1900 / 1920 / 1950 / 1970 / 1990 / 2020, applied by pass 62; the interval and the provision are the band values stated above. Multiple units: 15 per cent of A, event 1.2A every eight years at 100,000 / 120,000 / 161,000 km a car-year (research pass 45/53; [vehicle-cost/mean-annual-distance](vehicle-cost/mean-annual-distance.md)). Bus: 220,000 km, 25 and 40, rescaled to a 37.5 per cent annual share of the measured maintenance head where the capital-share profile exceeds it (the 1947 fleet composition; [vehicle-cost/source-composition](vehicle-cost/source-composition.md)). Lorry: bands by introduction year - before 1930 35-50 per cent, 1930-59 44-56, 1960-84 25-35, 1985-2004 20-30 - with the interval corrected to 80,000 / 80,000 / 160,000 / 400,000 km (the 1938-55 costings give 46, 53 and 44 per cent; [research-pricing-report-42](cost-balancing/research-pricing-report-42.md)). Tram: pre-1950 28 per cent of gross A at two years, event 0.35A rising to 0.75A, 35 per cent renewals; 1950-90 28 per cent of the repairs-only 150 rung at three years, event 0.54A rising to 1.15A, no renewals; modern 6 per cent at twelve years, one event of 0.75A, no renewals (96,000 / 144,000 / 1,080,000 km). Ship 2 and 5; aircraft 2.5 and 5. Wagon: head = 0.8A and overhaul event = 1.2A every six years at the 40,000 km/yr reference duty (240,000 km), where A is the measured wagon ladder; the 0.20 share and six years are an estimate, reconciled in [wagon-overhaul-source-analysis](cost-balancing/wagon-overhaul-source-analysis.md). Upgrade: 30-35 per cent of the new price for rail, 22-50 per cent for trams by introduction year (research pass 47), 50 per cent for the remaining classes. [vehicle-cost-evidence](vehicle-cost-evidence.md) "Overhauls and upgrades" |

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
| Piers, docks, quays | no | yes (per metre by construction) | partial (Margate 1853; Tilbury works) | yes | Per-metre ladder by construction type; maintenance heuristic 0.8-4% a year. The 111 bridge-substructure pier rows are charged by pass 68 at 19 per cent of the matching bridge family's measured rate (the midpoint of the measured 13-25 per cent low-bridge band), capital only: the measured share is a structure share, not a maintenance one, and no substructure maintenance rate is measured. [infrastructure-cost-evidence](infrastructure-cost-evidence.md) §5 |
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
