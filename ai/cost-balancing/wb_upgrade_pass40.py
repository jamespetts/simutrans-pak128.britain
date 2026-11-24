# -*- coding: utf-8 -*-
# wb_upgrade_pass40.py — assign upgrade_price (the sheet's S column, "Suggested upgrade GBP") on
# the "Overhauls & upgrades" sheet from the .dat upgrade[i] links and the measured upgrade rules.
#
# Rule sources: New/ai/vehicle-cost/maintenance-decomposition.md "Upgrade costs" and
# New/ai/cost-balancing/research-pricing-report-40.md §4. Mapping rule (the engine charges the
# TARGET's upgrade_price and deletes the old vehicle with no resale credit):
#   U = B + (C - V') + (V_old - R); case 2 (in-place works, V' = C) gives U = B.
# Shares are of the TARGET's capital except brake pairs, measured against the UNFITTED source
# (GBP 35 a carriage = 7.7% of the unfitted price). A target has ONE upgrade_price, so where a
# target has several inbound links the highest rule applies (printed in the basis).
#
# This script touches only column S and the upgrade sentence appended to column X of the
# Overhauls & upgrades sheet. Never rebuild the workbooks (build_workbooks.py warning).
import os
import re
import sys
from openpyxl import load_workbook


def find_base():
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-capital.xlsx')):
            return d
        p = os.path.dirname(d)
        if p == d:
            raise SystemExit('workspace root not found')
        d = p


BASE = find_base()
PATH = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')
FOLDERS = ['trains', 'bus', 'boats', 'air', 'trams', 'narrowgauge', 'maglev', 'london-underground']
MARK = 'upgrade (pass 40'
FORCE = '--force' in sys.argv

# --------------------------------------------------------------- extract links from .dat blocks
def extract():
    blocks = {}
    for folder in FOLDERS:
        d = os.path.join(BASE, 'New', folder)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith('.dat'):
                continue
            path = os.path.join(d, fn)
            try:
                text = open(path, encoding='latin-1').read()
            except Exception:
                continue
            for chunk in re.split(r'(?im)^obj=', text)[1:]:
                fields = {}
                for line in chunk.splitlines():
                    m = re.match(r'\s*([A-Za-z_0-9\[\]]+)\s*=\s*(.*)$', line)
                    if m and m.group(1) not in fields:
                        fields[m.group(1)] = m.group(2).strip()
                name = fields.get('name')
                if not name:
                    continue
                links = {}
                for k, v in fields.items():
                    m = re.match(r'upgrade\[(\d+)\]$', k)
                    if m:
                        links[int(m.group(1))] = v
                blocks[name] = {'file': folder + '/' + fn, 'links': links,
                                'engine': fields.get('engine_type', '')}
    inbound = {}
    for name, b in blocks.items():
        for _i, t in sorted(b['links'].items()):
            inbound.setdefault(t, []).append(name)
    return blocks, inbound


# --------------------------------------------------------------- rules
GOODS_WORDS = set('''cargo mail cool piece high density van open covered tank flat low barrel
timber livestock coal grain cattle milk fish reefer container express parcel horse box general
purpose goods perishable''' .split())
VARIANT_RE = re.compile(r'cargo|mail|cool|piece|high[- ]?density|covered|open|van|tank|flat|'
                        r'livestock|container|parcel|reefer|perishable', re.I)


def classify_link(src, tgt):
    sl, tl = src.lower(), tgt.lower()
    if re.search(r'unfit|plain|non[- ]?fit', sl) and re.search(r'fit|vacuum|air', tl):
        return 'brake'
    if re.search(r'renatus', tl):
        return 'renatus'
    if re.search(r'greenway', tl):
        return 'greenway'
    if re.search(r'repower|equipmake|\bzeb\b|battery', tl):
        return 'repower'
    if re.search(r'flex|769', tl):
        return 'flex'
    if re.search(r'mtu|re[- ]?engin', tl):
        return 'reengine'
    if re.search(r'extension|life[- ]?ext', tl):
        return 'lifeext'
    sw = set(re.split(r'[^a-z0-9]+', sl)) - {''}
    tw = set(re.split(r'[^a-z0-9]+', tl)) - {''}
    diff = (sw - tw) | (tw - sw)
    if not diff:
        return 'change'
    if all(w.isdigit() for w in diff):
        return 'subclass'
    if len(diff) <= 3 and all(re.search(r'(cargo|mail|cool|piece|high|density|covered|'
                                        r'open|van|tank|flat|livestock|container|parcel|'
                                        r'reefer|perishable|trolley|mk|type)', w, re.I)
                              for w in diff):
        return 'variant'
    return 'change'


