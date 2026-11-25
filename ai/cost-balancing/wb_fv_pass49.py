# -*- coding: utf-8 -*-
# wb_fv_pass49.py — put the locomotive maintenance on research pass 46's dated ladder AND put the
# works overhaul inside that total.
#
# TWO DEFECTS, ONE PASS.
#
# 1. The upkeep was era-blind and double counted. Every locomotive was priced from Hill's GBP 253
#    an engine-year, which report 46 shows is the Great Western maximum, not the nineteen-company
#    average (GBP 208 18s. = GBP 215 in 1900 money), and the same Hill money was then charged a
#    second time as a per-km rate: his 2.51d. a train-mile is the annual total divided by mileage,
#    not a marginal rate. This pass reads the dated ladder and derives the per-km rate from it.
#
# 2. The works overhaul was charged ON TOP of the total. Passes 46-51 of the workbook put the
#    other classes on the envelope; the locomotives were still charging a capital-share event
#    beside the measured figure, over-recovering by up to 2.8 times. This pass applies the same
#    envelope rule.
#
# THE LADDER (research pass 46 section 5), GBP per engine-year in 1900 money:
#     1900 215 | 1950 306 | 1961 800 | 1977 2,100 | 1995 1,045 | 2020 520
# log-linear between, flat outside. A straight-electric locomotive takes 0.5 of the rung
# (Calder's Class 87 is 52 per cent of the Class 47 on the same duty); steam introduced after
# 1961 stays on the 1961 rung, because the modern fall is a property of the Class 66 generation.
#
# THE SPLIT:
#   renewals  25 per cent only where the rung is gross of them (Hill, to 1900), phased out by
#             1950 because the 1950 rung is repairs-only; the 1961 rung is gross of capital
#             provision, bounded at 22 per cent non-maintenance, so 22 per cent is deducted there
#             and phased out by 1977 where Calder's figure has capital outside.
#   overhaul  provision 35 per cent of A for steam (report 46: 30-50 per cent) and 39 per cent
#             for diesel and electric (the one independent pair, the Class 47 at 2.7 x the annual
#             total over seven years). The head is the residual.
#   fixed     steam 65/35, diesel and electric 60/40 (report 46 section 4.2). The per-km rate is
#             the variable share of the head over the row's own mean annual distance, which is
#             what removes the old double count.
#
# Run: py -3 wb_fv_pass49.py [--write] [--force]. Dry run by default. Idempotent: rows carrying
# 'pass 49' are skipped unless --force. Never rebuild the workbooks.
import math
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 49'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv

LADDER = ((1900, 215.0), (1950, 306.0), (1961, 800.0), (1977, 2100.0), (1995, 1045.0),
          (2020, 520.0))
ELECTRIC_FACTOR = 0.50
PROVISION = {'steam': 0.35, 'diesel': 0.39, 'electric': 0.39}
FIXED_SHARE = {'steam': 0.65, 'diesel': 0.60, 'electric': 0.60}


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
sys.path.insert(0, os.path.join(BASE, 'New', 'ai', 'cost-balancing'))
import evidence_data as ed


def ladder(year):
    ys = [p[0] for p in LADDER]
    if year <= ys[0]:
        return LADDER[0][1]
    if year >= ys[-1]:
        return LADDER[-1][1]
    for (y0, v0), (y1, v1) in zip(LADDER, LADDER[1:]):
        if y0 <= year <= y1:
            t = (year - y0) / float(y1 - y0)
            return math.exp(math.log(v0) + (math.log(v1) - math.log(v0)) * t)
    return LADDER[-1][1]


