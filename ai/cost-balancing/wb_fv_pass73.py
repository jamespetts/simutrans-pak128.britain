# -*- coding: utf-8 -*-
# wb_fv_pass73.py - apply the 2026-11-27 road and air research to the workbooks.
#
# WHAT THIS PASS DOES
# 1. ROAD FORGE: 315,000 -> 20,000 raw = GBP79.26/km. It is the bed of an unsurfaced track of
#    bridleway width: 79 per cent of the bridleway's GBP100/km whole construction, and 72 per cent
#    of Telford's 1825 measured bed-preparation rate for a 32 ft road. It is the only per-waytype
#    value that is both realistic and no greater than the cheapest road, so no way-only value can
#    be negative. Every higher road carries its excess formation in its way object.
# 2. AIR FORGE: 1,875,000 -> 110,000 raw = GBP435.94/km. It is 76 per cent of the grass taxiway's
#    GBP575/km whole construction, the formation share of a grass strip from the Valuation Office
#    Agency grass specification. The paved rows carry their pavement and excess formation in the
#    way object.
# 3. COBBLESTONE CAPITAL: the present GBP123/km is the 1819 turnpike network average, not a sett
#    carriageway. The measured sett band is GBP3,400-8,000/km, working band GBP5,000-7,000; the
#    midpoint GBP6,000 is entered. Without this the row's maintenance rate would be meaningless.
# 4. ROAD AND AIR ROUTINE MAINTENANCE: replace the single GBP21.57/km-year road rate and the single
#    GBP6.67 air rate with the per-object routine bands of the research (section 11.4). The rates
#    are routine only; renewal is charged separately through weg_t::renew() and wear_capacity.
#    Concrete is 0.25 per cent of its own capital and asphalt 0.50 per cent, so the rate ratio is
#    1:2; the absolute concrete/asphalt difference follows the capital ratio. The present .dat
#    maintenance percentages include renewal and are 7.6-24 times the routine-only rate.
# 5. The two paved-runway measured binds (GBP69 per square metre bound as GBP per kilometre) are
#    rejected, as the water binds were in pass 72.
#
# Run: py -3 wb_fv_pass73.py [--write]. Dry run by default. Idempotent by the pass 73 marker.
import os
import re
import shutil
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pass 73'
WRITE = '--write' in sys.argv
PER_KM = 252.32708655576          # raw units per GBP1900 per km
WAY_MONTH = 0.09511464            # GBP1900 per km-year per raw maintenance unit

ROAD_FORGE = 20000
AIR_FORGE = 110000
COBBLE_TOTAL = 6000.0             # midpoint of the measured sett band GBP5,000-7,000/km

