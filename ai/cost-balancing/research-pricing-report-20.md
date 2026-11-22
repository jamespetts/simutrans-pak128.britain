---
status: draft
verified: none
---
# Research pass 20: anecdotal evidence of build cost and reliability by locomotive class, pre-1948

**Covers**: statements and figures that a named British locomotive class, or a company's
locomotive practice, cost more or less to build than equivalent engines, or was more or less
reliable or more or less burdensome to maintain. Pre-grouping companies and the Southern Railway
to 1948. 63 rows in `ai/temp/research-pricing-rows-20.csv`.

Nothing under `New/` has been modified. No git command was run. No Simutrans `.dat` price was used
as evidence and no figure was fitted to the pakset.

Parent method: `New/ai/vehicle-cost-method.md` (the fitted ladder and the rule that a class term is a
small correction to a specification-based price). Sibling passes: pass 7 (feature premiums:
compounding, superheat, cylinders) and pass 8 (vehicle feature taxonomy). This pass does not repeat
them: it supplies the **class and company** terms that the feature premiums cannot express.

---

## 1. Method and confidence grades

The evidence falls into five kinds, in descending order of value:

1. **A matched pair of prices for the same design, same year, different builder.** The NER P3 of
   1908 is the only clean case found.
2. **A price with a specification**, which can be checked against the ladder.
3. **A stated mileage or cost interval** (miles between general repairs, repair cost per engine
   mile, miles per boiler stay change).
4. **An explicit statement by an engineer or works official**, with the mechanism given.
5. **A reputation in a secondary source**, with no mechanism.

Grades used in this report and in the CSV notes:

- **A** — a measured figure from a primary or near-primary record, or an arithmetic difference
  between two matched figures.
- **B** — an explicit statement by a named engineer, works official or specialist historian, with
  the mechanism stated.
- **C** — a single anecdote, a Wikipedia-only statement, or a figure whose scope is uncertain.

Every adjustment in the table below is a **multiplier on the price the fitted ladder already
produces for that class**, not on the class's `.dat` value. The bands are deliberately narrow
(5 to 20 per cent) because the underlying claims are qualitative and because the ladder already
absorbs most of the real cost differences through weight and power.

---

## 2. The result in one paragraph

The evidence supports small class terms in both directions, and it does **not** support the large
premiums that the anecdotes imply when read literally. The three claims with real numbers behind them
are all modest: the NER built its own P3 0-6-0 for about 15 per cent less than the cheapest
contractor quote for the identical engine (1908); the LNWR Precursor ran 6.6 per cent further between
general repairs than the Experiment built in the same works at the same time (1910); and the LNWR
0-8-0 was about 20 per cent lighter and cheaper to build than the GCR 2-8-0 it was tested against
(1919-20). The large anecdote — that the LNWR could build three 4-6-0s for the price of two GWR
Stars — is a 50 per cent claim and should be capped at +10 to +20 per cent.

The most important single check is on the Brighton average. Stroudley told the Institution of Civil
Engineers in 1885 that his 410 engines averaged £2,370 each including tenders, and that the expense
was "somewhat above the average" because of the material and workmanship. The ladder prices a
38.75-ton engine at about **£2,485**. Whether that is above or below the Brighton figure depends
entirely on the basis of the ladder:

- comparing nominal with nominal, £2,370 against £2,485 puts Brighton **4.6 per cent below** the
  ladder;
- bringing the 1885 figure to 1900 with the pakset's `vehicle purchase` index (1885 = 74) gives
  **£3,203**, which is **28.9 per cent above** the ladder.

The Brighton evidence therefore bounds a premium between about -5 and about +29 per cent and does
not settle it. Until the ladder's date basis is stated — whether its constants are nominal or 1900
constant — a Brighton build term cannot be more than provisional. The recommendation below uses
+5 per cent, the low end of that range, because the qualitative statements support a premium but no
figure does.

---

## 3. Findings by company

### 3.1 LBSCR (the largest single body of evidence)

