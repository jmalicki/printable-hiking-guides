PY=.venv/bin/python
# `make` rebuilds the guide + PDF from cached data. `make refresh` re-downloads trails/elevation/basemap first.
all: pdf
.venv:
	python3 -m venv .venv && .venv/bin/pip install -q pillow pymupdf
routes: .venv
	$(PY) scripts/build_routes.py
guide: .venv
	$(PY) scripts/build_guide.py
pdf: guide
	sh scripts/make_pdf.sh
refresh: .venv
	$(PY) scripts/fetch_osm.py && $(PY) scripts/build_routes.py && $(PY) scripts/fetch_tiles.py && $(MAKE) pdf
.PHONY: all routes guide pdf refresh
