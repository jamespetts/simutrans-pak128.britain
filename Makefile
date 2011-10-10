# Makefile based on the pak64 Makefile. Thank you prissi et al!
# Makefile for pak128-britain standard and experimental
# 2010-06 sdog 
# 2010-06 neroden
#
# Just run
#   make clean all archives
# to get fresh and ready to deploy .tbz2 and .zip archives
CONFIG ?= config.default
-include $(CONFIG)

MAKEOBJ ?= ./makeobj

PAKNAME ?= pak128.britain.testing
DESTDIR  ?= .
PAKDIR   ?= $(DESTDIR)/$(PAKNAME)
DESTFILE ?= $(PAKNAME)

NAMEPREFIX ?=
NAMESUFFIX ?=

CPFILES ?= compat.tab
CPFILES += readme.txt
CPFILES += licence.txt
CPFILES += demo.sve
CPFILES += config
CPFILES += text
#CPFILES += sound

DIRS64 :=
DIRS64 += gui/gui64

DIRS128 :=
DIRS128 += attractions
DIRS128 += boats
DIRS128 += bus
DIRS128 += citybuildings
DIRS128 += citycars
DIRS128 += depots
DIRS128 += goods
DIRS128 += grounds
DIRS128 += hq
DIRS128 += industry
DIRS128 += london-underground
DIRS128 += maglev
DIRS128 += pedestrians
DIRS128 += smokes
DIRS128 += stations
DIRS128 += townhall
DIRS128 += trains
DIRS128 += trams
DIRS128 += trees
DIRS128 += ways
DIRS128 += gui/gui128

DIRS192 :=
DIRS192 += boats/boats192

DIRS224 :=
DIRS224 += boats/boats224

#Objects in .dat files to be paked into a single pak file
# Actually, this is done as a single directory with one file
SINGLE128 :=
SINGLE128 += pak1file/128


DIRS := $(DIRS64) $(DIRS128) $(DIRS192) $(DIRS224) $(SINGLE128)

#generating filenames
#with this function the filenames are assembled, by removing the dir, adding prefix
#and suffix
make_name = $(NAMEPREFIX)$(notdir $1)$(NAMESUFFIX)
#make_name = $(subst $(NAMEPREFIX)grounds$(NAMESUFFIX),ground.Outside.pak,$(NAMEPREFIX)$(notdir $1)$(NAMESUFFIX))


.PHONY: $(DIRS) copy tar zip clean

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
	@mkdir -p $(PAKDIR)
	@cp -prt $(PAKDIR) $(CPFILES)

$(DIRS64):
	@echo "===> PAK64 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK $(PAKDIR)/$(call make_name,$@) $@/ > /dev/null

$(DIRS128):
	@echo "===> PAK128 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK128 $(PAKDIR)/$(call make_name,$@) $@/ > /dev/null

$(DIRS192):
	@echo "===> PAK192 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK192 $(PAKDIR)/$(call make_name,$@) $@/ > /dev/null

$(DIRS224):
	@echo "===> PAK224 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK224 $(PAKDIR)/$(call make_name,$@) $@/ > /dev/null


$(SINGLE128):
	@echo "===> PAK128 $@"
	@mkdir -p $(PAKDIR)
	@$(MAKEOBJ) quiet PAK128 $(PAKDIR)/ground.Outside.pak $@/ > /dev/null


clean:
	@echo "===> CLEAN"
	@rm -fr $(PAKDIR) $(DESTFILE).tbz2 $(DESTFILE).zip
