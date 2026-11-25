# Cost-balancing workbooks: handoff

**Status**: analysis complete and committed 2026-11-25; `.dat` costs deliberately NOT changed.
The workbooks carry the current treatments and are ready for the user's review.

## What this is

Two workbooks, `New/cost-balancing-capital.xlsx` and `New/cost-balancing-maintenance.xlsx`, compare
every `.dat` price in the pakset with a target derived from **measured historical evidence**. The
target column must never take a `.dat` price as an input: that is the quantity under audit, and
using it to build the target is circular.

Coverage: **4,071 of 4,218 objects have a capital target (97%); 4,154 have a maintenance target
(98%)**. Both workbooks rebuild with zero error cells.

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
| Rail carriages | 33 / 140 / 265 / 460 / 440 GBP a vehicle-year at 1900 / 1950 / 1970 / 1990 / 2020, log-linear between and flat outside | Provision 28 / 24 / 19 / 12 / 10 / 8 per cent of A at 6 / 5 / 3 / 2 / 2 / 2.6 years; first event 0.70 of the maximum over three; upgrade 7.7 per cent for brake pairs, 25-30 per cent for structural conversion | 70/30 | 35,000 / 36,000 / 55,000 / 88,000 / 120,000 / 113,000 km by era |
| Rail wagons | 4.2 / 8.7 / 14.3 / 24.8 / 23.8 GBP per 10-tonne wagon-year at 1900 / 1950 / 1970 / 1990 / 2020, scaled by (payload/10)^0.4 | Head 0.8A; event 1.2A every six years, first event 0.75 of the steady event; upgrade 10-20 per cent for brake pairs | 65/35 | 40,000 km |
| Rail locomotives | 215 / 306 / 800 / 2,100 / 1,045 / 520 GBP an engine-year at 1900 / 1950 / 1961 / 1977 / 1995 / 2020, log-linear between | Renewals 25 per cent (22.5 for 1948-61 electric, 20.6 for 1962+ diesel/electric); provision 35 per cent steam and 39 per cent diesel/electric; events scaled to the provision | 60/40 steam, 50/50 diesel/electric | The row's own measured duty |
| Multiple units | 66 / 241 / 380 / 510 / 780 GBP a car-year at 1900 / 1950 / 1970 / 1990 / 2020, log-linear between | Provision 15 per cent of A; event 1.2A every eight years, first event 0.70 of the maximum over three; upgrade 8-12 per cent refresh, 20-25 per cent re-tractioning | 50/50 | 100,000 / 120,000 / 161,000 km by era; tube and metro 120,000 |
| Trams | Pre-1950 gross 84 / 131 / 106 / 89 GBP a car-year at 1900 / 1920 / 1931 / 1939; 1950-90 repairs-only 150 (band 130-210); 1990+ 1,177 | Pre-1950: renewals 35 per cent, provision 28 per cent at two years, event 0.35A rising to 0.75A. 1950-90: renewals 0, provision 28 per cent at three years, event 0.54A rising to 1.15A. 1990+: renewals 0, provision 6 per cent at twelve years, one event of 0.75A. Upgrade 0.22 of the new price to 1950, rising linearly to 0.50 by 1990 | 50/50 | 48,000 km to 1989; 90,000 km from 1990 |
| Buses and coaches | Measured Commercial Motor level, rescaled to the 37.5 per cent overhaul composition | 220,000 km, 25 to 40 per cent of capital, rescaled to the measured annual share | 75/25 | 55,000 km overhaul reference; 40,000 km split reference |
| Lorries and vans | Measured Commercial Motor level | Introduction-year bands: before 1930 35-50 per cent, 1930-59 44-56, 1960-84 25-35, 1985-2004 20-30; intervals 80,000 / 80,000 / 160,000 / 400,000 km; vans 80,000 / 160,000 km | 75/25 | 40,000 km split reference (25,000 for short-duty vans) |
| Ships | Measured repair level; see [source-composition](../vehicle-cost/source-composition.md) | Five-year special survey; 2 to 5 per cent of capital | 50-65 per cent standing | 115,000 km |
| Aircraft | BOAC engineering cost per flying hour; see [aircraft-maintenance](../vehicle-cost/aircraft-maintenance.md) | C-check every 4,000-6,000 flight hours; 2.5 to 5 per cent of capital; D-check in the cycle | Class rule | 4,200,000 km per C-check |
| Maglev | Overseas system unit costs; see [maglev-costs](../vehicle-cost/maglev-costs.md) | 15 per cent of A, event 1.2A every eight years | 50/50 | 300,000 km |
| Holds and animals | Holds are containers inside a vehicle: 1 per cent of their own capital, no per-km charge. Animals are 45 GBP an animal-year (90 for a pair), standing only | Holds take no overhaul and a zero target; animals replace at 100 per cent of the purchase price at 70,000 km; upgrade 50 per cent | Holds all fixed; animals all fixed | Holds none; animals 10,000 km a year |

