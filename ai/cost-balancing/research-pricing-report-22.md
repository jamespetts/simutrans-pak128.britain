# Research pass 22 — build cost and reliability of British road vehicles

Status: draft evidence. Compiled 2026-11-22. Output for the parent session. The knowledge base is
not edited here.

**Covers**: anecdotal and stated evidence that named British road vehicle models cost more or less
to build, or were more or less reliable, than comparable models, 1909-1980, with the mechanism
identified in each case and a modest adjustment where the evidence supports one.

**Companion file**: `research-pricing-rows-22.csv`, 45 rows — 29 adjustments, 15 measured prices or
maintenance costs, and 1 benchmark recorded as a dead end.

**Rule observed**: no Simutrans `.dat` price was read, used, or fitted to. The only `.dat` files
touched were directory listings, used to check which model names the pakset actually carries.
No value in this pass is derived from the pakset.

---

## 1. Method, and what the evidence is worth

One web search per turn, then the page fetched and read before a claim was used. The productive
source was the **Commercial Motor archive** (`archive.commercialmotor.com`), which carries the
full text of road tests, operator surveys and conference reports from 1905 onwards. That archive
supplied most of the strong rows. Two PDFs (SELNEC history, Atlantean history) could not be
machine-read; quotes from them are taken from the publisher's extract or the search index and are
graded down accordingly.

Three kinds of evidence are kept apart:

- **Measured** — a price, an operating cost per mile, a maintenance cost, a fleet figure.
- **Stated** — a named engineer or operator says a model was dearer, cheaper, durable or fragile,
  with the mechanism visible. The adjustment is then a band inside ±5-15 per cent.
- **Inferred** — a band transferred from a stated mechanism or a related model. Marked low.

Confidence grades:

| Grade | Meaning |
|---|---|
| High | A named engineer or operator states it and a second source or a hard fleet fact agrees |
| Medium-high | One good named source with a clear mechanism, or two weaker sources that agree |
| Medium | One secondary source, no contradiction found |
| Low | Inference, or one weak source; placeholder only |

**Direction convention.** In the CSV, `price` is signed. Positive raises the cost or the burden,
negative lowers it. `scope` says whether the percentage applies to build cost, routine
maintenance, or body repair.

**The selection trap in every operator survey.** Operators who reply to a "why did you buy
foreign" questionnaire are the ones who are pleased. The 1973 Commercial Motor survey itself
prints the one dissenting operator, and the 1978 NBC trial prints the cost of every type, which is
why those two sources are used heavily and the enthusiast histories are not.

---

## 2. Recommended adjustments

Each row below has a stated mechanism. Confidence is given per row; the low rows are placeholders
only, not findings. The percent is the suggested default; the CSV carries the same value with the
full source record.

### 2.1 Buses and coaches

| Model | Scope | Adj. | Mechanism | Confidence |
|---|---|---:|---|---|
| AEC Routemaster | build cost | +10 | Light-alloy integral body and high specification; dearer than rivals and bought by no operator outside London | High direction, medium size |
| AEC Routemaster | routine maintenance | −10 | Aluminium body free of rot; fewer road failures than the RT; body overhaul reduced to wear items | High |
| Leyland Atlantean PDR1 | build cost | +10 | Integral rear-engine layout and dropped axle were costly; production version still dearer than a PD3 | Medium |
| Leyland Atlantean (early) | routine maintenance | +15 | Rear-engine heat and transmission duty; spare ratio 20-25 per cent against 10 per cent for a PD3 | High direction, medium size |
| Bristol VRT series 1 | routine maintenance | +10 | Throttle linkage, engine-bay ventilation, mitre-box final drive; 91 vehicles exchanged for Lodekkas in 1973 | Medium |
| Bristol VRT series 3 | routine maintenance | −5 | Developed into the cheapest bus in the NBC trial (with a Gardner) | Medium-high |
| Leyland National (early) | routine maintenance | +10 | Fixed-head 510: valves changed only with the engine out; early fault list; poor fuel consumption | Medium-high |
| Leyland National | body repair | −5 | Galvanised pressings, epoxy powder coat, full underseal; body structure gave no trouble | Medium |
| MCW Metropolitan | routine maintenance | +10 | Highest cost of four in the NBC trial (+24.8 per cent); propshaft and UJ faults | Medium |
| Ailsa | routine maintenance | +5 | Second of four (+19.7 per cent); gear-change control faults; best oil consumption | Medium |
| Leyland Titan PD2/PD3 | routine maintenance | −5 | Understressed O.600, long overhaul intervals, negligible Pneumocyclic maintenance, low spare ratio | Medium-high |
| Leyland Pneumocyclic gearbox | routine maintenance | −5 | Walsall: maintenance "negligible"; drivers preferred it to a conventional gearbox | Medium |
| ECW aluminium body | body repair | −5 | NBC: aluminium bodies outlasted steel competitors | Medium-high |
| Roe body on Atlantean | body repair | +10 | Water ingress, structural rebuild, internal corrosion, early withdrawal | Medium |

