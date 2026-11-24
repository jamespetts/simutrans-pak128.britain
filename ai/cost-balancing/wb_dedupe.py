# Python 3: remove duplicate rows from "Research prices (all passes)" where (domain, kind, item,
# year, price) match an earlier row (price compared numerically). Keeps the first occurrence.
# CAUTION (2026-11-24): this scans the WHOLE sheet. The committed workbook content contains some
# genuine duplicate rows of its own; deleting those shifts every row below and so touches
# committed content. Run this only on rows you appended yourself, or accept the shift knowingly.
import sys
from openpyxl import load_workbook

wb = load_workbook(sys.argv[1])
ws = wb['Research prices (all passes)']
seen = set()
dupes = []
for r in range(3, ws.max_row + 1):
    vals = [ws.cell(r, c).value for c in range(1, 6)]
    if all(v is None for v in vals):
        continue
    e = vals[4]
    key = (str(vals[0] or '').strip().lower(), str(vals[1] or '').strip().lower(),
           str(vals[2] or '').strip().lower(), str(vals[3] or '').strip(),
           ('%g' % e) if isinstance(e, (int, float)) else str(e or '').strip())
    if key in seen:
        dupes.append(r)
    else:
        seen.add(key)
for r in reversed(dupes):
    ws.delete_rows(r)
wb.save(sys.argv[1])
print('deleted %d duplicate rows from %s' % (len(dupes), sys.argv[1]))
