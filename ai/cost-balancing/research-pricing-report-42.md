# Research pricing report 42: lorry overhaul composition and invoices, 1933-2026

**Status**: research pass, 2026-11-25. Evidence and recommendation only. No workbook, `.dat`
value, existing doc or knowledge-base index was changed. Two new files: this report and
`research-pricing-rows-42.csv` (43 rows).

**Question**: what share of a British lorry's total maintenance spend is major overhauls, by era
and class, and should the lorry rows take the 37.5 per cent coach composition?

**Answer**: no. The three full-vehicle lorry costings that itemise both the total and the overhaul
give 46, 53 and 44 per cent for 1938, 1949 and 1955, not 37.5. The share falls to about 30 per cent
by the 1970s, 25 per cent by the 1990s and 10-15 per cent today. The coach share measures a
different split of the same physical work and must not be transplanted.
## 1. Method

- One Exa search per turn; every page relied on was fetched and read. A search result was not
  treated as evidence.
- Commercial Motor article pages fetched directly from `archive.commercialmotor.com` returned
  HTTP 200 and the full article text on every URL tried in this pass; the `pages` JSON of region
  coordinates (report 40 section 5) was not needed because every figure used is in the prose. OCR
  damage remains in headings and some numerals and is noted where it bites.
- Money is nominal of the stated year. No deflator or index conversion was applied anywhere; the
  one cross-year computation (section 6, 2026) is marked COMPUTED and its mixed years are stated.
- Grades: **MEASURED** = operator's or company's own account or transaction; **STATED** =
  trade-press costing or official table, not a transaction record; **COMPUTED** = arithmetic on
  stated figures, with the arithmetic shown; **ESTIMATE** = judgement where no measured figure
  exists.
- No `.dat` price, `runningcost`, `fixed_cost` or overhaul field was read or used.

## 2. The figures already in the files: confirmed, with corrections

| Figure as filed | Confirmed? | Correction |
|---|---|---|
| 1933 steam wagon annual overhaul GBP 40-70 (CM 10 Mar 1933) | Yes, verbatim: the maker does the work annually "at a cost ... varying from GBP 40 to GBP 70" | It is a **one-wagon owner** who does no other maintenance. The same article's 12-wagon fleet does its own annual overhaul with four mechanics at GBP 2-2 2s a vehicle-week, and the author states that figure is incomplete (wages and materials only, overheads unknown). The 36,000-mile annual mileage is the enthusiast fleet's, not the one-wagon owner's. A steam wagon, not a motor lorry. |
| 1936 heavy overhaul GBP 253 (CM 17 Jan 1936) | Yes | The vehicle type is **not stated** ("a vehicle"), the event is one overhaul in the second half of 1933, not an interval, and the article does not say whether the GBP 253 is inside the GBP 295 cumulative repair bill over 92,000 miles. "Heavy" is report 31's word, not the source's. |
| 1938 4-5 ton lorry major overhaul at 45,000 miles plus GBP 20 repaint (CM 16 Sep 1938) | Yes | The overhaul price was missing and is now recovered: operation 6 is 0.5d retail and 0.4d own-workshop, i.e. **GBP 93 15s or GBP 75** at 45,000 miles. The GBP 20 repaint is additional. The article prints three totals: 1.087d retail, 0.863d own, 0.887d weighted (Table VI). |
| 1950 engine overhaul "say GBP 80" at 48,000 miles; recon engine GBP 120-140 at 90,000 (CM 11 Aug 1950) | Yes | The GBP 80 **includes "a certain amount of chassis repair"**. The GBP 120-140 is an exchange reconditioned engine, not a fitted price; the article takes GBP 130. A top overhaul at 30,000 miles is GBP 7 at a garage or GBP 5 10s in the owner's workshop. |
| 1959 AEC exchange engine GBP 205-285 (CM 10 Apr 1959) | Yes | Basic charge, current models, exchange unit **not fitted**, new liners, pistons, rings, main and big-end bearings, crank reground to one of four standards, one year's guarantee. Older engines fall outside the basic charge. |
| 1955 cycle GBP 60 engine plus GBP 220 chassis and body at 100,000 miles | Yes, but the article is **CM 28 January 1955, p. 50**, not p. 53 | The GBP 60 engine overhaul or reconditioned unit is due at **50,000 miles**. The GBP 220 chassis and body major overhaul is due at **100,000 miles and includes the fitting of a second reconditioned engine**. The two are not additive at the same point. Assumed vehicle: petrol 6-tonner, 400 miles a week. |

