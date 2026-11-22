# Research 23: build cost and reliability of British railway carriages, wagons and multiple units

**Task**: anecdotal, source-backed evidence that particular British carriage, wagon and multiple-unit
classes cost more or less to build, or were more or less reliable, than comparable stock. This feeds a
modest qualitative adjustment layer on a cost model whose first pass extrapolates from fitted ladders.

**Scope**: pre-grouping company stock, the Big Four standard designs, BR Mk1 to Mk4, Pullman and
dining vehicles; mineral, fitted and container wagons and the private-owner fleets; first-generation
DMUs and EMUs, the PEP family, the Pacers and Sprinters, and the Mk3-derived units.

**Outputs**: `research-pricing-rows-23.csv` (35 rows: 23 adjustments and 12 prices or price ratios) and
this report. No knowledge-base file was edited and no `git` command was run. No Simutrans `.dat` price
was used and no figure was fitted to the pakset.

---

## S1. Method and conventions

### S1.1 What counts as evidence here

The brief ranks sources: an operating department or a maintenance engineer outranks a magazine
impression. In practice the ranking that emerged from the search was:

1. **Primary operating documents**: the British Transport Commission memorandum of 14 February 1955
   on DMU availability; the British Railways Board's ECML project completion certificate. These are
   the strongest things found and there are only a few of them.
2. **Institution papers by named engineers**: Power on HST fleet operation (IMechE, 1978); Wakefield
   on twenty years of diesel railcars (IMechE Railway Division, 1971); Watts on the Mk4 (IEE, 1989);
   Wilson and Kirk on Mk1 crashworthiness (HSE, 2000). These state mechanism, which is what the
   adjustment layer needs.
3. **Company and works records**: the Pullman Car Company car histories; the Gloucester Railway
   Carriage and Wagon Company records at Gloucestershire Archives; the NER build records already in
   the knowledge base. These carry prices.
4. **Official statistics and parliamentary answers**: *Facts and Figures about British Railways*
   (1956, 1959); Hansard written answers. Fleet totals, not unit prices.
5. **Trade and technical press**: *Railway Magazine*, *Modern Railways*, *Rail*, *The Commercial
   Motor*. Useful where they quote a contract total or an engineer, weak as impression.
6. **Secondary web accounts**: Zavanak on the Pacers, heritage-railway carriage reviews. Used only
   where the arithmetic can be checked or where the claim is a mechanism rather than a judgement.

### S1.2 The sign convention used in the CSV

`price` is the recommended **percentage adjustment to the fitted base price** for that class, so that
the parent model can add it to the ladder output without re-reading the prose:

- **positive** = the class cost more to build, or was better regarded, than its weight, capacity and
  power imply;
- **negative** = the class cost less to build, or was less reliable, than those attributes imply;
- **magnitude** = 5, 10 or 15 per cent, except where a real price ratio was measured, and then the
  row says so and the notes give the arithmetic.

Each row states whether the driver is **build cost** or **reliability / whole-life cost**. They are not
the same thing and the model charges them in different fields: build cost belongs in `cost`,
reliability belongs in `runningcost` or in a service-life assumption. Mixing them is the main risk in
this dataset.

### S1.3 The discipline that keeps the adjustments modest

The fitted ladder already prices weight, capacity and power. An adjustment must therefore capture only
what those three cannot:

- fittings and systems that weigh little and cost much (air-conditioning, catering, secondary
  suspension);
- structure that is strong but light, or heavy but weak (integral bodies, corrosion paths);
- reliability that is a property of the design rather than of the duty cycle;
- volume effects on unit price that are not a property of the vehicle at all.

Where an effect is really a weight effect it has **not** been given a row. That is why there is no
adjustment for the Mk3 being longer than the Mk2: the 23 m body weighs more and the ladder sees it.

---

## S2. The defensible adjustments at a glance

