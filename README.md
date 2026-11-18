# Muir Woods by the back door

Printable A4 hiking guide + map: Mountain Home Inn -> Panoramic -> Canopy View (down) -> Muir Woods -> Bootjack (up) -> Troop 80 -> back, plus a driving map from the Golden Gate Bridge.

## Outputs (`out/`)
- `muir-woods-back-door.pdf` — the guide (5 pages)
- `muir-woods-main.gpx`, `muir-woods-short.gpx` — import into CalTopo / Komoot / AllTrails / Gaia
- `guide.html`, `preview-N.png` — intermediate render and page previews

## Rebuild
- `make` — rebuild guide + PDF from cached data (no network)
- `make routes` — recompute routes/GPX from cached OSM data (elevation is cached in `data/elev-cache.json`)
- `make refresh` — re-download OSM trails, elevation and basemap tiles, then rebuild everything

## Where to edit
- **Words** (pitch, fitness, directions, food): `guide/template.html`
- **Which trails the routes follow**: `ROUTES` / junction node ids in `scripts/build_routes.py`
- **Map styling, labels, elevation profile**: `scripts/build_guide.py`
- **Driving route / access map**: `scripts/fetch_access.py` (OSRM), drawn in `scripts/build_guide.py`
- **Map extent / basemap**: `scripts/fetch_tiles.py` (USGS Topo, public domain)

Needs: python3, Google Chrome (headless PDF), a venv with pillow + pymupdf (`make .venv`).
Data: trail lines (c) OpenStreetMap contributors; elevation USGS 3DEP via opentopodata.org.
