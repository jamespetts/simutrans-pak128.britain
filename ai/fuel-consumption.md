---
status: draft
verified: New ex-15 working tree @ 6d28e20d5
---
# Fuel consumption

**Covers**: the per-vehicle `.dat` fields that make the engine charge fuel — `fuel_per_km`,
`calibration_speed`, `cut_off_speed` and `range` — and the `config/fuel.tab` unit convention they
depend on. The researched figures per sector are in the child documents.

Read before setting or checking any vehicle's fuel consumption, and before changing `config/fuel.tab`.

## Documents

| Document | Read when | Contents |
|---|---|---|
| [fuel/steam](fuel/steam.md) | setting or checking a steam locomotive, steam tram, narrow-gauge steam engine, steam ship or steam wagon | the sheet the figures come from, the coal types, the calibration decision, and the range analysis |
| [fuel/road](fuel/road.md) | setting or checking a bus, coach, lorry, van, steam wagon, trolleybus or horse-drawn vehicle | mpg and pounds-per-mile evidence from the forum thread and the *Commercial Motor* archive |
| [fuel/rail](fuel/rail.md) | setting or checking a diesel or electric locomotive, multiple unit, tram, tube train or maglev | the brake-specific-consumption and traction-energy derivation, and the service-duty correction |
| [fuel/water](fuel/water.md) | setting or checking a ship, barge, ferry or hovercraft | coal per indicated horsepower-hour and marine diesel consumption, and the engine-type corrections made |
| [fuel/air](fuel/air.md) | setting or checking an aircraft or airship | cruise fuel flow from documented sector burns and from engine specific consumption |
| [fuel-evidence](fuel-evidence.md) | you need the published price of a fuel | the coal, oil, petrol, electricity and aviation series behind `fuel.tab` |
| [conversion-chains](conversion-chains.md) | converting a fuel figure to pounds | the canonical conversion table |

## The fields

All four are optional and default to 0. `[CODE simutrans-extended ex-15]`

- `fuel_per_km` — fuel consumed per kilometre, in thousandths of the fuel's unit. With 0, the
  vehicle is charged no fuel at all; this is the correct value for unpowered vehicles (carriages,
  wagons, unpowered trailer cars, holds) and for sail, which `fuel.tab` prices at 0 anyway.
  The field is a 32-bit unsigned integer.
- `calibration_speed` — the speed in km/h at which `fuel_per_km` was measured. **A `fuel_per_km`
  with `calibration_speed` left at 0 charges nothing**, because the speed multiplier becomes 0.
- `cut_off_speed` — the speed below which the part-load reduction stops reducing consumption. It
  only matters when `calibration_speed` is below the vehicle's maximum speed; see the design rule
  below.
- `range` — the maximum distance in kilometres to the next scheduled stop, counted from the
  vehicle's last stop. 0 means no limit. The convoy takes the smallest nonzero value among its
  vehicles. The engine has a `vehicle_t::replenish()` method and a `replenishment_seconds` field,
  but nothing in this source tree calls `replenish()`, so a range is never restored: a `range` is a
  permanent cap on how far a convoy may run between stops. Aircraft, ships and a few road vehicles
  already carry ranges.

## What the engine does with them

`vehicle_t::calc_fuel_consumption` in `vehicle/vehicle.cc` runs as the vehicle moves.
`[CODE simutrans-extended ex-15]`

- At maximum output — accelerating, or held at the maximum physical speed the convoy can reach with
  its present load — fuel per km is `fuel_per_km × calibration_speed ÷ actual speed`.
- Otherwise — cruising at a speed the convoy can hold at part throttle — fuel per km is
  `fuel_per_km × calibration_speed ÷ maximum physical speed`, with the actual speed floored at
  `cut_off_speed` before the division.