| # | Domain | Class or item | Adj. | Driver | Confidence |
|---|---|---|---|---|---|
| 1 | carriage | BR Mk1, all variants | −5 | build (spartan finish, batch production) | medium-high |
| 2 | carriage | BR Mk1 corrosion (doors, windows, gangway ends) | −10 | reliability / whole life | medium |
| 3 | carriage | BR Mk1 override crash structure | −5 | safety / service life | medium-high |
| 4 | carriage | BR Mk2 integral body | +5 | build (tooling, lost flexibility) | medium-high |
| 5 | carriage | BR Mk3 systems beyond weight | +5 | build (air-con, air suspension) | medium |
| 6 | carriage | BR Mk3 BT10 axlebox and disc brakes, 1977-78 | −10 | reliability | high |
| 7 | carriage | BR Mk3 late-life corrosion and PRM | −5 | whole life | medium |
| 8 | carriage | BR Mk4 new-design risk, 1989-91 | −10 | reliability | medium-high |
| 9 | carriage | Pullman and dining | +15 | build (catering, finish, low volume) | medium |
| 10 | carriage | Pre-grouping and Big Four | 0 | no new adjustment needed | high |
| 11 | wagon | BR 16-ton all-steel mineral | −10 | build (volume, unsprung, unfitted) | medium-high |
| 12 | wagon | BR 16-ton mineral, short economic life | −5 | whole life | medium-high |
| 13 | wagon | Private owner coal wagons | −15 | build (cheap spec) and neglect | medium |
| 14 | wagon | Vacuum-fitted stock as a class | +10 | build (brake equipment) | medium-high |
| 15 | MU | First-generation DMUs, design | −10 | reliability | high |
| 16 | MU | First-generation DMUs, fire risk | −5 | reliability | medium-high |
| 17 | MU | SR diesel-electric multiple units | +10 | reliability (body-mounted engines) | medium-high |
| 18 | MU | Pacer family 141-144, build | −15 | build (bus body, four-wheel) | medium |
| 19 | MU | Pacer family, ride and track wear | −5 | whole life | low-medium |
| 20 | MU | Sprinter family 150/155/156 | +10 | build (conventional bogie DMU) | medium |
| 21 | MU | PEP family 313/314/315/507/508 | +10 | build and durability | medium-high |
| 22 | MU | Class 508 on the Southern | −5 | reliability (braking, wheel slide) | low-medium |
| 23 | MU | Class 455 value-engineered | −5 | build (cheaper, slower) | medium |

Rows 2, 3, 6, 7, 8, 12, 16, 19 and 22 are reliability or whole-life effects. If the parent model puts
all of these into `cost`, a troublesome class will be made *cheaper to buy*, which is the wrong
direction for a class that was troublesome precisely because it was bought cheap. **Recommendation:
put the build-cost rows (1, 4, 5, 9, 11, 13, 14, 18, 20, 21, 23) into `cost`, and keep the reliability
rows as notes for `runningcost` or for a separate reliability term.**

---

## S3. Carriages and coaches

### S3.1 BR Mk1 (1951-1964)

The Mk1 is the best-documented carriage in the search and the one where the evidence points in two
directions at once.

**Heavy and robust.** Divall and Shin's study of the Mk2's gestation gives the cleanest statement:

> "The Mk1 thus followed the best of conventional practice with a steel body mounted on a steel,
> load-bearing underframe; although stronger and safer than most of the Big Four's coaches, there was
> otherwise little advance on familiar standards."

and, on why the Mk2 had to be integral:

> "This gave a much lighter vehicle for a given strength - important since most improvements to the
> Mk1 made a heavy design even heavier."

So the Mk1 is a **heavy** design that got heavier with every improvement, built to be strong rather
than light or luxurious. The same paper is explicit that the finish was cheap:

> "This design was at best workman-like... continuing shortages of capital and materials precluded
> much innovation."

> "the interiors were plain (perhaps influenced by the prevailing aesthetics of utility), with simple
> details, spartan fittings and predominantly wooden wall finishes"

Two forces therefore pull in opposite directions, and they must not be confused:

- **Upward**: the separate body and underframe is more labour per ton than an integral shell;
- **Downward**: spartan fittings, wooden wall finishes, and batch production in BR's own works over
  the thirteen years 1951-1964 hold the unit price down.

The heaviness itself is not an argument for a premium, because the ladder already charges for it. On
balance the evidence points **down**, so the adjustment is −5 (row 1), not a premium. A parent that
wants to model the Mk1 as "heavy but cheap" can do so with this row plus the weight the `.dat` already
states.

**Corroding.** The Bluebell Railway's carriage and wagon department, which has maintained Mk1s since
the 1980s, names the failure modes precisely:

> "the main weakness in Mk.I design being the door and door-frame structure"

> "The end-loading pillars, quarter-inch thick steel channels, had rusted almost completely through at
> the bottom."

> "it is, however, the condition of the door pillars which is the limiting factor on safety grounds,
> and will, if corrosion is unchecked, lead to the demise of any Mk 1 coach."

and the maintenance consequence: each coach needs "major work each decade".

**Crash structure.** Wilson and Kirk, writing for the HSE research programme, describe the design
problem in structural terms:

> "This vehicle's basic design consists of a substantial underframe to which is attached, at either
> end, two four-wheel bogie sets. A relatively light body is then attached to this underframe."

In an override the underframe climbs and penetrates the lighter body. That is why the class left the
national network, and it is a service-life fact, not a build-cost fact.

**What to do with it.** −5 for build (row 1), −10 for corrosion (row 2), −5 for the crash structure
(row 3). The three do not cancel: they belong in different fields.

### S3.2 BR Mk2 (1964-1975)

The Mk2's value to this exercise is that its advantage is *already priced* by a weight ladder, and its
disadvantage is not. From Divall and Shin:

> "This gave a much lighter vehicle for a given strength"

