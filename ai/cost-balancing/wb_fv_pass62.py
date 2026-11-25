# -*- coding: utf-8 -*-
# wb_fv_pass62.py - re-base the carriage maintenance ladder on research pass 51.
#
# WHY THIS PASS EXISTS
# Pass 47 put every carriage on the measured overhaul bands and pass 60 put the standard-gauge
# rows on the class and era distance table. The annual figure A, however, still came from the
# report 43 ladder of 33 / 140 / 265 / 460 / 440 GBP a vehicle-year at 1900 / 1950 / 1970 / 1990 /
# 2020, whose 1920 and 1950 points were interpolations with no measurement behind them. Research
# pass 51 tests those points against company accounts and the Ministry of Transport's rolling-stock
# head. It finds the 1912 company mean (GBP 26.89 in 1900 money) and the measured 1913-1921 real
# change (x1.143), and derives 39 GBP a carriage-year at 1920 (band 28-55). It re-draws 1950 from
# 140 to 121 by interpolation between 39 at 1920 and the measured 183 at 1961. The 1900, 1970,
# 1990 and 2020 points stand. The 1948 and 1966 values (112 and 226) are read from the new
# interpolation.
#
# WHAT MOVES
# A, the renewals deduction, the overhaul provision, the continuous head, the first and maximum
# overhaul events and the per-km charge all move with A. The overhaul provision share, the
# interval in years, the 70/30 fixed/per-km split, the renewals treatment and the reference
# duty are unchanged. The interval in kilometres is the band's years times the row's reference
# duty from New/ai/vehicle-cost/mean-annual-distance.md, as pass 60 left it.
#
# SCOPE
# The 758 standard-gauge carriage rows carrying pass 47 and pass 60 notes on the 'Rail vehicles'
# sheet. Multiple-unit stock, tube stock, passenger-rated wagons, the narrow gauge and the
# non-carriage rows that pass 47 also touched are excluded: they belong to other class rules.
# The row's own class factor (brake 0.5, mail/TPO 0.75, BR standard 0.9 and so on) is preserved
# relative to the standard carriage ladder.
#
# Run: py -3 wb_fv_pass62.py [--write] [--force]. Dry run by default. Idempotent by the pass 62
# marker in the maintenance note.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 62'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
FIXED_SHARE = 0.70
FIRST_RATIO = 0.70
RUNGS = 3

OLD_LADDER = ((1900, 33.0), (1950, 140.0), (1970, 265.0), (1990, 460.0), (2020, 440.0))


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


def renewals(year):
    """Renewals share of the published ladder value at this introduction year, as pass 47."""
    if year <= 1961:
        return 0.35, 'Hill 1895 states that the figure is repairs and renewals'
    if year >= 1984:
        return 0.0, ('the 1984, 1990 and 2020 anchors are total-maintenance rates that exclude '
                     'the capital lease')
    r = 0.35 * (1984.0 - year) / 23.0
    return r, ('the ladder point is interpolated between the 1961 anchor, which carries '
               'provision, and the 1984 anchor, which excludes capital, so the share is phased '
               'out linearly across those 23 years')


