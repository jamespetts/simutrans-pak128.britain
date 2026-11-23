---
title: Road vehicle capital costs - British motor buses and coaches, 1896-1960
purpose: Historical purchase-price evidence for Pak128.Britain-Ex motor bus and coach cost balancing
author: research subagent (OpenCode)
date: 2026-11-23
status: working paper, not a knowledge-base document
scope: measured British bus and coach purchase prices 1896-1960, with same-year same-duty comparisons between makers
companion: ai/temp/road-rows-bus-capital.csv (one row per measured figure)
---

# Road vehicle capital costs: British motor buses and coaches, 1896-1960

This paper collects prices actually paid, tendered or published for British motor buses,
coaches and trolleybuses between 1896 and 1960, with the specification needed to compare
one make with another. It answers, as far as the evidence allows, whether Daimler buses
cost more than Leyland buses, and by how much.

The figures are nominal pounds of the year stated. Nothing has been converted, deflated
or rebased.

## 1. Method

### 1.1 Where the figures come from

Two classes of source were used.

1. **Contemporary trade press.** The Commercial Motor archive at
   `archive.commercialmotor.com`. Its weekly columns "Municipal Purchases and Proposals"
   and "Wheels of Industry" report, in a standard formula, what each corporation
   committee resolved to buy and at what price: "The tramways committee of X Corporation
   recommends acceptance of the tender of Y at £N each". Road-test and new-model articles
   give makers' list prices. These are the closest thing to a primary record that is
   available online, because the corporation minutes themselves are not digitised.

2. **Secondary histories that quote committee minutes.** Two MDS Books PDFs were
   especially productive: Bob Rowe's *Ashton & Manchester's Trolleybuses*, which reprints
   a complete ten-bidder trolleybus tender table, and Michael Yelton's *Gelligaer*
   (Prestige Series), which quotes the purchase resolutions of a small South Wales urban
   district council in sequence with prices.

### 1.2 How the figures were checked

Every figure recorded as MEASURED was read on the page carrying it, either by fetching
the Commercial Motor article directly or by extracting the document text and reading the
surrounding paragraph. Search-result snippets alone were not accepted.

The Commercial Motor archive's own search page is behind a JavaScript challenge and
cannot be queried. Its article pages fetch normally. Search was therefore run through
Exa and the resulting article URLs were fetched directly.

### 1.3 OCR damage

The archive's OCR is old and its characteristic failures matter for price work:

- The pound sign is frequently dropped or replaced by `1`, `i`, `L`, `2` or `4`.
  "at 11,345 each" is £1,345; "at i1.,220 each" is £1,220; "at 2650 each" is £650.
- A decimal point is sometimes substituted for a digit: "£70.5 each" for a body is
  £705.
- Company names are the worst affected. "SALroan Corporation" is Salford; "YARISOUTIE"
  is Yarmouth; "Earlier Motors, Ltd." is a maker I cannot identify with certainty.

Every figure where the pound sign was reconstructed is marked in the notes column of the
CSV and in the tables below. Four figures are excluded altogether because the OCR damage
cannot be resolved arithmetically (section 9).

### 1.4 Confidence labels

- **MEASURED** - a price paid, tendered, awarded or published as a price by the maker.
- **STATED** - a historian's or official's "about £X", a budget, a loan provision or an
  estimate. Not a transaction.
- **INFERRED** - my arithmetic or reading, not stated by the source.

### 1.5 What this pass did not do

It did not read any Simutrans `.dat` cost, runningcost, fixed_cost or upgrade_cost field,
and no pakset price enters any calculation here. The Simutrans forum thread 6521 was not
revisited.

## 2. Measured prices, 1909-1938

Prices are per vehicle unless marked "body" or "chassis". "Conf." is confidence in the
figure as read, not in the source's accuracy.

### 2.1 Before 1920

| Year | Make / item | Chassis or complete | Seats | £ | Source | Conf. |
|---|---|---|---|---|---|---|
| 1909 | Commer Car, Widnes UDC (4) | complete | 34 | 844 | CM 25 Mar 1909 p.6 | medium (OCR "4:844") |
| 1912 | LGOC B-type chassis, sold to Perth WA (30) | chassis | - | 650 | CM 25 Jan 1912 p.8 | high |
| 1913 | Daimler, Coventry (6) | complete | - | 739 | CM 2 Oct 1913 p.9 | medium (maker conflict) |
| 1915 | Daimler, Walsall (6) | complete | - | 894 16s 8d | CM 18 Feb 1915 p.10 | high |
| 1915 | Durham Churchill chassis, Sheffield (6) | chassis | - | 650 | CM 18 Feb 1915 p.10 | medium (OCR "2650") |

### 2.2 1926-1929

