# -*- coding: utf-8 -*-
"""Build cost-balancing-capital.xlsx and cost-balancing-maintenance.xlsx.

MODEL (derived from the ex-15 engine source, 2026-11-22)
--------------------------------------------------------
1. `.dat` money values are 1900 nominal (index 100).            [prices.tab line 2]
2. The engine scales a descriptor's money at load time:
       price       = base_cost       x meters_per_tile / 1000   (integer division)
       maintenance = base_maintenance x meters_per_tile / 1000
       fixed_cost  = base_fixed_cost x meters_per_tile / 1000
   for every descriptor that karte_t::set_scale() visits. running_cost is NOT scaled.
3. Every display/charge then applies the object type's own price series at the current
   month: adjusted = value x index(month) / 100.  The series are:
       vehicle cost .......... vehicle purchase
       vehicle running/fixed . general   (vehicle maintenance is commented out)
       ways/tunnels/bridges/way objects/signals/roadsigns .. infrastructure
       buildings (stations, signalboxes, depots, HQ, city buildings, industries) .. buildings
       engine settings ....... general (forge costs: infrastructure)
4. Charges that accrue per month are additionally multiplied by
       calc_adjusted_monthly_figure: 2^(bits_per_month - 18) / INT(base_mpt / mpt)
   = 2 at 125 m/tile, 22 bits.  This applies to vehicle fixed_cost, way/tunnel/bridge/
   way-object maintenance (finance_t::get_maintenance_with_bits) and building maintenance.
5. Display divides by 100.  So, at 125 m/tile and 22 bits:
       vehicle cost  = .dat x 0.00125 x index / 100
       vehicle fixed = .dat x 0.0025  x index / 100  (per month)
       vehicle run   = .dat x 0.01    x index / 100  (per km)
       way cost      = .dat x 0.01    x index / 100  (per km)
       way maint     = .dat x 0.02    x index / 100  (per km per month)
       building cost = .dat x 0.00125 x index / 100
       building maint= .dat x 0.0025  x index / 100  (per month)
6. The engine's index is a *type* index.  A historical price must therefore be brought to
   1900 with the same series the engine applies to that object, not with `general`.

Consumes:
  ai/temp/cost-inventory.csv        - every costed object in New/ (subagent-built)
  ai/temp/individual-price-rows.csv - measured historical prices (subagent-built)
  ai/temp/evidence_data.py          - manual mappings + class extrapolation bases
  New/config/prices.tab             - all price series (parsed here)
  New/text/en.tab                   - English display names (two-line key/value format)

Run: C:\\WINDOWS\\py.exe -3 ai\\temp\\build_workbooks.py
Output: New/cost-balancing-capital.xlsx, New/cost-balancing-maintenance.xlsx

WARNING (2026-11-24): the committed workbooks New/cost-balancing-capital.xlsx and
New/cost-balancing-maintenance.xlsx contain manual corrections this script does NOT reproduce
(the power-line maintenance conversion, the x8 way-maintenance columns, a maintained formula
variant, and in-place object corrections). A fresh build OVERWRITES them. Do not rebuild without
first porting those corrections into this script. To add notes or rows to the existing workbooks,
patch them in place with wb_patch.py (decision notes and research-pricing-rows-*.csv rows),
wb_dedupe.py (duplicate-row cleanup), wb_dump.py and wb_diff.py (cell-level before/after
verification), all in this folder.
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import namedtuple
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
HERE = os.path.join(BASE, 'New', 'ai', 'cost-balancing')
INVENTORY = os.path.join(HERE, 'cost-inventory.csv')
PRICE_ROWS = os.path.join(HERE, 'individual-price-rows.csv')
RESEARCH_ROWS = os.path.join(HERE, 'research-pricing-rows.csv')
RESEARCH_ROWS_2 = os.path.join(HERE, 'research-pricing-rows-2.csv')
RESEARCH_ROWS_3 = os.path.join(HERE, 'research-pricing-rows-3.csv')
RESEARCH_ROWS_6 = os.path.join(HERE, 'research-pricing-rows-6.csv')
RESEARCH_ROWS_5 = os.path.join(HERE, 'research-pricing-rows-5.csv')
RESEARCH_ROWS_4 = os.path.join(HERE, 'research-pricing-rows-4.csv')
RESEARCH_ROWS_4B = os.path.join(HERE, 'research-pricing-rows-4b.csv')
PRICES_TAB = os.path.join(BASE, 'New', 'config', 'prices.tab')
EN_TAB = os.path.join(BASE, 'New', 'text', 'en.tab')
# Output directory. The default is the live pakset folder. Set COST_BALANCE_OUT to any existing
# directory to run a test rebuild without touching the live workbooks (a review or a comparison
# run uses this), so a rebuild can never overwrite the reviewed files by accident.
OUT_DIR = os.environ.get('COST_BALANCE_OUT') or os.path.join(BASE, 'New')
OUT_CAP = os.path.join(OUT_DIR, 'cost-balancing-capital.xlsx')
OUT_MAINT = os.path.join(OUT_DIR, 'cost-balancing-maintenance.xlsx')

RATE_CAPITAL = 0.396311
RATE_REVENUE = 0.005208
TOL_MATCH, TOL_NEAR = 0.25, 0.5

# Pakset settings the factors are derived from (see Params sheet; B8-B11).
MPT = 125
BITS_PER_MONTH = 22
BASE_MPT = 1000
BASE_BITS = 18
MONTH_FACTOR = (2 ** (BITS_PER_MONTH - BASE_BITS)) / (BASE_MPT // MPT)   # 16/8 = 2

FAC_SCALED = MPT / 1000.0 / 100.0            # 0.00125
FAC_UNSCALED = 0.01
FAC_WAY_KM = MPT / 1000.0 * 8.0 / 100.0      # 0.01
FAC_VEH_MONTH = FAC_SCALED * MONTH_FACTOR     # 0.0025
FAC_WAY_MONTH = FAC_WAY_KM * MONTH_FACTOR     # 0.02
FAC_BLD_MONTH = FAC_SCALED * MONTH_FACTOR     # 0.0025
FAC_UNSC_MONTH = FAC_UNSCALED * MONTH_FACTOR  # 0.02

# ---------------------------------------------------------------- styles
HDR_FILL = PatternFill('solid', fgColor='1F4E78')
HDR_FONT = Font(bold=True, color='FFFFFF', size=10)
TITLE_FONT = Font(bold=True, size=14, color='1F4E78')
LABEL_FONT = Font(bold=True, size=10)
WRAP = Alignment(wrap_text=True, vertical='top')
BORDER = Border(*[Side(style='thin', color='BFBFBF')] * 4)
GREEN = PatternFill('solid', fgColor='C6EFCE'); GREEN_F = Font(color='006100')
AMBER = PatternFill('solid', fgColor='FFEB9C'); AMBER_F = Font(color='9C5700')
RED   = PatternFill('solid', fgColor='FFC7CE'); RED_F   = Font(color='9C0006')
GREY  = PatternFill('solid', fgColor='D9D9D9'); GREY_F  = Font(color='595959')
GREY_TXT = Font(color='808080', italic=True)
GREY_FILL = PatternFill('solid', fgColor='F2F2F2')

def grey_group(ws, r, cols):
    """Grey a group of cells that is not the basis of the row's verdict."""
    for j in cols:
        c = ws.cell(r, j)
        c.font = GREY_TXT
        c.fill = GREY_FILL
FMT_GBP = u'£#,##0.00'
FMT_SC  = u'#,##0.00"¢"'
FMT_RATIO = '0.00"x"'
FMT_YEAR = '0'

SCOPE_NOTE = ('Cost scope: the purchase/construction and upkeep of the object itself only. Crew and '
              'staff wages (config/staff.tab), fuel and energy (config/fuel.tab), and station/depot '
              'staff are simulated separately and are NOT included in these fields '
              '(New/ai/vehicle-cost-model.md "What these costs exclude"; '
              'New/ai/cost-balancing-register.md "Cost scope").')

# Index sheet column order. The engine uses a separate series for each object type.
SERIES_ORDER = [
    ('general', 'General'),
    ('vehicle purchase', 'Vehicle purchase'),
    ('infrastructure', 'Infrastructure'),
    ('buildings', 'Buildings'),
    ('goods rate', 'Goods rate'),
    ('passenger fare', 'Passenger fare'),
    ('mail rate', 'Mail rate'),
    ('city land', 'City land'),
    ('country land', 'Country land'),
]
SERIES_COL = {k: i + 2 for i, (k, _) in enumerate(SERIES_ORDER)}   # A=Year, B.. are series

# ---------------------------------------------------------------- prices.tab
def load_series():
    """Every price series in prices.tab, expanded to one value per year with the
    engine's rule: linear between listed years, first value before, last after."""
    text = open(PRICES_TAB, encoding='utf-8', errors='replace').read()
    raw = {}
    for m in re.finditer(r'(?m)^([A-Za-z][A-Za-z ]*)=(.*)$', text):
        key = m.group(1).strip()
        nums = [int(x) for x in m.group(2).split(',') if x.strip().lstrip('-').isdigit()]
        if len(nums) >= 4:
            raw[key] = list(zip(nums[0::2], nums[1::2]))
    out = {}
    for key, pairs in raw.items():
        pairs.sort()
        d = {}
        for y in range(1500, 2151):
            if y <= pairs[0][0]:
                d[y] = float(pairs[0][1])
            elif y >= pairs[-1][0]:
                d[y] = float(pairs[-1][1])
            else:
                for (y0, v0), (y1, v1) in zip(pairs, pairs[1:]):
                    if y0 <= y <= y1:
                        d[y] = v0 + (v1 - v0) * (y - y0) / (y1 - y0)
                        break
        out[key] = d
    return out

