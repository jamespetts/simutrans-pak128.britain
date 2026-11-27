---
status: draft
verified: New ex-15 @ f60346f99 (working tree), 2026-11-27
---
# Stop waiting comfort: evidence

**Covers**: the evidence behind the values in [stop-waiting](stop-waiting.md): the historical and
modern facility ladders, the maximum-tolerance evidence for terminals, airports, coaching inns and
harbours, the perception research, and the capacity sources. It records what is measured, what is
inferred and what is an estimate. Parent: [stop-waiting](stop-waiting.md).

## 1. Comfortable values

### Historical facility ladder

The historical evidence is a ladder of complaints and provisions, not a measured distribution:

- An hour in a heated waiting room was unremarkable; an hour with no waiting room, or in a
  refreshment room, was a grievance; 1.5-2 hours in a cold booking hall was a public complaint;
  several hours was endured only under duress.
  `[LITERATURE:https://api.parliament.uk/historic-hansard/lords/1889/mar/26/second-reading]`
  `[LITERATURE:https://api.parliament.uk/historic-hansard/lords/1890/mar/24/second-reading]`
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1940/jun/26/troops-accommodation-railway-termini]`
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1957/oct/31/railway-stations-manchester]`
- The Board of Trade required shelter on every platform, conveniences where necessary, and
  nameboards, and only for new railways. Provision therefore froze at each station's build date.
  `[LITERATURE:https://www.railwaysarchive.co.uk/documents/BoT_Requirements1902.pdf]`
- Waiting rooms spread slowly. The Liverpool & Manchester had no waiting room; the Stockton &
  Darlington spent £83 19s 11d on one in 1836 and rented a room at the Mason's Arms, Shildon, for
  £6 a year including fire and cleaning in 1837. Third-class rooms were normal at staffed stations
  by about 1870 and near-universal by 1900; halts never had them.
  `[LITERATURE:https://rchs.org.uk/wp-content/uploads/2023/09/Railway-Passenger-Stations.pdf]`
- Dated rooms: Halifax 1855 had four class- and sex-separated waiting rooms of 29-41 m2; Hampstead
  Heath's 1892 hall was 160 m2 and held 600 people at crush density; Ilkeston had seven seats for a
  town of 7,000. These support the 30-45 minute comfortable values for enclosed rooms and the
  60-75 minute values for great termini.
  `[LITERATURE:https://manchestervictorianarchitects.org.uk/buildings/halifax-railway-station-horton-street-halifax]`
  `[LITERATURE:https://rchs.org.uk/wp-content/uploads/2023/09/Railway-Passenger-Stations.pdf]`
  `[LITERATURE:https://www.oldilkeston.co.uk/16718-2/]`

The resulting ladder is: nameboard only 10; roof only 18; enclosed unheated 30; enclosed heated
40-45; large hall with refreshment 60; great terminus 60-75; coaching inn 75-90. The modern
standards below use the same ladder for the modern buildings.

### Modern standards

- Network Rail, *Station Capacity Planning* (NR/GN/CIV/100/03, 2023) gives 1.0 m2 per person in a
  concourse and 0.93 m2 on a platform at normal operation, falling to 0.45 and 0.28 m2 under
  disruption. These are the density basis for `comfort_capacity`, not for the time values.
  `[LITERATURE:https://www.networkrail.co.uk/wp-content/uploads/2023/12/NR-GN-CIV-100-03-Station-Capacity-Planning-guidance.pdf]`
- Network Rail, *Station Facilities & Amenities* (NR/GN/CIV/200/03, 2022) requires shelters on all
  platforms, waiting rooms where passengers dwell, seating for 10% of peak waiting passengers, and
  150 lux in waiting areas. It gives no maximum waiting time.
  `[LITERATURE:https://www.networkrail.co.uk/wp-content/uploads/2022/03/NR_GN_CIV_200_03-Station-Facilities-Amenities.pdf]`
- DfT and Transport Scotland, *Design Standards for Accessible Railway Stations* (2015), requires a
  seating area with a wheelchair space on every platform; it sets no time limit.
- TRB, "Functional Design Elements for Ferry Terminals", *Transportation Research Record* 817
  (1981), states that 15 minutes "appears to be a tolerable maximum" standing time and that seating
  should rise with the sailing interval. This is a standing tolerance, not a total waiting limit.
  `[LITERATURE:https://onlinepubs.trb.org/Onlinepubs/trr/1981/817/817-005.pdf]`
