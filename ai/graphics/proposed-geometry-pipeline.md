---
status: draft
verified: none
---
# Proposed AI-assisted geometry pipeline

**Covers**: the proposed (never run end to end) vision-loop geometry pipeline — its Stage A /
Stage B mechanics, the `stageA_export.py` exporter contract, and the verified Blender findings
made while developing it. Moved here from [blender-rendering](blender-rendering.md) on
2026-09-27. Parent: [blender-rendering](blender-rendering.md).

**Relationship to other docs**: current status of AI `.blend` work (what is workable and what
is not), the failure record, and the verification doctrine live in
[blend-creation](blend-creation.md); the stage model and generalized error categories live in
[ai-pipeline](ai-pipeline.md). This doc holds only the proposed process and its
Blender-level mechanics; it does not restate status or doctrine.

## The proposed process

Recorded 2026-09-23 as a potential process only. No end-to-end run has been performed and no
AI-authored geometry has been accepted through it. All points below are `[UNVERIFIED]` except
where tagged.

- Stage A (modern Blender, headless, vision-feedback agent): builds geometry only, in metres,
  front toward −Y, controlled object names with `BUFFER_` prefix for buffer meshes. Part colours
  set on the Principled BSDF `Base Color` input (the legacy `diffuse_color` property does not
  export). Text converted to mesh before export. Export of selected mesh objects only to
  interchange (`.dae`) in scratch space. Every asset inherits its lighting and camera rig from a
  donor blend; geometry may be modified or built fresh, but the rig is always inherited and never
  built from nothing. `[RECOLLECTION:2026-09-25]` `[UNVERIFIED]`
- The Stage A vision-feedback loop is real and working, established earlier in this same
  session by a vision-capable model that has since been swapped out (the model change, not a
  new session). It is underdocumented: the screenshot harness, viewport-view procedure,
  see-act tooling, and worked examples were never written down — they lived only in that
  earlier model's context. The later model (which authored the S69/DC-8 work and this note)
  has no image input and cannot see that earlier model's working detail, so the loop's
  specification must be recovered and recorded here. Do NOT treat the loop as non-existent.
  `[RECOLLECTION:2026-09-25]` The loop's mechanism exists, but AI image-reading is not a
  verification capability: live tests on 2026-09-27 found fabricated observations under
  priming (see [blend-creation](blend-creation.md)); treat the loop's see-act output as
  unverified. `[EXECUTION-VERIFIED:2026-09-27]`
- Stage A export script (prototype `ai/temp/stageA_export.py`, verified 2026-09-23): Blender 2.79
  headless, `blender.exe --background --python stageA_export.py -- <blend> <out.dae>
  [--layers 1,6] [--no-fonts] [--keep-meta] [--apply-mirrors]`. Opens the blend read-only and never saves.
  `--layers` (default `1`) selects model layers; layer 3 rig presence is validated, never
  exported. The script makes model layers visible (the exporter skips hidden layers), converts
  in-scope FONT objects, skips META/rig/empty listings, repairs space/underscore material-id
  collisions in the working copy, rejects relative output paths, and prints one `EXPORT_JSON`
  summary line (`EXPORT_FAIL <reason>`, exit 1, otherwise). The script is tracked in the blends
  repository root (`stageA_export.py`) since 2026-09-25. Verified 2026-09-25: a layers 1+6
  export of `trains/Locomotives/ger-claud.blend` selects the documented 43 in-scope objects
  (10 distinct materials; re-import materialises 11 through importer duplication); the `.blend`
  hash is unchanged across runs; relative output paths and unknown flags fail with exit code 1.
  `[EXECUTION-VERIFIED:2026-09-25]`
