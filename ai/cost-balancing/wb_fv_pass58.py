# -*- coding: utf-8 -*-
# wb_fv_pass58.py - recalibrate the trams to research pass 47.
#
# WHY THIS PASS EXISTS
# Pass 55 applied research pass 47's tramcar ladder, but three parts of the application do
# not match the research:
#   1. It deducted 35 per cent renewals from every era. Report 47 section 5 puts renewals at
#      35 per cent of A for the municipal series to 1990 and at zero on the modern contract,
#      because the modern Nottingham contract excludes renewal and the capital lease.
#   2. It used 48,000 km a year for the modern rows. Report 47 uses 90,000 km a year for the
#      modern contract and therefore 1,080,000 km between 12-year overhauls, not 576,000 km.
#   3. It set two overhauls to the maximum before 1950. Report 47 sets three events to the
#      maximum before 1950, two from 1950 to 1990 and one from 1990. It also sets the
#      downtime at 0.4 / 0.5 / 0.8 months, which pass 55 did not write.
#
# THE RULE (research pass 47 sections 4 and 5)
#   A = gross annual maintenance, 1900 GBP a car-year, at the reference duty:
#       84 at 1900-13, 131 at 1920, 106 at 1931, 89 at 1939, 131 at 1950, 150 at 1960-90
#       (estimate, band 120-250), and 1,177 from 1990 (2011 Nottingham contract).
#   Renewals: 35 per cent of A to 1990; zero from 1990.
#   Works-overhaul provision: 28 per cent of A at two years to 1939; 18 per cent at three
#       years from 1940 to 1990; 6 per cent at twelve years from 1990.
#   Head = A - renewals - provision, split 25 per cent standing and 75 per cent per km.
#   Event: first 0.35A rising to 0.75A over 3 events before 1950, 2 events from 1950 to
#       1990, and one event of 0.75A from 1990. Interval 96,000 / 144,000 / 1,080,000 km.
#   The reference distance is 48,000 km a car-year for the historic series and 90,000 km for
#       the modern contract.
#
# SCOPE
# Every non-horse row on the 'Tram vehicles' sheet with a positive capital target. The six
# horses are on the animal rule from pass 57 and are skipped. The articulated sections have
# a zero capital target and are skipped. The six steam tram engines and the one tram trailer
# are included: the Ministry of Transport returns count trailers as cars, and no separate
# measured tram-engine rate exists.
#
# Run: py -3 wb_fv_pass58.py [--write] [--force]. Dry run by default. Idempotent by the
# pass marker in the maintenance note; --force re-derives a marked row.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 58'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
FIXED_SHARE = 0.25
HORSES = {
    'Clydesdale horses (pair)', 'Clydesdale horse',
    'Irish draught horses (pair)', 'Irish draught horse',
    'Shire horses (pair)', 'Shire horse',
}


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


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def rule(intro):
    if intro >= 1990:
        return dict(renewals=0.0, share=0.06, years=12.0, km=90000.0, rungs=1,
                    first=0.75, mx=0.75, months=0.8)
    if intro >= 1950:
        return dict(renewals=0.35, share=0.18, years=3.0, km=48000.0, rungs=2,
                    first=0.35, mx=0.75, months=0.5)
    return dict(renewals=0.35, share=0.28, years=2.0, km=48000.0, rungs=3,
                first=0.35, mx=0.75, months=0.4)


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

    stats = {'rows': 0, 'skipped': 0, 'marked': 0, 'missing': 0,
             'historic': 0, 'postwar': 0, 'modern': 0}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name or name in HORSES:
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            stats['missing'] += 1
            continue
        capital = wo.cell(q, 13).value or 0
        if capital <= 0:
            stats['skipped'] += 1
            continue
        note = str(ws.cell(r, 31).value or '')
        if MARK in note and not FORCE:
            stats['marked'] += 1
            continue
        if 'pass 61' in note and not FORCE:
            # Pass 61 supersedes this calibration; do not overwrite it.
            stats['marked'] += 1
            continue
        try:
            intro = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            intro = 1900
        a = ev.tram_maint(intro)
        ru = rule(intro)
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
        extra = ''
        low = name.lower()
        if 'engine' in low and 'tram' in low:
            extra = (' The figure is the tramcar rate: the Ministry returns are car-only and '
                     'no separate measured rate for a steam tram engine exists.')
        elif 'trailer' in low:
            extra = (' The Ministry returns count trailers as cars, so the tramcar rate '
                     'applies to this trailer.')
        note_out = (
            'Maintenance decomposition (pass 58, research pass 47). Annual maintenance figure '
            '%s GBP a car-year gross in 1900 money at %s km a year; renewals %s per cent = '
            '%s GBP; works-overhaul provision %s per cent = %s GBP; the continuous head is '
            '%s GBP, split 75/25 between distance and standing: %.10f GBP a km and %s GBP a '
            'year. The measured annual total is the envelope. The historic series is 84 at '
            '1900-13, 131 at 1920, 106 at 1931, 89 at 1939, 131 at 1950 and 150 at 1960-90 '
            '(estimate, band 120-250); the modern value is 1,177 from the 2011 Nottingham '
            'contract at 90,000 km, with zero renewals. The overhaul event is %s to %s GBP '
            'at %s km, %d event%s to the maximum. Pass 58 corrects the modern renewals, the '
            'modern reference distance and the overhaul interval and rung count.%s | %s'
            % (f2(a), format(int(ru['km']), ','), f2(ru['renewals'] * 100), f2(renewals),
               f2(ru['share'] * 100), f2(prov), f2(head), perkm, f2(fixed),
               f2(first), f2(mx), format(interval, ','), ru['rungs'],
               '' if ru['rungs'] == 1 else 's', extra, MARK))
        cap_note = (
            'tram (pass 58, research pass 47): the gross annual ladder is the envelope. '
            'Provision 28 / 18 / 6 per cent of A at 2 / 3 / 12 years; the first event is '
            '0.35A rising to 0.75A over 3 / 2 / 1 events; renewals 35 per cent to 1990 and '
            'zero on the modern contract. The modern rows use 90,000 km a year and a '
            '1,080,000 km overhaul interval (Nottingham contract). The London County Council '
            'E/1 rebuild and the Supertram life extension are upgrade_price events at 22-50 '
            'per cent of the new price (pass 56). | pass 55 | pass 56 | pass 58')
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
            wo.cell(q, 19, round(capital * ev.tram_upgrade_share(intro), 1))
            wo.cell(q, 24, cap_note)
        stats['rows'] += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  tram rows recalibrated: %d (historic %d, postwar %d, modern %d); '
          'already marked %d; zero-capital sections skipped %d; missing overhaul row %d'
          % (stats['rows'], stats['historic'], stats['postwar'], stats['modern'],
             stats['marked'], stats['skipped'], stats['missing']))


if __name__ == '__main__':
    main()
