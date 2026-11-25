---
status: draft
verified: New ex-15 @ fcd40c0bc (working tree)
date: 2026-11-25
---
# Research pass 56 - Gross tonnage for the 216 water objects, and what the three per-ton rates measure

Research pass for the Pak128.Britain-Ex cost balancing. Compiled 25 November 2026.
Files written: this report, `water-gross-tonnage.csv` and `research-pricing-rows-56.csv`.
No workbook, `.dat` file, `evidence_data.py`, `build_workbooks.py` or existing document was
changed.

The water class is the last vehicle class with no size ladder. The three rates that would give it
one - **84.1 x GT^0.90** for ferries, **GBP 35 a gross ton** for coastal cargo and **GBP 17 a gross
ton** for inland craft, all in 1900 money - need a gross tonnage for each object, and the pakset
records none. This pass supplies the tonnage by identifying the real vessel behind each pakset
object, or the type it represents, and reading the register figure for that vessel. The brief was
to record whether each figure is GRT or GT, its year and its source, and to leave it blank where
no tonnage can be found.

The pass found the tonnage it was sent for, for 39 vessels covering 57 of the 216 rows. It also
found something that changes the use of the three rates: **the three rates are capital prices per
gross ton, not annual repair costs.** The arithmetic is set out in §4.4 and it is exact for two of
the three. Applied as maintenance they would charge a ship's entire capital every year. The
recommendation in §5 therefore separates the two things the rates can do: size a hull (capital),
and - at 2 to 5 per cent of that capital - set its annual repair.

## 1. What this pass found

1. **Thirty-nine vessels now carry a sourced gross tonnage, covering 57 of the 216 rows.** Of the
   216 rows, 34 name a real vessel, 7 are mail holds of named vessels, 7 name a class and 168 are
   types. The 57 rows that carry a figure are the 34 named vessels, 7 class sisters and 16 type
   representatives. The other 159 are blank, and 152 of those are type rows: all 37 narrowboats,
   all 6 coasters, all 9 hovercraft, all 6 tugs and every generic steamer. Coverage by type:
   ferries 28 of 37 rows, cargo ships 11 of 21, river boats 6 of 24, barges 12 of 62, narrowboats
   0 of 37, coasters 0 of 6, hovercraft 0 of 9, tugs 0 of 9. **MEASURED (2 rows), STATED (54),
   DERIVED (1), UNAVAILABLE (159).**

2. **The pakset names more real ships than its object names suggest.** Many objects name the
   vessel outright (PS Comet, PS Chevalier, PS Madge Wildfire, PS Waverley, MV Balmoral,
   MV Lochfyne, TSS King Edward, TSS Queen Mary, RMS Columba, SECR Queen, SR-N4 Mountbatten,
   SR-N6 Winchester, HSC Our Lady, HSC Wight Ryder). Others are identified by the `.dat` comment,
   the intro year and the capacity together: `clan-line-steamer.dat` cites SS Clan Alpine (1942),
   `hsc-our-lady.dat` cites HSC Our Lady Pamela, and `secr-queen.dat` cites TSS The Queen. In all
   34 named-vessel rows the tonnage is the vessel's own. **CODE (`.dat` comments and object
   names), with the tonnage STATED from the vessel article.**

3. **One object is recorded by the pakset as unidentifiable.** `boats/clyde-steamer.dat` carries
   the comment "It is not clear which specific ship that this is supposed to represent, but the
   style suggests that it is a 20th century vessel." Its tonnage is blank because the pakset
   itself says the ship is unknown, not because the search failed. **CODE.**

4. **The three rates are capital prices per gross ton.** Three independent checks, each in 1900
   money on the `general` series in `New/config/prices.tab`:
   - **Ferries.** 149.7 x GT^0.90 is the measured **purchase price** fit of
     [report 25](research-pricing-report-25.md) (14 British passenger vessels, 1924-38, R2 0.992,
     nominal at the 1931 sample midpoint). Deflated at the general index 178 - between 1931 (180)
     and 1932 (176) - it is **84.06 x GT^0.90**. The stated repair rate is 84.1 x GT^0.90. The
     agreement is exact at every tonnage, and the exponent and the R2 are the capital fit's to
     three figures.
   - **Inland.** SB Cambria cost GBP 1,895 in 1906 for 109 gross tons (report 25, section 6).
     Deflated at the 1906 index of 102 that is GBP 1,858, or **GBP 17.04 a gross ton**. The stated
     inland rate is GBP 17 a gross ton.
   - **Coastal cargo.** The British Railways 1950-53 cargo ships cost GBP 148.6-173.3 a gross ton
     (report 25, section 3.3). Deflated at the 1951-53 indices of 391 and 440 that is
     **GBP 38.0-39.4 a gross ton**. The stated rate is GBP 35, 8 to 11 per cent below the range.
   The inland and ferry agreements are exact; the cargo agreement is close. **DERIVED from three
   measured prices and the `general` index.**

