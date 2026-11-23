---
status: stub
verified: none
---
# Object types

**Covers**: the engine object types (the `Obj=` value in each `.dat`) used by the pakset. This
is the entry point to the per-type documentation.

Every pakset `.dat` declares its object type with an `Obj=` line. The types the engine knows,
and therefore the types the pakset can use, each have a child doc here. Some types are not
currently present in the pakset; they are recorded so that the type's scope and intent are not
lost. Read the child doc for the type a task touches.

Every new asset also requires translation texts (`New/text/en.tab` entries) as part of its
creation: [translations-and-text](translations-and-text.md). `[USER-DIRECTION:2026-11-15]`

## Type docs

- [vehicle](objects/vehicle.md) — read when touching trains, buses, trams, boats, aircraft, or any `Obj=vehicle`. Keys the [field reference](objects/vehicle-fields.md), [coupling constraints](objects/coupling-constraints.md), and [way constraints](objects/way-constraints.md) child docs.
- [building](objects/building.md) — read when touching any `Obj=building`; keys the city, public, and town hall child docs.
- [way](objects/way.md) — read when touching any `Obj=way` (track, road, tram, water, air, power). Keys the `elevated-ways` child doc.
- [bridge](objects/bridge.md) — read when touching `Obj=bridge`.
- [tunnel](objects/tunnel.md) — read when touching `Obj=tunnel`.
- [roadsign](objects/roadsign.md) — read when touching signals and signs (`Obj=roadsign`).
- [crossing](objects/crossing.md) — read when touching level crossings (`Obj=crossing`).
- [way-object](objects/way-object.md) — read when touching `Obj=way-object`.
- [tree](objects/tree.md) — read when touching `Obj=tree`.
- [citycar](objects/citycar.md) — read when touching private cars (`Obj=citycar`).
- [road-vehicle-lengths](objects/road-vehicle-lengths.md) — read when setting or checking a `length` field on a citycar or road vehicle, or when road vehicles queue with the wrong spacing.
- [pedestrian](objects/pedestrian.md) — read when touching `Obj=pedestrian`.
- [factory](objects/factory.md) — read when touching industries (`Obj=factory`). Keys the [factory fields](objects/factory-fields.md) child doc.
- [pier](objects/pier.md) — read when touching `Obj=pier`.
- [ground](objects/ground.md) — read when touching ground and water textures (`Obj=ground`).
- [fences](objects/fences.md) — read when touching fences.
- [smoke](objects/smoke.md) — read when touching smoke and moving effect objects (`Obj=smoke`).
- [good](objects/good.md) — read when touching goods definitions (`Obj=good`).
- [ui](objects/ui.md) — read when touching pakset interface images (`symbol`, `menu`, `cursor`, UI `misc`), including button graphics.
- [program-text](objects/program-text.md) — read when touching `Obj=program_text` or `Obj=dummy_info` support objects.
- [ground-object](objects/ground-object.md) — read when considering ground objects (not currently present).
- [moving-object](objects/moving-object.md) — read when considering moving objects (not currently present).
- [misc](objects/misc.md) — read when touching `Obj=misc` objects such as sidewalks and power lines.

## Open questions

- Which engine source is the authority for the full list of object types, and should this doc
  list every type the engine supports even where the pakset uses none?
- Should object docs be grouped further (for example a single rail-traffic parent) as they grow?
