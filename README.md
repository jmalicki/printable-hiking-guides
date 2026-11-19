# Printable hiking guides

Paper guides to hikes worth the drive: five or six pages you can print, fold into a pocket and follow where a
phone has no signal.

## The idea

Most trail information is either an app that needs signal and battery, or a write-up that sells the hike without
telling you whether you can do it. Each guide here tries to do five things on a few sheets of paper:

- **Make the case for the hike**: why this one, against the obvious alternative.
- **Say honestly who it is for.** Every guide has an "Is this for me?" section: distance, climb, time, and what is
  actually hard about it.
- **Put everything in one place**: a topographic map, an elevation profile, step-by-step directions keyed to the
  map, how to get to the trailhead, and where to eat afterwards.
- **Explain what you are looking at**, where you are standing: the geology, the history, the plants and animals.
- **Warn early.** Snow slopes, rough roads, dry stretches and old mine workings are on page 1, not page 5.

They are written for a fit visitor who does not know the area. They are also honest about their own limits: most
were compiled from maps, land-manager pages and published trip reports and were not walked for the guide, and each
one says so. Check conditions and closures with the land manager before you go.

Everything is built by scripts from open data (OpenStreetMap trails, USGS maps and elevation), so a guide can be
corrected and rebuilt, and new ones added the same way.

## The guides

- **[Bay Area hikes](BAY-AREA-HIKES.md)**: six day hikes around San Francisco Bay, from Mount Tamalpais to the
  Ohlone Wilderness.
- **[Further afield](FURTHER-AFIELD.md)**: the Trinity Alps, Yosemite, Yellowstone and Grand Teton, including
  multi-day backpacking trips.

The finished PDFs are in this repository, under `out/<guide>/`, in two editions: US Letter in feet and miles
(`<name>.pdf`) and A4 in metric (`<name>-metric-a4.pdf`). Each folder also has GPX tracks to load into CalTopo,
Gaia, Komoot or AllTrails.

## Printing a guide

A guide is meant to get rained on. Checked in November 2026; shop offerings and prices change.

**Settings, whatever you print on**
- Use the Letter edition in the US and the A4 edition elsewhere.
- Print at **100% / "actual size"**, not "fit to page", in colour, double-sided. The maps have a drawn scale bar,
  which stays correct at any size, but shrinking makes the map labels harder to read.

**Cheapest: plain paper in a bag.** Print on ordinary paper and carry it folded in a gallon zip-top freezer bag,
map page outwards. Laser prints cope with damp better than inkjet prints: most inkjet colour inks are dye-based
and run when wet. Paper of any kind tears once it is soggy.

**At a print shop: ask for water-resistant paper, not vinyl.**
- **FedEx Office** (formerly Kinko's) sells exactly this, and calls it **"water-resistant paper"**: a thin
  synthetic (plastic) sheet, 8.5 × 11 in, printable in full colour on both sides.
  - Online: *Copies & Custom Documents*, upload the PDF, and choose the water-resistant stock under the specialty
    papers, full colour, double-sided.
  - At the counter: "water-resistant synthetic paper, letter size, full colour, double-sided".
  - It is Letter only, so use the Letter edition. FedEx says it is not fully waterproof: fine in rain, not meant
    to sit under water. It cannot be laminated, and FedEx suggests scoring it before folding. The self-service
    machines appear to take standard paper only, so order online or at the counter.
- **Vinyl** is sign material sold by the square foot. It is the wrong product for a few letter-size pages.
- **Lamination** works but turns each sheet into a stiff card that cannot be folded. It suits one page, such as
  the route map. Staples lists letter-size pouches from about $2 a sheet. Neither Staples nor The UPS Store lists a
  synthetic paper for documents.
- **By post:** Doxzoo prints single copies from a PDF on synthetic sheets in both Letter and A4.

**At home**
- **Laser printer:** Rite in the Rain all-weather printer paper (Letter and A4; a treated paper) or its DuraCopy
  sheets (Letter; a true synthetic). Both print on both sides. The maker says neither is for inkjet printers.
- **Inkjet printer:** most waterproof papers do not take ordinary inkjet ink. Papers such as PuffinPaper and
  iGage Weatherproof are sold for *pigment*-ink inkjets (and lasers), not dye-ink ones. If you are not sure which
  you have, print on plain paper and bag it, or let a shop print it.

## Building and editing

Each guide is a folder under `guides/` holding a `config.py` (route, maps, photos) and a `template.html` (the
words). `out/<guide>/` gets the PDFs, GPX files, `guide.html` and page previews. Style, audience, required sections
and working method for writing a new guide are in `AGENTS.md`: read it first. After adding or changing a guide, run
`scripts/make_index.py` to refresh the two lists above (set `REGION='bay-area'` in the config for a Bay Area hike).

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

## Licence
- Code (`scripts/`, `Makefile`, `guides/shared.css`): MIT, see [LICENSE](LICENSE).
- Guide text, templates, maps and profiles: CC BY 4.0, see [LICENSE-CONTENT.md](LICENSE-CONTENT.md).
- Photos, trail data and basemaps belong to others and keep their own terms: see [NOTICE.md](NOTICE.md) and
  [CREDITS.md](CREDITS.md) (regenerate with `scripts/make_credits.py`).
