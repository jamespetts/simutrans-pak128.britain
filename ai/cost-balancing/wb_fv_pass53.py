# -*- coding: utf-8 -*-
# wb_fv_pass53.py — put every multiple-unit car on the report 45 maintenance ladder.
#
# WHY
# Multiple-unit cars were priced two ways, and both were wrong. Twenty rows carried the
# multiple-unit capital ladder but took Hill's 1892 carriage rate of GBP 32.6 a car-year for
# maintenance. The remaining cars were indistinguishable from locomotive-hauled stock, because
# is_multiple_unit() matched only names carrying EMU, DMU, DEMU, railcar, APT or tyneside-unit:
# a powered car of br-158-*, BR-365*, BR-465* or any *TubeStock* class took the locomotive rate
# of GBP 253 an engine-year, and an unpowered car took the carriage ladder. Research report 45
# section 6 item 2 found the classifier defect and section 5 gives the replacement rule.
#
# THE RULE (research report 45 section 5)
#   A = the multiple-unit ladder at the row's introduction year, 1900 money per car-year:
#       66 / 241 / 380 / 510 / 780 at 1900 / 1950 / 1970 / 1990 / 2020, log-linear between and
#       flat outside. One ladder applies to motor cars and trailer cars alike: no British source
#       separates them, and every measured rate is per vehicle over a whole formation.
#   Renewals: none deducted. Report 45 states that the ladder is a total-maintenance figure with
#       vehicle renewal and the capital lease outside it. The 1900 rung is 2.0 times the carriage
#       1900 value on report 43's renewals-excluded basis; the 1950, 1970 and 1990 rungs are
#       interpolations; the 2013 and 2024 anchors on which the 2020 rung rests are
#       total-maintenance rates that exclude the capital lease. No rung is stated to be gross of
#       renewals, so nothing is deducted. Pass 47 (wb_fv_pass47.py) found that report 43's 1900
#       and 1950 carriage anchors are gross of renewals (Hill writes "repairs and renewals"),
#       which puts the 1900 rung's composition in doubt; report 45 does not settle it, the note
#       says so, and the deduction stays at zero.
#   Overhaul provision: 15 per cent of A, an event of 1.2 x A every eight years (the measured
#       Class 158/9 C6 interval, where C6 is a classified heavy overhaul), the first at 0.70
#       of the maximum, three overhauls to the maximum. Report 45 states that works overhauls
#       are inside the ladder, so the provision is deducted from A.
#   Head: A - renewals - provision, split 50/50 fixed and per-km over the row's own mean annual
#       distance, as report 45 section 6 recommends.
#
# ZERO-PRICED REAR AND MIDDLE CARS
# build_workbooks.py treats a name ending '-rear' or '-middle' as a locomotive section and gives
# it a zero capital target, so 27 multiple-unit cars sat at zero maintenance. They are full cars:
# their .dat cost and their in-game charges equal the front car's. This pass restores the capital
# target from the sister car (scaled by the .dat cost where the two cars differ) and gives them
# the full treatment, because a formation's maintenance must count every car it runs.
#
# Run: py -3 wb_fv_pass53.py [--write]. Dry run by default. Idempotent: a row whose note carries
# 'pass 53' is skipped, so a second run reports zero changes. Never rebuild the workbooks.
import os
import re
import sys

from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from evidence_data import interp_log, is_multiple_unit

MARK = 'pass 53'
WRITE = '--write' in sys.argv
MU_MAINT_LADDER = ((1900, 66.0), (1950, 241.0), (1970, 380.0), (1990, 510.0), (2020, 780.0))
PROVISION = 0.15
YEARS = 8.0
FIRST_RATIO = 0.70
RUNGS = 3
FIXED_SHARE = 0.50
REF_KM = 161000.0     # 100,000 miles, the reference duty of report 45 section 5

RULE = ('research-pricing-report-45.md section 5 (and section 6 item 2 for the classifier)')


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


def num(pattern, text, default=None):
    m = re.search(pattern, text)
    if not m:
        return default
    try:
        return float(m.group(1).replace(',', ''))
    except (ValueError, IndexError):
        return default


