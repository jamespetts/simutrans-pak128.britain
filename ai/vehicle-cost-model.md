---
status: draft
verified: simutrans-extended ex-15 @ 9fdefa153; New ex-15 @ 8d0603d81
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
- Because `fixed_cost` is doubled by the settings while `runningcost` is not, the balance between
  standing and distance costs in the `.dat` files is not the balance the player experiences.
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
  vehicle capital to "in game" by dividing by 8 and the monthly figure by 4. The engine does
  neither: it charges the `.dat` figure with only the price index applied, and multiplies the
  monthly figure by 2 at this pakset's settings. The workbook's in-game columns are therefore not
  a description of the engine. Which convention the older calibration was built on, and whether
  any `.dat` value was set from that column, is unresolved.
