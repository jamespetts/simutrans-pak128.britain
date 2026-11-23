---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Guards and driver-only operation on multiple units

**Covers**: the `staff[2]` guard declaration on rail multiple units under `New/trains/`,
`New/narrowgauge/` and `New/london-underground/`, and the classes that run without a guard.

Parent doc: [crew-complements](crew-complements.md).

## The rule

A guard is declared, `staff[2]=1`, on one car of each unit, unless the class is one of those that
runs under driver-only operation. One car per unit means a two-unit formation pays two guards,
which is correct: each unit keeps its own guard.

A class runs without a guard when it is in the driver-only list below. Otherwise:

- diesel multiple units always keep a guard;
- electric multiple units introduced before 1983 keep a guard;
- electric multiple units introduced in 1983 or later run without one unless they are in the guard
  list.

The year 1983 is the introduction of the Class 317 on the St Pancras to Bedford line, the first
British unit built for driver-only operation. `[LITERATURE:https://abcommuters.com/wp-content/uploads/2016/11/rssb-report-on-doo.pdf]`
In 2007, 28 per cent of passenger journeys were dispatched by driver only, so both regimes persist
to the present and the pakset has to choose per class.
`[LITERATURE:https://www.orr.gov.uk/sites/default/files/om/gtr-southern-driver-only-operation-report-january-2017.pdf]`

## Driver-only classes

Electric multiple units declared without a guard. Every other electric multiple unit introduced in
1983 or later is also driver-only, by the year rule; these are the ones named in the class list:

| Classes |
|---|
| 317, 319, 320, 321, 322, 323, 325, 332, 333, 334, 345, 350, 357, 360, 365, 373, 374, 375, 376, 377, 378, 379, 380, 385, 387, 390, 395, 397 |
| 700, 701, 707, 710, 717, 720, 730, 745, 755, 769, 800, 801, 802 |
| London Underground 1983, 1992, 1995 and 2009 tube stock, and the S Stock |

Electric multiple units that keep a guard after 1983, because they were operated with one:

| Classes |
|---|
| 442, 444, 450, 456, 458, 465, 466, 483 |

Diesel multiple units keep a guard whatever their date. That covers the Sprinter and Pacer
families (141, 142, 144, 150, 153, 156, 158, 159), the Network Turbos and their successors (165,
166, 168, 170, 171, 172, 175, 180, 185), the Voyager and Meridian families (220, 221, 222), and
the 195, 196 and 230.

Railcars and single-unit stock follow the same rule: a railcar that enters service before 1983
carries a guard, a later one does not.

## Where the guard sits

The guard is declared on the car whose code contains "B" (DMBS, DMSB, BSO, BSK, TSOB) where the
class has one, otherwise on the rear driving car. `[USER-DIRECTION:2026-11-23]` This choice does
not change the amount charged, because the engine sums other staff over the whole convoy
regardless of order; it determines which car shows the staff in the vehicle list.

## London Underground

Underground stock carried guards until one-person operation, agreed with the unions from 1984 on
the Hammersmith and City line and requiring new trains on the Central and Northern lines in the
1990s. `[LITERATURE:https://en.wikipedia.org/wiki/British_electric_multiple_units]` The pakset
therefore declares a guard on tube stock up to the 1973 stock and none from the 1983 stock onward.

## DLR

Docklands Light Railway cars carry a train captain and no driver: `staff[6]=1` on one car of each
unit, charged at the conductor rate. `[USER-DIRECTION:2026-11-23]`

## Known approximations

- The guard is a class property in the pakset but a route and operator property in reality. The
  Class 465, for example, worked both with and without a guard.
- A unit that keeps a guard pays one guard per unit even when two units run together and one guard
  works the train. The engine cannot share other staff across coupled units; see
  [multiple-working](multiple-working.md).
