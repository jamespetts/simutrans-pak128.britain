---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Multiple-working codes

**Covers**: the British railway multiple-working codes, the integer each is given in
`multiple_working_type`, the classes that carried each code, and the rules used to assign the field
to every rail vehicle in `New/`. The engine mechanics and the coupling rules are in
[multiple-working](multiple-working.md); the crew complements are in
[crew-complements](crew-complements.md).

## Engine meaning

`multiple_working_type` is an opaque equality label. `convoi_t::get_salaries` charges the leading
vehicle's drivers, and charges every other vehicle whose value differs from the leading vehicle's.
The value does not affect coupling, physics or the save format; it is in the descriptor checksum.
`[CODE simutrans-extended ex-15]`

The pakset therefore gives one integer to each real control system: every class that could work in
multiple with the others of that code shares the integer, and every class that could not has a
different integer or 0.

## The codes

### Locomotive codes

| No. | Code | System | Classes in the pakset |
|---:|---|---|---|
| 1 | blue star | electro-pneumatic | 15, 20, 24, 25, 26, 27, 30 (rebuilt to 31/1), 31/1, 33/0, 37, 40, 45 |
| 2 | red circle | electro-magnetic | 16, 21, 28, 29 |
| 3 | green circle | not stated | some 47s; the pakset gives the 47 no code (see below) |
| 4 | orange square | diesel-hydraulic, then re-used | 41, 50 |
| 5 | red diamond | not stated, then re-used | 17, 56, 58, LMS 10000 |
| 6 | white diamond | diesel-hydraulic | 42 |
| 7 | yellow triangle | diesel-hydraulic | 35 |

`[LITERATURE:https://en.wikipedia.org/wiki/Multiple_working]`, citing the *British Railways Diesel
Traction Manual for Enginemen* (BTC, 1962), p. 184.

Systems that carried no symbol:

| No. | System | Classes in the pakset |
|---:|---|---|
| 8 | Southern 27-wire | SR and BR(S) electric stock: 2-NOL, 2-HAL, 3-SUB, 4-LAV, 401, 404, 410, 414, 415, 419, 421, 423, 430, 442, 489, 202, 205, 73 |
| 14 | HST pair | Class 43 power cars |
| 15 | time-division multiplex | 86, 87, 89, 90, 91, push-pull 47, DBSO, DVT |
| 17 | AAR | 59, 66, 67, 68 (008-015), 69, 70, 73/9 |
| 18 | BSI | 33 modern EMU and DEMU classes (for example 313, 315, 317, 321, 350, 377, 390, 700) |
| 19 | Scharfenberg | 4 classes (for example 395, 397, 700) |

`[LITERATURE:https://en.wikipedia.org/wiki/Multiple_working]`

### Multiple-unit codes

The first-generation diesel multiple-unit codes are the best-documented set.

| No. | Code | System | Classes in the pakset |
|---:|---|---|---|
| 9 | blue square | EP control with relays; leading car signals, each car switches its own battery | most mechanical DMUs: 100-112, 114-124, 128, 130, 131; 113; 127 until 1969 |
| 10 | yellow diamond | direct battery control, no relays | Derby Lightweight (mechanical), Metro-Cammell Lightweight, 129 |
| 11 | red triangle | West Riding hydraulic Derby Lightweights; from 1969 Class 127 | 127 (from 1969) |
| 12 | orange star | hydraulic transmission with pneumatic throttle and an extra air pipe | 125 |
| 13 | white circle | relays, no through air pipe | 126 |

`[LITERATURE:https://railcar.co.uk/technology/controls/coupling-codes/]`
`[LITERATURE:https://railcar.co.uk/technology/the-basics/?page=page-02]`

### Post-1970 and individual codes

British Railways stopped publishing symbols, and each later design had its own control system.
The pakset therefore uses one integer per compatible family or class. The full list is in
`multiple_working_type` on the vehicles themselves; the grouping rule is:

- a builder family that shared a control system gets one integer (for example PEP 313/314/315/507,
  Mk3 EMU 317-322/769, Electrostar 375-379/387, Desiro 444/450, Aventra 345/701/710/720/730);
- a class with no documented compatibility gets its own integer (for example 323, 350, 390,
  395, 458, 185);
- a fixed formation gets one integer for its driving ends (APT, Eurostar, Blue Pullman, the GWR
  twin set).

The integers are 32-73. They are labels only; the order has no meaning.

