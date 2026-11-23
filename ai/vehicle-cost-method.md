---
status: draft
verified: New ex-15 @ 33cf9b106
---
# Vehicle cost method

**Covers**: how to compare vehicle prices across eras and across classes when the vehicle itself
changes, and how to turn measured prices into the two things the pakset needs: a base level in
1900 terms and a year index.

Read with [vehicle-cost-model](vehicle-cost-model.md), which gives the engine mechanics, and
[prices-config](prices-config.md), which gives the index authoring rules.

## The problem

A price index needs a constant thing whose price is being tracked. A locomotive of 1830 and one
of 1910 are not the same thing: the later machine is larger, more powerful, built of better
material, and made to closer tolerances. Comparing their nominal prices and calling the
difference inflation measures a change in the product as well as a change in the price level.

The same applies within an era across classes, and it applies to carriages (four-wheel to bogie,
unfitted to corridor), wagons (wooden to steel, 8 tons to 20 tons) and road vehicles.

Two consequences for this project:

- A purchase-price index built from bare nominal prices is an upper bound on inflation, because
  part of every increase is quality.
- A base level set from "the price of a locomotive in 1900" is meaningless without saying which
  locomotive.

## The structural advantage this pakset has

Every vehicle in the pakset is a fixed specification. The `.dat` file states its weight, its
power or tractive effort, its capacity and its speed, and those do not drift: a given class is
one machine for its whole life. The quality problem therefore does not have to be solved inside
the index. It can be moved to the base level, once, where it can be done with the evidence in
front of us.

That suggests splitting the work:

1. **Base level.** Estimate what a vehicle of *this* specification would have cost in 1900. This
   is a cross-section problem, not a time-series one.
2. **Index.** Track the price of a *constant specification basket* from 1900 onwards. Because the
   specification is held fixed by construction, this is a matched-model index and needs no
   quality adjustment at all.

The rest of this doc sets out how to do each.

## Estimating the 1900 base level

### The price surface

Fit a price surface over vehicles of the 1890s and 1900s, using the attributes that the pakset
already stores:

`log(price) ≈ a + b·log(weight) + c·log(power or tractive effort) + d·log(capacity) + class terms + error`

- `weight` is the strongest single predictor for rail vehicles, because material content drives
  cost and the engine already gives weight for every vehicle.
- `power` or `tractive effort` separates a shunter from an express engine of the same weight.
- `capacity` separates a carriage from a van of the same weight.
- Class terms (locomotive, carriage, wagon, bus, lorry, ship, aircraft) absorb the parts of the
  cost that are not proportional to the attributes: fittings, finish, regulatory equipment.

The fit gives a predicted 1900 price for every pakset vehicle from its own specification. That
prediction is the base level, and it is comparable across classes because it is built from one
equation.

### What the fit needs

- Prices with a specification, not prices alone. A price with weight and power is worth ten
  without.
- A single decade of dense data, ideally 1895-1910, because that is where the pakset's index is
  100 by construction and where measurement error is smallest.
- Several builders or companies, so that one firm's costing convention does not set the surface.
- A handful of outlier checks: a very large and a very small vehicle of each class, to test
  whether the fit behaves outside the middle of the range.

The North Eastern Railway build records reproduced in the forum thread are close to ideal for
carriages and wagons: many vehicles, consecutive years, stated cost and stated layout. For
locomotives the thread carries individual class prices from 1897 onwards, which is thinner but
workable.

### Testing the surface

- Plot the residuals against year. If the specification explains the price, the residuals show
  no trend. A trend is the measure of how much of the price change was quality.
- Compare the implied price of a specified vehicle with a directly measured price of the same
  class where one exists. The surface should reproduce it.
- Check that the implied price per ton and per horsepower falls within the ranges the engineering
  literature gives for the period.

### The fitted locomotive ladder (2026-11-22)

The locomotive surface is now fitted rather than assumed. Two forms, both in 1900 GBP:

