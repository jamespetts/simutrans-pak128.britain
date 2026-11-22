# Aircraft purchase prices: fourth research pass

**Status**: draft research report for the cost-balancing project. Not a knowledge-base document and
not reviewed. Companion data: `ai/temp/research-pricing-rows-4.csv` (124 rows, domain `aircraft`,
kind `capital`). Draft evidence note: `ai/temp/aircraft-price-sources-flight.md`.

---

## 1. Starting point

`New/ai/vehicle-cost-evidence.md` records aircraft as the weakest class: one forum figure and eight
published figures, "none with a full specification", and says aircraft "need a procurement-price
source of their own". `ai/temp/individual-price-rows.csv` held nine aircraft capital rows, all
1933-1963, of which only four were British new-build prices.

The pakset has 107 air `.dat` files (230 objects once mail and cargo variants are counted). The type
list runs from the Handley Page O/400 and Junkers F 13 to the 737 MAX, with the densest coverage in
1945-1990.

This pass set out to test routes the earlier passes had not used. Three worked. One of them — the
Flight "Commercial Aircraft of the World" survey — is a price table that the earlier pass walked past
because it looked at "Civil Aircraft of the World" instead.

## 2. What worked, in order of yield

### 2.1 Flight International, "Commercial Aircraft of the World" (1959, 1960, 1961)

The annual survey prints, for every current type, a **basic price** line and often a price history.
The 20 November 1959 issue alone yielded 77 money-and-price sentences. The survey issue is
identifiable by a high density of the strings "basic price", "price paid by" and "market price".

* 1959: `sim_flight-international_1959-11-20_76_2645`
* 1960: `sim_flight-international_1960-11-18_78_2697`
* 1961: `sim_flight-international_1961-11-23_80`

Each is a public `_djvu.txt` on the Internet Archive. Method: download the November/December issues,
score them on those marker strings, take the highest-scoring issue, split into sentences, and keep
every sentence containing both a currency amount and a price word, with 300 characters of leading
context (which carries the type name) and the following "Powerplant/Weights/Accommodation" fields
(which carry the specification).

The survey lives in the `sim_` microfilm run, which **stops at 1961**. This is the binding
constraint on the route: it gives 1945-1961 prices and nothing later.

### 2.2 Flight International, "Airliner price index" (10 August 1972, p.183)

A single page tabulating **new equipped price and used market indication in US dollars** for every
airliner then on the market, with a remark column ("new deliveries", "production terminated",
"prices hardening now production virtually closed"). It is a systematic, dated, single-source table:
26 new-aircraft prices in 1972 dollars, from the Skyvan at $650,000 to Concorde at $33.8m.

The FlightGlobal PDF archive is dead (404), but the viewer page is in the Wayback Machine and the
underlying PDF was archived with it:

* viewer: `https://web.archive.org/web/20121108041948/http://www.flightglobal.com/pdfarchive/view/1972/1972%20-%202020.html`
* PDF: `http://www.flightglobal.com/FlightPDFArchive/1972/1972 - 2020.PDF` (1.5 MB, one page, with a
  text layer and an embedded JPEG)

The text layer's column order is scrambled, so the table was read from the page image. This is the
only place in the whole pass where an image had to be read rather than text, and it is worth it: the
table is the best single document found.

### 2.3 Wayback recovery of Wikipedia's removed `unit cost` infobox field

As instructed. `https://archive.org/wayback/available?url=en.wikipedia.org/wiki/<Page>&timestamp=YYYYMMDD`
returned the closest snapshot; the infobox row was matched in the HTML; the citation beside it was
pulled from the same page when present. Where the HTML had no row, the MediaWiki API was used to
fetch an old revision (`prop=revisions&rvstart=...`) and a raw wikitext fetch (`oldid=...&action=raw`),
then a line-anchored match on `|unit cost =` accepting only values containing a digit.

Two mechanical notes for anyone repeating this:

* The availability API returns **nothing** if the URL argument is fully percent-encoded. Pass
  `en.wikipedia.org/wiki/Vickers_VC10` with underscores and only spaces encoded.