## 3. Invoices and intervals

| Year | Class or operator | Item | As stated | Interval | Scope | Source | Grade |
|---|---|---|---|---|---|---|---|
| 1933 | Steam wagon, one-wagon owner | Maker's complete annual overhaul | GBP 40-70 | annual, ~36,000 mi fleet | Complete overhaul; boiler retube every 3 years extra | CM 10 Mar 1933, p. 48 | MEASURED |
| 1936 | Vehicle type not stated | One overhaul | GBP 253 | not stated | Not itemised | CM 17 Jan 1936, p. 50 | MEASURED |
| 1938 | 4-5 ton rigid | Operation 6, the 45,000-mile overhaul | GBP 93 15s retail; GBP 75 own | 45,000 mi = 72,400 km | Overhaul only; repaint GBP 20 extra | CM 16 Sep 1938, p. 34 | STATED |
| 1943 | 5-ton oiler, 600 mi/wk | Complete engine overhaul | GBP 130 | 60,000 mi = 96,600 km | Engine only | CM 29 Jan 1943, p. 24 | STATED |
| 1949 | 6-ton petrol, 400 mi/wk | Chassis and body overhaul incl. recon engine | GBP 170 (engine 75, chassis 40, body 15, labour 40) | 48,000 mi = 77,250 km | Engine, chassis, body | CM 27 May 1949, p. 22 | STATED |
| 1950 | 6-ton petrol, 600 mi/wk | Engine overhaul plus some chassis repair | GBP 80 | 48,000 mi | Engine + minor chassis | CM 11 Aug 1950, p. 46 | STATED |
| 1950 | 6-ton petrol | Complete exchange recon engine | GBP 120-140, mean 130 | 90,000 mi = 144,800 km | Engine only | Same | STATED |
| 1955 | Petrol 6-ton, 400 mi/wk | Engine overhaul or recon unit | GBP 60 | 50,000 mi = 80,500 km | Engine only | CM 28 Jan 1955, p. 50 | STATED |
| 1955 | Petrol 6-ton | Chassis and body major overhaul incl. second recon engine | GBP 220 | 100,000 mi = 160,900 km | Chassis, body, engine | Same | STATED |
| 1955 | 6-ton oiler, 800 mi/wk | Top / minor / major overhaul | GBP 5 / 60 / 120 | 10,000 / 40,000 / 80,000 mi | Top; minor incl. recon engine; major | CM 30 Dec 1955, p. 48 | STATED |
| 1959 | AEC exchange engine | Basic charge | GBP 205-285 | not stated | Exchange unit, not fitted | CM 10 Apr 1959, p. 72 | MEASURED |
| 1972 | AEC 691 (bus) | Repair vs new | GBP 195 vs 295 | not stated | Cracked tappet housing, new liners | CM 17 Nov 1972, p. 98 | MEASURED |
| 1972 | Rear axle casing | Repair vs new | GBP 50 vs 250 | not stated | Casing only | Same | MEASURED |
| 1973 | 32-t artic tractor, 10-vehicle fleet | Whole-life maintenance | GBP 5,000 + GBP 3,200 downtime | 200,000-mi life | 326 jobs, labour and materials | CM 20 Apr 1973, p. 31 | STATED |
| 1980 | Bedford KM | Full rebuild vs new | GBP 7,800 vs 15,000 | not stated | New cab, exchange engine, driveline, brakes, tyres | CM 12 Jul 1980, p. 92 | MEASURED |
| 1991 | Scania 142 V8 | Exchange engine | GBP 12,611.54 | not stated | Complete unit, 15 h to fit | CM 7 Nov 1991, p. 104 | MEASURED |
| 1991 | Scania 142 V8 | In-frame overhaul | GBP 3,210.88 parts + 40 h | not stated | Bearings, pistons, head, injectors | Same | MEASURED |
| 1993 | 300 hp tractor | Exchange engines | GBP 10,534 / 5,382 / 15,274 / 2,750 short | not stated | List ex-VAT | CM 23 Dec 1993, p. 112 | MEASURED (secondary) |
| 2011 | Volvo FH, 11 yrs, 1.4m mi | Engine rebuild at ~8 yrs | GBP 5,000 | ~1m mi | Rebuild | CM 15 Dec 2011, p. 38 | MEASURED |
| 2013 | Foden Alpha mixer, 10 yrs, 350,000 km | Re-body with new drum | ~25% of GBP 90,000 = ~22,500 | 10 yrs / 350,000 km | Drum and body, not engine | CM 23 May 2013, p. 31 | STATED / COMPUTED |
| 2023 | Scania, 16-truck fleet | Preventive clutch and turbo | GBP 500-600 + <1,000 | 500,000 km | Preventive replacement | TE May 2023 | MEASURED |
| 2023 | DAF CF 18-plate | Camshaft + turbo | GBP 1,600 + 4,600 | not stated | Failure repair | TE May 2023 | MEASURED |
| 2023 | 44-t tractor | Engine failure | GBP 5,000-15,000; up to 20,000 | 750,000 km design life | Engine | TE May 2023 | STATED |

