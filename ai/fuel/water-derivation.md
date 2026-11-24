# Ship fuel consumption - water sector (341 objects, 75 models)

Researched for the `fuel_per_km` / `calibration_speed` / `cut_off_speed` fields. Nothing in
`New/` was modified. Every figure below is either taken from a named source, derived by the
arithmetic shown, or labelled `ESTIMATE` with its anchor.

## 1. Method

### 1.1 What the 341 objects actually are

The water checklist is not 341 ships. It is 341 *vehicles*, and the pakset splits most hulls
into a propulsion unit plus one or more bolt-on payload modules:

| Kind | Objects | What they are | `engine_type` | Fuel |
|---|---|---|---|---|
| Self-propelled hulls and complete ships | 156 | carry an engine, or a sailing rig | 26 sail, 55 steam, 61 diesel, 8 bio, 6 petrol | per sections 1.4-1.8 |
| Payload hold modules | 134 | `Constraint[Prev]` on a hull; `length=1`; carry freight or passengers only | 64 `sail`, 70 none | **0** |
| Independent unpowered / towed craft | 51 | dumb barges, tub boats, flyboats, box boats, market boats, unpowered narrowboats, `TugBarge*` | none | **0** |

The checklist counts 220 objects as sail/diesel/steam/bio/petrol: 90 `sail`, 61 `diesel`, 55
`steam`, 8 `bio`, 6 `petrol`. Of the 90 `sail` objects, **26 are sailing hulls** (`BrigHull`,
`SchoonerHull`, `ClipperHull`, `EastIndiamanHull`, `BlackwallFrigateHull`, `WindjammerHull`,
`Dogger`, `Fifie`, `HumberKeel*` x6, `NorfolkWherry*` x7, `ThamesSailingBarge*` x5) and **64 are
sail-rigged hold modules** (`BrigAdd*`, `ClipperAdd*`, `EastIndiamanAdd*`, `SchoonerAdd*`,
`WindjammerAdd*`, `BlackwallFrigateAdd*`, `CarferryAdd*`, `humber-keel-mail-hold`). The sail
holds carry `engine_type=sail` only so that they can be attached to a sailing convoy; they have
no propulsion and get 0.

The 70 hold modules with no `engine_type` are the object families named `...AddPax`, `...AddBulk`,
`...AddMail`, `...AddCool`, `...AddPiece`, `...AddLong`, `...AddOil`, `...AddLivestock`, `...AddCar`,
`...AddPax-first-class`, `...AddPax-second-class`, plus `(AddMail)` in `boats192`/`boats224`, plus
`ferry-mail`, `mail-space`, `MarketBargeAddMail`, `MarketNarrowboatAddMail`,
`PacketBargeAddMail`. So there are 134 hold modules in all, and 219 of the 341 objects get
`fuel_per_km=0`; only 122 objects (55 steam, 61 diesel, 6 petrol) are fuelled.

**Fuel goes only on the object that has the `engine_type` and its own `power` field.** The holds
are set to 0. This matters because a convoy is charged fuel per vehicle: if a hold also carried
a figure, a 9-hold East Indiaman would be charged nine times.

### 1.2 Units and the calibration convention

`fuel_per_km` is in **grams of coal/km** for coal-fired steam and **millilitres of liquid
fuel/km** for diesel, petrol and oil-fired steam, per section 3 of the brief. `calibration_speed` is
the pakset `speed` of each object; `cut_off_speed` is half that.

The brief's engine model makes `base x calibration_speed` the fuel burned per hour at full
output, and the split between the two factors is arithmetically irrelevant. I set
`calibration_speed` to the pakset speed and then set `fuel_per_km` to the fuel the ship actually
burns per km **at that speed in service**. That is the correct choice for ships because:

* the pakset `speed` is the maximum speed the ship can reach in the game, and `is_at_full_power()`
 is true at maximum physical speed, so the base figure is charged in full whenever the ship is
 running at its coded speed;
* a ship's coded service speed is well below the speed at which its engines develop maximum
 continuous rating (typically service speed is 80-85% of trial speed, and propeller power
 varies as the cube of speed, so service power is 50-60% of MCR);
* therefore "full output at calibration speed" would *overstate* the fuel a ship burns by a
 factor of nearly two if "full output" were read as MCR.

So the physical quantity I research is **fuel per hour at the coded service speed**, and
`fuel_per_km = (fuel per hour) / (coded speed in km/h)`. This also means that any documented
"tons of coal per day at X knots" converts directly, exactly as the brief says:
`tons/day / (speed x 24)`.

Worked unit check (proves the ml/km convention and the /1000 divider):
a 30 L/100 km bus is `fuel_per_km = 300`. Diesel in 2000 is 15,839 units = 82.5p/l, so cost/km =
300 x 15,839 / 1000 = 4,752 Simucents = 4,752 x GBP 0.00005208 = **GBP 0.2475/km**, and 0.30 l/km x
82.5p = GBP 0.2475. Exact.

### 1.3 Coal-fired steam: the specific-consumption series

`g coal/km = ihp x LF x C x 453.592 / speed_kmh`, where `C` is lb of coal per indicated
horsepower-hour and `LF` is the fraction of rated power actually developed at the coded speed.

`C` is taken from measured returns, not from a guess:

