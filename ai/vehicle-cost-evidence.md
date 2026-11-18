---
status: draft
verified: New ex-15 @ 8d0603d81; simutrans-extended ex-15 @ bdfdc8311
---
# Vehicle cost evidence

**Covers**: the measured purchase, build and maintenance costs of British transport vehicles, by
class and era, and what those figures can and cannot support when the pakset's vehicle costs are
re-examined.

Method: [vehicle-cost-method](vehicle-cost-method.md). Engine mechanics:
[vehicle-cost-model](vehicle-cost-model.md). Index series: [prices-config](prices-config.md).
This doc is evidence and analysis only. No `.dat` value has been changed, and none should be
until every cost domain has reached this depth. `[UiER-DIRECTION:2026-11-16]`

## The evidence base

| Document | Read when | Contents |
|---|---|---|
| [forum-prices-part-1](vehicle-cost/forum-prices-part-1.md) | you need a purchase price for a specific class or era | 208 rows from forum thread 6521, rows 1-208 |
| [forum-prices-part-2](vehicle-cost/forum-prices-part-2.md) | as above, later classes | 208 rows from the same thread, rows 209-416 |
| [published-capital](vehicle-cost/published-capital.md) | you need a price with a specification attached | 81 figures from company records, builder records, technical press and official returns, each with the specification the source states |
| [published-maintenance](vehicle-cost/published-maintenance.md) | you need a repair or running cost figure | 53 figures, each with its inclusion and exclusion stated |
| [index-sources-purchase-a](vehicle-cost/index-sources-purchase-a.md) | you are auditing the `vehicle purchase` series, 1988 onwards | ONi D7CO, L544 and DOCi, and Feinstein's railway rolling stock column, with annual values |
| [index-sources-purchase-b](vehicle-cost/index-sources-purchase-b.md) | as above, earlier and rejected series | Feinstein's ships, plant and machinery and capital goods columns, the iefton and Weale values, and the series checked and rejected |
| [index-sources-maintenance](vehicle-cost/index-sources-maintenance.md) | you are reconsidering the maintenance fallback | the repair and maintenance series available, with annual values, and why none carries the 1750-1987 span |
| [deflator-search](vehicle-cost/deflator-search.md) | you are questioning whether a published vehicle deflator exists | the search across national accounts vintages, and the alternatives tested and rejected |
| [deflator-series](vehicle-cost/deflator-series.md) | you are auditing the 1938-1997 block of the series | the Blue Book current and constant price series and the Feinstein bridge, with annual values |
| [base-maintenance](vehicle-cost/base-maintenance.md) | you need a maintenance level in engine units | the converted per-kilometre and per-vehicle-year figures, the maintenance-to-capital ratio, and the field mapping |
| [aircraft-maintenance](vehicle-cost/aircraft-maintenance.md) | you need an aircraft maintenance cost | British operator engineering cost per flying hour 1969-73, IATA benchmarks, check intervals |
| [road-maintenance-1959-2016](vehicle-cost/road-maintenance-1959-2016.md) | you need a road vehicle maintenance figure after 1958 | Commercial Motor tables 1963-74, Merseyside 1983, FTA 2016 |
| [modern-traction-multiple-units](vehicle-cost/modern-traction-multiple-units.md) | you need a multiple unit maintenance cost | RDG per vehicle-mile, London Underground per car-year, Civity per train-km |
| [modern-traction-locomotives-and-wagons](vehicle-cost/modern-traction-locomotives-and-wagons.md) | you need a post-1987 locomotive or a wagon figure | Class 66 and 47 rebuild costs, wagon routes and gaps, the scheduled/unscheduled question |
| [ship-maintenance](vehicle-cost/ship-maintenance.md) | you need a ship repair or dry-docking cost | 50 figures 1849-2026, dry-docking and survey costs |
| [inland-boat-maintenance](vehicle-cost/inland-boat-maintenance.md) | you need an inland boat repair cost | canal company repair jobs 1877-1928, modern narrowboats |
| [horse-keep-components](vehicle-cost/horse-keep-components.md) | you need a horse cost component | feed, farriery, veterinary, stabling, 1876-1897 London |
| [horse-keep-totals](vehicle-cost/horse-keep-totals.md) | you need a horse annual keep figure | totals, horsekeeper wages, working life and work done |
| [tram-maintenance](vehicle-cost/tram-maintenance.md) | you need a tram or light rail maintenance cost | Ministry of Transport returns 1913-1930, iheffield iupertram budgets, DfT mileage |

