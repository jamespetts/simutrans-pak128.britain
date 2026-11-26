# Cost-balancing workbooks: handoff

**Status**: analysis complete; passes 62-71 applied in the working tree; `.dat` costs deliberately
NOT changed. The workbooks carry the current treatments and are ready for the user's review. The
independent sanity check of 2026-11-25/26 (`sanity-check-2026-11-25.md`) found them fit for review
and not yet fit for the `.dat` pass: 19 suggested `.dat` values exceed the engine's signed 32-bit
cost field and 8 way rows have a negative way-only cost, both of which need a decision before that
pass. Its documentation and workbook defects are fixed by pass 71.

## What this is

Two workbooks, `New/cost-balancing-capital.xlsx` and `New/cost-balancing-maintenance.xlsx`, compare
every `.dat` price in the pakset with a target derived from **measured historical evidence**. The
target column must never take a `.dat` price as an input: that is the quantity under audit, and
using it to build the target is circular.

Coverage: **4,071 of 4,218 objects have a capital target (97%); 4,154 have a maintenance target
(98%)**. Both workbooks rebuild with zero error cells. Before commissioning a research pass, read
[negative-findings](negative-findings.md): it records the searches that found nothing and the
archive routes that remain.

## How it is built

| File | Role |
|---|---|
| `evidence_data.py` | vehicle ladders, the mean annual distance table, `tram_overhaul()`, feature multipliers, the `extrapolation()` entry point, the qualitative adjustment layer |
| `measured_infra.py` | infrastructure capital and maintenance from measured rates; writes `measured-infrastructure.csv` |
| `build_workbooks.py` | reads the inventory, research CSVs and the two files above; writes both workbooks |
| `vehicle-adjustments.csv` | 81 sourced qualitative adjustments (capital and maintenance factors) |
| `infrastructure-features.csv` | 655 infrastructure objects x 43 attributes, from `.dat` fields and comments |
| `vehicle-features-*.csv` | locomotive, multiple-unit and general vehicle attributes |
| `measured-infrastructure.csv` | per-object measured targets and their basis strings |
| `water-capacity.csv` | hull + hold capacity for the 216 water objects |
| `research-pricing-rows-*.csv` | the evidence register, one row per measured price, with source |
| `research-pricing-report-*.md` | the findings behind each pass |
| [vehicle-cost/mean-annual-distance](../vehicle-cost/mean-annual-distance.md) | the class and era mean annual distance table, its evidence and the rows it applies to |

Rebuild: `C:\WINDOWS\py.exe -3 New\ai\cost-balancing\build_workbooks.py`, then recalculate with
LibreOffice (`--headless --convert-to xlsx`) and copy the recalculated files over `New/*.xlsx`,
which stores cached values so the workbooks open with numbers rather than formulas. **A rebuild
discards the pass 40-61 notes**: the patch tools below write into the existing workbook, and are
the only supported route for changes after a build. `evidence_data.BASE` was pointing one
directory short until 2026-11-25, so the generator read no `.dat` files at all; it resolves
the workspace root, and a rebuild reproduces the pass-43 values. The overhaul columns of a
rebuild follow passes 46-47 (`CARRIAGE_OVERHAUL` and `WAGON_OVERHAUL` in `evidence_data.py`),
but the maintenance split of columns 27-30 still comes from the patch scripts: the generator
carries no mean-annual-distance ladder, which is the open question "how is the mean annual
distance per class to be fixed". Do not treat a rebuild as reproducing the current workbooks.

## Current treatments

The workbooks apply the treatments below. **A** is the measured annual maintenance figure for the
class; money is 1900 GBP. The pass-by-pass history and the rejected treatments are in
[pass-history](pass-history.md); this section states only the current position.

