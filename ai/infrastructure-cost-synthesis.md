---
status: draft
verified: New ex-15 @ 96cff9eed (working tree); simutrans-extended ex-15 @ 22cc3af
---
# Infrastructure cost synthesis

**Covers**: eight research tasks on the capital and maintenance cost of every infrastructure object
family, their conversion to `.dat` values, and the decisions that remain. No `.dat` value has been
changed except the two bugs in section 6.

Companions: [infrastructure-base-costs](infrastructure-base-costs.md) (the conversion chain),
[infrastructure-cost-findings](infrastructure-cost-findings.md) (first-pass audit),
[infrastructure-cost-evidence](infrastructure-cost-evidence.md) (measured figures),
[prices-infrastructure](prices-infrastructure.md) (year index).

**Figures recomputed 2026-11-17** for the interface's division of engine money by 100 before display:
a raw `.dat` unit is £0.00396311, not £0.396311. Factors: `.dat` × **0.00396311** for way, bridge,
tunnel, way-object and forge capital per kilometre, and `.dat` × **0.00792622** for way maintenance
per kilometre per month (× 12 for the year), which is twice the capital factor because
`calc_adjusted_monthly_figure` applies to the maintenance charge; `.dat` × **0.00049539** for a
scaled one-tile object and **0.00396311** for an unscaled one. Derivation and the code path:
[infrastructure-base-costs](infrastructure-base-costs.md), confirmed in
[balance-conversion-check](balance-conversion-check.md). Ratios stand; levels moved, and the
conclusions with them: infrastructure capital is too cheap, while maintenance is close to the
measured range.

## 1. The scaling map

From `simworld.cc` (`karte_t::set_scale`) and `obj/roadsign.cc` at `22cc3af`:

| Class | Scaled by | `.dat` value for a real £X |
|---|---|---|
| Ways, tunnels, bridges, way objects | `meters_per_tile/1000` = 0.125 | £/km × 252.3 |
| Station buildings, platforms, signalboxes, signals, industries | 0.125 | £ per object × 2,019 |
| Depots, headquarters, city buildings, attractions | not scaled | £ per object × 252.3 |

Three research returns used the per-kilometre formula for per-object classes, so signals, station
buildings and signalboxes were **eight times too small**. `[CODE New ex-15 @ 96cff9eed]`

## 2. The cross-cutting finding: maintenance carries renewal

The maintenance column appears built from accounts that combine routine maintenance with renewal,
which Simutrans charges separately through `weg_t::renew()` when wear runs out.

| Source, date | Figure, 1900 prices |
|---|---|
| BR 1966, track maintenance excluding renewal | £44/km/year |
| ORR 2015-16, track maintenance excluding renewal | £334/km/year |
| Cudworth 1886, brick viaduct upkeep | £0.05/m/year |
| Cudworth 1886, iron viaduct upkeep | £0.23-0.25/m/year |
| Plain line upkeep, various 1839-1902 | £0.05-0.31/m/year |
| Canal routine upkeep, 1938 | £62/km/year |

The rule is **single, not object by object**: strip renewal out of every maintenance value. At the
corrected rate `wssr` capital is **£218 a km**, six to nine times below the measured £1,300-1,900,
while its maintenance is **£52 a km a year** (550 × 0.00792622 × 12), which sits just inside the
measured £44-334 range rather than below it; `wssri_intermediate` capital is **£416**.

## 3. Decision tables

"Now" is the current `.dat` value; every recommended value is 100 times the pre-correction draft's.

### 3.1 Track ways

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| waggonway | 3,250 → **105,000** | 400 → **1,000** |
| plateway | 10,000 → **195,000** | 600 → **500** |
| cast_iron | 30,000 → **165,000** | 800 → **500** |
| wrought_iron_fishbelly | 30,000 → **150,000** | 755 → **600** |
| wrought_iron_light | 32,000 → **185,000** | 750 → **800** |
| wrought_iron_intermediate | 36,000 → **215,000** | 725 → **1,000** |
| wrought_iron_track | 40,000 → **255,000** | 700 → **1,100** |
| wrought_iron_improved | 46,500 → **280,000** | 610 → **1,200** |
| wssr-early | 52,000 → **315,000** | 575 → **1,300** |
| wssr | 55,000 → **320,000** | 550 → **1,300** |
| wssr_light | 32,000 → **250,000** | 375 → **900** |
| wssri | 75,000 → **360,000** | 500 → **1,400** |
| wssri_intermediate | 90,000 → **370,000** | 450 → **1,500** |
| wssri_light | 45,000 → **305,000** | 360 → **1,100** |
| wssri_heavy | 135,000 → **240,000** | 650 → **1,800** |
| cssr_light | 105,000 → **265,000** | 200 → **3,500** |
| cssr | 140,000 → **325,000** | 375 → **4,000** |
| cssri-125 | 150,000 → **420,000** | 575 → **5,000** |
| tgv | 250,000 → **2,400,000** | 950 → **3,500** |
| cssri | 175,000 → **850,000** | 630 → **6,000** |

