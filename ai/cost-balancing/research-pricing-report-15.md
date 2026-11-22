# Measured maintenance costs: road, tram, water and air

Research note 15. Compiled 2026-11-22. Evidence only, plus a recommended ladder per mode at the
end of each section. No `.dat` value was read as evidence, nothing under `New/` was modified, and
no git command was run.

Companion file: `research-pricing-rows-15.csv` (151 rows).

## What this note adds

The knowledge base already holds a large maintenance evidence base, but it is organised by
source and by mode rather than as a ladder. This note does four things:

1. It collects every measured maintenance figure for the four non-rail modes into one
   machine-readable table, with the scope and the denominator of each row.
2. It converts each mode's evidence to **1900 GBP per vehicle-year**, which is the unit the
   pakset ladder needs, and states the annual mileage used for every conversion.
3. It adds new measured rows found this session, the most important of which is a **1915
   municipal motorbus account that gives repairs per bus-mile with tyres and workshop overheads
   explicitly inside the head**, and a **1914 engineering-paper split of tram rolling-stock
   maintenance from track maintenance**.
4. It records the dead ends explicitly, including two that the brief specifically asked for
   (ship repairs per gross ton, 1900-1939; British aircraft maintenance per hour before 1969).

## Conversion

Nominal figures are brought to 1900 by dividing by the `general` index for the year in
`New/config/prices.tab` (1900 = 100) and multiplying by 100. Key values used: 1915 = 120,
1928 = 196, 1936 = 174, 1948 = 338, 1955 = 468, 1958 = 526, 1968 = 709, 1970 = 795, 1983 = 3642,
2016 = 11279, 2026 = 16281.

Foreign currency is converted at the year's average: USD 4.03 to the pound in 1947, 1.63 in 2003,
1.83 in 2005, 1.79 in 2006, 1.55 in 2013 and 1.28 in 2024. Financial years are indexed to their
later calendar year (1913-14 to 1914, 1969/70 to 1970, 2025/26 to 2026).

**A unit trap that affects every post-1971 row.** Figures printed in "p" after 1971 are decimal
pence (1/100 of a pound); the 1900 ladder is in old pence (1/240 of a pound). A decimal penny is
2.4 old pence. Converting a post-1971 pence-per-mile figure by dividing by the index alone
understates it by a factor of 2.4. The per-vehicle-year figures in this note are converted
through pounds and are unaffected; the per-mile column is stated in old pence and has been
corrected. **The "later anchors" block in `New/ai/vehicle-cost/base-maintenance.md` (1983
Merseyside, 2016 FTA) appears to have been converted without the 2.4, so its `runningcost`
values of 74 and 9 are probably about 2.4 times too small (about 177 and 23 on the same method).
That is a proposal for the KB owner to check, not a change made here.**

A second trap, already in the KB but worth repeating: the Commercial Motor "maintenance" item
excludes tyres and lubricants by construction, while a municipal "repairs" head usually includes
them. Rows in the CSV say which.

## Annual mileage used for the per-vehicle-year conversions

Every per-vehicle-year figure below states its own denominator. Where a source gives only a
per-mile rate, the mileage used is:

| Class | Miles a year | Basis |
|---|---|---|
| Bus, 1915 | 26,386 | Sheffield 1915: 369,404 miles over an average of 14 buses |
| Bus, 1928-1955 | 30,000 | Commercial Motor 1934 states 30,000 for a bus, 31,800 for a trolleybus, 28,200 for a tram |
| Bus/coach, 1948 | 20,800 | 400 miles a week, as the article assumes |
| Lorry, 1958 | 26,000 | 500 miles a week, as the article assumes |
| Lorry, 1968 | 20,800 | 400 miles a week |
| Lorry, 1970 | 41,600 | 800 miles a week |
| Lorry, 2016 | 55,000 | FTA's middle band for a 32-tonne tipper |
| Tram, 1914-1931 | 28,200 | Commercial Motor 1934; Glasgow 1915 implies 28,254 |
| Tram, 2025/26 | 48,000 | Sheffield: 1.2m vehicle-miles over 25 cars (computed) |

