---
status: draft
verified: New ex-15 @ 2b3ae85bf (working tree, 2026-11-21)
---
# Citycar asset gaps (current register)

**Covers**: the coverage audit of `New/citycars/` after the 2026-11 private-car programme, the
gaps that remain, and the evidence for each. The 2026-11-15/16 build register is closed; this
document is its successor, not a queue for models that are already built. Calibration context:
[citycar-wealth-classes](citycar-wealth-classes.md); parc anchors:
[citycar-parc-anchors](citycar-parc-anchors.md); production method:
[car-batch-production](../graphics/car-batch-production.md); pipeline rules:
[visual-asset-controls](../graphics/visual-asset-controls.md) (all builds are
photograph-based). Figures are UK registrations/sales or GB licensed parc from the 2026-11-15
research (DfT VEH0120 via ukmotoring.co.uk; SMMT via AROnline; marque production records).

## Status of the 2026 programme

- The fleet is **425 cars, 7 motorcycle outfits and 4 horse-drawn vehicles: 436 models, 1,767
  objects**. `[CODE New ex-15 @ 2b3ae85bf]`
- Orders 1–51 of the 2026-11-15/16 build register closed on 2026-11-20. The per-order record is
  in the git history and `ai/temp/handoff.md`; it is not repeated here.
- Every named P1, P2 and P3 gap in the 2026-11-15 register is closed. The remaining gaps are
  **segment, marque, body-style and luxury-richness** gaps, not hard coverage failures.
- Exceptions carried forward: the Toyota Corolla E90 (1987–92) was in the generation scope but
  was not built; the E140 was dropped because Toyota GB did not sell it. The Toyota Yaris XP130
  is built and held for a user decision on its outline.

## A. Class coverage (P1) — closed

No month from 1750-01 to 2026-11 has a class with non-zero ownership and an empty or single-model
pool. The thinnest pools are now:

| Pool | Minimum | When | Evidence |
| --- | --- | --- | --- |
| Class 4 Very high | 7 models | 1920 and 1926 | 1926: Mercedes Simplex 60, Rolls-Royce Silver Ghost, Wolseley 16/20, Daimler TE30, Vauxhall 30-98, Aston 1½-Litre, Vauxhall 14/40. The 1920 pool replaces the Aston and Vauxhall 14/40 with the Citroen Type A and the open carriage |
| Class 3 High | 16 models | 1920 | the pre-war luxury and upper-middle fleet, from the Silver Ghost and Simplex to the Rover Twelve and Citroen Type A |

The target of three class-3 and three class-4 models per era is met in every era from 1920. The
pre-1920 pools are audited in [citycar-pre-1920-audit](citycar-pre-1920-audit.md). One texture
gap remains, not a P1 failure: in 1750–1829 classes 3 and 4 have exactly two models (a closed and
an open carriage); the park drag adds a third from April 1830.

## B. Entry-level (P2) — closed

The defining cheap cars of every era are now in the tree:

| Era | Fill models |
| --- | --- |
| 1920s–30s | Ford Model Y, Ford Model A, Austin Seven, Morris Minor 1928, Austin Ten, Ford Model C |
| 1950s | Ford Popular 103E, Austin A30 (the A35 shares the shell), Morris Minor, Ford Anglia 100E, Ford Prefect |
| 1960s–70s | Hillman Imp, Vauxhall Viva HA/HB/HC, Vauxhall Chevette, Ford Escort Mk1–Mk4, BMC Mini |
| 1980s–2000s | Citroen 2CV, Fiat 126, Lada Riva, Yugo 45, Skoda Estelle, VW Polo Mk2, Peugeot 205/206, Renault Clio, Nissan Micra K10–K15 |
| 2010s–20s | Dacia Sandero, Kia Picanto, Hyundai i10, Toyota Aygo/Aygo X, VW Up, Fiat Panda 1–3, Vauxhall Viva 2015 |

## C. Mainstream density (P3) — named gaps closed, segment gaps remain

The 2026 register's named mainstream gaps are closed: Vauxhall Cavalier Mk1–Mk3, Vauxhall Astra
Mk1–Mk8, VW Beetle, VW Golf Mk1–Mk8, Nissan Micra K10–K15 and Peugeot 205/206 are all present.
The remaining density gaps are structural, not marque-wide. The research segment column counts
the 425 cars as:

| Segment | Models | Segment | Models |
| --- | --- | --- | --- |
| A City | 16 | E Executive | 110 |
| B Supermini | 51 | F Luxury | 64 |
| C Lower medium | 115 | Sports | 27 |
| D Upper medium | 7 | SUV | 29 |
| MPV | 6 | | |

The D and MPV rows are the outliers:

- **Upper-medium (D) is the thinnest mainstream segment.** The research segment column has only
  7 D models, all Ford or Vauxhall: Cavalier Mk1–Mk3, Vectra B/C and Mondeo Mk1/Mk4. The Nissan
  Primera P10–P12 are upper-medium cars but currently fall into C in that column. This is a
  volume class, not a niche: the Cavalier alone was 1,201,693 licensed in 1995. The missing
  volume upper-medium saloons are Rover 600, Peugeot 405/406/407, Renault Laguna, VW Passat,
  Citroen BX/Xantia/C5, Toyota Carina/Avensis, Honda Accord and Mazda 626.
- **MPV is thin.** Six models, all Ford Galaxy Mk1–Mk3 and Vauxhall Zafira A–C. Missing: Renault
  Espace, Citroen Picasso, VW Touran/Sharan, SEAT Alhambra and Ford S-Max.
- **VW Polo is one generation only.** Mk2 is present; Mk1 and Mk3–Mk6 are absent.
- **Peugeot 306/307/308 are absent.** The 205 and 206 bracket them but do not cover the 1993–2013
  lower-medium continuity.

These are P3 by UK parc. Research the volumes before building; the D and MPV gaps are the
strongest remaining density claims.

## C1. Motorcycle-and-sidecar outfits (P2) — closed

Five period outfits are built: BSA 557 cc with BSA Type 1 chair, BSA 557 Sloper with Watsonian
Monarch, Norton Big Four 633 cc WD, BSA M21 600 cc with Watsonian Maxstoke, and BSA M21 with
Watsonian Monaco. Two more (Norton 16H and BSA M20) were built on 2026-11-20. The research
evidence remains: motorcycles 278,600 in 1920 (outnumbering cars), 125,499 outfits in 1936
(24.8% of the motorcycle parc), and about 130,000–150,000 outfits by 1952. The outfits are the
characteristic Very-low motorised transport of 1920–65; a single outfit would have been enough
for coverage, and the set now gives era-specific texture.
`[LITERATURE:https://assets.publishing.service.gov.uk/media/5a7506feed915d502d6cce89/vehicles-tables-csv.zip]`
`[USER-DIRECTION:2026-11-15]` `[EXECUTION-VERIFIED:2026-11-21]`

## D. Marque coverage (P3/P4)

The fleet covers the volume marques: Austin/Morris/BMC, Ford, Vauxhall, Rover, Jaguar, Land
Rover, Mini, BMW, Mercedes-Benz, Audi, Volkswagen, Porsche, Citroen, Peugeot, Renault, Fiat,
Nissan, Toyota, Kia, Hyundai, Dacia, Tesla, BYD and Jaecoo.

Absent marques with a significant UK presence are **Alfa Romeo, Saab, Mazda, Honda, Mitsubishi,
Subaru, SEAT, MG and Riley**. The most obvious model gaps are the Mazda MX-5, Honda Civic and
Accord, Saab 900 and 9000, Alfa 156 and Giulietta, MG MGB and Metro, and the pre-war Riley.
These are P4/P5 until the D and MPV density gaps are closed; assess each by UK parc before
adding.

## E. Luxury and executive (P4) — target met, optional richness

The old section B list is no longer a gap list: the three-per-era target is met, and the 1970s
and 1980s rows are fully represented. The remaining absent models, strongest evidence first:

| Era | Absent models | Evidence |
| --- | --- | --- |
| 1920s | Armstrong Siddeley Twenty; Bentley 3 Litre | 8,847 Twenty built 1926–36; 1,622 3 Litres |
| 1930s | Lanchester Eighteen; Alvis Speed 20 | 901 Lanchesters |
| 1950s | Jaguar Mk VII; Humber Super Snipe Mk IV; Armstrong Siddeley Sapphire; Wolseley 6/90; Daimler Conquest; Vanden Plas 4-Litre R | 20,908 Mk VII; 17,993 Super Snipe; 7,697 Sapphire; 2,509 Vanden Plas |
| 1960s | Jaguar Mk IX; Jaguar Mk X/420G | 10,009 Mk IX; 24,282 Mk X/420G |
| 1990s | Mercedes E-Class W210 | 87,509 licensed in 2000 |
| 2000s–20s | Mercedes E-Class W211/W213 | 247,289 licensed in 2020, the biggest prestige parc |

