# -*- coding: utf-8 -*-
# wb_fv_pass47.py — put the carriage works overhaul inside the measured carriage maintenance total.
#
# Pass 45 replaced the era-blind Hill 1892 carriage head with the measured ladder of research
# pass 43 (33 / 140 / 265 / 460 / 440 GBP a vehicle-year at 1900 / 1950 / 1970 / 1990 / 2020),
# deducted 35 per cent renewals and split the rest 70/30, but left the Overhauls & upgrades
# sheet's carriage events (8-27 per cent of capital) outside it. Those events come to several
# times the whole net annual total at 1900, so the in-game charge over-recovers by several times.
# Pass 46 fixed the same defect for wagons; this pass applies the same envelope rule to
# carriages, with the interval and the overhaul share of research pass 44.
#
# The identity. A is the ladder value at the row's intro year. A = renewals + overhaul provision
# + routine remainder. Head = A - renewals - provision; the events amortise to the provision, so
# head + provision = A - renewals = the net maintenance total.
#
# GROSS OR NET, and why the renewals deduction stays. Report 43's heading ("renewals excluded")
# was wrong: the 1900 and 1950 anchors are gross of renewals (Hill states "repairs and
# renewals") and the 1961 anchor is gross of "provision", while the 1984, 1990 and 2020 anchors
# are total-maintenance rates that exclude the capital lease. The 1900 anchor of 33 is also
# correct to within 3.8 per cent, because the 1892 general index is 97 (33.3 nominal = 34.3 in
# 1900 money); report 43's 42.7 came from the vehicle purchase index (1892 = 78), which
# prices.tab forbids for maintenance. The renewals share is therefore 35 per cent up to 1961 and
# phased linearly to zero by 1984, where the source definition changes. Report 44 assumed A was
# already net of renewals; that is corrected in its section 2.
#
# THE OVERHAUL SHARE AND INTERVAL are research pass 44's era table (section 5): the provision is
# a share of the published A, derived from two measured events - Lacy & Dow's GBP 62 in the
# 1860s (1.84 A) and the 1982 York Works Mk 1 overhaul at "more than GBP 2,000" (0.16 A) - and
# the interval is 6 / 5 / 3 / 2 / 2 / 2.6 years by era. The interval km is the band's reference
# distance, as report 44 recommends; the reference duty is stated in every basis.
#
# The engine's smoothstep is symmetric, so the mean event is (first + max) / 2 and the amortised
# provision is (first + max) / (2 n). Setting the provision at s x A gives
# max = 2 s n A / (1 + f), first = f x max, with f = 0.7 and 3 rungs (report 44 section 6).
#
# Run: py -3 wb_fv_pass47.py [--write]. Dry run by default. Idempotent: rows carrying 'pass 47'
# are skipped. Never rebuild the workbooks.
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 47'
WRITE = '--write' in sys.argv
FIXED_SHARE = 0.70      # fixed part of the continuous head, as pass 42/45
FIRST_RATIO = 0.70      # first event as a share of the maximum (report 44 section 6, ESTIMATE)
RUNGS = 3


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


def renewals(year):
    """Renewals share of the published ladder value at this introduction year."""
    if year <= 1961:
        return 0.35, 'Hill 1895 states that the figure is repairs and renewals'
    if year >= 1984:
        return 0.0, 'the 1984, 1990 and 2020 anchors are total-maintenance rates that exclude the capital lease'
    r = 0.35 * (1984.0 - year) / 23.0
    return r, ('the ladder point is interpolated between the 1961 anchor, which carries '
               'provision, and the 1984 anchor, which excludes capital, so the share is phased '
               'out linearly across those 23 years')


