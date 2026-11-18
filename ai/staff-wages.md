---
status: draft
verified: New ex-15 @ 8d0603d81
---
# Transport crew wages, 1750-2026

**Covers**: published British wage rates for transport crew, 1750 to 2026, by grade and employer,
with the period, hours basis and inclusions of each figure. This is the evidence base for
`config/staff.tab`, which prices crew separately from vehicles.

Read with [balance-synthesis](balance-synthesis.md), which finds that railway crew is charged
nowhere in the present pakset because only two of 871 train `.dat` files declare any staff, and
with [vehicle-cost-model](vehicle-cost-model.md), which records how the engine charges crew.

Data appendix: it runs slightly over the usual document length because the source register is
shared across all eleven sections and cannot be split without orphaning it.

Evidence file for the `staff` domain of the pakset cost calibration. Target: a wage rate per person
per year, per hour, or per week, by staff type and era, for `New/config/staff.tab`.

Compiled 17 November 2026. Every value below was read from the cited source on that date.
Rules applied: only what the source states is recorded; no conversion, no deflation, no derived
hourly rate, no annualisation, no interpolation; where a value is computed it is labelled
`computed`. Crew wages only: no vehicle, fuel or maintenance cost is included here.

Staff type names are the source's own grade names. Where a source grade does not match a
`staff.tab` type exactly, the nearest type is named in square brackets in the "Staff type" column.

## Sources

- **S1** — Bank of England, *A millennium of macroeconomic data* (version 3.1), sheet `A47. Wages
  and prices`, columns "Farm wages in England, Clark (2009)", "Building craftsmen's wages in
  England, Clark (2009)" and "Building labourers' wages in England, Clark (2009)", pence per day.
  Workbook: https://www.bankofengland.co.uk/-/media/boe/files/statistics/research-datasets/a-millennium-of-macroeconomic-data-for-the-uk.xlsx .
  Secondary: the Bank reproduces Gregory Clark's estimates; the underlying figures are themselves
  constructed wage series, not payroll records. Accessed 17 November 2026.
- **S2** — Board of Trade (Labour Department), *Fifteenth Abstract of Labour Statistics of the
  United Kingdom* (London: HMSO, 1913), pp. 65, 82, 127-130. Digitised by the University of
  Southampton Library: https://archive.org/details/op1256113-1001 . Primary: official statistical
  compilation. The volume's tables run to 1912.
- **S3** — Board of Trade, *Report of an Enquiry by the Board of Trade into the Earnings and Hours
  of Labour of Workpeople of the United Kingdom. VII. Railway Service in 1907* (Cd. 6053 of 1912),
  as reproduced in S2 pp. 128-130. Primary.
- **S4** — Board of Trade, *Report of an Enquiry ... IV. Public Utility Services in 1906*
  (Cd. 5196 of 1910), as reproduced in S2 p. 127. Primary.
- **S5** — United States, Bureau of Railway Economics, *A Comparative Study of Railway Wages and
  the Cost of Living in the United States, the United Kingdom and the Principal Countries of
  Continental Europe*, Bulletin No. 34 (Washington, D.C., 1912), pp. 10-17.
  https://archive.org/details/comparativestudy00burerich . Secondary: a United States compilation
  that reproduces the Board of Trade's 1907 returns after converting sterling to dollars.
- **S6** — Department of Employment and Productivity, *British Labour Statistics: Historical
  Abstract 1886-1968* (London: HMSO, 1971), Table 42 pp. 102-103, Table 46 pp. 110-111, Table 48
  pp. 114-115, Table 50 pp. 118-119, Table 61 p. 136.
  https://escoe-website.s3.amazonaws.com/wp-content/uploads/2019/06/19120215/British-Labour-Statistics-Historical-Abstract-1886-1968.pdf .
  Primary: official statistical compilation.
- **S7** — Office for National Statistics, *Annual Survey of Hours and Earnings, Table 14.7a Annual
  pay - Gross, 2019 revised* (SOC2010 four-digit occupation).
  https://www.ons.gov.uk/file?uri=/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/occupation4digitsoc2010ashetable14/2019revised/table142019revised.zip .
  Primary. Accessed 17 November 2026.
