---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pricing report 48: whether the van and trailer maintenance figures contain the works overhaul

**Status**: research pass, 2026-11-25. Evidence and recommendation only. The pass created this
report and `research-pricing-rows-48.csv` (35 rows); the workbooks, `.dat` files, existing docs and
the knowledge-base index are untouched.

**Question**: the maintenance workbook charges some road vehicles an annual maintenance figure and
a separate works overhaul. A **works overhaul** is a scheduled rebuild of the vehicle or a major
unit in a workshop, after which the vehicle returns to service with its wear reset; the engine
charges it through `initial_overhaul_cost`, `max_overhaul_cost` and
`max_distance_between_overhauls`, and the workbook holds its annualised cost as the **overhaul
provision** (defined in [maintenance-decomposition](../vehicle-cost/maintenance-decomposition.md)).
The **head** is the part of the source figure charged continuously through the fixed and per-km
fields. Charging both is correct only where the annual figure excludes the works overhaul. The
pass examines the van rows, whose annual figure comes from the operating-cost tables of the journal
*The Commercial Motor*, and the trailer rows, whose annual figure comes from the Freight Transport
Association (FTA) *Managers' Guide to Distribution Costs* (October 2016).

**Answer**:

- **Vans: the annual figure contains the works overhaul.** The Commercial Motor maintenance item
  is a combined total whose second part is defined as "repairs and overhauls", and the van
  computations apply that two-part total. The checked-out workbook already deducts an overhaul
  provision from every van row, so the pass recommends no numeric change: deduct 35-50 per cent
  before 1930, 44 per cent for 1930-59, 26-35 per cent for 1960-84 and 27-30 per cent for
  1985-2004 (the lorry bands, which sit at the top of the van evidence), keep the overhaul target
  and keep the interval at 80,000 km for 1930-59 and 160,000 km for 1960-84.
- **Trailers: the FTA line states no workscope, and the treatment that avoids a double count is
  the envelope (head plus annualised provision equals the source figure).** A trailer does receive
  a works refurbishment of its body, running gear and chassis at about one-third of its new price
  every ten to twelve years. The pass recommends that the measured refurbishment become the
  overhaul event (0.33 of the capital target, every 440,000 km at the workbook's 40,000 km
  reference duty), that its annualised provision (about 3 per cent of capital a year) be deducted
  from the FTA head, and that the event be kept. That replaces the present events of 148-1,871 per
  cent of the annual head.

## 1. What this pass found

1. **The Commercial Motor maintenance item is a two-part total whose second part is the
   overhaul.** The journal states that from at least the 1942 edition the Tables (the Commercial
   Motor Tables of Operating Costs) split maintenance into "Maintenance (d)", the routine
   operations scheduled on a time basis (washing, greasing, repainting, varnishing), and
   "Maintenance (e)", "expenditure on repairs and overhauls, operations which are necessary not at
   intervals measured by time but by mileage" (Commercial Motor, 15 January 1943, p. 24; repeated
   for the 1948 Tables on 11 August 1950, p. 46). The 1933 and 1934 Tables print a single
   maintenance line (a 2-ton van at 0.88d. a mile, a 2-ton lorry at 0.75d.), with tyres and
   depreciation separate (transcription in
   [cm-transcription-1937-and-costs](cm-transcription-1937-and-costs.md)); the two-part split is
   first recorded for the 1942 Tables and appears as 0.38d. (d) and 1.23d. (e) in the 1949 6-ton
   costing ([research-pricing-report-42](research-pricing-report-42.md) section 4). Containment
   before 1942 is therefore an ESTIMATE from the later definition. Grade: **STATED** from 1942.
2. **Maintenance (e) contains engine, chassis and body overhauls by name.** The 1956 statement of
   the Tables' introduction lists "engine overhauls and rebores, chassis overhauls, repairs to
   brakes, clutches, transmission, universal joints, cracked frames, repairs to bodywork"
   (Commercial Motor, 5 October 1956, p. 72). The 1966 definition is "washing, servicing and major
   repairs" (Commercial Motor, 16 December 1966, p. 65). Grade: **STATED**.
