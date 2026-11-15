---
status: draft
verified: none
---
# Private cars (`citycar`)

**Covers**: `Obj=citycar` objects in `New/citycars/` — the private cars that appear on
Simutrans-Extended city roads. Parent: [object-types](../object-types.md). Pipeline:
[photo-to-pak-pipeline](../graphics/photo-to-pak-pipeline.md).

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
| `retire_year` / `retire_month` | Year/month it is last seen regularly (early retires mean rare sights from that date) | — |
| `speed` | Top speed in mph (existing values 110–149) | — |

Other conventions shared by all `citycar` objects:

- Source folder: `New/citycars/`; images under `New/citycars/images/`; compile target
  `PAK128` (`DIRS128`/`TR_DIRS` in `New/Makefile`).
- Image names: `<model-slug>-<colour>_<VIEW>.png` (e.g. `audi-a4-b6-silver_E.png`).
- All views are supplied as separate files (8 views), compiled into one `.pak` per folder.
- The per-view image offset table used by every citycar in this pakset is
  `E: -33,14; SE: -13,0; S: 0,0; SW: -8,10; W: 4,5; NW: 12,10; N: 0,33; NE: 0,24`.

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

## Open questions

- Whether the same staggered-colour rule applies to player-help vehicle fleets.
- Exact engine internals of citycar generation and weighting (not recorded; see
  [object-types](../object-types.md)).
- Whether the per-view offset table should be adjusted per-size or stay global.
