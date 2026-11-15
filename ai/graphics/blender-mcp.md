---
status: draft
verified: New ex-15 @ 66e9c2dfd
---
# Blender MCP

**Covers**: the Model Context Protocol link between the AI agent and a live Blender session —
the installed environment, what it may and may not write, and its status. Parent:
[graphics-pipelines](../graphics-pipelines.md).

**Status: tested end to end once, on one experimental asset** (Audi A4 B6, 2026-11-14/15),
not yet a pakset object; user hand-edits the scene in parallel; AI reading of renders is
displaced for iteration but not for verification. No pakset object has been produced through
it. Current status of AI-authored geometry and the failure record that motivates this route:
[blend-creation](blend-creation.md). Pipeline lessons and file-placement rules recorded in
[photo-to-pak-pipeline](photo-to-pak-pipeline.md).

## Session findings 2026-11-14/15 (Audi A4 B6, first full Stage A→B run)

- `execute_blender_code` is racy on dispatch: results alternate between Python results from
  the addon and bare JS-engine errors (`ReferenceError`, `SyntaxError … plain JavaScript`).
  Working protocol: send multi-line payloads starting `import bpy`; wrap every call in a
  retry loop that stops on `Code executed successfully` or `Error executing code:`; make
  payloads idempotent (delete named objects/materials before creating them); verify effects
  afterwards by reading, never by trusting the result string.
- `look` returns a viewport image directly into the task — usable for iteration review;
  axis-orthographic via `view_axis` needs a `temp_override(area=…, region=…)` around it;
  perspective 3/4 is the default view user reviews prefer; frame with
  `region_3d.view_distance` / `view_location`; set shading to `MATERIAL` to see materials;
  `hide_set` cameras/lights to cut clutter.
- Hand edits happen in the live session *while the agent works*: user edited the headlamps
  in 4.5 mid-flow. Rule: the 4.5 `.blend` must be saved regularly (`wm.save_as_mainfile`
  with an absolute path) so agent rebuilds may not silently overwrite human edits, and the
  `.blend` in `4.5/` is the irreplaceable source of truth; the `.dae` is derived from it.
- **Never rename an object without a before-and-after world-space bounds print.** Two
  rename attempts produced `.001` suffixes, a mangled `Rear_Valance`→`Rear_VaR` /
  `Bumper_R`→`BumperR`, and a left/right swap of every mirrored part. `_L`/`_R` suffixes
  = vehicle's own frame (front −Y ⇒ left = +X).
- **Never trust a global bbox as proof of model correctness.** Cuboid-positioned parts
  survived a mesh-only scale (floating ~3.5 m ahead of the car) while the global bbox
  passed. The reusable gates are: per-object attachment check vs the hull bbox, and
  post-render connected-cluster analysis of all non-transparent pixels. The "8/8 must be
  one cluster" form of the latter is not reliable at pak scale: the accepted A4 renders
  themselves split into 2–3 clusters in NW/SE. Use cluster counts as a diagnostic against
  a known-good baseline, not as a pass/fail gate ([geometry-pitfalls](geometry-pitfalls.md)).
- **`save_as_mainfile` destroys the window context for the rest of the call.**
  `bpy.ops.wm.collada_export` then fails with `poll() failed, context is incorrect`, and
  `bpy.context.window` can be `None`. Build and save in one `execute_blender_code` call,
  then export in a fresh call. Multi-model loops that save and export in the same call fail
  on the first export. `[EXECUTION-VERIFIED:2026-11-15]`
- **`look` needs `mode: "angles"` to choose a view.** With `mode: "viewport"` the `view`
  and `distance` parameters are ignored and every call returns the same user viewport.
  `mode: "angles"` with `views: ["front","right","three_quarter","top"]` and a `distance`
  gives a labelled multi-view tile. `[EXECUTION-VERIFIED:2026-11-15]`
- **The connection drops when Blender 4.5 exits**, whether closed by the user or crashed.
  The addon reports `Connection to Blender lost` and every later call returns
  `Not connected to Blender`. Relaunch 4.5 (with the master file) and wait for port 9876
  to listen again; the MCP server reconnects without restarting OpenCode.
  `[EXECUTION-VERIFIED:2026-11-15]`

## Why this route is favoured

The recorded failures are not coding failures. They are failures of geometric foresight: code
that runs and builds the wrong shape, parts that do not move with their dependencies, and an
inability to detect either from the code
([blend-creation](blend-creation.md), failure record). Blender MCP addresses the mechanism
directly. It gives the agent three capabilities the file-and-script pipeline cannot: queries
against the live scene graph, rendered views of the result within the same turn, and bounded
single operations instead of whole-file rewrites.

The external evidence for this ordering is in [model-selection](model-selection.md).

## Installed environment

Measured on the maintainer's machine, 2026-11-14 `[EXECUTION-VERIFIED:2026-11-14]`:

