---
status: draft
verified: New ex-15 @ 23149dd57 (working tree), 2026-11-25
---
# Source composition of maintenance source figures

**Covers**: what each maintenance source states that its source figure contains, and the
decomposition treatment that composition requires in the maintenance workbook
(`New/cost-balancing-maintenance.xlsx`, columns AA-AC of the seven vehicle sheets). Read before
applying the decomposition identity, before netting a renewals share or an overhaul provision
from any source figure, and before changing those columns. Also read when a source figure is being
added to the workbook: the treatment is decided here, not per row.
Parent: [maintenance-decomposition](maintenance-decomposition.md). Evidence:
[base-maintenance](base-maintenance.md), [published-maintenance](published-maintenance.md),
[road-maintenance-1959-2016](road-maintenance-1959-2016.md),
[tram-maintenance](tram-maintenance.md), [ship-maintenance](ship-maintenance.md),
[aircraft-maintenance](aircraft-maintenance.md),
[inland-boat-maintenance](inland-boat-maintenance.md),
[horse-keep-totals](horse-keep-totals.md), [horse-keep-components](horse-keep-components.md),
[modern-traction-locomotives-and-wagons](modern-traction-locomotives-and-wagons.md),
[modern-traction-multiple-units](modern-traction-multiple-units.md); research record:
[research-pricing-report-39](../cost-balancing/research-pricing-report-39.md),
[research-pricing-report-40](../cost-balancing/research-pricing-report-40.md),
[research-pricing-report-15](../cost-balancing/research-pricing-report-15.md).

## Why the treatment is decided per source

A maintenance source figure is money spent on some set of activities. Three of those activities
are charged elsewhere in the engine, so money attributed to them in the maintenance fields would
be charged twice:

- **routine upkeep** — repairs, servicing, cleaning, inspection. This is the part the
  maintenance fields are for.
- **renewals** — replacing the vehicle. In-game this is the player's purchase decision, charged
  through `cost` and `upgrade_price`.
- **major works** — overhauls. In-game these are charged as events through the overhaul fields
  (`initial_overhaul_cost`, `max_overhaul_cost`, `max_distance_between_overhauls`).

The decomposition equation `annual maintenance figure = renewals provision + overhaul provision + routine remainder` in
[maintenance-decomposition](maintenance-decomposition.md) subtracts all three. It is valid only
for a source figure that the source states contains all three. A figure whose composition is
different must be treated according to what the source states, and a figure whose composition is
not stated at all must be left whole: assuming that an element is inside a figure is never
acceptable, because the assumption cannot be checked against the source and it silently moves
money between the fields. `[USER-DIRECTION:2026-11-25]`

No source in the checked-out files states that its figure contains routine upkeep, renewals and
major works together. **Full identity therefore currently applies to no source figure**, and the
identity is a general equation, not a rule to apply. `[CODE New ex-15 @ 23149dd57]`

## Element vocabulary

| Mark | Meaning |
|---|---|
| CONTAINED | the source's own wording states that the activity is inside the figure |
| NOT CONTAINED | the source's wording or table structure places the activity outside the figure |
| UNRECORDED | no checked-out source states either way for this figure |

## Composition table