def rung_text(year):
    """Which ladder rung the introduction year uses, named in the note."""
    pts = MU_MAINT_LADDER
    if year <= pts[0][0]:
        return ('the introduction year is at or before the 1900 rung, so the ladder is flat at '
                'its 1900 value of %s GBP' % f2(pts[0][1]))
    if year >= pts[-1][0]:
        return ('the introduction year is at or after the 2020 rung, so the ladder is flat at '
                'its 2020 value of %s GBP' % f2(pts[-1][1]))
    for y, v in pts:
        if year == y:
            return 'the introduction year falls on the %d rung (%s GBP)' % (y, f2(v))
    for (y0, v0), (y1, v1) in zip(pts, pts[1:]):
        if y0 < year < y1:
            return ('the introduction year falls between the %d rung (%s GBP) and the %d rung '
                    '(%s GBP), read log-linearly' % (y0, f2(v0), y1, f2(v1)))
    return 'the ladder'


def stem(nm):
    """The class stem of a car name, with the formation-position suffix removed."""
    n = nm.lower()
    for suf in ('-driving-rear', '-driving-front', '-rear-composite', '-rear', '-middle',
                '-middle1', '-middle2', '-centre', '-centre1', '-centre2', '-centre3',
                '-front', '-power', '-motor', '-trailer', '-panto', '-pantograph'):
        if n.endswith(suf):
            return n[:-len(suf)]
    return n