* Several articles carry `|unit cost =` **empty**, and a naive `\|\s*unit cost\s*=` regex will then
  capture the *next* parameter. Anchor the match to the line and require a digit.

**Yield and citation quality.** 40 values were recovered. 12 of the 124 rows in the CSV are marked
UNVERIFIED because the infobox carried no citation or named only a book page that could not be
reached (Bowers 1989 p.434; Velupillai 1981 p.1243; Fricker 1968 p.77). The 1972-index citations all
resolved to the same document, which was then fetched directly — that is the strongest chain in the
pass and the reason §2.2 exists.

## 3. What the prices look like

### 3.1 By era (rows in the CSV)

| Era | Rows | Examples |
|---|---|---|
| 1918-1939 | 3 | HP O/400 £6,000; Boeing 307 $315,000; DC-3 £18-23,000 |
| 1940-1959 | 51 | DC-4 £140-160k; Constellation £170k; Viscount £235k; Vanguard £1.0m; Britannia £768k; Comet 1 £275k |
| 1960-1969 | 15 | One-Eleven £835k; VC10 £2.2m; Trident £1.167m; 747-100 $24m; 727 $4.25m; 737-100 $3.6m |
| 1970-1979 | 29 | the 1972 index (26 rows) plus Cessna 310 $147,750, 747-200 $39m |
| 1980-1999 | 5 | BAe 146-200 £11m; 747-300 $83m; A340-200 $87m; ERJ-145 $15m; HS.125 $12.995m |
| 2000-2012 | 13 | 757 $65-80m; 737NG $50-85m; A320 family $56-91m; A330 $200-222m; ATR 42/72 |
| undated in source | 8 | Fokker 50, Do 228/328, Dash 8 Q200/300/400, King Air C90GTi |

### 3.2 British types now priced

Viscount (1953 list, 1955 BEA contract, 1958 700D, 1961 800), Vanguard (1955 BEA, 1957 TCA),
Britannia (1955 BOAC, 1957 range, 1959 312), Comet 1/4/4B/4C, Trident 1 and 3B, One-Eleven 200/475/500,
VC10 and Super VC10 (1961 list and 1957 BOAC contract), HS.748 (1959, 1960, 1972), Herald,
Argosy, HS.125 (-1 1962, -600 1972, 1995), Dove, Heron, Twin Pioneer, Islander, Skyvan, BAe 146-200,
Concorde (1972 launch quote and 1977 figure).

Still unpriced: **Bristol 170 Freighter, Ambassador (new), Hastings, York, Tudor, Lancastrian,
Belfast, Jetstream 31/41, ATP, Shorts 330/360, Viscount 810 new**. None of the three routes carried a
price for these; see §5.

### 3.3 The ladder that matters for calibration

Because the 1959-61 surveys print *price histories*, a single 1959 document gives a time series for
the same type: DC-6 £210-230k (1946) → £310k (1951); DC-7B £680k (1955) → £820k (1957); DC-7C £800k
(1956) → £930k (1958); DC-6B £400k (1951) → £500k (1958); Electra £818k (1959) → £928k (1961). That
is matched-model inflation for aircraft in the same decade, which the class ladder otherwise lacks.

## 4. Basis and comparability

Every row records the basis in `notes`. Four bases are present and **must not be mixed without
comment**:

1. **Manufacturer basic/list price, new, fully equipped** — the bulk. Flight's "basic price" excludes
   radio and seats unless it says otherwise; the 1972 index is explicitly "fully equipped".
2. **Contract or order price** — BEA/TCA/BOAC orders. Several are quoted **with spares**, which
   inflates them: BEA's Viscounts at "approximately £1m each" with spares against a £400,000 basic
   price for a 700D is the clearest example. Rows derived by dividing an order total are labelled
   "=£X each" and the divisor is given.
3. **Second-hand** — Ambassador £69,500, Viking £20,000, and the whole 1972 "market indication"
   column (not carried into the CSV except where a new price was absent).
4. **Launch/breakeven assumptions** — Concorde's $33.8m in 1972 is "price for first deliveries 1975",
   a forward quote, not a transaction.

No conversion or deflation has been applied. GBP and USD rows are kept apart (62 each).