**The 1940-2020 gap.** 1943, 1949, 1950, 1955 and 1959 are now filled. 1960-1971 has **no lorry
overhaul price**: the nearest is the 1972 AEC bus engine and the 1973 whole-life account, neither a
lorry overhaul invoice. 1972, 1973, 1980, 1991 and 1993 are filled; 2000-2010 only by the 2011
rebuild; 2011-2026 by five measured points.

## 4. The decisive evidence: compositions with both sides

No measured operator account giving both the total maintenance spend and its overhaul component
for the same lorries was found. That is the central gap. What exists is S.T.R.'s itemised
Commercial Motor costings, which build the total from the operations and therefore print both
sides for the same vehicle. They are STATED, not MEASURED, and **all are by the same Commercial
Motor costs writer (S.T.R.)**: one method at six dates, not six independent observers. That is why
the lorry share is graded STATED, not MEASURED.

| Year | Vehicle and duty | Total maintenance | Overhaul component | Share | Grade |
|---|---|---|---|---|---|
| 1938 | 4-5 ton rigid, 45,000-mi cycle | 1.087d retail, 0.863d own, 0.887d weighted (Table VI) | 0.4-0.5d/mi | 46% on the direct sums; Table VI does not print the overhaul separately | STATED |
| 1943 | 5-ton oiler, 600 mi/wk | 1.50d (d 0.22 + e 1.28) | 0.52d engine only | 35% of total; 41% of (e) | STATED |
| 1949 | 6-ton petrol, 400 mi/wk | 1.61d (d 0.38 + e 1.23) | 0.85d | 53% of total; 69% of (e) | STATED |
| 1950 | 6-ton petrol, 600 mi/wk | (e) 1.23d | 0.384d engine only | 31% of (e); floor | STATED |
| 1955 | 6-ton oiler, 800 mi/wk | 1.90d | 0.84d | 44% of total; 76% of the mileage-based items (0.84 + brakes 0.06 + sundries 0.20 = 1.10d) | STATED |
| 2026 | 44-t tractor, 75,000 mi/yr | GBP 10,957.50/yr | GBP 5,000-15,000 per engine event | 7-16%, central ~12% | COMPUTED |

**The wider subhead.** The Tables split maintenance into (d) routine, time-based, and (e) repairs
and overhauls, mileage-based. The measured (e) shares are 85 per cent (1943), 76 per cent (1949)
and 72 per cent (1955, a 7-tonner at 400 miles a week). The overhaul alone is 41-76 per cent of (e)
on the three full-vehicle costings, and 31 per cent on the 1950 engine-only floor. The difference
between (e) and the overhaul is routine and unscheduled repair, which must stay in the routine
remainder.

**The pre-1960 band.** Full-vehicle compositions are 44, 46 and 53 per cent; counting repaint and
brake refacing with the overhaul raises the 1938 and 1955 figures to 54-55 per cent. Engine-only
floors are 31 and 35 per cent. The band is **44-56 per cent, central 50**. The 37.5 per cent coach
figure sits below every full-vehicle lorry composition.

