---
status: draft
verified: simutrans-extended ex-15 @ bdfdc8311; New ex-15 @ 8d0603d81
---
# Cost of capital

**Covers**: the planned borrowing and equity mechanism, what exists in the engine today, the gap
between the two, and the pakset-side evidence and settings the feature will need.

The design is recorded in the engine's own roadmap, `ai/project-roadmap.md`, section "Cost of
capital". This document does not replace it; it records the state of play and what the pakset must
supply.

## Why it matters now

The arithmetic has to be done in engine units. A pound figure taken at the capital conversion
cannot be compared with a cash figure taken at the revenue conversion, and an earlier draft of
this section did exactly that and overstated the case.

- Starting money in 1900 is `30,000,000` units.
- A complete route kilometre — its share of way, stations, land, signalling, locomotives and
  carriages — is **3,163,096 units** at present values, which is £12,536 at the capital
  conversion. Starting money buys **9.5 kilometres**.
- After the corrections, infrastructure to the synthesis's recommendations and rolling stock ÷8,
  the same kilometre is **2,372,530 units**, or £9,403. Starting money buys **12.6 kilometres**.
- So the corrected first line is **cheaper than the present one**, not dearer: by about a third.
  It is cheaper because rolling stock is 92 per cent of the capital and falls eightfold, while
  infrastructure is 8 per cent and rises about sevenfold on this line.

The composition changes even though the total falls: rolling stock drops from 92 per cent of the
capital to about 13, and infrastructure rises to about 87. That is why extension becomes
relatively more expensive than intensity, even though both are cheaper.

**The start is therefore not a capital-shortage problem.** What the corrections change is the
operating account: standing charges, crew and traffic expenses bite from the first month, before
revenue has built. The case for borrowing is an operating-loss case, not a construction-cost one,
and the facility should be sized against the months of operating loss a new line runs before it
breaks even — not against its capital cost.

That is a weaker case than "a railway was financed with other people's money", but it is the one
the arithmetic supports. `[USER-DIRECTION:2026-11-17]`

## The plan as recorded

The engine roadmap sets out, in substance:

- **Players should start with nothing or a very small lump sum** and take long-term loans to
  invest. The present large free lump sum under-estimates the cost of capital.
- **Bonds**, in the manner of Railroad Tycoon: issued for one, two, five or ten years, the longer
  bonds carrying a higher annual rate; issuable only if the company's **credit rating** is good
  enough; poorer ratings pay more, and bad enough ratings cannot issue at all; a new player starts
  with a moderate rating, able to borrow but at fairly high rates; the bond is repaid in a lump
  sum at maturity.
- **Or bank loans**, repayable in instalments from a month after drawdown, possibly with a three
  month repayment holiday, which is easier for a player to budget.
- **GUI**: a new dialogue from the finance window showing the number of loans or bonds, dates
  taken, dates due, rates, a control for borrowing more and one for early repayment at a penalty;
  and a new graph for loan and bond repayments.
- **Credit limit for a young company**, in part dependent on the wealth-weighted aggregate
  success of the other established companies: profit as a proportion of assets per annum, so a
  late entrant in a map with a large, profitable incumbent can borrow more, and recent
  insolvencies count against. There should be a **minimum**, which is also the default when
  starting a map with no other players.

## What exists today

Two things, neither of them the feature.

- **A starting windfall.** `starting_money` in `config/simuconf.tab`, inflation-adjusted through
  the `general` index, is granted at the start. `[CODE simutrans-extended ex-15 @ bdfdc8311]`
- **An overdraft.** `finance_t::book_interest_monthly` charges interest each month on a negative
  balance at `get_overdraft_rate_percent()` over twelve months, which is the `base rate` series
  plus `overdraft_percent_above_base_rate`, default 2. `finance_t::can_afford` lets a player spend
  down to a soft credit limit, itself half the better of two computations: twelve months of
  operating profit divided by the overdraft rate, or the value of non-financial assets.
  `[CODE simutrans-extended ex-15 @ bdfdc8311]`

So borrowing happens only as an overdraft, with no term, no maturity, no instrument and no
rating, and a company with no history and no assets has a limit of zero. The source says as much:
"Currently only overdraft interest. TODO: Add other kinds of borrowing."

## What the pakset must supply

