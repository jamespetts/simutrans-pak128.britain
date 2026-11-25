# -*- coding: utf-8 -*-
# wb_fv_pass48.py — give every narrow-gauge vehicle a divided maintenance figure: a continuous
# head AND a works-overhaul target.
#
# WHY THIS PASS EXISTS
# The generator's overhaul_profile() has no branch for the 'narrowgauge-vehicles' class, so
# build_workbooks skipped all 73 narrow-gauge vehicles: the Overhauls & upgrades sheet has no
# narrow-gauge row at all, and passes 45-47 left their measured annual total undivided (the
# carriage and wagon rows carried the whole figure as the continuous head and a note recording
# "the gap"). In game that means no overhaul cost ever, which is as wrong as double counting.
# This pass divides every one of the 73 rows and adds the overhaul targets to the sheet.
#
# THE DIVISION, by class, using the best evidence available for each:
#   carriage (34): the measured carriage total is the envelope. Works-overhaul provision
#       28 / 24 / 19 / 12 / 10 / 8 per cent of A by era at 6 / 5 / 3 / 2 / 2 / 2.6 years
#       (research pass 44 section 5), the first event 0.70 of the maximum over three. The gauge
#       is not a variable in any source: a narrow-gauge carriage is a carriage.
#   wagon (14): the measured wagon total is the envelope. Head = 0.8A, overhaul event = 1.2A
#       every six years at the 40,000 km/yr reference duty (240,000 km), first event 0.75 of the
#       steady event, two rungs (research pass 46).
#   locomotive (22): the class profile every other locomotive in the pakset carries - steam
#       5 per cent of capital first and 15 late over four events at 150,000 km (the narrow-gauge
#       archetype of research pass 40 section 1.8), diesel/electric 7 and 20 over three at
#       300,000 km. The locomotive class as a whole is still on a capital share rather than an
#       envelope; that is a fleet-wide open item, recorded in the handoff, and this pass does not
#       invent a narrow-gauge-only answer.
#   horse (3): standing rule 2 - the overhaul is the replacement at the end of the working life
#       at 100 per cent of the purchase price, at 70,000 km (the 7-year Leeds cadence at the
#       knowledge base's existing 10,000 km/yr assumption).
#   multi-part section (4): zero, like every other articulated section - the leading unit carries
#       the consist.
#
# Run: py -3 wb_fv_pass48.py [--write]. Dry run by default. Idempotent: rows carrying 'pass 48'
# are skipped. Never rebuild the workbooks.
import os
import re
import sys
from copy import copy
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

MARK = 'pass 48'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv
FIXED_SHARE = 0.70

BANDS = (
    (1890, 6.0, 210000, 0.28),
    (1923, 5.0, 180000, 0.24),
    (1948, 3.0, 165000, 0.19),
    (1975, 2.0, 176000, 0.12),
    (2000, 2.0, 240000, 0.10),
    (9999, 2.6, 294000, 0.08),
)


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
    if year <= 1961:
        return 0.35, 'Hill 1895 states that the figure is repairs and renewals'
    if year >= 1984:
        return 0.0, 'the 1984, 1990 and 2020 anchors exclude the capital lease'
    r = 0.35 * (1984.0 - year) / 23.0
    return r, ('the ladder point is interpolated between the 1961 anchor, which carries '
               'provision, and the 1984 anchor, which excludes capital, so the share is phased '
               'out linearly across those 23 years')


def band(year):
    for hi, years, km, share in BANDS:
        if year < hi:
            return years, km, share
    return BANDS[-1][1:]


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def dat_fields(key, base_name):
    """The .dat fields for this object, for the in-game columns of the overhaul sheet."""
    out = dict(cost=None, initial=None, max=None, rungs=None, km=None, months=None, upgrade=None)
    path = os.path.join(BASE, 'New', key)
    if not os.path.isfile(path):
        return out
    block = {}
    want = (base_name or '').strip().lower()
    for raw in open(path, encoding='utf-8', errors='replace'):
        line = raw.split('#', 1)[0].strip()
        if not line:
            continue
        m = re.match(r'^obj\s*=\s*(.+)$', line, re.I)
        if m:
            if block.get('name', '').lower() == want:
                break
            block = {}
            continue
        if '=' in line:
            k, v = line.split('=', 1)
            block[k.strip().lower()] = v.strip()
    if block.get('name', '').lower() != want:
        return out

    def num(name):
        try:
            return int(float(block.get(name)))
        except (TypeError, ValueError):
            return None

    for field, name in (('cost', 'cost'), ('initial', 'initial_overhaul_cost'),
                        ('max', 'max_overhaul_cost'), ('rungs', 'overhauls_before_max_cost'),
                        ('km', 'max_distance_between_overhauls'),
                        ('months', 'overhaul_month_tenths'), ('upgrade', 'upgrade_price')):
        out[field] = num(name)
    return out


