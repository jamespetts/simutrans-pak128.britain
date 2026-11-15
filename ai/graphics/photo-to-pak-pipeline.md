---
status: draft
verified: none
---
# Photo-to-pak pipeline (experimental, first full run 2026-11-14/15)

**Covers**: building a pakset vehicle image end to end from a reference photograph and a
short description — Blender 4.5 MCP build, `.dae` interchange, headless Blender 2.79 Stage B
scale/placement/render. Parent: [graphics-pipelines](../graphics-pipelines.md). Sibling:
[proposed-geometry-pipeline](proposed-geometry-pipeline.md) (stage mechanics),
[blender-mcp](blender-mcp.md) (MCP environment and session findings).

Status: experimental. One full run exists (Audi A4 B6, 2026-11-14/15) as far as render; the
asset is **not** a pakset object (no `.dat`/`.pak`, not placed in a folder, not reviewed
out of Blender). AI reading of renders is displaced for *iteration* by user direction
(2026-11-14); the user remains the visual gate and is excluded from verification claims.

## The recorded run (Audi A4 B6)

- Reference photograph: user-supplied side profile (`ai/temp/A4.png`); description: 2000s
  Audi A4 B6 saloon; real dimensions L 4.55 m, W 1.77 m, H 1.42 m (built 1.44 m, 2 cm over
  spec — not yet ruled on), wheelbase 2.65 m, wheel Ø 0.63 m.
- Build: ~20-iteration low-poly assembly in metres, driven over MCP in a live 4.5 session
  (superellipse lofts, 20-segment wheels, cuboid lamps; single-mesh glasshouse with crown
  faces assigned to the paint material between y −0.22 and +0.80). User hand-edited the
  headlamps in 4.5 at one point (both pushed forward); those edits survived later rebuilds
  only because the 4.5 session was saved after them.
- **Scaling happens in 4.5, at export** (user direction 2026-11-15): the metres master is
  scaled on every `AudiA4_*` object (locations × (0.70942, 0.56754, 0.70942), then
  `transform_apply(location=False, rotation=False, scale=True)`), the `.dae` is exported at
  pak scale, and the master reloads from disk so the authoring file stays in metres.
  `citycars/4.5/audi-a4-b6.blend`; interchange `citycars/4.5/audi-a4-b6.dae`
  (pak units: x ±0.654, y −1.342…+1.325, z 0…1.024); 2.79 working copy
  `citycars/audi-a4-b6.blend` (untouched `base.blend` copy, never scaled).
- Stage B (2.79 headless): layers 1+2+3 (object → layer 1, Camera → layer 2, Sphere →
  layer 3), animation data cleared on Camera/Lamp.001/Sphere, PNG/RGBA, OSA 11, import
  (21 objects, no strangers), flat shading enforced, **translate only** (front min-y at
  −4.0, X centred, lowest Z 0), per-object attachment check vs hull bbox (all 21 pass),
  saved **before** rendering. No scaling in 2.79, ever; if scaling in 2.79 were ever
  unavoidable, all meshes must be joined into one object first so the scale is atomic and
  cannot separate parts.
- Render: 8 road views via `render_SimutransRender_pak128Britain-65.py` with `op_list="1"`,
  `image_name="audi-a4-b6"`; outputs moved to `ai/temp/audi-a4-b6-views/`.
- Numeric checks: the original run recorded 8/8 views as a single connected non-transparent
  pixel cluster (75–105 px per view; front-on and rear-on ≈ 99/102 px; end views ≈ 75–78 px);
  transparent background everywhere. **Correction (2026-11-15):** re-analysis of the same
  images gives NW = 3 clusters and SE = 2, with the other six views single; the "8/8" claim is
  not reproducible and the gate is unreliable at this scale
  ([geometry-pitfalls](geometry-pitfalls.md)). Small sizes expected at pak scale.
  `[EXECUTION-VERIFIED:2026-11-15]`
- Earlier failure worth remembering: an attempt to scale inside 2.79 baked scale into
  meshes but left cuboid LOCATIONS in metres (lamps floated ~3.5 m ahead of the car) while
  the global bbox check passed; fixed by the 4.5-side scaling above and catched by the
  per-object attachment check.

## File placement rule (user direction, 2026-11-15)

