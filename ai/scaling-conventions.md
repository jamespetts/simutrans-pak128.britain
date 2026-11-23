---
status: draft
verified: New master @ fc87c0424
---
# Scaling conventions

**Covers**: the pakset's scale system, its calibration rulers, logarithmic scaling of long
objects, and oversized images. The authoritative description is the revised graphics workflow in
the forum post
`msg162208` (https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208);
the logarithmic ship scale was agreed in the 2013 thread
`topic=3409.msg112506`
(https://forum.simutrans.com/index.php/topic,3409.msg112506). Rulers and mesh measurements below
are from `GitBlends master @ 8d4bf9e0`.

## The scale system at a glance

| Object class | Length scale | Width/height scale | Cell | Source |
| --- | --- | --- | --- | --- |
| Rail, road, tram vehicles ≤ 15 m | 8.5131 Blender units = 15 m (0.56754 units/m = 8.5131 ÷ 15) | 1.25 × 0.56754 = 0.70942 units/m (i.e. 1 m width/height → 0.70942 units) | 128×128 | `[FORUM msg162208]` `[EXECUTION-VERIFIED:2026-11-14]` |
| Vehicles/objects > 15 m (ships) | logarithmic (sqrt), see below | same logarithmic treatment | 128, or 192/254 oversize | `[FORUM msg162208]` `[FORUM topic=3409.msg112506]` |
| Aircraft | 128 px (one tile) = 46 m, **linear** | not separately documented; treated as per aircraft docs | 128, typically 192 | `[FORUM msg162208]` [aircraft-notes](graphics/aircraft-notes.md) |
| Non-vehicles (buildings, trees, signals…) | not documented | not documented | 128 | open question |

In-game one tile is 128 px wide as an image cell, but adjacent tile centres are 64 px apart
horizontally and 32 px vertically (`display/viewport.cc`: `x = (x - y) * img_size / 2`,
`y = (x + y) * img_size / 4`), and a vehicle crossing a tile moves 64 px horizontally
(`vehicle_base_t::get_screen_offset`). The 8.5131-unit length ruler is therefore **half a tile**:
15 m = 8.5131 units = 32 px, so the graphics scale is 30 m per tile. Vehicle `length` values
follow it at 1.875 m per carunit (16 carunits per tile); the evidence and the method are in
[road-vehicle-lengths](objects/road-vehicle-lengths.md).
Each axis factor is the same chain of multiplication, stated explicitly so it cannot be
misread:

- **Length (Y), 0.56754 units/m** = `8.5131 ÷ 15` — i.e. `11 × 0.7739161 = 8.5131` units
  per 15 m, per `components/15m-rule.dae`.
- **Width and height (X and Z), 0.70942 units/m** = `1.25 × 0.56754 = 1.25 × (8.5131 ÷ 15)`.
  The 1.25 is the forum's multiplier (“width and height 1.25 times the scale of the
  length”), not anything derived from the renderer; the result is **not** the reciprocal
  (1 ÷ 1.25 = 0.8 would be 0.4540 units/m, and is not supported by the measured bodies).
- Worked example (the Audi A4 B6 test build, 4.55 × 1.77 × 1.42 m):
  length `4.55 × 0.56754 = 2.58` units; width `1.77 × 0.70942 = 1.26` units;
  height `1.42 × 0.70942 = 1.01` units.

`[FORUM msg162208]` (“the width and height are 1.25 times the scale of the length”)

## Rulers (`components/`, `air/`)

- `components/15m-rule.dae` — calibration for the length axis. The Collada mesh is an 11-unit
  long plane (Y extent −4.0148…6.9852); its node carries Y scale 0.7739161, giving
  11 × 0.7739161 = 8.5131 units for 15 m. Origin offset Y 0.7569; no rotation.
  `[CODE GitBlends master @ 8d4bf9e0]` `[EXECUTION-VERIFIED:2026-11-14]`
- `components/-standard_gauge_rule.dae` — same 11-unit mesh rotated 90° about Z, Y scale
  0.07403746, parked below the floor at Z −2.818: 0.8144 units = 1.435 m at the 15 m factor. A
  standard-gauge track reference. No document records its intended use.
  `[CODE GitBlends master @ 8d4bf9e0]` `[EXECUTION-VERIFIED:2026-11-14]`