def animal_bases(wm):
    """Base names the maintenance workbook marks as animals (pass 43 put them on horse-keep)."""
    out = set()
    for sheet in wm.sheetnames:
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            ae = str(ws.cell(r, 31).value or '')
            if 'per animal-year' in ae or 'horse-keep' in ae:
                out.add(str(ws.cell(r, 2).value or ''))
    return out


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    ws = wm['Narrow gauge vehicles']
    ws_cap = wc['Narrow gauge vehicles']
    wo = wc['Overhauls & upgrades']
    have = set()
    row_of = {}
    done = set()
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            have.add(str(b))
            row_of[str(b)] = r
            if 'pass 48' in str(wo.cell(r, 24).value or ''):
                done.add(str(b))
    cap = {}
    for r in range(7, ws_cap.max_row + 1):
        b = ws_cap.cell(r, 2).value
        if b:
            cap[str(b)] = ws_cap.cell(r, 22).value
    stats = {'carriage': 0, 'wagon': 0, 'locomotive': 0, 'horse': 0, 'section': 0, 'skipped': 0}
    samples = []
    problems = []
    new_rows = []
    already = 0
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        ae = str(ws.cell(r, 31).value or '')
        if MARK in ae:
            stats['skipped'] += 1
            continue
        base = str(ws.cell(r, 2).value or '')
        key = str(ws.cell(r, 3).value or '')
        if base in have and not FORCE:
            stats['skipped'] += 1
            continue
        try:
            year = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            year = 1900
        capital = float(cap.get(base) or 0)
        low = name.lower()
        mH = re.search(r'Annual maintenance figure ([\d,.]+) GBP', ae)
        A = float(mH.group(1).replace(',', '')) if mH else 0.0
        mK = re.search(r'at mean annual distance ([\d,]+) km', ae)
        K = float(mK.group(1).replace(',', '')) if mK else 40000.0
        if capital <= 0:
            kind = 'section'
        elif 'per animal-year' in ae or re.search(r'\b(horse|pony|mule)\b', low):
            kind = 'horse'
        elif 'per wagon-year' in ae:
            kind = 'wagon'
        elif 'carriage maintenance ladder' in ae:
            kind = 'carriage'
        else:
            kind = 'locomotive'
        stats[kind] += 1
        head = None      # None = leave the maintenance columns alone
        per_km = None
        if kind == 'section':
            first = mx = 0.0
            rungs, km, months, up = 0, 0, 0, 0.0
            basis = ('narrow-gauge multi-part section (pass 48): zero, like every other '
                     'articulated section - the leading unit carries the consist')
        elif kind == 'horse':
            first = mx = capital
            rungs, km, months, up = 0, 70000, 0, 0.50 * capital
            basis = ('narrow-gauge horse (pass 48): the overhaul is the replacement of the animal '
                     'at the end of its working life, at 100 per cent of the purchase price '
                     '(standing rule 2 of maintenance-decomposition.md). Life 7 years (the Leeds '
                     'renewal cadence) at the knowledge base\'s existing 10,000 km/yr assumption '
                     '= 70,000 km. First and maximum are the same, so overhauls_before_max_cost is '
                     '0. Direction: a measured annual distance for a working horse would rescale '
                     'the interval; it would not change the share.')
        elif kind == 'carriage':
            n, km, share = band(year)
            # A modern mainline duty (172,600 km a year) leaked into many narrow-gauge rows as
            # the family default. No narrow-gauge carriage ran anything like it, and the sheet's
            # own assumption for the class is 40,000 km a year, inside research pass 44's
            # measured 29,000-41,000 km a carriage-year for 1892. Normalise and say so.
            duty = ''
            if K > 60000:
                duty = (' The mean annual distance was carrying %s km, the modern mainline '
                        'carriage duty, which no narrow-gauge carriage ran; it is corrected to '
                        'the class assumption of 40,000 km a year, inside research pass 44\'s '
                        'measured 29,000-41,000 km a carriage-year in 1892.'
                        % format(int(K), ','))
                K = 40000.0
            rs, rlabel = renewals(year)
            rho = A * rs
            prov = share * A
            head = A - rho - prov
            mx = 2.0 * share * A * n / 1.70
            first = 0.70 * mx
            rungs, months, up = 3, 0.5, 0.35 * capital
            per_km = (1.0 - FIXED_SHARE) * head / K if K else 0.0
            basis = ('narrow-gauge carriage (pass 48): the measured annual carriage total is the '
                     'envelope, as on the standard gauge. The works-overhaul provision is %s per '
                     'cent of A (research pass 44 section 5: 28, 24, 19, 12, 10 and 8 per cent at '
                     '1830-89, 1890-1922, 1923-47, 1948-74, 1975-99 and 2000-26, from two measured '
                     'events), the interval %s years = %s km at the band\'s reference duty, the '
                     'first event 0.70 of the maximum over three. The gauge is not a variable in '
                     'any source, so the standard-gauge bands apply unchanged. Mean event %s GBP = '
                     'provision x interval x A. Upgrade 35 per cent of capital.'
                     % (f2(100.0 * share), ('%g' % n), format(int(km), ','), f2(prov * n)))
        elif kind == 'wagon':
            head = 0.8 * A
            per_km = None
            mx = 1.2 * A
            first = 0.75 * mx
            rungs, km, months, up = 2, 240000, 0.2, 0.35 * capital
            basis = ('narrow-gauge wagon (pass 48): the measured annual wagon total is the '
                     'envelope, as on the standard gauge. Head = 0.8A, overhaul event = 1.2A '
                     'every six years at the 40,000 km/yr reference duty (240,000 km), first event '
                     '0.75 of the steady event, two rungs (research pass 46). The 0.20 share and '
                     'the six years are an estimate; only their product is constrained. Upgrade '
                     '35 per cent of capital.')
        else:  # locomotive
            steam = year < 1950
            if steam:
                first, mx, rungs, km, months = 0.05 * capital, 0.15 * capital, 4, 150000, 1.0
                basis = ('narrow-gauge steam locomotive (pass 48): first overhaul 5 per cent of '
                         'capital, late-life 15 per cent over four events at 150,000 km - the '
                         'narrow-gauge archetype of research pass 40 section 1.8 (Festiniog '
                         'practice, 8-12 years at 120,000-180,000 km). Upgrade 35 per cent of '
                         'capital. NOTE: the locomotive class is the one rail class still on a '
                         'capital share rather than a measured envelope; that is a fleet-wide '
                         'open item, not a narrow-gauge one.')
            else:
                first, mx, rungs, km, months = 0.07 * capital, 0.20 * capital, 3, 300000, 0.8
                basis = ('narrow-gauge diesel locomotive (pass 48): first overhaul 7 per cent of '
                         'capital, late-life 20 per cent over three events at 300,000 km (BR\'s '
                         '2.75/5.5/11-year cycle), the same diesel profile as the standard gauge. '
                         'Upgrade 35 per cent of capital. NOTE: the locomotive class is the one '
                         'rail class still on a capital share rather than a measured envelope; '
                         'that is a fleet-wide open item.')
            up = 0.35 * capital
        # ---------------------------------------------------------------- maintenance sheet
        if kind == 'carriage':
            note = ('Maintenance decomposition (pass 48). Annual maintenance figure %s GBP per '
                    'vehicle-year in 1900 money, at mean annual distance %s km a year. Source: '
                    'the rail carriage maintenance ladder (research-pricing-report-43) at the '
                    'introduction year (%d). Composition: the 1900 and 1950 anchors are gross of '
                    'renewals and the 1961 anchor is gross of provision; the 1984, 1990 and 2020 '
                    'anchors exclude the capital lease. Renewals are %s per cent of this figure = '
                    '%s GBP a year (%s), leaving %s GBP net. The measured total is the envelope: '
                    'the works-overhaul provision of research pass 44 is %s per cent of the same '
                    'figure = %s GBP a year and the continuous head is the remainder, %s GBP a '
                    'year, so the head plus the amortised events equals the net total. The '
                    'interval is %s years, entered as %s km at the band\'s reference duty; the '
                    'event is %s GBP every %s years, the first at %s GBP rising to a maximum of '
                    '%s GBP over %d overhauls, a mean event of %s GBP. The overhaul target is on '
                    'the Overhauls & upgrades sheet, narrow-gauge block. The head is split %d/%d '
                    'fixed/per-km: fixed %s GBP a year, per-km %.8f GBP per km. The narrow gauge '
                    'takes the standard-gauge era bands because no source distinguishes gauge in '
                    'carriage maintenance. Direction: a company narrow-gauge carriage repair '
                    'account itemising a works overhaul would set the share directly.%s'
                    % (f2(A), format(int(K), ','), year, f2(100.0 * rs), f2(rho), rlabel,
                       f2(A - rho), f2(100.0 * share), f2(prov), f2(head), ('%g' % n),
                       format(int(km), ','), f2(mx), ('%g' % n), f2(first), f2(mx), rungs,
                       f2(prov * n), round(FIXED_SHARE * 100), round((1 - FIXED_SHARE) * 100),
                       f2(FIXED_SHARE * head), per_km, duty))
            if WRITE:
                ws.cell(r, 27, round(FIXED_SHARE * head, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = round(per_km, 8)
                ws.cell(r, 30).value = 1900
                ws.cell(r, 31, note)
        elif kind == 'wagon':
            note = ('Maintenance decomposition (pass 48). Annual maintenance figure %s GBP per '
                    'wagon-year in 1900 money, from the rail wagon ladder '
                    '(research-pricing-report-43). The measured total is the envelope: the '
                    'continuous head is 0.8 x %s = %s GBP a year, written whole in the fixed '
                    'column, and the overhaul event is 1.2 x %s = %s GBP every six years at the '
                    '40,000 km/yr reference duty (240,000 km), the first at 0.75 of that. The '
                    'overhaul target is on the Overhauls & upgrades sheet, narrow-gauge block. '
                    'The 0.20 share and the six years are an estimate; only their product is '
                    'constrained. Direction: a measured wagon overhaul invoice would set the '
                    'event directly.'
                    % (f2(A), f2(A), f2(head), f2(A), f2(mx)))
            if WRITE:
                ws.cell(r, 27, round(head, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = None
                ws.cell(r, 30).value = None
                ws.cell(r, 31, note)
        # ---------------------------------------------------------------- overhaul row
        if base in have:
            already += 1
            continue
        new_rows.append(dict(name=name, base=base, key=key, year=year, kind=kind,
                             capital=capital, first=first, mx=mx, rungs=rungs, km=km,
                             months=months, up=up, basis=basis))
        if len(samples) < 6 and kind not in [s[0] for s in samples]:
            samples.append((kind, name, A, capital, first, mx, km))
    # ---------------------------------------------------------------- the animals
    # Pass 40 profiled the animals by the sheet they sit on rather than by what they are, so
    # horses on the rail sheet took the diesel/electric locomotive ladder (7 per cent of capital
    # at 300,000 km), horses on the tram sheet the tram ladder and boat horses the ship survey.
    # Several rows also carry the wrong capital: the tram-sheet horses took the horse-drawn car's
    # 670 GBP. Standing rule 2 makes a horse's overhaul its replacement at the end of working
    # life, at 100 per cent of the purchase price, so the capital is taken from the capital
    # worksheet for the object itself and the row is rewritten to that.
    cap_by_base = {}
    for sheet in wc.sheetnames:
        if sheet in ('README', 'Index', 'Params', 'Overhauls & upgrades', 'Continuous brakes',
                     'Research prices (all passes)', 'Snippet prices (6521)', 'Engine settings'):
            continue
        w = wc[sheet]
        for r in range(7, w.max_row + 1):
            b = w.cell(r, 2).value
            if b and isinstance(w.cell(r, 22).value, (int, float)):
                cap_by_base[str(b)] = float(w.cell(r, 22).value)
    animals = animal_bases(wm)
    fixed_animals = 0
    for r in range(7, wo.max_row + 1):
        base = str(wo.cell(r, 2).value or '')
        if base not in animals:
            continue
        basis = str(wo.cell(r, 24).value or '')
        capv = cap_by_base.get(base) or float(wo.cell(r, 13).value or 0)
        if capv <= 0:
            continue
        want = (round(capv, 1), round(capv, 1), 1, 70000, 0.1, round(0.50 * capv, 1))
        cur = tuple(wo.cell(r, c).value for c in (14, 15, 16, 17, 18, 19))
        same = all(isinstance(a, (int, float)) and abs(a - b) < 0.05
                   for a, b in zip(cur, want))
        if same and basis.startswith('horse ('):
            continue
        if WRITE:
            wo.cell(r, 13, round(capv, 1))
            for c, v in zip((14, 15, 16, 17, 18, 19), want):
                wo.cell(r, c, v)
            wo.cell(r, 24, 'horse (pass 48): the overhaul is the replacement of the animal at the '
                           'end of its working life, at 100 per cent of the purchase price '
                           '(standing rule 2 of maintenance-decomposition.md). Measured renewal '
                           'cadence: the Leeds tramway horses were renewed about once every 7 '
                           'years at a cost equal to the purchase price (1894-5 accounts). Life '
                           '7 years at the knowledge base\'s existing 10,000 km/yr assumption = '
                           '70,000 km; first and maximum are the same, so the rungs do not '
                           'matter. Upgrade 50 per cent. Replaces the pass-40 sheet profile, '
                           'which gave an animal the locomotive, tram or ship overhaul, and takes '
                           'the capital from the horse breed/type ladder rather than from a '
                           'vehicle of the sheet it sits on.')
        fixed_animals += 1
    # ---------------------------------------------------------------- append the rows
    new_rows.sort(key=lambda d: d['base'].lower())
    start = wo.max_row + 1
    for i, d in enumerate(new_rows):
        r = start + i
        vals = {1: d['name'], 2: d['base'], 3: d['key'], 4: 'vehicle', 5: d['year'],
                6: 'narrowgauge-vehicles', 13: d['capital'],
                14: round(d['first'], 1), 15: round(d['mx'], 1), 16: d['rungs'],
                17: (int(d['km']) or None), 18: d['months'], 19: round(d['up'], 1),
                24: str(d['basis']) + ' | pass 48'}
        df = dat_fields(d['key'], d['base'])
        vals[7] = df['cost']
        for col, key in ((8, 'initial'), (9, 'max'), (10, 'rungs'), (11, 'km'), (12, 'months')):
            if df[key] is not None:
                vals[col] = df[key]
        if WRITE:
            for c in range(1, 25):
                cell = wo.cell(r, c)
                cell.value = vals.get(c)
                src = wo.cell(7, c)
                if src.has_style:
                    cell._style = copy(src._style)
            for c, src in ((20, 14), (21, 15)):
                wo.cell(r, c, '=IF(AND(ISNUMBER({s}{r}),ISNUMBER(Params!$B$2),'
                              'ISNUMBER(Params!$B$12)),{s}{r}/Params!$B$12/Params!$B$2,"")'
                        .format(s=get_column_letter(src), r=r))
            wo.cell(r, 22, vals[17])
            wo.cell(r, 23, '=IF(AND(ISNUMBER({s}{r}),ISNUMBER(Params!$B$2),'
                           'ISNUMBER(Params!$B$12)),{s}{r}/Params!$B$12/Params!$B$2,"")'
                    .format(s='S', r=r))
        else:
            new_rows[i]['row'] = r
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  carriage %d, wagon %d, locomotive %d, horse %d, section %d; animal rows already '
          'present %d; overhaul rows to append %d; animals repointed to the replacement rule %d'
          % (stats['carriage'], stats['wagon'], stats['locomotive'], stats['horse'],
             stats['section'], already, len(new_rows), fixed_animals))
    for s in samples:
        print('  %-10s %-50s A=%8.2f cap=%7.0f first=%8.1f max=%8.1f km=%s' % s)
    if problems:
        print('PROBLEMS:', problems[:10])
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
