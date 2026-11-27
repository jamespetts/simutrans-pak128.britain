# -*- coding: utf-8 -*-
# wb_fv_pass75.py - make the pass 74 research visible and checkable in the spreadsheets.
#
# WHY THIS PASS EXISTS
# Pass 74 filled four gap classes but left three of them visible only as notes or formulas:
#   1. The tram maintenance "band" was described in a note but had no numeric cells, which made it
#      read as if a measured band had existed before. It did not. This pass adds the band as two
#      numeric columns and a derivation block that shows every step: measured combined charge,
#      annualised renewal, routine component, and the 25-40 year sensitivity.
#   2. The depot targets were in the class-price column and the constraint (a depot can only cost
#      cost_depot_<waytype> x level) was in prose. This pass adds the measured cost per unit, the
#      target, the charge the game actually makes today, the ratio, and the constraint itself as a
#      column, so the engine-or-level decision can be taken from the sheet.
#   3. The station extensions showed a class price but not what it was derived from. This pass adds
#      the inferred floor area, the rate per square metre, the derived capital, the current .dat
#      capital and the ratio. It also states, in the sheet, that there is no measured goods-shed
#      price: the derivation is an ESTIMATE against a measured building-rate ladder.
#
# Run: py -3 wb_fv_pass75.py [--write]. Dry run by default. Idempotent by the pass 75 marker.
import os
import shutil
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pass 75'
WRITE = '--write' in sys.argv

CAP_UNIT = 0.00396311
BLD_UNIT = 0.00049539
WAY_MONTH_YEAR = 0.09511464
TRAM_FORGE_GBP = 89000 * CAP_UNIT
TRAM_RATE = 0.04568
MAGLEV_RATE = 0.012

TRAM_CAPITAL = {
    'TramTrack': 2486.0, 'TramTrack-55lb': 2637.0, 'TramTrack-75lb': 2852.0,
    'TramTrack-85lb': 2960.0, 'TramTrack-92lb': 3036.0, 'TramTrack-98lb': 3100.0,
    'TramTrackHeavy': 2960.0, 'TramTrack-mothballed': 0.0,
}
MAGLEV_CAPITAL = {
    'Concrete_Maglev_Track': 124786.0,
    'Concrete_Maglev_Track_Elevated': 152238.0,
    'Economical_Concrete_Maglev_Track': 124786.0,
    'Economical_Concrete_Maglev_Track_Elevated': 152238.0,
    'Mothballed_Maglev_Track': 0.0,
}
DEPOT_RATE = {'rail': 750.0, 'road': 187.0, 'ship': 1304.0, 'air': 18745.0}
DEPOT_CURRENT = {'rail': 2000.0, 'road': 1000.0, 'ship': 4000.0, 'air': 7500.0}
DEPOT = {
    'OldTrainDepot': ('rail', 3000.0), 'AirHangarModern': ('air', 25440.0),
    'AirHangarOld': ('air', 13812.0), 'CoachStable': ('road', 5600.0),
    'MaglevDepot': ('rail', 4382.0), 'ModernBoatyard': ('ship', 1304.0),
    'ModernRoadDepot': ('road', 5600.0), 'ModernRoadDepotElectric': ('road', 5600.0),
    'ModernRoadDepotMixed': ('road', 5600.0), 'ModernTrainDepot': ('rail', 4382.0),
    'ModernTrainDepotElectric': ('rail', 4382.0), 'ModernTrainDepotNarrow': ('rail', 4382.0),
    'ModernTramDepot': ('rail', 9560.0), 'OldBoatyard': ('ship', 1304.0),
    'OldBoatyardSteam': ('ship', 1304.0), 'OldRoadDepot': ('road', 5600.0),
    'OldRoadDepot2': ('road', 5600.0), 'OldRoadDepotElectric': ('road', 5600.0),
    'OldRoadDepotSteam': ('road', 3000.0), 'OldTrainDepotDiesel': ('rail', 4382.0),
    'OldTrainDepotElectric': ('rail', 4382.0), 'OldTrainDepotHorse': ('rail', 2083.0),
    'OldTrainDepotNarrow': ('rail', 3000.0), 'OldTrainDepotNarrowHorse': ('rail', 2083.0),
    'OldTramDepot': ('rail', 9560.0), 'OldTramDepotHorse': ('rail', 9560.0),
    'OldTramDepotSteam': ('rail', 9560.0),
}
# base -> (floor area m2 or None, rate GBP/m2 or None, capital GBP, description, maintenance share)
EXTENSION = {
    'GoodsWarehouseOld': (250, 2.50, 625.0, 'brick or timber goods shed, 11 m by 23 m', 0.050),
    'GoodsWarehouseModern': (400, 3.25, 1300.0, 'steel-framed goods shed, 11 m by 36 m', 0.020),
    'BulkGoodsBunker': (100, 5.00, 500.0, 'brick bulk goods bunker, 8 m by 12 m', 0.015),
    'CarYard': (1000, 0.50, 500.0, 'surfaced car yard, 25 m by 40 m', 0.020),
    'LivestockPen': (150, 1.50, 225.0, 'open timber livestock pen, 11 m by 14 m', 0.050),
    'OldPostOffice': (200, 4.00, 800.0, 'brick sorting office, 12 m by 17 m', 0.015),
    'ModernPostOffice': (400, 4.50, 1800.0, 'concrete or steel sorting office, 15 m by 27 m', 0.020),
    'FluidStorageStation': (None, None, 750.0, 'tank farm: three tanks at GBP150 plus GBP300 of bund and pipework', 0.020),
}


