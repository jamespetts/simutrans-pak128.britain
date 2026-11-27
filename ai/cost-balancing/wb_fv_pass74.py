# -*- coding: utf-8 -*-
# wb_fv_pass74.py - fill the four research gaps of 2026-11-27.
#
# WHAT THIS PASS DOES
# 1. TRAM WAY MAINTENANCE. The maintenance workbook carried no target for any tram way row.
#    The target is now the routine component of the measured 1930-31 permanent-way charge:
#    "Maintenance and Renewals out of Revenue - Permanent Way" GBP 1,635,654 against permanent-way
#    capital of GBP 35,807,350, i.e. 4.568 per cent a year (Ministry of Transport return 1930-31,
#    summary Part II). The engine charges renewal separately through weg_t::renew(), so the
#    annualised renewal (way cost / 30 years) is deducted; the 30-year life is an inference.
#    The routine component is GBP 42-50 per km-year, which is raw 446-526.
# 2. TRAM WAY CAPITAL. The measured bind on the 41 lb row (GBP600 in 1911) is a per-mile forge
#    rate, not a per-kilometre capital price, and produced a negative way-only value. It is
#    rejected. forge_cost_tram is corrected from 225,000 raw to 89,000 raw, the GBP600 per mile
#    source deflated to 1900 money, which is the trench and concrete bed the forge represents.
# 3. MAGLEV WAY MAINTENANCE. The maintenance workbook carried no target. The target is the routine
#    component at 1.2 per cent of the row's own class capital, which is 60 per cent of the 2 per
#    cent combined rate the synthesis carried; no operator account exists, so the rate is an
#    ESTIMATE with a 0.75-2.0 per cent band.
# 4. DEPOT CAPITAL. The engine charges cost_depot_<waytype> x level and ignores the building
#    cost. The measured per-unit rates are entered and each object's required level is stated.
#    The four settings are proposed, not applied: they are stored in savegames.
# 5. DEPOT MAINTENANCE. The target is 1.5 per cent of capital (research report 16). The route into
#    the game is the depot's own .dat maintenance field, which is unscaled 0.00792622 GBP per raw
#    per month; the column now says so.
# 6. STATION EXTENSION BUILDINGS. The eight type=extension objects that carry goods or mail
#    capacity were priced at the passenger-place rate (250 goods units treated as 250 passenger
#    places). They are now priced by floor area at measured building rates, with the footprint
#    inferred from the function. The passenger station buildings are unchanged.
#
# Run: py -3 wb_fv_pass74.py [--write]. Dry run by default. Idempotent by the pass 74 marker.
import os
import shutil
import sys
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
MARK = 'pass 74'
WRITE = '--write' in sys.argv

CAP_UNIT = 0.00396311            # GBP1900 per raw capital unit, unscaled object
BLD_UNIT = 0.00049539            # GBP1900 per raw capital unit, scaled building
BLD_MONTH_YEAR = 0.01188936      # GBP1900 per raw per year, scaled building maintenance
WAY_MONTH_YEAR = 0.09511464      # GBP1900 per km-year per raw way maintenance

TRAM_FORGE = 89000
TRAM_RENEWAL_LIFE = 30
TRAM_COMBINED_RATE = 0.04568     # 1930-31 permanent way charge / permanent-way capital

# base name -> class capital GBP1900/km (col V of the capital workbook)
TRAM_CAPITAL = {
    'TramTrack': 2486.0, 'TramTrack-55lb': 2637.0, 'TramTrack-75lb': 2852.0,
    'TramTrack-85lb': 2960.0, 'TramTrack-92lb': 3036.0, 'TramTrack-98lb': 3100.0,
    'TramTrackHeavy': 2960.0, 'TramTrack-mothballed': 0.0,
}
TRAM_RAIL = {
    'TramTrack': '41 lb/yard', 'TramTrack-55lb': '55 lb/yard', 'TramTrack-75lb': '75 lb/yard',
    'TramTrack-85lb': '85 lb/yard', 'TramTrack-92lb': '92 lb/yard',
    'TramTrack-98lb': '98 lb/yard', 'TramTrackHeavy': 'heavy rail-compatible',
}

