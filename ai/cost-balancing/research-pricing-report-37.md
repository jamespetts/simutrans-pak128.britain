# Overhaul, rebuild and upgrade costs for road vehicles, trams, ships and aircraft, 1850-2026

Research pass completed 23 November 2026. This is the companion to the rail-vehicle overhaul pass; no rail vehicle is covered here.

## 1. Scope

The pass looked for measured overhaul, rebuild and upgrade costs, and the interval at which they fell due, for:

- buses and coaches;
- lorries and vans;
- trams and light rail;
- ships;
- aircraft.

The purpose is to populate `max_distance_between_overhauls`, `initial_overhaul_cost`, `max_overhaul_cost`, `overhauls_before_max_cost`, `overhaul_month_tenths` and `upgrade_price` for the non-rail part of the pakset, where only nine of 3,539 vehicles currently carry any overhaul data and all nine are rail. The companion CSV, `ai/temp/overhaul-rows-road.csv`, has 92 rows.

## 2. Method and limits

Searches ran on Exa, one search per turn. Every page cited was fetched and read; search-result highlights were not treated as evidence. Commercial Motor article pages return HTTP 202 to a plain fetch and are behind a JavaScript challenge, so they were retrieved through the Exa contents endpoint, which returns the article text. The archive's own search was not used.

No Simutrans `.dat` cost, runningcost, fixed_cost, overhaul or upgrade value was read, and no pakset price enters any calculation. All money is nominal money of the year stated, in the unit printed. Nothing is inflation-adjusted. The only conversions are explicit kilometre equivalents in the recommendations, marked COMPUTED, because the engine field is in kilometres.

Confidence tags follow the pakset conventions:

- **MEASURED** — a contemporary account, an operator's own statement, a contract award or a company disclosure.
- **STATED** — an engineer's, historian's or trade-press figure that is not itself a transaction record.
- **COMPUTED** — my arithmetic on two stated figures, with the arithmetic shown.
- **ESTIMATE** — a judgement where no measured figure exists.

## 3. Headline results

- **Buses.** The pre-war London cycle was annual, because the police licence ran for twelve months. The London General Omnibus Company overhauled its whole 3,000-4,200 bus fleet every year at Chiswick, with the bus itself out of service for two days. After the war the cycle lengthened: 3.5 years at Aldenham's opening in 1956, four years by 1965, six years by the 1970s, and four to five years in the 1984 "Wasp" programme, before London Buses abandoned complete overhauls in October 1985. The 1965 cost was £2,000 a bus, excluding the units overhauled at Chiswick. Municipal Liverpool used a five-year complete overhaul tied to the Certificate of Fitness. Engine major overhauls in municipal fleets fell at 120,000-150,000 miles.
- **Lorries and vans.** The evidence is overwhelmingly mileage-based. A 1950 engineering estimate put a complete engine overhaul at 90,000 miles and £120-£140 for a reconditioned engine; a 1955 estimate put an engine overhaul at 50,000 miles and £60, and a chassis and body overhaul at 100,000 miles and £220. By 1959 AEC was exchanging fully rebuilt engines at £205-£285. By 1991-93 a Scania exchange engine was £10,534-£12,612. The light-van case is much shorter: 15,000 miles and about £20 for a replacement engine in 1956.
- **Trams.** The modern evidence is good and the historic evidence is poor. Metrolink gave its original 26 T68 trams a mid-life refurbishment at £80,000 each in 2004, at about twelve years and one million miles. Supertram is paying £21.4m plus VAT to extend the life of 25 1992-94-vintage trams to 2035, about £856,000 a tram. No measured historic municipal tramcar overhaul price was found.
- **Ships.** The classification cycle is the driver: special survey every four years in the nineteenth century, and a five-year cycle with intermediate surveys today, with drydocking every 2.5-5 years. A 2009 benchmark put bulk-carrier drydocking at US$1.1m-1.9m; 2020 Bulkers disclosed US$2.3m for two ships in the first quarter of 2025 and US$1.2m for one ship in May 2025. A routine five-year docking is about twelve days at the yard, five of them in dock.
- **Aircraft.** Checks are frequent and expensive but small relative to the aircraft: a C check every 18-24 months and about three weeks, a D check every six years and three to six weeks at several million dollars. The A320 base-check cycle is US$3.5m per 26,000 flight cycles. CFM56-5B shop visits are US$1.15m-1.5m at 8,000 engine flight cycles; CFM56-7B shop visits are US$2.6m-3.8m at 11,000-20,000 cycles.
- **Strongest upgrade figures.** The Supertram life extension at £21.4m for 25 trams is the largest measured per-unit tram upgrade in this pass. For buses the cleanest is East Lancashire Coachbuilders' 1991 Leyland National Greenway at about £45,000, stated to be half the price of a new vehicle, with a new Gardner engine, reconditioned gearbox and new body. The 2023 Equipmake battery-electric repower of ten Big Bus Tours open-toppers at £1.75m, £175,000 a bus, is the clearest modern road-vehicle upgrade.

## 4. Buses and coaches

### 4.1 London before the war: Chiswick

The London General Omnibus Company opened Chiswick in 1921. The overhaul cycle was set by the Metropolitan Police licence, which ran for twelve months; the licence could not be renewed until the bus had been completely overhauled. In 1922 the company had 3,000 buses in regular use, 245 full working days a year, and put 15 buses a day through the works, 75 a week. The whole fleet was therefore overhauled annually.

The work was a full dismantling, not a service. The body was lifted off the chassis. The chassis was stripped into engine, gearbox, steering, front axle, rear axle and frame on a moving platform; every part was cleaned in caustic soda and hot water, inspected against jigs and limit gauges, and marked green for use, blue for rectification or red for scrap. Engines were rebored or relined, crankshafts reground to standard undersizes, bearings re-metalled and line-bored, and each engine run in and dynamometer tested. Bodies were stripped, defective panels and pillars renewed, rewired, repainted and revarnished, and refitted with overhauled seats and fittings.

By 1926 the works had reduced the elapsed time for a body to about four working days: one hour stripping, eight hours on the repair line, two and a half days in the paint shop and three hours remounting. The chassis took two days. Because bodies and chassis were pooled and the licence was transferred to a completed bus, the bus itself was out of service for only two days a year, and no more than one per cent of the 4,000-bus fleet was ever off the road for complete overhaul. Output was 90 buses a week in 1926, with a peak of 120.

The only measured cost in the Chiswick accounts that I found is the paint and varnish: £14 a bus in 1926, including labour, materials and a proportion of overhead. That is the finishing stage only, not the whole overhaul.

