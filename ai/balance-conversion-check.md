---
status: draft
verified: simutrans-extended ex-15 @ bdfdc8311; New ex-15 @ 8d0603d81
---
# The conversion check

**Covers**: the in-game price evidence that settles the `.dat` unit to pound conversion, the
arithmetic, and what it does and does not settle. Parent:
[balance-synthesis](balance-synthesis.md), which holds the operating account that depends on it.

## The evidence

A screenshot of the in-game railway tools tooltip was supplied on 2026-11-17. It reads:

> Steel track (97.5lb/yard), 1,974.00c (-4.21c) / km, 160km/h, 20t, Durability: 356,400.0000

**The object is identified exactly, not inferred.** The durability divides by 10,000 before
display, so the tooltip's 356,400 corresponds to `wear_capacity = 3564000000`. Only one file in
the pakset carries that value: `New/ways/wssri-intermediate.dat`, which also matches the tooltip's
97½ lb/yard, 160 km/h and 20-tonne axle load, and whose `cost=90000` and `maintenance=450` are
therefore the values on display. `[CODE New ex-15 @ 8d0603d81]`

## The formula, read from the engine

```cpp
// tool_build_way_t::get_tooltip, simtool.cc
const sint64 tile_price = desc->get_value();
const sint64 km_price = (tile_price * base_meters_per_tile) / meters_per_tile;
const sint64 km_maint = (tile_maint * base_meters_per_tile) / meters_per_tile;
tooltip_with_price_maintenance(welt, desc->get_name(), (-km_price - km_forge_cost), km_maint);

// tooltip_with_price_maintenance
money_to_string(tool_t::toolstr+n, (double)price/-100.0);
```

`desc->get_value()` is the engine-scaled value: `set_scale` has already multiplied the `.dat` value
by `meters_per_tile / 1000`. The tooltip then multiplies by `base_meters_per_tile / meters_per_tile`
and divides by 100. The two length factors cancel, so **the displayed figure per kilometre is the
`.dat` value per tile divided by 100**, plus the same treatment of the forge cost.
`[CODE simutrans-extended ex-15 @ bdfdc8311]`

## The conversion

| Step | Result |
|---|---|
| `.dat` value | 1 raw `.dat` unit |
| engine scale | × 0.125 |
| kilometre | × 8 |
| display | ÷ 100 |
| timescale, capital | × £0.396311 |
| **combined** | **× £0.00396311** |

So one raw `.dat` unit is £0.00396311 in 1900 for a capital or annualised amount, and
£0.00005208 for a revenue amount. The earlier statement that it was £0.396311 was a
per-*displayed*-unit rate applied to a per-raw-unit value, and it made every infrastructure pound
figure 100 times too large.

## Confirmation from the tooltip

`wssri-intermediate` at 90,000 a tile, with `forge_cost_track` 15,000, gives
`(90,000 + 15,000) × 0.00396311 = £416` a kilometre in 1900 money. The tooltip displays a figure
scaled by the price index in force at the time of the reading; the index cancels from the
`.dat`-to-pound ratio, so the conversion does not depend on the year of the screenshot.

## Two screenshots, two years, one formula

A second screenshot from the **master** branch of the engine and pakset was supplied on
2026-11-17, showing the same object:

| Reading | Build | Price per km | Maintenance per km |
|---|---|---|---|
| 1 | ex-15 test run | 1,974.00 | -4.21 |
| 2 | master | 1,100.00 | 0.00 |

Both are the same object: the tooltip's durability of 356,400 is `wear_capacity` 3,564,000,000,
which only `ways/wssri-intermediate.dat` carries, and its 97½ lb/yard, 160 km/h and 20-tonne axle
load match. `[CODE New master @ 8d0603d81]` The two branches' values for that file are identical:
`cost=90000`, `maintenance=450`. `[CODE New master and ex-15 @ 8d0603d81]`

**Settings cannot explain the difference, and the tile length cancels.** In the engine's path the
stored value is `.dat × (meters_per_tile / 1000) × (index / 100)`, and the kilometre conversion is
`× (base_meters_per_tile / meters_per_tile)`. The two length factors cancel exactly for any
`meters_per_tile`, and `bits_per_month` does not enter the price at all. So the displayed price is
`.dat / 100 × index / 100`, and nothing else:

| Displayed | Implied index | Nearest year in the `infrastructure` series |
|---|---|---|
| 1,100 | 104.76 | between 1910 (104) and 1911 (106) |
| 1,974 | 188.00 | exactly 1930 (188) |

That is the whole of the difference: the same object in two runs at about 1910 and about 1930.
Two independent builds agreeing to the unit on one formula is the strongest confirmation available
without a controlled in-game reading, and it confirms the capital chain.

## What the screenshots do not validate

Maintenance. The maintenance line of the way tooltip cannot be reconciled with the booking code.
`finance_t::get_maintenance_with_bits` charges
`get_inflation_adjusted_price(month, calc_adjusted_monthly_figure(maintenance[tt]), infrastructure)`,
i.e. the `.dat` maintenance is scaled by `meters_per_tile/1000`, doubled by the monthly factor and
indexed by `infrastructure`. For `wssri-intermediate` (`maintenance=450`) at the reading's own
index (188, 1930) that is 16.85 a kilometre per month; without the doubling it is 8.42. The
tooltip showed 4.21. That value is reproducible only with the index at 94 (about 1895) and no
doubling, which contradicts the price reading in the same tooltip. The maintenance line is
therefore unreliable, and the earlier inference that the paks carry a near-zero maintenance value
does not follow. The capital conversion is unaffected.
`[CODE simutrans-extended ex-15 @ 2ec587a]`

## What it confirms

- The measured permanent-way-only cost is £1,300-1,900 a kilometre. The pakset's 97½ lb/yard
  track, with its forge, is £416: **three to four times too low**.
- `wssr`, the plain 86 lb/yard way at 55,000 a tile, is £218 a kilometre: **six to nine times too
  low**.
- So infrastructure capital is too cheap, not too expensive, and the maintenance finding inverts
  in the same way.

## What it does not settle

- **Which timescale a per-month charge uses.** The capital rate is confirmed for one-off
  purchases. Way maintenance and vehicle `fixed_cost` accrue per month, and whether they take the
  capital or the revenue rate depends on kilometres travelled per game month, which is still M3.
- **The revenue side.** Fares and the coal rate are pinned by their own anchors at 76.09 times the
  capital rate; nothing in this check touches them.
- **The vehicle capital anomaly.** At the confirmed rate, the present vehicle `.dat` costs are two
  to nine times too *high* while infrastructure is three to nine times too *low*. That contradiction
  is in the data, not in the conversion, and is recorded in
  [vehicle-cost-evidence](vehicle-cost-evidence.md).
