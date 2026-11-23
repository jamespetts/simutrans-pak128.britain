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
BASE = os.path.dirname(os.path.dirname(HERE))
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
                elif k in ('freight', 'capacity', 'weight', 'power', 'engine', 'engine_type', 'payload'):
                    n = re.match(r'^-?[0-9.]+', v)
                    cur['engine' if k == 'engine_type' else k] = float(n.group(0)) if n else v
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
TRAM_MAINT = 64.0          # car only, 1913-14, excluding track and electrical supply
# Modern light rail maintenance is a different order. The only measured contract for rolling
# stock alone is Nottingham, 2011: GBP 101m over 23 years for 37 trams = GBP 118,657 a tram-year,
# corroborated by Alstom's EUR 120m (EUR 141k a tram-year). In 1900 money that is GBP 1,301.
# Nothing measures 1950-1990, so the break is placed at 1990, where the LRV generation begins.
TRAM_MAINT_TOTAL = [(1900, 64.0), (1990, 64.0), (2011, 1301.0), (2026, 1301.0)]
# Reference annual distance, km: a 1920s car ran about 30,000 miles; the Nottingham figure
# assumes 90,000 km a tram-year.
TRAM_REF_KM = [(1900, 48000.0), (1990, 48000.0), (2011, 90000.0), (2026, 90000.0)]
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
    return bool(re.search(r'dmu|emu|demu|railcar|\bapt\b|multiple.?unit|tyneside-unit', nm))

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
    if nm.endswith('-double') or '-double-' in nm or 'pair' in nm:
        base *= 2
    return base
WAGON_PER_TON = 7.07      # Shildon 1906 mean 7.2 nominal = 7.07 at 1900 (range 6.2-8.2)
HORSE_KEEP_YR = 45.0      # London accounts 1876-97, band 28-60 (1900 GBP/yr)
TRAM_PERKM = 0.0045       # MoT returns 1913-30: 0.91-1.28 d/car-km at 1900 = 0.0038-0.0053 GBP
LOCO_REPAIR_PERKM = 0.0067  # Hill 1892 19-company average 1.61 d/km at 1900 (band 0.0039-0.0118)
LOCO_MAINT_YR = 253.0     # Hill: 253 GBP per engine-year at 1900 (~12% of price)
CARRIAGE_MAINT_YR = 32.6  # Hill: 18.6-46.7 GBP per vehicle-year at 1900

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
    'maglev-vehicles':    ('no', 'no', 'no'),
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
# Overhaul and upgrade profiles, by class. Shares are of the vehicle's own capital target.
#   initial / max       cost of the first and the late-life overhaul, as a share of capital
#   n                   overhauls before the cost reaches the maximum
#   interval_km         distance between overhauls
#   months              time out of service per overhaul
#   upgrade             net cost of replacing an old vehicle with this type, as a share of the
#                       new vehicle's capital (a trade-in price, not the new price)
# These are placeholders pending research pass 36/37 and are the single place to change.
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
    # half a new bus, so 50 per cent.
    'bus':            (0.25, 0.40, 3, 220000.0, 0.5, 0.50),
    'tram':           (0.08, 0.45, 3, 600000.0, 0.5, 0.50),
    'lorry':          (0.10, 0.30, 3, 160000.0, 0.3, 0.50),
    'van':            (0.10, 0.30, 3, 60000.0, 0.1, 0.50),
    'ship':           (0.02, 0.05, 6, 0.0, 0.4, 0.50),
    'aircraft':       (0.025, 0.05, 4, 0.0, 0.8, 0.50),
    'horse':          (0.00, 0.00, 0, 0.0, 0.0, 0.50),
}

OVERHAUL_CLASS = [
    (r'^(br-|lner|lms|gwr|sr-|ner-|lnwr|lbscr|gnr|nbr|ger|secr|mr-|cr-)', 'locomotive'),
]


