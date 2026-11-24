# Fuel consumption of road vehicles (pak128.Britain-Ex)

Sector: `waytype=road` in `New/bus/` plus the unpowered road hold `mail-boot`.
Covers **704 objects**: 246 diesel, 172 petrol, 106 steam, 94 with no engine (trailers, horse-drawn vehicles and rear half-units), 64 electric, 21 bio and 1 battery.

Units: **mL/km** petrol, diesel and bio; **g/km** coal for steam road vehicles; **Wh/km** for trolleybuses and the one battery bus. `fuel_per_km` is an integer.

## 1. Method

### 1.1 What the engine does with the number

`vehicle_t::calc_fuel_consumption()` multiplies `fuel_per_km` by `calibration_speed` and divides by the speed actually run, then scales by load. So the product `fuel_per_km x calibration_speed` is the fuel burned per hour at maximum output. The pakset convention, given in the brief, is that `calibration_speed` is the speed at which the vehicle develops its rated output, and for a road vehicle that is its maximum speed: `calibration_speed` is therefore taken directly from each object's `speed` field. `cut_off_speed` is set to half the calibration speed, following the one filled-in precedent (`GNR-Stirling8Foot`: 75 and 40).

### 1.2 Conversions used throughout

All fuel-economy figures for road vehicles are quoted per distance, so only one conversion is needed. For UK gallons (4.54609 L) and statute miles (1.609344 km):

```
mL/km = 4546.09 / (mpg x 1.609344) = 2824.81 / mpg
```

So 8 mpg = 2824.81 / 8 = **353 mL/km**; 9.75 mpg = 290; 11 mpg = 257; 15.5 mpg = 182; 30 mpg = 94. Litres per 100 km convert by x10 (47.2 L/100 km = 472 mL/km).

Coal, from pounds per mile:

```
g/km = lb/mile x 453.592 / 1.609344 = lb/mile x 281.85
```

So 5.21 lb/mile = 1468 g/km; 8.66 lb/mile = 2441 g/km; 2.94 lb/mile = 829 g/km.

Electricity, from kWh per car-mile: 1 kWh/mile = 1000 / 1.609344 = **621.4 Wh/km**, so 1.65 units/car-mile = 1025 Wh/km and 2.75 units/car-mile = 1709 Wh/km.

### 1.3 Evidence base

The Simutrans forum thread *A snippet of relative pricing information* supplied the core bus and steam-wagon figures (posts linked as S1-S8 below). The rest comes from *The Commercial Motor* archive (contemporary road tests, 1907-1968) and from DfT/Zemo/TRL bus and HGV statistics. Every row in the model table carries the source key that applies; the keys are listed here with full URLs.

| key | source and what it measures |
|---|---|
| S1 | Simutrans forum, Heritage Commercials: Sentinel steam bus, 110 lb coal per 10 miles (40 mph capability) — https://forum.simutrans.com/index.php?msg=157715 |
| S2 | Simutrans forum, Czech Sentinel page: 4 kg coal/km maximum, 3.2 kg/km on a 62 km laden run — https://forum.simutrans.com/index.php?msg=157721 |
| S3 | Simutrans forum quoting Nick Baldwin, 'An Illustrated History of Dennis Buses and Trucks': 2-ton lorry/GL 15-16 mpg laden; Lancet 11 mpg; Lancet II 17 mpg — https://forum.simutrans.com/index.php?msg=159560 |
| S4 | Simutrans forum: Guy CX 6-wheeler c.1926, 4 mpg in service (recollection, flagged as such) — https://forum.simutrans.com/index.php?msg=160790 |
| S5 | Simutrans forum, London Bus Museum curator: Routemaster-era 8-10 mpg, modern buses 6-7 mpg, old petrol buses 4 mpg — https://forum.simutrans.com/index.php?msg=161438 |
| S6 | Simutrans forum, 'Ian Allan Transport Library - Daimler': COG5 32-seat single-decker 11.79-12.55 mpg on local services — https://forum.simutrans.com/index.php?msg=166768 |
| S7 | Simutrans forum quoting Wikipedia: Leyland Titan PD2/20 advertised at 9.75 mpg in daily service, late 1950s — https://forum.simutrans.com/index.php?msg=198196 |
| S8 | Simutrans forum quoting a 1930s source: 1.25 units (kWh) per trolleybus car-mile — https://forum.simutrans.com/index.php?msg=202630 |
| S9 | The Commercial Motor, 11 April 1907, IMechE discussion: best double-deck petrol omnibus record 'something like six miles per gallon' — https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses |
| S10 | The Commercial Motor, 23 February 1926: Dover 18-seater charabanc, 1,266 miles on 147 gallons = 8.6 mpg — https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry |
| S11 | The Commercial Motor, 3 November 1925: Morris 1-ton truck 19.48 mpg laden, 12 cwt van 21.19 mpg, RAC-observed — https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials |
| S12 | The Commercial Motor, 16 October 1923: Saurer 6.5-tonner, 9.84 mpg at 10.6 t gross, RAC trial — https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon |
| S13 | The Commercial Motor, 24 February 1931: oil-engined bus over 13 mpg at 10.5 t laden — https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses |
| S14 | The Commercial Motor, 16 February 1911: five Foden wagons in 1910 service, 7.90-9.35 lb coal/mile at 8-9 ton loads — https://archive.commercialmotor.com/article/16th-february-1911/27/concerning-steam-wagons-generally |
| S15 | The Commercial Motor, 16 March 1926: Fodens, 1 cwt of coal for 25 miles with 6 tons at 15-20 mph by 1922 (9-10 miles per cwt in 1901) — https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career |
| S16 | The Commercial Motor, 20 November 1923: Super-Sentinel, 5.91 lb coal/mile, 8.2 ton load, 13.3 mph average — https://archive.commercialmotor.com/article/20th-november-1923/26/trying-out-an-undertype-steam-wagon |
| S17 | The Commercial Motor, 20 December 1927: Sentinel DG6, 8.66 lb coal/mile, 12 ton load, 17.05 mph average — https://archive.commercialmotor.com/article/20th-december-1927/51/the-cm-tests-a-nem--wheeled-steam-wagon |
| S18 | The Commercial Motor, 4 February 1930: Sentinel DG6, 218 lb coal in 41.8 miles = 5.21 lb/mile, 12 ton load — https://archive.commercialmotor.com/article/4th-february-1930/50/the-road-performance-o-a-popular-six-wheeled-steam |
| S19 | The Commercial Motor, 9 September 1930: Sentinel DG8, average 14 miles per cwt of coal fully laden — https://archive.commercialmotor.com/article/9th-september-1930/63/sentinels-new-steamer |
| S20 | The Commercial Motor, 16 June 1933: Sentinel S4, 173 lb coal in 58.8 miles = 2.94 lb/mile — https://archive.commercialmotor.com/article/16th-june-1933/45/road-test-no-149 |
| S21 | The Commercial Motor, 20 December 1968: 1933 Sentinel S4 still using 1 cwt of Welsh coal per 30 miles fully laden — https://archive.commercialmotor.com/article/20th-december-1968/36/commercial-motor-christmas-road-test |
| S22 | The Commercial Motor, 16 February 1934: Sentinel S6 six-wheeler, 19 tons laden, coal measured over 60 miles — https://archive.commercialmotor.com/article/16th-february-1934/42/a-modern-steamei |
| S23 | Nature, 9 December 1939, abstract of Sinclair (IEE): trolleybuses on intensive service average 2.75 units per car-mile at the substation — https://doi.org/10.1038/144989a0 |
| S24 | Ministry of Transport, Tramways and Light Railways returns 1930-31: trackless trolley undertakings used 1.65-1.69 traction units per car-mile — https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf |
| S25 | Zemo Partnership, Economics of Bus Drivelines: typical diesel bus 50 L/100 km; city electric bus about 0.8 kWh/km — https://www.zemo.org.uk/assets/workingdocuments/BWG-P-05-21%20Bus%20Driveline%20Economics.pdf |
| S26 | Zemo/EY Scottish bus electrification report: UK averages 9.1 mpg single-decker, 7.8 mpg double-decker — https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf |
| S27 | LowCVP/Ricardo bus roadmap 2013: urban duty cycle 8 mpg single-deck, 6 mpg double-deck — https://www.zemo.org.uk/assets/reports/LowCVP-Ricardo%20Bus%20Roadmap%20FINAL.pdf |
| S28 | DfT/TRL Low Emission Bus Scheme monitoring 2022: Euro VI diesel baseline 47.2 L/100 km on the MLTB cycle — https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf |
| S29 | DfT road freight statistics 2010: rigid HGVs average 9.1 mpg, articulated 7.6 mpg — https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf |
| S30 | Zemo/Ricardo low-carbon HGV roadmap 2010: 40-44 t artic 8 mpg (36 L/100 km); 7.5-26 t delivery 12 mpg (24 L/100 km); 7.5 t benchmark 20.6 L/100 km — https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf |
| S31 | Perrotta et al., HDM-4 verification using 1,645 trucks of telematics data: median 15.5 L/100 km light, 23.3 medium, 26.5 heavy trucks — https://nottingham-repository.worktribe.com/index.php/OutputFile/1317351 |
| S32 | Zemo, Alternative fuel costs - bus operators: London midibus 8 mpg, double-decker 5 mpg — https://www.zemo.org.uk/assets/workingdocuments/ACFNFAxSaWaY.pdf |
| S33 | TRID abstract of Andrist and Rose, 'The trolleybus - can it be reintroduced?' (1980): thyristor control and regenerative braking reduced consumption from about 4.8 to 2.5 kWh/km — https://trid.trb.org/view/160001 |

### 1.4 How the figures were assigned

**Liquid fuels (petrol, diesel).** Measured service consumption per km is used wherever a figure exists for the model or for a vehicle of the same class, era and size. Because a bus or lorry spends much of its life accelerating and idling, the service figure per km is close to the per-km figure at its normal maximum speed, and it is not scaled with speed. Where no measured figure exists for a model, the nearest documented vehicle of the same class is the anchor and the figure is scaled by rated power with a 0.5 exponent:

```
C = C0 x (P / P0)^0.5
```

The result is then capped at the flow the engine could physically deliver at full output, using brake-specific fuel consumption by era (petrol 400 g/kWh before 1930, 340 to 1960, 315 after; diesel 260 before 1960, 235 to 1990, 210 after) and fuel density (petrol 0.735 kg/L, diesel 0.84 kg/L):

```
C_max (mL/km) = BSFC (g/kWh) x P (kW) / (density (kg/L) x v (km/h))
```

Worked example, Routemaster: 235 x 86 / (0.84 x 73) = 20,210 / 61.3 = 330 mL/km, so the measured 8-10 mpg figure of 320 mL/km sits just inside the engine's full-output flow (23.4 L/h at 73 km/h). The cap only bites on objects given an unusually high top speed for their engine, for example the Leyland Tiger Cub PSUC1/2 at 113 km/h, which is held to 185 mL/km instead of the class figure of 250.

**Steam.** The Commercial Motor tests give coal per mile on a measured run at a known average speed. Those are steady-road figures, so they are converted from the test speed to the pakset calibration speed with an exponent of 0.7 (steam flow rises with speed but not in proportion, because boiler and transmission losses are large at low output):

```
C_cal = C_test x (v_cal / v_test)^0.7
```

Worked example, Sentinel DG6 (1930 test): 218 lb of coal in 41.8 miles = 5.21 lb/mile = 1468 g/km at 13.6 mph (21.9 km/h). At the pakset's 20 km/h calibration speed: 1468 x (20/21.9)^0.7 = 1378, rounded to 1450 g/km. The same boiler on pneumatic tyres is calibrated at 50 km/h and therefore takes 2400 g/km: 1468 x (50/21.9)^0.7 = 2510, rounded to 2400. The Sentinel S4 (1933 test, and 1.05 kg/km at about 40 km/h in the 1968 re-test) gives 1050 x (65/40)^0.7 = 1480, rounded to 1500 g/km at 65 km/h.

**Electric.** Trolleybus consumption is taken from undertaking returns and from Sinclair's 1939 IEE paper: 1.65-1.69 units per car-mile (about 1.0 kWh/km) for the 1920s and early 1930s systems, 2.75 units per car-mile at the substation (1.7 kWh/km) for the large 1930s London fleet. Values rise with size and era from 950 to 1750 Wh/km. These are energy drawn from the wires, which is what `fuel[electric]` prices. The one battery vehicle, the Optare Solo EV, is given 800 Wh/km. The Zemo figure of about 0.8 kWh/km for a city electric bus is measured at the charging infrastructure; treating it as energy at the wheels, with no deduction for charging losses, is conservative and leaves the engine's 85% battery round-trip efficiency to be applied on top.