# ---------------------------------------------------------------- en.tab
def load_english_names():
    names = {}
    try:
        lines = open(EN_TAB, encoding='utf-8', errors='replace').read().splitlines()
    except OSError:
        return names
    key = None
    for line in lines:
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        if key is None:
            key = s
        else:
            names[key] = s
            key = None
    return names

# ---------------------------------------------------------------- data loading
def pick(d, *names):
    low = {str(k).lower().strip(): v for k, v in d.items() if k}
    for n in names:
        v = low.get(n.lower())
        if v not in (None, ''):
            return v
    return ''

def num(v):
    try:
        return float(str(v).replace(',', '').replace('£', '').replace('GBP', '').strip())
    except (TypeError, ValueError):
        return None

def load_inventory():
    rows = list(csv.DictReader(open(INVENTORY, encoding='utf-8-sig')))
    out = []
    for r in rows:
        if r.get('class') == 'engine-settings':
            nm = (r.get('name') or '')
            fn = (r.get('file') or '')
            if fn != 'simuconf.tab':
                continue
            if not re.match(r'^(cost_|forge_cost_|maintenance_building)', nm):
                continue
        out.append(r)
    # Objects with no cost= are skipped by the inventory scan, which hides exactly the
    # infrastructure that is hardest to price (26 depots, 7 headquarters, 23 station
    # objects). Add them from the attribute table so the audit can show them.
    seen = {r.get('name') for r in out}
    feat = os.path.join(HERE, 'infrastructure-features.csv')
    classes = {'depot': 'depots', 'building': 'headquarters', 'station': 'stops-stations/stations'}
    if os.path.exists(feat):
        frows = list(csv.DictReader(open(feat, encoding='utf-8-sig')))
        # some inventory rows kept the file name instead of the object name; recover them by
        # matching the one feature row with the same cost and object type
        for r in out:
            nm = r.get('name') or ''
            if nm and not nm.lower().endswith('.dat'):
                continue
            try:
                c = float(r.get('cost') or '')
            except (TypeError, ValueError):
                continue
            cands = [f['name'] for f in frows
                     if f.get('obj_type') == r.get('obj_type')
                     and f.get('dat_cost') and abs(float(f['dat_cost']) - c) < 1]
            if len(cands) == 1:
                r['name'] = cands[0]
                seen.add(cands[0])
        for r in frows:
            nm = r.get('name')
            if not nm or nm in seen:
                continue
            cls = classes.get(r.get('obj_type'))
            if not cls:
                continue
            out.append({'class': cls, 'folder': r.get('class', ''), 'file': '',
                        'obj_type': r.get('obj_type', ''), 'name': nm,
                        'waytype': r.get('waytype', ''), 'cost': r.get('dat_cost', ''),
                        'maintenance': r.get('dat_maintenance', ''),
                        'intro_date': r.get('intro_year', '')})
            seen.add(nm)
    return out

def load_price_rows(full=False):
    """Measured rows for matching, or the complete set for the display sheet.

    `full=False` returns the curated register plus research passes 1-6, which is the set the
    matcher uses. `full=True` adds every research pass file, deduplicated on domain, kind, name,
    year and price, for the Research prices sheet. The uncurated passes carry rows that have not
    been checked for binding (a ship's engine builder, a US locomotive price in dollars), so they
    are displayed rather than matched.
    """
    if not full:
        rows = []
        for path in (PRICE_ROWS, RESEARCH_ROWS, RESEARCH_ROWS_2, RESEARCH_ROWS_3,
                     RESEARCH_ROWS_6, RESEARCH_ROWS_5, RESEARCH_ROWS_4, RESEARCH_ROWS_4B):
            if os.path.exists(path):
                with open(path, encoding='utf-8-sig') as f:
                    for row in csv.DictReader(f):
                        row['_source'] = os.path.basename(path)
                        rows.append(row)
        return rows

    paths = [PRICE_ROWS]
    passes = []
    for name in os.listdir(HERE):
        m = re.match(r'research-pricing-rows(?:-(\d+b?))?\.csv$', name)
        if m:
            tag = m.group(1) or '1'
            passes.append(((int(re.sub(r'\D', '', tag)), tag), os.path.join(HERE, name)))
    paths += [p for _, p in sorted(passes)]

    rows, seen = [], set()
    for path in paths:
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                key = ((row.get('domain') or '').strip().lower(),
                       (row.get('kind') or '').strip().lower(),
                       (row.get('name_or_item') or '').strip().lower(),
                       str(row.get('year') or '').strip(),
                       str(row.get('price') or '').strip())
                if key in seen:
                    continue
                seen.add(key)
                row['_source'] = os.path.basename(path)
                rows.append(row)
    return rows

# ---------------------------------------------------------------- families
Fam = namedtuple('Fam', 'cap_num cap_cell m_num m_cell km_num km_cell series unit')

def families(row):
    """Conversion family: numeric factors (for extrapolation maths), the Params cell
    that holds each factor (so the tile/bits settings are switchable in one place),
    the engine price series that indexes the object, and the unit note."""
    obj = pick(row, 'obj_type', 'obj', 'type').lower()
    folder = pick(row, 'folder', 'dir').lower().replace('\\', '/')
    name = pick(row, 'name').lower()
    if pick(row, 'class') == 'engine-settings' or obj in ('settings', 'engine-setting'):
        if name.startswith('forge_cost_'):
            return Fam(FAC_WAY_KM, '$B$15', FAC_WAY_MONTH, '$B$17', None, None,
                       'infrastructure', 'per km (forge: formation for a new way)')
        return Fam(FAC_UNSCALED, '$B$16', FAC_UNSC_MONTH, '$B$19', None, None,
                   'general', 'per action or object (engine setting)')
    if obj == 'vehicle':
        return Fam(FAC_SCALED, '$B$12', FAC_VEH_MONTH, '$B$14', FAC_UNSCALED, '$B$16',
                   'vehicle purchase', 'per vehicle')
    if obj in ('way', 'bridge', 'tunnel', 'way-object', 'powerline', 'elevated-way', 'canal', 'pier'):
        return Fam(FAC_WAY_KM, '$B$15', FAC_WAY_MONTH, '$B$17', None, None,
                   'infrastructure', 'per km (length-based)')
    if obj in ('roadsign', 'signal'):
        return Fam(FAC_SCALED, '$B$12', FAC_BLD_MONTH, '$B$18', None, None,
                   'infrastructure', 'per object (scaled)')
    if 'depot' in folder or 'depot' in name or 'headquarter' in name or 'hq' in name:
        return Fam(FAC_UNSCALED, '$B$16', FAC_UNSC_MONTH, '$B$19', None, None,
                   'buildings', 'per object (unscaled)')
    if any(k in folder for k in ('citybuilding', 'city-building', 'attraction', 'town', 'groundobj', 'tree')):
        return Fam(FAC_UNSCALED, '$B$16', FAC_UNSC_MONTH, '$B$19', None, None,
                   'buildings', 'per object (unscaled)')
    return Fam(FAC_SCALED, '$B$12', FAC_BLD_MONTH, '$B$18', None, None,
               'buildings', 'per object (scaled)')

def series_vlookup(year_cell, series):
    return 'IFERROR(VLOOKUP({y},Index!$A:${last},{c},FALSE),"")'.format(
        y=year_cell, c=SERIES_COL[series], last=get_column_letter(len(SERIES_ORDER) + 1))

def deflate_formula(value_cell, year_cell, series):
    """GBP of `year` -> GBP of 1900, using the series the engine applies to this object."""
    return ('=IF(AND(ISNUMBER({v}),ISNUMBER({y})),'
            'IFERROR({v}*100/{lk},""),"")').format(v=value_cell, y=year_cell,
                                                   lk=series_vlookup(year_cell, series))

def load_forge_costs():
    """simuconf.tab forge_cost_* per waytype: the per-tile formation charge."""
    values = {}
    path = os.path.join(BASE, 'New', 'config', 'simuconf.tab')
    if os.path.exists(path):
        for line in open(path, encoding='utf-8', errors='replace'):
            m = re.match(r'^\s*forge_cost_([a-z]+)\s*=\s*(\d+)', line, re.I)
            if m:
                values[m.group(1).lower()] = int(m.group(2))
    return values

FORGE = load_forge_costs()
FORGE_KEY = {
    'track': 'track', 'road': 'road', 'water': 'water', 'air': 'air',
    'tram_track': 'tram', 'tram': 'tram', 'maglev_track': 'maglev', 'maglev': 'maglev',
    'narrowgauge_track': 'narrowgauge', 'narrowgauge': 'narrowgauge',
    'monorail_track': 'monorail', 'monorail': 'monorail',
}

def forge_for(row):
    """Forge (formation) charge per tile for a plain way; 0 for everything else.
    Bridges, tunnels, piers and way objects do not pay it (wegbauer/tunnel_builder).

    Water is zero by the decision of 2026-11-24: for a canal the forging is the building and
    there is no separate formation, so the whole channel construction is in the way object.
    The simuconf.tab setting was changed to 0 on 2026-11-27 in both the source and the live
    runtime copy; this override keeps the workbook aligned with it.
    """
    if pick(row, 'obj_type', 'obj', 'type') != 'way':
        return 0
    wt = (pick(row, 'waytype') or '').lower()
    if wt == 'water':
        return 0
    if wt == 'road':
        # Road and air research 2026-11-27 section 4: the bed of an unsurfaced track of
        # bridleway width, GBP79.26/km, the only per-waytype value no greater than the cheapest
        # road. The simuconf.tab setting is still 315,000; this override follows the research.
        return 20000
    if wt == 'air':
        # Road and air research 2026-11-27 section 6: 76 per cent of the grass taxiway's whole
        # construction, GBP435.94/km. The simuconf.tab setting is still 1,875,000.
        return 110000
    return FORGE.get(FORGE_KEY.get(wt, ''), 0)