### 2.2 Lorries, vans and engines

| Model or item | Scope | Adj. | Mechanism | Confidence |
|---|---|---:|---|---|
| Gardner 6LX/6LXB option | build cost | +10 | "By far the most expensive engine option" (Bassett, 1980); no price quoted, so band inferred | Medium-high direction, low size |
| Gardner 6LX/6LXB | routine maintenance | −10 | Reliability, long life, fuel, resale; two breakdowns a year in one fleet; cheapest in the NBC trial | Medium-high |
| Rolls-Royce Eagle 265L option | build cost | −5 | Guinness: lower price almost exactly offset the Gardner's fuel advantage over eight years | Medium |
| Turbocharged diesel option | build cost | +15 | Survey average 15 per cent above naturally aspirated in 1970 | Medium |
| Leyland 500 fixed head | routine maintenance | +15 | Valve access needs special tools and block separation; casting tolerances; melted pistons; repowering | Low-medium |
| Leyland Marathon Mk1 | routine maintenance | +10 | 67 days out of service in 16 months; six cracked pistons; bracket fracture; air cleaner placement | Medium-high |
| Scammell Crusader (BRS spec) | routine maintenance | −5 | Built on proven Rolls-Royce, Fuller and Leyland axle at BRS insistence; mechanically sound | Medium |
| Volvo F86 | routine maintenance | −10 | Reliability was the stated reason for purchase; 125 in one fleet; 1.7 million mile example | Medium-high |
| Scania 110 | routine maintenance | −5 | 1.18 pence per mile against 1.62 for a Leyland 26-ton, but 1.03 for a Leyland 16-ton; one defector | Low-medium |
| Bedford TK | build cost | −5 | Simple driveline, shared components with TC/S, no-frills cab, £1,330 complete in 1960 | Low-medium |
| Ford Transit Mk1 | build cost | −5 | One range from 12 cwt to 35 cwt off a £10m tooling programme; £542 launch price | Low-medium |
| Bedford CF | routine maintenance | +5 | Slow, heavy, unreliable engine against the Transit | Low |

### 2.3 Cars

| Model | Scope | Adj. | Mechanism | Confidence |
|---|---|---:|---|---|
| BL cars of the 1970s (Marina, Allegro, Princess, Maestro, Montego) | build cost | +5 | CPRS 1975: assembly labour "nearly double" the continental requirement, engines 50-60 per cent more; BLMC fixed assets per man £920 against £2,657 at Ford Dagenham | Medium-high mechanism, low size |
| Morris Marina | build cost | −5 | Eighteen-month gestation on existing engines and gearbox; What Car? found it loose and rattly but expected reliability from tried parts | Low-medium |

### 2.4 Early vehicles

| Model | Scope | Adj. | Mechanism | Confidence |
|---|---|---:|---|---|
| Tilling-Stevens TS3 petrol-electric | build cost | +15 | Extra dynamo, traction motor and control gear; Stevens stated prime cost 25 per cent above a gear-driven chassis. Capped at 15 | Medium-high direction |

### 2.5 How to apply these without double counting

1. **Body and chassis are separate.** The Roe and ECW rows are body-maker effects. Applying an
   ECW credit and a VRT series-1 penalty to the same vehicle is correct only because they are
   different scopes (body repair against mechanical maintenance).
2. **Engine and vehicle are separate.** The Gardner rows and the Bristol VRT rows both draw on
   the 1978 NBC trial. Apply the Gardner credit to the engine option, and the VRT series-3 credit
   to the chassis, but do not apply both at full size to a Gardner-engined VRT.
3. **The Atlantean rows are for the early bus.** The AN68 of 1972 is a different vehicle; the
   SELNEC evidence concerns the original design. There is no evidence in this pass for a penalty
   on the AN68.
4. **The BL build-cost row is a maker effect, not a model effect.** It should not be stacked with
   the Marina row without deciding which is the larger claim: the Marina was cheap to develop
   and the maker was expensive to assemble. Net them, or use the maker row alone for later models.
5. **Nothing here is a price.** Every adjustment row is a percentage band. The only money figures
   are the fifteen measured prices and costs in section 3.

---

## 3. Measured prices and costs found

Nominal money of the stated year. These are the rows the parent can use as anchors rather than
bands.