---

# 1. Road vehicles

## 1.1 What is measured

| Year | Vehicle | As stated | 1900 GBP per vehicle-year | 1900 old pence per mile | Source |
|---|---|---|---|---|---|
| 1905 | Motor omnibus tyres, one town | 4.09d per mile | n/a | 4.09 | Commercial Motor, 13 Jul 1905 |
| 1915 | Motorbus, Sheffield Corporation (14 in service) | 1.92d per bus-mile, repairs head including tyres and workshop | **176** | 1.60 | Commercial Motor, 5 Aug 1915 |
| 1928 | Trolleybus, Keighley | 2.371d per vehicle-mile | **151** | 1.21 | Commercial Motor, 14 Aug 1928 |
| 1930 | 5-ton lorry, fully costed schedule | 1.78d per mile | 103 at 26,000 miles | 0.95 | Commercial Motor, 30 Sep 1930 |
| 1936 | 2-ton van | 0.94d per mile at 250 miles a week | **29** | 0.54 | Commercial Motor, 10 Jan 1936 |
| 1948 | 26-seat bus | 2.50d per mile (tyres 0.72d separate) | **64** (83 with tyres) | 0.74 (0.95) | Commercial Motor, 6 Feb 1948 |
| 1948 | 26-seat coach | 1.50d per mile (tyres 1.00d) | 38 (64 with tyres) | 0.45 | Commercial Motor, 6 Feb 1948 |
| 1955 | Municipal bus, all undertakings average | 2.82d per vehicle-mile | **75** | 0.60 | Chambers report via Commercial Motor, 12 Sep 1958 |
| 1955 | London Transport bus | 4.36d per vehicle-mile | **116** | 0.93 | as above |
| 1955 | Lorry, 7-ton | 2.00d petrol / 1.80d oil per mile | 53 / 48 at 30,000 miles | 0.43 / 0.38 | Commercial Motor, 9 Dec 1955 |
| 1958 | Lorry, 5-ton petrol | 1.95d per mile | **40** | 0.37 | Commercial Motor, 3 Jan 1958 |
| 1963 | Lorry, 7-ton oil | 2.71d per mile | 58 | 0.46 | Commercial Motor, 13 Aug 1965 |
| 1966 | Lorry, 10-ton articulated | 3.13d per mile | 59 | 0.47 | Commercial Motor, 18 Mar 1966 |
| 1968 | Lorry, 16-ton eight-wheeler | 5.06d per mile | **62** | 0.71 | Commercial Motor, 13 Sep 1968 |
| 1970 | Lorry, 16-ton four-wheeler | 4.66d per mile at 800 a week | **102** | 0.59 | Commercial Motor, 11 Sep 1970 |
| 1983 | Bus fleet, Merseyside PTE | 53.7p per mile, repairs and maintenance head | **442** | 3.54 | Commercial Motor, 21 Jan 1984 |
| 2016 | Lorry, 32-tonne tipper | GBP 11,751 a year, 21.37p per mile | **104** | 0.45 | FTA Managers' Guide, Oct 2016 |
| 2016 | Lorry, 44-tonne artic tractor unit | GBP 7,290 a year | **65** | 0.32 | as above |

The pre-1940 rows are the important new ones. The **1915 Sheffield account** is the only
pre-1920 figure found that gives repairs per bus-mile for a named municipal fleet with the
mileage, the fleet count and the scope all stated. It is also the only one that says outright
that tyres, workshop tools, buildings and fixtures are inside the head. At 26,386 miles per bus
it is GBP 211 a bus-year nominal, or GBP 176 in 1900 money.

## 1.2 What the shape is

Read in 1900 money, road maintenance per mile is **U-shaped**, not a trend:

- 1915: 1.60 old pence per bus-mile, with tyres and workshop inside the head.
- 1928-1955: 0.54 to 0.95, falling as vehicles became more reliable and as fleet workshops
  became more productive.
