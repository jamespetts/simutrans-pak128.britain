---
status: draft
verified: New ex-15 @ 8b04b2114
---
# Blender rendering

**Covers**: the `.blend` meta-sources, headless rendering, aligned `.png` views, and the
transparency workflow.

## Initial facts

- The `.blend` meta-sources live in `Git Blends/Pak128.Britain-blends/` (a separate git
  repository from `New/`). `[CODE GitBlends master @ 1c1acf58]`
- The render script is `render_SimutransRender_pak128Britain-65.py`, with `bl_info` name "Render
  Simutrans Views Pak128.Britain-refresh", version `(1, 5)`, and `blender` `(2, 6, 5)`.
  `[CODE GitBlends master @ 1c1acf58]`
- The script renders 4 or 8 direction views and saves them with direction suffixes (for example
  `_W`, `_NE`). `[CODE GitBlends master @ 1c1acf58]`
- The script has a mask mode for materials whose names start with `sp_`, rendered to magenta
  `(1,0,0.5)`. Per the current workflow this mode is obsolete and belongs to a different pakset;
  it should be ignored. `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`
- Blender 2.79 is required because the render scripts depend on its software renderer. The
  executable is `C:\Program Files\Blender Foundation\Blender\blender.exe`; the scripts directory
  is `C:\Program Files\Blender Foundation\Blender\2.79\scripts`. Blender must be driven headless;
  `.blend` files are never hand-edited (AGENTS.md hard rule 5).
  `[CODE local Blender installation, 2026-09-19]`
- Rendered `.png` views are placed into the `New/` `.dat` objects that use them.
  `[CODE GitBlends master @ 1c1acf58]`
- Vehicle models are assemblies of simple mesh primitives. `gnr-sturrock-single.blend` contains
  114 objects (mostly cubes, cylinders, circles, and planes), 27 materials, and renders at
  128x128 with the `BLENDER_RENDER` engine. `[CODE GitBlends master @ 1c1acf58]`

## Workflow and conventions

From the revised graphics workflow in forum post
`msg162208` (https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208):

- View count and alignment, set with the "Rendering views for Simutrans" script's `op_list`:
  - Road vehicles: render 8 views, normal alignment.
  - All other vehicles (trams, rail, water, aircraft): render 8 views, vehicle alignment.
  - Buildings, signs, signals, stations, and stops: render 4 views, normal alignment.
  A vehicle or way therefore produces 8 `.png` files, one per alignment; the other objects produce
  4. `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`
- Aircraft use normal alignment (8 views). Verified 2026-09-23: headless normal-alignment
  renders of the 707 match the shipped `Boeing_707_420_BOAC.png` sheet cells within 4 px; the
  sheet order is E, NE, N, NW, W, SW, S, SE. New aircraft follow the per-view file convention
  (one `.png` per direction, as for the 737) with RGBA transparent backgrounds.
  `[EXECUTION-VERIFIED:2026-09-23]`
- Trams follow the rail graphics process throughout: 8 views with vehicle alignment and no
  per-image offsets (one measured exception, `bombardier-flexity-swift.dat`, uses sheet cells
  with small offsets). `[RECOLLECTION:2026-09-25]` `[CODE New ex-15 @ 8b04b2114]`
- The current workflow uses alpha transparency. Set the render "output" to RGBA so that Blender
  writes a transparent background, and export anti-aliased images so that edges blend with the
  background. Most older `.blend` files have output set to RGB, which produces black backgrounds.
  With alpha transparency, no post-processing of the exported graphics is needed, except for
  multi-tile buildings and objects that need special colours.
  `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`
- Render-settings check before rendering any model: output must be RGBA (older files use RGB)
  and anti-aliasing (OSA) set to 11 (older files use 16). `[RECOLLECTION:2026-09-23]`
- Many existing graphics still use the old system, a flat special-colour background with no
  anti-aliasing to the background. The aim is to convert all of them to the alpha-transparency
  type. This is limited by missing source files: not all `.blend` files exist, and most London
  Underground vehicles will need to be recreated. `[RECOLLECTION:2026-09-19]`
- The older method set the rendered background to `#e7ffff`, which is the engine's special
  transparency colour `0x00E7FFFF`. It applies only where the alpha-transparency workflow is not
  used. `[CODE simutrans-extended master @ f378cf551]`
- The "Make Masks" function in the render script is obsolete and belongs to a different pakset's
  workflow. `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`
- Liveries are built from separate coloured polygons (planes), or from textures, rather than from
  player colours; see [liveries-and-special-colours](liveries-and-special-colours.md).
- The guide states that standard pak128 artwork is less bright and smoother, and that
  pak128.Britain artwork must be darker and consistent with the existing assets.
  `[FORUM:https://forum.simutrans.com/index.php/topic,2401.0/all.html]`
