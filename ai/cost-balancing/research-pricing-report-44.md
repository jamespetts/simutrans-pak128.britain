---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 44 — Carriage works overhauls: interval and share, 1830-2026

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026. Files
written: this report and `research-pricing-rows-44.csv`. No workbook, `.dat` or existing doc was
changed.

This pass extends [report 43](research-pricing-report-43.md). Report 43 fixed the annual carriage
total A (33 / 140 / 265 / 460 / 440 in 1900 money at 1900 / 1950 / 1970 / 1990 / 2020); this pass
fixes the two quantities needed to split A into a continuous head and a periodic works event:

    A = renewals provision + overhaul provision + routine remainder
    overhaul provision = (mean overhaul event) / (interval in years)

The two deliverables per era are therefore (a) the interval between works overhauls and (b) the
size of one event, expressed where possible as a multiple of A so that no capital denominator is
needed.

## 1. What this pass found

1. **Victorian carriages went to the works two or three times a year, and those visits were mostly
   light.** The North Eastern Railway's York and Shildon shops in 1892 built 200 carriages,
   rebuilt 100, and passed **8,700 through for repairs** on a stock of **3,281** — **2.65 works
   visits a carriage-year**. The Midland's Derby carriage repairing shop in 1910 turned out
   **about 140 repaired carriages a week** (7,280 a year). Neither source separates heavy from
   light. **MEASURED** (NER), **STATED** (Midland). This kills the reading of the 2.65 as an
   overhaul rate: a heavy overhaul every 4.5 months is not consistent with any cost figure in
   Hill.
2. **No pre-1923 source separates a heavy overhaul from a light works visit.** The nearest
   measured split is the GWR in 1935: Swindon's carriage works could repair **5,000 coaches a
   year, "3,000 being in the nature of heavy repairs"**, against **8,948 coaching vehicles** —
   a **works visit every 1.8 years and a heavy repair every 3.0 years**. **MEASURED** (works
   capacity, reported by the company). This is the only measured heavy-repair interval before
   1948, and it belongs to the grouping era, not to the Victorian band that has been built on a
   bare visit rate.
3. **The "25 per cent of capital" attached to the Lacy & Dow £62 is not measured.** The source,
   as transcribed, gives 50 Midland composite carriages "accepted for repairing, repainting and
   retrimming" at **£62 each**. The 25 per cent is a forum author's division of £62 by the top of
   a **£225-250** range that describes "early carriages (1860s and before)" — smaller vehicles
   than a composite. On a £450-500 composite the event is **12-14 per cent**. **MEASURED** (£62),
   **STATED** (£225-250), **DERIVED** (the percentage). The knowledge base's "Victorian measured
   at 25%" overstates the grade and probably the value.
4. **A 25-per-cent-of-capital event cannot recur every 4-6 years inside Hill's measured total.**
   At a £250 carriage the 25 per cent event is £62.50; at £450 it is £112.50. Hill's £33 6s
   contains renewals of £6.30-£16.40 (2.53 per cent of stock at those prices), leaving £17-£27 of
   repair spend. At £450 the event alone is 5.1 times the entire annual repair spend, so even at a
   ten-year interval it takes 51 per cent of repairs; at £250 it needs **6-8 years** to fall to
   29-39 per cent of repairs. **DERIVED** from Hill Tables II and XXIV and the Lacy & Dow figure.
   The 4-6-year Victorian band therefore survives only if the event is nearer 12 per cent of
   capital, not 25.
5. **In units that need no price denominator, the overhaul fell from about 1.8 years of the annual
   total to about 0.16 years.** The 1860s £62 is **1.84 × A** (both in 1900 money, 1865 index 98,
   1892 index 97); the 1982 York Works overhaul at **"more than £2,000"** a Mk 1 vehicle is
   **0.16 × A** (1982 index 3,483; A interpolated to 1982 = £369). At a 6-year interval the first
   is a **30 per cent provision**; at a 2-year interval the second is **8 per cent**. **DERIVED**
   from two MEASURED event prices. This is the single most useful result in the pass, because it
   is independent of carriage prices, of the pakset and of the deflator's level.