- 1983: 3.54, a real-terms rise of nearly five times on 1955. The Merseyside head is an outlier
  and may include workshop and depot overheads that the Commercial Motor item excludes, but the
  direction is consistent with the labour-intensity of bus maintenance in a high-wage economy.
- Lorries: 0.37 (1958) to 0.71 (1968) to 0.45 (2016). Real maintenance per mile for goods
  vehicles is roughly flat across sixty years, with the 1968 peak explained by the
  maximum-weight eight-wheeler.

Per vehicle-year the same evidence gives GBP 176 for a 1915 bus, GBP 64-116 for a 1948-55 bus,
GBP 29-40 for a 1930s-50s light goods vehicle, GBP 62-102 for a 1960s heavy lorry, and GBP 65-104
for a modern lorry.

## 1.3 Recommended road ladder

1900 GBP per vehicle-year, mid-life vehicle, at the stated annual mileage. "Measured" means a
source states both the cost and the denominator; "derived" means one arithmetic step from a
measured figure; "extrapolated" means no measurement exists in that era.

| Era | Class | Miles a year | GBP per vehicle-year | Basis | Confidence |
|---|---|---|---|---|---|
| 1900-1914 | Motor bus | 26,000 | 180 | Extrapolated flat from Sheffield 1915 | Low |
| 1900-1914 | Motor lorry, 2-3 tons | 20,000 | 45 | Extrapolated from the 1936 van and the 1958 5-tonner, raised for the unreliability of the period | Low |
| 1900-1914 | Motor car or taxi | 12,000 | 18 | Extrapolated from the 1936 van by unladen weight | Very low |
| 1915-1930 | Motor bus | 26,000 | 175 | Measured (Sheffield 1915) | High |
| 1915-1930 | Trolleybus | 30,000 | 150 | Measured (Keighley 1928) | Medium |
| 1915-1930 | Lorry, 2-5 tons | 20,000 | 55 | Derived from the 1930 five-tonner | Medium |
| 1930-1945 | Bus and coach | 26,000 | 110 | Interpolated between 1928 and 1948 | Medium |
| 1930-1945 | Lorry and van | 18,000 | 35 | Measured (1936 van) | Medium |
| 1945-1960 | Bus | 25,000 | 75 | Measured (1955 municipal average) | High |
| 1945-1960 | Coach | 25,000 | 45 | Measured (1948 coach) | Medium |
| 1945-1960 | Lorry, 5-7 tons | 26,000 | 45 | Measured (1958) | High |
| 1960-1980 | Bus and coach | 30,000 | 110 | Interpolated between 1955 and 1983 | Low |
| 1960-1980 | Lorry, 10-16 tons | 30,000 | 70 | Measured (1968, 1970) | High |
| 1980-2000 | Bus | 30,000 | 350 | Measured (1983) less an allowance for the suspected wider head | Low |
| 1980-2000 | Lorry, 32-38 tonnes | 60,000 | 100 | Interpolated to 2016 | Low |
| 2000-2026 | Lorry, 32-44 tonnes | 55,000-70,000 | 65-105 | Measured (FTA 2016) | High |
| 2000-2026 | Bus | 40,000 | 450 | Extrapolated from 1983 | Very low |

**How to use it.** The engine's `fixed_cost` is a monthly charge, so divide the yearly figure by
twelve; `runningcost` is per kilometre, so divide the yearly figure by the annual kilometres and
convert to 1900 pence per kilometre (1 mile = 1.609 km). A bus at GBP 75 a vehicle-year and
25,000 miles is 0.72 old pence a mile, or 0.45 old pence a kilometre.

**The weakest point** is the whole 1900-1914 block. There is no measured maintenance figure for
any British motor vehicle before 1915 in any source reached. The 1915 Sheffield account is only
fifteen years after 1900 and is the correct shape to extrapolate backwards, but early vehicles
had solid tyres, no electric starting, and repair bills that were a much larger share of capital.
Treat the 1900 values as a floor.

---

# 2. Trams

## 2.1 The measurement problem

