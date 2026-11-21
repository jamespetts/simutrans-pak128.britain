---
status: stub
verified: none
---
# Comfort calibration — player vehicles

**Covers**: comfort for player-owned vehicles: rail, road (buses and coaches), air and sea.
Parent: [comfort-calibration](../comfort-calibration.md). Register:
[comfort-table](comfort-table.md#player-vehicles). Fields:
[vehicle-fields](../objects/vehicle-fields.md) and [class](../class.md).

Status: stub. The method below records the old system and the migration; the type anchors and
the register rows are not yet written.

## The old system (0–255 rating)

- Player vehicles declare `comfort[i]` per accommodation class. The value **is the maximum
  comfortable journey time in minutes**, not an abstract score: 69 means 69 minutes
  ([class](../class.md)).
- The field is capped at 255. The cap is a schema limit, not a calibration boundary; a
  long-distance or sleeper vehicle can legitimately want more.
- The tolerable time is **not per vehicle**: the engine derives it from the journey time through
  the table in `config/simuconf.tab` (10 up to 5 minutes, 50 to 60, 125 to 150, 165 to 360,
  250 to 1440 and above), so the register's tolerable column is a calibration target for these
  vehicles.
- The historical calibration work is in `Comfort calibration overview.ods` (sheets `Overview`
  and `All vehicles`) and `Exp-Cater-Comfort-Capacity.ods`; those are the old system's inputs,
  not canonical values ([balancing](../balancing.md)).

## Method for new and revised values

1. Set the comfortable time from the accommodation: seating, space, ride, noise, catering and
   service. A first-class carriage or a sleeper sits well above a commuter bench seat.
2. Derive the tolerable time from the line ([comfort-calibration](../comfort-calibration.md#the-line))
   unless the type justifies a deviation, and record the deviation.
3. Convert an existing 0–255 value by keeping its minutes, then check it against the line. A
   value that hits 255 is suspect: it may have been capped rather than chosen.
4. Record the value per class index; later indices repeat the previous value if omitted
   ([vehicle-fields](../objects/vehicle-fields.md)).

## Type anchors (to establish)

| Type | Comfortable anchor | Tolerable anchor | Status |
| --- | --- | --- | --- |
| Rail — commuter | not set | not set | to research |
| Rail — long distance / sleeper | not set | not set | to research |
| Bus / coach | not set | not set | to research |
| Air | not set | not set | to research |
| Sea | not set | not set | to research |

The car anchors (Mini 40/390, Sierra 120/510) are not appropriate for these types; each needs
its own reference accommodation, then the same line and deviation discipline.

## Migration plan

1. Extract `comfort[i]` for every player vehicle from the `.dat` files, per class.
2. Mark every value of 255 as capped and review it first.
3. Derive the target tolerable time and add it to the register.
4. Where the engine supports per-vehicle tolerable fields, migrate the `.dat` values; until
   then the register is the record of intent.

## Open questions

- Does ex-15 support per-vehicle tolerable journey times for player vehicles, or only the global
  `simuconf.tab` table?
- Which vehicle is the low-end anchor for rail, and which for buses and coaches?
- Should aircraft and ships use journey-time comfort at all in the same way, given that the
  journey is usually a single leg with no interchange?
