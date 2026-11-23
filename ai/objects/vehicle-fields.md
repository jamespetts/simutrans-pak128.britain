---
status: draft
verified: New master @ fc87c0424
---
# Vehicle fields

**Covers**: what every `Obj=vehicle` `.dat` field does, and what happens if it is omitted.
Reference for all vehicle editing; keyed from [vehicle](vehicle.md). Engine semantics come
from Simutrans-Extended master at `d09e920` unless stated otherwise.

The general rule is a hard-coded default in makeobj: absent keys are read as empty or via
`obj.get_int(key, DEFAULT)`. Notable consequences of omission are called out per field below.

## Identity and dates

- `name` is the savegame identity of the vehicle; renames need a `compat.tab` entry (see
  [pakset-compatibility](../pakset-compatibility.md)). If omitted it is empty, which is not a
  compile error but makes the object unusable: every nameless vehicle shares one key and
  overwrites the others, and lookup by name fails. Treat it as required.
  `[CODE simutrans-extended master @ d09e920]`
- `copyright` is the authorship credit. If omitted it is empty.
  `[CODE simutrans-extended master @ d09e920]`
- `intro_year` and `intro_month` open availability for new purchase. If omitted they default
  to the engine's 1492 introduction in month 1.
  `[CODE simutrans-extended master @ d09e920]`
- `retire_year` and `retire_month` close new availability: retirement ends production only,
  the engine's retired check meaning "no longer in production". Existing vehicles keep
  running, and upgrades to a retired type stop being offered. If omitted they default to the
  engine's 2999 retirement in month 1.
  `[CODE simutrans-extended master @ d09e920]`
- The timeline must be on for dates to apply; this pakset runs `use_timeline = 3` from
  `starting_year = 1750`. `[CODE New master @ f8859c42d]`

## Economics

- `cost` is the purchase price; if omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `runningcost` is the per-kilometre cost; if omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `fixed_cost` is the monthly cost. `fixed_maintenance` is the original Extended name and is
  still read; if both are omitted the value is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `battery_round_trip_efficiency` is the battery round-trip efficiency as an integer
  percentage (85 = 85 percent), used only by `engine_type=battery` vehicles. Battery
  traction has no entry of its own in `config/fuel.tab` (see [balancing](../balancing.md)):
  the engine prices its energy from the electricity entry (`fuel[electric]`) of that file
  divided by this efficiency, because electricity is bought from the grid and a proportion
  of it is lost in charging and discharging the battery. If omitted it is 85, the average
  of 2020s-dated values: 85 percent (NREL Annual Technology Baseline 2023 and 2024
  utility-scale battery storage assumptions, from Cole & Karmakar 2023); 84 percent
  (computed from EIA 2022 United States utility-scale battery fleet data: gross generation
  2,913,805 MWh against 539,294 MWh of charging electricity and own loads, published 2023);
  86 percent (measured round-trip efficiency of a 3.0Ah NMC 18650 cell at a 0.2C charge
  rate; Bobanac, Basic & Pandzic, IEEE EUROCON 2021); (85 + 85 + 84 + 86) / 4 = 85. A value
  of 0 falls back to the unscaled electricity cost.
  `[CODE simutrans-extended ex-15, uncommitted working tree @ 2026-09-20]`
- For how these values are calibrated, see [balancing](../balancing.md).

## Physics and running

- `speed` is the maximum speed in km/h; if omitted it is 0, and a zero-speed vehicle is not
  rejected by makeobj. `[CODE simutrans-extended master @ d09e920]`
- `power` is engine power in kW; if omitted it is 0. `gear` multiplies power and tractive
  effort, with 64 meaning 100 percent; if omitted it is 100 percent (stored 64).
  `[CODE simutrans-extended master @ d09e920]`
- `tractive_effort` is starting tractive effort in kN; if omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `brake_force` is vehicle braking force in kN, meaning the force stopping the vehicle, not
  the force of the brakes on the wheels. If omitted it is `BRAKE_FORCE_UNKNOWN` (65535), which
  the engine treats as unknown rather than zero; a value of 0 means an unbraked vehicle.
  `[CODE simutrans-extended master @ d09e920]`