The Ministry of Transport statutory returns give a "General Repairs and Maintenance" head per
car-mile for every year from 1913-14 to 1930-31, and it is a **combined** head: permanent way,
line electrical equipment and cars and equipment of cars together. It is therefore an upper
bound on car maintenance, not car maintenance.

This session found the split, in an Institution of Civil Engineers paper of 1914:

> "The cost of maintenance of the rolling stock — about 30 per cent. more than the average for
> English tramways — amounts to only about ¾d. per car-and-trailer-mile."
> — Gribble, *Comparative Economics of Tramways and Railless Electric Traction*, ICE Minutes of
> Proceedings 198 (1914), pp. 24-57

Amsterdam's figure is 0.75d and is 30 per cent above the English average, so the English average
rolling-stock maintenance is about **0.58d per car-mile in 1913**. The same paper states that
tramways which can afford it spend about **0.5d per car-mile on track**, with a range of 0.21d to
1.25d. Those two together are about 1.08d against the statutory combined head of 1.57d for
1913-14, which leaves roughly 0.5d for line electrical equipment and works — internally
consistent.

**Caveat.** The paper is paywalled; its text was read from a search-provider extraction of the
article, not from the printed page. The division (0.75/1.3) is the compiler's. Treat the 0.58d as
an order-of-magnitude split, not as a measured row.

## 2.2 What is measured

| Year | Group | As stated (combined head) | 1900 GBP per car-year at 28,200 car-miles | 1900 old pence per car-mile |
|---|---|---|---|---|
| 1913-14 | All, Great Britain | 1.57d | 172 | 1.47 |
| 1913-14 | Companies | 1.70d | 187 | 1.59 |
| 1922-23 | All | 4.46d | 258 | 2.20 |
| 1923-24 | All | 4.10d | 238 | 2.03 |
| 1924-25 | All | 3.68d | 214 | 1.82 |
| 1925-26 | All | 3.43d | 201 | 1.71 |
| 1927-28 | All | 3.16d | 189 | 1.61 |
| 1928-29 | All | 3.10d | 189 | 1.61 |
| 1929-30 | All | 3.04d | 190 | 1.62 |
| 1930-31 | All | 3.01d | 196 | 1.67 |
| 2025/26 | Sheffield Supertram, rolling stock only | GBP 1.37 per vehicle-mile (computed) | 405 | 2.02 |

Cars-only, using the 1914 split at 0.369 of the combined head:

| Year | Cars only, 1900 GBP per car-year | 1900 old pence per car-mile |
|---|---|---|
| 1913-14 | 64 | 0.54 |
| 1925-26 | 74 | 0.63 |
| 1930-31 | 73 | 0.62 |

The car-only rate is remarkably flat at about **GBP 65-75 a car-year in 1900 money from 1914 to
1931**, while the combined head moves by 30 per cent. That is what a vehicle-maintenance series
should look like: the track and the overhead line carried the post-war cost increase, not the
cars.

## 2.3 Recommended tram ladder

1900 GBP per car-year, at 28,200 car-miles:

| Era | Rate | Basis | Confidence |
|---|---|---|---|
| 1870-1890 | 45 | Extrapolated below 1914; horse and steam cars were simpler and cheaper to repair than electric cars | Low |
| 1890-1905 | 55 | Extrapolated | Low |
| 1905-1920 | 64 | Derived from the 1914 ICE split | Medium |
| 1920-1935 | 73 | Derived from the 1925-26 and 1930-31 heads at the 1914 ratio | Medium |
| 1935-1950 | 80 | Extrapolated; the surviving systems were old and the cars worn | Low |
| 1990-2026 | 400 | Measured (Sheffield rolling stock budget, 2025/26) | Medium |

Equivalently, if the combined statutory head is what is available for a year, use **37 per cent
of it** for the car and put the rest in the way and the electrical supply. Do not charge the
whole head to the vehicle: that overstates car maintenance by about 2.7 times.

**The gap.** There is still no measured **car-only** figure from a British undertaking. The 1914
split is a paper's average, not an account. The route to a real one is a corporation's own
abstract of accounts, where "repairs and maintenance of cars" is a separate line from "permanent
way" — Manchester, Birmingham, Glasgow, Liverpool, Leeds and Sheffield all kept such abstracts.
None is online in text form.

