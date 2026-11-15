---
status: draft
verified: none
---
# AI asset authoring pipeline (MCP)

**Covers**: the staged process for AI-assisted pakset asset creation as it now runs —
geometry and scaling in a live Blender 4.5 session driven through Model Context Protocol
(MCP), rendering in headless Blender 2.79, and pak integration. Parent:
[graphics-pipelines](../graphics-pipelines.md). Historical record of the superseded
pre-MCP pipeline: [error-categories-pre-mcp](error-categories-pre-mcp.md) and
[blend-creation](blend-creation.md).

## What "pre-MCP" means

"Pre-MCP" refers to the AI pipeline used before 2026-11-14: the agent wrote per-task Python
scripts that modified `.blend` files headlessly (Blender 2.81), then imported the result
into Blender 2.79 for rendering. The agent had no live view of the scene and no way to
query it interactively — every check was a script run followed by renders the agent could
not reliably interpret. That pipeline produced two assets by modifying existing models
under close human review, and repeatedly produced wrong-but-plausible geometry when asked
for novel work. Its recorded error categories are kept for reference; its procedure is
superseded and is not used for new work. `[USER-DIRECTION:2026-11-15]`

## Stages (MCP procedure)

1. **Research** — published dimensions, model-year data, market and popularity statistics,
   and livery/colour sources. Record every value with its source; training-data priors are
   search hints only.
2. **Specification** — a numeric plan (parts, sizes, positions, colours, dates, weights)
   agreed with the user before Blender work starts.
3. **Stage A — geometry in live Blender 4.5 through MCP.** The agent builds or edits
   geometry in metres with bounded operations, verifying after every step by reading the
   scene (object lists, world bounding boxes, material values). The user can watch and
   hand-edit the same session. The 4.5 `.blend` is saved regularly under `<folder>/4.5/`
   beside the normal blend folder (file-placement rule:
   [photo-to-pak-pipeline](photo-to-pak-pipeline.md)). Iteration is visual: renders are
   pulled into the conversation with the MCP tooling and the agent states what it sees; the
   user remains the judge of appearance (Review gates).
4. **Stage A export — scale here, never in 2.79.** Object locations and mesh vertices are
   multiplied by the axis factors (X and Z 0.70942, Y 0.56754 —
   [scaling-conventions](../scaling-conventions.md)), the scale is applied, the `.dae` is
   exported at pak scale, and the metres master is reloaded from disk so the 4.5 file stays
   in metres. Rationale: scaling in 2.79 cannot be seen or checked there, and a
   mesh-only scale leaves position-carrying parts behind (recorded failure,
   [photo-to-pak-pipeline](photo-to-pak-pipeline.md)).
5. **Stage B — placement and rendering in headless Blender 2.79.** Import the pak-scale
   `.dae` (no scaling anywhere in this stage), clear animation data, set RGBA output and
   OSA 11, flat-shade, translate only (X centred; body front at Y −4.0; lowest point Z 0),
   run a per-object attachment check against the hull, save the working copy before
   rendering, then render the class's view set with
   `render_SimutransRender_pak128Britain-65.py`.
6. **Pak integration** — rendered views into the source folder's `images/` directory; the
   object's `.dat` written to the class's conventions (for private cars: staggered colour
   intro/retire dates and popularity-based weights; [citycar](../objects/citycar.md)); the
   folder compiled with makeobj as the validity check.
7. **Review gates** — the human approves geometry and final renders. AI checks are working
   tools, never acceptance evidence.

Tooling: the MCP server ([blender-mcp](blender-mcp.md)); the render script and rig in
`Git Blends/Pak128.Britain-blends/`; makeobj (`New/makeobj-extended` — invocation pitfall
and freshness rule: [build-and-toolchain](../build-and-toolchain.md)); small
checker scripts in `ai/temp/` per session (per-object attachment check, PNG cluster
analysis).

## Procedure status

- **MCP has been shown to be the only process that works to any extent.**
  `[USER-DIRECTION:2026-11-15]`