| Year | Make / item | Chassis or complete | Seats | £ | Source | Conf. |
|---|---|---|---|---|---|---|
| 1926 | Leyland Lioness, York (3) | complete | 26 class | 1,212 | CM 16 Nov 1926 p.42 | high |
| 1926 | C.H. Roe body, Leeds | body | - | 740 | CM 16 Nov 1926 p.42 | high |
| 1927 | Leyland single-deck, Birkenhead (9) | complete | - | 1,370 4s 5d | CM 11 Jan 1927 p.43 | high |
| 1927 | Leyland double-deck, Birkenhead (10) | complete | - | 1,510 4s | CM 11 Jan 1927 p.43 | high |
| 1928 | Leyland Titan, Glasgow (100) | complete | 52 class | 1,655 | CM 15 May 1928 p.40 | high |
| 1928 | Leyland Lion, Eastbourne (10) | complete | 36 | 1,345 | CM 10 Jan 1928 p.47 | medium (OCR) |
| 1928 | Bristol chassis, Hull (6) | chassis | - | 963 | CM 10 Jan 1928 p.47 | high |
| 1928 | C.H. Roe body, Hull (6) | body | - | 795 | CM 10 Jan 1928 p.47 | medium (OCR) |
| 1928 | Associated Daimler, Salford (6) | chassis | - | 1,220 | CM 20 Mar 1928 p.48 | medium |
| 1928 | Karrier(?), Salford (6) | chassis | - | 1,238 | CM 20 Mar 1928 p.48 | low (name OCR) |
| 1928 | Dennis, Salford (6) | chassis | - | 1,263 | CM 20 Mar 1928 p.48 | high |
| 1928 | Leyland, Salford (6) | chassis | - | 1,270 | CM 20 Mar 1928 p.48 | high |
| 1928 | Karrier 6-wheel, Portsmouth (6) | chassis | - | 1,217 | CM 20 Mar 1928 p.48 | high |
| 1928 | English Electric, Portsmouth (5) | body | 61 | 705 | CM 20 Mar 1928 p.48 | medium (OCR) |
| 1928 | Dennis E-type, Portsmouth (8) | chassis | - | 902 | CM 20 Mar 1928 p.48 | high |
| 1928 | Davidson, Portsmouth (8) | body | 36 | 443 | CM 20 Mar 1928 p.48 | high |
| 1928 | Bristol, Bradford (12) | complete | - | 1,300 | CM 20 Mar 1928 p.48 | high |
| 1928 | Leyland Tiger, Gelligaer (4) | complete | - | 1,485 | Yelton, *Gelligaer* | high |
| 1929 | Leyland Tiger LWS, Plymouth (25) | complete | 32 | 1,386 | CM 6 Aug 1929 p.48 | high |
| 1929 | Leyland, Stockton (5) | complete | 51 | 1,682 10s | CM 6 Aug 1929 p.48 | high |
| 1929 | Thornycroft, Gelligaer (2) | complete | - | 1,297 10s | Yelton, *Gelligaer* | high |

### 2.3 1930-1938

| Year | Make / item | Chassis or complete | Seats | £ | Source | Conf. |
|---|---|---|---|---|---|---|
| 1930 | Leyland chassis, Glasgow (75) | chassis | - | 950 | CM 2 Sep 1930 p.45 | high |
| 1930 | Vulcan chassis, Glasgow (25) | chassis | - | 933 | CM 2 Sep 1930 p.45 | medium (OCR "1933") |
| 1930 | Cowieson body, Glasgow (100) | body | - | 690 | CM 2 Sep 1930 p.45 | high |
| 1930 | Leyland Titan, Birkenhead (17) | complete | - | 1,720 | CM 14 Jan 1930 p.46 | medium (OCR) |
| 1930 | Leyland Lion, Birkenhead (6) | complete | - | 1,303 | CM 14 Jan 1930 p.46 | high |
| 1930 | Leyland, Croydon (2) | complete | - | 1,379 | CM 7 Oct 1930 p.45 | medium (OCR) |
| 1930 | Daimler, Lancaster (4) | complete | - | 1,375 | CM 14 Jan 1930 p.46 | high |
| 1930 | Daimler CH6, list | chassis | - | 1,275 | CM 28 Oct 1930 p.88 | high (list) |
| 1930 | Daimler CG6, list | chassis | - | 1,175 | CM 28 Oct 1930 p.88 | high (list) |
| 1931 | Leyland chassis, Birkenhead (5) | chassis | - | 957 | CM 13 Oct 1931 p.57 | high |
| 1931 | Massey body, Birkenhead (5) | body | - | 690 | CM 13 Oct 1931 p.57 | high |
| 1931 | Dennis + Strachans, Salford (18) | complete | 50-52 | 1,498 | CM 13 Oct 1931 p.57 | high |
| 1931 | Daimler, Middlesbrough (5) | complete | - | 1,634 | CM 13 Oct 1931 p.57 | high |
| 1931 | AEC Regent chassis, Yarmouth (5) | chassis | - | 930 | CM 28 Apr 1931 p.47 | high |
| 1931 | United body, Yarmouth (5) | body | - | 668 | CM 28 Apr 1931 p.47 | high |
| 1931 | Leyland chassis, Warrington (9) | chassis | - | 987 | CM 28 Apr 1931 p.47 | medium (OCR) |
| 1932 | Leyland chassis, Leicester (6) | chassis | - | 877 | CM 1 Mar 1932 p.42 | high |
| 1932 | Brush body, Leicester (6) | body | 50 | 666 | CM 1 Mar 1932 p.42 | high |
| 1932 | Leyland Titan chassis, Preston (10) | chassis | - | 918 | CM 2 Feb 1932 p.72 | high (recommended) |
| 1932 | Leyland Lion chassis, Preston (4) | chassis | - | 805 | CM 2 Feb 1932 p.72 | high (recommended) |
| 1932 | English Electric body, Preston | body | - | 720 | CM 2 Feb 1932 p.72 | medium (OCR) |
| 1932 | English Electric body, Preston | body | - | 480 | CM 2 Feb 1932 p.72 | high |
| 1932 | Leyland Titan, Cardiff (10) | complete | - | 1,525 | CM 1 Mar 1932 p.42 | high |
| 1932 | Leyland Tiger, Cardiff (5) | complete | - | 1,090 | CM 1 Mar 1932 p.42 | high |
| 1932 | Leyland Hybridge, Rawtenstall (14) | complete | - | 1,525 | CM 1 Mar 1932 p.42 | high |
| 1932 | Oil-engined bus, Gelligaer | complete | - | 1,599 10s | Yelton, *Gelligaer* | medium (year inferred) |
| 1933 | AEC, Gelligaer (3, average) | complete | 32 / 39 | 1,472 10s | Yelton, *Gelligaer* | high (average) |
| 1933 | AEC Q, Gelligaer (quoted) | complete | 39 | 1,847 | Yelton, *Gelligaer* | high |
| 1936 | AEC Q, Gelligaer | complete | 39 | 1,800 | Yelton, *Gelligaer* | high (part exchange) |
| 1937 | Glasgow, 100 double-deckers (class) | complete | - | 1,800 | CM 22 Jan 1937 p.27 | high (class) |
| 1937 | Guy Vixen + Duple, list | complete | 26 | 1,047 | CM 5 Nov 1937 p.50 | high (list) |
| 1937 | Trolleybus chassis, Manchester (10 bidders) | chassis | - | 960-1,500 | Rowe, *Ashton & Manchester* | high (year inferred) |
| 1938 | Leyland TS8 + Strachans, Gelligaer (2) | complete | - | 1,492 10s | Yelton, *Gelligaer* | high |
| 1938 | AEC Regal + Strachans, Gelligaer (1) | complete | - | 1,464 | Yelton, *Gelligaer* | high |

