# -*- coding: utf-8 -*-
# wb_fv_pass43.py — remedy three evidenced defects in the two cost-balancing workbooks.
#
#   1. ANIMALS. Horses, ponies, mules and donkeys on the rail, narrow-gauge, tram and water
#      sheets were priced from the sheet's class ladder (a steam locomotive's 253 GBP/engine-year,
#      a tram car's 64 GBP/car-year, a ship's 2 per cent of capital) and given a per-km charge.
#      The generator's horse clause sits after the class dispatch, so it only ever reached the
#      road sheet. Every animal now takes the London horse-keep figure: 45 GBP an animal-year
#      (band 28-60), standing only, doubled for a pair. Its capital becomes the horse breed/type
#      ladder instead of the tram car / locomotive / ship figure.
#
#   2. MAGLEV. All 22 maglev vehicles carried the Hill 1895 steam locomotive maintenance figure
#      (253 GBP/engine-year) and a per-km charge, and the capital came from the diesel/electric
#      locomotive ladder. There are no mainline maglevs in Britain, so (user direction) maglev
#      prices use overseas maglev system costs adjusted for labour. The figures are the
#      Almujibah and Preston (2018) unit costs from the Shanghai, Linimo, Incheon and Changsha
#      systems: EUR 49,233 a seat to acquire and EUR 0.011 a seat-km to maintain, at 2009 prices.
#      They are converted at EUR 1 = GBP 0.89, deflated on the workbook's own index (vehicle
#      purchase 8,287 and general 9,163 in 2009), adjusted for labour (x0.96 for Germany, the
#      source country, at a 25 per cent labour share; research-pricing-report-17 section 5).
#      Non-passenger stock has no seat count, so the same rate is applied per metre of length,
#      using the 14 m / 54-seat reference car. The maintenance figure is a per-seat-km unit cost,
#      so it is wholly a per-km charge: no decomposition, no fixed charge.
#
#   3. ROAD BUSES AND COACHES. The pass-42 treatment deducted the annualised overhaul provision
#      from the Commercial Motor maintenance total. That provision is an estimate from capital
#      shares; on 235 road rows it exceeded the whole measured total, and on the pre-1930 and
#      modern bus bands it consumed almost all of it (Leyland Tiger PS2/13: head 108.4 GBP/yr,
#      provision 106.1, routine remainder 2.28). The one measured composition of that total is
#      the 1947 Commercial Motor fleet account: twelve 32-seat coaches, GBP 426.7 a vehicle-year,
#      of which engine reconditioning (GBP 120) and body overhaul (GBP 200) on alternate years
#      are GBP 160, or 37.5 per cent (research-pricing-report-31). Where the capital-share
#      estimate exceeds 37.5 per cent of the head, the provision is rescaled to 37.5 per cent,
#      the routine remainder becomes 62.5 per cent, and the overhaul targets in the capital
#      workbook are rescaled to the same figure. Where the estimate is already at or below
#      37.5 per cent it is left alone: it is a specific figure and the measured composition does
#      not contradict it. Lorries and trailers are not changed: their provisions mostly fit
#      inside the head already, so the data do not contradict the algorithm for them.
#
# Run: py -3 wb_fv_pass43.py [--write]. Dry run by default. Idempotent: rows carrying
# 'pass 43' are skipped. Never rebuild the workbooks.
import os
import re
import sys
from openpyxl import load_workbook

MARK = 'pass 43'
WRITE = '--write' in sys.argv

# ---------------------------------------------------------------- evidence constants
HORSE_KEEP_YR = 45.0
HORSE_PRICE = {
    'pony': 25.0, 'hackney': 55.0, 'freisian': 120.0, 'friesian': 120.0,
    'cleveland': 90.0, 'yorkshire': 90.0, 'irish': 135.0, 'clydesdale': 175.0,
    'shire': 180.0, 'heavy': 135.0, 'coach': 90.0, 'cart': 60.0, 'dray': 60.0,
}
HORSE_DEFAULT = 70.0