### 4.2 London after the war: Aldenham

Aldenham opened as a bus overhaul works in 1956, taking over body and chassis work while Chiswick concentrated on engines, gearboxes, electrical units and axles. At opening, output was 56 buses a week, the interval was 3.5 years, and the fleet was about 8,500 vehicles. By January 1965 output was 32-35 buses a week, the interval was four years, and the fleet was about 8,060. Overhauls were set by time, not mileage. The 1965 article is explicit that the engine and gearbox units were not overhauled at Aldenham, or at the same time as the bus; they were exchanged for reconditioned units at the garage as required, while steering and axle units were removed at overhaul and exchanged from Chiswick. The chassis structure itself was washed, stripped, repaired and repainted at Aldenham.

The Aldenham process for an RT or Routemaster was:

- drain fuel and water, inspect the body, lift the body off the chassis in the high bay;
- send the body through the body shop, where it was inverted, pressure-cleaned underneath, stripped, repaired, repanelled and repainted;
- send the chassis through a washing tunnel, strip it, overhaul it and repaint it;
- remount the body on the first available overhauled chassis, not necessarily its own;
- refit seats, blinds and fittings, test-run the bus, and present it to the Ministry of Transport inspectors.

The body shop averaged 7-8 days for a full RT body overhaul and 6-7 days for a chassis (S46). The works float meant the operator's road fleet lost only the identity, not a vehicle: the bus entering the works handed its licence and fleet number to a bus leaving. The last overhaul of a bus's life was a "final overhaul", repaired with minimum structural replacement, using plonk-on plates rather than full panel repair (S46).

The cost in January 1965 was an average of £2,000 a bus once every four years, excluding the units overhauled at Chiswick. That figure is the one already known; it is confirmed here with its scope. It is not the cost of an engine or gearbox overhaul.

After 1965 the interval stretched. A London Transport Museum photograph description of 1970-1980 says full overhauls were by then carried out once every six years. In April 1984 London Transport was operating five- and four-year "Wasp" overhauls and planned to stop demounting Routemaster bodies. In October 1985 London Buses decided to stop sending buses for complete overhaul every four to five years and to do most of the work at garages; the maintenance business lost £29.5m of annual turnover on a total of £217m, and Aldenham closed in 1986.

The £29.5m is not a per-bus price, but it can be divided by the number of overhauls it bought. With a fleet of about 6,000 buses and a four-to-five-year cycle, that is 1,200-1,500 overhauls a year, or about £20,000-£25,000 an overhaul in 1985 (COMPUTED; low confidence because the fleet and cycle are assumptions). That is roughly ten times the 1965 figure in nominal terms, against a general price level several times higher over the same twenty years (ESTIMATE); part of the difference is real, part is the wider scope of the later overhaul.

### 4.3 Municipal and company fleets

The municipal evidence is about mileage, not time, and it shows a clear split between engine overhaul and body overhaul.

- **Liverpool** in 1961 did its five-year complete overhaul at Edge Lane for the Certificate of Fitness. Engines were changed only as needed, and some Leylands had passed 400,000 miles.
- **Midland Red** in 1952 ran A, B, C and D docks at 7,000, 49,000, 98,000 and 147,000 miles. The D dock was the major overhaul at Carlyle Road. The first D dock bored the block 0.030 in oversize; the second resleeved it. The fuel pump was reconditioned every 35,000 miles, the starter motor changed at 70,000 miles, and the exhausters and brake cylinders at the C dock.
- **Coventry** in 1952 stripped engines for major overhaul at 125,000 miles, raised from 100,000 since the war. The block was exchanged at 50,000 miles, pistons were replaced at 75,000 miles, and the crankshaft was ground to a standard undersize at 125,000 miles.
- **Wolverhampton** ran Gardner 5LW and 6LW engines to 120,000 miles without reboring or resleeving, with new rings every 40,000 miles.
- **Walsall** left the Gardner engines until 60,000 miles, then resleeved and fitted reconditioned pistons, and ran to a 150,000-mile major overhaul.
- **Burton-on-Trent** rebored at 50,000 miles, resleeved at 100,000 miles, and changed the unit at 200,000 miles.
- **Don Everall's coaches** were overhauled at 75,000-140,000 miles, the interval depending on the unit; the seasonal nature of coach work made reliability, not cost, the first consideration.
- **Ribble** in 1938 docked at about 10,000 miles for two whole days on the larger vehicles, and did complete overhauls at a fixed mileage, up to eight buses a week at Frenchwood.

For body work, London Transport in 1947 overhauled a bus body completely every two to three years at Chiswick, stripping the interior, removing panels, examining and repairing pillars, rebuilding floors, overhauling seats and route gear, and repainting and varnishing. Midland Red kept bodies for about two and a half years between complete overhauls, with a light overhaul and external repaint every fifteen months.

### Table 4.1 Buses and coaches

