---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 53 - Midland composite carriage price, 1860s

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026. Files
written: this report and `research-pricing-rows-53.csv`. No workbook, `.dat` or existing doc
was changed.

This pass closes one gap in [report 44](research-pricing-report-44.md) §8. Report 44
established a measured **works overhaul** (a heavy repair in the company's carriage works, at
which the vehicle is stripped, repainted and retrimmed) of **£62** for a **composite carriage**
(a carriage whose compartments serve more than one class) in the 1860s, and could not express it
as a share of capital because no price for the carriage itself had been found. Report 44 assumed
a composite at £450-500 and put the overhaul at 12-14 per cent of capital, against the 25 per
cent that the transcription of Lacy & Dow had suggested. This pass tests that assumption and
finds that the source's own range for the carriages of the era is **£225-250**, the range the
transcription applies to the overhauled composites, so the overhaul is **24.8-27.6 per cent** of
capital, not 12-14 per cent.

## 1. What this pass found

1. **No composite-specific Midland price for the 1860s is readable online.** Lacy & Dow vol. 1
   gives the £62 overhaul on p. 31 but the transcription does not record the price of the
   carriage the money was spent on; the book itself has no digital copy (Internet Archive has no
   scan under the title, Google Books returns `noview`, Open Library has no ebook, HathiTrust has
   no record). The routes that remain are a library copy and the Midland Railway Company records
   at The National Archives (§7). **UNAVAILABLE.**

2. **The same source's price range for the era is £225-250 a vehicle.** The transcription
   summarises the book as showing that "early railway carriages (1860s and before) do not appear
   to differ greatly in price, being something between £225 and £250 per vehicle for the most
   part". It then introduces the £62 overhaul with the words "a price for overhaul is given of
   **these vehicles**". The range is therefore the one the transcriber applied to the overhauled
   composites; it is not a range for a different, smaller class. `[FORUM:https://forum.simutrans.com/index.php?topic=6521.35]`
   **STATED.**

3. **The 25 per cent is the transcriber's division of a measured event by that stated range,
   not a division by an unrelated figure.** £62 / £250 = 24.8 per cent; £62 / £225 = 27.6 per
   cent. Report 44 finding 3 called the range a description of "smaller vehicles than a
   composite" and proposed £450-500 for the composite. The transcription gives no composite
   price at that level. Its only figure near £500 is the p. 44 note that "by the 1860s, the cost
   seems to have risen to £500 apiece"; that note follows the travelling post office item, and
   the same post gives £225-250 for early carriages generally, so the £500 is best read as a
   different, specialised vehicle. The correction is set out in §5.

4. **The nearest measured Midland carriage prices are the board's own figures of 4 November
   1874, and they bracket a composite between £250 and £450.** On that date the board recorded
   the "capital cost of a first-class carriage of three compartments" as "about £450", a
   second-class of four compartments as "about £250", and a third-class of four compartments as
   "about £270". The figures were used to compare each class's yearly earnings with its capital
   cost, in the discussion that led to the abolition of second class from 1 January 1875.
   `[LITERATURE:https://archive.org/details/historyofmidland00strerich]` **MEASURED (quoted in a company history).**

5. **The nearest dated Midland composite is an 1870s bogie carriage at £820 or £979.** Lacy &
   Dow p. 57 records a Midland bogie carriage (a carriage carried on two swivelling wheeled
   trucks) of the 1870s at £820 with four-wheeled bogies and £979 with six-wheel bogies. The
   transcription does not state its class or length, and it is a main-line bogie vehicle, not the
   four-wheel stock of the 1860s. **STATED.**

