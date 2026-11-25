---
status: draft
verified: none
---
# Research pricing report 41 (2026-11-24: web-accessible gaps, four routes)

Four routes from the handoff (3, 8, 9, 10) worked in order: (A) railcar.co.uk first-generation
DMU exam ladders, (B) 1939-54 bus prices and road-test panels, (C) carriage and electric stock
prices, (D) coke prices. Notation as in report 40: **M** measured in source, **S** stated,
**C** computed here, **L** lead only. Figures read from OCR text layers of scans are flagged
OCR-READ (page image not yet verified). Companion rows: `research-pricing-rows-41.csv`.
Downloaded third-party material with manifest: `ai/temp/research-pdfs/` (scratch; never committed).

## 1. Route A — first-generation DMU exam ladders (railcar.co.uk)

Retrieval works exactly as recorded in report 40 §1.9: a browser User-Agent plus
`Referer: https://www.railcar.co.uk/documentation/miscellaneous/` retrieves the PDFs under
https://www.railcar.co.uk/assets/maintenance/ . All four documents below were downloaded and
read (page images rendered from the PDFs with PyMuPDF; the PDFs are scans without text layers).

### 1.1 BR 87264/1 (Revised March 1965) — the 1965 ladder

*Standard Examinations of Diesel Multiple Unit Trains with Mechanical Transmission*, Circular
MP 11A, British Railways Board (Revised) March 1965. 67 leaves = 12 index pages + 55 numbered
sheet pages carrying items 1-196. Structure: "Index to Items" (part name → mileage or period →
item number), then job sheets with columns Item | Parts | Cars Applicable | Period in Miles |
Engine Running or Stopped | Description of work to be done | Remarks.

**Mileage bands** (interval at which each component gets attention): 625-750; 1,250-1,500;
2,500-3,000; 5,000-6,000; 10,000-12,000; 20,000-24,000; 30,000-36,000 (speedometers only);
40,000-48,000; 60,000-72,000; 120,000-144,000 miles; and 240,000-250,000 miles for Rolls-Royce
engines (item 180).

**Time bands**: Daily (propane gas equipment, buffet cars, item 1); Three Monthly (ambulance and
emergency tool cupboards, item 114); 6/8 Months (Smiths heater complete, item 186); Once or
Twice Yearly (coolant systems, item 185); Yearly, Two Yearly, Four Yearly, Five Yearly (all
fire-extinguisher weigh/renewal items 187-196).

**Named exams**: "General examination — (a) Body details (b) Underframes and bogie details" at
625-750 miles (item 8); "General examination — Mechanical" and "— Electrical" at 1,250-1,500
miles (items 16, 17). Higher bands are component job intervals rather than named exams.

**Cost or labour-hour figures: none.** The sheet format has no time or money column anywhere;
sampled sheets (item 2 engine oil sumps p.3; items 188-196 pp.54-55) confirm. Scope per item is
prose ("allow oil to settle for 5 minutes…", torque settings, dipstick pint figures per engine
type — e.g. AEC 150 h.p. 16 pints min-to-max).

**Correction to report 40 §1.7/§1.9.** The phrase "exams from 625 miles up to five yearly" is
the span of intervals covered by the 1965 index (625-750 miles up to the five-yearly component
renewals), not a five-yearly top exam. The five-yearly items are automatic fire-extinguisher
renewals only. The top *exam* event for first-generation DMUs is the No. 8 examination of the
1973 ladder (below): 80,000-96,000 miles / sixteen-monthly (LMR). The engine mapping in
maintenance-decomposition ("first-gen: … the 5-yearly top exam (DMU)") should use the No. 8
event.

### 1.2 BR 12014 / BR 12013 (Issue 1, June 1973) — the numbered ladder

BR 12014 *Standard Examination Schedules — Diesel Multiple Units with Mechanical Transmission
(Blue Square, White Circle)*, Issue 1 June 1973 (introduction signed October 1973), BRB Office
of the Chief Mechanical & Electrical Engineer. Its own text: "This issue replaces schedule BR
87264/1"; the format was "divided into two basic parts: (i) Examination summaries, (ii) Job
Descriptions", job descriptions being BR 12013 (Issue 1, June 1973; sections: engines incl.
fuel and coolant; transmission; brake equipment; compressed air; electrical; body/bogies/
underframe; fire protection and emergency equipment; train heating; AWS; lubrication charts).
A separate book BR 12014/1 covers hydraulic-transmission units (Red Triangle, Orange Star).

Exams are **numbered No. 1 to No. 8, plus a Daily check**. Frequencies (M, each region has its
own page):