`forge_cost_track`: **15,000 → 76,000-101,000** (£301-400 a route km, against measured formation of
£110-400/km; the present 15,000 is £59/km).

Only `wssri` £1,427, `wssri_intermediate` £1,466 and `cssri-125` £1,664 land inside the measured £1,300-1,900; seven steel-rail rows fall to £951-1,288 and `cssri` and `tgv` rise to £3,369-9,511.

### 3.2 Roads

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| bridleway | 1,600 → **12,000** | 8 → **100** |
| dirt-road | 2,000 → **20,000** | 16 → **200** |
| improved_road | 2,200 → **50,000** | 120 → **300** |
| macadam_road | 13,000 → **300,000** | 70 → **500** |
| cobblestone-road | 6,500 → **650,000** | 250 → **6,000** |
| tarmac_road | 40,000 → **500,000** | 400 → **600** |
| tarmac_city_road | 35,000 → **700,000** | 350 → **5,000** |
| concrete_road | 110,000 → **8,000,000** | 175 → **3,500** |
| city-road | 75,000 → **9,000,000** | 425 → **4,500** |
| motorway | 190,000 → **25,000,000** | 625 → **7,000** |
| hr-asphalt heavy / medium / light | 92,000 / 80,000 / 73,000 → **11,000,000 / 7,500,000 / 4,500,000** | 425 → **4,500 / 3,500 / 3,000** |

Rows near-unchanged in the old draft now rise: `cobblestone-road` 100 times, `city-road` 120,
`motorway` 132.

### 3.3 Bridges, viaducts, tunnels

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| masonry-viaduct | 5,120,000 → **25,000,000** | 205 → **5,500** |
| brick-viaduct | 4,480,000 → **21,500,000** | 205 → **5,000** |
| iron-viaduct | 1,200,000 → **20,000,000** | 960 → **9,500** |
| iron-girder-bridge | 1,904,000 → **30,000,000** | 1,269 → **9,500** |
| iron-lattice-girder | 2,160,000 → **38,000,000** | 1,269 → **9,500** |
| tubular-box-girder | 1,980,000 → **280,000,000** | 1,269 → **10,500** |
| iron-arch-rail | 4,480,000 → **75,000,000** | 1,280 → **10,000** |
| beam-bridge | 3,120,000 → **30,000,000** | 1,269 → **9,500** |
| plate-girder | 2,760,000 → **38,000,000** | 1,269 → **9,500** |
| steel-truss | 2,520,000 → **88,000,000** | 1,269 → **11,000** |
| wooden-trestle | 672,000 → **16,500,000** | 4,480 → **10,500** |
| concrete-viaduct | 1,456,000 → **33,000,000** | 149 → **5,500** |
| RailTunnelStone / Brick | 2,200,000 / 2,700,000 → **21,500,000** | 3,000 / 4,400 → **7,500** |
| severn-tunnel | 2,250,000 → **100,000,000** | 5,250 → **15,000** |
| RailTunnelConcrete | 3,000,000 → **42,000,000** | 4,000 → **10,000** |
| SubSurfaceRailTunnelBrick | 2,000,000 → **30,000,000** | 4,000 → **7,500** |
| LT_Tunnel | 775,000 → **15,000,000** | 1,375 → **9,500** |

Timber runs 7-8 times plain line upkeep, brick about half, iron 1.2-1.5 times.