def find_base():
    d = HERE
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-capital.xlsx')):
            return d
        p = os.path.dirname(d)
        if p == d:
            raise SystemExit('workspace root not found')
        d = p


BASE = find_base()
CAP = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')
MAINT = os.path.join(BASE, 'New', 'cost-balancing-maintenance.xlsx')
BACKUP = os.path.join(BASE, 'ai', 'temp', 'pre-pass75')


def read_levels():
    import glob
    import re
    out = {}
    for path in glob.glob(os.path.join(BASE, 'New', 'depots', '*.dat')):
        text = open(path, encoding='utf-8', errors='replace').read()
        for block in re.split(r'(?im)^\s*obj\s*=', text)[1:]:
            name = None
            level = None
            for line in block.splitlines():
                m = re.match(r'\s*name\s*=\s*(\S+)', line, re.I)
                if m:
                    name = m.group(1).strip()
                m = re.match(r'\s*level\s*=\s*(\d+)', line, re.I)
                if m:
                    level = int(m.group(1))
            if name and level is not None:
                out[name] = level
    return out


def tram_cells(cap):
    combined = TRAM_RATE * cap
    renewal = (cap - TRAM_FORGE_GBP) / 30.0
    routine = combined - renewal
    low = (TRAM_RATE * cap - (cap - TRAM_FORGE_GBP) / 25.0) / WAY_MONTH_YEAR
    high = (TRAM_RATE * cap - (cap - TRAM_FORGE_GBP) / 40.0) / WAY_MONTH_YEAR
    return combined, renewal, routine, low, high


def maglev_cells(cap):
    return (0.0075 * cap / WAY_MONTH_YEAR, 0.02 * cap / WAY_MONTH_YEAR)


