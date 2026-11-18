---
status: draft
verified: New ex-15 @ 8d0603d81
---
# Published transport-equipment deflator, United Kingdom, 1938-1990

**Covers**: the search for a published transport-equipment deflator, the Blue Book current and
constant price series that replace it, and the Feinstein plant and machinery bridge. Parent:
[vehicle-cost-evidence](../vehicle-cost-evidence.md).

Research note compiled 16 November 2026. Purpose: find a published deflator for transport
equipment to replace the derived Sefton and Weale GFCF ratio for 1938-1990.

Every figure below was read from the publisher's own file or from a digitised copy of the
publisher's own table on the access date. Nothing has been rebased, spliced, interpolated or
rounded. Where a series is only published as current-price and constant-price values, both are
recorded and labelled as values; no ratio is computed anywhere in this note.

---

## 1. The central finding

**No published annual price index for transport equipment covering 1938-1990 was found.** The
United Kingdom national accounts have never, in the vintages examined, published an asset-level
gross fixed capital formation (GFCF) price index. They publish, at asset level, a current-price
value series and a constant-price value series; the asset deflator exists only as the arithmetic
relation between the two.

This is not an inference from a search failure. It was verified in three separate official
publications spanning forty years:

- **National Income and Expenditure 1969** (CSO), Section XI, Tables 51-64: gross domestic fixed
  capital formation is tabulated "at current and 1963 prices" by sector and by type of asset. The
  section contains no index-number table.
- **Blue Book 1997**, Tables 13.1-13.5 (`bb97.xlsx`, sheet index): "at current market prices" and
  "at constant 1990 market prices". No index table. No series in the workbook carries the word
  "deflator".
- **Blue Book time series file** (`bb.csdb`): the complete series dictionary was searched in two
  vintages — the superseded 2015 file (header `020151030BB`, 1,862,723 bytes) and the current
  2026 file (header `020261030BB`, 3,104,754 bytes). In the current file, 15 lines contain the
  string "deflator" and none of them is an asset-level deflator; the only GFCF deflator is
  `Gross fixed capital formation deflator: SA`, which is whole-economy and has no asset split.
  There is exactly one asset-level GFCF series headed "Vehicles, Ships & Aircraft", the chained
  volume measure `Gross Fixed Capital Formation: Vehicles, Ships & Aircraft: CVM NSA: £m`, which
  starts in 1987. Section 7 gives that series and its current-price counterpart in full.

Consequence: for 1938-1990 the only published asset-specific numbers are (a) Feinstein's explicit
price indices, which end in 1965 and are blank for 1939-1947 in the vehicle columns, and (b) the
official current-price and constant-price value pairs, of which the longest run at asset level is
Blue Book 1997, covering 1965-1997 on the constant-price side and 1948-1997 on the current-price
side.

---

## 2. Series S1 — Blue Book 1997, Table 13.2, vehicles, ships and aircraft, current prices

- **Exact identifier**: *United Kingdom National Accounts 1997* (Blue Book 1997), Table 13.2,
  "Gross fixed capital formation by type of asset at current market prices". Sector heading `UK`,
  price basis `CP NSA`, flow `GFCF`. Column headings and CDIDs:
  `Buses and coaches` DFKA; `Other road vehicles` DFKB; `Railway rolling stock` DFKC;
  `Ships` GGBU; `Aircraft` GGBV; `Vehicles, ships and aircraft` DFEJ.
- **Type**: value series, £ million, current prices. Not an index.
- **Price base**: none needed; current prices of each year.
- **Coverage**: DFEJ runs 1948-1997 with no gaps. The five components run 1965-1997 with no gaps.
  Values for 1998 Q1 also exist in the file but are quarterly and are not recorded here.
- **File fetched**: https://escoe-website.s3.amazonaws.com/wp-content/uploads/2018/10/16202313/Anne-Harrison-BB97.xlsx
  (sheet `T 13.2 gfcf2`), linked from
  https://www.escoe.ac.uk/research/historical-data/national-accounts/ as "Fifty Years of UK
  National Accounts - Blue Book data 1948 to 1997".
- **Access date**: 16 November 2026.
- **Publisher caveats**: the file was constructed on behalf of the ONS by Anne Harrison from ONS
  computer files, and its `Guide` sheet states that the tables are "actually consistent with the
  last quarterly accounts published before Blue Book 1998, that is containing data up to 1998
  quarter 1", so the 1997 observation exists although it does not appear in Blue Book 1997. Where
  figures did not reach back far enough in the ONS files they were "retrieved from the printed
  publications". Figures derived by applying an accounting identity are shown in red in the
  original; the cells transcribed below were read as plain numbers.

