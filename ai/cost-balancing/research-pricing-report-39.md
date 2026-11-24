---
status: draft
verified: New ex-15 working tree, 2026-11-24
---
# Research pricing report 39 (2026-11-24: seven parallel passes)

Seven research tasks run in parallel on 2026-11-24, one per standing gap identified in
[cost-data-coverage](../cost-data-coverage.md). Each section records its findings, its dead ends
(so no settled search is repeated) and its remaining routes. Companion rows:
`research-pricing-rows-39.csv`. Where a figure is marked DERIVED the arithmetic is shown; where
MEASURED-INDEX the figure was read from a search extract of a paywalled primary and needs
confirmation at source.

Sections 5-7 (locomotive maintenance; the Commercial Motor interwar tables; tram car-only
maintenance and coke prices) are appended when those passes report.

## 1. Wagon and carriage maintenance: Hill 1895 Tables II and III recovered

The largest single gap in the maintenance evidence is closed. Hill, A. J., "Repairs and Renewals
of Railway Rolling-Stock (including Appendixes)", *Minutes of the Proceedings of the Institution of
Civil Engineers* 122 (1895), pp. 224-264 (doi 10.1680/imotp.1895.19704) has **three** vehicle
tables in Appendix II: Table I locomotives, **Table II carriages (pp. 240-241)**, **Table III
wagons (pp. 242-243)**. The knowledge base previously cited "Table I" for all three and recorded
the wagon column as unreadable and the carriage column as unattributed. Both are now read from the
page images of Internet Archive `minutesproceedi43britgoog` (Google/Harvard scan), 2026-11-24.

**Wagons (Table III)**, per wagon per year, five years ending June 1892, "maintenance, that is the
cost of repairs and renewals":

| Company | Stock | £ per wagon-year |
|---|---:|---:|
| Great Eastern | 15,311 | 4 12s. |
| London, Chatham & Dover | 2,045 | 6 10s. |
| North-Eastern | 79,366 | 5 10s. |
| London & North-Western | 55,126 | 2 4s. |
| Lancashire & Yorkshire | 20,993 | 4 |
| Glasgow & South-Western | 12,630 | 3 12s. |
| Great Northern | 24,375 | 3 8s. |
| London & South-Western | 8,934 | 6 |
| South-Eastern | 5,128 | 4 14s. |
| Midland | 95,214 | 4 16s. |
| Manchester, Sheffield & Lincolnshire | 13,762 | 3 12s. |
| Great Western | 42,184 | 4 6s. |
| London, Brighton & South Coast | 7,133 | 3 12s. |
| Caledonian | 46,800 | 2 12s. |
| North British | 40,618 | 2 12s. |
| Midland Great Western (I) | 2,168 | 4 |
| Great Northern (I) | 3,517 | 4 10s. |
| Belfast & Northern Counties | 1,731 | 3 10s. |
| Great Southern & Western (I) | 3,658 | 5 12s. |
| **Average of 19 companies** | | **4 4s.** (3.66d. per goods train-mile) |

**Verification and the fixed/variable question.** Every per-wagon figure reproduces from Hill's own
per-train-mile rate × goods train-miles per wagon, and the column order is validated by the mileage
subtotals. The rate/miles pairs (d per goods train-mile × miles per wagon-year) are: GER 2.50 ×
438 · LCDR 5.29 × 296 · NER 7.80 × 182 · L&NWR 1.59 × 360 · L&YR 3.20 × 298 · G&SWR 4.13 × 208 ·
GNR 2.13 × 380 · L&SWR 3.66 × 392 · SER 3.72 × 306 · MR 4.88 × 238 · MSLR 1.92 × 458 · GWR 2.55 ×
400 · LBSCR 4.10 × 210 · CR 4.54 × 140 · NBR 3.42 × 176 · MGWR 2.75 × 360 · GNRI 4.12 × 264 ·
BNCR 3.75 × 228 · GSWRI 3.99 × 340. One printed inconsistency: the L.B.&S.C.R. goods-miles-per-wagon
cell reads "300" where 210 (= 1,498,118 ÷ 7,133) is internally consistent.

