---
status: draft
verified: simutrans-extended ex-15 @ 2ec587a; New ex-15 @ e46fd294b
---
# Vehicle cost model

**Covers**: the money fields of `Obj=vehicle` (`.dat` keys `cost`, `runningcost`, `fixed_cost`,
`upgrade_cost`), what the engine charges for each, and the scaling that `bits_per_month` and
`meters_per_tile` apply, so that capital, per-kilometre and per-month costs can be compared and
calibrated against each other.

## Purpose

Balancing vehicles needs the arithmetic before the prices. The `.dat` cost values currently in
the tree are not a reference level: they predate the historical-price balancing that ex-15 is
intended to allow, and are to be replaced rather than adjusted.
`[USER-DIRECTION:2026-11-16]`

This doc records the mechanism. The index series are specified in [prices-config](prices-config.md);
the base-level evidence by vehicle type belongs in a vehicle evidence doc, alongside
[infrastructure-cost-evidence](infrastructure-cost-evidence.md).

## The money fields

| `.dat` key | Engine member | Default if omitted | Charged as |
|---|---|---|---|
| `cost` | `base_cost` | 0 | One-off purchase price; basis of the resale value |
| `runningcost` | `running_cost` | 0 | Per whole kilometre, per vehicle |
| `fixed_cost` (also read as `fixed_maintenance`) | `fixed_cost` | 0 | Per game month, per vehicle |
| `upgrade_price`, overridden by `upgrade_cost` | `upgrade_price` | `cost` | One-off, when an obsolete vehicle is upgraded |
| `max_running_cost` | `max_running_cost` | `runningcost × 3` | Ceiling of the wear ramp |
| `increase_maintenance_by_percent` | | 0, meaning the `simuconf.tab` value (400) | Obsolescence ceiling, as a percentage of the base |
| `years_before_maintenance_max_reached` | | 0, meaning the `simuconf.tab` value (20) | Years over which the obsolescence ceiling is reached |

`[CODE simutrans-extended ex-15 @ 9fdefa153]`

## Units

- The canonical table covering every category of money is [conversion-chains](conversion-chains.md);
  the three vehicle rows are derived here and must agree with it.
- The engine stores money in hundredths of the displayed currency unit (Simucents); every display path
  divides by 100. `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- The pakset's conversion from that displayed unit to 1900 pounds is recorded in
  [prices-config](prices-config.md#unit-conversion): 1 Simucredit is £0.005208 on the revenue
  timescale and £0.396 on the capital timescale.
- The engine knows only one currency: a vehicle's purchase price, its per-kilometre cost and its
  monthly cost all leave the same account. The two timescale rates are a device for comparing
  different kinds of real cost to 1900 pounds; they are not an engine distinction. Which rate a
  given field should be calibrated at is therefore a decision for the synthesis, not a property
  of the field. The present `.dat` level cannot be used to infer it.

## Engine scaling of the money fields

Derived from the **ex-15** engine source on 2026-11-22 (branch `ex-15`, not `master`; the two agree
on these functions, but every claim here was read on `ex-15`).

- `karte_t::set_scale` passes `scale_factor = get_meters_per_tile()` to every vehicle descriptor,
  and to ways, tunnels, bridges, way objects, station buildings, goods, industries and signals.
  Depots, headquarters and city buildings are absent, so they are not scaled.
  `SIMTYPES.H set_scale_generic<T>(value, f) = value x f / 1000`, integer division.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`
- `obj_desc_transport_related_t::set_scale` computes `price = base_cost x scale_factor / 1000`,
  and the same for `maintenance` and `way_only_cost`; `vehicle_desc_t::set_scale` additionally
  scales `upgrade_price`, `fixed_cost`, `initial_overhaul_cost` and `max_overhaul_cost`.
  **`running_cost` is not scaled.** `[CODE simutrans-extended ex-15 @ 2ec587a]`