| Year | Vehicle or item | Interval | Cost | Scope | Downtime | Source | Conf. |
|---|---|---|---|---|---|---|---|
| 1922 | LGOC Chiswick, London | 12 months, annual police licence | — | 3,000 buses; 15 a day; 75 a week | — | S1 | MEASURED |
| 1926 | LGOC Chiswick, London | 12 months | Paint and varnish £14 | 4,000 buses; 90 a week, peak 120 | 2 days bus idle; body 4 working days | S2 | MEASURED |
| 1938 | Ribble Motor Services | Docking about 10,000 miles; complete overhaul at fixed mileage | — | 1,060 buses; 8 overhauls a week | 2 days for larger vehicles | S3 | MEASURED |
| 1947 | London Transport | Body overhaul every 2-3 years | — | Chiswick | — | S4 | MEASURED |
| 1947 | Midland Red | Complete body overhaul about 2.5 years; light overhaul and repaint every 15 months | — | Company fleet | — | S4 | STATED |
| 1952 | Midland Red | D dock 147,000 miles; A 7,000, B 49,000, C 98,000 | — | Carlyle Road works | — | S5 | MEASURED |
| 1952 | Coventry Corporation | Major overhaul 125,000 miles, was 100,000 | — | 291 buses | — | S6 | MEASURED |
| 1952 | Wolverhampton Corporation | Major overhaul 120,000 miles; rings every 40,000 | — | 126 buses | — | S6 | MEASURED |
| 1952 | Walsall Corporation | Major overhaul 150,000 miles; resleeve at 60,000 | — | 205 vehicles | — | S6 | MEASURED |
| 1952 | Burton-on-Trent | Unit change 200,000 miles; rebore 50,000; resleeve 100,000 | — | — | — | S6 | MEASURED |
| 1952 | Don Everall coaches | Major overhaul 75,000-140,000 miles | — | 50 coaches | — | S6 | MEASURED |
| 1956 | LT Aldenham | 3.5 years; 56 a week | — | 8,500 vehicles | — | S8 | MEASURED |
| 1961 | Liverpool Corporation | Complete overhaul 5 years, Certificate of Fitness | — | 1,232 buses; Edge Lane | — | S7 | MEASURED |
| 1965 | LT Aldenham | 4 years; 32-35 a week | £2,000 a bus | 8,060 vehicles; body and chassis only | Body 7-8 days; chassis 6-7 days | S8, S46 | MEASURED; STATED for works days |
| c.1975 | LT Aldenham | 6 years | — | — | — | S13 | STATED |
| 1984 | LT Aldenham | 4-5 years, "Wasp" | — | 90 per cent of LRT overhauls | — | S9 | MEASURED |
| 1985 | London Buses | Complete overhauls every 4-5 years discontinued | £29.5m annual turnover lost | — | — | S11 | MEASURED |
| 1972 | AEC 691 bus engine | — | £195 repair against £295 new | Bus company workshop | — | S22 | MEASURED |
| 1991 | ELC Leyland National Greenway | — | £45,000 a bus, about half new | New Gardner engine, reconditioned gearbox, new body | — | S12 | MEASURED |
| 1991 | ELC Atlantean conversion | — | £37,000 a bus | New single-deck body | — | S12 | MEASURED |
| 2023 | Equipmake Big Bus Tours repower | — | £1.75m for 10, £175,000 each COMPUTED | Battery-electric driveline | — | S43 | MEASURED |

## 5. Lorries and vans

The lorry evidence is a sequence of engineering cost estimates and exchange-engine prices. It is more consistent than the bus evidence because lorries were always maintained on mileage.

The 1949 fleet policy is the clearest statement of a complete cycle. Light cars and commercial vehicles under one ton were expected to last 60,000 miles, with a top overhaul at 15,000, a complete engine, chassis and body overhaul at 30,000, and another top overhaul at 45,000. Vehicles over one ton were expected to last 100,000 miles, with a top overhaul at 15,000, a complete overhaul at 30,000, a top overhaul plus chassis and body complete overhaul at 45,000, a complete engine overhaul at 60,000, and top overhauls at 75,000 and 90,000.

The 1950 Commercial Motor calculation is the fullest cost account. It assumed a 3-5 ton lorry, a top overhaul at 30,000 miles costing £7 at a garage or £5 10s in the operator's own workshop, and a complete engine overhaul at 90,000 miles by replacement with a reconditioned engine costing £120-£140. It also gave an example of an engine overhaul plus chassis repair at 48,000 miles for £80. The 1955 calculation, for a petrol-engined 6-tonner, put the engine overhaul or reconditioned unit at £60 after 50,000 miles, and the chassis and body major overhaul at 100,000 miles at £220 including a second reconditioned engine. It also priced a brake reline at £5 10s every 10,000 miles and decarbonising at £2 10s every 10,000 miles.

The component exchange prices are the best measured series:

- AEC, 1959: £205-£285 for a completely rebuilt exchange engine for current models, with new liners, pistons, rings, main and big-end bearings, reground crankshaft, new valves and a one-year guarantee. Throughput was 30-35 engines a week, capacity 50, or 100 with a night shift.
- Scania, 1991: £12,611.54 for an exchange V8 including water pump, compressor, flywheel and housing, manifolds, turbocharger, oil cooler and injection equipment. An independent reconditioner was 20 per cent cheaper; an in-frame overhaul with new bearings, pistons, liners, head work and injectors cost £3,210.88 in parts, plus 40 hours labour against 15 hours to fit an exchange engine. A reconditioned engine took seven days.
- 1993: service exchange engines for a 300 hp Euro-1 tractor unit were £10,534 for Scania, £5,382 for Renault, £15,274 for Mercedes-Benz including a £6,159 damaged-core surcharge, and £2,750 for a Cummins L300/L325 short engine.

Downtime is short for an exchange. A Bedford tipper engine change after 60,000 miles took about 6.5 hours in 1953; a back axle or gearbox took about 1.5 hours. A Reliant 5-cwt van engine replacement in 1956 took under 24 hours and cost little more than £20. The 1991 exchange took 15 hours to install.

The 1973 whole-life study is the best measure of the total burden. For a 32-ton articulated tractive unit over a 200,000-mile life, a ten-vehicle fleet generated 326 maintenance jobs costing £5,000, divided roughly equally between labour and materials, plus £3,200 for 1,600 hours off the road. The whole-life maintenance cost including downtime was £8,200, against a running cost of 17p a mile.

### Table 5.1 Lorries and vans

