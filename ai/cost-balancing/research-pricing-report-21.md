# Research pass 21 — build cost and reliability of BR Standard steam and early diesel and electric classes

Status: draft evidence. Compiled 2026-11-22. Output for the parent session. The knowledge base is
not edited here.

**Covers**: anecdotal and measured evidence of build cost, routine maintenance burden and
overhaul interval for the BR Standard steam classes and the early diesel and electric classes,
with the mechanism stated in each case and a suggested modest adjustment where the evidence
supports one.

**Companion file**: `research-pricing-rows-21.csv`, 77 rows — 38 adjustments, 19 prices,
13 overhaul intervals, 5 boiler maintenance costs and 2 cross-traction benchmarks.

**Rule observed throughout**: no Simutrans `.dat` price was read, used or fitted to. Every
figure below is a historical price, a historical maintenance figure, or a band derived from a
stated mechanism. The fitted locomotive ladder in `New/ai/vehicle-cost-method.md` is mentioned
once only, as a cross-check on whether a class price is above or below its power-class norm; it
is not the source of any adjustment.

---

## 1. Method, evidence grades and what "adjustment" means here

The pass used one web search per turn on Exa, then fetched the page before relying on it. The
search targets were the classes named in the brief, plus Hansard for primary price and
maintenance statements, plus the Ministry of Transport accident reports for the electric
multiple units.

Three kinds of evidence are kept apart:

- **Measured** — a contract, works cost, Government answer or company account for a named class.
- **Stated** — a named engineer, historian or operator says a class was unreliable, expensive or
  durable, without a number. The adjustment is then a band inside the brief's ±5-20 per cent.
- **Inferred** — a band transferred from a related class or from a stated mechanism. Marked as
  such and given low confidence.

Confidence grades in this report:

| Grade | Meaning |
|---|---|
| High | Two independent sources agree, or a primary document states it, and the mechanism is identified |
| Medium-high | One good source with a clear mechanism, or two weaker sources that agree |
| Medium | One secondary source, no contradiction found |
| Low | Inference from a related case; use only as a placeholder |

**Direction convention.** In the CSV, `price` is a signed percentage. For `kind=adjustment` a
positive number raises the cost and a negative number lowers it. The `scope` field says whether
the percentage applies to build cost, routine maintenance or overhaul interval. A negative
overhaul interval means the locomotive goes to works sooner.

---

## 2. Actual prices found

These are the strongest rows in the pass. All are nominal money of the stated year.

### 2.1 BR Standard steam

| Class | Year | Price | Scope | Source | Confidence |
|---|---|---:|---|---|---|
| Class 7 Britannia 70000 | 1951 | £20,325 | loco, tender not stated | Preserved British Steam Locomotives | Medium |
| Class 7 Britannia 70054 | 1954 | £25,331 | loco, tender not stated | Preserved British Steam Locomotives | Medium |
| Class 6 Clan 72000 | 1951 | £20,426 | loco, tender not stated | The Clan Project, citing RCTS and Cox | Medium-high |
| Class 5 73000 | 1950 | £16,000 | loco, tender not stated | Riddles, JILE 40 (1950), via Railway Magazine Jan 1951 | Medium-high |
| Class 5, Derby batch 73075-89 | 1955 | £21,750 | engine and tender | 73082 Camelot Locomotive Society | Medium |
| Class 5, Doncaster batch 73080-89, 73110-19 | 1955 | £22,783 | engine and tender | 73082 Camelot Locomotive Society | Medium |
| Class 5 Walschaerts 73165-71 | 1957 | £25,606 | loco | Wardale, quoting BR figures | High |
| Class 5 Caprotti 73146-54 | 1957 | £28,469 | loco | Wardale, quoting BR figures | High |
| Class 9F (CRO comparison) | 1954 | £23,500 | loco | SteamIndex, quoting Atkins, Railway World 1988 | Medium |
| Class 9F 92220 Evening Star | 1960 | £33,500 | loco | Preserved British Steam Locomotives | Medium |
| Britannia pattern boiler | 1953 | £6,193 | boiler | Landau, SLS Journal 2004, from Cox | Medium |

### 2.2 What the steam prices establish

1. **The Standard Class 5 was the cheap end of the range.** Riddles' own 1950 figure is £16,000.
   By 1955 a Class 5 with tender cost £21,750 at Derby or £22,783 at Doncaster. The 4.7 per cent
   difference between two works in the same year is a builder effect, not a class effect.

2. **The Britannia was about 27 per cent dearer than the Class 5 in the same year** (£20,325
   against £16,000). That is the expected direction for a larger Pacific, and it is consistent
   with the fitted ladder. No build-cost adjustment is proposed for the Britannia.

3. **The Clan is the clear anomaly.** 72000 cost £20,426 in December 1951, against £20,325 for
   Britannia 70000 earlier the same year. The Clan was 7.7 per cent lighter (86 t 19 cwt against
   94 t 3 cwt) and had 14.4 per cent less tractive effort (27,520 lbf against 32,160 lbf), yet
   cost 0.5 per cent **more**. Both were built at Crewe. This is the strongest same-year,
   same-works pair in the pass, and it is the basis for a build-cost premium for the Clan.

4. **Caprotti was 11.2 per cent dearer than Walschaerts**, measured on a same-year, same-class
   pair (£28,469 against £25,606, +£2,863). This confirms the premium already used in the
   workbooks from the same source.

5. **The two 9F figures cannot be chained.** £23,500 in 1954 to £33,500 in 1960 is +42.6 per cent,
   far above general inflation, and the 1960 source also calls £33,500 the class average without
   reconciling the two. The likely causes are a later-batch specification or a tender-inclusive
   figure; the sources do not say. Use £23,500 for a 1954 comparison and £33,500 only as a
   1960 data point with the scope flagged.