The current coherence audit reports 3,539 vehicles, 3,265 envelopes checked, 274 zero-priced
sections, 0 unchecked and 0 failures. The distance check reports 1,524 rows with a stated mean
and 0 deviations over 10 per cent.

## Remaining work, in order

1. **Documentation review.** This handoff, `maintenance-decomposition.md`,
   `source-composition.md`, `cost-balancing-register.md`, `cost-data-coverage.md`,
   `vehicle-cost-evidence.md`, `mean-annual-distance.md` and the research reports 47-53 state
   the current treatments and the remaining work. The user reviews and approves the docs before
   any commit.
2. **Carriage re-base on report 51 (not applied).** Report 51 recommends 39 GBP a carriage-year
   in 1900 money for 1920 (band 28-55) and 121 for 1950, against the current interpolations; 1948
   falls at 112 and 1966 at 226, and the 1990 rung of 460 stands untested. A carriage pass would
   change the annual figure A, the provision, the head and the event in 758 rows, so it needs a
   fresh backup and a full audit.
3. **Locomotive report 50 (not applied).** Keep the ladder levels 215 / 306 / 800 / 2,100 /
   1,045 / 520. The measured 1913-1938 points validate the 1900-1950 interpolation within 5 per
   cent; do not add a 1922 rung. Add the measured Class 92 level of 868 GBP at 2018 as a
   class-specific override (band 740-1,000), keep 520 at 2020 for the Class 66 freight line, and
   state the 1950 composition break (pre-1950 gross of renewals, 1950 net) in the basis text. If
   the 25 per cent renewals deduction is kept on the pre-1961 rows, the 1950 rung is 408 gross so
   that the deduction returns 306 net. Report 46 covers the diesel/freight line; report 50 covers
   the electric-passenger line.
4. **Tram 1950-90 measured figure.** Report 49 closes the 1949-50 point with the Sheffield
   repairs line (147.3 GBP a car-year, repairs-only) and applies the 150 repairs-only rung with
   zero renewals. No measured municipal repairs figure after 1950 was found; the routes are the
   Ministry "Tramways and trolley vehicle undertakings" volumes after 1949-50 and the Glasgow,
   Blackpool and later Sheffield accounts.
5. **Wagon 1972-81.** Report 52 finds the HMRS repair-cost data are archive-only (SKU ME0354);
   the BRB accounts are search-only and the Serpell report has no per-wagon split. The seven-year
   HAA cycle supports the six-year band; the 1.2A event remains an ESTIMATE.
6. **Midland carriage price.** Report 53 finds the GBP 225-250 range for 1860s composites, so the
   GBP 62 overhaul is 24.8-27.6 per cent of capital (about 25 per cent). This supports the
   existing Victorian 28 per cent provision; no workbook change.
7. **Carriage size term.** The carriage annual figure is flat per vehicle, so a 1900 50 ft bogie
   carriage and an 1833 four-wheeler carry the same figure: 2.4 per cent of capital against 14
   per cent. The wagon ladder has a (payload/10)^0.4 term; the carriage ladder has none. A seats
   or tare based term is the next research question and would change the overhaul events too.
8. **Maglev unit costs** are estimates (Almujibah and Preston 2018), not operator accounts. An
   Aichi Rapid Transit or Shanghai rolling-stock maintenance line would replace them; the open
   questions are in `maglev-costs.md`.
9. **Water size ladder.** The measured rates are ready: ferries 84.1 x GT^0.90 in 1900 GBP (R2
   0.992), coastal cargo GBP 35/GT, inland GBP 17/GT. Blocked because the pakset records no gross
   tonnage. `water-capacity.csv` gives hull+hold capacity in tonnes; the missing step is a
   GT-versus-capacity bridge fitted from research pass 25. Then replace the flat GBP 38,958 ship
   ladder.
