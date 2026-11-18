---
status: draft
verified: simutrans-extended ex-15 @ bdfdc8311
---
# Engine bugs

**Covers**: defects in the Simutrans-Extended engine, repository
`jamespetts/simutrans-extended`, discovered while doing pakset work, together with the evidence
needed to fix them.

Pakset defects live in [known-bugs](known-bugs.md). This doc exists because some pakset
balancing work cannot be completed correctly until the engine defect is fixed, and the fix is
made in a different repository.

## Notes

- Read this before investigating a discrepancy between a cost or distance the engine reports
  and the value the `.dat` or `config/` file implies.
- The engine repository is a separate workspace. Do not edit it from this one.
- Each entry gives the function, the exact code as found, the intended behaviour, the history,
  the effect measured against the pakset's own settings, and a test that distinguishes the two
  behaviours. That is enough for an agent with no other context to act on.

## 1. Odometer remainder is discarded, and goes negative above one kilometre

**Fixed on `ex-15` by `bdfdc8311`** ("FIX: Retain the odometer remainder and book way distance
consistently"). Deliberately **not** applied to `master`, so the two branches differ in
distance-based running cost by the amount quantified below.

Priority 3 (minor) by economic effect. It is a correctness defect, and it is documented at this
length because every existing balance was struck against the old behaviour.

### Where

`convoi_t::increment_odometer`, in `simconvoi.cc`. The function is called with the number of
vehicle steps the convoy has just moved and converts them into whole kilometres, charging
distance-based running costs once a kilometre has accumulated.

### What the code did

After computing the whole kilometres in the accumulator, the remainder was removed with:

```cpp
steps_since_last_odometer_increment -= km * steps_since_last_odometer_increment;
```

`steps_since_last_odometer_increment` is declared `sint64` in `simconvoi.h`, and `km` is the
integer division of that same accumulator by the steps in a kilometre. The expression therefore
multiplied the accumulator by itself divided by the kilometre length.

### What it should have done

```cpp
steps_since_last_odometer_increment -= km * welt->get_settings().get_steps_per_km();
```

The remainder after removing the whole kilometres has to be the accumulator minus the kilometres
charged, each kilometre being `get_steps_per_km()` steps.

### History

The defect was introduced by commit `f11d45a8b`, "Yet another odometer fix", 20 August 2011,
which replaced a correct expression with the present one while rewriting the surrounding
function. The commit replaced

```cpp
steps_since_last_odometer_increment -= (km * 255000) / meters_per_tile;
```

with the broken form. The replacement loses the `get_steps_per_km()` factor; `255000 /
meters_per_tile` was the former spelling of that same quantity.
`[CODE simutrans-extended ex-15 @ bdfdc8311]`

### What the fix changed

Two things, not one:

- The subtraction now uses the kilometre length, so the sub-kilometre remainder survives to the
  next booking.
- `departure_data_t::increment_way_distance` now receives the booked distance rather than the
  whole accumulator. Before the fix it received the whole accumulator and the accumulator was
  then cleared, so the way distance was correct by accident; after the fix the remainder is
  retained, and passing the whole accumulator would count it twice. The way-owner revenue split
  is therefore unchanged in size, not increased.
  `[CODE simutrans-extended ex-15 @ bdfdc8311]`

The two figures affected by the defect itself are the kilometres booked for running cost and the
kilometres passed to `vehicle_t::step_km` for wear. `CONVOI_DISTANCE` and
`total_distance_traveled` record the same figure and are affected identically.

### Effect on the balance

The size of the error is fixed by two numbers: the steps in a kilometre, S, and the steps booked
in one call, c.

- `S = (1000 × VEHICLE_STEPS_PER_TILE) / meters_per_tile = (1000 × 256) / 125 = 2,048` at the
  pakset's 125 metres per tile.
- The accumulator rises in steps of c, so the value at the moment of booking is
  `c × ceil(S / c)`, not S. The old code charged one kilometre for that whole cycle and then set
  the accumulator to zero. The distance charged was therefore short by

  `loss = (c × ceil(S / c) − S) / (c × ceil(S / c))`

  and running cost, wear distance and the distance statistic were all understated by that
  fraction. The factor by which they were understated is `1 / (1 − loss)`.
- c is set by speed and by the sync step:
  `c ≈ (256 / meters_per_tile) × speed(m/s) × step_seconds`, with
  `step_seconds = (1000 / fps) × time_multiplier / 16`. At the default 25 frames per second and
  normal speed that is 0.04 s; the game speed multiplier scales it.
  `[CODE simutrans-extended ex-15 @ bdfdc8311]`

| c | Speed at normal speed | Loss |
|---|---|---|
| 1, 2, 4, 8, 16, 32, 64 | up to 2,800 km/h for 64 | 0 (c divides 2,048 exactly) |
| 3 | about 130 km/h | 0.05 per cent |
| 5 | about 220 km/h | 0.10 per cent |
| 6 | about 260 km/h | 0.20 per cent |
| 9 | about 395 km/h | 0.20 per cent |
| 12 | about 525 km/h | 0.20 per cent |
| 18 | about 790 km/h | 0.20 per cent |
| 24 | about 1,050 km/h | 0.78 per cent |
| 36 | about 1,580 km/h | 0.20 per cent |
| 73 | not reached by speed alone | 3.3 per cent |
| 96 | not reached by speed alone | 3.0 per cent |

The loss is not monotonic in c: it vanishes whenever c divides 2,048 exactly, which is why the
powers of two show none.

In normal play c is small. A train at 100 km/h books 2 steps per call, one at 160 km/h books 3,
an aircraft at 800 km/h books 18: losses of 0, 0.05 and 0.2 per cent. The game speed multiplier
multiplies c, so at four times normal speed a 100 km/h train books 9 and loses 0.2 per cent. The
largest loss reachable by any plausible combination of speed and game speed is about 3 per cent,
and that needs a step size in the seventies or nineties, which only a high multiplier with a fast
vehicle produces.

### Consequences

1. **It does not explain the infrastructure finding.** Infrastructure charges never pass through
   the odometer. Way, bridge, tunnel, signal and station costs are set by their own `.dat` prices
   and maintenance and are untouched by this defect. A vehicle running cost that is at most 0.8
   per cent low in normal play cannot make infrastructure appear too expensive.
2. **It is not a material cause of operating costs being low relative to revenue.** The
   direction is right, but the size is far below the resolution of the historical evidence and
   far below any factor-level discrepancy that has been measured. It should be corrected for
   correctness, not used as an explanation.
3. **The fork is safe.** Because the effect is at most about 0.8 per cent in normal play and
   usually zero, a balance derived on `ex-15` does not need a separate version for `master`. Any
   future statement of a balance should name the branch it was derived on, but the two branches
   do not need different `.dat` values.
4. **Do not attribute a large historical discrepancy to this defect.** If a later comparison
   finds costs wrong by a factor, the cause is elsewhere: the calibration level, the price
   index, or the specification change between eras, not the odometer.

## 2. Vehicle upgrade price follows the maintenance index, not the purchase index

Decision needed, not a confirmed defect. Recorded here because it changes what the
`vehicle purchase` and `vehicle maintenance` series in `config/prices.tab` control.

- `vehicle_desc_t::get_upgrade_price()` applies the `vehicle maintenance` price type.
  `vehicle_desc_t::get_value()` and `get_base_price()` apply `vehicle purchase`; `running_cost`,
  `max_running_cost`, `fixed_cost` and `upgrade_price` all apply `vehicle maintenance`.
  `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- An upgrade is capital expenditure, so indexing it by maintenance is unexpected. The likely
  reason it is deliberate is that the same field also prices overhauls:
  `vehicle_t::` overhaul handling takes the cost from `get_upgrade_price()` when an upgrade is
  involved, and an overhaul is maintenance. Splitting the two uses would need a separate field.
  `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- Consequence for balancing: any change to the relative level of the two series moves upgrade
  and overhaul costs with maintenance, not with purchase. Do not "correct" this without deciding
  what should index an overhaul.

## Checked and not defects

Recorded so that the same ground is not re-investigated.

- The two vehicle price types are applied. `price_type::vehicle_purchase` and
  `price_type::vehicle_maintenance` appear in `descriptor/vehicle_desc.cc`, not only in the
  naming switch in `simworld.h` and the display in `prices/gui`. `[CODE simutrans-extended ex-15
  @ 9fdefa153]`
- The price interpolation is correct. `get_inflation_adjusted_price` compares a month index with
  the record's year field, and `price_record_t`'s constructor multiplies the parsed year by 12,
  so both sides are in months. `[CODE simutrans-extended ex-15 @ 9fdefa153]`
- Running costs are booked as negative amounts, consistently with the rest of the finance code.
  `convoi_t::add_running_cost` accumulates the negated per-vehicle running cost before booking
  it, and the toll calculation relies on that sign. `[CODE simutrans-extended ex-15 @ 9fdefa153]`

## Open questions

- Should `increment_way_distance` receive the charged distance or the full accumulator?
- Should overhauls and upgrades share one price type, and if so which?