## Assignment rules

1. A locomotive carries its class code if the class was fitted for multiple working; otherwise 0.
   Steam locomotives, and diesel or electric classes with no multiple working (09, 47, 52, 55, 57,
   62, 71, 81, 83, 85, and the LMS 10800, LNER EM1/EM2 and NER electrics), carry 0, so a
   double-header pays one driver per locomotive.
2. A multiple unit carries its code on every driving car, powered or a driving trailer, and on no
   intermediate motor car or trailer. Both ends of a unit therefore agree, and a two-unit formation
   pays one driver.
3. A railcar or single unit with no multiple working carries 0. Seven objects were set to 0:
   `ac-railbus`, `BR-139`, the three GWR railcars (`GWR-Gloucester-Railcar`,
   `GWR-Gloucester-Parcel-Railcar`, `GWR-ParkRoyal-Railcar`), `leyland-railbus` and
   `ner-tyne-petrol-electric-railcar`.
4. A vehicle whose class is uncertain between two codes takes the majority code; the conflict is
   recorded below.
5. Trams use 16, separate from every rail code. The 25 articulated tramcars that work in multiple
   carry it; every other tram carries 0.

## Codes requested but not found

The brief named **orange circle** and **green triangle**. No locomotive or multiple-unit table read
in this pass contains either. The documented symbols are:

- locomotives: blue star, red circle, green circle, orange square, red diamond, white diamond,
  yellow triangle;
- first-generation DMUs: blue square, yellow diamond, red triangle, orange star, white circle.

The nearest documented items to orange circle are orange square (locomotives) and orange star
(Class 125); the nearest to green triangle is yellow triangle (Class 35). The symbol **blue square**
is documented only as a diesel multiple-unit code, not as a Southern electric code.

The only occurrence of **orange circle** found in any source is a railway forum recollection
(RailUK Forums, 2010, https://www.railforums.co.uk/threads/a-peculiar-1st-gen-dmu-query.35740/),
which also places it among DMU markings. The documented DMU lists — the Railcar Association,
Wikipedia's table and the *British Railways Diesel Traction Manual* — give orange **star**
(Class 125) and white **circle** (Class 126), not orange circle. Without a primary source the
pakset does not use it.

Confirmed assignments for the examples in the brief: **Class 50 carries orange square (4)**, as
does Class 41; **red triangle is 11**, carried by Class 127 from 1969 (and, historically, by the
West Riding Derby Lightweights); **blue square is 9**, the standard first-generation DMU code.

`[UNVERIFIED]` The Southern 27-wire system is documented, but no source read assigns it a symbol.
The pakset names code 8 by the system and leaves the symbol question open.

## Evidence gaps

| Point | Status |
|---|---|
| Locomotive codes 1-7 | Verified against the 1962 manual table reproduced by Wikipedia |
| First-generation DMU codes 9-13 | Verified against railcar.co.uk and Wikipedia |
| Southern 27-wire system | System verified; symbol not |
| HST, TDM, AAR | Verified as systems; the class lists are from the same table |
| BSI and Scharfenberg | Coupler families verified; control compatibility is an estimate |
| Post-1970 families 32-43 | No published code; grouped by builder family and the pakset constraint graph |
| Single-class codes 44-71 and 73 | No published code; own-class assignment by inference |
| Class 47 | Wikipedia lists green circle for some 47s; a railway staff source says 47s were never fitted. The pakset gives 0 |
| Class 57 | Rebuilt from the 47; given 0 on the same evidence |
| Classes 17, 21, 31 | Each carried two codes; the pakset has one object each, so the majority code is used |
| Class 139 | Treated as not fitted; an estimate |

## Open questions

1. Did any Southern electric stock carry a symbol, and was it blue square? The *Live Rail* articles
   "SR EMU Control Systems" parts 1 and 2 would settle it.
2. Should Class 47 and 57 carry green circle? The sources conflict.
3. Should the post-1970 block be collapsed to a smaller number of family codes? The present 73
   integers distinguish more groups than any published source confirms.
4. Did Class 30 retain blue star after rebuilding to 31/1? The pakset assumes it did.
5. Were Class 33/0 and 33/1 both blue star? The pakset has one object and gives it blue star; 33/1
   also carried the Southern 27-wire system.
6. Are BSI and Scharfenberg couplers evidence of control compatibility, or only of mechanical
   coupling?