- **S8** — Office for National Statistics, *Annual Survey of Hours and Earnings, Table 14.7a Annual
  pay - Gross, 2026 provisional* (SOC2020 four-digit occupation).
  https://www.ons.gov.uk/file?uri=/employmentandlabourmarket/peopleinwork/earningsandworkinghours/datasets/occupation4digitsoc2010ashetable14/2026provisional/ashetable142026provisional.zip .
  Primary, provisional. Accessed 17 November 2026.

Notes on the ONS tables (S7, S8): ASHE covers employee jobs in the United Kingdom, excludes the
self-employed and employees not paid in the reference period, and annual estimates relate to
employees on adult rates of pay who have been in the same job for more than a year, for the tax
year ending 5 April. The release publishes a "Gross" table and a separate "Excluding overtime"
table, so "Gross" includes overtime; the table itself does not itemise bonuses and allowances.

---

## 1. General wage comparators, 1750-1914

Average daily wage rates, pence per day, England. These are rates, not earnings; days worked per
week are not stated in the source. Use for expressing transport wages relative to a general wage.

| Year | Staff type | Industry | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1750 | Farm labourer [agricultural labourer] | English agriculture | 10.74d | per day | money wage rate; no allowances stated | S1 | Secondary |
| 1750 | Building craftsman [skilled] | English building | 20.00d | per day | money wage rate | S1 | Secondary |
| 1750 | Building labourer | English building | 12.89d | per day | money wage rate | S1 | Secondary |
| 1800 | Farm labourer | English agriculture | 17.83d | per day | money wage rate | S1 | Secondary |
| 1850 | Farm labourer | English agriculture | 18.61d | per day | money wage rate | S1 | Secondary |
| 1850 | Building labourer | English building | 29.13d | per day | money wage rate | S1 | Secondary |
| 1850 | Building craftsman | English building | 44.13d | per day | money wage rate | S1 | Secondary |
| 1900 | Building labourer | English building | 57.18d | per day | money wage rate | S1 | Secondary |
| 1900 | Building craftsman | English building | 78.85d | per day | money wage rate | S1 | Secondary |
| 1914 | Building craftsman | English building | 90.30d | per day | money wage rate | S1 | Secondary |

Source values are carried at the workbook's full precision; only the first two decimal places are
shown. The farm-wage column of S1 has no value after 1869.

## 2. Railway servants, all grades, 1901-1910

Average earnings per head per week, United Kingdom, 27 companies. The source states that the
figures relate, with few exceptions, to the first week in December of each year and are affected by
the proportions of men on high and low rates and by overtime or short time; they are average
earnings, not rates for an individual grade.

| Year | Staff type | Employer | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1901 | All railway servants | 27 UK railway companies | 25s 0¼d | per week | actual cash earnings; overtime and short time included; no uniform or housing allowance | S2 p. 82 | Primary |
| 1906 | All railway servants | 27 UK railway companies | 25s 5¼d | per week | as above | S2 p. 82 | Primary |
| 1910 | All railway servants | 27 UK railway companies | 25s 9d | per week | as above | S2 p. 82 | Primary |

The full published run is 1901: 25s 0¼d; 1902: 24s 11¼d; 1903: 24s 10¼d; 1904: 25s 0¼d;
1905: 25s 3¼d; 1906: 25s 5¼d; 1907: 25s 10d; 1908: 25s 0d; 1909: 25s 4¼d; 1910: 25s 9d.

## 3. Railway crew by grade, 1907

Board of Trade enquiry into the railway service, last pay-week of October 1907, time workers
regularly employed. Two measures are published for each grade: the "average rate of wages for full
ordinary time" and "average actual earnings". United Kingdom column. Hours of duty are not stated
in the table. Values marked * in the source include bonus paid in addition to the nominal rate; the
plain rate is recorded below and the bonus variant is noted.

