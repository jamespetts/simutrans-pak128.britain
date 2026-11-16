---
status: draft
verified: New ex-15 @ 96cff9eed (working tree); simutrans-extended ex-15 @ 22cc3af
---
# Infrastructure cost synthesis

**Covers**: the combined result of eight research tasks on the capital and maintenance cost of
every infrastructure object family, the conversions that turn those findings into `.dat` values,
and the decisions that remain. Awaiting the pakset owner's decision; **no `.dat` value has been
changed** except the two bugs noted below.

Companions: [infrastructure-base-costs](infrastructure-base-costs.md) (the conversion chain),
[infrastructure-cost-findings](infrastructure-cost-findings.md) (the first-pass audit),
[prices-infrastructure](prices-infrastructure.md) (the year index).

## 1. The scaling map, verified from the engine

Every `.dat` price is scaled before use, but **not every object class is scaled the same way**.
Read from `simworld.cc` (`karte_t::set_scale`) and `obj/roadsign.cc` at `22cc3af`:

| Class | Scaled by | `.dat` value for a real £X |
|---|---|---|
| Ways, tunnels, bridges, way objects (electrification) | `meters_per_tile/1000` = 0.125 | £ per km × 2.523; £ per metre × 2,523 |
| Station buildings, platforms, signalboxes (all in `modifiable_station_buildings`) | 0.125 | £ per object **× 20.19** |
| Signals and roadsigns (`roadsign_t::set_scale`) | 0.125 | £ per object **× 20.19** |
| Industries | 0.125 | — |
| Depots, headquarters, city buildings, attractions | **not scaled** | £ per object × 2.523 |

The distinction matters: three of the research returns used the per-kilometre formula for
per-object classes. Their values for signals, station buildings and signalboxes are therefore
**eight times too small**, and have been corrected in this document. Depots and headquarters are
not scaled and take the smaller factor. Maintenance is scaled on the same pattern, then charged
per month, so annual maintenance in £ = `.dat maintenance` × 0.125 × 0.396311 × 12 for a scaled
one-tile object, and `.dat maintenance` × 0.396311 × 12 for an unscaled one.

## 2. The cross-cutting finding: maintenance carries renewal

The maintenance column appears to have been built from historical accounts that combine routine
maintenance with renewal. Acworth's "maintenance of way and works" and the Board of Trade heading
that the 1938 figure uses both do exactly that, and the Victorian practice of lifting and packing
by travelling relayers was booked to renewal. Simutrans renews separately — `weg_t::renew()`
charges the full way cost again when wear capacity runs out — so any renewal element in
maintenance is double counting.

Every family the researchers examined shows the same shape: capital within a few times of
history, maintenance between four and a hundred times too high. The measured maintenance-only
figures are:

| Source, date | Figure, 1900 prices |
|---|---|
| BR 1966, track maintenance excluding renewal | £44/km/year |
| ORR 2015-16, track maintenance excluding renewal | £334/km/year |
| Cudworth 1886, brick viaduct upkeep | £0.05/m/year |
| Cudworth 1886, iron viaduct upkeep | £0.23-0.25/m/year |
| Plain line upkeep, various 1839-1902 | £0.05-0.31/m/year |
| Canal routine upkeep, 1938 | £62/km/year |

The recommendation is therefore a **single rule rather than object-by-object judgement**: strip
the renewal element out of every maintenance value, and let the wear mechanic fund renewal.

## 3. Decision tables

Values are the researchers' recommendations, corrected for the scaling map above. "Now" is the
current `.dat` value.