# base name -> class capital GBP1900/km (col V of the capital workbook)
MAGLEV_CAPITAL = {
    'Concrete_Maglev_Track': 124786.0,
    'Concrete_Maglev_Track_Elevated': 152238.0,
    'Economical_Concrete_Maglev_Track': 124786.0,
    'Economical_Concrete_Maglev_Track_Elevated': 152238.0,
    'Mothballed_Maglev_Track': 0.0,
}
MAGLEV_ROUTINE_RATE = 0.012      # routine share of own capital a year; band 0.0075-0.020

# depot family -> measured GBP per unit of size
DEPOT_RATE = {'rail': 750.0, 'road': 187.0, 'ship': 1304.0, 'air': 18745.0}
# base name -> (family, target GBP)
DEPOT = {
    'OldTrainDepot': ('rail', 3000.0), 'AirHangarModern': ('air', 25440.0),
    'AirHangarOld': ('air', 13812.0), 'CoachStable': ('road', 5600.0),
    'MaglevDepot': ('rail', 4382.0), 'ModernBoatyard': ('ship', 1304.0),
    'ModernRoadDepot': ('road', 5600.0), 'ModernRoadDepotElectric': ('road', 5600.0),
    'ModernRoadDepotMixed': ('road', 5600.0), 'ModernTrainDepot': ('rail', 4382.0),
    'ModernTrainDepotElectric': ('rail', 4382.0), 'ModernTrainDepotNarrow': ('rail', 4382.0),
    'ModernTramDepot': ('rail', 9560.0), 'OldBoatyard': ('ship', 1304.0),
    'OldBoatyardSteam': ('ship', 1304.0), 'OldRoadDepot': ('road', 5600.0),
    'OldRoadDepot2': ('road', 5600.0), 'OldRoadDepotElectric': ('road', 5600.0),
    'OldRoadDepotSteam': ('road', 3000.0), 'OldTrainDepotDiesel': ('rail', 4382.0),
    'OldTrainDepotElectric': ('rail', 4382.0), 'OldTrainDepotHorse': ('rail', 2083.0),
    'OldTrainDepotNarrow': ('rail', 3000.0), 'OldTrainDepotNarrowHorse': ('rail', 2083.0),
    'OldTramDepot': ('rail', 9560.0), 'OldTramDepotHorse': ('rail', 9560.0),
    'OldTramDepotSteam': ('rail', 9560.0),
}

# base name -> (description, floor area m2, rate GBP1900/m2, maintenance share)
EXTENSION = {
    'GoodsWarehouseOld': ('brick or timber goods shed, 11 m by 23 m', 250, 2.50, 0.050),
    'GoodsWarehouseModern': ('steel-framed goods shed, 11 m by 36 m', 400, 3.25, 0.020),
    'BulkGoodsBunker': ('brick bulk goods bunker, 8 m by 12 m', 100, 5.00, 0.015),
    'CarYard': ('surfaced car yard, 25 m by 40 m', 1000, 0.50, 0.020),
    'LivestockPen': ('open timber livestock pen, 11 m by 14 m', 150, 1.50, 0.050),
    'OldPostOffice': ('brick sorting office, 12 m by 17 m', 200, 4.00, 0.015),
    'ModernPostOffice': ('concrete or steel sorting office, 15 m by 27 m', 400, 4.50, 0.020),
}
EXTENSION_PREV = {
    'GoodsWarehouseOld': 1150000, 'GoodsWarehouseModern': 1150000,
    'BulkGoodsBunker': 1150000, 'FluidStorageStation': 1150000,
    'CarYard': 1150000, 'LivestockPen': 1150000,
    'OldPostOffice': 850000, 'ModernPostOffice': 1000000,
}

EXTENSION_FLUID = ('tank farm: three tanks at GBP150 plus GBP300 of bund and pipework', 750.0, 0.020)


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
BACKUP = os.path.join(BASE, 'ai', 'temp', 'pre-pass74')


def append_note(cell, text):
    old = str(cell.value or '')
    if MARK in old:
        return False
    cell.value = (old + ' | ' if old else '') + text
    return True


def find_row(ws, base, start=7):
    for r in range(start, ws.max_row + 1):
        if str(ws.cell(r, 2).value or '') == base:
            return r
    return None