- The `.dat` value is the 1900 nominal. `config/prices.tab` line 2: "100% = the price specified in
  the .dat file (adjusted for meters per tile and bits per month)". At display or charge the engine
  applies the **object type's own series** for the current month:
  `adjusted = value x index(month) / 100` (`get_inflation_adjusted_price`, linear interpolation
  between the listed years, month = `year x 12 + month`).
  `[CODE simutrans-extended ex-15 @ 2ec587a]`
- The series differ by type, and this is the part that is easy to get wrong:

  | Object | Series |
  |---|---|
  | Vehicle `cost` | `vehicle purchase` |
  | Vehicle `runningcost`, `fixed_cost`, `upgrade_price` | `general` (`vehicle maintenance` is commented out, so it falls back) |
  | Ways, tunnels, bridges, way objects, signals, roadsigns | `infrastructure` |
  | Buildings: stations, station buildings, signalboxes, depots, HQ, city buildings, industries | `buildings` |
  | Goods | `goods rate` |
  | Land | `city land` / `country land` |
  | Engine settings (`cost_*`) | `general`; `forge_cost_*` are indexed `infrastructure` |

  `[CODE simutrans-extended ex-15 @ 2ec587a]` `[CODE New ex-15]`
- At `meters_per_tile = 125` and `bits_per_month = 22` (`base_bits = 18`, `base_mpt = 1000`) the
  factors at index 100 are: purchase and building cost **`.dat x 0.00125`**; building, way and
  vehicle monthly maintenance **x 2** on top of the load-time scale
  (`calc_adjusted_monthly_figure` = `2^(22-18) / INT(1000/125)` = 2); `runningcost`
  **`.dat x 0.01` per km**; way/tunnel/bridge/way-object cost **`.dat x 0.01` per km**.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`
- The per-month factor applies to **all** monthly charges, not only vehicle `fixed_cost`:
  `finance_t::get_maintenance_with_bits` computes
  `get_inflation_adjusted_price(month, calc_adjusted_monthly_figure(maintenance[tt]), infrastructure)`,
  and `weg_t` and `gebaeude_t` book their `get_maintenance()` into that accumulator. Building
  maintenance follows the same path with the `buildings` series.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`

### Worked example: CSLR 1890 Tube Locomotive, January 1891

`.dat`: `cost=650000`, `runningcost=51`, `fixed_cost=10677`. Series at Jan 1891:
`vehicle purchase` 80, `general` 97.

| Figure | Arithmetic | At 125 m/tile | At 120 m/tile |
|---|---|---|---|
| Price | 650,000 x 0.125 = 81,250; x 80/100 = 65,000; /100 | **650.00** | **624.00** |
| Maintenance per km | 51 x 97/100 = 49; /100 | **0.49** | **0.49** |
| Maintenance per month | 10,677 x 0.125 = 1,334; x 97/100 = 1,293; x2 = 2,586; /100 | **25.86** | **24.84** |

The user's 2026-11-22 screenshot shows 624.00 / 0.49 / 24.84. `runningcost` is the control: it is
not tile-scaled, so it is identical at both settings, and its 0.49 fixes the date (general 97) and
the conversion. The two scaled figures are both 4 per cent below the 125 m/tile prediction, which
is exactly the ratio 120/125. The three figures therefore reproduce the dialog only at
`meters_per_tile = 120`. Setting `METERS_PER_TILE` on the workbooks' Params sheet to 120 gives
624.00 / 0.49 / 24.86; the last differs by 0.02 from the dialog because the engine truncates to an
integer at each step (1,281 -> 1,242 -> 2,484 -> 24.84) while the workbook multiplies exactly.
Either the game in the screenshot did not load the pakset's `config/simuconf.tab` (125), or its
setting was changed; this is recorded as an open question, not as an inference about the `.dat`
values. A fresh game with the checked-out config should show 650.00 / 0.49 / 25.86.

