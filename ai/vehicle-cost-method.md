---
status: draft
verified: New ex-15 @ 8d0603d81
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