**Check against the invoices at the workbook's own reference distance.** The workbook holds lorries
at 40,000 km (24,855 miles) a year. At that distance:
- 1938: head 0.887d × 24,855 = GBP 91.9; 50 per cent = GBP 45.9/yr; one overhaul every 80,000 km
  (2 years) = GBP 91.9, against the measured GBP 75-93 15s.
- 1949: head 1.61d × 24,855 = GBP 166.7; 50 per cent = GBP 83.4/yr; one overhaul every 80,000 km =
  GBP 166.7, against the measured GBP 170.
- 1955: head 1.90d × 24,855 = GBP 196.8; 50 per cent = GBP 98.4/yr; one overhaul every 80,000 km =
  GBP 196.8, against the measured GBP 120 major plus two GBP 60 minors and top overhauls, about
  GBP 189 at 80,000 km.

The share, the interval and the invoices are mutually consistent. This is the strongest result of
the pass.

## 5. Why the lorry share is above the coach share

The 1947 coach account (CM 2 May 1947, p. 50) gives GBP 5,120 for twelve coaches: chassis labour
GBP 800 and materials GBP 2,400, engine reconditioning GBP 720, body overhaul GBP 1,200. The
overhaul is GBP 1,920, or 37.5 per cent; the routine chassis maintenance is GBP 3,200, or 62.5 per
cent.

The lorry costings put chassis and body work into the periodic overhaul, not into routine
maintenance: the 1949 GBP 170 includes GBP 40 of chassis parts and GBP 15 of body materials; the
1955 schedule puts GBP 120 into the major overhaul and GBP 20 into a repaint at half that interval.
The lorry's "routine" is the monthly service only: 0.68d of 1.90d in 1955, 36 per cent.

So part of the difference is accounting convention, not only wear. That is exactly why the coach
37.5 per cent cannot be moved onto lorries: it measures a different split of the same physical
work. It does not follow that lorries overhaul more; it follows that the lorry schedules classify
more work as overhaul.

## 6. The 1960-2026 taper, and the class question

**1960-1984.** No itemised composition and no lorry overhaul invoice. The 1973 whole-life study
gives 326 jobs over 200,000 miles, "almost 80 per cent of the total number of maintenance jobs"
routine, GBP 5,000 maintenance and GBP 3,200 downtime. The 1972 component repairs (GBP 195 engine,
GBP 50 axle casing) are small against a GBP 5,000 life cost. ESTIMATE **25-35 per cent, central
30**.

**1985-2004.** The exchange-unit era. The 1991 Scania exchange is GBP 12,611.54, the in-frame
alternative GBP 3,210.88 in parts plus 40 hours; 1993 exchanges run GBP 5,382-15,274. Against a
lifetime R&M of roughly GBP 40,000-48,000 (implied by the 1989 statement, recorded in
[road-maintenance-1959-2016](../vehicle-cost/road-maintenance-1959-2016.md), that an operator would
pay half the purchase price in maintenance over five years), one exchange is 26-32 per cent.
ESTIMATE **20-30 per cent, central 25**.

**2005-2026.** The pakset has **no lorry row introduced after 2000** (263 rows: 105 before 1930, 77
in 1930-59, 43 in 1960-84, 38 in 1985-2004, none later), so this band is recorded for completeness
and changes nothing today. RHA 2026 gives 14.61p a mile for a 44-t tractor at 75,000 miles =
GBP 10,957.50 a year, with no overhaul line. Over ten years that is GBP 109,575; a GBP 5,000-15,000
engine rebuild is 4.6-13.7 per cent, and adding clutch and turbo at GBP 1,550 twice in a million km
gives 7.4-16.5 per cent. COMPUTED **8-16 per cent, central 12**. The physical basis is stated by
DAF: modern engines and gearboxes "will usually keep working for at least five years/750,000km
without giving any significant trouble". The overhaul has largely ceased to be a scheduled event.

**Class.** All three itemised compositions are rigids. **No measured composition exists for an
articulated tractor or a van.** The brief's hypothesis (lower for tractors, higher for rigids) is
not supported by anything in this pass and should not be applied as a prior.

