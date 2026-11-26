---
status: draft
verified: New ex-15 @ cd856ac71 (working tree, 2026-11-26); simutrans-extended-sources ex-15 @ c85608eeeb
---
# Cost-balancing workbooks: independent sanity check, 2026-11-25

**Covers**: `New/cost-balancing-capital.xlsx`, `New/cost-balancing-maintenance.xlsx`, the
generator and patch scripts in `New/ai/cost-balancing/`, research reports 50-57, and the
current-state documents `handoff.md`, `pass-history.md`, `negative-findings.md`,
`cost-balancing-register.md`, `cost-data-coverage.md`, `vehicle-cost-evidence.md` and
`vehicle-cost/*.md`.

This is a read-only review of the state after passes 62-70, run on the night of 2026-11-25/26. No
workbook, patch script, `evidence_data.py`, `build_workbooks.py`, `.dat` file or existing document
was modified. Scratch work is in `New/ai/temp/sanity/`; the scratch rebuild output is in
`New/ai/temp/sanity-rebuild/`.

**Terms used.** A = the measured annual maintenance figure for a class, in 1900 GBP. The
**envelope** is one measured total that already contains some of the components the object's
cost fields must charge; **renewals** and the **provision** are the components deducted from A,
and the **head** is what remains for the continuous charge. These terms are defined in
[maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md). The **smoothstep** is
the engine's cubic easing f(t) = t²(3 − 2t), used by `vehicle_t::get_overhaul_cost()` to raise
the overhaul invoice from the first to the maximum value; its source is `utils/simrandom.h` and
`vehicle/vehicle.cc` in the engine. A **sint32** is a 32-bit signed integer, range
−2,147,483,648 to 2,147,483,647. The **forge cost** is the engine's per-tile way formation
charge in `config/simuconf.tab`; the **way-only** .dat value is the suggested total net of it. A
**capacity rule** prices a water object per passenger or per capacity tonne; the **per-gross-ton
ladder** prices it at a measured rate per gross ton of hull. `first` and `max` are the
`Overhauls & upgrades` sheet's suggested first and maximum overhaul costs, and N is its
"Overhauls to max" value (the engine's `overhauls_before_max_cost`). The **39 capacity-rule water
rows** are the water objects with no usable gross tonnage, which keep the capacity rule. The
**median x2.55** is the median ratio of the new to the previous capital target over the 177
re-based water rows. The **coherence audit** is `New/ai/cost-balancing/wb_audit_coherence.py`;
the **distance check** is `wb_distance_check.py`.

`[CODE New ex-15 @ cd856ac71]` unless a finding says otherwise; engine facts are
`[CODE simutrans-extended-sources ex-15 @ c85608eeeb]`.

## 1. Verdict

**2 blocking, 7 material, 9 minor, 7 observations.** The workbooks are fit for the user's
review. The coherence audit passes unchanged (3,539 vehicles, 3,265 envelopes, 274 zero-priced
sections, 0 unchecked, 0 failures), the distance check passes (1,524 rows, 0 deviations over 10
per cent), and every recent pass re-derives exactly: the 758 carriages, 34 narrow-gauge
carriages, 3 electric locomotives, 111 piers and 216 water rows all reproduce from their stated
rules, as do the 4,182-row conversion chain and the stated water median of x2.55. They are
**not yet fit for the `.dat` pass**: 19 suggested `.dat` values exceed the engine's signed
32-bit cost field, 8 way rows have a suggested total below the forge cost (a negative way-only
value), and the "Suggested .dat interval km" column is stale on 2,751 of 2,971 rows. The most
important items for the review are therefore the two `.dat` blockers and that stale column,
together with the documentation that still describes the pre-decision water and pier
treatments. The overhaul arithmetic is sound for the first cycle: the engine's first event is
`first` and its (N+1)th is `max`, so the mean is exactly (first + max)/2. The note's "over N
overhauls" is off by one, and a vehicle kept beyond the maximum over-recovers (189,890
GBP1900/yr, 1.09 per cent of A, if each of the 3,124 assessed rows takes two further overhauls at
the maximum); that is recorded as an observation because the workbook states no vehicle life. The
recent passes are not the cause of the blocking issues; they inherit them or expose them.

## 1a. Disposition, 2026-11-26

Pass 71 fixes the workbook defects the review found, and the documentation edits of the same day
fix the stale statements. The two blocking items and the two design questions are left for a
decision because they change the `.dat` policy, the forge rule or the overhaul life.

