---
status: draft
verified: none
---

# Research report 14: measured British maintenance costs of railway signalling, incandescent against LED

**Covers**: maintenance of mechanical semaphore, colour-light incandescent and LED signals; lamp and
head economics; signalling maintenance per SEU and per route km from Network Rail's regulatory
accounts and the ORR periodic reviews; signalbox operating and apparatus maintenance; traffic
signals as a cross-check on LED economics.

All figures are nominal money of the year stated. No deflation has been applied anywhere in this
report or in `research-pricing-rows-14.csv`, except where a figure is explicitly labelled as
inflated or restated. No Simutrans `.dat` price was used as evidence, and no figure was fitted to
the pakset. Nothing under `New/` was modified and no git command was run.

Evidence base: 70 rows in `research-pricing-rows-14.csv`. Domains: 20 signal, 16 signalbox,
19 signalling-system, 15 traffic-light. The pakset has 164 signal objects and 21 signalbox objects,
and the maintenance workbook has no class maintenance value for any of them; this report supplies
rates for the classes, not for individual objects.

---

## 1. The answer in one page

1. **A lineside colour-light signal cost about £56-142 a year to maintain in 1959-62, and about
   £825-900 a year by 2019, in nominal money.** The 1959 figure is the residual additional annual
   charge on the Kent Coast scheme after interest is removed; the 2019 figure is the measured £750 a year
   saving from replacing a filament signal and its structure with a self-cleaning LED signal, plus
   an inferred residual LED cost. The nominal rise is about 5-16 times. A real comparison is not
   robust, because the 1959 figure is a marginal residual and the 2019 figure is a saving rather
   than a measured total; the two are anchors, not a deflated series.

2. **A self-cleaning LED signal saves about £750 per signal-year against a filament signal and
   structure (2019), or about £270 per signal-year for the signal alone, structure not mentioned
   (2005 values).** That is roughly 80-90 per cent of the lineside signal-plus-post maintenance
   cost, and it is the strongest confirmation of the "LED costs less to maintain" intention.

3. **The saving does not come from the LED as such. It comes from removing the annual maintenance
   visit.** Network Rail's own reliability-centred maintenance standard still requires an annual
   visit for "all other LED and filament signals"; only the Unipart Dorman iLS and CLS LITE signals
   are designated self-cleaning and require no visit where exposed to free-falling rain. A
   retrofit LED head that keeps the annual visit saves only the lamp changes and the energy, which
   is a much smaller share of maintenance — perhaps 10-20 per cent, not 80-90 per cent.

4. **The "LED costs more to install" half of the intention is not supported for a British railway
   signal-plus-post object.** The only British railway evidence found in this pass on the
   installed-cost direction is the Unipart Dorman LNE case, which reports a 40 per cent cost saving
   on structure renewal and a 60 per cent reduction in changeover time, because the LED head is
   lighter and the structure simpler. The LED head unit itself may cost more: the traffic-signal
   evidence is £150 for an incandescent head against £600-700 for an LED head in 2006, a premium of
   about four times. There is no measured British railway pair of LED and incandescent head prices.
   The capital premium, if any, belongs to the head, not to the post and structure.

5. **The system total is the right check on the per-signal figures.** Network Rail spent £167m on
   signalling core maintenance in 2011-12, which is £2,594 per SEU-year at the 2011 SEU count of
   64,373, or £10,537 per route-km-year. In 2023-24 the combined signalling and telecoms
   maintenance line was £325m, which is £5,135 per SEU-year at the 2023 count of 63,295, or
   £20,507 per route-km-year. The 2023-24 figure is an upper bound because it includes telecoms;
   a like-for-like signalling-only estimate is about £3,800-4,300 per SEU-year.

6. **The lineside signal is a small part of the system total.** At £825-900 per signal-year, and
   about 0.63 signals per SEU (40,000 signals against 63,295 SEU), the lineside signal carries
   about £520-570 of the £3,800-4,300 per SEU-year. The rest — interlocking, control, track
   circuits, testing, supervision and fault response — belongs to the signalbox or system object,
   not to the signal object. That is a smaller share than the 20-40 per cent capital apportionment
   in report 12, but the direction is the same: the lineside signal is a minority of the total.

7. **Signalbox operating cost is dominated by staff, not apparatus.** A signaller FTE cost
   £62,917 in 2023-24. A continuously manned single-manned box needs about 4.31 FTE at 39 hours a
   week before holiday cover, so its operating cost is at least £271,000 a year. A 12-hour box is
   at least £135,500. Apparatus maintenance is a small fraction of that: the measured historic
   figures are £6.30 a box-year at Spetisbury in 1901, £1.38 a lever-year on the LNWR in 1884, and
   £80.35 a box-year for a 48-lever electro-pneumatic frame at Derby in 1908.

8. **Traffic signals corroborate the direction and the order of magnitude.** A West Sussex
   maintenance contract cost £380,000-400,000 a year for 248 monitored sites in 2020, or
   £1,532-1,613 per site-year. TfGM reports a £600,000 a year maintenance saving across 1,800
   sites, or £333 per site-year, from replacing 52,000 incandescent bulbs with LED aspects. That is
   about 20-22 per cent of the West Sussex total, not 80-90 per cent: the road-signal saving is
   smaller because the annual visit is not removed, only the lamp changes and energy.

---

## 2. Method and evidence grades

The evidence is graded as follows:

1. **Measured account or contract** — an actual tender, contract sum, company account or
   regulatory statement, with its scope stated.
2. **Primary engineering description with a cost** — an IRSE paper, an ICE discussion, or a
   Network Rail standard that states a cost or a maintenance interval.
3. **Supplier case study** — a manufacturer's quantified claim. Useful, but marketing, and not
   independently audited.
4. **Derived** — arithmetic on a measured figure, with the arithmetic shown.
5. **Inference** — an assumption needed to bridge a gap. Every inference is labelled.

Where a source is a PDF, it was downloaded and the text extracted. Several ORR PDFs had to be
retrieved from the Wayback Machine because the live site returned HTML. The 1885 ICE discussion
was paywalled: the figures are from the search extract of the article, not from a full-text read,
and are graded low confidence. The Liverpool City Region business case was blocked by Cloudflare:
its figures are from the search extract and are graded low confidence.

---