- Model templates and the blend repositories are linked from the guide. The blend repository used
  by this workspace is `Git Blends/Pak128.Britain-blends/`.
  `[FORUM:https://forum.simutrans.com/index.php/topic,2401.0/all.html]`
- For multi-tile buildings, the tool that splits the graphics into tiles does not work with alpha
  transparency; the post describes the alternatives.
  `[FORUM:https://forum.simutrans.com/index.php/topic,2401.msg162208.html#msg162208]`

## AI authorship of `.blend` sources

- `.blend` sources were authored manually until September 2026, when AI-assisted production
  with constrained numeric operations and human review gates delivered two assets (the S69
  Belpaire transplant and the DC-8 707-derivative). Early language-model attempts at direct
  spatial reasoning demonstrated incapability of even basic spatial reasoning within Blender.
  `[RECOLLECTION:2026-09-25]` `[EXECUTION-VERIFIED:2026-09-19]`
- Current status (user direction 2026-09-27, updated 2026-11-15): under the superseded
  pre-MCP pipeline, novel `.blend` creation was **unstable**; minor `.blend` changes
  (livery/texture substitution, re-rendering, bounded numeric edits) were **workable**; the
  pipeline from `.blend` to `.pak` is **workable**. Under the MCP procedure the agent builds
  and edits in a live Blender 4.5 session and iterates on renders; that is the only process
  shown to work to any extent, and the extent of that work is still being established
  ([ai-pipeline](ai-pipeline.md), [photo-to-pak-pipeline](photo-to-pak-pipeline.md)). Status,
  failure record, and verification doctrine: [blend-creation](blend-creation.md).
  `[RECOLLECTION:2026-09-27]` `[EXECUTION-VERIFIED:2026-09-27]` `[USER-DIRECTION:2026-11-15]`

## Proposed AI-assisted geometry pipeline

The proposed vision-loop geometry pipeline (never run end to end), its Stage A/B mechanics,
the `stageA_export.py` exporter contract, and the verified findings made while developing it
now live in [proposed-geometry-pipeline](proposed-geometry-pipeline.md). Current status of AI
`.blend` creation work: [blend-creation](blend-creation.md).

## Test record 2026-09-23 (Tests 1–2)

- Test 1 (scale/position): PASS. A 7.0 × 2.6 × 2.0 m box plus two `BUFFER_`-prefixed boxes was
  built in Blender 2.81, exported to `.dae`, and imported in 2.79. The 15 m ruler measured 8.5131
  Blender units (0.567539 units/m). All six numeric checks passed within 0.01: scaled length and
  width, X center 0, body front excluding buffers at Y +4.0, lowest point at Z 0, and buffers
  projecting forward of the front (Y 4.227). `[EXECUTION-VERIFIED:2026-09-23]` (Historical
  run: the sign convention is since corrected to front at Y −4.0; see the placement
  convention below. `[RECOLLECTION:2026-09-25]`)
- Test 2 (render parity): PASS with the exact human procedure on a real asset. The 1847
  4-wheel carriage rendered all 8 vehicle-alignment views, 128×128 RGBA with transparent
  backgrounds: 270–465 opaque px per view, 93–100% of them lit, side views in dark red/brown
  livery tones (lit-pixel mean RGB about 53–77, 45–54, 45–54), end views grey. Earlier mechanics
  runs with a provisional sun on the known test box also passed (8 distinct views, blue test
  material renders blue-dominant). `[EXECUTION-VERIFIED:2026-09-23]`
- Finding: `components/base.blend` carries stale 8-frame camera and lamp animation actions (a
  legacy normal-alignment orbit at height 10). At render time fcurve evaluation overrides directly
  set transforms, so all 8 views rendered byte-identical until the actions were cleared. The
  measured vehicle files contain no animation data. Stage B must call `animation_data_clear()` on
  camera, lamp, and sun before positioning.
  `[EXECUTION-VERIFIED:2026-09-23]`
- Finding: the saved sun lamp (`Lamp.001`, parented to `Sphere`) lights nothing while scene
  layers show layer 1 only: the lamp is parked on layer 3 with energy 0.028, and the hidden
  Sphere excludes its child lamp from render evaluation. Enabling layer 3 activates the lamp;
  an unparented sun lights from any layer, so the layer rule is an effect of the parenting, not
  of lamp layers. Raising energy alone did not help. `[EXECUTION-VERIFIED:2026-09-23]`
- Finding: `components/63.5ft-underframe.dae` contains a single 6-polygon plane (a flat profile,
  not 3D geometry), so it cannot judge render parity; the known 3D test box was used instead.
  `[EXECUTION-VERIFIED:2026-09-23]`
