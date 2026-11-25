# -*- coding: utf-8 -*-
# wb_fv_pass44.py — apply the measured lorry overhaul bands to the two cost-balancing workbooks.
#
# Research pass 42 (New/ai/cost-balancing/research-pricing-report-42.md) recovered three itemised
# Commercial Motor costings that print both the total maintenance and the overhaul component for
# the same lorry: 1938 4-5 ton rigid 46 per cent, 1949 6-ton 53 per cent, 1955 6-ton oiler 44 per
# cent, with engine-only floors of 31-35 per cent. The 37.5 per cent coach composition does not
# apply: the lorry schedules classify chassis and body work as overhaul, the coach account does
# not. Four introduction-year bands are recommended, applied as a floor-and-cap to the annual
# provision (both tails are contradicted by the three compositions), with the interval corrected
# in the same pass (the measured intervals are 45,000-50,000 miles in 1938-55 and 100,000 miles in
# 1955; the 160,000 km applied to every lorry is more than twice the 1938 interval and less than
# half the modern one):
#
#   intro year     share band    interval
#   before 1930    35-50 (45)    80,000 km
#   1930-1959      44-56 (50)    80,000 km
#   1960-1984      25-35 (30)    160,000 km
#   1985-2004      20-30 (25)    400,000 km
#
# The share applies to the maintenance head, so the per-event overhaul costs in the Overhauls &
# upgrades sheet are rescaled to the same annual provision; the first:max shape is kept. The
# maintenance row's deduction and routine remainder are then rewritten to match, as in pass 43.
#
# Run: py -3 wb_fv_pass44.py [--write]. Dry run by default. Idempotent: rows carrying 'pass 44'
# are skipped. Never rebuild the workbooks.
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 44'
WRITE = '--write' in sys.argv

BANDS = [
    # (max intro year exclusive, label, min, centre, max, interval km)
    (1930, 'before 1930', 0.35, 0.45, 0.50, 80000.0),
    (1960, '1930-1959', 0.44, 0.50, 0.56, 80000.0),
    (1985, '1960-1984', 0.25, 0.30, 0.35, 160000.0),
    (10000, '1985-2004', 0.20, 0.25, 0.30, 400000.0),
]


def find_base():
    d = os.path.dirname(os.path.abspath(__file__))
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