## 3. Mechanical semaphore maintenance, 1870s-1930s

### 3.1 Per lever and per signal

The best British series is the London and North Western Railway evidence in the 1885 Institution
of Civil Engineers discussion. F. W. Webb gave the maintenance cost per lever for the half-year
ending 1874 as £1 3s 8d, and for the half-year ending 1884 as 13s 10d. Doubled to annual figures:

| Year | Per lever-year | Nominal |
|---|---|---|
| 1874 | £1 3s 8d per half-year | **£2.37** |
| 1884 | 13s 10d per half-year | **£1.38** |

The 1884 figure includes ordinary maintenance and extensions whose cost did not exceed £10. The
fall from 1874 to 1884 is attributed to stronger locking gear. The same discussion records a Great
Northern claim that locking maintenance had not cost 10d per lever per annum, but that figure is
so far below the LNWR's that it is recorded and not used.

The KB's 1873 figure of £27 a lever with maintenance at 10 per cent a year gives £2.70 a
lever-year. That sits between the LNWR's 1874 and 1884 figures. The 10 per cent rate is much higher
than the apparatus-only rate at Spetisbury in 1901 (1.4 per cent of the box and apparatus cost),
which suggests the 10 per cent includes renewals or heavy maintenance, not apparatus alone.

At Spetisbury in 1901, a 9-lever box with eight semaphores and block instruments cost £6.30 a year
in apparatus maintenance, with no manning. That is **£0.70 a lever-year** and **£0.79 a
signal-year**. The apparatus-only cost is therefore about £1-3 a signal-year across the period,
before lamp oil and before manning.

### 3.2 Lamp oil and the £3 figure

The KB records "an oil signal lamp cost about £3 a year all in (1885)". The 1885 discussion does
not say that. It says the new petroleum lamp **saved** about £3 per lamp per annum, and that
applying it to all the LNWR's signal lamps would save over £40,000 a year. The £3 is a saving, not
a cost. This is a KB conflict, recorded in section 13 below.

The same discussion gives about £5 per signal-year for an additional second light, which the elbow
sidelight avoided. The absolute cost of lighting a signal lamp in 1885 is therefore not measured;
the saving from the petroleum lamp is.

### 3.3 Manning and the box

The KB records three men per box at £60 a man-year in 1873, which is **£180 a box-year** for
manning alone. In 1909 a small mechanical box with its signals and instruments cost about £150 a
year to man and maintain. That £150 cannot be three men at 1873 wages, let alone 1909 wages; it is
consistent with one man plus apparatus, or with a box that was switched out for part of the day.
The figure is recorded as stated, with that caveat.

The LMS gives a large-scale check: the abolition of 190 signal boxes in 1931-35 reduced costs by
£60,000 a year, or **£315.79 a box-year**. That is an operating-cost saving, including staff and
apparatus, and it is the best 1930s British figure for the whole cost of keeping a box open.

### 3.4 What a mechanical signal cost to maintain

Adding the apparatus share (£0.8-2.0 a signal-year) to the lamp share (a few pounds a year) gives
a lineside maintenance cost of about **£4-7 a signal-year in the 1880s-1900s**, rising to about
**£8-12 a signal-year by the 1930s**. Manning is separate and belongs to the signalbox, not to the
signal. These are the figures to use for the mechanical signal objects; the per-lever figures are
for the signalbox frame.

---

## 4. Colour-light incandescent maintenance, 1950s-2010s

### 4.1 The Kent Coast scheme, 1959-62

The Tyler 1962 IRSE paper's Appendix E gives the complete cost and apparatus count for the Kent
Coast electrification signalling. Phase I (1959) cost £4.3m for 97 route miles, with 361
multiple-aspect signals, 279 shunt signals, 930 track circuits and 275 point machines. The paper
states net increased annual charges, including interest at 6 per cent, of **£193,000**.

The like-for-like renewal value was £1.94m, so the additional capital was £2.36m. Interest at 6 per
cent on £2.36m is £141,600, leaving **£51,400 a year** for the additional maintenance and renewal
charge. The discussion in the paper used £2.46m and arrived at £45,000; the difference is recorded,
not resolved. The £51,400 figure is the arithmetic consistent with the paper's own Phase I
like-for-like renewal value.

Derived rates:

| Measure | Value | Arithmetic |
|---|---|---|
| Total annual charge per route km | £1,236 | £193,000 / 156.1 km |
| Residual maintenance per route km | £329 | £51,400 / 156.1 km |
| Residual maintenance per running signal | £142 | £51,400 / 361 |

The £142 per running signal is an upper bound: the same residual also covers 279 shunt signals,
930 track circuits and 275 point machines. Allocating the residual across 915 signal and point SEUs
gives about £56 per SEU-year, which is the better central figure for a lineside signal in 1959.
The truth for the signal object is therefore **£56-142 a signal-year**, and the £142 end is only
defensible if the whole residual is loaded onto running signals.

The important qualitative finding is in the discussion: the new colour-light installation had
**higher** maintenance and renewal charges than the mechanical signalling it replaced. Tyler says
the difficulty in showing a return "lies in the fact that mechanical signalling is much cheaper than
power signalling", and that "bearing in mind the increased maintenance and renewal charges for the
new installation ... there may well be an annual debit". Colour light was not sold on maintenance
savings; it was sold on capacity and safety.

### 4.2 Lamp life and lamp economics

The 1962 paper gives the incandescent lamp economics in unusual detail:

- The SL17 lamp was **rated at 1,000 hours**.
- The Southern routinely put new lamps in the red and yellow aspects, ran them for **4,000 hours**,
  then moved them to the green aspect for another **4,000 hours** — about **8,000 hours** in all.
- There were about 8,000 lamps in service and about 16 total failures a year, a 0.2 per cent total
  failure rate.
- The Western Region used tripole lamps, did not set up routine changing, and ran them until the
  main filament failed; it got "a life several times better than the rated 1,000 hour".
- The independent double-filament lamp was a **12-volt 16/24-watt** lamp. The proving circuits it
  required added **£50-70** to the cost of each signal.

The later standard lamp is the SL35 long-life filament, rated at **8,000 hours** in the 2025
Network Rail standard. At 100 per cent duty that is 0.91 years; at 50 per cent duty, 1.83 years. A
red aspect is lit for most of the time, so a filament red lamp is effectively an annual replacement.