# ---------------------------------------------------------------- sheet helpers
def write_index_sheet(wb):
    ws = wb.create_sheet('Index')
    heads = ['Year'] + [label for _, label in SERIES_ORDER]
    for j, h in enumerate(heads, start=1):
        c = ws.cell(1, j, h); c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = Alignment(wrap_text=True)
    ws.cell(1, len(heads) + 1, 'Source: New/config/prices.tab, engine-style linear interpolation between '
                               'listed years. These are the series the engine applies, by object type: '
                               'vehicle cost -> vehicle purchase; vehicle running/fixed -> general; '
                               'ways/tunnels/bridges/way objects/signals -> infrastructure; buildings -> '
                               'buildings. 1900 = 100.')
    for r, y in enumerate(range(1500, 2151), start=2):
        ws.cell(r, 1, y).number_format = FMT_YEAR
        for j, (key, _) in enumerate(SERIES_ORDER, start=2):
            ws.cell(r, j, round(SERIES_DB[key].get(y, 100.0), 3))
    ws.column_dimensions['A'].width = 8
    for j in range(2, len(heads) + 1):
        ws.column_dimensions[get_column_letter(j)].width = 16
    ws.freeze_panes = 'B2'

PARAM_ROWS = [
    ('RATE_CAPITAL', RATE_CAPITAL, '1 Simucredit = GBP 0.396311 in 1900 - capital and annualised amounts'),
    ('RATE_REVENUE', RATE_REVENUE, '1 Simucredit = GBP 0.005208 in 1900 - revenue and per-km amounts'),
    ('RATIO', '=B2/B3', 'Ratio of the two rates = time compression 76.09 (a diagnostic, NOT a scale factor)'),
    ('MONTHS_PER_YEAR', 12, 'Game months per source year when converting an annual figure to a monthly one (M2)'),
    ('TOL_MATCH', TOL_MATCH, 'In-game within +/-25% of the derived price = green'),
    ('TOL_NEAR', TOL_NEAR, 'Within +/-50% = amber; beyond = red'),
    ('METERS_PER_TILE', MPT, 'ENGINE SETTING. Pakset config/simuconf.tab says 125. All SC factors below follow this cell.'),
    ('BITS_PER_MONTH', BITS_PER_MONTH, 'ENGINE SETTING. Pakset config/simuconf.tab says 22.'),
    ('BASE_METERS_PER_TILE', BASE_MPT, 'ENGINE SETTING. base_meters_per_tile = 1000.'),
    ('BASE_BITS_PER_MONTH', BASE_BITS, 'ENGINE SETTING. base_bits_per_month = 18.'),
    ('FACTOR_SCALED', '=B8/1000/100', 'Scaled object: .dat -> SC (price = .dat x mpt/1000, display /100). '
                                      'Stations, signalboxes, signals, industries, vehicles.'),
    ('FACTOR_MONTH', '=2^(B9-B11)/INT(B10/B8)', 'calc_adjusted_monthly_figure: 2^(bits-18) / INT(base_mpt/mpt) = 2 here.'),
    ('FACTOR_VEHICLE_MONTH', '=B12*B13', 'Vehicle fixed_cost -> SC per game month (.dat x 0.0025 at 125/22).'),
    ('FACTOR_WAY_KM', '=B8/1000*8/100', 'Way/tunnel/bridge/way-object -> SC per km (the tile factor cancels: 0.01 at any mpt).'),
    ('FACTOR_UNSCALED', 0.01, 'Unscaled object (depots, HQ, city buildings) and per-dat action: 1/100.'),
    ('FACTOR_WAY_MONTH', '=B15*B13', 'Way/tunnel/bridge/way-object maintenance -> SC per km per month (0.02 at 125/22).'),
    ('FACTOR_BUILDING_MONTH', '=B12*B13', 'Building (station, signalbox, industry) maintenance -> SC per object per month.'),
    ('FACTOR_UNSCALED_MONTH', '=B16*B13', 'Unscaled object maintenance -> SC per object per month (0.02 at 125/22).'),
    ('MILES_TO_KM', 1.609344, 'Convert GBP per mile to GBP per km by dividing by this'),
]

def write_params_sheet(wb):
    ws = wb.create_sheet('Params')
    for i, h in enumerate(('Parameter', 'Value', 'Meaning / source'), start=1):
        c = ws.cell(1, i, h); c.font = HDR_FONT; c.fill = HDR_FILL
    for i, (k, v, note) in enumerate(PARAM_ROWS, start=2):
        ws.cell(i, 1, k).font = LABEL_FONT
        ws.cell(i, 2, v)
        ws.cell(i, 3, note).alignment = WRAP
    # Forge (formation) charges: read from simuconf.tab; shown here for reference.
    rec = {
        'track': '76,000-101,000', 'narrowgauge': '76,000-114,000', 'road': '250,000-380,000',
        'tram': '150,000-300,000', 'water': '0 (decision 2026-11-24; whole construction in the way object)',
        'air': '1,500,000-2,250,000', 'monorail': '90,000-125,000', 'maglev': '90,000-125,000',
    }
    r = len(PARAM_ROWS) + 2
    for key in ('track', 'road', 'water', 'tram', 'narrowgauge', 'maglev', 'monorail', 'air'):
        if key in FORGE:
            ws.cell(r, 1, 'FORGE_' + key.upper()).font = LABEL_FONT
            if key == 'water':
                value = 0
                note = ('forge_cost_water: 0 per the user direction of 2026-11-27 and the recorded '
                        'decision of 2026-11-24. For a canal the forging is the building and there '
                        'is no separate formation, so the whole construction is in the way object. '
                        'The simuconf.tab setting was changed to 0 on 2026-11-27 in both the source '
                        'and the live runtime copy.')
            elif key == 'road':
                value = 20000
                note = ('forge_cost_road: 20,000 raw = GBP79.26/km, the road and air research '
                        'recommendation of 2026-11-27: the bed of an unsurfaced track of bridleway '
                        'width, 79 per cent of the bridleway and 72 per cent of Telford\'s measured '
                        'bed-preparation rate. The live simuconf.tab setting is still 315,000; its '
                        'change is outstanding.')
            elif key == 'air':
                value = 110000
                note = ('forge_cost_air: 110,000 raw = GBP435.94/km, the road and air research '
                        'recommendation of 2026-11-27: 76 per cent of the grass taxiway, the '
                        'formation share of a grass strip. The live simuconf.tab setting is still '
                        '1,875,000; its change is outstanding.')
            else:
                value = FORGE[key]
                note = ('forge_cost_%s in simuconf.tab: formation charge per tile, before the '
                        'infrastructure index. Charged on plain and elevated ways; bridges, tunnels, '
                        'piers and way objects do not pay it. Synthesis recommendation: %s.'
                        % (key, rec.get(key, '-')))
            ws.cell(r, 2, value)
            ws.cell(r, 3, note).alignment = WRAP
            r += 1
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 12
    ws.column_dimensions['C'].width = 110
    ws.freeze_panes = 'A2'

