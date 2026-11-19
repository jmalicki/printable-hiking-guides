# Hike guides: notes for agents (and people) writing one

This repo makes printable hiking guides (PDF with maps) from scripts. `README.md` covers the mechanics
(build commands, where config lives). This file covers what the README does not: who the guides are for,
how they should read and look, and the working method that produced them. Read both before starting or
repairing a guide, and read one existing `guides/<slug>/template.html` end to end as the model
(`trinity-traverse` and `four-lakes` for multi-day trips, `west-point` for a day walk).

## Who reads them

A fit visitor who does not know the area: someone who runs or cycles, mostly on flat ground, and is not a
regular mountain walker. Write for that general reader, not for one person or one country. So:

- Do not name the reader's country, city or home hills (no Madrid, Guadarrama, Vaalserberg, Pyrenees).
  Compare effort to things anyone can picture: a brisk walk on the flat, a tall building, "a multi-day walk
  carrying your own gear".
- Still explain what a visitor would not know: fire roads, trailhead parking rules, wilderness permits,
  poison oak, ticks, bear canisters, what a "use trail" is, that kitchens close early.
- **Write the source in British spelling and vocabulary** (kilometres, colour, car park, autumn). The imperial
  build converts to American (center, color, parking lot, fall) through `US_WORDS` in `scripts/hikelib.py`; the
  metric build keeps the British. When you use a British word that is not in that table, add it. Times of day
  as am/pm ("9 pm", "by 7:00").
- They will print it and carry it, so every page must work on paper. Links are a bonus (restaurants,
  permits), never the only way to get a fact.

## Units and paper size (build-time options)

`make` builds **US Letter, feet and miles** by default. `make UNITS=metric PAPER=a4` builds the metric A4
variant, written beside it with a `-metric-a4` suffix. Both must fit the same number of pages.

- **Write templates and config strings in metric.** `hikelib.units()` converts at build time: `9.3 km` to
  miles, `2,260 m` to feet, ranges and signed figures too (`+810 m`, `300–500 m`, `940 → 2,260 m`).
  `X km (Y mi)` and `X m (Y ft)` collapse to the bracketed figure. Map scale bars and profile axes switch too.
- Use `{{u:metric text|imperial text}}` wherever automatic conversion would read badly:
  - words: `{{u:seven kilometres|five miles}}`, `every few hundred {{u:metres|yards}}`;
  - short horizontal distances, which should be fractions of a mile, not thousands of feet: `{{u:600 m|0.4 mi}}`;
  - other units: `{{u:12–15 kg|25–35 lb}}`, `{{u:8 °C|15 °F}}`, `{{u:2 litres|2 quarts (2 liters)}}`;
  - a published figure that differs from the converted one by rounding (`{{u:2,260 m|7,420 ft}}`), so one
    place never shows two values;
  - stat-strip captions that would repeat the headline (`{{u:25 miles, trailhead to trailhead|trailhead to trailhead}}`);
  - things that must not convert: `{{u:10 m|10 m}}` terrain model, and **"jog {{u:5 km|5 km}}"**. A 5K is a
    running distance in the US as well; the owner asked for it to stay.
- After editing text, build both variants and read the imperial output for leftovers ("km", "metres",
  doubled figures such as "18 mi / 18 miles").
- Letter is 18 mm shorter and 6 mm wider than A4. `hikelib.PAGE_CSS` compensates with tighter margins, a 3%
  zoom and narrower full-width maps. `make_pdf.sh` prints `*** OVERFLOW ***` when a PDF has more pages than
  the template has `<section class="page">`; treat that as a failed build.

## Voice

- **Sell the hike, honestly.** Each guide opens with why this walk beats the obvious alternative (walking
  into Muir Woods versus driving to the front door; four lake basins versus the one popular canyon). Then it
  is frank about what is hard.
- **"Is this for me?" is mandatory** and must be blunt: distance, climb, time, what flat-ground fitness does
  and does not prepare you for (descents, uneven footing, heat, altitude, exposure). For anything off trail,
  say that skill matters more than fitness.
