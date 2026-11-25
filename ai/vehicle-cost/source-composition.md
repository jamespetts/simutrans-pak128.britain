---
status: draft
verified: New ex-15 @ fcd40c0bc + passes 62-65 (working tree), 2026-11-25
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
[research-pricing-report-42](../cost-balancing/research-pricing-report-42.md) (lorry overhaul
composition), [research-pricing-report-43](../cost-balancing/research-pricing-report-43.md)
(carriage and wagon maintenance levels), [research-pricing-report-15](../cost-balancing/research-pricing-report-15.md).

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

## When decomposition applies at all

The direction that governs this document `[USER-DIRECTION:2026-11-25]`:

- Decomposition arithmetic is needed **only** where a source gives a figure that is a confirmed
  combined total of two or more quantities the pakset represents in separate fields, and the
  components are not stated separately.
- Where a source gives one or more of those quantities individually for a vehicle, those figures
  are used directly and the combined figure is never decomposed.
- Where some components are known and others are not, the known ones are used directly and the
  missing ones are estimated. The estimate must be as specific to the vehicle as the data allow.
- A decomposition applied across a class must rest on a formula that has been assessed against the
  data. If data contradict it for any vehicle or set of vehicles, the formula is reconsidered from
  the ground up — discarded, modified, or limited to the range where it is rigorously supported —
  and not merely flagged as an anomaly.

## Element vocabulary

| Mark | Meaning |
|---|---|
| CONTAINED | the source's own wording states that the activity is inside the figure |
| NOT CONTAINED | the source's wording or table structure places the activity outside the figure |
| UNRECORDED | no checked-out source states either way for this figure |

## Composition table

