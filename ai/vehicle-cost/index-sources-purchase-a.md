---
status: draft
verified: New ex-15 @ 8d0603d81
---
# Vehicle price index sources: purchase, part 1

Parent: [vehicle-cost-evidence](../vehicle-cost-evidence.md).

Data collection for the `vehicle purchase` index series: the published index and value series for
transport equipment prices, as annual numbers. Part 2 covers Feinstein's ships, plant and
machinery and capital goods, the Sefton and Weale values, and the series checked and rejected:
[index-sources-purchase-b](index-sources-purchase-b.md).

Compiled 16 November 2026. Every value below was read from the publisher's own file on that date.
Values are transcribed as published, including the published number of decimal places. Nothing has
been rebased, spliced, interpolated, converted or rounded. Where a series is discontinuous, the
discontinuity is recorded rather than repaired.

Annual values for the ONS series are the published annual averages (the mean of the twelve monthly
index values), not December values. The ONS annual average for 2026 does not exist at the access
date: the ONS publishes it with the January 2027 release. For 2026 the published quarterly and
monthly values are given instead.

---

# Part A. Purchase price of transport equipment

## A1. ONS CPI 07.1 Purchase of vehicles — series D7CO

- **Identifier**: D7CO, published title `CPI INDEX 07.1 : PURCHASE OF VEHICLES 2015=100`.
  07.1 is a COICOP group within division 07 (transport); it is not itself a division.
- **Dataset**: ONS consumer price inflation time series, dataset MM23.
- **Base year**: 2015 = 100.
- **Units**: index, not seasonally adjusted.
- **Frequency published**: monthly, with quarterly and annual averages.
- **Coverage**: 1988 to 2025 annual. Series begins 1988.
- **URL fetched**: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/d7co/mm23/data
- **Access date**: 16 November 2026.
- **Publisher caveats**: CPI weights are updated each January, so the fixed-weight basket changes
  annually and the index is a chain of year-on-year changes, not a fixed-basket comparison over the
  whole run. Class 07.1 is composed of 07.1.1A new cars, 07.1.1B second-hand cars and 07.1.2/3
  motorcycles and bicycles (class list verified in the MM23 dataset, 16 November 2026); it is
  therefore a consumer purchase index, not a capital goods index, and it contains no railway
  rolling stock, ships, aircraft or commercial goods vehicles.

Annual values:

```
1988  91.2
1989  94.4
1990  96.4
1991  100.9
1992  106.1
1993  104.9
1994  107.4
1995  109.2
1996  112.0
1997  114.4
1998  113.5
1999  109.8
2000  104.3
2001  100.8
2002  99.9
2003  99.3
2004  99.5
2005  98.5
2006  98.0
2007  97.9
2008  95.9
2009  97.2
2010  101.4
2011  102.2
2012  101.5
2013  100.6
2014  100.9
2015  100.0
2016  98.5
2017  99.9
2018  103.2
2019  104.6
2020  108.0
2021  116.1
2022  125.2
2023  126.4
2024  122.9
2025  124.8
```

2026, published quarters: 2026 Q1 = 125.0, 2026 Q2 = 125.0, 2026 Q3 = 123.5. Published months to
September 2026: Jul 123.7, Aug 123.5, Sep 123.3. No 2026 annual average exists at the access date.

## A2. ONS CPIH 07.1.1A New cars — series L544

- **Identifier**: L544, published title `CPIH INDEX 07.1.1A : NEW CARS 2015=100`.
- **Dataset**: ONS consumer price inflation time series, dataset MM23.
- **Base year**: 2015 = 100.
- **Units**: index, not seasonally adjusted.
- **Coverage**: 1996 to 2025 annual. The published series begins in 1996; it does not run back to
  1988 with D7CO.
