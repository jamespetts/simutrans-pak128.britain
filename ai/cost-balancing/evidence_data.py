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
    'bus':   dict(anchor=1011.0,   year=1941, b=0.0000, ref=50.0,  exp=0.75),
    'lorry': dict(anchor=183.0,    year=1942, b=0.0000, ref=10.0,  exp=0.60),
    'car':   dict(anchor=234.0,    year=1959, b=0.0000, ref=4.0,   exp=0.40),
    'air':   dict(anchor=196419.0, year=1959, b=0.0200, ref=115.0, exp=0.70),
    'ship':  dict(anchor=38958.0,  year=1909, b=0.0000, ref=None,  exp=0.00),
    'tram':  dict(anchor=904.0,    year=1929, b=0.0000, ref=40.0,  exp=0.50,
                  # structural break, not a trend: the 1880s-1980s cars sit at 904-1,976 and
                  # the 2010s LRVs at 21,380 (2 rows). Interpolate log-linearly, flat outside.
                  pts=[(1929, 904.0), (1985, 1976.0), (2012, 21380.0)]),
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
ROAD_MAINT_BUS = [(1915, 176.0), (1955, 95.0), (1983, 442.0)]
ROAD_MAINT_LORRY = [(1936, 29.0), (1958, 40.0), (1968, 62.0), (2016, 104.0)]
TRAM_MAINT = 64.0          # car only, 1913-14, excluding track and electrical supply
SHIP_MAINT_RATIO = 0.02    # 1850 GSN GBP 788 against a ship capital of about GBP 39,000
AIR_MAINT_RATIO = 0.20     # BOAC VC10 1969/70 GBP 49,057 against a VC10 capital of GBP 209,085
HORSE_VEH_MAINT = 38.0     # 1893-97 horse-only accounts, 29-47

HORSE_PRICE = {
    'pony': 25.0, 'hackney': 55.0, 'freisian': 120.0, 'friesian': 120.0,
    'cleveland': 90.0, 'yorkshire': 90.0, 'irish': 135.0, 'clydesdale': 175.0,
    'shire': 180.0, 'heavy': 135.0, 'coach': 90.0, 'cart': 60.0, 'dray': 60.0,
}
HORSE_DEFAULT = 70.0

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
        for fn in ('vehicle-features.csv', 'vehicle-features-locomotives.csv'):
            p = os.path.join(HERE, fn)
            if os.path.exists(p):
                for row in csv.DictReader(open(p, encoding='utf-8-sig')):
                    nm = (row.get('name') or '').strip().lower()
                    if nm:
                        _features[nm] = row
    return _features

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
    # Freight and post aircraft carry either kilograms (A320 post: 17,800) or goods units
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
    else:
        price = p['anchor'] * math.exp(p['b'] * (y - p['year']))
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