The Brighton evidence is unusually good because Stroudley published his own costs to the ICE in
1885, and because Harold Holcroft, who worked at Brighton, left a detailed comparison with LSWR and
SECR practice.

**Build cost.** Stroudley's discussion reply gives:

- average cost of the 410 engines, £2,370 each including tenders, average age nine years;
- the Gladstone 0-4-2 for express work, with tender, at **£51 per ton**;
- the company average at **£67 per ton**;
- tank engines dearer per ton than tender engines, "in consequence of the greater amount of work in
  proportion to the total weight";
- the admission that "if the expense of the engines was somewhat above the average that must be
  pleaded as his excuse", on the grounds of the best material and workmanship.

J. C. Park of the North London Railway replied that Brighton engines were "charged to capital account
at the rate of nearly £2,800 per engine", and that the LNWR would have needed £113,954 more for
renewals on the same basis. He also said that "all the polish shown on the specimens exhibited was
not necessary for the proper working of an engine". That is a contemporary statement that Brighton
practice cost more than LNWR practice, from a hostile but informed witness.

The average figure can be checked against the ladder, and the check is ambiguous. At 38.75 tons the
ladder gives £2,485, which is 4.6 per cent above £2,370 on a nominal basis and 22 per cent below it
if the 1885 price is first brought to 1900 with the `vehicle purchase` index (74). The Brighton
average is therefore consistent with anything from no premium to about 29 per cent, and the
qualitative statements are needed to choose within that range. See section 2.

The B4 4-4-0 of 1900 is the only Brighton batch contract price found: **£3,250 each for 20 engines**,
approved by the Locomotive Committee (Marx, *Robert Billinton* p. 37).

**Reliability and maintenance.** Holcroft's comparison is the strongest class-level statement in the
whole pass:

> "All bogies for Brighton engines were individually sprung, and without exception all frames had
> patches where fractures had occurred in them, while quite a number had the frames duplicated by
> additional plates extending over the whole length. I never found one bogie which was not patched
> in some way... On the contrary, it was quite exceptional to find patched bogie frames on either
> the Eastern or Western Sections, which had the Adams type of bogie with equaliser bars..."

He adds that Brighton parts were not interchangeable between engines of a class, because the
erecting-shop chargemen had been allowed latitude in repairs. Both statements point the same way: a
maintenance penalty for Brighton engines relative to LSWR and SECR practice, with a stated mechanism
(individual springing against equaliser bars; absence of standardisation in the erecting shop).

The Marsh classes divide sharply and should not be given one class term:

- I1 and I2 4-4-2T: "very bad steamers", "wash-outs" (Burtt; Holcroft).
- I4: "grossly over-cylindered" (Holcroft).
- I3: the one success, and the reason is stated — it was "virtually a tank engine edition of
  Billinton's B4, which had a really good boiler", plus superheating (Holcroft).
- C3 0-6-0: "an indifferent performer", the running department preferring the rebuilt C2X.
- L 4-6-4T: rolling led to the derailment of all three coupled axles; the cure, a well tank below
  the barrel, needed the boiler lifted for access to it.
- K 2-6-0: "capable and reliable but more expensive to run" than the Maunsell N and Urie S15 in the
  1924 comparison (Bradley, RCTS part 3, p. 139), yet the K stayed sound while the N needed new
  frames and cylinders (p. 141).

### 3.2 LNWR

Two opposite policies sit in the same company.

**Cheap by design.** Brian Reed, on Whale's management: "The new policy at Crewe, quite clearly, was
the smooth and easy running of headquarters and various sub-departments, and complete simplicity
allied to cheapness in first cost of all new locomotives, the latter taken to such a degree that the
first large 4-4-2T had a rigid trailing axle to save the small extra expense of a radial axlebox."
Le Fleming, on Webb's 500 0-6-0 coal engines: "probably the simplest and cheapest ever built for a
main line. One of these was erected in twenty-five and a half hours." Reed also records that Crewe's
improvements gave "economy in construction and maintenance", and that locomotive cost per train mile
was lower in the 1880s than in the 1860s.