def write_readme(wb, title, extra_lines):
    ws = wb.create_sheet('README', 0)
    ws['A1'] = title; ws['A1'].font = TITLE_FONT
    lines = [
        'Working paper for the cost-balancing project (New/ai/cost-balancing-register.md).',
        'Every in-game item with a cost of the relevant kind appears as a row on the type sheets.',
        '',
        'COST SCOPE',
        'Each row costs the purchase/construction and upkeep of the object itself ONLY. Crew and staff',
        'wages are simulated separately (config/staff.tab), as is fuel and energy (config/fuel.tab);',
        'neither is included in vehicle runningcost/fixed_cost. Building maintenance is the upkeep of the',
        'fabric only. See New/ai/vehicle-cost-model.md and New/ai/cost-balancing-register.md "Cost scope".',
        '',
        'MODEL - .DAT TO IN-GAME (derived from the ex-15 engine source, 2026-11-22)',
        '1. A .dat money value is the 1900 nominal (config/prices.tab line 2: 100% = the .dat price).',
        '2. At load, karte_t::set_scale multiplies cost, maintenance and fixed_cost by',
        '   meters_per_tile/1000 (integer). running_cost is NOT scaled. Display then divides by 100.',
        '3. At display/charge the engine applies the object type\'s OWN price series for the month:',
        '      vehicle cost ....................... vehicle purchase',
        '      vehicle running / fixed ............ general (vehicle maintenance is commented out)',
        '      ways, tunnels, bridges, way objects, signals, roadsigns ... infrastructure',
        '      buildings (stations, signalboxes, depots, HQ, city buildings, industries) ... buildings',
        '      engine settings .................... general (forge costs: infrastructure)',
        '4. Per-month charges are additionally multiplied by calc_adjusted_monthly_figure =',
        '   2^(bits_per_month-18) / INT(base_meters_per_tile / meters_per_tile) = 2 at 125 / 22 bits.',
        '   This covers vehicle fixed_cost, way/tunnel/bridge/way-object maintenance and building',
        '   maintenance (finance_t::get_maintenance_with_bits; simhalt.cc).',
        '5. Therefore, at 125 m/tile and 22 bits (all cells driven by the Params sheet):',
        '      vehicle cost      .dat x 0.00125 x index/100',
        '      vehicle fixed     .dat x 0.0025  x index/100  per game month',
        '      vehicle running   .dat x 0.01    x index/100  per km',
        '      way cost          .dat x 0.01    x index/100  per km',
        '      way + forge       (.dat cost + forge_cost_waytype) x 0.01 x index/100 per km',
        '      way maintenance   .dat x 0.02    x index/100  per km per month',
        '      building cost     .dat x 0.00125 x index/100',
        '      building maint.   .dat x 0.0025  x index/100  per month',
        '6. THE INDEX IS A TYPE INDEX, NOT ALWAYS general. A historical price must be brought to 1900',
        '   with the same series the engine applies to that object. Using general for everything',
        '   mismatches the .dat basis wherever the series diverge: by 2026 vehicle purchase is 0.90x',
        '   general, infrastructure 0.57x general and buildings 1.35x general. This was the error in',
        '   the first version of these workbooks.',
        '',
        'WORKED EXAMPLE - CSLR 1890 Tube Locomotive, January 1891',
        '  .dat cost 650,000, fixed_cost 10,677, runningcost 51. Index at Jan 1891: vehicle purchase 80,',
        '  general 97. At 125 m/tile: price = 650,000 x 0.00125 x 0.80 = 650.00; running = 51 x 0.01 x',
        '  0.97 = 0.49/km; fixed = 10,677 x 0.0025 x 0.97 = 25.86/month. With meters_per_tile = 120 the',
        '  same chain gives 624.00 / 0.49 / 24.84, which is the figure on the user\'s 2026-11-22',
        '  screenshot; runningcost is the control, because it is not tile-scaled. Setting Params B8 to',
        '  120 reproduces it here (24.86 for the fixed charge: the engine truncates to integers at each',
        '  step, giving 24.84, while the workbook multiplies exactly).',
        '',
        'COLUMNS',
        'Name (English) | base name | .dat file | Obj= | intro year | status (a)-(d) | in-game .dat value |',
        'forge cost per tile | in-game SC @1900 way only | in-game SC @1900 way + forge | in-game SC',
        '@ intro | index @ intro. Then two parallel groups:',
        '  MEASURED  price + year -> GBP @1900 -> SC @1900 -> suggested .dat (total and way-only)',
        '  CLASS     class-derived price + year + basis -> GBP @1900 -> SC @1900 -> suggested .dat',
        '            (total and way-only)',
        'then the two ratios, the Match verdict, the source reference and notes.',
        'Every measured and class figure is deflated to 1900, the same basis as the .dat value. The two',
        '"@ intro" columns are the only ones at a different date: they apply the engine price series at the',
        'object introduction date and show what the game displays then. The class group is greyed out',
        'wherever a measured price exists, because the Match verdict then uses the measured price.',
        '"Suggested .dat" is the value the .dat field would need to be for that side to match the target;',
        'compare it directly with the in-game .dat column.',
        '',
        'SHEET "Snippet prices (6521)"',
        'The complete register of the forum thread "A snippet of relative pricing information"',
        '(https://forum.simutrans.com/index.php?topic=6521.0): all 416 rows, including those with no',
        'absolute price or no stated year, with the numeric price, the 1900 conversion and the SC /',
        'suggested .dat figures where they can be computed, and the object each row binds to (if any).',
        'Nothing from the thread is omitted because it failed to bind.',
        '',
        'SHEET "Research prices (all passes)"',
        'Every measured row: the evidence register plus all research passes 1-38, deduplicated on',
        'domain, kind, item, year and price. The register rows are the merged subset; the per-pass',
        'files carry the full record, including passes (aircraft, ships, overhauls, .dat comments)',
        'that were never merged. Most are class-level evidence and do not bind to one object.',
        '',
        'COLOUR CODING (Match column; priority: source-derived first, then class-derived)',
        'Green = within +/-25%. Amber = within +/-50%. Red = beyond. Grey = no data.',
        '',
        'STATUS COLUMNS (a)-(d): (a) balanced, (b) class data, (c) item data, (d) extrapolation possible.',
        '',
        'OPEN QUESTIONS affecting every figure: M1 (maintenance display confirmation); M2 (which rate a',
        'per-month charge uses). Vehicle .dat values ARE engine-scaled (karte_t::set_scale); the legacy',
        'x8 factor of Vehicle cost table.ods is that engine scale.',
        '',
    ] + extra_lines
    for i, line in enumerate(lines, start=3):
        ws.cell(i, 1, line)
    ws.column_dimensions['A'].width = 120

# ---- column plans -----------------------------------------------------------
LEAD_COLS = [
    ('Name (English)', 36), ('Base name (untranslated)', 30), ('Object key (.dat)', 26), ('Obj=', 11), ('Intro', 7),
    ('(a)\nbalanced', 9), ('(b)\nclass data', 9), ('(c)\nitem data', 9), ('(d)\nextrapolate', 9),
]
CAP_COLS = LEAD_COLS + [
    ('In-game cost\n(.dat/tile)', 12), ('Forge cost\n(.dat/tile)', 12),
    ('In-game SC @1900\n(way only)', 13), ('In-game SC @1900\n(way + forge)', 14),
    ('In-game SC\n@ intro', 12), ('Index @\nintro (%)', 10),
    ('Measured price\n(GBP)', 13), ('Measured\nyear', 8), ('Measured GBP\n@1900', 12),
    ('Measured SC\n@1900', 13), ('Suggested .dat\ntotal (measured)', 13),
    ('Suggested .dat\nway only (measured)', 13),
    ('Class price\n(GBP)', 13), ('Class\nyear', 8), ('Class basis', 26), ('Class GBP\n@1900', 12),
    ('Class SC\n@1900', 13), ('Suggested .dat\ntotal (class)', 13),
    ('Suggested .dat\nway only (class)', 13),
    ('In-game /\nmeasured', 10), ('In-game /\nclass', 10), ('Match (priority)', 18),
    ('Source reference', 32), ('Notes', 46),
    ('Intro\nmonth', 6),
]
CAP_L = dict(dat='J', forge='K', sc_way='L', sc='M', sc_intro='N', idx_intro='O',
             src='P', src_yr='Q', src900='R', src_sc='S', sug_src='T', sug_src_way='U',
             ext='V', ext_yr='W', ext_basis='X', ext900='Y', ext_sc='Z', sug_ext='AA', sug_ext_way='AB',
             r_src='AC', r_ext='AD', match='AE', ref='AF', notes='AG', intro_m='AH')
CAP_FMT = dict(dat_cols=(10, 11, 20, 21, 27, 28), gbp_cols=(16, 18, 22, 25), sc_cols=(12, 13, 19, 26),
               ratio_cols=(29, 30), year_cols=(5, 17, 23), num_cols=(15, 34))

MAINT_COLS = LEAD_COLS + [
    ('In-game maint.\n(.dat)', 12), ('In-game fixed SC\n@1900 /month', 13),
    ('In-game per-km\n(.dat)', 11), ('In-game per-km\nSC @1900', 12),
    ('In-game fixed\nSC @ intro', 13), ('In-game per-km\nSC @ intro', 13), ('Index @\nintro (%)', 10),
    ('Measured fixed\n(GBP/yr)', 13), ('Fixed\nyear', 8), ('Measured fixed\nGBP @1900', 12),
    ('Measured fixed\nSC @1900 /month', 13), ('Suggested .dat\nfixed (measured)', 13),
    ('Measured per-km\n(GBP)', 12), ('Per-km\nyear', 8), ('Measured per-km\nGBP @1900', 12),
    ('Measured per-km\nSC @1900', 12), ('Suggested .dat\nper-km (measured)', 13),
    ('Class fixed\n(GBP/yr)', 12), ('Class fixed\nyear', 8), ('Class per-km\n(GBP)', 12),
    ('Class per-km\nyear', 8), ('Class basis', 24),
    ('Class fixed\nSC @1900 /month', 12), ('Class per-km\nSC @1900', 12),
    ('Suggested .dat\nfixed (class)', 13), ('Suggested .dat\nper-km (class)', 13),
    ('In-game/measured\nfixed', 10), ('In-game/measured\nper-km', 10),
    ('In-game/class\nfixed', 10), ('In-game/class\nper-km', 10),
    ('Match (priority)', 18),
    ('Source reference', 32), ('Notes', 46),
    ('Intro\nmonth', 6),
]
MAINT_L = dict(dat='J', sc='K', km_dat='L', km_sc='M',
               f_intro='N', k_intro='O', idx_intro='P',
               src_f='Q', src_f_yr='R', src_f900='S', src_f_sc='T', sug_f='U',
               src_k='V', src_k_yr='W', src_k900='X', src_k_sc='Y', sug_k='Z',
               ext_f='AA', ext_f_yr='AB', ext_k='AC', ext_k_yr='AD', ext_basis='AE',
               ext_f_sc='AF', ext_k_sc='AG', sug_ef='AH', sug_ek='AI',
               r_sf='AJ', r_sk='AK', r_ef='AL', r_ek='AM', match='AN', ref='AO', notes='AP',
               intro_m='AQ')
MAINT_FMT = dict(dat_cols=(10, 12, 21, 26, 34, 35), gbp_cols=(17, 19, 22, 24, 27, 29),
                 sc_cols=(11, 13, 14, 15, 20, 25, 32, 33), ratio_cols=(36, 37, 38, 39),
                 year_cols=(5, 18, 23, 28, 30), num_cols=(16, 43))

def style_header(ws, cols, row):
    for j, (name, width) in enumerate(cols, start=1):
        c = ws.cell(row, j, name)
        c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
        ws.column_dimensions[get_column_letter(j)].width = width
    ws.row_dimensions[row].height = 40

def style_data_area(ws, ncols, first_row, last_row, fmt):
    for r in range(first_row, last_row + 1):
        for j in range(1, ncols + 1):
            c = ws.cell(r, j)
            c.border = BORDER
            c.alignment = WRAP
            if j in fmt['dat_cols']:
                c.number_format = '#,##0'
            if j in fmt['gbp_cols']:
                c.number_format = FMT_GBP
            if j in fmt.get('sc_cols', ()):
                c.number_format = FMT_SC
            if j in fmt['ratio_cols']:
                c.number_format = FMT_RATIO
            if j in fmt['year_cols']:
                c.number_format = FMT_YEAR
            if j in fmt.get('num_cols', ()):
                c.number_format = '0'

