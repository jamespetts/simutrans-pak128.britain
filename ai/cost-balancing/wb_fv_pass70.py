# -*- coding: utf-8 -*-
# wb_fv_pass70.py - price the water objects on the measured gross-tonnage ladder.
#
# WHY THIS PASS EXISTS
# The workbook has priced every water object per unit of payload: 66 GBP a passenger for a
# sea-going ferry, 8.5 GBP a cargo tonne, 32 GBP a tonne for steam inland craft. Those rates are
# not in research report 25; they are report 25's per-gross-ton price divided by an assumed
# number of gross tons per passenger or per cargo tonne. Research pass 56 shows the assumption is
# route-dependent and spans 0.80 to 188.9 gross tons per capacity tonne across the 39 identified
# vessels, so the per-payload ladder cannot scale with the hull around the payload. On the 57
# rows with a sourced tonnage the per-payload target is a median 0.30 of the per-gross-ton
# figure.
#
# The 2026-11-25 decision is to use the gross-tonnage ladder. This pass applies the measured
# capital rates:
#   passenger vessels (ferries and river boats)  84.1 x GT^0.90
#   cargo ships and coasters                     GBP 35 a gross ton
#   inland craft (barges and narrowboats)       GBP 17 a gross ton
#   tugs                                        GBP 39 a gross ton (report 25 s9.4, one point)
#   fishing and small craft                     GBP 17 a gross ton (the nearest measured
#                                               per-gross-ton rate; report 56 left them blank
#                                               for want of a tonnage, not of a rate)
# Hovercraft and holds keep their current rules: an air-cushion vehicle has no gross tonnage,
# and a hold is a container inside a parent whose tonnage is already charged on the parent row.
#
# TONNAGE
# water-gross-tonnage.csv (pass 56) plus water-gross-tonnage-additions.csv (pass 57, where it
# exists). A row with no figure takes report 56's bridge: inland 1.2 gross tons per capacity
# tonne, river 6.2, cargo 1.6. The bridge is recorded as ESTIMATE on the row.
#
# WHAT MOVES
# The capital target, and with it the 2 per cent annual repair figure and the overhaul event,
# which are shares of capital. The overhaul provision share, the five-year interval and the
# downtime are unchanged; the event is scaled by the same factor as the capital.
#
# Run: py -3 wb_fv_pass70.py [--write]. Dry run by default. Idempotent by the pass 70 marker.
import csv
import math
import os
import re
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pass 70'
WRITE = '--write' in sys.argv
REPAIR_SHARE = 0.02
BRIDGE = {'barge': 1.2, 'narrowboat': 1.2, 'river-boat': 6.2, 'cargo': 1.6, 'coaster': 1.6}


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
CSV1 = os.path.join(HERE, 'water-gross-tonnage.csv')
CSV2 = os.path.join(HERE, 'water-gross-tonnage-additions.csv')


def f2(x):
    if abs(x - round(x)) < 0.005:
        return format(int(round(x)), ',')
    return format(round(x, 2), ',')


def load_tonnage():
    out = {}
    for path in (CSV1, CSV2):
        if not os.path.exists(path):
            continue
        with open(path, encoding='utf-8-sig') as f:
            for r in csv.DictReader(f):
                gt = (r.get('gross_tonnage') or '').strip()
                v = 0.0
                if gt:
                    try:
                        v = float(gt.replace(',', ''))
                    except ValueError:
                        v = 0.0
                key = r['name'].lower()
                cur = out.get(key, {})
                kind = (r.get('kind') or '').strip().lower() or cur.get('kind', '')
                out[key] = {
                    'gt': v,
                    'kind': kind,
                    'method': (r.get('method') or '').strip().lower() or cur.get('method', ''),
                    'definition': (r.get('gross_tonnage_definition') or '').strip() or cur.get('definition', ''),
                    'year': (r.get('year') or '').strip() or cur.get('year', ''),
                    'grade': (r.get('evidence_grade') or '').strip() or cur.get('grade', ''),
                    'identity': (r.get('identity') or '').strip() or cur.get('identity', ''),
                    'source': (r.get('source_url') or '').strip() or cur.get('source', ''),
                    'type': (r.get('type') or '').strip().lower() or cur.get('type', ''),
                    'size': (r.get('total_size_t') or '').strip() or cur.get('size', ''),
                }
    return out


def rate_for(kind, gt):
    """(capital GBP, class label) or (None, reason) where no per-gross-ton rate applies."""
    if kind in ('ferry', 'river-boat'):
        return 84.1 * (gt ** 0.90), 'passenger 84.1 x GT^0.90'
    if kind in ('cargo', 'coaster'):
        return 35.0 * gt, 'cargo GBP 35/GT'
    if kind in ('barge', 'narrowboat'):
        return 17.0 * gt, 'inland GBP 17/GT'
    if kind == 'tug':
        return 39.0 * gt, 'tug GBP 39/GT'
    if kind == 'other':
        return 17.0 * gt, 'small craft at the inland GBP 17/GT rate (nearest measured)'
    return None, 'no per-gross-ton rate for this type'