The reason the artic rows look over-provided is a **head defect**, not a class composition.
Thirteen tractor/artic rows (DAF XF Artic, DAF CF Artic, Leyland DAF 95 Artic, Leyland DAF 85
Artic, Leyland T45 Roadtrain, Scammell Handyman, Highwayman, Crusader, Townsman, Mechanical Horse,
Scarab, Thornycroft Amazon, Thornycroft Q) carry the class basis "road ladder (car) ... tractor-unit
ladder". Their maintenance heads are therefore built on the **private-car** per-mile ladder: DAF XF
Artic has a head of GBP 48.4 a year against capital of GBP 1,010. Nine of the nineteen rows above
60 per cent are in this group. Correcting the head is a separate and prior job; applying a lower
share to these rows without it would cut the overhaul provision while leaving the total
maintenance far too low.

**Vans.** The only measured van overhaul event is the 1956 Reliant 5-cwt engine at 15,000 miles and
"little more than GBP 20" (CM 17 Aug 1956, recorded in report 37). No van composition exists. Vans
were run to disposal. Leave them on the lorry band and record the gap; do not invent a lower van
share.

## 7. Recommendation

**R1. Do not apply 37.5 per cent to the lorry rows.** It is a coach composition and lies below
every full-vehicle lorry composition measured (44, 46, 53). Grade: **STATED**, strongly supported
(three dates, one costing method, one author).

**R2. Replace the single lorry profile with four era bands, applied as a floor-and-cap to the
annual provision, then rescale the overhaul targets to the same provision** (the pass-43 mechanism,
but two-sided):

| Intro band | Rows | Band centre | Band | Interval | Grade | Basis |
|---|---|---|---|---|---|---|
| before 1930 | 105 | 45% | 35-50 | 80,000 km | ESTIMATE | Back-cast from 1938; the 1933 steam wagon gives 15-26% of the Tables' head, so the band spans it |
| 1930-1959 | 77 | 50% | 44-56 | 80,000 km | STATED | 1938 46 (55 with repaint), 1949 53, 1955 44 (54 with repaint and brakes); invoices reconcile at 40,000 km/yr |
| 1960-1984 | 43 | 30% | 25-35 | 160,000 km | ESTIMATE | 1973 whole-life: 80% of jobs routine; 1972 component repairs small |
| 1985-2004 | 38 | 25% | 20-30 | 400,000 km | ESTIMATE / COMPUTED | 1991-93 exchange prices against lifetime R&M |

The floor matters: the bus rule is cap-only because 37.5 per cent is a single measured upper bound.
For lorries there are three compositions with a spread, so both tails are contradicted. Rows inside
the band keep their capital-share variation; rows outside are moved to the nearer edge, not to the
midpoint.

**R3. Change the interval with the band**: 80,000 km before 1960 (from 160,000), 160,000 km
unchanged for 1960-84, 400,000 km for 1985-2004. Basis: 45,000-50,000 miles (72,000-80,000 km) in
1938-55; 100,000 miles (160,000 km) in 1955; 500,000 km clutch/turbo and 750,000 km engine life in
2023. The 160,000 km now applied to a 1938 lorry is more than twice the measured interval, and to a
2000 lorry it is less than half.

**R4. Apply the share to the head as it stands, but fix the thirteen car-ladder tractor heads
first.** If the head fix lands first, the share rule changes those rows by less; if the share rule
lands first, the DAF pair's provision falls to about GBP 14.5 a year while its head stays at GBP
48.4. Either order removes the 104 per cent conflict; only the head fix makes the total right.

**R5. Do not touch the coach 37.5 per cent, the bus rows, or the shape of the lorry event** (first
10 per cent, max 30 per cent, three to the maximum). The shape is not what the evidence
contradicts; the share and the interval are.

**R6. Record the steam-wagon evidence as an open question.** The 1933 one-wagon owner's annual
overhaul is GBP 40-70 at about 36,000 miles, 15-26 per cent of the Tables' 1.80d head, not 50 per
cent. The 12-wagon fleet's own overhaul cost is unrecoverable. The pre-1930 band 35-50 spans both
readings; a steam-wagon band would need a fleet account with both sides.

## 8. Exact figures and rows the recommendation would change

