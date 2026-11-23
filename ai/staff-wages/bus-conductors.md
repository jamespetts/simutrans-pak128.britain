---
status: draft
verified: New ex-15 working tree, 2026-11-23
---
# Bus and tram conductors

**Covers**: the `staff[6]` conductor declaration on road passenger vehicles and trams under
`New/bus/` and `New/trams/`, the legal and operating dates behind it, and the types that keep a
conductor after the general cut-off.

Parent doc: [crew-complements](crew-complements.md).

## The legal framework

- From 1 August 1931 a conductor was required on any stage carriage seating more than 20
  passengers, with an exemption for single-deck vehicles of 26 seats or fewer where no adult fare
  was under 6d. Regulation 14, Public Service Vehicle (Equipment and Use) Regulations.
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1931/jun/18/public-service-vehicles-conductors]`
- Before 1931 there was no statutory requirement. Horse omnibuses and motor omnibuses carried a
  conductor as operating practice; the smallest vehicles did not.
- From the early 1950s one-man operation was licensed for single-deck vehicles, first to 26 seats
  and later to 35 with a dispensation. London Transport's first one-man service ran from
  Leatherhead in March 1954 with three modified RF-class country buses, after the seating limit was
  raised to 26. `[LITERATURE:http://red-rf.com/the%20rf%20story/rejuvenation.aspx]`
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1958/apr/16/public-service-vehicles]`
- The 1968 Transport Act and the bus grant accelerated conversion: by the early 1970s one-man
  operation was the norm outside London. Deregulation in 1986 removed the remaining crew
  operation outside London.
- London ran later. The first central-area one-man routes were converted on 18 November 1964; the
  last crew single-deck route in April 1971; the executive's target was complete conversion by
  1978, but conversion stopped in the 1980s with 53 per cent of London's buses one-man operated in
  1984. Rear-platform Routemasters kept conductors until 2005.
  `[LITERATURE:https://archive.commercialmotor.com/article/30th-april-1971/22/full-o-m-o-by-1978-is-lt-target]`

## The rule applied

`driver[5]=1` on every bus. `staff[6]=1` when any of the following holds:

1. the class is a Routemaster or Routemaster derivative (rear-platform boarding);
2. it entered service before 1931 and seats more than 12;
3. it entered service in 1931-1967 and seats more than 26.

Otherwise the bus is driver only. Trams follow [the same idea](#trams).

The two thresholds encode the statute: 12 seats is the small-vehicle exemption, and 26 seats is the
licensed one-man limit of the 1950s. A bus of 21-26 seats from 1931-1967 is treated as one-man
operated; that is correct only where the minimum fare was 6d or more, which the data cannot show,
so those vehicles are the least certain group.

## Effect on the fleet

`[CODE New ex-15 working tree, 2026-11-23]` Of 343 bus objects, 238 declare a conductor. All 105
that do not are either 12 seats or fewer, 27 seats or more and introduced in 1968 or later, or
21-26 seats in 1931-1967.

The declarations are static: a bus whose modelled life spans the conversion carries one complement
for the whole of that life. The largest such errors are the 1950s and 1960s double-deckers, which
lose their conductors in reality some years before the pakset's retirement date.

## Trams

- Every powered tram car before 1984: `driver[5]=1` and one `staff[6]=1` for the set.
- 1984 and later: driver only, except Sheffield Supertram, which kept conductors, and Blackpool's
  Centenary cars, which were built for one-person operation in 1984.
- Tram engines and horses declare no crew. The driver and conductor are declared on the pre-1900
  tramcar they draw, because the driver sits in the car and a steam tram was permitted only one
  trailer. That car takes no multiple-working type, since it does not work in multiple.
  `[USER-DIRECTION:2026-11-23]`

## Sources

- Regulation 14 and the 1931 requirement: Hansard, HC Deb 18 June 1931 vol 253 c1923.
- One-man operation in London, with the 1954 Leatherhead trial and the 1964 and 1971 central-area
  conversions: "Rejuvenation", the RF story, red-rf.com.
- London Transport's 1978 target and the 1970 counts: *Commercial Motor*, 30 April 1971, p. 22.
- The 12-seat utility-vehicle relaxations and the 26- and 35-seat one-man limits: Hansard, HC Deb
  16 April 1958 vol 586 cc301-12.
- Driver-only operation of London buses to 1984: Transport Studies Unit, Oxford, TSU 287 (1985),
  cited in TRID record 00399634.

## Open questions

- Should a 21-26 seat bus of 1931-1967 carry a conductor? The statute allowed either, depending on
  the fare scale, which the pakset does not record.
- Should the London conversion dates be modelled by treating London-only body types separately
  (for example the RT and RF families) rather than by the national rule?
