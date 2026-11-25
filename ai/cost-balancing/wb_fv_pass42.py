# -*- coding: utf-8 -*-
# wb_fv_pass42.py — write the maintenance decomposition into the vehicle sheets of
# New/cost-balancing-maintenance.xlsx (columns AA Class fixed GBP/yr, AB year,
# AC Class per-km GBP, AD year, AE Class basis note).
#
# Supersedes wb_fv_pass41.py, which applied T = rho + O + R to every row on the assumption that
# every head figure contains renewals and works overhauls. That assumption is wrong: the
# treatment follows the composition each source states (user direction 2026-11-25;
# New/ai/vehicle-cost/source-composition.md).
#
# Treatments, per head family:
#   PARTIAL-RENEWALS   the source states renewals are inside the figure but is silent on works
#                      overhauls: deduct rho only, write the routine remainder split.
#   PARTIAL-OVERHAUL   the source states major repairs/overhauls are inside the figure and keeps
#                      depreciation outside: deduct the annualised overhaul provision only.
#   NO DECOMPOSITION   nothing is stated to be inside of a subtractable element: deduct nothing.
#                      Standing-only classes are written whole in the fixed column.
#   OPEN QUESTION      the composition is not stated anywhere in the recorded evidence: deduct
#                      nothing, split nothing, write the class figure whole and flag the passage
#                      that would settle it.
#
# NEVER rebuild the workbooks (build_workbooks.py warning): this script patches cells in place
# and touches no other sheet or workbook. Run: py -3.13 wb_fv_pass42.py [--write] [--force]
# Default is a dry run. Idempotent: rows whose basis already carries MARK are skipped unless
# --force (used when re-running after restoring the workbook from git, which has no MARK).
import os
import re
import sys
from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wb_overhaul_pass40 as ov40


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
MARK = 'pass 42'
WRITE = '--write' in sys.argv
FORCE = '--force' in sys.argv

SHEETS = ('Rail vehicles', 'Road vehicles', 'Tram vehicles', 'Water vehicles', 'Air vehicles',
          'Narrow gauge vehicles', 'Maglev vehicles')

# Fixed share of the routine remainder, by class (research-pricing-report-40 sections 3 and 5;
# estimates at rung 2-3, recorded here because the engine has two money fields).
SPLIT = {'carriage': 0.70, 'steam': 0.60, 'diesel': 0.50, 'mu': 0.50, 'wagon': 0.65,
         'bus': 0.25, 'lorry': 0.25, 'tram': 0.48}
DIESEL_K = ov40.DIESEL_K
DIESEL_K_DEFAULT = 109000
HILL_SRC = ('Hill 1895, "Repairs and Renewals of Railway Rolling-Stock", Minutes of the '
            'Proceedings of the Institution of Civil Engineers 122, Appendix II')


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def carriage_k(tag):
    if 'Victorian' in tag:
        return 32000, 'the Victorian carriage band puts 160,000 km between overhauls at 4-6 years'
    if 'Edwardian' in tag:
        return 40000, 'the late Victorian/Edwardian band puts 240,000 km at 5-7 years'
    if 'Grouping' in tag:
        return 37000, 'the Grouping band puts 130,000 km at 3-4 years'
    if 'Mk 1/2' in tag:
        return 60000, 'the Mk 1/2 band puts 120,000 km per two-year coded visit'
    if 'Mk 3+' in tag:
        return 45450, 'the Mk 3+ band puts 500,000 km at a 10-12 year heavy event'
    return 172600, 'the modern band puts 450,000 km at a 950-day heavy event'


def k_for(kind, tag, name, year):
    if kind == 'mu':
        if 'third-gen' in tag:
            return 172600, 'the third-generation band puts 450,000 km at a 950-day event'
        if 'first-gen' in tag:
            return 100000, 'the first-generation band puts 200,000 km at a two-year visit'
        return 120000, 'the second-generation band puts 480,000 km at a four-year C4'
    if kind == 'carriage':
        return carriage_k(tag)
    if kind == 'diesel':
        low = name.lower()
        for pat, kk, label in DIESEL_K:
            if re.search(pat, low):
                return kk, 'measured class duty %s %s km/yr (TRB Special Report 180)' % (
                    label, format(int(kk), ','))
        return DIESEL_K_DEFAULT, 'no measured class duty is recorded; 109,000 km/yr is assumed'
    if kind == 'steam':
        return 40000, 'no measured class duty is recorded; 40,000 km/yr is assumed'
    if kind == 'wagon':
        return 40000, 'no measured class duty is recorded; 40,000 km/yr is assumed'
    return 40000, 'no measured class duty is recorded; 40,000 km/yr is assumed'


