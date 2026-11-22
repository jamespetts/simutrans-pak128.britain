# Research pass 26 — London Underground rolling stock: build cost, reliability and overhaul

Status: draft evidence for the parent session. Compiled 2026-11-22. The knowledge base is not
edited here.

**Covers**: the London Underground objects in the pakset — multiple-unit tube and surface
stocks, the Metropolitan and District electric locomotives, and the locomotive-hauled
Metropolitan carriages. For each: a contract or published price where one exists, contemporary
statements about reliability with the mechanism, and works intervals kept separate from both.

**Companion file**: `research-pricing-rows-26.csv` — 47 rows: 7 capital and 40 adjustments. The
period-evidence rows carry `price=0` and `scope=maintenance (period evidence, not additive)`; they
record a source without changing the lifetime adjustment.

**Rule observed throughout**: no Simutrans `.dat` price was read, used or fitted to. Pakset
object names were used only to identify which stock was being researched. Where a price is
derived per car or per train, the arithmetic is shown in the row notes and the original figure
is the one recorded.

---

## 1. Summary

1. **No contract price was found for the C69 batch, the 1938 stock, the 1959/62 stock, any of the
   electric-locomotive classes, or the hauled carriages.** The C77 batch is the exception: £7.7m
   for 11 six-car trains in 1976. The accessible London Transport annual reports are not
   digitised in a searchable form; the TfL Corporate Archives catalogue (LT000258/004/001) lists
   them, but only catalogue descriptions and thumbnails were retrieved from the public interface
   in this pass. This is the largest gap.
2. **Seven real capital figures were found**: the 1973 stock order (£39m, 1972), the C77 batch
   (£7.7m for 11 six-car trains, 1976), the 1983 stock costing (£1.5m per six-car train, 1979),
   the 1992 stock contract (£300m plus, 1991), the 1995 stock PFI (£400m, 1995), the S stock
   price (about £7m per train, c.2010) and the all-in Bombardier turnkey programme (£3.4bn,
   2003). The 1973, C77, 1983, 1992 and S stock figures are close to vehicle-only; the 1995 PFI
   includes maintenance and depots, and the 2009 figure is a whole-programme total, so neither
   must be divided into a per-car price.
3. **The C stock recollection is supported for the early 1970s and contradicted for the late
   period.** Two named London Transport engineers say, in 1971 and 1974, that the C69 had fewer
   preparation problems than earlier stock programmes and a lower failure rate than the
   CO/CP stock it replaced. The record is silent for 1975-1999 and negative for 2000-2014, when
   the fleet was the worst on the network. The lifetime penalty is therefore reduced from +10 to
   **+5**, with the period split set out in section 10. The **1973 stock**'s "by far the most
   reliable" statement is a late-life judgement, so its credit is reduced from −10 to **−5**.
4. **The 1983 stock recollection is strongly supported.** It was the last in-house LU design,
   used Kiepe camshaft control, Mawdsley motor alternators, Westinghouse analogue brakes,
   single-leaf doors and welded H-frame bogies, and was withdrawn after 14 years. Rebuilding it
   to 1996 standard was only 10 per cent cheaper than a new fleet.
5. **The camelback is electric, as the pakset has it.** The name describes the central cab with
   sloping bonnets of the Westinghouse locomotive of 1906. No steam camelback is involved.
   This question is settled and is not pursued further.
6. **Reliability is not one number per class.** The same fleet moves from about 1,000 km mean
   distance between failures (MDBF) at introduction to 30,000-48,000 km when mature. The
   adjustments in section 9 are lifetime averages and exclude the first year, except where
   stated.

---

## 2. Method, grades and what "adjustment" means

One web search per turn through the Exa-backed `websearch` tool, then the page fetched and read
before any claim was used. PDFs were downloaded and their text extracted locally. Where a page
blocked fetching (Cloudflare, paywall, 403, lending restriction) the claim was dropped or carried
at low confidence with the block recorded.

Three kinds of evidence are kept apart:

- **Measured** — a contract, published price, company account or Government answer. These rows
  state a real number.
- **Stated** — a named operator, engineer or historian says a stock was reliable or troublesome,
  without a number. The adjustment is then a band.
- **Inferred** — a band transferred from a measured related case, or from the known mismatch
  between the fitted ladder and the era. Marked low confidence.

| Grade | Meaning |
|---|---|
| High | A primary document states it (TfL board paper, DfT release, company paper) or two independent sources agree |
| Medium-high | One good source with a clear mechanism, or a primary figure whose basis is uncertain |
| Medium | One secondary source with a cited source behind it, no contradiction found |
| Low-medium / Low | Inference, a reputation without a number, or a blocked/untraced source |

**Direction convention.** In the CSV, `kind=adjustment` rows state a signed percentage in
`price`. Positive raises cost (worse reliability or higher build cost); negative lowers it.
`scope` says whether the adjustment applies to build or maintenance. `kind=capital` rows state
money in `price_unit`.

**The adjustment layer must not double-count.** Where a real price row exists, use the price and
not a build percentage. The build percentages below are only for the classes with no price.

---

## 3. The pakset objects and the lettered stocks

The pakset uses year names for tube stock and letters for surface stock. The mapping, with the
year the object represents:

| Letter | Stock | Years | Pakset object | Note |
|---|---|---|---|---|
| A | A60/A62 | 1960-62 | `lul-a-stock` (1960) | Metropolitan line |
| C | C69/C77 | 1969-77 | `lul-c-stock` (1969) | Circle, H&C, Edgware Road-Wimbledon |
| D | D78 | 1978-80 | `lul-d-stock` (1980) | District line |
| P | O/P stock | 1935-37 | `lul-op-stock` (1937) | Metropolitan line |
| R | R stock | 1938/49/52 | `lul-r-stock` (1949) | District line |
| S | S7/S8 | 2009-10 | `lul-s-stock` (2010) | Sub-surface lines |
| Q | Q stock | 1923-38 | not modelled as Q | District line; the pakset has G, KLMN and O/P objects instead |

**Name collision.** The pakset also contains `district-bcd-stock`, which is the District
Railway's B stock of about 1905, not the 1969 C stock. In this report "C stock" always means
C69/C77 unless the District B/C/D stock is named explicitly.

---

## 4. Multiple-unit stocks

### 4.1 C69/C77 (1969/77) — `lul-c-stock`