def capital_depots(wb, changed):
    ws = wb['Depots']
    levels = read_levels()
    if MARK not in str(ws.cell(6, 37).value or ''):
        for c, text in ((37, 'Level now (from the .dat)'),
                        (38, 'Measured cost per unit (GBP)'),
                        (39, 'Target capital (GBP)'),
                        (40, 'Charge the game makes today (GBP)'),
                        (41, 'Target / current'),
                        (42, 'Constraint')):
            ws.cell(6, c, '%s %s' % (text, MARK))
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in DEPOT:
            continue
        fam, target = DEPOT[base]
        rate = DEPOT_RATE[fam]
        setting = DEPOT_CURRENT[fam]
        level = levels.get(base, 1)
        current = setting * level * CAP_UNIT
        ws.cell(r, 37, level)
        ws.cell(r, 38, rate)
        ws.cell(r, 39, target)
        ws.cell(r, 40, round(current, 2))
        ws.cell(r, 41, round(target / current, 2) if current else None)
        ws.cell(r, 42, 'cost_depot_%s x level only' % fam)
        changed.append(('depot data', base, round(current, 2), target))
    row = 44
    notes = [
        'HOW A DEPOT IS PRICED, AND WHY THIS SHEET HAS NO PER-OBJECT .dat COST (pass 75, '
        '2026-11-27)',
        'The engine charges a depot cost_depot_<waytype> x level and never reads the building .dat '
        'cost field. cost_depot_rail covers track, narrow gauge, tram, monorail and maglev; the '
        'other three settings cover road, water and air.',
        'There are therefore only two ways to make a depot cost what it should: (a) change the '
        'engine so a depot with an explicit cost field is charged that cost; or (b) set level to '
        'encode the whole cost, using one setting per waytype. Column AI gives the level each '
        'object needs under option (b); column AJ gives the setting each object would need if its '
        'present level were kept.',
        'Columns AK to AP state the level in force, the measured cost per unit, the measured '
        'target, the charge the game makes today, the ratio and the constraint, so the size of the '
        'error can be seen without leaving the sheet.',
    ]
    for i, text in enumerate(notes):
        ws.cell(row + i, 1, text)


def capital_extensions(wb, changed):
    ws = wb['Stations & bus stops']
    if MARK not in str(ws.cell(6, 35).value or ''):
        for c, text in ((35, 'Inferred floor area (m2)'),
                        (36, 'Rate (GBP1900/m2)'),
                        (37, 'Derived capital (GBP)'),
                        (38, 'Current .dat capital (GBP)'),
                        (39, 'Derived / current'),
                        (40, 'Evidence class')):
            ws.cell(6, c, '%s %s' % (text, MARK))
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in EXTENSION:
            continue
        area, rate, cap, desc, share = EXTENSION[base]
        current_raw = ws.cell(r, 10).value
        current = current_raw * BLD_UNIT if isinstance(current_raw, (int, float)) else None
        ws.cell(r, 35, area)
        ws.cell(r, 36, rate)
        ws.cell(r, 37, cap)
        ws.cell(r, 38, round(current, 2) if current else None)
        ws.cell(r, 39, round(cap / current, 2) if current else None)
        ws.cell(r, 40,
                'ESTIMATE: no measured goods-shed price. Area from the function; rate from the '
                'measured building ladder. Not a measurement of this object.')
        changed.append(('extension data', base, round(current, 2) if current else None, cap))


