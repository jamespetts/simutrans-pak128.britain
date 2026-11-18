---
status: draft
verified: New ex-15 @ b8f011fcd; simutrans-extended ex-15 @ 22cc3af
---
# Infrastructure price series

**Covers**: the `infrastructure` key of `New/config/prices.tab`: the engine costs that key
scales, the published index series that exist, how those series chain together, and what to do
about the period before 1980. General method, unit conversion and the other price types:
[prices-config](prices-config.md).

The series is **implemented** in `prices.tab` as of 2026-11-16. Its lower end follows the
`general` index and its 1980-2026 end follows the chained ONS series; the reasoning is below.

## Engine coverage

The key is applied through `karte_t::get_inflation_adjusted_price(monthyear, base_price,
price_type)`, which divides by 100 after interpolating the year index. The mapping below was
read from the engine source at `22cc3af` and is identical at `d4893f3`, the commit an earlier
note cited when it recorded that every `cst_*` multiplier follows `buildings`.

- **Transport infrastructure objects.** `obj_desc_transport_related_t` in
  `descriptor/obj_base_desc.cc` applies `infrastructure` to `get_base_price()`, `get_value()`,
  `get_base_way_only_cost()` and `get_way_only_cost()`. `way_desc_t`, `bridge_desc_t`,
  `tunnel_desc_t`, `pier_desc_t` and `way_obj_desc_t` all derive from
  `obj_desc_transport_infrastructure_t`, which derives from it, so way, bridge, tunnel, pier
  and way-object construction and value all follow this key.
  `[CODE simutrans-extended ex-15 @ 22cc3af]`
- **Forging cost.** `settings_t::get_forge_cost()` in `dataobj/settings.cc` applies it to the
  per-tile cost, after scaling the `forge_cost_*` setting by `meters_per_tile` and dividing by
  1000. `bauer/wegbauer.cc` adds that figure to the way cost, and reduces it by
  `parallel_ways_forge_cost_percentage` where a parallel way of the same type already exists.
  `[CODE simutrans-extended ex-15 @ 22cc3af]`
- **Halt construction multipliers.** `get_cost_multiply_station()`, `_dock()`, `_roadstop()`,
  `_airterminal()` and `_post()` apply it. In `simtool.cc` a halt building whose `.dat` has no
  `cost=` and no `station_price=` is priced as the multiplier times its `level`; a halt
  building with an explicit price is priced from that price and therefore follows `buildings`
  instead. Most of the pakset's station `.dat` files carry `cost=`, so in practice station
  buildings are mostly on `buildings` and only the level-derived ones are on this key.
  `[CODE simutrans-extended ex-15 @ 22cc3af]`
- **Maintenance and landscaping.** Way, way-object, bridge, tunnel, signal, roadsign and
  electrification maintenance, and the land alteration, reclaim land, alter climate, set slope
  and remove tree costs, apply it at their call sites in `player/finance.cc`,
  `gui/way_info.cc`, `gui/money_frame.cc`, `obj/signal.cc`, `obj/roadsign.cc` and
  `dataobj/settings.cc`. `[CODE simutrans-extended ex-15 @ 22cc3af]`

## What the published index measures

The official measure is the ONS output price index for new work: infrastructure. It is not a
general construction index and not a civil engineering index in the broad sense:

- The representative projects are asphalt roads (90%) and bridges (10%). Materials, labour and
  plant are weighted 40.2%, 48.1% and 11.7% within each project.
  `[LITERATURE:https://www.ons.gov.uk/aboutus/transparencyandgovernance/freedomofinformationfoi/ouputpriceindexandtheindexfornewwork]`
- It is built by a project cost approach: input costs are weighted and a profit mark-up is
  applied, so it is a proxy for the price paid rather than a record of tenders.
  `[LITERATURE:https://www.ons.gov.uk/businessindustryandtrade/constructionindustry/methodologies/constructionoutputpriceindicesopisqmi]`
- The index contains road and bridge projects only. It has no railway permanent way, earthwork,
  canal, dock or pier project in it. For those the index is a stand-in chosen because no
  separate published series exists.

## The three vintages

No single file covers the whole period. The series arrives in three blocks, each with an
overlap on the next:

| Years | Source | Base | Frequency |
|---|---|---|---|
| 1980-2011 | BIS Construction Price and Cost Indices, Output Price Indices, Table 1 column 13 | 2005 = 100 | annual rows, then quarterly |
| 1996-2015 | ONS interim construction output price indices, "New work" table, infrastructure column | 2005 = 100 | monthly |
| 2014-2026 | ONS construction output price indices, "New work" table, infrastructure column | 2015 = 100 | monthly |