### 3.4 Canals, aqueducts, piers

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| canal_tubboat | 9,000 → **280,000** | 75 → **800** |
| canal_narrowboat | 15,000 → **480,000** | 100 → **1,100** |
| canal (barge) | 30,000 → **885,000** | 200 → **1,300** |
| canal-lined | 45,000 → **1,160,000** | 150 → **1,100** |
| canal_ship | 240,000 → **5,050,000** | 250 → **2,100** |
| canal_largeship | 2,500,000 → **68,630,000** | 300 → **3,300** |
| masonry-aqueduct tub/narrow/barge | 5,120,000 → **27,800,000 / 39,100,000 / 53,000,000** | 205 → **12,600 / 17,900 / 24,400** |
| brick-aqueduct tub/narrow/barge | 4,480,000 → **21,400,000 / 30,300,000 / 41,600,000** | 205 → **12,600 / 17,700 / 24,400** |
| concrete-aqueduct tub/narrow/barge | 1,456,000 → **11,400,000 / 15,600,000 / 21,400,000** | 149 → **9,500 / 13,000 / 17,900** |
| piers, timber / iron / brick-stone / concrete | → **5,000,000 / 8,800,000 / 27,800,000 / 13,900,000** | → **14,700 / 14,700 / 18,500 / 11,600** |

`forge_cost_water`: **25,000 → 100,000** (or 50,000 if `way + forge` must equal the anchor exactly).
At 25,000 it charges £99/km, more than a narrow canal's way cost (£59/km).

### 3.5 Stations, platforms, shelters, depots

These are scaled as buildings, so the `.dat` values carry the ×2,019 factor.

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| wooden platform | 75,000 → **760,000** | 4,000 → **3,200** |
| brick platform | 180,000 → **1,510,000** | 2,700 → **1,900** |
| concrete platform | 250,000 → **1,310,000** | 2,250 → **2,200** |
| wooden station building | 250,000 → **1,010,000** | 11,000 → **3,400** |
| brick or stone building | 800,000-850,000 → **1,510,000** | 10,000-11,800 → **1,500** |
| concrete small building | 615,000 → **1,110,000** | 8,000 → **1,400** |
| staging post / bare bus stop | 4,000 / 8,500 → **10,400** | 400 → **20** |
| old bus shelter (timber) | none → **121,000** | none → **700** |
| modern bus shelter | none → **51,000** | none → **130** |

The evidence gives timber 4-8% of capital a year in maintenance, brick 0.8-1.5%, concrete 1.5-2.5%; the recommendations meet that, the present values, with concrete below brick, do not.

Bus shelters, loading bays, bus terminals and every depot have **no cost line**: `cost_depot_rail` =
2,000 implies **£7.93**, against £3,973 for the Tilbury shed and £20,390 for Plaistow. Suggested
1,000,000 rail and 500,000 road.

### 3.6 Signals, signalboxes, electrification

Signals and signalboxes are scaled per object. A semaphore post with its share of the wires is £15-18
(1912), a colour-light head £85-160, and the 1909 figure of £100 an arm stands. One maintenance unit
is now **£0.0059 a year**, so a post's upkeep is expressible: "the field must be 0 or 1" is void.

Signalboxes carry the signalling infrastructure: about £75 all-in per signal controlled in the
mechanical era, £1,272 on the 1959-62 Kent Coast scheme, £2,250-3,434 today, on a box-to-posts ratio
of about 3:1 mechanical and 8-10:1 power and modern.

Electrification is per km of track and takes the same rate:

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| 750VDCRailCatenary | 69,000 → **250,000** | 400 → **500** |
| tram electrification | 69,000 → **200,000** | 400 → **500** |
| DC rail catenary | 157,000 → **500,000** | 500 → **800** |
| AC high speed catenary | 105,000 → **1,150,000** | 350 → **1,900** |
| third rail | 83,000 → **900,000** | 550 → **800** |
| fourth rail | 95,000 → **1,100,000** | 570 → **900** |
| third rail + DC catenary | 240,000 → **1,400,000** | 900 → **1,300** |
| third rail + AC catenary | 188,000 → **1,800,000** | 800 → **1,500** |

These convert to £793-7,134 a track km; history falls from £10,000 in 1925 to £4,600 for young OLE,
and the pakset has the reverse order (750 V DC 69,000, AC 105,000), which the recommendations keep.
Only the two third-rail-plus-catenary values reach the £4,600-10,000 band; the 750 V DC catenary at
£991 is ten times below the 1925 anchor.

### 3.7 Airports, power lines, elevated ways

| Object | Cost now → recommended | Maintenance now → recommended |
|---|---|---|
| runway | 182,500 → **15,100,000** | 1,063 → **25,000** |
| concrete runway | 392,500 → **39,250,000** (2.15× premium, inference) | 1,950 → **30,000** |
| taxiway | 109,500 → **6,700,000** | 638 → **11,000** |
| terminal | 2,500,000-2,700,000 → **272,000,000** | ~9,000 → **681,000** |
| hangar | — → **30,300,000** | — → **75,700** |
| control tower | — → **70,700,000** | — → **177,000** |
| power line | 35,000 → **6,800,000** | 25 → **200** |
| elevated way (concrete) | 1,456,000 → **50,500,000** | 149 → **42,000** |