| Finding | Status |
|---|---|
| B1, 19 values above the signed 32-bit cost field | Open: needs a representation decision before the `.dat` pass (cap at 2,147,483,647, widen the engine field, or lower the target) |
| B2, 8 way rows with a negative way-only cost | Open: raise the total to the forge cost, zero the forge, or treat the object as forge-dominated |
| M1, stale suggested interval column | Fixed by pass 71: column 22 synced to column 17 on 3,302 rows |
| M2, rebuild divergences | Recorded in the handoff with the four extra areas; the generator fixes (multiple-unit ladder, narrow-gauge and maglev overhaul branches) remain outstanding |
| M3, README stale | Fixed in the workbook and in `evidence_data.readme_extra()` |
| M4, `negative-findings.md` stale | Fixed |
| M5, pass 69 suffix misstates the old distance | Fixed on 68 rows; the three lost markers restored |
| M6, `vehicle-cost-evidence.md` stale bullets and link | Fixed |
| M7, pier and elevated-way double count | Open: decide whether the way target is the complete structure or the deck |
| m1, register summary and fishing reason | Fixed |
| m2, tub-boat four tonnages | Fixed by pass 71 (4.8 GT on all four fits) |
| m3, water event sized to A | Fixed by pass 71 (53 rows re-sized to the provision) |
| m4, m5, m6, m7, m8, m9, o7 | Fixed in the handoff and the evidence docs; the three narrow-gauge locomotives are moved by pass 71 |
| o2, life-dependent over-recovery | Open: needs a stated vehicle life; recorded in the handoff |

## 2. Findings