### 2.3 Early diesel and electric

| Class | Year | Price | Scope | Source | Confidence |
|---|---|---:|---|---|---|
| Pilot-scheme diesels, average of 174 | 1956 | £65,517 | average per locomotive, Types 1-4 | White Paper Oct 1956, via Bradley | High arithmetic |
| Class 55 Deltic | 1958 | £155,000 | loco, 22 for £3,410,000 | Haresnape, Fleet Survey 3, p.6; Webb 1982 | High |
| DP2 prototype | 1965 | £104,950 | loco, April 1965 tender | RAIL 85, from BR Board papers | Medium-high |
| Class 47 (derived) | 1965 | £115,330 | derived, DP2 9 per cent cheaper | RAIL 85 | Low-medium |
| Class 50 (imputed) | 1966 | £131,000 | loco, imputed delivered cost | RAIL 85 | Medium-high |
| Standard Class 5 | 1951 | £13,300 per 1,000 drawbar hp | at 1 May 1951 | Hansard, 25 Feb 1952 | High |
| CC electric, Manchester-Sheffield | 1951 | £17,650 per 1,000 drawbar hp | at 1 May 1951 | Hansard, 25 Feb 1952 | High |

The £65,517 pilot-scheme average is the only figure that covers Classes 15, 16, 17, 21, 22, 23
and 28 as a group. It must not be used as a class price: the 174 locomotives span 800 hp Type 1s
to 2,000 hp Type 4s, so a Type 1 was well below the average and a Type 4 well above it. It is
recorded to show the order of magnitude (about £65,000 for a pilot-scheme diesel in 1956) and to
support the cross-traction ratio below.

The 1951 Hansard answer is the cleanest steam-versus-electric capital comparison found: the
Standard Class 5 cost £13,300 per 1,000 drawbar hp and the Manchester-Sheffield CC electric
£17,650, on the same date and the same basis. That is a 32.7 per cent electric premium for
comparable haulage capacity.

---

## 3. BR Standard steam: findings by class

### 3.1 The standardisation claim and its limit

Riddles' 1950 presidential address made the case for steam on capital cost. The figures he used
were: Class 5 £16,000; a 1,600 hp diesel £78,100; a gas turbine £138,700; an electric £37,400.
Cost per drawbar hp was 13s 6d for steam, £65 for diesel, £69 7s for the turbine and £17 13s for
the electric.

The Government White Paper of October 1956 used a different and much smaller ratio: diesel first
cost was "three to four times that of steam locomotives of comparable power". Riddles' figures
imply 4.9 times. The two are not consistent, and neither is a measured contract comparison. The
safe statement is that a main-line diesel of the mid-1950s cost roughly three to five times a
steam locomotive of comparable power, and that the ratio fell as diesel production grew.

The Standard design intent was lower maintenance: high running plates, exposed pipework,
self-cleaning smokebox, rocking grate, hopper ashpan and standard fittings. The evidence below
shows that this worked in general but that four specific variants carried a penalty.

### 3.2 Class 6 Clan — build cost above its class, maintenance slightly above

The Clan carries a real build-cost premium. The evidence is the same-year price equality with the
larger Britannia (§2.2, point 3). The mechanism is that the class was a new 225 psi boiler and a
Pacific chassis built in a batch of ten, so it carried design and setting-up cost without batch
economies. The Clan was also one of the few Standard types not recalled for investigative testing (with the
82xxx and 80xxx tanks and the 77xxx and 76xxx 2-6-0s), which suggests the teething problems were
worked out in service rather than at Rugby.

E.S. Cox, who led the design team, was critical: "The Class 6 4-6-2 locomotives turned out to be
the least effective of all the standard types", and he recorded "a woolliness quite absent in the
other types". Against that, the Scottish Region's Running and Maintenance Officer reported in
August 1952 that the boiler needed "few repairs" and that the class was "capable of producing
excellent results", with 31.8 lb of coal per mile.

Recommended: **build cost +10 per cent**, **routine maintenance +5 per cent**. The build figure is
high confidence on the price pair and medium on the band; the maintenance figure is medium.

### 3.3 Class 5 Caprotti — measured build premium, mixed maintenance effect

The 30 Caprotti Class 5s (73125-54) cost £28,469 each in 1957 against £25,606 for the Walschaerts
batch 73165-71, a measured +11.2 per cent. The Caprotti gear was specialist work while BR
workshops were tooled for piston valves and Walschaerts gear, and the Caprotti engines had
different cylinders.

The maintenance evidence cuts both ways:

- Valve examinations moved from every 30,000-35,000 miles on piston-valve engines to the major
  overhaul at 180,000-201,000 miles on Caprotti engines. That is a large saving.
- Piston rings at St Rollox were changed every 8,000 miles on Caprotti engines against
  11,000-12,000 on piston-valve engines. That is a real extra cost.
- Contemporary opinion, and the pattern of withdrawals, treated Caprotti as more expensive to
  maintain. The Wikipedia article on Caprotti gear states that most Caprotti-fitted locomotives
  were withdrawn before their Walschaerts counterparts because of the maintenance burden.

Recommended: **build cost +11 per cent** (measured), **routine maintenance +8 per cent**
(medium confidence, reflecting the heavier ring wear and specialist attention, net of the longer
valve-examination interval).

### 3.4 The three-cylinder question

The brief asks about "the 3-cylinder and Caprotti variants". The checked record gives only **one**
three-cylinder BR Standard: No. 71000 Duke of Gloucester, the single Class 8 Pacific. Every other
Standard class was two-cylinder. The three-cylinder premise therefore applies to one locomotive,
not to a family, and there is no measured three-cylinder premium to transfer.