- `air/46m-rule.dae` — the aircraft ruler referenced by [aircraft-notes](graphics/aircraft-notes.md).
  Its geometry does not map obviously onto either the 15 m factor or a 46 m span (mesh Y extent
  13.54 units; node matrix Y scale −1.8117, giving ≈24.5 units). What that file's transform
  actually represents has not been determined. `[CODE GitBlends master @ 8d4bf9e0]`
  `[EXECUTION-VERIFIED:2026-11-14]`

## Axis factors (the "1.25 times" rule, measured)

The forum states only that "the width and height are 1.25 times the scale of the length".
The measured citycar bodies below (main car mesh, excluding the rig `Sphere` and the giant
`Plane_002_003*` measurement planes; body mesh is the car-sized largest mesh in each file,
`Cube.001` in every modern citycar checked) bracket that rule:

| Pak file | Generation (Wikipedia) | Real L×W×H (m) | Blend X×Y×Z (units) | L | W | H |
| --- | --- | --- | --- | --- | --- | --- |
| `ford-focus.blend` | Mk1 1998 5dr | 4.175 × 1.700 × 1.440 | 1.219 × 2.362 × 1.029 | 0.566 | 0.717 | 0.715 |
| `rover-sd1.blend` | Rover SD1 1976 | 4.699 × 1.768 × 1.372 | 1.278 × 2.654 × 0.984 | 0.565 | 0.723 | 0.717 |
| `ford-ka.blend` | BE146 1996 | 3.620–3.650 × 1.631–1.695 × 1.368–1.409 | 1.255 × 2.033 × 0.971 | 0.557–0.561 | 0.74–0.77 | 0.689–0.710 |
| `new-mini.blend` | R50 2000–04 base | 3.627 × 1.689 × 1.420 | 0.989 × 1.760 × 0.957 | 0.485 | 0.586 | 0.674 |

Real dimensions are from the Wikipedia articles cited in each `.dat` (or the Ka article);
blend sizes measured by headless Blender 2.79 world-bbox probe, 2026-11-14.
`[EXECUTION-VERIFIED:2026-11-14]`

- Length factor ≈ 0.5675 units/m holds across the measured files (within ~1%) and is the
  convention for all new work: 0.56754 = 8.5131 ÷ 15.
- **The width/height rule is binding, not empirical.** 1.25 × 0.56754 = 0.70942 units/m on X
  and Z is the pakset convention (forum msg162208); new and rescaled vehicles must use it
  exactly. A vehicle that does not follow the 1.25 multiple exactly is out of convention and
  should be flagged for rescale (user direction, 2026-11-15).
- The measured bodies bracket the rule but deviate from it: Focus 0.717/0.715 and SD1
  0.723/0.717 sit slightly above, the Ka 0.689–0.710 on height slightly below. Under the
  binding rule these are out of convention, not evidence of acceptable variation.
- `new-mini.blend` is small on **all three axes** (0.485 / 0.586 / 0.674) — a pre-rescale
  leftover or a different convention; see open questions.
- The legacy files are hand-aligned, not built by the fixed algorithm, which is why their
  measurements scatter. The recorded standard, not the scatter, governs new work.

## Length > 15 m (ships)

The 2017 post restates the 2013 agreement: for a vehicle over 15 m, scale the length ruler on Y
by sqrt(L/15) relative to the 15 m reference — for a 50 m ship, sqrt(50)/sqrt(15) = 7.07/3.87 =
1.83 — then derive a width ruler by duplicating the re-scaled length ruler, rotating it 90°, and
scaling it by width/length (4/50 = 0.08); bow and stern are fitted to the red bars by freeform
scaling, sides to the width bars by X-constrained scaling.
`[FORUM msg162208]` `[FORUM topic=3409.msg112506, posts 316–325]`

The 2013 thread records the maintainers not fully agreeing on the details: jamespetts described
the per-ship width-ruler method above; kierongreen and The Hood stated that width/length/height
should all use the same scale proportional to sqrt of length, at 1:1 aspect ratio. The 2017 post
restates the jamespetts version; The Hood records that existing boats were "scaled … to the
square root lengthscale". Treat the 2017 statement as the current one; the disagreement on the
aspect-ratio question is a recorded, unresolved tension.
`[FORUM topic=3409.msg112506]`

