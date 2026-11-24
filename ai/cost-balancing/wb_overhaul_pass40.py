# -*- coding: utf-8 -*-
# wb_overhaul_pass40.py — write the pass-40 decomposition values into the "Overhauls & upgrades"
# sheet of New/cost-balancing-capital.xlsx, row by row.
#
# NEVER rebuild the workbooks (see build_workbooks.py warning): this script patches the sheet in
# place and touches no other sheet. Columns written: N first overhaul GBP, O max overhaul GBP,
# P overhauls to max, Q interval km, R downtime months, X basis. M (capital target) and S (upgrade)
# are left as they stand; the upgrade mapping is a separate step.
#
# Rules and their sources: New/ai/vehicle-cost/maintenance-decomposition.md and
# New/ai/cost-balancing/research-pricing-report-40.md (§1.1 wagon, §1.2 overhaul, §1.7 diesel/MU,
# §1.8 steam, §1.9 carriage era). Every written basis names its rung and what would move it.
#
# Convention: interval_km is the HISTORICAL distance between overhaul events (option (a) of the
# recorded trigger decision), from measured distance where it exists and years x class annual km
# where the source gives years. The assumed annual km is printed in each basis.
# Idempotent: rows already carrying the pass-40 marker are skipped unless --force.
import re
import sys
from openpyxl import load_workbook

BASE = None
for d in [__file__ and sys.path[0] or '.', '.']:
    pass


def find_base():
    import os
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-capital.xlsx')):
            return d
        p = os.path.dirname(d)
        if p == d:
            raise SystemExit('workspace root not found')
        d = p


PATH = find_base() + '/New/cost-balancing-capital.xlsx'
MARK = 'pass 40'
FORCE = '--force' in sys.argv

# ---------------------------------------------------------------- steam: Bond 1953 Table IV
# average miles between periodical repairs (classified works visits). Interval = this value,
# overhauls_before_max_cost = 2 (Hart-Davies: general at twice the periodical spacing).
BOND_MI = [
    (r'coronation|duchess|princess (royal|coronation)', 'Coronation/Duchess', {'coronation|duchess': 73188, 'princess': 169808}),
    (r'\ba[1234]\b|a[1234] |class a[1234]', 'LNER A1-A4', {'a1': 93363, 'a2': 85671, 'a3': 83574, 'a4': 86614}),
    (r'black five|class 5mt|5mt|stanier class 5|class 5 4-6-0', 'Black Five', None, 56969),
    (r'royal scot|5xp|class 5x|patriot', 'Royal Scot/5XP', None, 70495),
    (r'\b8f\b|class 8f|2-8-0 class 8', '8F', None, 50361),
    (r'king arthur|king arth', 'King Arthur', None, 70995),
    (r'\bking\b', 'King', None, 78987),
    (r'\bcastle\b', 'Castle', None, 87424),
    (r'\bhall\b', 'Hall', None, 87942),
    (r'\bcounty\b', 'County', None, 87588),
    (r'28xx|28-0|class 28', '28XX', None, 86981),
    (r'3150|81xx', '3150/81XX', None, 71720),
    (r'merchant navy', 'Merchant Navy', None, 75687),
    (r'west country', 'West Country', None, 74650),
    (r'lord nelson', 'Lord Nelson', None, 81611),
    (r'king arthur|king arth', 'King Arthur', None, 70995),
    (r'schools', 'Schools', None, 69851),
    (r'\bb1\b|class b1', 'B1', None, 78396),
    (r'\bv2\b|class v2', 'V2', None, 77892),
    (r'\bv[13]\b|class v[13]', 'V1/V3', None, 66500),
    (r'\bl1\b|class l1', 'L1', None, 67213),
    (r'\bo1\b|class o1', 'O1', None, 55616),
    (r'\bwd\b|war austerity|austerity', 'WD Austerity', None, 62624),
    (r'2-6-4t class 4|class 4 2-6-4', 'LMS 2-6-4T', None, 55579),
]
# BR Standard classes: months between shop repairs (Bond) x 40,000 km/yr assumed duty.
BRSTD_MONTHS = [
    (r'standard 7|class 7 |cl7|7mt 4-6-2', 15), (r'standard 6|class 6 |cl6|6mt 4-6-2', 18),
    (r'standard 5|class 5 |cl7|5mt 4-6-0|standard class 5', 24), (r'standard 4|class 4 |4mt', 28),
    (r'standard 3|class 3 |3mt', 33), (r'standard 2|class 2 |2mt', 36),
]
STEAM_ARCH = [
    (r'shunter|industrial|saddle|fireless|0-4-0|vertical|pocket|quarry|works|pug', 'industrial', 62500),
    (r'2-6-4|2-4-4|4-4-4|0-6-4|2-4-2|metro|tube|underground|pannier|2-6-2t|2-6-0t', 'suburban/metro tank', 130000),
    (r'2-8-0|2-8-2|2-10-0|0-6-0|2-6-0|goods|freight|mineral', 'heavy freight', 140000),
    (r'4-6-2|4-4-2|pacific|atlantic|express|4-6-0', 'express', 210000),
]
STEAM_DEFAULT = ('mixed traffic', 260000)


