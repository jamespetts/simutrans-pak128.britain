# Fuel consumption: non-steam rail traction (pak128.Britain-Ex)

Sector: every rail-guided object with `waytype` `track`, `tram_track`, `narrowgauge_track` or
`maglev_track` whose engine type is not steam. 2,071 objects in
`ai/temp/sector-rail-nonsteam.txt`.

Numbers below are candidates for `fuel_per_km`, `calibration_speed` and `cut_off_speed`. Nothing
in `New/` was edited. Engine behaviour quoted here is from
`simutrans-extended-sources/vehicle/vehicle.cc` (`calc_fuel_consumption`, `is_at_full_power`) and
`descriptor/vehicle_desc.cc` (`get_fuel_cost_per_unit`).

---

## 1. Method

### 1.1 What the number is

`calc_fuel_consumption` charges `base * cal / v` at full power and scales by `v / vmax` at part
load, so `base * calibration_speed` is the fuel burned per hour at maximum output. For rail I take
the sector instruction literally:

- `calibration_speed` = the object's own top speed (`speed` in its `.dat`);
- `fuel_per_km` = the fuel or energy that object uses per km at that speed with its own engine or
  motors at rated output.

Every figure is therefore computed from the object's **own** `power` field, not from a unit total.
A multiple unit's consumption is the sum over its motor cars, which is what the engine does when it
charges each vehicle in the convoy. A car with `power=0` is charged 0 (see 1.10). This is the only
allocation that is both mechanical and consistent with the engine's per-vehicle charge; an
alternative (dividing a unit total equally across all cars) is discussed in 4.2.

Power is taken as the rated output at the shaft for diesel and petrol (BSFC is a shaft figure) and
at the rail for electric and maglev (so the line-to-rail loss is added by the efficiency divisor).
That matches the RSSB convention, which measures electric energy at the pantograph or shoe and
diesel energy as litres delivered to the tank.

### 1.2 Diesel and petrol

    fuel_per_km [ml/km] = P[kW] * BSFC[g/kWh] / rho[g/litre] / v[km/h] * 1000

