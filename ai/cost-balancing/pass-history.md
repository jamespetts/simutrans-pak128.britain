---
status: draft
verified: New ex-15 @ 35fb36f78 + passes 66-69 (working tree), 2026-11-25
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
- **The carriage 1920 interpolation of 59 and the 1950 rung of 140.** Report 51's 1912 company
  mean and 1913-1921 rolling-stock change give 39 at 1920 (band 28-55) and 121 at 1950; pass 62
  applies them, with 1948 at 112 and 1966 at 226 by interpolation.
- **The Class 92 ladder value of 543.16.** It is half the 1994 rung under the blanket electric
  factor. The 2018 Alstom/GB Railfreight contract measures 868; pass 63 applies it as a class
  override, not a time rung.
- **The 408 gross 1950 locomotive rung.** The workbook phases the 25 per cent renewals share out
  by 1950 and enters the 1950 rung net at 306; the gross alternative is not used.
- **The 0.5 electric factor for the Class 88.** It is Calder's 1977 Class 87/Class 47 passenger
  result; the 2014 Class 88 is a dual-mode mixed-traffic locomotive, and the Class 68 diesel at
  the same date (614.82) is the nearest measured class. Pass 64 withdraws the factor for the
  Class 88.
- **The 507.6 GBP a seat maglev acquisition estimate.** It is the Almujibah and Preston
  serial-production model; the only transaction-level price, the 2003 Shanghai imported car, gives
  1,088 GBP a seat. Pass 65 applies the transaction figure and records 507.6 as the floor.
- **The 0.5-of-the-diesel-ladder value for the intermediate electric locomotives.** 740.69,
  712.52 and 685.42 on Classes 89, 90 and 91 are half the Class 47 line, from Calder's 1977
  Class 87/Class 47 ratio. Report 50 shows the ratio is a class result, not a traction-type
  constant, and the measured electric track gives 1,073.61, 1,070.39 and 1,067.18; pass 66
  applies it. The 0.5 factor still prices Classes 83, 85, 86 and 87, which is an open question:
  Calder also measures the Class 86 at 176,000 km (the same order as the 1977 electric point).
- **The inherited 109,000 km locomotive mean annual distance.** Pass 49 read a single distance
  from the workbook's earlier default on 40 diesel and electric rows and on 11 post-1948 steam
  rows at 40,000 km. Pass 69 replaces the defaults with the class and era distance table; the
  measured class duties of Classes 37, 47, 55, 86 and 87 and the CSLR tube locomotive stay.

## Pass log, 42-65

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
- **62**: 758 standard-gauge carriage rows re-based on report 51; 39 at 1920 and 121 at 1950,
  1948 112 and 1966 226, 1900/1970/1990/2020 stand.
- **63**: 423 locomotive notes record the report 50 1913-1938 validation and the 1950 composition
  break; the mixed-traffic Class 92 takes the measured 868 class/duty override (Caledonian
  Sleeper).
- **64**: the Class 88 loses the 0.5 electric factor (A 307.41 to 614.82, the Class 68 level);
  the Class 92 notes say mixed traffic on the Caledonian Sleeper duty.
- **65**: the 22 maglev capital targets take the Shanghai acquisition price, 1,087.5 GBP a seat
  (4,194.6 GBP a metre for stock with no seat count) in place of 507.6.
- **66**: the BR Class 89, 90 and 91 leave the 0.5-of-the-diesel-ladder rule for the measured
  electric-locomotive track (1,476 at 1950, 1,103 at 1977, 1,045 at 1995, 868 at 2018); A becomes
  1,073.61, 1,070.39 and 1,067.18 in place of 740.69, 712.52 and 685.42.
- **67**: the 34 narrow-gauge carriage rows are re-based on research report 51, as pass 62 did for
  the standard gauge; A, the provision, the head and the event are recomputed with the class
  factors kept, and the overhaul interval becomes the band's years at the narrow gauge's own
  40,000 km a year.
- **68**: the 111 `Piers & docks` rows take the measured 13-25 per cent substructure share at its
  19 per cent midpoint against the bridge family's measured rate; capital only, and the basis is
  recorded on every row.
- **69**: 71 locomotive rows whose stated mean annual distance was the inherited 109,000 km
  default (and 11 post-1948 steam rows at the 40,000 km default) move to the class and era
  distance table; the measured class duties stay, and only the per-km charge and the overhaul
  interval move.

## Link from current docs

Current-state documents link here when the earlier state explains a rule. They do not repeat the
history inline.