| Class | Annual level (1900 money) | Overhaul and upgrade | Fixed/per-km | Mean annual distance |
|---|---|---|---|---|
| Rail carriages | 33 / 39 / 121 / 265 / 460 / 440 GBP a vehicle-year at 1900 / 1920 / 1950 / 1970 / 1990 / 2020, log-linear between and flat outside; 1948 and 1966 read 112 and 226 by interpolation | Provision 28 / 24 / 19 / 12 / 10 / 8 per cent of A at 6 / 5 / 3 / 2 / 2 / 2.6 years; first event 0.70 of the maximum over three; upgrade 35 per cent on 682 rows, 32.5 per cent on 56, and 5.3-6.6 per cent on the 20 brake pairs, as the sheet holds them | 70/30 | 35,000 / 36,000 / 55,000 / 88,000 / 120,000 / 113,000 km by era |
| Rail wagons | 4.2 / 8.7 / 14.3 / 24.8 / 23.8 GBP per 10-tonne wagon-year at 1900 / 1950 / 1970 / 1990 / 2020, scaled by (payload/10)^0.4 | Head 0.8A; event 1.2A every six years, first event 0.75 of the steady event; upgrade 10-20 per cent for brake pairs | 65/35 | 40,000 km |
| Rail locomotives | 215 / 306 / 800 / 2,100 / 1,045 / 520 GBP an engine-year at 1900 / 1950 / 1961 / 1977 / 1995 / 2020, log-linear between; the Class 92 is a mixed-traffic class override at 868 (2018, Caledonian Sleeper duty), the Class 88 takes the Class 68 level of 614.82, and Classes 89, 90 and 91 take the measured electric-locomotive track of 1,476 / 1,103 / 1,045 / 868 at 1950 / 1977 / 1995 / 2018; none is a time rung of the diesel ladder | Renewals 25 per cent at 1900 phasing to zero by 1950; 22 per cent at 1961, phased in from 1950 and out by 1977; provision 35 per cent steam and 39 per cent diesel/electric; events scaled to the provision | 65/35 steam, 60/40 diesel/electric | The row's measured duty where the class has one, else the class and era distance table |
| Narrow-gauge carriages | The standard-gauge carriage series (33 / 39 / 121 / 265 / 460 / 440), because no source distinguishes gauge in carriage maintenance; class factors (brake 0.5, mail 0.75) kept | As rail carriages, with the narrow gauge's own 40,000 km a year setting the interval | 70/30 | 40,000 km |
| Multiple units | 66 / 241 / 380 / 510 / 780 GBP a car-year at 1900 / 1950 / 1970 / 1990 / 2020, log-linear between | Provision 15 per cent of A; event 1.2A every eight years, first event 0.70 of the maximum over three; upgrade 8-12 per cent refresh, 20-25 per cent re-tractioning | 50/50 | 100,000 / 120,000 / 161,000 km by era; tube and metro 120,000 |
| Trams | Pre-1950 gross 84 / 131 / 106 / 89 GBP a car-year at 1900 / 1920 / 1931 / 1939; 1950-90 repairs-only 150 (band 130-210); 1990+ 1,177 | Pre-1950: renewals 35 per cent, provision 28 per cent at two years, event 0.35A rising to 0.75A. 1950-90: renewals 0, provision 28 per cent at three years, event 0.54A rising to 1.15A. 1990+: renewals 0, provision 6 per cent at twelve years, one event of 0.75A. Upgrade 0.22 of the new price to 1950, rising linearly to 0.50 by 1990 | 50/50 | 48,000 km to 1989; 90,000 km from 1990 |
| Buses and coaches | Measured Commercial Motor level, rescaled to the 37.5 per cent overhaul composition | 220,000 km, 25 to 40 per cent of capital, rescaled to the measured annual share | 75/25 | 55,000 km overhaul reference; 40,000 km split reference |
| Lorries and vans | Measured Commercial Motor level | Introduction-year bands: before 1930 35-50 per cent, 1930-59 44-56, 1960-84 25-35, 1985-2004 20-30; intervals 80,000 / 80,000 / 160,000 / 400,000 km; vans 80,000 / 160,000 km | 75/25 | 40,000 km split reference (25,000 for short-duty vans) |
| Ships | Capital is the per-gross-ton ladder: 84.1 × GT^0.90 passenger, GBP 35/GT cargo and coasters, GBP 17/GT inland craft, GBP 39/GT tugs; 177 of 216 rows carry a sourced tonnage (research pass 57), and 39 keep the capacity rule with the reason stated. Repair is 2 per cent of capital; see [source-composition](../vehicle-cost/source-composition.md) | Five-year special survey; 2 to 5 per cent of capital | 50-65 per cent standing | 115,000 km |
| Aircraft | BOAC engineering cost per flying hour; see [aircraft-maintenance](../vehicle-cost/aircraft-maintenance.md) | C-check every 4,000-6,000 flight hours; 2.5 to 5 per cent of capital; D-check in the cycle | Class rule | 4,200,000 km per C-check |
| Maglev | Shanghai imported-car acquisition at 1,088 GBP a seat (1,087.5 before rounding; report 55; the 507.6 Almujibah estimate remains the serial-production floor); maintenance 0.00010257 GBP a seat-km | 15 per cent of A, event 1.2A every eight years | 50/50 | 300,000 km |
| Holds and animals | Holds are containers inside a vehicle: 1 per cent of their own capital, no per-km charge. Animals are 45 GBP an animal-year (90 for a pair), standing only | Holds take no overhaul and a zero target; animals replace at 100 per cent of the purchase price at 70,000 km; upgrade 50 per cent | Holds all fixed; animals all fixed | Holds none; animals 10,000 km a year |
| Piers (infrastructure) | The 111 bridge-substructure pier rows take 19 per cent, the midpoint of the measured 13-25 per cent low-bridge substructure share, of their bridge family's measured rate: brick and stone 107,500 GBP a km, iron 164,000, concrete 410,317, steel 280,000, timber 48,000 | Capital only: no substructure maintenance rate is measured, so the maintenance sheet's pier rows stay blank | Not applicable (infrastructure) | Not applicable |