- IATA's Airport Development Reference Manual and BAA practice size holdrooms at 1.0-1.5 m2 per
  seated passenger and 50-60% seated; they publish no maximum waiting time.
  `[LITERATURE:https://www.flypgd.com/wp-content/uploads/2023/05/PGD-Terminal-Planning-Study_9-13-22-RFS1-Black-Back.pdf]`
- TfL and local authority bus-stop guidance provides shelters above about 10-20 boardings a day and
  sizes them at 0.4 m2 per passenger in the busiest hour. There is no national bus-stop standard.
  `[LITERATURE:https://content.tfl.gov.uk/bus-stop-design-guidance.pdf]`
  `[LITERATURE:https://www.gloucestershire.gov.uk/media/f31gshed/appendix-e-bus-stop-design-specification.pdf]`

### Perception evidence

- Fan, Guthrie and Levinson (2016) measured 702 waits at Minneapolis-St Paul bus stops and rail
  stations. Mean reported wait was 6.80 minutes against 5.64 measured, a ratio of 1.21; the ratio
  falls with wait length. A no-amenity stop predicts 5 minutes perceived as 10, 10 as 15, 15 as 20.
  Shelter and a bench together are worth 2-3 minutes on a 5-15 minute wait. Perceived insecurity
  (women, 10-minute wait) inflates the wait to 17 minutes.
  `[LITERATURE:https://conservancy.umn.edu/server/api/core/bitstreams/8c4f1ae0-d334-48d6-a515-765b30b3eeb1/content]`
- Mishalani, McCord and Wirtz (2006) fit `perceived = 1.33 + 0.92 x actual`; the bias is a fixed
  overhead of about one minute, not a constant multiplier.
  `[LITERATURE:https://digitalcommons.usf.edu/jpt/vol9/iss2/5/]`
- Arhin et al. (2019) surveyed 3,387 passengers at 71 District of Columbia bus stops. The mean
  stated maximum excess wait beyond the scheduled arrival was 7.0 minutes in the morning peak,
  10.5 midday and 7.5 in the evening peak; most answers were 5-15 minutes, and the maximum accepted
  by anyone was 20 minutes. A bench raised the stated acceptable wait from 7.5 to 9.0 minutes.
  `[LITERATURE:https://doi.org/10.4236/ojce.2019.94019]`
- The generalised-cost weight of waiting is 1.5-2.5 minutes of in-vehicle time per minute, above
  the engine's 1.0 below the comfortable limit. This is a pakset-wide issue and is not fixed by the
  stop values.

## 2. Maximum tolerated values

### Railway terminals

- Typical planned dwell at 19 Network Rail managed stations is 19 minutes; St Pancras is 24
  minutes. The 90th percentile is estimated at 40-60 minutes for domestic long-distance travel.
  These are normal waits, not the hard limit.
  `[LITERATURE:https://property.networkrail.co.uk/news-help-and-insights/news/the-best-place-in-the-uk-to-rent-retail-space/]`
- DfT, *Rail Passenger Experience of Disruption Handling* (2021), surveyed 1,049 passengers at 11
  stations. Of those who would stay and wait, the average longest wait for updates was 45 minutes;
  37% said 31-60 minutes and 8% said more than 60 minutes. Only 5% would abandon a severely
  disrupted journey. This is a stated maximum for an unplanned disruption and anchors the
  comfortable value, not the absolute hard limit.
  `[LITERATURE:https://assets.publishing.service.gov.uk/media/60b89536e90e0743a210ddda/passenger-experience-of-disruption-handling-report.pdf]`
