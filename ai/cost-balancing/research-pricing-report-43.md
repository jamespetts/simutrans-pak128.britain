---
status: draft
verified: New ex-15 @ 70a098c64 (working tree)
---
# Research pass 43 — Carriage and wagon maintenance, 1892-2026

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report and `research-pricing-rows-43.csv`. No workbook, `.dat` or
existing doc was changed.

## 1. What this pass found

1. **A measured 1961 pair on one definition.** The Beeching Report's functional split of
   1961 working expenses gives £55.0m for "multiple units, carriages and parcels vans" and
   £46.1m for wagons, both headed "provision, maintenance, stabling and servicing", against
   46,089 carrying vehicles and 848,591 wagons. That is **£1,193 a carrying vehicle-year**
   and **£54.3 a wagon-year** — **4.6 per cent**, or **5.4 per cent** without the MU cars.
   Against 1892's 12.6 per cent, the wagon:carriage ratio **falls by more than half** in 69
   years.
2. **The carriage level in real terms rises 5.3 times, 1892-1961, and eleven to twenty times
   by the 1980s.** Hill's 1892 £33.3 gross is £34.3 in 1900 money (£22.3 net of the 35 per
   cent renewals provision): the 1892 general index is 97, not the 78 of the `vehicle
   purchase` series, and `prices.tab` requires the general index for maintenance. The 1961
   figure is £183 in 1900 money; the 1984 train-mile evidence gives £374-686; the 2013 RDG
   rate gives £308-615.
3. **The user's ratio method works, but only with a ratio that is allowed to fall.** Scaling
   the 1892 wagon level by the carriage index (method a) overstates the 1961 wagon by about
   2.3 times. Scaling the wagon maintenance-to-capital proportion by the change in the
   carriage proportion (method b) cannot be tested, because no measured 1961 wagon price
   exists and the answer swings by a factor of five across the plausible range.
4. **Recommended ladder, 1900 money per vehicle-year:** carriage 33 / 140 / 265 / 460 / 440
   at 1900 / 1950 / 1970 / 1990 / 2020; wagon (10-tonne reference) 4.2 / 8.7 / 14.3 / 24.8 /
   23.8, scaled by (payload/10)^0.4. The modern 100-tonne hopper then carries £59.7, which is
   close to the present 8-per-cent-of-capital rule (£56.6); old and small wagons are 2-6 times
   too cheap today, while modern 100-tonne hoppers are already about right.

## 2. Method

- **Deflator.** Nominal figures are converted to 1900 money with the `general` series in
  `New/config/prices.tab` (1900 = 100): 1892 97; 1913 107; 1920 275; 1948 338; 1950 359;
  1961 552; 1966 660; 1970 795; 1982 3,483; 1984 3,824; 1990 5,408; 2009 9,163; 2013
  10,725; 2024 15,309; 2026 16,281. `prices.tab` states that vehicle maintenance stays on the
  general index, so this is the engine's own treatment, not a new choice.
  **Correction, 2026-11-25.** The first draft of this report used the `vehicle purchase`
  series (1892 78; 1920 226; 1961 462) for the 1892 and 1920 conversions. Those are the
  purchase index, not the general one, and a maintenance figure must not use them. The
  corrected 1892 values are 34.3 gross and 22.3 net, not 42.7 and 27.8; the 1920 interpolation
  on the corrected anchors is 68, not 61. The 1961 correction to 552 was already made in §6.
  The ladder itself (33 / 140 / 265 / 460 / 440) is unaffected apart from the 1900 anchor's
  basis, see §6.
- **Grades.** MEASURED = an account, contract or published total with a stated scope.
  STATED = a trade or academic statement of a rate without the underlying account.
  DERIVED = my arithmetic from a measured or stated figure, with the chain shown.
  ESTIMATE = my judgement, used only where no measurement exists, and marked in every table.