| Item | Year | Figure | Scope | Source | Confidence |
|---|---|---:|---|---|---|
| Bedford TK 7-ton, complete with body | 1960 | £1,330 | chassis £1,100; chassis and cab £1,200 | CM road test, 28 Oct 1960 | High |
| Ford Transit SWB van, launch | 1965 | £542 | entry model | Ford launch price, secondary | Medium |
| Volvo F86 rigid at 32 tons | 1972 | £5,355 | primer, standard equipment | CM road test, 31 Mar 1972 | High |
| Scammell Crusader 4x2 | 1977 | £16,622 | basic; £17,556 as tested | CM road test, 16 Dec 1977 | High |
| Leyland Atlantean PDR1, complete | 1958 | about £7,000 | complete bus, approximate | Toy (2011) | Low-medium |
| Aldenham bus overhaul, average | 1965 | £2,000 | per bus, every four years | CM, 22 Jan 1965 | High figure, low transferability |
| Ribble National 755 re-engining | 1977 | about £7,000 | 680H conversion including engine | CM, 4 May 1979 | Medium-high |
| Noise encapsulation on a bus | 1974 | £400-£500 | added purchase price | CM, 7 Jun 1974 | Medium |

Comparative maintenance series:

| Fleet and vehicle | Year | Pence per mile | Source |
|---|---|---:|---|
| J. P. Wood, Scania 110 (272,000 miles) | 1973 | 1.18 | CM, 21 Sep 1973 |
| J. P. Wood, Leyland 16-ton | 1973 | 1.03 | CM, 21 Sep 1973 |
| J. P. Wood, Leyland 26-ton | 1973 | 1.62 | CM, 21 Sep 1973 |

| NBC/Maidstone trial type | Year | £ per 1,000 miles | Index |
|---|---|---:|---:|
| Gardner-engined Bristol VRT/SL3 | 1978 | 90.82 | 100 |
| Ailsa | 1978 | 108.71 | 120 |
| Leyland-engined Bristol VRT/SL3 | 1978 | 109.24 | 120 |
| MCW Metropolitan | 1978 | 113.30 | 125 |

The NBC table is the single most useful thing in the pass: four types, one operator, one depot
pair, two years, all costs counted the same way. It is the closest thing found to a controlled
comparison of British buses of the 1970s.

---

## 4. The strongest statements

Quoted because the wording matters and because a later reader should be able to check the
interpretation.

**Routemaster, build cost.** A. A. M. Durrant, chief engineer of London Transport (Road Services),
1965: production of an aluminium alloy vehicle such as the Routemaster "was a little more costly
initially", but "the light alloy integral construction ... had more than justified itself". George
McKay, NBC director of technical services, 1974: the Routemaster "was not sold (apart from 50 to
NBC's Northern General Company) outside London because it was more expensive than its
competitors".

**Routemaster, reliability.** Durrant, 1965: the RM "had experienced fewer road failures arising
from engine and fuel system, steering, fluid flywheel, gearbox and bodywork than its predecessor";
the aluminium bodies were "completely free from rot and corrosion" and would "easily reach the
designed life of 20 years".

**Atlantean, reliability.** SELNEC's history: "Reliability of the original design was poor, so much
so that spare ratios for Atlanteans were 20-25%, as compared with 10% or less with PD3 or similar
front-engined chassis." Walter Womar of Midland Red, 1970: "in the first 50,000 miles first the
clutch, then the gearbox and finally the engine failed. The cooling of the engine and flywheel did
not stand up to the work."

**Leyland National, engine.** Commercial Motor, 1979: the 680H conversion was made "to assess
whether the more familiar and simpler 680 would reduce maintenance costs"; "Its valves, for
instance, can be changed in [hours] whereas a 510 engine has to be removed to achieve the same
effect." The conversion cost nearly £7,000.

**Gardner, price and worth.** Len Bassett, 1980: "though it is by far the most expensive engine
option it's worth the extra outlay in terms of reliability and durability". Harry Bannister,
Guinness: over eight years "the Gardners' slightly better fuel consumption is almost exactly
offset by the lower price of the Rolls-Royce and there is little overall cost difference".

**British Leyland cars, build cost.** CPRS, 1975: "the labour requirements for assembling the same
car, even with identical capital equipment, are nearly double. In engines it is 50 per cent to 60
per cent more."

**British heavies versus imports.** Commercial Motor's 1973 survey: about 60 per cent of responding
operators cited foreign reliability and spares assurances; about 30 per cent had "gone foreign"
after bad experience with UK vehicles. One dissenter, G. J. Allen: "Price was a major factor,
particularly on Swedish vehicles, which received certain subsidies"; and British engines were "proving
to have longer life with less maintenance than foreign".

---

## 5. Findings by maker

**AEC.** The Routemaster is the clearest case in the whole pass of a vehicle that cost more to
build and less to maintain, with both halves stated by the customer's own chief engineer. The AEC
Regent III/RT is the baseline against which the Routemaster's reliability was measured, and no
separate AEC reliability penalty or credit was found. The AEC V8 was not researched to a usable
standard.

