---
status: draft
verified: New ex-15 @ 8d0603d81
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
| [fuel/oil-and-power](fuel/oil-and-power.md) | you need an oil, petrol, electricity or aviation price | gas oil, derv, industrial gas oil, petrol, industrial electricity, marine bunkers, aviation fuel, with the duty position stated |

## The long coal series

Clark and Jacks, "Coal and the Industrial Revolution, 1700-1869", *European Review of Economic
History* 11 (2007), table 1, column "'Pithead' average": decade averages for the northeast
coalfield in shillings per ton, 2.60 in the 1750s, 4.87 in the 1800s, 5.60 in the 1860s. It has a
stated method and standard error, and it is the only continuous pre-1770 series found. Its link
forward is Church's northeast pithead series for 1882-1913, which Clark and Jacks cite and which
has not been obtained.
`[LITERATURE:https://doi.org/10.1017/S1361491607001965]`

## An observation to verify

`fuel[steam]` in `config/fuel.tab` reads 10 at 1913 and 29 at 1919. Against the pithead series,
those numbers equal the price **per ton in shillings** (10s 1½d at 1913, 29s 4d at 1919), not a
price per kilogram. The file's own comment says the unit is kilograms. The two cannot both be
right, and the file's fuel consumption figures are in kilograms per kilometre.

This matters because it decides whether steam traction is charged the pithead or the delivered
price, which differ by the cost of moving coal to the depot. The arithmetic is recorded as an
observation, not as a claim about the intended unit; the unit question is open.
`[CODE New ex-15 @ 8d0603d81]`

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
