---
status: draft
verified: none
---
# Private cars (`citycar`)

**Covers**: `Obj=citycar` objects in `New/citycars/` — the private cars that appear on
Simutrans-Extended city roads. Parent: [object-types](../object-types.md). Pipeline:
[photo-to-pak-pipeline](../graphics/photo-to-pak-pipeline.md). Child docs: the wealth-class
calibration ([citycar-wealth-classes](citycar-wealth-classes.md)), the current coverage audit
and remaining gaps ([citycar-asset-gaps](citycar-asset-gaps.md)), the parc-anchor research
([citycar-parc-anchors](citycar-parc-anchors.md)), and the batch production method for adding
them ([car-batch-production](../graphics/car-batch-production.md)).

Status: draft, created 2026-11-15 to record the conventions for private citycars, which
differ fundamentally from player vehicles.

## What makes private cars different

Private cars are not owned by the player. They exist only as visual traffic, and their
game mechanics are governed by different design rules:

1. **Introduction and retirement dates are based on when the car would be seen regularly
   on the roads**, not on when the model entered or left production. A car model built
   2000–2004 may remain in use for 10–25 years; conversely a rare variant is seen seldom
   for its whole life. Production dates are therefore a weak guide for citycar dates —
   use them only as a floor and ceiling, then stagger by what the roads actually saw.
2. **Introduction and retirement are staggered per colour**, because colour popularity
   differs by year of first registration. A red and a silver variant of the same model
   need not appear or disappear together.
3. **Frequency (`DistributionWeight`) tracks actual popularity**, measured against the
   number of that model on the road, compared with existing citycars of the same era.
   A niche 1970s executive saloon should weigh less than a 1998 Ford Focus; an
   upper-medium executive car should sit between the two. For private cars the weight is
   **only ever relative** to other cars at a given time; absolute car frequency is
   determined elsewhere. `[USER-DIRECTION:2026-11-15]`

`[USER-DIRECTION:2026-11-15]`

## Colour rule

Two rules govern the colour set and its weights. `[USER-DIRECTION:2026-11-15]`

1. **Use colours the real car was offered in.** Draw the palette from the manufacturer's
   UK colour range for that generation and era, not from generic red/blue/silver. Use the
   marketing paint name where it is known (Flame Red, Star Silver, Mineral Black) and an
   approximate render shade; exact paint codes are not required, but the hue must be
   recognisable and must not stand in for a different colour.
2. **Relative weights follow colour popularity.** Within one model's colour objects, the
   `DistributionWeight` values must be proportional to the measured popularity of those
   colours on UK roads during the model's years. Do not give every colour the same
   weight. The sum of the model's colour weights remains the model's overall weight tier;
   only the split between colours is set by the colour shares.

A model need not reproduce the full factory palette. It should model the few colours that
were actually common; a colour that was offered but rare may be omitted. Every modelled
colour must still be one the real car was sold in.

Method:

1. Identify the colours offered and sold in the UK for the generation, with paint names.
2. Read DVSA first-registration colour shares for the model's years (table at
   <https://www.ukmotoring.co.uk/statistics/car-colours/>). For pre-1994 models, use the
   nearest measured years as the base and state any adjustment made for the earlier era.
