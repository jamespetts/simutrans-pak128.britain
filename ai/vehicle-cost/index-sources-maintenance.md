---
status: draft
verified: New ex-15 @ 8d0603d81
---
# Vehicle price index sources: maintenance and repair

**Covers**: the published series available for a vehicle maintenance price index, with their
identifiers, bases, coverage and annual values. Parent:
[vehicle-cost-evidence](../vehicle-cost-evidence.md). The finding is that no usable series
exists before January 1987, and that the later ones measure private motor cars.

## Maintenance and repair

## B1. ONS RPI motoring expenditure: maintenance of motor vehicles — series DOCT

- **Identifier**: DOCT, published title
  `RPI: motoring expenditure: maintenance of motor vehicles (Jan 1987=100)`.
- **Dataset**: ONS consumer price inflation time series, dataset MM23.
- **Base year**: January 1987 = 100.
- **Units**: index, not seasonally adjusted.
- **Coverage**: 1987 to 2025 annual. The published series begins in January 1987 and has no earlier
  values in this dataset.
- **URL fetched**: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/doct/mm23/data
- **Access date**: 16 November 2026.
- **Publisher caveats**: RPI is a legacy measure and ONS states that it is not a National Statistic.
  The component covers the cost of servicing and repairing motor vehicles for households; it
  excludes commercial vehicle fleets, railway rolling stock and ships. The RPI basket and weights
  have been changed repeatedly since 1987, including the 2010 and 2013 reclassifications of some
  motoring items.

Annual values:

```
1987  102.9
1988  109.3
1989  116.1
1990  127.9
1991  142.2
1992  153.4
1993  162.4
1994  166.4
1995  169.6
1996  177.3
1997  186.9
1998  194.6
1999  202.2
2000  210.6
2001  220.9
2002  232.3
2003  246.2
2004  261.1
2005  277.0
2006  293.9
2007  309.0
2008  327.2
2009  340.6
2010  356.6
2011  374.2
2012  381.1
2013  390.4
2014  400.8
2015  408.2
2016  415.1
2017  426.4
2018  441.6
2019  454.0
2020  466.4
2021  481.3
2022  515.6
2023  555.8
2024  593.8
2025  633.6
```

2026, published quarters: 2026 Q1 = 658.1, 2026 Q2 = 673.7, 2026 Q3 = 673.4.

## B2. ONS CPI 07.2.3 Maintenance and repairs of personal transport equipment — series D7ED

- **Identifier**: D7ED, published title `CPI INDEX 07.2.3 : MAINTENANCE & REPAIRS 2015=100`.
- **Dataset**: ONS consumer price inflation time series, dataset MM23.
- **Base year**: 2015 = 100.
- **Units**: index, not seasonally adjusted.
- **Coverage**: 1988 to 2025 annual. The published series begins in 1988, one year later than DOCT.
- **URL fetched**: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7ed/mm23/data
- **Access date**: 16 November 2026.
- **Publisher caveats**: as A1 on annual reweighting. The class is the maintenance and repair
  component of COICOP 07.2 "operation of personal transport equipment"; it is a household consumer
  index and not a fleet or industrial maintenance index.

Annual values:

```
1988  25.6
1989  27.5
1990  30.9
1991  34.4
1992  36.7
1993  38.4
1994  39.6
1995  40.7
1996  42.4
1997  44.6
1998  46.7
1999  48.8
2000  51.2
2001  54.6
2002  57.6
2003  61.6
2004  65.8
2005  70.3
2006  74.6
2007  78.3
2008  82.5
2009  85.1
2010  88.5
2011  92.6
2012  94.1
2013  95.8
2014  97.9
2015  100.0
2016  101.7
2017  104.0
2018  107.5
2019  110.2
2020  112.7
2021  115.0
2022  122.9
2023  132.7
2024  141.9
2025  150.9
```

2026, published quarters: 2026 Q1 = 156.9, 2026 Q2 = 160.9, 2026 Q3 = 160.4.

## B3. ONS CPIH 07.2.3 Maintenance and repairs — series L54A