- Lesson: a relative `render.filepath` in one headless run resolved outside the project directory
  (8 files written to `C:\ai\temp\`; copies recovered to `ai/temp/`). Stage B scripts must use
  absolute output paths. `[EXECUTION-VERIFIED:2026-09-23]`

## Modify-existing roundtrip 2026-09-23 (ger-claud locomotive)

- Layer substitutions exist: a single `.blend` holds alternative part versions on different
  layers, and only one alternative is rendered. In `trains/Locomotives/ger-claud.blend` (108
  meshes, 16,730 polygons, 30 materials, no animation data) layer 6 holds the normal Claud
  boiler and layer 7 the Belpaire-firebox boiler ("super Claud"). The normal Claud renders from
  layers 1+3+6 and the Belpaire version from 1+3+7; layers 11 and 13 and the measurement meshes
  on 12 and 14–20 are not in the shipped renders. The tender lives in the separate
  `ger-claud-tender.blend`. There is no universal export layer set: each asset needs its own
  layer map. `[RECOLLECTION:2026-09-23]` `[EXECUTION-VERIFIED:2026-09-23]`
- Layer-set verification (S view, 128×128 RGBA): layers 1+3+6 reproduces the shipped
  `ger-claud_S.png` exactly (391 opaque px, identical bounding box and mean RGB); 1+3+7
  reproduces `ger-belpaire-claud_S.png` (395 vs 392 px); enabling 6 and 7 together renders both
  boilers at once (439 px) — the earlier export error. `[EXECUTION-VERIFIED:2026-09-23]`
- Verified working roundtrip (all headless, repo files never saved): in 2.79 enable the mapped
  model layers, convert FONT objects to mesh, export selected to `.dae`; in 2.81 import,
  re-export unchanged; in 2.79 re-import and render with the exact human procedure. Result for
  the normal Claud: 43/43 objects and 11/11 in-scope materials preserved; re-rendered S view
  matches the shipped PNG (387 vs 391 opaque px, identical bounding box, lit-pixel mean RGB
  51,40,68 vs 48,38,67). `[EXECUTION-VERIFIED:2026-09-23]`
- Roundtrip rules found by failure: the 2.79 Collada exporter silently skips objects on invisible
  layers even when selected (first export carried only 59/102 objects); all model layers must be
  visible first. FONT→mesh conversion also requires the font's layer to be visible. Material names
  differing only by space versus underscore (`Black lining` vs `Black_lining`, different shades)
  collide to one `.dae` id; rename to collision-free names in the working copy before export.
  Polygon counts rise through the roundtrip (triangulation) without changing rendered output.
  `[EXECUTION-VERIFIED:2026-09-23]`
- Firebox profile (Belpaire square shoulders vs round-top wrapper) IS visually significant at
  128×128 pak resolution: misidentified as negligible from pixel counts alone 2026-09-23 and
  corrected on human review. Do not dismiss shape deltas from numeric stats without a render
  check. `[EXECUTION-VERIFIED:2026-09-23]`
- Blender 2.80+ scripting note: matrix–vector multiplication must use the `@` operator; the
  pre-2.80 `*` form raises `TypeError`. Scene-graph refresh is `view_layer.update()`, not
  `scene.update()`. Object names with dots are returned with underscores after a 2.81 Collada
  import (`Cylinder.016` → `Cylinder_016`). Track multi-import objects by name sets, not wrapper
  identity, and expect `.001` collision suffixes where two layers reuse a part name (both L1 and
  L7 contain a `Cylinder.011`); bounding-box asserts disambiguate. `[EXECUTION-VERIFIED:2026-09-23]`
- S69 Belpaire transplant (S3, in review): removed L6 round-top wrappers (`Cylinder_018/019`)
  and transplanted 4 L7 Belpaire parts (`Cube_005`, `Cylinder_010/011/025`) shifted +0.30 rigidly
  to the middle-driver datum. No see-through gaps in any of 8 views. `[EXECUTION-VERIFIED:2026-09-23]`
- S69 smokebox fix (S5/S6): review caught an over-long dark smokebox region. Raycast coverage check
  found a 0.6-unit hole in the upper boiler band (Y −3.65..−3.0) between the shifted smokebox rear
  and the transplant front; extending the black wrapper closed the hole but left a black band
  where blue barrel belongs (the wrapper's saddle material). Split the wrapper faces by world-Y
  (164 front faces to blue `MainColour1`, 60 rear faces stay black): barrel now runs blue
  continuous from smokebox to firebox. Lesson: transplanted parts carry their donor-zone
  materials; reassign per-face when the new position changes the visible role.
  `[EXECUTION-VERIFIED:2026-09-23]`
- Modify-existing principle: source models contain dimensional and other defects (eye-judged
  proportions, undersized parts). When deriving a new model, verify each transplanted dimension
  against research and correct defects; never carry them into the new model. Instance 2026-09-23:
  the transplanted S69 firebox proved too short on review (S69 grate 26.5 sq ft vs Claud 21.6)
  and was lengthened in S4. `[RECOLLECTION:2026-09-23]` `[EXECUTION-VERIFIED:2026-09-23]`

## Modification roundtrip 2026-09-23 (ger-claud edited in 2.81)

- Two edits applied to the imported Claud in Blender 2.81: one part (`Cylinder_016`) moved +0.3
  in Y, and `MainColour1` set to green (0,1,0) via Principled Base Color. After re-export and
  2.79 re-import: the part bounding box moved exactly +0.3 (Y −0.37..0.05 became −0.073..0.352),
  the material arrived as diffuse (0.0, 1.0, 0.0), and the S-view render kept the same silhouette
  (436 opaque px, same bounding box) with green-dominant mean RGB (38,130,33) against the
  original blue-purple (45,36,64). Both geometric and colour edits propagate through the
  interchange in both directions. `[EXECUTION-VERIFIED:2026-09-23]`
- Placement rule for modify-existing work: keep the original placement exactly (no rescaling, no
  fixed-algorithm repositioning). The −4.0/center/zero rules apply to new builds only; moving a
  modified locomotive would break coupling and tender alignment.
  `[UNVERIFIED]`

## Related docs

- [liveries-and-special-colours](liveries-and-special-colours.md) — read when handling special colours and liveries.
- [image-layout](image-layout.md) — read when placing rendered views into image sheets.
- [scaling-conventions](../scaling-conventions.md) — read when deciding model and image scale.
- [proposed-geometry-pipeline](proposed-geometry-pipeline.md) — read for the proposed Stage A/B geometry pipeline mechanics and its development record.
- [blend-creation](blend-creation.md) — read for the current status, failure record, and verification doctrine of AI `.blend` work.

## Open questions

- Under what demonstrated conditions may AI-authored `.blend` geometry be accepted? See the AI
  authorship section above.
- Should the stale 8-frame camera/lamp animation actions be removed from
  `components/base.blend`, so new assets started from the template cannot inherit the
  render-positioning trap? See the test record.
- What is the exact command line used to render a blend file headless, and is it automated?
- Are there other render scripts in use besides `...-65.py`, and which is canonical?
- Which blend produces which `.png` and `.dat` object?
- Which objects still need the old `#e7ffff` background rather than alpha transparency?
- What is the model placement convention relative to the scene origin? Fixed algorithm adopted
  2026-09-23 (no exemplar matching: existing models were aligned approximately by eye and are not
  exact). `[RECOLLECTION:2026-09-23]`
  - Locomotive orientation: the smokebox (front) faces −Y and the cab sits at +Y, measured in
  `ger-claud.blend` (chimney Y≈−2.7, dome −1.28, cab +0.28..+1.54, bogie forward, drivers
  rearward) and confirmed by the user. The earlier recorded "front toward +Y" was wrong.
  The frontmost point of the body sits at Y −4.0, confirmed 2026-09-25.
  `[EXECUTION-VERIFIED:2026-09-23]` `[RECOLLECTION:2026-09-25]`
  - Length axis is Y. After scaling, translate the model so
  the frontmost point of the body sits at Y −4.0. `[RECOLLECTION:2026-09-25]`
  - For rail vehicles, buffers are excluded from the −4.0 measurement: buffer geometry may extend
    forward of Y −4.0 (to more negative Y). Excluding buffers gives better visual coupling alignment.
    `[RECOLLECTION:2026-09-23]` Buffer meshes are identified by a controlled name prefix assigned
    at build time (fresh Stage A builds use controlled names, unlike legacy files).
    `[UNVERIFIED]`
  - Center the body bounding box at X 0. `[UNVERIFIED]`
  - Set the lowest point of the model (wheel bottoms for vehicles) to Z 0.
  `[RECOLLECTION:2026-09-23]` Legacy files sit slightly above this (measured wheel bottoms at
  approximately Z 0.11–0.13), consistent with approximate eye alignment rather than exact
  placement. `[EXECUTION-VERIFIED:2026-09-23]`
  - Measured 2026-09-23, legacy files do not follow this rule: the body of
  `trains/Carriages/1847-carriage-mr.blend` spans Y −3.8 to +0.97 and the body of
  `trains/Locomotives/bird-class.blend` spans Y −4.14 to −1.02 (sun object `Sphere` excluded).
  `[EXECUTION-VERIFIED:2026-09-23]` Do not position new models by matching these files.
- Ship offsets follow no single table (holds and the oversized classes carry per-size offsets;
  small base hulls generally none): is there a governing rule, or is each vessel bespoke?
