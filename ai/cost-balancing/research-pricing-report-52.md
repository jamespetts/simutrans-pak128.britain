---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 52 - British Rail wagon repair costs, 1972-1981

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-52.csv`. No workbook, `.dat` or
existing document was changed.

This pass looks for the one thing the wagon costing still lacks: a measured cost of
repairing or overhauling a British Rail wagon between 1972 and 1981. It was asked to
prioritise the Historical Model Railway Society (HMRS) material, British Railways Board
(BRB) accounts and returns, the trade press, and academic work, and to record a negative
result precisely if the figures cannot be read. The wagon overhaul event currently in the
workbook is an estimate of **1.2 A every six years**, where **A** is the measured annual
maintenance total for a wagon-year, so the pass also tests that rule against what it found.
[report 46](research-pricing-report-46.md), [wagon overhaul source analysis](wagon-overhaul-source-analysis.md).

## 1. What this pass found

1. **The HMRS document exists and is archive-only.** The catalogue entry is *Wagons -
   annual average repair costs 1972-81*, catalogue number (SKU) **ME0354**, archive series
   Mechanical Engineering, archive section Railway Engineering Collection, catalogue date
   1972-01-01, availability "for request". The online entry prints the title and nothing
   else: no figures, no page count, no description of contents. It is not digitised and
   cannot be read from the web. **UNAVAILABLE.**
2. **Three companion HMRS items carry the repair cost limits.** *Wagon repairs - cost
   limits 1977-79* (SKU **ME0350**), *Wagon repairs - cost limits 1980-83* (SKU **ME0349**)
   and *Wagon repair and maintenance 1980-1981* (SKU **ME0463**) are in the same series and
   are likewise "for request" with no figures online. These are the documents that would
   state BR's cash limit per repair: the mechanism that the 8-20 per cent rule in
   [report 36](research-pricing-report-36.md) mistook for an overhaul share.
   **UNAVAILABLE.**
3. **No HMRS Journal article carries the series.** A text search of the digitised combined
   index to volumes 1-21 of the *HMRS Journal* found no entry under "repair costs",
   "maintenance cost", "average repair" or "wagon repair" for 1972-81. The nearest entry is
   Keith Turton, "Wagon Repair Cards", volume 20 number 10 (April-June 2014), pages
   332-335, which is about the repair card itself, not a cost series. The Journal is
   members-only and the index optical-character text is imperfect, so this is a negative
   search result rather than a proof of absence. **UNAVAILABLE (Journal).**
4. **The BRB annual reports for 1972-77 survive in one digitised copy and it is not
   readable.** HathiTrust holds volumes 10-15 (1972-1977) as item `mdp.39015024382049`,
   rights code "Limited (search-only)"; the full-text search endpoint returns HTTP 403 and
   no page can be displayed. No other digitised run was found. **UNAVAILABLE.**
5. **The one readable official aggregate gives no wagon split.** The Serpell report
   (*Railway Finances*, 1983, reporting 1981 out-turn at 1982 prices) gives total vehicle
   maintenance of **£473m**, of which British Rail Engineering Limited (BREL) carried out
   **£266m**, 55 per cent. It records 38 wagon maintenance depots, a real rise in depot
   maintenance costs of about 30 per cent for some vehicle types between 1977 and 1981, and
   - the reason this pass found no published per-wagon series - that **"maintenance records
   are not kept for individual vehicles"**. **MEASURED (aggregate); no wagon line.**
6. **The only documented BR wagon repair interval is seven years.** The Rail Accident
   Investigation Branch (RAIB) records that, before 1992, HAA and similar wagons (HAA is
   the air-braked merry-go-round coal hopper) "were subjected to General Repairs (GR) at
   wagon workshops on a seven-yearly cycle. During this work, wagons were normally
   dismantled to individual components, which were repaired, refurbished or replaced as
   appropriate and wagons reassembled. The majority of HAA wagons received new bodies as
   part of these works." The passage cites BR Engineering Instruction WF/81 of 1980.
   **STATED (official, resting on a BR instruction of 1980).**
   This is the strongest evidence in the pass for the interval and for the scope of the
   event: six years sits inside the 5-7 year band, and the event is a full strip, not a
   running repair.
7. **A measured 1970 new-wagon price exists.** On 28 April 1970 the Ministry of Transport
   stated that the Railways Board would spend **£5.2 million on 1,429 new wagons** in 1970,
   an average of **£3,639 a wagon = £458 in 1900 money** at the general index 795. That is a
   measured wagon capital figure for a year for which the knowledge base had none: the
   nearest earlier measured price is the 1923-24 Gloucester Gas order for a 12-ton
   private-owner wagon, and the 1963 Liner Train £3,000 is a design case, not a fleet
   average. It lets the overhaul event be expressed against capital for the 1970s.
   **DERIVED from a stated programme.** The same answer gives £10.7 million on 427
   carriages, an average of £25,059 a carriage = £3,152 in 1900 money.
8. **The 1.2 A rule is denominator-free, and that is its strength.** At 1900 the event
   (1.2 × £4.2 = £5.04) is 4.5 per cent of a railway-built 10/12-ton wagon (£111 in 1900
   money, 1883) and 7.8 per cent of a mass-produced private-owner 7-plank (£64.7, c1906).
   At 1970, on the modelled A of £14.3, it is **3.8 per cent** of the measured £458 wagon.
   The "7-15 per cent of new" band in
   [wagon-overhaul-source-analysis](wagon-overhaul-source-analysis.md) §4 is therefore a
   1900-era statement: it is met only at the private-owner end in 1900 and not at all in
   1970, because the new-wagon price rose faster than the wagon's maintenance cost. A rule
   written as a multiple of A does not drift that way. **DERIVED.**
9. **The HMRS series would calibrate A, not the event multiple.** Its title is "annual
   average repair costs", so it measures a per-wagon-year cost, and probably a fleet
   average. It would settle the level of A in the window and would not by itself separate
   running repairs from general repairs. The event share stays an estimate even after the
   document is read. **ESTIMATE (scope inference).**
10. **Result: no measured wagon repair cost per wagon-year for 1972-81 is readable.** The
    level for the window rests on the 1961 Beeching figure (£54.3 a wagon-year) and on the
    ratio-derived ladder in [report 43](research-pricing-report-43.md), not on a
    measurement. The overhaul event remains an estimate. **UNAVAILABLE.**

## 2. Method

- **Deflator.** Every nominal figure is converted with the `general` series in
  `New/config/prices.tab` (1900 = 100): 1961 552; 1969 747; 1970 795; 1972 932; 1973 1,016;
  1974 1,179; 1975 1,465; 1976 1,708; 1977 1,978; 1978 2,142; 1979 2,429; 1980 2,866;
  1981 3,207; 1982 3,483. "**1900 money**" below means nominal × 100 ÷ the index for the
  year named. `prices.tab` states that vehicle maintenance stays on the general index, so
  this is the engine's own treatment and not a new choice.
  `[CODE New @ 70a098c64: config/prices.tab]`
- **Grades.** MEASURED = an account, return or contract with a stated scope. STATED = a
  trade, academic or official statement of a rate or practice without the underlying
  account. DERIVED = arithmetic here from a measured or stated figure, with the chain
  shown. ESTIMATE = judgement, marked wherever it is used. UNAVAILABLE = identified but not
  readable. Definitions and tags: [claim tags](../claim-tags.md).
- **A.** The symbol **A** means the measured annual maintenance total for one wagon-year,
  from a source that states what the total contains. It is the envelope in standing rule 0
  of [maintenance decomposition](../vehicle-cost/maintenance-decomposition.md): the
  continuous head plus the amortised overhaul events must equal A, not A plus an event.
  Two derived quantities are used in §5 and §6: **s**, the overhaul share of A (the share of
  the annual total that is the amortised works event), and **n**, the interval between works
  events in years. Only their product is constrained by the evidence.
- **Provision.** In the Beeching functional line quoted in row 1 of the table, "provision"
  is the capital charge carried inside the costing, not a repair cost; the same report
  prices "provision of wagon" as a separate element in its coal costing, as
  [wagon overhaul source analysis](wagon-overhaul-source-analysis.md) §2(iv) records. It is
  therefore part of the wagon line but is not maintenance, which is why the 1961 figure is
  an upper bound on A. Earlier passes also used "provision" for the annualised overhaul
  charge (the event divided by the interval); this report calls that the **annualised
  overhaul charge** throughout, to keep the two senses apart.
- **The 1.2 A rule.** The workbook's wagon overhaul event is 1.2 × A every six years, with
  a continuous head of 0.8 A. The annualised overhaul charge is therefore 1.2 ÷ 6 = 0.20 A
  a year, and head plus that charge equals A. In `New/ai/cost-balancing/evidence_data.py`
  the parameters are `WAGON_OVERHAUL = dict(provision=0.20, years=6.0, km=240000.0,
  first_ratio=0.75)`, and `wagon_overhaul()` returns a first event of 0.75 × 1.2 A = 0.9 A
  and a maximum of 1.2 A. `[CODE New @ 70a098c64: evidence_data.py]`
- **The event types, distinguished.**
  - **Running repair**: day-to-day and intermediate work at a depot, with no general strip.
  - **Periodic overhaul (POH)**: the generic term used in earlier passes and in the Indian
    Railways wagon manual for a scheduled works visit. The British documents in this pass
    use **General Repair (GR)** for the same event; the two terms are kept distinct here
    because the sources do.
  - **Heavy general repair**: for a locomotive, a works visit at which the boiler is lifted;
    for a wagon, the equivalent is the GR at which the vehicle is dismantled to components
    (definition from the RAIB passage, row 14 of the table).
  - **Condemnation**: the administrative decision not to repair, after which the wagon is
    withdrawn. It is a capital decision and never a maintenance charge; the engine's nearest
    equivalents are `upgrade_price`, the wear ramp and the obsolescence ramp.
- **Wagon-year.** One wagon in stock for one year. A **fleet average** divides the fleet
  total by the number of wagons in stock; it is not a cost for a named diagram.
- **Reference duty.** The workbook's reference duty is 40,000 km a wagon-year, so a
  six-year interval is 240,000 km. The interval is a distance in the engine
  (`max_distance_between_overhauls`); the year count is a statement about the reference
  duty, not a field.
- **Sourcing.** Every page relied on was fetched and read in this pass. The Serpell report
  and the RAIB report were read as PDFs by text extraction, and the passages quoted were
  printed from the page in which they appear. The HMRS catalogue entries were read directly.
  Hansard was read in the Historic Hansard transcription.
- **No `.dat` value, workbook figure or pakset price is used as evidence anywhere in this
  pass.** The one place a pakset figure would have been convenient - the 1900 wagon
  capital - is filled instead with the measured 1883 and c1906 wagon prices.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1961 | Beeching, wagon functional line | £46.1m for 848,591 wagons = £54.3 a wagon-year | "provision, maintenance, stabling and servicing"; capital provision in | wagon-year | MEASURED inputs, DERIVED per wagon | *The Reshaping of British Railways* (1963), p. 6, https://railnews-business.co.uk/docs%20library/1963%20BRB_Beech001a.pdf |
| 2 | 1970 | Minister of Transport, approved rolling stock programme | "£10.7 million on 427 new passenger carriages, and £5.2 million on 1,429 new wagons" | planned 1970 capital programme, mixed types | per new vehicle | STATED; average DERIVED | HC Deb 28 April 1970 vol 800 c1024, https://api.parliament.uk/historic-hansard/commons/1970/apr/28/railways-rolling-stock |
| 3 | 1970 | House of Lords, short-wheelbase wagon fleet | "330,000 short-wheelbase goods wagons" in March 1969, "should be reduced to about 260,000 by the end of this year"; 3,200 new wagons since January 1969 | short-wheelbase wagons only; the rest of the fleet is not counted | wagons | MEASURED | HL Deb 29 October 1970 vol 312 cc193-4, https://api.parliament.uk/historic-hansard/lords/1970/oct/29/railway-goods-wagons |
| 4 | 1972-81 | HMRS, *Wagons - annual average repair costs 1972-81* | title only; no figures in the online catalogue entry | annual average repair costs; composition not stated | per wagon-year (inferred from the title) | UNAVAILABLE | SKU ME0354, https://hmrs.org.uk/archives/wagons---annual-average-repair-costs-1972-81.html |
| 5 | 1977-79 | HMRS, *Wagon repairs - cost limits 1977-79* | title only | cost limits per repair | per repair | UNAVAILABLE | SKU ME0350, https://hmrs.org.uk/wagon-repairs---cost-limits-1977-79.html |
| 6 | 1980-83 | HMRS, *Wagon repairs - cost limits 1980-83* | title only | cost limits per repair | per repair | UNAVAILABLE | SKU ME0349, https://hmrs.org.uk/wagon-repairs---cost-limits-1980-83.html |
| 7 | 1980-81 | HMRS, *Wagon repair and maintenance 1980-1981* | title only | wagon repair and maintenance | not stated | UNAVAILABLE | SKU ME0463, https://hmrs.org.uk/wagon-repair-and-maintenance-1980-1981.html |
| 8 | 1981 | Serpell, total vehicle maintenance | "£473 million (1982 prices)" | day-to-day, light, intermediate and general repairs; all vehicle types; capital out | whole fleet | MEASURED aggregate | *Railway Finances* (1983), para 6.44, https://railnews-business.co.uk/docs%20library/1982%20The-Serpell-Report-on-Railway-Finances-1982.pdf |
| 9 | 1981 | Serpell, BREL maintenance and repair | "£266 million (1982 prices) - 55 per cent of all maintenance expenditure" | heavy maintenance and repairs by BREL, all vehicle types | whole fleet | MEASURED aggregate | as row 8, para 6.49 |
| 10 | 1977-81 | Serpell, depot maintenance trend | costs "rising (by about 30 per cent in real terms for some vehicle types) since 1977"; "about one-fifth" of the rise from "lengthened intervals between repairs" | depot maintenance, not wagon-specific | per vehicle | MEASURED (consultants' finding) | as row 8, paras 6.46 and 6.51 |
| 11 | 1981 | Serpell, maintenance depots | "150 maintenance depots, 77 for traction units, 46 for passenger rolling stock and 38 for wagons" | depot count | depots | MEASURED | as row 8, para 6.47 |
| 12 | 1981 | Serpell, records | "maintenance records are not kept for individual vehicles" | the reason no per-vehicle series was published | n/a | STATED (official finding) | as row 8, para 6.45 |
| 13 | 1981 | Serpell, BREL unit costs 1977-81 | "by 40 per cent or more for locomotives, by 35-40 per cent for multiple units, by 25 per cent for HSTs and by 15 per cent for coaches" | BREL repairs; wagons not listed | per repair | MEASURED | as row 8, para 6.51 |
| 14 | pre-1992 (BR instruction 1980) | RAIB, HAA wagon General Repairs | "HAA and similar wagons were subjected to General Repairs (GR) at wagon workshops on a seven-yearly cycle ... The majority of HAA wagons received new bodies as part of these works" | HAA and similar merry-go-round hoppers | per wagon per event | STATED (official; cites BR Engineering Instruction WF/81 of 1980) | RAIB report 02/2008, p. 21, paras 87-88, https://assets.publishing.service.gov.uk/media/547c9032e5274a428d00017f/R022008_080131_King_Edward_Bridge.pdf |
| 15 | 1977 | BR Research, direct operating costs method | report exists; PDF behind a free registration wall | method for fleet operating costs, not a cost series | n/a | UNAVAILABLE | IM-TAG-005, https://www.rssb.co.uk/spark/sparkitem/pb008307 |

Row 1 is the only measured level near the window and row 14 the only documented cycle.
Row 1 is 11 years before the window opens; row 14 describes practice that was in force
inside it.

## 4. The series

### 4.1 The points that exist

| Date | Nominal | 1900 money | Grade | Basis |
|---|---|---|---|---|
| 1892 | £4 4s. a wagon-year | 4.33 | MEASURED | Hill, 19 companies, repairs and renewals, renewals inside |
| 1961 | £54.3 a wagon-year | 9.84 | MEASURED inputs, DERIVED | Beeching, functional line including provision, 848,591 wagons |
| 1970 | not measured | - | UNAVAILABLE | no per-wagon repair figure for the year |
| 1972-81 | not readable | - | UNAVAILABLE | HMRS ME0354 |
| 1981 | not measured | - | UNAVAILABLE | Serpell gives a whole-fleet total with no wagon split |

The 1892 figure is Hill's £4 4s. at the general index 97. Note that
`research-pricing-rows-43.csv` records **5.38** for the same nominal figure; 5.38 is
£4.20 × 100 ÷ 78, which uses the `vehicle purchase` index and not the `general` index that
`prices.tab` requires for maintenance. The correct conversion is 4.33, and the correction
is recorded here rather than applied, because the CSV is outside this pass's remit.

### 4.2 What the series shows

The measured level rises 2.3 times in real terms between 1892 and 1961 (£4.33 to £9.84),
and nothing readable measures it after 1961. [report 43](research-pricing-report-43.md)
carries the ratio-derived ladder at 14.3 in 1970, 24.8 in 1990 and 23.8 in 2020 (1900
money, 10-tonne reference); those are ESTIMATES built from the falling wagon-to-carriage
ratio, not measurements, and this pass neither confirms nor overturns them. The Serpell
evidence in row 10 says the real direction in 1977-81 was upward - depot maintenance costs
rose about 30 per cent in real terms for some vehicle types - so a flat real line across
the window would contradict the one official statement about the trend.

### 4.3 The overhaul event against a new wagon

This is the check the new 1970 price makes possible. A is the annual maintenance total; the
event is 1.2 A; the fourth and fifth columns express those two as percentages of a measured
new-wagon price.

| Date | A (1900 money) | New wagon (1900 money) | A as % of new | Event 1.2 A as % of new | Grade |
|---|---|---|---|---|---|
| 1900 | 4.20 (Hill, 1892, held) | 111.2 (GER 10/12-ton, 1883) | 3.8% | 4.5% | DERIVED from two MEASURED figures |
| 1900 | 4.20 | 64.7 (private-owner 7-plank, c1906) | 6.5% | 7.8% | DERIVED from two MEASURED figures |
| 1970 | 14.3 (ladder, ESTIMATE) | 457.7 (BR programme average, 1970) | 3.1% | 3.8% | DERIVED from a MEASURED price and an ESTIMATE |
| 2020 | 23.8 (ladder, ESTIMATE) | not used | - | - | ESTIMATE |

Two conclusions follow.

- **The event is smaller against capital after 1900 than the 7-15 per cent band in the
  source analysis suggests.** At 1970 it is 3.8 per cent if the ladder's A is right. The
  band rests on 1900-era relationships between the annual total and the wagon's price and
  cannot be carried forward without the prices: the new-wagon price rose from £111 to £458
  in real terms (4.1 times) while the modelled A rose 3.4 times, so the same money event
  became a smaller share of the wagon.
- **The HMRS series would discriminate between two levels of A.** If it puts A near £27 in
  1900 money for a 16-ton wagon (5.9 per cent of the measured 1970 price, the 1900
  relationship), the event is 7.1 per cent of new and the ladder's 14.3 is too low. If it
  puts A near £14, the event is 3.8 per cent and the ladder is right. That is the single
  most useful thing the document would settle.

### 4.4 The fleet and the denominator

The 1972-81 fleet was the tail of a very large, old, mixed fleet. At March 1969 it
contained 330,000 short-wheelbase wagons, falling to about 260,000 at the end of 1970; in
October 1970 the government described that class as "still the vast majority of the
fleet". Against it sat a small modern fleet: 3,200 new wagons of 15-foot or longer
wheelbase since January 1969, and the air-braked HAA hopper, of which about 10,500 were
built between 1964 and 1982. The average capacity of the 1,124,812 wagons in stock in 1955
was 13.8 tons, so the 10-tonne reference wagon of the maintenance ladder describes the older
majority and not the new hoppers. A fleet-average A from the HMRS document would therefore
sit below the cost of an HAA and above the cost of a 16-ton mineral wagon, and it should not
be read as either. [report 43](research-pricing-report-43.md) §4 for the 1961 composition
and [wagon overhaul source analysis](wagon-overhaul-source-analysis.md) §2 for the 1955
capacity figure. `[MEASURED: rows 2-3 and RAIB 02/2008 para 27]`

## 5. Recommended treatment for the wagon overhaul event

**Keep the A-based envelope; do not convert the event to a share of capital.** The
parameters are a head of 0.8 A, a first event of 0.9 A, a maximum event of 1.2 A, and an
interval of 240,000 km. The reasons, and the conditions attached to them:

1. **The interval of six years is supported.** Six years sits inside the 5-7 year band
   assembled in [wagon-overhaul-source-analysis](wagon-overhaul-source-analysis.md) §2, and
   the one documented BR cycle is seven years for HAA and similar wagons (row 14). Six is
   the midpoint and the workbook's reference duty. If the documented seven years is
   preferred, the interval becomes 280,000 km at 40,000 km a year, and the head must rise
   from 0.8 A to 0.83 A to keep head plus annualised overhaul charge equal to A; a 1.2 A
   event at seven years is a 0.171 A annual charge, not 0.20 A. Either pair is coherent; the
   pair, not either number, is what the evidence constrains.
2. **The event multiple of 1.2 A is an estimate and remains one.** Nothing measured for
   1972-81 prices a wagon GR. What the evidence does say is that the GR was a full strip -
   dismantling to components, repair or replacement of components, reassembly - and that
   most HAA wagons received a new body during it. A full strip is a large event, so a
   multiple above 1.0 A is more plausible than a multiple below it; 1.2 A is at the
   conservative end of "large".
3. **The new body is capital, not maintenance.** If BR charged rebodying to capital, as a
   renewal rather than a repair, the maintenance account saw the strip and the component
   work but not the body. That is a further reason not to raise the event multiple to cover
   a body: under the envelope rule the body belongs to the vehicle's purchase cost and to
   `upgrade_price`, and charging it again as an overhaul would double count it.
   [source composition](../vehicle-cost/source-composition.md) records that no source
   states the composition of a wagon maintenance figure, so this remains an inference from
   the RAIB description, not a measured split.
4. **The first-event ratio of 0.75 is untested.** It gives 0.9 A for the first event and
   1.2 A thereafter. No source measures the first event separately. The steady-state
   annualised overhaul charge is exactly 0.20 A and the envelope holds from the second
   event; the first event is 0.3 A below the steady event, so the first six-year cycle
   under-recovers by about 0.05 A a year. That is a timing choice, not a double count, and
   it should be recorded as such in the basis text.
5. **What would move the multiple, and in which direction.** A wagon GR invoice or works
   order price would move it directly; the HMRS cost-limit files (rows 5-6) would bound it
   from above, because a repair assessed at or above the limit was not carried out; the HMRS
   average repair cost series (row 4) would move A and therefore the event in money, but not
   the multiple. A measured GR price below 1.2 A would lower the event and raise the head; a
   price above 1.2 A would do the reverse. The sum stays at A either way.

**Exact fields for the workbook.** `max_distance_between_overhauls` 240,000 km;
`initial_overhaul_cost` 0.9 A; `max_overhaul_cost` 1.2 A; the continuous head 0.8 A. The
basis string should name this report, the six-year interval as "6 years at the 40,000 km a
year reference duty", and the event multiple as an ESTIMATE.

## 6. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| A, 1972-81, 10-tonne wagon (1900 money) | not measured | 9.8-27 | 1961 measured 9.84; the ladder's 1970 value 14.3; a capital-proportional 1970 value would be about 27 |
| Interval between GRs | 6 years | 5-7 | contract terms of 5 and 7 years; the HAA GR documented at 7 years |
| Event share of A, s | 0.20 | 0.10-0.30 | no measurement; the source analysis's range |
| Event as a multiple of A, s × n | 1.2 | 0.5-2.1 | product of the two rows above |
| Event as % of a 1970 new wagon | 3.8% | 1.1-12% | product of the multiple band above and the A band, against the measured £458 |
| Real trend of A, 1977-81 | rising | +10 to +30% | ESTIMATE, guided by Serpell's 30 per cent for "some vehicle types"; wagons not named |

**Structural assumptions.** (i) A is a fleet average, so it mixes 16-ton minerals with
air-braked hoppers; the ladder's size term is the only adjustment. (ii) The 1970 wagon price
is an average over a mixed programme including high-capacity air-braked stock, so it is
above a 16-ton mineral wagon's price and the percentages against it are correspondingly
low. (iii) The RAIB description is of HAA and similar wagons, the newest and heaviest class;
older vacuum-braked wagons may have had a different cycle and a smaller event. (iv) The HMRS
series, when read, may be a fleet average over a fleet whose composition changed every year
of the window.

## 7. Gaps and routes

In order of value, with the exact route to each.

1. **HMRS ME0354, *Wagons - annual average repair costs 1972-81*.** Route: use the "Contact
   Archivist for Information" form on the catalogue page
   (https://hmrs.org.uk/archives/wagons---annual-average-repair-costs-1972-81.html), or the
   contact page at https://hmrs.org.uk/contacts, quoting SKU ME0354. The HMRS archives page
   states that items are available "to bona-fide researchers or historians at our Museum and
   Study Centre by prior appointment" and that "within reason and for a copying and
   administrative fee, copies of some items can be created", though not "large extracts of
   more than a few sheets". A request should therefore ask for the extent of the item first
   (how many sheets, which years, whether it is annual by wagon type) and then for a quote
   for the pages covering 1972, 1975, 1978 and 1981. **UNAVAILABLE.**
2. **HMRS ME0350 and ME0349, the repair cost limits for 1977-79 and 1980-83.** Same route
   and same form, quoting both SKUs. These are the documents that would state the cash
   limit per repair and so bound the GR price from above. **UNAVAILABLE.**
3. **HMRS ME0463, *Wagon repair and maintenance 1980-1981*.** Same route. It may be the
   narrative companion to ME0354 and would say what the cost series counted.
   **UNAVAILABLE.**
4. **BRB Annual Report and Accounts, 1972-1981.** Route: the British Library or the
   National Railway Museum library for the printed volumes; HathiTrust item
   `mdp.39015024382049` covers 1972-1977 but is search-only. The accounts line to look for
   is "maintenance of rolling stock", which is a whole-fleet total; the reports may also
   carry a statistical appendix of wagon numbers, which would supply the denominator.
   **UNAVAILABLE.**
5. **BR Research IM-TAG-005 (1977), *A method for evaluating the direct operating costs
   incurred by the acquisition, maintenance and movement of a fleet of vehicles*.**
   Route: free registration at RSSB SPARK, then download from
   https://www.rssb.co.uk/spark/sparkitem/pb008307. A 1977 BR Research method paper may
   carry unit costs for wagons as a worked example. **UNAVAILABLE.**
6. **The trade press.** No accessible index entry for a *Railway Gazette* or *Modern
   Railways* article on wagon repair costs in the window was found; the Railway Citation
   Index (https://railwaycitationindex.omeka.net) indexes titles and returned nothing under
   "wagon repair costs". The route is the bound volumes at the NRM library, searching the
   1972-81 issues for "wagon repairs", "wagon maintenance" and "BREL charges".
   **UNAVAILABLE.**
7. **The fleet count at the end of the window.** The verified count in this pass is for
   1970. A Commons debate of 22 March 1983 is reported to give a fleet of about 65,000
   wagons; the page was not read here, so the figure is recorded as a lead and not used.
   Route: the BRB statistical appendix for 1981, or a Hansard written answer on wagon
   stock. **UNAVAILABLE.**

**What a positive result would and would not change.** Reading ME0354 would replace the
ladder's 1970 value of 14.3 with a measured A and so change the money amount of both the
head and the event; it would not change the 1.2 multiple, the six-year interval or the
0.8/0.2 split, none of which the document's title suggests it contains. The multiple needs
a works order price for one GR, and the cost-limit files are the nearest identified source
that would bound it.
