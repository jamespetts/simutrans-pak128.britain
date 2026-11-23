---
status: draft
verified: New ex-15 @ 33cf9b106
---
# Cost data coverage

**Covers**: the quality of the historical cost data available for each class of in-game object with
a cost of any kind, what each class's data can and cannot support, and the main gaps. Status flags
(balanced / class data / item data / extrapolate) are in
[cost-balancing-register](cost-balancing-register.md); the figures themselves are in the evidence
docs named below and in the working spreadsheets `New/cost-balancing-capital.xlsx` and
`New/cost-balancing-maintenance.xlsx`.

## Rating scale

- **Good** — measured figures spanning the era or a usable specification-normalised ladder; enough
  to set levels and interpolate individual items.
- **Fair** — measured figures but thin: one era, one region, or a ladder that covers only part of
  the item range.
- **Poor** — a few isolated points, proxies only, or evidence recorded as unusable for calibration.
- **None** — no measured historical cost data exists in the knowledge base.

## Vehicles

**Rail locomotives — Good (capital), Fair (maintenance).** Thirteen dated purchase prices 1831-1960
covering pre-grouping steam, Grouping steam, early diesels and one industrial engine; two
specification-normalised ladders (price per ton of engine weight, £32-78 steam era; £ per 1,000
draw-bar hp, 1951 Hansard). The diesel-to-steam price ratio (2.5x at equivalent power, 1955
modernisation report) brackets the traction transition. Maintenance: 1892 repair per train-mile for
six companies, Hill's £253 per engine-year (about 12% of purchase price a year), renewals 3.6% a
year; modern rebuild costs. Gaps: no pre-1890 repair figure; no per-hour British diesel/electric
operating figure; no price surface can be fitted (only eight classes matched to a pakset weight).
Calibration use: interpolate steam-era locomotives by weight; do not extrapolate diesels from steam
or vice versa.

**Rail carriages — Good.** Nine dated build prices 1846-1980s plus type-band ladders (pre-grouping
bogie third £1,200-1,500; corridor composite or dining £1,600-2,000; twelve-wheel diner £2,500-3,000;
1920s corridor third £2,300-2,500). The NER build records (1905-34, consecutive years, stated
diagrams and prices) are the strongest block in the vehicle evidence and the natural basis for a
carriage price surface. Maintenance: Hill's £18-45 per vehicle-year 1892 with the full `fixed_cost`
conversion recorded. Gap: nothing between 1934 and the early 1980s.

**Rail wagons — Good (capital), None (maintenance).** Eleven Shildon 1906 builds priced by capacity,
a clean £6.37-8.40 per ton of capacity ladder (mean £7.2) with a modest fixed element and a
speculation point at 23 tons. No per-wagon-year maintenance figure exists in any source read (Hill's
wagon column is unreadable; the Railway Returns route is untried).

**Multiple units — Poor.** Modern per-vehicle-mile maintenance only (diesel £0.80, electric £0.44 at
2013 prices; Underground, Civity, ScotRail comparators). No purchase price ladder at all.

**Road vehicles (buses, coaches, lorries) — Good.** The 2026-11-23 pass adds 284 measured rows:
the Commercial Motor "Municipal Purchases and Proposals" series for buses (72 prices, 1909-55,
including a four-maker chassis tender at Salford in 1928 and a ten-bidder trolleybus tender at
Manchester in 1937), the ten-make 1960 lorry price list with a further 129 lorry and van prices
1919-61, and a measured repair series from operator accounts (Edinburgh 1925, Glasgow 1931-34)
with the purchase price in the same accounts. Maintenance is charged from the measured
per-kilometre total, split 75 per cent distance-driven to 25 per cent standing; the split is an
estimate and is recorded as one. Gaps: no 1939-54 bus price ladder worth the name; the
Commercial Motor cost tables are page images and could not be machine-read; Tilling-Stevens has
no price in any year. Modern prices (1980-2026) are now measured from 59 tender awards and price
lists, which show a 40 per cent real rise after 1990 and a battery-electric bus premium of about
twice the diesel price.
[vehicle-cost-evidence](vehicle-cost-evidence.md) "Buses, coaches and lorries";
[cost-balancing/research-pricing-report-29](cost-balancing/research-pricing-report-29.md),
[-30](cost-balancing/research-pricing-report-30.md),
[-31](cost-balancing/research-pricing-report-31.md),
[-32](cost-balancing/research-pricing-report-32.md).

