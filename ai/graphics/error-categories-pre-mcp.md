---
status: draft
verified: none
---
# Error categories of the pre-MCP pipeline (historical)

**Covers**: the recorded error categories of the superseded pre-MCP AI pipeline. Kept as a
checklist of geometry mistakes and as the historical record of why that procedure was
abandoned. For the current procedure see [ai-pipeline](ai-pipeline.md); for the status and
failure record see [blend-creation](blend-creation.md).

**Context**: the pre-MCP pipeline (before 2026-11-14) had the AI write per-task Python
scripts against `.blend` files headlessly, with no live scene view and no interactive scene
queries. Its checks were script runs and renders the agent could not reliably interpret.
Every category below was recorded under those conditions. They remain valid descriptions of
what goes wrong in AI geometry work — the current MCP procedure prevents some of them
structurally and detects others by scene queries — but the procedures that produced them
are superseded. `[USER-DIRECTION:2026-11-15]`

**Assets named below** (pakset identifiers): S69 and Claud — GER steam locomotives; B12/3 —
an LNER 4-6-0; DC-8-10 and 707 — airliners; Belpaire — a firebox type.

## Categories

1. **Numeric similarity is not visual similarity.** Pixel counts, bounding boxes, and mean
   colours can match while the shape is wrong (round-top vs Belpaire firebox) or hide faults
   (a black wrapper band reading as extended smokebox). Every claim about appearance requires
   a render check; statistics alone prove nothing about looks.
2. **Fix source defects; do not transplant them.** Checked-out models are eye-judged and
   contain dimensional errors. Verify each reused dimension against research and correct
   errors in the model being built. Instance: an undersized transplanted firebox lengthened
   to a grate-area-derived length.
3. **No universal layer set exists.** Each asset needs its own layer map: which layers
   combine, which substitute for each other (never render two alternatives together), and
   which hold measurement aids, variants, or rigs. Verify the map by rendering layer
   combinations and matching shipped `.png` files before editing.
4. **Exporter mechanics.** The 2.79 Collada exporter silently skips objects on invisible
   layers even when selected: enable all model layers first. FONT-to-mesh conversion also
   requires a visible layer. Material names colliding after space-to-underscore sanitization
   merge silently; rename in the working copy. Polygon counts rise through interchange
   (triangulation) without changing rendered output; compare geometry by bounding box and
   render, not face counts.
5. **Stale animation data overrides script positioning.** Template-derived files can carry
   keyframed camera/lamp actions; fcurve evaluation defeats directly set transforms at
   render time (all views render byte-identical). Clear animation data on camera, lamp, and
   sun before positioning. `components/base.blend` carries such actions; the working vehicle
   files measured so far do not.
6. **Lighting procedure.** Design on layer 1 (upper layers hold aids, temporary objects, and
   livery variants); enable layer 3 only just before rendering; save before running the
   render script and never after (the script leaves the lighting-sphere handle displaced).
   Mechanism: the sun lamp is parented to the layer-3 Sphere handle, and the hidden handle
   excludes its child lamp from render evaluation.
7. **Placement.** Modify-existing work keeps the source placement exactly (no rescaling, no
   repositioning); the fixed algorithm (X centre 0, body front excluding buffers at Y −4.0,
   lowest point Z 0) applies to new builds only. Orientation is per class and measured, not
   assumed.
8. **Transplanted parts carry donor-zone materials.** Reassign per-face when the new
   position changes the visible role (front faces blue barrel vs rear faces black saddle on
   one wrapper).
9. **Hole detection.** Assemblies edited across origins develop coverage gaps that read as
   dark masses. Raycast coverage check per Y slice (side rays across Z bands) before
   presenting assembly renders; extend or add wrappers until solid.
10. **Absolute paths.** Relative output paths have resolved outside the project directory.
    All scripts take absolute paths and reject relative ones.
11. **Version API notes.** Blender 2.80+ needs the `@` matrix operator and
    `view_layer.update()`, and returns underscore-renamed imports; 2.79 uses `*` and
    `scene.update()`. Track multi-import objects by name sets (expect `.001` collision
    suffixes where layers reuse part names) with bounding-box asserts, never wrapper
    identity.
12. **Render-settings check (all models).** Before rendering any model, verify output is
    RGBA (older files use RGB) and anti-aliasing is 11 (older files use 16).
13. **Review authority.** The human approves geometry from renders. The AI proposes specs
    and executes operations; it does not judge novelty or historical accuracy.
14. **Half-models with mirror modifiers.** Older aircraft model one side plus a mirror
    modifier. Interchange drops unapplied modifiers (half model arrives); apply
    deterministically before editing. Reshaping by moving vertices preserves UV assignments,
    which live per-face independently of positions.
15. **TexFace images do not interchange.** Face-assigned livery images are absent from
    `.dae` output (no `library_images`); UV layers and materials survive. Record the
    mesh-to-image mapping at export time and re-link images by path afterwards. New liveries
    are authored as 2D images fitted to the existing UV layout.
16. **Flat shading only.** All faces must be shaded flat (`use_smooth = False` on every
    polygon); smooth shading produces visible artifacts. Check and enforce in Stage B before
    rendering, for every model.
17. **Check the light rig before taming materials.** A black or blown-out model is usually a
    mis-set sun rig, not a material problem. With the verified aircraft rig
    ([aircraft-notes](aircraft-notes.md)) the 707/VC-10 material settings (diffuse 0.8,
    specular 0.5) render correctly. Only reduce material intensity after the rig is verified.
    Ground vehicles are the exception: reuse the existing rig as is and reduce only very
    light roofs or upward-facing surfaces ([blender-rendering](blender-rendering.md)).
18. **argv handling.** A probe script deriving its output path from the first `--` in
    `sys.argv` wrote its object list into the open `.blend`, reducing a tracked blend to 18
    bytes of text (recovered via `git restore`, re-verified by header and object count). The
    defensive rules: take script arguments after the last `--`, and refuse output paths by
    extension (never write non-`.txt`/non-`.dae` targets). `stageA_export.py` follows both.
19. **AI render-reading is not verification.** Under priming, the AI fabricates image
    observations (four of nine candidate defects falsified by the user, 2026-09-27) and
    misses real ones. Image ambiguity is resolved silently toward expectation; confidence
    labels do not help. This is why the pre-MCP pipeline could not check its own output.
    [blend-creation](blend-creation.md) records the tests. `[EXECUTION-VERIFIED:2026-09-27]`
20. **As capability rises, failures move to geometric foresight.** Below about 20% all-pass,
    82% of failures are comprehension or code that does not run; above 55%, geometric
    foresight is the largest failure stage at about 40%: the code runs and builds the wrong
    shape, most often through unforeseen interaction between parts or parts left floating.
    Figures and sources: [model-selection](model-selection.md).
    `[LITERATURE:https://arxiv.org/abs/2610.38231]`

## Open questions

- Which categories has the MCP procedure made structurally impossible, and which does it
  only detect? Each category should record its MCP-era equivalent when one exists.