6. **The overhaul-to-capital ratio is not an input to the workbook.** The engine's overhaul
   fields are calibrated from the event as a multiple of the annual maintenance total A, not as
   a share of capital ([report 44](research-pricing-report-44.md) §5;
   [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md) "Carriage overhaul
   by era"). This pass changes the documented **capital share** (the overhaul price as a
   proportion of the vehicle's new price) and the reading of report 44 finding 3; it changes no
   workbook value and no `.dat` value.

## 2. Method

- **Deflator.** Nominal figures are converted with the `general` series in
  `New/config/prices.tab` (1900 = 100) wherever a 1900-money comparison is made. The values used
  are **1865 = 98** and **1874 = 109**; 1863 is also 98. `prices.tab` states that vehicle
  maintenance stays on the general index and that no UK maintenance price index exists before
  January 1987, so the general series is the engine's own treatment rather than a choice made
  here. No vehicle-purchase index is used.
- **Date convention.** Lacy & Dow give the overhaul only as "the 1860s". This pass uses 1865
  for deflation, the same mid-decade convention as report 44. The 1860s general index runs from
  97 (1864) to 110 (1867); 1865 at 98 is within 12 per cent of either extreme.
- **Grades.** MEASURED = an account, contract or published total with a stated scope. STATED = a
  statement of a price or rate without the underlying account. DERIVED = arithmetic from a
  measured or stated figure, with the chain shown. ESTIMATE = judgement, marked as such.
  UNAVAILABLE = identified but not readable.
- **Transcriptions are marked.** The Lacy & Dow figures were not read in the book. They come
  from the Simutrans forum transcription of 18 August 2012, which quotes page numbers for most
  items. The 1874 board figures come from Stretton's company history, which quotes the board
  discussion; the original minute was not read. Both are graded MEASURED or STATED with the
  route stated, not promoted to a reading of the original.
- **Claim tags.** External figures carry `[LITERATURE:<url>]` or `[FORUM:<url>]` because
  untagged prose in a draft is implicitly `[CODE]` under
  [conventions](../conventions.md) and would wrongly claim verification against this repository.
- **No `.dat` value, workbook value or pakset price is used as evidence anywhere in this pass.**
  Every figure is a period price or arithmetic on one.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Grade | Source |
|---|---|---|---|---|---|---|
| 1 | 1860s | Lacy & Dow, Midland composite overhaul | 50 composite carriages "accepted for repairing, repainting and retrimming" at £62 a carriage | one works overhaul; retrim and repaint inside | MEASURED (via a transcription) | Lacy & Dow, *Midland Railway Carriages* I p. 31, transcribed at https://forum.simutrans.com/index.php?topic=6521.35 (post 57, 18 Aug 2012) |
| 2 | 1860s and before | Lacy & Dow, early carriage prices | "between £225 and £250 per vehicle for the most part" | early carriages; no page given; composite not separately priced | STATED (secondary transcription) | as row 1 |
| 3 | 4 Nov 1874 | Midland board, first-class carriage | "capital cost ... about £450" (three compartments); yearly earnings "about £530" (118 per cent) | capital cost per vehicle; board's traffic comparison | MEASURED (quoted) | Stretton, *The History of the Midland Railway* (1901) pp. 202-203; https://archive.org/details/historyofmidland00strerich |
| 4 | 4 Nov 1874 | Midland board, second-class carriage | "about £250" (four compartments); earnings "about £430" | as row 3; the printed 122 per cent does not follow from £430/£250 (172 per cent), so one printed number is suspect | MEASURED (quoted), internally inconsistent | as row 3 |
| 5 | 4 Nov 1874 | Midland board, third-class carriage | "about £270" (four compartments); earnings "about £890" (330 per cent) | as row 3 | MEASURED (quoted) | as row 3 |
| 6 | 1870s | Lacy & Dow, Midland bogie carriage | £820 each with four-wheeled bogies; £979 with six-wheel bogies | main-line bogie carriage; class and length not stated | STATED | Lacy & Dow I p. 57, via row 1 forum |
| 7 | early 1870s | Lacy & Dow, passenger-rated milk van | £171 each | non-passenger rated vehicle | STATED | Lacy & Dow I p. 42, via row 1 forum |
| 8 | Feb 1840 | Midland Counties Railway carriage orders | enclosed second £210; open-sided second £168; fully open third £143 | order prices per vehicle | MEASURED (via a transcription) | Lacy & Dow I p. 5, via https://forum.simutrans.com/index.php?topic=6521.210 (post, 31 Dec 2017) |
| 9 | 1844 | Midland travelling post office | £460 each | TPO vehicle, outside contractor | STATED | Lacy & Dow I p. 43, via row 1 forum |
| 10 | 1860s | Lacy & Dow, "vehicles" | "the cost seems to have risen to £500 apiece" | subject not clear in the transcription; the note follows the TPO item | STATED, scope uncertain | Lacy & Dow I p. 44, via row 1 forum |
| 11 | 1863 | Highland Railway composite | £322 10s each | composite, out-of-company comparator | STATED (secondary) | Tatlow, *Highland Railway Carriages and Wagons* p. 29, via https://forum.simutrans.com/index.php?topic=6521.210 |
| 12 | 1879 | Highland Railway tri-composite | £499 each; 35 ft 1 in; 14 t 10 cwt | six-wheel tri-composite, later comparator | STATED (secondary) | Tatlow p. 38, via the same thread |
| 13 | 1865 | £62 as a share of £225 and £250 | 27.6 per cent and 24.8 per cent | nominal, same year | DERIVED | rows 1-2 |
| 14 | 1865 | £62 and £225-250 in 1900 money | £63.3; £229.6 and £255.1 | general index 98 | DERIVED | rows 1-2; `prices.tab` |
| 15 | 1874 | £450, £250 and £270 in 1900 money | £412.8, £229.4 and £247.7 | general index 109 | DERIVED | rows 3-5; `prices.tab` |
| 16 | 1865 and 1874 | £62 as a share of the 1874 class prices | 15.3 per cent (first), 27.6 per cent (second), 25.5 per cent (third), 19.7 per cent at a £350 midpoint | both figures deflated to 1900 money | DERIVED | rows 13-15 |
| 17 | 1863 | £62 as a share of the Highland composite | 19.2 per cent | both at index 98 | DERIVED | rows 1 and 11 |

## 4. The price and the overhaul share

**The answer to the brief.** No composite-specific Midland price for the 1860s was readable. The
nearest figure is the source's own range for early carriages, **£225-250** (STATED, 1860s and
before, no page). Applied to the measured £62 overhaul it gives **24.8-27.6 per cent of
capital**. The carriage's builder, length, compartment count and wheel arrangement are not in
the accessible transcription: all four are **UNAVAILABLE**, and the only type information is
that it was a composite.

