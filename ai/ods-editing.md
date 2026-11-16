---
status: draft
verified: none
---
# Editing `.ods` working papers

**Covers**: the safe, verified end-to-end procedure for adding or modifying a row in the
`New/*.ods` calibration spreadsheets (e.g. `steam-physics-calcs.ods`,
`Comfort calibration overview.ods`) without corrupting them. Parent: [balancing](balancing.md).

Do NOT improvise this. Every step below is the result of real failures documented throughout
2026-09-23; the procedure has been run end-to-end and verified against the tracked files.

## Hard rules (break none of these)

1. Never edit `.ods` by parsing `content.xml` and re-serialising it (ElementTree, lxml, etc.).
   Re-serialisation rewrites ODF namespace prefixes (`calcext:` and the many root `xmlns`
   declarations), drops or reorders attributes (`calcext:value-type`, `table:style-name`), and
   breaks the `office:value`/`<text:p>` cached-display pairing. Some readers then render the
   raw formula text (`=of:=(29*0.45359237)/1.6`) and, worse, silently drop whole rows. The
   only supported edit is a **byte splice**: a literal string inserted into `content.xml`
   decoded as UTF-8, with every other zip entry copied byte-identically.
2. The tracked file in `New/` is authoritative. Before starting, and after any doubt, recover
   it with `git -C New restore <file>`. Then redo the edit on the clean file.
3. Work on a copy in `ai/temp/`; only copy into `New/` at the very end.
4. These sheets are **sorted** — insert at the sorted position, never append at the end.
5. A raw splice does **not** renumber formulas the way an interactive row insert does; for a
   mid-table insert you must renumber the shifted references yourself.

## Environment: how to run these scripts

The scripts below are pure-stdlib (`zipfile`, `re`, `os`, `shutil`, `xml.etree`) and
operate on spreadsheet zips only. Run them with Python 3 from the project root:

```
& C:\WINDOWS\py.exe -3 "ai\temp\<script>.py"
```

`py -3` resolves to Python 3.7.8 64-bit on the maintainer's machine.
`[EXECUTION-VERIFIED:2026-09-25]` (Bare `python.exe` is Python 2.7 and unsuitable; the
`python3.exe` WindowsApps entry is a 0-byte stub. `[EXECUTION-VERIFIED:2026-09-25]`)
All results print to stdout; filter with `Select-String`.

## 1. Inspect before editing (never skip)

Ten facts you must establish before touching a byte:

- Which `<table:table table:name="...">` block the target sheet is (use `table_span`).
- How many `<table:table-row>` elements it has, and what the sort key is
  (`steam … Extrapolation`: column A = intro year; `Comfort … All vehicles`: column 3 =
  comfort rating). Dump the first few cells of the last 8 rows and the rows around the target
  with the `cell_texts` helper — this also exposes trailing footer rows.
- Whether there are **footer rows** below the data (`Extrapolation` ends with three `kG/hour`
  unit rows) — they reserve the bottom and are why tail-append lands past the last data row.
- Whether any formula references cross sheets (none here; all references are current-sheet
  `[.X<n>]`). Verify each time by scanning every `table:formula="..."` attribute.

```python
import re, zipfile
BASE = 'C:/Users/James E. Petts/Documents/Development/Simutrans/PakBritain sources/'

def read(rel):
    return zipfile.ZipFile(BASE + rel).read('content.xml').decode('utf-8')

def table_span(x, name):
    i = x.find('table:name="%s"' % name)
    if i < 0: raise SystemExit('table not found: ' + name)
    s = x.rfind('<table:table', 0, i)
    e = x.find('</table:table>', s)
    return s, e

def row_starts(x, s, e):
    # lookahead excludes <table:table-rows> and <table:table-row-group>
    return [s + m.start() for m in re.finditer(r'<table:table-row(?=[ >])', x[s:e])]

def cell_texts(x, s, e):
    out = []
    for m in re.finditer(r'<table:table-cell(?=[ >])|<table:covered-table-cell', x[s:e]):
        cs = s + m.start()
        ce = x.find('</table:table-cell>', cs)
        if ce < 0 or ce > e: ce = e
        t = re.search(r'<text:p>([^<]*)</text:p>', x[cs:ce])
        out.append(t.group(1) if t else '')
    return out

def formulas(x):
    return re.findall(r'table:formula="([^"]*)"', x)
```

Reference-scan (do this before any mid-table insert):

```python
f  = formulas(x)
cross = [t for f in f for t in re.findall(r'\[([^.\]\[]+)\.[^\]]*\]', f)]
refs = re.findall(r'\[\.([A-Z]{1,3})(\d+)\]', x)
print('cross-sheet refs:', cross, '| ref row range:',
      min(int(n) for _, n in refs), '-', max(int(n) for _, n in refs))
```

`cross` must be empty and `refs` must only reference current-sheet rows. If either check
fails, stop and report — the renumber rule below no longer applies.

## 2. Build the new row (exact native cell format)

Copy the exact cell shape the file uses (verified raw examples from `steam-physics-calcs.ods`):

```
<table:table-cell table:style-name="ce72" table:formula="of:=([.H191]/2.5)*0.7457"
  office:value-type="float" office:value="487.6878" calcext:value-type="float">
  <text:p>488</text:p></table:table-cell>
```

A new cell must carry `office:value-type`, the full-precision `office:value`,
`calcext:value-type`, and a `<text:p>` with the display value. Formulas use the `of:=` syntax
with sheet-relative `[.E<n>]` references. Percentage cells use `office:value-type="percentage"`
and a fractional `office:value` (0.059 = 5.90%). Helpers that emit this shape:

```python
def esc(v):
    return v.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def cell_num(value, display, formula=None):
    f = ' table:formula="%s"' % formula if formula else ''
    return ('<table:table-cell%s office:value-type="float" office:value="%s" '
            'calcext:value-type="float"><text:p>%s</text:p></table:table-cell>'
            % (f, value, esc(display)))

def cell_pct(value, display):
    return ('<table:table-cell office:value-type="percentage" office:value="%s" '
            'calcext:value-type="percentage"><text:p>%s</text:p></table:table-cell>'
            % (value, esc(display)))

def cell_str(v):
    return ('<table:table-cell office:value-type="string" '
            'calcext:value-type="string"><text:p>%s</text:p></table:table-cell>' % esc(v))

def row_xml(cells):
    return '<table:table-row>' + ''.join(cells) + '</table:table-row>'
```

## 3. Plan the insertion position (sorted sheets)

Find the position by its **neighbour key**, never by tail position:

- Steam `Extrapolation`: the S69 (1911) was inserted after the last 1911 row
  (`GWR 4300 Class`) and before the first 1912 row (`LNWR G1 Class`). Anchor the splice on the
  neighbour's name text.
- `Comfort … All vehicles`: the DC-8 was inserted immediately after its sibling
  (`Boeing 707 (economy)`, and separately `Boeing 707 (first)`), keeping each in its comfort
  band.

Compute the new row's sheet number `P` = (1-based index of the row that will now follow it).
For the steam S69 into 1911, `P = 263`.

## 4. Renumber, then splice (mid-table inserts only)

Because every row from `P` downward shifts by one, and the file's formulas are self-referential
`[.X<n>]`, do this **in order**:

```python
def renumber(x, P):
    def repl(m):
        n = int(m.group(2))
        return '[.%s%d]' % (m.group(1), n + 1 if n >= P else n)
    return re.sub(r'\[\.([A-Z]{1,3})(\d+)\]', repl, x)

newx = renumber(x, P)                       # 1. bump existing refs n>=P
insert_at = newx.find('</table:table-row>', newx.find('<anchor text>')) + len('</table:table-row>')
newx = newx[:insert_at] + row_xml(cells) + newx[insert_at:]   # 2. insert AFTER renumber
```

The new row's own formulas must reference `P` (its final position). Only the new row should
ever reference `P` afterwards — this is a good automatic check (see §6).

## 5. Re-zip (byte-identical everywhere except content.xml)

```python
def rezip(src_rel, dst_rel, newx):
    z = zipfile.ZipFile(BASE + src_rel)
    names = z.namelist()
    wz = zipfile.ZipFile(BASE + dst_rel, 'w')
    wz.writestr('mimetype', z.read('mimetype'), compress_type=zipfile.ZIP_STORED)  # must be first, stored
    for n in names:
        if n == 'mimetype': continue
        wz.writestr(n, newx if n == 'content.xml' else z.read(n),
                    compress_type=zipfile.ZIP_DEFLATED)
    wz.close(); z.close()
```

Write to `ai/temp/<name>.ods`; do not touch `New/` yet.

## 6. Verify before installing

```python
import xml.etree.ElementTree as ET
fixed = read('ai/temp/<name>.ods')
ET.fromstring(fixed.encode('utf-8'))          # well-formed
s, e = table_span(fixed, '<sheet>')
print(len(row_starts(fixed, s, e)))           # == old count + 1 per inserted row
print(fixed.count('<marker>'))                # == 1 (no duplicates)
print(formulas-in-new-row)                     # all reference the right P
print(re.findall(r'\[\.([A-Z]{1,3})%d\]' % P, fixed))  # only the new row's own refs may match P
```

Also confirm the footer rows are untouched and `git -C New diff --stat <file>` shows only the
intended byte-size change. If anything is off, `git -C New restore <file>` and redo.

## 7. Install and confirm

```python
shutil.copyfile('ai/temp/<name>.ods', 'New/<repo-name>.ods')
```

Then `git -C New status --short` shows the file modified, and its byte size is close to the
original (a one-row insert of ~3 KB expands `content.xml`; the re-zipped total can shrink a
little). Re-open in the spreadsheet app and confirm the row is visible in its sorted position
and that search finds its name.

## Known failure modes (all hit during 2026-09-23)

- ElementTree round-trip → namespace rewrite + dropped `calcext`/`<text:p>` → rows dropped /
  formula text shown. Never round-trip.
- Tail-append (`insert before </table:table>`) → row lands after the `kG/hour` footer, out of
  sort order and past the last data row.
- Mid-table insert **without** renumber → every downstream row's self-reference points one row
  too high, silently wrong values.
- Matching the substring `<table:table` also matches `<table:table-row/-cell/-column/-rows`;
  use the lookahead regex `r'<table:table-row(?=[ >])'` to count/iterate rows.
- Slicing `x[s:e]` and then using slice-relative offsets to index the full `x` → wrong
  boundaries; always add `s` back when converting to absolute positions.
- Duplicated marker names after two table names collide (e.g. `Black lining` vs
  `Black_lining`) — verify marker counts are exactly 1.

## Open questions

- Where should the standalone helper script live permanently (currently re-assembled in
  `ai/temp/` each session)?
- Does any spreadsheet use cross-sheet or range (`[.A1:B2]`) references that would need a
  richer renumber routine?