Runways were called the family already close to history, but that compared the raw `.dat` 182,500 with
a recommendation 100 times too small: at the corrected rate the runway is £723 a km against £59,843.

## 4. Decisions recorded, 2026-11-16

Nothing has been applied to any `.dat` file.

- **4.1 The way object is the permanent way alone.** Netted of the forge, the `.dat` cost is the
  permanent way; the forge is the *difference* between renewing on a bed and forging on virgin terrain.
- **4.2 Track miles for the way, route miles for the forge.** Double-track statistics are halved for a
  single-track way object but not for the forge, because the engine already models the second track
  through the parallel-ways discount in `bauer/wegbauer.cc`.
- **4.3 A motorway tile is one carriageway**, the way cost being the road surface; roadbed and
  formation are in the forge, and the second road of a dual carriageway takes the 50% discount.
- **4.4 Renewals belong in the revenue account**, not in capital; the game books them as capital,
  which needs an engine change and affects every earlier cost-to-revenue ratio. `[CODE 96cff9eed]`

## 5. Forge costs by way type

Values are 1900 pounds per **route** kilometre; the setting is the pound figure × 252.3.

| Way type | Setting now | Recommended setting | Basis, 1900 prices |
|---|---|---|---|
| track | 15,000 | **76,000-101,000** | £110/km flat (1803), £253/km with fencing (1830), £250-400/km typical (1855-1900), up to £4,600/km in heavy terrain |
| narrow gauge | 10,000 | **76,000-114,000** | £250-450/km typical, £500-620/km for a Festiniog-type mountain line; terrain-dominated, not gauge-dominated |
| road | 7,500 | **250,000-380,000** | turnpike and macadam formation £50-250/km, modern asphalt roadbed £2,000-8,000/km. One value cannot fit both eras; the recommendation favours the early road |
| tram | 5,000 | **150,000-300,000** | £600-1,200/km, a street reservation sharing the road formation, so trench and concrete bed only |
| water | 25,000 | **300,000-450,000**, or 125,000 | see the definitional note below |
| air | 22,500 | **1,500,000-2,250,000** | £6,000-9,000/km formation, 30-40% of the pavement cost; the present value is 67 to 100 times below the range |
| monorail | 20,000 | **90,000-125,000** if a ground formation | no British historical basis |
| maglev | 20,000 | **90,000-125,000** if a ground formation | if these are elevated guideways the forge belongs with pier foundations instead |

**The canal definitional flag.** The formation — cut, drainage, fencing, land clearance — is large at
£1,200-2,200/km; re-puddling is small. Section 4.1 puts the formation in the forge, yet the pakset puts
the whole channel in the way object: either the water forge rises to 300,000-450,000, or stays at 125,000.

**Parallel ways.** Track 35%, road 50%, water 75% and air 85% hold on the marginal cost of a second way; tram does not, at nearer 40% than 85%.

**Definitional choice, 2026-11-22.** Heavy earthworks are **excluded** from the forge by user
direction: cuttings and embankments are made with the raise/lower land tool, not the forge. The
forge is bed preparation only, which is the £250-400/km band behind the track recommendation (the
1840 Midland Counties heavy earthworks were about £3,200/km, matching the L&M figure, and are not
in the forge). The recommended settings were applied on 2026-11-22 as the midpoints of the ranges
above: track 88,000, narrow gauge 95,000, road 315,000, tram 225,000, water 125,000, air
1,875,000, monorail and maglev 108,000. `[USER-DIRECTION:2026-11-22]`
`[LITERATURE:research-pricing-report-3.md §4.5]`

## 6. Defects found in passing

- `ways/wooden-trestle-stone-pillar.dat` read `cost=cost=672000`, and `ways/iron-arch-rail.dat` had
  `maintenance=15360`, exactly 1280 × 12. **Both fixed** (`96cff9eed`).
- `ways/signals.dat` and `signals-narrow.dat` hold 168 objects with costs differing by 178×; all brick
  viaducts share one cost regardless of height, span or spacing.
- The forum's Primrose Hill tunnel row gives 9,700 m for a tunnel of about 1,168 m, so its £12/m
  figure is a length artefact; the Islington canal tunnel row conflicts with the London &
  Birmingham evidence by a factor of about seventeen.
- Eight `.dat` files hold several `Obj=` blocks, so any audit keyed to one object per file reads
  only the first.

