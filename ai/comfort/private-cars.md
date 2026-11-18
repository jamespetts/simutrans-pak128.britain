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

1. **Start from the line.** `tolerable ≈ 180 + 1.5 × comfortable`, rounded to 5 minutes
   ([comfort-calibration](../comfort-calibration.md#the-line)).
2. **Set the comfortable time from the car itself**: era, size and class, suspension and
   refinement, seating, noise and weather protection. The Mini (40) and Sierra (120) are the
   calibration points; interpolate between them and beyond.
3. **Below the Mini is normal.** The Mini is a low-end anchor, not a floor: motorcycle outfits,
   cycle cars, early light cars and worn utility models legitimately sit below 40. Record how
   far below and why. `[USER-DIRECTION:2026-11-15]`
4. **Apply the type deviation** where the body type justifies it: an open motorcycle outfit
   takes **line − 30** because the rider and passenger are exposed; a closed luxury saloon may
   take a bonus.
5. **Every colourway shares the model's values.** Set them once per model.
6. **Record the reason** in the `.dat` header: the anchors used, any deviation, and the
   feature that justifies it.

## Motorcycle outfits

| Outfit | Comfortable | Tolerable | Reason |
| --- | --- | --- | --- |
| BSA 557 + Type 1 (1921–32) | 20 | 180 | rigid frame, sprung saddle only, leaf-sprung open chair |
| BSA Sloper + open chair (1930–39) | 25 | 190 | girder fork, sprung saddle, no rear suspension, open chair |
| Norton Big Four WD (1940–48) | 25 | 190 | rigid military outfit, open tub |
| BSA M21 + Maxstoke (1946–66) | 25 | 190 | post-war plunger frame but an open chair |
| BSA M21 + Monaco (1960–68) | 35 | 200 | sprung sidecar wheel and low sports body, still open |

All five are line − 30. The comfortable times differ by era and chair quality; the tolerable
times follow the same penalty so the class stays comparable.

## Notes on the register

The [register](comfort-table.md#private-cars) lists every citycar model with its intro and
retire years. Its note column records the relationship to the line (`line`, `line +5`,
`open outfit: line − 30`); the model-specific reasoning is in each `.dat` header. Models added
before 2026-11-15 were checked against the line and are consistent with it, but their original
reasoning was not always written down; treat their notes as provisional until reviewed.

## Open questions

- Should the outfit penalty stay a flat 30 minutes, or scale with the comfortable time (for
  example 25%)?
- Do horse-drawn vehicles belong on the same line as motor cars, or do they need their own
  anchor? They currently follow it.