def steam_values(name):
    low = name.lower()
    for entry in BOND_MI:
        pat, label = entry[0], entry[1]
        if re.search(pat, low):
            if entry[2] is not None:  # dict of sub-patterns
                for sp, mi in entry[2].items():
                    if re.search(sp, low):
                        return mi * 1.60934, 'Bond 1953 Table IV: %s periodical-repair spacing %s mi' % (label, format(int(mi), ',')), 2
                return None
            mi = entry[3]
            return mi * 1.60934, 'Bond 1953 Table IV: %s periodical-repair spacing %s mi' % (label, format(int(mi), ',')), 2
    for pat, months in BRSTD_MONTHS:
        if re.search(pat, low):
            return months / 12.0 * 40000, 'BR Standard shop-repair rule: %d months (Bond 1953) at 40,000 km/yr' % months, 2
    for pat, label, km in STEAM_ARCH:
        if re.search(pat, low):
            return km, 'steam archetype %s (report 40 §1.8; rung 3/5 estimate)' % label, 2
    km, label = STEAM_DEFAULT[1], STEAM_DEFAULT[0]
    return km, 'steam archetype %s (report 40 §1.8; rung 3/5 estimate)' % label, 2


# ---------------------------------------------------------------- classes and era bands
WAGON_RE = re.compile(r'wagon|brake ?van|brakevan|plank|mineral|gondola|hop(per|e)|lowmac|conflat|'
                      r'bolster|cattle|sheep|box van|goods van|tank wagon|petrol|cement|silo|'
                      r'timber|grampus|seal|herring|catfish|\d+-ton|\d+ ton|four plank|five plank|'
                      r'six plank|seven plank|three plank|single plank|double plank|tar van|'
                      r'brake end|gunpowder|acid|van s|livestock', re.I)
MU_RE = re.compile(r'\b(dmu|emu)\b|multiple unit|-car unit|car unit|driving motor|driving trailer|'
                   r'motor coach|class (10[0-9]|11[0-9]|12[0-9]|14[0-9]|15[0-9]|16[0-9]|17[0-9]|'
                   r'18[0-9]|21[0-9]|22[0-9]|3[0-9][0-9]|4[0-9][0-9]|7[0-9][0-9]|8[0-9][0-9])\b', re.I)
DIESEL_K = [(r'class 37|\b37\b', 81000, 'Class 37'), (r'class 47|\b47\b', 113000, 'Class 47'),
            (r'class 55|deltic|\b55\b', 226000, 'Class 55'), (r'class 86|\b86\b', 176000, 'Class 86'),
            (r'class 87|\b87\b', 274000, 'Class 87')]


def diesel_values(name):
    low = name.lower()
    if re.search(r'power car|hst|class 43', low):
        return 150000, 3, ('HST power car: interval at the annual works visit (~150,000 km), rising '
                           'to the D event 252,000 mi at 3 rungs (report 40 §1.7)')
    if re.search(r'class 66|\b66\b', low):
        return 500000, 3, ('Class 66: heavy rebuild at 1.6M km modelled as 3 rungs from 500,000 km '
                           '(report 40 §1.7)')
    for pat, k, label in DIESEL_K:
        if re.search(pat, low):
            return 2.75 * k, 4, ('2.75-year works event at the measured class duty %s %s km/yr '
                                 '(TRB 1976-77), 4 rungs to the 11-year event (report 40 §1.7)' % (label, format(k, ',')))
    return 300000, 4, ('2.75-year works event at an assumed 109,000 km/yr class duty, 4 rungs to the '
                       '11-year event (report 40 §1.7; per-class k pending)')


