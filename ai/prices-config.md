---
status: draft
verified: New ex-15 @ b39ac938d (working tree); simutrans-extended ex-15 @ 22cc3af
---
# Prices config

**Covers**: `New/config/prices.tab`: the price types, the year-index method, the unit
conversion, and the research required for each type that has no series of its own.

## Mechanism

- The engine multiplies a base price by index divided by 100, so an index of 100 leaves the
  price unchanged. Between listed years the index is interpolated linearly; before the first
  year the first value applies; after the last year the last value applies. With the timeline
  off, base prices are returned unadjusted. A type with no entry falls back to `general`.
  Engine mechanism and coverage: [balancing](balancing.md#inflation-recording-ex-15).
- `prices.tab` holds one line per type as `key=year,index,year,index,...`.
  `[CODE New ex-15 @ 8d0603d81]`
- Base prices in `.dat` files and in the finance settings of `simuconf.tab` are in 1900
  terms, and 1900 is 100 by construction. `[CODE New ex-15 @ 8d0603d81]`

## Types and state

Eight types have a series of their own: `general`, `passenger fare`, `mail rate`,
`corporation tax`, `base rate`, `city land`, `country land` and `buildings`. The remaining
four are present only as commented-out placeholders and therefore use `general`:

- `goods rate`
- `vehicle purchase`
- `vehicle maintenance`
- `infrastructure`

`[CODE New ex-15 @ 8d0603d81]`; `buildings` added 2026-11-15.

The placeholders are flat at index 100. Do not uncomment one without a real series: that would
remove inflation from the category entirely, which is a larger error than inheriting `general`.
The `infrastructure` series has been researched and is ready to insert; it is not in the file
yet.

`corporation tax` and `base rate` are rates, not index numbers. Their entries are percentages
used as rates rather than as multipliers on a base price; confirm this against the engine.

## Engine change: land base split

- The engine reads `cost_buy_land` for country land and `cost_buy_city_land` for land inside
  towns; the C++ fields are `cst_buy_land` and `cst_buy_city_land`. Inside a town the city
  base is multiplied by 6 (capital), 4 (city) or 3 (town) before applying the `city land`
  index; outside a town the `country land` index applies with no multiplier. The same
  multiplied city base feeds the wayleave deduction on elevated or underground ways.
  `[CODE simutrans-extended ex-15 @ 0d41455e]`
- The city land cost is stored in saves from Extended 15.15. Older saves load with the city
  cost equal to the country cost, and a pakset that sets only `cost_buy_land` mirrors it into
  the city cost. `[CODE simutrans-extended ex-15 @ 0d41455e]`
- `simuconf.tab` carries `cost_buy_land=1500` and `cost_buy_city_land=2625`. The city base is
  set for a reference multiplier of 4: 1500 × 7 ÷ 4 = 2625. With the capital/city/town
  multipliers of 6/4/3, the 1900 urban/farmland ratio is about 10.5:1 for a capital, 7:1 for
  a city and 5.25:1 for a town. Both price types stay at the 1900=100 convention.
  `[USER-DIRECTION:2026-11-15]`
- The value 2625 assumes the multipliers remain and are applied to `cost_buy_city_land`. If
  they are removed, the city base must be 10500 instead. Both values are provisional against
  the `meters_per_tile` scaling and the per-tile land model. Do not change either 1900 anchor
  while the per-tile land model is outstanding. `[USER-DIRECTION:2026-11-15]`

## Unit conversion

The pakset uses two conversion rates because the engine has two timescales.

- Revenue (short timescale): 1 SimuCent = £0.005208 in 1900 = 1.25 old pence = 0.5208 new
  pence. 80 units = 1d; 192 units = 1 new penny; £1 = 19,200 units.
- Capital and annualised costs (long timescale): the `Currency conversion` sheet of
  `New/Infrastructure balancing calibration-2.ods` gives 1 SimuCent = £0.396 in 1900.
  `[CODE New ex-15 @ 8d0603d81]`

The index itself is unitless, so the same percentage applies to both timescales. The
conversion rates are for sanity checks: index divided by 100, multiplied by the relevant
rate and the real price for a year, should reproduce the entered value.

## Authoring a series

1. Choose a nominal price series for the class of thing the price type covers.
2. Index equals price(year) divided by price(1900), multiplied by 100.
3. Where the source starts after 1750, extend backwards by holding the real level constant:
   index(year) equals `general`(year) divided by `general`(1900), multiplied by 100.
4. Where the source ends before 2050, extend forwards by holding the real level constant:
   index(year) equals the last index multiplied by `general`(year) divided by
   `general`(last year).
5. Keep both ends of a plateau; drop only interior repeats. A plateau needs its first and
   last points or linear interpolation cuts the corner.
6. Add a `Last updated:` line and name the source, the base year and the transformations in
   the comment ([calibration-sources](calibration-sources.md)).
7. Check the structure: pair count, ascending years, no duplicate years, integers only, and
   no redundant same-value entries.
8. Check the result against a second source at several dates. A block that changes basis
   mid-series produces a step that is not in the historical record; divide by a known real
   price for several years to test it.

## What each outstanding type needs

| Type | What the engine scales | Series required | Main source route |
|---|---|---|---|
| `vehicle purchase` | Vehicle purchase and upgrade costs | Price index of transport equipment | ONS CPI D7CO and CPIH L544 for 1988-2026; a transport equipment deflator or historical price lists before 1988 |
| `vehicle maintenance` | Vehicle running and fixed costs | Repair and servicing price index | ONS RPI DOCT and CPI repair components for 1987-2026; wage and parts indices before 1987 |
| `infrastructure` | Ways, bridges, tunnels, piers, way objects, signals, roadsigns, their maintenance, the forge costs and the halt multipliers | Civil engineering construction cost index | ONS output price index for infrastructure from 1980, chained through three vintages; `buildings` before 1980 (see [prices-infrastructure](prices-infrastructure.md)) |
| `goods rate` | Goods revenue | Rail freight revenue per ton-mile | Railway Returns 1848-1962; British Rail and GBR statistics 1948-1994; ORR statistics 1994-2026 |

## Access

- Free to use: ONS time series and methodology, ORR statistics, GERS handbooks, Savills and
  Knight Frank reports, RICS/RAU summaries, the JST Macrohistory Database, and digitised
  Railway Returns.
- Paywalled or print: Spon's handbook, the BCIS index series, and Feinstein's national accounts
  tables. These need a library or a subscription; record the edition and table used.
- The Bank of England workbook "A millennium of macroeconomic data for the UK" carries long
  annual series that would otherwise need print sources, including the Mitchell building-cost
  index 1845-1938 and Holmans's construction-cost index from 1939 (sheet A32).
  `[LITERATURE:https://www.bankofengland.co.uk/statistics/research-datasets]`
- For era-relative prices, which a year index cannot supply, start from the forum thread
  "A snippet of relative pricing information" ([research-and-forum](research-and-forum.md));
  what it holds for buildings: [prices-forum-fragments](prices-forum-fragments.md).

## Type notes

### `vehicle purchase`

- The engine has one key for every vehicle type. The index is therefore a compromise between
  cars, lorries, buses, locomotives, ships and aircraft, whose real prices moved differently.
  A car-only series must not be applied without checking its effect on rail, sea and air
  vehicles.
- ONS CPI 07.1 Purchase of vehicles (series D7CO, 2015 = 100) is annual from 1988; CPIH 07.1.1A
  New cars (series L544, 2015 = 100) is the narrower alternative.
  `[LITERATURE:https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7co/mm23]`
  `[LITERATURE:https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l544/mm23]`
- For 1900-1988, use the national accounts deflator for transport equipment, linked to
  Feinstein's investment goods price index, and cross-check against the historical purchase
  prices in `New/Vehicle cost table.ods` and the `Vehicles (historical)` sheet of
  `New/Infrastructure balancing calibration-2.ods`.
- This is the only series expected to fall in real terms over most of the period.
- The `.dat` purchase costs are a constant multiple of the real 1900 SimuCent cost in the
  vehicles the `Vehicles (historical)` sheet lists (the ratio there is about eight). The index
  must preserve the relative change only; it must not be used to rescale the `.dat` level.

### `vehicle maintenance`

- Covers repairs, overhaul and consumables. Fuel is priced separately in `fuel.tab`; crew is
  priced in `staff.tab`.
- ONS RPI motoring expenditure: maintenance of motor vehicles (series DOCT, January 1987 = 100)
  is annual from 1987; CPI maintenance and repair components are annual from 1988.
  `[LITERATURE:https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/doct/mm23]`
- Before 1987, use railway repair cost per mile from the Railway Returns and British Rail
  statistics, and road vehicle repair cost data, or construct a weighted index of wages and
  parts prices.
- The mix differs by mode. A single index cannot represent a steam locomotive overhaul and a
  bus service at the same time; choose the index that is defensible for the majority of
  vehicles in each era.
- This series is expected to diverge least from `general`. If the result stays close to
  `general` across the game's era, leaving the type on the fallback is preferable to adding a
  fragile series.

### `buildings`

- Implemented in `prices.tab`. The engine applies this key to building purchase and maintenance
  cost, and to the depot, headquarters, found city, found industry, building removal, field
  removal and transformer costs and the transformer maintenance. A halt building with an
  explicit `cost=` or `station_price=` is also priced through this key.
  `[CODE simutrans-extended ex-15 @ 22cc3af]`
- The station, dock, roadstop, air terminal and post office multipliers do **not** follow this
  key; they follow `infrastructure`. The engine mapping recorded here before the series was
  built said that every `cst_*` multiplier follows `buildings`, and that was wrong: the mapping
  is the same at `d4893f3` and at `22cc3af`, so it was misread rather than changed.
  `[CODE simutrans-extended ex-15 @ 22cc3af]`
- The series is a four-block chain, each block linked on an overlap period and the whole rebased
  to 1900 = 100:
  - **1845-1938**: Mitchell, *British Historical Statistics* (1988) ch VII table 8, building
    costs, 1930 = 100, in sheet A32 column S of the Bank of England "A millennium of
    macroeconomic data" workbook.
  - **1939-1954**: Holmans, *Historical Statistics of Housing in Britain* table M.10,
    construction costs, 1958-60 = 100, in the same sheet, column T; 1940-1947, which that sheet
    omits, from Mitchell and Deane, *Abstract of British Historical Statistics* (1962) ch IX
    table 4.
  - **1955-2013**: BIS output price index, all new construction, 2005 = 100, BIS quarterly price
    and cost indices 2014 Q1, table 1; 2013 is the mean of the four published quarters.
  - **2014-2026**: ONS construction output price index, all new work, 2015 = 100, annual means of
    the monthly series; 2026 is the mean of January to September.
- Link periods: 1938/1939 by continuity, following the join the Bank of England sheet makes (the
  implied 1938 value in the Holmans base is 29.0 against a published 1939 value of 29, so the
  join adds no step); 1955 on the Holmans-BIS overlap; 2014 Q1 on the BIS-ONS overlap.
- Before 1845 the block is a backcast that holds the 1845 real level and tracks `general`. That
  is a tested choice, not a default. The obvious alternative is a wage series: the same workbook
  carries Clark's building craftsmen's money wage for England (sheet A47), overlapping the
  Mitchell index 1845-1914. Fitting a blend of w times the wage ratio and (1 - w) times the
  price ratio to the Mitchell index gives a best fit at w = 0.02 (log RMSE 0.052); w = 0.5 gives
  0.231 and w = 1 gives 0.407. Money wages rose 82% between 1845 and 1900 while the index rose
  10% with prices flat, so a wage-based backcast contradicts the best-documented period and
  ignores the fall in unit labour input. No free pre-1845 building cost series was found; the
  remaining candidates are print or paywalled: Chalklin's building-cost appendix, the London
  *Builder's Price Books* of 1776-1796, and Spon's.
  `[LITERATURE:https://www.bankofengland.co.uk/statistics/research-datasets]`
  `[USER-DIRECTION:2026-11-15]`
- Results: 1845 = 91, 1900 = 100, 1920 = 302, 1955 = 571, 1980 = 4,462, 2026 = 22,040 and
  2050 = 36,854. The 2026 level is 1.35 times `general`; the ratio ranges from about 0.8 (1847)
  to about 1.6 (1980). `[CODE New 2026-11-15]`
- Traps: the blocks measure slightly different things — the Mitchell and Holmans indices are cost
  indices, the BIS and ONS series are output prices paid by clients. Tender prices are not input
  costs; specifications and quality change; VAT replaced purchase tax in 1973. Repair and
  maintenance prices are not spliced in, although the engine applies the same key to
  maintenance, which is more labour-intensive. `[LITERATURE:https://doi.org/10.4324/9780203473283]`

### `infrastructure`

- Researched and ready to implement; not yet in `prices.tab`, so the type still uses `general`.
  Read [prices-infrastructure](prices-infrastructure.md) when building, reviewing or inserting
  this series: the engine coverage verified against the source, the three published vintages,
  the link factors and the treatment of the period before 1980.
- The key covers ways, bridges, tunnels, piers, way objects, signals and roadsigns, their
  maintenance, the `forge_cost_*` settings, and the station, dock, roadstop, air terminal and
  post office multipliers. `[CODE simutrans-extended ex-15 @ 22cc3af]`
- The official series is the ONS output price index for new work: infrastructure, which measures
  roads and bridges and starts in 1980. No free civil engineering series reaches back further;
  the forum's individual structure prices were tested as a substitute and cannot carry an index.
- The `Infrastructure capital costs (historical)` sheet of
  `New/Infrastructure balancing calibration-2.ods` holds project costs at specific dates
  (ship canal 1724 to motorway 2011) normalised to 1900. It is a calibration workbook, not a
  price index, and must not be used as one.

### `city land`

- Implemented in `prices.tab`. Covers land purchase inside town boundaries; confirm the
  boundary rule against the engine.
- 1900-1995 uses the JST Macrohistory Database UK nominal house price index (`hpnom`) as a
  land-price proxy. The series is UK-specific, starts in 1899, and has a gap for 1939-1945
  which is interpolated. `[LITERATURE:https://www.macrohistory.net/database/]`
- 1995-2025 uses the ONS series "Land underlying dwellings" (AN.21111, current prices).
  `[LITERATURE:https://www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/adhocs/3709-landunderlyingcultivationbuildingsandstructuresestimatesfrom1995to2025]`
- The series is an average urban land price. The engine applies its own ×3 (town), ×4 (city)
  and ×6 (capital) multipliers to the base, so `cost_buy_city_land` is set for the ×4 city
  reference; see the engine change section.
- Before 1900 the 1900 real level is held. After 2025 the 2025 real level is held and grown
  with `general` to 2050.
- Traps: the pre-1995 section assumes land prices moved with house prices; the ONS series is
  a total value, not a value per dwelling, so the 1995-2025 growth includes the increase in
  the dwelling stock. Both are first-pass limitations until the per-tile land model replaces
  the index. No United States or other-country land data is used.

### `country land`

- Implemented in `prices.tab`. Covers land purchase outside town boundaries.
- 1900-2024 uses the Savills England farmland series, all land types, from the chart data
  embedded on the Savills rural land values page. The source values are real, rebased to
  2023; they are converted to nominal with `general` and indexed to 1900.
  `[LITERATURE:https://www.savills.co.uk/landing-pages/rural-land-values.aspx]`
- Before 1900 the 1900 real level is held. After 2024 the 2024 real level is held and grown
  with `general` to 2050.
- Savills reports nominal growth of 5.7% a year over the past century and real growth of just
  under 2% a year; the implemented index sits at about 2.6 times `general` in 2026.
- Traps: the series is England, not the whole United Kingdom; the source is a chain of
  several surveys and may contain splice steps (1959-1960 and 1963-1964 are visible in the
  data); holding the real level flat before 1900 misses the Napoleonic and mid-Victorian
  movements.

### `goods rate`

- Covers goods revenue. The base rates in the `goods-128.dat` header come from Ackworth and
  the Railway Clearing House for the 1840s to the 1890s; they are the early anchor, not a
  continuous series.
- Build average revenue per ton-mile from the Railway Returns (1848-1962), British Rail and
  GBR annual statistics (1948-1994; the GERS handbook tabulates freight receipts and net
  ton-miles) and ORR freight statistics (1994-2026).
  `[LITERATURE:http://hdl.handle.net/2027/umn.31951p01072589t]`
  `[LITERATURE:https://gersociety.org.uk/images/stories/emporium/RH102_contents.pdf]`
- Convert miles to kilometres: one ton-mile equals 1.60934 tonne-kilometres. Record which
  definition each source uses.
- Traps: the average is affected by the mix of high-value and bulk goods and by average haul
  length; rates were regulated before the 1950s and the basis changed at nationalisation
  (1948) and privatisation (1994). A block that changes basis mid-series must be linked on an
  overlap year.
- Before 1848, use canal and turnpike rates if a series can be found; otherwise hold the real
  level constant.

## Order of work

1. `infrastructure`. Researched; the series and its method are set out in
   [prices-infrastructure](prices-infrastructure.md) and only the insertion into `prices.tab`
   remains.
2. `vehicle purchase`. The CPI tail is ready; the early part needs a transport equipment
   deflator.
3. `vehicle maintenance`. The CPI and RPI tails are ready; the early part can be proxied from
   wages and parts.
4. `goods rate`. The longest splice and the weakest source continuity; do it last.

`buildings` and the land pair (`city land`, `country land`) are implemented. The land pair will
be revisited when the engine models land value per tile.

## Open questions

- Confirm from the engine source which `.dat` fields each price type scales, especially the
  split between vehicle purchase and vehicle maintenance.
- Confirm that `city land` applies inside town boundaries and `country land` outside.
- Confirm the `meters_per_tile` scaling of `cost_buy_land` and `cost_buy_city_land` before
  the per-tile land model replaces the index. The base split carries the 1900 urban/farmland
  ratio; the absolute land levels still depend on that scaling.
