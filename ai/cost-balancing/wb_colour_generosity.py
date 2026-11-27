# -*- coding: utf-8 -*-
# wb_colour_generosity.py - shade the active "Suggested .dat" columns of the two cost-balancing
# workbooks by how far each suggested figure is from the figure in the current .dat file.
#
# WHAT IT DOES
# 1. Shading is applied to the pair of suggested columns that supplies the target the Match
#    verdict uses on that row:
#       capital      Suggested .dat total (measured / class) and way only (measured / class)
#       maintenance  Suggested .dat fixed (measured / class) and per-km (measured / class)
#    The measured pair is used where a measured price exists, the class pair otherwise. The
#    superseded class cells keep their existing grey fill and are not shaded.
# 2. For each shaded cell the comparison is with the current .dat figure in the same field:
#       capital total       J + K   (way cost plus forge cost)
#       capital way only    J       (way cost)
#       maintenance fixed   J       (fixed maintenance)
#       maintenance per-km  L       (per-km maintenance)
#    A cell with no current .dat figure is left unshaded: there is nothing to compare with.
# 3. Orange = the suggested figure is higher than the current figure, so the change is less
#    favourable to the player. Blue = the suggested figure is lower, so more favourable.
#    White = the two figures are equal.
# 4. Saturation is linear in the base-2 logarithm of suggested/current, so equal doublings
#    change the shade by equal steps. Full saturation is reached at a factor of 64 either way
#    (6 doublings). That bound is the 95th percentile of the |log2| differences actually
#    present in the two workbooks on 2026-11-27 (5.83); the remaining 5 per cent clamp to the
#    full colour. A ratio of 2 is one sixth of the way to full colour, a ratio of 8 one half.
# 5. A suggested charge where the current .dat figure is zero has no finite ratio and is
#    shown at full orange; a suggested zero against a current charge is full blue; a negative
#    suggested figure is full blue. Those three states are recorded in the workbook README.
#
# Run: py -3 wb_colour_generosity.py [--write] [--clear]. Dry run by default. Idempotent: a
# re-run replaces the shading it wrote and leaves every other fill alone. --clear removes the
# shading and its README section, restoring the untouched fills.
import math
import os
import shutil
import subprocess
import sys
from copy import copy
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import PatternFill

HERE = os.path.dirname(os.path.abspath(__file__))

# Sheets that hold one row per in-game object. The remaining sheets are reference material.
TYPE_SHEETS = [
    'Rail vehicles', 'Road vehicles', 'Tram vehicles', 'Water vehicles', 'Air vehicles',
    'Narrow gauge vehicles', 'Maglev vehicles', 'Ways - rail', 'Ways - road', 'Ways - water',
    'Ways - tram', 'Ways - narrow gauge', 'Ways - air', 'Ways - maglev', 'Ways - power',
    'Bridges & viaducts', 'Tunnels', 'Way objects (electrification)', 'Signals', 'Signalboxes',
    'Roadsigns', 'Stations & bus stops', 'Piers & docks', 'Depots', 'Engine settings',
]

WHITE = (255, 255, 255)
ORANGE = (237, 125, 49)      # the full "less favourable" colour
BLUE = (74, 134, 200)        # the full "more favourable" colour
FULL_SCALE = 6.0             # doublings from 1:1 to full saturation; see note 4 above
GREY_OUT = 'FFF2F2F2'        # the existing "superseded by measured" fill

README_MARK = 'GENEROSITY SHADING'


def find_base():
    d = HERE
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
WORK = os.path.join(BASE, 'ai', 'temp', 'colourwork')
RECALC = os.path.join(WORK, 'recalc')
RECALC_IN = os.path.join(WORK, 'in')
WRITE = '--write' in sys.argv
CLEAR = '--clear' in sys.argv

README_INTRO = [
    '',
    README_MARK + ' (the two active Suggested .dat columns; added 2026-11-27)',
    'Orange = the suggested figure is above the current .dat figure in the same field, so the',
    'change is less favourable to the player. Blue = the suggested figure is below it, so the',
    'change is more favourable. White = the two figures are equal.',
]
README_FIELDS = {
    'capital': [
        'The columns are Suggested .dat total (measured or class), compared with J+K (way cost',
        'plus forge cost), and Suggested .dat way only (measured or class), compared with J.',
    ],
    'maintenance': [
        'The columns are Suggested .dat fixed (measured or class), compared with J, and',
        'Suggested .dat per-km (measured or class), compared with L.',
    ],
}
README_TAIL = [
    'Saturation is linear in the base-2 logarithm of suggested/current: a ratio of 2 is one',
    'sixth of full colour and a ratio of 8 one half; full colour is a factor of 64 either way,',
    'the 95th percentile of the differences in these workbooks (5.83 doublings). The pair shaded',
    'is the one the Match verdict uses on that row: measured where a measured price exists,',
    'class otherwise; the superseded class pair keeps its grey fill. A row with no current .dat',
    'figure is left unshaded. Three states have no finite ratio: a charge introduced where the',
    'current figure is zero is full orange, a suggested zero against a current charge is full',
    'blue, and a negative suggested figure is full blue. The shading is static: it does not',
    'recalculate.',
]