def carriage_values(year):
    if year < 1890:
        return 160000, 0.09, 0.25, 2, 1.0, ('carriage-Victorian band (pass 40 §1.9): 4-6 yr ≈ 160,000 km; visits 9%, full renovation 25% '
                                            '(Lacy & Dow £62 ≈ 25% of capital); rung 3 interval, rung 1 share')
    if year < 1920:
        return 240000, 0.09, 0.225, 2, 1.0, ('carriage-Edwardian band (pass 40 §1.9): 5-7 yr ≈ 240,000 km; visits 9%, heavy 20-25% (ESTIMATE)')
    if year < 1948:
        return 130000, 0.08, 0.20, 2, 1.0, ('carriage-Grouping band (pass 40 §1.9): 3-4 yr ≈ 130,000 km (computed from GWR 1935 capacity); '
                                            'visits 8%, heavy 15-25% (ESTIMATE share)')
    if year < 1976:
        return 120000, 0.08, 0.26, 5, 0.7, ('carriage Mk 1/2 band (pass 40 §1.9): 2-yr coded visits ≈ 120,000 km at 25-50,000 mi/yr; '
                                            'C1 full renovation at the 5th visit (1965 code, years 9-11); 8% -> 26% (MEASURED ladder)')
    if year < 2005:
        return 500000, 0.06, 0.135, 2, 0.5, ('carriage Mk 3+ band (pass 40 §1.9): balanced ≈2 yr; heavy structural 10-12 yr ≈ 500,000 km; '
                                             '6% -> 13% (exam ladder M, shares EST)')
    return 450000, 0.08, 0.12, 2, 0.5, ('carriage modern band (pass 40 §1.9): heavy ≈950 days ≈ 450,000 km (STATED, paywall); 8% -> 12% (EST)')


def bus_values(year):
    if year < 1930:
        return 35000, 0.25, 0.25, 1, 0.5, ('bus pre-1930 band (pass 40 §1.9): annual overhaul (LGOC Chiswick, licence-driven) '
                                           '≈ 35,000 km at 35,000 km/yr; 25% (ESTIMATE — only the 1926 £14 paint figure is measured)')
    if year < 1965:
        return 120000, 0.15, 0.30, 2, 0.5, ('bus 1930-64 band (pass 40 §1.9): body overhaul 2-3 yr (LT 1947; Midland Red 2.5 yr) '
                                            '≈ 120,000 km at 40,000 km/yr; 15% -> 30% (ESTIMATE)')
    return 220000, 0.25, 0.40, 2, 0.5, ('bus modern band (pass 40 §1.9): Aldenham 4-yr cycle 220,000 km; 25% -> 40% '
                                        '(£2,000 = 25-33% of a new double-decker, 1965, MEASURED)')