**Trams and light rail — Good (modern capital), Fair (historic maintenance).** The 2026-11-23
pass adds 28 rows. Modern vehicle prices are now solid: every UK order 2007-19 that prices
vehicles alone falls between £1.80m and £2.72m a tram (Metrolink's seven orders, Croydon,
DLR, West Midlands, Edinburgh's £2.396m settled final account, Blackpool's £2.0625m), against
£575-590 for a municipal car in 1901-04 and £1,750-2,688 for Blackpool's 1926-34 cars. Modern
rolling-stock maintenance is anchored on Nottingham 2011: £101m over 23 years for 37 trams,
£118,657 a tram-year. Historic maintenance remains the Ministry of Transport returns 1913-30
on a **combined** head that includes permanent way and line electrical equipment, so it is an
upper bound on car cost. Gaps: nothing measured between 1950 and 1994, and no car-only
historic maintenance figure from an abstract of accounts.
[vehicle-cost/tram-maintenance](vehicle-cost/tram-maintenance.md);
[cost-balancing/research-pricing-report-35](cost-balancing/research-pricing-report-35.md).

**Ships — Fair.** 76 research rows, 1845-1987, including ten 1927-38 ferries of 38-2,910
GT at £70-80/GT and 14 British passenger vessels 1924-38 fitted at £149.7 × GT^0.90 (R² 0.992).
Cargo ships are flat at £149-173/GT (1950-53) and the Fairplay tramp at £6.3-8.1 per deadweight
ton (1898-1930). Repair evidence remains Martin's 5%-of-capital rule and dry-docking figures, not
per-voyage costs. Gross tonnage is not recorded in the pakset, so the workbook applies the ladder
through capacity (passengers, cargo tonnes). `[LITERATURE: research pass 25; Moses 2010, Table 2.7;
Wallasey fleet list]`

**Inland boats — Fair.** Motor narrowboats £700-900 (1928-37), a butty £390, a steam narrowboat
£600 (1909), a horse boat £190 (1912) and a sailing barge £1,895 (1906), giving £7-32 per ton of
capacity by engine type. No annual repair figure for a carrying boat.
`[LITERATURE: research pass 25; canal company records]`

**Aircraft — Fair (purchase), Poor (maintenance).** The workbook fits a hedonic purchase surface
on 116 measured aircraft, 1936-2015: seats^0.867 × engines^0.768 × engine type × wide-body ×
1.0111^(year-1959), R² 0.948. Pressurisation and swept wing are not identifiable in that sample and
are not applied. Maintenance evidence is engineering cost per flying hour (1969/70, 1972/73),
IATA benchmarks and check intervals; it does not support a maintenance ladder. The earlier
statement that aircraft costs must not be calibrated from the forum evidence applies to that
three-point set, which the hedonic sample replaces. `[LITERATURE: research pass 18; aircraft
price survey 1959]`

**Horses and horse vehicles — Good (keep), Poor (purchase).** Itemised London keep accounts 1876-97:
about £45 a year, range £28-60, excluding the horsekeeper's wages; the shape of the cost (low
`cost`, high `fixed_cost`) is well evidenced. Purchase prices exist only in `Horses cost table.ods`;
nothing before 1830 outside one coach account.

**Narrow-gauge, monorail, maglev vehicles — None.** No measured British vehicle costs; the narrow
gauge forge basis is terrain, not gauge.

**Vehicle overhauls and upgrades — Fair (rail), Poor (everything else).** Until 2026-11-23 only
nine of the pakset's 3,539 vehicles carried any overhaul field, and 403 carried an
`upgrade_price`, most of them the token 5000. The two passes now give measured intervals and cost
shares. Rail: steam general repairs at 104,000-196,000 miles, a GWR 28xx heavy general of £450-700
against a £4,992 build, BR's 2.75/5.5/11-year diesel overhauls, a two-year carriage cycle.
Road: a four-year bus overhaul of about 220,000 km at £2,000 a bus in 1965 (25-33% of a new
double-decker), lorry engine cycles at 50,000-100,000 miles, and a 1955 lorry overhaul of £280 at
100,000 miles. Trams: Metrolink's 12-year mid-life at £80,000 and Supertram's 32-34-year life
extension at £856,000. Ships and aircraft: five-year surveys and C/D checks at 2-5% of new value.
Upgrades: measured rebuilds at 20-50% of a new vehicle (Class 47-to-57, Class 321 Renatus, Mk3
sliding-door conversion, steam reboilering, the Leyland National Greenway). Gaps: no measured
wagon overhaul price in any era, no per-overhaul money for a BR diesel or electric locomotive, no
measured historic municipal tramcar overhaul, and no pre-2009 ship or pre-2000 aircraft cost series.

