---
status: draft
verified: New ex-15 working tree @ 6d28e20d5
---
# Fuel consumption: steam

**Covers**: the `fuel_per_km` and `calibration_speed` values on every steam-powered rail vehicle in
`New/trains/`, `New/livery-trains/`, `New/narrowgauge/`, `New/london-underground/` and `New/trams/`,
and the working paper behind them. Engine semantics and the unit convention: [fuel-consumption](../fuel-consumption.md).

Steam ships are in [water](water.md) and steam road vehicles in [road](road.md); both are priced from
the same grammes-of-coal unit.

## The source

`New/steam-physics-calcs.ods`, sheet `Extrapolation`. It is the pakset's existing steam locomotive
physics paper; the `power` values of many steam locomotives in the `.dat` files were taken from its
`Power kW` column. `[CODE New ex-15 working tree @ 6d28e20d5]`

The sheet holds one row per locomotive or locomotive variant, 372 rows, 1813 to 1957, with:

| Column | Meaning | Unit |
|---|---|---|
| B | locomotive | — |
| E | maximum speed | km/h |
| F | calibration speed, formula `= E / 2` | km/h |
| G | grate area | sq ft |
| N | calorific value of the coal assigned to that row | kWh/kg |
| O | fuel burn, either typed in or derived | kg per hour per sq ft of grate |
| P | thermal efficiency, either typed in or derived | percent |
| M | power, either typed in or formula `MIN(G×O×N×P, heating surface limit)` | kW |
| S | fuel capacity | tonnes |
| T | fuel consumption, formula `= O / F × G` | kg/km |

The physical model is therefore: **coal burned per hour = grate area × the measured burn rate for
that class**, and **coal per kilometre = that hourly rate ÷ the speed it was measured at**. The
efficiency column is mostly derived from the power, and where the efficiency is the input the power
is derived from it. `[CODE New ex-15 working tree @ 6d28e20d5]`

## Coal types

The sheet assigns a calorific value per row from its own `Theoretical figures` sheet, which cites
8.076 kWh/kg for coke, 8.115 for Yorkshire bituminous, 9.078 for Welsh steam coal, 6.784 for
sub-bituminous and 6.053 for American coal. `[CODE New ex-15 working tree @ 6d28e20d5]`

The assignment it makes is: coke for every row up to 1842, when the smoke prohibition still forced
coke; Welsh steam coal for the Great Western and for most London, Brighton and South Coast and London,
Tilbury and Southend rows; bituminous for everything else. That assignment is kept, and each `.dat`
now records which coal its figure assumes.