Rail and road vehicles are never this long. Aircraft are not log-scaled: they use the linear
46 m scale. `[FORUM msg162208]`

## Oversized images

- Most objects use 128×128 cells. Some aircraft and ships need larger images. The post gives
  two non-standard sizes: 192×192 and 254×254, with 254 the maximum Simutrans supports.
  `[FORUM msg162208]`
- To produce an oversized object, set the Blender render resolution to the size and scale the
  object down by 128 divided by that size (for 192, scale by 0.67), then apply offsets in the
  `.dat` as for road vehicles. `[FORUM msg162208]`
- `New/Makefile` has size classes of 192, 224, and 256, which does not match the post's 192 and
  254 and must be reconciled. `[CODE New master @ e36ec2321]`

## Worked example (new build, length ≤ 15 m)

The Stage A export applies the axis factors to a model built in real metres — scaling
happens in Blender 4.5, never in 2.79: scale Y ×0.56754, X and Z ×0.70942 on object
locations and mesh vertices, apply the scale, export the `.dae` at pak scale, then reload
metres master. Stage B then translates only: X centred at 0, body front (excluding
`BUFFER_*`) at Y −4.0, lowest point at Z 0. Example: the 4.55 × 1.77 × 1.42 m Audi A4 B6
becomes 2.58 × 1.26 × 1.01 Blender units before placement.

For road vehicles the `.dat` also needs per-view offset modifiers (the canonical table used for
`daimler-wagonette`, e.g. `E: ,-33,14`; `NW: ,12,10`; …), which position the image on the tile;
whether the fixed-algorithm placement reproduces the framing those offsets assume is unverified
(see open questions and [image-layout](graphics/image-layout.md)).

## Related docs

- [aircraft-notes](graphics/aircraft-notes.md) — aircraft 46 m scale procedure, 192-class cells.
- [blender-rendering](graphics/blender-rendering.md) — placement rules, test records.
- [proposed-geometry-pipeline](graphics/proposed-geometry-pipeline.md) — the proposed vision-loop process record.
- [image-layout](graphics/image-layout.md) — offset modifiers and image sheets.
- [ai-pipeline](graphics/ai-pipeline.md) — the Stage A export applies these factors; Stage B places and renders.

## Open questions

- What is the scale convention for **non-vehicles** (buildings, trees, signs, ground textures,
  stations)? The forum post and all checked-out material address vehicles and ways only.
- Beyond aircraft (46 m linear) and >15 m ships (sqrt), are there further vehicle-specific
  scales (e.g. tram vs rail, narrow gauge)? The `-standard_gauge_rule.dae` (1.435 m) file's
  intended use is unrecorded.
- Does the fixed placement algorithm (front at Y −4.0) apply to road vehicles, or is the road
  alignment achieved solely by the canonical `.dat` offset table? Do the shipped road-vehicle
  `.dat` offsets assume a particular Blender-side placement?
- Why is `new-mini.blend` (R50, `intro_year=2000`) off-scale on all three axes relative to its
  Wikipedia dimensions (L 0.485, W 0.586, H 0.674)? A pre-rescale leftover, or scaled to a
  different convention? The 2017 post states road vehicles were rescaled by April 2017 while
  goods vehicles mostly were not, and that pre-1960s rail wagons are often too large; the older
  `RECOLLECTION:2026-09-19` claim in this KB that "the rescaling of the pakset to this system is
  complete" is contradicted by the forum record for those classes and should be adjudicated.
- Which source governs the ship width-scaling detail — the 2017 workflow post
  (per-ship width ruler) or the 2013 kierongreen/Hood position (uniform sqrt, 1:1 aspect)?
- What does the transform in `air/46m-rule.dae` actually represent, and what is the correct
  way to import it (it does not measure 46 m against the 15 m factor)?
- What are the giant `Plane_002_003*` meshes (≈5.16 units tall, present in every modern citycar
  file) and the 1.0 × 2.5 × 0.8 `Cube` present alongside them? Purpose undocumented.
- The 192/254 (forum) vs 192/224/256 (`New/Makefile`) cell classes: which is authoritative?