def add_match_formatting(ws, match_col, ratio_cols, first_row, last_row):
    m = get_column_letter(match_col)
    rng = '%s%d:%s%d' % (m, first_row, m, last_row)
    for text, fill, font in (('MATCH', GREEN, GREEN_F), ('NEAR', AMBER, AMBER_F),
                             ('FAR', RED, RED_F), ('no data', GREY, GREY_F)):
        ws.conditional_formatting.add(rng, FormulaRule(
            formula=['ISNUMBER(SEARCH("%s",$%s%d))' % (text, m, first_row)],
            fill=fill, font=font, stopIfTrue=True))
    for col in ratio_cols:
        L = get_column_letter(col)
        rng = '%s%d:%s%d' % (L, first_row, L, last_row)
        ws.conditional_formatting.add(rng, CellIsRule(
            operator='between', formula=[str(1 - TOL_MATCH), str(1 + TOL_MATCH)], fill=GREEN, font=GREEN_F))
        ws.conditional_formatting.add(rng, CellIsRule(
            operator='between', formula=[str(1 - TOL_NEAR), str(1 + TOL_NEAR)], fill=AMBER, font=AMBER_F))
        ws.conditional_formatting.add(rng, CellIsRule(
            operator='greaterThan', formula=[str(1 + TOL_NEAR)], fill=RED, font=RED_F))
        ws.conditional_formatting.add(rng, CellIsRule(
            operator='lessThan', formula=[str(1 - TOL_NEAR)], fill=RED, font=RED_F))
        ws.conditional_formatting.add(rng, FormulaRule(
            formula=['NOT(ISNUMBER($%s%d))' % (L, first_row)], fill=GREY, stopIfTrue=True))

def sheet_header_block(ws, title, lines, rate_cells):
    ws['A1'] = title; ws['A1'].font = TITLE_FONT
    r = 2
    for label, value in rate_cells:
        ws.cell(r, 1, label).font = LABEL_FONT
        ws.cell(r, 2, value)
        r += 1
    ws.cell(r, 1, 'Scope:').font = LABEL_FONT
    ws.cell(r, 2, lines)
    return r + 2

# ---------------------------------------------------------------- row fill
def item_names(row, en):
    base = pick(row, 'name', 'object', 'title') or pick(row, 'file')
    eng = en.get(base) or en.get(base.replace('_', ' ')) or ''
    return eng, base

def intro_year(row):
    v = pick(row, 'intro_date', 'intro')
    m = re.match(r'\s*(\d{4})', str(v))
    return int(m.group(1)) if m else ''

def intro_month(row):
    v = pick(row, 'intro_date', 'intro')
    m = re.search(r'-(\d{1,2})', str(v))
    return int(m.group(1)) if m else ''

def index_at_intro_formula(year_cell, month_cell, series):
    """Engine interpolation at the introduction month: value at the year, plus the
    year-on-year delta prorated by (month-1)/12, truncated (C++ integer division)."""
    last = get_column_letter(len(SERIES_ORDER) + 1)
    c = SERIES_COL[series]
    v0 = 'VLOOKUP({y},Index!$A:${l},{c},FALSE)'.format(y=year_cell, l=last, c=c)
    v1 = 'VLOOKUP({y}+1,Index!$A:${l},{c},FALSE)'.format(y=year_cell, l=last, c=c)
    return ('IFERROR(IF(ISNUMBER({y}),'
            '{v0}+TRUNC(({v1}-{v0})*(IF(ISNUMBER({m}),{m},1)-1)/12),""),"")'
            ).format(y=year_cell, v0=v0, v1=v1, m=month_cell)

def build_cap_sheet(wb, name, rows, prows, ev, en):
    ws = wb.create_sheet(name)
    L = CAP_L
    HDR = sheet_header_block(ws, name + ' - capital costs', SCOPE_NOTE,
                             [('Rate (1 SC = GBP1900):', '=Params!$B$2'),
                              ('Factor used:', 'per-row, from Params B12/B15/B16 (see README)')])
    ws.cell(HDR - 1, 2, 'Capital timescale. All measured and class figures are deflated to 1900 (the .dat '
                        'basis); the "@ intro" columns apply the engine price series at the introduction date. '
                        'For plain ways the in-game figure includes the separate forge_cost_* formation charge '
                        '(per tile, from simuconf.tab); the way-only suggested .dat shows cost net of it.')
    style_header(ws, CAP_COLS, HDR)
    r = HDR + 1
    for row in rows:
        fill_cap_row(ws, r, row, prows, ev, en)
        r += 1
    last = r - 1
    if last >= HDR + 1:
        style_data_area(ws, len(CAP_COLS), HDR + 1, last, CAP_FMT)
        add_match_formatting(ws, 31, (29, 30), HDR + 1, last)
    ws.column_dimensions['AH'].hidden = True       # intro-month helper
    ws.freeze_panes = 'B%d' % (HDR + 1)

def build_maint_sheet(wb, name, rows, prows, ev, en):
    ws = wb.create_sheet(name)
    HDR = sheet_header_block(ws, name + ' - maintenance costs', SCOPE_NOTE,
                             [('Fixed rate (1 SC = GBP1900):', '=Params!$B$2'),
                              ('Per-km rate (1 SC = GBP1900):', '=Params!$B$3')])
    ws.cell(2, 3, 'Capital timescale for fixed/annual figures (open question M2).')
    ws.cell(3, 3, 'Revenue timescale for vehicle per-km figures; infrastructure per-km maintenance uses the capital rate - change this cell to =Params!$B$2 for those sheets if desired.')
    ws.cell(5, 2, 'All measured and class figures are deflated to 1900 (the .dat basis); the "@ intro" columns '
                  'apply the engine price series at the introduction date.')
    style_header(ws, MAINT_COLS, HDR)
    r = HDR + 1
    for row in rows:
        fill_maint_row(ws, r, row, prows, ev, en)
        r += 1
    last = r - 1
    if last >= HDR + 1:
        style_data_area(ws, len(MAINT_COLS), HDR + 1, last, MAINT_FMT)
        add_match_formatting(ws, 40, (36, 37, 38, 39), HDR + 1, last)
    ws.column_dimensions['AQ'].hidden = True       # intro-month helper
    ws.freeze_panes = 'B%d' % (HDR + 1)

def fill_cap_row(ws, r, row, prows, ev, en):
    L = CAP_L
    eng, base = item_names(row, en)
    fam = families(row)
    cls = pick(row, 'class', 'folder')
    ws.cell(r, 1, eng or base)
    ws.cell(r, 2, base)
    ws.cell(r, 3, pick(row, 'file', 'filename', 'path'))
    ws.cell(r, 4, pick(row, 'obj_type', 'obj', 'type'))
    ws.cell(r, 5, intro_year(row))
    for j, v in enumerate(ev.status(cls, base), start=6):
        ws.cell(r, j, v)

    dat = num(pick(row, 'cost', 'cost_value'))
    if dat is None and pick(row, 'obj_type', 'obj', 'type') in ('engine-setting',):
        dat = num(pick(row, 'value'))
    if pick(row, 'obj_type', 'obj', 'type') in ('engine-setting',) and pick(row, 'name').startswith('maintenance_'):
        dat = None          # upkeep setting, not a capital cost
    forge = forge_for(row)
    ws.cell(r, 10, dat if dat is not None else '')
    # Write 0 as 0, not blank: water is deliberately zero by the 2026-11-24 decision, and a blank
    # would read as "no forge" rather than "forge set to zero".
    ws.cell(r, 11, forge if forge is not None else '')
    ws.cell(r, 12, '=IF(ISNUMBER({d}{r}),{d}{r}*Params!{fac},"")'.format(
        d=L['dat'], r=r, fac=fam.cap_cell))
    ws.cell(r, 13, '=IF(ISNUMBER({d}{r}),({d}{r}+N({f}{r}))*Params!{fac},"")'.format(
        d=L['dat'], f=L['forge'], r=r, fac=fam.cap_cell))

    # Engine display at the introduction date: 1900 SC x index(intro)/100.
    ws.cell(r, 34, intro_month(row))
    ws.cell(r, 15, '=' + index_at_intro_formula('E%d' % r, 'AH%d' % r, fam.series))
    ws.cell(r, 14, '=IFERROR(IF(AND(ISNUMBER({sc}{r}),ISNUMBER(O{r})),{sc}{r}*O{r}/100,""),"")'.format(
        sc=L['sc'], r=r))

    m = ev.match(prows, cls, base)
    if m:
        ws.cell(r, 16, m.get('capital_gbp'))
        ws.cell(r, 17, m.get('capital_year'))
        ws.cell(r, 32, m.get('source_ref', ''))
        ws.cell(r, 33, m.get('notes', ''))
    ws.cell(r, 18, deflate_formula('{}{}'.format(L['src'], r), '{}{}'.format(L['src_yr'], r), fam.series))
    ws.cell(r, 19, '=IF(ISNUMBER({n}{r}),{n}{r}/B$2,"")'.format(n=L['src900'], r=r))
    ws.cell(r, 20, '=IF(ISNUMBER({q}{r}),{q}{r}/Params!{fac},"")'.format(q=L['src_sc'], r=r, fac=fam.cap_cell))
    ws.cell(r, 21, '=IF(ISNUMBER({s}{r}),{s}{r}-N({f}{r}),"")'.format(s=L['sug_src'], f=L['forge'], r=r))

    x = ev.extrapolation(cls, base, dat, fam.cap_num * RATE_CAPITAL, intro_year(row) or None)
    if x:
        ws.cell(r, 22, x.get('capital_gbp'))
        ws.cell(r, 23, x.get('year'))
        ws.cell(r, 24, x.get('basis', ''))
    ws.cell(r, 25, deflate_formula('{}{}'.format(L['ext'], r), '{}{}'.format(L['ext_yr'], r), fam.series))
    ws.cell(r, 26, '=IF(ISNUMBER({s}{r}),{s}{r}/B$2,"")'.format(s=L['ext900'], r=r))
    ws.cell(r, 27, '=IF(ISNUMBER({w}{r}),{w}{r}/Params!{fac},"")'.format(w=L['ext_sc'], r=r, fac=fam.cap_cell))
    ws.cell(r, 28, '=IF(ISNUMBER({z}{r}),{z}{r}-N({f}{r}),"")'.format(z=L['sug_ext'], f=L['forge'], r=r))

    ws.cell(r, 29, '=IF(AND(ISNUMBER({g}{r}),ISNUMBER({d}{r}),{d}{r}>0),{g}{r}/{d}{r},"")'.format(g=L['sc'], d=L['src_sc'], r=r))
    ws.cell(r, 30, '=IF(AND(ISNUMBER({g}{r}),ISNUMBER({d}{r}),{d}{r}>0),{g}{r}/{d}{r},"")'.format(g=L['sc'], d=L['ext_sc'], r=r))
    ws.cell(r, 31, (
        '=IF(AND(ISNUMBER(${g}{r}),ISNUMBER(${d}{r}),${d}{r}>0),'
        'IF(ABS(${g}{r}/${d}{r}-1)<={t1},"MATCH vs measured",IF(ABS(${g}{r}/${d}{r}-1)<={t2},"NEAR vs measured","FAR vs measured")),'
        'IF(AND(ISNUMBER(${g}{r}),ISNUMBER(${e}{r}),${e}{r}>0),'
        'IF(ABS(${g}{r}/${e}{r}-1)<={t1},"MATCH vs class",IF(ABS(${g}{r}/${e}{r}-1)<={t2},"NEAR vs class","FAR vs class")),'
        '"no data"))').format(g=L['sc'], d=L['src_sc'], e=L['ext_sc'], r=r, t1=TOL_MATCH, t2=TOL_NEAR))

    # A measured price makes the class-derived group the fallback: grey it out.
    if m and isinstance(m.get('capital_gbp'), (int, float)):
        grey_group(ws, r, list(range(22, 29)) + [30])

    if cls == 'engine-settings':
        ws.cell(r, 33, ((ws.cell(r, 33).value or '') + ' | unit: ' + fam.unit).strip(' |'))