- Second person, plain sentences, concrete nouns. No brochure adjectives, no exclamation marks.
- **Titles and the subtitle are written from the walker's position.** The title names a moment the walker
  will have, or a way of experiencing the place: "Muir Woods, by the back door", "The balcony of Mount Tam",
  "A lake behind every ridge: the Four Lakes Loop". The owner rejected "Round the mountain" (the route's
  shape; fits any loop), "Four lakes, one mountain" (a count that restates the trail's name) and "Red rock,
  white rock, four lakes" (a feature list with no walker in it). Test: could the title go on another hike,
  and does it read like a map legend? If so, try again.
  The subtitle is not the itinerary. The rejected one listed the stages, a height and the logistics, all
  of which the stat strip and pitch already carry. The accepted one uses verbs, keeps one number for where
  it impresses, and ends on the honest cost: "Cross one high pass and the trail circles a single peak,
  handing you a new lake each time you top a ridge: four in seven miles… You pay for it on day one."
  (The reasons are the writing agent's inference from this one exchange in November 2026; the owner said
  only which versions they liked and disliked.)
- **Never assert what was not checked.** Unverified items (turn directions from memory, opening hours,
  facilities, road surface, fire and canister rules, ecology written from memory) are either verified against
  a source, worded as uncertain in the guide ("I could not confirm…"), or left out. Tell the owner in chat
  which ones remain unverified. When sources disagree on a figure, use the route's own computed number.
- If the owner's premise is wrong, say so before building on it (Bootjack was not the gentler climb; no
  trail joins Canyon Creek Lakes to Sapphire Lake).
- Hazards get a red `.warn` box on page 1 with explicit "Turn back if" rules. Say on the last page that the
  route was compiled from maps and reports and not walked, when that is the case.

## What every guide contains

In roughly this page order (5–6 pages; see the existing templates):

1. **Cover**: `.kicker`, title, `.sub`, hero photo, the five-cell `.stats` strip (distance, climb, time, high
   point, grade), the pitch, "Is this for me?" as a `.verdict` line plus a `.cmp` table, any `.warn` box.
2. **The route**: map with `.legend`, elevation profile, and for multi-day trips a `.days` stage table.
3. **Step by step**: a table keyed to the map's markers, with cumulative distance, height, trail names as
   signed, which way to turn, and what you see there. Views and points of interest are called out where
   they occur. Include a shorter variant if a sensible one exists.
4. **An inset that explains the place** (`.inset`): why it looks the way it does (West Point: five habitats
   and the fog/geology/aspect reasons; Four Lakes: red peridotite, white granite, cirques). Use "worlds" or
   "habitats", not "biome". Give real numbers with sources if claiming something is special.
5. **Getting there**: driving map with lettered markers, turn-by-turn table, parking stated explicitly
   (including free roadside parking), no-car options, shuttle if needed.
6. **Practical**: when to go, fees/permits, what to bring, hazards, rules.
7. **Afterwards**: where to eat, with links to each restaurant's own site. Open every link and check it is
   the real business (one domain had become a gambling page; it was dropped). No link beats a wrong one.
8. **Sources and photo credits** on the last page.

## House style: what went wrong once and must not again

A first draft of the Four Lakes guide was written without following the existing guides and had to be
rebuilt. Each point below is something that was wrong in it.

- **Use `guides/shared.css` and its classes.** Do not restyle in the template's `<style>` block (it set its
  own body size, heading sizes, table and fact-box styles). The only thing in `<style>` is `{{CSS}}`. New
  layout needs go into `shared.css` as a named class, checked for name collisions.
- **One renderer.** PDFs are made by headless Chrome through `make`. Do not add a second renderer with its
  own stylesheet or markup hooks (`data-print-*` wrappers); the result cannot match the other guides. If
  Chrome is unavailable, say so and stop.
- **Use the page.** Two-column `.cols` layouts with the map beside its legend and stages, as in the other
  guides. A page that is half white, a single narrow column of text, or a map at a third of the page width
  is a layout failure: merge pages or rebalance until every page is at least three-quarters used.
- **Sell first.** The cover needs the pitch against the obvious alternative and the stat strip; a paragraph
  of description under a photo is not a cover.