**Leyland.** Two distinct stories. The Titan PD2/PD3 is the durable, simple baseline; the
Atlantean is the expensive, troublesome successor, with municipal spare ratios double the PD3's.
The National repeats the pattern in a different form: an advanced body that gave no trouble and a
fixed-head engine that did. Leyland's own later products (Marathon, Crusader) show the split
between a good driveline and poor integration.

**Bristol and ECW.** The VRT's first two years were bad enough that 91 vehicles were exchanged for
front-engined Lodekkas; the developed series 3 with a Gardner was the cheapest bus in the NBC
trial. Both statements are true and the model needs both, weighted by year.

**Daimler.** The Fleetline evidence conflicts. SELNEC calls it "potentially a far superior vehicle"
to the Atlantean; the Road Transport History Association records London Transport withdrawing
2,646 Fleetlines prematurely. No adjustment is recommended.

**Guy, Sentinel, Foden, Thornycroft.** Nothing usable was found in the time available. The
pre-1930 lorry and bus field is a gap.

**Bedford and Ford.** Bedford TK is the cheap, simple, well-liked British medium lorry; the CF is
the one with a poor reputation. Ford's advantage is scale and standardisation (Transit), not a
superior component. The evidence for both build-cost credits is inferential.

**Gardner.** The strongest engine-level evidence in the pass. Expensive to buy, cheap to run, and
the operators say so in their own words. This is the model case for a build-cost penalty offset by
a maintenance credit.

**Volvo and Scania.** The direction is clear from operator surveys; the size is not, and the
Leyland 16-ton figure in the same fleet shows that "British" was not uniformly worse. Treat the
import credit as a 1970s heavy-lorry effect, not a permanent maker effect.

---

## 6. Dead ends, explicitly

1. **PSV Circle and Omnibus Society publications** are not online in usable form. No fleet
   history from either was read. This is the largest single gap: those are exactly the sources
   that carry per-vehicle cost and overhaul data.
2. **AA and RAC reliability statistics** for 1900-1980 were not found online. The modern MoT
   pass-rate datasets that surface in search are not evidence about period reliability and were
   discarded.
3. **Municipal fleet reports** (watch committees, transport committee minutes) were not found
   digitised. The SELNEC and Walsall statements reached this pass only through secondary
   publications.
4. **Alexander versus Metro-Cammell body corrosion**: no direct comparative statement was found.
   The only usable body-maker evidence is ECW aluminium against steel (McKay) and Roe against the
   rest (Toy). The brief's Alexander/Metro-Cammell axis is unresolved.
5. **London Transport's internal Atlantean report** (nine engine changes, 20 gearbox changes, 116
   fluid-flywheel failures, 37 radiator failures) is quoted only through Toy's book. The original
   report was not seen.
6. **Daimler Fleetline**: conflicting evidence, no adjustment.
7. **Scania 110**: conflicting evidence (one fleet reports lower cost per mile than a Leyland
   26-ton; another reports disappointing engine life and a return to British vehicles).
8. **AEC V8, Leyland T45 Roadtrain, Leyland Tiger/Leopard, Optare and Dennis products after
   1980**: not researched. The post-1980 bus and lorry field is a gap.
9. **Cars**: no contemporary model-level reliability survey was found. What Car?'s reliability
   survey, Which? and the MoT datasets all begin too late or measure the wrong thing. The car
   rows therefore rest on a government productivity report and one magazine road test.
10. **Tilling-Stevens maintenance**: the 1909 claim and counter-claim cannot be resolved from the
    available text; recorded as a benchmark with no adjustment.

---

## 7. Traps a later reader should not fall into

- **The NBC trial is not a build-cost comparison.** It measures operating cost over two years.
  A +25 per cent operating cost is not a +25 per cent purchase price; the rows are capped at +10
  for that reason.
- **Spare ratio is not failure rate.** The Atlantean's 20-25 per cent spare ratio reflects fleet
  policy and duty as well as reliability, but the contrast with the PD3 in the same fleet is
  still meaningful.
- **The 1974 National breakdown percentages are unusable.** McKay's figures (Nationals 34 per
  cent of breakdowns, VRT 49 per cent) are not divided by fleet share, and the article says they
  were still being analysed. Do not turn them into rates.
- **Durrant's "250,000,000 miles" engine overhaul figure is a typographical error** in the
  archived text. Read it as 250,000 miles; the sentence is otherwise unusable.
- **Selection bias in the 1973 import survey.** Only operators who had bought imported vehicles
  were asked. The one dissenter is the most valuable reply in the sample.
- **The 1909 petrol-electric prime cost is a manufacturer's claim.** It is good evidence of
  direction and roughly of size, not of a contract price.
- **Build-cost percentages are not additive across maker and model.** See 2.5.
