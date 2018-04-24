# Just run
#   make clean all archives
# to get fresh and ready to deploy .tbz2 and .zip archives
#
# Change THIS to change the version string encoded in the pak file
# VERSION_STRING = "pak128.Britain-Ex-0.9.3"
#
#
#
MAKEOBJ ?= ./makeobj-extended

DESTDIR  ?= .
PAKDIR   ?= $(DESTDIR)/pak128.Britain-Ex
DESTFILE ?= simupak128.Britain-Ex

# Dirs for simutranslator
TR_DIRS :=

OUTSIDE :=
OUTSIDE += pak1file/128
TR_DIRS += pak1file/128

DIRS32 :=
DIRS32 += boats/holds
TR_DIRS += boats/holds

DIRS64 :=
DIRS64 += gui/gui64
TR_DIRS += gui

DIRS128 :=
DIRS128 += air
TR_DIRS += air
DIRS128 += attractions
TR_DIRS += attractions
DIRS128 += boats
TR_DIRS += boats
DIRS128 += bus
TR_DIRS += bus
DIRS128 += citybuildings
TR_DIRS += citybuildings
DIRS128 += citycars
TR_DIRS += citycars
DIRS128 += depots
TR_DIRS += depots
DIRS128 += goods
TR_DIRS += goods
DIRS128 += grounds
TR_DIRS += grounds
DIRS128 += gui/gui128
DIRS128 += hq
TR_DIRS += hq
DIRS128 += industry
TR_DIRS += industry
DIRS128 += london-underground
TR_DIRS += london-underground
DIRS128 += maglev
TR_DIRS += maglev
DIRS128 += narrowgauge
TR_DIRS += narrowgauge
DIRS128 += pedestrians
TR_DIRS += pedestrians
DIRS128 += smokes
TR_DIRS += smokes
DIRS128 += stations
TR_DIRS += stations
DIRS128 += signalboxes
TR_DIRS += signalboxes
DIRS128 += townhall
TR_DIRS += townhall
DIRS128 += trains
TR_DIRS += trains
DIRS128 += trams
TR_DIRS += trams
DIRS128 += trees
TR_DIRS += trees
DIRS128 += ways
TR_DIRS += ways

DIRS192 := 
DIRS192 += boats/boats192
DIRS192 += air/air192

DIRS224 := 
DIRS224 += boats/boats224

DIRS256 := 
DIRS256 += air/air256

DIRS := $(OUTSIDE) $(DIRS32) $(DIRS64) $(DIRS128) $(DIRS192) $(DIRS224) $(DIRS256)


.PHONY: $(DIRS) copy tar zip simutranslator

all: copy $(DIRS)

archives: tar zip

tar: $(DESTFILE).tbz2
zip: $(DESTFILE).zip

$(DESTFILE).tbz2: $(PAKDIR)
	@echo "===> TAR $@"
	@tar cjf $@ $(DESTDIR)

$(DESTFILE).zip: $(PAKDIR)
	@echo "===> ZIP $@"
	@zip -rq $@ $(DESTDIR)

copy:
	@echo "===> COPY"
	@mkdir -p $(PAKDIR)/config
	@cp -p config/* $(PAKDIR)/config
	@mkdir -p $(PAKDIR)/text 
	@cp -p text/*.* $(PAKDIR)/text
#   @mkdir -p $(PAKDIR)/text/citylists 
	@mkdir -p $(PAKDIR)/sound
	@cp -p sound/* $(PAKDIR)/sound
#	@mkdir -p $(PAKDIR)/scenario
#	@cp -p scenario/* $(PAKDIR)/scenario
	@cp -p demo.sve $(PAKDIR)
	@cp -p licence.txt $(PAKDIR)
	@cp -p compat.tab $(PAKDIR)
	@cp -p symbol.BigLogo.pak $(PAKDIR)

$(DIRS32):
	@echo "===> PAK32 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK32 $(PAKDIR)/ $@/ > /dev/null

$(DIRS64):
	@echo "===> PAK64 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK $(PAKDIR)/ $@/ > /dev/null

$(DIRS128):
	@echo "===> PAK128 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK128 $(PAKDIR)/ $@/ > /dev/null

$(DIRS192):
	@echo "===> PAK192 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK192 $(PAKDIR)/ $@/ > /dev/null

$(DIRS224):
	@echo "===> PAK224 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK224 $(PAKDIR)/ $@/ > /dev/null

$(DIRS256):
	@echo "===> PAK256 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK256 $(PAKDIR)/ $@/ > /dev/null

$(OUTSIDE):
	@echo "===> OUTSIDE with REVISION and grounds"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK128 $(PAKDIR)/ $@/ > /dev/null

clean:
	@echo "===> CLEAN"
	@rm -fr $(PAKDIR) $(DESTFILE).tbz2 $(DESTFILE).zip simutranslator/*.zip

# -----------
# Everything after this point in the Makefile is designed for
# the generation of zip files to upload to simutranslator
# written by Nathanael Nerode
# -----------

# The following image files are too large for simutranslator.
OVERSIZE_IMAGES :=
OVERSIZE_IMAGES += attractions/images/cur/football-ground-lg.png
OVERSIZE_IMAGES += attractions/images/cur/cricket-ground-sm.png
OVERSIZE_IMAGES += boats/images/clan-line-steamer.png
OVERSIZE_IMAGES += boats/images/handysize.png


# For each zip file to generate,
# (1) Use 'find' to get everything under the directory;
# (2) But exclude everything in 'blends';
# (3) And only collect files with .dat and .png endings;
# (4) Then use zip, but exclude "known bad" image files.

simutranslator/%.zip:
	FILE_LIST=`find -path ./$*/\* \! -path ./$*/blends/\* \( -name \*.dat -o -name \*.png \)` ; \
	zip -r $@ $$FILE_LIST -x $(OVERSIZE_IMAGES)

# Special case: Program texts
simutranslator/program_texts.zip:
	zip $@ simutranslator/*.dat

# Convert the list of TR_DIRS to a list of TR_ZIPFILES
TR_ZIPFILES := $(patsubst %,simutranslator/%.zip, $(TR_DIRS) )

# Finally, depend on all the individual zipfiles.
simutranslator: $(TR_ZIPFILES)

# Potential problems.
# - The entire attractions folder may be too big to do in one go.
# - separate out the stone attractions?
STONE_ATTRACTIONS :=
STONE_ATTRACTIONS += attractions/stone-attractions.dat
STONE_ATTRACTIONS += attractions/images/cur/stone-attractions.png 
STONE_ATTRACTIONS += attractions/images/cur/stone-attractions-snow.png
# - The entire boats folder may also be too big
# - separate out the large boats?
# - The entire trains folder may ALSO be too big
