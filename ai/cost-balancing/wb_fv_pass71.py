# -*- coding: utf-8 -*-
# wb_fv_pass71.py - correct the defects the independent sanity check found in the workbooks.
#
# WHAT THIS PASS FIXES
# 1. The "Suggested .dat interval km" column (Overhauls & upgrades, column 22) is stale on 2,751
#    rows: it disagrees with the modelled interval in column 17. The engine's
#    max_distance_between_overhauls is taken from the suggested column at the .dat pass, so the
#    two must be the same number. The pass copies column 17 into column 22 wherever they differ.
# 2. The four tub-boat fits carry four different gross tonnages (4.8, 2.4, 2.4, 4.2) because each
#    was bridged from its own capacity. Report 57 section 4 holds that gross tonnage is a property
#    of the hull, and the other multi-fit hulls already carry one figure on every fit. The four
#    take the largest fit's 4.8 GT and are re-priced at GBP 17/GT.
# 3. Twenty-eight water rows size the overhaul event to the whole annual figure A rather than to
#    the provision: the 15 sailing and small-craft rows (Brig, Schooner, the Norfolk wherries, the
#    skiff wherries, the Thames sailing barges) recover the continuous head a second time through
#    the event, and 13 more differ by 3-7 per cent. The event is re-sized so that its mid-point is
#    the provision times the interval in years, keeping the row's first/max ratio.
# 4. The pass 69 suffix on 68 locomotive notes prints the row's new distance as the inherited one
#    (for example "the inherited 65,000 km default is replaced ... (65,000 km)"). It is rewritten
#    with the true inherited value from the workbook before pass 69. Classes 89, 90 and 91 lost the
#    pass 69 suffix when pass 66 rewrote their notes; it is restored.
# 5. Three narrow-gauge locomotives still carry the inherited 109,000 km default outside pass 69's
#    scope (the rail sheet only): Baguely-Drewery 0-6-0, Funkey B-B and Hibberd Planet 4wDM. They
#    move to the class and era distance table, and the per-km charge and interval are recomputed.
#
# Run: py -3 wb_fv_pass71.py [--write]. Dry run by default. Idempotent by the pass 71 marker.
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evidence_data as ev

MARK = 'pass 71'
WRITE = '--write' in sys.argv
TUB_GT = 4.8
TUB_RATE = 17.0
YEARS_DEFAULT = 5.0
NG_LOCOS = ('Baguely-Drewery 0-6-0', 'Funkey B-B', 'Hibberd Planet Class 4wDM')


def find_base():
    d = HERE
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-capital.xlsx')):
            return d
        p = os.path.dirname(d)
        if p == d:
            raise SystemExit('workspace root not found')
        d = p


BASE = find_base()
CAP = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')
MAINT = os.path.join(BASE, 'New', 'cost-balancing-maintenance.xlsx')
PRE69 = os.path.join(BASE, 'ai', 'temp', 'pre69.xlsx')


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def old_distances(ws):
    """base name -> the mean annual distance stated before pass 69."""
    out = {}
    for r in range(7, ws.max_row + 1):
        b = str(ws.cell(r, 2).value or '')
        note = str(ws.cell(r, 31).value or '')
        m = re.search(r'at mean annual distance ([\d,]+) km', note)
        if b and m:
            out[b] = m.group(1)
    return out


def provision_from_note(note, A):
    """(provision share, provision GBP) from either water note form."""
    m = re.search(r'provision is ([\d.]+) per cent of A = ([\d,.]+) GBP', note)
    if m:
        return float(m.group(1)) / 100.0, float(m.group(2).replace(',', ''))
    m = re.search(r'provision \(([\d,.]+)\)', note)
    if m and A:
        p = float(m.group(1).replace(',', ''))
        return p / A, p
    return 0.35, 0.35 * A