5. **Applied as maintenance, the ferry rate charges the whole hull every year.** At 500 GT the
   rate gives GBP 22,588 a year in 1900 money. The same 500 GT hull's measured 1931 capital,
   deflated to 1900 money, is GBP 22,588. The rate is 56 per cent of the nominal 1931 price at
   every size, and 56 per cent is the 1900-money deflator for 1931-32 (100 / 178 = 0.562). A rate
   that equals capital cannot be a repair cost. **DERIVED, arithmetic only.**

6. **The inland rate is impossible for a narrowboat.** A 22 GT narrowboat at GBP 17 a gross ton
   is GBP 374 a year. President, the 1909 Fellows Morton & Clayton steamer, cost GBP 600, which
   is GBP 583 in 1900 money at the 1909 index of 103: the rate would be 64 per cent of the boat's
   capital every year. The rate is coherent only for craft of roughly 100 gross tons and above,
   which is the size at which the Cambria price it was derived from sits. **DERIVED.**

7. **Gross tonnage is not proportional to capacity, and the ratio is set by route, not by size.**
   Across the 39 vessels the ratio of gross tonnage to one tonne of capacity (passengers at
   0.075 t each, or cargo tonnes) runs from **0.80 to 188.9**, a factor of 236. The bands are
   tight within a route class and very wide across classes: river and excursion steamers
   3.1-9.3; cargo ships 0.8-2.3; inland craft 0.9-1.5; cross-Channel and Irish Sea ferries
   27-45; modern ro-ro ferries and catamarans 78-189. **MEASURED inputs, DERIVED ratios.**

8. **A single power law fits the passenger fleet poorly.** Fitted on 32 distinct passenger
   vessels, gross tonnage = 14.49 x capacity^1.111, R2 0.47, median absolute error 80 per cent.
   The linear fit through the origin (gross tonnage = 41.9 x capacity) has R2 0.32. Neither is
   usable as a bridge. The same fit on the five cargo ships is much better: gross tonnage =
   3.00 x capacity^0.891, R2 0.891, and its median error is 28 per cent. **DERIVED.**

9. **The capital workbook's `weight` field is not a tonnage and cannot stand in for one.**
   `weight` is 29 for PS Comet against 28 tons burthen, but 3,000 for SS Great Eastern against
   18,915 gross tons and 15,000 for Spirit of Britain against 47,592. It is the engine's mass
   parameter, scaled for the vehicle's effect on the game, not a register figure. **CODE.**

10. **The evidence file that should hold the rates does not contain them.** At `fcd40c0bc`,
    [ship-maintenance](../vehicle-cost/ship-maintenance.md) ends at the heading "# B. Inland and
    canal boats" with no text under it, and its sea-going section (F1-F33) records no ferry
    maintenance fit. The three rates appear in [handoff](handoff.md) item 9 and in the brief for
    this pass. Their sample, scope and denominator are therefore unrecorded in the knowledge base,
    and the arithmetic in point 4 is the only check on them. **CODE (file read), UNAVAILABLE (the
    fit's own record).**

11. **Result.** The gross tonnage now exists for 57 rows and a defensible band exists for the
    inland and cargo types. The passenger fleet cannot be bridged on capacity alone because the
    pakset's `type` field does not record route class: a 450-passenger river steamer and a
    450-passenger ro-ro are both `ferry`. The three rates should be used as capital, with
    maintenance set at 2 to 5 per cent of the capital they imply.

## 2. Method

- **The rows.** The 216 rows are the `water-vehicles` class of
  `New/ai/cost-balancing/cost-inventory.csv`, joined to `water-capacity.csv` on the object name.
  The join is clean: 216 rows on each side, no unmatched names. `total_size_t` is the capacity
  column of `water-capacity.csv`, which is hull plus hold capacity in tonnes; for a passenger
  craft the capacity is the passenger count at **0.075 t a passenger**, which is the pakset's own
  passenger weight, and for a cargo craft it is the payload in tonnes. The same figure serves as
  the "capacity" of the fits in §4. `[CODE New ex-15 @ fcd40c0bc: cost-inventory.csv,
  water-capacity.csv]`
- **The `.dat` reading.** For each of the 97 source files the pass read `name`, `engine_type`,
  `freight`, `payload`, `speed`, `weight`, `length`, `intro_year` and every `#` comment. The
  comments are the pakset's own statement of identity where one exists.
  `[CODE New ex-15 @ fcd40c0bc: boats/]`
- **Identity.** Three bases, recorded in `identity_basis`:
  - **named** - the pakset object is a specific vessel, named in the object name or cited in a
    `.dat` comment, and the tonnage is that vessel's.
  - **class representative** - the object is one ship of a named class and the tonnage is a
    sister's; the class is named in `identity` and the sister is named in the source.
  - **type representative** - the object is a generic type and the tonnage belongs to a documented
    example of the type. The `identity` string says so in the form "type (representative:
    vessel, year)", and the `notes` column repeats it. **No type representative is presented as
    the object's own identity.**