### 4.3 What a colour-light signal cost to maintain

The measured anchors are:

| Year | Rate | Basis |
|---|---|---|
| 1959 | £56-142 per signal-year | Kent Coast residual, per SEU or per running signal |
| 2005 | £270.73 per signal-year saving | Unipart: £4.061m over 15 years for 1,000 signals |
| 2019 | £750 per signal-year saving | Unipart LNE: signal and structure, self-cleaning LED |

For the first colour-light era, 1926-1949, no British maintenance figure was found. The 1950-1970
anchor is the nearest, but the direction of the difference is not established: the early
installations were simpler, while labour was cheaper and the lamps were less reliable.

The 2005 figure is the saving from eliminating the annual maintenance visit on a filament signal.
The 2019 figure is the saving from eliminating the annual visit and reducing the structure
maintenance on a signal plus post. The 2019 figure is therefore the right comparator for a pakset
signal object that represents a post with its arms or lamps, mechanism and share of the wires.

The nominal rise from £56-142 in 1959 to £750-900 in 2019 is about 5-16 times. A real-terms
comparison is not robust: the 1959 figure is a marginal residual over the mechanical installation,
and the 2019 figure is a saving rather than a measured total. The two figures are useful anchors at
either end of the colour-light era, not a deflated series. The modern figure is not a different
order of magnitude from the 1959 figure in nominal terms, but no stronger claim is supported.

---

## 5. LED maintenance and lamp/head economics, 2000s-2026

### 5.1 The measured saving

Two British railway case studies give a quantified maintenance saving:

| Year | Saving | Scope | Source |
|---|---|---|---|
| 2005 values | £270.73 per signal-year | 1,000 filament colour-light signals, structure not mentioned, annual visit eliminated | Unipart Dorman, December 2015 |
| 2019 | £750 per signal-year | Over 20 signals and structures a year, LNE, signal plus structure | Unipart Dorman, July 2019 |

The 2005 case is explicit about the mechanism: "previously these signals would have required an
annual check, involving a minimum of two track workers. With the new maintenance standard, we are
removing the need for these visits." The 2019 case is explicit about the scope: "£11,000 in whole
life benefits ... by reducing the maintenance regimes and an annual saving of £750 per signal per
annum." The £11,000 whole-life figure is consistent with £750 × 15 years = £11,250.

The 2019 case also contains the only British railway evidence found in this pass on the
installed-cost direction: a **40 per cent cost saving** when renewing traditional signal structures
with the fold-down LED solution, and a **60 per cent reduction in changeover time** using an
existing base (30 per cent with a new base). That is a capital saving, not a premium, for the signal-plus-structure object.

The 2015 case adds a performance claim that is not a maintenance saving: filament signals
"accounted for 72,000 delay minutes, equating to a cost of £2,775,000 annually", which the LED
replacement would eliminate. That is a delay-cost estimate from the supplier, not an audited
performance account, and it is not included in the maintenance figures above. It does mean that a
whole-life LED case which includes performance is stronger than the maintenance-only case.

### 5.2 The condition that matters

Network Rail's reliability-centred maintenance standard NR/L3/SIG/10665 (issue 24, 7 June 2025)
sets out the regimes:

- **Dorman Lite, iLS, iLS Modular and Dorman Classic LED signals**: module renewal frequency by
  aspect duty cycle. At 100 per cent duty, red and yellow modules last **14.84 years** and green
  **11.76 years**; at 75 per cent duty, 19.78 and 15.68 years; at 50 per cent duty, 29.68 and 23.52
  years.
- **SL35 8000-hour filament**: the standard requires 8,000-hour lamps in all main aspects and
  applies a renewal regime instead of the default service A and B.
- **All other LED and filament signals**: the Unipart case states that these "have an annual
  maintenance visit cycle".

The module renewal interval and the annual visit are different regimes: a Dorman Classic LED head
can have both a long module renewal interval and an annual cleaning visit. Only the iLS and CLS LITE
are designated self-cleaning and can drop the annual visit.

So the LED saving is not a property of the light source alone. It is a property of the combination
of a sealed, self-cleaning head and a maintenance regime that removes the annual visit. A
retrofit LED head that keeps the annual visit saves the lamp changes and the energy, but not the
visit. That is the distinction the pakset should carry if it distinguishes LED heads by type.

### 5.3 Energy

The Unipart iLS specification gives two versions:

| Version | Current | Power at 110 V |
|---|---|---|
| Current-proved, matching the SL35 filament load | 300 mA | **33 W** |
| Low-wattage, voltage-free contacts | 45 mA | **5 W** |

The saving is about **28 W per lit aspect**, or 85 per cent. At 8,760 hours and 25p/kWh that is
245.3 kWh, or **£61 a signal-year** for a signal with one aspect lit at a time. That is small
against £750 of maintenance: the energy saving is about 7-8 per cent of the total saving, and the
maintenance visit is the rest.

Network Rail's 2012 Great Western announcement gives a longer LED head life: "typically could last
between 25,000 to 100,000 hours". At 8,760 hours a year that is 2.9 to 11.4 years. The upper end is
consistent with the 11.76-14.84-year module renewal interval in the 2025 standard; the lower end is
not, and is best read as an early product estimate rather than a maintenance interval.

### 5.4 What an LED signal costs to maintain

If the incandescent signal-plus-structure total is £825-900 a year (the £750 saving plus £75-150
residual LED cost), the LED residual is **£75-150 a signal-year**. That residual is fault response
plus the amortised module replacement. No British source gives the module replacement cost or the
fault-response cost separately, so the residual is an inference, not a measurement.

The measured saving is **£750 a signal-year**. Against the inferred incandescent total of £825-900,
that is **83-91 per cent**; the report uses **80-90 per cent** as the conservative summary. For a
signal-only object whose structure is not mentioned, the saving is £270.73 a signal-year at 2005
values, or about 68-85 per cent of an inferred signal-only total of £320-400; the implied
self-cleaning signal-only LED residual is £50-130.

---

## 6. The LED comparison: capital, maintenance, payback, verdict

### 6.1 Capital

The design intention is that LED should cost more to install. The evidence is mixed:

- **Traffic signals, 2006**: a standard incandescent head cost about £150; an LED head cost
  £600-700. That is a premium of £450-550, or about four times the incandescent head price. This is
  the cleanest British LED capital premium in the record.
- **Traffic signals, 2009**: TfL's programme cost £2.4m for 3,500 heads, or £686 a head of
  programme cost. That is not a bare head price, but it is close to the 2006 LED head price.
- **Railway, 2019**: the Unipart LNE case reports a **40 per cent cost saving** on structure
  renewal and a 60 per cent reduction in changeover time. The LED head is lighter and the
  structure simpler, so the renewed signal-plus-post costs less, not more.
- **Railway, 2010**: Network Rail's weighted average signal head purchase price was £1,980, across
  33 variants and 1,025 items. It is not a like-for-like LED/filament pair, so it cannot be used to
  measure a premium.

The verdict on capital is therefore: **the LED head unit may cost more, but the installed British
railway signal-plus-post does not.** The pakset signal object represents the post, arm or lamp,
mechanism and share of the wires; on that object the evidence points to a capital saving, not a
penalty. If a capital premium is wanted, it should be applied to a head-only object, and it should
be labelled as an inference from the traffic-signal market rather than as a measured railway price.

### 6.2 Maintenance

The maintenance half of the intention is strongly supported, with the condition in section 5.2:

| Case | Incandescent | LED | Saving | Share |
|---|---|---|---|---|
| Signal-only, self-cleaning LED, 2005 values | £320-400 inferred | £50-130 inferred | £270.73 measured | 68-85% |
| Signal plus structure, self-cleaning LED, 2019 | £825-900 inferred | £75-150 inferred | £750 measured | 83-91% |
| Signal plus structure, annual-visit LED, 2019 | £825-900 inferred | £670-800 inferred | £100-160 | 11-19% |

The last row is the important qualification. It is an inference from the fact that the annual
visit is the dominant cost and the Unipart case says all other LED and filament signals keep it.
The pakset should not give every LED signal the self-cleaning saving.

**Verdict.** The maintenance half of the intention is supported on the supplier's figures: by about
**£750 a signal-year** (80-90 per cent) for a self-cleaning LED signal-plus-post, or by about
**£100-160 a signal-year** (11-19 per cent) for a retrofit LED that keeps the annual visit. The capital half is not supported
for the signal-plus-post object: the only British railway evidence points to a **40 per cent
structure-renewal saving for the integrated LED signal and fold-down structure**, not for the LED
head alone, and the only measured LED premium found in this pass is the traffic-signal head, at
about four times the incandescent head price in 2006. The intention should therefore be modelled as a
maintenance saving, not as a capital penalty on the post.

### 6.3 Payback

There is no measured British railway LED capital premium, so a railway payback cannot be computed
from evidence. Two sensitivities show the range:

- If the LED premium were £1,500 a signal and the saving £750 a year, payback would be **2 years**.
- If the premium were £450-550, as in the 2006 traffic-signal head, and the saving £750 a year,
  payback would be **under a year**.

The traffic-signal evidence gives a real payback: TfL reported an overall payback of about **five
years** in 2006. Its 2009 programme spent £2.4m to save £200,000 a year in energy alone, which is 12
years on energy alone; a five-year payback would require about £280,000 a year of maintenance saving
as well. That split is an inference, not a published figure. The five-year TfL estimate is the only
quantified British LED payback estimate found in this pass. The railway case is more favourable because the
maintenance saving is larger, but it is not measured as a payback.

---

## 7. Signalling maintenance per SEU and per route km, CP4-CP6

### 7.1 The totals

| Period | Signalling maintenance | Price basis | Scope | Source |
|---|---|---|---|---|
| 2011-12 | £167m | 2011-12 cash | GB, core maintenance, excludes operations | RailKonsult/ORR, March 2013 |
| CP5 annual average | £137.25m | 2011-12 prices | GB, IIP signalling maintenance | ORR freight cap review, March 2012 |
| 2023-24 | £325m | 2023-24 cash | GB, regionally managed signalling and telecoms | Network Rail RFS 2024, Statement 3.2 |

The £167m is the cleanest signalling-only total. The £325m is an upper bound because it includes
telecoms: central telecoms maintenance was a further £28m, and the regional signalling and telecoms
line is not split. The CP5 £137.25m is lower than the 2011-12 £167m in nominal terms, which reflects
the CP5 efficiency assumption and a different scope (IIP signalling maintenance), not a real fall
of the same size. The CP6 cumulative signalling and telecoms maintenance line was £1,563m over five
years, or £312.6m a year on average in mixed cash prices; at 63,295 SEU that is £4,939 per SEU-year.

### 7.2 Per SEU

An SEU is Network Rail's unit of signalling volume: broadly one signal post or one point end, plus
level crossings and other controlled functions. It is the denominator Network Rail uses for
signalling renewals and maintenance benchmarking.

The SEU count is 64,373 in 2011 (AMCL/ORR, Review of SICA and Signalling Renewals Volumes, 13 May
2011) and 63,295 in 2023 (ORR, Review of Network Rail's conventional signalling and obsolescence
management, 14 June 2023, Figure 1: Eastern 20,105; North West and Central 15,520; Scotland 7,468;
Southern 11,633; Wales and Western 8,569).

| Period | £ per SEU-year | Arithmetic |
|---|---|---|
| 2011-12 | **£2,594** | £167m / 64,373 |
| CP5, 2011-12 prices | **£2,132** | £137.25m / 64,373 |
| 2023-24, signalling and telecoms | **£5,135** | £325m / 63,295 |
| 2023-24, like-for-like signalling only | **about £3,800** | £167m × CPI 1.43 / 63,295 |

The like-for-like £3,800 is an inference: it inflates the 2011-12 signalling-only total by
approximate CPI and divides by the 2023 SEU count. It is the best central estimate for a
signalling-only maintenance rate in 2023-24 money. The range is **£3,800-5,135 per SEU-year**. The
£4,300 top of the signalling-only range is an allowance for activity growth above CPI; it is an
inference, not a published figure. The £5,135 top of the full range is the measured signalling and
telecoms total.

### 7.3 Per route km

The GB mainline route length open for traffic was 15,849 km on 31 March 2024 (ORR, Rail
infrastructure and assets 2023-24, 10 October 2024); this is slightly wider than Network Rail
managed infrastructure because it includes the Core Valley Lines and the Elizabeth line central
section. Using that length:

| Period | £ per route km-year | Arithmetic |
|---|---|---|
| 2011-12 | **£10,537** | £167m / 15,849 |
| CP5, 2011-12 prices | **£8,660** | £137.25m / 15,849 |
| 2023-24, signalling and telecoms | **£20,507** | £325m / 15,849 |
| 2023-24, like-for-like signalling only | **about £15,200-17,200** | £241m-£272m / 15,849 |

The route length is the 2024 figure; the 2012 length was close but not identical. The per-route-km
figures are therefore slightly conservative for the earlier years.

### 7.4 Maintenance against renewal

The renewal rates from report 12 are repeated here for the split:

| Period | £ per SEU | Price basis |
|---|---|---|
| CP4 | £232,000 | inflation adjusted |
| CP5 | £412,000 | inflation adjusted |
| CP5 restated | £533,000 | 2023-24 prices |
| CP6 year 5 | £297,000 | 2023-24 prices |

The maintenance-to-renewal ratio is therefore about **1:60 to 1:125** per SEU-year on a cash basis
(£4,000-5,000 maintenance against £300,000-500,000 renewal), or about **1:2 to 1:3** if the renewal
is annualised over a 35-year asset life (the average life used in the AMCL SICA report). The
annualised comparison is the meaningful one for a pakset: a signal position costs about £4,000-5,000
a year to maintain and about £8,600-14,300 a year to renew, so maintenance is roughly a quarter to a
third of the whole-life annual cost.

---

## 8. Signalbox operating and apparatus maintenance

### 8.1 Apparatus and per-lever costs

The measured historic figures are:

| Year | Rate | Scope | Source |
|---|---|---|---|
| 1873 | £2.70 per lever-year | 10 per cent of £27 capital | KB S7 |
| 1874 | £2.37 per lever-year | LNWR locking maintenance | Webb et al. 1885 |
| 1884 | £1.38 per lever-year | LNWR locking maintenance | Webb et al. 1885 |
| 1901 | £6.30 per box-year | Spetisbury, 9 levers, 8 semaphores, no manning | KB S7 |
| 1901 | £0.70 per lever-year | Spetisbury | Derived |
| 1908 | £80.35 per box-year | Derby Way and Works, 48-lever electro-pneumatic frame, total operating | Derby Signalling History |
| 1909 | £150 per box-year | Small mechanical box, man and maintain | KB S7 |
| 1873 | £180 per box-year | Three men at £60 a man-year, manning only | KB S7 |
| 1933 | £315.79 per box-year | LMS saving from abolishing 190 boxes, 1931-35 | LMS Society |

The 1908 Derby figure is the most interesting because it is a powered frame. The source gives
£40 3s 6d for six months, or £80.35 a year, and separately gives maintenance at 0.0117d per lever
movement and power at 0.00496d per movement. The components do not reconcile exactly with the
stated total, so the total is recorded as the measured figure and the unit rates as unit rates. The
frame was a 48-lever Siemens & Halske electro-pneumatic installation, so £80.35 a year is about
£1.67 a lever-year. The scope is total operating cost, not locking maintenance alone, so it is not
directly comparable with the LNWR figures; it is recorded as a separate powered-frame data point.

The apparatus share is small against manning. The 1909 £150 a box-year is the total of manning and
maintenance for a small box; the 1873 manning alone was £180 for three men. A modern signaller FTE
is £62,917, so the ratio of staff to apparatus is now enormous.

### 8.2 Modern staffing

The 2023-24 regulatory accounts give:

- Signallers and level crossing keepers: **£302m**.
- Operations management: £94m.
- Controllers: £74m.
- Electrical control room operators: £24m.

The ORR PR23 benchmarking report gives more than **4,800 FTE** in 24/7 signalling operations and
£292m of signalling grade staff cost in 2021-22. Dividing £302m by 4,800 gives **£62,917 per
FTE-year**. Network Rail's average employment cost across all staff in 2023-24 was £62,782 per FTE,
so the signaller figure is consistent with the company average.

Derived box operating costs:

| Cover | FTE at 39 hours a week | Cost a box-year |
|---|---|---|
| 24 hours a day, 7 days | 4.31 | **£271,026** |
| 12 hours a day, 7 days | 2.15 | **£135,513** |

These are floors: they do not include holiday and sickness cover, relief signallers, or the box's
apparatus maintenance. They are the right order for a continuously manned single-manned box.

The 2011 Rail Engineer article gives the structural ratio: 18 per cent of Network Control (the
mechanical and early-box end) absorbed 49 per cent of operating costs, while 12 per cent of Network
Control (the ROC end) absorbed 4 per cent. That is the economic case for closing mechanical boxes, and it is consistent with the
LMS's £316 a box-year saving in the 1930s.

### 8.3 What a signalbox should carry

The pakset's signalbox objects represent "building, frame, locking, block instruments, interlocking,
track circuits and control". That is the residual of the signalling system after the lineside
signal objects. The recommended method is:

1. Take the system maintenance rate of **£3,800-4,300 per SEU-year** (2023-24 money).
2. Subtract the lineside signal share. At about 0.63 signals per SEU and £825-900 a signal-year,
   that is about **£520-570 per SEU-year**.
3. The residual is **£3,300-3,800 per SEU-year** for the box, interlocking, control, track circuits
   and supervision.

For a box controlling a known number of SEUs:

| Box type | SEUs controlled | Residual box maintenance a year |
|---|---|---|
| Mechanical, small | 20 | £66,000-76,000 |
| Relay | 43 | £142,000-163,000 |
| Electronic | 50 | £165,000-190,000 |
| ROC workstation | 250 | £825,000-950,000 |

The SEU-per-interlocking figures are from the AMCL SICA report: mechanical 20, relay 43, electronic
50, with an average of 36. The ROC workstation figure of 250 SEU is from the 2011 Rail Engineer
article, which says one signaller in a ROC can control 200-300 SEU. These are allocations, not
measurements of a particular box.

Add the signaller cost if the box is manned: £62,917 per FTE-year, £271,026 for a 24/7 post,
£135,513 for a 12-hour post. Do not add the signaller cost to a ROC workstation as well as the
residual: the residual is apparatus and supervision, the signallers are separate.