def band_for(year):
    for limit, label, lo, mid, hi, km in BANDS:
        if year < limit:
            return label, lo, mid, hi, km
    return BANDS[-1][1:]


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']
    overhaul = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            overhaul[str(b)] = r

    ws = wm['Road vehicles']
    stats = {'changed': 0, 'skipped': 0, 'in_band': 0}
    problems = []
    samples = []
    for r in range(7, ws.max_row + 1):
        name = ws.cell(r, 1).value
        if not name:
            continue
        ae = str(ws.cell(r, 31).value or '')
        if 'pass 4' not in ae or MARK in ae:
            continue
        base = str(ws.cell(r, 2).value or '')
        rec = overhaul.get(base)
        if rec is None:
            continue
        tag = str(wo.cell(rec, 24).value or '')
        if not tag.startswith('lorry '):
            continue
        aa = ws.cell(r, 27).value
        if not isinstance(aa, (int, float)) or aa == 0:
            continue
        mH = re.search(r'Annual maintenance figure ([\d,.]+) GBP', ae)
        mK = re.search(r'at mean annual distance ([\d,]+) km', ae)
        first, mx, km0 = wo.cell(rec, 14).value, wo.cell(rec, 15).value, wo.cell(rec, 17).value
        if not (mH and mK and isinstance(first, (int, float))
                and isinstance(km0, (int, float)) and km0):
            problems.append(('arithmetic missing', r, name))
            stats['skipped'] += 1
            continue
        H = float(mH.group(1).replace(',', ''))
        K = float(mK.group(1).replace(',', ''))
        try:
            year = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            year = 1900
        mx = mx if isinstance(mx, (int, float)) else first
        mean0 = (first + mx) / 2.0
        O0 = mean0 * K / km0
        s0 = O0 / H if H else 0.0
        label, lo, mid, hi, km1 = band_for(year)
        s1 = min(max(s0, lo), hi)
        O1 = s1 * H
        mean1 = O1 * km1 / K
        ratio = (first / mean0) if mean0 else 1.0
        first1 = mean1 * ratio
        max1 = mean1 * (2.0 - ratio)
        R = H - O1
        F = 0.25 * R
        V = 0.75 * R / K
        in_band = abs(s1 - s0) < 1e-9
        if in_band:
            stats['in_band'] += 1
        stats['changed'] += 1
        note = ('Maintenance decomposition (pass 44). Annual maintenance figure %s GBP per '
                'vehicle-year in 1900 money, at mean annual distance %s km a year. The source '
                'figure is the Commercial Motor maintenance total, which states that it contains '
                'washing, servicing and "major repairs" (see pass 42), so overhauls are inside '
                'it. The lorry overhaul share is measured from the itemised Commercial Motor '
                'costings that print both sides: 46 per cent (1938 4-5 ton rigid at a 45,000-mile '
                'cycle), 53 per cent (1949 6-ton at 400 miles a week) and 44 per cent (1955 6-ton '
                'oiler at 800 miles a week), with engine-only floors of 31-35 per cent; overhauls '
                'are 72-85 per cent of the (e) "repairs and overhauls" subhead '
                '(research-pricing-report-42). This vehicle was introduced in %d, in the %s band '
                '(%d-%d per cent): %d per cent of this head is deducted. Routine remainder %s GBP '
                'a year, split 75/25 distance/standing (the measured 1959 split is 22-33 per cent '
                'standing at 31,200 miles a year, so the 25 per cent used is inside it): fixed %s '
                'GBP a year, per-km %.8f GBP per km. The overhaul target in the Overhauls & '
                'upgrades sheet was rescaled to the same provision (first %s, max %s GBP, '
                'interval %s km). %s Direction: a measured fleet account giving the total and the '
                'overhaul line for the same lorries would replace the band share; the band itself '
                'is STATED (three itemised costings by one Commercial Motor costs writer), not '
                'measured.'
                % (f2(H), format(int(K), ','), year, label, round(lo * 100), round(hi * 100),
                   round(s1 * 100), f2(R), f2(F), V, f2(first1), f2(max1), format(int(km1), ','),
                   ('The share and the interval are inside the band; the provision is unchanged.'
                    if (in_band and int(km1) == int(km0)) else
                    ('The share is inside the band; the interval was corrected from %s km to %s '
                     'km and the per-event cost rescaled to keep the same annual provision.'
                     % (format(int(km0), ','), format(int(km1), ','))) if in_band else
                    ('The pass 42 figure of %s GBP a year was %d per cent of the head, outside the '
                     'measured band; the provision is now %s GBP a year.'
                     % (f2(O0), round(s0 * 100), f2(O1))))))
        if len(samples) < 6:
            samples.append((r, name, year, s0, s1, O0, O1, km0, km1, note))
        if WRITE:
            ws.cell(r, 27, round(F, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(V, 8)
            ws.cell(r, 30).value = 1900
            ws.cell(r, 31, note)
            wo.cell(rec, 14, round(first1, 1))
            wo.cell(rec, 15, round(max1, 1))
            wo.cell(rec, 17, int(km1))
            wo.cell(rec, 24, str(tag) + (' | pass 44: %s band (%d-%d per cent of the maintenance '
                                         'head, centre %d); annual provision %s -> %s GBP, interval '
                                         '%s -> %s km, first/max %s/%s -> %s/%s. Basis: report 42, '
                                         'the three itemised Commercial Motor costings (46, 53 and '
                                         '44 per cent).'
                                         % (label, round(lo * 100), round(hi * 100),
                                            round(mid * 100), f2(O0), f2(O1),
                                            format(int(km0), ','), format(int(km1), ','),
                                            f2(first), f2(mx), f2(first1), f2(max1))))

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  changed %d (of which %d were already inside the band; interval only)'
          % (stats['changed'], stats['in_band']))
    print('  skipped %d' % stats['skipped'])
    for s in samples:
        print('\n--- r%d %s (intro %d): share %d%% -> %d%%, provision %.1f -> %.1f, interval %d -> %d'
              % (s[0], s[1], s[2], round(s[3] * 100), round(s[4] * 100), s[5], s[6], s[7], s[8]))
        print('    ' + s[9][:600])
    if problems:
        print('\nPROBLEMS:')
        for p in problems:
            print('   ', p)
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