but also, because the body was load-bearing:

> "it was much harder to change the position or size of the holes for doors, windows or inter-coach
> (gangway) connections"

and the stress analysis delayed the design: the Board's decision in 1961 was taken on the basis of an
"as-yet unfinished Swindon prototype", and the more radical structural proposals would have delayed
the coaches "by possibly 18 months".

So the +5 is for engineering effort and lost flexibility, not for the shell — the shell's weight
saving is the ladder's business.

The same paper also records that the Mk1's "improved riding qualities proved short-lived as the
suspension wore badly, and interior noise levels were higher than in most older stock". That is a
reliability point against the Mk1 and in favour of the later bogie designs, but it is a maintenance
statement without a number, so it is recorded in the notes of row 1 rather than given its own row.

### S3.3 BR Mk3 (1976-1988)

**Construction.** All-welded mild-steel stressed skin, fully integral monocoque, 23 m, BT10 bogies
with secondary air suspension, disc brakes, air-conditioning in modules behind the bodyside skirt.
The Mk3 is the first UK coach at 23 m and weighs about 34 t (Railnews, November 1980, comparing it
with the aluminium APT trailer at 24 t).

**Early reliability: the strongest single finding in the carriage domain.** Power's 1978 IMechE paper,
written by BR's Chief Mechanical and Electrical Engineer at Paddington while the fleet was two years
old, records two design failures:

> "Following discovery of a fractured axle box on a Mark III locomotive hauled coach, an immediate
> survey of all HST coach axleboxes was undertaken and this resulted in a number of vehicles being
> withdrawn from service... The outcome was a policy decision to design and manufacture a new axlebox
> with a view to replacing the existing one."

> "Initially the discs on the locomotive hauled stock, which have the fitted bolts at the corners,
> began to fracture in this area... Despite this, fractures of the fitted bolts and the disc have
> continued and as a result considerable design effort is being put into this particular problem."

This is exactly the sort of evidence the brief asks for: a named engineer, a fleet-wide survey, a
withdrawal, a redesign, and a problem that had not been solved two years later. It justifies a −10
reliability adjustment for early Mk3, tapering as the fixes went in.

**Late life.** By the 2010s the Mk3's problem was corrosion, not structure. Chiltern's project engineer
in *Rail* (2012):

> "beyond the doors, the major work required is to repair corrosion damage. This will allow the
> coaches to remain in traffic for at least 10 to 12 years before the work is required again."

The same article records that the rebuild cost £6.5m and that "economics dictate that it is cheaper to
rebuild the Mk 3s than to order brand new DMUs". That is a durability statement as much as a corrosion
one: the vehicle is worth rebuilding after forty years.

**Net.** +5 for systems (row 5), −10 for the early axlebox and brake problems (row 6), −5 for late
corrosion (row 7). A parent model that wants one number for the whole life should use 0 and note both.

### S3.4 BR Mk4 (1989-1992)

Two facts matter.

**It is steel, not aluminium.** Watts (Metro-Cammell, IEE 1989):

> "The bodyshell of the Mk IV passenger vehicles and the Driving Van Trailers is of conventional
> construction based upon the lightweight shell developed by Metro-Cammell for the British Rail Class
> 156 Diesel Multiple Units... The structure is a total monocoque all-welded carbon steel
> construction designed with the aid of finite element analysis."

So the Mk4's shell is the Class 156 shell technique scaled up, which ties the two classes together in
any cost model.

**It was a high-risk introduction, and BR said so.** The ECML project completion certificate (1992):

> "the decision to go for new designs in both the power units and the coaches was high risk and, as
> the progress reports from October 1988 onwards show, we paid the price."

New bodyshell, new SIG BT41 bogies, new gangways, and a locomotive that was itself split into a
ten-unit proving batch. The Mk4 ran in service behind Class 91s hauling Mk3s for the first months of
electric working because the coaches were not ready. −10 for introduction reliability (row 8) is
defensible; there is no evidence found that the Mk4 was unusually expensive per vehicle once the
contract was let.

**Quantities**, from the DfT *Rolling Stock Perspective* (fourth edition): 302 Mk4 vehicles built
1989-92 including 31 DVTs. The same series lists Mk3 vehicles in blocks totalling about 186 for
1976-85.

### S3.5 Pullman and dining vehicles

The Pullman archive gives complete-car prices with tare, seating and builder, which is rare.

| Car | Year | Builder | Tare | Seats | Cost |
|---|---|---|---|---|---|
| MADELINE, kitchen | 1926 | Metropolitan-Cammell | 39 t | 20 | £5,050 |
| GSR 100-103, third buffet | 1926 | Birmingham RC&W | 39.5 t | 46 | £5,537 5s |
| No. 53, 12-wheel kitchen third (conversion) | 1929 | Pullman, Preston Park | 42.5 t | 33 as built, 18 after | £471 3s 9d |

