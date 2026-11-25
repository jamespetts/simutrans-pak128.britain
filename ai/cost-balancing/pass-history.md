---
status: draft
verified: New ex-15 @ 70a098c64 (working tree), 2026-11-25
---
# Pass history and rejected treatments

**Covers**: previous states of the cost-balancing workbooks and the treatments they replaced.
Read this only when the earlier state is needed to avoid repeating a failure. Current rules and
current values are in [handoff](handoff.md),
[vehicle-cost/maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md) and
[cost-balancing-register](../cost-balancing-register.md).

**This document records history.** It is not current guidance. A "withdrawn" or "replaced"
statement here means the treatment is not in the workbooks; it does not describe what the
workbooks now do. A **pass** is one numbered workbook patch script (`wb_fv_pass*.py`) or research
report (`research-pricing-report-*.md`). The terms for the combined figure and the continuous head
follow [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md).

## Failure modes that motivated the decomposition rule

1. **A class with no overhaul row.** Pass 48 found that no narrow-gauge vehicle had an overhaul
   row: the generator's `overhaul_profile()` had no branch for `narrowgauge-vehicles`. The
   money was charged continuously, but the vehicle never entered works, its wear never reset and
   its availability never recovered. The same defect existed for the 22 maglev rows (pass 50).
   Nothing errored; the rows simply had no target.
2. **A capital-share overhaul charged on top of a measured total.** Pass 49 found 827 locomotive
   rows charging a works overhaul beside Hill's annual figure, which already contained it. The
   over-recovery reached 2.8 times the measured cost on the Class 92. Passes 46, 47, 48, 49, 50
   and 51 undid the same pattern for wagons, carriages, narrow gauge, locomotives, maglev, trams,
   water, aircraft and multiple units.
3. **A capped head in place of a measured figure.** Passes 51 and 55 found tram rows whose
   annualised overhaul exceeded the routine remainder after a renewals deduction; earlier passes
   had capped the head at 10 per cent of the total. Pass 55 replaced those rows with measured
   figures and removed the cap.
4. **A class-wide filter applied to the wrong objects.** Pass 55 matched every positive-capital
   row on the `Tram vehicles` sheet, including six horses. It wrote the tramcar ladder to them,
   and pass 56 wrote the tram rebuild share. Pass 57 restored the animal rule.
5. **An inherited modern default.** Pass 53 put every multiple-unit car on a 172,600 km a
   car-year duty, an inherited pass 42 default rather than a measured figure. Pass 59 replaced
   it with the class and era table.
6. **A scope change treated as an arithmetic error.** Pass 58 deducted 35 per cent renewals from
   the 1950-90 tram rung, which report 49 shows is a repairs-only head. Pass 61 set renewals to
   zero and the overhaul provision to 28 per cent at three years.

## Rejected treatments

- **Hill 1895's GBP 253 an engine-year** as the locomotive total. It is the Great Western
  maximum, not the nineteen-company average of GBP 208 18s.; the dated ladder in
  [research-pricing-report-46](research-pricing-report-46.md) replaces it.
- **The GBP 64 tram car-year as a gross figure.** It is a net-of-renewals 1930s figure. The
  gross historic ladder starts at 84 GBP and the 1950-90 rung is repairs-only 150 GBP
  ([research-pricing-report-47](research-pricing-report-47.md);
  [research-pricing-report-49](research-pricing-report-49.md)).
- **The GBP 1,301 modern tram figure.** It is a 2009-index conversion; the 2011 conversion is
  1,177 GBP ([research-pricing-report-47](research-pricing-report-47.md)).
- **Capital-share overhauls for carriages, wagons, locomotives, trams and trailers.** They
  charge a component beside a total that contains it. The workbooks use provisions of the
  measured annual total instead.
- **The 8-per-cent-of-capital wagon rule and the flat GBP 38,958 ship ladder.** The wagon
  ladder is 4.2 / 8.7 / 14.3 / 24.8 / 23.8 GBP per 10-tonne wagon-year; the ship treatment is
  in [source-composition](../vehicle-cost/source-composition.md).
- **22 maglev vehicles: the Hill 1895 steam figure and the diesel/electric purchase ladder are
  withdrawn.** Maglev prices come from overseas system costs adjusted for labour
  ([vehicle-cost/maglev-costs](../vehicle-cost/maglev-costs.md)).
- **The tramcar ladder on the six tram-sheet horses.** Withdrawn by pass 57; the animal rule
  applies.
- **The 172,600 km multiple-unit default.** Withdrawn by pass 59; the distance table applies.

## Pass log, 42-61

Each entry is a one-line record only; the research reports and patch scripts hold the detail.

- **42**: road maintenance splits and fixed/per-km treatment.
- **43**: animals on horse keep; maglev from overseas system costs; buses and coaches on the
  37.5 per cent overhaul composition; four lorry overhaul bands; carriage and wagon ladders;
  wagon head 0.8A and event 1.2A every six years.
- **44**: 263 lorry rows on the four introduction-year bands.
- **45**: carriage and wagon maintenance ladders.
- **46**: 56 standard-gauge wagon rows on the envelope.
- **47**: 1,077 carriage rows on the measured era bands and overhaul provision.
- **48**: 73 narrow-gauge vehicles given an overhaul row; 17 animal rows repointed to the
  replacement rule.
- **49**: 827 locomotive rows on the dated ladder; the second per-km charge removed.
- **50**: 22 maglev rows given an overhaul row.
- **51**: 556 tram, water, aircraft and multiple-unit rows put on the envelope.
- **52**: two holds given no overhaul and nominal maintenance.
- **53**: 707 multiple-unit cars on the report 45 ladder.
- **54**: 65 road trailers on the measured refurbishment.
- **55**: 65 trams and 65 trailers on the measured ladders; no cap.
- **56**: tram upgrade prices from the two measured rebuilds.
- **57**: the six tram-sheet horses restored to the animal rule.
- **58**: tram recalibration on report 47; modern renewals, reference distance and interval.
- **59**: 707 multiple-unit cars on the distance table.
- **60**: 758 carriage rows on the distance table.
- **61**: final tram calibration on report 49; 1950-90 repairs-only, 50/50 split.

## Link from current docs

Current-state documents link here when the earlier state explains a rule. They do not repeat the
history inline.