### 2.4 After 1938

Only one clean measured figure in the window was found.

| Year | Make / item | Chassis or complete | Seats | £ | Source | Conf. |
|---|---|---|---|---|---|---|
| 1955 | AEC/ACV double-decker, Newcastle (20) | complete | - | 4,328 14s | CM 22 Apr 1955 p.39 | high |

The 1939-1954 gap is a real gap in this pass, not an absence of purchases. Section 8
records the approximate class figures that partly fill it.

## 3. The Daimler question

### 3.1 The four same-year comparisons found

| Year | Daimler | Leyland | Difference |
|---|---|---|---|
| 1928 | Salford, Associated Daimler chassis £1,220 | Salford, Leyland chassis £1,270 | Daimler 3.9 per cent cheaper |
| 1930 | Lancaster, Daimler complete £1,375 | Croydon, Leyland complete £1,379 | Daimler 0.3 per cent cheaper |
| 1931 | Middlesbrough, Daimler complete £1,634 | Birkenhead, Leyland chassis £957 + Massey body £690 = £1,647 | Daimler 0.8 per cent cheaper |
| 1962 | Walsall, Daimler CVG6 chassis £2,839 | Walsall, Leyland Lowlander chassis £3,027 10s | Daimler 6.2 per cent cheaper |

The first is the only one drawn from a single tender list in which both makers quoted for
the same batch of vehicles. The 1931 and 1930 pairs compare different operators in the
same year, which is weaker but still controlled for date and for vehicle class. The 1962
pair is outside the 1896-1960 window and is included only because it is a direct
like-for-like quotation from the same committee in the same year.

The 1928 Salford tender in full, six vehicles from each of four makers in one resolution:

| Maker | Price per chassis | Change against Leyland |
|---|---|---|
| Associated Daimler | £1,220 | -3.9% |
| Karrier (OCR "Earlier Motors") | £1,238 | -2.5% |
| Dennis | £1,263 | -0.6% |
| Leyland | £1,270 | reference |

Leyland was the dearest of the four. The spread across all four makers was 4.1 per cent.

### 3.2 The one real Daimler cost adder

Daimler's distinctive specification in this period was the fluid flywheel with a Wilson
preselective gearbox. The maker's own published list prices for October 1930 price that
specification exactly:

| Model | Transmission | Chassis, double-deck | Chassis, single-deck |
|---|---|---|---|
| Daimler CH6 | fluid flywheel + Wilson preselective | £1,275 | £1,250 |
| Daimler CG6 | single-plate clutch + 4-speed sliding pinion | £1,175 | £1,150 |

The transmission accounted for £100 on a £1,175 chassis, 8.5 per cent. That is a
specification premium, not a maker premium: a Leyland with the optional Lysholm-Smith
torque converter, tested by Commercial Motor on 19 January 1934, carried its own adder in
the same way.

So the correct model is: Daimler's *base* chassis was priced at or slightly below
Leyland's, and Daimler's *typical municipal specification* included a transmission that
added roughly 8 per cent. Operators who bought Daimler almost always bought the fluid
flywheel, which is why Daimler fleets look expensive in aggregate while Daimler chassis
prices in tenders do not.

### 3.3 Statements by operators and engineers

