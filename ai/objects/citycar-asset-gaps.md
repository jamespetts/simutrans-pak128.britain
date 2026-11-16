---
status: draft
verified: New ex-15 @ cfd36f1b3
---
# Citycar asset gaps (work register)

**Covers**: every known gap in `New/citycars/` coverage, with the most popular real models
of the era needed to fill each, evidence figures, and priority. This is a work register for
future sessions: pick entries from it when adding citycars. Calibration context:
[citycar-wealth-classes](citycar-wealth-classes.md); parc anchors:
[citycar-parc-anchors](citycar-parc-anchors.md); pipeline rules:
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
| 1920s | **BSA 4¼ hp 557 cc side-valve single + BSA No. 3 sidecar** | factory catalogue combination, £95 in 1922 (vs £75 solo); BSA the volume leader |
| 1930s | **BSA 557 cc Sloper + Watsonian Monarch open tourer** | Sloper silhouette; Watsonian the volume chair maker; alt: Norton Big Four 633 + Watsonian Oxford |
| 1940–45 | **Norton Big Four 633 cc WD combination** (driven sidecar wheel) | 4,779 combinations built 1938–41 — the only counted outfit of the period |
| 1946–59 | **BSA M21 600 cc sv + Watsonian Maxstoke (adult + child)** — if only ONE outfit is ever built, this is it (1950–1963) | purpose-built sidecar machine (lugs, low gearing, heavy flywheels, large rear tyre); AA fleet use; production 1937–63; Maxstoke = the literal family configuration |
| 1960–65 | BSA M21 + Watsonian Monaco (or Triumph 6T 650 + Monaco) | documented 1958–59 body range; late lower silhouette |

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

## E. Known and deferred (see also [pakset-roadmap](../pakset-roadmap.md))

- Re-do photograph-based geometry for the text-derived families (deferred by the user):
  Ford Fiesta Mk1–Mk7, BMC1100, Ford Escort Mk2, Vauxhall Nova/Corsa B–F.
- Ratification pending: Morris Cowley represented by the Oxford twins; E04A/E494A Anglia
  represented by FordPrefectEarly.
- RangeRover retire date (1988) may be too early — see
  [citycar-wealth-classes](citycar-wealth-classes.md) open questions.
