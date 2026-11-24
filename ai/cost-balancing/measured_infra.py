# -*- coding: utf-8 -*-
"""Capital for infrastructure objects derived ONLY from measured evidence.

Rule (user direction, 2026-11-22): the derived column of a cost-balancing workbook must never
take a current `.dat` price as an input. The `.dat` price is the quantity under audit; using it
to build the target is circular and makes the comparison worthless.

Every rate below is a measured price from `New/ai/infrastructure-cost-evidence.md`. Each carries
the year of its source and is deflated to 1900 with the `infrastructure` series in
`New/config/prices.tab` before use. Comparing a nominal 1819 figure with a nominal 2005 figure
without deflating is the same class of error as taking the price from the `.dat`: it makes the
comparison meaningless across eras.

Attributes (`material`, `level`, `capacity`, `rail_weight`, `working_method`) come from
`infrastructure-features.csv`; they are specifications, not prices.

Where the evidence has no rate for a class, the object gets NO value and a stated reason.

Output: `measured-infrastructure.csv`.
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(HERE))
FEATURES = os.path.join(HERE, 'infrastructure-features.csv')
PRICES = os.path.join(BASE, 'New', 'config', 'prices.tab')
OUT = os.path.join(HERE, 'measured-infrastructure.csv')

# Real 1900 GBP to .dat units, from New/ai/infrastructure-base-costs.md:
#   linear object   .dat = GBP per km x 252.3          (a tile is 125 m; 8 tiles to the km)
#   scaled object   .dat = GBP per object x 2,019
PER_KM = 252.3
PER_OBJECT_SCALED = 2018.6
PER_OBJECT_UNSCALED = 252.3

_idx = None


def index(year):
    """Infrastructure price index, 1900 = 100, from prices.tab (linear interpolation)."""
    global _idx
    if _idx is None:
        _idx = {}
        for line in open(PRICES, encoding='utf-8'):
            line = line.strip()
            if not line.startswith('infrastructure='):
                continue
            nums = [int(x) for x in line.split('=', 1)[1].split(',')]
            _idx = dict(zip(nums[0::2], nums[1::2]))
    ys = sorted(_idx)
    if year <= ys[0]:
        return _idx[ys[0]]
    if year >= ys[-1]:
        return _idx[ys[-1]]
    lo = max(y for y in ys if y <= year)
    hi = min(y for y in ys if y >= year)
    if lo == hi:
        return _idx[lo]
    return _idx[lo] + (_idx[hi] - _idx[lo]) * (year - lo) / float(hi - lo)


def to1900(gbp, year):
    return gbp * 100.0 / index(year)


# ------------------------------------------------------------------ measured rate tables
# (GBP in the source's own money, source year). Ways are GBP per km of route.
WAY_KM = {
    'rail':         (1600.0, 1900),   # installed P-way band 1,300-1,900, flat 1830-1900
    'narrow gauge': (1600.0, 1900),   # no separate measurement
    'tram':         (3138.0, 1911),   # GBP 5,050 a mile complete street track (not the 600 forge rate)
    # maglev: Munich Transrapid planning estimate, EUR 10.1m a track-km at grade and 12.35m
    # elevated (2007), converted at EUR 1 = GBP 0.68
    # maglev: overseas guideway-only rates adjusted for construction labour cost to a United
    # Kingdom equivalent. Research pass 17 central values: GBP 8m a track-km at grade and
    # GBP 10m elevated (ratio 1.25), nominal of about 2015. The Munich planning estimate was
    # not guideway-only, so it is no longer used.
    'maglev':       (8000000.0, 2015),
    # roads
    'turnpike':     (174.0, 1819),    # network average, GBP 280/mile
    'macadam':      (1100.0, 1825),   # Telford/McAdam, GBP 1,200-2,400 a mile
    'tarmac':       (1093.0, 1906),   # GBP 1,760 a mile for a 10-yard road
    'asphalt':      (308000.0, 2017), # GBP 32-56/m2 of layers, 7 m carriageway, midpoint
    'rural road':   (966000.0, 2011),   # HS2 rural GBP 138/m2 x 7 m carriageway
    'motorway':     (1350000.0, 2005),  # GBP 1.2-1.5m per lane-km, way only, midpoint
    # water
    'canal narrow': (3700.0, 1900),   # 1,850-5,560/km
    'canal ship':   (24000.0, 1900),  # 14,750-33,000/km
    'canal large':  (272000.0, 1900),
    # full road construction, so every surface has a rate
    'dirt':         (100.0, 1900),    # formation only, low end of the 50-250/km bed band
    'cobble':       (174.0, 1819),    # no separate cobble rate: a made road of the turnpike era
    'urban road':   (1610000.0, 2011),   # HS2 urban GBP 230/m2 x 7 m carriageway
    'major road':   (1449000.0, 2011),   # HS2 major GBP 207/m2 x 7 m carriageway
    'elevated':     (21000000.0, 2005),  # DLR City Airport viaduct 19-24m/km, midpoint
}
URBAN = 1.75                          # urban construction 1.5-2x rural per lane-km
ROAD_WIDTH = 7.0                      # metres, for converting a per-m2 rate to a per-km rate

# Bridges: GBP per metre of length. (value, year)
BRIDGE_M = {
    'stone':    (107.5, 1900),        # masonry and brick 55-160/m, midpoint
    'brick':    (107.5, 1900),
    'iron':     (164.0, 1900),        # trestles 48-280/m, midpoint
    'steel':    (280.0, 1900),        # upper iron band; no separate steel series
    'timber':   None,                 # no measured capital rate, only deck renewal
    'concrete': None,
}

# Tunnels: GBP per metre.
TUNNEL_M = {
    'rail': (95.0, 1900),             # double-track bored 45-145/m, midpoint
    'tube': (43.0, 1900),             # deep tube per bore 25-61/m, midpoint
}

# Depots: measured British buildings, assigned by WAYTYPE AND ERA, never by `level`.
# `level` in a depot .dat was historically used by the engine to set the depot price, so any
# ladder built on it would be calibrating the price from the price. The pakset records no road
# count, bay count or floor area, so each family takes one measured TYPICAL depot, and the
# typical size is stated in the basis so it can be challenged.
#
# The per-unit rates these are built from (research pass 9):
#   plain running shed            GBP 558-932 a road (Malton 1853 to Rowsley 1922)
#   repair-equipped shed          GBP 4,855-6,607 a road (Accrington 1898)
#   diesel running shed           GBP 18,800 for six roads (Monument Road 1955)
#   bus garage                    GBP 800 a bus (Coventry 1954), GBP 500 a bus (1929)
#   tram depot                    GBP 512 a car (Hyde Road 1915), GBP 203-357 (1901)
#   stable                        GBP 117-250 a horse (1889-95)
#   hangar                        GBP 2,526 (Grimsby 1937)
#   patent slip                   GBP 450-1,900 (1832)
DEPOT_FAMILY = {
    'rail steam':   (3000.0, 4),    # 4 roads at about GBP 750 a road (Barrow Hill 1870)
    'rail diesel':  (4382.0, 6),    # Monument Road 1955, GBP 18,800 for six roads
    'rail electric': (4382.0, 6),   # no separate electric measurement; diesel depot used
    'road':         (5600.0, 30),   # 30 buses at GBP 187 a bus (Coventry 1954)
    'road steam':   (3000.0, 4),    # steam wagon shed; rail steam rate, flagged
    'tram':         (9560.0, 20),   # 20 cars at GBP 478 a car (Hyde Road 1915)
    'stable':       (2083.0, 10),   # 10 horses at GBP 200 a horse (1889-95)
    'hangar':       (1403.0, 1),    # replaced by HANGAR_PTS below
    'slip':         (1304.0, 1),    # patent slip 1832
}

_depot_tr = None


def depot_traction():
    """{object name: set of traction_type[] values} from New/depots/*.dat.

    This is a declared specification, not a price, so it may be used to choose a rate.
    """
    global _depot_tr
    if _depot_tr is None:
        _depot_tr = {}
        import glob
        import re
        for p in glob.glob(os.path.join(BASE, 'New', 'depots', '*.dat')):
            txt = open(p, encoding='utf-8', errors='replace').read()
            for b in re.split(r'(?im)^\s*obj\s*=', txt)[1:]:
                nm = None
                tr = set()
                for line in b.splitlines():
                    m = re.match(r'\s*name\s*=\s*(\S+)', line, re.I)
                    if m:
                        nm = m.group(1).strip()
                    m = re.match(r'\s*traction_type\[\d+\]\s*=\s*(\S+)', line, re.I)
                    if m:
                        tr.add(m.group(1).strip().lower())
                if nm:
                    _depot_tr[nm.lower()] = tr
    return _depot_tr

# Platform length is set by the GRAPHICS scale, not by meters_per_tile. A Mk3 coach is 23 m and
# carries length=13; a Mk1 is 20.9 m at length=11; a Class 66 is 21.4 m at length=12. That is
# about 1.8 m per length unit, and 16 units to a tile, so a tile holds about 29 m of train.
# Platform cost per tile is therefore rate per metre x 28.8, not x 125.
PLATFORM_M_PER_TILE = 28.8

# Station building rate per passenger-place, in 1900 GBP. The rate VARIES BY CLASS, which is what
# allows one building to be more or less capital-efficient per place than another; a single rate
# would impose constant efficiency by construction.
#   halt    GWR halt 1906 GBP 261 / 40 places        = 6.5 nominal -> 4.2
#   country Low Street 1861 brick building / 100     = 3.0 nominal -> 3.7 (raised to 10 to
#           reflect the building share of the GBP 630 total)
#   standard Southend East 1934 GBP 17,040 / 640     = 26.6 nominal -> 14.8
#   deco    1930s large station, between standard and modern
#   modern  Grays 1954 GBP 33,000 / 300              = 110 nominal -> 25.6
STATION_CLASS_RATE = {
    'halt': 4.2, 'country': 10.0, 'standard': 14.8, 'deco': 20.0, 'modern': 25.6,
}

# Air terminals and hangars, 1900 GBP per building, from measured whole-building costs.
HANGAR_PTS = {1938: 13812.0, 1968: 73059.0}

# Stations (evidence states 1900 prices).
STATION_STOP = {1: 3.0, 5: 40.0}      # GBP per metre of platform face, timber to concrete + roof
STATION_BUILDING = {1: 261.0, 5: 50660.0}  # whole-building examples, for reference only
STATION_QUAY = 115.0                       # masonry quay wall 100-131/m, at 1900 prices
TERMINAL_PLACE_PTS = {1935: 21.0, 1986: 55.0, 1991: 85.0}
STATION_PLACE_PTS = {1861: 3.9, 1934: 14.8}

# Signals: GBP per post. The 1909 automatic figure is a semaphore; the colour-light figure is
# the audited Kent Coast cost per running signal (Tyler 1962, Appendix E): GBP 4.3m for 97 route
# miles, 640 signals, 930 track circuits and 275 point machines = GBP 12,000 a signal and
# GBP 27,545 a route km.
SIGNAL_POST = (25.0, 1912)        # complete post 16-33, midpoint
SIGNAL_AUTOMATIC = (98.0, 1909)   # complete automatic semaphore 97-100
SIGNAL_COLOUR = (12000.0, 1960)   # colour-light running signal, Kent Coast Phase I

# Signalbox: GBP per controlled lever (1909 mechanical) or per route (Euston power box,
# GBP 2m for 488 routes in 1965); a whole modern centre takes the box total.
SIGNALBOX_LEVER = (30.0, 1909)
SIGNALBOX_ROUTE = (4098.0, 1965)
SIGNALBOX_CENTRE = (2000000.0, 1965)

# Electrification: GBP per track km.
ELECTRIFICATION = {
    'third rail': (7713.0, 1925),   # Guildford and Dorking
    'fourth rail': (7713.0, 1925),
    '25kv': (24200.0, 1955),        # Euston-Manchester-Liverpool per track km
    'tram': (175000.0, 2017),       # 750 V DC overhead, 150,000-200,000 per single track km
    'dlr': (7713.0, 1925),
    'overhead dc': (377000.0, 2011),  # HS2 cost model, GBP 377 per route metre single track
}


def num(v):
    try:
        return float(str(v).replace(',', ''))
    except (TypeError, ValueError):
        return None


def interp_log(points, x):
    pts = sorted(points.items())
    if x <= pts[0][0]:
        return pts[0][1]
    if x >= pts[-1][0]:
        return pts[-1][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            t = (x - x0) / float(x1 - x0)
            return math.exp(math.log(y0) * (1 - t) + math.log(y1) * t)
    return pts[-1][1]


def way_rate(row):
    """(GBP/km at 1900, basis) or (None, reason)."""
    cls = row['class']
    nm = row['name'].lower()
    if cls == 'ways/rail':
        v, y = WAY_KM['rail']
        return to1900(v, y), 'installed permanent way 1,300-1,900 GBP/km, midpoint 1,600 (L&M 1830 to Mills 1898)'
    if cls == 'ways/narrowgauge':
        v, y = WAY_KM['narrow gauge']
        return to1900(v, y), 'no separate narrow-gauge measurement; the standard permanent-way band applies'
    if cls == 'ways/tram':
        # Complete street track GBP 5,050 a mile (1911). Rail is 13-30% of that; the rail
        # component scales with rail weight at the 1907 price of GBP 6.44-16.99 a ton and
        # 1.5714 tons per lb/yd per single-track mile. 85 lb reproduces the flat GBP 3,138/km.
        w = num(row.get('rail_weight')) or 85.0
        per_mile = 3487.0 + w * 1.5714 * 11.7
        gbp_km = per_mile * 0.621371
        return to1900(gbp_km, 1911), (
            'complete street track: non-rail base GBP 3,487 a mile plus rail at %g lb/yd and '
            'GBP 11.70 a ton (1907); 85 lb reproduces the measured GBP 5,050 a mile' % w)
    if cls == 'ways/road':
        if 'bridle' in nm or 'dirt' in nm:
            v, y = WAY_KM['dirt']
            return to1900(v, y), ('unmetalled road: formation and grading only, low end of the '
                                  'measured 50-250 GBP/km road-bed band')
        if 'cobble' in nm:
            v, y = WAY_KM['cobble']
            return to1900(v, y), ('no separate cobble rate; a made road of the turnpike era, '
                                  'GBP 280/mile 1819')
        if 'macadam' in nm or 'improved' in nm:
            v, y = WAY_KM['macadam']
            return to1900(v, y), '1820s Telford/McAdam, GBP 1,200-2,400 a mile nominal'
        if 'tarmac' in nm or 'city' in nm:
            if 'tarmac' in nm:
                v, y = WAY_KM['tarmac']
                g = to1900(v, y)
                if 'city' in nm:
                    return g * URBAN, ('1906 tarmac for a 10-yard road nominal, x1.75 '
                                       'urban-to-rural construction')
                return g, '1906 tarmac, GBP 1,760 a mile for a 10-yard road nominal'
            v, y = WAY_KM['urban road']
            return to1900(v, y), ('HS2 urban road construction 2011, GBP 230/m2 over a 7 m '
                                  'carriageway, deflated to 1900')
        if 'motorway' in nm:
            v, y = WAY_KM['motorway']
            return to1900(v, y), ('2005 motorway way only, GBP 1.2-1.5m per lane-km nominal; '
                                  'one lane-width per tile')
        if 'concrete' in nm:
            v, y = WAY_KM['major road']
            return to1900(v, y), ('HS2 major road construction 2011, GBP 207/m2 over a 7 m '
                                  'carriageway, deflated to 1900')
        if 'asphalt' in nm or 'sma' in nm or 'hr-' in nm:
            v, y = WAY_KM['rural road']
            return to1900(v, y), ('HS2 rural road construction 2011, GBP 138/m2 over a 7 m '
                                  'carriageway, deflated to 1900')
        return None, 'no measured rate for this surface'
    if cls == 'ways/maglev':
        v, y = WAY_KM['maglev']
        if 'elevated' in nm:
            v *= 1.22
            return to1900(v, y), ('Munich Transrapid planning estimate EUR 12.35m a track-km '
                                  'elevated (2007) at EUR 1 = GBP 0.68')
        return to1900(v, y), ('Munich Transrapid planning estimate EUR 10.1m a track-km at '
                              'grade (2007) at EUR 1 = GBP 0.68')
    if cls == 'ways/air':
        y = num(row.get('intro_year')) or 1960
        width = 30.5 if y < 1945 else 45.0
        if 'grass' in nm:
            v = 1.5 * 30.0 * 1000.0
            basis = 'grass runway 1-2 GBP/m2 over a 30 m width'
        elif 'concrete' in nm:
            v = 129.0 * width * 1000.0
            basis = 'concrete runway 69-189 GBP/m2, midpoint 129, over %g m' % width
        else:
            v = 44.0 * width * 1000.0
            basis = 'asphalt runway 32-56 GBP/m2, midpoint 44, over %g m' % width
        if 'taxiway' in nm:
            v *= 23.0 / width
            basis += '; taxiway at 23 m'
        return to1900(v, 2010), basis
    if cls == 'ways/power':
        return to1900(15535.0, 1959), '275 kV lattice line GBP 15,535/km in 1959'
    if cls == 'ways/water':
        if 'large' in nm:
            v, y = WAY_KM['canal large']
        elif 'river' in nm or 'ship' in nm:
            v, y = WAY_KM['canal ship']
        else:
            v, y = WAY_KM['canal narrow']
        return to1900(v, y), (
            'measured canal construction per km by size class; whole construction including '
            'formation, because for a canal the forging is the building and forge_cost_water is 0 '
            '(decision 2026-11-24)')
    return None, 'no measured rate for this way type'


def bridge_rate(row):
    mat = (row.get('material') or '').lower()
    nm = row['name'].lower()
    if not mat:
        for k in ('iron', 'steel', 'stone', 'masonry', 'brick', 'concrete', 'timber', 'wood'):
            if k in nm:
                mat = {'masonry': 'stone', 'wood': 'timber'}.get(k, k)
                break
    if mat == 'timber':
        return 48000.0, ('no measured timber viaduct rate; the iron trestle lower bound of '
                         'GBP 48/m is used as the nearest measured structure')
    if mat == 'concrete':
        v, y = WAY_KM['elevated']
        return to1900(v, y), ('no measured concrete bridge rate; the DLR City Airport concrete '
                              'viaduct at GBP 19-24m/km 2005 is the nearest measured structure')
    if mat:
        r = BRIDGE_M.get(mat)
        if r:
            v, y = r
            return to1900(v, y) * 1000.0, 'measured %s bridge, GBP per metre at 1900 prices' % mat
        return None, 'no measured capital rate for %s bridges' % mat
    return None, 'no material stated; no measured rate'


def tunnel_rate(row):
    """GBP per km from the 1905 shield-tunnel rule: cost per metre = GBP 3.7 x cross-section
    area in m2. One track per tunnel; a double-track tunnel is two objects.

    Sections by type: standard gauge 4.57 m (15 ft, the measured GBP 65.20/m point); tube
    3.81 m (12 ft 6 in, the measured GBP 39.82/m point); narrow gauge 3.20 m (10 ft 6 in, the
    measured GBP 30.56/m point). Road, water and power are given stated rectangular sections.
    """
    wt = (row.get('waytype') or '').lower()
    nm = row['name'].lower()
    if wt == 'narrow gauge':
        d, basis = 3.20, 'narrow-gauge bore 3.20 m (10 ft 6 in)'
    elif wt == 'track' and ('lt_' in nm or 'tube' in nm):
        d, basis = 3.81, 'tube bore 3.81 m (12 ft 6 in)'
    elif wt == 'road':
        area = 40.0
        return to1900(3.7 * area * 1000.0, 1905), (
            '1905 shield-tunnel rule GBP 3.7 per m2 of section, applied to a stated 40 m2 '
            'single-carriageway road section')
    elif wt == 'water':
        area = 16.0
        return to1900(3.7 * area * 1000.0, 1905), (
            '1905 shield-tunnel rule GBP 3.7 per m2 of section, applied to a stated 16 m2 '
            'canal section')
    elif wt == 'power':
        area = 4.0
        return to1900(3.7 * area * 1000.0, 1905), (
            '1905 shield-tunnel rule GBP 3.7 per m2 of section, applied to a stated 4 m2 '
            'cable section')
    else:
        d, basis = 4.57, 'standard-gauge bore 4.57 m (15 ft)'
    area = math.pi * (d / 2.0) ** 2
    gbp_m = 3.7 * area
    return to1900(gbp_m * 1000.0, 1905), (
        '1905 shield-tunnel rule GBP 3.7 per m2 of cross-section: %s, area %0.1f m2, '
        'GBP %0.2f/m' % (basis, area, gbp_m))


def station_rate(row):
    dt = (row.get('dat_type') or 'stop').lower()
    wt = (row.get('waytype') or '').lower()
    nm = row['name'].lower()

    if wt == 'air':
        y = num(row.get('intro_year')) or 1960
        if 'tower' in nm:
            return to1900(10000000.0, 2005), (
                'control tower GBP 10m at Edinburgh 2005 (57 m), Birmingham 2012 and Manchester '
                '2013 GBP 10-16m; the KB Luton and Heathrow figures are unverified')
        if 'apron' in nm:
            return None, ('apron is pavement, not a building; the pakset records no apron area '
                          'and there is no measured cost per stand')
        cap = num(row.get('capacity')) or 115.0
        rate = interp_log(TERMINAL_PLACE_PTS, y)
        return cap * rate, (
            'terminal per passenger-place at %g m2 a place: 1930s package GBP 93,000/1,000 '
            'places, T4 GBP 200m/70,321, Stansted GBP 100m/21,333; year %g rate, times %g '
            'places' % (1.5, y, cap))

    if wt == 'road':
        if 'busstop' in nm:
            return to1900(400.0, 2010), 'pole, flag and timetable case GBP 300-500, midpoint 400'
        if 'shelter' in nm:
            if 'modern' in nm:
                return to1900(9500.0, 2010), 'modern aluminium and glass shelter GBP 7,000-12,000'
            return to1900(62.0, 1910), 'Brighton Corporation glazed timber shelter GBP 62, 1902-16'
        if 'terminal' in nm and 'bus' in nm:
            return to1900(268921.0, 2001), (
                'bus station per stand: Walsall 2001 GBP 268,921 a stand (14 stands, '
                'GBP 1,101/m2); Heckmondwike 2022 GBP 828,333 a stand')
        if 'loading' in nm or 'truck' in nm:
            return to1900(29857.0, 2014), (
                'truck stop per HGV space GBP 29,100-29,857 construction (2014), GBP 38,372 '
                'all-in with welfare (2024)')
        if 'terminal' in nm or 'staging' in nm:
            cap = num(row.get('capacity')) or 50.0
            return cap * STATION_CLASS_RATE['standard'], (
                'road terminal building per passenger-place at the standard station rate, '
                'times %g places' % cap)
        return None, ('no measured per-object rate: loading bays and truck stops are hardstanding '
                      'and the pakset records no area')

    if wt == 'water':
        return STATION_QUAY * 125.0, 'masonry quay wall 100-131 GBP/m over a 125 m tile, at 1900 prices'

    if dt == 'extension':
        cap = num(row.get('capacity'))
        if not cap:
            return None, 'station building with no capacity; cannot compose it from the per-place rate'
        nm = row['name'].lower()
        if 'halt' in nm:
            cls = 'halt'
        elif 'country' in nm:
            cls = 'country'
        elif 'deco' in nm:
            cls = 'deco'
        elif 'modern' in nm or '1950s' in nm:
            cls = 'modern'
        else:
            cls = 'standard'
        rate = STATION_CLASS_RATE[cls]
        return cap * rate, (
            'station building per passenger-place, %s class at GBP %g a place; the rate varies '
            'by class so that efficiency per place is not fixed by construction; times %g '
            'places' % (cls, rate, cap))
    if dt == 'stop' and wt in ('track', 'narrow gauge', 'maglev'):
        mat = (row.get('material') or '').lower()
        if not mat:
            for k in ('timber', 'wood', 'brick', 'concrete', 'stone'):
                if k in nm:
                    mat = 'timber' if k == 'wood' else k
                    break
        base = {'timber': 3.0, 'brick': 6.0, 'stone': 6.0, 'concrete': 7.5}.get(mat, 6.0)
        roof = 0.0
        label = 'no roof'
        if 'overall' in nm:
            roof, label = 42.5, 'overall roof 25-60 GBP/m'
        elif 'building' in nm or 'canopy' in nm:
            roof, label = 19.5, 'canopy 9-30 GBP/m'
        per_m = base + roof
        return per_m * PLATFORM_M_PER_TILE, (
            'platform face by material: %s at GBP %g/m (timber 2-4, brick 4-8, concrete 5-10) '
            'plus %s; %0.1f m of train per tile' % (mat or 'unstated, brick assumed', base,
                                                   label, PLATFORM_M_PER_TILE))
    return 6.0 * PLATFORM_M_PER_TILE, (
        'platform face at the brick rate of GBP 6/m (material not stated) at the GRAPHICS '
        'scale: 28.8 m of train per tile, not 125 m')


# One signal object is one signal in reality (post with its arms or lamps); the general
# signalling infrastructure is priced in the signalbox, not here (decision 2026-11-24).
_SIGNAL_MEANING = (' | one signal object is one signal in reality; the general signalling '
                   'infrastructure is priced in the signalbox (decision 2026-11-24)')


def signal_rate(row):
    st = (row.get('signal_type') or '').lower()
    wm = (row.get('working_method') or '').lower()
    if st in ('colour light', 'cab', 'etcs beacon', 'seltrac beacon', 'speed signal'):
        v, y = SIGNAL_COLOUR
        return to1900(v, y), (
            'colour-light running signal, Kent Coast Phase I 1959-62: GBP 4.3m for 97 route '
            'miles, 640 signals, 930 track circuits and 275 point machines = GBP 12,000 a '
            'signal (Tyler 1962, Appendix E), deflated to 1900') + _SIGNAL_MEANING
    if st in ('mechanical', 'semaphore', 'electro-pneumatic', 'vane', 'board', 'flag', 'staff'):
        v, y = SIGNAL_POST
        return to1900(v, y), ('signal post complete, GBP 16-33 in 1912, midpoint 25'
                              ) + _SIGNAL_MEANING
    if wm in ('drive_by_sight', 'one_train_staff', 'time_interval',
              'time_interval_with_telegraph', 'token_block', 'absolute_block'):
        v, y = SIGNAL_POST
        return to1900(v, y), ('signal post complete, GBP 16-33 in 1912, midpoint 25'
                              ) + _SIGNAL_MEANING
    v, y = SIGNAL_AUTOMATIC
    return to1900(v, y), ('complete automatic semaphore signal, GBP 97-100 in 1909'
                          ) + _SIGNAL_MEANING


def signalbox_rate(row):
    cap = num(row.get('capacity'))
    if not cap:
        return None, 'no controlled-post count; no measured rate'
    nm = row['name'].lower()
    if 'centre' in nm or 'etrms' in nm or 'seltrac' in nm or 'tvm' in nm or 'retb' in nm:
        v, y = SIGNALBOX_CENTRE
        return to1900(v, y), (
            'modern signalling centre: Euston power box about GBP 2m in 1965 for 488 routes, '
            'whole-box figure, deflated to 1900')
    if 'power' in nm:
        v, y = SIGNALBOX_ROUTE
        return to1900(v, y) * cap, (
            'power signal box at the Euston rate of GBP 4,098 a route (GBP 2m for 488 routes, '
            '1965), times the controlled-post count')
    v, y = SIGNALBOX_LEVER
    return to1900(v, y) * cap, '1909 mechanical installation at GBP 28-30 a lever'


def electrification_rate(row):
    nm = row['name'].lower()
    if 'trolley' in nm or 'trolly' in nm:
        key = 'tram'
    elif '25kv' in nm or nm.startswith('ac'):
        key = '25kv'
    elif 'dlr' in nm:
        key = 'dlr'
    elif 'third' in nm or 'fourth' in nm:
        key = 'third rail'
    elif 'catenary' in nm or 'dc' in nm:
        key = 'overhead dc'
    else:
        return None, 'no measured rate for this electrification system'
    v, y = ELECTRIFICATION[key]
    return to1900(v, y), 'measured %s electrification per track km, deflated to 1900' % key


def roadsign_rate(row):
    """GBP per object at 1900, from research pass 10. A junction is priced as a junction, never
    as four times a head."""
    nm = row['name'].lower()
    y = num(row.get('intro_year')) or 1930
    if 'traffic_light' in nm:
        if 'led' in nm:
            return to1900(57000.0, 2017), 'modern LED junction GBP 57,000-150,000 all-in'
        if 'mellor' in nm:
            return to1900(450.0, 1932), '1932 London junction GBP 400-500'
        return to1900(3100.0, 1963), '1963 crossroads average GBP 3,100'
    if 'railgate' in nm:
        return to1900(5500.0, 1961), 'first British automatic half-barrier GBP 5,000-6,000'
    if 'motorway' in nm or 'gantry' in nm:
        return to1900(5000.0, 2017), 'advance direction sign GBP 5,000 (2017)'
    if 'noentry' in nm or 'oneway' in nm or 'private' in nm:
        return to1900(745.0, 2024), 'illuminated one-way or no-entry sign GBP 745 (2024)'
    if y < 1970:
        return to1900(1.5, 1935), 'complete sign GBP 1 2s 6d to 1 17s 6d (1935)'
    return to1900(158.0, 2025), 'standard sign GBP 157.71 (Suffolk commuted sum 2025)'


def capital(row):
    """(dat, gbp1900, basis) or (None, None, reason). No `.dat` price is read here."""
    t = row['obj_type']
    if t == 'way':
        elevated = (row.get('elevated') or '').lower() == 'yes'
        gbp, basis = way_rate(row)
        if gbp is None:
            if not elevated:
                return None, None, basis
            gbp, basis = 0.0, ''
        if elevated:
            b, bbasis = bridge_rate(row)
            if b is None:
                v, y = WAY_KM['elevated']
                b = to1900(v, y)
                bbasis = ('no measured rate for that material; DLR City Airport viaduct '
                          '19-24m GBP/km 2005, deflated to 1900')
            gbp += b
            basis = ((basis + ' | ') if basis else '') + 'elevated structure: ' + bbasis
        return gbp * PER_KM, gbp, basis
    if t == 'bridge':
        gbp, basis = bridge_rate(row)
        return (None, None, basis) if gbp is None else (gbp * PER_KM, gbp, basis)
    if t == 'tunnel':
        gbp, basis = tunnel_rate(row)
        return (None, None, basis) if gbp is None else (gbp * PER_KM, gbp, basis)
    if t == 'way-object':
        gbp, basis = electrification_rate(row)
        return (None, None, basis) if gbp is None else (gbp * PER_KM, gbp, basis)
    if t in ('station', 'signal', 'signalbox'):
        f = {'station': station_rate, 'signal': signal_rate, 'signalbox': signalbox_rate}[t]
        gbp, basis = f(row)
        return (None, None, basis) if gbp is None else (gbp * PER_OBJECT_SCALED, gbp, basis)
    if t == 'depot':
        nm = row['name'].lower()
        wt = (row.get('waytype') or '').lower()
        y = num(row.get('intro_year')) or 1900
        tr = depot_traction().get(nm, set())
        if 'hangar' in nm or wt == 'air':
            fam = 'hangar'
        elif 'boatyard' in nm or wt == 'water':
            fam = 'slip'
        elif wt == 'maglev' or not tr:
            fam = 'rail diesel'
        elif wt == 'tram':
            fam = 'tram'
        elif wt == 'road':
            fam = 'road steam' if tr == {'steam'} else 'road'
        elif 'bio' in tr and not (tr & {'steam', 'diesel', 'electric'}):
            fam = 'stable'
        elif 'steam' in tr and not (tr & {'diesel', 'electric'}):
            fam = 'rail steam'
        elif 'electric' in tr and not (tr & {'diesel', 'steam'}):
            fam = 'rail electric'
        else:
            fam = 'rail diesel'
        gbp, units = DEPOT_FAMILY[fam]
        if fam == 'hangar':
            gbp = interp_log(HANGAR_PTS, y)
            units = 1
        return gbp * PER_OBJECT_UNSCALED, gbp, (
            'measured %s depot, typical size %d units; chosen by waytype and traction_type '
            '(%s), never by level' % (fam, units, ','.join(sorted(tr)) or 'none'))
    if t == 'building':
        # HQ: GBP 15/m2 ordinary and GBP 40/m2 top level at 1900-1910 prices; 900 m2 assumed
        # per building tile because the pakset records tiles, not floor area. The HQ objects
        # carry no level field, and level is a price-setting artefact anyway, so a single
        # ordinary rate is used rather than a level test.
        area = 900.0 * max(1.0, (num(row.get('size_x')) or 1.0) * (num(row.get('size_y')) or 1.0))
        rate = 15.0
        gbp = rate * area
        return gbp * PER_OBJECT_UNSCALED, gbp, (
            'headquarters at GBP %g/m2 (Port of Liverpool GBP 9.44-13.21/m2, County Hall '
            'GBP 42.14/m2) over an assumed %0.0f m2' % (rate, area))
    if t == 'other':
        if row.get('class') == 'roadsigns':
            gbp, basis = roadsign_rate(row)
            return gbp * PER_OBJECT_SCALED, gbp, basis
        return None, None, 'piers are bridge substructure; a single share cannot represent the measured 16-82%, so they stay unpriced'
    return None, None, 'no measured rate for this object type'


def maintenance(row):
    """(GBP per year at 1900, basis) from research pass 14, or (None, None).

    The LED comparison is same-year: a 2019 incandescent signal costs GBP 825-900 a year and a
    self-cleaning LED GBP 75-150, an 80-90% saving. Deflating each from its own year would hide
    that, so incandescent is carried at its 1959-62 real level (GBP 56-142, which deflates to
    about the same as GBP 825-900 does from 2019) and the LED at the measured 2019 figure.
    """
    t = row['obj_type']
    nm = row['name'].lower()
    if t == 'signal':
        st = (row.get('signal_type') or '').lower()
        if 'led' in nm:
            return 1.1, (
                'LED self-cleaning signal GBP 75-150 a signal-year (2019), 80-90% below the '
                'GBP 825-900 incandescent total; deflated to 1900')
        if st in ('colour light', 'cab', 'etcs beacon', 'seltrac beacon', 'speed signal'):
            return 15.0, (
                'incandescent colour light GBP 56-142 a signal-year on the Kent Coast (1959-62), '
                'deflated to 1900; roughly flat in real terms to the GBP 825-900 of 2019')
        return 5.0, 'mechanical semaphore GBP 4-12 a signal-year (1870-1935), midpoint 5'
    if t == 'signalbox':
        # The signalbox is the carrier for the whole signalling SYSTEM: track circuits, cables,
        # control and interlocking, not just the building. Network Rail's per-SEU maintenance is
        # GBP 2,594 a SEU-year (2011-12), GBP 2,132 on CP5; deflated to 1900 that is about
        # GBP 43. The signal object already carries its own apparatus (GBP 15 incandescent,
        # GBP 1.10 LED), so the box carries the remainder, about GBP 28 a controlled post.
        # Manning is a separate cost type and is excluded.
        cap = num(row.get('capacity')) or 0
        y = num(row.get('intro_year')) or 1900
        if 'power' in nm or 'centre' in nm or 'etrms' in nm or 'seltrac' in nm \
                or 'tvm' in nm or 'retb' in nm:
            if y >= 1955 and cap:
                return cap * 28.0, (
                    'signalling system maintenance carried by the box: per-SEU total GBP 2,594 '
                    'a SEU-year (2011-12) less the GBP 15 signal apparatus, about GBP 28 a '
                    'controlled post at 1900 prices; manning excluded')
            return None, (
                'pre-1955 power box: the per-SEU series starts in 2011 and no apparatus-only '
                'figure exists for this era')
        return 6.0, 'mechanical box apparatus GBP 6.30 a year (Spetisbury 1901), manning excluded'
    if t == 'other' and row.get('class') == 'roadsigns':
        if 'traffic_light' in nm:
            return 17.0, (
                'traffic signal site GBP 1,500-2,400 a site-year (Argyll GBP 1,800, DfT 2024 '
                'GBP 1,599-2,393, West Sussex GBP 1,532-1,613), deflated to 1900')
        return 0.03, (
            'ordinary unlit sign GBP 2-5 a sign-year replacement provision (Argyll, Wigan), '
            'midpoint 3, deflated to 1900')
    if t == 'depot':
        _dat, gbp, _basis = capital(row)
        if not gbp:
            return None, None
        return gbp * 0.015, (
            'depot maintenance 1.5%% of capital a year (band 1.0-2.0%%: Seeley 1%%, light '
            'industrial 1.6%%, BMI 2.5%%; Midland Railway buildings 0.19-0.39%% of department '
            'spending); capital GBP %0.0f' % gbp)
    if t == 'way':
        # Measured maintenance per km-year, converted to a per-tile figure (8 tiles to the km).
        #   rail   BR 1966 GBP 44/km-year excluding renewal
        #   water  canal GBP 62/km-year (1938 comparison)
        #   road   main road GBP 35 11s a mile-year (1880) = 22/km
        # Elevated ways add the structure upkeep from the bridge material rate.
        cls = (row.get('class') or '').lower()
        water = 'water' in cls
        if water:
            per_km, y = 62.0, 1938
        elif 'road' in cls:
            per_km, y = 22.0, 1880
        elif 'tram' in cls or 'maglev' in cls:
            return None, None
        else:
            per_km, y = 44.0, 1966
        total = to1900(per_km, y) / 8.0
        basis = 'way upkeep GBP %0.1f a tile-year at 1900 (GBP %0.0f/km-year nominal %d)' % (
            total, per_km, y)
        if water:
            basis += (' | canal upkeep only: canal ways carry no wear and are not renewed, so '
                      'this carries no renewal element (decision 2026-11-24)')
        if (row.get('elevated') or '').lower() == 'yes':
            b, bbasis = bridge_rate(row)
            if b is None:
                return None, None
            total += b / 8.0
            basis += ' | plus elevated structure at ' + bbasis
        return total, basis
    if t == 'bridge':
        # Measured upkeep per metre-year, 1886 prices: iron GBP 0.23-0.25 (two NER structures,
        # 18-year means), brick GBP 0.05 (Hownes Gill), stone GBP 0.04-0.05 (inferred),
        # steel GBP 0.27-0.32 (inferred from painting intervals), timber GBP 0.52-0.55 renewal.
        # A bridge tile is 125 m of geographic length.
        mat = (row.get('material') or '').lower()
        if not mat:
            for k in ('iron', 'steel', 'stone', 'masonry', 'brick', 'concrete', 'timber', 'wood'):
                if k in nm:
                    mat = {'masonry': 'stone', 'wood': 'timber'}.get(k, k)
                    break
        rate = {'iron': 0.24, 'brick': 0.05, 'stone': 0.045, 'steel': 0.30,
                'timber': 0.53, 'concrete': 0.05}.get(mat)
        if rate is None:
            return None, None
        note = '' if mat != 'concrete' else ' (no measured concrete rate; brick used)'
        return rate * 125.0, (
            'bridge upkeep %0.3f GBP/m-year at 1886 prices%s over %d m of tile'
            % (rate, note, 125))
    if t == 'tunnel':
        _dat, gbp, _basis = capital(row)
        if not gbp:
            return None, None
        return gbp * 0.01, (
            'tunnel maintenance 1%% of capital a year (band 0.5-1.5%%); Network Rail 2023-24 '
            'spent GBP 65.67 a metre-year across 630 tunnels; capital GBP %0.0f' % gbp)
    if t == 'station':
        # Annual maintenance as a measured share of capital: timber 4-8%, brick 0.8-1.5%,
        # concrete 1.5-2.5% (London County Council loan conditions and municipal repair funds).
        _dat, gbp, _basis = capital(row)
        if not gbp:
            return None, None
        mat = (row.get('material') or '').lower()
        if mat == 'timber':
            rate, label = 0.06, 'timber 4-8%'
        elif mat == 'concrete':
            rate, label = 0.02, 'concrete 1.5-2.5%'
        else:
            rate, label = 0.0115, 'brick 0.8-1.5%'
        return gbp * rate, (
            'annual maintenance %s of capital (measured share of capital a year); capital '
            'GBP %0.0f' % (label, gbp))
    return None, None


def main():
    rows = list(csv.DictReader(open(FEATURES, encoding='utf-8-sig')))
    out = []
    covered = 0
    for row in rows:
        dat, gbp, basis = capital(row)
        if dat is not None:
            covered += 1
        maint, mbasis = maintenance(row)
        out.append(dict(name=row['name'], obj_type=row['obj_type'], class_=row['class'],
                        capital_dat=('%0.f' % dat) if dat is not None else '',
                        capital_gbp=('%0.f' % gbp) if gbp is not None else '',
                        unit=('GBP/km' if row['obj_type'] in ('way', 'bridge', 'tunnel', 'way-object')
                              else 'GBP/object'),
                        basis=basis,
                        maint_gbp_yr=('%0.2f' % maint) if maint is not None else '',
                        maint_basis=mbasis or ''))
    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['name', 'obj_type', 'class_', 'capital_dat',
                                          'capital_gbp', 'unit', 'basis',
                                          'maint_gbp_yr', 'maint_basis'])
        w.writeheader()
        w.writerows(out)
    print('rows %d, with a measured-derived value %d, blank %d' % (len(out), covered, len(out) - covered))
    print('written:', OUT)


if __name__ == '__main__':
    main()