### 3.1 Track ways

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| waggonway | 3,250 → **1,050** | 400 → **10** |
| plateway | 10,000 → **1,950** | 600 → **5** |
| cast_iron | 30,000 → **1,650** | 800 → **5** |
| wrought_iron_fishbelly | 30,000 → **1,500** | 755 → **6** |
| wrought_iron_light | 32,000 → **1,850** | 750 → **8** |
| wrought_iron_intermediate | 36,000 → **2,150** | 725 → **10** |
| wrought_iron_track | 40,000 → **2,550** | 700 → **11** |
| wrought_iron_improved | 46,500 → **2,800** | 610 → **12** |
| wssr-early | 52,000 → **3,150** | 575 → **13** |
| wssr | 55,000 → **3,200** | 550 → **13** |
| wssr_light | 32,000 → **2,500** | 375 → **9** |
| wssri | 75,000 → **3,600** | 500 → **14** |
| wssri_intermediate | 90,000 → **3,700** | 450 → **15** |
| wssri_light | 45,000 → **3,050** | 360 → **11** |
| wssri_heavy | 135,000 → **2,400** | 650 → **18** |
| cssr_light | 105,000 → **2,650** | 200 → **35** |
| cssr | 140,000 → **3,250** | 375 → **40** |
| cssri-125 | 150,000 → **4,200** | 575 → **50** |
| tgv | 250,000 → **24,000** | 950 → **35** |
| cssri | 175,000 → **8,500** | 630 → **60** |

`forge_cost_track`: **15,000 → 800-1,000**. Measured formation costs are £110/km (1803),
£253/km (1830, including fencing) and £250-400/km (1855-1900).

### 3.2 Roads

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| bridleway | 1,600 → **120** | 8 → **1** |
| dirt-road | 2,000 → **200** | 16 → **2** |
| improved_road | 2,200 → **500** | 120 → **3** |
| macadam_road | 13,000 → **3,000** | 70 → **5** |
| cobblestone-road | 6,500 → **6,500** | 250 → **60** |
| tarmac_road | 40,000 → **5,000** | 400 → **6** |
| tarmac_city_road | 35,000 → **7,000** | 350 → **50** |
| concrete_road | 110,000 → **80,000** | 175 → **35** |
| city-road | 75,000 → **90,000** | 425 → **45** |
| motorway | 190,000 → **250,000** | 625 → **70** |
| hr-asphalt heavy / medium / light | 92,000 / 80,000 / 73,000 → **110,000 / 75,000 / 45,000** | 425 → **45 / 35 / 30** |

### 3.3 Bridges, viaducts, tunnels

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| masonry-viaduct | 5,120,000 → **250,000** | 205 → **55** |
| brick-viaduct | 4,480,000 → **215,000** | 205 → **50** |
| iron-viaduct | 1,200,000 → **200,000** | 960 → **95** |
| iron-girder-bridge | 1,904,000 → **300,000** | 1,269 → **95** |
| iron-lattice-girder | 2,160,000 → **380,000** | 1,269 → **95** |
| tubular-box-girder | 1,980,000 → **2,800,000** | 1,269 → **105** |
| iron-arch-rail | 4,480,000 → **750,000** | 1,280 → **100** |
| beam-bridge | 3,120,000 → **300,000** | 1,269 → **95** |
| plate-girder | 2,760,000 → **380,000** | 1,269 → **95** |
| steel-truss | 2,520,000 → **880,000** | 1,269 → **110** |
| wooden-trestle | 672,000 → **165,000** | 4,480 → **105** |
| concrete-viaduct | 1,456,000 → **330,000** | 149 → **55** |
| RailTunnelStone / Brick | 2,200,000 / 2,700,000 → **215,000** | 3,000 / 4,400 → **75** |
| severn-tunnel | 2,250,000 → **1,000,000** | 5,250 → **150** |
| RailTunnelConcrete | 3,000,000 → **420,000** | 4,000 → **100** |
| SubSurfaceRailTunnelBrick | 2,000,000 → **300,000** | 4,000 → **75** |
| LT_Tunnel | 775,000 → **150,000** | 1,375 → **95** |

The timber trestle's high maintenance is historical, not an error: timber runs 7-8 times plain
line upkeep, brick about half, iron about 1.2-1.5 times.

### 3.4 Canals, aqueducts, piers

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| canal_tubboat | 9,000 → **2,800** | 75 → **8** |
| canal_narrowboat | 15,000 → **4,800** | 100 → **11** |
| canal (barge) | 30,000 → **8,850** | 200 → **13** |
| canal-lined | 45,000 → **11,600** | 150 → **11** |
| canal_ship | 240,000 → **50,500** | 250 → **21** |
| canal_largeship | 2,500,000 → **686,300** | 300 → **33** |
| masonry-aqueduct tub/narrow/barge | 5,120,000 → **278,000 / 391,000 / 530,000** | 205 → **126 / 179 / 244** |
| brick-aqueduct tub/narrow/barge | 4,480,000 → **214,000 / 303,000 / 416,000** | 205 → **126 / 177 / 244** |
| concrete-aqueduct tub/narrow/barge | 1,456,000 → **114,000 / 156,000 / 214,000** | 149 → **95 / 130 / 179** |
| piers, timber / iron / brick-stone / concrete | → **50,000 / 88,000 / 278,000 / 139,000** | → **147 / 147 / 185 / 116** |