- Stage B (Blender 2.79, headless): imports the interchange **at pak scale** — the `.dae` is
  exported pre-scaled from the 4.5 session (object locations and mesh vertices scaled by
  (0.70942, 0.56754, 0.70942), then reload of the metres master from disk); 2.79 does NOT
  scale. Placement only: X centre 0; body front excluding `BUFFER_*` at Y −4.0; lowest point
  at Z 0. Per-object attachment check vs the hull bounding box; clear all animation data
  (stale actions override script positioning); enable layers 1, 2 (camera) and 3 (rig
  sphere); renders with the `...-65.py` view positions. Stage B works on a copy, never saves
  the `.blend` after rendering, and never scales. Scaling belongs to 4.5 because it can be
  seen and verified there; scaling in 2.79 leaves cuboid locations in metres while mesh
  vertices scale (floating parts), and the failure is invisible to a global bounding box
  check. If 2.79 scaling is ever unavoidable, all meshes must be joined into one object
  first so scale is atomic. Stage B works on a fresh copy of `base.blend`, and never saves
  the `.blend` after the render steps: the render script displaces the lighting-sphere
  handle, which is hard to recover. `[EXECUTION-VERIFIED:2026-11-15]` See
  [photo-to-pak-pipeline](photo-to-pak-pipeline.md) for the full run record and rules.
- Lighting workflow (human procedure, verified by reproduction 2026-09-23): design on layer 1
  (layers 4 and above hold measurement aids, temporary objects, and variants such as different
  goods loads); enable layer 3 only just before rendering; save the `.blend` before running the
  render script and never after. `[RECOLLECTION:2026-09-23]` `[EXECUTION-VERIFIED:2026-09-23]`
- Lighting mechanism (measured): the sun lamp is parented to the giant `Sphere` handle parked on
  layer 3. While scene layers show layer 1 only, the hidden Sphere excludes its child lamp from
  render evaluation, so the scene renders black; enabling layer 3 activates the lamp. An
  unparented sun lights from any layer, so the layer rule is an effect of the parenting, not of
  lamp layers. `[EXECUTION-VERIFIED:2026-09-23]`
- Ground-vehicle lighting rule: reuse the existing rig as is; no rig adjustment is needed.
  If roofs or upward-facing surfaces are very light (for example white), reduce their material
  intensity in Blender instead. `[RECOLLECTION:2026-09-25]`
- Aircraft light rig (verified 2026-09-24): under the script's per-view `Sphere` rotations, a
  lamp parented to `Sphere` with `matrix_parent_inverse = identity` and local rotation
  `(117.3791°, 0, -143.7421°)` points about 45° above and to the camera's left; colour
  RGB 0.56, energy 0.028. The rigs saved in the 707, 737 and `air-template.blend` produce a
  horizontal beam, and the DC-8's delivered rig produced an upward beam (a black model);
  always verify the beam direction is downward before rendering. Full recipe:
  [aircraft-notes](aircraft-notes.md). `[EXECUTION-VERIFIED:2026-09-24]`
- Interchange links verified individually 2026-09-23: `.dae` geometry roundtrip from Blender 2.81
  to 2.79 preserves meshes; Principled red (1,0,0) exports as `<color sid="diffuse">1 0 0 1</color>`
  and imports as Blender Internal diffuse (1.0, 0.0, 0.0); a 7-character text object converted to
  mesh (439 polygons) survives the roundtrip with polygon count intact.
  `[EXECUTION-VERIFIED:2026-09-23]`
- Acceptance of AI-authored geometry requires passing the test protocol presented 2026-09-23
  (interchange calibration, scale/position checks, render parity, full-chain review, makeobj
  compile); the protocol itself is untested. `[UNVERIFIED]`

## Related docs

- [blender-rendering](blender-rendering.md) — render workflow, placement, test records.
- [ai-pipeline](ai-pipeline.md) — stage model and generalized error categories.
- [blend-creation](blend-creation.md) — current status, failure record, verification doctrine.
- [aircraft-notes](aircraft-notes.md) — aircraft scale, rig, and livery procedure.

## Open questions

- The vision-feedback loop's harness, viewport procedure, and worked examples were never
  written down (they lived in a swapped-out model's context). Recover and record them, or
  formally retire the loop given the 2026-09-27 findings in
  [blend-creation](blend-creation.md)?
- The acceptance test protocol presented 2026-09-23 is untested as a checklist; is it still
  the intended gate for any future novel-geometry work?