**Build.** 212 cars (35 six-car trains plus a spare) ordered from Metro-Cammell in May 1968;
the first train entered service on 28 September 1970. A second batch of 67 cars (C77) followed
in 1977-78 for the Edgware Road-Wimbledon service. No C69 price was found. The C77 batch is the
one C stock price located: £7.7m for 11 six-car trains in 1976, an expected cost (*Underground
News* 177, 22 October 1976, newsflash 1711), which is £700,000 per train and £116,667 per car.
The order date and builder are from Wikipedia's citation of Bruce, *Steam to Silver* (1983),
pp. 114-117, and from the Tubeprune page.

**Reliability, 1970-1974: positive, from named London Transport engineers.**

- **May 1971 (contemporary, named).** J. Graeme Bruce, LT Mechanical Engineer
  (Running-Railways), Acton Works, replying to a report that the C69 introduction was delayed:
  "there is no delay in the introduction of C.69 stock into service. Trains are being transferred
  at the rate of 1 per fortnight ... There are always teething troubles ... small problems have
  arisen on the cab door interlocks and the air suspension units which are unique to this rolling
  stock ... the problems which have arisen in the preparation for service of the C.69 stock have
  been less than those which have occurred in previous rolling stock programmes." (*Underground
  News* 113, May 1971, p. 78.) The teething troubles he names are small and confined to the cab
  door interlocks and the air suspension.
- **July 1974 (contemporary, named).** H. Clarke, LT Divisional Engineer 'A' (Railways), Acton
  Works, defending the scrapping of 1938 stock: "One has only to compare the failure rates of the
  CO/CP and C69 stocks on the Hammersmith and Circle to realise that there comes a time to
  replace ageing stocks." (*Underground News* 151, July 1974, p. 107.) The C69 was the new stock
  whose lower failure rate made the case for replacing the old one.
- **1972 (contemporary, anonymous).** A contemporary article on the Northern line's acquisition
  of the 1959 stock says the Central line, with the 1959/62 stock, had "the best record for a low
  number of failures on the whole system", and the Piccadilly line, with the same stock, was "our
  second best line" (*Underground News* 132, December 1972, p. 184). This is a system-wide
  comparison: in 1972 the 1959/62 stock, not the C stock, was the benchmark for reliability.
- **1974 (fleet margin).** 35 C69 trains for 31 required in the peak, a spare ratio of 12.3 per
  cent (*Underground News* 154, October 1974, question-and-answer section). A tight but not
  exceptional margin.

**Reliability, 1975-1999: the record is silent on the fleet's failure rate.** What is recorded is
a series of technical and operational defects, none of which is a fleet reliability figure:

- **1975-76.** Ventilation experiments on C69 cars 5527, 5567 and 6567 were unsuccessful
  (*Underground News* 157, January 1975); car 6527 had louvres fitted in 1972 for the same reason
  (*Underground News* 132, December 1972).
- **1980.** *Modern Railways* vol. 501 p. 321: "Rough riding of 'C' stock remedied" — a
  ride-quality defect.
- **1985.** The C stock driver had to leave his seat and turn round to open the doors, which
  "caused extended station stops"; the fleet was modified with an extra set of door controls
  (*Underground News* 285, September 1985). This is a dwell-time defect, not a failure rate.
- **1992.** *Underground News* 1992 index: "C69/77, shortage affecting Wimbledon-Edgware Road
  service" and "being returned to Doncaster for modified bogies".

**Reliability, 2000-2014: negative, and quantified.**

- **c.2000 (secondary, technical).** Tubeprune: "London Underground's most unreliable stock,
  only occasionally reaching 5,000 kms between service failures. It is usually below this. The
  stock has always been troublesome." Mechanisms given: Metacone suspension and load/weigh
  control difficult to maintain (removed at refurbishment without much improvement); 25 per cent
  more doors than any other stock, and doors about half of all train failures; the Circle line
  duty cycle is one of the hardest on the system.
- **2006/07 (primary).** TfL's Managing Director's Performance Report: "The largest single cause
  of peak train cancellations this period was poor availability and reliability of 'C' stock
  with over 15% of the Circle line's peak trains cancelled for this reason." In the period-13
  table the Circle line ran 83.2 per cent of its peak trains, against 97.3 per cent network-wide,
  with 85 of 94 cancellations attributed to stock.
- **2014 (primary).** TfL's withdrawal press release: the C stock had "become increasingly
  unreliable and costly to maintain as time has gone on".

**What the period record does and does not say.** It says the C stock was a good introduction and
more reliable than the CO/CP it replaced in 1970-74. It does not say the C stock was the most
reliable fleet on the system: the 1959/62 stock held that position in 1972. It says nothing about
the fleet's failure rate between 1975 and 1999. It is clearly negative from about 2000. The
recollection of a reliable C stock is therefore best explained as a memory of the early 1970s,
when the C stock displaced the Metadyne-derived CO/CP and was the new, reliable fleet on the
Circle and Hammersmith & City.

**No source dates a change.** Tubeprune's c.2000 retrospective says the stock "has always been
troublesome", which conflicts with the 1971 and 1974 statements. No source says the fleet
deteriorated at a particular date. The period split above is a reading of the balance of the
evidence, not a contemporary claim that reliability changed in a stated year.

**Adjustment.** +5 per cent maintenance (worse) for the lifetime average: the early positive
period and the late negative period roughly offset, with the late period weighted slightly more
because it is quantified. This replaces the +10 of the first pass. Confidence medium-high for
both ends, none for 1975-1999.

### 4.2 1983 stock (Jubilee line) — `1983-tube-stock`

**Build.** Fifteen six-car trains ordered from Metro-Cammell in 1982; a second batch of 16.5
trains ordered in August 1986. 31.5 six-car trains, 189 cars, in service May 1984 to 9 July 1998.
Squarewheels states the trains "had been costed at £1.5M each in 1979"; that is the only
per-train figure found, and it is a costing, not a signed contract. It implies £250,000 per car
and about £47m for the fleet. Confidence low-medium.

**Reliability.** Negative, with an unusually complete mechanism list:

- **Control equipment.** Kiepe electrically driven camshaft control; Mawdsley motor alternators;
  Westinghouse analogue brake control. Tubeprune: "a number of innovations ... and these were all
  conspicuously unsuccessful."
- **Doors.** Single-leaf doors, a tube version of the D stock layout. The London Transport Museum
  says the doors "slowed down boarding and was a significant factor in the decision to withdraw
  these trains after just 15 years service."
- **Bogies.** Welded H-frame bogies, a tube version of the D stock design; Tubeprune: "Even the
  bogies were a disaster, a design similar to the ill-fated D stock bogie", with frame cracking
  attributed to track quality.
