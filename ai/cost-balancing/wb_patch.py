# Python 3: patch the maintained cost-balancing workbooks IN PLACE (never rebuild them from
# build_workbooks.py: the committed workbooks carry manual corrections the generator does not
# reproduce, e.g. the power-line maintenance conversion and the x8 way-maintenance columns).
# Applies: the 2026-11-24 decision notes (costing pass, canals, signals) and any rows in
# research-pricing-rows-39.csv not already present in the "Research prices (all passes)" sheet.
# Idempotent: re-running only appends rows not already present.
import csv
import os
from openpyxl import load_workbook

def find_base():
    """The workspace root: the ancestor directory holding New/cost-balancing-capital.xlsx."""
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.exists(os.path.join(d, 'New', 'cost-balancing-capital.xlsx')):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            raise SystemExit('workspace root not found above ' + __file__)
        d = parent


BASE = find_base()
CAP = os.path.join(BASE, 'New', 'cost-balancing-capital.xlsx')
MAINT = os.path.join(BASE, 'New', 'cost-balancing-maintenance.xlsx')
ROWS39 = os.path.join(BASE, 'New', 'ai', 'cost-balancing', 'research-pricing-rows-39.csv')

CANAL_CAP = ('; whole construction including formation, because for a canal the forging is the '
             'building and forge_cost_water is 0 (decision 2026-11-24)')
CANAL_MAINT = (' | canal upkeep only: canal ways carry no wear and are not renewed, so this '
               'carries no renewal element (decision 2026-11-24)')
SIGNAL = (' | one signal object is one signal in reality; the general signalling infrastructure '
          'is priced in the signalbox (decision 2026-11-24)')

README_CAP = [
    'THE COSTING PASS: nothing in these sheets is applied to the .dat files. These sheets are',
    'the research store; copying their values into the .dat files is the costing pass, one',
    'operation, run only when the research is complete and the sheets hold the final figures',
    '(user direction 2026-11-24). Corrections found before then accumulate here.',
    'CANALS: deliberate zero forge and zero renewal. For a canal there is no way surface - the',
    'forging is the building, and it differs by canal class (ship canal against tub-boat',
    'canal), so the formation is folded into the per-class way cost and forge_cost_water goes',
    'to 0 at the costing pass (decision 2026-11-24). The suggested canal values are the whole',
    'construction and are unchanged by the fold.',
    'SIGNALS: one signal object is one signal in reality (post with its arms or lamps); the',
    'general signalling infrastructure is represented by the signalbox cost (decision',
    '2026-11-24). The 168 signal objects are calibrated to the per-post ladder at the pass.',
]
README_MAINT = [
    'THE COSTING PASS: nothing here is applied to the .dat files until the research is',
    'complete and the sheets hold the final figures (user direction 2026-11-24).',
    'CANALS: canal ways carry no wear and are not renewed, so their maintenance is upkeep',
    'only and carries no renewal element (decision 2026-11-24).',
]

MARK = 'decision 2026-11-24'


def patch_readme(ws, lines):
    last = max((c.row for row in ws.iter_rows(min_col=1, max_col=1) for c in row
                if c.value is not None), default=0)
    # idempotence: skip if already applied
    existing = ' '.join(str(c.value) for row in ws.iter_rows(min_col=1, max_col=1) for c in row
                        if c.value)
    if 'THE COSTING PASS' in existing:
        return 0
    r = last + 2
    for line in lines:
        ws.cell(r, 1, line)
        r += 1
    return len(lines)


def patch_suffix(ws, needle, suffix):
    """Append `suffix` to every string cell containing `needle` that lacks it."""
    n = 0
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and needle in c.value and suffix not in c.value:
                c.value = c.value + suffix
                n += 1
    return n


def patch_1_38(ws):
    """Research passes 1-38 -> 1-39 in the README/note text."""
    n = 0
    for row in ws.iter_rows():
        for c in row:
            if isinstance(c.value, str) and 'passes 1-38' in c.value:
                c.value = c.value.replace('passes 1-38', 'passes 1-39')
                n += 1
    return n


def append_research_rows(ws):
    with open(ROWS39, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    existing = set()
    for row in ws.iter_rows(min_row=3):
        key = ((str(row[0].value or '').strip().lower(), str(row[1].value or '').strip().lower(),
                str(row[2].value or '').strip().lower(), str(row[3].value or '').strip().lower(),
                ('%g' % row[4].value) if isinstance(row[4].value, (int, float)) else
                str(row[4].value or '').strip()))
        existing.add(key)
    last = ws.max_row
    added = 0
    for r in rows:
        key = ((r['domain'] or '').strip().lower(), (r['kind'] or '').strip().lower(),
               (r['name_or_item'] or '').strip().lower(), (r['year'] or '').strip(),
               ('%g' % float(r['price'])) if r['price'] not in ('', '0') else '')
        if key in existing:
            continue
        last += 1
        ws.cell(last, 1, r['domain'])          # Domain
        ws.cell(last, 2, r['kind'])            # Kind
        ws.cell(last, 3, r['name_or_item'])    # Item
        ws.cell(last, 4, r['year'])            # Year
        ws.cell(last, 5, float(r['price']) if r['price'] not in ('', '0') else None)  # Price
        ws.cell(last, 6, r['price_unit'])      # Currency
        ws.cell(last, 7, r['scope'])           # Scope
        ws.cell(last, 8, r['notes'])           # Notes / specification
        ws.cell(last, 9, r['source_ref'])      # Source reference
        ws.cell(last, 10, r['kb_location'])    # Evidence file
        added += 1
    return added


def main():
    changed = []
    wb = load_workbook(CAP)
    changed.append(('cap README', patch_readme(wb['README'], README_CAP)))
    changed.append(('cap 1-38->1-39', sum(patch_1_38(wb[s]) for s in wb.sheetnames)))
    n = 0
    for s in ('Ways - water',):
        n += patch_suffix(wb[s], 'measured canal construction per km by size class', CANAL_CAP)
    changed.append(('cap canal basis', n))
    n = 0
    for s in wb.sheetnames:
        n += patch_suffix(wb[s], 'signal post complete', SIGNAL)
        n += patch_suffix(wb[s], 'complete automatic semaphore signal', SIGNAL)
        n += patch_suffix(wb[s], 'colour-light running signal, Kent Coast', SIGNAL)
    changed.append(('cap signal basis', n))
    changed.append(('cap research rows', append_research_rows(wb['Research prices (all passes)'])))
    wb.save(CAP)

    wb = load_workbook(MAINT)
    changed.append(('maint README', patch_readme(wb['README'], README_MAINT)))
    changed.append(('maint 1-38->1-39', sum(patch_1_38(wb[s]) for s in wb.sheetnames)))
    n = 0
    # water upkeep basis cells: contain the 1938 canal rate
    for row in wb['Ways - water'].iter_rows():
        for c in row:
            if (isinstance(c.value, str) and 'way upkeep GBP' in c.value
                    and '1938' in c.value and CANAL_MAINT not in c.value):
                c.value = c.value + CANAL_MAINT
                n += 1
    changed.append(('maint canal basis', n))
    n = 0
    for s in wb.sheetnames:
        n += patch_suffix(wb[s], 'signal post complete', SIGNAL)
        n += patch_suffix(wb[s], 'complete automatic semaphore signal', SIGNAL)
        n += patch_suffix(wb[s], 'colour-light running signal, Kent Coast', SIGNAL)
    changed.append(('maint signal basis', n))
    wb.save(MAINT)

    for name, n in changed:
        print('%-24s %d' % (name, n))


if __name__ == '__main__':
    main()
