---
status: draft
verified: New master @ 70a098c64 (working tree)
---
# Wagon overhaul: a source-by-source analysis of the 8-20 per cent band

**Covers**: the wagon rows of `New/cost-balancing-capital.xlsx` (Overhauls & upgrades,
Rail vehicles), `New/ai/cost-balancing/evidence_data.py` (`OVERHAUL_PROFILE`, the wagon
maintenance branch), and the wagon sections of [report 36](research-pricing-report-36.md),
[report 39](research-pricing-report-39.md), [report 40](research-pricing-report-40.md) and
[report 43](research-pricing-report-43.md).

**Question**: reports 36, 40 and 43 give three different wagon overhaul rules (8-20 per cent at
3 years; 10-15 per cent at 5-7 years; 20 per cent of the annual total at 3 years). This doc
compares the underlying sources to find what each measures, on what denominator, in which field,
and why the figures do not meet. It does not choose a winner; §5 recommends a field assignment.

Definitions used here. **Running repair**: day-to-day and intermediate work at a depot or works,
no general strip. **Heavy overhaul / general repair**: periodic works visit with the body lifted
or stripped, wheelsets and brake gear attended, repainted. **Condemnation**: the administrative
decision not to repair, after which the vehicle is withdrawn. **Renewal**: a new vehicle in place
of a scrapped one (capital). **Capital provision**: the depreciation or capital charge carried
inside a costing line.

## 1. The figures in conflict, with the arithmetic

Deflator: the `general` series in `New/config/prices.tab`, 1900 = 100 (1883 101, 1892 97, 1896 93,
1906 102, 1923 203, 1929 193, 1934 172, 1948 338, 1955 468, 1961 552, 2020 12,521).
`[CODE New @ 70a098c64]`

| Rule | First event | Max event | Interval | Annual provision | Implied total a year (head plus overhaul) |
|---|---|---|---|---|---|
| Report 36 | 8% of capital | 20% of capital | 3 years | 2.7-6.7% of capital a year | 10.7-14.7% |
| Report 40 | 10-15% of new | 20% of new | 5-7 years | 1.4-3.0% | (with the measured 3-4% head) 4.4-7.0% |
| Report 43 | 20% of the annual total x 3 years = 60% of a year's spend (3.5% of capital at 1900) | same | 3 years | 20% of the annual total | (head is the total, so no addition) |
| Workbook | 12% of capital | 20% of capital | 240,000 km (6 yr at 40,000 km/yr) | 2.0-3.3% | 10.0-11.3% |
| Generator | 10% | 30% | 200,000 km (5 yr at 40,000) | 2.0-6.0% | 10.0-14.0% |

Workbook: 58 of the 84 wagon rows carry 12/20 per cent at 240,000 km; seven others carry 10/30 at
200,000 km; the remaining rows are road and stage wagons with their own profiles.
`[CODE New @ 70a098c64: Overhauls & upgrades]`

The only measured total is **3.9-6.7 per cent of a new wagon a year** across 1892-1934, the range
coming from which measured new price is used (§2), or **5.9 per cent of the pakset's 1900 capital**
(£4.2 on £70.7). Every pakset combination above is 1.7 to 2.5 times that total before any renewal
is counted. `[DERIVED]`

**Where report 43's "2.0 per cent" comes from.** Report 43 takes 0.20 x 3 x 23.8 = £14.3 and
divides by £707: `[DERIVED from report 43 §6]`

- 23.8 is the 2020 ladder value for a **10-tonne** wagon. £707 is 100 tonnes x £7.07, the pakset's
  per-ton capital, i.e. a **100-tonne** wagon. Numerator and denominator describe different wagons.
- Matched at 10 tonnes: 14.3 / 70.7 = **20.2 per cent of capital** — the top of report 36's band.
- Matched at 100 tonnes with the ladder's own size term: annual = 23.8 x (100/10)^0.4 = 59.7;
  event = 0.6 x 59.7 = 35.8; 35.8 / 707 = **5.1 per cent** at a 3-year cycle, **10.1 per cent** at
  6 years. Neither is 2 per cent. `[DERIVED]`