# ----------------------------------------------------------------------------- capital workbook

def capital_tram(wb, changed):
    ws = wb['Ways - tram']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in TRAM_CAPITAL:
            continue
        if MARK in str(ws.cell(r, 33).value or ''):
            continue
        ws.cell(r, 11, TRAM_FORGE)
        if base == 'TramTrack':
            for c in (16, 17):
                ws.cell(r, c).value = None
            append_note(ws.cell(r, 33),
                        '%s: the measured GBP600 (1911) was a per-mile forge rate, not a '
                        'per-kilometre capital price; the bind is rejected and the class group is '
                        'used.' % MARK)
        append_note(ws.cell(r, 33),
                    '%s: forge_cost_tram = 89,000 raw (GBP352.70/km), the 1911 GBP600 a mile '
                    'trench-and-bed figure deflated to 1900. The complete street track stays in the '
                    'way object; the previous 225,000 was 2.54 times its own source. Tram and '
                    'depot report 2026-11-27 section 2.' % MARK)
        changed.append(('tram capital', base, 'forge', TRAM_FORGE))
    ps = wb['Params']
    for r in range(1, ps.max_row + 1):
        if ps.cell(r, 1).value == 'FORGE_TRAM':
            if ps.cell(r, 2).value != TRAM_FORGE:
                ps.cell(r, 2, TRAM_FORGE)
                ps.cell(r, 3,
                        'forge_cost_tram: 89,000 raw = GBP352.70/km, the 1911 GBP600 a mile '
                        'trench and concrete bed deflated to 1900. The live simuconf.tab setting '
                        'is still 225,000; its change is outstanding. [USER-DIRECTION:2026-11-27]')
                changed.append(('Params FORGE_TRAM', 'FORGE_TRAM', 225000, TRAM_FORGE))


def capital_air_binds(wb, changed):
    """Pass 73 meant to reject the two paved-runway measured binds, but ws.cell(r, c, None)
    is a no-op in openpyxl, so the values survived. Cleared here."""
    ws = wb['Ways - air']
    for r in range(7, ws.max_row + 1):
        if str(ws.cell(r, 2).value or '') not in ('concrete-runway', 'runway'):
            continue
        if ws.cell(r, 16).value is None and ws.cell(r, 17).value is None:
            continue
        ws.cell(r, 16).value = None
        ws.cell(r, 17).value = None
        append_note(ws.cell(r, 33),
                    '%s: the measured GBP69 per square metre was bound as GBP per kilometre; the '
                    'bind is rejected and the class group is used. Pass 73 intended this and the '
                    'clearing call did not take effect.' % MARK)
        changed.append(('air measured bind cleared', ws.cell(r, 2).value, '', ''))


def capital_depots(wb, changed):
    ws = wb['Depots']
    ws.cell(6, 35, 'Required level (pass 74)')
    ws.cell(6, 36, 'Setting implied by the present level (raw)')
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in DEPOT:
            continue
        fam, target = DEPOT[base]
        rate = DEPOT_RATE[fam]
        level = max(1, int(round(target / rate)))
        this_level = 0
        key = str(ws.cell(r, 3).value or '')
        # read the level from the object's .dat, keyed by base name
        this_level = LEVELS.get(base, 1)
        ws.cell(r, 35, level)
        ws.cell(r, 36, round(rate * this_level / CAP_UNIT))
        append_note(ws.cell(r, 33),
                    '%s: measured %s depot rate GBP%g a unit; target GBP%g is level %d at that rate. '
                    'The engine charges cost_depot_<waytype> x level, so the present level %d '
                    'produces GBP%g against the target. Depot section of the tram and depot report '
                    '2026-11-27.' % (MARK, fam, rate, target, level, this_level,
                                     rate * this_level))
        changed.append(('depot level', base, this_level, level))
    # Settings block, at fixed rows so a re-run does not append a second copy.
    row = 35
    ws.cell(row, 1, 'DEPOT ENGINE SETTINGS (pass 74, 2026-11-27): proposed, not applied')
    row = 36
    for c, text in enumerate(('Setting', 'Applies to', 'Current raw', 'Proposed raw',
                              'GBP per level', 'Basis'), start=1):
        ws.cell(row, c, text)
    block = [
        ('cost_depot_rail', 'track, narrow gauge, tram, monorail, maglev', 2000, 'rail', 750.0),
        ('cost_depot_road', 'road', 1000, 'road', 187.0),
        ('cost_depot_ship', 'water', 4000, 'ship', 1304.0),
        ('cost_depot_air', 'air', 7500, 'air', 18745.0),
    ]
    row = 37
    for name, applies, cur, fam, rate in block:
        ws.cell(row, 1, name)
        ws.cell(row, 2, applies)
        ws.cell(row, 3, cur)
        ws.cell(row, 4, round(rate / CAP_UNIT))
        ws.cell(row, 5, rate)
        ws.cell(row, 6,
                'Measured per-unit rate x level. No engine change is needed for the mechanism, but '
                'each depot .dat level must be set to its size at the costing pass: the present '
                'levels are historical leftovers and bear no relation to it. The correct fix is to '
                'honour the building cost when one is set; see the report.')
        row += 1
    ws.cell(42, 1, 'The setting is stored in savegames. Do not change it in a live pakset '
                   'without the user decision recorded in the report.')