- `weight` is in kilogrammes; if omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `axles` counts the vehicle's axles; it is not stored directly. If omitted it is 1 for water
  and maglev, otherwise 2. `[CODE simutrans-extended master @ d09e920]`
- `axle_load` is the load of the heaviest axle, used in routing against each way's limit. If
  omitted it is computed as `weight / axles` in tonnes.
  `[CODE simutrans-extended master @ d09e920]`
- `length` is in carunits, of which there are 16 to a tile: 8 is half a tile and 4 a quarter.
  If omitted it is 8. One carunit is 1.875 m at the pak's graphics scale (30 m per tile); the
  value, however, must cover the drawn sprite rather than the real body, because the field
  spaces the images. Derivation and method: [road-vehicle-lengths](road-vehicle-lengths.md).
  `[CODE simutrans-extended master @ d09e920]` `[CODE New master @ fc87c0424]`
- `waytype` selects the way system: `track`, `road`, `tram_track`, `water`, `air`,
  `narrowgauge_track`, `maglev_track`. It is required: if omitted, makeobj aborts with an
  invalid-waytype error. `[CODE simutrans-extended master @ d09e920]`
- `engine_type` selects traction: steam, diesel, electric, bio, sail, fuel_cell, hydrogene,
  battery, petrol or turbine. If omitted it is "unknown", except that an `electrified_track`
  waytype forces electric. `[CODE simutrans-extended master @ d09e920]`
- `freight` names the good carried, as defined in `New/goods/goods-128.dat` (see
  [goods](good.md)). If omitted it is the special `None` good.
  `[CODE simutrans-extended master @ d09e920]`
- `air_resistance` and `rolling_resistance` are the drag coefficients in physics
  calculations. If omitted they default per waytype: air resistance 1.6 track/tram/monorail,
  1.2 narrow gauge, 25 water, 1.45 maglev, 1.0 air, 0.15 road; rolling resistance 0.0015
  track/monorail, 0.006 tram, 0.0017 narrow gauge, 0.001 air and water, 0.0013 maglev, 0.009
  road. `[CODE simutrans-extended master @ d09e920]`
- `range` is the maximum kilometres between stops, used by aircraft and some road vehicles;
  if omitted it is 0 (no limit). `minimum_runway_length` gates aircraft by airfield size; if
  omitted it is 0. `[CODE simutrans-extended master @ d09e920]`
- `way_wear_factor` is the wear the vehicle inflicts on ways, in standard 8-tonne axle loads
  times 10,000, applied on every tile traversed. If omitted it is left uninitialised and the
  engine computes it from waytype, axle load, weight and steam hammer-blow during scaling.
  `[CODE simutrans-extended master @ d09e920]`
- `is_tall` marks vehicles barred from restricted-height bridges: routing treats
  height-restricted tiles as land for tall convoys. If omitted it is not set, so the vehicle
  is not treated as tall. `[CODE simutrans-extended master @ d09e920]`
- `is_tilting` marks tilting trains, which take corners at higher speeds. If omitted it is
  false. `[CODE simutrans-extended master @ d09e920]`
- `override_way_speed` frees the vehicle from the underlying way's speed limit, intended for
  fly boats. If omitted it is false. `[CODE simutrans-extended master @ d09e920]`
- `is_sidewalker` matches no code in Extended master or its makeobj writer, so it has no
  effect whether present or omitted. It is present in `New/bus/man_on_bicycle.dat` and
  `New/bus/post-boy.dat`. `[CODE simutrans-extended master @ d09e920]`
  `[CODE New master @ f8859c42d]`

## Capacity, comfort and loading

- `payload[i]` is capacity per accommodation class index, and `comfort[i]` its comfort
  rating; see [class](../class.md). If `payload[0]`/`comfort[0]` are omitted they fall back
  to the older unindexed `payload`/`comfort` keys, with defaults 0 and 100 respectively;
  later class indices omitted repeat the previous class's comfort value.
  `[CODE simutrans-extended master @ d09e920]`