`forge_cost_water`: **25,000 → 1,000** (or 500 if `way + forge` must equal the anchor exactly).
At 25,000 it charges £9,908/km, more than an entire narrow or barge canal.

### 3.5 Stations, platforms, shelters, depots

These are scaled as buildings, so the `.dat` values carry the ×20.19 factor.

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| wooden platform | 75,000 → **7,600** | 4,000 → **32** |
| brick platform | 180,000 → **15,100** | 2,700 → **19** |
| concrete platform | 250,000 → **13,100** | 2,250 → **22** |
| wooden station building | 250,000 → **10,100** | 11,000 → **34** |
| brick or stone building | 800,000-850,000 → **15,100** | 10,000-11,800 → **15** |
| concrete small building | 615,000 → **11,100** | 8,000 → **14** |
| staging post / bare bus stop | 4,000 / 8,500 → **104** | 400 → **0.2** (below one unit) |
| old bus shelter (timber) | none → **1,210** | none → **7** |
| modern bus shelter | none → **510** | none → **1.3** |

The intended trade-off is **confirmed by the evidence** and **contradicted by the current data**:
timber 4-8% of capital a year in maintenance, brick 0.8-1.5%, concrete 1.5-2.5%. The pakset has
concrete below brick where it should be between, and concrete capital above brick where it should
be at or slightly below.

Bus shelters, loading bays, bus terminals and every depot currently have **no cost or maintenance
line at all** — they are free. `cost_depot_rail` = 2,000 implies £2,523 against a measured
£3,973 for the Tilbury shed and £20,390 for Plaistow; suggested 10,000 for rail and 5,000 for road.

### 3.6 Signals, signalboxes, electrification

Signals and signalboxes are scaled per object. The research value per post is small: a semaphore
post with one arm and its share of the wires is £15-18 (1912), a colour-light head £85-160, and
the 1909 figure of £100 an arm for automatic signals stands. Because one `.dat` maintenance unit
is £4.76 a year, **a semaphore post's annual upkeep cannot be expressed** — the field must be 0 or
1, and the true per-post upkeep belongs in the signalbox.

Signalboxes carry the general signalling infrastructure. Measured all-in per signal controlled:
about £75 in the mechanical era, £1,272 on the 1959-62 Kent Coast scheme, £2,250-3,434 today. The
box-to-posts ratio should be about 3:1 mechanical, 8-10:1 power and modern.

Electrification recommendations are per km of track and need **no** scaling correction, because a
way object spans a 125 m tile:

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| 750VDCRailCatenary | 69,000 → **2,500** | 400 → **5** |
| tram electrification | 69,000 → **2,000** | 400 → **5** |
| DC rail catenary | 157,000 → **5,000** | 500 → **8** |
| AC high speed catenary | 105,000 → **11,500** | 350 → **19** |
| third rail | 83,000 → **9,000** | 550 → **8** |
| fourth rail | 95,000 → **11,000** | 570 → **9** |
| third rail + DC catenary | 240,000 → **14,000** | 900 → **13** |
| third rail + AC catenary | 188,000 → **18,000** | 800 → **15** |

The inversion is fixed by these: historically, cost per track km *falls* from about £10,000 in
1925 to £4,600 young OLE, whereas the pakset has late electrification comparatively cheap.

### 3.7 Airports, power lines, elevated ways

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| runway | 182,500 → **151,000** | 1,063 → **250** |
| concrete runway | 392,500 → keep (concrete premium) | 1,950 → **~300** |
| taxiway | 109,500 → **67,000** | 638 → **110** |
| terminal | 2,500,000-2,700,000 → **2,720,000** | ~9,000 → **6,810** |
| hangar | — → **303,000** | — → **757** |
| control tower | — → **707,000** | — → **1,770** |
| power line | 35,000 → **68,000** | 25 → **2** |
| elevated way (concrete) | 1,456,000 → **505,000** | 149 → **420** |