**Zero.** Horse-drawn vehicles, hand carts, trailers, the rear half-units of articulated buses (`MercedesCitaroG(Rear)`, `WrightStreetcar(Rear)`, both 0 kW) and the road hold `mail-boot` are 0. For horses this follows the note in `New/config/fuel.tab` that fodder belongs in fixed maintenance and `fuel[bio]` is priced at 0. Every trailer in the sector is unpowered and is drawn by a tractor that carries its own figure.

### 1.5 Sanity checks against price and running cost

Fuel cost per km in the year of the price is `mL/km x pence per litre / 1000`:

| vehicle | figure | price in year | fuel cost |
|---|---|---|---|
| Routemaster, 1956 | 320 mL/km | 6.19p/L | 1.98p/km (8.8 mpg) |
| Leyland Comet, 1947 | 235 mL/km | 2.35p/L | 0.55p/km |
| Dennis Enviro400, 2006 | 380 mL/km | 94.2p/L | 35.8p/km |
| Sentinel S4, 1933 | 1500 g/km | 0.089p/kg | 0.13p/km |
| Karrier E6 trolleybus, 1930 | 1150 Wh/km | 0.578p/kWh | 0.66p/km |

The Enviro400 figure agrees with the Zemo statement that a typical diesel bus uses 50 L/100 km at 36p/km (S25); the Routemaster agrees with the 8-10 mpg museum figure (S5) and with the 9.75 mpg advertised for the PD2/20 (S7). The raw ratio to the pakset `runningcost` is not a useful check for modern vehicles because `runningcost` is in 1900 money and is multiplied by the maintenance index, but the ratios for 1940s-1960s vehicles fall between 1 and 2, which is where they should be.

## 2. Per-model table

One row per model and fuel figure. Where a model was built in two forms with different governing speeds (solid versus pneumatic tyres, for example) the calibration speeds are listed with a slash. Basis: DOC = measured on the vehicle or an identical one; DER = derived from a documented class anchor by the power scaling in 1.4; EST = estimate anchored on the class figure named in the source column.