- **Manchester, 1939.** The city council divided 250 chassis between Crossley (84),
  Leyland (83) and Daimler (83). The Daimler contract was "valued at over £200,000" and
  the report adds, significantly, "The Daimler vehicles will, of course, incorporate the
  Fluid Flywheel in the transmission" (CM 21 Apr 1939 p.96). The phrase "of course"
  indicates that the fluid flywheel was treated as part of the Daimler price, not as an
  extra. The aggregate figures are not usable (section 9).
- **Middlesbrough, 1935.** Both Middlesbrough and Stockton "adopted" Daimler
  double-deckers with fluid flywheels and preselective gearboxes for their joint
  heavy-traffic route, while using Leyland Titans where a low height was required
  (CM 8 Feb 1935 p.112). This is a duty-based split, not a price statement, but it shows
  the two makes being bought for different reasons in the same town.
- **Ipswich, 1953.** "Although Leyland Motors, Ltd., offered a lower price, four A.E.C.
  ... with Park Royal bodies are recommended to be purchased by Ipswich Corporation. It
  was decided to preserve standardization on A.E.C./Park Royal products" (CM 4 Sep 1953
  p.37). The clearest contemporary statement found that corporations did *not* simply
  buy the cheapest tender, and that the reason was fleet standardization rather than
  quality.
- **AEC Regal Mark II, 1936.** Commercial Motor: "although the price at which the
  machine is offered may appear high, in terms of value for money it is not only
  reasonable but competitive" (CM 17 Jan 1936 p.42). AEC was the maker with a
  reputation for high asking prices, not Daimler.
- **Daimler COG6 road test, 1937.** "first-class workmanship throughout the chassis ...
  seemed to augur well for the service life of the machine" (CM 13 Aug 1937 p.50). An
  impression from a new vehicle, not a measurement.

### 3.4 Reliability and durability

No measured comparison of Daimler and Leyland durability was found for 1896-1960. What
exists is context and one late statement.

Context on what "durability" meant in this trade: Maidstone Corporation docked and
decarbonised petrol vehicles every 10,000 miles and gave a complete overhaul every 30,000
miles (CM 26 Apr 1932 p.61); North Western Road Car used a 7,500-mile maintenance
multiple, a 30,000-mile light docking, a 60,000-mile medium docking and a 120,000-mile
general overhaul (CM 3 Sep 1948 p.38); a 1930 Institution of Automobile Engineers paper
described a 500-vehicle fleet achieving "nearly 98 per cent" availability on eight days
off the road per vehicle per year (CM 7 Jan 1930 p.62). These are fleet norms across mixed
makes, not maker differentials.

The only direct maker-versus-maker reliability testimony found is Sheffield's, and it is
from 1969, outside the window: the transport committee paid £307 per chassis more for
Daimler Fleetlines than the lowest tender because "they had found them more reliable and
less costly to maintain" (CM 26 Sep 1969 p.41). That is evidence for a Daimler durability
premium in the rear-engined era, and no evidence at all for one in 1920-1960.

### 3.5 Answer

**Were Daimler buses dearer to buy than Leyland buses?** On the figures found, no. In four
same-year comparisons spanning 1928 to 1962, Daimler was between 0.3 and 6.2 per cent
*cheaper* than Leyland, and in the one genuine multi-maker tender (Salford 1928) Leyland
was the dearest of four makers.

**By how much?** The measured spread between makes in a single tender is small: 4.1 per
cent across four makers at Salford in 1928. That is the scale of any realistic maker
premium or discount in this period. It is much smaller than the effect of specification.

**Were they more reliable or more durable?** No evidence was found either way for
1896-1960. The one measured reliability statement in the archive favours Daimler, but it
is from 1969.

**What should the pakset do?** Treat the fluid flywheel and preselective gearbox as a
costed option worth about 8 per cent of chassis price, and treat the Daimler marque
itself as priced at parity with Leyland, not above it. A Daimler premium of more than
about 3 per cent is not supported by anything found in this pass.

## 4. The other makers against Leyland

| Maker | Best evidence | Against Leyland | Read |
|---|---|---|---|
| Dennis | Salford 1928 chassis £1,263 v Leyland £1,270 | -0.6% | at parity |
| Dennis | Salford 1931 complete £1,498 v Middlesbrough Daimler £1,634 | -8.3% v Daimler | cheaper than Daimler |
| Karrier | Salford 1928 £1,238 | -2.5% | slightly cheaper |
| Karrier | Portsmouth 1928 six-wheel DD chassis £1,217 | not comparable | six-wheeler |
| AEC | Yarmouth 1931 Regent chassis £930; Leyland Glasgow 1930 £950, Leicester 1932 £877 | -2.1% / +6.0% | at parity |
| AEC | Gelligaer 1938 £1,464 v Leyland £1,492 10s | -1.9% | at parity |
| Bristol | Hull 1928 chassis £963; Bradford 1928 complete £1,300 | no Leyland comparator | cheap |
| Vulcan | Glasgow 1930 chassis £933 v Leyland £950, same order | -1.8% | slightly cheaper |
| Guy | Vixen coach 1937 list £1,047 (26 seats) | no comparator | light, cheap class |
| Crossley | Manchester trolleybus 1937 £995, in the 995 cluster | 0% | at parity |
| Tilling-Stevens | none found | - | unknown |
| Thornycroft | Gelligaer 1929 £1,297 10s | no comparator | - |

The pattern is consistent: in a competitive tender the chassis prices of the major makers
sat within a few per cent of each other, and the choice was made on standardization,
delivery, specification or local preference. Ipswich 1953 is the explicit statement of
that behaviour.