- **Identifier**: L54A, published title `CPIH INDEX 07.2.3 : MAINTENANCE & REPAIRS 2015=100`.
- **Dataset**: ONS consumer price inflation time series, dataset MM23.
- **Base year**: 2015 = 100.
- **Units**: index, not seasonally adjusted.
- **Coverage**: 1988 to 2025 annual.
- **URL fetched**: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l54a/mm23/data
- **Access date**: 16 November 2026.
- **Caveat specific to this pair**: in the 16 November 2026 vintage, every annual value of L54A is
  identical to the corresponding value of D7ED. The two series are nevertheless distinct
  identifiers in distinct measures and are recorded separately. Their values are therefore not
  repeated here: read the D7ED block in B2 for the L54A annual values, 1988-2025.
- **Publisher caveats**: as A2.

## B4. Feinstein 1972, Table 65, column 1 — average weekly wage rates

- **Identifier**: Feinstein 1972, Table 65, "Indices of wage rates, wage earnings and retail prices,
  1855-1965", column (1) "Average weekly wage rates".
- **Base year**: 1913 = 100.
- **Units**: index.
- **Coverage**: 1855 to 1965 annual, unbroken.
- **URL fetched**: as A4 (sheet `Table 65`).
- **Access date**: 16 November 2026.
- **Publisher caveats**: this is an economy-wide wage rate index, not an engineering or railway
  wage index. It measures rates, not earnings, so it ignores changes in hours and in the composition
  of the workforce. It is recorded here because no engineering-specific wage index covering
  1855-1965 was found in machine-readable form.

Annual values:

```
1855=72, 1856=72, 1857=69, 1858=68, 1859=68, 1860=69, 1861=69, 1862=70
1863=71, 1864=74, 1865=76, 1866=78, 1867=77, 1868=76, 1869=76, 1870=78
1871=81, 1872=86, 1873=90, 1874=91, 1875=89, 1876=88, 1877=87, 1878=85
1879=83, 1880=83, 1881=83, 1882=83, 1883=84, 1884=84, 1885=83, 1886=83
1887=83, 1888=83, 1889=86, 1890=90, 1891=90, 1892=89, 1893=88, 1894=88
1895=87, 1896=88, 1897=89, 1898=91, 1899=93, 1900=97, 1901=95, 1902=94
1903=93, 1904=93, 1905=92, 1906=94, 1907=94, 1908=94, 1909=94, 1910=94
1911=95, 1912=98, 1913=100, 1914=101, 1915=108, 1916=118, 1917=139, 1918=179
1919=215, 1920=257, 1921=256, 1922=198, 1923=176, 1924=178, 1925=181, 1926=181
1927=179, 1928=177, 1929=176, 1930=175, 1931=173, 1932=170, 1933=168, 1934=168
1935=170, 1936=173, 1937=180, 1938=185, 1939=187, 1940=207, 1941=226, 1942=242
1943=254, 1944=267, 1945=280, 1946=302, 1947=313, 1948=329, 1949=337, 1950=344
1951=373, 1952=403, 1953=422, 1954=441, 1955=470, 1956=507, 1957=533, 1958=552
1959=567, 1960=581, 1961=606, 1962=628, 1963=651, 1964=681, 1965=711
```

## B5. Feinstein 1972, Table 65, column 2 — average weekly wage earnings

- **Identifier**: Feinstein 1972, Table 65, column (2) "Average weekly wage earnings".
- **Base year**: 1913 = 100.
- **Units**: index.
- **Coverage**: 1855 to 1938, then 1940 to 1965. There is no published value for 1939.
- **URL fetched**: as A4.
- **Access date**: 16 November 2026.
- **Publisher caveats**: as B4, plus a discontinuity that the source does not explain: the index
  falls from 468 in 1949 to 400 in 1950 and then rises to 538 in 1951. A 15 per cent fall in
  average weekly earnings in 1950 is not credible, so this is a break in the series, most probably
  a change of source at 1950. The column should not be used across that break without further work.

Annual values:

