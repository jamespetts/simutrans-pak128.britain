---
status: draft
verified: New ex-15 @ fcd40c0bc (working tree)
date: 2026-11-25
---
# Research pass 54 - British Rail wagon repair costs, 1972-1981: the archive route

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-54.csv`. No workbook, `.dat` or
existing document was changed.

This pass continues [report 52](research-pricing-report-52.md). Report 52 established that the
Historical Model Railway Society (HMRS) item *Wagons - annual average repair costs 1972-81*
(catalogue number ME0354) is archive-only, that the British Railways Board (BRB) annual reports
for 1972-77 on HathiTrust are search-only, and that the one readable official aggregate, the
Serpell report of 1983, gives a whole-fleet vehicle maintenance total with no wagon line. It
concluded that no measured per-wagon-year repair cost for 1972-81 is readable. Two quantities were
therefore left as estimates:

- the wagon maintenance **ladder**, the ratio-derived series in
  [report 43](research-pricing-report-43.md) §6, at **14.3** in 1900 money for a 10-tonne wagon in
  1970;
- the overhaul event of **1.2 A** every six years, where **A** is the measured annual maintenance
  total for one wagon-year and a **General Repair** is the periodic works visit at which a wagon is
  dismantled to components.

"1900 money" means a nominal amount multiplied by 100 and divided by the `general` price index for
its year; the index is 100 in 1900. This pass searched beyond the sources report 52 used. It found
no figure, and it located the document that would carry the figure: a public archive holds it,
with a shelfmark, an open access status, and a date range that covers the whole window.

## 1. What this pass found

1. **A wagon-works file titled "Unit cost of repair: wagons" exists at The National Archives
   and covers 1965 to 1981.** Catalogue reference **AN 112/25**, title *Unit cost of repair:
   wagons*, covering dates 1965 May to 1981 December, former departmental reference "4-0-17 part
   1", in series AN 112 *British Rail Engineering Ltd: Correspondence and Papers*, sub-series
   Temple Mills Workshops, correspondence and papers. The catalogue records the closure status
   as open (code O, meaning available to the public) and the record opening date as 4 January
   2005. The record is **not digitised** (`digitised: false`). This is the closest identified
   document to the missing
   measurement: a file kept by a wagon works, whose title is the unit cost of a wagon repair,
   spanning the entire window (1972-1981). **UNAVAILABLE in this pass; readable at Kew.**
   `[LITERATURE: https://discovery.nationalarchives.gov.uk/details/r/C599443]`
2. **The file has a continuation.** **AN 112/26**, same title, 1982 April to 1983 June, former
   reference "4-0-17 part 2", open, not digitised. It covers the two years after the window and
   would show how the unit cost moved at the end of it. **UNAVAILABLE.**
3. **The same series holds the General Repair procedure.** **AN 112/87**, *Workshops Overhaul
   Procedure: Wagons, G.R. Plate and Intermediate Repairs*, 1966 June. The title establishes
   that British Rail had a formal works procedure for the **General Repair (GR)** and a separate
   class of **intermediate repair**, and that the GR was identified on the wagon by a plate. It
   is a procedure document, not a price, and it was not read in this pass: only its catalogue
   title was seen. **STATED (title only); UNAVAILABLE for a cost.**
4. **British Rail Engineering Limited (BREL) accounts for 1974 are in the same series.**
   **AN 112/129**, *B.R.E.L. Annual Report and Accounts 1974*, 1974. If those accounts split
   repair turnover by vehicle type, the file is a primary account inside the window. The
   catalogue entry was seen in a series listing; its closure status and contents were not
   checked. **UNAVAILABLE.**
5. **A second BRB file concerns wagon repair activity in the window.** **AN 171/941**,
   *British Railways workshops: repair and production policy; wagon repair activities*, 1971
   April to 1982 July, in the records of the British Transport Commission and British Railways
   Board, Industrial Relations and Employee Relations Departments. It is open (code O, closure
   type U, 2005). It is a policy and industrial-relations file, so it may state repair volumes
   and targets rather than costs, but it is the only BRB-level file found with "wagon repair"
   in the title across the window. **UNAVAILABLE.**
6. **The HMRS series is confirmed unchanged and remains the only per-wagon-year series
   identified.** The catalogue page for ME0354 prints the title *Wagons - annual average repair
   costs 1972-81*, archive series Mechanical Engineering, archive section Railway Engineering
   Collection, date 1972-01-01, availability "for request", and no figure, page count or
   description. The companion items *Wagon repairs - cost limits 1977-79* (ME0350) and *Wagon
   repairs - cost limits 1980-83* (ME0349) are in the same state. **UNAVAILABLE.**
7. **No additional digitised copy of the BRB annual reports was found.** A search of the
   Internet Archive metadata index for the BRB's annual report and accounts returned no copy;
   the only two items with the BRB as a subject are unrelated. The HathiTrust catalogue returned
   a Cloudflare challenge in this pass, so the search-only status recorded in report 52 could not
   be re-tested and no second HathiTrust copy could be identified. The Google Books volume API
   returned HTTP 429 (daily quota exhausted) for every query, so no Google Books copy was searched
   either. **UNAVAILABLE.**
8. **The trade press is digitised but not readable.** The Internet Archive holds lending copies
   of *Modern Railways* from the 1970s and early 1980s (for example item `modernrailways33unse_3`,
   1976). Their full text is indexed and returns snippets, but the copies cannot be displayed
   without borrowing. Snippets for "wagon repairs", "wagon maintenance", "repair costs" and "per
   wagon" in those volumes show depot openings and closures, the Private Wagon Federation
   exhibition, and statements that wagon maintenance is "largely a time cost"; none shows a cost
   per wagon or per repair. This is a search-index result, not a reading of the pages.
   **UNAVAILABLE.**
9. **The Institution of Mechanical Engineers' 1981 freight conference is digitised, lending
   only, and carries no wagon cost figure in its searchable text.** *Rail freight: a
   contribution to the conservation of energy*, sponsored by the Railway Division of the
   Institution of Mechanical Engineers and the Private Wagon Federation, London, 5 March 1981
   (ISBN 0 85298 472 3), is Internet Archive item `isbn_0852984723`. Snippets mention that "the
   wagon repair industry has been concerned about the reduction" in work and carry a Wagon
   Repairs Limited advertisement, but no per-wagon or per-repair cost appears in the indexed
   text. A page-by-page reading needs a borrow. **UNAVAILABLE.**
10. **The academic thesis on a wagon works that was read contains no wagon repair cost.**
    *The jewel in British Rail's crown: an account of the closure at Shildon Wagon Works*
    (Durham e-theses, 1990, https://etheses.durham.ac.uk/id/eprint/6230) is an industrial and
    political history of the works. Its treatment of the closure quotes the Serpell report's
    £220m and £45m cost-saving totals; a text search for monetary figures attached to wagon
    repair found none. **UNAVAILABLE.**
11. **The 1981 electrification review excludes wagon costs by design.** *Review of Main Line
    Electrification: Final Report* (Department of Transport and British Railways Board, 1981,
    Her Majesty's Stationery Office, 1978 price levels) states that costs "excluded from the
    appraisal because they were assumed not to be significantly affected by electrification
    included general track costs; signalling and administration and the costs of freight and
    parcels wagons". The document therefore cannot bound A, and its exclusion confirms that
    wagon maintenance sat outside the BRB's project appraisals as well as outside its
    published maintenance aggregates. **STATED (negative).**
    `[LITERATURE: https://www.railwaysarchive.co.uk/documents/DoTBRB_Electrification1981.pdf, para 34]`
12. **A second official aggregate for BREL's repair business exists, with no wagon split.**
    In the Commons debate of 22 March 1983 a speaker, quoting James Urquhart's supplement to
    chapter 7 of the Serpell report, stated: "Of BREL's turnover of £600 million, about 60 per
    cent. goes to the maintenance of the existing British Rail fleet". That implies about
    **£360m** a year of BREL maintenance turnover for all vehicle types. The Serpell main report
    gives £266m of BREL maintenance and repair expenditure (report 52, row 9); the two figures
    measure turnover and expenditure respectively and are not additive or directly comparable.
    Neither has a wagon line. **STATED; the £360m is DERIVED from the stated turnover and
    share.** `[LITERATURE: https://hansard.parliament.uk/commons/1983-03-22/debates/d59fe008-4e86-433c-9c56-941721175e27/RailwayWorkshops]`
13. **A pre-window wagon-specific fleet total exists in a book that could not be opened, and was
    seen only as a search snippet.** *British Railways after Beeching* (1965) states that "for
    1963, wagon repair costs were down to £23m, compared with £30.3m" in 1962. The copy is a
    lending item (`britishrailwaysa0000gfre`) and the page could not be displayed. The wording
    is wagon-specific, but the containing sentence, the account from which the figure comes and
    the fleet denominator were not read. **STATED (snippet only); a lead, not evidence, and not
    used in this pass's arithmetic.** If verified it would be the only wagon-specific fleet
    total between 1961 and 1981, and it would give a repairs-only cross-check on the 1961
    Beeching line, which includes capital provision.
14. **Result: no measured per-wagon-year repair cost and no measured General Repair price for
    1972-81 is readable.** The ladder's 1970 level of 14.3 and the 1.2 A event are unchanged by
    this pass and remain estimates. What has changed is that the gap is no longer an open search
    problem: the quantity sought is named in a public catalogue, in an open file, with a date
    range that covers the window, at one named repository.

## 2. Method

- **Deflator.** Every nominal figure is converted with the `general` series in
  `New/config/prices.tab` (1900 = 100), because `prices.tab` states "Vehicle maintenance stays
  on the general index" and no separate maintenance or repair price index exists before 1987.
  The index values used or quoted in this pass: 1961 **552**; 1963 **587**; 1970 **795**;
  1972 **932**; 1973 **1,016**; 1974 **1,179**; 1975 **1,465**; 1976 **1,708**; 1977 **1,978**;
  1978 **2,142**; 1979 **2,429**; 1980 **2,866**; 1981 **3,207**; 1982 **3,483**. "**1900
  money**" means nominal × 100 ÷ the index for the year named. A **nominal** figure is a price as
  stated in the money of its own year. Only 1961 (quoted from report 52), 1963 (the §4.1 check)
  and 1970 (the §4.3 check) enter arithmetic; 1982 is quoted because the Serpell total is stated
  at 1982 prices, and the remaining years are listed so that a later pass can use the same values
  without recomputing them. `[CODE New ex-15 @ fcd40c0bc: config/prices.tab]`
- **Grades.** MEASURED = an account, return or contract with a stated scope. STATED = a trade,
  academic or official statement of a rate or practice without the underlying account. DERIVED
  = arithmetic here from a measured or stated figure, with the chain shown. ESTIMATE = judgement,
  marked wherever it is used. UNAVAILABLE = identified but not readable. Definitions:
  [claim tags](../claim-tags.md).
- **A.** The symbol **A** means the measured annual maintenance total for one wagon-year, from a
  source that states what the total contains. It is the envelope in standing rule 0 of
  [maintenance decomposition](../vehicle-cost/maintenance-decomposition.md): the continuous
  **head** plus the amortised overhaul events equals A. The **head** is the part of A charged
  continuously for running and intermediate repairs; the **envelope** is the rule that the annual
  figure covers both the head and the amortised works events, so the two parts sum to A and are
  not added to A.
- **Ladder.** The wagon maintenance series in [report 43](research-pricing-report-43.md) §6,
  built from the ratio of wagon to carriage maintenance and extended to 1970, 1990 and 2020. It
  is an ESTIMATE at every point; its 1970 value for a 10-tonne wagon is 14.3 in 1900 money.
- **s, n and the event multiple.** **s** is the overhaul share of A, that is the fraction of the
  annual total that is the amortised works event; **n** is the interval between works events in
  years; the **event multiple** is s × n, the size of one works event expressed in years of A.
  Only the product s × n is constrained by the evidence.
- **Reference duty.** The distance a wagon is assumed to run in a year. The modelled duty is
  40,000 km a wagon-year, so the modelled distance between overhauls of 240,000 km is six years.
- **Open and not digitised.** An **open** record is one The National Archives will serve to the
  public without a closure exemption. **Not digitised** means no page images exist online, so the
  record must be read at Kew or copied by the record copying service. **TNA** abbreviates The
  National Archives, and **Discovery** is its online catalogue.
- **GR (General Repair).** The periodic works visit at which a wagon is dismantled to individual
  components, the components are repaired, refurbished or replaced, and the wagon is reassembled.
  The definition is the Rail Accident Investigation Branch's description of HAA wagon practice
  before 1992 (HAA is the air-braked merry-go-round coal hopper), quoted in report 52 row 14; the
  two words are capitalised here because the archive file in row 3 of the table uses "G.R." as the
  name of a defined procedure.
- **Intermediate repair.** The lesser scheduled repair class named alongside the GR in the title
  of AN 112/87. The catalogue does not define its content, so this report uses the term only as
  the name of a class that existed, not as a defined scope.
- **Unit cost of repair.** The phrase in the title of AN 112/25 and AN 112/26. A unit cost is a
  total cost divided by a count of units. The catalogue does not say whether the unit is one
  wagon, one repair event or one standard hour, nor whether the cost is a works cost or a charge
  to the customer. That ambiguity is the reason the file must be read before the figure is used.
- **Works cost and fleet-average charge.** A **works cost** is what one workshop spent on one
  repair. A **fleet-average charge** is the total spent on a class of vehicle in a year divided
  by the number of vehicles in stock. Report 52's A is a fleet average; a works unit cost is not,
  and the difference matters because a works unit cost excludes depot running repairs and
  overheads carried elsewhere.
- **Searching versus reading.** Pages that were read in full are cited by page or paragraph.
  Pages returned only as search snippets are marked as such and are not used as evidence. This
  distinction is stated in the table for every row.
- **No `.dat` value, workbook figure or pakset price is used as evidence anywhere in this pass.**
  The 1970 new-wagon price of £3,639 in §4 is report 52's derived average of a stated government
  programme, repeated only as the denominator of the percentage check.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1965-1981 | The National Archives, AN 112/25, *Unit cost of repair: wagons* | title only; no figure in the catalogue | a wagon works file; unit cost of a wagon repair; composition not stated | not stated | UNAVAILABLE | TNA Discovery, AN 112/25, https://discovery.nationalarchives.gov.uk/details/r/C599443 |
| 2 | 1982-1983 | The National Archives, AN 112/26, *Unit cost of repair: wagons* | title only | continuation of row 1 | not stated | UNAVAILABLE | TNA Discovery, AN 112/26 |
| 3 | 1966 | The National Archives, AN 112/87, *Workshops Overhaul Procedure: Wagons, G.R. Plate and Intermediate Repairs* | title only | procedure for the GR and the intermediate repair; not a price | n/a | STATED (title only); UNAVAILABLE (cost) | TNA Discovery, AN 112/87, series AN 112 |
| 4 | 1974 | The National Archives, AN 112/129, *B.R.E.L. Annual Report and Accounts 1974* | title only; closure status and contents not checked | BREL accounts; wagon split unknown | n/a | UNAVAILABLE | TNA Discovery, AN 112/129, series AN 112 |
| 5 | 1971-1982 | The National Archives, AN 171/941, *British Railways workshops: repair and production policy; wagon repair activities* | title only | BRB policy and industrial relations; wagon repair activity | n/a | UNAVAILABLE | TNA Discovery, AN 171/941 |
| 6 | 1972-1981 | HMRS, *Wagons - annual average repair costs 1972-81* | title only; "for request" | annual average repair costs; composition not stated | per wagon-year (inferred from the title) | UNAVAILABLE | SKU ME0354, https://hmrs.org.uk/archives/wagons---annual-average-repair-costs-1972-81.html |
| 7 | 1977-1979 | HMRS, *Wagon repairs - cost limits 1977-79* | title only; "for request" | cost limits per repair | per repair | UNAVAILABLE | SKU ME0350 |
| 8 | 1980-1983 | HMRS, *Wagon repairs - cost limits 1980-83* | title only; "for request" | cost limits per repair | per repair | UNAVAILABLE | SKU ME0349 |
| 9 | 1981 | Department of Transport and BRB, *Review of Main Line Electrification: Final Report* | wagon costs "excluded from the appraisal" | freight and parcels wagons; excluded, not measured | n/a | STATED (negative) | para 34, https://www.railwaysarchive.co.uk/documents/DoTBRB_Electrification1981.pdf |
| 10 | 1982-1983 | Hansard, BREL turnover and maintenance share | "turnover of £600 million, about 60 per cent ... maintenance of the existing British Rail fleet" = about £360m | BREL turnover; all vehicle types; no wagon split | whole fleet | STATED; £360m DERIVED | HC Deb 22 March 1983 vol 39 cc726-72, https://hansard.parliament.uk/commons/1983-03-22/debates/d59fe008-4e86-433c-9c56-941721175e27/RailwayWorkshops |
| 11 | 1981 | Serpell, total vehicle maintenance | "£473 million (1982 prices)" | all vehicle types; capital out | whole fleet | MEASURED aggregate (repeated from report 52) | *Railway Finances* (1983), para 6.44 |
| 12 | 1981 | Serpell, records | "maintenance records are not kept for individual vehicles" | the reason no per-vehicle series was published | n/a | STATED (repeated from report 52) | as row 11, para 6.45 |
| 13 | pre-1992 | RAIB, HAA General Repairs | "General Repairs ... on a seven-yearly cycle ... dismantled to individual components" | HAA and similar hoppers; full strip | per wagon per event | STATED (repeated from report 52) | RAIB report 02/2008, p. 21, paras 87-88 |
| 14 | 1963 | *British Railways after Beeching* (1965), wagon repair costs | "wagon repair costs were down to £23m, compared with £30.3m" in 1962 | wagons; the containing sentence and the account were not read | fleet total; denominator not read | STATED (search snippet only; page not read) | Internet Archive item `britishrailwaysa0000gfre` |

Rows 1-5 are archive references, not measurements: they are the output of this pass and the
input to the next. Rows 11-13 repeat figures already in report 52 so that the series in §4 can be
read without switching documents; they are not new findings. Row 14 is graded STATED on a search
snippet only and is marked so that no later pass mistakes it for a reading of the page.

## 4. The series

### 4.1 The points that exist

| Date | Nominal | 1900 money | Grade | Basis |
|---|---|---|---|---|
| 1892 | £4 4s. a wagon-year | 4.33 | MEASURED | Hill, 19 companies, repairs and renewals, renewals inside (report 52 §4.1) |
| 1961 | £54.3 a wagon-year | 9.84 | MEASURED inputs, DERIVED | Beeching, functional line including provision, 848,591 wagons |
| 1970 | not measured | 14.3 (ESTIMATE) | ESTIMATE | ratio-derived ladder, 10-tonne wagon, [report 43](research-pricing-report-43.md) §6 |
| 1972-81 | not readable | - | UNAVAILABLE | HMRS ME0354; TNA AN 112/25 |
| 1981 | not measured | - | UNAVAILABLE | Serpell gives a whole-fleet total with no wagon split |

This pass adds **no point** to the series. The 1963 lead in row 14 is the only candidate it
found, and it is unread. For scale only: if the snippet is accurate and the 1963 wagon fleet was
400,000 (the level the whole wagon fleet reached by December 1971, when a speaker in the Commons
put it at "nearer 400,000", so the 1963 fleet was larger), £23m is at most £57.5 a wagon-year
nominal, or **£9.8 in 1900 money** at the index 587; at 500,000 wagons it is £46 nominal, or £7.8.
Neither number is a measurement: the page was not read and the denominator is not verified. The
arithmetic is given so that a later pass can judge whether the book is worth ordering.
`[LITERATURE: HC Deb 2 December 1971 vol 827 cc769-96]`

### 4.2 What the archive file would and would not settle

AN 112/25 is a Temple Mills Workshops file. Temple Mills was one of the principal wagon works, so
its unit costs are **works costs for one works**, not a fleet average. Read on its own it would:

- give a measured price for a wagon repair at one works, year by year from 1965 to 1981, which is
  the quantity the 1.2 A event needs;
- bound the event multiple from below: a Temple Mills repair cost is a works cost, so it excludes
  depot work and overhead carried elsewhere, and the full cost of a GR is at least that much. For
  a comparable wagon, a works cost above 1.2 A would therefore show the multiple is too low; a
  works cost below 1.2 A would be inconclusive until the scopes of the two figures are matched;
- not give A, because A is a fleet average that includes depot running repairs, which a works file
  does not carry.

ME0354, by contrast, is titled as an annual average repair cost and would give A, but not a price
per event. The two documents answer different halves of the question, so this pass lists both as
routes, each for the half it answers.

### 4.3 The event against a new wagon

The check in report 52 §4.3 is unchanged by this pass, because neither of its two inputs changed:
the measured 1970 new-wagon price is £3,639 nominal = £457.7 in 1900 money at the index 795, and
the ladder's value for A at 1970 is 14.3. The 1.2 A event is £17.16 in 1900 money, **3.8 per
cent** of the new-wagon price. The band in
[wagon-overhaul-source-analysis](wagon-overhaul-source-analysis.md) §4 of 7-15 per cent of a new
wagon is a 1900-era relationship and is not met at 1970 on these inputs; report 52 explains why,
and this pass has no new price with which to test the explanation.

## 5. Recommended treatment for the wagon overhaul event

**Keep the A-based envelope and change neither 14.3 nor 1.2 A on the evidence of this pass.** The
parameters are a continuous head of 0.8 A, a first event of 0.9 A, a maximum event of 1.2 A, and
an interval of 240,000 km (six years at the 40,000 km a year reference duty). The reasons:

1. **No measurement was obtained, so no number may move.** The ladder's 14.3 is an ESTIMATE built
   from the falling wagon-to-carriage ratio; the 1.2 A event is an ESTIMATE built from the
   overhaul share s = 0.20 and the six-year interval. A pass that finds no measurement cannot
   improve either, and changing them on the strength of an archive catalogue entry would replace
   one estimate with another while making the second look measured.
2. **The archive finding supports the structure, not the magnitude.** AN 112/87's title records a
   formal General Repair procedure and a separate intermediate repair class. That is documentary
   support for the model's two-part structure - a continuous head that carries running and
   intermediate repairs, and a discrete works event that carries the GR - and it is an archival
   attestation of the split independent of the workshop testimony recorded in the
   [wagon overhaul source analysis](wagon-overhaul-source-analysis.md). It leaves the magnitude of
   both parts open.
3. **The interval of six years still sits inside the documented band.** The one documented BR
   cycle is seven years for HAA and similar wagons (RAIB report 02/2008, citing BR Engineering
   Instruction WF/81 of 1980). Six years at the 40,000 km a year reference duty is the modelled
   interval, and six is the midpoint of the 5-7 year band assembled in the source analysis. This
   pass found no second interval.
4. **The event multiple remains an estimate with a known direction of error.** The GR was a full
   strip, and most HAA wagons received a new body during it. A full strip is a large event, so a
   multiple above 1.0 A is more plausible than one below it. Whether the body was charged to
   capital or to maintenance is not stated in any readable source; report 52's treatment, that
   the body belongs to the vehicle's purchase cost and not to the overhaul, is retained.
5. **The acquisition order.** AN 112/25 first, because it is open, dated across the whole window,
   and at a repository that supplies copies; ME0354 second, because it needs an appointment and a
   fee quotation. The exact route to each is in §7. The question to put to each is different:
   to Kew, "what was the unit cost of a wagon repair at Temple Mills in 1972, 1975, 1978 and
   1981, and what did the unit include?"; to the HMRS, "what is the extent of ME0354, is it annual
   by wagon type, and what did the average include?".
6. **Basis string for `WAGON_OVERHAUL`.** If the basis text is revised, it should say: "head 0.8 A
   plus 1.2 A every 240,000 km (6 years at 40,000 km a year); the first event is 0.9 A, three
   quarters of the steady event; A and the event multiple are ESTIMATES per research pass 52 and
   pass 54; the interval is STATED for HAA wagons at 7 years, RAIB 02/2008." No change to the
   fields themselves is proposed.

## 6. Error bars

Nothing in this pass narrows a numeric band. The bands below are report 52's, restated so that
this report can be read alone, with a note on whether this pass touched each.

| Quantity | Central | Band | Why | Changed by this pass? |
|---|---|---|---|---|
| A, 1972-81, 10-tonne wagon (1900 money) | not measured | 9.8-27 | 1961 measured 9.84; the ladder's 1970 value 14.3; a capital-proportional 1970 value would be about 27 | No |
| Interval between General Repairs | 6 years | 5-7 | contract terms of 5 and 7 years; the HAA GR documented at 7 years | No |
| Event share of A, s | 0.20 | 0.10-0.30 | no measurement; the source analysis's range | No |
| Event as a multiple of A, s × n | 1.2 | 0.5-2.1 | product of the two rows above | No |
| Event as % of a 1970 new wagon | 3.8% | 1.1-12% | product of the multiple band and the A band, against the measured £458 | No |
| Real trend of A, 1977-81 | rising | +10 to +30% | ESTIMATE, guided by Serpell's 30 per cent for "some vehicle types"; wagons not named | No |

**Structural assumptions.** (i) A is a fleet average, so it mixes 16-ton minerals with air-braked
hoppers; the ladder's size term is the only adjustment. (ii) The 1970 wagon price is an average
over a mixed programme including high-capacity air-braked stock, so it sits above a 16-ton mineral
wagon's price and the percentages against it are correspondingly low. (iii) The RAIB description
is of HAA and similar wagons, the newest and heaviest class; older vacuum-braked wagons may have
had a different cycle and a smaller event. (iv) AN 112/25 is a works file, so even when read it
will bound the event price from the works side and will not give a fleet average.

## 7. Gaps and routes

In order of value, with the exact route to each. A route is the access path to a document, not a
claim that the document contains a figure.

1. **The National Archives, AN 112/25, *Unit cost of repair: wagons*, 1965 May - 1981 Dec.** Route:
   order a copy through The National Archives' record copying service, quoting the reference
   AN 112/25 and the catalogue identifier C599443, or consult the original at Kew. The record is
   open and not digitised. Ask for the leaves covering 1972, 1975, 1978 and 1981 first, and ask
   what the unit and the cost include. This is the most direct document identified in this pass.
   **UNAVAILABLE.**
2. **HMRS ME0354, *Wagons - annual average repair costs 1972-81*.** Route: the "Contact Archivist
   for Information" form on the catalogue page, or the contact page at
   https://hmrs.org.uk/contacts, quoting SKU ME0354. Ask for the extent first, then a quotation
   for the pages covering 1972, 1975, 1978 and 1981. **UNAVAILABLE.**
3. **The National Archives, AN 112/26, *Unit cost of repair: wagons*, 1982 Apr - 1983 Jun.** Same
   route as item 1. It extends the series past the window and would show the direction of the
   unit cost at the end of it. **UNAVAILABLE.**
4. **The National Archives, AN 112/129, *B.R.E.L. Annual Report and Accounts 1974*.** Same route.
   BREL's own accounts may split repair turnover by vehicle type, which would give a wagon total
   for one year inside the window. **UNAVAILABLE.**
5. **The National Archives, AN 112/87, *Workshops Overhaul Procedure: Wagons, G.R. Plate and
   Intermediate Repairs*, 1966 June.** Same route. It would define what a GR contained and what an
   intermediate repair contained, which is the scope question behind the 0.8 A head and the 1.2 A
   event. It is a procedure, so it is unlikely to price either. **UNAVAILABLE.**
6. **HMRS ME0350 and ME0349, the repair cost limits for 1977-79 and 1980-83.** Same route as item
   2, quoting both SKUs. A repair assessed at or above the limit was not carried out, so the limits
   bound the GR price from above. **UNAVAILABLE.**
7. **The National Archives, AN 171/941, *British Railways workshops: repair and production policy;
   wagon repair activities*, 1971 Apr - 1982 Jul.** Same route. A BRB policy file may give repair
   volumes, targets and unit costs for the window even though its title is about policy.
   **UNAVAILABLE.**
8. **BRB Annual Report and Accounts, 1972-1981.** Route: the printed volumes at the British
   Library or the National Railway Museum library. HathiTrust item `mdp.39015024382049` covers
   1972-77 but is search-only, and its catalogue was blocked in this pass. The published account
   line is a single "maintenance of rolling stock" total (Beeching p. 6, £122.2m for 1961), so the
   reports cannot give a per-wagon figure; their value is the wagon count in the statistical
   appendix, which would supply a denominator. **UNAVAILABLE.**
9. **The National Railway Museum library catalogue.** Route: the Science Museum Group collections
   site, which the museum's research pages direct readers to
   (https://www.railwaymuseum.org.uk/research-and-archive/further-resources/catalogues). The site
   returned HTTP 403 from its content delivery network in this pass, so no search was completed.
   **UNAVAILABLE.**
10. **The trade press.** *Modern Railways* from the 1970s and early 1980s is on the Internet
    Archive as lending copies (for example `modernrailways33unse_3`); borrow and read the freight
    and workshop articles. No digitised *Railway Gazette* issue for 1972-81 was found; the
    Internet Archive's sampled holdings are 1930s to 1960s. The Railway Citation Index has no cost
    entry: a search for "wagon repair" returns 13 items, all depot, place or company citations, and
    "wagon maintenance" returns 38, mostly modern maintenance-depot items. **UNAVAILABLE.**
11. **BR Research IM-TAG-005 (1977), *A method for evaluating the direct operating costs incurred
    by the acquisition, maintenance and movement of a fleet of vehicles*.** Route: free
    registration at RSSB SPARK, then the item at
    https://www.rssb.co.uk/spark/sparkitem/pb008307. The public abstract is readable; the report is
    behind the login. **UNAVAILABLE.**
12. **The 1963 wagon repair total in *British Railways after Beeching* (1965).** Route: borrow
    Internet Archive item `britishrailwaysa0000gfre` and read the page containing "wagon repair
    costs were down to £23m". If the figure is wagon-specific, it is a repairs-only fleet total for
    1963 and a cross-check on the 1961 Beeching line, which includes capital provision.
    **UNAVAILABLE in this pass (lending copy).**
13. **Parliamentary papers.** The Historic Hansard search endpoint is backed by a Google custom
    search and returned a Google block page in this pass, so the 1972-81 written answers could not
    be searched by keyword. The printed Hansard indexes at the British Library are the route. The
    only 1970s answers located by other means concern workshop closures, not per-wagon costs.
    **UNAVAILABLE.**
14. **Institution of Railway Signal Engineers papers.** The institution's subject is signalling, so
    its papers are not expected to price wagon repairs; none was searched. **NOT APPLICABLE.**
15. **The Office of Rail and Road.** The regulator's public output belongs to the privatised
    railway that followed British Rail, so it cannot hold a 1972-81 cost series; the BRB's own
    records are at The National Archives in the AN series listed above. No ORR publication was
    used. **NOT APPLICABLE.**

**What a positive result would change.** Reading AN 112/25 would give a measured works price for a
wagon repair at one works across the window. A works price above 1.2 A would show the event
multiple is too low. A works price below 1.2 A would not by itself show it is too high, because the
works cost excludes depot work that A contains; the scopes would have to be matched first. Reading
ME0354 would replace the ladder's value for A with a measured fleet average, which changes the
money amount of both the head and the event but not the multiple. Until one of the two is read,
14.3 and 1.2 A are the best available estimates, and this pass recommends leaving them unchanged.