---

# 3. Ships and inland craft

## 3.1 What is measured

| Year | Vessel | As stated | 1900 GBP per vessel-year | Per gross ton, 1900 GBP | Source |
|---|---|---|---|---|---|
| 1849 | Patent slip hire, Llanelly | 0.5d per register ton per day | n/a | n/a | Craig 1958 |
| 1850 | GSN fleet, 44 vessels | Repairs GBP 31,896 | 788 | n/a | Forrester 2006 |
| 1855 | GSN fleet | Repairs GBP 57,771 | 1,152 | n/a | Forrester 2006 |
| 1860 | GSN fleet | Repairs GBP 41,693 | 938 | n/a | Forrester 2006 |
| 1862 | 400-500 ton ship | Sheathing GBP 120 a year | 119 | 0.25-0.31 | Mercer 1862 |
| 1908 | Stroudwater Navigation ice boat | Repairs GBP 16 1s 5d | 16 | n/a | Stroudwater minutes |
| 1913 | 50,000-ton passenger liner | Overhaul GBP 30,000 a year | 28,037 | 0.56 | Kirkaldy 1914 |
| 1924 | General cargo steamer, mid-life | 5 per cent of original investment a year | 5% of capital | 5% of capital | Martin 1924 |
| 1947 | C1-B cargo ship | USD 44,000 a year, including overhaul and repair reserve | 3,477 (at 4.03 USD/GBP) | 0.48 | MIT 1947 |
| 1947 | Liberty ship, 7,176 gt | USD 41,130 a year | 3,251 | 0.45 | MIT 1947 |
| 2003 | Handysize bulker, 28,909 dwt | USD 162,196 a year (R&M plus spares) | 1,363 | 0.08 | OpCost 2004 |
| 2003 | As above, R&M only | USD 77,155 a year | 648 | 0.04 | OpCost 2004 |
| 2013 | Eight managed vessels | USD 405,000 per docking | n/a | n/a | NTNU 2013 |
| 2020 | 50-foot narrowboat | GBP 600 general maintenance and GBP 250 blacking a year | 7 (at 2020 index 12521) | n/a | IWA |

Two things stand out.

**The per-gross-ton rate falls by an order of magnitude.** GBP 0.56 a gross ton in 1913,
GBP 0.48 in 1947, GBP 0.08 in 2003. That is not a units error: welded steel, epoxy coatings,
better pumps and shore-side workshops cut the labour content of hull and machinery upkeep by
very large factors. **A ladder built on tonnage alone will therefore misstate every era but its
own.**

**The per-vessel-year rate does not fall.** GBP 788 in 1850, GBP 3,477 in 1947, GBP 1,363 in
2003, for vessels that grew from a few hundred gross tons to about 17,000. The two statements are
consistent: cost per vessel is roughly flat in real terms while vessels got much bigger.

## 3.2 Recommended ship ladder

Because tonnage and era interact, the transportable quantity is **maintenance as a share of
hull-and-machinery capital**, not pounds per ton:

| Era | Share of capital a year | Basis | Confidence |
|---|---|---|---|
| 1850-1870 | 4.0 per cent | GSN repairs against a fleet whose capital is not stated; the share is inferred from the 1850s repair bills and typical steamer values | Low |
| 1870-1900 | 3.0 per cent | Interpolated | Low |
| 1900-1920 | 2.0 to 2.5 per cent | Measured (1913 liner overhaul alone is 2.0 per cent; running repairs would add) | Medium |
| 1920-1945 | 4.0 to 5.0 per cent | Martin's surveyor's working figure is 5 per cent | Medium |
| 1945-1970 | 4.0 per cent | Interpolated from 1947 costings | Low |
| 1970-2000 | 2.5 per cent | Interpolated | Low |
| 2000-2026 | 1.5 to 2.0 per cent | Derived from OpCost 2004 against a newbuild value | Medium |