# ---------------------------------------------------------------- head families
def head_family(sheet, ae, T, tag):
    """Which source head figure the row carries, from the generator's basis text."""
    t = ae.lower()
    if 'horse-keep accounts' in t:
        return 'HORSE_KEEP'
    if ('cart maintenance' in t or 'horse-drawn passenger ladder' in t
            or re.search(r'\brepair gbp \d', t)):
        # The cart maintenance rule covers horse-drawn vehicles AND motor trailers; the
        # overhaul sheet's tag separates them.
        return 'TRAILER_RULE' if 'trailer (pass 40)' in tag else 'HORSE_VEHICLE'
    if 'multiple-unit car ladder' in t:
        return 'MU_CARRIAGE'
    if 'carriage interpolation' in t or 'carriage rate' in t or 'carriage ladder' in t:
        return 'HILL_CARRIAGE'
    if 'wagon maintenance' in t:
        return 'WAGON_RULE'
    if ('weight^0.86' in t or 'power^0.889' in t or 'per hp' in t
            or 'electric locomotive' in t):
        return 'HILL_LOCO'
    if sheet == 'Tram vehicles':
        return 'TRAM_MOT' if (T or 0) <= 200 else 'TRAM_CONTRACT'
    if sheet == 'Water vehicles':
        return 'WATER_SHARE'
    if sheet == 'Air vehicles':
        return 'AIR_LINE'
    if sheet == 'Road vehicles':
        return 'ROAD_TRAILER' if 'for the trailer alone' in t else 'ROAD_MEASURED'
    return None


CLASS_PATTERNS = (
    (r'^steam \(pass 40', 'steam'),
    (r'^diesel/electric \(pass 40', 'diesel'),
    (r'^MU ', 'mu'),
    (r'^wagon \(pass 40', 'wagon'),
    (r'^carriage-.*band \(pass 40', 'carriage'),
    (r'^bus .*band \(pass 40', 'bus'),
    (r'^lorry \(pass 40', 'lorry'),
    (r'^tram ', 'tram'),
)


def tag_class(tag):
    for pat, kind in CLASS_PATTERNS:
        if re.search(pat, tag):
            return kind
    return None


def mu_name_kind(name, dat):
    if re.search(r'\btube stock\b|multiple unit|\bemu\b|\bdmu\b|stock \(.*\btrailer\b|'
                 r'\bUNDM\b|driving motor|driving trailer|motor coach|non-driving motor',
                 name, re.I) or re.search(r'tube-stock|multiple-unit|-emu|-dmu', dat, re.I):
        return 'mu'
    return None


def fallback_class(name, dat, year, sheet, ae):
    kind = ov40.classify(name, dat, '', '', year)
    if kind in ('mu-first', 'mu-second', 'mu-third'):
        return 'mu'
    if kind in ('steam', 'diesel', 'wagon', 'carriage', 'bus', 'lorry', 'tram'):
        return kind
    t = ae.lower()
    if 'multiple-unit car ladder' in t:
        return 'mu'
    if 'carriage interpolation' in t or 'carriage rate' in t or 'carriage ladder' in t:
        return 'carriage'
    if 'wagon maintenance' in t:
        return 'wagon'
    if 'weight^0.86' in t:
        return 'steam'
    if 'power^0.889' in t or 'per hp' in t or 'electric locomotive' in t:
        return 'diesel'
    if sheet == 'Maglev vehicles':
        return 'diesel'
    if sheet == 'Narrow gauge vehicles':
        return 'steam'
    return None