## 5. Chassis against body

### 5.1 Same-order splits

These are the most reliable, because chassis and body were bought in the same resolution
for the same vehicles.

| Year | Operator | Chassis £ | Body £ | Complete £ | Chassis share | Body maker |
|---|---|---|---|---|---|---|
| 1928 | Hull | 963 (Bristol) | 795 | 1,758 | 54.8% | C.H. Roe |
| 1928 | Portsmouth (SD) | 902 (Dennis) | 443 | 1,345 | 67.1% | Davidson |
| 1930 | Glasgow | 950 (Leyland) | 690 | 1,640 | 57.9% | Cowieson |
| 1931 | Birkenhead | 957 (Leyland) | 690 | 1,647 | 58.1% | Massey |
| 1931 | Yarmouth | 930 (AEC) | 668 | 1,598 | 58.2% | United |
| 1932 | Leicester | 877 (Leyland) | 666 | 1,543 | 56.8% | Brush |
| 1932 | Preston (DD) | 918 (Leyland) | 720 | 1,638 | 56.0% | English Electric |
| 1932 | Preston (SD) | 805 (Leyland) | 480 | 1,285 | 62.6% | English Electric |

For double-deckers the chassis took 55 to 58 per cent of the complete price. For a
single-deck saloon the chassis took 63 to 67 per cent, because the body was smaller.

The practical consequence for the pakset: a "chassis" price and a "complete vehicle" price
are not interchangeable, and the ratio is stable enough (0.55-0.58 for double-deck,
0.63-0.67 for single-deck) to use as a cross-check on any figure that does not state
which it is.

### 5.2 Body prices by body maker

| Year | Body maker | Seats | £ | £ per seat | Source |
|---|---|---|---|---|---|
| 1926 | C.H. Roe | - | 740 | - | CM 16 Nov 1926 |
| 1928 | C.H. Roe | - | 795 | - | CM 10 Jan 1928 |
| 1928 | English Electric | 61 | 705 | 11.56 | CM 20 Mar 1928 |
| 1928 | Davidson | 36 | 443 | 12.31 | CM 20 Mar 1928 |
| 1930 | Cowieson | - | 690 | - | CM 2 Sep 1930 |
| 1931 | Massey | - | 690 | - | CM 13 Oct 1931 |
| 1931 | United Automobile Services | - | 668 | - | CM 28 Apr 1931 |
| 1932 | Brush | 50 | 666 | 13.32 | CM 1 Mar 1932 |
| 1932 | English Electric | - | 720 | - | CM 2 Feb 1932 |
| 1932 | English Electric | - | 480 | - | CM 2 Feb 1932 |
| 1954 | Whitson ("Economist") | 44 | 1,885 | 42.84 | CM 16 Jul 1954 |

Two cautions. First, only three of these state seating, so £/seat can be computed for
only three 1920s-30s bodies; those three sit between £11 11s and £13 6s per seat, a
15 per cent band. Second, the 1954 Whitson figure is ambiguous: the headline calls it a
"bus body priced at £1,885" but the text says the vehicle was "mounted on a Sentinel
chassis", which may mean the price is for the complete vehicle.

Within the 1928-1932 window, body prices cluster at £666-£795 for a double-deck body and
£443-£480 for a single-deck body. The spread between body makers is comparable to the
spread between chassis makers: roughly 10 to 20 per cent.

## 6. Trolleybuses and petrol-electrics

### 6.1 The Manchester tender, 1937 (vehicles delivered 1938)

The only complete same-specification tender table found. Tenders were invited for 46
trolleybuses, equally split between four- and six-wheel types. The body contract went
separately and entirely to Crossley, so these prices are chassis with electrical
equipment.

| Bidder | 4-wheel £ | 6-wheel £ |
|---|---|---|
| Cravens | 960 | 1,037 |
| Brush Electrical | 995 | 1,090 |
| Crossley | 995 | 1,090 |
| English Electric | 995 | 1,090 |
| MCW | 995 | 1,090 |
| Park Royal | 995 | 1,090 |
| Roe | 995 | 1,090 |
| Strachans | 1,092 | 1,152 |
| Leyland | no bid | 1,035 |
| Cowieson | 1,500 | 1,600 |

Six of the ten bidders quoted exactly £995 and £1,090. The author of the source raises the
possibility of a price ring and notes that more than half the bidders were bodybuilders
who would have had to subcontract the chassis. Whatever the cause, the table shows that
in the trolleybus market list prices were administratively aligned to a degree not seen in
motorbus tenders, and that Cravens and Leyland were the only bidders willing to go below
the alignment.

The order went to Leyland (10 four-wheel, 26 six-wheel) and Crossley (28 four-wheel,
12 six-wheel). Cravens, the lowest bidder in both classes, got nothing.

### 6.2 Other trolleybus figures

| Year | Item | £ | Basis | Source |
|---|---|---|---|---|
| 1934 | Nottingham, 31 trolleybuses proposed | not stated | - | CM 26 Oct 1934 |
| 1936 | Huddersfield, 85 Karrier E6 with Park Royal bodies | about 1,176 each | STATED, "nearly £100,000" | CM 23 Oct 1936 p.60 |
| 1937 | Ashton-under-Lyne, 6 trolleybuses | loan sanction £12,149 for six = 2,025 each | STATED | CM 17 Dec 1937 p.7 |
| 1937 | Rotherham, one AEC 664T | not stated | - | CM 17 Dec 1937 |