- So the "finding, not a rounding error" is an artefact of the mismatched pair. The conclusion it
  supports ("either 2-3 per cent of capital or 6-10 years") is not required by any source.

**A propagated conversion error.** [source-composition](../vehicle-cost/source-composition.md) and
the task brief both give "GBP 54.3 nominal = GBP 14.3 in 1900 money". The deflator gives **£9.84**
(54.3 x 100/552; report 43 uses 528, which is the 1959 value, so its figure would be £10.28). £14.3
is not the 1961 level at all: it is 0.6 x 23.8, the 2020 **event** from the ladder. A measured 1961
cost and a modelled 2020 event have been conflated, which is how a composition acquired the
appearance of a measurement. `[DERIVED]`

**A second units collision.** "20 per cent" means two different things. Report 36's 20 per cent is
20 per cent of **capital** per event. Report 43's 20 per cent is 20 per cent of the **annual
maintenance total**. At 1900 the first is £14.1 and the second £0.84 — a factor of 17. No
reconciliation is possible until the two are named differently. `[DERIVED]`

## 2. Source by source

Grade: MEASURED = an account, contract or published total with a stated scope; STATED = a trade,
academic or witness statement without the account; DERIVED = arithmetic here from a measured or
stated figure; ESTIMATE = judgement; UNAVAILABLE = identified but not readable.