## 5. Dead ends, recorded so they are not retried

| Route | Result |
|---|---|
| **Jane's All the World's Aircraft** | Definitive: **Jane's does not print aircraft prices**. The 1947 volume (Internet Archive `in.ernet.dli.2015.278957`, full text) contains 38 pound signs, all in advertisements and airfield/airline notes, and 25 uses of "price", all subscriptions. The 1977-78 volume (`janes-all-the-worlds-aircraft-1977-78`, 7.6 MB text) has 24 pound signs and 25 "price" mentions, all editorial or contract news. Most other volumes (1953-54 to 1991-92) exist on the Internet Archive but are lending-only: their `_djvu.txt` returns a 172-byte error and the `fulltext/inside.php` search endpoint returns "Item not available". |
| Internet Archive global full-text search | `ia-fts.archive.org` does not resolve from this machine. |
| Google Books API | `429 RESOURCE_EXHAUSTED`: the API key's daily quota is 0. |
| `hansard.millbanksystems.com` | HTTP 522 (server down). `hansard.parliament.uk/search` sits behind a Cloudflare challenge. `api.parliament.uk/historic-hansard/sittings/YYYY/mmm/dd` **does** work for direct page fetches, but there is no usable full-text search, so it can only confirm a page whose date is already known. |
| FlightGlobal PDF archive (live) | 404. Only reachable through Wayback, and only if the exact viewer URL is known. |
| `sim_flight-international` after 1961 | Zero issues. The run is 1909-1961 (2,846 issues). `sim_aviation-week` covers 1916-1961 plus 1984-85; `sim_american-aviation` 1937-1961; `sim_aeroplane` 1958-1961 only. |
| Wikipedia live `unit cost` | Still absent; the prose yields only a handful (737-100/200, 767 list price). |
| Wikipedia `insource:"Airliner price index"` | 11 articles, all pointing at the same 1972 page. No other year of the index was found, and the Flight year-index pages do not expose page titles to a script. |

**Open question**: the 1972 page is headed "MAINLINER / Airliner price index", which suggests a
recurring feature. If the same page exists in 1973-1985 it would close most of the remaining
1970s-80s gap, but the Wayback capture has to be found by exact viewer URL and the archive's own
search is gone.

## 6. Coverage before and after

| | Before | After |
|---|---|---|
| Aircraft capital rows | 9 | 124 |
| With a stated specification | 0 | ~55 (engines, weights or seats from the same survey entry) |
| British new-build types priced | 4 | 16 types (28 variant rows) |
| Years represented | 1933-1963 | 1918-2012, with 66 rows in 1945-1979 |

The gap is no longer "no aircraft prices". It is now **specific**: the 1962-1971 block (which the
1961 survey just misses and the 1972 index just post-dates), the 1973-2000 block outside the
surviving Wikipedia list prices, and the handful of British types listed in §3.2.

## 7. Proposed knowledge-base update

Propose adding to `New/ai/vehicle-cost/` a new child doc, **`aircraft-purchase-prices.md`**, keyed
from `vehicle-cost-evidence.md` under the existing "Ships and aircraft" heading, carrying:

* the three source families and their exact locators (the `sim_` identifiers and the Wayback PDF URL);
* the basis taxonomy of §4, with the "with spares" warning;
* the price ladder by type and year, as a table mirroring the CSV;
* the finding that Jane's carries no prices, so future passes do not spend time on it;
* the open question about other years of the Airliner price index.

`vehicle-cost-evidence.md` should then change from "Aircraft are the weakest class ... should not be
calibrated from this evidence" to a pointer at the new doc, with the residual gaps named. That is a
claim about the evidence, so it needs the user's review before commit, per the documentation rule.

## 8. What remains unmeasured

1. 1962-1971: no systematic table found. Individual contract prices exist in Hansard (Britannia,
   Trident, One-Eleven, Concorde launch aid) but the search route is broken; direct page fetches
   would work if the sitting dates were known.
2. 1973-1999 outside the Wikipedia list prices: the 1972 index is a single snapshot.
3. The small British types in §3.2, which appear to have had no published list price at all
   (Bristol 170, Ambassador, Hastings, York, Tudor, Lancastrian, Belfast).