- **Renewals.** Hill's rail figures include renewals ("maintenance, that is the cost of
  repairs and renewals"). The KB's measured renewals shares are 35 per cent for carriages
  and 50 per cent for wagons (report 40 §2; Hill Appendix III). Both the gross and the net
  figure are shown wherever the distinction changes the answer.
- **Sourcing.** Every page relied on was read; the 1961 money column was read from the page image because the OCR layer had lost it.
- **Nothing here uses a `.dat` value as a target.** The pakset capital ladders appear only as
  a comparator, and are identified as such.

## 3. Evidence table

| # | Date | Item | Figure as stated | Scope (in / out) | Denominator | Grade | Source |
|---|---|---|---|---|---|---|---|
| 1 | 1887-92 | Hill, carriages, 19 companies | £33 6s. a vehicle-year (range £18 6s.-£52 14s.) | "maintenance, that is the cost of repairs and renewals"; renewals in | vehicle-year | MEASURED | Hill 1895, App. II Table II; https://doi.org/10.1680/imotp.1895.19704 |
| 2 | 1887-92 | Hill, wagons, 19 companies | £4 4s. a wagon-year (range £2 4s.-£6 10s.) | as row 1 | wagon-year | MEASURED | Hill 1895, App. II Table III |
| 3 | 1892 | Wagon:carriage ratio | 12.6 per cent (£4.20/£33.30) | same definition and same five years | per vehicle-year | DERIVED | rows 1-2; the brief's 13.2 per cent uses £4 8s. |
| 4 | 1961 | Beeching, carrying units | £55.0m | "provision, maintenance, stabling and servicing"; includes the capital charge (see §4) | 46,089 MU cars, coaches and parcels vans | MEASURED | *The Reshaping of British Railways* (1963), p. 6; https://railnews-business.co.uk/docs%20library/1963%20BRB_Beech001a.pdf |
| 5 | 1961 | Beeching, wagons | £46.1m | as row 4 | 848,591 wagons | MEASURED | as row 4 |
| 6 | 1961 | Beeching, locomotives | £55.9m | as row 4 | 12,657 locomotives | MEASURED | as row 4 |
| 7 | 1961 | Beeching, maintenance account line | £122.2m | "maintenance of rolling stock" in the consolidated revenue account; excludes train and vehicle operating expenses £187.5m | whole fleet, 953,872 units | MEASURED | as row 4 |
| 8 | 1961 | Carrying unit, per vehicle | £1,193.3 | row 4 ÷ row 4 denominator | vehicle-year | DERIVED | rows 4-5 |
| 9 | 1961 | Wagon, per wagon | £54.3 | row 5 ÷ row 5 denominator | wagon-year | DERIVED | rows 4-5 |
| 10 | 1961 | Wagon:carrying-unit ratio | 4.6 per cent; 5.4 per cent against a coach-only estimate of £1,012 | same definition | per vehicle-year | DERIVED | rows 8-9 and §4 |
| 11 | 1961 | Stock counts | DMU 4,074; EMU 6,958; passenger coaches 22,575; non-passenger coaches 12,482; wagons 848,591; containers 46,535 | at 31 December 1962, one year after the money | vehicles | MEASURED | as row 4, Appendix 3 |
| 12 | 1977-81 | Serpell, BREL repair unit costs | coach repair cost per repair +15 per cent real; locomotives +40; MUs +35-40; HSTs +25 | BREL repairs only; one-fifth attributed to longer intervals | per repair | MEASURED | *Railway Finances* (1983), para 6.51; https://railnews-business.co.uk/docs%20library/1982%20The-Serpell-Report-on-Railway-Finances-1982.pdf |
| 13 | 1981 | Serpell, BREL vehicle maintenance | £266m (1982 prices), 55 per cent of all maintenance expenditure | heavy and light maintenance and repairs by BREL | BREL works | MEASURED | Serpell, para 6.49 |
| 14 | 1982 | Serpell, total vehicle maintenance | £473m (1982 prices) | day-to-day, light, intermediate and general repairs; all vehicle types | whole fleet | MEASURED | Serpell, para 6.44 |
| 15 | 1984 | HST set, maintenance | £2.28 a train-mile (0.51p a seat-mile; the source prints "51p") | maintenance only, set against a separate capital charge of £1.32 a train-mile; 450 seats | train-mile, 8-car set | STATED | Barnett 1992, citing Potter 1988: 111; https://escholarship.org/uc/item/7rp0g3k3 |
| 16 | 1984 | Class 87 loco-hauled train | £1.55 a train-mile | computed from row 15 and the stated "47 per cent higher" for the HST | train-mile, 10 coaches + loco + DVT | DERIVED | as row 15 |
| 17 | Feb 2013 | RDG, new EMU | £0.44 a vehicle-mile | "total maintenance costs"; capital lease, energy and track are separate | vehicle-mile | MEASURED | RDG, *LTPRSS* 3rd ed., Table 5 (quoted in `New/ai/vehicle-cost/modern-traction-multiple-units.md`); https://www.raildeliverygroup.com/publications/archive/367-2015-03-long-term-passenger-rolling-stock-strategy-3rd-ed/file.html |
| 18 | Feb 2013 | RDG, new DMU | £0.80 a vehicle-mile | as row 17 | vehicle-mile | MEASURED | as row 17 |
| 19 | 2005 | Benchmark ratio | "traction maintenance is approximately twice as expensive as that for coaches" | "daily cleaning and servicing to regular light and intermittent heavy maintenance" | vehicle-km | STATED | Bente and Roeleveld, *Railway Gazette International*, 1 Apr 2006 (quoted in the same KB doc); https://www.railwaygazette.com/news/2006/04/01/benchmarking-identifies-good-practice-in-rolling-stock-maintenance/ |
| 20 | 2024-25 | ORR, passenger fleets | median £0.72 a vehicle-mile (TSA first term), £1.42 (TSSSA), £1.73 (in-house), £1.88 (TSA after first term) | total maintenance cost incurred by the TOC, contracted and in-house; 17 TOCs, 87 fleets; freight excluded | vehicle-mile | MEASURED | ORR, *Rolling Stock Maintenance Market Review*, interim, 29 Oct 2026, Figure 4.2; https://www.orr.gov.uk/sites/default/files/2026-10/2026-interim-report-rolling-stock-maintenance-market-review.pdf |
| 21 | 2024-25 | ORR, per vehicle | median £93,000 (TSA first term), £136,000 (TSSSA), £199,000 (in-house), £285,000 (TSA after first term) | as row 20 | vehicle-year | MEASURED | ORR 2026, Figure 4.3 |
| 22 | 2012 | Chiltern Mk3 rebuild | £325,000 a coach (£6.5m/20) | plug doors, corrosion repair, full rebuild | per coach, one event | MEASURED | Rail Magazine, 13 Jun 2012; report 36 §6 |
| 23 | 2015 | Greater Anglia Mk3 refresh | £100,840 a coach (£12m/119) | interior refresh | per coach, one event | MEASURED | Rail Magazine, 2 Feb 2015; report 36 §6 |
| 24 | 2025 | EMR Class 158 refresh | £100,000 a vehicle (£5.2m/26 two-car units) | interior refresh | per vehicle, one event | MEASURED | Modern Railways, 24 Jul 2025; report 36 §6 |
| 25 | 1996 | BR overhaul interval, coaches | full vehicle overhaul "approximately every two years", examinations at 1/3/6/12 months | overhaul only; routine exams separate | vehicle | STATED | Hansard, 11 Mar 1996, vol. 273; https://hansard.parliament.uk/Commons/1996-03-11/debates/3523c0ba-a67a-4c8e-bb28-bb2605561e75/Railways(RollingStockMaintenance) |
| 26 | 1978 | HST annual works overhaul | 15 working days, target 3 weeks out of service | annual workshop overhaul; depot exams separate | per vehicle-year | MEASURED | Power, *High Speed Train — Fleet Operation*, Proc IMechE 192 (1978); https://steane.com/images/documents/IMechE/High%20Speed%20Train%20-%20Fleet%20Operation.pdf |
| 27 | 2022 | GBRf/Wabtec wagon contract | 720 wagons (570 Wascosa) + wheelset overhaul, "multi-million-pound", term not stated | planned preventive maintenance and failure repairs | fleet | STATED | Rail UK, 13 Jul 2022; https://railuk.com/contract-news/gb-railfreightawards-wabtec-uklongterm-maintenance-contract/ |
| 28 | 2026 | GBRf/Wabtec intermodal contract | 585 FEA wagons, 10 years, value not disclosed | pit-stop inspection and servicing | fleet | STATED | GBRf, 29 Jan 2026; https://www.gbrailfreight.com/gb-railfreight-signs-new-biggest-maintenance-deal-with-wabtec-in-peterborough/ |
| 29 | 2024 | GBRf, wagon maintenance practice | "wagon maintenance ... has not changed much in the last 50 years" | process, not cost | n/a | STATED | Rail Engineer, 15 Feb 2024; https://www.railengineer.co.uk/whole-life-cost-optimisation-main-line-passenger-and-freight/ |
| 30 | 2026 | GBRf, wagon maintenance level | "typically measured in pennies per mile" | "very small proportion of total train operating costs" | per mile | STATED | GBRf supporting statement, Mar 2026, para 2; https://nsip-documents.planninginspectorate.gov.uk/published-documents/TR050008-000220-Document%207.2B%20GB%20Rail%20Freight%20Supporting%20Statement.pdf |
| 31 | 2011 | UIP wheelset cycle | wheelset overhaul every 250,000 km; heavy at 1,000,000 km, about €1,800 an axle | wheelset only | per axle per event | STATED | report 40 §3, citing UIP WG 2011 §3.5 |
| 32 | 2020s | Wagon contract structure | standing fee per wagon-period plus an assumed 50,000 km a year, excess at €0.04 a wagon-km | full-service lease and maintenance | wagon-year / wagon-km | STATED | report 40 §3, citing Railtrans GTC cl. 10 |