def main():
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    cs = wc['Water vehicles']
    ms = wm['Water vehicles']
    ton = load_tonnage()
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r

    stats = {'rows': 0, 'skipped': 0, 'bridged': 0, 'keep': 0, 'missing': 0}
    samples = []
    for r in range(7, cs.max_row + 1):
        name = str(cs.cell(r, 1).value or '').strip()
        base = str(cs.cell(r, 2).value or '').strip()
        if not name:
            continue
        note = str(cs.cell(r, 24).value or '')
        if MARK in note:
            stats['skipped'] += 1
            continue
        key = base.lower()
        info = ton.get(key)
        kind = (info or {}).get('type') or ''
        if not kind:
            # The tonnage file keys on the pakset name; fall back to the row's own basis text.
            kind = ''
        kind = kind.lower()
        if not info:
            # Try the English name as the key (the CSVs use the pakset name).
            info = ton.get(name.lower())
        if info and not kind:
            kind = (info.get('type') or '').lower()
        if not kind:
            stats['missing'] += 1
            continue
        # A hold is a container inside a parent vehicle: its tonnage belongs to the parent and
        # is already charged on the parent's row. Horses on the water sheet take the animal rule.
        if 'horse' in name.lower():
            if WRITE:
                cs.cell(r, 24, str(cs.cell(r, 24).value or '') +
                        ' | pass 70: not a vessel (a towing horse); the animal rule of 45 GBP an '
                        'animal-year stands.')
            stats['keep'] += 1
            continue
        if info and info.get('kind') == 'hold':
            if WRITE:
                cs.cell(r, 24, str(cs.cell(r, 24).value or '') +
                        ' | pass 70: a hold is a container inside a parent vehicle; the parent\'s '
                        'gross tonnage is charged on the parent\'s row, so the hold keeps its 1 '
                        'per cent rule and takes no per-gross-ton price.')
            stats['keep'] += 1
            continue
        if name.lower().startswith('towpath'):
            if WRITE:
                cs.cell(r, 24, str(cs.cell(r, 24).value or '') +
                        ' | pass 70: not a vessel; the road/animal rule stands.')
            stats['keep'] += 1
            continue
        gt = info['gt'] if info else 0.0
        grade = info['grade'] if info else 'ESTIMATE'
        definition = info['definition'] if info else 'bridge'
        identity = info['identity'] if info else ''
        year = info['year'] if info else ''
        bridged = False
        if not gt:
            if kind == 'hovercraft':
                if WRITE:
                    cs.cell(r, 24, str(cs.cell(r, 24).value or '') +
                            ' | pass 70: an air-cushion vehicle has no gross register tonnage; '
                            'the capacity rule of 40 GBP a passenger stands.')
                stats['keep'] += 1
                continue
            # Respect the research: a row the tonnage pass examined and left blank with a
            # reason (an unidentified hull, or a fit whose capacity bridge would price one hull
            # at three different sizes) is not bridged here. Only a row the pass itself bridged,
            # or one the tonnage file does not cover, may take the bridge.
            method = (info or {}).get('method', '')
            if method.startswith('unavailable'):
                if WRITE:
                    cs.cell(r, 24, str(cs.cell(r, 24).value or '') +
                            ' | pass 70: research pass 57 examined this row and left the gross '
                            'tonnage blank (' + method.replace('unavailable-', '') + '); the '
                            'capacity rule stands.')
                stats['keep'] += 1
                continue
            ratio = BRIDGE.get(kind)
            try:
                size = float(info['size']) if info and info.get('size') else 0.0
            except ValueError:
                size = 0.0
            if ratio and size > 0:
                gt = ratio * size
                grade = 'ESTIMATE'
                definition = 'bridge'
                identity = 'type bridge %g gross tons per capacity tonne on %.1f capacity tonnes' \
                           % (ratio, size)
                year = ''
                bridged = True
            else:
                if WRITE:
                    if kind == 'hovercraft':
                        why = ('an air-cushion vehicle has no gross register tonnage; the capacity '
                               'rule of 40 GBP a passenger stands')
                    else:
                        why = ('research pass 57 could not establish a gross tonnage for this type '
                               'and the sources are archive-only (research-pricing-report-57 '
                               'section 6); the capacity rule stands')
                    cs.cell(r, 24, str(cs.cell(r, 24).value or '') + ' | pass 70: ' + why + '.')
                stats['keep'] += 1
                continue
        cap_new, label = rate_for(kind, gt)
        if cap_new is None:
            stats['keep'] += 1
            continue
        # Capital target, the current value and the scale factor.
        try:
            cap_old = float(cs.cell(r, 22).value)
        except (TypeError, ValueError):
            stats['missing'] += 1
            continue
        if cap_old <= 0:
            stats['missing'] += 1
            continue
        k = cap_new / cap_old
        q = ovh.get(base)

        # Maintenance: A is 2 per cent of capital; the provision share is the row's existing
        # share of A, so the split and the interval do not change, only their size.
        m_note = str(ms.cell(r, 31).value or '')
        mA = re.search(r'Annual maintenance figure ([\d,.]+) GBP', m_note)
        mP = re.search(r'provision \(([\d,.]+)\) = ([_\d,.]+)', m_note.replace('_', ''))
        A_old = float(mA.group(1).replace(',', '')) if mA else REPAIR_SHARE * cap_old
        P_old = float(mP.group(1).replace(',', '')) if mP else 0.35 * A_old
        share = (P_old / A_old) if A_old else 0.35
        A_new = REPAIR_SHARE * cap_new
        P_new = share * A_new
        H_new = A_new - P_new
        ev_first = None
        ev_max = None
        if q:
            try:
                ev_first = float(wo.cell(q, 14).value) * k
                ev_max = float(wo.cell(q, 15).value) * k
            except (TypeError, ValueError):
                ev_first = ev_max = None

        cap_note = (
            'water (pass 70, per-gross-ton capital ladder): %s gross tons (%s%s), priced at %s. '
            'The three per-gross-ton rates are the measured capital prices of research report 25 '
            '(84.1 x GT^0.90 is the 14-vessel passenger fit deflated to 1900 money; GBP 17/GT is '
            'Cambria 1906; GBP 35/GT is the British Railways 1950-53 cargo price), established by '
            'research report 56 and applied by the 2026-11-25 decision. The identity is %s, so '
            'the capital target is %s GBP at 1900. Repair is 2 per cent of capital a year. The '
            'per-payload ladder this replaces is a conversion of the same fit at an assumed gross '
            'tonnage per capacity unit. | pass 70'
            % (format(round(gt, 1), ','), definition or 'tonnage', (', ' + year) if year else '',
               label, identity or 'recorded on the row', f2(cap_new)))

        if WRITE:
            cs.cell(r, 22, round(cap_new, 2))
            cs.cell(r, 23, 1900)
            cs.cell(r, 24, cap_note)
            ms.cell(r, 27, round(H_new, 2))
            ms.cell(r, 29, None)
            ms.cell(r, 31, (
                'Maintenance decomposition (pass 70, per-gross-ton capital ladder). Annual '
                'maintenance figure %s GBP per vessel-year in 1900 money, being 2 per cent of the '
                'per-gross-ton capital target of %s GBP. The level evidence is the 1850 General '
                'Steam Navigation repair bill (GBP 31,896 for 44 vessels = GBP 788 a vessel-year; '
                'research-pricing-report-15 section 3.1), and 2 per cent is that report\'s '
                '1900-1920 share band, of which the 1913 liner overhaul alone is 2 per cent '
                '(Kirkaldy 1914, p. 211). Composition unrecorded: no source states whether the 2 '
                'per cent covers routine repairs, overhauls, renewals or all three. Renewals are '
                '0 per cent = 0 GBP a year (nothing is deducted; the measured total is the '
                'envelope). The measured total is the envelope: the works-overhaul provision is '
                '%s per cent of A = %s GBP a year, and the continuous head is the remainder, %s '
                'GBP a year, so the head plus the amortised events equals the net total. Nothing '
                'is split per kilometre: the upkeep is a standing charge. Pass 70 re-bases A and '
                'the event on the per-gross-ton capital (a factor of %s on the previous target). '
                'Hovercraft and holds keep their current rules and are not re-based. | pass 51 | '
                'pass 70' % (f2(A_new), f2(cap_new), f2(100.0 * share), f2(P_new), f2(H_new),
                             ('%.3f' % k).rstrip('0').rstrip('.'))))
            if q and ev_first is not None:
                wo.cell(q, 14, round(ev_first, 1))
                wo.cell(q, 15, round(ev_max, 1))
                wo.cell(q, 24, str(wo.cell(q, 24).value or '') +
                        ' | pass 70: the event is scaled by %.3f with the per-gross-ton capital '
                        'target; the interval and the provision share are unchanged.'
                        % k)
        stats['rows'] += 1
        if bridged:
            stats['bridged'] += 1
        if len(samples) < 12:
            samples.append((name, kind, gt, cap_old, cap_new, k, grade))
    if WRITE:
        wm.save(MAINT)
        wc.save(CAP)
    print('DRY RUN (no workbook changed)' if not WRITE else 'WRITTEN')
    print('  water rows re-based: %d; bridged: %d; kept on their current rule: %d; already '
          'marked: %d; missing: %d'
          % (stats['rows'], stats['bridged'], stats['keep'], stats['skipped'], stats['missing']))
    for s in samples:
        print('  %-34s %-11s GT=%9s  %10s -> %10s  x%.2f  %s'
              % (s[0][:34], s[1], format(int(round(s[2])), ','), f2(s[3]), f2(s[4]), s[5], s[6]))


if __name__ == '__main__':
    main()
