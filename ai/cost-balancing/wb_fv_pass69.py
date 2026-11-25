# -*- coding: utf-8 -*-
# wb_fv_pass69.py - put the locomotive per-km charge on the class and era distance table.
#
# WHY THIS PASS EXISTS
# Pass 49 derived the per-km charge as the variable share of the continuous head over "the row's
# own mean annual distance". For 40 near-1950 diesel and electric rows and 11 post-1948 steam rows
# that distance was not a measurement: it was the inherited workbook default of 109,000 km (and
# 40,000 km for steam). A single 109,000 km figure on a 1950s shunter and on a 2010s express is a
# default, not a duty, and the standing rule is that a modern default is not a measurement: use
# the class and era distance table. The generator now reads that table, so the workbook and a
# rebuild agree only if the rows move to it.
#
# WHAT MOVES
# The per-km charge and the overhaul interval of the rows whose stated distance is the inherited
# default. The fixed charge, A, the renewals deduction, the provision and the overhaul event do
# not move: they do not depend on the duty.
#
# SCOPE
# The `Rail vehicles` rows carrying an engine-year note and a stated distance, where the distance
# is the default the workbook inherited:
#   - 109,000 km on any row (40 rows); and
#   - 40,000 km on a row introduced in 1948 or later (11 steam rows).
# A measured class duty is kept: Class 37 at 81,000 (Calder 1977), Class 47 at 113,000, the Class
# 55 at 226,000, the Class 86 at 176,000, the Class 87 at 274,000 and the CSLR tube locomotive at
# 120,000. The table then supplies 40,000 km before 1948, 65,000 in 1948-60, 113,000 in 1961-89
# and 150,000 from 1990.
#
# Run: py -3 wb_fv_pass69.py [--write] [--force]. Dry run by default. Idempotent by the pass 69
# marker.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 69'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
DEFAULT_KM = 109000
STEAM_DEFAULT_KM = 40000
YEARS = 7.0


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
    samples = []
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'engine-year' not in note or 'per vehicle-year' in note or 'per animal-year' in note:
            continue
        if MARK in note and not FORCE:
            stats['skipped'] += 1
            continue
        mK = re.search(r'at mean annual distance ([\d,]+) km', note)
        if not mK:
            stats['missing'] += 1
            continue
        repair = MARK in note
        if repair:
            # Repair mode: strip the previous pass 69 suffix and recompute from the note's own
            # arithmetic, so a wrong first write can be corrected without a backup restore.
            note = re.sub(r'\s*\| pass 69:[^|]*$', '', note).rstrip()
        K_old = float(mK.group(1).replace(',', ''))
        try:
            intro = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            stats['missing'] += 1
            continue
        if not (K_old == DEFAULT_KM or (K_old == STEAM_DEFAULT_KM and intro >= 1948)
                or repair):
            continue
        K_new = ev.mean_annual_km('locomotive', intro)
        if not K_new or (K_new == K_old and not repair):
            stats['skipped'] += 1
            continue
        mhead = re.search(r'the continuous head is the remainder, ([\d,.]+) GBP', note)
        msplit = re.search(r'split (\d+)/(\d+) fixed/per-km', note)
        myrs = re.search(r'The interval is ([\d.]+) years', note)
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not mhead or not msplit or not q:
            stats['missing'] += 1
            continue
        years = float(myrs.group(1)) if myrs else YEARS
        head = float(mhead.group(1).replace(',', ''))
        fixed_share = float(msplit.group(1)) / 100.0
        V = (1.0 - fixed_share) * head / K_new
        km_interval = int(round(years * K_new))
        if WRITE:
            ws.cell(r, 29).value = round(V, 10)
            wo.cell(q, 17, km_interval)
            note_out = re.sub(r'at mean annual distance [\d,]+ km a year',
                              'at mean annual distance %s km a year' % format(int(K_new), ','),
                              note, count=1)
            note_out = re.sub(r'The interval is [\d.]+ years = [\d,]+ km at that distance',
                              'The interval is %g years = %s km at that distance'
                              % (years, format(km_interval, ',')), note_out)
            note_out = re.sub(r'per-km [\d.]+ GBP per km',
                              'per-km %.10f GBP per km' % V, note_out)
            note_out = (note_out.rstrip() + ' | pass 69: the inherited %s km default is replaced '
                        'by the class and era distance table (%s km at this introduction year); '
                        'the fixed charge, the provision and the overhaul event are unchanged.'
                        % (format(int(K_old), ','), format(int(K_new), ',')))
            ws.cell(r, 31, note_out)
        stats['rows'] += 1
        if len(samples) < 12:
            samples.append((name, intro, K_old, K_new, V, km_interval))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  locomotive rows moved to the distance table: %d; already marked: %d; missing: %d'
          % (stats['rows'], stats['skipped'], stats['missing']))
    for s in samples:
        print('  %-44s intro %d  %8s -> %8s km  per-km %.10f  interval %s'
              % (s[0][:44], s[1], format(int(s[2]), ','), format(int(s[3]), ','), s[4],
                 format(s[5], ',')))


if __name__ == '__main__':
    main()