Against a 1924-25 Southern eight-compartment third at £2,500 and a 1929-30 LNER five-compartment brake
third at £2,300 (both already in the knowledge base), the Pullman kitchen car is **2.0 to 2.2 times**
the price of a corridor third for a similar length.

That whole ratio must not become a class term. Three reasons:

1. **Kitchen equipment is a separate object** in the pakset. If the dining car carries a catering
   vehicle's cost, the class term would charge the kitchen twice.
2. **Volume.** Thirty cars for the *Queen of Scots* and four for Ireland are not batch production;
   the unit price carries the tooling and the hand-finished marquetry.
3. **Tare.** 39 t for a 57 ft car is heavy; the ladder sees that and will already price it high.

Hence +15 (row 9), with the measured 2.0-2.2× recorded in the notes as the ceiling. The 1929
conversion at £471 is useful as a lower bound on what a catering refit cost against a car of about
£2,000-2,500 — roughly a fifth of a new vehicle for the kitchen alone.

### S3.6 Pre-grouping and the Big Four: no new adjustment

The knowledge base already holds the best pre-grouping evidence available in this workspace, and it is
better than anything the web search produced: the NER build records with diagram numbers, lengths,
wheel arrangements and prices, plus the same-body pairs from the Midland, GWR and Highland.

Those pairs already separate the variables this task cares about:

- six-wheel against bogie, same body: +19.4 per cent (Midland, 1870s);
- steel against wood panelling: +25.0 per cent (GWR Toplight, c.1903-10);
- first against third, same dimensions and weight: +78.4 per cent (Highland, 1873);
- clerestory against arc roof: +2.6 per cent (Midland, 1880);
- dining car against composite, same length and wheels: +£710 (NER, 1909).

Adding a second, weaker class term for "pre-grouping carriage" on top of these would double-count. The
recommendation is therefore **zero** (row 10), and the row exists to stop a later reader adding one.

What the search did **not** find is any statement that a particular pre-grouping company's stock was
regarded as over-built or trouble-prone — the LNWR's weight, the GWR's finish, the NER's lavish
dining cars. Those are common claims in enthusiast writing and none of them surfaced in a source
strong enough to cite. Recorded as a dead end (S9).

---

## S4. Wagons

### S4.1 The BR 16-ton all-steel mineral wagon

This is the cheapest, most numerous and least durable wagon class in the evidence, and all three
properties are documented.

**Volume and standardisation.** *Facts and Figures about British Railways* (1956):

> "New wagons produced in 1955 totalled 58,733 of which nearly 42,000 were all-steel 16-ton coal
> wagons... At the end of 1955 there were 230,000 all-steel 16-ton coal wagons"

> "By standardisation it has been possible to reduce the number of designs in current production."

The wagon historian's count is 352,801 built to 1962 by 28 builders; 206,444 of them were diagram 1/108
alone, built by 17 firms in 183 lots, with Pressed Steel responsible for 71,000-77,709. That is the
definition of a volume-built cheap article.

**Specification.** Nine-foot wheelbase, unsprung, unfitted, Morton brake, plain bearings, no continuous
brake. The vacuum-braked minority was 7,700 of the 206,444.

**Short life.** By 1959 the same official series records:

> "Fewer wagons were built in 1958 - 36,284 compared with 59,687 in 1957 and 61,474 in 1956.
> Concurrently with this new construction, some 121,000 wagons were withdrawn."

and "the last of the 16-ton wagon orders... are almost complete; future coal-carrying wagons will have
capacities of something over 20 tons". A class whose build ended in 1959 was being withdrawn in bulk
in the same decade. The 1956 edition had already conceded that "many wagons had to be kept in service
beyond their normal life".

**Adjustments**: −10 for build (row 11), −5 for the truncated economic life (row 12). A model that
prices wagons by capacity and weight will overprice the 16-tonner; the volume and the absence of a
brake system are the reason.

### S4.2 Private owner wagons

Three separate facts, from three separate record sets, agree.

**Price.** The Gloucester Railway Carriage and Wagon Company records, through Gloucestershire Archives,
give the C.P. Teague fleet: "Wagon 6 was purchased for £66.00 and the original seven year repair
contract with GRCW was renewed in October 1913." Against £81 for a 10-ton railway-owned Shildon wagon
of 1906 (knowledge base) — the Teague wagon's capacity is not stated in the source — the private owner
wagon is about **18 per cent cheaper**.

**Specification and condition.** Grease axleboxes, no continuous brake, wooden bodies. The standard
trade description is blunt: wagons "often poorly maintained", and "these grease boxes tended to dry out,
causing fires and sometimes melting the ends off the axles", so that axleboxes "had to be inspected
frequently when in transit".

