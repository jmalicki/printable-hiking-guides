# Hike guides (Mount Tamalpais / Muir Woods)

Printable A4 hiking guides with maps, built from scripts. One folder per guide under `guides/`.

| Guide | Folder | PDF |
|---|---|---|
| Muir Woods by the back door (Mountain Home Inn loop) | `guides/muir-woods` | `out/muir-woods/muir-woods-back-door.pdf` |
| The balcony of Mount Tam (Rock Spring – West Point Inn – Matt Davis – Bootjack) | `guides/west-point` | `out/west-point/mount-tam-west-point-loop.pdf` |

Each `out/<slug>/` also has GPX files (import into CalTopo / Komoot / AllTrails), `guide.html` and page previews.

## Build
- `make` — rebuild every PDF from cached data (no network)
- `make GUIDE=west-point` — one guide
- `make routes-west-point` — recompute a guide's route + GPX from cached trail data
- `make refresh GUIDE=west-point` — re-download trails, basemaps, driving route and photos, then rebuild

## Where to edit
- **Words**: `guides/<slug>/template.html` (placeholders: `{{MAP}} {{PROFILE}} {{ACCESS}} {{PHOTO:key}} {{PHOTO_CREDITS}}`)
- **Route, map labels, profile notes, driving-map markers, photos**: `guides/<slug>/config.py`
- **Shared look**: `guides/shared.css`
- **Finding photos**: `.venv/bin/python scripts/commons_search.py "query"` then add the `File:` title to `PHOTOS` in the config

## New guide
Copy a guide folder, edit `config.py` (bounding boxes, junctions, route order), then
`scripts/fetch.py <slug>`, `scripts/build_routes.py <slug>` (prints leg-by-leg trail names to check), write the template, `make GUIDE=<slug>`.

Needs python3, Google Chrome (headless PDF), venv with pillow + pymupdf (`make .venv`).
Data: trails (c) OpenStreetMap contributors; basemap USGS The National Map; elevation USGS 3DEP via opentopodata.org; driving route OSRM; photos Wikimedia Commons (credited in each guide).