The Huddersfield figure of about £1,176 for a complete 64-seat six-wheel trolleybus with a
Park Royal body is low against the Manchester chassis-only price of £1,035-£1,090 for a
six-wheeler in the same period, which suggests either a favourable contract or a
mis-OCR'd total. It is recorded as STATED only.

### 6.3 Petrol-electric

No price for a Tilling-Stevens petrol-electric chassis was found in this pass. The type is
documented as having been approved by the Metropolitan Police in early 1911 (CM 16 Mar
1926 p.27) but no purchase price appeared. This is the largest single gap in the maker
coverage.

## 7. Price by seating capacity and by year

### 7.1 Complete double-deck buses

| Year | £ | Example |
|---|---|---|
| 1913 | 739 | Coventry, 34 seats, open top |
| 1915 | 895 | Walsall Daimler |
| 1927 | 1,510 | Birkenhead Leyland |
| 1928 | 1,300-1,655 | Bradford low, Glasgow Titan high |
| 1929 | 1,683 | Stockton, 51 seats |
| 1930 | 1,375-1,720 | Lancaster Daimler low, Birkenhead Titan high |
| 1931 | 1,498-1,647 | Salford Dennis, Birkenhead Leyland |
| 1932 | 1,525-1,543 | Cardiff/Rawtenstall, Leicester |
| 1937 | 1,800 | Glasgow, 100 buses |
| 1955 | 4,329 | Newcastle |

The 1931 upper figure of £1,647 is a derived complete equivalent (Leyland chassis £957
plus Massey body £690 bought in the same resolution), not a single measured complete
price. The Salford 1928 chassis prices are excluded from this ladder because they are
chassis only.

### 7.2 Price per seat

| Year | Vehicle | Seats | £ | £/seat |
|---|---|---|---|---|
| 1913 | Coventry | 34 | 739 | 21.7 |
| 1928 | Eastbourne Lion SD | 36 | 1,345 | 37.4 |
| 1929 | Plymouth Tiger SD | 32 | 1,386 | 43.3 |
| 1929 | Stockton DD | 51 | 1,683 | 33.0 |
| 1931 | Salford Dennis DD | 50-52 | 1,498 | 28.8-30.0 |
| 1932 | Leicester (877+666) | 50 | 1,543 | 30.9 |
| 1937 | Guy Vixen coach | 26 | 1,047 | 40.3 |

Two structural facts fall out of this, and both matter for a size ladder:

1. **Cost per seat falls as capacity rises within a body type.** The 32-seat single-decker
   cost £43 per seat; the 50-seat double-decker cost £29-31.
2. **A double-decker is cheaper per seat than a single-decker of similar total capacity**
   in the same year. The 36-seat Eastbourne single-decker at £37.4 per seat against the
   51-seat Stockton double-decker at £33.0 the following year.

The 1913 figure at £21.7 per seat is not comparable: open-top bodies, solid tyres and no
electrical equipment.

### 7.3 The post-1938 gap, in STATED figures only

| Year | Item | £ | Basis | Source |
|---|---|---|---|---|
| 1946 | Glasgow, 230 buses, "about £800,000" | about 3,478 | class average | CM 27 Dec 1946 p.32 |
| 1947 | Manchester, 100 double-deckers, £350,000 loan | 3,500 | loan provision | CM 10 Jan 1947 p.57 |
| 1953 | Liverpool, 130 buses, "about £500,000" | about 3,846 | estimate | CM 18 Mar 1955 p.87 |
| 1958 | Leyland Atlantean, complete | about 7,000 | author's statement | *Impact of the Atlantean* |

Between the 1937 figure of £1,800 and the 1946 figure of about £3,478 the nominal price
roughly doubled, which is consistent with the wartime inflation recorded elsewhere in the
trade press (Leeds' rolling-stock engineer put a double-decker at "roughly £1,750" before
the war and "practically £3,500" in November 1946, CM 29 Nov 1946 p.54). That statement is
the best single control on the 1939-1946 price level.

## 8. Premia I would recommend

Mechanism: a chassis-cost multiplier applied by make against a Leyland base of 1.00, with
the Daimler transmission modelled separately as a specification adder rather than folded
into the marque multiplier. Bands are the range the evidence supports, not a point
estimate; the width reflects how few matched pairs exist.

| Make | Multiplier band | Per cent band | Central | Mechanism | Basis |
|---|---|---|---|---|---|
| Leyland | 1.00 | 0 | 1.00 | reference | dearest at Salford 1928; mid-cluster elsewhere |
| Daimler | 0.95-1.02 | -5% to +2% | 0.98 | marque multiplier, plus separate +8% transmission adder when the model has fluid flywheel and preselector | 4 same-year pairs, all at or below Leyland |
| AEC | 0.97-1.02 | -3% to +2% | 1.00 | parity | Yarmouth 1931, Gelligaer 1938 |
| Dennis | 0.95-1.00 | -5% to 0% | 0.98 | parity to small discount | Salford 1928, Salford 1931 |
| Guy | 0.95-1.00 | -5% to 0% | 0.97 | discount; light construction | Vixen list price, class reputation |
| Karrier | 0.95-1.00 | -5% to 0% | 0.97 | small discount | Salford 1928 |
| Crossley | 0.97-1.01 | -3% to +1% | 0.99 | parity | Manchester trolleybus tender only |
| Bristol | 0.95-1.00 | -5% to 0% | 0.97 | discount | Hull 1928, Bradford 1928, no direct comparator |
| Vulcan | 0.98-1.01 | -2% to +1% | 0.99 | parity | Glasgow 1930 same order |
| Thornycroft | 0.97-1.03 | -3% to +3% | 1.00 | parity, low confidence | one figure only |
| Tilling-Stevens | no evidence | - | 1.00 | leave at parity and mark as unverified | nothing found |

