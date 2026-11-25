# -*- coding: utf-8 -*-
# wb_fv_pass52.py — holds and lockers: no overhaul, nominal maintenance.
#
# A hold is a container inside a vehicle, not a vehicle in its own right: the mail locker of a
# travelling post office, the mail boot of a mail van, the mail deck of a steamer. The pakset
# prices holds at zero and lets the host vehicle carry the cost, but three rows escaped that
# treatment: the rail mail locker (GBP 24.75 a year, an artefact of the carriage ladder being
# applied to a locker), the road mail boot (GBP 2.50, from the horse-vehicle rule) and the water
# holds (already zero).
#
# Rule applied here: a hold carries NO overhaul (its host's overhauls cover it) and a nominal
# maintenance of 1 per cent of its own capital target a year, with no per-kilometre charge. The 1
# per cent is an ESTIMATE, not a measurement: it exists so the object is not free to operate, and
# it is small enough to be immaterial against the host vehicle. Zero was rejected because the
# engine then treats the hold as cost-free, and a hold is a real container that wears.
#
# Run: py -3 wb_fv_pass52.py [--write]. Dry run by default. Idempotent (marker 'pass 52').
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 52'
WRITE = '--write' in sys.argv
SHARE = 0.01


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


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    done = 0
    for sheet in wm.sheetnames:
        if 'vehicles' not in sheet.lower():
            continue
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            note = str(ws.cell(r, 31).value or '')
            key = str(ws.cell(r, 3).value or '')
            if 'boats/holds/' not in key and 'hold' not in note.lower():
                continue
            if MARK in note:
                continue
            q = ovh.get(str(ws.cell(r, 2).value))
            if not q:
                continue
            cap = wo.cell(q, 13).value or 0
            fixed = round(SHARE * cap, 2) if cap else 0.0
            already = (not ws.cell(r, 27).value and not ws.cell(r, 29).value
                       and not (wo.cell(q, 15).value or 0))
            if already:
                continue
            if WRITE:
                ws.cell(r, 27, fixed)
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = None
                ws.cell(r, 30).value = None
                ws.cell(r, 31,
                        ('Maintenance decomposition (pass 52). A hold is a container inside a '
                         'vehicle, not a vehicle in its own right, so its host carries the '
                         'overhaul and almost all of the upkeep. Maintenance is a nominal %d per '
                         'cent of the hold\'s own capital target (%s GBP) = %s GBP a year, with no '
                         'per-kilometre charge, and the overhaul target is zero. The %d per cent '
                         'is an ESTIMATE, not a measurement: it keeps the object from being free '
                         'to operate without pretending that a locker wears like a carriage. The '
                         'earlier figure came from applying a vehicle ladder to a container.')
                        % (round(SHARE * 100), format(int(cap), ','), format(fixed, ','),
                           round(SHARE * 100)))
                wo.cell(q, 14, 0)
                wo.cell(q, 15, 0)
                wo.cell(q, 16, 0)
                wo.cell(q, 17).value = None
                wo.cell(q, 24, ('hold (pass 52): no overhaul - the host vehicle carries it; '
                                'nominal maintenance of %s GBP a year = 1 per cent of the capital '
                                'target. | pass 52' % format(fixed, ',')))
            print('  %-18s r%-4d %-30s capital %8s -> fixed %s, no overhaul'
                  % (sheet, r, name[:30], cap, fixed))
            done += 1
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  holds set to nominal maintenance and no overhaul: %d' % done)


if __name__ == '__main__':
    main()
