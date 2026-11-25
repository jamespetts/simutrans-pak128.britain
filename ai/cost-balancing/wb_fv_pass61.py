# -*- coding: utf-8 -*-
# wb_fv_pass61.py - final tram calibration on research passes 47 and 49.
#
# WHY THIS PASS EXISTS
# Pass 58 used report 47's gross-of-renewals reading for every era. Report 49 finds that the
# 1950-1990 rung is a repairs-only head: the measured Sheffield 1949-50 repairs line is
# GBP 147.3 a car-year in 1900 money, and the accounts put renewals in a separate appropriation.
# Deducting 35 per cent renewals from the 150 GBP rung removes money the figure never contained.
# Report 49 recommends: hold A = 150 (band 130-210), renewals 0, overhaul provision 28 per cent
# at three years (mean event 0.85A), routine head 108.
# Report 49 also records the standing share of the tram routine head as 40-55 per cent. Pass 58
# used 25 per cent standing. This pass uses the 50 per cent centre of the measured band for all
# tram rows.
#
# THE RULE
#   1900-1949: A from the report 47 gross ladder; renewals 35%; overhaul provision 28% at two
#       years; first event 0.35A, maximum 0.75A over three; 96,000 km; 0.4 months.
#   1950-1989: A = 150 repairs-only; renewals 0; overhaul provision 28% at three years; first
#       event 0.54A (81), maximum 1.15A (172.5), mean 0.85A; 144,000 km; 0.5 months.
#   1990-2026: A = 1,177; renewals 0; overhaul provision 6% at twelve years; one event of 0.75A;
#       1,080,000 km; 0.8 months.
#   Every era: the continuous head is A less renewals less provision, split 50/50 standing and
#       per kilometre. At the reference duty the two charges add to the head.
#
# SCOPE
# Every non-horse row on the 'Tram vehicles' sheet with a positive capital target. The six
# horses are on the animal rule from pass 57 and are skipped; the articulated sections have a
# zero capital target and are skipped. The six steam tram engines and the one trailer take the
# tramcar rate because no separate measured rate exists and the Ministry returns count trailers
# as cars.
#
# Run: py -3 wb_fv_pass61.py [--write] [--force]. Dry run by default. Idempotent by the pass 61
# marker in the maintenance note.
import os
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 61'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
FIXED_SHARE = 0.50
HORSES = {
    'Clydesdale horses (pair)', 'Clydesdale horse',
    'Irish draught horses (pair)', 'Irish draught horse',
    'Shire horses (pair)', 'Shire horse',
}


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


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


def rule(intro):
    if intro >= 1990:
        return dict(a=1177.0, renewals=0.0, share=0.06, years=12.0, km=90000.0, rungs=1,
                    first=0.75, mx=0.75, months=0.8,
                    basis='research pass 47 modern contract; repairs-only, zero renewals')
    if intro >= 1950:
        return dict(a=150.0, renewals=0.0, share=0.28, years=3.0, km=48000.0, rungs=2,
                    first=0.54, mx=1.15, months=0.5,
                    basis='research pass 49 repairs-only rung, 0 renewals, 28 per cent at three years')
    return dict(a=ev.tram_maint(intro), renewals=0.35, share=0.28, years=2.0, km=48000.0,
                rungs=3, first=0.35, mx=0.75, months=0.4,
                basis='research pass 47 gross ladder, 35 per cent renewals, 28 per cent at two years')


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

    stats = {'rows': 0, 'skipped': 0, 'missing': 0, 'historic': 0, 'postwar': 0, 'modern': 0}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name or name in HORSES:
            continue
        note = str(ws.cell(r, 31).value or '')
        if MARK in note and not FORCE:
            stats['skipped'] += 1
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            stats['missing'] += 1
            continue
        capital = wo.cell(q, 13).value or 0
        if capital <= 0:
            stats['missing'] += 1
            continue
        try:
            intro = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            intro = 1900
        ru = rule(intro)
        a = ru['a']
        renewals = ru['renewals'] * a
        prov = ru['share'] * a
        head = a - renewals - prov
        fixed = FIXED_SHARE * head
        perkm = (1.0 - FIXED_SHARE) * head / ru['km']
        interval = int(ru['years'] * ru['km'])
        first = ru['first'] * a
        mx = ru['mx'] * a
        era = 'modern' if intro >= 1990 else ('postwar' if intro >= 1950 else 'historic')
        stats[era] += 1
        low = name.lower()
        extra = ''
        if 'engine' in low and 'tram' in low:
            extra = (' The figure is the tramcar rate; no separate measured rate for a steam '
                     'tram engine exists.')
        elif 'trailer' in low:
            extra = ' The Ministry returns count trailers as cars, so the tramcar rate applies.'
        note_out = (
            'Maintenance decomposition (pass 61, research passes 47 and 49). Annual maintenance '
            'figure %s GBP a car-year in 1900 money at %s km a year; %s. renewals %s per cent '
            '= %s GBP; works-overhaul provision %s per cent = %s GBP; the continuous head is '
            '%s GBP, split 50/50 between distance and standing: %.10f GBP a km and %s GBP a '
            'year. The overhaul event is %s to %s GBP at %s km, %d event%s to the maximum. The '
            'measured annual total is the envelope; the total charged at the reference duty is '
            '%s GBP.%s | %s'
            % (f2(a), format(int(ru['km']), ','), ru['basis'],
               f2(ru['renewals'] * 100), f2(renewals),
               f2(ru['share'] * 100), f2(prov),
               f2(head), perkm, f2(fixed),
               f2(first), f2(mx),
               format(interval, ','), ru['rungs'], '' if ru['rungs'] == 1 else 's',
               f2(head), extra, MARK))
        cap_note = (
            'tram (pass 61, research passes 47 and 49): %s. Provision %s per cent of A at %g '
            'years; first event %s GBP, maximum %s GBP over %d event%s; interval %s km; '
            'downtime %g months. The continuous head is %s GBP, split 50/50 standing and '
            'distance. The London County Council E/1 rebuild and the Supertram life extension '
            'are upgrade_price events at 22-50 per cent of the new price (pass 56). | pass 55 | '
            'pass 56 | pass 58 | pass 61'
            % (ru['basis'], format(int(ru['share'] * 100), ','), ru['years'],
               format(int(round(first)), ','), format(int(round(mx)), ','), ru['rungs'],
               '' if ru['rungs'] == 1 else 's', format(interval, ','), ru['months'],
               format(int(round(head)), ',')))
        if WRITE:
            ws.cell(r, 27, round(fixed, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(perkm, 10)
            ws.cell(r, 30, 1900)
            ws.cell(r, 31, note_out)
            wo.cell(q, 14, round(first, 1))
            wo.cell(q, 15, round(mx, 1))
            wo.cell(q, 16, ru['rungs'])
            wo.cell(q, 17, interval)
            wo.cell(q, 18, ru['months'])
            wo.cell(q, 24, cap_note)
        stats['rows'] += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  tram rows recalibrated: %d (historic %d, postwar %d, modern %d); already marked '
          '%d; missing or zero capital %d'
          % (stats['rows'], stats['historic'], stats['postwar'], stats['modern'],
             stats['skipped'], stats['missing']))


if __name__ == '__main__':
    main()