| ID | Severity | Object, sheet, row | What is wrong | Evidence | Proposed fix |
|---|---|---|---|---|---|
| B1 | Blocking (`.dat` pass) | 19 capital rows: 18 on `Air vehicles` (787-8 and 787-9 high density; L-1011-1, -200 and -500 high density; 747-100 and 747-100 high density; 747-200B and 747-200B high density; 747-200F mail, piece and perishable; 747-400 and 747-400 high density; 747-400F mail, piece and perishable; 747-8i) and 1 on `Water vehicles` (P&O Spirit class ferry) | The suggested `.dat` total exceeds the engine's cost field. `obj_base_desc.h` declares `sint32 base_cost`; `vehicle_reader.cc` reads the `.dat` cost with `decode_uint32` into it, so a value above 2,147,483,647 wraps negative. Largest: Boeing 747-400F 7,608,981,835; Spirit 2,751,885,867. The current pakset maximum is 532,224,000 (SS Great Eastern). | Capital workbook, column 27 (suggested `.dat` total) on the 19 rows named in this cell; engine `descriptor/obj_base_desc.h` and `descriptor/reader/vehicle_reader.cc`. Because `.dat` = GBP1900 / 0.396311 / 0.00125 = GBP × 2,018.6, any capital above about 1,063,900 GBP1900 overflows. | Decide the representation before the `.dat` pass: cap the 19 rows at 2,147,483,647 and record the cap, or widen the engine field (a code change), or set a lower policy target for those objects. The workbook values themselves are arithmetically correct; it is the field that cannot hold them. |
| B2 | Blocking (`.dat` pass) | 8 way rows: `Ways - road` Bridleway, Cobblestone, Unsurfaced (2), MacAdam, Tar MacAdam; `Ways - air` Grass runway, Grass taxiway | The suggested `.dat` total is below the forge cost, so "way only" (total − forge) is negative: −289,767 / −283,964 / −289,767 / −289,767 / −104,812 / −44,505 on the road rows and −1,682,474 / −1,729,912 on the air rows. A negative cost cannot be written into a `.dat`. | Capital workbook, `Ways - road` and `Ways - air`, columns 27 and 28; the forge costs are Params B21-B28 (315,000 road, 1,875,000 air). | Raise these totals to at least the forge cost, or set the forge cost to zero for the affected way types (the canal precedent in the workbook README), or record the target as "forge-dominated, no separate way cost" and put the measured construction into the forge. |
| M1 | Material (`.dat` pass) | `Overhauls & upgrades`, column 22 "Suggested .dat interval km", 2,751 of 2,971 populated rows | The column disagrees with the modelled interval in column 17. Examples: District carriage 210,000 vs 250,000; Dennis 15cwt van 80,000 vs 160,000; bus rows 35,000 vs 220,000; CSLR tube locomotive 840,000 vs 300,000; WCR tube stock 960,000 vs 250,000. The ratios run from 0.19 to 6.29, so this is not a unit conversion. The engine's `max_distance_between_overhauls` is in km and is not tile-scaled (`vehicle_desc.h`), and an existing `.dat` carries 9,000. | Re-derived from both workbooks: 2,971 rows with a suggested interval, 220 agree, 2,751 differ; the patch passes write column 17 (`wo.cell(q, 17, ...)`) and not column 22. | Copy column 17 into column 22 (or delete column 22) before the `.dat` pass, and state in the handoff which column the pass will write. |
| M2 | Material (handoff and tooling) | Rebuild comparison, 444 capital rows, 827 A rows, 95 overhaul rows | A rebuild diverges from the live workbook in more than the three documented ways. Capital: 444 class-price rows differ (rail 401, air 38, maglev 5 — the maglev five are 58,724 vs 58,725 rounding). Maintenance A: 827 rows differ (rail 781, road 6, air 38, narrow gauge 2). Overhauls: 95 live rows are missing from the rebuild — all 73 narrow-gauge and all 22 maglev rows — which reintroduces the pass-48/pass-50 "no overhaul row" defect; 2,771 matched rows have at least one differing field (9,742 cells). The rail A difference is dominated by 707 multiple-unit cars: the generator writes the Hill 1892 carriage rate (32.6 GBP a vehicle-year for the powered cars, the carriage ladder for the trailers) where the workbook has the multiple-unit ladder (66-780), a cut of up to 96 per cent (780 to 32.6). | `evidence_data.py`, the multiple-unit branch of `extrapolation()` (`maint_gbp_yr=CARRIAGE_MAINT_YR`); the generator's `overhaul_profile()` has no narrow-gauge or maglev branch; the rebuild output in `New/ai/temp/sanity-rebuild/`. | Extend the "What a rebuild still does not reproduce" list in the handoff with these four items, and add the multiple-unit maintenance ladder and the narrow-gauge/maglev overhaul branches to the generator before any rebuild. Keep the `COST_BALANCE_OUT` guard: it worked (the live files' hashes did not change). |
| M3 | Material (documentation) | Capital workbook, README sheet, water and piers paragraphs | The README still says "WATER: priced by capacity, not the flat whole-ship ladder ... Passenger vessels GBP/passenger (sea-going 66, river 16.7, estuary 10); cargo GBP 8.5/t" and "PIERS: the 111 bridge-substructure pier objects are deliberately unpriced". Both directly contradict pass 70 (water on the per-gross-ton ladder) and pass 68 (all 111 piers charged). | README sheet, the rows beginning "WATER:" and "PIERS:". | Replace both paragraphs with the current treatments (per-GT rates; piers at 19 per cent of the family rate, capital only). |
| M4 | Material (documentation) | `negative-findings.md`, section "Water objects and the per-GT rates" | The "Result" cell still says "39 vessels covering 57 rows; 159 rows blank" and the Status paragraph says "applying the per-GT capital ladder to the 57 measured rows is the next pass, and the route-class assignment is the open decision". Both are pre-pass-57/70 statements; the coverage is 177 of 216 and both decisions are closed (2026-11-25). | The file's water section, compared with the handoff's "Decision, 2026-11-25" and the 177/216 count. | Rewrite the Result cell to the current 177/216 and the 39 blank rows, and replace the Status paragraph with the decision and the remaining archive routes (report 57 section 6). |
| M5 | Material (workbook row notes) | `Rail vehicles`, the 68 rows carrying the pass 69 suffix | The suffix reads "the inherited X km default is replaced by the class and era distance table (X km ...)", printing the row's new distance as the inherited one. The true inherited distance was 109,000 on 55 of the 68 and 40,000 on the other 13. Examples: BR Class 71 was 109,000 and is now 65,000, but the note says "the inherited 65,000 km default is replaced ... (65,000 km)"; BR Class 68 was 109,000 and is now 150,000, and the note says 150,000 → 150,000. | Compare the pre-pass workbook at `58b1a8e3c^` (58 Rail rows at 109,000) with the post-pass workbook at `58b1a8e3c`; the current notes; `wb_fv_pass69.py` suffix template and its repair mode (`repair = MARK in note` strips the suffix and re-reads the current distance as `K_old`). | Write the true old value into the suffix (store it and parse it in repair mode), or restore the suffixes from the pre-pass state. The distances and the per-km charges are correct; only the row notes misstate the change. |
| M6 | Material (documentation) | `vehicle-cost-evidence.md`, Ships and aircraft bullets | The same section contains "Gross tonnage is not recorded for any pakset water object" and "The workbook prices passenger vessels per passenger ... and cargo and inland craft per tonne of capacity", followed lower down by "The workbook now uses the per-gross-ton capital ladder". The first two statements are pre-pass-70 and now false; "Cargo is priced at £8.5 per tonne of capacity" also remains as a present-tense statement. | The file's Ships section, the bullets beginning "Gross tonnage is not recorded" and "Cargo is priced at". | Delete or rewrite the two pre-decision bullets as history, and make the £8.5/t statement apply only to the 39 capacity-rule rows. |
| M7 | Material (design consistency) | `Piers & docks` versus `Ways - rail` elevated-track rows | The elevated-way targets include the elevated structure: the "Concrete viaduct elevated track" basis is "installed permanent way ... / elevated structure: ... the DLR City Airport concrete viaduct at GBP 19-24m/km 2005". The pier basis says "the deck and track are carried by the way object it supports", while the engine's way builder checks that a pier exists beneath a raised way where the ground drops away (`bauer/wegbauer.cc`, "universal check for piers"). A player who places one pier tile under each tile of a one-km elevated concrete viaduct therefore pays the complete viaduct rate through the way plus 19 per cent of the bridge rate through the eight pier tiles. | `Ways - rail` Concrete viaduct elevated track (class 411,917 GBP/km); `Bridges & viaducts` ConcreteViaduct (410,317); `Piers & docks` concrete rows (77,960 = 19 per cent); `bauer/wegbauer.cc`. | Decide whether the way target is the complete structure or the deck only. If complete, net the 19 per cent out of the elevated-way targets or set the pier target to zero for elevated-way use; if deck only, state that in the way basis. |
| m1 | Minor (documentation) | `cost-balancing-register.md`, "Cross-cutting status" and the Ships row | The status summary still lists "No: multiple units, ships, aircraft, inland boats ...", although the register's own Ships and Aircraft rows say the class data exist. The Ships row says fishing craft "keep their capacity rule" because there is "no measured rate"; the actual reason is that the seven fishing craft have no usable tonnage (they are among the 39 unavailable rows). | The register's summary paragraph and Ships row. | Update the summary; state the no-tonnage reason for the fishing craft. |
| m2 | Minor (water rule) | `Water vehicles`, 4 Tub Boat rows | One hull is priced at four gross tonnages: TubBoatBulk 4.8 GT / 81.60 GBP, Cool 2.4 / 40.80, Long 2.4 / 40.80, Piece 4.2 / 71.40. Report 57 section 4 states "Gross tonnage is a property of the hull, so every cargo fit of one hull carries the same figure" and rejects bridging each fit separately; the handoff's "each object carries its whole hull once" repeats it. The Handysize (12,600 GT) and Clan (7,168 GT) fits do follow the rule. | `water-gross-tonnage-additions.csv` rows TubBoatBulk/Cool/Long/Piece (method `bridge`); the four capital rows. | Give all four fits one hull tonnage (the largest fit, 4.8 GT, or an independent tub-boat figure) and re-price them at 17 GBP/GT. |
| m3 | Minor (water amortisation) | `Water vehicles`, 15 sailing/small-craft rows | The overhaul event is sized to the whole annual figure A, while a continuous head is also charged: the provision is 90-96 per cent of A and (first + max)/2 is 5 × A to 5.07 × A, not 5 × provision. The head is therefore recovered twice. Rows: Brig (hull), Schooner (hull), 6 Norfolk wherries, 5 skiff wherries, 2 Thames sailing barges. The 13 remaining n=6 rows differ from 5 × provision by 3-7 per cent (rounding/scaling). | The water notes ("provision is 90 per cent of A", "head is the remainder") and the events, e.g. Schooner: A 273.70, provision 246.33, head 27.37, first/max 684.60/2,052.40, mid 1,368.50 = 5 × 273.70. The 15 double-charged heads sum to 55.82 GBP a year at 1900. | Re-size these 15 events to 5 × provision (the mid-point rule) or state the head is included in the event and set the head to zero. Correct the 13 small n=6 discrepancies at the same time. |
| m4 | Minor (handoff accuracy) | `handoff.md`, "What the decision produced" | "Each of those rows says on the capital basis why it was not re-based" overstates the row text: the 18 unidentified hulls say only "research pass 57 examined this row and left the gross tonnage blank (nofigure); the capacity rule stands". The reason (which register would close it) is in report 57 section 6, not on the row. | The 39 capital-basis cells, e.g. "Channel paddle ship (hull)". | Add the actual reason to the 18 rows, or soften the handoff sentence to "each row records that pass 57 left it blank; the routes are in report 57 section 6". |
| m5 | Minor (documentation) | `handoff.md`, "Verification used" | The handoff points to backups in `ai/temp/pre-pass66/` to `pre-pass70/`, `pre-pass57/`, `pre-pass62/`-`pre-pass65/`, `post-pass68/` and `post-pass70/`. None of those folders exists; `ai/temp/` now contains only `refs/`, `sanity/` and `sanity-rebuild/`. | Directory listing of `New/ai/temp/`. | State that the backups were cleared under the scratch rule, or restore them. |
| m6 | Minor (link) | `vehicle-cost-evidence.md`, Ships section | The link `[cost-balancing/handoff](../cost-balancing/handoff.md)` does not resolve: from `New/ai/vehicle-cost-evidence.md` the target is `New/cost-balancing/handoff.md`. It is the only broken relative link in the 454 checked across the reviewed documents. | Link check over the 15 current-state docs and the vehicle-cost folder; 453 of 454 resolve. | Change to `cost-balancing/handoff.md`. |
| m7 | Minor (handoff accuracy) | `handoff.md`, rail-carriage row | "upgrade 7.7 per cent for brake pairs, 25-30 per cent for structural conversion" is not what the sheet holds. Of the 758 pass-62 rows, 682 carry 35 per cent of capital, 56 carry 32.5 per cent, and 20 carry 5.3-6.6 per cent (the brake pairs, e.g. the District four-wheel brake at 53.4/834 = 6.4 per cent; 7.7 per cent may be the share of the pre-pass-62 capital). | Overhauls column 19 divided by column 13 for the 758 pass-62 rows. | State the shares the sheet actually carries, or re-base the 20 brake-pair upgrades to 7.7 per cent of the current capital. |
| m8 | Minor (handoff accuracy) | `handoff.md`, "Verification used" | The parser list omits the pass 43, 45 and 51 note forms, yet 629 audited rows carry those markers (pass 43: 347, pass 45: 22, pass 51: 260), and their envelopes are checked. | Note-marker count over the seven vehicle sheets. | Add 43, 45 and 51 to the list, or say the list names only the forms added after pass 42. |
| m9 | Minor (workbook and documentation) | `Narrow gauge vehicles`, 3 rows: Baguely-Drewery 0-6-0 (1983), Funkey B-B (1968), Hibberd Planet 4wDM (1954) | All three still state 109,000 km and a 763,000 km overhaul interval. Pass 69's scope was the `Rail vehicles` sheet only, so they were never candidates; the documents do not mention them. At their introduction years the class and era table gives 113,000, 113,000 and 65,000 km. | The three rows; `wb_fv_pass69.py` sets `ws = wm['Rail vehicles']`; the pre-pass and post-pass workbooks both show them at 109,000. | Move them to the table, or state in the handoff that the narrow-gauge locomotives are outside pass 69 and why. |
| o1 | Observation | `Water vehicles`, 18 rows | The 18 rows flagged against the 2 per cent rule are 13 that differ only by one-decimal rounding (±0.05 GBP on A), 2 towing horses that take the animal rule (A 45 and 90 GBP an animal-year), and 3 zero-priced holds with no annual figure. No action. | A versus 0.02 × class price for all 216 rows. | None. |
| o2 | Observation | All classes with first < max | The workbook's first-cycle amortisation is exact: the engine's first event is `first` (the counter is 0 at `get_overhaul_cost()`), its (N+1)th event is `max`, and the mean of those N+1 events is exactly (first + max)/2. The note's "over N overhauls" is off by one — the maximum is reached at the (N+1)th event — and a vehicle kept beyond that pays `max` every time, so the lifetime mean exceeds the provision. If each of the 3,124 assessed rows takes two further overhauls at the maximum, the over-recovery is 189,890 GBP1900/yr, 1.09 per cent of A (rail 1.90 per cent, road 4.10, water 3.49, air 1.02, narrow gauge 1.94, tram 0.86). The workbook states no vehicle life, so this is a sensitivity, not a defect. | Engine `utils/simrandom.h` (sigmoid = t²(3 − 2t)) and `vehicle/vehicle.cc` (`get_overhaul_cost()` before `overhauls++`); first-cycle mean recomputed on 3,124 rows, 0 differences from (first + max)/2. | State the assumed vehicle life and the number of overhauls after the maximum, and say "N steps to the maximum, i.e. N+1 events" in the note. |
| o3 | Observation | 19 rows above 2^31 | The values are economically plausible for the objects: the 747-400F target is 76 times its current `.dat` cost, and 3.77m GBP1900 is the hedonic answer for a 2000s freighter. The defect is the encoding, not the price. | Capital rows; current `.dat` 100,000,000 for the 747-400F. | See B1. |
| o4 | Observation | All capital and maintenance sheets | The 1900 deflation uses the right index series per object type: vehicles column 3 of `Index` (vehicle purchase), ways/bridges/piers column 4 (infrastructure), buildings column 5 (buildings), maintenance column 2 (general). All class prices are dated 1900, so the class deflation is a no-op. | The `R` and `Y` formulas on each sheet; the `Index` header. | None. |
| o5 | Observation | Pass scripts 62-70 | All nine dry runs are idempotent and report 0 rows changed, with one count per pass in order: 758 carriages (62), 423 locomotive notes (63), 2 Class 88 rows (64), 22 maglev (65), 3 electrics (66), 34 narrow-gauge carriages (67), 111 piers (68), 68 locomotive rows (69), 216 water rows (70). The pass 69 dry-run count is 68 because three of the 71 notes were later rewritten by pass 66 (o7). | `wb_fv_pass62.py` to `wb_fv_pass70.py`, default dry run. | None. |
| o6 | Observation | `wb_audit_coherence.py` | The audit checks head + provision = A − renewals, but never checks the event against the provision. The first-cycle event arithmetic matches the provision exactly, so the check would only bite if a vehicle life were stated (o2). | The audit's `main()`, the coherence block. | Add an event check that takes an assumed life, or record why the first-cycle check is sufficient. |
| o7 | Observation | `Rail vehicles`, Classes 89, 90 and 91 | These three rows took the pass 69 distance change (109,000 → 113,000 km) but no longer carry the pass 69 suffix, because pass 66 rewrote their notes with the marker list "pass 49, pass 63, pass 66". The values are correct; the provenance record is incomplete. | The three notes and the pre-pass workbook at `58b1a8e3c^`. | Add the pass 69 marker to the three notes, or record in the handoff that pass 66 supersedes it. |