def classify(name, dat, basis, profile, year):
    # Ship holds are priced zero and carry no overhaul (README: "holds zero").
    if '/holds/' in dat or dat.endswith('/holds'):
        return None
    # Tenders are overhauled with their engine: steam rule (Bond matching via the class in the
    # name). Guarded to the rail folders so ship tenders and boats stay on their own profiles.
    if (re.search(r'tender', dat, re.I) or re.search(r'tender', name, re.I)) and \
            dat.startswith(('trains/', 'london-underground/', 'narrowgauge/')):
        return 'steam'
    # Sailing craft (guarded to the boats folder): inshore/coastal versus deep-sea by name.
    if dat.startswith('boats/') and \
            re.search(r'sail|brig|schooner|wherry|smack|ketch|yawl|cutter|barque|brigantine|'
                      r'spritsail|yacht|windjammer|clipper|frigate|ship-rigged', name + ' ' + dat, re.I) and \
            not re.search(r'paddle|steam|motor|diesel|tug|with sail', name, re.I):
        if re.search(r'windjammer|clipper|frigate|barque|ship-rigged', name + ' ' + dat, re.I):
            return 'sailing-deep'
        return 'sailing-inshore'
    # The Comet 1 is a special case: its airframe was written off by pressurisation-cycle
    # fatigue, so its overhaul is replacement at 100% of the purchase price (user direction
    # 2026-11-24). The Comet 4 family must NOT take this rule.
    if 'dh-comet-1' in dat or re.search(r'\bcomet 1\b', name, re.I):
        return 'comet1'
    # Rows already carrying a pass-40 basis classify from its prefix (the profile string is gone).
    for prefix, k in (('steam (pass 40', 'steam'), ('diesel/electric (pass 40', 'diesel'),
                      ('MU ', 'mu'), ('carriage', 'carriage'), ('wagon (pass 40', 'wagon'),
                      ('bus ', 'bus'), ('lorry (pass 40', 'lorry'), ('tram ', 'tram'),
                      ('ship (pass 40', 'ship'), ('aircraft (pass 40', 'aircraft')):
        if basis.startswith(prefix) and 'pass 40' in basis:
            return k
    # Non-rail profiles resolve first: their names contain rail-like words ("3-ton", "van").
    for p, k in (('bus', 'bus'), ('lorry', 'lorry'), ('tram', 'tram'),
                 ('ship', 'ship'), ('aircraft', 'aircraft')):
        if profile == p:
            return k
    # The old "horse profile" bucket held three populations: the animals, horse-drawn vehicles,
    # and (misclassified) motor trailers and articulated bus sections. Horses and horse vehicles
    # wear out and take overhauls (user direction 2026-11-24): a horse's overhaul is the
    # replacement at the end of its working life.
    if profile == 'horse':
        if re.search(r'trailer', name, re.I):
            return 'trailer'
        if '(rear)' in name.lower():
            return 'bus'
        if 'mechanical horse' in name.lower():
            return 'lorry'
        if re.search(r'horse', name, re.I) and (dat.startswith('bus/horse-')
                                               or 'pack-horse' in dat or 'pack horse' in name.lower()):
            return 'horse-animal'
        return 'horse-vehicle'
    # Rail-family rows: wagons and MUs are distinguished by name within the loco/carriage profiles.
    if profile in ('carriage', 'locomotive', 'locomotive-steam', 'multiple-unit'):
        if WAGON_RE.search(name) or WAGON_RE.search(dat):
            return 'wagon'
        if MU_RE.search(name):
            return 'mu'
        if profile == 'locomotive-steam':
            return 'steam'
        if profile == 'locomotive':
            return 'diesel'
        if profile == 'multiple-unit':
            return 'mu'
        return 'carriage'
    return None


