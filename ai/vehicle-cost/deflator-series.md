---
status: draft
verified: New ex-15 @ 8d0603d81
---
# Transport equipment deflator: the series

**Covers**: the Blue Book current and constant price series and the Feinstein plant and machinery
bridge, with their annual values. Parent: [vehicle-cost-evidence](../vehicle-cost-evidence.md).
The search that tested and rejected the alternatives is in
[deflator-search](deflator-search.md).

## 6. Assessment

One line per candidate series.

- **S1, Blue Book 1997 Table 13.2 (current prices, £m, 1948-1997): usable as the price-side half of
  the backbone but not as a deflator in itself**, because it is a value series and the brief
  requires a published index; its DFEJ column is unbroken for 1948-1997 and its five vehicle
  columns are unbroken for 1965-1997.
- **S2, Blue Book 1997 Table 13.4 (constant 1990 prices, £m, 1965-1997): usable as the volume-side
  half of the backbone for 1965-1997 only**, because it starts in 1965, does not separate railway
  rolling stock from ships and aircraft, and is chain-linked before 1986.
- **S1 with S2 (official values pair, 1965-1997): the best available official basis for the
  1966-1986 hole**, because it is the ONS's own deflation of the same asset heading, but the index
  obtained from it is arithmetic, not published, and the brief forbids presenting it as a published
  index.
- **S3, Feinstein Table 63 column 4 (1913 = 100, 1938-1948): usable for the war years only**, because
  it is the only published explicit index that runs unbroken through 1939-1947, but it is a plant
  and machinery index, not a vehicle index.
- **Feinstein Table 63 columns 5, 6 and 7: usable to 1965 for ships and road vehicles and to 1938
  for railway rolling stock**, because the vehicle columns are blank for 1939-1947 and stop in 1965.
- **NIE 1969 Tables 51-54, Blue Book 2026 `bb.csdb`, Sefton and Weale A13/A14: not usable**, because
  the first two are value series or aggregate deflators and the third is the derived series already
  rejected.
- **Overall: there is no single published transport-equipment deflator covering 1938-1990.** The
  longest published asset-level run of official numbers is Blue Book 1997 current prices
  1948-1997, paired with constant 1990 prices 1965-1997. Anyone needing a continuous 1938-1990
  series must either accept an arithmetic deflator from those official values or accept a splice of
  Feinstein (1938-1965) onto them (1965-1990); both are constructions, and neither is a published
  index.

---

## 7. Blue Book 2026: the modern vehicle series

Two series are required: the chained volume measure and the matching current-price series for the
same asset heading. **Both exist in the same file**, but they are not titled alike, and that is the
single most important thing to know about this pair.

File examined: `bb.csdb` for the Blue Book 2026 dataset, header line `020261030BB`, 3,104,754
bytes, downloaded from
https://www.ons.gov.uk/file?uri=/economy/grossdomesticproductgdp/datasets/bluebook/current/bb.csdb
on 16 November 2026. Series release date 30 October 2026. Every value below was cross-checked
against the ONS series feed for the same CDID
(`https://www.ons.gov.uk/generator?format=csv&uri=/economy/grossdomesticproductgdp/timeseries/<cdid>/bb`),
which returned the same numbers.

### 7.1 DLWJ — the chain volume measure

- **Exact series title as the file gives it**: `Gross Fixed Capital Formation: Vehicles, Ships &
  Aircraft: CVM NSA: £m`.
- **CDID**: DLWJ. The file's fixed-format identifier field reads `DLWJAU`; the ONS series feed
  gives the series ID as `DLWJ`. Blue Book table reference in the file record: `BB268.5`.
- **Units**: £ million. The ONS series feed gives `PreUnit` = £ and `Unit` = m.
- **Type**: chained volume measure, not seasonally adjusted. Not a price index. Not a value at
  current prices.
- **Coverage**: 1987 to 2025 inclusive, 39 annual observations, no gaps. 2025 is present and is the
  last available year at the access date.

```
1987=11407, 1988=12363, 1989=12835, 1990=11367, 1991=10341, 1992=8583, 1993=10582
1994=12260, 1995=10452, 1996=10711, 1997=16621, 1998=18523, 1999=19014, 2000=17231
2001=20077, 2002=21267, 2003=19728, 2004=18655, 2005=18630, 2006=21939, 2007=22720
2008=21617, 2009=19449, 2010=22858, 2011=18319, 2012=18248, 2013=16444, 2014=22357
2015=28674, 2016=33708, 2017=33293, 2018=24105, 2019=25224, 2020=22532, 2021=18972
2022=26495, 2023=31094, 2024=32036, 2025=24899
```

### 7.2 DLWZ — the current-price counterpart

- **Exact series title as the file gives it**: `Gross Fixed Capital Formation :Total Economy:Total
  Transport Equipment: CP NSA`.
- **CDID**: DLWZ. The file's fixed-format identifier field reads `DLWZAU`. Blue Book table
  reference in the file record: `BB268.1`.
