---
status: draft
verified: New ex-15 working tree @ 6d28e20d5
---
# Fuel consumption: diesel and electric rail

**Covers**: the `fuel_per_km` and `calibration_speed` values of every rail-guided vehicle that is not
steam — locomotives, multiple units and their motor cars, trams, London Underground stock, narrow-gauge
diesel and the maglev. Engine semantics and the unit convention: [fuel-consumption](../fuel-consumption.md).
Steam locomotives are in [steam](steam.md).

`fuel_per_km` is millilitres of diesel per kilometre for `diesel`, `petrol` and `bio`; watt-hours per
kilometre drawn from the line for `electric`, and from the tank or battery for `battery`,
`fuel_cell` and `hydrogene`. `calibration_speed` is the vehicle's own maximum speed. Trailer cars and
unpowered vehicles carry no figure.

## Method

Every figure is derived from the object's own `power` and top speed:

- **Diesel, petrol and bio**: `fuel per km = power × brake-specific fuel consumption ÷ 835 g/L ÷ speed`.
  Brake-specific consumption is 228 g/kWh for the EE 12CSVT, substantiated by a Sulzer 12LDA28 type
  test, 210 g/kWh from a 1987 British Rail engine survey and 195 g/kWh for the Mirrlees MB275; the
  remaining ratings are estimates between 200 and 235 g/kWh. `[LITERATURE:Modern Railways, 2019]`
- **Electric**: `watt-hours per km = power × 1000 ÷ line-to-rail efficiency ÷ speed`. The efficiency
  of 0.76 is measured for the Class 390, whose traction equipment draws 6.7 MW at the overhead line
  for 5.1 MW at the rail; `[LITERATURE:RSSB T618]` every other efficiency in the sequence is an
  estimate.
- **Hydrogen maglev**: the same as electric, from the fuel-cell power.

That model produces the **full-output** rate at line speed. The engine charges `fuel_per_km` per
kilometre at part load, so the figure has to be the average over a journey, not the full-output rate.
Measured fleet consumption from RSSB T618 supplies the correction:

| unit | computed at full output | measured | computed ÷ measured |
|---|---:|---:|---:|
| Class 170, 3-car | 1,414 mL/km | 1,362 | 1.04 |
| HST, 2+8 | 4,320 mL/km | 4,210 | 1.03 |
| Class 222, 9-car | 4,024 mL/km | 4,684 | 0.86 |
| Class 180, 5-car | 3,353 mL/km | 2,626 | 1.28 |
| Class 220, 4-car | 2,683 mL/km | 2,256 | 1.19 |
| Class 357, 4-car | 14,205 Wh/km | 9,440 | 1.50 |
| Class 91 + Mk4 | 27,485 Wh/km | 16,610 | 1.65 |
| Class 390, 9-car | 29,982 Wh/km | 16,650 in service | 1.80 |

Diesel therefore needs little correction and electric a large one: a diesel unit's engines work near
rated output at line speed, while an electric unit's installed power is used only while accelerating.
The applied correction is **0.85 for diesel, petrol and bio**, and **0.60 for electric traction on
`waytype=track`**. Trams are left uncorrected, because their installed power is matched to a
stop-start duty: the one measured tramcar, the Blackpool Centenary, computes at 1,430 Wh/km against
1,500 measured, and applying 0.60 to it would understate by 43 per cent.

Two independent checks from the Simutrans forum agree with the diesel figures before correction: a
102 hp Gardner railcar returning 12 mpg at 45 mph is 235 mL/km against 272 computed, and the
late-1950s railbuses at 9 mpg are 314 mL/km against 326.
`[FORUM:https://forum.simutrans.com/index.php?topic=6521.35]`
`[FORUM:https://forum.simutrans.com/index.php?topic=6521.280]`

The full per-object derivation, one row per traction rating: [rail-derivation](rail-derivation.md).

## Result

Applied figures: Class 47 2,916 mL/km at 153 km/h, Class 55 (Deltic) 3,568 mL/km at 160 km/h, Class
91 16,069 Wh/km at 225 km/h, Class 390 3,000 Wh/km per motor car at 225 km/h, Blackpool Centenary
tram 1,429 Wh/km at 70 km/h.

595 objects carry a figure; 1,476 are zero. Of the zero objects, 1,170 declare no `engine_type` at
all — carriages, wagons and trailer cars — and 291 declare an engine but have `power=0`, which is how
this pakset marks a non-motorised car of a multiple unit. The remaining 15 are horse-drawn.

## Gaps and doubts

- **Hydrogen is not priced.** `fuel[hydrogene]` is commented out in `config/fuel.tab`, so the 22
  maglev objects will be charged nothing whatever figure they carry. Either uncomment the series or
  accept that hydrogen maglev is free to run.
- **Power figures that are wrong** were left alone and flagged: the Class 357 and the London
  Underground 1995 and 2009 stocks are overstated, and the Sheffield Supertram middle car carries
  554 kW where its siblings have far less, which makes the articulated tram figure three times the
  measured value.
- **No measured gallons-per-mile record** was found for any diesel locomotive class, so the diesel
  figures rest on the parameter chain rather than on class records.
- No measured energy data exists for electric stock before 1990.
- The 0.60 and 0.85 corrections are the largest uncertainty in this sector. They are single numbers
  standing for a duty cycle that differs between a metro and an express.

## Open questions

- Should a hydrogen price be added to `config/fuel.tab`? The series is present but commented out, and
  it copies the electricity series, which is the wrong basis for hydrogen bought as a fuel.
- Should the electric correction be varied by class rather than by traction type, now that the
  measured ratios range from 0.91 to 1.80?