```
1855=59, 1856=59, 1857=57, 1858=56, 1859=57, 1860=58, 1861=58, 1862=58
1863=60, 1864=60, 1865=62, 1866=66, 1867=66, 1868=64, 1869=64, 1870=66
1871=69, 1872=76, 1873=83, 1874=81, 1875=80, 1876=79, 1877=78, 1878=75
1879=73, 1880=73, 1881=73, 1882=76, 1883=76, 1884=76, 1885=74, 1886=73
1887=74, 1888=76, 1889=81, 1890=84, 1891=84, 1892=84, 1893=84, 1894=84
1895=84, 1896=84, 1897=85, 1898=88, 1899=90, 1900=95, 1901=94, 1902=92
1903=92, 1904=90, 1905=90, 1906=92, 1907=97, 1908=95, 1909=95, 1910=95
1911=96, 1912=99, 1913=100, 1914=101, 1915=117, 1916=133, 1917=170, 1918=211
1919=241, 1920=278, 1921=260, 1922=209, 1923=193, 1924=196, 1925=198, 1926=193
1927=197, 1928=194, 1929=195, 1930=193, 1931=189, 1932=185, 1933=184, 1934=186
1935=189, 1936=194, 1937=199, 1938=207, 1940=269, 1941=294, 1942=331, 1943=364
1944=370, 1945=368, 1946=383, 1947=412, 1948=449, 1949=468, 1950=400, 1951=538
1952=582, 1953=617, 1954=657, 1955=713, 1956=771, 1957=813, 1958=841, 1959=864
1960=914, 1961=978, 1962=1012, 1963=1055, 1964=1147, 1965=1240
```

## B6. Before 1987 — statement of what does not exist

No published index of motor vehicle maintenance or repair prices for the United Kingdom before
January 1987 was found. The ONS MM23 dataset, which carries the current CPI and RPI series, contains
the maintenance-of-motor-vehicles index only from January 1987; the dataset does not carry any
earlier version of that component.

No engineering-specific wage index, no metal goods price index specific to vehicle repair, and no
railway repair cost index were found in machine-readable form for the period before 1987. The
available published substitutes are:

- economy-wide wage rates and earnings, 1855-1965 (B4 and B5);
- the plant and machinery capital goods price index, 1855-1965 (A7), as a proxy for the materials
  and equipment bought in by a repair workshop;
- the total capital goods price index, 1870-1965 (A8).

The period 1966 to 1986 is not covered by any of them. That gap is real and is not filled here.

---

# Assessment

## A. Purchase price of transport equipment

Covered by real published numbers:

- **1850s-1890s**: Feinstein Table 63 railway rolling stock from 1856, ships from 1855, plant and
  machinery from 1855; Feinstein Table 61 capital goods from 1870. Road vehicles are not covered
  before 1900.
- **1900s-1910s**: all of the above plus Feinstein Table 63 road vehicles from 1900.
- **1920s-1930s**: Feinstein Table 63 (to 1938) and Sefton and Weale current-price GFCF from 1920,
  so the decade is covered twice by independent published estimates.
- **1940s**: Sefton and Weale current prices cover the whole decade. Feinstein's road vehicle and
  railway rolling stock columns are blank for 1939-1947; those years are missing, and his 1938-1948
  link rests on Blue Book 1957 Tables 48-49 with Redfern's interpolation used behind the series.
- **1950s-1960s**: Feinstein Table 63 to 1965 and Sefton and Weale to 1990.
- **1970s-1980s**: Sefton and Weale only, at the asset level "vehicles, ships and aircraft", current
  prices 1920-1990 and constant prices in the 1948-1990 block. No vehicle-specific price index for
  this window was found.
- **1987**: ONS DOCS only.
- **1988-1995**: ONS D7CO and DOCS.
- **1996-2025**: ONS D7CO, L544 and DOCS.
- **2026**: published quarters only; no annual average yet.

Not covered:

- Before 1855: no series.
- 1855-1899 for road vehicles: no series before 1900.
- A single continuous transport-equipment purchase price index across 1855-2026: none exists. The
  three families (Feinstein to 1965, Sefton and Weale 1920-1990, ONS from 1987/88) overlap but are
  separate published series on separate bases.

## B. Maintenance and repair price index

Covered by real published numbers:

- **1850s-1965**: Feinstein Table 65 wage rates, continuous 1855-1965; Table 65 earnings with a break
  at 1949/50 and no 1939 value; Table 63 plant and machinery prices 1855-1965 as a materials proxy.
- **1987-2025**: ONS DOCT.
- **1988-2025**: ONS D7ED and L54A.
- **2026**: published quarters only.

Not covered:

- **1966-1986**: no series. This is the whole of the gap between the end of Feinstein and the start
  of the RPI component.
- Before 1855: no series.
- Any period before 1987 at the level of motor vehicle maintenance specifically: nothing published
  was found. The pre-1987 entries are labour cost and materials proxies, not maintenance prices.

## Consequence for the two target series

Neither target series can be built as one published index over 1750-2026. Each needs at least three
published series joined end to end, and the maintenance series needs a decision about what to use
for 1966-1986 that no published number currently answers.