For a `.dat` value the practical route is: take the vessel's capital price, multiply by the share
for its era, and put the result in `fixed_cost` divided by twelve. Split about 60 per cent hull
and 40 per cent machinery if the source separates them; the 1947 C1-B costing is the model
(hull USD 23,080, machinery USD 10,800).

**The gap.** No British source gives repair cost per gross ton per annum for a tramp steamer
between 1900 and 1939. Kirkaldy was downloaded in full this session and searched: the book
discusses repairs qualitatively and gives the 1913 liner overhaul, but no per-ton repair series.
The Chamber of Shipping returns were not reached. British liner and tramp accounts print "working
expenses" as one line, so the figure exists only in archival ledgers (P&O's ships' cost and
repair ledgers 1855-1941 are catalogued but not published).

## 3.3 Inland craft

The Grand Junction Canal Company tunnel tug repairs (£1 15s to £17 2s 6d a job, 1879-1890) and
the Stroudwater ice boat repair (£16 1s 5d in 1908) are per-job figures, not annual rates. The
only annual figures are modern pleasure craft: GBP 600 general maintenance plus GBP 250 blacking
on a 50-foot narrowboat in 2020. **No annual repair rate for a working narrowboat or wide boat
exists in any published source found**, and the canals' own carrying-company ledgers are
uncatalogued for this purpose. Recommend that inland boats take the ship share-of-capital rule at
the low end (1.5 per cent), flagged as an assumption.

---

# 4. Aircraft

## 4.1 What is measured

| Year | Operator and type | As stated | 1900 GBP per aircraft-year | 1900 GBP per flying hour | Source |
|---|---|---|---|---|---|
| 1956 | BEA, whole fleet | Maintenance is 25-30 per cent of total direct operating cost | n/a | n/a | Major 1956 |
| 1968/69 | British United Airways, engineering department | GBP 2.9m a year, whole department | n/a | n/a | BUA house newspaper |
| 1969/70 | BOAC Standard VC10 | GBP 130 per flying hour; total GBP 448 | 49,057 at 3,000 hours | 16.4 | Hall 1974 |
| 1969/70 | BOAC Super VC10 | GBP 123 per flying hour | 46,414 | 15.5 | Hall 1974 |
| 1969/70 | BOAC Boeing 707-436 | GBP 120 per flying hour | 45,283 | 15.1 | Hall 1974 |
| 1969/70 | BOAC Boeing 707-336 | GBP 102 per flying hour | 38,490 | 12.8 | Hall 1974 |
| 1972/73 | BOAC Standard VC10 | GBP 154 per flying hour | 45,472 | 15.2 | Hall 1974 |
| 1972/73 | BOAC Super VC10 | GBP 133 per flying hour | 39,272 | 13.1 | Hall 1974 |
| 1972/73 | BOAC Boeing 707-436 | GBP 141 per flying hour | 41,634 | 13.9 | Hall 1974 |
| 1972/73 | BOAC Boeing 707-336 | GBP 117 per flying hour | 34,547 | 11.5 | Hall 1974 |
| c.2006 | Airbus A320, benchmark | USD 635-700 per flight hour, airframe and components only | n/a | 4.2-4.6 | Aircraft Commerce 44 |
| 2013 | Airbus A320, US carriers | USD 716 per block-hour | n/a | 4.3 | US DOT Form 41 |
| 2024 | IATA MCX, 28 airlines | USD 5.05m per aircraft-year; USD 1,522 per flight hour | 25,771 | 7.8 | IATA 2026 |

The utilisation of 3,000 flying hours a year is an assumption; BOAC's long-haul VC10 fleet
probably ran 2,800-3,200. BEA's short-haul utilisation in 1957-58 was 1,731 hours for the fleet
and 2,409 for the Viscount 701, which is the only British utilisation figure measured.

## 4.2 What the shape is

In **1900 money per flying hour** the rate falls: about 16 (1969/70), 15 (1972/73), 4 to 5 (2006
benchmark and 2013), then 8 for the 2024 IATA cross-fleet average, which is higher because the
IATA sample is weighted to widebodies. In **nominal money** it rises from GBP 130 to USD 1,522.
The whole of the nominal rise and more is price level.