**`.dat` comments — Fair, as a supplementary channel.** The pakset authors wrote historical
notes into the `.dat` files: 25,113 comment lines across 2,664 files. Of 1,022 vehicle comments
with a qualitative judgement, 80 made a comparative claim worth an adjustment, and 26 rows were
accepted into `vehicle-adjustments.csv` at the 5-15 per cent band. The channel ranks below
literature — 20 claims cite a source, 60 are the authors' own assertions — and it must be read
with two rules: a fuel-economy claim belongs to `fuel_per_km`, not to the cost fields, and a
comment that states a price is an individual price rather than an adjustment. The comments also
hold 76 price statements, which are being parsed into the register separately.
[vehicle-cost-method](vehicle-cost-method.md) "Comment-derived adjustments".
[vehicle-cost-model](vehicle-cost-model.md) "Overhauls and upgrades".

## Ways and structures

**Rail ways — Good.** Permanent way installed £1,300-1,900/km roughly flat 1830-1900 (L&M 1830,
Leicester 1877, Leeds 1881, Dewsbury 1881-82, Mills c.1898); a rail-weight materials ladder; whole
line capital strikingly flat at £20,300-22,400/km 1858-1902 (the single most useful anchor), with the
1858 component split (6% parliamentary, 18% land, 66% works, 10% rolling stock); maintenance and
renewal separately documented (relaying 50-60% of new). Gaps: permanent way 1900-1930 and after 1945;
the capital-to-maintenance target ratio for a bare way is not established (Acworth's 72.7 years is a
whole railway).

**Road ways — Good.** Turnpike construction and upkeep 1819-23, Telford/McAdam new roads, 1880
upkeep, tarmac and tarred slag rates 1906-11, modern asphalt £/m2, motorway 2005 and 2011 (the 2011
yard rate is the decisive check: the pakset motorway is 2.5 times too cheap). Urban-vs-rural factors
documented. Gap: no road construction cost from before 1950 from a historical source.

**Canal ways — Good.** Construction per km by canal class (£1,850-5,560 narrow and barge; £14,750-
33,000 ship; £272,000 large ship); seven named canals 1724-1905; the itemised Leeds & Liverpool 1776
estimate; lock prices by class and per foot of fall; routine maintenance £62/km/year. Caution: the
pakset's canal way object and forge meanings are reversed (conflict 7).

**Tram ways — Fair.** Track laid £600/mile 1911 (excluding electrification); line equipment
maintenance and renewal £58/km/year 1930-31; a defensible street-reservation forge basis. The
rail-vs-tram forge differential in the present data is wrong (conflict 4).

**Narrow-gauge, monorail, maglev ways — Poor/None.** Forge derivations only (£250-620/km narrow,
terrain-dominated; monorail and maglev explicitly without British historical basis).

**Bridges and viaducts — Good (ladder), Fair (parameters).** Per-metre ladders by construction
(masonry and brick £55-160/m; iron trestles £48-280/m by span and pier height; tubular and major
river £337-1,321/m; major crossings about 10x an ordinary underbridge, confirmed independently
1832); 25 named viaducts 1828-1978 normalised to 1900; Cudworth's eighteen-year NER maintenance
accounts giving maintenance relative to plain line (brick 0.25-0.5x, iron 1.2-1.5x, timber 7-8x).
Gaps: cost by height cannot be separated; the present data treats all brick viaducts alike and
reverses masonry against history; the 2022 note conflicts with present data by two orders of
magnitude (conflict 1).

**Tunnels — Good.** Ordinary double-track bored £45-145/m; 1830s named tunnels £22-113/m; hard ground
2-3x; cut-and-cover £120-170/m; deep tube per bore £25-61/m; 21 named tunnels 1779-1962 in the forum
table. Two table artefacts recorded (Primrose Hill length; Islington canal tunnel conflict).

**Piers, docks, quays — Fair.** Per-metre ladder by construction (timber wharf £18/m to Admiralty
breakwater £1,061/m); Margate-type landing stage 1853; the Tilbury works itemisations. No wharf cost
per unit of berth; no measured dock/pier maintenance account (heuristic 0.8-4% a year).

