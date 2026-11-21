---
status: draft
verified: New ex-15 @ 209c09a77 (working tree; retirement and comfort pass 2026-11-20)
---
# Citycar asset gaps (work register)

**Covers**: every known gap in `New/citycars/` coverage, with the most popular real models
of the era needed to fill each, evidence figures, priority, and the ordered build queue. This
is a work register for future sessions: pick entries from it when adding citycars. Calibration
context: [citycar-wealth-classes](citycar-wealth-classes.md); parc anchors:
[citycar-parc-anchors](citycar-parc-anchors.md); production method:
[car-batch-production](../graphics/car-batch-production.md); pipeline rules:
[visual-asset-controls](../graphics/visual-asset-controls.md) (all builds are
photograph-based). Figures are UK registrations/sales or GB licensed parc, 2026-11-15
research (DfT VEH0120 via ukmotoring.co.uk; SMMT via AROnline; marque production records).

## Priority key

- **P1** — hard failure: a wealth-class pool is empty at an era where `privatecar.tab`
  gives that class non-zero car access.
- **P2** — entry-level fidelity: the defining cheap cars of an era are absent.
- **P3** — mainstream density: very common cars absent (traffic mix thin).
- **P4** — luxury richness beyond the P1 minimum.
- **P5** — marginal volume or texture.

## A. Hard class-coverage gaps (P1)

Both recorded rows are **CLOSED** as of 2026-11-20. The coverage audit found no historical month
from 1750-01 to 2026-11 in which a class with non-zero ownership had 0 or 1 models.

| Gap | Status and fill models | Evidence |
| --- | --- | --- |
| Very high, 1922–1947 | **CLOSED.** Minimum class-4 pool is 7 models, at 1926: Mercedes Simplex 60, Rolls-Royce Silver Ghost, Wolseley 16/20, Daimler TE30, Vauxhall 30-98, Aston 1½-Litre and Vauxhall 14/40; the 1929–39 Rolls-Royce 20/25, Phantom II, 25/30 and Derby Bentley follow, then the Bentley Mk VI from 1947 | production records; >16 RAC hp classes were <10,000 registrations/yr in 1930 |
| Very high, 1989-2025 | **CLOSED.** Minimum class-4 pool is 11 models (1989): Rolls-Royce Silver Shadow and Silver Spirit, Mercedes W116 and W126, Aston V8 Vantage and Virage, BMW 7-series E23, Renault 25 Phase 1 and Phase 2, Citroen CX Series 2 and Bentley Turbo R; the later XJ, S-Class W140–W222, 7-series E32–G70, Range Rover P38/L322/L405, Bentley Continental GT 2–4, Audi A8 D2–D5 and Lexus LS400 follow | DfT VEH0120 parc series |

One texture gap remains, not a P1 failure: in 1750–1829 classes 3 and 4 have exactly two models
(a closed and an open carriage). The park drag adds a third from April 1830.

## B. Luxury / executive segment (P4, with P1 models above)