In **share of aircraft capital** the rate is high and falling: about 26 per cent a year for a
VC10 in 1970 (GBP 390,000 against a capital cost of about GBP 1.5m), about 10 per cent for a 2024
narrowbody (USD 5.05m against a market value of about USD 50m). That is the same shape as ships:
the real cost per unit of capacity falls, and the capital value per unit rises faster.

## 4.3 Recommended aircraft ladder

| Era | Share of aircraft capital a year | Per flying hour, 1900 GBP | Basis | Confidence |
|---|---|---|---|---|
| 1930-1945 | 25 per cent | n/a | No British money figure at all; inferred from the high labour intensity of the period | Very low |
| 1945-1960 | 22 per cent | n/a | BEA's 25-30 per cent of direct operating cost, and the 1,700-2,400 hour utilisation | Low |
| 1960-1980 | 26 per cent | 15-16 | Measured (BOAC engineering column) | High |
| 1980-2000 | 18 per cent | n/a | Interpolated | Low |
| 2000-2026 | 10 per cent | 4-8 | Measured (IATA 2024, A320 benchmarks) | Medium |

**The gap.** There is still no British money-per-flying-hour maintenance figure before 1969.
The 1930-1960 rows are inferences from a cost share and a utilisation, not measurements. The
BUA 1968/69 department total is the nearest thing to a company-level figure and it has no
denominator at all.

**A warning about deflating aircraft.** A 1900-equivalent aircraft-year of GBP 49,000 is not a
statement that an aeroplane cost GBP 49,000 to maintain in 1900; it is a statement that the
general price index rose by a factor of about 300 between 1900 and 1970. Because aircraft did not
exist in 1900, the number is only meaningful as a ratio to the aircraft's capital value deflated
by the same index. If the pakset's single `vehicle purchase` index does not track aircraft
capital, the aircraft maintenance ladder will drift against the aircraft price. **For aircraft
and ships, recommend setting the maintenance rate from the share of capital and letting the
purchase index carry the level, rather than entering a deflated 1900 figure.**

---

# 5. Horse

Already well covered in `New/ai/vehicle-cost/horse-keep-totals.md`; the rows are transcribed into
the CSV so that the ladder has them in one place. In 1900 money:

| Source | Year | 1900 GBP per horse-year |
|---|---|---|
| London General Omnibus Co., horse only | 1893 | 29 |
| Wandsworth District Board of Works, horse only | 1897 | 47 |
| Fulham Vestry, horse only | 1892 | 59 |
| London coal wharf, horse only | 1830 | 65 |
| North Metropolitan Tramways, feed only | 1886 | 25 |
| Norfolk holdings, including depreciation | 1919 | 33 |

The GBP 45 already recorded in `base-maintenance.md` sits in the middle of the 1830-1900 range and
is confirmed. The 1919 Norfolk figure deflates to GBP 33 only because the general index rose
fivefold while horse keep did not; that is a real fall, not an error, and it is the correct end
point for a horse ladder that runs past 1900.

---

# 6. Cross-mode summary

Recommended 1900 GBP per vehicle-year, mid-life, at the stated annual mileage:

| Mode and class | 1900-1914 | 1920-1940 | 1945-1960 | 1960-1980 | 1980-2026 |
|---|---|---|---|---|---|
| Bus | 180 | 120 | 75 | 110 | 350 |
| Coach | 110 | 80 | 45 | 90 | 300 |
| Trolleybus | n/a | 150 | n/a | n/a | n/a |
| Lorry, light | 45 | 35 | 45 | 65 | 90 |
| Lorry, heavy | 60 | 55 | 60 | 70-100 | 65-105 |
| Car or taxi | 18 | 15 | 20 | 30 | 50 |
| Tram car | 64 | 73 | 80 | n/a | 400 |
| Ship | 2.0-2.5% of capital | 4-5% of capital | 4% of capital | 2.5% of capital | 1.5-2% of capital |
| Aircraft | n/a | 25% of capital | 22% of capital | 26% of capital | 10% of capital |
| Horse | 45-60 | 33 (1919) | n/a | n/a | n/a |