`rho` = **835 g/litre**. BS EN 590 diesel is 820-845 kg/m3 at 15 C; the Sulzer 12LDA28 works test
quoted below used fuel of specific gravity 0.843 at 20 C
([derbysulzers.com](https://www.derbysulzers.com/sncf65500.html)). Petrol: 720 g/litre.

Brake-specific fuel consumption, from two independent contemporary sources:

| token | BSFC | applies to | source |
|---|---|---|---|
| `D228` | 228 g/kWh | all 1955-1985 diesel classes, including the Sulzer-engined 44-47 | Sulzer 12LDA28 UIC 100-hour test: 169 g/bhp·h at full load = 227 g/kWh ([derbysulzers.com](https://www.derbysulzers.com/sncf65500.html)), and the same page's Class 44 test gives 388-408 kg/h at 2,358 hp = 220-232 g/kWh; Roger Ford, "Freight diesel traction realities", *Modern Railways* 21 Mar 2019: the English Electric 12CSVT "were consuming 228g/kWh on full power" ([modernrailways.com](https://www.modernrailways.com/article/freight-diesel-traction-realities)) |
| `D230` | 230 g/kWh | SR 1-Co-Co-1 (10203), a one-off 1948 locomotive | ESTIMATE: the Sulzer figure rounded up, for an earlier and less developed engine |
| `D215` | 215 g/kWh | Paxman Valenta HST; Ruston-engined Classes 56/58 | ESTIMATE: between the 1950s-60s 227-228 and the 1980s 195-216, for high-speed four-strokes of the 1970s |
| `D210` | 210 g/kWh | 1985-1994 introductions | Ford, ibid.: the 1987 BR conference paper gave "worst new engine" 216 g/kWh and best 198 g/kWh |
| `D205` | 205 g/kWh | Class 66 (EMD 710) | ESTIMATE: General Motors never published a figure (Ford, ibid.); anchored on the 1987 band |
| `D200` | 200 g/kWh | 1995 and later | Ford, ibid.: the Mirrlees MB275 set the benchmark at 195 g/kWh and the 1987 best new engine was 198 g/kWh |
| `D195` | 195 g/kWh | Class 60 (Mirrlees MB275), Classes 68/70 (CAT C175, GE GEVO) | Ford, ibid.: "the Mirrlees MB275 set a new benchmark at 195g/kWh" |
| `D235` | 235 g/kWh | pre-1955 diesel railcars and the LMS 10000 | ESTIMATE: pre-war and immediate post-war rail engines were less efficient than the 1956 Sulzer; no measured figure found |
| `P300` | 300 g/kWh | NER petrol-electric railcar | ESTIMATE: 1920s petrol engines of 25-30% thermal efficiency |

Era assignment uses each object's `intro_year` from its `.dat`, with per-class overrides for the
classes whose engine is named in the sources (Class 37 = `D228`, Classes 44-47 = `D228`,
Class 50 = `D228`, Class 60 = `D195`, Class 66 = `D205`, Class 68/70 = `D195`, HST = `D215`).

Worked example, **BR-Class47** (1,922 kW, 153 km/h):

    1,922 * 228 = 438,216 g/h = 438.2 kg/h
    438.2 / 0.835 = 524.8 litres/h
    524.8 / 153 = 3.430 litres/km  ->  fuel_per_km = 3430

Worked example, **BR-Class43** HST power car (1,678 kW, 200 km/h):

    1,678 * 215 = 360,770 g/h = 360.8 kg/h
    360.8 / 0.835 = 432.1 litres/h
    432.1 / 200 = 2.160 litres/km  ->  fuel_per_km = 2160

### 1.3 Electric

    fuel_per_km [Wh/km] = P[kW] * 1000 / eta / v[km/h]

`eta` is the efficiency from the pantograph or shoe to the rail at rated output. The only published
figure found that states both ends is the Class 390 in RSSB's *Traction Energy Metrics*: "the
installed power is 5.1 MW at the rail or 6.7 MW at the overhead line", i.e. **eta = 0.76** for a
2000s 25 kV AC unit ([RSSB T618, Kemp 2007, p.20](https://kipdf.com/research-programme-engineering-traction-energy-metrics_5ac4bba31723dd375738e8f7.html)).
That is lower than the sum of transformer, converter, motor and gear losses alone would give, and it
is probably conservative, but it is measured and it is the right order.

| token | eta | applies to | basis |
|---|---|---|---|
| `E76` | 0.76 | 25 kV AC classes introduced 1990 or later | RSSB T618 Class 390, 5.1/6.7 MW |
| `E78` | 0.78 | 25 kV AC classes before 1990, and the LMS 6.6 kV AC units | ESTIMATE: transformer + rectifier + DC motors is a little worse than a modern converter drive; anchored on the 0.76 measurement |
| `E80` | 0.80 | DC traction introduced before 1930 | ESTIMATE: DC motors of the period at about 88% and gearing at 95%, with series resistance control still in circuit at rated speed |
| `E85` | 0.85 | DC traction 1930-1989 | ESTIMATE: no transformer; motors and gears only |
| `E88` | 0.88 | DC traction 1990 or later (chopper and inverter drives) | ESTIMATE: modern DC motor and gear efficiency, no transformer |

AC/DC classification is by class: Classes 81-92, 302-315, 317-325, 331-334, 345, 350, 360, 365,
370, 373, 374, 379, 385, 387, 390, 395, 397, 700, 720, 730, 745, 800 and 801 are 25 kV AC; the
Southern Region, London Underground, Mersey, Tyneside, L&YR, MSJ&A, LOR, DLR, Tyne and Wear and all
tram classes are DC. A misclassified class changes the answer by 9% at most.

Worked example, **BR-Class90** (3,730 kW, 177 km/h):

    3,730 / 0.78 = 4,782 kW at the pantograph
    4,782 * 1000 / 177 = 27,017 Wh/km

Worked example, **BR-390 motor car** (855 kW, 225 km/h):
855 / 0.76 = 1,125 kW; 1,125,000 / 225 = **5,000 Wh/km per motor car**; six motor cars = 30,000
Wh/km for the unit, against the published 6.7 MW at the overhead line / 225 km/h = 29,778 Wh/km.

### 1.4 Hydrogen fuel cell (maglev)

`engine_type=hydrogene` is a separate enum value from `fuel_cell`, so
`vehicle_desc_t::get_fuel_cost_per_unit` does not apply the round-trip efficiency fallback to it;
it calls `get_fuel_cost(year, hydrogene)` directly. `fuel[hydrogene]` in `New/config/fuel.tab` is
**commented out**, so that call returns 0 and maglev energy is currently free. The figures below are
therefore the **tank** energy that a hydrogen maglev would need, so that the values are right if a
hydrogen price is ever added:

    fuel_per_km [Wh/km] = P[kW] * 1000 / 0.85 / 0.50 / v[km/h]

0.85 is the linear-motor and converter loss, 0.50 the fuel-cell system efficiency (ESTIMATE for a
2030s unit; current automotive fuel cells are 50-60% at part load and lower at full power).

Worked example, **BR-Ultra-450** (3,400 kW, 430 km/h): 3,400/0.85/0.50 = 8,000 kW at the tank;
8,000,000/430 = 18,605 Wh/km.

### 1.5 Bio (horses) and unpowered objects

`fuel[bio]` is 0 for all years, and the file's own comment says fodder belongs in fixed
maintenance. All 15 horse objects (six standard-gauge, three narrow gauge, six tram) get
`fuel_per_km=0`.

### 1.6 Calibration speed and cut-off speed

`calibration_speed` is the object's own `speed`, including for a motor car inside a multiple unit
(the unit's speed and the car's are the same in this pakset). `cut_off_speed` is
`round(0.53 * calibration_speed)`, which reproduces the one existing precedent exactly
(`GNR-Stirling8Foot`: 75 -> 40). Because `base * cal` is fixed, the split between the two does not
change fuel per hour, only the shape of the part-load curve.

### 1.7 Validation against measured fleet consumption

RSSB T618 reports measured fleet figures for exactly the stock this sector covers. Comparing the
computed full-output figure for a whole unit with the measured average:

| unit | motor power in pakset (kW) | computed at full output | measured (RSSB T618) | computed / measured |
|---|---|---|---|---|
| Class 170, 3-car | 3 x 315 = 945 | 1,414 ml/km | 3 x 0.454 L/vehicle-km = 1,362 ml/km | 1.04 |
| HST 2+8 | 2 x 1,678 = 3,356 | 4,320 ml/km | 0.89 L/100 seat-km x 473 = 4,210 ml/km | 1.03 |
| Class 222, 9-car | 6 x 560 = 3,360 | 4,024 ml/km | 0.98 L/100 seat-km x 478 = 4,684 ml/km | 0.86 |
| Class 180, 5-car | 5 x 560 = 2,800 | 3,353 ml/km | 0.98 L/100 seat-km x 268 = 2,626 ml/km | 1.28 |
| Class 220, 4-car | 4 x 560 = 2,240 | 2,683 ml/km | 1.20 L/100 seat-km x 188 = 2,256 ml/km | 1.19 |
| Class 455, 4-car | 746 | 7,254 Wh/km | about 8,000 Wh/km (ESTIMATE, 2.0 kWh/car-km) | 0.91 |
| Class 357, 4-car | 4 x 500 = 2,000 | 14,205 Wh/km | 4 x 2.36 kWh/vehicle-km = 9,440 Wh/km | 1.50 |
| Class 91 + Mk4, 11 cars | 4,700 | 27,485 Wh/km | 11 x 1.51 = 16,610 Wh/km | 1.65 |
| Class 373, 20 cars | 2 x 6,100 = 12,200 | 53,509 Wh/km | 0.055 kWh/seat-km x 750 = 41,250 Wh/km | 1.30 |
| Class 390, 9 cars | 6 x 855 = 5,130 | 29,982 Wh/km | 6.7 MW at the OLE = 29,778 Wh/km; 9 x 1.85 kWh/vehicle-km = 16,650 Wh/km in service | 1.01 / 1.80 |

Diesel comes out within about 30% of the measured fleet average. Electric comes out 30-80% above
the measured *average*, and within 1% of installed input power for the one class where that is
published. The reason is structural, not an arithmetic error: a diesel multiple unit's engines run
near rated output at line speed, while an electric unit's installed power is used only while
accelerating. See 4.1 for what to do about that if a service-average figure is wanted instead.

Two independent checks from the forum thread agree with the diesel numbers: a 102 hp (76 kW) Gardner
railcar of 18 t 12 cwt returning 12 mpg at 45 mph ([topic 6521.35](https://forum.simutrans.com/index.php?topic=6521.35))
is 235 ml/km, against 272 ml/km computed at full output; and the late-1950s BR railbuses at 9 mpg
(31 L/100 km, [topic 6521.280](https://forum.simutrans.com/index.php?topic=6521.280)) are 314 ml/km,
against 326 ml/km computed for the 110 kW AC railbus.

The tram figures can be checked the same way against the UMIST measurements of UK tramcars
reproduced by Lewis Lesley (Blackpool Centenary 1.5 kWh/km, Manchester Metrolink 4.1, Croydon
Tramlink 3.9, Sheffield Supertram 4.5; [london-trams.com](http://www.london-trams.com/reducing_costs.html)):
the single Blackpool Centenary car computes at 1.43 kWh/km, 0.95 of measured; the articulated trams
compute at 1.31 times measured for Croydon, 1.66 for Metrolink and 3.50 for Sheffield, the last
because of the suspect 554 kW middle car noted in 4.4. The pattern is the same as for the EMUs: a
tram's installed power is much larger than its average demand, and the gap widens as the stock gets
more powerful.

### 1.8 Cost sanity check against `runningcost`

Fuel cost per km in Simucents is `fuel_per_km * fuel.tab_value / 1000`; `runningcost` is 1900 money
and is multiplied by the general index from `prices.tab` before the player sees it. Comparing the
two in the same (nominal) year:

| object | year | fuel_per_km | fuel cost/km | runningcost/km nominal | ratio |
|---|---|---|---|---|---|
| BR-Class43 | 1976 | 2160 | 7,417 | 14,347 | 0.52 |
| BR-Class47 | 1962 | 3430 | 3,728 | 5,541 | 0.67 |
| BR-Class90 | 1987 | 27,017 | 23,964 | 16,300 | 1.47 |
| BR-Class66 | 1998 | 4,879 | 61,812 | 50,013 | 1.24 |
| BR-390 motor car | 2003 | 5,000 | 6,910 | 9,951 | 0.69 |
| BR-455 motor car | 1985 | 7,253 | 6,535 | 2,434 | 2.68 |

Across all 568 powered objects with a running cost, the ratio has a median of 1.19; none is below
0.25, 46 are above 4 and one, the 1885 `Blackpool-Original` tram, above 10. The high
outliers are modern DMUs (fuel really is the larger cost) and pre-1930 trams, whose `runningcost` in
the pakset (13-38 Simucents/km) is very low: an LCC A-class tram at 1,758 Wh/km costs about 9 times
its running cost, which is high but an order of magnitude short of the "30 times means the unit is
wrong" test.

### 1.9 Power corrections applied

The brief warns that `power` is populated from mixed sources. Four corrections were applied; every
other object uses its `.dat` power unchanged.

| object(s) | `.dat` power | used | reason |
|---|---|---|---|
| `BR-Class43(...)`, `BR-Class43Rear(...)` (20 livery objects) | 2,010 kW | 1,678 kW | the compiled `BR-Class43` is 1,678 kW (2,250 hp Paxman Valenta); the livery folder is not in the Makefile and its figure is wrong |
| `BR-Class90(GNER)`, `BR-Class90(NationalExpress)` | 5,860 kW | 3,730 kW | the compiled `BR-Class90` is 3,730 kW (5,000 hp); 5,860 kW is not a Class 90 rating |
| `BR-Class88` | 4,700 kW | 2,980 kW | Class 88 is 4,000 hp (2,980 kW) in electric mode; 4,700 kW is the Class 92's rating |
| `BR-374(...)` (5 objects) | 2,000 kW | 3,200 kW | the e320 class is 16,000 kW over 16 cars; 5 x 2,000 = 10,000 kW understates it, 5 x 3,200 = 16,000 kW matches |

Known but **not** corrected, because the change would also alter acceleration and is outside this
brief: Class 357 motor cars are 500 kW each (2,000 kW for a 4-car unit) against a published 1,500 kW;
London Underground 1995/2009 stock cars are 500 kW against roughly 350 kW; the Class 800 diesel
rating is applied to six cars. Each is noted here so the figure can be revisited.

### 1.10 How the 1,476 zero-fuel objects are identified

The rule has two parts, and between them they cover 1,476 objects:

**(a) any object whose `power` field in the checklist is `0` or empty gets `fuel_per_km=0`** — 1,461
objects:

| group | count | how identified |
|---|---|---|
| no engine type at all (carriages, wagons, mail carriers, unpowered tram trailers) | 1,170 | `engine` column empty: 1,115 `track`, 48 `narrowgauge_track`, 7 `tram_track` |
| electric multiple-unit trailer cars and unpowered electric tram cars | 256 | `engine=electric`, `power` 0 (240 `track`, 16 `tram_track`) |
| diesel multiple-unit trailer cars and kitchen cars, declared diesel with no engine | 35 | `engine=diesel`, `power` 0 |

**(b) the 15 horse objects get `fuel_per_km=0`** — `engine=bio`, six standard gauge, three narrow
gauge, six tram. They carry `power=1` or `2` so rule (a) does not catch them. `fuel[bio]` is 0 for
every year.

`calibration_speed` and `cut_off_speed` are still stated for these (their own speed and 0.53 of it)
so that the fields are populated uniformly, but `calc_fuel_consumption` returns 0 before reading
them when `fuel_per_km` is 0.

---

## 2. Per-model table

One row per distinct traction rating: engine type, `power` (after the 1.9 corrections) and top
speed. Objects that share a rating share a row; the model label names the classes in the group (the
first three family names, then a count of further families). `basis` gives the parameter used and
`source` the token from the tables in 1.2-1.4:

- `MR2019` — Roger Ford, *Modern Railways* 21 Mar 2019, https://www.modernrailways.com/article/freight-diesel-traction-realities
- `Sulzer` — Sulzer 12LDA28 UIC test, https://www.derbysulzers.com/sncf65500.html
- `RSSB` — RSSB T618 *Traction Energy Metrics* (Kemp 2007), https://kipdf.com/research-programme-engineering-traction-energy-metrics_5ac4bba31723dd375738e8f7.html
- `SMT2004` — Shanghai maglev power test, http://www.maglev.ir/eng/documents/papers/conferences/maglev2004/topic4/IMT_CP_M2004_T4_2.pdf
- `EST` — estimate as set out in 1.2-1.4

`range` is blank for every object: no rail vehicle in this sector sets `range`.

| model | power kW | speed km/h | fuel_per_km | calibration_speed | cut_off_speed | range | basis | source |
|---|---|---|---|---|---|---|---|---|
| M1 BR-Class43 | 1678 | 200 | **2160** ml/km | 200 | 106 | - | diesel; 215 g/kWh | EST |
| M2 BR-Class90 | 3730 | 175 | **27326** Wh/km | 175 | 93 | - | electric; eta 0.78 | RSSB/EST |
| M3 BR-Class91 | 4700 | 225 | **26781** Wh/km | 225 | 119 | - | electric; eta 0.78 | RSSB/EST |
| M4 1890TubeStockLoco | 85 | 40 | **2656** Wh/km | 40 | 21 | - | electric; eta 0.80 | EST |
| M5 1898TubeStock | 50 | 50 | **1250** Wh/km | 50 | 26 | - | electric; eta 0.80 | EST |
| M6 1903TubeStock | 100 | 50 | **2500** Wh/km | 50 | 26 | - | electric; eta 0.80 | EST |
| M7 1920TubeStockAirDoor / 1906TubeStock / WatfordJointStock | 120 | 60 | **2500** Wh/km | 60 | 32 | - | electric; eta 0.80 | EST |
| M8 1914TubeStock / 1915TubeStock | 150 | 60 | **3125** Wh/km | 60 | 32 | - | electric; eta 0.80 | EST |
| M9 1923TubeStock | 200 | 72 | **3472** Wh/km | 72 | 38 | - | electric; eta 0.80 | EST |
| M10 1923TubeStock | 150 | 72 | **2604** Wh/km | 72 | 38 | - | electric; eta 0.80 | EST |
| M11 1938TubeStock / 1938TubeStockNDM / LUL_OP_StockFrontDM +4 more | 220 | 72 | **3595** Wh/km | 72 | 38 | - | electric; eta 0.85 | EST |
| M12 1940TubeStock | 283 | 60 | **5549** Wh/km | 60 | 32 | - | electric; eta 0.85 | EST |
| M13 1959TubeStock | 300 | 90 | **3922** Wh/km | 90 | 48 | - | electric; eta 0.85 | EST |
| M14 1967TubeStock / 1967TubeStockMiddle2 | 400 | 100 | **4706** Wh/km | 100 | 53 | - | electric; eta 0.85 | EST |
| M15 1973TubeStockFrontDM / 1973TubeStockFrontUNDM / 1973TubeStockRearDM +5 more | 300 | 100 | **3529** Wh/km | 100 | 53 | - | electric; eta 0.85 | EST |
| M16 1983TubeStockFrontDM / 1983TubeStockFrontUNDM / 1983TubeStockRearDM +1 more | 350 | 100 | **4118** Wh/km | 100 | 53 | - | electric; eta 0.85 | EST |
| M17 1992TubeStock / 1992TubeStockMiddle1 / 1992TubeStockMiddle2 | 275 | 100 | **3125** Wh/km | 100 | 53 | - | electric; eta 0.88 | EST |
| M18 1995TubeStockFrontDM / 1995TubeStockFrontUNDM / 1995TubeStockRearDM +6 more | 500 | 100 | **5682** Wh/km | 100 | 53 | - | electric; eta 0.88 | EST |
| M19 BR-Class483 / BR-Class483NDM | 250 | 72 | **4085** Wh/km | 72 | 38 | - | electric; eta 0.85 | EST |
| M20 BR-Class485 | 200 | 72 | **3268** Wh/km | 72 | 38 | - | electric; eta 0.85 | EST |
| M21 1900TubeLoco | 150 | 50 | **3750** Wh/km | 50 | 26 | - | electric; eta 0.80 | EST |
| M22 District_A_StockFrontDM / District_A_StockRearDM | 280 | 60 | **5833** Wh/km | 60 | 32 | - | electric; eta 0.80 | EST |
| M23 District_BCD_StockFrontDM / District_BCD_StockRearDM / District_E_StockFrontDM +1 more | 298 | 65 | **5731** Wh/km | 65 | 34 | - | electric; eta 0.80 | EST |
| M24 DistrictElectricLoco | 596 | 65 | **11462** Wh/km | 65 | 34 | - | electric; eta 0.80 | EST |
| M25 District_F_StockFrontDM / District_F_StockRearDM | 440 | 72 | **7639** Wh/km | 72 | 38 | - | electric; eta 0.80 | EST |
| M26 District_G_StockFrontDM / District_G_StockRearDM | 300 | 70 | **5357** Wh/km | 70 | 37 | - | electric; eta 0.80 | EST |
| M27 District_KLMN_StockFrontDM / District_KLMN_StockRearDM | 325 | 72 | **5642** Wh/km | 72 | 38 | - | electric; eta 0.80 | EST |
| M28 DLR-B07 | 150 | 85 | **2005** Wh/km | 85 | 45 | - | electric; eta 0.88 | EST |
| M29 DLR-B92 | 140 | 80 | **1989** Wh/km | 80 | 42 | - | electric; eta 0.88 | EST |
| M30 DLR-P86 | 131 | 80 | **1926** Wh/km | 80 | 42 | - | electric; eta 0.85 | EST |
| M31 LUL_A_StockFrontDM / LUL_A_StockRearDM | 335 | 110 | **3583** Wh/km | 110 | 58 | - | electric; eta 0.85 | EST |
| M32 LUL_C_StockFrontDM / LUL_C_StockRearDM | 350 | 90 | **4575** Wh/km | 90 | 48 | - | electric; eta 0.85 | EST |
| M33 LUL_S_Stock | 400 | 100 | **4545** Wh/km | 100 | 53 | - | electric; eta 0.88 | EST |
| M34 Metropolitan1905Gate | 440 | 65 | **8462** Wh/km | 65 | 34 | - | electric; eta 0.80 | EST |
| M35 Metropolitan1913Circle | 600 | 65 | **11538** Wh/km | 65 | 34 | - | electric; eta 0.80 | EST |
| M36 Metropolitan1921Circle | 600 | 67 | **11194** Wh/km | 67 | 36 | - | electric; eta 0.80 | EST |
| M37 MetBTHLoco / MetCamelbackLoco | 640 | 80 | **10000** Wh/km | 80 | 42 | - | electric; eta 0.80 | EST |
| M38 Metropolitan-Motor-Third-Back / Metropolitan-Motor-Third | 400 | 65 | **7692** Wh/km | 65 | 34 | - | electric; eta 0.80 | EST |
| M39 met-mv-stock | 410 | 65 | **7885** Wh/km | 65 | 34 | - | electric; eta 0.80 | EST |
| M40 Metropolitan-Vickers | 890 | 105 | **10595** Wh/km | 105 | 56 | - | electric; eta 0.80 | EST |
| M41 BR-M-Class9000 | 800 | 180 | **10458** Wh/km | 180 | 95 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M42 RMU-aerocab | 500 | 320 | **3676** Wh/km | 320 | 170 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M43 RMUbox | 1600 | 320 | **11765** Wh/km | 320 | 170 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M44 RMUflat | 800 | 160 | **11765** Wh/km | 160 | 85 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M45 BR-Ultra-450 | 3400 | 430 | **18605** Wh/km | 430 | 228 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M46 BR-Ultra-520 | 5000 | 525 | **22409** Wh/km | 525 | 278 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M47 BR-Ultra-520DD | 5100 | 525 | **22857** Wh/km | 525 | 278 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M48 BR-Ultra-Mail | 3400 | 450 | **17778** Wh/km | 450 | 238 | - | fuel cell; eta 0.85 x FC 0.50 | SMT2004 |
| M49 Baguely-Drewery-0-6-0 | 186 | 60 | **846** ml/km | 60 | 32 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M50 Funkey-Deisel | 265 | 60 | **1206** ml/km | 60 | 32 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M51 Hibberd-Planet | 134 | 60 | **629** ml/km | 60 | 32 | - | diesel; 235 g/kWh | EST |
| M52 ac-railbus | 110 | 92 | **326** ml/km | 92 | 49 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M53 BR-101-DMBS / BR-101-DMCL / BR-104 +3 more | 224 | 113 | **541** ml/km | 113 | 60 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M54 BR-110-DMBC / BR-110-DMCL | 268 | 113 | **648** ml/km | 113 | 60 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M55 BR-120-DMBC / BR-120-DMSL | 224 | 109 | **561** ml/km | 109 | 58 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M56 BR-121 | 224 | 112 | **546** ml/km | 112 | 59 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M57 BR-123-DMBS / BR-123-DMS / BR-128 | 343 | 112 | **836** ml/km | 112 | 59 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M58 BR-127-DMBS | 355 | 113 | **858** ml/km | 113 | 60 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M59 BR-139 | 64 | 65 | **236** ml/km | 65 | 34 | - | diesel; 200 g/kWh | MR2019 |
| M60 br-141-0 | 153 | 121 | **345** ml/km | 121 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M61 br-141-1 | 172 | 121 | **357** ml/km | 121 | 64 | - | diesel; 210 g/kWh | MR2019 |
| M62 br-142-1 / br-144-1 | 172 | 120 | **360** ml/km | 120 | 64 | - | diesel; 210 g/kWh | MR2019 |
| M63 br-142 / br-144-0 | 153 | 120 | **321** ml/km | 120 | 64 | - | diesel; 210 g/kWh | MR2019 |
| M64 br-150 | 212 | 121 | **478** ml/km | 121 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M65 br-153 / br-156 | 212 | 120 | **444** ml/km | 120 | 64 | - | diesel; 210 g/kWh | MR2019 |
| M66 br-158 / BR-166 / BR-166Middle-Trolley | 260 | 145 | **451** ml/km | 145 | 77 | - | diesel; 210 g/kWh | MR2019 |
| M67 br-159 | 298 | 145 | **517** ml/km | 145 | 77 | - | diesel; 210 g/kWh | MR2019 |
| M68 BR-165 | 260 | 120 | **545** ml/km | 120 | 64 | - | diesel; 210 g/kWh | MR2019 |
| M69 BR-170 | 315 | 160 | **472** ml/km | 160 | 85 | - | diesel; 200 g/kWh | MR2019 |
| M70 BR-172-0 | 360 | 120 | **719** ml/km | 120 | 64 | - | diesel; 200 g/kWh | MR2019 |
| M71 BR-172-2 | 360 | 160 | **539** ml/km | 160 | 85 | - | diesel; 200 g/kWh | MR2019 |
| M72 BR-175 / BR-175Middle | 340 | 160 | **509** ml/km | 160 | 85 | - | diesel; 200 g/kWh | MR2019 |
| M73 BR-180 / BR-180Middle-Buffet / BR-180Middle-first +5 more | 560 | 200 | **671** ml/km | 200 | 106 | - | diesel; 200 g/kWh | MR2019 |
| M74 BR-185 | 560 | 160 | **838** ml/km | 160 | 85 | - | diesel; 200 g/kWh | MR2019 |
| M75 BR-195 / BR-196 / BR-196Front +1 more | 390 | 160 | **584** ml/km | 160 | 85 | - | diesel; 200 g/kWh | MR2019 |
| M76 BR-202 | 370 | 120 | **842** ml/km | 120 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M77 BR-205 | 750 | 120 | **1707** ml/km | 120 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M78 BR-210-DM | 850 | 145 | **1601** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M79 BR-251 | 750 | 145 | **1412** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M80 BR-302 | 565 | 120 | **6036** Wh/km | 120 | 64 | - | electric; eta 0.78 | RSSB/EST |
| M81 BR-303 / BR-304Centre-Motor | 618 | 120 | **6603** Wh/km | 120 | 64 | - | electric; eta 0.78 | RSSB/EST |
| M82 BR-307 | 545 | 120 | **5823** Wh/km | 120 | 64 | - | electric; eta 0.78 | RSSB/EST |
| M83 BR-309-1 / BR-309 | 846 | 160 | **6779** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M84 BR-310-MBSO | 806 | 120 | **8611** Wh/km | 120 | 64 | - | electric; eta 0.78 | RSSB/EST |
| M85 BR-312-MBSO | 806 | 145 | **7126** Wh/km | 145 | 77 | - | electric; eta 0.78 | RSSB/EST |
| M86 BR-313 / BR-314 / BR-315 | 328 | 120 | **3504** Wh/km | 120 | 64 | - | electric; eta 0.78 | RSSB/EST |
| M87 BR-317-Motor / BR-319Engine | 990 | 160 | **7933** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M88 BR-318-Motor | 1072 | 145 | **9478** Wh/km | 145 | 77 | - | electric; eta 0.78 | RSSB/EST |
| M89 BR-320 | 1072 | 145 | **9728** Wh/km | 145 | 77 | - | electric; eta 0.76 | RSSB |
| M90 BR-321 | 1072 | 160 | **8590** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M91 BR-323 | 390 | 145 | **3539** Wh/km | 145 | 77 | - | electric; eta 0.76 | RSSB |
| M92 BR-325 | 990 | 160 | **8141** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M93 BR-331 / BR-331Motor | 880 | 160 | **7237** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M94 BR-332 / BR-333 | 700 | 160 | **5757** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M95 BR-334 | 400 | 145 | **3630** Wh/km | 145 | 77 | - | electric; eta 0.76 | RSSB |
| M96 BR-345 / BR-345MS3 / BR-345Panto | 440 | 145 | **3993** Wh/km | 145 | 77 | - | electric; eta 0.76 | RSSB |
| M97 BR-345 / BR-345Middle | 880 | 145 | **7985** Wh/km | 145 | 77 | - | electric; eta 0.76 | RSSB |
| M98 BR-350-1 | 750 | 177 | **5575** Wh/km | 177 | 94 | - | electric; eta 0.76 | RSSB |
| M99 BR-350-2 / BR-385 | 750 | 160 | **6168** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M100 c2c-357 / BR-375-6 / BR-377-7Middle2 +4 more | 500 | 160 | **3551** Wh/km | 160 | 85 | - | electric; eta 0.88 | EST |
| M101 BR-360 | 775 | 160 | **6373** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M102 BR-365 | 628 | 160 | **5164** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M103 BR-370 | 2983 | 250 | **15297** Wh/km | 250 | 132 | - | electric; eta 0.78 | RSSB/EST |
| M104 BR-373 | 6100 | 300 | **26754** Wh/km | 300 | 159 | - | electric; eta 0.76 | RSSB |
| M105 BR-374 | 3200 | 320 | **13158** Wh/km | 320 | 170 | - | electric; eta 0.76 | RSSB |
| M106 BR-376 / BR-376MiddlePower2 | 500 | 120 | **4735** Wh/km | 120 | 64 | - | electric; eta 0.88 | EST |
| M107 BR-378 / BR-378Middle2 / BR-465 | 600 | 120 | **5682** Wh/km | 120 | 64 | - | electric; eta 0.88 | EST |
| M108 BR-379 / BR-379Middle2 | 600 | 160 | **4934** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M109 BR-380 / BR-444 / BR-450 +4 more | 750 | 160 | **5327** Wh/km | 160 | 85 | - | electric; eta 0.88 | EST |
| M110 BR-387 / BR-387Middle2 | 600 | 177 | **4460** Wh/km | 177 | 94 | - | electric; eta 0.76 | RSSB |
| M111 BR-390 | 855 | 225 | **5000** Wh/km | 225 | 119 | - | electric; eta 0.76 | RSSB |
| M112 BR-395 | 840 | 225 | **4912** Wh/km | 225 | 119 | - | electric; eta 0.76 | RSSB |
| M113 BR-397 | 880 | 200 | **5789** Wh/km | 200 | 106 | - | electric; eta 0.76 | RSSB |
| M114 BR-410[CEP] | 375 | 145 | **3043** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M115 BR-414[HAP] | 370 | 140 | **3109** Wh/km | 140 | 74 | - | electric; eta 0.85 | EST |
| M116 BR-4EPB / SR-4DD | 373 | 120 | **3657** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M117 BR-419[MLV] | 373 | 145 | **3026** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M118 BR-421[CIG]Motor | 750 | 145 | **6085** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M119 BR-423-MBSO | 750 | 140 | **6303** Wh/km | 140 | 74 | - | electric; eta 0.85 | EST |
| M120 BR-430[REP] | 1200 | 145 | **9736** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M121 BR-442-Middle2 | 1200 | 160 | **8824** Wh/km | 160 | 85 | - | electric; eta 0.85 | EST |
| M122 BR-455-Motor | 746 | 121 | **7253** Wh/km | 121 | 64 | - | electric; eta 0.85 | EST |
| M123 BR-456-DMSO | 373 | 121 | **3503** Wh/km | 121 | 64 | - | electric; eta 0.88 | EST |
| M124 BR-489[GLV] | 370 | 145 | **3002** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M125 BR-501 | 740 | 120 | **7255** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M126 BR-506 | 552 | 120 | **5412** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M127 BR-507 | 328 | 120 | **3216** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M128 BR-700 | 850 | 160 | **6990** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M129 BR-707 | 850 | 160 | **6037** Wh/km | 160 | 85 | - | electric; eta 0.88 | EST |
| M130 BR-710 | 450 | 120 | **4261** Wh/km | 120 | 64 | - | electric; eta 0.88 | EST |
| M131 BR-717 | 400 | 137 | **3318** Wh/km | 137 | 73 | - | electric; eta 0.88 | EST |
| M132 BR-720 | 575 | 160 | **4729** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M133 BR-730-0 | 500 | 145 | **4537** Wh/km | 145 | 77 | - | electric; eta 0.76 | RSSB |
| M134 BR-730-2 / BR-730-2Middle | 500 | 177 | **3717** Wh/km | 177 | 94 | - | electric; eta 0.76 | RSSB |
| M135 BR-769Motor | 780 | 145 | **1288** ml/km | 145 | 77 | - | diesel; 200 g/kWh | MR2019 |
| M136 BR-800Composite18+58 / BR-800FrontMS / BR-800 +2 more | 700 | 200 | **838** ml/km | 200 | 106 | - | diesel; 200 g/kWh | MR2019 |
| M137 BR-801Composite18+58 / BR-801FrontMS / BR-801 +2 more | 904 | 225 | **5287** Wh/km | 225 | 119 | - | electric; eta 0.76 | RSSB |
| M138 BR-Class09 | 298 | 44 | **1849** ml/km | 44 | 23 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M139 BR-Class15 / BR-Class16 | 597 | 97 | **1681** ml/km | 97 | 51 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M140 BR-Class17 | 671 | 97 | **1889** ml/km | 97 | 51 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M141 BR-Class20 | 746 | 120 | **1697** ml/km | 120 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M142 BR-Class21 | 820 | 120 | **1866** ml/km | 120 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M143 BR-Class24 | 865 | 121 | **1952** ml/km | 121 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M144 BR-Class25 / BR-Class27 | 932 | 145 | **1755** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M145 BR-Class26 | 865 | 130 | **1817** ml/km | 130 | 69 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M146 BR-Class28 | 895 | 120 | **2037** ml/km | 120 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M147 BR-Class28-2 | 1230 | 120 | **2799** ml/km | 120 | 64 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M148 BR-Class29 | 1010 | 130 | **2121** ml/km | 130 | 69 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M149 BR-Class30 | 930 | 130 | **1953** ml/km | 130 | 69 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M150 BR-Class31-1 | 1097 | 145 | **2066** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M151 BR-Class33 | 1156 | 140 | **2255** ml/km | 140 | 74 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M152 BR-Class35 | 1305 | 145 | **2457** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M153 BR-Class37 | 1304 | 145 | **2456** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M154 BR-Class40 | 1490 | 145 | **2806** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M155 BR-Class41 | 1492 | 145 | **2810** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M156 BR-Class42 | 1692 | 145 | **3186** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M157 BR-Class45 | 1864 | 145 | **3510** ml/km | 145 | 77 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M158 BR-Class47 | 1922 | 153 | **3430** ml/km | 153 | 81 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M159 BR-Class50 | 2010 | 160 | **3430** ml/km | 160 | 85 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M160 BR-Class52 | 2025 | 140 | **3950** ml/km | 140 | 74 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M161 BR-Class55 | 2460 | 160 | **4198** ml/km | 160 | 85 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M162 BR-Class56 | 2420 | 130 | **4793** ml/km | 130 | 69 | - | diesel; 215 g/kWh | EST |
| M163 BR-Class57 | 2050 | 153 | **3209** ml/km | 153 | 81 | - | diesel; 200 g/kWh | MR2019 |
| M164 BR-Class58 | 2460 | 130 | **4872** ml/km | 130 | 69 | - | diesel; 215 g/kWh | EST |
| M165 BR-Class60 | 2300 | 97 | **5537** ml/km | 97 | 51 | - | diesel; 195 g/kWh | MR2019 |
| M166 BR-Class62 | 3000 | 175 | **4106** ml/km | 175 | 93 | - | diesel; 200 g/kWh | MR2019 |
| M167 BR-Class66 | 2385 | 120 | **4879** ml/km | 120 | 64 | - | diesel; 205 g/kWh | EST |
| M168 BR-Class67 | 2200 | 200 | **2635** ml/km | 200 | 106 | - | diesel; 200 g/kWh | MR2019 |
| M169 BR-Class68 | 2800 | 160 | **4087** ml/km | 160 | 85 | - | diesel; 195 g/kWh | MR2019 |
| M170 BR-Class70 | 2750 | 120 | **5352** ml/km | 120 | 64 | - | diesel; 195 g/kWh | MR2019 |
| M171 BR-Class71 | 1720 | 145 | **13955** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M172 BR-Class73 | 1059 | 145 | **8592** Wh/km | 145 | 77 | - | electric; eta 0.85 | EST |
| M173 BR-Class81 | 2390 | 160 | **19151** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M174 BR-Class83 | 2240 | 160 | **17949** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M175 BR-Class85 | 2400 | 160 | **19231** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M176 BR-Class86 | 3010 | 160 | **24119** Wh/km | 160 | 85 | - | electric; eta 0.78 | RSSB/EST |
| M177 BR-Class87 / BR-Class90 | 3730 | 177 | **27017** Wh/km | 177 | 94 | - | electric; eta 0.78 | RSSB/EST |
| M178 BR-Class88 | 2980 | 160 | **24507** Wh/km | 160 | 85 | - | electric; eta 0.76 | RSSB |
| M179 BR-Class89 | 4286 | 200 | **27474** Wh/km | 200 | 106 | - | electric; eta 0.78 | RSSB/EST |
| M180 BR-Class92 | 5040 | 140 | **47368** Wh/km | 140 | 74 | - | electric; eta 0.76 | RSSB |
| M181 BR-Derby-Lightweight-DMBS / BR-Derby-Lightweight-DMBS-single / BR-Derby-Lightweight-DMCL +1 more | 224 | 100 | **630** ml/km | 100 | 53 | - | diesel; 235 g/kWh | EST |
| M182 GWR-Gloucester-Parcel-Railcar / GWR-Gloucester-Railcar | 195 | 130 | **422** ml/km | 130 | 69 | - | diesel; 235 g/kWh | EST |
| M183 GWR-ParkRoyal-Railcar | 195 | 100 | **549** ml/km | 100 | 53 | - | diesel; 235 g/kWh | EST |
| M184 gwr-swindon-railcar-parcels / gwr-swindon-railcar / GWR-Swindon-Twinset | 154 | 112 | **387** ml/km | 112 | 59 | - | diesel; 235 g/kWh | EST |
| M185 leyland-railbus | 71 | 90 | **222** ml/km | 90 | 48 | - | diesel; 235 g/kWh | EST |
| M186 LMS-10000 | 1200 | 150 | **2251** ml/km | 150 | 80 | - | diesel; 235 g/kWh | EST |
| M187 BR-Class10800 | 617 | 110 | **1532** ml/km | 110 | 58 | - | diesel; 228 g/kWh | MR2019/Sulzer |
| M188 LMS-502 | 705 | 112 | **7405** Wh/km | 112 | 59 | - | electric; eta 0.85 | EST |
| M189 LMS-EMU | 792 | 110 | **9231** Wh/km | 110 | 58 | - | electric; eta 0.78 | RSSB/EST |
| M190 LNER-ClassEM1 | 1400 | 105 | **15686** Wh/km | 105 | 56 | - | electric; eta 0.85 | EST |
| M191 LNER-ClassEM2 | 2060 | 150 | **16157** Wh/km | 150 | 80 | - | electric; eta 0.85 | EST |
| M192 LNER-1937-Tyneside-EMU-MPV | 640 | 90 | **8366** Wh/km | 90 | 48 | - | electric; eta 0.85 | EST |
| M193 LNER-1937-Tyneside-EMU | 320 | 90 | **4183** Wh/km | 90 | 48 | - | electric; eta 0.85 | EST |
| M194 LOR-EMU | 52 | 60 | **1083** Wh/km | 60 | 32 | - | electric; eta 0.80 | EST |
| M195 LSWR-EMU | 402 | 97 | **5180** Wh/km | 97 | 51 | - | electric; eta 0.80 | EST |
| M196 L&YR-EMU | 552 | 89 | **7753** Wh/km | 89 | 47 | - | electric; eta 0.80 | EST |
| M197 Mersey-EMU-1923 | 186 | 70 | **3321** Wh/km | 70 | 37 | - | electric; eta 0.80 | EST |
| M198 Mersey-EMU | 175 | 70 | **3125** Wh/km | 70 | 37 | - | electric; eta 0.80 | EST |
| M199 MSJ&A-EMU | 978 | 97 | **11862** Wh/km | 97 | 51 | - | electric; eta 0.85 | EST |
| M200 NER-ClassEE1 | 1342 | 105 | **15976** Wh/km | 105 | 56 | - | electric; eta 0.80 | EST |
| M201 NER-ClassEF1 | 820 | 85 | **12059** Wh/km | 85 | 45 | - | electric; eta 0.80 | EST |
| M202 NER-ClassES1 | 480 | 75 | **8000** Wh/km | 75 | 40 | - | electric; eta 0.80 | EST |
| M203 ner-tyne-petrol-electric-railcar | 63 | 70 | **375** ml/km | 70 | 37 | - | petrol; 300 g/kWh | EST |
| M204 NER-Tyneside-mpv / NER-Tyneside-unit | 200 | 70 | **3571** Wh/km | 70 | 37 | - | electric; eta 0.80 | EST |
| M205 SR-1-Co-Co-1 | 1300 | 140 | **2558** ml/km | 140 | 74 | - | diesel; 230 g/kWh | EST |
| M206 SR-2-NOL | 410 | 97 | **4973** Wh/km | 97 | 51 | - | electric; eta 0.85 | EST |
| M207 sr-2hal / SR-4LAV / SR-401[BIL] | 410 | 120 | **4020** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M208 SR-3SUB | 410 | 97 | **5284** Wh/km | 97 | 51 | - | electric; eta 0.80 | EST |
| M209 SR-404[COR] | 336 | 121 | **3267** Wh/km | 121 | 64 | - | electric; eta 0.85 | EST |
| M210 SR-5-BEL / SR-6PAN | 671 | 120 | **6578** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M211 SR-4SUB | 412 | 120 | **4039** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M212 SR-CC | 1100 | 120 | **10784** Wh/km | 120 | 64 | - | electric; eta 0.85 | EST |
| M213 TyneWearMetroClass994 | 220 | 80 | **3235** Wh/km | 80 | 42 | - | electric; eta 0.85 | EST |
| M214 1-Deck-Closed / 2-Deck-Open / lut-type-z | 37 | 32 | **1445** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M215 Blackpool-Balloon / Blackpool-Brush / Blackpool-EE-Railcoach | 85 | 65 | **1538** Wh/km | 65 | 34 | - | electric; eta 0.85 | EST |
| M216 Blackpool-Centenary / Blackpool-Jubilee / Blackpool-ProgressTwin | 85 | 70 | **1429** Wh/km | 70 | 37 | - | electric; eta 0.85 | EST |
| M217 Blackpool-Coronation | 134 | 70 | **2252** Wh/km | 70 | 37 | - | electric; eta 0.85 | EST |
| M218 Blackpool-Dreadnought | 30 | 32 | **1172** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M219 Blackpool-Millenium | 85 | 70 | **1380** Wh/km | 70 | 37 | - | electric; eta 0.88 | EST |
| M220 Blackpool-Original | 22 | 30 | **917** Wh/km | 30 | 16 | - | electric; eta 0.80 | EST |
| M221 Blackpool-Standard / glasgow-standard-3 / sheffield-rocker-panel | 60 | 32 | **2344** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M222 Bombardier-Flexity-2 | 240 | 70 | **3896** Wh/km | 70 | 37 | - | electric; eta 0.88 | EST |
| M223 Flexity-Swift / Metrolink-T68A | 240 | 80 | **3409** Wh/km | 80 | 42 | - | electric; eta 0.88 | EST |
| M224 CAF-Edinburgh / CAF-Edinburgh-motor / CAF-Urbos-3 | 320 | 70 | **5195** Wh/km | 70 | 37 | - | electric; eta 0.88 | EST |
| M225 Croydon-Variobahn / bombardier-incentro | 180 | 80 | **2557** Wh/km | 80 | 42 | - | electric; eta 0.88 | EST |
| M226 feltham | 104 | 65 | **1882** Wh/km | 65 | 34 | - | electric; eta 0.85 | EST |
| M227 glasgow-coronation | 104 | 67 | **1826** Wh/km | 67 | 36 | - | electric; eta 0.85 | EST |
| M228 glasgow-cunarder | 107 | 67 | **1879** Wh/km | 67 | 36 | - | electric; eta 0.85 | EST |
| M229 glasgow-room-and-kitchen / sheffield-preston | 52 | 32 | **2031** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M230 glasgow-standard-1 / lcc-a-class / lcc-c-class +3 more | 45 | 32 | **1758** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M231 glasgow-standard-4 | 89 | 32 | **3477** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M232 lcc-e1-class / lcc-m-class | 63 | 32 | **2461** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M233 lcc-e3-class | 89 | 50 | **2094** Wh/km | 50 | 26 | - | electric; eta 0.85 | EST |
| M234 lcc-hr2-class | 104 | 50 | **2447** Wh/km | 50 | 26 | - | electric; eta 0.85 | EST |
| M235 Metrolink-T86 | 210 | 80 | **2983** Wh/km | 80 | 42 | - | electric; eta 0.88 | EST |
| M236 MidlandMetroT69 | 210 | 70 | **3409** Wh/km | 70 | 37 | - | electric; eta 0.88 | EST |
| M237 Sheffield-Roberts | 97 | 65 | **1756** Wh/km | 65 | 34 | - | electric; eta 0.85 | EST |
| M238 sheffield-standard | 75 | 32 | **2930** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
| M239 Sheffield-Supertram | 277 | 80 | **3935** Wh/km | 80 | 42 | - | electric; eta 0.88 | EST |
| M240 Sheffield-Supertram | 554 | 80 | **7869** Wh/km | 80 | 42 | - | electric; eta 0.88 | EST |
| M241 Sheffield-VosslohTramtrain | 290 | 100 | **3295** Wh/km | 100 | 53 | - | electric; eta 0.88 | EST |
| M242 Toastrack | 23 | 32 | **898** Wh/km | 32 | 17 | - | electric; eta 0.80 | EST |
## 3. Object mapping table

### 3.1 Objects that take `fuel_per_km=0`

Apply `fuel_per_km=0` under two rules, which together cover 1,476 objects.

**(a)** Every object in `ai/temp/sector-rail-nonsteam.txt` **whose `power` column is `0` or empty** —
1,461 objects. For these set `calibration_speed` to the object's own `speed` and `cut_off_speed` to
`round(0.53 * speed)`; both are inert because the engine returns 0 before reading them. The rule
catches:

- the 1,170 objects with no `engine_type` line (1,115 `track`, 48 `narrowgauge_track`,
  7 `tram_track`) — every carriage, wagon, mail vehicle, pulled trailer and unpowered tram car;
- the 256 electric multiple-unit trailer cars and unpowered electric tram cars that declare
  `engine_type=electric` with no motors (240 on `track`, 16 on `tram_track`);
- the 35 diesel multiple-unit trailer, kitchen and buffet cars that declare `engine_type=diesel`
  with no engine.

**(b)** The 15 objects with `engine=bio` — the horse-drawn vehicles, which have `power=1` or `2` and
so are not caught by (a). `fuel[bio]` is 0, and the fuel.tab comment puts fodder in fixed
maintenance.

The 291 objects in the second and third groups are the only judgement call: they belong to a powered
unit but develop no output themselves, and the model's figure is output-based, so they take 0 rather
than a share of the unit's energy. Their unit's total is the sum of its motor cars, which is the
unit's installed power. Section 4.2 discusses the alternative.

The 306 of these objects that **do** carry an engine type are listed individually below so that the
rule cannot be applied to the wrong object. The remaining 1,170 have no `engine_type` line at all
and take 0 without exception.

#### 3.1.1 Zero-fuel objects that declare an engine type

| object | engine | power | fuel_per_km | calibration_speed | cut_off_speed |
|---|---|---|---|---|---|
| 1898TubeStockMiddle | electric | 0 | 0 | 50 | 26 |
| 1900TubeStockTrailer | electric | 0 | 0 | 60 | 32 |
| 1920TubeStockAirDoorTrailer | electric | 0 | 0 | 60 | 32 |
| 1906TubeStockTrailer | electric | 0 | 0 | 60 | 32 |
| 1923TubeStockMiddle1 | electric | 0 | 0 | 72 | 38 |
| 1923TubeStockMiddle2 | electric | 0 | 0 | 72 | 38 |
| 1938TubeStockTrailer | electric | 0 | 0 | 72 | 38 |
| 1940TubeStockMiddle | electric | 0 | 0 | 60 | 32 |
| 1959TubeStockMiddle1 | electric | 0 | 0 | 90 | 48 |
| 1959TubeStockMiddle2 | electric | 0 | 0 | 90 | 48 |
| 1967TubeStockMiddle1 | electric | 0 | 0 | 100 | 53 |
| 1973TubeStockMiddle1 | electric | 0 | 0 | 100 | 53 |
| 1973TubeStockMiddle2 | electric | 0 | 0 | 100 | 53 |
| 1983TubeStockMiddle1 | electric | 0 | 0 | 100 | 53 |
| 1983TubeStockMiddle2 | electric | 0 | 0 | 100 | 53 |
| 1995TubeStockMiddle1 | electric | 0 | 0 | 100 | 53 |
| 1995TubeStockMiddle2 | electric | 0 | 0 | 100 | 53 |
| 2009TubeStockMiddle1 | electric | 0 | 0 | 100 | 53 |
| BR-Class483Trailer | electric | 0 | 0 | 72 | 38 |
| BR-Class485Middle1 | electric | 0 | 0 | 72 | 38 |
| BR-Class485Middle2 | electric | 0 | 0 | 72 | 38 |
| District_A_StockMiddle | electric | 0 | 0 | 60 | 32 |
| District_A_StockMiddle-first | electric | 0 | 0 | 60 | 32 |
| District_BCD_StockMiddle | electric | 0 | 0 | 65 | 34 |
| District_BCD_StockMiddle-first | electric | 0 | 0 | 65 | 34 |
| District_E_StockMiddle | electric | 0 | 0 | 65 | 34 |
| District_E_StockMiddle-first | electric | 0 | 0 | 65 | 34 |
| District_F_StockMiddle1 | electric | 0 | 0 | 72 | 38 |
| District_F_StockMiddle2 | electric | 0 | 0 | 72 | 38 |
| District_G_StockMiddle | electric | 0 | 0 | 70 | 37 |
| District_KLMN_StockMiddle | electric | 0 | 0 | 72 | 38 |
| LUL_A_StockMiddle1 | electric | 0 | 0 | 110 | 58 |
| LUL_A_StockMiddle2 | electric | 0 | 0 | 110 | 58 |
| LUL_C_StockMiddle1 | electric | 0 | 0 | 90 | 48 |
| LUL_C_StockMiddle2 | electric | 0 | 0 | 90 | 48 |
| LUL_D_StockMiddle1 | electric | 0 | 0 | 100 | 53 |
| LUL_D_StockMiddle2 | electric | 0 | 0 | 100 | 53 |
| LUL_OP_StockMiddle | electric | 0 | 0 | 72 | 38 |
| Metropolitan1905GateMiddle | electric | 0 | 0 | 65 | 34 |
| Metropolitan1913CircleMiddle | electric | 0 | 0 | 65 | 34 |
| Metropolitan1921CircleMiddle | electric | 0 | 0 | 67 | 36 |
| Metropolitan-Motor-First-Middle | electric | 0 | 0 | 65 | 34 |
| Metropolitan-Motor-Third-Middle | electric | 0 | 0 | 65 | 34 |
| met-mv-stock-centre | electric | 0 | 0 | 65 | 34 |
| met-mv-stock-centre-first | electric | 0 | 0 | 65 | 34 |
| WatfordJointStockMiddle | electric | 0 | 0 | 60 | 32 |
| narrowgauge-horse-clydesdale-single | bio | 0 | 0 | 11 | 6 |
| narrowgauge-horse-irish-draught-single | bio | 0 | 0 | 10 | 5 |
| narrowgauge-horse-shire-single | bio | 0 | 0 | 10 | 5 |
| BR-101-DTCL | diesel | 0 | 0 | 113 | 60 |
| BR-101-TSL | diesel | 0 | 0 | 113 | 60 |
| BR-104Middle | diesel | 0 | 0 | 113 | 60 |
| BR-110-TSL | diesel | 0 | 0 | 113 | 60 |
| BR-114-DTCL | diesel | 0 | 0 | 113 | 60 |
| BR-117-TCL | diesel | 0 | 0 | 113 | 60 |
| BR-120-TSLRB | diesel | 0 | 0 | 109 | 58 |
| BR-123-TBS | diesel | 0 | 0 | 112 | 59 |
| BR-123-TCK | diesel | 0 | 0 | 112 | 59 |
| BR-123-TS | diesel | 0 | 0 | 112 | 59 |
| BR-127-TS | diesel | 0 | 0 | 113 | 60 |
| BR-127-TSL | diesel | 0 | 0 | 113 | 60 |
| BR-202-buffet | diesel | 0 | 0 | 120 | 64 |
| BR-202-trailer | diesel | 0 | 0 | 120 | 64 |
| BR-202-trailer-first | diesel | 0 | 0 | 120 | 64 |
| BR-205Middle | diesel | 0 | 0 | 120 | 64 |
| BR-205Rear | diesel | 0 | 0 | 120 | 64 |
| BR-210-DTSOL | diesel | 0 | 0 | 145 | 77 |
| BR-210-TCOL | diesel | 0 | 0 | 145 | 77 |
| BR-210-TSO | diesel | 0 | 0 | 145 | 77 |
| BR-251FirstParlour | diesel | 0 | 0 | 145 | 77 |
| BR-251Kitchen | diesel | 0 | 0 | 145 | 77 |
| BR-251SecondParlour | diesel | 0 | 0 | 145 | 77 |
| BR-302(centre2) | electric | 0 | 0 | 120 | 64 |
| BR-302(front) | electric | 0 | 0 | 120 | 64 |
| BR-302(rear) | electric | 0 | 0 | 120 | 64 |
| BR-303Front | electric | 0 | 0 | 120 | 64 |
| BR-303Rear | electric | 0 | 0 | 120 | 64 |
| BR-304Centre-Trailer | electric | 0 | 0 | 120 | 64 |
| BR-304Front | electric | 0 | 0 | 120 | 64 |
| BR-304Rear | electric | 0 | 0 | 120 | 64 |
| BR-307(centre2) | electric | 0 | 0 | 120 | 64 |
| BR-307(front) | electric | 0 | 0 | 120 | 64 |
| BR-307(rear) | electric | 0 | 0 | 120 | 64 |
| BR-309-2Front | electric | 0 | 0 | 160 | 85 |
| BR-309Griddle | electric | 0 | 0 | 160 | 85 |
| BR-309Middle | electric | 0 | 0 | 160 | 85 |
| BR-309Rear | electric | 0 | 0 | 160 | 85 |
| BR-310-BDTSOL | electric | 0 | 0 | 120 | 64 |
| BR-310-DTCOL | electric | 0 | 0 | 120 | 64 |
| BR-310-TSO | electric | 0 | 0 | 120 | 64 |
| BR-312-BDTSOL | electric | 0 | 0 | 145 | 77 |
| BR-312-DTCOL | electric | 0 | 0 | 145 | 77 |
| BR-312-TSO | electric | 0 | 0 | 145 | 77 |
| BR-313Pantograph | electric | 0 | 0 | 120 | 64 |
| BR-314Pantograph | electric | 0 | 0 | 120 | 64 |
| BR-315Pantograph | electric | 0 | 0 | 120 | 64 |
| BR-315Trailer | electric | 0 | 0 | 120 | 64 |
| BR-317-Driving-Front | electric | 0 | 0 | 160 | 85 |
| BR-317-Driving-Rear | electric | 0 | 0 | 160 | 85 |
| BR-317-Trailer | electric | 0 | 0 | 160 | 85 |
| BR-318-Driving-Front | electric | 0 | 0 | 145 | 77 |
| BR-318-Driving-Rear | electric | 0 | 0 | 145 | 77 |
| BR-319Front | electric | 0 | 0 | 160 | 85 |
| BR-319FrontComposite | electric | 0 | 0 | 160 | 85 |
| BR-319Pantograph | electric | 0 | 0 | 160 | 85 |
| BR-319Rear | electric | 0 | 0 | 160 | 85 |
| BR-320(front) | electric | 0 | 0 | 145 | 77 |
| BR-320(rear) | electric | 0 | 0 | 145 | 77 |
| BR-321(front) | electric | 0 | 0 | 160 | 85 |
| BR-321(front-composite) | electric | 0 | 0 | 160 | 85 |
| BR-321(rear) | electric | 0 | 0 | 160 | 85 |
| BR-321(trailer) | electric | 0 | 0 | 160 | 85 |
| BR-325Front | electric | 0 | 0 | 160 | 85 |
| BR-325Middle | electric | 0 | 0 | 160 | 85 |
| BR-325Rear | electric | 0 | 0 | 160 | 85 |
| BR-331FrontPanto | electric | 0 | 0 | 160 | 85 |
| BR-331RearPanto | electric | 0 | 0 | 160 | 85 |
| BR-331Trailer | electric | 0 | 0 | 160 | 85 |
| BR-332(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-332(centre2) | electric | 0 | 0 | 160 | 85 |
| BR-333(centre-pantograph) | electric | 0 | 0 | 160 | 85 |
| BR-333(centre-trailer) | electric | 0 | 0 | 160 | 85 |
| BR-345TSW | electric | 0 | 0 | 145 | 77 |
| BR-350-1(centre1) | electric | 0 | 0 | 177 | 94 |
| BR-350-1(centre2) | electric | 0 | 0 | 177 | 94 |
| BR-350-2(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-350-2(centre2) | electric | 0 | 0 | 160 | 85 |
| c2c-357(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-360(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-360(centre2) | electric | 0 | 0 | 160 | 85 |
| BR-365Middle | electric | 0 | 0 | 160 | 85 |
| BR-365Power | electric | 0 | 0 | 160 | 85 |
| BR-370BrakeFirstFront | electric | 0 | 0 | 250 | 132 |
| BR-370BrakeFirstRear | electric | 0 | 0 | 250 | 132 |
| BR-370FrontCab | electric | 0 | 0 | 250 | 132 |
| BR-370RearCab | electric | 0 | 0 | 250 | 132 |
| BR-370RestaurantFront | electric | 0 | 0 | 250 | 132 |
| BR-370RestaurantRear | electric | 0 | 0 | 250 | 132 |
| BR-370TrailerFirst | electric | 0 | 0 | 250 | 132 |
| BR-370TrailerSecond | electric | 0 | 0 | 250 | 132 |
| BR-373Catering | electric | 0 | 0 | 300 | 159 |
| BR-373CateringRear | electric | 0 | 0 | 300 | 159 |
| BR-373Coach | electric | 0 | 0 | 300 | 159 |
| BR-373CoachFirstClass | electric | 0 | 0 | 300 | 159 |
| BR-373CoachFirstClassRear | electric | 0 | 0 | 300 | 159 |
| BR-373CoachRear | electric | 0 | 0 | 300 | 159 |
| BR-373FrontPower | electric | 0 | 0 | 300 | 159 |
| BR-373MiddleFront | electric | 0 | 0 | 300 | 159 |
| BR-373MiddleRear | electric | 0 | 0 | 300 | 159 |
| BR-373RearPower | electric | 0 | 0 | 300 | 159 |
| BR-374(panto) | electric | 0 | 0 | 320 | 170 |
| BR-375-6Panto | electric | 0 | 0 | 160 | 85 |
| BR-375Panto | electric | 0 | 0 | 160 | 85 |
| BR-376Middle | electric | 0 | 0 | 120 | 64 |
| BR-378Middle-unpowered | electric | 0 | 0 | 120 | 64 |
| BR-379Panto | electric | 0 | 0 | 160 | 85 |
| BR-380(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-380(centre2) | electric | 0 | 0 | 160 | 85 |
| BR-385(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-385(centre2) | electric | 0 | 0 | 160 | 85 |
| BR-387Panto | electric | 0 | 0 | 177 | 94 |
| BR-390Coach | electric | 0 | 0 | 225 | 119 |
| BR-390FrontPantograph | electric | 0 | 0 | 225 | 119 |
| BR-390RearPantograph | electric | 0 | 0 | 225 | 119 |
| BR-395Front | electric | 0 | 0 | 225 | 119 |
| BR-395Rear | electric | 0 | 0 | 225 | 119 |
| BR-397FrontPanto | electric | 0 | 0 | 200 | 106 |
| BR-397MiddleTrailer | electric | 0 | 0 | 200 | 106 |
| BR-397RearPanto | electric | 0 | 0 | 200 | 106 |
| BR-410[CEP]Brake | electric | 0 | 0 | 145 | 77 |
| BR-410[CEP]Buffet | electric | 0 | 0 | 145 | 77 |
| BR-410[CEP]Middle | electric | 0 | 0 | 145 | 77 |
| BR-414[HAP]Rear | electric | 0 | 0 | 140 | 74 |
| BR-2EPB(rear) | electric | 0 | 0 | 120 | 64 |
| BR-4EPB(centre1) | electric | 0 | 0 | 120 | 64 |
| BR-4EPB(centre2) | electric | 0 | 0 | 120 | 64 |
| BR-421[CIG]Buffet | electric | 0 | 0 | 145 | 77 |
| BR-421[CIG]Front | electric | 0 | 0 | 145 | 77 |
| BR-421[CIG]Middle | electric | 0 | 0 | 145 | 77 |
| BR-421[CIG]Rear | electric | 0 | 0 | 145 | 77 |
| BR-423-DTCL-Front | electric | 0 | 0 | 140 | 74 |
| BR-423-DTCL-Rear | electric | 0 | 0 | 140 | 74 |
| BR-423-TSO | electric | 0 | 0 | 140 | 74 |
| BR-430[REP]Brake | electric | 0 | 0 | 145 | 77 |
| BR-430[REP]Buffet | electric | 0 | 0 | 145 | 77 |
| BR-430[REP]Middle | electric | 0 | 0 | 145 | 77 |
| BR-442-Front | electric | 0 | 0 | 160 | 85 |
| BR-442-Middle1 | electric | 0 | 0 | 160 | 85 |
| BR-442-Middle3 | electric | 0 | 0 | 160 | 85 |
| BR-442-Rear | electric | 0 | 0 | 160 | 85 |
| BR-444(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-444(centre2) | electric | 0 | 0 | 160 | 85 |
| BR-444(centre3) | electric | 0 | 0 | 160 | 85 |
| BR-450(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-450(centre2) | electric | 0 | 0 | 160 | 85 |
| BR-455-Driving-Front | electric | 0 | 0 | 121 | 64 |
| BR-455-Driving-Rear | electric | 0 | 0 | 121 | 64 |
| BR-455-Trailer | electric | 0 | 0 | 121 | 64 |
| BR-456-DTSO | electric | 0 | 0 | 121 | 64 |
| BR-458(centre1) | electric | 0 | 0 | 160 | 85 |
| BR-460-TCO | electric | 0 | 0 | 160 | 85 |
| BR-460-TFO | electric | 0 | 0 | 160 | 85 |
| BR-460-TSO | electric | 0 | 0 | 160 | 85 |
| BR-465Middle | electric | 0 | 0 | 120 | 64 |
| BR-501(DTB) | electric | 0 | 0 | 120 | 64 |
| BR-501(T) | electric | 0 | 0 | 120 | 64 |
| BR-506Centre | electric | 0 | 0 | 120 | 64 |
| BR-506Rear | electric | 0 | 0 | 120 | 64 |
| BR-507(centre1) | electric | 0 | 0 | 120 | 64 |
| BR-507(centre2) | electric | 0 | 0 | 120 | 64 |
| BR-700MiddleTrailer | electric | 0 | 0 | 160 | 85 |
| BR-700Panto | electric | 0 | 0 | 160 | 85 |
| BR-700PantoRear | electric | 0 | 0 | 160 | 85 |
| BR-700TSOLW | electric | 0 | 0 | 160 | 85 |
| BR-700TSOW | electric | 0 | 0 | 160 | 85 |
| BR-701TLW | electric | 0 | 0 | 160 | 85 |
| BR-707MiddleTrailer | electric | 0 | 0 | 160 | 85 |
| BR-707Panto | electric | 0 | 0 | 160 | 85 |
| BR-707TSOW | electric | 0 | 0 | 160 | 85 |
| BR-717MiddleTrailer | electric | 0 | 0 | 137 | 73 |
| BR-717Panto | electric | 0 | 0 | 137 | 73 |
| BR-717TSOW | electric | 0 | 0 | 137 | 73 |
| BR-720Front | electric | 0 | 0 | 160 | 85 |
| BR-769Front | diesel | 0 | 0 | 145 | 77 |
| BR-769FrontComposite | diesel | 0 | 0 | 145 | 77 |
| BR-769Pantograph | diesel | 0 | 0 | 145 | 77 |
| BR-769Rear | diesel | 0 | 0 | 145 | 77 |
| BR-800Front | diesel | 0 | 0 | 200 | 106 |
| BR-800MiddleTrailer | diesel | 0 | 0 | 200 | 106 |
| BR-800Rear | diesel | 0 | 0 | 200 | 106 |
| BR-800Rear-compact | diesel | 0 | 0 | 200 | 106 |
| BR-800Rear-trolley | diesel | 0 | 0 | 200 | 106 |
| BR-801Front | electric | 0 | 0 | 225 | 119 |
| BR-801MiddleTrailer | electric | 0 | 0 | 225 | 119 |
| BR-801Rear | electric | 0 | 0 | 225 | 119 |
| BR-801Rear-compact | electric | 0 | 0 | 225 | 119 |
| BR-801Rear-trolley | electric | 0 | 0 | 225 | 119 |
| BR-Derby-Lightweight-DTCL | diesel | 0 | 0 | 100 | 53 |
| BR-Derby-Lightweight-TBSL | diesel | 0 | 0 | 100 | 53 |
| BR-Derby-Lightweight-TSL | diesel | 0 | 0 | 100 | 53 |
| rail-horse-cleveland-bay-single | bio | 0 | 0 | 14 | 7 |
| rail-horse-friesian-single | bio | 0 | 0 | 12 | 6 |
| rail-horse-yorkshire-coach-single | bio | 0 | 0 | 18 | 10 |
| LMS-502Middle | electric | 0 | 0 | 112 | 59 |
| LMS-502MiddleComposite | electric | 0 | 0 | 112 | 59 |
| LMS-502Rear | electric | 0 | 0 | 112 | 59 |
| LMS-EMU-centre-trailer | electric | 0 | 0 | 110 | 58 |
| LMS-EMU-driving-trailer | electric | 0 | 0 | 110 | 58 |
| LNER-1937-Tyneside-EMU-rear | electric | 0 | 0 | 90 | 48 |
| LNER-1937-Tyneside-EMU-rear-composite | electric | 0 | 0 | 90 | 48 |
| LOR-EMU(trailer) | electric | 0 | 0 | 60 | 32 |
| LSWR-EMU(centre) | electric | 0 | 0 | 97 | 51 |
| L&YR-EMU-driving-trailer | electric | 0 | 0 | 89 | 47 |
| Mersey-EMU-1923(trailer) | electric | 0 | 0 | 70 | 37 |
| Mersey-EMU-1923(trailer-first) | electric | 0 | 0 | 70 | 37 |
| Mersey-EMU(trailer) | electric | 0 | 0 | 70 | 37 |
| Mersey-EMU(trailer-first) | electric | 0 | 0 | 70 | 37 |
| MSJ&A-EMU-centre-trailer | electric | 0 | 0 | 97 | 51 |
| MSJ&A-EMU-driving-trailer | electric | 0 | 0 | 97 | 51 |
| NER-Tyneside-unit(driving trailer) | electric | 0 | 0 | 70 | 37 |
| NER-Tyneside-unit(trailer1) | electric | 0 | 0 | 70 | 37 |
| NER-Tyneside-unit(trailer2) | electric | 0 | 0 | 70 | 37 |
| rail-horse-clydesdale-single | bio | 0 | 0 | 11 | 6 |
| rail-horse-irish-draught-single | bio | 0 | 0 | 10 | 5 |
| rail-horse-shire-single | bio | 0 | 0 | 10 | 5 |
| SR-2-NOL-rear | electric | 0 | 0 | 97 | 51 |
| sr-2hal-rear | electric | 0 | 0 | 120 | 64 |
| SR-3SUB(centre) | electric | 0 | 0 | 97 | 51 |
| SR-4LAV(centre1) | electric | 0 | 0 | 120 | 64 |
| SR-4LAV(centre2) | electric | 0 | 0 | 120 | 64 |
| SR-401[BIL]Rear | electric | 0 | 0 | 120 | 64 |
| SR-404[COR]Middle-Buf | electric | 0 | 0 | 121 | 64 |
| SR-404[COR]Middle-Res | electric | 0 | 0 | 121 | 64 |
| SR-404[COR]Middle1 | electric | 0 | 0 | 121 | 64 |
| SR-404[COR]Middle2 | electric | 0 | 0 | 121 | 64 |
| SR-6PAN(buffet) | electric | 0 | 0 | 120 | 64 |
| SR-6PAN(trailer1) | electric | 0 | 0 | 120 | 64 |
| SR-6PAN(trailer2) | electric | 0 | 0 | 120 | 64 |
| SR-6PAN(trailer4) | electric | 0 | 0 | 120 | 64 |
| pullman-kitchen-composite | electric | 0 | 0 | 120 | 64 |
| SR-4SUB(centre1) | electric | 0 | 0 | 120 | 64 |
| SR-4SUB(centre2) | electric | 0 | 0 | 120 | 64 |
| SR-4DD-TT1 | electric | 0 | 0 | 120 | 64 |
| SR-4DD-TT2 | electric | 0 | 0 | 120 | 64 |
| Bombardier-Flexity-2-middle1 | electric | 0 | 0 | 70 | 37 |
| Bombardier-Flexity-2-middle2 | electric | 0 | 0 | 70 | 37 |
| Bombardier-Flexity-2-panto | electric | 0 | 0 | 70 | 37 |
| CAF-Edinburgh-bogie | electric | 0 | 0 | 70 | 37 |
| CAF-Edinburgh-middle1 | electric | 0 | 0 | 70 | 37 |
| CAF-Edinburgh-middle2 | electric | 0 | 0 | 70 | 37 |
| CAF-Edinburgh-panto | electric | 0 | 0 | 70 | 37 |
| CAF-Urbos-3-middle1 | electric | 0 | 0 | 70 | 37 |
| CAF-Urbos-3-middle2 | electric | 0 | 0 | 70 | 37 |
| CAF-Urbos-3-panto | electric | 0 | 0 | 70 | 37 |
| Croydon-Variobahn-middle1 | electric | 0 | 0 | 80 | 42 |
| Croydon-Variobahn-middle2 | electric | 0 | 0 | 80 | 42 |
| Croydon-Variobahn-panto | electric | 0 | 0 | 80 | 42 |
| bombardier-incentro-middle1 | electric | 0 | 0 | 80 | 42 |
| bombardier-incentro-middle2 | electric | 0 | 0 | 80 | 42 |
| bombardier-incentro-panto | electric | 0 | 0 | 80 | 42 |
| tram-horse-clydesdale-double | bio | 0 | 0 | 11 | 6 |
| tram-horse-clydesdale-single | bio | 0 | 0 | 11 | 6 |
| tram-horse-irish-draught-double | bio | 0 | 0 | 10 | 5 |
| tram-horse-irish-draught-single | bio | 0 | 0 | 10 | 5 |
| tram-horse-shire-double | bio | 0 | 0 | 10 | 5 |
| tram-horse-shire-single | bio | 0 | 0 | 10 | 5 |

### 3.2 Objects with a non-zero figure

595 objects, one row each.

| object | model | fuel_per_km | calibration_speed | cut_off_speed |
|---|---|---|---|---|
| BR-Class43(BlueGrey) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(BlueGrey) | M1 | 2160 | 200 | 106 |
| BR-Class43(FGW1) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(FGW1) | M1 | 2160 | 200 | 106 |
| BR-Class43(FGW2) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(FGW2) | M1 | 2160 | 200 | 106 |
| BR-Class43(FGW3) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(FGW3) | M1 | 2160 | 200 | 106 |
| BR-Class43(GrandCentralOriginal) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(GrandCentralOriginal) | M1 | 2160 | 200 | 106 |
| BR-Class43(GrandCentralDaylight) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(GrandCentralDaylight) | M1 | 2160 | 200 | 106 |
| BR-Class43(GNER) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(GNER) | M1 | 2160 | 200 | 106 |
| BR-Class43(GWT) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(GWT) | M1 | 2160 | 200 | 106 |
| BR-Class43(IntercitySwallow) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(IntercitySwallow) | M1 | 2160 | 200 | 106 |
| BR-Class43(NationalExpress) | M1 | 2160 | 200 | 106 |
| BR-Class43Rear(NationalExpress) | M1 | 2160 | 200 | 106 |
| BR-Class90(GNER) | M2 | 27326 | 175 | 93 |
| BR-Class90(NationalExpress) | M2 | 27326 | 175 | 93 |
| BR-Class91(EastCoast) | M3 | 26781 | 225 | 119 |
| BR-Class91(GNER) | M3 | 26781 | 225 | 119 |
| BR-Class91(NXEC) | M3 | 26781 | 225 | 119 |
| 1890TubeStockLoco | M4 | 2656 | 40 | 21 |
| 1898TubeStockFront | M5 | 1250 | 50 | 26 |
| 1898TubeStockRear | M5 | 1250 | 50 | 26 |
| 1903TubeStockFront | M6 | 2500 | 50 | 26 |
| 1903TubeStockRear | M6 | 2500 | 50 | 26 |
| 1920TubeStockAirDoorFront | M7 | 2500 | 60 | 32 |
| 1920TubeStockAirDoorRear | M7 | 2500 | 60 | 32 |
| 1906TubeStockFront | M7 | 2500 | 60 | 32 |
| 1906TubeStockRear | M7 | 2500 | 60 | 32 |
| 1914TubeStockFront | M8 | 3125 | 60 | 32 |
| 1914TubeStockRear | M8 | 3125 | 60 | 32 |
| 1915TubeStockFront | M8 | 3125 | 60 | 32 |
| 1915TubeStockRear | M8 | 3125 | 60 | 32 |
| 1923TubeStockFront | M9 | 3472 | 72 | 38 |
| 1923TubeStockRear | M10 | 2604 | 72 | 38 |
| 1938TubeStockFront | M11 | 3595 | 72 | 38 |
| 1938TubeStockNDM | M11 | 3595 | 72 | 38 |
| 1938TubeStockRear | M11 | 3595 | 72 | 38 |
| 1940TubeStockFront | M12 | 5549 | 60 | 32 |
| 1940TubeStockRear | M12 | 5549 | 60 | 32 |
| 1959TubeStockFront | M13 | 3922 | 90 | 48 |
| 1959TubeStockRear | M13 | 3922 | 90 | 48 |
| 1967TubeStockFront | M14 | 4706 | 100 | 53 |
| 1967TubeStockMiddle2 | M14 | 4706 | 100 | 53 |
| 1967TubeStockRear | M14 | 4706 | 100 | 53 |
| 1973TubeStockFrontDM | M15 | 3529 | 100 | 53 |
| 1973TubeStockFrontUNDM | M15 | 3529 | 100 | 53 |
| 1973TubeStockRearDM | M15 | 3529 | 100 | 53 |
| 1973TubeStockRearUNDM | M15 | 3529 | 100 | 53 |
| 1983TubeStockFrontDM | M16 | 4118 | 100 | 53 |
| 1983TubeStockFrontUNDM | M16 | 4118 | 100 | 53 |
| 1983TubeStockRearDM | M16 | 4118 | 100 | 53 |
| 1983TubeStockRearUNDM | M16 | 4118 | 100 | 53 |
| 1992TubeStockFront | M17 | 3125 | 100 | 53 |
| 1992TubeStockMiddle1 | M17 | 3125 | 100 | 53 |
| 1992TubeStockMiddle2 | M17 | 3125 | 100 | 53 |
| 1992TubeStockRear | M17 | 3125 | 100 | 53 |
| 1995TubeStockFrontDM | M18 | 5682 | 100 | 53 |
| 1995TubeStockFrontUNDM | M18 | 5682 | 100 | 53 |
| 1995TubeStockRearDM | M18 | 5682 | 100 | 53 |
| 1995TubeStockRearUNDM | M18 | 5682 | 100 | 53 |
| 2009TubeStockFrontDM | M18 | 5682 | 100 | 53 |
| 2009TubeStockFrontUNDM | M18 | 5682 | 100 | 53 |
| 2009TubeStockMiddle2 | M18 | 5682 | 100 | 53 |
| 2009TubeStockRearDM | M18 | 5682 | 100 | 53 |
| 2009TubeStockRearUNDM | M18 | 5682 | 100 | 53 |
| BR-Class483Front | M19 | 4085 | 72 | 38 |
| BR-Class483NDM | M19 | 4085 | 72 | 38 |
| BR-Class483Rear | M19 | 4085 | 72 | 38 |
| BR-Class485Front | M20 | 3268 | 72 | 38 |
| BR-Class485Rear | M20 | 3268 | 72 | 38 |
| 1900TubeLoco | M21 | 3750 | 50 | 26 |
| District_A_StockFrontDM | M22 | 5833 | 60 | 32 |
| District_A_StockRearDM | M22 | 5833 | 60 | 32 |
| District_BCD_StockFrontDM | M23 | 5731 | 65 | 34 |
| District_BCD_StockRearDM | M23 | 5731 | 65 | 34 |
| District_E_StockFrontDM | M23 | 5731 | 65 | 34 |
| District_E_StockRearDM | M23 | 5731 | 65 | 34 |
| DistrictElectricLoco | M24 | 11462 | 65 | 34 |
| District_F_StockFrontDM | M25 | 7639 | 72 | 38 |
| District_F_StockRearDM | M25 | 7639 | 72 | 38 |
| District_G_StockFrontDM | M26 | 5357 | 70 | 37 |
| District_G_StockRearDM | M26 | 5357 | 70 | 37 |
| District_KLMN_StockFrontDM | M27 | 5642 | 72 | 38 |
| District_KLMN_StockRearDM | M27 | 5642 | 72 | 38 |
| DLR-B07Front | M28 | 2005 | 85 | 45 |
| DLR-B07Rear | M28 | 2005 | 85 | 45 |
| DLR-B92Front | M29 | 1989 | 80 | 42 |
| DLR-B92Rear | M29 | 1989 | 80 | 42 |
| DLR-P86Front | M30 | 1926 | 80 | 42 |
| DLR-P86Rear | M30 | 1926 | 80 | 42 |
| LUL_A_StockFrontDM | M31 | 3583 | 110 | 58 |
| LUL_A_StockRearDM | M31 | 3583 | 110 | 58 |
| LUL_C_StockFrontDM | M32 | 4575 | 90 | 48 |
| LUL_C_StockRearDM | M32 | 4575 | 90 | 48 |
| LUL_D_StockFrontDM | M15 | 3529 | 100 | 53 |
| LUL_D_StockFrontUNDM | M15 | 3529 | 100 | 53 |
| LUL_D_StockRearDM | M15 | 3529 | 100 | 53 |
| LUL_D_StockRearUNDM | M15 | 3529 | 100 | 53 |
| LUL_OP_StockFrontDM | M11 | 3595 | 72 | 38 |
| LUL_OP_StockRearDM | M11 | 3595 | 72 | 38 |
| LUL_R_StockFrontDM | M11 | 3595 | 72 | 38 |
| LUL_R_StockMiddle | M11 | 3595 | 72 | 38 |
| LUL_R_StockRearDM | M11 | 3595 | 72 | 38 |
| LUL_S_Stock(Front) | M33 | 4545 | 100 | 53 |
| LUL_S_Stock(Middle) | M33 | 4545 | 100 | 53 |
| LUL_S_Stock(Rear) | M33 | 4545 | 100 | 53 |
| Metropolitan1905GateFront | M34 | 8462 | 65 | 34 |
| Metropolitan1905GateRear | M34 | 8462 | 65 | 34 |
| Metropolitan1913CircleFront | M35 | 11538 | 65 | 34 |
| Metropolitan1913CircleRear | M35 | 11538 | 65 | 34 |
| Metropolitan1921CircleFront | M36 | 11194 | 67 | 36 |
| Metropolitan1921CircleRear | M36 | 11194 | 67 | 36 |
| MetBTHLoco | M37 | 10000 | 80 | 42 |
| MetCamelbackLoco | M37 | 10000 | 80 | 42 |
| Metropolitan-Motor-Third-Back | M38 | 7692 | 65 | 34 |
| Metropolitan-Motor-Third-Front | M38 | 7692 | 65 | 34 |
| met-mv-stock-front | M39 | 7885 | 65 | 34 |
| met-mv-stock-rear | M39 | 7885 | 65 | 34 |
| Metropolitan-Vickers | M40 | 10595 | 105 | 56 |
| WatfordJointStockFront | M7 | 2500 | 60 | 32 |
| WatfordJointStockRear | M7 | 2500 | 60 | 32 |
| BR-M-Class9000 | M41 | 10458 | 180 | 95 |
| RMU-aerocab(front) | M42 | 3676 | 320 | 170 |
| RMU-aerocab(rear) | M42 | 3676 | 320 | 170 |
| RMUbox(cooled) | M43 | 11765 | 320 | 170 |
| RMUbox(piece) | M43 | 11765 | 320 | 170 |
| RMUflat(cooled) | M44 | 11765 | 160 | 85 |
| RMUflat(piece) | M44 | 11765 | 160 | 85 |
| BR-Ultra-450(Buffet) | M45 | 18605 | 430 | 228 |
| BR-Ultra-450(Open) | M45 | 18605 | 430 | 228 |
| BR-Ultra-450(front) | M45 | 18605 | 430 | 228 |
| BR-Ultra-450(rear) | M45 | 18605 | 430 | 228 |
| BR-Ultra-520(Buffet) | M46 | 22409 | 525 | 278 |
| BR-Ultra-520(Open) | M46 | 22409 | 525 | 278 |
| BR-Ultra-520(front) | M46 | 22409 | 525 | 278 |
| BR-Ultra-520(rear) | M46 | 22409 | 525 | 278 |
| BR-Ultra-520DD(Buffet) | M47 | 22857 | 525 | 278 |
| BR-Ultra-520DD(Open) | M47 | 22857 | 525 | 278 |
| BR-Ultra-520DD(front) | M47 | 22857 | 525 | 278 |
| BR-Ultra-520DD(rear) | M47 | 22857 | 525 | 278 |
| BR-Ultra-Mail(Open) | M48 | 17778 | 450 | 238 |
| BR-Ultra-Mail(front) | M48 | 17778 | 450 | 238 |
| BR-Ultra-Mail(rear) | M48 | 17778 | 450 | 238 |
| Baguely-Drewery-0-6-0 | M49 | 846 | 60 | 32 |
| Funkey-Deisel | M50 | 1206 | 60 | 32 |
| Hibberd-Planet | M51 | 629 | 60 | 32 |
| ac-railbus | M52 | 326 | 92 | 49 |
| BR-101-DMBS | M53 | 541 | 113 | 60 |
| BR-101-DMCL | M53 | 541 | 113 | 60 |
| BR-104Front | M53 | 541 | 113 | 60 |
| BR-104Rear | M53 | 541 | 113 | 60 |
| BR-110-DMBC | M54 | 648 | 113 | 60 |
| BR-110-DMCL | M54 | 648 | 113 | 60 |
| BR-114-DMBS | M53 | 541 | 113 | 60 |
| BR-117-DMBS | M53 | 541 | 113 | 60 |
| BR-117-DMS | M53 | 541 | 113 | 60 |
| BR-120-DMBC | M55 | 561 | 109 | 58 |
| BR-120-DMSL | M55 | 561 | 109 | 58 |
| BR-121 | M56 | 546 | 112 | 59 |
| BR-123-DMBS | M57 | 836 | 112 | 59 |
| BR-123-DMS | M57 | 836 | 112 | 59 |
| BR-127-DMBS-front | M58 | 858 | 113 | 60 |
| BR-127-DMBS-rear | M58 | 858 | 113 | 60 |
| BR-128 | M57 | 836 | 112 | 59 |
| BR-139 | M59 | 236 | 65 | 34 |
| br-141-0-front | M60 | 345 | 121 | 64 |
| br-141-0-rear | M60 | 345 | 121 | 64 |
| br-141-1-front | M61 | 357 | 121 | 64 |
| br-141-1-rear | M61 | 357 | 121 | 64 |
| br-142-1-front | M62 | 360 | 120 | 64 |
| br-142-1-rear | M62 | 360 | 120 | 64 |
| br-142-front | M63 | 321 | 120 | 64 |
| br-142-rear | M63 | 321 | 120 | 64 |
| br-144-0-front | M63 | 321 | 120 | 64 |
| br-144-0-middle | M63 | 321 | 120 | 64 |
| br-144-0-rear | M63 | 321 | 120 | 64 |
| br-144-1-front | M62 | 360 | 120 | 64 |
| br-144-1-middle | M62 | 360 | 120 | 64 |
| br-144-1-rear | M62 | 360 | 120 | 64 |
| br-150-centre | M64 | 478 | 121 | 64 |
| br-150-front | M64 | 478 | 121 | 64 |
| br-150-rear | M64 | 478 | 121 | 64 |
| br-153 | M65 | 444 | 120 | 64 |
| br-153-trolley | M65 | 444 | 120 | 64 |
| br-156-front | M65 | 444 | 120 | 64 |
| br-156-front-trolley | M65 | 444 | 120 | 64 |
| br-156-rear | M65 | 444 | 120 | 64 |
| br-158-centre | M66 | 451 | 145 | 77 |
| br-158-front | M66 | 451 | 145 | 77 |
| br-158-rear | M66 | 451 | 145 | 77 |
| br-159-centre | M67 | 517 | 145 | 77 |
| br-159-front | M67 | 517 | 145 | 77 |
| br-159-rear | M67 | 517 | 145 | 77 |
| BR-165Front | M68 | 545 | 120 | 64 |
| BR-165Middle | M68 | 545 | 120 | 64 |
| BR-165Rear | M68 | 545 | 120 | 64 |
| BR-166Front | M66 | 451 | 145 | 77 |
| BR-166Middle | M66 | 451 | 145 | 77 |
| BR-166Middle-Trolley | M66 | 451 | 145 | 77 |
| BR-166Rear | M66 | 451 | 145 | 77 |
| BR-170Front | M69 | 472 | 160 | 85 |
| BR-170Middle | M69 | 472 | 160 | 85 |
| BR-170Rear | M69 | 472 | 160 | 85 |
| BR-172-0Front | M70 | 719 | 120 | 64 |
| BR-172-0Middle | M70 | 719 | 120 | 64 |
| BR-172-0Rear | M70 | 719 | 120 | 64 |
| BR-172-2Front | M71 | 539 | 160 | 85 |
| BR-172-2Middle | M71 | 539 | 160 | 85 |
| BR-172-2Rear | M71 | 539 | 160 | 85 |
| BR-175Front | M72 | 509 | 160 | 85 |
| BR-175Middle | M72 | 509 | 160 | 85 |
| BR-175Middle-trolley | M72 | 509 | 160 | 85 |
| BR-175Rear | M72 | 509 | 160 | 85 |
| BR-180Front | M73 | 671 | 200 | 106 |
| BR-180Middle | M73 | 671 | 200 | 106 |
| BR-180Middle-Buffet | M73 | 671 | 200 | 106 |
| BR-180Middle-first | M73 | 671 | 200 | 106 |
| BR-180Rear | M73 | 671 | 200 | 106 |
| BR-185Front | M74 | 838 | 160 | 85 |
| BR-185Middle | M74 | 838 | 160 | 85 |
| BR-185Rear | M74 | 838 | 160 | 85 |
| BR-195Front | M75 | 584 | 160 | 85 |
| BR-195Middle | M75 | 584 | 160 | 85 |
| BR-195Rear | M75 | 584 | 160 | 85 |
| BR-196Front | M75 | 584 | 160 | 85 |
| BR-196Front-trolley | M75 | 584 | 160 | 85 |
| BR-196Middle | M75 | 584 | 160 | 85 |
| BR-196Rear | M75 | 584 | 160 | 85 |
| BR-196Rear-first | M75 | 584 | 160 | 85 |
| BR-202-front | M76 | 842 | 120 | 64 |
| BR-202-rear | M76 | 842 | 120 | 64 |
| BR-205Front | M77 | 1707 | 120 | 64 |
| BR-210-DM | M78 | 1601 | 145 | 77 |
| BR-220Front | M73 | 671 | 200 | 106 |
| BR-220Middle | M73 | 671 | 200 | 106 |
| BR-220Middle-shop | M73 | 671 | 200 | 106 |
| BR-220Rear | M73 | 671 | 200 | 106 |
| BR-221Front | M73 | 671 | 200 | 106 |
| BR-221Middle | M73 | 671 | 200 | 106 |
| BR-221Middle-shop | M73 | 671 | 200 | 106 |
| BR-221Rear | M73 | 671 | 200 | 106 |
| BR-222Front | M73 | 671 | 200 | 106 |
| BR-222MidBuffet | M73 | 671 | 200 | 106 |
| BR-222MidComposite | M73 | 671 | 200 | 106 |
| BR-222MidFirst | M73 | 671 | 200 | 106 |
| BR-222MidStandard | M73 | 671 | 200 | 106 |
| BR-222Rear | M73 | 671 | 200 | 106 |
| BR-251FrontFirst | M79 | 1412 | 145 | 77 |
| BR-251FrontSecond | M79 | 1412 | 145 | 77 |
| BR-251RearFirst | M79 | 1412 | 145 | 77 |
| BR-251RearSecond | M79 | 1412 | 145 | 77 |
| BR-302(centre1) | M80 | 6036 | 120 | 64 |
| BR-303Pantograph | M81 | 6603 | 120 | 64 |
| BR-304Centre-Motor | M81 | 6603 | 120 | 64 |
| BR-307(centre1) | M82 | 5823 | 120 | 64 |
| BR-309-1Front | M83 | 6779 | 160 | 85 |
| BR-309Power | M83 | 6779 | 160 | 85 |
| BR-310-MBSO | M84 | 8611 | 120 | 64 |
| BR-312-MBSO | M85 | 7126 | 145 | 77 |
| BR-313Front | M86 | 3504 | 120 | 64 |
| BR-313Rear | M86 | 3504 | 120 | 64 |
| BR-314Front | M86 | 3504 | 120 | 64 |
| BR-314Rear | M86 | 3504 | 120 | 64 |
| BR-315Front | M86 | 3504 | 120 | 64 |
| BR-315Rear | M86 | 3504 | 120 | 64 |
| BR-317-Motor | M87 | 7933 | 160 | 85 |
| BR-318-Motor | M88 | 9478 | 145 | 77 |
| BR-319Engine | M87 | 7933 | 160 | 85 |
| BR-320(pantograph) | M89 | 9728 | 145 | 77 |
| BR-321(pantograph) | M90 | 8590 | 160 | 85 |
| BR-323Front | M91 | 3539 | 145 | 77 |
| BR-323Middle | M91 | 3539 | 145 | 77 |
| BR-323Rear | M91 | 3539 | 145 | 77 |
| BR-325Power | M92 | 8141 | 160 | 85 |
| BR-331Front | M93 | 7237 | 160 | 85 |
| BR-331Motor | M93 | 7237 | 160 | 85 |
| BR-331Rear | M93 | 7237 | 160 | 85 |
| BR-332(front) | M94 | 5757 | 160 | 85 |
| BR-332(rear) | M94 | 5757 | 160 | 85 |
| BR-333(front) | M94 | 5757 | 160 | 85 |
| BR-333(rear) | M94 | 5757 | 160 | 85 |
| BR-334Front | M95 | 3630 | 145 | 77 |
| BR-334Middle | M95 | 3630 | 145 | 77 |
| BR-334Rear | M95 | 3630 | 145 | 77 |
| BR-345Front | M96 | 3993 | 145 | 77 |
| BR-345MS3Front | M96 | 3993 | 145 | 77 |
| BR-345MS3Rear | M96 | 3993 | 145 | 77 |
| BR-345Middle | M97 | 7985 | 145 | 77 |
| BR-345MiddleRear | M97 | 7985 | 145 | 77 |
| BR-345Panto | M96 | 3993 | 145 | 77 |
| BR-345PantoRear | M96 | 3993 | 145 | 77 |
| BR-345Rear | M96 | 3993 | 145 | 77 |
| BR-350-1(front) | M98 | 5575 | 177 | 94 |
| BR-350-1(rear) | M98 | 5575 | 177 | 94 |
| BR-350-2(front) | M99 | 6168 | 160 | 85 |
| BR-350-2(rear) | M99 | 6168 | 160 | 85 |
| c2c-357(centre2) | M100 | 3551 | 160 | 85 |
| c2c-357(centre3) | M100 | 3551 | 160 | 85 |
| c2c-357(front) | M100 | 3551 | 160 | 85 |
| c2c-357(rear) | M100 | 3551 | 160 | 85 |
| BR-360(front) | M101 | 6373 | 160 | 85 |
| BR-360(rear) | M101 | 6373 | 160 | 85 |
| BR-365Front | M102 | 5164 | 160 | 85 |
| BR-365Rear | M102 | 5164 | 160 | 85 |
| BR-370FrontPower | M103 | 15297 | 250 | 132 |
| BR-370RearPower | M103 | 15297 | 250 | 132 |
| BR-373FrontCab | M104 | 26754 | 300 | 159 |
| BR-373RearCab | M104 | 26754 | 300 | 159 |
| BR-374(buffet) | M105 | 13158 | 320 | 170 |
| BR-374(first) | M105 | 13158 | 320 | 170 |
| BR-374(front) | M105 | 13158 | 320 | 170 |
| BR-374(power) | M105 | 13158 | 320 | 170 |
| BR-374(rear) | M105 | 13158 | 320 | 170 |
| BR-375-6Front | M100 | 3551 | 160 | 85 |
| BR-375-6Middle | M100 | 3551 | 160 | 85 |
| BR-375-6Rear | M100 | 3551 | 160 | 85 |
| BR-377-7Middle2 | M100 | 3551 | 160 | 85 |
| BR-375Front | M100 | 3551 | 160 | 85 |
| BR-375Middle | M100 | 3551 | 160 | 85 |
| BR-375Middle2 | M100 | 3551 | 160 | 85 |
| BR-375Rear | M100 | 3551 | 160 | 85 |
| BR-376Front | M106 | 4735 | 120 | 64 |
| BR-376MiddlePower | M106 | 4735 | 120 | 64 |
| BR-376MiddlePower2 | M106 | 4735 | 120 | 64 |
| BR-376Rear | M106 | 4735 | 120 | 64 |
| BR-378Front | M107 | 5682 | 120 | 64 |
| BR-378Middle | M107 | 5682 | 120 | 64 |
| BR-378Middle2 | M107 | 5682 | 120 | 64 |
| BR-378Rear | M107 | 5682 | 120 | 64 |
| BR-379Front | M108 | 4934 | 160 | 85 |
| BR-379Middle | M108 | 4934 | 160 | 85 |
| BR-379Middle2 | M108 | 4934 | 160 | 85 |
| BR-379Rear | M108 | 4934 | 160 | 85 |
| BR-380(front) | M109 | 5327 | 160 | 85 |
| BR-380(rear) | M109 | 5327 | 160 | 85 |
| BR-385(front) | M99 | 6168 | 160 | 85 |
| BR-385(rear) | M99 | 6168 | 160 | 85 |
| BR-387Front | M110 | 4460 | 177 | 94 |
| BR-387Middle | M110 | 4460 | 177 | 94 |
| BR-387Middle2 | M110 | 4460 | 177 | 94 |
| BR-387Rear | M110 | 4460 | 177 | 94 |
| BR-390FrontCab | M111 | 5000 | 225 | 119 |
| BR-390FrontCoach | M111 | 5000 | 225 | 119 |
| BR-390PoweredCoach | M111 | 5000 | 225 | 119 |
| BR-390PoweredCoachFirst | M111 | 5000 | 225 | 119 |
| BR-390RearCab | M111 | 5000 | 225 | 119 |
| BR-390RearCoach | M111 | 5000 | 225 | 119 |
| BR-395Middle | M112 | 4912 | 225 | 119 |
| BR-397Front | M113 | 5789 | 200 | 106 |
| BR-397Middle | M113 | 5789 | 200 | 106 |
| BR-397Rear | M113 | 5789 | 200 | 106 |
| BR-410[CEP]Front | M114 | 3043 | 145 | 77 |
| BR-410[CEP]Rear | M114 | 3043 | 145 | 77 |
| BR-414[HAP]Front | M115 | 3109 | 140 | 74 |
| BR-4EPB(front) | M116 | 3657 | 120 | 64 |
| BR-4EPB(rear) | M116 | 3657 | 120 | 64 |
| BR-419[MLV] | M117 | 3026 | 145 | 77 |
| BR-421[CIG]Motor | M118 | 6085 | 145 | 77 |
| BR-423-MBSO | M119 | 6303 | 140 | 74 |
| BR-430[REP]Front | M120 | 9736 | 145 | 77 |
| BR-430[REP]Rear | M120 | 9736 | 145 | 77 |
| BR-442-Middle2 | M121 | 8824 | 160 | 85 |
| BR-444(front) | M109 | 5327 | 160 | 85 |
| BR-444(rear) | M109 | 5327 | 160 | 85 |
| BR-450(front) | M109 | 5327 | 160 | 85 |
| BR-450(rear) | M109 | 5327 | 160 | 85 |
| BR-455-Motor | M122 | 7253 | 121 | 64 |
| BR-456-DMSO | M123 | 3503 | 121 | 64 |
| BR-458(centre2) | M109 | 5327 | 160 | 85 |
| BR-458(front) | M109 | 5327 | 160 | 85 |
| BR-458(rear) | M109 | 5327 | 160 | 85 |
| BR-460-DMLFO | M109 | 5327 | 160 | 85 |
| BR-460-DMSO | M109 | 5327 | 160 | 85 |
| BR-460-MSO | M109 | 5327 | 160 | 85 |
| BR-465Front | M107 | 5682 | 120 | 64 |
| BR-465Rear | M107 | 5682 | 120 | 64 |
| BR-489[GLV] | M124 | 3002 | 145 | 77 |
| BR-501(DMB) | M125 | 7255 | 120 | 64 |
| BR-506Front | M126 | 5412 | 120 | 64 |
| BR-507(front) | M127 | 3216 | 120 | 64 |
| BR-507(rear) | M127 | 3216 | 120 | 64 |
| BR-700Front | M128 | 6990 | 160 | 85 |
| BR-700MiddlePower | M128 | 6990 | 160 | 85 |
| BR-700Rear | M128 | 6990 | 160 | 85 |
| BR-701Front | M100 | 3551 | 160 | 85 |
| BR-701Middle | M100 | 3551 | 160 | 85 |
| BR-701Panto | M100 | 3551 | 160 | 85 |
| BR-701PantoRear | M100 | 3551 | 160 | 85 |
| BR-701Rear | M100 | 3551 | 160 | 85 |
| BR-707Front | M129 | 6037 | 160 | 85 |
| BR-707MiddlePower | M129 | 6037 | 160 | 85 |
| BR-707Rear | M129 | 6037 | 160 | 85 |
| BR-710Front | M130 | 4261 | 120 | 64 |
| BR-710Middle | M130 | 4261 | 120 | 64 |
| BR-710Panto | M130 | 4261 | 120 | 64 |
| BR-710Rear | M130 | 4261 | 120 | 64 |
| BR-717Front | M131 | 3318 | 137 | 73 |
| BR-717MiddlePower | M131 | 3318 | 137 | 73 |
| BR-717Rear | M131 | 3318 | 137 | 73 |
| BR-720Middle | M132 | 4729 | 160 | 85 |
| BR-720Panto | M132 | 4729 | 160 | 85 |
| BR-720Rear | M132 | 4729 | 160 | 85 |
| BR-730-0Front | M133 | 4537 | 145 | 77 |
| BR-730-0Panto | M133 | 4537 | 145 | 77 |
| BR-730-0Rear | M133 | 4537 | 145 | 77 |
| BR-730-2Front | M134 | 3717 | 177 | 94 |
| BR-730-2MiddleFront | M134 | 3717 | 177 | 94 |
| BR-730-2MiddleRear | M134 | 3717 | 177 | 94 |
| BR-730-2Panto | M134 | 3717 | 177 | 94 |
| BR-730-2Rear | M134 | 3717 | 177 | 94 |
| BR-769Motor | M135 | 1288 | 145 | 77 |
| BR-800Composite18+58 | M136 | 838 | 200 | 106 |
| BR-800FrontMS | M136 | 838 | 200 | 106 |
| BR-800MiddleComposite | M136 | 838 | 200 | 106 |
| BR-800MiddleFirst | M136 | 838 | 200 | 106 |
| BR-800MiddlePower | M136 | 838 | 200 | 106 |
| BR-800RearMS | M136 | 838 | 200 | 106 |
| BR-801Composite18+58 | M137 | 5287 | 225 | 119 |
| BR-801FrontMS | M137 | 5287 | 225 | 119 |
| BR-801MiddleComposite | M137 | 5287 | 225 | 119 |
| BR-801MiddleFirst | M137 | 5287 | 225 | 119 |
| BR-801MiddlePower | M137 | 5287 | 225 | 119 |
| BR-801RearMS | M137 | 5287 | 225 | 119 |
| BR-Class09 | M138 | 1849 | 44 | 23 |
| BR-Class15 | M139 | 1681 | 97 | 51 |
| BR-Class16 | M139 | 1681 | 97 | 51 |
| BR-Class17 | M140 | 1889 | 97 | 51 |
| BR-Class20 | M141 | 1697 | 120 | 64 |
| BR-Class21 | M142 | 1866 | 120 | 64 |
| BR-Class24 | M143 | 1952 | 121 | 64 |
| BR-Class25 | M144 | 1755 | 145 | 77 |
| BR-Class26 | M145 | 1817 | 130 | 69 |
| BR-Class27 | M144 | 1755 | 145 | 77 |
| BR-Class28 | M146 | 2037 | 120 | 64 |
| BR-Class28-2 | M147 | 2799 | 120 | 64 |
| BR-Class29 | M148 | 2121 | 130 | 69 |
| BR-Class30 | M149 | 1953 | 130 | 69 |
| BR-Class31-1 | M150 | 2066 | 145 | 77 |
| BR-Class33 | M151 | 2255 | 140 | 74 |
| BR-Class35 | M152 | 2457 | 145 | 77 |
| BR-Class37 | M153 | 2456 | 145 | 77 |
| BR-Class40 | M154 | 2806 | 145 | 77 |
| BR-Class41 | M155 | 2810 | 145 | 77 |
| BR-Class42 | M156 | 3186 | 145 | 77 |
| BR-Class43 | M1 | 2160 | 200 | 106 |
| BR-Class43Rear | M1 | 2160 | 200 | 106 |
| BR-Class45 | M157 | 3510 | 145 | 77 |
| BR-Class47 | M158 | 3430 | 153 | 81 |
| BR-Class50 | M159 | 3430 | 160 | 85 |
| BR-Class52 | M160 | 3950 | 140 | 74 |
| BR-Class55 | M161 | 4198 | 160 | 85 |
| BR-Class56 | M162 | 4793 | 130 | 69 |
| BR-Class57 | M163 | 3209 | 153 | 81 |
| BR-Class58 | M164 | 4872 | 130 | 69 |
| BR-Class60 | M165 | 5537 | 97 | 51 |
| BR-Class62 | M166 | 4106 | 175 | 93 |
| BR-Class66 | M167 | 4879 | 120 | 64 |
| BR-Class67 | M168 | 2635 | 200 | 106 |
| BR-Class68 | M169 | 4087 | 160 | 85 |
| BR-Class70 | M170 | 5352 | 120 | 64 |
| BR-Class71 | M171 | 13955 | 145 | 77 |
| BR-Class73 | M172 | 8592 | 145 | 77 |
| BR-Class81 | M173 | 19151 | 160 | 85 |
| BR-Class83 | M174 | 17949 | 160 | 85 |
| BR-Class85 | M175 | 19231 | 160 | 85 |
| BR-Class86 | M176 | 24119 | 160 | 85 |
| BR-Class87 | M177 | 27017 | 177 | 94 |
| BR-Class88 | M178 | 24507 | 160 | 85 |
| BR-Class89 | M179 | 27474 | 200 | 106 |
| BR-Class90 | M177 | 27017 | 177 | 94 |
| BR-Class91 | M3 | 26781 | 225 | 119 |
| BR-Class92 | M180 | 47368 | 140 | 74 |
| BR-Derby-Lightweight-DMBS | M181 | 630 | 100 | 53 |
| BR-Derby-Lightweight-DMBS-single | M181 | 630 | 100 | 53 |
| BR-Derby-Lightweight-DMCL | M181 | 630 | 100 | 53 |
| BR-Derby-Lightweight-DMS | M181 | 630 | 100 | 53 |
| GWR-Gloucester-Parcel-Railcar | M182 | 422 | 130 | 69 |
| GWR-Gloucester-Railcar | M182 | 422 | 130 | 69 |
| GWR-ParkRoyal-Railcar | M183 | 549 | 100 | 53 |
| gwr-swindon-railcar-parcels | M184 | 387 | 112 | 59 |
| gwr-swindon-railcar | M184 | 387 | 112 | 59 |
| GWR-Swindon-TwinsetFront | M184 | 387 | 112 | 59 |
| GWR-Swindon-TwinsetRear | M184 | 387 | 112 | 59 |
| leyland-railbus | M185 | 222 | 90 | 48 |
| LMS-10000 | M186 | 2251 | 150 | 80 |
| BR-Class10800 | M187 | 1532 | 110 | 58 |
| LMS-502Front | M188 | 7405 | 112 | 59 |
| LMS-EMU-driving-motor | M189 | 9231 | 110 | 58 |
| LNER-ClassEM1 | M190 | 15686 | 105 | 56 |
| LNER-ClassEM2 | M191 | 16157 | 150 | 80 |
| LNER-1937-Tyneside-EMU-MPV | M192 | 8366 | 90 | 48 |
| LNER-1937-Tyneside-EMU-front | M193 | 4183 | 90 | 48 |
| LOR-EMU(front) | M194 | 1083 | 60 | 32 |
| LSWR-EMU(front) | M195 | 5180 | 97 | 51 |
| LSWR-EMU(rear) | M195 | 5180 | 97 | 51 |
| L&YR-EMU-driving-motor | M196 | 7753 | 89 | 47 |
| Mersey-EMU-1923(front) | M197 | 3321 | 70 | 37 |
| Mersey-EMU-1923(rear) | M197 | 3321 | 70 | 37 |
| Mersey-EMU(front) | M198 | 3125 | 70 | 37 |
| Mersey-EMU(rear) | M198 | 3125 | 70 | 37 |
| MSJ&A-EMU-driving-motor | M199 | 11862 | 97 | 51 |
| NER-ClassEE1 | M200 | 15976 | 105 | 56 |
| NER-ClassEF1 | M201 | 12059 | 85 | 45 |
| NER-ClassES1 | M202 | 8000 | 75 | 40 |
| ner-tyne-petrol-electric-railcar | M203 | 375 | 70 | 37 |
| NER-Tyneside-mpv | M204 | 3571 | 70 | 37 |
| NER-Tyneside-unit(front) | M204 | 3571 | 70 | 37 |
| NER-Tyneside-unit(rear motor) | M204 | 3571 | 70 | 37 |
| SR-1-Co-Co-1 | M205 | 2558 | 140 | 74 |
| SR-2-NOL-front | M206 | 4973 | 97 | 51 |
| sr-2hal-front | M207 | 4020 | 120 | 64 |
| SR-3SUB(front) | M208 | 5284 | 97 | 51 |
| SR-3SUB(rear) | M208 | 5284 | 97 | 51 |
| SR-4LAV(front) | M207 | 4020 | 120 | 64 |
| SR-4LAV(rear) | M207 | 4020 | 120 | 64 |
| SR-401[BIL]Front | M207 | 4020 | 120 | 64 |
| SR-404[COR]Front | M209 | 3267 | 121 | 64 |
| SR-404[COR]Rear | M209 | 3267 | 121 | 64 |
| SR-5-BEL-driving-motor-front | M210 | 6578 | 120 | 64 |
| SR-5-BEL-driving-motor-rear | M210 | 6578 | 120 | 64 |
| SR-6PAN(front) | M210 | 6578 | 120 | 64 |
| SR-6PAN(rear) | M210 | 6578 | 120 | 64 |
| SR-4SUB(front) | M211 | 4039 | 120 | 64 |
| SR-4SUB(rear) | M211 | 4039 | 120 | 64 |
| SR-4DD-front | M116 | 3657 | 120 | 64 |
| SR-4DD-rear | M116 | 3657 | 120 | 64 |
| SR-CC | M212 | 10784 | 120 | 64 |
| TyneWearMetroClass994Front | M213 | 3235 | 80 | 42 |
| TyneWearMetroClass994Rear | M213 | 3235 | 80 | 42 |
| 1-Deck-Closed | M214 | 1445 | 32 | 17 |
| 2-Deck-Open | M214 | 1445 | 32 | 17 |
| Blackpool-Balloon | M215 | 1538 | 65 | 34 |
| Blackpool-Brush | M215 | 1538 | 65 | 34 |
| Blackpool-Centenary | M216 | 1429 | 70 | 37 |
| Blackpool-Coronation | M217 | 2252 | 70 | 37 |
| Blackpool-Dreadnought | M218 | 1172 | 32 | 17 |
| Blackpool-EE-Railcoach | M215 | 1538 | 65 | 34 |
| Blackpool-Jubilee | M216 | 1429 | 70 | 37 |
| Blackpool-Millenium | M219 | 1380 | 70 | 37 |
| Blackpool-Original | M220 | 917 | 30 | 16 |
| Blackpool-ProgressTwin-Power | M216 | 1429 | 70 | 37 |
| Blackpool-Standard | M221 | 2344 | 32 | 17 |
| Bombardier-Flexity-2-front | M222 | 3896 | 70 | 37 |
| Bombardier-Flexity-2-rear | M222 | 3896 | 70 | 37 |
| Flexity-SwiftFront | M223 | 3409 | 80 | 42 |
| Flexity-SwiftRear | M223 | 3409 | 80 | 42 |
| CAF-Edinburgh-front | M224 | 5195 | 70 | 37 |
| CAF-Edinburgh-motor | M224 | 5195 | 70 | 37 |
| CAF-Edinburgh-rear | M224 | 5195 | 70 | 37 |
| CAF-Urbos-3-front | M224 | 5195 | 70 | 37 |
| CAF-Urbos-3-rear | M224 | 5195 | 70 | 37 |
| Croydon-Variobahn-front | M225 | 2557 | 80 | 42 |
| Croydon-Variobahn-rear | M225 | 2557 | 80 | 42 |
| feltham | M226 | 1882 | 65 | 34 |
| glasgow-coronation | M227 | 1826 | 67 | 36 |
| glasgow-cunarder | M228 | 1879 | 67 | 36 |
| glasgow-room-and-kitchen | M229 | 2031 | 32 | 17 |
| glasgow-standard-1 | M230 | 1758 | 32 | 17 |
| glasgow-standard-3 | M221 | 2344 | 32 | 17 |
| glasgow-standard-4 | M231 | 3477 | 32 | 17 |
| lcc-a-class | M230 | 1758 | 32 | 17 |
| lcc-c-class | M230 | 1758 | 32 | 17 |
| lcc-e-class | M230 | 1758 | 32 | 17 |
| lcc-e1-class | M232 | 2461 | 32 | 17 |
| lcc-e3-class | M233 | 2094 | 50 | 26 |
| lcc-g-class | M230 | 1758 | 32 | 17 |
| lcc-hr2-class | M234 | 2447 | 50 | 26 |
| lcc-m-class | M232 | 2461 | 32 | 17 |
| lut-type-t | M230 | 1758 | 32 | 17 |
| lut-type-z | M214 | 1445 | 32 | 17 |
| Metrolink-T68A(Rear) | M223 | 3409 | 80 | 42 |
| Metrolink-T86(Rear) | M235 | 2983 | 80 | 42 |
| Metrolink-T68A(Front) | M223 | 3409 | 80 | 42 |
| Metrolink-T86(Front) | M235 | 2983 | 80 | 42 |
| MidlandMetroT69Front | M236 | 3409 | 70 | 37 |
| MidlandMetroT69Rear | M236 | 3409 | 70 | 37 |
| bombardier-incentro-front | M225 | 2557 | 80 | 42 |
| bombardier-incentro-rear | M225 | 2557 | 80 | 42 |
| sheffield-preston | M229 | 2031 | 32 | 17 |
| Sheffield-Roberts | M237 | 1756 | 65 | 34 |
| sheffield-rocker-panel | M221 | 2344 | 32 | 17 |
| sheffield-standard | M238 | 2930 | 32 | 17 |
| Sheffield-Supertram(Front) | M239 | 3935 | 80 | 42 |
| Sheffield-Supertram(Middle) | M240 | 7869 | 80 | 42 |
| Sheffield-Supertram(Rear) | M239 | 3935 | 80 | 42 |
| Sheffield-VosslohTramtrain(Front) | M241 | 3295 | 100 | 53 |
| Sheffield-VosslohTramtrain(Middle) | M241 | 3295 | 100 | 53 |
| Sheffield-VosslohTramtrain(Rear) | M241 | 3295 | 100 | 53 |
| Toastrack | M242 | 898 | 32 | 17 |

---

## 4. Gaps and doubts

### 4.1 The full-output bias, which is the largest single uncertainty

`calc_fuel_consumption` charges the full-output figure whenever a vehicle is at its maximum physical
speed, and a train spends most of its distance at line speed. A railway vehicle therefore never uses
its rated output at the speed the model charges it at. The consequence is visible in 1.7: diesel
figures match measured fleet consumption within about 30%, but electric figures sit 30-80% above
the measured average because installed electric power is only used during acceleration.

If the orchestrator wants the *measured average* instead of the full-output figure, the conversion
is a single multiplier, derived from the rows of 1.7 (measured divided by computed): **electric
0.60, diesel 0.85**. I have not applied it, because the brief defines `fuel_per_km` as the
full-output figure and the steam precedent is built that way. But it should be a conscious choice:
as delivered, a Class 390 will be charged about 30 kWh/km where its measured average is 16.7.

### 4.2 Trailer cars carry no auxiliary load

The 291 motorless unit cars are charged 0. In reality a trailer car's lighting, heating and air
conditioning are fed from the motor car's auxiliary winding, about 60 kW for a whole modern unit
(RSSB T618, Class 458), i.e. 10-20 kW per car and 100-200 Wh/car-km at line speed. That is 3-6% of
the unit total at full output, so leaving it out is a small understatement. The alternative
treatment — computing a unit total and dividing it equally across every car, so that each car
carries the published kWh/vehicle-km — was rejected because it would put a non-zero `fuel_per_km`
on a vehicle with no engine and would double-count when a unit is formed from cars of two classes.

### 4.3 Hydrogen maglev is currently free

`fuel[hydrogene]` is commented out in `New/config/fuel.tab`, and `engine_type=hydrogene` is not
routed through the battery/fuel-cell efficiency fallback (that branch tests only `battery` and
`fuel_cell`). `get_fuel_cost()` therefore returns 0 and all 22 maglev objects will burn free
energy whatever figure is stored. The figures in section 2 are tank energy (linear motor 0.85, fuel
cell 0.50), so they are correct if a hydrogen series is added; if one is not, `fuel_per_km` has no
effect on cost for those objects. The maglev classes themselves (`RMU*`, `BR-Ultra-*`,
`BR-M-Class9000`) are fictional, so their power ratings cannot be checked against anything.

### 4.4 Power figures that are known to be wrong but were left alone

Corrected: see 1.9. Not corrected, because changing them would change acceleration and that is
outside this brief:

- **Class 357**: 4 x 500 kW in the pakset, 1,500 kW published. The computed 14,205 Wh/km for the
  unit is 50% above the measured 9,440.
- **London Underground 1995 and 2009 stocks**: 500 kW per car. I could not verify these against a
  published rating; if they are 350 kW the figures are 30% high.
- **Class 800**: 700 kW on six cars, i.e. 4.2 MW of diesel for a 5-car unit, which is more than the
  prototype's three 700 kW generator units.
- **Sheffield Supertram**: 277 + 554 + 277 kW. The middle car at 554 kW is twice the end cars, which
  looks like a data artifact rather than a real asymmetric formation; the unit total of 1,108 kW is
  high for a 1994 tram and gives 15,700 Wh/km against a measured 4,500.
- **Class 139**: the pakset's 64 kW may be the traction motor rather than the prime mover of this
  flywheel railcar; 236 ml/km would then be an understatement. I did not find a rating to check it.

The general rule I applied was to keep the pakset `power` wherever I had no published rating,
because fuel and acceleration should stay consistent with each other.

### 4.5 Diesel locomotives have no measured per-class consumption

The brief expected BR locomotive fuel records in the railway press. I did not find a published
gallons-per-mile figure for any individual diesel class. The diesel figures therefore rest on
engine BSFC (two contemporary sources, 1.2) rather than on measured locomotive consumption, and are
validated only at unit level for DMUs and the HST (1.7). The Class 47 result, 3,430 ml/km at
153 km/h, is 5.5 litres per mile and therefore 0.8 miles per gallon with the engine at full power,
which is the right order for a 2,580 hp locomotive but is not itself a measured figure.

### 4.6 Electric efficiency before 1990 is an estimate

The only published line-to-rail figure found is the Class 390's 0.76. Everything else in the `eta`
table is an engineering estimate, and the AC/DC split is by class list rather than from the data. A
misclassified class is worth 9%. Pre-1930 DC stock (0.80) is the weakest of these: series resistance
control at rated speed, motor and gear losses are all uncertain by several points.

No measured energy figure was found for any pre-1990 electric train, so the whole vintage electric
and tram fleet is derived rather than validated. The one independent check, a 1920s trolleybus at
1.25 units per car-mile (0.78 kWh/km, [topic 6521.245](https://forum.simutrans.com/index.php?topic=6521.245)),
is consistent with the full-output method once the 0.55-0.65 average-to-full-power ratio found in
1.7 is allowed for.

### 4.7 The calibration speed is not the speed of rated output

For a locomotive, rated output is developed at its continuous rated speed, not at its maximum speed:
a Class 90 develops 3,730 kW continuously at about 108 km/h, not at 177 km/h. The sector instruction
is to use the maximum speed, and that keeps `base * cal` equal to the fuel per hour at rated output,
which is the physical quantity. But the part-load curve is then anchored at a speed where the
vehicle cannot in fact be at full power. If the orchestrator prefers the physically consistent
anchor, `calibration_speed` should be the continuous rated speed (roughly 60-70% of maximum for
main-line locomotives and EMUs) and `fuel_per_km` should rise in proportion so that the product is
unchanged; that changes the part-load behaviour but not the full-power fuel rate.

### 4.8 Other smaller points

- **`livery-trains/`** is not in the Makefile and is not compiled into the pak. Its 116 objects in 34
  files are nevertheless in the checklist and are covered here, with the power corrected to the compiled
  class (1.9).
- **`range`** is unset on every object in this sector and is left blank. A Class 158's published
  1,600-mile range and a Class 47's 850-gallon tank both imply the pakset could carry a `range`, but
  that is a separate decision.
- **Battery and fuel-cell rail vehicles**: none exist in this sector, so the round-trip efficiency
  path in `vehicle_desc_t` is not exercised by rail.
- **Auxiliary loads** are not separately charged on any vehicle. For a modern EMU the auxiliaries
  are about 6% of the full-output figure; for a locomotive on hotel load they can be much more.
- **The 0.53 cut-off ratio** is copied from the one steam precedent. Nothing in the sector supports
  a different value, and it only affects part-load running below half of top speed.
- **Tram `runningcost` values** for the pre-1930 fleet look too low relative to any plausible
  traction energy cost (1.8). The discrepancy is in the running cost, not in the fuel figure.
