---
status: draft
verified: New ex-15 @ 937d464a9 (working tree; Anglia completion, divided-workflow amendment and correction-round control, 2026-11-15)
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
   the normal rhythm. Each capture is taken from the angle of one of the reference
   images, and the views for which no reference exists must also be captured and be
   coherent with them (same-angle capture rule, Gate B below). Before rendering, the
   model must already stand beside the
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

**Divided workflow (amendment, 2026-11-15).** Photograph sourcing and measurement may be done
by an orchestrating agent, with the geometry built by a delegated builder agent on a frontier
model. This replaces the requirement above that one agent both gathers and builds; every other
part of the rule stands, and its operative requirement is unchanged: **the brief must deliver
the image files themselves, the builder must open and view them before any geometry, and the
builder must measure the subject from them.** A brief that conveys shape in words — profile
descriptions, proportions, a named rear-window form — instead of images is the failure this
section exists to prevent, whatever the division of labour. Research and build remain one
session for the builder, which may not delegate further, so that the images it measured from
stay in its context; a mid-run pause still resumes in that same builder session. Division
mechanics and the brief template: [car-batch-production](car-batch-production.md).
`[USER-DIRECTION:2026-11-15]`

## Strictness scales with the object's size

**The smaller the object on screen, the more lenient the acceptance; the larger the object, the
stricter.** At the scale of a motorcycle-and-sidecar outfit — a few pixels in a 128 px sprite —
errors in internal detail are invisible, so the outline is the only thing worth judging. The
same calibration runs up the asset classes. `[USER-DIRECTION:2026-11-15]`

| Asset | What is judged |
| --- | --- |
| Motorcycle outfits and the smallest private cars | the outline only: does the silhouette read as the subject? Internal detail, trim and surface errors are accepted. |
| Private cars | the outline plus the defining features: grille, rear-window form, lamp shape, colour split. |
| Trains, trams and other large vehicles | structure, windows, livery, underframe and running gear; still low-poly. |
| Ships and aircraft | major forms, superstructure and livery; still low-poly. |

Practical effect: do not spend a correction round, and do not record a fault, for anything that
cannot be seen at the sprite's actual size. A missing grille on a car matters; a missing exhaust
on an outfit does not. This calibrates what the orchestrator raises, not who accepts: the user
remains the judge of appearance at every size.

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

   **Same-angle capture rule (2D images → .blend).** The 2D-image-to-.blend workflow
   ALWAYS requires views of the model to be captured regularly during construction, and
   every capture is taken **from the same angle as one of the reference images**. At each
   such angle the model's silhouette and visible features must match the reference image.
   Views for which no reference image exists must also be rendered, and must be coherent
   with the matched angles: no gaps, no floating or detached parts, and no surface that
   contradicts a matched view. A run has not passed Gate B until it has captured the
   reference angles and matched them, regardless of any other check it has passed.
   `[USER-DIRECTION:2026-11-15]`

   **Material rule — glazing is pure black.** The glazing material's diffuse colour is
   exactly `(0.0, 0.0, 0.0)`, lightness zero, in every asset; a dark grey or blue-grey reads
   as a different material at sprite scale. The render driver forces any material whose name
   contains `Glass` or `Glazing` to black, but the master itself must also carry black so the
   convention survives any other render path. Builders report the material name and RGB.
   `[USER-DIRECTION:2026-11-16]`
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
8. **Correction rounds are the user's decision.** On delegated private-car batch runs, when the
   orchestrator finds a mismatch it records the fault and presents it; it does not send the
   builder an automatic second round. The user authorises any correction round. For other asset
   classes the user sets the policy per run. Badly-wrong threshold and reporting form:
   [car-batch-production](car-batch-production.md#correction-rounds-are-the-users-decision).
   `[USER-DIRECTION:2026-11-15]`

## Open questions

- Whether landmark measurement from arbitrary photographs can be automated, or the
  measure-then-build loop stays semi-manual (carried over from
  [photo-to-pak-pipeline](photo-to-pak-pipeline.md)).
- Whether the two-phase gate A (spec returned for check) is fast enough in practice for
  multi-generation families, or needs a batch form.