**The fixed (per year) versus distance-driven (per km) split is NOT derived.** A cross-company
regression of cost per wagon-year on miles per wagon-year (2026-11-24) gives a £3.44 intercept and
0.61d/mile with **r² = 0.04** (stock-weighted: negative slope, r² ≈ 0); the per-mile form
(d/mile on 1/miles) gives 1.31d/mile variable + £2.66 fixed with r² = 0.37 but is heteroskedastic.
The cross-sectional scatter (accounting practice, wagon mix, idle share, repair standards) swamps
the mileage signal — the apparent inverse relation is largely the ratio's own denominator. The
intercept form weakly suggests fixed-dominated upkeep, the opposite direction from the road
vehicles' estimated 75/25 distance/standing split. Entering the figures into `fixed_cost` or
`runningcost` must wait for one of: the GER half-yearly series (Table IV) regressed within-company
against goods miles per half-year (the right structure); an engineering decomposition (wheel,
axle and spring wear against mileage; body, roof and paint against age); or modern maintenance
contract structures. Separately, Hill's total includes **complete renewals**, which in-game are
capital (the player's repurchase), so the figure must be netted of the renewal share before it
enters either field — the post-1911 MoT returns' "Complete renewals (wagons)" against "Repairs and
partial renewals (wagons)" columns are the measured route to that share. The same three-way
question stands for carriages (currently entered as all `fixed_cost`) and locomotives. The company spread is informative: large low-utilisation fleets
(Caledonian, NBR, L&NWR) run £2-2 12s.; small intensively-worked fleets (LCDR, LSWR) £6-6 10s.
Table IV (p. 244) gives the GER half-yearly series with wages and materials separate (e.g. Dec
1888 wages £15,317 + materials £22,020 = £37,950, 2.78d. per goods train-mile, stock 14,821);
Dec halves run about 30% dearer than June halves.

**Carriages (Table II)**, per carriage per year, same period and scope: G.E.R. £28 · L.C.&D.R. £31
· N.E.R. £45 6s. · L.&N.W.R. £52 14s. · L.&Y.R. £45 10s. · G.&S.W.R. £25 10s. · G.N.R. £41 12s. ·
L.&S.W.R. £26 4s. · S.E.R. £31 6s. · Mid.R. £40 14s. · M.S.&L.R. £27 6s. · G.W.R. £39 6s. ·
L.B.&S.C.R. £18 6s. · C.R. £36 14s. · N.B.R. £23 10s. · M.G.W.R. £34 · G.N.R.(I) £28 6s. ·
B.&N.C.R. £25 8s. · G.S.&W.R. £32 12s. · **average £33 6s.** The eight values the knowledge base
held map onto G.N.R., L.&S.W.R., M.S.&L.R., S.E.R., G.W.R., Mid.R., N.E.R.; the "company
attribution lost" note is obsolete.

**1929 private-owner repair contract**: Colchester Gas Company, 20 wagons, contractor Thomas
Burnett & Co, Hexthorpe Wagon & Wheel Works, Doncaster, £5 per wagon per year (£100 p.a.) for a
seven-year repair agreement (Essex Archives Online D/F 27/2/108, agreement 3 June 1929). Rate as
catalogued; the archival original is not digitised. The 1888 British Wagon Co → W. Edgar & Co £39
for five wagons (Gloucestershire Archives D4791/45/5) is **lease/hire, not maintenance** — context
only.

**Settled: the pre-1911 published returns carry no wagon-only money line.** The 1907 *Railway
Returns* (archive.org `op1255486-1001`) print "Repairs and Renewals of Carriages and Waggons" as
one combined line throughout (Abstract No. 16, Appendix C, No. 21). The carriage/wagon split
existed only in the companies' internal half-yearly workings. This is a structural absence, not an
OCR problem. The post-1911 MoT statutory form **does** separate "Complete renewals (wagons)" and
"Repairs and partial renewals (wagons)", so a 1912+ per-wagon-year series is realistic from those
volumes — HathiTrust/print only (library route).

**Wagon overhaul price: none in any era.** Confirms and extends report 36 §8. Hansard 1943-47
wagon overhaul/repair answers yield volumes and percentages only (5.28% of pool under repair Nov
1943; 182,082 wagons under or awaiting repair Nov 1947). The nearest measured per-overhaul price
is a **road steam wagon** maker's annual overhaul at £40-70 (*Commercial Motor*, 10 March 1933) —
order of magnitude only. Surviving route: undigitised repair invoices and agreements (Oxfordshire
History Centre B8/A5 incl. a 1913 GWR rerailing invoice; Essex D/F 27/2/108; Chasewater RCH
"Private Wagons Stopped for Repairs" 1926, "Re. Repairs to Wagons" 1943; Wagon Repairs Ltd worked
on 10% commission on Gloucester-held contracts). Archive enquiry or reading room; not web work.

Dead ends checked first: report 1 §5/6 (HathiTrust 403; Returns OCR), report 36 §8, report 23
§S4.2, report 15 §7. Gloucester RCW had about 25,000 wagons on repair contract across about 1,000
depots by 1918 and seven-year contracts are documented per customer (Burtt, Beak, Teague,
Crowther, Clee Hill Granite) but no rates are in print.

## 2. Carriage build prices 1935-1980

Two anchors now stand inside the 47-year gap (full reasoning: [cost-data-coverage](../cost-data-coverage.md)
"Rail carriages"):

| Year | Item | Figure | Coverage | Source |
|---|---|---|---|---|
| 1955 | BR passenger carriages, Modernisation Plan programme average | **£7,400/vehicle** (DERIVED: £230m ÷ about 31,000) | complete vehicles, plan prices (1954-55), loco-hauled + EMU + DMU | BTC *Modernisation and Re-equipment of British Railways* (1955) para 74, https://www.railwaysarchive.co.uk/documents/BTC_Mod001.pdf — figure read from the page image; the hidden OCR misreads it |
| 1955 | Same table, fleet reconciliation | 42,300 → 36,200 vehicles (loco-hauled 37,200→23,200; EMU 4,800→8,400; DMU/railcars 300→4,600) | denominators | same, p.21 table |
| 1955 | "Passenger traffic" heading (stock + stations + parcels depots) | £285m (headings reconcile: 210+345+285+365+35 = £1,240m) | bounds the carriage figure below £285m | same, pp.6-7 |
| 1959-63 | Coaching investment | £41m (1959), £30m/yr (1960-63); 5-yr totals £100m loco-hauled+EMU replacements, £30m MU diesel trains | annual allocation | BTC *Reappraisal* (Cmnd 813, 1959) paras 41, 49-50, https://www.railwaysarchive.co.uk/documents/BTC_Reappraisal1959.pdf |
| 1971 | BR inter-city coaches (Mk 2F / early Mk 3 era), 600 | **£16m = £26,667/coach** (DERIVED) | capital approval, complete coaches | Hansard HC 5 Nov 1971 vol 825 c37W, https://api.parliament.uk/historic-hansard/written-answers/1971/nov/05/railways-rolling-stock |
| 1971 | High-capacity coal wagons, 500 | £2m = £4,000/wagon (DERIVED) | same answer | same |
| 1971 | "90 car-sets", Great Northern suburban | £12m; per-unit NOT computable ("car-set" ambiguous) | EMU | same |
| 1955 / 1957 | Carriage build output | 1955: 1,713 passenger + 341 other coaching (incl. 282 EMU, 111 DMU); 1957: 1,964 + 596 (incl. 904 DMU) | production counts | *Facts and Figures about British Railways* 1956 & 1958 edns, https://my1950s.com/wp-content/uploads/2022/02/BR-1956-OCR.pdf , https://my1950s.com/wp-content/uploads/2022/04/br-1958.pdf |

Coherence check: £7,400 (1955) → £26,667 (1971) is consistent with about 2.3× price inflation plus
specification growth; £26,667 → the KB's early-1980s Mk III £100,000 with about 2× inflation plus
Mk III uplift.

**Dead ends (settled, do not repeat):** Modern Railways archive library-only (report 21); Pullman
1957 enquiry published no returned prices (report 8); Riddles 1950 JILE paper is motive-power only
(Class 5 £16,000; diesel £78,100; electric £37,400); BTC "Facts and Figures" 1956 & 1958 carry
production quantities, zero unit prices; Divall & Shin (JTH 2018, White Rose) on the Mk 2 coach is
qualitative (lead inside: TNA AN 97/124, Carriage Standards Committee minutes); Wikipedia's "£285m
of new carriages" is wrong — that is the heading; the page image shows £230m; Hansard 1948-63 gave
aggregate investment answers only; archive.org has no copy of the 1955 Plan and HathiTrust returns
403; no utility-coach price in any free source.

**Remaining routes:** Hansard Block C (HST/APT/Mark 3 cost questions 1974-80; historic Hansard has
no full-text search — find via Exa site: queries); RCTS Digital Archive (*Railway Observer* 1948-69
searchable PDFs at £6/volume, free 600 MB index PDF first); Grace's Guide contract notices 1935-48
(best free hope for Big Four and utility coaches); TNA AN 97/124 and RAIL carriage works cost
records (reading room — best route to Mark 1 outturns); NRM BTC/BRB *Statement of Accounts and
Statistics* (expenditure ÷ additions method) and the trade-press archives.

## 3. Multiple-unit and early electric purchase prices

| Year | Item | Figure | Coverage | Source |
|---|---|---|---|---|
| 1954 | First-generation DMU, 1,408-vehicle tranche (858 motor + 550 trailer) | £17,570,000 = **£12,479/vehicle** (DERIVED) | complete vehicles incl. BUT engines/transmissions; estimated cost approved 16 Dec 1954 | BTC Works & Equipment Committee memo 2 Dec 1954, transcribed at https://www.railcar.co.uk/topic/archive/54-12-02/ |
| 1954 | First tranche, schemes itemised | £3,112,487 incl. £171,733 jigs/shops; vehicles only £2,940,754/232 = £12,676; per-scheme e.g. W. Riding 16 motor £249,880 (£15,618 ea.), Metro-Cammell 72 £794,886 (£11,040 ea.) | as above | same memo |
| 1954 | GRC&W tender, Class 100-type | power car £20,811/£19,843/£19,300 and trailer £14,671/£13,723/£13,186 at 10/20/50 | tender prices; measured volume-price curve | https://www.railcar.co.uk/type/class-100/orders |
| 1955 | Derby-built share of the 1,408 (374 motor + 124 trailer) | "approximately £6 millions" ≈ £12,050/vehicle | works cost | Lightweight Trains Cttee min. 29, 11 Jan 1955, https://www.railcar.co.uk/topic/lightweight-trains-committee/meeting-29/page-06 |
| 1956 | Standard DMU motor car (Derby) | £15,200 (single-car prototype £15,500 "being £300 above") | works cost | Diesel Lightweight Trains Cttee min. 39, 15 Mar 1956, https://www.railcar.co.uk/topic/lightweight-trains-committee/meeting-39/page-03 |
| 1956 | Railbuses, 20 | tenders: W&M Donauwörth £13,888+duty; Wickhams £11,500; A.C. Cars £10,000; Bristol CV £11,000 | complete vehicles | W&E Cttee memo 30 Oct 1956, https://www.railcar.co.uk/topic/archive/56-10-30/ |
| c.1986 | Class 319 (PR85 extra batch), 16 four-car | "around £660,000 per vehicle in modern money" (2017-18 prices) | restated, not nominal | Roger Ford, *Modern Railways* 22 Mar 2018, https://www.modernrailways.com/article/record-spending-periodic-review-1985 |
| 1995 | BR passenger fleet business values | NBV £1.84bn/11,258 vehicles ≈ £163,000; "cost new" £3bn ≈ £266,000 | second-hand fleet values, not new-build; mixed fleets | Hansard HL 27 Nov 1995, https://api.parliament.uk/historic-hansard/lords/1995/nov/27/british-rail-rolling-stock-valuation |
| 1995-96 | Per-ROSCO sales | Angel £696m/3,753 (£185k); Eversholt £580-598m/4,050 (£145-148k); Porterbrook £527-528m/3,455 (£153k) | fleet business value | DoT press release 9 Nov 1995, https://www.railnews-business.co.uk/rh7/archive/arc_article.php?doc=1995-11-09+DoT-001 ; Hansard HL 12 Jun 1996 |

Restated from passes 23, 26 and 27 so the ladder is in one place: Class 508 £151,163/car (1979-80);
Class 141 £200,000; Class 142 £170,000; Classes 150/2, 155, 156 £263,204 (1984-86); LU per-car
1972-2010 (report 26 §7); LSWR 1915 conversion £1,520/car (report 27).

**Dead ends (settled):** BTC Reappraisal 1959 has programme totals only; the 1954 Plan scan is
images-only (report 39 §2 read it via page images for the carriage figure); Hansard 1964/1970
investment answers are £m aggregates; no cost figures for Classes 313/317/321/455 in TRID,
Wikipedia or Modern Railways; Grace's Guide LOR/District pages carry no money; *Engineering*
1903-08 and *The Engineer* 1889-94 greps find order news without values (report 27 corroborated);
*The Electrician* 1889-1907 undigitised (only vol 57); no GWR/SR railcar or 1920s EMU prices in
free sources.

**Remaining routes:** (a) 1950s-60s EMU per-car (302/304/305/308/310/312) — Railways Archive AEI
booklet "High-Voltage Multiple-Unit Stock" (docID 4082, page images), BTC works-committee papers
1958-61 at TNA/NRM (the railcar.co.uk transcriptions prove these carry per-scheme costs), BTC/BRB
Annual Report & Accounts 1958-62, NRM Railway Gazette runs; (b) 1980s order values (313/317/321/
455/158) — trade press at NRM, BRB annual reports 1984-91, Hansard on PTE-funded batches;
(c) ROSCO per-class values — 1998 NAO report on the sales and the three ROSCOs' first Companies
House accounts (free), split by EMU/DMU/HST with ORR counts; (d) 1890-1910 — **Electric Railway
Journal 1905-11 volumes are on archive.org** (this route produced the EF1 price in report 27);
TfL Corporate Archives LT001652/001 (C&SLR accounts), Met minutes (LMA GLC Acc 1297/MET), District
1905 order papers, Benest (LURS) at NRM/LURS library; (e) 1920s-40s — TNA RAIL 126/127, RCTS
Digital Archive, GWR Board papers (RAIL 264).

## 4. Permanent way 1900-2020s; depot maintenance; demolition and tree removal

### 4.1 Maintenance and renewal money heads, GB (MEASURED unless marked)

| Year | Head | Figure | Coverage | Source |
|---|---|---|---|---|
| 1955 | "Maintenance and Renewal of Way and Structures" | £83.7m | incl. signalling, structures, stations, renewal in revenue | BR *Facts and Figures* 1956 ed. p.5, https://my1950s.com/wp-content/uploads/2022/02/BR-1956-OCR.pdf |
| 1958 | "Maintenance of Way and Structures" (signalling separate, £35.2m) | £80.3m | cleaner scope | BR *Facts and Figures* 1959 ed., https://my1950s.com/wp-content/uploads/2022/04/br-1959.pdf |
| 1961 | "Maintenance of way and structures" (signalling £39.1m separate) | £85.4m | GB, excl. signalling | Beeching 1963 Part 1 p.6, https://en.wikisource.org/wiki/Page:The_Reshaping_of_British_Railways_(Beeching_Report).pdf/10 |
| 1961 | Beeching "cost of providing the signled track" | £110.0m total; £2,000/route-mile (cat. D single) to £15,000 (cat. A 3+-track) over 17,800 route miles | **includes signalmen's operation** — not comparable with the £85.4m head | Beeching Part 1 p.9, https://en.wikisource.org/wiki/Page:The_Reshaping_of_British_Railways_(Beeching_Report).pdf/13 |
| 1981 | Track renewals £128m; track maintenance **and ballasting** £173m; structures maintenance £42m | 26,500 track-miles (10,800 route-miles) | 1982 prices | Serpell, *Review of Railway Finances* (HMSO 1983) ch.6 ¶6.8, 6.18, https://railnews-business.co.uk/docs%20library/1982%20The-Serpell-Report-on-Railway-Finances-1982.pdf |
| 1998/99 | Railtrack maintenance £694m; renewals £1,130m (track renewals £354m) | GB | | Railtrack 1999 Annual Reconciliation Statement (MEASURED-INDEX) |
| 1999/2000 | maintenance £663m; renewals £1,285m (track £386m) | GB | | Railtrack 2000 Annual Reconciliation Statement |
| 2001/02 | Disclosure Statement 4: renewals total £1,911m (track £802m); maintenance total £951m (track £530m) | GB | | via Network Rail regulatory statements mirror (MEASURED-INDEX) |
| 2004/05-2008/09 | maintenance £1,271m→£1,104m; renewals £2,665m→£3,144m | GB | | Network Rail 2009 Annual Return Table 6 (MEASURED-INDEX) |
| 2010/11-2023/24 | ORR: maintenance and renewals regional average £152k/track-km-yr; MDU day-to-day maintenance £35k (2021-22) to £49k/track-km-yr (2023-24) | GB | MDUs cover 59% of maintenance spend | ORR cost benchmarking 2023-24 ¶1.7, 2.2, 2.8, https://www.orr.gov.uk/sites/default/files/2024-12/cost-benchmarking-of-network-rail-annual-report-2023-2024.pdf |

DERIVED per track-km-year (running track estimated at 1.92 × route from Beeching's 1961 ratio where
not stated): 1955 ≈ £1,420 (combined head); 1958 ≈ £1,380; 1961 £1,553 (34,150 running track-miles
measured); 1981 £4,055 (track maintenance and ballasting, 1982 prices); 1981 renewals £3,000
network-average; 2023-24 £49,000 (MDU) to about £150,000 (with renewals).

### 4.2 Renewal / installed cost per km

| Year | Item | Figure | Source |
|---|---|---|---|
| c.1955 | National track renewal expenditure | £17m/yr, of which about £6m new rail (MEASURED-INDEX: ICE 1955 paper, Emerald PDF blocked) | Proc. ICE Engineering Division Papers, iicep_1955_11425 |
| c.1955 | DERIVED cost per track-km renewed | £17m ÷ 1,819 track-miles renewed = **≈£5,800/track-km** | renewal volume from *Facts and Figures* 1956 p.37 |
| 1938-58 | Renewal volumes, track-miles/yr | 1938: 1,934; 1948: 2,018; 1951-55: 1,819-1,875; 1958: 2,017 | *Facts and Figures* 1956 & 1959 |
| 1946 | WR relaying **labour only**, new plain line | £1,318/mile = £819/km (149 miles relaid) | ICE 1960 discussion, M. G. R. Smith (CCE WR), doi 10.1680/iicep.1960.11808 (MEASURED-INDEX) |
| 1958 | WR relaying labour: manual £2,000/mile; mechanized £1,520/mile = £944/km; saving £430/mile | | same |
| 1981 | DERIVED full renewal ≈ £120,000/track-km | £128m ÷ (2.5% steady-state × 26,500 track-miles); weak link: 1981 volume not measured | Serpell + ORR 2010 benchmarking ¶4.30 |
| 2014-19 (CP5) | Conventional track renewals £578k/track-km (2023-24 prices) | 13% of renewals spend | ORR 2023-24 Annex C Table 3 |
| 2019/20-2022/23 | £869k/track-km (CP6 yrs 1-4 avg) | | same |
| 2023-24 | **£1,108k/track-km** GB (+7%/yr real since 2014-15); NR renewed 2.4% of track | | ORR 2023-24 ¶3.17-3.20 |
| CP5/CP6 (KB has) | full plain-line replacement £1.41-1.45m/track-km; rail-only 18-22%; re-ballast 42-46% | | ORR Table 4.3 via report 3 |

### 4.3 Technology change (justifies the era break)

FB track standard early 1949 ("more costly to instal but less maintenance, longer life", Hansard
30 Mar 1950); 1955-58 rail sections 109 lb/yd FB replacing 95 lb bullhead, 98 lb replacing 85 lb
on C, D-class renewed with cascaded bullhead; 2,112-2,288 softwood sleepers per single-track mile;
pre-assembled 60-ft panels 2,500 miles by 1956, 4,800 by 1958; long-welded rail 2,343 route-miles
end-1965 (*Facts and Figures* 1966); CWR dominant and relaying machines at 13 miles/yr by 1981
(Serpell ¶6.9-6.17); concrete sleepers and high-output renewal trains modern. Relaying **labour**
unit cost held roughly real-flat 1946-58 (money doubled; mechanisation recovered £430/mile).

### 4.4 The 1900-1930 money series: substantially solved

The Board of Trade "Maintenance of Ways and Structures" annual GB totals are digitised by NBER and
mirrored on FRED — the same head Acworth quotes (£500 a mile; FRED 1902 gives £461/mile):

- FRED A025AAGBA403NNBR (1860-1912): 1900 £9.54m; 1902 £10.21m; 1905 £10.59m; 1907 £11.26m; 1910
  £11.47m; 1912 £11.71m. https://fred.stlouisfed.org/data/A025AAGBA403NNBR
- FRED A025ABGBA403NNBR (1919-1933): 1919 £22.9m; 1920 £33.4m; 1921 £36.6m; 1922 £28.5m; 1925
  £24.0m; 1929 £22.5m; 1930 £21.1m; 1933 £18.1m. https://fred.stlouisfed.org/data/A025ABGBA403NNBR
- FRED A025ACGBA403NNBR (1928-1935) on a slightly different basis (1928 21.9 v. 22.5) — use one
  basis consistently.

DERIVED per km (route-mile divisors still to be pinned from NBER a02085a): 1900 £271/km; 1912
£311/km; 1921 £959/km (arrears catch-up year — Hansard 17 Jul 1922); 1925 £637/km; 1929 £600/km;
1933 £551/km. **Scope: combined maintenance and renewal of way, works and stations** (1868-Act
head). Company checks (Sheward for RCTS): Cheshire Lines £96.6-111.7k/yr 1900-07 over 143 route
miles (≈£675-780/mile); Metropolitan 1900 £58,055. Tension flagged: the KB's 1938 £384/km-year
combined figure sits below the 1933-derived £551/km — scope or divisor needs checking. Remaining:
an *installed* pw price 1900-1930 (1923 Grouping valuations — label valuations, not contract
prices; TNA RAIL and MT 45/47/64, summarised in *The Railway Gazette* 1925-27) and the mileage
divisors.

**Consistency flag on the KB's BR 1966 £44/km-year anchor** (now `[UNVERIFIED]` in
[infrastructure-cost-synthesis](../infrastructure-cost-synthesis.md) §2): the measured heads above
imply about £300-350/track-km-year at 1900 prices on the combined head; the £44 anchor is low by
close to an order of magnitude unless its scope is routine length-gang upkeep alone. Re-derive
before the post-1945 series rests on it. The ORR 2015-16 £334/km-year anchor does match the ORR
MDU day-to-day scope (£35-49k/track-km nominal) and is defensible if labelled as such.