- **Build quality.** The first batch was returned to Metro-Cammell because the cars were 18 mm
  too wide.
- **Service record.** Withdrawn after 14 years. The plan to refurbish the fleet for the Jubilee
  line extension was abandoned because replacing all the equipment and converting the single
  doors to double doors was only 10 per cent cheaper than a new fleet. Staff regarded the fleet
  as unreliable; Wikipedia's citation is Mitchell, *Jubilee Line Extension* (2003), pp. 126-127.

**No MDBF figure was found for the 1983 stock.** The 14-year life, the rebuild-cost ratio and the
mechanism list are the evidence; the size of the penalty is a policy choice within the 15 per cent
cap.

**Adjustment.** +15 per cent maintenance (worse), confidence high for direction.

### 4.3 1992 stock (Central line) — `1992-tube-stock-LU`

**Build.** 85 eight-car trains (680 cars) ordered from BREL in 1989, built 1991-94, in service
from 1993. Dobell and Fried's 1991 IMechE paper describes the process "into a £300M plus
contract". That is a floor, not an exact sum. Derived: £3.53m per eight-car train, £441,176 per
car.

**Reliability.** The best-quantified negative case:

- **MDBF.** About 8,000 km in 2015 (TfL Rail and Underground Panel), described as "the worst
  performing fleet on the LU network". The heavy overhaul was expected to raise MDBF by 1,000 km
  (12 per cent).
- **Traction.** Direct-current motors with chopper control; motor flashovers; "almost £8m per
  year is spent repairing and overhauling the traction motors and mitigating the frequency of
  motor flashovers" (TfL Finance and Policy Committee, 2016). The fleet has 32 motors per train.
- **Structure.** Premature bogie-frame cracking (frames replaced by Siemens, finished 2011) and
  some body cracks (Rail Engineer, 2022).
- **Utilisation.** Designed for 127,000 km per train-year; running about 155,000 km, 22 per cent
  higher.
- **Remedy.** The Central Line Improvement Project, about £500m, replacing the DC traction with
  AC and repairing body corrosion.

**Adjustment.** +15 per cent maintenance (worse), confidence high.

### 4.4 1995 and 1996 stocks (Northern and Jubilee lines)

**Build.** The 1995 stock was procured under a PFI signed on 7 April 1995: 106 six-car trains,
maintenance for 20 years and depot works, £400m net present value. The DfT release calls it
"around 100 new trains"; Railway Gazette gives 106 and notes that payments are spread over 36
years if the extension is taken up. The 1996 stock (59 seven-car trains, later 63) was part of
the same supplier family but no separate price was found.

**Reliability.** Both are above average in the 2016-18 MDBF table: 1995 stock 38,112,000 km
(2016) and 33,648,000 km (2018); 1996 stock 25,143,000 / 28,351,000 / 24,845,000 km. The 1995
stock is maintained under a PFI with availability payments, which is a contractual incentive, not
proof of design quality.

**Adjustment.** 1995 stock -10 per cent; 1996 stock -5 per cent. Confidence medium.

### 4.5 2009 stock (Victoria line)

**Build.** 47 eight-car trains, part of the £3.4bn Bombardier/Metronet turnkey for 1,738 cars
across the Victoria and sub-surface lines, with signalling, maintenance and project management.
No separable train price.

**Reliability.** A clear introduction curve: MDBF 1,075 km in October 2009, 1,744 km by March
2010, with "significant early problems with doors" (TfL Board, 24 March 2010). By 2016-18 it was
31,040,000 / 48,039,000 / 42,321,000 km. Rail Magazine called the fleet "simply phenomenal" in
2015. TfL's benchmarking report records a 74 per cent reliability improvement on the Victoria
line between 2010/11 and 2013/14, which includes signalling and track as well as the trains.

**Adjustment.** -10 per cent maintenance for steady-state service; the introduction penalty is
recorded in the report but not carried into the lifetime figure. Confidence medium.

### 4.6 S stock (S7/S8)

**Build.** 191 trains, 1,395 cars, built by Bombardier at Derby 2008-14. Piers Connor's Modern
Railways article gives "£7 million a train". That is a round figure, not a contract schedule,
and it is the only per-train price found. The £3.4bn programme total is not attributable to the
trains alone.

**Reliability.** Introduction was poor: deliveries were suspended in 2010 with only 21 of 192
trains accepted, after "spectacular sit downs" in service and low availability (Connor). Once
mature, the District and Hammersmith & City fleet MDBF rose from 25,427,000 km in 2016 (mixed D
and S stock) to 85,025,000 km in 2018 (S stock). That is the largest measured improvement in the
table.

**Adjustment.** -10 per cent maintenance for steady-state service. Confidence medium.

### 4.7 1973 stock (Piccadilly line)

**Build.** 87.5 six-car trains (525 cars) ordered from Metro-Cammell; the GLC authorised a £39m
order in January 1972. Service from 19 July 1975. Derived: £445,714 per six-car train, £74,286
per car. The source is a blog citing the GLC authority; the primary record was not located, so
confidence is medium-low as a single figure. It is corroborated by the C77 price: £446,000 in
1972 and £700,000 in 1976 per six-car train is a ratio of 1.57, close to the 1972-76 inflation
ratio, so the two figures support each other.

**Reliability, 1975-76: introduction defects.** The first years were not trouble-free. In May
1975 *Underground News* reported that "due to manufacturing difficulties a number of trains have
been delivered without doors" and that some would return to Metro-Cammell for finishing work
(issue 161, newsflash 1469). In June 1976 a defective 1973 stock train was restricted to 10 mph
and lost ninety minutes between Wood Green and Green Park in the morning peak (issue 174,
newsflash 1684). A crew-training train derailed at South Harrow in February 1976. These are
build-quality and early-life defects, not a fleet failure rate.

**Reliability, 2011-2018: the strong evidence is late-life.** Stephen Critchley, TfL's Chief
Finance Officer, told the London Assembly on 9 February 2011 that "the Piccadilly line trains
that we currently have are by far the most reliable ... in terms of ... the mean distance between
failures". The stock was then 36 years old. The 2016-18 figures are 45,730,000 / 35,291,000 /
30,775,000 km, still at or above most fleets, at 41-43 years old. No comparative reliability
figure for the 1970s or 1980s was found. The 2011 statement is therefore a late-life judgement:
it shows that the design aged well, not that it was outstanding when new.