| Source figure (and where it is used) | What the source states, verbatim or as its table structure | Routine | Renewals | Major works | Citation |
|---|---|---|---|---|---|
| Hill 1895 rail maintenance: per vehicle-year for carriages (£18 6s.-£52 14s., average £33 6s.) and wagons (£4 4s.), per engine-year (£184-£253) and per train-mile (2.51d.) for locomotives; used for every rail carriage, locomotive, multiple-unit and narrow-gauge row | "maintenance, that is the cost of repairs and renewals"; "the more general rule appears to be to include the cost of renewals with that of repairs"; locomotive running expenses (fuel, enginemen, water, shed) are a separate abstract | CONTAINED | CONTAINED | UNRECORDED — the repairs element is not itemised, and no passage states that a works overhaul is charged inside it | `[LITERATURE:https://doi.org/10.1680/imotp.1895.19704]` Hill 1895, *Minutes of the Proceedings of the ICE* 122, Appendix II Tables I-III and Appendix III Tables XXIII-XXV; [published-maintenance](published-maintenance.md) rows for 1892 and traps 1-3 |
| Hill 1895 renewal rates (3.6% locomotives, 2.53% carriages, 3.1% wagons a year by number) | renewal rate by stock number, not a money head; the source of the renewals shares used to size the renewals provision | — | CONTAINED (by definition) | NOT CONTAINED | Hill 1895 Appendix III Tables XXIII-XXV; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §2 |
| The 8-per-cent-of-capital wagon rule (generator rule, one head for every wagon row) | no source states the rule; its level evidence is Hill's £4 4s. a wagon-year for "repairs and renewals" | UNRECORDED | UNRECORDED | UNRECORDED | `[CODE New ex-15 @ 23149dd57]` `New/ai/cost-balancing/evidence_data.py` (wagon maintenance clause) |
| The 5-per-cent-of-capital cart and motor-trailer rule (generator rule) | no source states the rule; it is applied both to horse-drawn carts and to motor trailers | UNRECORDED | UNRECORDED | UNRECORDED | `[CODE New ex-15 @ 23149dd57]` same generator, cart-maintenance clause |
| Commercial Motor maintenance item (buses, coaches, lorries, vans) | "washing, servicing and major repairs"; the 1959 comparison: "this item consists of two elements. One is the repair work, which varies directly with the mileage run, and the other is servicing and washing, which are normally scheduled on a time basis"; tyres and depreciation are separate items in the same tables, and the maintenance item is itself split into "routine operations" and "repairs and overhauls" | CONTAINED | NOT CONTAINED (depreciation is a separate line) | CONTAINED | `[LITERATURE: Commercial Motor, 2 Jan 1959, pp. 62-65]`; [published-maintenance](published-maintenance.md) traps 5-7; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5; the 1947 coach costing carries engine reconditioning and body overhauls inside the maintenance total ([research-pricing-report-31](../cost-balancing/research-pricing-report-31.md)) |
| FTA 2016 lorry and trailer maintenance line (trailer rows) | "Maintenance as a separate running-cost line. Fuel £28,182, tyres £1,877, VED, insurance and depreciation are separate lines" | CONTAINED | NOT CONTAINED | UNRECORDED | `[LITERATURE: FTA Managers' Guide to Distribution Costs, October 2016]`, reproduced in CLOCS, *Investigating the Construction Industry's Use of HGV Types*, Figs 6-7; [road-maintenance-1959-2016](road-maintenance-1959-2016.md) |
| Merseyside PTE bus costs (1983/84) — not used as a head | a "repairs and maintenance" figure of 53.7p a mile is printed, and the PTE total of 196.4p a mile "includes maintenance, management and depreciation charges", so the maintenance element cannot be separated; the generator excludes it because the repairs head carries depot and works overheads no other source carries | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: Commercial Motor, 21 Jan 1984, p. 8 and 5 Jan 1985, p. 8]`; [road-maintenance-1959-2016](road-maintenance-1959-2016.md); generator comment |
| Tram Ministry of Transport car-only figure, "General Repairs and Maintenance (or Renewals out of Revenue)", Cars and other Rolling Stock column (pre-1950 tram rows) | the column covers "repairs and renewals charged to revenue of cars and their equipment only"; fund renewals, reserve appropriations and depreciation are printed in a separate part of the return; whether works overhauls are inside is not stated | CONTAINED | CONTAINED (revenue renewals only) | UNRECORDED | `[LITERATURE: MoT Tramways and Light Railways Returns, Abstract of Totals Part II, 1919-20 to 1932-33]`; [tram-maintenance](tram-maintenance.md) §A4; [research-pricing-report-39](../cost-balancing/research-pricing-report-39.md) §7.1 |
| Nottingham Express Transit 2011 rolling-stock maintenance contract (modern tram rows) | an availability payment: £101m over 23 years for 37 trams; no recorded source states its workscope | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: NET/Alstom contract as reported]`; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5; [tram-maintenance](tram-maintenance.md) §B |
| Martin 1924, 5 per cent of original investment a year (general cargo steamer) | "maintenance repairs only, paid from a depreciation reserve; excludes depreciation itself, insurance and fuel" | CONTAINED | NOT CONTAINED | UNRECORDED | `[LITERATURE:https://www.jstage.jst.go.jp/article/jjasnao1903/1924/35/1924_35_184/_pdf/-char/en]` Martin, "Economy of Ship Repairs", *Journal of the Society of Naval Architects of Japan* 35 (1924), p. 184; [published-maintenance](published-maintenance.md) |
| Kirkaldy 1913, "annual overhaul £30,000" on a £1,500,000 liner | "Overhaul only, stated separately from depreciation and from the 5 per cent return on capital in the same estimate" | NOT CONTAINED | NOT CONTAINED | CONTAINED (this is the overhaul element itself) | `[LITERATURE:https://archive.org/details/britishshippingi0000kirk]` Kirkaldy, *British Shipping* (1914), p. 211; [ship-maintenance](ship-maintenance.md) row F32 |
| The 2-per-cent-of-capital water rule (every water row) | the level evidence is the 1850 GSN repair bill (£31,896 for 44 vessels = £788 a vessel-year); the 2 per cent is report 15's 1900-1920 band, "measured (1913 liner overhaul alone is 2.0 per cent; running repairs would add)" | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: Forrester 2006 via research-pricing-report-15]`; [research-pricing-report-15](../cost-balancing/research-pricing-report-15.md) §3.1-3.2 |
| BOAC 1969/70 engineering cost per flying hour, used as a 20-per-cent-of-capital head (every aircraft row) | "Engineering" column only: fuel, obsolescence, landing fees, traffic handling and minor costs are separate columns and excluded; "The source does not itemise engineering into airframe, engine and components" | CONTAINED | NOT CONTAINED (obsolescence is a separate column) | UNRECORDED | `[LITERATURE:https://www.vc10.net/Data/Economics_VC10.html]` Hall, *Aircraft Procurement in BOAC* (1974), Table 1, via vc10.net; [aircraft-maintenance](aircraft-maintenance.md) §1 |
| CAA item 17 and the IATA MCX maintenance total (not used as a head) | item 17 includes engineering base costs, training, travel, accommodation and office costs; MCX covers "line, components, engines, heavy checks and modifications" | CONTAINED | UNRECORDED (aircraft depreciation is a separate charge) | CONTAINED | [published-maintenance](published-maintenance.md) trap 9; [aircraft-maintenance](aircraft-maintenance.md) |
| London horse keep, 1876-97 (£28-£60 a year, central £45) | itemised feed, farriery, veterinary care and stabling, "excluding the horsekeeper's wages"; the accounts used exclude depreciation of the animal (other accounts in the same file include it) | CONTAINED | NOT CONTAINED | NOT APPLICABLE (the horse's renewal is its replacement, charged as the overhaul) | [horse-keep-totals](horse-keep-totals.md) T-series and summary; `[LITERATURE: London horse-account series 1876-97]` |
| Horse-vehicle repair accounts (1760s coach £70 a coach-year; 1893-97 horse-only accounts £29-47) | repair bills per vehicle-year; no source separates rebuilds (wheels, axles, springs, bodywork) from routine repairs | CONTAINED | NOT CONTAINED | UNRECORDED | [base-maintenance](base-maintenance.md) coverage table; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5 |
| Sailing refit provision (Martin 5 per cent, with a refit share) | Martin's figure is maintenance repairs excluding depreciation; no source states that a hull, rig and spar refit is inside it | UNRECORDED | NOT CONTAINED | UNRECORDED | [ship-maintenance](ship-maintenance.md); [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5 |
| TRB Special Report 180 per-locomotive-year totals (modern traction; used for class duties only) | total maintenance cost per locomotive-year with annual distance stated; the abstract does not separate renewals or overhaul events | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: TRB Special Report 180]`; [modern-traction-locomotives-and-wagons](modern-traction-locomotives-and-wagons.md) |

## Treatments

| Treatment | When it applies | What the workbook holds |
|---|---|---|
| **FULL IDENTITY** — deduct the renewals provision and the overhaul provision | the source states routine upkeep, renewals and major works are all inside the figure | nothing currently: no checked-out source states all three for any source figure |
| **PARTIAL, renewals** — deduct the renewals provision only | the source states renewals are inside and is silent on major works | Hill 1895 rail figures: carriages 35 per cent, locomotives 25 per cent; tram car-only figure: 40 per cent. The routine remainder is split fixed/per-km at the class share with the mean annual distance stated as an assumption |
| **PARTIAL, overhauls** — deduct the overhaul provision only | the source states major repairs are inside and keeps depreciation outside | Commercial Motor road figures: the overhaul provision is the annualised provision from the `Overhauls & upgrades` sheet; the renewals share is zero; the remainder keeps the generator's 75/25 distance/standing split |
| **NO DECOMPOSITION** — deduct nothing | the figure is repairs-only or standing-only, so nothing recorded is charged twice | horse keep and horse-vehicle repairs: whole figure in the fixed column, no per-km figure (standing rule 2 of [maintenance-decomposition](maintenance-decomposition.md)); FTA trailer line: nothing deducted, generator split retained |
| **OPEN QUESTION** — deduct nothing, split nothing | the composition is not stated anywhere in the checked out files | whole figure in the fixed column, no per-km figure, and a note naming the passage that would settle it: the 8-per-cent wagon rule, the 5-per-cent motor-trailer rule, the 2-per-cent water rule, the 20-per-cent aircraft rule, and the modern tram contract |

The renewals-share and overhaul-provision figures themselves, and the fixed/distance splits, are not decided here: they are
the values of [maintenance-decomposition](maintenance-decomposition.md) (renewals shares and the
per-class splits) and of the `Overhauls & upgrades` sheet of
`New/cost-balancing-capital.xlsx` (overhaul shares and intervals).

## What would change a treatment

- **A works repair account.** A pre-1911 company repair account, or the post-1911 "Repairs and
  partial renewals" column, showing heavy general work carried in the repairs element would make
  the Hill rail figures FULL IDENTITY and add an overhaul deduction.
- **A stated workscope for a modern contract.** The NET maintenance schedule would settle the
  modern tram rows.
- **A ship repair account.** One separating running repairs from surveys and renewals would let
  the water rows be decomposed; until then the 2-per-cent share stays whole.
- **A BOAC or IATA engineering breakdown.** Airframe, engine and component shares would settle
  whether heavy checks and engine shop visits are inside the aircraft head.
- **A wagon repair contract** with its workscope would settle the 8-per-cent wagon rule.

## Open questions

- Do Hill's repairs contain works overhauls? The passage that would settle it is a company
  repair account (or the post-1911 Abstract B "Repairs and partial renewals" column) itemising a
  heavy general; until then the rail rows deduct renewals only, and their notes give the
  overhaul provision that a settled answer would remove.
- What does the 8-per-cent wagon rule cover? No source in the files states it; the level
  evidence (Hill £4 4s.) covers repairs and renewals.
- Is the 2-per-cent ship share the overhaul alone (as report 15's note suggests for 1900-1920)
  or a whole-upkeep figure? The ship rows are therefore written whole.
- What workscope does the Nottingham 2011 tram contract carry?
- The workbook's pre-1950 tram head (64 GBP a car-year in 1900 money) is not reconciled in the
  files to the car-only per-car-mile series (1.98d in 1923-24 falling to 1.52d in 1932-33):
  deflating either figure to 1900 money gives a materially higher level. Which passage the 64
  came from is unrecorded, so the tram rows' level is open even though their treatment is not.
- The `Overhauls & upgrades` sheet's road overhaul provisions exceed the maintenance head on a
  large minority of road rows (for example a pre-1930 bus at 25 per cent of capital a year,
  against a total Commercial Motor maintenance head of about 18 per cent of capital). The two
  workbook figures cannot both be right; the notes on the affected rows state the arithmetic and
  write the whole head, and a bus or lorry overhaul invoice with its interval would settle which
  figure is wrong.