EUR_GBP = 0.89
MAGLEV_EUR_SEAT = 49233.0          # Almujibah & Preston 2018 Table 6, 2009 prices
MAGLEV_EUR_SEAT_KM = 0.011
IDX_PURCHASE_2009 = 82.87        # workbook index 8,287 is in per cent of the 1900 level
IDX_GENERAL_2009 = 91.63
LABOUR = 0.96                      # Germany; report 17 section 5, 25 per cent labour share
REF_SEATS, REF_LENGTH = 54.0, 14.0
CAP_PER_SEAT = MAGLEV_EUR_SEAT * EUR_GBP / IDX_PURCHASE_2009 * LABOUR
CAP_PER_M = CAP_PER_SEAT * REF_SEATS / REF_LENGTH
MAINT_SEAT_KM = MAGLEV_EUR_SEAT_KM * EUR_GBP / IDX_GENERAL_2009 * LABOUR
MAINT_PER_M_KM = MAINT_SEAT_KM * REF_SEATS / REF_LENGTH

ROAD_OVERHAUL_SHARE = 0.375        # 1947 Commercial Motor fleet composition

SHEETS = ('Rail vehicles', 'Road vehicles', 'Tram vehicles', 'Water vehicles', 'Air vehicles',
          'Narrow gauge vehicles', 'Maglev vehicles')
ANIMAL_SHEETS = ('Rail vehicles', 'Road vehicles', 'Tram vehicles', 'Water vehicles',
                 'Narrow gauge vehicles')
ANIMAL_RE = re.compile(r'\b(horse|horses|pony|ponies|mule|mules|donkey|donkeys)\b', re.I)
PAIR_RE = re.compile(r'pair|\bdouble\b|\bhorses\b|\bponies\b|\bmules\b|\bdonkeys\b', re.I)


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
PREFIX = ' | Maintenance decomposition (pass 4'


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def head_and_k(ae):
    m = re.search(r'(?:Annual maintenance figure|Head figure) ([\d,.]+) GBP', ae)
    k = re.search(r'at (?:mean annual distance )?([\d,]+) km a year', ae)
    H = float(m.group(1).replace(',', '')) if m else None
    K = float(k.group(1).replace(',', '')) if k else None
    return H, K


def composition(ae):
    m = re.search(r'Source composition: (.*?) Treatment:', ae, re.S)
    return m.group(1).strip() if m else ''


def split_note(ae):
    """Everything before the first pass-4x decomposition paragraph."""
    i = ae.find(PREFIX)
    return (ae[:i].rstrip(' |') if i >= 0 else ae.rstrip()), (ae[i:] if i >= 0 else '')


def dat_blocks(path):
    txt = open(path, encoding='utf-8', errors='replace').read()
    out = {}
    for b in re.split(r'(?m)^name=', txt)[1:]:
        name = b.splitlines()[0].strip()
        def g(key):
            m = re.search(r'(?m)^%s=([^\r\n]+)' % re.escape(key), b)
            return m.group(1).strip() if m else None
        out[name.lower()] = dict(power=g('power'), engine=g('engine_type'),
                                 length=g('length'), payload0=g('payload[0]'),
                                 payload1=g('payload[1]'))
    return out