The current coherence audit reports 3,539 vehicles, 3,265 envelopes checked, 274 zero-priced
sections, 0 unchecked and 0 failures. The distance check reports 1,524 rows with a stated mean
and 0 deviations over 10 per cent.

**Feature premiums are applied, not outstanding.** The generator and the workbook basis notes
apply: road automatic transmission, air suspension, low floor, air conditioning and saloon
heating; carriage corridor, sleeping, steam/electric heating and air conditioning; tram
articulation. The earlier statement in this handoff that only road engine type and carriage
dining/bogie/steel were wired was wrong.

**User decisions, 2026-11-25** `[USER-DIRECTION:2026-11-25]`:

1. The `.dat` pass waits.
2. The generator must override every asset for which individual asset data exist. This is an
   invariant, not a preference.
3. Piers take the measured structure share.
4. The two knowledge-base corrections are closed: the road running-cost values were corrected on
   2026-11-23; the remaining timber wording is corrected now.
5. Class 89/91 are interpolated from the 1950s/1960s figures to the 1980s/1990s figures for
   intermediate locomotives. The user confirmed on 2026-11-25 that a class with its own measured
   figure takes that figure and a class without one sits on the interpolation line, so Class 90
   is included: none of the three has a measured figure, and all three take the electric track.
6. The narrow-gauge carriage rows are re-based on report 51.
7. **Water: use the per-gross-ton capital ladder.** The user decided on 2026-11-25 to price the
   water objects on the gross-tonnage ladder. Pass 70 applies it: the three measured per-gross-ton
   rates are the capital prices, repair stays at 2 per cent of the resulting capital, and the
   rows with no gross tonnage (hovercraft, holds and fishing craft) keep their current rules
   because no tonnage can exist or is recorded. Research pass 57 fills the blank tonnage rows.
   The analysis behind the decision is in "Water: the capital question" below.

## Passes 66-71 (2026-11-25 to 26)

- **Pass 66**: Classes 89, 90 and 91 leave the 0.5-of-the-diesel-ladder rule for the measured
  electric-locomotive track. A becomes 1,073.61, 1,070.39 and 1,067.18 in place of 740.69,
  712.52 and 685.42; the provision, head, fixed and per-km charges and event move with A under
  the existing diesel/electric rules.
- **Pass 67**: the 34 narrow-gauge carriage rows are re-based on report 51 exactly as pass 62 did
  for the standard gauge, with the class factors kept and the interval set at the band's years
  times the narrow gauge's own 40,000 km a year. Pass 48 had entered 210,000 km from the
  standard-gauge band reference, which is 5.25 years at 40,000 km and did not match the
  six-year interval the note stated.
- **Pass 68**: the 111 `Piers & docks` rows take 19 per cent of their bridge family's measured
  rate: brick and stone 107,500 GBP a km, iron 164,000, concrete 410,317, steel 280,000, timber
  48,000. Every row states the band, the family and the reason capital is charged and
  maintenance is not. The generator now carries the same rule, so a rebuild reproduces it.
- **Pass 69**: 71 locomotive rows whose mean annual distance was the inherited 109,000 km
  default, and 11 post-1948 steam rows at the 40,000 km default, move to the class and era
  distance table. The measured class duties stay (Class 37 81,000; Class 47 113,000; Class 55
  226,000; Class 86 176,000; Class 87 274,000; the CSLR tube locomotive 120,000). Only the
  per-km charge and the overhaul interval move.
- **Pass 70** (`wb_fv_pass70.py`): the water objects move to the per-gross-ton capital ladder
  after the 2026-11-25 decision. 177 of the 216 rows are re-based: 84.1 x GT^0.90 for passenger
  vessels, GBP 35/GT for cargo and coasters, GBP 17/GT for inland craft and GBP 39/GT for tugs,
  with repair at 2 per cent of capital and the overhaul event scaled by the same factor. The
  median capital movement is x2.55; the extremes are the small tugs (x0.13 to x0.31) and the
  large cargo hulls' low-value fits (a Handysize livestock fit moves x94, because every object is
  a separately purchased ship and carries its whole hull once). The 39 rows without a tonnage
  keep their capacity rule and say why: 9 hovercraft (no gross tonnage exists), 9 holds (the
  parent carries the hull), 2 towing horses and a towpath tractor (not vessels), and 18 hulls
  that research pass 57 could not identify.
- **Generator alignment for water**: `evidence_data.py` now carries `water_tonnage()`,
  `water_gt_price()` and the four rates, and the water branch uses them before the capacity
  ladder. A test rebuild reproduces all 216 water capital targets exactly.
