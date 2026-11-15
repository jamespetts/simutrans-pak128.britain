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
   upper-medium executive car should sit between the two.

`[USER-DIRECTION:2026-11-15]`

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

1. Find the vehicle's UK market weight in its era — compare like with like: Focus/Ka/
   Herald/SD1 tier. The Ford Focus is deliberately over-weighted (12–20 per colour) as the
   most common car of its era; the Ka sits at 3–10; the Herald 5–11.
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

3. Scale the colour shares to the tier step below the Focus and set integer weights. The
   A4 B6 was set at Silver 16, Blue 13, Black 11, Red 10, Grey 7, White 3.

`[EXECUTION-VERIFIED:2026-11-15, compile-checked through PAK128 into a scratch .pak]`

## The A4 B6 example (in tree)

`New/citycars/audi-a4-b6.dat` (six objects, introduced/retired in staggered order):

| Colour | Weight | Intro | Retire | Rationale |
| --- | --- | --- | --- | --- |
| Silver | 16 | 2000-11 | 2027-12 | Dominant colour of the era; longest visible tail |
| Blue | 13 | 2001-04 | 2024-12 | ~24% share all years; steady mid-tail |
| Black | 11 | 2002-02 | 2026-12 | Rising through 2005; long tail |
| Red | 10 | 2000-11 | 2022-06 | 13.3%→6.7% and falling; retires early |
| Grey | 7 | 2003-04 | 2029-12 | 3%→12% rocket; appears later, longest tail |
| White | 3 | 2002-07 | 2020-12 | Rare (~1%); early out |

## Open questions

- Whether the same staggered-colour rule applies to player-help vehicle fleets.
- Exact engine internals of citycar generation and weighting (not recorded; see
  [object-types](../object-types.md)).
- Whether the per-view offset table should be adjusted per-size or stay global.
