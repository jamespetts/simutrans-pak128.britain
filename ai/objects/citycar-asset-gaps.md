---
status: draft
verified: New ex-15 @ f05e52352 (working tree; second tranche added 2026-11-16)
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

| Gap | Fill models (most popular first) | Evidence |
| --- | --- | --- |
| Very high, 1922–1947 | Rolls-Royce Twenty (2,940 built 1922–29) or 20/25 (3,827, 1929–36, the inter-war best-seller); Bentley 3½/4¼ Derby (1,177 + 1,234); Daimler Light Twenty (877) or DB18; Bentley Mk VI (5,368, 1946–52) for 1946–47 | production records; >16 RAC hp classes were <10,000 registrations/yr in 1930 |
| Very high, 1989–2025 | Jaguar XJ (XJ40/X300/X308: 87,374 licensed 1995 → 22,384 in 2025); Mercedes S-Class W126/W140/W220/W221 (22–29k licensed); Bentley Continental GT (13,216 in 2025); Range Rover P38/L322/L405 (+ Sport: 142,546 licensed 2025); BMW 7-series (16–33k) | DfT VEH0120 parc series |

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
capacity 2 adults + 1 child; ~45–50 mph with the chair; comfort below the BMC Mini's 40/240
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
| 4a | **Ford Sierra, Mk1–Mk3 — every major mark, each with several realistic colourways** (priority insert 2026-11-15) | The comfort calibration anchor (120/360) and a major 1980s–90s parc; build immediately after the user's four, as a family like the Fiesta/Corsa runs | D, and [citycar](citycar.md#comfort-calibration) |
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

Later marks of the Cavalier, Astra and Golf are complete. The remaining open items are the tail of
order 22, the section F prestige rows, and the second tranche below.

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
| 27c | De Dion-Bouton Type V — **installed 2026-11-17**; Peugeot Type 69 Bébé — **installed**; Star 7 hp — in progress | The imported and cheap end of 1900–10; evidence, photographs and exclusions in [citycar-pre-1920-audit](citycar-pre-1920-audit.md) |
| 28 | Metro; Rover 200/400/800/75; Jaguar S-Type | The largest missing British mainstream block |
| 29 | BMW 3, 5 and 7 — **closed 2026-11-17**: 3-series E21, E30, E46, E90, G20; 5-series E12, E28, E60, G30, G60; 7-series E23, G11, G70, around the existing E32, E34, E36, E38, E39, E65, F01, F10 and F30. 52 objects, pak 870 → 922 | The largest missing import family, with existing marks to extend |
| 30 | Datsun/Nissan: Cherry, Stanza, Sunny, Bluebird, Primera, Qashqai, Juke, Note | Second largest missing import family |
| 31 | Toyota Yaris, Prius, Corolla | Third |
| 32 | Renault 15/17, 19, 21, 25, Megane | Fourth |
| 33 | Citroën DS and CX | Smallest import block |
| 34 | Aston Martin | Lowest volume and hardest shapes; taken last so it cannot displace coverage work |


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
| Datsun Cherry | E10 1970–74; F10 1974–78; N10 1978–82 | none |
| Datsun/Nissan Stanza | T11 1977–82, built only if research confirms a UK sale | none |
| Datsun Sunny | B310 1977–81; N12 1981–86; N13 1986–91; N14 1990–95 | none |
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
- **UK sale rule — user direction 2026-11-16.** A generation is built only where research
  establishes that it was sold in Britain. Any doubt about UK availability excludes it; the doubt
  is recorded in Open questions rather than resolved by assumption.
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

## E. Known and deferred (see also [pakset-roadmap](../pakset-roadmap.md))

- Re-do photograph-based geometry for the text-derived families (deferred by the user):
  Ford Fiesta Mk1–Mk7, BMC1100, Ford Escort Mk2, Vauxhall Nova/Corsa B–F.
- Ratification pending: Morris Cowley represented by the Oxford twins; E04A/E494A Anglia
  represented by FordPrefectEarly.
- RangeRover retire date (1988) may be too early — see
  [citycar-wealth-classes](citycar-wealth-classes.md) open questions.

## Open questions

- **Datsun/Nissan Stanza.** Whether the T11 was sold in Britain. Build only on positive evidence;
  otherwise the Stanza drops out of the block.
- **Pre-1920.** The audit's outcome: which classes have no model at all before 1920, and whether
  the existing veteran cars (Austin, Morris, Rover, Ford, Citroën) already cover the bands.
- **Re-rendered shells.** Whether the re-rendered Rover 800 (XX) and Nissan Qashqai (J10) should
  also have their `intro_year` and `retire_year` narrowed to the mark they now represent. The
  dates are savegame-relevant, so they are left alone until the user decides.

