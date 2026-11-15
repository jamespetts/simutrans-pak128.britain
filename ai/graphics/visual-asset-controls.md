---
status: draft
verified: New ex-15 @ 937d464a9 (working tree; Anglia completion update, 2026-11-15)
---
# Visual asset process controls

**Covers**: the controls that govern how shape is derived for pakset visual assets, and the
failure analysis behind them. Binds every agent that builds or modifies geometry in Blender,
including delegated subagents. Parent: [graphics-pipelines](../graphics-pipelines.md).
Procedure: [photo-to-pak-pipeline](photo-to-pak-pipeline.md) (canonical procedure record).
Hard rule: [project-notes](../project-notes.md).

## What a run actually needs

**Find sufficient reference images from the angles needed, then build the low-poly model
from them.** For cars that means the finished object in its colourways; for player
vehicles, in its liveries. Everything else is subordinate to that.
`[USER-DIRECTION:2026-11-15]`

1. **Images first.** Typically **1–3 reference images per vehicle** are sufficient (the
   user's manual practice). Real photographs preferred; **drawings are an acceptable source
   where photographs are not available**. Gather the angles needed to build the model: for
   tiny sprites (private cars) the defining views suffice (side profile plus the views
   showing the model's defining features — the Anglia 105E's rear, a finned car's tail);
   large vehicles (trains, aircraft, ships) take more angles because more of their form
   survives at scale. If suitable images cannot be found after honest effort, stop and ask
   the user for them.
2. **Basic measurements, then build.** Always establish the basic measurements — **length,
   width, height, wheelbase** — from the images (published overall dimensions may
   calibrate scale). Secondary measurements (width, height) can often be inferred rather
   than precisely measured, especially for private cars where detail is less critical at
   pak scale. Shape comes from the images, never from text (descriptions, dimension
   boxes, memory).
3. **Same session throughout.** The agent that gathers the images builds the model, with
   the images in its context; never hand the build to a fresh session.
4. **Work visually — the MCP session exists for this.** The working loop is: change
   geometry → capture the model → compare against the reference → correct. Never
   accumulate a run of edits without looking; a checked step every one or two edits is
   the normal rhythm. Before rendering, the model must already stand beside the
   reference at the same angle (Gate B) with a matching silhouette. Numeric checks are
   gross-error detectors only. **A model's own visual acceptance is not reliable**
   `[USER-DIRECTION:2026-11-15]`: delegated runs have accepted plainly wrong shapes after
   looking at them (the Anglia hatchback). The orchestrator must view the run's
   side-by-side evidence itself before acceptance.
5. **The user judges appearance** (Gate C). Report the images used and the side-by-side
   evidence; anything the tooling genuinely cannot express is a question for the user,
   never a silent omission.

## Control system

## Failure analysis: shape from text (2026-11-15)

The Ford Anglia 100E/105E citycars were built from dimension boxes and text descriptions
and produced a generic hatchback silhouette instead of the 105E's defining reverse-rake
rear window; the user rejected the renders. The same process had produced every family
since the Vauxhall Corsa. Evidence trail:

1. The first run (Audi A4 B6) was photograph-based: "from a reference photograph and a
   short description", with photograph ingestion and proportion measurement as stage 1 and
   iteration against the photograph ([photo-to-pak-pipeline](photo-to-pak-pipeline.md)).
2. The photograph requirement was lost when the procedure was restructured for MCP
   (`338e353f6`): the stage list kept "published dimensions, model-year data..." and
   dropped the photograph. No doc stated photographs were mandatory.
3. The parametric builder (`car_builder.py` SPECS dictionaries) made dimension-box numbers
   look like sufficient input; the Corsa run (`0ba8d7fc6`) is recorded as "built from a
   parametric dimension table".
4. Delegated-run briefs codified the text process; fresh-context subagents reproduced it
   literally and confidently.
5. Verification was self-referential: renders compared against other renders and against
   numeric baselines (cluster counts, pixel sizes, mean RGB). Every check passed on the
   rejected Anglia renders.
6. Human gates were dropped in delegation: spec approval before build became a final-report
   line, and "the builder cannot express X" was recorded as a deviation instead of a stop.
7. The error recurred at orchestration level: a rework brief asserted rear-window geometry
   from memory (in the wrong direction), and a shape question was answered from Wikipedia
   prose. The user's screenshot caught it.

Root cause: the source of shape moved from photographs to text at the builder/brief layer;
downstream checks were relative (render vs render) instead of absolute (model vs
photograph); and the pre-build human gates were not carried into the delegated process.
`[USER-DIRECTION:2026-11-15]` `[CODE New ex-15 @ 67d641657]`

The rejected Anglia outputs have been replaced by photograph-referenced models accepted
by the user and compiled into the local citycars pak. The failure analysis above remains
the reason for retaining these controls. Accepted sources:
[anglia-sources](anglia-sources.md).
`[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`

## Session continuity (hard rule)

**Research and build happen in ONE session.** The agent that gathers and measures the
reference photographs MUST be the same agent that builds the geometry, in the same
session, so the images remain in its context while it works. Never split "research
session" from "build session", and never hand a spec to a fresh agent to build: a fresh
context cannot see the photographs and repeats the shape-from-text failure. Gate
compliance is reported in the run's final report; the orchestrator reviews it and the
renders, and Gate B matching happens inside the same session. If a user checkpoint is
wanted mid-run, the run pauses and RESUMES IN THE SAME SESSION — never by delegation.
`[USER-DIRECTION:2026-11-15]`

## Control system

Every visual asset run, human- or subagent-driven, passes these gates in order. A run that
cannot pass a gate stops; it does not proceed on judgement.

1. **Gate A — reference gate (before any geometry).** Reference images in hand:
   typically **1–3 per vehicle** (photographs preferred, drawings where photographs are
   not available), covering the angles needed — defining views for tiny sprites, fuller
   coverage for large vehicles. Basic measurements (length, width, height, wheelbase)
   established from the images. If suitable images cannot be found after honest effort,
   stop and prompt the user to supply them. `[USER-DIRECTION:2026-11-15]`
2. **Gate B — shape-match gate (before rendering).** The model is captured at a
   photograph's angle and placed beside the photograph; the silhouette is iterated until
   it matches the photograph. Comparisons are model-vs-photograph only; model-vs-render or
   model-vs-numeric-baseline comparisons can never pass this gate (they passed on the
   rejected Anglia). Numeric checks remain gross-error detectors only.
3. **Gate C — user acceptance (after renders).** The human judges the renders against the
   photographs. Acceptance is recorded in the run history; AI readings are working tools.
4. **Escalation rule.** "The builder cannot express X" or "X does not read at pak scale"
   concerning a shape-defining feature is a **stop condition**: the user decides whether
   the feature is built another way, the builder is extended, or the asset is dropped.
   It is never recorded as a deviation and continued.
5. **Vision requirement.** The agent that controls the Blender MCP must be able to view
   images (photographs and renders) and must do so; a text-only model cannot run this
   process. Runs self-test this before starting (view the reference photographs and state
   what is seen).
6. **Report compliance.** Every run report contains a compliance section answering gates A
   and B and listing any escalations. Orchestrators reject reports without it.
7. **Source of truth.** [photo-to-pak-pipeline](photo-to-pak-pipeline.md) is canonical for
   the shape-source procedure; [ai-pipeline](ai-pipeline.md) carries the stage wording and
   pointer; [project-notes](../project-notes.md) carries the hard rule. Standing briefs
   used for delegated runs must reproduce the rule and gates and are checked against these
   docs at each run. `[USER-DIRECTION:2026-11-15]`

## Open questions

- Whether landmark measurement from arbitrary photographs can be automated, or the
  measure-then-build loop stays semi-manual (carried over from
  [photo-to-pak-pipeline](photo-to-pak-pipeline.md)).
- Whether the two-phase gate A (spec returned for check) is fast enough in practice for
  multi-generation families, or needs a batch form.