Body multipliers, against a notional English Electric/Roe base of 1.00:

| Body maker | Multiplier band | Basis |
|---|---|---|
| English Electric | 0.95-1.02 | 705 (1928), 720 and 480 (1932) |
| C.H. Roe | 1.00-1.05 | 740 (1926), 795 (1928) |
| Brush | 0.95-1.02 | 666 for 50 seats (1932) |
| Massey | 0.97-1.02 | 690 (1931) |
| United | 0.95-1.00 | 668 (1931) |
| Cowieson | 0.97-1.02 | 690 (1930) |
| Davidson | 0.95-1.00 | 443 for 36 seats (1928) |
| Strachans | 1.05-1.12 | 1,092 against a 995 cluster (1937 trolleybus) |
| Cravens | 0.93-0.98 | 960 against a 995 cluster (1937 trolleybus) |

Two warnings about these bands.

1. **The maker effect is small and the specification effect is large.** A 4 per cent
   spread across four makes in one tender is the realistic scale. Any pakset premium
   above about 5 per cent needs a specification reason, not a marque reason.
2. **The trolleybus cluster is not a free market.** Six identical bids at £995 and £1,090
   mean the trolleybus chassis prices cannot be used to rank makers. Use them only to set
   the trolleybus level against the motorbus level.

## 9. Dead ends and unusable figures

These were examined and rejected. Recording them prevents another pass repeating the work.

- **Manchester 1939, "orders total £644,000".** 250 chassis plus bodies. The headline says
  £644,000, the body text OCRs as "£044,000". Either figure gives £2,576 per bus, which is
  above the contemporary complete-bus price of about £1,750 quoted by Leeds in 1946 for
  the pre-war period. The Crossley share is given as "approximately £310,000" and
  Daimler's as "over £200,000", which cannot be reconciled with 250 chassis. Unusable.
- **Warrington 1931, nine Brush 56-seat bodies "at 03,318".** That is £369 each, against
  £666 for a 50-seat Brush body at Leicester the following year. Either the OCR has lost a
  digit or the bodies were shells. The chassis figure (£987) is retained; the body figure
  is not.
- **Coventry 1913, "six Daimler motorbuses" at £4,434.** Wikipedia's Coventry Corporation
  Transport article gives the identical £739 per bus for six Maudslay 34-seat open-top
  double-deckers in 1914. One of the two is wrong. The Commercial Motor figure is
  contemporary and is recorded, with the conflict flagged.
- **Associated Daimler, Salford 1928.** Associated Daimler Company was the 1926-1928
  Daimler/Guy sales combination. The model is not stated, so the £1,220 may be a
  Guy-derived rather than a Daimler-derived chassis. This weakens the strongest single
  comparison in the paper. It is retained because the entity traded as Daimler's sales
  company at the time, but it should not be presented as a pure Daimler figure.
- **Salford 1928, "Earlier Motors, Ltd." at £1,238.** The name is unrecoverable from the
  OCR. Karrier is the most probable reading on letter-shape grounds and is the reading
  used, but it is an inference.
- **Glasgow 1937, 100 buses for £180,000.** The composition is known (50 Leyland, 25
  Daimler, 25 AEC chassis; 50 Cowieson, 50 MCW bodies) but the per-maker split is not
  given. This is the most valuable missing figure in the whole pass.
- **Huddersfield 1936, 85 Karrier trolleybuses "nearly £100,000".** About £1,176 each,
  which is low against the Manchester chassis-only price for a six-wheel trolleybus.
  Recorded as STATED only.
- **Commercial Motor's own search.** The search page is JavaScript-gated and returns
  nothing to a direct fetch. All Commercial Motor material in this pass was reached
  through Exa and then fetched article by article. The archive also returns HTTP 202 to a
  plain scripted GET, so the article pages have to be fetched through a browser-like
  client.
- **Corporation minutes.** Not digitised. Every municipal figure in this paper comes
  either from Commercial Motor's reporting of the committee or from a published history
  quoting the minute.
- **Tilling-Stevens.** No purchase price found at all, in any year. The petrol-electric
  premium cannot be quantified from the sources used.
- **Bristol.** Only two prices (Hull 1928 chassis £963, Bradford 1928 complete £1,300) and
  no same-year Leyland comparator.
- **LGOC B-type at "about £300" (1911).** Not verified. The evidence found points the
  other way: a B-type chassis sold to Perth City Council in 1912 at £650, a complete
  Walsall Daimler at £895 in 1915, and a Sheffield budget of £825 per bus excluding tyres
  in 1914. A complete 34-seat bus at £300 in 1911 would be far below all of these. Either
  the £300 refers to a chassis-only production cost after the Walthamstow factory reached
  volume, or to a post-war surplus sale price, or it is a misremembering. It should not be
  used until a source states its basis.