| Year | Staff type | Employer | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1907 | Engine driver | UK railways (steam) | rate 40s 0d; earnings 45s 11d | per week | rate for full ordinary time; earnings include overtime; uniform allowance excluded (bonus variant 40s 3d) | S2 p. 128-129 (S3) | Primary |
| 1907 | Fireman | UK railways (steam) | rate 23s 9d; earnings 27s 5d | per week | as above (bonus variant 23s 10d) | S2 p. 128-129 (S3) | Primary |
| 1907 | Engine cleaner [locomotive cleaner] | UK railways (steam) | rate 17s 8d; earnings 20s 2d | per week | as above | S2 p. 128-129 (S3) | Primary |
| 1907 | Passenger guard | UK railways | rate 27s 8d; earnings 29s 3d | per week | as above (bonus variant 27s 9d) | S2 p. 128-129 (S3) | Primary |
| 1907 | Goods guard and brakesman | UK railways | rate 28s 2d; earnings 31s 2d | per week | as above | S2 p. 128-129 (S3) | Primary |
| 1907 | Shunter | UK railways | rate 23s 9d; earnings 25s 7d | per week | as above | S2 p. 128-129 (S3) | Primary |
| 1907 | Signalman | UK railways | rate 24s 8d; earnings 27s 6d | per week | as above (bonus variant 25s 4d) | S2 p. 128-129 (S3) | Primary |
| 1907 | Goods porter | UK railways | rate 20s 0d; earnings 21s 10d | per week | as above (bonus variant 20s 9d) | S2 p. 128-129 (S3) | Primary |
| 1907 | All adult men, all grades | UK railways | rate 24s 4d; earnings 26s 8d | per week | as above (bonus variant 24s 6d) | S2 p. 128-129 (S3) | Primary |
| 1907 | Carriage cleaner | UK railways | $4.66 | per week | standard weekly rate of pay; S5 states the figure was converted from the Board of Trade's sterling return; allowances for uniform and housing excluded | S5 p. 17 | Secondary |

The S5 conversion is at the Bulletin's own rate; the sterling figure for carriage cleaners is not
in the S2 table. S5 (pp. 12-13), describing the same 1907 enquiry, states that the earnings "do not
take account of allowances made to employees in the shape of uniforms or other clothing, houses
rent-free or at a reduced rental", and that overtime pay is included. Other grades in S2, not
recorded above: foreman 33s 11d rate / 35s 9d earnings;
ganger (permanent way) 23s 7d / 25s 11d; coaching porter (six-day) 18s 8d / 19s 9d; goods checker
24s 0d / 26s 9d; mechanic 29s 7d / 31s 8d; platelayer and packer 19s 5d / 21s 2d; carman and drayman
(one horse) 22s 10d / 24s 9d; locomotive, carriage and wagon labourer 20s 0d / 21s 9d.

## 4. Electric railway crew, 1907

Same enquiry; traffic and engineering departments and electricity generating stations of electric
railways. United Kingdom column.

| Year | Staff type | Employer | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1907 | Motorman [tram/rail driver] | UK electric railways | rate 38s 11d; earnings 38s 10d | per week | rate for full ordinary time; earnings include overtime (bonus variant 41s 1d / 41s 9d) | S2 p. 130 (S3) | Primary |
| 1907 | Conductor and gateman | UK electric railways | rate 24s 5d; earnings 24s 7d | per week | as above (bonus variant 24s 5d) | S2 p. 130 (S3) | Primary |
| 1907 | Ticket collector and examiner | UK electric railways | rate 22s 10d; earnings 22s 11d | per week | as above | S2 p. 130 (S3) | Primary |

## 5. Tramways, 1906

Average net earnings in the last pay-week of September 1906, workpeople who worked full time,
United Kingdom column. The enquiry covered tramway and omnibus services, but the published table
separates only tram car drivers and conductors; no separate omnibus grade is shown.

| Year | Staff type | Employer | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1906 | Tram car driver (motorman) | UK tramway undertakings | 31s 7d | per week | net earnings, full-time week; less or more than full time excluded from this column | S2 p. 127 (S4) | Primary |
| 1906 | Tram conductor | UK tramway undertakings | 29s 0d | per week | as above | S2 p. 127 (S4) | Primary |

For workpeople including those who worked less or more than full time, the same table gives
30s 8d for motormen and 26s 11d for conductors.

## 6. Merchant seamen, 1912

Predominant monthly rates of wages at 1st March 1912, compiled from returns by Superintendents of
Mercantile Marine showing the number of engagements at each rate. Food is in addition to wages.

| Year | Staff type | Employer | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1912 | Able seaman | Steamships, London, North America East Coast voyage | 100s 0d | per month | wages only; food in addition | S2 p. 65 | Primary |
| 1912 | Fireman [stoker] | Steamships, London, North America East Coast voyage | 110s 0d | per month | wages only; food in addition | S2 p. 65 | Primary |
| 1912 | Trimmer [stoker] | Steamships, Liverpool, West Coast of Africa voyage | 80s 0d | per month | wages only; food in addition | S2 p. 65 | Primary |