- **URL fetched**: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/l544/mm23/data
- **Access date**: 16 November 2026.
- **Publisher caveats**: as A1, and in addition CPIH includes owner occupiers' housing costs, which
  are irrelevant to this class; the class index itself is unaffected. The series is a new-car price
  index only, so it excludes the second-hand market in which most vehicle transactions occur.

Annual values:

```
1996  86.7
1997  88.5
1998  90.0
1999  89.1
2000  86.5
2001  82.6
2002  82.3
2003  82.9
2004  84.8
2005  86.3
2006  87.1
2007  88.4
2008  89.5
2009  90.6
2010  93.7
2011  96.8
2012  97.6
2013  97.1
2014  98.0
2015  100.0
2016  100.6
2017  103.6
2018  108.1
2019  112.2
2020  115.4
2021  119.4
2022  126.5
2023  132.6
2024  135.6
2025  139.5
```

2026, published quarters: 2026 Q1 = 140.7, 2026 Q2 = 141.0, 2026 Q3 = 140.9.

## A3. ONS RPI motoring expenditure: purchase of motor vehicles — series DOCS

Supplementary. This is the only ONS motor-vehicle purchase index that runs from 1987, one year
earlier than D7CO, and it is on the RPI basis rather than the CPI basis.

- **Identifier**: DOCS, published title
  `RPI: motoring expenditure: purchase of motor vehicles (Jan 1987=100)`.
- **Dataset**: ONS consumer price inflation time series, dataset MM23.
- **Base year**: January 1987 = 100.
- **Units**: index, not seasonally adjusted.
- **Coverage**: 1987 to 2025 annual.
- **URL fetched**: https://www.ons.gov.uk/economy/inflationandpriceindices/timeseries/docs/mm23/data
- **Access date**: 16 November 2026.
- **Publisher caveats**: the RPI is a legacy measure; ONS states that it is not a National
  Statistic. The RPI uses a different formula (Carli/Jevons arithmetic) and a different basket from
  the CPI, so DOCS and D7CO are not interchangeable and their levels are not comparable.

Annual values:

```
1987  105.0
1988  111.1
1989  115.1
1990  117.4
1991  123.1
1992  129.4
1993  128.1
1994  131.5
1995  133.6
1996  138.0
1997  141.3
1998  139.8
1999  133.8
2000  126.6
2001  124.8
2002  122.3
2003  118.9
2004  115.2
2005  109.2
2006  106.2
2007  103.4
2008  96.3
2009  95.6
2010  101.3
2011  99.5
2012  97.5
2013  96.3
2014  96.3
2015  94.2
2016  91.8
2017  92.2
2018  95.0
2019  95.4
2020  98.5
2021  106.7
2022  116.9
2023  117.9
2024  114.5
2025  116.4
```

2026, published quarters: 2026 Q1 = 116.5, 2026 Q2 = 116.5, 2026 Q3 = 115.2.

## A4. Feinstein 1972, Table 63, column 7 — road vehicles

- **Identifier**: C. H. Feinstein, *National Income, Expenditure and Output of the United Kingdom
  1855-1965* (Cambridge University Press, 1972), Table 63, "Price indices for capital goods,
  1855-1965", column (7) "Road vehicles".
- **Base year**: 1913 = 100.
- **Units**: index.
- **Coverage**: 1900 to 1965 annual. Published values exist for every year in that range.
- **File fetched**:
  https://escoe-website.s3.amazonaws.com/wp-content/uploads/2018/10/02122909/TABLES-Feinstein-1972-National-Income-Expenditure-and-Output-of-the-United-Kingdom-1855-1965.xlsx
  (sheet `Table 63`), linked from https://www.escoe.ac.uk/research/historical-data/national-accounts/