**Dearer when compound.** The SLS and the LNWR Society both state the general rule plainly:
compound engines "tend to be costlier to construct, maintain and repair than their single-expansion
fellows", and "with more cylinders and valve gear, a compound was inevitably more expensive to build
and maintain". That is a mechanism, not a class prejudice, and it matches the NER's measured
**£800 per engine** premium for its four-cylinder compound Atlantics.

**Measured maintenance interval.** Bowen Cooke reported in 1910 that Precursors ran **69,124 miles**
between general repairs against **64,835** for the Experiments: the same works, the same period, a
6.6 per cent difference attributed to coupled wheel diameter.

**Measured build comparison.** Talbot, on the 1919-20 trials, concludes that the LNWR G1 0-8-0 "had
the edge being 20 per cent lighter and cheaper to build" than the GCR 2-8-0.

**One counter-intuitive measured result.** T. M. Herbert's 1930 investigation at Springs Branch
found the round-top boiler ran **644 miles per firebox stay change** and the Belpaire only **244**,
a 164 per cent higher stay-change rate for the Belpaire. The proposed modification was not
implemented. This is a caution: the Belpaire firebox, which the GWR and SR adopted as good practice,
carried a boiler-maintenance penalty on the LNWR's own evidence.

### 3.3 GWR

**The famous claim.** The Stars were criticised in letters to *The Engineer* for being expensive to
build and maintain, and Churchward was asked by his directors why "the London and North Western
Railway could build three 4-6-0 locomotives for the cost of two of his". The reply is recorded as
"Because one of mine could pull two of their bloody things backwards". The story is sourced to Nock,
*The GWR Stars, Castles and Kings* (1980) p. 48. It is a 50 per cent claim, it is not
specification-matched (the Star was a heavier engine than the Experiment), and Nock is a
popular historian. Recommended band: +10 to +20, not +50.

**Against it.** Holcroft wrote that the Stars' advantages were "cheaply bought with the minimum of
added parts", and le Fleming that they were "remarkable free-running engines which rarely suffered
breakdown in service". The same class therefore carries a positive build term and a positive
reliability term, which is coherent: expensive to make, cheap to keep.

**Prices and intervals.** No. 2874 cost **£4,992** for the locomotive and **£6,193** with the tender
at Swindon in 1918; No. 2857 cost **£5,948** including tender in April 1918. A new Standard No. 1
boiler was **£971**; a heavy general in the 1930s **£450 to £700**; a boiler overhaul **£150 to
£700**. The 47xx class was booked for **100,000 miles between repairs** and achieved **300,000 miles
between heavy boiler repairs** on nine engines with one spare boiler.

**A contrary claim on frames.** David Jackson, Robinson's biographer, states that although GWR and
GCR frames used the same 1.25 in steel, "Swindon's frames were far less robust in their construction
and forever prone to constant patching and strengthening", while the GCR 8K frame "ensured low
maintenance costs, minimal lost time for repairs and gave high reliability". This is a GCR
partisan's claim and is graded C, but it is specific and it names the mechanism (frame assembly,
stretchers, cylinder casting bolted to the frame).

### 3.4 Midland

The Midland is the clearest case of a company policy with a stated economic reason: a small number of
standard designs, built in large numbers at Derby, each "cheaper to build and run than a larger
equivalent", with longer service lives because the engines were lightly loaded. The 4F 0-6-0 is
described by the Midland Railway Society as "very robust, while cheap in construction and repair due
to careful design and reliable fittings and auxiliaries", and it made up 10 per cent of the LMS fleet
at nationalisation.

The counter-evidence is specific: the standard Midland axlebox was sized for that light loading, and
ex-Midland engines suffered frequent axle-bearing failures in the 1920s once the LMS worked them
hard. That is a reliability penalty conditional on duty, not a property of the design in isolation.

The only Midland price found is late: No. 4422, built at Derby in 1927, at a book cost of **£3,217**
plus **£1,000** for the tender. No pre-1923 Midland contract price was found.

### 3.5 NER

