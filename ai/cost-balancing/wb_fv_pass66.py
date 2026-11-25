# -*- coding: utf-8 -*-
# wb_fv_pass66.py - put the intermediate electric locomotives on the electric track.
#
# WHY THIS PASS EXISTS
# Pass 49 gave every locomotive row the report 46 ladder and made a straight-electric locomotive
# take 0.5 of the ladder, because Calder's 1977 Class 87 was 52 per cent of the Class 47 on the
# same passenger duty. Research pass 50 shows that ratio is a class result, not a traction-type
# constant: it read the modern ladder as two class tracks, with the electric track at 1,103 in
# 1977 (Calder's Class 87) and 1,045 in 1995 (the BRML mixed-fleet turnover), and 868 in 2018
# (the measured Class 92 contract). Research pass 46 row 12 supplies the 1950s electric point:
# the Southern Region electric locomotives at GBP 5,300 each in 1949-50, repairs only, which is
# 1,476 in 1900 money.
#
# The 2026-11-25 decision is to interpolate the intermediate electric locomotives between those
# 1950s/1960s and 1980s/1990s figures rather than halve the diesel ladder. No class-specific
# measured figure exists for Classes 89, 90 or 91, so all three sit on the electric track at
# their introduction year. (
# The Class 92 already carries its own measured class figure from pass 63, and the Class 88 is
# the dual-mode Class 68 analogue from pass 64; neither is touched here.)
#
# WHAT MOVES
# A, the works-overhaul provision, the continuous head, the fixed and per-km charges and the
# overhaul event move together. The diesel/electric rules are unchanged: renewals 0, provision
# 39 per cent of A, 60/40 fixed/per-km, a seven-year heavy-event interval, and one event to the
# maximum. The row's own measured duty (109,000 km an engine-year) is unchanged.
#
# SCOPE
# Exactly three rows, matched by base name on the 'Rail vehicles' sheet: BR-Class89, BR-Class90
# and BR-Class91. The note test (engine-year and pass 49) is a guard, not the selector, so no
# other locomotive is included by a class-name filter.
#
# Run: py -3 wb_fv_pass66.py [--write]. Dry run by default. Idempotent by the pass 66 marker.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 66'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
PROVISION = 0.39
FIXED_SHARE = 0.60
YEARS = 7.0
TARGETS = {'BR-Class89': 'BR Class 89',
           'BR-Class90': 'BR Class 90',
           'BR-Class91': 'BR Class 91 "Electra"'}


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
    done = set()
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        base = str(ws.cell(r, 2).value or '').strip()
        if base not in TARGETS:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'engine-year' not in note:
            stats['missing'] += 1
            continue
        if MARK in note and not FORCE:
            stats['skipped'] += 1
            done.add(base)
            continue
        q = cap_row.get(base)
        if not q:
            stats['missing'] += 1
            continue
        mK = re.search(r'at mean annual distance ([\d,]+) km', note)
        if not mK:
            stats['missing'] += 1
            continue
        K = float(mK.group(1).replace(',', ''))
        try:
            intro = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            stats['missing'] += 1
            continue
        A = ev.interp_log(ev.ELEC_LOCO_LADDER, intro)
        rho = 0.0
        prov = PROVISION * A
        head = A - prov
        F = FIXED_SHARE * head
        V = (1.0 - FIXED_SHARE) * head / K
        km = int(round(YEARS * K))
        event = prov * YEARS
        note_out = (
            'Maintenance decomposition (pass 66, research passes 46 and 50). Annual maintenance '
            'figure %s GBP per engine-year in 1900 money, at mean annual distance %s km a year. '
            'Source: the electric-locomotive maintenance track at the introduction year (%d): '
            '1,476 GBP at 1950, 1,103 at 1977, 1,045 at 1995 and 868 at 2018, log-linear between '
            'and flat outside. The 1950 point is the Southern Region electric locomotives at '
            'GBP 5,300 each in 1949-50, repairs only, deflated at the general index 359 '
            '(research-pricing-report-46 row 12); the 1977 point is Calder\'s Class 87 at '
            '274,000 km converted to 1900 money (research-pricing-report-46 row 19); the 1995 '
            'point is the BRML mixed-fleet heavy-maintenance turnover and the 2018 point the '
            'measured Class 92 full-maintenance contract (research-pricing-report-50 section 5, '
            'item 6). The row takes the track, not half of the diesel ladder: the 0.5 factor is '
            'Calder\'s 1977 Class 87/Class 47 ratio, a class result rather than a traction-type '
            'constant (research-pricing-report-50 section 5, item 5). Class 90 has no measured '
            'figure of its own, so it sits on the same line between the 1977 and 1995 electric '
            'points. Composition: the 1950 point is repairs only and net; the 1977 and later '
            'points have capital outside. Renewals are 0 per cent = 0 GBP a year (the 1977 and '
            'later points have capital outside, so nothing is deducted), leaving %s GBP net. '
            'The measured total is the envelope: the works-overhaul provision is %s per cent of '
            'A = %s GBP a year (the diesel/electric rule from the Class 47 pair), and the '
            'continuous head is the remainder, %s GBP a year, so the head plus the amortised '
            'events equals the net total. The interval is %g years = %s km at that distance '
            '(the diesel/electric heavy-event interval); the event is %s GBP every %g years, the '
            'first at %s GBP rising to %s GBP over 0 overhauls, a mean event of %s GBP. The head '
            'is split %d/%d fixed/per-km at that distance: fixed %s GBP a year, per-km %.10f GBP '
            'per km. The per-km rate is the variable share of the head, not a separate constant. '
            '| pass 49 | pass 63 | pass 66'
            % (f2(A), format(int(K), ','), intro, f2(A), f2(100.0 * PROVISION), f2(prov),
               f2(head), YEARS, format(km, ','), f2(event), YEARS, f2(event), f2(event),
               f2(event), round(FIXED_SHARE * 100), round((1 - FIXED_SHARE) * 100), f2(F), V))
        cap_note = (
            'locomotive (pass 66, research passes 46 and 50): the measured annual total is the '
            'envelope. A = %s GBP an engine-year from the electric-locomotive track (1,476 at '
            '1950, 1,103 at 1977, 1,045 at 1995, 868 at 2018), read at the %d introduction year. '
            'The 0.5-of-the-diesel-ladder rule is withdrawn for this class: it is Calder\'s 1977 '
            'Class 87/Class 47 ratio, a class result, not a traction-type constant. Class 90 has '
            'no measured figure of its own and sits on the same line. Renewals 0; overhaul '
            'provision %s per cent of A; head = the residual. The interval is %g years = %s km; '
            'first and maximum event %s GBP, flat (one event to the maximum). The composition '
            'break and the measured points are stated in the maintenance note. | pass 49 | '
            'pass 63 | pass 66' % (f2(A), intro, f2(100.0 * PROVISION), YEARS, format(km, ','), f2(event)))
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
        done.add(base)
        stats['rows'] += 1
        print('  %-22s intro %d  A=%9.2f  prov=%8.2f  head=%8.2f  fixed=%7.2f  km=%s  '
              'event=%8.2f' % (TARGETS[base], intro, A, prov, head, F, format(km, ','), event))

    missing = sorted(set(TARGETS) - done)
    if missing:
        print('  NOT FOUND: %s' % ', '.join(missing))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  electric rows re-based: %d; already marked: %d; missing: %d'
          % (stats['rows'], stats['skipped'], stats['missing']))


if __name__ == '__main__':
    main()