# share of target capital, or ('source', share) to use the source's capital; min years for basis
RULES = {
    'brake':    ('source', 0.077, 'measured brake fitting: GBP 35 a carriage = 7.7% of the '
                                  'unfitted price (1879; the 1876 GBP 33 and 1881 GBP 5/10 '
                                  'conversions bracket it); wagons 10-20% (20-33% after 1922)'),
    'renatus':  ('target', 0.25, 'measured programme band: Class 321 Renatus GBP 500,000 a '
                                 'vehicle = 20-35% of a new EMU vehicle (re-traction/full refit)'),
    'greenway': ('target', 0.50, 'measured: Leyland National Greenway GBP 45,000 = about 50% of '
                                 'a new bus (1991)'),
    'repower':  ('target', 0.40, 'measured: Equipmake repower GBP 175,000 = 39-44% of a new '
                                 'e-bus (2023)'),
    'flex':     ('target', 0.25, 're-traction band (measured 20-25%: Class 455 GBP 109,890 a '
                                 'vehicle); 319-to-769 bi-mode conversion'),
    'reengine': ('target', 0.125, 'measured: HST power car re-engine 10-15% of new'),
    'lifeext':  ('target', 0.45, 'measured: Supertram life extension GBP 856,000 = 43-50% of new'),
    'variant':  ('target', 0.03, 'cabin/goods variant: 1-5% (interior or freight reconfiguration, '
                                 'not a type change); P2F at 4-8% of new list is the analogue'),
    'subclass': ('target', 0.12, 'MU sub-class variant (ESTIMATE between the measured bands: '
                                 'refresh 8-12%, re-traction 20-25%); direction: name the '
                                 'programme for each pair'),
    'change':   ('target', None, None),  # filled from folder below
}
CHANGE_SHARE = {'trains': ('target', 0.325, 'class default for an unidentified rail conversion: '
                                           '30-35% of the target (register rule; direction: name '
                                           'the programme)'),
                'london-underground': ('target', 0.325, 'as rail'),
                'narrowgauge': ('target', 0.325, 'as rail'),
                'trams': ('target', 0.45, 'tram structural conversions 45-50% (Supertram band)'),
                'bus': ('target', 0.50, 'bus/lorry full rebuild 50% (Bedford KM 52%, measured)'),
                'boats': ('target', 0.10, 'ship conversion/life-extension 10% (no measured '
                                          'conversion price; dry-dock cycles stay in overhaul)'),
                'air': ('target', 0.05, 'aircraft cabin-variant default 5% (P2F is a different '
                                        'event, measured at 4-8% of list)'),
                }


def rule_for(cls, src, tgt, folder):
    if cls == 'change':
        return CHANGE_SHARE.get(folder, CHANGE_SHARE['trains'])
    return RULES[cls]


def main():
    blocks, inbound = extract()
    wb = load_workbook(PATH)
    ws = wb['Overhauls & upgrades']
    row_of = {}
    for r in range(7, ws.max_row + 1):
        b = ws.cell(r, 2).value
        if b:
            row_of.setdefault(str(b), r)
    cap = {}
    for r in range(7, ws.max_row + 1):
        b = ws.cell(r, 2).value
        m = ws.cell(r, 13).value
        if b and isinstance(m, (int, float)):
            cap[str(b)] = m

    counts = {}
    updated = 0
    for tgt, srcs in sorted(inbound.items()):
        r = row_of.get(tgt)
        if r is None:
            continue
        x = str(ws.cell(r, 24).value or '')
        if MARK in x and not FORCE:
            continue
        M = cap.get(tgt)
        best_u, best_cls, best_basis = None, None, None
        for s in srcs:
            cls = classify_link(s, tgt)
            basis, share, note = rule_for(cls, s, tgt, (blocks.get(s) or {}).get('file', 'trains/').split('/')[0])
            if basis == 'source':
                Ms = cap.get(s)
                u = share * Ms if Ms else (share / 0.077 * 0.072 * (M or 0))
                note = note + ' (share of the unfitted partner %s)' % s
            else:
                u = share * (M or 0)
            if best_u is None or u > best_u:
                best_u, best_cls, best_basis = u, cls, note
        if M and best_u is not None and best_u > M:
            best_u = M  # cap: never above buying new
        ws.cell(r, 19, round(best_u, 1) if best_u is not None else None)
        note = ('upgrade (pass 40): %s; %s%s'
                % (best_cls, best_basis,
                   ' %d inbound links; one upgrade_price serves them all, the highest applies.' % len(srcs)
                   if len(srcs) > 1 else ''))
        ws.cell(r, 24, (x + ' | ' + note) if x else note)
        counts[best_cls] = counts.get(best_cls, 0) + 1
        updated += 1
    wb.save(PATH)
    print('upgrade targets updated:', updated)
    for k in sorted(counts):
        print('  %-10s %d' % (k, counts[k]))


if __name__ == '__main__':
    main()