6. **Report 36's "Mk 1 works overhaul 1982 ≈ 8 per cent of new" does not survive arithmetic.**
   £2,000 is **2-5 per cent** of any defensible Mk 1 new price: £5,500 in 1955 gives 4.9 per cent,
   £12,000 in 1957 gives 2.4, £16,000 in 1960 gives 1.9. Eight per cent would require a 1982
   new-build price of £25,000, which no source supports. The 8-per-cent figure propagated into
   [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md) as the BR band's
   first event and should be withdrawn. **DERIVED.**
7. **Annual carriage mileage can be measured for 1892 and 1961 and stated for the modern era.**
   1892: Hill's LNWR line is **3,650 passenger train-miles per carriage in stock** (21,000,664
   train-miles over 5,754 carriages) — a train-mile, not a carriage-mile, figure; at 5-7 carriages
   a train it is **29,000-41,000 km** a carriage-year. 1961: **229.6m passenger train-miles** over
   **33,607 passenger-carrying vehicles**, at 6-10 vehicles a train, is **66,000-110,000 km**.
   Modern: the 1983 Sprinter specification's "major overhaul every five years or 350,000 miles" is
   a design duty of **70,000 miles (113,000 km) a year**. **MEASURED + DERIVED.**
8. **The 35 per cent renewals share is an artefact of one accounting definition, not a physical
   constant.** Hill's 2.53 per cent of carriage stock renewed a year is an average of ten
   companies whose individual rates in the same table run from 2.8 to 8.4 per cent (the Midland's
   6.4 per cent is a rebuild programme, and Hill footnotes that "nearly the whole of the Midland
   carriage stock was rebuilt during the nine years preceding 1887"). At £250-650 a carriage the
   renewals share of Hill's £33 6s is therefore **19-49 per cent**, which brackets the 35 per cent
   but does not fix it. BR and later totals are net of renewals, so the 35 per cent must not be
   applied to them. **MEASURED (rates), DERIVED (shares).**
9. **The BR interval is verified at source.** Hansard, 11 March 1996: "The full vehicle overhaul
   is mileage based, but occurs approximately every two years", with coaching-stock examinations
   at one, three, six and twelve months and a three-to-four-day safety examination. **STATED**
   (ministerial answer quoting British Rail).
10. **No modern overhaul share can be measured.** The ORR's October 2026 interim review puts TOC
    maintenance at about **£1.5bn, 37 per cent of rolling stock expenditure** — which confirms
    that the lease (the renewals element) is outside the maintenance figure — but states that
    "the boundaries between routine maintenance, heavy maintenance and overhaul ... vary across
    fleets and contracts" and publishes no split. The heavy-overhaul cost that does exist
    (£180,000 a Class 158 vehicle, 2007-09) is a C6-plus *refurbishment with a full interior
    refit*, the same kind of event as the Chiltern rebuild, not a periodic works overhaul.
    **MEASURED (total), STATED (boundaries), UNAVAILABLE (split).**

## 2. Method

- **Deflator.** Every nominal figure is converted with the `general` series in
  `New/config/prices.tab` (1900 = 100): 1865 98, 1892 97, 1910 104, 1935 173, 1945 285, 1948 338,
  1950 359, 1955 468, 1957 510, 1960 534, 1961 552, 1970 795, 1982 3,483, 1984 3,824, 1990 5,408,
  2008 9,212, 2020 12,521. `prices.tab` states "Vehicle maintenance stays on the general index.
  No UK maintenance or repair price index exists before January 1987", so maintenance figures use
  `general` and the vehicle-purchase series is not used anywhere in this pass. Report 43's 1961
  rows used 528 (the 1959 value); this pass uses 552 and does not restate report 43's ladder.
- **Grades.** MEASURED = an account, contract or published total with a stated scope. STATED = a
  trade, academic or witness statement of a rate without the underlying account. DERIVED = my
  arithmetic from a measured or stated figure, chain shown. ESTIMATE = my judgement, used only
  where nothing measured exists and marked in every table. UNAVAILABLE = identified but not
  readable.
- **Three definitions, kept apart.** *Works visit*: any entry to a carriage works, however light.
  *Heavy overhaul / general repair*: the works visit at which the body is lifted or stripped,
  bogies and brake gear are attended and the vehicle is repainted or retrimmed. *Rebuild*: a new
  body on the old underframe, or a renewal in kind — capital, not maintenance. The NER's 100
  rebuilds in 1892 and the Midland's 1878-87 rebuild programme are rebuilds; the Lacy & Dow £62 is
  a heavy overhaul; the 1982 York contract is a heavy overhaul; the Chiltern £325,000 Mk 3 is a
  rebuild.
- **The identity.** `A = renewals provision + overhaul provision + routine remainder`;
  `head = A - renewals - provision`; `event = provision x interval x A`. Only the product
  `provision x interval` is constrained by any source; the two separately are a composition.
  Every row that separates them is marked ESTIMATE.
  **Correction, 2026-11-25.** The first draft of this report said "the workbook's A already
  excludes renewals (report 43 §6 heading)" and wrote the head as `(1 - provision) x A`. That
  heading was itself wrong, as report 43 now records: the 1900 and 1950 anchors are gross of
  renewals (Hill states "repairs and renewals") and the 1961 anchor is gross of "provision",
  while the 1984, 1990 and 2020 anchors are net of the capital lease. The provision below is
  computed against the published A, which is what the two measured events calibrate against, so
  it stands unchanged; the head must also carry the renewals deduction where the anchor is
  gross. The workbook phases the 35 per cent share out between 1961 and 1984 rather than at
  1922, because the 1961 Beeching functional line demonstrably contains "provision".
- **No `.dat` value and no pakset price is used as evidence anywhere in this pass.** The pakset
  capital ladders do not appear at all: every share here is a share of A, of a new price taken
  from a period source, or of an annual total taken from a period account.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1892 | NER, York and Shildon carriage shops | 200 new, 100 rebuilt, "8,700 passed through the workshops for repairs"; stock 3,281 carriages | all works visits, light and heavy; rebuilds separately stated | works visits a carriage-year | MEASURED | *Round the Works of our Great Railways* (1893), pp. 102-103; https://archive.org/details/cu31924031260031 |
| 2 | 1892 | NER works-visit rate | 2.65 visits a carriage-year (8,700 / 3,281) | as row 1 | per carriage-year | DERIVED | row 1 |
| 3 | 1892 | Hill, L&YR carriage stock | 3,586 carriages | stock only | vehicles | MEASURED | Hill 1895, App. II Table II; https://archive.org/details/minutesproceedi43britgoog |
| 4 | 1892 | Hill, LNWR train-miles per carriage | 3,650 (21,000,664 passenger train-miles / 5,754 carriages) | passenger **train**-miles per carriage in stock, not carriage-miles | per carriage-year | MEASURED + DERIVED | as row 3 |
| 5 | 1892 | Hill, carriage renewals | 2.53% of stock renewed a year (ten companies) | complete renewals by number | per carriage-year | MEASURED | Hill App. III Table XXIV |
| 6 | 1892 | Hill, Midland carriage renewals | 6.4% a year; "nearly the whole of the Midland carriage stock was rebuilt during the nine years preceding 1887" | rebuild programme, not steady-state renewal | per carriage-year | MEASURED | Hill Table XXIV and note |
| 7 | 1892 | Hill, carriage maintenance | £33 6s a carriage-year (range £18 6s-£52 14s) | "repairs and renewals"; renewals in | per carriage-year | MEASURED | Hill Table II |
| 8 | 1910 | Midland, Derby carriage repairing shop | "about 140 carriages are repaired weekly"; the same 140 "passed through these shops each week"; 12 tons of paint a week | works capacity, all repairs | works visits a year | STATED | *1910 Iron and Steel Institute: Visits to Works*; https://www.gracesguide.co.uk/1910_Iron_and_Steel_Institute:_Visits_to_Works |
| 9 | 1910 | Midland works-visit rate | 7,280 visits a year; 1.8 a carriage-year against the 1892 stock of 4,024 | stock for 1910 not given in the source | per carriage-year | DERIVED (stock ESTIMATE) | rows 8 and Hill Table II |
| 10 | 1935 | GWR, Swindon carriage works | repairs 5,000 coaches a year, "3,000 being in the nature of heavy repairs"; 8,948 coaching vehicles; 275 new vehicles a year | works capacity; heavy/light split given | works visits a year | MEASURED | *Swindon Works and its place in GWR History* (1935); https://www.gracesguide.co.uk/Swindon_Works_in_1935 |
| 11 | 1935 | GWR heavy-repair interval | 3.0 years heavy (8,948 / 3,000); 1.8 years any works visit | as row 10 | years | DERIVED | row 10 |
| 12 | 1860s | Lacy & Dow, Midland composite overhaul | 50 composite carriages "accepted for repairing, repainting and retrimming" at £62 a carriage | one works overhaul including retrim and repaint | per event | MEASURED (via a transcription; the book was not read) | Lacy & Dow, *Midland Railway Carriages* I p. 31, transcribed at https://forum.simutrans.com/index.php?topic=6521.35 |
| 13 | 1860s | Midland early carriage price | "£225-£250 per vehicle for the most part" | "early railway carriages (1860s and before)"; four-wheel, not a composite | capital | STATED (secondary transcription) | as row 12 |
| 14 | 1860s | £62 as a share of new | 24.8-27.6% on £225-250; 12.4-13.8% on £450-500 | arithmetic on rows 12-13 | capital | DERIVED | rows 12-13 |
| 15 | 1860s | £62 as a multiple of A | 1.84 x A (1865 £62 = £63.3 in 1900 money; A = £34.3) | A is Hill's 1892 figure; the 1860s A is not measured | annual total | DERIVED | row 12, row 7 |
| 16 | 1982 | York Works Mk 1 overhaul | "more than £2,000" a vehicle; 200 Mk 1 vehicles ordered | one works overhaul at a BR works | per event | MEASURED (reported by the owning group) | https://svrwiki.com/BR_25346_Standard_Corridor |
| 17 | 1982 | Mk 1 secondhand price | £1,100 (25346 sold to the LMS & BR Coach Fund, July 1982, immediately after overhaul) | secondhand sale, not new | per vehicle | MEASURED | as row 16 |
| 18 | 1982 | £2,000 as a multiple of A | 0.16 x A (£57.4 in 1900 money against A = £369 at 1982) | A interpolated between report 43's 1970 and 1990 points | annual total | DERIVED | row 16, report 43 §6 |
| 19 | 1982 | £2,000 as a share of new | 4.9% on a £5,500 (1955) vehicle, 2.4% on £12,000 (1957), 1.9% on £16,000 (1960), each inflated to 1982 | the new price itself is not measured in this pass | capital | DERIVED | row 16 |
| 20 | 1996 | BR full vehicle overhaul | "mileage based, but occurs approximately every two years"; exams at 1, 3, 6 and 12 months | full overhaul; routine exams separate | per vehicle | STATED | Hansard, 11 Mar 1996, vol. 273; https://hansard.parliament.uk/Commons/1996-03-11/debates/3523c0ba-a67a-4c8e-bb28-bb2605561e75/Railways(RollingStockMaintenance) |
| 21 | 1961 | BR passenger train-miles | 229.6m (fast 80.0, stopping 91.4, suburban 58.2) | passenger services only; freight by coaching train excluded from the train-mile column | train-miles | MEASURED | *The Reshaping of British Railways* (1963), Table 1, p. 12; https://railnews-business.co.uk/docs%20library/1963%20BRB_Beech001a.pdf |
| 22 | 1961 | BR passenger-carrying vehicles | 22,575 coaches + 11,032 multiple-unit cars = 33,607 | stock at 31 Dec 1962, one year after the money | vehicles | MEASURED | Beeching, Appendix 3 |
| 23 | 1961 | Carriage-miles a vehicle-year | 41,000-68,300 miles = 66,000-110,000 km at 6-10 vehicles a train | derived; train length not stated in the source | per vehicle-year | DERIVED | rows 21-22 |
| 24 | 1983 | Sprinter design specification | "an interval between major overhauls of five years or 350,000 miles (560,000 km)" | design duty for the Class 150/155/156/158 family; DMU, not a hauled coach | per vehicle | STATED (secondary) | Wikipedia, *British Rail Class 158*, citing Shore, *Proc IMechE* D 201(2) 1987, pp. 115-122; https://en.wikipedia.org/wiki/British_Rail_Class_158 |
| 25 | 2018 | IET heavy overhaul | "envisaged at around the 950-day mark" | heavy overhaul only; exams at 10 and 50 days separate | per vehicle | STATED (paywalled; via report 40) | *Modern Railways*, 27 Dec 2018, quoted in [report 40](research-pricing-report-40.md) §1.10 |
| 26 | 2024-25 | ORR, maintenance market | TOC maintenance about £1.5bn, 37 per cent of rolling stock expenditure; "the boundaries between routine maintenance, heavy maintenance and overhaul ... vary across fleets and contracts" | whole market; lease/capital outside; no heavy/routine split published | n/a | MEASURED (total), STATED (boundaries) | ORR, *Rolling Stock Maintenance Market Review*, interim, Oct 2026, paras 2.10-2.15 and p. 11; https://www.orr.gov.uk/sites/default/files/2026-10/2026-interim-report-rolling-stock-maintenance-market-review.pdf |
| 27 | 1888 | LNWR carriage stock and works staff | 4,500 passenger carriages; 2,234 workmen at Wolverton, 489 at Euston and Crewe, 731 at out-stations | stock and staff; no throughput given | n/a | MEASURED | Findlay, *The Working and Management of an English Railway* (1889), ch. 8; https://en.wikisource.org/wiki/The_Working_and_Management_of_an_English_Railway/Chapter_8 |
| 28 | 1890s | GER paint cycle | first varnishing about two years, second treatment about three more, then painted | paint and varnish only, not mechanical overhaul | per vehicle | STATED (via report 40) | [report 40](research-pricing-report-40.md) §1.10, citing the Stratford coach painters' chapter |

## 4. The series

### 4.1 The interval

| Era | Evidence | Interval (works overhaul) | Grade |
|---|---|---|---|
| 1830-1890 | NER 2.65 visits a carriage-year; Midland 1.8; GER 5-year paint cycle; Hill's envelope requires 6-8 years for a 25% event | **6 years** (band 5-8) | ESTIMATE, constrained by MEASURED |
| 1890-1922 | same works-visit rates; no heavy/light split; GER 5-year paint cycle | **5 years** (band 4-6) | ESTIMATE |
| 1923-1947 | GWR 1935: 3,000 heavy repairs on 8,948 vehicles | **3.0 years** (band 3-4) | MEASURED (capacity) |
| 1948-1975 | Hansard 1996: full overhaul about every two years; 1965 code: full renovation at years 9-11 and 19-21 | **2 years** (band 2-3) | STATED |
| 1975-2000 | 1978 HST annual works overhaul (15 days); C4 bogie at 600,000-750,000 miles | **2 years** (band 1-4) | STATED + MEASURED |
| 2000-2026 | IET heavy at ~950 days; Sprinter specification 5 years / 350,000 miles | **2.6 years** (band 2.6-5) | STATED |

The two-speed structure is real and is not a conflict: in every era there is a frequent light
visit (NER 2.65 a year; BR's monthly-to-annual exams; the modern 10- and 50-day exams) and a
rarer heavy event. The engine's single interval plus sigmoid can hold both, with
`overhauls_before_max_cost` set to the number of light visits per heavy event. What this pass
fixes is the heavy event, because that is the one that carries money.

### 4.2 The size of one event

| Date | Event | Nominal | 1900 money | A at the date (1900 money) | Event / A | Grade |
|---|---|---|---|---|---|---|
| 1860s | Lacy & Dow, Midland composite, repair + repaint + retrim | £62 | 63.3 | 34.3 (Hill 1892) | **1.84** | MEASURED event; A proxied |
| 1935 | GWR heavy repair | not priced | — | — | — | UNAVAILABLE |
| 1982 | York Works Mk 1 overhaul | £2,000+ | 57.4 | 369 (interpolated) | **0.16** | MEASURED event; A interpolated |
| 2007-09 | Class 158 C6+ refurbishment | £180,000 | 1,954 | about 400 | 4.9 | MEASURED, but a refurbishment, not a periodic overhaul |

The two usable points are 1.84 and 0.16. Between them A rises by a factor of eleven in real terms
(£34 to £369) while the event stays roughly constant (£63 in the 1860s, £57 in 1982), so the
event/A ratio falls by the same factor of eleven. That is the physical content of the series, and
it is why the overhaul *share* must be allowed to fall.

The 2007-09 Class 158 figure is excluded from the series for the reason given in finding 10: it
buys a new interior as well as a C6, so it belongs with the Chiltern and Greater Anglia
refurbishments in [report 36](research-pricing-report-36.md) §6, not with periodic works
overhauls.

### 4.3 Annual mileage per carriage

| Date | Basis | Miles a vehicle-year | km a vehicle-year | Grade |
|---|---|---|---|---|
| 1892 | 3,650 passenger train-miles per LNWR carriage x 5-7 carriages a train | 18,000-25,500 | 29,000-41,000 | MEASURED input, DERIVED |
| 1961 | 229.6m passenger train-miles x 6-10 / 33,607 vehicles | 41,000-68,300 | 66,000-110,000 | MEASURED inputs, DERIVED |
| 1983 | Sprinter specification, 350,000 miles / 5 years | 70,000 | 113,000 | STATED |
| 2026 | modern long-distance duty assumed in report 43 | 150,000 | 241,000 | ESTIMATE (report 43) |

The 1892 and 1961 figures are train-miles multiplied by an assumed train length, and the train
length is the weak link: the sources give the numerator and the stock but not the average
formation. A 20 per cent error in train length moves the answer by 20 per cent. The modern band is
wide for the same reason: 70,000 miles is a design duty for a regional DMU, 150,000 miles is a
long-distance assumption.

### 4.4 Renewals

Hill's 2.53 per cent is the only measured carriage renewal rate in any era. It is an average of
ten companies whose individual rates run from 2.8 to 8.4 per cent, and the Midland's 6.4 per cent
is a rebuild programme rather than a steady state. The share of the gross maintenance figure that
renewals represent therefore ranges from 19 per cent (a £250 carriage) to 49 per cent (a £650
carriage) around the knowledge base's 35 per cent. Nothing found in this pass states a carriage
renewals share directly. Nothing found supports carrying the 35 per cent the whole way either:
the BR maintenance account lines and the modern ORR figures are net of capital. The 1961
Beeching functional line used in report 43 is the one exception on the way down — it is headed
"provision, maintenance, stabling and servicing" and report 43 §4 bounds its non-maintenance
content at 22 per cent — which is why the workbook phases the share out between 1961 and 1984
rather than stopping at 1922. `[DERIVED]`

## 5. Recommended rule for the workbook

The provision is the quantity to recommend, because it is what the measurements constrain: the
1860s point gives 1.84 / 6 = 31 per cent and the 1982 point gives 0.16 / 2 = 8 per cent. The
intermediate values are interpolated between those two anchors and are ESTIMATE.

| Era band | Interval (years) | Interval (km) | Overhaul provision, % of A | Event, x A | Basis | Rung |
|---|---|---|---|---|---|---|
| 1830-1890 | 6 | 210,000 | **28%** (band 15-31) | 1.68 | Lacy & Dow £62 = 1.84 A; Hill envelope forces 6-8 yr at 25% of capital; GER 5-yr paint | 1 (measured point, composition for n) |
| 1890-1922 | 5 | 180,000 | **24%** (band 15-30) | 1.20 | interpolated; GWR 1935 3.0-yr heavy as the lower bound | 3 |
| 1923-1947 | 3.0 | 165,000 | **19%** (band 15-25) | 0.57 | GWR 1935 measured interval; provision interpolated | 2 (interval) / 3 (share) |
| 1948-1975 | 2.0 | 176,000 | **12%** (band 8-18) | 0.24 | Hansard 2-yr interval; 1982 £2,000 = 0.16 A as the lower bound | 2 |
| 1975-2000 | 2.0 | 240,000 | **10%** (band 7-15) | 0.20 | 1978 annual works overhaul; 1982 measured 0.16 A | 2 |
| 2000-2026 | 2.6 | 294,000 | **8%** (band 6-12) | 0.21 | IET 950 days; 1982 measured point held; ORR gives no split | 3 |

**How to read the table.** `event = provision x interval x A(era)`, and the head is
`A - renewals - provision` (see the correction in §2). An 1860s vehicle priced on the 1900 rung
gives 0.28 x 6 x 33 = **£55** an event; a 1990 vehicle gives 0.10 x 2 x 460 = **£92**; a 2020
vehicle gives 0.08 x 2.6 x 440 = **£92**. The event is therefore nearly flat in real terms,
which is what the two measured points say it should be.

**Estimation-protocol rungs** (from [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md)):
rung 1 = measured on the class and the era; rung 2 = measured on the class, another era or another
company; rung 3 = composed from measured parts with a named assumption. No row here is rung 4 or 5.

**What would move each row.** A Midland composite price for the 1860s moves 1830-1890 (the £62
could be 12 per cent rather than 25 per cent of capital, but the event/A ratio is unaffected). A
GWR heavy-repair price for 1935 moves 1923-1947. A BR C1 outturn price moves 1948-1975. A modern
TSA schedule separating heavy maintenance from routine moves 1975-2026.

## 6. What this changes in the generator and the workbook

1. **`New/ai/cost-balancing/evidence_data.py` line 1103.** The tuple
   `'carriage': (0.08, 0.27, 3, 250000.0, 0.5, 0.35)` cannot carry six era bands; `overhaul_profile()`
   already receives `intro`, so the carriage branch needs a band lookup rather than a constant.
   The replacement named table should be
   `CARRIAGE_OVERHAUL = ((1830, 6.0, 210000, 0.28), (1890, 5.0, 180000, 0.24),
   (1923, 3.0, 165000, 0.19), (1948, 2.0, 176000, 0.12), (1975, 2.0, 240000, 0.10),
   (2000, 2.6, 294000, 0.08))`, read with `interp()` and held flat outside it. The event is then
   `provision * interval_years * CARRIAGE_MAINT_YR[era]`, **not** `capital * share`.
2. **The two share fields.** `initial_overhaul_cost` = 0.7 x the computed event and
   `max_overhaul_cost` = the computed event, with `overhauls_before_max_cost` = 3 and
   `overhaul_month_tenths` unchanged at 0.5. The 0.7 first-event ratio is an ESTIMATE, the same
   convention the wagon analysis adopted at 0.75; what it encodes is that the first works overhaul
   of a new vehicle is a paint-and-trim visit rather than a lift.
3. **Workbook, `New/cost-balancing-capital.xlsx`, sheet `Overhauls & upgrades`, columns 14-17.**
   Column 14 "Suggested first overhaul GBP" and column 15 "Suggested max overhaul GBP" take the
   two computed figures; column 16 "Overhauls to max" takes 3; column 17 "Interval km" takes the
   band's km (210,000 / 180,000 / 165,000 / 176,000 / 240,000 / 294,000). Column 18 "Downtime
   months" stays at 0.5 and column 19 "Suggested upgrade GBP" is untouched at 0.35 of capital.
   The basis string in column 24 must name this report and the interval's reference duty.
4. **`New/ai/cost-balancing/evidence_data.py` comment block, lines 1094-1100.** The sentence
   "Carriage: two-year cycle, 8 per cent first and 25-30 per cent late, the Midland 1860s overhaul
   being 25-28 per cent" is wrong on both numbers and must be replaced with the band table and
   the £62-is-12-to-25-per-cent caveat.
5. **`New/ai/vehicle-cost/maintenance-decomposition.md`, "Carriage overhaul by era".** The table's
   Victorian row (4-6 yr, 8-10% -> 25%) and BR Mk 1/2 row (8% -> 25-27%) both need the new
   intervals and the event/A formulation. Not changed in this pass.
6. **Report 36 §7 "Carriages, 1830-2026".** Its `initial_overhaul_cost` 8 per cent and
   `max_overhaul_cost` 25-30 per cent are shares of capital that no source supports once the
   identity is enforced; the 1982 measurement is 0.16 A. Not changed in this pass.

## 7. Error bars and assumptions

| Quantity | Central | Band | Why |
|---|---|---|---|
| Victorian interval | 6 yr | 5-8 | constrained by Hill's envelope, not measured |
| Victorian event / A | 1.68 | 0.9-1.84 | £62 on a £250 or a £500 carriage changes nothing in event/A, but the 1860s A is proxied by 1892 |
| Grouping interval | 3.0 yr | 2.5-4 | works capacity, not outturn; the GWR may have run fewer heavy repairs than it could |
| BR interval | 2 yr | 2-3 | Hansard says "approximately"; the 1965 code's renovation is at 9-11 years |
| BR event / A | 0.24 | 0.16-0.4 | £2,000 may be a light works overhaul, not a C1 |
| Modern interval | 2.6 yr | 2.6-5 | 950 days for the IET; 5 years / 350,000 miles for the Sprinter family |
| Annual km, 1892 | 35,000 | 29,000-41,000 | train length 5-7 assumed |
| Annual km, 1961 | 88,000 | 66,000-110,000 | train length 6-10 assumed |
| Renewals share | 35% | 19-49% | ten-company range and carriage price range |

**Structural assumptions.** (i) The 1860s event is compared with an 1892 annual total; if the
1860s total was lower in real terms, the Victorian provision is understated. (ii) The 1982 event is
compared with an interpolated 1982 total; report 43 has no measured 1982 point. (iii) The
intermediate provisions are interpolated, not measured. (iv) The km column assumes a reference
duty, not the in-game duty; the engine triggers on distance only, so the generator must state
which duty it used.

## 8. Gaps

- **LNWR Wolverton repair accounts.** The National Railway Museum's Wolverton archive (GB 0756
  WOLV) holds the half-yearly "Reports to the Locomotive Committee" 1890-1921 with a separate
  "Repairs Account" (WOLV 1/5). That is the document that would give a pre-1923 heavy/light split
  and a per-carriage repair cost. Identified from the archive list; not readable online.
  **UNAVAILABLE.**
- **Midland Carriage & Wagon Committee returns.** Report 36 records that the six-monthly returns
  imply a nine-month works visit for wagons; the carriage equivalent, and the location of the
  returns, were not found. **UNAVAILABLE.**
- **A Midland composite carriage price for the 1860s.** Lacy & Dow p. 31 gives the £62 but not the
  carriage it was spent on. The £225-250 range is for "early carriages", which are smaller.
  A copy of Lacy & Dow vol. 1 in a library would settle finding 3 in one reading. **UNAVAILABLE.**
- **A pre-1900 carriage heavy-repair price other than Lacy & Dow.** The NER rebuilt 100 carriages
  in 1892 and the Midland rebuilt most of its stock between 1878 and 1887; neither company's
  rebuild price was found. **UNAVAILABLE.**
- **A BR C1 outturn price.** The 1982 York figure is the only BR works-overhaul price found, and
  its scope is not stated beyond "overhaul". A BREL or York Works schedule for C1-C6 would price
  each coded visit. **UNAVAILABLE.**
- **A modern heavy/routine split.** The ORR says the boundary varies by contract and publishes no
  split; no TOC or ROSCO document with a C4/C6 price as a share of the annual charge was found.
  **UNAVAILABLE.**
- **Hill's per-company renewal rates.** The OCR of Table XXIV is garbled in the percentage column;
  the 2.53 per cent average and the Midland 6.4 per cent are legible, the rest are not. A page
  image read would recover them. **UNAVAILABLE (partly).**
- **The 1961 train length.** Beeching gives train-miles and stock but not the average formation;
  a BR traffic-costing manual or the 1961 load-factor tables would replace the 6-10 assumption.
  **UNAVAILABLE.**