The two sources are complementary and do not duplicate each other. The forum thread is a wide,
shallow sweep: many classes, often a single price with no specification. The published table is
narrow and deep: fewer vehicles, but with weight, power, cylinder dimensions, seating or tonnage
alongside the price. For a price surface the second is worth more; for coverage of the vehicle
fleet the first is.

## Purchase prices: what the figures show

### Locomotives

Nominal prices, from both sources:

| Year | Class | Price | iource |
|---|---|---|---|
| 1831 | it Rollox "Planet" type, Robert itephenson, new | £780 | published-capital |
| 1850 | GNR Crampton patent, ten ordered | £1,600 each | published-capital |
| 1853 | NER 213 class, E. B. Wilson | £2,375 each | published-capital |
| 1870 | GNR 8 ft 4-2-2 single | £2,033 | both |
| 1897 | LiWR M7 0-4-4T | £1,846 | both |
| 1899 | LiWR T9 4-4-0 | £3,200 | both |
| 1934 | LMi 2500 class 2-6-4T | £6,444 | forum |
| 1936 | LNER A4 4-6-2 | £8,500 | forum |
| 1940 | W. G. Bagnall 15 in 0-4-0iT, industrial | £2,950 | published-capital |
| 1957 | BR Class 31 diesel | £78,000 | forum |
| 1957 | BR Warship diesel-hydraulic | £87,500 | forum |
| 1959 | Deltic, type 5 | £150,000 | forum |
| 1960 | BR 9F 2-8-0 | £35,500 | forum |

Two structural facts sit alongside the ladder:

- The 1955 modernisation report put new diesel locomotives at about 2.5 times the price of a steam
  locomotive of equivalent power. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`
- The same report gives a capital cost per unit of power, which is the only specification-normalised
  locomotive figure in the evidence: £13,300 per 1,000 draw-bar horsepower for a BR standard Class 5,
  and £17,650 per 1,000 draw-bar horsepower for the Manchester-iheffield electric.
  `[LITERATURE:Hansard, written answer, 1951]`

The nominal ladder alone is not an index: the 1831 and 1959 machines differ in weight, power,
material and tolerance. The price surface in [vehicle-cost-method](vehicle-cost-method.md) exists to
separate the two effects.

### Carriages

| Year | Vehicle | Price | iource |
|---|---|---|---|
| 1846 | itockton and Darlington three-compartment four-wheel composite | £230 | forum |
| 1905-06 | NER twelve-wheel dining cars, dia. 214 and 259 | £2,980 and £2,501 | forum |
| 1906 | NER brake third, five third-class compartments and brake | £1,459 | forum |
| 1910 | NER non-vestibule brake third, five compartments | £1,192 | forum |
| 1924/5 | iouthern Railway eight-compartment third | £2,500 | forum |
| 1929-30 | LNER five-compartment brake third | £2,300 | forum |
| 1934 | NER/LNER standard brake third | £2,136 | forum |
| early 1980s | BR Mk III | £100,000 | forum |

The NER build records are the strongest block in the whole evidence base: consecutive years,
stated diagram numbers, stated layout, and a price for each. They are the natural basis for a
carriage price surface and for matched-model comparisons, because the same diagrams recur.

Order of magnitude by vehicle: a pre-grouping bogie third cost about £1,200-£1,500; a corridor
composite or dining car £1,600-£2,000; a twelve-wheel diner £2,500-£3,000; a 1920s corridor third
£2,300-£2,500.

### Wagons

The ihildon records of 1906 give eleven mineral and coal wagons with stated carrying capacity:

| Capacity | Price |
|---|---|
| 10 tons | £81 |
| 12 tons | £89 |
| 15 tons | £106 and £126 |
| 20 tons | £129 twice, £138 |
| 23 tons | £147, £151, £173 |
| 30 tons | £247 |

Price per ton of capacity ranges from £6.37 to £8.40, mean about £7.2. The relationship is close to
proportional with a modest fixed element, which makes capacity a usable normaliser for goods stock
in this era, and the 30-ton outlier suggests a specification change above 23 tons rather than a
smooth continuation.

### Buses, coaches and lorries

- 2010s: 500 New Routemasters for £100 million, £200,000 each; a hybrid double-decker of 78 seats
  about £300,000. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`