4. Anything before 1918 and the Junkers/Fokker prewar types.
5. Second-hand values are present but sparse; the 1972 index's used column is the only systematic
   set and was deliberately not loaded except where no new price exists.

---

# Addendum (second working pass): basic prices and wider type coverage

**Rows**: `ai/temp/research-pricing-rows-4b.csv` (38 rows). `research-pricing-rows-4.csv` is not
edited, so the first pass stays auditable. Where 4b supersedes a 4 row, the 4b `notes` say so.

## A1. The basic-price rule applied

Capital covers the bare aircraft. Spares, crew training and support are maintenance. The first pass
had recorded several order values as if they were prices, because the source words them as "per
aircraft". They are now split:

| Type | rows-4 figure | What it actually was | 4b treatment |
|---|---|---|---|
| Britannia 312 | £1,070,000 | **mis-attributed**: the 1961 survey prints "Basic price new was £1.07m" in the **320** entry, not the 312 | 4b records **Britannia 320, £1,070,000, basic**. The 312 has no basic price in the survey |
| Britannia 102 | £768,000 | "Price paid by BOAC (fixed in April 1955) was £768,000 per aircraft" — nothing says spares are excluded | kept at £768,000 but **UNVERIFIED**: the spares share is not separable |
| Vanguard | £1,000,000 (BEA) and £1,195,000 (TCA) | BEA paid "approximately £1m each" **with spares**; TCA's £23.9m was for "20 aircraft **and parts**" | **no price**; both figures moved into `notes`; UNVERIFIED |
| Trident 1 | £1,166,667 | "Value of the BEA contract is £28m **with spares**" for 24 aircraft | kept, but labelled **contract with spares, UNVERIFIED** |
| Comet 4B | £1,166,667 | BEA's six "valued at about £7m **with spares**" | kept, labelled **contract with spares, UNVERIFIED** |
| Comet 4C | £1,666,667 | Mexicana's three "worth £5m **with spares and equipment**" | kept, labelled **contract with spares, UNVERIFIED** |
| VC10 (BOAC) | £1,714,286 | "£60m for 35 aircraft **less spares**" — spares are explicitly outside | **retained as a price**, basis stated as contract excluding spares |
| Viscount 700 (BEA) | £1,000,000 | "approximately £1 million each" **with spares** | **row withdrawn** (no price); the basic 700 (£235,000, 1953) and 700D (£400,000, 1958) rows in 4 stand |

Net effect: two rows lose their price (Vanguard, Viscount BEA), five keep their figure but carry an
explicit UNVERIFIED caveat, one is corrected to a different mark (Britannia 320), and one is
confirmed as a genuine aircraft-only contract price (VC10).

The lesson for future passes: *Flight* prints "basic price" when it means the bare aircraft, and
"price paid by", "contract value" or "worth" when it means an order, usually with spares. Only the
first is a capital price.

## A2. New coverage

**British**: Short Belfast SC.5/31 civil, £1.6-1.7m (1961), the only new British airframe price
recovered — 4 x Tyne RTy.31, MTOW 300,000 lb, 255 seats, 100,000 lb payload. Plus BAe ATP/Jetstream
61 $13.25m (1995), Jetstream 31 Super $4.5m (1996), Jetstream 41 $6.85m (1998).

**European**: Airbus A310 $88m (2004), A330-200 $229.0m (2015), A340-300 $238.0m (2011),
A350-900 $240.6m and A350-1000 $269.6m (2015), A380-800 $317.2-337.5m; Fokker 50 $13.2-14.0m (1998),
Fokker 100 $25-30m and Fokker 70 $20-25m (1997); Saab 340BPlus $9.7m and Saab 2000 $14.5m (1999).

**US**: Boeing 777-200ER $261.5m, 787-8 $224.6m (2015), 747-400 $230m (2006), 737 MAX 8 $95.2m and
MAX 9 $101.7m; MD-11 $132.0-147.5m (1999), MD-80 $42-49m and MD-90 $49-56.5m (1999); Embraer
EMB-120 $7.5m (2000), E170 $28.5m, E195 $47.0m; Bombardier CRJ700/900/1000 at $24.39m/$38.93m/
$46.37m (2014) and CRJ100/200 $24-39.7m (2006).

