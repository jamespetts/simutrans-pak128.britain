---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 47 - Tram maintenance and works overhauls, 1900-2026

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-47.csv`. No workbook, `.dat` or
existing doc was changed.

This pass answers the question left open by [report 37](research-pricing-report-37.md)
section 12: whether a municipal tramcar's annual repair and maintenance cost was about
£64 a car-year in 1900 money from 1900 to 1990, and what the measured overhaul events
were. It replaces the era-blind £64 and the capital-share overhaul with a dated gross
series and an overhaul provision expressed as a share of that series. The **generator**
is `New/ai/cost-balancing/evidence_data.py`, which produces the figures the workbooks
consume. The **workbooks** are `New/cost-balancing-maintenance.xlsx` and
`New/cost-balancing-capital.xlsx`.

## 1. What this pass found

1. **£64 is below the 1919-20 return's own arithmetic.** The Ministry of Transport
   return for 1919-20 gives £3,642,909 of local-authority car-only maintenance. At any
   fleet count between 12,000 and 16,000 cars, that is £228-£304 nominal a car-year,
   or £83-£111 in 1900 money at the general index 275. As a gross figure, £64 lies
   below that range. **MEASURED inputs, DERIVED.**

2. **The measured municipal car-only rate for 1923-1933 is 1.52-1.98d a car-mile.**
   In 1900 money that is 0.85-0.98d a car-mile, or £105-£121 a car-year at the
   reference duty of 48,000 km (29,800 miles). At the actual 1930-31 average of
   46,200 km, the 1930-31 return gives £102-£105 and the 1932-33 return gives £102.
   **MEASURED.** The head is "General Repairs and Maintenance (or Renewals out of
   Revenue)", Cars and other Rolling Stock column; it excludes permanent way, line
   electrical equipment, power, traffic expenses, rates, insurance and general
   expenses.

3. **The real level fell by about a quarter between 1923-24 and 1938-39.** The
   measured series is £121 (1923-24), £106 (1930-31), £107 (1932-33), £94 (1937) and
   £89 (1938-39) in 1900 money at 48,000 km. The shape is a post-1918 peak, an
   interwar fall and a plateau from 1930 to 1933. **MEASURED (1923-1933); DERIVED
   (1937-1939).**

4. **The post-war real level rose 41 per cent by 1949-50.** Sheffield's tramcar
   repairs rose 173.2 per cent in nominal terms between 1938-39 and 1949-50, against
   a general index rise of 92.3 per cent (181 to 348). The real increase is 1.41
   times. Applied to the 1938-39 national figure of £89-£94, that gives £125-£133,
   central £130. **DERIVED from MEASURED inputs.**

5. **£64 is defensible as a net-of-renewals 1930s figure at a 38-39 per cent
   renewals deduction; as a gross figure it is 39 per cent low.** The measured gross
   ladder is £84 / £84 / £131 / £106 / £89 / £131 / £150 at 1900 / 1913 / 1920 / 1931
   / 1939 / 1950 / 1960-1990. At a 35 per cent renewals provision the net ladder is
   £55 / £55 / £85 / £69 / £58 / £85 / £98. £64 sits between the 1931 and 1939 net
   values and below every value from 1950 onward. **MEASURED gross level; renewals
   share ESTIMATE.**

6. **The £400 London County Council E/1 event is a body rebuild, not a works
   overhaul.** The E/1 class was the council's 1,000-car standard class. Reed,
   *London Tramways*, page 89, records a 1934 plan to overhaul 250 E/1 cars for
   £100,000, £400 a car, including "some fairly substantial cosmetic alterations to
   the exteriors as well as fully enclosing the front areas which had hitherto been
   open". That is 20-27 per cent of an estimated new price of £1,500-£2,000 and
   1.9-2.2 times the annual maintenance figure. It belongs to `upgrade_price`.
   **STATED.**

7. **The £300 Feltham event is unverified and is a heavy reconditioning.** The
   Feltham cars were the 1931 London United and Metropolitan Electric Tramways class,
   bought second-hand by Leeds in 1949-50. The only source for the £300 is a Flickr
   comment quoted in a forum post, which says "many of them required an overhaul
   costing in the region of £300". The £500 purchase price is confirmed by the same
   *Modern Tramway* article, which calls it "a wonderful bargain". The work described
   in that article is a one-off reconditioning at Kirkstall Works: trucks stripped,
   worn parts replaced, hornways welded, tyres turned, damaged panels replaced,
   varnish removed and woodwork repolished, upholstery cleaned. The £300 is 0.66 times
   the annual maintenance figure and 4-5 per cent of a new bogie tram costing at least
   £7,000 in 1951. **STATED scope; UNAVAILABLE price.**

8. **The two modern events separate cleanly.** Metrolink's 2004 mid-life
   refurbishment cost £80,000 a tram at 12 years and about one million miles; it
   bought new seats, floors, livery and a major mechanical overhaul, with the body
   and electrical equipment retained. It is 0.85 times the annual maintenance figure
   and about 8 per cent of a new T68 (the class built for the 1992 Metrolink
   opening). Sheffield Supertram's 2026 life extension cost £856,000 a tram at 32-34
   years for structural strength, crashworthiness, reliability and corrosion repair;
   it is 4.5 times the annual maintenance figure and 43-50 per cent of a new tram.
   **MEASURED event prices.**

9. **The workbook's overhaul maxima are both rebuilds.** The pre-1950 22 per cent of
   capital is the London County Council rebuild; the post-1950 45 per cent is the
   Supertram life extension. The actual overhauls, the Feltham reconditioning and the
   Metrolink refurbishment, are 4-8 per cent of capital. The capital share is not
   transferable across eras: the capital ladder rises 27-fold from 1929 to 1996 while
   the municipal maintenance figure rises about 1.4-fold to 1990, so a fixed capital
   share overcharges the later era by more than an order of magnitude even before the
   rebuild is separated from the overhaul. **DERIVED.**

10. **The measured works-overhaul interval is two years.** A contemporary description
    of the London County Council's Charlton works, mid-1930s, states that every car
    was examined annually and certified to the Ministry of Transport, and that "a car
    is given a complete overhaul, occupying about thirteen days, every second year".
    **STATED.**

11. **The measured modern mid-life interval is 12 years or about one million miles.**
    Metrolink's original 26 T68 cars were built for the 1992 opening and received the
    £80,000 refurbishment in 2004. **MEASURED event; interval STATED.**

12. **The recommended gross ladder is £84 / £84 / £131 / £106 / £89 / £131 / £150 at
    1900 / 1913 / 1920 / 1931 / 1939 / 1950 / 1960-1990, and £1,177 for the modern
    contract.** The 1900 and 1913-14 values are derived from the 1913-14 combined head
    and a 45-50 per cent car share; 1923-1933 are measured; 1937-1939 are derived from
    the measured combined head and the 53 per cent car share; 1949-50 is derived from
    the Sheffield percentage change; 1960-1990 is an estimate; 2011 is the Nottingham
    Express Transit contract. **MIXED, graded in section 4.**

13. **The modern £1,301 is a 2009 conversion, not the 2011 conversion.**
    £118,657 at the 2011 general index 10,085 is £1,177. The 2009 index 9,163 gives
    £1,295, within 0.5 per cent of the workbook's £1,301. **DERIVED.**

14. **The recommended overhaul provision is 28 per cent of gross A at two years to
    1939, 18 per cent at three years from 1940 to 1990, and 6 per cent at 12 years
    from 1990.** The event ladder is 0.35A for the first overhaul rising to 0.75A for
    the late-life overhaul; the provision is the mean event divided by the interval.
    **ESTIMATE constrained by the measured events.**

15. **The 1984 example becomes £150 a year in place of £347.** At gross A = £150,
    the renewals provision is £53, the overhaul provision £27 and the routine head
    £70. The present £64 plus £283 is £347. The present overhaul alone is 10 times
    the recommended annual provision, and the present total is 2.3 times the
    recommended total. **DERIVED.**

## 2. Method

- **Deflator.** Every nominal figure is converted with the `general` series in
  `New/config/prices.tab` (1900 = 100): 1900 100; 1913 107; 1920 275; 1923 203;
  1930 188; 1932 176; 1937 180; 1939 188; 1949 348; 1950 359; 1960 534; 1961 552;
  1984 3,824; 1990 5,408; 2004 8,005; 2011 10,085; 2025 15,807; 2026 16,281.
  `prices.tab` states that vehicle maintenance stays on the general index.
- **Grades.** MEASURED = an account, return, contract or published total with a stated
  scope. STATED = a trade, academic or witness statement of a rate or an event
  without the underlying account. DERIVED = arithmetic from a measured or stated
  figure, with the chain shown. ESTIMATE = judgement, used only where no measurement
  exists and marked in every table. UNAVAILABLE = identified but not readable or not
  verifiable.
- **Terms.** The **car-only head** is the Ministry of Transport (MoT) return's "Cars
  and other Rolling Stock" column within "General Repairs and Maintenance (or Renewals
  out of Revenue)". It covers repairs and renewals charged to revenue of cars and
  their equipment. **Gross** means the car-only head as printed, with revenue
  renewals inside. **Net** means the car-only head less an estimated renewals
  provision. **A** means the gross annual maintenance figure per car-year in 1900
  money at the reference duty. A **works overhaul** is a periodic visit to a
  workshop at which the car is stripped, its trucks and motors are exchanged for
  reconditioned units, and the body is repaired and painted; it is charged to
  maintenance. A **rebuild** or **life extension** renews or substantially alters the
  body, the electrical equipment or the structure and is a capital event; the engine
  charges it through `upgrade_price`, the field that carries a capital rebuild or life
  extension. **Renewals** are replacements of life-expired components charged to
  revenue rather than to capital.
- **Denominators.** A **car-mile** is one tramcar run one mile; trailers count as
  cars in the Ministry returns. A **car-year** is one car in stock for a year. The
  reference duty is 48,000 km (29,800 miles) a car-year for the historic series,
  which is the measured 1930-31 municipal average of 46,200 km rounded up to the
  workbook's existing reference; the modern contract uses 90,000 km, the forecast
  annual mileage stated for the Nottingham Citadis fleet. The conversion from pence
  a car-mile to pounds a car-year at 48,000 km is 1d x 29,800 / 240 = £124.17.
- **Renewals.** The Ministry head contains renewals charged to revenue. The knowledge
  base's 30-50 per cent band is an estimate; the only directly measured renewals
  share anywhere is a steam tramway's, Dewsbury 1885, at 0.8d of 3.13d a car-mile,
  26 per cent. This pass uses 35 per cent central and shows the 26-50 per cent band
  wherever the distinction changes the answer.
- **Sourcing.** Every page relied on was fetched and read. The 1932-33 Ministry
  return was read from the Internet Archive text layer; the 1919-20 to 1932-33
  car-only totals are report 39's transcription and were checked against the 1932-33
  return's printed totals and car count. The two theses were read through their PDF
  text layers. The forum posts were read in full; the £400 and £300 figures are
  quoted with the caveats the posts themselves give.
- **No `.dat` value and no pakset price is used as evidence anywhere in this pass.**
  The pakset capital ladder appears only as a comparator in section 4.2 and is
  identified as such.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1913-14 | Ministry of Transport return, local-authority tramways, Great Britain | 1.52d per car-mile | "General Repairs and Maintenance"; power, traffic, rates, insurance and general expenses out | car-mile | MEASURED | Report 39 section 7.1; MoT return 1930-31, comparative table p. 8 |
| 2 | 1913-14 | Car-only share of the combined head | 45-50 per cent | share of row 1 | per cent | ESTIMATE | Report 39 section 7.1: 50-55 per cent over 1923-33, lower before 1923 as the permanent-way share was higher |
| 3 | 1919-20 | Ministry of Transport return, local-authority car-only head | £3,642,909 | cars and equipment; revenue renewals in; track, line electrical equipment, power out | fleet-year | MEASURED | Report 39 section 7.1; Internet Archive `railways00566412` |
| 4 | 1919-20 | Car-only per car-mile | 2.8-3.0d | as row 3; car-miles not read | car-mile | DERIVED | Report 39 section 7.1 |
| 5 | 1919-20 | Car-only per car-year at 12,000-16,000 cars | £228-£304 nominal; £83-£111 in 1900 money | as row 3 | car-year | DERIVED | Row 3; general index 275 |
| 6 | 1923-24 | Ministry of Transport return, local-authority car-only head | £2,458,932; 1.98d per car-mile | as row 3 | car-mile | MEASURED | Report 39 section 7.1 |
| 7 | 1930-31 | Ministry of Transport return, local-authority car-only head | £2,205,420; 1.60d per car-mile; 330,338,578 car-miles | as row 3 | car-mile | MEASURED | Report 39 section 7.1; MoT return 1930-31 |
| 8 | 1930-31 | Local-authority motor cars | 11,153-11,504 | cars owned at the year end; column-year mapping in the five-year table is ambiguous | cars | MEASURED | MoT return 1932-33, "Cars owned and capacity" |
| 9 | 1930-31 | Car-only per car-year | £192-£198 nominal; £102-£105 in 1900 money | as row 7 | car-year | DERIVED | Rows 7-8; general index 188 |
| 10 | 1930-31 | Average annual car-mileage | 28,714 miles (46,200 km) | 330,338,578 car-miles / 11,504 cars | car-year | DERIVED | Rows 7-8 |
| 11 | 1932-33 | Ministry of Transport return, local-authority car-only head | £1,928,948; 1.52d per car-mile; 10,793 motor cars | as row 3 | car-mile, car-year | MEASURED | MoT return 1932-33, Abstract of Totals Part II and "Cars owned and capacity" |
| 12 | 1932-33 | Car-only per car-year | £178.7 nominal; £101.5 in 1900 money | as row 11 | car-year | DERIVED | Row 11; general index 176 |
| 13 | 1937 | National tramway maintenance, combined head | 2.56d per car-mile | permanent way, line electrical equipment and cars together | car-mile | MEASURED | Ochojna 1974, appendix table "Tramway Statistics. Cost Breakdowns", from the Ministry returns, https://era.ed.ac.uk/handle/1842/6826 |
| 14 | 1937 | Car-only head | 1.36d per car-mile | 53 per cent car share | car-mile | DERIVED | Rows 2, 13 |
| 15 | 1938-39 | Car-only head | 1.33-1.35d per car-mile | 53 per cent car share; combined head 2.50-2.56d | car-mile | DERIVED | Rows 2, 13; 1938-39 return not read |
| 16 | 1938-39 to 1949-50 | Sheffield Transport, tramcar repairs | +173.2 per cent nominal | car repairs; permanent-way repairs separate | per cent | MEASURED inputs, DERIVED percentage | Buckley 1987, Table 48, https://hull-repository.worktribe.com/output/4212086 |
| 17 | 1938-39 to 1949-50 | Sheffield tramcar repairs in real terms | x1.41 | general index 181 to 348 | ratio | DERIVED | Row 16; `prices.tab` |
| 18 | 1930s | London County Council Charlton works | complete overhaul every second year, about 13 days; annual Ministry examination | complete overhaul; annual examination separate | years, days | STATED | *Wonders of World Engineering*, part 32, quoted at https://greenwichindustrialhistory.blogspot.com/2014/04/charlton-tram-depot.html |
| 19 | 1934 | London County Council E/1 rebuilding | £100,000 for 250 cars, £400 a car | overhaul plus substantial exterior alterations and enclosing the open front areas | per car, one event | STATED | Reed, *London Tramways*, p. 89, quoted at https://forum.simutrans.com/index.php?msg=129383 |
| 20 | 1934 | New E/1 price | £1,500-£2,000 | new car; estimated | per car | ESTIMATE | Forum post #120: Blackpool pantograph cars built 1928 at £2,000 each, citing Wikipedia, https://forum.simutrans.com/index.php?topic=6521.105; this pass's judgement |
| 21 | 1949-50 | Leeds Feltham reconditioning | about £300 a car | trucks stripped, tyres turned, panels replaced, upholstery cleaned; price from an unverified Flickr comment, scope from *Modern Tramway* | per car, one event | UNAVAILABLE price; STATED scope | https://forum.simutrans.com/index.php?msg=129628; *Modern Tramway*, January 1951, quoted at https://rogerfarnworth.com/2026/05/11/modern-tramway-january-1951-the-felthams-in-leeds/ |
| 22 | 1949 | Leeds Feltham purchase price | £500 a car, second-hand | second-hand purchase, not new price | per car | STATED | *Modern Tramway*, January 1951, as row 21 |
| 23 | 1951 | New bogie tram | at least £7,000 | new car | per car | STATED | *Modern Tramway*, January 1951, as row 21 |
| 24 | 2004 | Metrolink T68 mid-life refurbishment | £80,000 a tram | new seats, floors, livery, major mechanical overhaul; body and electrical equipment retained | per tram, one event | MEASURED | *Manchester Evening News*, 10 August 2004, https://www.manchestereveningnews.co.uk/news/greater-manchester-news/metrolink-fleets-million-mile-service-1148795 |
| 25 | 2026 | Supertram life extension | £21.4m plus VAT for 25 trams, £856,000 a tram | structural strength, crashworthiness, reliability, corrosion repair; 1992-2035 | per tram, one event | MEASURED | *Rail Business UK*, 29 October 2026, https://www.railbusinessuk.com/light-rail/2026/10/29/preferred-bidder-selected-for-south-yorkshire-supertram-refurbishment/ |
| 26 | 2011 | Nottingham Express Transit rolling-stock maintenance | £118,657 a tram-year as recorded (the division gives £118,684) | availability contract; workscope unrecorded; includes heavy overhaul years | tram-year | MEASURED contract | *International Railway Journal*, 15 August 2014, https://www.railjournal.com/passenger/light-rail/alstom-lrvs-enter-service-in-nottingham/; report 35 |
| 27 | 2011 | Nottingham figure in 1900 money | £1,177 at index 10,085 | as row 26 | tram-year | DERIVED | Row 26; `prices.tab` |
| 28 | 2011 | Nottingham figure at the 2009 index | £1,295 at index 9,163 | as row 26 | tram-year | DERIVED | Row 26; `prices.tab` |
| 29 | 2024-25 | Supertram rolling-stock maintenance budget | £1,647k for 25 trams = £65,880 a tram-year | rolling-stock maintenance only; staff costs separate | tram-year | MEASURED budget | Supertram 2025/26 Annual Business Plan, p. 19, https://www.southyorkshire-ca.gov.uk/getmedia/3d8fe37f-1809-4186-a525-a19a8c35178d/44262_Supertram-Busines-Plan_v7-2_compressed.pdf |
| 30 | 2024-25 | Supertram figure in 1900 money | £417 at index 15,807 | as row 29 | tram-year | DERIVED | Row 29; `prices.tab` |

## 4. The series

### 4.1 The maintenance level by era

All values are gross car-only figures at 48,000 km a car-year unless the row says
otherwise. "Nominal" is the pence per car-mile printed in the return. "1900 money"
is the nominal figure divided by the general index.

| Date | Nominal car-only | 1900 money per car-mile | 1900 money per car-year | Grade | Basis |
|---|---|---|---|---|---|
| 1900 | - | 0.64-0.71d | 79-88 | DERIVED | 1913-14 combined head x 45-50 per cent car share, at the 1900 index |
| 1913-14 | 0.68-0.76d | 0.64-0.71d | 79-88 | DERIVED | 1.52d combined x 45-50 per cent; index 107 |
| 1919-20 | 2.8-3.0d | 1.02-1.09d | 126-135 | MEASURED inputs, DERIVED | Car-only total and order-of-magnitude per car-mile; index 275 |
| 1923-24 | 1.98d | 0.975d | 121 | MEASURED | Car-only; index 203 |
| 1930-31 | 1.60d | 0.851d | 106 | MEASURED | Car-only; index 188; measured average duty 46,200 km gives £102 |
| 1932-33 | 1.52d | 0.864d | 107 | MEASURED | Car-only; index 176; measured average duty gives £102 |
| 1937 | 1.36d | 0.754d | 94 | DERIVED | Combined 2.56d x 53 per cent; index 180 |
| 1938-39 | 1.33-1.35d | 0.71-0.72d | 88-89 | DERIVED | Combined 2.50-2.56d x 53 per cent; index 188 |
| 1949-50 | 3.69d | 1.060d | 130 | DERIVED | 1938-39 1900-money value x 1.421; £125-£133 |
| 1960 | - | - | 150 (120-250) | ESTIMATE | Held from 1950 with a wage-pressure allowance; no measured figure |
| 1990 | - | - | 150 (120-250) | ESTIMATE | Held; no measured figure for 1960-1990 |
| 2011 | £118,657 a tram-year | - | 1,177 (900-1,300) | MEASURED contract | Nottingham Express Transit; full-service contract, 90,000 km |

**The gross and net readings of £64.** The measured gross level in 1930-33 is £102-£105
for 1930-31 and £102 for 1932-33 at the actual duty, and £106-£107 at 48,000 km. A 35
per cent renewals deduction gives £69-£70; a 38-39 per cent deduction gives £64-£65.
The workbook's £64 is therefore consistent with the measured 1930s gross level **only
if it is a net figure and the renewals deduction is at the top of the 30-50 per cent
band**. Read as a gross figure, it is 39 per cent below the measured 1931 level. From
1950 onward the net figure at 35 per cent is £85, and from 1960 to 1990 it is £98; £64
is 25-35 per cent below those values. The flat line is wrong after 1939 on either
reading.

**What the series does not show.** No measured municipal tramcar maintenance figure
exists for 1950-1990. The 1960-1990 rung is an ESTIMATE, and the error table widens
its band to £120-£250. The 1919-20 per car-mile is an order of magnitude because the
return's car-mileage was not read. The 1937-1939 car-only figures use a 53 per cent
car share measured in 1930-33.

### 4.2 The overhaul events by era

"A" is the gross annual maintenance figure for the same class and era, in 1900 money.
"Capital" is the new price where a measured or stated one exists; the 1934 E/1 price
is an estimate, the 1951 bogie tram price is stated, the 1992 T68 price is an
estimate, and the 2026 new-tram price is an estimate. The last two columns classify
the event: a **works overhaul** stays in maintenance, a **rebuild** or **life
extension** goes to `upgrade_price`.

| Date | Event | Nominal | 1900 money | A (1900 money) | Event / A | Share of capital | Class |
|---|---|---|---|---|---|---|---|
| 1934 | London County Council E/1, 250 cars | £400 a car | £233 | 106-121 | 1.9-2.2 | 20-27 per cent | Rebuild: body alterations and enclosed fronts |
| 1949-50 | Leeds Feltham reconditioning | about £300 a car | £86 | 131 | 0.66 | 4-5 per cent of a £7,000 new tram | Heavy works overhaul: trucks, tyres, panels, upholstery |
| 2004 | Metrolink T68 mid-life | £80,000 a tram | £999 | 1,177 | 0.85 | about 8 per cent of a £1m tram | Heavy works overhaul plus interior refurbishment |
| 2026 | Supertram life extension | £856,000 a tram | £5,258 | 1,177 | 4.5 | 43-50 per cent of a £1.7m-£2m tram | Rebuild: structure, crashworthiness, corrosion |

**The separation.** The two works overhauls sit at 0.66-0.85 times A and 4-8 per cent of
capital. The two rebuilds sit at 1.9-4.5 times A and 20-50 per cent of capital. The
workbook's pre-1950 10-22 per cent of capital and post-1950 8-45 per cent of capital
therefore straddle both categories. The 22 per cent is the 1934 rebuild; the 45 per
cent is the 2026 life extension. Neither is a recurring works overhaul.

**The interval.** The only measured municipal interval is the London County Council's
two years for a complete overhaul, with an annual examination. The modern interval is
the 12 years to Metrolink's mid-life refurbishment. No measured interval exists for a
1950-1990 municipal fleet.

## 5. Recommended rule for the workbook

**The rule.** Read a gross annual maintenance figure A from the dated ladder below.
Deduct a renewals provision of 35 per cent (band 26-50 per cent). Deduct the overhaul
provision from the remainder. The routine head is what is left. The overhaul event is
the provision times the interval times A. In the engine, `initial_overhaul_cost` is the
cost of the first overhaul and `max_overhaul_cost` is the cost of the late-life
overhaul; here they are 0.35A and 0.75A, so the mean event is 0.55A. The total over a
cycle equals A. This is the same envelope rule that [report 43](research-pricing-report-43.md),
[report 44](research-pricing-report-44.md) and [report 46](research-pricing-report-46.md)
apply to carriages, wagons and locomotives.

| Era band | Gross A (1900 £ a car-year) | Renewals provision | Overhaul provision (share of gross A) | Interval | Routine head (share of gross A) | Grade |
|---|---|---|---|---|---|---|
| 1900-1913 | 84 (79-88) | 35% (26-50) | 28% (20-35) | 2 years | 37% | Level DERIVED; provisions ESTIMATE; interval STATED |
| 1914-1923 | 125 (115-135) | 35% | 28% | 2 years | 37% | Level MEASURED; provisions ESTIMATE |
| 1924-1939 | 121 falling to 89 | 35% | 28% | 2 years | 37% | Level MEASURED; provisions ESTIMATE |
| 1940-1960 | 89 rising to 150 | 35% | 18% | 3 years | 47% | Level DERIVED; provisions ESTIMATE |
| 1961-1990 | 150 (120-250) | 35% | 18% | 3 years | 47% | Level ESTIMATE |
| 1990-2026 | 1,177 (900-1,300) | 0% (contract) | 6% (5-8) | 12 years | 94% | Level MEASURED contract; provision DERIVED |

**Do not mix the bases.** The overhaul provision is a share of **gross** A. On the net
figure the same event is 43 per cent of net A before 1950 (28/65) and 28 per cent of
net A from 1950 to 1990 (18/65). A workbook that keeps a net £64 and applies the gross
share of 28 per cent will understate the overhaul. The safe implementation is to carry
gross A in the generator, deduct the renewals provision and the overhaul provision
there, and write the net head to the maintenance column.

**The ladder to put in the generator.** Gross A in 1900 money:
`((1900, 84.0), (1913, 84.0), (1920, 131.0), (1931, 106.0), (1939, 89.0),
(1950, 131.0), (1960, 150.0), (1990, 150.0))`, with a separate modern value of 1,177
for introduction years from 1990. Read the historic ladder log-linearly between the
points and hold it flat before 1900 and after 1990. The modern value is a step at
1990: a full-service availability contract, a different scope from the municipal
repairs head.

**The overhaul event.** Pre-1950: initial 0.35A, maximum 0.75A, three events to the
maximum, 96,000 km between events (two years at 48,000 km), 0.4 months out of service.
1950-1990: initial 0.35A, maximum 0.75A, two events to the maximum, 144,000 km between
events (three years at 48,000 km), 0.5 months. 1990-2026: initial 0.75A, maximum
0.75A, one event, 1,080,000 km between events (12 years at 90,000 km), 0.8 months.
The 1990 modern provision of 6 per cent is the mean event of 0.75A divided by 12. The
6 per cent sits inside the Nottingham contract; adding it on top would charge the same
money twice.

**The 1984 worked example.** Gross A = £150. Renewals at 35 per cent = £53. Overhaul
provision at 18 per cent = £27. Routine head = £70. The annual total is £150. The
present workbook charges £64 of maintenance and £283 a year of overhaul, £347 in
total. The recommended overhaul provision is one tenth of the present one, and the
recommended total is £150 against £347. The present overhaul is 8-45 per cent of a
£13,352 capital; the recommended mean event is £81 every three years, 0.6 per cent of
that capital, and the maximum event is £113, 0.8 per cent.

**The rebuilds.** The 1934 London County Council rebuild at 20-27 per cent of a new car
and the 2026 Supertram life extension at 43-50 per cent of a new tram become
`upgrade_price` values: about 0.22 pre-1950 and 0.45-0.50 from 1990. `upgrade_price` is
the engine field that carries a capital rebuild or life extension. The existing
`OVERHAUL_PROFILE['tram']` upgrade share of 0.50 already matches the modern case; the
pre-1950 case needs a separate 0.22. The Metrolink mid-life refurbishment at 8 per cent
of capital is the modern works overhaul.

## 6. What this changes in the generator and the workbook

1. **`New/ai/cost-balancing/evidence_data.py`, `TRAM_MAINT_TOTAL`.** Replace the
   four-point constant `((1900, 64.0), (1990, 64.0), (2011, 1301.0), (2026, 1301.0))`
   with `TRAM_MAINT_LADDER = ((1900, 84.0), (1913, 84.0), (1920, 131.0),
   (1931, 106.0), (1939, 89.0), (1950, 131.0), (1960, 150.0), (1990, 150.0))` and
   `TRAM_MAINT_MODERN = 1177.0`. Keep `TRAM_REF_KM`; its 90,000 km modern value is
   the forecast annual mileage stated for the Citadis fleet.
2. **`evidence_data.py`, the tram branch of `extrapolation()`.** The branch currently
   does `total = interp(TRAM_MAINT_TOTAL, intro or 1929)`. Replace it with
   `total = TRAM_MAINT_MODERN if (intro or 0) >= 1990 else interp(TRAM_MAINT_LADDER,
   intro or 1929)`. The branch already computes `perkm` from `total`,
   `TRAM_REF_KM` and `ROAD_MAINT_FIXED_SHARE`; keep that derivation and pass
   `maint_gbp=total` to `overhaul_profile()`.
3. **`evidence_data.py`, `TRAM_PERKM`.** The constant `0.0045` is a stale separate
   per-km rate. The tram branch derives its own per-km figure from `total`; either
   delete `TRAM_PERKM` or make the branch read it as a cross-check. At the 1931
   ladder value of £106 and 48,000 km, the average rate is £0.0022 a km. The measured
   car-only rate is £0.0035 a car-mile, which is £0.0022 a km; `0.0045` is the
   combined head, which includes permanent way and line electrical equipment.
4. **`evidence_data.py`, `OVERHAUL_PROFILE['tram']`.** Remove the tuple
   `(0.08, 0.45, 3, 600000.0, 0.5, 0.50)` and add a `tram_overhaul(intro, maint_gbp)`
   function on the model of `carriage_overhaul()` and `wagon_overhaul()`. It returns
   `initial_gbp = 0.35 * A`, `max_gbp = 0.75 * A`, `overhauls = 3` before 1950 and
   `2` from 1950 to 1990, `1` from 1990, `interval_km` 96,000 / 144,000 / 1,080,000,
   and `months` 0.4 / 0.5 / 0.8. The tram branch of `overhaul_profile()` must call it
   with `maint_gbp` and must not fall through to the capital-share tuple.
5. **`evidence_data.py`, the tram branch's basis string.** The string currently says
   "maintenance %.0f GBP a car-year ... historic 64 GBP (MoT returns 1913-14 ...)
   modern 1,301 GBP". Replace it with the rung, the gross/net distinction, the
   renewals share and this report's name. The modern figure is £1,177, not £1,301.
6. **`New/cost-balancing-maintenance.xlsx`, sheet "Tram vehicles".** Columns Q
   ("Measured fixed (GBP/yr)") and AA ("Class fixed (GBP/yr)") take the new gross A;
   the derived columns S, T, U and AE follow. The basis text must say that the figure
   is gross of revenue renewals, that the 35 per cent renewals provision is separate,
   and that the overhaul provision is carved out of the same envelope.
7. **`New/cost-balancing-capital.xlsx`, sheet "Overhauls & upgrades".** The tram rows
   take the 0.35A initial and 0.75A maximum and the 2 / 3 / 12-year intervals. The
   London County Council rebuild and the Supertram life extension move to the upgrade
   column at 0.22 and 0.45-0.50 of the new price.
8. **What to leave alone.** Do not put this ladder into the carriage, wagon,
   locomotive or multiple-unit branches. The tram head is a different statutory head
   from the railway heads, and the modern contract is a different scope from the
   municipal repairs figure. The `TRAM_REF_KM` 90,000 km modern duty and the
   `TRAM_MAINT_MODERN` step must stay together.

## 7. Error bars and assumptions

| Quantity | Central | Band | Why |
|---|---|---|---|
| 1900 gross A | 84 | 79-88 | Car share 45-50 per cent; 1913-14 combined head 1.52d |
| 1920 gross A | 131 | 126-135 | Car-only per car-mile 2.8-3.0d; index 275 |
| 1931 gross A | 106 | 102-108 | Fleet count 11,153-11,504; car share 53 per cent |
| 1939 gross A | 89 | 85-94 | 1938-39 combined head not read; 2.50-2.56d assumed |
| 1950 gross A | 131 | 115-150 | Sheffield base vs national base; index 348-359 |
| 1960-1990 gross A | 150 | 120-250 | No measured figure |
| Modern A | 1,177 | 900-1,300 | Contract spread over 23 years; staff scope; 2009 vs 2011 index |
| Renewals provision | 35% | 26-50% | Only Dewsbury 1885 measured at 26%; electric tramcar share unmeasured |
| Mean overhaul event | 0.55A | 0.40-0.90A | Feltham unverified; Metrolink one event; LCC rebuild excluded |
| Interval, 1900-1950 | 2 years | 2-3 years | One fleet's practice, the largest fleet |
| Interval, 1950-1990 | 3 years | 2-4 years | No measured interval |
| Interval, 1990-2026 | 12 years | 10-15 years | Metrolink mid-life; one event |

**Structural assumptions.** (i) The 1913-14 car share is assumed, not measured; a 40
per cent share would lower the 1900 rung to £75. (ii) The 48,000 km reference duty is
a modelling choice; at the measured 1930-31 average of 46,200 km the rungs are 4 per
cent lower. (iii) The 1938-39 base is a national rate, not Sheffield's own; the
Sheffield percentage change is applied to the national level. (iv) The renewals share
is an estimate; the net figures are shown so the reader can apply a different share.
(v) The Feltham £300 is unverified and may include work that belongs to the purchase
price; the London County Council £400 is a projected cost, not an outturn. (vi) The
modern contract includes maintenance labour; if the engine charges
traffic staff separately and the contract's labour is maintenance labour only, the
figure is comparable; if it includes traffic staff, it is too high. (vii) The 1990
step is a scope change; the underlying real cost of maintaining a tram rose far less.

## 8. Gaps

- **No measured municipal tramcar maintenance figure for 1950-1990.** The 1960-1990
  rung is an ESTIMATE. The routes to close it are the Ministry of Transport
  "Tramways and trolley vehicle undertakings" volumes for 1949-50 onward, the
  Glasgow Corporation Transport annual reports to 1962, the Sheffield Transport
  annual reports to 1960 and the Blackpool Corporation Transport accounts to 1990.
  This is the largest gap in the pass.
- **No measured price for a routine works overhaul.** The London County Council £400
  is a projected rebuild, the Feltham £300 is unverified, and the Metrolink £80,000
  is a mid-life refurbishment. A works order or invoice for a 2-yearly complete
  overhaul at Charlton, Glasgow's Coplawhill works or Leeds's Kirkstall works would
  replace the 0.55A estimate.
- **The 1938-39 Ministry return was not read.** The 1938-39 base is derived from the
  1937 combined head and the Sheffield percentage change. The 1938-39 volume would
  make the 1939 rung measured.
- **No measured interval for a municipal fleet other than London.** The 2-year cycle
  is the London County Council's; Glasgow, Sheffield and Leeds may have differed.
- **No workscope for the Nottingham contract.** The £101m is an availability payment
  and no source states what it covers; the modern A's composition is unrecorded.
- **No measured renewals share for electric tramcars.** The 30-50 per cent band rests
  on a steam tramway's 26 per cent and judgement. A car-account with renewals out of
  revenue separated from repairs would close it.
- **No measured modern heavy-exam interval.** The 12-year Metrolink event is a
  mid-life refurbishment, not a recurring heavy exam; a light-rail maintenance plan
  with exam intervals would test the 12-year provision.
- **No measured 1934 new tram price.** The 20-27 per cent capital share uses an
  estimate; a 1934 contract price for an E/1 or a comparable car would make it
  measured.
- **The 1919-20 fleet count and car-mileage were not read.** The £64 comparison uses
  a 12,000-16,000 range; the return's own Part IV would fix it.
- **The 1930-31 car-count column mapping is ambiguous.** The five-year table gives
  11,153 or 11,504 depending on which year is the first column; the per-car figure
  moves by 3 per cent.