10. **General feature premiums.** Only road engine type and carriage dining/bogie/steel are
    wired. Transmission, suspension, heating, air conditioning, low floor, corridor, sleeping and
    tram articulation are researched (pass 8) and have attribute columns, but no multipliers.
11. **Piers**: 111 objects unpriced. Decision needed: leave at zero (bridge carries the structure)
    or charge the measured 13-25% substructure share.
12. **Knowledge-base corrections awaiting review**: the 1983 and 2016 road maintenance rows are
    2.4x too small (decimal pence treated as old pence; corrected 178, 22, 12); "timber bridge
    upkeep 7-8 times plain line" should read "7-8 times the brick rate".
13. **Generator alignment.** `evidence_data.py` carries the tram ladder and
    `tram_overhaul()`, the multiple-unit distance table and the tram upgrade share;
    `build_workbooks.py` passes `maint_a_gbp` to `overhaul_profile()`. A rebuild still discards
    every pass note after 40, and the carriage distance table is not wired into the generator;
    the patch scripts remain the supported route.
14. **`.dat` update.** The point of the exercise. Do it as one total-set pass, not object by
    object, after the workbook review.

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
  1950 row is net. The Class 92 measured level of 868 GBP at 2018 is a class override, not a new
  time rung; the 1995 rung of 1,045 is retained.
- Multiple-unit report 45 recommends five-year overhauls before 1948 and six-year overhauls to
  1999, both ESTIMATE; the workbook uses eight years for the whole fleet.
- The carriage 1920 and 1950 levels await the report 51 re-base; the distance table is separate
  and does not settle them.

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
   every vehicle fell through to defaults. When a class figure looks like a default, check the
   paths first.
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
unchecked and 0 failures. The parser reads the pass 42, 44, 46, 47, 48, 49, 52, 53, 57, 58, 59,
60 and 61 note forms, the standing-charge and written-whole cases, and the hold cases.

Run `py -3 New/ai/cost-balancing/wb_distance_check.py` for the distance table. The current run
reports 1,524 rows with a stated mean (707 multiple units, 758 carriages, 59 trams) and 0
deviations over 10 per cent.

Re-run each patch script in its default dry-run mode after writing; passes 55, 56, 57, 58, 59,
60 and 61 each report 0 rows changed. The maintenance workbook has no formula error cells. The
capital workbook's `Snippet prices (6521)` sheet contains literal `#0` and `#20` markers, which
are not formula errors.

Backups of the workbooks before the first pass of this session are in `ai/temp/pre-pass57/`.
Later passes overwrote the same two files; the pre-pass57 copies are the review baseline.

## Files

The patch scripts for this work are `wb_fv_pass57.py` to `wb_fv_pass61.py` and
`wb_distance_check.py`, in `New/ai/cost-balancing/`. The class and era distance table is
`New/ai/vehicle-cost/mean-annual-distance.md`; its constants are in `evidence_data.py`. The
research reports 49-53 and their `research-pricing-rows-*.csv` sit beside reports 42-48.
The supporting code is `evidence_data.py` (tram ladder, `tram_overhaul()`, `tram_upgrade_share()`,
`MEAN_ANNUAL_KM`, `mean_annual_km()`), `build_workbooks.py` (`maint_a_gbp`) and
`wb_audit_coherence.py` (widened parser, `--notes`). The current-state documents are this
handoff, `maintenance-decomposition.md`, `source-composition.md`, `cost-balancing-register.md`,
`cost-data-coverage.md`, `vehicle-cost-evidence.md` and `project-notes.md`; the previous states
are in [pass-history](pass-history.md).

## Git and push

The `New/` repository is on branch `ex-15`; this work is committed. Push with:

    git -C New -c credential.helper="!gh auth git-credential" push \
        https://github.com/jamespetts/simutrans-pak128.britain.git ex-15

## Scratch

`ai/temp/` holds the workbook backups, the research subagents' scratch folders (`rp47`, `rp48`,
`rp53`), and reference material that cannot be re-fetched (`research-pdfs/`, `erj/`,
`jgl/`, the `fig11_*` scripts). The session state file `ai/temp/session-state-balancing.md` is
deleted at the end of the session; this handoff is the record.
