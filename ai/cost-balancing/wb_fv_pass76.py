# -*- coding: utf-8 -*-
# wb_fv_pass76.py - apply the labour-adjusted maglev guideway research of 2026-11-27.
#
# WHAT THIS PASS DOES
# 1. CAPITAL. The class prices move from GBP124,786 (at grade) and GBP152,238 (elevated) to
#    GBP128,000 and GBP158,000 per track-km, band GBP105,000-160,000 and GBP130,000-195,000.
#    The change is small (+2.6 and +3.8 per cent) because the Munich planning figures already in
#    the sheet are confirmed against the primary document and against the 1993 Hamburg-Berlin
#    estimate once both are deflated to 1900 money and labour-adjusted.
# 2. MAINTENANCE. The rate falls from 1.2 per cent of capital a year to 0.15 per cent for the
#    concrete structure, band 0.08-0.25 per cent. The measured and modelled evidence (Transrapid
#    0.08, CIGGT 0.12, Volpe 0.215, Morgantown 0.008-0.031) is an order of magnitude below the
#    figure pass 74 used, which had been built as a combined structure-and-equipment rate.
# 3. The notes record that the pakset has no maglev electrification way object, so the linear
#    motor (stator rail and winding, GBP16,047 per track-km in 1900 money) is not charged at all,
#    and neither is the line-side power and control (a further GBP64,495).
#
# Run: py -3 wb_fv_pass76.py [--write]. Dry run by default. Idempotent by the pass 76 marker.
import os
import shutil
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pass 76'
WRITE = '--write' in sys.argv
WAY_MONTH_YEAR = 0.09511464

AT_GRADE = 128000.0
ELEVATED = 158000.0
AT_GRADE_BAND = (105000.0, 160000.0)
ELEVATED_BAND = (130000.0, 195000.0)
ROUTINE_RATE = 0.0015
BAND_RATE = (0.0008, 0.0025)

CAPITAL = {
    'Concrete_Maglev_Track': (AT_GRADE, 'at grade'),
    'Concrete_Maglev_Track_Elevated': (ELEVATED, 'elevated'),
    'Economical_Concrete_Maglev_Track': (AT_GRADE, 'at grade'),
    'Economical_Concrete_Maglev_Track_Elevated': (ELEVATED, 'elevated'),
}

CAPITAL_BASIS = (
    '%s: labour-adjusted overseas guideway cost, structure only. At grade GBP128,000 per '
    'track-km (band GBP105,000-160,000); elevated GBP158,000 (band GBP130,000-195,000). The 1993 '
    'Hamburg-Berlin and 2007 Munich estimates agree within 4 per cent at grade and 7 per cent '
    'elevated once both are deflated to 1900 and adjusted for labour at a labour share L = 0.25 '
    'and a relative labour cost R = 1.09 for Germany. The Shanghai residual (2004) and the '
    'Changsha unit rate (2022) bracket the band once adjusted at R = 6.5. Excludes the stator '
    'rail and winding, line-side power and control, stations, signalling and vehicles. '
    'Research report 59 section 3 and the 2026-11-27 subagent report.'
)

MAINT_BASIS = (
    '%s: routine guideway maintenance on the concrete structure only, 0.15 per cent of capital a '
    'year, band 0.08-0.25 per cent. The evidence is Transrapid 0.08 per cent (cited 1994), CIGGT '
    '0.12, the Volpe 1992 model 0.215 and Morgantown measured 0.008-0.031. The previous 1.2 per '
    'cent was a combined structure-and-equipment rate applied to a structure-only capital base; it '
    'is withdrawn. The pakset maglev way carries no wear_capacity, so this field carries the whole '
    'recurring cost and renewal is not charged separately. Research report 59 section 3.'
)

NO_WAYOBJ = (
    'No maglev electrification way object exists in the pakset (no Obj=wayobj with '
    'waytype=maglev_track), so the linear motor and the line-side power and control are charged '
    'nowhere. In 1900 money the Munich line items are GBP10,391 a track-km for the stator support '
    'rail and GBP5,656 for the winding, GBP40,271 for substations and line cables and GBP24,224 for '
    'operation control. Recorded as a separate task; do not fold them into the way cost without a '
    'way object.'
)


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
BACKUP = os.path.join(BASE, 'ai', 'temp', 'pre-pass76')


def append_note(cell, text):
    old = str(cell.value or '')
    if MARK in old:
        return False
    cell.value = (old + ' | ' if old else '') + text
    return True


def capital(wb, changed):
    ws = wb['Ways - maglev']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in CAPITAL:
            continue
        if MARK in str(ws.cell(r, 33).value or ''):
            continue
        value, kind = CAPITAL[base]
        ws.cell(r, 22, value)
        ws.cell(r, 23, 1900)
        ws.cell(r, 24, CAPITAL_BASIS)
        append_note(ws.cell(r, 33), '%s: %s' % (MARK, NO_WAYOBJ))
        changed.append(('maglev capital', base, ws.cell(r, 10).value, value))
    return


def maintenance(wb, changed):
    ws = wb['Ways - maglev']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in CAPITAL:
            continue
        if MARK in str(ws.cell(r, 42).value or ''):
            continue
        value, kind = CAPITAL[base]
        band = AT_GRADE_BAND if kind == 'at grade' else ELEVATED_BAND
        routine = ROUTINE_RATE * value
        low = BAND_RATE[0] * value
        high = BAND_RATE[1] * value
        ws.cell(r, 17, round(routine, 2))
        ws.cell(r, 18, 1900)
        ws.cell(r, 27, round(routine, 2))
        ws.cell(r, 28, 1900)
        ws.cell(r, 34, round(routine / WAY_MONTH_YEAR))
        ws.cell(r, 44, round(low / WAY_MONTH_YEAR))
        ws.cell(r, 45, round(high / WAY_MONTH_YEAR))
        ws.cell(r, 31, MAINT_BASIS)
        append_note(ws.cell(r, 42), MAINT_BASIS.replace('%s: ' % MARK, MARK + ': '))
        changed.append(('maglev maintenance', base, '', round(routine, 2),
                        round(routine / WAY_MONTH_YEAR)))


def main():
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    changed = []
    capital(wc, changed)
    maintenance(wm, changed)
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