def fill_maint_row(ws, r, row, prows, ev, en):
    L = MAINT_L
    eng, base = item_names(row, en)
    fam = families(row)
    cls = pick(row, 'class', 'folder')
    ws.cell(r, 1, eng or base)
    ws.cell(r, 2, base)
    ws.cell(r, 3, pick(row, 'file', 'filename', 'path'))
    ws.cell(r, 4, pick(row, 'obj_type', 'obj', 'type'))
    ws.cell(r, 5, intro_year(row))
    for j, v in enumerate(ev.status(cls, base), start=6):
        ws.cell(r, j, v)

    dm = num(pick(row, 'maintenance', 'maintenance_coins'))
    if dm is None:
        dm = num(pick(row, 'fixed_cost', 'fixed_maintenance'))
    if pick(row, 'obj_type', 'obj', 'type') in ('engine-setting',):
        dm = num(pick(row, 'value')) if pick(row, 'name').startswith('maintenance_') else None
    ws.cell(r, 10, dm if dm is not None else '')
    ws.cell(r, 11, '=IF(ISNUMBER({d}{r}),{d}{r}*Params!{fac},"")'.format(d=L['dat'], r=r, fac=fam.m_cell))
    dk = num(pick(row, 'runningcost'))
    ws.cell(r, 12, dk if dk is not None else '')
    ws.cell(r, 13, '=IF(ISNUMBER({d}{r}),{d}{r}*Params!{fac},"")'.format(
        d=L['km_dat'], r=r, fac=fam.km_cell or fam.m_cell))

    ser = 'general' if pick(row, 'obj_type') == 'vehicle' else fam.series
    ws.cell(r, 43, intro_month(row))
    ws.cell(r, 16, '=' + index_at_intro_formula('E%d' % r, 'AQ%d' % r, ser))
    ws.cell(r, 14, '=IFERROR(IF(AND(ISNUMBER({sc}{r}),ISNUMBER(P{r})),{sc}{r}*P{r}/100,""),"")'.format(
        sc=L['sc'], r=r))
    ws.cell(r, 15, '=IFERROR(IF(AND(ISNUMBER({km}{r}),ISNUMBER(P{r})),{km}{r}*P{r}/100,""),"")'.format(
        km=L['km_sc'], r=r))

    # measured_infra.maintenance() now returns way upkeep per kilometre-year, matching the
    # workbook column, so a way needs no correction. The bridge branch still returns per
    # tile-year, so bridge rows keep the x8 correction until their own unit pass.
    obj_type = pick(row, 'obj_type', 'obj', 'type')
    way_scale = 8.0 if obj_type == 'bridge' else 1.0
    m = ev.match(prows, cls, base)
    if m:
        ws.cell(r, 17, (m.get('maint_gbp_yr') * way_scale
                        if isinstance(m.get('maint_gbp_yr'), (int, float))
                        else m.get('maint_gbp_yr')))
        ws.cell(r, 18, m.get('maint_year'))
        ws.cell(r, 22, m.get('perkm_gbp'))
        ws.cell(r, 23, m.get('perkm_year'))
        ws.cell(r, 41, m.get('source_ref', ''))
        ws.cell(r, 42, m.get('notes', ''))
    ws.cell(r, 19, deflate_formula('{}{}'.format(L['src_f'], r), '{}{}'.format(L['src_f_yr'], r), ser))
    ws.cell(r, 20, '=IF(ISNUMBER({v}{r}),{v}{r}/Params!$B$5/B$2,"")'.format(v=L['src_f900'], r=r))
    ws.cell(r, 21, '=IF(ISNUMBER({t}{r}),{t}{r}/Params!{fac},"")'.format(t=L['src_f_sc'], r=r, fac=fam.m_cell))
    ws.cell(r, 24, deflate_formula('{}{}'.format(L['src_k'], r), '{}{}'.format(L['src_k_yr'], r), ser))
    ws.cell(r, 25, '=IF(ISNUMBER({v}{r}),{v}{r}/B$3,"")'.format(v=L['src_k900'], r=r))
    ws.cell(r, 26, '=IF(ISNUMBER({y}{r}),{y}{r}/Params!{fac},"")'.format(y=L['src_k_sc'], r=r, fac=fam.km_cell or fam.m_cell))

    x = ev.extrapolation(cls, base, None, fam.m_num * RATE_CAPITAL, intro_year(row) or None)
    if x:
        ws.cell(r, 27, (x.get('maint_gbp_yr') * way_scale
                        if isinstance(x.get('maint_gbp_yr'), (int, float))
                        else x.get('maint_gbp_yr')))
        ws.cell(r, 28, x.get('maint_year'))
        ws.cell(r, 29, x.get('perkm_gbp'))
        ws.cell(r, 30, x.get('perkm_year'))
        ws.cell(r, 31, x.get('basis', ''))
    ws.cell(r, 32, '=IF(ISNUMBER({v}{r}),{v}{r}/Params!$B$5/B$2,"")'.format(v=L['ext_f'], r=r))
    ws.cell(r, 33, '=IF(ISNUMBER({v}{r}),{v}{r}/B$3,"")'.format(v=L['ext_k'], r=r))
    ws.cell(r, 34, '=IF(ISNUMBER({t}{r}),{t}{r}/Params!{fac},"")'.format(t=L['ext_f_sc'], r=r, fac=fam.m_cell))
    ws.cell(r, 35, '=IF(ISNUMBER({y}{r}),{y}{r}/Params!{fac},"")'.format(y=L['ext_k_sc'], r=r, fac=fam.km_cell or fam.m_cell))

    ws.cell(r, 36, '=IF(AND(ISNUMBER({g}{r}),ISNUMBER({d}{r}),{d}{r}>0),{g}{r}/{d}{r},"")'.format(g=L['sc'], d=L['src_f_sc'], r=r))
    ws.cell(r, 37, '=IF(AND(ISNUMBER({g}{r}),ISNUMBER({d}{r}),{d}{r}>0),{g}{r}/{d}{r},"")'.format(g=L['km_sc'], d=L['src_k_sc'], r=r))
    ws.cell(r, 38, '=IF(AND(ISNUMBER({g}{r}),ISNUMBER({d}{r}),{d}{r}>0),{g}{r}/{d}{r},"")'.format(g=L['sc'], d=L['ext_f_sc'], r=r))
    ws.cell(r, 39, '=IF(AND(ISNUMBER({g}{r}),ISNUMBER({d}{r}),{d}{r}>0),{g}{r}/{d}{r},"")'.format(g=L['km_sc'], d=L['ext_k_sc'], r=r))
    ws.cell(r, 40, (
        '=IF(AND(ISNUMBER(${g}{r}),ISNUMBER(${d}{r}),${d}{r}>0),'
        'IF(ABS(${g}{r}/${d}{r}-1)<={t1},"MATCH measured fixed",IF(ABS(${g}{r}/${d}{r}-1)<={t2},"NEAR measured fixed","FAR measured fixed")),'
        'IF(AND(ISNUMBER(${k}{r}),ISNUMBER(${s}{r}),${s}{r}>0),'
        'IF(ABS(${k}{r}/${s}{r}-1)<={t1},"MATCH measured per-km",IF(ABS(${k}{r}/${s}{r}-1)<={t2},"NEAR measured per-km","FAR measured per-km")),'
        'IF(AND(ISNUMBER(${g}{r}),ISNUMBER(${e}{r}),${e}{r}>0),'
        'IF(ABS(${g}{r}/${e}{r}-1)<={t1},"MATCH class fixed",IF(ABS(${g}{r}/${e}{r}-1)<={t2},"NEAR class fixed","FAR class fixed")),'
        'IF(AND(ISNUMBER(${k}{r}),ISNUMBER(${n}{r}),${n}{r}>0),'
        'IF(ABS(${k}{r}/${n}{r}-1)<={t1},"MATCH class per-km",IF(ABS(${k}{r}/${n}{r}-1)<={t2},"NEAR class per-km","FAR class per-km")),'
        '"no data"))))').format(g=L['sc'], k=L['km_sc'], d=L['src_f_sc'], s=L['src_k_sc'],
                                e=L['ext_f_sc'], n=L['ext_k_sc'], r=r, t1=TOL_MATCH, t2=TOL_NEAR))

    measured = (isinstance(m, dict) and
                any(isinstance(m.get(k), (int, float)) for k in ('maint_gbp_yr', 'perkm_gbp')))
    if measured:
        grey_group(ws, r, list(range(27, 36)) + [38, 39])

    if cls == 'engine-settings':
        ws.cell(r, 42, ((ws.cell(r, 42).value or '') + ' | unit: ' + fam.unit).strip(' |'))