**Adjustment.** −5 per cent maintenance (better): half the previous −10, because the evidence is
strong but late-life and the 1970s record shows introduction defects. Confidence medium.

### 4.8 1959/62 stock

**Build.** 76 trains of 1959 stock ordered for the Piccadilly line, built by Metro-Cammell;
619 cars of 1962 stock followed. No price found.

**Reliability.** A long-life class with a poor ending. In 1997 LU's train service contracts
manager said "the 1959 stock is at the end of its design life and deteriorating rapidly"; 82 of
the Northern line's 101 trains dated from 1956-62. The class ran to January 2000, about 40 years.
No MDBF figure.

**Adjustment.** +5 per cent maintenance (worse) for the last decade; lower confidence because the
class was average or better for most of its life.

### 4.9 1938 stock

**Build.** 1,121 cars built 1938-50 by Metro-Cammell and the Birmingham Railway Carriage and
Wagon Company; all equipment under the floor. No price found.

**Reliability.** A long-lived and influential design, but by 1969 the fleet was in poor condition:
after a strike at Acton Works, compressor failures on the Bakerloo and Northern lines caused up
to 40 trains a day to be cancelled, and the 30 most unreliable 1938 trains were replaced by the
1972 MkI stock (LURS, "The 1972 MkI Tube Stock"). That is an end-of-life condition, not a
statement about the class when new.

**Adjustment.** 0. Confidence medium.

### 4.10 The other tube and surface stocks

No reliability statement was found for the 1967, A60/A62, D78, R, O/P or the early tube stocks
(1890-1923). All carry 0. The D stock has one enthusiast claim to be the third most reliable
fleet in 2014; it is a forum post, not a measurement, and is not used.

### 4.11 Metropolitan and District multiple units

- **District B/C/D stock (1905).** The doors were initially pneumatically controlled, "proved
  unreliable", and from 1908 were hand-operated by passengers. The early wooden-bodied units were
  replaced by steel cars from 1923. Adjustment +10, confidence medium for the mechanism.
- **Metropolitan 1905 Gate stock.** Problems with the Westinghouse equipment meant the option
  order switched to Thomson-Houston (BTH) control. The open lattice end gates left passengers
  exposed, so vestibules were fitted from 1906 and centre sliding doors from 1911. Adjustment +5.
- **Metropolitan 1913 Circle, 1921 Circle and MV stock.** No evidence, 0.

---

## 5. Electric locomotives

These are the objects the parent asked about specifically, because the pakset prices them on a
power ladder fitted to 1957-2013 traction.

| Object | Year | Power field (kW) | hp equivalent | Actual as built | Builder / scope | Price found |
|---|---|---:|---:|---:|---|---|
| 1890TubeStockLoco | 1890 | 85 | about 114 hp | not checked | City & South London Railway | none |
| 1900TubeLoco | 1900 | 150 | about 201 hp | not checked | Central London Railway | none |
| DistrictElectricLoco | 1905 | 596 | about 800 hp | 800 hp (4 x 200 hp) | Bodies Metropolitan Amalgamated; BTH equipment; 10 built | none |
| MetCamelbackLoco | 1906 | 640 | about 858 hp | 800-860 hp (4 x 200-215 hp; the LURS article says 200 hp motors and 800 hp total, Wikipedia says 215 hp and 860 hp) | British Westinghouse; bodies Metropolitan Amalgamated; 10 built | none |
| MetBTHLoco | 1907 | 640 | about 858 hp | 800 hp (4 x 200 hp) | Metropolitan Amalgamated; BTH control; 10 built | none |
| Metropolitan-Vickers (`met-vickers.dat`) | 1922-23 | 890 | about 1,193 hp | 1,200 hp (4 x 300 hp) | Metropolitan-Vickers; 20 built | none |

The pakset `power` field is in kW (engine source: `vehicle_desc.h`, "Power in kW"), so the four
measured classes are correctly rated. The fitted ladder also uses the `power` field, so there is
no unit mismatch in the ladder. The BTH value is about 7 per cent above its measured 800 hp; that
is within the source uncertainty and is not adjusted here.

**The camelback.** The pakset's `engine=electric` is correct. The Metropolitan ordered ten
electric locomotives from British Westinghouse in December 1904; the bodies and bogies were
subcontracted to Metropolitan Amalgamated. The first arrived at Neasden in June 1905 and the
class entered service in 1906. They were "in the 'camel back' format, having a large central cab
with sloping bonnets on either side" (Connor and Horsey, *Underground News*, April 2024). The
second ten, built 1907, were box-cabs with BTH control. All twenty were re-equipped in 1911-13
and replaced or reconstructed by Metropolitan-Vickers in 1919-23, the new locomotives reusing
some equipment. No steam camelback is recorded in the sources read. The Metropolitan's steam
classes are the A, B, C, E, F, G, H and K classes and the Burnett Tank, which the pakset already
prices on the steam ladder. The American camelback is a different locomotive type.

**Reliability.** Thin but real:

- The Westinghouse locomotives had only one driving position, which "proved troublesome", so a
  second master controller was added soon after entry into service.
- The motors were force-cooled to raise output; the locomotive-hauled train had 800 hp against
  1,200 hp for the equivalent six-car multiple unit, so the locomotive was the weaker option.
- The District locomotives were single-ended and normally worked in pairs back to back, doubling
  the equipment in use per train; three were stripped for their equipment in 1910.

**Build cost.** No contract price was found for any of the five classes. The identifiable sources
are Benest, *Metropolitan Electric Locomotives* (LURS, 2nd ed. 1984), the Metropolitan and
District company accounts, and the engineering press of 1904-07. None is digitised in a form that
could be searched in this pass. A +15 per cent build adjustment (capped, qualitative) is recorded
for the four pre-1923 classes and +10 for the 1922-23 class, as a placeholder only. The true gap
is likely larger: the ladder is anchored on 1957-2013 traction, and these are low-volume bespoke
machines with expensive control gear. The adjustment is a floor, not a measurement.

---

## 6. Hauled carriages

**Scope note.** The corrected brief lists the Metropolitan Dreadnought, Jubilee, Ashbury 1863 and
bogie carriages as the hauled stock. The District 4-wheel and 6-wheel carriages, which appeared
in the first version of the brief, are therefore not covered here. The pakset object
`district-4-wheel` remains unresearched.

The Metropolitan's locomotive-hauled stock is where a contract price per carriage would be most
useful. None was found. The specification and durability evidence is:

| Stock | Built | Builder | Seats | Weight / dimensions | Durability |
|---|---|---|---|---|---|
| Dreadnought | 1910-23 | Metropolitan Carriage, Wagon & Finance Co. | 108 (third), 84 (first), 85 (brake third) | 54 ft 4 in x 9 ft 3 in, 30 tons | Nearly 100 built; described as the "pinnacle" of Metropolitan coaching stock; wide footboards and curved door tops to reduce tunnel damage; lasted to 1961 |
| Jubilee | 1887-92 | Cravens | not stated in sources read | 27 ft 7 in x 8 ft 10 in, wooden body on fixed iron frame | 59 built; "well-built" and "very serviceable"; sold to light railways from 1907; too heavy for a Drewry railmotor in 1921 |
| Ashbury 1863 | 1863 | Ashbury | not stated | GWR-derived four-wheel | Some rebuilt as electric multiple units from 1906 and as push-pull trailers in 1940 |
| Bogie (1898-1900) | 1898-1900 | Ashbury and Cravens | 24 first + 30 third (composite); 7 compartments (third); 5 (brake third) | not stated | Rebuilt as electric multiple units from 1906; four survive on the Bluebell Railway |

**"Long Tom" and "Long Charlie".** The sources read do not support applying these names to the
1898-1900 bogie stock. "Long Charley" is documented for the Great Western four-wheelers used on
the Metropolitan from 1863 (German Wikipedia, citing the Met's own stock history). "Long Tom" was
not found in any source read. The pakset's `met-bogie-*` objects are the 1898-1900 Ashbury/Cravens
bogie carriages on the specification above; whether "Long Tom" belongs to them is an open
question, not a finding.

---

## 7. Build costs: what is measured and what is inferred

| Stock | Figure | Year | Basis | Per car | Confidence |
|---|---:|---|---|---:|---|
| 1973 | £39,000,000 | 1972 | 87.5 six-car trains, GLC authority | £74,286 | Medium-low |
| C77 | £7,700,000 | 1976 | 11 six-car trains, expected cost | £116,667 | Medium |
| 1983 | £1,500,000 | 1979 | per six-car train, costed | £250,000 | Low-medium |
| 1992 | £300,000,000+ | 1991 | contract, 85 eight-car trains | £441,176 | Medium-high |
| 1995 | £400,000,000 | 1995 | PFI, 106 six-car trains + maintenance + depots | not separable | High total / low per car |
| 2009 | £3,400,000,000 | 2003 | all-in turnkey, 1,738 cars + signalling | not attributable | High total / nil per car |
| S stock | £7,000,000 | c.2010 | per train, round figure | about £933,000 | Medium |

The five vehicle-like figures imply a nominal price per car of about £74,000 in 1972, £117,000
in 1976, £250,000 in 1979, £441,000 in 1991 and about £0.93m in 2010. That is consistent with
general inflation plus the larger electrical content of the later stocks. It is not a price
index and should not be used as one.

**Cross-check.** The 1973 price (£446,000 per six-car train, 1972) and the C77 price (£700,000
per six-car train, 1976) are mutually consistent: the ratio is 1.57, close to the 1972-76
inflation ratio. The 1983 figure (£1.5m per six-car train, 1979) is 2.14 times the C77 figure
over three years, well above inflation. That is plausible for a small, aluminium-bodied order
with new electronics, but it is the outlier of the 1970s figures and is the one most in need of
a primary contract check.

**What is missing.** The C69 batch, 1938, 1959/62, the electric locomotives and the hauled
carriages have no price at all. For those classes the choice is a qualitative build adjustment
or nothing. The brief allows 5, 10 or 15 per cent; only the electric locomotives get one, because
the ladder mismatch is structural and known.

---

## 8. Reliability: the quantitative comparisons

The only consistent quantitative series is TfL's mean distance between failures (MDBF), in
thousands of km, from FOI-3074-1819 (8 March 2019). No failures-per-train-mile series was found;
MDBF in kilometres is the modern LU metric, and 1 mile = 1.609 km if a conversion is needed.

| Line / fleet | 2016 | 2017 | 2018 |
|---|---:|---:|---:|
| Bakerloo (1972 stock) | 11,241 | 10,138 | 9,712 |
| Central (1992 stock) | 8,893 | 8,787 | 8,530 |
| District & H&C (D then S stock) | 25,427 | 42,271 | 85,025 |
| Jubilee (1996 stock) | 25,143 | 28,351 | 24,845 |
| Metropolitan (S stock) | 31,859 | 41,727 | 36,102 |
| Northern (1995 stock) | 38,112 | not given | 33,648 |
| Piccadilly (1973 stock) | 45,730 | 35,291 | 30,775 |
| Victoria (2009 stock) | 31,040 | 48,039 | 42,321 |

Read with care: the fleets differ in age in these years (the 1973 stock was 41-43 years old, the
S stock 6-8), and "line" figures include infrastructure-caused failures. The table is a
cross-check on direction, not a controlled experiment.

Other measured points:

- **1972 (qualitative)**: the Central line, with the 1959/62 stock, had "the best record for a low
  number of failures on the whole system"; the Piccadilly line, with the same stock, was "our
  second best line" (*Underground News* 132, December 1972, p. 184). No figure.
- **1992 stock, 2015**: about 8,000 km MDBF, the worst fleet (TfL panel paper).
- **2009 stock, 2009-10**: 1,075 km (October 2009) to 1,744 km (March 2010) at introduction.
- **C stock, c.2000**: under 5,000 km (Tubeprune, secondary).
- **S stock, 2010**: deliveries suspended at 21 of 192 trains accepted (Connor).
- **Victoria line, 2010/11-2013/14**: 74 per cent reliability improvement; **Jubilee line** 67
  per cent (TfL benchmarking report, 2015). These are line figures, not stock figures.

The scale is consistent: a new fleet starts at 1,000-2,000 km, a mature good fleet reaches
30,000-48,000 km, and a bad fleet sits at 8,000-9,000 km.

---

## 9. Recommended adjustments

Percentages are signed: positive = worse or dearer, negative = better or cheaper. All are
qualitative except the capital rows.

| Stock / object | Scope | Adjustment | Confidence | Basis |
|---|---|---:|---|---|
| C69/C77 | maintenance | +5 | Medium (period split) | Early 1970s positive (fewer preparation problems, lower failure rate than CO/CP); 1975-99 silent; 2000-14 negative (under 5,000 km MDBF, over 15% Circle cancellations) |
| 1983 | maintenance | +15 | High (direction) | Kiepe camshaft, Mawdsley MA, single doors, H-frame bogies, 18 mm too wide; withdrawn at 14 years |
| 1992 | maintenance | +15 | High | MDBF 8,000 km; motors, bogies, body cracks; £8m/yr motors; £500m CLIP |
| 1995 | maintenance | -10 | Medium | MDBF 33-38k km, among the best in the 2016-18 table |
| 1996 | maintenance | -5 | Medium | MDBF 24-28k km |
| 2009 | maintenance | -10 | Medium | MDBF 31-48k km; poor first year excluded |
| S stock | maintenance | -10 | Medium | District/H&C MDBF 25k to 85k km; poor introduction excluded |
| 1973 | maintenance | −5 | Medium | "By far the most reliable" (TfL CFO, 2011, at 36 years old); 30-46k km; 1975-76 introduction defects |
| 1959/62 | maintenance | +5 | Medium | "Deteriorating rapidly" at end of life (1997) |
| 1938 | maintenance | 0 | Medium | Long-lived design; 1969 failures are end-of-life |
| District B/C/D | maintenance | +10 | Medium | Pneumatic doors unreliable to 1908; wooden bodies |
| Met 1905 Gate | maintenance | +5 | Medium | Westinghouse equipment problems; gate access |
| District electric loco | maintenance | +5 | Low-medium | Single-ended, worked in pairs |
| Met camelback | maintenance | +5 | Low-medium | One driving position; force-cooled motors; 800 hp vs 1,200 hp |
| District electric loco | build | +15 | Low-medium | Placeholder; ladder mismatch |
| Met camelback | build | +15 | Low-medium | Placeholder; ladder mismatch |
| Met BTH loco | build | +15 | Low-medium | Placeholder; ladder mismatch |
| 1890 / 1900 tube locos | build | +15 each | Low | Placeholder; ladder mismatch |
| Met-Vickers loco | build | +10 | Low | Placeholder; ladder mismatch |
| 1967, A, D, R, O/P, Met 1913/1921/MV, District E/F/G/KLMN, 1890/1900 locos, hauled stock | maintenance | 0 | Low | No evidence; do not adjust |

**Do not apply both a price and a build percentage to the same stock.** The 1973, C77, 1983,
1992, 1995, S and 2009 stocks have capital rows; those are to be used instead of any build
adjustment. The three `period evidence` rows for the C69 and 1973 stocks carry 0 and are not
additive: they record the 1971, 1974 and 1975-76 sources behind the lifetime figures.

---

## 10. What the sources say about C, 1973 and 1983 stock

### C stock

The recollection is that the C stock was particularly reliable. The period record now supports
that for the early 1970s, and contradicts it for the late period. The evidence falls into three
periods.

**1970-1974: positive, from named London Transport engineers.**

1. **J. Graeme Bruce, LT Mechanical Engineer (Running-Railways), May 1971.** Replying to a report
   that the C69 introduction was delayed: there was "no delay"; trains were being transferred at
   one per fortnight; the teething troubles were small and confined to cab door interlocks and air
   suspension; and "the problems which have arisen in the preparation for service of the C.69
   stock have been less than those which have occurred in previous rolling stock programmes"
   (*Underground News* 113, p. 78).
2. **H. Clarke, LT Divisional Engineer 'A' (Railways), July 1974.** "One has only to compare the
   failure rates of the CO/CP and C69 stocks on the Hammersmith and Circle to realise that there
   comes a time to replace ageing stocks" (*Underground News* 151, p. 107). The C69 was the new
   stock whose lower failure rate made the case for replacing the old one.
3. **The system benchmark was still the 1959/62 stock.** A December 1972 article on the Northern
   line's acquisition of the 1959 stock says the Central line, with the 1959/62 stock, had "the
   best record for a low number of failures on the whole system", and the Piccadilly line, with
   the same stock, was "our second best line" (*Underground News* 132, p. 184). The C stock was
   better than the CO/CP, but it was not the most reliable fleet on the system.

**1975-1999: the record is silent on the fleet's failure rate.** The magazines record technical
and operational defects — unsuccessful ventilation experiments in 1975-76, rough riding remedied
in 1980, the 1985 door-control layout that extended station stops, bogie modifications by 1992 —
but no C stock MDBF, availability percentage or cancellations-attributable-to-stock figure. The
middle of the fleet's life is unmeasured in the sources read.

**2000-2014: negative, and quantified.**

1. **Tubeprune (c.2000)** says the stock was LU's most unreliable, usually below 5,000 km between
   failures, "always troublesome", and gives the mechanisms: 25 per cent more doors than any
   other stock, Metacone suspension, load/weigh control, and the Circle duty cycle.
2. **TfL's 2006/07 performance report** makes C stock reliability the largest single cause of
   peak train cancellations that period, with over 15 per cent of Circle line peak trains
   cancelled.
3. **TfL's 2014 withdrawal release** says the trains had "become increasingly unreliable and
   costly to maintain as time has gone on".

**Period split and adjustment.** The early record is positive, the middle is silent, the late
record is negative. A lifetime penalty of +10 (the first pass) let the late evidence stand for
the whole life. The revised figure is **+5**: the early positive and late negative periods
roughly offset, with the late period weighted slightly more because it is quantified. If the
parent prefers to weight the early period more, 0 is defensible; if it prefers the late period,
+10 is defensible. The one figure that is not defensible on this record is a negative adjustment
claiming the C stock was above average for its whole life.

**A second possible source of the recollection.** TfL's Chief Finance Officer said in 2011 that
the **1973 stock** was "by far the most reliable" on the network. The 1973 stock is the Piccadilly
line fleet, not the C stock. If the recollection is of a stock praised for reliability in that
period, the 1973 stock is the other candidate. The C stock explanation (a good new fleet replacing
a bad old one in 1970-74) is the better fit for the word "particularly", because it is supported
by two named LT engineers; the 1973 explanation is a hypothesis, not a finding.

### Period split: C stock and 1973 stock

The two stocks fail in opposite directions if a single lifetime figure is taken from one period:

| Period | C stock (1969/77) | 1973 stock |
|---|---|---|
| Introduction | **Positive.** Fewer preparation problems than previous stock programmes (Bruce, LT, May 1971); lower failure rate than the CO/CP it replaced (Clarke, LT, July 1974). Not the system best: the 1959/62 stock held that in 1972. | **Negative/thin.** Trains delivered without doors in 1975; a 10 mph defect in 1976; no comparative reliability figure. |
| Mature | **Silent.** Ventilation experiments (1975-76), rough riding remedied (1980), door-control dwell time (1985), bogie modifications (1992); no MDBF, availability or cancellation figure. | **Silent.** No comparative reliability figure for 1979-2000. |
| Late | **Negative.** Under 5,000 km MDBF c.2000; over 15 per cent Circle peak cancellations 2006/07; "increasingly unreliable" 2014. | **Positive.** "By far the most reliable" in 2011, at 36 years old; 45,730,000 km MDBF in 2016, at 41 years old. |

The C stock adjustment is **+5** and the 1973 adjustment is **−5**. The first pass used +10 and
−10 respectively, which let one end of each life stand for the whole. The period evidence does not
support that. A per-fleet MDBF table for 1970-1990 would replace the judgement with a measurement;
none was found.

### 1983 stock

The recollection is that the 1983 stock was particularly unreliable. The evidence supports it,
with mechanisms:

- **Traction and control**: Kiepe electrically driven camshaft, Mawdsley motor alternators,
  Westinghouse analogue brake control — all new, all troublesome (Tubeprune).
- **Doors**: single-leaf, slower boarding, "a significant factor" in the 14-year withdrawal (LTM).
- **Bogies**: welded H-frame, a tube version of the D stock design, with frame cracking
  (Tubeprune).
- **Build quality**: first batch 18 mm too wide and returned for modification.
- **Outcome**: withdrawn at 14 years; rebuilding to 1996 standard was only 10 per cent cheaper
  than a new fleet.

The gap is quantitative: no MDBF series was found for the 1983 stock. The 14-year life and the
rebuild-cost ratio are the strongest available measures.

### 1973 stock

The 1973 stock has the same problem in reverse: the strong positive evidence is late-life, and
the early record is one of introduction defects.

- **1975.** "Due to manufacturing difficulties a number of trains have been delivered without
  doors", and some were to return to Metro-Cammell for finishing work (*Underground News* 161,
  May 1975, newsflash 1469).
