# -*- coding: utf-8 -*-
# wb_fv_pass46.py — put the wagon overhaul back inside the measured wagon maintenance total.
#
# Pass 45 replaced the 8-per-cent-of-capital wagon head with the measured ladder but wrote the
# whole ladder value as continuous maintenance and left the overhaul events outside it, so the
# in-game total over-recovered by the event. The source analysis
# (New/ai/cost-balancing/wagon-overhaul-source-analysis.md) shows why the old 8-20 per cent band
# and the 20-per-cent share did not meet:
#
#   - report 36's 8-20 per cent is a share of *capital per event*, not of the annual total;
#   - report 43's "2 per cent of capital" divided a 10-tonne wagon's annual figure by a 100-tonne
#     wagon's capital; matched, the event is 20.2 per cent at 10 tonnes and 5.1 per cent at 100;
#   - the 8-20 per cent came from BR's condemnation/repair-limit rule, which is replacement logic,
#     not a recurring overhaul;
#   - report 43 wrote a year count (3) into a km field; 240,000 km is six years only at the
#     40,000 km/yr reference duty.
#
# The reconciliation: keep the measured total A as the envelope. Head = (1 - s)A, overhaul event =
# s x n x A, with s = 0.20 and n = 6 years (240,000 km at 40,000 km/yr). At 1900 that is an event
# of 1.2A = GBP 5.04 on a GBP 70.7 wagon, 7.1 per cent of capital; a 2020 100-tonne hopper gives
# 1.2 x 59.7 = GBP 71.6, 10.1 per cent. Both sit at the bottom of report 36's 8-20 per cent band
# and inside report 40's 10-15 per cent, and the head plus the annualised event equals A.
#
# The first overhaul is set at 0.75 of the steady event, the max at the steady event, with two
# rungs. s = 0.20 and n = 6 are an estimate (only their product is constrained); the basis says so.
#
# Run: py -3 wb_fv_pass46.py [--write]. Dry run by default. Idempotent: rows carrying 'pass 46'
# are skipped. Never rebuild the workbooks.
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 46'
WRITE = '--write' in sys.argv
SHARE = 0.20
YEARS = 6
REF_KM = 40000.0
INTERVAL_KM = YEARS * REF_KM     # 240,000 km at the 40,000 km/yr reference duty


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
    wo = wc['Overhauls & upgrades']
    overhaul = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            overhaul[str(b)] = r
    stats = {'wagon': 0, 'skipped': 0}
    samples = []
    problems = []
    for sheet in ('Rail vehicles', 'Narrow gauge vehicles'):
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            ae = str(ws.cell(r, 31).value or '')
            if 'pass 45' not in ae or 'per wagon-year' not in ae or MARK in ae:
                continue
            mH = re.search(r'Annual maintenance figure ([\d,.]+) GBP', ae)
            rec = overhaul.get(str(ws.cell(r, 2).value or ''))
            if not mH:
                stats['skipped'] += 1
                problems.append(('missing head', sheet, r, name))
                continue
            if rec is None:
                # No overhaul row exists for this class (the generator has no narrow-gauge
                # overhaul profile), so the event cannot be separated. Keep the whole measured
                # total as the head and record the gap rather than under-recover silently.
                A = float(mH.group(1).replace(',', ''))
                note = ('Maintenance decomposition (pass 46). Annual maintenance figure %s GBP per '
                        'wagon-year in 1900 money, the measured wagon ladder of pass 45. The '
                        'overhaul event cannot be separated from this figure because the '
                        'Overhauls & upgrades sheet has no row for a narrow-gauge vehicle: the '
                        'generator has no overhaul profile for that class. The whole measured '
                        'total therefore stands as the continuous head. When an overhaul row is '
                        'added, the split should be head = 0.8A and event = 1.2A every six years '
                        'at the reference duty, as on the standard-gauge wagons. Source analysis: '
                        'New/ai/cost-balancing/wagon-overhaul-source-analysis.md.'
                        % f2(A))
                stats['skipped'] += 1
                problems.append(('no overhaul row; total kept whole', sheet, r, name))
                if WRITE:
                    ws.cell(r, 31, note)
                continue
            A = float(mH.group(1).replace(',', ''))
            head = (1.0 - SHARE) * A
            event = SHARE * YEARS * A
            first = 0.75 * event
            note = ('Maintenance decomposition (pass 46). Annual maintenance figure %s GBP per '
                    'wagon-year in 1900 money, being the measured wagon ladder of pass 45 '
                    '(research-pricing-report-43) after the pass-23 adjustment. The measured '
                    'total is the envelope: the continuous head is (1 - 0.20) x %s = %s GBP, and '
                    'the heavy overhaul is 0.20 x 6 x %s = %s GBP every six years at the 40,000 '
                    'km/yr reference duty (240,000 km); the first event is 0.75 of that, %s GBP, '
                    'and the maximum is the steady event. The event is 7.1 per cent of a 1900 '
                    '10-tonne wagon\'s capital and 10.1 per cent of a 2020 100-tonne hopper\'s, '
                    'inside report 36\'s 8-20 per cent per-event band and report 40\'s 10-15 per '
                    'cent, at the bottom. The 8-20 per cent is a share of capital per event, not '
                    'an annual share; the old 20-per-cent-of-capital-at-three-years reading would '
                    'have been 6.7 per cent of capital a year, more than the whole measured total. '
                    'The 0.20 share and the six-year interval are an estimate; only their product '
                    'is constrained by the sources. Source analysis: '
                    'New/ai/cost-balancing/wagon-overhaul-source-analysis.md. Direction: a measured '
                    'wagon overhaul invoice or the 1947 BR repair regulation would set the event '
                    'directly; a measured wagon duty would replace the 40,000 km/yr reference.'
                    % (f2(A), f2(A), f2(head), f2(A), f2(event), f2(first)))
            stats['wagon'] += 1
            if len(samples) < 4:
                samples.append((sheet, r, name, A, head, event, first, note))
            if WRITE:
                ws.cell(r, 27, round(head, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = None
                ws.cell(r, 30).value = None
                ws.cell(r, 31, note)
                wo.cell(rec, 14, round(first, 1))
                wo.cell(rec, 15, round(event, 1))
                wo.cell(rec, 16, 2)
                wo.cell(rec, 17, int(INTERVAL_KM))
                wo.cell(rec, 24, str(wo.cell(rec, 24).value or '') +
                        (' | pass 46: the wagon overhaul is inside the measured total. Head = 0.8A '
                         'and event = 1.2A, with A the measured wagon-year figure of pass 45; the '
                         'event is every 6 years at the 40,000 km/yr reference duty (240,000 km), '
                         'first event 0.75 of the steady event, max the steady event, two rungs. '
                         'The 0.20 share and 6 years are an estimate; their product is what the '
                         'sources constrain. Basis: wagon-overhaul-source-analysis.md.'))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  wagons %d, skipped %d' % (stats['wagon'], stats['skipped']))
    for s in samples:
        print('\n--- %s r%d %s: A=%.2f head=%.2f event=%.2f first=%.2f' % s[:7])
        print('    ' + s[7][:500])
    if problems:
        print('\nPROBLEMS:')
        for p in problems:
            print('   ', p)
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
