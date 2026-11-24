# Python 3: dump every non-empty cell of the two cost-balancing workbooks to text, for diffing.
import sys
from openpyxl import load_workbook

out = open(sys.argv[2], 'w', encoding='utf-8')
wb = load_workbook(sys.argv[1], data_only=False)
for ws in wb.worksheets:
    out.write('=== SHEET %s\n' % ws.title)
    for row in ws.iter_rows():
        for c in row:
            if c.value is not None:
                out.write('%s|%s\n' % (c.coordinate, str(c.value).replace('\n', '\\n')))
out.close()
print('dumped', sys.argv[1], '->', sys.argv[2])