The 1970s and 1980s rows are complete: Granada Mk1/Mk2, Jaguar XJ6 S1/S2, Rover P6, Mercedes
W123, Jaguar XJ6 S3, Granada Mk3/Scorpio, Rover 800/Sterling and Mercedes W124 are all present.
The figures in the table are marque production records and DfT VEH0120 parc readings from the
2026-11-15 research return; the model-level sources are in the `.dat` headers. Every addition
remains subject to the photograph-first rule and the colour rule.

## F. Pre-1920 and pre-1900

The pre-1920 audit is closed: every model in its build list is in the tree, including the three
that were "prepared but not built" in the old text (Rolls-Royce Silver Ghost, Mercedes Simplex 60,
Vauxhall 30-98). The full audit is in [citycar-pre-1920-audit](citycar-pre-1920-audit.md).
Remaining pre-1920 questions are research questions, not asset gaps: the pre-1910 Wolseley
photograph, Star's pre-1910 output, the Humberette's class and whether the Singer Ten's pre-war
and post-war bodies justify two shells.

Pre-1900 texture is thin: the Daimler wagonette is the only object before 1902. This is P5; the
period park was tiny and a second veteran would be texture, not coverage.

## G. Body style and texture (P5)

- **Estates**: the Volvo 240 Estate is the only estate. There is no Cortina, Mondeo, Cavalier,
  Astra or 405 estate.
- **Convertibles**: the Triumph Spitfire 1500 is the only dedicated post-war roadster; the
  Triumph Stag is a targa-roofed tourer and the Citroen 2CV has a roll-back roof. The pre-war
  Wolseley 8 hp tonneau and Humberette are open, but there is no MGB, Escort or Fiesta
  convertible and no Saab 900 convertible.
- **Coupes**: Consul Capri, Rover P5/P5B coupe, the 1997 Ford Puma and the Aston range. The 2019
  Puma is a crossover, not a coupe. There is no Ford Capri, Vauxhall Calibra or BMW 3-series
  coupe.
- **MPVs**: see section C.
- **1940–45**: sparse by nature; the war years are represented by the pre-war and post-war cars
  that span them.

These are P5 texture. Add them only after the P3 and P4 gaps; the volume body per generation is
the existing rule.

## H. Build order (closed)

The 2026 build order ran to order 51 and closed on 2026-11-20 at 1,767 objects. The first
tranche (orders 1–22), the second tranche (23–37) and the third tranche (38–51) are all complete.
Do not re-open a closed order for a model that is already represented; use this document's current
sections for anything new. The per-order record, including pak counts and the few research
corrections, is in the git history and the session handoff.

## I. Known and deferred

- **Geometry re-do.** The text-derived families remain deferred: Ford Fiesta Mk1–Mk7, BMC1100,
  Ford Escort Mk2 and the Vauxhall Nova/Corsa B–F. They are acceptable at pak scale for now.
- **Stand-ins pending ratification.** Morris Cowley is represented by the Oxford twins; the
  E04A/E494A Anglia is represented by `FordPrefectEarly`.
- **Range Rover retire dates** settled 2026-11-20: all five colourways carry a staggered 1998–2005
  road tail.
- **Orphan renders** are closed: `morris-oxford-3-blue_*` is used by `morris-oxford-3.dat`, and
  `rover-sd1-yellow_*` is the Turmeric colourway of `rover-sd1.dat`.

## Open questions

- **Priority.** Should the next work close the D and MPV density gaps, the absent marques, or the
  luxury richness list? The evidence in this document supports D and MPV first, then the luxury
  models with production figures, then the marques.
- **Toyota Corolla E90.** The 1987–92 UK car is in the generation scope but was not built. Build
  it, or accept the E100 as the representative of the late 1980s Corolla?
- **Pre-1910 Wolseley.** Wolseley was the largest British maker of the 1910s, but no pre-1910
  photograph has been confirmed. Add only if one is found.
- **Rover 800 XX and Nissan Qashqai J10 dates.** The shells were re-rendered to one mark; whether
  to narrow `intro_year`/`retire_year` to that mark is savegame-relevant and remains undecided.
- **Body-style scope.** Are estates, convertibles and coupes wanted as a general programme, or
  does the one-volume-body-per-generation rule stand?