**Signals and signalboxes — Fair.** 1912 post prices by height complete with arm, lamp and wire;
1909 automatic signal £97-100 an arm; interlocking and lever costs 1873-84; Spetisbury 1901 and
other named boxes; the 15-20 fold real increase from mechanical to colour light ("the most important
fact in this domain"); per-route-km signalling £315 mechanical to £5,200 Kent Coast. Unresolved: what
one signal object represents (a block section, not an arm); the 168 signal objects differ 178x within
one era and method.

**Roadsigns — None.**

**Way objects (electrification) — Good.** Southern third rail 1925 £3,825/track-km; the clean 1955
BR pair at about £100,000-102,000 a route mile for overhead AC and third-rail DC; modern overhead
£6,100-8,100/track-km simple rising to £20,300 on troubled schemes; renewal intervals and
percentages by component; tramway line equipment £58/km/year. Weaknesses: no track count for the
1955 schemes; the pakset's era order is reversed.

**Crossings (level) — None.**

## Buildings and stations

**Stations, platforms, shelters, bus stops — Good.** Platform per metre of face by construction
(timber £2-4, brick £4-8, concrete £5-10 at 1900 prices) with maintenance as a share of capital
measured (timber 4-8%, brick 0.8-1.5%); canopies and roofs per square; shelters 1902-61; bus stop
pole and flag £300-500 to modern shelter £7,000-12,000; 25 named station projects 1851-1984.
Conflicts: station maintenance at 15-30% of capital a month against a defensible 10% a year
(conflict 2); which Tilbury 1906 items are station cost unresolved; no goods shed priced apart.

**Depots — Fair.** Eight named sheds 1851-1969 (each a different building, no series); the class
carries no cost line in the present settings. No measured depot maintenance figure (present
maintenance is too low where most things are too high, conflict 6).

**Headquarters — Fair (standing charge), Poor (building).** The administrative overhead is well
bracketed (3.3-5.8% of receipts across six undertakings 1838-1958, about £175 per route km a year).
The building cost itself could not be established from any free source; near anchors only (Derby
offices and works 1839, training college 1937, US office block 1882).

**Airports — Good (modern), Poor (historic).** Runways by pavement strength (£69-189/m2), terminals
and hangars per m2, control towers £2.3m-£50m, the wartime airfield programme, maintenance 1.6-2.4%
of capital a year and overlay cycles; formation £6,000-9,000/km as the air forge basis. No measured
pre-1950 figure; the pre-1950 method is to deflate modern £/m2 on the `buildings` index.

**Industry buildings — None.** **City buildings — None** (the forum holds no pre-1845 building prices
at all). **Trees — None. Ground objects, fences — None.**

**Power lines — Fair.** Two anchors (275 kV lattice £15,535/km 1959; £1.6m/km 2015; maintenance
about £650/km/year); no pre-1959 figure. **Transformers — None** as such.

## Land and engine-charged actions

**Land purchase — Fair (index series, no per-item data).** Country land from the Savills farmland
series; city land from a house-price proxy and ONS land values; the 1900 anchors provisional against
the `meters_per_tile` scaling (open).

**Land alteration (raise/lower land, cuttings, embankments) — Fair.** Formation £110-400/km;
earthwork rates 9d-1s 3d a cubic yard by lead distance and depth (Grand Junction contracts, Tring);
the L&M 1830 component account; a derived continuous-cutting table by depth and track count.
"Earthworks per km for a stated cross-section" is not established: the table rests on assumed slopes.

**Tree removal — None. Building and field removal — None.** Engine key coverage exists
([prices-infrastructure](prices-infrastructure.md) "Maintenance and landscaping") but no measured
figure for any removal operation.

**Forge costs — Good (rail), Fair (tram, water, air), Poor (narrow, monorail, maglev).** Formation
and minor earthworks £110/km (1803) to £250-400/km typical (1855-1900) as the rail basis; each other
way class has a derived basis recorded in
[infrastructure-cost-synthesis](infrastructure-cost-synthesis.md) §5.

**Engine finance settings (`cost_depot_*`, `cst_*`) — Poor.** Derivable from the per-action structure
ladders (building removal, transformer, found city/industry) but no measured figure is recorded per
action; unscaled by length and adjusted only by inflation.

## Config-driven costs (for completeness)

**Fuel — Good (series), Fair (basis).** Long coal series from the 1750s; oil, electricity and jet
1900-2026. Open: the `fuel[steam]` unit question (M3); no delivered-to-depot coal price.
**Crew wages — Good (1907, 1956-62, modern), Poor (before 1901, 1908-55).** Gaps recorded in
[staff-wages](staff-wages.md). **Revenue rates — Good** (statutory schedules and charged-rate series;
see [goods-rate-evidence](goods-rate-evidence.md)).

## Cross-cutting weaknesses

1. The conversion chain is settled but the maintenance display confirmation (M1) and the per-month
   rate question (M2) remain open ([balance-synthesis](balance-synthesis.md)).
2. Two-thirds of the whole-line capital comparison is composition the rural test line does not carry
   (urban land, tunnels, viaducts, terminals, multiple track).
3. Classes rated None account for a large share of the object count (signals aside): roadsigns,
   crossings, trees, ground objects, industry and city buildings, transformers, removal actions.
   For these the workbooks can record only in-game costs and derivations from neighbouring classes,
   clearly labelled as such.

## Open questions

- For the None-rated classes, is derivation from neighbouring-class ladders (for example city
  buildings from the station-building ladder) acceptable for balancing, or must they wait for
  measured sources?
- Should rating thresholds be numeric (years covered, number of points) rather than judgement?
