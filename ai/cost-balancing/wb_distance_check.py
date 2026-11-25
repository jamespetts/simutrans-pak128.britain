# -*- coding: utf-8 -*-
# wb_distance_check.py - report the rows whose stated mean annual distance differs from the
# class/era table by more than 10 per cent.
#
# Scope: the classes where the note states its own mean annual distance and the table is
# directly applicable: pass 47/62 carriages, pass 53 multiple units and pass 58 trams. The
# locomotive, road, ship and maglev figures are reference duties for the fixed/per-km split
# and are not an overhaul interval in years, so they are not checked here.
#
# Run: py -3 wb_distance_check.py [--verbose]. This is a report, not an audit; a measured
# row duty overrides the class/era reference.
import os
import re
import sys
from collections import Counter

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

VERBOSE = '--verbose' in sys.argv


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


def main():
    wm = load_workbook(MAINT, data_only=True)
    rows = []
    for sheet in ('Rail vehicles', 'Narrow gauge vehicles', 'Tram vehicles'):
        if sheet not in wm.sheetnames:
            continue
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            note = str(ws.cell(r, 31).value or '')
            if not name:
                continue
            if ('at mean annual distance' not in note
                    and 'pass 58' not in note and 'pass 61' not in note):
                continue
            try:
                intro = int(str(ws.cell(r, 5).value)[:4])
            except Exception:
                intro = 0
            if 'pass 58' in note or 'pass 61' in note:
                kind = 'tram'
            elif 'pass 53' in note:
                kind = 'multiple-unit'
            elif 'pass 47' in note or 'pass 62' in note:
                low = name.lower()
                if (ev.is_multiple_unit(low)
                        or any(k in low for k in ('tube stock', 'emu', 'demu', 'railcar',
                                                  'wagon'))):
                    continue
                kind = 'carriage'
            else:
                continue
            m = re.search(r'at mean annual distance ([\d,]+) km', note)
            if not m and kind == 'tram':
                m = re.search(r'at ([\d,]+) km a year', note)
            if not m:
                continue
            stated = float(m.group(1).replace(',', ''))
            if kind == 'multiple-unit':
                low = (name + ' ' + note).lower()
                reference = 120000.0 if any(
                    k in low for k in ('tube', 'lul', 'underground', 'dlr', 'docklands',
                                       'tyne & wear')) else ev.mean_annual_km(kind, intro)
            else:
                reference = ev.mean_annual_km(kind, intro)
            if not reference:
                continue
            diff = abs(stated - reference) / reference
            rows.append((diff, kind, name, intro, stated, reference))
    print('rows with a stated mean annual distance: %d' % len(rows))
    print('by kind: %s' % dict(Counter(x[1] for x in rows)))
    bad = [x for x in rows if x[0] > 0.10]
    print('deviations > 10 per cent: %d' % len(bad))
    print('by kind: %s' % dict(Counter(x[1] for x in bad)))
    for x in sorted(bad, key=lambda z: -z[0])[:20 if not VERBOSE else 200]:
        print('  %5.0f%%  %-16s %-55s %4s stated=%8.0f table=%8.0f'
              % (x[0] * 100, x[1], x[2][:55], x[3], x[4], x[5]))
    wm.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