| Item | Status | What is needed |
|---|---|---|
| `base rate` series | Implemented | The anchor rate; already a historical series in `config/prices.tab` |
| Overdraft margin | Implemented, 2 per cent | Confirm against historical bank overdraft practice |
| **Term structure** | **Partly researched** | Only short against long is observed: bank advance rate against corporate bond yield, 1922-1965. No 1/2/5/10 ladder exists, so it must be interpolated or set by design |
| **Railway borrowing yields** | **Researched** | Debenture yields 2.43-4.35 per cent 1854-1914; coupons 3-4 per cent 1850s-1930s; see [borrowing-rates](borrowing-rates.md) |
| **Non-railway transport yields** | **Researched** | Canals, omnibus and tramways 3.0-5.5 per cent, mostly 4.0-5.0, 1770-1908; docks and shipping; see [borrowing-land-transport-1750-1948](borrowing-land-transport-1750-1948.md) |
| **Commercial rates after 1945** | **Researched** | By decade and credit quality; see [commercial-rates-1945-2026](commercial-rates-1945-2026.md) |
| **Credit rating bands** | **Partly researched** | Poor credit paid more, and the 1997 Railtrack issue priced 78 basis points over the Treasury; the bands themselves still need setting |
| Starting money | Implemented | To be reduced to near zero once borrowing exists |

The gap is the rates. The engine can hard-code a term structure, but the pakset is where the
historical evidence belongs, and it is the pakset's job to say what a railway paid to borrow in
1840, 1900, 1930 and 1970.

## What exists in the evidence base already

- British railway net income on capital, 1923-1948: Southern 3.78 per cent, Great Western 3.07,
  LMS 2.63, LNER 2.00, against 14.55 for ten other public companies. That is the return earned,
  which bounds what could be paid to lenders.
- Acworth's capital-to-receipts ratio of about eight, and the 4-5 per cent net return used as the
  balance test.
- Ship dividends of 5 to 8 per cent in 1910 and 1912, from two tramp companies, recorded in
  [ship-maintenance](vehicle-cost/ship-maintenance.md).

None of these is a lending rate. A research task is needed before the feature can be calibrated.

## What the rates imply for the design

Seventy figures are recorded in [borrowing-rates](borrowing-rates.md). Four of them shape the
feature:

1. **The coupon was stable at 3 to 4 per cent for eighty years.** Board of Trade figures for 1865
   give an average rate paid of 4.10 per cent on funded debenture stock and 4.42 per cent on
   renewable debenture loans, against a standard 4 per cent coupon that persisted into the 1930s.
   A game bond should therefore carry a coupon in that band for most of the timeline.
2. **The variation came through the yield, not the coupon.** Debenture yields ran 2.43 to 4.35 per
   cent between 1854 and 1914, typically 3.0 to 4.1, with a trough of 2.4 to 2.5 in 1896-97 caused
   by the Trust Investment Acts. If the engine charges a rate, that rate is economically the yield,
   not the printed coupon.
3. **The `base rate` series must not be used as the coupon directly.** It moves far more than
   railway coupons did — from 3 per cent in 1900 to double figures in the 1970s — so using it would
   make early borrowing too cheap and late borrowing too dear relative to what a railway paid.
   It is the anchor for the *spread*, not the rate itself.
4. **There is no observed 1/2/5/10-year ladder.** The only usable term evidence is short against
   long: bank advance rate against corporate bond yield, 1922-1965. The ladder must therefore be
   either interpolated between those two and labelled as a construction, or set as a design choice
   and documented as one.

The later end is easy and well evidenced: long gilts at 6.55 to 14.88 per cent over 1965-1981,
corporate bonds at 7.07 to 15.94, and Railtrack in 1997 at a 7.375 per cent coupon and 7.33 per
cent yield, 78 basis points over the 8 per cent Treasury 2021 for twenty-five years. There is no
railway market rate today, because Network Rail's debt is sovereign-guaranteed and since 2014 it
borrows from the Department for Transport.

**That last point is a warning, not a figure to use.** The player runs a private enterprise in every
era, and from the twentieth century the pakset's fleet is mostly buses, coaches, lorries, ships and
aircraft rather than railway rolling stock. The rate that matters is therefore the **commercial
rate for a private company**, and after 1945 it is not a railway rate at all:

- railway debt became nationalised and then sovereign-guaranteed, so its rate measures the state's
  credit, not a company's;
- buses, coaches and lorries were financed by bank borrowing and hire purchase, and later by
  leasing;
- ships and aircraft were financed against the asset, by ship mortgage or by aircraft-secured
  lending, export credit and sale-and-leaseback, which prices differently from unsecured corporate
  debt.

So the rate table the feature needs is a **commercial** one, by era and by credit quality, with
asset-secured rates where the vehicle is the security. The railway debenture series is the best
evidence for the nineteenth century and for the corporate norm; it is not the whole of the
twentieth.