| model | fuel_per_km | calibration_speed | cut_off_speed | range (km) | basis | source |
|---|---|---|---|---|---|---|
| A1 Diddler trolleybus (1931) | 1000 | 48 | 24 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| ADC 416 | 315 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| ADC 416 | 365 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| ADC 423 | 365 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| ADC 424 coach | 325 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| ADC 802 | 560 | 32 | 16 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| AEC 602 trolleybus | 1000 | 34 | 17 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 602 trolleybus (pneumatic) | 1000 | 37 | 18 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 603 trolleybus | 1050 | 45 | 22 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 605 trolleybus | 1050 | 48 | 24 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 607 trolleybus | 1100 | 32 | 16 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 607 trolleybus (pneumatic) | 1100 | 40 | 20 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 661T trolleybus | 1300 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 661T/2 trolleybus | 1400 | 56 | 28 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 662T trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC 664T trolleybus | 1400 | 56 | 28 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| AEC K-type double-deck | 520 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| AEC K-type single-deck | 520 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| AEC NS-type | 440 | 32 | 16 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| AEC NS-type | 480 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| AEC Q2 petrol double-deck | 400 | 55 | 28 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| AEC Q4 oiler | 235 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| AEC Q5 oiler | 235 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| AEC Q6 oiler | 230 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| AEC Regal | 370 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| AEC Regal 10T10 coach | 225 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| AEC Regal 15T13 | 235 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| AEC Regal 9T9 coach | 230 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| AEC Regal T coach | 215 | 84 | 42 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| AEC Regent RT2 | 290 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| AEC Regent RT3 | 300 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| AEC Regent ST petrol | 435 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| AEC Reliance | 375 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| AEC Reliance (1954) | 260 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| AEC Reliance coach | 280 | 60 | 30 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| AEC Reliance long (1962) | 255 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| AEC Renown LT Bluebird (diesel) | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| AEC Renown LT Bluebird (petrol) | 435 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| AEC Renown LT petrol | 420 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| AEC Renown LT Scooter | 420 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| AEC RF | 280 | 56 | 28 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| AEC RF coach | 270 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| AEC S-type double-deck | 500 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| AEC S-type single-deck | 500 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| AEC STL (diesel, 1936) | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| AEC STL petrol | 435 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| AEC Swift | 280 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Austin Maestro van | 85 | 105 | 52 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Austin Seven van | 70 | 42 | 21 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Austin Twelve taxi (1921) | 95 | 70 | 35 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Austin Twelve taxi (1939) | 100 | 87 | 44 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Austin/Morris EA van | 110 | 82 | 41 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Bedford OB | 340 | 64 | 32 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Bedford WTB | 345 | 64 | 32 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Bradford Brown trolleybus (1913) | 950 | 37 | 18 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| BUT 9611T trolleybus | 1500 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| BUT 9613T trolleybus | 1550 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| BUT RETB1 trolleybus | 1550 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| BUT RETB1/1 trolleybus | 1500 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Caetano Levante 2-axle coach | 300 | 96 | 48 |  | EST (estimate) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Caetano Levante 3-axle coach | 310 | 96 | 48 |  | EST (estimate) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Cedes-Stoll double-deck trolleybus (1914) | 950 | 30 | 15 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| DAF CF artic (265 kW) | 380 | 90 | 45 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| DAF CF rigid | 310 | 90 | 45 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| DAF LF | 210 | 100 | 50 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| DAF XF artic (355 kW) | 400 | 90 | 45 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Daimler CC double-deck | 600 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Daimler CC single-deck | 600 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Daimler CF6 coach | 390 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Daimler CF6 single-deck | 390 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Daimler CH6 coach | 260 | 64 | 32 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Daimler CH6 double-deck | 335 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Daimler CH6 single-deck | 335 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Daimler CLG5 | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CLG6 | 245 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler COG5 coach | 235 | 64 | 32 |  | DOC (measured) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler COG5 double-deck | 240 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler COG5 single-deck | 235 | 50 | 25 |  | DOC (measured) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler COG6 double-deck | 230 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CP6 coach | 400 | 64 | 32 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Daimler CP6 double-deck | 420 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Daimler CP6 single-deck | 410 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Daimler CVA6 | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CVD6 coach | 245 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CVG5 | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CVG6 | 245 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CVG6/30 | 245 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler CVG6LX/30 | 270 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Daimler CWA6 | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Daimler Fleetline | 310 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Daimler Fleetline DMS | 320 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Daimler Freeline coach | 250 | 80 | 40 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Daimler wagonette (1901) | 300 | 20 | 10 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Dennis 15 cwt omnibus (1904) | 245 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Dennis 15 cwt van (1904) | 165 | 30 | 15 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Dennis 30 cwt bus (1924) | 295 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Dennis 30 cwt van (1912) | 220 | 34 | 17 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Dennis 30 cwt van (pneumatic, 1924) | 220 | 50 | 25 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Dennis 4-ton bus (1923) | 430 | 20 | 10 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Dennis 4-ton bus (pneumatic, 1928) | 400 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Dennis 4-ton single-deck bus (1921) | 430 | 20 | 10 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Dennis 4-ton single-deck bus (pneumatic, 1925) | 400 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Dennis Ace | 300 | 68 | 34 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Arrow (new) | 360 | 80 | 40 |  | DER (documented anchor, power-scaled) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Dennis Dart | 290 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Dart (1929) | 325 | 80 | 40 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Dart 9.8 m | 290 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Dart SLF 10.1 m | 290 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Dart SLF 9.2 m | 290 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Dominator | 330 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Dominator trolleybus (1977) | 1700 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Dennis E bus | 450 | 42 | 21 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Enviro200 10.2 m | 300 | 76 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro200 10.8 m | 300 | 76 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro200 8.9 m | 300 | 76 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro200 MMC 10.4 m | 300 | 76 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro200 MMC 11.8 m | 310 | 76 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro200 MMC 8.9 m | 295 | 76 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro300 | 340 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro350H hybrid | 380 | 64 | 32 | 100 | EST (estimate) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Dennis Enviro400 | 380 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro400 MMC | 375 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro400 MMC | 380 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Enviro400H City hybrid | 390 | 64 | 32 |  | EST (estimate) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Dennis EV bus | 370 | 65 | 32 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis F | 400 | 62 | 31 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Falcon | 330 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis FS | 360 | 75 | 38 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis G | 295 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis GL | 300 | 56 | 28 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis H | 480 | 32 | 16 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Lance | 400 | 55 | 28 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Lance (new) | 330 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Lance II | 400 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Lance SLF | 330 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Dennis Lancet | 255 | 50 | 25 |  | DOC (measured) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Lancet coach | 240 | 85 | 42 |  | DOC (measured) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Lancet II | 165 | 50 | 25 |  | DOC (measured) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Lancet II coach | 160 | 85 | 42 |  | DOC (measured) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Dennis Trident | 350 | 80 | 40 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| EE A-type trolleybus | 1150 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| EE E11 trolleybus | 1300 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| EE E11/100 trolleybus | 1350 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |  | DOC (measured) | [S14](https://archive.commercialmotor.com/article/16th-february-1911/27/concerning-steam-wagons-generally) |
| Ford Escort van | 85 | 105 | 52 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Ford Transit | 110 | 96 | 48 |  | EST (estimate) | [S31](https://nottingham-repository.worktribe.com/index.php/OutputFile/1317351) |
| Ford Transit Connect | 70 | 110 | 55 |  | EST (estimate) | [S31](https://nottingham-repository.worktribe.com/index.php/OutputFile/1317351) |
| Ford Transit Mk 1 | 110 | 86 | 43 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Ford Transit Mk 1 minibus | 110 | 86 | 43 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Guy 30 cwt minibus | 300 | 20 | 10 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Guy Arab | 300 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Guy Arab (1933) | 300 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Guy Arab III | 290 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Guy Arab IV | 290 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Guy Arab Mk II | 290 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Guy Arab V | 290 | 56 | 28 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Guy BB | 425 | 55 | 28 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Guy BT32 trolleybus | 1050 | 48 | 24 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BT32/2 trolleybus | 1100 | 64 | 32 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BT48 trolleybus | 1150 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BT56 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BTX39 trolleybus | 1250 | 67 | 34 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BTX40 trolleybus | 1150 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BTX60 trolleybus | 1150 | 45 | 22 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BTX66 trolleybus | 1250 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BTX68 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Guy BTX68/2 trolleybus | 1400 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Guy FBB | 480 | 45 | 22 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Guy FC | 510 | 32 | 16 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Guy FCX | 550 | 32 | 16 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Guy OND | 275 | 55 | 28 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Guy Special | 230 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Horse-drawn or man-powered (no engine) | 0 | 5-20 | 0 |  | 0 (no engine) | - |
| Karrier E4 single-deck trolleybus | 1150 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier E4 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier E4/2 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier E6 trolleybus | 1150 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier E6/2 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier E6/3 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier E6A trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier W4 trolleybus | 1250 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier W4R trolleybus | 1250 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier W4S trolleybus | 1250 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Karrier W4SR trolleybus | 1250 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland Atlantean | 295 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Atlantean | 310 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Atlantean AN68 | 320 | 75/87 | 38/44 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Atlantean PDR2/1 | 310 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Cheetah LZ2 | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Cheetah LZ2 coach | 245 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland class B steam wagon (1901) | 3500 | 12 | 6 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Leyland class F steam wagon (1911) | 2800 | 18 | 9 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Leyland class H steam wagon (1905) | 3200 | 12 | 6 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Leyland Comet | 235 | 61 | 30 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Leyland Cub | 415 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Cub KPO2 diesel | 240 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Leyland Cub KPZ1 diesel | 240 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S6](https://forum.simutrans.com/index.php?msg=166768) |
| Leyland Cub KPZ1 petrol | 380 | 64 | 32 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland DAF 200 van | 110 | 96 | 48 |  | EST (estimate) | [S31](https://nottingham-repository.worktribe.com/index.php/OutputFile/1317351) |
| Leyland DAF 65 | 220 | 100 | 50 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| Leyland DAF 85 artic (279 kW) | 390 | 88 | 44 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Leyland DAF 85 rigid | 310 | 88 | 44 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| Leyland DAF 95 artic (282 kW) | 390 | 88 | 44 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Leyland G | 120 | 95 | 48 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland G | 245 | 95 | 48 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland K2 trolleybus | 1300 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland Leopard L1 | 280 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leopard L2 | 280 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leopard PSU3 | 280 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leopard PSU3 bus | 280 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leopard PSU3A | 280 | 96 | 48 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leopard PSU3A bus | 280 | 85 | 42 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leopard PSU5 | 285 | 96 | 48 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Leveret LA | 500 | 32 | 16 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Leyland Lion LSC1 | 500 | 32 | 16 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Leyland Lion LSC3 | 480 | 40 | 20 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Leyland Lion LT1 | 435 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Leyland Lion LT5A | 370 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Leyland Lion LT7 diesel | 250 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Leyland Lioness LC1 | 435 | 50 | 25 |  | EST (estimate) | [S10](https://archive.commercialmotor.com/article/23rd-february-1926/7/wheels-of-industry) |
| Leyland Lynx | 330 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland National | 300 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland National 2 | 310 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland National 2 standee | 330 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland National B | 310 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland National LNC | 300 | 85 | 42 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Olympian | 340 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Olympian coach | 330 | 96 | 48 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Panther PSUR1 | 300 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Panther PSUR1A | 300 | 85 | 42 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Roadrunner | 175 | 100 | 50 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| Leyland Royal Tiger PSU1/11 | 250 | 90 | 45 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Royal Tiger PSU1/9 | 260 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Sherpa | 110 | 86 | 43 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Leyland T45 Constructor | 360 | 86 | 43 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Leyland T45 Roadtrain (173 kW) | 360 | 86 | 43 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| Leyland TB2 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland TB3 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland TB4 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland TBD1 trolleybus | 1150 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland Tiger Cub PSUC1/1 | 250 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger Cub PSUC1/2 | 185 | 113 | 56 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger PS1 | 270 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger PS1/1 | 270 | 85 | 42 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger PS2/13 | 260 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger PS2/14 | 260 | 90 | 45 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger PS2/5 | 260 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger PS2/7 | 260 | 90 | 45 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger TF | 270 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger TR | 350 | 96 | 48 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Tiger TS1 (comfort) | 400 | 62 | 31 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS1 (popular) | 410 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS4 | 400 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS4 coach | 380 | 85 | 42 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS6 | 400 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS6 coach | 380 | 82 | 41 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS6T | 400 | 50 | 25 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS6T coach | 380 | 82 | 41 |  | EST (estimate) | [S3](https://forum.simutrans.com/index.php?msg=159560) |
| Leyland Tiger TS7 | 280 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger TS7 coach | 270 | 80 | 40 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger TS7T | 280 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Tiger TS7T coach | 270 | 80 | 40 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan B15 | 380 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Leyland Titan PD1 | 290 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan PD2/1 | 290 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan PD2/12 | 290 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan PD2/3 | 290 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan PD2/30 | 290 | 50 | 25 |  | DOC (measured) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan PD3/1 | 300 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S7](https://forum.simutrans.com/index.php?msg=198196) |
| Leyland Titan TD1 | 420 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Leyland Titan TD2 | 410 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Leyland Titan TD3 | 410 | 50 | 25 |  | EST (estimate) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Leyland Titan TD4 diesel | 280 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S13](https://archive.commercialmotor.com/article/24th-february-1931/43/the-oil-engine-progresses) |
| Leyland TTB2 trolleybus | 1300 | 50 | 25 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland TTB3 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Leyland TTBD1 trolleybus | 1200 | 48 | 24 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| LGOC B-type double-deck | 565 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| LGOC B-type single-deck | 565 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| LGOC X-type double-deck | 515 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Maudslay van (1907) | 235 | 30 | 15 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| MCW Metrorider long | 290 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| MCW Metrorider short | 290 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| MCW Q1 trolleybus (1948) | 1400 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Mercedes Citaro | 360 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Mercedes Citaro G artic | 430 | 65 | 32 |  | DER (documented anchor, power-scaled) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Mercedes Citaro G artic (rear unit, no engine) | 0 | 65 | 32 |  | 0 (no engine) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Mercedes Citaro K | 340 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Milnes-Daimler double-deck | 570 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Milnes-Daimler single-deck | 570 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Milnes-Daimler single-deck (1902) | 515 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Morris Eight van | 100 | 80 | 40 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Morris FG | 120 | 88 | 44 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Morris J4 | 130 | 81 | 40 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Morris LD | 120 | 76/77 | 38/38 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Morris Marina van | 95 | 100 | 50 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Morris Minor van | 80 | 115 | 58 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Optare Alero | 260 | 75 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Delta | 380 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Excel | 350 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Excel 2 | 350 | 77 | 38 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Metrorider long | 300 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Metrorider short | 300 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Solo | 250 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Solo EV battery bus | 800 | 70 | 35 | 40 | DOC (measured) | [S25](https://www.zemo.org.uk/assets/workingdocuments/BWG-P-05-21%20Bus%20Driveline%20Economics.pdf) |
| Optare Solo SR | 240 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Tempo | 380 | 74 | 37 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Optare Tempo SR | 370 | 74 | 37 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| RET B10 trolleybus (1920) | 1000 | 32 | 16 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| RET F12 trolleybus (1922) | 1200 | 29 | 14 |  | DER (documented anchor, power-scaled) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| RET Hurst Nelson trolleybus (1911) | 1000 | 32 | 16 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| RET LF30 trolleybus (1925) | 1150 | 32 | 16 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Road hold (no engine) | 0 | 18 | 9 |  | 0 (no engine) | - |
| Road locomotive / traction engine | 6260 | 15 | 8 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Road locomotive / traction engine | 7000 | 20 | 10 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Routemaster | 320 | 73 | 36 |  | DOC (measured) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Routemaster coach | 265 | 90 | 45 |  | DOC (measured) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Routemaster long | 320 | 73 | 36 |  | DOC (measured) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Routemaster long coach | 265 | 90 | 45 |  | DOC (measured) | [S5](https://forum.simutrans.com/index.php?msg=161438) |
| Routemaster trolleybus conversion (1966) | 1750 | 50 | 25 |  | EST (estimate) | [S23](https://doi.org/10.1038/144989a0) |
| Scammell Crusader | 400 | 84 | 42 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Scammell Handyman/Highwayman | 320 | 68 | 34 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Scammell Handyman/Highwayman | 350 | 79 | 40 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Scammell Mechanical Horse (petrol) | 250 | 32 | 16 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Scammell Routeman | 280 | 79 | 40 |  | DER (documented anchor, power-scaled) | [S30](https://www.zemo.org.uk/assets/reports/low%20carbon%20HGV%20roadmapping.pdf) |
| Scammell Scarab (petrol) | 240 | 50 | 25 |  | EST (estimate) | [S11](https://archive.commercialmotor.com/article/3rd-november-1925/5/long---distance-morris-trials) |
| Scammell Townsman (diesel) | 200 | 80 | 40 |  | EST (estimate) | [S31](https://nottingham-repository.worktribe.com/index.php/OutputFile/1317351) |
| Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |  | DOC (measured) | [S18](https://archive.commercialmotor.com/article/4th-february-1930/50/the-road-performance-o-a-popular-six-wheeled-steam) |
| Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |  | DOC (measured) | [S18](https://archive.commercialmotor.com/article/4th-february-1930/50/the-road-performance-o-a-popular-six-wheeled-steam) |
| Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |  | DOC (measured) | [S18](https://archive.commercialmotor.com/article/4th-february-1930/50/the-road-performance-o-a-popular-six-wheeled-steam) |
| Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |  | DOC (measured) | [S18](https://archive.commercialmotor.com/article/4th-february-1930/50/the-road-performance-o-a-popular-six-wheeled-steam) |
| Sentinel S4 | 1500 | 65 | 32 |  | DOC (measured) | [S20](https://archive.commercialmotor.com/article/16th-june-1933/45/road-test-no-149) |
| Sentinel S6 | 1600 | 65 | 32 |  | EST (estimate) | [S22](https://archive.commercialmotor.com/article/16th-february-1934/42/a-modern-steamei) |
| Sentinel standard (1906) | 3300 | 18 | 9 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |  | EST (estimate) | [S15](https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career) |
| Straker LL trolleybus | 1100 | 40 | 20 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Straker-Squire A-type double-deck trolleybus | 1100 | 30 | 15 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Straker-Squire trolleybus | 1000 | 35 | 18 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Straker-Squire trolleybus (pneumatic) | 1000 | 38 | 19 |  | EST (estimate) | [S24](https://ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf) |
| Sunbeam F4 trolleybus | 1450 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Sunbeam F4A trolleybus | 1550 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Sunbeam F4S trolleybus | 1450 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Sunbeam S7 trolleybus | 1500 | 55 | 28 |  | DER (documented anchor, power-scaled) | [S23](https://doi.org/10.1038/144989a0) |
| Super-Sentinel (1923) | 1600 | 20 | 10 |  | DOC (measured) | [S16](https://archive.commercialmotor.com/article/20th-november-1923/26/trying-out-an-undertype-steam-wagon) |
| Super-Sentinel (pneumatic) | 2250 | 32 | 16 |  | DOC (measured) | [S16](https://archive.commercialmotor.com/article/20th-november-1923/26/trying-out-an-undertype-steam-wagon) |
| Thornycroft Amazon tractor | 380 | 50 | 25 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Thornycroft BT lorry (1913) | 190 | 34 | 17 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Thornycroft Q artic tractor | 300 | 34 | 17 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Thornycroft Q rigid | 300 | 34 | 17 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Thornycroft QC | 380 | 39/47 | 20/24 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Thornycroft Stag | 360 | 56 | 28 |  | EST (estimate) | [S12](https://archive.commercialmotor.com/article/16th-october-1923/8/one-hundred-ton-miles-to-the-gallon) |
| Thornycroft steam van (1896) | 900 | 16 | 8 |  | EST (estimate) | [S14](https://archive.commercialmotor.com/article/16th-february-1911/27/concerning-steam-wagons-generally) |
| Thornycroft steam wagon (1900) | 3000 | 12 | 6 |  | EST (estimate) | [S14](https://archive.commercialmotor.com/article/16th-february-1911/27/concerning-steam-wagons-generally) |
| Tilling-Stevens TS3 | 430 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TS3 single-deck | 430 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TS3A | 420 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TS7 double-deck | 420 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TS7 double-deck (pneumatic) | 420 | 32 | 16 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TS7 single-deck | 420 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TS7 single-deck (pneumatic) | 420 | 32 | 16 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TTA1 petrol-electric | 450 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TTA1 single-deck | 450 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Tilling-Stevens TTA2 | 430 | 20 | 10 |  | EST (estimate) | [S9](https://archive.commercialmotor.com/article/11th-april-1907/61/petrol-motor-omnibuses) |
| Unpowered trailer | 0 | 12-86 | 0 |  | 0 (no engine) | - |
| Volvo Alisa | 340 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Volvo B10M coach | 300 | 96 | 48 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Volvo B12M coach | 320 | 96 | 48 |  | DER (documented anchor, power-scaled) | [S29](https://assets.publishing.service.gov.uk/media/5a79d4cc40f0b670a8025be7/domestic-activity-of-GB-registered-heavy-goods-vehicles.pdf) |
| Volvo B7TL | 400 | 72 | 36 |  | DER (documented anchor, power-scaled) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Volvo Citybus | 380 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Volvo Olympian | 360 | 64 | 32 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Wright Electrocity | 340 | 70 | 35 |  | DER (documented anchor, power-scaled) | [S26](https://www.zemo.org.uk/assets/reports/EY_Report_Low_Carbon_Investment_-_Scottish_Bus_Electrification_commercial_and_economic_content_report.pdf) |
| Wright Streetcar | 450 | 84 | 42 |  | DER (documented anchor, power-scaled) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Wright Streetcar (rear unit, no engine) | 0 | 84 | 42 |  | 0 (no engine) | [S28](https://assets.publishing.service.gov.uk/media/646f304c24315700136f4228/lebs-monitoring-report.pdf) |
| Yorkshire steam wagon WH | 1400 | 55 | 28 |  | EST (estimate) | [S21](https://archive.commercialmotor.com/article/20th-december-1968/36/commercial-motor-christmas-road-test) |

## 3. Object mapping table

Every object in `ai/temp/sector-road.txt`, in checklist order, with the exact `.dat` name. `fuel_per_km` and the two speed fields are repeated so the table can be applied mechanically.

| object | model | fuel_per_km | calibration_speed | cut_off_speed |
|---|---|---|---|---|
| mail-boot | Road hold (no engine) | 0 | 18 | 9 |
| A1Diddler | A1 Diddler trolleybus (1931) | 1000 | 48 | 24 |
| adc-416a | ADC 416 | 315 | 45 | 22 |
| adc-416d | ADC 416 | 365 | 45 | 22 |
| adc-423 | ADC 423 | 365 | 45 | 22 |
| adc-424-coach | ADC 424 coach | 325 | 50 | 25 |
| adc-802 | ADC 802 | 560 | 32 | 16 |
| aec-602-pneumatic | AEC 602 trolleybus (pneumatic) | 1000 | 37 | 18 |
| aec-602 | AEC 602 trolleybus | 1000 | 34 | 17 |
| aec-603 | AEC 603 trolleybus | 1050 | 45 | 22 |
| aec-605 | AEC 605 trolleybus | 1050 | 48 | 24 |
| aec-607-pneumatic | AEC 607 trolleybus (pneumatic) | 1100 | 40 | 20 |
| aec-607 | AEC 607 trolleybus | 1100 | 32 | 16 |
| aec-661t-2 | AEC 661T/2 trolleybus | 1400 | 56 | 28 |
| aec-661t | AEC 661T trolleybus | 1300 | 48 | 24 |
| aec-662t | AEC 662T trolleybus | 1200 | 48 | 24 |
| aec-664t | AEC 664T trolleybus | 1400 | 56 | 28 |
| AECQ2 | AEC Q2 petrol double-deck | 400 | 55 | 28 |
| AECQ4 | AEC Q4 oiler | 235 | 55 | 28 |
| aec-q5 | AEC Q5 oiler | 235 | 55 | 28 |
| aec-q6 | AEC Q6 oiler | 230 | 70 | 35 |
| aec-regal-coach-10t10 | AEC Regal 10T10 coach | 225 | 70 | 35 |
| aec-regal-15t13 | AEC Regal 15T13 | 235 | 50 | 25 |
| aec-regal-coach-9t9 | AEC Regal 9T9 coach | 230 | 70 | 35 |
| aec-regal-t-coach | AEC Regal T coach | 215 | 84 | 42 |
| AECRegalT | AEC Regal | 370 | 50 | 25 |
| aec-regent-rt-2 | AEC Regent RT2 | 290 | 50 | 25 |
| aec-regent-rt-3 | AEC Regent RT3 | 300 | 50 | 25 |
| AECRegentST | AEC Regent ST petrol | 435 | 50 | 25 |
| aec-reliance-coach | AEC Reliance coach | 280 | 60 | 30 |
| aec-reliance-new-long | AEC Reliance long (1962) | 255 | 72 | 36 |
| aec-reliance-new | AEC Reliance (1954) | 260 | 64 | 32 |
| AECReliance | AEC Reliance | 375 | 45 | 22 |
| aec-renown-lt-bluebird-petrol | AEC Renown LT Bluebird (petrol) | 435 | 50 | 25 |
| aec-renown-lt-bluebird | AEC Renown LT Bluebird (diesel) | 250 | 50 | 25 |
| aec-renown-lt-scooter | AEC Renown LT Scooter | 420 | 50 | 25 |
| AECRenownLT | AEC Renown LT petrol | 420 | 50 | 25 |
| aec-regent-stl-late | AEC STL (diesel, 1936) | 250 | 50 | 25 |
| aec-regent-stl | AEC STL petrol | 435 | 50 | 25 |
| AECSwift | AEC Swift | 280 | 72 | 36 |
| AustinMaestroCool | Austin Maestro van | 85 | 105 | 52 |
| AustinMaestroPiece | Austin Maestro van | 85 | 105 | 52 |
| AustinMaestroPost | Austin Maestro van | 85 | 105 | 52 |
| AustinMorrisEACool | Austin/Morris EA van | 110 | 82 | 41 |
| AustinMorrisEAPiece | Austin/Morris EA van | 110 | 82 | 41 |
| AustinMorrisEAPost | Austin/Morris EA van | 110 | 82 | 41 |
| AustinSevenCool | Austin Seven van | 70 | 42 | 21 |
| AustinSevenPiece | Austin Seven van | 70 | 42 | 21 |
| AustinSevenPost | Austin Seven van | 70 | 42 | 21 |
| AustinTwelve-Taxi-1921 | Austin Twelve taxi (1921) | 95 | 70 | 35 |
| AustinTwelve-Taxi-1939 | Austin Twelve taxi (1939) | 100 | 87 | 44 |
| BTypeDouble | LGOC B-type double-deck | 565 | 20 | 10 |
| BTypeSingle | LGOC B-type single-deck | 565 | 20 | 10 |
| bedford-ob | Bedford OB | 340 | 64 | 32 |
| bedford-wtb | Bedford WTB | 345 | 64 | 32 |
| bradford-brown-trolleybus | Bradford Brown trolleybus (1913) | 950 | 37 | 18 |
| but-9611t | BUT 9611T trolleybus | 1500 | 55 | 28 |
| but-9613t | BUT 9613T trolleybus | 1550 | 55 | 28 |
| but-retb1-1 | BUT RETB1/1 trolleybus | 1500 | 55 | 28 |
| but-retb1 | BUT RETB1 trolleybus | 1550 | 50 | 25 |
| caetano-levante-2-axle | Caetano Levante 2-axle coach | 300 | 96 | 48 |
| caetano-levante-3-axle | Caetano Levante 3-axle coach | 310 | 96 | 48 |
| CartBulk | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| CartCool | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| CartLong | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| CartMail | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| CartMailNew | Horse-drawn or man-powered (no engine) | 0 | 12 | 6 |
| CartPiece | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| cedes-trolley-double | Cedes-Stoll double-deck trolleybus (1914) | 950 | 30 | 15 |
| DAFCFRigidBulk | DAF CF rigid | 310 | 90 | 45 |
| DAFCFRigidFluid | DAF CF rigid | 310 | 90 | 45 |
| DAFCFRigidLong | DAF CF rigid | 310 | 90 | 45 |
| DAFLFBulk | DAF LF | 210 | 100 | 50 |
| DAFLFCool | DAF LF | 210 | 100 | 50 |
| DAFLFLivestock | DAF LF | 210 | 100 | 50 |
| DAFLFLong | DAF LF | 210 | 100 | 50 |
| DAFLFPiece | DAF LF | 210 | 100 | 50 |
| DAFLFPost | DAF LF | 210 | 100 | 50 |
| daimler-cc-double | Daimler CC double-deck | 600 | 20 | 10 |
| daimler-cc-single | Daimler CC single-deck | 600 | 20 | 10 |
| daimler-cf6-coach | Daimler CF6 coach | 390 | 50 | 25 |
| daimler-cf6-single | Daimler CF6 single-deck | 390 | 50 | 25 |
| daimler-ch6-coach | Daimler CH6 coach | 260 | 64 | 32 |
| daimler-ch6-double | Daimler CH6 double-deck | 335 | 50 | 25 |
| daimler-ch6-single | Daimler CH6 single-deck | 335 | 50 | 25 |
| daimler-clg5-double | Daimler CLG5 | 250 | 50 | 25 |
| daimler-clg6-double | Daimler CLG6 | 245 | 50 | 25 |
| daimler-cog5-coach | Daimler COG5 coach | 235 | 64 | 32 |
| daimler-cog5-double | Daimler COG5 double-deck | 240 | 50 | 25 |
| daimler-cog5-single | Daimler COG5 single-deck | 235 | 50 | 25 |
| daimler-cog6-double | Daimler COG6 double-deck | 230 | 50 | 25 |
| daimler-cp6-coach | Daimler CP6 coach | 400 | 64 | 32 |
| daimler-cp6-double | Daimler CP6 double-deck | 420 | 50 | 25 |
| daimler-cp6-single | Daimler CP6 single-deck | 410 | 50 | 25 |
| daimler-cva6-double | Daimler CVA6 | 250 | 50 | 25 |
| daimler-cvd6-coach | Daimler CVD6 coach | 245 | 72 | 36 |
| daimler-cvg5-single | Daimler CVG5 | 250 | 50 | 25 |
| daimler-cvg6-30-double | Daimler CVG6/30 | 245 | 50 | 25 |
| daimler-cvg6-double | Daimler CVG6 | 245 | 50 | 25 |
| daimler-cvg6lx-30-double | Daimler CVG6LX/30 | 270 | 64 | 32 |
| daimler-cwa6-double | Daimler CWA6 | 250 | 50 | 25 |
| daimler-fleetline-dms | Daimler Fleetline DMS | 320 | 64 | 32 |
| daimler-fleetline | Daimler Fleetline | 310 | 64 | 32 |
| daimler-freeline-coach | Daimler Freeline coach | 250 | 80 | 40 |
| daimler-wagonette | Daimler wagonette (1901) | 300 | 20 | 10 |
| dennis-15cwt-omnibus | Dennis 15 cwt omnibus (1904) | 245 | 20 | 10 |
| dennis-15cwt-van-cool | Dennis 15 cwt van (1904) | 165 | 30 | 15 |
| dennis-15cwt-van-piece | Dennis 15 cwt van (1904) | 165 | 30 | 15 |
| dennis-15cwt-van-post | Dennis 15 cwt van (1904) | 165 | 30 | 15 |
| dennis-30cwt-bus | Dennis 30 cwt bus (1924) | 295 | 50 | 25 |
| dennis-30cwt-van-pneumatic-cool | Dennis 30 cwt van (pneumatic, 1924) | 220 | 50 | 25 |
| dennis-30cwt-van-pneumatic-piece | Dennis 30 cwt van (pneumatic, 1924) | 220 | 50 | 25 |
| dennis-30cwt-van-pneumatic-post | Dennis 30 cwt van (pneumatic, 1924) | 220 | 50 | 25 |
| dennis-30cwt-van-cool | Dennis 30 cwt van (1912) | 220 | 34 | 17 |
| dennis-30cwt-van-piece | Dennis 30 cwt van (1912) | 220 | 34 | 17 |
| dennis-30cwt-van-post | Dennis 30 cwt van (1912) | 220 | 34 | 17 |
| dennis-4t-bus-pneumatic | Dennis 4-ton bus (pneumatic, 1928) | 400 | 45 | 22 |
| dennis-4t-bus-single-pneumatic | Dennis 4-ton single-deck bus (pneumatic, 1925) | 400 | 45 | 22 |
| dennis-4t-bus-single | Dennis 4-ton single-deck bus (1921) | 430 | 20 | 10 |
| dennis-4t-bus | Dennis 4-ton bus (1923) | 430 | 20 | 10 |
| dennis-ace | Dennis Ace | 300 | 68 | 34 |
| dennis-arrow-new | Dennis Arrow (new) | 360 | 80 | 40 |
| dennis-arrow-new-2-door | Dennis Arrow (new) | 360 | 80 | 40 |
| dennis-dart-9.8m-1-door | Dennis Dart 9.8 m | 290 | 75 | 38 |
| dennis-dart-9.8m-2-door | Dennis Dart 9.8 m | 290 | 75 | 38 |
| dennis-dart-original | Dennis Dart (1929) | 325 | 80 | 40 |
| dennis-dart-slf-10.1m-1-door | Dennis Dart SLF 10.1 m | 290 | 75 | 38 |
| dennis-dart-slf-10.1m-2-door | Dennis Dart SLF 10.1 m | 290 | 75 | 38 |
| dennis-dart-slf-9.2m | Dennis Dart SLF 9.2 m | 290 | 75 | 38 |
| DennisDart | Dennis Dart | 290 | 75 | 38 |
| DennisDominatorTrolley | Dennis Dominator trolleybus (1977) | 1700 | 64 | 32 |
| DennisDominator | Dennis Dominator | 330 | 75 | 38 |
| dennis-e-bus | Dennis E bus | 450 | 42 | 21 |
| dennis-enviro-200-10.2m | Dennis Enviro200 10.2 m | 300 | 76 | 38 |
| Envrio200-10.8m-1-door | Dennis Enviro200 10.8 m | 300 | 76 | 38 |
| Envrio200-10.8m-2-door | Dennis Enviro200 10.8 m | 300 | 76 | 38 |
| dennis-enviro200-8.9m | Dennis Enviro200 8.9 m | 300 | 76 | 38 |
| dennis-enviro200-mmc-10.4m-1-door | Dennis Enviro200 MMC 10.4 m | 300 | 76 | 38 |
| dennis-enviro200-mmc-10.4m-2-door | Dennis Enviro200 MMC 10.4 m | 300 | 76 | 38 |
| dennis-enviro200-mmc-11.8m-1-door | Dennis Enviro200 MMC 11.8 m | 310 | 76 | 38 |
| dennis-enviro200-mmc-11.8m-2-door | Dennis Enviro200 MMC 11.8 m | 310 | 76 | 38 |
| dennis-enviro200-mmc-8.9m | Dennis Enviro200 MMC 8.9 m | 295 | 76 | 38 |
| Enviro300 | Dennis Enviro300 | 340 | 75 | 38 |
| dennis-enviro350h-1-door | Dennis Enviro350H hybrid | 380 | 64 | 32 |
| dennis-enviro350h-2-door | Dennis Enviro350H hybrid | 380 | 64 | 32 |
| dennis-enviro400mmc-1-door | Dennis Enviro400 MMC | 375 | 64 | 32 |
| dennis-enviro400mmc-2-door | Dennis Enviro400 MMC | 380 | 64 | 32 |
| DennisEnviro400 | Dennis Enviro400 | 380 | 75 | 38 |
| DennisEnviro400-1-door | Dennis Enviro400 | 380 | 75 | 38 |
| dennis-enviro400h-city-1-door | Dennis Enviro400H City hybrid | 390 | 64 | 32 |
| dennis-enviro400h-city-2-door | Dennis Enviro400H City hybrid | 390 | 64 | 32 |
| dennis-ev-bus | Dennis EV bus | 370 | 65 | 32 |
| dennis-f | Dennis F | 400 | 62 | 31 |
| dennis-falcon | Dennis Falcon | 330 | 75 | 38 |
| dennis-fs | Dennis FS | 360 | 75 | 38 |
| dennis-g | Dennis G | 295 | 50 | 25 |
| dennis-gl | Dennis GL | 300 | 56 | 28 |
| dennis-h | Dennis H | 480 | 32 | 16 |
| dennis-lance-2 | Dennis Lance II | 400 | 50 | 25 |
| dennis-lance-new | Dennis Lance (new) | 330 | 72 | 36 |
| dennis-lance-slf-1-door | Dennis Lance SLF | 330 | 72 | 36 |
| dennis-lance-slf-2-door | Dennis Lance SLF | 330 | 72 | 36 |
| dennis-lance | Dennis Lance | 400 | 55 | 28 |
| dennis-lancet-2-coach | Dennis Lancet II coach | 160 | 85 | 42 |
| dennis-lancet-2 | Dennis Lancet II | 165 | 50 | 25 |
| dennis-lancet-coach | Dennis Lancet coach | 240 | 85 | 42 |
| dennis-lancet | Dennis Lancet | 255 | 50 | 25 |
| dennis-trident | Dennis Trident | 350 | 80 | 40 |
| EagleTrailerBulk | Unpowered trailer | 0 | 20 | 10 |
| EagleTrailerCool | Unpowered trailer | 0 | 20 | 10 |
| EagleTrailerFluid | Unpowered trailer | 0 | 20 | 10 |
| EagleTrailerLivestock | Unpowered trailer | 0 | 20 | 10 |
| EagleTrailerLong | Unpowered trailer | 0 | 20 | 10 |
| EagleTrailerPiece | Unpowered trailer | 0 | 20 | 10 |
| ee-a-type | EE A-type trolleybus | 1150 | 48 | 24 |
| ee-e11-100 | EE E11/100 trolleybus | 1350 | 48 | 24 |
| ee-e11 | EE E11 trolleybus | 1300 | 48 | 24 |
| FodenCompoundBulk | Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |
| FodenCompoundCool | Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |
| FodenCompoundLivestock | Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |
| FodenCompoundLong | Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |
| FodenCompoundPiece | Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |
| FodenCompoundTanker | Foden compound overtype 5-ton (1911) | 2700 | 20 | 10 |
| FordEscortCool | Ford Escort van | 85 | 105 | 52 |
| FordEscortPiece | Ford Escort van | 85 | 105 | 52 |
| FordEscortPost | Ford Escort van | 85 | 105 | 52 |
| FordTransitConnectCool | Ford Transit Connect | 70 | 110 | 55 |
| FordTransitConnectPiece | Ford Transit Connect | 70 | 110 | 55 |
| FordTransitConnectPost | Ford Transit Connect | 70 | 110 | 55 |
| ford-transit-mk1-minibus | Ford Transit Mk 1 minibus | 110 | 86 | 43 |
| ford-transit-mk1-cool | Ford Transit Mk 1 | 110 | 86 | 43 |
| ford-transit-mk1-piece | Ford Transit Mk 1 | 110 | 86 | 43 |
| ford-transit-mk1-post | Ford Transit Mk 1 | 110 | 86 | 43 |
| FordTransitCool | Ford Transit | 110 | 96 | 48 |
| FordTransitPiece | Ford Transit | 110 | 96 | 48 |
| FordTransitPost | Ford Transit | 110 | 96 | 48 |
| guy-30cwt-minibus | Guy 30 cwt minibus | 300 | 20 | 10 |
| guy-arab-1933 | Guy Arab (1933) | 300 | 55 | 28 |
| guy-arab-3 | Guy Arab III | 290 | 55 | 28 |
| guy-arab-4 | Guy Arab IV | 290 | 55 | 28 |
| guy-arab-5 | Guy Arab V | 290 | 56 | 28 |
| guy-arab-mk2 | Guy Arab Mk II | 290 | 55 | 28 |
| GuyArab | Guy Arab | 300 | 55 | 28 |
| guy-bb | Guy BB | 425 | 55 | 28 |
| guy-bt-48 | Guy BT48 trolleybus | 1150 | 48 | 24 |
| guy-bt-56 | Guy BT56 trolleybus | 1200 | 48 | 24 |
| guy-bt32-2 | Guy BT32/2 trolleybus | 1100 | 64 | 32 |
| guy-bt32 | Guy BT32 trolleybus | 1050 | 48 | 24 |
| guy-btx-39 | Guy BTX39 trolleybus | 1250 | 67 | 34 |
| guy-btx-40 | Guy BTX40 trolleybus | 1150 | 48 | 24 |
| guy-btx-60 | Guy BTX60 trolleybus | 1150 | 45 | 22 |
| guy-btx-66 | Guy BTX66 trolleybus | 1250 | 48 | 24 |
| guy-btx-68-2 | Guy BTX68/2 trolleybus | 1400 | 55 | 28 |
| guy-btx-68 | Guy BTX68 trolleybus | 1200 | 48 | 24 |
| guy-fbb | Guy FBB | 480 | 45 | 22 |
| guy-fc | Guy FC | 510 | 32 | 16 |
| guy-fcx | Guy FCX | 550 | 32 | 16 |
| guy-ond | Guy OND | 275 | 55 | 28 |
| guy-special | Guy Special | 230 | 64 | 32 |
| HackneyCarriage | Horse-drawn or man-powered (no engine) | 0 | 12 | 6 |
| hansom-cab | Horse-drawn or man-powered (no engine) | 0 | 14 | 7 |
| road-horse-cleveland-bay-double | Horse-drawn or man-powered (no engine) | 0 | 14 | 7 |
| road-horse-clydesdale-double | Horse-drawn or man-powered (no engine) | 0 | 11 | 6 |
| road-horse-clydesdale-single | Horse-drawn or man-powered (no engine) | 0 | 11 | 6 |
| road-horse-friesian-double | Horse-drawn or man-powered (no engine) | 0 | 12 | 6 |
| road-horse-hackney-double | Horse-drawn or man-powered (no engine) | 0 | 13 | 6 |
| road-horse-hackney-single | Horse-drawn or man-powered (no engine) | 0 | 13 | 6 |
| road-horse-irish-draught-double | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| road-horse-irish-draught-single | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| road-horse-pony-double | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| road-horse-pony-single | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| road-horse-shire-double | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| road-horse-shire-single | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| road-horse-yorkshire-coach-double | Horse-drawn or man-powered (no engine) | 0 | 18 | 9 |
| aec-k-type-single | AEC K-type single-deck | 520 | 20 | 10 |
| KTypeDouble | AEC K-type double-deck | 520 | 20 | 10 |
| karrier-e4-2 | Karrier E4/2 trolleybus | 1200 | 48 | 24 |
| karrier-e4-single | Karrier E4 single-deck trolleybus | 1150 | 48 | 24 |
| karrier-e4 | Karrier E4 trolleybus | 1200 | 48 | 24 |
| karrier-e6-2 | Karrier E6/2 trolleybus | 1200 | 48 | 24 |
| karrier-e6-3 | Karrier E6/3 trolleybus | 1200 | 48 | 24 |
| karrier-e6 | Karrier E6 trolleybus | 1150 | 48 | 24 |
| karrier-e6a | Karrier E6A trolleybus | 1200 | 48 | 24 |
| karrier-w4-r | Karrier W4R trolleybus | 1250 | 48 | 24 |
| karrier-w4 | Karrier W4 trolleybus | 1250 | 48 | 24 |
| karrier-w4s-r | Karrier W4SR trolleybus | 1250 | 48 | 24 |
| karrier-w4s | Karrier W4S trolleybus | 1250 | 48 | 24 |
| DAFXFArtic | DAF XF artic (355 kW) | 400 | 90 | 45 |
| DAFXFArticMail | DAF XF artic (355 kW) | 400 | 90 | 45 |
| LargeArticTrailerBulk | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerCars | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerCool | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerFluid | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerLivestock | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerLong | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerMail | Unpowered trailer | 0 | 86 | 43 |
| LargeArticTrailerPiece | Unpowered trailer | 0 | 86 | 43 |
| LeylandDAF95Artic | Leyland DAF 95 artic (282 kW) | 390 | 88 | 44 |
| LeylandDAF95ArticMail | Leyland DAF 95 artic (282 kW) | 390 | 88 | 44 |
| leyland-atlantean-an68-1-entrance | Leyland Atlantean AN68 | 320 | 75 | 38 |
| leyland-atlantean-an68-2-entrance | Leyland Atlantean AN68 | 320 | 87 | 44 |
| leyland-atlantean-pdr2-1-entrance | Leyland Atlantean PDR2/1 | 310 | 64 | 32 |
| leyland-atlantean-pdr2-2-entrance | Leyland Atlantean PDR2/1 | 310 | 64 | 32 |
| LeylandAtlantean | Leyland Atlantean | 310 | 64 | 32 |
| leyland-atlantean-pdr1-2-entrance | Leyland Atlantean | 295 | 64 | 32 |
| leyland-cheetah-lz2-coach | Leyland Cheetah LZ2 coach | 245 | 75 | 38 |
| leyland-cheetah-lz2 | Leyland Cheetah LZ2 | 250 | 50 | 25 |
| leyland-class-b-bulk | Leyland class B steam wagon (1901) | 3500 | 12 | 6 |
| leyland-class-b-cool | Leyland class B steam wagon (1901) | 3500 | 12 | 6 |
| leyland-class-b-livestock | Leyland class B steam wagon (1901) | 3500 | 12 | 6 |
| leyland-class-b-long | Leyland class B steam wagon (1901) | 3500 | 12 | 6 |
| leyland-class-b-piece | Leyland class B steam wagon (1901) | 3500 | 12 | 6 |
| leyland-class-b-tanker | Leyland class B steam wagon (1901) | 3500 | 12 | 6 |
| leyland-class-f-bulk | Leyland class F steam wagon (1911) | 2800 | 18 | 9 |
| leyland-class-f-cool | Leyland class F steam wagon (1911) | 2800 | 18 | 9 |
| leyland-class-f-livestock | Leyland class F steam wagon (1911) | 2800 | 18 | 9 |
| leyland-class-f-long | Leyland class F steam wagon (1911) | 2800 | 18 | 9 |
| leyland-class-f-piece | Leyland class F steam wagon (1911) | 2800 | 18 | 9 |
| leyland-class-f-tanker | Leyland class F steam wagon (1911) | 2800 | 18 | 9 |
| leyland-class-f2-bulk | Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |
| leyland-class-f2-cool | Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |
| leyland-class-f2-livestock | Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |
| leyland-class-f2-long | Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |
| leyland-class-f2-piece | Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |
| leyland-class-f2-tanker | Leyland class F2 steam wagon (1919) | 2600 | 20 | 10 |
| leyland-class-h-bulk | Leyland class H steam wagon (1905) | 3200 | 12 | 6 |
| leyland-class-h-cool | Leyland class H steam wagon (1905) | 3200 | 12 | 6 |
| leyland-class-h-livestock | Leyland class H steam wagon (1905) | 3200 | 12 | 6 |
| leyland-class-h-long | Leyland class H steam wagon (1905) | 3200 | 12 | 6 |
| leyland-class-h-piece | Leyland class H steam wagon (1905) | 3200 | 12 | 6 |
| leyland-class-h-tanker | Leyland class H steam wagon (1905) | 3200 | 12 | 6 |
| LeylandCometBulk | Leyland Comet | 235 | 61 | 30 |
| LeylandCometCars | Leyland Comet | 235 | 61 | 30 |
| LeylandCometCool | Leyland Comet | 235 | 61 | 30 |
| LeylandCometFluid | Leyland Comet | 235 | 61 | 30 |
| LeylandCometLivestock | Leyland Comet | 235 | 61 | 30 |
| LeylandCometLong | Leyland Comet | 235 | 61 | 30 |
| LeylandCometPiece | Leyland Comet | 235 | 61 | 30 |
| leyland-cub-kpo2 | Leyland Cub KPO2 diesel | 240 | 50 | 25 |
| leyland-cub-kpz1-diesel | Leyland Cub KPZ1 diesel | 240 | 64 | 32 |
| leyland-cub-kpz1 | Leyland Cub KPZ1 petrol | 380 | 64 | 32 |
| leyland-cub | Leyland Cub | 415 | 50 | 25 |
| LeylandDAF200Cool | Leyland DAF 200 van | 110 | 96 | 48 |
| LeylandDAF200Piece | Leyland DAF 200 van | 110 | 96 | 48 |
| LeylandDAF200Post | Leyland DAF 200 van | 110 | 96 | 48 |
| LeylandDAF65Bulk | Leyland DAF 65 | 220 | 100 | 50 |
| LeylandDAF65Cool | Leyland DAF 65 | 220 | 100 | 50 |
| LeylandDAF65Livestock | Leyland DAF 65 | 220 | 100 | 50 |
| LeylandDAF65Long | Leyland DAF 65 | 220 | 100 | 50 |
| LeylandDAF65Piece | Leyland DAF 65 | 220 | 100 | 50 |
| LeylandDAF65Post | Leyland DAF 65 | 220 | 100 | 50 |
| LeylandDAF85RigidBulk | Leyland DAF 85 rigid | 310 | 88 | 44 |
| LeylandDAF85RigidFluid | Leyland DAF 85 rigid | 310 | 88 | 44 |
| LeylandDAF85RigidLong | Leyland DAF 85 rigid | 310 | 88 | 44 |
| LeylandGBulk | Leyland G | 245 | 95 | 48 |
| LeylandGCool | Leyland G | 245 | 95 | 48 |
| LeylandGLivestock | Leyland G | 245 | 95 | 48 |
| LeylandGLong | Leyland G | 245 | 95 | 48 |
| LeylandGPiece | Leyland G | 120 | 95 | 48 |
| LeylandGPost | Leyland G | 245 | 95 | 48 |
| LeylandK2 | Leyland K2 trolleybus | 1300 | 50 | 25 |
| leyland-leopard-l1 | Leyland Leopard L1 | 280 | 64 | 32 |
| leyland-leopard-l2 | Leyland Leopard L2 | 280 | 75 | 38 |
| leyland-leopard-psu3-bus | Leyland Leopard PSU3 bus | 280 | 72 | 36 |
| leyland-leopard-psu3 | Leyland Leopard PSU3 | 280 | 75 | 38 |
| leyland-leopard-psu3a-bus | Leyland Leopard PSU3A bus | 280 | 85 | 42 |
| leyland-leopard-psu3a | Leyland Leopard PSU3A | 280 | 96 | 48 |
| leyland-leopard-psu5 | Leyland Leopard PSU5 | 285 | 96 | 48 |
| leyland-leveret-la | Leyland Leveret LA | 500 | 32 | 16 |
| leyland-lion-lsc1 | Leyland Lion LSC1 | 500 | 32 | 16 |
| leyland-lion-lsc3 | Leyland Lion LSC3 | 480 | 40 | 20 |
| leyland-lion-lt1 | Leyland Lion LT1 | 435 | 50 | 25 |
| leyland-lion-lt5a | Leyland Lion LT5A | 370 | 50 | 25 |
| leyland-lion-lt7 | Leyland Lion LT7 diesel | 250 | 50 | 25 |
| leyland-lioness-lc1 | Leyland Lioness LC1 | 435 | 50 | 25 |
| LeylandLynx | Leyland Lynx | 330 | 75 | 38 |
| leyland-national-2-standee | Leyland National 2 standee | 330 | 75 | 38 |
| leyland-national-2-1-door | Leyland National 2 | 310 | 75 | 38 |
| leyland-national-2-2-door | Leyland National 2 | 310 | 75 | 38 |
| leyland-national-b-1-door | Leyland National B | 310 | 70 | 35 |
| leyland-national-b-2-door | Leyland National B | 310 | 70 | 35 |
| leyland-national-lnc | Leyland National LNC | 300 | 85 | 42 |
| Leyland_National_11(LC) | Leyland National | 300 | 75 | 38 |
| leyland-national-11-lc-2-door | Leyland National | 300 | 75 | 38 |
| LeylandOlympianCoach | Leyland Olympian coach | 330 | 96 | 48 |
| LeylandOlympian | Leyland Olympian | 340 | 70 | 35 |
| LeylandOlympian-1-door | Leyland Olympian | 340 | 70 | 35 |
| leyland-panther-panther-psur1a-1-entrance | Leyland Panther PSUR1A | 300 | 85 | 42 |
| leyland-panther-panther-psur1a-2-entrance | Leyland Panther PSUR1A | 300 | 85 | 42 |
| leyland-panther-panther-psur1-1-entrance | Leyland Panther PSUR1 | 300 | 64 | 32 |
| leyland-panther-panther-psur1-2-entrance | Leyland Panther PSUR1 | 300 | 64 | 32 |
| LeylandRoadrunnerBulk | Leyland Roadrunner | 175 | 100 | 50 |
| LeylandRoadrunnerCool | Leyland Roadrunner | 175 | 100 | 50 |
| LeylandRoadrunnerLivestock | Leyland Roadrunner | 175 | 100 | 50 |
| LeylandRoadrunnerLong | Leyland Roadrunner | 175 | 100 | 50 |
| LeylandRoadrunnerPiece | Leyland Roadrunner | 175 | 100 | 50 |
| LeylandRoadrunnerPost | Leyland Roadrunner | 175 | 100 | 50 |
| leyland-royal-tiger-psu1-11 | Leyland Royal Tiger PSU1/11 | 250 | 90 | 45 |
| leyland-royal-tiger-psu1-9 | Leyland Royal Tiger PSU1/9 | 260 | 55 | 28 |
| LeylandSherpaCool | Leyland Sherpa | 110 | 86 | 43 |
| LeylandSherpaPiece | Leyland Sherpa | 110 | 86 | 43 |
| LeylandSherpaPost | Leyland Sherpa | 110 | 86 | 43 |
| LeylandT45ConstructorBulk | Leyland T45 Constructor | 360 | 86 | 43 |
| LeylandT45ConstructorFluid | Leyland T45 Constructor | 360 | 86 | 43 |
| LeylandT45ConstructorLong | Leyland T45 Constructor | 360 | 86 | 43 |
| leyland-tb2 | Leyland TB2 trolleybus | 1200 | 48 | 24 |
| leyland-tb3 | Leyland TB3 trolleybus | 1200 | 48 | 24 |
| leyland-tb4 | Leyland TB4 trolleybus | 1200 | 48 | 24 |
| leyland-tbd1 | Leyland TBD1 trolleybus | 1150 | 48 | 24 |
| leyland-tiger-cub-psuc1-1 | Leyland Tiger Cub PSUC1/1 | 250 | 55 | 28 |
| leyland-tiger-cub-psuc1-2 | Leyland Tiger Cub PSUC1/2 | 185 | 113 | 56 |
| leyland-tiger-ps1-1 | Leyland Tiger PS1/1 | 270 | 85 | 42 |
| leyland-tiger-ps1 | Leyland Tiger PS1 | 270 | 50 | 25 |
| leyland-tiger-ps2-13 | Leyland Tiger PS2/13 | 260 | 50 | 25 |
| leyland-tiger-ps2-14 | Leyland Tiger PS2/14 | 260 | 90 | 45 |
| leyland-tiger-ps2-5 | Leyland Tiger PS2/5 | 260 | 50 | 25 |
| leyland-tiger-ps2-7 | Leyland Tiger PS2/7 | 260 | 90 | 45 |
| leyland-tiger-tf | Leyland Tiger TF | 270 | 64 | 32 |
| leyland-tiger-tr | Leyland Tiger TR | 350 | 96 | 48 |
| leyland-tiger-ts1-comfort | Leyland Tiger TS1 (comfort) | 400 | 62 | 31 |
| leyland-tiger-ts1-popular | Leyland Tiger TS1 (popular) | 410 | 50 | 25 |
| leyland-tiger-ts4-coach | Leyland Tiger TS4 coach | 380 | 85 | 42 |
| leyland-tiger-ts4 | Leyland Tiger TS4 | 400 | 50 | 25 |
| leyland-tiger-ts6-coach | Leyland Tiger TS6 coach | 380 | 82 | 41 |
| leyland-tiger-ts6 | Leyland Tiger TS6 | 400 | 50 | 25 |
| leyland-tiger-ts6t-coach | Leyland Tiger TS6T coach | 380 | 82 | 41 |
| leyland-tiger-ts6t | Leyland Tiger TS6T | 400 | 50 | 25 |
| leyland-tiger-ts7-coach | Leyland Tiger TS7 coach | 270 | 80 | 40 |
| leyland-tiger-ts7 | Leyland Tiger TS7 | 280 | 50 | 25 |
| leyland-tiger-ts7t-coach | Leyland Tiger TS7T coach | 270 | 80 | 40 |
| leyland-tiger-ts7t | Leyland Tiger TS7T | 280 | 50 | 25 |
| leyland-titan-pd1 | Leyland Titan PD1 | 290 | 50 | 25 |
| leyland-titan-pd2-1 | Leyland Titan PD2/1 | 290 | 50 | 25 |
| leyland-titan-pd2-12 | Leyland Titan PD2/12 | 290 | 50 | 25 |
| leyland-titan-pd2-3 | Leyland Titan PD2/3 | 290 | 50 | 25 |
| leyland-titan-pd2-30 | Leyland Titan PD2/30 | 290 | 50 | 25 |
| leyland-titan-pd3-1 | Leyland Titan PD3/1 | 300 | 55 | 28 |
| leyland-titan-td1 | Leyland Titan TD1 | 420 | 50 | 25 |
| leyland-titan-td2 | Leyland Titan TD2 | 410 | 50 | 25 |
| leyland-titan-td3 | Leyland Titan TD3 | 410 | 50 | 25 |
| leyland-titan-td4 | Leyland Titan TD4 diesel | 280 | 50 | 25 |
| LeylandTitanB15 | Leyland Titan B15 | 380 | 64 | 32 |
| LeylandTitanB15-1-door | Leyland Titan B15 | 380 | 64 | 32 |
| leyland-ttb2 | Leyland TTB2 trolleybus | 1300 | 50 | 25 |
| leyland-ttb3 | Leyland TTB3 trolleybus | 1200 | 48 | 24 |
| leyland-ttbd1 | Leyland TTBD1 trolleybus | 1200 | 48 | 24 |
| LivestockDrover | Horse-drawn or man-powered (no engine) | 0 | 5 | 2 |
| lorry-trailer-5t-bulk | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-5t-cool | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-5t-livestock | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-5t-long | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-5t-piece | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-early-bulk | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-early-cool | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-early-livestock | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-early-long | Unpowered trailer | 0 | 12 | 6 |
| lorry-trailer-early-piece | Unpowered trailer | 0 | 12 | 6 |
| mailcoach-regency | Horse-drawn or man-powered (no engine) | 0 | 18 | 9 |
| MailCoach | Horse-drawn or man-powered (no engine) | 0 | 16 | 8 |
| MailBike | Horse-drawn or man-powered (no engine) | 0 | 20 | 10 |
| MaudslayVanBulk | Maudslay van (1907) | 235 | 30 | 15 |
| MaudslayVanCool | Maudslay van (1907) | 235 | 30 | 15 |
| MaudslayVanLong | Maudslay van (1907) | 235 | 30 | 15 |
| MaudslayVanPiece | Maudslay van (1907) | 235 | 30 | 15 |
| MaudslayVanPost | Maudslay van (1907) | 235 | 30 | 15 |
| mcw-metrorider-long | MCW Metrorider long | 290 | 64 | 32 |
| mcw-metrorider-short | MCW Metrorider short | 290 | 64 | 32 |
| MCWQ1 | MCW Q1 trolleybus (1948) | 1400 | 55 | 28 |
| MercedesCitaroG(Front) | Mercedes Citaro G artic | 430 | 65 | 32 |
| MercedesCitaroG(Rear) | Mercedes Citaro G artic (rear unit, no engine) | 0 | 65 | 32 |
| MercedesCitaroK | Mercedes Citaro K | 340 | 75 | 38 |
| mercedes-citaro | Mercedes Citaro | 360 | 75 | 38 |
| milnes-daimler-double | Milnes-Daimler double-deck | 570 | 20 | 10 |
| milnes-daimler-single-1902 | Milnes-Daimler single-deck (1902) | 515 | 20 | 10 |
| milnes-daimler-single | Milnes-Daimler single-deck | 570 | 20 | 10 |
| MorrisEightCool | Morris Eight van | 100 | 80 | 40 |
| MorrisEightPiece | Morris Eight van | 100 | 80 | 40 |
| MorrisEightPost | Morris Eight van | 100 | 80 | 40 |
| MorrisFGBulk | Morris FG | 120 | 88 | 44 |
| MorrisFGCool | Morris FG | 120 | 88 | 44 |
| MorrisFGLivestock | Morris FG | 120 | 88 | 44 |
| MorrisFGLong | Morris FG | 120 | 88 | 44 |
| MorrisFGPiece | Morris FG | 120 | 88 | 44 |
| MorrisFGPost | Morris FG | 120 | 88 | 44 |
| MorrisJ4Cool | Morris J4 | 130 | 81 | 40 |
| MorrisJ4Piece | Morris J4 | 130 | 81 | 40 |
| MorrisJ4Post | Morris J4 | 130 | 81 | 40 |
| MorrisLDCool | Morris LD | 120 | 77 | 38 |
| MorrisLDPiece | Morris LD | 120 | 77 | 38 |
| MorrisLDPost | Morris LD | 120 | 76 | 38 |
| MorrisMarinaCool | Morris Marina van | 95 | 100 | 50 |
| MorrisMarinaPiece | Morris Marina van | 95 | 100 | 50 |
| MorrisMarinaPost | Morris Marina van | 95 | 100 | 50 |
| MorrisMinorCool | Morris Minor van | 80 | 115 | 58 |
| MorrisMinorPiece | Morris Minor van | 80 | 115 | 58 |
| MorrisMinorPost | Morris Minor van | 80 | 115 | 58 |
| NSTypeDouble | AEC NS-type | 480 | 20 | 10 |
| aec-ns-type-double-covered | AEC NS-type | 480 | 20 | 10 |
| aec-ns-type-double-pneumatic | AEC NS-type | 440 | 32 | 16 |
| OmnibusDoubleGardenseat | Horse-drawn or man-powered (no engine) | 0 | 11 | 6 |
| omnibus-double-knifeboard-later | Horse-drawn or man-powered (no engine) | 0 | 11 | 6 |
| OmnibusDoubleKnifeboard | Horse-drawn or man-powered (no engine) | 0 | 11 | 6 |
| omnibus-single-small | Horse-drawn or man-powered (no engine) | 0 | 11 | 6 |
| OmnibusSingle | Horse-drawn or man-powered (no engine) | 0 | 8 | 4 |
| OptareAlero | Optare Alero | 260 | 75 | 38 |
| optare-delta | Optare Delta | 380 | 64 | 32 |
| optare-excel-2 | Optare Excel 2 | 350 | 77 | 38 |
| OptareExcel | Optare Excel | 350 | 64 | 32 |
| Optare-Metrorider-Long | Optare Metrorider long | 300 | 64 | 32 |
| Optare-Metrorider-Short | Optare Metrorider short | 300 | 64 | 32 |
| optare-solo-ev | Optare Solo EV battery bus | 800 | 70 | 35 |
| optare-solo-sr | Optare Solo SR | 240 | 70 | 35 |
| OptareSolo | Optare Solo | 250 | 70 | 35 |
| OptareTempoSR | Optare Tempo SR | 370 | 74 | 37 |
| OptareTempo | Optare Tempo | 380 | 74 | 37 |
| pack-horse-bulk | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| pack-horse-food | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| pack-horse-liquid | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| pack-horse-long | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| pack-horse-piece | Horse-drawn or man-powered (no engine) | 0 | 7 | 4 |
| ParcelCoach | Horse-drawn or man-powered (no engine) | 0 | 18 | 9 |
| post-boy | Horse-drawn or man-powered (no engine) | 0 | 12 | 6 |
| ret-b10 | RET B10 trolleybus (1920) | 1000 | 32 | 16 |
| ret-f12 | RET F12 trolleybus (1922) | 1200 | 29 | 14 |
| ret-hurst-nelson | RET Hurst Nelson trolleybus (1911) | 1000 | 32 | 16 |
| ret-lf30 | RET LF30 trolleybus (1925) | 1150 | 32 | 16 |
| RFCoach | AEC RF coach | 270 | 64 | 32 |
| RF | AEC RF | 280 | 56 | 28 |
| HeavyRoadLocomotive | Road locomotive / traction engine | 7000 | 20 | 10 |
| LightRoadLocomotive | Road locomotive / traction engine | 6260 | 15 | 8 |
| aec-rmc | Routemaster coach | 265 | 90 | 45 |
| RoutemasterLongCoach | Routemaster long coach | 265 | 90 | 45 |
| RoutemasterLong | Routemaster long | 320 | 73 | 36 |
| RoutemasterTrolleybus | Routemaster trolleybus conversion (1966) | 1750 | 50 | 25 |
| Routemaster | Routemaster | 320 | 73 | 36 |
| STypeDouble | AEC S-type double-deck | 500 | 20 | 10 |
| STypeSingle | AEC S-type single-deck | 500 | 20 | 10 |
| Scammell1955TrailerBulk | Unpowered trailer | 0 | 79 | 40 |
| Scammell1955TrailerCars | Unpowered trailer | 0 | 79 | 40 |
| Scammell1955TrailerCool | Unpowered trailer | 0 | 79 | 40 |
| Scammell1955TrailerFluid | Unpowered trailer | 0 | 79 | 40 |
| Scammell1955TrailerLivestock | Unpowered trailer | 0 | 79 | 40 |
| Scammell1955TrailerLong | Unpowered trailer | 0 | 79 | 40 |
| Scammell1955TrailerPiece | Unpowered trailer | 0 | 79 | 40 |
| ScammellHandyman | Scammell Handyman/Highwayman | 350 | 79 | 40 |
| ScammellHighwayman | Scammell Handyman/Highwayman | 320 | 68 | 34 |
| ScammellCrusader | Scammell Crusader | 400 | 84 | 42 |
| ScammellCrusaderTrailerBulk | Unpowered trailer | 0 | 84 | 42 |
| ScammellCrusaderTrailerCars | Unpowered trailer | 0 | 84 | 42 |
| ScammellCrusaderTrailerCool | Unpowered trailer | 0 | 84 | 42 |
| ScammellCrusaderTrailerFluid | Unpowered trailer | 0 | 84 | 42 |
| ScammellCrusaderTrailerLivestock | Unpowered trailer | 0 | 84 | 42 |
| ScammellCrusaderTrailerLong | Unpowered trailer | 0 | 84 | 42 |
| ScammellCrusaderTrailerPiece | Unpowered trailer | 0 | 84 | 42 |
| ScammellMechHorseTrailerCool | Unpowered trailer | 0 | 80 | 40 |
| ScammellMechHorseTrailerLivestock | Unpowered trailer | 0 | 80 | 40 |
| ScammellMechHorseTrailerLong | Unpowered trailer | 0 | 80 | 40 |
| ScammellMechHorseTrailerMail | Unpowered trailer | 0 | 80 | 40 |
| ScammellMechHorseTrailerPiece | Unpowered trailer | 0 | 80 | 40 |
| ScammellMechanicalHorse | Scammell Mechanical Horse (petrol) | 250 | 32 | 16 |
| ScammellScarab | Scammell Scarab (petrol) | 240 | 50 | 25 |
| ScammellTownsman | Scammell Townsman (diesel) | 200 | 80 | 40 |
| ScammellRoutemanBulk | Scammell Routeman | 280 | 79 | 40 |
| ScammellRoutemanCool | Scammell Routeman | 280 | 79 | 40 |
| ScammellRoutemanFluid | Scammell Routeman | 280 | 79 | 40 |
| ScammellRoutemanLivestock | Scammell Routeman | 280 | 79 | 40 |
| ScammellRoutemanLong | Scammell Routeman | 280 | 79 | 40 |
| ScammellRoutemanPiece | Scammell Routeman | 280 | 79 | 40 |
| sentinel-dg4-pneumatic-bulk | Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg4-pneumatic-cool | Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg4-pneumatic-livestock | Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg4-pneumatic-long | Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg4-pneumatic-piece | Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg4-pneumatic-tanker | Sentinel DG4 (pneumatic tyres) | 2400 | 50 | 25 |
| SentinelDGBulk | Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |
| SentinelDGCool | Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |
| SentinelDGLivestock | Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |
| SentinelDGLong | Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |
| SentinelDGPiece | Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |
| SentinelDGTanker | Sentinel DG4 (solid tyres) | 1450 | 20 | 10 |
| sentinel-dg6-pneumatic-bulk | Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg6-pneumatic-cool | Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg6-pneumatic-livestock | Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg6-pneumatic-long | Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg6-pneumatic-piece | Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg6-pneumatic-tanker | Sentinel DG6 (pneumatic tyres) | 2400 | 50 | 25 |
| sentinel-dg6-bulk | Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |
| sentinel-dg6-cool | Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |
| sentinel-dg6-livestock | Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |
| sentinel-dg6-long | Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |
| sentinel-dg6-piece | Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |
| sentinel-dg6-tanker | Sentinel DG6 (solid tyres) | 1450 | 20 | 10 |
| SentinelSBulk | Sentinel S4 | 1500 | 65 | 32 |
| SentinelSCool | Sentinel S4 | 1500 | 65 | 32 |
| SentinelSLivestock | Sentinel S4 | 1500 | 65 | 32 |
| SentinelSLong | Sentinel S4 | 1500 | 65 | 32 |
| SentinelSPiece | Sentinel S4 | 1500 | 65 | 32 |
| SentinelSTanker | Sentinel S4 | 1500 | 65 | 32 |
| sentinel-s6-bulk | Sentinel S6 | 1600 | 65 | 32 |
| sentinel-s6-cool | Sentinel S6 | 1600 | 65 | 32 |
| sentinel-s6-livestock | Sentinel S6 | 1600 | 65 | 32 |
| sentinel-s6-long | Sentinel S6 | 1600 | 65 | 32 |
| sentinel-s6-piece | Sentinel S6 | 1600 | 65 | 32 |
| sentinel-s6-tanker | Sentinel S6 | 1600 | 65 | 32 |
| sentinel-standard-6t-bulk | Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |
| sentinel-standard-6t-cool | Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |
| sentinel-standard-6t-livestock | Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |
| sentinel-standard-6t-long | Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |
| sentinel-standard-6t-piece | Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |
| sentinel-standard-6t-tanker | Sentinel standard 6-ton (1906) | 3300 | 18 | 9 |
| SentinelStandardBulk | Sentinel standard (1906) | 3300 | 18 | 9 |
| SentinelStandardCool | Sentinel standard (1906) | 3300 | 18 | 9 |
| SentinelStandardLivestock | Sentinel standard (1906) | 3300 | 18 | 9 |
| SentinelStandardLong | Sentinel standard (1906) | 3300 | 18 | 9 |
| SentinelStandardPiece | Sentinel standard (1906) | 3300 | 18 | 9 |
| SentinelStandardTanker | Sentinel standard (1906) | 3300 | 18 | 9 |
| short-stagecoach | Horse-drawn or man-powered (no engine) | 0 | 12 | 6 |
| StageWagonCool | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| StageWagonMail | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| StageWagonPiece | Horse-drawn or man-powered (no engine) | 0 | 10 | 5 |
| stagecoach-besant | Horse-drawn or man-powered (no engine) | 0 | 16 | 8 |
| stagecoach-georgian | Horse-drawn or man-powered (no engine) | 0 | 15 | 8 |
| stagecoach-regency | Horse-drawn or man-powered (no engine) | 0 | 18 | 9 |
| StageCoach | Horse-drawn or man-powered (no engine) | 0 | 12 | 6 |
| DAFCFArtic | DAF CF artic (265 kW) | 380 | 90 | 45 |
| DAFCFArticMail | DAF CF artic (265 kW) | 380 | 90 | 45 |
| LeylandDAF85Artic | Leyland DAF 85 artic (279 kW) | 390 | 88 | 44 |
| LeylandDAF85ArticMail | Leyland DAF 85 artic (279 kW) | 390 | 88 | 44 |
| LeylandT45Roadtrain | Leyland T45 Roadtrain (173 kW) | 360 | 86 | 43 |
| LeylandT45RoadtrainMail | Leyland T45 Roadtrain (173 kW) | 360 | 86 | 43 |
| StandardArticTrailerBulk | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerCars | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerCool | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerFluid | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerLivestock | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerLong | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerMail | Unpowered trailer | 0 | 86 | 43 |
| StandardArticTrailerPiece | Unpowered trailer | 0 | 86 | 43 |
| straker-ll | Straker LL trolleybus | 1100 | 40 | 20 |
| straker-squire-a-type-double | Straker-Squire A-type double-deck trolleybus | 1100 | 30 | 15 |
| straker-squire-trolleybus-pneumatic | Straker-Squire trolleybus (pneumatic) | 1000 | 38 | 19 |
| straker-squire-trolleybus | Straker-Squire trolleybus | 1000 | 35 | 18 |
| sunbeam-f4 | Sunbeam F4 trolleybus | 1450 | 55 | 28 |
| sunbeam-f4a | Sunbeam F4A trolleybus | 1550 | 55 | 28 |
| sunbeam-f4s | Sunbeam F4S trolleybus | 1450 | 55 | 28 |
| sunbeam-s7 | Sunbeam S7 trolleybus | 1500 | 55 | 28 |
| super-sentinel-pneumatic-bulk | Super-Sentinel (pneumatic) | 2250 | 32 | 16 |
| super-sentinel-pneumatic-cool | Super-Sentinel (pneumatic) | 2250 | 32 | 16 |
| super-sentinel-pneumatic-livestock | Super-Sentinel (pneumatic) | 2250 | 32 | 16 |
| super-sentinel-pneumatic-long | Super-Sentinel (pneumatic) | 2250 | 32 | 16 |
| super-sentinel-pneumatic-piece | Super-Sentinel (pneumatic) | 2250 | 32 | 16 |
| super-sentinel-pneumatic-tanker | Super-Sentinel (pneumatic) | 2250 | 32 | 16 |
| super-sentinel-bulk | Super-Sentinel (1923) | 1600 | 20 | 10 |
| super-sentinel-cool | Super-Sentinel (1923) | 1600 | 20 | 10 |
| super-sentinel-livestock | Super-Sentinel (1923) | 1600 | 20 | 10 |
| super-sentinel-long | Super-Sentinel (1923) | 1600 | 20 | 10 |
| super-sentinel-piece | Super-Sentinel (1923) | 1600 | 20 | 10 |
| super-sentinel-tanker | Super-Sentinel (1923) | 1600 | 20 | 10 |
| ThornycroftAmazonBulk | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonCars | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonCool | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonFluid | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonLivestock | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonLong | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonPiece | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftAmazonTractor | Thornycroft Amazon tractor | 380 | 50 | 25 |
| ThornycroftBTBulk | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftBTCars | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftBTCool | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftBTLivestock | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftBTLong | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftBTPiece | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftBTPost | Thornycroft BT lorry (1913) | 190 | 34 | 17 |
| ThornycroftQArticBulk | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticCars | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticCool | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticFluid | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticLivestock | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticLong | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticPiece | Unpowered trailer | 0 | 50 | 25 |
| ThornycroftQArticTractor | Thornycroft Q artic tractor | 300 | 34 | 17 |
| ThornycroftQRigidBulk | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQRigidCars | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQRigidCool | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQRigidLivestock | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQRigidLong | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQRigidOil | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQRigidPiece | Thornycroft Q rigid | 300 | 34 | 17 |
| ThornycroftQCBulk | Thornycroft QC | 380 | 47 | 24 |
| ThornycroftQCCars | Thornycroft QC | 380 | 47 | 24 |
| ThornycroftQCCool | Thornycroft QC | 380 | 47 | 24 |
| ThornycroftQCFluid | Thornycroft QC | 380 | 47 | 24 |
| ThornycroftQCLivestock | Thornycroft QC | 380 | 39 | 20 |
| ThornycroftQCLong | Thornycroft QC | 380 | 47 | 24 |
| ThornycroftQCPiece | Thornycroft QC | 380 | 47 | 24 |
| ThornycroftStagBulk | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftStagCars | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftStagCool | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftStagFluid | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftStagLivestock | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftStagLong | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftStagPiece | Thornycroft Stag | 360 | 56 | 28 |
| ThornycroftSteamVanCool | Thornycroft steam van (1896) | 900 | 16 | 8 |
| ThornycroftSteamVanMail | Thornycroft steam van (1896) | 900 | 16 | 8 |
| ThornycroftSteamVanPiece | Thornycroft steam van (1896) | 900 | 16 | 8 |
| ThornycroftWagonBulk | Thornycroft steam wagon (1900) | 3000 | 12 | 6 |
| ThornycroftWagonCool | Thornycroft steam wagon (1900) | 3000 | 12 | 6 |
| ThornycroftWagonLivestock | Thornycroft steam wagon (1900) | 3000 | 12 | 6 |
| ThornycroftWagonLong | Thornycroft steam wagon (1900) | 3000 | 12 | 6 |
| ThornycroftWagonPiece | Thornycroft steam wagon (1900) | 3000 | 12 | 6 |
| tilling-stevens-ts3-single | Tilling-Stevens TS3 single-deck | 430 | 20 | 10 |
| tilling-stevens-ts3 | Tilling-Stevens TS3 | 430 | 20 | 10 |
| tilling-stevens-ts3a | Tilling-Stevens TS3A | 420 | 20 | 10 |
| tilling-stevens-ts7-double-pneumatic | Tilling-Stevens TS7 double-deck (pneumatic) | 420 | 32 | 16 |
| tilling-stevens-ts7-double | Tilling-Stevens TS7 double-deck | 420 | 20 | 10 |
| tilling-stevens-ts7-single-pneumatic | Tilling-Stevens TS7 single-deck (pneumatic) | 420 | 32 | 16 |
| tilling-stevens-ts7-single | Tilling-Stevens TS7 single-deck | 420 | 20 | 10 |
| tilling-stevens-tta1-single | Tilling-Stevens TTA1 single-deck | 450 | 20 | 10 |
| tilling-stevens-tta1 | Tilling-Stevens TTA1 petrol-electric | 450 | 20 | 10 |
| tilling-stevens-tta2 | Tilling-Stevens TTA2 | 430 | 20 | 10 |
| volvo-alisa-1-door | Volvo Alisa | 340 | 70 | 35 |
| volvo-alisa-2-door | Volvo Alisa | 340 | 70 | 35 |
| volvo-b10m-coach | Volvo B10M coach | 300 | 96 | 48 |
| volvo-b12m-coach | Volvo B12M coach | 320 | 96 | 48 |
| VolvoB7TL | Volvo B7TL | 400 | 72 | 36 |
| VolvoB7TL-1-door | Volvo B7TL | 400 | 72 | 36 |
| VolvoCitybus | Volvo Citybus | 380 | 70 | 35 |
| VolvoCitybus-1-door | Volvo Citybus | 380 | 70 | 35 |
| VolvoOlympian | Volvo Olympian | 360 | 64 | 32 |
| VolvoOlympian-1-door | Volvo Olympian | 360 | 64 | 32 |
| WagonBulk | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| WagonCool | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| WagonLong | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| WagonPiece | Horse-drawn or man-powered (no engine) | 0 | 6 | 3 |
| WrightElectrocity | Wright Electrocity | 340 | 70 | 35 |
| WrightStreetcar(Front) | Wright Streetcar | 450 | 84 | 42 |
| WrightStreetcar(Rear) | Wright Streetcar (rear unit, no engine) | 0 | 84 | 42 |
| lgoc-x-type-double | LGOC X-type double-deck | 515 | 20 | 10 |
| yorkshire-steam-wagon-wh-bulk | Yorkshire steam wagon WH | 1400 | 55 | 28 |
| yorkshire-steam-wagon-wh-cool | Yorkshire steam wagon WH | 1400 | 55 | 28 |
| yorkshire-steam-wagon-wh-livestock | Yorkshire steam wagon WH | 1400 | 55 | 28 |
| yorkshire-steam-wagon-wh-long | Yorkshire steam wagon WH | 1400 | 55 | 28 |
| yorkshire-steam-wagon-wh-piece | Yorkshire steam wagon WH | 1400 | 55 | 28 |
| yorkshire-steam-wagon-wh-tanker | Yorkshire steam wagon WH | 1400 | 55 | 28 |

## 4. Gaps and doubts

- **Most petrol and diesel vans and light lorries are EST.** No measured mpg was found for the Morris J4/LD/FG, Sherpa, Transit Connect, Escort/Maestro/Marina vans or the 1900s Maudslay and Dennis light commercials. They are anchored on the 1925 Morris RAC trials (S11) and on the class figures for the nearest lorry, scaled by power. A period road test for each would improve them by perhaps 10-15%.
- **Early petrol buses (1900-1914) rest on one qualitative record** (6 mpg, S9) and one curator's recollection (4 mpg, S5). The B-type, Milnes-Daimler and Daimler CC figures are interpolations between those two. The full-output cap in 1.4 also binds on several 1920s buses: a 26-36 kW bus with a 45-50 km/h top speed cannot physically use more than about 300-370 mL/km at that speed, however thirsty it is at 20 km/h, so those rows sit at the physical ceiling rather than at a measured service figure.
- **Steam wagons are the weakest group after the vans.** Only Sentinel (DG4/DG6/S4/S6), Super-Sentinel and Foden have measured coal rates; Leyland, Yorkshire, Thornycroft and the road locomotives are scaled from those by power. The 0.7 speed exponent is a judgement, not a measurement, and it moves the pneumatic-tyred Sentinels by a factor of 1.6 relative to the solid-tyred ones.
- **The calibration-speed convention distorts slow and fast variants of one engine.** For liquid fuels and electricity the per-km service figure is used unchanged, so a governed 50 km/h bus and its 75 km/h sister get the same number and the engine charges the slow one less per hour. For steam the speed conversion in 1.4 is applied. If the orchestrator prefers a single convention, the steam figures are the ones to revisit.
- **Trolleybus energy is measured at the substation**, so it includes feeder and overhead losses of perhaps 10%; energy at the pantograph would be about 10% lower. The 1966 Routemaster conversion is a fictional vehicle and is given 1750 Wh/km by analogy with the largest 1930s cars; the 1979 figure of 2.5 kWh/km with thyristor control (S33) is the modern end of the range and nothing in the pakset is that late.
- **Ranges are untouched.** Only the objects that already had a `range` in the `.dat` show one in the table; no new range values were proposed.
- **Not checked:** whether the engine's `is_at_full_power()` treats a road convoy's speed limit (rather than the vehicle's own maximum) as `vmax`. If it does, a bus running in a 30 km/h zone is charged 40% of the figure in this table, which would understate town consumption. That is an engine question, not a data one.
