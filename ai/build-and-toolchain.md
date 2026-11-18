---
status: draft
verified: New master @ 92c7b701c
---
# Build and toolchain

**Covers**: how the pakset is compiled from `New/`, the build files, and makeobj.

## Initial facts

- Canonical build: run GNU make from inside `New/` via Git Bash / MSYS2. `New/mkpak.sh` first
  refreshes the makeobj binaries from the engine workspace (see below), then runs
  `make clean DESTDIR=../../simutrans-extended-sources/simutrans; make DESTDIR=... -j12`.
  `[CODE New master @ e36ec2321]`
- `New/Makefile` uses `MAKEOBJ ?= ./makeobj-extended` and `DESTDIR ?= .`; the pakset is written
  to `$(DESTDIR)/pak128.Britain-Ex`. `[CODE New master @ e36ec2321]`
- Each source folder is compiled as one `.pak` with a size class: `PAK32`, `PAK64`, `PAK128`,
  `PAK192`, `PAK224`, `PAK256` (the folder-to-size mapping is in the `DIRS32`/`DIRS64`/`DIRS128`
  and similar variables in `New/Makefile`). `[CODE New master @ e36ec2321]`
- The `copy` target copies `config/`, `text/`, `sound/`, `demo.sve`, `licence.txt`, `compat.tab`,
  and `symbol.BigLogo.pak` into the built pakset; these are used directly and not compiled.
  `[CODE New master @ e36ec2321]`
- `New/makeALL.mos` (MOScript, run with mose.py) is an alternative build: `!mose
  min_version 3` requires MOScript version 3 or newer, and `!size` sets the pak size class
  for the folders built after it. `New/parameter.mos`
  defines the absolute makeobj path (`!makeobj`) and output directory (`!OUTPUT`).
  `New/pak128Britain.bat` is a further Windows alternative taking destination and source
  arguments. `[CODE New master @ e36ec2321]`
- **The makeobj used must always be the latest build from the engine workspace.** The
  authoritative binary is `simutrans-extended-sources/simutrans/Makeobj-Extended.exe` (built
  there from the engine source). `New/mkpak.sh` copies it over `New/makeobj-extended` and
  `New/Makeobj-Extended-ex-15.exe` whenever it is newer, before building; when invoking
  makeobj directly (for example `LIST`), use `New/makeobj-extended`. A stale makeobj does not
  fail on unknown keys: it ignores them with an `Entry ... ignored (check spelling)` warning,
  silently dropping new fields (this happened with the citycar comfort fields on 2026-11-15,
  when `Makeobj-Extended-ex-15.exe` proved to be a 2023 build). Always check the compile log
  for `ignored` warnings. **Invocation pitfall:** `makeobj-extended` has no file extension, so
  PowerShell/CreateProcess appends `.exe` and silently runs `Makeobj-Extended.exe` instead —
  under PowerShell invoke `Makeobj-Extended-ex-15.exe` explicitly; under Git Bash the
  extension-less name runs correctly (as the canonical build does). `mkpak.sh` keeps all
  three names refreshed from the engine build so every resolution lands on the latest.
  Run the extension-less binary from Git Bash (`bash -c 'cd <source-folder> &&
  ../../New/makeobj-extended pak128 <out.pak> *.dat'`); PowerShell quoting of a Git Bash
  invocation proved unreliable (2026-11-15).
  `[CODE New ex-15 @ 0ba8d7fc6]` `[USER-DIRECTION:2026-11-15]`
