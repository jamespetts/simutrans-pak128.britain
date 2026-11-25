# -*- coding: utf-8 -*-
# wb_fv_pass63.py - apply research pass 50 to the locomotive rows.
#
# WHY THIS PASS EXISTS
# Pass 49 put the locomotives on the report 46 ladder and inside the measured-total envelope.
# Research pass 50 closes the two gaps that pass left: a measured annual level for 1914-1948 and
# a measured modern electric passenger locomotive. It finds that the 1913-1938 Railway Returns
# points validate the 1900-1950 interpolation within 5 per cent, so no 1922 rung is added; that
# the series changes composition at 1950 (the pre-1950 rungs are gross of renewals, the 1950 rung
# is Southern Region repairs only and net); and that the 2018 Alstom/GB Railfreight Class 92
# full-maintenance contract is a measured GBP 868 an engine-year in 1900 money (band 740-1,000).
# The 2020 rung of 520 remains the Class 66 freight-diesel line; the Class 92 is a class override,
# not a new time rung.
#
# WHAT MOVES
# The BR Class 92 row only: A changes from the ladder value at its 1994 introduction (543.16) to
# the measured class level of 868, and the provision, head, per-km charge and overhaul event are
# recomputed with the existing diesel/electric rules (renewals 0, provision 39 per cent of A,
# 60/40 fixed/per-km, seven-year heavy-event interval). Every other locomotive row keeps its
# arithmetic; its maintenance and capital notes gain the report 50 composition and validation
# statement.
#
# SCOPE
# The 423 locomotive rows carrying pass 49 notes on the 'Rail vehicles' sheet. Multiple-unit,
# carriage, wagon, animal and narrow-gauge rows are excluded by the note test.
#
# Run: py -3 wb_fv_pass63.py [--write]. Dry run by default. Idempotent by the pass 63 marker.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 63'
WRITE = '--write' in sys.argv
PROVISION = 0.39
FIXED_SHARE = 0.60
YEARS = 7.0


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