- **1976.** A defective 1973 stock train was restricted to 10 mph and lost ninety minutes between
  Wood Green and Green Park in the morning peak (*Underground News* 174, June 1976, newsflash
  1684). A crew-training train derailed at South Harrow in February 1976, which is an accident,
  not a reliability measure.
- **2011.** TfL's Chief Finance Officer called the Piccadilly line trains "by far the most
  reliable" on mean distance between failures. The stock was 36 years old.
- **2016-2018.** MDBF 45,730,000 / 35,291,000 / 30,775,000 km, at 41-43 years old, the highest
  or near-highest in the table.

No 1970s or 1980s comparative reliability figure was found, positive or negative. The 2011
statement is a late-life judgement: it shows the design aged well, not that it was outstanding
when new. The adjustment is therefore −5 rather than −10. A 1970s fleet comparison would settle
it; none was found.

### Explicit comparisons

- **C stock against the stock it replaced (CO/CP).** The C stock replaced the CO/CP stock on the
  Circle and Hammersmith & City lines from 1970-71; the displaced CO/CP cars went to the District
  to replace Q stock. This comparison is made, qualitatively, by H. Clarke in July 1974: "One has
  only to compare the failure rates of the CO/CP and C69 stocks on the Hammersmith and Circle to
  realise that there comes a time to replace ageing stocks." The C69 was the more reliable of the
  two; no figure is given. This is the strongest period comparison in the pass.