def capital_extensions(wb, changed):
    ws = wb['Stations & bus stops']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base in EXTENSION:
            desc, area, rate, share = EXTENSION[base]
            gbp = area * rate
            text = ('%s: %s at GBP%0.2f/m2 (measured light-industrial shed band GBP2.91-4.60/m2 '
                    'in 1900 money, small brick store GBP1.24-2/m2, station building about '
                    'GBP6/m2), so GBP%0.2f. The object is a goods or mail building, not a passenger '
                    'concourse; the previous per-passenger-place rate treated its capacity as '
                    'passenger places. Extension section of the tram and depot report 2026-11-27.'
                    % (MARK, desc, rate, gbp))
            maint = gbp * share
        elif base == 'FluidStorageStation':
            desc, gbp, share = EXTENSION_FLUID
            text = ('%s: %s, so GBP%0.2f. The object is a goods building, not a passenger '
                    'concourse. Extension section of the tram and depot report 2026-11-27.'
                    % (MARK, desc, gbp))
            maint = gbp * share
        else:
            continue
        if MARK in str(ws.cell(r, 33).value or ''):
            continue
        ws.cell(r, 22, round(gbp, 2))
        ws.cell(r, 23, 1900)
        ws.cell(r, 24, text)
        append_note(ws.cell(r, 33), text)
        changed.append(('extension capital', base, 'class GBP', round(gbp, 2)))


def capital_engine_depots(wb, changed):
    ws = wb['Engine settings']
    row = ws.max_row
    for name, applies, cur, fam, rate in [
            ('cost_depot_rail', 'track, narrow gauge, tram, monorail, maglev', 2000, 'rail', 750.0),
            ('cost_depot_road', 'road', 1000, 'road', 187.0),
            ('cost_depot_ship', 'water', 4000, 'ship', 1304.0),
            ('cost_depot_air', 'air', 7500, 'air', 18745.0)]:
        existing = None
        for r in range(7, ws.max_row + 1):
            if ws.cell(r, 1).value == name:
                existing = r
                break
        if existing is None:
            row += 1
            ws.cell(row, 1, name)
            ws.cell(row, 2, name)
            ws.cell(row, 3, 'simuconf.tab')
            ws.cell(row, 4, 'engine-setting')
            ws.cell(row, 6, 'no')
            ws.cell(row, 7, 'partial')
            ws.cell(row, 8, 'no')
            ws.cell(row, 9, 'partial')
        else:
            row = existing
        ws.cell(row, 10, cur)
        ws.cell(row, 22, rate)
        ws.cell(row, 23, 1900)
        ws.cell(row, 24,
                '%s: measured per-unit depot rate GBP%g x level; the engine charges '
                'cost_depot_<waytype> x level and ignores the building cost. Proposed, not '
                'applied: the setting is stored in savegames. Depot section of the tram and depot '
                'report 2026-11-27.' % (MARK, rate))
        ws.cell(row, 33,
                'unit: per action or object (engine setting) | %s: applies to %s. Current raw '
                '%d, proposed raw %d (GBP%g a level). Every depot .dat level must be set to its '
                'size at the costing pass; the required level per object is in the Depots sheet '
                'column AI.' % (MARK, applies, cur, round(rate / CAP_UNIT), rate))
        changed.append(('engine depot setting', name, cur, round(rate / CAP_UNIT)))