**Regulation.** "In 1919 the Ministry of Transport Act obtained powers to restrict or prohibit the use
of private owner wagons on railway company lines. In the event these powers were never used." A fleet
that Parliament legislated against and then declined to regulate is a fleet with a recognised quality
problem.

**Salvage value.** At nationalisation, compensation was "sixteen pound ten shillings for an 8-ton
Private Owner wagon", paid "regardless of condition". That is a floor, not a price.

**Adjustment**: −15 (row 13). The seven-year repair contract is itself worth recording: private owner
wagons were bought with maintenance bundled, which is a different commercial object from a railway
company's own stock.

### S4.3 Fitted and unfitted stock

The only quantified statement found is the fitted share: 178,033 fitted freight wagons at the end of
1955 out of about 1,125,000, and pipe-fitted stock at 21 per cent of carrying stock. That is enough to
support a **+10 for fitted stock as a class** (row 14) on the ground that a vacuum brake, train pipe
and couplings are a real cost that the wagon's capacity and tare do not express.

It is not enough to separate individual fitted diagrams. No source found gives a per-wagon price
differential for fitting in the BR period.

### S4.4 Container flats and Freightliner

The only figure found is an aggregate: *The Commercial Motor*, 10 May 1968, reports the second stage of
the Freightliner network at about £8m for "some 4,750 containers and 875 Freightliner wagons", with
most construction in BR workshops. The wagon and container prices are not separated, so no per-wagon
figure can be derived without an assumption. Recorded as an upper bound row and **not** used for an
adjustment.

This is the largest single gap in the wagon domain (S9).

---

## S5. Multiple units

### S5.1 First-generation DMUs: the best-documented reliability failure in the set

Three independent sources, of three different kinds, agree.

**The operating document.** A British Transport Commission memorandum of a meeting at Marylebone on
14 February 1955, chaired by R.C. Bond, with E.S. Cox present, on the West Riding diesel trains:

> "the Report of 3rd February sent by the General Manager of the North Eastern Region... dealing with
> the deterioration which had occured in the availability of the West Riding Diesel Trains"

> "the recent severe weather conditions of driving rain and subsequently frost which had revealed
> weaknesses in design"

> "It was agreed that the troubles experienced could not be attributed to faulty workmanship either in
> Railway Workshops or by Contractors."

That last sentence is the important one for a cost model: **the failures were design, not build**. A
class that was cheaply built would show workmanship faults; this one did not. So the adjustment is a
reliability discount, not a build-cost discount.

The same memorandum shows the commercial consequence: modifications completed one set at a time at
Derby, weekly availability returns, monthly meetings with the supplier, and a proposal from British
United Traction to run its own model depot at Bradford, which BR refused because "the agreed policy
was for British Railways to undertake their own maintenance".

**The engineer's paper.** Wakefield's "Twenty years' experience with diesel railcars" (IMechE Railway
Division, paper RDP 2/71, 1971, 19 pages plus 19 of discussion) is described by the archive that holds
it as "19 pages of problems". The author's own summary:

> "Mistakes were obviously made in many areas, the whole fleet was built in an amazingly short space of
> time, and because of this, there was little or no opportunity to incorporate the experience obtained
> in service into the vehicles as built."

He also gives the only fleet maintenance figure found:

> "The total cost of maintaining the existing fleet of these vehicles in 1969 was £11.8m and during
> that time the total train mileage was 62.2m: givings an average cost of maintenance of £0.19 per
> vehicle mile."

**Arithmetic check**: 11.8 / 62.2 = 0.1897. The division works on **train** miles, so the stated "per
vehicle mile" is almost certainly wrong by the average formation length. Record the £11.8m and the
62.2m miles; do not propagate £0.19 per vehicle mile.

**The fire record.** In the discussion, J.R.H. Robertson gives the underfloor-engine fire series:

- 57 fires in 1965, 42 in 1969;
- rate per 100 power cars: about 0.6 in 1961, nearly 2.5 in 1965, 1.93 in 1967, 2.01 in 1968, 2.07 in
  1969;
- "more than 50 million miles a year, or about 1.2 million miles per fire";
- the trend was rising again at the end of the period, and the withdrawn vehicles were not the worst.

**Adjustments**: −10 for design reliability (row 15), −5 for fire risk (row 16).

### S5.2 Southern Region diesel-electric multiple units

The same discussion contains the single cleanest comparative reliability statement found in the whole
search:

> "the outstandingly good fire record of the diesel-electric multiple-unit trains of Southern Region
> which had body-mounted engines."

This is a contemporary engineer contrasting two design philosophies in the same discussion, on the same
statistic. It is worth more than any number of magazine impressions. +10 (row 17).

It also gives the model a principle rather than a class term: **body-mounted engines were safer than
underfloor engines**, because the fuel, the hot exhaust and the oxygen were not crowded together under
the passengers. Any future DMU/DEMU distinction in the pakset should start here.

### S5.3 Pacers and Sprinters: cheap, dearer, and the arithmetic between them