**The best matched pair in the pass.** In 1908 Darlington built ten P3 (LNER J27) 0-6-0s at
**£2,986 each**. In the same year the same design was ordered from Robert Stephenson at **£3,537**,
North British Locomotive at **£3,500** and Beyer Peacock at **£3,550**. The internal price is 14.7 per
cent below the cheapest quote and 15.6 per cent below Stephenson. Source: Irving (1976) p. 109,
citing PRO RAIL 527/1397, reproduced in Boughey's paper on internalisation.

**Compounds.** The NER's four-cylinder compound Atlantics cost about **£800 each more** than the
two-cylinder Atlantics, roughly 30 per cent on an Atlantic of the period. Their repair burden is
stated by the Gateshead district inspector in 1931: "I am very glad I only have two, as they are
definitely much heavier in repairs compared with the simple Atlantic engines doing a similar class of
work." The Worsdell two-cylinder compounds went the same way: the Locomotive Committee resolved in
1894 not to build more, because the coal saving did not cover the higher repair cost, and all 171
were eventually converted to simples.

**Durability.** D20 4-4-0 No. 2011 ran **284,182 miles** to its first general overhaul in March 1903;
the rest of the first batch averaged **163,000 miles**. The T2 (Q6) 0-6-0 is described by Nock as
having "almost unfailing reliability".

**A warning against a simple NER bonus.** Hill's 1895 ICE paper puts NER locomotive maintenance at
**4.40d per train mile**, the highest of nineteen companies, against **2.04d** on the LSWR and an
average of 2.51d. Hill notes the NER was charging new engines to revenue and later transferring them
to capital, which distorts the comparison. Any company-level NER adjustment must therefore be
class-specific, not corporate.

### 3.6 GCR

The 8K (LNER O4) is the best-evidenced reliable class in the pass, on two independent statements:
Jackson's on the frame construction and Robinson's insistence on "the most rugged assembly", and
Westwood's that "its general lack of sophistication meant that it was virtually immune to poor
maintenance". The 8K was chosen as the ROD standard and 521 were built, which is itself evidence of
reputation. The J11 0-6-0 ("Pom-Pom") is described as versatile and reliable over fifty years, but on
weaker sources.

The GCR 2-8-0 is also the engine against which the LNWR 0-8-0 was measured as "20 per cent lighter
and cheaper to build", so the two rows should be read together: the GCR engine is the expensive side
of that pair.

### 3.7 GER

The GER evidence is about production efficiency rather than about individual classes. C. J. Allen:
Holden's reorganisation of Stratford, "together with a considerable degree of standardisation,
brought Stratford to an exceptionally high position among British locomotive works in the speed and
efficiency of its locomotive production", and his classes "were rugged in design and with their
massive working parts have paid handsome dividends in reliability and ease of maintenance". The GER
Society adds that only five standard boilers were in production by the mid-1890s, that more than half
the fleet used the Y14 boiler alone, and that the Y14/J15 was erected in **9 hours 45 minutes** in
1913, halving the previous British record of 25 hours 30 minutes set by a Webb 0-6-0 at Crewe. That
record is a direct, if crude, measure of labour content per engine.

The Stratford "Letter Accounts" are the most promising archival lead in the pass: a new account was
opened for each batch of new engines, and building costs and subsequent maintenance were recorded
against it, so an average cost per locomotive could be established. The GER Society describes the
system; the accounts themselves were not consulted.

### 3.8 NBR

**In-house against contractor, with a price.** In January 1909 the NBR contracted with the North
British Locomotive Company for six Scott 4-4-0s at **£3,290 each**. In 1911 Cowlairs built ten more
at the same stipulated price. When NBL was later offered a further batch at "not more than £3,000" it refused,
and Cowlairs built them within that price — about 9 per cent below the 1909 contract rate. This is a
second, independent case of in-house building beating the trade price, and it is smaller than the
NER's 15 per cent.