| Exam | LMR mileage | LMR period | WR max mileage | WR period |
|---|---|---|---|---|
| No. 1 | 625-750 | 2-4 days | 750 | at fuelling point |
| No. 2 | 1,250-1,500 | weekly | 1,500 | weekly |
| No. 3 | 2,500-3,000 | two-weekly | n/a | n/a |
| No. 4 | 5,000-6,000 | monthly | 6,000 | monthly |
| No. 5 | 10,000-12,000 | two-monthly | 12,000 | two-monthly |
| No. 6 | 20,000-24,000 | four-monthly | 24,000 | four-monthly |
| No. 7 | 40,000-48,000 | eight-monthly | 48,000 | eight-monthly |
| No. 8 | 80,000-96,000 | sixteen-monthly | 96,000 | sixteen-monthly |

Eastern Region uses day periods by utilisation group (high = average ≥1,400 miles/week; medium
600-1,400; low = all others): No. 1 2-4/2-4/3-5 days; No. 2 6-8/6-8/9-12; No. 3 not applicable;
No. 4 18-21/24-28/36-40; No. 5 36-42/48-56/72-80; No. 6 72-84/96-112/144-160; No. 7
144-168/192-224/288-320; No. 8 not applicable (ER deleted No. 8 and added the "Low Mileage"
category). Scottish Region day periods (high/medium/low): No. 1 3/4/5; No. 2 6/[8]/10 (the
medium cell is misprinted or misread as "3"; the doubling pattern gives 8); No. 3 12/16/20;
No. 4 24/32/40; No. 5 48/64/80; No. 6 96/128/160; No. 7 192/256/320; No. 8 384/512/640.
Each region's page adds: "Certain parts are listed for change outside the examination sequence
on a mileage/time basis."

**Coverage structure**: BR 12014's "Examination Jobs Index" allocates every job number to exam
columns 1-8 (asterisks), and the "Examination Summaries" list, per exam, every job due at it
irrespective of the lower exams (e.g. No. 5 jobs 544-622 incl. starter motor security, earth
leakage test, jumper couplings, buffet-car equipment, body/bogie/underframe examination,
drawgear; No. 6 begins with the repair-book check and runs jobs 101-203+ engine/transmission
work incl. oil and filter changes, injector changes, speed checks). Engine-type variants (AEC,
Leyland, Leyland-Albion, Rolls-Royce, BUT) are called out per job. **No labour hours and no
costs** appear in BR 12014 or BR 12013 (job descriptions are prose and diagrams only).

BR 12014 **Issue 3 (February 1979)**: the Eastern Region frequency table is identical to Issue
1 (checked; p. ix) — the ladder was stable 1973-1979 on ER.

### 1.3 Inter-departmental labour split (Watford)