| Denominator | Date | Nominal | 1900 money | £62 as a share | Grade |
|---|---|---|---|---|---|
| Early carriage, low | 1860s | £225 | £229.6 | 27.6% | STATED price, DERIVED share |
| Early carriage, high | 1860s | £250 | £255.1 | 24.8% | STATED price, DERIVED share |
| Second-class, four compartments | 1874 | £250 | £229.4 | 27.6% | MEASURED price (suspect, §6) |
| Third-class, four compartments | 1874 | £270 | £247.7 | 25.5% | MEASURED price |
| Composite midpoint (estimate) | 1874 | £350 | £321.1 | 19.7% | ESTIMATE, between second and first |
| First-class, three compartments | 1874 | £450 | £412.8 | 15.3% | MEASURED price |
| Highland composite | 1863 | £322 10s | £329.1 | 19.2% | STATED, out of company |

The central value is **25 per cent** (24.8 per cent on £250). The 12-14 per cent in report 44
requires a composite at £450-500. The transcription has no composite at that level: its £500
note of p. 44 sits after the travelling post office item and would contradict the same post's
£225-250 range for early carriages if it were read as a general carriage price, so it is best
read as a specialised vehicle. The only measured Midland passenger carriage at £450 is the 1874
**first-class**, and nothing read in this pass says the 1860s composite was priced as a
first-class carriage.

**The event/A ratio is unchanged.** £62 at index 98 is £63.3 in 1900 money; Hill's 1892 total of
£34.3 ([report 43](research-pricing-report-43.md) §6) makes the event 1.84 × A, where A is the
annual maintenance total per carriage-year. The 1830-1890 **overhaul provision** (the annualised
charge, equal to the event divided by the interval) therefore remains 28 per cent of A at a
six-year interval ([report 44](research-pricing-report-44.md) §4.2 and §5). The capital price
does not enter that calculation.

## 5. Recommended treatment

1. **Record the Victorian carriage overhaul as 25 per cent of capital, band 14-28 per cent.**
   The central value is the £62 event against the £225-250 range that the source applies to the
   same vehicles. The band's lower end is the 1874 first-class bracket; its upper end is the
   £225 denominator. The 1863 Highland composite, at 19.2 per cent, sits inside the band.

2. **Correct report 44 finding 3 and the matching paragraph in
   [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md).** The statement
   that the range describes early carriages smaller than a composite, and that a composite cost
   £450-500, is not supported by the transcription: the transcription applies the range to
   "these vehicles", the ones overhauled at £62, and gives no composite price at all. The
   £450-500 figure should be withdrawn or relabelled ESTIMATE with the 1874 first-class price as
   its only anchor, together with a note that the p. 44 £500 refers to a specialised vehicle.

3. **Do not change the workbook.** `CARRIAGE_OVERHAUL` and the `Overhauls & upgrades` sheet use
   the event as a share of A; the capital share is documentation only. A pass that changed the
   capital share without changing A would move money between fields for no measured reason.

4. **Keep the description of the vehicle honest.** In any doc that mentions this overhaul, say
   "a Midland composite carriage, 1860s, builder and dimensions unrecorded" rather than
   implying a known 4-wheel or 6-wheel vehicle.

5. **Record the 1874 board figures as the nearest measured Midland carriage prices.** They are
   the only company-level capital costs per carriage found for the 1860s-1870s, and they are
   useful independently of this overhaul: first £450, second £250, third £270, with the
   second-class figure flagged as internally inconsistent.