## 4. The carriage series

**The 1961 composition.** The Beeching line is not maintenance-only. The same report prices
"provision of wagon" at 92s. for a single 6-ton wagon over 100 miles in its coal costing, a
charge that plainly includes the capital cost of the wagon; "provision" therefore includes
capital. The three functional lines total £157.0m against the £122.2m "maintenance of rolling
stock" line in the accounts, so **at most 78 per cent of the functional total is the
maintenance account line**; the rest is stabling, servicing and provision. I use the
functional figures as they stand and say so, because they are the only published split
between carrying units and wagons on one definition.

**Coach against multiple unit.** The £55.0m covers 35,057 coaches and 11,032 MU cars. A
modern MU car costs more to maintain than a coach because of the traction equipment; assuming
an MU car at 1.5, 1.75 or 2.0 times a coach gives £1,066, £1,012 or £963 a coach-year. The
central £1,012 is used; the ratio result moves only between 5.1 and 5.6 per cent.

**The series.** Values in 1900 money, per vehicle-year. "Measured" rows are converted from
the nominal figure; "interpolated" rows are log-linear between the measured points and are
ESTIMATE.

| Date | Nominal | 1900 money | Grade | Basis |
|---|---|---|---|---|
| 1892 | £33.3 gross; £21.6 net | 34.3 gross; 22.3 net | MEASURED | Hill Table II; general index 97; 35 per cent renewals removed for the net figure |
| 1920 | — | 68 | ESTIMATE | log-linear interpolation 1892-1961 |
| 1948 | — | 134 | ESTIMATE | log-linear interpolation 1892-1961 |
| 1950 | — | 140 | ESTIMATE | log-linear interpolation 1892-1961 |
| 1961 | £1,012 | 183 | MEASURED inputs, DERIVED split | Beeching rows 4-5, 11; MU at 1.75× coach; general index 552 |
| 1966 | — | 231 | ESTIMATE | log-linear interpolation 1961-1984 |
| 1970 | — | 277 | ESTIMATE | log-linear interpolation 1961-1984 |
| 1984 | £14,300-£26,200 | 374-686 | DERIVED | row 16 at 120,000-220,000 train-miles; 13 coach-equivalents per train |
| 1990 | — | 495 | ESTIMATE | interpolation 1984-2013 |
| 2013 | £33,000-£66,000 | 308-615 | DERIVED | row 17 × 150,000 miles; the low end applies the 2006 coach ratio (EMU ÷ 3), the high end takes the EMU rate whole |
| 2024-25 | £45,000-£66,000 | 296-433 | DERIVED | row 21 medians ÷ 3 for a coach; the all-vehicle median is £136,000-£199,000 (888-1,300) |

