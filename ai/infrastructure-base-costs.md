---
status: draft
verified: New ex-15 @ 6d8ebdbc5 (working tree); simutrans-extended ex-15 @ 22cc3af
---
# Infrastructure base costs

**Covers**: the `cost=` and `maintenance=` fields of the way, bridge, tunnel, canal and related
`.dat` files, the arithmetic that turns them into real 1900 money, and how the results compare
with the historical research. The year index that multiplies them: [prices-infrastructure](prices-infrastructure.md).
The general balancing context: [balancing](balancing.md).

This is a first-pass audit. Nothing here has been tested in game, and the comparison against
history rests on a small number of anchors.

## The conversion chain

The canonical table for every category of money, with its timescale and monthly factor, is
[conversion-chains](conversion-chains.md). This section derives the two rows that concern ways.

A `.dat` price is not a real price until four separate scalings are applied, and confusing any
two of them changes the answer by an order of magnitude.

1. **Engine scale.** `karte_t` calls `info->set_scale(get_settings().get_meters_per_tile())` on
   every way and structure descriptor. `set_scale_generic` in `simtypes.h` computes
   `value * scale_factor / 1000`, so with `meters_per_tile = 125` a `.dat` cost of 55,000 becomes
   6,875 in game Simucents per tile. `[CODE simutrans-extended ex-15 @ 22cc3af]`
2. **Length.** `meters_per_tile = 125` in `config/simuconf.tab`, so a kilometre is eight tiles.
   `[CODE New ex-15 @ 6d8ebdbc5]`
3. **Display.** The interface divides engine money by 100 before printing it.
   `tooltip_with_price_maintenance` in `simtool.cc` passes `price/-100.0` and
   `... / 100.0`, and `tool_build_way_t::get_tooltip` is the way tool that uses it. **This step
   was missing from the earlier version of this document, and its absence made every pound figure
   in this document and in the synthesis 100 times too large.**
   `[CODE simutrans-extended ex-15 @ bdfdc8311]`
4. **Timescale.** 1 displayed Simucredit is £0.396311 in 1900 for a capital or annualised amount,
   and £0.005208 for revenue. A way's cost and its maintenance are both capital-side amounts, so
   both take the first rate. `[CODE New ex-15 @ 6d8ebdbc5]`

The four combine, for a way, to a single convenient factor:

- real capital cost per kilometre = `.dat` cost × 0.125 × 8 ÷ 100 × 0.396311
  = **`.dat` cost × 0.00396311**;