def horse_price(name):
    nm = name.lower()
    base = HORSE_DEFAULT
    for k, v in HORSE_PRICE.items():
        if k in nm:
            base = v
            break
    if PAIR_RE.search(nm):
        base *= 2.0
    return base


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']

    # overhaul rows by base name
    overhaul = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            overhaul[str(b)] = r

    stats = {'horse': 0, 'horse_cap': 0, 'maglev': 0, 'road': 0}
    samples = []
    problems = []
    section_rows = set()

    # ------------------------------------------------------------ 1. animals
    for sheet in ANIMAL_SHEETS:
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = ws.cell(r, 1).value
            if not name or not ANIMAL_RE.search(str(name)):
                continue
            base = str(ws.cell(r, 2).value or '')
            datpath = os.path.join(BASE, 'New', str(ws.cell(r, 3).value or '').replace('/', os.sep))
            if not os.path.exists(datpath):
                problems.append(('animal dat missing', sheet, r, name))
                continue
            blocks = dat_blocks(datpath)
            blk = blocks.get(base.lower())
            if not blk or str(blk.get('engine') or '').lower() != 'bio':
                continue                      # a horse-drawn vehicle, not an animal
            try:
                power = float(blk.get('power') or 0)
            except ValueError:
                power = 0
            if power < 1:
                continue
            pair = bool(PAIR_RE.search(str(name)))
            keep = HORSE_KEEP_YR * (2 if pair else 1)
            price = horse_price(str(name))
            old = str(ws.cell(r, 31).value or '')
            if MARK in old:
                continue
            oldH, _ = head_and_k(old)
            pre, _ = split_note(old)
            road_horse = 'London horse-keep accounts' in old
            if road_horse and not pair and oldH == HORSE_KEEP_YR:
                continue                      # already correct: a single animal at 45
            if road_horse:
                note = ('%s | Maintenance decomposition (pass 43). Annual maintenance figure %s '
                        'GBP per animal-year in 1900 money (London horse-keep accounts 1876-97: '
                        'about 45 GBP a year an animal, band 28-60, excluding the horsekeeper\'s '
                        'wages; New/ai/vehicle-cost/horse-keep-totals.md). The figure is for a '
                        'pair of animals, so it is twice the single-animal keep. Composition: the '
                        'accounts itemise feed, farriery, veterinary care and stabling; no '
                        'renewal or overhaul element is stated to be inside, so nothing is '
                        'deducted. Treatment: the whole figure is the standing charge and there '
                        'is no per-km figure (maintenance-decomposition standing rule 2). The '
                        'pass 42 figure of %s GBP was the keep for one animal and understated a '
                        'pair; corrected in pass 43.'
                        % (pre, f2(keep), f2(oldH) if oldH is not None else '45'))
                stats['horse'] += 1
                if len(samples) < 4:
                    samples.append(('HORSE', sheet, r, name, keep, None, note))
                if WRITE:
                    ws.cell(r, 27, round(keep, 2))
                    ws.cell(r, 31, note)
                continue
            was = ('the tram car figure (64 GBP a car-year)'
                   if 'car-year' in old else
                   'the ship figure (2 per cent of capital)' if sheet == 'Water vehicles' else
                   'the Hill 1895 steam locomotive figure (253 GBP an engine-year)')
            note = ('Maintenance decomposition (pass 43). Annual maintenance figure %s GBP '
                    'per animal-year in 1900 money (London horse-keep accounts 1876-97: about 45 '
                    'GBP a year an animal, band 28-60, excluding the horsekeeper\'s wages; '
                    'New/ai/vehicle-cost/horse-keep-totals.md). Composition: the accounts itemise '
                    'feed, farriery, veterinary care and stabling; no renewal or overhaul element '
                    'is stated to be inside, so nothing is deducted. A horse has no overhaul in '
                    'the engine\'s sense: its replacement is the renewal and is charged through '
                    'the purchase price. Treatment: the whole figure is the standing charge and '
                    'there is no per-km figure (maintenance-decomposition standing rule 2).%s '
                    'This replaces the pass 42 figure of %s GBP a year, which was %s: the '
                    'generator\'s horse clause sat after the class ladders, so the animals on '
                    'this sheet took the sheet\'s head. Corrected in pass 43; the generator is '
                    'guarded by the same rule in source-composition.md.'
                    % (f2(keep), (' The figure is for a pair of animals, so it is twice the '
                                  'single-animal keep.' if pair else ''),
                       f2(oldH) if oldH is not None else 'an unknown figure', was))
            stats['horse'] += 1
            if len(samples) < 4:
                samples.append(('HORSE', sheet, r, name, keep, None, note))
            if WRITE:
                ws.cell(r, 27, round(keep, 2))
                ws.cell(r, 28, 1900)
                ws.cell(r, 29).value = None
                ws.cell(r, 30).value = None
                ws.cell(r, 31, note)

            # capital row
            cw = wc[sheet]
            cr = None
            for rr in range(7, cw.max_row + 1):
                if str(cw.cell(rr, 2).value or '') == base:
                    cr = rr
                    break
            if cr is None:
                problems.append(('horse capital row missing', sheet, r, name))
            else:
                oldcap = cw.cell(cr, 22).value
                capnote = ('horse breed/type ladder (1900 GBP): pony 25, hackney 55, Friesian 120, '
                           'Cleveland Bay 90, Yorkshire coach 90, Irish draught 135, Clydesdale '
                           '175, Shire 180, cart/dray 60; a pair doubles the figure (1893 London '
                           'type ladder: cab 30, omnibus 35, mail 36, railway 60, heavy team 105 '
                           'guineas at index 78; vestry medians 55-65; army remounts 20-60. '
                           'HORSE_PRICE in New/ai/cost-balancing/evidence_data.py). The row '
                           'previously carried %s GBP from the %s, because the generator\'s horse '
                           'clause sat after the class ladders. Corrected in pass 43.'
                           % (f2(oldcap) if isinstance(oldcap, (int, float)) else 'no figure',
                              {'Tram vehicles': 'tram car ladder',
                               'Water vehicles': 'flat whole-ship ladder',
                               'Rail vehicles': 'steam locomotive ladder',
                               'Narrow gauge vehicles': 'steam locomotive ladder'}.get(sheet, 'sheet ladder')))
                stats['horse_cap'] += 1
                if WRITE:
                    cw.cell(cr, 22, round(price, 1))
                    cw.cell(cr, 23, 1900)
                    cw.cell(cr, 24, capnote)

    # ------------------------------------------------------------ 2. maglev
    ws = wm['Maglev vehicles']
    cw = wc['Maglev vehicles']
    for r in range(7, ws.max_row + 1):
        name = ws.cell(r, 1).value
        if not name:
            continue
        old = str(ws.cell(r, 31).value or '')
        if MARK in old:
            continue
        base = str(ws.cell(r, 2).value or '')
        datpath = os.path.join(BASE, 'New', str(ws.cell(r, 3).value or '').replace('/', os.sep))
        if not os.path.exists(datpath):
            problems.append(('maglev dat missing', r, name))
            continue
        blk = dat_blocks(datpath).get(base.lower())
        if not blk:
            problems.append(('maglev block missing', r, name, base))
            continue
        length = float(blk.get('length') or 14)
        seats = None
        try:
            seats = float(blk.get('payload1') or 0)
        except ValueError:
            seats = 0
        if seats and seats > 0:
            capital = CAP_PER_SEAT * seats
            perkm = MAINT_SEAT_KM * seats
            unit = '%d seats at %.1f GBP a seat' % (int(seats), CAP_PER_SEAT)
            munit = '%d seats at %.8f GBP a seat-km' % (int(seats), MAINT_SEAT_KM)
        else:
            capital = CAP_PER_M * length
            perkm = MAINT_PER_M_KM * length
            unit = ('For stock with no seat count, the seat rate is applied per metre of car '
                    'length: %g m at %.1f GBP a metre (the 14 m, 54-seat reference car)'
                    % (length, CAP_PER_M))
            munit = '%g m at %.8f GBP a metre-km' % (length, MAINT_PER_M_KM)
        pre, _ = split_note(old)
        note = ('Maintenance decomposition (pass 43) — not a decomposition: the maintenance '
                'figure is an individual unit cost, so it is used directly. Overseas maglev '
                'rolling-stock maintenance: EUR 0.011 a seat-km at 2009 prices (Almujibah and '
                'Preston, "The total social costs of constructing and operating a maglev line", '
                'Transportation Systems and Technology 4(3 suppl. 1), 2018, Table 6; the unit '
                'costs are drawn from the Shanghai, Linimo, Incheon and Changsha systems). '
                'Converted at EUR 1 = GBP 0.89, deflated on the general index (91.63 times the '
                '1900 level in 2009) '
                'and adjusted for labour cost to United Kingdom levels (x0.96 for Germany, the '
                'source country, at a 25 per cent labour share; research-pricing-report-17 '
                'section 5): GBP %.8f a seat-km in 1900 money. %s = GBP %.8f a vehicle-km. The '
                'source cost is distance-driven, so the whole figure is the per-km charge and '
                'there is no fixed charge. This replaces the Hill 1895 steam locomotive figure '
                '(253 GBP an engine-year) and its per-km charge, which are not evidence for a '
                'maglev: there are no mainline maglevs in Britain (user direction; '
                'New/ai/vehicle-cost/maglev-costs.md).' % (MAINT_SEAT_KM, munit, perkm))
        stats['maglev'] += 1
        if len(samples) < 8:
            samples.append(('MAGLEV', 'Maglev vehicles', r, name, None, perkm, note))
        if WRITE:
            ws.cell(r, 27).value = None
            ws.cell(r, 28).value = None
            ws.cell(r, 29).value = round(perkm, 10)
            ws.cell(r, 30, 1900)
            ws.cell(r, 31, note)
        # capital
        cr = None
        for rr in range(7, cw.max_row + 1):
            if str(cw.cell(rr, 2).value or '') == base:
                cr = rr
                break
        if cr is None:
            problems.append(('maglev capital row missing', r, name))
            continue
        capnote = ('Overseas maglev rolling stock: EUR 49,233 a seat at 2009 prices (Almujibah and '
                   'Preston 2018, Table 6, the unit acquisition cost of a Transrapid trainset from '
                   'the Shanghai, Linimo, Incheon and Changsha system costs). Converted at EUR 1 = '
                   'GBP 0.89, deflated on the vehicle purchase index (82.87 times the 1900 level '
                   'in 2009) and adjusted for labour cost to United Kingdom levels (x0.96; '
                   'research-pricing-report-17 section 5): %.1f GBP a seat in 1900 money. %s = '
                   '%.0f GBP. This replaces the diesel/electric locomotive ladder, which is not '
                   'evidence for a maglev: there are no mainline maglevs in Britain (user '
                   'direction; New/ai/vehicle-cost/maglev-costs.md).' % (CAP_PER_SEAT, unit, capital))
        if WRITE:
            cw.cell(cr, 22, round(capital, 0))
            cw.cell(cr, 23, 1900)
            cw.cell(cr, 24, capnote)

    # ------------------------------------------------------------ 3. road buses
    # 3a. articulated rear sections misclassified as horse-drawn coaches
    ws = wm['Road vehicles']
    cw = wc['Road vehicles']
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if not name or not re.search(r'\((rear|centre)\)', name, re.I):
            continue
        aa = ws.cell(r, 27).value
        j = ws.cell(r, 10).value
        ae = str(ws.cell(r, 31).value or '')
        if not isinstance(aa, (int, float)) or aa == 0 or j not in (0, None):
            continue
        if 'horse-drawn passenger ladder' not in ae:
            continue
        pre, _ = split_note(ae)
        note = ('%s | Maintenance decomposition (pass 43). This is the rear section of an '
                'articulated road vehicle, not a separate vehicle: the leading section carries '
                'the whole maintenance and the whole purchase price (pakset convention, the same '
                'rule as the articulated tram sections; the .dat cost and fixed_cost are zero). '
                'The class figure of %s GBP a year came from the horse-drawn passenger ladder, '
                'which the generator applied to any unpowered passenger-carrying row; a motor bus '
                'rear section is not a horse-drawn coach. Corrected to zero in pass 43.'
                % (pre, f2(aa)))
        stats.setdefault('section', 0)
        stats['section'] += 1
        section_rows.add(r)
        if WRITE:
            ws.cell(r, 27, 0)
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = None
            ws.cell(r, 30).value = None
            ws.cell(r, 31, note)
        base = str(ws.cell(r, 2).value or '')
        for rr in range(7, cw.max_row + 1):
            if str(cw.cell(rr, 2).value or '') == base:
                cw.cell(rr, 22, 0)
                cw.cell(rr, 23, 1900)
                cw.cell(rr, 24, ('rear section of an articulated road vehicle: the leading '
                                 'section carries the whole purchase price (pakset convention; the '
                                 '.dat cost is zero). The class figure previously came from the '
                                 'horse-drawn passenger ladder. Corrected in pass 43.'))
                break

    ws = wm['Road vehicles']
    for r in range(7, ws.max_row + 1):
        name = ws.cell(r, 1).value
        if not name:
            continue
        if r in section_rows:
            continue
        old = str(ws.cell(r, 31).value or '')
        if 'pass 42' not in old or MARK in old:
            continue
        aa = ws.cell(r, 27).value
        if not isinstance(aa, (int, float)) or aa == 0:
            continue                      # zero-priced rear unit: nothing to decompose
        base = str(ws.cell(r, 2).value or '')
        rec = overhaul.get(base)
        if rec is None:
            continue
        tag = str(wo.cell(rec, 24).value or '')
        if not tag.startswith('bus '):
            continue
        H, K = head_and_k(old)
        first, mx, km = wo.cell(rec, 14).value, wo.cell(rec, 15).value, wo.cell(rec, 17).value
        if not (H and K and isinstance(first, (int, float)) and isinstance(km, (int, float)) and km):
            problems.append(('bus arithmetic missing', r, name))
            continue
        mx = mx if isinstance(mx, (int, float)) else first
        O = (first + mx) / 2.0 * K / km
        if O <= ROAD_OVERHAUL_SHARE * H * 1.0001:
            continue
        scale = ROAD_OVERHAUL_SHARE * H / O
        new_first, new_max = first * scale, mx * scale
        O2 = ROAD_OVERHAUL_SHARE * H
        R = H - O2
        F = 0.25 * R
        V = 0.75 * R / K
        comp = composition(old)
        pre, _ = split_note(old)
        note = ('%s | Maintenance decomposition (pass 43). Annual maintenance figure %s GBP per '
                'vehicle-year in 1900 money, at mean annual distance %s km a year. Source '
                'composition: %s Treatment: the source states major repairs are inside the '
                'figure, so it is a confirmed combined total and the overhaul money is a '
                'component of it. The split is measured, not estimated: the 1947 Commercial '
                'Motor fleet account for twelve 32-seat coaches at 24,000 miles a year gives '
                'GBP 426.7 a vehicle-year, of which engine reconditioning at GBP 120 and body '
                'overhaul at GBP 200, both on alternate years, are GBP 160, or 37.5 per cent '
                '(research-pricing-report-31 section 2.1). Deducted: GBP %s a year, being 37.5 '
                'per cent of this head. Routine remainder %s GBP a year, being 62.5 per cent, '
                'split 75/25 distance/standing (the measured 1959 split is 22-33 per cent '
                'standing at 31,200 miles a year, so the 25 per cent used is within it): fixed '
                '%s GBP a year, per-km %.8f GBP per km. The overhaul targets in the Overhauls & '
                'upgrades sheet were rescaled to the same provision (first %s, max %s GBP). This '
                'replaces the pass 42 treatment, which deducted the annualised overhaul '
                'provision itself, GBP %s a year, or %.0f per cent of the whole head; that '
                'provision is an estimate from capital shares, and a share above 37.5 per cent '
                'contradicts the only measured composition of this total. Direction: a measured '
                'overhaul invoice and interval for this vehicle would replace the 37.5 per cent '
                'share; a measured fixed/distance split would move the two values without '
                'changing their sum.'
                % (pre, f2(H), format(int(K), ','), comp, f2(O2), f2(R), f2(F), V,
                   f2(new_first), f2(new_max), f2(O), 100.0 * O / H))
        stats['road'] += 1
        if len(samples) < 12:
            samples.append(('ROAD', 'Road vehicles', r, name, (O, O2, H), V, note))
        if WRITE:
            ws.cell(r, 27, round(F, 2))
            ws.cell(r, 28, 1900)
            ws.cell(r, 29).value = round(V, 8)
            ws.cell(r, 30).value = 1900
            ws.cell(r, 31, note)
            wo.cell(rec, 14, round(new_first, 1))
            wo.cell(rec, 15, round(new_max, 1))
            wo.cell(rec, 24, str(tag) + (' | pass 43: rescaled from first %s / max %s to first %s '
                                         '/ max %s, because the annualised provision of GBP %s a '
                                         'year was %.0f per cent of the measured GBP %s maintenance '
                                         'head and the only measured composition of that Commercial '
                                         'Motor total puts overhauls at 37.5 per cent (1947 fleet: '
                                         'engine GBP 120 + body GBP 200 on alternate years = GBP 160 '
                                         'against GBP 426.7 a vehicle-year; '
                                         'research-pricing-report-31). The provision is now GBP %s '
                                         'a year.' % (f2(first), f2(mx), f2(new_first),
                                                       f2(new_max), f2(O), 100.0 * O / H, f2(H),
                                                       f2(O2))))

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    for k in ('horse', 'horse_cap', 'maglev', 'section', 'road'):
        print('  %-10s %d' % (k, stats.get(k, 0)))
    for s in samples:
        print('\n--- %s  %s r%d  %s' % (s[0], s[1], s[2], s[3]))
        if s[0] == 'ROAD':
            print('    overhaul annual: %.1f -> %.1f, head %.1f' % s[4])
        print('    ' + s[6][:700])
    if problems:
        print('\nPROBLEMS:')
        for p in problems:
            print('   ', p)
    wm.close()
    wc.close()


if __name__ == '__main__':
    main()
