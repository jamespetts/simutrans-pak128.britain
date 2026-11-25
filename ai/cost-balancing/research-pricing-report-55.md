---
status: draft
verified: New ex-15 @ fcd40c0bc (working tree)
date: 2026-11-25
---
# Research pass 55 - maglev rolling-stock acquisition and maintenance, operator evidence

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-55.csv`. No workbook, `.dat` file or
existing document was changed.

This pass looks for measured operator accounts or contract values for maglev rolling stock, to
replace or validate the two figures that currently price the pakset's maglev vehicles in
[maglev-costs](../vehicle-cost/maglev-costs.md): **EUR 49,233 a seat** to acquire and **EUR 0.011
a seat-km** to maintain, both at 2009 prices, from Almujibah and Preston (2018), Table 6. Those
two figures convert to **507.6 GBP a seat** and **0.00010257 GBP a seat-km** in 1900 money on the
workbook chain. Both are estimates assembled from system costs. The question for this pass is
whether an operator account or a contract value exists that would replace them with a
measurement. `[LITERATURE:https://doi.org/10.17816/transsyst201843s1298-327]`

The systems approached, in the order set for the pass, were the Shanghai Maglev Transportation
Development Co. Ltd, Aichi Rapid Transit (Linimo, Nagoya), Incheon Transit Corporation and the
Incheon International Airport Corporation, Hunan Maglev Transportation Development Co. (Changsha)
and Beijing S1, the Daejeon Expo line and the Transrapid Emsland facility, and the suppliers
Siemens, ThyssenKrupp, CRRC and Hyundai Rotem. The evidence that could be read is set out in §3;
what could not be read is in §7.

## 1. What this pass found

1. **No operator account obtained in this pass separates rolling-stock maintenance from
   infrastructure maintenance.** The Shanghai operator's own accounts could not be obtained. The
   listed company that names it as a related party, Shanghai Shentong Metro Co. Ltd (stock code
   600834), records it as a wholly-owned subsidiary of the controlling shareholder rather than of
   itself, so the listed company's published cost analysis does not consolidate the maglev line.
   Linimo publishes a profit and loss account with one operating-expense total and no
   asset-class split. The Incheon figures are whole-line operating totals and separately
   contracted heavy maintenance. **UNAVAILABLE (rolling-stock line).**
   `[LITERATURE:https://static.cninfo.com.cn/finalpage/2026-03-31/1225058595.PDF]`,
   `[LITERATURE:https://www.linimo.jp/profile/doc/2018020711555450_39.pdf]`
2. **The only transaction-level maglev vehicle price found is 2.14 times the current acquisition
   estimate.** Chinese trade press reports the Shanghai Transrapid cars at **more than RMB 100
   million a car**, with 15 cars ordered; a second report five years later gives the same figure
   and states that it includes the suppliers' development cost. At the 2003 average of RMB 13.531
   to GBP 1 that is GBP 7,390,579 a car, or **105,129 GBP a car in 1900 money** on the vehicle
   purchase index. A Shanghai five-car set carries 464 seats, so the price is **1,133 GBP a
   seat**, or **1,088 GBP a seat** after the 0.96 labour adjustment used in
   [maglev-costs](../vehicle-cost/maglev-costs.md). **STATED (trade press, two reports);
   DERIVED (per-seat conversion).**
   `[LITERATURE:https://finance.sina.com.cn/chanjing/b/20050518/07101596819.shtml]`,
   `[LITERATURE:https://kunming.cn/news/c/2010-04-09/2122408.shtml]`
3. **That price is consistent with the German contract envelope.** Fifteen cars at RMB 100m is
   RMB 1.5bn, 30.6 per cent of the DM 1,293m equipment and services contract (RMB 4.90bn at
   DM 1 = RMB 3.79). ThyssenKrupp Transrapid held 45 per cent of that contract, DM 581.9m or
   RMB 2.21bn, and its scope was the vehicles, the stator packs, the long stator winding cable and
   the switches. Vehicles at RMB 1.5bn would take 68 per cent of that share and leave about
   DM 187m for 125,000 stator packs, 950 km of winding cable and eight switches. The source does
   not give those three unit prices, so the split cannot be verified; the size is consistent.
   **DERIVED from a MEASURED contract and STATED shares.**
   `[LITERATURE:http://www.maglev.ir/eng/documents/papers/conferences/maglev2004/topic1/IMT_CP_M2004_T1_15.pdf]`
4. **The Almujibah acquisition rate cannot be traced to one transaction.** Table 6 carries five
   cited sources (60-64) for the whole table and the text does not say which source gives which
   row or how the per-seat rate was derived from it. The rate is therefore an **ESTIMATE** built
   from system costs, as [maglev-costs](../vehicle-cost/maglev-costs.md) already records, and it
   is not a measurement that a contract value can be checked against without a production-run
   assumption.
5. **Incheon supplies two measured maglev heavy-maintenance contracts.** The Incheon International
   Airport Corporation paid Hyundai Rotem **about KRW 3.8bn** for the first heavy maintenance of
   the four two-car sets (8 cars), April 2018 to September 2019, and contracted **KRW 5.77bn** for
   the second, October 2022 to October 2024. Both were sole-source contracts. Per trainset and per
   event the two convert to **5,189** and **5,987 GBP in 1900 money** (2019 general index
   12,299 and 2023 general index 14,825; the earlier draft used the 2016 general and the 2023
   vehicle index, which was inconsistent with the maintenance convention). The scope stated for the
   second contract is strip-down, inspection and repair of the whole train, with the braking,
   electrical and bogie systems checked and components replaced, followed by function tests and
   test running. **MEASURED (contract values reported from the operator's submission to the
   National Assembly audit); DERIVED (per-set conversion).**
   `[LITERATURE:https://www.incheonilbo.com/news/articleView.html?idxno=1165368]`,
   `[LITERATURE:https://www.redaily.co.kr/news/articleView.html?idxno=4449]`
6. **At Incheon's utilisation those contracts alone cost 1.1 to 1.3 times the current total
   maintenance rate.** The two contract starts are 4.5 years apart, so the annualised heavy
   maintenance is 1,153 and 1,330 GBP a set-year in 1900 money. The timetable of 103 trips a day
   over 6.1 km gives 229,330 train-km a year for four sets, or 57,332 a set-year. With 180
   passengers a set (capacity, not seats) that is **0.000112 to 0.000129 GBP a seat-km**, against
   the current 0.00010257. The current figure is a total and the Korean figure is one event type,
   so the comparison says either that the current figure excludes heavy overhauls or that it is
   low for a small, lightly used urban line. **DERIVED.**
7. **Shanghai's spare-parts procurement is about a quarter of the current rate.** The operator's
   2026 single-source notice budgets **RMB 15m** for sensors, maglev control boards, magnet poles
   and custom parts for the four trains. At the 2025 average of RMB 9.393 to GBP 1 and the 2026
   vehicle purchase index that is 10,846 GBP in 1900 money, or 7.8 GBP a seat-year across the
   three 464-seat sets. At 292,000 train-km a train-year that is **0.0000267 GBP a seat-km**, 26
   per cent of the current rate. The notice is a budget for one procurement, not a statement of
   annual consumption, so the figure is a floor and not an annual rate. **STATED (budget);
   DERIVED (per-seat conversion).**
   `[LITERATURE:https://m.yfbzb.com/inviteBid/detail/20261016_639341101.html]`
8. **The overhaul interval has three different values, and they belong to three different
   technologies.** Hunan Maglev states that a Changsha train receives a full 架修 (jiaxiu, the
   Chinese term for a scheduled works overhaul) at about **seven years or 1.4 million train-km**,
   and that this is twice the 600,000 km interval of a metro car. Incheon's two heavy-maintenance
   contracts start **4.5 years apart**. CRRC Qingdao Sifang's deputy chief engineer stated in 2021
   that the Shanghai line had run 20 years **without a single 大修** (daxiu, a major overhaul).
   **STATED (Changsha, Shanghai); DERIVED (Incheon).**
   `[LITERATURE:https://www.hn.chinanews.com.cn/news/2022/0329/445377.html]`,
   `[LITERATURE:https://www.thepaper.cn/newsDetail_forward_15007774]`
9. **Linimo's whole-line operating expense is confirmed and contains no vehicle split.** The
   financial year 2025 profit and loss account shows operating revenue JPY 2,026m, operating
   expense JPY 1,931m and depreciation JPY 142m for the 8.9 route-km line. That is **6,963 GBP a
   route-km-year in 1900 money**, of which no part can be assigned to the three-car trains
   from the published account. **MEASURED (statutory accounts); UNAVAILABLE (vehicle line).**
   `[LITERATURE:https://www.linimo.jp/profile/doc/2018020711555450_39.pdf]`
10. **Result: change the acquisition rate, keep the maintenance rate.** The acquisition figure has
    a transaction-level alternative at 2.14 times its value; the maintenance figure has no
    transaction-level alternative, and the evidence that exists brackets it rather than displacing
    it. The recommended values and the reasons are in §5.

## 2. Method

- **1900 money.** A nominal amount is converted as nominal × 100 ÷ the index for its year, where
  the index is the value in `New/config/prices.tab` expressed as per cent of 1900 (1900 = 100, so
  8,287 is written 82.87 in the conversion). Vehicle prices use the `vehicle purchase` series and
  maintenance uses the `general` series, which is the engine's own treatment. Index values used:
  2003 vehicle 7,030 and general 7,774; 2005 vehicle 7,445; 2009 vehicle 8,287 and general 9,163;
  2016 general 11,279; 2017 general 11,684; 2018 general 11,999; 2019 general 12,299; 2021 general
  12,832; 2023 vehicle 13,407 and general 14,825; 2025 general 15,807; 2026 vehicle 14,724.
  `[CODE New ex-15 @ fcd40c0bc: config/prices.tab]`
- **Exchange rates.** Annual averages, cross rates computed from the two published dollar rates.
  The Federal Reserve G.5A release quotes the pound as United States dollars per pound and the
  yuan and won as units per United States dollar, so the cross rate multiplies. The Internal
  Revenue Service table quotes the pound as pounds per United States dollar, so the cross rate
  divides. Values used: RMB 13.531 to GBP 1 in 2003 (8.2772 yuan and 1.6347 dollars to the pound);
  RMB 14.916 in 2005 (8.1936 and 1.8204); KRW 1,571.5 in 2016; KRW 1,455.3 in 2017; KRW 1,469.0
  in 2018; KRW 1,488.5 in 2019; KRW 1,574.8 in 2021; KRW 1,625.2 in 2023; JPY 197.1 and RMB 9.393
  in 2025. The 2026 procurement is converted at the 2025 average because the 2026 average is not
  yet published.
  `[LITERATURE:https://www.federalreserve.gov/releases/g5a/20040102/]`,
  `[LITERATURE:https://www.federalreserve.gov/releases/g5a/20060103/]`,
  `[LITERATURE:https://www.federalreserve.gov/releases/g5a/20200102/]`,
  `[LITERATURE:https://www.irs.gov/individuals/international-taxpayers/yearly-average-currency-exchange-rates]`
- **Grades.** MEASURED = an account, contract, audit submission or statutory return with a stated
  scope. STATED = a trade, academic or official statement of a rate or practice without the
  underlying account. DERIVED = arithmetic here from a measured or stated figure, with the chain
  shown. ESTIMATE = judgement or a modelled unit cost, marked wherever it is used. UNAVAILABLE =
  identified but not readable. Definitions and tags: [claim tags](../claim-tags.md).
- **Denominators, kept apart throughout.**
  - **seat**: one passenger seat. The pakset's `payload[1]` is a seat count, so this is the
    denominator the workbook uses.
  - **car**: one vehicle section. A Shanghai five-car set has five cars and 464 seats, so 92.8
    seats a car.
  - **trainset**: the coupled formation that is maintained as a unit: five cars in Shanghai, three
    in Changsha and Linimo, two in Incheon.
  - **seat-km**: one seat carried one kilometre. The engine's `runningcost` is charged on this
    basis when the vehicle carries passengers.
  - **train-km**: one trainset travelled one kilometre, whatever its load.
  - **set-event**: one heavy maintenance of one trainset.
  - **line-year**: one year of operation of a whole line, including stations, power, staff and
    administration.
- **Scope of the maintenance figures, distinguished.** The Incheon heavy maintenance is a
  scheduled strip and component-replacement event, stated to include braking, electrical and bogie
  systems, function tests and test running. It is not routine daily maintenance and it is not
  infrastructure. The Shanghai parts budget covers only the parts listed in the notice and not
  labour or workshop overhead. The Changsha contracts in rows 20-21 of §3 are civil, track,
  electrical and communications maintenance and explicitly exclude the trains. The Almujibah
  maintenance rate is stated to cover labour, materials and spare parts and train use; it does not
  state whether a heavy overhaul is inside it.
- **Sourcing.** Every page relied on was fetched and read in this pass, except the Almujibah
  article's PDF, which the publisher's site would not serve; its text, Table 6 and reference
  list were read on the article page. The Hunan Maglev procurement site returned HTTP 403 to a
  direct request, so the Changsha tender titles and scopes are taken from search-result
  reproductions of the same notices, and their values are graded as stated in §3.
- **No `.dat` value, workbook figure or pakset price is used as evidence anywhere in this pass.**
  The two figures under test, 507.6 and 0.00010257, appear only as the quantities being compared,
  and every comparison says so.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 2001-01-23 | Shanghai equipment and services contract | DM 1,293m | vehicles, operation control, propulsion and power supply, stator packs and winding cables, switch steel bending girders; guideway civil works out | whole contract | MEASURED | Shanghai Maglev timeline, http://www.smtdc.com/cn/gycf2.html |
| 2 | 2001 | Shanghai consortium shares | Transrapid International 7%, Siemens 48%, ThyssenKrupp Transrapid 45% | contract split by party | share of contract | MEASURED | D. Hoffmann, *Transrapid Project Shanghai*, Maglev 2004, http://www.maglev.ir/eng/documents/papers/conferences/maglev2004/topic1/IMT_CP_M2004_T1_15.pdf |
| 3 | 2001 | ThyssenKrupp Transrapid scope | DM 581.85m derived at 45 per cent | vehicles, stator packs, long stator winding, switches | whole share | DERIVED | as row 2 |
| 4 | 2003 | Shanghai imported car price | "more than RMB 100 million a car"; 15 cars ordered | first batch; price includes suppliers' development cost per the 2010 report | per car | STATED | *China Business Times*, 18 May 2005, https://finance.sina.com.cn/chanjing/b/20050518/07101596819.shtml |
| 5 | 2010-04-08 | Shanghai imported car price, second report | "RMB 100 million a car" | imported cars; development cost included | per car | STATED | *Beijing Daily*, reprinted 9 April 2010, https://kunming.cn/news/c/2010-04-09/2122408.shtml |
| 6 | 2002-03 | Shanghai five-car formation and seats | head car 52, each middle car 110, tail car 78; 464 seats a set reported | Shanghai Maglev Train (SMT) five-car set | per trainset | MEASURED | operator page, http://wx.smtdc.com/wx/DisplayShow.aspx?Id=20 |
| 7 | 2003 | Shanghai car converted | 105,129 GBP a car; 1,133 a seat before labour, 1,088 after | vehicle only | per car, per seat | DERIVED | rows 4 and 6, §2 rates |
| 8 | 2010 | Shanghai domestic car cost | 30 per cent below the imported car | domestically built sample car, two sections | per car | STATED | row 5 source |
| 9 | 2009 | Almujibah and Preston acquisition | EUR 49,233 a seat | modelled unit cost; five cited sources for the whole table | per seat | ESTIMATE | https://doi.org/10.17816/transsyst201843s1298-327 |
| 10 | 2009 | Almujibah and Preston maintenance | EUR 0.011 a seat-km | modelled unit cost; labour, materials, spare parts, train use; overhaul content not stated | per seat-km | ESTIMATE | as row 9 |
| 11 | 2018-04 to 2019-09 | Incheon first heavy maintenance | about KRW 3.8bn paid | four two-car sets (the source does not state the count; four is the fleet size and the second contract's scope); strip, inspect, repair, component replacement | per fleet-event | MEASURED | *Incheon Ilbo*, 16 October 2022, https://www.incheonilbo.com/news/articleView.html?idxno=1165368 |
| 12 | 2022-10 to 2024-10 | Incheon second heavy maintenance | KRW 5.77bn contracted | four two-car sets; same scope, plus function tests and test running | per fleet-event | MEASURED | as row 11; *Railway Economy News*, 18 October 2022, https://www.redaily.co.kr/news/articleView.html?idxno=4449 |
| 13 | 2018-2024 | Incheon heavy maintenance per set | 5,189 and 5,987 GBP 1900 a set-event | vehicle only | per set-event | DERIVED | rows 11 and 12, §2 rates |
| 14 | 2018 | Incheon annual operating cost | USD 6.3m a year | whole line: employment, power, maintenance, administration; employment about 70 per cent | per line-year | STATED | D.-Y. Park and J. F. Gieras, *Incheon Airport Maglev Line*, doi:10.15199/48.2019.06.01, https://powerquality.blog/2024/02/16/incheon-airport-maglev-line/ |
| 15 | 2016 | Incheon maintenance and operating spend | KRW 3,420.95m (February to December) | whole line | per year | MEASURED | *Asia Economy*, 8 October 2018, https://www.ajunews.com/view/20181008074745331 |
| 16 | 2017 | Incheon maintenance and operating spend | KRW 4,562.37m | whole line | per year | MEASURED | as row 15 |
| 17 | 2018 (8 months) | Incheon maintenance and operating spend | KRW 1,993.92m | whole line | per 8 months | MEASURED | as row 15 |
| 18 | 2023 | Incheon cumulative operating spend 2016-2023 | KRW 61.2bn; about KRW 7.7bn a year | whole line; no fare revenue | 8 years | MEASURED | *Kyunghyang Shinmun*, 10 October 2024, https://www.khan.co.kr/article/202410101505001 |
| 19 | 2021 | Incheon 30-year operating forecast | KRW 534.9bn; average KRW 17.8bn a year | whole line; includes renewals | 30 years | STATED | *Kyunghyang Shinmun*, 15 October 2021, https://www.khan.co.kr/article/202110151036001 |
| 20 | 2022-2025 | Changsha civil and track maintenance | ceiling RMB 7,008,411.03 for 36 months | civil works, subgrade, bridges, F-rail track; trains excluded | per 3 years | MEASURED | tender notice, http://www.chinaiut.com/zhaobiao/10264.html |
| 21 | 2021-2024 | Changsha electrical and communications maintenance | ceiling RMB 21,903,170.79 for 36 months | power, contact rail, communications, automation; trains excluded | per 3 years | MEASURED | project record, https://dinggc.cbi360.net/project/4347739352856526848.html |
| 22 | 2022 | Changsha overhaul interval | 7 years or 1.4 million train-km | full 架修 of one train; metro comparison 600,000 km | per train-event | STATED | China News Service Hunan, 29 March 2022, https://www.hn.chinanews.com.cn/news/2022/0329/445377.html |
| 23 | 2019-12-31 | Shanghai cumulative train-km | 19.85 million train-km since 2002; 6,210 days; 59.94 million passengers | four trains | cumulative | MEASURED | Tongji University, 22 June 2020, https://news.tongji.edu.cn/info/1006/74123.htm |
| 24 | 2021-10 | Shanghai overhaul practice | no 大修 in 20 years of operation | whole fleet; statement by the vehicle supplier's deputy chief engineer | per fleet | STATED | *China Business Journal*, 21 October 2021, https://www.thepaper.cn/newsDetail_forward_15007774 |
| 25 | 2026 | Shanghai spare-parts procurement | budget RMB 15m | sensors, control boards, magnet poles, custom parts; four trains | per procurement | STATED | single-source notice, 16 October 2026, https://m.yfbzb.com/inviteBid/detail/20261016_639341101.html |
| 26 | 2025-26 | Linimo operating expense | JPY 1,931m; revenue JPY 2,026m; depreciation JPY 142m | whole 8.9 km line; no asset-class split | per line-year | MEASURED | statutory accounts, https://www.linimo.jp/profile/doc/2018020711555450_39.pdf |
| 27 | 2014 | Korean maglev heavy-maintenance man-hours | 2,137 man-hours a two-car set | heavy maintenance work study; heavy rail 5,558 for four cars, light rail 3,540 for two cars | per set-event | MEASURED | S. K. Ma et al., KSR2014S098, http://railway.or.kr/Papers_Conference/201401/pdf/KSR2014S098.pdf |
| 28 | 2013 | Incheon two-car capacity | about 180 passengers a set | crush capacity, not a seat count | per trainset | STATED | Hyundai Rotem, 7 October 2022, https://blog.hyundai-rotem.co.kr/755 |

Rows 1-3 price a system, not a vehicle, and are used only to test the vehicle price for
consistency. Rows 15-19 are whole-line figures and cannot be used as rolling-stock rates. Rows
20-21 are the contracts that show the Changsha trains are maintained in house, outside the
outsourced infrastructure contracts.

## 4. The series

### 4.1 Acquisition per seat

| Price year | System | GBP a seat, 1900 money | Grade | Basis |
|---|---|---|---|---|
| 2003 | Shanghai, imported car | 1,133 (1,088 after labour) | STATED; DERIVED | RMB 100m a car, 464 seats a five-car set |
| 2005 | Shanghai, imported car at the 2005 price year | 970 (932 after labour) | STATED; DERIVED | same nominal price, 2005 index and rate |
| 2009 | Almujibah and Preston | 529 (508 after labour) | ESTIMATE | EUR 49,233 a seat |
| 2010 | Shanghai, domestic car | 793 (761 after labour) | DERIVED from STATED | 30 per cent below the imported price |
| 2021 | Changsha, four trains and signalling | UNAVAILABLE | - | tender value not published |

The 2005 row is not a second observation. It shows what the same nominal price becomes when the
price year is moved: the 1900-money value falls 14 per cent because the vehicle purchase index
rises faster than the exchange rate falls. The price year is therefore part of the estimate, and
2003 (the delivery year) is used for the central value.

### 4.2 Maintenance per seat-km

| Year | Item | GBP a seat-km, 1900 money | Grade | Basis |
|---|---|---|---|---|
| 2009 | Almujibah and Preston total maintenance | 0.00010257 | ESTIMATE | EUR 0.011 a seat-km |
| 2019 | Incheon first heavy maintenance, annualised over 4.5 years | 0.000112 | DERIVED | KRW 3.8bn, 4 sets, 57,332 train-km a set-year, 180 passengers, 2019 general index |
| 2023 | Incheon second heavy maintenance, annualised over 4.5 years | 0.000129 | DERIVED | KRW 5.77bn, same denominators, 2023 general index |
| 2026 | Shanghai spare parts only | 0.0000267 | STATED; DERIVED | RMB 15m, 1,392 seats, 292,000 train-km a train-year |

The three non-Almujibah rows are not alternatives to the Almujibah rate. The Incheon rows are one
event type at a low annual distance; the Shanghai row is parts only. They bracket the total rather
than replace it.

### 4.3 Overhaul intervals

| System | Interval | Grade | Basis |
|---|---|---|---|
| Shanghai Transrapid | more than 20 years, no 大修 | STATED | supplier statement, 2021 |
| Incheon Airport Maglev | 4.5 years between the starts of two heavy-maintenance contracts | DERIVED | contract dates, 2018-04 and 2022-10 |
| Changsha Maglev Express | 7 years or 1.4 million train-km | STATED | operator statement, 2022 |

The three values describe three different duty cycles: 430 km/h long-distance operation at about
292,000 train-km a train-year, 110 km/h airport shuttle operation at about 57,000, and 100 km/h
urban operation. They do not contradict one another, and none of them can be transferred to the
pakset without choosing which duty the pakset's maglev represents.

### 4.4 What the series shows

The acquisition evidence has one transaction and one model, and they differ by a factor of 2.14.
The transaction is a first batch of 15 cars with development cost inside the price. The model is a
unit cost whose derivation is not published. Neither is a serial-production price for a mature
maglev vehicle, because no such market has existed. The choice between them is therefore a choice
about production volume, not about which arithmetic is right.

The maintenance evidence is consistent in order of magnitude across three systems and two
decades: the Incheon heavy-maintenance contracts, annualised at the utilisation those trains
actually ran, are 1.1 to 1.3 times the current total rate; Shanghai's parts procurement is about a
quarter of it; the Korean work study puts maglev heavy-maintenance labour 23 per cent below heavy
rail and 40 per cent below light rail for comparable formations. Nothing in that set contradicts
0.00010257 as a total rate, and nothing in it confirms the rate either, because no source
separates routine maintenance from heavy maintenance.

The overhaul evidence is the most useful new material for the pakset, because the pakset currently
has no maglev overhaul rows. It shows that a full strip is a real event with a real price (Incheon)
and a real interval (Changsha), and that a high-speed line can run two decades without one
(Shanghai).

## 5. Recommended treatment

### 5.1 Acquisition: change 507.6 to 1,088 GBP a seat

**Recommendation: replace the Almujibah rate with the Shanghai transaction rate, 1,088 GBP a seat
in 1900 money.** The reasons:

1. It is the only figure in the set that is tied to an actual transfer of maglev vehicles, and it
   is corroborated by two reports five years apart and by the internal arithmetic of the German
   contract.
2. The pakset's maglev fleets are small bespoke orders. The Shanghai order was 15 cars (three
   five-car trains); the Incheon order was 8; the Changsha initial order was 15 cars (five
   three-car trains). No maglev fleet has been bought in serial production, so a serial-production
   unit cost describes a market that does not exist.
3. The current figure is an estimate whose derivation is not published, and it cannot be
   reconciled with the transaction without assuming a production volume that no source supplies.

The consequence for the workbook and the generator, at 1,088 GBP a seat (1,087.5 before rounding):

| Object | Seats or length | Purchase now (GBP 1900) | Purchase at 1,088 (GBP 1900) |
|---|---|---|---|
| RMU 9000 Class | 8 m, no seats | 15,663 | 33,557 |
| RMU Aerocab | 10 m, no seats | 19,579 | 41,946 |
| RMU Box Car / Flat Car | 16 m, no seats | 31,326 | 67,114 |
| Ultraspeed M10 "Zephyr" (front/rear) | 54 seats | 27,410 | 58,725 |
| Ultraspeed M30 "Platinum Jubilee" (centre) | 108 seats | 54,821 | 117,450 |

The per-metre rate becomes **4,194.6 GBP a metre** (1,087.5 × 54 ÷ 14) in place of 1,957.7.

The change is a factor of 2.14. If the user prefers not to move on a press figure, the defensible
alternative is to keep 507.6 and record 1,088 as the upper bound; the two cannot both be right for
the same production volume, and the report should then say which volume the workbook assumes.

### 5.2 Maintenance: keep 0.00010257 GBP a seat-km

**Recommendation: no change.** The evidence brackets the figure rather than displacing it:

- the Incheon heavy-maintenance contracts alone are 1.1 to 1.3 times the rate at Incheon's
  utilisation, so the rate is not generous;
- the Shanghai parts procurement is about a quarter of the rate, so the rate is not below the
  parts cost;
- the Korean work study says maglev heavy maintenance needs less labour than heavy rail, which
  supports a rate below the rail ladder rather than above it.

What the evidence cannot do is confirm that the Almujibah rate includes heavy overhauls. If it
excludes them, the pakset under-charges by the annualised overhaul cost; if it includes them, the
pakset is right. The figure should therefore carry a note that its overhaul content is not stated,
and the band in §6 should be wide enough to cover both readings.

### 5.3 Overhauls: add no rows in this pass

**Recommendation: do not add maglev overhaul rows yet.** The pakset's maglev objects have no
overhaul fields, so the continuous rate is currently the whole maintenance charge. Adding an event
on top without reducing the head would charge the same work twice, contrary to standing rule 0 of
[maintenance decomposition](../vehicle-cost/maintenance-decomposition.md). The evidence for an
event exists (Incheon's contracts, Changsha's interval), but the split between head and event does
not, and the pakset has no measured envelope to split. Record the evidence and leave the single
rate in place.

If an overhaul row is added later, the Changsha interval of 1.4 million train-km is the only
measured maglev interval expressed in distance, and it is the one the engine's
`max_distance_between_overhauls` field needs. The Incheon interval of 4.5 years is a period, not a
distance, and would need the reference duty to convert it.

### 5.4 Stock with no seats

The per-metre application stays an extrapolation from passenger stock, because no maglev system
runs freight stock. The acquisition uplift carries through to 4,194.6 GBP a metre; the maintenance
rate per metre-km is unchanged at 0.00039563. The note in
[maglev-costs](../vehicle-cost/maglev-costs.md) that this is an extrapolation should stay.

### 5.5 What would move the figures

- A rolling-stock maintenance line in the Shanghai operator's accounts, or in a bond prospectus,
  would replace the estimate with a measurement and would settle the overhaul question at the same
  time.
- A Changsha 架修 contract value would give a second measured maglev overhaul price, at a
  different speed and duty from Incheon's.
- An Incheon annual maintenance breakdown by asset class would turn the whole-line totals in rows
  15-19 into a rolling-stock rate.
- A published vehicle contract value for Changsha's 2021 four-train order or for Beijing S1 would
  give a Chinese production price to set against the German first-batch price, and would show how
  far the 2.14 factor is a development-cost effect.

## 6. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| Acquisition, GBP a seat, 1900 money | 1,088 | 761-1,133 | 761 is the domestic-build price at 30 per cent below; 1,133 is the imported price before the labour adjustment; the 2005 price year gives 932 inside the band |
| Acquisition, ratio to the current figure | 2.14 | 1.50-2.23 | band above divided by 507.6 |
| Maintenance, GBP a seat-km, 1900 money | 0.00010257 | 0.00006-0.00016 | 0.00016 is Incheon's heavy maintenance alone at 4.5 years; 0.00006 is a judgement for a cheaper labour base with heavy overhauls excluded; neither end is measured |
| Incheon heavy maintenance, GBP a set-event, 1900 money | 5,987 | 5,189-5,987 | the two contracts; the second is a sole-source price and may carry a supplier premium |
| Incheon overhaul interval, years | 4.5 | 4-5.1 | starts 4.5 years apart, completions 5.1 years apart |
| Shanghai annual train-km a train | 292,000 | 250,000-330,000 | 19.85 million train-km over 17 years and four trains; the divisor depends on when the fourth train entered service |
| Changsha overhaul interval, train-km | 1,400,000 | 1,000,000-1,800,000 | operator statement "about 7 years or 1.4 million km", which implies 200,000 km a train-year; the band allows for the "about" |

**Structural assumptions.** (i) The Shanghai price is a vehicle price and not a system price; the
2005 report says "each carriage" and derives a nine-car train at RMB 900m, which is consistent with
a vehicle price. (ii) The 464-seat denominator is the reported seat count; the operator's car
capacities sum to 460, so the per-seat rate could be 1 per cent higher. (iii) The Incheon capacity
of 180 is a crush capacity and not a seat count, so the Incheon per-seat-km figures are lower
bounds if the seated capacity is smaller. (iv) The Incheon annual distance is derived from the
published timetable (103 trips a day, 6.1 km) and not from a train-km return, so it inherits any
difference between the timetable and the actual service. (v) The 2026 Shanghai procurement is
converted at the 2025 average exchange rate. (vi) The 0.96 labour adjustment is a construction
labour factor at a 25 per cent labour share, taken from
[report 17](research-pricing-report-17.md) §5; a vehicle is more labour-intensive than a guideway,
so the true vehicle factor is probably further from 1, and the 1900-money figures carry that
uncertainty in addition to the bands above.

## 7. Gaps and routes

In order of value, with the exact route to each.

1. **Shanghai Maglev Transportation Development Co. accounts.** Route: the issuer-disclosure
   platforms for Chinese bonds, Shanghai Clearing House (https://www.shclearing.com.cn) and China
   Foreign Exchange Trade System (https://www.chinamoney.com.cn), searched under the company's
   Chinese name 上海磁浮交通发展有限公司 for a 募集说明书 (offering circular) or 年度报告
   (annual report); alternatively the Shanghai municipal audit bureau's published audit findings
   for the line's early years (2004-2006). Look for 运营成本 (operating cost) and 维修费
   (repair cost) lines and for a 车辆 (vehicle) sub-line. **UNAVAILABLE.**
2. **The 2026 Shanghai spare-parts award value.** Route: the award notice that follows the
   single-source notice of 16 October 2026, on the Shentong Metro procurement platform; the budget
   is RMB 15m and the award may be lower. This would turn row 25 from a budget into a price.
   **UNAVAILABLE.**
3. **Changsha 架修 contract.** Route: the Hunan Maglev procurement results pages
   (https://www.hncsmtr.com/webfiles/908/931/) returned HTTP 403 to a direct request; the same
   notices are republished on 城轨采购网 (https://www.mtrmart.com) and on the Changsha public
   resource trading platform (https://fwpt.csggzy.cn). Search for 磁浮列车 架修 and 均衡架修
   between 2021 and 2024. A contract value would give a second measured maglev overhaul price.
   **UNAVAILABLE.**
4. **Changsha 2021 vehicle order.** Route: tender 0716-214HNE960570, four trains (12 cars) and
   signalling for the T3 extension, published on 中国国际招标网
   (http://chinabidding.mofcom.gov.cn). The evaluation result is listed but its bid values were
   not readable in this pass. **UNAVAILABLE.**
5. **Incheon vehicle supply contract.** Route: Hyundai Rotem's 2013 business report (사업보고서) on
   the Korean electronic disclosure system (https://dart.fss.or.kr), searching 현대로템 and
   자기부상; or the Incheon International Airport Corporation's audit submission for the same
   year. This would give a measured low-speed maglev vehicle price to compare with Shanghai's
   high-speed price. **UNAVAILABLE.**
6. **Linimo vehicle maintenance.** Route: the Railway Statistics Annual (鉄道統計年報), published
   by the Ministry of Land, Infrastructure, Transport and Tourism, which gives 修繕費 (repair
   cost) as one total, or Aichi Prefecture's published management analysis of its third-sector
   companies, which may break the figure down. **UNAVAILABLE.**
7. **Beijing S1 vehicle contract.** Route: the Beijing municipal major projects office
   (北京市重大项目建设指挥部办公室) and the Beijing municipal commission of transport, searching
   for 磁浮S1线 车辆 采购 between 2015 and 2017. Beijing S1's vehicle order is the second of the two
   Chinese orders whose value was not found in this pass, the other being Changsha's 2021 order.
   **UNAVAILABLE.**
8. **Transrapid Emsland vehicle cost.** Route: the German federal parliament's printed papers
   (Bundestagsdrucksachen) for the Emsland facility and the Munich project, searching for
   Fahrzeugkosten (vehicle cost) and Transrapid. A test vehicle price would be a supplier price
   rather than an operator price, and is the least valuable of the eight. **UNAVAILABLE.**

**What a positive result would and would not change.** A Shanghai rolling-stock maintenance line
would replace the maintenance estimate and settle the overhaul question; it would not by itself
change the acquisition rate. A Changsha or Beijing vehicle contract would test whether the
Shanghai first-batch price is a development-cost artefact; if a Chinese production price came out
near 507.6, the recommendation in §5.1 would fall and the Almujibah estimate would be vindicated as
a serial-production rate. That is the single most useful test of the acquisition recommendation.