71000 had three cylinders and Caprotti gear, was a one-off, and performed disappointingly at
first; the faults were later found to lie elsewhere in the design. Recommended: **routine
maintenance +10 per cent**, low-to-medium confidence, mechanism only. If the parent prefers to
leave a one-off unadjusted, that is defensible.

### 3.5 Class 9F — no adjustment, and why the boiler figure misleads

The 9F is the one Standard class with an unqualified success statement. SteamIndex: "The
scientific tests performed on the class showed it to be both powerful and efficient." Heritage
Railway: "particularly successful", capable of 90 mph. The class's high boiler maintenance figure
of 1.53d per mile against the Britannia's 0.89d is not a reliability signal: Landau attributes it
to the 9F's low annual mileage and the longer time between boiler overhauls, because boiler
deterioration is partly time-related rather than mileage-related.

Recommended: **no adjustment**. The Crosti variant is separate (below).

### 3.6 Franco-Crosti 9Fs (92020-29) — maintenance penalty, variant only

The ten Crosti locomotives are a distinct variant. The preheater drum collected ash and reduced
steaming; the smokebox corroded through sulphuric acid; exhaust blackened the cab in cross-winds
and crews criticised the draughting and the difficulty of burning large coal. All ten were
rebuilt to conventional form from 1959. Recommended: **routine maintenance +10 per cent** for the
ten Crosti locomotives only, medium confidence.

### 3.7 Class 7 Britannia — a small maintenance penalty, not a build penalty

The Britannia was efficient and well liked on the Great Eastern, and three locomotives exceeded
100,000 miles in a year. It also had three specific maintenance-relevant faults:

- Coupling rods broke because the driving wheels moved on their axles; the whole class was
  temporarily withdrawn in 1951. The cause was the roller-bearing fitting and it was corrected.
- Water carry-over from the dome knocked out cylinder ends and broke pistons early in service.
- The slide bars were fixed in a way that made the securing nuts difficult to tighten. The loss
  of a bottom slide bar led to the Blea Moor derailment of 21 January 1960 and five deaths. The
  Ministry of Transport report attributed it to poor maintenance which "in turn reflected poor
  detailed design".

Recommended: **routine maintenance +5 per cent**, medium confidence. The class was not unreliable
in the ordinary sense; the penalty reflects the access and detail-design faults that made
maintenance error more likely.

### 3.8 The smaller Standards — small or nil penalties

- **Class 4 4-6-0 (75000)**: poor steaming, double chimneys fitted to some. Powell: "steaming was
  poor in the extreme". **+5 per cent maintenance**, low confidence.
- **Class 4 2-6-0 (76000)**: "indifferent steamers" on the Southern, "required frequent mechanical
  adjustments by shed staff", but "reliable machines". **+5 per cent maintenance**, low confidence.
- **Class 2 2-6-0 (78000)**: "reliable if not remarkable"; some crews said it did not steam well
  and the footplate was draughty. **No adjustment**, medium confidence.
- **Class 3, Class 4 tank, Class 2 tank**: no adverse evidence found. No adjustment.

---

## 4. Early diesel and electric: findings by class

### 4.1 The Type 1 failures — 15, 16, 17

These are the three classes the user named, and the evidence is strong and consistent.

**Class 15 (BTH, Paxman 16YHXL, 44 built).** "As delivered, the engine was found to require
excessive maintenance." Modifications to pistons, rings and maintenance schedules and cast iron
cylinder heads produced "considerable improvements", but the engine remained a complex V16 for
800 hp. The class was withdrawn between 1968 and 1971. The publisher's description of Anthony
Sayer's 2021 book adds that BR records show "fractured crankcases, distorted cylinder heads and
blocked turbochargers", and that the BTH design had "significantly higher availability" than the
North British counterpart. Recommended: **maintenance +10 per cent, overhaul interval -10 per
cent**, high confidence on the mechanism and medium on the interval band.

**Class 16 (NBL, the same Paxman engine, 10 built).** The same engine was worse in the NBL
locomotive because ventilation was inadequate and the engine seized. Cylinder-head failure put
coolant into the fuel oil. The control equipment was a non-standard electro-mechanical system
("red circle") that was prone to failure and could not multiple with the standard "blue star"
locomotives. All ten were withdrawn in 1968 after about ten years. BRDatabase records that after
a short period the whole fleet was concentrated at Stratford "so as to be close to Stratford
repair shops for urgent attention if required". Recommended: **maintenance +15 per cent, overhaul
interval -15 per cent**, high confidence on the mechanism and medium on the interval band.

**Class 17 Clayton (117 built).** Twin Paxman 6ZHXL engines gave camshaft and cylinder-head
failures, oil leaks and fractured crankcases. Wikipedia, citing Sayer p.58, gives "overall
availability was around 60 per cent, even after extensive modifications". The Gloucestershire
Transport History account gives 50 per cent at the worst point. Withdrawals began in July 1968
and the last went in December 1971, so some locomotives had less than five years in service.
Recommended: **maintenance +15 per cent, overhaul interval -15 per cent**, high confidence.

### 4.2 The NBL Type 2 family — 21, 22, 41, 43

**Class 21 (58 built).** "Chronically unreliable" in Eastern Region service; the Hornsey
allocation was moved to New England Yard for storage by March 1960 and the Daily Telegraph
reported that new diesels were being hidden, which led to questions in Parliament. Faults:
power-unit/generator coupling failures, inadequate cooling, fractured cylinder heads, lubricating
oil escaping into the battery compartments, and engine-room fires that wrote off several
locomotives. Minor faults could only be fixed at depot or works, so daily availability was poor.
Twenty were rebuilt with Paxman Ventura engines as Class 29; the other 38 were withdrawn in
1967-68. Recommended: **maintenance +15 per cent, overhaul interval -10 per cent**, high
confidence.