- The BIS sheet's own footnote reads "Infrastructure index not available before 1980", and the
  series does start in 1980. The same file carries an infrastructure output price index for
  repair and maintenance in Table 2, but that one starts only in 2010, so there is no long-run
  maintenance series for this key either.
  `[LITERATURE:https://www.gov.uk/government/statistics/bis-prices-and-cost-indices]`
- The ONS interim back history was released on 2016-02-17 as the back series for the output
  price indices that replaced the BIS indices in 2015.
  `[LITERATURE:https://www.ons.gov.uk/economy/inflationandpriceindices/adhocs/005372interimconstructionoutputpriceindicesopis1996to2015]`
- The current ONS dataset runs from January 2014 to the latest month and is reissued quarterly;
  the release used here is that of 2026-11-12, covering to September 2026.
  `[LITERATURE:https://www.ons.gov.uk/businessindustryandtrade/constructionindustry/datasets/interimconstructionoutputpriceindices/current]`

## Chaining

Annual means are taken where a source is monthly; the BIS annual rows are used as published.
Two link factors are then applied, each measured on the overlap year:

- BIS to ONS interim, at 1996: the interim series is 1.0334 times the BIS series.
- ONS interim to current ONS, at 2014: the current series is 0.7981 times the interim series,
  that is, 2005 sits at 79.8 on the 2015 = 100 scale.

The first factor is not a price movement. The two series measure the same thing and differ by
between 6% below and 9% above across 1996-2011, so the interim back history is a
re-estimation, not a reproduction, of the BIS figures. The link absorbs that difference into a
single step at 1996.

The base year itself cannot be used to check the second factor, because the 2015 value of the
current series is 100 by construction.

## Before 1980

No free civil engineering or road construction price series reaching back before 1980 was
found. The candidates checked, and why each fails:

- **Department of the Environment road construction tender price indices, from 1970.** The
  series exists and is the obvious continuation, but its values are tabulated only in Spon's
  handbook and in *Housing and Construction Statistics*; no free tabulation was found in the
  Construction Statistics Annual, Transport Statistics Great Britain, RDE0102, the National
  Archives web archive or Parliament. It was superseded by ROADCON in 1985.
  `[LITERATURE:https://www.routledge.com/Spons-Construction-Cost-and-Price-Indices-Handbook/Fleming-Tysoe/p/book/9780419153306]`
- **Department of the Environment Cost of New Construction index, 1949 Q1 to 1980 Q1.** The
  official predecessor of the output price indices, but again not freely tabulated in full; the
  Construction Statistics Annual states only that the output price indices superseded it. Some
  annual United Kingdom values for 1957-1970 are in Hansard.
- **PAFI Civil Engineering, the 1970 Series, formerly the NEDO or Baxter indices.** Monthly from
  1970 on a 1970 = 100 base, and still published, but it is an input cost index rather than a
  price index, and the bulletin is not free; quarterly values are reproduced in Spon's Civil
  Engineering and Highway Works Price Book.
- **BCIS General Civil Engineering Cost Index.** First published in December 2008, so it is not
  a long-run series and cannot reach back.
- **BIS tender price indices for all construction (ALLCON), public sector building (PUBSEC),
  social housing (TPISH) and road construction (ROADCON).** All begin in 1985. PUBSEC alone runs
  from 1950 but is a building index, not a civil engineering one.
  `[LITERATURE:https://www.gov.uk/government/statistics/bis-prices-and-cost-indices]`
- **The Department for Transport road construction tender price index, table RDE0102.** Covers
  2002-2017 only; each Transport Statistics Great Britain edition carries a rolling ten-year
  window, so no edition holds a long run.
  `[LITERATURE:https://www.gov.uk/government/statistical-data-sets/rde01-road-construction-and-taxation]`
- **Mills, *Railway Construction* (Longmans; the 1910 fourth impression reprints the 1898
  setting).** Checked in full. It has no cost per mile by class of line, no earthwork rates, no
  bridge or viaduct rates, no station, land or parliamentary figures, and no price year. What it
  has is a permanent-way materials schedule by rail weight, which is c.1898 and excludes labour,
  and a paragraph of illustrative tunnel rates from £32 to £150 per lineal yard, which the author
  declines to present as an average. That lead is closed.
  `[LITERATURE:https://www.gutenberg.org/ebooks/50696]`

The one free long-run construction series that does exist is the Bank of England workbook, sheet
A32, continuous annual from 1845 to 2001, built from Mitchell's building costs to 1938 and
Holmans's construction costs after that. It is a building and construction series, not a civil
engineering one, and it is the source already used for `buildings`. No road, infrastructure or
civil engineering price index appears anywhere in the workbook's 109 sheets.
`[LITERATURE:https://www.bankofengland.co.uk/statistics/research-datasets]`

### Test of the forum's structure prices

The forum thread holds individual canal, aqueduct, viaduct and tunnel prices from 1724 to 1978,
tabulated in [prices-forum-fragments](prices-forum-fragments.md). They were tested as a possible
pre-1980 series by deflating each price with the `general` index and asking whether the
deflated cost per unit drifts against the year of building.