# ---------------------------------------------------------------- snippet thread
FORUM_DIR = os.path.join(BASE, 'New', 'ai', 'vehicle-cost')
FORUM_DOCS = ['forum-prices-part-1.md', 'forum-prices-part-2.md']

def load_forum_rows():
    """Every row of the forum thread 'A snippet of relative pricing information'."""
    rows = []
    for fn in FORUM_DOCS:
        path = os.path.join(FORUM_DIR, fn)
        if not os.path.exists(path):
            continue
        for line in open(path, encoding='utf-8', errors='replace'):
            m = re.match(r'^\|\s*(\d+)\s*\|', line)
            if not m:
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) < 8:
                continue
            rows.append(dict(no=int(cells[0]), year=cells[1], item=cells[2], price=cells[3],
                             spec=cells[4], basis=cells[5], source=cells[6],
                             page=cells[7] if len(cells) > 7 else '',
                             post=cells[8] if len(cells) > 8 else ''))
    return rows

def forum_numeric(prows):
    """Row number -> (total GBP/USD, unit, domain), combining component rows where the
    extraction split a single quoted price."""
    by = {}
    for r in prows:
        loc = r.get('kb_location', '')
        if 'forum-prices' not in loc:
            continue
        m = re.search(r'row (\d+)', loc)
        if not m:
            continue
        by.setdefault(int(m.group(1)), []).append(r)

    def val(r):
        try:
            return float(str(r.get('price', '')).replace(',', ''))
        except (TypeError, ValueError):
            return None

    out = {}
    for n, rs in by.items():
        comps = [r for r in rs if '(component)' in r.get('kb_location', '')]
        base = [r for r in rs if '(component)' not in r.get('kb_location', '')]
        anchor = base[0] if base else comps[0]
        if comps:
            csum = sum(val(r) or 0.0 for r in comps)
            b = val(base[0]) if base else None
            # 224: components sum to the quoted total; 238/253: components are extras.
            total = b if (b and abs(csum - b) / b < 0.01) else ((b or 0.0) + csum)
        elif base:
            total = val(base[0])
        else:
            continue
        out[n] = (total, anchor.get('price_unit', ''), anchor.get('domain', ''))
    return out

def norm_name(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())

def build_snippet_sheet(wb, forum, numeric, inv, name_index):
    ws = wb.create_sheet('Snippet prices (6521)')
    heads = ['No.', 'Year (as stated)', 'Item (as stated)', 'Price (as stated)', 'Specification',
             'Basis', 'Source', 'Page', 'Post', 'Domain', 'Price (numeric)', 'Currency',
             'Year', 'GBP @1900', 'SC @1900', 'Suggested .dat', 'Bound object', 'Workbook sheet', 'Row']
    for j, h in enumerate(heads, start=1):
        c = ws.cell(1, j, h); c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.cell(2, 1, 'Source: forum thread "A snippet of relative pricing information", '
                  'https://forum.simutrans.com/index.php?topic=6521.0, extracted in '
                  'New/ai/vehicle-cost/forum-prices-part-1.md and -2.md. Every row of the thread appears '
                  'here, bound or not. GBP rows are deflated to 1900 with the vehicle-purchase series and '
                  'converted at 0.396311 GBP/SC; Suggested .dat = SC / 0.00125. Non-sterling rows are left '
                  'unconverted. Rows with no absolute price (relative statements) have no numeric value.')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(heads))
    ws.cell(2, 1).alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[2].height = 48

    names = {norm_name(r.get('name')): r.get('name') for r in inv if r.get('name')}
    r = 3
    for f in forum:
        ws.cell(r, 1, f['no'])
        ws.cell(r, 2, f['year'])
        ws.cell(r, 3, f['item'])
        ws.cell(r, 4, f['price'])
        ws.cell(r, 5, f['spec'])
        ws.cell(r, 6, f['basis'])
        ws.cell(r, 7, f['source'])
        ws.cell(r, 8, f['page'])
        ws.cell(r, 9, f['post'])
        num = numeric.get(f['no'])
        if num and num[0]:
            total, unit, domain = num
            ws.cell(r, 10, domain)
            ws.cell(r, 11, total)
            ws.cell(r, 12, 'GBP' if 'gbp' in unit.lower() else ('USD' if 'usd' in unit.lower() or '$' in unit.lower() else unit))
            ym = re.search(r'(1[5-9]\d\d|20\d\d|21[0-4]\d)', f['year'])
            if ym:
                year = int(ym.group(1))
                ws.cell(r, 13, year)
                if 'gbp' in unit.lower() and 1500 <= year <= 2150:
                    idx = SERIES_DB['vehicle purchase'].get(year)
                    if idx:
                        gbp1900 = total * 100.0 / idx
                        sc = gbp1900 / RATE_CAPITAL
                        ws.cell(r, 14, round(gbp1900, 2))
                        ws.cell(r, 15, round(sc, 2))
                        ws.cell(r, 16, round(sc / FAC_SCALED, 0))
        # binding: prefer an exact name, then the closest (shortest) variant; independent of price
        nm = norm_name(f['item'])
        matches = []
        if nm:
            for key, base in names.items():
                if not key:
                    continue
                if key == nm:
                    matches.append((0, key, base))
                elif len(nm) > 8 and nm in key:
                    matches.append((len(key) - len(nm), key, base))
                elif len(key) > 8 and key in nm:
                    matches.append((len(nm) - len(key), key, base))
        if matches:
            matches.sort()
            bound = matches[0][2]
            ws.cell(r, 17, bound)
            loc = name_index.get(bound)
            if loc:
                ws.cell(r, 18, loc[0]); ws.cell(r, 19, loc[1])
        r += 1

    widths = [5, 16, 34, 26, 26, 26, 30, 6, 6, 13, 11, 8, 7, 11, 11, 12, 26, 20, 6]
    for j, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(j)].width = w
    for row in ws.iter_rows(min_row=3, max_row=r - 1, max_col=len(heads)):
        for c in row:
            c.alignment = WRAP
            c.border = BORDER
    for row in range(3, r):
        for j in (11, 14, 15):
            ws.cell(row, j).number_format = u'£#,##0.00'
        ws.cell(row, 16).number_format = '#,##0'
        for j in (1, 13, 19):
            ws.cell(row, j).number_format = '0'
    ws.freeze_panes = 'B3'
    ws.auto_filter.ref = 'A1:S%d' % (r - 1)
    return r - 3

def build_research_sheet(wb, rows, name_index):
    """Register of measured rows added by the 2026-11-22 deep-research pass."""
    ws = wb.create_sheet('Research prices (all passes)')
    heads = ['Domain', 'Kind', 'Item', 'Year', 'Price', 'Currency', 'Scope', 'Notes / specification',
             'Source reference', 'Evidence file', 'GBP @1900', 'SC @1900', 'Suggested .dat',
             'Bound object', 'Workbook sheet', 'Row']
    for j, h in enumerate(heads, start=1):
        c = ws.cell(1, j, h); c.font = HDR_FONT; c.fill = HDR_FILL
        c.alignment = Alignment(wrap_text=True, vertical='center')
    ws.cell(2, 1, 'Every measured row: the evidence register plus all research passes 1-38, '
                  'deduplicated on domain, kind, item, year and price. Only capital rows with a '
                  'stated year and a vehicle/way/building unit are converted here. Maintenance rows are left nominal because '
                  'the quoted unit (per engine-mile, per vehicle-year, per mile of way) decides the '
                  'conversion; see the reports for the unit of each row.')
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(heads))
    ws.cell(2, 1).alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[2].height = 42

    vehicle_domains = {'locomotive', 'carriage', 'wagon', 'multiple-unit', 'tram', 'road-vehicle',
                       'ship', 'boat', 'aircraft'}
    r = 3
    for row in rows:
        ws.cell(r, 1, row.get('domain', ''))
        ws.cell(r, 2, row.get('kind', ''))
        ws.cell(r, 3, row.get('name_or_item', ''))
        ym = re.search(r'(1[5-9]\d\d|20\d\d|21[0-4]\d)', row.get('year', '') or '')
        year = int(ym.group(1)) if ym else None
        ws.cell(r, 4, year if year else row.get('year', ''))
        price = num(row.get('price'))
        ws.cell(r, 5, price if price is not None else row.get('price', ''))
        unit = (row.get('price_unit') or '')
        ws.cell(r, 6, 'GBP' if 'gbp' in unit.lower() else ('USD' if 'usd' in unit.lower() else unit))
        ws.cell(r, 7, row.get('scope', ''))
        ws.cell(r, 8, row.get('notes', ''))
        ws.cell(r, 9, row.get('source_ref', ''))
        ws.cell(r, 10, os.path.basename(str(row.get('kb_location', ''))))
        dom = (row.get('domain') or '').lower()
        if (row.get('kind') == 'capital' and price and year and 'gbp' in unit.lower()
                and dom in vehicle_domains | {'station', 'depot', 'way'}):
            if dom == 'way':
                series, fac = 'infrastructure', FAC_WAY_KM
            elif dom == 'depot':
                series, fac = 'buildings', FAC_UNSCALED
            else:
                series, fac = 'vehicle purchase', FAC_SCALED
            idx = SERIES_DB[series].get(year)
            if idx:
                gbp = price * 100.0 / idx
                sc = gbp / RATE_CAPITAL
                ws.cell(r, 11, round(gbp, 2))
                ws.cell(r, 12, round(sc, 2))
                ws.cell(r, 13, round(sc / fac, 0))
        # binding
        nm = norm_name(row.get('name_or_item'))
        matches = []
        if nm:
            for base in sorted({v for v in name_index.keys() if v}):
                key = norm_name(base)
                if not key:
                    continue
                if key == nm:
                    matches.append((0, key, base))
                elif len(nm) > 8 and nm in key:
                    matches.append((len(key) - len(nm), key, base))
                elif len(key) > 8 and key in nm:
                    matches.append((len(nm) - len(key), key, base))
        if matches:
            matches.sort()
            bound = matches[0][2]
            ws.cell(r, 14, bound)
            loc = name_index.get(bound)
            if loc:
                ws.cell(r, 15, loc[0]); ws.cell(r, 16, loc[1])
        r += 1

    for j, w in enumerate([13, 9, 40, 8, 11, 8, 12, 60, 45, 22, 11, 11, 12, 26, 20, 6], start=1):
        ws.column_dimensions[get_column_letter(j)].width = w
    for row in ws.iter_rows(min_row=3, max_row=r - 1, max_col=len(heads)):
        for c in row:
            c.alignment = WRAP
            c.border = BORDER
    for row in range(3, r):
        for j in (5, 11, 12):
            ws.cell(row, j).number_format = u'£#,##0.00'
        ws.cell(row, 13).number_format = '#,##0'
        for j in (4, 16):
            ws.cell(row, j).number_format = '0'
    ws.freeze_panes = 'C3'
    ws.auto_filter.ref = 'A1:P%d' % (r - 1)
    return r - 3