- **Access date**: 16 November 2026.
- **Publisher caveats**: Feinstein's own source note records that 1900-1920 comes from Table 24 row
  (7) and Table 25 row (7); that 1920-1938 is a current-weighted average of his indices for goods
  vehicles, buses and taxis, and passenger cars (Feinstein [162], pp. 158-9); and that 1938-1948
  comes from Blue Book 1957 Tables 48 and 49, with Redfern (p. 171) used for interpolation of
  1939-1947 in constructing the series. The printed table nevertheless carries no values for
  1939-1947: the entries jump from 1938 to 1948. Those years are missing from this source, not
  merely interpolated within it.
  The index is a capital goods price index, not a transaction price index for vehicles sold second-hand.

Annual values:

```
1900=113, 1901=115, 1902=116, 1903=118, 1904=119, 1905=120, 1906=122, 1907=123
1908=123, 1909=123, 1910=123, 1911=123, 1912=123, 1913=100, 1914=100, 1915=109
1916=147, 1917=176, 1918=206, 1919=195, 1920=210, 1921=188, 1922=164, 1923=148
1924=141, 1925=141, 1926=129, 1927=122, 1928=115, 1929=110, 1930=114, 1931=114
1932=105, 1933=98, 1934=89, 1935=90, 1936=89, 1937=91, 1938=96, 1948=205.4
1949=212.8, 1950=223.3, 1951=263.5, 1952=295, 1953=279.5, 1954=274.6, 1955=274.6, 1956=294
1957=304.5, 1958=308.9, 1959=297.1, 1960=291.9, 1961=296.2, 1962=302.4, 1963=281.7, 1964=287.9
1965=289.7
```

## A5. Feinstein 1972, Table 63, column 6 — railway rolling stock

- **Identifier**: Feinstein 1972, Table 63, column (6) "Railway rolling stock".
- **Base year**: 1913 = 100.
- **Units**: index.
- **Coverage**: 1856 to 1938 annual, then 1948 only. The published table is blank for 1939-1947.
  There are no values after 1948: from 1949 the column is merged with ships and aircraft.
- **URL fetched**: as A4.
- **Access date**: 16 November 2026.
- **Publisher caveats**: table note (b) states "From 1949 includes aircraft; the combined index for
  railway rolling stock, ships and aircraft for 1948 (1913 = 100) is 431.2". The 1856-1920 figures
  are indices of costs of labour and materials described in Feinstein chapter 9; 1920-1938 uses
  Feinstein [162] p. 150.

Annual values:

```
1856=97.7, 1857=90.9, 1858=83.1, 1859=85.5, 1860=87.2, 1861=81.1, 1862=81.8, 1863=87.9
1864=89.7, 1865=88.7, 1866=87.6, 1867=83.6, 1868=83.1, 1869=84.1, 1870=86.5, 1871=85.7
1872=103.8, 1873=113.3, 1874=106, 1875=95.4, 1876=91.2, 1877=89, 1878=84.6, 1879=76.9
1880=87.6, 1881=84.7, 1882=85.2, 1883=81.6, 1884=77.9, 1885=76.1, 1886=76.1, 1887=77.9
1888=77.9, 1889=80.2, 1890=85.9, 1891=81.5, 1892=80, 1893=79.5, 1894=77.3, 1895=79.1
1896=81, 1897=82.7, 1898=84.8, 1899=94.6, 1900=102.3, 1901=90.9, 1902=89, 1903=91.2
1904=87.3, 1905=92.1, 1906=94.4, 1907=96.3, 1908=93.1, 1909=89.8, 1910=91.3, 1911=92.6
1912=97.4, 1913=100, 1914=98.6, 1915=112.5, 1916=145.4, 1917=174.9, 1918=183, 1919=229.3
1920=231.6, 1921=233.4, 1922=238.5, 1923=149.8, 1924=142.8, 1925=140.5, 1926=132.3, 1927=116.6
1928=119.3, 1929=119.3, 1930=128, 1931=127.2, 1932=126.3, 1933=127.5, 1934=127.9, 1935=133.4
1936=131.2, 1937=127.4, 1938=132.8, 1948=360.5
```

Continued in [index-sources-purchase-b](index-sources-purchase-b.md).
