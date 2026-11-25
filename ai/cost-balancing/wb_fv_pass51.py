# -*- coding: utf-8 -*-
# wb_fv_pass51.py — finish the envelope: tram, water, aircraft and multiple-unit rows.
#
# WHY
# After passes 47-50 the rail carriages, wagons, locomotives, the narrow gauge and the maglev are
# on the envelope: the measured annual total is the total the engine charges, the works overhaul
# comes OUT of it, and head + amortised provision = the net total. Four groups were still charging
# a works overhaul ON TOP of a figure that already contained it:
#
#   tram   95 rows — the note deducts renewals (40 per cent) and leaves a routine remainder, then
#                    the sheet charges 10-22 per cent of capital on top: a provision of about
#                    0.67 of the net total at 48,000 km a year.
#   water 216 rows — the note says in terms "nothing is deducted and nothing is split; the figure
#                    is written whole", and the sheet nevertheless charges a 2-5 per cent survey
#                    on top: about 0.35 of the total.
#   air   230 rows — same: the 20-per-cent-of-capital engineering figure is written whole and a
#                    2.5-5 per cent C/D check is charged on top.
#   MU     20 rows — the note itself says the values "double count the overhaul events"; its own
#                    arithmetic puts the provision at GBP 80.54 against a net total of GBP 21.19.
#
# THE RULE, per group. The head is the residual, so neither the total nor the split can drift:
#   tram, water, air: keep the existing event (it is the class's measured or stated overhaul
#       evidence) and scale it so that its amortised value equals provision; head = A - renewals -
#       provision. The interval in years is the row's interval km over its mean annual distance
#       where the note states one; water uses the 5-year special survey and air the C-check
#       interval at 2,800 flight-hours a year.
#   multiple unit: research pass 45's rule replaces the event ladder — provision 15 per cent of A,
#       event 1.2A every eight years (the measured Class 158/9 C6 interval), the first at 0.70 of
#       the maximum. The maintenance LEVEL of these 20 rows is still the era-blind Hill 1892
#       carriage rate; the multiple-unit ladder of report 45 is the next pass and will re-derive
#       the head from the new A without changing this rule.
#
# Run: py -3 wb_fv_pass51.py [--write]. Dry run by default. Idempotent.
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 51'
WRITE = '--write' in sys.argv
AIR_KM_A_YEAR = 2800 * 857.0     # 2,800 flight-hours at 857 km/h, from maintenance-decomposition
WATER_YEARS = 5.0                # the five-year special survey the 575,000 km interval came from
MU_PROVISION = 0.15              # research pass 45
MU_YEARS = 8.0
MU_FIRST = 0.70


def find_base():
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(d, 'New', 'certificateless')):
            pass
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


def num(pattern, text, default=None):
    m = re.search(pattern, text)
    if not m:
        return default
    try:
        return float(m.group(1).replace(',', ''))
    except (ValueError, IndexError):
        return default