**What the series shows.** Real carriage maintenance per vehicle rose about 5.3 times between
1892 and 1961, reached £374-495 in 1900 money in the 1980s, and has been roughly flat since.
Serpell's £473m for 1982 is consistent with that: at an assumed 50,000 vehicles the fleet
average is £272 in 1900 money, and a coach at 1.5-2 times the fleet average is £408-544. The
1980s were a high-cost period on the industry's own evidence: Serpell records depot
maintenance costs up about 30 per cent real for some types between 1977 and 1981 and
attributes most of the rise to "a decline in efficiency" (para 6.46). The modern ORR medians
are higher than the RDG rate (up to £1,300 in 1900 money for an all-vehicle median) but they
cover traction, heavy maintenance and technical support; divided to a coach they fall back
into the same band.

**What it does not show.** No 1920, 1948, 1966 or 1990 point is measured; those rows are the weakest (§10).

## 5. The wagon:carriage ratio, and the two methods tested

| Date | Wagon | Carriage | Ratio | Grade |
|---|---|---|---|---|
| 1892 | £4.20 | £33.30 | 12.6% | MEASURED |
| 1900 | £4.20 (1892 figure) | £33.30 | 12.6% | MEASURED |
| 1920 | — | — | 8.9% | ESTIMATE, interpolated |
| 1948 | — | — | 6.3% | ESTIMATE, interpolated |
| 1961 | £54.3 | £1,012 | 5.4% | MEASURED/DERIVED |
| 1966-2026 | — | — | 5.4% held | ASSUMPTION (no later pair) |