**Class 22 (58 built).** The usual assumption is that this class was a failure. The evidence is
more mixed: engine and transmission faults when new, repairs under the NBL contract, improvement
by 1961, and "by the mid 1960s, the locos had settled down to give reliable service, with
availability over 85 per cent". The class was withdrawn in 1967-72 partly because NBL closed in
1962 and spares became difficult. Recommended: **maintenance +5 per cent only**, medium
confidence. This is a case where the anecdotal reputation is worse than the measured later
availability.

**Class 41 D600 (5 built).** The usual assumption is that this was the worst diesel-hydraulic.
The record contradicts it: "according to Laira staff reliability was not a problem as many have
thought". The five were withdrawn en bloc in December 1967 because they were non-standard and
few in number, and because the D800 Warships were the Western Region's preferred type.
Recommended: **no adjustment**, medium confidence. This is the clearest example in the pass of a
class reputation that the evidence does not support.

**Class 43 Warship, NBL-built (33 built).** Less reliable than the Swindon-built Class 42.
Mild-steel exhaust manifolds fractured, filling the cabs with exhaust fumes and losing turbo
pressure; piston-ring life was short because the engine was highly rated without active piston
cooling; metric-to-imperial conversion errors in the MAN drawings lowered tolerances. Spares
became difficult after NBL closed in 1962. Recommended: **maintenance +10 per cent**, medium-high
confidence.

### 4.3 The two-stroke experiments — 23 and 28

**Class 23 Baby Deltic (10 built).** The strongest quantitative reliability evidence in the whole
pass. The Type 2s of the period averaged 30,000-40,000 miles per failure; the Baby Deltics managed
"less than a quarter of this". By October 1960 the ten locomotives had covered only 40,000-60,000
miles each and had needed 44 engine changes in 18 months. Causes: fractured cylinder liners at the
injector hole, turbocharger bearing failures, seized pistons, and an auxiliary gearbox and
driveshaft that whipped and ruptured coolant hoses. After the 1963-65 refurbishment they became
"very reliable ... except for continuing coolant system problems". Recommended: **maintenance
+15 per cent, overhaul interval -15 per cent**, high confidence.

**Class 28 Co-Bo (20 built).** Crossley HST V8 two-stroke engines gave frequent failures; the
whole class was handed back to the manufacturer in 1961 for remedial work on the engines and to
cure cab windows falling out. The electrical and mechanical equipment was reliable; the engine
was not. BR obtained a quotation from English Electric to re-engine with the 8SVT but withdrew
the class in 1967-68 before doing it. Recommended: **maintenance +15 per cent**, high confidence.

### 4.4 The mainstream diesel-electrics — 31, 40, 44-46, 47, 50, 52, 55

**Class 31 (263 built, originally Class 30).** The Mirrlees JVS12T gave generally satisfactory
service for five years, then fatigue cracking appeared in welded major components. A sample of 34
locomotives produced 28 cracked components in engines with up to 20,500 hours. BR lost faith and
re-engined the whole fleet with the English Electric 12SVT between 1964 and 1969. After that the
class was reliable. Recommended: **maintenance +5 per cent**, high confidence on the fault and
medium on the residual band, because the fault was cured by re-engining.

**Class 40 (200 built).** The 16SVT was deliberately held at 2,000 hp to keep stresses low, and
the Class Forty Preservation Society records "generally good reliability". The class was
underpowered for its weight, which is a performance defect, not a reliability defect.
Recommended: **maintenance -5 per cent**, medium confidence.

**Classes 44, 45 and 46 (Peaks).** No reliability criticism was found in the sources reached. The
1969 availability figures quoted on a forum (from National Archives documents) show Class 44 at
5.6 of 10 and Class 45 at 72.6 of 107, which is unexceptional for the period, but that is a lead,
not a source. Recommended: **no adjustment**, medium confidence from absence of evidence.

**Class 47 (512 built).** The Sulzer 12LDA28C suffered crankcase and cylinder-block cracking. In
October 1965, 25 per cent of the 402 locomotives then delivered were out of traffic. The engine
was derated from 2,750 hp at 800 rpm to 2,580 hp at 750 rpm, the crankcase phasing and balance
weights were changed, and Vickers' welding was corrected. After that the class gave long service.
Recommended: **maintenance +5 per cent**, high confidence on the fault and medium on the residual
band.

**Class 50 (50 built).** Early service was poor: voltage spikes in the electronic control system
caused unexplained shutdowns, cylinder heads cracked and water entered the cylinders, connecting
rods bent and pistons seized; the main generator failed at an unacceptable rate. The manufacturer
guaranteed 84 per cent availability and was penalised for missing it. By the mid-1970s
"availability and reliability were extremely high, permitting favourable comparison with any
other Type 4". Recommended: **maintenance +8 per cent**, medium-high confidence, representing the
early-life penalty; a later-life figure would be negative.

**Class 52 Western (74 built).** Final-drive and transmission-bearing failures, bogie-frame
cracking, cylinder-head cracking and turbo-blower casing cracks; more than 60 modifications in
the 1960s. Most were cured and the class became reliable late on, with availability comparable
with other Type 4s. Recommended: **maintenance +8 per cent**, medium-high confidence. The
overhaul intervals are recorded separately in §7.

**Class 55 Deltic (22 built).** Reliability was good enough that in April 1965 BR judged the
Deltic better than the Class 47 for West Coast work "for reliability and scheduling". The
maintenance burden was nevertheless high: a five-year English Electric service contract covering
engines and generators, 13 spare engines for 22 locomotives, and specialist engine exchange at
overhaul. Recommended: **maintenance +8 per cent**, medium confidence. The penalty is for cost
and workshop burden, not for failure rate.

