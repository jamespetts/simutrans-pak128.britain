---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Transport crew wages, 1750-2050

**Covers**: published British wage rates for transport crew, 1750 to 2050, by grade and employer,
with the period, hours basis and inclusions of each figure. This is the analysis and reconstruction
record for `config/staff.tab`; the measured tables are in
[staff-wages/evidence-1700-1913](staff-wages/evidence-1700-1913.md),
[staff-wages/evidence-1914-1946](staff-wages/evidence-1914-1946.md) and
[staff-wages/post-1980](staff-wages/post-1980.md).

Read with [balance-synthesis](balance-synthesis.md), which finds that railway crew is now charged
across the vehicle fleet and records the effect on the operating account, and with
[vehicle-cost-model](vehicle-cost-model.md), which records how the engine charges crew. The crew
complements declared in the `.dat` files — who travels on which vehicle, and why — are in
[staff-wages/crew-complements](staff-wages/crew-complements.md).

Evidence file for the `staff` domain of the pakset cost calibration. Target: a wage rate per person
per year, per hour, or per week, by staff type and era, for `New/config/staff.tab`.

## Reconstruction, 2026-11-23

The file was rebuilt as twelve grade series in annual old pence: seven land grades, three sea grades
and two air grades. They are converted to the engine's monthly Simucents at ×10/3 (1 old penny = 80
Simucents; /12 months; /2 for the engine's monthly factor). The previous file held annual pence
unconverted, so the engine charged 3/10 of the intended wage, and it used one all-grades railway
average for `staff[0]` rather than the driver rate.

The method, anchor table and measured/derived/estimated status are in
[staff-wages/reconstruction](staff-wages/reconstruction.md). The 1839-1946 evidence added in
this pass, including the 1914-1925 Hansard tables, the 1885-1946 signalman record and the
1946 grades, is in [staff-wages/evidence-1914-1946](staff-wages/evidence-1914-1946.md). The
1980-2050 evidence — the New Earnings Survey 1980 anchor and the measured 1982-1995 years, the
ASHE annual series 1999-2026, and the projection method — is in
[staff-wages/post-1980](staff-wages/post-1980.md).

Compiled 17 November 2026; extended 23 November 2026. Every value in the child tables was read
from the cited source. Rules applied: only what the source states is recorded; no deflation, no
derived hourly rate, no annualisation, no interpolation; where a value is computed it is labelled
`computed`. Crew wages only: no vehicle, fuel or maintenance cost is included here.

Staff type names are the source's own grade names. Where a source grade does not match a
`staff.tab` type exactly, the nearest type is named in square brackets in the "Staff type" column.

## Sources and tables

The measured tables for 1750-2026 — the Bank of England general wage comparators, the 1901-1910
all-grades series, the 1907 railway grades, the 1906 tramways, the 1912 seamen, the 1938 and 1948
transport averages, the 1956-1968 British Rail and London Transport averages, the 1963-1968
fitters and lorry drivers, and the 2019/2026 ASHE figures — are in
[staff-wages/evidence-1700-1913](staff-wages/evidence-1700-1913.md), with the full source records
S1-S8. The 1839-1946 rows added in the 2026-11-23 pass are in
[staff-wages/evidence-1914-1946](staff-wages/evidence-1914-1946.md). The New Earnings Survey
1970-1996 file, the NES tables for 1980-1995, the ASHE occupational timeseries and the 2017-2026 ASHE
releases are S18-S21 in [staff-wages/post-1980](staff-wages/post-1980.md).

## Assessment

Source IDs S1-S8 refer to the register in the evidence-1700-1913 child document; S9-S17 to
the register in the evidence-1914-1946 child document; S18-S21 to the register in the
post-1980 child document.

### Best long-run series found

**Railway crew, 1901-1910.** The Board of Trade series of average weekly earnings per head, United
Kingdom, 27 companies (S2 p. 82), is the only continuous annual series of railway pay found that
runs for a decade with a stated basis. It is an all-grades average, not a grade rate, and it stops
in 1910.