"Maintenance on Diesel Railcars by C&W Examiners", stamped Carriage & Wagon Watford (B.O.
62011), undated; the railcar.co.uk editor dates it to the Watford first-generation DMU
allocation May 1958 - January 1965. It prints "the inter-departmental division of responsibility
for maintenance of diesel units at maintenance depots" as a matrix over items × Power Cars /
Trailer Cars with Driving Cabs / Trailer Cars without Driving Cabs, departments M.P.S. (Motive
Power Supt's Dept.), C.&W.E. (Carriage & Wagon Engineer's Dept.), C.M.&E.E., C.O.S. (Chief
Operating Supt's Dept.). Engine, transmission and control equipment, exhausters and brake
valves, radiator fan drive, windscreen wipers, speedometer drive, Graviner fire extinguisher =
M.P.S.; roof tanks, brake pipes/cylinders/rigging/hosepipes, passenger communication
equipment, generators/batteries/lighting, heating, bodywork, gangways, buffing and drawgear,
bogies/wheels/tyres/axles = C.&W.E. Labour-organisation evidence only; no hours or money.

### 1.4 Engine mapping input

The first-generation DMU ladder is now fully measured: Daily + eight exams from 625-750 miles
(2-4 days) to 80,000-96,000 miles (sixteen-monthly) on the LMR duty basis, with regional
variants scaling by utilisation (ER/ScR) or topping out at No. 8 (WR/ScR). For the engine's
single interval field: the **No. 8 event (80,000-96,000 miles ≈ 129,000-154,000 km)** is the
top exam, with `overhauls_before_max_cost` = 7 rungs (No. 1 to No. 8) if each exam is a rung.

## 2. Route B — 1939-54 bus and coach prices; road-test panels

Method (report 39 §6) re-verified: article text is in the page HTML; page scans appear only in
the inline `fullImages` JS variable (`.../issues/<issue>/<n>.jpg?size=x&token=...`, one entry
per article page, leaf number = journal page number, tokens bound to the requested size); the
CDN requires `Referer: https://archive.commercialmotor.com/`. The archive's own
`/search?term=` endpoint is JavaScript-driven and returns empty to command-line fetchers
(dead end); issue browsing (`/issues?year=YYYY`, `/issue/<date>`) works.

**Prices verified at source** (each page fetched and read before recording):

| Date, page | Item | Figure |
|---|---|---|
| CM 28 Jul 1939 p.38 | Commer "Superpoise" 32-seat bus, complete (Waveney body) | £800 (incl. painting and lettering) |
| same | Commer 32-seat chassis | £335 |
| same | Commer 30-seat luxury coach, complete | £895 |
| same | Commer 26-seat bus / luxury coach, complete | £760 / £880 |
| same | Commer 20-seat bus / luxury coach, complete | £640 / £780 |
| same | Commer 20-seat chassis (12 ft 9 in wb) | £285 |
| same | Perkins P6 / P4 oil-engine option (larger / smaller chassis) | +£214 / +£183 |
| CM 7 Jul 1939 p.48 | Austin 26-seat passenger chassis | £328 |
| same | Burlingham/Plaxton 26-seat bodies: bus / bus-coach / coach / de luxe | £430 / £497 / £535 / £565 (20-seat £10 less each; one-man door +£12) |
| CM 3 Sep 1948 p.28 | Jensen 38-40-seat lightweight oil-engined passenger chassis | £1,675 ex-works |
| CM 8 Oct 1948 p.66 | Seddon passenger chassis (Perkins P6 Mk III N, 32-seat body) | £1,250 |
| CM 23 Oct 1953 p.36 | Whitson 44-seat bus body "Economist" / 41-seat coach body "Fairline" | £1,785 / £1,845 |
| CM 16 Jul 1954 p.43 | Whitson "Economist" 44-seat body (on Sentinel chassis) | £1,885 |

**Road-test panel, one read in full** (the method for the panels): "ROAD TEST No. 354 — SEDDON
BUS", CM 8 Oct 1948, journal p.294 (scan leaf 68): Seddon MK 4 single-deck bus; weights —
unladen 4 t 9 cwt, payload 1 t 12 cwt, driver and observer 5 cwt, gross as tested 6 t 4 cwt
3 qrs (cross-check C: 70 b.h.p. ÷ 0.561 b.h.p./cwt = 124.8 cwt; payload 27.4% of gross);
engine Perkins P6 six-cylinder oil, 86.9 × 127 mm (4,730 c.c.), 70 b.h.p. at 2,200 r.p.m.,
184 lb-ft at 1,000; Borg & Beck 12-in clutch, David Brown five-speed gearbox (8.14/4.73/2.79/
1.6/1; reverse 7.76; axle 7:1); brakes Clayton Dewandre servo and Lockheed hydraulic, Girling
two-leading-shoe, 16-in drums, total friction area 376.1 sq. ins. (60.5 per ton gross); fuel —
express service 16.7 m.p.g. at 24 m.p.h. (one stop per mile), stage service 11.1 m.p.g. at
15 m.p.h. (103.9 and 69.2 gross ton-m.p.g.); tank 30 gallons, range 330-500 miles; acceleration
0-20 in 14 s, 0-30 in 23.8 s, 10-30 in top gear 17.2 s; braking 20 m.p.h.→21 ft, 30 m.p.h.→
58 ft; turning circles 58 ft both locks; wheelbase 14 ft, overall length 24 ft 5½ in; maker
Seddon Motors Ltd., Oldham. **The panel carries no price** — the £1,250 is in the article text.

**Not found / dead ends**: no annual Buyers'-Guide-style price table for 1939-54 was located
(the 5 May 1939 issue is a goods-transport special; the 1 Oct 1948 Show review "After 11 Years
the Show Again" is descriptive with no model price table); the archive's site search is
JS-only; 1940-47 and 1949-52 price points remain empty (wartime price control 1940-45, then
sparse announcement coverage found so far). The Crellin Duplex 60-seater (CM 19 Mar 1948 p.36)
is relative only ("25 per cent. lower than the normal price of a double-decker seating an equal
number").

## 3. Route C — carriage and electric stock prices

### 3.1 Carriage prices 1935-48 (Grace's Guide) — partially worked

gracesguide.co.uk is **unreachable from this client**: PowerShell Invoke-WebRequest fails TLS
trust negotiation, curl.exe fails the connection (HTTP 000), the built-in webfetch gets a
transport error (all 2026-11-24). The **Wayback Machine serves individual Grace's pages**
(`http://web.archive.org/web/2025/https://gracesguide.co.uk/<page>`) and Exa site: search finds
the pages; that combination works.

One priced contract recovered (M, via Wayback copy of Grace's Guide "London, Midland and
Scottish Railway", sourced to *The Engineer* 3 Apr 1925): LMS placed "a contract with Hurst,
Nelson and Co., of Motherwell, for **seven five-coach trains, at a total cost of about £100,000**,
and another one with Pickering and Co., of Wishaw, for thirteen coaches" (unpriced) — **C:
≈ £2,857 a coach** (35 coaches). The Grace's LMS/LNER/SR/GWR pages carry no other priced coach
contracts 1935-48 in their text: the 1938 LNER Liverpool Street-Shenfield order (92 sets plus
8 for Manchester-Glossop; Birmingham RC&W and Metropolitan-Cammell builders) and 1939
"New Tyneside Stock" entries are named without prices. Grace's also indexes scanned *Commercial
Motor* page images (covers 1930, 1938, 1947, 1948 seen). Report 39 §2's named routes (TNA
AN 97/124, RAIL carriage works cost records) remain reading-room work and were not attempted.

### 3.2 1950s-60s EMU per-car prices (AEI booklet) — specifications only

Railways Archive docID 4082 = AEI *Descriptive List 1747-1, Edition A, September 1960*,
"High-Voltage Multiple-Unit Stock for British Railways — Four-car 25-kV. 50-cycle suburban
trains", a reprint (with photographs) of a *Railway Gazette* article of 3 June 1960
(https://www.railwaysarchive.co.uk/documents/AEI_HVMU_1960.pdf). Read in full: 35 four-car
trains (15 Manchester-Crewe, 20 Liverpool-Crewe) built at Wolverton Works, electrical
equipment British Thomson-Houston (AEI Traction Division). Leading particulars (M): overall
length of train 264 ft 6 in; vehicle length 63 ft 6 in; width 9 ft 3 in; seating 19 first +
294 second per set; maximum service speed 75 m.p.h.; **weights — motor car 53 t 12 cwt,
driving trailer 35 t 12 cwt, trailer (brake) 31 t 8 cwt, composite trailer 31 t 5 cwt**.
**No prices anywhere in the document** (technical description and equipment photographs only).
The 1950s-60s EMU per-car price gap is therefore unchanged by this route; the remaining routes
are BTC works-committee papers 1958-61 (TNA/NRM) and BTC/BRB annual accounts (report 39 §3).

### 3.3 Electric stock prices 1890-1910 (Electric Railway Journal) — holdings mapped, no prices in text greps

Archive.org holdings (M): *Street Railway Journal* vols 3-31 (1886-1908) as
`streetrailwayjo<N><YYYY>newy` (vols 10-31 present for 1894-1908), *Electric Railway Journal*
vols 32-38 (1908-11) as `electricrailway<N><YYYY>newy`, later volumes as `erj-<NN><c|p>`. Each
item has a text layer (`<id>_djvu.txt`) and page images. Text greps of vols 14 (1898), 23
(1904) and 25 (1905) find British items with aggregate money — Hull Corporation tramway
Siemens Bros. equipment tender **£42,228** (1898); Central London Railway construction and
equipment contract "slightly less than £3,250,000" (1898); Underground Railways Company of
London capital £5,000,000 (1904); Mersey Railway receipts +£8,000 a half-year (1904) — but
**no per-vehicle rolling-stock prices** in the text layer (greps for "per car / per coach /
rolling stock / electric locomotive" near money return US content only). Report 27's EF1 price
was read from page images; the same per-issue page-image pass over vols 14 and 22-27
(1898-1906) is the remaining route and is labour-intensive by the report-39 §6 method.

## 4. Route D — coke prices

### 4.1 Matthews Figure 11 — thesis obtained; figure digitised (2026-11-24/25)

The thesis is identified exactly (correcting report 39's "Hull PhD 1981"): **Matthews, Derek,
*The London Gasworks: A Technical, Commercial and Labour History to 1914*, PhD thesis,
University of Hull, submitted July 1981, awarded 1983**. Repository record:
https://hull-repository.worktribe.com/output/4214381 ; PDF:
https://hull-repository.worktribe.com/OutputFile/4214383 (40.07 MB). The repository's Cloudflare
managed challenge still blocks every automated fetcher (see §5), but the file was obtained by
manual download (user, 2026-11-24) and is held at `Research\content-hull_7030a.pdf` (532 PDF
pages: scanned page images with an OCR text layer). The text layer was used for navigation only;
 every figure below was read from the page images (report 39 §6 method), never from the OCR.

**The figure** (PDF page 227 of 532, printed p.181; the page is one scanned raster, 3529x2377
px): caption "Figure 11. Price of coke per chaldron (26 cwt.) and value of residuals per ton of
coal carbonised 1816-1914." Two polylines through near-annual points: **coke** solid, left axis
"Coke — Shillings per chaldron", ticks 10/20/30 (0 at the frame bottom); **residuals** dashed,
right axis "Residuals — Shillings per ton of coal", ticks 15/10/5 (0 at the frame bottom). The
frame is hand-drawn and not rectangular (the two axes tilt differently, ~1.4-1.9 degrees; the
bottom axis is horizontal to 0.2 degrees), and the year positions run across the frame width at
each height rather than vertically — see the mapping note below.

**The figure's own sources and notes** (transcribed from the page image): "Sources and notes:
1. Coke prices from scattered figures in company records 1816-1869; Field's Analysis 1869-1914.
2. Residuals from records of the Imperial 1828-1869; Field's Analysis for South Metropolitan
1869-1914."

**Surrounding prose** (printed pp.179-180, transcribed from the page images) — the source record
for the series' bases and the dated checks:

- p.179: "Per thousand foot of gas made, residuals earned 19.9d. in 1830, 10.5d in 1861 and
  only 7.7d in 1914. Per ton of coal carbonised, residuals made 202.6d in 1830, 82d in 1861 and
  109d in 1914." (thesis Tables 10 and 13, i.e. the same company records as the figure). Also:
  "residuals realised only 13 per cent of gas sales in 1830 but 20 per cent by 1861 and 28 per
  cent by 1914".
- pp.179-180: "Throughout the period coke was the most 'valuable' of the residuals ... it was 80
  per cent of the total value of residuals in the London gasworks in 1869 and still 71 per cent
  in 1914. As it was usually about half the value of coal the gas companies used 33 per cent of
  their own coke as the fuel in the furnaces." (footnotes: Field's Analysis (1869) p.2 and (1864)
  p.10; Hughes' Treatise (1853) p.107; S. Metro. SHM 30 Jan 1896.)
- p.180: "In both long and short-term, coke prices generally followed those of coal, as can be
  seen from a comparison between Figures 6 and 11. Coke prices, however, failed to rally in
  mid-century as did coal and continued a secular decline which hit bottom in the 1880s. In 1816,
  for example, coke sold in London for 28s a chaldron; by 1887 it had reached an all time low of
  4s 5d per chaldron. As with coal, the price of coke turned up after 1890 and reached perhaps
  19s 7d by 1913." (footnote 6: "See Figure 11.")
- p.180: in the early decades tar "never fetched more than 1½d per gallon", and "each ton of
  coal carbonised produced ten gallons of tar and thirty gallons of ammoniacal liquor" (JGL 10
  Apr 1849 p.46; 1 Apr 1856 p.181). Figure 12 (p.183) is the tar/ammoniacal-liquor counterpart
  ("Value of tar and ammoniacal liquor in pence per ton of coal carbonised for the Imperial Gas
  Company 1829-1871 and South Metropolitan 1869-1914"; sources as the two series above) — not
  digitised in this pass.

**Digitisation record** (M — read-from-figure measurement; every value below is an estimate
digitised from the page image): the page's embedded scan (JBIG2, 3529x2377) was decoded and
processed under `ai/temp/`. Value scales were fitted from the tick marks (left 30/20/10 at scan
y 584/1063/1539; right 15/10/5 at y 572.5/1057/1531; each linear, scale zero at the frame bottom
to within 0.1 s). The curves were traced through the ink column-by-column with continuity
tracking, the two spike regions and the 1913-14 ends were assembled from the individual dash
components, and the traces were re-drawn over the page image and checked visually at every
crossing. **Year mapping**: the plotted points track the frame width, not the printed decade
ticks (the tick grid is 0.5-2% narrower than the point grid: the 1816 point falls at the tick
grid's 1813.8, the 1887 trough at its 1886.6), so points were dated by
`year = 1810 + 104*(x - xL)/(xR - xL)` across the frame at the point's own height (xL, xR the
two axis lines). Four dated anchors in the thesis's own prose fix this mapping to ±0.3 y (the
checks below). **Precision**: values ±0.25 s/chaldron (±0.2 s/ton coke) and ±0.25 s/ton coal
(±3 d); the two spike apexes and the 1911-14 ends ±5-6 d; the year of each plotted point ±0.5 y
(±1 y where points crowd: 1828-30, 1907-14). One plotted point per year is given where a point
falls within 0.6 y of that year; years between plotted points are linearly interpolated (flag
`i`). The pre-1869 coke points are the caption's "scattered figures", so some years sit on long
straight runs between distant points; the post-1869 sections are near-annual (point spacing
≈ 24-25 px ≈ 1 y). The chaldron is 26 cwt per the caption, so s/ton coke = s/chaldron x 20/26.

**The series** (M, digitised; shillings; coke per chaldron of 26 cwt, residuals per ton of coal
carbonised) [LITERATURE:https://hull-repository.worktribe.com/output/4214381]:

Coke, s/chaldron (i = interpolated between plotted points):
`1816 28.2 · 1817 26.0i · 1818 22.1 · 1819 22.7i · 1820 23.6 · 1821 24.4 · 1822 26.0 · 1823 22.0 · 1824 22.1 · 1825 25.9 · 1826 22.5 · 1827 21.3i · 1828 21.1 · 1829 20.9 · 1830 18.1 · 1831 20.1 · 1832 18.6i · 1833 14.3 · 1834 12.2 · 1835 13.8 · 1836 18.9 · 1837 16.3 · 1838 19.1 · 1839 16.6 · 1840 14.4`
`1841 14.2 · 1842 15.2 · 1843 15.0 · 1844 16.1 · 1845 15.1 · 1846 15.1i · 1847 15.2 · 1848 16.0 · 1849 15.1i · 1850 12.9 · 1851 10.2 · 1852 11.1i · 1853 12.4i · 1854 13.2 · 1855 13.1 · 1856 11.5 · 1857 8.6 · 1858 9.1 · 1859 9.3 · 1860 9.1 · 1861 10.4 · 1862 10.5 · 1863 11.2i · 1864 11.6i · 1865 12.2 · 1866 10.7i · 1867 8.5 · 1868 7.9 · 1869 7.9 · 1870 8.5`
`1871 7.5 · 1872 10.3 · 1873 16.0 · 1874 10.8 · 1875 10.4 · 1876 9.4 · 1877 9.0 · 1878 7.7 · 1879 5.3 · 1880 5.0 · 1881 5.9 · 1882 5.4 · 1883 5.4i · 1884 5.4i · 1885 5.4 · 1886 5.0 · 1887 4.6 · 1888 9.8 · 1889 10.1 · 1890 17.5 · 1891 16.4i · 1892 14.9 · 1893 16.2 · 1894 16.3 · 1895 14.2i · 1896 11.4 · 1897 11.3 · 1898 14.7i · 1899 18.2i · 1900 22.4`
`1901 20.0i · 1902 16.6 · 1903 18.0 · 1904 16.9 · 1905 14.4 · 1906 14.9 · 1907 18.7 · 1908 19.0 · 1909 16.2 · 1910 17.8 · 1911 18.8 · 1912 20.4 · 1913 19.9 · 1914 16.6`

Residuals, d/ton of coal carbonised (i = interpolated between plotted points):
`1828 139 · 1829 182 · 1830 201 · 1831 134 · 1832 130 · 1833 102 · 1834 113 · 1835 130 · 1836 134i · 1837 140 · 1838 158 · 1839 153 · 1840 158 · 1841 163 · 1842 163 · 1843 138 · 1844 134 · 1845 138 · 1846 114 · 1847 112 · 1848 98 · 1849 91 · 1850 112 · 1851 87 · 1852 81 · 1853 84 · 1854 108 · 1855 97 · 1856 80`
`1857 59 · 1858 73 · 1859 67 · 1860 79 · 1861 82 · 1862 82 · 1863 75 · 1864 81 · 1865 84 · 1866 79 · 1867 78i · 1868 77 · 1869 72 · 1870 79i · 1871 101 · 1872 125 · 1873 197 · 1874 141 · 1875 137 · 1876 132 · 1877 116 · 1878 116i · 1879 115 · 1880 108 · 1881 124 · 1882 125 · 1883 113 · 1884 102i · 1885 91 · 1886 86 · 1887 80 · 1888 93 · 1889 98 · 1890 112`
`1891 98 · 1892 95 · 1893 101i · 1894 110 · 1895 88 · 1896 78 · 1897 72 · 1898 80 · 1899 109i · 1900 133 · 1901 120 · 1902 98 · 1903 111 · 1904 106 · 1905 97 · 1906 99 · 1907 102 · 1908 114 · 1909 99 · 1910 108 · 1911 128 · 1912 136 · 1913 142 · 1914 115`

Notes on the crowded end stretches: the coke's 1909-12 points sit at 0.8-1.0 y mapped spacing
with one small drawing-wobble level (17.1 s at mapped 1909.7) not treated as a data point; the
residuals' 1911-14 points crowd at mapped 1911.3-1914.0 and the four levels 128/136/142/115 d
are assigned to 1911/1912/1913/1914 (year labels ±0.6 y; the 1913 level is the plotted peak).

**Internal checks** — the digitised figure against the thesis's own dated statements:

1. Coke 1816: 28.2 s/chaldron vs "28s a chaldron" (p.180) — agrees within ±0.2.
2. Coke trough: digitised minimum 4.56 s at mapped 1887.0 vs "4s 5d per chaldron" (4.42) "by
   1887" — agrees within ±0.2 s.
3. Coke 1913: 19.9 s vs "perhaps 19s 7d by 1913" (19.58) — agrees within the prose's own hedge;
   the plotted maximum 20.4 s falls at 1912.
4. Residuals 1830: 200.8 d/ton at the spike apex vs "202.6d in 1830" (p.179) — agrees within
   ±3 d.
5. Residuals 1861: 81.6 d vs "82d in 1861" — agrees within ±3 d.
6. Residuals 1914: 114.7 d vs "109d in 1914" — within the ±6 d end precision (the digitised end
   is where the dashed line meets the tilted frame edge).
7. The 1873 spike (residuals 197 d; coke 16.0 s/chaldron) matches the 1871-73 boom the prose
   dates ("Tar prices rose from 1d a gallon in 1869 to 3½d in 1873. In the same year, sulphate
   of ammonia peaked at ... £19 15s a ton", p.184).
8. Shape statements (p.180) all appear as described: the secular decline into the 1880s, the
   post-1890 turn, and the 1899-1900 surge.

**The Gas Journal figures of §4.2 do not reconcile on units — open.** At the caption's basis the
coke series' 1900 value 22.4 s/chaldron = 17.2 s/ton coke = £0.86/ton: about 1.9x the 8s 10.55d/
ton (£0.44) 1900 company realisation of §4.2, and 0.78x the 22s/ton London contract minimum for
1901 (1.02x if the JGL's "22s." in that passage is per chaldron — the unit as recorded is
uncertain). §4.2's own two JGL figures already differ 2.5x (contract minimum vs bulk
realisation), so a contract-vs-realisation gap may explain part of it; the unnamed JGL company
may not be London. [UNVERIFIED] the figure's coke series is most likely a London
wholesale/contract level in the caption's chaldrons, not a company average realisation per ton;
the basis reconciliation with §4.2 is unresolved.

**What remains open from this figure**: the coke-basis reconciliation with §4.2 (above); Figure
12 (tar and ammoniacal liquor per ton of coal, 1829-1914) not digitised (the same method
applies, p.183); the individual pre-1869 coke points cannot be dated below ±0.5-1 y from the
figure alone (the caption's "scattered figures"); and the series ends at 1914 (the frame edge) —
the thesis contains no post-1914 extension, so route D(ii) (the BPP returns) remains the
post-1914 route.

### 4.2 BPP Gas Undertakings returns 1882-1935 — new working route via the Gas Journal

The returns themselves are not web-accessible here: archive.org's catalogue holds only the 1907
Census of Production Part IX (already mined in report 39); HathiTrust is blocked (settled);
the Google Books API rate-limited this run (429). Hansard confirms the series and supplies the
parliamentary paper numbers (M): returns for year ended 31 Dec 1888 [No. 97] and year ended
25 Mar 1882 [No. 98] ordered 2 Apr 1889; 1898 return [No. 364] presented 8 Aug 1898; 1914-15
returns continuing Nos. 311/312 ordered 28 Jul 1915.

**New working route (verified)**: the *Journal of Gas Lighting* (later *Gas Journal*) weekly run
is on archive.org as SIM items `sim_gas-journal_<YYYY-MM-DD>_<vol>_<iss>` (complete 1856-1945+,
e.g. vol 78 (1901) = `sim_gas-journal_1901-07-02_78_1990` …); each issue's OCR text downloads as
`https://archive.org/download/<id>/<id>_djvu.txt` and greps cleanly once whitespace is
normalised. Sample figures read from the 1901 volume (all OCR-READ; page images not yet
verified):

- London gas companies' coke contracts for 1901: "the minimum price fixed being 22s." per ton
  (JGL 30 Jul 1901, iss 1994) — gas coke, contract basis (M).
- A large gas company (unnamed in the passage as read): coke sold 219,100 tons in 1900 at an
  average 8s 10.55d per ton, against 6s 0.93d in 1899 (JGL 24 Sep 1901, iss 2002) — company
  report realisation, gas coke (M).
- Coke realisation "5s. 1d. per ton in excess of that obtained in the year 1899" (company
  report, JGL 23 Jul 1901, iss 1993) — the 1900 rise against 1899 again.
- Best Lancashire foundry coke 24s-25s per ton at the ovens (JGL 13 and 27 Aug 1901) —
  foundry (metallurgical) grade, not gas coke.
- Best Durham coke for export 17s 6d-18s 6d per ton f.o.b. (JGL 3 Sep and 24 Sep 1901) —
  export/metallurgical grade.

The returns' internal structure is confirmed in JGL correspondence ("Gas Undertakings (Local
Authorities) Government Returns, p. 41, column 17"; columns 17 and 20 introduced in 1897), so
per-undertaking coke tonnages and values exist in the returns as claimed. The JGL's own annual
analysis article of the returns was **not** located in the Jul-Dec 1901 window searched; a
year-by-year pass (return year Y discussed mid-Y+1) over the `_djvu.txt` files is the open
route to the 1882-1935 national gas-coke price series.

## 5. Dead ends (do not repeat)

- railcar.co.uk PDFs: not dead; browser header + Referer retrieves them (report 40 §1.9
  confirmed again). No labour-hour or cost figures exist in BR 87264/1, BR 12013/12014 or the
  Watford responsibility paper.
- archive.commercialmotor.com `/search?term=` is JavaScript-only (empty to PowerShell and
  webfetch); use Exa site: searches plus `/issues?year=` browsing. The 1 Oct 1948 Show review
  has no price table.
- gracesguide.co.uk direct access fails at TLS/transport for PowerShell, curl and webfetch
  (2026-11-24); Wayback per-page copies work; Special:Search is not archived.
- hull-repository.worktribe.com Cloudflare managed challenge blocks all fetchers tried, including
  r.jina.ai; no Wayback, no CORE, no EThOS-hosted copy of the Matthews thesis. RESOLVED
  OTHERWISE (2026-11-24): the user downloaded the PDF manually; it is at
  `Research\content-hull_7030a.pdf` and Figure 11 is digitised in §4.1. Automated fetching stays
  blocked for any further Hull items.
- archive.org catalogue has no BPP Gas Undertakings returns; Google Books API returned 429
  (retry later); HathiTrust stays blocked (report 39).
- ERJ/SRJ text layers carry British tramway and construction contract money but no
  per-vehicle railway stock prices in vols 14/23/25 greps; page-image reading is required.
- Wayback availability API shows no snapshot of hull-repository.worktribe.com output pages.

## 6. What remains open

1. **1940-47 and 1949-52 bus/coach prices** (route B): announcement articles only so far; more
   Exa site: passes over archive.commercialmotor.com will find individual priced items; any
   annual price table 1939-54 is yet to be located (if one exists).
2. **Road-test specification panels 1939-54** (route B): method proven with panel No. 354;
   each further panel is one fetch-and-read cycle of the `fullImages` scan pages.
3. **Grace's Guide carriage contract notices 1935-48** (route C(i)): Wayback + Exa route works
   but needs page-by-page navigation; TNA AN 97/124 and RAIL works cost records are
   reading-room work.
4. **1950s-60s EMU per-car prices** (route C(ii)): AEI booklet gives specifications only;
   BTC works-committee papers 1958-61 (TNA/NRM) and BTC/BRB annual accounts remain.
5. **Electric stock prices 1890-1910** (route C(iii)): per-issue page-image pass over SRJ/ERJ
   vols 14, 22-27 (1898-1906) and 32-35 (1908-11).
6. **Matthews Fig 11** (route D(i)): DONE — figure digitised in §4.1 (both series 1816-1914,
   annual values; checks pass against the thesis's own dated statements). Open from it: the
   coke-basis reconciliation with the §4.2 Gas Journal tonnage figures (about 2:1), Figure 12
   (tar and ammoniacal liquor) not digitised, and the pre-1869 coke points dated only ±0.5-1 y.
7. **BPP Gas Undertakings returns 1882-1935** (route D(ii)): the JGL year-by-year analysis pass
   (method verified) or paper/HathiTrust copies of the returns themselves.