**Construction and reliability.** Reid's engines are described as "very robust, solid construction",
with "nearly every structural component made just a little larger and heavier than had been the case
in Holmes's time" — heavier and dearer, in other words, and long-lived. The Atlantics are the
counter-example: rough riding, broken rails and spread track, a 55 mile/h limit imposed by the civil
engineer, and nearly two years of trouble before they settled down. The Scotts had "a somewhat
doubtful reputation as saturated engines" and were "regarded as good engines once superheated".

### 3.9 Caledonian

The Caledonian is the clearest case of a class whose reliability and maintenance reputation is
negative for a stated mechanical reason. The 600 class 0-8-0 cost **£3,000 each** in 1901 and the
492 class 0-8-0T **£2,250 each** in 1903-04, which are useful absolute prices. But the 600s had
"spiral rear springs which were difficult to maintain", "heavy slide valves [which] were also
difficult to maintain", and "tended to go off beat very quickly". Dunbar's verdict, quoted by
SteamIndex, is that they were "brutes", and they were withdrawn by 1930. This is a case where a
maintenance penalty is better supported than a build-cost penalty.

### 3.10 Highland

The Jones Goods were ordered as a single contract of fifteen at **£2,795 each** in 1894, which is a
clean price for a whole class. A Lochgorm Works foreman, interviewed in 1958, said "the Jones Goods
were excellent engines and never experienced broken springs", while the Clan Goods and the Skye
Bogies were "troublesome". The River class of 1915 is the negative case: rejected as too heavy before
delivery and sold to the Caledonian, with the steam reverser the main problem in service.

### 3.11 LSWR

The LSWR supplies the clearest statement that high build cost bought durability. Eric Forge, on
Urie's 4-6-0s: main frames of 1.25 in plate were "the heaviest yet used on a British locomotive"; the
axle journals were much larger than Drummond's and used "a large manganese brass bearing with white
metal lining. They were heavy and expensive - but they lasted! Even after the normal spell of 75,000
miles between general overhauls, the boxes were often found to require only minimal attention." That
is a mechanism, an interval and a cost direction in one paragraph, and it is the best single
justification in the pass for a positive build term paired with a positive reliability term.

The negative cases are class-specific: the L11's marine-type big ends "were a big problem", and the
T9's cross-water firebox tubes were "difficult to maintain" and were removed. Hill's 1895 figure of
**2.04d per train mile** is the lowest locomotive maintenance of nineteen companies, which supports a
company-level LSWR maintenance advantage but cannot be assigned to a class.

### 3.12 SECR

The SECR is thinly evidenced. The C 0-6-0 is "robust, but of simple construction", "gave little
trouble in traffic", and 107 of 109 passed to BR — a cheap and reliable goods engine. The N 2-6-0 is
the counter-case: "lightly braced frames" gave excessive vibration, frames were later replaced and 29
engines needed new cylinders between 1955 and 1961. The N class was also nicknamed the "Woolworths"
for the low price of the Woolwich Arsenal batch, which is a build-cost statement in a nickname rather
than in a figure.

---

## 4. Recommended adjustments

Apply as a multiplier to the ladder price. Where a row says "maintenance" or "reliability", apply to
`runningcost`/`fixed_cost`, not to `cost`. Do not stack a class term with a pass 7 feature premium
for the same feature (for example, do not apply both the LNWR compound term and the pass 7
compounding premium).