3. Set integer weights in the same ratio, then scale the set to the model's total weight
   tier (see [DistributionWeight method](#distributionweight-method)).
4. Record the paint names, the share years and the total weight in the `.dat` comments.

### Corsa family compliance (2026-11-15)

| Model | Colours and weights | Measured shares used | Note |
| --- | --- | --- | --- |
| Nova | Blue 15, Red 14, White 9, Black 8 | 1994–96: blue 23–25%, red 19–23%, white 7–10%, black 8–10% | White and red weighted up for the 1980s; measured base is late survivors |
| Corsa B | Blue 16, Silver 13, Red 12, Green 9 | 1993–2000: blue 23–25%, silver 9–25% rising, red 15–23% | Green is in the 20–25% "other" group, the 1990s green share |
| Corsa C | Silver 24, Blue 19, Black 10, Red 7 | 2000–06: silver 29–34%, blue 23–25%, black 9–20%, red 7–13% | Four largest measured colours |
| Corsa D | Silver 17, Black 15, Blue 14, Grey 9 | 2006–14: black 20–23%, silver 21–30%, blue 17–23%, grey 13–15% | Four largest measured colours |
| Corsa E | White 13, Black 13, Grey 12, Blue 10 | 2015–19: white 18–22%, black 19–20%, grey 16–23%, blue 15–17% | Red (10–13%) is next, omitted |
| Corsa F | Grey 13, Black 11, White 9, Blue 9 | 2020–22: grey 25–26%, black 19.6–20.1%, white 16.9–17.7%, blue 16.9–17.7% | Red (9%) is next, omitted |

`[EXECUTION-VERIFIED:2026-11-15]`

## Fields (one `obj=citycar` per colour)

| Field | Meaning | Omit behaviour |
| --- | --- | --- |
| `obj` | `citycar` | — |
| `name` | Model name with colour suffix, e.g. `AudiA4B6(Red)` | — |
| `copyright` | Holder of the images (`JamesPetts` for this pakset) | — |
| `DistributionWeight` | Spawn frequency relative to other citycars | **unverified; do not omit** |
| `intro_year` / `intro_month` | Year/month the colour is first seen on roads | — |
| `retire_year` / `retire_month` | Year/month it is last seen regularly (early retires mean rare sights from that date). Models still in production in 2026 with no announced end have the fields commented out, not deleted | omitted → open-ended |
| `speed` | Top speed in **km/h** (the engine reads it with `kmh_to_speed`; the tree's values are a game-balance figure, not always the model's real top speed) | — |
| `length` | Vehicle length in carunits (16 to a tile), e.g. `2` for a family car; set from the model's real length at 1.875 m per carunit ([road-vehicle-lengths](road-vehicle-lengths.md)) | omitted → 4 (a quarter tile) |
| `maximum_comfortable_journey_minutes` | Maximum comfortable journey time for private-car travel, in whole minutes (the `_tenths` form gives tenths of a minute) | omitted/0 → engine default 180 minutes |
| `maximum_tolerable_journey_minutes` | Maximum tolerable journey time, same units (`_tenths` form available) | omitted/0 → three times the comfortable time |
| `class` | Comma-separated passenger wealth class indices the car is available to (0 = Very low … 4 = Very high in this pakset), e.g. `class=1,2` | omitted → available to **all** classes; an empty `class=` is a fatal makeobj error |

Comfort fields are time-based (ex-15; the old 0–255 comfort rating is deprecated): specifying
both the `_minutes` and `_tenths` form of one quantity is a fatal makeobj error. Values are
stored in tenths of minutes. `class` indices must exist in the pakset (five passenger wealth
classes); the engine keeps per-class car pools and validates indices at load.
`[CODE simutrans-extended ex-15 @ 8517e6c9f]`

### Retirement policy (2026-11-20)

1. **A model still in production in 2026 with no announced end of production has no retire
   date.** Comment out `retire_year` and `retire_month`; do not delete them. The engine treats
   the model as open-ended. Revisit when an end is announced.
2. **A model that is out of production has a road-presence retirement date**, not its production
   end. The date is an estimate of when that colour stops being a regular sight, normally
   15–22 years after the colour's introduction, and is staggered across colourways. A future
   date is normal for a recently withdrawn model. Two documented exceptions: the Mondeo Mk4
   dates follow the Mk5 stand-in to 2022 (2030–34), and the Range Rover dates follow the
   classic's 1996 production end rather than the 1970 introduction (1998–2005).
3. **A model with an announced end of production** is treated as out of production from that
   date and gets the same road-tail treatment.
4. The policy note is written at the top of each affected `.dat` file as
   `# Retire policy 2026-11-20: ...`, and the body header's date sentence is kept in step.

The 2026-11-20 pass applied this to 47 models: 36 current-production models had their retire
fields commented out, and 11 out-of-production or open-ended models had road-tail dates set or
corrected, including the Ford Ka, Ford Focus, New Mini, Qashqai J10, Mondeo Mk4, Galaxy Mk3 and
Range Rover. The other citycar files changed on the same date only for the comfort
recalibration. The Hyundai i10 Mk3 is treated as current in 2026: its header originally read
2020–2026 and was changed to 2020–present. Confirm that when Hyundai announces the model's end.

Other conventions shared by all `citycar` objects:

- Source folder: `New/citycars/`; images under `New/citycars/images/`; compile target
  `PAK128` (`DIRS128`/`TR_DIRS` in `New/Makefile`).
- Image names: `<model-slug>-<colour>_<VIEW>.png` (e.g. `audi-a4-b6-silver_E.png`).
- All views are supplied as separate files (8 views), compiled into one `.pak` per folder.
- The per-view image offset table used by every citycar in this pakset is
  `E: -33,14; SE: -13,0; S: 0,0; SW: -8,10; W: 4,5; NW: 12,10; N: 0,33; NE: 0,24`.
- `length` is set on every object (2026-11-23 pass). Most cars are `3`, small cars and the
  Mini class `2`, large saloons and estates `3`–`4`, and the horse-drawn carriages `4`–`5`
  because their sprites include the horse. The value is measured from the `E`-view sprite's
  extent along the 2:1 axis, not from the real vehicle length. Method, calibration and the
  road-vehicle counterpart: [road-vehicle-lengths](road-vehicle-lengths.md).

## DistributionWeight method

`[USER-DIRECTION:2026-11-15]` The most popular car on the road at a given time is the anchor:
`DistributionWeight = 100` assuming 5 colourways. A model with fewer colourways scales
inversely (single colourway, e.g. `FordT(Black)`, → 500). Every other car is weighted relative
to that era's anchor. The historical anchors (most numerous model in use on GB roads at
5-year points 1920–2025), their evidence, and the pakset coverage check are recorded in
[citycar-parc-anchors](citycar-parc-anchors.md) — read it when rebasing weights or checking
popularity evidence.

1. Find the vehicle's popularity in its era relative to the era's anchor
   ([citycar-parc-anchors](citycar-parc-anchors.md); where no research exists, compare like
   with like: Focus/Ka/Herald/SD1 tier).
2. Colour shares below are DVSA first-registration data (cars tested in 2025, counted once),
   from the UK Motoring analysis: <https://www.ukmotoring.co.uk/statistics/car-colours/>.
   For a 2000–2005 D-segment saloon, the six common colours carried roughly:

   | Colour | 2000 | 2001 | 2002 | 2003 | 2004 | 2005 |
   | --- | --- | --- | --- | --- | --- | --- |
   | Silver | 28.9% | 30.5% | 32.6% | 34.5% | 34.5% | 33.6% |
   | Blue | 24.5% | 24.3% | 24.6% | 24.2% | 23.5% | 23.7% |
   | Red | 13.3% | 10.8% | 9.5% | 8.1% | 7.0% | 6.7% |
   | Black | 9.3% | 10.3% | 11.7% | 13.3% | 15.1% | 18.0% |
   | Grey | 2.9% | 4.9% | 6.5% | 7.7% | 10.2% | 11.9% |
   | White | 2.1% | 1.6% | 1.2% | 0.9% | 0.7% | 0.6% |

   UK first-registration volumes: Audi A4 ≈ 20,700 (2001), 30,800 (2002), 33,900 (2003),
   31,700 (2004) — roughly a sixth to a tenth of the Ford Focus's annual UK volume.
   `[WEBSITE:https://www.howrareismycar.co.uk/audi/a4/how-many-audi-a4-were-made.aspx]`

3. Scale the colour shares to the model's era weight (step 1) and set integer weights. The
   A4 B6 was set at Silver 16, Blue 13, Black 11, Red 10, Grey 7, White 3.

Weights currently in the tree that were set before the 2026-11-15 anchor rebase (for example
the Ford Focus at 12–20 per colour and the A4 B6 weights above) use an earlier tiering
convention and are to be rebased against the anchors.
`[USER-DIRECTION:2026-11-15]`

`[EXECUTION-VERIFIED:2026-11-15, compile-checked through PAK128 into a scratch .pak]`

## The A4 B6 example (in tree)

`New/citycars/audi-a4-b6.dat` (six objects, introduced/retired in staggered order). The
weights shown are pre-rebase values (see above):

| Colour | Weight | Intro | Retire | Rationale |
| --- | --- | --- | --- | --- |
| Silver | 16 | 2000-11 | 2027-12 | Dominant colour of the era; longest visible tail |
| Blue | 13 | 2001-04 | 2024-12 | ~24% share all years; steady mid-tail |
| Black | 11 | 2002-02 | 2026-12 | Rising through 2005; long tail |
| Red | 10 | 2000-11 | 2022-06 | 13.3%→6.7% and falling; retires early |
| Grey | 7 | 2003-04 | 2029-12 | 3%→12% rocket; appears later, longest tail |
| White | 3 | 2002-07 | 2020-12 | Rare (~1%); early out |

## The Corsa family example (in tree)

Six generations, four colours each, 24 objects, in `vauxhall-nova.dat` and
`vauxhall-corsa-{b,c,d,e,f}.dat`. The first generation is named `VauxhallNova`, because
that was its UK name; the Corsa name was adopted only with the B in April 1993.

| Model | Objects | Total weight | UK intro | Replaced in UK | Notes |
| --- | --- | --- | --- | --- | --- |
| VauxhallNova (Corsa A) | 4 | 46 | 1983-04 | 1993-03 | Boxy 3/5-door; black bumpers; 3.62 m |
| VauxhallCorsaB | 4 | 50 | 1993-04 | 2000-09 | Rounded; black bumpers; 3.73 m |
| VauxhallCorsaC | 4 | 60 | 2000-10 | 2006-09 | 3.82 m; second best-selling UK car 2002–04 |
| VauxhallCorsaD | 4 | 55 | 2006-10 | 2014-12 | 4.00 m; body-colour bumpers; top-three seller |
| VauxhallCorsaE | 4 | 48 | 2015-01 | 2019-12 | 4.02 m; Summit White, Mineral Black, Asteroid Grey, Darkmoon Blue |
| VauxhallCorsaF | 4 | 42 | 2020-01 | present (2026) | 4.06 m; Quartz Grey, Diamond Black, Arctic White, Voltaic Blue |

Model dimensions are the Wikipedia dimension boxes (Corsa A 3.622 × 1.540 × 1.365 m;
B 3.729 × 1.610 × 1.440; C 3.817 × 1.645 × 1.440; D 3.999 × 1.737 × 1.488;
E 4.021 × 1.746 × 1.480; F 4.060 × 1.765 × 1.435). UK registration figures are from
bestsellingcarsblog/AROnline (1993–2000), the UK top-20 tables (2000–04) and
howrareismycar/DVLA (2006–25); colour shares are the DVSA first-registration table at
<https://www.ukmotoring.co.uk/statistics/car-colours/>. The pre-1994 shares are not in
that table; the Nova weights start from the 1994–96 survivor shares and shift towards red
and white, which were more common on 1980s registrations.
`[LITERATURE:https://en.wikipedia.org/wiki/Opel_Corsa]`
`[LITERATURE:https://www.ukmotoring.co.uk/statistics/car-colours/]`

Colour weights are set in the Escort/Focus tier: total model weight is roughly half to
two-thirds of the equivalent Ford, matching the UK sales ratio (Corsa 84–108k against
Focus 110–151k at the C/D peak; Nova ~70k against Escort ~130k). Retire dates give a
15–18 year road tail from UK launch, staggered per colour.

Colour selection and the relative split follow the colour rule above: each generation's
four colours are actual UK Vauxhall offerings, and the weights preserve the measured order
and approximate ratios. The `.dat` comments record the paint names and share years.

The Corsa F was still on sale in November 2026; its retire dates (2032–2039) are
estimates. A Corsa G is expected in 2028 on the STLA One platform and is not modelled.

Images follow the same `<slug>-<colour>_<VIEW>.png` convention under
`New/citycars/images/`. The six models were built with the parametric
`car_builder.py` in the blends repository (see [ai-pipeline](../graphics/ai-pipeline.md))
and compiled with `Makeobj-Extended-ex-15.exe`; the debug engine loaded the resulting
`citycars.pak` and reported `MAP-GEN: PASS` on 2026-11-15. `[EXECUTION-VERIFIED:2026-11-15]`

## The BMC1100 example (in tree)

`New/citycars/bmc1100.dat` (5 colourways, 2026-11-15): one model for the ADO16 (the car sold
as the Austin and Morris 1100/1300), whose shell did not change enough across Mk I–III to
read at pak scale. Period BMC paint names and codes from the 1966 and 1970 Austin-Morris
colour charts; the pre-1994 colour shares are era-adjusted from the 1994–96 measured base,
with the adjustment stated in the `.dat` header (the same method as the VauxhallNova's
1980s adjustment). Comfort 70/435 reflects the Hydrolastic suspension. The slim chrome
bumper was applied as a post-build edit in the 4.5 session (bumper bars scaled down and the
material set to chrome) without changing `car_builder.py`'s builder code.

## The BSA M21 outfit example (in tree)

`New/citycars/bsa-m21-combo.dat` (2026-11-15): the first non-car citycar, a BSA M21 600 cc
motorcycle with a Watsonian Maxstoke sidecar. Three colourways — Black 140, Maroon 60, BSA
Light Green 40 — total 240 against the Morris Minor anchor's 500, classes 0–1, 72 km/h,
comfort 25/338, road presence 1946-66 staggered by colour. Sources and reasoning are in the
`.dat` header.

Conventions it establishes:

- **The motorcycle sits at the tile centre, not the bounding box.** An outfit is asymmetric:
  the Stage B rig centres the combined bounding box, so a further +0.339 pak-unit lateral
  shift is applied after preparation and before rendering. Without it the outfit rides about
  3 px left of a car.
- **Two-cluster vehicles** pass `-` as the hull argument to `stageB_car_prepare.py`, which
  substitutes a connectivity check for the single-hull test
  ([ai-pipeline](../graphics/ai-pipeline.md)).
- **Render one colour per process** for a multi-object vehicle. A three-colour run stopped
  after 20 of 24 images; single-colour runs completed and exited 0.
- **The sidecar shape and the motorcycle shape can come from different references.** Here the
  chair came from the Watsonian brochure and the bike from photographs of a real outfit whose
  chair was a different model; the brief must say which reference governs which part.

The 1923 BSA 557 outfit (`bsa-557-combo.dat`, Green and Black) followed on 2026-11-15 as a
deliberately lean build: nine objects, medium model effort, one side comparison and a
four-view check. It was accepted under the size-based leniency rule
([visual-asset-controls](../graphics/visual-asset-controls.md#strictness-scales-with-the-objects-size)):
at a 9 x 6 px sprite only the outline is judged.

## Comfort calibration

The method is canonical in [comfort-calibration](../comfort-calibration.md): the Mini (40/390)
and Sierra (120/510) anchors, the line `tolerable ≈ 330 + 1.5 × comfortable` capped at 600, and
the rule that the Mini is a low-end anchor rather than a floor. The private-car method, the
outfit penalty and the separate horse-drawn line are in
[private cars](../comfort/private-cars.md); the per-model values and their notes are in the
[register](../comfort/comfort-table.md#private-cars). Every colourway of a model shares the
model's values.

## The Fiesta family example (in tree)

A second family run (2026-11-15): `FordFiestaMk1`–`Mk7` in `New/citycars/ford-fiesta-mk{1..7}.dat`,
7 generations, 4 colours each, 28 objects. Same method as the Corsa family; per-generation
dimensions, paint names, share years and sources are recorded in the `.dat` header comments.
Colourway weights total 500 per generation (the anchor convention), provisional pending the
central rebase. Built with `car_builder.py` and the Stage B car scripts.

## Bulk gap-fill lessons (2026-11-23)

The 36-model gap-fill programme produced four rules worth carrying into the next batch.

1. **The photograph governs body style, not the brief.** Three cars had a plausible generic
   description that the surviving car contradicted: the Rover 6 is open and windscreen-free, the
   Napier 8 (AP 3575) is a double phaeton rather than a two-seater, and the Jaguar 1½ Litre is
   the later body without the exposed wing-mounted spare. In each case the builder stopped at the
   reference check and the model followed the photographs, with the other body recorded as not
   represented. Builders must keep stopping for this.
2. **A claimed "true side elevation" must be verified by the builder.** Three packs classified as
   true side (E-type S2, E-type S3, XJS) were oblique when the builder opened them. The comparison
   camera is matched to the actual angle and the limitation goes into the `.dat`.
3. **Stage B attachment needs the right hull or the connectivity mode.** The Type 01 roof and
   camera attached to the cabin rather than the hull; grouping the painted cabin and roof into
   `Hull` fixed it. Surface details that sit proud of the body (Mark V plates, overriders,
   hubcaps, spat latches) and chassis-based brass cars pass with `-` connectivity, not the
   hull-only check.
4. **Derivatives may correct a weak parent, but must not alter it.** The 240 and 340 were built
   from corrected derivative shells because the existing Mark 2 master was too squared; the Mark 2
   asset itself stayed byte-identical and is flagged for a later graphics replacement.

## Open questions

- Whether the same staggered-colour rule applies to player-help vehicle fleets.
- Exact engine internals of citycar generation and weighting (not recorded; see
  [object-types](../object-types.md)).
- Whether the per-view offset table should be adjusted per-size or stay global.