Other rates in the same table: able seamen on sailing vessels, Liverpool to West Coast of America
70s per month; able seamen on steamships, Liverpool to North America 90s, 95s and 100s; firemen,
Liverpool to North America 100s, 105s, 110s and 120s; firemen, Southampton to North America
110s and 120s.

## 7. Transport industry comparators, 1938-1948

Average hourly earnings of manual men, transport industry group, United Kingdom, pence per hour.
Industry averages, not crew grades; recorded because they are the only 1938-1948 transport wage
figures recorded here.

| Year | Staff type | Industry | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1938 (Oct) | Manual men, all grades | Transport | 17.2d | per hour | earnings include overtime; part-time women excluded from the men's column | S6 Table 46 p. 110-111 | Primary |
| 1948 (Apr) | Manual men, all grades | Transport | 32.6d | per hour | as above | S6 Table 46 p. 110-111 | Primary |
| 1938 (Oct) | Manual men, all grades | All industries | 17.4d | per hour | as above | S6 Table 46 p. 110-111 | Primary |
| 1948 (Apr) | Manual men, all grades | All industries | 32.9d | per hour | as above | S6 Table 46 p. 110-111 | Primary |

## 8. British Rail and London Transport manual staff, 1956-1962

Average weekly earnings of full-time manual workers (ordinarily employed for more than 30 hours a
week), April each year, Great Britain. British Rail and London Transport were outside the
Department of Employment enquiry and are published in this separate table.

| Year | Staff type | Employer | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1956 | Manual men aged 20 and over, wages staff other than workshop | British Rail | £10 18s 10d | per week | earnings; full-time workers | S6 Table 50 p. 118 | Primary |
| 1958 | Manual men aged 20 and over, wages staff other than workshop | British Rail | £11 12s 0d | per week | as above | S6 Table 50 p. 118 | Primary |
| 1960 | Manual men aged 20 and over, wages staff other than workshop | British Rail | £13 14s 0d | per week | as above | S6 Table 50 p. 118 | Primary |
| 1962 | Manual men aged 20 and over, wages staff other than workshop | British Rail | £14 17s 0d | per week | as above | S6 Table 50 p. 118 | Primary |
| 1956 | Manual men, road staff | London Transport | £11 5s 10d | per week | earnings; full-time workers | S6 Table 50 p. 118 | Primary |
| 1958 | Manual men, road staff | London Transport | £12 4s 6d | per week | as above | S6 Table 50 p. 118 | Primary |
| 1960 | Manual men, road staff | London Transport | £14 9s 0d | per week | as above | S6 Table 50 p. 118 | Primary |
| 1962 | Manual men, road staff | London Transport | £15 16s 0d | per week | as above | S6 Table 50 p. 118 | Primary |

The same table continues to 1967 (British Rail) and 1968 (London Transport) on pp. 118-119. British
Rail workshop staff are published as a separate column (1956: £11 18s 11d; 1962: £14 18s 0d).
London Transport rail staff and common services are separate columns (1956: £12 3s 0d and
£12 6s 4d for men). The source states that British Rail was included in the Department of Employment
enquiry from April 1968 (actually October 1967).

## 9. Agricultural labourers, 1956 and 1968

Average weekly earnings of full-time manual workers, April, Great Britain. Source note: earnings
include some allowance in kind valued in accordance with the Agricultural Wages Order.

| Year | Staff type | Industry | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1956 | Man aged 20 and over | Agriculture (England and Wales) | £8 4s 8d | per week | earnings include allowance in kind valued under the Agricultural Wages Order | S6 Table 50 p. 118 | Primary |
| 1968 | Man aged 20 and over | Agriculture (England and Wales) | £15 10s 0d | per week | as above | S6 Table 50 p. 119 | Primary |

## 10. Engineering fitters and lorry drivers, 1963-1968

Average hourly earnings excluding overtime premium, manual men, Great Britain, pence per hour.
The "skilled" row covers timeworkers in engineering; the lorry-driver row is the "Lorries drivers"
occupation within "Construction other than constructional engineering".