## 7. Gaps, and heuristics to fill them

| Gap | Suggested heuristic |
|---|---|
| Permanent-way cost 1900-1930 and after 1945 | Interpolate between the measured 1898, 1966 and 2000 anchors; treat the 1922 rail contract as a component check |
| Earthworks per km for a stated cross-section | Use the measured 9d-1s 3d per cubic yard and a stated depth; the L&M's £3,284/km is the heavy-grading check |
| Straight-sided retaining walls, modern | Use the Victorian £0.70-1.70/m² of wall face and scale by wall height |
| Structure maintenance by type where no account exists | Apply the measured relativities: brick 0.5× plain line, iron 1.2-1.5×, timber 7-8×, tunnel 1.5-2.5× |
| Dock and pier maintenance | Use 2-4% a year for timber and 0.8-1% for masonry and concrete |
| Hangars, terminals and towers before 1950 | Deflate modern £/m² on the `buildings` index; there is no measured pre-war figure |
| Total signalling cost per route km before 1909 | Use Rapier's 1874 model: 10 levers a mile, one box per 1.5 miles, 4.2 posts a km, about £315/route km |
| Contact-wire and conductor-rail renewal | 35-45% of new build for wire every 35-40 years, 25-35% for conductor rail every 60-80 years |

## 8. The balance question

If applied, these recommendations would make infrastructure dearer: capital rises by about 2 to 500 times the present `.dat` values, maintenance by 0.05 to 280 times, so profitable lines become less so.

**The earlier explanation fails.** The track ways were said to sit at whole-line capital, about
£21,800 a km against Acworth's £22,596. At the corrected rate they are **£218 a km**: a hundred times
below Acworth and six to nine times below the £1,300-1,900 of permanent way alone.

**What remains** is that other costs are too low — vehicle purchase and running together are, you
recorded in 2022, "about or even less than half in Simutrans what they are in reality" — or that
revenue is too high: fares were calibrated on 1d a mile against a real average near 0.55d.

**The test** is to cost a representative line against Acworth's £22,596 a kilometre and the revenue it
earned: capital about eight times gross receipts, a net return of 4-5% after working expenses.

## 9. Headquarters as administrative overhead

General charges — management, legal, audit, office — run 3.3-5.8% of receipts (Great Western 5.84%,
1838-40; Cheshire Lines 4.47%, 1874; Metropolitan 3.6-4.2%, 1893-1900; Tilbury 5.2%, 1896-1902; East
London 3.28%, 1930-36; British Railways 3.2-4.1%, 1955-58). On Acworth's eight times gross receipts,
about £3,500 a route kilometre a year, they come to **about £175 per route kilometre per year, range
£140-210** - the figure a required headquarters should stand as proxy for. `corporation tax` already
models taxation, so rates and taxes are excluded.

**The headquarters building cost itself could not be established.** No free source gives a
construction cost for a British railway head office, divisional office or district office. The
nearest anchors are a combined offices-and-works figure of £62,000 at Derby in 1839, a training
college at £50,000 in 1937, and a United States office block at about £72,000 in 1882. Since the
overhead is an annual charge and the building is a capital one, the mechanism may not need a
measured building price at all: a nominal building cost plus the £175 a kilometre a year standing
charge would represent the overhead more honestly than a large building price pretending to be
the whole of it.

### Open question: property rates

Railway companies paid rates on the assessed value of their land, buildings and works. This was a
large item, quite separate from tax on profit, and its basis changed repeatedly between 1840 and
1990 - the parochial assessment system, the 1844 and 1858 Acts, the Railway and Canal Traffic Act
period, derating in 1929, and the move to a national formula after 1948.

Modelling those changes is not practical, and a series of rates that ignored them would be worse
than no series. The alternative is to fold a representative rates charge into the headquarters
overhead, so that the player pays something for the burden without the game attempting to model
its changing basis.

That choice interacts with `corporation tax`, which is already a rate on profit: folding property
rates into the overhead would charge a second, differently based tax on the same business, which
is defensible historically but must be documented rather than accidental. Whether to do it, and if
so which era's basis to use as the representative level, is left open.

This belongs in the same body of work as the cost audit: it is a real cost that the game does not
currently charge, and it may account for part of the balance gap in section 8.

## 10. What I would do first

1. **The maintenance rule**, across every family.
2. **`forge_cost_track` and `forge_cost_water`**, both an order of magnitude too **low** now.
3. **The masonry and brick structures**, five times too low, then the free shelters and depots.
4. **Signals**, once a signal object's meaning is settled.