## 6. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| 1860s composite price | £250 | £225-450 | source range £225-250; 1874 first-class £450 as the upper bracket; composite class position unknown |
| Overhaul share of capital | 25% | 14-28% | the same band; the low end needs a first-class-level composite |
| Date of the £62 event | 1865 | 1860-1869 | source says only "the 1860s"; index 97-110, so the converted figure is stable only to about 12 per cent |
| 1874 second-class price | £250 | £250-352 | printed 122 per cent implies £305 earnings or £352 cost against the printed £430 and £250; two scans agree on the digits, so the inconsistency is in the printed page |
| Composite class position | between second and first | £250-450 | the 1874 class spread is 1.8 times; no composite price found |

**Structural assumptions.** (i) The £225-250 range is taken as applying to the composites
because the transcription introduces the £62 as a price "of these vehicles" after stating the
range; the book's own page for the range was not read, so a page-level reading could show the
range covering only some classes. (ii) The 1874 figures are
board capital costs used for a traffic comparison, not contract prices; their scope (whether
they include the whole vehicle) is not stated. (iii) The Highland 1863 composite is a different
company and may have been built to a different specification.

## 7. Gaps and routes

- **Lacy & Dow, *Midland Railway Carriages* vol. 1 (Wild Swan, 1984, 170 pp., ISBN 0906867193).**
  Out of print. No digital copy: Internet Archive has no scan under the title; Open Library
  records no ebook (`ebook_access: no_ebook`); Google Books holds a volume (`MseoJwAACAAJ`) but
  returns `preview: noview`, so there is no snippet search; HathiTrust has no record for the
  ISBN. **UNAVAILABLE online.**
  Reading routes: the Midland Railway Study Centre library, ref. 104, in the Reading Room at the
  Museum of Making, Derby (consultation only, no loans); the British Library; the National
  Railway Museum's archive and library catalogue; second-hand copies at £30-45 a volume (a 2021
  RMweb thread records that range:
  https://www.rmweb.co.uk/topic/167740-modeller-friendly-loco-and-coaching-stock-books-for-lnwr-and-mr/page/2/).
  One reading of p. 31 and the adjacent price pages would settle the composite price, its
  builder, dimensions and lot.
- **The National Archives, RAIL 491, Midland Railway Company: Records.** The series description
  lists "contracts, specifications and plans; locomotive and rolling stock records"; pieces
  969-1016, 1021-1043, 1058-1063, 1068-1076, 1078 and 1080 are digitised. A committee or board
  minute recording the tender acceptance (the wording "accepted for repairing, repainting and
  retrimming" is minute language) is the document type that would carry the price, and the same
  series would record new-carriage tenders. The Midland committee that handled carriage business
  in the 1860s, and its piece numbers, were not identified in this pass. **UNAVAILABLE online.**
- **Midland Railway Study Centre Carriage & Wagon database.** The Lot & Diagram lists give lot
  numbers, quantities and dates for carriages from 1877 (Lot 1 onwards), but no prices; the
  catalogue search for "composite" in the Carriage & Wagon Department Document category returns
  one item, a specification list without prices. **UNAVAILABLE for prices.**
- **Midland Railway Society Journal and Midland Record indexes.** Searched for "composite
  carriage", "carriage cost", "carriage prices", "carriage building" and "Kirtley carriage":
  no article on carriage prices. The indexes are title-level only. **No route found.**
- **The 1860s trade press.** *The Railway Times*, *Herapath's Railway Journal* and *The Engineer*
  carried contract notices and sometimes prices. Not searched page by page in this pass; the
  volumes are partly digitised but not full-text searchable from this environment. A
  contract-price note for a Midland composite lot would close the gap directly.
- **A Midland half-yearly report or board minute giving a carriage lot price.** The published
  reports are expected to give rolling-stock capital totals rather than unit prices (not read in
  this pass); a lot-level price needs the committee or board minutes (above).
- **A second company's 1860s composite price.** The Highland Railway's £322 10s in 1863 (Tatlow
  p. 29) is the only other British composite price of the decade found, and it converts to 19.2
  per cent for the £62 event. A Midland price at that level would put the overhaul at about a
  fifth of capital rather than a quarter.

## Open questions

- Was the £62 contract of the early 1860s or the late 1860s? The book gives only the decade, and
  the general index moves from 97 to 110 across it, so the converted figure is stable only to
  about 12 per cent, and the date matters for matching the contract to a lot.
- Did the Midland price composites as second-class or between the classes in the 1860s? The 1874
  board figures are the first class-differentiated prices found, and they are nine years later.
- Is the printed second-class figure £250 or £350? The stated 122 per cent implies £352 at £430
  earnings, and the page is worth a visual check in a library copy of Stretton.
