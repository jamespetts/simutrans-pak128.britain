# -*- coding: utf-8 -*-
# wb_fv_pass55.py — trams and trailers on measured ladders, with no caps.
#
# WHY THIS PASS EXISTS
# Both classes charged a works overhaul as a share of the vehicle's purchase price, on top of an
# annual maintenance figure that was itself wrong. The overhaul then dwarfed the annual figure and
# earlier passes "fixed" it by capping the head, which hid the error. Research passes 47 (trams) and
# 48 (trailers) re-derive both figures from source and this pass applies them. No cap is used.
#
# TRAM RULE (research pass 47 section 5). Annual maintenance, gross of renewals, 1900 GBP a
# car-year at 48,000 km a year: 84 at 1900-13, 131 at 1920, 106 at 1931, 89 at 1939, 131 at 1950,
# 150 at 1960-90, 1,177 from 1990. The GBP 64 the workbook used is a NET 1930s figure (gross of a
# 38-39 per cent renewals deduction), not a gross one, and it is 25-35 per cent below the net
# 1950-90 level. Renewals 35 per cent. Works-overhaul provision: 28 per cent of gross A at a
# two-year interval to 1939; 18 per cent at three years, 1940-90; 6 per cent at twelve years from
# 1990. The event is 0.35A for the first overhaul rising to 0.75A, or 0.75A flat from 1990.
# The LCC E/1 at GBP 400 (1934) and the Supertram life extension at GBP 856,000 are rebuilds and
# belong to upgrade_price, not to the overhaul fields.
#
# TRAILER RULE (research pass 48 section 5). The annual figure for every cargo variant of one
# trailer is the highest figure that family already carries, because a trailer's upkeep does not
# fall sixfold with its cargo. The works refurbishment is about one third of the purchase price
# (TIP 2025; Cooks 1988 at GBP 4,000 against GBP 12,000) every eleven years, so its annual share is
# 3 per cent of the purchase price and comes out of the annual figure. Rows whose annual figure is
# the generator's five-per-cent allowance take the same envelope divided two parts routine work to
# three parts refurbishment. Horse-drawn trailers take a 10,000 km year and a five-year life.
#
# Run: py -3 wb_fv_pass55.py [--write]. Dry run by default. Idempotent (marker 'pass 55').
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 55'
WRITE = '--write' in sys.argv

TRAM_LADDER = ((1900, 84.0), (1914, 84.0), (1920, 131.0), (1931, 106.0), (1939, 89.0),
               (1950, 131.0), (1960, 150.0), (1990, 150.0), (1991, 1177.0), (2026, 1177.0))
TRAM_RENEWALS = 0.35
TRAILER_SHARE = 0.33
TRAILER_YEARS = 11.0
HORSE_KM = 10000.0
HORSE_YEARS = 5.0
REF_KM = 40000.0


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
CAPW = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')


def num(pattern, text, default=None):
    m = re.search(pattern, text)
    if not m:
        return default
    try:
        return float(m.group(1).replace(',', ''))
    except ValueError:
        return default


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def tram_level(year):
    if year <= TRAM_LADDER[0][0]:
        return TRAM_LADDER[0][1]
    if year >= TRAM_LADDER[-1][0]:
        return TRAM_LADDER[-1][1]
    for (y0, v0), (y1, v1) in zip(TRAM_LADDER, TRAM_LADDER[1:]):
        if y0 <= year <= y1:
            if y0 == y1:
                return v1
            t = (year - y0) / float(y1 - y0)
            return v0 + (v1 - v0) * t
    return TRAM_LADDER[-1][1]