## 3. Checks run

| Check | Method | Coverage | Result |
|---|---|---|---|
| Coherence audit | `py -3 New/ai/cost-balancing/wb_audit_coherence.py` | all seven vehicle sheets | 3,539 vehicles, 3,265 envelopes, 274 zero-priced sections, 0 unchecked, 0 failures |
| Distance check | `py -3 New/ai/cost-balancing/wb_distance_check.py` | carriage, multiple-unit, tram rows | 1,524 rows (707 / 758 / 59), 0 deviations over 10 per cent |
| Envelope re-check | Re-parsed every note with the audit's parser and summed A, renewals, provision and head | 3,189 rows with all four values | 0 failures (largest error 0.44 GBP) |
| Fixed + per-km × K = head | Recomputed from the class columns and the note's stated distance | 2,665 rows | 0 failures beyond rounding |
| Interval = years × K | Recomputed from the note's years and distance | 2,016 rows | 12 mismatches, exactly the 12 non-carriage narrow-gauge rows documented as the known open item |
| Event against the note | Parsed "first at X rising to Y" and "mean event of Z" | 440 locomotive rows | 0 mismatches; the note's mean is (first + max)/2 on every one |
| Event against the provision | Engine sequence simulated exactly: event 1 = first, events 2..N+1 stepped by the smoothstep, event N+2 onward = max; first-cycle mean versus (first + max)/2 | 3,124 rows | 0 differences; the first-cycle amortisation is exact. Two further overhauls at the maximum would over-recover 189,890 GBP1900/yr (1.09 per cent of A), a life-dependent tail (o2) |
| Water re-derivation | Recomputed GT, rate, capital, 2 per cent A and the event from the two CSVs | 216 rows; 177 priced | 0 price mismatches; 0 tonnage or type conflicts; the 39 capacity rows are exactly the 39 without a usable tonnage; 0 rows with a tonnage left on the capacity rule; median factor 2.550 (range 0.127-93.99) |
| Water sister fits | Grouped the 216 rows by the tonnage identity and compared capital | 15 groups with more than one fit | 8 groups differ; 7 are different vessels or capacity-rule fits; the Tub Boat is the one per-GT violation (m2) |
| Piers | Re-derived family, share, price and chain for all rows | 111 rows | 0 problems; families 25 brick, 23 stone, 29 concrete, 16 iron, 3 steel, 15 timber; every price is 19 per cent of the family rate; the basis matches report 13 section 6 |
| Conversion chain | Class price → GBP1900 → SC (/B2) → suggested `.dat` (/B12, /B15 or /B16) on every sheet | 4,182 rows | 0 mismatches; way-only = total − forge on every way row |
| Magnitudes | Maxima and minima per sheet; values above 2^31 and below the forge | all capital sheets | 19 above 2^31 (B1); 8 negative way-only (B2); 7 overhaul upgrade cells above 2^31 (all 747s) |
| Class rules | Ships 2 per cent, holds 1 per cent, maglev 15 per cent provision and 1.2A mid-point | 216 water, all hold rows, 22 maglev | Ships and holds match within rounding; maglev provision 0.150 and mid 1.200A on all 22 |
| Locomotives | Classes 89/90/91 against the electric track; measured duties 37/47/55/86/87 and the CSLR tube; intervals; 109,000 km default | 440 locomotive rows | C89/90/91 exact (1,073.61 / 1,070.39 / 1,067.18), provision 39 per cent, 60/40 split, 791,000 km = 7 × 113,000; all six measured duties correct; 3 rows still at 109,000 (m9); 68 pass-69 notes misstate the old distance (M5) |
| Carriages | A against the ladder × class factor, era band, 70/30 split and interval | 758 standard + 34 narrow gauge | 0 A mismatches; bands and intervals correct; 70/30 holds to rounding; narrow-gauge count 34 |
| Rebuild | `COST_BALANCE_OUT=New/ai/temp/sanity-rebuild py -3 build_workbooks.py`, recalculated with LibreOffice, compared row by row | 3,539 vehicles, 111 piers | Live hashes unchanged; 444 capital, 827 A and 2,771 overhaul rows differ (M2); water and piers reproduce exactly |
| Patch idempotence | Every pass script in default dry-run mode | passes 62-70 | 0 rows changed in every pass |