```
steam, before 1900     price = 107 x weight^0.86
steam, 1900 onwards    price = 132 x weight^0.86 x (power/600)^0.15
diesel / electric      price =  28 x power^0.889
```

`weight` is engine weight in tons as the `.dat` states it; `power` is the `.dat` power field.
The constants are least-squares fits in log space to the measured rows (Whishaw 1833-40; Planet
1831; Stirling 1870; Metropolitan A 1871; M7 1897; T9 1899; Stanier 4P/5MT 1934; A4 1936; 9F 1960;
Class 31/52/55/66/68). Class 57 is excluded from the diesel fit because it is a rebuild at about a
third of a new-build price.

**Why not a flat price per ton.** On the twelve steam rows, log price on log weight has an
elasticity of 0.86 and an R² of 0.91: a 10 per cent heavier engine cost about 8.6 per cent more,
so price per ton *falls* as engines grow. Adding power raises R² only to 0.93, and adding a year
term to 0.97. Across all traction, weight alone explains 0.70 and, once power is included, weight
becomes insignificant (power 0.889, R² 0.90) - diesels and electrics are priced by power and
electrical equipment, not by tonnage. The flat £32-78/ton ladder it replaces had a mean absolute
log error of 0.31 against the measured rows; the fitted ladder has 0.21.

**Caveats.** The fit rests on 12 steam and 5 diesel points, which is enough to fix the slope and
the order of magnitude, not to separate builders or specifications. The `.dat` weight may or may
not include the tender while the measured prices sometimes do, which is worth perhaps 10-20 per
cent at the light end. The era split at 1900 is a convention, not a measured break. Refit when
more points arrive; the scripts are `ai/temp/regress_locomotive_price.py`,
`ai/temp/analyse_price_per_ton.py` and `ai/temp/compare_ladders.py`.

### The fitted road ladders (2026-11-23)

The road ladders were refitted on complete vehicles only, because the old ones mixed chassis,
body and complete prices and a body is 42-45 per cent of a complete bus. All in 1900 GBP:

```
bus, complete        price = 1240 x (seats/50)^0.67          flat to 1990, then 1.40 by 2026
lorry, complete      price =  162 x payload^0.30 up to 7 t
                             x (payload/7)^0.75 above 7 t     real fall 1.8% a year to 1960,
                                                              then 1.40 by 2026
steam wagon          price =  300 x payload^0.464
battery-electric     price = diesel price x 2.10 for a bus or a lorry from 7.5 t
                             x 1.50 for a coach
                             x 1.25 for a van
```

The bus fit rests on 18 complete vehicles 1909-80 (mean absolute error 23 per cent) and the
lorry fit on 34 complete lorries and vans 1920-60 (15 per cent). The lorry exponent of 0.30
below the knee carries the fixed element the old `payload^0.60` ladder lacked: a 1.5-ton van
measures £160-210, not £58. Above 7 tons the measured 1960s and 1970s heavies require the
steeper 0.75 leg. The real trend is fitted on 1920-60 and held flat outside that range; the
post-1990 rise is carried by the modern level, measured from 59 tender awards and price lists.

Chassis-only and body-only measured rows are excluded from the match for road vehicles, and so
are option prices: a magneto at £12 and a diesel premium of £135 are additions to a chassis,
not the chassis. `[CODE ai/temp/evidence_data.py; research passes 29-30]`

### The road maintenance split (2026-11-23)

Maintenance is charged from a measured per-kilometre total, split 75 per cent to `runningcost`
and 25 per cent to `fixed_cost`. The per-kilometre anchors, in 1900 pence per km:

```
bus, 50 seats     1925 1.16   1955 0.37 (size^0.25)
lorry, 5 tons     1935 0.38   1955 0.21   1970 0.22   2016 0.20 (size^0.45)
```

The standing quarter is an **estimate**, not a measurement: no source found separates the
annual test, inspection, cleaning and body care from the mileage-driven repairs. The band is
15-35 per cent, and the reference annual distance at which the total becomes the two charges
is 50,000 km (bus), 40,000 km (lorry) and 25,000 km (van). Each row prints the split, the
reference distance and the implied share of capital, so the assumption is visible wherever the
figure is used. `[CODE ai/temp/evidence_data.py; research pass 31]`

