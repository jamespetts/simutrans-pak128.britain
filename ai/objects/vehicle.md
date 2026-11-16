---
status: draft
verified: New ex-15 @ 8b04b2114
---
# Vehicle objects

**Covers**: `Obj=vehicle` objects; trains, buses, trams, boats, and aircraft, including their
`.dat` definitions, images, and constraints.

## Initial facts

- `Obj=vehicle` is the most numerous object type in the pakset. `waytype=` values present are
  `track`, `road`, `air`, `water`, `tram_track`, `narrowgauge_track`, and `maglev_track`.
  `[CODE New master @ e36ec2321]`
- Vehicle source folders include `New/trains/` (subdivided into `carriages/`, `horses/`,
  `locomotives/`, `railcars/`, `wagons/`), `New/bus/`, `New/trams/`, `New/boats/`, `New/air/`,
  `New/maglev/`, `New/narrowgauge/`, `New/london-underground/`, and `New/livery-trains/`.
  `[CODE New master @ e36ec2321]`
- Vehicles use Simutrans-Extended's livery system; player colours are not currently used. See
  [liveries-and-special-colours](../graphics/liveries-and-special-colours.md).
  `[RECOLLECTION:2026-09-19]`
- Goods vehicles carry loaded-state image sets (empty, and one per cargo), indexed in the
  `.dat`; see [image-layout](../graphics/image-layout.md). `[RECOLLECTION:2026-09-19]`

## Related docs

- [liveries-and-special-colours](../graphics/liveries-and-special-colours.md) — read when adding or changing a livery.
- [image-layout](../graphics/image-layout.md) — read when indexing images, including loaded states.

## Folders by waytype

- Rail (`waytype=track`): `New/trains/` holds the `.dat` definitions; `carriages/`, `horses/`,
  `locomotives/`, `railcars/` and `wagons/` hold images. London Underground stock lives in
  `New/london-underground/`. `[CODE New master @ f8859c42d]`
- Road: `New/bus/`. Tram: `New/trams/`. Water: `New/boats/` with `holds/`, `boats192/` and
  `boats224/` size variants. Air: `New/air/` with `air192/` and `air256/` variants.
  Narrow gauge and maglev: `New/narrowgauge/`, `New/maglev/`.
  `[CODE New master @ f8859c42d]`
- `New/livery-trains/` holds per-livery `.dat` variants of rail vehicles and tenders.
  `[CODE New master @ f8859c42d]`
- The timeline is on (`use_timeline = 3`) from `starting_year = 1750` in
  `New/config/simuconf.tab`; see era coverage below. `[CODE New master @ f8859c42d]`

## Field reference

- Every field is explained in full in [vehicle-fields](vehicle-fields.md): identity and
  dates, economics, physics, capacity and comfort, operation and cabs, upgrades,
  obsolescence, and images. In brief: `cost`, `runningcost` and `fixed_cost` set purchase,
  per-kilometre and monthly costs; `speed`, `power`, `tractive_effort`, `weight` and
  `axle_load` drive physics and way limits; per-class `payload[i]` and `comfort[i]` set
  capacity; `intro_year` opens and `retire_year` closes new availability.
- Retirement ends production only: retired types cannot be bought new, but existing
  vehicles keep running. See [vehicle-fields](vehicle-fields.md).

## Constraints

- Coupling rules (`Constraint[Prev]`, `Constraint[Next]`, direction and cab flags) are
  explained in full in [coupling-constraints](coupling-constraints.md).
- Way access bits are explained in full in [way-constraints](way-constraints.md), including
  the meaning of each index in this pakset.

## Liveries and images

- `liverytype[i]` names the livery of each image set; `EmptyImage[direction][livery]` and
  `FreightImage` entries index into per-livery sheets. Full indexing rules:
  [liveries-and-special-colours](../graphics/liveries-and-special-colours.md) and
  [image-layout](../graphics/image-layout.md). `[CODE New master @ f8859c42d]`

## Rail vehicles: consists, coupling and liveries

- Consists are assembled from separately defined vehicles: locomotives, tenders, carriages
  and wagons coupled under the rules in [coupling-constraints](coupling-constraints.md).
  Fixed formations use per-position parts such as Front, Middle and Rear units.
  `[CODE New master @ f8859c42d]`
- Livery-train variants are separate vehicles whose names carry the livery in parentheses,
  for example `BR-Class43(FGW1)` in `New/livery-trains/br-cl43-a-fgw1.dat`, with a single
  image set and constraints naming same-livery partners such as `BR-Mk3-TO(FGW1)`.
  `[CODE New master @ f8859c42d]`