def do_row(ws, r, note, wc_row, family):
    """Return (head, per_km, first, max, years, provision, extra) or None."""
    A = num(r'Annual maintenance figure ([\d,.]+) GBP', note)
    if A is None:
        return None
    rho = 0.0
    if family == 'tram':
        rho_pct = num(r'[Rr]enewals (?:are |at )?([\d.]+) per cent', note)
        rho = (rho_pct or 0.0) / 100.0
        K = num(r'at mean annual distance ([\d,]+) km', note)
        if not K:
            K = num(r'at ([\d,]+) km a year', note)
        km = wc_row.get('km') or 0
        if not K or km <= 0:
            return None
        years = km / K
        fixed_share = num(r'split (\d+)/(\d+)', note)
        fixed_share = 0.75
        m = re.search(r'split (\d+)/(\d+)', note)
        if m:
            fixed_share = int(m.group(1)) / 100.0
    elif family == 'water':
        K = None
        years = WATER_YEARS
        fixed_share = 1.0
    elif family == 'air':
        K = None
        km = wc_row.get('km') or 0
        years = km / AIR_KM_A_YEAR if km else 2.0
        fixed_share = 1.0
    else:  # multiple unit
        rho_pct = num(r'[Rr]enewals (?:are |at )?([\d.]+) per cent', note)
        rho = (rho_pct if rho_pct is not None else 30.0) / 100.0
        K = num(r'at mean annual distance ([\d,]+) km', note)
        years = MU_YEARS
        fixed_share = 0.50
        m = re.search(r'split (\d+)/(\d+)', note)
        if m:
            fixed_share = int(m.group(1)) / 100.0
    net = A * (1.0 - rho)
    if family == 'mu':
        prov = MU_PROVISION * A
        mx = 2.0 * prov * years / (1.0 + MU_FIRST)
        first = MU_FIRST * mx
        rungs = 3
        km = (K * years) if K else None
    else:
        first0 = wc_row.get('first') or 0.0
        max0 = wc_row.get('max') or 0.0
        if max0 <= 0:
            return None
        prov = ((first0 + max0) / 2.0) / years
        mean = prov * years
        scale = mean / ((first0 + max0) / 2.0)
        first = first0 * scale
        mx = max0 * scale
        rungs = wc_row.get('rungs') or 2
        km = wc_row.get('km')
    head = net - prov
    if head <= 0:
        head = 0.10 * net
        prov = 0.90 * net
    per_km = (1.0 - fixed_share) * head / K if (K and family in ('tram', 'mu')) else None
    return dict(A=A, rho=rho, net=net, head=head, prov=prov, first=first, mx=mx, rungs=rungs,
                km=km, years=years, per_km=per_km, fixed_share=fixed_share)


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    stats = {}
    samples = []
    problems = []
    for sheet, family in (('Tram vehicles', 'tram'), ('Water vehicles', 'water'),
                          ('Air vehicles', 'air'), ('Maglev vehicles', 'skip')):
        if family == 'skip':
            continue
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            note = str(ws.cell(r, 31).value or '')
            if MARK in note:
                continue
            q = ovh.get(str(ws.cell(r, 2).value or ''))
            if not q:
                problems.append(('no overhaul row', sheet, name))
                continue
            row = dict(first=wo.cell(q, 14).value, max=wo.cell(q, 15).value,
                       rungs=wo.cell(q, 16).value, km=wo.cell(q, 17).value,
                       capital=wo.cell(q, 13).value)
            res = do_row(ws, r, note, row, family)
            if not res:
                if 'articulated tram section' in note or 'hold object' in note:
                    stats['zero'] = stats.get('zero', 0) + 1
                    continue
                if 'per animal-year' in note or 'horse-keep' in note:
                    stats['animal'] = stats.get('animal', 0) + 1
                    continue
                # Rows with no annual figure are zero-priced sections and holds: the leading
                # unit carries the consist, so the overhaul target belongs at zero too.
                if (row.get('capital') or 0) == 0 and (row.get('max') or 0) > 0:
                    if WRITE:
                        wo.cell(q, 14, 0)
                        wo.cell(q, 15, 0)
                        wo.cell(q, 16, 0)
                        wo.cell(q, 17).value = None
                        wo.cell(q, 24, str(wo.cell(q, 24).value or '') +
                                (' | pass 51: zero - the leading section carries the consist '
                                 '(zero-priced in the .dat).'))
                    stats['zero'] = stats.get('zero', 0) + 1
                else:
                    problems.append(('unparsed', sheet, name))
                continue
            add = (' | pass 51: the measured total is the envelope and the overhaul comes out of '
                   'it. Head = A - renewals (%s) - provision (%s) = %s GBP a year; the works '
                   'overhaul is %s GBP every %g years (%s km), the first at %s GBP. The split '
                   'above is superseded: charging the overhaul separately from a figure that '
                   'already contained it over-recovered by %s GBP a year.'
                   % (f2(res['A'] * res['rho']), f2(res['prov']), f2(res['head']), f2(res['mx']),
                      res['years'], format(int(res['km']), ',') if res['km'] else 'n/a',
                      f2(res['first']), f2(res['prov'])))
            stats[family] = stats.get(family, 0) + 1
            if len(samples) < 6 and family not in [s[0] for s in samples]:
                samples.append((family, name, res))
            if WRITE:
                ws.cell(r, 27, round(res['fixed_share'] * res['head'], 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = round(res['per_km'], 10) if res['per_km'] else None
                ws.cell(r, 30).value = 1900 if res['per_km'] else None
                ws.cell(r, 31, note + add)
                wo.cell(q, 14, round(res['first'], 1))
                wo.cell(q, 15, round(res['mx'], 1))
                wo.cell(q, 16, res['rungs'])
                if res['km']:
                    wo.cell(q, 17, int(round(res['km'])))
                wo.cell(q, 24, str(wo.cell(q, 24).value or '') +
                        (' | pass 51: the overhaul comes out of the measured annual total; the '
                         'events amortise to a provision of %s GBP a year, so head plus provision '
                         'equals the net total. %s'
                         % (f2(res['prov']),
                            'Multiple-unit rule of research pass 45: 15 per cent of A, event 1.2A '
                            'every eight years.' if family == 'mu' else
                            'The class event is kept and scaled to the provision.')))
    # ---------------- the 20 multiple-unit rows still on the Hill carriage rate
    ws = wm['Rail vehicles']
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'multiple-unit car ladder' not in note or MARK in note:
            continue
        q = ovh.get(str(ws.cell(r, 2).value or ''))
        if not q:
            problems.append(('no overhaul row', 'MU', name))
            continue
        row = dict(first=wo.cell(q, 14).value, max=wo.cell(q, 15).value,
                   rungs=wo.cell(q, 16).value, km=wo.cell(q, 17).value,
                   capital=wo.cell(q, 13).value)
        res = do_row(ws, r, note, row, 'mu')
        if not res:
            problems.append(('unparsed', 'MU', name))
            continue
        add = (' | pass 51: the measured total is the envelope. Head = A - renewals (%s) - '
               'provision (%s) = %s GBP a year, and the works overhaul is %s GBP every eight '
               'years, the first at %s GBP, amortising to the 15 per cent provision of research '
               'pass 45. The earlier treatment charged the overhaul on top of the same total. The '
               'maintenance LEVEL is still the era-blind Hill 1892 carriage rate; the '
               'multiple-unit ladder of report 45 replaces it in the next pass and re-derives the '
               'head without changing this rule.'
               % (f2(res['A'] * res['rho']), f2(res['prov']), f2(res['head']), f2(res['mx']),
                  f2(res['first'])))
        stats['mu'] = stats.get('mu', 0) + 1
        if WRITE:
            ws.cell(r, 27, round(res['fixed_share'] * res['head'], 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(res['per_km'], 10) if res['per_km'] else None
            ws.cell(r, 30).value = 1900 if res['per_km'] else None
            ws.cell(r, 31, note + add)
            wo.cell(q, 14, round(res['first'], 1))
            wo.cell(q, 15, round(res['mx'], 1))
            wo.cell(q, 16, res['rungs'])
            if res['km']:
                wo.cell(q, 17, int(round(res['km'])))
            wo.cell(q, 24, str(wo.cell(q, 24).value or '') +
                    (' | pass 51: multiple-unit rule of research pass 45 - the overhaul comes out '
                     'of the measured annual total; 15 per cent provision, event 1.2A every eight '
                     'years, first 0.70 of the maximum. | pass 51'))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  ' + ', '.join('%s %d' % (k, v) for k, v in sorted(stats.items())))
    for s in samples:
        r = s[2]
        print('  %-5s %-40s A=%8.1f net=%8.1f head=%8.1f prov=%8.1f event=%8.1f/%g yr'
              % (s[0], s[1][:40], r['A'], r['net'], r['head'], r['prov'], r['mx'], r['years']))
    if problems:
        print('PROBLEMS:', problems[:10])
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