### 4.5 Electrics and EMUs — 76, 77, 303/305

**Class 76 EM1 (58 built).** Early problems were weight transfer, wheel slip and bent or fractured
bogie centre pins; forged steel pins and a weight-transfer switch cured them. By the late 1970s
the class was "among the oldest in service and yet one of the most reliable classes, on account
of robust design". Recommended: **maintenance -5 per cent**, medium confidence.

**Class 77 EM2 (7 built).** The LNER Encyclopedia records that the Woodhead route "did not
provide any difficulties for the EM2s". They were withdrawn because the 1,500 V DC system was
abandoned and the class was small, not because they failed. Sold to the Netherlands, they
averaged 2.5 million miles each against 800,000 in England. Recommended: **maintenance -5 per
cent**, medium confidence.

**Class 303/305 25 kV EMUs.** The Ministry of Transport's 1962 final report investigated
transformer failures on the Glasgow suburban stock and equipment failures on the North-East
London units. Five Glasgow transformers failed between October and December 1960; the fifth led
to withdrawal of the whole Glasgow electric service. Sixty-eight AEI transformers were rebuilt.
The North-East London GEC units suffered rectifier and surge-protection failures and were
relegated to the Chingford and Colchester-Clacton lines while the faults were corrected. Hansard
in June 1962 recorded that "all the fundamental difficulties ... have been overcome". Recommended:
**maintenance +10 per cent**, medium confidence, as an early-life penalty only.

---

## 5. Classes 15 and 16 in detail

The user's two examples are well supported, and the pass found a direct comparison between them.

**Class 15.** The Paxman 16YHXL was a high-speed V16 of 800 hp. It required excessive maintenance
as delivered. BR modified the pistons, rings and maintenance schedules and fitted cast iron
cylinder heads, which produced "considerable improvements in the engine's reliability". The class
was nevertheless described as "relatively unreliable", and it was withdrawn in favour of the
Class 20, which met the same Type 1 specification and was "less troublesome to operate". The
publisher's description of Sayer's book records BR archive material showing "fractured
crankcases, distorted cylinder heads and blocked turbochargers".

**Class 16.** The same engine, in a North British locomotive with inadequate ventilation, seized
frequently. Cylinder-head failure contaminated the fuel oil with coolant. The control system was
non-standard and failure-prone. BRDatabase records that the fleet was concentrated at Stratford
to be near the repair shops. The class lasted about ten years.

**The direct comparison.** The publisher's description of Sayer's 2021 volume is the single most
useful statement: it says BR records show the BTH design "had a significantly higher availability
than its North British counterpart". That is exactly the direction the user's example assumes,
and it justifies a larger penalty for Class 16 than for Class 15.

**What the evidence does not give.** No overhaul interval in miles or months was found for
either class, and no per-class contract price. The CSV therefore records the overhaul effect as a
percentage band, marked qualitative, not as a mileage.

---

## 6. Recommended adjustments

Only the classes with a stated mechanism are listed. "Build" means the purchase price; "maint"
means routine maintenance; "interval" means the time or mileage between overhauls. A dash means
no adjustment is recommended.

### 6.1 BR Standard steam

| Class | Build | Maint | Interval | Mechanism | Confidence |
|---|---:|---:|---:|---|---|
| Class 6 Clan | +10% | +5% | — | Same-year price equal to the larger Britannia; Cox calls it the least effective Standard | High on price, medium on band |
| Class 7 Britannia | — | +5% | — | Slide-bar access, water carry-over, coupling-rod failures; all corrected | Medium |
| Class 5 Caprotti | +11% | +8% | — | Measured +£2,863 build; heavier ring wear, specialist gear | High build, medium maint |
| Class 8 71000 | — | +10% | — | Only three-cylinder Standard; one-off with Caprotti | Low-medium |
| Class 9F Crosti | — | +10% | — | Ash-blocked preheater, acid corrosion, poor footplate conditions | Medium |
| Class 4 4-6-0 75000 | — | +5% | — | Poor steaming; double chimneys on some | Low |
| Class 4 2-6-0 76000 | — | +5% | — | Indifferent steaming; frequent shed adjustments | Low |
| Class 2 78000 | — | — | — | Reliable if unremarkable | Medium |
| Class 9F | — | — | — | Successful; high boiler cost is a mileage effect | Medium |

### 6.2 Early diesel and electric

| Class | Maint | Interval | Mechanism | Confidence |
|---|---:|---:|---|---|
| Class 15 | +10% | -10% | Paxman 16YHXL excessive maintenance; cured only partly | High |
| Class 16 | +15% | -15% | Engine seizures from poor ventilation; control gear failures | High |
| Class 17 | +15% | -15% | Paxman 6ZHXL; 60 per cent availability | High |
| Class 21 | +15% | -10% | NBL/MAN failures, fires, poor availability | High |
| Class 22 | +5% | — | Poor when new, 85 per cent availability later | Medium |
| Class 23 | +15% | -15% | 44 engine changes in 18 months; under a quarter of Class 24 miles per failure | High |
| Class 28 | +15% | — | Crossley two-stroke failures; class returned to maker | High |
| Class 31 | +5% | — | Mirrlees crankcase cracking, cured by re-engining | High fault, medium band |
| Class 40 | -5% | — | Conservatively rated 16SVT; generally good reliability | Medium |
| Classes 44-46 | — | — | No adverse evidence found | Medium |
| Class 47 | +5% | — | Sulzer crankcase cracking; 25 per cent of fleet out of traffic in 1965 | High fault, medium band |
| Class 50 | +8% | — | Early control, cylinder-head and generator failures; later excellent | Medium-high |
| Class 52 | +8% | — | Transmission, bearing and cylinder-head faults; 60+ modifications | Medium-high |
| Class 55 | +8% | — | Specialist Deltic maintenance, service contract, spare engines | Medium |
| Class 41 | — | — | Laira staff said reliability was not a problem | Medium |
| Class 42 | +5% | — | Maybach cooling and cylinder-head problems | Medium |
| Class 43 | +10% | — | NBL/MAN manifolds, ring life, tolerance errors | Medium-high |
| Class 76 | -5% | — | Cured early faults, then robust and reliable | Medium |
| Class 77 | -5% | — | No difficulties on Woodhead; long life in the Netherlands | Medium |
| Class 303/305 | +10% | — | Transformer, rectifier and surge failures, 1960-62 | Medium |
| LBSCR (context) | +5% | -5% | Stroudley's stated cost premium; 62.8 per cent survival to 1948 | Low |