- **Generator alignment (the general path repair)**: `build_workbooks.py` had the same
  one-directory path error that `evidence_data.BASE` had before 2026-11-25 and failed at its
  first file read, so no rebuild had been possible. The path is fixed; `evidence_data.py` now
  carries the locomotive ladder, the electric track, the Class 92 and Class 88 overrides, the
  measured class duties, the pier share and the class and era distance table for the carriage
  overhaul interval, and `build_workbooks.py` uses the table. A test rebuild reproduces the
  patched values for the electric locomotives, the Class 92, Classes 86, 87 and 37 and all 111
  piers.
- **Pass 71** (`wb_fv_pass71.py`): the workbook defects the sanity check found. It syncs the
  "Suggested .dat interval km" column with the modelled interval on 3,302 rows (2,751 disagreements
  and 551 blanks), so the `.dat` pass cannot write a stale interval; gives the four tub-boat fits
  one hull tonnage of 4.8 GT and re-prices them at GBP 17/GT; re-sizes 53 water overhaul events so
  that the mid-point is the provision times five years rather than the whole annual figure A (the
  15 sailing rows were recovering the continuous head a second time, and 38 more differed by
  rounding or by the same cause); corrects the pass 69 suffix on 68 locomotive notes to state the
  true inherited distance (55 at 109,000, 13 at 40,000) and restores the marker on Classes 89, 90
  and 91; and moves the three narrow-gauge locomotives still on the 109,000 km default (Baguely-
  Drewery, Funkey, Hibberd Planet) to the class and era distance table.
- **What a rebuild still does not reproduce** (measured by the sanity check,
  `sanity-check-2026-11-25.md` section 5): the qualitative maintenance adjustments on locomotive
  rows (for example the Class 47 ×1.05 from the October 1965 failure rate, which pass 49
  overwrote and the generator still applies); the fixed/per-km split of the carriage, wagon and
  multiple-unit rows, which the generator still writes as a whole annual figure; and the pass
  notes after 40, which a rebuild discards. Beyond those three: 444 capital rows differ (317
  multiple-unit rows are on the diesel/electric `28 × power^0.889` ladder in the workbook but on
  the multiple-unit car ladder in the generator, 67 early-electric per-hp rows, 14 multiple-unit
  feature-term rows and 3 steam rows); 827 annual-maintenance rows differ (the 707 multiple-unit
  cars are at the generator's 32.6 carriage rate against the workbook's 66-780 ladder, plus the
  Class 47 adjustment, 6 road and 38 air rows); and all 95 narrow-gauge and maglev overhaul rows
  are missing from a rebuild, because the generator has no branch for either class. The two
  classes the handoff names as reproduced (the electric locomotives, the water rows and the
  piers) do reproduce.

## Remaining work, in order

1. **Documentation review.** This handoff, `maintenance-decomposition.md`,
   `source-composition.md`, `cost-balancing-register.md`, `cost-data-coverage.md`,
   `vehicle-cost-evidence.md`, `mean-annual-distance.md`, `negative-findings.md` and the research
   reports 47-57 state the current treatments and the remaining work. Read
   [negative-findings](negative-findings.md) before commissioning any research pass.
2. **Tram 1950-90 measured figure.** Report 49 closes the 1949-50 point with the Sheffield
   repairs line (147.3 GBP a car-year, repairs-only) and applies the 150 repairs-only rung with
   zero renewals. No measured municipal repairs figure after 1950 was found; the routes are the
   Ministry "Tramways and trolley vehicle undertakings" volumes after 1949-50 and the Glasgow,
   Blackpool and later Sheffield accounts.
3. **Wagon 1972-81.** Report 52 finds the HMRS repair-cost data are archive-only (SKU ME0354);
   the BRB accounts are search-only and the Serpell report has no per-wagon split. The seven-year
   HAA cycle supports the six-year band; the 1.2A event remains an ESTIMATE. Research pass 54
   found no readable measurement but located The National Archives file **AN 112/25, "Unit cost
   of repair: wagons", 1965-1981** (open, not digitised), with AN 112/26, AN 112/87, AN 112/129
   and AN 171/941 as related routes. The ladder's 14.3 and the 1.2A event are unchanged.
4. **Midland carriage price.** Report 53 finds the GBP 225-250 range for 1860s composites, so the
   GBP 62 overhaul is 24.8-27.6 per cent of capital (about 25 per cent). This supports the
   existing Victorian 28 per cent provision; no workbook change.
5. **Carriage size term.** The carriage annual figure is flat per vehicle, so a 1900 50 ft bogie
   carriage and an 1833 four-wheeler carry the same figure: 2.4 per cent of capital against 14
   per cent. The wagon ladder has a (payload/10)^0.4 term; the carriage ladder has none. A seats
   or tare based term is the next research question and would change the overhaul events too.
6. **Maglev maintenance and overhaul evidence.** The acquisition price is applied by pass 65
   (1,088 GBP a seat; the 507.6 Almujibah estimate remains the serial-production floor). The
   maintenance rate stays 0.00010257 GBP a seat-km because no operator account separates
   rolling-stock maintenance. The remaining routes are a Shanghai operator maintenance line, a
   Changsha 架修 contract value and an Incheon asset-class split; [negative-findings](negative-findings.md)
   records them.