**Profiles.**
- `New/ai/cost-balancing/evidence_data.py`, line 1096:
  `'lorry': (0.10, 0.30, 3, 160000.0, 0.3, 0.50)` is the single profile behind all 263 lorry rows.
  It becomes an intro-year table (four bands above).
- `overhaul_profile()`, lines 1132-1139, takes one `key` per class; it needs an intro-year branch
  for `lorry`. `'van'` (line 1097) is unused by these rows (all 263 resolve to `lorry`).
- `New/cost-balancing-capital.xlsx`, sheet `Overhauls & upgrades`: the 263 `lorry` rows' columns
  N-Q (suggested first, max, number, interval) are rescaled.
- `New/cost-balancing-maintenance.xlsx`, sheet `Road vehicles`: the same 263 rows' class fixed and
  per-km columns and their pass-42 notes.

**Counts.** Of 261 rows audited (2 of the 263 notes do not parse, so the four band counts below are
two short in total), **132 change** and 129 stay inside their band:

| Band | Rows | Change | Up | Down |
|---|---|---|---|---|
| before 1930 | 103 | 43 | 15 | 28 |
| 1930-1959 | 77 | 35 | 30 | 5 |
| 1960-1984 | 43 | 17 | 0 | 17 |
| 1985-2004 | 38 | 37 | 0 | 37 |

**Largest reductions** (percentage points of the head):
- DAF XF Artic and DAF CF Artic, 2000: 104.3% → 30% (-74.3). These two are the rows the brief
  names; today they deduct nothing and flag the conflict.
- Leyland DAF 95 Artic (1987) and Leyland DAF 85 Artic (1988): 92.7% → 30% (-62.7).
- Leyland T45 Roadtrain (1978): 91.1% → 35% (-51.1); Scammell Townsman (1967): 90.9% → 35%
  (-50.9); Scammell Crusader (1968): 76.8% → 35% (-36.8).
- Scammell Handyman and Highwayman (1955), Scammell Routeman (1955): 60-72% → 56% (cap).
- Foden Compound (1911), five rows: 60.6-63.2% → 50%; Thornycroft steam van (1896): 60.5% → 50%.

**Largest increases** (rows the capital-share estimate under-provides):
- Morris Eight van (1934): 26.0% → 44%; Thornycroft Amazon (1933): 27.4% → 44%; Thornycroft Stag
  Rigid (1934): 28.5% → 44%; Morris Minor van (1948): 28.6% → 44%. In all, 30 of the 77 rows in
  1930-59 rise to the 44 per cent floor.

**What does not change.** The 37.5 per cent coach and bus treatment; the 13 car-ladder heads (until
the separate head fix); the `van` profile; and the total maintenance charge, which is the head and is
not touched by a composition change.

## 9. Gaps that remain

1. **No measured fleet account with both sides.** A BRS, Pickfords, Unilever, brewery or local-authority transport account showing total repairs and the overhaul line for the same vehicles would settle the lorry share; none was found online and the records are not digitised. The lorry shares rest on S.T.R.'s costings, all by one author.
2. **1960-1971.** No lorry overhaul invoice; the 1968 GPO fleet gives intervals but no money, and the 1972 figures are bus and component repairs.
3. **1960-1985 composition.** No itemised total-versus-overhaul costing; the 30 per cent is an ESTIMATE from the 1973 job count and the 1972 repair prices.
4. **1985-2004 composition.** One exchange price and one contract-maintenance statement; the 25 per cent is an ESTIMATE.
5. **Artics and vans.** No composition of any kind; the 13 car-ladder heads are a known defect and the largest single cause of the rows above 60 per cent.
6. **Steam wagons.** The only pre-1935 composition is 15-26 per cent of the Tables' head for a one-wagon owner; the fleet figure is incomplete.
7. **Modern.** RHA and FTA publish one repairs-and-maintenance line and no overhaul line; the modern share is computed, not stated by any operator.
8. **The 1947 coach 37.5 per cent** remains the only measured composition of the Commercial Motor total; it is a coach composition and no lorry equivalent exists.

## 10. Sources