- **Four end-to-end runs now exist.** The first (2026-11-14/15) was an Audi A4 B6 saloon
  taken through geometry, six colour variants, render and makeobj compile into a private
  car ([photo-to-pak-pipeline](photo-to-pak-pipeline.md)). The second (2026-11-15) was a
  six-generation Vauxhall Corsa family (Nova/Corsa A to Corsa F, 24 citycar objects),
  built from a parametric dimension table (`car_builder.py`), rendered at eight views per
  colour, compiled into `citycars.pak`, and loaded by the debug engine in a
  `-generate_map` run that printed `MAP-GEN: PASS`. This was the first multi-model run
  without the user participating in the geometry loop. It also exposed three recurring
  geometry faults, now recorded with fixes in [geometry-pitfalls](geometry-pitfalls.md).
  The third (2026-11-15) was the Ford Fiesta family (Mk1–Mk7, 28 citycar objects), the
  first run executed by delegated subagents (model DeepSeek V4.1 Flash) on the same
  parametric pipeline; the user accepted its renders on 2026-11-15. The fourth (2026-11-15)
  was the single-model BMC1100 (ADO16, 5 colourways), also subagent-executed, including a
  post-build chrome-bumper edit in the 4.5 session without changing the builder code; the
  user accepted its renders on 2026-11-15. The fifth (2026-11-15) was the Ford Anglia 100E
  and 105E (10 colourways), subagent-executed; its renders were REJECTED by the user the
  same day — the brand-defining rear shapes (105E reverse-rake window, 100E spare-wheel boot
  hump) had been omitted as "not readable at pak scale" ([geometry-pitfalls](geometry-pitfalls.md))
  — and a geometry rework is queued. Every numeric check had passed on the rejected renders.
  `[EXECUTION-VERIFIED:2026-11-15]` `[USER-DIRECTION:2026-11-15]`
- **What remains untested**: citycar spawning and image alignment in a running game
  session. `-generate_map` proves the pakset loads and the world initialises; it does not
  advance time far enough for private cars to appear. The image offset table and the
  in-game look of the Corsa and A4 images are still unverified.
- The pre-MCP procedure is superseded: its failures survived every check it had, because it
  could not see the model it was building. Its error categories remain a useful checklist of
  geometry mistakes ([error-categories-pre-mcp](error-categories-pre-mcp.md)).
- Class-specific state: rail placement (front at Y −4.0) and rail/tram/narrow-gauge offsets
  (none); road offsets (standard table, S `,0,0`; see [vehicle](../objects/vehicle.md));
  aircraft procedure ([aircraft-notes](aircraft-notes.md)); private cars
  ([citycar](../objects/citycar.md)). Ships still need per-task treatment. Aircraft values
  do not transfer to ground classes.

## Tooling

- `Git Blends/Pak128.Britain-blends/car_builder.py` — parametric low-poly car builder.
  `SPECS` holds one dict per generation (length, width, height, wheelbase, belt/bonnet/roof
  heights, screen stations, wheel size, bumper material, lamp sizes). `build(name)` creates
  the 15-object assembly in metres; `export_pak_dae()` applies the pak axis factors, writes
  the `.dae`, and reloads the metres master. The geometry rules it encodes (non-coplanar
  appliqués, local taper for lamps, wheel/arch clearances) are in
  [geometry-pitfalls](geometry-pitfalls.md).
- `Git Blends/Pak128.Britain-blends/stageB_car_prepare.py` and `stageB_car_render.py` —
  the 2.79 half of the car pipeline: import/place/attachment-check/save, then render the
  eight views for each paint colour from a JSON colour list. Translate-only; never scale
  in 2.79. The render step has been observed to exit 1 part-way after producing some views
  with no traceback; re-running it for the remaining colours completes the set (2026-11-15).
- `execute_blender_code` runs in a context that loses its window after
  `save_as_mainfile`. Build and save in one call, then call `export_pak_dae()` in a fresh
  call; a save followed by `collada_export` in the same call fails with
  `poll() failed, context is incorrect` ([blender-mcp](blender-mcp.md)).

## Related docs

- [photo-to-pak-pipeline](photo-to-pak-pipeline.md) — the recorded MCP run, rules, and lessons.
- [blender-mcp](blender-mcp.md) — the MCP environment, dispatch workaround, session findings.
- [geometry-pitfalls](geometry-pitfalls.md) — z-fighting, lamp placement and wheel/arch faults found in the first Corsa build, with fixes.
- [error-categories-pre-mcp](error-categories-pre-mcp.md) — historical error checklist.
- [blend-creation](blend-creation.md) — status and failure record entries still relevant.
- [blender-rendering](blender-rendering.md) — 2.79 render workflow and placement records.
- [model-selection](model-selection.md) — model evidence and where models fail.
- [scaling-conventions](../scaling-conventions.md) — axis factors, rulers, oversize rules.
- [liveries-and-special-colours](liveries-and-special-colours.md) — livery system, HSV table.
- [image-layout](image-layout.md) — sheet layout, makeobj image rules.

## Open questions

- Under what demonstrated conditions may AI-authored novel geometry be accepted? The MCP
  procedure makes the question testable; no formal protocol has been run.
- Does the MCP procedure hold for modify-existing geometry (transplants, reshaping) as well
  as for new builds?
- Which further asset classes need canonical placement/offset records?
- How much unattended work is achievable before the user's participation becomes the
  limiting factor?