7. **Water: the per-gross-ton ladder is applied.** Pass 70 re-based 177 of the 216 rows on the
   measured per-gross-ton capital rates and research pass 57 raised the tonnage coverage to 177
   rows. The remaining work in the class is to close the 18 unidentified hulls (5 generic
   ferries, the three PS Industry fits, ClydeSteamer, 2 early tugs and 7 fishing craft), each of
   which has an archive route in research pass 57 section 6, and to decide whether the
   unavailable groups should later take a type representative.
8. **Class 83, 85, 86 and 87 electric factor.** Pass 66 moved only Classes 89, 90 and 91. Classes
   83, 85, 86 and 87 still take 0.5 of the diesel ladder, and Calder measures the Class 86/0 at
   176,000 km as well as the Class 87 at 274,000 km: both measured figures are of the same order
   as the 1,103 electric point, not the 509 and 825 that the 0.5 factor produces. A decision is
   needed on whether the electric track covers the 1960s and 1970s electrics too.
9. **The qualitative maintenance adjustments that pass 49 overwrote.** `vehicle-adjustments.csv`
   carries sourced factors on some locomotive rows (the Class 47 ×1.05 from the October 1965
   failure rate, research pass 21). Pass 49 rewrote the whole maintenance figure and lost them;
   the generator still applies them, so a rebuild gives the Class 47 216.10 where the workbook has
   205.85. A pass should re-apply the maintenance factors to the locomotive envelope, or the
   factors should be recorded as withdrawn.
10. **Pier maintenance.** Pass 68 charges capital only. Research pass 13 measures no substructure
    maintenance share, and the bridge upkeep rates (0.045-0.24 GBP a m-year) are per metre of
    finished structure. The options are 19 per cent of the bridge upkeep, a measured bridge
    upkeep rate, or leaving the rows blank; the rows are blank now.
11. **The 12 non-carriage narrow-gauge rows that pass 47 touched** (tube stock, Stanhope wagons,
    SR EMU trailers and a passenger wagon) still carry the pre-51 carriage ladder. Report 51's
    evidence is mainline carriage, so they need the same separate decision pass 67 resolved for
    the narrow-gauge carriages.
12. **Generator: what a rebuild still does not reproduce.** The fixed/per-km split of the
    carriage, wagon and multiple-unit rows is still written whole, and a rebuild still discards
    every pass note after 40. The locomotive ladder, the electric track, the Class 92 and 88
    overrides, the measured class duties, the pier share and the carriage distance table are now
    carried.
13. **`.dat` update.** **Decision: not yet.** It remains one total-set pass, not object by
    object, after the workbook review.

## Water: the capital question

The question is which capital ladder the 216 water rows should carry. Both candidates come from
research report 25; they differ in what they take as the size measure.

- **The current ladder is per passenger or per capacity tonne**: 66 GBP a passenger for a
  sea-going ferry, 16.7 for a river or estuary vessel, 40 for a hovercraft, 8.5 GBP a cargo
  tonne, 32 GBP a tonne for steam inland craft. It is recorded in
  [vehicle-cost-evidence](../vehicle-cost-evidence.md) and in the register, but report 25 does
  not contain those rates: they are a conversion of the per-gross-ton fit at an assumed gross
  tonnage per capacity unit.
