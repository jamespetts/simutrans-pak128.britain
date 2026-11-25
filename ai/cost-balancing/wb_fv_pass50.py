# -*- coding: utf-8 -*-
# wb_fv_pass50.py — give the maglev vehicles a divided maintenance figure.
#
# WHY
# overhaul_profile() has no branch for 'maglev-vehicles', so the class was dropped from the
# Overhauls & upgrades sheet exactly as the narrow gauge was: the maintenance rate was charged
# continuously and the overhaul mechanic never fired. The money was all there, but there was no
# works visit, no wear reset and no availability restoration - an incoherent vehicle.
#
# THE SPLIT
# No maglev operator publishes an overhaul share. The knowledge base's overhaul table already
# directs this class to the nearest analogue (rung 5), and the nearest analogue is the multiple
# unit: research pass 45 puts the MU overhaul at 15 per cent of the annual figure with an event of
# 1.2A every eight years. That rule is applied unchanged.
#
# The maintenance figure is a per-seat-km rate from the overseas systems (EUR 0.011 a seat-km,
# 2009, Almujibah and Preston 2018), so an annual figure needs a duty. 300,000 km a vehicle-year
# is an ESTIMATE for a high-speed system; it is stated in every basis and in the note. The
# interval is 8 years x 300,000 = 2,400,000 km.
#
# Run: py -3 wb_fv_pass50.py [--write]. Dry run by default. Idempotent.
import os
import re
import sys
from copy import copy
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

MARK = 'pass 50'
WRITE = '--write' in sys.argv
PROVISION = 0.15         # share of A (multiple-unit analogue, research pass 45)
YEARS = 8.0
DUTY_KM = 300000.0       # ESTIMATE: annual distance per maglev vehicle
FIRST_RATIO = 0.70


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


def dat_fields(key, base_name):
    out = dict(cost=None)
    path = os.path.join(BASE, 'New', key)
    if not os.path.isfile(path):
        return out
    block = {}
    want = (base_name or '').strip().lower()
    for raw in open(path, encoding='utf-8', errors='replace'):
        line = raw.split('#', 1)[0].strip()
        if not line:
            continue
        if re.match(r'^obj\s*=', line, re.I):
            if block.get('name', '').lower() == want:
                break
            block = {}
            continue
        if '=' in line:
            k, v = line.split('=', 1)
            block[k.strip().lower()] = v.strip()
    try:
        out['cost'] = int(float(block.get('cost')))
    except (TypeError, ValueError):
        pass
    return out


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    ws = wm['Maglev vehicles']
    ws_cap = wc['Maglev vehicles']
    wo = wc['Overhauls & upgrades']
    have = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            have[str(b)] = r
    cap = {}
    for r in range(7, ws_cap.max_row + 1):
        b = ws_cap.cell(r, 2).value
        if b:
            cap[str(b)] = ws_cap.cell(r, 22).value
    km = YEARS * DUTY_KM
    new_rows = []
    done = 0
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if MARK in note:
            continue
        base = str(ws.cell(r, 2).value or '')
        key = str(ws.cell(r, 3).value or '')
        V = ws.cell(r, 29).value
        if not isinstance(V, (int, float)) or V <= 0:
            continue
        A = V * DUTY_KM
        prov = PROVISION * A
        head = A - prov
        mx = 2.0 * prov * YEARS / (1.0 + FIRST_RATIO)
        first = FIRST_RATIO * mx
        newV = head / DUTY_KM
        note_out = ('Maintenance decomposition (pass 50). Annual maintenance figure %s GBP per '
                    'vehicle-year in 1900 money, being the overseas-system rate (EUR 0.011 a '
                    'seat-km at 2009 prices, Almujibah and Preston 2018) applied at an assumed '
                    '%s km a vehicle-year - an ESTIMATE, stated because the source is a rate per '
                    'seat-kilometre and not a per-year figure. The measured total is the envelope: '
                    'the works-overhaul provision is 15 per cent of it = %s GBP a year, the '
                    'nearest-analogue rule of research pass 45 (multiple unit: 15 per cent of the '
                    'annual figure, event 1.2A every eight years), and the continuous head is the '
                    'remainder, %s GBP a year, charged per km at %0.10f GBP. The event is %s GBP '
                    'every eight years (%s km at the assumed duty), the first at %s GBP. No maglev '
                    'operator publishes an overhaul share, so the analogue is a rung-5 estimate; '
                    'an Aichi or Shanghai rolling-stock maintenance line would replace it.'
                    % (f2(A), format(int(DUTY_KM), ','), f2(prov), f2(head), newV, f2(mx),
                       format(int(km), ','), f2(first)))
        if WRITE:
            ws.cell(r, 27).value = None
            ws.cell(r, 28).value = 1900
            ws.cell(r, 29).value = round(newV, 10)
            ws.cell(r, 30).value = 1900
            ws.cell(r, 31, note_out)
        done += 1
        if base in have:
            continue
        new_rows.append(dict(name=name, base=base, key=key, capital=cap.get(base) or 0,
                             first=first, mx=mx, km=km))
    start = wo.max_row + 1
    new_rows.sort(key=lambda d: d['base'].lower())
    for i, d in enumerate(new_rows):
        r = start + i
        vals = {1: d['name'], 2: d['base'], 3: d['key'], 4: 'vehicle', 5: None,
                6: 'maglev-vehicles', 13: d['capital'], 14: round(d['first'], 1),
                15: round(d['mx'], 1), 16: 3, 17: int(d['km']), 18: 0.4, 19: None,
                24: ('maglev (pass 50): no operator publishes an overhaul share, so the nearest '
                     'analogue (research pass 45, multiple unit) is used - 15 per cent of the '
                     'annual figure, event 1.2A every eight years at an assumed 300,000 km a '
                     'vehicle-year. Rung 5. | pass 50')}
        df = dat_fields(d['key'], d['base'])
        vals[7] = df['cost']
        if WRITE:
            for c in range(1, 25):
                cell = wo.cell(r, c)
                cell.value = vals.get(c)
                src = wo.cell(7, c)
                if src.has_style:
                    cell._style = copy(src._style)
            for c, src in ((20, 14), (21, 15)):
                wo.cell(r, c, '=IF(AND(ISNUMBER({s}{r}),ISNUMBER(Params!$B$2),'
                              'ISNUMBER(Params!$B$12)),{s}{r}/Params!$B$12/Params!$B$2,"")'
                        .format(s=get_column_letter(src), r=r))
            wo.cell(r, 22, vals[17])
            wo.cell(r, 23, '=IF(AND(ISNUMBER({s}{r}),ISNUMBER(Params!$B$2),'
                           'ISNUMBER(Params!$B$12)),{s}{r}/Params!$B$12/Params!$B$2,"")'
                    .format(s='S', r=r))
    # intro year from the capital sheet
    intro = {str(ws_cap.cell(r, 2).value): ws_cap.cell(r, 5).value
             for r in range(7, ws_cap.max_row + 1) if ws_cap.cell(r, 2).value}
    if WRITE:
        for i, d in enumerate(new_rows):
            wo.cell(start + i, 5, intro.get(d['base']))
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  maglev rows divided %d, overhaul rows appended %d' % (done, len(new_rows)))
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
