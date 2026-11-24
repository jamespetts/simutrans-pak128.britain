---
status: draft
verified: New ex-15 working tree @ 6d28e20d5
---
# Fuel consumption: road vehicles

**Covers**: the `fuel_per_km` values of the 704 road vehicles in `New/bus/` — buses, coaches, lorries,
vans, steam wagons, traction engines, trolleybuses and horse-drawn vehicles. Engine semantics and the
unit convention: [fuel-consumption](../fuel-consumption.md).

`fuel_per_km` is millilitres per kilometre for petrol, diesel and bio; grammes of coal per kilometre
for steam; watt-hours per kilometre for trolleybuses and the one battery bus. `calibration_speed` is
the object's own maximum speed. Horse-drawn vehicles, trailers and unpowered half-units carry no
figure.

## Method

All road fuel economy is quoted per distance, so the conversions are direct:

- `mL/km = 2824.81 ÷ mpg` (UK gallons, statute miles); litres per 100 km becomes mL/km by ×10.
- `g/km of coal = 281.85 × lb per mile`.
- `Wh/km = 621.4 × kWh per car-mile`.

The evidence comes first from the Simutrans forum thread *A snippet of relative pricing information*,
which holds the bus figures the exercise was expected to find, and then from the *Commercial Motor*
archive, whose road tests from 1907 to 1968 report measured fuel consumption for the exact vehicle
classes in the pakset. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.0]`
`[LITERATURE:https://archive.commercialmotor.com/]`

The forum supplies:

| Key | Figure |
|---|---|
| S1 | Sentinel steam bus, 110 lb of coal per 10 miles |
| S2 | Sentinel steam wagon, 4 kg/km maximum and 3.2 kg/km on a 62 km laden run |
| S3 | Two-ton lorry 15-16 mpg laden; Leyland Lancet 11 mpg, Lancet II 17 mpg |
| S5 | Routemaster-era buses 8-10 mpg, modern buses 6-7 mpg, old petrol buses about 4 mpg |
| S6 | Daimler COG5 32-seat single-decker 11.79-12.55 mpg on local services |
| S7 | Leyland Titan PD2/20, 9.75 mpg in daily service in the late 1950s |
| S8 | Trolleybus, 1.25 kWh per car-mile |

The *Commercial Motor* supplies the measured steam-wagon rates in pounds of coal per mile, the
1925 Morris RAC-observed trials for light commercial vehicles, and the 1930s oil-engined bus records.

The full per-model table with a source key on every row, and the per-object mapping:
[road-derivation](road-derivation.md).

Where a model has no measurement, the figure is scaled from the nearest documented vehicle of the
same class and era by the square root of the power ratio, and then capped at the flow the engine
could physically deliver at full output from the brake-specific consumption of its era. The cap bites
only on objects whose top speed is implausibly high for their engine.

Steam needed one further conversion: a steam wagon's coal per mile was measured at a known test
speed, and the flow rises with speed sub-proportionally. It is converted to the pakset calibration
speed with an exponent of 0.7. This is the weakest step in the sector and it is why the solid-tyred
and pneumatic-tyred Sentinel variants differ by a factor of 1.6: they are the same boiler at 20 and
50 km/h.

## Result

| Traction | Objects | Range of `fuel_per_km` | Typical |
|---|---:|---|---:|
| petrol | 172 | 70-600 mL/km | 319 |
| diesel | 246 | 70-450 mL/km | 273 |
| steam | 106 | 900-7000 g/km | 2411 |
| electric | 64 | 950-1750 Wh/km | 1229 |
| battery | 1 | 800 Wh/km | 800 |

Named objects: Routemaster 320 mL/km at 73 km/h, Routemaster trolleybus 1750 Wh/km at 50 km/h, Foden
compound steam wagon 2700 g/km at 20 km/h, Sentinel S4 1500 g/km at 65 km/h, a 1931 trolleybus
1000 Wh/km at 48 km/h.

117 objects are zero: 94 with no engine type, 21 bio (horses, whose fodder is in `fixed_cost` by the
convention stated in `config/fuel.tab`), and the `mail-boot` road hold.

## Gaps and doubts

- Light vans and petrol commercials of the 1900s rest on the 1925 Morris trials; only Sentinel and
  Foden steam wagons have measured coal rates, and the Leyland, Yorkshire and Thornycroft wagons and
  the traction engines are power-scaled from those.
- Early petrol buses rest on one 1907 record of about 6 mpg and one curator's figure of 4 mpg.
- The 0.7 speed exponent for steam is a judgement, not a measurement.
- The pakset's road `runningcost` values are not consistent with the fuel figures for the smallest
  vehicles; as with aircraft, that is a maintenance-cost problem rather than a fuel one.

## Open questions

- Should the steam-wagon figures be given at the measured test speed instead of being scaled to the
  pakset top speed? The choice changes them by up to 60 per cent.
