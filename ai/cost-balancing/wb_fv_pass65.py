# -*- coding: utf-8 -*-
# wb_fv_pass65.py - apply research pass 55's Shanghai acquisition price to the maglev rows.
#
# WHY THIS PASS EXISTS
# The maglev capital targets came from Almujibah and Preston (2018): EUR 49,233 a seat at 2009
# prices, converted to 507.6 GBP a seat in 1900 money. Research pass 55 found the only
# transaction-level maglev vehicle price: Shanghai imported Transrapid cars at more than RMB 100m
# a car (two reports five years apart), GBP 105,129 a car in 1900 money, 92.8 seats a five-car
# set = 1,133 GBP a seat before the 0.96 labour adjustment, 1,087.5 after. The pass recommends
# replacing 507.6 with 1,087.5. The maintenance rate is unchanged: no operator account separates
# rolling-stock maintenance, and the evidence brackets the existing 0.00010257 GBP a seat-km.
#
# WHAT MOVES
# The class capital target only: 1,087.5 GBP a seat, or 4,194.6 GBP a metre on the 14 m, 54-seat
# reference car for stock with no seat count. The overhaul rows keep their A-based events; only
# their capital column is brought into line. The maintenance figures do not move.
#
# Run: py -3 wb_fv_pass65.py [--write]. Dry run by default. Idempotent by the pass 65 marker.
import os
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 65'
WRITE = '--write' in sys.argv
CAP_PER_SEAT = 1087.5
CAP_PER_M = 4194.6
OLD_PER_SEAT = 507.6


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
CAP = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')


def main():
    wc = load_workbook(CAP, data_only=False)
    ws = wc['Maglev vehicles']
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    specs = ev.vehicle_specs()
    stats = {'rows': 0, 'skipped': 0, 'missing': 0}
    samples = []
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        base = str(ws.cell(r, 2).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 24).value or '')
        if MARK in note:
            stats['skipped'] += 1
            continue
        sp = specs.get(base.lower(), {})
        seats = float(sp.get('seats') or 0)
        length = float(sp.get('length') or 0)
        old = ws.cell(r, 22).value
        if not isinstance(old, (int, float)) or old <= 0:
            stats['missing'] += 1
            continue
        if seats > 0:
            new = CAP_PER_SEAT * seats
            unit = '%g seats at %s GBP a seat' % (seats, format(CAP_PER_SEAT, ','))
        elif length > 0:
            new = CAP_PER_M * length
            unit = '%g m at %s GBP a metre' % (length, format(CAP_PER_M, ','))
        else:
            stats['missing'] += 1
            continue
        new = int(round(new))
        basis = (
            'Overseas maglev rolling stock: Shanghai imported Transrapid cars at more than '
            'RMB 100m a car (2003), GBP 105,129 a car in 1900 money, 92.8 seats a five-car set '
            '= 1,087.5 GBP a seat after the 0.96 labour adjustment (research pass 55; band '
            '761-1,133); %s. The per-metre rate for stock with no seat count is 4,194.6 GBP a '
            'metre on the 14 m, 54-seat reference car. Maintenance is the separate overseas rate, '
            '0.00010257 GBP a seat-km. | pass 65' % unit)
        if WRITE:
            ws.cell(r, 22, new)
            ws.cell(r, 23, 1900)
            ws.cell(r, 24, basis)
            q = ovh.get(base)
            if q:
                wo.cell(q, 13, new)
                wo.cell(q, 24, str(wo.cell(q, 24).value or '') +
                        ' | pass 65: the capital target is the Shanghai acquisition price, %s GBP '
                        '(%s); the overhaul events are A-based and unchanged.'
                        % (format(new, ','), unit))
        stats['rows'] += 1
        if len(samples) < 8:
            samples.append((name, seats, length, old, new))
    if WRITE:
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  maglev rows re-priced: %d; already marked: %d; missing: %d'
          % (stats['rows'], stats['skipped'], stats['missing']))
    for s in samples:
        print('  %-48s seats=%g length=%g old=%s new=%s'
              % (s[0], s[1], s[2], format(int(s[3]), ','), format(s[4], ',')))


if __name__ == '__main__':
    main()