| Year | Vehicle or item | Interval | Cost | Scope | Downtime | Source | Conf. |
|---|---|---|---|---|---|---|---|
| 1949 | Fleet policy, vehicles under 1 ton | Complete overhaul 30,000 miles; top 15,000 and 45,000 | — | 120 vehicles | — | S20 | MEASURED |
| 1949 | Fleet policy, vehicles over 1 ton | Engine complete 60,000; chassis and body 45,000; top 15,000, 75,000, 90,000 | — | 120 vehicles | — | S20 | MEASURED |
| 1950 | 3-5 ton lorry | Top overhaul 30,000 miles | £7 garage; £5 10s own workshop | — | — | S15 | STATED |
| 1950 | 3-5 ton lorry | Complete engine overhaul 90,000 miles | £120-£140 reconditioned engine | — | — | S15 | STATED |
| 1950 | Lorry, example | Engine overhaul and chassis repair 48,000 miles | £80 | — | — | S15 | STATED |
| 1953 | Bedford tipper | Engine change 60,000 miles | — | 19 tippers | 6.5 hours | S17 | MEASURED |
| 1953 | Bedford tipper | Back axle or gearbox renewal | — | — | 1.5 hours | S17 | MEASURED |
| 1955 | Petrol 6-tonner | Engine overhaul 50,000 miles | £60 | — | — | S16 | STATED |
| 1955 | Petrol 6-tonner | Chassis and body overhaul 100,000 miles | £220 including second engine | — | — | S16 | STATED |
| 1955 | Petrol 6-tonner | Brake reline 10,000 miles | £5 10s | — | — | S16 | STATED |
| 1955 | Petrol 6-tonner | Decarbonise 10,000 miles | £2 10s | — | — | S16 | STATED |
| 1956 | Reliant 5-cwt van | Engine replacement 15,000 miles | Little more than £20 | — | Under 24 hours | S18 | MEASURED |
| 1956 | Commer 8-cwt van | Engine replacement 40,000 miles | — | — | — | S18 | MEASURED |
| 1956 | Thornycroft 7-ton lorry | Engine replacement 73,000 miles | — | — | — | S18 | MEASURED |
| 1959 | AEC exchange engine | — | £205-£285 | 30-35 a week; one-year guarantee | — | S19 | MEASURED |
| 1968 | GPO fleet | Docking 15,000 miles | — | 60,000 vehicles | — | S21 | MEASURED |
| 1972 | AEC 691 bus engine | — | £195 repair against £295 new | — | — | S22 | MEASURED |
| 1972 | Rear axle casing | — | £50 repair against £250 new | — | — | S22 | MEASURED |
| 1973 | 32-ton articulated unit | 200,000-mile life; 326 jobs | £5,000 maintenance plus £3,200 downtime | 10-vehicle fleet | 1,600 hours | S23 | STATED |
| 1980 | Bedford KM rebuild | — | £7,800 against £15,000 new | Full rebuild | — | S24 | MEASURED |
| 1987 | Cummins remanufactured engine | — | 30-50 per cent below new | — | — | S25 | STATED |
| 1991 | Scania 142 V8 | — | £12,611.54 exchange | — | 15 hours to install | S26 | MEASURED |
| 1991 | Scania 142 in-frame overhaul | — | £3,210.88 in parts | — | 40 hours; 7 days for recon | S26 | MEASURED |
| 1993 | 300 hp tractor engines | — | Scania £10,534; Renault £5,382; Mercedes £15,274; Cummins short £2,750 | Exchange, list ex-VAT | — | S27 | MEASURED |

## 6. Trams and light rail

The modern record is much better than the historic one.

**Metrolink, 2004.** The original 26 T68 trams, built for the 1992 opening, had each run about one million miles. The mid-life refurbishment cost £80,000 a tram and included new seats, floors, a new livery and a major mechanical overhaul. One tram was done first for reaction, then the fleet. The refurbishment did not cover the trams bought for the Salford Quays and Eccles line.

**Supertram, 2026.** The 25 Siemens-Duewag trams date from the 1992-94 opening (the award notice says 1992, the tender notice says 1994) and are expected to run to 2035. The life extension contract was awarded to Brodie Engineering at £21.4m plus VAT, about £856,000 a tram (COMPUTED), with a two-year programme to the end of November 2028. The scope is structural strength, crashworthiness, reliability and corrosion repair; the corrosion allowance is explicitly provisional until each tram is stripped. The tender's estimated value was £13m, so the award is 65 per cent above the estimate. The trams are about 32-34 years old at award and the work buys roughly nine more years.

Croydon, Edinburgh and Blackpool yielded no measured overhaul contract in this pass. Croydon's CR4000 fleet is being replaced rather than life-extended, Edinburgh's fleet is too new, and Blackpool's heritage rebuilds are not priced in public documents.

No measured historic municipal tramcar overhaul price was found. The corporation accounts that were accessible combine tramcar repairs with permanent way and electrical equipment, and the tramway histories describe rebuilding programmes without prices. The Blackpool Standard cars of the 1920s were rebuilds of older cars so extensive that they were effectively new cars, but no cost per car was found.

### Table 6.1 Trams

| Year | Vehicle or item | Interval | Cost | Scope | Downtime | Source | Conf. |
|---|---|---|---|---|---|---|---|
| 2004 | Metrolink T68 | 12 years, about 1 million miles | £80,000 a tram | 26 trams; seats, floors, livery, mechanical overhaul | — | S28 | MEASURED |
| 2024 | Supertram life extension, tender estimate | — | £13m for 25 | Estimate only | — | S30 | STATED |
| 2026 | Supertram life extension, award | About 32-34 years since new | £21.4m plus VAT for 25, £856,000 each COMPUTED | Structural, crashworthiness, corrosion, reliability | 2-year programme | S29 | MEASURED |

## 7. Ships

The classification cycle is the structure within which ship overhaul costs sit. Lloyd's Register's 1870 rules put 100A1 and 90A1 ships on special survey every four years, and lower classes every three. The modern cycle is a five-year special survey with intermediate and annual surveys (STATED, standard classification practice); the practical drydocking interval is 2.5-5 years (S31). Hydrex notes that the usual mandatory interval is 2.5-5 years depending on ship type and age, extended to 7.5 years for certain ships under certain conditions.

The cost evidence is benchmark rather than contract, with one good company disclosure:

- Moore Stephens' OpCost 2009, reported by Dry Cargo International in 2010, put average drydock costs for bulk carriers at US$1,105,981 to US$1,909,589, with Capesize at the top of the range and Handymax at the bottom. Drydocking costs for bulkers rose 33 per cent in 2008 over 2007.
- 2020 Bulkers disclosed drydocking for Bulk Shenzhen and Bulk Sydney at a total cost of US$2.3m in the first quarter of 2025, and Bulk Sao Paulo at US$1.2m in May 2025. The company also reported 63 days off-hire in the quarter in connection with drydocking, for the two ships.
- A 2026 ship-repair guide gives a worked example of a 14-year-old chemical tanker at its third special survey: a US$4.2m package covering hull structural inspection, tank coating renewal, ballast water treatment installation, main engine major overhaul, machinery work and the full painting cycle, lasting 47 days against an estimate of 36.

Downtime for a routine five-year docking is much shorter. The Baltic Exchange's standard five-year drydocking specification assumes twelve days at the yard, five of them in dry dock, with no steel exchange and no full blasting.

### Table 7.1 Ships

| Year | Vessel or item | Interval | Cost | Scope | Downtime | Source | Conf. |
|---|---|---|---|---|---|---|---|
| 1870 | Lloyd's Register 100A1 and 90A1 | Special survey every 4 years | — | Iron ships | — | S36 | MEASURED (rule) |
| 2012 | Most ships | Drydocking every 2.5-5 years, up to 7.5 years | — | — | — | S31 | STATED |
| 2010 | Bulk carriers, OpCost 2009 | 5-year cycle | US$1,105,981-1,909,589 per docking | Benchmark | — | S32 | MEASURED |
| 2010 | Bulk carriers, 2008 against 2007 | Annual | Drydocking cost up 33 per cent | Benchmark | — | S32 | MEASURED |
| 2025 | 2020 Bulkers, two ships | — | US$2.3m total | Q1 2025 dockings | 63 days off-hire for two ships | S33 | MEASURED |
| 2025 | 2020 Bulkers, one ship | — | US$1.2m | May 2025 docking | — | S33 | MEASURED |
| 2026 | Chemical tanker, 14 years | Third special survey | US$4.2m | Hull, coatings, BWTS, main engine, painting | 47 days | S34 | STATED |
| 2012 | Standard five-year docking | 5 years | — | No steel exchange, no full blasting | 12 days at yard, 5 in dock | S35 | STATED |