**Blender 4.5 files are saved separately from Blender 2.79 files.** The rule:

- Blender 4.5 sources live in a `4.5/` subdirectory of the normal `.blends` folder, e.g.
  `citycars/4.5/audi-a4-b6.blend`; the interchange `.dae` lives alongside it
  (`citycars/4.5/audi-a4-b6.dae`).
- Blender 2.79 working copies stay at the normal path (`citycars/audi-a4-b6.blend`), copied
  fresh from `base.blend` per asset, and are never saved after the render script runs (the
  render displaces the rig handle).
- Never let the two versions write one file; 2.79 scripts depend on its software renderer.

Note: AGENTS.md hard rule 5 was amended on 2026-11-15 to permit 4.5 to save `.blend` files
under this `4.5/` rule; it previously forbade 4.5 from saving a `.blend` at all.

## Lessons that make the next run faster

1. **The client-side dispatch is racy.** Every `execute_blender_code` call must go through
   a retry loop that stops on `Code executed successfully` or `Error executing code:` and
   retries on bare JS-style errors. Multi-line payloads starting `import bpy`; keep
   payloads idempotent (delete named objects first). See [blender-mcp](blender-mcp.md).
2. **Save the 4.5 session regularly**, e.g. after every accepted change. `bpy.ops.wm.
   save_as_mainfile(filepath=<absolute>)` works via MCP; without it, a later AI rebuild
   overwrites user hand edits.
3. **Never rename without a bounds print.** Two rename attempts produced `.001` suffixes,
   a mangled `AudiA4_Rear_Valance`→`AudiA4_Rear_VaR`, `Bumper_R`→`BumperR`/`BumR`, and a
   left/right swap of every mirrored part. Rule: no rename of any object without printing
   world-space vertex bounding boxes before and after.
4. **Superellipse lofts taper inward below the horizontal mid-line.** Anything straight and
   wider than the local half-width at its z floats (the sills hung in free space beside the
   underside). Pre-check: for every part's z-range, compute the hull half-width at each
   station and require the part's outer x-extent to fit; delete or shrink offenders. Same
   failure class as the lamp corners poking above the nose taper.
5. **Do not assign crown-paint to every ring**; restrict painted faces by station range,
   else the whole glass band turns red (windshield included).
6. **Measurement protocol**: calibrate px↔m from a known feature (tyre Ø 84 px ≈ 0.632 m);
   probe column/row dark runs for landmarks (glass span, hub positions, roofline); compare
   ratios (wheelbase/body, glass span, gather position) — never judge silhouette by eye.
7. **Views for review**: perspective 3/4 (user's standing requirement) *and* axis-orthographic
   for profile; `AREA` shading `MATERIAL` shows materials; `view_axis` needs a `WINDOW`
   region override (`bpy.context.temp_override(area=…, region=…)`); frame with
   `region_3d.view_distance` / `view_location`; hide Camera/Light icons with `hide_set`.
8. **Stale-file discipline**: before Stage B, compare the working copy's hash to `base.blend`
   (it may carry deliberate prior work). The working copy and `.dae` are outputs of the last
   **approved** model, never of an intermediate build.
9. **Numeric gate is not visual acceptance**: opaque-px counts, alpha bboxes and mean
   lit-pixel RGB catch black renders and gross errors only; the user's eyes are the gate.

## Target automated pipeline (photograph + description/stats → pakset asset)

1. Photograph ingestion + measurement of key proportions (calibration + dark-run probing).
2. Parameterised build via MCP from a dimension table (one script per vehicle archetype,
   spec dict or JSON; today the build is bespoke).
3. Iteration loop against the photograph until the user approves the model.
4. Stage A export to `.dae` (absolute path into `4.5/`).
5. Stage B: 2.79 headless; layers, anim clear, RGBA/OSA 11; import; layer 1; flat shading;
   scale; place; save before render; 8 road views.
6. Numeric checks; human review.
7. Pak integration (`.dat`/`Obj=`/makeobj) — **not yet attempted for this asset**.

## Open questions

- Can landmark extraction from arbitrary photographs be automated at all, or is the
  measure-first-then-build loop semi-manual permanently?
- Is a parametric dimension-table build practical across this pakset's vehicle families?
- Should the 2.79 working copy be auto-stamped with a session id to defeat stale-copy
  masquerade?