def overhaul_profile(cls, name, capital_gbp, intro):
    """Suggested overhaul and upgrade figures for one vehicle, in 1900 GBP."""
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
    s0, smax, n, km, months, up = OVERHAUL_PROFILE[key]
    cap = capital_gbp or 0.0
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

    if cls in ('rail-vehicles', 'narrowgauge-vehicles', 'maglev-vehicles'):
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
                diesel = any(t in eng for t in ('diesel', 'electric', 'turbine')) \
                    or cls == 'maglev-vehicles'
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
            x.update(maint_gbp_yr=LOCO_MAINT_YR, maint_year=1900,
                     perkm_gbp=LOCO_REPAIR_PERKM, perkm_year=1900,
                     basis=(x.get('basis', '') + ' | Hill 1892: 253 GBP/engine-year and 1.61 d/km repair (19-company average) at 1900').strip(' |'))
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
            x.update(maint_gbp_yr=CARRIAGE_MAINT_YR, maint_year=1900,
                     basis=basis + ' | Hill 1892: 18.6-46.7 GBP/vehicle-year (mid 32.6) at 1900')
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
            x.update(maint_gbp_yr=round(CARRIAGE_MAINT_YR * f, 1), maint_year=1900,
                     basis=label + ' | Hill 1892 carriage rate 32.6 GBP/vehicle-year, scaled')
        else:
            try:
                tons = float(sp.get('payload') or cap or 0)
            except (TypeError, ValueError):
                tons = 0
            if tons > 0:
                wcap = tons * WAGON_PER_TON
                x.update(capital_gbp=round(wcap, 0), year=1900,
                         basis='payload x Shildon 1906 mean 7.2 GBP/ton nominal = 7.07 GBP/ton at 1900 (measured range 6.2-8.2)')
                x.update(maint_gbp_yr=round(wcap * 0.08, 1), maint_year=1900,
                         basis='wagon maintenance 8% of capital a year (a 10 t wagon at about '
                               'GBP 71 capital carries about GBP 6 a year)')
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
        total = interp(TRAM_MAINT_TOTAL, intro or 1929)
        km = interp(TRAM_REF_KM, intro or 1929)
        perkm = total * (1.0 - ROAD_MAINT_FIXED_SHARE) / km
        x.update(capital_gbp=round(tram, 0), year=1900,
                 basis='tram ladder: measured points 670 GBP (1900) for a 1902 municipal car, '
                       '904 at 1929, 24,026 at 1996 (Croydon CR4000) and 24,500 at 2026; the '
                       'modern LRV is a different machine, not inflation; the era itself is '
                       'carried by the vehicle purchase index' +
                       ((' | ' + ', '.join(tparts)) if tparts else ''))
        x.update(maint_gbp_yr=round(total * ROAD_MAINT_FIXED_SHARE, 1), maint_year=1900,
                 perkm_gbp=round(perkm, 6), perkm_year=1900)
        x['basis'] = (x['basis'] + ' | maintenance %.0f GBP a car-year in 1900 money, split '
                      '%.0f/%.0f between the per-km charge and a standing charge at %.0f km a '
                      'year: historic 64 GBP (MoT returns 1913-14, car only, track and '
                      'electrical supply excluded); modern 1,301 GBP from the Nottingham 2011 '
                      'contract, GBP 118,657 nominal for 37 trams over 23 years'
                      % (total, (1.0 - ROAD_MAINT_FIXED_SHARE) * 100,
                         ROAD_MAINT_FIXED_SHARE * 100, km))
    elif cls == 'road-vehicles':
        pwr = sp.get('power')
        eng0 = str(sp.get('engine', '')).lower()
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
        # Capacity-based water ladder, research pass 25. The measured per-GT ferry fit
        # (84.1 x GT^0.90, R2 0.992) cannot be applied because GT is not recorded and the
        # measured GT-per-passenger relationship is type-dependent (R2 0.08 within 1924-38).
        # The report's practical route is therefore used: GBP per passenger for passenger
        # vessels, GBP per tonne of cargo for cargo and inland craft, with the measured
        # anchors below. See ai/temp/water-capacity.csv for the capacity of every object.
        wc = water_capacity().get(nm)
        if wc and wc['kind'] == 'hold':
            x.update(capital_gbp=0, year=1900, maint_gbp_yr=0.0, maint_year=1900,
                     basis='hold object: the parent hull carries the whole cost (pakset convention; '
                           'the holds are part of the hull advertised outfit)')
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
    ]

def readme_extra_maint():
    return [
        'Fixed = per game month per object (per km per month for length-based ways).',
        'Per-km = vehicle runningcost, per whole vehicle-km. Vehicles fixed_cost is charged at',
        '2x .dat per game month at the pakset settings (see Params FIXED_COST_MONTH_FACTOR).',
        'Maintenance source figures given per mile are converted to per km when entered',
        '(divide by MILES_TO_KM); the notes column records the original figure.',
    ]