## 8. Aircraft

Aircraft maintenance is organised in letter checks that are being replaced by task intervals, but the economics are still described by the old letters.

- **A check** every 500-600 flight hours, or every 8-10 weeks; 6-24 hours on a 737.
- **C check** every 18-24 months, or 6,000 flight hours for system tasks, 4,500 flight cycles for structural items and 20 months for zonal tasks on the A320; about three weeks.
- **D check** or heavy maintenance visit every six years for older types, twelve years for the 787; three to six weeks and several million dollars.

The A320 maintenance guide gives a direct cost for the base-check cycle: US$3.5m per 26,000 flight cycles for base checks, which is US$128 per flight cycle, plus US$77,000 a year for A checks and US$595,000 a year for line and ramp checks. The same guide gives a total airframe and component maintenance cost of about US$668 per flight hour for the A320 family.

Engine shop visits are the largest single event:

- CFM56-5A: first shop visit US$1.15m at 8,000 engine flight cycles, performance restoration; second US$1.5m with core and low-pressure turbine work plus US$880,000 of life-limited parts; third US$1.3m with fan and booster work plus US$875,000 of life-limited parts.
- CFM56-5B: removal intervals of 15,000 engine flight cycles and 27,000 engine flight hours for the first two removals, with shop visits in the same cost range.
- CFM56-7B: a medium-interval shop visit at 11,000-15,000 engine flight cycles costs about US$2.6m; a long-interval visit at 17,000-20,000 cycles costs about US$3.8m.

In the CFM56-5A series the second shop visit is the most expensive, because it carries the life-limited parts replacement, and the third falls back a little. That is a direct, measured example of overhaul cost escalation.

### Table 8.1 Aircraft

| Year | Vehicle or item | Interval | Cost | Scope | Downtime | Source | Conf. |
|---|---|---|---|---|---|---|---|
| 2003 | CFM56-5A first shop visit | 8,000 engine flight cycles | US$1.15m | Performance restoration | — | S38 | MEASURED |
| 2003 | CFM56-5A second shop visit | 8,000 engine flight cycles | US$1.5m plus US$880,000 LLP | Core and LPT | — | S38 | MEASURED |
| 2003 | CFM56-5A third shop visit | 8,000 engine flight cycles | US$1.3m plus US$875,000 LLP | Fan and booster | — | S38 | MEASURED |
| 2021 | CFM56-7B medium shop visit | 11,000-15,000 engine flight cycles | US$2.6m | Medium workscope | — | S39 | MEASURED |
| 2021 | CFM56-7B long shop visit | 17,000-20,000 engine flight cycles | US$3.8m | Long workscope | — | S39 | MEASURED |
| 2010 | A320 family base checks | 26,000 flight cycles | US$3.5m | Base checks | — | S37 | MEASURED |
| 2010 | A320 family A checks | 6-7 a year | US$77,000 a year | A checks | — | S37 | MEASURED |
| 2010 | A320 family C-check tasks | 6,000 flight hours | — | System tasks | — | S37 | MEASURED |
| 2016 | Qantas 737 and A330 C check | 18-24 months | — | — | 3 weeks | S40 | STATED |
| 2016 | Qantas D check | 6 years | Several million dollars | Full dismantle | 3-6 weeks | S40 | STATED |
| 2022 | Boeing 737-800 P2F | — | US$4.2m | Passenger-to-freighter conversion | 4-8 months | S41, S42 | STATED |
| 2022 | Airbus A321-200 P2F | — | US$6.1m | Conversion | 4-8 months | S41, S42 | STATED |
| 2022 | Boeing 767-300ER P2F | — | US$14.7m | Conversion | 4-8 months | S41, S42 | STATED |
| 2022 | Airbus A330-300 P2F | — | US$18.4m | Conversion | 4-8 months | S41, S42 | STATED |

## 9. How cost escalates with successive overhauls

The evidence supports a consistent shape, with three mechanisms.

**1. The second overhaul carries the expensive renewal.** The first major overhaul of an engine usually rebores or reconditions the original parts. The second has to resleeve, replace life-limited parts or grind the crankshaft to a new undersize. Midland Red bored the block 0.030 in oversize at the first D dock and resleeved at the second. Burton-on-Trent rebored at 50,000 miles, resleeved at 100,000 and changed the unit at 200,000. The CFM56-5A first shop visit was US$1.15m, the second US$1.5m because it added US$880,000 of life-limited parts, and the third US$1.3m. The CFM56-7B medium visit was US$2.6m and the long visit US$3.8m. This is the strongest evidence for `overhauls_before_max_cost` = 2 and a max/initial ratio of about 1.3-1.5.

**2. The late-life overhaul can fall again.** Once the expensive structural renewal has been done, the next overhaul is cheaper. The CFM56-5A third visit at US$1.3m is below the second at US$1.5m. London Transport's "final overhaul" at the end of a bus's life used plonk-on plates and minimum structural replacement, so it cost less than a mid-life overhaul. This argues for a maximum at the second or third overhaul, not a straight line to the end of life.

**3. A one-off life extension is a different event from a recurring overhaul.** The Metrolink mid-life refurbishment at £80,000 in 2004 and the Supertram life extension at £856,000 in 2026 are not successive overhauls of the same kind; the second is a structural life extension at about 32-34 years. In engine terms the recurring overhaul should carry `max_overhaul_cost`, and the life extension should carry `upgrade_price`.

The bus case is the least well evidenced for escalation. The 1965 £2,000 and the 1985 derived £20,000-£25,000 are twenty years apart and mostly nominal. The structural logic is the same as for lorries and aircraft, but no series of successive bus overhaul invoices was found. I would use a 1.5 ratio for buses, not the 1.8-2.5 that the lorry and ship evidence might suggest.

## 10. Upgrade and rebuild costs