| Class or company | Applies to | Direction | Factor | Basis | Grade |
|---|---|---|---|---|---|
| LBSCR all classes, 1885-1922 | cost | + | 5% | Stroudley's own admission of expense above average; Park's £2,800 capital charge against LNWR practice | B |
| LBSCR all classes | runningcost | + | 10% | Patched bogie frames, non-interchangeable parts (Holcroft) | B |
| LBSCR I1, I2, I4 | runningcost | − | 10% | Bad steamers, over-cylindered | B |
| LBSCR L 4-6-4T | runningcost | + | 10% | Instability and inaccessible well tank | B |
| LBSCR K 2-6-0 | runningcost | +5 / −5 | mixed | Dearer to run, cheaper to keep (Bradley) | B |
| LNWR Coal Engine 0-6-0 | cost | − | 10% | Simplest and cheapest main-line engine; 25.5-hour erection | B |
| LNWR Whale/Bowen Cooke classes | cost | − | 5% | Crewe policy of cheapness in first cost (Reed) | B |
| LNWR Webb compounds | cost | + | 10% | Compounds costlier to build (SLS, LNWR Society) | B |
| LNWR Webb compounds | runningcost | − | 5% | Erratic and temperamental, but contested | C |
| LNWR Precursor | runningcost | + | 6.6% | 69,124 against 64,835 miles between general repairs | A |
| LNWR G1 0-8-0 | cost | − | 10% | 20% lighter and cheaper than the GCR 8K; capped | B |
| GWR Star | cost | + | 10% | "Three for two" against the LNWR; 50% claim capped | C |
| GWR Star | runningcost | + | 5% | Rarely suffered breakdown in service (le Fleming) | B |
| GWR all classes | runningcost | + | 5% | Frames prone to patching (Jackson, GCR source) | C |
| Midland 4F and standard classes | cost and runningcost | − | 5% | Cheap in construction and repair; small-engine policy | B |
| Midland standard classes under hard work | runningcost | − | 5% | Axlebox sized for light loading; failures under LMS | C |
| NER works-built batches | cost | − | 15% | P3 built at £2,986 against £3,500-3,550 quoted | A |
| NER four-cylinder compounds | cost | + | 10% | £800 each above the simple Atlantic; capped | B |
| NER four-cylinder compounds | runningcost | − | 10% | Much heavier in repairs (Schlegel) | B |
| NER D20, Q6 | runningcost | + | 5% | 284,182 and 163,000 miles to first overhaul; "unfailing reliability" | B |
| GCR 8K/O4 | runningcost | − | 5% | Frame construction gave low maintenance, high reliability | B |
| GCR 8K/O4 | runningcost | + | 5% | Immune to poor maintenance (Westwood) | B |
| GER Y14/J15 and Holden classes | cost | − | 5% | Simple standard design; 9 h 45 min erection | B |
| GER Holden classes | runningcost | + | 5% | Rugged, easy to maintain (Allen) | B |
| NBR Scott | cost | − | 9% | Cowlairs beat the contractor's £3,000 floor | B |
| NBR Atlantics | runningcost | − | 5% | Rough riding and track damage until sorted | B |
| Caledonian 600 | runningcost | + | 10% | Springs and slide valves difficult to maintain | B |
| Caledonian 600 | runningcost | − | 5% | "Brutes"; withdrawn by 1930 | C |
| Highland Jones Goods | runningcost | + | 5% | Never broke a spring | C |
| Highland River | runningcost | − | 5% | Steam reverser trouble; rejected as too heavy | B |
| LSWR Urie 4-6-0s | cost | + | 10% | Heaviest frames yet used; "expensive but they lasted" | B |
| LSWR Urie 4-6-0s | runningcost | + | 10% | Axleboxes needed minimal attention at 75,000 miles | B |
| LSWR L11 | runningcost | − | 5% | Marine big ends a known problem | B |
| SECR C | cost | − | 5% | Robust but of simple construction | B |
| SECR C | runningcost | + | 5% | Gave little trouble in traffic | B |
| SECR N | runningcost | + | 5% | Lightly braced frames; later frame and cylinder renewal | B |

Rows where the factor is a real price rather than a factor are in the CSV with
`price_unit = GBP`, `GBP per ton`, `miles...` or `pence...`, and must not be averaged with the
percentage rows.

---

## 5. The strongest statements in the pass

Ranked by evidential value, not by size of effect.

1. **NER P3, 1908: £2,986 in-house against £3,500 to £3,550 from three contractors for the identical
   engine.** A matched design, a matched year, four builders, and an archival source (PRO RAIL
   527/1397) quoted by a published economic historian. This is the only clean measurement of the
   value of in-house building found.
2. **Holcroft on Brighton bogie frames.** Every Brighton bogie frame patched or duplicated; "quite
   exceptional" on the Adams-bogie engines of the LSWR and SECR. A named engineer, a stated
   mechanism, a direct comparison between companies, and a maintenance consequence.