The LBSCR rows are context only, outside the brief's period. They are included because the user
cited the LBSCR example: Stroudley told the ICE in 1885 that his engines cost "somewhat above the
average" and justified it by "the very best material and the best possible workmanship", and the
survival statistic supports the durability half of the claim. The counter-evidence is that
Brighton Works had a serious repair backlog in 1905-12 (20 per cent of stock awaiting or under
repair; 43 days for a general overhaul against 21 at Ashford), so the durability claim applies to
the designs, not to the works.

---

## 7. Overhaul-interval evidence, kept separate

This section is not priced. It is recorded for the later overhaul-interval feature.

### 7.1 Steam: the general-repair norm

Ten-year averages, 1951-1960, from a Class 8 boiler record at the National Railway Museum,
compiled by Landau:

| Class | Miles per general repair | Months per general repair | Days in works |
|---|---:|---:|---:|
| LNER A4 | 107,257 | 19.6 | 35 |
| GWR King | 104,261 | 24.6 | 40 |
| LNER A1 | 122,789 | 20.9 | 31 |
| LMS Princess Royal | 169,808 | 32.0 | 45 |
| LMS Duchess | 195,993 | 32.7 | 39 |
| SR Merchant Navy | 195,934 | 40.9 | 53 |

The spread is large: about 104,000 to 196,000 miles, and 20 to 41 months. Region and class
practice mattered as much as design.

### 7.2 Steam: the BR Standard and comparator figures

| Class | Interval | Basis | Source | Confidence |
|---|---:|---|---|---|
| BR Standard 5 (LMR) | 189,000 miles | between general overhauls, 1957 | Wardale, quoting Cox | Medium-high |
| LMS Black Five | 145,000 miles to 1939; about 160,000 by 1952 | between general repairs | Preserved British Steam Locomotives | Medium |
| Class 5 Caprotti | 180,000-201,000 miles | valve inspection at major overhaul | Wardale, quoting Duncan | Medium |
| Class 5 piston valve | 30,000-35,000 miles | piston and valve examination | Wardale, quoting Duncan | Medium |
| Class 5 piston valve | 11,000-12,000 miles | piston ring change, St Rollox | Wardale, quoting Powell | Medium |
| Class 5 Caprotti | 8,000 miles | piston ring change, St Rollox | Wardale, quoting Powell | Medium |

The BR Standard 5 at 189,000 miles is at the top of the steam range, above the Black Five it was
derived from. That is consistent with the design intent (roller bearings, rocking grate, hopper
ashpan) and argues against a general "Standards needed more works attention" adjustment. The
Caprotti evidence is the exception: ring life was shorter even though valve examinations were
much less frequent.

### 7.3 Diesel: the one measured interval

| Class | Interval | Basis | Source | Confidence |
|---|---:|---|---|---|
| Class 52 Western | 4-5 years | complete overhaul | Western Locomotive Association | Medium-high |
| Class 52 Western | 6,000 running hours (about 18 months) | light overhaul | Western Locomotive Association | Medium-high |
| Class 55 Deltic | 5-year service contract | English Electric maintained engines and generators | Haresnape; Wikipedia | High |

The Class 52 engines could be changed in a single working day, which is why a short engine
interval did not translate into long locomotive downtime. Any overhaul-interval model that
charges the locomotive for engine changes will overstate the Class 52's absence from traffic.

### 7.4 What is missing

- No overhaul interval in miles or months was found for Classes 15, 16, 17, 21, 22, 23, 28, 31,
  40, 41, 42, 43, 44-47, 50, 76 or 77.
- No works-turnround time was found for any of the early diesels, except the statements that
  Class 16 was concentrated at Stratford to be near the shops and that Class 21 minor faults
  needed depot or works attention.
- The Landau table is steam only. No equivalent BR diesel general-repair table was reached.

---

## 8. The strongest statements

Verbatim, with source. These are the quotations a later reviewer should test first.

1. **Class 15/16 comparison** — Anthony Sayer, *The BTH and North British Type 1 Bo-Bo
   Diesel-Electric Locomotives* (Pen & Sword, 2021), publisher's description: "We read of
   fractured crankcases, distorted cylinder heads and blocked turbochargers, but it is also clear
   from BR records that the BTH design had a significantly higher availability than its North
   British counterpart."

2. **Class 15 engine** — Wikipedia, citing Bradley and Clough: "as delivered, the engine was found
   to require excessive maintenance."

3. **Class 16** — Wikipedia, citing Bradley: "inadequate ventilation resulted in frequent engine
   seizures ... They were fitted with a non-standard type of electro-mechanical control equipment
   (coded 'red circle' by BR) which was prone to failure."