def renewals(year):
    """Renewals share of the published rung, by the composition of the rungs that bracket it."""
    if year <= 1900:
        return 0.25, 'Hill states repairs and renewals, so 25 per cent is deducted'
    if year <= 1950:
        r = 0.25 * (1950.0 - year) / 50.0
        return r, ('the rung is interpolated between Hill (renewals inside) and the 1950 repairs-only '
                   'figure, so the 25 per cent shares is phased out by 1950')
    if year <= 1961:
        r = 0.22 * (year - 1950.0) / 11.0
        return r, ('the 1961 Beeching rung is headed "provision, maintenance, stabling and '
                   'servicing"; its non-maintenance content is bounded at 22 per cent, deducted from '
                   '1961 and phased in from 1950')
    if year <= 1977:
        r = 0.22 * (1977.0 - year) / 16.0
        return r, ('the rung is interpolated between the 1961 rung, which carries capital '
                   'provision, and Calder 1977, which has capital outside; the 22 per cent is '
                   'phased out across those 16 years')
    return 0.0, 'the 1977 and later rungs have capital outside, so nothing is deducted'


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    specs = ed.vehicle_specs()
    stats = {'steam': 0, 'diesel': 0, 'electric': 0, 'skipped': 0, 'capped': 0}
    samples = []
    problems = []
    for sheet in ('Rail vehicles', 'Narrow gauge vehicles'):
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            ae = str(ws.cell(r, 31).value or '')
            if 'locomotive running expenses' not in ae and 'engine-year' not in ae:
                continue
            if 'per animal-year' in ae or 'horse-keep' in ae or 'multiple-unit car ladder' in ae:
                continue
            if MARK in ae and not FORCE:
                stats['skipped'] += 1
                continue
            mk = re.search(r'at mean annual distance ([\d,]+) km', ae)
            q = ovh.get(str(ws.cell(r, 2).value or ''))
            if not mk or not q:
                stats['skipped'] += 1
                problems.append(('unparsed or no overhaul row', sheet, r, name))
                continue
            K = float(mk.group(1).replace(',', ''))
            try:
                year = int(str(ws.cell(r, 5).value)[:4])
            except Exception:
                year = 1900
            base = str(ws.cell(r, 2).value or '').lower()
            eng = str((specs.get(base) or {}).get('engine') or '').lower()
            if eng not in ('steam', 'diesel', 'electric'):
                eng = 'steam' if year < 1950 else 'diesel'
            first0 = float(wo.cell(q, 14).value or 0.0)
            max0 = float(wo.cell(q, 15).value or 0.0)
            rungs = int(wo.cell(q, 16).value or 0)
            km = float(wo.cell(q, 17).value or 0.0)
            if km <= 0 or max0 <= 0 or K <= 0:
                stats['skipped'] += 1
                problems.append(('no interval or event', sheet, r, name))
                continue
            rung = 1961 if (eng == 'steam' and year > 1961) else year
            A = ladder(rung)
            if eng == 'electric':
                A *= ELECTRIC_FACTOR
            rs, rlabel = renewals(year)
            prov_share = PROVISION[eng]
            fs = FIXED_SHARE[eng]
            rho = A * rs
            prov = prov_share * A
            head = A - rho - prov
            if head < 0.10 * (A - rho):
                prov = 0.90 * (A - rho)
                head = 0.10 * (A - rho)
                stats['capped'] += 1
            years = km / K
            if eng in ('diesel', 'electric'):
                # The measured heavy event is the Class 47's "major work every seven years,
                # up to GBP 400,000" - 2.7 times its annual total. Model the heavy event itself,
                # at its measured interval, as a flat charge (rungs 0): that reproduces the
                # measured event size instead of spreading the same money over four light visits.
                years = 7.0
                km = years * K
                rungs = 0
                first = mx = prov * years
            else:
                mean_event = prov * years
                scale = mean_event / ((first0 + max0) / 2.0)
                first = first0 * scale
                mx = max0 * scale
                mean_event = (first + mx) / 2.0
            if eng in ('diesel', 'electric'):
                mean_event = (first + mx) / 2.0
            F = fs * head
            V = (1.0 - fs) * head / K
            note = ('Maintenance decomposition (pass 49). Annual maintenance figure %s GBP per '
                    'engine-year in 1900 money, at mean annual distance %s km a year, at the '
                    'introduction year (%d) of the locomotive ladder of research pass 46 section '
                    '5: 215 at 1900, 306 at 1950, 800 at 1961, 2,100 at 1977, 1,045 at 1995 and '
                    '520 at 2020, log-linear between and flat outside%s. That ladder replaces '
                    'Hill\'s GBP 253 an engine-year, which report 46 shows is the Great Western '
                    'maximum, not the nineteen-company average (GBP 208 18s. = GBP 215 in 1900 '
                    'money). Composition: the 1900 rung is Hill, repairs and renewals; the 1950 '
                    'rung is Southern Region repairs only; the 1961 rung is Beeching\'s '
                    '"provision, maintenance, stabling and servicing"; the 1977 and later rungs '
                    'have capital outside. Renewals are %s per cent = %s GBP a year (%s), leaving '
                    '%s GBP net. The measured total is the envelope: the works-overhaul provision '
                    'is %s per cent of A = %s GBP a year (report 46: 30-50 per cent for steam; 39 '
                    'per cent for diesel and electric, the Class 47 pair at 2.7 times the annual '
                    'total over seven years), and the continuous head is the remainder, %s GBP a '
                    'year, so the head plus the amortised events equals the net total. The '
                    'interval is %g years = %s km at that distance; the event is %s GBP every %g '
                    'years, the first at %s GBP rising to %s GBP over %d overhauls, a mean event '
                    'of %s GBP. The head is split %d/%d fixed/per-km at that distance: fixed %s '
                    'GBP a year, per-km %.8f GBP per km. The per-km rate is the variable share of '
                    'the head, not a separate constant: report 46 shows Hill\'s 2.51d. a train-mile '
                    'is his annual total divided by mileage, so the old 0.0067 GBP per km charged '
                    'the same money twice. Direction: a measured annual total per locomotive after '
                    '1977, a measured steam annual total, or a same-class annual-plus-overhaul '
                    'pair would move the rungs; none changes the envelope rule.'
                    % (f2(A), format(int(K), ','), year,
                       ' (a straight-electric locomotive takes half the rung: Calder\'s Class 87 '
                       'is 52 per cent of the Class 47 on the same duty)' if eng == 'electric' else '',
                       f2(100.0 * rs), f2(rho), rlabel, f2(A - rho), f2(100.0 * prov_share),
                       f2(prov), f2(head), years, format(int(km), ','), f2(mx), years, f2(first),
                       f2(mx), rungs, f2(mean_event), round(fs * 100), round((1 - fs) * 100),
                       f2(F), V))
            stats[eng] += 1
            if len(samples) < 6 and eng not in [s[0] for s in samples]:
                samples.append((eng, name, A, head, mx, years))
            if WRITE:
                ws.cell(r, 27, round(F, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = round(V, 8)
                ws.cell(r, 30).value = 1900
                ws.cell(r, 31, note)
                wo.cell(q, 14, round(first, 1))
                wo.cell(q, 15, round(mx, 1))
                wo.cell(q, 16, rungs)
                wo.cell(q, 17, int(round(km)))
                wo.cell(q, 24, ('locomotive (pass 49, research pass 46): the measured annual total '
                                'is the envelope. A = the locomotive ladder at the intro year (%s '
                                'GBP here, %s); renewals %s per cent; overhaul provision %s per '
                                'cent of A; head = the residual. The measured class interval and '
                                'rung count are kept and the events scaled to the provision, so '
                                'head plus amortised events equals the net total. The per-km '
                                'maintenance is now the variable share of the head, not a second '
                                'charge of Hill\'s total.' % (f2(A), eng, f2(100.0 * rs),
                                                              f2(100.0 * prov_share))))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  steam %d, diesel %d, electric %d; capped %d; skipped %d'
          % (stats['steam'], stats['diesel'], stats['electric'], stats['capped'],
             stats['skipped']))
    for s in samples:
        print('  %-8s %-38s A=%8.1f head=%8.1f max=%8.1f years=%.1f' % s)
    if problems:
        print('PROBLEMS:', problems[:8])
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