**Prices.** The figures found are consistent and, unusually, allow a like-for-like comparison.

| Order | Date | Vehicles | Price | Per vehicle |
|---|---|---|---|---|
| Class 141, 20 two-car sets | 1984 | 40 | £8m | £200,000 |
| Class 142, 50 two-car sets | Jan 1984 | 100 | £17m | £170,000 |
| Classes 150/2, 155, 156 | 1984-86 | 568 | £149.5m | £263,204 |
| Class 508, 43 four-car sets | 1979-80 | 172 | £26m | £151,163 |

So a Pacer car cost about **35 per cent less than a Sprinter car** (£170,000 against £263,204), and the
contemporary comparison offered by the Leyland/BREL record is with a three-car Class 210 estimated at
£1m, "almost half the price on a car by car basis".

**Reliability.** *Rail* (2019) on the Pacers:

> "issues with their mechanical transmission being among the most significant. By 1987... 26 of the 57
> '142's based at Newton Heath depot in Manchester were out of service. The entire 25-strong fleet of
> Class 143s which were then allocated to Heaton in Newcastle were also affected"

and the fix: "replacing the troublesome Leyland running units with more dependable Cummins L10 engines
and Voith hydraulic transmissions". After that, "consistently less reliable than the Sprinters".

**Adjustments**: −15 for the Pacer's build (row 18), −5 for ride and track wear (row 19), +10 for the
Sprinter (row 20).

**A warning about the price comparison.** The Class 508 figure is 1979-80 and the Pacer figures are
1984. In nominal terms a four-car PEP EMU car was *cheaper* than a two-car Pacer car five years later;
deflated by the inflation of those five years it would not be. The Pacer was cheap **relative to a
conventional DMU of its own year**, not cheap in absolute terms. A model that reads "Pacer = half
price" from the Class 210 comparison and applies it to a 1980s base will over-discount.

### S5.4 The PEP family and the Mk3-derived units

**Construction and durability.** The PEP prototypes of 1971-72 were aluminium alloy on a steel frame,
integral, with every axle motored, Scharfenberg couplers, rheostatic braking and sliding doors. The
production Classes 313, 314, 315, 507 and 508 followed, 755 vehicles in all.

**The engineer's verdict.** *Modern Railways* (2019), from someone who worked on the door controls at
the Railway Technical Centre:

> "They were lightweight and had all axles motored, which gave them terrific acceleration."

and on what happened next:

> "by the time the '508s' appeared they had been 'value engineered' and the number of motored axles
> reduced to 50%, but the lightweight aluminium body remained - a '508' trailer weighs only 26.5
> tonnes, compared to a '450' trailer at 35.5."

> "in 1984 came the '455', back to 25% axles motored with a steel body roughly based on the Mk 3 coach."

That 26.5 t against 35.5 t is the most useful weight comparison in the multiple-unit evidence: a
nine-tonne difference on a trailer car between two generations of the same route's stock.

**Longevity.** Class 313 entered service on 8 November 1976 and the last were withdrawn in 2023; Class
507 from 1978 into the mid-2020s. That is about 46 years, which is durability evidence of a kind no
paper states.

**The 508's specific trouble.** The 508s were built for Merseyrail and diverted to the Southern, where
they "didn't find much favour with the operating department, which had issues with braking and wheel
slide, with one unit failing to stop at Shepperton station and running through the buffer stops". They
went north as soon as Class 455s were available. A −5 for the 508 alone (row 22), inside a +10 for the
family (row 21).

**The 455.** Value-engineered from the 508: 25 per cent of axles motored, steel body based on the Mk3.
Cheaper to build and slower, which the pakset's power and weight fields partly capture; −5 (row 23) for
the rest.

### S5.5 What the multiple-unit evidence cannot do