4. **Class 17** — Wikipedia, citing Sayer p.58: "overall availability was around 60 per cent, even
   after extensive modifications."

5. **Class 23** — Wikipedia, citing Webb p.18: "The Type 2s were averaging 30,000-40,000 miles per
   failure, the Baby Deltic less than a quarter of this." And: "in this 18 months there had been
   44 engine changes across only 10 locomotives."

6. **Class 41** — Wikipedia: "according to Laira staff reliability was not a problem as many have
   thought."

7. **Class 22** — Wikipedia: "by the mid 1960s, the locos had settled down to give reliable
   service, with availability over 85 per cent."

8. **Class 47** — Central Bylines, from BR records: "in October 1965, 25% of the 402 fleet members
   then delivered were out of traffic."

9. **Class 50** — RAIL 85 (October 1988): "The manufacturers had guaranteed an availability of
   84% and they were penalised heavily during the first years in traffic by failing to meet this
   target." And later: "both availability and reliability were extremely high."

10. **Class 52 maintenance** — Western Locomotive Association, J. Vaughan: "The maintenance of the
    locos called for complete overhauls only every four to five years and the high revving engines
    required light overhaul every 6,000 running hours, which would normally be achieved at
    approximately 18 month intervals."

11. **Class 6 Clan** — E.S. Cox, *British Railways Standard Steam Locomotives* (1966): "The
    Class 6 4-6-2 locomotives turned out to be the least effective of all the standard types."

12. **Caprotti costs** — Wardale, quoting Duncan: Walschaerts 73165-71 £25,606; Caprotti 73146-54
    £28,469; "Difference in capital cost of £2,863 per locomotive."

13. **Steam versus diesel first cost** — Riddles, JILE 40 (1950): Class 5 £16,000; 1,600 hp diesel
    £78,100; electric £37,400.

14. **Diesel maintenance** — Hansard, 13 May 1959: "the cost per engine mile of maintaining a
    diesel locomotive seems likely to be at least 20 per cent. less than for a steam locomotive
    of comparable power."

15. **Pilot-scheme average** — White Paper, October 1956: "Orders have been placed for 174 main
    line diesel locomotives at a cost of £11·4 million." That is £65,517 each.

---

## 9. Dead ends, gaps and cautions

### 9.1 Dead ends

- **No per-class contract price** was found for Classes 15, 16, 17, 21, 22, 23, 28, 31, 40, 41,
  42, 43, 44, 45, 46, 47, 76 or 77. The pilot-scheme average is the only group figure.
- **The Modern Railways archive** is not freely searchable. One January 1965 issue is available
  as a PDF at doublearrow.co.uk but was not parsed (no PDF text extractor on this machine).
- **The Ministry of Transport 1962 EMU report** is PDF-only at the Railways Archive. Only the
  contents page, the archive summary and the Hansard statement of 6 June 1962 were read. The
  body of the report, which would give the failure counts by equipment type, was not extracted.
- **RAIB** did not exist in the period, so there is no RAIB report on these classes. The 1962
  Ministry of Transport report is the equivalent primary source, and the 1955 Milton and 1960
  Blea Moor reports are the relevant steam accident reports.
- **Hansard** has no per-unit diesel prices. Searches returned only the 1951 per-drawbar-hp
  comparison, the 1955 and 1956 order debates, the 1959 maintenance comparison and the 1962 EMU
  statement.
- **The RCTS class histories** (`A Detailed History of British Railways Standard Steam
  Locomotives`, volumes 1-5) were identified as the authoritative source but were not read
  directly. The Clan and Britannia prices come from society pages that cite them.
- **The Sayer, Clough, Haresnape, Webb and Bradley books** were not read directly. Their
  statements are used through the publisher's descriptions, Wikipedia citations and the Whyte
  paper that quotes Webb. This is the main weakness of the diesel evidence.

### 9.2 Cautions on the price evidence

- **Scope is not stated for the Britannia and Clan prices.** If one includes a tender and the
  other does not, the 0.5 per cent equality is not a like-for-like comparison. Both sources are
  class histories that quote a single "cost to build" figure, which suggests the same scope, but
  this is an inference.
- **The 9F 1954 and 1960 figures cannot be chained** (§2.2, point 5).
- **The Class 47 price is derived**, not stated. It should not be used as a measured row.
- **The pilot-scheme average spans four power bands.** It cannot price a Type 1.
- **The White Paper's "three to four times" and Riddles' figures disagree.** Do not present a
  single steam-to-diesel ratio as measured.

### 9.3 Cautions on the reliability evidence

- **Availability and reliability are not the same measure.** A class can have high availability
  with frequent minor faults, or low availability from a few long repairs. The Class 52 is the
  clearest case: short engine life, but engines changed in a day.
- **The Class 15, 16 and 17 evidence is partly from the same publisher's series.** Sayer's three
  volumes are independent research but share an author and a viewpoint. The BTH-versus-NBL
  availability comparison is the strongest single statement because it is comparative.
- **The Class 22 and Class 41 findings contradict the common reputation.** They are included
  deliberately. A blanket "all early diesels were unreliable" adjustment would be wrong.
- **The 1969 availability figures** quoted on RMweb (Class 44 5.6/10, Class 45 72.6/107, Class 50
  30.2/50, Class 52 55/74, Warships 45/61 etc.) come from National Archives documents but were
  read on a forum. They are a lead for a future pass, not a source.
- **The LBSCR evidence is mixed.** The survival statistic supports durability; the Brighton Works
  backlog contradicts it for the 1905-12 period.

### 9.4 Largest gaps

1. **No measured maintenance cost per mile for any diesel class.** The only per-mile figures are
   steam boiler maintenance (Landau) and the 1959 Hansard ratio.