3. **The van computations carry the same two-part total.** Three 1951 articles divide a van's
   maintenance into (d) and (e): a 30-cwt van at 10s. a week for (d) and 0.60d. a mile for (e)
   (14 December 1951, p. 58); a 30-cwt van at 10s. a week and 0.83d. a mile (4 May 1951, p. 70);
   a 3-ton furniture van with (e) at 1.34d. a mile (6 April 1951, p. 62). The van table therefore
   publishes the same combined total as the goods-vehicle table. Grade: **STATED**.
4. **The van total includes engine replacement.** The Commercial Motor compares a 10-cwt petrol
   van with the same van fitted with an oil engine: maintenance 0.85d. against 0.57d. a mile, the
   0.28d. difference being "because, apart from requiring less frequent service than the petrol
   engine, the oil engine will probably last the life of the vehicle. During the same period,
   however, two replacement petrol engines will probably be needed" (9 January 1959, p. 76). Two
   engines in 100,000 miles are 0.28d. a mile, or 33 per cent of the petrol van's maintenance
   total. Grade: **DERIVED**; the 0.28d. also covers the oil engine's lighter servicing, so 33 per
   cent is an upper bound and 27 per cent the figure if servicing accounts for 0.05d. of the
   difference.
5. **Vans receive works overhauls that include body and running-gear work.** A 1949 account of a
   185-vehicle fleet of 5-cwt to 30-cwt vans describes a standing overhaul rota: "Major overhauls
   are usually, but not always, carried out at the company's main depot ... There is always one
   vehicle undergoing a major overhaul." The overhaul "usually provides for the fitting of a
   reconditioned engine. The bodywork receives attention at the same time (by an outside concern),
   and the vehicle is repainted and relettered", after a 28-point check covering the clutch,
   gearbox, transmission, rear axle, brakes, steering, king-pins, springs, shock absorbers and
   body (Commercial Motor, 25 March 1949, p. 24). Grade: **MEASURED** description; no price.
6. **The measured van overhaul prices and intervals.** A Reliant 5-cwt (quarter-ton) van needed an
   engine replacement every 15,000 miles, and "a replacement unit can be purchased for little more
   than GBP 20 and can be collected from the factory, and fitted ... without the van being docked
   for more than 24 hours" (Commercial Motor, 17 August 1956, p. 50). The same fleet expected a
   Commer 8-cwt van's original engine to reach 40,000 miles, and gave the Bedford light vans a
   150,000-mile life. Grade: **MEASURED**. No van body or chassis overhaul price was found.
7. **The checked-out workbook already deducts for vans.** The 50 van rows on the `Road vehicles`
   sheet of `New/cost-balancing-maintenance.xlsx` carry the lorry band: 35-50 per cent of the head
   for the 20 rows introduced before 1930, 44 per cent for the 6 rows of 1930-59, 26-35 per cent
   for the 15 rows of 1960-84 and 27-30 per cent for the 9 rows of 1985-2004. The overhaul targets
   in `New/cost-balancing-capital.xlsx` amortise to the same provision (for example, the Morris
   Eight van of 1934 deducts GBP 27.81 a year and carries a first overhaul of GBP 27.81 rising to
   GBP 83.42 every 80,000 km). Grade: **CODE**, workbook arithmetic; not evidence about the world.
8. **The FTA maintenance line states no workscope.** The October 2016 table prints one line headed
   "Maintenance Trailer" (GBP 4,002 a year, 5.72p. a mile at 70,000 miles) and one headed
   "Maintenance Tractor" (GBP 7,290, 10.41p.), with tyres, depreciation, VED and insurance as
   separate lines. The only published statement of the line's composition is the Guide's forecast
   assumption that maintenance is "50% labour costs, 40% parts costs and 10% overhead costs" (2019
   sample, Appendix 1 note 5). The Guide is a subscription publication; the public extract
   reproduces the tables without notes. Grade: **UNRECORDED** for the workscope.
9. **The FTA trailer line is worth more than twice the trailer it maintains.** At GBP 4,002 a year
   over the table's 12-year trailer life the line totals GBP 48,024, against a replacement cost of
   GBP 22,488: 2.14 times the purchase price. The tractor line totals GBP 58,320 over 8 years
   against GBP 103,350, or 0.56 times. Grade: **DERIVED**. The ratio is consistent with the trailer
   line funding at least one refurbishment; it is not a statement that it does.