### 4.5 Depot (engine shed) building maintenance

No clean figure this pass, but the account head is established: under the Railway Companies
(Accounts and Returns) Act 1911 / 1928 Order, Abstract A "Maintenance of Way and Works" carries
"Maintenance of Stations and Buildings", subdivided "Stations, Depots and Offices" / "Carriage
Sheds" / "Carriage Workshops or other Buildings" (structure read from the East London Railway Joint
Committee *Financial Accounts and Statistical Returns 1936*, https://transportist.org/wp-content/uploads/2016/07/erljc-1936-financial.pdf
— heads legible, figures not). One printed copy of a Big Four *Accounts and Statistical Tables*
volume or a post-1913 *Railway Returns* abstract (TNA/NRM/library) will produce the sub-head per
year. Beware: pre-grouping "shed expenses" in Locomotive Power accounts is a running head
(coaling, lighting, cleaning), not building repair. Modern partial: Serpell 1981 structures
maintenance £42m with "nearly 3,000 stations and depots" inside a wider £115m head. Two RSSB/BR
Research compilations exist behind membership (Thornton 1973 track-cost model Table 1; Orme 1979
economic statistics — the best single compilation of the BRB heads).

### 4.6 Demolition and tree removal

Buildings (labour constants, MEASURED via Barker, "Nineteenth-Century Labour Figures for
Demolition", TRAC 2010, doi 10.16995/trac2010_89_101): Hurst/Spon 1865 brick wall demolition 4.6
man-hours/m³ (≈40 man-hours/rod); Rea 1902 lime mortar 5.7, cement 6.9 man-hours/m³ (dismantling,
removing, cleaning, stacking); careful deconstruction for re-use 30-55% more man-hours than crude
demolition. DERIVED money at a builders'-labourer 7d/hour (c.1900): about 3s 4d-4s per m³ ≈ 29-35s
per rod, labour only (cite the wage from [staff-wages](../staff-wages.md) before use). Pre-1950s
norm: demolition often cost the client nothing — the contractor took the salvage (Reyniers et al.,
8ICCH 2024). Modern UK £50-120/m² of floor area (aggregator bands; unit caution: floor area against
the Victorian per-volume-of-wall constants). **Spon's money rates per rod/per square were not
located** — the target item in the scanned editions on archive.org.

Trees (MEASURED, Paths for All *Estimating price guide for path projects* rev. 2023): felling,
stacking and chipping £75-180 per tree (avg £127.50), 0.5-1.0 m girth £250-600; scrub clearance
£1,300-1,700/ha; hedge cut and leave £2.00-2.50/linear m.
https://walkingscotland.org.uk/wp-content/uploads/2025/05/estimating-price-guide-for-path-projects_paths-for-all_-rev4-march-2023-1.pdf
Modern garden-market bands £150-3,500+ by size (aggregators). **Historic tree-felling rates not
found** — routes: Spon's "cutting down trees" item; estate and forestry accounts (the kind Rackham
cites).

