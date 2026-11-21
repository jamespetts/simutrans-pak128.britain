---
status: draft
verified: none
---
# Comfort calibration

**Covers**: how passenger comfort is calibrated across every vehicle type: what the numbers
mean, the anchor vehicles, the line that relates maximum comfortable and maximum tolerable
journey times, the method per vehicle type, and the register of calibrated vehicles.
Children: [private cars](comfort/private-cars.md), [player vehicles](comfort/player-vehicles.md)
(rail, road, air and sea), and the [register](comfort/comfort-table.md).

## What the number means

- Comfort is a **journey time in minutes**: the maximum comfortable journey time for that
  accommodation. Revenue falls once the journey exceeds the passengers' tolerance; above
  tolerance a luxury bonus applies ([class](class.md)).
- **Private cars** carry it as two fields, `maximum_comfortable_journey_minutes` and
  `maximum_tolerable_journey_minutes` (or their `_tenths` forms). Omitted or 0 gives the engine
  defaults: 180 comfortable minutes and three times the comfortable time as tolerable
  ([citycar](objects/citycar.md#fields-one-objcitycar-per-colour)). The engine default is not the
  calibrated line: citycars carry explicit values on the line below.
- **Player vehicles** carry it per accommodation class as `comfort[i]`, in the same minutes
  ([vehicle-fields](objects/vehicle-fields.md)). The tolerable time is currently an engine-wide
  table in `config/simuconf.tab`, not a per-vehicle field, so the tolerable column in the
  register is a **calibration target** for player vehicles until the schema supports it.
- The historic **0–255 comfort rating** is the same quantity with a schema cap. Values were
  written as bare ratings; the cap is a limit of the old field, not a calibration boundary, and
  long-journey stock can legitimately want more than 255 minutes.

## Anchors

| Vehicle | Comfortable | Tolerable | Role |
| --- | --- | --- | --- |
| BMC Mini | 40 | 390 | **Low-end anchor, not a floor.** Motorcycle outfits and older or less comfortable cars sit below it. `[USER-DIRECTION:2026-11-15]` |
| Ford Sierra | 120 | 510 | Middle-of-the-road comfortable car. `[USER-DIRECTION:2026-11-15]` |

The Mini and Sierra are calibration points, not limits. A vehicle harsher than the Mini is
expected, and its value records how much harsher.

## The line

`tolerable ≈ 330 + 1.5 × comfortable` minutes, rounded to the nearest minute and capped at 600.

Both anchors lie on it (Mini 390, Sierra 510). It is the default for every motor vehicle.
Horse-drawn passenger carriages use `tolerable ≈ 240 + 4 × comfortable`, capped at 600; working
carts use `tolerable ≈ 180 + 6 × comfortable`, capped at 300. A closed landau is a private
carriage, not a lowly cart: coaching passengers travelled six to ten hours a day, so its limit is
passenger endurance, not the horse. A motor vehicle that deviates records the reason in its note:
an open motorcycle outfit takes a flat −30, a luxury saloon or a sleeper may take a bonus. The
2026-11-15 values (Mini 240, Sierra 360) are superseded by the 2026-11-20 recalibration; the
evidence is in the private-car audit of that date.

## Method per type

- [Private cars](comfort/private-cars.md) — citycars, including motorcycle outfits.
- [Player vehicles](comfort/player-vehicles.md) — rail, road, air and sea; the old rating and
  the migration to explicit times.
- [Register](comfort/comfort-table.md) — every calibrated vehicle, with intro and retire years
  and the reason for its values.

## Open questions

- Does ex-15 support per-vehicle tolerable times for player vehicles, or only the global
  `simuconf.tab` table? The register records targets either way.
- How should the 0–255 cap be handled for long-journey stock once the explicit fields are
  available: raise the cap, or migrate those vehicles first?
- Does the raised tolerance (330 + 1.5 × comfortable, cap 600) make citycars too competitive on
  long trips? They carry no running cost, so comfort is currently the only brake. Test on a
  large map before treating the line as final.
- Should the motor-car intercept differ for player vehicles? It is calibrated on cars; a
  first-class sleeper and a motorcycle outfit both use it with an explicit deviation.