def report50_text():
    return ('pass 63 (research pass 50): the measured 1913-1938 Railway Returns points validate '
            'the 1900-1950 interpolation within 5 per cent; no 1922 rung is added. The series '
            'changes composition at 1950: the pre-1950 rungs are gross of renewals and the 1950 '
            'rung is repairs-only and net. The 25 per cent renewals share is phased out by 1950, '
            'so the 1950 rung is entered net at 306. The 2018 Class 92 measured level of 868 GBP '
            'is a class override, not a time rung; the 2020 rung of 520 remains the Class 66 '
            'freight-diesel line.')


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    ws = wm['Rail vehicles']
    wo = wc['Overhauls & upgrades']
    cap_row = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            cap_row[str(b)] = r

    stats = {'notes': 0, 'c92': 0, 'skipped': 0, 'missing': 0}
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'engine-year' not in note or 'pass 49' not in note:
            continue
        if 'per animal-year' in note or 'multiple-unit car ladder' in note:
            continue
        if MARK in note:
            stats['skipped'] += 1
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            stats['missing'] += 1
            continue
        mK = re.search(r'at mean annual distance ([\d,]+) km', note)
        if not mK:
            stats['missing'] += 1
            continue
        K = float(mK.group(1).replace(',', ''))
        if name == 'BR Class 92':
            A = 868.0
            rho = 0.0
            prov = PROVISION * A
            head = A - rho - prov
            F = FIXED_SHARE * head
            V = (1.0 - FIXED_SHARE) * head / K
            km = int(round(YEARS * K))
            event = prov * YEARS
            note_out = (
                'Maintenance decomposition (pass 63, research pass 50). Annual maintenance figure '
                '%s GBP per engine-year in 1900 money, at mean annual distance %s km a year. This '
                'is the measured Class 92 full-maintenance contract, not a rung of the locomotive '
                'ladder: Alstom and GB Railfreight announced on 17 April 2018 a contract worth '
                'about GBP 15 million over 12 years for 12 Class 92 locomotives, or GBP 104,167 a '
                'locomotive-year at 2018 prices, GBP 868 in 1900 money at the general index 11,999 '
                '(band 740-1,000). The 12-year term contains the heavy events, so the measured '
                'total is the envelope. The time ladder\'s 2018 interpolation is 550 and its 2020 '
                'rung of 520 remains the Class 66 freight-diesel line; this override is a class '
                'figure, not a new time rung. Composition: the 1900 rung is Hill, repairs and '
                'renewals; the pre-1950 rungs are gross of renewals; the 1950 rung is Southern '
                'Region repairs only and net; the 1961 rung is Beeching\'s "provision, maintenance, '
                'stabling and servicing"; the 1977 and later rungs have capital outside. The '
                'measured 1913-1938 points validate the 1900-1950 interpolation within 5 per cent, '
                'so no 1922 rung is added. Renewals are 0 per cent = 0 GBP a year (the 1977 and '
                'later rungs have capital outside, so nothing is deducted), leaving %s GBP net. '
                'The measured total is the envelope: the works-overhaul provision is %s per cent '
                'of A = %s GBP a year (the diesel/electric rule from the Class 47 pair; the '
                'contract does not itemise the heavy/routine split), and the continuous head is '
                'the remainder, %s GBP a year, so the head plus the amortised events equals the '
                'net total. The interval is %g years = %s km at that distance (the diesel/electric '
                'heavy-event interval; the 12-year contract term contains the heavy events, and '
                'the seven-year interval is the class rule); the event is %s GBP every %g years, '
                'the first at %s GBP rising to %s GBP over 0 overhauls, a mean event of %s GBP. '
                'The head is split %d/%d fixed/per-km at that distance: fixed %s GBP a year, '
                'per-km %.10f GBP per km. The per-km rate is the variable share of the head, not '
                'a separate constant. | pass 49 | pass 63'
                % (f2(A), format(int(K), ','), f2(A), f2(100.0 * PROVISION), f2(prov), f2(head),
                   YEARS, format(km, ','), f2(event), YEARS, f2(event), f2(event), f2(event),
                   round(FIXED_SHARE * 100), round((1 - FIXED_SHARE) * 100), f2(F), V))
            cap_note = (
                'locomotive (pass 63, research passes 46 and 50): the measured annual total is '
                'the envelope. The Class 92 is a class override at %s GBP an engine-year, from the '
                '2018 Alstom/GB Railfreight full-maintenance contract (about GBP 15m over 12 years '
                'for 12 locomotives, GBP 104,167 a locomotive-year, GBP 868 in 1900 money; band '
                '740-1,000). It is not a time rung: the ladder\'s 2018 interpolation is 550 and the '
                '2020 rung of 520 remains the Class 66 freight-diesel line. Renewals 0; overhaul '
                'provision %s per cent of A; head = the residual. The interval is %g years = %s '
                'km; first and maximum event %s GBP, flat (one event to the maximum). The 12-year '
                'contract term contains the heavy events. The composition break at 1950 and the '
                '1913-1938 validation are stated in the maintenance note. | pass 49 | pass 63'
                % (f2(A), f2(100.0 * PROVISION), YEARS, format(km, ','), f2(event)))
            if WRITE:
                ws.cell(r, 27, round(F, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = round(V, 10)
                ws.cell(r, 30, 1900)
                ws.cell(r, 31, note_out)
                wo.cell(q, 14, round(event, 1))
                wo.cell(q, 15, round(event, 1))
                wo.cell(q, 16, 0)
                wo.cell(q, 17, km)
                wo.cell(q, 24, cap_note)
            stats['c92'] += 1
            print('  Class 92: A=%s head=%s event=%s km=%s' % (f2(A), f2(head), f2(event),
                                                               format(km, ',')))
            continue
        suffix = ' | ' + report50_text()
        if WRITE:
            ws.cell(r, 31, note + suffix)
            wo.cell(q, 24, str(wo.cell(q, 24).value or '') + suffix)
        stats['notes'] += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  locomotive notes updated: %d; Class 92 overrides: %d; already marked: %d; missing: %d'
          % (stats['notes'], stats['c92'], stats['skipped'], stats['missing']))


if __name__ == '__main__':
    main()