Taken as one pool, they do drift: about 1.2% a year for bridges, 1.9% for tunnels and 2.1% for
canals, each significant. That drift is specification, not price. A 1978 concrete bridge is a
larger structure per metre than an 1830 stone viaduct, and the mix of structure types changes
with the date, so a pooled regression measures the change of mix.

Within a fixed specification the drift disappears:

| Class | Years | n | Drift a year | 95% interval |
|---|---|---|---|---|
| Stone viaducts | 1828-1933 | 8 | -0.24% | -1.25 to +0.78 |
| Brick viaducts | 1840-1897 | 6 | -1.69% | -6.21 to +3.04 |
| Two-track tunnels | 1837-1875 | 6 | -0.53% | -6.21 to +5.49 |
| Single-track tunnels | 1839-1926 | 3 | +0.75% | +0.62 to +0.87 |
| Canals, narrowboat and barge | 1724-1777 | 4 | -1.65% | -3.83 to +0.57 |
| Electrification, per kilometre | 1891-1986 | 4 | -0.87% | -2.72 to +1.02 |

Every class except the three-point single-track tunnel group is consistent with no drift. That
group's interval is implausibly narrow because its three points lie almost on a straight line,
which is a property of three points rather than evidence. Repeating the test with `buildings`
instead of `general` moves no interval by more than 0.15 percentage points a year, because the
two indices are close over most of the period, so the data cannot separate them.

The prices therefore do not replace the index, but they are not uninformative either: they
exclude a drift larger than about 1% a year, which is a factor of 2.7 over a century, and they
are silent below that. The pre-1980 path is consequently supported to within a factor of about
three, and no better.

That leaves a choice the data cannot settle: whether the pre-1980 path should be `general`,
which is what the key already inherits, or `buildings`. The series as implemented follows
`general`, for two reasons: the test finds no movement within a fixed specification, which is
exactly a flat real path, and the workbook that derived the base prices deflated its historical
items with `general`, so the base prices are already on that basis. Against `buildings` stands
only the construction family it belongs to.

### Acworth's capital figures

Acworth, *The Elements of Railway Economics*, gives the stock of railway capital rather than a
series, but it supplies levels that the forum's individual projects do not. There are three
editions, and the 1911 is a reprint of the 1905 setting with identical text and pagination, so
the two can be cited together; the 1924 edition is a revision with a different territorial base
and must not be differenced against them. `[LITERATURE:https://archive.org/details/cu31924070676402]`

| Edition | Year referred to | Total capital | Road and buildings | Route miles | Per mile |
|---|---|---|---|---|---|
| 1905, 1911 | c.1902, United Kingdom | £1,000,000,000 spent | £800,000,000 | 22,000 | £36,364 |
| 1924 | c.1923, Great Britain | £1,180,000,000 spent | £878,000,000 | 20,300 | £43,251 |

- Named lines: the West Highland, built in 1900, about £13,000 a mile; the Great Central's
  London extension, opened in 1898, ten to twelve times that; the North London, £330,000 a mile;
  the Waterford and Tramore, £10,000. The 1924 edition substitutes the Highland at £14,500 for
  the Waterford and Tramore in the cheap-against-dear comparison.
- Illustrative, not measured: £40,000 for a great English line, £10,000 for an American line and
  £4,000 for a light railway in 1905, raised to £50,000 and £15,000 in 1924 with the light
  railway unchanged. Preliminary and parliamentary expenses are a quoted estimate of about
  £4,000 a mile in both editions, attributed to "a competent authority" and described by Acworth
  as a figure nobody knows.
- Maintenance of way and works: £500 a mile of open line in 1902, ranging from £85 for the
  Waterford and Tramore and £145 for the Midland Great Western of Ireland up to about £3,000 for
  the North London; £1,200 a route mile in 1923, ranging from £119 for the Weston, Clevedon and
  Portishead to £5,400 for the Metropolitan. The two averages rest on different mileage bases and
  Acworth never sets them side by side, so they are not a series.
- The book has no component breakdown of construction, no cost per mile for any pre-1900 railway,
  no station, land or permanent-way cost per mile, and no price year. Its maintenance tables for
  the Midland (1903) and the LNER (1923) are the only component analyses, and they are running
  costs rather than construction.

The average capital figure and the maintenance figure are levels at about 1900, on the 1900 basis
the `.dat` prices use, so they are useful for checking way and structure base prices. They do not
give the movement of prices over time.

The test therefore leaves the position below unchanged, but for a different reason than a
straight rejection: the prices cannot distinguish `general` from `buildings`, and both are
consistent with the data within wide bounds. The pre-1980 path is supported to within a factor
of about three rather than by positive measurement.