**Railway crew, 1956-1967.** Table 50 of S6 gives average weekly earnings of British Rail manual
men, April each year, with the wage-staff and workshop-staff grades separated, and the same table
gives London Transport road staff. This is the best post-war series for crew as a body, but it is
again an all-grades average.

**Individual grades.** The 1907 railway enquiry (S3, via S2) gives a rate and an actual-earnings
figure for engine driver, fireman, cleaner, passenger guard, goods guard, shunter, signalman and
goods porter in one year. The 1914-1925 Hansard table (S9, S10) gives engine drivers, ticket
collectors and goods porters over five dates, and the 1946 film (S12) gives signalmen,
platelayers, porters, cleaners and clerks. The 1962 Hansard table (S15) gives railway engine
drivers and passenger porters at 1914, 1920, 1930, 1940, 1950 and 1961, and road passenger
transport drivers and conductors at the same dates. None of these is a continuous annual
series.

**Modern.** ASHE (S7, S8, S20, S21) gives annual gross pay for named occupations at every year
from 1999, and the whole run 1999-2026 has now been transcribed into
[staff-wages/post-1980](staff-wages/post-1980.md) for eight occupations. The occupation codes
change between the classifications, so the series is built within each one (SOC90 for 1999-2001,
SOC2000 for 2002-2011, SOC2010 for 2012-2020, SOC2020 from 2021) and spliced at the breaks.

**1980.** The New Earnings Survey for April 1980 (S18, S19) gives mean gross weekly earnings for
locomotive drivers and motormen, bus and coach drivers, bus conductors and general labourers in
one table, on one basis. It replaces the unverified 1980 anchor that the file previously carried.

No single series spanning 1750-2050 for any transport crew grade was found. The longest general
series available is Clark's daily wage rates (S1): 1209-1914 for building craftsmen, 1221-1914 for
building labourers and 1209-1869 for farm labourers.

**The reconstructed path.** The longest measured wage path used in `staff.tab` is the
Williamson general labourer, 1710-1911 (S11). The 1907 railway grades give the grade ratios,
the 1914-1925 Hansard ranges give the war and post-war path, the signalman record runs
1885-1946, the 1946 film gives the general grades, the 1956-1962 British Rail and London
Transport averages and the 1980 NES and 1999-2026 ASHE figures give the post-war anchors. No
one grade has a continuous measured series over the whole span; the reconstruction is a splice,
and its estimated points are listed in [staff-wages/reconstruction](staff-wages/reconstruction.md).

### Coverage by decade