| Year | Staff type | Industry | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 1963 (Jan) | Skilled timeworker [skilled engineering tradesman] | Engineering | 87.9d | per hour | earnings excluding overtime premium | S6 Table 61 p. 136 | Primary |
| 1968 (June) | Skilled timeworker [skilled engineering tradesman] | Engineering | 114.7d | per hour | as above | S6 Table 61 p. 136 | Primary |
| 1963 (Jan) | Lorry driver | Construction other than constructional engineering | 77.1d | per hour | as above | S6 Table 61 p. 136 | Primary |
| 1968 (June) | Lorry driver | Construction other than constructional engineering | 94.6d | per hour | as above | S6 Table 61 p. 136 | Primary |

## 11. ASHE, 2019 and 2026

Median and mean annual gross pay, all employees, United Kingdom. Median is ONS's preferred average.
"x" means the estimate is suppressed by ONS. SOC code and title are given as published in each year;
the two years use different occupation classifications (SOC2010 for 2019, SOC2020 for 2026), so
the codes are not interchangeable.

| Year | Staff type | Industry | Amount | Period | Inclusions | Src | Type |
|---|---|---|---|---|---|---|---|
| 2019 | Train and tram drivers (SOC 8231) | All industries | median £56,102; mean £56,816 | per year | annual gross pay (the release also publishes an excluding-overtime variant); self-employed excluded | S7 | Primary |
| 2026 | Train and tram drivers (SOC 8231) | All industries | median £73,873.6; mean £72,019.7 | per year | as above; provisional | S8 | Primary |
| 2019 | Bus and coach drivers (SOC 8213) | All industries | median £25,202; mean £25,419 | per year | as above | S7 | Primary |
| 2026 | Bus and coach drivers (SOC 8212) | All industries | median £33,929.5; mean £33,495.4 | per year | as above; provisional | S8 | Primary |
| 2019 | Large goods vehicle drivers (SOC 8211) | All industries | median £30,130; mean £29,804 | per year | as above | S7 | Primary |
| 2026 | Large goods vehicle drivers (SOC 8211) | All industries | median £40,936.1; mean £40,677.6 | per year | as above; provisional | S8 | Primary |
| 2019 | Aircraft pilots and flight engineers (SOC 3512) | All industries | median £75,934; mean £82,070 | per year | as above | S7 | Primary |
| 2026 | Aircraft pilots and air traffic controllers (SOC 3511) | All industries | median £96,622.6; mean £108,996.4 | per year | as above; provisional | S8 | Primary |
| 2019 | Air travel assistants [cabin crew] (SOC 6214) | All industries | median £19,009; mean £19,646 | per year | as above | S7 | Primary |
| 2026 | Air travel assistants [cabin crew] (SOC 6213) | All industries | median £21,826.6; mean £22,095.1 | per year | as above; provisional | S8 | Primary |
| 2019 | Rail travel assistants [guard, ticket collector] (SOC 6215) | All industries | median £36,238; mean £36,228 | per year | as above | S7 | Primary |
| 2026 | Rail travel assistants [guard, ticket collector] (SOC 6214) | All industries | median £48,179.7; mean £47,963.9 | per year | as above; provisional | S8 | Primary |
| 2019 | Rail transport operatives [signalman, shunter] (SOC 8234) | All industries | median £44,344; mean £44,176 | per year | as above | S7 | Primary |
| 2026 | Rail transport operatives [signalman, shunter] (SOC 8234) | All industries | median £58,369.9; mean £61,077 | per year | as above; provisional | S8 | Primary |
| 2019 | Ship and hovercraft officers (SOC 3513) | All industries | median suppressed; mean £46,444 | per year | as above | S7 | Primary |
| 2026 | Ship and hovercraft officers (SOC 3512) | All industries | median suppressed; mean £55,972.7 | per year | as above; provisional | S8 | Primary |
| 2019 | Metal working production and maintenance fitters (SOC 5223) | All industries | median £32,719; mean £34,178 | per year | as above | S7 | Primary |
| 2026 | Metal working production and maintenance fitters (SOC 5223) | All industries | median £41,147.9; mean £43,222.6 | per year | as above; provisional | S8 | Primary |
| 2019 | Farm workers (SOC 9111) | All industries | median £20,860; mean £19,904 | per year | as above | S7 | Primary |
| 2026 | Farm workers (SOC 9111) | All industries | median £27,008; mean £26,702.5 | per year | as above; provisional | S8 | Primary |