`DFEJ`, vehicles, ships and aircraft, £ million, current prices:

```
1948=249, 1949=272, 1950=262, 1951=256, 1952=260, 1953=308, 1954=332, 1955=369
1956=426, 1957=498, 1958=530, 1959=571, 1960=636, 1961=598, 1962=516, 1963=515
1964=621, 1965=613, 1966=563, 1967=633, 1968=801, 1969=843, 1970=968, 1971=1093
1972=1321, 1973=1621, 1974=1786, 1975=1989, 1976=2285, 1977=3151, 1978=4004, 1979=4684
1980=4566, 1981=3846, 1982=4285, 1983=4530, 1984=5664, 1985=6439, 1986=6222, 1987=7805
1988=8849, 1989=10324, 1990=10266, 1991=8647, 1992=8710, 1993=10000, 1994=11499, 1995=11190
1996=11844, 1997=13895
```

Components, £ million, current prices, 1965-1997:

`DFKA` buses and coaches:

```
1965=29, 1966=29, 1967=28, 1968=32, 1969=29, 1970=41, 1971=50, 1972=52
1973=60, 1974=58, 1975=85, 1976=120, 1977=126, 1978=157, 1979=173, 1980=175
1981=153, 1982=132, 1983=153, 1984=117, 1985=122, 1986=125, 1987=166, 1988=199
1989=179, 1990=164, 1991=139, 1992=116, 1993=149, 1994=142, 1995=142, 1996=202
1997=169
```

`DFKB` other road vehicles:

```
1965=391, 1966=406, 1967=410, 1968=443, 1969=496, 1970=532, 1971=573, 1972=666
1973=818, 1974=1012, 1975=1102, 1976=1484, 1977=2206, 1978=2955, 1979=3718, 1980=3208
1981=2971, 1982=3710, 1983=3676, 1984=4302, 1985=4970, 1986=5329, 1987=6754, 1988=7677
1989=8603, 1990=8013, 1991=6532, 1992=6807, 1993=7559, 1994=8497, 1995=9710, 1996=10350
1997=10751
```

`DFKC` railway rolling stock:

```
1965=47, 1966=33, 1967=25, 1968=30, 1969=17, 1970=21, 1971=16, 1972=29
1973=38, 1974=47, 1975=59, 1976=57, 1977=79, 1978=98, 1979=126, 1980=163
1981=136, 1982=123, 1983=101, 1984=75, 1985=106, 1986=95, 1987=126, 1988=187
1989=242, 1990=377, 1991=363, 1992=504, 1993=591, 1994=393, 1995=224, 1996=80
1997=42
```

`GGBU` ships:

```
1965=105, 1966=76, 1967=134, 1968=210, 1969=258, 1970=275, 1971=339, 1972=482
1973=626, 1974=580, 1975=639, 1976=433, 1977=528, 1978=533, 1979=308, 1980=355
1981=221, 1982=326, 1983=284, 1984=502, 1985=332, 1986=162, 1987=239, 1988=116
1989=122, 1990=234, 1991=500, 1992=119, 1993=363, 1994=684, 1995=695, 1996=78
1997=109
```

`GGBV` aircraft:

```
1965=41, 1966=19, 1967=36, 1968=86, 1969=43, 1970=99, 1971=115, 1972=92
1973=79, 1974=89, 1975=104, 1976=191, 1977=212, 1978=261, 1979=359, 1980=665
1981=365, 1982=-6, 1983=316, 1984=668, 1985=909, 1986=511, 1987=520, 1988=670
1989=1178, 1990=1478, 1991=1113, 1992=1164, 1993=1338, 1994=1783, 1995=419, 1996=1134
1997=2824
```

Note that `GGBV` is negative in 1982. That is a published negative value (disposals exceeded
acquisitions in the aircraft component that year), not a transcription error, and it is a further
reason not to build a deflator from these components for that year.

---

## 3. Series S2 — Blue Book 1997, Table 13.4, transport equipment, constant 1990 prices

- **Exact identifier**: Blue Book 1997, Table 13.4, "Gross fixed capital formation by type of asset
  at constant 1990 market prices". Sector heading `UK`, price basis `KP 90`, flow `GFCF`. Column
  headings and CDIDs: `Buses and coaches` DFKF; `Other road vehicles` DFKG;
  `Railway rolling stock, ships and aircraft` DFKH; `Plant and machinery` DFCY;
  `Dwellings` DFDV; `Other new buildings and works` DFKE; `Costs of ownership transfer` DFDW;
  `Total gross fixed capital formation` DFDM.