def maintenance_tram(wb, changed):
    ws = wb['Ways - tram']
    if MARK not in str(ws.cell(6, 44).value or ''):
        ws.cell(6, 44, 'Band low, 25-year renewal life (raw) %s' % MARK)
        ws.cell(6, 45, 'Band high, 40-year renewal life (raw) %s' % MARK)
    current_raw = {}
    for r in range(7, 15):
        base = str(ws.cell(r, 2).value or '')
        if base:
            current_raw[base] = ws.cell(r, 10).value
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in TRAM_CAPITAL:
            continue
        cap = TRAM_CAPITAL[base]
        if cap == 0:
            ws.cell(r, 44, 0)
            ws.cell(r, 45, 0)
            continue
        combined, renewal, routine, low, high = tram_cells(cap)
        ws.cell(r, 44, round(low))
        ws.cell(r, 45, round(high))
        changed.append(('tram band', base, round(low), round(high)))
    # Derivation block below the table, at a fixed row so a re-run is idempotent.
    start = 17
    title = 'TRAM WAY MAINTENANCE DERIVATION (pass 75, 2026-11-27): what is measured and what is assumed'
    ws.cell(start, 1, title)
    headers = ['Object', 'Class capital GBP1900/km', 'Measured combined charge at 4.568%',
               'Annualised renewal, 30-year life', 'Routine component (entered)',
               'Raw entered', 'Band low raw (25-year life)', 'Band high raw (40-year life)',
               'Current .dat maintenance (raw)']
    for c, text in enumerate(headers, start=1):
        ws.cell(start + 1, c, text)
    r = start + 2
    for base, cap in TRAM_CAPITAL.items():
        if cap == 0:
            continue
        combined, renewal, routine, low, high = tram_cells(cap)
        ws.cell(r, 1, base)
        ws.cell(r, 2, cap)
        ws.cell(r, 3, round(combined, 2))
        ws.cell(r, 4, round(renewal, 2))
        ws.cell(r, 5, round(routine, 2))
        ws.cell(r, 6, round(routine / WAY_MONTH_YEAR))
        ws.cell(r, 7, round(low))
        ws.cell(r, 8, round(high))
        ws.cell(r, 9, current_raw.get(base))
        r += 1
    notes = [
        'WHAT IS MEASURED. The 1930-31 Ministry of Transport tramway return gives permanent-way '
        'maintenance and renewals of GBP1,635,654 against permanent-way capital of '
        'GBP35,807,350, which is 4.568 per cent a year, and 1.024d per car-mile against '
        '383,378,799 car-miles. That is the only measured quantity in this block.',
        'WHAT IS ASSUMED. The return is gross of renewals, and the engine charges renewal '
        'separately through weg_t::renew(), so a renewal life is needed to split the measured '
        'charge. 30 years is the central assumption; the two band columns show the result at '
        '25 and 40 years. The band is therefore a SENSITIVITY RANGE ON AN ASSUMPTION, not a '
        'measured band. It did not exist in the workbook before pass 74 added it.',
        'WHAT IS NOT INCLUDED. The measured charge is per route-kilometre of double track; the '
        'table is per track-kilometre. The capital is the historic capital account, not '
        'revalued, which is why the car-mile conversion is 15 per cent lower than the capital '
        'conversion. Both are stated in research-pricing-report-59.md section 2.',
    ]
    r += 1
    for text in notes:
        ws.cell(r, 1, text)
        r += 1


def maintenance_maglev(wb, changed):
    ws = wb['Ways - maglev']
    if MARK not in str(ws.cell(6, 44).value or ''):
        ws.cell(6, 44, 'Band low, 0.75 per cent (raw) %s' % MARK)
        ws.cell(6, 45, 'Band high, 2.0 per cent (raw) %s' % MARK)
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in MAGLEV_CAPITAL:
            continue
        low, high = maglev_cells(MAGLEV_CAPITAL[base])
        ws.cell(r, 44, round(low))
        ws.cell(r, 45, round(high))
        changed.append(('maglev band', base, round(low), round(high)))


def main():
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    changed = []
    capital_depots(wc, changed)
    capital_extensions(wc, changed)
    maintenance_tram(wm, changed)
    maintenance_maglev(wm, changed)
    for item in changed:
        print(' | '.join(str(x) for x in item))
    print('\n%d changes' % len(changed))
    if not WRITE:
        print('dry run: pass --write to save')
        return
    os.makedirs(BACKUP, exist_ok=True)
    for src, dst in ((CAP, os.path.join(BACKUP, 'cost-balancing-capital.xlsx')),
                     (MAINT, os.path.join(BACKUP, 'cost-balancing-maintenance.xlsx'))):
        if not os.path.exists(dst):
            shutil.copy2(src, dst)
    wc.save(CAP)
    wm.save(MAINT)
    print('written; backups in', BACKUP)


if __name__ == '__main__':
    main()
