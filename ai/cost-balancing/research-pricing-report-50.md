---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 50 — Locomotive maintenance, 1914-1948 and after 1977

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-50.csv`. No workbook, `.dat` or
existing document was changed.

This pass closes the two gaps left by [research pass 46](research-pricing-report-46.md), the
locomotive maintenance ladder: a measured annual locomotive maintenance figure for 1914-1948,
and a measured annual figure after 1977. It is the third pass in the locomotive series, after
report 46's ladder and the composition work in [report 43](research-pricing-report-43.md),
[report 44](research-pricing-report-44.md) and
[source-composition](../vehicle-cost/source-composition.md). The governing rule remains
standing rule 0 of [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md):
the measured total is the envelope, and no component of it may be charged a second time.

> **Correction, 2026-11-25.** The Class 92 is a mixed-traffic locomotive: the pakset object
> `BR-Class92` has `freight=None`, so it can work passenger or freight trains. The 2018
> Alstom/GB Railfreight contract is for 12 locomotives on the Caledonian Sleeper, a low-mileage
> passenger duty. The report's "electric passenger" label describes that measured duty, not the
> class's traffic capability. The GBP 868 is therefore a class/duty override, not a clean anchor
> for an electric-passenger track.

## 1. What this pass found

1. **The 1914-1948 gap is closed by the Ministry of Transport's annual *Railway Returns*.**
   The statutory summary table carries a line "Maintenance and Renewal of Rolling Stock —
   (1) Locomotives" for every railway company in Great Britain. For 1930 the line is
   **£11,168,381** on **22,751 traffic locomotives**, or **£490.9 an engine-year** (one
   locomotive in stock for a year). Deflated at the general index 188, that is **£261 in 1900
   money** (nominal pounds divided by the general index, 1900 = 100). The 1923 and 1930 volumes
   of the same return give 1913, 1919-1922 and 1927-1930. The 1927-1929 totals are printed as
   such; the 1930 total is the printed steam sub-head less the printed engine-power credit, the
   same arithmetic the 1929 volume prints in full for 1927-1929. **MEASURED (1913, 1919-1922,
   1927-1929); MEASURED inputs, DERIVED total (1930).**

2. **The stable interwar level is £249-£261 in 1900 money, and the existing ladder already
   passes through it.** The ladder is 215 / 306 / 800 / 2,100 / 1,045 / 520 in 1900 money per
   engine-year at 1900 / 1950 / 1961 / 1977 / 1995 / 2020, read log-linearly between the points.
   The stable measured points are 1927 £254, 1928 £249, 1929 £261 and 1930 £261; 1913 is £240
   and 1922 is the post-war high at £286. The ladder's log-linear interpolation between 1900
   (£215) and 1950 (£306) gives £236 at 1913 and £260-£266 at 1927-1930. The fit is within 5
   per cent in every stable year and within 2 per cent at 1913. **DERIVED from MEASURED.**

3. **The early 1920s sit above the ladder, and 1920-1921 are an abnormal spike.** The measured
   points are 1919 £274, 1920 £316, 1921 £398 and 1922 £286. The ladder gives £246-£251 over
   the same years, so 1919 and 1922 are 11-14 per cent high and 1920-1921 are 28-60 per cent
   high. The 1921 figure is a strike and deflation year (nominal repairs rose 14 per cent while
   the general index fell from 275 to 251), and the 1920-1921 figures are arrears of repairs
   being worked off. They are recorded, not adopted as rungs. **MEASURED; interpretation
   DERIVED.**

4. **The 1938 cross-check is £260, within 8 per cent of the ladder.** The *Statistical
   Abstract* gives £21,606,213 for the whole rolling-stock maintenance head in 1938, and the
   *Summary Table of Statistical Returns* gives 19,646 steam locomotives. The 1930 locomotive
   share of the rolling-stock head was 43.23 per cent; holding that share gives £9,340,938, or
   £475.5 an engine-year, or **£260 in 1900 money**. The direct 1938 Abstract B(1) figure was
   not readable, so this is **DERIVED**, not measured. **MEASURED inputs, DERIVED allocation.**

5. **The whole 1914-1948 series is gross of renewals and net of engine power.** The statutory
   head contains complete renewals and repairs and partial renewals, both charged to revenue.
   Fuel, water, lubricants, the wages of drivers and firemen and running-department
   superintendence sit in Abstract C ("Locomotive Running Expenses"), not in Abstract B. Capital
   and depreciation are outside. The detailed account deducts "engine power supplied to and by
   the company" before arriving at the net head; the 1930 deduction is £520,503. **MEASURED
   scope.**

6. **The ladder changes composition at 1950, and the change is worth about a quarter of the
   figure.** The 1900 and 1914-1948 points are gross of renewals; the 1950 Southern Region
   (British Railways' Southern Region) point of £1,100 (£306) is repairs only. On a gross basis
   the 1950 equivalent is **£408** (306 / 0.75, a 25 per cent renewals share of the gross). The
   gross level rises from about £260 at 1938 (derived) to £408 at 1950 (the stated figure
   grossed up), a real rise of 57 per cent; the net level rises from about £195 to £306, the
   same 57 per cent. The ladder's 281 (1938 interpolation) to 306 (1950) shows only 9 per cent,
   because it compares a gross 1938 figure with a net 1950 figure. **DERIVED.**

7. **The post-1977 gap is closed by a measured full-maintenance contract.** Alstom's press
   release of 17 April 2018 states that it will provide "full maintenance support for 12
   Class 92 locomotives" (a large mixed-traffic electric locomotive) for twelve years
   "in a contract worth around £15 million", awarded by GB Railfreight for the Caledonian
   Sleeper, the London-Scotland overnight service. That is **£1.25m a year for 12 locomotives =
   £104,167 a locomotive-year**, or **£868 in 1900 money** at the general index 11,999.
   **MEASURED** (a contract with a stated scope and value). The release also says the
   arrangement covers carriage and locomotive maintenance; the £15m is read as the locomotive
   contract because the 12 locomotives are the stated subject, and a whole-train reading would
   leave an implausibly small residual for the 40-odd sleeper coaches. If the coach work is
   inside the £15m, £868 is an upper bound. The release does not itemise the heavy/routine
   split; the 12-year term and "full maintenance support" wording are read as including the
   heavy overhauls. If the heavy events are outside, £868 is a floor.

8. **The Class 92 is 1.67 times the Class 66 rung, not half of it.** The 2020 Class 66 rung
   (the Class 66 is a 2000s freight diesel) is £520 in 1900 money. The measured Class 92 is
   £868, a ratio of **1.67**. The blanket "straight-electric locomotive takes 0.5 of the
   ladder" rule in report 46 is a 1977 result: Calder's Class 87 was 52 per cent of the
   Class 47 on the same passenger duty. It does not hold for a large modern mixed-traffic electric
   locomotive on a low-mileage sleeper duty. The modern ladder of £520 is a **Class 66
   freight-diesel** line, not a universal modern locomotive line. **DERIVED from two MEASURED
   figures.**

9. **The Class 92 level supports the 1995 rung and contradicts the size of the 1995-2020
   fall for large electric traction.** £868 is 17 per cent below the 1995 rung of £1,045,
   but 58 per cent above the ladder's 2018 interpolation of £550. The fall from £1,045 to £520
   is therefore a change of class generation (Class 47/87/92 to Class 66), not a general fall
   in the real cost of maintaining a locomotive. A large mixed-traffic electric locomotive of the
   Class 92 generation stays near £870-£1,045; a 2000s freight diesel sits at £520. **DERIVED.**

10. **No 1980s or 1990s locomotive-specific measured annual total was found.** The British
    Railways Board annual reports are catalogued as search-only on HathiTrust; the National
    Audit Office report on the sale of British Rail Maintenance Limited gives turnover and
    vehicle counts but no locomotive split; the Serpell Report gives total vehicle maintenance
    (£473m in 1982) and BREL's maintenance and repair turnover (£266m in 1981) but no
    per-locomotive figure. The 1995 rung therefore remains DERIVED. **UNAVAILABLE.**

## 2. Method

- **Deflator.** Every nominal figure is converted with the `general` series in
  `New/config/prices.tab` (1900 = 100): 1913 107; 1919 216; 1920 275; 1921 251; 1922 216;
  1927 196; 1928 196; 1929 193; 1930 188; 1938 183; 1950 359; 2018 11,999; 2020 12,521.
  `prices.tab` states that vehicle maintenance stays on the general index. The
  `vehicle purchase` series is not used anywhere in this pass.
- **Grades.** MEASURED = an account, return, contract or published total with a stated scope.
  STATED = a trade, academic or witness statement of a rate without the underlying account.
  DERIVED = arithmetic from a measured or stated figure, chain shown. ESTIMATE = judgement,
  used only where nothing measured exists and marked in every table. UNAVAILABLE = identified
  but not readable.
- **The engine-year.** One locomotive in stock for a year. The denominator is the number of
  traffic locomotives in the same return and year. Departmental locomotives are excluded from
  the count (a few dozen in 1913 and under 1 per cent of the fleet thereafter); the financial
  head includes their repairs, so the per-engine figure is overstated by well under 1 per cent.
  The returns cover Great Britain (England, Wales and Scotland); the Irish railways were
  separate and are outside the series, so the series is a Great Britain series, not a United
  Kingdom one.
- **Reference duty.** The ladder figures are per engine-year at each source's own duty, not at
  one common mileage: Hill's 20,164 train-miles an engine (32,450 km) for 1892; 113,000 km for
  Calder's Class 47; 1.6m km between rebuilds, or about 89,000 km a year, for the Class 66;
  and the Caledonian Sleeper duty for the Class 92, which the source does not quantify but
  which is a low-mileage overnight service. The 1914-1948 figures are fleet averages at the
  fleet's actual mileage. The workbook's locomotive rows use their own mean annual distance,
  and report 46's class overhaul profile uses 150,000 km for steam and 300,000 km for
  diesel/electric; the ladder is a per-engine-year level and is not rescaled to those duties
  in this pass.
- **The statutory head.** "Maintenance and Renewal of Rolling Stock — (1) Locomotives" is
  Abstract B(1) of the accounts prescribed by the Railway Companies (Accounts and Returns) Act
  1911. It contains complete renewals (in the company's shops and by contractors), repairs and
  partial renewals, and transfers to or from the renewal or suspense account. It is net of
  engine power supplied to and by the company. It excludes the running expenses in Abstract C
  (fuel, water, lubricants, stores, wages of drivers and firemen, running-department
  superintendence), capital expenditure, and depreciation as such. For 1913-1922 the figure is
  the summary line as printed; for 1927-1930 the detailed account shows the engine-power
  deduction explicitly, and the 1929 volume reproduces the 1929 summary figures exactly.
- **What "renewals" means here.** A complete renewal is a new locomotive in place of a
  scrapped one, charged to revenue through the renewal account. It is capital in economic
  substance. A partial renewal is a new boiler, firebox, cylinders or frames on an existing
  locomotive; it is a works overhaul and is inside the repairs line. Both are inside the
  measured totals, which is why the totals are described as gross of renewals.
- **The ladder.** The six-point series 215 / 306 / 800 / 2,100 / 1,045 / 520 in 1900 money per
  engine-year at 1900 / 1950 / 1961 / 1977 / 1995 / 2020, read log-linearly between the points
  and flat outside them, as recommended in [report 46](research-pricing-report-46.md) §5. The
  ladder is the object of the comparison, not evidence; no `.dat` price and no workbook figure
  is used as evidence anywhere in this pass.
- **Sourcing.** The Railway Returns volumes were read page by page through the HathiTrust
  text-only view (the catalogue records the volumes as full view; scripted access to
  `babel.hathitrust.org` is blocked and the pages were read through the search index's cached
  text). The 1929 *Railway Returns* was read as a control: its 1929 locomotive figures reproduce
  the 1930 volume's 1929 column exactly, which confirms the column alignment of the OCR. The
  1938-44 summary table and the 1934-38 *Statistical Abstract* were read from the Internet
  Archive text. Every page relied on was fetched and read.
- **Search record.** Sources checked and found not to yield a locomotive-specific annual
  total: the ORR 2026 rolling-stock maintenance review (passenger only, freight out of scope,
  no heavy/routine split); the Serpell Report (total vehicle maintenance and BREL turnover, no
  per-locomotive figure); the NAO report on the sale of British Rail Maintenance Limited
  (BRML) (turnover and vehicle counts, no locomotive split); the BRB annual reports
  (catalogued search-only); the *Railway Gazette
  International* 1998 Class 66/Class 47 article (event costs only); the *Modern Railways*
  volumes for 1978-1984 (not readable through the lending restriction); the Stadler Class 99
  full-service release (no value); and the Alstom Class 92 release (used, row 19). The Railway
  Clearing House statistical returns, the Institution of Locomotive Engineers and Institution
  of Mechanical Engineers cost papers, and the BR sector accounts were not read; they are
  listed as routes in §7.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1913 | Railway Returns 1923, Abstract B(1), all GB companies | £6,062,388 | repairs and renewals: complete renewals, repairs and partial renewals; running expenses, capital and depreciation out | 23,581 traffic locomotives | MEASURED | *Railway Returns … 1923*, p. 14 (https://babel.hathitrust.org/cgi/pt?id=uc1.c2628626&seq=18) and p. 20 (…&seq=24) |
| 2 | 1913 | per engine-year | £257.1; £240 in 1900 money | as row 1 | engine-year | DERIVED | row 1; index 107 |
| 3 | 1919 | Railway Returns 1923, Abstract B(1) | £14,426,221 | as row 1 | 24,368 locomotives | MEASURED | as row 1 |
| 4 | 1920 | Railway Returns 1923, Abstract B(1) | £21,370,861 | as row 1 | 24,620 locomotives | MEASURED | as row 1 |
| 5 | 1921 | Railway Returns 1923, Abstract B(1) | £24,343,454 | as row 1 | 24,392 locomotives | MEASURED | as row 1 |
| 6 | 1922 | Railway Returns 1923, Abstract B(1) | £14,987,374 | as row 1 | 24,235 locomotives | MEASURED | as row 1 |
| 7 | 1922 | per engine-year | £618.4; £286 in 1900 money | as row 1 | engine-year | DERIVED | row 6; index 216 |
| 8 | 1927 | Railway Returns 1929 and 1930, Abstract B(1) | £11,913,976 | as row 1; net of engine power supplied | 23,963 locomotives | MEASURED | *Railway Returns … 1929*, p. 15, https://babel.hathitrust.org/cgi/pt?id=uc1.c2628630&seq=19; *… 1930*, p. 17, https://babel.hathitrust.org/cgi/pt?id=uc1.c2628620&seq=23 |
| 9 | 1928 | as row 8 | £11,517,947 | as row 8 | 23,617 locomotives | MEASURED | as row 8 |
| 10 | 1929 | as row 8 | £11,806,662 | as row 8 | 23,404 locomotives | MEASURED | as row 8 |
| 11 | 1930 | as row 8 | £11,168,381 | as row 8; steam sub-head £11,688,884 less £520,503 engine-power credit | 22,751 locomotives | MEASURED inputs, DERIVED total | *… 1930*, p. 17, seq 23; stock p. 23, seq 29 |
| 12 | 1930 | per engine-year | £490.9; £261 in 1900 money | as row 11 | engine-year | DERIVED | row 11; index 188 |
| 13 | 1930 | Abstract B total, all rolling stock | £25,833,211 | locomotives, carriages, wagons and rail motors; as row 1 | whole fleet | MEASURED | *… 1930*, p. 16, https://babel.hathitrust.org/cgi/pt?id=uc1.c2628620&seq=22 |
| 14 | 1938 | Abstract B total, all rolling stock | £21,606,213 | as row 13 | whole fleet | MEASURED | *Statistical Abstract for the United Kingdom 1934-1938*, table 252, p. 335, https://archive.org/details/annual-abstract-of-statistics-gb_1934-1938_83 |
| 15 | 1938 | traffic locomotives | 19,646 steam; 13 electric; 43 petrol | traffic stock; departmental out | locomotives | MEASURED | *Summary Table of Statistical Returns of Railways of Great Britain 1938 to 1944*, Item 2 (locomotives), https://archive.org/details/railways00609131 |
| 16 | 1930 | locomotive share of Abstract B | 43.23% | rows 11 and 13 | ratio | DERIVED | rows 11 and 13 |
| 17 | 1938 | locomotive maintenance, derived | £9,340,938; £475.5 an engine-year; £260 in 1900 money | row 14 x row 16; 19,646 locomotives; index 183 | engine-year | DERIVED | rows 14-16 |
| 18 | 1950 | Southern Region steam locomotive repairs | £1,100; £306 in 1900 money | repairs only; renewals out; fleet average | engine-year | STATED | Warder discussion, *J. Instn Loco. Engrs* 41 (1951), https://steamindex.com/jile/jile41.htm; [report 46](research-pricing-report-46.md) row 19 |
| 19 | 2018 | Alstom / GB Railfreight Class 92 full-maintenance contract | about £15m over 12 years for 12 locomotives | full maintenance support; the release does not itemise the heavy/routine split; fuel, crew, capital and depreciation out | 12 locomotives | MEASURED | Alstom press release, 17 April 2018, https://www.alstom.com/press-releases-news/2018/4/alstom-wins-maintenance-contract-for-caledonian-sleeper-class-92-locomotives-from-wembley-depot; GB Railfreight, same date, https://www.gbrailfreight.com/gbrf-awards-alstom-maintenance-contract-for-caledonian-sleeper-class-92-locomotives-from-wembley-depot/ |
| 20 | 2018 | per engine-year | £104,167; £868 in 1900 money | as row 19 | engine-year | DERIVED | row 19; index 11,999 |
| 21 | 2020 | Class 66 annual total | £65,205; £521 in 1900 money | heavy event £312,984 every 12 years / 0.40 heavy share; running maintenance and capital out | engine-year | DERIVED | [report 46](research-pricing-report-46.md) row 48; Contracts Finder, 13 October 2020, https://www.contractsfinder.service.gov.uk/Notice/b0130cac-2720-44df-8b08-ad62146e60f3 |
| 22 | 2018 | Class 92 against Class 66 | 1.67 | row 20 / row 21 | ratio | DERIVED | rows 20-21 |
| 23 | 1977 | Class 87 against Class 47 | 52 per cent | same passenger duty; Calder's depot-cost statistics | ratio | MEASURED | [report 46](research-pricing-report-46.md) row 19; Calder, TRB Special Report 180 (1977), https://onlinepubs.trb.org/Onlinepubs/sr/sr180/180-011.pdf |
| 24 | 1913-1930 | measured level against the ladder | ratios 1.02 (1913), 1.11 (1919), 1.28 (1920), 1.60 (1921), 1.14 (1922), 0.98 (1927), 0.95 (1928), 0.99 (1929), 0.98 (1930) | rows 2, 7, 12 against the log-linear ladder | ratio | DERIVED | rows 2, 7, 12; [report 46](research-pricing-report-46.md) §5 |
| 25 | 1938 | measured level against the ladder | ratio 0.92 | row 17 against the ladder at 1938 (£281) | ratio | DERIVED | row 17 |
| 26 | 2018 | measured level against the ladder | ratio 1.58 | row 20 against the ladder at 2018 (£550) | ratio | DERIVED | row 20; [report 46](research-pricing-report-46.md) §5 |

## 4. The series and the comparison with the existing ladder

### 4.1 The 1914-1948 series

All figures are Great Britain, all railway companies, per traffic locomotive in stock. "1900
money" uses the `general` index. The ladder column is the log-linear interpolation of
215 (1900) and 306 (1950).

| Date | Nominal total | Locomotives | Per engine-year | Index | 1900 money | Ladder | Measured / ladder |
|---|---|---|---|---|---|---|---|
| 1913 | £6,062,388 | 23,581 | £257.1 | 107 | 240 | 236 | 1.02 |
| 1919 | £14,426,221 | 24,368 | £592.0 | 216 | 274 | 246 | 1.11 |
| 1920 | £21,370,861 | 24,620 | £868.0 | 275 | 316 | 248 | 1.28 |
| 1921 | £24,343,454 | 24,392 | £998.0 | 251 | 398 | 249 | 1.60 |
| 1922 | £14,987,374 | 24,235 | £618.4 | 216 | 286 | 251 | 1.14 |
| 1927 | £11,913,976 | 23,963 | £497.2 | 196 | 254 | 260 | 0.98 |
| 1928 | £11,517,947 | 23,617 | £487.7 | 196 | 249 | 262 | 0.95 |
| 1929 | £11,806,662 | 23,404 | £504.5 | 193 | 261 | 264 | 0.99 |
| 1930 | £11,168,381 | 22,751 | £490.9 | 188 | 261 | 266 | 0.98 |
| 1938 | £9,340,938 (derived) | 19,646 | £475.5 | 183 | 260 | 281 | 0.92 |
| 1950 | — | n/a | £1,100 (repairs only) | 359 | 306 | 306 | 1.00 |

The 1930 all-locomotive figure is the steam sub-head £11,688,884 less the £520,503 engine-power
credit. The 1929 *Railway Returns* shows the same subtraction for 1927-1929, and its results
reproduce exactly (1927 £12,431,292 - £517,316 = £11,913,976; 1928 £12,036,186 - £518,239 =
£11,517,947; 1929 £12,326,281 - £519,619 = £11,806,662), which is why the 1930 subtraction is
treated as a measured input with a derived total, not as an estimate.

The all-locomotive head includes the engine-power credit, which is largely an electric-traction
accounting adjustment. The steam-only net for 1930 is £11,688,884, or £513.8 an engine-year, or
£273 in 1900 money, 4.5 per cent above the all-locomotive £261. This report uses the
all-locomotive head because it is the statutory summary line on which the 1913-1922 and 1938
figures are also based; the steam-only figure is given here so that a reader who wants the pure
steam level can use it. The difference is inside the error band and does not change the
comparison with the ladder.

**What the series shows.** The real cost of keeping a locomotive in service was roughly flat
from 1913 to 1938 at £240-£286 an engine-year, with a post-war hump in 1919-1922 and a
measurable decline from 1922 to 1928. The 1938 figure is derived but sits exactly where the
trend of 1927-1930 would put it. The 1950 figure is a different composition (repairs only) and
is not on the same line; its gross equivalent is £408. The 1950 ratio of 1.00 is by
construction: it is the ladder's own anchor.

**The 1920-1921 spike.** The nominal locomotive head rose from £21.4m in 1920 to £24.3m in
1921 while the general index fell from 275 to 251. The railway companies were working short
time during the coal strike and the trade depression, and locomotives were laid up for
repairs; the 1922 figure falls back to £15.0m as traffic recovered. The 1921 point is a
genuine accounting figure but not a sustainable rate, and it is not used as a rung.

**The denominator.** The 1913-1922 counts are "traffic locomotives" from the same return;
the 1927-1930 counts are the same category. The 1938 count is steam traffic locomotives; the
13 electric and 43 petrol locomotives are excluded, which overstates the per-engine figure by
0.3 per cent. Departmental locomotives are excluded throughout, which overstates it by under
1 per cent.

### 4.2 The comparison with the ladder

The ladder was built in [report 46](research-pricing-report-46.md) from the pre-1900 measured
evidence (E. R. Hill's 1892 nineteen-company average at its head), a stated 1950 figure, and
derived 1961-2020 points. It had no point between 1900 and 1950. The measured 1913-1938 points
fill that interval and show that the interpolation is sound:

- **1913 and 1927-1930 fit within 5 per cent.** The ladder is not a straight line in real
  terms; it rises from 215 to 306 over fifty years, and the measured stable interwar level of
  249-261 is almost exactly the ladder's 260-266. The pre-1914 point at 240 is 2 per cent
  above the ladder's 236.
- **1919 and 1922 are 11-14 per cent above.** This looks like a real post-war premium, not
  noise: two independent years, one at the start and one at the end of the spike, sit at the
  same elevated level. A ladder that passed through 1922 would need a hump; the present
  log-linear line smooths it away. For a long-run cost series that is the right choice.
- **The early 1920s are the only material disagreement.** 1920-1921 are 28-60 per cent above
  the ladder, but they are strike and arrears years. If the workbook wants a measured anchor
  in the period, 1922 at £286 is the defensible one; it is 14 per cent above the ladder's
  £251. Adding it would raise every locomotive introduced between 1900 and 1950 by up to 14
  per cent on a log-linear read, which is not supported by the 1927-1938 evidence. The
  recommendation is therefore to record it, not to add it.

### 4.3 The post-1977 series

| Date | Item | Nominal | 1900 money | Grade |
|---|---|---|---|---|
| 1977 | Class 47, Calder | $69,100 = £39,599 | 2,118 | MEASURED + DERIVED |
| 1995 | British Rail Maintenance Limited (BRML) mixed fleet, x 2.0 locomotive-to-fleet / 0.40 heavy share | £66,667 | 1,045 | DERIVED |
| 1998 | Class 47 rebuild provision | £142,855 | 2,045 | DERIVED |
| 1998 | Class 66 rebuild provision | £27,778 | 398 | DERIVED |
| 2018 | Class 92 full maintenance contract | £104,167 | 868 | MEASURED |
| 2020 | Class 66 F-examination provision | £65,205 | 521 | DERIVED |

The 1995 row converts a mixed-fleet heavy-maintenance turnover into a locomotive total: the
£13,333 a vehicle-year from the BRML sale is multiplied by 2.0 for a locomotive against the
mixed-fleet average and divided by 0.40, the assumed heavy share of the annual total. The 2020
row is the DRS Class 66 12-yearly (F) examination, a heavy event, divided by the same 0.40
heavy share. The 0.40 is an ESTIMATE, not a measurement; report 46 §4.3 gives the reasoning.

The 2018 point is the only locomotive-specific measured annual total in the post-1977
series. It is 17 per cent below the 1995 rung and 58 per cent above the ladder's 2018
interpolation. The Class 66 point at 2020 is 40 per cent below the Class 92. The series
therefore has two modern levels, not one:

- **the Class 66 freight-diesel level of about £520**, which is the 2020 rung as it stands;
- **the large electric locomotive level of about £870**, which is the 2018 Class 92 contract.

The 1995 rung of £1,045 sits between them and is consistent with a mixed fleet in transition.
The fall from £1,045 to £520 is not a uniform real decline: it is the replacement of the
Class 47/87/92 generation by the Class 66. A large mixed-traffic electric locomotive of the Class 92
generation in 2018 still cost £868 to maintain, 83 per cent of the 1995 rung.

## 5. Recommended treatment

1. **Keep the ladder levels unchanged: 215 / 306 / 800 / 2,100 / 1,045 / 520.** The measured
   1913-1938 points validate the 1900-1950 interpolation within 5 per cent in every stable
   year. Do not add a 1922 rung; the 14 per cent hump is a post-war episode, and a log-linear
   ladder cannot hold it without distorting 1923-1949. Record the measured points in the basis
   text of the locomotive rows, not in the ladder. The measured totals are envelopes: the works
   overhauls and the renewals are inside them, so the overhaul provision and the renewals
   provision are deducted from them, never added.
2. **State the composition break at 1950 in every locomotive row's basis.** The 1900 and
   1914-1948 points are gross of renewals; the 1950 point is repairs only. If the workbook
   applies the 25 per cent renewals deduction to the pre-1961 rows, the 1950 rung must be
   entered as **£408 gross** (306 / 0.75) so that the deduction returns it to 306. If the
   workbook does not apply the deduction, the pre-1950 rows carry about 25 per cent of their
   total as renewals that the player also pays through the purchase price, so they over-charge
   by about a third relative to a net basis; the post-1950 rows are net and do not carry that
   excess, and the basis text must say so.
3. **Keep £520 at 2020 as the Class 66 freight-diesel rung.** It is a measured-and-derived
   Class 66 figure, not a universal modern locomotive figure. Do not apply it to a large
   electric locomotive on passenger or mixed-traffic duty.
4. **Add the measured Class 92 level of £868 at 2018 as a class-specific value.** Band
   £740-£1,000. It applies to a large mixed-traffic electric locomotive on a low-mileage sleeper
   duty, and it is the nearest measured analogue for a modern large electric locomotive on that
   duty. The £868 is an envelope: the 12-year full-maintenance term contains the heavy
   events, so the Class 92's overhaul provision is deducted from it, not added.
5. **Withdraw the blanket 0.5 electric factor for post-1995 electrics.** The 0.5 factor is
   Calder's 1977 Class 87/Class 47 result on high-mileage passenger duty. For a modern large
   mixed-traffic electric locomotive on that sleeper duty the measured ratio is **1.67** (band 1.3-2.0). The factor is
   a class factor, not a traction-type constant: 0.5 against the Class 47 for the Class 87
   generation, 1.67 against the Class 66 for the Class 92 generation.
6. **Read the modern ladder as two class tracks, not one time track.** The diesel/freight
   track is 2,100 (1977) → 1,045 (1995) → 520 (2020). The electric track is 1,103
   (1977, Class 87) → 1,045 (1995, mixed fleet) → 868 (2018, Class 92 on the Caledonian
   Sleeper, a passenger duty). The Class 92 is mixed traffic, so the 868 is a class/duty
   override, not a clean electric-passenger point. The workbook needs a
   class override only where a measured class figure exists; unmeasured classes take the
   nearest measured class of the same generation and duty.
7. **Do not interpolate the 2018 point as a time rung.** It is a class figure. The time
   ladder's 1995-2020 fall remains the diesel/freight line; the electric line is
   flat from 2018 and does not fall to 520.
8. **Update [report 46](research-pricing-report-46.md).** Its gap "no measured 1914-1948
   point" is closed by the evidence in §3, rows 1-17. Its gap "no measured UK annual total per
   locomotive after 1977" is partly closed by the Class 92 contract; the 1995 rung remains
   derived, but the 2018 measured point constrains the modern electric level. Report 46's
   ladder values and its finding 11 stand for the diesel/freight line; finding 14 is
   superseded for the large electric locomotive class.
9. **Do not change the 1995 rung.** £1,045 remains the best available mixed-fleet transition
   figure. The Class 92 at £868 is 17 per cent below it, which is a plausible real decline for
   a 1990s design maintained in 2018; it is not evidence for a fall to £520.

## 6. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| 1913-1930 national totals | per table | ±5-8% | account head, traffic-locomotive denominator, engine-power allocation, departmental locomotives |
| 1919-1922 | 274-398 | ±15% | post-war arrears, coal strike, deflation; 1921 is an outlier |
| 1938 derived | 260 | 235-285 | constant 1930 locomotive share (43.23%); 1938 total and stock measured; a 5-point share error moves the answer by 11% |
| 1950 gross equivalent | 408 | 383-437 | 25% renewals share of the gross, band 20-30% (383 at 20%, 437 at 30%) |
| 2018 Class 92 | 868 | 740-1,000 | "around £15m"; 12 locomotives; scope "full maintenance support"; low-mileage fleet overhead |
| Ladder fit, stable interwar years | 0.95-1.02 | ±10% | account definition and stock |
| Modern electric factor | 1.67 | 1.3-2.0 | one class, one contract, one duty |

**Structural assumptions.** (i) The 1913-1930 totals are fleet averages across main-line,
tank, shunting and small locomotives; the 1961+ ladder is a main-line series, so the
1914-1948 points are not like-for-like with the post-1961 rungs. (ii) The 1938 point is a
constant-share allocation, not a measured locomotive head. (iii) The 2018 Class 92 contract is
a single 12-locomotive fleet on a low-mileage duty; its fixed-cost overhead per locomotive is
higher than a 200-locomotive fleet's. (iv) The 1950 gross equivalent assumes the 25 per cent
renewals share measured for 1892; the interwar share may have been lower as renewals were
deferred.

## 7. Gaps and routes

- **Direct 1938 Abstract B(1).** The 1937-38 *Railway Returns* is catalogued as "Limited
  (search only)" on HathiTrust (record 100007368), not full view as report 46 recorded. A
  physical copy at The National Archives (the Ministry of Transport railway statistics papers)
  or the British Library would give the exact 1938 locomotive head and remove the constant-share
  assumption. Request: *Railway Returns 1938*, Abstract B(1), all companies; or the Ministry's
  *Summary Table of Statistical Returns 1938*.
- **1948 Railway Executive accounts.** The British Transport Commission's *Annual Report and
  Accounts 1948* and *Financial and Statistical Accounts 1948* would give the first
  nationalised year on the same head. The BTC annual reports are not on the Internet Archive;
  The National Archives (British Transport Commission papers) and the British Library hold
  them. This is the strongest remaining point for the end of the 1914-1948 gap.
- **1981-1994 British Railways Board annual reports.** HathiTrust record 000553686 lists them
  as search-only. The profit and loss account and notes should carry "maintenance of
  locomotives" or "repairs and renewals of locomotives" and the locomotive stock; the same
  volumes carry the sector accounts (InterCity, Railfreight, Network SouthEast), which may
  split traction maintenance by business. Request: *British Railways Board Annual Report and
  Accounts*, 1981/82 to 1993/94, at The National Archives (British Railways Board papers) or
  the British Library. This is the strongest remaining point for the 1980s-1990s.
- **The Serpell engineering annex.** The main report refers to a separate summary report by
  R. Travers Morgan and Partners, made available to the Secretary of State. It may contain
  locomotive unit costs that the main report does not. Route: Department for Transport
  library, The National Archives, or a freedom of information request.
- **The BRML sale documents.** The National Audit Office report gives the £180m turnover and
  the 13,500 vehicles but not the locomotive share. The Department of Transport's 1995 sale
  process for the six depots may have produced a prospectus or information memorandum giving
  the split by vehicle type. Route: The National Archives, rail archive.
- **Class 99 full-service contract value.** Stadler's April 2023 release gives 30 Class 99
  locomotives, a 16-year full-service contract and a new Leicester depot, but no value. The
  OJEU/TED award notice, or a freedom of information request to Beacon Rail or GB Railfreight,
  would give the per-locomotive annual figure and a second modern point.
- **Class 68 and other modern electric classes.** Direct Rail Services' wet-lease arrangements
  for the Class 68 are described in the trade press, but their values are not published. A
  franchise agreement schedule or a freedom of information request would test whether the 1.67
  electric ratio generalises beyond the Class 92.
- **The 1920-1921 spike.** The 1921 or 1922 *Railway Returns* introduction may comment on the
  coal strike, short-time working and arrears. The 1923 volume's introduction (read for this
  pass) discusses heavy repairs and the numbers under repair but not the cost spike. A Board of
  Trade or Ministry of Transport commentary would turn the interpretation in §4.1 from DERIVED
  into MEASURED.
- **The Railway Clearing House statistics.** The RCH's statistical returns may give
  repairs-and-renewals per engine-mile by company for the interwar years, which would provide
  a per-mile cross-check on the per-engine figures. Not read in this pass.

## 8. What this changes in the knowledge base

- [Report 46](research-pricing-report-46.md) §8 gap 2 ("no measured 1914-1948 point") is
  closed by §4.1 of this pass. Its gap 1 ("no measured UK annual total after 1977") is partly
  closed by the Class 92 contract; the 1995 rung remains derived.
- [Maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md) "Rail
  locomotives" should record the measured 1913-1938 level and the composition break at 1950,
  and should record the Class 92 measured level and the 1.67 modern electric ratio. The doc's
  current text says the ladder "rises to a 1970s peak and falls about fourfold to the Class 66
  generation"; that is correct for the diesel/freight line but not for a modern electric
  passenger locomotive, which falls only 17 per cent from 1995 to 2018.
- [Source-composition](../vehicle-cost/source-composition.md) should record that the
  Abstract B(1) head is gross of complete renewals and partial renewals and net of engine
  power supplied, and that the 1950 Southern figure is repairs only.
- No change to the ladder values is recommended. The measured points are evidence for the
  basis text and for the class overrides, not new rungs.
