# -*- coding: utf-8 -*-
# wb_fv_pass45.py — apply the rail carriage and wagon maintenance ladders of research pass 43.
#
# Research pass 43 (New/ai/cost-balancing/research-pricing-report-43.md) measured a carriage
# maintenance series and a wagon:carriage ratio that falls from 12.6 per cent (1892) to 5.4 per
# cent (1961) and is held after. It recommends:
#
#   carriage, GBP per vehicle-year in 1900 money:
#       1900 33 | 1950 140 | 1970 265 | 1990 460 | 2020 440
#   wagon, GBP per 10-tonne wagon-year in 1900 money:
#       1900 4.2 | 1950 8.7 | 1970 14.3 | 1990 24.8 | 2020 23.8
#       scaled by (payload tonnes / 10) ^ 0.4
#
# The ladders are log-linear between the points and flat outside. This pass replaces the era-blind
# Hill 1892 carriage head (32.6 GBP a vehicle-year) and the wagon 8-per-cent-of-capital rule. It
# does NOT change the overhaul shares or intervals: report 43's 30/20 per cent split is a separate
# decision, and the wagon share is under source review (wagon-overhaul-source-analysis.md).
# Carriage renewals stay at 35 per cent and the fixed/per-km split at 70/30, as in pass 42.
#
# Out of scope: multiple-unit cars (their branch must not inherit the carriage ladder), and the
# car transporters (Cartruck, Carflat, Autic, Cartic), whose payload is counted in cars, not
# tonnes, so the wagon size term cannot apply to them.
#
# Run: py -3 wb_fv_pass45.py [--write]. Dry run by default. Idempotent: rows carrying 'pass 45'
# are skipped. Never rebuild the workbooks.
import math
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 45'
WRITE = '--write' in sys.argv

CARRIAGE_MAINT = ((1900, 33.0), (1950, 140.0), (1970, 265.0), (1990, 460.0), (2020, 440.0))
WAGON_MAINT = ((1900, 4.2), (1950, 8.7), (1970, 14.3), (1990, 24.8), (2020, 23.8))
CARRIAGE_RENEWALS = 0.35
WAGON_REF_TONNES = 10.0
WAGON_SIZE_EXP = 0.4
WAGON_PER_TON = 7.07


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
sys.path.insert(0, os.path.join(BASE, 'New', 'ai', 'cost-balancing'))
import evidence_data as ed


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def ladder(points, year):
    ys = [p[0] for p in points]
    if year <= ys[0]:
        return points[0][1]
    if year >= ys[-1]:
        return points[-1][1]
    for (y0, v0), (y1, v1) in zip(points, points[1:]):
        if y0 <= year <= y1:
            t = (year - y0) / float(y1 - y0)
            return math.exp(math.log(v0) + (math.log(v1) - math.log(v0)) * t)
    return points[-1][1]


def family(ae):
    pre = ae.split(' | Maintenance decomposition')[0]
    if 'being 8 per cent of the wagon' in ae:
        return 'wagon'
    if 'multiple-unit car ladder' in pre:
        return None
    if 'Hill 1895' in ae and ('carriage' in pre.lower() or 'mail or TPO' in pre
                              or 'brake van at half' in pre or 'parcels/luggage' in pre):
        return 'carriage'
    return None


def scalar(pre):
    if 'brake van at half' in pre:
        return 0.50, 'a brake van at half the carriage ladder'
    if 'parcels/luggage van at 0.60' in pre:
        return 0.60, 'a parcels/luggage van at 0.60 of the carriage ladder'
    if 'mail or TPO vehicle at 0.75' in pre:
        return 0.75, 'a mail or TPO vehicle at 0.75 of the carriage ladder'
    return 1.0, 'the carriage ladder'