10. **A trailer receives a works refurbishment at about one-third of a new trailer's price.** TIP's
    Stoke-on-Trent refurbishment centre strips, washes, repairs, shot-blasts, repaints, re-curtains
    and refits a trailer, overhauls its axles, brakes and suspension, and returns it to service for
    "a further 10 years"; the price is "around one-third of the cost of buying a new one", against
    GBP 35,000 for a new tri-axle curtainsider in 2025 (Commercial Motor, 3 October 2025). In 1988
    Cooks quoted "around GBP 4,000" for a flat-to-curtainsider body conversion against a new
    trailer at "around GBP 12,000", and "close to GBP 10,000" for a major conversion on a
    10-year-old trailer (Commercial Motor, 21 July 1988, p. 47). Grade: **STATED**, with the 2025
    price a ratio rather than an invoice.
11. **The present trailer overhaul events exceed the annual figure they sit beside.** In the
    checked-out workbook the 65 trailer rows carry events of 148-1,871 per cent of the annual head,
    and annualised provisions of 26-293 per cent of it, because the event is 30 per cent of the
    trailer's capital at a 160,000 km interval (four years at the 40,000 km reference duty). Grade:
    **DERIVED**, workbook arithmetic.
12. **A second 2016 source puts trailer maintenance at about half the FTA level.** The Motor
    Transport cost tables of 12 December 2016 give "Maintenance and repairs" of 2.73p. a mile for
    a tandem-axle trailer and 3.06p. for a tri-axle at 80,000 miles a year, against the FTA's
    5.72p. at 70,000 miles. Grade: **STATED**. The gap supports treating the FTA trailer line as a
    rich total that may carry works a pure repairs line would exclude; it leaves the FTA workscope
    open.
13. **Twenty of the 65 trailer rows have no source figure at all.** The Eagle (1857), Thornycroft
    Amazon (1933) and Thornycroft Q (1924) trailers take the generator's "cart maintenance 5% of
    capital a year" rule, which applies to horse-drawn carts and motor trailers alike and for
    which no source states a composition. Grade: **CODE**; the rule, not the world.

## 2. Method

- One Exa search per turn; every page relied on was fetched and read in full. A search result was
  not treated as evidence.
- The Commercial Motor Tables of Operating Costs are printed as page images with no machine-
  readable text (recorded in [research-pricing-report-31](research-pricing-report-31.md) section
  6). The line values used here are the figures the articles state in prose, and the (d)/(e)
  definitions the journal prints in the text of its costing articles. The 1959 and 1964 van
  articles state the single maintenance figure and leave the printed table unread.
- Grades: **MEASURED** = an operator's or manufacturer's own transaction or account; **STATED** =
  a trade-press costing, official table or published definition; **DERIVED** = arithmetic on
  stated figures, with the arithmetic shown; **ESTIMATE** = judgement where no measured figure
  exists; **UNRECORDED** = no checked-out source states the fact; **CODE** = workbook or generator
  arithmetic, not evidence about the world.
- Money is nominal of the stated year; `d.` is pence in the pre-decimal currency and `p.` is
  decimal pence. The deflator is the `general` series of `New/config/prices.tab` (1900 = 100):
  1938 183, 1947 314, 1959 528, 1961 552, 1970 795, 1985 4057, 2016 11279. VED is vehicle excise
  duty.
- No `.dat` value and no pakset price were read or used. The workbook was read with `openpyxl` from
  `New/cost-balancing-maintenance.xlsx` and `New/cost-balancing-capital.xlsx`; scratch files were
  kept in `ai/temp/rp48/`.

## 3. Evidence table