# ---------------------------------------------------------------- overhaul rows
def load_overhaul():
    wb = load_workbook(CAP, data_only=False)
    ws = wb['Overhauls & upgrades']
    ov = {}
    for r in range(7, ws.max_row + 1):
        base = ws.cell(r, 2).value
        name = ws.cell(r, 1).value
        if not base and not name:
            continue
        rec = dict(tag=str(ws.cell(r, 24).value or ''),
                   first=ws.cell(r, 14).value, mx=ws.cell(r, 15).value,
                   km=ws.cell(r, 17).value)
        for key in (base, name):
            if key:
                ov.setdefault(str(key), rec)
    wb.close()
    return ov


def annual_overhaul(rec, k_row):
    """(mean event cost GBP, annualised provision GBP/yr): mean divided by the interval in
    years, the interval being interval_km / k_row."""
    if not rec or not isinstance(rec.get('first'), (int, float)):
        return None
    if not isinstance(rec.get('km'), (int, float)) or not rec['km'] or not k_row:
        return None
    mx = rec['mx'] if isinstance(rec.get('mx'), (int, float)) else rec['first']
    mean = (rec['first'] + mx) / 2.0
    return mean, mean * k_row / rec['km']


# ---------------------------------------------------------------- notes
def note_rail(head, comp, rho, T, R, s, k, ksrc, F, V, o_ann, extra, o_basis):
    return ('Maintenance decomposition (pass 42). Head figure %s. Source composition: %s '
            'Deducted: renewals at %d per cent = %s GBP/yr, because the source states renewals '
            'are inside the figure and a vehicle renewal is the player\'s capital repurchase '
            'in-game (the `cost` field). Not deducted: works overhauls, because the source does '
            'not state whether the repairs element contains them.%s Routine remainder %s '
            'GBP/yr split %d/%d fixed/per-km at k = %s km/yr (%s): fixed %s GBP/yr, per-km %s '
            'GBP/km.%s Direction: a source statement that works overhauls sit inside the '
            'repairs element lowers the routine remainder by %s GBP/yr; a measured '
            'fixed/distance split or a measured annual distance moves the two values without '
            'changing their sum.'
            % (head, comp, round(rho * 100), f2(rho * T), o_basis, f2(R), round(s * 100),
               round((1 - s) * 100), format(int(k), ','), ksrc, f2(F), format(V, '.8f'),
               extra, o_ann))


