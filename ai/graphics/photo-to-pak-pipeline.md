---
status: draft
verified: New ex-15 @ 937d464a9; GitBlends master @ 8d4bf9e0 (Anglia-related working-tree checks, 2026-11-15)
---
# Photo-to-pak procedure

**Covers**: building a pakset vehicle image end to end from a reference photograph and a
short description — Blender 4.5 MCP build and scaling, `.dae` interchange, headless Blender
2.79 placement/render, and pak integration. Parent: [graphics-pipelines](../graphics-pipelines.md). Sibling:
[proposed-geometry-pipeline](proposed-geometry-pipeline.md) (stage mechanics),
[blender-mcp](blender-mcp.md) (MCP environment and session findings).

This procedure has produced user-accepted Anglia replacement graphics through pak
compilation. It is not evidence of reliable unattended geometry creation. The agent uses
images for iteration; the user judges appearance. Compilation does not establish in-game
traffic appearance or alignment. `[EXECUTION-VERIFIED:2026-11-15]`
`[USER-DIRECTION:2026-11-15]`

## Reference and review controls

The mandatory controls are defined in [visual-asset-controls](visual-asset-controls.md):
reference images before geometry, basic dimensions established, the same image-reading
session doing the construction, repeated captures at the reference angles, coherent
additional views, and user acceptance of the final renders. Text supplies numeric and
historical facts, not the vehicle's shape. Do not substitute a dimension table or a
comparison with another model for direct photograph matching.
`[USER-DIRECTION:2026-11-15]`

The operational stage sequence is in [ai-pipeline](ai-pipeline.md). Keep scaling entirely
in Stage A and preserve a metres master; Stage B is translation and rendering only.

## Maintained asset examples

- [anglia-sources](anglia-sources.md) — read when editing or re-rendering the accepted
  Anglia 100E/105E sources, choosing between the accepted and rejected masters, or using
  their builder, exporter and colour lists.
- The Audi A4 B6 established the MCP save/export/render procedure. Its persistent source
  is `citycars/4.5/audi-a4-b6.blend` in the blends repository; its pakset definition is
  `New/citycars/audi-a4-b6.dat`. Do not rely on deleted scratch captures as source files.

The Anglia photographic replacements were accepted after reference comparisons and user
corrections, then compiled without warnings. Their compile check is separate from any
in-game traffic test. `[EXECUTION-VERIFIED:2026-11-15]`
`[USER-DIRECTION:2026-11-15]`

## File placement rule (user direction, 2026-11-15)

**Blender 4.5 files are saved separately from Blender 2.79 files.** The rule:

- Blender 4.5 sources live in a `4.5/` subdirectory of the normal blends folder, e.g.
  `citycars/4.5/audi-a4-b6.blend`.
- Blender 2.79 working copies stay at the normal path (`citycars/audi-a4-b6.blend`), copied
  fresh from `base.blend` per asset, and are never saved after the render script runs (the
  render displaces the rig handle).
- Never let the two versions write one file; 2.79 scripts depend on its software renderer.
- Regenerable interchange, logs and test renders belong in project-root `ai/temp/`.
  Irreplaceable `.blend` working files must remain in the relevant repository, not solely
  in scratch. The prepared render copy may be copied to scratch to produce review images
  without replacing the persistent source.

The placement and scratch rules are defined in the project `AGENTS.md`; the Anglia
export/import procedure exercised this separation. `[EXECUTION-VERIFIED:2026-11-15]`

Note: AGENTS.md hard rule 5 was amended on 2026-11-15 to permit 4.5 to save `.blend` files
under this `4.5/` rule; it previously forbade 4.5 from saving a `.blend` at all.

## Lessons that make the next run faster

1. **The client-side dispatch is racy.** Every `execute_blender_code` call must go through
   a retry loop that stops on `Code executed successfully` or `Error executing code:` and
   retries on bare JS-style errors. Multi-line payloads starting `import bpy`; keep
   payloads idempotent (delete named objects first). See [blender-mcp](blender-mcp.md).
2. **Save the 4.5 session regularly**, e.g. after every accepted change.
   `bpy.ops.wm.save_as_mainfile(filepath=<absolute>)` works via MCP. Saving preserves the
   edits on disk; it does not make a subsequent destructive rebuild safe. Edit the saved
   master and do not rerun a builder over hand-edited geometry.
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
6. **Measurement protocol**: check the vehicle generation and actual camera angle first.
   Use known dimensions to calibrate the basic size, and compare feature proportions at the
   photograph's angle. Do not treat coordinates from an oblique photograph as precise
   orthographic measurements. The visual comparison remains necessary
   ([geometry-pitfalls](geometry-pitfalls.md#photograph-identity-and-camera-angle)).
7. **Views for review**: perspective 3/4 (user's standing requirement) *and* axis-orthographic
   for profile; `AREA` shading `MATERIAL` shows materials; `view_axis` needs a `WINDOW`
   region override (`bpy.context.temp_override(area=…, region=…)`); frame with
   `region_3d.view_distance` / `view_location`; hide Camera/Light icons with `hide_set`.
8. **Source identity**: start from the identified accepted metres master. Preserve existing
   render files before replacing them and do not mistake an older rejected source for the
   accepted one. Import checks must refer to the actual exported scene, not a memorised
   object count or bounding box from another build.
9. **Numeric gate is not visual acceptance**: opaque-px counts, alpha bboxes and mean
   lit-pixel RGB catch black renders and gross errors only; the user's eyes are the gate.

The Anglia implementation adds temporary-copy export, complete-shell attachment checks,
closed-wheel verification after import, and surface-fitted details. See
[anglia-sources](anglia-sources.md) for the implementation and
[geometry-pitfalls](geometry-pitfalls.md) for the reasons for those checks.
`[EXECUTION-VERIFIED:2026-11-15]`

## Open questions

- Can landmark extraction from arbitrary photographs be automated at all, or is the
  measure-first-then-build loop semi-manual permanently?
- How much of photograph fitting can be automated without losing direct reference
  comparisons and human appearance acceptance?
- Should the 2.79 working copy carry machine-readable source identity to prevent accidental
  reuse of a rejected or unrelated source?
