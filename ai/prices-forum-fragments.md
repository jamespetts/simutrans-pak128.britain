---
status: draft
verified: New ex-15 @ b39ac938d (working tree)
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

The thread also carries pre-1845 prices, but for **other** object types: canals, bridges,
tunnels, aqueducts, locomotives (from 1812), carriages (from 1838) and ships. The structure
prices are tabulated below and belong with `infrastructure`, not with `buildings`; locomotives,
carriages and ships belong with `vehicle purchase` and the ship series.

## Infrastructure fragments

### Canals and aqueducts

| Year | Item | Cost | Length | Cost per km | Page |
|---|---|---|---|---|---|
| 1724 | Exeter Canal, 4-mile improvement, England's earliest ship canal | £20,000 | 6.4 km | £3,125 | `.220` |
| 1761 | Bridgewater Canal, barge canal | £220,000 | 66 km | £3,330 | `.120` |
| 1771 | Staffordshire and Worcestershire Canal, narrowboat | over £100,000 | 74 km | over £1,350 | `.120` |
| 1777 | Trent and Mersey Canal, narrowboat | £296,000 | 150 km | £1,970 | `.120` |
| 1795 | Lune Aqueduct, stone, 20 ft wide | £50,000 | 202 m | about £243,000 at 1900 prices | `.260` |
| 1800 | Pontcysyllte Aqueduct, iron, 12 ft wide | £47,000 | 307 m | about £153,000 at 1900 prices | `.260` |
| 1810 | River Cart Aqueduct, stone, flyboat canal | £5,440 | 9.1 m | about £383,000 at 1900 prices | `.260` |
| 1827 | Gloucester and Sharpness Canal, ship canal | £440,000 | 25.5 km | £17,250 | `.120` |
| 1894 | Manchester Ship Canal, large ship canal | £15,000,000 | 58 km | £260,000 | `.120` |
| 1905 | New Junction Canal, ship canal | £300,000 | 9 km | £34,000 | `.120` |

The canal figures include earthworks, tunnels, aqueducts and the watercourse itself, so they are
whole-route costs rather than way costs. The three narrowboat and barge canals of 1761-1777 span
£1,350 to £3,330 per km, a factor of 2.5 within sixteen years.

### Viaducts

Assembled from the Wikipedia articles the thread's contributor could find; the contributor
warns that some of the source articles failed verification, and that the "wet" or "dry"
foundation is the majority of the pillars.

| Year | Viaduct | Material | Cost | Length | Nominal £/km | £/km at 1900 prices |
|---|---|---|---|---|---|---|
| 1828 | Sankey | stone | £45,000 | 183 m | 245,902 | 241,080 |
| 1836 | Dutton | stone | £54,000 | 457 m | 118,162 | 121,816 |
| 1837 | Penkridge | stone | £6,000 | 82 m | 73,171 | 73,910 |
| 1838 | Victoria | stone | £40,338 | 247 m | 163,312 | 163,312 |
| 1839 | Willington Dene | timber on stone | £25,000 | 319 m | 78,370 | 73,243 |
| 1840 | Stockport | brick | £72,000 | 547 m | 131,627 | 120,759 |
| 1842 | Ouse Valley | brick | £38,500 | 450 m | 85,556 | 87,302 |
| 1848 | Usk | timber | £20,000 | 366 m | 54,645 | 62,096 |
| 1849 | Chappel | brick | £32,000 | 320 m | 100,000 | 117,647 |
| 1849 | Yarm | stone | £44,500 | 690 m | 64,493 | 75,874 |
| 1851 | Knaresborough | stone | £9,803 | 80 m | 122,538 | 149,436 |
| 1854 | Hengoed | stone | £20,000 | 260 m | 76,923 | 80,128 |
| 1857 | Crumlin | wrought iron trestle | £62,000 | 500 m | 124,000 | 136,264 |
| 1857 | Belah | lattice truss | £31,630 | 317 m | 99,779 | 109,647 |
| 1859 | Grosvenor | metal arch | £84,000 | 283.5 m | 296,296 | 336,700 |
| 1861 | Kingsland | brick, urban, 4,500 people displaced | £1,000,000 | 3,000 m | 333,333 | 387,597 |
| 1869 | Ribblehead | stone and brick | £343,318 | 400 m | 858,295 | 964,376 |
| 1871 | Scotswood | wrought iron beam | £20,000 | 212 m | 94,340 | 102,543 |
| 1878 | Welland | brick, made on site | £12,000 | 1,166 m | 10,292 | 11,187 |
| 1897 | Fledborough | brick | £65,000 | 814 m | 79,853 | 92,852 |
| 1898 | Glenfinnan | cement arch | £18,904 | 380 m | 49,747 | 55,275 |
| 1906 | King Edward VII | lattice on stone piers | £500,000 | 350 m | 1,428,571 | 1,587,302 |
| 1909 | Queen Alexandra | truss on stone | £450,000 | 274 m | 1,642,336 | 1,845,321 |
| 1933 | Carnon | stone | £40,000 | 230 m | 173,913 | 110,072 |
| 1978 | Queen Elizabeth II | truss on concrete | £4,900,000 | 352.7 m | 13,892,827 | 499,024 |

