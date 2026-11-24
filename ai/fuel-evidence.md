---
status: draft
verified: New ex-15 @ 687347620 (working tree), 2026-11-24
---
# Fuel evidence

**Covers**: published British fuel and energy prices by fuel and year, for `config/fuel.tab`, which
prices fuel separately from vehicles by fuel and engine type.

The engine charges fuel outside the vehicle money fields: `fuel.tab` holds one series per traction
type, and a battery or fuel-cell vehicle buys electricity divided by its round-trip efficiency.
`[CODE New ex-15 @ 8d0603d81]`

## Documents

| Document | Read when | Contents |
|---|---|---|
| [fuel/coal](fuel/coal.md) | you need a coal or town gas price | northeast pithead decade averages from the 1700s, district prices for 1860, pithead proceeds 1913-1944, bunker and shipment coal, delivered industrial coal 1993-2025 |
| [fuel/coke](fuel/coke.md) | you need a coke price, or are pricing a coke-burning tramway or railway | gas coke and furnace/foundry coke by decade 1846-2026 with the basis of each figure, the 1.5-2.5x coke:coal ratio, and the grade rule |
| [fuel/oil-and-power](fuel/oil-and-power.md) | you need an oil, petrol, electricity or aviation price | gas oil, derv, industrial gas oil, petrol, industrial electricity, marine bunkers, aviation fuel, with the duty position stated |

## The long coal series

Clark and Jacks, "Coal and the Industrial Revolution, 1700-1869", *European Review of Economic
History* 11 (2007), table 1, column "'Pithead' average": decade averages for the northeast
coalfield in shillings per ton, 2.60 in the 1750s, 4.87 in the 1800s, 5.60 in the 1860s. It has a
stated method and standard error, and it is the only continuous pre-1770 series found. Its link
forward is Church's northeast pithead series for 1882-1913, which Clark and Jacks cite and which
has not been obtained.
`[LITERATURE:https://doi.org/10.1017/S1361491607001965]`

## The unit, resolved

`fuel[steam]` reads 10 at 1913 and 29 at 1919, and the file's own comment says kilograms. Read as
192 × the price in decimal pence per kilogramme, those values give 10s 6d a ton in 1913 and 30s 8d in
1919, against a pithead series that records 10s 1½d and 29s 4d. Read instead as a price per ton in
shillings, they give exactly the same figures. The two readings are numerically almost identical
because one shilling a ton is 0.945 stored units per kilogramme, a coincidence of the decimal penny
and the 2,240 lb ton, and they separate by only about 5 per cent across the whole series.

The unit is therefore thousandths of a fuel unit per km for `fuel_per_km`, with the price per
kilogramme, litre or kWh in `fuel.tab`. The convention and its verification against the rest of the
file are in [conversion-chains](conversion-chains.md#fuel-resolved-2026-11-23); the consumption
figures that depend on it are in [fuel-consumption](fuel-consumption.md). `[CODE New ex-15 working tree @ 6d28e20d5]`

Two defects in the steam series remain, and are recorded rather than fixed:

- The 1968 value, 55, implies £2.91 a ton between 1959 (£4.55) and 1971 (£5.73). Interpolation between
  its neighbours gives about 103.
- The series has no 1920 spike, although the average pithead price reached 48s 7d that year against
  29s 4d in 1919.

## Gaps

- No railway contract or delivered-to-depot coal price for any year.
- Coal 1861-1912.
- Town gas and electricity before 1950.
- Marine bunker oil.
- No power-by-the-hour or contract fuel rate.

## Open questions

- What unit does `fuel[steam]` actually use, and does the engine divide it by the thousand as the
  file comment says?
- Should fuel.tab carry the pithead price, the delivered price, or a delivered price net of the
  infrastructure cost of coal handling that the pakset models elsewhere?