# object base name -> (routine maintenance GBP1900/km-year, rate description, basis)
ROAD_MAINT = {
    'bridleway': (3.0, '3.0 per cent of capital', 'track bed: grading and grips; no surface renewal'),
    'old_dirt_road': (3.0, '3.0 per cent of capital', 'track bed: grading and grips; no surface renewal'),
    'dirt_road': (3.0, '3.0 per cent of capital', 'track bed: grading and grips; no surface renewal'),
    'cobblestone_road': (120.0, '2.0 per cent of the corrected GBP6,000/km sett capital',
                         'Victorian urban band, low end; setts and concrete bed'),
    'macadam_road': (10.0, '1.2 per cent of capital', '1880 main-road rate less re-stoning'),
    'tarmac_road': (49.0, '4.6 per cent of capital', '1911 tarred-slag upkeep; annual re-tarring'),
    'tarmac_city_road': (60.0, '3.2 per cent of capital', '1911 tarred-slag upkeep, urban loading'),
    'hr-asphalt-road-heavy': (79.0, '0.50 per cent of capital', 'flexible: patching, crack sealing, surface preservation'),
    'hr-asphalt-road-light': (79.0, '0.50 per cent of capital', 'flexible: patching, crack sealing, surface preservation'),
    'hr-asphalt-road-medium': (79.0, '0.50 per cent of capital', 'flexible: patching, crack sealing, surface preservation'),
    'sma-road-heavy': (79.0, '0.50 per cent of capital', 'flexible: patching, crack sealing, surface preservation'),
    'sma-road-light': (79.0, '0.50 per cent of capital', 'flexible: patching, crack sealing, surface preservation'),
    'sma-road-medium': (79.0, '0.50 per cent of capital', 'flexible: patching, crack sealing, surface preservation'),
    'concrete_road': (59.0, '0.25 per cent of capital', 'rigid: joint resealing and slab repair; renewal is wear-driven'),
    'city_road': (132.0, '0.50 per cent of capital', 'flexible, urban intensity'),
    'city_road-sma': (132.0, '0.50 per cent of capital', 'flexible, urban intensity'),
    'motorway': (132.0, '0.50 per cent of capital', 'bottom of the 1982 young-motorway band GBP125-310'),
    'motorway-sma': (132.0, '0.50 per cent of capital', 'bottom of the 1982 young-motorway band GBP125-310'),
}
AIR_MAINT = {
    'GrassRunway': (10.0, '1.3 per cent of capital', 'mowing and rolling; no overlay'),
    'GrassTaxiway': (7.0, '1.2 per cent of capital', 'mowing and rolling; no overlay'),
    'runway': (114.0, '0.50 per cent of capital', 'flexible airfield: patching, crack sealing, surface preservation'),
    'tarmac-runway': (114.0, '0.50 per cent of capital', 'flexible airfield: patching, crack sealing, surface preservation'),
    'taxiway': (86.0, '0.50 per cent of capital', 'flexible airfield: patching, crack sealing, surface preservation'),
    'tarmac-taxiway': (86.0, '0.50 per cent of capital', 'flexible airfield: patching, crack sealing, surface preservation'),
    'concrete-runway': (246.0, '0.25 per cent of capital', 'rigid airfield: joint resealing, spall and slab repair'),
    'concrete-taxiway': (126.0, '0.25 per cent of capital', 'rigid airfield: joint resealing, spall and slab repair'),
}
PAVED_REJECT = {'concrete-runway', 'runway'}


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
BACKUP = os.path.join(BASE, 'ai', 'temp', 'pre-pass73')


def append_note(cell, text):
    old = str(cell.value or '')
    if MARK in old:
        return False
    cell.value = (old + ' | ' if old else '') + text
    return True


