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
`Git Blends/Pak128.Britain-blends/`; makeobj (`Makeobj-Extended-ex-15.exe` for ex-15); small
checker scripts in `ai/temp/` per session (per-object attachment check, PNG cluster
analysis).

## Procedure status

- **MCP has been shown to be the only process that works to any extent.**
  `[USER-DIRECTION:2026-11-15]`
- **As of 2026-11-15 the extent to which it works is somewhat uncertain.** One end-to-end
  run exists (an Audi A4 B6 saloon taken through geometry, six colour variants, render and
  makeobj compile into a private car; [photo-to-pak-pipeline](photo-to-pak-pipeline.md)).
  Whether the procedure holds on other classes, on modify-existing geometry, and at
  unattended quality without the user's active participation is untested. This section is
  to be reviewed and updated by the AI when the effectiveness is more clearly established.
  `[USER-DIRECTION:2026-11-15]`
- The pre-MCP procedure is superseded: its failures survived every check it had, because it
  could not see the model it was building. Its error categories remain a useful checklist of
  geometry mistakes ([error-categories-pre-mcp](error-categories-pre-mcp.md)).
- Class-specific state: rail placement (front at Y −4.0) and rail/tram/narrow-gauge offsets
  (none); road offsets (standard table, S `,0,0`; see [vehicle](../objects/vehicle.md));
  aircraft procedure ([aircraft-notes](aircraft-notes.md)); private cars
  ([citycar](../objects/citycar.md)). Ships still need per-task treatment. Aircraft values
  do not transfer to ground classes.

## Related docs

- [photo-to-pak-pipeline](photo-to-pak-pipeline.md) — the recorded MCP run, rules, and lessons.
- [blender-mcp](blender-mcp.md) — the MCP environment, dispatch workaround, session findings.
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