- On 27 December 2014, several hundred passengers queued outside Finsbury Park for two to three
  hours; at Paddington the wait reached about five hours 45 minutes. At Carlisle in April 2022
  passengers slept on the station floor. In 1940, passengers at Liverpool Street and King's Cross
  waited four to six hours and slept on platforms and waiting-room floors. These are the upper-tail
  observations behind the 480-720 minute values for large main-line stations.
  `[LITERATURE:https://www.orr.gov.uk/sites/default/files/om/investigation-report-2015-02-12.pdf]`
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1940/jun/26/troops-accommodation-railway-termini]`

### Airports

- Measured planned terminal dwell is 80-100 minutes: median total time 80 minutes across 89 US
  airports; mean arrival 91-145 minutes before departure. Modern holdroom occupancy is 30-45
  minutes, with a 90th percentile near 75-90 minutes.
  `[LITERATURE:https://www.caa.co.uk/publication/download/15054]`
  `[LITERATURE:https://bibliotekanauki.pl/articles/393495.pdf]`
- CAA, *Passenger experiences during flight disruption* (CAP 1258, 2015): mean wait 4 hours after a
  delay, 13 hours after a cancellation; 23% of cancelled passengers waited 12-24 hours and 23% more
  than 24 hours or did not travel. Only 2% of delayed passengers took a refund; 21% of cancelled
  passengers did.
  `[LITERATURE:https://www.caa.co.uk/publication/download/15054]`
- The Heathrow Winter Resilience Enquiry (2011) records 9,500 passengers sleeping in the terminals
  on 18 December 2010, 5,600 the next night, and many refusing hotel rooms to keep their place in
  the queue.
  `[LITERATURE:https://im.ft-static.com/content/images/89937494-55ed-11e0-8de9-00144feab49a.pdf]`
- EU/UK 261 gives a refund right after a five-hour delay, but almost nobody uses it. The legal right
  is not the behavioural refusal point.

### Coaching inns

- The inn was a hotel and booking office as well as a waiting room. Emily Shore's 1836 journey from
  London to Salisbury arrived at 6.30 p.m. and left at 5 a.m., an overnight dwell of about 10.5
  hours. James Woodforde's coach reached Cirencester at about 5 p.m. and left about 6 a.m., 13
  hours. A 1751 Edinburgh coach spent 36 hours at one inn over a Sunday. A missed daily coach cost
  24 hours.
  `[LITERATURE:https://archive.org/details/journalemilysho00shorgoog]`
  `[LITERATURE:https://www.campop.geog.cam.ac.uk/research/projects/transport/travellerstales/woodforde.pdf]`
  `[LITERATURE:https://archive.org/details/stagecoachmailin01harp]`

### Harbours

- Sailing packets waited for wind and tide. Edward Watson records 18 days at Holyhead in 1821 on
  which the weather prevented any packet sailing; the packets sailed at high water, so departure
  times moved with the tide. Passengers waited in "different and distant inns" and were collected
  when the mail arrived; the waiting building served the last hours before embarkation.
  `[LITERATURE:https://archive.org/details/royalmailtoirela00watsiala]`
- The Neston House of Correction records, 1750-1800, show that "a month's wait was not uncommon",
  with an eight-week delay in 1775 and a 65-day maximum in 1757. These waits were spent ashore, not
  in the harbour waiting room. The building values therefore stop at 24 hours for the old harbour
  and fall to 15 hours for the modern terminal.
  `[LITERATURE:https://livrepository.liverpool.ac.uk/3175875/1/303317.pdf]`
- Modern ferry regulation (EU 1177/2010) triggers care at a 90-minute delay and accommodation for an
  overnight delay; the Isle of Man Steam Packet charter provides a hot meal at eight hours. These
  are operator obligations, not refusal points.
  `[LITERATURE:https://www.legislation.gov.uk/eur/2010/1177/article/17]`

### Ordinary stops and waiting rooms

- The historical extreme cases are a three-hour open-air wait in 1860 and four-to-six-hour and
  overnight waits at the 1940 London termini. The 1957 Manchester London Road complaint was about
  1.5-2 hours in a cold booking hall. These support the 240-minute open-platform, 360-minute
  unheated-room and 720-minute heated-room maxima.
  `[LITERATURE:https://eprints.lancs.ac.uk/id/eprint/163191/1/Spotlight_on_the_Traveller_final_accepted.pdf]`
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1957/oct/31/railway-stations-manchester]`
- The Underground buildings are metro buildings with frequent trains; their 120-minute maximum is a
  transport-frequency judgement, not a main-line terminal value.

## 3. Comfort capacity

- The capacity values are `round_to_5(k x station capacity)`. The factors come from the waiting-area
  research: 0.4 for a shelter, 0.45-0.60 for a platform or through-station building, 0.70-0.78 for a
  harbour, 0.95-1.0 for a terminal or airport holdroom, and 0.20 for an entrance building.
- The density basis is 0.93-1.0 m2 per person (Network Rail and TfL); historic bench-lined rooms
  seated 50-75 per 100 people, modern rail seats 10 per 100, ferry terminals 20-40% at a 15-20
  minute headway, and airport holdrooms 50-70%.
- A through-station waiting room covers about half of station capacity; a terminal concourse covers
  all of it. The pakset's station capacities are partly guessed, so the factors are more defensible
  than the absolute numbers.

## 4. Confidence and gaps

- **High**: the modern density and seating standards; the capacity factors for shelters, platforms
  and stations; the open-platform, roof and unheated-room physical evidence.
- **Medium**: the historical facility ladder; the airport and coaching-inn values; the main-line
  station maxima; the harbour values.
- **Low**: the 1909-1949 airport maximum; the old harbour maximum; the 24-hour greatest-terminus
  option; the exact upper tail at ordinary stops.
- **No measured distribution** of British waiting-room areas by station class, or of passenger
  refusal points at stops, was found. The values are estimates built from the evidence above.
- The engine's expected wait is half the service interval, and actual passengers are discarded above
  the tolerable value. A daily service can produce a 1,440-minute actual wait; the values are human
  maxima, not service floors.

## 5. Sources

- Board of Trade, *Requirements of the Board of Trade in regard to the Opening of Railways*, 1892,
  annotated for the 1902 issue.
  `[LITERATURE:https://www.railwaysarchive.co.uk/documents/BoT_Requirements1902.pdf]`
- Hansard, HL Deb 26 March 1889, vol. 334, cols 814-25.
  `[LITERATURE:https://api.parliament.uk/historic-hansard/lords/1889/mar/26/second-reading]`
- Hansard, HL Deb 24 March 1890, vol. 342, cols 1642-63.
  `[LITERATURE:https://api.parliament.uk/historic-hansard/lords/1890/mar/24/second-reading]`
- Hansard, HC Deb 26 June 1940, vol. 362, cols 533-64.
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1940/jun/26/troops-accommodation-railway-termini]`
- Hansard, HC Deb 31 October 1957, "Railway Stations, Manchester".
  `[LITERATURE:https://api.parliament.uk/historic-hansard/commons/1957/oct/31/railway-stations-manchester]`
- M. E. Quick, *Railway Passenger Stations in Great Britain: A Chronology*, RCHS, 5th edition,
  2023. `[LITERATURE:https://rchs.org.uk/wp-content/uploads/2023/09/Railway-Passenger-Stations.pdf]`
- Network Rail, *Station Capacity Planning*, NR/GN/CIV/100/03, 2023.
  `[LITERATURE:https://www.networkrail.co.uk/wp-content/uploads/2023/12/NR-GN-CIV-100-03-Station-Capacity-Planning-guidance.pdf]`
- Network Rail, *Station Facilities & Amenities*, NR/GN/CIV/200/03, 2022.
  `[LITERATURE:https://www.networkrail.co.uk/wp-content/uploads/2022/03/NR_GN_CIV_200_03-Station-Facilities-Amenities.pdf]`
- DfT, *Rail Passenger Experience of Disruption Handling*, 2021.
  `[LITERATURE:https://assets.publishing.service.gov.uk/media/60b89536e90e0743a210ddda/passenger-experience-of-disruption-handling-report.pdf]`
- ORR, *Investigation report: King's Cross and Paddington, 27-28 December 2014*, 2015.
  `[LITERATURE:https://www.orr.gov.uk/sites/default/files/om/investigation-report-2015-02-12.pdf]`
- CAA, *Passenger experiences during flight disruption*, CAP 1258, 2015.
  `[LITERATURE:https://www.caa.co.uk/publication/download/15054]`
- *Heathrow Winter Resilience Enquiry*, 2011.
  `[LITERATURE:https://im.ft-static.com/content/images/89937494-55ed-11e0-8de9-00144feab49a.pdf]`
- TRB, "Functional Design Elements for Ferry Terminals", *TRR* 817, 1981.
  `[LITERATURE:https://onlinepubs.trb.org/Onlinepubs/trr/1981/817/817-005.pdf]`
- Fan, Guthrie and Levinson, "Waiting time perceptions at transit stops and stations", *TR-A* 88,
  2016. `[LITERATURE:https://conservancy.umn.edu/server/api/core/bitstreams/8c4f1ae0-d334-48d6-a515-765b30b3eeb1/content]`
- Arhin et al., "Patron survey of acceptable wait times at transit bus stops", *OJCE* 9(4), 2019.
  `[LITERATURE:https://doi.org/10.4236/ojce.2019.94019]`
- Emily Shore, *Journal of Emily Shore*, 1898.
  `[LITERATURE:https://archive.org/details/journalemilysho00shorgoog]`
- James Woodforde diaries, Shaw-Taylor transcript, 2017.
  `[LITERATURE:https://www.campop.geog.cam.ac.uk/research/projects/transport/travellerstales/woodforde.pdf]`
- Charles G. Harper, *Stage-coach and Mail in Days of Yore*, 1903.
  `[LITERATURE:https://archive.org/details/stagecoachmailin01harp]`
- Edward Watson, *The Royal Mail to Ireland*, 1917.
  `[LITERATURE:https://archive.org/details/royalmailtoirela00watsiala]`
- G. W. Place, *The Rise and Fall of Parkgate*, 1990.
  `[LITERATURE:https://livrepository.liverpool.ac.uk/3175875/1/303317.pdf]`
