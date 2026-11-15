---
status: draft
verified: New ex-15, working tree 2026-11-15
---
# Forum price fragments

**Covers**: prices of individual buildings and structures posted in the Simutrans forum thread
"A snippet of relative pricing information", and what that thread can and cannot supply.

The thread is https://forum.simutrans.com/index.php?topic=6521.0 (Pak128.Britain-Ex board,
started 2010-12-29, 287 replies). It collects contemporaneous prices with their printed sources.
The table below was extracted from all nine pages of the thread on 2026-11-15. The page suffix
in the last column gives the thread page (`.0` is the first, `.280` the last) so that an item can
be found again. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`

## What it supplies

Building and structure prices, mostly railway stations and depots, from 1851 to 1984. These are
the raw material for the relative costs the engine sets by multiplier rather than by `.dat`
price — `cost_multiply_station`, `cost_multiply_depot` and the platform and canopy proportions.

| Year | Item | Cost | Page |
|---|---|---|---|
| 1851 | Carriage shed, Brighton | £790 | `.0` |
| 1861 | Unspecified shed | £6,271 | `.0` |
| 1861 | Low Street station: 200 ft double-track platforms and one brick building, "parsimonious facilities", estimated | £630 | `.140` |
| 1865 | Cambrian Railway depot, Oswestry | £28,000 | `.175` |
| 1868 | Shed to cover five hundred vehicles | £20,000 | `.0` |
| 1881-85 | Tilbury station improvements, six recorded sums | £953, £187, £389, £217, £246, £479 | `.175` |
| 1886 | Tilbury Town station, works and station, junctions and sidings | £3,150 | `.175` |
| 1891 | Westcliff-on-Sea, new small station, estimate | £4,000-5,000 | `.140` |
| 1894/5 | Bromley-by-Bow station rebuilt after fire, including a signalbox | £18,131 | `.140` |
| 1904 | Tilbury: pile foundations and new station building, estimate | £10,563 | `.175` |
| 1905 | Tilbury: new locomotive shed | £3,496 | `.175` |
| 1906 | Tilbury: station buildings, concourse, platform awnings and stairs | £16,460 | `.175` |
| 1906 | Tilbury: booking office at road level, goods store with office | £1,500 | `.175` |
| 1906 | Tilbury: platform walls, awning foundations and luggage inclines | £3,488 | `.175` |
| 1906 | Tilbury: water tank house, offices, stores and turntable foundations | £1,245 | `.175` |
| 1906 | GWR halt, single wooden building | £264 | `.35` |
| 1906 | Electric tram depot | £30,000 | `.280` |
| 1910 | Plaistow depot, tender accepted | £21,200 | `.140` |
| 1932 | Southend East station, total (of which buildings and canopies £17,040) | £50,660 | `.140` |
| 1934 | Upminster Bridge station: 700 ft platform, canopies, buildings, entrance | £24,511 | `.140` |
| 1938 | Laindon booking and parcels office, planned | £14,620 | `.140` |
| 1954 | Grays, new station building, small station | £33,000 | `.140` |
| 1984 | East Tilbury rebuilt: concrete platforms, brick booking office and shelter | £80,000 | `.140` |

The thread also carries pre-1845 prices, but for **other** object types: canals (Bridgewater
1761, Staffordshire and Worcestershire 1771, Trent and Mersey 1777), bridges (Wharncliffe 1837,
Sankey 1828, Dutton 1836, Victoria 1838, Willington Dene 1839), the Thames Tunnel (1825),
locomotives (from 1812), carriages (from 1838) and ships. Those belong with `infrastructure`,
`vehicle purchase` and the ship series, not with `buildings`.

## What it does not supply

- **No pre-1845 building construction prices.** The earliest building or structure price in the
  thread is the 1851 Brighton carriage shed. The `buildings` index therefore cannot be extended
  backwards from this thread; the 1750-1844 block remains the general-index backcast recorded in
  [prices-config](prices-config.md).
- No continuous series of any kind. Each item is a single project with its own scope, so the
  items cannot be chained into an index: the 1861 Low Street station at £630 and the 1891
  Westcliff station at £4,000-5,000 are not the same building written twice.

## Use

- For relative pricing within one era, which is what the thread was created for, and for
  checking the engine's structure multipliers against real projects of similar scope.
- For the absolute level of building costs, use the chained index rather than any single
  project: a station price is a project price, and its scope varies by a factor of tens.

## Open questions

- Which of the Tilbury 1906 items should be treated as the "station" cost and which as separate
  structures, for comparison with `cost_multiply_station`? The thread's own grouping is not
  stated.
- Are there pre-1845 building prices in other pak128.Britain threads or in the forum's
  pak128.Britain sub-board that this thread does not carry?
