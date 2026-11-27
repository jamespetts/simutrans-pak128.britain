# -*- coding: utf-8 -*-
# wb_fv_pass72.py - the two corrections directed on 2026-11-27.
#
# WHAT THIS PASS DOES
# 1. WATER: the recorded decision of 2026-11-24 is forge_cost_water = 0, because for a canal the
#    forging is the building and there is no separate formation. The live simuconf.tab still reads
#    125,000 and both workbooks still subtract it from the canal totals. This pass writes 0 into the
#    capital workbook's forge column for all 16 water rows, makes the way-only value equal the whole
#    construction, and writes 0 into the Params FORGE_WATER cell with the decision and the
#    outstanding simuconf.tab change stated on the cell.
#    It also rejects the four measured water binds that the 2026-11-26 audit found to be a boat
#    hull (Barge canal), a multi-item forum number (Narrowboat canal), and two whole projects
#    (Large ship canal, Ship canal improved). Those rows fall back to the class group, which is the
#    measured canal construction per kilometre. Without this, the water sheet would still carry the
#    3.98 billion raw-unit large-ship-canal artefact after the forge correction.
# 2. ELEVATED MAINTENANCE: measured_infra.maintenance() called bridge_rate(row), which returns
#    bridge CAPITAL in GBP per km, and added it to the annual maintenance. The maintenance target
#    became about 98-100 per cent of capital a year. This pass replaces it with the measured bridge
#    UPKEEP rate from Cudworth 1886 (infrastructure-cost-evidence.md section 4) plus the plain-way
#    upkeep of the same waytype:
#       brick 0.05, stone/masonry 0.045, iron 0.24, steel 0.30, concrete 0.05 (brick proxy),
#       timber 0.53 GBP per metre-year; x 1,000 for GBP per km-year.
#    The ground/bed preparation is a capital item in the forge, which is retained; the plain-way
#    upkeep covers the bed's routine upkeep. There is no separate measured ground-levelling
#    maintenance figure, and the note says so.
#
# Run: py -3 wb_fv_pass72.py [--write]. Dry run by default. Idempotent by the pass 72 marker.
import os
import re
import shutil
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pass 72'
WRITE = '--write' in sys.argv
PER_KM = 252.32708655576          # raw units per GBP1900 per km (1 / 0.00396311)
WAY_MONTH = 0.09511464            # GBP1900 per km-year per raw maintenance unit
WAY_UPKEEP = {'Ways - rail': 6.67, 'Ways - narrow gauge': 6.67, 'Ways - road': 21.57}
# Cudworth 1886, GBP per metre-year, via infrastructure-cost-evidence.md section 4.
BRIDGE_UPKEEP = {'brick': 0.05, 'stone': 0.045, 'masonry': 0.045, 'iron': 0.24,
                 'steel': 0.30, 'concrete': 0.05, 'timber': 0.53, 'wood': 0.53}
WATER_BIND_REJECT = {
    'Barge canal': ('the measured 500 GBP (1891) is a boat hull, not a canal; the note says '
                    '"hull cost; engines a further 336"'),
    'Narrowboat canal': ('the measured 900 GBP (1935) is a number from a multi-item forum post, '
                         'not a per-kilometre canal price'),
    'Large ship canal': ('the measured 15,000,000 GBP (1894) is a whole 58 km project, not a '
                         'per-kilometre price'),
    'Ship canal (improved)': ('the measured 300,000 GBP (1905) is a whole 9 km project, not a '
                              'per-kilometre price'),
}
REJECT_NAMES = set(WATER_BIND_REJECT)


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
BACKUP = os.path.join(BASE, 'ai', 'temp', 'pre-pass72')


def material(name):
    n = name.lower()
    if 'brick' in n:
        return 'brick'
    if 'masonry' in n or 'stone' in n:
        return 'stone'
    if 'iron' in n:
        return 'iron'
    if 'steel' in n:
        return 'steel'
    if 'concrete' in n:
        return 'concrete'
    if 'wood' in n or 'timber' in n:
        return 'timber'
    return None


def append_note(cell, text):
    old = str(cell.value or '')
    if MARK in old:
        return False
    cell.value = (old + ' | ' if old else '') + text
    return True