| Year | Vehicle or item | Cost | Comparator | Source | Conf. |
|---|---|---|---|---|---|
| 1977 | Leyland National 680H conversion | About £7,000 | Already known; not re-researched | — | MEASURED (known) |
| 1980 | Bedford KM full rebuild | £7,800 | £15,000 new, so 52 per cent | S24 | MEASURED |
| 1987 | Cummins remanufactured engine | 30-50 per cent below new | New engine price | S25 | STATED |
| 1991 | ELC Leyland National Greenway | £45,000 | About half the price of a new bus | S12 | MEASURED |
| 1991 | ELC Atlantean conversion | £37,000 | New single-deck body | S12 | MEASURED |
| 2004 | Metrolink T68 mid-life refurbishment | £80,000 a tram | 12-year-old tram | S28 | MEASURED |
| 2022 | 737-800 passenger-to-freighter | US$4.2m | 4-8 months downtime | S41, S42 | STATED |
| 2022 | A321-200 passenger-to-freighter | US$6.1m | 4-8 months downtime | S41, S42 | STATED |
| 2022 | 767-300ER passenger-to-freighter | US$14.7m | 4-8 months downtime | S41, S42 | STATED |
| 2022 | A330-300 passenger-to-freighter | US$18.4m | 4-8 months downtime | S41, S42 | STATED |
| 2023 | Equipmake battery-electric repower | £1.75m for 10, £175,000 a bus | New battery-electric bus | S43 | MEASURED |
| 2026 | Supertram life extension | £21.4m for 25, £856,000 a tram | About 32-34-year-old tram | S29 | MEASURED |

The cleanest comparator is the 1991 ELC Greenway: £45,000 for a new Gardner engine, a reconditioned gearbox, a new aluminium body and the running gear brought to top condition, stated by the supplier to be about half the price of a new vehicle. That is a genuine rebuild, not a repaint, and it is the best single figure for the bus `upgrade_price`.

The 2023 Equipmake repower is the best modern figure: £175,000 a bus for a battery-electric driveline, on a 2012 open-top double-decker. It is a conversion, not a new vehicle, and it is the closest analogue to a mid-life re-engining.

The 1980 Bedford KM rebuild at £7,800 against £15,000 new is the best lorry rebuild figure, and it is a complete vehicle rebuild rather than a component exchange.

## 11. Recommended engine values

The recommendations are shares of the object's purchase price, not absolute sums, because the purchase price varies by object and is set by the separate capital pass. The kilometre equivalents are COMPUTED from the time intervals using an assumed annual distance: 40,000 km a year for a pre-war bus, 55,000 km for a post-war bus, 60,000 km for a modern bus, 40,000 km for a historic tram, 60,000 km for a modern tram, 100,000 km for a ship, and 2-3 million km for an airliner. They exist only because `max_distance_between_overhauls` is in kilometres; the evidence itself is in years or miles.

| Class and era | Interval as evidenced | km equivalent (COMPUTED) | Initial overhaul, % of purchase | Max overhaul, % of purchase | Overhauls before max | Downtime, tenths of a month | Upgrade, % of purchase |
|---|---|---|---|---|---|---|---|
| Bus, 1920-1945 | 12 months | 40,000 | 8 | 12 | 2 | 0.7 | 15 |
| Bus, 1945-1985 | 4 years | 220,000 | 20 | 30 | 2 | 3 | 30 |
| Bus, 1985-2026 | 10 years mid-life | 600,000 | 10 | 15 | 1 | 6 | 40 |
| Coach, 1945-1985 | 4 years | 300,000 | 15 | 25 | 2 | 3 | 25 |
| Coach, 1985-2026 | 10 years | 700,000 | 10 | 15 | 1 | 5 | 35 |
| Lorry, 1945-1970 | 50,000 miles | 80,000 | 8 | 15 | 2 | 1 | 15 |
| Lorry, 1970-2000 | 100,000 miles | 160,000 | 12 | 22 | 2 | 3 | 25 |
| Lorry, 2000-2026 | 500,000 km | 500,000 | 15 | 25 | 1 | 4 | 35 |
| Van, 1945-1980 | 30,000 miles | 48,000 | 8 | 15 | 2 | 0.5 | 15 |
| Van, 1980-2026 | 150,000 km | 150,000 | 10 | 20 | 1 | 1 | 25 |
| Tram, 1900-1950 | 7 years | 280,000 | 8 | 15 | 2 | 4 | 30 |
| Tram, 1990-2026 | 12 years | 720,000 | 8 | 12 | 2 | 8 | 50 |
| Ship, 1870-1970 | 4 years | 400,000 | 2 | 4 | 3 | 4 | 10 |
| Ship, 1970-2026 | 5 years | 500,000 | 2 | 5 | 3 | 4 | 10 |
| Aircraft, 1950-1990 | 6 years | 12,000,000 | 2 | 3 | 2 | 14 | 10 |
| Aircraft, 1990-2026 | 6 years | 18,000,000 | 2 | 3 | 2 | 14 | 10 |

Notes on the bands:

- **Bus 1920-1945.** The 8-12 per cent band is inferred from the scale of the Chiswick work, not from a measured invoice. The £14 paint and varnish cost of 1926 is plainly a small fraction of the price of a new bus, which was in the thousands of pounds by the 1930s (S44), so the full overhaul must be several times that. The band is an ESTIMATE; the two-day downtime is measured.
- **Bus 1945-1985.** The 20-30 per cent band is anchored on £2,000 against a new London double-decker of roughly £6,000-£8,000 in the mid-1960s (ESTIMATE), which is 25-33 per cent, and on the 1985 derived £20,000-£25,000 against a new bus of roughly £60,000-£70,000 (ESTIMATE), which is about 30-40 per cent. The overhaul costs are measured; the new prices are not.
- **Bus 1985-2026.** The 10-15 per cent band is a mid-life refurbishment, not a body-off rebuild. The 40 per cent upgrade is the battery-electric repower at £175,000 against a new electric bus of about £400,000-£450,000 (ESTIMATE).
- **Coach.** Coaches do higher annual mileage than city buses, so the same four-year cycle buys more kilometres. The share is lower than a bus because the body is lighter and the seating less intensively used.
- **Lorry 1945-1970.** The 8 per cent initial and 15 per cent maximum are anchored on £60 for an engine overhaul against a new 6-tonner of roughly £1,000-£1,200 (ESTIMATE), and on £220 for a chassis and body overhaul, which is about 18-22 per cent.
- **Lorry 1970-2000.** The 12-22 per cent band is anchored on £10,534-£12,612 for an exchange engine against a new 38-tonne tractor unit of roughly £50,000-£60,000 (ESTIMATE), which is 18-25 per cent.
- **Tram 1990-2026.** The 8 per cent initial is measured: £80,000 against a new T68 of about £1m (ESTIMATE). The 50 per cent upgrade is the Supertram life extension at £856,000 against a new tram of about £1.7m-£2m (ESTIMATE).
- **Ship.** The 2-5 per cent band is anchored on US$1.2m for a 2025 bulk-carrier drydocking against a newbuild value of roughly US$60m-US$70m (ESTIMATE), and on the 2009 range of US$1.1m-1.9m. The three overhauls before maximum reflect the 5-year special survey cycle and the rising cost of the second and third special surveys. The 1870-1970 band is an extrapolation from the classification cycle, not a measured price series.
- **Aircraft.** The 2-3 per cent band is anchored on US$3.5m for a 26,000-cycle base-check package against a new A320 of roughly US$45m-US$50m (ESTIMATE), and on a D check at several million dollars. The 14 tenths of a month is the three-to-six-week D check. The engine shop visit is a separate event and is not in this row; it is better treated as a separate overhaul with its own interval in engine flight cycles. The 1950-1990 band is an extrapolation from the later check structure, not a measured price series.

