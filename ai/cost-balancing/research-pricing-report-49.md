---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 49 - Municipal tramcar maintenance, 1950-1990

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-49.csv`. No workbook, `.dat` file or
existing document was changed.

This pass answers the question left open by [report 47](research-pricing-report-47.md) section 8:
whether a measured municipal tramcar maintenance figure exists for 1950-1990, to replace the
ESTIMATE of GBP 150 a car-year (band 120-250) that the workbook uses for tram introduction years
1960-1990. The figure feeds the tram class's annual maintenance total **A**, which is decomposed
under [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md) standing rule 0:
the continuous head and the overhaul events must together charge the source figure, never the
figure plus a component of it. The terms used below are defined in section 2.

## 1. What this pass found

1. **A measured municipal car-only repair rate survives for 1938-39 to 1949-50.** Sheffield
   Corporation Tramways' revenue accounts print a "Cars" line inside Repairs at **1.511d a
   car-mile in 1938-39, rising to 4.128d in 1949-50**. Nine years are transcribed in section 3
   (1938-39 to 1949-50, with 1940-41 to 1942-43 missing). The line covers cars and their
   equipment only: permanent way, electrical equipment of line, buildings, workshops and tools,
   and other rolling stock are separate lines of the same table. **MEASURED**
   [LITERATURE:https://hull-repository.worktribe.com/output/4212086].

2. **The Sheffield line excludes renewals.** The same accounts carry a separate Renewals
   appropriation (GBP 120,000 a year for the trams from 1949-50) and a renewal fund whose
   recorded spending is on permanent way. The "Cars" line is therefore a **repairs-only** head,
   not the Ministry of Transport's "General Repairs and Maintenance (or Renewals out of
   Revenue)" head, which contains revenue renewals. **MEASURED line; STATED composition.**

3. **In 1900 money the measured rate is GBP 102.5 a car-year in 1938-39 and GBP 147.3 in
   1949-50**, at the reference duty of 48,000 km (29,800 miles) a car-year and the `general`
   series of `New/config/prices.tab`. The real rise over the eleven years is 44 per cent; the
   rise from 1945-46 is 31 per cent. **DERIVED.**

4. **The measured 1949-50 value almost equals the workbook's rung, but not on the same basis.**
   GBP 147.3 against GBP 150. The workbook deducts 35 per cent for renewals from its GBP 150,
   leaving GBP 97.50 in the maintenance fields; the measured GBP 147 already excludes renewals,
   so like for like the workbook's net figure is 34 per cent low. **DERIVED.**

5. **No Ministry return later than 1949-50 was found.** The national statutory series is the
   "Tramways and trolley vehicle undertakings" return. The New York Public Library bound set runs
   1929/30 to 1949/50 in one volume, no later volume is held digitally by the Internet Archive,
   HathiTrust or the Stationery Office collections searched, and the 1949-50 volume itself is
   search-only at HathiTrust. **UNAVAILABLE**, with the caveat that a copyright library may hold
   later paper volumes.

6. **No measured car-only maintenance figure for 1950-1990 was found in any accessible source.**
   The operator accounts that contain one are archival and undigitised: Glasgow Corporation
   Transport Department annual reports 1945-1972 (Mitchell Library, D-TR and D-TC series),
   Sheffield Transport annual reports 1944/45-1962/63 (HathiTrust search-only), and the Blackpool
   accounts to 1990 (no digitised run found). **UNAVAILABLE; negative result after the archives in
   section 7 were checked.**

7. **The measured series is a single operator's, not a national average.** Sheffield ran about
   440 cars in 1938-39 and about 450 in 1949-50, at about 32,700 and 29,000 miles a car-year.
   Its 1938-39 rate was 16 per cent above the national car-only rate derived in report 47
   (GBP 102.5 against GBP 88-89 in 1900 money), and its 1949-50 rate 12 per cent above the
   national chain (GBP 147.3 against GBP 131). Sheffield was hilly, intensively worked and ran a
   large fleet, so its costs sit at the upper end of the municipal range. **DERIVED.**

8. **The network contracted to one operator.** Great Britain had 2,907 tramcars in service in the
   early 1950s and 333 in 1961; Glasgow closed in 1962 and Blackpool was the only traditional
   street tramway left in mainland Britain. From 1962 to 1990 the rung describes Blackpool's
   fleet alone, of the order of 70-100 cars. **MEASURED (fleet count); DERIVED (the rest).**

9. **The GBP 150 rung stands as a central value, but its scope must be declared repairs-only.**
   Section 5 recommends holding GBP 150, band **130-210**, with renewals provision **0** and the
   overhaul provision rescaled to **28 per cent** so that the measured 0.55A event is preserved.
   **ESTIMATE constrained by the measured 1949-50 level.**

## 2. Method

- **Deflator.** Every nominal figure is converted with the `general` series in
  `New/config/prices.tab` (1900 = 100). Values used: 1938 183; 1939 188; 1943 270; 1944 277;
  1945 285; 1946 293; 1947 314; 1948 338; 1949 348; 1950 359; 1960 534; 1962 576; 1990 5,408.
  **Convention:** a financial year beginning in calendar year Y is deflated at the index for Y,
  so 1938-39 uses 183 and 1949-50 uses 348, matching report 47's treatment of 1949-50 (report 47
  used 188 for 1938-39, which moves that year by 2.7 per cent). `prices.tab` states that vehicle
  maintenance stays on the general index.
- **Grades.** **MEASURED** = an account, return, contract or published total with a stated scope.
  **STATED** = a trade, academic or witness statement of a rate or an event without the
  underlying account. **DERIVED** = arithmetic from a measured or stated figure, with the chain
  shown. **ESTIMATE** = judgement, used only where no measurement exists and marked in every
  table. **UNAVAILABLE** = identified but not readable or not verifiable.
- **The car-only head.** The Ministry of Transport return's "Cars and other Rolling Stock"
  column within "General Repairs and Maintenance (or Renewals out of Revenue)": repairs and
  renewals charged to revenue of cars and their equipment. Permanent way, line electrical
  equipment, power, traffic expenses, rates, insurance and general expenses are outside it.
  Trailers count as cars.
- **Repairs-only.** A head that covers repairs and maintenance of cars and their equipment but
  **not** renewals: renewals are charged to a separate renewal fund or to capital. This is the
  scope of the Sheffield "Cars" line, and it is a narrower scope than the Ministry car-only head.
- **A** is the annual maintenance figure per car-year in 1900 money at the reference duty. A
  **works overhaul** is a periodic visit to a workshop at which the car is stripped, its trucks
  and motors are exchanged or reconditioned, and the body is repaired and painted; it is charged
  to maintenance and is therefore inside a repairs-only head unless the source says otherwise.
  **Renewals** are replacements of life-expired components or whole cars charged to a renewal fund
  or to capital rather than to the repairs account.
- **Denominators.** A **car-mile** is one tramcar run one mile; trailers count as cars in the
  Ministry returns. A **car-year** is one car in stock for a year. The **reference duty** is
  48,000 km (29,800 miles) a car-year for the historic series. The conversion from pence a
  car-mile to pounds a car-year at the reference duty is 1d x 29,800 / 240 = **GBP 124.17**.
- **Sourcing.** Every page relied on was read: the Buckley thesis through its PDF text layer and,
  for the rotated tables, through page images rendered from the PDF; the *Annual Abstract of
  Statistics* through the Internet Archive text layer; the *Commercial Motor* articles through
  their full pages. A search result was not treated as evidence. No `.dat` value and no pakset
  price is used as evidence anywhere in this pass.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1938-39 | Sheffield Corporation Tramways, Cars line within Repairs | 1.511d a car-mile | Cars and equipment in; permanent way, electrical equipment of line, buildings, workshops and tools, other rolling stock out; renewals out | car-mile | MEASURED | Buckley 1987, Appendix S15, thesis p. 487 |
| 2 | 1939-40 | as row 1 | 1.574d | as row 1 | car-mile | MEASURED | as row 1 |
| 3 | 1943-44 | as row 1 | 2.207d | as row 1 | car-mile | MEASURED | as row 1 |
| 4 | 1944-45 | as row 1 | 2.320d | as row 1 | car-mile | MEASURED | as row 1 |
| 5 | 1945-46 | as row 1 | 2.578d | as row 1 | car-mile | MEASURED | as row 1 |
| 6 | 1946-47 | as row 1 | 2.912d | as row 1 | car-mile | MEASURED | as row 1 |
| 7 | 1947-48 | as row 1 | 3.438d | as row 1 | car-mile | MEASURED | as row 1 |
| 8 | 1948-49 | as row 1 | 3.846d | as row 1 | car-mile | MEASURED | as row 1 |
| 9 | 1949-50 | as row 1 | 4.128d | as row 1 | car-mile | MEASURED | as row 1 |
| 10 | 1938-39 and 1949-50 | Sheffield total Repairs (all sub-heads) | 2.459d and 6.322d | permanent way, electrical equipment, buildings, workshops and tools, cars, other rolling stock | car-mile | MEASURED | as row 1 |
| 11 | 1949-50 | Sheffield total working costs | 24.376d | all working heads including superannuation and sickness payments | car-mile | MEASURED | as row 1 |
| 12 | 1938-39 and 1949-50 | Share of repairs (cars + track) in total working costs | 17.90 and 22.81 per cent | (Cars + permanent way) / total working costs | per cent | DERIVED | Rows 1, 10, 11; Buckley p. 360 states both percentages independently |
| 13 | 1949-50 | Sheffield car-miles and fleet | about 13.0 million car-miles; about 450 cars (443-459) | derived from the printed working cost and cost per car-mile; cars in stock at the year end | car-miles, cars | DERIVED / MEASURED | Buckley Appendix S3, pp. 460-61 |
| 14 | 1938-39 and 1949-50 | Sheffield car-miles per car | about 32,700 and 29,000 miles | 14,468,290 / 442; 13.0m / about 450 | miles a car-year | DERIVED | Buckley Appendix S3, pp. 460-61 |
| 15 | 1949-50 | Glasgow Corporation Transport, trams, total working expenses | 22.29d a car-mile | all working heads; not a car-only repairs figure | car-mile | STATED | *Commercial Motor*, 11 Aug 1950, p. 38 |
| 16 | 1961-62 | Glasgow Corporation Transport, trams, operating result | loss of GBP 513,148 | whole tramway account; not a maintenance figure | tram-year | MEASURED | *Commercial Motor*, 17 Aug 1962, p. 34 |
| 17 | 1961 | Great Britain, tramcars in service | 333 | undertakings open for traffic | cars | MEASURED | *Annual Abstract of Statistics* 1962, Table 233, p. 185 |
| 18 | 1949-50 | Ministry of Transport, tramways and trolley vehicle undertakings return | not read | national car-only head | fleet-year, car-mile | UNAVAILABLE | HathiTrust record 103185290, holdings 1929/30-1949/50 |
| 19 | 1945-1972; 1944/45-1962/63; 1949-50 to 1990 | Glasgow Corporation Transport Department, Sheffield Tramways Committee and Blackpool Corporation Transport accounts | not read | revenue accounts by head | - | UNAVAILABLE | Glasgow City Archives D-TR and D-TC; HathiTrust record 103009915; no digitised Blackpool run found |

Sources: Buckley 1987 (thesis, Appendix S15 at p. 487, read from page images of the rotated scan;
PDF at https://hull-repository.worktribe.com/output/4212086, and the copy read at
https://web.archive.org/web/20250123094436/https://hull-repository.worktribe.com/OutputFile/4212090);
*Annual Abstract of Statistics* No. 99, 1962, Table 233,
https://archive.org/details/annual-abstract-of-statistics-gb_1962_99; *Commercial Motor*,
11 August 1950, p. 38, 19 September 1952, p. 62 and 17 August 1962, p. 34
(https://archive.commercialmotor.com); HathiTrust records 103185290 and 103009915
(https://catalog.hathitrust.org); Glasgow Life, "Ask the Archivist - Glasgow trams",
https://www.glasgowlife.org.uk/libraries/family-history/stories-and-blogs-from-the-mitchell/ask-the-archivist/ask-the-archivist-glasgow-trams.

Two checks on the transcription. First, the sub-heads of the Repairs block sum to the printed
total in every year used: for 1938-39, 0.630 + 0.259 + 0.046 + 0.002 + 1.511 + 0.011 = 2.459;
for 1949-50, 1.427 + 0.430 + 0.308 + 0.029 + 4.128 = 6.322. Second, the ratio of repairs to
total working costs computed from rows 1, 10 and 12 reproduces the 17.90 and 22.81 per cent
stated in the thesis text, which confirms that the line read as "Cars" is the one the author
uses. Two annual totals disagree with the sum of their sub-heads by 0.007d (1944-45) and 0.020d
(1947-48), within the OCR uncertainty of the scan.

## 4. The series

### 4.1 The measured Sheffield series, nominal and in 1900 money

All values are the "Cars" line, at the reference duty of 48,000 km (29,800 miles) a car-year.
"1900 money" is the nominal pence per car-mile divided by the general index (1900 = 100).

| Financial year | Nominal (d a car-mile) | General index | 1900 money (d a car-mile) | 1900 money (GBP a car-year) | Grade |
|---|---|---|---|---|---|
| 1938-39 | 1.511 | 183 | 0.826 | 102.5 | MEASURED |
| 1939-40 | 1.574 | 188 | 0.837 | 104.0 | MEASURED |
| 1943-44 | 2.207 | 270 | 0.817 | 101.5 | MEASURED |
| 1944-45 | 2.320 | 277 | 0.838 | 104.0 | MEASURED |
| 1945-46 | 2.578 | 285 | 0.905 | 112.3 | MEASURED |
| 1946-47 | 2.912 | 293 | 0.994 | 123.4 | MEASURED |
| 1947-48 | 3.438 | 314 | 1.095 | 136.0 | MEASURED |
| 1948-49 | 3.846 | 338 | 1.138 | 141.3 | MEASURED |
| 1949-50 | 4.128 | 348 | 1.186 | 147.3 | MEASURED |

At Sheffield's own duty of about 29,000 miles a car-year in 1949-50 the figure is about GBP 143;
the reference duty adds about 3 per cent.

### 4.2 The 1949-50 cross-check
The national chain gives 3.69d a car-mile, **GBP 131** in 1900 money (report 47); the Sheffield
measurement gives 4.128d, **GBP 147.3**. The two bracket the 1949-50 level at GBP 131-147. The
workbook's gross GBP 150 sits just above the top of that range; its net GBP 97.5 sits a third
below the bottom of it.

### 4.3 The 1950-1990 series

| Period | Operator | Figure | Grade |
|---|---|---|---|
| 1950-1960 | Sheffield | no car-only figure after 1949-50 in the transcribed source; fleet falls from about 450 to 60 cars and car-miles from 13.0m to 2.7m | UNAVAILABLE |
| 1960-1962 | Glasgow, Sheffield, Blackpool | no car-only figure found; Glasgow's trams lost GBP 513,148 in 1961-62 on the whole account | UNAVAILABLE |
| 1962-1990 | Blackpool | no car-only figure found; fleet of the order of 70-100 cars; tram mileage fell from 3.3m in 1959 to 1.2m in 1970 | UNAVAILABLE |
| 1960-1990 | all | **GBP 150 (130-210)** recommended rung, repairs-only, 1900 money, 48,000 km | ESTIMATE constrained by the measured 1949-50 level |

## 5. Recommended treatment for the workbook

**The rung.** Hold the 1960-1990 level at **GBP 150 a car-year**, band **130-210**, repairs-only,
in 1900 money at 48,000 km. The central value is supported by the measured 1949-50 figure of
GBP 147.3 and the national chain of GBP 131; nothing measured shows a fall between 1950 and 1990,
and the falling utilisation and ageing fleet of the surviving operators point upward. The bottom
of the band is the national-chain 1949-50 value; the top allows for the higher unit costs of a
single small fleet.

**The scope must be declared.** The figure is a **repairs-only** head: cars and their equipment,
routine repairs and works overhauls inside, renewals outside, and permanent way, line electrical
equipment, power, traffic, rates, insurance and general expenses outside. The measured Sheffield
line is the only post-1945 municipal figure and has this scope; writing "gross of renewals" beside
GBP 150, as report 47 does, describes a different head.

**Renewals provision: 0 per cent.** A renewals deduction is taken only where the source says
renewals are inside the figure ([source-composition](../vehicle-cost/source-composition.md)).
The Sheffield accounts put them outside, in a separate appropriation of GBP 120,000 a year whose
recorded spending is on permanent way. Deducting 35 per cent from GBP 150 would remove GBP 52.50
that the figure never contained and leave GBP 97.50 against a measured GBP 147.30.

**If the workbook instead keeps the gross-of-renewals definition, the rung must be restated.**
The equivalent gross figure at a 35 per cent renewals share is 147.3 / 0.65 = **GBP 226**
(band 200-320). No measured gross figure exists after 1939 for that reading, so the repairs-only
reading is preferred: it rests on a measurement.

**Overhaul provision: 28 per cent of the rung, at three years.** Report 47's 18 per cent was a
share of a gross figure containing renewals, and its mean event of 0.55A was measured against
that gross A. On a repairs-only base of 0.65A the same event is 0.55 / 0.65 = 0.846 of the base,
so at a three-year interval the provision is **28 per cent** (band 22-38):

```
A (repairs-only)            = 150
renewals provision          =   0
overhaul provision          =  42   (28 per cent of A, three-year interval, mean event 0.85A)
routine head                = 108   (72 per cent of A)
```

The engine fields take the routine head split into `fixed_cost` and `runningcost` on the
standing-share basis in [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md)
"Trams and light rail" (40-55 per cent standing), and the overhaul fields take the initial and
maximum events that produce the GBP 42 a year provision.

**The 1984 worked example under this treatment.** A = GBP 150, overhaul provision GBP 42,
routine head GBP 108, total charged GBP 150. The present workbook charges GBP 64 of maintenance
plus GBP 283 a year of overhaul, GBP 347 in total: the recommended total is 57 per cent lower and
the recommended overhaul provision is one seventh of the present one. The GBP 283 a year is 2.1
per cent of a GBP 13,352 capital value (6.4 per cent over a three-year cycle), against a
measured mean works overhaul of about GBP 127 every three years. Rescaled to the repairs-only
base, report 47's ladder is 0.54A for the first overhaul (GBP 81) rising to 1.15A for the
late-life overhaul (GBP 173), mean 0.85A (GBP 127).

**Do not double-count the rebuilds.** The 1934 London County Council E/1 rebuild at 20-27 per
cent of a new car and the 2026 Supertram life extension at 43-50 per cent remain
`upgrade_price` values (report 47 section 5). They are not part of A.

## 6. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| Sheffield 1938-39 rate | GBP 102.5 | 99-106 | Deflator convention (183 or 188); OCR of the scanned table |
| Sheffield 1949-50 rate | GBP 147.3 | 143-152 | Own duty 29,000 vs reference 29,800 miles; OCR |
| National 1949-50 chain | GBP 131 | 115-150 | Report 47: Sheffield percentage change applied to a national base |
| 1960-1990 rung | GBP 150 | 130-210 | Measured 1949-50 level; no post-1950 measurement; small-fleet penalty at the top |
| Renewals provision | 0 per cent | 0-35 | 0 on the measured repairs-only scope; 35 only if the rung is restated gross |
| Overhaul provision | 28 per cent | 22-38 | 0.85A mean event at 3 years; interval unmeasured for 1950-1990 |
| Overhaul interval | 3 years | 2-4 | Report 47; the only measured municipal interval is the LCC's 2 years to 1939 |

**Structural assumptions.** (i) The Sheffield line is taken as representative of municipal
practice although it is one operator 12-16 per cent above the national average. (ii) The
48,000 km reference duty is a modelling choice; Sheffield's own 1949-50 duty was about 3 per
cent lower. (iii) The exclusion of renewals rests on the accounts' separate renewal appropriation
and the thesis's attribution of the fund to permanent way, not on an itemised statement that no
car renewal passed through the repairs line. (iv) The works overhaul is assumed to be inside the
Sheffield repairs line; if it were outside, the total charged would rise by the provision.
(v) The 1960-1990 figure is held flat in real terms; the unmeasured influences point upward,
which is why the band is asymmetric.

## 7. Gaps and routes

- **The 1949-50 Ministry return is the nearest national measurement and has not been read.** It
  would fix the national car-only rate for the last year of the statutory series and test the
  GBP 131 chain. Route: British Library or National Library of Scotland (paper), or the New York
  Public Library copy behind HathiTrust (search-only).
- **The Sheffield series stops in 1949-50 although the undertaking ran trams until 1960.** The
  annual reports for 1949-50 to 1962-63 carry the same "Cars" line and would give eleven more
  measured years, including the 1950s when the fleet halved. Route: Sheffield Archives; the
  University of Illinois copy is search-only at HathiTrust.
- **Glasgow is the largest municipal fleet and is entirely unmeasured here.** The annual reports
  1945-1972 are in the Glasgow City Archives (D-TR and D-TC series); one year's revenue account,
  1955 or 1960, would give a large-fleet comparator and a measured 1960 anchor. Route: Mitchell
  Library, Glasgow.
- **Blackpool is the only operator for 1962-1990 and no account has been read.** Route: Blackpool
  Central Library local studies, or The National Archives for departmental correspondence about
  the tramway's finance.
- **No measured works-overhaul interval for 1950-1990.** The three-year interval is report 47's
  estimate. Glasgow's Coplawhill and Sheffield's Queens Road records would settle it; the National
  Tramway Museum catalogue lists Sheffield "Summary of repairs done by day staff, 1957-1959".
- **No measured renewals share for an electric tramcar.** The zero provision is a scope decision,
  not a measured zero: it says that the Sheffield figure excludes renewals, not that electric
  tramcars needed no renewal. A car account separating repairs from revenue renewals would test
  the gross reading.
- **The 1949-50 national fleet and car-mileage were not read.** They would convert the national
  car-only total to a per-car-year figure and remove the 12,000-16,000 car range that report 47
  used for 1919-20.

## Open questions

- Does the workbook's tram row keep the Ministry's gross-of-renewals definition, or move to the
  repairs-only definition that the only post-1945 measurement supports?
- Is the works overhaul inside the Sheffield "Cars" line? The accounts are silent; an itemised
  Queens Road account would settle it and would move the split without changing the total.
- Should the 1962-1990 rung be Blackpool-specific rather than a municipal average?