3. **Bowen Cooke's 1910 repair intervals: 69,124 miles (Precursor) against 64,835 (Experiment).**
   Same works, same period, same traffic; the only measured class-against-class interval found.
4. **Forge on Urie's axleboxes: "They were heavy and expensive - but they lasted!"** with the
   75,000-mile general overhaul and the minimal attention found there. The clearest statement in the
   pass that a build-cost premium bought durability.
5. **Stroudley's own costs, 1885: £2,370 average per engine, £51 per ton for the Gladstone against
   £67 average, and an admission of expense above average.** A primary source from the engineer
   responsible, and the only case where the ladder can be checked directly against a company average.
6. **Schlegel, 1931: the NER compound Atlantics "definitely much heavier in repairs" than the simple
   Atlantics.** A repair officer's judgement in an Institution discussion, with the comparison
   specified.
7. **Talbot on the LNWR G1 against the GCR 8K: "20 per cent lighter and cheaper to build".** A
   specification-normalised build comparison between two classes, from trial data.

---

## 6. Prices found (usable as ladder evidence)

| Year | Class | Price | Scope | Source | Grade |
|---|---|---|---|---|---|
| 1885 | LBSCR, all classes | £2,370 | average per engine, with tender | Stroudley, Min. Proc. ICE 81 | A |
| 1885 | LBSCR Gladstone B1 | £51 per ton | with tender | Stroudley, Min. Proc. ICE 81 | A |
| 1894 | Highland Jones Goods | £2,795 | per engine, 15 ordered | Preserved British Steam Locomotives | B |
| 1900 | LBSCR B4 | £3,250 | per engine, batch of 20 | Marx, *Robert Billinton* p. 37 | B |
| 1901 | Caledonian 600 0-8-0 | £3,000 | per engine | Dunbar, *Railway World* 24 | B |
| 1903 | Caledonian 492 0-8-0T | £2,250 | per engine | Dunbar, *Railway World* 24 | B |
| 1908 | NER P3, Darlington | £2,986 | per engine, internal | Irving (1976) p. 109 | A |
| 1908 | NER P3, Stephenson | £3,537 | per engine, contract | Irving (1976) p. 109 | A |
| 1909 | NBR Scott | £3,290 | per engine, contract | Cameron, NBR SG Journal 140 | A |
| 1912 | NBR superheated Scott | £2,990 | per engine (pair £5,980) | Cameron, NBR SG Journal 140 | C |
| 1918 | GWR 2874 | £4,992 / £6,193 | loco / with tender | 2874 Trust, GWR records | B |
| 1918 | GWR 2857 | £5,948 | with tender | 2857 Society | B |
| 1918 | GWR Standard No. 1 boiler | £971 | new boiler | 2874 Trust | B |
| 1927 | Midland/LMS 4F 4422 | £3,217 / £1,000 | loco / tender book cost | 44422 Locomotive Company | B |
| 1930 | SR S15 No. 830 | £6,585 | cost when new | Locobase, citing Maunsell Society | C |

The last of these and the 1912 NBR figure are the two whose scope is uncertain; both are marked C.

---

## 7. Dead ends

Recorded so that a later pass does not repeat them.

- **No published table of average locomotive cost per company was found.** The *Railway Year Book*
  1903 and 1913 have "Costings" sections (HathiTrust; Railway Citation Index item 339632) but the
  pages could not be read in this pass.
- **R. P. Williams, "On the serviceable life and average annual cost of locomotives in Great
  Britain", Min. Proc. ICE (1909)** is exactly the right paper — serviceable life by company — but
  only the abstract is exposed; the full text is behind the ICE paywall.
- **A. J. Hill's 1895 paper** was readable only in part; the per-company tables are the valuable part
  and were not extracted beyond the figures quoted above.