| Component | Version | Path |
| --- | --- | --- |
| Blender | 4.5.16 LTS (built 2026-11-10) | `C:\Program Files\Blender Foundation\Blender 4.5\` |
| uv / uvx | 0.13.8 | `%USERPROFILE%\.local\bin\` |
| MCP server | `mcp-for-blender` 2.2.9 (PyPI; formerly `blender-mcp`) | run on demand by uvx |
| Blender addon | `blender_mcp.py`, addon 2.0, protocol 16 | `%APPDATA%\Blender Foundation\Blender\4.5\scripts\addons\` |
| Client configuration | project-scoped `mcp.servers.blender` | `opencode.json` in the base workspace |

Connection: the addon opens a socket on `127.0.0.1:9876` when Blender starts; the server
connects to it. Addon version and protocol are checked on connect and reported by the addon
status tool. Abilities advertised at protocol 16: `execute_code`, `get_scene_info`,
`get_object_info`, `list_scene_items`, `bpy_api_lookup`, `describe_node_type`,
`get_viewport_screenshot`, `pick_viewport_object`, `get_world_state_snapshot`,
`drain_human_activity`. `[EXECUTION-VERIFIED:2026-11-14]`

Telemetry consent is off. Asset libraries (Poly Haven, Sketchfab, Poly Pizza) and generators
(Tripo, Hunyuan3D, Hyper3D, Meshy) are all off and require API keys; none is needed for pakset
work. `[EXECUTION-VERIFIED:2026-11-14]`

## Role in the pipeline

Blender 4.5 is the **Stage A editor**, driven through the MCP server; the version split in
AGENTS.md hard rule 5 (amended 2026-11-15) is:

- It may read, modify, and save `.blend` files. Any `.blend` it saves must live in a `4.5/`
  subdirectory of the relevant blends folder (for example
  `citycars/4.5/audi-a4-b6.blend`), kept separate from the 2.79-era `.blend` files. The 4.5
  file is the master source for the asset; the `.dae` is derived from it.
- It does not render the pakset views: rendering remains in Blender 2.79, whose software
  renderer the render scripts depend on. 4.5 viewport renders (the `look` tool) are used for
  iteration, not for pak output.
- Geometry produced in 4.5 reaches the render pipeline only as `.dae` (already at pak scale,
  see [ai-pipeline](ai-pipeline.md)), and must be re-verified after import into 2.79.
  Interchange is lossy: triangulation, dropped modifiers, lost face images, renamed
  duplicates ([error-categories-pre-mcp](error-categories-pre-mcp.md)).

## Interchange constraint

Blender 5.0 removed native Collada support (`.dae` import and export, upstream pull request
139337), so `wm.collada_export` does not exist in 5.x. This is why 4.5.16 LTS was installed
rather than a 5.x release: `.dae` is the only route from modern geometry into the 2.79 render
rig, and 4.5 is the newest release that keeps it built in. `[EXECUTION-VERIFIED:2026-11-14]`

Round-trip verified 2026-11-14: a 2 m cube exported from 4.5.16 (`wm.collada_export`, 10,085
bytes) imported into Blender 2.79 headless with 8 vertices, correct 2×2×2 dimensions, and 6
quads arriving as 12 triangles — the same triangulation behaviour recorded for the 2.81 to 2.79
interchange in [proposed-geometry-pipeline](proposed-geometry-pipeline.md).
`[EXECUTION-VERIFIED:2026-11-14]`

If a 5.x Blender is ever required, `.dae` needs a third-party extension; none has been tested
against this pipeline. Treat that as an open question, not a plan.

## Known limits

- The published benchmarks behind the favouring of this route evaluate editing of single
  procedural objects. They do not test multi-part vehicle assemblies on layered scenes, nor a
  2.79 render step ([model-selection](model-selection.md)). Transfer is expected, not
  demonstrated.
- An MCP session drives one live Blender instance. It is not a headless batch build, so it does
  not replace the makeobj and render stages.
- AI reading of rendered images can be wrong even with the MCP supplying them: on
  2026-11-15 the agent explained detached parts as anti-aliasing while the actual cause was a
  mesh-only scale in 2.79. Render readings inform iteration; they are not verification
  ([blend-creation](blend-creation.md), verification doctrine).

## Open questions

- What is the smallest asset on which the MCP route can be judged? The recorded failure cases
  (B12/3 frame profile, S69 boiler transplant) are re-runnable under a fixed protocol and would
  test the recorded failure modes directly, but no such run has been attempted.
- Does `BLENDER_MCP_SAFE_MODE=1`, which checks generated code before execution, block operations
  the pakset needs? It is unset in the current configuration.
- Should the MCP route run against 2.81 instead of 4.5? 4.5 was chosen for addon compatibility
  and current API documentation coverage, not because the pipeline requires it. The
  2026-11-15 rule makes 4.5 the Stage A editor; 2.81 remains legacy.
