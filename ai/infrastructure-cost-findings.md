---
status: draft
verified: New ex-15 @ 5a254ba24 (working tree)
---
# Infrastructure cost findings

**Covers**: the results of the absolute-cost audit of `New/ways/`, against the historical anchors
assembled for the purpose. The conversion chain and the first-pass ratios:
[infrastructure-base-costs](infrastructure-base-costs.md). The year index:
[prices-infrastructure](prices-infrastructure.md).

Read this as a set of findings awaiting a decision, not as a record of changes made. Nothing
below has been applied to any `.dat` file.

## The chain is right; the objects are not

The audit's first question was whether the conversion chain itself is wrong, because a wrong
chain would make every ratio meaningless.

The decisive test is the one object whose real price is known from a modern contract rather than
from a historical account: `motorway`, `.dat` cost 190,000, introduced in 1958. On the chain used
in [infrastructure-base-costs](infrastructure-base-costs.md) that is £75,299 a kilometre at 1900
prices, which becomes about £7.2 million a kilometre in 2011 money against a real figure of about
£18.6 million from the 2011 road cost data. The pakset motorway is therefore **2.5 times too
cheap**, not orders of magnitude out.

An alternative reading at one twelfth of the chain would put every 19th-century railway class
within a factor of two of its own history, and the motorway thirty times too cheap. A road
contract price is much stronger evidence than a handful of Victorian structure accounts, so the
chain stands and the defects are in the objects.

## What the objects look like against history

| Class | Ratio of pakset to history | Confidence |
|---|---|---|
| Track ways, against whole-line capital | 1.0 to 1.3 for 1845-1888; up to 4.9 for 1981 | The ways match the whole-line average of £20,300-22,400 a km from 1858 to 1902 almost exactly |
| Track ways, against permanent way only | 11.5 to 16.8 | The same numbers read against rails rather than whole line |
| Way maintenance | 7.9, and 8.3 years of capital against a historical 65 | Firm anchor, three independent dates agreeing within 20% |
| Masonry and brick viaducts | 14 to 30 | Firm; the forum's viaduct table is consistent within a factor of five |
| Aqueducts | 8 to 20 | Three items only |
| Railway tunnels, capital | 6 to 40 | Firm; four independent dated tunnels agree |
| Railway tunnels, maintenance | 43 to 76 | Firm |
| Timber trestle, maintenance | 65, and 22 times the masonry viaduct it is a cheaper version of | Almost certainly a data error |
| Canals, capital | 3 to 12 | Firm; the class anchors are wide but consistent |
| Canals, maintenance | 15 to 23 | Single 1938 ratio |
| Electrification | 3 to 9, with the trend inverted | Weak; no track count for the 1955 schemes |
| Signals | Not comparable as specified | The objects appear to price a block section, not an arm |

## What this means

The ways are the one class that is close to right, and they are right against **whole-line
capital**, not against permanent way. That is a real design question rather than an error: if the
way object is meant to be the whole line, the numbers are correct and the structures should be
cheap premiums; if it is meant to be permanent way, both are wrong in opposite directions.

The structures and the maintenance are wrong by large factors. Maintenance is the defect that
matters most in play, because 8.3 years of capital against a historical 65 makes routes
uneconomic in a way no historical railway was.

## Data defects found in passing

These are bugs, not calibration judgements, and are independent of any decision below:

- `ways/wooden-trestle-stone-pillar.dat` has `cost=cost=672000`, which is malformed and will not
  parse as intended.
- `ways/iron-arch-rail.dat` has `maintenance=15360`, which is 73 times a first-class way and
  3.5 times a brick tunnel. Almost certainly a misplaced digit.
- All brick viaducts share one cost regardless of height, span or pillar spacing, and all masonry
  aqueducts share one cost across three widths.
- `signals.dat` and `signals-narrow.dat` hold 168 objects with costs differing by 178 times within
  a single working method and era.
- Eight files hold several `Obj=` blocks, so an audit script keyed to one object per file reads
  only the first.

## The decision to take

1. **What is a way object?** Whole line, or permanent way only. This decides whether the track
   costs are right or twelve times too dear, and it decides whether structures should carry their
   full historical cost or only a premium.
2. **Maintenance.** Whichever answer above, the maintenance of ways, tunnels and canals is far too
   high relative to capital, and tunnels by a factor of forty. This is the change with the largest
   effect on play and the strongest evidence behind it.
3. **Structures.** Masonry and brick are 14 to 30 times their historical cost per metre, and the
   relative price of masonry against iron and timber is also wrong: masonry is 4.3 times iron in
   the pakset where history has them within 10%.
4. **Signals.** Decide what one signal object represents before any number is changed.

## Not established

- Permanent way cost for 1900-1930 and after 1945. Every post-1925 way ratio is against the 1898
  anchor held flat.
- Earthworks per km for a stated cross-section.
- Vault or viaduct cost by height, which the forum table does not separate.
- Any measured split of maintenance between rails, earthworks, bridges and tunnels.
- A signalling cost per route kilometre.

## Open questions

- Is the motorway at 2.5 times too cheap part of the same problem, or a separate calibration?
- Should the forge cost, which is £5,945 a kilometre at the track setting, be inside the way cost
  or separate from it? As it stands the two together exceed whole-line capital before any
  structure is built.