| Era | Models (most popular first) | Evidence |
| --- | --- | --- |
| 1920s | Rolls-Royce Silver Ghost (7,874 built 1907–26); Armstrong Siddeley Twenty (8,847, 1926–36 — the pre-war volume car of the band); Bentley 3 Litre (1,622) | production records |
| 1930s | Rolls-Royce 20/25 (3,827); Derby Bentley 3½/4¼ (2,411); Daimler 15–20; Lanchester Eighteen (901); Alvis Speed 20 | production records |
| 1950s | Rover 75/90 P4 (33,267 / 35,903); Jaguar Mk VII (20,908); Silver Cloud I (3,107); Humber Super Snipe Mk IV (17,993); Armstrong Siddeley Sapphire (7,697); Wolseley 6/90; Daimler Conquest; Vanden Plas 4-Litre R (2,509) | production records |
| 1960s | Jaguar Mk 2 (83,976); Rover P5/P5B (~69,000); Jaguar Mk IX (10,009); Silver Shadow (30,057 — highest-volume Rolls); Jaguar Mk X/420G (24,282) | production records |
| 1970s | Ford Granada Mk1/Mk2 (38–52k UK/yr at peak — the actual executive volume leader); Jaguar XJ6 S1/S2 (82,126 / 91,227); Rover P6 (322,302 total); Mercedes W123 | SMMT; production |
| 1980s | Jaguar XJ6 S3 (132,952); Ford Granada Mk3/Scorpio; Rover 800/Sterling (317,126 built; 128,630 licensed 1995 — the decade's largest executive parc); Mercedes W124 ("300": 33,082 licensed 1994) | production; VEH0120 |
| 1990s | BMW 5 E34/E39 (121,954 licensed 1995 → 168,426 in 2000); Mercedes E-Class W210 (87,509 in 2000); Jaguar XJ40/X300; Lexus LS (4,462) | VEH0120 |
| 2000s–20s | BMW 5 F10/G30 (199–230k licensed); Mercedes E W211/W213 (247,289 in 2020 — the biggest prestige parc); Jaguar XF (102,228 in 2020); Audi A8 (7–13k); Porsche Cayenne (39,383 in 2025) | VEH0120 |

## C. Entry-level segment (P2)

| Era | Models (most popular first) | Evidence |
| --- | --- | --- |
| 1920s–30s | Ford Model Y / Popular (£100 car, 157,668 UK, 1932–37 — the 1930s counterpart to the Model T) | production |
| 1950s | **Ford Popular 103E** (>150,000 sold 1953–59; the cheapest new car at £390 — biggest single entry gap); **Austin A30/A35** (222,823 + 353,849 built) | SMMT-era figures; production |
| c.1920–1965 | **Motorcycle and sidecar outfits** (era-specific, below) — the characteristic Very-low motorised transport of the mid-20th century `[USER-DIRECTION:2026-11-15]` | see the outfit table below |
| 1960s–70s | Hillman Imp (42,663 in 1965); Vauxhall Viva HA/HB/HC (76,838 in 1970); Vauxhall Chevette (46,059 in 1980) | SMMT |
| 1980s price floor | Fiat 126 (£899, 1974); Citroën 2CV; Lada Riva; Yugo 45; Škoda Estelle (£2,547, 1985) — what the poorest car-owners actually bought | price-floor series |
| 1980s–2000s | VW Polo (664,223 licensed 2025); Peugeot 205 (50,205 in 1990); Renault Clio (52,576 in 1995); Nissan Micra (566,382 licensed 2000) | SMMT; VEH0120 |
| 2010s–20s | Dacia Sandero (the price floor 2013–25); Kia Picanto / Hyundai i10 / Toyota Aygo X (P5) | price-floor series |

## C1. Motorcycle-and-sidecar outfits, era by era (P2; research 2026-11-15)

No published model-level outfit counts exist before 1994; each row is the best-supported
candidate (catalogue combinations, production figures, fleet use). Parc statistics are
measured: motorcycles 278,600 (1920, outnumbering cars), 491,438 (1925), 690,672 (1928),
505,779 of which **125,499 = 24.8% outfits (1936, peak share)**, 443,651 (1938), 634,536
(1949); outfits **~130,000–150,000 by 1952 (peak count, ≈1 in 7 of the motorcycle parc)**;
motorcycles 1,475,101 (1958). Outfits were ~1 in 10 of new registrations in 1932 (4,876 of
50,072) and 1 in 20 in 1946. Collapse: Watsonian chair output 3,461 (1962) → 637 (1967);
BSA M21 production ended 1963 ("could no longer compete with the Leyland Mini"); Road
Traffic Act 1960 barred learners from machines over 250 cc from 1 Jul 1961.

| Era | Asset to build (recommended) | Support |
| --- | --- | --- |
| 1920s | **BSA 4¼ hp 557 cc side-valve single + BSA Type 1 sidecar — built 2026-11-15** (the register previously said No. 3; the period photographs identify the Type 1) | factory catalogue combination, £95 in 1922 (vs £75 solo); BSA the volume leader |
| 1930s | **BSA 557 cc Sloper + Watsonian Monarch open tourer — built 2026-11-15** | Sloper silhouette; Watsonian the volume chair maker; alt: Norton Big Four 633 + Watsonian Oxford |
| 1940–45 | **Norton Big Four 633 cc WD combination — built 2026-11-15** (driven sidecar wheel) | 4,779 combinations built 1938–41 — the only counted outfit of the period |
| 1946–59 | **BSA M21 600 cc sv + Watsonian Maxstoke (adult + child) — built 2026-11-15** — if only ONE outfit is ever built, this is it (1950–1963) | purpose-built sidecar machine (lugs, low gearing, heavy flywheels, large rear tyre); AA fleet use; production 1937–63; Maxstoke = the literal family configuration |
| 1960–65 | BSA M21 + Watsonian Monaco (or Triumph 6T 650 + Monaco) — built 2026-11-15 | documented 1958–59 body range; late lower silhouette |

Rendering/behaviour notes: sidecar on the **nearside (left)**; a typical outfit is a 500–650 cc
low-revving side-valve single (or 650 twin late) with a stiff lugged frame, girder/telescopic
fork, and a bulbous-nosed chair with small screen and nearside door. Provisional game values:
capacity 2 adults + 1 child; ~45–50 mph with the chair; comfort below the BMC Mini's 40/390
(far below — open chair, exposed rider); classes `0,1`. Folklore to avoid when modelling: the
M20 was NOT the sidecar machine (it was built mostly without sidecar lugs — the M21 was);
"one in four BSAs" is a 1920s advertising slogan, not a measured share.

## D. Mainstream density (P3) — the remaining "absent but relevant" set

| Model | Evidence |
| --- | --- |
| Vauxhall Cavalier (Mk1–Mk3) | 1,201,693 licensed 1995; UK best-seller class rival to the Escort |
| Vauxhall Astra | 1,086,005 licensed 2000; 2,845,357 UK sales 1965–2014 (SMMT cumulative) |
| VW Golf | 626,880 licensed 2000 → 981,882 in 2025 |
| VW Beetle | the iconic 1950s–70s small car; large UK parc |
| Nissan Micra / Peugeot 206 | 566,382 / 567,307 licensed (2000 / 2005) |

## Build order (2026-11-15)

The sequence in which to work the register. Evidence lives in the section named in the last
column; this table gives order and scope only. One brief per car, or per generation family
that shares a body shell; the production method is
[car-batch-production](../graphics/car-batch-production.md). `[USER-DIRECTION:2026-11-15]`

| Order | Models | Reason for position | Evidence |
| --- | --- | --- | --- |
| 1 | Vauxhall Cavalier, Mk1–Mk3 as separate shells — **built 2026-11-16** (four colourways each) | The user's next four, and the largest missing mainstream UK parc | D |
| 2 | Vauxhall Astra, Mk1–Mk4 first, later marks after | Same; the long-running Escort-class rival | D |
| 3 | VW Beetle (one model; the 1998 New Beetle is a separate car) | Same; the defining small car of the 1950s–70s | D |
| 4 | VW Golf, Mk1–Mk4 first, later marks after | Same; the Escort-class rival of the 1980s–2000s | D |
| 4a | **Ford Sierra, Mk1–Mk3 — every major mark, each with several realistic colourways** (priority insert 2026-11-15) | The comfort calibration anchor (120/510) and a major 1980s–90s parc; build immediately after the user's four, as a family like the Fiesta/Corsa runs | D, and [citycar](citycar.md#comfort-calibration) |
| 4b | **Audi A4 B5, B7, B8 and B9 — complete the family** (priority insert 2026-11-16; the B6 is already in the tree) | The B6 was the first car built with the MCP pipeline; the family should be complete, with authentic colours for each mark | [citycar](citycar.md) |
| 5 | Rolls-Royce 20/25 | Closes the Very-high gap 1925–47 at its largest-volume model | A |
| 6 | Derby Bentley 3½/4¼ | Same gap, second volume | A |
| 7 | Bentley Mk VI | Same gap for 1946–47 | A |
| 8 | Jaguar XJ (XJ40/X300/X308 as one shell family) | Closes the Very-high gap 1989–2025 at its largest parc | A |
| 9 | Mercedes S-Class W140 and W220 | Same gap, prestige volume | A |
| 10 | Range Rover P38, L322 and L405 | Same gap, largest non-saloon parc | A |
| 11 | BMW 7-series E38 and E65 | Same gap | A |
| 12 | Bentley Continental GT | Same gap, top of the band | A |
| 13 | Ford Popular 103E | Largest single entry-level gap | C |
| 14 | Austin A30/A35 (one shell) | The other 1950s entry car | C |
| 15 | BSA M21 600 cc with Watsonian Maxstoke sidecar — **built 2026-11-15** | The characteristic Very-low vehicle of 1946–65; if only one outfit is built, this one | C1 |
| 16 | Ford Model Y / Popular | The 1930s entry car | C |
| 17 | Hillman Imp; Vauxhall Viva HA/HB/HC; Vauxhall Chevette | 1960s–70s entry and lower-medium volume | C |
| 18 | Citroën 2CV; Fiat 126; Lada Riva; Škoda Estelle; Yugo 45 | The 1970s–80s price floor | C |
| 19 | Peugeot 205 and 206; Renault Clio; Nissan Micra; VW Polo | Mainstream density 1980s–2000s | C, D |
| 20 | Rover 25 and 45 | British mainstream density of the 1990s–2000s | D |
| 21 | Jaguar Mk 2; Rover P5/P5B; Ford Granada Mk1/Mk2; Rolls-Royce Silver Shadow; Jaguar XJ6 S1–S3; Mercedes W123 and W124; BMW 5 E34/E39 | Executive richness through the 1960s–90s | B |
| 22 | Dacia Sandero; Kia Picanto / Hyundai i10 / Toyota Aygo; Porsche Cayenne; Audi A8; Lexus LS | Marginal volume and recent texture | B, C |

Later marks of the Cavalier, Astra and Golf are complete. The first tranche is closed, and the
second tranche closed with orders 34–51 on 2026-11-20; the tables below record the build history.

### Build order, second tranche (2026-11-16)

User-specified families. Sequenced to close the open documented rows first, then to work from the
largest missing parc down to the smallest, with the hardest and lowest-volume family last. The
generations to build for each family are listed in section G; the sequence is here.
`[USER-DIRECTION:2026-11-16]`

| Order | Family | Reason for position |
| --- | --- | --- |
| 23 | Porsche Cayenne, Audi A8 D3, Lexus LS400 — **all installed 2026-11-16** | Order 22 closed |
| 24 | Section F, 1900–1918 and 1919–1939 rows — **closed 2026-11-17**: Silver Ghost, Simplex 60, Vauxhall 30-98, Phantom II, 25/30, Rover 12 P2, Rover 14 P2, Argyll 15/30 | The last unbuilt section F rows |
| 25 | Section F, 1940–1959 and 1960–1979 class 4 — **closed 2026-11-17**: Bentley S1, Silver Cloud I, Bentley R-Type, Silver Cloud II, Mercedes W116. Silver Shadow II skipped because the existing Silver Shadow already spans 1965–1980 | The last two open luxury rows |
| 26 | Peugeot 206 — **installed 2026-11-17** | The last open entry in order 19 |
| 27a | Wolseley 16/20, Sunbeam 12/16, Rover Twelve — **installed 2026-11-17** | Closes the section F 1900–1918 class-3 row |
| 27b | Singer Ten, Humberette, Standard 9.5, GWK cyclecar (optional Daimler TE30 — **TE30 built**) | The cheap end of 1912–20, which the register had not recorded |
| 27c | De Dion-Bouton Type V - **installed 2026-11-17**; Peugeot Type 69 Bébé - **installed**; Star 7 hp - **installed 2026-11-17** (4 objects) | The imported and cheap end of 1900-10; evidence, photographs and exclusions in [citycar-pre-1920-audit](citycar-pre-1920-audit.md) |
| 28 | Metro; Rover 200/400/800/75; Jaguar S-Type | The largest missing British mainstream block |
| 29 | BMW 3, 5 and 7 — **closed 2026-11-17**: 3-series E21, E30, E46, E90, G20; 5-series E12, E28, E60, G30, G60; 7-series E23, G11, G70, around the existing E32, E34, E36, E38, E39, E65, F01, F10 and F30. 52 objects, pak 870 → 922 | The largest missing import family, with existing marks to extend |
| 30 | Datsun/Nissan: Cherry, Stanza, Sunny, Bluebird, Primera, Qashqai, Juke, Note | Second largest missing import family |
| 31 | Toyota — **closed 2026-11-18 except the Yaris XP130**: Prius XW20, XW30, XW50, XW60; Yaris XP10, XP90, XP210; Corolla E100, E110, E120. Ten models, 40 objects, pak 1,018 → 1,058. The XP130 is built and held for a user decision on its outline; the Corolla E140 is dropped because Toyota GB never sold it in Britain | Third |
| 32 | Renault - **closed 2026-11-19**: 15, 17, 19 phases 1 and 2, 21 phases 1 and 2, 25 phases 1 and 2, Megane I-IV and the Megane E-Tech (the British Megane V). Thirteen models, 52 objects, pak 1,058 -> 1,114 | Fourth |
| 33 | Citroen - **closed 2026-11-19**: DS 1955-62 (open lamps), DS 1962-75 (Series 3 canopy), CX Series 1, CX Series 2. Four models, 16 objects. The Series 2 DS nose of 1962-67 is not separately represented | Smallest import block |
| 34 | Aston Martin - **CLOSED 2026-11-20**: all 22 generations installed, 88 objects, pak 1,222 → 1,234. Pre-war 1½-Litre, International, Ulster, 2-Litre and 15/98; post-war DB2, DB Mk III, DB4, DB5, DB6, DBS, V8 Vantage, Virage, DB7, Vanquish, DB9, Vantage 2005, DBS V12, Rapide, DB11, Vantage 2018 and DBX | Lowest volume and hardest shapes; taken last so it cannot displace coverage work |
| 35 | Motorcycle riders for the five outfits — **closed 2026-11-20**: riders and passengers added to all five, 80 sprites replaced, no new objects; names, dates and colours unchanged | Completes the outfit block without new shells |
| 36 | Glazing re-render of the pre-rule sprites — **complete 2026-11-17** | Graphics repair, no new objects |
| 37 | Triumph — **closed 2026-11-18**: 2000 Mk1 (re-render), 2000 Mk2, 2500, 1500, Spitfire 1500, Stag | British executive and sports coverage |
| 38 | Rover: original 75 and 60, P3, P4 range, P5, P6 - **CLOSED 2026-11-20**: 12 models, 48 objects, pak 1,294 → 1,302. P3; P4 60/90/95/100/105R/110; P5 3-Litre; P5 coupé and P5B coupé (**four-door coupés** with the lowered roofline, as Rover built them, not two-doors); P6 2200/3500. The original 75 is already `rover-p4-75` | The missing Rover executive line, 1948-1977; closes section F rows and the P4/P5/P6 families |
| 39 | Ford: Pilot, Consul, Zephyr/Zodiac, Granada Mk3 - **CLOSED 2026-11-20**: 14 models, 55 objects, pak 1,317 → 1,337. Pilot; Consul Mk I/II, Classic, Capri; Zephyr and Zodiac Mk I-IV; Granada Mk III hatchback | The missing 1947-72 Ford executive and six-cylinder line, plus the last Granada |
| 40 | Wolseley: 8 hp tonneau, Ten, 14/60, 18/85, 21/60, Hornet (1930s and Mini), Wasp - **CLOSED 2026-11-20**: 8 models, 32 objects, pak 1,353 → 1,369. The 21/60 is the real 1929-35 car and the Wasp the real 1935-36 car; the 1930s Hornet is the photographed open two-seater | The pre-war and BMC-era Wolseley line around the existing 16/20 and 6/80 |
| 41 | Hillman Minx: pre-war, post-war Mk I-VIII, Series I-V, Arrow - **CLOSED 2026-11-20**: 4 models, 16 objects, pak 1,369 → 1,385. The post-war car is the Mk IV and the Series car the Series V, as the packs photograph; the other marks are not separately represented | The Rootes volume car, 1931-1970 |
| 42 | BMW: i3, 1-series, X5, iX3 - **CLOSED 2026-11-20**: 10 models, 40 objects, pak 1,417 → 1,425. i3; 1-series E87/F20/F40/F70; X5 E53/E70/F15/G05; iX3. The F15/G05/iX3 were built on the fallback builder and carry simplified-shape notes in their headers | Extends the existing 3/5/7 register into the compact, SUV and electric ranges |
| 43 | Audi: A6 C4-C8, A8 D2/D4/D5 - **CLOSED 2026-11-20**: 8 models, 32 objects, pak 1,441 → 1,457. All carry simplified-shape notes; the A6 C6/C7 and A8 D4/D5 are distinguished mainly by grille and lamp forms | Extends the existing A4 and A8 D3 register |
| 44 | Jaguar XF; Land Rover Discovery 1-5; Lexus ES - **CLOSED 2026-11-20**: 8 models, 32 objects, pak 1,477 → 1,489 | Executive, SUV and prestige imports |
| 45 | Toyota Aygo X; Hyundai i10 Mk2/Mk3; Kia Sportage 1-5; Fiat Panda 1-3; VW Up! - **CLOSED 2026-11-20**: 12 models, 48 objects, pak 1,489 → 1,537. Aygo X; i10 Mk2 and Mk3; Sportage 1-5; Panda 1-3; Up! | Entry-level and compact-SUV density, 1980-2025 |
| 46 | Porsche Macan Electric; Tesla Model 3 and Model Y - **CLOSED 2026-11-20**: 3 models, 12 objects, pak 1,537 → 1,549. The Macan is the XAB electric car only; the Model 3 is the pre-facelift car and the Model Y the pre-Juniper car | The modern electric and performance-SUV texture |
| 47 | Jaecoo 5, 7 and 8 - **CLOSED 2026-11-20**: 3 models, 12 objects, pak 1,549 → 1,561. The Jaecoo 5 is the petrol 1.6T only; the E5 has a different nose and is not represented | The newest Chinese entrants to the UK market |
| 48 | Norton 16H outfit; BSA M20 outfit - **CLOSED 2026-11-20**: 2 models, 2 objects, pak 1,561 → 1,563. Both adapted from the existing outfit masters. No period photograph of either exact combination exists, so the chairs and mounts are estimates and each header records it | The two remaining period outfits identified by the user |
| 49 | Tesla Model S; Nissan Micra K10, K12, K13, K14, K15; Fiat Grande Panda Electric; Datsun Cherry F10 coupé; Datsun 1200 (B110); Datsun 120Y (B210); Nissan Sunny B11 and N14 - **CLOSED 2026-11-20**: 12 models, 48 objects, pak 1,563 → 1,611. The F10 is the coupé, the only F10 body sold in Britain (from 1977, as the 120A); the B11 is the four-door saloon, the five-door hatch role having been the N12 Cherry; the N14 is the five-door hatchback; the K15 and the Grande Panda Electric are current cars | The missing Micra generations, the missing Cherry and Sunny generations, the Model S and the electric Grande Panda |
| 50 | Bentley Continental GT 2-4; BYD Dolphin, Atto 3, Seal, Sealion 7; Vauxhall Wyvern/Velox/Cresta; Carlton; Vectra; Zafira; Mokka; Viva HB/HC/2015; Ford Galaxy Mk2; Vauxhall pre-war A-type through 20-60 - **CLOSED 2026-11-20**: 36 models, 144 objects, pak 1,611 → 1,755. There is no Vauxhall Vectra A (the 1988-95 UK car was the Cavalier Mk3, already in the tree) and no Carlton Mk3; the five Velox/Cresta shells each carry both names; the Bentley gen 4 is a 4.0 V8 plug-in hybrid | The modern high end, the Chinese electric entrants, and the missing Vauxhall and Ford families |
| 51 | Ford Puma (1997 coupé and 2019 crossover); Austin Allegro - **CLOSED 2026-11-20**: 3 models, 12 objects, pak 1,755 → 1,767. The two Pumas are unrelated cars sharing only the name; the Allegro is the Series 2 four-door saloon | Two Fords that share a name and nothing else, plus the Allegro; none was in the tree |


Do not build a generation that is already represented by a declared stand-in without first
ratifying that stand-in (the E494A Anglia and the Morris Cowley; see section E).

## Renders without objects

Complete eight-view image sets exist in `New/citycars/images/` with no object referencing them:
`morris-oxford-3-blue_*` and `rover-sd1-yellow_*`, both added with their models in 2017. Each
is either a colourway to define, with the colour-share and weight justification the colour rule
requires, or a superseded set to delete. User decision outstanding.
`[CODE New @ 228dc21d1, 278e70310]`

## F. Affluent and luxury coverage (class 3 and class 4)

Research 2026-11-16 (DfT VEH0120/VEH0124 for 1994+, SMMT/AROnline, production records).
The aim is at least three class-3 and three class-4 models per era, overlapping. The evidence
does **not** support "several on an ordinary street" for early prestige cars; weights must stay
low even where three models are added. Full evidence and strength ratings are recorded in the
session research return of 2026-11-16.

| Era | Class 4 (very high) — strongest first | Class 3 (high) — strongest first |
| --- | --- | --- |
| 1900–1918 | Silver Ghost; Mercedes Simplex 60 hp; Vauxhall 30-98 — the last two are the approved substitutes for the unverifiable Daimler 38 hp and Napier 60 hp | Rover Twelve (Clegg); Sunbeam 12/16; Wolseley 16/20 — all three photographed and buildable |
| 1919–1939 | Rolls-Royce Twenty; Phantom II; 25/30 | Rover Twelve P1/P2; Daimler Fifteen; Rover Fourteen |
| 1940–1959 | Bentley S1; Silver Cloud I; Bentley R-Type | Rover P4 75; Humber Hawk VI/VIa; Wolseley 6/80 |
| 1960–1979 | Silver Shadow I; Silver Cloud II; Silver Shadow II; Mercedes W116 (verify UK) | Rover P6; Jaguar Mk2; Rover P5B |
| 1980–1999 | BMW 7 E32; Bentley Turbo R; Silver Spirit; Mercedes W126 (verify) | BMW 3 E36; BMW 5 E34; Rover 800; Mercedes W124 |
| 2000–2025 | Mercedes S W222; S W221; BMW 7 F01/F02 | BMW 3 F30; Mercedes C W204; BMW 5 F10 |

Priorities: the strongest-evidenced additions are the 1940s–70s class-3 cars (Rover P4 75,
Humber Hawk, Wolseley 6/80, Rover P6, Jaguar Mk2, Rover P5B), the 1980s–2000s BMW/Mercedes/Rover
classes 3, and the modern S-Class and 7-series. Early prestige models are representative rather
than proven common and should carry very low weights. Every row is subject to the same
photograph-first pipeline and the colour rule as the rest of the catalogue.

The pre-1920 market outside these two rows is audited in
[citycar-pre-1920-audit](citycar-pre-1920-audit.md): section F covers only the affluent end, and
the larger gap is the light-car and cyclecar market of 1912–1920, which the register did not
record.

## G. Second tranche — user-specified families (2026-11-16)

**Covers**: the generation scope of every family added to the register on 2026-11-16. The
sequence is the second tranche of the build order. "All major versions" means every UK-market
generation that formed a distinct body shell; trim and engine variants are not separate objects,
but pre- and post-facelift noses are where the brief says so. Each generation is one brief with
period colourways, both comfort fields and the `class=` values of its wealth band, as everywhere
else in the catalogue. `[USER-DIRECTION:2026-11-16]`

| Family | Generations to build (UK-market shells) | Already in the pak |
| --- | --- | --- |
| BMW 3-series | E21 1975–83; E30 1982–94; E46 1998–2005; E90 2005–12; G20 2019– | E36, F30 |
| BMW 5-series | E12 1972–81; E28 1981–88; E60 2003–10; G30 2017–23; G60 2023– | E34, E39, F10 |
| BMW 7-series | E23 1977–86; G11 2015–22; G70 2022– | E32, E38, E65, F01 |
| Datsun Cherry | E10 1970–74; F10 1974–79 (coupé 120A from 1977); N10 1978–82; N12 1982–86 | E10, F10, N10, N12 |
| Datsun/Nissan Stanza | T11 1977–82, built only if research confirms a UK sale | T11 |
| Datsun/Nissan Sunny | B110 1971–73; B210 1973–77; B310 1977–81; B11 1982–86; N13 1986–91; N14 1991–95 | B110, B210, B310, B11, N13, N14 |
| Nissan Micra | K10 1983–92; K11 1992–2003; K12 2003–10; K13 2010–17; K14 2017–23; K15 2025– | K10, K11, K12, K13, K14, K15 |
| Nissan Bluebird | 910 1980–84; T72 1984–86; T12 1986–90 | none |
| Nissan Primera | P10 1990–96; P11 1996–2002; P12 2002–07 | none |
| Nissan Qashqai | J10 2007–14; J11 2014–21; J12 2021– | one J10-era shell, to be re-rendered as the J10 |
| Nissan Juke | F15 2010–19; F16 2019– | none |
| Nissan Note | E11 2006–13; E12 2013–17 | none |
| Austin/Rover Metro | Mk2 1984–90; Rover Metro 1990–94; Rover 100 1994–98 | one 1980 Metro shell |
| Rover 200 | SD3 1984–89; R8 1989–95; R3 1995–99 | none |
| Rover 400 | R8 1990–95; HH-R 1995–99 | none |
| Rover 800 | XX 1986–91; R17 1991–99 | one generic 1986–99 shell, retained |
| Rover 75 | 1999–2005 | none |
| Jaguar S-Type | 1963–68 original; 420 1966–70; X200 1998–2008 | none |
| Toyota Yaris | XP10 1999–2005; XP90 2005–11; XP130 2011–20; XP210 2020– | none |
| Toyota Prius | XW10 1997–2003; XW20 2003–09; XW30 2009–15; XW50 2015–22; XW60 2023– | none |
| Toyota Corolla | E90 1987–92; E100 1991–97; E110 1997–2002; E120 2002–07; E140 2007–13 | none |
| Renault 15/17 | 15 1971–79; 17 1972–79 | none |
| Renault 19 | Phase 1 1988–92; Phase 2 1992–96 | none |
| Renault 21 | Phase 1 1986–89; Phase 2 1989–94 | none |
| Renault 25 | Phase 1 1984–88; Phase 2 1988–92 | none |
| Renault Megane | I 1995–2002; II 2002–08; III 2008–16; IV 2016–22; V 2022– | none |
| Citroën DS | 1955–62; 1962–75 (facial change) | none |
| Citroën CX | Series 1 1974–85; Series 2 1985–91 | none |
| Aston Martin | pre-war 1½-Litre 1922–25, International 1929–32, Ulster 1934–36, 2-Litre 1936–39, 15/98 1937–39; post-war DB2 1950–53, DB Mk III 1957–59, DB4 1958–63, DB5 1963–65, DB6 1965–70, DBS 1967–72, V8 Vantage 1977–89, Virage 1989–94, DB7 1994–2003, Vanquish 2001–07, DB9 2004–16, Vantage 2005–17, DBS V12 2007–12, Rapide 2010–20, DB11 2016–23, Vantage 2018–, DBX 2020– | none |

Decisions taken when the tranche was set:

- **Existing generic shells — user direction 2026-11-16.** Where a family already has one
  generic shell, the existing objects keep their names and dates so that savegames stay valid;
  their graphics are replaced so that they represent one specific mark of the family, and the
  remaining marks are added as new objects. This applies to the Rover 800 (the existing objects
  become the XX of 1986–91, with the R17 of 1991–99 added new) and to the Nissan Qashqai (the
  existing objects become the J10 of 2007–14, with the J11 and J12 added new).
- **UK sale rule — user direction 2026-11-16, amended 2026-11-20.** A generation is built only
  where research establishes that it was sold in Britain, OR that its British sale has been
  announced with a date. The amended form (2026-11-20): a car announced for the UK but not yet
  on sale is included, with an intro date set to the announced sale date rather than omitted.
  A car with no UK announcement at all is still excluded, and the doubt is recorded in Open
  questions rather than resolved by assumption.
- **Rover 75.** Added because the 200, 400 and 800 all ended in 1999, so the 75 is the model that
  carries the Rover range into the early 2000s.
- **Rover 100.** The Rover 100 ended in 1998, not in the 2000s; it was replaced by the 200. The
  Metro block therefore stops at 1998.
- **Jaguar.** The 420 is built with the original S-Type because it shares the body and is the
  better-known version. The X200's 2004 facelift is a colour run on the same master, not a second
  shell, because only the nose and lamps changed.
- **Renault.** The 17 is built with the 15: same body, and the 17 is the one with the UK
  following.
- **Pre-1920.** An audit first. No model is built for that era until the research identifies the
  gap and references are found; the Daimler 38 hp and Napier 60 hp failures are the precedent.

## H. Third tranche — user-specified families (2026-11-19)

**Covers**: the generation scope of the families added to the register on 2026-11-19, orders 38-48.
The same rules apply as in section G: one object per colourway, one brief per distinct UK shell,
trim and engine variants only where the photographs show a different outline, and the UK sale rule.
Dates below are the planning window; every one is confirmed or corrected by the per-model research
before the brief is written. `[USER-DIRECTION:2026-11-19]`

| Family | Generations to build (UK-market shells) | Already in the pak |
| --- | --- | --- |
| Rover 75 and 60 (original) | P4 75 1949-59 (the original 75); P4 60 1953-59 | `rover-p4-75` (1949-64) — the 75 is already represented and is **not** rebuilt; the 60 is new |
| Rover P3 | 60 and 75 1948-49 | none |
| Rover P4 | 60 1953-59; 90 1954-59; 95 1962-64; 100 1960-62; 105R 1956-58 (the 105S shares the shell); 110 1962-64 | `rover-p4-75` only |
| Rover P5 | 3-Litre saloon 1958-67 (Mk I-III noses); 3-Litre coupé 1962-67; P5B coupé 1967-73 | `rover-p5b` (the P5B saloon, 1967-73) |
| Rover P6 | 2200 1973-77; 3500 1968-77 (3500S shares the shell) | `rover-p6` (the 2000, 1963-77) |
| Ford Pilot | 1947-51 V8 | none |
| Ford Consul | Mk I 1950-56; Mk II 1956-62; Classic 1961-63; Capri 1961-64 | `ford-cortina` (the Consul Cortina, 1962) |
| Ford Zephyr/Zodiac | Zephyr Mk I 1950-56 and Zodiac Mk I 1953-56; Zephyr/Zodiac Mk II 1956-62; Zephyr/Zodiac Mk III 1962-66; Zephyr/Zodiac Mk IV 1966-72 | none |
| Ford Granada | Mk III 1985-94 (sold as Scorpio from 1994) | `ford-granada-mk1`, `ford-granada-mk2` |
| Wolseley 8 hp | 2-cylinder tonneau, c.1902-06 — the exact model and dates to be established by research | none |
| Wolseley Ten | 1939-48 | none |
| Wolseley 14/60 | 1938-48; the narrower 12/48 shell, shared 2.654 m wheelbase | none |
| Wolseley 18/85 | 1938-48; shared 2.654 m wheelbase with the 14/60 and 16/65 | none |
| Wolseley 21/60 | **1929-35, not 1938-48** (research correction 2026-11-20: the 21/60 is a 2,677 cc six of 1929-35; from 1936 the large six was the "21" and the 1938-48 large Wolseley was the 25 hp) | none |
| Wolseley Hornet | 1930-36 six-cylinder; 1961-69 Mini-based | none |
| Wolseley Wasp | **1935-36, not 1955-56** (research correction 2026-11-20: 1,069 cc, 5,815 built in 1935-36) | none |
| Hillman Minx | pre-war 1931-35; post-war Mk I-VIII 1947-57; Series I-V 1956-65; Arrow 1967-70 | none |
| BMW i3 | 2013-22 | none |
| BMW 1-series | E87 2004-11; F20 2011-19; F40 2019-24; F70 2024- | none |
| BMW X5 | E53 1999-2006; E70 2006-13; F15 2013-18; G05 2018- | none |
| BMW iX3 | G08 2020- | none |
| Audi A6 | C4 1994-97; C5 1997-2004; C6 2004-11; C7 2011-18; C8 2018- | none |
| Audi A8 | D2 1994-2002; D4 2010-17; D5 2017- | `audi-a8-d3` |
| Jaguar XF | X250 2007-15; X260 2015-24 | none |
| Land Rover Discovery | 1 1989-98; 2 1998-2004; 3 2004-09; 4 2009-16; 5 2017- | `land-rover-series` |
| Lexus ES | XZ10 2018- — the first ES sold new in Britain; earlier generations were not UK models | `lexus-ls400` |
| Toyota Aygo X | 2022- | `toyota-aygo` (the 2005-14 Aygo) |
| Hyundai i10 | Mk 2 2013-19; Mk 3 2019- | `hyundai-i10` (Mk 1) |
| Kia Sportage | 1 1993-2004; 2 2004-10; 3 2010-15; 4 2015-21; 5 2021- | none |
| Fiat Panda | 1 1980-2003 (UK imports to the mid-1990s); 2 2003-12; 3 2012- | none |
| VW Up! | 2011-23 | none |
| Porsche Macan Electric | 2024- (the petrol Macan of 2014-23 is a different car and is not in this order) | `porsche-cayenne` |
| Tesla Model 3 | 2017- (the 2023 Highland facelift is a nose and tail change on the same shell) | none |
| Tesla Model Y | 2020- | none |
| Jaecoo 5 | 2025- | none |
| Jaecoo 7 | 2024- | none |
| Jaecoo 8 | 2025- | none |
| Norton 16H outfit | 1937-45, 490 cc side-valve single with sidecar | none |
| BSA M20 outfit | 1939-45, 500 cc side-valve single with sidecar | none |

Decisions taken when the tranche was set:

- **The original Rover 75 is not rebuilt.** `rover-p4-75` already represents the 1949-59 P4 75.
  The order adds the 60 and the rest of the P4 range around it, so the family reads as the real
  range rather than as one model.
- **Zodiac and Zephyr share a shell within each mark.** The Zodiac is a trim and grille variant of
  the Zephyr of the same mark; the four Zodiacs are built as variants of the four Zephyr masters,
  not as independent bodies. The same applies to the Rover P4 105S (the 105R shell with a manual
  gearbox) and the P6 3500S (the 3500 shell).
- **One body per generation.** "All major subtypes" means every distinct UK-market generation or
  mark, not every body style of one generation. The volume body is modelled: saloon for the Audi
  A6 and A8, Jaguar XF, Rover P4/P5/P6 and Ford Consul/Zephyr/Zodiac; five-door for the Land
  Rover Discovery, BMW 1-series and Kia Sportage; hatchback for the Fiat Panda and VW Up!. Avant,
  estate, convertible, coupé and three-door variants that share the generation's principal shell
  are not separate objects, in line with the existing A4, Golf and 3-series runs. A body style
  that is a different shell (the Rover P5 coupé, the Ford Consul Capri, the BMW 1-series E82
  coupé) is listed separately where the order names it.
- **The BSA M20 outfit is built as the user directed, with the caveat recorded.** The M20 was
  built mostly without sidecar lugs; the purpose-built outfit of the period was the M21, which is
  already in the tree. The M20 outfit is a period-correct combination nonetheless, and its `.dat`
  header records the distinction.
- **Wolseley 21/60 and Wasp dates corrected.** The research on 2026-11-20 found that the 21/60
  is 1929-35, not 1938-48, and that the Wasp is 1935-36, not 1955-56. The order builds the real
  cars; the dates in the user's list were planning placeholders and the research governs. The
  1938-48 large Wolseley is the 25 hp, not the 21/60, and is not part of this order.
- **Jaecoo.** The three models are new to Britain in 2024-25; the research must establish the
  exact UK launch dates and the body each model carries before any build.
- **Lexus ES.** Only the XZ10 is a UK model. Building the earlier ES generations would break the
  UK sale rule and is excluded.

## E. Known and deferred (see also [pakset-roadmap](../pakset-roadmap.md))

- Re-do photograph-based geometry for the text-derived families (deferred by the user):
  Ford Fiesta Mk1–Mk7, BMC1100, Ford Escort Mk2, Vauxhall Nova/Corsa B–F.
- Ratification pending: Morris Cowley represented by the Oxford twins; E04A/E494A Anglia
  represented by FordPrefectEarly.
- RangeRover retire dates settled 2026-11-20: all five colourways carry a staggered 1998–2005
  road tail, replacing the single 1988 date on the Blue colourway.

## Open questions

- **Datsun/Nissan Stanza.** Whether the T11 was sold in Britain. Build only on positive evidence;
  otherwise the Stanza drops out of the block.
- **Pre-1920.** The audit's outcome: which classes have no model at all before 1920, and whether
  the existing veteran cars (Austin, Morris, Rover, Ford, Citroën) already cover the bands.
- **Re-rendered shells.** Whether the re-rendered Rover 800 (XX) and Nissan Qashqai (J10) should
  also have their `intro_year` and `retire_year` narrowed to the mark they now represent. The
  dates are savegame-relevant, so they are left alone until the user decides.