| Year | Source | Item | Figure as stated | Grade |
|---|---|---|---|---|
| 1943 | Commercial Motor, 15 Jan, p. 24 | Tables' split of maintenance | (d) routine, time-based; (e) "repairs and overhauls ... not at intervals measured by time but by mileage" | STATED |
| 1950 | Commercial Motor, 11 Aug, p. 46 | Tables' split, restated | "as I have done for many years"; a GBP 80 engine overhaul and chassis repair at 48,000 miles = 0.4d. a mile | STATED |
| 1956 | Commercial Motor, 5 Oct, p. 72 | Contents of (e) | "engine overhauls and rebores, chassis overhauls, repairs to brakes, clutches, transmission ... repairs to bodywork" | STATED |
| 1966 | Commercial Motor, 16 Dec, p. 65 | Definition of maintenance | "includes washing, servicing and major repairs" | STATED |
| 1959 | Commercial Motor, 2 Jan, p. 62 | Maintenance's two elements | "the repair work, which varies directly with the mileage run" and "servicing and washing ... on a time basis" | STATED |
| 1951 | Commercial Motor, 14 Dec, p. 58 | 30-cwt van, (d) and (e) | (d) 10s. a week; (e) 0.60d. a mile; (e) is 62 per cent of the total at 325 miles a week | STATED |
| 1951 | Commercial Motor, 4 May, p. 70 | 30-cwt van, (d) and (e) | (d) 10s. a week; (e) 0.83d. a mile | STATED |
| 1951 | Commercial Motor, 6 Apr, p. 62 | 3-ton furniture van, (e) | (e) 1.34d. a mile; bodywork repairs inside (e) | STATED |
| 1959 | Commercial Motor, 9 Jan, p. 76 | 10-cwt van, petrol against oil | 0.85d. against 0.57d. a mile; two replacement petrol engines per 100,000 miles | STATED |
| 1959 | Commercial Motor, 16 Jan, p. 64 | 1-ton van, 200 miles a week | maintenance 1.43d. a mile | STATED |
| 1964 | Commercial Motor, 31 Jul, p. 65 | 10-cwt van at 100 miles a week; 1-ton van at 200 | 2.00d. and 1.81d. a mile | STATED |
| 1956 | Commercial Motor, 17 Aug, p. 50 | Reliant 5-cwt van engine | "little more than GBP 20" at 15,000 miles; Commer 8-cwt at 40,000 miles | MEASURED |
| 1949 | Commercial Motor, 25 Mar, p. 24 | Fleet overhaul of light vans | reconditioned engine, bodywork, repaint and relettering; one vehicle always under overhaul | MEASURED (description) |
| 2016 | FTA Managers' Guide, October 2016, Figure 7 | Trailer maintenance | GBP 4,002 a year, 5.72p. a mile at 70,000 miles; 12-year, 840,000-mile life; replacement GBP 22,488 | STATED |
| 2016 | Same, Figure 7 | Tractor maintenance | GBP 7,290 a year, 10.41p. a mile | STATED |
| 2019 | FTA Managers' Guide, sample 2019, Table 4 | Trailer maintenance | GBP 4,276 at 70,000 miles; GBP 5,105 at 85,000; GBP 5,873 at 100,000 | STATED |
| 2016 | Motor Transport, 12 Dec 2016 | Trailer maintenance and repairs | 2.73p. a mile tandem, 3.06p. tri-axle, at 80,000 miles | STATED |
| 2025 | Commercial Motor, 3 Oct 2025 | Trailer refurbishment | "around one-third of the cost of buying a new one"; new tri-axle curtainsider GBP 35,000; "a further 10 years" | STATED |
| 1988 | Commercial Motor, 21 Jul, p. 47 | Trailer refurbishment and rebody | GBP 4,000 body conversion against a GBP 12,000 new trailer; up to GBP 29,000 for a major conversion; GBP 10,000 on a 10-year-old trailer | STATED |

## 4. What each figure contains

