# -*- coding: utf-8 -*-
# wb_fv_pass57.py - restore the animal rule for the six tram-sheet horses.
#
# WHY THIS PASS EXISTS
# Pass 55 applied the tramcar maintenance ladder to every row on the 'Tram vehicles'
# sheet with a positive capital target. That sheet also holds six horses: three pairs
# and three singles. Pass 48 had placed them on the animal rule, and pass 55 replaced
# it with the tramcar envelope (84 GBP a car-year, 35 per cent renewals, 28 per cent
# overhaul provision at two years and 96,000 km). Pass 56 then set their upgrade price
# to 22 per cent of the purchase price, where every other animal row carries 50 per cent.
#
# THE ANIMAL RULE (pass 43 maintenance figure; pass 48 overhaul)
#   Annual maintenance: 45 GBP per animal-year in 1900 money, from the London horse-keep
#   accounts 1876-97 (band 28-60), excluding the horsekeeper. A pair is two animals, so
#   its annual figure is 90 GBP. The whole figure is a standing charge; a horse has no
#   distance-based maintenance.
#   Overhaul: the replacement of the animal at the end of its working life, at 100 per
#   cent of the purchase price. The measured renewal cadence is the Leeds tramway
#   horses, about once every seven years at a cost equal to the purchase price
#   (1894-5 accounts). Seven years at the knowledge base's 10,000 km/yr assumption gives
#   70,000 km. First and maximum are the same, so the rungs do not matter.
#   Downtime: 0.1 months, as in pass 48.
#   Upgrade: 50 per cent of the purchase price, as on every other animal row.
#
# SCOPE
# Only the six horse rows on the 'Tram vehicles' sheet. The pass does not touch the
# 82 tram cars, the six steam tram engines or the one trailer.
#
# Run: py -3 wb_fv_pass57.py [--write]. Dry run by default. Idempotent (marker in the
# maintenance note and in the overhaul basis note).
import os
import sys
from openpyxl import load_workbook

MARK = 'pass 57'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv

NAMES = {
    'Clydesdale horses (pair)': 90.0,
    'Clydesdale horse': 45.0,
    'Irish draught horses (pair)': 90.0,
    'Irish draught horse': 45.0,
    'Shire horses (pair)': 90.0,
    'Shire horse': 45.0,
}

MAINT_NOTE = (
    'Maintenance decomposition (pass 57). Annual maintenance figure %s GBP per '
    'animal-year in 1900 money, from the London horse-keep accounts 1876-97 (about '
    '45 GBP an animal-year, band 28-60, excluding the horsekeeper)%s. The figure is a '
    'standing charge; a horse has no distance-based maintenance. The overhaul is the '
    'replacement of the animal at the end of its working life at 100 per cent of the '
    'purchase price, at 70,000 km: the Leeds tramway horses were renewed about once '
    'every seven years at a cost equal to the purchase price (1894-5 accounts), and '
    'seven years at the knowledge base\'s 10,000 km/yr assumption gives 70,000 km. '
    'Pass 57 restores this rule after pass 55 applied the tramcar ladder to these six '
    'rows.'
)

CAP_NOTE = (
    'horse (pass 57): the overhaul is the replacement of the animal at the end of its '
    'working life, at 100 per cent of the purchase price. The measured renewal cadence '
    'is the Leeds tramway horses, about once every seven years at a cost equal to the '
    'purchase price (1894-5 accounts); seven years at the knowledge base\'s 10,000 km/yr '
    'assumption gives 70,000 km. First and maximum are the same, so the rungs do not '
    'matter. Downtime 0.1 months. Upgrade 50 per cent of the purchase price, the share '
    'every other animal row carries. Pass 57 restores the animal rule after pass 55 '
    'applied the tramcar ladder to these six rows and pass 56 set a 22 per cent tram '
    'rebuild share.'
)


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


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    ws = wm['Tram vehicles']
    wo = wc['Overhauls & upgrades']

    cap_row = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            cap_row[str(b)] = r

    stats = {'rows': 0, 'skipped': 0, 'missing_overhaul': 0}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if name not in NAMES:
            continue
        a = NAMES[name]
        note = str(ws.cell(r, 31).value or '')
        if MARK in note and not FORCE:
            stats['skipped'] += 1
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            stats['missing_overhaul'] += 1
            continue
        capital = wo.cell(q, 13).value or 0
        if capital <= 0:
            stats['missing_overhaul'] += 1
            continue
        pair = '(pair)' in name.lower()
        note_out = MAINT_NOTE % (f2(a), ', doubled from 45 because this row is a pair' if pair else '')
        if WRITE:
            ws.cell(r, 27, round(a, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = None
            ws.cell(r, 30, 1900)
            ws.cell(r, 31, note_out + ' | ' + MARK)
            wo.cell(q, 14, round(capital, 1))
            wo.cell(q, 15, round(capital, 1))
            wo.cell(q, 16, 1)
            wo.cell(q, 17, 70000)
            wo.cell(q, 18, 0.1)
            wo.cell(q, 19, round(0.50 * capital, 1))
            wo.cell(q, 24, CAP_NOTE + ' | ' + MARK)
        stats['rows'] += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  horse rows restored: %d; already marked: %d; missing overhaul row: %d'
          % (stats['rows'], stats['skipped'], stats['missing_overhaul']))


if __name__ == '__main__':
    main()