- **Units**: the series metadata states none — both `PreUnit` and `Unit` are empty in the ONS
  series feed. The values are on the same scale as the £ million CVM series above and as the other
  £ million GFCF series in the same table, and are recorded here as £ million on that basis, not on
  an explicit statement in the source.
- **Type**: value series at current prices, not seasonally adjusted. Not an index.
- **Coverage**: 1987 to 2025 inclusive, 39 annual observations, no gaps.

```
1987=7890, 1988=8551, 1989=9447, 1990=9041, 1991=9004, 1992=8008, 1993=9553
1994=11692, 1995=10764, 1996=11276, 1997=12637, 1998=13740, 1999=14415, 2000=12828
2001=14718, 2002=15713, 2003=14687, 2004=13800, 2005=13770, 2006=16230, 2007=16962
2008=16627, 2009=15285, 2010=18117, 2011=14725, 2012=14613, 2013=13297, 2014=18017
2015=23187, 2016=27070, 2017=26910, 2018=20416, 2019=21550, 2020=19755, 2021=16545
2022=22483, 2023=28610, 2024=32036, 2025=24143
```

### 7.3 Does the current-price counterpart exist in the same file?

Yes. DLWZ is the total-economy current-price series for transport equipment and it is carried in the
same file, in the same Blue Book chapter and the same table family as DLWJ.

The qualification is one of naming, not of substance. **No series in the file is titled "Vehicles,
Ships & Aircraft" with a CP basis.** DLWJ is titled "Vehicles, Ships & Aircraft" and is a CVM; DLWZ
is the CP series and is titled "Total Transport Equipment". Both are the ESA asset heading
"transport equipment", of which "vehicles, ships and aircraft" is the older name used by the CSO and
early ONS. A user matching on the title string alone will fail to find the pair.

Nearest alternative current-price series, all of which are disaggregations of DLWZ rather than
alternatives to it, and all of which start in 1997 rather than 1987:

- `EQBVAU` — `ESA:GFCF:Private Sector:Transport Equipment CPNSA`
- `EQCIAU` — `ESA:GFCF:Total Economy:General Government:Transport Equipment CPNSA`
- `L5Z4AU` — `GFCF:Private non-fin corps: TOTAL: Transport equipment: £m: CP: NSA`
- `L5Z5AU` — `GFCF:Financial corporations: TOTAL: Transport equipment: £m: CP: NSA`
- `L5Z6AU` — `GFCF:Central government: TOTAL: Transport equipment: £m: CP: NSA`
- `L5Z7AU` — `GFCF:Local government: TOTAL: Transport equipment: £m: CP: NSA`
- `CRGSAU` — `GFCF: Households:TOTAL:Transport equipment:£m:CP:NSA`
- `CRGTAU` — `GFCF:NPISH:TOTAL:Transport equipment:£m:CP:NSA`

The matching CVM disaggregations, `EQCVAU20` (private sector) and `EQDJAU20` (general government),
also start in 1997. So the only pair in the file that reaches back to 1987 at total-economy level is
DLWJ with DLWZ.

### 7.4 Is the CVM series chain-linked, and does the file give a rebasing caveat?

**Chain-linked**: yes. The title designates it `CVM`, chained volume measure. Three pieces of
evidence in the file itself, beyond the title:

1. The fixed-format record for DLWJ carries the value 2024 in its first numeric field, where the
   record for DLWZ carries 0. A current-price series needs no such year; a chain-linked volume
   series does.
2. DLWJ and DLWZ are exactly equal in 2024: both are 32036. That is the signature of a chain-linked
   volume measure expressed in the prices of its reference year. **This equality is an observation
   about two published values, not a computed ratio**, and it identifies 2024 as the reference year.
3. The file uses the same convention in the title of another series, `Real households? (S.14)
   expenditure implied deflator: Index (Reference year 2024)`.

**Rebasing caveat**: the `.csdb` file carries no caveat text of any kind. It is a fixed-format data
file whose only provenance marker is the vintage header `020261030BB`. The rebasing statement is
therefore not in the file. What the dataset's own page records, and what bears on these two series,
is a correction dated 14 November 2025:

> "A number of legacy time series relating to historic Gross Fixed Capital Formation (GFCF) for the
> period 1987–1996 were unintentionally included in the Blue Book 2025 dataset. These series have
> now been removed to maintain consistency with previous practice on pre-1997 data content."

DLWJ and DLWZ nevertheless retain values for 1987-1996 in the current file, so that removal did not
reach these two series. The standard property of an annually chain-linked series applies and should
be stated wherever the pair is used: the series is not additive across components, the year-on-year
growth rates are the meaningful comparanda, and any level comparison across a long span carries the
effect of successive re-referencing.

### 7.5 Can the pair give an annual deflator for 1987-2025?

Yes, arithmetically — DLWJ divided by DLWZ gives an annual deflator for transport equipment for
1987-2025 with 2024 = 100, but it is a derived ratio and not a published index, the two series are
differently named ("Vehicles, Ships & Aircraft" against "Total Transport Equipment"), the volume
measure is chain-linked and re-referenced to 2024 so the earlier years carry chain-linking effects,
and the 2025 observation is a first estimate subject to revision.

Begins in [deflator-search](deflator-search.md).