## 4. Cross-document discrepancies

| Document | Statement | Workbook value | Verdict |
|---|---|---|---|
| `handoff.md` (Passes 66-70) and `pass-history.md` (pass log 69) | "71 locomotive rows ... move to the class and era distance table" | 71 Rail rows changed (pre-pass workbook at `58b1a8e3c^`: 58 at 109,000 plus 13 post-1948 steam at 40,000); 3 narrow-gauge locomotives remain at 109,000 | Count correct for the `Rail vehicles` sheet; the 3 narrow-gauge rows are omitted (m9) |
| Workbook pass-69 notes (68 rows) | "the inherited X km default is replaced ... (X km)" | 55 of the 68 were at 109,000 and 13 at 40,000; the note prints the new value | Wrong note (M5) |
| `negative-findings.md` (water section, Status) | "applying the per-GT capital ladder ... is the next pass, and the route-class assignment is the open decision" | Pass 70 applied the ladder; 177 of 216 rows priced; the decision is dated 2026-11-25 | Stale (M4) |
| `negative-findings.md` (water section, Result) | "39 vessels covering 57 rows; 159 rows blank" | 177 rows with a figure, 39 blank | Stale (M4) |
| Capital workbook README (water paragraph) | "priced by capacity, not the flat whole-ship ladder" | Per-gross-ton ladder on 177 rows | Stale (M3) |
| Capital workbook README (piers paragraph) | "the 111 ... pier objects are deliberately unpriced" | All 111 charged at 19 per cent | Stale (M3) |
| `vehicle-cost-evidence.md` (Ships) | "Gross tonnage is not recorded for any pakset water object"; "Cargo is priced at £8.5 per tonne of capacity" | 177 rows carry a tonnage; cargo priced at GBP 35/GT on those rows | Stale (M6) |
| `cost-balancing-register.md` (Cross-cutting status; Ships) | "No: multiple units, ships, aircraft, inland boats"; fishing craft "no measured rate" | Ships and aircraft have measured evidence; the fishing craft lack tonnage | Stale reason (m1) |
| `handoff.md` (Current treatments, rail carriages) | "upgrade 7.7 per cent for brake pairs, 25-30 per cent for structural conversion" | 682 rows at 35 per cent, 56 at 32.5, 20 at 5.3-6.6 | Inaccurate (m7) |
| `handoff.md` (Verification used) | Backups in `ai/temp/pre-pass66/` ... `post-pass70/` | Folders do not exist | Stale (m5) |
| `handoff.md` (Verification used) | The audit parser reads the pass 42, 44, 46, ... forms | It also checks 629 rows marked pass 43, 45 and 51 | Incomplete (m8) |
| `handoff.md` (What the decision produced) | "Each of those rows says ... why it was not re-based" | 18 rows say only that pass 57 left the figure blank | Overstated (m4) |
| `handoff.md` | 3,539 vehicles, 3,265 envelopes, 274 zero-priced, 0/0; 1,524 distance rows | Same | Correct |
| `handoff.md` | 177 of 216 water rows; 98 MEASURED, 56 STATED, 23 DERIVED, 39 UNAVAILABLE; median x2.55 | Same; median computed from the 177 note factors = 2.550 | Correct |
| `handoff.md` / register / evidence | 111 piers at 19 per cent; 34 narrow-gauge carriages; 1,087.5 maglev; Class 88 614.82; Class 89/90/91 1,073.61/1,070.39/1,067.18; Class 92 868 | Same | Correct |
| `handoff.md` | "A test rebuild reproduces ... all 216 water capital targets exactly ... and all 111 piers" | 0 water capital diffs, 0 pier diffs | Correct (capital only; water maintenance fixed differs by the documented split) |
| `handoff.md` | "A rebuild discards the pass 40-61 notes" and the three-item "what a rebuild still does not reproduce" | 444 capital, 827 A, 95 missing overhaul rows in addition | Incomplete (M2) |