- **C stock against the 1983 stock.** No direct comparison was found. The two fleets were on
  different lines and overlapped only from 1984 to 1998. The C stock outlasted the 1983 stock by
  16 years, but the per-fleet MDBF series begins in 2016, long after both had gone.
- **1983 stock against the 1959/62 stock.** No direct comparison was found, and the fleets did
  not replace one another: the 1983 stock replaced 1972 MkII stock on the Jubilee line, while the
  1959/62 stock was replaced by the 1995 stock on the Northern line. The only comparison available
  is life: 14 years against about 40.
- **1983 stock against the 1973 stock.** This is the closest comparison in design lineage: the
  1983 stock was a development of the 1973 stock, with the same steel underframe and a similar
  body. The 1973 stock was described by TfL in 2011 as "by far the most reliable" — a late-life
  judgement, at 36 years old — and ran for about 50 years; the 1983 stock was withdrawn at 14.
  The comparison is implicit, not a controlled measurement: the 1983 stock had newer control
  equipment, single-leaf doors and a different duty cycle, and the 1973 stock's early record also
  shows introduction defects.
- **1992 stock against the 1962 stock it replaced.** The 1962 stock was "deteriorating rapidly"
  at the end of its life in 1997; the 1992 stock then became the worst fleet on the network by
  2015. The two statements are about different ends of different lives and do not form a direct
  comparison.
- **S stock against the C and D stocks it replaced.** This is the one measured before-and-after:
  the District and Hammersmith & City fleet MDBF was 25,427,000 km in 2016 (mixed D and S stock)
  and 85,025,000 km in 2018 (S stock). The C stock was replaced by S7 stock in 2012-14, before
  the series begins, so its replacement cannot be isolated in the same way.

---

## 11. Overhaul intervals and works events (kept separate)

Overhaul interval is not a modelled feature. It is recorded here so that it is not confused with
reliability or with build cost.

| Stock | Interval / event | Source | Confidence |
|---|---|---|---|
| 1992 | Programme Lift every 6 years; Heavy Overhaul every 12 years; every second Programme Lift coincides with a Heavy Overhaul | TfL Rail and Underground Panel, 12 Feb 2015, para 3.2 | High |
| 1992 | Utilisation 155,000 km per train-year against a 127,000 km design | Same paper, para 3.4 | High |
| 1967 | "Overhauls, first cycle completed" by 1981, about 12-13 years after introduction | LURS *Underground News* index 1982, citing the 1981 LT annual report | Medium |
| C stock | Mid-life refurbishment 1990-94 by RFS Engineering (Doncaster); not a periodic overhaul | Tubeprune; Squarewheels | Medium |
| 1973 | Refurbished 1995-2000 by Bombardier Prorail, about 20-25 years after introduction | TfL 1973 stock information sheet | Medium |
| 1983 | No heavy overhaul; withdrawn at 14 years | LTM; Squarewheels | High |
| 1995 | Refurbished 2013-15 by Alstom, about 16-18 years after introduction | GB Trains, citing TfL | Medium |
| 1996 | Heavy overhaul about £132m under way in 2023, about 26 years after introduction | GB Trains, citing TfL | Medium |
| 1992 | Heavy Overhaul Programme Lift 2015-17, about 22 years after introduction; CLIP from 2022 | TfL papers | High |