def tram_rule(year):
    if year <= 1939:
        return 0.28, 2.0, 0.35, 0.75
    if year <= 1990:
        return 0.18, 3.0, 0.35, 0.75
    return 0.06, 12.0, 0.75, 0.75


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAPW, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    stats = {'tram': 0, 'skip_tram': 0, 'trailer': 0, 'horse': 0}

    # ------------------------------------------------------------------ trams
    ws = wm['Tram vehicles']
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name:
            continue
        note = str(ws.cell(r, 31).value or '')
        if MARK in note or 'pass 58' in note or 'pass 61' in note:
            stats['skip_tram'] += 1
            continue
        q = ovh.get(str(ws.cell(r, 2).value))
        if not q:
            continue
        capital = wo.cell(q, 13).value or 0
        if capital <= 0:
            stats['skip_tram'] += 1
            continue
        try:
            year = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            year = 1900
        A = tram_level(year)
        prov_share, years, first_share, max_share = tram_rule(year)
        rho = A * TRAM_RENEWALS
        prov = prov_share * A
        head = A - rho - prov
        fixed = 0.25 * head
        per_km = 0.75 * head / 48000.0
        note_out = ('Maintenance decomposition (pass 55). Annual maintenance figure %s GBP per '
                    'car-year in 1900 money, gross of renewals, from the tram ladder of research '
                    'pass 47 section 5 (84 at 1900-13, 131 at 1920, 106 at 1931, 89 at 1939, 131 at '
                    '1950, 150 at 1960-90 and 1,177 from 1990, per car-year at 48,000 km a year). '
                    'The GBP 64 this row carried was a NET 1930s figure, gross of a 38-39 per cent '
                    'renewals deduction, and it was 25-35 per cent below the net 1950-90 level. '
                    'Renewals are 35 per cent = %s GBP, leaving %s GBP net. The measured total is '
                    'the envelope: the works-overhaul provision is %s per cent of the gross figure '
                    '= %s GBP a year, at a %g-year interval = %s km, the event %s to %s GBP; the '
                    'head is the remainder, %s GBP a year, split 75/25 distance to standing: '
                    '%.8f GBP a km and %s GBP a year. No cap is used. The rebuild events recorded '
                    'for the LCC E/1 (GBP 400, 1934) and Supertram (GBP 856,000) are life '
                    'extensions and belong to upgrade_price, not here. Direction: a measured '
                    'municipal tramcar maintenance figure for 1950-90 would replace the estimate '
                    'at those rungs.'
                    % (f2(A), f2(rho), f2(A - rho), f2(100 * prov_share), f2(prov), years,
                       format(int(years * 48000), ','), f2(first_share * A), f2(max_share * A),
                       f2(head), per_km, f2(fixed)))
        if WRITE:
            ws.cell(r, 27, round(fixed, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(per_km, 10)
            ws.cell(r, 30).value = 1900
            ws.cell(r, 31, note_out)
            wo.cell(q, 14, round(first_share * A, 1))
            wo.cell(q, 15, round(max_share * A, 1))
            wo.cell(q, 16, 1 if first_share == max_share else 2)
            wo.cell(q, 17, int(years * 48000))
            wo.cell(q, 24, ('tram (pass 55, research pass 47): the gross annual ladder is the '
                            'envelope. Provision %s per cent of the gross figure at %g years; the '
                            'event is %s to %s GBP. Rebuilds such as the E/1 and Supertram life '
                            'extension belong to upgrade_price. | pass 55'
                            % (f2(100 * prov_share), years, f2(first_share * A),
                               f2(max_share * A))))
        stats['tram'] += 1

    # ------------------------------------------------------------------ trailers
    ws = wm['Road vehicles']
    fam_A = {}
    fam_rows = []
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name or 'trailer' not in name.lower():
            continue
        note = str(ws.cell(r, 31).value or '')
        if MARK in note:
            continue
        q = ovh.get(str(ws.cell(r, 2).value))
        if not q:
            continue
        a = num(r'Annual maintenance figure ([\d,.]+) GBP', note)
        capital = wo.cell(q, 13).value or 0
        if not a or not capital:
            continue
        fam = name.split('(')[0].strip().lower()
        fam_rows.append((r, q, name, note, a, capital, fam))
        fam_A[fam] = max(fam_A.get(fam, 0.0), a)
    for r, q, name, note, a, capital, fam in fam_rows:
        try:
            year = int(str(ws.cell(r, 5).value)[:4])
        except Exception:
            year = 1900
        horse = year < 1900
        cart_rule = abs(a / capital - 0.05) < 0.004
        if cart_rule:
            A = a
            prov = 0.60 * A
        else:
            A = fam_A[fam]
            prov = TRAILER_SHARE * capital / TRAILER_YEARS
            if prov >= 0.95 * A:
                prov = 0.95 * A
        head = A - prov
        years = HORSE_YEARS if horse else TRAILER_YEARS
        event = prov * years
        km = HORSE_KM if horse else REF_KM
        interval_km = int(years * km)
        K = HORSE_KM if horse else REF_KM
        fixed = 0.25 * head
        per_km = 0.75 * head / K
        note_out = ('Maintenance decomposition (pass 55). Annual maintenance figure %s GBP per '
                    'vehicle-year in 1900 money, at %s km a year. %s The measured total is the '
                    'envelope: the works refurbishment is %s GBP every %g years at that duty, its '
                    'annual share %s GBP coming out of the figure, so the head is %s GBP a year, '
                    'split 75/25 distance to standing: %.8f GBP a km and %s GBP a year. No cap is '
                    'used. Research passes 48 and 47.'
                    % (f2(A), format(int(K), ','),
                       ('The figure is the full Freight Transport Association trailer line; every '
                        'cargo variant of this trailer takes the same line, because a trailer\'s '
                        'upkeep does not vary with what it carries.'
                        if not cart_rule else
                        'The figure is the generator\'s allowance of 5 per cent of the purchase '
                        'price a year, divided two parts routine work to three parts '
                        'refurbishment.'),
                       f2(event), years, f2(prov), f2(head), per_km, f2(fixed)))
        if WRITE:
            ws.cell(r, 27, round(fixed, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(per_km, 10)
            ws.cell(r, 30).value = 1900
            ws.cell(r, 31, note_out)
            wo.cell(q, 14, round(event, 1))
            wo.cell(q, 15, round(event, 1))
            wo.cell(q, 16, 1)
            wo.cell(q, 17, interval_km)
            wo.cell(q, 24, ('trailer (pass 55, research pass 48): the annual figure is the '
                            'envelope. Refurbishment 0.33 of the purchase price at eleven years '
                            'for a motor trailer, or the five-year horse-trailer cycle; its '
                            'annual share comes out of the figure. | pass 55'))
        if horse:
            stats['horse'] += 1
        else:
            stats['trailer'] += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAPW)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  tram rows rewritten %d, zero-priced sections left alone %d; trailer rows %d '
          '(horse-drawn %d)' % (stats['tram'], stats['skip_tram'], stats['trailer'],
                                stats['horse']))


if __name__ == '__main__':
    main()
