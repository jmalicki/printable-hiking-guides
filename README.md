# Hike guides (Mount Tamalpais, Muir Woods, Trinity Alps)

Printable hiking guides with maps (US Letter in feet and miles by default; A4 and metric as a build option), built from scripts. One folder per guide under `guides/`.

| Guide | Folder | PDF |
|---|---|---|
| Muir Woods by the back door (Mountain Home Inn loop) | `guides/muir-woods` | `out/muir-woods/muir-woods-back-door.pdf` |
| The balcony of Mount Tam (Rock Spring – West Point Inn – Matt Davis – Bootjack) | `guides/west-point` | `out/west-point/mount-tam-west-point-loop.pdf` |
| Trinity Alps: Canyon Creek Lakes over Kalmia Pass to Sapphire Lake (off-trail traverse) | `guides/trinity-traverse` | `out/trinity-traverse/trinity-alps-canyon-creek-to-sapphire.pdf` |
| Four lakes around Siligo Peak (Long Canyon and Stoney Ridge entrances) | `guides/four-lakes` | `out/four-lakes/trinity-alps-four-lakes-loop.pdf` |
| Behind the Grand Teton: Paintbrush Canyon, Paintbrush Divide, Lake Solitude and Cascade Canyon from String Lake | `guides/paintbrush-cascade` | `out/paintbrush-cascade/grand-teton-paintbrush-cascade-loop.pdf` |
| Almaden Quicksilver: the Mine Hill mining-history loop from the Hacienda entrance | `guides/almaden-quicksilver` | `out/almaden-quicksilver/almaden-quicksilver-mine-hill-loop.pdf` |
| Chasing the rain to Murietta Falls (Ohlone Wilderness from Del Valle, out and back) | `guides/murietta-falls` | `out/murietta-falls/ohlone-murietta-falls.pdf` |

Each `out/<slug>/` also has GPX files (import into CalTopo / Komoot / AllTrails), `guide.html` and page previews.

Style, audience, required sections and working method for writing a new guide are in `AGENTS.md`. Read it first.

## Build
- `make` — rebuild every PDF from cached data (no network)
- `make UNITS=metric PAPER=a4` — the metric A4 variant, written as `<name>-metric-a4.pdf` (defaults: `UNITS=imperial PAPER=letter`). Templates are written in metric and converted at build time; `{{u:metric text|imperial text}}` overrides the conversion
- `make GUIDE=west-point` — one guide
- `make routes-west-point` — recompute a guide's route + GPX from cached trail data
- `make refresh GUIDE=west-point` — re-download trails, basemaps, driving route and photos, then rebuild

## Where to edit
- **Words**: `guides/<slug>/template.html` (placeholders: `{{u:metric|imperial}} {{MAP}} {{DETAIL}} {{PROFILE:route}} {{PROFILE}} {{ACCESS}} {{PHOTO:key}} {{PHOTO_CREDITS}}`)
- **Route, map labels, profile notes, driving-map markers, photos**: `guides/<slug>/config.py`
- **Shared look**: `guides/shared.css`
- **Finding photos**: `.venv/bin/python scripts/commons_search.py "query"` then add the `File:` title to `PHOTOS` in the config; or a Flickr CC photo by direct URL with `artist`, `license`, `page`

## Off-trail legs
`scripts/dem_route.py <slug>` samples a terrain grid (config `DEM`) and traces a least-steep line between the waypoints in `OFFTRAIL`; `build_routes.py` splices those legs in and marks them so maps draw them dashed. The traced line is an approximation for the map, not a surveyed track. A guide can also have a close-up map (`DETAIL`, `DETAIL_TILES`, `{{DETAIL}}`) and extra driving routes (`ACCESS['extra']`).

## New guide
Copy a guide folder, edit `config.py` (bounding boxes, junctions, route order), then
`scripts/fetch.py <slug>`, `scripts/build_routes.py <slug>` (prints leg-by-leg trail names to check), write the template, `make GUIDE=<slug>`.

Needs python3, Google Chrome (headless PDF), venv with pillow + pymupdf (`make .venv`).
Data: trails (c) OpenStreetMap contributors; basemap USGS The National Map; elevation USGS 3DEP via opentopodata.org; driving route OSRM; photos Wikimedia Commons and Flickr (credited in each guide).