**Freighter and combi variants.** No new separately quoted freighter price was found in this pass.
The only split pair remains the 1972 index's Boeing 707-320B ($10.0m) against 707-320C ($10.5m),
already in rows-4; the index quotes one price per model and does not otherwise distinguish cargo
variants.

## A3. New source family: Forecast International archived forecasts

The most useful addition after Flight. Forecast International's discontinued *Civil Aircraft
Forecast* reports are still served as PDFs from
`https://www.forecastinternational.com/archive/disp_old_pdf.cfm?ARC_ID=<n>`, and every report opens
with a "Price Range" line that states the currency year, for example:

* ARC_ID 304 — BAe ATP/Jetstream 61: "approximately $13.25 million fully equipped (1995 US constant
  dollars)"
* ARC_ID 337 — Fokker 70/100: "Fokker 100, $25-$30 million; Fokker 70, $20-$25 million; both in 1997
  US dollars"
* ARC_ID 316 — MD-11: "$132.0-$147.5 million in 1999 US dollars"

Mechanics. The server returns 200 with an empty body unless a **Referer** header is sent; with
`Referer: https://www.forecastinternational.com/` the PDF downloads normally. The reports also
carry a "Technical Data" block with dimensions, weights and powerplant, which supplies part of the
specification column for these rows.

Coverage of the archive is partial: the civil-aircraft reports identified run from ARC_ID 291 to
361, roughly 40 reports, and do not include ATR, Dash 8, Shorts 330/360, the BAe 146/RJ family, the
A300/A330/A340 or the Boeing 737/747/777. A scrape of 420-600 found only defence and electro-optical
reports, so the civil set really is that small.

## A4. Specification

Every 4b row carries seats, engines/power, MTOW or range, and the basis, in `notes`, to the extent
the retrieved source states them. Rows where the specification could not be retrieved say so:
A330-200, A340-300, A350-1000, 777-200ER (partly), A380, 787-8 (capacity only), E170/E195, and the
older A310 entry, whose report gives seating and range but not powerplant. This is deliberate: the
project rule is that priors are not evidence, so a figure that could not be read in a source is not
written.

## A5. Dead ends added in this pass

| Route | Result |
|---|---|
| Wayback `unit cost` for Jetstream 31/41, ATP, Shorts 330/360, Saab 340/2000, Fokker 70/100, Herald, HS.748 | The field is not present in any snapshot 2008-2022. These articles never carried it. |
| `ageconsearch.umn.edu` (Hunsaker 1982, 30-60 seat commuter market, DOI 10.22004/ag.econ.311536) | HTTP 202 with an empty body; the PDF carrying 1981 price estimates for the SD-330, SD-360, ATR 42, Dash 8, EMB-120 and Saab 340 could not be retrieved, so those figures were not used. Worth retrying from a browser session. |
| Forecast International PDF without a Referer header | Empty 200 response. With the header it works. |
| Forecast International ARC_ID 420-600 | Defence and electro-optical forecasts only, no civil aircraft. |
| Wikipedia specification sections for A300/A330/A340/A380/777/787 | The plain-text extract collapses the specification templates into navigation boxes; the wikitext `Aircraft specs` parameters were not retrievable before the API rate-limited. |

## A6. What is still unmeasured after 4b

1. **Bristol 170, Ambassador, Hastings, York, Tudor, Lancastrian, Hermes** — the 1959-61 surveys
   either omit them or carry no price line. They are the last British types in the pakset with no
   capital figure at all.
2. **Shorts 330/360, ATR 42/72 new prices, Dash 8 new prices, BAe 146/RJ family, A300/A330/A340
   outside the Airbus list years, 757/767 launch-era prices, 727/737-200 outside 1972.**
3. **1962-1971** remains the largest hole: the surveys stop in 1961 and the price index starts in
   1972.
4. Year-of-price is missing for six rows (A380, 777-200ER, 737 MAX 8/9, E170, E195) because the
   archived infobox field does not state one; they are marked UNVERIFIED for year.