def band_for(year):
    row = ev.CARRIAGE_OVERHAUL[0]
    for cand in ev.CARRIAGE_OVERHAUL:
        if year >= cand[0]:
            row = cand
    return row


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

    stats = {'rows': 0, 'skipped': 0, 'missing': 0, 'factor_1': 0, 'factored': 0}
    factors = {}
    samples = []
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '').strip()
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'pass 62' not in note and ('pass 47' not in note or 'pass 60' not in note):
            continue
        if MARK in note and not FORCE:
            stats['skipped'] += 1
            continue
        q = cap_row.get(str(ws.cell(r, 2).value or ''))
        if not q:
            stats['missing'] += 1
            continue
        try:
            intro = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            intro = 1900
        if MARK in note:
            mf = re.search(r'class factor of ([\d.]+) relative', note)
            factor = float(mf.group(1)) if mf else 1.0
        else:
            mA = re.search(r'Annual maintenance figure ([\d,.]+) GBP', note)
            if not mA:
                stats['missing'] += 1
                continue
            A_old = float(mA.group(1).replace(',', ''))
            old_base = ev.interp_log(OLD_LADDER, intro)
            if old_base <= 0:
                stats['missing'] += 1
                continue
            factor = round(A_old / old_base, 3)
        A = ev.interp_log(ev.CARRIAGE_MAINT_LADDER, intro) * factor
        mK = re.search(r'at mean annual distance ([\d,]+) km', note)
        if mK:
            K = float(mK.group(1).replace(',', ''))
        else:
            K = float(ev.mean_annual_km('carriage', intro) or 0)
        if K <= 0:
            stats['missing'] += 1
            continue
        _, years, _band_km, share = band_for(intro)
        km_interval = int(round(years * K))
        rs, rlabel = renewals(intro)
        rho = A * rs
        prov = share * A
        head = A - rho - prov
        emax = 2.0 * share * A * years / (1.0 + FIRST_RATIO)
        efirst = FIRST_RATIO * emax
        F = FIXED_SHARE * head
        V = (1.0 - FIXED_SHARE) * head / K
        factor_text = ''
        if abs(factor - 1.0) > 0.001:
            factor_text = (' The row keeps its class factor of %s relative to the standard '
                           'carriage ladder.' % ('%g' % factor))
            stats['factored'] += 1
            factors[factor] = factors.get(factor, 0) + 1
        else:
            stats['factor_1'] += 1
        note_out = (
            'Maintenance decomposition (pass 62, re-based on research pass 51). Annual maintenance '
            'figure %s GBP per vehicle-year in 1900 money, at mean annual distance %s km a year. '
            'Source: the rail carriage maintenance ladder at the introduction year (%d): 33 GBP at '
            '1900, 39 at 1920, 121 at 1950, 265 at 1970, 460 at 1990 and 440 at 2020, log-linear '
            'between and flat outside (research-pricing-report-43, re-based on '
            'research-pricing-report-51).%s Composition: the 1900, 1920 and 1950 rungs are treated '
            'as gross of renewals (report 51 records the 1912 figure\'s renewals treatment as the '
            'dominant uncertainty); the 1961 anchor is gross of provision; the 1984, 1990 and 2020 '
            'anchors are total-maintenance rates that exclude the capital lease. Renewals are %s '
            'per cent of this figure = %s GBP a year (%s), leaving %s GBP net. The measured total '
            'is the envelope: the works-overhaul provision of research pass 44 is %s per cent of '
            'the same figure = %s GBP a year, and the continuous head is the remainder, %s GBP a '
            'year, so the head plus the amortised events equals the net total and the overhaul '
            'does not sit on top of it. The interval is %g years, entered as %s km at the band\'s '
            'reference duty of %s km a carriage-year; the engine is distance-triggered. The mean '
            'event is %s per cent x %g years x %s = %s GBP, paid as a first overhaul of %s GBP '
            'rising to a maximum of %s GBP over %d overhauls; the smoothstep is symmetric, so '
            '(first + max)/2 is the mean and the events amortise to the provision. The continuous '
            'head is split %d/%d fixed/per-km: fixed %s GBP a year, per-km %.10f GBP per km. '
            'Pass 62 re-bases A on research pass 51: 39 at 1920 and 121 at 1950 replace the '
            'previous interpolations (59 at 1920 and 140 at 1950); 1948 reads 112 and 1966 226 '
            'by interpolation; 1900, 1970, 1990 and 2020 stand. '
            'The 1920 band is 28-55. The provision share, the interval, the renewals deduction and '
            'the 70/30 split are unchanged; A, the provision, the head and the event move '
            'together. The reference duty is from New/ai/vehicle-cost/mean-annual-distance.md.'
            % (f2(A), format(int(K), ','), intro, factor_text, f2(100.0 * rs), f2(rho), rlabel,
               f2(A - rho), f2(100.0 * share), f2(prov), f2(head), years,
               format(int(km_interval), ','), format(int(K), ','), f2(100.0 * share),
               years, f2(A), f2(prov * years), f2(efirst), f2(emax), RUNGS,
               round(FIXED_SHARE * 100), round((1 - FIXED_SHARE) * 100), f2(F), V))
        cap_note = (
            'carriage (pass 62, research passes 44 and 51): annual figure A %s GBP a vehicle-year; '
            'provision %s per cent of A at %g years; first event %s GBP, maximum %s GBP over %d '
            'overhauls; interval %s km; downtime 0.5 months. The continuous head is %s GBP, split '
            '70/30 fixed and per-km. The measured annual total is the envelope: head plus the '
            'amortised events equals A less renewals. The 1920 and 1950 rungs are re-based on '
            'research-pricing-report-51; 1900, 1970, 1990 and 2020 stand; 1948 and 1966 are read '
            'from the interpolation. | pass 47 | pass 60 | pass 62'
            % (f2(A), f2(100.0 * share), years, f2(efirst), f2(emax), RUNGS,
               format(int(km_interval), ','), f2(head)))
        if WRITE:
            ws.cell(r, 27, round(F, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(V, 10)
            ws.cell(r, 30, 1900)
            ws.cell(r, 31, note_out)
            wo.cell(q, 14, round(efirst, 1))
            wo.cell(q, 15, round(emax, 1))
            wo.cell(q, 16, RUNGS)
            wo.cell(q, 17, km_interval)
            wo.cell(q, 18, 0.5)
            wo.cell(q, 24, cap_note)
        stats['rows'] += 1
        if len(samples) < 8:
            samples.append((name, intro, A, head, efirst, emax, factor))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  carriage rows re-based: %d; already marked: %d; missing: %d; standard factor: %d; '
          'factored: %d' % (stats['rows'], stats['skipped'], stats['missing'], stats['factor_1'],
                            stats['factored']))
    print('  factors: %s' % dict(sorted(factors.items())))
    for s in samples:
        print('  %-58s intro %d A=%8.2f head=%8.2f first=%8.2f max=%8.2f factor=%g' % s)


if __name__ == '__main__':
    main()