| Source figure (and where it is used) | What the source states, verbatim or as its table structure | Routine | Renewals | Major works | Citation |
|---|---|---|---|---|---|
| Hill 1895 rail maintenance: per vehicle-year for carriages (£18 6s.-£52 14s., average £33 6s.) and wagons (£4 4s.), per engine-year (£184-£253) and per train-mile (2.51d.) for locomotives; used for the rail carriage, locomotive and narrow-gauge rows that have no measured ladder | "maintenance, that is the cost of repairs and renewals"; "the more general rule appears to be to include the cost of renewals with that of repairs"; locomotive running expenses (fuel, enginemen, water, shed) are a separate abstract | CONTAINED | CONTAINED | UNRECORDED — the repairs element is not itemised, and no passage states that a works overhaul is charged inside it | `[LITERATURE:https://doi.org/10.1680/imotp.1895.19704]` Hill 1895, *Minutes of the Proceedings of the ICE* 122, Appendix II Tables I-III and Appendix III Tables XXIII-XXV; [published-maintenance](published-maintenance.md) rows for 1892 and traps 1-3 |
| Hill 1895 renewal rates (3.6% locomotives, 2.53% carriages, 3.1% wagons a year by number) | renewal rate by stock number, not a money head; the source of the renewals shares used to size the renewals provision | — | CONTAINED (by definition) | NOT CONTAINED | Hill 1895 Appendix III Tables XXIII-XXV; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §2 |
| Ministry of Transport Railway Returns, "Maintenance and Renewal of Rolling Stock - Locomotives", 1913-1938 | the statutory head contains complete renewals and repairs and partial renewals, both charged to revenue, and is net of engine power supplied to or by the company; fuel, water, enginemen and superintendence are in Abstract C | CONTAINED | CONTAINED | UNRECORDED (the repairs element is not itemised; the measured total is used as the envelope) | `[LITERATURE: Ministry of Transport Railway Returns, 1923 and 1930 volumes]`; [research-pricing-report-50](../cost-balancing/research-pricing-report-50.md) |
| Wagon maintenance ladder, research pass 43 (one head for every wagon row) | 4.2 / 8.7 / 14.3 / 24.8 / 23.8 GBP per 10-tonne wagon-year at 1900 / 1950 / 1970 / 1990 / 2020, scaled by (payload/10)^0.4 | CONTAINED | UNRECORDED | UNRECORDED | [research-pricing-report-43](../cost-balancing/research-pricing-report-43.md); [research-pricing-report-46](../cost-balancing/research-pricing-report-46.md); [wagon-overhaul-source-analysis](../cost-balancing/wagon-overhaul-source-analysis.md) |
| The 5-per-cent-of-capital cart rule and the measured motor-trailer refurbishment | the cart rule has no source; it remains for horse-drawn carts only. Motor trailers take the measured refurbishment of 0.33 of the capital target every eleven years (about 3 per cent of capital a year), deducted from the FTA line | UNRECORDED (cart); CONTAINED (trailer refurbishment is a measured event) | UNRECORDED | CONTAINED (the trailer refurbishment is the overhaul) | [research-pricing-report-48](../cost-balancing/research-pricing-report-48.md); passes 54-55 |
| Commercial Motor maintenance item (buses, coaches, lorries, vans) | "washing, servicing and major repairs"; the 1959 comparison: "this item consists of two elements. One is the repair work, which varies directly with the mileage run, and the other is servicing and washing, which are normally scheduled on a time basis"; tyres and depreciation are separate items in the same tables, and the maintenance item is itself split into "routine operations" and "repairs and overhauls". The composition is measured for one fleet: the 1947 account of twelve 32-seat coaches gives GBP 426.7 a vehicle-year, of which engine reconditioning (GBP 120) and body overhaul (GBP 200) on alternate years are GBP 160, or 37.5 per cent | CONTAINED | NOT CONTAINED (depreciation is a separate line) | CONTAINED | `[LITERATURE: Commercial Motor, 2 Jan 1959, pp. 62-65]`; `[LITERATURE: Commercial Motor, 2 May 1947, p. 50]`; [published-maintenance](published-maintenance.md) traps 5-7; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5; the 1947 coach costing is [research-pricing-report-31](../cost-balancing/research-pricing-report-31.md) §2.1 |
| FTA 2016 lorry and trailer maintenance line (trailer rows) | "Maintenance as a separate running-cost line. Fuel £28,182, tyres £1,877, VED, insurance and depreciation are separate lines" | CONTAINED | NOT CONTAINED | CONTAINED as a measured refurbishment: 0.33 of the capital target every eleven years, its annual share deducted from the FTA line | `[LITERATURE: FTA Managers' Guide to Distribution Costs, October 2016]`, reproduced in CLOCS, *Investigating the Construction Industry's Use of HGV Types*, Figs 6-7; [road-maintenance-1959-2016](road-maintenance-1959-2016.md); [research-pricing-report-48](../cost-balancing/research-pricing-report-48.md) |
| Merseyside PTE bus costs (1983/84) — not used as a head | a "repairs and maintenance" figure of 53.7p a mile is printed, and the PTE total of 196.4p a mile "includes maintenance, management and depreciation charges", so the maintenance element cannot be separated; the generator excludes it because the repairs head carries depot and works overheads no other source carries | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: Commercial Motor, 21 Jan 1984, p. 8 and 5 Jan 1985, p. 8]`; [road-maintenance-1959-2016](road-maintenance-1959-2016.md); generator comment |
| Tram Ministry of Transport car-only figure, "General Repairs and Maintenance (or Renewals out of Revenue)", Cars and other Rolling Stock column (pre-1950 tram rows) | the column covers "repairs and renewals charged to revenue of cars and their equipment only"; fund renewals, reserve appropriations and depreciation are printed in a separate part of the return. Pre-1950 rows treat the head as gross: renewals 35 per cent and the works-overhaul provision 28 per cent at two years. The 1950-90 rung is a repairs-only head from the measured Sheffield account: no renewals deduction and a 28 per cent overhaul provision at three years. The 1990-2026 contract has zero renewals and a 6 per cent provision | CONTAINED (pre-1950); NOT CONTAINED (1950-90 repairs-only) | CONTAINED (revenue renewals only pre-1950) | CONTAINED (the pre-1950 head is the envelope; a two-yearly complete overhaul is measured at the LCC Charlton works) | `[LITERATURE: MoT Tramways and Light Railways Returns, Abstract of Totals Part II, 1919-20 to 1932-33]`; [tram-maintenance](tram-maintenance.md) §A4; [research-pricing-report-39](../cost-balancing/research-pricing-report-39.md) §7.1; [research-pricing-report-47](../cost-balancing/research-pricing-report-47.md); [research-pricing-report-49](../cost-balancing/research-pricing-report-49.md) |
| Nottingham Express Transit 2011 rolling-stock maintenance contract (modern tram rows) | an availability payment: £101m over 23 years for 37 trams; no recorded source states its workscope. The workbook treats it as the gross annual total with zero renewals and a 6 per cent overhaul provision at twelve years | CONTAINED | NOT CONTAINED (the contract excludes renewal and the capital lease) | CONTAINED as a 6 per cent provision; the workscope is unrecorded | `[LITERATURE: NET/Alstom contract as reported]`; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5; [research-pricing-report-47](../cost-balancing/research-pricing-report-47.md) |
| Martin 1924, 5 per cent of original investment a year (general cargo steamer) | "maintenance repairs only, paid from a depreciation reserve; excludes depreciation itself, insurance and fuel" | CONTAINED | NOT CONTAINED | UNRECORDED | `[LITERATURE:https://www.jstage.jst.go.jp/article/jjasnao1903/1924/35/1924_35_184/_pdf/-char/en]` Martin, "Economy of Ship Repairs", *Journal of the Society of Naval Architects of Japan* 35 (1924), p. 184; [published-maintenance](published-maintenance.md) |
| Kirkaldy 1913, "annual overhaul £30,000" on a £1,500,000 liner | "Overhaul only, stated separately from depreciation and from the 5 per cent return on capital in the same estimate" | NOT CONTAINED | NOT CONTAINED | CONTAINED (this is the overhaul element itself) | `[LITERATURE:https://archive.org/details/britishshippingi0000kirk]` Kirkaldy, *British Shipping* (1914), p. 211; [ship-maintenance](ship-maintenance.md) row F32 |
| The 2-per-cent-of-capital water rule (every water row) | the level evidence is the 1850 GSN repair bill (£31,896 for 44 vessels = £788 a vessel-year); the 2 per cent is report 15's 1900-1920 band, "measured (1913 liner overhaul alone is 2.0 per cent; running repairs would add)" | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: Forrester 2006 via research-pricing-report-15]`; [research-pricing-report-15](../cost-balancing/research-pricing-report-15.md) §3.1-3.2 |
| BOAC 1969/70 engineering cost per flying hour, used as a 20-per-cent-of-capital head (every aircraft row) | "Engineering" column only: fuel, obsolescence, landing fees, traffic handling and minor costs are separate columns and excluded; "The source does not itemise engineering into airframe, engine and components" | CONTAINED | NOT CONTAINED (obsolescence is a separate column) | UNRECORDED | `[LITERATURE:https://www.vc10.net/Data/Economics_VC10.html]` Hall, *Aircraft Procurement in BOAC* (1974), Table 1, via vc10.net; [aircraft-maintenance](aircraft-maintenance.md) §1 |
| CAA item 17 and the IATA MCX maintenance total (not used as a head) | item 17 includes engineering base costs, training, travel, accommodation and office costs; MCX covers "line, components, engines, heavy checks and modifications" | CONTAINED | UNRECORDED (aircraft depreciation is a separate charge) | CONTAINED | [published-maintenance](published-maintenance.md) trap 9; [aircraft-maintenance](aircraft-maintenance.md) |
| London horse keep, 1876-97 (£28-£60 a year, central £45) | itemised feed, farriery, veterinary care and stabling, "excluding the horsekeeper's wages"; the accounts used exclude depreciation of the animal (other accounts in the same file include it) | CONTAINED | NOT CONTAINED | NOT APPLICABLE (the horse's renewal is its replacement, charged as the overhaul) | [horse-keep-totals](horse-keep-totals.md) T-series and summary; `[LITERATURE: London horse-account series 1876-97]` |
| Horse-vehicle repair accounts (1760s coach £70 a coach-year; 1893-97 horse-only accounts £29-47) | repair bills per vehicle-year; no source separates rebuilds (wheels, axles, springs, bodywork) from routine repairs | CONTAINED | NOT CONTAINED | UNRECORDED | [base-maintenance](base-maintenance.md) coverage table; [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5 |
| Sailing refit provision (Martin 5 per cent, with a refit share) | Martin's figure is maintenance repairs excluding depreciation; no source states that a hull, rig and spar refit is inside it | UNRECORDED | NOT CONTAINED | UNRECORDED | [ship-maintenance](ship-maintenance.md); [research-pricing-report-40](../cost-balancing/research-pricing-report-40.md) §5 |
| TRB Special Report 180 per-locomotive-year totals (modern traction; used for class duties only) | total maintenance cost per locomotive-year with annual distance stated; the abstract does not separate renewals or overhaul events | UNRECORDED | UNRECORDED | UNRECORDED | `[LITERATURE: TRB Special Report 180]`; [modern-traction-locomotives-and-wagons](modern-traction-locomotives-and-wagons.md) |
| Maglev vehicle acquisition and maintenance (every maglev row) | acquisition from the 2003 Shanghai imported-car transaction: RMB 100m a car, GBP 105,129 a car in 1900 money, 92.8 seats a car = 1,087.5 GBP a seat after labour (band 761-1,133); maintenance from the overseas unit cost, EUR 0.011 a seat-km at 2009 prices (0.00010257 GBP). Individual figures, not a combined total | CONTAINED (the figures are the pakset's purchase and per-km maintenance fields) | - | - | `[LITERATURE:https://doi.org/10.17816/transsyst201843s1298-327]` Almujibah and Preston 2018, Table 6 for maintenance; `[LITERATURE:https://finance.sina.com.cn/chanjing/b/20050518/07101596819.shtml]` for acquisition; [maglev-costs](maglev-costs.md); [research-pricing-report-55](../cost-balancing/research-pricing-report-55.md) |

## Treatments

The rule that governs this table is standing rule 0 of
[maintenance-decomposition](maintenance-decomposition.md): where a source gives one combined
figure covering several cost fields, the fields must sum to it; a component is deducted only
where the source states it is inside and another field charges it; an estimated split is used
where the composition is unrecorded; and no class is left without an overhaul figure or a stated
reason for zero. The five treatments below are the per-source application of that rule; the
difference between the last two is whether the split rests on a stated composition or a stated
estimate.

| Treatment | When it applies | What the workbook holds |
|---|---|---|
| **FULL IDENTITY** — deduct the renewals provision and the overhaul provision | the source states routine upkeep, renewals and major works are all inside the figure | the rail carriage rows, from pass 47 and re-based by pass 62 on [report 51](../cost-balancing/research-pricing-report-51.md): the measured ladder is 33 / 39 / 121 / 265 / 460 / 440 GBP a vehicle-year at 1900 / 1920 / 1950 / 1970 / 1990 / 2020, the envelope; the renewals share is 35 per cent up to 1961 and phased to zero by 1984 (the 1984-2020 anchors exclude the capital lease), and the works overhaul is 28 / 24 / 19 / 12 / 10 / 8 per cent of A by era ([research-pricing-report-44](../cost-balancing/research-pricing-report-44.md)). Head = A − renewals − provision; the events amortise to the provision; head plus provision equals the net total. The locomotives take the same identity from pass 49 (renewals 25 per cent phasing out by 1950; overhaul 35 per cent steam and 39 per cent diesel/electric), with the measured Class 92 override at 868 GBP from pass 63 (a mixed-traffic class on the Caledonian Sleeper), and the narrow gauge from pass 48 |
| **PARTIAL, overhauls** — deduct the overhaul provision only | the source states major repairs are inside and keeps depreciation outside | Commercial Motor road figures: the overhaul deduction is bounded by the measured composition of the total. For buses and coaches the measured share is 37.5 per cent (the 1947 fleet account); a capital-share estimate above that share is rescaled to it, the overhaul targets are rescaled to the same provision, and the routine remainder is the other 62.5 per cent. Where the estimate is at or below 37.5 per cent it is used directly. Lorries take their own measured bands, applied as a floor-and-cap with the interval corrected in the same pass: 35-50 per cent before 1930, 44-56 in 1930-59 (the itemised 1938, 1949 and 1955 costings give 46, 53 and 44 per cent), 25-35 in 1960-84 and 20-30 in 1985-2004 ([research-pricing-report-42](../cost-balancing/research-pricing-report-42.md)). The renewals share is zero; the remainder keeps the generator's 75/25 distance/standing split |
| **ESTIMATED SPLIT** — deduct an estimated overhaul provision | the composition is unrecorded, so no share is measured, but the class still needs both figures | The tram, water, aircraft and multiple-unit rows take the class's own measured or stated overhaul event and make it the provision; the head becomes the residual, and every basis states the estimate and what would replace it. The multiple-unit rows also take research pass 45's rule (15 per cent of A, event 1.2A every eight years). This is the treatment that the standing rule requires where data are thin: a stated estimate that sums to the total, never a blank |
| **NO DECOMPOSITION** — deduct nothing | the figure is standing-only or is an individual unit cost that the source does not describe as a combined total | horse keep and horse-vehicle repairs: whole figure in the fixed column, no per-km figure (standing rule 2 of [maintenance-decomposition](maintenance-decomposition.md)); FTA trailer line: nothing deducted, generator split retained. Both still carry an overhaul target, because the replacement of a horse and the attention a trailer needs are real events |
| **ZERO** — no maintenance and no overhaul | the vehicle is zero-priced in the .dat and the leading unit carries the consist | holds, and the rear, centre and articulated sections of multi-part units. The audit treats a zero target as correct only where the vehicle itself is zero-priced |

The wagons take the era ladder of
[research-pricing-report-43](../cost-balancing/research-pricing-report-43.md) (4.2 / 8.7 / 14.3 /
24.8 / 23.8 GBP per 10-tonne wagon-year, scaled by (payload/10)^0.4), split head = 0.8A and
overhaul event = 1.2A every six years at the 40,000 km/yr reference duty; the source analysis is
[wagon-overhaul-source-analysis](../cost-balancing/wagon-overhaul-source-analysis.md). The
narrow-gauge wagons and carriages take the same rules as their standard-gauge equivalents, and
every narrow-gauge vehicle has an overhaul row.

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
- **A wagon repair contract** with its workscope would settle the composition of the wagon
  ladder.
- **A maglev operator's rolling-stock maintenance line** would replace the overseas unit costs;
  the rule and the current figures are in [maglev-costs](maglev-costs.md).

## Open questions

- Do Hill's repairs contain works overhauls? The passage that would settle it is a company
  repair account (or the post-1911 Abstract B "Repairs and partial renewals" column) itemising a
  heavy general. The carriage rows treat the measured total as the envelope and take the overhaul
  provision out of it, so the charge equals the measured total whether or not Hill itemised the
  overhaul. The locomotive rows deduct renewals only.
- What does the wagon ladder cover? The composition of the wagon figure remains unrecorded. The
  8-20 per cent band in report 36 is a share of *capital per event*, not of the annual total, and
  comes from BR's condemnation rule (replacement logic, not a recurring overhaul). The split is
  head = 0.8A and event = 1.2A every six years at the 40,000 km/yr reference duty, which puts the
  event at 7.1 per cent of a 1900 wagon's capital and 10.1 per cent of a 2020 100-tonne hopper's.
  The 1961 wagon level is £54.3 nominal = **£9.84** in 1900 money at the general index of 552;
  the ratio 5.4 per cent is unaffected because both sides are nominal. A measured wagon overhaul
  invoice or the 1947 BR repair regulation would replace the 0.20 share.
- Is the 2-per-cent ship share the overhaul alone (as report 15's note suggests for 1900-1920)
  or a whole-upkeep figure? The ship rows are therefore written whole.
- What workscope does the Nottingham 2011 tram contract carry? The workbook uses it as the gross
  annual total with zero renewals and a 6 per cent overhaul provision; a workscope would confirm
  the split.
- The tram 1950-90 rung (150 GBP a car-year, band 130-210) is a repairs-only estimate from the
  measured Sheffield 1949-50 figure of 147.3; no municipal repairs figure after 1950 was found.
  The research route is the Ministry "Tramways and trolley vehicle undertakings" volumes and the
  Glasgow, Blackpool and later Sheffield accounts
  ([research-pricing-report-49](../cost-balancing/research-pricing-report-49.md) section 7).
- Does the 37.5-per-cent overhaul share measured on the 1947 coach fleet hold for lorries and
  for the modern bus bands? It does not hold for lorries: the itemised lorry costings give 46,
  53 and 44 per cent (1938, 1949, 1955), because the lorry schedules put chassis and body work
  into the periodic overhaul while the coach account keeps it in routine maintenance. The lorry
  rows therefore use their own bands ([research-pricing-report-42](../cost-balancing/research-pricing-report-42.md)).
  The modern bus bands still use the 37.5 per cent coach bound; a modern bus fleet account with
  both sides would settle whether they should have their own band. Neither the lorry nor the bus
  share rests on an operator account: the lorry compositions are three itemised costings by one
  Commercial Motor costs writer, and the coach figure is one twelve-coach fleet. A BRS,
  Pickfords, Unilever, brewery or municipal account showing the total and the overhaul line for
  the same vehicles would replace the lorry bands.