Two further ASHE points, not tabulated above because they are aggregate grades rather than crew:
2019 "Skilled agricultural and related trades" (SOC 51) median £20,074; 2026 "Agricultural and
fishing trades n.e.c." (SOC 5119) median £29,318.4.

---

## Assessment

### Best long-run series found

**Railway crew, 1901-1910.** The Board of Trade series of average weekly earnings per head, United
Kingdom, 27 companies (S2 p. 82), is the only continuous annual series of railway pay found that
runs for a decade with a stated basis. It is an all-grades average, not a grade rate, and it stops
in 1910.

**Railway crew, 1956-1967.** Table 50 of S6 gives average weekly earnings of British Rail manual
men, April each year, with the wage-staff and workshop-staff grades separated, and the same table
gives London Transport road staff. This is the best post-war series for crew as a body, but it is
again an all-grades average.

**Individual grades.** The only source found that gives the wages of named crew grades over any
period is the 1907 railway enquiry (S3, via S2): one year, but engine driver, fireman, cleaner,
passenger guard, goods guard, shunter, signalman and goods porter together, with both a rate and an
actual-earnings figure for each.

**Modern.** ASHE (S7, S8) gives annual gross pay for named occupations at every year from 1997,
but only 2019 and 2026 have been transcribed here. The occupation codes change between the two
years, so a series must be built within one classification (SOC2010 for 2011-2019, SOC2020 for
2021 onward).

No single series spanning 1750-2026 for any transport crew grade was found. The longest general
series available is Clark's daily wage rates (S1): 1209-1914 for building craftsmen, 1221-1914 for
building labourers and 1209-1869 for farm labourers.

### Coverage by decade

| Period | Coverage found |
|---|---|
| 1750-1799 | General wages only (farm labourer, building craftsman, building labourer). No transport crew. |
| 1800-1849 | General wages only. No transport crew. |
| 1850-1899 | General wages only. No transport crew. |
| 1900-1913 | Railway all-grades average 1901-1910; railway grades 1907; electric railway grades 1907; tram driver and conductor 1906; able seaman, fireman and trimmer 1912. |
| 1914-1938 | Transport industry hourly average, October 1938, only. |
| 1939-1955 | Transport industry hourly average, April 1948, only. |
| 1956-1968 | British Rail and London Transport manual men 1956-1962 (source continues to 1967-1968); agricultural labourers 1956 and 1968; skilled engineering timeworkers 1963 and 1968; lorry drivers 1963 and 1968. |
| 1969-1996 | Nothing found. |
| 1997-2026 | ASHE 2019 and 2026 for nine occupations. |

### Main gaps

1. **Railway crew before 1901.** No wage rate for an engine driver, fireman, guard or signalman
   before 1907 was found in an accessible, citable source. The 1907 report gives rates that had
   been in place for some years, but no earlier observation. This is the largest gap relative to
   the value of the period.
2. **Road crew before 1906.** No horse omnibus driver, conductor, ostler or groom wage was found.
   The 1906 public utility enquiry is the earliest road passenger crew figure located.
3. **Railway grades 1908-1955.** Nothing by grade. Only the 1938 and 1948 industry hourly averages
   bridge this period.
4. **1969-1996.** Nothing. ASHE begins in 1997; the Department of Employment Gazette series that
   would fill the gap was not transcribed.
5. **Sea, 1750-1911 and 1913-2018.** Except the 1912 monthly rates and the ASHE ship's-officer
   figures, nothing. No ship's master, mate or engineer rate was found before 2019.
6. **Air before 2019.** Nothing. No pilot or cabin crew pay scale was found in an accessible
   source.
7. **Hours.** Most weekly and daily figures are published without hours of duty. No hourly rate can
   be derived from them without an assumption, and none has been made here.
8. **Overtime and allowances.** Only the 1907 railway table separates a rate for ordinary time from
   actual earnings. The 1906 tram, 1912 sea and 1956-1968 figures are earnings and their overtime
   content is not stated. The 1912 sea rates are wages only, with food in addition.
9. **Currency.** The 1907 carriage-cleaner figure exists only in the United States Bulletin's
   dollar conversion (S5); no sterling figure for that grade was found.
