---
status: draft
verified: New ex-15 @ 937d464a9; GitBlends master @ 8d4bf9e0 (working trees, 2026-11-15)
---
# Accepted Anglia graphics sources

**Covers**: maintaining the photograph-referenced Ford Anglia 100E/105E models and
reproducing their pakset renders. Parent:
[photo-to-pak-pipeline](photo-to-pak-pipeline.md). Controls:
[visual-asset-controls](visual-asset-controls.md).

The user approved the 105E, then the 100E after reducing its boot crown. The replacements
are installed in the pakset source tree and compiled into the local citycars pak. This
does not establish in-game traffic appearance or alignment.
`[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`

## Source identity

Paths in this section are relative to `Git Blends/Pak128.Britain-blends/`.

| Asset | Metres master, Blender 4.5 | Prepared render source, Blender 2.79 |
| --- | --- | --- |
| 100E | `citycars/4.5/ford-anglia-100e-photo.blend` | `citycars/ford-anglia-100e.blend` |
| 105E | `citycars/4.5/ford-anglia-105e-photo.blend` | `citycars/ford-anglia-105e.blend` |

The **`-photo.blend` masters are the accepted sources**. The unqualified older 4.5 files
`ford-anglia-100e.blend`, `ford-anglia-105e.blend` and
`ford-anglia-105e-rework.blend` are not substitutes for them.
`citycars/anglia-shape-spec.md` and the earlier failed rework scripts are not specifications
for the accepted models. The prior 2.79 render sources were retained under
`citycars/handoff-assets/anglia-pre-photo-20261115/`.
`[EXECUTION-VERIFIED:2026-11-15]`

The pakset definitions, including their accepted-master pointers, are
`New/citycars/ford-anglia-100e.dat` and `New/citycars/ford-anglia-105e.dat`.
Keep object data and paint names there rather than duplicating them in this guide.

## Reference images

The retained photographs are in `citycars/handoff-assets/anglia-refs/`.
The builder's header identifies the images used for each generation.

For the 105E, `hi-1960_Ford_105E_Anglia__licence_AL-17-79__pic7.jpg` is the side
comparison photograph. `hi-1963_Ford_Anglia_105E_Saloon__15316029686_.jpg` is front
three-quarter, not side-on. The earlier spec mislabelled that angle.
For the 100E, `1956_Ford_Anglia_100E_1.2_Rear__1_.jpg` shows the earlier generation,
not the 105E. Confirm the actual photograph before interpreting a difference as a model
defect. Shape and attachment lessons: [geometry-pitfalls](geometry-pitfalls.md).
`[EXECUTION-VERIFIED:2026-11-15]`

## Editing and exporting

- Edit the accepted metres master in the live Blender 4.5 session and save it under `4.5/`.
  User hand edits take precedence over a later builder invocation.
- `anglia_mesh.py::build_100e()` and `build_105e()` construct new models. Run them only in
  a new scene, never over an existing hand-edited master.
- For export without rebuilding, load `anglia_mesh.py`, set its module variable `P` to
  `FordAnglia100E` or `FordAnglia105E`, and call `export_pak()` with an absolute project
  scratch `.dae` path. Use a fresh MCP call after saving.
- The exporter includes only the active scene's matching car meshes. It applies the
  [pak axis factors](../scaling-conventions.md) to temporary mesh copies and restores the
  original data and transforms in `finally`. Do not save a scaled master.

`[EXECUTION-VERIFIED:2026-11-15]`

## Blender 2.79 rendering

Use `stageB_car_prepare.py` with the base rig, exported pak-scale `.dae`, an absolute output
`.blend` path, the appropriate object prefix and the mesh count read from that export.
Preparation is translation only. Check import bounds, wheelbase, glazing, closed wheels and
attachments against the complete shell; save the prepared source before rendering.

Use `stageB_car_render.py` with the prepared 2.79 source and the matching arguments:

| Object prefix | Image stem | Colour-list path in blends repository |
| --- | --- | --- |
| `FordAnglia100E` | `ford-anglia-100e` | `citycars/ford-anglia-100e-colours.json` |
| `FordAnglia105E` | `ford-anglia-105e` | `citycars/ford-anglia-105e-colours.json` |

The render driver writes beside the opened `.blend`. For test renders, use a copy in
`ai/temp/`. Never save the render source after the view script has moved the rig.
Validate the expected views and image contents even if Blender reports a teardown error;
see [ai-pipeline](ai-pipeline.md#tooling).
`[EXECUTION-VERIFIED:2026-11-15]`

After user approval, copy the final renders to `New/citycars/images/` and retain matching
renders in the blends repository. Follow [build-and-toolchain](../build-and-toolchain.md)
for compilation. The accepted rework passed non-quiet makeobj compilation and the make
citycars target, with byte-identical output and no warnings or ignored fields. Its `.dat`
changes were comments only. In-game traffic testing remains separate.
`[EXECUTION-VERIFIED:2026-11-15]`

## Open questions

- Does in-game traffic testing confirm the accepted renders' road alignment and appearance?