| Source figure | What the source states the figure is | Overhauls inside? | Conclusion |
|---|---|---|---|
| Commercial Motor maintenance item, 1942-1966 Tables | Two sub-items: (d) routine time-based servicing and painting; (e) "repairs and overhauls", itemised in 1956 as engine overhauls and rebores, chassis overhauls, transmission and bodywork | **Yes**, stated | A combined total. Deduct the overhaul provision and keep the overhaul target. |
| Commercial Motor van computations, 1951 | The same (d) and (e) sub-items applied to 30-cwt and 3-ton vans | **Yes**, stated | The van table is the same kind of total as the lorry table. Deduct. |
| Commercial Motor 10-cwt van, 1959 | One maintenance figure (0.85d. petrol, 0.57d. oil), whose petrol-oil difference is attributed to two replacement engines in 100,000 miles | **Yes**, by the Tables' definition; the article identifies engine replacement inside it | Deduct. The engine alone is 27-33 per cent of the total. |
| Commercial Motor 1-ton van 1959 and 10-cwt van 1964 | One maintenance figure, falling per mile as annual mileage rises (a time-based element inside it) | **Yes**, by the Tables' definition | Deduct. The article prints no sub-lines, so the share comes from the class evidence. |
| FTA 2016 tractor maintenance | One line headed "Maintenance Tractor"; tyres, depreciation, VED and insurance separate | **Unrecorded** | Out of scope for this pass; the same question applies to lorry and tractor rows. |
| FTA 2016 trailer maintenance | One line headed "Maintenance Trailer"; tyres, depreciation, VED and insurance separate; 2.14 times the trailer's replacement cost over the stated life | **Unrecorded** | Treat as a total that may contain the refurbishment: deduct the measured provision, keep the event. |
| FTA 2019 trailer maintenance | One line; the Guide's only composition statement is 50 per cent labour, 40 per cent parts, 10 per cent overhead | **Unrecorded** | Confirms the level and the absence of a workscope. |
| Motor Transport 2016 trailer maintenance and repairs | "Maintenance and repairs" at 2.73-3.06p. a mile | **Unrecorded** | A lower comparator; supports treating the FTA line as a rich total. |
| TIP 2025 refurbishment | A full works rebuild at about one-third of the new price, extending life by 10 years | The figure **is** the overhaul | Use as the measured overhaul event for trailers. |
| Cooks 1988 refurbishment | GBP 4,000 body conversion; up to GBP 29,000 for a major conversion; GBP 10,000 on a 10-year-old trailer | The figure **is** the overhaul | Corroborates the one-third ratio 37 years earlier. |
| Generator 5-per-cent trailer rule | No source; a percentage of capital applied to carts and motor trailers alike | **Unrecorded** | Keep the event and deduct the measured provision, so the total stays at the rule's own allowance. |

## 5. Recommended treatment for the workbook

### Vans

The Commercial Motor maintenance item contains the works overhaul, so the van rows must deduct
one. The checked-out workbook already does, at the lorry band's shares, and the pass recommends
keeping those shares:

| Introduction | Rows | Share deducted | Overhaul interval | Grade of the share |
|---|---|---|---|---|
| before 1930 | 20 | 35-50 per cent (band 35-50) | 80,000 km | ESTIMATE, back-cast from 1938 |
| 1930-1959 | 6 | 44 per cent (band 44-56) | 80,000 km | STATED for lorries, ESTIMATE for vans |
| 1960-1984 | 15 | 26-35 per cent (band 25-35) | 160,000 km | ESTIMATE |
| 1985-2004 | 9 | 27-30 per cent (band 20-30) | 400,000 km | ESTIMATE |

The 44 per cent share is a ceiling rather than a point estimate. The only van-specific composition
is the 1959 10-cwt petrol van, where engine replacement alone is 27-33 per cent of the maintenance
total; the 1949 fleet overhaul adds bodywork, repaint and a 28-point check, which lifts the share
towards the lorry band and leaves it unmeasured. The lorry band stays because it is the only
measured composition of the same Commercial Motor total, and it over-provides the overhaul relative
to the van's engine-only floor, which cannot double count. A measured van fleet account, or a
priced van body or chassis overhaul, would replace the band; a share of 30-40 per cent is the
direction the van evidence points.

The overhaul target stays and continues to amortise to the deduction. The interval stays at
80,000 km for 1930-59 and 160,000 km for 1960-84; the measured van intervals are 24,000 km
(Reliant 5-cwt, 15,000 miles) and 64,000 km (Commer 8-cwt, 40,000 miles), so 80,000 km sits above
the measured range and suits the larger vans, while a 5-cwt van is nearer 24,000 km.

### Trailers

