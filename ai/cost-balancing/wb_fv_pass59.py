# -*- coding: utf-8 -*-
# wb_fv_pass59.py - apply the multiple-unit reference distance from the distance table.
#
# WHY THIS PASS EXISTS
# Pass 53 put every multiple-unit car on the research pass 45 ladder at a mean annual
# distance of 172,600 km, an inherited modern default, and wrote that figure into every
# maintenance note. The capital intervals meanwhile carried several different values
# (800,000, 872,000, 960,000 and 1,380,800 km), so the note, the per-km charge and the
# interval did not agree. Research pass 45 states the reference duty as 100,000 miles a
# car-year (161,000 km), and the measured tube and metro duty is 120,000 km.
#
# THE TABLE
# New/ai/vehicle-cost/mean-annual-distance.md, represented by
# evidence_data.MEAN_ANNUAL_KM['multiple-unit']:
#   before 1960: 100,000 km a car-year (ESTIMATE, pass 42 first-generation band)
#   1960-1999: 120,000 km (measured tube and metro duty; ESTIMATE for mainline stock)
#   2000-2026: 161,000 km (100,000 miles, research pass 45 section 5)
# Tube, LUL, Underground, DLR, Docklands and Tyne & Wear stock take 120,000 km in every era.
#
# WHAT MOVES
# The 50/50 split from pass 53 is kept. The annual figure A, the 15 per cent provision, the
# event and the continuous head are unchanged. The per-km charge is rescaled to the table
# mean, and the overhaul interval becomes eight years at that mean. At the reference duty
# the fixed and per-km charges still add to the head.
#
# SCOPE
# Every pass 53 multiple-unit row whose maintenance note states a mean annual distance.
# Articulated sections with zero capital are skipped.
#
# Run: py -3 wb_fv_pass59.py [--write]. Dry run by default. Idempotent by the pass 59
# marker in the maintenance note.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 59'
WRITE = '--write' in sys.argv
YEARS = 8.0


def find_base():
    d = HERE
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-maintenance.xlsx')):
            return d
        p = os.path.dirname(d)
        if p == d:
            raise SystemExit('workspace root not found')
        d = p


BASE = find_base()
MAINT = os.path.join(BASE, 'New', 'cost-balancing-maintenance.xlsx')
CAP = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')


def mu_mean(name, note, intro):
    low = (name + ' ' + note).lower()
    if any(k in low for k in ('tube', 'lul', 'underground', 'dlr', 'docklands',
                              'tyne & wear')):
        return 120000.0, 'tube and metro stock, 120,000 km a car-year'
    value = ev.mean_annual_km('multiple-unit', intro)
    return value, 'the multiple-unit table, %s km a car-year' % format(int(value), ',')


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    ws = wm['Rail vehicles']
    wo = wc['Overhauls & upgrades']

    cap_row = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            cap_row[str(b)] = r

    stats = {'rows': 0, 'skipped': 0, 'missing': 0}
    by_mean = {}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'pass 53' not in note or 'at mean annual distance' not in note:
            continue
        if MARK in note:
            stats['skipped'] += 1
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            stats['missing'] += 1
            continue
        fixed = ws.cell(r, 27).value
        if not isinstance(fixed, (int, float)) or fixed <= 0:
            stats['missing'] += 1
            continue
        try:
            intro = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            intro = 1900
        mean, label = mu_mean(name, note, intro)
        perkm = fixed / mean
        interval = int(YEARS * mean)
        maint_note = re.sub(r'at mean annual distance [\d,]+ km',
                            'at mean annual distance %s km' % format(int(mean), ','), note)
        maint_note = (maint_note + ' | pass 59: the reference duty is %s, from '
                      'New/ai/vehicle-cost/mean-annual-distance.md. The 50/50 split, the '
                      'annual figure, the provision and the event are unchanged; the per-km '
                      'charge and the interval are rescaled to the reference duty.'
                      % label)
        old_interval = wo.cell(q, 17).value
        cap_note = str(wo.cell(q, 24).value or '')
        if isinstance(old_interval, (int, float)):
            cap_note = cap_note.replace(format(int(old_interval), ','), format(interval, ','))
        cap_note = (cap_note + ' | pass 59: the overhaul interval is %s km, eight years at '
                    '%s km a car-year (New/ai/vehicle-cost/mean-annual-distance.md).'
                    % (format(interval, ','), format(int(mean), ',')))
        if WRITE:
            ws.cell(r, 29).value = round(perkm, 10)
            ws.cell(r, 31, maint_note)
            wo.cell(q, 17, interval)
            wo.cell(q, 24, cap_note)
        stats['rows'] += 1
        by_mean[int(mean)] = by_mean.get(int(mean), 0) + 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  multiple-unit rows set to the distance table: %d; already marked: %d; '
          'missing overhaul row: %d' % (stats['rows'], stats['skipped'], stats['missing']))
    print('  by reference duty: %s' % dict(sorted(by_mean.items())))


if __name__ == '__main__':
    main()