## 12. Dead ends

- **Historic tram overhaul prices.** No municipal tramcar overhaul price was found. The corporation accounts that are online combine car repairs with permanent way and electrical equipment. The tramway histories describe rebuild programmes, not invoices. A corporation abstract of accounts for Liverpool, Leeds, Sheffield or Blackpool would be needed.
- **Pre-1945 bus overhaul prices.** The Chiswick accounts are not online. The only measured cost found is the £14 paint and varnish figure for 1926. The London Transport Museum and TfL Corporate Archives hold the works records, but they are not digitised.
- **Coach body overhaul.** No coach-specific body overhaul price was found; the coach evidence is engine overhaul mileage (Don Everall, 1952).
- **Van overhaul.** Apart from the Reliant engine replacement at £20 and 15,000 miles, no van body or chassis overhaul price was found. Vans were generally run to disposal rather than overhauled.
- **Cab refurbishment.** No measured cab refurbishment price was found for lorries or buses; cab work appears inside the chassis and body overhaul, not as a separate priced item.
- **Ship drydocking before 2009.** The classification rules give the cycle back to 1870, but no measured drydocking price before the Moore Stephens 2009 benchmark was found. Statutory survey fees, such as the £198 dry-dock survey fee in the Irish Merchant Shipping (Fees) Order 1987, are not a proxy for the cost of docking and were not used.
- **Aircraft maintenance before the 2000s.** Manufacturer maintenance planning documents are not public, and the older trade press is not indexed. The aircraft evidence starts in the 2000s.
- **Drewry.** The 2025/26 Ship Operating Costs report has the right tables, but the report is paywalled. Only the table of contents was accessible, so the 2025 cost figure comes from 2020 Bulkers' company disclosure, not from Drewry.
- **Aircraft Monitor.** The Aircraft Monitor maintenance-reserve PDFs were not text-extractable, so their A320 and 737-800 check costs were not used, even though the search index showed them. The aircraft table relies on Aircraft Commerce and Qantas.
- **Commercial Motor search.** The archive's own search is behind a JavaScript challenge. Articles were reached through Exa and fetched through the Exa contents endpoint. This worked for every article cited, but it makes systematic coverage of the archive impossible in one pass.
- **A £29.5m derivation.** The 1985 per-overhaul cost is a COMPUTED figure from turnover, fleet size and cycle. It is useful as an order of magnitude, not as a measured invoice.

## 13. Sources