def pick_sister(name, cost, pool):
    """The same-class car whose .dat cost is closest to this row's, so the capital transfer is
    a like-for-like one."""
    s = stem(name)
    exact = [p for p in pool if stem(p['base']) == s]
    if not exact:
        s2 = s.rsplit('-', 1)[0]
        exact = [p for p in pool if stem(p['base']).startswith(s2) and len(s2) >= 5]
    if not exact:
        return None
    return min(exact, key=lambda p: abs((p['cost'] or 0.0) - (cost or 0.0)))


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r

    # ---- scan the multiple-unit rows of both maintenance sheets
    records = []
    for sheet in ('Rail vehicles', 'Narrow gauge vehicles'):
        if sheet not in wm.sheetnames:
            continue
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            base = str(ws.cell(r, 2).value or '')
            if not name or not base or not is_multiple_unit(base):
                continue
            note = str(ws.cell(r, 31).value or '')
            q = ovh.get(base)
            if q is None:
                raise SystemExit('no overhaul row for %s' % base)
            try:
                year = int(str(ws.cell(r, 5).value)[:4])
            except (TypeError, ValueError):
                year = 1900
            records.append(dict(sheet=sheet, row=r, name=name, base=base, note=note, q=q,
                                year=year,
                                K=num(r'at mean annual distance ([\d,]+) km', note),
                                M=wo.cell(q, 13).value if isinstance(wo.cell(q, 13).value,
                                                                    (int, float)) else 0.0,
                                cost=wo.cell(q, 7).value if isinstance(wo.cell(q, 7).value,
                                                                      (int, float)) else 0.0))

    # Sister pools: rows that already carry a distance and a positive capital target.
    pool_k = [x for x in records if x['K']]
    pool_m = [x for x in records if x['M'] and x['M'] > 0]

    stats = {}
    samples = []
    changed = 0
    for x in records:
        if MARK in x['note']:
            stats['already'] = stats.get('already', 0) + 1
            continue
        # ---- distance: the row's own, else the sister car's, else the 100,000-mile reference
        k_note = ''
        if not x['K']:
            sis = pick_sister(x['base'], x['cost'], pool_k)
            if sis is not None and sis['K']:
                x['K'] = sis['K']
                k_note = (' The distance is the sister car %s\'s %s km a car-year, because this '
                          'row carried no distance of its own.' % (sis['base'],
                                                                   format(int(x['K']), ',')))
            else:
                x['K'] = REF_KM
                k_note = (' The distance is the 100,000-mile reference duty of report 45 '
                          'section 5, 161,000 km a car-year, because the row stated none.')
        # ---- capital target for a row the generator zeroed as a multi-part section
        zero_note = ''
        if not x['M']:
            sis = pick_sister(x['base'], x['cost'], pool_m)
            if sis is None:
                raise SystemExit('cannot restore the capital target of %s' % x['base'])
            ratio = (x['cost'] / sis['cost']) if (sis['cost'] and x['cost']) else 1.0
            x['M'] = round(sis['M'] * ratio, 1)
            zero_note = (' The capital target was zero because build_workbooks.py treats a name '
                         'ending -rear or -middle as a locomotive section; this is a full car '
                         'with a positive .dat cost, so the target is restored to the class '
                         'value of %s GBP (from %s, scaled by the .dat cost where the two cars '
                         'differ). The overhaul arithmetic is absolute and does not use it.'
                         % (f2(x['M']), sis['base']))
        A = round(interp_log(MU_MAINT_LADDER, x['year']), 1)
        prov = round(PROVISION * A, 2)
        head = round(A - prov, 2)
        mean_event = round(prov * YEARS, 1)
        mx = round(2.0 * prov * YEARS / (1.0 + FIRST_RATIO), 1)
        first = round(FIRST_RATIO * mx, 1)
        km = int(round(YEARS * x['K']))
        F = round(FIXED_SHARE * head, 2)
        V = round((1.0 - FIXED_SHARE) * head / x['K'], 10)
        note = ('Maintenance decomposition (pass 53). Annual maintenance figure %s GBP per '
                'car-year in 1900 money, at mean annual distance %s km a year. Source: %s, the '
                'multiple-unit car ladder at the introduction year (%d): 66 GBP at 1900, 241 at '
                '1950, 380 at 1970, 510 at 1990 and 780 at 2020, log-linear between and flat '
                'outside, applied to every car of the formation because no British source '
                'separates a motor car from a trailer; %s.'
                % (f2(A), format(int(x['K']), ','), RULE, x['year'], rung_text(x['year'])))
        note += (' Composition, rung by rung: the 1900 rung is an estimate of 2.0 times the '
                 'carriage 1900 value and its composition is unsettled - report 45 calls it '
                 'renewals-excluded, but the carriage pass recorded in wb_fv_pass47.py found the '
                 'carriage anchor it doubles to be gross of renewals (the 1892 carriage source, '
                 'Hill, writes "repairs and renewals"), and if that applies 35 per cent of the '
                 'rung (%s GBP a year) is renewal; the 1950, 1970 and 1990 '
                 'rungs are log-linear interpolations and inherit that uncertainty, so their '
                 'composition is also unsettled; the 2013 and 2024 anchors on which the 2020 '
                 'rung rests are total-maintenance rates that exclude the capital lease, '
                 'because the Rail Delivery Group (RDG) prints maintenance and capital lease as '
                 'separate lines and the Office of Rail and Road (ORR) collects maintenance cost '
                 'only. Report 45 section 5 deducts no renewals '
                 'anywhere and directs that the 30 per cent multiple-unit renewals share in '
                 'maintenance-decomposition.md must not be applied to this ladder. This row '
                 'therefore deducts nothing. Renewals are 0 per cent of this figure = 0 GBP a '
                 'year.' % f2(0.35 * A))
        note += (' Works overhauls are inside the ladder, so the measured total is the envelope: '
                 'the continuous head and the amortised overhaul events together recover it. '
                 'The works-overhaul provision is %s per cent of A = %s GBP a year (report 45 '
                 'section 5), an event of 1.2 times A every eight years, the measured Class '
                 '158/9 C6 (classified heavy overhaul) interval. The mean event is %s GBP, paid '
                 'as a first overhaul of %s '
                 'GBP rising to a maximum of %s GBP over %d overhauls, the first at 0.70 of the '
                 'maximum. The interval is 8 years, entered as %s km at that distance. The '
                 'continuous head is the remainder, %s GBP a year, so the head plus the '
                 'amortised events equals A less renewals. The head is split %d/%d fixed and '
                 'per-km at this row\'s own distance, as report 45 section 6 recommends: fixed '
                 '%s GBP a year, per-km %.8f GBP a km. The optional diesel multiple unit (DMU) '
                 'premium of 1.8 in '
                 'report 45 section 5 is not applied, because the 1961 anchor is itself a '
                 'blend of diesel and electric multiple units (DMUs and EMUs) and the premium '
                 'would double-count it.%s%s'
                 % (f2(100.0 * PROVISION), f2(prov), f2(mean_event), f2(first), f2(mx), RUNGS,
                    format(km, ','), f2(head), round(FIXED_SHARE * 100),
                    round((1.0 - FIXED_SHARE) * 100), f2(F), V, zero_note, k_note))
        basis = ('pass 53: multiple-unit rule of research-pricing-report-45.md section 5. '
                 'Annual maintenance A = %s GBP a car-year from the ladder at %d (%s); '
                 'provision 15 per cent = %s GBP a year; event 1.2 x A = %s GBP every eight '
                 'years (%s km at %s km a car-year), first overhaul %s GBP, maximum %s GBP over '
                 'three overhauls, the first at 0.70 of the maximum. Head (the continuous annual '
                 'charge) = A - renewals (0) - '
                 'provision = %s GBP a year, split 50/50 fixed and per-km over the row\'s own '
                 'distance. The earlier capital-share overhaul target and the earlier five-to-six-'
                 'year interval '
                 'are superseded: report 45 measures the Class 158/9 C6 (classified heavy '
                 'overhaul) interval at '
                 'eight years and prices the routine C6X (classified heavy overhaul) event at '
                 '1.2 x A.%s'
                 % (f2(A), x['year'], rung_text(x['year']), f2(prov), f2(mean_event),
                    format(km, ','), format(int(x['K']), ','), f2(first), f2(mx), f2(head),
                    zero_note))
        stats['written'] = stats.get('written', 0) + 1
        fam = family(x['base'])
        stats[fam] = stats.get(fam, 0) + 1
        if len(samples) < 8 and fam not in [s[0] for s in samples]:
            samples.append((fam, x['name'], A, head, prov, first, mx, km, x['K']))
        if WRITE:
            ws = wm[x['sheet']]
            ws.cell(x['row'], 27, F)
            ws.cell(x['row'], 28, 1900)
            ws.cell(x['row'], 29).value = V
            ws.cell(x['row'], 30).value = 1900
            ws.cell(x['row'], 31, note)
            wo.cell(x['q'], 13, x['M'])
            wo.cell(x['q'], 14, first)
            wo.cell(x['q'], 15, mx)
            wo.cell(x['q'], 16, RUNGS)
            wo.cell(x['q'], 17, km)
            wo.cell(x['q'], 24, basis)
        changed += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  changed %d, already on pass 53 %d' % (changed, stats.get('already', 0)))
    print('  ' + ', '.join('%s %d' % (k, v) for k, v in sorted(stats.items())
                           if k not in ('written', 'already')))
    for s in samples:
        print('  %-18s %-34s A=%7.1f head=%7.1f prov=%6.1f event=%7.1f/%7.1f km=%8d K=%8d'
              % (s[0], s[1][:34], s[2], s[3], s[4], s[5], s[6], s[7], s[8]))
    wm.close()
    wc.close()


def family(nm):
    n = nm.lower()
    if re.search(r'dmu|demu', n):
        return 'dmu'
    if 'emu' in n:
        return 'emu'
    if re.search(r'railcar|railbus|railmotor|twinset', n):
        return 'railcar'
    if 'tyneside' in n:
        return 'tyneside'
    if 'tubestock' in n:
        return 'tube'
    if n.startswith(('lul_', 'district_', 'metropolitan', 'met-mv-stock', 'watfordjointstock')):
        return 'underground'
    if n.startswith('dlr-') or 'tynewearmetro' in n:
        return 'light-metro'
    if n.startswith('sr-'):
        return 'sr-emu'
    if n.startswith(('br-', 'c2c-')):
        return 'br-class'
    if n.startswith('lms-502'):
        return 'lms-emu'
    return 'pre-1948'


if __name__ == '__main__':
    main()