- **Definitions of tonnage.** Three measures appear and are kept apart in
  `gross_tonnage_definition`:
  - **GRT** - gross register tonnage, the pre-1969 register measure: the enclosed volume of the
    ship in units of 100 cubic feet. It is a volume, not a weight.
  - **GT** - gross tonnage under the 1969 Convention, a dimensionless volume index defined by a
    formula on the same enclosed volume. It is not comparable with GRT ton for ton, but for the
    ships here the two differ by a few per cent.
  - **bm** - builder's old measurement, the pre-1836 capacity formula (length x beam x depth),
    which is what "tons burthen" means on a wooden or early iron hull. It is a capacity measure
    closer to cargo tonnage than to GRT, and it is flagged wherever it is used.
- **Grades.** MEASURED = the figure is cited to a register or an authority in the source.
  STATED = the figure is printed in a fleet table, article or infobox without the register
  behind it being visible. DERIVED = arithmetic here from a stated range, with the arithmetic
  shown. UNAVAILABLE = identified but not readable, or no vessel to identify. Definitions:
  [claim tags](../claim-tags.md).
- **1900 money.** Nominal x 100 / the `general` index of the year named, from
  `New/config/prices.tab`. The indices used: 1906 102; 1931 180; 1932 176; 1951 391; 1953 440.
  `[CODE New ex-15 @ fcd40c0bc: config/prices.tab]`
- **The `year` column.** It is the year of the tonnage figure - the vessel's build or register
  year - not the pakset intro year. The two differ where the pakset's date is wrong (Clan Alpine,
  introduced in the pakset in 1912 and built in 1942) and where a hull was re-measured
  (PS Premier, 1846 hull, 129 GRT after the 1878 rebuild).
- **The fits.** One point per **distinct vessel**, not per pakset row, because a hull with six
  cargo fits would otherwise count six times and weight the fit to whichever fit carries the
  most tonnes. Where a hull has several cargo fits the largest capacity is used, which is the
  hull's full-load capacity. Fits: linear through the origin (ordinary least squares on
  `GT = k x capacity`), and log-log (`GT = a x capacity^b`). R2 is reported both about the mean
  (the conventional R2) and about the origin for the through-origin fit, because the two differ
  and the through-origin one is the more favourable. Median absolute percentage error (MedAPE)
  is reported because it is robust to the largest ships.
- **No `.dat` price, workbook figure or existing target is used as evidence anywhere in this
  pass.** The `weight` field is used only in point 9 of §1, to show that it is not a tonnage.

## 3. Evidence table

Every gross tonnage used in this pass. The URL is the page read; all are English Wikipedia
articles, which for ships of this era reproduce the register in an infobox or a fleet table. The
grade is against the figure, not the page.

