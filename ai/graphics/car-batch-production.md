---
status: draft
verified: none
---
# Private-car batch production (divided workflow)

**Covers**: the division of private-car asset production between a research and integration
agent and a delegated Blender builder agent on a frontier model: what each side owns, the
build brief, the files handed back, and how the acceptance gates are kept. Parent:
[graphics-pipelines](../graphics-pipelines.md). Mandatory controls:
[visual-asset-controls](visual-asset-controls.md). Stage detail:
[photo-to-pak-pipeline](photo-to-pak-pipeline.md) and [ai-pipeline](ai-pipeline.md).
Private-car fields and conventions: [citycar](../objects/citycar.md). Ordered list of cars to
build: [citycar-asset-gaps](../objects/citycar-asset-gaps.md#build-order).

Status: draft, created 2026-11-15 at the user's direction for the private-car backlog.
`[USER-DIRECTION:2026-11-15]`

## Why the work is divided

Geometry authoring is the part that needs the strongest model, and therefore the most expensive
one. The surrounding work — finding and checking photographs, fixing dimensions and colour
ranges, computing colour shares and weights, writing the `.dat`, the text entry and compiling
the pak — is text and arithmetic work that a cheaper model does reliably. Dividing the work at
that line keeps the expensive model on geometry only.

The evidence that geometry is the hard part is the recorded failure class: models that write
code which runs and builds the wrong shape, most often through poor geometric foresight rather
than coding error ([model-selection](model-selection.md#where-failures-come-from)). Supplying the
builder with the photographs themselves, and requiring comparison against them, is the control
that addresses that failure class.

| Role | Who | Owns |
| --- | --- | --- |
| Orchestrator | the session agent, normally the cheaper model | research pack, build brief, file routing, `.dat` and text entry, Stage B render, compilation, first view of the gate evidence, reporting to the user |
| Builder | delegated agent on the strongest available geometry model | reference self-test, Stage A geometry in the live Blender 4.5 MCP session, Gate B comparisons, metres master, pak-scale `.dae`, colour list |
| User | the maintainer | Gate C appearance acceptance, and any decision on an escalation |

## Hard rule: the brief carries images, not shape

**The builder must receive the reference image files and must view them before any geometry.**
This is the operative content of the session-continuity rule in
[visual-asset-controls](visual-asset-controls.md#session-continuity-hard-rule), restated for the
divided workflow: the rule exists because a text-only brief cannot convey shape, and a delegated
builder that never sees the photographs repeats the shape-from-text failure. Delivering the
photographs to the builder satisfies it; describing the shape in prose does not, and is
forbidden however detailed the description.

The builder may not delegate the geometry further. Research and build stay in one builder
session, so that the images the builder measured from remain in its context while it works.

Gate A is therefore satisfied twice: the orchestrator establishes the images and the basic
measurements before writing the brief, and the builder re-tests them by viewing each image and
stating what it shows before it models anything. A builder that cannot see the images must stop,
not proceed from the brief's text.

## What the orchestrator researches first

One research pack per car, saved under
`Git Blends/Pak128.Britain-blends/citycars/references/<slug>/`. That folder is **gitignored**:
reference photographs and brochure scans are third-party research material and are never
committed or pushed. Every item is recorded with its source; the rules are in
[calibration-sources](../calibration-sources.md).

1. **Identity.** Maker, model and exact generation, with the UK production years, confirmed
   from the image page or a maker source rather than from memory. A wrong generation silently
   produces a wrong car.
2. **Photographs.** Normally 1–3, covering the angles needed to build: a level side profile with
   the wheels visible, a front three-quarter, a rear three-quarter, and whichever additional
   view shows the model's defining feature. Real photographs first; scale drawings where no
   suitable photograph exists. Record the source URL, the licence and a one-line statement of
   what the image shows.
3. **Basic dimensions.** Overall length, width, height and wheelbase from a published source
   (maker handbook, road test, or dimension table). These calibrate scale; they do not supply
   shape.
4. **Colour range.** The UK paint names offered on that generation, with the years each was
   offered. Omit rare colours; keep the ones actually common on the road.
5. **Colour shares and weight.** Colour-split `DistributionWeight` from the measured shares,
   era-adjusted where the measured years are later than the car, and the model's total weight
   from the parc evidence against the era anchor. Method and anchors:
   [citycar](../objects/citycar.md#colour-rule) and
   [citycar-parc-anchors](../objects/citycar-parc-anchors.md).
6. **Game values.** Per-colour intro and retire dates, speed, comfort, class bands, object name
   and copyright, and the `New/text/en.tab` entry. Conventions:
   [citycar](../objects/citycar.md#fields-one-objcitycar-per-colour).

The research pack is complete when the brief can be written without further searching. Finding
one more photograph is cheaper than one more build cycle.

## The build brief

The brief is a single message to the builder. It contains the following, in this order.
`<blends>` below is the root of the blends repository,
`Git Blends/Pak128.Britain-blends/`.

```
TASK: build the <maker> <model> <generation> private car for pak128.Britain-Ex, Stage A only.

1. REFERENCE OWNERSHIP
   Read [visual-asset-controls.md] and [geometry-pitfalls.md] first.
   Read every image in <reference directory>. Before any modelling, state in one line
   per image what it shows and which angle it is. If an image does not show the car,
   stop and say so.

2. REFERENCE FILES
   <absolute path> -- <what it shows, angle>
   <absolute path> -- ...
   <absolute path> -- ... (scale drawing, if any)

3. MEASUREMENTS (calibration only; shape comes from the images)
   overall length <m>, width <m>, height <m>, wheelbase <m>; source <...>.
   Measure the proportions from the images and reconcile; if the images and the
   published dimensions disagree, report the disagreement instead of choosing silently.

4. WHAT TO BUILD
   Object prefix: <ObjectPrefix>. Save the metres master to
   <blends>/citycars/4.5/<slug>.blend. Export the pak-scale .dae to
   <blends>/citycars/4.5/<slug>.dae.
   Parts: lower body, upper body and glazing, four wheels, bumpers, lamps, grille and
   any trim the photographs show. One <ObjectPrefix>Paint material; the render driver
   looks it up by that exact name, so it must carry no .001 suffix.
   Detail budget: at 128 px the car reads by silhouette, roof line, wheel position, lamp
   shapes and colour. Build to that; do not model what cannot be seen.

5. GATES
   Gate B: capture the model at each reference angle and place the capture beside that
   photograph. Iterate until the silhouettes match. Then capture a full turn (eight
   views) and check coherence: no gaps, no floating parts, no surface contradicting a
   matched view. Keep every comparison image.
   Escalation: if a shape-defining feature cannot be expressed, STOP and report it. Do
   not record it as a deviation and continue.

6. RETURN
   metres master saved; .dae at pak scale (X/Z 0.70942, Y 0.56754 applied and the
   metres state restored before saving); colour list JSON in the form
   [["blue", [r,g,b]], ...] at <blends>/citycars/<slug>-colours.json; the
   comparison images; an object list with per-object world bounds; a report with a
   compliance section stating what each reference image shows and the Gate B
   comparison made from it.
```

Rules for writing the brief:

- Name parts and materials, never profile or proportion. "Reverse-rake rear window" is a shape
  description and belongs only in the `.dat` comment after the model exists.
- Give absolute paths. The builder has no memory of this session.
- Name one car, or one family that shares a shell, per brief. A family brief is acceptable only
  where the generations differ in trim and not in body.
- State the colour list once; the builder does not choose colours.

## What comes back, and what the orchestrator does with it

1. **Check the builder's own evidence.** Open every comparison image and judge it against the
   photograph. A builder's statement that the silhouette matches is not evidence; delegated runs
   have accepted plainly wrong shapes ([visual-asset-controls](visual-asset-controls.md)).
   A mismatch is **not** sent back automatically: record the fault and put it to the user, who
   decides whether a correction round is paid for (below).
2. **Stage B.** Run `stageB_car_prepare.py` then `stageB_car_render.py` in headless Blender
   2.79, translate-only, with the colour list. Check the images that were actually written:
   expected count, 128 × 128 RGBA, non-empty alpha. Blender 2.79 can exit 1 after writing a
   complete set, so inspect output rather than trusting the exit code.
3. **Install.** Copy the renders into `New/citycars/images/` under
   `<slug>-<colour>_<VIEW>.png`.
4. **Write the `.dat`.** One `obj=citycar` per colour, with the header comment recording
   identity, dimensions, paint names, share years, weight reasoning and the metres master path.
   Add the `New/text/en.tab` entries in the same change.
5. **Compile.** `make citycars DESTDIR=.` through MSYS2 (the `make` binary is
   `C:\msys64\usr\bin\make.exe` when it is not on `PATH`); the build is the validity
   check for the fields. Without `make`, the same result is
   `./makeobj-extended PAK128 pak128.Britain-Ex/citycars.pak citycars/` from `New/`. The
   folder argument must end in a forward slash: without it makeobj writes an empty pak and
   still exits 0, so check the packed-object count or the pak size.
6. **Report to the user for Gate C** with the renders and the photograph comparisons. The user
   judges appearance; compilation and file checks do not substitute for that.

## Correction rounds are the user's decision

**A delegated build gets one paid geometry pass by default.** The orchestrator does not send a
second round on its own, however clear the fault. It reports:

- the reference photograph beside the builder's same-angle capture;
- the specific faults in plain terms (for example "the nose is a vertical slab; the brochure
  shows a long low taper");
- whether each fault still reads at 128 px.

The user then chooses: accept as built, authorise one correction round, or drop the asset. Only
an authorised round goes back to the builder, and it goes back to the same session with the
authorised faults only.

Why: a correction round re-edits geometry and re-runs every comparison at frontier prices, and
the orchestrator's own visual judgement is not acceptance evidence. An automatic loop can spend
several rounds on a difference the user would have accepted or rejected at once.
`[USER-DIRECTION:2026-11-15]`

Raise a fault when the first pass is badly wrong, judged at the asset's actual size
([visual-asset-controls](visual-asset-controls.md#strictness-scales-with-the-objects-size)):

- for the smallest assets (motorcycle outfits, tiny cars), the outline does not read as the
  subject;
- for cars, a defining feature is missing, mirrored, or in the wrong part of the object;
- parts float, intersect each other, or the separate clusters do not connect;
- the model contradicts a reference photograph in a way a viewer would notice at pak scale.

Do not raise, and do not correct: details invisible at pak scale (spokes, seams, fixings,
upholstery), minor trim, or a difference the reference does not settle. Note them in the report
if they matter for a later rework, and proceed.

A first pass that passes the orchestrator's check goes to Stage B without asking.

## Order and cost

- Builds are serial: one live Blender session drives one instance, so a batch runs one car at a
  time. Keep the session open across a family to save startup and reference reloading.
- Default builder: GPT-6.2 Sol (`opencode/gpt-6.2-sol`), which superseded 6.1 Sol on 2026-11-18.
  The 6.1 evidence base remains the reason this family is used at all: it is the only model
  recorded as successful on this project's Blender MCP work. Selection evidence:
  [model-selection](model-selection.md#local-blender-mcp-model-experience). Dispatch it as the
  `general` subagent with that model set; the `blender-geometry` subagent runs the headless
  Blender 2.79 measure-render loop and is not the route this workflow uses.
  `[USER-DIRECTION:2026-11-18]`
- **Builder effort** `[USER-DIRECTION:2026-11-16]`: `#low` by default for cars, motorcycles
  and small vans; `#medium` for cars with complex shapes or glazing, and for lorries and buses;
  `#high` for aircraft and ships. The effort variant is set on the subagent's model string,
  for example `opencode/gpt-6.2-sol#low`. Cars count as complex where wraparound or
  multi-plane glazing, compound curves or flush lamp/glass graphics are defining features;
  boxy three-box saloons and simple hatchbacks do not. Repeated low-effort builds of
  glazing-heavy cars produced intersections and obscured lamps (Astra Mk6-Mk8, Beetle,
  Golf Mk2, Continental GT), which is what the complex-shape exception covers.
- **Build the whole family, not one mark.** If a model is worth building, build every major mark or
  generation in the same run — the Cavalier means Mk1, Mk2 and Mk3; the Astra means every major
  mark; the Sierra means Mk1–Mk3, each with several realistic colourways. A single mark is only
  acceptable where the later marks share the shell or are already in the tree. The one exception
  is a deliberate sample to test the pipeline, not a production asset. `[USER-DIRECTION:2026-11-15]`
- **Glazing must sit proud of the body, never inside it.** Build each window as a
  separate panel lying 0.01-0.02 m outside the body surface, with the windscreen clearly
  visible from the front. Embedded or intersecting glazing has failed Gate B repeatedly
  (Astra Mk6-Mk8, Beetle, Golf Mk2, Continental GT) even when the silhouette is right.
  `[EXECUTION-VERIFIED:2026-11-16]`
- **Glazing colour is pure black, lightness zero, in every asset.** The glazing material's
  diffuse colour must be exactly `(0.0, 0.0, 0.0)`; the pakset convention is black glass, and
  dark grey reads as a different material at sprite scale. State this in every builder brief,
  alongside the glazing geometry rule, and have the builder report the material name and RGB.
  `[USER-DIRECTION:2026-11-16]`
- A correction round is a second full geometry pass at frontier prices. Budget one build per
  car; a second round is the user's decision, never the orchestrator's ([above](#correction-rounds-are-the-users-decision)).
- Do not spend builder tokens on research, `.dat` writing, text entries or compiling. Those are
  orchestrator work by design.
- Collect the reference pack for the next car while the builder works on the current one; the
  two activities do not contend for Blender.

## Failure guards

| Failure | Guard |
| --- | --- |
| Brief states shape in prose and the builder never opens the images | The brief's first section orders the builder to describe each image before modelling; a report without that section is rejected |
| Builder accepts its own render | Orchestrator views every comparison before Stage B |
| Orchestrator sends correction after correction on its own | Every mismatch stops and goes to the user; no automatic second round ([above](#correction-rounds-are-the-users-decision)) |
| Builder saves the metres master at pak scale | Export applies the axis factors to temporary copies and restores them in `finally` ([ai-pipeline](ai-pipeline.md)) |
| Material arrives as `<Prefix>Paint.001` | Brief names the exact material; render driver fails loudly if the lookup misses |
| Colours chosen by the builder | Colour list is fixed in the brief and returned as data |
| Wrong generation photographed | Identity is confirmed at research time, before the brief is written |
| Subagent loses the Blender connection | Reopen 4.5 with the saved master, verify, continue the same session ([blender-mcp](blender-mcp.md)) |

## Open questions

- Does GPT-5.6 Terra, the Terra model the provider actually offers, complete a photograph-matched
  car to the standard Sol reached? One measured run would answer it; no run has been made.
- How many cars can one builder session produce before its context degrades enough to justify a
  fresh session, and does a fresh session with the same reference pack hold quality?
- Should the builder return the `.dae`, or should the orchestrator re-export it from the metres
  master to keep the scaling step under one owner?