# Era bands (research pass 44 section 5): upper year exclusive, interval years, reference km,
# overhaul provision as a share of A. Report 44's grade: measured point for the 1830s-90s and
# 1948-75 bands' shares, GWR 1935 for the 1923-47 interval, interpolations elsewhere.
BANDS = (
    (1890, 6.0, 210000, 0.28),
    (1923, 5.0, 180000, 0.24),
    (1948, 3.0, 165000, 0.19),
    (1975, 2.0, 176000, 0.12),
    (2000, 2.0, 240000, 0.10),
    (9999, 2.6, 294000, 0.08),
)


def band(year):
    for hi, years, km, share in BANDS:
        if year < hi:
            return years, km, share
    return BANDS[-1][1:]


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
    stats = {'carriage': 0, 'skipped': 0, 'ng': 0}
    samples = []
    problems = []
    for sheet in ('Rail vehicles', 'Narrow gauge vehicles'):
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            ae = str(ws.cell(r, 31).value or '')
            if 'pass 45' not in ae or 'per vehicle-year' not in ae or MARK in ae:
                continue
            # Multiple-unit cars carry their own ladder and are not carriages, even where a later
            # note has left the words "per vehicle-year" in place.
            if 'multiple-unit car ladder' in ae:
                continue
            mH = re.search(r'Annual maintenance figure ([\d,.]+) GBP', ae)
            mK = re.search(r'at mean annual distance ([\d,]+) km', ae)
            try:
                year = int(str(ws.cell(r, 5).value)[:4])
            except Exception:
                year = 1900
            if not mH or not mK:
                stats['skipped'] += 1
                problems.append(('arithmetic missing', sheet, r, name))
                continue
            A = float(mH.group(1).replace(',', ''))
            K = float(mK.group(1).replace(',', ''))
            n, km, share = band(year)
            rs, rlabel = renewals(year)
            rho = A * rs
            prov = share * A
            head = A - rho - prov
            emax = 2.0 * share * A * n / (1.0 + FIRST_RATIO)
            efirst = FIRST_RATIO * emax
            F = FIXED_SHARE * head
            V = (1.0 - FIXED_SHARE) * head / K
            tag = re.search(r'the row takes ([^:]+):', ae)
            scalar = tag.group(1).strip() if tag else 'the carriage ladder'
            rec = overhaul.get(str(ws.cell(r, 2).value or ''))
            if rec is not None and 'no overhaul' in str(wo.cell(rec, 24).value or ''):
                # A hold is zero-priced and carries no overhaul (pass 40 audit). Leave it alone.
                stats['hold'] = stats.get('hold', 0) + 1
                continue
            gap = ''
            if rec is None:
                gap = (' No overhaul row exists for this class: the generator has no overhaul '
                       'profile for a narrow-gauge vehicle. The whole net total therefore stands '
                       'as the continuous head, and the split should be applied when an overhaul '
                       'row is added.')
                head, F, V = A - rho, FIXED_SHARE * (A - rho), (1.0 - FIXED_SHARE) * (A - rho) / K
                stats['ng'] += 1
            note = ('Maintenance decomposition (pass 47). Annual maintenance figure %s GBP per '
                    'vehicle-year in 1900 money, at mean annual distance %s km a year. Source: '
                    'the rail carriage maintenance ladder (research-pricing-report-43) at the '
                    'introduction year (%d): 33 GBP at 1900, 140 at 1950, 265 at 1970, 460 at '
                    '1990 and 440 at 2020, log-linear between and flat outside, taken at %s.'
                    % (f2(A), format(int(K), ','), year, scalar))
            note += (' Composition: the 1900 and 1950 anchors are gross of renewals (Hill 1895 '
                     'states "repairs and renewals") and the 1961 anchor is gross of provision; '
                     'the 1984, 1990 and 2020 anchors are total-maintenance rates that exclude '
                     'the capital lease. Renewals are %s per cent of this figure = %s GBP a year '
                     '(%s), leaving %s GBP net.'
                     % (f2(100.0 * rs), f2(rho), rlabel, f2(A - rho)))
            note += (' The measured total is the envelope: the works-overhaul provision of '
                     'research pass 44 is %s per cent of the same figure = %s GBP a year, and the '
                     'continuous head is the remainder, %s GBP a year, so the head plus the '
                     'amortised events equals the net total and the overhaul does not sit on top '
                     'of it. The interval is %s years, entered as %s km at the band\'s reference '
                     'duty of %s km a carriage-year; the engine is distance-triggered. The mean '
                     'event is %s per cent x %s years x %s = %s GBP, paid as a first overhaul of '
                     '%s GBP rising to a maximum of %s GBP over %d overhauls; the smoothstep is '
                     'symmetric, so (first + max)/2 is the mean and the events amortise to the '
                     'provision. The continuous head is split %d/%d fixed/per-km: fixed %s GBP a '
                     'year, per-km %.8f GBP per km.%s'
                     % (f2(100.0 * share), f2(prov), f2(head), ('%g' % n), format(int(km), ','),
                        format(int(round(km / n)), ','), f2(100.0 * share), ('%g' % n), f2(A),
                        f2(prov * n), f2(efirst), f2(emax), RUNGS,
                        round(FIXED_SHARE * 100), round((1 - FIXED_SHARE) * 100), f2(F), V, gap))
            note += (' This replaces the pass-45 arithmetic (a flat 35 per cent renewals '
                     'deduction and no overhaul provision) and the pass-40 overhaul events on the '
                     'Overhauls & upgrades sheet, which were a share of capital and came to '
                     'several times the whole net annual total. The provision falls across the '
                     'eras because the measured event stayed roughly flat in real money while the '
                     'annual total rose elevenfold: GBP 62 in the 1860s is 1.84 times the annual '
                     'total, GBP 2,000 in 1982 is 0.16 times. The 0.70 first-event ratio is an '
                     'estimate; only the product of the provision and the interval is constrained '
                     'by the measured figures. Direction: a Midland composite carriage price, a '
                     'GWR 1935 heavy-repair price, a BR C1 outturn price or a modern TSA schedule '
                     'separating heavy maintenance would move the provision and the head without '
                     'changing their sum.')
            stats['carriage'] += 1
            if len(samples) < 6 and (n, km, share) not in [s[7] for s in samples]:
                samples.append((sheet, r, name, A, head, emax, note, (n, km, share)))
            if WRITE:
                ws.cell(r, 27, round(F, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = round(V, 8) if V else None
                ws.cell(r, 30).value = 1900
                ws.cell(r, 31, note)
                if rec is not None:
                    wo.cell(rec, 14, round(efirst, 1))
                    wo.cell(rec, 15, round(emax, 1))
                    wo.cell(rec, 16, RUNGS)
                    wo.cell(rec, 17, int(km))
                    wo.cell(rec, 24, str(wo.cell(rec, 24).value or '') +
                            (' | pass 47: the carriage overhaul is inside the measured carriage '
                             'maintenance total. Head = A - renewals - provision and the events '
                             'amortise to the provision, with A the pass-45 ladder value at the '
                             'intro year. Provision %s per cent of A, interval %s years = %s km '
                             'at the band\'s reference duty; first event %s GBP, maximum %s GBP '
                             'over %d overhauls, mean event %s GBP. Basis: '
                             'research-pricing-report-44 section 5, research-pricing-report-43 '
                             'section 6, maintenance-decomposition.md.'
                             % (f2(100.0 * share), ('%g' % n), format(int(km), ','), f2(efirst),
                                f2(emax), RUNGS, f2(prov * n))))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  carriages %d, narrow-gauge without an overhaul row %d, holds left alone %d, '
          'skipped %d' % (stats['carriage'], stats['ng'], stats.get('hold', 0), stats['skipped']))
    for s in samples:
        print('\n--- %s r%d %s: A=%.2f head=%.2f max=%.2f' % s[:6])
        print('    ' + s[6][:2000])
    if problems:
        print('\nPROBLEMS:')
        for p in problems[:20]:
            print('   ', p)
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