- It cannot rank the first-generation **EMU** classes. The search found no equivalent of Wakefield's
  paper for the SR EMUs, and the 1972 IEE paper by Kibblewhite ("various defects and modifications
  noted") is paywalled at abstract level.
- It cannot price a DMU engine or transmission separately, which is what a reliability model would
  really want.
- It gives no Class 142/143/144 price split; the £17m is for the 142 batch only.

---

## S6. Every price found, with its arithmetic

| Item | Year | Nominal | Basis | Per vehicle |
|---|---|---|---|---|
| Pullman kitchen car MADELINE | 1926 | £5,050 | complete car | £5,050 |
| Pullman third buffet, GSR | 1926 | £5,537 5s | complete car | £5,537 |
| Pullman No. 53 conversion | 1929 | £471 3s 9d | conversion only | n/a |
| PO 7-plank coal wagon (Teague) | c.1906 | £66 | complete wagon | £66 |
| PO wagon compensation, 8-ton | 1948 | £16 10s | salvage value | £16.50 |
| Class 508, 43 × 4-car | 1979-80 | £26m | complete sets | £151,163 |
| Class 141, 20 × 2-car | 1984 | £8m | complete sets | £200,000 |
| Class 142, 50 × 2-car | 1984 | £17m | complete sets | £170,000 |
| Classes 150/2, 155, 156 | 1984-86 | £149.5m | 568 vehicles | £263,204 |
| Freightliner equipment | 1968 | £8m | 875 wagons + 4,750 containers | not separable |
| First-gen DMU maintenance | 1969 | £11.8m | 62.2m miles | £0.19 per mile |
| IC225 rolling stock | 1988-92 | £447m at 2017 prices | 31 × 91, 21 × 90, 31 DVT, 283 Mk4, 4 × 317 | not separable |

Two notes on use:

- The IC225 figure is a **2017-price restatement** by the project director, not a 1990 contract value.
  It is useful as an order of magnitude for a nine-car 225 km/h train and nothing more.
- The Class 141 and 142 figures come from a secondary account of Leyland and BREL documents. The
  arithmetic is internally consistent (20 × £400,000 = £8m; 50 × £340,000 = £17m) and consistent with
  the Class 210 comparison, which is why they are graded medium rather than low.

---

## S7. The strongest statements, verbatim

These are the sentences a later reader should be able to find without re-running the search.

1. **On first-generation DMU failures being design, not build** — BTC memorandum, 14 February 1955:
   "It was agreed that the troubles experienced could not be attributed to faulty workmanship either in
   Railway Workshops or by Contractors."

2. **On the same, from the engineer who lived with it** — Wakefield, RDP 2/71, 1971: "Mistakes were
   obviously made in many areas, the whole fleet was built in an amazingly short space of time, and
   because of this, there was little or no opportunity to incorporate the experience obtained in
   service into the vehicles as built."

3. **On body-mounted against underfloor engines** — Robertson, discussion in RDP 2/71: "the
   outstandingly good fire record of the diesel-electric multiple-unit trains of Southern Region which
   had body-mounted engines."

4. **On the Mk3's early structural trouble** — Power, IMechE 1978: "Following discovery of a fractured
   axle box on a Mark III locomotive hauled coach, an immediate survey of all HST coach axleboxes was
   undertaken and this resulted in a number of vehicles being withdrawn from service."

5. **On the Mk1 being heavy by design** — Divall and Shin, 2018: "most improvements to the Mk1 made a
   heavy design even heavier."

6. **On the Mk1's corrosion limit** — Bluebell Railway C&W: "it is, however, the condition of the door
   pillars which is the limiting factor on safety grounds, and will, if corrosion is unchecked, lead to
   the demise of any Mk 1 coach."

7. **On the Mk4 introduction** — BRB ECML completion certificate, 1992: "the decision to go for new
   designs in both the power units and the coaches was high risk and... we paid the price."

8. **On wagon standardisation** — *Facts and Figures about British Railways*, 1956: "By
   standardisation it has been possible to reduce the number of designs in current production."

9. **On the Pacer's transmission** — *Rail*, 26 August 2019: "26 of the 57 '142's based at Newton Heath
   depot in Manchester were out of service."

10. **On the PEP being a good machine** — *Modern Railways*, 21 November 2019: "They were lightweight
    and had all axles motored, which gave them terrific acceleration."

---

## S8. Recommended adjustment table

Apply to the fitted base price. Values in **bold** are build-cost rows and belong in `cost`; the rest
are reliability or whole-life and belong in a separate term.

| Domain | Class or item | Adjustment | Field | Confidence |
|---|---|---|---|---|
| rail-carriage | **Mk1, all variants** | **−5%** | cost | medium-high |
| rail-carriage | Mk1 corrosion | −10% | running / life | medium |
| rail-carriage | Mk1 crash structure | −5% | life | medium-high |
| rail-carriage | **Mk2** | **+5%** | cost | medium-high |
| rail-carriage | **Mk3 systems** | **+5%** | cost | medium |
| rail-carriage | Mk3 axlebox and discs, 1977-78 | −10% | running | high |
| rail-carriage | Mk3 late corrosion | −5% | life | medium |
| rail-carriage | Mk4 introduction | −10% | running | medium-high |
| rail-carriage | **Pullman and dining** | **+15%** | cost | medium |
| rail-carriage | Pre-grouping and Big Four | 0% | — | high |
| rail-wagon | **16-ton mineral** | **−10%** | cost | medium-high |
| rail-wagon | 16-ton mineral life | −5% | life | medium-high |
| rail-wagon | **Private owner** | **−15%** | cost | medium |
| rail-wagon | **Fitted stock** | **+10%** | cost | medium-high |
| multiple-unit | First-gen DMU design | −10% | running | high |
| multiple-unit | First-gen DMU fire | −5% | running | medium-high |
| multiple-unit | SR DEMU | +10% | running | medium-high |
| multiple-unit | **Pacer build** | **−15%** | cost | medium |
| multiple-unit | Pacer ride and track | −5% | life | low-medium |
| multiple-unit | **Sprinter** | **+10%** | cost | medium |
| multiple-unit | **PEP family** | **+10%** | cost | medium-high |
| multiple-unit | Class 508 only | −5% | running | low-medium |
| multiple-unit | **Class 455** | **−5%** | cost | medium |

**How to use the table without doing damage.** The adjustments are not additive across the rows for
one vehicle. A Mk3 is +5 build and −10 early reliability and −5 late corrosion; a parent that adds all
three gets −10 for a vehicle that was the mainstay of InterCity for thirty years. Pick one field per
row, as the "Field" column says.

---

## S9. Dead ends, recorded

1. **No RCTS volume is available online.** The carriage and wagon volumes are the obvious authority and
   are print-only. Not consulted.
2. **Institution papers are paywalled.** IMechE, IEE and Sage hosted the abstracts and, in two cases,
   full text through a third-party mirror (Power 1978, Watts 1989). Wakefield's paper exists only as
   the SteamIndex summary and the archive's description; the full text was not read.
3. **No National Railway Museum full-text catalogue.** The Pullman drawings list is a finding aid, not
   evidence; the NRM's curatorial text on coach types was not reachable.
4. **No RAIB or accident report bearing on carriage or wagon build cost.** Searches returned the 1987
   Walton-on-the-Naze buffer-stop collision (a 313 brake relay) and nothing on structural cost.
5. **No new-build wagon price.** The 16-ton mineral, the HAA hopper, the Freightliner flat and the
   Speedlink vans all lack a per-wagon price in the sources found. The Freightliner aggregate cannot be
   decomposed without an assumption.
6. **No per-class first-generation EMU reliability ranking.** The 1972 IEE paper is abstract-only.
7. **No source for the common claims about pre-grouping over-building** (LNWR weight, GWR finish, NER
   dining cars). These are enthusiast commonplaces; none surfaced in citable form.
8. **No Pullman build cost before 1923.** The archive's earlier cars carry tare and seating but the
   cost field is blank.
9. **No Mark 1 contract price.** The 1950s build was in BR workshops and in batch orders; no per-coach
   figure appeared in Hansard, the official *Facts and Figures*, or the press.
10. **The £0.19 per vehicle mile in Wakefield does not survive its own arithmetic.** It is a train-mile
    figure. Any model that uses it as a per-vehicle figure will overstate maintenance by the average
    formation length.

---

## S10. Confidence, and what not to do

**High confidence** (primary document or named engineer, mechanism stated): the first-generation DMU
design problems, the SR DEMU comparison, the Mk3 axlebox and disc brake failures, the Mk1's
heavy-but-corrodible structure, the 16-ton mineral wagon's volume and short life, the PEP family's
lightweight construction and longevity.

**Medium confidence** (trade press quoting a named person, or a company record read through a
secondary account): the Mk3 and Mk4 introduction stories, the Pacer and Sprinter prices and
reliability, the Pullman prices, the private owner wagon price.

**Low confidence**: the Pacer ride and crew-health penalties, the Class 508's Southern troubles, the
private owner wagon salvage value. These are recorded because the direction is not in doubt, but they
should not drive a figure on their own.

**Three things not to do:**

1. **Do not add a class term for weight.** Every heavy vehicle in this set (Mk1, Pullman, 16-ton
   mineral) is heavy for a reason the ladder already measures. The class term is for the part of the
   cost that is not weight.
2. **Do not put reliability discounts into `cost`.** A troublesome class that was cheap to buy would
   become even cheaper, which rewards the model for buying it. Reliability belongs in the monthly
   charge or in a service life.
3. **Do not compare nominal prices across 1979-1986 without deflating.** The Class 508 (1979-80) and
   the Pacer (1984) are close in nominal per-vehicle terms and about 30 per cent apart after
   inflation. The only comparison in this dataset that is safe without a deflator is the Pacer against
   the Sprinter, because they are the same years and the same buyer.

---

## S11. Overlap with earlier research and how to merge

`research-pricing-rows-8.csv` already holds eleven carriage rows, all of them **within-family price
differentials** from the NER, Midland, GWR and Highland records: six-wheel against bogie, steel against
wood, first against third, clerestory against arc roof, dining car against composite, and the LMS
gas-to-electric lighting conversion. Those are better than anything here for separating body, bogie and
finish.

This file does not repeat them. It adds:

- the **across-family** judgements (Mk1 to Mk4, Pullman, wagon classes, MU families);
- the **reliability** evidence, which report 8 did not attempt;
- the **contract prices** for the 1979-86 multiple units, which are the only clean per-vehicle figures
  in the set.

When merging, keep report 8's differentials as the calibration evidence and this file's rows as the
adjustment layer. They answer different questions.