**Method (a): scale the 1892 wagon level by the carriage index.** Predicted 1961 wagon =
£4.20 × (1,012/33.30) = £127.6. Actual £54.3. **Overstated 2.35 times.** The method fails
because it carries the 1892 ratio forward implicitly.

**Method (b): scale the wagon maintenance-to-capital proportion by the change in the carriage
proportion.** At 1892 a wagon at £70.7 (the pakset's 10-tonne capital) carried 5.9 per cent
and a carriage at about £1,000 nominal carried 3.3 per cent. At 1961 the carriage ladder gives
about £11,400 nominal for a standard coach, so a £1,012 maintenance figure is 8.9 per cent and
the carriage proportion has risen 2.7 times. The method predicts a wagon proportion of
5.9 × 2.7 = 15.9 per cent. The measured wagon figure is £54.3, and the proportion depends
entirely on the wagon capital used: £373 nominal on the pakset's frozen 1906 capital gives
14.6 per cent, £2,000 on a plausible 1961 16-tonne steel wagon gives 2.7 per cent, £1,500
gives 3.6 per cent. **The method cannot be tested without a measured 1961 wagon price, and it
swings by a factor of five across the plausible range.** It is therefore rejected as a
transfer rule, and it is also the wrong shape: it lets the wagon's own capital carry the whole
answer, which is exactly the quantity the files do not measure after 1906.

**Why both fail.** They both assume a stable relationship between wagon and carriage
maintenance intensity. The measurement says the relationship is not stable: the ratio fell
from 12.6 to 5.4 per cent because the carriage acquired interiors, heating, lighting,
corridor connections, air conditioning and electronics while the wagon acquired steel bodies,
larger bogies and air brakes but no interior. The correct transfer is therefore **the trend
common to the two, not the carriage trend alone**: the gross wagon level rose 2.3 times real
between 1892 and 1961 while the gross carriage level rose 5.3 times. A transfer that uses the
carriage index alone overstates by the difference (2.3 times).

**Which method the data support.** Neither in its pure form. The measured pair supports a
**ratio-declining** transfer: hold the measured 1892 and 1961 ratios, interpolate between
them, and hold the 1961 ratio after 1961 (there is no later pair, and the qualitative
evidence — GBRf's "pennies per mile", the standardised wagon, the long service lives — is
consistent with no further relative rise). This is the rule used for the recommended ladder
in §6. Its error bar is wide after 1961, and the assumption is named in the table.

## 6. Recommended ladders

**Carriage, 1900 money per vehicle-year, all maintenance including overhauls.** The
composition changes across the series, and each anchor says which it is. The 1900 and 1950
points are **gross of renewals** (Hill states "repairs and renewals"; the 1950 point is
interpolated between two gross anchors). The 1961 point is **gross of "provision"**, because
the Beeching functional line carries capital (see §4). The 1984, 1990 and 2020 points are
**net of capital**, because the train-mile rate, the RDG rate and the ORR medians all exclude
the capital lease. A single renewals treatment applied to the whole series is therefore wrong
at one end or the other; the workbook applies the 35 per cent deduction only where the anchor
is gross.

| Era | Value | Grade | Anchor |
|---|---|---|---|
| 1900 | 33 | MEASURED | Hill 1892 gross: £33.3 nominal at the general index 97 is £34.3 in 1900 money, so the anchor is 3.8 per cent below the deflated figure; kept at 33 on the workbook's existing basis |
| 1950 | 140 | ESTIMATE | log-linear interpolation between the two gross anchors; the 1961 measured point constrains it |
| 1970 | 265 | ESTIMATE | interpolation between 1961 (gross) and 1984 (net); the point is a blend and the workbook phases the renewals deduction out across it |
| 1990 | 460 | DERIVED | 1984 train-mile evidence and the 2013 RDG rate bracket it; net of capital |
| 2020 | 440 | DERIVED | RDG at 150,000 miles, and the ORR median divided to a coach; net of capital |

**Wagon, 1900 money per wagon-year, 10-tonne reference, all maintenance including overhauls.**

| Era | Value | Grade | Ratio used |
|---|---|---|---|
| 1900 | 4.2 | MEASURED | 12.6% of 33 (Hill's own pair) |
| 1950 | 8.7 | ESTIMATE | 6.2% |
| 1970 | 14.3 | ESTIMATE | 5.4% |
| 1990 | 24.8 | ESTIMATE | 5.4% |
| 2020 | 23.8 | ESTIMATE | 5.4% |

**Correction, 2026-11-25.** The 1961 deflator used in this section was 528, the 1959 general
index; the workbook's 1961 index is 552. The 1961 figures are therefore **£9.84 a wagon-year** and
**£183 a coach-year** in 1900 money, not £14.3 and £192. The nominal ratio is unchanged at 5.4 per
cent, and the ladder's 1970 value of 14.3 is a ratio-derived point (5.4 per cent of 265), not the
deflated 1961 level. The 2.0-per-cent-of-capital finding in the overhaul-share paragraph divided a
10-tonne wagon's annual figure by a 100-tonne wagon's capital; matched, the event is 20.2 per cent
at 10 tonnes and 5.1 per cent at 100 tonnes. The reconciliation of the 8-20 per cent band, the
20 per cent share and the interval is in
[wagon-overhaul-source-analysis](wagon-overhaul-source-analysis.md).

**Size adjustment.** Multiply by (payload tonnes / 10)^0.4. The exponent is an ESTIMATE: the
wheelset and bogie count rises about twofold across 10-100 tonnes (exponent about 0.3), while
the present 8-per-cent-of-capital rule implies 1.0; 0.4 is the midpoint and it keeps the
modern 100-tonne hopper close to the present rule. A 100-tonne 2020 hopper is therefore
23.8 × 2.51 = **£59.7** in 1900 money (£7,475 nominal at the 2020 index), against £56.6 under
the present rule. A 10-tonne 1900 wagon is unchanged at £4.2. Type (vacuum or air brake, flat
or hopper) carries no separate factor: Hill's ±50 per cent company range is the allowance for
type and mileage, and the size term carries capacity.

**Sensitivity.** Exponent 0.3 gives £43.9 for the 100-tonne hopper, 0.5 gives £69.6, and no
size term gives £23.8: a factor of 2.9 on the modern hopper, nothing on the 1900 wagon.

**Overhaul share.** Recommended 30 per cent of the carriage total and 20 per cent of the
wagon total, with the event every 2 years for a carriage and every 3 years for a wagon. The
measured total is the envelope: the head plus the amortised event equals the total, and the
event does not sit on top of it. On that reading a carriage event of 0.30 × 2 × annual = 60
per cent of a year's total is **9.2 per cent of the modern pakset capital** (£264 on £2,871)
before the renewals deduction, which sits at the bottom of report 36's 8-27 per cent band. The
wagon half of this paragraph was superseded by pass 46: the 20 per cent share at a three-year
interval does not fit the measured total, and the reconciliation — a 20 per cent share at six
years, event 1.2A — is in [wagon-overhaul-source-analysis](wagon-overhaul-source-analysis.md).
The carriage half was superseded by [report 44](research-pricing-report-44.md) and applied in
pass 47: the provision falls from 28 per cent of A in the 1830s-90s to 8 per cent from 2000,
because two measured events show it nearly flat in real money while A rose elevenfold. Both
halves remain estimates of the same kind — only the provision times the interval is constrained —
but the carriage half is now anchored on two measured event prices rather than on this
paragraph's judgement.

## 7. Cross-checks against direct modern wagon evidence

- **No direct British per-wagon-year figure was found.** GBRf's contracts (rows 27-28) do
  not disclose values; the ORR 2026 review excludes freight; the ORR 2009 market study's
  "wagon lease 50-60 per cent, maintenance 40-50 per cent of annual wagon costs" is recorded
  in report 40 without a retrievable citation and is not used as a level.
- **The qualitative statements fit.** £23.8 in 1900 money is £2,980 nominal in 2020; at
  50,000 km a year that is 5.9p a wagon-km, "pennies per mile" (row 30). A figure 2-3 times
  higher would be 12-18p, which the same statement does not comfortably fit.
- **The pakset's own rule fits at the top.** The 8-per-cent rule gives £56.6 for a 100-tonne
  hopper, 2.4 times the ratio ladder before the size term, and equal to it after the size
  term. The disagreement is therefore about *small and old* wagons, not modern ones, and no
  direct figure contradicts the ratio method; the 1961 aggregate contradicts it only if the
  ratio is held constant.

## 8. Error bars and assumptions

| Quantity | Central | Band | Why |
|---|---|---|---|
| 1892 carriage | 34.3 gross / 22.3 net | ±15% | Hill's own company range £18 6s.-£52 14s.; renewals share ±10 points |
| 1961 carriage | 192 | 182-202 | MU-to-coach multiplier 1.5-2.0 |
| 1961 wagon | 54.3 | ±25% | functional line includes capital and servicing; the 78 per cent bound is fleet-wide |
| 1984 carriage | 374-686 | wide | train mileage assumption 120,000-220,000 and the coach-equivalent split |
| 2013 carriage | 308-615 | wide | RDG rate is a modelled benchmark, not outturn; mileage assumption |
| 2024 carriage | 296-433 | wide | ORR median divided by 3; the division is the 2006 ratio, not a measurement |
| wagon ladder after 1961 | 5.4% ratio held | ±50% | one measured pair, 65 years before the modern era |

**Structural assumptions.** (i) The wagon trend is transferred from the carriage trend, so it
inherits any error in the carriage series. (ii) Wagons have no interiors, heating, lighting,
water or electronics, so the carriage trend **overstates** wagon growth; the measured fall in
the ratio (12.6 to 5.4 per cent) is the size of that overstatement between 1892 and 1961.
(iii) Modern wagons have air brakes, larger bogies and higher axle loads, which **understates**
it; the size term is the allowance. (iv) The method transfers the trend, not the level.

## 9. What this changes in the generator and the workbook

1. `New/ai/cost-balancing/evidence_data.py` line 775: `CARRIAGE_MAINT_YR = 32.6` becomes the
   five-point ladder `((1900,33.0),(1950,140.0),(1970,265.0),(1990,460.0),(2020,440.0))`,
   read with `interp()`, flat before 1900 and after 2020.
2. `evidence_data.py` lines 1327-1328 (carriage branch) and 1341-1342 (mail, TPO, brake and
   parcels, which scale the carriage rate by 0.5-0.75): read the ladder, scalars unchanged.
3. `evidence_data.py` line 1241 (multiple-unit cars) uses the same constant. That branch is
   **out of scope here**; it must not silently inherit the carriage ladder, which is why the
   constant is replaced by a named ladder rather than by editing its value.
4. `evidence_data.py` line 1352: `maint_gbp_yr=round(wcap * 0.08, 1)` becomes
   `WAGON_LADDER[era] * (tons / 10.0) ** 0.4`, with `WAGON_LADDER` =
   `((1900,4.2),(1950,8.7),(1970,14.3),(1990,24.8),(2020,23.8))`. `wcap` remains the capital
   figure; it is no longer the maintenance base.
5. `New/cost-balancing-maintenance.xlsx`, sheet **Rail vehicles**: column **Q** ("Measured
   fixed (GBP/yr)") and column **AA** ("Class fixed (GBP/yr)") for every rail carriage row and
   every wagon row; the derived columns **S** (GBP @1900), **T** (SC @1900/month), **U**
   (suggested .dat fixed) and **AE** (basis) follow automatically. The same columns exist on
   the Narrow gauge vehicles sheet, and the basis text must name the new source.
6. `New/cost-balancing-capital.xlsx`, sheet **Overhauls & upgrades**: the carriage and wagon
   overhaul shares and intervals. **Applied after this report:** the carriage half by pass 47,
   using [report 44](research-pricing-report-44.md)'s era table (an overhaul provision of 28 / 24
   / 19 / 12 / 10 / 8 per cent of the annual total at 6 / 5 / 3 / 2 / 2 / 2.6-year intervals) in
   place of the 30 per cent flat estimate given in §6 of this report; the wagon half by pass 46,
   per [wagon-overhaul-source-analysis](wagon-overhaul-source-analysis.md). `evidence_data.py`
   now carries `CARRIAGE_OVERHAUL` and `WAGON_OVERHAUL` and `overhaul_profile()` takes the
   measured maintenance figure.
7. `New/ai/vehicle-cost/source-composition.md` and `maintenance-decomposition.md` would need
   the 1961 composition and the declining ratio recorded. Not done in this pass.

## 10. Gaps

- **No measured carriage figure for 1920, 1948, 1966 or 1990, and no measured wagon figure
  after 1961.** The routes to close them are the BR annual accounts (1948-68), the BR sector
  accounts (1982-94) and the unpublished GBRf contract values.
- **The 1961 line includes capital provision.** A BR traffic-costing manual defining
  "provision" would let the 78 per cent bound be replaced by an exact split.
- **No measured overhaul event for a BR coach at a named works.** Report 36's Chiltern,
  Greater Anglia and Class 158 figures are refurbishments, not routine overhauls.
- **The 1892 wagon average is a fleet average of 19 companies with a 2.7-fold range.** The
  size term does not carry the company/type variation Hill measured.
- **No direct check on the post-1961 ratio.** A published GB wagon maintenance contract with
  a value and a wagon count would test the 5.4 per cent assumption; none is public.