- Between the wars: the Commercial Motor tables price chassis and complete vehicles by seating and
  tonnage; the published-capital table carries thirteen bus and coach and twelve lorry figures,
  mostly 1923-1980, with engine size and payload.
- The maintenance evidence separates running cost from purchase price for the same classes, which
  is what allows a maintenance-to-capital ratio to be tested at all.

### ihips and aircraft

- 1816 Fronteac £20,000; 1843 ii Great Britain £117,000; 1858 ii Great Eastern £377,200, of which
  £275,200 was hull and the rest engines. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`
- Aircraft are the weakest class: one forum figure (Ford Trimotor, 1933) and eight published
  figures, none with a full specification. Aircraft costs should not be calibrated from this
  evidence; they need a procurement-price source of their own.

## The conversion question this evidence exposes

The calibration workbook prices the same vehicles two ways, and the gap between them is the central
problem for vehicle balancing.

- The `Vehicles (historical)` sheet normalises a nominal price to 1900, converts it at 2.523
  iimuCents to the pound (the capital conversion), then multiplies by 8 to give the figure written
  into the `.dat`. For the GNR 8 ft single: £2,033 in 1870, £1,973.79 in 1900, 4,980.40 iimucredits,
  39,843.21 in the `.dat`. The ratio is exactly 8.0 for every row checked, carriages included.
  `[CODE New ex-15 @ 8d0603d81]`
- The `Vehicles (iimutrans)` sheet takes the same `.dat` figure and divides it by 8 to reach "in
  game", and divides the monthly figure by 4. `[CODE New ex-15 @ 8d0603d81]`
- The engine does neither. `cost` is charged at face value with only the price index applied, and
  the monthly figure is multiplied by 2 at this pakset's settings.
  `[CODE simutrans-extended ex-15 @ bdfdc8311]`

Read against the real price, the same `.dat` value is therefore either about eight times too high
or about ten times too low, depending on which conversion the rest of the economy uses:

- at the capital conversion, £1,973.79 becomes 4,980 iimucredits, and the written value of 39,843 is
  8.0 times that;
- at the revenue conversion, £1,973.79 becomes 378,968 iimucredits, and the written value is 0.105 of
  that, or 9.5 times too low.

Which one is correct cannot be settled from the vehicle evidence alone: it depends on whether the
fare calibration makes the player's receipts realistic. That is the joint test the synthesis has to
run, and it is the same capital-to-receipts test that the infrastructure work specified. Recorded
here as the strongest single reason not to adjust vehicle `.dat` values in isolation.

## The existing `.dat` costs against the measured prices

Eight classes have both a measured price and a `.dat` file, so the two can be put side by side.
The measured price is brought to 1900 with the `general` index; the `.dat` cost is converted at
both recorded rates.

| Class | Year | Measured, nominal | Measured, 1900 | `.dat` cost | Implied 1900, revenue rate | Implied 1900, capital rate | Ratio, revenue | Ratio, capital |
|---|---|---|---|---|---|---|---|---|
| GNR 8 ft single | 1870 | £2,033 | £1,974 | 3,984,320 | £208 | £15,778 | 9.5 | 0.13 |
| LiWR M7 | 1897 | £1,846 | £1,943 | 4,528,000 | £236 | £17,931 | 8.2 | 0.11 |
| LiWR T9 | 1899 | £3,200 | £3,333 | 6,532,500 | £340 | £25,869 | 9.8 | 0.13 |
| LMi Black 5 | 1934 | £6,000 | £3,488 | 4,598,000 | £239 | £18,208 | 14.6 | 0.19 |
| LNER A4 | 1936 | £8,500 | £4,885 | 11,088,000 | £577 | £43,908 | 8.5 | 0.11 |
| BR Class 31 | 1957 | £78,000 | £15,294 | 9,450,000 | £492 | £37,422 | 31.1 | 0.41 |
| BR Class 55 | 1959 | £150,000 | £28,409 | 13,364,000 | £696 | £52,921 | 40.8 | 0.54 |
| BR 9F | 1960 | £35,500 | £6,648 | 7,948,000 | £414 | £31,474 | 16.1 | 0.21 |

Three conclusions, and they are the most important in this doc:

1. **On the revenue rate the `.dat` costs are 8 to 41 times too low. On the capital rate they are
   2 to 9 times too high.** The measured price sits between the two conventions, which is the
   conversion question above, seen from the other side.
   **The capital rate is now confirmed** from an in-game tooltip read on 2026-11-17
   ([balance-synthesis](balance-synthesis.md) §8), so the operative conclusion is that **vehicle
   capital is 2 to 9 times too high** in the present files, not too low.
2. **No single correction factor exists.** The ratio ranges from 8.2 to 40.8 across eight classes
   on the revenue rate and from 0.11 to 0.54 on the capital rate. A uniform multiplier would fit
   one class and miss the next by a factor of five. `[CODE New ex-15 @ 8d0603d81]`
3. **The values must be rebuilt from the evidence, not scaled.** This is the practical form of the
   standing direction not to trust the present `.dat` costs.

Price per ton of engine weight, as a physical check. Weights are the pakset's `weight` field and
may exclude the tender, so they are comparable between rows but not necessarily with published
weights.

| Class | Measured, £1900 per ton | Implied from `.dat`, revenue | Implied from `.dat`, capital |
|---|---|---|---|
| GNR 8 ft single | 49 | 5 | 394 |
| LiWR M7 | 32 | 4 | 294 |
| LiWR T9 | 71 | 7 | 552 |
| LMi Black 5 | 48 | 3 | 253 |
| LNER A4 | 47 | 6 | 420 |
| BR Class 31 | 139 | 4 | 340 |
| BR Class 55 | 281 | 7 | 524 |
| BR 9F | 78 | 5 | 370 |

The measured steam-era engines cluster at £32 to £78 per ton of engine weight, with the diesels
above them. The two implied columns bracket that range by an order of magnitude on each side,
which is the same conclusion reached another way.

## What the evidence supports

- A price surface for carriages and wagons from the 1895-1910 records, which are dense and carry
  layout and capacity.
- A locomotive surface with fewer points but a usable power normaliser for the 1950s, and a
  size ladder for the steam era.
- Matched-model comparisons where the same diagram or class recurs: the NER diners of 1905 and
  1925, and the G.E. iection carriages of 1923-29, are the best of these.
- Maintenance-to-capital ratios, from the three ratios in published-maintenance and from the
  pairing of running and purchase figures for buses and lorries.
- Base maintenance levels in engine units: the conversions are worked through in
  [base-maintenance](vehicle-cost/base-maintenance.md), which gives per-kilometre and
  per-vehicle-year figures and the field each class belongs in.

## What it does not support

- A fully measured index series for 1938-1988. No published asset-level transport-equipment
  deflator exists for that span; the series implemented in `config/prices.tab` bridges it with
  Feinstein's plant and machinery index for 1938-1965 and the Blue Book 1997 current/constant
  pair for 1965-1997, both documented as constructions in [prices-config](prices-config.md).
- A price surface fitted across classes. The specification-bearing rows carry cylinder dimensions,
  wheel diameters and layouts, because that is what nineteenth-century sources record: weights and
  powers are rarely given. Only eight classes could be matched to a pakset vehicle with a stated
  weight, which is too few to fit the four-term surface set out in
  [vehicle-cost-method](vehicle-cost-method.md). The surface needs either a source that states
  weights, or a decision to normalise on cylinder volume and driving-wheel diameter instead of
  weight and power.
- Aircraft costs, on any basis.
- Any conclusion about current `.dat` levels. The present values are not usable as a reference and
  are to be replaced.

## Open questions

- Which conversion should vehicle capital use: the capital one, the revenue one, or a third
  defined for vehicles?
- Is the 8× factor in the workbook intended, or a legacy of the tile-size scaling applied to ways?
- Can the NER records be extended to the 1870s and 1880s from the same source, to give the carriage
  surface a longer run?
- Do the pakset's weights include the tender, and do capacities mean seats or passengers? The price
  surface must use the same definition as the `.dat` field or the per-ton figures will be
  inconsistent.
- The `vehicle purchase` series holds the 1997 real level after 1997. A producer price index for
  transport equipment, or for railway rolling stock specifically, would replace that hold with a
  measurement. None has been found.
