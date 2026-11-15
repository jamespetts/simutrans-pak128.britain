---
status: draft
verified: New ex-15 @ b39ac938d (working tree); simutrans-extended ex-15 @ 22cc3af
---
# Infrastructure price series

**Covers**: the `infrastructure` key of `New/config/prices.tab`: the engine costs that key
scales, the published index series that exist, how those series chain together, and what to do
about the period before 1980. General method, unit conversion and the other price types:
[prices-config](prices-config.md).

The series described here is **researched but not implemented**: `infrastructure` is still a
commented-out placeholder and therefore still inherits `general`.

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

- BIS tender price indices for all construction (ALLCON), public sector building (PUBSEC),
  social housing (TPISH) and road construction (ROADCON) all begin in 1985.
  `[LITERATURE:https://www.gov.uk/government/statistics/bis-prices-and-cost-indices]`
- The Department for Transport road construction tender price index, table RDE0102, covers
  2002-2017 only, and the table notes that the ONS has no plans to produce a replacement.
  `[LITERATURE:https://www.gov.uk/government/statistical-data-sets/rde01-road-construction-and-taxation]`
- Spon's *Construction Cost and Price Indices Handbook* lists the two genuine civil
  engineering series that do reach back: the Department of the Environment road construction
  tender price indices from 1970 and Spon's constructed civil engineering cost index from 1970.
  Both are print or subscription, and neither reaches 1845.
  `[LITERATURE:https://doi.org/10.4324/9780203473283]`

### Test of the forum's structure prices

The forum thread holds individual canal, aqueduct, viaduct and tunnel prices from 1724 to 1978,
tabulated in [prices-forum-fragments](prices-forum-fragments.md). They were tested as a possible
pre-1980 series by dividing each price by the `buildings` index for its year, which asks whether
the cost of a structure in 1900 prices stays the same across the period.

It does not. The viaducts built between 1828 and 1859 come out between £73,000 and £337,000 per
kilometre in 1900 prices, a factor of 4.6, with no trend against the date of building. The
two-track tunnels built between 1838 and 1875 come out between £45 and £144 per metre, a factor
of 3.2; Primrose Hill, built in 1837 and also two tracks, comes out at £12 per metre, which is
further out still and makes the full range a factor of 12. The apparent fall between the 1840s
and 1875 rests on a single 1875 tunnel.

The spread comes from the specification: height, span, foundations, and whether the structure is
timber, brick, stone, iron or concrete. It is larger than the inter-decade price movement that
would have to be measured, so these prices cannot be chained into an index. They are useful for
relative costs within an era and for checking a base price, not for the year index.

The test therefore leaves the position below unchanged. It does, however, mean that the
pre-1980 path is supported by the absence of any alternative rather than by positive evidence
that infrastructure prices moved with building prices.

The treatment recommended here is the one already used for other short series: hold the
`buildings` path for 1750-1980 and splice the infrastructure index onto it at 1980. The
combined series is then continuous at 1980, and 1900 stays at 100 by construction because
`buildings` is 100 in 1900.

That choice discards the relative level the BIS series shows for 1980, where infrastructure
prices stood about 48% above all-new-construction prices. Keeping that level would require a
step at 1980, because nothing in the pre-1980 data can support it. The consequence is that the
whole pre-1980 range carries building prices rather than civil engineering prices.

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

To insert it, the placeholder line `#infrastructure=1750,100,2022,100` is replaced by a real
line running from 1750 to 2050 on the same basis as the other series: 1750-1980 is the
`buildings` value for that year, 1980-2026 is the chained index, and 2027-2050 holds the 2026
real level and tracks `general`, as `buildings`, `city land` and `country land` already do.

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

- Should the 1980 relative level be kept, at the cost of a step at 1980, rather than discarded
  by the splice? The current recommendation is to discard it.
- Are the Department of the Environment road construction tender price indices obtainable in a
  library, so that 1970-1980 could be covered by civil engineering prices rather than building
  prices?
- Should ways, which are the majority of `infrastructure` spending in game, be indexed by the
  roads-and-bridges measure at all, or would a building index be closer to railway permanent
  way work? No source settles this; the road measure is used because it is construction work
  rather than building work.
- The forum structure prices were rejected as an index because the specification spread is too
  large. Would a cost book that tabulates unit rates for a fixed specification, such as Mills's
  *Railway Construction* (1910) or a Spon's volume, give a narrow enough spread to measure the
  movement between two dates?
- The relative costs of structure types that the forum data implies, such as a bridge at about
  ten times a plain way, belong to the `.dat` base prices rather than to the year index. Should
  they be applied to the way, bridge, tunnel and pier base costs, and if so under which doc?
