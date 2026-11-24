---
status: draft
verified: New ex-15 working tree @ 6d28e20d5
---
# Fuel consumption: aircraft

**Covers**: the `fuel_per_km` and `calibration_speed` values of the 230 aircraft in `New/air/`,
`New/air/air192/` and `New/air/air256/`, and the evidence behind them. Engine semantics and the unit
convention: [fuel-consumption](../fuel-consumption.md).

`fuel_per_km` is millilitres of fuel per kilometre at cruise: jet fuel for `engine_type=turbine`,
avgas for `petrol`. `calibration_speed` is the type's cruise speed, which for every aircraft in the
pakset is also its `speed` field, so the engine charges exactly `fuel_per_km` per kilometre in normal
line service. `cut_off_speed` is not set, because it has no effect when the calibration speed is the
maximum speed. `range` is already set on every aircraft and was not touched.

## Method

Three routes, recorded in the report's `basis` column:

- **Documented fuel burn per km on a stated sector**, converted to cruise. The tables in
  Wikipedia's *Fuel economy in aircraft* article compile Airclaims, Aircraft Commerce and airline
  submissions as kilogrammes per kilometre for a sector of stated length.
  `[LITERATURE:https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft]` Conversion: kilogrammes to
  litres at 0.80 kg/L, then a climb-and-taxi correction of 0.97 for sectors of 8,000 km or more, 0.93
  for 1,900-8,000 km, 0.90 for 900-1,900 km and 0.85 below 900 km. 23 models rest on this.
- **Power or thrust model**: fuel flow equals drag times specific fuel consumption, drag being weight
  divided by lift-to-drag ratio. Cruise weight is taken as the pakset `weight` times 1.35 for jets,
  1.30 for turboprops and 1.25 for piston types, adjusted on the types whose `weight` field is
  evidently loaded rather than empty. Engine cruise specific fuel consumption comes from the
  thrust-specific fuel consumption table and lift-to-drag ratios from the lift-to-drag article; piston
  types use 0.45-0.55 lb/hp/hour. `[LITERATURE:https://en.wikipedia.org/wiki/Thrust-specific_fuel_consumption]`
  `[LITERATURE:https://en.wikipedia.org/wiki/Lift-to-drag_ratio]` 85 models rest on this, and it
  reproduces the documented flows to within 25 per cent.

The full per-model derivation, with the cruise weight, lift-to-drag ratio and engine type used for
each model: [air-derivation](air-derivation.md).
- **Estimate**, for four models with no usable source: the 1910 mail monoplane, three Boeing 737
  variants, and the two smallest airships.

A cross-check on the piston and airship types is usable fuel capacity divided by published range,
which is fuel-limited on those types. It confirms the DC-3, the Ford Trimotor, the Handley Page
O/400 and the two large airships, and suggests the Junkers Ju 52 figure is about 30 per cent low.

## Result

Millilitres per kilometre at cruise: Junkers F 13 188, de Havilland Dragon Rapide about 400, Douglas
DC-3 1,233, Vickers Viscount 802 2,886, Airbus A320 3,639, Boeing 747-400 13,471, Concorde 13,996.
The spread is 188 to 14,081.

**Independent check.** The Simutrans forum thread *A snippet of relative pricing information* contains
one directly usable aircraft figure: an operator summary of an Airbus A340-300 at 271 t take-off
weight, cruising at one tonne of fuel per 70 nautical miles. That is 7.72 kg/km, or about 9.65 L/km,
which agrees with the modelled widebody rows. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.175]`

**Cost check.** Fuel cost per kilometre against `runningcost` scaled by the general price index is
1.16 for the Boeing 747-400 and 1.27 for the Airbus A320, which is the intended order. For small
types it is 3.2 for the DC-3 and 16.8 for the DHC-6 Twin Otter. The cause is the pakset's aircraft
maintenance costs, not the fuel figures: the Twin Otter's `runningcost` of 6 Simucents a kilometre is
far below any plausible maintenance cost.

## Gaps and doubts

- Jane's All the World's Aircraft could not be searched in full text, so the 1950s-1970s British jets
  — Comet, Trident, VC10, One-Eleven, Vanguard, Britannia — are modelled rather than documented.
- The pakset `weight` field mixes empty and maximum weights, which is the largest error in the
  modelled rows.
- The earliest aircraft and the two small Zeppelins rest on installed power and specific fuel
  consumption alone.
- Aircraft maintenance costs are evidently far too low for small types. This is a separate pass.

## Open questions

- Should the modelled rows be replaced once Jane's or the type flight manuals can be read in full?
- Is the pakset `weight` field meant to be empty or maximum weight? Six modelled rows carry an
  explicit correction factor because it is evidently the other one.