def main():
    import os
    wb = load_workbook(PATH)
    ws = wb['Overhauls & upgrades']
    counts = {}
    changed = 0
    for r in range(7, ws.max_row + 1):
        name = ws.cell(r, 1).value
        if not name:
            continue
        dat = str(ws.cell(r, 3).value or '')
        basis = str(ws.cell(r, 24).value or '')
        if MARK in basis and not FORCE:
            continue
        profile_m = re.match(r'([a-z\- ]+) profile:', basis)
        profile = profile_m.group(1).strip() if profile_m else ''
        yv = ws.cell(r, 5).value
        try:
            year = int(str(yv)[:4])
        except Exception:
            year = 1900
        kind = classify(str(name), dat, basis, profile, year)
        if kind is None:
            continue
        M = ws.cell(r, 13).value
        M = M if isinstance(M, (int, float)) else None
        if kind == 'steam':
            v = steam_values(str(name))
            if v is None:
                continue
            km, why, rungs = v
            q, first, mx, p, downtime = km, 0.05, 0.15, rungs, 1.5
            tag = ('steam (pass 40): interval %s km between classified works visits (%s); events 5%% -> 15%% '
                   'of capital (heavy general measured 9-14%% at GWR 28xx), %d rungs to the general; 1.5 months '
                   'in works (Crewe avg 24 d). Direction: class record cards / Bond Table IV.' % (format(int(km), ','), why, p))
        elif kind == 'diesel':
            km, rungs, why = diesel_values(str(name))
            q, first, mx, p, downtime = km, 0.07, 0.20, rungs, 0.8
            tag = ('diesel/electric (pass 40): interval %s km, events 7%% -> 20%%, %d rungs; %s' % (format(int(km), ','), p, why))
        elif kind == 'mu':
            low = str(name).lower()
            if re.search(r'class (700|707|717|720|745|755|769|777|800|801|802|810)', low):
                q, first, mx, p, downtime = 450000, 0.08, 0.12, 1, 0.5
                tag = ('MU third-gen (pass 40): 950-day heavy event ≈ 450,000 km (STATED, Modern Railways 2018 paywall '
                       'extraction); 8% -> 12% (ESTIMATE). Direction: any IET heavy-overhaul contract value.')
            elif re.search(r'class (10[0-9]|11[0-9]|12[0-9]|14[0-9]|2[0-9][0-9]|30[0-9]|31[0-5])|dmu', low):
                q, first, mx, p, downtime = 200000, 0.08, 0.20, 2, 0.5
                tag = ('MU first-gen (pass 40): 2-year works visit ≈ 200,000 km (Hornsey regime, forum #267); top exam '
                       '5-yearly (BR 87264/1); events 8% -> 20% (ESTIMATE shares). C4 measured mileages where known.')
            else:
                q, first, mx, p, downtime = 480000, 0.08, 0.20, 2, 0.5
                tag = ('MU second-gen (pass 40): C4 at 4 yr ≈ 480,000 km (measured C4 mileages: 150 325k mi, 153/156 350k, '
                       '357 450k), rungs to C6; events 8% -> 20% pending the MU purchase ladder.')
        elif kind == 'wagon':
            q, first, mx, p, downtime = 240000, 0.12, 0.20, 3, 0.5
            tag = ('wagon (pass 40): 6-year heavy/contract cycle ≈ 240,000 km at an assumed 40,000 km/yr wagon duty '
                   '(k-dependent); events 12% -> 20%, 3 rungs (composed from 7-yr repair contracts, 4-6-yr POH analogue, '
                   'reconciled with measured £5-£5 8s 6d/wagon-yr contracts). The annual light works visit (NER 1892: '
                   '0.95/wagon-yr) belongs to routine cost. Direction: RCH per-job schedules; a wagon overhaul invoice.')
        elif kind == 'horse-animal':
            q, first, mx, p, downtime = 70000, 1.0, 1.0, 1, 0.1
            tag = ('horse (pass 40): the overhaul is the replacement of the horse at the end of its '
                   'working life (user direction 2026-11-24). Measured renewal cadence: the Leeds '
                   'tramway horses were renewed about once every 7 years at a cost equal to the '
                   'purchase price (1894-5 accounts, forum 6521 #116); 7 yr = 70,000 km at an '
                   'assumed 10,000 km/yr (k-dependent). Keep is the routine cost and carries no '
                   'renewal element.')
        elif kind == 'horse-vehicle':
            q, first, mx, p, downtime = 50000, 0.15, 0.30, 2, 0.5
            tag = ('horse vehicle (pass 40): rebuilding wheels, axles, springs, bodywork and paint; '
                   'ESTIMATE 5 yr = 50,000 km at an assumed 10,000 km/yr (k-dependent); 15% -> 30% '
                   '(carriage-era analogue: the Lacy & Dow event at 25% of capital). Direction: '
                   'coaching and omnibus accounts (Hanforth type), preserved practice.')
        elif kind == 'trailer':
            q, first, mx, p, downtime = 160000, 0.10, 0.25, 2, 0.5
            tag = ('trailer (pass 40): lorry-cadence attention without the engine element; 160,000 km, '
                   '10% -> 25% (ESTIMATE from the lorry bands). Direction: trailer maintenance '
                   'schedules.')
        elif kind == 'carriage':
            q, first, mx, p, downtime, why = carriage_values(year)
            tag = why
        elif kind == 'bus':
            q, first, mx, p, downtime, why = bus_values(year)
            tag = why
        elif kind == 'lorry':
            q, first, mx, p, downtime = 160000, 0.10, 0.30, 2, 0.5
            tag = ('lorry (pass 40): engine exchange at 100-250k mi is the intermediate event (interval 160,000 km), '
                   'complete overhaul 250,000 mi at the 2nd event (CM 1960/69, MEASURED); 10% -> 30%.')
        elif kind == 'tram':
            if year < 1950:
                q, first, mx, p, downtime = 200000, 0.10, 0.22, 2, 0.5
                tag = ('tram pre-1950 (pass 40): no measured interval (report 40 §1.9); ESTIMATE 5 yr ≈ 200,000 km at '
                       '40,000 km/yr; events 10% -> 22% (E/1 £400 a tram 1934 against ~£1,500-2,000 new).')
            else:
                q, first, mx, p, downtime = 600000, 0.08, 0.45, 3, 0.5
                tag = ('tram modern (pass 40): 12-yr mid-life 600,000 km (Metrolink £80,000; Supertram extension '
                       '£856,000, MEASURED); 8% -> 45%.')
        elif kind == 'sailing-deep':
            q, first, mx, p, downtime = 500000, 0.03, 0.10, 3, 0.8
            tag = ('sailing ship, deep-sea (pass 40): Lloyd\'s-classed like steamers, 5-year special '
                   'survey cycle at the duty of the ocean trades (ESTIMATE 5 yr = 500,000 km at an '
                   'assumed 100,000 km/yr, k-dependent); hull survey and refit 3% -> 10% (between '
                   'the motor-ship band and the wooden refit band; measured analogue: "Earl of '
                   'Esce" overhaul GBP 1,100 against GBP 4,154 new, 1877 = 26% at 18 years). '
                   'Refit share carved OUT of the Martin 5% annual provision at the costing pass. '
                   'Direction: RMG barque accounts (ELEANOR DODSON AMS/36; BURNS MSS/77/063).')
        elif kind == 'sailing-inshore':
            q, first, mx, p, downtime = 175000, 0.05, 0.15, 3, 0.8
            tag = ('sailing boat, inshore/coastal (pass 40): hull, rig and spar refits (re-planking, '
                   're-masting, re-rigging, sheathing); ESTIMATE 5 yr = 175,000 km at an assumed '
                   '35,000 km/yr (k-dependent); 5% -> 15% (measured analogue: "Earl of Essex" 26% '
                   'at 18 years). Refit share carved OUT of the Martin 5%-of-capital annual '
                   'provision at the costing pass. Direction: RMG barque accounts; coastal trader '
                   'histories.')
        elif kind == 'ship':
            q, first, mx, p, downtime = 575000, 0.02, 0.05, 6, 0.4
            tag = ('ship (pass 40): 5-year special survey ≈ 575,000 km (200-250 sea-days at 9-12 kn, ESTIMATE — the '
                   'engine triggers on distance only; time basis is measured); 2% -> 5% (bare survey+dock <1.5%, with '
                   'steel renewal 3-9%).')
        elif kind == 'comet1':
            q, first, mx, p, downtime = 1790000, 1.0, 1.0, 1, 0.8
            tag = ('Comet 1 (pass 40): the overhaul is REPLACEMENT at the pressurisation-cycle '
                   'fatigue limit, 100% of the purchase price (user direction 2026-11-24; the '
                   'airframe could not withstand many pressurisation cycles). Measured limit '
                   'about 1,000 pressurisation cycles (G-ALYP failed on its 1,286th pressurised '
                   'flight, G-ALYY on her 903rd; FAA: production Comets formed fatigue cracks at '
                   'approximately 1,000 flight cycles; the RAE tank airframe failed at 3,060 '
                   'total, about 2,500 service-equivalent; the design assumption had been 10,000). '
                   '1,000 cycles at the measured BOAC mean sector 1,790 km = 1,790,000 km '
                   '(sector-dependent: shorter sectors reach the cycle limit sooner per km). '
                   'C.A.P. 127 (1955); RAE Accident Note 270. The Comet 4 and 1XB must not carry '
                   'this rule (redesigned structure, safe life tens of thousands of hours).')
        elif kind == 'aircraft':
            q, first, mx, p, downtime = 4200000, 0.025, 0.05, 4, 0.8
            tag = ('aircraft (pass 40): one C-check every 4,000-6,000 FH ≈ 4,200,000 km at cruise (ESTIMATE — real duty; '
                   'the open trigger decision may rescale to in-game duty); heavy check 0.8-1.1% of new airframe, cycle '
                   'with engines/gear 2-5%; 4 rungs.')
        if M:
            ws.cell(r, 14, round(M * first, 1))
            ws.cell(r, 15, round(M * mx, 1))
        ws.cell(r, 16, p)
        ws.cell(r, 17, int(q))
        ws.cell(r, 18, downtime)
        ws.cell(r, 24, tag)
        counts[kind] = counts.get(kind, 0) + 1
        changed += 1
    wb.save(PATH)
    print('rows updated:', changed)
    for k in sorted(counts):
        print('  %-10s %d' % (k, counts[k]))


if __name__ == '__main__':
    main()