# --------------------------------------------------------------------------- maintenance workbook

def maintenance_tram(wb, changed):
    ws = wb['Ways - tram']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in TRAM_CAPITAL or base == 'TramTrack-mothballed':
            continue
        if MARK in str(ws.cell(r, 42).value or ''):
            continue
        cap = TRAM_CAPITAL[base]
        combined = TRAM_COMBINED_RATE * cap
        renewal = (cap - TRAM_FORGE * CAP_UNIT) / TRAM_RENEWAL_LIFE
        routine = combined - renewal
        sug = round(routine / WAY_MONTH_YEAR)
        ws.cell(r, 17, round(routine, 2))
        ws.cell(r, 18, 1900)
        ws.cell(r, 27, round(routine, 2))
        ws.cell(r, 28, 1900)
        ws.cell(r, 34, sug)
        note = ('%s: routine maintenance only, GBP%0.2f per km-year = %d raw. Basis: the 1930-31 '
                'Ministry return puts permanent-way maintenance and renewals at GBP1,635,654 '
                'against permanent-way capital of GBP35,807,350, 4.568 per cent a year; the '
                'engine charges renewal separately, so the annualised renewal of the way object '
                '(capital less the forge, over 30 years) is deducted. Band at a 25-40 year '
                'life: %d-%d raw. Tram and depot report 2026-11-27 section 2.'
                % (MARK, routine, sug,
                   round((TRAM_COMBINED_RATE * cap - (cap - TRAM_FORGE * CAP_UNIT) / 25.0)
                         / WAY_MONTH_YEAR),
                   round((TRAM_COMBINED_RATE * cap - (cap - TRAM_FORGE * CAP_UNIT) / 40.0)
                         / WAY_MONTH_YEAR)))
        append_note(ws.cell(r, 31), note)
        append_note(ws.cell(r, 42), note)
        changed.append(('tram maintenance', base, '', round(routine, 2), sug))


def maintenance_maglev(wb, changed):
    ws = wb['Ways - maglev']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in MAGLEV_CAPITAL:
            continue
        if MARK in str(ws.cell(r, 42).value or ''):
            continue
        cap = MAGLEV_CAPITAL[base]
        routine = MAGLEV_ROUTINE_RATE * cap
        sug = round(routine / WAY_MONTH_YEAR)
        ws.cell(r, 17, round(routine, 2))
        ws.cell(r, 18, 1900)
        ws.cell(r, 27, round(routine, 2))
        ws.cell(r, 28, 1900)
        ws.cell(r, 34, sug)
        note = ('%s: routine guideway maintenance at 1.2 per cent of the row\'s class capital a year '
                '= GBP%0.2f per km-year = %d raw, band 0.75-2.0 per cent = %d-%d raw. No maglev '
                'operator publishes a guideway maintenance line. The 2 per cent combined rate the '
                'synthesis carried (42,000 raw on the elevated row) is superseded by the '
                'routine-only rule in the same way as tram, road and air: renewal is charged '
                'through weg_t::renew(). The rate is an ESTIMATE. Tram and depot report 2026-11-27 '
                'section 3.'
                % (MARK, routine, sug, round(0.0075 * cap / WAY_MONTH_YEAR),
                   round(0.02 * cap / WAY_MONTH_YEAR)))
        append_note(ws.cell(r, 31), note)
        append_note(ws.cell(r, 42), note)
        changed.append(('maglev maintenance', base, '', round(routine, 2), sug))


