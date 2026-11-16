#!/bin/sh
# Always build with the latest makeobj: refresh ./makeobj-extended (and the
# Makeobj-Extended-ex-15.exe alias used by other tooling) from the engine
# workspace's makeobj build whenever that is newer. makeobj binaries are git-ignored.
MAKEOBJ_SRC=../../simutrans-extended-sources/simutrans/Makeobj-Extended.exe
for target in ./makeobj-extended ./Makeobj-Extended-ex-15.exe ./Makeobj-Extended.exe; do
    if [ ! -f "$target" ] || [ "$MAKEOBJ_SRC" -nt "$target" ]; then
        cp "$MAKEOBJ_SRC" "$target"
    fi
done
make clean DESTDIR=../../simutrans-extended-sources/simutrans; make DESTDIR=../../simutrans-extended-sources/simutrans -j12
