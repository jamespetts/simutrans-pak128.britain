---
status: draft
verified: New ex-15 working tree @ 6d28e20d5
---
# Fuel consumption: water

**Covers**: the `fuel_per_km` and `calibration_speed` values of the 341 objects in `New/boats/`,
`New/boats/holds/`, `New/boats/boats192/` and `New/boats/boats224/`. Engine semantics and the unit
convention: [fuel-consumption](../fuel-consumption.md).

`fuel_per_km` is grammes of coal per kilometre for `steam`, and millilitres per kilometre for
`diesel`, `petrol` and `bio`. `calibration_speed` is the object's own service speed, which is the
pakset `speed` field. `range` is already set on many vessels and was not touched.

## What the 341 objects are

They are not 341 ships. 156 are self-propelled hulls and ships, 134 are payload hold modules
(70 with no engine type and 64 sail-rigged holds such as `BrigAdd*` and `CarferryAdd*`), and 51 are
independent unpowered or towed craft — dumb barges, tub boats, flyboats and the `TugBarge*` family.
Fuel goes only on the 122 objects that have their own engine; the other 219 are zero, which is
correct, because a dumb barge burns nothing.

## Method

- **Coal-fired steam**: `g/km = ihp × load factor × lb coal per ihp-hour × 453.592 ÷ speed in km/h`.
  The specific consumption is measured, not assumed, from a series that falls from 5.1 lb/ihp-hour
  for SS *Britannia* in 1840 through 3.8 for *Persia* in 1856, 2.11 for a 28-ship fleet average in
  1872, 1.522 for 28 three-stage expansion engines at sea in 1891, to about 1.25 by 1940. Small
  craft sit 55-75 per cent above the deep-sea series, anchored on the measured tug *Nubia* (2.0,
  1890) and ferry *Kookooburra* (2.84, 1907). `[LITERATURE:A Review of Marine Engineering, 1891, tables 5 and 6]`
  Load factors are 0.60 for reciprocating steamers, 0.75 for turbine steamers and 0.50 for the small
  craft whose coded speed is far below the engine's rated speed.
- **Diesel**: `mL/km = kW × load factor × specific fuel consumption ÷ 0.84 kg/L ÷ speed`. Consumption
  runs from 163-176 g/kWh for modern slow-speed two-stroke plant through 205-215 for 1950s-70s
  engines to 300 for 1905-1920 hot-bulb semi-diesels; load factors 0.40 for canal craft to 0.80 for
  fast craft. `[LITERATURE:MAN B&W engine programme; Wärtsilä 31 data]`
- **Petrol**: three hovercraft, by the same relation.

**Validation.** SS *Great Western* (1838) is independently documented as crossing the Atlantic in 15
days 5 hours on 400 of her 600 tons of coal, which is 26.3 t a day. The method gives 28.3 t a day,
within 8 per cent, and that is the best check the sector offers.

The full per-model table with a source key on every row, the power substitutions and the per-object
mapping: [water-derivation](water-derivation.md).

## Result

| Traction | Objects | Range of `fuel_per_km` |
|---|---:|---|
| coal steam | 53 | 1,990 g/km (steam narrowboat) to 303,325 g/km (SS *Great Eastern*) |
| diesel | 61 | 500 mL/km (diesel narrowboat) to 172,891 mL/km (HSS 1500) |
| petrol | 6 | 3,423-3,446 mL/km |

The two extremes are not errors: a narrowboat moves a few tonnes at walking pace and an ocean liner
of 18,900 tons displaces at 25 km/h.

## Two corrections made while applying the figures

- **`BTCLordWarden`**, a 1951 oil-fired steam turbine, is coded `engine_type=steam` because the
  pakset's convention codes turbine steamers as steam. Its researched figure is millilitres of oil
  per kilometre, which would be priced against the coal series and come out about fifteen times too
  cheap. It is stored as **184,600 g of coal-equivalent per km**, converted at 42.7 MJ/kg for oil and
  29.3 MJ/kg for coal. That is the energy normalisation that the comment at the head of
  `config/fuel.tab` already sanctions, and it charges the right sum while keeping the object's
  identity.
- **Three cargo variants of diesel craft carried `engine_type=steam`** — `LightweightDieselBargeOil`,
  `DieselNarrowboatOil` and `SemiDieselNarrowboatOil` — while all their siblings are diesel. The two
  lower-case ones are corrected to `diesel`; the third was `Diesel` with a capital D and is now lower
  case. Without the correction a diesel barge was priced as coal.

`SRInvicta` burned coal from 1939 to 1946 and oil from 1946 to 1952. It is modelled as coal, which is
what it burned for most of its life; period fidelity would need two objects.

## Gaps and doubts

- **Early steamer power ratings in the pakset are far too high.** About twenty steam models needed a
  horsepower substituted by the researcher because the code value is three to thirteen times the real
  installed power. Those are marked `ESTIMATE` in the report. Correcting the `power` field instead
  would change the game's acceleration and is a separate decision.
- No measured coal log was found for a Clyde puffer or a steam narrowboat; those cover six objects
  each.
- No operator fuel figure was found for the HSS 1500; its figure is 68 MW at a 0.65 load factor and
  may be about twice too high.
- The sanity check against `runningcost` passes for coal but not for liquid fuels, where fuel is
  hundreds of times maintenance. The cause is the pakset's ship maintenance costs, which are
  implausibly low and mutually inconsistent, and the fact that `fuel.tab` uses road diesel prices
  rather than marine bunker prices. Both are separate problems.

## Open questions

- Should marine bunker prices have their own `fuel.tab` entry? The diesel series is a road derv
  series and is dearer than bunker fuel.
- Should the ~20 impossible `power` values on early steamers be corrected, and if so, does that need
  a savegame-compatibility note?