### 4.7 Dead ends this pass

ICE/Emerald full text paywalled (the 1946/1958/1955 figures are MEASURED-INDEX from search
extracts); BTC Report and Accounts 1948-62 HathiTrust 403 (GERS sells scans of the 1953 report
and *Facts and Figures 1980* for small sums); railnews-business.co.uk index pages 403 (individual
PDFs serve); 1923 valuation returns not surfaced by web search; Hansard PQs on track renewal cost
per mile 1950s-60s are qualitative; historic Hansard's /search endpoint unusable (known).

### 4.8 Remaining routes

1960s-70s heads and renewal volumes: Orme 1979 (RSSB SPARK IM-TAG-032; inter-library loan); BRB
Annual Report and Statement of Accounts per year (HMSO; TNA/large reference library);
*Transport Statistics Great Britain* on archive.org 1962-75. A measured BR-era renewal unit cost:
*Travers Morgan* supplementary Serpell volume (TNA MT 29) or BRB "miles of track renewed" 1963-96.
1945-50 head: MoT *Summary Table of Statistical Returns of Railways of Great Britain 1938-1947*
and *Government Control of Railways* (TNA MT series / legal deposit libraries). 1955 renewal cost
decade-indexed: the ICE 1955 paper (institutional access) or the 1954 Plan document itself.
Depot: one printed accounts volume (above). Demolition money rates: Spon's scanned editions
(archive.org volume search-inside). Trees: estate/forestry accounts.