The treatment recommended here is the one already used for other short series: hold the
`buildings` path for 1750-1980 and splice the infrastructure index onto it at 1980. The
combined series is then continuous at 1980, and 1900 stays at 100 by construction because
`buildings` is 100 in 1900.

That choice discards the relative level the BIS series shows for 1980, where infrastructure
prices stood about 48% above all-new-construction prices. Keeping that level would require a
step at 1980, because nothing in the pre-1980 data can support it. The consequence is that the
whole pre-1980 range carries building prices rather than civil engineering prices.

### Cross-check against tender prices

There is a second, independent measure of the same thing: ROADCON, the tender price index for
road construction, which is built from actual contract prices rather than from a cost model. It
is free from 1985 to 2011 in the BIS tender price file, on a 1995 = 100 base, and it does not
continue after 2012.

Over the 27 common years the two correlate closely in logarithms, at 0.977, so they describe the
same broad movement. They do not agree on magnitude. Rebased to 1995, ROADCON runs about 15%
below the output price index in 1990-92 and about 20% above it by 2010-11, having risen 26% more
across the period as a whole.

That matters for the series because it means the choice of measure, not only the choice of
deflator, moves the answer. The real fall of about 43% quoted below is what the output price
index gives. The same calculation taken to the tender index would give a fall nearer 26%. Both
are falls, but the size is uncertain by roughly fifteen percentage points over the period.
`[LITERATURE:https://assets.publishing.service.gov.uk/media/5a798116ed915d07d35b60ad/12-p147c-tender-price-indices-2012Q3.xls]`

The output price index is used as the series because it covers 1980 to 2026 continuously and
because it is the measure that ONS publishes as the official one. The divergence is recorded
rather than resolved.

## Candidate results

Computed on 2026-11-15 from the three sources above, with the 1980 splice:

| Year | Infrastructure | `general` | Ratio to `general` |
|---|---|---|---|
| 1980 | 4,462 | 2,866 | 1.56 |
| 1990 | 6,331 | 5,408 | 1.17 |
| 2005 | 7,967 | 8,232 | 0.97 |
| 2014 | 9,908 | 10,978 | 0.90 |
| 2026 | 14,409 | 16,281 | 0.89 |

Over 1980-2026 the index rises 3.23 times, against 5.68 times for `general` and 4.94 times for
`buildings`. The implied real fall in infrastructure prices is about 43%, which follows from
the BIS series itself: infrastructure output prices rose 1.84 times between 1980 and 2005 while
all-new-construction prices rose 2.72 times. `[CODE New ex-15, working tree 2026-11-15]`

That 43% is the output price index answer. The cross-check above gives about 26% on the tender
price index, so treat the size of the fall as uncertain by roughly fifteen percentage points
over the period even after 1980.

The implemented line in `prices.tab` runs from 1750 to 2050 on the same basis as the other
series: 1750-1980 is the `buildings` value for that year, 1980-2026 is the chained index, and
2027-2050 holds the 2026 real level and tracks `general`, as `buildings`, `city land` and
`country land` do.

## Traps

- The three vintages sit on two base years, so any block assembled without both link factors
  contains a break.
- The BIS series was compiled for BIS by the Building Cost Information Service under contract,
  and the ONS interim back history is an experimental series. Neither carries the standing of
  the current ONS release.
- The index is an output price for public sector roads and bridges. Applying it to a canal, a
  pier or a railway cutting assumes those moved with road construction prices.
- As with `buildings`, the key covers maintenance as well as construction, and the index
  measures new work.

## Open questions

- Should the pre-1980 path be `general` rather than `buildings`? The test above cannot separate
  them. `general` adds no claim the key does not already make, so the series would change only
  after 1980; `buildings` keeps the infrastructure key in the same family as the construction
  prices it belongs to.
- Should the relative level the BIS series shows for 1980, about 48% above all-new-construction
  prices, be kept at the cost of a step at 1980 rather than discarded by the splice?
- Are the Department of the Environment road construction tender price indices obtainable in a
  library, so that 1970-1980 could be covered by civil engineering prices rather than building
  prices?
- Should ways, which are the majority of `infrastructure` spending in game, be indexed by the
  roads-and-bridges measure at all, or would a building index be closer to railway permanent
  way work? No source settles this; the road measure is used because it is construction work
  rather than building work.
- Would a cost book that tabulates unit rates for a fixed specification tighten the intervals in
  the test above enough to distinguish `general` from `buildings`? Mills was checked and has no
  such rates; Spon's is the remaining candidate, and it is print or subscription. The present
  intervals are wide because each class has three to eight items.
- The relative costs of structure types that the forum data implies, such as a bridge at about
  ten times a plain way, belong to the `.dat` base prices rather than to the year index. Should
  they be applied to the way, bridge, tunnel and pier base costs, and if so under which doc?