| Vessel | Year | Tonnage | Definition | Grade | Source (en.wikipedia.org/wiki/) |
|---|---|---:|---|---|---|
| Norfolk wherry *Albion* (type) | 1898 | 22.78 | GRT | STATED | Albion_(wherry) |
| PS *Comet* | 1812 | 28 | bm | STATED | PS_Comet |
| Thames sailing barge *Cambria* (type) | 1906 | 109 | GRT | STATED | SB_Cambria |
| PS *Premier* (as rebuilt) | 1878 | 129 | GRT | STATED | PS_Premier |
| MV *Loch Striven* (Loch class) | 1986 | 206 | GT | STATED | MV_Loch_Striven |
| PS *Madge Wildfire* | 1886 | 220 | GRT | STATED | Caledonian_Steam_Packet_Company |
| Brig (type, *HMS Beagle*) | 1820 | 235 | bm | STATED | HMS_Beagle |
| PS *Chevalier* (II) | 1866 | 292 | GRT | STATED | David_MacBrayne |
| HSC *Our Lady Pamela* | 1986 | 312 | GT | STATED | Our_Lady_Pamela |
| *FastCat Shanklin* | 1996 | 482 | GT | STATED | FastCat_Shanklin |
| TS *King Edward* | 1901 | 502 | GRT | STATED | TS_King_Edward |
| *Wight Ryder I* | 2009 | 520 | GT | STATED | Wight_Ryder_I |
| PS *Waverley* (1899) | 1899 | 537 | GT | MEASURED | PS_Waverley_(1899) |
| RMS *Columba* | 1878 | 543 | GRT | STATED | RMS_Columba |
| MV *Royal Iris of the Mersey* | 1959 | 611 | GT | STATED | MV_Royal_Iris_of_the_Mersey |
| MV *Balmoral* | 1949 | 736 | GRT | STATED | MV_Balmoral_(1949) |
| MV *Lochfyne* | 1931 | 754 | GRT | STATED | MV_Lochfyne |
| TS *Queen Mary* | 1933 | 871 | GRT | STATED | TS_Queen_Mary |
| Tea clipper *Cutty Sark* (type) | 1869 | 963 | GRT | STATED | Cutty_Sark |
| East Indiaman (type, midpoint) | c.1800 | 1,200 | bm | DERIVED | East_Indiaman |
| TSS *The Queen* | 1903 | 1,676 | GRT | STATED | TSS_The_Queen |
| SS *Great Western* | 1837 | 1,700 | GRT | STATED | SS_Great_Western |
| SS *Isle of Thanet* | 1925 | 2,701 | GRT | STATED | British_Railways_ships |
| HSC *Cat* (Incat 74 m, class) | 1990 | 3,003 | GT | STATED | Incat |
| Four-masted barque *Herzogin Cecilie* (type) | 1902 | 3,242 | GRT | STATED | Herzogin_Cecilie |
| TSS *Lord Warden* | 1951 | 3,333 | GRT | STATED | British_Railways_ships |
| SS *Great Britain* | 1843 | 3,443 | bm | STATED | SS_Great_Britain |
| MDV 1200 class (class) | 1996 | 3,971 | GT | STATED | MDV_1200-class_fast_ferry |
| SS *Invicta* | 1939 | 4,178 | GRT | STATED | SS_Invicta_(1939) |
| MV *Europic Ferry* | 1968 | 4,190 | GT | STATED | MS_Europic_Ferry |
| MV *Horsa* | 1972 | 5,590 | GT | STATED | British_Railways_ships |
| HSC *Manannan* (Incat 96 m, class) | 1998 | 5,743 | GT | STATED | HSC_Manannan |
| SS *Clan Alpine* | 1942 | 7,168 | GRT | STATED | SS_Clan_Alpine_(1942) |
| HSC *Express 1* (Incat 112 m, class) | 2009 | 10,503 | GT | STATED | Incat |
| SS *Great Eastern* | 1858 | 18,915 | GRT | STATED | SS_Great_Eastern |
| HSS 1500 | 1995 | 19,638 | GT | STATED | HSS_1500 |
| *Pride of Dover* | 1987 | 26,433 | GT | STATED | MS_Pride_of_Dover |
| *Pride of Burgundy* (class) | 1993 | 28,138 | GT | STATED | MS_Pride_of_Burgundy |
| *Spirit of Britain* | 2010 | 47,592 | GT | MEASURED | MS_Oscar_Wilde_(2010) |

Notes on the rows where the figure needs explanation:

- **PS Comet.** The article prints "Tonnage 28 ton" and describes a "28 ton burthen craft", so the
  measure is burthen, not GRT. It pre-dates the register.
- **PS Premier.** 129 GRT is the tonnage after the 1878 rebuild, the only figure the article
  states. The 1846 hull tonnage is not recorded there, so the figure is the same hull's later
  measure and is flagged in the CSV. `ps-premier-covered` is a cabin variant of the same hull;
  the `.dat` comment says Premier was never covered and cites the Gravesend ferry *Sir Walter
  Raleigh* of 1854 as the nearest covered type.
- **PS Chevalier.** The MacBrayne fleet table lists Chevalier (I) of 1853 at 329 GRT and
  Chevalier (II) of 1866 at 292 GRT. The pakset intro year of 1866 identifies the second.
- **PS Waverley (1899).** The infobox cites The National Archives merchant shipping movement
  record, "Gross Tonnage: 537". This is not the preserved 1947 *Waverley* (693 GRT).
- **SS Invicta.** The article text states 4,178 GRT and 1,982 NRT; the infobox gives 4,220. The
  text figure is used.
- **SS Isle of Thanet.** The British Railways ships table prints 2,701 GRT; the crew-complement
  register in this knowledge base records 2,664 from the Dover Ferry Photos pages. The
  difference is 1.4 per cent and does not affect any fit.
- **SS Clan Alpine.** The pakset intro year is 1912, which is earlier than the ship. The identity
  rests on the `.dat` comment, which cites this ship, not on the date; the CSV says so.
- **Pride of Dover, Spirit of Britain, Pride of Burgundy.** The pakset names (`POPride`,
  `POSpirit`, `POSuperEuropean*`) do not name the ship. The identification is by operator, year
  and size, and the CSV records it as named only where the year and size leave one candidate
  (Pride of Dover, 1987, 26,433 GT) and as a class where several ships share the year (the
  1991-93 P&O Dover freight ferries). Spirit of Britain is identified by name and is now the
  *Oscar Wilde*.