### Comment-derived adjustments (2026-11-23)

The pakset's `.dat` comments carry the authors' historical notes, and a scan of all 25,113
comment lines produced 1,022 with a qualitative judgement, of which 80 made a comparative claim
worth an adjustment. The audit is `ai/temp/dat-comment-audit.md`; the accepted rows are tagged
`dat comment audit 2026-11-23` in `vehicle-adjustments.csv`.

Two rules came out of it.

1. **An adjustment must land in the field the claim is about.** Five of the proposed rows were
   dropped because the claim was about *fuel economy* — "30 lbs of coal per mile against 40 for
   the saturated equivalent", "especially economical", "expensive on fuel". The engine charges
   fuel separately from `config/fuel.tab` and the vehicle's `fuel_per_km`, so putting a coal
   saving into `runningcost` or `fixed_cost` would place it in the wrong account and double
   count. Those comments are evidence for a future `fuel_per_km` calibration, not for the cost
   fields.
2. **A specific row must carry the maker multiplier it displaces.** The adjustment engine
   applies only the longest matching row and never stacks. A new `guy-arab` row therefore has
   to carry the existing `guy` capital multiplier of 0.97 as well as its own maintenance
   credit, or the maker effect is silently lost.
3. **A comment that states a price is not an adjustment.** "These were very cheap: £155 in
   1923" is an individual price and belongs in the register, not in a 10 per cent multiplier.
4. **Where a measured capital price exists, the capital multiplier does not apply to it.** The
   percentage stays on the class ladder, which is the fallback for variants with no price, and
   only the maintenance multiplier continues to apply to the measured object. The Leyland
   National is the worked case: the audit gave the family capital 1.000 and maintenance 1.100,
   and the measured £9,500 of 1971 is bound as the capital figure through an explicit manual
   entry, because the matcher cannot link a long measured name to the short object names.

Comment evidence ranks below literature: 20 of the claims cite a source and are tagged
SOURCED, 60 are the authors' own assertions and are tagged AUTHOR, and the band is capped at
15 per cent. `[CODE ai/temp/dat-comment-audit.md; New/ai/cost-balancing/vehicle-adjustments.csv]`

### Feature premiums in the workbooks (2026-11-22)

The class ladders are fitted to samples of mixed specification. A vehicle that records a priced
option is adjusted by the measured premium for that option against the same vehicle without it,
so the ladder level stays the anchor and the premium carries the specification. The factors
applied are from research pass 8, which rests on same-vehicle option prices and same-model pairs:

| Feature | Factor | Applied to | Evidence |
|---|---|---|---|
| Automatic transmission | ×1.15 (semi-automatic ×1.08 is not separately recorded) | road vehicles with `transmission=automatic` | Bristol RELL 1966; ERF 1965 |
| Air suspension | ×1.06 | road vehicles with `suspension=air` | Bristol RELL, £206 on £3,335 |
| Saloon heating | ×1.04 | buses with `heating=yes` | Bristol RELL exhaust heater |
| Air conditioning | ×1.08 road, ×1.10 rail | rows with `aircon=yes` | ITDP norm; Pullman enquiry |
| Low floor | ×1.03 | road vehicles with `low_floor=yes` | Scania 1995; ITDP; TRL |
| Corridor | ×1.02 | carriages with `corridor=yes` | NER 1906 and 1910/11 pairs |
| Sleeping car | ×2.2 | carriages with `sleeping=yes`, or a `sleep` name | Jenkinson averages |
| Tram articulation | ×1.30 | trams with `articulated=yes` | structure and capacity, inferred |

The already-applied premiums are the diesel, trolleybus and steam road factors; carriage
dining/kitchen ×1.45, buffet ×1.15, bogie ×1.20 and steel panelling ×1.25; and the steam
locomotive superheat, compound, cylinder and Caprotti factors. `[LITERATURE: research pass 8,
"Recommended multiplier table"; Bristol RELL list, 4 November 1966; NER carriage records 1905-34]`