### 8.4 Per route km

No British source gives signalbox operating cost per route km. The components exist — 10,000 boxes
in 1900 (Rail Engineer 2011), about 800 boxes in 2011 (Rail Engineer 2011), £150 a box-year in 1909
and £271,026 a box-year for a 24/7 post in 2023-24 — but the box density, the route length for the
same year and the proportion of boxes that were manned are not stated in the same source. The
modern equivalent cannot be computed without the manned-box count and the average cover per box.
This is a gap, not a figure to use.

---

## 9. Traffic signals as a cross-check

### 9.1 Maintenance per site

West Sussex County Council's 2020 maintenance contract extension gives an estimated revenue spend
of **£380,000-400,000 a year** and a remote monitoring estate of **248 sites**. That is
**£1,532-1,613 per site-year**. The estate includes vehicle-activated signs and other electrical
equipment, so it is an upper bound for traffic signals alone, but it is a real contract figure, not
a supplier claim.

TfGM's LED retrofit gives the saving: **£600,000 a year** across **1,800 sites**, or **£333 per
site-year**, from replacing 52,000 incandescent bulbs with LED aspects. If the West Sussex total is
representative, the LED saving is about **20-22 per cent** of the site maintenance cost. That is a
useful cross-check: the road-signal saving is much smaller than the railway signal saving because
the annual visit is not removed, only the lamp changes and the energy.

### 9.2 Lamp and energy economics

| Item | Incandescent | LED | Source |
|---|---|---|---|
| Head price, 2006 | £150 | £600-700 | UKERC 2006 |
| Lamp life and replacement interval | 12-18 months lamp life; 6-12 months bulk replacement | up to 30 years (2006); 6.3 years (Liverpool 2021) | UKERC 2006; Liverpool FBC |
| Power per aspect | 50 W bright, 25 W dim | 8 W (West Sussex 2023); about one-third of incandescent (UKERC 2006) | West Sussex 2023; UKERC 2006 |
| Energy cost per unit-year, 2022 | £125 | £16 | Telent 2022 |
| Energy saving per junction-year, 2009 | — | £667 | TfL 2009 |
| Energy saving per aspect-year, 2023 | — | £92 | West Sussex 2023 |

The 2006 UKERC report gives the national scale: about **420,000 traffic and pedestrian signal
heads**, using **101.7m kWh a year**, with a 12-18-month incandescent lamp life and bulk replacement
every 6-12 months, and LED lamps lasting up to 30 years. It also gives the measured payback: TfL "envisages an overall
payback period of around five years". That is the only quantified British LED payback estimate
found in this pass.

The 2009 TfL programme is the largest single data point: **3,500 heads at about 300 junctions**,
**£2.4m**, a **60 per cent** electricity saving, and **£200,000 a year** in energy costs. The
capital per head is £686; the energy saving per junction is £667 a year. The press release says the
bulbs "will last about ten times longer than standard bulbs", which is the source of the
maintenance claim, but it gives no percentage maintenance saving.

### 9.3 The explicit percentage question

No British railway or highways source found in this pass states a percentage maintenance saving
from LED. The record contains:

- TfL 2009: "cut electricity consumption ... by a massive 60 per cent" and bulbs "last about ten
  times longer", with no maintenance percentage.
- West Sussex 2020: "additional reduction in the annual maintenance rate when sites are upgraded to
  LEDs", with no percentage.
- TfGM/Yunex: £600,000 a year maintenance saving across 1,800 sites, with no baseline, so the
  percentage cannot be computed from the source.
- Unipart 2015 and 2019: absolute savings of £270.73 and £750 a signal-year, with no percentage.

The percentages in this report are therefore derived, not quoted: 20-22 per cent for traffic
signals (TfGM saving against West Sussex total), and 80-90 per cent for self-cleaning railway
signals (the £750 saving against the inferred £825-900 total). The first is a cross-authority
comparison and should be treated as an order of magnitude; the second is an inference from a
supplier case study.

---

## 10. Recommended maintenance rate table

The rates below are recommendations for the pakset, derived from the evidence. They are not
measurements, and the confidence column says how much of each is measured. All rates are nominal
for the year or era shown, and all are annual. The pakset's maintenance fields are monthly, so
divide by 12 at the point of entry; the conversion is left to the pakset because the engine's
scaling is outside the evidence.

### 10.1 Signal objects

| Signal type | Era | Recommended rate | Confidence | Basis |
|---|---|---|---|---|
| Mechanical semaphore, oil lamp | 1870-1900 | **£4-7 a signal-year** | Medium | LNWR £1.38 a lever-year; Spetisbury £0.79 a signal-year; lamp a few pounds |
| Mechanical semaphore, oil or electric | 1900-1935 | **£6-12 a signal-year** | Medium | Spetisbury £0.79 a signal-year plus lamp and nominal growth; manning separate |
| Colour light incandescent | 1950-1970 | **£70-140 a signal-year** | High for the anchor | Kent Coast residual £56-142; 1959-62 prices |
| Colour light incandescent | 1970-1990 | **£200-450 a signal-year** | Low (interpolated) | Interpolated between the 1962 and 2005 anchors; not a measured series |
| Colour light incandescent | 1990-2010 | **£500-800 a signal-year** | Medium | Interpolated between the 1962, 2005 and 2019 anchors |
| Colour light incandescent | 2010-2020 | **£825-900 a signal-year** | Medium | 2019 £750 saving plus £75-150 residual |
| LED, annual visit retained, signal-plus-post | 2010-2026 | **£670-800 a signal-year** | Low | 2019 £825-900 incandescent total less £100-160 of lamp changes and energy |
| LED, self-cleaning, signal-plus-post | 2015-2026 | **£75-150 a signal-year** | Medium | 2019 £750 saving against £825-900 incandescent total; residual inferred |

The mechanical rates exclude signalman wages, which belong to the signalbox. The colour-light rates
include the lineside signal's share of testing and fault response but not the interlocking or
control, which belong to the signalbox.

### 10.2 Signalbox objects