The 6/12-year pattern is the only published interval found. It should not be generalised to the
pre-war stocks without evidence.

---

## 12. Strongest sources

In descending order of value:

1. **TfL board and committee papers** (content.tfl.gov.uk): the 2015 Central line heavy overhaul
   and 2016 CLIP papers give MDBF, motor costs, bogie and body defects and the 6/12-year overhaul
   cycle; the 2010 Victoria/Sub-Surface upgrade paper gives the 2009 stock introduction MDBF.
2. **TfL FOI-3074-1819** (8 March 2019): the only per-fleet MDBF table found, 2016-18.
3. **DfT press release, 7 April 1995**, and **Railway Gazette International, 1 June 1997**: the
   £400m Northern line PFI, with the 1959 stock's end-of-life condition.
4. **Dobell and Fried, IMechE 1991**: the £300m-plus Central line contract.
5. **Connor and Horsey, *Underground News*, April 2024** (LURS PDF): the Metropolitan electric
   locomotives, including the camelback description and the single-controller defect.
6. **LURS *Underground News* historical archive (1962-1987)**: the letters from J. Graeme Bruce
   (May 1971) and H. Clarke (July 1974) are the only named, contemporary statements found on C
   stock reliability, and the C77 price (1976) is the only C stock capital figure found. The
   issues also give the 1972 1959/62 failure-record comparison and the 1973 stock's 1975-76
   introduction defects.
7. **London Transport Museum collection pages**: the 1983 stock doors and withdrawal, the 1938
   stock, the Jubilee carriage.
8. **Vintage Carriages Trust and the Colonel Stephens Society**: Dreadnought and Jubilee carriage
   dimensions, seats, weight and durability.
9. **Tubeprune** (secondary, technical, undated): the fullest mechanism lists for C and 1983
   stock. Use with the confidence grade, not as a primary source.
10. **Squarewheels** (secondary): the £1.5m per 1983 train figure, C stock history.
11. **Wikipedia** (finding aid only): useful for the District and Metropolitan multiple-unit
    history and for the citations to Bruce, Hardy and Mitchell, none of which was read.

---

## 13. Dead ends

Recorded so that a later pass does not repeat them.

- **London Transport / LPTB annual reports.** Not on the Internet Archive in the relevant years
  (only 1998/99 to 2003 are there, and they do not give stock prices). The TfL Corporate
  Archives catalogue at `tfl-2.access.preservica.com` lists the full series (LT000258/004/001,
  1934-2003), but the public interface returned only catalogue descriptions and thumbnails; the
  underlying files were not retrieved in the time available. This is the most promising
  unexplored source for C stock, 1938 and 1959/62 prices and for period reliability statements.
- **Hansard / TheyWorkForYou.** No results for "1983 tube stock", "1983 stock" or "tube stock"
  in 1955-70. The Parliament search API returned unrelated recent contributions, and the
  Historic Hansard site has no full-text search.
- **Bruce, *The London Underground Tube Stock* (1988) and *Steam to Silver* (1983).** On the
  Internet Archive but lending-restricted: the text files return 401/403.
- **Modern Railways.** The archive is not online. The Railway Citation Index gives one relevant
  entry only: "Rough riding of 'C' stock remedied", vol. 501 p. 321 (1980).
- **LURS *Underground News*.** The website hosts indexes, not the articles. The 2012 index
  identifies "LU Train Reliability" by John Hawkins at pp. 21-22 (issue 601), which would
  probably give a per-stock MDBF table for 2011; the issue itself was not found online.
- **Electric locomotive prices.** No contract price found for the District 1905, Metropolitan
  1906/1907 or Metropolitan-Vickers 1922-23 classes. Benest's LURS monograph (1984) is the
  identified source; it is not digitised. The Railway Times volumes on the Internet Archive have
  usable page images but OCR too poor to search for the accounts.
- **Hauled carriage prices.** No contract price per Dreadnought, Jubilee, Ashbury or bogie
  carriage found. The Metropolitan Carriage, Wagon & Finance Co. order books were not located.
- **C69 build price.** The May 1968 order for 212 cars is documented, but no value. The C77 batch
  price was found (row: £7.7m, 1976); the C69 order value was not.
- **1938 stock build price.** 1,121 cars documented; no value.
- **1959/62 stock build price.** 76 trains and 619 cars documented; no value.
- **1983 stock MDBF.** No per-fleet figure found for 1984-98.
- **C stock 1975-1999 reliability.** No MDBF, availability or cancellations figure found. The
  LURS *Underground News* issues for 1975, 1976, 1977 and 1985 were read in full; they record
  defects (ventilation, rough riding, door-control dwell time, bogies) but no fleet reliability
  statistic. Issues from 1988 onward are not digitised. The LT annual reports' statistical tables
  are the missing source.
- **C stock 1970-1974 reliability.** The period is not silent: two named LT engineers give
  qualitative statements (Bruce 1971, Clarke 1974), and the 1972 staff article gives the 1959/62
  benchmark. What is missing is a number. The same applies to the 1973 stock: the 1975-76
  introduction defects are recorded, but no comparative reliability figure.

---

## 14. Open questions

1. Does the parent accept the C stock period split? The present recommendation is **+5**: the
   early 1970s are positive (Bruce 1971, Clarke 1974), 1975-1999 is silent, and 2000-2014 is
   negative. A parent that weights the early period more should use 0; one that weights the late
   period more should use +10. A 1970s or 1980s London Transport annual report with a per-fleet
   MDBF table would settle it; that is the single most valuable missing document for this pass.
2. Does the parent accept **−5** for the 1973 stock? The "by far the most reliable" statement is
   a 2011 judgement at 36 years old, and the 1975-76 record shows introduction defects. A 1970s
   fleet comparison would settle whether the stock was also outstanding when new.
3. Should the 1959/62 penalty be applied to the whole life or only to the last decade? The CSV
   applies a single +5 lifetime figure.
4. Should the 2009 and S stock introduction penalties be modelled separately, given that both
   fleets were below 2,000 km MDBF in their first year and above 30,000 km when mature? The
   model has no introduction curve; the CSV uses the mature figure.
5. Is a contract price for the 1905-07 electric locomotives available in the TfL Corporate
   Archives or the Benest monograph? If so, it should replace the +15 build placeholders.
6. Do the `met-bogie-*` objects represent the "Long Tom" class? The name was not confirmed in
   any source read; the specification is the 1898-1900 Ashbury/Cravens bogie stock.
