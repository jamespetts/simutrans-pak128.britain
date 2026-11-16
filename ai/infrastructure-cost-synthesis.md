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
[infrastructure-cost-evidence](infrastructure-cost-evidence.md) (the measured historical figures
by domain), [prices-infrastructure](prices-infrastructure.md) (the year index).

**This document is a record, not a decision.** The programme of work is to research each important
domain to this depth first, and only then derive the balance implications from the whole body of
research at once. The recommendations here are inputs to that later decision, and the figures may
change as other domains — revenue, vehicles, staff, fuel — are examined with the same rigour.

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

## 4. Decisions recorded, 2026-11-16

The pakset owner has settled the four questions. They are recorded here and nothing has been
applied to any `.dat` file.

**4.1 The way object is the permanent way alone.** The `.dat` cost of a way, netted of the forge
cost, represents the permanent way itself. The forge cost represents the *difference* between
renewing the permanent way on an already prepared bed and forging the way on virgin terrain. That
is the definition, and it is why the two are separate fields rather than one whole-line price. The
recommended way values in section 3.1 are therefore correct as they stand, and the forge is the
only part that changes with terrain.

**4.2 Track miles for the way, route miles for the forge.** For the permanent way, what counts is
track mileage, so where a historical statistic covers double track it is halved for a single-track
way object. For the forge, it is route mileage and must **not** be halved: the engine already
models the second track through the parallel-ways discount, which charges a reduced forge cost
when a parallel way of the same type already exists. Halving the forge as well would count the
saving twice.

The discount is in `bauer/wegbauer.cc`: when a neighbouring way of the same type is found,
`forge_cost` is multiplied by `parallel_ways_forge_cost_percentage` and divided by 100. The
values in `config/simuconf.tab` are: track 35, narrow gauge 35, road 50, water 75, monorail 35,
maglev 40, tram 85, air 85. `[CODE New ex-15 @ 96cff9eed]`

**4.3 A motorway tile is one carriageway.** Each way tile represents a single carriageway, so a
dual carriageway is built as two parallel roads, and the second attracts the 50% parallel-ways
forge discount. The way cost is the road surface; the roadbed, minor earthworks and formation are
in the forge cost. The "delivered against way-only" question in the previous draft of this
document was therefore the wrong question, and the way-only reading is correct.

**4.4 Renewals belong in the revenue account.** Historically, renewal was charged to revenue
rather than capital, and the game books it as capital. This will need an engine change in due
course, and it affects every cost-to-revenue ratio used in earlier calibration work.

## 5. Forge costs by way type

Section 4.1 establishes that each way type has its own forge cost, and `simuconf.tab` carries a
separate value for each of eight. These have now been researched. Values are 1900 pounds per
**route** kilometre; the setting is the pound figure multiplied by 2.523.

| Way type | Setting now | Recommended setting | Basis, 1900 prices |
|---|---|---|---|
| track | 15,000 | **760-1,010** | £110/km flat (1803), £253/km with fencing (1830), £250-400/km typical (1855-1900), up to £4,600/km in heavy terrain |
| narrow gauge | 10,000 | **760-1,140** | £250-450/km typical, £500-620/km for a Festiniog-type mountain line; terrain-dominated, not gauge-dominated |
| road | 7,500 | **2,500-3,800** | turnpike and macadam formation £50-250/km, modern asphalt roadbed £2,000-8,000/km. One value cannot fit both eras; the recommendation favours the early road |
| tram | 5,000 | **1,500-3,000** | £600-1,200/km, a street reservation sharing the road formation, so trench and concrete bed only |
| water | 25,000 | **3,000-4,500**, or 1,250 | see the definitional note below |
| air | 22,500 | **15,000-22,500** | £6,000-9,000/km formation, 30-40% of the pavement cost; the present value is already at the top of the range |
| monorail | 20,000 | **900-1,250** if a ground formation | no British historical basis |
| maglev | 20,000 | **900-1,250** if a ground formation | if these are elevated guideways the forge belongs with pier foundations instead |

**The canal definitional flag.** For a canal the formation — the cut, drainage, fencing, land
clearance — is large, at £1,200-2,200/km in 1900 prices, while the renewable element, re-puddling
and relining, is small. Under the definition in section 4.1 the formation belongs in the forge and
the way object should shrink to the renewal element. The present pakset has this reversed: the
canal way object carries the whole channel and the forge only a token. Either the water forge rises
to 3,000-4,500 and the canal way objects fall, or the way object keeps the whole channel and the
forge stays near 1,250. The two cannot both be right, and the meaning of the canal way object has
to be settled before either is changed.