- **Type**: value series, £ million, constant 1990 market prices. Not an index.
- **Price base**: 1990, stated in the table title and in the `KP 90` column header.
- **Coverage**: 1965-1997 with no gaps. The sheet contains year rows from 1948 but every cell in
  1948-1964 is empty for these columns: the constant-price asset breakdown is published only from
  1965. Values for 1998 Q1 exist and are not recorded here.
- **Important structural caveat**: this table has three vehicle lines, not five. `Railway rolling
  stock, ships and aircraft` is a single combined column, so the constant-price table cannot be
  matched to `DFKC`, `GGBU` and `GGBV` separately. There is no published constant-price total
  column for "vehicles, ships and aircraft" in this table; the three vehicle lines must be added
  to obtain one.
- **File fetched and access date**: as S1 (sheet `T 13.4 gfcf4`).
- **Publisher caveats**: the `Guide` sheet states: "For the constant price data it is not possible to
  conduct such rigorous checking since the identities do not hold for earlier years... Long-run
  constant price series are derived by chain linking when the base year changed... In Blue Book
  1997, the base year is 1990 and additivity holds only from 1986." Article: the 1990-price figures
  for 1965-1985 are a chain-linked construct across the base years 1958, 1963, 1970, 1975, 1980 and
  1985. They are official, but they are not a single fixed-basket revaluation, and any deflator
  formed from them inherits the chain-linking.

`DFKF` buses and coaches, £ million, 1990 prices:

```
1965=286, 1966=295, 1967=277, 1968=296, 1969=269, 1970=340, 1971=376, 1972=376
1973=416, 1974=369, 1975=374, 1976=437, 1977=378, 1978=392, 1979=380, 1980=332
1981=265, 1982=215, 1983=254, 1984=174, 1985=170, 1986=163, 1987=193, 1988=233
1989=190, 1990=164, 1991=151, 1992=124, 1993=131, 1994=154, 1995=142, 1996=181
1997=157
```

`DFKG` other road vehicles, £ million, 1990 prices:

```
1965=4377, 1966=4463, 1967=4473, 1968=4795, 1969=5049, 1970=5078, 1971=4955, 1972=5401
1973=6059, 1974=6413, 1975=5176, 1976=5825, 1977=7079, 1978=8102, 1979=9112, 1980=6681
1981=5766, 1982=6569, 1983=6396, 1984=7056, 1985=7527, 1986=7454, 1987=8672, 1988=9083
1989=9422, 1990=8013, 1991=5963, 1992=6029, 1993=6567, 1994=7246, 1995=8228, 1996=8519
1997=8828
```

`DFKH` railway rolling stock, ships and aircraft, £ million, 1990 prices:

```
1965=1283, 1966=827, 1967=1267, 1968=2029, 1969=1847, 1970=2115, 1971=2352, 1972=2803
1973=3124, 1974=2604, 1975=2542, 1976=1849, 1977=1849, 1978=1833, 1979=1470, 1980=1995
1981=1081, 1982=636, 1983=925, 1984=1580, 1985=1617, 1986=876, 1987=981, 1988=1056
1989=1619, 1990=2089, 1991=1894, 1992=1634, 1993=2029, 1994=2474, 1995=1080, 1996=1032
1997=2375
```

`DFCY` plant and machinery, £ million, 1990 prices (recorded only as a comparator; it is not a
vehicle series):

```
1965=14617, 1966=15605, 1967=16238, 1968=16589, 1969=16541, 1970=17741, 1971=17412, 1972=16752
1973=18828, 1974=19384, 1975=18505, 1976=19166, 1977=19428, 1978=20775, 1979=22390, 1980=22304
1981=20726, 1982=20963, 1983=22010, 1984=24083, 1985=27081, 1986=27512, 1987=29086, 1988=33770
1989=37925, 1990=36762, 1991=33955, 1992=32602, 1993=31749, 1994=33705, 1995=36352, 1996=37012
1997=38404
```

Internal check on the base year and the column mapping: for 1990 the three constant-price vehicle
lines sum to 164 + 8013 + 2089 = 10266, which equals `DFEJ` (10266) in S1. This confirms both that
the table is at 1990 prices and that the columns transcribed above are the intended ones. The same
equality does not hold for 1985 or earlier, which is consistent with the publisher's statement that
additivity holds only from 1986.

---

## 4. Series S3 — Feinstein 1972, Table 63, column 4, plant and machinery: the 1938-1948 bridge