## 10. Open questions

1. Does any published history give the per-maker values of the Glasgow 1937 contract?
2. Did Birmingham, which standardised on Daimler, record what it paid relative to the
   Leyland tender? Birmingham's committee minutes are the most promising untapped source.
3. What was a Tilling-Stevens petrol-electric chassis priced at, and what premium did it
   carry over a comparable petrol chassis?
4. What is the basis of the £300 B-type figure?
5. What were Leyland PD2/PD3 and Daimler CVG6 chassis prices in 1955-1960? The single
   1955 Newcastle figure is not enough to build a post-war maker ladder.

## 11. Sources

Contemporary trade press, all at `archive.commercialmotor.com`:

- 25 March 1909, p.6, "Motorbus" - Widnes Commer Cars.
- 11 July 1907, p.7, "The Motor Omnibus World" - Sheffield's £1,000 estimate.
- 25 January 1912, p.8, "The Latest Issue Result" - Perth B-type chassis.
- 2 October 1913, p.9, "In Public Service" - Coventry.
- 22 January 1914, p.14, "In Public Service" - Sheffield £825 ceiling.
- 18 February 1915, p.10, "The Wheels of Industry" - Walsall, Sheffield.
- 16 March 1926, p.27, "Public-Service Vehicle Development" - Tilling-Stevens approval.
- 16 November 1926, p.42, "Wheels of Industry" - York, Leeds.
- 11 January 1927, p.43, "Wheels of Industry" - Birkenhead.
- 10 January 1928, p.47, "Municipal Purchases and Proposals" - Eastbourne, Hull.
- 20 March 1928, p.48, "Municipal Purchases and Proposals" - Salford, Portsmouth, Bradford.
- 15 May 1928, p.40, "Loose Leaves" - Glasgow Titans.
- 6 August 1929, p.48, "Municipal Purchases and Proposals" - Plymouth, Stockton.
- 14 January 1930, p.46, "Municipal Purchases and Proposals" - Birkenhead, Lancaster.
- 2 September 1930, p.45, "Municipal Purchases and Proposals" - Glasgow.
- 7 October 1930, p.45, "Municipal Purchases and Proposals" - Croydon.
- 28 October 1930, p.88, "New Daimler Chassis" - CH6 and CG6 list prices.
- 7 January 1930, p.62, "Maintaining Public-Service Vehicles" - availability.
- 28 April 1931, p.47, "Municipal Purchases and Proposals" - Warrington, Yarmouth.
- 13 October 1931, p.57, "Municipal Purchases and Proposals" - Birkenhead, Salford,
  Middlesbrough.
- 2 February 1932, p.72, "Municipal Purchases and Proposals" - Preston.
- 1 March 1932, p.42, "Municipal Purchases and Proposals" - Leicester, Cardiff,
  Rawtenstall.
- 26 April 1932, p.61, "Maintenance Methods at Maidstone".
- 19 January 1934, p.42, "Testing a Leyland Titan with Torque Converter".
- 8 February 1935, p.112, "Tees-side Without Tramways".
- 17 January 1936, p.42, "New A.E.C. Regal Mark II".
- 23 October 1936, p.60, "Trolleybus Extensions at Huddersfield".
- 22 January 1937, p.27, "Glasgow's £180,000 Bus Order".
- 13 August 1937, p.50, "Refinement Characterises the Performance of the Daimler
  Double-decker".
- 5 November 1937, p.50, "Guy" - show prices.
- 17 December 1937, p.7, "Municipal Purchases and Proposals" - Ashton-under-Lyne.
- 21 April 1939, p.96, "Operating Aspects of" - Manchester contract values.
- 27 December 1946, p.32, "Glasgow Orders 230 New Buses".
- 29 November 1946, p.54, "Has the Double-decker Outworn its Usefulness?".
- 10 January 1947, p.57, "£000,000 Loan for Manchester?".
- 3 September 1948, p.38, "Fleet Maintenance Between Peaks".
- 4 September 1953, p.37, "Ipswich Accepts Higher Tender".
- 16 July 1954, p.43, "Lightweight Bus Body Priced at £1,885".
- 18 March 1955, p.87, "Liverpool Wants 130 Buses".
- 22 April 1955, p.39, "Municipal Purchases and Proposals" - Newcastle.
- 26 September 1969, p.41, "Sheffield Plumps for Dearer Buses".
- 6 July 1962, p.40, "Walsall Bus Orders".

Secondary works:

- Rowe, Bob. *Ashton & Manchester's Trolleybuses*. MDS Books.
  `mdsbooks.co.uk/media/wysiwyg/freedownloads/Ashton_Manchester_TB.pdf`
- Yelton, Michael. *Gelligaer* (Prestige Series). MDS Books.
  `mdsbooks.co.uk/media/wysiwyg/Gelligaer.pdf`
- *Impact of the Atlantean*. MDS Books.
  `mdsbooks.co.uk/media/wysiwyg/Impact_of_the_Atlantean.pdf`

Web references used only for conflict checking:

- "Coventry Corporation Transport", Wikipedia (the £739 Maudslay conflict).
- "LGOC B-type", Wikipedia (general history; no price).