**The parallel-ways percentages were tested as well.** Track 35%, road 50%, water 75% and air 85%
are all supported by the evidence on the marginal cost of a second parallel way. **Tram is not**:
because a second tram track shares the street formation, the marginal cost is nearer 40% than the
85% the pakset charges, so tramways are currently overcharged for doubling. Monorail and maglev
have no historical basis and should keep railway-like values.

Because the forge is the difference between renewing on a prepared bed and forging virgin terrain,
its value scales with the difficulty of the earthworks, not with the mode's traffic or capacity.
That is why a tramway's forge is far below a railway's, and why airfields, which are essentially a
levelling bill, are the highest of all.

## 6. Defects found in passing

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
| Contact-wire and conductor-rail renewal cost | Take 35-45% of new build for wire every 35-40 years, and 25-35% for conductor rail every 60-80 years |

## 8. The balance question

If these recommendations were applied as they stand, infrastructure costs would fall by roughly
ten to thirty times, and player lines that are already profitable under the interim balance would
become considerably more so. That is not a reason to abandon historical pricing, but it does mean
one of three things is true, and it is worth knowing which before anything is changed.

**Either the calibration is wrong somewhere.** The most likely candidate is not the chain but the
*scope* of the current values: the track ways sit at whole-line capital (about £21,800/km against
the historical £22,596/km) when the way object is meant to be permanent way alone (£1,300-1,900).
If the other parts of a line — land, structures, stations, terrain work — were calibrated on the
same whole-line assumption, then the present total for a complete line is far too high and the
profitability under the interim balance is a consequence of high revenue rather than correct costs.

**Or other costs are too low.** You recorded in 2022 that vehicle purchase and running costs
together are "about or even less than half in Simutrans what they are in reality", and that
unpowered rolling stock has had a zero per-kilometre cost since the interim rebalance. If
infrastructure falls by 20× while vehicle costs stay half of reality, the balance shifts further
than either change alone implies.

**Or the revenue calibration is too high.** The fare calibration used the 1844 Act maximum of
1d a mile; the real average third-class fare was nearer 0.55d, which is a factor of about 1.8 on
revenue, and you noted the possibility of halving fares with a steeper class gradient.

**The test that separates these** is not to compare individual objects with history but to cost a
complete representative line, all objects together, and compare the total with Acworth's
whole-line capital of £22,596 a kilometre and with the revenue a line of that era actually earned.
The historical ratios to match are roughly: capital about eight times annual gross receipts, and a
net return of 4-5% after working expenses. If the in-game total for a representative line is close
to £22,600/km then the components can be corrected without moving the balance; if it is much
below, the shortfall is elsewhere — most likely land, stations or vehicle costs.

I have not done that costing yet. It is the natural next analysis and it should precede any
`.dat` edit.

## 9. Headquarters as administrative overhead

A mechanism is needed before 15.x that requires a headquarters before a player can expand, with
the headquarters cost standing as a proxy for the general corporate and administrative overhead
that appears in the historical accounts. The present intention is that one headquarters is
required before building more than one depot, and that successively larger headquarters permit
progressively more depots.

The historical basis exists and should be researched rather than invented. The Railway Returns
carry a "general charges" heading — management, legal and audit, and general office costs —
separately from way and works, traffic and locomotive expenses. Acworth discusses the same
division. **Rates and taxes are excluded from this**, because the pakset already models taxation
separately through `corporation tax` in `config/prices.tab`, and counting them here would charge
the same thing twice.

The figure needed is general charges per route mile per year, by era, and the cost of the
headquarters buildings themselves, which the existing depot and station figures bound but do not
measure.

### What the research found

General charges, with rates and taxes excluded, are remarkably stable as a share of gross
receipts across a century:

| Source | Year | General charges as % of receipts |
|---|---|---|
| Great Western | 1838-40 | 5.84 |
| Cheshire Lines Committee | 1874 | 4.47 |
| Metropolitan | 1893-1900 | 3.6-4.2 |
| London, Tilbury and Southend | 1896-1902 | 5.2 |
| East London Railway Joint Committee | 1930-36 | 3.28 |
| British Railways "General" | 1955 and 1958 | 3.2-4.1, upper bound |

The company figures come from accounts that already carry rates and taxes under a separate
heading, so they are clean for this purpose. The British Railways figures do not clearly separate
the two and must be stripped before use.

Applied to the receipts implied by Acworth's capital figure — capital about eight times gross
receipts, so about £3,500 a route kilometre a year in 1900 prices — general charges come to
**about £175 per route kilometre per year, range £140-210**. That is the figure the headquarters
mechanism should stand as proxy for. It is stable enough that one value serves most of the
timeline.

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
1990 — the parochial assessment system, the 1844 and 1858 Acts, the Railway and Canal Traffic Act
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
