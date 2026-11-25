# -*- coding: utf-8 -*-
# wb_fv_pass64.py - Class 88 electric-factor correction and Class 92 mixed-traffic wording.
#
# WHY THIS PASS EXISTS
# Research pass 50 measured the Class 92 at 868 GBP an engine-year on the 2018 Caledonian Sleeper
# contract, and 5 of its recommendations were applied by pass 63. Two points remained:
#   1. The 0.5 "straight-electric" factor is Calder's 1977 Class 87/Class 47 passenger result.
#      It does not describe a post-1995 dual-mode mixed-traffic locomotive. The Class 88 (2014)
#      still read 307.41 = 0.5 x 614.82. The Class 68 diesel at the same date is 614.82, and is
#      the nearest measured class by generation and duty; the Class 88 takes that level.
#   2. The Class 92 is a mixed-traffic locomotive (the pakset object has freight=None), not an
#      electric-passenger type. The 868 is a class/duty override from a 12-locomotive sleeper
#      contract, not a clean electric-passenger track point. The note now says so.
#
# WHAT MOVES
# Class 88 only: A 307.41 -> 614.82; provision 119.89 -> 239.78; head 187.52 -> 375.04; first and
# maximum overhaul event 839.23 -> 1,678.46; fixed 112.51 -> 225.02; per-km 0.00068815 ->
# 0.00137629. The interval (7 years = 763,000 km) and the diesel/electric 39 per cent provision
# and 60/40 split are unchanged. The Class 92 numbers are unchanged; its notes gain the
# mixed-traffic/Caledonian Sleeper wording.
#
# Run: py -3 wb_fv_pass64.py [--write]. Dry run by default. Idempotent by the pass 64 marker.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 64'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
PROVISION = 0.39
FIXED_SHARE = 0.60
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


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def c88_note(note, A, rho, prov, head, event, F, V):
    note = note.replace(
        '(a straight-electric locomotive takes half the rung: Calder\'s Class 87 is 52 per cent '
        'of the Class 47 on the same duty)',
        '(the 0.5 straight-electric factor is not applied: the Class 88 is a dual-mode '
        'mixed-traffic locomotive, and the Class 68 diesel at the same date is the nearest '
        'measured class)')
    note = note.replace('Annual maintenance figure 307.41', 'Annual maintenance figure 614.82')
    note = note.replace('leaving 307.41 GBP net', 'leaving 614.82 GBP net')
    note = note.replace('provision is 39 per cent of A = 119.89',
                        'provision is 39 per cent of A = 239.78')
    note = note.replace('continuous head is the remainder, 187.52',
                        'continuous head is the remainder, 375.04')
    note = note.replace(
        'event is 839.23 GBP every 7 years, the first at 839.23 GBP rising to 839.23 GBP over 0 '
        'overhauls, a mean event of 839.23',
        'event is 1,678.46 GBP every 7 years, the first at 1,678.46 GBP rising to 1,678.46 GBP '
        'over 0 overhauls, a mean event of 1,678.46')
    note = note.replace('fixed 112.51 GBP a year, per-km 0.00068815',
                        'fixed 225.02 GBP a year, per-km 0.00137629')
    if 'pass 64' not in note:
        note += (' | pass 64 (research pass 50 recommendation 5): the 0.5 electric factor is '
                 'withdrawn for this post-1995 dual-mode mixed-traffic locomotive. The factor is '
                 'Calder\'s 1977 Class 87/Class 47 passenger result; the nearest measured class at '
                 'the same date is the Class 68 diesel at 614.82, and the Class 88 takes that level. '
                 'The ladder\'s 2014 rung is 614.82; the 1995 and 2020 rungs are unchanged.')
    return note


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

    stats = {'c88': 0, 'c92': 0, 'skipped': 0}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'engine-year' not in note or 'pass 49' not in note:
            continue
        if MARK in note and not FORCE:
            stats['skipped'] += 1
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            continue
        mK = re.search(r'at mean annual distance ([\d,]+) km', note)
        if not mK:
            continue
        K = float(mK.group(1).replace(',', ''))
        if name == 'BR Class 88 "Vossloh Euro Dual"':
            A = 614.82
            rho = 0.0
            prov = PROVISION * A
            head = A - rho - prov
            F = FIXED_SHARE * head
            V = (1.0 - FIXED_SHARE) * head / K
            km = int(round(YEARS * K))
            event = prov * YEARS
            note_out = c88_note(note, A, rho, prov, head, event, F, V)
            cap_note = str(wo.cell(q, 24).value or '')
            cap_note = cap_note.replace(
                'A = the locomotive ladder at the intro year (307.41 GBP here, electric)',
                'A = the locomotive ladder at the intro year (614.82 GBP here, no 0.5 factor)')
            cap_note = cap_note.replace('first and maximum event 839.23 GBP',
                                        'first and maximum event 1,678.46 GBP')
            if 'pass 64' not in cap_note:
                cap_note += (' | pass 64 (research pass 50 recommendation 5): the 0.5 electric '
                             'factor is withdrawn for this post-1995 dual-mode mixed-traffic '
                             'locomotive; the Class 68 diesel at the same date is the nearest '
                             'measured class, 614.82. The interval and the 39 per cent provision '
                             'are unchanged.')
            if WRITE:
                ws.cell(r, 27, round(F, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = round(V, 10)
                ws.cell(r, 30, 1900)
                ws.cell(r, 31, note_out)
                wo.cell(q, 14, round(event, 1))
                wo.cell(q, 15, round(event, 1))
                wo.cell(q, 16, 0)
                wo.cell(q, 17, km)
                wo.cell(q, 18, 0.8)
                wo.cell(q, 24, cap_note)
            stats['c88'] += 1
            print('  Class 88: A=%s head=%s event=%s km=%s' % (f2(A), f2(head), f2(event),
                                                               format(km, ',')))
        elif name == 'BR Class 92':
            suffix = (' | pass 64: the Class 92 is a mixed-traffic locomotive (the pakset object '
                      'has freight=None); the contract covers 12 locomotives on the Caledonian '
                      'Sleeper, a low-mileage passenger duty. The 868 is a class/duty override, '
                      'not a general mixed-traffic average or an electric-passenger track point.')
            if WRITE:
                ws.cell(r, 31, note if MARK in note else note + suffix)
                cap_note = str(wo.cell(q, 24).value or '')
                wo.cell(q, 24, cap_note if MARK in cap_note else cap_note + suffix)
            stats['c92'] += 1
            print('  Class 92: mixed-traffic wording appended; numbers unchanged')

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  Class 88 corrected: %d; Class 92 notes: %d; already marked: %d'
          % (stats['c88'], stats['c92'], stats['skipped']))


if __name__ == '__main__':
    main()