| Date | Source | Figure | Denominator | Scope | Interval | Grade |
|---|---|---|---|---|---|---|
| 1883 | GERS, GER 5-plank | £112 7s (body £70 + ironwork £21 12s + wheelsets £20 15s) | one new 10/12-t wagon, works estimate | capital | — | STATED |
| c1906 | GRCW / Teague fleet (via report 23) | £66 | one new PO 7-plank | capital | sold with a 7-year repair contract | MEASURED (via report 23) |
| 1923-24 | Gloucester Gas (Pope) | £135 10s (10 off); £163 (20 off) | one new 12-t PO wagon | capital | — | MEASURED (not re-fetched: 403) |
| 1892 | Hill, App. II Table III | £4 4s a wagon-year (range £2 4s-£6 10s; simple mean of 19 companies; stock-weighted £4 0s) | per wagon **in stock**, fleet average of 19 companies | "maintenance, that is the cost of repairs and renewals" — **complete renewals in** | annual | MEASURED |
| 1892 | Hill, App. II Table II | £33 6s a carriage-year (range £18 6s-£52 14s) | per carriage in stock | same definition, same five years | annual | MEASURED |
| 1892 | Hill, App. III Table XXV | 3.1% of stock renewed a year (range 1.0-6.4; Midland 6.4) | per wagon in stock, **by number** | complete renewals only | annual | MEASURED |
| 1892 | Hill, App. III Table XXIV | 2.53% a year | per carriage in stock, by number | complete renewals only | annual | MEASURED |
| 1896 | *Railway Magazine* v1 p.67 | £2 12s a wagon-year, "£5 a few years before" | per Midland wagon | "the charge for **renewals**" | annual | STATED |
| 1929 | Essex D/F 27/2/108 | £5 a wagon-year (20 wagons, £100 a year) | per wagon-year | "repair agreement"; scope not in the catalogue | 7-year term | MEASURED (catalogue; original not digitised) |
| 1934-39 | Lightmoor, COAL36 48 | £5 8s 6d a wagon-year (507 wagons) | per wagon-year | **all** maintenance: the colliery closed its own repair shed and made 20 men redundant | 5-year term | MEASURED |
| 1935 | GWR, *Swindon Works* (via Grace's Guide) | 8,000 repairs a year on 80,350 wagons = 0.10 a wagon-year | one works, capacity | "repairing"; heavy and light not separated | 10 years if all repairs | STATED |
| 1947 | Hansard 445 c288W | 182,082 under or awaiting repair; about half major | whole fleet | backlog of all repairs | — | MEASURED |
| 1948 | MoT compensation (report 23) | £16 10s for an 8-t ex-PO wagon, "regardless of condition" | book/compensation value | capital value of the oldest stock | — | MEASURED (via report 23) |
| 1952 | Swindon, IMechE visit | 16,000 repairs a year | one works, capacity | "repair" | 5 years if all repairs | STATED |
| 1955 | BR *Facts and Figures* 1956 | 1,124,812 wagons; 58,733 new in 1955; 75,403 under or awaiting repair | fleet | counts | annual | MEASURED |
| 1961 | Beeching p.6 | £46.1m | 848,591 wagons = £54.3 a wagon-year | "**provision**, maintenance, stabling and servicing" | annual | MEASURED |
| 1961 | Beeching p.6 | £122.2m maintenance account vs £157.0m for the three vehicle functional lines = 77.8% | whole fleet | bound on the maintenance share of the functional lines | annual | MEASURED, ratio DERIVED |
| 1961 | Beeching App. 3 | gross book value £1,037m; 2,973m wagon-miles | whole fleet; 848,591 wagons = 3,503 miles (5,638 km) a wagon-year | capital; utilisation | annual | MEASURED |
| 1963 | Beeching App. 4 | Liner Train wagon £3,000; 100,000 chassis-miles a year assumed | one purpose-built flat | design case | annual | STATED |
| 1947 | HMRS ME1660, *Regulations for Repairing & Rebuilding of Wagons* | — | — | the condemnation rule itself | — | UNAVAILABLE |
| 1972-81 | HMRS, wagon average repair costs | — | — | the post-1961 series | — | UNAVAILABLE |
| 1960s-70s | ex-BR C&W staff, RMweb | monetary limits per repair, set by wagon type and varied seasonally; from about £1 (1973, Vanfits) upward; over-limit wagons condemned or stored until the limit changed | per **repair**, not per year | condemnation threshold | per event | STATED (testimony) |

Sources, in table order: https://gersociety.org.uk/rolling-stock/wagons/1880-1889 ;
https://glostransporthistory.visit-gloucestershire.co.uk/ROD_Universal%20Works_GA_GRCW.html (via
report 23) ; https://glostransporthistory.visit-gloucestershire.co.uk/Pope.htm (returned 403 on
2026-11-25; figures taken from report 40, which read the page) ; https://archive.org/details/minutesproceedi43britgoog
(Hill 1895, pp. 224-264; page images read, doi 10.1680/imotp.1895.19704) ;
https://steamindex.com/rlymag/rm1on.htm ; Essex Archives Online D/F 27/2/108 (item has no public
URL; catalogue read in report 39, original not digitised) ; https://lightmoor.co.uk/forestcoal/CoalA&E.html ;
https://www.gracesguide.co.uk/Swindon_Works_in_1935 ;
https://api.parliament.uk/historic-hansard/written-answers/1947/dec/15/wagon-repairs ;
https://www.gracesguide.co.uk/1952_Institution_of_Mechanical_Engineers:_Visits_to_Works ;
https://my1950s.com/wp-content/uploads/2022/02/BR-1956-OCR.pdf ;
https://railnews-business.co.uk/docs%20library/1963%20BRB_Beech001a.pdf ;
https://hmrs.org.uk/archives/regulations-for-repairing---rebuilding-of-wagons-me1660.html ;
https://hmrs.org.uk/archives/wagons---annual-average-repair-costs-1972-81.html ;
https://www.rmweb.co.uk/topic/181446-wagon-maintenance-and-repairs/ ;
https://www.rmweb.co.uk/topic/188447-wagon-works-scrap-1970s-onwards/page/2/ ;
https://www.rmweb.co.uk/topic/185505-wagon-maintenance-in-the-early-british-railways-period-1948-1960/ .

## 3. Where the contradiction comes from