## The rate by era, 1750-2026

Two collections now cover the whole timeline. The striking result is how stable the rate was
before the Second World War, and how little the railway differed from other transport borrowers:

| Era | Borrower | Rate, per cent |
|---|---|---|
| 1770-1848 | canals: Stroudwater 1796, Grand Junction, Leeds and Liverpool, Grand Canal, Manchester Ship Canal | 3.0-5.0, mostly 3.5-5.0 |
| 1854-1914 | railways, debenture **yield** | 2.43-4.35, typically 3.0-4.1 |
| 1865 | railways, average **rate paid** (Board of Trade) | 4.10 funded stock, 4.42 renewable loans |
| 1894-1908 | omnibus and tramway debentures and preference: LGOC, Tilling, Associated Omnibus, ten tramway companies | 3.5-5.5, mostly 4.0-4.5 |
| 1945-2026 | all sectors, commercial | see the decade table below |

So a British transport company borrowed at about **4 to 5 per cent from the 1770s to 1948**, and
the railway was not exceptional: the canal, omnibus and tramway rates sit in the same band. That
is a considerable simplification for the feature — for two-thirds of the game's timeline a single
rate with a narrow credit loading is historically sufficient, and only after 1945 does a series
become necessary.

Sources: [borrowing-rates](borrowing-rates.md) for the railway series,
[borrowing-land-transport-1750-1948](borrowing-land-transport-1750-1948.md) for canals, omnibus and
tramways, and
[borrowing-docks-shipping-1750-1948](borrowing-docks-shipping-1750-1948.md) for docks, shipping and
the general industrial benchmark.

## The commercial rate by decade, 1945-2026

From [commercial-rates-1945-2026](commercial-rates-1945-2026.md), a private company of moderate
credit paid approximately:

| Decade | Rate, per cent | Basis |
|---|---|---|
| 1945-49 | 3.2-3.4 | bank advance, at or below Bank Rate |
| 1950-59 | about 4.5 | bank advance; hire purchase 7.5-9.0 flat alongside |
| 1960-69 | about 6.9 | bank advance; hire purchase 8.5-13.0 flat |
| 1970-79 | 10.1-18.4 | peak 1974-75 |
| 1980-89 | 14.3-18.4 | peak 1980 |
| 1990-99 | 10.3-16.7 | peak 1990 |
| 2000-09 | 5.2-7.7 | |
| 2010-19 | 2.9-3.1 | bank loans cheaper than long bonds |
| 2020-26 | 5.8-7.5 | SME new lending 6.55 in September 2026 |

A good credit, BBB or better, runs from about 3.8 in 1945 to 19.4 at the 1974 peak, 2.5-4.8 over
2010-19, and 6.3-6.8 in October 2026. The spread between good and moderate credit is therefore
narrower than the movement of the rate itself, which is the pattern the credit rating should
reproduce: the level moves with the market, the loading distinguishes the borrower.

Three limits are recorded in the source and matter for the design:

- **No rating-bucket series exists before December 1997.** Before that the Bank of England
  debenture series and the BofA sterling investment-grade index are single aggregates. A rating
  ladder before 1997 must be constructed, or the rating must act on a single rate by a stated
  loading.
- **No hire purchase or leasing series after 1974**, so the road-fleet finance used from the
  1970s onward has to be proxied by bank or lease rates.
- **Hire purchase figures before 1974 are flat rates**, which are roughly double the true annual
  rate; they must not be entered as though they were interest rates.

## Acceptance tests

1. A new company starts with a small or zero balance and can borrow only through an instrument
   with a stated term and rate.
2. A bond matures on its stated date and the principal is debited in one sum; a loan is debited
   in instalments.
3. Interest on each instrument appears monthly under interest, and the repayment appears in the
   finance history and graph.
4. Credit rating gates issuance, a new company can issue at a high rate, and the minimum limit
   applies when no other companies exist.
5. Early repayment applies the stated penalty.
6. With no instruments outstanding the behaviour matches the present engine, so existing
   savegames load and run unchanged.

## Open questions

- Bond or instalment loan first? The roadmap records both; the instalment loan is the easier to
  budget and the easier to implement, and the bond requires the credit rating and the maturity
  logic.
- Should the credit limit consultation of other companies apply in single-player against AI
  companies, or only in multiplayer?
- Should `base rate` remain the anchor for the term structure, or should railway debenture yields
  become their own series in `config/prices.tab`?
- Does the starting windfall disappear entirely, or remain as a small founder's stake?
