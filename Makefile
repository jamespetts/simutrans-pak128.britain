# Just run
#   make clean all archives
# to get fresh and ready to deploy .tbz2 and .zip archives

MAKEOBJ ?= ./makeobj

DESTDIR  ?= simutrans
PAKDIR   ?= $(DESTDIR)/pak128.Britain-Ex
DESTFILE ?= simupak128.Britain-Ex

OUTSIDE :=
OUTSIDE += grounds

DIRS64 :=
DIRS64 += gui/gui64

DIRS128 :=
DIRS128 += air
DIRS128 += attractions
DIRS128 += boats
DIRS128 += bus
DIRS128 += citybuildings
DIRS128 += citycars
DIRS128 += depots
DIRS128 += goods
DIRS128 += gui/gui128
DIRS128 += hq
DIRS128 += industry
# Experimental doesn't treat livery trains separately
# DIRS128 += livery-trains
DIRS128 += london-underground
DIRS128 += maglev
DIRS128 += narrowgauge
DIRS128 += pedestrians
DIRS128 += smokes
DIRS128 += stations
DIRS128 += townhall
DIRS128 += trains
DIRS128 += trams
DIRS128 += trees
DIRS128 += ways

DIRS192 := 
DIRS192 += boats/boats192
DIRS192 := 
DIRS192 += air/air192


DIRS224 := 
DIRS224 += boats/boats224

DIRS256 := 
DIRS256 += air/air256

DIRS := $(OUTSIDE) $(DIRS64) $(DIRS128) $(DIRS192) $(DIRS224) $(DIRS256)


.PHONY: $(DIRS) copy tar zip

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
	@mkdir -p $(PAKDIR)/text $(PAKDIR)/text/citylists $(PAKDIR)/config
	@cp -p compat.tab $(PAKDIR)
	@cp -p config/* $(PAKDIR)/config
#	@mkdir -p $(PAKDIR)/sound $(PAKDIR)/text $(PAKDIR)/config $(PAKDIR)/scenario
#	@cp -p sound/* $(PAKDIR)/sound
#	@cp -p scenario/* $(PAKDIR)/scenario
	@cp -p text/*.tab $(PAKDIR)/text

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
	@$(MAKEOBJ) PAK128 $(PAKDIR)/ $@/ > /dev/null
	@echo -e -n "Obj=ground\nName=Outside\ncopyright=pak128.Britain.Experimental git " >$@/outsiderev.dat
	@svnversion >>$@/outsiderev.dat
	@echo -e "Image[0][0]=images/ls-water-128.0.0\n-" >>$@/outsiderev.dat
	@$(MAKEOBJ) PAK128 $(PAKDIR)/ $@/outsiderev.dat > /dev/null
	@rm $@/outsiderev.dat

clean:
	@echo "===> CLEAN"
	@rm -fr $(PAKDIR) $(DESTFILE).tbz2 $(DESTFILE).zip