The table gives the engine's integer-truncated results. Exact multiplication gives 0.4947 for the
per-kilometre charge and 25.89 for the monthly one; the engine casts to integers after each step
(`1,334 -> 1,293 -> 2,586`), so a workbook built on exact arithmetic will differ in the second
decimal place.
`[USER-DIRECTION:2026-11-22]` `[CODE New ex-15]`

### What the example does not say

- It does not make the `.dat` values 1891 prices. They are 1900 prices; the 1891 figure is the
  1900 figure deflated by the vehicle-purchase index. Writing 624 (or 650) into `cost` would
  double-count the deflation.
- The four per cent tile difference is a settings difference, not an inflation effect. The
  `general` index at 1890 is 96, which happens to equal 120/125; that coincidence is what made the
  earlier derivation look like a second index.

## Per-kilometre cost

- Charged once per whole kilometre travelled, per vehicle, from `runningcost`:
  `convoi_t::increment_odometer` converts accumulated steps to kilometres and books the sum of
  the convoy's per-vehicle `running_cost`. `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- Steps per kilometre are `(1000 × VEHICLE_STEPS_PER_TILE) / meters_per_tile`, with
  `VEHICLE_STEPS_PER_TILE` equal to 256. At 125 metres per tile that is 2,048 steps.
  `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- Consequences: the per-kilometre charge is independent of `bits_per_month`, and independent of
  `meters_per_tile` in real terms, because the step count is derived from the same setting. A
  `runningcost` of 1 is one hundredth of a currency unit per vehicle-kilometre at any scale.
- The charge is subject to the wear ramp (below). On `master` it is also subject to the odometer
  remainder defect, which under-charges the distance by up to about 0.8 per cent in normal play;
  `ex-15` fixes it. The size of that under-charge, and why it does not explain any large
  discrepancy, is in [engine-bugs](engine-bugs.md).

## Per-month cost

- Charged per game month for each vehicle from `fixed_cost`, through
  `player_t::book_vehicle_maintenance` and `karte_t::calc_adjusted_monthly_figure`.
  `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- The figure charged is

  `fixed_cost × 2^(bits_per_month − base_bits_per_month) ÷ (base_meters_per_tile ÷ meters_per_tile)`

  with `base_bits_per_month` 18 and `base_meters_per_tile` 1000.
  `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- At the pakset's settings, `bits_per_month = 22` and `meters_per_tile = 125`: the month factor
  is 2^(22−18) = 16 and the tile factor is 1000/125 = 8, so `fixed_cost` is charged at **twice**
  its `.dat` value per game month. `[CODE New ex-15 @ 8d0603d81]`
- Consequences: unlike the per-kilometre charge, the monthly charge **is** sensitive to both
  settings, and the two effects run in opposite directions. Raising `bits_per_month` lengthens
  the game month and raises the charge proportionally; lowering `meters_per_tile` shortens the
  tile and lowers it. Only the ratio of the two is visible in the `.dat` figure.
- The same factor applies to **way, bridge, tunnel, way-object and building maintenance**.
  `weg_t` and `gebaeude_t` book `get_maintenance()` into the player's `maintenance[waytype]`
  accumulator; `finance_t::get_maintenance_with_bits` then applies
  `calc_adjusted_monthly_figure` and the `infrastructure` series (buildings: `buildings`).
  A way's `.dat` maintenance therefore costs `.dat x 0.02` SC per km per month at the pakset
  settings, not `.dat x 0.01`. The earlier workbooks applied the doubling to vehicles only and
  understated every infrastructure and building maintenance row by a factor of two.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`