The FTA line states no workscope, and a trailer does receive a works refurbishment. The treatment
that cannot double count is the **envelope**: the measured refurbishment is the overhaul event, its
annualised provision comes out of the FTA head, and the head plus the provision equals the FTA
figure.

| Parameter | Value | Basis |
|---|---|---|
| Overhaul event (first and maximum) | 0.33 x the capital target (column 13 of the capital workbook's `Overhauls & upgrades` sheet, the 1900-money purchase price the row is balanced to) | TIP 2025: about one-third of a new trailer; Cooks 1988: GBP 4,000 against GBP 12,000 |
| Interval | 440,000 km | 11 years at the workbook's 40,000 km reference duty; TIP extends life by 10 years, the FTA trailer life is 12 |
| Overhauls to maximum | 1 | The first refurbishment is the maximum; successive refurbishments cost the same |
| Annual provision | 0.03 x the capital target | 0.33 / 11 years (2.8 per cent at 12 years, 3.3 per cent at 10) |
| Head | FTA figure minus the provision | The envelope identity |
| Cap | Provision at most 50 per cent of the FTA figure | 14 rows, including the 4 car-carrier rows, would otherwise carry a provision above half the head; the cap keeps the head positive and flags the low head as a separate defect |

Worked example, Large Artic Trailer (bulk goods), maintenance row 256: FTA head 27.60, capital
target 299.33, event 98.78, provision 8.98, head 18.62, split 75/25 into fixed 4.66 and
0.00034875 a km. The provision is 33 per cent of the head, against 57 per cent for the present
annualised provision; the event is 3.6 times the annual head, against 3.25 times for the present
maximum, and it falls due every 440,000 km instead of every 160,000 km.

The twenty rows on the 5-per-cent-of-capital rule take the same event and envelope. Their annual
figure is the generator's allowance, so the envelope divides that allowance into roughly 2 points
of routine work and 3 points of refurbishment; the six Eagle trailers of 1857 are the least secure,
because no measured works event exists for a horse-drawn trailer.

## 6. What this changes in the workbook

**`New/cost-balancing-maintenance.xlsx`, sheet `Road vehicles`, columns 27 (AA, class fixed
GBP a year) and 29 (AC, class per km, GBP).**

- **Vans: no numeric change.** The 50 van rows keep their present shares and overhaul intervals.
  The class basis in column 31 and, where present, the notes in column 42 change to record that the
  Commercial Motor total contains overhauls by the Tables' own definition, with the 1949 fleet
  overhaul and the 1959 engine composition as the van-specific evidence.
- **Trailers: all 65 rows change.** Grouped by maintenance-sheet row: Eagle 175-180; Large Artic
  256-263; 5t 414-418; 3t 419-423; Scammell 1955 504-510; Crusader 514-520; Mechanical Horse
  521-525; Standard Artic 597-604; Amazon 625-631; Q 640-646. For each row the head (the sum of
  column 27 and column 29 multiplied by 40,000 km) falls by the provision in the parameter table
  in section 5, and the split remains 75 per cent distance, 25 per cent standing. The group result
  before the 50-per-cent cap:

| Group | Rows | Present provision, per cent of head | Envelope provision before the cap, per cent of head |
|---|---|---|---|
| Eagle (1857) | 6 | 88-89 | 50-51 |
| Large Artic (1987) | 8 | 57-262 | 33-150 |
| 5t (1907) | 5 | 26-39 | 15-22 |
| 3t (1900) | 5 | 33-48 | 19-28 |
| Scammell 1955 | 7 | 53-293 | 30-168 |
| Crusader (1968) | 7 | 38-231 | 22-132 |
| Mechanical Horse (1934) | 5 | 32-91 | 18-52 |
| Standard Artic (1978) | 8 | 55-327 | 32-187 |
| Amazon (1933) | 7 | 88 | 50 |
| Q (1924) | 7 | 88 | 50 |

**`New/cost-balancing-capital.xlsx`, sheet `Overhauls & upgrades`, columns 14-17 (N-Q: suggested
first overhaul GBP, suggested maximum overhaul GBP, overhauls to maximum, interval km).**

- **Vans: no numeric change.**
- **Trailers: all 65 rows change.** Column 14 (N) and column 15 (O) both take 0.33 x the capital
  target in column 13 (M), capped so that the annualised provision is at most half of the FTA head
  (an event of at most 0.5 x the head x 11 years); column 16 (P) takes 1; column 17 (Q) takes
  440,000. The recommended .dat columns 20-23 follow, and the downtime in column 18 becomes 0.33
  months (10 days, from the TIP workscope).

## 7. Error bars and assumptions

- **The van share is an estimate by analogy.** The deduction itself is STATED; the 44 per cent
  share is measured on lorries and the other bands are estimates. The van evidence gives 27-33 per
  cent for engine replacement alone, so the share could be 10 points lower without contradicting
  anything measured. A 10-point error moves a 1930-59 van's head by about 18 per cent of itself.
- **The refurbishment ratio is 0.33 with a band of about 0.25-0.40.** The 1988 and 2025 statements
  agree on one-third, and neither is an invoice. A 0.25 ratio cuts the provision by a quarter.
- **The interval is 10-12 years.** TIP gives "a further 10 years"; the FTA table gives a 12-year
  trailer life. At the workbook's 40,000 km reference duty that is 400,000-480,000 km and a
  provision of 2.8-3.3 per cent of capital a year.
- **The FTA containment is unrecorded.** If the FTA line excludes refurbishment, the envelope
  undercharges by about 3 per cent of capital a year, which is 15-51 per cent of the head. That is
  the price of a treatment that cannot double count; the alternative risks charging the
  refurbishment twice.
- **The capital target is itself high.** The 1987 and later trailer rows carry 30 per cent of the
  combination's capital, while the same row's basis cites measured tractor-trailer pairs at
  19-21 per cent. On 20 per cent the capital target would be about GBP 199 instead of GBP 299, and
  the provision would fall by a third. That is a capital-side correction, outside this pass.
- **The 40,000 km reference duty is assumed.** It is the workbook's reference distance for road
  vehicles, not a measured trailer mileage. The FTA table's own trailer duty is 70,000 miles
  (112,700 km); its trailer share of the combination's maintenance is 35 per cent, which the pass
  applies to trailers of every era, because no pre-2016 trailer maintenance figure was found.
- **Four car-carrier rows and ten other rows hit the 50-per-cent cap.** Their annual heads are low
  relative to the trailer's capital (the car carriers because the head is scaled by car capacity),
  which is a head defect separate from the overhaul composition.
- **The Commercial Motor tables are page images.** The 1959 and 1964 van figures are prose
  statements of the maintenance item; the printed tables, which would show the (d)/(e) sub-lines
  for those years, were not read.

## 8. Gaps

1. **No FTA statement of the maintenance line's workscope.** The Guide is subscription-only and the
   public extract carries the tables without notes. An FTA methods page, or a member's copy of the
   2016 introduction, would settle whether refurbishment sits inside the line.
2. **No measured van body or chassis overhaul price.** The 1949 fleet describes the workscope but
   gives no money; the only priced van overhaul is an engine at GBP 20 in 1956.
3. **No invoice-level trailer refurbishment price.** TIP gives a ratio to the new price and Cooks
   gives two 1988 examples; a refurbishment invoice with its itemised workscope would replace the
   0.33 ratio.
4. **No trailer maintenance figure before 2016.** The 45 FTA trailer rows (1900-1987 introductions)
   take a 2016 rate deflated to 1900 money, which assumes the trailer-to-tractor maintenance ratio
   is constant.
5. **No measured van composition end to end.** The 1959 10-cwt article gives engine replacement
   alone; the body and chassis share of the van total remains unmeasured.
6. **The 1926 Morris 12-cwt van table and the 1959 Tables of Operating Costs remain unread page
   images.** Reading the printed tables would give the (d)/(e) split for vans directly.
7. **The twenty 5-per-cent trailer rows have no source.** The generator rule applies the same
   percentage to horse-drawn carts and motor trailers; a trailer repair account would replace it.
8. **The fourteen capped trailer rows have heads too low for their capital.** The four car carriers
   are the most severe. A separate pass on the road-vehicle head ladders is needed before the cap
   can be removed.