- **The claim that Brighton engines were "more expensive to construct than the neighbouring
  companies' machines"** appears in a 2018 forum post citing an unidentified WordPress page. It was
  not used. The same post's claim about higher maintenance from leading-wheel flange wear is also
  unverified, though Ahrons independently notes that the Gladstone's large leading tyres were
  "expensive to re-turn or replace".
- **RCTS volumes** (Bradley LBSCR, Le Fleming GWR, RCTS LNER, Cormack and Stevenson Highland) were
  not available online; quotations reached through SteamIndex and through Wikipedia's citations
  only.
- **LNWR class contract prices**: Crewe built in-house and no published per-class price was found.
  The £2,800 per engine in Park's 1885 remark is a capital-account charge, not a Crewe cost.
- **Midland pre-1923 prices**: only the 1927 Derby book cost was found.
- **SECR D and C contract prices**: not found, although the builders and batch sizes are known
  (Neilson Reid and Sharp Stewart, 1900).
- **Highland pre-1894 prices**: not found.
- **National Archives cost ledgers**: PRO RAIL 527/1397 (NER) and PRO RAIL 254/19 (GWR) are cited by
  Boughey and by Irving and would settle both the internal-cost question and the overhead allowance
  question. They are not digitised.

---

## 8. Largest gaps

1. **No measured build cost for an LNWR, Midland or SECR class before 1923.** These are three of the
   four largest fleets and the pass has reputation but no price for them.
2. **No specification-matched cross-company price pair except the NER P3.** The whole class-term
   question would be settled by two or three more pairs of that kind (same design, same year,
   different builder or company).
3. **Reliability evidence is qualitative outside four cases** (LNWR Precursor/Experiment intervals,
   NER D20 overhaul mileages, GWR 47xx intervals, LSWR 75,000-mile spell). The Board of Trade
   returns and the companies' own repair accounts would give failure rates and costs per engine
   mile by class; neither was accessible.
4. **Nothing on Scottish companies beyond single anecdotes**, and nothing at all on the GNSR, FY,
   L&Y or N Staffs, which the pakset also covers.
5. **The "expensive but durable" pairing is only demonstrated for the LSWR** (Urie) and asserted for
   the LBSCR. For the LBSCR the check against the ladder is ambiguous by a factor of 1.35, so the
   claim needs either a specification-matched comparison or a settled ladder basis before it can be
   applied with confidence.

---

## 9. How to apply this, and what not to do

- Apply class terms **after** the ladder, as a single multiplier, and record the row number from the
  CSV beside the value.
- Do not apply a build term and a feature premium for the same physical feature. The LNWR and NER
  compound rows in this pass overlap the pass 7 compounding premium; use one or the other.
- Do not apply a company-wide term and a class term together at full value. The company terms here
  (LNWR cheapness, Midland cheapness, Brighton expense) are policies that the class terms already
  express.
- Reliability terms belong in `runningcost` or `fixed_cost`, not in `cost`. The engine charges
  `cost` once and the monthly fields every month, so a reliability term placed in `cost` would be
  charged once and then forgotten.
- Treat the Brighton positive term as provisional. The 1885 average of £2,370 per engine lies
  between 5 per cent below and 29 per cent above the ladder's £2,485, depending on whether the
  ladder's constants are nominal or 1900 constant. Settle that basis before relying on the term.
- Nothing here is strong enough to justify more than 20 per cent in either direction, and most rows
  justify 5 per cent.

## Open questions

- Are the constants in the fitted ladder nominal or 1900 constant? The Brighton average price cannot
  be tested against the ladder until this is settled, and the answer moves the implied Brighton
  premium by about 34 percentage points.
- Did Brighton engines carry more weight per unit of power than LSWR or SECR engines of the same
  class? If so, the "expensive" reputation is a specification effect and needs no class term at all.
- Is the NER £800 compound premium measured against the simple Atlantic with or without tender, and
  at what date?
- Can the Railway Year Book costings pages be read from a library copy, to give a company-by-company
  average cost per engine for 1903 and 1913?
- Do the GER Stratford Letter Accounts survive, and where? They would give a per-batch build cost for
  every GER class from the 1860s to 1922.