- **Folder argument separator.** A whole folder can be compiled directly from PowerShell with
  `.\makeobj-extended PAK128 pak128.Britain-Ex/citycars.pak citycars/` from `New/`. The source
  folder must end in a **forward slash**. Two wrong forms both fail without a useful message: a
  backslash path (`citycars\`) makes makeobj read the `.dat` files but fail to open
  `./images/...`; a path with no trailing separator (`citycars`) writes an empty pak (a few
  dozen bytes) and **exits 0**, so check the packed-object count or the file size, not just the
  exit code. The `make` binary lives at `C:\msys64\usr\bin\make.exe` when it is not on `PATH`.
  `[EXECUTION-VERIFIED:2026-11-15]`
- Several makeobj builds are present in `New/` (for example `Makeobj-Extended.exe`,
  `Makeobj-Extended-ex-15.exe`, `makeobj-extended`). makeobj binaries are ignored by
  `New/.gitignore`. `[CODE New master @ e36ec2321]`
- `New/Makefile` also has a `simutranslator` target that packages `.dat` and `.png` files into
  zips for upload to simutranslator. `[CODE New master @ e36ec2321]`

## Build destination and engine workspace

- `New/mkpak.sh` passes `DESTDIR=../../simutrans-extended-sources/simutrans` for both `make
  clean` and `make -j12`. The destination is the engine workspace in the directory adjacent to
  this base directory. `[CODE New master @ 92c7b701c]`
- `New/Makefile` defaults `DESTDIR` to the current directory and writes the pakset to the
  `pak128.Britain-Ex` subdirectory of the destination. `[CODE New master @ 92c7b701c]`
- `New/parameter.mos` defines the `!makeobj` executable path and the `!OUTPUT` directory as
  absolute paths inside the same engine workspace. `[CODE New master @ 92c7b701c]`

## Alternative builds and observed differences

- `New/makeALL.mos` declares `!mose min_version 3` and sets `!size` per folder. Its copy set
  includes `readme.txt` in addition to the `New/Makefile` copy set of `config/`, `text/`,
  `sound/`, `demo.sve`, `licence.txt`, `compat.tab`, and `symbol.BigLogo.pak`.
  `[CODE New master @ 92c7b701c]`
- `New/pak128Britain.bat` takes a destination argument and a source argument. It compiles the
  `config/` folder into `BritConfig-Ex`, while `New/Makefile` copies `config/` directly without
  compiling. Its `PAK32` step writes `Holds256-Ex` from `boats/holds/`.
  `[CODE New master @ 92c7b701c]`
- `New/.gitignore` excludes `makeobj-extended*`, `*.exe`, `*.pak`, and `*.sve`. The makeobj
  binaries present in `New/` are therefore untracked. `[CODE New master @ 92c7b701c]`

## Testing the compiled pakset

- The ex-15 engine executable is `Simutrans-Extended-debug-optimised.exe` in the engine
  runtime dir (`../../simutrans-extended-sources/simutrans/` relative to `New/`); it reports
  "Simutrans 123.2 Extended Nightly development build 15.0" and supports `-generate_map`.
  `simutrans-extended.exe` in the same dir is build 14.23 (stale — not ex-15). Only a build
  15.0 exe that supports `-generate_map` is correct for this test.
  `[EXECUTION-VERIFIED:2026-09-24]`
- `New/test-pakset.ps1` (PowerShell) does the automated smoke test: it mirrors
  `New/pak128.Britain-Ex/` over the engine runtime's `pak128.Britain-Ex/` (an out-of-workspace
  write), then runs the ex-15 exe with
  `-objects pak128.Britain-Ex -generate_map -map_size 64,64 -log -nomidi -nosound` and reports
  PASS only on `MAP-GEN: PASS` plus exit code 0. `-generate_map` loads the whole pakset,
  initializes a blank world from the default settings, prints `MAP-GEN: PASS`, and quits
  without entering the game loop; it does NOT save a map or instantiate a specific vehicle.
  `[EXECUTION-VERIFIED:2026-09-24]`
- To confirm a specific new object actually compiled, use
  `./Makeobj-Extended-ex-15.exe LIST pak128.Britain-Ex/<name>.pak` and check the object line
  (e.g. `vehicle douglas-dc-8-10`, `vehicle ger-s69`).
  `[EXECUTION-VERIFIED:2026-09-24]`
- In-game behaviour testing is manual for now: Squirrel (scenario scripting, the usual
  automation path) has been broken and is in the process of being re-integrated. Until it is
  working, the `-generate_map` path neither applies `-startyear` nor
  saves. This needs a blank map at the vehicle's intro year and a person to buy/run it;
  `demo.sve` is 1943 and unsuitable for a 1911 or 1959 introduction.
  `[EXECUTION-VERIFIED:2026-09-24]`

## Planned sections

- Known build pitfalls.

## Open questions

- Is the canonical build the `make` path, or should it be documented differently for releases?
