# -*- coding: utf-8 -*-
# wb_fv_pass60.py - apply the carriage distances from the mean annual distance table.
#
# WHY THIS PASS EXISTS
# Pass 47 put each carriage on the measured overhaul bands (28 / 24 / 19 / 12 / 10 / 8 per
# cent of A at 6 / 5 / 3 / 2 / 2 / 2.6 years) but left the maintenance split on the older
# pass 42 mean annual distances: 32,000 km for Victorian carriages, 37,000 for Edwardian,
# 40,000 for Grouping, 60,000 for Mk 1/2 and 45,450 for Mk 3. Several rows carried a modern
# default (109,000 or 172,600 km). The overhaul band and the maintenance split therefore used
# different reference duties. This pass puts both on the table in
# New/ai/vehicle-cost/mean-annual-distance.md:
#   1830-1889 35,000; 1890-1922 36,000; 1923-1947 55,000; 1948-1974 88,000;
#   1975-1999 120,000; 2000-2026 113,000 km a vehicle-year.
#
# WHAT MOVES
# Only the reference duty, the per-km charge and the overhaul interval in kilometres. The
# annual figure A, the renewals deduction, the overhaul provision, the continuous head and
# the event cost are unchanged. The 70/30 fixed/per-km split is kept. At the new reference
# duty the fixed and per-km charges still add to the head, and the interval in years is the
# value the overhaul band states.
#
# SCOPE
# Standard-gauge rail-vehicles rows whose maintenance note carries pass 47 and states its
# mean annual distance. Multiple-unit stock, tube stock, passenger-rated wagons and the
# narrow gauge are excluded: the first three belong to another class rule and the narrow
# gauge keeps its own 40,000 km assumption.
#
# Run: py -3 wb_fv_pass60.py [--write]. Dry run by default. Idempotent by the pass 60
# marker in the maintenance note.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 60'
WRITE = '--write' in sys.argv
FIXED_SHARE = 0.70


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


def band_years(intro):
    value = 6.0
    for start, years in ((1830, 6.0), (1890, 5.0), (1923, 3.0), (1948, 2.0),
                         (1975, 2.0), (2000, 2.6)):
        if intro >= start:
            value = years
    return value


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

    stats = {'rows': 0, 'skipped': 0, 'missing': 0, 'excluded': 0}
    by_mean = {}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'pass 47' not in note or 'at mean annual distance' not in note:
            continue
        if MARK in note:
            stats['skipped'] += 1
            continue
        low = name.lower()
        if ev.is_multiple_unit(low) or any(
                k in low for k in ('tube stock', 'emu', 'demu', 'railcar', 'wagon')):
            stats['excluded'] += 1
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
        mean = ev.mean_annual_km('carriage', intro)
        m = re.search(r'interval ([\d.]+) years', note)
        years = float(m.group(1)) if m else band_years(intro)
        head = fixed / FIXED_SHARE
        perkm = (1.0 - FIXED_SHARE) * head / mean
        interval = int(years * mean)
        maint_note = re.sub(r'at mean annual distance [\d,]+ km',
                            'at mean annual distance %s km' % format(int(mean), ','), note)
        maint_note = (maint_note + ' | pass 60: the reference duty is %s km a vehicle-year, '
                      'the carriage row of New/ai/vehicle-cost/mean-annual-distance.md. The '
                      'annual figure, the provision, the head and the event are unchanged; the '
                      'per-km charge and the interval are rescaled to the reference duty.'
                      % format(int(mean), ','))
        old_interval = wo.cell(q, 17).value
        cap_note = str(wo.cell(q, 24).value or '')
        if isinstance(old_interval, (int, float)):
            cap_note = cap_note.replace(format(int(old_interval), ','), format(interval, ','))
        cap_note = (cap_note + ' | pass 60: the overhaul interval is %s km at %s km a '
                    'vehicle-year (New/ai/vehicle-cost/mean-annual-distance.md).'
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
    print('  carriage rows set to the distance table: %d; already marked: %d; excluded: %d; '
          'missing overhaul row: %d' % (stats['rows'], stats['skipped'], stats['excluded'],
                                        stats['missing']))
    print('  by reference duty: %s' % dict(sorted(by_mean.items())))


if __name__ == '__main__':
    main()
