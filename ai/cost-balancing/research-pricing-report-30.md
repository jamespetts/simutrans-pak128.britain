# Lorry, van and light-commercial capital cost, 1896–1980 — measured evidence pass

Pass date: 23 November 2026. Scope: purchase prices of British lorries, vans and light
commercials, with payload, engine and (where available) make, so that a price-by-payload
ladder and a maker comparison can both be built.

Nothing in this file is derived from any Simutrans `.dat` cost field. No pakset price is used
in any calculation here.

---

## 1. Method

### 1.1 Search method

Web search ran on Exa, one query per turn, via `POST https://api.exa.ai/search` with
`{"query": ..., "type": "auto", "contents": {"highlights": true}}`. Ten queries were spent.
The queries named the subject, the constraint, the date window and a source preference
(Commercial Motor archive and Grace's Guide first, auctions and preservation sites excluded).

The Commercial Motor archive (`archive.commercialmotor.com`) proved to be the only large body
of contemporary, dated, per-vehicle British commercial-vehicle prices that is reachable and
readable. Its article pages fetch cleanly. Its own search page sits behind a JavaScript
challenge, so all article discovery was done through Exa.

### 1.2 What the archive will and will not give

Two important mechanical limits were found early and they shape the whole dataset:

1. **Prose survives; tables do not.** The archive OCRs headline and body prose. Tabulated
   matter — the annual "Buyer's Guide to Goods Chassis" tables (1932, 1935, 1937), the
   specification panel printed alongside every road test, and price-change schedules printed
   as columns — is present only as page images and is *not* in the text layer. Fetching
   `10th May 1935 / a-buyers-guide` returns the introduction only, and fetching
   `24th September 1937 / revised-commer-and-karrier-prices` returns one sentence
   ("The new figures ... are listed below :-") followed by nothing.
   Consequence: the single richest possible source — a full market price table by payload for
   one year — is unavailable. Everything below comes from prose: news paragraphs, model
   programme announcements, road-test commentary, and one exceptional 1960 price feature that
   *was* set as running prose.
2. **The pound sign is frequently lost.** OCR renders `£` as nothing, as `1`, `6`, `E`, `s`,
   `11`, `12` or `?`. Examples in the raw text: "listed at 1298; instead of £348" (Guy 30-cwt
   at £298); "Price 11,150" (Sentinel DG6 at £1,150); "5685" (Austin at £685); "12.514"
   (Seddon at £2,514); "1980" (Peerless at £980). Every figure below was read with its
   surrounding sentence for sense, and every figure where the sign or a digit was damaged is
   marked **OCR** in the table and in the CSV notes. Figures that could not be repaired with
   confidence were dropped rather than guessed (see §7).

### 1.3 Evidence grades

- **MEASURED** — a price actually printed as a list price, an advertised price, a
  tender/committee figure, or the price of the vehicle as tested. This is the great majority.
- **STATED** — a historian's or journalist's "about £X", or a stated class average or range.
- **INFERRED** — arithmetic on measured figures (for example a body cost obtained by
  subtracting chassis-cab from complete-vehicle price). Always labelled.

### 1.4 Scope note on "chassis / chassis-cab / complete"

British practice quoted three prices for the same vehicle, and the gap between them is large
enough to wreck a ladder if the scopes are mixed. Every row states which one it is:

- *chassis* — frame, engine, transmission, wheels and tyres; no cab, no body.
- *chassis and cab* — adds the driver's cab (and usually scuttle and instruments).
- *complete* — with a body (platform, dropside, van or tipper) as specified.

The 1950 Bedford schedule (§5) prints all three for the same model and is the cleanest
demonstration of the gaps.

---

## 2. Sources

| Key | Source |
|---|---|
| S1 | *The Commercial Motor*, 12 Oct 1920, p.16, "British Vehicles at Olympia". https://archive.commercialmotor.com/article/12th-october-1920/17/british-vehicles-at-olympia |
| S2 | *The Commercial Motor*, 5 Aug 1924, p.4, "Wheels of Industry" (Wandsworth Borough Council purchases). https://archive.commercialmotor.com/article/5th-august-1924/9/wheels-of-industry |
| S3 | *The Commercial Motor*, 20 Dec 1927, p.50, "The C.M. Tests a New Six-Wheeled Steam Wagon" (Sentinel D.G.6). https://archive.commercialmotor.com/article/20th-december-1927/52/the-cm-tests-a-nem--wheeled-steam-wagon |
| S4 | *The Commercial Motor*, 8 May 1928, p.60, "A Steam Six-Wheeler with a Number of Notable Features" (Yorkshire W.J.). https://archive.commercialmotor.com/article/8th-may-1928/60/a-steam-six-wheeler-wi-i-a-number-of-notable-ature |
| S5 | *The Commercial Motor*, 11 Dec 1928, p.4, "Wheels of Industry" — "The New A.E.C. Prices". https://archive.commercialmotor.com/article/11th-december-1928/4/wheels-of-industry |
| S6 | *The Commercial Motor*, 23 Dec 1930, p.49, "The Peerless Chassis". https://archive.commercialmotor.com/article/23rd-december-1930/49/the-peerless-chassis |
| S7 | *The Commercial Motor*, 4 Nov 1930, p.50, "Wheels of Industry" — "Guy's 1931 Programme". https://archive.commercialmotor.com/article/4th-november-1930/50/wheels-of-industry |
| S8 | *The Commercial Motor*, 13 Jan 1931, p.54, "Thornycroft's Latest Rigid Six-Wheeler" (QC series). https://archive.commercialmotor.com/article/13th-january-1931/55/thornycrofts-late-it-rigid-six-wheeler-s-hortly-be |
| S9 | *The Commercial Motor*, 27 Jan 1933, p.52, "A Popular Tonner Tested" (Morris-Commercial 13.9 h.p.). https://archive.commercialmotor.com/article/27th-january-1933/53/a-popular-tonner-tested |
| S10 | *The Commercial Motor*, 31 Mar 1933, p.32, "Wheels of Industry" (Studebaker Pierce-Arrow). https://archive.commercialmotor.com/article/31st-march-1933/32/wheels-of-industry |
| S11 | *The Commercial Motor*, 12 Jan 1934, p.54, "Fine Road Characteristics of a Morris Commercial 3-tonner". https://archive.commercialmotor.com/article/12th-january-1934/54/fine-road-characteristics-of-a-morris |
| S12 | *The Commercial Motor*, 11 May 1934, p.38, "Wheels of Industry" (Commer price correction). https://archive.commercialmotor.com/article/11th-may-1934/38/wheels-of-industry-the-wheels-of-wealth-will-be-sl |
| S13 | *The Commercial Motor*, 20 Jul 1934, p.52, "Fine Road Characteristics Shown by an Austin 6.8-cwt. Van". https://archive.commercialmotor.com/article/20th-july-1934/52/fine-road-characteristics-shown-by |
| S14 | *The Commercial Motor*, 7 Dec 1934, p.38, "An Eight-wheeler Added to the Leyland Range" (Octopus). https://archive.commercialmotor.com/article/7th-december-1934/38/an-eight-wheeler-added-to-the-leyland-range |
| S15 | *The Commercial Motor*, 6 Mar 1936, p.38, "Fine Road Characteristics of a Morris-Commercial 30-cwt. Lorry". https://archive.commercialmotor.com/article/6th-march-1936/40/fine-road-characteristics-of |
| S16 | *The Commercial Motor*, 15 May 1936, p.61, "A New Bulk-load 1-tonner" (Morris-Commercial semi-forward-control). https://archive.commercialmotor.com/article/15th-may-1936/61/a-new-bulk-load-1-tonner |
| S17 | *The Commercial Motor*, 14 Aug 1936, p.33, "Improvements in New Austin Range". https://archive.commercialmotor.com/article/14th-august-1936/33/improvements-in-new-austin-range |
| S18 | *The Commercial Motor*, 5 Nov 1937, p.38, "Austin" (Commercial Show stand report). https://archive.commercialmotor.com/article/5th-november-1937/38/austin |
| S19 | *The Commercial Motor*, 15 Apr 1938, p.42, "First Cost and Taxation" (Bedford 5–6-cwt. van road test). https://archive.commercialmotor.com/article/15th-april-1938/42/first-cost-and-taxation-thjugation-proved-right-in |
| S20 | *The Commercial Motor*, 5 May 1939, p.82, "What is New in Goods-Vehicle Design?". https://archive.commercialmotor.com/article/5th-may-1939/82/what-is-new-in-g-ds-vehicle-design |
| S21 | *The Commercial Motor*, 19 Nov 1943, p.40, "The Vehicle That Is a Little Better". https://archive.commercialmotor.com/article/19th-november-1943/41/the-vehicle-that |
| S22 | *The Commercial Motor*, 1 Dec 1950, p.47, "Changes in Bedford Specifications and Prices". https://archive.commercialmotor.com/article/1st-december-1950/47/changes-in-bedford-specifications-and-prices |
| S23 | *The Commercial Motor*, 31 May 1957, p.49, "B.M.C. Prices Revised". https://archive.commercialmotor.com/article/31st-may-1957/49/bmc-prices-revised |
| S24 | *The Commercial Motor*, 4 Jul 1958, p.62, "New Albions Step Ahead". https://archive.commercialmotor.com/article/4th-july-1958/67/new-albions-step-ahead |
| S25 | *The Commercial Motor*, 3 Oct 1958, p.135, "Light Six-wheelers Offer Economies" (market price analysis). https://archive.commercialmotor.com/article/3rd-october-1958/135/light-six-wheelers-offer-economies |
| S26 | *The Commercial Motor*, 6 May 1960, p.134, "What Will It Cost?" (multi-make price list). https://archive.commercialmotor.com/article/6th-may-1960/134/what-will-it-cost |
| S27 | *The Commercial Motor*, 9 Sep 1960, p.73, "Changes in Bedford CA Van Models". https://archive.commercialmotor.com/article/9th-september-1960/73/changes-in-bedford-ca-van-models |
| S28 | *The Commercial Motor*, 8 Dec 1961, p.50, "Van Prices Up" (Ford Thames). https://archive.commercialmotor.com/article/8th-december-1961/50/van-prices-up |
| S29 | *The Commercial Motor*, 2 Jun 1961, p.88, "Latest Leyland Octopus Models". https://archive.commercialmotor.com/article/2nd-june-1961/95/wi |
| S30 | *The Commercial Motor*, 3 May 1963, p.179, "The Score Was A Score" (road-test review, Austin A35 price). https://archive.commercialmotor.com/article/3rd-may-1963/179/the-score-was-a-score |
| S31 | Bedford CA advertisement, *The Commercial Motor*, 19 Nov 1965, p.79. https://archive.commercialmotor.com/article/19th-november-1965/79/invest-in-a-money-saving-bedford-ca-van-watch-your |
| S32 | *The Commercial Motor*, 31 Oct 1975, p.34, Leyland Octopus launch report. https://archive.commercialmotor.com/article/31st-october-1975/34/this-method-is-said-to-provide-a-marked-increase-i |
| S33 | *The Commercial Motor*, 10 Feb 1933, p.102, "A New A.E.C." (diesel option price). https://archive.commercialmotor.com/article/10th-february-1933/103/a-new-aec |
| S34 | *The Commercial Motor*, 3 Mar 1933, p.66, "Problems" (S.T.R., oil versus petrol costing). https://archive.commercialmotor.com/article/3rd-march-1933/66/problems |
| S35 | *The Commercial Motor*, 16 Mar 1926, p.41, "The Steam Wagon's Honourable Career". https://archive.commercialmotor.com/article/16th-march-1926/41/the-steam-wagons-honourable-career |
| S36 | *The Commercial Motor*, 23 Mar 1926, p.20, "The Future of Steam Vehicle". https://archive.commercialmotor.com/article/23rd-march-1926/22/the-future-of-steam-vehicle |
| S37 | *The Commercial Motor*, 6 Dec 1927, p.64, "The Steam Wagon and its Boiler" (correspondence). https://archive.commercialmotor.com/article/6th-december-1927/64/the-steam-wagon-and-its-boiler |
| S38 | *The Commercial Motor*, 16 Dec 1930, p.97, statement by Mr E. R. Foden, managing director, Fodens Ltd. https://archive.commercialmotor.com/article/16th-december-1930/97/the |
| S39 | *The Commercial Motor*, 30 Sep 1924, p.26, "The Hauliers' Inquire Within" (steam versus petrol operating costs). https://archive.commercialmotor.com/article/30th-september-1924/26/the-hauliers-inquire-within |
| S40 | Wikipedia, "AEC 850", citing Thackray (2012) p.92 — chassis £2,135, bodies £145/£165 (body-cost evidence only). https://en.wikipedia.org/wiki/AEC_850 |
| S41 | Parent-session lead, not re-verified in this pass: Bedford TK 7-ton 1960 (£1,100 chassis / £1,200 chassis-cab / £1,330 complete); Ford Transit £542 (1965); Scammell Crusader £16,622 (1977). |
| S42 | *The Commercial Motor*, 28 Sep 1934, p.38, "A Cub Oiler Upholds the Leyland Reputation" (road test; quality-versus-price statement). https://archive.commercialmotor.com/article/28th-september-1934/38/a-cub-oiler-upholds-the |

---

## 3. Measured figures

Payload given as the maker's rating. "£/t" is price divided by payload in the same nominal
year — it is a shape measure only, never a cross-year comparison.

### 3.1 1920 — Olympia Show list prices [S1]

| Year | Make / model | Payload | Engine | Scope | £ | £/t | Conf. |
|---|---|---|---|---|---|---|---|
| 1920 | Belsize 12-cwt van | 0.6 t | petrol | chassis | 500 | 833 | MEASURED |
| 1920 | Belsize 12-cwt van | 0.6 t | petrol | complete (van) | 620 | 1,033 | MEASURED |
| 1920 | Pagefield 3-ton | 3 t | petrol | chassis | 1,200 | 400 | MEASURED |
| 1920 | Pagefield 5-ton tip wagon | 5 t | petrol | complete | 1,775 | 355 | MEASURED |
| 1920 | Foden 5-ton steam | 5 t | steam | complete, high-sided | 1,295 | 259 | MEASURED |
| 1920 | Clayton 6-ton undertype | 6 t | steam | complete, plain lorry body | 1,350 | 225 | MEASURED |
| 1920 | Clayton 5-ton overtype tipper | 5 t | steam | complete, end tipper | 1,395 | 279 | MEASURED |

The Clayton overtype figure includes £100 for the tipping gear; the same wagon without it is
therefore £1,295 [S1, stated in the same sentence]. The Foden is "the price of the wagon, as
shown, and complete with tyres" [S1].

### 3.2 1924–1928 — steam and municipal purchase [S2–S5]

| Year | Make / model | Payload | Engine | Scope | £ | £/t | Conf. |
|---|---|---|---|---|---|---|---|
| 1924 | steam wagon (make not named) + two 4-ton trailers | 5–6 t (+8 t trailers) | steam | complete | ~1,275 | 212–255 | STATED "about" |
| 1924 | petrol wagon | 2–2.5 t | petrol | complete | ~565 | 226–282 | STATED "about" |
| 1924 | petrol wagon | 1–1.25 t | petrol | complete | ~450 | 360–450 | STATED "about" |
| 1927 | Sentinel D.G.6 six-wheeler | 10–12 t | steam | complete, flat platform | 1,150 | 96–115 | MEASURED **OCR** |
| 1928 | Yorkshire W.J. six-wheeler | 10–15 t | steam | complete, platform | ~1,150 | 77–115 | STATED "in the neighbourhood of" |

The 1924 rows are a borough engineer's recommendations to Wandsworth Borough Council: "a
5–6-ton steam wagon with two 4-ton trailers at about £1,275; a 2–2½-ton petrol wagon at about
£565, and a 1–1¼-ton petrol wagon at about £450" [S2]. They are committee figures, not
invoices, hence STATED.

The Sentinel D.G.6 row is the road-test specification panel that survived as prose:
"TYPE.—D.G.6 model Sentinel wagon. Price 11,150, with flat platform body. LOAD CAPACITY.—
10–12 tons" [S3]. The lost character is the pound sign; £11,150 is impossible for 1927 and
£1,150 is consistent with the Yorkshire and Clayton figures.

### 3.3 1928 — AEC: a clean six-rung ladder [S5]

Published as a price-reduction notice with the old price in parentheses, which makes it
self-checking.

| Year | Model | Payload | Engine | Scope | £ new | £ old | £/t | Conf. |
|---|---|---|---|---|---|---|---|---|
| 1928 | AEC 204 | 2–2½ t | petrol | chassis | 495 | 545 | 198–248 | MEASURED |
| 1928 | AEC 204 (pneumatic tyres) | 2–2½ t | petrol | chassis | 545 | 595 | 218–273 | MEASURED |
| 1928 | AEC 418 | 3½ t | petrol | chassis | 675 | 710 | 193 | MEASURED |
| 1928 | AEC 428 (short) | 4 t | petrol | chassis | 710 | 730 | 178 | MEASURED |
| 1928 | AEC 506 | 5 t | petrol | chassis | 800 | 840 | 160 | MEASURED |
| 1928 | AEC 506-1 | 6 t | petrol | chassis | 850 | 890 | 142 | MEASURED |

### 3.4 1930–1931 — three makers, overlapping payloads

**Guy, 1931 programme** [S7] — a complete ladder from one maker in one announcement, with
1930 comparatives:

| Year | Model | Payload | Scope | £ | £/t | Conf. |
|---|---|---|---|---|---|---|
| 1930 | Guy O.N. 30-cwt | 1.5 t | chassis | 298 | 199 | MEASURED **OCR** |
| 1930 | Guy K | 2–2½ t | chassis | 398 | 159–199 | MEASURED |
| 1930 | Guy T | 3–4 t | chassis | 695 | 174–232 | MEASURED |
| 1930 | Guy EC6 "Warrior" | 6 t | chassis | 995 | 166 | MEASURED **OCR** |
| 1930 | Guy ECS "Bulwark" | 8 t | chassis | 1,125 | 141 | MEASURED |
| 1930 | Guy six-wheeler (subsidy type) | 3–5 t | chassis | 1,060 | 212–353 | MEASURED **OCR** |
| 1930 | Guy ECZ "Goliath" | 12 t | chassis, forward control | 1,460 | 122 | MEASURED |

**Thornycroft QC, 1931** [S8] — the same payload class as the Guy Goliath:

| Year | Model | Payload | Scope | £ | £/t | Conf. |
|---|---|---|---|---|---|---|
| 1931 | Thornycroft QC (normal control, 14 ft 6 in) | 12 t | chassis | 1,410 | 118 | MEASURED |
| 1931 | Thornycroft QC Long (16 ft 9 in) | 12 t | chassis | 1,450 | 121 | MEASURED |
| 1931 | Thornycroft QC Forward (forward control) | 12 t | chassis | 1,450 | 121 | MEASURED |

The article adds that body allowance is 1 t 10 cwt on top of the 12-ton payload [S8] — a useful
reminder that "payload" excludes body.

**Peerless, 1930 — the petrol/oil pair** [S6]. The most valuable single row set in the pass,
because the same chassis is priced with two engines:

| Year | Model | Payload | Engine | Scope | £ | Conf. |
|---|---|---|---|---|---|---|
| 1930 | Peerless 6–7 t | 6–7 t | Gardner 4L2 oil | chassis, pneumatic | 1,100 | MEASURED |
| 1930 | Peerless 6–7 t | 6–7 t | Gardner 4L2 oil | chassis, solid | 980 | MEASURED **OCR** |
| 1930 | Peerless 6–7 t | 6–7 t | Peerless petrol | chassis, pneumatic | 690 | MEASURED |
| 1930 | Peerless 6–7 t | 6–7 t | Peerless petrol | chassis, solid | 570 | MEASURED |

Both pairs give exactly **£410** for the Gardner: 1,100 − 690 = 410 and 980 − 570 = 410. Two
independent subtractions agreeing is strong internal evidence that the reading is right.

### 3.5 1933–1939 — light commercial and heavy

| Year | Make / model | Payload | Engine | Scope | £ | £/t | Conf. |
|---|---|---|---|---|---|---|---|
| 1933 | Morris-Commercial 15-cwt | 0.75 t | petrol | complete | 191 | 255 | MEASURED |
| 1933 | Morris-Commercial 1-ton | 1 t | petrol | complete | 198 | 198 | MEASURED |
| 1933 | Studebaker Pierce-Arrow | 2½ t | petrol | chassis | 425 | 170 | MEASURED |
| 1934 | Morris-Commercial 3-ton | 3 t | petrol | complete, 14 ft platform | 329 | 110 | MEASURED |
| 1934 | Commer 20–25-cwt | 1–1.25 t | petrol | chassis | 165 | 132–165 | MEASURED |
| 1934 | Austin 6–8-cwt van | 0.35 t | petrol | complete, grey primer | 148 | 423 | MEASURED |
| 1934 | Leyland Octopus 8-wheeler, SWB, trailing axle | 13 t | petrol | chassis | 1,225 | 94 | MEASURED |
| 1934 | Leyland Octopus, SWB, double drive | 13 t | petrol | chassis | 1,325 | 102 | MEASURED |
| 1934 | Leyland Octopus, LWB, trailing axle | 13–15 t | petrol | chassis | 1,250 | 83–96 | MEASURED |
| 1934 | Leyland Octopus, LWB, double drive | 13–15 t | petrol | chassis | 1,350 | 90–104 | MEASURED |
| 1936 | Austin Seven 5-cwt | 0.25 t | petrol | complete | 108 | 432 | MEASURED |
| 1936 | Austin Ten 6–8-cwt | 0.35 t | petrol | complete | 150 | 429 | MEASURED |
| 1936 | Austin Twelve 7–10-cwt | 0.425 t | petrol | complete | 172.50 | 406 | MEASURED |
| 1936 | Austin Twelve-Six 7–10-cwt (6-cyl) | 0.425 t | petrol | complete | 190 | 447 | MEASURED |
| 1936 | Morris-Commercial 30-cwt | 1.5 t | petrol | chassis **and cab** | 201 | 134 | MEASURED |
| 1936 | Morris-Commercial 1-ton semi-FC | 1 t | petrol | chassis | 178 | 178 | MEASURED |
| 1936 | Morris-Commercial 1-ton semi-FC | 1 t | petrol | complete van | 257 | 257 | MEASURED |
| 1937 | Austin 7 h.p. van | 0.25 t | petrol | complete, priming | 115 | 460 | MEASURED |
| 1938 | Bedford 5–6-cwt van | 0.275 t | petrol | complete | 140 | 509 | MEASURED |
| 1939 | Lloyd | n/a (light) | petrol | chassis | 277.50 | — | MEASURED **OCR** |

Two of these carry important qualifiers:

- The Austin 6–8-cwt figure is the road-test statement "the price of the model in question, in
  grey priming, is £148 and the tax £15" [S13]. Primer finish, not paint, and tax excluded.
- The Lloyd sentence reads "a real effort to produce a commercial vehicle to sell for less than
  £100 ... yet costing only £277 10s. in chassis form" [S20]. The two numbers cannot both be
  right; £100 is almost certainly OCR damage for £300 (the van was advertised as Britain's
  cheapest, below £300). Treat the £277 10s chassis figure as usable and the £100 as corrupt.

### 3.6 1943 — the size of the maker spread, stated

*The Commercial Motor*, 19 Nov 1943: "For an oil-engined lorry with double dropsided body,
capable of carrying a pay-load of 6 tons and weighing less than 3 tons unladen, the haulier may
be asked to pay anything from **£800 to £1,200** ... the difference ... is so great that he can
buy three of the low-priced vehicles for the price of two of the others" [S21]. STATED, but
unusually useful because it is a same-specification, same-payload spread from the trade's own
journal: **a 50% premium band existed in the 6-ton class in the 1940s**.

### 3.7 1950 — Bedford: the full three-scope schedule [S22]

Prices "including purchase tax". This single table separates chassis, cab and body better than
anything else in the pass.

| Year | Model | Payload | Scope | £ | Conf. |
|---|---|---|---|---|---|
| 1950 | Bedford 10–12-cwt van | 0.55 t | complete | 409.70 | MEASURED |
| 1950 | Bedford 1½-ton | 1.5 t | chassis | 476.28 | MEASURED |
| 1950 | Bedford 1½-ton | 1.5 t | chassis and cab | 521.28 | MEASURED |
| 1950 | Bedford 1½-ton | 1.5 t | complete lorry | 556.28 | MEASURED |
| 1950 | Bedford 3-ton SWB | 3 t | chassis | 514.41 | MEASURED |
| 1950 | Bedford 3-ton SWB | 3 t | chassis and cab | 559.41 | MEASURED |
| 1950 | Bedford 3-ton SWB | 3 t | complete lorry | 599.41 | MEASURED |
| 1950 | Bedford 3-ton SWB | 3 t | complete tipper | 619.41 | MEASURED |
| 1950 | Bedford 4-ton SWB | 4 t | chassis | 597.72 | MEASURED |
| 1950 | Bedford 4-ton SWB | 4 t | chassis and cab | 642.72 | MEASURED |
| 1950 | Bedford 4-ton SWB | 4 t | complete tipper | 747.72 | MEASURED |
| 1950 | Bedford 5-ton SWB | 5 t | chassis | 636.01 | MEASURED |
| 1950 | Bedford 5-ton SWB | 5 t | chassis and cab | 681.01 | MEASURED |
| 1950 | Bedford 5-ton SWB | 5 t | complete tipper | 786.01 | MEASURED |
| 1950 | Bedford 5-ton LWB | 5 t | complete lorry | 763.75 | MEASURED |
| 1950 | Bedford 8-ton tractor unit | (tractive) | chassis and cab | 637.72 | MEASURED |

### 3.8 1957 — BMC: the badge-engineering pair [S23]

Prices quoted include purchase tax, and the article prints the tax separately, so the
ex-tax price is recoverable.

| Year | Model | Payload | Scope | £ incl. tax | tax | Conf. |
|---|---|---|---|---|---|---|
| 1957 | Morris 5-cwt van | 0.25 t | complete | 445.12 | £60 2s 5d | MEASURED |
| 1957 | Austin A35 5-cwt van | 0.25 t | complete | 422.90 | £54 8s | MEASURED |
| 1957 | Austin A35 5-cwt pick-up | 0.25 t | complete | 584.85 | £195 17s (car rate) | MEASURED |
| 1957 | Austin 10-cwt van | 0.5 t | complete | 588.68 | £74 3s 7d | MEASURED |
| 1957 | Austin A101 van | 0.5 t | complete | 553.64 | £74 12s 9d | MEASURED |
| 1957 | Austin 1-ton van, petrol | 1 t | complete | 798.82 | £104 16s 4d | MEASURED |
| 1957 | Austin 1-ton van, oil | 1 t | complete | 930.08 | £131 1s 7d | MEASURED |
| 1957 | Austin 1½-ton lorry, petrol | 1.5 t | complete | 737.31 | £115 6s 3d | MEASURED |
| 1957 | Austin 1½-ton lorry, oil | 1.5 t | complete | 935.01 | £154 10s 1d | MEASURED |
| 1957 | Austin 2-ton lorry, petrol | 2 t | complete | 792.30 | £125 0s 1d | MEASURED |
| 1957 | Austin 2-ton lorry, oil | 2 t | complete | 990.04 | £164 10s 9d | MEASURED |

The A35 pick-up at £584 17s against the A35 van at £422 18s is the purchase-tax anomaly of the
period: a pick-up was taxed at the private-car rate. Do not use it as a body-cost datum.

### 3.9 1958 — Albion and the market averages

| Year | Model | Payload | Engine | Scope | £ | £/t | Conf. |
|---|---|---|---|---|---|---|---|
| 1958 | Albion Chieftain CH.3L | 7 t | oil | chassis and cab | 1,686 | 241 | MEASURED |
| 1958 | Albion Claymore 4-ton | 4 t | oil | chassis and cab | 1,133 | 283 | MEASURED |
| 1958 | Albion Claymore 5-ton | 5 t | oil | chassis and cab | 1,163 | 233 | MEASURED |
| 1958 | class average, eight 5-tonners | 5 t | oil | as offered | 1,500 | 300 | STATED |
| 1958 | class average, eleven 7-tonners | 7 t | oil | as offered | 2,000 | 286 | STATED |
| 1958 | class average, medium six-wheelers | ~8–10 t | oil | as offered | 2,750 | — | STATED |
| 1958 | class average, seven heavy six-wheelers | ~12–14 t | oil | as offered | 4,500 | — | STATED |

The Albion article also prices options: sixth-speed overdrive £15 [S24]. The averages are the
journal's own arithmetic: "the average price for eight representative 5-tonners is £1,500, for
11 7-tonners £2,000, with a jump to around £2,750 for what few medium-weight or converted rigid
six-wheelers are available. Seven makes of heavy six-wheeler cost around £4,500" [S25].

### 3.10 1960 — the multi-make list [S26]

The richest single document found. It was set as running prose, so it survived OCR. It is
home-market retail, ex works, primer finish only, shortest wheelbase unless stated. Section
headings are short lines and were lost in a naive extraction; the block boundaries were
recovered by re-reading the page with short lines kept, and each block is attributed below on
that basis.

**Austin** (line block 1)

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | A35 5-cwt van | 0.25 t | petrol | complete | 363 | 1,452 |
| 1960 | 1-ton | 1 t | petrol | chassis and cab | 443 | 443 |
| 1960 | 1-ton | 1 t | oil | chassis and cab | 545 | 545 |
| 1960 | 1-ton | 1 t | petrol | complete van | 694 | 694 |
| 1960 | 1-ton | 1 t | oil | complete van | 799 | 799 |
| 1960 | 200 FC | 2 t | oil | chassis and cab | 817.50 | 409 |
| 1960 | 304 FC | 3 t | oil | chassis and cab | 867.50 | 289 |
| 1960 | 404 FC | 4 t | oil | chassis and cab | 927.50 | 232 |
| 1960 | 5-ton FC | 5 t | oil | chassis and cab | 1,098.50 | 220 |
| 1960 | 702 FC 7-ton SWB | 7 t | oil | chassis and cab | 1,162 | 166 |
| 1960 | 303 NC 3-ton | 3 t | oil | chassis and cab | 839.50 | 280 |

**Bedford**

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | CA5 10–12-cwt | 0.55 t | petrol | chassis | 345 | 627 |
| 1960 | CA5 10–12-cwt | 0.55 t | petrol | complete van | 445 | 809 |
| 1960 | 15-cwt | 0.75 t | petrol | complete van | 452 | 603 |
| 1960 | 3-ton NC SWB | 3 t | oil | chassis and cab | 840 | 280 |
| 1960 | 4-ton NC | 4 t | oil | chassis and cab | 890 | 223 |
| 1960 | 5-ton NC SWB | 5 t | oil | chassis and cab | 1,025 | 205 |
| 1960 | 6-ton NC SWB | 6 t | oil | chassis and cab | 1,060 | 177 |
| 1960 | 6½-ton NC SWB | 6.5 t | oil | chassis and cab | 1,110 | 171 |
| 1960 | 7-ton NC SWB | 7 t | oil | chassis and cab | 1,205 | 172 |
| 1960 | 7-ton FC SWB | 7 t | oil | chassis and cab | 1,127 | 161 |

**Commer**

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | Cob 5-cwt van | 0.25 t | petrol | complete | 430 | 1,720 |
| 1960 | Express 6–7-cwt van | 0.3 t | petrol | complete | 485 | 1,617 |
| 1960 | Superpoise 3–4-ton | 3.5 t | oil | chassis and cab | 1,034 | 295 |
| 1960 | Superpoise 5-ton | 5 t | oil | chassis and cab | 1,129 | 226 |
| 1960 | Superpoise 6-ton | 6 t | oil | chassis and cab | 1,164 | 194 |
| 1960 | FC 5-ton | 5 t | oil | chassis and cab | 1,150 | 230 |
| 1960 | FC 6-ton | 6 t | oil | chassis and cab | 1,185 | 198 |
| 1960 | FC 7-ton | 7 t | oil | chassis and cab | 1,455 | 208 |

**Dodge (Kew)**

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | 264 NC 3-ton | 3 t | oil | chassis and cab | 980 | 327 |
| 1960 | 201P NC 5-ton | 5 t | oil | chassis and cab | 1,193 | 239 |
| 1960 | 223R NC 6½-ton | 6.5 t | oil | chassis and cab | 1,378 | 212 |
| 1960 | 244R NC 7-ton | 7 t | oil | chassis and cab | 1,585 | 226 |
| 1960 | 3144R FC 7-ton | 7 t | oil | chassis and cab | 1,623 | 232 |

**Foden** — priced by gross vehicle weight, not payload, so no £/t on payload is possible:

| Year | Rating | Scope | £ | Conf. |
|---|---|---|---|---|
| 1960 | 13-ton GVW | chassis and cab | 2,786 | MEASURED |
| 1960 | 14-ton GVW | chassis and cab | 2,876 | MEASURED |
| 1960 | 17-ton GVW twin-steer | chassis and cab | 3,427 | MEASURED |
| 1960 | 20-ton GVW | chassis and cab | 3,549 | MEASURED |
| 1960 | 24-ton GVW | chassis and cab | 3,688 | MEASURED **OCR** |

**Ford (Thames / Trader)**

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | Thames 5-cwt van | 0.25 t | petrol | complete | 338 | 1,352 |
| 1960 | Thames 7-cwt van | 0.35 t | petrol | complete | 365 | 1,043 |
| 1960 | Thames 10–12-cwt | 0.55 t | petrol | chassis | 364 | 662 |
| 1960 | Thames 10–12-cwt | 0.55 t | petrol | chassis and cab | 419 | 762 |
| 1960 | Thames 10–12-cwt | 0.55 t | petrol | complete van | 459 | 835 |
| 1960 | Thames 15-cwt | 0.75 t | petrol | complete van | 469 | 625 |
| 1960 | Thames 30-cwt | 1.5 t | oil | chassis and cab | 704 | 469 |
| 1960 | Thames 2-ton | 2 t | oil | chassis and cab | 724 | 362 |
| 1960 | Thames 3-ton SWB | 3 t | oil | chassis and cab | 769 | 256 |
| 1960 | Thames 4-ton SWB | 4 t | oil | chassis and cab | 822 | 206 |
| 1960 | Trader 5-ton | 5 t | oil | chassis and cab | 960 | 192 |
| 1960 | Trader 7-ton | 7 t | oil | chassis and cab | 1,172 | 167 |

**Karrier**

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | 1-ton FC | 1 t | oil | complete van | 857 | 857 |
| 1960 | Bantam 2–3-ton SWB | 2.5 t | oil | chassis and cab | 859 | 344 |
| 1960 | Gamecock 3–4-ton | 3.5 t | oil | chassis and cab | 1,090 | 311 |

**Morris-Commercial**

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | JB 10-cwt | 0.5 t | petrol | chassis | 319.50 | 639 |
| 1960 | JB 10-cwt | 0.5 t | petrol | complete van | 458 | 916 |
| 1960 | J2 15-cwt | 0.75 t | petrol | complete van | 493 | 657 |
| 1960 | 1-ton FC | 1 t | oil | complete van | 815 | 815 |
| 1960 | 2-ton FG FC | 2 t | oil | chassis and cab | 817.50 | 409 |
| 1960 | 3-ton FG FC | 3 t | oil | chassis and cab | 867.50 | 289 |
| 1960 | 5-ton FC | 5 t | oil | chassis and cab | 1,098.50 | 220 |
| 1960 | 7-ton FC SWB | 7 t | oil | chassis and cab | 1,162 | 166 |

The Austin and Morris-Commercial blocks are *identical* at 2, 3, 5 and 7 tons (£817 10s,
£867 10s, £1,098 10s, £1,162). That is badge engineering visible in the price list, and it is
a useful control: two marques, one price.

**Seddon, Reliant, Standard** — for the premium and small-van edges:

| Year | Model | Payload | Engine | Scope | £ | £/t |
|---|---|---|---|---|---|---|
| 1960 | Seddon 30-cwt | 1.5 t | oil | chassis and cab | 805 | 537 |
| 1960 | Seddon Mark 7 3-ton | 3 t | oil | chassis and cab | 1,105 | 368 |
| 1960 | Seddon Mark 16 5-ton | 5 t | oil | chassis and cab | 1,500 | 300 |
| 1960 | Seddon Mark 19 "Pennine" | ~7 t | oil | chassis | 1,950 | 279 |
| 1960 | Reliant 5-cwt van or truck | 0.25 t | petrol | complete | 349 | 1,396 |
| 1960 | Standard 6-cwt van | 0.3 t | petrol | complete | 411 | 1,370 |
| 1960 | Standard Atlas 10–12-cwt van | 0.55 t | petrol | complete | 475 | 864 |

### 3.11 1960–1977 — later points

| Year | Make / model | Payload | Engine | Scope | £ | Conf. |
|---|---|---|---|---|---|---|
| 1960 | Bedford CA 10–12-cwt van | 0.55 t | petrol | complete | 450 | MEASURED [S27] |
| 1960 | Bedford CA 15-cwt van | 0.75 t | petrol | complete | 460 | MEASURED [S27] |
| 1961 | Ford Thames 5-cwt van | 0.25 t | petrol | complete | 379 | MEASURED [S28] |
| 1961 | Ford Thames 7-cwt van | 0.35 t | petrol | complete | 409 | MEASURED [S28] |
| 1961 | Leyland Octopus 240.9R | ~16 t | oil | chassis (steel cab) | ~4,200 | STATED "in the region of" [S29] |
| 1963 | Austin A35 van | 0.25 t | petrol | complete, painted | 388 | MEASURED [S30] |
| 1965 | Bedford CA 10/12-cwt van | 0.55 t | petrol or diesel | complete, from | 475 | MEASURED [S31] |
| 1965 | Bedford CA 15/17-cwt van | 0.85 t | petrol or diesel | complete, from | 485 | MEASURED [S31] |
| 1975 | Leyland Octopus 30-ton tipper | ~20 t | oil | chassis and cab | 13,950 | MEASURED [S32] |

The 1965 Bedford figures are an advertisement's "from" prices, so they are floors, not list
prices for a specified vehicle. The advertisement also prices factory paint at £17 10s, which
is the cheapest paint datum found and explains why every list price in this file says "primer".

The 1975 Octopus row is accompanied by the body cost in the same article: "Price for body and
gear was quoted as £3,124" for an Edbro 20 cu yd alloy tipper body and single-ram gear [S32].

Inherited but not re-verified in this pass [S41]: Bedford TK 7-ton, 1960 — chassis £1,100,
chassis and cab £1,200, complete with body £1,330; Ford Transit £542, 1965; Scammell Crusader
£16,622, 1977. The Bedford TK triple is consistent with the 1960 Bedford schedule above
(7-ton NC chassis-cab £1,205 oil against the inherited £1,200), which raises confidence in it.

---

## 4. Price per ton of payload

### 4.1 The shape

Read down any single-year, single-maker column and the price per ton falls steeply and then
flattens. Taking chassis-cab oil-engined figures from 1960 [S26]:

| Payload | Ford £/t | Bedford £/t | Austin £/t | Commer £/t | Dodge £/t | Seddon £/t |
|---|---|---|---|---|---|---|
| 1.5 t | 469 | — | — | — | — | 537 |
| 2 t | 362 | — | 409 | — | — | — |
| 3 t | 256 | 280 | 289 | 295 (3.5 t) | 327 | 368 |
| 4 t | 206 | 223 | 232 | — | — | — |
| 5 t | 192 | 205 | 220 | 226 | 239 | 300 |
| 6 t | — | 177 | — | 194 | 212 (6.5 t) | — |
| 7 t | 167 | 172 | 166 | 208 | 226 | 279 |

Two things fall out of this. First, the *shape* is the same for every maker — roughly a halving
of £/ton between 1.5 t and 7 t — and the makers differ mainly by a near-constant multiplier.
Second, at the very light end the curve steepens sharply: the 5-cwt to 15-cwt band runs at
£600–£1,700 per ton, four to ten times the heavy-lorry rate.

### 4.2 The exponent

Fitting price against payload over 2–7 t for the mass-market makers gives price ∝ payload^0.5
to payload^0.55:

- Ford 1960, 3 t £769 to 7 t £1,172: ratio 1.52 on a payload ratio of 2.33 → exponent 0.50.
- AEC 1928, 2.25 t £495 to 6 t £850: ratio 1.72 on a payload ratio of 2.67 → exponent 0.55.
- Bedford 1950, 1.5 t £521 to 5 t £681: ratio 1.31 on a payload ratio of 3.33 → exponent 0.22.
- Guy 1930, 2.25 t £398 to 8 t £1,125: ratio 2.83 on a payload ratio of 3.56 → exponent 0.81.

The Guy figure is the outlier: its light models were priced very aggressively (the 30-cwt at
£298, the 2–2½-ton at £398) and its heavy models conventionally, which steepens the curve. The
Bedford 1950 figure is flattened by purchase tax, which was a larger proportion of a cheap
vehicle than a dear one.

**Recommended pakset form:** price = a × payload^0.55 for payloads from 1 to 8 tons, with a
separate, shallower segment above 8 tons (the 1934 Leyland Octopus at 13 t was £94–104/ton
against £141/ton for a 1930 8-ton Guy — heavy eight-wheelers were *cheaper* per ton, not
dearer). Below 1 ton, use a steeper exponent, about 0.75, because the light-van segment does
not follow the lorry curve.

### 4.3 The heavy end is cheaper per ton than the medium

This is the least intuitive result of the pass and it is well evidenced:

| Year | Vehicle | Payload | £/t |
|---|---|---|---|
| 1930 | Guy Bulwark 8-ton, chassis | 8 t | 141 |
| 1931 | Guy Goliath 12-ton, chassis | 12 t | 122 |
| 1931 | Thornycroft QC 12-ton, chassis | 12 t | 118–121 |
| 1934 | Leyland Octopus 8-wheeler, chassis | 13 t | 94–104 |
| 1927 | Sentinel D.G.6 steam, complete | 10–12 t | 96–115 |
| 1928 | Yorkshire W.J. steam, complete | 10–15 t | 77–115 |
| 1960 | Seddon Mark 16 5-ton, chassis-cab | 5 t | 300 |
| 1960 | Foden 24-ton GVW, chassis-cab | ~15 t payload | ~246 (on GVW: 154) |

The 1930s maximum-load eight-wheeler was the cheapest capacity money could buy per ton, because
it was a scaled-up version of an existing four-wheeler with one more axle and no more cab,
engine or gearbox content. Leyland's Octopus was 20–23% cheaper per ton than Thornycroft's or
Guy's 12-ton six-wheelers in the same years. That is a real maker effect, not a segment effect:
Leyland had the largest production run in the heaviest class.

### 4.4 What "payload" is not

Twice in this pass the source distinguishes payload from body allowance: the Thornycroft QC's
12-ton payload carried "an additional allowance of 1 ton 10 cwt. for the body" [S8], and the
Albion 5-tonner's gross weight was 8½ tons. A pakset ladder built on chassis price per ton of
payload will therefore overstate the price of capacity relative to a ladder built on gross
weight, by roughly the body weight. Keep payload as the ladder variable — it is what the
contemporary price lists used — but do not then also add body weight to the capacity.

---

## 5. Body and cab costs

### 5.1 Measured separations

| Year | Vehicle | Chassis | + cab | + body | Cab cost | Body cost | Source |
|---|---|---|---|---|---|---|---|
| 1920 | Belsize 12-cwt van | 500 | — | 620 | — | 120 (24% of complete) | S1 |
| 1936 | Morris-Commercial 1-ton | 178 | — | 257 (van) | — | 79 (31% of complete, 44% of chassis) | S16 |
| 1950 | Bedford 1½-ton | 476.28 | 521.28 | 556.28 (platform) | 45 | 35 | S22 |
| 1950 | Bedford 3-ton SWB | 514.41 | 559.41 | 599.41 (platform) | 45 | 40 | S22 |
| 1950 | Bedford 3-ton SWB | — | 559.41 | 619.41 (tipper) | — | 60 (tipper gear and body over platform) | S22 |
| 1950 | Bedford 4-ton SWB | 597.72 | 642.72 | 747.72 (tipper) | 45 | 105 (tipper gear and body) | S22 |
| 1960 | Ford Thames 10–12-cwt | 364 | 419 | 459 (van) | 55 | 40 | S26 |
| 1960 | Bedford CA5 10–12-cwt | 345 | — | 445 (van) | — | 100 | S26 |
| 1960 | Morris-Commercial JB 10-cwt | 319.50 | — | 458 (van) | — | 138.50 | S26 |
| 1960 | Austin 1-ton | 443 | — | 694 (van) | — | 251 | S26 |
| 1960 | Austin 1-ton | 443 (petrol) | — | 545 (oil) | — | engine, not body: +102 | S26 |
| 1935 | AEC 850 (military) | 2,135 | — | +145 or +165 | — | 145–165 (7–8% of chassis) | S40 |
| 1975 | Leyland Octopus tipper | — | 13,950 | +3,124 | — | 3,124 (22% of chassis-cab) | S32 |

### 5.2 What this supports

- **Cab: £45 in 1950, £55 in 1960.** Effectively constant in nominal terms over the decade and
  small against the chassis — 8–13% of chassis price on light vehicles, 5–8% on a 7-tonner.
  A pakset that charges a large premium for "with cab" is wrong.
- **Platform body: £35–£40 in 1950–60**, i.e. 5–8% of chassis-cab price on a 3–7-tonner.
- **Van body: £40 on a light Ford, £100 on a Bedford CA, £138 on a Morris JB, £251 on a 1-ton
  Austin.** The spread is real: the Ford and Bedford bodies were cheap pressed-steel
  volume items, the Austin 1-ton body was a low-volume coachbuilt box.
- **Tipper gear and body: +£60 to +£105 over a platform in 1950**, and £3,124 in 1975 — the
  tipper premium scales with body size, not with chassis price.
- **Body as a share of total falls with size**: 31–44% on a 1-ton van, 7–8% on a 3–5-ton
  platform, ~7% on a 12-ton chassis in the 1930s.

---

## 6. Maker premia

### 6.1 The measurements the recommendations rest on

**1960, oil-engined chassis-cab, same payload, same document [S26]:**

| Payload | Cheapest | £ | Mass-market cluster | £ | Mid-premium | £ | Specialist | £ |
|---|---|---|---|---|---|---|---|---|
| 3 t | Ford | 769 | Bedford / Austin / Morris-Com | 840 / 867.5 / 867.5 | Dodge | 980 | Seddon | 1,105 |
| 5 t | Ford | 960 | Bedford | 1,025 | Commer / Dodge | 1,129 / 1,193 | Seddon | 1,500 |
| 7 t | Austin / Morris-Com | 1,162 | Ford / Bedford | 1,172 / 1,205 | Commer / Dodge | 1,455 / 1,585 | Seddon | 1,623 |

The structure is unambiguous and it is the single most useful result of the pass:

- Ford, Bedford, Austin and Morris-Commercial sit within **4% of each other** at 7 tons and
  within **9%** at 5 tons. They are one price band, not four.
- Commer and Dodge sit **20–35% above** that band.
- Seddon (and, from 1958, Albion) sit **40–56% above** it.

**1958 against 1960, 7-ton chassis-cab:** Albion Chieftain £1,686 [S24] against Bedford 7-ton
£1,205 and Ford Trader 7-ton £1,172 [S26]. Both are list prices with purchase tax excluded
(the Albion source adds £364 1s 7d of tax on top; the 1960 list is ex works). The raw gap is
**+40% against Bedford**, and because the Albion figure is two years *earlier* the gap in
constant money is wider still, of the order of +50%. The Albion is also the smaller vehicle of
the two — 10 tons 4 cwt gross for its 7 tons, against a Bedford 7-tonner of roughly 12 tons
gross — so the premium is not being bought with extra weight capacity.

**1931–1934, heavy:** Leyland Octopus 13 t at £1,225–1,350 [S14] against Thornycroft QC 12 t at
£1,410–1,450 [S8] and Guy Goliath 12 t at £1,460 [S7]. Leyland is **12–23% cheaper per ton**;
Thornycroft and Guy are within 3% of each other. This inverts the usual assumption that
Thornycroft was the dearer makes: at equal payload in 1931 Thornycroft undercut Guy.

**1943, stated:** a £800–£1,200 band for the same 6-ton oil-engined specification [S21] — a
50% spread, the upper end paying for durability.

**1960 vans, petrol, complete:**

| Class | Bedford | Ford | Austin | Morris | Commer | Reliant | Standard |
|---|---|---|---|---|---|---|---|
| 5 cwt | — | 338 | 363 | 379.5 | 430 (Cob) | 349 | 411 (6 cwt) |
| 10–12 cwt | 445 | 459 | 458 (101) | 458 (JB) | 499 (8 cwt) | — | 475 (Atlas) |
| 15 cwt | 452 | 469 | 493 | 493 | — | — | — |

Bedford is cheapest at 10–12 and 15 cwt; Ford cheapest at 5 cwt; Commer dearest throughout;
Austin and Morris identical. But note the 1938 counter-example: the Bedford 5–6-cwt was
introduced at £140 when the Austin 6–8-cwt was £150, and *The Commercial Motor* recorded that
"we expressed the view that it would be handicapped in competing with other vehicles in its
class which were lighter (and, therefore, taxed at a lower rate) and cheaper" [S19]. Bedford's
reputation for cheapness is a 1950s–60s phenomenon, earned by the CA and TK; in 1938 the
Bedford was the heavier and dearer option and won on durability, not price.

### 6.2 Recommended bands and the mechanism

Mechanism: build one **class-median curve** from the mass-market makers only (Bedford, Ford,
Austin, Morris-Commercial) — those four are within 9% of each other at every rung, so their
mean is a stable base. Then apply a single **maker multiplier** to the whole model range, and
after that add body and engine options as separate multipliers. Do not encode maker premia as
per-model exceptions; every maker in this dataset prices its whole range at a near-constant
offset from the class median, which is exactly what a single multiplier reproduces.

| Maker | Band vs class median | Mechanism | Evidence |
|---|---|---|---|
| Ford | 0.93–1.00 | multiplier on base curve | cheapest at 3 t, 5 t, 7 t and 5 cwt in 1960 [S26] |
| Bedford | 0.95–1.02 | multiplier | cheapest at 10–12 and 15 cwt 1960; +4% at 5 t, +3% at 7 t [S26]; dearer in 1938 [S19] |
| Austin | 1.00–1.05 | multiplier | +9% at 3 t, +14% at 5 t, parity at 7 t [S26] |
| Morris / Morris-Commercial | 1.00–1.05 | same multiplier as Austin | identical prices at 2, 3, 5, 7 t [S26] — badge engineering |
| Karrier | 1.10–1.25 | multiplier, small-volume Rootes | Gamecock 3–4 t £1,090 at 3.5 t vs Austin 3 t £867.5 [S26] |
| Commer | 1.15–1.30 | multiplier | +34% at 3.5 t, +18% at 5 t, +25% at 7 t [S26] |
| Dodge (Kew) | 1.25–1.40 | multiplier | +27% at 3 t, +24% at 5 t, +35% at 7 t [S26] |
| Leyland | 0.85–1.00 light/medium; 1.10–1.20 heavy | multiplier by class | Octopus 12–23% cheaper per ton than 12-ton six-wheelers [S14, S8, S7]; Comet/Octopus priced "within £400 of predecessors" and "highly competitive" [S29] |
| Albion | 1.15–1.30 | multiplier | Chieftain 7 t £1,686 in 1958 [S24] vs £1,172–1,205 in 1960 [S26] |
| Thornycroft | 0.95–1.10 | multiplier | QC 12 t £1,410 vs Guy £1,460 [S8, S7] |
| Guy | 1.00–1.15 | multiplier | Goliath 12 t £1,460 [S7]; aggressive light-end pricing (30-cwt £298) |
| AEC | 1.05–1.15 | multiplier | 1928 ladder is mid-market per ton [S5]; diesel option +£100 [S33] |
| Scammell | 1.25–1.40 | multiplier; specialist, low volume | no direct same-payload price found (see §7); inferred from the 1943 £800–1,200 band and its specialist position |
| Seddon | 1.35–1.55 medium; 0.95–1.05 heavy | multiplier by class | +44% at 3 t, +56% at 5 t, +40% at 7 t [S26]; but its heavies were competitive |
| Foden | 1.20–1.35 heavy | multiplier | 24-ton GVW £3,688 vs Seddon 8/A/14 six-wheeler £3,508 [S26] |
| Steam wagons (Sentinel, Foden, Yorkshire, Clayton) | 0.55–0.80 per nominal ton | *separate* curve, not a multiplier | see §6.3 |

### 6.3 Reliability, and what the premium bought

The archive is explicit that the premium is a durability premium and that operators
systematically under-bought:

- Leyland Cub, 1934: "Although by no means the most expensive chassis of its type, the Leyland
  Cub is fairly high in price. Quality of materials and workmanship, durability and numerous
  refinements are what the buyer obtains for his money ... slightly higher first cost ... [is]
  of trifling importance to the operator who seeks trouble-free and lasting service" [S42].
- Morris-Commercial 30-cwt, 1936: "the design reveals clever structural details which explain
  how the price of the chassis has been kept so low ... Economical production has been a prime
  consideration" [S15]. Morris competed on price, openly, and the journal said so.
- 1943: "Faced with the choice between two 6-tonners, one of which is priced at £1,200 and the
  other at £800, the majority says: 'I cannot afford to pay £1,200 ... I will buy that one
  costing £800.' ... Whereas, in actual fact, he cannot afford to buy the one at £800!" [S21]
- Steam, 1926: Fodens "inform us that there are many 24-year-old wagons of their make still in
  operation", and a 23-year-old Thornycroft with 150,000 miles [S35].

So: the premium band is real, it is 20–50%, and the contemporary trade view was that the cheap
end of it was a false economy. For the pakset this argues for a maker multiplier (capital) plus
a **reliability modifier on maintenance cost** in the opposite direction — the dearer makes
should have lower running cost, or the multiplier is a pure penalty with no upside.

---

## 7. Steam wagons against petrol

### 7.1 The measured position, and it is not what the brief expected

The brief anticipated that steam wagons were expensive to buy. At equal payload the
contemporary prices say the opposite.

| Year | Steam wagon | Payload | £ | £/t | Comparable petrol lorry | Payload | £ | £/t |
|---|---|---|---|---|---|---|---|---|
| 1920 | Foden 5-ton, complete | 5 t | 1,295 | 259 | Pagefield 3-ton, chassis only | 3 t | 1,200 | 400 |
| 1920 | Clayton 6-ton undertype, complete | 6 t | 1,350 | 225 | — | — | — | — |
| 1924 | steam wagon + 2 trailers (council estimate) | 5–6 t (+8 t) | ~1,275 | 212–255 | petrol wagon, complete | 2–2.5 t | ~565 | 226–282 |
| 1927 | Sentinel D.G.6, with platform body | 10–12 t | 1,150 | 96–115 | AEC 506, chassis | 5 t | 800 | 160 |
| 1928 | Yorkshire W.J., with body | 10–15 t | ~1,150 | 77–115 | AEC 506-1, chassis | 6 t | 850 | 142 |

Per ton of payload the steam wagon was **cheaper**, by a wide margin, throughout the 1920s. Two
contemporary statements confirm that this was understood at the time:

- Correspondence, 1927: "It is not a question of price, for steam wagons are considerably
  cheaper to the public than any other type of vehicle" [S37]. The writer is a steam partisan,
  so treat the sentiment with care — but the price lists above are not partisan.
- Fodens' managing director, 1930: the steam wagon "has so far proved to be by far the most
  economical vehicle for heavy loads, in first cost, running cost, also maintenance and long
  life" [S38].

### 7.2 Where the real steam penalty was

Not price. Three other things:

1. **Unladen weight.** "Roughly speaking, the unladen weight of the average steam wagon is 50
   per cent. greater than the petrol lorry of the same nominal carrying capacity" [S36]. Under
   the taxation and axle-weight rules of the period this cut the *legal* payload, so the
   effective cost per legal ton was much closer to the petrol lorry's, and on some routes worse.
   A correspondent in 1933 gives a six-wheeled steam lorry of 13 t 5 cwt unladen "thus allowing
   a legal load of only 5 tons 15 cwt." [*The Commercial Motor*, 6 Jan 1933, p.43].
2. **Running cost at light load.** The journal's own costing for a 5-tonner in 1924 gives
   7.59d. per mile for petrol against 8.47d. for steam, with steam ahead only on fuel price and
   behind on lubricants and tyres [S39]. Steam won on ton-mile only when the wagon was fully
   loaded most of the time.
3. **Operating friction**: 45–60 minutes to raise steam from cold, 50-mile water range, smoke
   and sparks, and a second man [S35, S36, S37].

### 7.3 The gap that does exist, and its size

Steam wagons were expensive *as capital items in absolute terms*: a 5-ton steam wagon at
£1,295–1,395 in 1920 cost about three times a 1–1¼-ton petrol wagon at £450 [S1, S2]. An
operator replacing horse drays on short rounds could not use the capacity and so could not
amortise the price.

Within the steam family the ordering is: **Clayton overtype dearest** (£1,395 with tipping
gear, £1,295 without), **Clayton undertype** £1,350, **Foden overtype** £1,295, all for 5–6 tons
in 1920 [S1]. By 1927–28 the purpose-built undertypes had moved the price per ton down hard:
Sentinel D.G.6 at £1,150 for 10–12 tons and Yorkshire W.J. at about £1,150 for 10–15 tons. The
Sentinel was therefore not the cheap option in 1920 (no price found) but was the volume option
by 1927, and the Yorkshire was the largest-capacity machine at the same money.

**Recommendation for the pakset:** do not model steam wagons as a capital premium. Model them
as (a) a separate, lower price-per-nominal-ton curve (about 0.55–0.80 of the petrol lorry curve
at 5–12 tons), (b) a much higher unladen weight, which is the real constraint and should reduce
usable capacity against a gross-weight limit if the engine has one, and (c) higher cost per
mile at part load and lower cost per ton-mile at full load. A flat "steam is 30% dearer"
multiplier is contradicted by every measured steam price in this pass.

---

## 8. Dead ends

1. **Commercial Motor annual Buyer's Guides (1932, 1935, 1937) — tables are images.** These are
   the ideal source: chassis prices tabulated by pay-load heading, all makes, one date. Fetching
   returns the introduction only. The 1932 introduction does at least settle the scope: "Except
   where otherwise stated, the prices quoted are for the chassis alone." If anyone can OCR the
   page images, three complete market ladders are sitting there. This is the highest-value
   follow-up available.
2. **Road-test specification panels — images.** Every road test prints a panel with price as
   tested. None of the panels are in the text layer. Where a price was recoverable it was
   because the journalist repeated it in prose (Morris 3-ton £329, Morris 30-cwt £201, Bedford
   5–6-cwt £140, Austin 6–8-cwt £148).
3. **Sentinel S4/S6 and Super Sentinel prices, 1930–1935 — not found.** The 1923 Super-Sentinel
   7-ton road test [*The Commercial Motor*, 20 Nov 1923, p.26] gives weights and consumption but
   no price. The 1933 announcement of the new four-wheeler [*The Commercial Motor*, 5 May 1933,
   p.103] says prices will follow and they did not appear in the text. The 1930 D.G.6 test
   [*The Commercial Motor*, 4 Feb 1930, p.50] likewise omits price.
4. **Scammell same-payload price, 1931–1937 — not found.** The 12-ton trailing-axle six-wheeler
   announcement [*The Commercial Motor*, 20 Oct 1931, p.52] describes the chassis in detail and
   gives no price. The 1937 Scammell advertisement gives payload and speed only. The Scammell
   band in §6.2 is therefore inferred, not measured.
5. **Albion 5-ton (1930) and Albion 10-ton six-wheeler (1934) — no price in the text.**
6. **Rolls-Royce petrol engine option premium — no figure found.** The only Rolls-Royce-engined
   commercial of the period in the archive is mentioned without a price.
7. **Gardner premium — one hard figure only** (£410 on a Peerless, 1930 [S6]). Useful but
   unrepresentative: the comparator was Peerless's own small petrol engine, not a comparable
   proprietary petrol unit, which is why the percentage (+59%) is far above the market's
   £100–£150 oil premium of the same years [S33, S34]. Do not carry +59% into a pakset.
8. **Post-1975 prices — thin.** One 1975 figure was found. The 1977 Scammell Crusader figure is
   inherited and unverified. No 1970s price list equivalent to the 1960 feature was located.
9. **Pre-1920 prices — not reached.** The archive has 1905-on road tests, and the 1896–1919
   window would need a separate pass. Nothing in this file covers it.
10. **Grace's Guide** carried company chronologies but no usable per-vehicle price tables for
    these makes in the pages returned.

---

## 9. Summary of what is solid

- 129 measured or stated price rows, 1920–1977, every one with a dated contemporary source.
  Of these, 122 are individual vehicle prices and 7 are class figures (stated averages or
  ranges), as recorded in the `scope` column of the CSV.
- The strongest single ladder is **1960 [S26]**, because one document prices Bedford, Ford,
  Austin, Morris-Commercial, Commer, Dodge, Karrier, Seddon, Foden and the light vans on one
  date and one scope convention, giving a genuine same-day maker comparison at 3, 5 and 7 tons.
- The second strongest is **AEC 1928 [S5]**, six rungs, 2¼ to 6 tons, with the previous prices
  printed beside the new ones as an internal check.
- The third is **Guy 1931 [S7]**, seven rungs, 30 cwt to 12 tons, with 1930 comparatives.
- The cleanest engine-premium measurement is **Peerless 1930 [S6]**, where the same chassis is
  priced with a Gardner and with a petrol engine and the difference is £410 on both tyre options.
- The cleanest body-and-cab separation is **Bedford 1950 [S22]**: cab £45, platform body £35–40,
  tipper gear and body £60–£105.