- Engine types on rail include steam, diesel, electric, petrol and bio.
  `[CODE New master @ f8859c42d]` Depots can be set to build only certain traction types.
  `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`

## Road vehicles, trams, boats, and aircraft

- Road vehicles (`New/bus/`) add tall and sidewalk classes, road wear contribution, load
  mixing bans, and operating range to the common fields; see
  [vehicle-fields](vehicle-fields.md). `[CODE New master @ f8859c42d]`
- Trams (`New/trams/`) use bidirectional running, rear-lead cabs, and way constraints; see
  [vehicle-fields](vehicle-fields.md) and [way-constraints](way-constraints.md).
  Their graphics process is the rail one; see
  [blender-rendering](../graphics/blender-rendering.md). `[CODE New master @ f8859c42d]`
  `[RECOLLECTION:2026-09-25]`
- Ships separate hulls from holds: a hull such as `BrigHull` carries no payload while hold
  vehicles such as `BrigAddPax` declare `Constraint[Prev]` on the hull and hold the
  `payload`, `comfort` and `catering_level` (see
  [coupling-constraints](coupling-constraints.md)). Other boats map cargo graphics with
  `freightimagetype[i]`, for example cement, coal and iron ore on `New/boats/box-boat.dat`.
  Ships use prohibitive way constraints for ship sizes and `override_way_speed`; see
  [vehicle-fields](vehicle-fields.md) and [way-constraints](way-constraints.md).
  Ship image offsets follow no single standard table: holds and the oversized
  (`boats192`/`boats224`) classes carry per-size offsets, while small base hulls generally
  carry none. `[CODE New master @ f8859c42d]` `[CODE New ex-15 @ 8b04b2114]`
- Aircraft (`New/air/`) add air resistance, operating range and minimum runway length, and
  omit rail-only running gear fields; see [vehicle-fields](vehicle-fields.md).
  `[CODE New master @ f8859c42d]`

## Road vehicle image offsets

- Rail vehicles carry no per-image offsets: no `.dat` in `New/trains/`,
  `New/london-underground/` or `New/livery-trains/` uses the `,x,y` modifier.
  `[CODE New ex-15 @ 8b04b2114]`
- Road vehicles (`New/bus/`) use one standard per-direction offset table on every image
  reference (sheets are 128x128 RGBA): E `,-33,14`; SE `,-13,0`; S `,0,0`; SW `,-8,10`;
  W `,4,5`; NW `,12,10`; N `,0,33`; NE `,0,24`.
  `[CODE New ex-15 @ 8b04b2114]`
- S is canonically `,0,0` for new work. `[RECOLLECTION:2026-09-25]` A minority of files
  carry `,4,0` in S instead; measured content framing is identical between the two batches,
  so the variant places the S sprite about 3 px differently rather than compensating a
  framing difference — treat it as superseded, not as an alternative standard.
  `[CODE New ex-15 @ 8b04b2114]` `[RECOLLECTION:2026-09-25]`
- Two tiny sidewalk vehicles carry bespoke offsets (`post-boy`, `man_on_bicycle`).
  `[CODE New ex-15 @ 8b04b2114]`
- Other classes: narrow-gauge vehicles carry no offsets (like rail); maglev vehicles carry
  bespoke per-vehicle offsets. `[CODE New ex-15 @ 8b04b2114]`

## Naming, dates and era coverage

- Names are the savegame identity (see [pakset-compatibility](../pakset-compatibility.md)).
  Base names use lowercase hyphenation such as `4-wheel-1870s-brake-unfitted`; class
  locomotives and units use prefixes such as `BR-`, `LMS-` or `GWR-`; unit parts append
  `Front`, `Middle`, `Rear`, `Pantograph` or similar; livery variants append the livery in
  parentheses. `[CODE New master @ f8859c42d]`
- Dates run from sailing ships in 1700 (for example `BrigAddPax` in
  `New/boats/holds/brig-holds.dat`) through the 1750 timeline start to current stock with
  introductions in 2025 and retirements into the 2030s. `[CODE New master @ f8859c42d]`

## Open questions

- Which engine fields govern vehicle behaviour in Simutrans-Extended (physics, wear, comfort),
  and where are they documented?
- Should this doc eventually be split into one doc per `waytype`?
- Ships and maglev carry per-size or per-vehicle offsets: is there a governing rule for
  either, or is each asset bespoke?