def build_name_index(wb):
    idx = {}
    for sn in wb.sheetnames:
        if sn in ('README', 'Index', 'Params', 'Snippet prices (6521)'):
            continue
        ws = wb[sn]
        for r in range(7, ws.max_row + 1):
            b = ws.cell(r, 2).value
            if b and b not in idx:
                idx[b] = (sn, r)
    return idx

# ---------------------------------------------------------------- main
SERIES_DB = load_series()

def build_overhaul_sheet(wb, rows, prows, ev, en):
    """Overhaul and upgrade targets, one row per vehicle.

    The engine charges: initial_overhaul_cost, rising on a sigmoid to max_overhaul_cost across
    overhauls_before_max_cost overhauls, each due after max_distance_between_overhauls km and
    taking overhaul_month_tenths/10 months. upgrade_price prices a replacement with a newer type.
    """
    ws = wb.create_sheet('Overhauls & upgrades')
    cols = [
        ('Name (English)', 26), ('Base name', 22), ('Object key (.dat)', 30), ('Obj=', 8),
        ('Intro', 7), ('Class', 14),
        ('In-game cost\n(.dat)', 12), ('In-game\ninitial overhaul', 12),
        ('In-game\nmax overhaul', 12), ('In-game\noverhauls to max', 10),
        ('In-game\ninterval km', 11), ('In-game\ndowntime tenths', 11),
        ('Capital target\nGBP @1900', 12),
        ('Suggested first\noverhaul GBP', 13), ('Suggested max\noverhaul GBP', 13),
        ('Overhauls\nto max', 9), ('Interval\nkm', 10), ('Downtime\nmonths', 10),
        ('Suggested\nupgrade GBP', 12),
        ('Suggested .dat\ninitial', 13), ('Suggested .dat\nmax', 13),
        ('Suggested .dat\ninterval km', 12), ('Suggested .dat\nupgrade', 13),
        ('Basis', 76),
    ]
    hdr = sheet_header_block(ws, 'Overhauls & upgrades - targets', SCOPE_NOTE,
                             [('Rate (1 SC = GBP1900):', '=Params!$B$2'),
                              ('Factor (FACTOR_SCALED):', '=Params!$B$12')])
    ws.cell(5, 2, 'One-off charges. The engine books an overhaul and an upgrade as vehicle '
                  'maintenance, so they are indexed by the maintenance series at charge time, '
                  'but the field is tile-scaled like cost, which is why the .dat conversion here '
                  'uses FACTOR_SCALED and the capital rate. upgrade_price is the whole net cost of '
                  'replacing the old vehicle, because the engine deletes it with no resale credit.')
    for i, (title, width) in enumerate(cols, 1):
        c = ws.cell(hdr, i, title)
        c.font = Font(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor='1F4E79')
        c.alignment = Alignment(wrap_text=True, vertical='center')
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.row_dimensions[hdr].height = 44
    r = hdr + 1
    n = 0
    for row in rows:
        cls = pick(row, 'class', 'folder')
        eng, base = item_names(row, en)
        cap = None
        intro = intro_year(row)
        x = ev.extrapolation(cls, base, pick(row, 'cost'), 0.00396311, intro)
        if x:
            cap = x.get('capital_gbp')
        prof = ev.overhaul_profile(
            cls, base, cap, intro,
            (x or {}).get('maint_a_gbp', (x or {}).get('maint_gbp_yr')))
        if not prof:
            continue
        other = pick(row, 'other_cost_fields') or ''

        def fld(name):
            m = re.search(r'%s=(\d+)' % name, other)
            return int(m.group(1)) if m else None

        ws.cell(r, 1, eng or base)
        ws.cell(r, 2, base)
        ws.cell(r, 3, pick(row, 'file'))
        ws.cell(r, 4, pick(row, 'obj_type', 'obj', 'type'))
        ws.cell(r, 5, intro)
        ws.cell(r, 6, cls)
        ws.cell(r, 7, num(pick(row, 'cost')))
        ws.cell(r, 8, fld('initial_overhaul_cost'))
        ws.cell(r, 9, fld('max_overhaul_cost'))
        ws.cell(r, 10, fld('overhauls_before_max_cost'))
        ws.cell(r, 11, fld('max_distance_between_overhauls'))
        ws.cell(r, 12, fld('overhaul_month_tenths'))
        ws.cell(r, 13, cap)
        ws.cell(r, 14, prof['initial_gbp'])
        ws.cell(r, 15, prof['max_gbp'])
        ws.cell(r, 16, prof['overhauls'])
        ws.cell(r, 17, prof['interval_km'] or None)
        ws.cell(r, 18, prof['months'])
        ws.cell(r, 19, prof['upgrade_gbp'])
        for c, src in ((20, 14), (21, 15)):
            ws.cell(r, c, '=IF(AND(ISNUMBER({s}{r}),ISNUMBER(Params!$B$2),ISNUMBER(Params!$B$12)),'
                          '{s}{r}/Params!$B$12/Params!$B$2,"")'.format(s=get_column_letter(src), r=r))
        ws.cell(r, 22, prof['interval_km'] or None)
        ws.cell(r, 23, '=IF(AND(ISNUMBER({s}{r}),ISNUMBER(Params!$B$2),ISNUMBER(Params!$B$12)),'
                       '{s}{r}/Params!$B$12/Params!$B$2,"")'.format(s='S', r=r))
        ws.cell(r, 24, prof['basis'])
        r += 1
        n += 1
    if n:
        style_data_area(ws, len(cols), hdr + 1, r - 1,
                        dict(dat_cols=(7, 8, 9, 10, 11, 12, 22), gbp_cols=(13, 14, 15, 19),
                             sc_cols=(), ratio_cols=(), year_cols=(5,), num_cols=(16, 18)))
    ws.freeze_panes = 'B%d' % (hdr + 1)
    return n


def main():
    import evidence_data as ev
    inv = load_inventory()
    prows = load_price_rows()
    en = load_english_names()
    print('inventory rows: %d | measured price rows: %d | series: %d | en.tab names: %d'
          % (len(inv), len(prows), len(SERIES_DB), len(en)))

    cap_wb = Workbook(); cap_wb.remove(cap_wb.active)
    main_wb = Workbook(); main_wb.remove(main_wb.active)
    write_index_sheet(cap_wb); write_params_sheet(cap_wb)
    write_index_sheet(main_wb); write_params_sheet(main_wb)
    write_readme(cap_wb, 'Cost balancing - capital costs (1900 basis)', ev.readme_extra())
    write_readme(main_wb, 'Cost balancing - maintenance costs (fixed and per-km)', ev.readme_extra_maint())

    for sheet_name, matcher in ev.tabs():
        rows = [r for r in inv if matcher(r)]
        build_cap_sheet(cap_wb, sheet_name, rows, prows, ev, en)
        build_maint_sheet(main_wb, sheet_name, rows, prows, ev, en)
        print('  %-28s %4d items' % (sheet_name, len(rows)))

    forum = load_forum_rows()
    numeric = forum_numeric(prows)
    name_index = build_name_index(cap_wb)
    n = build_snippet_sheet(cap_wb, forum, numeric, inv, name_index)
    print('  %-28s %4d rows (forum thread 6521)' % ('Snippet prices (6521)', n))
    research = load_price_rows(full=True)
    if research:
        m = build_research_sheet(cap_wb, research, name_index)
        print('  %-28s %4d rows (all research passes)' % ('Research prices', m))

    veh = [r for r in inv if pick(r, 'obj_type', 'obj', 'type') == 'vehicle']
    m = build_overhaul_sheet(cap_wb, veh, prows, ev, en)
    print('  %-28s %4d rows' % ('Overhauls & upgrades', m))

    cap_wb.save(OUT_CAP)
    main_wb.save(OUT_MAINT)
    print('written:', OUT_CAP)
    print('written:', OUT_MAINT)

if __name__ == '__main__':
    main()
