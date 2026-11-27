---
status: draft
verified: New master @ 7a0a145e1
---
# Classes

**Covers**: passenger and mail classes, vehicle accommodation classes, and how comfort,
catering and travelling post offices modify revenue.

## Passenger classes

- Passengers generate with a wealth class, 5 levels: `p_class[0]` Very low, `p_class[1]` Low,
  `p_class[2]` Medium, `p_class[3]` High, `p_class[4]` Very high, named in `New/text/en.tab`.
  `[CODE New master @ eff439751]`
- Different buildings generate and demand different proportions of each class. Commuting
  passengers never head for residential buildings; visiting passengers sometimes do.
  Lower-class passengers cannot afford high prices; each class travels on the
  lowest-journey-time route available at prices it can pay. Players set per-convoy and
  per-vehicle prices to match what each class can pay, which lets aircraft, train and coach
  coexist between the same points at different price points.
  `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`
- Per-class fares use the `p_fare[i]` keys in `New/text/en.tab`.
  `[CODE New master @ eff439751]`
- In very early eras only medium class and above can afford any passenger transport; moving
  very low class passengers at a profit in the stagecoach era indicates a cost balancing
  error, not a generation error.
  `[FORUM:https://forum.simutrans.com/index.php/topic,21310.msg198349.html#msg198349]`

## Mail classes

- Mail generates with an ability-to-pay class, 2 levels: `m_class[0]` Normal and
  `m_class[1]` Priority, with matching `m_accommodation[i]` and `m_fare[i]` keys in
  `New/text/en.tab`. `[CODE New master @ eff439751]`
- As with passengers, lower-class mail cannot afford high prices and travels on the fastest
  affordable route; players price convoys and vehicles to match.
  `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`
- Unlike passengers, mail has no comfort mechanic; class differences act purely through price
  and accommodation availability. Priority mail earns 250 percent of the normal rate
  (`class_revenue_percent[1]=250` on `name=Post` in `New/goods/goods-128.dat`).
  `[CODE New master @ 7a0a145e1]`

## Economic calibration

- Fare base: the low-class second fare stage of 0.50 cents per kilometre represents 1d per
  mile, the third-class maximum of the Regulation of the Railways Act 1844, at 1900 levels.
  `[FORUM:https://forum.simutrans.com/index.php/topic,21310.0.html]`
- Current per-class revenue percents in `New/goods/goods-128.dat`: passengers 50, 100, 150,
  200 and 300 across the five classes; mail 100 and 250 across the two classes.
  `[CODE New master @ 7a0a145e1]`
- Proposed 1900 revision: actual average third-class fares around 1900 were about 0.55d per
  mile rather than the nominal 1d, with workmen's fares lower still at about half the
  ordinary rate. The proposal halves average fares, sets very low fares at half of low fares
  with steeper gradients to high fares at twice low fares, restores the 1840s 1d, 2d and 3d
  gradient through the low, high and very high classes once inflation is simulated, removes
  the 16 km first-stage differential not used for UK passengers, and retains very-long-journey discounts aimed at sea and air travel. `[FORUM:https://forum.simutrans.com/index.php/topic,21310.msg198283.html#msg198283]`
- Accommodation build costs by class: an 1844 LBSCR first-class carriage cost 319 pounds 10
  shillings against 231/10 for second class and 160 pounds for third; by 1866 first class
  cost 283 to 315 pounds, second 277/10 and third 269, showing convergence.
  `[FORUM:https://forum.simutrans.com/index.php/topic,6521.msg82605.html#msg82605]`

## Accommodation

- Vehicles declare capacity and comfort per class index: `payload[i]` and `comfort[i]`, for
  example `New/trains/4wheel-1850s-first.dat` carries `payload[3]=18` with `comfort[3]=69`,
  and later stock such as `New/trains/br-251.dat` uses index 4.
  `[CODE New master @ eff439751]`
- A comfort rating is the maximum comfortable journey time for that accommodation. Revenue
  falls when comfort is below the passengers' tolerance; above tolerance a luxury bonus
  applies. Passengers in overcrowded vehicles count comfort as 10 for revenue purposes, or
  lower where the base rating is 10 or below.
  `[FORUM:https://forum.simutrans.com/index.php/topic,1959.0.html]`
- Upgrade willingness: passengers who can afford higher-class accommodation on the same convoy
  pay for it only where the extra comfort is worthwhile, randomised per passenger between the
  lower accommodation's maximum comfortable journey time and
  `max_comfort_preference_percentage = 650` percent of it.
  `[CODE New master @ eff439751]`

## Comfort and revenue

- Tolerable comfort ratings by journey time in `New/config/simuconf.tab`: 10 for up to 5
  minutes, 50 for up to 60, 125 for up to 150, 165 for up to 360, 250 for 1440 and above,
  with scaled proportions between. Revenue impact is strongest at long journey times.
  `[CODE New master @ eff439751]`
- The discomfort penalty is calibrated higher than the luxury bonus:
  `max_discomfort_penalty_differential = 220` with `max_discomfort_penalty_percent = 25`.
  `[CODE New master @ eff439751]`
- Waiting comfort at stops is a separate application of the same curve, with per-building
  comfortable and tolerable waiting times; see [stop-waiting](comfort/stop-waiting.md).

## Catering and travelling post offices

- Catering levels on longer journeys earn extra revenue per passenger: no revenue below
  `catering_min_minutes = 45`; level maxima of 160 from 60 minutes, 390 from 90, 830 from
  120, 1600 from 180, and 4400 from 210, with scaled proportions between levels. Catering
  vehicles also add a small comfort increase. `[CODE New master @ eff439751]`
- Vehicles declare catering with `catering_level`, for example `catering_level=1` on early
  carriages and `catering_level=3` on `New/trains/br-123.dat`. `[CODE New master @ eff439751]`
- Travelling post offices earn `tpo_revenue = 300` per mail bag carried on trips above
  `tpo_min_minutes = 90`. `[CODE New master @ eff439751]`

## Fare stages

- Distance-staged revenue and per-class revenue percents are recorded per good in
  `New/goods/goods-128.dat` (`value[i]` with `to_distance[i]`, `class_revenue_percent[i]`);
  see [goods](objects/good.md). `[CODE New master @ 7a0a145e1]`
- The staged values match the proposed 1900-calibrated fares from the cost balancing project.
  `[RECOLLECTION:2026-09-19]`

## Open questions

- What historical basis sets the mail class revenue percents (100 and 250)? No dedicated
  postage calibration source has been located.