Two rules keep the premiums from double-counting. A blank feature cell is the baseline: the
factor applies only where the feature is explicitly recorded, so an unrecorded feature receives
no premium and the result is a lower bound. A factor is not applied where the ladder already
prices the feature through its size measure: bus deck type, for example, is left out because the
capacity term already prices the extra seats. The factors are small-sample estimates; the
ranges in research pass 8 are the uncertainty band, not a confidence interval.

## Building the index from 1900

With the base level fixed, the index only has to move a constant basket. Three routes, in order
of preference:

1. **Matched models.** The same class, diagram or specification priced at two or more dates:
   repeat orders, rebuilt classes, the same builder supplying the same design later. This is the
   cleanest evidence and needs no statistics. The North Eastern dining cars of 1905 and 1925, and
   the G.E. Section carriages of 1923-29, are matched-model evidence of this kind.
2. **Matched specifications across classes.** Where no single vehicle was built twice, compare
   vehicles of similar weight, power and capacity at different dates, and take the ratio after
   allowing for the attribute differences with the surface above.
3. **Published deflators.** Use a transport equipment or capital goods price index as the
   backbone, and correct it with the matched-model evidence where the two disagree. The deflator
   is the only route for eras with no vehicle-level prices, and it is the check on everything
   else.

The index should be presented with its evidence, not as a single line: the matched-model points,
the deflator, and the final choice, so that a later reader can see which parts are measured and
which are carried by the deflator.

## Traps

- **Weight and era are correlated.** Later vehicles are heavier and dearer. A regression that
  omits one of them attributes the whole joint movement to the other. Always fit them together,
  and read the era term only after the attributes are in the model.
- **Currency form.** Guineas, shillings and pence, and dollars for imported ships and aircraft.
  Record as stated; convert once, at the point of use, not in the evidence table.
- **Basis.** A contract price for a batch, a build cost from company accounts, a tender price and
  a second-hand price are four different things. The batch price per vehicle is not the marginal
  cost of one more vehicle.
- **Scope of the figure.** Some records include the boiler, some the tender, some the electrical
  equipment, some the body only. A carriage record that excludes bogies or a locomotive record
  that excludes the tender is not comparable with one that includes them. The evidence table
  records the scope; the fit must use only like with like.
- **Wartime and reconstruction.** 1914-1920 and 1939-1948 are not usable as ordinary price points
  without an explicit statement of what was being bought and at what controlled price.
- **One index, many vehicle types.** The engine applies a single `vehicle purchase` index to
  every vehicle. Cars, lorries, buses, locomotives, ships and aircraft did not move together.
  The index is therefore a weighted compromise, and the weights must be stated: they are the
  pakset's own mix of vehicles by era, not the national economy's.
- **The existing `.dat` values and the calibration workbook are not evidence.** The workbook
  applies a division by 8 to vehicle capital and by 4 to the monthly figure that the engine does
  not perform; the engine charges the `.dat` figure with only the price index applied. See
  [vehicle-cost-model](vehicle-cost-model.md). The values are to be replaced, not adjusted.

## What the output looks like

- A table of measured prices by class and year, with specification and source.
- A fitted 1900 price surface, with its coefficients and residuals.
- A base price for every pakset vehicle, derived from its own specification.
- A matched-model index from 1900, with the deflator beside it.
- A statement of the vehicle mix used to weight the single index, and of what the index cannot
  represent.

## Open questions

- Is the 1895-1910 evidence dense enough to fit one surface across all classes, or does each
  class need its own equation with a shared era term?
- Do the pakset's weights include the tender, the load or the crew? The specification used for
  the surface must match what the `.dat` weight means, or the price per ton will be inconsistent.
- Should ships and aircraft be inside the same index at all, given that their prices moved for
  reasons (steel, marine engines, aero engines) that have little to do with railway practice?