No document still says the narrow gauge has 35 rows (all say 34), the generator is "workbook-only",
or Class 90 is unresolved; Class 90 appears only in the handoff's resolved decision.

## 5. Rebuild comparison

`$env:COST_BALANCE_OUT = "<absolute path to New/ai/temp/sanity-rebuild>"; py -3 New/ai/cost-balancing/build_workbooks.py`
ran without error and wrote both workbooks to the scratch folder. The live files' SHA-256 hashes
before and after were identical (`221547FA...` capital, `BDCC1F49...` maintenance), and
`git -C New status` shows only the expected untracked `ai/temp/`. The environment variable is
therefore respected.

| Area | Rows differing | Detail |
|---|---|---|
| Capital, class price | 444 | Rail 401 (317 multiple-unit rows on the diesel/electric `28 × power^0.889` ladder in the live workbook vs the generator's multiple-unit car ladder; 67 on the early-electric per-hp ladders, 42 of them pre-1948 and 25 for 1948-55; 14 on the multiple-unit ladder with a different feature term; 3 on the steam weight ladder), air 38 (33 class, 5 measured; mail fits with no seats differ by up to 61 times, e.g. MailMonoPlane 457 vs 27,970), maglev 5 (58,724 vs 58,725 rounding). Water 0, piers 0. |
| Maintenance A | 827 | Rail 781 (the multiple-unit rows at the generator's 32.6 carriage rate vs the workbook's 66-780 multiple-unit ladder; the Class 47 216.10 vs 205.85 is the documented qualitative adjustment), air 38 (follows the capital), road 6 (5 pack-horse pairs at 90 vs 45; mail-boot 0.5 vs 2.5), narrow gauge 2 (24.75 vs 24.80 rounding). |
| Maintenance fixed with the same A and a live per-km charge | 1,086 | The documented split gap: the generator writes the whole annual figure as the fixed charge. |
| Maintenance fixed with the same A and no live per-km charge | 469 | The wagon head: the live fixed is 0.8A and the generator writes A (e.g. BulkRCH12T 4.40 vs 5.50). Part of the documented split gap. |
| Overhauls | 2,771 rows, 9,742 cells | Interval km 2,432, first 2,063, max 2,050, overhauls-to-max 1,448, capital 645, upgrade 1,104. The generator's `locomotive_overhaul()` uses seven years for every locomotive, so the steam rows move (e.g. GER H88 "Super Claud" 260,000 → 280,000 km); the water rows get no interval; the multiple-unit and road events follow the A differences. |
| Overhaul rows present | 95 | All 73 narrow-gauge and all 22 maglev rows are missing from the rebuild: the generator still has no branch for either class, so a rebuild would reintroduce the pass-48 and pass-50 "no overhaul row" defect. |

The objects the handoff explicitly names as reproduced do reproduce: Classes 86, 87, 88, 89,
90, 91, 92 and 37, and all 111 piers (capital and per-km; the Class 47's A is the documented
exception). The two split areas in the table (the fixed charge with a live per-km charge, and the
wagon head) are the documented difference; the other four areas are beyond it. The three
documented differences (the qualitative locomotive maintenance adjustments, the
carriage/wagon/multiple-unit fixed-per-km split, and the pass notes after 40) are present and are
not reported as defects.

## 6. Known open items: confirmed as documented

| Open item | Documented? |
|---|---|
| Qualitative locomotive maintenance adjustments lost by pass 49 (Class 47 ×1.05) | Yes: handoff item 9, with the 216.10 vs 205.85 example |
| Classes 83, 85, 86, 87 still on the 0.5 electric factor | Yes: handoff item 8 and the pass-history rejected-treatments list |
| Pier maintenance blank | Yes: handoff item 10 and the handoff table |
| 12 non-carriage narrow-gauge rows on the pre-51 ladder | Yes: handoff item 11 and the interim section; the 12 are the 12 interval mismatches |
| Generator does not reproduce the fixed/per-km splits or the pass notes | Yes, but incompletely: the A and overhaul gaps of M2 are not listed |
| 18 unidentified water hulls and 3 non-vessels | Yes: handoff "What the decision produced", pass-history pass 70, report 57 section 6, and the 39 rows' basis text |

## 7. What could not be checked, and why

- **The pre-pass workbooks.** The handoff's scratch backups in `New/ai/temp/` have been cleared,
  so the passes could not be diffed against their scratch predecessors. The committed workbook at
  `58b1a8e3c^` was extracted from git to verify pass 69 (58 Rail rows at 109,000 before the pass);
  the other passes were checked from the current state, the dry runs and the notes. The median
  x2.55 was re-derived from the 177 factors stated in the maintenance notes.
- **Whether the suggested `.dat` values are the right policy targets.** Only their internal
  consistency and representability were checked. The `.dat` pass has not been done by design, so
  no target was compared with a `.dat` field (and the `.dat` files were confirmed unmodified).
- **The measured evidence behind the ladders.** Reports 13 and 57 were read against the workbook
  and the CSVs; reports 25, 44, 46, 50, 51, 55 and 56 were used only as cited by the notes and
  were not re-audited. The independent re-derivation therefore tests the arithmetic and the
  application of the stated rules, not the historical measurements themselves.
- **The non-vehicle, non-pier sheets.** Stations, signals, signalboxes, roadsigns, depots, tunnels,
  bridges other than the pier family, and the engine settings were checked for chain consistency
  and magnitude but not for the correctness of their measured rates.
- **The maglev seat and length basis.** The 22 capital values were checked against the workbook's
  own 1,087.5 per seat / 4,194.6 per metre constants and the maintenance rate; the underlying
  seat counts and car lengths were not re-read from the `.dat` files.
- **The engine's index values at historical dates.** The object-type columns are correct and all
  class prices are at 1900, so the class deflation is a no-op; the measured-price series were not
  re-checked against `prices.tab` year by year.
- **The vehicle service life.** The workbook states no retirement age, so the tail over-recovery in
  o2 is a sensitivity, not a measured quantity. A stated life (or a measured scrapping age by
  class) would turn it into a checkable number.
- **The `Continuous brakes` sheet.** It is outside the vehicle audit and was not reviewed.

## Open questions

- Should the overhaul provision cover only the first cycle (N+1 events, where the mean is exactly
  (first + max)/2) or a stated vehicle life that includes the flat maximum? The answer changes o2's
  tail estimate.
- Is the elevated-way target the complete structure or the deck only? The answer decides M7.
- Which column will the `.dat` pass write for the overhaul interval: the modelled column 17 or the
  stale "suggested" column 22?