def main():
    wm = load_workbook(MAINT, data_only=False)
    specs = ed.vehicle_specs()
    stats = {'carriage': 0, 'wagon': 0, 'wagon_skip_cars': 0, 'skipped': 0}
    samples = []
    problems = []
    for sheet in ('Rail vehicles', 'Narrow gauge vehicles'):
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            ae = str(ws.cell(r, 31).value or '')
            if 'pass 42' not in ae and 'pass 43' not in ae:
                continue
            if MARK in ae:
                continue
            fam = family(ae)
            if fam is None:
                continue
            pre = ae.split(' | Maintenance decomposition')[0]
            try:
                year = int(str(ws.cell(r, 5).value)[:4])
            except Exception:
                year = 1900
            mH = re.search(r'(?:Annual maintenance figure|Head figure) ([\d,.]+) GBP', ae)
            mK = re.search(r'at (?:mean annual distance|k = ) ?([\d,]+) km', ae)
            if not mH or (fam == 'carriage' and not mK):
                stats['skipped'] += 1
                problems.append(('arithmetic missing', sheet, r, name))
                continue
            oldH = float(mH.group(1).replace(',', ''))
            K = float(mK.group(1).replace(',', '')) if mK else 0.0
            if fam == 'carriage':
                s = 0.70
                ms = re.search(r'split (\d+)/(\d+) fixed/per-km', ae)
                if ms:
                    s = int(ms.group(1)) / 100.0
                f, flabel = scalar(pre)
                pure = ladder(CARRIAGE_MAINT, year) * f
                gcls = 'narrowgauge-vehicles' if sheet == 'Narrow gauge vehicles' else 'rail-vehicles'
                try:
                    gx = ed.extrapolation(gcls, str(ws.cell(r, 2).value or ''),
                                          str(ws.cell(r, 3).value or ''), intro=year) or {}
                    ghead = gx.get('maint_gbp_yr')
                except Exception:
                    ghead = None
                adjust = ''
                if (isinstance(ghead, (int, float)) and ghead > 0
                        and 0.5 * pure < ghead < 2.0 * pure
                        and abs(ghead - pure) > 0.005 * pure):
                    head = float(ghead)
                    adjust = (' The pass-23 vehicle adjustment applies: the ladder figure is %s '
                              'GBP and the adjusted figure is %s GBP.' % (f2(pure), f2(head)))
                else:
                    head = pure
                rho = head * CARRIAGE_RENEWALS
                R = head - rho
                F = s * R
                V = (1.0 - s) * R / K
                note = ('Maintenance decomposition (pass 45). Annual maintenance figure %s GBP '
                        'per vehicle-year in 1900 money, at mean annual distance %s km a year. '
                        'Source: the rail carriage maintenance ladder '
                        '(research-pricing-report-43): 33 GBP at 1900, 140 at 1950, 265 at 1970, '
                        '460 at 1990 and 440 at 2020, log-linear between and flat outside, from '
                        'Hill 1895 (1892), the Beeching 1961 split (GBP 1,012 a coach-year), the '
                        '1984 HST train-mile evidence, the RDG 2013 rate and the ORR 2024-25 '
                        'medians. At the introduction year (%d) the ladder gives %s GBP, and the '
                        'row takes %s: %s GBP.%s Composition: Hill states the 1892 figure is '
                        '"maintenance, that is the cost of repairs and renewals", so renewals '
                        'are inside it; the works-overhaul content is unrecorded. Deducted: '
                        'renewals at 35 per cent = %s GBP a year. Routine remainder %s GBP a '
                        'year split %d/%d fixed/per-km at %s km a year: fixed %s GBP a year, '
                        'per-km %.8f GBP per km. This replaces the era-blind Hill 1892 figure of '
                        '%s GBP a year, which was applied to every era; the pass-42 treatment is '
                        'otherwise unchanged. Direction: a measured works-overhaul share would '
                        'add a deduction; a measured fixed/distance split would move the two '
                        'values without changing their sum.'
                        % (f2(head), format(int(K), ','), year, f2(ladder(CARRIAGE_MAINT, year)),
                           flabel, f2(pure), adjust, f2(rho), f2(R), round(s * 100),
                           round((1 - s) * 100), format(int(K), ','), f2(F), V, f2(oldH)))
                stats['carriage'] += 1
                if len(samples) < 5:
                    samples.append(('CARRIAGE', sheet, r, name, oldH, head, note))
                if WRITE:
                    ws.cell(r, 27, round(F, 2))
                    ws.cell(r, 28, 1900)
                    ws.cell(r, 29).value = round(V, 8)
                    ws.cell(r, 30).value = 1900
                    ws.cell(r, 31, note)
            else:
                low = name.lower()
                if any(t in low for t in ('cartruck', 'carflat', 'autic', 'cartic')):
                    stats['wagon_skip_cars'] += 1
                    continue
                sp = specs.get(str(ws.cell(r, 2).value or '').lower()) or {}
                try:
                    tons = float(sp.get('payload_sum') or sp.get('payload') or 0)
                except (TypeError, ValueError):
                    tons = 0.0
                if tons <= 0:
                    tons = oldH / (0.08 * WAGON_PER_TON)
                tons = min(max(tons, 1.0), 100.0)
                pure = ladder(WAGON_MAINT, year) * (tons / WAGON_REF_TONNES) ** WAGON_SIZE_EXP
                gcls = 'narrowgauge-vehicles' if sheet == 'Narrow gauge vehicles' else 'rail-vehicles'
                try:
                    gx = ed.extrapolation(gcls, str(ws.cell(r, 2).value or ''),
                                          str(ws.cell(r, 3).value or ''), intro=year) or {}
                    ghead = gx.get('maint_gbp_yr')
                except Exception:
                    ghead = None
                adjust = ''
                if (isinstance(ghead, (int, float)) and ghead > 0
                        and 0.5 * pure < ghead < 2.0 * pure
                        and abs(ghead - pure) > 0.005 * pure):
                    head = float(ghead)
                    adjust = (' The pass-23 vehicle adjustment applies: the ladder figure is %s '
                              'GBP and the adjusted figure is %s GBP.' % (f2(pure), f2(head)))
                else:
                    head = pure
                old_cap = oldH / 0.08 * 1.0
                note = ('Maintenance decomposition (pass 45). Annual maintenance figure %s GBP '
                        'per wagon-year in 1900 money, being the rail wagon ladder '
                        '(research-pricing-report-43) at the introduction year (%d): 4.2 GBP a '
                        '10-tonne wagon-year at 1900, 8.7 at 1950, 14.3 at 1970, 24.8 at 1990 and '
                        '23.8 at 2020, log-linear between and flat outside, scaled by '
                        '(payload/10)^0.4. This wagon is taken as %g tonnes, giving %s GBP.%s '
                        'This replaces the 8-per-cent-of-capital rule, which gave %s GBP from a '
                        'capital of about %s GBP. Composition unrecorded: no recorded source '
                        'states what the wagon maintenance figure covers, so whether renewals, '
                        'works overhauls or routine repairs alone are inside it is unknown. '
                        'Nothing is deducted and nothing is split; the figure is written whole '
                        'as the class figure. The overhaul share and interval are under source '
                        'review (New/ai/cost-balancing/wagon-overhaul-source-analysis.md); the '
                        'overhaul targets in the Overhauls & upgrades sheet are unchanged. '
                        'Direction: a wagon repair contract or a pre-1911 company wagon account '
                        'separating renewals from repairs would settle the composition; a '
                        'measured wagon overhaul invoice would settle the overhaul share.'
                        % (f2(head), year, tons, f2(pure), adjust, f2(oldH), f2(old_cap)))
                stats['wagon'] += 1
                if len(samples) < 10:
                    samples.append(('WAGON', sheet, r, name, oldH, head, note))
                if WRITE:
                    ws.cell(r, 27, round(head, 2))
                    ws.cell(r, 28, 1900)
                    ws.cell(r, 29).value = None
                    ws.cell(r, 30).value = None
                    ws.cell(r, 31, note)
    if WRITE:
        wm.save(MAINT)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    for k, v in stats.items():
        print('  %-16s %d' % (k, v))
    for s in samples:
        print('\n--- %s %s r%d %s: head %.2f -> %.2f' % (s[0], s[1], s[2], s[3], s[4], s[5]))
        print('    ' + s[6][:700])
    if problems:
        print('\nPROBLEMS:')
        for p in problems[:20]:
            print('   ', p)
    wm.close()


if __name__ == '__main__':
    main()