- **Numbers for the route, letters for extras.** Markers on the main route are numbered in walking order;
  an alternative approach or the driving map uses letters. The same marker appears on the map, the profile,
  the stage table and the step table, drawn with `<span class="num">`.
- **Sizes on maps are in image pixels, so they depend on the tile zoom.** Aim for markers about 2 mm across
  and labels about 6 pt as printed: set the map's `k` so that `19·k` pixels is roughly 2 mm at the printed
  width. A driving map that covers under 60 km needs `z=13` tiles, not `z=11`, or it prints blurred with
  oversized lines. Keep the scale bar clear of markers and move labels off the route line.
- **Profile notes go inside the filled area under the line**, away from marker circles, not across the line.
- **A photo for each place the guide names as a highlight** (each of the four lakes, each habitat), found on
  Commons or Flickr and looked at before use. One hero and one flower is not enough.
- **The cover photo must show its whole subject.** A wide strip crop that cuts the top off the mountain is
  wrong; put the photo beside the pitch at a taller aspect (`figure.cover`) if needed.
- **Elevations come from the shared 10 m source** (`build_routes.py`, cached in `data/elev-cache.json`), so
  every guide's climb figures are comparable. Do not switch source per guide.
- **Check the facts the draft inherited.** Re-read the cited pages and drop or soften what they do not
  support; note conflicts (three sources gave three heights for one pass).
- **Leave shared scripts tidy.** Extend them generically and say what was added; do not leave an unused
  parallel code path behind. (The draft's MuPDF renderer and per-guide raster elevation option were removed.)

## Photos

- The hero must show the thing promised (the West Point hero has to show the San Francisco skyline clearly,
  not fog). Show places as a hiker meets them (the inn with its lawn, people and the view).
- Sources: Wikimedia Commons (`file='File:…'` in config) or Flickr CC via the direct
  `live.staticflickr.com` URL with `artist`, `license`, `page` set by hand. Read the licence on the photo's
  own page. **ND licences must not be cropped** (use the `nd` figure class). Every photo is credited via
  `{{PHOTO_CREDITS}}`.
- Make a contact sheet of candidates and look at it before choosing. If no free photo matches what the
  owner asked for, say so rather than substituting a weak one; they can drop their own file into
  `data/<slug>/photos/<key>.jpg`.

## Maps and data

- Trails from OpenStreetMap (Overpass), basemap USGS topo tiles, elevation USGS 3DEP via opentopodata,
  driving routes from OSRM. AllTrails blocks automated access; do not try to get round it. The GPX in
  `out/<slug>/` is the CalTopo/AllTrails/Komoot hand-off.
- After `build_routes.py`, read the printed leg-by-leg "via" trail names and confirm each leg uses the
  trail the text names. Distances and climbs quoted in the text come from that output, never from memory
  or from another site.
- Main route solid with direction arrows; alternatives in blue dashes; off-trail legs dashed red and shaded
  on the profile.
- Off-trail legs: `dem_route.py` gives a least-steep line between hand-placed waypoints. Cross-check
  against at least two independent trip reports, and label the GPX track as approximate.

## Working method

- Deterministic work goes in scripts, cached under `data/`, so a rebuild costs no network and few tokens.
- After every build, look at the `out/<slug>/preview-N.png` pages (tile several into one image to save
  time) and check: page count, no overflow, no half-empty page, no clipped or overlapping map labels,
  photos rendered and uncropped where it matters. The previews show whichever variant was built last, so
  finish with a plain `make`.
- Ask the owner only real route choices (which trail, which finish). Commit when they ask, and add the
  guide to the table in `README.md`.
- Another session's uncommitted work in this repo is not yours to delete. Work round it and tell the owner.

## Known snags

- Overpass returns 502/timeouts: retry with backoff.
- Wikimedia thumbnails: use standard widths (1280) and pause between requests, or expect 429.
- Constraining a leg to one trail name (`LEG_ALLOW`) fails if OSM has that trail as discontinuous ways.
- `make_pdf.sh` assumes Google Chrome at the macOS default path.
- `fetch.py` skips a photo whose source is unchanged, so replacing a photo means changing its URL or
  deleting the cached file.