def _name_score(pn, nn):
    """0 = exact; >0 = containment, closer is better; None = reject.
    A containment that changes the digits (Class 45 vs Class 455) is rejected."""
    if not pn or not nn:
        return None
    if pn == nn:
        return 0
    if len(pn) > 8 and pn in nn:
        i = nn.index(pn)
        before = nn[i - 1] if i else ''
        after = nn[i + len(pn)] if i + len(pn) < len(nn) else ''
        if before.isdigit() or after.isdigit():
            return None
        return 2 + (len(nn) - len(pn))
    if len(nn) > 8 and nn in pn:
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
        try:
            price = float(str(pr.get('price', '')).replace(',', ''))
        except ValueError:
            continue
        unit = (pr.get('price_unit') or '').lower()
        yr = re.match(r'^(\d{4})', pr.get('year') or '')
        if not yr:
            continue
        year = int(yr.group(1))
        if pr.get('kind') == 'capital' and 'gbp' in unit:
            if 'capital_gbp' not in out:
                out.update(capital_gbp=price, capital_year=year)
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
            if any(t in nm for t in ('dining', 'restaurant', 'kitchen', 'buffet')):
                base *= DINING_MULT
                mods.append('dining/kitchen x1.45')
            if 'bogie' in nm:
                base *= 1.19
                mods.append('bogie x1.19')
            if 'steel' in nm:
                base *= 1.25
                mods.append('steel panelling x1.25')
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
        x.update(perkm_gbp=TRAM_PERKM, perkm_year=1900,
                 basis='MoT tramway returns 1913-30: 0.91-1.28 d/car-km at 1900 (maintenance and repairs only, narrow scope)')
        cap = sp.get('payload_sum') or sp.get('capacity')
        x.update(capital_gbp=round(capital_ladder('tram', intro, cap), 0), year=1900,
                 basis='tram ladder: anchor points 904 GBP (1900) at 1929, 1,976 at 1985, '
                       '21,380 at 2012 (modern LRVs are a different machine, not inflation), '
                       'seats^0.5; the era itself is carried by the vehicle purchase index')
        x.update(maint_gbp_yr=TRAM_MAINT, maint_year=1900,
                 basis=x['basis'] + ' | maintenance 64 GBP a car-year, car only, 1913-14, '
                       'excluding track and electrical supply')
    elif cls == 'road-vehicles':
        pwr = sp.get('power')
        if 'horse' in nm:
            x.update(capital_gbp=round(horse_price(name), 0), year=1900,
                     basis='horse breed/type ladder (1900 GBP): pony 25, hackney 45, coach 77, '
                           'draught 110-135; double = pair')
            x.update(maint_gbp_yr=HORSE_KEEP_YR, maint_year=1900,
                     basis='London horse-keep accounts 1876-97: about 45 GBP/yr (band 28-60) at '
                           '1900, excluding the horsekeeper')
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
            if 'diesel' in eng2:
                f, lab = ROAD_DIESEL, 'diesel x1.17'
            elif 'electric' in eng2:
                f, lab = ROAD_TROLLEY, 'electric/trolleybus x1.14'
            elif 'steam' in eng2:
                f, lab = ROAD_STEAM, 'steam x1.10'
            else:
                f, lab = 1.0, 'petrol'
            base = base * f / ROAD_MIX_NORM
            x.update(capital_gbp=round(base, 0), year=1900,
                     basis='road ladder (%s): median measured whole-vehicle price in 1900 GBP, '
                           'flat in real terms, size-scaled by capacity | %s' % (kind, lab))
            if kind == 'bus':
                m = interp(ROAD_MAINT_BUS, intro or 1930)
            elif kind == 'lorry':
                m = interp(ROAD_MAINT_LORRY, intro or 1950)
            else:
                m = 0.5 * interp(ROAD_MAINT_LORRY, intro or 1950)
            x.update(maint_gbp_yr=round(m, 1), maint_year=1900,
                     basis=x['basis'] + ' | maintenance %0.0f GBP a vehicle-year (research pass 15)' % m)
    elif cls == 'water-vehicles':
        # The measured water ladder (research pass 25) is ready: ferries 84.1 x GT^0.90 in
        # 1900 GBP, coastal cargo GBP 35/GT, inland craft GBP 17/GT, R2 0.992 on the ferry fit.
        # It cannot be applied yet because no boat .dat carries a capacity or a gross tonnage,
        # and `weight` is a game parameter rather than displacement: a coal box boat is weight
        # 1.0 with payload 17 t, a hovercraft weight 48. The flat ladder stands, flagged.
        ship_cap = capital_ladder('ship', intro)
        x.update(capital_gbp=round(ship_cap, 0), year=1900,
                 basis='ship ladder: median measured whole-ship price 38,958 GBP (1900) at 1909, '
                       'flat; the measured per-GT ladder (ferries 84.1 x GT^0.90, cargo GBP 35/GT, '
                       'inland GBP 17/GT) is ready but no boat records a tonnage or capacity')
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
    if cls != 'tunnels':
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
    ]

def readme_extra_maint():
    return [
        'Fixed = per game month per object (per km per month for length-based ways).',
        'Per-km = vehicle runningcost, per whole vehicle-km. Vehicles fixed_cost is charged at',
        '2x .dat per game month at the pakset settings (see Params FIXED_COST_MONTH_FACTOR).',
        'Maintenance source figures given per mile are converted to per km when entered',
        '(divide by MILES_TO_KM); the notes column records the original figure.',
    ]