- **S1** Commercial Motor, "A Works Which Overhauls 15 Buses Per Day", 31 January 1922, p. 16. https://archive.commercialmotor.com/article/31st-january-1922/16/a-works-which-ovei
- **S2** Commercial Motor, "Two Days for a Bus Overhaul", 29 June 1926, p. 9. https://archive.commercialmotor.com/article/29th-june-1926/11/two-days-for-a-bus-overhaul
- **S3** Commercial Motor, "How Precision Maintenance Keeps 1,000 Buses on the Road", 11 February 1938, p. 96. https://archive.commercialmotor.com/article/11th-february-1938/96/how-precision-maintenance-keeps-1000-buses-on-the-
- **S4** Commercial Motor, "Structural Maintenance and Care of Finishes Will Prolong the Life", 19 December 1947, p. 43. https://archive.commercialmotor.com/article/19th-december-1947/43/structural-maintenance-and-care-of-finishes-will-p
- **S5** Commercial Motor, "Maintenance for Profit", 21 March 1952, p. 42. https://archive.commercialmotor.com/article/21st-march-1952/42/maintenance-fc-profit
- **S6** Commercial Motor, "Six Approaches to Maintenance", 11 April 1952, p. 42. https://archive.commercialmotor.com/article/11th-april-1952/45/six-appr-maint-lches-to-tance
- **S7** Commercial Motor, "Thinking in the Future With Liverpool Buses", 28 July 1961, p. 50. https://archive.commercialmotor.com/article/28th-july-1961/52/thinking-in-the-future-with-liverpool-buses
- **S8** Commercial Motor, "Overhauling the Routemaster", 22 January 1965, p. 59. https://archive.commercialmotor.com/article/22nd-january-1965/59/ating-the-routemaster
- **S9** Commercial Motor, "LT works plan", 7 April 1984, p. 22. https://archive.commercialmotor.com/article/7th-april-1984/22/lt-works-plan
- **S10** Commercial Motor, "Aldenham loses some work", 30 November 1985, p. 22. https://archive.commercialmotor.com/article/30th-november-1985/22/aldenham-loses-some-work
- **S11** Commercial Motor, "Fighting to survive", 17 January 1987, p. 39. https://archive.commercialmotor.com/article/17th-january-1987/39/fighting-to-survive
- **S12** Commercial Motor, "Rejuvenation for the Atlanteans", 11 July 1991, p. 12. https://archive.commercialmotor.com/article/11th-july-1991/12/rejuvenation-for-the-atlanteans
- **S13** London Transport Museum, colour transparency 2002/18956, "A Routemaster bus being overhauled at Aldenham Works, 1970-1980". https://www.ltmuseum.co.uk/collections/collections-online/photographs/item/2002-18956
- **S14** TfL Corporate Archives, Research Guide No 33: Aldenham Bus Works. https://content.tfl.gov.uk/research-guide-33-aldenham-bus-works.pdf
- **S15** Commercial Motor, "What an Engine Costs", 11 August 1950, p. 46. https://archive.commercialmotor.com/article/11th-august-1950/46/what-an-engine-costs
- **S16** Commercial Motor, "Maintenance What It Costs", 28 January 1955, p. 50. https://archive.commercialmotor.com/article/28th-january-1955/53/maintenance-what-it-costs
- **S17** Commercial Motor, "Seeing to It Himself", 27 February 1953, p. 38. https://archive.commercialmotor.com/article/27th-february-1953/38/seeing-to-it-himself
- **S18** Commercial Motor, "Transp for £30,000 Loads", 17 August 1956, p. 50. https://archive.commercialmotor.com/article/17th-august-1956/53/transp-for-30000-loads
- **S19** Commercial Motor, "Engine Rebuilding to Plan", 10 April 1959, p. 72. https://archive.commercialmotor.com/article/10th-april-1959/72/engine-rebuilding-to-plan
- **S20** Commercial Motor, "Preventive Maintenance for Catered Fleet", 24 June 1949, p. 14. https://archive.commercialmotor.com/article/24th-june-1949/16/preventii-laintenance-for-catered-fleet
- **S21** Commercial Motor, "Flowline Solves Giant Problem", 5 April 1968, p. 94. https://archive.commercialmotor.com/article/5th-april-1968/94/flowline-solves-giant-problem
- **S22** Commercial Motor, "When to repair rather than replace", 17 November 1972, p. 98. https://archive.commercialmotor.com/article/17th-november-1972/98/when-to-repair-rather-than-replace
- **S23** Commercial Motor, "Reducing maintenance costs", 20 April 1973, p. 31. https://archive.commercialmotor.com/article/20th-april-1973/31/reducing-maintenance-costs
- **S24** Commercial Motor, "Half-price rebuilds: are they bargains?", 12 July 1980, p. 92. https://archive.commercialmotor.com/article/12th-july-1980/93/half-price-rebuilds-are-they-bargainsi
- **S25** Commercial Motor, "Specialist LP", 29 October 1987, p. 32. https://archive.commercialmotor.com/article/29th-october-1987/32/specialist-lp
- **S26** Commercial Motor, "Engine Options", 7 November 1991, p. 104. https://archive.commercialmotor.com/article/7th-november-1991/104/engine-options
- **S27** Commercial Motor, "The Sum of the Parts Equals...", 23 December 1993, p. 112. https://archive.commercialmotor.com/article/23rd-december-1993/112/the-sum-of-the-parts-equals
- **S28** Manchester Evening News, "Metrolink fleet's million-mile service", 10 August 2004. https://www.manchestereveningnews.co.uk/news/greater-manchester-news/metrolink-fleets-million-mile-service-1148795
- **S29** Rail Business UK, "Preferred bidder selected for South Yorkshire Supertram refurbishment", 29 October 2026. https://www.railbusinessuk.com/light-rail/2026/10/29/preferred-bidder-selected-for-south-yorkshire-supertram-refurbishment/
- **S30** Find a Tender, South Yorkshire Mayoral Combined Authority, "Supertram, Life Extension of 25 Trams", 2024/S 000-026935, 22 August 2024. https://www.find-tender.service.gov.uk/Notice/026935-2024
- **S31** Hydrex, White Paper No 11: Extending the Interval Between Drydocking to Ten Years, 2012. https://boudvanrompay.com/wp-content/uploads/2022/11/WhitePaper11.pdf
- **S32** Dry Cargo International, "Bulker maintenance", 24 March 2010. https://www.drycargomag.com/bulker-maintenance
- **S33** 2020 Bulkers Ltd, Board of Directors' Report Q1 2025, 7 May 2025. https://storage.mfn.se/1625deaa-7aff-4987-899a-1398322dacc5/2020-bulkers-board-of-directors-report-q1-2025.pdf
- **S34** PortServiceFinder, "Singapore Drydock and Ship Repair Complete Guide 2026", 5 June 2026. https://www.portservicefinder.com/blog/singapore-drydock-ship-repair-welding-painting-2026-complete-guide
- **S35** Baltic Exchange, Operating Expense Index brochure. https://www.balticexchange.com/content/dam/balticexchange/consumer/data-services-/documents-/brochures/The%20Baltic%20Exchange%20Operating%20Expense%20Index.pdf
- **S36** Lloyd's Register Foundation, "Classification symbols 1764-1994". https://heritage.lrfoundation.org.uk/classification-symbols-1764-1994
- **S37** Aircraft Commerce, "A320 family maintenance analysis and budget", Issue 44. https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/A320%20FAMILY/ISSUE%2044-A320%20MTCE.pdf
- **S38** Aircraft Commerce, "CFM56-5A/-5B owner's and operator's guide", Issue 50. https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/CFM56-5A-5B/ISSUE%2050-CFM56-5A-5B%20GUIDE.pdf
- **S39** Aircraft Commerce, "CFM56-7B maintenance management and shop visit inputs and reserves", 2021. https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/General%20Articles/2021/134_MTCE_A.pdf
- **S40** Qantas Newsroom, "The A, C and D of aircraft maintenance", 2016. https://news.qantas.com/roo-tales/2016/the-a-c-and-d-of-aircraft-maintenance
- **S41** Air Cargo News, "Financial risks for P2F conversions", 13 January 2022. https://www.aircargonews.net/business/2022/01/financial-risks-for-p2f-conversions/
- **S42** FreightWaves, "Orders for freighter aircraft slow to a trickle", 14 September 2023. https://www.freightwaves.com/news/orders-for-freighter-aircraft-slow-to-a-trickle
- **S43** routeone, "Equipmake to repower 10 Big Bus Tours Ankai open-tops to electric", 2 October 2023. https://www.route-one.net/news/equipmake-to-repower-10-big-bus-tours-ankai-open-tops-to-electric/
- **S44** Hanger London, "Before the Routemaster: AEC RT (Regent III) and RF (Regal IV) buses" (1939 RT about £4,000). https://www.hangerlondon.com/rt-london-bus/
- **S45** Commercial Motor, "Era of the one-man bus", 30 September 1966, p. 133 (Park Royal Leyland Panther about £10,000). https://archive.commercialmotor.com/article/30th-september-1966/134/era-of-the-one-man-bus
- **S46** Red-RF, "Bus overhauls", undated, with detail attributed to Brian Watkinson, Aldenham from 1965. http://www.red-rf.com/lt_operations_-_general/overhauls.aspx