The single most useful cross-check is the ratio to purchase price. Mid-life road vehicles come
out at **10 to 25 per cent of capital a year**; ships at 2 to 5 per cent; aircraft at 10 to 26 per
cent; a horse at more than its own purchase price. Those ratios are stable enough to sanity-check
any `.dat` pair: if `runningcost` at the expected annual mileage plus `fixed_cost` times twelve
does not land in the right share of the vehicle's price, one of the three is wrong.

---

# 7. Dead ends, recorded

1. **Ship repairs per gross ton, 1900-1939.** No British source found. Kirkaldy's *British
   Shipping* (1914) was downloaded in full and searched; it gives the 1913 liner overhaul but no
   per-ton repair series. British liner and tramp accounts print working expenses as one line.
2. **Chamber of Shipping returns.** Not reached. No published volume of repair returns was
   located.
3. **Lloyd's Register class survey fees.** No published fee schedule per vessel found; the only
   fee schedules located are flag-state ones (Norwegian Maritime Authority 2026, UK MCA via SCMS
   2026), which are certification, not classification.
4. **British aircraft maintenance per hour before 1969.** The 1949 BEA arrangement buys engines
   at a fixed hourly rate but publishes no rate. No Imperial Airways or pre-war operator figure
   exists in the sources reached.
5. **Power-by-the-hour rates.** No published schedule for any engine type, then or now.
6. **Tram car-only maintenance from a British account.** The 1914 ICE split is a paper's average,
   not an account. The 1930-31 Ministry return's detailed pages do print a "cars and equipment of
   cars" column, but the digitised text dumps the columns vertically and the values cannot be
   attributed; the printed page would have to be read.
7. **The 1918/19-1928/29 Ministry of Transport returns.** HathiTrust records them as full view
   (New York Public Library copy), but there is no accessible text layer and no page-level
   extraction route was found from this machine.
8. **`0-11.pdf` of the 1930-31 return.** Has a text layer, but the PDF could not be read: the
   fetch tool rejects `application/pdf` and no PDF text library is installed.
9. **Commercial Motor abridged Tables.** The 1933 and 1934 articles' cost tables are page images,
   so the maintenance column cannot be read even though the surrounding text is searchable.
10. **Merseyside 1983 scope.** The 53.7p per mile head is not defined, and it may include
    workshop overheads; it is an outlier against every other bus figure and should not be used
    without an adjustment.
11. **Motor vehicle maintenance before 1915.** No British figure found. The 1915 Sheffield
    account is the earliest measured point in any source reached.

---

# 8. What would close the largest gaps

In order of value to the ladder:

1. **A municipal tramways abstract of accounts with a separate "repairs of cars" line** —
   Manchester, Glasgow, Leeds or Sheffield, any year 1900-1935. This would replace the 1914
   derived split with a measured car-only rate and settle the largest single uncertainty in the
   tram ladder.
2. **A railway company's steamer account, 1900-1939.** The LNER, LMS and GWR steamer fleets were
   reported in the audited railway accounts as a separate "repairs and maintenance of steamboats"
   head, with the fleet printed in the returns. That is the most likely published route to a
   British per-vessel-year ship figure for the period the ladder is weakest.
3. **Pre-1915 motorbus and motor lorry accounts.** The Commercial Motor archive for 1905-1914
   reports municipal experiments (Eastbourne, Sheffield, Wolverhampton) and could yield two or
   three more per-vehicle-year points to replace the flat extrapolation back to 1900.
4. **Imperial Airways annual reports, 1930-1939**, for a maintenance total and a fleet count. Even
   a department total with a fleet number would give the first pre-1945 aircraft per-aircraft-year
   figure.
5. **CAA *UK Airlines* item 17 paired with a fleet or hours table, 1991-1999.** The maintenance
   pounds are published by airline; the missing half is the denominator, which is in the same
   statistical series.