**The mass figure does not depend on the coal type.** The grate limits mass throughput, so a
locomotive burning a higher-calorific coal does not burn fewer kilogrammes per hour at full firing; it
raises more steam from the same mass. The coal type therefore enters the economy through the price
per kilogramme, not through `fuel_per_km`. This matters because the pakset has one coal price series
and cannot charge a Welsh premium separately; see [the note on the price series](#the-price-series).

Two corrections were made to the sheet's assignment:

- **27 rows dated 1941-1957 are marked 6.784 kWh/kg.** Those are British main-line classes, and the
  sheet uses 8.115 or 9.078 for the same railways before 1941 and after 1957. The 6.784 value is
  treated as a sheet error and those rows are recorded as bituminous, or as Welsh for the Great
  Western rows. `[UNVERIFIED]` The change does not alter any `fuel_per_km`, because those rows all
  have a grate area and a typed burn rate; it alters only the efficiency the sheet reports for them,
  and hence the derived power.
- **One row, L&TSR 1 Class, carries 9.12 kWh/kg**, which is 9.078 rounded differently. It is treated
  as Welsh.

## Corrections to the sheet's own figures

Three defects in the sheet had to be worked around before its numbers could be used.

- **18 rows carry a cached `kg/km` that disagrees with the sheet's own formula**, by between −90 per
  cent and +125 per cent. The cause is a value edited after the cached result was stored, usually the
  maximum speed. The formula value `grate × burn rate ÷ calibration speed` is used instead.
- **14 rows have no grate area**, so neither the burn rate nor the efficiency is defined and the
  sheet's `kg/km` is `#VALUE!`. For those, coal burned per hour is derived as
  `power ÷ (calorific value × efficiency)`, with the efficiency interpolated from the sheet's own
  efficiency curve at that row's year. The curve runs from 1.13 per cent in 1813 to 6.6 per cent in
  1957. All 14 are 1833-1859 classes.
- **Three classes have no row at all**: the Southern Railway Leader, and the two LNER steam railmotors
  of 1924 and 1928. The Leader is derived from its own 25.5 sq ft grate at the 1949 burn rate; the
  railmotors from their power at 5.6 per cent efficiency.

## Calibration

`calibration_speed` is set to each vehicle's **maximum speed**, not to the sheet's half-maximum
figure. The reasoning is in [fuel-consumption: the design rule](../fuel-consumption.md#the-design-rule):
the engine charges `fuel_per_km` per kilometre at part load at any speed up to the calibration speed,
so the calibration speed is what turns the sheet's "kilogrammes per kilometre at about half maximum
speed" into the flat per-kilometre charge. `fuel_per_km` is the sheet's figure in grammes, rounded to
the nearest 10 g.

The one steam locomotive that already carried fuel figures, the GNR Stirling 8 ft single, held
`fuel_per_km=7650`, `calibration_speed=75`, `cut_off_speed=40` — the unmodified sheet values. It now
carries `7660` at `calibration_speed=135`, and its `cut_off_speed` is removed.

## Result

390 objects carry a figure; the other 52 steam objects in those folders are tenders, the middle and
rear units of Garratts, and other unpowered parts, and are correctly left at 0. Fuel consumption by
the decade the class was introduced:

| Introduced | Classes | Median | Lowest | Highest |
|---|---|---|---|---|
| 1800-1819 | 3 | 16000 | 6300 | 17540 |
| 1820-1839 | 16 | 9325 | 4930 | 19280 |
| 1840-1859 | 37 | 8790 | 5980 | 17590 |
| 1860-1879 | 68 | 9410 | 1590 | 20540 |
| 1880-1899 | 66 | 9975 | 1720 | 17790 |
| 1900-1919 | 94 | 11730 | 4530 | 19100 |
| 1920-1939 | 78 | 13005 | 6150 | 33930 |
| 1940-1959 | 28 | 13520 | 8350 | 23020 |

Named classes, in grammes of coal per kilometre: LMR Rocket 5500, GNR Stirling 8 ft single 7660, GWR
Castle 10170, LNER A4 16270, LMS Black Five 12650, BR Standard 9F 23020, LMS Garratt 33930.

Checked against the published coal consumption of the same classes, 1 kg/km is 3.55 lb per mile. The
Castle's 10.17 kg/km is 36 lb per mile against a published 30-40; the A4's 16.3 is 58 lb against
45-65 at speed; the Black Five's 12.65 is 45 lb against about 40-45; the 9F's 23.0 is 82 lb against
about 60-70, the worst fit in the set. `[PRIOR]`

As an end-to-end check, a Black Five in 1950 is charged 13.3 old pence a mile for coal at the 1950
price in `fuel.tab`, against a published coal cost of roughly 12-15 pence a mile. That is the
strongest single validation of the unit convention and of the price series together.

## Range

`range` is set on 175 of the 390 objects: **the coal range at full bunker**, computed as the class's
fuel capacity divided by `fuel_per_km` and recorded in the same comment line. It runs from 144 km
(GWR railmotor, 0.76 t) to 924 km, median 360 km. The other objects are tenders, or classes whose
sheet row records no fuel capacity.

The value is the coal in the bunker, so on a tender engine it is the coal in its standard tender. The
pakset's coupling constraints fix the tender for each class, so a locomotive cannot be given a larger
one to extend the range.

Three limits on the figure:

- It is the **coal** range. Water was often the binding constraint in service, and the sheet records
  no water capacity, so a water range cannot be derived from it. A locomotive working hard would need
  water before it needed coal.
- It is the theoretical capacity divided by the service consumption: no allowance is made for coal
  left unburnable in the corners of the bunker or for a fire built up at the end of a turn.
- It was withheld until replenishment was added to the engine, because nothing in the engine restores
  a range — `vehicle_t::replenish()` is never called — so a range is a permanent cap on the distance
  to the next scheduled stop with no way to comply. With replenishment, the cap becomes a real
  operating constraint that a stop satisfies.

## The price series

`fuel[steam]` in `config/fuel.tab` reads as 192 × pence per kilogramme, which is the same unit as the
rest of the file. Three observations on it, none of them changed here because the price series is
owned by [fuel-evidence](../fuel-evidence.md):

- The apparent agreement between the series and the pithead coal price **in shillings per ton** is a
  coincidence of the imperial and decimal systems: one shilling a ton is 0.945 stored units per
  kilogramme. The series is a price per kilogramme.
- The 1968 value, 55, implies £2.91 a ton between 1959 (£4.55) and 1971 (£5.73). A price cannot halve
  and recover; the value is wrong, and interpolation between its neighbours gives about 103. The
  error affects steam only from 1968, which is the last years of the Clyde puffers.
- The series has no 1920 spike, although the average pithead price reached 48s 7d that year against
  29s 4d in 1919.
- Before about 1840 locomotives burned coke, which cost more per ton than coal. The early part of the
  series is a coal price, so the coke era's fuel cost is understated.

## Open questions

- Should the sheet's 18 stale cached values be fixed in the spreadsheet itself, so that the paper and
  the `.dat` files agree? The `.dat` files now hold the formula values.
- The sheet's power column for the 1941-1957 classes is 20 per cent low as a direct consequence of
  the 6.784 calorific value. Correcting it would raise the `power` of 27 classes and change their
  acceleration; that is a physics change outside this work.
- Is the GWR's Welsh coal really priced correctly? Its calorific advantage (9.078 against 8.115) and
  its price premium are of the same order and roughly cancel, so charging Welsh coal at the
  bituminous price is a small error, but it is an error and it is not measured.
- The sheet records no tender water capacity, so the water-limited range — the figure that actually
  bound in service — cannot be derived from it.