def maintenance_depots(wb, changed):
    ws = wb['Depots']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base not in DEPOT:
            continue
        if MARK in str(ws.cell(r, 42).value or ''):
            continue
        note = ('%s: depot maintenance is 1.5 per cent of capital a year (report 16, band '
                '1.0-2.0). The route into the game is the depot building own .dat maintenance '
                'field, which is unscaled: GBP0.00792622 per raw per month, so the suggested raw '
                'figure in column AH is the field value. The engine default (maintenance_building '
                'x level) is not evidence and should not stand. Depot section of the tram and '
                'depot report 2026-11-27.' % MARK)
        append_note(ws.cell(r, 31), note)
        append_note(ws.cell(r, 42), note)
        changed.append(('depot maintenance note', base, '', '', ws.cell(r, 27).value))


def maintenance_extensions(wb, changed):
    ws = wb['Stations & bus stops']
    for r in range(7, ws.max_row + 1):
        base = str(ws.cell(r, 2).value or '')
        if base in EXTENSION:
            desc, area, rate, share = EXTENSION[base]
            gbp = area * rate
        elif base == 'FluidStorageStation':
            desc, gbp, share = EXTENSION_FLUID
        else:
            continue
        if MARK in str(ws.cell(r, 42).value or '') and 'current capital' in str(ws.cell(r, 42).value or ''):
            continue
        maint = gbp * share
        sug = round(maint / BLD_MONTH_YEAR)
        prev_raw = int(ws.cell(r, 10).value or 0)
        prev_gbp = prev_raw * BLD_MONTH_YEAR
        prev_cap = EXTENSION_PREV[base] * BLD_UNIT
        note = ('%s: maintenance at %0.1f per cent of the GBP%0.2f capital a year = GBP%0.2f, '
                'raw %d. The building material sets the rate: brick 0.8-1.5 per cent, steel or '
                'concrete 1.5-2.5, timber 4-8 (measured brick share of capital; timber and '
                'concrete estimated). The previous %d raw was GBP%0.2f a year, %0.1f per cent of '
                'the GBP%0.2f current capital, the station-maintenance conflict recorded in the '
                'evidence. Extension section of the tram and depot report 2026-11-27.'
                % (MARK, share * 100, gbp, maint, sug, prev_raw, prev_gbp,
                   100.0 * prev_gbp / prev_cap, prev_cap))
        ws.cell(r, 27, round(maint, 2))
        ws.cell(r, 28, 1900)
        ws.cell(r, 34, sug)
        ws.cell(r, 31, note)
        append_note(ws.cell(r, 42), note)
        changed.append(('extension maintenance', base, '', round(maint, 2), sug))


# ------------------------------------------------------------------------------------------ main

LEVELS = {}


def read_levels():
    import glob
    import re
    for path in glob.glob(os.path.join(BASE, 'New', 'depots', '*.dat')):
        text = open(path, encoding='utf-8', errors='replace').read()
        for block in re.split(r'(?im)^\s*obj\s*=', text)[1:]:
            name = None
            level = None
            for line in block.splitlines():
                m = re.match(r'\s*name\s*=\s*(\S+)', line, re.I)
                if m:
                    name = m.group(1).strip()
                m = re.match(r'\s*level\s*=\s*(\d+)', line, re.I)
                if m:
                    level = int(m.group(1))
            if name and level is not None:
                LEVELS[name] = level


def main():
    read_levels()
    wc = load_workbook(CAP, data_only=False)
    wm = load_workbook(MAINT, data_only=False)
    changed = []
    capital_tram(wc, changed)
    capital_air_binds(wc, changed)
    capital_depots(wc, changed)
    capital_extensions(wc, changed)
    capital_engine_depots(wc, changed)
    maintenance_tram(wm, changed)
    maintenance_maglev(wm, changed)
    maintenance_depots(wm, changed)
    maintenance_extensions(wm, changed)
    for item in changed:
        print(' | '.join(str(x) for x in item))
    print('\n%d changes' % len(changed))
    if not WRITE:
        print('dry run: pass --write to save')
        return
    os.makedirs(BACKUP, exist_ok=True)
    for src, dst in ((CAP, os.path.join(BACKUP, 'cost-balancing-capital.xlsx')),
                     (MAINT, os.path.join(BACKUP, 'cost-balancing-maintenance.xlsx'))):
        if not os.path.exists(dst):
            shutil.copy2(src, dst)
    wc.save(CAP)
    wm.save(MAINT)
    print('written; backups in', BACKUP)


if __name__ == '__main__':
    main()