| Box type | Era | Recommended rate | Confidence | Basis |
|---|---|---|---|---|
| Mechanical box, small | 1870-1909 | **£5-15 apparatus + £150-180 manning a box-year** | High for the anchors | Spetisbury £6.30; 1909 £150; 1873 £180 |
| Mechanical box, larger | 1900-1950 | **£15-130 apparatus + manning a box-year** | Medium | Per-lever £0.70-2.70 × 20-48 levers |
| Power box | 1950-1990 | **£5,000-40,000 a box-year** | Low (inference) | 1-2 per cent of £0.5m-£2m capital; no measured apparatus figure |
| IECC / ROC | 1990-2026 | **£150,000-600,000 a box-year** | Low (inference) | 1-2 per cent of £15m-£30m capital; no measured apparatus figure |
| Modern box, per SEU | 2010-2026 | **£3,300-3,800 per SEU-year residual** | Medium | System total £3,800-4,300 less lineside signal share £520-570 |
| Signaller | 2023-24 | **£62,917 per FTE-year** | High | £302m / 4,800 FTE |

The 21 signalbox objects will need mapping to these types; the per-SEU method is preferable where
the object represents an interlocking of known size, and the box-type rows are for objects whose
size is not known. For the 1930s, the LMS £316 a box-year saving is the best total operating anchor;
apparatus alone is not measured. The power-box and ROC rates are the weakest rows in the table. No British source
measures apparatus maintenance for a power box or a ROC separately from the system total. The 1-2 per cent of capital
is an inference from the general building and equipment maintenance range, not a signalling
measurement. If the pakset uses the per-SEU residual method instead, it does not need these rows.

### 10.3 Traffic-light objects

| Type | Era | Recommended rate | Confidence | Basis |
|---|---|---|---|---|
| Incandescent junction or site | 2020 | **£1,500-1,600 a site-year** | Medium | West Sussex £380-400k / 248 sites |
| LED junction or site | 2020 | **£1,200-1,300 a site-year** | Low | West Sussex total less TfGM £333 saving |

The traffic-light rates are for the whole site, not per head. A junction may have several sites;
the West Sussex 248 is a site count, not a junction count.

### 10.4 The share between signal and signalbox

For a modern installation, the recommended split is:

- Signal object: **£825-900 a signal-year** for an incandescent signal-plus-post, **£75-150** for a
  self-cleaning LED signal-plus-post.
- Signalbox object: **£3,300-3,800 per SEU-year** residual, plus signaller cost if manned.

This keeps the total at the measured system rate of £3,800-4,300 per SEU-year. If the pakset gives
every signal object £825-900 and every signalbox object the full per-SEU rate, it will double count
by about 12-15 per cent. The residual method avoids that.

---

## 11. Confidence

**High confidence.**

- The Spetisbury/1909 KB anchors and the 1884 LNWR figure (which the KB corroborates).
- The Kent Coast counts, costs and annual charges (Tyler 1962, primary source).
- The Network Rail signalling maintenance totals for 2011-12 and 2023-24, and the SEU counts for
  2011 and 2023.
- The signaller cost per FTE and the 24/7/12-hour box derivations.
- The West Sussex contract value and site count.
- The traffic-signal head prices and lamp life from UKERC 2006.

**Medium confidence.**

- The LNWR per-lever figures for 1874 and 1885, because the full ICE text was paywalled; the 1884
  figure is corroborated by the KB.
- The Unipart Dorman case studies. They are supplier marketing, not audited accounts, but they are
  specific about scope and arithmetic.
- The per-SEU and per-route-km derivations, because the scope (signalling only against signalling
  and telecoms) and the price bases differ.
- The 1959 Kent Coast residual, because the interest allocation is ambiguous between £45,000 and
  £51,400.
- The West Sussex site count as a denominator, because 248 is the monitored estate, not
  necessarily every site, and the 2023 energy saving, which is a council estimate at 25p/kWh, not a
  metered outturn.
- The 1908 Derby total, because the components do not reconcile exactly.
- The 1933 LMS box-closure saving, which is a company history figure, not an audited account.

**Low confidence.**

- The 1885 £3 lamp saving, because the full ICE text was paywalled and the figure is from the
  search extract.
- The Liverpool FBC figures, because the PDF was blocked by Cloudflare.
- The inferred incandescent totals of £320-400 (2005) and £825-900 (2019), and the LED residuals
  of £50-130 and £75-150.
- The 2023 energy saving of £61 a signal-year, because it uses the West Sussex road electricity
  price, not a railway traction or signalling supply price.
- The power-box and ROC apparatus rates, which are inferences from a general percentage of capital.

---

## 12. Dead ends

Recorded so that they are not searched again.

