---
status: draft
verified: New ex-15 @ 937d464a9; GitBlends master @ 8d4bf9e0 (Anglia-related working-tree checks, 2026-11-15)
---
# Low-poly vehicle geometry pitfalls

**Covers**: recurring geometry faults found while building the Corsa and Anglia models in
Blender 4.5 through MCP, and the construction checks that detect or prevent them. Applies
to Stage A vehicle builds generally. Parent: [graphics-pipelines](../graphics-pipelines.md);
procedure: [ai-pipeline](ai-pipeline.md).

These are working notes, not a reviewed standard. Numeric construction checks supplement
photograph comparisons and user acceptance; they do not replace them.
`[EXECUTION-VERIFIED:2026-11-15]`

## Missing brand-defining silhouette (Ford Anglia rear, rejected 2026-11-15)

**Symptom**: the Anglia 100E/105E renders read as generic modern cars from behind — the user
rejected them: "They were famous for their rear shape, but these renders look like modern
hatchbacks. These need re-doing." `[USER-DIRECTION:2026-11-15]`

**Mechanism**: the rejected build treated the rear shapes as omissions permitted by the
builder, rather than matching photographs. The 105E's reverse rake means that the window
**top is rearward of its base**, not forward of it. The 100E is a different generation,
with conventional sloping rear glass and a separate rounded boot; describing that boot as
an external spare-wheel hump was incorrect. Its accepted replacement has a shallow crown,
reduced after the user found the first rework too bulbous.
`[EXECUTION-VERIFIED:2026-11-15]` `[USER-DIRECTION:2026-11-15]`

**Rule**: if a feature defines the model's recognisable silhouette (reverse-rake window,
separate boot, fins, sloping or upright tail), it must be modelled even when the builder
cannot express it, using a post-build geometry edit in the 4.5 session (the BMC1100 chrome
bumper is the precedent). Any "does not read at pak scale" judgement about a silhouette
feature must be referred to the user at the spec stage, not decided in the build. Numeric
checks (cluster count, pixel size, colour) cannot detect this class of error: all of them
passed on the rejected renders. `[EXECUTION-VERIFIED:2026-11-15]` `[USER-DIRECTION:2026-11-15]`

The Anglia rework is accepted and installed; its maintained source files are identified in
[anglia-sources](anglia-sources.md). The failed build remains a reason to retain the
reference and human-review controls, not an outstanding Anglia rework.
`[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-15]`

## Photograph identity and camera angle

Inspect the actual image before assigning its use. A front three-quarter Anglia photograph
had been labelled a side profile in the rejected spec. Published overall dimensions do
not turn oblique image coordinates into orthographic lengthwise positions. Establish the
basic dimensions, compare the model at the photograph's angle, and refine the geometry
visually; do not treat approximate positions inferred from perspective as precise
measurements. Follow the [reference controls](visual-asset-controls.md).
`[EXECUTION-VERIFIED:2026-11-15]`

## Attachment checks need the actual support surface

- `stageB_car_prepare.py` compares every part's bounding box with
  `<ObjectPrefix>_Hull`. A lower-body-only hull can falsely reject trim attached to the
  cabin roof. The Anglia builder's `finish_shell()` includes cabin and glazing in that
  reference shell. Check the intended supporting mesh rather than moving correct roof
  trim downwards to satisfy an incomplete bounding box.
- Bounding-box overlap is a gross-error check, not proof of surface contact. On a curved
  rear wing, a flat lamp panel can be exposed above the body or buried inside it while its
  overall box overlaps the hull. The 100E builder's `fit_rear_lamps()` projects the lamp
  geometry onto the actual rear surface and closes its back inside the body.
- Fit boot seams and handles to the revised body surface after changing its curvature;
  retaining their earlier coordinates can leave detached details.

`[EXECUTION-VERIFIED:2026-11-15]`

## Closed tyres and matching panel boundaries

- A tread band and hubcap do not close the tyre's sidewalls. Build a closed wheel profile
  and check for non-manifold edges again after Collada import. The Anglia wheels were
  checked in both Blender stages.
- A curved windscreen or rear window must share the complete sampled boundary of its
  supporting roof. A four-corner boundary below a crowned roof leaves a visible opening.
  Include the roof's cross-section breaks and remove any painted support faces that would
  obscure the glazing. See `anglia_mesh.py::screen()`.

`[EXECUTION-VERIFIED:2026-11-15]`

## Coplanar detail faces (z-fighting)

**Symptom**: jagged black/red patches on the nose or tail, in the 4.5 viewport and in the
2.79 render. The user reported this on the first Corsa F build. `[USER-DIRECTION:2026-11-15]`

**Mechanism**: the hull's nose cap is a flat face at `y = -L/2`. The grille, both headlamps,
the bumper and the number plate were all built with their front faces at exactly `y = -L/2`
as well. Several surfaces therefore occupied the same plane and the renderer chose between
them per pixel. The two bumper boxes also met at one `z` plane.

**Fix** — every appliqué overlaps the body, never merely touches it:

| Part | Front face | Back face |
| --- | --- | --- |
| Headlamp / taillamp | 6 mm proud of the body cap | inside the body |
| Grille | 8 mm proud | inside the body |
| Bumper | 12 mm proud | inside the body |
| Number plate | 10 mm beyond the bumper face | inside the bumper |

Bumper upper and lower boxes overlap in Z by about 2 cm, and the lower lip is 1.5% narrower,
so no horizontal faces are coplanar. The rule is: a detail's back face must be *inside* the
host mesh and its visible face must be *outside* it by at least 6 mm. `[EXECUTION-VERIFIED:2026-11-15]`

## Headlamps outside the local body envelope

**Symptom**: headlamps stand above the bonnet or project beyond the nose corners like wings.
The user reported this on the first Corsa F build. `[USER-DIRECTION:2026-11-15]`

**Mechanism**: lamp positions were derived from overall width and from `nose_z` as if the
nose were a vertical wall of full width. The hull tapers in plan towards the nose and its
deck slopes; a lamp centred at `W/2 * 0.67` and `nose_z + lamp_h/2 + 0.02` therefore sat
partly above and outboard of the body.

**Fix**: size and place lamps from the local envelope:

- `hw_local = W/2 * taper(y_lamp)`;
- `lamp_outer = hw_local * 0.96`;
- `lamp_w = min(spec_lamp_w, 2 * lamp_outer * 0.47)`;
- lamp top at `nose_z - 0.01`, centre at `top - lamp_h/2`.

Taillamps use the local taper at `y = L/2 - tail_d/2` and their top at
`belt_rear - 0.01`. After building, print each lamp bbox and require it to lie inside the
hull bbox in X and below the deck in Z. `[EXECUTION-VERIFIED:2026-11-15]`

## Wheels: lower-body taper, arches, and tangency

**Symptom**: wheels either sit outside the body like bolt-on parts, or a jagged intersection
line runs along the top of the tyre where it meets the body.

**Mechanism**: the hull cross-section originally tapered sharply inwards below its widest
point (`lower half-width = 0.80 × max`), with the widest point at 55% of the body height.
The wheels were then far outside the lower body. Bringing them back in until they were
nearly coincident with the body surface produced a tangent intersection, which renders as a
jagged line.

**Fix**:

- Lower body nearly full width: `lower half-width = 0.97 × max half-width`.
- Widest point low: `z_low = z0 + 0.22 × (z1 - z0)`, not mid-height.
- Wheel outer face at `W/2 - 0.045`, i.e. inside the body's widest point and inside the
  arch lip.
- Arch rise `0.10 m` (not 0.15–0.17 m). A larger arch leaves the tyre silhouette separated
  from the body by a transparent row at 128 px render scale.
- Never place a tyre face within about 5 mm of the body side: that is a tangent, not an
  overlap.

`[EXECUTION-VERIFIED:2026-11-15]`

## The connected-cluster render gate is unreliable

The recorded A4 run claims "8/8 views are a single connected non-transparent pixel cluster".
Re-analysing the same accepted `ai/temp/audi-a4-b6-views/*.png` files on 2026-11-15 gives:

| View | E | N | NE | NW | S | SE | SW | W |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A4 clusters | 1 | 1 | 1 | 3 | 1 | 2 | 1 | 1 |
| Corsa F clusters | 1 | 1 | 2 | 3 | 1 | 3 | 3 | 1 |

The Corsa F render therefore matches the accepted A4's pattern almost exactly. At pak scale,
in the straight rear/front views (NW and SE in this render rig) the
lower body, bumper and wheel silhouettes separate by one anti-aliased row. That is a
sampling artefact, not detached geometry. `[EXECUTION-VERIFIED:2026-11-15]`

Use the cluster count as a **diagnostic against a known-good baseline**, never as a pass/fail
gate of "1 cluster per view". The reliable structural checks remain the per-object world
  bbox overlap against the complete shell, local surface checks and visual inspection of the render. A genuine detached part
shows as a whole object missing from the body silhouette (for example a lamp floating ahead
of the nose), which the bbox check also catches. `[EXECUTION-VERIFIED:2026-11-15]`

The earlier A4 claim in [photo-to-pak-pipeline](photo-to-pak-pipeline.md) has been
corrected in that doc: its NW and SE views were not single clusters.

## Pre-build checklist

1. Build all appliqués 6–12 mm proud of the host face; back faces inside.
2. Compute lamp size and position from the local taper, not from overall W.
3. Hull lower half-width 0.97 × max; widest point low; arch rise 0.10 m.
4. Wheel outer face at W/2 − 0.045.
5. Check every part against its supporting surface; use the complete-shell bounding box
   only as a gross-error check. Verify closed wheels and matching glazing boundaries.
6. Capture the reference angles and additional views, then obtain user acceptance at
   sprite scale. Cluster counts are diagnostic, not an acceptance condition.

## Open questions

- Should the render camera elevation be lowered so body sides occupy more pixels?
  That is a pakset-wide change and needs its own review.
- Is an object-index render pass a better automated check than alpha-cluster counting?
- Do the same rules hold for vans, lorries and buses, whose wheel/body relationships differ?
