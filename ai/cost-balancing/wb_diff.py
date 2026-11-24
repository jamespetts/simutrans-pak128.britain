# Python 3: line-level diff of two workbook dumps; prints changed coordinates only.
import sys

def load(p):
    d = {}
    sheet = None
    for line in open(p, encoding='utf-8'):
        line = line.rstrip('\n')
        if line.startswith('=== SHEET '):
            sheet = line[10:]
        else:
            coord, _, val = line.partition('|')
            d[(sheet, coord)] = val
    return d

a = load(sys.argv[1])
b = load(sys.argv[2])
keys = set(a) | set(b)
changed = sorted(k for k in keys if a.get(k) != b.get(k))
print('total cells before/after: %d / %d; changed: %d' % (len(a), len(b), len(changed)))
sheets = {}
for k in changed:
    sheets.setdefault(k[0], []).append(k)
for s in sorted(sheets):
    print('SHEET %s: %d changed' % (s, len(sheets[s])))
    for k in sheets[s][:12]:
        print('  %s' % k[1])
        print('    - %s' % (a.get(k) or '<absent>')[:220])
        print('    + %s' % (b.get(k) or '<absent>')[:220])
    if len(sheets[s]) > 12:
        print('  ... %d more' % (len(sheets[s]) - 12))