- Fuel is booked only while the convoy is moving, and is charged as
  `fuel_cost_per_unit × fuel_used ÷ 1000` Simucents, where the 1000 is `fuel_unit_cost_divider` in
  `New/config/simuconf.tab`. `[CODE New ex-15 working tree @ 6d28e20d5]`

The quantity that does not depend on the choice of calibration speed is their product:
`fuel_per_km × calibration_speed` is the fuel burned per hour at maximum output. Splitting it
differently changes the per-kilometre charge, not the hourly rate.

## The design rule

**Set `calibration_speed` to the vehicle's maximum speed.** Then the part-load branch charges
exactly `fuel_per_km` per kilometre at every speed up to the maximum, and the full-power branch
charges more in proportion to how far below the maximum speed the convoy is struggling. The result
is a flat per-kilometre charge at cruise plus a penalty for hard work, which is the shape the
underlying evidence supports: the researched figure is the fuel a vehicle burns per kilometre in
ordinary service, not per hour.

With this rule `cut_off_speed` has no effect and should be left at 0. It matters only for a vehicle
whose calibration speed is below its maximum speed, which this pakset no longer does.

## Units

`config/fuel.tab` stores, per traction type, one `year,value` series. The engine takes the value for
the current year with **no inflation index**, so the series are nominal prices.

The pakset's convention, now verified, is that a stored value is **192 × the price in decimal pence
per unit of fuel**, so that one stored unit is one Simucent (£0.00005208 on the revenue timescale).
Applied to the diesel series it reproduces £0.825 a litre in 2000 and £1.65 a litre in 2026; applied
to the coal series it reproduces about 10s 6d a ton in 1900 and about £2.50 a ton in 1950, both of
which match the published series. The ÷1000 divider therefore makes `fuel_per_km`:

| Traction | `fuel.tab` prices | `fuel_per_km` unit | example |
|---|---|---|---|
| steam | per kilogramme of coal | grammes per km | Black 5 at 12.65 kg/km → 12650 |
| diesel, petrol, turbine | per litre | millilitres per km | bus at 30 L/100 km → 300 |
| electric, battery, fuel cell, hydrogene | per kilowatt hour | watt-hours per km | EMU at 20 kWh/km → 20000 |

`[CODE New ex-15 working tree @ 6d28e20d5]`

**Check every figure against its neighbour.** Cost per kilometre in Simucents is
`fuel_per_km × fuel.tab value ÷ 1000`. Fuel and `runningcost` — which is maintenance only, per the
engine's own comment on the field — should normally be within a factor of about three of each
other. A figure thirty times its neighbourhood is a unit error.

## Coverage

1,924 powered objects carry a figure. `[CODE New ex-15 working tree @ 6d28e20d5]`

| Sector | Objects with a figure | Deliberately zero |
|---|---:|---:|
| Rail, narrow gauge and trams, steam | 390 | 52 unpowered parts and tenders |
| Road | 587 | 117: 94 unpowered, 21 horse-drawn, 1 hold |
| Water | 122 | 219 holds, sail and unpowered craft |
| Air | 230 | 0 |
| Rail, diesel and electric | 595 | 1,476 unpowered or non-motorised |

What is not done:

- `fuel[hydrogene]` is commented out in `config/fuel.tab`, so the 22 hydrogen maglev vehicles carry a
  figure that is never charged.
- The fuel price series has defects recorded in [fuel-evidence](fuel-evidence.md); the steam series'
  1968 point is about half what it should be.
- `range` is not set on steam locomotives. The analysis and the numbers are in [fuel/steam](fuel/steam.md#range).
- Marine bunker fuel has no price series of its own; ships buy road diesel.

## Open questions

- The engine charges fuel and maintenance as separate money categories but reports both under
  `CONVOI_OPERATIONS`; whether the finance window should show fuel separately is a code question,
  not a pakset one.
- No pakset or engine display yet shows a vehicle's fuel consumption, so a wrong figure is invisible
  to the player until it reaches the accounts.
