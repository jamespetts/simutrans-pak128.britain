# -*- coding: utf-8 -*-
# wb_audit_coherence.py — check every vehicle row for the two failures that the cost-balancing
# work keeps producing: a class left with no overhaul target, and a split that does not add up.
#
# WHY THIS EXISTS
# The workbooks are patched class by class, and two whole classes were found with the same
# defect: the narrow-gauge vehicles had no overhaul row at all (so the game charged no overhaul
# ever), and the locomotives had a capital-share overhaul charged on top of a measured annual
# total that already contained it (so the game charged up to 2.8 times the measured cost).
# Neither produced an error cell, a negative number or any other visible symptom. This script
# checks the two invariants directly and fails loudly instead.
#
# THE INVARIANTS (maintenance-decomposition.md, standing rule 0)
#   1. COVERAGE. Every vehicle in a maintenance sheet has a row in Overhauls & upgrades. A vehicle
#      with no overhaul row is never overhauled in game.
#   2. A DIVIDED FIGURE. Every vehicle carries either a positive overhaul target or an explicit
#      statement that it needs none (a zero-priced hold, a multi-part section). A zero target
#      with no such statement is a silent omission.
#   3. COHERENCE. Where the note states a measured annual figure A and an overhaul provision, the
#      continuous head plus the amortised provision equals A less the renewals deducted:
#          head + provision = A - renewals
#      A row that fails this is charging its components twice or not at all, however plausible
#      each component looks on its own.
#
# Run: py -3 wb_audit_coherence.py [--verbose] [--notes]. Exit code 1 on any failure.
import os
import re
import sys

from openpyxl import load_workbook

VERBOSE = '--verbose' in sys.argv
NOTES = '--notes' in sys.argv
VEHICLE_SHEETS = ('Rail vehicles', 'Narrow gauge vehicles', 'Road vehicles', 'Tram vehicles',
                  'Water vehicles', 'Air vehicles', 'Maglev vehicles')


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


def num(pattern, text):
    m = re.search(pattern, text)
    if not m:
        return None
    try:
        return float(m.group(1).replace(',', ''))
    except ValueError:
        return None


def first_of(patterns, text):
    for p in patterns:
        m = re.search(p, text)
        if m:
            try:
                return float(m.group(1).replace(',', ''))
            except (ValueError, IndexError):
                continue
    return None


def envelope_from_note(note):
    """(A, renewals, provision, head) where the note states them, else None per field."""
    A = first_of((r'Annual maintenance figure ([\d,.]+) GBP',
                  r'Maintenance is a nominal [\d.]+ per cent of the hold\'s own capital target '
                  r'\([\d,.]+ GBP\) = ([\d,.]+) GBP a year'), note)
    # The deduction the source supports is renewals in some classes and the overhaul in others;
    # the pass-42 template calls both "Deducted". Read the explicit renewal phrases first, then
    # the pass-51 arithmetic, then take "Deducted" as the overhaul only where the note says the
    # figure contains major repairs.
    rho = first_of((r'Renewals are [\d.]+ per cent of this figure = ([\d,.]+) GBP',
                    r'Head = A - renewals \(([\d,.]+)\)',
                    r'renewals at 25 per cent = ([\d,.]+) GBP',
                    r'Renewals are 25 per cent = ([\d,.]+) GBP',
                    r'Renewals are [\d.]+ per cent = ([\d,.]+) GBP',
                    r'renewals [\d.]+ per cent = ([\d,.]+) GBP'), note)
    if rho is None:
        rho = 0.0
    prov = first_of((r'provision (?:of research pass 44 )?is [\d.]+ per cent of the (?:same )?'
                     r'figure = ([\d,.]+) GBP',
                     r'provision is [\d.]+ per cent of A = ([\d,.]+) GBP',
                     r'works-overhaul provision is [\d.]+ per cent of the gross figure = '
                     r'([\d,.]+) GBP',
                     r'annual share ([\d,.]+) GBP coming out of the figure',
                     r'works-overhaul provision is [\d.]+ per cent of the same figure = '
                     r'([\d,.]+) GBP',
                     r'- provision \(([\d,.]+)\)',
                     r'works-overhaul provision is 15 per cent of it = ([\d,.]+) GBP',
                     r'works-overhaul provision [\d.]+ per cent = ([\d,.]+) GBP',
                     r'annualised overhaul provision of ([\d,.]+) GBP a year is deducted'), note)
    if prov is None and A is not None:
        share = num(r'in the [^:]+ band \([^)]+\): ([\d.]+) per cent of this head is deducted',
                    note)
        if share is None:
            share = num(r': ([\d.]+) per cent of this head is deducted', note)
        if share is not None:
            prov = share / 100.0 * A
    if prov is None and ('overhaul' in note.lower() or 'major repairs' in note.lower()):
        prov = first_of((r'Deducted: (?:GBP )?([\d,.]+) a year, being [\d.]+ per cent of this '
                         r'head',
                         r'the provision is now ([\d,.]+) GBP a year'), note)
    head = first_of((r'continuous head is the remainder, ([\d,.]+) GBP',
                     r'the head is the remainder, ([\d,.]+) GBP',
                     r'provision \([\d,.]+\) = ([\d,.]+) GBP a year',
                     r'the continuous head is 0\.8 x [\d,.]+ = ([\d,.]+) GBP',
                     r'the continuous head is \(1 - [\d.]+\) x [\d,.]+ = ([\d,.]+) GBP',
                     r'the continuous head is ([\d,.]+) GBP, split',
                     r'the head is ([\d,.]+) GBP a year',
                     r'Routine remainder ([\d,.]+) GBP a year'), note)
    if head is None and A is not None:
        if ('the whole figure is the fixed charge' in note
                or 'the whole figure is the standing charge' in note
                or 'written whole as the class figure' in note
                or ('A hold is a container' in note and 'overhaul target is zero' in note)):
            head = A
            prov = 0.0
            rho = 0.0
    return A, rho, prov, head