2. **No per-class diesel prices** for the Type 1 and Type 2 classes, which are exactly the classes
   with the strongest reliability evidence.
3. **No overhaul interval for any early diesel except the Class 52.** The overhaul-interval
   feature will need either a class-by-class archive search (BR works records at the National
   Railway Museum) or a default interval with explicit class multipliers.
4. **No EMU reliability series.** The 1962 report would supply it if the PDF can be extracted.
5. **No verification of the Britannia and Clan tender scope.** A copy of RCTS volume 1 would
   settle it.

---

## 10. Sources

**Primary and official**

- Hansard, HC Deb 25 February 1952 vol 496, Written Answer 80, "New Locomotives (Costs)".
- Hansard, HC Deb 13 May 1959 vol 605, Written Answer 19, "Diesel and Steam Locomotives
  (Maintenance Costs)".
- Hansard, HC Deb 6 June 1962 vol 661 cc60-1W, "Electric Trains (Report)".
- White Paper on the Modernisation Plan, October 1956, as quoted in R. Bradley, *2-Stroke Diesels
  on Britain's Rail Network* (2019).
- Ministry of Transport, *Final Report on the Accidents and Failures that occurred in Multiple
  Unit Electric Trains in the Scottish Region and Eastern Region* (HMSO, 1962), via the Railways
  Archive, document 732.
- Ministry of Transport, *Report on the Derailment ... at Milton ... 20 November 1955* (HMSO,
  1956); *Report on the Accident ... near Settle ... 21 January 1960* (HMSO, 1960), both cited by
  SteamIndex.
- J. Stroudley, discussion on "The Construction of Locomotive Engines", ICE Minutes of
  Proceedings 82 (1885).

**Books and journal papers**

- R.A. Riddles, "Nationalisation and the Mechanical Engineer", J. Instn Loco. Engrs 40 (1950)
  675-694; figures reproduced in Railway Magazine, January 1951, 60-61.
- E.S. Cox, *British Railways Standard Steam Locomotives* (Ian Allan, 1966).
- A. Sayer, *The BTH and North British Type 1 Bo-Bo Diesel-Electric Locomotives* (Pen & Sword,
  2021); *The Clayton Type 1* (2021); *The Metropolitan-Vickers Type 2 Co-Bo* (2020); *The North
  British Type 2 Classes 21 & 29* (2019); *The English Electric Type 2 Baby Deltic* (2019).
- D. Clough, *Diesel Pioneers* (Ian Allan, 2005).
- B. Haresnape, *British Rail Fleet Survey 3: Production Diesel-Electrics Types 4 and 5* (Ian
  Allan, 1982).
- B. Webb, *The Deltic Locomotives of British Rail* (David & Charles, 1982).
- P. Atkins, "The BR Standard 2-8-0s", Railway World 49 (1988) 222-223; *The British Railways
  Standard 9F 2-10-0* (Irwell Press, 1993).
- A.J. Powell, *Living with London Midland Locomotives* (1977), ch. 13.
- D. Landau, "Some Locomotive Boiler Statistics", SLS Journal (September/October 2004).
- D. Wardale, "Piston vs. Caprotti Valves - The Final Discussion?" (3 September 2009), quoting
  John Duncan's BR cost and maintenance figures.
- RCTS, *A Detailed History of British Railways Standard Steam Locomotives*, vols 1-5 (cited by
  the Clan Project, not read directly).

**Trade and institutional press**

- "Why the 50s triumphed in class struggle", RAIL 85 (October 1988), reproducing BR Board papers
  on DP2, the Class 47 and the Class 50.
- "50s in view", RAIL 85 (October 1988).
- Railway Magazine, January 1951, "Standardisation and Comparative Costs of Motive Power on B.R."
- Railway Gazette, 1956, "British Railways class 5 locomotives: thirty engines fitted with British
  Caprotti valve gear", cited by SteamIndex.
- Railway World, 1955, correspondence on the Franco-Crosti 2-10-0s, cited by SteamIndex.
- Modern Railways, January 1965 (PDF issue at doublearrow.co.uk; not parsed).

**Company and preservation sources**

- The Clan Project (Standard Steam Locomotive Company), "Clan History".
- 73082 Camelot Locomotive Society, S. Desmond, "Design and Construction" (1996).
- Western Locomotive Association, J. Vaughan, "About Westerns".
- Class 15 Preservation Society, "History".
- Class Forty Preservation Society, "History".
- Baby Deltic Project, "The Locos".
- Great Western.org.uk, "D800 Warship index" and "D600 Warship index".
- LNER Encyclopedia, EM1 and EM2 pages.
- BRDatabase, Class 16 history and Pilot Scheme list.
- SteamIndex, "British Railways standard classes".
- Preserved British Steam Locomotives, Britannia, Clan, 9F, Evening Star and Black Five pages.
- Key Model World, "Reality Check: The BR Standard 2MT 2-6-0s" (2023) and "Reality Check: Brush
  Type 2 variants" (2024).
- Gloucestershire Transport History, "The Greenest of Diesels".
- Mirrlees heritage paper, "The Mirrlees J and J Major Engines" (ipowere.org).
- derbysulzers.com, "sulzer 12LDA28C".
- Railway Matters, "Vickers and the Brush-Sulzer Class 47" and "Class 47 - almost 60".

**Used as finding aids only**

- Wikipedia articles on Classes 15, 16, 17, 21, 22, 23, 28, 41, 43, 47, 52, 55, 76, the BR
  Standard classes, the 9F, the Caprotti valve gear, Brighton railway works and the LBSCR.
  Where Wikipedia cites a book, the book is named in the row and the confidence is reduced
  accordingly.
