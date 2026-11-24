---
status: draft
verified: simutrans-extended ex-15 @ 2ec587a; New ex-15 working tree, 2026-11-23
---
# Conversion chains

**Covers**: for every category of money in the pakset, how the stored number becomes 1900 pounds.
This is the canonical statement. Other documents derive from it and must not restate it.

Read before setting, checking or converting any cost, fare, wage or fuel price. The engine
mechanics are in [vehicle-cost-model](vehicle-cost-model.md) and the index method in
[prices-config](prices-config.md); this document is the arithmetic that joins them.

## The two units and the two timescales

- The engine stores money as a signed integer in **Simucents**. Every display path divides by 100
  to show **Simucredits**. One Simucentric is one hundredth of a Simucredit.
  `[CODE simutrans-extended ex-15 @ 2ec587a]`
- **Revenue timescale**: 1 Simucredit = £0.005208 in 1900, so 1 Simucent = £0.00005208. This is
  the rate for anything earned or spent per kilometre of travel.
- **Capital timescale**: 1 Simucredit = £0.396311 in 1900, so 1 Simucent = £0.00396311. This is
  the rate for one-off purchases and for monthly charges.
- The two rates differ by 76.09, which is the workbook's time compression. Using the wrong one
  changes a figure by two orders of magnitude.
- A third, separate factor applies to **monthly** charges: `calc_adjusted_monthly_figure`, which
  at this pakset's settings is 16 ÷ 8 = **2**. Any charge booked monthly through that function is
  doubled before it reaches the player.

Confirmed against an in-game tooltip in [balance-conversion-check](balance-conversion-check.md).

## The table

`£ per raw .dat unit` means: take the number in the `.dat` or `.tab` file as written, multiply by
the factor, and the result is 1900 pounds.

| Category | Where the value lives | Engine scale | Timescale | Monthly ×2 | £ per raw unit | Status |
|---|---|---|---|---|---|---|
| Way, bridge, tunnel, way-object **capital** | `.dat` `cost`, per tile | × 0.125, then × 8 tiles per km | capital | no | **0.00396311 per km** | verified |
| Way, bridge, **maintenance** | `.dat` `maintenance`, per tile per month | × 0.125, then × 8 per km | capital | **yes** | **0.00792622 per km per month** | verified |
| Scaled per-object **capital** (stations, platforms, signalboxes, signals) | `.dat` `cost` | × 0.125 | capital | no | **0.00049539 per object** | verified |
| Scaled per-object **maintenance** | `.dat` `maintenance` | × 0.125 | capital | **yes** | **0.00099078 per object per month** | inferred |
| Unscaled object **capital** (depots, headquarters, city buildings) | `.dat` `cost` | none | capital | no | **0.00396311 per object** | verified |
| Unscaled object **maintenance** | `.dat` `maintenance` | none | capital | **yes** | **0.00792622 per object per month** | inferred |
| Vehicle **purchase** | `.dat` `cost` | none | capital | no | **0.00396311 per vehicle** | verified |
| Vehicle **running** | `.dat` `runningcost` | none | revenue | no | **0.00005208 per km** | verified |
| Vehicle **fixed** | `.dat` `fixed_cost` | none | capital | **yes** | **0.00792622 per vehicle per month** | verified |
| Fares and goods values | `.dat` `value[1]` and class fields | none | revenue | no | **0.00005208 per unit** | verified |
| Land | `simuconf.tab` `cost_buy_land`, `cost_buy_city_land`, per tile | none; town multipliers ×6 capital, ×4 city, ×3 town | capital | no | **0.00396311 per tile** for `cost_buy_land` | partly verified |
| Corporation tax | `prices.tab` `corporation tax` | percentage, not a price | n/a | n/a | n/a | verified |
| Interest | `prices.tab` `base rate` plus the `simuconf.tab` margin | percentage, not a price | n/a | n/a | n/a | verified |
| Fuel | `fuel.tab` per fuel type, per kg / litre / kWh; `fuel_per_km` per km | ÷ 1000 | revenue | no | **0.00005208 per Simucent; a `fuel.tab` value is 192 × the price in pence per unit** | verified |
| Staff wages | annual old pence in `staff.tab`, one value per grade | × 10/3 | revenue | yes | **0.00010416 per stored unit per month** | verified |

## The three rules this table enforces

1. **Name the timescale before quoting a pound figure.** A pound figure is meaningless without it.
   The recurring error in this programme has been to mix a capital-rate figure with a revenue-rate
   one, which is how two 100-fold errors and one 2-fold error were made.
2. **Check the monthly factor separately from the timescale.** They are independent. A monthly
   charge takes the capital rate *and* is doubled; a per-kilometre charge takes the revenue rate
   and is not.
3. **A new money field is added here before it is used.** If a category is not in the table, its
   conversion is not known, and any figure derived from it is an assumption to be labelled as one.

## Fuel (resolved 2026-11-23)

`fuel.tab` holds one series per traction type, read at the current year with no inflation index, so
the series are nominal prices. The engine books `fuel_cost_per_unit × fuel_used ÷ 1000` Simucents,
the 1000 being `fuel_unit_cost_divider` in `New/config/simuconf.tab`.

The stored value is **192 × the price in decimal pence per unit of fuel** (per kg for coal, per litre
for liquid fuels, per kWh for electricity), so one stored unit is one Simucent of 1900 revenue money.
`fuel_per_km` is therefore in thousandths of that unit: grammes, millilitres or watt-hours per km.

The reading is confirmed against the series themselves: 192 × pence per litre reproduces £0.825 a
litre for diesel in 2000 and £1.65 in 2026; 192 × pence per kilogramme reproduces about 10s 6d a ton
for coal in 1900 and about £2.50 a ton in 1950. The earlier "pithead price in shillings per ton"
reading was a coincidence — one shilling a ton is 0.945 stored units per kilogramme — and it is
withdrawn. Figures per vehicle and per sector: [fuel-consumption](fuel-consumption.md).
`[CODE New ex-15 working tree @ 6d28e20d5]`

**Staff (resolved 2026-11-23).** `staff.tab` holds a monthly salary per person in Simucents. The
series is compiled as nominal annual old pence and converted at ×10/3: 1 old penny = 80 Simucents
at the revenue rate, divided by 12 months and by the engine's ×2 monthly factor. The previous file
held the annual-pence values unconverted, which is why 13,824 at 1900 charged £0.72 a month at the
revenue rate. The reconstruction, anchors and estimates are in
[staff-wages/reconstruction](staff-wages/reconstruction.md).

## What this replaces

These statements remain in their own documents because they explain a derivation, but the table
above governs:

- [infrastructure-base-costs](infrastructure-base-costs.md#the-conversion-chain) — the derivation
  from `set_scale_generic`, the tile count and the display division.
- [vehicle-cost-model](vehicle-cost-model.md) — what each vehicle field is charged for and when.
- [vehicle-cost/base-maintenance](vehicle-cost/base-maintenance.md#conversion) — the conversion
  applied to the measured maintenance series.
- [balance-conversion-check](balance-conversion-check.md) — the in-game confirmation.

## Open questions

- Is the scaled per-object maintenance doubled as well? The table says yes by inference from
  `finance_t::get_maintenance_with_bits`; no direct observation confirms it.
- Is land scaled by `meters_per_tile` at all? It is absent from `modifiable_station_buildings`, so
  the table says no, but the multipliers in town are a separate mechanism that is only partly
  verified.
- What are the `fuel.tab` units? That row remains open and blocks the fuel domain. The `staff.tab`
  row is resolved.