## 5. Locomotive maintenance gaps

*(pending — appended when the pass reports)*

## 5. Locomotive maintenance gaps

### 5.1 Pre-1890 repair: closed

Two coherent pre-1890 datasets, both ICE *Minutes of Proceedings*, both read in source:

**Price Williams, "The Maintenance and Renewal of Railway Rolling Stock", ICE Min. Proc. 30
(1870), paper 1,277, Table 6** (https://archive.org/details/minutesofproceed30inst) — per
train-mile and per engine-year, repairs **and renewals** of engines and tenders, company averages
over 5-23 years preceding 1869: LNWR 3.45d / £228.72 (11 yr to 1868); Great Northern 2.94d /
£228.00 (20 yr); Midland 3.56d / £275.24 (21 yr); Great Western 3.37d / £251.84 (5 yr);
Lancashire & Yorkshire 2.68d / £195.00 (18 yr); GSWR 3.03d / £219.50 (to 1875); plus GER,
LC&DR, LB&SCR, MSL, North London and SER at 2.74-4.39d / £212-357. Cross-checks in the same
source: engine net cost £1,513 (goods engine); "money life" 8.8 years (LSWR) to 12.3 (L&YR), so
repairs+renewals ≈ 8-11% of purchase price a year against Hill's ~12% in 1892.

**McDonnell, "The Repairs and Renewals of Locomotives", ICE Min. Proc. 48 (1877), paper 1,469**
(doi 10.1680/imotp.1877.22532; https://archive.org/details/minutesproceedi10britgoog) — July
1868-June 1876 per train-mile: LNWR 3.07d, Midland 2.87d, GNR 3.21d, GWR 3.22d, L&YR 3.20d,
GSWR 3.45d (wages about 1.3-1.9d + materials about 1.3-1.9d); discussion rules of thumb: large
English lines "about 3d per train mile", NER "about 4d"; GNR (Stirling) 1876 2.66d with 24,600
train-miles per engine-year ≈ £273.

**Conclusion**: the 1892 extrapolation is roughly right per engine-year (£195-275 pre-1869
against Hill's £184-253 in 1892) but understates early cost **per train-mile** (10-40% above
Hill's 2.51d average, because annual mileage per engine was lower at 16,000-18,600 train-miles).

**Component and overhaul money (pre-1890)**: goods engine + tender £1,512.88; total renewals over
a 30-year life £4,197 = £139.91 an engine-year (Price Williams Tables A/B); component cycles —
tubes/ferrules about 4-5 years £973 over 30 years, crank axles 6-year £256, boiler/axle-boxes/
firebox 7- and 10-year groups £672/£1,447, painting six-monthly; Midland boiler replacement £400
per boiler per 400,000 miles (actual break-up average 382,890 miles to 1896; Johnson 1898 via
Dodgson, https://personal.lse.ac.uk/colvinc/clio/Dodgson.pdf); Midland boiler lives 10-18 years by
class; Midland 1896 rate case: locomotive power 6.94d passenger / 9.29d merchandise / 11.68d
mineral per train-mile.

**TNA (undigitised, descriptions verified)**: RAIL 236/669 (GNR "Statement of cost per train mile
for locomotive power", 1856-66); RAIL 667/692 (Stockton & Darlington, 1854); RAIL 1110/269 (LNWR
1849-68); RAIL 254/24 (GWR 1901-25); RAIL 491/881 (Midland staff returns).

### 5.2 BR diesel/electric overhaul money: partial

| Year | Item | Figure | Coverage | Source |
|---|---|---|---|---|
| 1970 | BREL Swindon, Maybach loco engines (Class 52-type) | reconditioning "normally in excess of £5,000" | power-unit reconditioning at BR works prices | *Commercial Motor* 6 Mar 1970 p.83, https://archive.commercialmotor.com/article/6th-march-1970/83/old-engines-need-never-die-it-would-seemprovided-s |
| 2000-01 | Class 91 heavy general repair+modification, 31 locos | £30m ≈ £1m per locomotive (DERIVED) | heavy general incl. gearboxes, bogies, TPWS | RAIL "No rest for the '91s", 20 Mar 2013, citing RAIL 404 |
| 1977-81 | BREL repair cost by vehicle type | relative: locomotives +40%+, MUs +35-40%, HSTs +25%, coaches +15% per repair | index only | Serpell 1983 §6.51 |
| 1981 | BR rolling stock spend | £548m: £109m new build, £439m servicing/repairs/overhauls; BREL maintenance £266m | whole-system | Serpell §§6.49, 7.1 |
| 2018 | Class 37/47 full rebuild | about £600k; 'heavy general' Class 37 about £750k | trade-press bounds | *Railway Magazine* 4 Sep 2018 |

**The single most promising unmined document**: TNA **COAL 101/164**, NCB Operational Research
Executive, "The maintenance costs of diesel locomotives (first draft)", Apr 1957 — open at Kew.
With it: **AN 88/108** (Railway Executive, "Cost of Locomotive repairs: report", Mar 1950) and
**AN 112/89** (BREL, "Standard Documentation (Repairs and Overhauls)", Dec 1966) — BREL charged BR
on standard charges per job, so a charge schedule **is** a per-overhaul price list. Also COAL
101/17 (1948) and COAL 101/523/3 (1973). Explaining the public absence: Serpell §6.45 records that
BR kept no per-vehicle maintenance records before the "cost of ownership data bank" then under
construction (its outputs c.1985-92 would be M&EE/AM&P papers at the NRM, GB 756 series).

### 5.3 Diesel/electric operating cost per hour or per vehicle-mile

The practical chain: Beeching 1961 per train-mile by traffic class (fast/semi-fast 21.8d, stopping
14.9d, suburban 16.6d; freight 2.20d per wagon-mile — ch.3 Table 1) → TRB Special Report 180 (BR
depot data 1975: Class 87 electric 500 maintenance hours a locomotive-year incl. 150 cleaning;
Class 47 diesel 1,240; exam intervals 55/275/825/2,500/5,000 engine-hours; electric:diesel
maintenance-time 1:6 per km; https://onlinepubs.trb.org/Onlinepubs/sr/sr180/180-011.pdf) → Serpell
1975-82 per passenger-mile (9.2-11.3p) and per loaded train-mile (IC direct £5.68, 1981) → ORR
from 2000-01 (cost per vehicle-km mean £2.2 in 2010-11; cost per train-hour mean £736,
https://www.orr.gov.uk/sites/default/files/om/toc-benchmarking-report-2012.pdf) and McNulty 2011
(TOC cost £10.6 per train-km, 2009).

**Provenance of `Operators' per-km finances _ RailUK Forums.htm`**: railforums.co.uk thread 260369,
computed by a user from ORR table 7223/7233, April 2022-March 2023, per **passenger**-km (GB
totals: staff 7.2, diesel fuel 0.8, rolling stock 6.0, access 6.6, other 4.9 = 25.5p). The data is
ORR's and citable to ORR, not the forum; it corroborates modern cost *structure* only.

**Dead ends**: TRB host refuses direct fetches (Table 3 read via search extraction); Serpell Table
7.1 is image-only; historic Hansard free-text search unusable (day indexes work); ministers refused
to publish locomotive-works comparative costs (HC WA 16 Dec 1968 c275W; 31 Jan 1969 c403W); TNA
Discovery multi-term phrase queries silently return zero (two-term queries work); BoT Returns per
the settled dead end — unnecessary now, the ICE papers carry per-company series in readable text.

**Remaining**: Kew (above); BR sector Annual Reports & Accounts 1983/4-1996/7 (BL/NRM) and BTC
Annual Reports 1948-62 for cost-per-train-mile series; the Deltic five-year fixed-price maintenance
contract (1961) in English Electric records; *Diesel & Electric Locomotive Annual* (Ian Allan) —
untried, low probability.

## 6. The Commercial Motor interwar tables

Recovered: all three complete market ladders and the 1933-34 operating-cost tables. **Full
transcriptions** (every figure seen in the page scans, including the 1935/37 chassis-weight, tare
and rated-h.p. columns): [cm-transcription-1932](cm-transcription-1932.md),
[cm-transcription-1935](cm-transcription-1935.md),
[cm-transcription-1937-and-costs](cm-transcription-1937-and-costs.md).

**Repeatable method**: article text is in the page HTML; the scans are exposed only in the inline
`fullImages` variable (`.../issues/<issue>/<n>.jpg?size=x&token=...`, native 1028x1500); the CDN
rejects requests without `Referer: https://archive.commercialmotor.com/`; download each page and
read crops visually.

| Guide | Coverage | Convention |
|---|---|---|
| CM 3 May 1932, pp. 410-412 | about 250 models, 2 cwt-25 tons | chassis alone except rows flagged (van)/(with body)/(complete) |
| CM 10 May 1935, pp. 444-446 | the whole market again; no 8-9 ton class in the source | "Chassis Price"; complete-vehicle rows starred; weight/tare/h.p. columns |
| CM 30 Apr 1937, pp. 414-417 | as 1935 | chassis only throughout; weight/tare/h.p. columns |

Cross-validation against pass 30's prose rows: Commer 20-25 cwt £165 (1935 guide) matches the 1934
correction figure exactly; Morris-Commercial C11/30 £184½ (1935) sits between previously measured
tender/prose figures. The scans are being read correctly.

**Operating-cost tables (1933-34)**:

- **Steam wagons** (CM 10 Mar 1933, pp. 126-127): seven real vehicles' per-mile costs split fuel,
  oil, tyres, maintenance and depreciation (totals 5.12-12.33d; mean 7.62d at 17.6 mi/cwt), the
  journal's own comparison row (7.73d) and the maker's row (5.56d); the journal's recommended set
  for a 6-tonner: fuel 1.80, oil 0.30, tyres 1.60, maintenance 1.80, depreciation 1.73 = **7.23d a
  mile**, coal 15 mi/cwt at 48s 6d a ton or more, depreciation on a 160,000-mile life. Prose adds
  one steamer-year at £743 all-in, overhauls annually, boilers retubed every three years, tyre
  life 30,000 miles a set. This is the first measured operating-cost curve for steam wagons.
- **2-ton van standing charges** (CM 31 Mar 1933, p. 258): £237 10s a year itemised (licence
  £27 10s, insurance £20, ground rent £26, interest £8, wages £156) plus running costs by item.
- **2-ton lorry completed tables** (CM 10 Aug 1934, p. 876): running 2.90d a mile (fuel 1.15, oil
  0.05, tyres 0.45, maintenance 0.75, depreciation 0.50) and standing £4 13s 10d a week itemised.

**Not recovered**: road-test specification panels 1925-39 (the recipe works; each panel is a
separate fetch-and-read cycle — a future pass can continue where this stopped); **bus and coach
prices 1939-54** (unchanged; the one remaining open gap in the price ladder); the standalone
"Tables of Operating Costs" master tables and the 1935 "Table I of 7 cwt to 7 tons" (7 June 1935).
Scan ambiguities are flagged inline in the transcriptions (a handful of fractions and payload
pairings).

**Assessment**: the interwar lorry and van ladder is complete and same-day comparable at three
dates; steam wagons have measured operating costs for the first time; the 1933/34 haulier cost
structures fill the line-item gaps report 31 listed as blocked. Evidence grade: every figure was
seen in the scans except the few prose figures in the 1933 van article.

## 7. Tram car-only maintenance and coke prices

### 7.1 Tramcar maintenance, car only: solved

The structural question in [tram-maintenance](../vehicle-cost/tram-maintenance.md) is answered:
from 1919-20 the Ministry of Transport / Board of Trade tramway returns print "General Repairs and
Maintenance (or Renewals out of Revenue)" analysed into **Permanent Way | Electrical Equipment |
Engines or Horses | Cars and other Rolling Stock | Buildings, Fixtures, Tools and Miscellaneous**
(1924-25 onward: *Permanent Way | Electrical Equipment of Line | Cars and Equipment of Cars |
Miscellaneous*), and the "Abstract of Totals" page carries the GB totals of each sub-column. The
sub-columns sum exactly to the printed maintenance total in every year checked, which validates the
OCR-recovered figures. Coverage: repairs **and renewals charged to revenue** of cars and their
equipment only; car-miles (trailers counted) are the denominator. 1919-20/1920-21 are UK scope;
1922-23 onward GB.

National car-only totals and per car-mile (computed £×240 ÷ car-miles; combined head shown for
the share):

| Year | LA cars (GB/UK) | LA per car-mile | Car share of combined | Companies cars | Companies per car-mile |
|---|---|---|---|---|---|
| 1919-20 | £3,642,909 (area scope uncertain in OCR) | ≈2.8-3.0d (car-miles not read) | — | — | — |
| 1920-21 | £3,420,280 (UK) | ≈2.8-3.0d (order of magnitude) | — | £972,543 (UK) | — |
| 1922-23 | £2,559,714 | — | — | £662,760 | — |
| 1923-24 | £2,458,932 | 1.98d | 50.1% | £641,001 | 2.39d |
| 1924-25 | £2,395,733 | 1.84d | 50.7% | £508,505 | ≈1.85d implied |
| 1925-26 | £2,376,877 | 1.76d | 51.7% | £448,365 | 1.67d |
| 1926-27 | £2,273,261 | 1.71d | 52.4% | £418,783 | — |
| 1927-28 | £2,311,645 | 1.65d | 53.0% | £395,910 | 1.55d |
| 1928-29 | £2,292,675 | 1.63d | 53.7% | £367,533 | 1.49d |
| 1929-30 | £2,260,772 | 1.60d | 54.0% | £365,232 | 1.57d |
| 1930-31 | £2,205,420 | 1.60d | 54.4% | £332,758 | 1.51d |
| 1932-33 | £1,928,948 | 1.52d | 54.2% | £250,408 | — |

Sources: MoT *Returns … Tramways and Light Railways* per year, Abstract of Totals Part II
(archive.org items `railways00566412` (1919-20), `railways00566414` (1920-21), `railways00590412`
(1922-23), `railways00590413` (1923-24), `railways00609099`-`railways00609135` (1924-25 to
1929-30), `railways1675821-1001` (1932-33); 1930-31 via
https://www.ekeving.se/ext/uk/TW-LR-TT_1931/0-11.pdf (text layer). The combined d/car-mile
reproduces the existing A1 values to ±0.01d in every year — a further cross-check.

**Pakset rule**: car-only maintenance is **50-55% of the combined head** over 1923-33, the share
rising slowly as the permanent-way share falls. The existing combined series can be converted by
taking about half.

Named municipal undertakings, car-only (Part IIA "Cars and other Rolling Stock", renewals out of
revenue included), 1923-24 unless stated: LCC £568,948 · Liverpool £222,409 · Glasgow £159,769 ·
Manchester and District £150,467 · Birmingham £111,713 · Sheffield £85,521 · Leeds £71,699 ·
Leicester £41,597 · Bolton £31,029 · Blackpool £23,511 · Southampton £11,312 · Birkenhead £8,517 ·
Blackburn £8,035 · Middlesbrough £6,618 · Ashton-under-Lyne £5,688 · Accrington £5,170. 1922-23:
LCC £585,923 · Liverpool £244,253 · Manchester £153,670. 1920-21: Accrington £6,851 · Aberdare
£3,447. Pair with each undertaking's Part IV car-miles for per-car-mile figures.

**Remaining**: 1931-32 and 1933-39 car-only splits (one row each in the returns' Abstract of
Totals; BPP via ProQuest/library — archive.org holds only the years listed); per-undertaking
per-car-mile extraction (mechanical, page images); 1900-13 pre-war returns (whether they separate
cars is unknown; HathiTrust reading room); municipal abstracts now mainly useful for pre-1914.

### 7.2 Coke prices

Grades matter: **gas coke** is what the steam tramways burned; **furnace/foundry coke** is the
metallurgical grade. Prices per ton (2,240 lb pre-1971):

| Year | Grade, basis | Figure | Source |
|---|---|---|---|
| 1846-49 | Coke at the ovens, John Bowes & Partners, Durham | 8s-9s | Mountford, *History of John Bowes & Partners up to 1914* (Durham M.A. 1967) pp.120-21, https://etheses.durham.ac.uk/id/eprint/9966/1/9966_6760.PDF |
| 1853 | Marley Hill coke at ovens | 13s | same |
| c.1862-63 | Durham coke sold at the mines 8s-9s (cost 8s: coal 6s 9d + making 1s 3d); best coke f.o.b. Tyne 12s 6d-14s | as stated | Gruner & Lan, *Mining and Smelting Magazine* June 1863 p.324 |
| 1873 | Pontop ovens coke contract | 23s (yr 1), 18s (yr 2) | Mountford p.131 (Strathmore MSS, Durham CRO) |
| 1881 | Gas coke, Dewsbury (steam tram fuel) | 23s 6d | Kinnear Clark, *Tramways* (1894) p.453 — already in the KB |
| 1907 | Gas coke and breeze ex-works, UK gas undertakings | 11s 8¼d average (companies 12s 7d, public authorities 10s 2d) | Census of Production 1907 Preliminary Tables Part IX, https://archive.org/details/op1255951-1001 |
| 1914-17 | Foundry coke f.o.b. Tyne 19s-23s; best Durham blast-furnace coke Tees-side 19s (1915) → 36s (1916) → 42s 6d | as stated | Redmayne, *The British Coal-Mining Industry During the War* (1923) pp.9, 48, 85 |
| 1919 | Foundry coke f.o.b. Tyne 49s 6d-110s by market | as stated | same p.228 (column-mapping caveat) |
| 1920 | Gas coke exports £4 13s 9d; other coke £5 0s 6d | f.o.b. average value | Hansard HC 15 Mar 1920 c1770 |
| 1922-23 | Gas coke exports 30s 6d / 29s 2d | f.o.b. average value | Hansard HC 2 Jul 1923 cc44-5 |
| 1930-38 | Durham furnace coke delivered Middlesbrough, March each year | 20.00, 16.00, 16.35, 15.50, 20.10, 19.13, 23.13, 28.50, 36.00s | Hansard HC 13 Apr 1938 c1117 (Colliery Guardian quotations) |
| 1945 | Large coke, London, ex gas works 59s 3d-64s 5d by lot; 74s 10d retail | as stated | Hansard WA 20 Nov 1945 cc400-1W |
| 1959-65 | Gas coke sold by area gas boards | £7.47 → £9.57 a ton | Hansard WA 1 Feb 1966 c181W (Ministry of Power digest) |
| 2017-26 | Metallurgical coke, European export benchmark | €194/t (2021) → €519-722/t (2022) → €270-380/t (mid-2026) | steelonthenet (Trade Data Monitor); Britain has had no coke ovens since Port Talbot closed 20 Mar 2024 |

Observed coke:coal relationship: about **1.5-2.5×** coal at each date checked (1863, 1907, 1913-14,
1930s) — the check figure for the fuel tab.

**Dead ends (do not retry without a different access route)**: HathiTrust is completely
Cloudflare-blocked to this client (this blocks the Manchester/Liverpool abstracts, the BPP Gas
Undertakings returns 1882-1835 and *Gas World* vols 54-77); ekeving.se serves only pp. 1-11 of the
1930-31 return; the 1931-32 and 1933-39 returns are not online; Matthews, *The London Gasworks*
(Hull PhD 1981) Figure 11 (coke prices **1816-1914** — the one document that would close the whole
steam era) is Cloudflare-blocked at Hull with no Wayback copy; the 1919 Sankey report is
lending-only; the Samuel Commission 1926 gives coal at coke ovens, not coke selling prices; the
1924 Census "Coke and By-products Trade" is image-only.

**Remaining**: Matthews Figure 11 (browser session / BL EThOS / Hull library — highest value); BPP
Gas Undertakings returns 1882-1935 (annual coke sold and value per undertaking → national gas-coke
price); *Gas World*/*Gas Journal* annual reviews; Colliery Guardian quotations via BNA/Gale; Durham
Record Office NCB I/CO 493-494 (coke price ascertainments 1924-47) and 81-85 (selling-price
certificates 1871-1946); pre-1845 via early railway coke contracts (S&DR, L&M minutes, RAIL).