The 1900 column is this repository's own conversion, using the `buildings` series divided by 100;
the thread's contributor used an unstated deflator and published a similar column. Almost all
these structures carried two tracks, and the thread's contributor halves the figures for a
single-track model.

### Tunnels

| Year | Tunnel | Type | Cost | Length | Nominal £/m | £/m at 1900 prices |
|---|---|---|---|---|---|---|
| 1779 | Dudley | narrowboat canal | £9,700 | 2,900 m | 3.3 | 5 |
| 1810 | Standedge | narrowboat canal | £160,000 | 4,979 m | 32.1 | 23 |
| 1818 | Islington | canal | £700,000 | 878 m | 797 | 613 |
| 1837 | Primrose Hill | two tracks, bored | £120,000 | 9,700 m | 12.4 | 12 |
| 1838 | Kilsby | two tracks | £320,000 | 2,216 m | 144.4 | 144 |
| 1839 | Woodhead | one track, gunpowder | £200,000 | 4,840 m | 41.3 | 39 |
| 1839 | Clay Cross | rail | £140,000 | 1,631 m | 85.8 | 80 |
| 1840 | Milford | two tracks | £93,122 | 783 m | 118.9 | 109 |
| 1841 | Summit | two tracks | £251,000 | 2,638 m | 95.2 | 89 |
| 1843 | Thames | shield, single track | £454,000 | 396 m | 1,146 | 1,318 |
| 1845 | Thackley | two tracks | £68,000 | 1,200 m | 56.7 | 62 |
| 1846 | Standedge | single track | £201,000 | 4,880 m | 41.2 | 43 |
| 1858 | Netherton | barge canal | £302,000 | 2,768 m | 109.1 | 123 |
| 1875 | Blea Moor | two tracks, dynamite | £109,000 | 2,404 m | 45.3 | 45 |
| 1897 | Blackwall | two-lane road, shield | £1,400,000 | 1,350 m | 1,037 | 1,206 |
| 1908 | Rotherhithe | two-lane road, shield | £1,000,000 | 1,482 m | 675 | 750 |
| 1926 | Colwall New | single track, pneumatic tools | £196,080 | 1,432 m | 137 | 72 |
| 1930 | Queensway | four lanes | £8,000,000 | 3,240 m | 2,469 | 1,403 |
| 1953 | Woodhead 3 | two tracks | £4,300,000 | 4,888 m | 880 | 165 |
| 1962 | Victoria line | two single-track tubes | £56,000,000 | 21,000 m | 2,667 | 414 |

Mills, *Railway Construction* (1910), quoted in the thread, gives the contemporary range for
double-line tunnels as £32 to £150 per lineal yard, with £50 to £60 typical and the range
attributed to ground conditions and the cost of lining material.

### Roads and other structures

| Year | Item | Figure |
|---|---|---|
| 2011 | Motorway, ordinary three-lane | £17,045 per yard |
| 2011 | Motorway tunnel | £142,000 per yard |
| 2011 | Elevated motorway section | £78,000 per yard |
| 2011 | Bridges against plain ways | about 10 times the cost |
| 1909 | Small mechanical signalbox, with signals and block instruments | about £300, plus £150 a year to man and maintain |
| 1938 | Way maintenance, canals against railways | £184 per mile against £1,130 per mile |

The 2011 road figures and the 1938 maintenance comparison are the only figures in the thread
that state a ratio between structure types directly.

## What it does not supply

- **No pre-1845 building construction prices.** The earliest building or structure price in the
  thread is the 1851 Brighton carriage shed. The `buildings` index therefore cannot be extended
  backwards from this thread; the 1750-1844 block remains the general-index backcast recorded in
  [prices-config](prices-config.md).
- No continuous series of any kind. Each item is a single project with its own scope, so the
  items cannot be chained into an index: the 1861 Low Street station at £630 and the 1891
  Westcliff station at £4,000-5,000 are not the same building written twice.
- No infrastructure price index, for a different reason: the points were tested as a series and
  show no drift within a fixed specification, but the uncertainty is wide enough that they
  cannot refine the path. The test and its intervals are in
  [prices-infrastructure](prices-infrastructure.md).

## Use

- For relative pricing within one era, which is what the thread was created for, and for
  checking the engine's structure multipliers against real projects of similar scope.
- For the absolute level of building costs, use the chained index rather than any single
  project: a station price is a project price, and its scope varies by a factor of tens.
- For relative costs of structure types, the 2011 road figures give the only stated ratios in
  the thread: a bridge about ten times a plain way, and elevated and tunnel sections several
  times a bridge.

## Open questions

- Which of the Tilbury 1906 items should be treated as the "station" cost and which as separate
  structures, for comparison with `cost_multiply_station`? The thread's own grouping is not
  stated.
- Are there pre-1845 building prices in other pak128.Britain threads or in the forum's
  pak128.Britain sub-board that this thread does not carry?
