---
status: draft
verified: New master @ fc87c0424
---
# Vehicle length fields

**Covers**: the `length` field in `New/citycars/*.dat` (`Obj=citycar`) and in road
`Obj=vehicle` files under `New/bus/`; the graphics scale that calibrates it; the method used to
set it; the 2026-11-23 citycar and free-standing road vehicle pass. Parent:
[object-types](../object-types.md). Field reference: [vehicle-fields](vehicle-fields.md).

## Units and defaults

`length` is in **carunits**, 16 to a tile, so 8 is half a tile and 4 a quarter. The engine
defines `CARUNITS_PER_TILE` as 16 and `OBJECT_OFFSET_STEPS` as 16, and the vehicle reader
multiplies the stored value by `OBJECT_OFFSET_STEPS / CARUNITS_PER_TILE` (that is, by one), so
the `.dat` number is the carunit count directly.
`[CODE simutrans-extended master @ d09e920]`

- `Obj=vehicle`: omitted gives 8 (half a tile).
- `Obj=citycar`: omitted gives `citycar_desc_t::DEFAULT_LENGTH` = 4 (a quarter tile).

## The graphics scale: 1 carunit = 1.875 m

One tile of travel is 64 px horizontally, not 128: the image cell is 128 px wide, but
`display/viewport.cc` places adjacent tile centres 64 px apart in x and 32 px in y, and
`vehicle_base_t::get_screen_offset` moves a vehicle 64 px across a tile.

The 2.79 render rig (both `citycars/base.blend` and the bus rig) is orthographic with
`ortho_scale` 24 over a 128 px image, and the Stage A convention is 0.56754 Blender units per
metre. A length lying along a tile axis projects cos 45° = 0.7071 horizontally, so the sprite
scale is `0.7071 × 0.56754 ÷ (24/128)` = 2.14 px per metre. One tile (64 px) is therefore
64 ÷ 2.14 = **29.9 m**, and 16 carunits per tile gives **1.87 m per carunit**.
`[CODE simutrans-extended master @ d09e920]` `[CODE GitBlends @ 8d4bf9e0]`

Cross-check against the rail fleet, where the lengths must join: the BR Mk2 coach is 20.1 m at
`length=11` (1.83 m/unit) and the Mk3 23.0 m at `length=13` (1.77 m/unit). A 15 m tile would
require the Mk2 to be `length=21`, longer than a whole tile.

## Method

The field spaces the drawn sprites, so the target is the **sprite's extent along the 2:1
length axis**, not the real vehicle length. One carunit of spacing is 4 px horizontally, which
is `√(4² + 2²)` = 4.47 px along the 26.57° axis; measure the opaque pixels of the `E`-view
sprite, project them onto that axis, and take the extent:

    length = round(extent_px / 4.472 + 0.35)

clamped to 1–16. The 0.35 bias leaves roughly half a pixel of clearance: a 4.55 m car measures
10.7 px, which is 2.4 units, and the rounding sends it to 3 (13.4 px of spacing) rather than 2
(8.9 px, which makes queued cars overlap).

The physical length is a useful starting point but is not the answer on its own: at 1.875 m per
carunit it gives 2.43 units for that car, and the extra tenth that the sprite is drawn larger
than the body is enough to tip the rounding the wrong way. Horse-drawn vehicles show the same
trap more strongly: the sprite includes the horse, so a carriage measures about 7 m even though
the carriage body is 4.3 m.

## The 2026-11-23 pass

**Citycars.** All 1,911 objects were given a length; none had one before. Each object's `E`
sprite was measured as above, per colourway, and the result is `length=3` for 1,414 objects,
2 for 478, 4 for 11 (the horse carriages, whose sprites include the horse), 5 for 3 (the park
drag) and 1 for 5 (the Peel P50 and the smallest motorcycle outfits). An earlier draft of this
pass used the real length from the metres masters in
`Git Blends/Pak128.Britain-blends/citycars/4.5/*.blend` and was too short in game: cars in a
queue overlapped, because 2 units space a 4.55 m car's 10.7 px sprite only 8.9 px apart.

**Road vehicles.** The set is every road `Obj=vehicle` that is in no coupled consist: neither a
`Constraint[Next]` naming a real vehicle nor named in another object's `Constraint[Prev]`.
Vehicles in a consist keep their lengths, because those set the coupling geometry. The set is
573 objects in 350 files. Each was measured the same way; where the sprite needs more room than
the existing value the value was raised, never lowered. Documented dimensions were used to
override the sprite where the `.dat` comment or file name states one (the Dennis Dart and
Enviro200 families, Enviro400 at 10.3 m, Routemaster 8.38 m, Leyland National 11.3 m, Caetano
Levante 12.6/15 m, the Plaxton-bodied coaches at 12 m, the 27 ft and 30 ft Titans and Tigers).

**makeobj.** Citycar `length` support was added to `citycar_writer.cc` on 2026-11-22, after the
makeobj binary in use (2026-11-15) was built. That binary warns `Entry "length=N" ignored (check
spelling)` and drops the value. The engine makeobj must be rebuilt before the citycar values
take effect; the road vehicle values compile with the older binary.

## Deliberate exceptions

- `New/boats/holds/mail-boot.dat` keeps `length=0`. It is an invisible hold used to let mail
  coaches carry passengers, not a visible vehicle.
- Pedestrian-class objects (`man_on_bicycle`, `post-boy`, `livestock_driver`) are set to 1–2
  carunits to match their sprite, not a road vehicle convention.

## Open questions

- Should the free-standing road vehicle values that were derived from sprites be replaced by
  documented dimensions model by model? The set is 350 files, and many are obscure early
  chassis for which no dimensioned drawing has been found.
- Is the 2.79 rig's `ortho_scale` of 24 the intended permanent setting? It fixes 1 carunit at
  1.875 m for every rendered asset; a rig change would invalidate every length in the pakset.