def main():
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    wo = wc['Overhauls & upgrades']
    cs = wc['Water vehicles']
    ms = wm['Water vehicles']
    ns = wm['Narrow gauge vehicles']

    stats = {'interval': 0, 'tub': 0, 'water_events': 0, 'suffix': 0, 'ng': 0}

    # 1. Suggested .dat interval = modelled interval.
    for r in range(7, wo.max_row + 1):
        if not wo.cell(r, 2).value:
            continue
        km = wo.cell(r, 17).value
        sug = wo.cell(r, 22).value
        if not isinstance(km, (int, float)) or km <= 0:
            continue
        if isinstance(sug, (int, float)) and abs(sug - km) < 0.5:
            continue
        if WRITE:
            wo.cell(r, 22, km)
        stats['interval'] += 1

    # 2. The tub boat: one hull tonnage on all four fits, re-priced at the inland rate.
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r
    for r in range(7, cs.max_row + 1):
        name = str(cs.cell(r, 1).value or '')
        if 'tub boat' not in name.lower():
            continue
        base = str(cs.cell(r, 2).value or '')
        cap_new = TUB_RATE * TUB_GT
        try:
            cap_old = float(cs.cell(r, 22).value)
        except (TypeError, ValueError):
            continue
        if abs(cap_old - cap_new) < 0.01:
            continue
        m_note = str(ms.cell(r, 31).value or '')
        if MARK in m_note:
            continue
        mA = re.search(r'Annual maintenance figure ([\d,.]+) GBP', m_note)
        A_old = float(mA.group(1).replace(',', '')) if mA else 0.0
        share, P_old = provision_from_note(m_note, A_old)
        A_new = 0.02 * cap_new
        P_new = share * A_new
        H_new = A_new - P_new
        q = ovh.get(base)
        ev_first = ev_max = None
        if q:
            try:
                r_old = float(wo.cell(q, 14).value) / float(wo.cell(q, 15).value)
            except (TypeError, ValueError, ZeroDivisionError):
                r_old = 0.333
            mid = P_new * YEARS_DEFAULT
            ev_max = 2.0 * mid / (1.0 + r_old)
            ev_first = r_old * ev_max
        if WRITE:
            cs.cell(r, 22, round(cap_new, 2))
            cs.cell(r, 23, 1900)
            cap_note = str(cs.cell(r, 24).value or '')
            cap_note = re.sub(r'[\d,.]+ gross tons', '%s gross tons' % TUB_GT, cap_note, count=1)
            cap_note = re.sub(r'capital target is [\d,.]+ GBP', 'capital target is %s GBP'
                              % f2(cap_new), cap_note, count=1)
            cs.cell(r, 24, cap_note +
                    ' | pass 71: the four tub-boat fits share one hull of %g gross tons (report 57 '
                    'section 4); the per-fit capacity bridge is withdrawn and all four are priced '
                    'at GBP %g/GT.' % (TUB_GT, TUB_RATE))
            ms.cell(r, 27, round(H_new, 2))
            ms.cell(r, 29, None)
            mn = str(ms.cell(r, 31).value or '')
            mn = re.sub(r'Annual maintenance figure [\d,.]+ GBP',
                        'Annual maintenance figure %s GBP' % f2(A_new), mn, count=1)
            mn = re.sub(r'capital target of [\d,.]+ GBP',
                        'capital target of %s GBP' % f2(cap_new), mn, count=1)
            mn = re.sub(r'provision is [\d.]+ per cent of A = [\d,.]+ GBP',
                        'provision is %s per cent of A = %s GBP'
                        % (f2(100.0 * share), f2(P_new)), mn, count=1)
            mn = re.sub(r'head is the remainder, [\d,.]+ GBP',
                        'head is the remainder, %s GBP' % f2(H_new), mn, count=1)
            ms.cell(r, 31, mn +
                    ' | pass 71: re-priced at the hull tonnage of %g GT, which is the largest fit; '
                    'A, the provision and the head follow it.' % TUB_GT)
            if q and ev_first is not None:
                wo.cell(q, 14, round(ev_first, 1))
                wo.cell(q, 15, round(ev_max, 1))
        stats['tub'] += 1

    # 3. Water overhaul events sized to the provision, not to A.
    for r in range(7, cs.max_row + 1):
        name = str(cs.cell(r, 1).value or '')
        if not name:
            continue
        m_note = str(ms.cell(r, 31).value or '')
        if 'per animal-year' in m_note:
            continue
        base = str(cs.cell(r, 2).value or '')
        q = ovh.get(base)
        if not q:
            continue
        try:
            first = float(wo.cell(q, 14).value)
            mx = float(wo.cell(q, 15).value)
        except (TypeError, ValueError):
            continue
        if mx <= 0:
            continue
        if 'pass 71' in str(wo.cell(q, 24).value or ''):
            continue
        mA = re.search(r'Annual maintenance figure ([\d,.]+) GBP', m_note)
        A_note = float(mA.group(1).replace(',', '')) if mA else 0.0
        share, P = provision_from_note(m_note, A_note)
        if P <= 0:
            continue
        myrs = re.search(r'every ([\d.]+) years', m_note)
        years = float(myrs.group(1)) if myrs else YEARS_DEFAULT
        r_old = (first / mx) if mx else 0.333
        mid = P * years
        mid_old = (first + mx) / 2.0
        if abs(mid - mid_old) <= max(0.05, 0.005 * mid_old):
            continue
        mx_new = 2.0 * mid / (1.0 + r_old)
        first_new = r_old * mx_new
        if WRITE:
            wo.cell(q, 14, round(first_new, 1))
            wo.cell(q, 15, round(mx_new, 1))
            wo.cell(q, 24, str(wo.cell(q, 24).value or '') +
                    ' | pass 71: the event is sized to the provision at %g years (mid = %s x %g = '
                    '%s GBP), not to the whole annual figure; the first/max ratio is unchanged.'
                    % (years, f2(P), years, f2(mid)))
        stats['water_events'] += 1

    # 4. The pass 69 suffix: the true inherited distance, and the three restored markers.
    if os.path.exists(PRE69):
        pre = load_workbook(PRE69, data_only=False)['Rail vehicles']
        old = old_distances(pre)
    else:
        old = {}
    ws = wm['Rail vehicles']
    for r in range(7, ws.max_row + 1):
        note = str(ws.cell(r, 31).value or '')
        if 'pass 69:' not in note:
            continue
        base = str(ws.cell(r, 2).value or '')
        true_old = old.get(base)
        if not true_old:
            new = re.search(r'at mean annual distance ([\d,]+) km', note)
            true_old = '40,000' if new and new.group(1) == '65,000' else '109,000'
        fixed = re.sub(r'(pass 69: the inherited )([\d,]+)( km default is replaced)',
                       r'\g<1>%s\g<3>' % true_old, note, count=1)
        if fixed != note:
            if WRITE:
                ws.cell(r, 31, fixed)
            stats['suffix'] += 1
    # Classes 89, 90 and 91 lost the pass 69 marker when pass 66 rewrote their notes.
    for r in range(7, ws.max_row + 1):
        name = str(ws.cell(r, 1).value or '')
        if name not in ('BR Class 89', 'BR Class 90', 'BR Class 91 "Electra"'):
            continue
        note = str(ws.cell(r, 31).value or '')
        if 'pass 69' in note:
            continue
        if WRITE:
            ws.cell(r, 31, note.rstrip() +
                    ' | pass 69: the inherited 109,000 km default is replaced by the class and era '
                    'distance table (113,000 km at this introduction year); the fixed charge, the '
                    'provision and the overhaul event are unchanged.')
        stats['suffix'] += 1

    # 5. The three narrow-gauge locomotives on the inherited 109,000 km default.
    for r in range(7, ns.max_row + 1):
        name = str(ns.cell(r, 1).value or '').strip()
        if name not in NG_LOCOS:
            continue
        note = str(ns.cell(r, 31).value or '')
        if 'pass 71' in note:
            continue
        mK = re.search(r'at mean annual distance ([\d,]+) km', note)
        if not mK:
            continue
        try:
            intro = int(str(ns.cell(r, 5).value)[:4])
        except Exception:
            continue
        K_new = ev.mean_annual_km('locomotive', intro)
        if not K_new:
            continue
        mhead = re.search(r'the continuous head is the remainder, ([\d,.]+) GBP', note)
        msplit = re.search(r'split (\d+)/(\d+) fixed/per-km', note)
        myrs = re.search(r'The interval is ([\d.]+) years', note)
        q = ovh.get(str(ns.cell(r, 2).value or ''))
        if not (mhead and msplit and q):
            continue
        head = float(mhead.group(1).replace(',', ''))
        fixed_share = float(msplit.group(1)) / 100.0
        years = float(myrs.group(1)) if myrs else 7.0
        V = (1.0 - fixed_share) * head / K_new
        km_interval = int(round(years * K_new))
        if WRITE:
            ns.cell(r, 29).value = round(V, 10)
            wo.cell(q, 17, km_interval)
            wo.cell(q, 22, km_interval)
            out = re.sub(r'at mean annual distance [\d,]+ km a year',
                         'at mean annual distance %s km a year' % format(int(K_new), ','),
                         note, count=1)
            out = re.sub(r'The interval is [\d.]+ years = [\d,]+ km at that distance',
                         'The interval is %g years = %s km at that distance'
                         % (years, format(km_interval, ',')), out)
            out = re.sub(r'per-km [\d.]+ GBP per km', 'per-km %.10f GBP per km' % V, out)
            out = (out.rstrip() + ' | pass 71: the inherited %s km default is replaced by the class '
                   'and era distance table (%s km at this introduction year); the fixed charge, the '
                   'provision and the overhaul event are unchanged.'
                   % (mK.group(1), format(int(K_new), ',')))
            ns.cell(r, 31, out)
        stats['ng'] += 1

    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  suggested intervals synced: %d; tub-boat rows: %d; water events re-sized: %d; '
          'pass 69 suffixes corrected: %d; narrow-gauge locomotives: %d'
          % (stats['interval'], stats['tub'], stats['water_events'], stats['suffix'], stats['ng']))


if __name__ == '__main__':
    main()
