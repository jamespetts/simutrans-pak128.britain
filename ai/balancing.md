---
status: draft
verified: New ex-15 @ 8d0603d81 (working tree)
---
# Balancing

**Covers**: prices, costs, capacities, speeds, and intro/retire dates, and how they are chosen to
be economically and historically realistic.

## Notes

- Balancing is a stated long-term priority, and the ex-15 engine work is critical for balancing
  to work ([../../AGENTS.md](../../AGENTS.md)). Read this doc before tuning any value, and read
  [high-level-design-goals](high-level-design-goals.md) first.
- Passenger, mail and accommodation classes: [class](class.md).
- Year-indexed prices: `config/prices.tab`, its price types and the research still outstanding
  for them: [prices-config](prices-config.md).
- Source-recording rule for every historically derived value: [calibration-sources](calibration-sources.md).
- Private-car colours and their relative `DistributionWeight` split: [objects/citycar](objects/citycar.md#colour-rule).
- The main source of pricing information is the forum thread "A snippet of relative pricing
  information": https://forum.simutrans.com/index.php/topic,6521.0.html
   `[FORUM:https://forum.simutrans.com/index.php/topic,6521.0.html]`. It collects historical British
   transport costs and prices, including vehicle purchase prices and related data.

## Cost balancing project

- Forum thread "Cost balancing - the great project" on the Pak128.Britain-Ex board, started
  January 2022: https://forum.simutrans.com/index.php/topic,21310.0.html
  `[FORUM:https://forum.simutrans.com/index.php/topic,21310.0.html]`. It records the calibration
  method and the interim findings.
- Calibration: all figures are normalised to the year 1900. General inflation uses the Bank of
  England inflation calculator; labour costs use measuringworth, which separates average
  earnings. The SimuCent to GBP conversion comes from passenger revenue: the `.dat` figure of
  0.50 cents per kilometre (second fare stage) represents 1d per mile, the third-class maximum
  prescribed by the Regulation of the Railways Act 1844. Per-kilometre costs use the short
  timescale and capital or annual costs use the long timescale; the day counts as 16 active
  hours. `[FORUM:https://forum.simutrans.com/index.php/topic,21310.0.html]`
- Interim findings: infrastructure capital and maintenance costs are broadly realistic except
  that bridges are far too cheap and the rail forge cost is too high; operating costs are too
  low relative to revenue; passenger revenue is possibly overstated, with roughly halved fares
  proposed for the 1900 calibration. `[FORUM:https://forum.simutrans.com/index.php/topic,21310.0.html]`
- Interim stance: where simulating features do not yet exist (inflation, vehicle wear and
  overhauls), balance errs on the side of being generous to the player, with more detail added
  as the feature set permits. `[FORUM:https://forum.simutrans.com/index.php/topic,21310.0.html]`
- Much of the full balancing work described in the thread is still in the future for the ex-15
  engine version. `[RECOLLECTION:2026-09-19]`
- The vehicle cost balancing in the project takes effect only after ex-15 with its inflation
  feature; without year-indexed price adjustment, the calibrated vehicle figures cannot apply.
  `[RECOLLECTION:2026-09-19]`

## Inflation recording (ex-15)

- Engine mechanism: `karte_t::get_inflation_adjusted_price` multiplies a base `.dat` price by a
  year-indexed factor: adjusted price equals base price times index divided by 100, so an index
  of 100 leaves prices unchanged. Between listed years the index is linearly interpolated; past
  the last year the last index applies, before the first year the first index applies. Where a
  price type has no table, the `general` table is used. With the timeline off, base prices are
  returned unadjusted. `[CODE simutrans-extended ex-15 @ d4893f3]`
- Pakset record: `config/prices.tab` in the pakset directory. It holds one line per price type
  with year and index pairs in increasing year order. The engine loads it in `prices_init` and
  reports ill-formed lines, falling back to defaults for that type.
  `[CODE simutrans-extended ex-15 @ d4893f3]`
- Price type keys, 12 in total: `general`, `passenger fare`, `mail rate`, `goods rate`,
  `vehicle purchase`, `vehicle maintenance`, `buildings`, `infrastructure`, `city land`,
  `country land`, `corporation tax`, `base rate`.
  `[CODE simutrans-extended ex-15 @ d4893f3]`
- Coverage: vehicle purchase, running, fixed and upgrade costs; passenger, mail and goods fares;
  way, bridge, tunnel, signal, roadsign and way-object construction and maintenance; buildings,
  depots and stations; the `cst_*` construction-cost settings (dock, station, roadstop,
  airterminal, post, headquarters, depot, land alteration, tree removal, building removal and
  transformer multipliers); corporation tax; land values; and overdraft
  interest via `base rate`. `[CODE simutrans-extended ex-15 @ d4893f3]`
- Savegames: the price tables are stored in saves on extended version 15 and above, and the
  pakset-directory file is re-read on load. `[CODE simutrans-extended ex-15 @ d4893f3]`
- Fuel and staff sit outside this file: absolute yearly prices per fuel and engine type live in
  `fuel.tab`, and yearly wages per staff type in `staff.tab`.
  `[CODE simutrans-extended ex-15 @ d4893f3]`
- Units: 1 SimuCent = £0.005208 in 1900 on the revenue timescale, and £0.396 in 1900 on the
  capital timescale; 192 revenue units = 1 new penny. The index is unitless, so the same
  percentage applies to both. Method and conversions: [prices-config](prices-config.md).
  `[CODE New ex-15 @ 8d0603d81]`
- No in-game display currently reads these tables; the planned display of price factors over
  time is outstanding.
  `[FORUM:https://forum.simutrans.com/index.php/topic,22054.msg202141.html]`
- Pakset status: `New/config/` contains `prices.tab`, `fuel.tab` and `staff.tab`, with series
  running to 2026 and projections to 2050. `general`, `passenger fare`, `mail rate`,
  `corporation tax`, `base rate`, `city land` and `country land` have their own series; five
  types still fall back to `general`. [prices-config](prices-config.md) records the method and
  the research outstanding for those five. `[CODE New ex-15 @ 8d0603d81]`

## Time system and the two timescales

- There are two separate measures of time: (1) the measure by which km/h is measured, expanded
  in Extended to journey and waiting times used in routing; (2) the measure by which months and
  years are measured. Monthly items are adjusted by the `bits_per_month` setting so that
  outcomes are functionally equivalent whatever the month length; `meters_per_tile` applies
  equivalent normalisation so that movement code and displayed vehicle speed are unchanged
  across settings.
  `[FORUM:https://forum.simutrans.com/index.php/topic,7735.msg73543.html#msg73543]`
- Short timescale: per-kilometre revenues and costs. Long timescale: capital costs and
  per-month or per-annum costs. A game month lasts about 6.4 hours; the day counts 16 active
  hours after 8 hours of sleep or inactivity.
  `[FORUM:https://forum.simutrans.com/index.php/topic,21310.0.html]`
- Pakset records in `New/config/simuconf.tab`: `base_meters_per_tile = 1000` and
  `base_bits_per_month = 18` assume a Standard-based month length; `bits_per_month = 22`;
  `job_replenishment_per_hundredths_of_months = 375`, set so jobs
  replenish every 24 hours with a 6:24 month. `[CODE New master @ eff439751]`
- Pakset scale: 125 metres per tile (`meters_per_tile = 125` in `New/config/simuconf.tab`).
  Journey times, revenues, maintenance costs, comfort and catering values are all calculated
  from this scale. `[CODE New master @ eff439751]`

## Passenger and mail generation

- Passengers generate only from residential buildings, as commuting trips to buildings with
  jobs or visiting trips to buildings with visitor demand, with per-building class
  proportions. Travel happens only within journey time tolerance; unroutable passengers fall
  back to alternative destinations, scaled to jobs and visitor demand so the count scales with
  map size. `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`
- Rates in `New/config/simuconf.tab`: 3 trip attempts per 16-hour day per person gives 120,
  entered as `passenger_trips_per_month_hundredths = 156` to offset multithreading rounding;
  mail intended as 5, entered as `mail_packets_per_month_hundredths = 7`. Commuting chance is
  `commuting_trip_chance_percent = 20`, derived from 1 commuting attempt per day out of 3,
  times 5/7 days, times 60% in work, matching Department for Transport and Hertfordshire
  survey data cited in the file. `[CODE New master @ eff439751]`
- Calibration rule: compare trips generated per person per 6.4-hour month across all modes,
  including walking. Rail-only passenger counts are not a valid basis, as they depend on
  service levels and competing private cars. Earlier calibration discussion lives in threads
  9981, 10953, 12551, 17336 and 18423.
  `[FORUM:https://forum.simutrans.com/index.php/topic,21310.msg198373.html#msg198373]`
- Tolerances: commuting `min_commuting_tolerance = 30` with `range_commuting_tolerance = 180`;
  visiting `min_visiting_tolerance = 12` with `range_visiting_tolerance = 12000`; skewed
  distributions (`random_mode_commuting = 2`, `random_mode_visiting = 6`) and
  `tolerance_modifier_percentage = 66`. `[CODE New master @ eff439751]`

## Industry production

- Consumer industries, except power stations and zero-visitor-demand industries, consume goods
  in proportion to visiting passengers. Producing industries scale output to filled jobs: more
  than 20% unfilled posts reduce output proportionally, and 0% filled means no output.
  Consumer industries refuse visitors below 66% staffing. Staff are laid off without input
  goods, which stops commuting inflow until supply resumes. The percentages are set in
  `simuconf.tab`. `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`
- Pakset records in `New/config/simuconf.tab`: a new consumer industry per 2000 town
  population (`industry_increase_every = 2000`); `just_in_time = 4`, demanding stock to cover
  estimated time to next delivery; electricity supply at 1200 parts per thousand of demand
  (`electric_promille = 1200`); factory spacing minimum 2 tiles, maximum 100% of map size.
  `[CODE New master @ eff439751]`
- Density: new factories hold the industry-density-to-population ratio from game start, with
  per-factory density contributions set by pakset authors; the pakset uses this for UK
  industrial decline from the 1970s. Factories close within 30 years of their retirement date
  and chains relink or close, with upgrading where configured.
  `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`

## Town size and scaling

- Level abstraction: buildings carry a level converted for older or Standard-only data by
  `population_per_level = 4`, `visitor_demand_per_level = 4`, `jobs_per_level = 3`, and
  `mail_per_level = 1` in `New/config/simuconf.tab`. `[CODE New master @ eff439751]`
- Size bands: village below 2500, city above, capital above 25000
  (`city_threshold_size`, `capital_threshold_size`), overridden by relative shares
  (`city_threshold_percentage = 20`, `capital_threshold_percentage = 2`). Generation caps
  are `max_city_size = 100000` and `max_small_city_size = 50000`; growth divisors are
  `growthfactor_villages = 832`, `growthfactor_cities = 480`, `growthfactor_capitals = 120`,
  where lower means faster growth. `[CODE New master @ eff439751]`
- Placement: city sizes follow Zipf distribution, with clusters, low-ground preference, and
  river and sea preference; the distribution was reported broken circa 2017 with a fix pending
  a growth rewrite. Congestion at 100 or more stops a city growing.
  `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`
- `New/config/cityrules.tab` was adapted for the pakset in 2010, rebalanced in December 2018
  for the new passenger generation, and modified in December 2019 for the revised town growth
  system. `minimum_city_distance = 80`, noted in the file as 10 km at 125 m per tile.
  `[CODE New master @ eff439751]`

## Calibration working papers

- `New/` contains calibration spreadsheets used as working papers for balancing decisions. They
  are inputs, not canonical values; the canonical values live in the `.dat` files.
  `[CODE New master @ c842afdbd]`
- Vehicle purchase prices and operating physics: `Vehicle cost table.ods`,
  `Horses cost table.ods`, `steam-physics-calcs.ods`, `road-vehicle-physics-calibration.ods`,
  `Rolling resistance calcs.ods`, `Multiple unit TE extrapolation.ods`, `Track weights.ods`.
  `[CODE New master @ c842afdbd]`
- Interim vehicle balance: `Pak128 Britain - mod.xlsx` is reported to be the interim balancing
  spreadsheet for vehicles, attributed to neroden. `[RECOLLECTION:2026-09-19]`
- Passenger capacity and comfort: `Comfort calibration overview.ods` (sheets `Overview` and
  `All vehicles`), `Exp-Cater-Comfort-Capacity.ods`, `Passenger density calculations.ods`,
  `payload-tonnage-calcs.ods`, `stagecoach-passenger-calcs.ods`.
  `[CODE New master @ c842afdbd]`
- Infrastructure costs: `Infrastructure balancing calibration.ods`,
  `Infrastructure balancing calibration-2.ods` (calculation spreadsheet behind the thread tables;
  sheets include currency conversion, historical and Simutrans infrastructure costs, historical
  and Simutrans vehicles, wages, passenger fares, revenue ratios, and fuel price normalisation;
  one sheet links to the `Extrapolation` sheet of `steam-physics-calcs.ods`),
  `bridges-new.xls`,
  `road-bridges.xls`, `Tunnel cost research (PJMack).ods`, `ways-rail-balance-v1.ods`,
  `Wear calculations.ods`, `road-vehicle-wear-calcs.ods`. `[CODE New master @ c842afdbd]`
- Steam locomotive physics: `steam-physics-calcs.ods` (sheets `Hill (AEO)`, `Hill (Hood)`,
  `Extrapolation`, `Theoretical figures`). `[CODE New master @ c842afdbd]`
- Demand and wider economy: `Agricultural output calibration.ods`,
  `Population growth extrapolation.ods`, `Congestion index.ods`, `balancing.xls`,
  `new-balancing.xls`, `Simutrans Ship Balance.xlsx`. `[CODE New master @ c842afdbd]`
- The relationship between these working papers and the engine's economic simulation is not
  yet documented; see the open questions below.

## Editing `.ods` working papers programmatically

- The calibration `.ods` files must only ever be edited by byte-splicing `content.xml`, never
  by XML round-tripping; get the procedure right from the maintenance guide:
  [ods-editing](ods-editing.md). It covers the non-negotiable rules, the rescue path
  (`git -C New restore <file>`), inspection, sorted-position insertion, reference
  renumbering, re-zipping, and verification, with the working helper code.
  `[EXECUTION-VERIFIED:2026-09-23]`

## Planned sections

- The calibration method: what data sources are used and how values are derived.
- The relationship between pakset values and the engine's economic simulation.
- Vehicle operating costs, capacities, and weights.
- Infrastructure costs and maintenance.
- Historical price and wage data sources.

## Open questions

- What is the current, documented calibration method, and where does it live?
- Which engine fields must a balancing change touch together to stay coherent?
- Who authored `Pak128 Britain - mod.xlsx` and which vehicle classes does its interim balance
  cover?
- What yearly factors should `New/config/prices.tab` record per price type, and from which
  historical sources? The method and sources are recorded in [prices-config](prices-config.md)
  and [calibration-sources](calibration-sources.md); the remaining open points are the engine
  field mapping and the five unfinished series.
- Locate the board-75 thread "Recalibrating industry consumption and production" and integrate
  its conclusions on industry rates.