def capital_pass(wb, changed):
    # Road forge and way-only values.
    ws = wb['Ways - road']
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        if 'elevated' in name.lower() or 'mothballed' in name.lower():
            continue
        if MARK in str(ws.cell(r, 33).value or ''):
            continue
        # Cobblestone capital correction.
        if name == 'Cobblestone road':
            ws.cell(r, 22, COBBLE_TOTAL)
            ws.cell(r, 23, 1900)
            ws.cell(r, 24, 'sett carriageway GBP3,400-8,000/km measured, working band GBP5,000-7,000; '
                           'midpoint GBP6,000 entered; the previous GBP123/km was the 1819 turnpike '
                           'network average, not a sett rate. Road and air research 2026-11-27 section 2.2.')
            changed.append(('cobblestone capital', name, '123', COBBLE_TOTAL))
        gbp = ws.cell(r, 22).value
        year = ws.cell(r, 23).value
        if not isinstance(gbp, (int, float)) or year != 1900:
            changed.append(('road: no 1900 class total', name, gbp, year))
            continue
        total = gbp * PER_KM
        ws.cell(r, 11, ROAD_FORGE)
        ws.cell(r, 28, total - ROAD_FORGE)
        append_note(ws.cell(r, 33),
                    '%s: forge_cost_road = 20,000 raw (GBP79.26/km), the bed of an unsurfaced track '
                    'of bridleway width; the way object carries the excess formation. No negative '
                    'way-only value is possible because the forge is below the cheapest road. '
                    'Road and air research 2026-11-27 section 4.' % MARK)
        changed.append(('road forge', name, 315000, ROAD_FORGE))
    # Air forge and way-only values.
    ws = wb['Ways - air']
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        if MARK in str(ws.cell(r, 33).value or ''):
            continue
        base = str(ws.cell(r, 2).value or '')
        if base in PAVED_REJECT:
            for c in (16, 17, 18, 19, 20, 21):
                ws.cell(r, c, None)
            append_note(ws.cell(r, 33),
                        '%s: the measured GBP69 per square metre was bound as GBP per kilometre; '
                        'the bind is rejected and the class group is used. Road and air research '
                        '2026-11-27 section 6.' % MARK)
            changed.append(('air measured bind rejected', name, 'cleared', ''))
        gbp = ws.cell(r, 22).value
        year = ws.cell(r, 23).value
        if not isinstance(gbp, (int, float)) or year != 1900:
            changed.append(('air: no 1900 class total', name, gbp, year))
            continue
        total = gbp * PER_KM
        ws.cell(r, 11, AIR_FORGE)
        ws.cell(r, 28, total - AIR_FORGE)
        append_note(ws.cell(r, 33),
                    '%s: forge_cost_air = 110,000 raw (GBP435.94/km), 76 per cent of the grass '
                    'taxiway; the way object carries the pavement and the excess formation. '
                    'Road and air research 2026-11-27 section 6.' % MARK)
        changed.append(('air forge', name, 1875000, AIR_FORGE))
    # Params notes.
    ps = wb['Params']
    for r in range(1, ps.max_row + 1):
        key = ps.cell(r, 1).value
        if key == 'FORGE_ROAD' and ps.cell(r, 2).value != ROAD_FORGE:
            ps.cell(r, 2, ROAD_FORGE)
            ps.cell(r, 3, 'forge_cost_road: 20,000 raw = GBP79.26/km, the research recommendation '
                          'of 2026-11-27. The live simuconf.tab setting is still 315,000; its '
                          'change is outstanding. [USER-DIRECTION:2026-11-27]')
            changed.append(('Params FORGE_ROAD', key, 315000, ROAD_FORGE))
        elif key == 'FORGE_AIR' and ps.cell(r, 2).value != AIR_FORGE:
            ps.cell(r, 2, AIR_FORGE)
            ps.cell(r, 3, 'forge_cost_air: 110,000 raw = GBP435.94/km, the research recommendation '
                          'of 2026-11-27. The live simuconf.tab setting is still 1,875,000; its '
                          'change is outstanding. [USER-DIRECTION:2026-11-27]')
            changed.append(('Params FORGE_AIR', key, 1875000, AIR_FORGE))


def maintenance_pass(wb, changed):
    for sheet, table in (('Ways - road', ROAD_MAINT), ('Ways - air', AIR_MAINT)):
        ws = wb[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            if 'elevated' in name.lower() or 'mothballed' in name.lower():
                continue
            base = str(ws.cell(r, 2).value or '')
            rec = table.get(base)
            if not rec:
                continue
            if MARK in str(ws.cell(r, 31).value or ''):
                continue
            value, rate, why = rec
            sug = value / WAY_MONTH
            old = ws.cell(r, 27).value
            note = ('%s: routine maintenance %s = GBP%0.2f per km-year, renewal excluded. %s. '
                    'Renewal is charged separately through weg_t::renew() and wear_capacity; the '
                    'previous figure included renewal and is withdrawn. Road and air research '
                    '2026-11-27 section 11.4.'
                    % (MARK, rate, value, why))
            ws.cell(r, 27, value)
            ws.cell(r, 34, sug)
            ws.cell(r, 17, value)
            ws.cell(r, 18, 1900)
            ws.cell(r, 41, 'Road and air research 2026-11-27 section 11.4')
            append_note(ws.cell(r, 31), note)
            append_note(ws.cell(r, 42), note)
            changed.append(('maintenance', sheet, name, old, value, sug))


def main():
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    changed = []
    capital_pass(wc, changed)
    maintenance_pass(wm, changed)
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