1. **No British railway source gives a percentage LED maintenance saving.** The British record gives
   absolute savings (£270.73 and £750 a signal-year) and qualitative statements ("last about ten
   times longer"), not percentages.
2. **No measured British railway pair of LED and incandescent signal head prices.** The only
   measured pair found in this pass is the traffic-signal head, £150 against £600-700 in 2006.
3. **No modern per-box apparatus maintenance cost for a power box or ROC.** The system total and the
   per-SEU rate are the only modern measures.
4. **No railway signal lamp purchase price.** The lamp life and wattage are measured; the lamp price
   is not.
5. **No measured labour cost per railway signal lamp change.** The Rail Engineer 2017 article says a
   signal light call-out is "a van with two or three people ... half a day", but gives no cost.
6. **No colour-light maintenance figures for 1926-1959.** The Southern's first colour light was
   1926, but the per-signal maintenance cost before the Kent Coast scheme is not in the record.
7. **No 1930s or 1940s colour-light maintenance figures.** The LMS 1931-35 figure is a box-closure
   saving, not a colour-light signal cost.
8. **No per-junction traffic-signal maintenance split between incandescent and LED from a single
   authority.** The 20-22 per cent figure is a cross-authority comparison.
9. **No TfGM baseline maintenance cost**, so the £600,000 saving cannot be converted to a
   percentage from that source alone.
10. **The 1885 ICE discussion is paywalled.** The DOI page returns metadata only; the figures are
    from the search extract.
11. **The Liverpool City Region UTC business case is blocked by Cloudflare.** The figures are from
    the search extract.
12. **Several ORR PDFs return HTML on the live site.** The 2011 SICA report, the 2012 freight cap
    review and the 2013 asset management review were retrieved from the Wayback Machine.
13. **The 1908 Derby cost components do not reconcile.** The total is recorded; the per-movement
    rates are recorded as unit rates, not multiplied into an annual total.
14. **The West Sussex 2,000 bulbs a year is inconsistent with 649 aspects.** If 649 aspects were
    changed once a year, the count would be 649, not 2,000. The 2,000 is recorded as stated; it
    probably covers the whole halogen estate, not just the 649 aspects in the programme.
15. **No per-balise, per-track-circuit or per-point maintenance cost** was found in this pass; the
    system total per SEU is the only aggregate.
16. **No signalbox operating cost per route km.** The box count, box cost and route length exist in
    different sources and different years; they cannot be combined into a measured rate.

---

## 13. Conflicts with the knowledge base

One correction and one usage caution in `New/ai/infrastructure-cost-evidence.md` section 7 need
review. The KB has not been edited.

1. **The £3 oil lamp figure is a saving, not a cost.** The KB says "an oil signal lamp cost about
   £3 a year all in (1885)". The 1885 ICE discussion says the new petroleum lamp saved about £3 per
   lamp per annum, and that applying it to all LNWR lamps would save over £40,000 a year. The
   absolute cost of lighting a lamp is not measured in the source. The KB sentence should be
   corrected or qualified.

2. **The 1909 £150 a year is a manning-plus-maintenance figure for a small box, not a per-signal
   figure.** The KB already says "plus £150 a year to man and maintain", which is correct, but the
   figure is sometimes used as if it were the signal maintenance cost. It is a box operating cost,
   and it cannot be compared directly with the per-signal rates in this report.

The KB's per-lever figures (1873 £2.70, 1884 £1.3-1.5), the Spetisbury £6.30, the 1901 £450 box
cost and the 1909 £300 box cost all survive checking. The 1873 10 per cent rate is higher than the
Spetisbury apparatus-only rate, but the two measure different things; the KB does not say
otherwise.

---

## 14. Sources

Full URLs for every row are in `research-pricing-rows-14.csv`; the list below gives the source,
date and the URL for the principal new sources.

Primary and official:

- F. W. Webb, J. S. Farmer, C. E. Spagnoletti et al., "Discussion on the Signalling of the
  London and North-Western Railway", *Minutes of the Proceedings of the Institution of Civil
  Engineers* 82 (1885), 189-219, doi:10.1680/imotp.1885.21405. Search extract; full text paywalled.
- J. F. H. Tyler, "Signalling Developments on the Southern Region", IRSE Proceedings 1962,
  Appendix E. jonroma.net IRSE archive.
- Derby Signalling History, "Signalling around Derby Station",
  http://www.derby-signalling.org.uk/Station.htm (1908 Siemens & Halske frame costs).
- LMS Society, "A Record of Large-Scale Organisation and Management, 1923-1946: Signalling",
  https://lmssociety.org.uk/lmsRecord/signalling.php (1931-35 box abolition saving).
- Network Rail, NR/L3/SIG/10665, "Reliability Centred Maintenance of Signalling", issue 24,
  7 June 2025,
  https://sitescdn.wearevennture.co.uk/public/matchtech/assets/nr_l3_sig_10665reliabilitycentredmaintenanceofsignallingequipment.pdf.
- Network Rail, "Regulatory Financial Statements, year ended 31 March 2024", Statement 3.1 and
  3.2.
- Network Rail, "Regulatory Financial Statements, year ended 31 March 2012", as used by
  RailKonsult/ORR, March 2013.
- RailKonsult/ORR, "Review of Asset Management Best Practice", March 2013, section 9.4.2.
- ORR, "Independent Reporter A — Review of Analysis in Network Rail's Freight Cap Consultation",
  30 March 2012, section 4.1.
- AMCL/ORR, "Review of SICA and Signalling Renewals Volumes", 13 May 2011.
- ORR, "Review of Network Rail's conventional signalling and obsolescence management", 14 June
  2023, Figure 1.
- ORR, "Rail infrastructure and assets, April 2023 to March 2024", 10 October 2024.
- ORR, "Signalling market study: final report", 9 November 2021 (more than 40,000 signals; the
  renewals SEU series).
- ORR, "PR23 final determination: Report on benchmarking Network Rail operations and support
  costs", August 2023.
- ORR, "Annual efficiency and finance assessment of Network Rail 2024", 1 October 2024
  (average employment cost £62,782 per FTE).
- Arup/ORR, "Network Rail bottom-up benchmarking programme audit", January 2012, section 6.3.2.
- Civity/ORR, "International benchmarking of Network Rail's operations and support functions
  expenditure", 17 April 2013.
- Arup/ORR, "Network Rail bottom up benchmarking review: benchmarking of operations costs",
  2 March 2012.

Supplier and trade:

- Unipart Dorman, "Zero Maintenance Signalling" case study, December 2015,
  https://www.unipartdorman.com/assets/zero-maintenance-case-study.pdf.
- Unipart Dorman, "Signal & Structure Renewals" case study, July 2019,
  https://www.unipartdorman.co.uk/wp-content/uploads/2022/10/unipart-dorman-signal-and-structure-replacement-case-study-website-1.pdf.
- Unipart Dorman, "LED Signalling Handbook",
  https://www.unipartdorman.co.uk/wp-content/uploads/2022/09/led_signalling_handbook.pdf.
- Rail Engineer, "Wholesale closure of almost every signal box on the network", 6 September 2011.
- Rail Engineer, "In case you missed it — How many railway technicians does it take to change a
  light bulb?", 30 December 2017.
- Network Rail media centre, "Rail investment signals start of revamp on Great Western",
  4 April 2012.
- UKERC, "Quick Hits 3: Traffic signals", December 2006.
- TfL press release, "Mayor gives green light to energy busting LED traffic signals",
  17 August 2009.
- West Sussex County Council, "Traffic Signals Maintenance Contract Extension", August 2020.
- West Sussex County Council, "Traffic Signals Halogen Replacement Programme", July 2023.
- Yunex Traffic, "Retrofit Solutions".
- Telent, "LED Signals" slides, 2022.
- Liverpool City Region, "UTC Phase 1 FBC", January 2021 (search extract; PDF blocked).

Knowledge base:

- `New/ai/infrastructure-cost-evidence.md` section 7.
- `ai/temp/research-pricing-report-12.md` and `research-pricing-rows-12.csv` (capital only).