- The way tooltip and the charge do not agree. The charge path above applies the doubling and the
  `infrastructure` index; the tooltip path (`tool_build_way_t::get_tooltip` ->
  `tooltip_with_price_maintenance`) divides the per-kilometre figure by 100. For `wssri`
  (`maintenance=450`) the charge at the price reading's own index (188, 1930) is
  16.85 SC per km per month, and without the doubling it would still be 8.42; the tooltip showed
  4.21. That figure is reproducible only with the index at 94 and no doubling, which contradicts
  the price reading in the same tooltip. The maintenance line of the way tooltip is therefore
  unreliable; do not calibrate way maintenance from it. The booking code, not the tooltip, is the
  authority.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`
- The tile factor is the same one applied to factory output and passenger generation. For a
  monthly charge the reason for dividing by it is not documented in the engine; see the open
  questions.

## Capital cost

- Charged once at purchase: `vehicle_builder_t` books `-get_value()` for a new vehicle and
  `-get_upgrade_price()` for an upgrade. `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- No time or distance scaling is applied to either figure.
- Resale value is `cost × 0.997^(months owned)`, reduced by `used_vehicle_reduction` per mille if
  the vehicle has been driven. The pakset sets `used_vehicle_reduction = 1`, so the reduction is
  0.1 per cent. `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- The 0.997 monthly factor alone puts a vehicle at half its purchase price after about 231
  months, close to 19 years. `[UNVERIFIED]` — arithmetic on the factor, not a pakset decision.

## Overhauls and upgrades

Separate from the wear ramp, a vehicle can be overhauled at a depot. The mechanics are in
`vehicle_t::is_overhaul_needed`, `vehicle_t::overhaul` and `vehicle_t::get_overhaul_cost`:

- **When.** An overhaul falls due when `km_since_last_overhaul` exceeds
  `max_distance_between_overhauls`. A value of zero disables overhauls for that vehicle.
  `[CODE simutrans-extended ex-15]`
- **What it costs.** The first overhaul costs `initial_overhaul_cost`. Successive overhauls
  rise on a sigmoid across `overhauls_before_max_cost` toward `max_overhaul_cost`; the cost is
  `initial + (max - initial) × sigmoid(overhauls, overhauls_before_max_cost)`.
  `[CODE simutrans-extended ex-15]`
- **Where it is booked.** As vehicle maintenance, not as capital: the charge goes through
  `book_vehicle_maintenance`. It is therefore indexed by the `vehicle maintenance` series, not
  by `vehicle purchase`. `[CODE simutrans-extended ex-15]`
- **How long it takes.** `overhaul_month_tenths / 10` months, applied as a wait lock.
  `[CODE simutrans-extended ex-15]`
- **Upgrades.** Replacing a vehicle with a newer type charges `upgrade->get_upgrade_price()` —
  the target vehicle's `upgrade_price`, again as vehicle maintenance. The old vehicle is
  deleted with no resale credit, so `upgrade_price` is the whole net cost of the replacement,
  not a supplement to a trade-in. `upgrade_price` defaults to `cost`, which would make an
  upgrade cost as much as a new vehicle. `[CODE simutrans-extended ex-15]`
- **Coverage.** At the start of this work only nine of the pakset's 3,539 vehicles carried any
  overhaul field, all rail, and 403 carried an `upgrade_price`, most of them the token value
  5000. The targets are now in the `Overhauls & upgrades` sheet of the capital workbook.



## Obsolescence and wear

Two separate ramps raise the charged running cost, and both also reach the monthly cost:

- **Obsolescence.** From the retirement date, `vehicle_desc_t::calc_running_cost` raises the
  running and fixed figures linearly to `increase_maintenance_by_percent` (default 400 per cent)
  over `years_before_maintenance_max_reached` (default 20 years). The pakset does not override
  either setting. `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- **Wear.** `vehicle_t::get_running_cost` raises the running cost from the base figure to
  `max_running_cost` (default three times the base) as kilometres accumulate between overhauls,
  starting at the vehicle's availability-decay distance. `[CODE simutrans-extended ex-15
  @ 9fdefa153]`
- The purchase price is not affected by either ramp. An old, worn vehicle therefore costs more
  to run but not more to buy.

## What these costs exclude

Deliberately, because each is charged elsewhere:

- **Staff.** Crew wages come from `config/staff.tab`, by staff type and year, not from
  `fixed_cost`. `[USER-DIRECTION:2026-11-16]` The engine charges crew only for a vehicle that
  declares `staff[i]` in its `.dat` file; an undeclared type is absent from the vehicle's staff
  map rather than defaulted. Only two of the 871 `.dat` files in `New/trains/` declare any staff
  at all, so railway crew is charged nowhere in the present pakset.
  `[CODE New ex-15 @ 8d0603d81]`
- **Fuel and energy.** Priced in `config/fuel.tab`, by fuel and engine type, and charged per unit
  consumed. `[USER-DIRECTION:2026-11-16]`
- **Infrastructure.** Depot upkeep is charged on the depot building, way maintenance on the way,
  and corporate administration on the headquarters. None of it is in the vehicle fields.
  `[USER-DIRECTION:2026-11-16]`

The consequence for calibration is that the vehicle fields cover only the vehicle itself:
purchase, repair and servicing, and the standing cost of owning it.

## How the three relate

For one vehicle in one game month:

`outlay = fixed_cost × K ÷ F + runningcost × kilometres + fuel + staff`

where K is the month factor and F the tile factor, which are 16 and 8 at the pakset settings.
The purchase price is separate and one-off.

The most useful single ratio for judging a vehicle is **months of fixed cost per purchase
price**, `cost ÷ (fixed_cost × K ÷ F)`. It says how long the standing charge takes to equal the
capital outlay, and it is invariant to the currency conversion, so it can be compared with
historical figures before the conversion question is settled.

Worked arithmetic, using a 1952 BR Mk1 TSO as it stands in the tree (`cost` 583,000,
`fixed_cost` 694, `runningcost` 0): the monthly charge is 694 × 2 = 1,388 engine units, and the
purchase price is 420 months of it, or 35 years. The numbers illustrate the arithmetic only; the
`.dat` values are not calibrated and are not evidence of anything. `[CODE New ex-15 @
8d0603d81]`

## Consequences for calibration

- Changing `cost` moves only capital and resale. It does not change running or fixed cost.
- Changing `runningcost` is a per-kilometre statement, so its effect depends on utilisation; a
  figure that is right for a busy vehicle is too high for an idle one.
- Changing `fixed_cost` is charged whether or not the vehicle runs, so it is the field that
  decides whether an idle fleet bleeds money.
- Because every per-month charge is doubled by the settings while `runningcost` is not, the
  balance between standing and distance costs in the `.dat` files is not the balance the player
  experiences.
- `upgrade_price` defaults to `cost` and is indexed by the `vehicle maintenance` series, while
  `cost` is indexed by `vehicle purchase`. If both are left at the same nominal figure, the two
  price types will pull them apart over time. See [engine-bugs](engine-bugs.md).

## Open questions

- Why is the monthly charge divided by the tile factor? The factor exists to keep per-tile
  economics constant as tile size changes; for a charge that accrues per month regardless of
  distance, the reason is unrecorded.
- Which of the two conversion rates applies to each vehicle field? To be settled in the vehicle
  synthesis, not here.
- Should the obsolescence ceiling (400 per cent) and the wear ceiling (300 per cent) be set
  independently in the pakset? Neither is currently overridden.
- Is `upgrade_price`'s default of `cost` intended to mean that an upgrade costs as much as a new
  vehicle unless stated?
- The `Vehicles (Simutrans)` sheet of `New/Infrastructure balancing calibration-2.ods` converts
  vehicle capital to "in game" by dividing by 8 and the monthly figure by 4. The capital division
  matches the engine's `meters_per_tile/1000` scale (1/8 at 125 m/tile). The monthly division does
  not: the engine **multiplies** `fixed_cost` by 2 at this pakset's settings. The sheet's monthly
  in-game column is therefore 8 times too small. Which convention the older calibration was built
  on, and whether any `.dat` value was set from that column, is unresolved.