**(i) The 8-20 per cent is a condemnation ceiling in the wrong field — confirmed.** The only
evidence for the rule's content is secondary testimony that BR set a **cash limit per repair**,
varied by wagon type and by seasonal demand, and condemned (or stored, re-assessing when the limit
changed) any wagon whose assessed repair exceeded it. `[STATED: RMweb, ex-BR C&W staff]` That is a
threshold applied at the moment a wagon is carded for repair, and it decides replacement, not
recurring maintenance. Report 36's own sentence says the same — "condemning a wagon when the repair
estimate exceeded a monetary limit" — and then uses the limit as `max_overhaul_cost`, a field the
engine charges every interval for the life of the vehicle. `[CODE New @ 70a098c64]` See
[vehicle-cost-model](../vehicle-cost-model.md), "Overhauls and upgrades".
Nothing published ties the limit to 20 per cent of new price: the observed limits range from about
£1 (a 1973 Vanfit) upward, and rose when a wagon type was in demand, by an amount the witness does
not quantify. The 1947 regulation that would state the rule is archive-only.

**(ii) The 3-year interval is unsourced, and the documented heavy cycle is 5-10 years —
confirmed.**
Report 36 rejects the one interval it had (the Midland's nine-month works visit, correctly, as an
examination) and substitutes 3 years with no citation. The intervals that are documented are:
5 years (Arthur & Edward contract term 1934-39); 7 years (Colchester Gas 1929; GRCW's contract
sold with the Teague wagon, renewed 1913); 5 years then 7 (BR mineral-wagon descale and repaint
policy 1954-62, secondary: https://www.rmweb.co.uk/topic/185505-wagon-maintenance-in-the-early-british-railways-period-1948-1960/ );
4-6 years first POH (Indian Railways manual, quoted in report 40, not re-read); 10 years (GWR
Swindon capacity, if all 8,000 repairs were heavy, which they were not).
`[MEASURED/STATED as tagged in §2]` Note the weakness: a **contract term** fixes a price for a
period; it is not a repair interval. The 5- and 7-year terms are consistent with a 5-7-year cycle
but do not measure one.

**(iii) The denominators differ — confirmed, and it is the largest single effect.** £4 4s deflated
to 1900 money (£4 7s) is 3.9 per cent of the 1883 GER wagon (£111 in 1900 money), 6.7 per cent of
the 1906 PO wagon (£65) and 6.1 per cent of the pakset's £70.7. The "new wagon price" itself ranges
over 1.7 times within 23 years in the same country, because a railway-built 10/12-ton wagon and a
mass-produced PO 7-plank are different products. `[DERIVED]` The 1961 figure adds a second layer: £54.3 is a
**fleet average** over 848,591 wagons whose 1955 composition was 595,264 mineral, 309,502 open
merchandise and 143,628 covered, with 239,579 ex-private-owner within the 1,124,812 total and an
average capacity of 13.8 tons — old, small and largely depreciated. `[MEASURED: BR 1956]` No
published average age was found; the same booklet concedes only that "many wagons had to be kept in
service beyond their normal life". An 8-ton ex-PO wagon was valued at £16 10s at nationalisation. A
percentage of a **new** wagon and a percentage of that fleet's **book** capital are not the same
quantity and cannot be compared without both.

**(iv) The 1961 figure includes capital provision — confirmed.** The functional heading is
"provision, maintenance, stabling and servicing", and Beeching's own coal costing (printed p.32)
prices "provision of wagon" as a separate element at 92s. for a 6-ton wagon over 100 miles —
about 11d a wagon-mile against a fleet-average 3.7d — a charge that only makes sense as capital
recovery plus turnround, not as repair. The three vehicle functional lines total £157.0m against
the £122.2m "maintenance of rolling stock" account line, so at most 77.8 per cent of the wagon
line is maintenance at all, and part of the remainder is stabling and servicing rather than
provision. `[MEASURED + DERIVED]` Proportional allocation would give £42.3 a wagon-year as the
maintenance-only figure — an upper bound, not a measurement. `[DERIVED]`

**(v) The 20 per cent overhaul share is an estimate — confirmed, and report 43 says so.** "The
split is an ESTIMATE: Hill's figures do not separate works overhauls from running repairs, and no
wagon overhaul price exists in any era." [report 43](research-pricing-report-43.md) §6. The same is
true of reports 36 and 40.
No source in any era prices a wagon heavy overhaul. The 8, 10-15 and 20 per cent figures are all
compositions, not measurements.

**(vi) Part of the wagon overhaul belongs in the renewal field — confirmed, with a split.** Hill's
£4 4s contains complete renewals. At 3.1 per cent of stock a year and £70.7 a wagon, renewals alone
are £2.19, or 52 per cent of the £4.2 total — the figure [report 40](research-pricing-report-40.md)
§2 carries as the wagon renewals share. `[DERIVED from Hill Tables III and XXV]` The Midland's own figures show the same thing from
the other side: its 6.4 per cent renewal rate (Hill Table XXV) on a £70-80 wagon is £4.50-5.10 a
year, which is the "£5 a few years before" of the 1897 note; the fall to £2 12s in 1896 tracks the
end of a rebuild programme, not a fall in repair cost. `[DERIVED]` So the condemnation decision and
the renewal provision are capital, and only the heavy general repair is maintenance. Report 36 put
a condemnation threshold in the overhaul field; the engine has no condemnation event at all, and
replacement is carried by `upgrade_price` plus the obsolescence and wear ramps.

**A seventh mechanism: the interval is a distance field.** `max_distance_between_overhauls` is in
kilometres, and the engine has no calendar interval. `[CODE New @ 70a098c64]` Report 36 wrote "3
years" into a field that cannot hold years; the workbook wrote 240,000 km instead. The conversion
depends wholly on assumed annual mileage: 240,000 km is 6 years at 40,000 km/yr (the workbook's
implicit duty, close to the modern 50,000 km/yr contract assumption) but **42.6 years at the
measured 1961 duty of 5,638 km a wagon-year** (2,973m wagon-miles / 848,591 wagons).
`[DERIVED: Beeching Table 1 and App. 3]` A distance chosen for modern freight duty is being applied
to every era, so the same field means a 6-year cycle in one era and a 40-year cycle in another.

## 4. Reconciliation

Let A be the measured annual total (3.9-6.7 per cent of new, central 5.9 per cent at 1900), s the
overhaul share of A, and n the interval in years. The event is s x n x A and the head is (1-s) x A.
Only the product s x n is constrained by the sources; s and n separately are not.

| Basis | Event | Interval | Event as % of capital | Fits A? |
|---|---|---|---|---|
| Report 36 as written (8-20%) | 8-20% | 3 yr | 8-20 | No: 2.7-6.7% a year is 45-113% of A before any running repair |
| Report 36 with a 6-10-year interval | 8-20% | 6-10 yr | 8-20 | Yes, at 0.8-3.3% a year (14-56% of A) |
| Report 40 as written | 10-15% | 5-7 yr | 10-15 | Yes, at 1.4-3.0% a year (24-51% of A) |
| Report 43 as written (20% of A) | 0.6A | 3 yr | 3.5 (1900) | Yes, by construction, but the event is small |
| Report 43 with 6 years | 1.2A | 6 yr | 7.1 (1900), 10.1 (2020 100 t) | Yes |
| "20% of capital" at 6 years | 20% | 6 yr | 20 | Only if running repairs are 43% or less of A |
| "20% of capital" at 10 years | 20% | 10 yr | 20 | Yes, if running repairs are 66% or less of A |

The combination consistent with **all** the measured sources is: an event of **7-15 per cent of
new**, at **6-10 years**, inside the measured total, with running repairs carrying the remainder.
At 1900 that is about £5-10 on a £71 wagon; at 2020, £50-105 on a £707 100-tonne hopper. A 20 per
cent event is consistent only at 10 years or with an unusually low running-repair share. `[DERIVED]`

## 5. Recommendation

1. **Keep the measured total as the envelope.** The head plus the amortised overhaul must equal
   A, not A plus an event. Pass 45 already replaced the 8-per-cent head with the ladder; the
   overhaul must therefore come **out of** that ladder.
2. **Head** = (1 - s) x A. With s = 0.20: 3.36 at 1900 for a 10-tonne wagon, 47.8 for a 2020
   100-tonne hopper.
3. **Overhaul event** = s x n x A. With s = 0.20, n = 6: £5.04 at 1900 (7.1 per cent of capital)
   and £71.6 for the 2020 100-tonne hopper (10.1 per cent). Set `initial_overhaul_cost` at about
   0.75 of the steady event and `max_overhaul_cost` at the steady event, `overhauls_before_max_cost`
   = 2. `[ESTIMATE for s and for the 0.75 first-event ratio; DERIVED for the totals]`
4. **State the interval basis.** 240,000 km is defensible only as "6 years at 40,000 km/yr", and
   that is a modern-duty assumption. At the measured 1961 duty of 5,638 km a wagon-year, six years
   is 33,800 km. Whichever is chosen, put the reference duty in the basis text; do not write a year
   count into a km field.
5. **Condemnation is not an overhaul.** Keep it out of `max_overhaul_cost`. The engine's nearest
   equivalents are `upgrade_price` (the whole replacement cost, since the old vehicle is deleted
   with no resale credit) and the wear/obsolescence ramps. The current class tuple's 0.35 upgrade
   share is a rebuild share, not a like-for-like wagon replacement.
6. **Do not use 20 per cent of capital at 3 years.** That event alone would be 6.7 per cent of
   capital a year, 1.13 times the entire measured annual maintenance, leaving nothing for running
   repairs.
7. **Record the split as an estimate.** s = 0.20 and n = 6 are a composition; only their product
   is constrained. Say so in the basis string, as pass 45 does for the head.

Evidence that would settle the remainder, in order of value: the 1947 HMRS *Regulations for
Repairing & Rebuilding of Wagons* (the condemnation rule and its money limits); the HMRS wagon
average repair costs 1972-81 (the only per-wagon-year series after 1961); the Chasewater RCH
"Charges for Private Owner Wagons" 1937 and "Private Wagons Stopped for Repairs" 1926 (per-job
prices, which would price a heavy repair directly; both archive-only); a Wagon Repairs Ltd contract
schedule (what the annual charge covered); and any later BR working instruction that restates the
monetary limits, since only the 1947 regulation and the 1960s-70s practice are now attested.

## Open questions

- What did the 1929 Colchester Gas and 1934 Arthur & Edward contracts **exclude**? The Lightmoor
  note shows the colliery shed closing, which implies everything, but the contract text is not
  readable online and neither is the Essex original.
- Was Swindon's 8,000 a year outturn or capacity, and what did it count as a repair? Both the 1935
  and the 1952 statements are worded as capacity, and the second is double the first, so either the
  works expanded or the two counted different work.
- What was the fleet's average wagon age in 1961? Neither Beeching nor the *Facts and Figures*
  booklets publish one, and without it the degree of depreciation behind the £1,037m is unknown.
- What was the wagon share of the £1,037m gross book value in 1961? Without it the book-value
  denominator cannot be computed and the 1961 figure can only be compared with a new price.
- What was a new 16-ton steel wagon's price in 1961? No measured figure was found; the pakset's own
  capital target (£113 at 1900, £624 nominal) is a model output, not evidence.
- Did BR's monetary limits ever get expressed as a percentage of new price, or were they always
  cash sums fixed administratively? Only the second is attested.
- Should `source-composition.md`'s "£54.3 = £14.3" line and report 43's 1961 deflator (528 against
  the table's 552) be corrected? Both are doc changes outside this pass's remit.
- Should the pakset's overhaul interval encode historical duty or in-game duty? This is a design
  choice, not a measurement, and it needs a user decision before the `.dat` pass.