- **The per-gross-ton ladder is the measured price itself**: 84.1 x GT^0.90 for passenger
  vessels (report 25's fit of 14 vessels, 1924-38, R² 0.992, deflated to 1900 money),
  GBP 17/GT for inland craft (Cambria, 1906) and GBP 35/GT for coastal cargo (BR, 1950-53).

What the data now say about each:

- **The conversion factor is not a constant.** Across the 39 identified vessels the gross
  tonnage per capacity tonne runs from 0.80 to 188.9, and the bands are set by route, not by
  size (river steamers 3.1-9.3, cargo 0.8-2.3, inland craft 0.9-1.5, cross-Channel ferries
  27-45, modern ro-ro 78-189). A per-passenger ladder therefore embeds an unstated assumption
  worth a factor of 200 between the river steamer and the ro-ro.
- **On the 57 rows with a sourced tonnage, the capacity target is a median 0.30 of the per-GT
  figure.** Two individual checks bound the disagreement: *TS King Edward* (502 GT, GBP 33,000
  in 1901) is reproduced almost exactly by the capacity target (32,348) and 31 per cent above the
  per-GT figure (22,669); *Spirit of Britain* (47,592 GT) is priced by the per-GT rate at ten
  times the capacity figure. The capacity ladder is anchored on the 1900s sample and does not
  scale with the size of the ship around the payload.
- **The per-GT ladder is not exact either.** At 1901 it is 31 per cent below the managed price
  and at 2010 about half the measured price in 1900 money; it is a 1924-38 fit applied across
  eras, and the report states the band as ±16 per cent on its own sample.
- **The maintenance side does not decide the question.** At 2 per cent of either capital, a
  500 GT ferry pays 0.9-1.3 GBP a gross ton a year, against the measured 0.24-0.60 GBP/GT of
  1862-1913: within a factor of 2-4 either way, and inside report 56's 2-5 per cent band.

The recommendation to put to the user is therefore: adopt the per-GT capital ladder on the rows
where a sourced tonnage exists (57 rows), use report 56's type bridges for the homogeneous
groups (1.2 GT per capacity tonne inland, 6.2 river, 1.6 cargo), keep the capacity ladder only
where no tonnage or bridge exists, and keep repair at 2 per cent of capital. That replaces an
undocumented conversion with a measured price, at the cost of a median 3.3-fold rise in the
water capital targets. The alternative is to keep the capacity ladder and record it as an
explicitly unproven placeholder.

**Decision, 2026-11-25: adopt the per-gross-ton ladder.** Research pass 57 fills the blank
tonnages where the evidence allows, and pass 70 applies these rates: passenger vessels
(ferries and river boats) 84.1 x GT^0.90; cargo ships and coasters GBP 35 a gross ton; inland
craft (barges and narrowboats) GBP 17 a gross ton; tugs GBP 39 a gross ton, report 25's one
measured tug point (1882, 81 GT); and fishing and small craft at the inland rate, the nearest
measured per-gross-ton price. Repair stays at 2 per cent of the resulting capital, which is
inside report 56's 2-5 per cent band and within a factor of 2-4 of the measured 0.24-0.60 GBP a
gross ton a year.

**What the decision produced.** Research pass 57 raised the tonnage coverage from 57 to 177 of
216 rows: 98 MEASURED, 56 STATED, 23 DERIVED and 39 UNAVAILABLE. Pass 70 re-based 177 rows, a
median x2.55 on the previous capital. The 39 rows left on the capacity rule are: 9 hovercraft
(no gross tonnage exists), 9 holds (the parent carries the hull), 2 towing horses and a towpath
tractor (not vessels), and 18 hulls research pass 57 could not identify (5 generic ferries, 4
river boats including the three PS Industry fits and ClydeSteamer, 2 early tugs and 7 fishing
craft). Each of those rows records that research pass 57 examined it and left the tonnage blank;
the reason and the archive route for each are in report 57 section 6.

**Each object carries its whole hull once.** A pakset water object is a separately purchased
vehicle, and the cargo and mail fits of one hull are alternative configurations of that vehicle,
not sections of a consist. The per-gross-ton price is therefore charged in full on every fit of
a hull: a livestock-fit Clan liner costs the same hull as its bulk fit. Report 57 section 7
cautions against applying a hull's tonnage once per cargo fit; that caution would apply to a
consist, and a ship is not one. The same logic already governed the capacity ladder, where each
fit was priced separately by its own capacity.

## Piers: what was charged and what was not

Pass 68 charges the 111 `Piers & docks` rows at 19 per cent, the midpoint of the measured
13-25 per cent low-bridge substructure share, of the measured rate of the bridge family the
object belongs to. The share is measured: Tower Bridge 15.8 per cent, the Humber 1900 worked
example at 60 ft 25 per cent; Maynard's 200 ft viaduct gives 65.9 and 82.3 per cent, which is why
the pale high-viaduct shares are not applied to objects whose height the pakset does not record.
The object is charged as the substructure component of the equivalent bridge; the deck and track
are carried by the way object. If the object is later shown to carry the deck as well, the target
should rise to the whole bridge rate, not the share. Maintenance is not charged because no
substructure maintenance rate is measured.

The two knowledge-base corrections are closed. Commit `6b46c373c` (2026-11-23) corrected the
1983 and 2016 road maintenance running-cost rows to **177, 23 and 11** and the main timber-ratio
wording; the two remaining ambiguous instances in `cost-data-coverage.md` and
`infrastructure-cost-synthesis.md` are corrected now to **7-8 times the brick rate**. The earlier
handoff wording "178, 22, 12" was a rounded restatement; the current file values in
`base-maintenance.md` are 177, 23 and 11.

## Interim, not settled

- `prices.tab` `vehicle purchase` 1921 and 1922 are a constant-rate bridge pending Feinstein
  p. 150 (print only).
- `passenger fare` 1914-21 is an unclosed plateau; post-1971 mail rates need a Post Office check.
- Steam: the ladder is a complete-engine ladder on engine weight; tank/tender handling is inferred.
  Post-1900 feature premiums are applied relative to the sample's composition (baseline 1.137).
- Aircraft pressurisation and swept wing are unidentifiable in the sample and not applied.
- The tram series changes scope at 1950: the pre-1950 rows are gross of renewals and the 1950-90
  rows are repairs-only. The 150 GBP rung is an estimate constrained by the Sheffield 1949-50
  measurement; no municipal repairs figure after 1950 was found.
- The locomotive series changes scope at 1950: the pre-1950 rows are gross of renewals and the
  1950 row is net. The 25 per cent renewals share is phased out by 1950, so the 1950 rung is
  entered net at 306; the 408 gross alternative is not used. The Class 92 measured level of
  868 GBP at 2018 is a class/duty override for a mixed-traffic locomotive on the Caledonian
  Sleeper, applied by pass 63, not a new time rung; the 1995 rung of 1,045 is retained and the
  2020 rung of 520 remains the Class 66 freight-diesel line. The 868 is not a clean
  electric-passenger anchor, because the class is mixed traffic and the contract covers a
  low-mileage passenger duty.
- Multiple-unit report 45 recommends five-year overhauls before 1948 and six-year overhauls to
  1999, both ESTIMATE; the workbook uses eight years for the whole fleet.
- The carriage 1920 and 1950 levels were applied by pass 62 on report 51 (39 and 121); the
  distance table is separate and does not settle them.
- Pass 62 covers the 758 standard-gauge carriage rows on the distance table. Pass 67 re-bases the
  34 narrow-gauge carriage rows on the same report 51 series. The 12 non-carriage rows that pass
  47 also touched (tube stock, Stanhope wagons, SR EMU trailers and a passenger wagon) still carry
  the pre-51 carriage ladder and need a separate decision.

## Rules in force

1. **Never use a `.dat` price, or a value derived from one, as a target.** Balancing spreadsheets
   other than the two workbooks (`Vehicle cost table.ods`, `Simutrans Ship Balance.xlsx` and the
   rest) are not evidence.
2. **Never use `level` as a cost driver.** A ladder on it reproduces the prices already in the
   `.dat` files.
3. **Read the inventory names exactly.** Name matching has cost several passes: `GWR-Churchward-Star`
   is not `gwr-star`; `LNWR-precursor-webb` is not the Webb compound; Sprinters and Pacers are
   `br-150`, `br-142`; Underground stocks are `LUL_C_Stock` with underscores. Resolve names
   against `cost-inventory.csv`.
4. **Match the sample, not the intuition.** A variance is not a premium until the sample's own
   composition is the baseline.
5. **Unit scales differ by object type.** Ways and bridges are per kilometre (a tile is 125 m);
   platforms use the graphics scale (28.6 m of train per tile, from vehicle `length`); per-object
   classes are scaled 0.125; depots and HQ are unscaled.
6. **Decompose only a confirmed combined total.** If a source gives a component individually, use
   it directly and do not decompose the combined figure. If data contradict a decomposition
   formula, reconsider the formula rather than only flagging the row. Full rule:
   [vehicle-cost/maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md)
   standing rule 0.
7. **Check the file paths before the research.** A generator that reads no files fails silently:
   `evidence_data.BASE` was one directory short, `vehicle_specs()` returned an empty dict and
   every vehicle fell through to defaults. `build_workbooks.py` had the same defect until
   2026-11-25 and could not start. When a class figure looks like a default, check the paths
   first.
8. **Maglev prices use overseas system costs adjusted for labour.** There are no mainline maglevs
   in Britain. Rule and figures:
   [vehicle-cost/maglev-costs](../vehicle-cost/maglev-costs.md).
9. **Use the index the engine uses for that category.** `prices.tab` has separate `general`,
   `vehicle purchase`, `buildings` and `infrastructure` series, and vehicle maintenance stays on
   the `general` series. Check the series name against the category and the year.
10. **A measured annual total is one combined figure.** The object's cost fields must charge it
    exactly once: deduct the components charged through other fields, estimate the rest from
    surrounding evidence, and check that the fields sum to the figure. Do not charge a component
    beside a total that contains it.
11. **A class with no overhaul row is broken.** The money may still be charged continuously, but
    the vehicle never enters works, its wear never resets and its availability never recovers.
    Every vehicle needs an overhaul figure or a stated reason for zero.
12. **Match the object, not the sheet or the class name.** A class-wide filter can include
    objects that are not members of the class.
13. **A scope change is not an arithmetic error.** State the source basis on every row: gross of
    renewals, repairs-only, or contract. Do not deduct a component the source has already put
    outside the figure.
14. **A modern default is not a measurement.** Use the class and era distance table:
    [vehicle-cost/mean-annual-distance](../vehicle-cost/mean-annual-distance.md).
15. **A new note form must extend the audit parser in the same session.** The audit reads the
    wording the patch scripts write; a new wording otherwise appears as "unchecked".
16. **A rebuild is not a patch.** A workbook rebuild discards the pass notes; the patch scripts
    are the supported route for changes after a build.
17. **The pass records are historical.** Current-state documents state the current position; the
    previous states and rejected treatments are in [pass-history](pass-history.md).

## Verification used

Run `py -3 New/ai/cost-balancing/wb_audit_coherence.py` after every pass. The current run reports
3,539 vehicles coverage-clean, 3,265 envelopes checked, 274 zero-priced sections, 0 rows
unchecked and 0 failures. The parser reads the pass 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53,
57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 69, 70 and 71 note forms (pass 68 is infrastructure and
outside the vehicles audit), the standing-charge and written-whole cases, and the hold cases.

Run `py -3 New/ai/cost-balancing/wb_distance_check.py` for the distance table. The current run
reports 1,524 rows with a stated mean (707 multiple units, 758 carriages, 59 trams) and 0
deviations over 10 per cent.

Re-run each patch script in its default dry-run mode after writing; passes 55, 56, 57, 58, 59,
60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 and 71 each report 0 rows changed. The maintenance
workbook has no formula error cells.
The capital workbook's `Snippet prices (6521)` sheet contains literal `#0` and `#20` markers, which
are not formula errors.

Backups of the workbooks before each pass of this session are in the workspace-root scratch folder
`ai/temp/` (not `New/ai/temp/`): `pre-pass66/` to `pre-pass71/`, with `post-pass70/` for the state
before the first rebuild test and `post-rebuild2/` for the earlier one. The sanity check's outputs
are in `New/ai/temp/sanity/` and `New/ai/temp/sanity-rebuild/`.

Backups of the workbooks before the first pass of this session are in `ai/temp/pre-pass57/`.
The pass 62-65 review baselines are `ai/temp/pre-pass62/`, `ai/temp/pre-pass63/`,
`ai/temp/pre-pass64/` and `ai/temp/pre-pass65/`.

## Files

The patch scripts for this work are `wb_fv_pass57.py` to `wb_fv_pass71.py` and
`wb_distance_check.py`, in `New/ai/cost-balancing/`. The independent review is
`sanity-check-2026-11-25.md` (2 blocking, 7 material, 9 minor, 7 observations; the blocking two
are `.dat`-pass decisions). The class and era distance table is
`New/ai/vehicle-cost/mean-annual-distance.md`; its constants are in `evidence_data.py`. The
research reports 49-57 and their `research-pricing-rows-*.csv` sit beside reports 42-48; report
56 writes `water-gross-tonnage.csv`, and report 57 writes `water-gross-tonnage-additions.csv`.
Report 54 is the wagon archive route, report 55 the maglev evidence, report 56 the water gross
tonnage and the capital/maintenance correction, and report 57 the tonnage additions for the
blank rows.
The supporting code is `evidence_data.py` (`LOCO_MAINT_LADDER`, `ELEC_LOCO_LADDER`,
`LOCO_CLASS_OVERRIDES`, `LOCO_DUTY_KM`, `loco_maint()`, `loco_renewals()`,
`locomotive_overhaul()`, `PIER_SHARE`, `pier_extrapolation()`, `WATER_FERRY_RATE`,
`WATER_GT_BRIDGE`, `water_tonnage()`, `water_gt_price()`, `tram_overhaul()`,
`tram_upgrade_share()`, `MEAN_ANNUAL_KM`, `mean_annual_km()`, the report 51 carriage ladder and
the report 55 maglev acquisition constants), `build_workbooks.py` (`maint_a_gbp`, and the path
repair of 2026-11-25) and `wb_audit_coherence.py` (widened parser, `--notes`). The Class 92 and
Class 88 corrections, the locomotive ladder, the pier share and the water ladder are now
carried by the generator as well as the workbook. The current-state documents are this handoff,
`negative-findings.md`,
`maintenance-decomposition.md`, `source-composition.md`, `cost-balancing-register.md`,
`cost-data-coverage.md`, `vehicle-cost-evidence.md`, `vehicle-cost/maglev-costs.md` and
`project-notes.md`; the previous states are in [pass-history](pass-history.md).

## Git and push

The `New/` repository is on branch `ex-15`; the pass 62-65 work is committed at `a3560ded3`,
the pass 66-69 work and its documentation at `58b1a8e3c` and `494791b20`, the water
gross-tonnage work at `3976c0e00` and `3b7192a39`, and the sanity-check fixes at `8f58f1bf3`
(CHANGE) and `1a970ac5c` (DOC), all pushed to `origin/ex-15`. Push with:

    git -C New -c credential.helper="!gh auth git-credential" push \
        https://github.com/jamespetts/simutrans-pak128.britain.git ex-15

## Scratch

`ai/temp/` holds the workbook backups (`pre-pass47` to `pre-pass69`, `post-pass68`,
`post-rebuild2`), the research subagents' scratch folders (`rp47`, `rp48`, `rp53`, `rp54`,
`rp55`, `rp56`), and reference material that cannot be re-fetched (`research-pdfs/`, `erj/`,
`jgl/`, the `fig11_*` scripts). The session state file `ai/temp/session-state-balancing.md` is
deleted at the end of the session; this handoff is the record.
