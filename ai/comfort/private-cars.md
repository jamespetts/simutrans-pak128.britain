---
status: draft
verified: none
---
# Comfort calibration — private cars

**Covers**: how `maximum_comfortable_journey_minutes` and
`maximum_tolerable_journey_minutes` are set for `Obj=citycar` objects, including motorcycle
outfits. Parent: [comfort-calibration](../comfort-calibration.md). Register:
[comfort-table](comfort-table.md#private-cars). Field definitions:
[citycar](../objects/citycar.md#fields-one-objcitycar-per-colour).

## Method

1. **Start from the line.** `tolerable ≈ 330 + 1.5 × comfortable`, rounded to the nearest
   minute and capped at 600 ([comfort-calibration](../comfort-calibration.md#the-line)).
2. **Set the comfortable time from the car itself**: era, size and class, suspension and
   refinement, seating, noise and weather protection. The Mini (40) and Sierra (120) are the
   calibration points; interpolate between them and beyond.
3. **Below the Mini is normal.** The Mini is a low-end anchor, not a floor: motorcycle outfits,
   cycle cars, early light cars and worn utility models legitimately sit below 40. Record how
   far below and why. `[USER-DIRECTION:2026-11-15]`
4. **Apply the type deviation** where the body type justifies it: an open motorcycle outfit
   takes **line − 30** because the rider and passenger are exposed; a closed luxury saloon may
   take a bonus.
5. **Horse-drawn passenger carriages use `tolerable ≈ 240 + 4 × comfortable`, capped at 600;
   working carts use `tolerable ≈ 180 + 6 × comfortable`, capped at 300.** A closed landau is a
   private carriage, not a lowly cart: coaching passengers travelled six to ten hours a day, so
   the closed carriage is 60/480, the open carriage 30/360 and the park drag 40/400; the working
   cart is 10/240.
6. **Every colourway shares the model's values.** Set them once per model.
7. **Record the reason** in the `.dat` header: the anchors used, any deviation, and the
   feature that justifies it.

## Motorcycle outfits

| Outfit | Comfortable | Tolerable | Reason |
| --- | --- | --- | --- |
| BSA 557 + Type 1 (1921–32) | 20 | 330 | rigid frame, sprung saddle only, leaf-sprung open chair |
| BSA Sloper + open chair (1930–39) | 25 | 338 | girder fork, sprung saddle, no rear suspension, open chair |
| Norton Big Four WD (1940–48) | 25 | 338 | rigid military outfit, open tub |
| BSA M21 + Maxstoke (1946–66) | 25 | 338 | post-war plunger frame but an open chair |
| BSA M21 + Monaco (1960–68) | 35 | 353 | sprung sidecar wheel and low sports body, still open |

All five are line − 30. The comfortable times differ by era and chair quality; the tolerable
times follow the same flat penalty so the class stays comparable. The penalty is absolute, not
proportional: exposure costs a fixed number of minutes per hour whatever the seat.

## Horse-drawn vehicles

A closed landau is a private carriage with a folding hood, glazing, padded seats and springs. It
is not a lowly cart. The pakset's `HorseCarriageClosed` object displays as "Landau"; the open
`HorseCarriageOpen` object is the generic open carriage, and `HorseCart` is the working cart. Its
passengers travelled long days: London–York took 31 hours in 1796
with overnight stops, a Stamford coach covered 99 miles in 9 hours 4 minutes in 1807 including
meals, and by 1833 London–Shrewsbury (154 miles), Exeter (171) and Manchester (187) were done in
a day. A private carriage was slower than a mail coach but still a full-day vehicle.

| Vehicle | Comfortable | Tolerable | Reason |
| --- | --- | --- | --- |
| Closed landau | 60 | 480 | private sprung carriage, glazed and padded; a full coaching day |
| Open carriage | 30 | 360 | sprung but exposed to weather; a long day is possible in good conditions |
| Park drag | 40 | 400 | sporty open carriage for a day's outing, not a working vehicle |
| Working cart | 10 | 240 | hard seat, no springs, a working vehicle; short journeys |

Passenger carriages use `240 + 4 × comfortable`, capped at 600. The working cart uses
`180 + 6 × comfortable`, capped at 300. The cart is deliberately kept below the carriages: its
limit is the rider's tolerance of a hard, unsprung seat, not the horse's ability to walk on.

## Notes on the register

The [register](comfort-table.md#private-cars) lists every citycar model with its intro and
retire years. Its note column records the relationship to the line (`line`,
`open outfit: line − 30`, or `horse-drawn`); the model-specific reasoning is in each `.dat`
header. After the 2026-11-20 recalibration every motor car sits exactly on the line; only the
outfits carry the flat −30 note. Models added before 2026-11-15 were checked against the line,
but their original reasoning was not always written down; treat their notes as provisional
until reviewed.

## Open questions

- Does the raised tolerance make citycars too competitive on long trips? They carry no running
  cost, so comfort is the only brake on long private-car journeys. Test on a large map before
  treating the new line as final.
- Is the comfortable column itself right? The 2026-11-20 audit corrected five visible
  inversions (Rolls-Royce 20/25, Derby Bentley, Bentley Mk VI, Audi A4 B6, Mercedes S-Class
  W220); there may be more between 1955 and 1990 that the ratio screen did not catch.