| Year | lb coal/ihp-h | Source and what it measures |
|---|---|---|
| 1840 | 5.1 | SS *Britannia*, 710 ihp at 8.5 kn, North Atlantic service (Ocean Steamships, 1891, table "Coal per indicated horse-power per hour") |
| 1856 | 3.8 | SS *Persia*, 3,600 ihp at 13.1 kn, same table |
| 1872 | 2.11 | fleet average, 28 ships (Marshall's 1881 return, tabulated in *A Review of Marine Engineering*, 1891, Table 6) |
| 1881 | 1.828 | same return, Table 6 |
| 1889 | 1.0 | tug *Oceania*, 900 ehp, "one pound per HP per hour" (Simutrans forum thread, post #39) |
| 1890 | 2.0 | tug *Nubia*, 350 ihp triple expansion, "two pounds per HP per hour" (same post) |
| 1891 | 1.522 | average of 28 three-stage expansion engines at sea, same paper, Table 5 |
| 1893 | 1.76-2.2 | tri-compound battleship at 7-55% of designed power (US Naval Institute *Proceedings*, 1893, "Coal Consumption of Ships of War") |
| 1907 | 2.84 | ferry *Kookooburra*, 427 ihp at 11.1 kn, measured coal weighings (Engineering Association of NSW, trial report) |

Two series are interpolated from these points: a **deep-sea** series (the measured fleet
averages, 1840-1950) and a **small-craft** series 55-75% higher, because small engines,
short steam passages and indifferent firing gave away most of the gain that the big plants
made. The small-craft series is anchored on the 1890 *Nubia* (2.0) and 1907 *Kookooburra*
(2.84) measurements. Ships between 600 and 2,500 ihp take a 35/65 blend of the two.

**Load factor LF.** For reciprocating steamers 0.60; for the small craft whose coded speed is far
below the engine's rated speed (puffers, tugs, narrowboats, launches) 0.50; for turbine steamers,
which run near full power at service speed, 0.75. The 0.60 is the propeller law at a service
speed 15% below the speed at which MCR is developed: (0.85)^3 = 0.61.

**Validation.** SS *Great Western* (1838) is independently documented: she sailed Bristol-New
York in 15 days 5 hours on 400 of her 600 tons of coal, i.e. 26.3 t/day at about 8.2 kn.
This method gives 59,990 g/km x 20 km/h x 24 / 1,016,000 = **28.3 t/day**. Agreement is within
8%. That is the single best check available on the whole steam method, and it lands.

### 1.4 Oil-fired steam - flagged separately

One object is an oil-fired steam turbine coded `steam`: **`BTCLordWarden`** (1951, 11,900 kW of
Parsons turbines). A second, `SRInvicta`, was coal-fired when built in 1939 and converted to oil
in 1946; it is modelled as coal because that is what it burned for most of its life, but the
orchestrator should be aware.

`BTCLordWarden` is given in **millilitres of oil per km**, not grams of coal:
`shp x LF x 0.90 lb oil/shp-h x 453.6 / 0.84 kg/l / speed`. 0.90 lb/shp-h is the mid-point of the
0.8-1.0 lb/shp-h band for oil-fired marine steam plant. **Its `fuel_per_km` is on a different
unit from the other 34 steam models.** If it is applied with `engine_type=steam` the engine will
price the millilitres against the coal series and undercharge by a wide margin; either recode
the object as `diesel` (it burns oil, and the diesel series is a per-litre series) or accept a
wrong price. Flagged in section 4 as well.

### 1.5 Diesel

`ml/km = kW x LF x SFC (g/kWh) / 0.84 kg/l / speed_kmh`. Diesel density 0.84 kg/l.

Specific fuel consumption, from manufacturers' published data:

* modern slow-speed two-stroke: 163-176 g/kWh at 100% MCR (MAN B&W G/S-series, *Marine engine
 programme* 2025); 162 g/kWh at 70% load (MAN 8G95ME-C9.5 part-load table)
* modern medium-speed four-stroke: 169 g/kWh (Wärtsilä 31, best in class); 176 g/kWh in diesel
 mode for the dual-fuel version
* auxiliary / older medium-speed: 190-217 g/kWh (MAN auxiliary-engine table)

I use 175-180 for 2000s medium-speed and slow-speed plant, 185-195 for 1980s-90s, 205-215 for
1950s-70s, 240-260 for 1930s-50s, 280 for 1920s small diesels and 300 for 1905-1920 hot-bulb
semi-diesels (which were genuinely inefficient).

Load factors: 0.75 for ocean motor ships, 0.80 for fast craft whose coded speed is near trial
speed, 0.65 for conventional ferries and motor ships at service speed, 0.60 for small harbour
and estuarine craft, 0.40 for canal craft whose rated power is far above what the waterway
allows them to use.

**Validation.** *Handysize* bulk carrier: 6,100 kW x 0.75 x 180 g/kWh = 823.5 kg/h = 980 l/h,
which is 19.8 t/day at 13.5 kn - the expected 20-25 t/day for a 30,000 dwt handysize. A 30 kW
narrowboat gives 4.0 l/h at the coded 8 km/h; the measured canal figure is 1.0-1.5 l/h at
3 mph (4.8 km/h), and 4.0 l/h is what 12 kW at 8 km/h implies, consistent with the measured
2-3.5 kW at 2.5-2.8 mph once the speed difference is cubed.

### 1.6 Petrol

`ml/km = kW x LF x 300 g/kWh / 0.74 kg/l / speed`. 300 g/kWh is a 1980s-2000s spark-ignition
figure. All six petrol objects are hovercraft (AP1-88, BHT-130, BHT-150); 894-900 kW at 90 km/h
gives 308 l/h, which matches the published ~300 l/h of an AP.1-88.

### 1.7 Sail, bio, holds and unpowered craft

`fuel_per_km = 0`. `fuel[sail]` and `fuel[bio]` are 0 in `fuel.tab`, and the pakset's design note
says fodder is carried in maintenance. Bio covers the two horse boats and the six skiff-wherries.

### 1.8 Sanity check against `runningcost`

The check in section 3 of the brief was run for every powered model, using the real `fuel.tab`
series at each object's intro year. Fuel cost per km in Simucents is
`fuel_per_km * fuel_tab_value / 1000`; `runningcost` is in the same units.

| Traction | models | ratio fuel/maintenance: min | median | max |
|---|---|---|---|---|
| coal steam | 34 | 0.26 | 1.6 | 8.2 |
| oil steam | 1 | 22 | 22 | 22 |
| diesel | 37 | 8.6 | 458 | 12,322 |
| petrol | 3 | 1,120 | 1,138 | 1,138 |

**The coal steamers land exactly where the brief says they should**, which is independent
evidence that the steam arithmetic and the gram/km convention are right.

**The liquid-fuel ships do not, and the reason is the pakset's ship `runningcost`, not the fuel
figure.** Worked example, `SealinkHorsa` (1972, runningcost 863, fuel 38,707 ml/km, diesel 1,561
units = 8.1p/l): fuel cost = 38,707 x 1,561 / 1000 = 60,422 Simucents/km = GBP 3.15/km. Check
against the physical figure: 38.7 l/km x 8.1p/l = GBP 3.13/km. The fuel number is right. The
runningcost of 863 Simucents is GBP 0.045/km, which is not a plausible maintenance cost for an
18-knot cross-Channel ferry. Every diesel ship in the set shows the same pattern, and the
biggest ratios (HSS-1500 12,322; Incat74m 6,714; POSuperEuropeanMixed 3,000+) come from the
runningcosts, which are mutually inconsistent: `Incat74m` has runningcost 46 against
`Incat112m` 963 for two similar fast ferries.

Two further structural reasons why ships are not like road vehicles here:

* `fuel.tab` prices liquid fuel at **road diesel** prices, while ships burn marine gas oil or
 heavy fuel oil at roughly a third to a fifth of that price per litre. The physical figure in
 litres is right; the price attached to it is high.
* real shipping has fuel at 50-70% of voyage cost, so a fuel figure that dwarfs maintenance is
 the correct direction of error.

Recommendation: apply the physical figures and treat the ship `runningcost` values as a separate
balancing problem. If the orchestrator instead wants ships to keep roughly their present
fuel:maintenance ratio, the whole diesel set would have to be scaled by about 1/50, which would
make a Handysize burn 0.4 t of fuel a day and is not defensible.

### 1.9 Power figures

The pakset `power` field for ships is in **kW** and, for the modern ships, is the real installed
power (Incat 112 m: 32,000 kW = 4 x 8,200 kW; HSS 1500: 68,000 kW = 4 turbines; Clan Alpine:
1,870 kW = 2,510 ihp; *Our Lady Pamela*: 2,869 kW = 2 x 1,950 bhp; *Invicta*: 8,200 kW =
11,000 shp). It is reliable for 1880-2020 tonnage and **unreliable for the early steamers**,
where it is often several times the real figure.

19 steam models and 1 diesel model use a horsepower I supplied instead of the pakset figure,
because the pakset figure is physically impossible for the type. Each is marked `ESTIMATE` in
the model table with the pakset value in brackets, and they are listed again in section 4.

## 2. Per-model table

75 models. `fuel_per_km` is grams of coal/km for the 34 coal-fired steam models and millilitres
of liquid fuel/km for the other 41 (37 diesel, 3 petrol, 1 oil-fired steam). `calibration_speed`
is the pakset `speed`; `cut_off_speed` is half of it. `range` is the value already in the `.dat`
(blank where no object of that model has one) and is unchanged.

Source keys used in the table:

* **C1** - measured fleet returns of coal per ihp-hour: 2.11 (1872), 1.828 (1881), 1.522 (1891,
 28 three-stage expansion engines at sea), Table 5/6 of *A Review of Marine Engineering*,
 `openjournals.library.sydney.edu.au/EANSW/article/download/3029/3557`
* **C2** - small-craft checks: tugs *Nubia* 2.0 lb/ihp-h and *Oceania* 1.0 lb/ihp-h (1890),
 `forum.simutrans.com/index.php?topic=6521.35`; ferry *Kookooburra* 2.84 lb/ihp-h measured
 (1907), `openjournals.library.sydney.edu.au/EANSW/article/download/3628/4234`
* **C3** - *Britannia* 5.1 and *Persia* 3.8 lb/ihp-h (1840/1856), *Ocean Steamships* (1891),
 `gutenberg.org/files/54136/54136-h/54136-h.htm`
* **D1** - MAN Energy Solutions, *Marine engine programme 2025*, two-stroke SFOC 163-176 g/kWh,
 `man-es.com/docs/default-source/marine/marine-engine-programme-20205656db69fafa42b991f030191bb3bbb4.pdf`
* **D2** - MAN 8G95ME-C9.5 SFOC-versus-load table (162 g/kWh at 70% load),
 `man-es.com/docs/default-source/document-sync/efficiency-improvements-main-engine-auxiliary-systems-eng.pdf`
* **D3** - Wartsila 31, 169.4 g/kWh, `brandhub.wartsila.com/m/19b25d19ebe05062/original/Wartsila-31-Brochure.pdf`
* **N1** - narrowboat measurements: 1.0-1.5 l/h at canal speed,
 `canalworld.net/forums/index.php?/topic/59872-diesel-consumption/`; 2-3.5 kW at 2.5-2.8 mph,
 `ortomarine.co.uk/wp-content/uploads/2021/10/Ortomarine-Narrowboat-Trial-Final-Report.pdf`

"ESTIMATE" in the basis or source column means the number is mine, not a source's; the anchor
is stated in the same cell.

| model | fuel_per_km | calibration_speed | cut_off_speed | range (km or blank) | basis | source |
|---|---|---|---|---|---|---|
| ClanLineSteamer | 47476 | 20 | 10 | | 2,510 ihp x 0.60 x 1.39 lb/ihp-h x 453.6 / 20 km/h = 949522 g coal/h -> 47476 g/km; 2,510 ihp triple expansion (Clan Alpine, Wikipedia); pakset 1,870 kW agrees | power en.wikipedia.org/wiki/SS_Clan_Alpine_(1942); C1 |
| ChannelPaddleSteamerHull | 73860 | 20 | 10 | 250 | 1,200 ihp x 0.60 x 4.52 lb/ihp-h x 453.6 / 20 km/h = 1477190 g coal/h -> 73860 g/km; ESTIMATE 1,200 ihp (pakset 3,550 kW = 4,760 ihp is ~4x too high for a 1853 Channel paddler) | C1; C2 |
| ChannelScrewSteamship | 38762 | 25 | 12 | 275 | 1,500 ihp x 0.60 x 2.37 lb/ihp-h x 453.6 / 25 km/h = 969043 g coal/h -> 38762 g/km; ESTIMATE 1,500 ihp (pakset 3,550 kW = 4,760 ihp) | C1; C2 |
| ClydeCargoSteamerHull | 30065 | 20 | 10 | 150 | 700 ihp x 0.60 x 3.16 lb/ihp-h x 453.6 / 20 km/h = 601300 g coal/h -> 30065 g/km; ESTIMATE 700 ihp (pakset 4,550 kW = 6,101 ihp is ~8x too high for an 1869 cargo steamer) | C1; C2 |
| ClydePuffer | 3780 | 15 | 8 | 180 | 100 ihp x 0.50 x 2.50 lb/ihp-h x 453.6 / 15 km/h = 56699 g coal/h -> 3780 g/km; 100 ihp compound (puffer Cretan, 1910); pakset 200 kW = 268 ihp is too high | power dalmadan.com/?p=63375 (puffer Cretan, 100 ihp); C1; C2 |
| ClydeSteamer | 13154 | 26 | 13 | 150 | 300 ihp x 0.60 x 4.19 lb/ihp-h x 453.6 / 26 km/h = 342008 g coal/h -> 13154 g/km; ESTIMATE 300 ihp (pakset 1,000 kW = 1,341 ihp is ~5x too high for an 1860 Clyde steamer) | C1; C2 |
| IronPaddleSteamer | 7017 | 22 | 11 | 100 | 121 ihp x 0.50 x 5.62 lb/ihp-h x 453.6 / 22 km/h = 154363 g coal/h -> 7017 g/km; pakset 90 kW = 121 ihp | C1; C2 |
| IronRiverSteamer | 10148 | 20 | 10 | | 200 ihp x 0.60 x 3.73 lb/ihp-h x 453.6 / 20 km/h = 202950 g coal/h -> 10148 g/km; ESTIMATE 200 ihp (pakset 500 kW = 670 ihp is ~3x too high for a river steamer) | C1; C2 |
| LargeSteelRiverSteamer | 7838 | 25 | 12 | | 300 ihp x 0.60 x 2.40 lb/ihp-h x 453.6 / 25 km/h = 195952 g coal/h -> 7838 g/km; ESTIMATE 300 ihp (pakset 500 kW = 670 ihp) | C1; C2 |
| SteelRiverSteamer | 8981 | 25 | 12 | | 300 ihp x 0.60 x 2.75 lb/ihp-h x 453.6 / 25 km/h = 224528 g coal/h -> 8981 g/km; ESTIMATE 300 ihp (pakset 500 kW = 670 ihp) | C1; C2 |
| WoodenRiverSteamer | 7031 | 15 | 8 | 100 | 80 ihp x 0.50 x 5.81 lb/ihp-h x 453.6 / 15 km/h = 105460 g coal/h -> 7031 g/km; ESTIMATE 80 ihp (pakset 120 kW = 161 ihp) | C1; C2 |
| WoodenPaddleSteamer | 5712 | 15 | 8 | 100 | 50 ihp x 0.50 x 7.56 lb/ihp-h x 453.6 / 15 km/h = 85678 g coal/h -> 5712 g/km; ESTIMATE 50 ihp (pakset 90 kW = 121 ihp) | C1; C2 |
| PSChevalier | 10148 | 25 | 12 | 65 | 250 ihp x 0.60 x 3.73 lb/ihp-h x 453.6 / 25 km/h = 253688 g coal/h -> 10148 g/km; ESTIMATE 250 ihp (pakset 600 kW = 804 ihp is ~3x too high) | C1; C2 |
| PSComet | 2419 | 15 | 8 | 60 | 20 ihp x 0.50 x 8.00 lb/ihp-h x 453.6 / 15 km/h = 36287 g coal/h -> 2419 g/km; ESTIMATE 20 ihp (pakset 55 kW = 74 ihp is ~4x too high for 1812) | C1; C2 |
| PSIndustry | 3578 | 15 | 8 | 100 | 30 ihp x 0.50 x 7.89 lb/ihp-h x 453.6 / 15 km/h = 53675 g coal/h -> 3578 g/km; ESTIMATE 30 ihp (pakset 200 kW = 268 ihp is ~9x too high for 1814) | C1; C2 |
| PSMadgeWildfire | 17314 | 30 | 15 | 120 | 804 ihp x 0.60 x 2.37 lb/ihp-h x 453.6 / 30 km/h = 519407 g coal/h -> 17314 g/km; pakset 600 kW = 804 ihp | C1; C2 |
| PSPremier | 7399 | 20 | 10 | 50 | 120 ihp x 0.50 x 5.44 lb/ihp-h x 453.6 / 20 km/h = 147984 g coal/h -> 7399 g/km; ESTIMATE 120 ihp (pakset 200 kW = 268 ihp) | C1; C2 |
| ps-premier-covered | 6634 | 20 | 10 | 50 | 120 ihp x 0.50 x 4.88 lb/ihp-h x 453.6 / 20 km/h = 132676 g coal/h -> 6634 g/km; ESTIMATE 120 ihp (pakset 200 kW = 268 ihp) | C1; C2 |
| PSWaverley2 | 15590 | 35 | 18 | 135 | 939 ihp x 0.60 x 2.14 lb/ihp-h x 453.6 / 35 km/h = 545664 g coal/h -> 15590 g/km; pakset 700 kW = 939 ihp | C1; C2 |
| RMSColumba | 16358 | 39 | 20 | 130 | 872 ihp x 0.60 x 2.69 lb/ihp-h x 453.6 / 39 km/h = 637954 g coal/h -> 16358 g/km; pakset 650 kW = 872 ihp | C1; C2 |
| SECRQueen | 55652 | 40 | 20 | 260 | 5,700 ihp x 0.60 x 1.44 lb/ihp-h x 453.6 / 40 km/h = 2226093 g coal/h -> 55652 g/km; pakset 4,250 kW = 5,700 ihp | C1; C2 |
| SeineNetterSteam | 3518 | 25 | 12 | | 100 ihp x 0.50 x 3.88 lb/ihp-h x 453.6 / 25 km/h = 87946 g coal/h -> 3518 g/km; ESTIMATE 100 ihp (pakset 1,000 kW = 1,341 ihp is ~13x too high for a fishing vessel) | C1; C2 |
| SSGreatBritain | 72495 | 20 | 10 | | 1,000 ihp x 0.60 x 5.33 lb/ihp-h x 453.6 / 20 km/h = 1449907 g coal/h -> 72495 g/km; 1,000 ihp (2 x 500 hp engines, Wikipedia) | power en.wikipedia.org/wiki/SS_Great_Britain; C3; C1 |
| SSGreatWestern | 59990 | 20 | 10 | | 750 ihp x 0.60 x 5.88 lb/ihp-h x 453.6 / 20 km/h = 1199796 g coal/h -> 59990 g/km; 750 hp (Wikipedia) | power en.wikipedia.org/wiki/SS_Great_Western (which also gives 400 t of coal in 15 d 5 h); C3 |
| SSGreatEastern | 303325 | 26 | 13 | | 8,000 ihp x 0.60 x 3.62 lb/ihp-h x 453.6 / 26 km/h = 7886453 g coal/h -> 303325 g/km; 8,000 hp total (Wikipedia) | power en.wikipedia.org/wiki/SS_Great_Eastern; C3; C1 |
| SRInvicta | 114089 | 41 | 20 | 250 | 11,000 ihp x 0.75 x 1.25 lb/ihp-h x 453.6 / 41 km/h = 4677668 g coal/h -> 114089 g/km; 11,000 shp turbines (Wikipedia) | power en.wikipedia.org/wiki/SS_Invicta_(1939); C1 |
| SRIsleOfThanet | 95808 | 40 | 20 | 200 | 8,502 ihp x 0.75 x 1.33 lb/ihp-h x 453.6 / 40 km/h = 3832336 g coal/h -> 95808 g/km; pakset 6,340 kW = 8,502 ihp | C1; C2 |
| SteamBargeTug | 8611 | 8 | 4 | | 60 ihp x 0.50 x 5.06 lb/ihp-h x 453.6 / 8 km/h = 68889 g coal/h -> 8611 g/km; ESTIMATE 60 ihp (pakset 100 kW = 134 ihp) | C1; C2 |
| SteamNarrowboatTug | 5634 | 8 | 4 | | 40 ihp x 0.50 x 4.97 lb/ihp-h x 453.6 / 8 km/h = 45076 g coal/h -> 5634 g/km; ESTIMATE 40 ihp (pakset 60 kW = 80 ihp) | C1; C2 |
| SteamNarrowboat | 1990 | 8 | 4 | | 27 ihp x 0.50 x 2.60 lb/ihp-h x 453.6 / 8 km/h = 15921 g coal/h -> 1990 g/km; pakset 20 kW = 27 ihp | C1; C2 |
| TSSKingEdward | 46450 | 38 | 19 | 120 | 2,450 ihp x 0.75 x 2.12 lb/ihp-h x 453.6 / 38 km/h = 1765092 g coal/h -> 46450 g/km; pakset 1,827 kW = 2,450 ihp | C1; C2 |
| TSSQueenMary | 29816 | 39 | 20 | 140 | 2,660 ihp x 0.75 x 1.29 lb/ihp-h x 453.6 / 39 km/h = 1162817 g coal/h -> 29816 g/km; pakset 1,984 kW = 2,660 ihp | C1; C2 |
| WoodenPaddleTug | 5880 | 15 | 8 | | 50 ihp x 0.50 x 7.78 lb/ihp-h x 453.6 / 15 km/h = 88198 g coal/h -> 5880 g/km; ESTIMATE 50 ihp (pakset 100 kW = 134 ihp) | C1; C2 |
| IronSteamTug | 6698 | 20 | 10 | | 100 ihp x 0.50 x 5.91 lb/ihp-h x 453.6 / 20 km/h = 133951 g coal/h -> 6698 g/km; ESTIMATE 100 ihp (pakset 200 kW = 268 ihp) | C1; C2 |
| BTCLordWarden | 150799 | 36 | 18 | 400 | 15,958 shp x 0.70 x 0.90 lb/shp-h x 453.6 / 0.84 / 36 km/h = 150799 ml/km; oil-fired steam turbine coded 'steam' in the pakset | 0.8-1.0 lb oil/shp-h band ESTIMATE |
| BantamPusher | 1860 | 8 | 4 | | 100 kW x 0.50 x 250 g/kWh = 12,500 g/h / 0.84 kg/l / 8 km/h = 1860 ml/km; small harbour pusher | D1; D3 |
| Handysize | 39214 | 25 | 12 | | 6,100 kW x 0.75 x 180 g/kWh = 823,500 g/h / 0.84 kg/l / 25 km/h = 39214 ml/km; 6,100 kW = one MAN 6S50MC-class slow-speed | power pakset 6,100 kW = one MAN 6S50MC; D1; D2 |
| HSS-1500 | 172891 | 70 | 35 | 300 | 68,000 kW x 0.65 x 230 g/kWh = 10,166,000 g/h / 0.84 kg/l / 70 km/h = 172891 ml/km; 68,000 kW of gas turbines | power 68,000 kW installed; gas-turbine SFOC 230 g/kWh ESTIMATE, cf. D1 |
| Incat112m | 72381 | 80 | 40 | 350 | 32,000 kW x 0.80 x 190 g/kWh = 4,864,000 g/h / 0.84 kg/l / 80 km/h = 72381 ml/km; 4 x 8,200 kW medium-speed | D1; D3 |
| Incat74m | 38204 | 70 | 35 | 250 | 14,400 kW x 0.80 x 195 g/kWh = 2,246,400 g/h / 0.84 kg/l / 70 km/h = 38204 ml/km; medium-speed | D1; D3 |
| Incat96m | 65782 | 80 | 40 | 300 | 28,337 kW x 0.80 x 195 g/kWh = 4,420,572 g/h / 0.84 kg/l / 80 km/h = 65782 ml/km; medium-speed | D1; D3 |
| MDV-1200 | 72959 | 70 | 35 | 350 | 27,500 kW x 0.80 x 195 g/kWh = 4,290,000 g/h / 0.84 kg/l / 70 km/h = 72959 ml/km; medium-speed | D1; D3 |
| SealinkHorsa | 38707 | 36 | 18 | 300 | 8,575 kW x 0.65 x 210 g/kWh = 1,170,488 g/h / 0.84 kg/l / 36 km/h = 38707 ml/km; medium-speed | D1; D3 |
| TTEuropeanFreight | 41020 | 35 | 18 | 320 | 8,835 kW x 0.65 x 210 g/kWh = 1,205,978 g/h / 0.84 kg/l / 35 km/h = 41020 ml/km; medium-speed | D1; D3 |
| POPride | 83086 | 41 | 20 | 300 | 23,170 kW x 0.65 x 190 g/kWh = 2,861,495 g/h / 0.84 kg/l / 41 km/h = 83086 ml/km; medium-speed | D1; D3 |
| POSpirit | 102917 | 40 | 20 | 350 | 30,400 kW x 0.65 x 175 g/kWh = 3,458,000 g/h / 0.84 kg/l / 40 km/h = 102917 ml/km; medium-speed | D1; D3 |
| POSuperEuropeanFreight | 96629 | 40 | 20 | 360 | 27,000 kW x 0.65 x 185 g/kWh = 3,246,750 g/h / 0.84 kg/l / 40 km/h = 96629 ml/km; medium-speed | D1; D3 |
| POSuperEuropeanMixed | 94018 | 40 | 20 | 360 | 27,000 kW x 0.65 x 180 g/kWh = 3,159,000 g/h / 0.84 kg/l / 40 km/h = 94018 ml/km; medium-speed | D1; D3 |
| FBM-Hydrocat | 2095 | 45 | 22 | 200 | 450 kW x 0.80 x 220 g/kWh = 79,200 g/h / 0.84 kg/l / 45 km/h = 2095 ml/km; small high-speed | D1; D3 |
| HSC-FastCat | 12094 | 63 | 32 | 200 | 4,000 kW x 0.80 x 200 g/kWh = 640,000 g/h / 0.84 kg/l / 63 km/h = 12094 ml/km; high-speed | D1; D3 |
| HSC-Our-Lady | 10626 | 54 | 27 | 250 | 2,869 kW x 0.80 x 210 g/kWh = 481,992 g/h / 0.84 kg/l / 54 km/h = 10626 ml/km; high-speed | D1; D3 |
| HSC-WightRyder | 9524 | 60 | 30 | 85 | 3,000 kW x 0.80 x 200 g/kWh = 480,000 g/h / 0.84 kg/l / 60 km/h = 9524 ml/km; high-speed | D1; D3 |
| Island | 1004 | 16 | 8 | 50 | 100 kW x 0.60 x 225 g/kWh = 13,500 g/h / 0.84 kg/l / 16 km/h = 1004 ml/km; small high-speed | D1; D3 |
| Loch | 2560 | 18 | 9 | 80 | 300 kW x 0.60 x 215 g/kWh = 38,700 g/h / 0.84 kg/l / 18 km/h = 2560 ml/km; small high-speed | D1; D3 |
| MerseyFerry | 7202 | 26 | 13 | 60 | 1,100 kW x 0.65 x 220 g/kWh = 157,300 g/h / 0.84 kg/l / 26 km/h = 7202 ml/km; medium-speed | D1; D3 |
| MVBalmoral | 3560 | 35 | 18 | 120 | 700 kW x 0.65 x 230 g/kWh = 104,650 g/h / 0.84 kg/l / 35 km/h = 3560 ml/km; 1930s-40s medium-speed | D1; D3 |
| MVLochfyne | 4847 | 30 | 15 | 135 | 783 kW x 0.65 x 240 g/kWh = 122,148 g/h / 0.84 kg/l / 30 km/h = 4847 ml/km; 1930s medium-speed | power en.wikipedia.org/wiki/MV_Lochfyne (1,000 ihp); D1 |
| River-Runner-150 | 4141 | 46 | 23 | 30 | 1,000 kW x 0.80 x 200 g/kWh = 160,000 g/h / 0.84 kg/l / 46 km/h = 4141 ml/km; high-speed | D1; D3 |
| River-Runner-200 | 4396 | 52 | 26 | 30 | 1,200 kW x 0.80 x 200 g/kWh = 192,000 g/h / 0.84 kg/l / 52 km/h = 4396 ml/km; high-speed | D1; D3 |
| SeineNetterDiesel | 1264 | 30 | 15 | | 200 kW x 0.65 x 245 g/kWh = 31,850 g/h / 0.84 kg/l / 30 km/h = 1264 ml/km; 1920s diesel; pakset 1,250 kW is ~6x too high for a fishing vessel | D1; D3 |
| SemiDieselNarrowboat | 536 | 8 | 4 | | 30 kW x 0.40 x 300 g/kWh = 3,600 g/h / 0.84 kg/l / 8 km/h = 536 ml/km; hot-bulb semi-diesel | power pakset 30 kW; N1; SFC 300 g/kWh ESTIMATE (hot-bulb) |
| DieselNarrowboat | 500 | 8 | 4 | | 30 kW x 0.40 x 280 g/kWh = 3,360 g/h / 0.84 kg/l / 8 km/h = 500 ml/km; early small diesel | power pakset 30 kW; N1 |
| DieselBarge | 774 | 8 | 4 | | 50 kW x 0.40 x 260 g/kWh = 5,200 g/h / 0.84 kg/l / 8 km/h = 774 ml/km; small diesel | power pakset 50 kW; N1 |
| LightweightDieselBarge | 714 | 8 | 4 | | 50 kW x 0.40 x 240 g/kWh = 4,800 g/h / 0.84 kg/l / 8 km/h = 714 ml/km; small diesel | power pakset 50 kW; N1 |
| SR-N4-Mountbatten-Mk1 | 41328 | 110 | 55 | 90 | 1,000 imp gal/h = 4,546 l/h at 50 kn cruise (Wikipedia SR.N4) / 110 km/h = 41328 ml/km; gas-turbine hovercraft; 1,000 gal/h is the documented service rate | H1 en.wikipedia.org/wiki/SR.N4 |
| SR-N4-Mountbatten-Mk3 | 41328 | 110 | 55 | 110 | 1,000 imp gal/h = 4,546 l/h at 50 kn cruise (Wikipedia SR.N4) / 110 km/h = 41328 ml/km; gas-turbine hovercraft; 1,000 gal/h is the documented service rate | H1 en.wikipedia.org/wiki/SR.N4 |
| SR-N6-Winchester | 3033 | 90 | 45 | 110 | 780 kW x 0.80 x 350 g/kWh (gas turbine at part load) / 0.80 kg/l / 90 km/h = 3033 ml/km; gas-turbine hovercraft | H1 en.wikipedia.org/wiki/SR.N4; SFC ESTIMATE |
| Super-Loch | 7714 | 20 | 10 | 100 | 1,200 kW x 0.60 x 180 g/kWh = 129,600 g/h / 0.84 kg/l / 20 km/h = 7714 ml/km; medium-speed | D1; D3 |
| ThameslineRiverbus | 1310 | 45 | 22 | 40 | 300 kW x 0.75 x 220 g/kWh = 49,500 g/h / 0.84 kg/l / 45 km/h = 1310 ml/km; small high-speed | D1; D3 |
| TowpathTractor | 816 | 14 | 7 | | 80 kW x 0.50 x 240 g/kWh = 9,600 g/h / 0.84 kg/l / 14 km/h = 816 ml/km; small diesel | D1; D3 |
| DieselTug | 2571 | 20 | 10 | | 300 kW x 0.60 x 240 g/kWh = 43,200 g/h / 0.84 kg/l / 20 km/h = 2571 ml/km; 1930s diesel | D1; D3 |
| TyneFerry | 686 | 25 | 12 | 60 | 100 kW x 0.60 x 240 g/kWh = 14,400 g/h / 0.84 kg/l / 25 km/h = 686 ml/km; 1930s diesel | D1; D3 |
| BHC-AP1-88 | 3423 | 90 | 45 | 100 | 894 kW x 0.85 x 300 g/kWh = 227,970 g/h / 0.74 kg/l / 90 km/h = 3423 ml/km; high-speed petrol | spark-ignition 300 g/kWh ESTIMATE; AP.1-88 published ~300 l/h |
| BHT-130 | 3446 | 90 | 45 | 100 | 900 kW x 0.85 x 300 g/kWh = 229,500 g/h / 0.74 kg/l / 90 km/h = 3446 ml/km; high-speed petrol | spark-ignition 300 g/kWh ESTIMATE; AP.1-88 published ~300 l/h |
| BHT-150 | 3446 | 90 | 45 | 125 | 900 kW x 0.85 x 300 g/kWh = 229,500 g/h / 0.74 kg/l / 90 km/h = 3446 ml/km; high-speed petrol | spark-ignition 300 g/kWh ESTIMATE; AP.1-88 published ~300 l/h |

## 3. Object mapping table

One line per object, exact `name=` value from the `.dat`, 341 lines. `SAIL`, `BIO` and
`UNPOWERED` all mean `fuel_per_km=0` (and no `calibration_speed` is needed). The model keys in
this column are the ones used in section 2. Four objects are worth reading section 4 before applying:
`BTCLordWarden`, `LightweightDieselBargeOil`, `DieselNarrowboatOil`, `SemiDieselNarrowboatOil`.

| object | model |
|---|---|
| BHC-AP1-88_100 | BHC-AP1-88 |
| BHC-AP1-88_400(Cool) | BHC-AP1-88 |
| BHC-AP1-88_400(Piece) | BHC-AP1-88 |
| BantamPusher | BantamPusher |
| BHT-130 | BHT-130 |
| BHC-BHT-150_400(Cool) | BHT-150 |
| BHT-150(Piece) | BHT-150 |
| BoatHorsesFly | BIO |
| BoatHorsesSingle | BIO |
| BlackwallFrigateHull | SAIL |
| BTCLordWarden | BTCLordWarden |
| ClanLineSteamerBulk | ClanLineSteamer |
| ClanLineSteamerCars | ClanLineSteamer |
| ClanLineSteamerCool | ClanLineSteamer |
| ClanLineSteamerLivestock | ClanLineSteamer |
| ClanLineSteamerLong | ClanLineSteamer |
| ClanLineSteamerOil | ClanLineSteamer |
| ClanLineSteamerPiece | ClanLineSteamer |
| ClipperHull | SAIL |
| EastIndiamanHull | SAIL |
| HandysizeBulk | Handysize |
| HandysizeCars | Handysize |
| HandysizeCool | Handysize |
| HandysizeLivestock | Handysize |
| HandysizeLong | Handysize |
| HandysizeOil | Handysize |
| HandysizePiece | Handysize |
| HSS-1500 | HSS-1500 |
| HSS-1500(AddMail) | UNPOWERED |
| Incat112m | Incat112m |
| Incat112m(AddMail) | UNPOWERED |
| Incat74m | Incat74m |
| Incat74m(AddMail) | UNPOWERED |
| Incat96m | Incat96m |
| Incat96m(AddMail) | UNPOWERED |
| MDV-1200 | MDV-1200 |
| MDV-1200(AddMail) | UNPOWERED |
| SealinkHorsa | SealinkHorsa |
| SRInvicta | SRInvicta |
| SRIsleOfThanet | SRIsleOfThanet |
| SSGreatBritain | SSGreatBritain |
| SSGreatBritainAddMail | UNPOWERED |
| SSGreatWestern | SSGreatWestern |
| SSGreatWesternAddMail | UNPOWERED |
| TTEuropeanFreight | TTEuropeanFreight |
| POPride | POPride |
| POSpirit | POSpirit |
| POSuperEuropeanFreight | POSuperEuropeanFreight |
| POSuperEuropeanMixed | POSuperEuropeanMixed |
| SSGreatEastern | SSGreatEastern |
| SSGreatEasternAddMail | UNPOWERED |
| WindjammerHull | SAIL |
| BoxBoatBulk | UNPOWERED |
| BoxBoatCool | UNPOWERED |
| BoxBoatLong | UNPOWERED |
| BoxBoatPiece | UNPOWERED |
| BrigHull | SAIL |
| ChannelPaddleSteamerHull | ChannelPaddleSteamerHull |
| ChannelScrewSteamship | ChannelScrewSteamship |
| ClydeCargoSteamerHull | ClydeCargoSteamerHull |
| ClydePufferBulk | ClydePuffer |
| ClydePufferCool | ClydePuffer |
| ClydePufferLivestock | ClydePuffer |
| ClydePufferLong | ClydePuffer |
| ClydePufferOil | ClydePuffer |
| ClydePufferPiece | ClydePuffer |
| ClydeSteamer | ClydeSteamer |
| CompositeHullUnpoweredNarrowboatBulk | UNPOWERED |
| CompositeHullUnpoweredNarrowboatCool | UNPOWERED |
| CompositeHullUnpoweredNarrowboatLivestock | UNPOWERED |
| CompositeHullUnpoweredNarrowboatLong | UNPOWERED |
| CompositeHullUnpoweredNarrowboatOil | UNPOWERED |
| CompositeHullUnpoweredNarrowboatPiece | UNPOWERED |
| DieselBargeBulk | DieselBarge |
| DieselBargeCool | DieselBarge |
| DieselBargeLivestock | DieselBarge |
| DieselBargeLong | DieselBarge |
| DieselBargeOil | DieselBarge |
| DieselBargePiece | DieselBarge |
| LightweightDieselBargeBulk | LightweightDieselBarge |
| LightweightDieselBargeCool | LightweightDieselBarge |
| LightweightDieselBargeLivestock | LightweightDieselBarge |
| LightweightDieselBargeLong | LightweightDieselBarge |
| LightweightDieselBargeOil | LightweightDieselBarge |
| LightweightDieselBargePiece | LightweightDieselBarge |
| DieselNarrowboatBulk | DieselNarrowboat |
| DieselNarrowboatCool | DieselNarrowboat |
| DieselNarrowboatLivestock | DieselNarrowboat |
| DieselNarrowboatLong | DieselNarrowboat |
| DieselNarrowboatOil | DieselNarrowboat |
| DieselNarrowboatPiece | DieselNarrowboat |
| Dogger | SAIL |
| FBM-Hydrocat | FBM-Hydrocat |
| Fifie | SAIL |
| BlackwallFrigateAddBulk | SAIL |
| BlackwallFrigateAddCool | SAIL |
| BlackwallFrigateAddLivestock | SAIL |
| BlackwallFrigateAddLong | SAIL |
| BlackwallFrigateAddMail | SAIL |
| BlackwallFrigateAddPax | SAIL |
| BlackwallFrigateAddPax-first-class | SAIL |
| BlackwallFrigateAddPax-second-class | SAIL |
| BlackwallFrigateAddPiece | SAIL |
| BrigAddBulk | SAIL |
| BrigAddCool | SAIL |
| BrigAddLivestock | SAIL |
| BrigAddLong | SAIL |
| BrigAddMail | SAIL |
| BrigAddPax | SAIL |
| BrigAddPax-first-class | SAIL |
| BrigAddPiece | SAIL |
| BTCLordWardenAddCool | UNPOWERED |
| BTCLordWardenAddMail | UNPOWERED |
| BTCLordWardenAddPiece | UNPOWERED |
| CarferryAddBulk0 | SAIL |
| CarferryAddBulk1 | SAIL |
| CarferryAddCar0 | SAIL |
| CarferryAddCar1 | SAIL |
| CarferryAddCool0 | SAIL |
| CarferryAddCool1 | SAIL |
| CarferryAddLivestock0 | SAIL |
| CarferryAddLivestock1 | SAIL |
| CarferryAddLong0 | SAIL |
| CarferryAddLong1 | SAIL |
| CarferryAddOil0 | SAIL |
| CarferryAddOil1 | SAIL |
| CarferryAddPiece0 | SAIL |
| CarferryAddPiece1 | SAIL |
| ChannelPaddleSteamerAddBulk | UNPOWERED |
| ChannelPaddleSteamerAddCool | UNPOWERED |
| ChannelPaddleSteamerAddLivestock | UNPOWERED |
| ChannelPaddleSteamerAddLong | UNPOWERED |
| ChannelPaddleSteamerAddMail | UNPOWERED |
| ChannelPaddleSteamerAddPax | UNPOWERED |
| ChannelPaddleSteamerAddPiece | UNPOWERED |
| ChannelScrewSteamshipAddMail | UNPOWERED |
| ClipperAddBulk | SAIL |
| ClipperAddCool | SAIL |
| ClipperAddLivestock | SAIL |
| ClipperAddLong | SAIL |
| ClipperAddMail | SAIL |
| ClipperAddPax | SAIL |
| ClipperAddPax-first-class | SAIL |
| ClipperAddPax-second-class | SAIL |
| ClipperAddPiece | SAIL |
| ClydeCargoSteamerAddBulk | UNPOWERED |
| ClydeCargoSteamerAddCool | UNPOWERED |
| ClydeCargoSteamerAddLivestock | UNPOWERED |
| ClydeCargoSteamerAddLong | UNPOWERED |
| ClydeCargoSteamerAddMail | UNPOWERED |
| ClydeCargoSteamerAddPiece | UNPOWERED |
| IronPaddleSteamerMail | UNPOWERED |
| PSChevalierMail | UNPOWERED |
| PSCometMail | UNPOWERED |
| PSMadgeWildfireMail | UNPOWERED |
| PSWaverley2Mail | UNPOWERED |
| RMSColumbaMail | UNPOWERED |
| TSSKingEdwardMail | UNPOWERED |
| TSSQueenMaryMail | UNPOWERED |
| WoodenPaddleSteamerMail | UNPOWERED |
| EastIndiamanAddBulk | SAIL |
| EastIndiamanAddCool | SAIL |
| EastIndiamanAddLivestock | SAIL |
| EastIndiamanAddLong | SAIL |
| EastIndiamanAddMail | SAIL |
| EastIndiamanAddPax | SAIL |
| EastIndiamanAddPax-first-class | SAIL |
| EastIndiamanAddPax-second-class | SAIL |
| EastIndiamanAddPiece | SAIL |
| ferry-mail | UNPOWERED |
| humber-keel-mail-hold | SAIL |
| mail-space | UNPOWERED |
| MarketBargeAddMail | UNPOWERED |
| MarketNarrowboatAddMail | UNPOWERED |
| PacketBargeAddMail | UNPOWERED |
| POPrideAddCool | UNPOWERED |
| POPrideAddMail | UNPOWERED |
| POPrideAddPiece | UNPOWERED |
| POSpiritAddCool | UNPOWERED |
| POSpiritAddMail | UNPOWERED |
| POSpiritAddPiece | UNPOWERED |
| POSuperEuropeanFreightAddBulk | UNPOWERED |
| POSuperEuropeanFreightAddCar | UNPOWERED |
| POSuperEuropeanFreightAddCool | UNPOWERED |
| POSuperEuropeanFreightAddLivestock | UNPOWERED |
| POSuperEuropeanFreightAddLong | UNPOWERED |
| POSuperEuropeanFreightAddMail | UNPOWERED |
| POSuperEuropeanFreightAddOil | UNPOWERED |
| POSuperEuropeanFreightAddPiece | UNPOWERED |
| POSuperEuropeanMixedAddCool | UNPOWERED |
| POSuperEuropeanMixedAddMail | UNPOWERED |
| POSuperEuropeanMixedAddPiece | UNPOWERED |
| SchoonerAddBulk | SAIL |
| SchoonerAddCool | SAIL |
| SchoonerAddLivestock | SAIL |
| SchoonerAddLong | SAIL |
| SchoonerAddMail | SAIL |
| SchoonerAddPax | SAIL |
| SchoonerAddPiece | SAIL |
| SealinkHorsaAddCool | UNPOWERED |
| SealinkHorsaAddMail | UNPOWERED |
| SealinkHorsaAddPiece | UNPOWERED |
| SECRQueenAddMail | UNPOWERED |
| SRInvictaAddMail | UNPOWERED |
| SRIsleOfThanetAddMail | UNPOWERED |
| TTEuropeanFreightAddBulk | UNPOWERED |
| TTEuropeanFreightAddCar | UNPOWERED |
| TTEuropeanFreightAddCool | UNPOWERED |
| TTEuropeanFreightAddLivestock | UNPOWERED |
| TTEuropeanFreightAddLong | UNPOWERED |
| TTEuropeanFreightAddMail | UNPOWERED |
| TTEuropeanFreightAddOil | UNPOWERED |
| TTEuropeanFreightAddPiece | UNPOWERED |
| WindjammerAddBulk | SAIL |
| WindjammerAddCool | SAIL |
| WindjammerAddLivestock | SAIL |
| WindjammerAddLong | SAIL |
| WindjammerAddMail | SAIL |
| WindjammerAddOil | SAIL |
| WindjammerAddPiece | SAIL |
| HSC-FastCat | HSC-FastCat |
| HSC-Our-Lady | HSC-Our-Lady |
| HSC-WightRyder | HSC-WightRyder |
| HumberKeelBulk | SAIL |
| HumberKeelCool | SAIL |
| HumberKeelLivestock | SAIL |
| HumberKeelLong | SAIL |
| HumberKeelPassenger | SAIL |
| HumberKeelPiece | SAIL |
| IronPaddleSteamer | IronPaddleSteamer |
| IronRiverSteamer | IronRiverSteamer |
| Island | Island |
| LargeSteelRiverSteamer | LargeSteelRiverSteamer |
| Loch | Loch |
| MarketBarge | UNPOWERED |
| MarketNarrowboat | UNPOWERED |
| MerseyFerry | MerseyFerry |
| MVBalmoral | MVBalmoral |
| MVLochfyne | MVLochfyne |
| NorfolkWherryBulk | SAIL |
| NorfolkWherryCool | SAIL |
| NorfolkWherryLivestock | SAIL |
| NorfolkWherryLong | SAIL |
| NorfolkWherryMail | SAIL |
| NorfolkWherryPassenger | SAIL |
| NorfolkWherryPiece | SAIL |
| PacketBarge | UNPOWERED |
| PSChevalier | PSChevalier |
| PSComet | PSComet |
| PSIndustryCool | PSIndustry |
| PSIndustryMail | PSIndustry |
| PSIndustryPiece | PSIndustry |
| PSMadgeWildfire | PSMadgeWildfire |
| ps-premier-covered | ps-premier-covered |
| PSPremier | PSPremier |
| PSWaverley2 | PSWaverley2 |
| River-Runner-150 | River-Runner-150 |
| River-Runner-200 | River-Runner-200 |
| RMSColumba | RMSColumba |
| SchoonerHull | SAIL |
| SECRQueen | SECRQueen |
| SeineNetterDiesel | SeineNetterDiesel |
| SeineNetterSteam | SeineNetterSteam |
| SemiDieselNarrowboatBulk | SemiDieselNarrowboat |
| SemiDieselNarrowboatCool | SemiDieselNarrowboat |
| SemiDieselNarrowboatLivestock | SemiDieselNarrowboat |
| SemiDieselNarrowboatLong | SemiDieselNarrowboat |
| SemiDieselNarrowboatOil | SemiDieselNarrowboat |
| SemiDieselNarrowboatPiece | SemiDieselNarrowboat |
| skiff-wherry-bulk | BIO |
| skiff-wherry-cool | BIO |
| skiff-wherry-livestock | BIO |
| skiff-wherry-long | BIO |
| skiff-wherry-passenger | BIO |
| skiff-wherry-piece | BIO |
| SR-N4-Mountbatten-Mk1 | SR-N4-Mountbatten-Mk1 |
| SR-N4-Mountbatten-Mk3 | SR-N4-Mountbatten-Mk3 |
| SR-N6-Winchester | SR-N6-Winchester |
| SteamBargeTug | SteamBargeTug |
| SteamNarrowboatTug | SteamNarrowboatTug |
| SteamNarrowboatBulk | SteamNarrowboat |
| SteamNarrowboatCool | SteamNarrowboat |
| SteamNarrowboatLivestock | SteamNarrowboat |
| SteamNarrowboatLong | SteamNarrowboat |
| SteamNarrowboatOil | SteamNarrowboat |
| SteamNarrowboatPiece | SteamNarrowboat |
| SteelHullDumbBargeBulk | UNPOWERED |
| SteelHullDumbBargeCool | UNPOWERED |
| SteelHullDumbBargeLivestock | UNPOWERED |
| SteelHullDumbBargeLong | UNPOWERED |
| SteelHullDumbBargeOil | UNPOWERED |
| SteelHullDumbBargePiece | UNPOWERED |
| SteelHullUnpoweredNarrowboatBulk | UNPOWERED |
| SteelHullUnpoweredNarrowboatCool | UNPOWERED |
| SteelHullUnpoweredNarrowboatLivestock | UNPOWERED |
| SteelHullUnpoweredNarrowboatLong | UNPOWERED |
| SteelHullUnpoweredNarrowboatOil | UNPOWERED |
| SteelHullUnpoweredNarrowboatPiece | UNPOWERED |
| SteelRiverSteamer | SteelRiverSteamer |
| Super-Loch | Super-Loch |
| ThamesSailingBargeBulk | SAIL |
| ThamesSailingBargeCool | SAIL |
| ThamesSailingBargeLivestock | SAIL |
| ThamesSailingBargeLong | SAIL |
| ThamesSailingBargePiece | SAIL |
| ThameslineRiverbus | ThameslineRiverbus |
| TowpathTractor | TowpathTractor |
| TSSKingEdward | TSSKingEdward |
| TSSQueenMary | TSSQueenMary |
| TubBoatBulk | UNPOWERED |
| TubBoatCool | UNPOWERED |
| TubBoatLong | UNPOWERED |
| TubBoatPiece | UNPOWERED |
| DieselTug | DieselTug |
| IronSteamTug | IronSteamTug |
| TugBargeBulk | UNPOWERED |
| TugBargeCool | UNPOWERED |
| TugBargeLivestock | UNPOWERED |
| TugBargeLong | UNPOWERED |
| TugBargeOil | UNPOWERED |
| TugBargePiece | UNPOWERED |
| WoodenPaddleTug | WoodenPaddleTug |
| TyneFerry | TyneFerry |
| FlyboatCool | UNPOWERED |
| FlyboatMail | UNPOWERED |
| FlyboatPax | UNPOWERED |
| FlyboatPiece | UNPOWERED |
| WoodenHullDumbBargeBulk | UNPOWERED |
| WoodenHullDumbBargeCool | UNPOWERED |
| WoodenHullDumbBargeLivestock | UNPOWERED |
| WoodenHullDumbBargeLong | UNPOWERED |
| WoodenHullDumbBargeOil | UNPOWERED |
| WoodenHullDumbBargePiece | UNPOWERED |
| WoodenHullUnpoweredNarrowboatBulk | UNPOWERED |
| WoodenHullUnpoweredNarrowboatCool | UNPOWERED |
| WoodenHullUnpoweredNarrowboatLivestock | UNPOWERED |
| WoodenHullUnpoweredNarrowboatLong | UNPOWERED |
| WoodenHullUnpoweredNarrowboatOil | UNPOWERED |
| WoodenHullUnpoweredNarrowboatPiece | UNPOWERED |
| WoodenPaddleSteamer | WoodenPaddleSteamer |
| WoodenRiverSteamer | WoodenRiverSteamer |

## 4. Gaps and doubts

### 4.1 Unit mixing - must be resolved before applying

1. **`BTCLordWarden`** is oil-fired (1951 steam turbine) and is coded `engine_type=steam`. Its
 figure, **150,799**, is **millilitres of oil per km**, not grams of coal. Applied against the
 coal series it will be charged as if the number were grams of coal and will be far too cheap.
 Recommended fix: recode to `diesel` (the diesel series is per litre, which is what it burns).
 On the coal series it is about 15x too cheap over 1951-72 (coal 47 units in 1951 against
 diesel 739). If it must stay `steam`, convert the oil to the coal of equal energy first:
 150,799 ml/km x 0.84 kg/l = 126.7 kg oil/km x 42.7 MJ/kg = 5,410 MJ/km, and coal at
 29.3 MJ/kg gives 184,600 g/km. That is a fudge and I do not recommend it.
2. `SRInvicta` burned coal 1939-46 and oil 1946-52. Given in grams of coal for the whole life.
 If the pakset wants period fidelity it needs two objects, not one.

### 4.2 Objects whose `engine_type` looks like a slip in the `.dat`

These are diesel craft whose "Oil" cargo variant has the wrong traction type:

* `LightweightDieselBargeOil` - `engine_type=steam` in `diesel-light-barge.dat` (its five
 siblings are `diesel`; runningcost 4 against their 10). It is a diesel barge; the figure 714 is
 millilitres of diesel/km and needs `engine_type=diesel`.
* `DieselNarrowboatOil` - `engine_type=steam` in `diesel-narrowboat.dat` (siblings `diesel`,
 runningcost 3 against 6). Figure 500 ml/km; needs `engine_type=diesel`.
* `SemiDieselNarrowboatOil` - `engine_type=Diesel` with a capital D. Figure 536 ml/km. Whether
 makeobj accepts the capitalised spelling is not something I tested; worth checking, as the
 other five in the file are lower case.

The lower runningcost on all three Oil variants is probably why the traction type was changed
(the author was suppressing something), but the effect is that a diesel barge is priced as coal.

### 4.3 Power figures I substituted (all `ESTIMATE`)

Nineteen steam models and one diesel model use a horsepower I supplied because the pakset
`power` is impossible for the type. Each is flagged in the model table; the pakset value is in
brackets there. They are:

`ChannelPaddleSteamerHull` (4,760->1,200 ihp), `ChannelScrewSteamship` (4,760->1,500),
`ClydeCargoSteamerHull` (6,101->700), `ClydeSteamer` (1,341->300), `IronRiverSteamer` (670->200),
`SteelRiverSteamer` and `LargeSteelRiverSteamer` (670->300 each), `WoodenRiverSteamer` (161->80),
`WoodenPaddleSteamer` (121->50), `PSChevalier` (804->250), `PSComet` (74->20), `PSIndustry`
(268->30), `PSPremier` and `ps-premier-covered` (268->120 each), `SeineNetterSteam` (1,341->100),
`SteamBargeTug` (134->60), `SteamNarrowboatTug` (80->40), `WoodenPaddleTug` (134->50),
`IronSteamTug` (268->100), `SeineNetterDiesel` (1,250->200 kW).

The test I applied was whether the resulting coal per day was credible for a ship of that type
and date. A 1,341 ihp engine in an 1860 Clyde steamer implies 34 t of coal a day, which no
1860 steamer of that size carried. Substituting 300 ihp brings it to 8.2 t/day and brings the
fuel/maintenance ratio into the same band as the rest of the steam fleet. If the orchestrator
prefers to keep the pakset figures, the affected `fuel_per_km` values must be multiplied by
pakset ihp / substituted ihp; the model table gives both numbers.

### 4.4 Where the low end of the range may be too low

* `ClydePuffer` (3,780 g/km) is the weakest figure in the set. It rests on a single documented
 engine rating (the puffer *Cretan*, 100 ihp, 1910) and a 0.50 load factor; the folklore figure
 of "a ton of coal a day" for a puffer comes out at 1.36 t/day here, which is consistent, but
 no measured puffer coal log was found. The 1958 Ross & Marshall record of a puffer loading
 **17 tons 6 cwts of bunkers** for a Troon-Eriskay round trip suggests a much larger bunker
 capacity than consumption figure and does not help.
* `SteamNarrowboat` (1,990 g/km) is checked only against a modern replica (100 kg of coal for a
 day's steaming, `youtube.com/watch?v=AeD5iU36vYk`), not an 1889 boat. A working boat with a
 worn engine would be worse.

### 4.5 Sources I could not read in full

* The 1891 *Review of Marine Engineering* is a scanned PDF with no usable text layer when
 downloaded; I read the quoted tables from the publisher's page as returned by the search index,
 not by OCR. The three numbers used (2.11 for 1872, 1.828 for 1881, 1.522 for 1891) appear in
 its Table 6 and in the body text and are internally consistent.
* Project Gutenberg was returning HTTP 503 for the whole session, so *Ocean Steamships* (1891),
 the source of the 5.1 lb/ihp-h *Britannia* and 3.8 lb/ihp-h *Persia* figures, was read from the
 index extract of the page rather than the page itself. Both figures also appear in the
 secondary literature. If a citation-grade check is wanted, fetch
 `gutenberg.org/files/54136/54136-h/54136-h.htm` when it is back.
* The MAN and Wärtsilä SFOC figures come from the manufacturers' own PDFs located by search; I
 did not parse the PDFs themselves. The values (163-176 g/kWh two-stroke, 169 g/kWh
 medium-speed) are unremarkable and match the published project guides.

### 4.6 Judgement calls that could reasonably go the other way

* **Load factors.** The whole liquid-fuel set scales linearly with LF, so a different convention
 moves every diesel figure. I used the propeller-law justification and validated against the
 handysize and the narrowboat; a reader who thinks ships run harder at service speed would
 raise the ocean figures by 10-15%.
* **`HSS-1500` at 172,891 ml/km.** 68 MW of gas turbine at 0.65 load is 12.1 t/h; some published
 accounts put the class nearer 6.5 t/h at 40 kn, which would imply LF ~ 0.35. I could not
 source a consumption figure and kept the physical calculation. This is the least reliable
 large figure in the set.
* **`SSGreatEastern` at 303,325 g/km** (189 t/day at 14 kn) is the highest coal figure in the
 pakset by a factor of three. It is what 8,000 ihp at 3.6 lb/ihp-h gives, and the ship's
 15,000-ton coal capacity against a 35-day half-world voyage is consistent with roughly 190-430
 t/day, but no measured daily log was found.
* **Hovercraft traction types.** `SR-N4-Mountbatten-Mk1`, `SR-N4-Mountbatten-Mk3`,
 `SR-N6-Winchester` and the three petrol hovercraft burned kerosene in gas turbines, not diesel
 or petrol. The units are litres either way, so the arithmetic survives, but the price series
 used (`fuel[diesel]`, `fuel[petrol]`) is the wrong one; `fuel[turbine]` exists and is the jet
 fuel series. This is a pakset coding question, not a research gap.
* **`range`.** I have reported the existing `range` values as found and have not reviewed or
 changed any of them; `range` is a routing constraint, not a fuel quantity.

### 4.7 What I would do with more time

1. Pull Board of Trade coal-consumption returns for 1900-1914 cross-Channel and coastal
 steamers - that would replace the interpolated small-craft series with measurements for
 exactly the ships in `boats192`.
2. Get one measured coal log for a Clyde puffer and one for a steam narrowboat; both are the
 weakest anchors and both cover six objects.
3. Find a fuel-consumption figure for the HSS 1500 and the Incat 96 m from a ferry operator's
 submission, which would settle the fast-ferry load factors.
4. Check the 1830s-50s steamer power figures against Lloyd's Register returns, which record
 nominal horsepower for every British steamer; that would replace about a dozen estimates with
 measurements.