- real maintenance per kilometre per month = `.dat` maintenance × 0.125 × 2 × 8 ÷ 100 × 0.396311
  = **`.dat` maintenance × 0.00792622**, and per year that × 12. The `2` is
  `calc_adjusted_monthly_figure` (16 ÷ 8 at the pakset settings), applied by
  `finance_t::get_maintenance_with_bits` to the `maintenance[waytype]` accumulator into which
  `weg_t` books `get_maintenance()`. The way tooltip omits it; the charge does not.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`

For per-object classes the same factor applies once the engine scale is used instead of the tile
count: a scaled one-tile object is `.dat` × 0.125 ÷ 100 × 0.396311 = `.dat` × 0.00049539, and an
unscaled object is `.dat` ÷ 100 × 0.396311 = `.dat` × 0.00396311.

**Worked check.** `wssr` has `cost=55000`, so a kilometre costs 55,000 × 0.00396311 = **£218**.
The measured permanent-way-only cost is £1,300-1,900 a kilometre, so the way capital in the
present files is **three to nine times too low**, not a few times too high.

An in-game tooltip read on 2026-11-17 confirms the mechanics: a 97.5 lb/yard steel track displays
1,974.00 a kilometre, and the object is `wssri-intermediate` with `cost=90000` and
`forge_cost_track=15000`. `(90,000 + 15,000) × 0.00396311` is £416 a kilometre, and the displayed
figure is the same quantity divided by the year index in force at the time of the reading; the
ratio between `.dat` and pounds does not depend on that index, because it cancels.
`[CODE simutrans-extended ex-15 @ bdfdc8311]`

## Forge costs

A plain way's build price is `cost + forge_cost_waytype` per tile, not `cost` alone. The forge
charge is the **bed preparation** — trimming, drainage, fencing — and is a separate
`simuconf.tab` setting. Bulk earthworks (cuttings and embankments) are deliberately **excluded**:
they are made with the raise/lower land tool, not with the forge. `[USER-DIRECTION:2026-11-22]`

Settings from 2026-11-22 (midpoints of the synthesis ranges, at 1900 prices): 88,000 for track,
315,000 road, 125,000 water, 225,000 tram, 95,000 narrow gauge, 108,000 maglev, 108,000 monorail,
1,875,000 air. They are scaled by `meters_per_tile/1000` and indexed by `infrastructure`, exactly
like the way's own `cost`. `settings_t::get_forge_cost` (settings.cc) and `wegbauer`
(bauer/wegbauer.cc) show the charge; the parallel-way rule reduces it to
`parallel_ways_forge_cost_percentage_*` (35 per cent for track) when a way of the same type
already runs alongside, and to zero on a tile that already carries one. Bridges, tunnels, piers
and way objects do not pay it. `[CODE simutrans-extended ex-15 @ 2ec587a]`

The 2026-11-22 workbook revision splits the way figures explicitly: "way only" and "way + forge"
in-game columns, and the same split in the suggested `.dat` values. The "way only" suggested
figure is the value for the `.dat` `cost` field at the present settings; the "way only" in-game
column is what the way object alone costs. At the new track forge of 88,000 the bed preparation
is larger than most present way costs, which is the correction: the old 15,000 was £59 per route
kilometre against a measured bed-preparation range of £250-400. `[USER-DIRECTION:2026-11-22]`

## What changing meters_per_tile would do

The setting does not affect every object the same way, and the difference matters if it is ever
changed.

- **Length-based objects.** For ways, bridges, tunnels and way objects, the engine's `0.125` and
  the eight tiles to the kilometre cancel, so the cost per kilometre is independent of
  `meters_per_tile`. Changing the setting from 125 to another value leaves these prices unchanged.
- **Per-object classes.** Station buildings, platforms, signalboxes and signals carry `set_scale`
  but have no compensating tile count, so their price in game is proportional to
  `meters_per_tile`. At 125 m a signal costs `.dat × 0.125`; at 250 m it would cost twice as much.
  **Changing `meters_per_tile` therefore rescales every building, platform and signal price in
  proportion, and leaves every per-kilometre price alone.** Any future change to the setting must
  be accompanied by a rebalancing of the per-object family.
- **Depots, headquarters and city buildings are not scaled at all.** They are absent from
  `karte_t::set_scale` because they are not in `hausbauer_t::modifiable_station_buildings`, so
  neither `meters_per_tile` nor any tile count affects them. `cost_depot_*` is unscaled by length
  and receives only the inflation adjustment.

The per-tile land model, which is outstanding, may force a change to `meters_per_tile`. If it
does, the per-object family and the land values need rebalancing together; the length-based
family does not.

## A trap in the calibration workbook

`New/Infrastructure balancing calibration-2.ods` carries a sheet named "Capital to maintenance
ratio" whose value 76.0917 is 5,843.84 real active hours a year divided by 76.8 Simutrans active
hours a year. That is the **time compression** of the game, and it appears again as 0.013142 in
the Currency conversion sheet.

It is not a scale factor. Treating it as one understates every capital figure by a factor of 9.5,
which is the error this document was written to correct.

The workbook's "Infrastructure costs (Simutrans)" sheet cannot be used for this audit in any
case. Its cost column holds 320, 150 and 130 for ways, while the present `.dat` files hold values
between 3,250 and 250,000, and no way file contains any of those three numbers: the sheet predates
the current data. Its per-kilometre total is also computed as `forge + cost + land × 8`, which
adds two per-tile figures once and a third eight times; every capital-to-maintenance ratio in that
sheet inherits the error.

## Track ways

| Way | Intro | `.dat` cost | Implied £/km, 1900 | Implied £/km/year maintenance | Years of capital |
|---|---|---|---|---|---|
| Wooden waggonway | 1700 | 3,250 | 1,288 | 1,902 | 0.7 |
| Plateway | 1767 | 10,000 | 3,963 | 2,853 | 1.4 |
| Cast iron track | 1789 | 30,000 | 11,889 | 3,805 | 3.1 |
| Wrought iron fishbelly | 1820 | 30,000 | 11,889 | 3,591 | 3.3 |
| Wrought iron | 1845 | 40,000 | 15,852 | 3,329 | 4.8 |
| Wrought iron improved | 1855 | 46,500 | 18,428 | 2,901 | 6.4 |
| WSSR early | 1868 | 52,000 | 20,608 | 2,735 | 7.5 |
| WSSR | 1874 | 55,000 | 21,797 | 2,616 | 8.3 |
| WSSRI | 1888 | 75,000 | 29,723 | 2,378 | 12.5 |
| WSSRI heavy | 1925 | 135,000 | 53,502 | 3,091 | 17.3 |
| CSSR | 1968 | 140,000 | 55,484 | 1,783 | 31.1 |
| TGV | 1981 | 250,000 | 99,078 | 4,518 | 21.9 |

The final column is the capital divided by the annual maintenance, which is the quantity the
engine's economy actually depends on: it sets how many years of maintenance a route must earn
before its construction is paid for.

## The historical comparison

Acworth, *The Elements of Railway Economics*, gives the two sides of that ratio for the United
Kingdom in 1902 and 1903: maintenance of way and works at £500 a mile of open line a year, and
capital for road and buildings of £36,364 a mile. Those are £311 a kilometre a year and £22,596 a
kilometre, giving **72.7 years** of capital. `[LITERATURE:https://archive.org/details/cu31924070676402]`

Every track way in the pakset sits far below that. The best is the 1968 continuous-welded way at
31 years; the 1874 way is 8.3 years and the 1700 waggonway is 0.7 of a year, meaning its annual
maintenance is larger than its construction cost.

Read as a proportion, the pakset's maintenance runs between two and a hundred times the historical
level relative to the capital cost of the same way. The early ways are worst.

The comparison is not exact, and three differences push in known directions:

- Acworth's capital covers road, land, stations and parliamentary expenses, so it is larger than
  the bare way and the true way-only ratio is below 72.7.
- Acworth's maintenance covers way, works and buildings together, so it is also larger than
  way-only maintenance.
- Acworth counts route miles, not track miles; his own per-track figures are lower.

Those three largely cancel, and none of them accounts for a factor of eight.

## What this does not cover

Bridges, viaducts, tunnels, aqueducts, canals, depots and stations all carry their own `cost=` and
`maintenance=` values and have not yet been put through the same arithmetic. Neither has the
forge cost, which adds a per-tile charge taken from `simuconf.tab` rather than from the object.

## Open questions

- What capital-to-maintenance ratio should the pakset target? Acworth gives 72.7 years for a whole
  railway; a bare way with no stations or land is a different object, and the right target for it
  has not been established.
- Is the maintenance of the early ways simply too high, or is the capital too low? The 1700
  waggonway's ratio of 0.7 can only be corrected by one of the two.
- Does the engine charge way maintenance per tile per month as this document assumes, or is there
  a further factor at the call site? The arithmetic here is from the descriptor scaling and
  `config/simuconf.tab`, not from tracing a maintenance payment through the engine.
