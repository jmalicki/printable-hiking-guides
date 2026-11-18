PY=.venv/bin/python
GUIDES=$(notdir $(patsubst %/config.py,%,$(wildcard guides/*/config.py)))
# make                      rebuild every guide's PDF from cached data (no network)
# make GUIDE=west-point     just one guide
# make refresh GUIDE=...    re-download trails, basemaps, driving route, photos, then rebuild
ifdef GUIDE
GUIDES=$(GUIDE)
endif
all: $(GUIDES:%=pdf-%)
.venv:
	python3 -m venv .venv && .venv/bin/pip install -q pillow pymupdf
routes-%: .venv
	$(PY) scripts/build_routes.py $*
pdf-%: .venv
	$(PY) scripts/build_guide.py $* && sh scripts/make_pdf.sh $*
refresh: .venv
	for g in $(GUIDES); do $(PY) scripts/fetch.py $$g && $(PY) scripts/build_routes.py $$g && $(MAKE) pdf-$$g; done
.PHONY: all refresh
