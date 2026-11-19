# Hike guides: notes for agents (and people) writing one

This repo makes printable A4 hiking guides (PDF with maps) from scripts. `README.md` covers the mechanics
(build commands, where config lives). This file covers what the README does not: who the guides are for,
how they should read and look, and the working method that produced the first three. Read both before
starting a new guide, and read one existing `guides/<slug>/template.html` end to end as the model.

## Who reads them

A fit visitor who does not know the area. So:

- **Metric first**, imperial in brackets where a US sign or map will show it: `9.3 km (5.8 mi)`, `2,260 m (7,420 ft)`.
- **A4**, British spelling (kilometres, colour); durations as plain ranges ("2–2½ hours").
- Explain American things a visitor would not know: fire roads, trailhead parking rules, wilderness permits,
  poison oak, ticks, bear canisters, what a "use trail" is.
- Compare effort and landscape to things they know: flat running/cycling in the Netherlands, and the
  Sierra de Guadarrama / Madrid climate. Do not overdo it; one or two references per guide.
- They will print it and carry it, so every page must work on paper. Links are a bonus (restaurants, permits), never the only way to get a fact.

## Voice

- **Sell the hike, honestly.** Each guide opens with why this walk beats the obvious alternative (walking
  into Muir Woods versus driving to the front door; the balcony view; the crossing nobody signs). Then it
  is frank about what is hard.
- **"Is this for me?" is mandatory** and must be blunt: distance, climb, time, what flat-land fitness does
  and does not prepare you for (descents, uneven footing, heat, altitude, exposure). For anything off trail,
  say that skill matters more than fitness.
- Second person, plain sentences, concrete nouns. No brochure adjectives, no exclamation marks.
- Titles are an image plus a plain subtitle: "Muir Woods, by the back door", "The balcony of Mount Tam",
  "Over the top: …".
- **Never assert what was not checked.** Unverified items (turn directions from memory, opening hours,
  facilities, fire rules, ecology written from memory) are either verified against a source, worded as
  uncertain in the guide, or left out. Tell the owner in chat which ones remain unverified.
- If the owner's premise is wrong, say so before building on it (Bootjack was not the gentler climb; no
  trail joins Canyon Creek Lakes to Sapphire Lake).
- Off-trail or hazardous sections get a red `.warn` box on page 1 and explicit "Turn back if" rules. Say
  in the guide that the line was traced from trip reports and a terrain model, not walked.

## What every guide contains

In roughly this page order (5–6 pages; see the existing templates):

1. **Cover**: title, hero photo, stat strip (distance, climb, time, high/low point), the pitch, "Is this for me?".
2. **The route**: full-page-width map, elevation profile, and for multi-day trips a stage table.
3. **Step by step**: a numbered table keyed to the map's lettered/numbered markers, with cumulative km,
   trail names as signed, and what you see there. Views and points of interest are called out where they
   occur, not in a separate essay. Include a shorter variant if a sensible one exists.
4. **An inset that explains the place**: why it looks the way it does (West Point: five habitats and the
   fog/geology/aspect reasons; Trinity: granite, glaciers, conifers). Use "worlds" or "habitats", not
   "biome" (these are plant communities inside one biome; the West Point guide has a box saying so).
   Give real numbers with sources if claiming something is special.
5. **Getting there**: driving map with lettered markers, turn-by-turn notes, parking stated explicitly
   (including free roadside parking), no-car options, shuttle if needed.
6. **Practical**: when to go, fees/permits, what to bring, hazards, rules.
7. **Afterwards**: where to eat, with links to each restaurant's own site. Check every link resolves to the
   real business (one domain had become a gambling page; it was dropped). No link is better than a wrong one.
8. **Sources and photo credits** on the last page.

## Photos

- Only where they add something, but: the hero must show the thing promised (the West Point hero has to
  show the San Francisco skyline clearly, not fog), and when the guide describes several habitats or
  stages, **each one gets its own photo** that actually illustrates it.
- Show places as a hiker meets them (the inn with its lawn, people and the view), not a generic postcard.
- Sources: Wikimedia Commons (`file='File:…'` in config) or Flickr CC via the direct
  `live.staticflickr.com` URL with `artist`, `license`, `page` set by hand. Read the licence on the photo's
  own page. **ND licences must not be cropped** (use the `nd` figure class). Every photo is credited via `{{PHOTO_CREDITS}}`.
- Look at the downloaded image before using it. If no free photo matches what the owner asked for, say so
  rather than substituting a weak one; they can drop their own file into `data/<slug>/photos/<key>.jpg`.

## Maps and data

- Trails from OpenStreetMap (Overpass), basemap USGS topo tiles, elevation USGS 3DEP via opentopodata,
  driving routes from OSRM. AllTrails blocks automated access; do not try to get round it. The GPX in
  `out/<slug>/` is the CalTopo/AllTrails/Komoot hand-off.
- After `build_routes.py`, read the printed leg-by-leg "via" trail names and confirm each leg uses the
  trail the text names. Distances and climbs quoted in the text come from `routes.json`, never from memory.
- Main route solid with direction arrows; alternatives in a second colour; off-trail legs dashed and
  shaded on the profile. Marker letters on the map, profile and step table must agree.
- Off-trail legs: `dem_route.py` gives a least-steep line between hand-placed waypoints. Cross-check
  against at least two independent trip reports, and label the GPX track as approximate.

## Working method

- Deterministic work goes in scripts, cached under `data/`, so a rebuild costs no network and few tokens.
  Extend `scripts/` and `guides/shared.css` generically rather than special-casing one guide.
- After every build, open the `out/<slug>/preview-N.png` pages and check: page count unchanged, no
  overflow onto an extra page, no clipped map labels, photos rendered. Fix by trimming text or adjusting
  `pad`/`k`/label anchors in the config.
- CSS class names are global across guides; a new figure class must not collide with a layout class
  (`setting` did; it became `fogpic`).
- Ask the owner only real route choices (which trail, which finish). Commit when they ask, one commit per
  guide or per round of changes, and add the guide to the table in `README.md`.

## Known snags

- Overpass returns 502/timeouts: retry with backoff.
- Wikimedia thumbnails: use standard widths (1280) and pause between requests, or expect 429.
- Constraining a leg to one trail name (`LEG_ALLOW`) fails if OSM has that trail as discontinuous ways.
- `make_pdf.sh` assumes Google Chrome at the macOS default path.