- **Exact identifier**: C. H. Feinstein, *National Income, Expenditure and Output of the United
  Kingdom 1855-1965* (Cambridge University Press, 1972), Table 63, "Price indices for capital
  goods", column (4) "Plant and machinery".
- **Type**: index number. **Base**: 1913 = 100.
- **Coverage**: 1855-1965, unbroken. Unlike columns (5) ships, (6) railway rolling stock and
  (7) road vehicles, column (4) carries values for every year of the Second World War.
- **File fetched**: https://escoe-website.s3.amazonaws.com/wp-content/uploads/2018/10/02122909/TABLES-Feinstein-1972-National-Income-Expenditure-and-Output-of-the-United-Kingdom-1855-1965.xlsx
  (sheet `Table 63`), linked from https://www.escoe.ac.uk/research/historical-data/national-accounts/
- **Access date**: 16 November 2026.
- **Publisher caveats**: this is not a vehicle index. It is the price index for plant and machinery
  as a capital good, built from engineering costs of labour and materials. It is recorded here
  because it is the only published explicit index of engineering capital goods that spans
  1938-1948 without a gap.

1938-1948, 1913 = 100:

```
1938=140.8, 1939=147.1, 1940=162.7, 1941=181.5, 1942=200.2, 1943=231.5
1944=244.1, 1945=244.1, 1946=244.1, 1947=281.6, 1948=312.9
```

The values for 1938-1948 are the only ones this note records from Feinstein, because they are the
only ones that answer the 1938-1948 part of the brief. Feinstein's vehicle columns are already
transcribed in `vehicle-index-sources.md` sections A4 to A6 and are not repeated here.

---

## 5. Sources checked and rejected as candidates

These are recorded so that the same ground is not covered twice. None supplies annual transport
equipment prices for 1938-1990.

- **National Income and Expenditure 1969** (CSO), Tables 51-54, gross domestic fixed capital
  formation by sector and by type of asset at current and 1963 prices, 1958-1968. A digitised copy
  was obtained (https://web.archive.org/web/2020id_/https://researchrepository.wvu.edu/cgi/viewcontent.cgi?article=1121&context=rri_ioacctdata,
  120 pages, access date 16 November 2026). It contains values, not indices: the asset rows are
  "Other road vehicles / Railway rolling stock / Ships / Aircraft". The OCR text layer is too
  corrupt to transcribe figures from (digits are systematically misread, for example "t963" for
  1963 and "7,648" for 1,648), so no numbers are recorded from it. Its use here is evidential: it
  shows that the CSO practice in 1969 was to publish current and constant price values only.
- **Blue Book time series file** (`bb.csdb`), fetched in two vintages on 16 November 2026: the
  superseded 2015 file at
  https://www.ons.gov.uk/file?uri=%2Feconomy%2Fgrossdomesticproductgdp%2Fdatasets%2Fbluebook%2Fcurrent%2Fprevious%2Fv1%2Fbb.csdb
  and the current 2026 file at
  https://www.ons.gov.uk/file?uri=%2Feconomy%2Fgrossdomesticproductgdp%2Fdatasets%2Fbluebook%2Fcurrent%2Fbb.csdb.
  In the 2026 file, asset-level GFCF in vehicles, ships and aircraft exists only as a chained
  volume measure from 1987, and the only GFCF deflator is whole-economy. The dataset page records a
  correction dated 14 November 2025 which removed "a number of legacy time series relating to
  historic Gross Fixed Capital Formation (GFCF) for the period 1987–1996" from the Blue Book 2025
  dataset; the two series recorded in section 7 nevertheless carry values from 1987 in the current
  file.
- **Sefton and Weale, balanced estimates, table A13 (`S046`) and table A14 (`S051`)**, current and
  constant price values for "Vehicles Ships & Aircraft", 1920-1990. Already recorded in
  `vehicle-index-sources.md` A9 and A10. These are values, not an index, and the constant-price
  block has two different price bases that overlap in 1948. No use is made of them here.
- **Board of Trade wholesale price index for engineering and allied trades / vehicles.** This is the
  natural bridge for 1938-1948 and it is referred to in the CSO's own 1955 statement that the 1948
  price indices "are derived mainly from the sources used for compiling the wholesale price indices
  prepared by the Board of Trade". No machine-readable annual run of that index by commodity group
  for 1938-1990 was found. It is not recorded here because no numbers were obtained.
- **ONS producer price index, transport equipment.** The published PPI series for transport
  equipment found in the course of the search begin in 1990 (1990 = 100 basis). They do not cover
  the gap.

---

Continued in [deflator-series](deflator-series.md).