Runways are the one family whose capital is already close: the present 182,500 against a
recommended 151,000.

## 4. The structural decisions

Four questions decide how the numbers above are applied, and none can be settled from the
research:

1. **Way = permanent way, or way + forge = whole line?** The evidence says the way object is
   permanent way (5.5-5.8% of whole-line capital, a ratio stable from 1830 to 1902). The present
   values sit at whole-line capital instead. Either lower the ways to the permanent-way figures
   and keep a small forge, or keep the ways and raise the forge to about 18,000. The tables above
   assume the first.
2. **Single-track or double-track basis for structures?** Almost all historical structures were
   double track. The forum's own convention was to halve them for the game. The tables above use
   the historical per-metre figures unhalved. Whichever is chosen must be applied to ways too.
3. **Motorway: way-only or delivered?** The way-only basis is consistent with structures being
   separate objects, and puts the motorway within 1.3× of the 2005 ITC per-lane-km figures. The
   delivered basis makes it 2.5× too cheap. This also decides whether the "motorway proves the
   chain" argument in [infrastructure-cost-findings](infrastructure-cost-findings.md) survives.
4. **Do way renewals belong in the revenue account?** You noted in 2022 that they are booked as
   capital in the game where reality charged them to revenue. That affects every cost-to-revenue
   ratio used in the original calibration.

## 5. Defects found in passing

- `ways/wooden-trestle-stone-pillar.dat` read `cost=cost=672000`. **Fixed** (`96cff9eed`).
- `ways/iron-arch-rail.dat` had `maintenance=15360`, exactly 1280 × 12. **Fixed** (`96cff9eed`).
- `ways/signals.dat` and `signals-narrow.dat` hold 168 objects with costs differing by 178× within
  one working method and era.
- All brick viaducts share one cost regardless of height, span or pillar spacing; all masonry
  aqueducts share one cost across three widths.
- The forum's Primrose Hill tunnel row gives 9,700 m for a tunnel of about 1,168 m, so its
  £12/m figure is a length artefact; the Islington canal tunnel row conflicts with the London &
  Birmingham evidence by a factor of about seventeen.
- Bus shelters, loading bays, bus terminals and all depots have no cost or maintenance line.
- Eight `.dat` files hold several `Obj=` blocks, so any audit keyed to one object per file reads
  only the first.

## 6. Gaps, and heuristics to fill them

| Gap | Suggested heuristic |
|---|---|
| Permanent-way cost 1900-1930 and after 1945 | Interpolate between the measured 1898, 1966 and 2000 anchors; treat the 1922 rail contract as a component check |
| Earthworks per km for a stated cross-section | Use the measured 9d-1s 3d per cubic yard and a stated depth; the L&M's £3,284/km is the heavy-grading check |
| Straight-sided retaining walls, modern | Use the Victorian £0.70-1.70/m² of wall face and scale by wall height |
| Structure maintenance by type where no account exists | Apply the measured relativities: brick 0.5× plain line, iron 1.2-1.5×, timber 7-8×, tunnel 1.5-2.5× |
| Dock and pier maintenance | Use 2-4% a year for timber and 0.8-1% for masonry and concrete |
| Hangars, terminals and towers before 1950 | Deflate modern £/m² on the `buildings` index; there is no measured pre-war figure |
| Total signalling cost per route km before 1909 | Use Rapier's 1874 model: 10 levers a mile, one box per 1.5 miles, 4.2 posts a km, about £315/route km |
| Contact-wire and conductor-rail renewal cost | Take 35-45% of new build for wire every 35-40 years, and 25-35% for conductor rail every 60-80 years |

## 7. What I would do first

In order of value per change, and in order of confidence in the evidence:

1. **The maintenance rule**, applied across every family. It is one decision, it is supported by
   every family, and it is the change that most affects play.
2. **`forge_cost_track` and `forge_cost_water`**, both an order of magnitude too high and both
   measurable.
3. **The masonry and brick structures**, which are the largest capital errors and the ones with
   the firmest anchors.
4. **The missing values** — shelters, depots and bus stops that are currently free.
5. **Signals**, but only after deciding what a signal object represents and how to express
   sub-unit maintenance.