def main():
    ov = load_overhaul()
    wb = load_workbook(MAINT, data_only=False)
    stats = {}
    negatives = []
    skipped = 0
    for sheet in SHEETS:
        ws = wb[sheet]
        for r in range(7, ws.max_row + 1):
            name = ws.cell(r, 1).value
            if not name:
                continue
            ae = str(ws.cell(r, 31).value or '')
            if MARK in ae and not FORCE:
                skipped += 1
                continue
            aa = ws.cell(r, 27).value
            ac = ws.cell(r, 29).value
            if not isinstance(aa, (int, float)) or aa == 0:
                continue                      # zero-priced units (multi-part convention)
            dat = str(ws.cell(r, 3).value or '')
            yv = ws.cell(r, 5).value
            try:
                year = int(str(yv)[:4])
            except Exception:
                year = 1900
            base = str(ws.cell(r, 2).value or '')
            rec = ov.get(base) or ov.get(str(name)) or {}
            tag = rec.get('tag', '')

            split_row = sheet in ('Road vehicles', 'Tram vehicles') and isinstance(ac, (int, float))
            T = aa / 0.25 if split_row else float(aa)
            fam = head_family(sheet, ae, T, tag)
            if fam is None:
                skipped += 1
                continue

            kind = None
            if sheet in ('Rail vehicles', 'Narrow gauge vehicles', 'Maglev vehicles'):
                kind = mu_name_kind(str(name), dat)
            kind = kind or tag_class(tag) or fallback_class(str(name), dat, year, sheet, ae)
            k, ksrc = k_for(kind, tag, str(name), year)
            m = re.search(r'at ([\d,]+) km a year', ae)
            if m and fam in ('ROAD_MEASURED', 'ROAD_TRAILER', 'TRAM_MOT', 'TRAM_CONTRACT'):
                k = float(m.group(1).replace(',', ''))   # the duty the generator split at
                ksrc = 'the reference distance the head was split at, assumed not measured'
            s = SPLIT.get(kind, 0.5)
            o = annual_overhaul(rec, k)
            o_ann = o[1] if o else 0.0

            F = V = None
            if fam in ('HILL_CARRIAGE', 'MU_CARRIAGE', 'HILL_LOCO', 'TRAM_MOT'):
                if fam == 'HILL_LOCO':
                    rho, comp = 0.25, (
                        'Hill states the figure is "maintenance, that is the cost of repairs and '
                        'renewals", the general rule being "to include the cost of renewals with '
                        'that of repairs", so renewals are inside it; locomotive running '
                        'expenses (fuel, enginemen, water, shed) are a separate abstract and '
                        'outside.')
                elif fam == 'TRAM_MOT':
                    rho, comp = 0.40, (
                        'the head is printed as "General Repairs and Maintenance (or Renewals '
                        'out of Revenue)" and the car-only column covers "repairs and renewals '
                        'charged to revenue of cars and their equipment only", so renewals '
                        'charged to revenue are inside it; fund renewals and depreciation sit '
                        'in a separate part of the return.')
                else:
                    rho, comp = 0.35, (
                        'Hill states the figure is "maintenance, that is the cost of repairs and '
                        'renewals", the general rule being "to include the cost of renewals with '
                        'that of repairs", so renewals are inside it; running expenses are a '
                        'separate abstract and outside.')
                if fam == 'MU_CARRIAGE':
                    T = 32.6      # the generator's mis-assignment of the locomotive figure
                    head = ('32.6 GBP per vehicle-year in 1900 money, the Hill 1892 carriage '
                            'rate, NOT the 253 the generator wrote to this row by mistake (a '
                            'guard was added to the generator on 2026-11-25; the multiple-unit '
                            'car ladder\'s intended maintenance head is the carriage rate)')
                elif fam == 'TRAM_MOT':
                    head = ('%s GBP per car-year in 1900 money (tram MoT returns, "Cars and '
                            'other Rolling Stock" column from 1919-20; New/ai/vehicle-cost/'
                            'tram-maintenance.md section A4; research-pricing-report-39 '
                            'section 7.1)' % f2(T))
                else:
                    head = '%s GBP per vehicle-year in 1900 money (%s)' % (f2(T), HILL_SRC)
                R = T * (1.0 - rho)
                if fam == 'TRAM_MOT':
                    s = 0.25
                    F, V = 0.25 * R, 0.75 * R / k
                else:
                    F, V = s * R, (1.0 - s) * R / k
                o_basis = (' If works overhauls are inside the repairs element, these values '
                           'double count the overhaul events charged separately in-game, and '
                           'netting them would reduce the routine remainder by O = %s GBP/yr '
                           '(mean event cost over the interval the Overhauls & upgrades sheet '
                           'records).' % f2(o_ann)) if o else ''
                extra = ''
                if fam == 'HILL_LOCO':
                    extra = (' Hill also prints the charge per train-mile (1.61d a train-mile = '
                             '0.0067 GBP/km); his per-mile and per-engine-year figures are the '
                             'same money only at about 37,000 km a year, so the per-km value '
                             'here is the apportioned share of the annual figure at the '
                             'assumed duty, not Hill\'s own rate.')
                elif fam == 'TRAM_MOT':
                    extra = (' The 75/25 distance/standing split is the generator\'s estimate, '
                             'kept here; research-pricing-report-40 section 5 recommends 40-55 '
                             'per cent standing, which would raise the fixed value and lower '
                             'the per-km value.')
                else:
                    extra = (' The source records carriage maintenance per vehicle-year only, '
                             'so this apportionment is the estimator\'s, not the source\'s.')
                note = note_rail(head, comp, rho, T, R, s, k, ksrc, F, V, f2(o_ann), extra,
                                 o_basis)

            elif fam in ('ROAD_MEASURED', 'ROAD_TRAILER'):
                O = 0.0
                flag = ''
                if fam == 'ROAD_MEASURED' and o is not None:
                    if T - o_ann < 0:
                        negatives.append((sheet, str(name), T, o_ann))
                        flag = (' The recorded elements exceed the figure: the head is %s '
                                'GBP/yr and the annualised overhaul provision from the '
                                'Overhauls & upgrades sheet is %s GBP/yr, which is %s GBP/yr '
                                'more than the whole head. A negative remainder is not a cost, '
                                'so the whole head is written here and no overhaul provision is '
                                'deducted. The excess is a conflict between two workbook '
                                'figures, not a rounding: the measured Commercial Motor '
                                'overhaul events are far smaller than the per-event figures the '
                                'overhaul sheet carries for this class (1947 coach: GBP 120 '
                                'engine recondition and GBP 200 body overhaul a vehicle on '
                                'two-year cycles). A bus or lorry overhaul invoice with its '
                                'interval would settle which figure is wrong.'
                                % (f2(T), f2(o_ann), f2(o_ann - T)))
                    else:
                        O = o_ann
                R = T - O
                F, V = 0.25 * R, 0.75 * R / k
                if fam == 'ROAD_TRAILER':
                    comp = ('the FTA 2016 table prints maintenance as a separate running-cost '
                            'line, with fuel, tyres, depreciation and VED as separate lines; it '
                            'does not itemise the line, so whether overhauls are inside is '
                            'unrecorded')
                    treat = ('nothing is deducted: depreciation is a separate line, so no '
                             'renewals share applies, and the source does not state that '
                             'overhauls are inside, so no overhaul provision is deducted')
                    direction = ('a statement of what the FTA maintenance line contains, and a '
                                 'second multi-band FTA table, would settle whether an overhaul '
                                 'provision belongs in the deduction')
                else:
                    comp = ('the Commercial Motor maintenance item is "washing, servicing and '
                            'major repairs"; the 1959 comparison states that it "consists of '
                            'two elements. One is the repair work, which varies directly with '
                            'the mileage run, and the other is servicing and washing, which are '
                            'normally scheduled on a time basis"; tyres and depreciation are '
                            'separate items in the same tables (published-maintenance.md '
                            '"Main definitional traps" 5-7; research-pricing-report-40 section '
                            '5)')
                    if O:
                        treat = ('renewals not deducted, because depreciation is a separate '
                                 'line (0 per cent); the annualised overhaul provision of %s '
                                 'GBP/yr is deducted because "major repairs" and "repairs and '
                                 'overhauls" are inside the figure, as the 1947 coach costing '
                                 'shows (engine reconditioning and body overhauls carried '
                                 'inside the maintenance total)' % f2(O))
                    else:
                        treat = ('nothing is deducted: depreciation is a separate line (0 per '
                                 'cent), and no overhaul row in the Overhauls & upgrades sheet '
                                 'matched this vehicle, so no overhaul provision is available '
                                 'to deduct even though "major repairs" are inside the figure')
                    if O:
                        direction = ('a maintenance figure that excludes overhauls would raise '
                                     'the routine remainder by %s GBP/yr; the measured 1959 '
                                     'split is 22-25 per cent standing at 31,200 miles a year, '
                                     'so a higher-duty vehicle carries a lower fixed share than '
                                     'the 25 per cent used here' % f2(O))
                    else:
                        direction = ('the recorded overhaul provision of %s GBP/yr is not '
                                     'deducted here, so a corrected overhaul figure well below '
                                     'it leaves these values unchanged, and a figure that fits '
                                     'inside the head lowers the routine remainder by its '
                                     'amount; the measured 1959 split is 22-25 per cent '
                                     'standing at 31,200 miles a year, so a higher-duty vehicle '
                                     'carries a lower fixed share than the 25 per cent used '
                                     'here' % f2(o_ann if o else 0))
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per '
                        'vehicle-year in 1900 money, at k = %s km/yr (the reference distance '
                        'the head was split at; assumed, not measured). '
                        'Source composition: %s. Treatment: %s.%s Routine remainder %s GBP/yr '
                        'split 75/25 distance/standing (generator estimate, band 15-35 per '
                        'cent): fixed %s GBP/yr, per-km %s GBP/km. Direction: %s.'
                        % (f2(T), format(int(k), ','), comp, treat, flag, f2(R), f2(F),
                           format(V, '.8f'), direction))

            elif fam in ('HORSE_KEEP', 'HORSE_VEHICLE'):
                F, V = T, None
                if fam == 'HORSE_KEEP':
                    comp = ('the London horse-keep accounts of 1876-97 itemise feed, farriery, '
                            'veterinary care and stabling and exclude the horsekeeper\'s '
                            'wages; no renewal or overhaul element is stated inside')
                    treat = ('nothing is deducted and nothing is split: the keep is a standing '
                             'cost, so the whole figure is the fixed charge and there is no '
                             'per-km figure (maintenance-decomposition standing rule 2). The '
                             'horse\'s own renewal is its overhaul (replacement at the end of '
                             'working life), which the keep figure excludes')
                else:
                    comp = ('the horse-vehicle accounts are repair bills per vehicle-year '
                            '(1760s coach GBP 70 a coach-year, about 70 per cent of capital); '
                            'no source states a renewal or overhaul element inside them')
                    treat = ('nothing is deducted and nothing is split: horse-drawn vehicles '
                             'take the standing-only treatment (maintenance-decomposition '
                             'standing rule 2), so the whole figure is the fixed charge')
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per '
                        'vehicle-year in 1900 money. Source composition: %s. Treatment: %s. '
                        'Direction: a measured per-mile repair split for horse vehicles, or an '
                        'account separating repairs from renewals, would change the treatment; '
                        'the level moves with the accounts sampled (horses, band 28-60 a year).'
                        % (f2(T), comp, treat))

            elif fam == 'TRAILER_RULE':
                F, V = T, None
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per '
                        'vehicle-year in 1900 money, being 5 per cent of the trailer\'s capital '
                        'as the generator computes it (the rule it applies to horse vehicles as '
                        'well). Composition unrecorded: no recorded source states what the 5 '
                        'per cent covers for a motor trailer, so whether renewals, works '
                        'overhauls or routine repairs alone are inside it is unknown. Nothing '
                        'is deducted and nothing is split; the figure is written whole. Open '
                        'question: the FTA 2016 maintenance line for a trailer (GBP 5.72 a '
                        'mile) would replace the 5-per-cent rule, and a trailer maintenance '
                        'schedule would state its composition. Direction: the FTA line is '
                        'probably lower than 5 per cent of capital a year, which would lower '
                        'this figure.' % f2(T))

            elif fam == 'WAGON_RULE':
                F, V = T, None
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per '
                        'vehicle-year in 1900 money, being 8 per cent of the wagon\'s capital as '
                        'the generator computes it; the level evidence behind the rule is Hill '
                        '1895 Appendix II Table III (19 companies, average GBP 4 4s. a '
                        'wagon-year for "repairs and renewals"). Composition unrecorded: no '
                        'recorded source states what the 8 per cent covers, so whether '
                        'renewals, works overhauls or routine repairs alone are inside it is '
                        'unknown. Nothing is deducted and nothing is split; the figure is '
                        'written whole as the class figure. Open question: a wagon repair '
                        'contract or a pre-1911 company wagon account separating complete '
                        'renewals from repairs and partial renewals would settle it (the '
                        'post-1911 Ministry of Transport returns print both columns but are not '
                        'digitised). Direction: if renewals are inside, the routine figure '
                        'falls by the renewals share (about 50 per cent by report 40 section '
                        '2); if works overhauls are inside, it falls by the annualised overhaul '
                        'provision.' % f2(T))

            elif fam == 'TRAM_CONTRACT':
                F, V = T, None
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per car-year '
                        'in 1900 money, from the Nottingham Express Transit 2011 rolling-stock '
                        'maintenance contract (GBP 101m over 23 years for 37 trams = GBP '
                        '118,657 a tram-year nominal, deflated to 1900; research-pricing-report-'
                        '40 section 5). Composition unrecorded: the contract is an availability '
                        'payment and no recorded source states whether renewals, overhauls or '
                        'routine upkeep alone are inside it. Nothing is deducted and nothing is '
                        'split; the figure is written whole as the class figure. Open question: '
                        'the contract\'s maintenance schedule or the operator\'s asset-renewal '
                        'accounting would settle it. Direction: research-pricing-report-40 '
                        'section 5 recommends 40-55 per cent standing for trams, so a settled '
                        'composition would move part of this figure to the per-km charge.'
                        % f2(T))

            elif fam == 'WATER_SHARE':
                F, V = T, None
                sail = bool(re.search(r'sail|brig|schooner|barge|keel|dogger|fifie|wherry|'
                                      r'clipper|barque|frigate|sloop|smack|hoy',
                                      str(name) + ' ' + ae, re.I))
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per '
                        'vessel-year in 1900 money, being 2 per cent of capital a year as the '
                        'generator computes it; the level evidence is the 1850 General Steam '
                        'Navigation repair bill (GBP 31,896 for 44 vessels = GBP 788 a '
                        'vessel-year; research-pricing-report-15 section 3.1), and 2 per cent '
                        'is that report\'s 1900-1920 share band, of which the 1913 liner '
                        'overhaul alone is 2 per cent (Kirkaldy 1914, p. 211). Composition '
                        'unrecorded: no recorded source states whether this share covers '
                        'routine repairs, overhauls, renewals or all three, and the report\'s '
                        'own note says that running repairs would add to the 2 per cent. '
                        'Nothing is deducted and nothing is split; the figure is written whole '
                        'as the class figure%s. Open question: a ship repair account separating '
                        'running repairs from surveys and renewals (Drewry Appendix 11/12, the '
                        'P&O repair ledgers, or the Royal Museums Greenwich barque accounts '
                        'ELEANOR DODSON AMS/36 and BURNS MSS/77/063) would settle it. '
                        'Direction: if the share is the overhaul alone, the routine figure '
                        'rises; if renewals are inside, it falls.'
                        % (f2(T), ('; sailing craft take the standing-only treatment in any '
                                   'case (maintenance-decomposition standing rule 2), so no '
                                   'per-km figure applies') if sail else ''))

            elif fam == 'AIR_LINE':
                F, V = T, None
                note = ('Maintenance decomposition (pass 42). Head figure %s GBP per '
                        'aircraft-year in 1900 money, being 20 per cent of capital a year as the '
                        'generator computes it, from BOAC\'s 1969/70 VC10 engineering cost (GBP '
                        '49,057 a year against a capital of GBP 209,085; '
                        'aircraft-maintenance.md section 1). Composition recorded only in part: '
                        'the engineering column excludes fuel, obsolescence, landing fees, '
                        'traffic handling and minor costs, which are separate columns, so '
                        'depreciation is outside the figure; the source does not itemise the '
                        'column into airframe, engine and components, so whether heavy checks '
                        'and engine shop visits are inside is unrecorded. Nothing is deducted '
                        'and nothing is split; the figure is written whole as the class figure. '
                        'Open question: a BOAC engineering-cost breakdown, or the IATA '
                        'Maintenance Cost Data eXchange segment tables, would settle whether '
                        'overhauls are inside. Direction: research-pricing-report-40 section 5 '
                        'measures 30-35 per cent of the bill as calendar-driven at 2,800 '
                        'flight-hours a year, so a settled composition would move about a third '
                        'of this figure to the fixed charge and the rest to the per-km charge.'
                        % f2(T))

            else:
                skipped += 1
                continue

            stats[fam] = stats.get(fam, 0) + 1
            if WRITE:
                ws.cell(r, 27, round(F, 2))
                ws.cell(r, 28, 1900)
                # openpyxl's ws.cell(r, c, None) does NOT clear a cell: assign .value instead.
                ws.cell(r, 29).value = round(V, 8) if V is not None else None
                ws.cell(r, 30).value = 1900 if V is not None else None
                ws.cell(r, 31, ae + ' | ' + note)

    if WRITE:
        wb.save(MAINT)
        print('WRITTEN')
    else:
        print('DRY RUN (no workbook changed)')
    wb.close()
    total = 0
    for key in sorted(stats):
        print('  %-16s %d rows' % (key, stats[key]))
        total += stats[key]
    print('rows written: %d; skipped: %d' % (total, skipped))
    print('rows where the stated elements exceed the head: %d' % len(negatives))
    for row in negatives[:10]:
        print('   %s %s T=%.2f O=%.2f' % row)


if __name__ == '__main__':
    main()