| Period | Coverage found |
|---|---|
| 1750-1799 | General labourer 1710-1797 (Williamson); 18th-century seamen (RN 22s 6d a month, merchant 25-30s a lunar month). No railway or road crew. |
| 1800-1849 | General labourer 1805-1835 (Williamson); 1839 driver-plus-fireman total for the S&D *Wilberforce*. No per-man grade rate. |
| 1850-1899 | General labourer annually to 1891 (Williamson); signalman 1885-1899 (one man's record and L&TSR 1897); tram driver and conductor late 1890s (Gladwin); dining-car staff 1896; Tilbury shed crew 1897. |
| 1900-1913 | Railway all-grades 1901-1910; railway grades 1907; tram driver and conductor 1906; signalman 1909 and 1912; seamen 1912; general labourer 1901 and 1911. |
| 1914-1938 | Railway driver 1914, 1920, 1930; passenger porter 1914-1930; road driver and conductor 1914-1930 (Hansard 1962 table); railway driver, ticket collector and goods porter 1914-1925 (Hansard 1922/1925); signalman 1920-1922 (one man's record); transport industry hourly average 1938. |
| 1939-1955 | Railway driver 1940 and 1950; passenger porter 1940 and 1950; road driver and conductor 1940 and 1950 (Hansard 1962 table); 1946 signalman, control centre, marshalling yard, platelayer, cleaner, parcels porter and booking clerk; transport industry hourly average 1948. |
| 1956-1968 | Railway driver 1961; road driver and conductor 1961; local authority labourer 1950 and 1961 (Hansard 1962 table); British Rail manual averages 1956-1968 (Table 50; 1963 missing), used for the 1962-1968 differential points; agricultural labourers 1956 and 1968; skilled engineering timeworkers 1963 and 1968; lorry drivers 1963 and 1968. |
| 1969-1996 | 1970-1975 relative pay by grade group (Hansard 1976); NES mean earnings 1970-1979 and 1980 (Hansard 1980); NES April grade means for locomotive drivers, bus drivers, bus conductors, general labourers and construction labourers at 1980, 1982, 1985, 1988, 1990, 1992 and 1995 (S18); no rail driver row published in 1990 or 1992. |
| 1997-2026 | ASHE 1999-2026 annual medians for twelve occupations, including ship and hovercraft officers, marine and waterways transport operatives, aircraft pilots and cabin crew; five rail values interpolated over ONS suppressions; 2030-2050 hold 2026 real pay and rise with the general index (projection). |

### Main gaps

1. **Railway crew before 1839.** The earliest total is the 1839 S&D *Wilberforce* driver and
   fireman figure, and it is a combined total, not a per-man rate. No engine-driver, fireman or
   guard rate for 1840-1900 was found. This remains the largest gap relative to the value of the
   period; the reconstruction carries the 1907 ratios back to 1710 as an assumption.
2. **Railway fireman, guard and attendant 1926-1968; driver 1962-1968.** The 1962 Hansard table
   gives the driver and passenger porter at 1930, 1940, 1950 and 1961, and the road driver and
   conductor at the same dates. The 1962-1968 points apply each grade's 1961 ratio to the
   British Rail all-grades average (Table 50); they are differential-derived, not measured
   grade rates. It does not give fireman, guard or carriage-attendant rates, so those remain
   1907-ratio derivations.
3. **1969-1998.** The 1976 Hansard table gives relative pay for 1970-1975 and the 1980 Hansard
   gives NES mean earnings for 1970-1979. The NES April grade means are transcribed for 1980,
   1982, 1985, 1988, 1990, 1992 and 1995 (S18); the years between them are interpolated by the
   engine, and 1981, 1983-84, 1986-87, 1989, 1991, 1993-94 and 1996 have not been transcribed.
   1990 and 1992 publish no rail engine driver row, so the driver is interpolated 1988-1995.
4. **Road crew.** No horse omnibus driver or conductor before 1890. The NES gives the bus driver
   at 1980, 1982, 1985, 1988, 1990, 1992 and 1995, and the bus conductor in 1980 and 1982 only.
   No conductor grade survives in ASHE, so the conductor is held at 0.891 of the bus driver, the
   measured 1980 ratio. The 1956 and 1962 London Transport averages are London-weighted and are
   no longer used for the national series.
5. **Sea, 1938-1966 and 1981-1989.** The sea grades were added on 2026-11-23: the rating has
   18th-century rates, 1912, the 1928-1960 National Maritime Board series, McConville's 1967-1980
   gross earnings, NES 1990/1992 and ASHE from 1999; the officer has the 1937 masters' minimum and
   McConville's 1973-1980 earnings, with 1967 and 1970 derived and 1.90 × the rating before that;
   catering has one measured shipboard rate (1928). No AB rate was found for 1961-1966 or
   1981-1989, and no officer earnings for 1990-1992; these are accepted and left to interpolation.
   `[USER-DIRECTION:2026-11-23]`
6. **Air, 1909-1923, 1925-1953, 1955-1968 and 1970-1998.** The air grades were added on 2026-11-23
   with measured anchors at 1924, 1954 and 1969 and ASHE from 1999. The gaps are filled by
   interpolation; the 1969-1999 gap carries a derived 1980 point.
7. **Hours.** Most weekly and daily figures are published without hours of duty. No hourly rate can
   be derived from them without an assumption, and none has been made here.
8. **Overtime and allowances.** Only the 1907 railway table separates a rate for ordinary time from
   actual earnings. The 1906 tram, 1912 sea and 1956-1968 figures are earnings and their overtime
   content is not stated. The 1912 sea rates are wages only, with food in addition.
9. **Currency.** The 1907 carriage-cleaner figure exists only in the United States Bulletin's
   dollar conversion (S5); no sterling figure for that grade was found.