Fetched and read in full this pass:
1. Commercial Motor, "Users' Figures Reveal Possibilities of Economy Latent in New Types", 10 Mar 1933, p. 48. https://archive.commercialmotor.com/article/10th-march-1933/48/users-figures-reveal-possibilities-of-economy-late
2. Commercial Motor, "When is a Replacement Economically Essential?", 17 Jan 1936, p. 50. https://archive.commercialmotor.com/article/17th-january-1936/50/when-is-a-replacement-economically-essential
3. Commercial Motor, "And Now Maintenance in Pence Per Mile", 16 Sep 1938, p. 34. https://archive.commercialmotor.com/article/16th-september-1938/34/and-now-maintenance-in-ence-per-mile
4. Commercial Motor, "The Cost of Efficient Maintenance", 29 Jan 1943, p. 24. https://archive.commercialmotor.com/article/29th-january-1943/24/the-cost-of-efficient-maintenance
5. Commercial Motor, "Maintenance", 27 May 1949, p. 22. https://archive.commercialmotor.com/article/27th-may-1949/22/main-tena-ce
6. Commercial Motor, "Keeping Track of Rising Expenses", 10 Feb 1950, p. 48. https://archive.commercialmotor.com/article/10th-february-1950/48/keeping-track-of-rising-expenses
7. Commercial Motor, "What an Engine Costs", 11 Aug 1950, p. 46. https://archive.commercialmotor.com/article/11th-august-1950/46/what-an-engine-costs
8. Commercial Motor, "Maintenance What It Costs", 28 Jan 1955, p. 50. https://archive.commercialmotor.com/article/28th-january-1955/53/maintenance-what-it-costs
9. Commercial Motor, "How to Check Rate-cutting", 9 Sep 1955, p. 60. https://archive.commercialmotor.com/article/9th-september-1955/60/how-to-check-rate-cutting
10. Commercial Motor, "The Cost of Maintenance", 30 Dec 1955, p. 48. https://archive.commercialmotor.com/article/30th-december-1955/51/the-cost-of-maintenance
11. Commercial Motor, "Engine Rebuilding to Plan", 10 Apr 1959, p. 72. https://archive.commercialmotor.com/article/10th-april-1959/72/engine-rebuilding-to-plan
12. Commercial Motor, "When to repair rather than replace", 17 Nov 1972, p. 98. https://archive.commercialmotor.com/article/17th-november-1972/98/when-to-repair-rather-than-replace
13. Commercial Motor, "Reducing maintenance costs", 20 Apr 1973, p. 31. https://archive.commercialmotor.com/article/20th-april-1973/31/reducing-maintenance-costs
14. Commercial Motor, "Half-price rebuilds: are they bargains?", 12 Jul 1980, p. 92. https://archive.commercialmotor.com/article/12th-july-1980/93/half-price-rebuilds-are-they-bargainsi
15. Commercial Motor, "Engine options", 7 Nov 1991, p. 104. https://archive.commercialmotor.com/article/7th-november-1991/104/engine-options
16. Commercial Motor, "The Sum of the Parts Equals...", 23 Dec 1993, p. 112. https://archive.commercialmotor.com/article/23rd-december-1993/112/the-sum-of-the-parts-equals
17. Commercial Motor, "Keep on running", 15 Dec 2011, p. 38. https://archive.commercialmotor.com/article/15th-december-2011/38/keep-on-running
18. Commercial Motor, "Mixed emotions", 23 May 2013, p. 31. https://archive.commercialmotor.com/article/23rd-may-2013/31/mixed-emotions-why-spend-90000-on-a-new-six-wheel-
19. Transport Engineer, "Life extension", May 2023. https://te.mydigitalpublication.co.uk/articles/life-extension
20. Road Haulage Association, *Cost Tables 2026*, pp. 5-17 and Appendix I. https://www.rha.uk.net/Portals/0/Membership/Annual%20Cost%20and%20Pay%20Surveys/Cost%20Tables%202026.pdf

Not re-fetched this pass, and marked accordingly: `research-pricing-report-37.md` (sources S18,
S27, for the 1993 prices and one 1956 van price). Earlier passes relied on for the 1947 coach
composition and the 1989 contract-maintenance statement: `research-pricing-report-31.md`,
`research-pricing-report-40.md`, [road-maintenance-1959-2016](../vehicle-cost/road-maintenance-1959-2016.md),
[source-composition](../vehicle-cost/source-composition.md).