def main():
    wm = load_workbook(MAINT, data_only=False)
    wc = load_workbook(CAP, data_only=False)
    wo = wc['Overhauls & upgrades']
    ovh = {}
    for r in range(7, wo.max_row + 1):
        b = wo.cell(r, 2).value
        if b:
            ovh[str(b)] = r

    fails = []
    unchecked = []
    zero_sections = []
    warnings = []
    checked = 0
    vehicles = 0
    for sheet in VEHICLE_SHEETS:
        if sheet not in wm.sheetnames:
            continue
        ws = wm[sheet]
        for r in range(7, ws.max_row + 1):
            name = str(ws.cell(r, 1).value or '')
            if not name:
                continue
            vehicles += 1
            base = str(ws.cell(r, 2).value or '')
            note = str(ws.cell(r, 31).value or '')
            q = ovh.get(base)
            # 1. coverage
            if q is None:
                fails.append(('no overhaul row', sheet, name, base))
                continue
            first = wo.cell(q, 14).value
            mx = wo.cell(q, 15).value
            km = wo.cell(q, 17).value
            cap = wo.cell(q, 13).value
            basis = str(wo.cell(q, 24).value or '')
            # A zero target is correct only where the vehicle itself is zero-priced: the rear and
            # centre sections of a multi-part unit, and tenders, have cost=0 in the .dat and the
            # leading unit carries the consist. Anything else needs a reasoning.
            zero_stated = ((isinstance(cap, (int, float)) and cap == 0)
                           or 'no overhaul' in basis or 'multi-part section' in basis
                           or 'articulated' in basis or 'leading unit carries' in basis
                           or 'the leading section carries' in basis)
            A0 = num(r'Annual maintenance figure ([\d,.]+) GBP', note) or 0.0
            if isinstance(cap, (int, float)) and cap == 0 and A0 > 0:
                fails.append(('maintenance charged on a zero-priced section (A=%.1f)' % A0,
                              sheet, name, base))
                continue
            # 2. a divided figure
            if (not isinstance(mx, (int, float)) or mx <= 0) and not zero_stated:
                fails.append(('zero overhaul and no statement why', sheet, name, base))
                continue
            if isinstance(mx, (int, float)) and mx > 0 and (not isinstance(km, (int, float)) or km <= 0):
                fails.append(('overhaul target with no interval', sheet, name, base))
                continue
            if isinstance(first, (int, float)) and isinstance(mx, (int, float)) and first > mx + 0.01:
                fails.append(('first overhaul above the maximum', sheet, name, base))
                continue
            # 3. coherence, where the note states the split
            A, rho, prov, head = envelope_from_note(note)
            if 'per wagon-year' in note and A:
                # research pass 46: head = 0.8A, overhaul event = 1.2A every six years
                checked += 1
                if abs((head or 0) - 0.8 * A) > 0.05 or abs((mx or 0) - 1.2 * A) > 0.05:
                    fails.append(('wagon head/event not 0.8A/1.2A (head %.2f, event %.2f, A %.2f)'
                                  % (head or 0, mx or 0, A), sheet, name, base))
                continue
            is_animal = ('per animal-year' in note
                         or (basis.startswith('horse (') and 'per vehicle-year' in note))
            if is_animal:
                # standing rule 2: the overhaul is the replacement at 100 per cent of the price
                checked += 1
                if not isinstance(cap, (int, float)) or abs((mx or 0) - cap) > 0.5:
                    fails.append(('animal overhaul is not the purchase price (%.2f vs %.2f)'
                                  % (mx or 0, cap or 0), sheet, name, base))
                continue
            if None in (A, rho, prov, head):
                dat_cost = ws.cell(r, 10).value
                zero_priced = ((isinstance(cap, (int, float)) and cap == 0)
                               or (isinstance(dat_cost, (int, float)) and dat_cost == 0))
                if ('priced zero' in note or 'carries the whole cost' in note
                        or 'carried by the leading section' in note or zero_priced):
                    zero_sections.append((sheet, name))
                    if (zero_priced and not re.search(
                            r'section|leading|zero|rear|centre|hold|locker|deck', note, re.I)):
                        warnings.append(('zero-priced section has an unrelated basis note',
                                         sheet, name))
                    continue
                unchecked.append((sheet, name, note))
                continue
            checked += 1
            if abs(head + prov - (A - rho)) > max(0.25, 0.005 * A):
                fails.append(('head + provision != net total (%.2f + %.2f != %.2f)'
                              % (head, prov, A - rho), sheet, name, base))
                continue
            # The interval written in the sheet must be the interval the note's arithmetic used.
            # Only where the note says it converts years at the row's own distance (the locomotive
            # and tram rows); the carriage and wagon bands use a fixed reference km by design.
            if isinstance(mx, (int, float)) and mx > 0 and 'at that distance' in note:
                yrs = num(r'The interval is ([\d.]+) years', note)
                K = num(r'at mean annual distance ([\d,]+) km', note)
                if yrs and K and isinstance(km, (int, float)) and km > 0:
                    if abs(km / K - yrs) > 0.06 * max(1.0, yrs):
                        fails.append(('written interval %.0f km is %.2f years at %.0f km/yr, but '
                                      'the note sizes the event at %.2f years'
                                      % (km, km / K, K, yrs), sheet, name, base))
                        continue
            # the head written in the cells must be the head the note states
            K = num(r'at mean annual distance ([\d,]+) km', note)
            if K is None:
                K = num(r'at ([\d,]+) km a year', note)
            F = ws.cell(r, 27).value
            V = ws.cell(r, 29).value or 0.0
            if isinstance(F, (int, float)) and K:
                if abs(F + V * K - head) > max(0.6, 1e-3 * head):
                    fails.append(('written fixed + per-km != stated head (%.2f != %.2f)'
                                  % (F + V * K, head), sheet, name, base))

    print('vehicles audited: %d | coverage+division ok: %d | envelope checked: %d | '
          'zero-priced sections: %d | unchecked (note states no split): %d | failures: %d'
          % (vehicles, vehicles - len([f for f in fails if 'no overhaul' in f[0]]),
             checked, len(zero_sections), len(unchecked), len(fails)))
    by_sheet = {}
    for sheet, _, _ in unchecked:
        by_sheet[sheet] = by_sheet.get(sheet, 0) + 1
    if by_sheet:
        print('unchecked by sheet: ' + ', '.join('%s %d' % (k, v) for k, v in by_sheet.items()))
    if warnings:
        print('warnings: %d zero-priced sections carry a note that does not describe a section'
              % len(warnings))
        for w in warnings[:10]:
            print('   warning:', w[0], '|', w[1], '|', w[2])
    if VERBOSE:
        for u in unchecked[:80]:
            print('   unchecked:', u[:2])
    if NOTES:
        for sheet, name, note in unchecked:
            print('\n--- %s | %s\n%s' % (sheet, name, note))
    if fails:
        print('\nFAILURES:')
        for f in fails[:60]:
            print('   %-58s %-22s r? %s' % (f[0], f[1], f[2]))
        if len(fails) > 60:
            print('   ... and %d more' % (len(fails) - 60))
        wm.close()
        wc.close()
        return 1
    print('PASS: every vehicle has an overhaul target and every stated split adds up.')
    wm.close()
    wc.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
