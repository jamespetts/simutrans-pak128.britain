# -*- coding: utf-8 -*-
# wb_fv_pass68.py - charge the seven pier families their measured substructure share.
#
# WHY THIS PASS EXISTS
# Research pass 13 section 6 measured the substructure share of four bridge contracts: Tower
# Bridge 15.8 per cent, the Humber 1900 worked example at a 60 ft height 25 per cent, Maynard's
# 200 ft viaduct 65.9 per cent and the same viaduct with 60 ft spans 82.3 per cent. The share
# rises with pier height and falls with span, so no single share represents every bridge. The
# visible pakset objects are low viaduct modules, and the measured low-bridge band is 13-25 per
# cent; the 111 `Piers & docks` rows have carried a blank target since the workbook was built.
#
# The 2026-11-25 decision is to charge the measured structure share. This pass applies 19 per
# cent, the midpoint of the 13-25 per cent low-bridge band, to every pier row, at the measured
# rate of the bridge family the object belongs to. The band is recorded on every row.
#
# WHAT MOVES
# The class price, class year (1900, the basis of every measured rate) and class basis of the 111
# rows. The suggested .dat columns are formulas over those three and are left as formulas, as in
# every other infrastructure row. No .dat file is changed.
#
# WHAT IS NOT CHARGED
# Maintenance: research pass 13 measures no substructure maintenance share, and the bridge
# upkeep rates are per metre of finished structure, not of substructure. The maintenance sheet's
# pier rows stay blank and the question is recorded for a decision rather than guessed here.
# The deck: a pier object is charged as the substructure component of the equivalent bridge; the
# deck and track are carried by the way object the pier supports. If the object is later shown to
# carry the deck as well, the target should rise to the whole bridge rate, not the share.
#
# FAMILY MATCH
# By the object's base name, never by the sheet: brick, stone, concrete, iron (including the L*
# girder and brickironarch names), steel and timber. The rate is the measured brick, masonry,
# concrete, iron, steel or timber bridge target in measured-infrastructure.csv, which is the same
# figure the `Bridges & viaducts` sheet uses, so the pier and the bridge cannot drift apart.
#
# Run: py -3 wb_fv_pass68.py [--write] [--force]. Dry run by default. Idempotent by the pass 68
# marker in the class basis.
import csv
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

MARK = 'pass 68'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
SHARE = 0.19
BAND = '13-25'
FAMILIES = (
    # (prefix test, family, representative bridge object, narrative)
    (lambda b: b.startswith('steel'), 'steel', 'SteelTruss', 'steel'),
    (lambda b: b.startswith('iron') or b.startswith('L') or b == 'brickironarch',
     'iron', 'IronViaduct', 'iron'),
    (lambda b: b.startswith('brick'), 'brick', 'BrickViaduct', 'brick'),
    (lambda b: b.startswith('stone'), 'stone', 'MasonryViaduct', 'stone (masonry)'),
    (lambda b: b.startswith('concrete'), 'concrete', 'ConcreteViaduct', 'concrete'),
    (lambda b: b.startswith('wood'), 'timber', 'WoodenTrestle', 'timber'),
)


def find_base():
    d = HERE
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-capital.xlsx')):
            return d
        p = os.path.dirname(d)
        if p == d:
            raise SystemExit('workspace root not found')
        d = p


BASE = find_base()
CAP = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')
MEAS = os.path.join(HERE, 'measured-infrastructure.csv')


def rates():
    out = {}
    with open(MEAS, encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['obj_type'] != 'bridge' or not r['capital_gbp']:
                continue
            out[r['name']] = (float(r['capital_gbp']), float(r['capital_dat'] or 0))
    return out


def main():
    wc = load_workbook(CAP, data_only=False)
    ws = wc['Piers & docks']
    rate = rates()
    stats = {'rows': 0, 'skipped': 0, 'unmatched': 0}
    by_family = {}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        base = str(ws.cell(r, 2).value or '').strip()
        if not name or ws.cell(r, 4).value != 'pier':
            continue
        basis = str(ws.cell(r, 24).value or '')
        if MARK in basis and not FORCE:
            stats['skipped'] += 1
            continue
        fam = None
        for test, key, rep, word in FAMILIES:
            if test(base):
                fam = (key, rep, word)
                break
        if fam is None:
            stats['unmatched'] += 1
            print('  UNMATCHED: %s (%s)' % (name, base))
            continue
        key, rep, word = fam
        gbp_km, dat = rate[rep]
        v = SHARE * gbp_km
        basis_out = (
            'pier (pass 68, research pass 13 section 6): the measured 13-25 per cent substructure '
            'share of a low bridge, applied at its midpoint 19 per cent, to the %s bridge rate of '
            'GBP %s a km at 1900 (the %s target on the Bridges & viaducts sheet). Tower Bridge '
            'measures 15.8 per cent and the Humber 1900 worked example at 60 ft 25 per cent; the '
            'share rises with pier height (Maynard 1868: 65.9 per cent at 200 ft, 82.3 per cent '
            'with 60 ft spans). The pakset records no height or span for a pier object, so the '
            'low-bridge midpoint is used and the band is stated on every row. The object is '
            'charged as the substructure component of the equivalent bridge; the deck and track '
            'are carried by the way object it supports. Maintenance is not charged: pass 13 '
            'measures no substructure maintenance share. | pass 68'
            % (word, format(int(gbp_km), ','), rep))
        if WRITE:
            ws.cell(r, 22, round(v, 2))
            ws.cell(r, 23, 1900)
            ws.cell(r, 24, basis_out)
            ws.cell(r, 33, 'pass 68: substructure share %d per cent of the %s rate (band %s per '
                           'cent); capital target only.' % (round(SHARE * 100), rep, BAND))
        stats['rows'] += 1
        by_family[key] = by_family.get(key, 0) + 1
    if WRITE:
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  pier rows charged: %d; already marked: %d; unmatched: %d'
          % (stats['rows'], stats['skipped'], stats['unmatched']))
    print('  by family: %s' % dict(sorted(by_family.items())))
    for k in sorted(by_family):
        rep = [f[2] for f in FAMILIES if f[1] == k][0]
        gbp_km, dat = rate[rep]
        print('  %-9s %3d rows  bridge %-16s GBP %9s/km -> pier GBP %9s/km -> .dat %12s'
              % (k, by_family[k], rep, format(int(gbp_km), ','), format(int(SHARE * gbp_km), ','),
                 format(int(round(SHARE * gbp_km * 100 / 0.396311)), ',')))


if __name__ == '__main__':
    main()
