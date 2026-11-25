# -*- coding: utf-8 -*-
"""Evidence layer for build_workbooks.py.

Binds measured historical prices (individual-price-rows.csv + manual map) to pakset
items, derives extrapolated/interpolated class-ladder values where item data is
missing, and supplies the (a)-(d) coverage status per class.

All extrapolated values are expressed in 1900 GBP with extrap year = 1900, so the
workbook's normalisation formula leaves them unchanged and the comparison is clean.
"""
import csv, os, re, glob, math

HERE = os.path.dirname(os.path.abspath(__file__))
# The script lives in <workspace>/New/ai/cost-balancing; the pakset sources are under
# <workspace>/New and the scratch inventories under <workspace>/ai/temp.
BASE = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PRICE_ROWS = os.path.join(HERE, 'individual-price-rows.csv')
SYNTH = os.path.join(HERE, 'synthesis-recommended.csv')   # optional
PRICES_TAB = os.path.join(BASE, 'New', 'config', 'prices.tab')

# ---------------------------------------------------------------- price index
_idx = None
def general_index():
    global _idx
    if _idx is None:
        raw = None
        with open(PRICES_TAB, encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('general='):
                    raw = line.strip().split('=', 1)[1]; break
        vals = raw.split(',')
        pairs = [(int(vals[i]), float(vals[i + 1])) for i in range(0, len(vals) - 1, 2)]
        idx = {}
        for (y0, v0), (y1, v1) in zip(pairs, pairs[1:]):
            for y in range(y0, y1 + 1):
                idx[y] = v0 if y == y0 else v0 + (v1 - v0) * (y - y0) / (y1 - y0)
        idx[pairs[-1][0]] = pairs[-1][1]
        _idx = idx
    return _idx

def to_1900(nominal, year):
    """Nominal GBP of `year` -> 1900 GBP on the general index."""
    idx = general_index()
    y = int(year)
    if y in idx:
        return nominal * 100.0 / idx[y]
    ys = sorted(idx)
    if y <= ys[0]:
        return nominal * 100.0 / idx[ys[0]]
    return nominal * 100.0 / idx[ys[-1]]

def from_1900(g1900, year):
    return to_1900  # symmetry not needed; kept explicit below
def g1900_to_year(g1900, year):
    idx = general_index()
    y = int(year)
    v = idx.get(y, idx[min(idx)] if y < min(idx) else idx[max(idx)])
    return g1900 * v / 100.0

# ---------------------------------------------------------------- vehicle specs
_specs = None
def vehicle_specs():
    """{lower name: dict(freight, capacity, weight, power, engine)} from vehicle .dat blocks."""
    global _specs
    if _specs is not None:
        return _specs
    specs = {}
    folders = ['trains', 'bus', 'trams', 'boats', 'air', 'narrowgauge', 'maglev',
               'london-underground', 'boats/boats192', 'boats/boats224', 'air/air192', 'air/air256']
    for folder in folders:
        for path in glob.glob(os.path.join(BASE, 'New', folder, '*.dat')):
            name = None
            cur = {}
            def flush():
                if name:
                    specs[name.lower()] = cur.copy()
            try:
                text = open(path, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            for raw in text.splitlines():
                line = raw.split('#', 1)[0].strip()
                if not line:
                    continue
                m = re.match(r'^obj\s*=\s*(.+)$', line, re.I)
                if m:
                    flush(); name = None; cur = {}
                    continue
                if '=' not in line:
                    continue
                k, v = line.split('=', 1)
                k = k.strip().lower(); v = v.strip()
                if k in ('name', 'name__'):
                    if name is None:
                        name = v
                elif k in ('freight', 'capacity', 'weight', 'power', 'engine', 'engine_type',
                           'payload', 'length', 'cost'):
                    n = re.match(r'^-?[0-9.]+', v)
                    cur['engine' if k == 'engine_type' else k] = float(n.group(0)) if n else v
                elif k == 'payload[1]':
                    # passenger capacity: the conventional index for seats in this pakset
                    n = re.match(r'^-?[0-9.]+', v)
                    if n:
                        cur['seats'] = float(n.group(0))
                elif re.match(r'^payload\[\d+\]$', k):
                    n = re.match(r'^-?[0-9.]+', v)
                    if n:
                        cur['payload_sum'] = cur.get('payload_sum', 0.0) + float(n.group(0))
            flush()
    _specs = specs
    return specs

def spec(name, key, default=None):
    d = vehicle_specs().get(name.lower(), {})
    return d.get(key, default)

# ---------------------------------------------------------------- ladders (1900 GBP)
# Measured points converted to 1900 GBP; see New/ai/vehicle-cost-evidence.md and
# New/ai/vehicle-cost/base-maintenance.md.
CARRIAGE_PTS = [   # (year, 1900 GBP) standard compartment stock; dining vehicles x2.15
    (1846, 234.0), (1906, 1433.0), (1910, 1146.0),
    (1924, 1238.0), (1929, 1192.0), (1934, 1242.0), (1982, 2871.0),
]
DINING_MULT = 1.45   # measured dining/kitchen premium over a standard vehicle (research pass 7)
# Locomotive ladder, refitted 2026-11-22 on the measured rows bound to pakset objects.
# Steam:  price1900 = K_pre  * weight^0.86                        (before 1900)
#         price1900 = K_post * weight^0.86 * (power/600)^0.15     (1900 onwards)
# Diesel/electric: price1900 = K_diesel * power^0.889
# Fitted values from ai/temp/regress_locomotive_price.py and analyse_price_per_ton.py:
#   steam log price on log weight: elasticity 0.86, R2 0.91 (n=12);
#   adding power: R2 0.93; adding year: R2 0.97;
#   all traction: weight alone R2 0.70, power 0.889 with weight insignificant (R2 0.90).
LOCO_STEAM_B = 0.86
LOCO_STEAM_K_PRE = 107.0     # median K for 1831-1899 rows (Planet, Whishaw, Stirling, M7, T9)
LOCO_STEAM_K_POST = 132.0    # median K for 1934-1960 rows (Stanier 4P/5MT, A4, 9F)
LOCO_STEAM_POWER_B = 0.15
LOCO_STEAM_POWER_REF = 600.0
LOCO_POWER_B = 0.889
LOCO_DIESEL_K = 28.0         # median K for Class 31/52/55/66/68 (Class 57 rebuild excluded)

# Capital ladders for the other vehicle classes, 1900 GBP.
# price = anchor x exp(b x (year - anchor_year)) x (capacity / ref)^exp
# anchors are the median clean whole-vehicle measured price at the median year of the sample;
# b is the fitted real trend. See ai/temp/fit_capital_trends.py and capital_ladder_medians.py.
CAP_LADDER = {
    # anchor: median measured price in 1900 GBP at `year`, for `ref` capacity units.
    # b: residual real drift per year, fitted on 1900-GBP values (0 where the fit did not
    #    survive a size control, which is every class except aircraft).
    # The era itself is carried by prices.tab, not by the ladder: a .dat value is a 1900
    # price and the engine indexes it. A growth term here is real cost drift only.
    'bus':   dict(anchor=1240.0,   year=1930, b=0.0000, ref=50.0,  exp=0.67),
    'lorry': dict(anchor=162.0,    year=1950, b=-0.0180, ref=1.0,  exp=0.32),
    'car':   dict(anchor=234.0,    year=1959, b=0.0000, ref=4.0,   exp=0.40),
    'air':   dict(anchor=196419.0, year=1959, b=0.0200, ref=115.0, exp=0.70),
    'ship':  dict(anchor=38958.0,  year=1909, b=0.0000, ref=None,  exp=0.00),
    'tram':  dict(anchor=904.0,    year=1929, b=0.0000, ref=40.0,  exp=0.50,
                  # Structural break, not a trend. Measured points in 1900 GBP:
                  #   1901-04 municipal cars GBP 575-590 nominal -> 663-676 (Wallasey, Dover)
                  #   1929 fitted anchor 904
                  #   1996 Croydon CR4000 GBP 1.46m -> 24,026
                  #   2009 Blackpool Flexity 2 GBP 2,062,500 -> 24,888
                  #   2014 Edinburgh CAF GBP 2,396,074 -> 26,139
                  #   2018 Metrolink M5000 GBP 2,666,667 -> 24,555
                  # The old 1,976 at 1985 was unsupported by any measured price and implied a
                  # 12-fold fall then rise; it is replaced by a log-linear line from 1929 to the
                  # measured 1996 modern level. No UK tram price exists between 1950 and 1994.
                  pts=[(1902, 670.0), (1929, 904.0), (1996, 24026.0), (2026, 24500.0)]),
}

# Horse capital by breed/type, 1900 GBP for a single animal. Double = a pair.
# Anchors: 1893 London type ladder (cab 30, omnibus 35, mail 36, railway 60, heavy team 105
# guineas, deflated at index 78), vestry medians 55-65, army remounts 20-60.
# Aircraft hedonic fit, research pass 18: 116 priced aircraft 1936-2015, deflated on the vehicle
# purchase series. R2 0.948, standard error 0.334, against a mean absolute log error of 0.504 for
# the ladder it replaces. The year term survives (1.10%/yr on the full record) so it is kept, but
# at 1.0111 rather than the 1.02 that was right only for the 1936-61 sample.
AIR_HEDONIC = dict(k=785.2, seats=0.867, engines=0.768, year=1.0111, y0=1959, wide=1.22)
AIR_TYPE = {'piston': 1.00, 'turboprop': 1.50, 'turbojet': 2.48, 'turbofan': 2.75}
# per vehicle-year; ships and aircraft are carried as a share of capital because their real
# maintenance per ton and per aircraft fell so far that a deflated level is not meaningful.
# Road maintenance is now charged from the measured per-kilometre series below, split between
# the distance-driven charge and a standing charge. The capital-share evidence is kept as the
# cross-check, not as the model: the ratios measured are 21 per cent (1932 Glasgow bus, both
# sides in one set of accounts), 14 per cent (1961 bus, both sides in one article), 12 per cent
# (1934 1-ton lorry) and 21 per cent (1933 2-ton van), but the per-kilometre route implies
# 7-9 per cent for a 1955 municipal bus, so the true band is 7-21 per cent and the two routes
# do not reconcile for every vehicle. See ai/temp/road-pass-maintenance.md section 5.
ROAD_MAINT_SHARE = 0.17

# The share falls a little by era: the measured ratios are 25-30 per cent in 1914-25,
# 15-21 per cent in the 1930s and 12-14 per cent in the 1960s.
ROAD_MAINT_SHARE_ERA = [(1900, 0.22), (1920, 0.18), (1940, 0.16), (1960, 0.14)]


def road_maint_share(year):
    y = year or 1930
    s = ROAD_MAINT_SHARE_ERA[0][1]
    for (yr, val) in ROAD_MAINT_SHARE_ERA:
        if y >= yr:
            s = val
    return s


# Maintenance per kilometre, 1900 pence, from the measured operator accounts. This is the
# total repair bill (servicing and major repairs; tyres are separate and are not charged
# anywhere else, so the figures here include them where the source itemises them).
#   bus: 1925 Edinburgh 1.86 d/mile = 1.16 d/km; 1955 municipal average 0.60 d/mile = 0.37;
#        1961 31-seat 0.59 d/mile = 0.37. The 1932 Glasgow 0.91 and 1934 0.86 fall on the
#        line between 1925 and 1955.
#   lorry: normalised to a 5-tonner at payload^0.45. 1933 2-ton van 0.48, 1938 4-5 ton 0.32,
#        1950 6-ton 0.19, 1958 5-ton 0.23, 1966 7-ton 0.23, 1970 16-ton 0.22, 2016 32-ton
#        0.20. The 1982 Merseyside bus figure is excluded: its repairs head carries depot and
#        works overheads no other source includes.
ROAD_PERKM_BUS = [(1925, 1.16), (1955, 0.37)]
ROAD_PERKM_LORRY = [(1935, 0.38), (1955, 0.21), (1970, 0.22), (2016, 0.20)]
ROAD_PERKM_SIZE_BUS = 0.25      # one clean pair: 31-seat 0.59 against 41-seat 0.63 d/mile
ROAD_PERKM_SIZE_LORRY = 0.45    # fitted range 0.26-0.48 across the measured size pairs

# Lorry price has a kink at about 7 tons. Below it a fixed element (cab, engine, controls)
# dominates and the measured exponent is 0.26-0.35; above it price is close to proportional
# to payload. Measured 1900 prices: 1960 7-ton 269 and 1964 16-ton 670 (exponent 1.10 across
# that pair); 1977 32-ton Crusader 983; 1984 25-ton Roadtrain 1,059. A single power law
# cannot hold both ends, which is why the old payload^0.60 ladder priced a 25-ton tractor at
# a third of its measured price.
ROAD_LORRY_KNEE_T = 7.0
ROAD_LORRY_EXP_LIGHT = 0.30
ROAD_LORRY_EXP_HEAVY = 0.75

# Modern real level. The measured 2021-26 vehicles sit about 40 per cent above the real level
# the ladders carry: diesel single-deck bus 2021 GBP 169,000 and double-deck 236,000-251,000
# against a flat ladder; 3.5 t van 2026 GBP 47,395; 44 t tractor 2024 GBP 138,223. Interpolated
# from 1990 so the historical fit is untouched.
ROAD_MODERN_LEVEL = [(1990, 1.00), (2026, 1.40)]

# Battery-electric premium over the diesel price of the same vehicle. The 2026-11-23 electric
# pass found it is a class multiple, not a cash figure and not a single ratio: 12 same-document
# pairs cluster at about 2.0x for heavy goods vehicles from 7.5 t up (7.5 t 2.17, 12 t 2.00-2.25,
# 18 t 2.00-2.32, 26 t refuse 2.02-2.40, 44 t 1.80-2.70), 2.19-2.24 for single-deck buses and
# 1.95-2.06 for double-deck, 1.5 for coaches and a median 1.20 for vans (1.03-1.47).
# The earlier flat "GBP 230,000 cash" reading came from sampling buses only, whose diesel price
# happened to range GBP 160,000-251,000; a flat cash adder overprices a 7.5 t tipper by 105
# per cent. Hydrogen buses are about 2.2x.
ROAD_BATTERY = 2.10          # bus, coach heavy and lorry
ROAD_BATTERY_VAN = 1.25      # 2.0-3.5 t panel van
ROAD_BATTERY_COACH = 1.50

# Split between the distance-driven bill and the standing bill. No source measures the split,
# so this is an estimate and is recorded as one. The mileage part is the repairs, servicing,
# tyres and wear; the standing part is the annual test, periodic inspection, washing,
# cleaning, body and paint care and the workshop overhead that accrues whether or not the
# vehicle runs. A quarter of the total is the central estimate; the defensible band is 15-35
# per cent, and the sensitivity is that a bus at 50,000 km a year carries about GBP 0.4 a
# month of standing cost for every percentage point.
ROAD_MAINT_FIXED_SHARE = 0.25

# Reference annual distance at which the total bill is turned into the two charges.
ROAD_REF_KM = {'bus': 50000.0, 'lorry': 40000.0, 'van': 25000.0}

# A towed trailer, measured only in the FTA 2016 table: maintenance GBP 5.72 a mile for the
# trailer against 10.41 for the tractor, so 35 per cent of the combination; capital about 30
# per cent of a new combination. The old code priced trailers as horse carts, at 50 x
# (payload/2)^0.5 with 5 per cent a year and no distance charge at all.
ROAD_TRAILER_MAINT_SHARE = 0.35
ROAD_TRAILER_CAPITAL_SHARE = 0.30
ROAD_TRACTOR_MAINT_SHARE = 0.65    # FTA 2016: tractor 10.41p a mile against the trailer's 5.72

# Articulated tractor units, 1900 GBP, fitted directly on measured chassis-cab prices:
#   1933 Scammell Mechanical Horse GBP 300 -> 240; 1962 10/11-ton tractive unit GBP 1,480
#   -> 315; 1978 Seddon Atkinson 32.5 t GBP 19,500 -> 1,007; 1980 Leyland T45 Roadtrain
#   32.39 t GBP 25,495 -> 1,007; 1989 Leyland DAF 95.310 GBP 46,000 -> 1,002; 1997 DAF 95XF
#   GBP 72,790 -> 1,192; 2024 Volvo 6x2 44 t GBP 138,223 -> 1,031; RHA 2026 GBP 141,108 -> 958.
# Price scales close to the gross combination weight up to about 32 tons and then flattens,
# because a 44-tonne driveline costs little more than a 32-tonne one. GCW^0.90 fits the whole
# set to within about 18 per cent. A tractor carries no goods of its own, so the .dat has no
# payload to scale by; the nominal GCW of its era is used instead.
TRACTOR_K = 36.5
TRACTOR_EXP = 0.90
TRACTOR_GCW = [(0, 8.0), (1941, 11.0), (1966, 20.0), (1976, 32.5), (1991, 40.0), (2006, 44.0)]

# Tractor share of a new combination. Paired evidence (research pass 33): 1996/97 D-Tec trailer
# GBP 19,000 against a DAF 95XF at 72,790 = 20.7 per cent trailer; RHA 2024 139,243 and 36,946
# = 21.0; RHA 2026 141,108 and 33,075 = 19.0. Mechanical horses were different: a 1939 set of
# one unit and four trailers at GBP 1,400 against a GBP 300 unit implies about GBP 275 a trailer,
# so 55:45.
TRACTOR_TRAILER_CAPITAL_SPLIT = [(0, 0.45), (1966, 0.30), (2001, 0.22)]


def tractor_gcw(year):
    y = year or 1960
    g = TRACTOR_GCW[0][1]
    for (yr, val) in TRACTOR_GCW:
        if y >= yr:
            g = val
    return g


def tractor_trailer_ratio(year):
    """Trailer capital as a fraction of the tractor's, from the tractor share."""
    y = year or 1960
    share = TRACTOR_TRAILER_CAPITAL_SPLIT[0][1]
    for (yr, val) in TRACTOR_TRAILER_CAPITAL_SPLIT:
        if y >= yr:
            share = val
    return share / (1.0 - share)

# What each capital ladder is built from, for the basis text.
ROAD_LADDER_NOTE = {
    'bus': 'GBP 1,240 for a 50-seat complete vehicle, seats^0.67, flat in real terms; fitted to '
           '18 measured complete buses and coaches 1909-1980 (mean abs error 23 per cent). '
           'Chassis-only and body-only prices are excluded: a body is 42-45 per cent of a '
           'complete double-decker and the two scopes cannot share one anchor',
    'lorry': 'GBP 162 for a 1-ton complete lorry in 1950, payload^0.32, real level falling '
             '1.8 per cent a year; fitted to 34 measured complete lorries and vans 1920-60 '
             '(mean abs error 15 per cent). The fixed element is what the old payload^0.60 '
             'ladder lacked: a 1.5-ton van measures GBP 160-210, not GBP 58',
    'car': 'private car ladder, 4 seats at GBP 234 in 1959, seats^0.40',
}
# Tram maintenance, 1900 money a car-year, gross of revenue renewals. Research pass 47
# (New/ai/cost-balancing/research-pricing-report-47.md) measures 1923-1933, derives 1900,
# 1913, 1937-1939 and 1949-50, and estimates 1960-1990 at 150 (band 120-250) because no
# municipal tramcar account for that period was found. The modern value is the 2011
# Nottingham Express Transit availability contract, GBP 118,657 a tram-year at index 10,085
# = GBP 1,177 in 1900 money; it is a different scope (full service, 90,000 km a year) and is
# held flat from 1990. Renewals are 35 per cent of A to 1990 and zero on the modern
# contract; the works-overhaul provision is 28 / 18 / 6 per cent of A at 2 / 3 / 12 years.
TRAM_MAINT_LADDER = ((1900, 84.0), (1913, 84.0), (1920, 131.0), (1931, 106.0),
                     (1939, 89.0), (1950, 131.0), (1960, 150.0), (1990, 150.0))
TRAM_MAINT_MODERN = 1177.0
TRAM_REF_HISTORIC = 48000.0
TRAM_REF_MODERN = 90000.0

# Mean annual distance by class and era, km a vehicle-year. This table converts an overhaul
# interval in years to the engine's `max_distance_between_overhauls` field and sets the
# reference duty for the fixed/per-km split. It is a class/era reference, not a per-row
# measurement: a measured row duty overrides it. Evidence and grades:
# New/ai/vehicle-cost/mean-annual-distance.md. Values are step bands: the value applies from
# its start year to the year before the next band.
MEAN_ANNUAL_KM = {
    'carriage': ((1830, 35000.0), (1890, 36000.0), (1923, 55000.0), (1948, 88000.0),
                 (1975, 120000.0), (2000, 113000.0)),
    'wagon': ((1900, 40000.0),),
    'locomotive': ((1900, 40000.0), (1948, 65000.0), (1961, 113000.0), (1990, 150000.0)),
    'multiple-unit': ((1900, 100000.0), (1960, 120000.0), (2000, 161000.0)),
    'tram': ((1900, 48000.0), (1990, 90000.0)),
    'bus': ((1900, 55000.0),),
    'lorry': ((1900, 40000.0),),
    'van': ((1900, 40000.0),),
    'ship': ((1900, 115000.0),),
    'maglev': ((1900, 300000.0),),
}


def mean_annual_km(kind, intro):
    """Class/era mean annual distance in km, or None if the class is not in the table."""
    points = MEAN_ANNUAL_KM.get(kind)
    if not points:
        return None
    y = intro or 1900
    value = points[0][1]
    for start, candidate in points:
        if y >= start:
            value = candidate
    return value
SHIP_MAINT_RATIO = 0.02    # 1850 GSN GBP 788 against a ship capital of about GBP 39,000
AIR_MAINT_RATIO = 0.20     # BOAC VC10 1969/70 GBP 49,057 against a VC10 capital of GBP 209,085
HORSE_VEH_MAINT = 38.0     # 1893-97 horse-only accounts, 29-47

HORSE_PRICE = {
    'pony': 25.0, 'hackney': 55.0, 'freisian': 120.0, 'friesian': 120.0,
    'cleveland': 90.0, 'yorkshire': 90.0, 'irish': 135.0, 'clydesdale': 175.0,
    'shire': 180.0, 'heavy': 135.0, 'coach': 90.0, 'cart': 60.0, 'dray': 60.0,
}
HORSE_DEFAULT = 70.0

# Horse-drawn passenger vehicles, 1900 GBP. Evidence: ai/temp/road-pass-stagecoach.md.
#   stage and mail coach: GBP 100 (Hanforth's Manchester coaches, c.1760-64; general index
#     61, so GBP 164 at 1900) and Felton's 1796 plain perch coach at GBP 105 9s (index 109,
#     so GBP 96). Flat at 135: the two points bracket it and the evidence gives no trend.
#   omnibus: GBP 100-110 (1853, index 97) and GBP 150-160 (1901; index 100). 145.
#   cab: GBP 35-55 new, c.1850-1900. 52; second-hand about 26 is not a new-build price.
HORSE_PAX = {
    'stage/mail coach': 135.0,
    'short stage coach': 115.0,
    'parcel coach': 150.0,
    'omnibus': 145.0,
    'cab': 52.0,
}
HORSE_PAX_NOTE = {
    'stage/mail coach': 'GBP 100 c.1760 and Felton 1796 GBP 105 9s, both at 1900 prices',
    'short stage coach': 'lighter body than the full coach; 85 per cent of the coach',
    'parcel coach': 'no direct price; the later omnibus band, GBP 150-160 in 1901',
    'omnibus': 'GBP 100-110 in 1853 and GBP 150-160 in 1901, both at 1900 prices',
    'cab': 'GBP 35-55 new, c.1850-1900',
}
# Annual repair, 1900 GBP per vehicle-year, excluding the horse and harness.
# The one measured figure is Hanforth's GBP 210 a year for three coaches and their harness
# (c.1760): GBP 115 a coach at 1900 prices, or 70 per cent of the coach's capital. The report
# judges that a well-maintained upper bound, because Palmer complained in 1787 that
# contractors were skimping on repairs, so 55 per cent is used. The omnibus and cab figures
# are the report's inferred bands, not measurements.
HORSE_PAX_MAINT = {
    'stage/mail coach': 90.0,
    'short stage coach': 80.0,
    'parcel coach': 90.0,
    'omnibus': 90.0,
    'cab': 25.0,
}
HORSE_PAX_MAINT_NOTE = {
    'stage/mail coach': 'repair GBP 90 a year, 55 per cent of capital; the measured 1760s '
                        'account gives GBP 115 (70 per cent), judged an upper bound; charged as '
                        'a standing cost because no per-mile coaching repair figure exists',
    'short stage coach': 'repair GBP 80 a year, as the coach less the heavier body; standing',
    'parcel coach': 'repair GBP 90 a year, as the omnibus; standing',
    'omnibus': 'repair GBP 90 a year, the middle of the report\u2019s GBP 60-120 band; standing',
    'cab': 'repair GBP 25 a year, the middle of the report\u2019s GBP 15-30 band; standing',
}


def horse_pax_class(nm):
    """Which horse-drawn passenger ladder a vehicle belongs to."""
    if 'omnibus' in nm:
        return 'omnibus'
    if 'hackney' in nm or 'hansom' in nm or 'cab' in nm:
        return 'cab'
    if 'parcel' in nm:
        return 'parcel coach'
    if 'short' in nm:
        return 'short stage coach'
    return 'stage/mail coach'


def horse_pax_capital(kind):
    return HORSE_PAX[kind]


def horse_pax_maintenance(kind):
    return HORSE_PAX_MAINT[kind]

# Feature premiums, from ai/temp/research-pricing-report-7.md (2026-11-22).
# Locomotives: Horwich batch comparisons, 1907-10 (Hughes, Proc. IMechE 78).
STEAM_SUPERHEAT = 1.117      # +£350 on a ~£3,000 engine; LBSCR did it for ~£175
STEAM_COMPOUND = 1.067       # 2-cyl compound vs 2-cyl simple, +£200
STEAM_4CYL = 1.087           # four-cylinder motion vs two-cylinder simple, +£260
STEAM_3CYL = 1.045           # third cylinder alone, inferred (weak) from the 4-cyl pair
STEAM_CAPROTTI = 1.112       # BR Standard 5, 1957
# Road: 33 same-model petrol/oil pairs, Commercial Motor 1960; median +16.6%
ROAD_DIESEL = 1.17
ROAD_TROLLEY = 1.14
ROAD_STEAM = 1.10
ROAD_MIX_NORM = 1.085        # anchors are a petrol/diesel mix; normalise so the mean is unchanged
# Steam wagons are their own ladder, not a multiplier: six measured steam vehicles 1901-1933
# give price1900 = 300 x payload^0.464 (mean abs error 11 per cent), and they are all steam, so
# the petrol/diesel mix normalisation does not apply to them. At 10 tons this is 870 GBP against
# the petrol ladder's 440 in the same year, and the measured 1927-28 Sentinels and Yorkshire at
# 1,150 GBP for 10-15 tons sit on it. The report's finding that steam was cheaper per ton holds
# against a 5-6 ton petrol lorry (about 128 GBP a ton in 1927 against 101 for steam), not
# against the ladder's price at the steam wagon's own size.
ROAD_STEAM_LADDER = dict(anchor=300.0, exp=0.464)

# General feature premiums, research pass 8 (2026-11-22), 1900 GBP.
# Applied only where the feature table records the feature explicitly; a blank is the
# baseline (the same vehicle without the feature). Labels are carried into the basis.
F_AUTOMATIC = 1.15           # full automatic, heavy chassis; semi-automatic is 1.08
F_AIR_SUSP = 1.06
F_SALOON_HEAT = 1.04
F_AIRCON_BUS = 1.08
F_LOW_FLOOR = 1.03
F_CORRIDOR = 1.02
F_SLEEPING = 2.2
F_HEAT_STEAM = 1.02
F_HEAT_ELECTRIC = 1.03
F_AIRCON_RAIL = 1.10
F_TRAM_ARTIC = 1.30

# Water, research pass 25 (2026-11-22), all 1900 GBP.
# Passenger anchors are medians of measured whole-ship prices divided by capacity:
# sea-going 1927-55, river excursion 1901-37, Mersey/estuary 1847-1958.
SHIP_PAX_SEA = 66.0
SHIP_PAX_RIVER = 16.7
SHIP_PAX_ESTUARY = 10.0
# Cargo: Fairplay 7,500 dwt 1900 GBP 8.11/t; 1918 steel barge 9.12/t; Cambria 10.95/t.
SHIP_CARGO_T = 8.5
SHIP_COASTER_T = 12.0
# Inland: President steam 32.4/t; Otter/Fulbourne motor 14.5/12.2; Cambria sail 10.9;
# Ilkeston horse 7.0, Fulwell butty 8.7.
SHIP_INLAND_STEAM_T = 32.0
SHIP_INLAND_MOTOR_T = 14.0
SHIP_INLAND_SAIL_T = 11.0
SHIP_INLAND_HORSE_T = 8.0
# Vehicle deck: measured ro-ro lane-metre prices are 640 GBP/m (1987) and 1,447-3,204
# GBP a car; the pakset hold set understates car capacity, so 200 GBP a cargo tonne is a
# conservative bridge, not a measured rate.
SHIP_VEHICLE_T = 200.0
SHIP_HOVERCRAFT_PAX = 40.0   # no measured hovercraft price; assumption
SHIP_TUG_PER_HP = 40.0       # one measured tug, 1882: 81 GT, GBP 3,106 at 1900

# Multiple units: 1900 GBP per car, from set prices divided by car count and deflated.
MU_CAR_PTS = [(1905, 1745.0), (1955, 2671.0), (1982, 9500.0)]

def is_multiple_unit(nm):
    """True where the object is a car of a multiple-unit formation.

    Widened in research pass 45 section 6 item 2: the original predicate matched only names
    carrying EMU, DMU, DEMU, railcar, APT, multiple-unit or tyneside-unit, so it missed every
    BR 1xx-8xx multiple-unit class whose name carries only the class number (br-158-*, BR-365*,
    BR-465*), every *TubeStock* name, the London Underground A/C/D/OP/R/S stock, the District,
    Metropolitan, Watford and MV stock, the Southern 2-NOL/2-HAL/3-SUB/4-LAV/4-SUB/4-DD/
    401/404/5-BEL/6-PAN classes, the LMS 502 and the Docklands and Tyne & Wear metro cars.

    A locomotive, a locomotive-hauled carriage and a wagon stay out. The exclusions that carry
    a matching token are named explicitly: the 1890 tube-stock locomotive and the trailer it
    hauls (the City & South London stock was locomotive-worked), the District electric
    locomotive, and the push-pull, auto-train and augmentation-trailer carriages, whose names
    contain no MU token in the first place. BR class numbers that are locomotives (2MT, 4MT,
    5MT, 7MT, 8P, 9F, 43, 91) are absent from the class-number list.
    """
    n = (nm or '').lower()
    if not n:
        return False
    # Locomotives and locomotive-hauled stock that carry a multiple-unit token.
    if 'tubestockloco' in n or n == '1890tubestocktrailer':
        return False
    # Named multiple-unit families and the generic tokens.
    if re.search(r'dmu|emu|demu|railcar|railbus|railmotor|\bapt\b|multiple.?unit|tyneside', n):
        return True
    if 'tubestock' in n or 'twinset' in n:
        return True
    # London Underground, District, Metropolitan, Watford and Metrovick multiple-unit stock.
    if n.startswith(('lul_', 'district_', 'met-mv-stock', 'watfordjointstock')):
        return True
    if n.startswith(('metropolitan1905', 'metropolitan1913', 'metropolitan1921',
                     'metropolitan-motor')):
        return True
    # Light metro cars.
    if n.startswith('dlr-') or 'tynewearmetro' in n:
        return True
    # Southern Region and BR electric-multiple-unit class codes.
    if re.match(r'br-(2epb|4epb)', n) or re.match(r'br-class(483|485)', n):
        return True
    if re.match(r'sr-(2-nol|2hal|3sub|4lav|401|404|4dd|4sub|5-bel|6pan)', n):
        return True
    # BR diesel and electric multiple-unit class numbers. EMU classes are 3xx, 4xx (with the
    # 4-EPB and 4-SUB codes named above), 5xx and 7xx-8xx; DMU/DEMU classes are 1xx-2xx.
    br_mu = ('101', '104', '110', '114', '117', '120', '121', '123', '127', '128', '139',
             '141', '142', '144', '150', '153', '156', '158', '159', '165', '166', '170',
             '172', '175', '180', '185', '195', '196', '202', '205', '210', '220', '221',
             '222', '251', '302', '303', '304', '307', '309', '310', '312', '313', '314',
             '315', '317', '318', '319', '320', '321', '323', '325', '331', '332', '333',
             '334', '345', '350', '357', '360', '365', '370', '373', '374', '375', '376',
             '377', '378', '379', '380', '385', '387', '390', '395', '397', '410', '414',
             '419', '421', '423', '430', '442', '444', '450', '455', '456', '458', '460',
             '465', '489', '491', '499', '501', '506', '507', '700', '701', '707', '710',
             '717', '720', '730', '769', '800', '801')
    m = re.match(r'br-(\d{3})(?!\d)', n)
    if m and m.group(1) in br_mu:
        return True
    if n.startswith('br-derby-lightweight') or n.startswith('c2c-357') or n.startswith('lms-502'):
        return True
    return False

_features = None

def vehicle_features():
    """Object name -> feature row, from the research attribute tables if present."""
    global _features
    if _features is None:
        _features = {}
        for fn in ('vehicle-features-general.csv', 'vehicle-features.csv',
                   'vehicle-features-locomotives.csv'):
            p = os.path.join(HERE, fn)
            if os.path.exists(p):
                for row in csv.DictReader(open(p, encoding='utf-8-sig')):
                    nm = (row.get('name') or '').strip().lower()
                    if nm:
                        _features[nm] = row
    return _features

_water = None
def water_capacity():
    """Object name -> capacity record from ai/temp/water-capacity.csv."""
    global _water
    if _water is None:
        _water = {}
        p = os.path.join(HERE, 'water-capacity.csv')
        if os.path.exists(p):
            for row in csv.DictReader(open(p, encoding='utf-8-sig')):
                nm = (row.get('name') or '').strip().lower()
                if not nm:
                    continue
                def f(key):
                    try:
                        return float(str(row.get(key, '')).replace(' t', '').strip())
                    except (TypeError, ValueError):
                        return 0.0
                _water[nm] = dict(pax=f('passengers'), cargo=f('cargo_tonnes'),
                                  total=f('total_size'),
                                  type=(row.get('type') or '').strip().lower(),
                                  kind=(row.get('kind') or '').strip().lower())
    return _water

# Per-gross-ton water ladder (2026-11-25 decision). Research reports 56 and 57 established that
# the three per-GT rates are the measured capital prices of report 25: 84.1 x GT^0.90 is the
# 14-vessel passenger fit deflated to 1900 money, GBP 35/GT is the British Railways 1950-53
# cargo price and GBP 17/GT is Cambria's 1906 inland price. The tug rate of GBP 39/GT is report
# 25 section 9.4's single 1882 point (81 GT). Rows without a tonnage keep the capacity ladder:
# hovercraft (no gross tonnage exists), holds (the parent carries the hull) and the hulls the
# tonnage passes could not identify.
WATER_FERRY_RATE = 84.1
WATER_CARGO_PER_GT = 35.0
WATER_INLAND_PER_GT = 17.0
WATER_TUG_PER_GT = 39.0
WATER_GT_BRIDGE = {'barge': 1.2, 'narrowboat': 1.2, 'river-boat': 6.2, 'cargo': 1.6,
                   'coaster': 1.6}

_water_gt = None
def water_tonnage():
    """Object name -> gross-tonnage record from water-gross-tonnage.csv and its additions."""
    global _water_gt
    if _water_gt is None:
        _water_gt = {}
        for fn in ('water-gross-tonnage.csv', 'water-gross-tonnage-additions.csv'):
            p = os.path.join(HERE, fn)
            if not os.path.exists(p):
                continue
            for row in csv.DictReader(open(p, encoding='utf-8-sig')):
                nm = (row.get('name') or '').strip().lower()
                if not nm:
                    continue
                cur = _water_gt.get(nm, {})
                gt = (row.get('gross_tonnage') or '').strip()
                try:
                    gt = float(gt.replace(',', ''))
                except ValueError:
                    gt = 0.0
                _water_gt[nm] = dict(
                    gt=gt or cur.get('gt', 0.0),
                    kind=(row.get('kind') or '').strip().lower() or cur.get('kind', ''),
                    method=(row.get('method') or '').strip().lower() or cur.get('method', ''),
                    type=(row.get('type') or '').strip().lower() or cur.get('type', ''),
                    size=(row.get('total_size_t') or '').strip() or cur.get('size', ''),
                    definition=(row.get('gross_tonnage_definition') or '').strip()
                    or cur.get('definition', ''),
                    year=(row.get('year') or '').strip() or cur.get('year', ''),
                    grade=(row.get('evidence_grade') or '').strip() or cur.get('grade', ''),
                    identity=(row.get('identity') or '').strip() or cur.get('identity', ''))
    return _water_gt


def water_gt_price(name):
    """(capital GBP, basis) from the per-gross-ton ladder, or (None, reason).

    A row the tonnage research examined and left blank with a reason is not bridged: an
    unidentified hull, or a fit whose capacity bridge would price one hull at three sizes, keeps
    the capacity rule. A row the research bridged carries its figure and is priced normally."""
    nm = (name or '').lower()
    rec = water_tonnage().get(nm)
    if not rec:
        return None, 'no tonnage record'
    kind = rec.get('type') or ''
    gt = rec.get('gt') or 0.0
    basis_extra = ''
    if not gt:
        if rec.get('method', '').startswith('unavailable') or kind == 'hovercraft':
            return None, 'no gross tonnage: ' + (rec.get('method') or 'hovercraft')
        ratio = WATER_GT_BRIDGE.get(kind)
        try:
            size = float(rec.get('size') or 0)
        except ValueError:
            size = 0.0
        if ratio and size > 0:
            gt = ratio * size
            basis_extra = ' (bridge %g gross tons per capacity tonne on %.1f capacity tonnes)' \
                          % (ratio, size)
        else:
            return None, 'no gross tonnage'
    if kind in ('ferry', 'river-boat'):
        return WATER_FERRY_RATE * (gt ** 0.90), (
            '%s gross tons%s at 1900, priced on the passenger fit 84.1 x GT^0.90'
            % (format(round(gt, 1), ','), basis_extra))
    if kind in ('cargo', 'coaster'):
        return WATER_CARGO_PER_GT * gt, (
            '%s gross tons%s at 1900, priced at GBP %g a gross ton'
            % (format(round(gt, 1), ','), basis_extra, WATER_CARGO_PER_GT))
    if kind in ('barge', 'narrowboat'):
        return WATER_INLAND_PER_GT * gt, (
            '%s gross tons%s at 1900, priced at GBP %g a gross ton'
            % (format(round(gt, 1), ','), basis_extra, WATER_INLAND_PER_GT))
    if kind == 'tug':
        return WATER_TUG_PER_GT * gt, (
            '%s gross tons%s at 1900, priced at GBP %g a gross ton (the 1882 tug point)'
            % (format(round(gt, 1), ','), basis_extra, WATER_TUG_PER_GT))
    if kind == 'other':
        return WATER_INLAND_PER_GT * gt, (
            '%s gross tons%s at 1900, priced at GBP %g a gross ton (the inland rate, the nearest '
            'measured per-gross-ton price for a small craft)'
            % (format(round(gt, 1), ','), basis_extra, WATER_INLAND_PER_GT))
    return None, 'no per-gross-ton rate for this type'

def _flag(row, key):
    return str((row or {}).get(key) or '').strip().lower()

def _num(row, key):
    try:
        return float((row or {}).get(key))
    except (TypeError, ValueError):
        return None

def road_premiums(nm, kind):
    """(multiplier, labels) for bus/lorry features, research pass 8."""
    f = vehicle_features().get(nm, {})
    m, parts = 1.0, []
    trans = _flag(f, 'transmission')
    if trans in ('automatic', 'auto'):
        m *= F_AUTOMATIC
        parts.append('automatic transmission x%.2f' % F_AUTOMATIC)
    if _flag(f, 'suspension') == 'air':
        m *= F_AIR_SUSP
        parts.append('air suspension x%.2f' % F_AIR_SUSP)
    if _flag(f, 'low_floor') in ('yes', 'y', 'true', '1'):
        m *= F_LOW_FLOOR
        parts.append('low floor x%.2f' % F_LOW_FLOOR)
    if _flag(f, 'aircon') in ('yes', 'y', 'true', '1'):
        m *= F_AIRCON_BUS
        parts.append('air conditioning x%.2f' % F_AIRCON_BUS)
    if kind == 'bus' and _flag(f, 'heating') in ('yes', 'y', 'true', '1'):
        m *= F_SALOON_HEAT
        parts.append('saloon heating x%.2f' % F_SALOON_HEAT)
    return m, parts

def carriage_premiums(nm):
    """(multiplier, labels) for railway carriage features, research pass 8."""
    f = vehicle_features().get(nm, {})
    m, parts = 1.0, []
    if _flag(f, 'corridor') in ('yes', 'y', 'true', '1'):
        m *= F_CORRIDOR
        parts.append('corridor x%.2f' % F_CORRIDOR)
    sleep = _flag(f, 'sleeping')
    if sleep in ('yes', 'y', 'true', '1') or (not sleep and 'sleep' in nm):
        m *= F_SLEEPING
        parts.append('sleeping car x%.1f' % F_SLEEPING)
    heat = _flag(f, 'heating')
    if heat == 'steam':
        m *= F_HEAT_STEAM
        parts.append('steam heating x%.2f' % F_HEAT_STEAM)
    elif heat == 'electric':
        m *= F_HEAT_ELECTRIC
        parts.append('electric heating x%.2f' % F_HEAT_ELECTRIC)
    elif heat in ('yes', 'y', 'true', '1'):
        m *= F_HEAT_STEAM
        parts.append('heating x%.2f' % F_HEAT_STEAM)
    if _flag(f, 'aircon') in ('yes', 'y', 'true', '1'):
        m *= F_AIRCON_RAIL
        parts.append('air conditioning x%.2f' % F_AIRCON_RAIL)
    return m, parts

def tram_premiums(nm):
    """(multiplier, labels) for tram features, research pass 8."""
    f = vehicle_features().get(nm, {})
    m, parts = 1.0, []
    if _flag(f, 'articulated') in ('yes', 'y', 'true', '1'):
        m *= F_TRAM_ARTIC
        parts.append('articulated x%.2f' % F_TRAM_ARTIC)
    return m, parts


def steam_features(nm):
    """(cylinders, arrangement, superheat, valve_gear) from the table, else from the name."""
    f = vehicle_features().get(nm, {})
    def norm(v):
        return str(v or '').strip().lower()
    cyl = norm(f.get('cylinders'))
    if not cyl:
        if re.search(r'4[- ]?cyl|four[- ]?cyl', nm):
            cyl = '4'
        elif re.search(r'3[- ]?cyl|three[- ]?cyl', nm):
            cyl = '3'
        elif 'compound' in nm:
            cyl = '2'
    arr = norm(f.get('arrangement'))
    if not arr and 'compound' in nm:
        arr = 'compound'
    sup = norm(f.get('superheat'))
    if not sup and 'superheat' in nm:
        sup = 'yes'
    vg = norm(f.get('valve_gear')) or ('caprotti' if 'caprotti' in nm else '')
    return cyl, arr, sup, vg

def steam_multiplier(nm):
    m, parts = 1.0, []
    cyl, arr, sup, vg = steam_features(nm)
    if sup in ('yes', 'y', 'true', '1'):
        m *= STEAM_SUPERHEAT; parts.append('superheat x1.117')
    if arr == 'compound':
        m *= STEAM_COMPOUND; parts.append('compound x1.067')
    if cyl == '4':
        m *= STEAM_4CYL; parts.append('4-cyl x1.087')
    elif cyl == '3':
        m *= STEAM_3CYL; parts.append('3-cyl x1.045 (weak)')
    if vg.startswith('caprotti') or 'caprotti' in vg:
        m *= STEAM_CAPROTTI; parts.append('Caprotti x1.112')
    return m, parts

def consist_extra_weight(name):
    """Weight of the other units of a multi-part locomotive.

    The pakset convention is that the front unit carries the whole cost, so the weight ladder
    must see the whole weight. A tender or a Garratt middle/rear is a separate object with its
    own weight; its weight is added here and its own price is set to zero.
    """
    nm = name.lower()
    extra = 0.0
    S = vehicle_specs()
    d = S.get(nm + '-tender')
    if d:
        extra += float(d.get('weight') or 0)
    if nm.endswith('-front'):
        stem = nm[:-6]
        for suf in ('-middle', '-rear'):
            d = S.get(stem + suf)
            if d:
                extra += float(d.get('weight') or 0)
    return extra


_adj = None


def vehicle_adjustments():
    """[(match, capital, maintenance, source, note)] from ai/temp/rail-adjustments.csv.

    A qualitative adjustment layer for classes whose build cost or reliability is documented but
    for which no individual price exists. Adjustments are deliberately modest (5-15 per cent) and
    are applied only where a source states the direction.
    """
    global _adj
    if _adj is None:
        _adj = []
        p = os.path.join(HERE, 'vehicle-adjustments.csv')
        if os.path.exists(p):
            with open(p, encoding='utf-8-sig') as f:
                for r in csv.DictReader(f):
                    try:
                        _adj.append((r['match'].lower(), float(r['capital']),
                                     float(r['maintenance']), r.get('source', ''),
                                     r.get('note', '')))
                    except (TypeError, ValueError):
                        continue
        # longest match first so a specific class beats a company prefix
        _adj.sort(key=lambda x: -len(x[0]))
    return _adj


def apply_adjustment(name, x):
    nm = (name or '').lower()
    for match, cap, mnt, src, note in vehicle_adjustments():
        if match in nm:
            if cap != 1.0 and x.get('capital_gbp'):
                x['capital_gbp'] = round(x['capital_gbp'] * cap, 0)
            if mnt != 1.0 and x.get('maint_gbp_yr'):
                x['maint_gbp_yr'] = round(x['maint_gbp_yr'] * mnt, 1)
            x['basis'] = (x.get('basis', '') + ' | adjustment x%.3f capital, x%.3f maintenance: '
                          '%s (%s)' % (cap, mnt, note, src)).strip(' |')
            return True
    return False


def air_seats(name):
    """Passenger-seat equivalent of an aircraft.

    Air .dat files carry `payload[n]` per class; postal and freight variants put kilograms
    in the same field (an A320 post aircraft has payload 17,800 = 17.8 t of mail). Summing
    the field blindly turns a freighter into a 17,800-seat airliner, so non-passenger
    aircraft are converted at 100 kg per seat-equivalent and passenger aircraft are capped
    at a plausible airliner size.
    """
    d = vehicle_specs().get(name.lower(), {})
    freight = str(d.get('freight', '')).lower()
    cap = d.get('payload_sum') or d.get('payload')
    try:
        capf = float(cap) if cap is not None else None
    except (TypeError, ValueError):
        capf = None
    if capf is None:
        return None
    if 'passagiere' in freight or 'passenger' in freight:
        return capf if capf <= 900 else None
    # Post aircraft carry kilograms in the same field at every size; 100 kg is one
    # seat-equivalent. The generic goods-unit heuristic below would read a 1,000 kg
    # post payload as 1,000 seats.
    if 'post' in freight:
        return capf / 100.0
    # Freight aircraft carry either kilograms (A320 post: 17,800) or goods units
    # (A320 fish/piece: 210 units of 17.8 t). Above 1,000 the figure is kilograms; below, it
    # is a goods count that happens to be of the same order as a seat count.
    return capf / 100.0 if capf > 1000 else capf


def capital_ladder(kind, year, capacity=None):
    p = CAP_LADDER[kind]
    y = year or p['year']
    pts = p.get('pts')
    if pts:
        # log-linear interpolation between measured anchor points, flat outside the range
        if y <= pts[0][0]:
            price = pts[0][1]
        elif y >= pts[-1][0]:
            price = pts[-1][1]
        else:
            for (y0, p0), (y1, p1) in zip(pts, pts[1:]):
                if y0 <= y <= y1:
                    t = (y - y0) / float(y1 - y0)
                    price = math.exp(math.log(p0) * (1 - t) + math.log(p1) * t)
                    break
    elif kind == 'lorry':
        # Piecewise ladder: a fixed element below the knee, near-proportional above it.
        yl = min(max(y, 1920), 1960)
        base = p['anchor'] * math.exp(p['b'] * (yl - p['year']))
        t = max(float(capacity or 1.0), 0.2)
        if t <= ROAD_LORRY_KNEE_T:
            price = base * t ** ROAD_LORRY_EXP_LIGHT
        else:
            price = (base * ROAD_LORRY_KNEE_T ** ROAD_LORRY_EXP_LIGHT
                     * (t / ROAD_LORRY_KNEE_T) ** ROAD_LORRY_EXP_HEAVY)
        return price
    else:
        # The lorry trend is fitted on 1920-1960 and must not be extrapolated outside it: at
        # 1750 it would multiply the level by 36, and after 1980 the pakset's modern heavy
        # lorries measure well above it. The modern level is carried by ROAD_MODERN_LEVEL.
        yl = min(max(y, 1920), 1960) if kind == 'lorry' else y
        price = p['anchor'] * math.exp(p['b'] * (yl - p['year']))
    if p['ref'] and capacity:
        price *= (float(capacity) / p['ref']) ** p['exp']
    return price

def horse_price(name):
    nm = name.lower()
    base = HORSE_DEFAULT
    for k, v in HORSE_PRICE.items():
        if k in nm:
            base = v
            break
    if nm.endswith('-double') or '-double-' in nm or 'pair' in nm or (
            re.search(r'horses|ponies|mules|donkeys', nm) and 'single' not in nm):
        base *= 2
    return base
WAGON_PER_TON = 7.07      # Shildon 1906 mean 7.2 nominal = 7.07 at 1900 (range 6.2-8.2)
HORSE_KEEP_YR = 45.0      # London accounts 1876-97, band 28-60 (1900 GBP/yr per animal)
ANIMAL_NAME = re.compile(r'horse|pony|ponies|mule|donkey', re.I)
PAIR_NAME = re.compile(r'pair|double|horses|ponies|mules|donkeys', re.I)

# Maglev: no mainline maglev exists in Britain, so its prices come from the overseas systems,
# adjusted for labour cost (USER DIRECTION, recorded in New/ai/vehicle-cost/maglev-costs.md).
# Acquisition: the Shanghai imported Transrapid cars at more than RMB 100m a car (2003; research
# pass 55), GBP 105,129 a car in 1900 money, 92.8 seats a five-car set = 1,087.5 GBP a seat after
# the 0.96 labour adjustment (band 761-1,133). The previous Almujibah and Preston estimate
# (EUR 49,233 a seat at 2009 prices = 507.6) remains the serial-production floor.
# Maintenance: Almujibah and Preston 2018, Table 6 (2009 prices), EUR 0.011 a seat-km; no
# operator account found in pass 55 separates rolling-stock maintenance, so the rate stands.
# EUR 1 = GBP 0.89; deflated on the workbook index (vehicle purchase 82.87 and general 91.63
# times 1900 in 2009); labour x0.96 for Germany, the source country (report 17 section 5).
# Non-passenger stock has no seat count: the acquisition rate is applied per metre of car length
# on the 14 m, 54-seat reference car.
MAGLEV_CAP_PER_SEAT = 1087.5
MAGLEV_MAINT_SEAT_KM = 0.011 * 0.89 / 91.63 * 0.96
MAGLEV_REF_SEATS = 54.0
MAGLEV_REF_LENGTH = 14.0
MAGLEV_CAP_PER_M = MAGLEV_CAP_PER_SEAT * MAGLEV_REF_SEATS / MAGLEV_REF_LENGTH
MAGLEV_MAINT_M_KM = MAGLEV_MAINT_SEAT_KM * MAGLEV_REF_SEATS / MAGLEV_REF_LENGTH
LOCO_REPAIR_PERKM = 0.0067  # Hill 1892 1.61 d/km; WITHDRAWN as a separate charge (report 46)
LOCO_MAINT_YR = 253.0     # Hill 1892 GWR maximum; WITHDRAWN as the total (report 46)
CARRIAGE_MAINT_YR = 32.6  # Hill 1892 carriage average, retained for the multiple-unit branch
# Rail carriage and wagon maintenance ladders, 1900 money per vehicle-year. Research pass 43
# (New/ai/cost-balancing/research-pricing-report-43.md): the carriage series is measured at 1892
# (Hill), 1961 (the Beeching functional split, GBP 1,012 a coach-year), 1984 (the HST train-mile
# rate), 2013 (RDG EMU rate) and 2024-25 (ORR medians); the wagon ladder uses the measured
# wagon:carriage ratio, which falls from 12.6 per cent in 1892 to 5.4 per cent in 1961 and is held
# after. Research pass 51 re-bases the carriage series: the 1912 company mean and the measured
# 1913-1921 rolling-stock change give 39 at 1920 (band 28-55), and the 1950 rung is re-drawn to
# 121 by interpolation between 39 at 1920 and 183 at 1961. The 1948 and 1966 values (112 and 226)
# are read from the interpolation, not stored. Log-linear between points, flat outside. The wagon
# figure is per 10-tonne wagon-year and scales by (payload/10)^0.4.
CARRIAGE_MAINT_LADDER = ((1900, 33.0), (1920, 39.0), (1950, 121.0), (1970, 265.0), (1990, 460.0),
                         (2020, 440.0))
WAGON_MAINT_LADDER = ((1900, 4.2), (1950, 8.7), (1970, 14.3), (1990, 24.8), (2020, 23.8))
# Locomotive maintenance, 1900 money per engine-year. Research pass 46 section 5, validated and
# extended by research pass 50: the 1900, 1950 and 1961 points are measured fleet averages, 1977
# is Calder's measured main-line Class 47, and 1995 and 2020 are derived from measured
# heavy-maintenance turnover. Log-linear between points, flat outside. This is the diesel/steam
# line; a straight-electric locomotive does NOT take a share of it (see ELEC_LOCO_LADDER).
LOCO_MAINT_LADDER = ((1900, 215.0), (1950, 306.0), (1961, 800.0), (1977, 2100.0),
                     (1995, 1045.0), (2020, 520.0))
# Electric-locomotive maintenance track, 1900 money per engine-year. Research pass 50 section 5
# item 6 reads the modern ladder as two class tracks; research pass 46 row 12 supplies the 1950s
# point. The 1950 point is the Southern Region electric locomotives at GBP 5,300 each in 1949-50,
# repairs only, deflated at the general index 359 (5,300 x 100 / 359 = 1,476). The 1977 point is
# Calder's Class 87, GBP 1,103 in 1900 money (report 46 row 19). The 1995 point is the BRML
# mixed-fleet heavy-maintenance turnover (report 50), and the 2018 point is the measured Class 92
# full-maintenance contract (868). Log-linear between points, flat outside. The 0.5-of-the-diesel
# -ladder rule is Calder's 1977 Class 87/Class 47 ratio, a class result rather than a
# traction-type constant; this track replaces it for the intermediate electric classes.
ELEC_LOCO_LADDER = ((1950, 1476.3), (1977, 1103.0), (1995, 1045.0), (2018, 868.0))
# Class overrides with their own measured figure. A class here takes the figure, not a rung of
# either track. The Class 92 is the 2018 Alstom/GB Railfreight full-maintenance contract on the
# Caledonian Sleeper duty (research pass 50; GBP 868, band 740-1,000). The Class 88 is the 2014
# dual-mode, which pass 64 puts at the Class 68 level (614.82) rather than on half the electric
# ladder. Keys are the lower-case pakset object names.
LOCO_CLASS_OVERRIDES = {
    'br-class92': (868.0, 'the 2018 Alstom/GB Railfreight full-maintenance contract, GBP 868 an '
                          'engine-year in 1900 money (research pass 50; band 740-1,000)'),
    'br-class88': (614.82, 'the Class 68 level of 614.82 GBP an engine-year (pass 64), the '
                           'nearest measured 2014 dual-mode diesel'),
}
# Classes with no class-specific figure that take the electric track rather than half the
# diesel/steam ladder. The 2026-11-25 decision: interpolate the intermediate electric
# locomotives between the measured 1950s and 1980s/1990s points.
LOCO_ELECTRIC_TRACK = ('br-class89', 'br-class90', 'br-class91')
# Measured class duties, km an engine-year, where Calder's 1977 paper gives the class its own
# figure rather than the class/era table's band (research pass 46 row 17). Keys are the
# lower-case pakset object names. Every other locomotive takes MEAN_ANNUAL_KM['locomotive'].
LOCO_DUTY_KM = {
    'br-class37': 81000.0,
    'br-class55': 226000.0,
    'br-class86': 176000.0,
    'br-class87': 274000.0,
    '1890tubestockloco': 120000.0,
}


def loco_duty(name, intro):
    """km an engine-year: the class's own measured duty if it has one, else the table band."""
    nm = (name or '').lower()
    if nm in LOCO_DUTY_KM:
        return LOCO_DUTY_KM[nm]
    return mean_annual_km('locomotive', intro) or 40000.0


# Bridge-substructure piers (the 111 `Piers & docks` rows). Research pass 13 section 6 measures
# the substructure share of a low bridge at 13-25 per cent (Tower Bridge 15.8, the Humber 60 ft
# worked example 25); the share rises with pier height to 65.9-82.3 per cent at 200 ft. The pakset
# records no height or span for a pier object, so the low-bridge midpoint of 19 per cent is
# charged against the measured rate of the bridge family the object belongs to. The deck and
# track are carried by the way object; no substructure maintenance rate is measured, so the
# maintenance sheet's pier rows stay blank.
PIER_SHARE = 0.19
PIER_FAMILY_RATE = {
    'brick': ('BrickViaduct', 107500.0),
    'stone': ('MasonryViaduct', 107500.0),
    'concrete': ('ConcreteViaduct', 410317.0),
    'iron': ('IronViaduct', 164000.0),
    'steel': ('SteelTruss', 280000.0),
    'timber': ('WoodenTrestle', 48000.0),
}


def pier_family(name):
    """brick, stone, concrete, iron, steel or timber, by the object's base name."""
    nm = (name or '').lower()
    if nm.startswith('steel'):
        return 'steel'
    if nm.startswith('iron') or nm.startswith('l') or nm == 'brickironarch':
        return 'iron'
    if nm.startswith('brick'):
        return 'brick'
    if nm.startswith('stone'):
        return 'stone'
    if nm.startswith('concrete'):
        return 'concrete'
    if nm.startswith('wood'):
        return 'timber'
    return None


def pier_extrapolation(name):
    fam = pier_family(name)
    if not fam:
        return None
    rep, rate = PIER_FAMILY_RATE[fam]
    return {'capital_gbp': round(PIER_SHARE * rate, 2), 'year': 1900,
            'basis': ('pier (pass 68, research pass 13 section 6): the measured 13-25 per cent '
                      'substructure share of a low bridge at its midpoint 19 per cent, applied to '
                      'the %s bridge rate of GBP %s a km at 1900. Tower Bridge measures 15.8 per '
                      'cent and the Humber 60 ft worked example 25 per cent; the share rises with '
                      'pier height (Maynard 1868: 65.9 per cent at 200 ft and 82.3 per cent with '
                      '60 ft spans). The pakset records no height or span for a pier object, so '
                      'the low-bridge midpoint is used and the band is stated. The object is '
                      'charged as the substructure component of the equivalent bridge; the deck '
                      'and track are carried by the way object it supports. Maintenance is not '
                      'charged: pass 13 measures no substructure maintenance share.'
                      % (rep, format(int(rate), ',')))}



def loco_maint(name, engine, intro):
    """(A, basis) for one locomotive, 1900 GBP an engine-year.

    A class with a measured figure takes it. A Class 89, 90 or 91 takes the electric track at
    its introduction year. Any other straight-electric locomotive after 1961 takes half the
    diesel/steam ladder (Calder's 1977 Class 87/Class 47 ratio); a pre-1961 electric takes the
    ladder whole. Everything else takes the diesel/steam ladder."""
    nm = (name or '').lower()
    eng = (engine or '').lower()
    y = intro or 1900
    if nm in LOCO_CLASS_OVERRIDES:
        a, label = LOCO_CLASS_OVERRIDES[nm]
        return a, 'class figure: ' + label
    electric = ('electric' in eng) and ('diesel' not in eng)
    if electric and nm in LOCO_ELECTRIC_TRACK:
        return interp_log(ELEC_LOCO_LADDER, y), (
            'electric-locomotive track: 1,476 at 1950 (Southern Region electrics, GBP 5,300 each '
            'in 1949-50, repairs only), 1,103 at 1977 (Calder\'s Class 87), 1,045 at 1995 (BRML '
            'mixed fleet) and 868 at 2018 (the Class 92 contract), read at the introduction year '
            '(research passes 46 row 12, 50 section 5 item 6)')
    base = interp_log(LOCO_MAINT_LADDER, y)
    if electric and y > 1961:
        return 0.5 * base, ('half the diesel/steam ladder: Calder\'s 1977 Class 87 is 52 per cent '
                            'of the Class 47 on the same duty (research pass 46 row 19)')
    return base, ('locomotive ladder: 215 at 1900, 306 at 1950, 800 at 1961, 2,100 at 1977, 1,045 '
                  'at 1995 and 520 at 2020 (research passes 46 and 50)')


def loco_renewals(intro):
    """Renewals share of A for a locomotive: 25 per cent at 1900 phased out by 1950, 22 per cent
    at 1961 phased in from 1950 and out by 1977, zero after."""
    y = intro or 1900
    if y <= 1950:
        return 0.25 * (1950.0 - y) / 50.0
    if y <= 1961:
        return 0.22 * (y - 1950.0) / 11.0
    if y <= 1977:
        return 0.22 * (1977.0 - y) / 16.0
    return 0.0


def locomotive_overhaul(intro, maint_gbp, km, steam):
    """Overhaul targets for a locomotive inside the measured-total envelope (passes 49-66)."""
    a = maint_gbp or 0.0
    share = 0.35 if steam else 0.39
    years = 7.0
    rho = loco_renewals(intro) * a
    prov = share * a
    mx = prov * years
    return dict(initial_gbp=round(mx, 1), max_gbp=round(mx, 1), overhauls=0,
                interval_km=int(round(years * (km or 40000.0))), months=0.8,
                mean_gbp=round(mx, 1),
                basis=('locomotive overhaul (passes 49-66): the measured annual total is the '
                       'envelope. Renewals %.1f per cent of A; works-overhaul provision %.0f per '
                       'cent of A; head = the residual; the event is provision x %.0f years = '
                       '%.1f GBP, one event to the maximum. The interval is %.0f years at the '
                       'class/era distance. %s'
                       % (100.0 * loco_renewals(intro), 100.0 * share, years, mx, years,
                          'steam: 35 per cent provision and a 65/35 split'
                          if steam else 'diesel/electric: 39 per cent provision and a 60/40 '
                                        'split, from the Class 47 pair')))


def interp_log(points, x):
    """Log-linear interpolation between the points, flat outside the ends."""
    xs = [p[0] for p in points]
    if x <= xs[0]:
        return points[0][1]
    if x >= xs[-1]:
        return points[-1][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= x <= x1:
            t = (x - x0) / float(x1 - x0)
            return math.exp(math.log(y0) + (math.log(y1) - math.log(y0)) * t)
    return points[-1][1]

def interp(points, x):
    xs = [p[0] for p in points]
    if x <= xs[0]:
        return points[0][1]
    if x >= xs[-1]:
        return points[-1][1]
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= x <= x1:
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return points[-1][1]

# ---------------------------------------------------------------- status (a)-(d)
STATUS = {
    # class: (b class data, c item data, d extrapolate)
    'rail-vehicles':      ('yes', 'yes', 'partial'),
    'road-vehicles':      ('yes', 'partial', 'yes'),
    'water-vehicles':     ('partial', 'partial', 'no'),
    'air-vehicles':       ('partial', 'no', 'no'),
    'tram-vehicles':      ('partial', 'partial', 'partial'),
    'narrowgauge-vehicles': ('no', 'no', 'no'),
    'maglev-vehicles':    ('yes', 'no', 'partial'),   # overseas system costs; no British maglev
    'ways/rail':          ('yes', 'yes', 'yes'),
    'ways/road':          ('yes', 'partial', 'yes'),
    'ways/water':         ('yes', 'yes', 'yes'),
    'ways/tram':          ('partial', 'no', 'partial'),
    'ways/narrowgauge':   ('partial', 'no', 'partial'),
    'ways/air':           ('yes', 'partial', 'yes'),
    'ways/maglev':        ('no', 'no', 'no'),
    'ways/power':         ('partial', 'partial', 'partial'),
    'bridges':            ('yes', 'yes', 'partial'),
    'tunnels':            ('yes', 'yes', 'partial'),
    'signals':            ('yes', 'partial', 'partial'),
    'signalboxes':        ('yes', 'partial', 'partial'),
    'roadsigns':          ('no', 'no', 'no'),
    'way-objects':        ('yes', 'partial', 'yes'),
    'stops-stations/stations': ('yes', 'yes', 'yes'),
    'stops-stations/piers':    ('yes', 'partial', 'yes'),
    'depots':             ('partial', 'partial', 'partial'),
    'engine-settings':    ('partial', 'no', 'partial'),
}

def status(cls, name):
    b, c, d = STATUS.get(cls, ('no', 'no', 'no'))
    return ['no', b, c, d]

# ---------------------------------------------------------------- manual measured map
# item name pattern -> (year, nominal GBP, kind, source_ref, note)
MANUAL = [
    (r'(?i)^leyland[-_]national(?![-_]?b)', 1971, 9500, 'capital',
     'The Commercial Motor, 3 December 1971, p.41, Grand National road test',
     'Complete integral bus as road-tested, with all the extras. This is a measured capital price, '
     'so the class capital adjustment is not applied to it; the family maintenance adjustment '
     'still is. The -b variant is excluded because it has its own capital adjustment and no price.'),
    (r'(?i)^aero-commander-500$', 1952, 16071, 'capital',
     'All Aero, "Aero Design & Engineering 500 / 520 / 560 / 580 / Shrike Commander / L-26"; '
     'AOPA, "An Aero Commander Restoration" (2002)',
     'Aero Commander 520, the first production model (1951-52), $45,000 at $2.80/GBP = GBP '
     '16,071 nominal; the 500 series began in 1958 and the 500B was $87,000 standard in 1960'),
    (r'(?i)^lswr-emu', 1915, 1520, 'capital',
     'research pass 27; Electric Railway Journal 7 Aug 1915 and the LSWR 1916 annual meeting',
     'LSWR 1915 stock conversion: GBP 383,000 for 252 cars = GBP 1,520 a car, GBP 4,560 a '
     'three-car unit; bodies converted from 1902-12 bogie-block coaches at Eastleigh, British '
     'Westinghouse equipment (type 339, 275 hp, four per unit), 600 V DC third rail'),
    (r'(?i)^lmr-planet(-goods)?$', 1831, 780, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; published-capital',
     'St Rollox "Planet" type, Robert Stephenson, new'),
    (r'(?i)^lswr-m7$', 1897, 1846, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'LSWR M7 0-4-4T'),
    (r'(?i)^lswr-t9(-superheated)?$', 1899, 3200, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'LSWR T9 4-4-0'),
    (r'(?i)^lms-stanier-4p-tank(-3-cylinder)?$', 1934, 6444, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'LMS 2500 class 2-6-4T'),
    (r'(?i)^lms-stanier-5mt$', 1934, 6000, 'capital',
     'balance-synthesis.md 5.2; forum thread 6521', 'LMS Black 5'),
    (r'(?i)^lner-a4$', 1936, 8500, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'LNER A4 4-6-2'),
    (r'(?i)^br-class31-1$', 1957, 78000, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'BR Class 31 diesel'),
    (r'(?i)^br-class52$', 1957, 87500, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'BR Warship diesel-hydraulic'),
    (r'(?i)^br-class55$', 1959, 150000, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'Deltic type 5'),
    (r'(?i)^br-9f$', 1960, 35500, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; forum thread 6521', 'BR 9F 2-8-0'),
    (r'(?i)^br-mk3-tso$', 1982, 100000, 'capital',
     'vehicle-cost-evidence.md "Carriages"; forum thread 6521', 'BR Mk III, early 1980s; stands for the Mk III family'),
    (r'(?i)^gnr-stirling8foot$', 1870, 2033, 'capital',
     'vehicle-cost-evidence.md "Locomotives"; both', 'GNR G Class "Stirling 8ft Single" 4-2-2 of 1870'),
]

def _manual_for(name):
    for pat, yr, gbp, kind, ref, note in MANUAL:
        if re.match(pat, name):
            return yr, gbp, kind, ref, note
    return None

# ---------------------------------------------------------------- measured rows cache
_prows = None
def price_rows():
    global _prows
    if _prows is None:
        if os.path.exists(PRICE_ROWS):
            with open(PRICE_ROWS, encoding='utf-8-sig') as f:
                _prows = list(csv.DictReader(f))
        else:
            _prows = []
    return _prows

def _norm(s):
    return re.sub(r'[^a-z0-9]+', '', (s or '').lower())


# US dollars per pound, by year. The fixed pegs are exact: the classical gold standard at 4.86
# (to 1913), the interwar return at 4.86 (1925-31), the Bretton Woods peg at 4.03 (1940-49),
# 2.80 (1949-67) and 2.40 (1967-71). The floating years are annual averages to about 5 per
# cent, sufficient because a exchange-rate error of that size is small beside the cost scatter.
# The register records dollars as stated and this table converts only at the point of use,
# which is what vehicle-cost-method.md requires.
USD_PER_GBP = {
    1850: 4.86, 1875: 4.86, 1900: 4.86, 1913: 4.86,
    1914: 4.90, 1915: 4.75, 1916: 4.55, 1917: 4.45, 1918: 4.30, 1919: 4.42,
    1920: 3.66, 1921: 3.85, 1922: 4.42, 1923: 4.57, 1924: 4.43,
    1925: 4.86, 1926: 4.86, 1927: 4.86, 1928: 4.86, 1929: 4.86, 1930: 4.86, 1931: 4.86,
    1932: 3.50, 1933: 4.25, 1934: 5.04, 1935: 4.90, 1936: 4.97, 1937: 4.94, 1938: 4.89,
    1939: 4.03, 1940: 4.03, 1945: 4.03, 1947: 4.03, 1949: 4.03,
    1950: 2.80, 1952: 2.80, 1954: 2.80, 1955: 2.80, 1956: 2.80, 1957: 2.80, 1958: 2.80,
    1959: 2.80, 1960: 2.80, 1961: 2.80, 1962: 2.80, 1963: 2.80, 1964: 2.80, 1965: 2.80,
    1966: 2.80, 1967: 2.75, 1968: 2.40, 1969: 2.40, 1970: 2.40, 1971: 2.45,
    1972: 2.50, 1973: 2.45, 1974: 2.34, 1975: 2.22, 1976: 1.80,
    1977: 1.75, 1978: 1.92, 1979: 2.12, 1980: 2.33,
    1981: 2.03, 1982: 1.75, 1983: 1.52, 1984: 1.34, 1985: 1.30, 1986: 1.47, 1987: 1.64,
    1988: 1.78, 1989: 1.61, 1990: 1.79,
    1991: 1.77, 1992: 1.77, 1993: 1.50, 1994: 1.53, 1995: 1.58, 1996: 1.56, 1997: 1.64,
    1998: 1.66, 1999: 1.62,
    2000: 1.52, 2001: 1.44, 2002: 1.50, 2003: 1.64, 2004: 1.83, 2005: 1.82, 2006: 1.84,
    2007: 2.00, 2008: 1.85, 2009: 1.57,
    2010: 1.55, 2011: 1.60, 2012: 1.59, 2013: 1.56, 2014: 1.65, 2015: 1.53, 2016: 1.36,
    2017: 1.29, 2018: 1.34, 2019: 1.28,
    2020: 1.28, 2021: 1.38, 2022: 1.24, 2023: 1.24, 2024: 1.28, 2025: 1.30, 2026: 1.30,
}


def usd_per_gbp(year):
    """US dollars to the pound for a year, using the nearest listed year."""
    if not year:
        return None
    ys = sorted(USD_PER_GBP)
    if year <= ys[0]:
        return USD_PER_GBP[ys[0]]
    if year >= ys[-1]:
        return USD_PER_GBP[ys[-1]]
    lo = max(y for y in ys if y <= year)
    hi = min(y for y in ys if y >= year)
    if lo == hi:
        return USD_PER_GBP[lo]
    t = (year - lo) / float(hi - lo)
    return USD_PER_GBP[lo] * (1 - t) + USD_PER_GBP[hi] * t

def _name_score(pn, nn):
    """0 = exact; >0 = containment, closer is better; None = reject.
    A containment that changes the digits (Class 45 vs Class 455) is rejected."""
    if not pn or not nn:
        return None
    if pn == nn:
        return 0
    # The containment length floor used to be 8 characters, which silently excluded every short
    # object name: aec-605, ee-e11, guy-bt-56 and but-9611t could never bind a measured row
    # whose name carried a description. Five characters, with the digit guard below, admits them
    # without letting "class 45" match "class 455".
    if len(pn) > 4 and pn in nn:
        i = nn.index(pn)
        before = nn[i - 1] if i else ''
        after = nn[i + len(pn)] if i + len(pn) < len(nn) else ''
        if before.isdigit() or after.isdigit():
            return None
        return 2 + (len(nn) - len(pn))
    if len(nn) > 4 and nn in pn:
        i = pn.index(nn)
        before = pn[i - 1] if i else ''
        after = pn[i + len(nn)] if i + len(nn) < len(pn) else ''
        if before.isdigit() or after.isdigit():
            return None
        return 2 + (len(pn) - len(nn))
    return None

def match(prows, cls, name):
    """Return measured source data bound to this item, or None."""
    out = {}
    m = _manual_for(name)
    if m:
        yr, gbp, kind, ref, note = m
        if kind == 'capital':
            out.update(capital_gbp=gbp, capital_year=yr)
        else:
            out.update(maint_gbp_yr=gbp, maint_year=yr)
        out.update(source_ref=ref, notes=note)
    # scored name match against the measured rows: exact first, then the closest
    # containment; fleet totals and multi-vehicle orders are penalised, per-unit wording favoured
    nn = _norm(name)
    cands = []
    for pr in prows:
        pn = _norm(pr.get('name_or_item'))
        s = _name_score(pn, nn)
        if s is None:
            continue
        raw = (pr.get('name_or_item') or '').lower()
        if 'per locomotive' in raw or 'per vehicle' in raw or 'per unit' in raw or raw.endswith('each'):
            s -= 2
        if ('fleet' in raw or 'order (' in raw
                or re.search(r'\b\d+\s+(locomotives|vehicles|carriages|wagons|units)\b', raw)):
            s += 6
        cands.append((s, pr))
    cands.sort(key=lambda t: t[0])
    for _, pr in cands:
        # A Simutrans road vehicle is a complete vehicle. Binding it to a chassis-only or
        # body-only measured price compares unlike with unlike: a body is 42-45 per cent of a
        # complete bus, so the measured figure would read about half the real price.
        if cls == 'road-vehicles' and pr.get('kind') == 'capital':
            note = (pr.get('notes') or '').lower()
            unit = (pr.get('price_unit') or '').lower()
            oname = (pr.get('name_or_item') or '').lower()
            # Scope is read from the name and the unit, never from the notes: a complete vehicle
            # legitimately records "chassis plus body" in its note.
            scope_text = unit + ' ' + oname
            if (('chassis' in scope_text and 'complete' not in scope_text)
                    or 'body only' in scope_text or 'bodies at' in scope_text):
                continue
            if ('complete' not in oname
                    and re.search(r'\b(chassis|body)\b', oname)):
                continue
            # Option and differential prices are not vehicle prices: a magneto at GBP 12 and
            # a diesel premium of GBP 135 are additions to a chassis, not the chassis.
            oname = (pr.get('name_or_item') or '').lower()
            if any(k in oname or k in note for k in
                   ('option', 'additional cost', 'price difference', 'differential', 'extra')):
                continue
            # A trailer is not a tractor: the Scammell Crusader price must not bind to each of
            # its trailer variants.
            if 'trailer' in nn and 'trailer' not in oname:
                continue
        try:
            price = float(str(pr.get('price', '')).replace(',', ''))
        except ValueError:
            continue
        unit = (pr.get('price_unit') or '').lower()
        yr = re.match(r'^(\d{4})', pr.get('year') or '')
        if not yr:
            continue
        year = int(yr.group(1))
        # Dollars are recorded as stated in the register and converted only here, at the point
        # of use, which is what vehicle-cost-method.md requires. USD_PER_GBP holds the rates.
        is_usd = ('usd' in unit or '$' in unit or 'dollar' in unit)
        if is_usd:
            rate = usd_per_gbp(year)
            if not rate:
                continue
            price = price / rate
            unit = unit.replace('usd', 'gbp').replace('$', 'gbp').replace('dollar', 'gbp')
            conv_note = 'converted from US dollars at %.2f to the pound' % rate
        else:
            conv_note = ''
        if pr.get('kind') == 'capital' and 'gbp' in unit:
            if 'capital_gbp' not in out:
                out.update(capital_gbp=price, capital_year=year)
                if conv_note:
                    out['notes'] = conv_note
        elif pr.get('kind') == 'maintenance':
            if 'per vehicle-year' in unit or 'per year' in unit or '/yr' in unit:
                if 'maint_gbp_yr' not in out:
                    out.update(maint_gbp_yr=price, maint_year=year)
            elif 'per km' in unit or 'per mile' in unit or 'per m ' in unit or unit.endswith('per m'):
                if 'per mile' in unit:
                    price = price / 1.609344
                if 'perkm_gbp' not in out:
                    out.update(perkm_gbp=price, perkm_year=year)
        ref = pr.get('source_ref', '')
        kb = pr.get('kb_location', '')
        out.setdefault('source_ref', ('%s (%s)' % (ref, kb)).strip())
        notes = pr.get('notes', '')
        if notes:
            out['notes'] = (out.get('notes', '') + ' | ' + notes).strip(' |')
    return out or None

# ---------------------------------------------------------------- extrapolation
# Overhaul and upgrade profiles, by class. Shares are of the vehicle's own capital target,
# except the rail carriage and wagon classes, which are shares of the measured annual
# maintenance figure (see CARRIAGE_OVERHAUL and WAGON_OVERHAUL below).
#   initial / max       cost of the first and the late-life overhaul, as a share of capital
#   n                   overhauls before the cost reaches the maximum
#   interval_km         distance between overhauls
#   months              time out of service per overhaul
#   upgrade             net cost of replacing an old vehicle with this type, as a share of the
#                       new vehicle's capital (a trade-in price, not the new price)
# These are placeholders pending research pass 36/37 and are the single place to change.
CARRIAGE_OVERHAUL = (
    # Research pass 44 section 5: (from year, interval years, reference km, provision of A).
    # The provision is calibrated on two measured events: Lacy & Dow's GBP 62 in the 1860s
    # (1.84 x A) and the 1982 York Works Mk 1 overhaul at "more than GBP 2,000" (0.16 x A).
    (1830, 6.0, 210000.0, 0.28),
    (1890, 5.0, 180000.0, 0.24),
    (1923, 3.0, 165000.0, 0.19),
    (1948, 2.0, 176000.0, 0.12),
    (1975, 2.0, 240000.0, 0.10),
    (2000, 2.6, 294000.0, 0.08),
)
WAGON_OVERHAUL = dict(provision=0.20, years=6.0, km=240000.0, first_ratio=0.75)
# Research pass 46: the measured wagon total A is the envelope, head = 0.8A and the event
# 1.2A every six years at the 40,000 km/yr reference duty. Only the product 0.20 x 6 is
# constrained; the split between the share and the interval is an estimate.
OVH_FIRST_RATIO = 0.70   # first event as a share of the maximum (research pass 44 section 6)
OVH_RUNGS = 3


def carriage_overhaul(intro, maint_gbp):
    """Overhaul targets for a carriage, from the measured annual maintenance figure A."""
    y = intro or 1900
    row = CARRIAGE_OVERHAUL[0]
    for cand in CARRIAGE_OVERHAUL:
        if y >= cand[0]:
            row = cand
    _, years, km, share = row
    # The interval is the band's years at the class and era distance table's reference duty,
    # not a per-band constant: the two agree at every existing band, and this is the route by
    # which a row's own measured duty can replace the table default.
    table_km = mean_annual_km('carriage', y)
    if table_km:
        km = years * table_km
    ann = share * (maint_gbp or 0.0)
    mx = 2.0 * ann * years / (1.0 + OVH_FIRST_RATIO)
    return dict(initial_gbp=round(OVH_FIRST_RATIO * mx, 1), max_gbp=round(mx, 1),
                overhauls=OVH_RUNGS, interval_km=km, months=0.5,
                mean_gbp=round(ann * years, 1))


def wagon_overhaul(maint_gbp):
    """Overhaul targets for a wagon, from the measured annual maintenance figure A."""
    a = maint_gbp or 0.0
    first = WAGON_OVERHAUL['first_ratio'] * WAGON_OVERHAUL['provision'] * WAGON_OVERHAUL['years'] * a
    mx = WAGON_OVERHAUL['provision'] * WAGON_OVERHAUL['years'] * a
    return dict(initial_gbp=round(first, 1), max_gbp=round(mx, 1), overhauls=2,
                interval_km=WAGON_OVERHAUL['km'], months=0.2,
                mean_gbp=round((first + mx) / 2.0, 1))


def tram_maint(intro):
    """Gross annual maintenance A for a tram, 1900 GBP a car-year (research pass 47)."""
    y = intro or 1929
    if y >= 1990:
        return TRAM_MAINT_MODERN
    return interp_log(TRAM_MAINT_LADDER, y)


def tram_upgrade_share(intro):
    """Share of the new price charged as upgrade_price (research pass 47 section 5)."""
    y = intro or 1900
    if y <= 1950:
        return 0.22
    if y >= 1990:
        return 0.50
    return 0.22 + 0.28 * (y - 1950) / 40.0


def tram_overhaul(intro, maint_gbp):
    """Overhaul targets for a tram, from the gross annual maintenance figure A.

    Research pass 47: renewals are inside A for the municipal series; the works-overhaul
    provision is 28 / 18 / 6 per cent of A at 2 / 3 / 12 years. The first event is 0.35A
    rising to 0.75A over 3 / 2 / 1 events; the modern contract carries one event of 0.75A.
    """
    a = maint_gbp or 0.0
    y = intro or 1900
    if y >= 1990:
        share, years, km, months, rungs = 0.06, 12.0, 1080000.0, 0.8, 1
        first = 0.75 * a
        mx = 0.75 * a
    elif y >= 1950:
        share, years, km, months, rungs = 0.18, 3.0, 144000.0, 0.5, 2
        first = 0.35 * a
        mx = 0.75 * a
    else:
        share, years, km, months, rungs = 0.28, 2.0, 96000.0, 0.4, 3
        first = 0.35 * a
        mx = 0.75 * a
    return dict(initial_gbp=round(first, 1), max_gbp=round(mx, 1), overhauls=rungs,
                interval_km=km, months=months, mean_gbp=round(share * a * years, 1))


OVERHAUL_PROFILE = {
    # rail: research pass 36. Steam interval 104,000-196,000 miles per general repair
    # (BR Pacifics 1951-60) = 167,000-315,000 km; cost 5 per cent first, 15 per cent late,
    # from the GWR 28xx heavy general at GBP 450-700 against a GBP 4,992 build (9-14 per cent);
    # downtime 31-53 days. Diesel and electric: BR's 2.75/5.5/11-year overhauls, cost 6-8 per
    # cent first and 18-22 per cent late (estimate). Carriage: two-year cycle, 8 per cent first
    # and 25-30 per cent late, the Midland 1860s overhaul being 25-28 per cent. Multiple unit:
    # 4 per cent first, 20 per cent late. Upgrade: reboilering 19.5-27.3 per cent of capital and
    # the Class 47-to-57 rebuild about a third of a new build, so 30-35 per cent.
    'locomotive-steam': (0.05, 0.15, 4, 200000.0, 1.2, 0.35),
    'locomotive':     (0.07, 0.20, 3, 300000.0, 0.8, 0.35),
    'carriage':       (0.08, 0.27, 3, 250000.0, 0.5, 0.35),
    'wagon':          (0.10, 0.30, 3, 200000.0, 0.2, 0.35),
    'multiple-unit':  (0.04, 0.20, 3, 300000.0, 0.4, 0.30),
    # road, tram, ship and aircraft: research pass 37. Bus four-year overhaul about 220,000 km,
    # GBP 2,000 a bus in 1965 excluding Chiswick units (25-33 per cent of a new double-decker),
    # late-life 30-40 per cent; municipal engine overhauls at 120,000-150,000 miles. Lorry
    # 80,000-160,000 km, the 1955 cycle GBP 60 engine plus GBP 220 chassis and body at 100,000
    # miles (8-22 per cent); van 24,000-64,000 km. Tram: Metrolink mid-life at 12 years and
    # GBP 80,000 (about 8 per cent), Supertram life extension at 32-34 years and GBP 856,000
    # (40-50 per cent); no measured historic municipal tramcar overhaul. Ship: five-year special
    # survey, drydocking every 2.5-5 years, 2-5 per cent of newbuild value, 12 days. Aircraft:
    # C check 18-24 months and three weeks, D check six years, base checks 2-3 per cent of a new
    # narrowbody. Upgrade: the Leyland National Greenway rebuild at GBP 45,000 was stated to be
    # half a new bus, so 50 per cent. Trams are handled by tram_overhaul() from A, not here.
    'bus':            (0.25, 0.40, 3, 220000.0, 0.5, 0.50),
    'lorry':          (0.10, 0.30, 3, 160000.0, 0.3, 0.50),
    'van':            (0.10, 0.30, 3, 60000.0, 0.1, 0.50),
    'ship':           (0.02, 0.05, 6, 0.0, 0.4, 0.50),
    'aircraft':       (0.025, 0.05, 4, 0.0, 0.8, 0.50),
    'horse':          (0.00, 0.00, 0, 0.0, 0.0, 0.50),
}

OVERHAUL_CLASS = [
    (r'^(br-|lner|lms|gwr|sr-|ner-|lnwr|lbscr|gnr|nbr|ger|secr|mr-|cr-)', 'locomotive'),
]


def overhaul_profile(cls, name, capital_gbp, intro, maint_gbp=None):
    """Suggested overhaul and upgrade figures for one vehicle, in 1900 GBP.

    maint_gbp is the measured annual maintenance figure from extrapolation(); the rail
    carriage and wagon classes take their overhaul events from it (research passes 44 and 46)
    and fall back to the capital-share rule only when it is absent."""
    nm = (name or '').lower()
    key = None
    if cls == 'rail-vehicles':
        d = vehicle_specs().get(nm, {})
        freight = str(d.get('freight', '')).lower()
        if is_multiple_unit(nm):
            key = 'multiple-unit'
        elif 'wagons' in nm or 'wagon' in nm:
            key = 'wagon'
        else:
            key = 'carriage' if ('passagiere' in freight or 'post' in freight) else 'locomotive'
            if key == 'locomotive' and 'steam' in str(d.get('engine', '')).lower():
                key = 'locomotive-steam'
    elif cls == 'tram-vehicles':
        key = 'tram'
    elif cls == 'road-vehicles':
        d = vehicle_specs().get(nm, {})
        if 'horse' in nm or not d.get('power'):
            # A horse-drawn vehicle is not overhauld in the engine's sense; its repair is in
            # the standing charge. The horse itself likewise.
            key = 'horse'
        else:
            key = 'bus' if 'passagiere' in str(d.get('freight', '')).lower() else 'lorry'
    elif cls == 'water-vehicles':
        key = 'ship'
    elif cls == 'air-vehicles':
        key = 'aircraft'
    if key is None:
        return None
    cap = capital_gbp or 0.0
    if key == 'tram':
        a = maint_gbp if maint_gbp else tram_maint(intro)
        p = tram_overhaul(intro, a)
        p['upgrade_gbp'] = round(cap * tram_upgrade_share(intro), 1)
        p['basis'] = ('tram overhaul (research pass 47 section 5): the gross annual figure A '
                      'is the envelope. Provision 28 / 18 / 6 per cent of A at 2 / 3 / 12 '
                      'years, the event 0.35A rising to 0.75A over 3 / 2 / 1 events; renewals '
                      '35 per cent of A to 1990 and zero on the modern contract. Upgrade %.0f '
                      'per cent of the new price, from the measured 1934 London County Council '
                      'E/1 rebuild and the 2026 Supertram life extension.'
                      % (tram_upgrade_share(intro) * 100))
        return p
    up = OVERHAUL_PROFILE[key][5]
    if key in ('locomotive', 'locomotive-steam') and maint_gbp:
        km = loco_duty(name, intro)
        p = locomotive_overhaul(intro, maint_gbp, km, key == 'locomotive-steam')
        p['upgrade_gbp'] = round(cap * up, 1)
        return p
    if key == 'carriage' and maint_gbp:
        p = carriage_overhaul(intro, maint_gbp)
        p['upgrade_gbp'] = round(cap * up, 1)
        p['basis'] = ('carriage overhaul (research pass 44 section 5): the measured annual '
                      'maintenance figure is the envelope. The works-overhaul provision is 28, '
                      '24, 19, 12, 10 and 8 per cent of A at 1830-89, 1890-1922, 1923-47, '
                      '1948-74, 1975-99 and 2000-26, from two measured events (Lacy & Dow GBP 62 '
                      'in the 1860s = 1.84 A; the 1982 York Works Mk 1 overhaul = 0.16 A); the '
                      'interval is 6, 5, 3, 2, 2 and 2.6 years, entered as the band\'s reference '
                      'km. The mean event is provision x interval x A = %s GBP, paid as a first '
                      'overhaul of %s GBP rising to a maximum of %s GBP over %d. The 0.70 '
                      'first-event ratio is an estimate. Upgrade %.0f per cent of the new price.'
                      % (p['mean_gbp'], p['initial_gbp'], p['max_gbp'], p['overhauls'], up * 100))
        return p
    if key == 'wagon' and maint_gbp:
        p = wagon_overhaul(maint_gbp)
        p['upgrade_gbp'] = round(cap * up, 1)
        p['basis'] = ('wagon overhaul (research pass 46): the measured annual maintenance figure '
                      'is the envelope, head = 0.8A and the event 1.2A every six years at the '
                      '40,000 km/yr reference duty (240,000 km), first event 0.75 of the steady '
                      'event, two rungs. The 0.20 share and the six years are an estimate; only '
                      'their product is constrained. Upgrade %.0f per cent of the new price.'
                      % (up * 100))
        return p
    s0, smax, n, km, months, up = OVERHAUL_PROFILE[key]
    return dict(initial_gbp=round(cap * s0, 1), max_gbp=round(cap * smax, 1),
                overhauls=n, interval_km=km, months=months,
                upgrade_gbp=round(cap * up, 1),
                basis='%s profile: first overhaul %.0f per cent of capital, late-life %.0f per '
                      'cent, %d overhauls to the maximum, %s km between overhauls, %.1f months '
                      'out of service; upgrade %.0f per cent of the new price'
                      % (key, s0 * 100, smax * 100, n,
                         ('%d' % km) if km else 'n/a', months, up * 100))


def extrapolation(cls, name, dat, gbp_per_dat=0.00396311, intro=None):
    """Class-ladder extrapolation for an item with no individual data. None if unsupported.
    gbp_per_dat converts one .dat unit to 1900 GBP for the row's family; intro is the
    item's intro year where known, used to interpolate the ladders."""
    nm = name.lower()
    sp = vehicle_specs().get(nm, {})
    freight = str(sp.get('freight', '')).lower()
    cap = sp.get('capacity')
    wt = sp.get('weight')
    pwr = sp.get('power')
    eng = str(sp.get('engine', '')).lower()
    year = None  # all outputs expressed at 1900
    x = {}
    if cls == 'stops-stations/piers':
        p = pier_extrapolation(name)
        if p:
            return p

    # Animals are not locomotives, tram cars or vessels. The horse-keep evidence is the only
    # measure for them, and it applies on every sheet (pass 43). The horse clause below used to
    # sit after the class dispatch, so rail, narrow-gauge, tram and water animals took the
    # sheet's ladder (a locomotive's 253 GBP/engine-year, a tram car's 64, a ship's 2 per cent).
    if ANIMAL_NAME.search(nm) and str(sp.get('engine', '')).lower() == 'bio':
        try:
            animal_power = float(sp.get('power') or 0)
        except (TypeError, ValueError):
            animal_power = 0.0
        if animal_power >= 1:
            pair = 1.0
            if PAIR_NAME.search(nm) and 'single' not in nm:
                pair = 2.0
            x.update(capital_gbp=round(horse_price(name), 0), year=1900,
                     basis='horse breed/type ladder (1900 GBP): pony 25, hackney 55, Friesian 120, '
                           'Cleveland Bay 90, Yorkshire coach 90, Irish draught 135, Clydesdale '
                           '175, Shire 180, cart/dray 60; a pair doubles the figure')
            x.update(maint_gbp_yr=HORSE_KEEP_YR * pair, maint_year=1900,
                     basis=x['basis'] + ' | London horse-keep accounts 1876-97: about 45 GBP an '
                           'animal-year (band 28-60) at 1900, excluding the horsekeeper; the '
                           'whole figure is standing and there is no per-km charge')
            return x

    # Maglev rolling stock: overseas system costs adjusted for labour (user direction), used
    # directly as individual figures: no decomposition applies to either the capital price or
    # the per-seat-km maintenance cost.
    if cls == 'maglev-vehicles':
        seats = sp.get('seats') or 0.0
        length = sp.get('length') or MAGLEV_REF_LENGTH
        if seats and seats > 0:
            capital = MAGLEV_CAP_PER_SEAT * seats
            perkm = MAGLEV_MAINT_SEAT_KM * seats
            unit = '%d seats' % seats
        else:
            capital = MAGLEV_CAP_PER_M * length
            perkm = MAGLEV_MAINT_M_KM * length
            unit = '%g m of car length (no seat count, so the seat rate is applied per metre ' \
                   'on the 14 m, 54-seat reference car)' % length
        x.update(capital_gbp=round(capital, 0), year=1900,
                 basis='overseas maglev stock: Shanghai imported Transrapid cars at more than '
                       'RMB 100m a car (2003), GBP 105,129 a car in 1900 money, 92.8 seats a '
                       'five-car set = 1,087.5 GBP a seat after the 0.96 labour adjustment '
                       '(research pass 55; band 761-1,133); the previous EUR 49,233 a seat '
                       'estimate (507.6) is the serial-production floor: %.1f GBP a '
                       'seat in 1900 money; %s' % (MAGLEV_CAP_PER_SEAT, unit))
        x.update(perkm_gbp=round(perkm, 10), perkm_year=1900,
                 basis=x['basis'] + ' | maintenance EUR 0.011 a seat-km at 2009 prices, at the '
                       'same exchange and labour adjustment and deflated on the general index '
                       '(91.63 times 1900 in 2009): the cost is distance-driven, so the whole '
                       'figure is the per-km charge and there is no fixed charge')
        return x

    if cls in ('rail-vehicles', 'narrowgauge-vehicles'):
        # Multi-part locomotives: the front unit carries the whole cost; tenders and Garratt
        # middle/rear units are priced at zero. Their weight is added to the front unit instead.
        if 'tender' in nm or nm.endswith('-middle') or nm.endswith('-rear'):
            x.update(capital_gbp=0, year=1900,
                     maint_gbp_yr=0.0, maint_year=1900,
                     basis='multi-part locomotive: the front unit carries the whole cost, so this '
                           'unit is priced zero by pakset convention')
            return x
        if pwr and float(pwr) > 0:                      # locomotive or multiple-unit car
            pw = float(pwr)
            yr_match = _manual_for(name)
            yi = intro or (yr_match[0] if yr_match else None)
            if is_multiple_unit(nm):
                cap = sp.get('payload_sum') or sp.get('capacity')
                try:
                    capf = float(cap) if cap is not None else 80.0
                except (TypeError, ValueError):
                    capf = 80.0
                base = interp(MU_CAR_PTS, yi or 1955)
                base *= (max(capf, 1.0) / 80.0) ** 0.5
                x.update(capital_gbp=round(base, 0), year=1900,
                         basis='multiple-unit car ladder: 1,745 GBP (1905) to 9,500 GBP (1982) per '
                               'car (1900), from set prices divided by car count, x (seats/80)^0.5')
                x.update(maint_gbp_yr=CARRIAGE_MAINT_YR, maint_year=1900,
                         basis=x['basis'] + ' | Hill 1892 carriage rate 32.6 GBP/vehicle-year')
            else:
                diesel = any(t in eng for t in ('diesel', 'electric', 'turbine'))
                if diesel and 'electric' in eng and yi and yi <= 1930:
                    rate = 8.8 if (pw >= 1000 and 'ee1' in nm) else 4.4
                    x.update(capital_gbp=round(rate * pw, 0), year=1900,
                             basis=('early electric locomotive at GBP %.1f per hp: measured 1902-22 '
                                    'series GBP 4.4/hp, one-off prototypes GBP 8.8/hp; ES1 5.66, '
                                    'Met 1922 3.93, EE1 8.88' % rate))
                elif diesel and 'electric' in eng and yi and yi <= 1955:
                    x.update(capital_gbp=round(7.0 * pw, 0), year=1900,
                             basis=('electric locomotive 1948-55 at GBP 7 per hp: Riddles 1951 '
                                    'GBP 37,400 and the 1955 average of GBP 55,000 give 6.4-9.4 '
                                    'per hp'))
                elif diesel:
                    x.update(capital_gbp=round(LOCO_DIESEL_K * (pw ** LOCO_POWER_B), 0), year=1900,
                             basis=('power^0.889 x 28 GBP (1900), fitted on measured diesels/electric '
                                    '1957-2013 (Class 31, 52, 55, 66, 68; Class 57 rebuild excluded)'))
                elif wt and float(wt) > 0:
                    # The ladder is a complete-engine ladder fitted on the engine weight, so the
                    # tender's cost is already inside it. A tank engine has no tender and must not
                    # pay for one: the measured tank engines sit at 0.84-0.88 of the ladder, so
                    # 0.86 is applied.
                    wtf = float(wt)
                    k = LOCO_STEAM_K_POST if (yi and yi >= 1900) else LOCO_STEAM_K_PRE
                    capital = k * (wtf ** LOCO_STEAM_B)
                    if yi and yi >= 1900:
                        capital *= (pw / LOCO_STEAM_POWER_REF) ** LOCO_STEAM_POWER_B
                        basis = ('weight^0.86 x 132 GBP (1900) x (power/600)^0.15; fitted on 1934-1960 '
                                 'steam; complete-engine ladder on the engine weight, the tender '
                                 'cost being inside it')
                    else:
                        basis = ('weight^0.86 x 107 GBP (1900); fitted on 1831-1899 steam including '
                                 'the Whishaw 1830s engines; complete-engine ladder on the engine '
                                 'weight, the tender cost being inside it')
                    sm, parts = steam_multiplier(nm)
                    # The premium is applied relative to the feature composition of the sample the
                    # ladder was fitted on, not by era. The pre-1900 sample is all saturated
                    # two-cylinder (baseline 1.000); the post-1900 sample is three superheated
                    # two-cylinder (1.117) and two superheated three-cylinder (1.167), geometric
                    # mean 1.137. A post-1900 saturated engine is therefore cheaper than the base,
                    # and a post-1900 three-cylinder one dearer.
                    baseline = 1.137 if (yi and yi >= 1900) else 1.000
                    rel = sm / baseline
                    if abs(rel - 1.0) > 0.001:
                        capital *= rel
                        basis += (' | features x%.3f relative to the fitted base (base x%.3f: %s)'
                                  % (rel, baseline, ', '.join(parts) if parts else 'none'))
                    x.update(capital_gbp=round(capital, 0), year=1900, basis=basis)
            # The Hill 1892 GBP 253 an engine-year is withdrawn as the total (research pass 46:
            # it is the Great Western maximum, not the nineteen-company average). The rows take
            # the dated ladder, the electric track or a class figure, and are decomposed into a
            # continuous head and an overhaul provision inside the same total.
            if not is_multiple_unit(nm):
                A, mtrack = loco_maint(name, eng, yi)
                steam = 'steam' in eng
                share = 0.35 if steam else 0.39
                fixed_share = 0.65 if steam else 0.60
                km = loco_duty(name, yi)
                rho = loco_renewals(yi)
                head = A - rho * A - share * A
                perkm = head * (1.0 - fixed_share) / km
                x.update(maint_a_gbp=round(A, 1),
                         maint_gbp_yr=round(head * fixed_share, 1), maint_year=1900,
                         perkm_gbp=round(perkm, 10), perkm_year=1900)
                x['basis'] = (x.get('basis', '') +
                              ' | maintenance: A %s GBP an engine-year from %s; renewals %.1f '
                              'per cent; works-overhaul provision %.0f per cent; the continuous '
                              'head is %s GBP, split %.0f/%.0f fixed/per-km at the class/era '
                              'distance of %s km a year'
                              % (round(A, 1), mtrack, 100.0 * rho, 100.0 * share,
                                 round(head, 1), 100.0 * fixed_share,
                                 100.0 * (1.0 - fixed_share), format(int(km), ','))).strip(' |')
        elif freight and 'passagiere' in freight:       # carriage
            base = interp(CARRIAGE_PTS, intro or 1910)
            mods = []
            f = vehicle_features().get(nm, {})
            cat = _flag(f, 'catering')
            if cat in ('dining', 'kitchen') or (
                    not cat and any(t in nm for t in ('dining', 'restaurant', 'kitchen'))):
                base *= DINING_MULT
                mods.append('dining/kitchen x1.45')
            elif cat == 'buffet' or (not cat and 'buffet' in nm):
                base *= 1.15
                mods.append('buffet x1.15')
            bogie = _flag(f, 'bogie')
            if bogie in ('yes', 'y', 'true', '1') or (not bogie and 'bogie' in nm):
                base *= 1.19
                mods.append('bogie x1.19')
            panel = _flag(f, 'panelling')
            if panel == 'steel' or (not panel and 'steel' in nm):
                base *= 1.25
                mods.append('steel panelling x1.25')
            fm, fparts = carriage_premiums(nm)
            if fparts:
                base *= fm
                mods.extend(fparts)
            basis = 'carriage interpolation from measured points 1846-1982 (1900 GBP): 234, 1433, 1146, 1238, 1192, 1242, 2871'
            if mods:
                basis += ' | ' + ', '.join(mods)
            x.update(capital_gbp=round(base, 0), year=1900, basis=basis)
            x.update(maint_gbp_yr=round(interp_log(CARRIAGE_MAINT_LADDER, intro or 1900), 1),
                     maint_year=1900,
                     basis=basis + ' | rail carriage maintenance ladder (pass 43, re-based on '
                           'pass 51): 33, 39, 121, 265, 460 and 440 GBP a vehicle-year at 1900, '
                           '1920, 1950, 1970, 1990 and 2020')
        elif 'post' in freight or any(k in nm for k in ('mail', 'tpo', 'brake', 'parcel', 'luggage')):
            # Non-passenger carriage stock: a mail or TPO vehicle is a carriage body without
            # seats, a brake van is simpler still. Priced as a fraction of the carriage ladder,
            # because the body, running gear and bogies are the same.
            if 'brake' in nm:
                f, label = 0.50, 'brake van at half the carriage ladder'
            elif 'luggage' in nm or 'parcel' in nm:
                f, label = 0.60, 'parcels/luggage van at 0.60'
            else:
                f, label = 0.75, 'mail or TPO vehicle at 0.75 of the carriage ladder'
            base = interp(CARRIAGE_PTS, intro or 1910) * f
            x.update(capital_gbp=round(base, 0), year=1900, basis=label)
            x.update(maint_gbp_yr=round(interp_log(CARRIAGE_MAINT_LADDER, intro or 1900) * f, 1),
                     maint_year=1900,
                     basis=label + ' | rail carriage maintenance ladder (pass 43, re-based on '
                           'pass 51): 33, 39, 121, 265, 460 and 440 GBP a vehicle-year at 1900, '
                           '1920, 1950, 1970, 1990 and 2020, scaled by the same factor')
        else:
            try:
                tons = float(sp.get('payload') or cap or 0)
            except (TypeError, ValueError):
                tons = 0
            if tons > 0:
                wcap = tons * WAGON_PER_TON
                x.update(capital_gbp=round(wcap, 0), year=1900,
                         basis='payload x Shildon 1906 mean 7.2 GBP/ton nominal = 7.07 GBP/ton at 1900 (measured range 6.2-8.2)')
                x.update(maint_gbp_yr=round(
                    interp_log(WAGON_MAINT_LADDER, intro or 1900)
                    * (tons / 10.0) ** 0.4, 1), maint_year=1900,
                    basis='rail wagon maintenance ladder (pass 43): 4.2, 8.7, 14.3, 24.8 and 23.8 '
                          'GBP a 10-tonne wagon-year at 1900, 1950, 1970, 1990 and 2020, scaled by '
                          '(payload/10)^0.4; replaces the 8-per-cent-of-capital rule')
    elif cls == 'tram-vehicles':
        if re.search(r'(middle|rear|panto|bogie|motor)', nm):
            # An articulated tram is modelled as separate sections, and the .dat puts the whole
            # vehicle price on the leading section with zero on the rest. The class target must
            # do the same or a six-section tram is priced six times over.
            x.update(capital_gbp=0, year=1900,
                     basis='articulated tram section: the leading section carries the whole '
                           'vehicle price, matching the .dat convention')
            x.update(maint_gbp_yr=0, maint_year=1900,
                     basis='articulated tram section: maintenance carried by the leading section')
            return x
        cap = sp.get('payload_sum') or sp.get('capacity')
        # The modern anchors are whole-vehicle prices, so the seat exponent must not be applied
        # to them: a modern LRV's front section seats fewer than the whole tram carries.
        scale_cap = None if (intro or 0) >= 1990 else cap
        tram = capital_ladder('tram', intro, scale_cap)
        tparts = []
        tm, tmods = tram_premiums(nm)
        if tmods and (intro or 0) < 1990:
            # The modern anchors are already prices for articulated LRVs, so the articulation
            # premium would double count them.
            tram *= tm
            tparts = tmods
        total = tram_maint(intro or 1929)
        modern = (intro or 0) >= 1990
        km = TRAM_REF_MODERN if modern else TRAM_REF_HISTORIC
        renewals = 0.0 if modern else 0.35
        prov = 0.06 if modern else (0.18 if (intro or 0) >= 1950 else 0.28)
        head = total - renewals * total - prov * total
        perkm = head * (1.0 - ROAD_MAINT_FIXED_SHARE) / km
        x.update(capital_gbp=round(tram, 0), year=1900,
                 basis='tram ladder: measured points 670 GBP (1900) for a 1902 municipal car, '
                       '904 at 1929, 24,026 at 1996 (Croydon CR4000) and 24,500 at 2026; the '
                       'modern LRV is a different machine, not inflation; the era itself is '
                       'carried by the vehicle purchase index' +
                       ((' | ' + ', '.join(tparts)) if tparts else ''))
        x.update(maint_a_gbp=round(total, 1),
                 maint_gbp_yr=round(head * ROAD_MAINT_FIXED_SHARE, 1), maint_year=1900,
                 perkm_gbp=round(perkm, 6), perkm_year=1900)
        x['basis'] = (x['basis'] + ' | maintenance %.0f GBP a car-year gross in 1900 money; '
                      'renewals %.0f per cent; works-overhaul provision %.0f per cent; the '
                      'continuous head is %.0f GBP, split %.0f/%.0f between the per-km charge '
                      'and a standing charge at %.0f km a year. Historic series from the '
                      'Ministry of Transport car-only returns, 1923-1933 measured and 1900, '
                      '1913, 1937-1939 and 1949-50 derived; 1960-1990 is an estimate of 150 '
                      'GBP (band 120-250). Modern value from the Nottingham 2011 contract, '
                      'GBP 118,657 nominal for 37 trams over 23 years, at 90,000 km and zero '
                      'renewals. Research pass 47.'
                      % (total, renewals * 100, prov * 100, head,
                         (1.0 - ROAD_MAINT_FIXED_SHARE) * 100,
                         ROAD_MAINT_FIXED_SHARE * 100, km))
    elif cls == 'road-vehicles':
        pwr = sp.get('power')
        eng0 = str(sp.get('engine', '')).lower()
        if not pwr and re.search(r'\((rear|centre)\)', nm):
            # An articulated bus is two vehicle objects; the leading object carries the whole
            # purchase price and maintenance, as for articulated tram sections. Without this
            # guard the unpowered passenger section fell through to the horse-drawn ladder.
            x.update(capital_gbp=0, year=1900, maint_gbp_yr=0.0, maint_year=1900,
                     basis='rear section of an articulated road vehicle: the leading section '
                           'carries the whole purchase price and maintenance (pakset convention, '
                           'as for articulated tram sections)')
            return x
        if 'horse' in nm and eng0 == 'bio':
            # Only the animals: the Scammell mechanical horse is a petrol tractor and its
            # trailers are unpowered, so a plain name test would price both as horses.
            x.update(capital_gbp=round(horse_price(name), 0), year=1900,
                     basis='horse breed/type ladder (1900 GBP): pony 25, hackney 45, coach 77, '
                           'draught 110-135; double = pair')
            x.update(maint_gbp_yr=HORSE_KEEP_YR, maint_year=1900,
                     basis='London horse-keep accounts 1876-97: about 45 GBP/yr (band 28-60) at '
                           '1900, excluding the horsekeeper')
        elif not pwr and ('passagiere' in str(sp.get('freight', '')).lower() or 'coach' in nm):
            kind = horse_pax_class(nm)
            cap = horse_pax_capital(kind)
            x.update(capital_gbp=round(cap, 0), year=1900,
                     basis='horse-drawn passenger ladder (%s): %s; not scaled by capacity, '
                           'because the measured prices do not connect price to seating and a '
                           '4-seat mail coach cost as much as a 10-seat stage coach '
                           '(ai/temp/road-pass-stagecoach.md)' % (kind, HORSE_PAX_NOTE[kind]))
            x.update(maint_gbp_yr=round(horse_pax_maintenance(kind), 1), maint_year=1900,
                     basis=x['basis'] + ' | ' + HORSE_PAX_MAINT_NOTE[kind])
        elif not pwr and 'trailer' in nm and (intro or 0) >= 1896:
            # A towed trailer: no engine, but it wears on tyres, brakes, suspension, body and
            # coupling exactly as the tractor does. The FTA 2016 table is the only measured
            # split found and it puts the trailer at 5.72p a mile against the tractor's 10.41,
            # so the trailer carries 35 per cent of the combination's maintenance and 30 per
            # cent of its capital (a semi-trailer is about a quarter to a third of a new
            # combination). Payload is capped at 30 tons, the heaviest real combination, because
            # the ladder above that prices a rigid vehicle that does not exist. Before 1896 a
            # trailer was horse-drawn and stays on the cart ladder.
            freight = str(sp.get('freight', '')).lower()
            cap = sp.get('payload_sum') or sp.get('capacity') or sp.get('payload')
            try:
                capf = float(cap) if cap is not None else 5.0
            except (TypeError, ValueError):
                capf = 5.0
            if 'post' in freight:
                capf *= 0.01
            if 'bucher' in freight or 'autos' in freight:
                capf *= 0.1
            capf = min(max(capf, 0.5), 30.0)
            tractor = TRACTOR_K * tractor_gcw(intro) ** TRACTOR_EXP
            x.update(capital_gbp=round(tractor * tractor_trailer_ratio(intro), 0), year=1900,
                     basis='towed trailer: %.1f per cent of the combination in capital, taken '
                           'from the measured tractor-to-trailer pairs (1996 20.7 per cent, RHA '
                           '2024 21.0, RHA 2026 19.0; mechanical horses 45)' %
                     (tractor_trailer_ratio(intro) / (1.0 + tractor_trailer_ratio(intro)) * 100))
            perkm = interp(ROAD_PERKM_LORRY, intro or 1955) * \
                (capf / 5.0) ** ROAD_PERKM_SIZE_LORRY * ROAD_TRAILER_MAINT_SHARE
            total_yr = perkm / 240.0 * ROAD_REF_KM['lorry']
            x.update(perkm_gbp=round(perkm * (1.0 - ROAD_MAINT_FIXED_SHARE) / 240.0, 6),
                     perkm_year=1900,
                     maint_gbp_yr=round(total_yr * ROAD_MAINT_FIXED_SHARE, 1), maint_year=1900)
            x['basis'] = (x['basis'] + ' | maintenance %.2f d/km for the trailer alone, %.0f per '
                          'cent of the tractor-and-trailer combination (FTA 2016 split 5.72p '
                          'trailer against 10.41p tractor); %.0f per cent of it into the per-km '
                          'charge and %.0f per cent into the standing charge (ESTIMATE)'
                          % (perkm, ROAD_TRAILER_MAINT_SHARE * 100,
                             (1.0 - ROAD_MAINT_FIXED_SHARE) * 100, ROAD_MAINT_FIXED_SHARE * 100))
        elif not pwr:
            cap = sp.get('payload_sum') or sp.get('capacity') or sp.get('payload')
            try:
                capf = float(cap) if cap is not None else 2.0
            except (TypeError, ValueError):
                capf = 2.0
            capf = max(capf, 1.0)
            cart = 50.0 * (capf / 2.0) ** 0.5
            x.update(capital_gbp=round(cart, 0), year=1900,
                     basis='unpowered horse-drawn cart/wagon: 50 GBP (1900) for a 2-unit cart, '
                           'scaled by payload^0.5')
            x.update(maint_gbp_yr=round(cart * 0.05, 1), maint_year=1900,
                     basis='cart maintenance 5% of capital a year; the horse itself is costed '
                           'separately at the London keep rate')
        else:
            freight = str(sp.get('freight', '')).lower()
            cap = sp.get('payload_sum') or sp.get('capacity') or sp.get('payload')
            try:
                capf = float(cap) if cap is not None else None
            except (TypeError, ValueError):
                capf = None
            if capf is not None and 'post' in freight:
                # Post vehicles carry mail bags, ten to the tonne: a 100-unit steam mail van is
                # a one-ton van, not a 100-tonner. The .dat payload is a count of bags.
                capf = capf * 0.01
            if capf is not None and ('bucher' in freight or 'autos' in freight):
                # Books and motor cars are counted in units, not tonnes. In this pakset a
                # Bucher payload of 3 is an Austin Seven van and 11 a Transit, so a unit is
                # about a tenth of a tonne.
                capf = capf * 0.1
            if 'passagiere' in freight and (capf is None or capf >= 10):
                kind = 'bus'
            elif 'passagiere' in freight:
                kind = 'car'
            elif capf and capf > 0:
                kind = 'lorry'
            else:
                kind = 'car'
            base = capital_ladder(kind, intro, capf)
            eng2 = str(sp.get('engine', '')).lower()
            tractor = None
            if not freight and 'steam' not in eng2:
                # Articulated tractor unit: no goods of its own, so no payload to scale by.
                # It is priced directly on the measured chassis-cab prices by gross combination
                # weight, and it carries the tractor's share of the combination's maintenance.
                tractor = TRACTOR_K * tractor_gcw(intro) ** TRACTOR_EXP
                base = tractor
                f, lab = 1.0, ('tractor-unit ladder: 36.5 x GCW^%.2f in 1900 GBP, fitted to 1933-'
                               '2026 chassis-cab prices; nominal GCW %.1f tons for this era'
                               % (TRACTOR_EXP, tractor_gcw(intro)))
            elif 'diesel' in eng2:
                f, lab = ROAD_DIESEL, 'diesel x1.17'
            elif 'battery' in eng2:
                if kind == 'car':
                    bm, bl = ROAD_BATTERY_VAN, 'battery-electric x1.25 on the diesel price (van pairs 1.03-1.47)'
                elif 'coach' in nm:
                    bm, bl = ROAD_BATTERY_COACH, 'battery-electric x1.50 on the diesel price (coach class)'
                else:
                    bm, bl = ROAD_BATTERY, 'battery-electric x2.10 on the diesel price (heavy vehicles and buses cluster at 2.0-2.2)'
                f = ROAD_DIESEL * bm
                lab = bl
            elif 'electric' in eng2:
                f, lab = ROAD_TROLLEY, 'electric/trolleybus x1.14'
            elif 'steam' in eng2:
                base = ROAD_STEAM_LADDER['anchor'] * (max(capf or 1.0, 0.5) ** ROAD_STEAM_LADDER['exp'])
                f, lab = 1.0, 'steam: own ladder 300 x payload^0.464 (six measured steam wagons ' \
                              '1901-33, mean abs error 11 per cent); the petrol/diesel mix ' \
                              'normalisation does not apply'
            else:
                f, lab = 1.0, 'petrol'
            base = base * f / (1.0 if ('steam' in eng2 or tractor) else ROAD_MIX_NORM)
            ml = interp(ROAD_MODERN_LEVEL, intro or 1950)
            if ml != 1.0 and not tractor:
                # The tractor ladder is fitted across 1933-2026, so the modern real level is
                # already inside its constant; applying it again would double count.
                base *= ml
                lab += '; modern level x%.2f' % ml
            rfm, rparts = road_premiums(nm, kind)
            if rparts:
                base *= rfm
            basis = ('road ladder (%s): %s | %s' % (kind, ROAD_LADDER_NOTE[kind], lab))
            if rparts:
                basis += ' | ' + ', '.join(rparts)
            x.update(capital_gbp=round(base, 0), year=1900, basis=basis)
            # Maintenance: a measured per-kilometre total, split between the distance-driven
            # bill and a standing allowance. The split is an estimate; see the constants.
            if tractor:
                perkm = interp(ROAD_PERKM_LORRY, intro or 1955) * \
                    ((tractor_gcw(intro) / 1.45) / 5.0) ** ROAD_PERKM_SIZE_LORRY * \
                    ROAD_TRACTOR_MAINT_SHARE
                ref_km = ROAD_REF_KM['lorry']
            elif kind == 'bus':
                perkm = interp(ROAD_PERKM_BUS, intro or 1930) * \
                    (max(capf or 50.0, 4.0) / 50.0) ** ROAD_PERKM_SIZE_BUS
                ref_km = ROAD_REF_KM['bus']
            else:
                perkm = interp(ROAD_PERKM_LORRY, intro or 1955) * \
                    (max(capf or 5.0, 0.2) / 5.0) ** ROAD_PERKM_SIZE_LORRY
                ref_km = ROAD_REF_KM['lorry'] if (capf or 0) >= 2.0 else ROAD_REF_KM['van']
            total_yr = perkm / 240.0 * ref_km
            x.update(perkm_gbp=round(perkm * (1.0 - ROAD_MAINT_FIXED_SHARE) / 240.0, 6),
                     perkm_year=1900,
                     maint_gbp_yr=round(total_yr * ROAD_MAINT_FIXED_SHARE, 1), maint_year=1900)
            x['basis'] = (x['basis'] + ' | maintenance %.2f d/km in 1900 money, size^%.2f: '
                          '%.0f per cent into the per-km charge and %.0f per cent into the '
                          'standing charge (ESTIMATE, band 15-35) at %.0f km a year; total '
                          '%.0f GBP a year, %.0f per cent of capital'
                          % (perkm, ROAD_PERKM_SIZE_BUS if kind == 'bus' else ROAD_PERKM_SIZE_LORRY,
                             (1.0 - ROAD_MAINT_FIXED_SHARE) * 100,
                             ROAD_MAINT_FIXED_SHARE * 100, ref_km, total_yr,
                             (total_yr / base * 100.0) if base else 0.0))
    elif cls == 'water-vehicles':
        # Per-gross-ton capital ladder (the 2026-11-25 decision), from research reports 25, 56
        # and 57. Where a tonnage exists it supersedes the capacity ladder below. The capacity
        # ladder remains for hovercraft (no gross tonnage exists), holds (the parent carries the
        # hull) and the hulls the tonnage passes could not identify.
        wc = water_capacity().get(nm)
        if wc and wc['kind'] == 'hold':
            x.update(capital_gbp=0, year=1900, maint_gbp_yr=0.0, maint_year=1900,
                     basis='hold object: the parent hull carries the whole cost (pakset convention; '
                           'the holds are part of the hull advertised outfit)')
            return x
        gt_price, gt_basis = water_gt_price(nm)
        if gt_price is not None:
            x.update(capital_gbp=round(gt_price, 2), year=1900,
                     basis='water (per-gross-ton capital ladder, research reports 25, 56 and 57): '
                           + gt_basis)
            x.update(maint_gbp_yr=round(gt_price * SHIP_MAINT_RATIO, 1), maint_year=1900,
                     basis=x['basis'] + ' | maintenance 2% of capital a year (1850 GSN comparison)')
            return x
        if wc:
            pax, cargo, typ = wc['pax'], wc['cargo'], wc['type']
            engine = str(sp.get('engine', '')).lower()
            wt = float(sp.get('weight') or 0)
            pwr2 = float(sp.get('power') or 0)
            parts = []
            if typ == 'tug':
                if engine == 'bio' or pwr2 <= 2:
                    price = 100.0
                    parts.append('horse-drawn craft: flat 100 GBP')
                else:
                    price = max(200.0, SHIP_TUG_PER_HP * pwr2)
                    parts.append('tug at %g GBP/hp (single 1882 tug point; assumption)'
                                 % SHIP_TUG_PER_HP)
            elif typ in ('cargo', 'coaster'):
                rate = SHIP_COASTER_T if typ == 'coaster' else SHIP_CARGO_T
                price = rate * cargo
                parts.append('%s at %g GBP/t cargo' % (typ, rate))
            elif typ in ('barge', 'narrowboat', 'other'):
                if typ == 'other' and pax >= 10 and cargo < 1:
                    price = SHIP_PAX_ESTUARY * pax
                    parts.append('small passenger craft at %g GBP/passenger' % SHIP_PAX_ESTUARY)
                else:
                    rate = {'steam': SHIP_INLAND_STEAM_T, 'diesel': SHIP_INLAND_MOTOR_T,
                            'sail': SHIP_INLAND_SAIL_T}.get(engine, SHIP_INLAND_HORSE_T)
                    price = rate * cargo
                    parts.append('%s inland craft at %g GBP/t cargo' % (engine or 'unpowered', rate))
                    if pax:
                        price += SHIP_PAX_ESTUARY * pax
                        parts.append('%g GBP/passenger' % SHIP_PAX_ESTUARY)
            elif typ in ('ferry', 'river-boat', 'hovercraft'):
                if typ == 'hovercraft':
                    price = SHIP_HOVERCRAFT_PAX * pax + SHIP_CARGO_T * cargo
                    parts.append('hovercraft at %g GBP/passenger (assumption)'
                                 % SHIP_HOVERCRAFT_PAX)
                elif typ == 'river-boat' or not (
                        cargo > 10 or wt >= 2000 or (intro and intro >= 1960 and pax >= 500)):
                    price = SHIP_PAX_RIVER * pax + SHIP_CARGO_T * cargo
                    parts.append('river/estuary passenger vessel at %g GBP/passenger'
                                 % SHIP_PAX_RIVER)
                else:
                    price = SHIP_PAX_SEA * pax + SHIP_VEHICLE_T * cargo
                    parts.append('sea-going/vehicle ferry at %g GBP/passenger + %g GBP/t cargo'
                                 % (SHIP_PAX_SEA, SHIP_VEHICLE_T))
            else:
                price = SHIP_CARGO_T * cargo + SHIP_PAX_RIVER * pax
                parts.append('water craft at %g GBP/t cargo + %g GBP/passenger'
                             % (SHIP_CARGO_T, SHIP_PAX_RIVER))
            if typ in ('cargo', 'coaster', 'ferry', 'river-boat') and engine == 'diesel':
                price *= 1.15
                parts.append('diesel x1.15')
            price = max(price, 20.0)
            x.update(capital_gbp=round(price, 0), year=1900,
                     basis='water capacity ladder (research pass 25): ' + ', '.join(parts))
            x.update(maint_gbp_yr=round(price * SHIP_MAINT_RATIO, 1), maint_year=1900,
                     basis=x['basis'] + ' | maintenance 2% of capital a year (1850 GSN comparison)')
        else:
            ship_cap = capital_ladder('ship', intro)
            x.update(capital_gbp=round(ship_cap, 0), year=1900,
                     basis='ship ladder: median measured whole-ship price 38,958 GBP (1900) at 1909, '
                           'flat; no capacity record for this object, so the flat whole-ship figure stands')
            x.update(maint_gbp_yr=round(ship_cap * SHIP_MAINT_RATIO, 1), maint_year=1900,
                     basis=x['basis'] + ' | maintenance 2% of capital a year (1850 GSN comparison)')
    elif cls == 'air-vehicles':
        # Hedonic fit on 116 priced aircraft: seats, engines, engine type, wide body and year.
        # Attributes come from the general vehicle feature table, which is a specification.
        d = vehicle_features().get(nm, {})

        def _f(v, default):
            try:
                return float(v)
            except (TypeError, ValueError):
                return default

        seats = _f(d.get('seats'), 0) or (air_seats(name) or 115.0)
        engines = _f(d.get('engines'), 4.0)
        etype = str(d.get('engine_type') or 'turbojet').strip().lower()
        wide = str(d.get('wide_body') or '').strip().lower() in ('yes', 'y', 'true', '1')
        y = intro or 1960
        price = (AIR_HEDONIC['k'] * seats ** AIR_HEDONIC['seats']
                 * engines ** AIR_HEDONIC['engines']
                 * AIR_TYPE.get(etype, AIR_TYPE['turbojet']))
        if wide:
            price *= AIR_HEDONIC['wide']
        price *= AIR_HEDONIC['year'] ** (y - AIR_HEDONIC['y0'])
        x.update(capital_gbp=round(price, 0), year=1900,
                 basis=('aircraft hedonic: seats^0.867 x engines^0.768 x %s x %s x 1.0111^(year-1959); '
                        '%0.0f seats, %0.0f engines, %s%s'
                        % (etype, 'wide-body x1.22' if wide else 'narrow body', seats, engines,
                           etype, ', wide body' if wide else '')))
        x.update(maint_gbp_yr=round(price * AIR_MAINT_RATIO, 1), maint_year=1900,
                 basis=x['basis'] + ' | maintenance 20% of capital a year (BOAC VC10 1969/70 '
                       'GBP 49,057 a year against a VC10 capital of GBP 209,085)')
    elif 'horse' in nm and 'vehicle' in (cls or ''):
        x.update(maint_gbp_yr=HORSE_KEEP_YR, maint_year=1900,
                 basis='London horse-keep accounts 1876-97: about 45 GBP/yr (band 28-60) at 1900, excluding the horsekeeper')

    # infrastructure: measured-derived values only (measured_infra.py).
    # The class column must never take a current .dat price as an input: see
    # ai/temp/discarded-dat-derived.md. Objects with no measured rate stay blank.
    mv = measured_infra().get(name)
    if mv:
        if mv.get('capital_gbp') is not None:
            x.setdefault('capital_gbp', mv['capital_gbp'])
            x.setdefault('year', 1900)
        if mv.get('maint_gbp_yr') is not None:
            x.setdefault('maint_gbp_yr', mv['maint_gbp_yr'])
            x.setdefault('maint_year', 1900)
        x['basis'] = (x.get('basis', '') + ' | ' + mv['basis']).strip(' |')
        if mv.get('maint_basis'):
            x['basis'] = (x['basis'] + ' | maintenance: ' + mv['maint_basis']).strip(' |')
    # maintenance: synthesis values, which are measured-anchored (Hill, BR 1966, ORR,
    # Cudworth). Checked against the current values: way slope 0.06, R2 0.00; bridge 0.12;
    # station 0.21; only tunnels inherit the current ordering (slope 0.48, R2 0.60), so tunnel
    # maintenance is withheld pending a measured series.
    # Annual real maintenance per km = .dat x 0.00792622 x 12 (the monthly figure already
    # includes the engine's x2 monthly adjustment).
    if cls not in ('tunnels', 'stops-stations/piers'):
        rec = synth_recommendations().get(name)
        if rec and rec.get('rec_maint'):
            x.setdefault('maint_gbp_yr', round(rec['rec_maint'] * 0.00792622 * 12, 1))
            x.setdefault('maint_year', 1900)
            x['basis'] = (x.get('basis', '') + ' | maintenance: ' +
                          rec.get('note', 'infrastructure-cost-synthesis.md')).strip(' |')
    if cls and str(cls).endswith('vehicles') and x:
        apply_adjustment(name, x)
    return x or None

_meas = None
def measured_infra():
    global _meas
    if _meas is None:
        _meas = {}
        p = os.path.join(HERE, 'measured-infrastructure.csv')
        if os.path.exists(p):
            with open(p, encoding='utf-8-sig') as f:
                for r in csv.DictReader(f):
                    try:
                        gbp = float(r['capital_gbp'])
                    except (TypeError, ValueError):
                        gbp = None
                    try:
                        mnt = float(r['maint_gbp_yr'])
                    except (TypeError, ValueError):
                        mnt = None
                    if gbp is None and mnt is None:
                        continue
                    _meas[r['name']] = {'capital_gbp': gbp, 'maint_gbp_yr': mnt,
                                        'basis': r.get('basis', ''),
                                        'maint_basis': r.get('maint_basis', '')}
    return _meas

_synth = None
def synth_recommendations():
    global _synth
    if _synth is None:
        _synth = {}
        if os.path.exists(SYNTH):
            with open(SYNTH, encoding='utf-8-sig') as f:
                for r in csv.DictReader(f):
                    nm = (r.get('obj_name') or '').strip()
                    if not nm:
                        continue
                    def n(k):
                        try:
                            return float(str(r.get(k, '')).replace(',', ''))
                        except ValueError:
                            return None
                    _synth[nm] = {'rec_cost': n('rec_cost'), 'rec_maint': n('rec_maint'),
                                  'note': r.get('note', '')}
    return _synth

# ---------------------------------------------------------------- tabs
def tabs():
    ordered = [
        ('Rail vehicles', 'rail-vehicles'),
        ('Road vehicles', 'road-vehicles'),
        ('Tram vehicles', 'tram-vehicles'),
        ('Water vehicles', 'water-vehicles'),
        ('Air vehicles', 'air-vehicles'),
        ('Narrow gauge vehicles', 'narrowgauge-vehicles'),
        ('Maglev vehicles', 'maglev-vehicles'),
        ('Ways - rail', 'ways/rail'),
        ('Ways - road', 'ways/road'),
        ('Ways - water', 'ways/water'),
        ('Ways - tram', 'ways/tram'),
        ('Ways - narrow gauge', 'ways/narrowgauge'),
        ('Ways - air', 'ways/air'),
        ('Ways - maglev', 'ways/maglev'),
        ('Ways - power', 'ways/power'),
        ('Bridges & viaducts', 'bridges'),
        ('Tunnels', 'tunnels'),
        ('Way objects (electrification)', 'way-objects'),
        ('Signals', 'signals'),
        ('Signalboxes', 'signalboxes'),
        ('Roadsigns', 'roadsigns'),
        ('Stations & bus stops', 'stops-stations/stations'),
        ('Piers & docks', 'stops-stations/piers'),
        ('Depots', 'depots'),
        ('Engine settings', 'engine-settings'),
    ]
    out = []
    for sheet, cls in ordered:
        out.append((sheet, (lambda c: (lambda r: r.get('class') == c))(cls)))
    return out

def readme_extra():
    return [
        'TYPE SHEETS: one per object class (register: New/ai/cost-balancing-register.md).',
        'Goods objects are excluded: their value[] fields are revenue rates, not costs.',
        'Objects with no cost field of any kind (citycars, pedestrians, trees, city buildings,',
        'industry buildings, HQ buildings, crossings) have no row; their costs, where charged at',
        'all, come through the Engine settings sheet (cost_* / cst_* / forge_cost_*).',
        '23 station buildings with no cost line are priced by cost_multiply_* x level and are',
        'noted on the Stations sheet where identified.',
        'WATER: priced by capacity, not the flat whole-ship ladder. Passenger vessels GBP/passenger',
        '(sea-going 66, river 16.7, estuary 10); cargo GBP 8.5/t; inland GBP 8-32/t by engine;',
        'vehicle ferries +GBP 200/t; tugs GBP 40/hp; holds zero. Source: research pass 25.',
        'FEATURES: the class ladders carry measured option premiums where the feature table records',
        'the option (automatic 1.15, air suspension 1.06, aircon 1.08 road / 1.10 rail, low floor',
        '1.03, corridor 1.02, sleeping 2.2, tram articulation 1.30, and the earlier diesel/dining/',
        'bogie/steel/steam factors). A blank feature cell is the baseline. Source: research pass 8.',
        'PIERS: the 111 bridge-substructure pier objects are deliberately unpriced. The measured',
        'substructure share is 16-82% of bridge cost and depends on pier height and span, so one',
        'share would be wrong for most bridges (research pass 13 section 6).',
        'THE COSTING PASS: nothing in these sheets is applied to the .dat files. These sheets are',
        'the research store; copying their values into the .dat files is the costing pass, one',
        'operation, run only when the research is complete and the sheets hold the final figures',
        '(user direction 2026-11-24). Corrections found before then accumulate here.',
        'CANALS: deliberate zero forge and zero renewal. For a canal there is no way surface - the',
        'forging is the building, and it differs by canal class (ship canal against tub-boat',
        'canal), so the formation is folded into the per-class way cost and forge_cost_water goes',
        'to 0 at the costing pass (decision 2026-11-24). The suggested canal values are the whole',
        'construction and are unchanged by the fold.',
        'SIGNALS: one signal object is one signal in reality (post with its arms or lamps); the',
        'general signalling infrastructure is represented by the signalbox cost (decision',
        '2026-11-24). The 168 signal objects are calibrated to the per-post ladder at the pass.',
    ]

def readme_extra_maint():
    return [
        'Fixed = per game month per object (per km per month for length-based ways).',
        'Per-km = vehicle runningcost, per whole vehicle-km. Vehicles fixed_cost is charged at',
        '2x .dat per game month at the pakset settings (see Params FIXED_COST_MONTH_FACTOR).',
        'Maintenance source figures given per mile are converted to per km when entered',
        '(divide by MILES_TO_KM); the notes column records the original figure.',
        'THE COSTING PASS: nothing here is applied to the .dat files until the research is',
        'complete and the sheets hold the final figures (user direction 2026-11-24).',
        'CANALS: canal ways carry no wear and are not renewed, so their maintenance is upkeep',
        'only and carries no renewal element (decision 2026-11-24).',
    ]