- **Incat, MDV 1200, Loch class, Pride of Burgundy.** Class representatives: the tonnage is a
  sister's, and the sister is named in the `identity` string.
- **Type representatives.** Albion, Cambria, HMS Beagle, Cutty Sark, the East Indiaman and
  Herzogin Cecilie are not pakset objects. They are the documented examples chosen for the
  Norfolk wherry, Thames sailing barge, brig, clipper, East Indiaman and windjammer types. The
  East Indiaman figure is the midpoint of the range the article states ("generally measuring
  between 1100 and 1400 tons burthen"), which is why it is the one DERIVED row.

## 4. The series

### 4.1 Coverage

| Group | Rows | Rows with a tonnage | Named | Class | Type |
|---|---:|---:|---:|---:|---:|
| Ferries (sea) | 37 | 28 | 21 | 7 | 0 |
| River boats (estuarine) | 24 | 6 | 6 | 0 | 0 |
| Cargo ships | 21 | 11 | 7 | 0 | 4 |
| Coasters | 6 | 0 | 0 | 0 | 0 |
| Barges | 62 | 12 | 0 | 0 | 12 |
| Narrowboats | 37 | 0 | 0 | 0 | 0 |
| Hovercraft | 9 | 0 | 0 | 0 | 0 |
| Tugs | 9 | 0 | 0 | 0 | 0 |
| Other (fishing, skiffs) | 11 | 0 | 0 | 0 | 0 |
| Holds | 9 | 0 | 0 | 0 | 0 |
| **Total** | **216** | **57** | **34** | **7** | **16** |

The 57 rows are 26 per cent of the class. They are concentrated in the sea-going passenger fleet,
which is where the ferry rate's own sample lies.

### 4.2 Gross tonnage against capacity

One point per distinct vessel; capacity is `total_size_t` from `water-capacity.csv`. The ratio is
gross tons per tonne of capacity.

| Band | n | Ratio: min | median | max | Reading |
|---|---:|---:|---:|---:|---|
| River and excursion steamers (`river-boat`) | 5 | 3.11 | 6.24 | 9.33 | Tight. A 983-passenger excursion steamer is 3.1 GT a capacity tonne; a 40-passenger paddle steamer is 9.3. |
| Cargo ships (sailing and steam) | 5 | 0.80 | 1.63 | 2.26 | Tight enough to bridge. The largest, a 9,000 t Clan liner, is the lowest ratio. |
| Inland craft (wherry, sailing barge) | 2 | 0.91 | 1.18 | 1.45 | Two points only; a ratio, not a fit. |
| Ferries, pre-1960 | 13 | 3.65 | 27.28 | 137.10 | Very wide: Clyde ferries 3.8-16, cross-Channel 27-45, ocean liners 66-137. |
| Ferries, 1960 onward | 14 | 4.40 | 55.70 | 188.86 | Very wide: small catamarans 4-28, large ro-ro 78-189. |

The pre-1960 ferry band splits cleanly once the three Brunel ocean liners are removed: ten
Clyde, Mersey and cross-Channel ferries run from 3.65 to 45.27 with a median of 13.1. The three
liners (1,700-18,915 GT) are a different population and should not be pooled with ferries.

### 4.3 The fits

**Passenger, 32 distinct vessels.** Capacity alone does not explain gross tonnage:

```
GT = 14.49 x capacity^1.111          n = 32   R2 = 0.474   MedAPE = 80%
GT = 41.9 x capacity                 n = 32   R2 = 0.317 (centred)
                                     MedAPE = 195%
```

The exponent above 1 says gross tonnage grows faster than passenger count, which is the vehicle
deck and the amenity, not the passengers. The worst residuals, in log space:

| Vessel | Ratio | Error | Why |
|---|---:|---:|---|
| HSS 1500 | 181.8 | -87% | 1,500 passengers and a large car deck in 19,638 GT |
| SS *Great Western* | 137.1 | -86% | 148 passengers in a 1,700 GT ocean hull with a 12 t capacity figure |
| *Spirit of Britain* | 188.9 | -86% | 2,000 passengers and 89.6 t of vehicles in 47,592 GT |
| HSC *Express 1* | 121.4 | -80% | 1,200 passengers in a 112 m catamaran |
| HSC *Cat* | 92.4 | -77% | 450 passengers in a 3,003 GT catamaran |
| *Pride of Dover* | 105.8 | -75% | 2,290 passengers and 90 t of vehicles in 26,433 GT |

Every large residual is a ship whose gross tonnage is mostly vehicle deck or cabin space, which
the pakset capacity does not count, and every one of them is an under-prediction: the fitted line
gives them a quarter to a seventh of their real tonnage. That is the structural reason a single
bridge cannot work for passengers.

**Cargo, 5 distinct ships.**

```
GT = 3.00 x capacity^0.891           n = 5    R2 = 0.891   MedAPE = 28%
GT = 0.84 x capacity                 n = 5    R2 = 0.843 (centred)
```

The through-origin fit gives 0.84 because it is dominated by the largest observation (the 9,000 t
Clan liner at 0.80); the median ratio is 1.63. The disagreement between 0.84 and 1.63 is itself
the finding: gross tonnage is not proportional to cargo tonnage across the sailing-to-steam
transition, so a ratio is safer than a slope. **Use 1.6, band 0.8-2.3.**

**Inland, 2 distinct craft.** No fit is possible. The two points give 0.91 (Albion, 22.78 GRT
against 25 t) and 1.45 (Cambria, 109 GRT against 75 t). The ratio 1.2 is the midpoint and the
band is 0.9-1.5.

**The reason the ratio rises with ship size in the passenger fleet** is worth stating plainly,
because it is what the workbook has to encode: a passenger is 0.075 t of payload, while the ship
around him is 3 to 190 gross tons. The multiplier is the amount of ship per passenger, and that
is set by the route: an excursion steamer packs passengers on decks, a cross-Channel ferry gives
each one a cabin and a share of a vehicle deck, and a modern ro-ro gives each one a share of two
vehicle decks and a shopping mall.

### 4.4 What the three rates measure

| Rate as stated | What it equals | Arithmetic | Grade |
|---|---|---|---|
| Ferries 84.1 x GT^0.90 | The report 25 purchase-price fit, deflated to 1900 money | 149.7 x GT^0.90 x 100 / 178 = 84.06 x GT^0.90 | DERIVED, exact |
| Coastal cargo GBP 35/GT | The BR 1950-53 cargo price per gross ton, deflated | 148.6-173.3 x 100 / 391-440 = 38.0-39.4 | DERIVED, within 11% |
| Inland GBP 17/GT | The 1906 Cambria price per gross ton, deflated | 1,895 x 100 / 102 / 109 = 17.04 | DERIVED, exact |

The ferry agreement is not approximate. At 100, 500, 2,000 and 10,000 gross tons the ratio of the
deflated capital fit to the stated rate is 1.000, because both are the same power law with a
constant factor. The exponent (0.90) and the R2 (0.992) are also the capital fit's. The
alternative reading - that a repair-cost regression on the same 14 hulls happened to reproduce the
capital fit's exponent and R2 to three figures and its coefficient to 0.05 per cent - requires a
coincidence that the evidence does not support.

What the rates would charge if they were treated as annual maintenance, at four tonnages:

| Gross tons | Ferry rate, GBP a year (1900 money) | Same hull's capital (1900 money) | Rate as % of capital | 2% of capital |
|---:|---:|---:|---:|---:|
| 100 | 5,306 | 5,306 | 100% | 106 |
| 500 | 22,588 | 22,588 | 100% | 452 |
| 2,000 | 78,654 | 78,655 | 100% | 1,573 |
| 10,000 | 334,808 | 334,813 | 100% | 6,696 |

The measured per-gross-ton repair figures in report 25 section 8 (the 1913 liner at GBP 0.60 a
gross ton a year; the 1862 sheathing at GBP 0.24-0.30; the 2003 bulker at US$5.61 a deadweight
ton) sit two to three orders of magnitude below the stated rate. At 500 GT they imply GBP 120-300
a year, which is 0.5-1.3 per cent of the hull's capital - the same order as the workbook's 2 to 5
per cent rule, and not the same order as GBP 22,588.

The inland rate fails the same test at the small end. A 22 GT narrowboat at GBP 17/GT is GBP 374
a year against President's GBP 583 capital; a Thames sailing barge at 109 GT is GBP 1,853 a year,
which is the Cambria's whole capital. The rate is a capital price per ton for a barge of about
100 tons, and it cannot be applied to a 22-ton canal boat as maintenance, or as capital, without
producing a figure above the boat's own price.

## 5. Recommended treatment for the 216 objects

1. **Use the tonnage that exists before any bridge.** The 57 rows in
   `water-gross-tonnage.csv` carry a figure with a source and a grade. Nothing in this pass
   replaces them with a fitted value. The 34 named rows are the strongest: a named ship's own
   register figure needs no bridge at all.

2. **Bridge the homogeneous groups only, and state the band.** The bridge is a ratio, not a power
   law, and it is used only where the group's spread is small enough to price with:
   - **Inland cargo craft** (87 blank rows: narrowboats, barges, box boats, tub boats, flyboats,
     market boats, packet barges, dumb barges): **gross tonnage = 1.2 x capacity tonnes**, band
     0.9-1.5, n = 2. This is the weakest bridge in the pass and should be labelled ESTIMATE in
     the basis text. It rests on Albion (22.78 GRT against 25 t) and Cambria (109 GRT against
     75 t).
   - **River and excursion steamers** (18 blank rows of type `river-boat`): **gross tonnage =
     6.2 x capacity tonnes**, band 3.1-9.3, n = 5. Tighter than the inland pair and better
     supported.
   - **Cargo ships** (10 blank rows of type `cargo`, plus the six coasters): **gross tonnage =
     1.6 x cargo tonnes**, band 0.8-2.3, n = 5.
   - **Do not bridge generic ferries.** The six generic ferry rows span 1853 to 2007
     (Channel paddle steamer 1853, Channel screw steamship 1886, Tyne ferry 1940, Island 1973,
     Hydrocat 1991, Super-Loch 2007) and the band they would draw on is 4.4-188.9. A bridge there
     would be a guess dressed as a measurement.
   - **Do not bridge tugs, hovercraft, holds or fishing craft.** See point 5.

3. **Use the three rates as the capital per gross ton they are, not as maintenance.** If the
   workbook keeps a capital ladder for water, these are it: ferries 84.1 x GT^0.90, coastal cargo
   GBP 35/GT, inland GBP 17/GT, all in 1900 money. The flat GBP 38,958 ship ladder - the single
   capital anchor the capital workbook carries for every water object, at 1909 - is then replaced
   by a size ladder, which is the thing it has never had. The exact field is the capital target
   for the object; the rate names the group, and the group must be assigned by route (see
   point 2), not by the pakset's `type` field alone.

4. **Set maintenance at 2 to 5 per cent of that capital.** That gives, in 1900 money:
   - ferries **1.7 to 4.2 x GT^0.90** a year;
   - coastal cargo **GBP 0.70 to 1.75 a gross ton** a year;
   - inland **GBP 0.34 to 0.85 a gross ton** a year.
   Those bands bracket the measured per-ton repair figures in report 25 section 8 (GBP 0.24-0.60
   a gross ton a year for 1862-1913) and the workbook's existing 2 to 5 per cent rule, so the
   maintenance side needs no new measurement - it needs the capital side to be right. If the user
   confirms that the three rates were always intended as maintenance, they must be divided by
   about 20 to 50 before use, and the capital ladder has to come from somewhere else.

5. **Leave these blank, and say why in the basis text.**
   - **Hovercraft (9 rows).** An air-cushion vehicle is not a registered ship and has no gross
     register tonnage; its size is length and light displacement. The three rates cannot reach
     it. The AP1-88, BHT-130/150, SR.N4 and SR.N6 need their own treatment.
   - **Holds (9 rows).** A hold is a container inside a vehicle. The tonnage belongs to the parent
     and is on the parent's row; repeating it would charge the same hull twice. The parent and
     its tonnage are named in each hold's `notes`.
   - **Tugs (6 rows).** The pass found no British tug with a published tonnage and price that
     would fix a type figure; report 25 records the same gap for prices. A harbour tug of 150-250
     GT is the standing assumption recorded there and is not used here.
   - **Fishing craft and skiffs (11 rows of type `other`).** The Dogger, Fifie, seine netters and
     skiff wherries are open or small-decked boats; no register figure was found and the rates
     are not designed for them.
   - **PS Industry (3 rows).** The 1814 hull could not be matched to a verifiable vessel.
   - **ClydeSteamer.** The `.dat` says the ship is unknown.

6. **What the three rates still cannot do.** They cannot separate a Clyde excursion steamer from
   a cross-Channel ferry of the same passenger count, because the pakset records the count and
   not the route. A river steamer and a cross-Channel ferry carrying the same 450 passengers
   (6.2 and 27 gross tons a capacity tonne respectively) differ by 4.4 times in capital and
   therefore in maintenance. Until the pakset records a route class, the ferry band should be
   assigned by the object's name and era where that is possible, and the generic ferry rows should
   keep a stated central value with a wide band rather than a false precision.

## 6. Error bars

| Quantity | Central | Band | Why |
|---|---|---|---|
| Gross tonnage, named vessel (34 rows) | the register figure | +/- 2% | register figures; the widest known disagreement in the set is Isle of Thanet at 1.4% |
| Gross tonnage, class representative (7 rows) | sister's figure | +/- 10% | sisters of one class differ by fitting-out |
| Gross tonnage, type representative (16 rows) | the example's figure | -40% / +100% | the type's own size range; the East Indiaman range alone is 1,100-1,400 bm |
| GT per capacity tonne, river boat | 6.2 | 3.1-9.3 | n = 5 |
| GT per capacity tonne, cargo ship | 1.6 | 0.8-2.3 | n = 5 |
| GT per capacity tonne, inland craft | 1.2 | 0.9-1.5 | n = 2 |
| GT per capacity tonne, ferry pre-1960 | 13.1 | 3.7-45.3 | n = 10, the three Brunel liners excluded |
| GT per capacity tonne, ferry 1960+ | 55.7 | 4.4-188.9 | n = 14 |
| The three rates as capital | as stated | ferry exact; cargo +8 to +11%; inland exact | §4.4 |
| The three rates as maintenance | not supported | 1/50 to 1/20 of the stated figure | §4.4 |

**Structural assumptions.** (i) The pakset capacity is a payload measure - passengers at 0.075 t
and cargo in tonnes - so the bridge is between payload and enclosed volume, two different things;
the ratio is therefore a type constant, not a physical law. (ii) The named vessels are mostly
preserved or famous ships, which biases the sample towards survivors and towards the well
documented: the LMS, LNER and MacBrayne fleets are over-represented against the ordinary coaster.
(iii) The 1931-38 capital fit that the ferry rate reproduces covers 14 passenger vessels of
38-2,910 GT; below 200 GT it is an extrapolation, and the smallest bridge users (the river
steamers) sit below it. (iv) The cargo ratio rests on five ships, three of them sailing vessels;
no British motor coaster with a published GT and price was found. (v) The inland ratio rests on
two craft, both sailing barges; no narrowboat's register tonnage was found at all.

## 7. Gaps and routes

In order of value, with the exact route to each.

1. **The fit behind the three rates.** The rates are in [handoff](handoff.md) item 9 and were
   supplied with this pass's brief, but [ship-maintenance](../vehicle-cost/ship-maintenance.md)
   ends at the heading "# B. Inland and canal boats" with no text, and its sea-going section has
   no ferry fit. Route: the pass that produced the 84.1 coefficient should record the 14 vessels,
   the repair figures and the year of the fit in `New/ai/vehicle-cost/ship-maintenance.md`
   section B (or a new subsection under A). Until that is written, the arithmetic in §4.4 is the
   only check on the coefficient, and it says the figure is capital. **UNAVAILABLE.**

2. **Register tonnage for the inland fleet.** The pass could not find a single narrowboat's gross
   register tonnage. The route is the National Historic Ships UK register, which was read for
   President (registration 55) and prints dimensions but **not** tonnage; the Canal & River Trust
   and the Historic Narrow Boat Club hold the carrying fleet's gauging sheets, which record
   tonnage by canal. The Waterways Archive at Ellesmere Port holds the Grand Union Canal Carrying
   Company boat registers. A sample of gauging sheets would replace the 1.2 ratio for the 87
   inland rows. **UNAVAILABLE.**

3. **A modern handysize bulker's gross tonnage.** The seven `Handysize*` rows carry 20,000 t of
   cargo each and are the largest cargo type in the pakset. A 20,000 dwt handysize is of the order
   of 12,000 GT, but no single vessel with a published register figure was adopted, and the
   GT-to-deadweight ratio of a modern bulker (about 0.6) is far below the sailing and steam cargo
   ships in the sample, so the 1.6 ratio must not be carried to it. Route: a classification
   society particulars page or an Equasis record for a named 20,000 dwt bulker. **UNAVAILABLE.**

4. **A British motor coaster, 1950-80.** The cargo ratio has no twentieth-century motor ship in
   it. Route: the *Motor Ship* or *Fairplay* vessel particulars for a named British coaster of
   500-1,500 GT, or a port authority register. **UNAVAILABLE.**

5. **Tug tonnage.** Six tug rows have no figure. Route: the Gamecock and Watkins fleet lists,
   which report 90-479 GT for London tugs (report 25 section 7), give tonnage without price; a
   single named tug with both would fix the type. **UNAVAILABLE.**

6. **The generic steamer rows.** Thirteen river-boat rows have no named vessel (Iron, Wooden,
   Steel and Large steel paddle and river steamers; the three PS Industry fits; ClydeSteamer;
   the three Thames river buses) and six ferry rows have none (the two Channel steamers, the Tyne
   ferry, Island, the Hydrocat and Super-Loch). Route: the `.dat` comments already cite the Tyne
   ferries page and the Canal Museum; for the Channel steamers the South Eastern Railway fleet
   lists would name the class the pakset's 1853 `ChannelPaddleSteamer` represents. **UNAVAILABLE.**

7. **What a positive result would change.** Item 1 decides whether the three rates are capital or
   maintenance, and therefore whether the workbook needs one ladder or two. Items 2-6 widen the
   bridge from 57 rows to most of the 216. Neither changes the finding that the passenger fleet
   needs a route class before it can be priced by gross tonnage.
