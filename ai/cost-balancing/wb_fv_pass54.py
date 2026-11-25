# -*- coding: utf-8 -*-
# wb_fv_pass54.py — trailers: put the works refurbishment inside the FTA maintenance figure.
#
# WHY
# The road trailer rows take an annual maintenance figure from the Freight Transport Association's
# Managers' Guide to Distribution Costs and then charge a works refurbishment on top of it. The
# refurbishment is 148 to 1,871 per cent of the annual figure, and annualised to 26-293 per cent of
# it, because the event was a share of the purchase price with no reference to the annual figure.
# Research pass 48 establishes that a trailer does receive a works refurbishment (strip, blast,
# repaint, new curtains, floor and body, axle, brake and suspension overhaul), measured at about
# one third of a new trailer (TIP 2025; Cooks 1988 at GBP 4,000 against a GBP 12,000 new trailer),
# and that the FTA line gives no workscope. The treatment that cannot double count is therefore the
# envelope: the annual figure is the total, the refurbishment's annual share comes out of it, and
# the head plus that share equals the annual figure.
#
# THE RULE (research pass 48 section 5)
#   event (first and maximum) = 0.33 x the capital target, i.e. the row's 1900-money purchase price
#   interval                  = 440,000 km (11 years at the workbook's 40,000 km a year)
#   overhauls to maximum      = 1 (the first refurbishment is the maximum)
#   annual provision          = event / 11, capped at 50 per cent of the annual figure
#   head                      = annual figure - provision, split 75/25 fixed and per-kilometre
#
# Applies to every road row whose name denotes a trailer (45 FTA-based rows and 20 on the
# generator's 5-per-cent cart rule).
#
# Run: py -3 wb_fv_pass54.py [--write]. Dry run by default. Idempotent (marker 'pass 54').
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 54'
WRITE = '--write' in sys.argv
EVENT_SHARE = 0.33
YEARS = 11.0
CAP = 0.50
FIXED = 0.75
REF_KM = 40000.0


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
CAPW = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')


def num(pattern, text, default=None):
    m = re.search(pattern, text)
    if not m:
        return default
    try:
        return float(m.group(1).replace(',', ''))
    except ValueError:
        return default


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAPW, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    ws = wm['Road vehicles']
    done = 0
    capped = 0
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name or 'trailer' not in name.lower():
            continue
        note = str(ws.cell(r, 31).value or '')
        if MARK in note:
            continue
        q = ovh.get(str(ws.cell(r, 2).value))
        if not q:
            continue
        A = num(r'Annual maintenance figure ([\d,.]+) GBP', note)
        K = num(r'at mean annual distance ([\d,]+) km', note, REF_KM)
        capital = wo.cell(q, 13).value or 0
        if not A or not capital:
            continue
        prov = EVENT_SHARE * capital / YEARS
        was_capped = False
        if prov > CAP * A:
            prov = CAP * A
            was_capped = True
            capped += 1
        head = A - prov
        event = prov * YEARS
        fixed = FIXED * head
        per_km = (1.0 - FIXED) * head / K
        text = ('Maintenance decomposition (pass 54). Annual maintenance figure %s GBP per '
                'vehicle-year in 1900 money, at mean annual distance %s km a year; the figure is '
                'the Freight Transport Association trailer line or, for a horse-drawn trailer, the '
                'generator allowance. The measured total is the envelope: a trailer receives a '
                'works refurbishment (strip, blast, repaint, new curtains, floor and body, axle, '
                'brake and suspension overhaul) measured at about one third of a new trailer '
                '(TIP 2025; Cooks 1988 at GBP 4,000 against a GBP 12,000 new trailer), so the '
                'refurbishment is %s GBP every %g years at the reference duty, the first and the '
                'maximum at the same cost, and its annual share %s GBP comes out of the figure. '
                'The head is %s GBP a year, split %d/%d fixed and per kilometre: fixed %s GBP a '
                'year, %.8f GBP a km.%s Research pass 48 section 5; the 0.33 share and the '
                'eleven-year interval are the measured refurbishment and its life.'
                % (f2(A), format(int(K), ','), f2(event), YEARS, f2(prov), f2(head),
                   round(FIXED * 100), round((1 - FIXED) * 100), f2(fixed), per_km,
                   ' The annual share is held at half the figure because one third of this '
                   'trailer exceeds it, which leaves a low head and is recorded as a separate '
                   'defect.' if was_capped else ''))
        if WRITE:
            ws.cell(r, 27, round(fixed, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(per_km, 10)
            ws.cell(r, 30).value = 1900
            ws.cell(r, 31, text)
            wo.cell(q, 14, round(event, 1))
            wo.cell(q, 15, round(event, 1))
            wo.cell(q, 16, 1)
            wo.cell(q, 17, int(round(YEARS * REF_KM)))
            wo.cell(q, 24, ('trailer (pass 54, research pass 48): the FTA annual figure is the '
                            'envelope. The works refurbishment is 0.33 x the capital target at '
                            '440,000 km, first and maximum the same, and its annual share comes '
                            'out of the figure; head plus share equals the figure. | pass 54'))
        done += 1
    if WRITE:
        wm.save(MAINT)
        wc.save(CAPW)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  trailer rows set to the envelope rule: %d, of which the annual share was capped at '
          'half the figure: %d' % (done, capped))


if __name__ == '__main__':
    main()