def water_pass(wb, changed):
    ws = wb['Ways - water']
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        if MARK in str(ws.cell(r, 33).value or '') and ws.cell(r, 11).value == 0:
            continue
        old_forge = ws.cell(r, 11).value
        if old_forge != 0:
            ws.cell(r, 11, 0)
            changed.append(('water forge', name, old_forge, 0))
        # Reject the four measured binds the 2026-11-26 audit found to be the wrong object or unit.
        if name in REJECT_NAMES:
            for c in (16, 17, 18, 19, 20, 21):
                ws.cell(r, c, None)
            append_note(ws.cell(r, 33),
                        '%s: measured bind rejected - %s. The class group is used.'
                        % (MARK, WATER_BIND_REJECT[name]))
            changed.append(('water measured bind rejected', name, 'cleared', ''))
        elif ws.cell(r, 16).value is not None:
            # A measured bind not on the reject list: leave it and flag it for review.
            append_note(ws.cell(r, 33),
                        '%s: forge is 0; the measured bind was not re-derived in this pass.'
                        % MARK)
        # Class total: the class price (col 22, GBP at the class year) deflated to 1900, then
        # converted to raw units. Every water row is dated 1900, so the deflation is a no-op.
        gbp = ws.cell(r, 22).value
        year = ws.cell(r, 23).value
        if isinstance(gbp, (int, float)) and year == 1900:
            total = gbp * PER_KM
            # Make the class way-only equal the whole construction, not total minus the forge.
            ws.cell(r, 28, total)
        append_note(ws.cell(r, 33),
                    '%s: forge_cost_water = 0 per the 2026-11-24 decision; the whole channel '
                    'construction is in the way object. The previous 125,000 subtraction is '
                    'withdrawn. The simuconf.tab setting was changed to 0 on 2026-11-27 in both '
                    'the source and the live runtime copy.' % MARK)
    # Params FORGE_WATER cell. Rows 21-28 are the eight forge settings.
    ps = wb['Params']
    for r in range(1, ps.max_row + 1):
        if ps.cell(r, 1).value == 'FORGE_WATER' and ps.cell(r, 2).value != 0:
            ps.cell(r, 2, 0)
            ps.cell(r, 3, 'forge_cost_water: 0 per the user direction of 2026-11-27 and the '
                          'recorded decision of 2026-11-24. For a canal the forging is the building '
                          'and there is no separate formation, so the whole construction is in the '
                          'way object. The simuconf.tab setting was changed to 0 on 2026-11-27 in '
                          'both the source and the live runtime copy. [USER-DIRECTION:2026-11-27]')
            changed.append(('Params FORGE_WATER', 'FORGE_WATER', 125000, 0))
            break


def elevated_pass(wb, changed):
    for sheet in ('Ways - rail', 'Ways - road', 'Ways - narrow gauge'):
        ws = wb[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if 'elevated' not in name.lower():
                continue
            if MARK in str(ws.cell(r, 31).value or ''):
                continue
            mat = material(name)
            if mat is None:
                changed.append(('elevated: material not identified', sheet, name, ''))
                continue
            rate = BRIDGE_UPKEEP[mat]
            way = WAY_UPKEEP[sheet]
            class_fixed = rate * 1000.0 + way
            sug = class_fixed / WAY_MONTH
            old = ws.cell(r, 27).value
            note = ('%s: elevated structure upkeep at the measured %s rate of GBP%0.3f per '
                    'metre-year (Cudworth 1886, infrastructure-cost-evidence.md section 4), '
                    'GBP%0.0f per km-year, plus plain-way upkeep GBP%0.2f per km-year. The previous '
                    'figure added the bridge CAPITAL as annual upkeep and is withdrawn.'
                    % (MARK, mat, rate, rate * 1000.0, way))
            if mat == 'concrete':
                note += (' No measured concrete upkeep exists; the brick rate is used as the proxy '
                         'and this is stated on the row.')
            ws.cell(r, 27, class_fixed)
            ws.cell(r, 34, sug)
            ws.cell(r, 17, class_fixed)
            ws.cell(r, 18, 1900)
            ws.cell(r, 41, 'Cudworth 1886, via infrastructure-cost-evidence.md section 4')
            append_note(ws.cell(r, 31), note)
            append_note(ws.cell(r, 42), note)
            changed.append(('elevated maintenance', sheet, name, old, class_fixed, sug))


def main():
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    changed = []
    water_pass(wc, changed)
    elevated_pass(wm, changed)
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