- `overcrowded_capacity` is standing capacity; if omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `mixed_load_prohibition` forbids mixing another good in the same car; if omitted it is
  false. `[CODE simutrans-extended master @ d09e920]`
- `catering_level` is 0 for no catering, higher for better catering; see
  [class](../class.md). If omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`
- `min_loading_time` and `max_loading_time` bound loading time with few versus full
  boardings, in seconds. If omitted they are the sentinel 65535, and the vehicle reverts to
  the old tick-based default by waytype: 2000 road and tram, 4000 rail, narrow gauge,
  monorail and maglev, 20000 water, 30000 air.
  `[CODE simutrans-extended master @ d09e920]`

## Operation, cabs and upgrades

- `bidirectional`, `can_lead_from_rear`, `has_front_cab` and `has_rear_cab` feed the
  coupling placement flags; see [coupling-constraints](coupling-constraints.md). If
  `has_front_cab` and `has_rear_cab` are omitted, they are the sentinel 255 meaning "auto",
  and the placement flags are derived from `bidirectional`, `power` and the constraint lists.
  Setting a cab key to 0 suppresses the derived head flag on that end and disables the
  corresponding automatic rule. `[CODE simutrans-extended master @ d09e920]`
- `sound` names the running sound; -1 means none. If omitted it is no-sound.
  `[CODE simutrans-extended master @ d09e920]`
- `smoke` names the exhaust smoke object shown while running; if omitted there is none.
  `[CODE simutrans-extended master @ d09e920]`
- `upgrade[i]` names successor vehicle types. If omitted there is no upgrade target.
  `upgrade_price` is the upgrade cost; `upgrade_cost`, where present, overrides it. If both
  are omitted the upgrade price equals `cost`. `available_only_as_upgrade` blocks new
  purchase, leaving the type obtainable only by upgrading; if omitted it is false.
  The variant key `available_as_upgrade_only`, used in `New/trains/gwr-aberdare-superheated.dat`,
  is not read by makeobj and has no effect. `[CODE simutrans-extended master @ d09e920]`
  `[CODE New master @ f8859c42d]`

## Obsolescence

- `increase_maintenance_after_years` is the number of years after retirement at which
  maintenance begins to rise; if omitted it is 0, meaning use the `simuconf.tab` default for
  the waytype. `increase_maintenance_by_percent` is the size of the eventual increase; if
  omitted it is 0. `years_before_maintenance_max_reached` is the number of years over which
  the rise reaches its maximum; if omitted it is 0.
  `[CODE simutrans-extended master @ d09e920]`

## Constraints, liveries and images

- `Constraint[Prev][i]` and `Constraint[Next][i]` name coupling partners, with the special
  values `none` and `any`; if all are omitted the end is free and the placement flags are
  derived as described above. Full rules: [coupling-constraints](coupling-constraints.md).
- `way_constraint_permissive[i]` and `way_constraint_prohibitive[i]` set way access bits; if
  omitted they are ignored (the writer's sentinel of 255 is out of range), so no constraint
  is set. Full rules: [way-constraints](way-constraints.md).
- `liverytype[i]` names liveries; if no `EmptyImage` livery index is present no livery types
  are required, but once any `EmptyImage[dir][livery]` exists, every `liverytype[i]` up to the
  livery count is mandatory and makeobj aborts if one is missing.
  `[CODE simutrans-extended master @ d09e920]`
- `EmptyImage[dir]` (and `[dir][livery]`) supplies the empty/base images. If omitted there
  are none and the vehicle has no sprite. `FreightImage[...]` supplies loaded images; if
  omitted there are none and the base image is used. `FreightImageType[i]` names the goods
  shown; it is required once loaded images exist. See
  [liveries-and-special-colours](../graphics/liveries-and-special-colours.md) and
  [image-layout](../graphics/image-layout.md).
  `[CODE simutrans-extended master @ d09e920]`

## Open questions

- What historical sources calibrate `brake_force` values? None located: thread 8087 covers
  only the braking-distance formula, and `.dat` comments cross-reference other vehicles
  (for example Class 331 reuses Class 195 brakes).