def soffice_path():
    for p in (r'C:\Program Files\LibreOffice\program\soffice.exe',
              r'C:\Program Files (x86)\LibreOffice\program\soffice.exe'):
        if os.path.exists(p):
            return p
    found = shutil.which('soffice')
    if found:
        return found
    raise SystemExit('LibreOffice not found; the values are needed to compute the shading')


def recalc(workbook_path):
    """Convert a copy of the workbook with LibreOffice so the formula results can be read."""
    os.makedirs(RECALC, exist_ok=True)
    os.makedirs(RECALC_IN, exist_ok=True)
    name = os.path.basename(workbook_path)
    source = os.path.join(RECALC_IN, name)
    target = os.path.join(RECALC, name)
    if os.path.exists(target):
        os.remove(target)
    shutil.copyfile(workbook_path, source)
    profile = Path(os.path.join(WORK, 'lo-profile')).as_uri()
    subprocess.run([soffice_path(), '-env:UserInstallation=' + profile, '--headless',
                    '--convert-to', 'xlsx', '--outdir', RECALC, source],
                   check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if not os.path.exists(target):
        raise SystemExit('LibreOffice produced no recalculated copy of ' + workbook_path)
    return target


def is_num(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def blend(colour, strength):
    """Mix white with `colour`; strength 0 is white, 1 is the colour itself."""
    strength = max(0.0, min(1.0, strength))
    return tuple(int(round(255 + (channel - 255) * strength)) for channel in colour)


def shade(suggested, current):
    """Return (r, g, b) for the comparison, or None when it cannot be made."""
    if not is_num(suggested) or not is_num(current) or current < 0:
        return None
    if current == 0:
        if suggested == 0:
            return WHITE
        return BLUE if suggested < 0 else ORANGE
    if suggested <= 0:
        # A zero or negative suggestion is infinitely below any positive current figure.
        return BLUE
    strength = abs(math.log2(suggested / current)) / FULL_SCALE
    return blend(ORANGE if suggested > current else BLUE, strength)


def capital_cells(values, row):
    """(column, current value, label) for the active suggested pair on a capital sheet."""
    measured = is_num(values['T%d' % row].value)
    total_col, way_col = ('T', 'U') if measured else ('AA', 'AB')
    j = values['J%d' % row].value
    k = values['K%d' % row].value
    if is_num(j) or is_num(k):
        current_total = (j if is_num(j) else 0) + (k if is_num(k) else 0)
    else:
        current_total = None
    return [
        (total_col, current_total, 'total'),
        (way_col, j if is_num(j) else None, 'way only'),
    ]


def maintenance_cells(values, row):
    """(column, current value, label) for the active suggested pair on a maintenance sheet."""
    measured = is_num(values['U%d' % row].value)
    fixed_col, km_col = ('U', 'Z') if measured else ('AH', 'AI')
    return [
        (fixed_col, values['J%d' % row].value, 'fixed'),
        (km_col, values['L%d' % row].value, 'per-km'),
    ]


def collect_stats(stats, suggested, current):
    if is_num(suggested) and is_num(current):
        if current == 0 and suggested > 0:
            stats['new charge (full orange)'] += 1
        elif suggested <= 0 and current != 0:
            stats['removed charge or negative (full blue)'] += 1
        elif current == 0 and suggested == 0:
            stats['both zero (white)'] += 1
        elif suggested > 0 and current > 0:
            stats['ratio'].append(abs(math.log2(suggested / current)))


def readme_add(ws, kind):
    existing = ' '.join(str(c.value) for row in ws.iter_rows(min_col=1, max_col=1)
                        for c in row if c.value)
    if README_MARK in existing:
        return 0
    lines = README_INTRO + README_FIELDS[kind] + README_TAIL
    last = max((c.row for row in ws.iter_rows(min_col=1, max_col=1) for c in row
                if c.value is not None), default=0)
    style = copy(ws.cell(last, 1)._style)
    row = last
    for line in lines:
        row += 1
        cell = ws.cell(row, 1, line if line else None)
        cell._style = copy(style)
    return len(lines)


def readme_clear(ws):
    start = None
    for row in ws.iter_rows(min_col=1, max_col=1):
        cell = row[0]
        if isinstance(cell.value, str) and cell.value.startswith(README_MARK):
            start = cell.row
            break
    if start is None:
        return 0
    cleared = 0
    for row in range(start, ws.max_row + 1):
        cell = ws.cell(row, 1)
        if cell.value is not None:
            cell.value = None
            cleared += 1
    return cleared


def clear_workbook(path, kind):
    book = load_workbook(path)
    columns = (['T', 'U', 'AA', 'AB'] if kind == 'capital'
               else ['U', 'Z', 'AH', 'AI'])
    cleared = 0
    for sheet in TYPE_SHEETS:
        if sheet not in book.sheetnames:
            continue
        ws = book[sheet]
        for column in columns:
            for row in range(7, ws.max_row + 1):
                cell = ws['%s%d' % (column, row)]
                fill = cell.fill
                if fill is None or fill.patternType != 'solid':
                    continue
                if fill.start_color.rgb == GREY_OUT:
                    continue
                cell.fill = PatternFill(fill_type=None)
                cleared += 1
    readme_clear(book['README'])
    book.save(path)
    print('%-15s cleared cells: %d' % (kind, cleared))


def shade_workbook(path, kind):
    recalculated = recalc(path)
    values_wb = load_workbook(recalculated, data_only=True)
    book = load_workbook(path)
    stats = {'ratio': [], 'new charge (full orange)': 0,
             'removed charge or negative (full blue)': 0, 'both zero (white)': 0}
    shaded = 0
    skipped_no_current = 0
    skipped_no_suggestion = 0
    skipped_grey = 0
    per_sheet = []

    for sheet in TYPE_SHEETS:
        if sheet not in book.sheetnames:
            continue
        values = values_wb[sheet]
        styled = book[sheet]
        sheet_count = 0
        for row in range(7, values.max_row + 1):
            cells = (capital_cells(values, row) if kind == 'capital'
                     else maintenance_cells(values, row))
            for column, current, label in cells:
                suggested = values['%s%d' % (column, row)].value
                if not is_num(suggested):
                    skipped_no_suggestion += 1
                    continue
                collect_stats(stats, suggested, current)
                colour = shade(suggested, current)
                if colour is None:
                    skipped_no_current += 1
                    continue
                target = styled['%s%d' % (column, row)]
                if (target.fill is not None and target.fill.patternType == 'solid'
                        and isinstance(target.fill.start_color.rgb, str)
                        and target.fill.start_color.rgb == GREY_OUT):
                    skipped_grey += 1
                    continue
                if WRITE:
                    target.fill = PatternFill(fill_type='solid',
                                              start_color='FF%02X%02X%02X' % colour)
                shaded += 1
                sheet_count += 1
        per_sheet.append((sheet, sheet_count))

    if WRITE:
        readme_add(book['README'], kind)
        book.save(path)

    ratios = sorted(stats['ratio'])
    print('%-15s shaded cells: %d' % (kind, shaded))
    for sheet, count in per_sheet:
        if count:
            print('    %-28s %d' % (sheet, count))
    if ratios:
        n = len(ratios)
        def percentile(p):
            return ratios[min(n - 1, max(0, int(round(p * (n - 1)))))]
        print('    finite comparisons %d; |log2| p50 %.2f p75 %.2f p90 %.2f p95 %.2f max %.2f'
              % (n, percentile(0.50), percentile(0.75), percentile(0.90),
                 percentile(0.95), ratios[-1]))
    print('    new charge where current is zero: %d; suggested zero or negative: %d; '
          'both zero: %d' % (stats['new charge (full orange)'],
                             stats['removed charge or negative (full blue)'],
                             stats['both zero (white)']))
    print('    skipped: no suggestion %d, no current .dat figure %d, grey-out cell %d'
          % (skipped_no_suggestion, skipped_no_current, skipped_grey))
    return shaded


def main():
    os.makedirs(WORK, exist_ok=True)
    if CLEAR:
        if WRITE:
            raise SystemExit('use either --write or --clear, not both')
        clear_workbook(CAP, 'capital')
        clear_workbook(MAINT, 'maintenance')
        return
    total = shade_workbook(CAP, 'capital') + shade_workbook(MAINT, 'maintenance')
    print('%s: %d cells' % ('written' if WRITE else 'dry run (use --write)', total))


if __name__ == '__main__':
    main()
