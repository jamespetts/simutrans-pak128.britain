# -*- coding: utf-8 -*-
# wb_fv_pass56.py — tram upgrade prices from the two measured rebuilds.
#
# Research pass 47 separates a works overhaul, which stays in maintenance, from a rebuild or life
# extension, which is a capital event that the engine charges through `upgrade_price`. Two rebuild
# prices are measured:
#
#   1934  London County Council E/1, rebuilt for GBP 400 against an estimated new price of
#         GBP 1,500-2,000: 20-27 per cent of the new price, central 0.22.
#   2026  Supertram life extension at GBP 856,000, 43-50 per cent of a new tram, central 0.50.
#
# The workbook currently charges 0.50 of the new price for every tram, so a 1907 tram carries the
# modern life-extension share. This pass sets the share from the measured pair: 0.22 for trams
# introduced up to 1950, rising linearly to 0.50 by 1990, and 0.50 from 1990.
#
# Run: py -3 wb_fv_pass56.py [--write]. Dry run by default. Idempotent (marker in column 24).
import os
import sys
from openpyxl import load_workbook

MARK = 'pass 56'
WRITE = '--write' in sys.argv


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
CAPW = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')


def share(year):
    if year <= 1950:
        return 0.22
    if year >= 1990:
        return 0.50
    return 0.22 + (0.50 - 0.22) * (year - 1950) / 40.0


def main():
    wc = load_workbook(CAPW, data_only=False)
    wo = wc['Overhauls & upgrades']
    done = 0
    for r in range(7, wo.max_row + 1):
        if str(wo.cell(r, 6).value) != 'tram-vehicles':
            continue
        cap = wo.cell(r, 13).value or 0
        if cap <= 0:
            continue
        basis = str(wo.cell(r, 24).value or '')
        if MARK in basis:
            continue
        try:
            year = int(str(wo.cell(r, 5).value)[:4])
        except Exception:
            year = 1900
        s = share(year)
        if WRITE:
            wo.cell(r, 19, round(s * cap, 1))
            wo.cell(r, 24, basis + (' | pass 56: upgrade_price %s of the new price, from the two '
                                    'measured tram rebuilds (research pass 47): the 1934 London '
                                    'County Council E/1 rebuild at GBP 400 against a new price of '
                                    'GBP 1,500-2,000, 0.22; the Supertram life extension at '
                                    'GBP 856,000, 0.50. A rebuild or life extension is a capital '
                                    'event and belongs here, not in the overhaul fields.'
                                    % ('0.22' if s == 0.22 else
                                       ('0.50' if s == 0.50 else format(s, '.2f')))))
        done += 1
    if WRITE:
        wc.save(CAPW)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  tram upgrade prices set from the measured rebuilds: %d' % done)


if __name__ == '__main__':
    main()
