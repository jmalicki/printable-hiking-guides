# Hike guides: notes for agents (and people) writing one

This repo makes printable hiking guides (PDF with maps) from scripts. `README.md` covers the mechanics
(build commands, where config lives). This file covers what the README does not: who the guides are for,
how they should read and look, and the working method that produced them. Read both before starting or
repairing a guide, and read one existing `guides/<slug>/template.html` end to end as the model
(`trinity-traverse` and `four-lakes` for multi-day trips, `west-point` for a day walk).

## How to read this file

Most of what follows records a decision the owner made about **one guide**, with the case that prompted it.
Treat each as "in a situation like that one, do this", not as something every guide must now contain.
Over-reading has already cost rework twice: a remark that the owner liked one guide's "Read this first"
box turned into disclaimers on a guide that needed none, and a request for road warnings turned into a
label on every road, including paved ones.

- **The owner liking something once is not a request for it everywhere.** Each element has to earn its
  place on the hike in front of you.
- **Check the condition before applying a rule.** The table below says when each optional element belongs.
- **Do not escalate.** If a rule says "a line", do not write a paragraph; if it says "sparingly", most
  guides get none.
- **Existing guides are the tie-breaker.** If a comparable guide does without something, the new one
  probably should too. When a new guide seems to need an element no guide has, ask the owner first.
- **Dated notes about the owner's reasons that say "inference" are guesses.** Follow the example, hold the
  explanation loosely.

| Element | Belongs when | Does not belong when |
|---|---|---|
| Cover pitch, stat strip, "Is this for me?", map, profile, step table, getting there, practical, sources | always | |
| Red `.warn` box on page 1 | a real hazard (snow slope, off-trail ground, old mine workings), or directions that rest on thin evidence where being wrong is dangerous | an ordinary signed trail; general unfamiliarity; facts you could verify |
| Red "author has not done this hike" banner (`.unwalked`) | every guide the owner has not hiked: the very top of page 1, above the kicker | a hike the owner has done. Ask if you do not know |
| "I could not confirm…" in the text | one fact that matters to the plan and cannot be checked (a bear-canister rule) | routine details: verify them or leave them out |
| Inset explaining the place | the place has something that needs explaining (habitats, geology, a mine) | nothing does: do not manufacture one |
| History in the step table, date tags, date strip | the hike is about its history (Almaden) | a hike with a ruin or two: a sentence at that stop is enough |
| Wildlife inset | the owner asks, or animals are a reason to go | otherwise a line under "Watch for" |
| Water section | overnight trips | day hikes: one line in Practical on whether there is a tap |
| "Last water" sign in the step table | a stretch dry and long enough to be dangerous | ordinary gaps between streams |
| Road warning box, and its line on page 1 | an unpaved approach graded "mixed reports" or "high clearance" | paved or good gravel: "any car should be fine" in the running text, nothing more |
| A photo of a named place | it shows the reader something they need to recognise or want to see | filling space; the original brief was "only where they add something" |
| Shorter variant, no-car option, food | a sensible one exists | none does: leave it out, heading and all. No line saying there is none |

## Who reads them

A fit visitor who does not know the area: someone who runs or cycles, mostly on flat ground, and is not a
regular mountain walker. Write for that general reader, not for one person or one country. So:

- Do not name a reader's country, city or home hills, or compare the hike to places only some readers know.
  Compare effort to things anyone can picture: a brisk walk on the flat, a tall building, "a multi-day walk
  carrying your own gear".
- Still explain what a visitor would not know: fire roads, trailhead parking rules, wilderness permits,
  poison oak, ticks, bear canisters, what a "use trail" is, that kitchens close early.
- **"Hike", not "walk", for the trip itself** ("Why this hike", "a day hike", "the most popular hike in the
  range", "hikers"). "Walk" stays as an ordinary verb ("walk down to the lake") and for flat ground ("a brisk
  walk on the flat"). The owner corrected this in November 2026.
- **Write the source in British spelling and vocabulary** (kilometres, colour, car park, autumn). The imperial
  build converts to American (center, color, parking lot, fall) through `US_WORDS` in `scripts/hikelib.py`; the
  metric build keeps the British. When you use a British word that is not in that table, add it. Times of day
  as am/pm ("9 pm", "by 7:00"). Write phone numbers as `+1 408 535 4070`; the imperial build prints them the
  American way, `(408) 535-4070`.
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
  - other units: `{{u:12–15 kg|25–35 lb}}`, `{{u:8 °C|15 °F}}`;
  - a published figure that differs from the converted one by rounding (`{{u:2,260 m|7,420 ft}}`), so one
    place never shows two values;
  - stat-strip captions that would repeat the headline (`{{u:25 miles, trailhead to trailhead|trailhead to trailhead}}`);
  - **water is in litres in both builds.** Write `2 litres` plain, with no `{{u:}}` override: the imperial
    build only respells it ("2 liters"). American hikers measure water bottles and bladders in liters, and
    the owner had every "quart" removed (November 2026). Do not write quarts, gallons or fluid ounces for
    drinking water;
  - things that must not convert: `{{u:10 m|10 m}}` terrain model, and **"jog {{u:5 km|5 km}}"**. A 5K is a
    running distance in the US as well; the owner asked for it to stay.
- After editing text, build both variants and read the imperial output for leftovers ("km", "metres",
  doubled figures such as "18 mi / 18 miles").
- Letter is 18 mm shorter and 6 mm wider than A4. `hikelib.PAGE_CSS` gives both the same working width
  (tight margins plus a 3% zoom on Letter, 5% on A4), so a layout that fits Letter fits A4. `make_pdf.sh` prints `*** OVERFLOW ***` when a PDF has more pages than
  the template has `<section class="page">`; treat that as a failed build.

## Voice

- **Sell the hike, honestly.** Each guide opens with why this walk beats the obvious alternative (walking
  into Muir Woods versus driving to the front door; four lake basins versus the one popular canyon). Then it
  is frank about what is hard.
- **"Is this for me?" is mandatory** and must be blunt: distance, climb, time, what flat-ground fitness does
  and does not prepare you for (descents, uneven footing, heat, altitude, exposure). For anything off trail,
  say that skill matters more than fitness.
- Second person, plain sentences, concrete nouns. No brochure adjectives, no exclamation marks.
- **Do not report an absence.** Every sentence gives the reader something to act on or look at. The
  Almaden guide had an "Afterwards" section that opened "New Almaden has no café", a "Without a car"
  section that read "I found no public transport to New Almaden", and a parking line ending "I found no
  reliable account of how early". The owner had all three removed: each records what the research turned
  up empty, and the reader can do nothing with it. The cause was filling in the outline: a heading from
  the model guide was kept and then had to say something. When a section has nothing to offer, delete the
  heading with it. Two things survive this rule. An absence the reader plans around is stated as a plain
  fact where they plan ("no water at the trailhead", "no shuttle between the trailheads" on a
  point-to-point trip). And one "I could not confirm" is allowed for a fact the plan depends on, as
  below. Before finishing, search the template for "no ", "none", "I found no" and "could not" and
  justify each hit.
- **Headings inside the guide follow the same rule as titles: one plain phrase that says something about
  this place.** The owner called "Quicksilver: what it was for, who dug it, and what it left" AI slop. It
  is a label, a colon, and then a three-part list that is only a table of contents for the paragraphs
  under it. It became "The mercury behind the Gold Rush", and the bold run-in heads under it went from
  "What it was for", "Who dug it", "What it left" to "Gold needed it", "The miners", "The waste". What
  failed was the combination: a label, a colon, and a string of "what/who/why" clauses. Test: if the
  heading could be generated from the paragraph headings below it, it adds nothing. This is narrow. A
  plain label that lists what a section holds ("Parking, fees and the gate", "Grass, cattle and ponds")
  is fine, and so is a short question the section answers ("Why this way round", "Will there be water?").
  A subagent told to apply the first wording of this rule rewrote five such headings in the Murietta
  guide, and they were put back.
  One exception the owner kept: **"Who lives here"** (or "Who lives here now") as the head for the animals
  paragraph. It recurs from guide to guide (West Point, Murietta Falls, Purisima) as a running thread, so
  use those words wherever a guide has that paragraph and do not "fix" it.
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
- **Never assert what was not checked, and check before hedging.** First try to verify (a second source, the
  agency's own page, the route data). What still cannot be confirmed is left out if it is minor, or stated
  once as uncertain if the reader's plan depends on it ("I could not confirm whether the canister rule
  covers Deer Creek"). A guide sprinkled with "I could not confirm" reads as unreliable; one or two such
  lines is normal, five is a sign the research is not finished. Tell the owner in chat what remains
  unverified. When sources disagree on a figure, use the route's own computed number.
- **Do not be cagey, and do not disclaim by reflex.** The red box is for hazards and for guidance that
  rests on thin evidence where being wrong is dangerous (the off-trail crossing in the Trinity traverse).
  An ordinary signed trail in a park needs no "nobody walked this" warning: the owner asked why the Almaden
  guide had one when the others did not, and it was removed. That a guide was compiled and not walked is said
  once, in the red banner at the top of page 1 (see "Hikes the author has not done"), and again in a few
  words in the sources footer ("Compiled November 2026; not walked for this guide"). It still does not go in
  the `.warn` box, which is for hazards. Never put
  tooling problems in a guide (a blocked web page is not the reader's concern), and do not hedge facts you
  could verify with a little more work: verify them.
- **A page that refuses automated fetching (HTTP 403) is not unreadable.** Open it in the browser pane and
  read it there before writing around it; the county park pages for Almaden read fine that way. PDFs opened
  in the browser pane trigger a download prompt for the owner, so ask before opening one.
- If the owner's premise is wrong, say so before building on it (Bootjack was not the gentler climb; no
  trail joins Canyon Creek Lakes to Sapphire Lake).
- **Warnings up front, when there is something to warn about.** A hazard, or a rough road, goes in a red
  `.warn` box on page 1 so it is read before anything is planned. The owner singled out the Trinity
  traverse's "Read this first" box as something they love: it says in bold what the reader must know
  before committing (the off-trail line is approximate and unsurveyed) and what to do about it (carry a
  real map, phone the ranger station), with explicit "Turn back if" rules. What they liked is a serious
  warning stated plainly and early. It is not a licence to open every guide with caveats: the Muir Woods
  and West Point guides have no red box at all, and that is correct.

## Hikes the author has not done

The owner's rule (November 2026): **a guide to a hike the owner has not done says so in a red banner at the
very top of page 1**, above the kicker, so nobody reads the pitch as a first-hand recommendation.

- Markup: `<div class="unwalked">The author has not done this hike. This guide is compiled from maps,
  agency pages and other hikers' reports.</div>` as the first element inside the first
  `<section class="page">`. Keep that wording unless the guide needs something more specific (a
  reconstructed route says "reconstructed" there).
- `scripts/make_index.py` sees the banner and prints the same sentence under the guide's entry in the hike
  lists, so the index carries it too.
- The sources footer still ends "Compiled <month year>; not walked for this guide".
- The banner states a fact about the guide. It is separate from the `.warn` box: an unwalked guide to an
  ordinary signed trail gets the banner and no red box.
- Most guides before November 2026 are hikes the owner knows well and have no banner. When starting a guide,
  ask the owner whether they have done the hike if they have not said.

## What a guide contains

In roughly this page order (5–6 pages; see the existing templates). Items 1–3, 5, 6 and 8 are in every
guide; 4 and 7 only when there is something to say:

1. **Cover**: `.kicker`, title, `.sub`, hero photo, the five-cell `.stats` strip (distance, climb, time, high
   point, grade), the pitch, "Is this for me?" as a `.verdict` line plus a `.cmp` table, any `.warn` box.
2. **The route**: map with `.legend`, elevation profile, and for multi-day trips a `.days` stage table.
3. **Step by step**: a table keyed to the map's markers, with cumulative distance, height, trail names as
   signed, which way to turn, and what you see there. Views and points of interest are called out where
   they occur. Include a shorter variant if a sensible one exists.
4. **An inset that explains the place** (`.inset`), when the place needs explaining: why it looks the way it does (West Point: five habitats
   and the fog/geology/aspect reasons; Four Lakes: red peridotite, white granite, cirques). Use "worlds" or
   "habitats", not "biome". Give real numbers with sources if claiming something is special.
5. **Getting there**: driving map with lettered markers, turn-by-turn table, parking stated explicitly
   (including free roadside parking), a no-car option if one exists, shuttle if needed.
6. **Practical**: when to go, fees/permits, what to bring, hazards, rules.
7. **Afterwards**: where a hiker in boots would actually eat nearby; if there is nowhere, no section. Links to each restaurant's own site. Open every link and check it is
   the real business (one domain had become a gambling page; it was dropped). No link beats a wrong one.
8. **Sources and photo credits** on the last page, wrapped in `<div class="foot">` so they sit at the
   bottom of the page as footnotes, not directly under the last paragraph (the owner asked for this).

## History woven into the route

This section applies when the history is the reason for the hike (Almaden Quicksilver is the model). A
hike that merely passes an old cabin gets one sentence at that stop and none of the machinery below.
Where it does apply, the history goes **where the hiker is standing**, not in an essay at the back. The owner asked for this, on the pattern of the red and white rock
in the Four Lakes guide.

- **The step-by-step table carries it.** Each stop says what to do and then what happened on that spot and
  what is left to see. A red date tag (`<span class="tag when">1866</span>`) opens the stop, so the table
  reads as a timeline even though the trail does not visit things in date order.
- **A strip of dated moments** (`<div class="dates">`, six cells) under the map gives the whole story in
  thirty seconds, so the stops make sense in any order.
- **One inset** (`.inset`) holds what does not belong to a single spot: why the thing is here (geology),
  what it was for, who did the work and on what terms, and what it left behind. Be as blunt about the
  cost (poisoned workers, unequal pay, pollution still in the creek) as about the achievement.
- **The title and pitch come from the story**, written from the walker's position. For Almaden the owner preferred the people to the engineering: "The ghost towns of
  Mine Hill" replaced "A hundred miles of tunnel under your boots".
- **Say what remains.** For every site, state what is physically there today (a fenced furnace, a sealed
  portal, a flagpole), so nobody hikes to a ruin that is only a sign.
- **History needs sourcing more than anything else in a guide.** Local history pages repeat each other's
  errors. Give figures only when two sources agree or name the range; put the disagreements in a small
  note at the foot of the inset; drop superlatives that trace back to a plaque ("richest mine in
  California"); mark single-source stories as such. Do not add motives or explanations of your own to
  events (why Lincoln backed down, why the Cornish were hired) unless a source gives them.
- Use a period photograph if a public-domain one exists, credited with photographer and date.

## Backpacking guides: water

Overnight guides only. A day hike needs one line in Practical saying whether there is a tap. Any overnight
guide has a **Water** section (`.cols.water`), because the reader plans the trip around it.
Research it properly: the Forest Service pages, then dated trip reports, and note the month and year of
each observation. It has two halves:

- **Where it is**, in walking order by day or approach: where the trail is beside water and where it is out
  of reach, the dry stretches, which sources fail late in the season or in dry years (give the dated
  report), and whether trailheads and nearby campgrounds have a tap and in which months.
- **How clean, and what to do to it.** Say plainly whether the water is clear or carries silt, tannin or
  debris, i.e. whether a filter or tablets alone are enough or it needs settling or pre-filtering first.
  Give the official treatment advice. Then what is upstream: heavy camping, pack stock, cattle, old mines,
  recent burns, unusual geology. Where you found nothing, say "I found no report of…" rather than "there
  is none".

**"Last water" signs** (`<span class="tag water">` in the step table, like "last gas 40 miles"): the owner
wants these **used sparingly, only for a stretch long and dry enough that running short would be
dangerous**. Ordinary gaps between streams go in the Water section only. The two so far: L Lake to Mirror
Lake on the Trinity traverse (5–10 hours off trail), and the Stoney Ridge climb late in the season (8 km
and 700 m in the sun with no sure water and no tap at the trailhead).

## The drive: rating the road to the trailhead

This matters only for unpaved approaches; most trailheads are on paved roads and get no treatment at all.
The owner's rule: **an easy road gets a few words in the running text ("any car should be fine") and no
box; a rough or high-clearance road gets a red box that cannot be missed** (`<div class="roadwarn">` with a
`<span class="h">` heading, inside the driving-table cell). **A rough or high-clearance road is also flagged on page 1**, as a bold line in
the red `.warn` box with the page number of the directions, so the reader sees it before choosing a
trailhead or a vehicle. The owner asked for this: the driving page alone is too late.

| Grade | In the guide | When |
|---|---|---|
| Easy | plain sentence: "any car should be fine" | Paved, or Forest Service level 3–5 with reports agreeing |
| Mixed reports | amber box, `<div class="roadwarn mixed">`: "Road warning · rated for cars, reports mixed · length" | Level 3 on paper (officially fit for ordinary cars) but first-hand reports disagree or describe ruts and rock. Stoney Ridge is the model case |
| High clearance | red box, `<div class="roadwarn">`: "High-clearance road · length" | Level 2 ("not maintained for passenger cars"), or the agency itself says high clearance or 4WD. The last hill to Stuart Fork is the model case |

The owner wants these two kept **distinct**: "mixed reports" must say that the road is officially rated for
cars and that the doubt comes from reports; "high clearance" is the official rating. Both are warnings, and
both are flagged on page 1 in words that keep the same distinction ("may be rough… mixed reports" versus
"needs high clearance").

- The official basis is the **Forest Service road maintenance level** (2 = high-clearance vehicles, 3 =
  "a prudent driver in a standard passenger car"). Look a road up by number in the FS road data
  (`apps.fs.usda.gov/arcx/rest/services/EDW/EDW_RoadBasic_01/MapServer/0`, fields `OPER_MAINT_LEVEL` and
  `SURFACE_TYPE`); the MVUM layer (`EDW_MVUM_01/MapServer/1`) gives seasonal opening dates.
- **In the guide, the box heading plus a short description is enough**: length, surface (gravel, bare dirt), width,
  the official level in brackets, what to expect (ruts, rock, a ford, a steep hill), seasonal closure dates,
  unsigned forks, whether phone maps misroute, and which trailhead is the easier drive when there is a
  choice. **Do not recite trip reports in the guide**; the owner said the rating and a description would
  have been enough to choose the other trailhead.
- Reports are for grading, behind the scenes. The level states what a road is maintained for, not its
  condition this year, so read dated first-hand reports and grade down when they disagree with the level.
  Check the level against the road geometry, not from memory or distance alone: Stoney Ridge is level 3 for
  the whole drive (the level 2 section starts just past the turn), and it is graded "rough" because of a
  2016 Forest Service note against low cars and the owner's own recollection of wishing for a truck.

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
- **A photo for each thing the guide is built around** (each of the four lakes, each of the five habitats),
  found on Commons or Flickr and looked at before use. This is about the handful of headline subjects,
  not every stop in the step table: photos go only where they add something.
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
- Never leave a build that printed `OVERFLOW` on disk for long: that PDF has stray near-empty pages, and
  the owner may open it while you are still fitting text. Fix the fit before doing anything else.
- After every build, look at the `out/<slug>/preview-N.png` pages (tile several into one image to save
  time) and check: page count, no overflow, no half-empty page, no clipped or overlapping map labels,
  photos rendered and uncropped where it matters. The previews show whichever variant was built last, so
  finish with a plain `make`.
- Ask the owner only real route choices (which trail, which finish). Commit when they ask, then run
  `scripts/make_index.py` so the guide appears in `BAY-AREA-HIKES.md` or `FURTHER-AFIELD.md` (set
  `REGION='bay-area'` in its config for a Bay Area hike).
- Another session's uncommitted work in this repo is not yours to delete. Work round it and tell the owner.

## Known snags

- Overpass returns 502/timeouts: retry with backoff.
- Wikimedia thumbnails: use standard widths (1280) and pause between requests, or expect 429.
- Constraining a leg to one trail name (`LEG_ALLOW`) fails if OSM has that trail as discontinuous ways.
- `make_pdf.sh` assumes Google Chrome at the macOS default path.
- `fetch.py` skips a photo whose source is unchanged, so replacing a photo means changing its URL or
  deleting the cached file.

## Wildlife

The owner asked for wildlife sidebars (Paintbrush–Cascade is the model, November 2026), on the pattern of
the history and geology insets. One `.inset` of `.biome3` rows, a photo each: what the animal is, how to
recognise it, **where on this loop to look** (keyed to the route markers), and the park's distance rules up
front. They also asked that the smaller animals get named, not only bears and moose: the weasel family
(short-tailed weasel/stoat, long-tailed weasel, marten, mink, otter, badger, wolverine), marmots, pikas.
It need not be a separate panel per group; mentioning the species is enough. Do not be cagey about it: the owner had a "what I could not place" disclaimer (no source names these
animals in these canyons; locations inferred from habitat) removed. Saying where each animal lives by
habitat is fine without a caveat. Still note in the caption when a photo was not taken in the park.

**Each wildlife page is built from what is seen on that trail, not from the last guide's list.** The first
Bighorn Peak page reused the Paintbrush–Cascade rows (pika, marmot, weasels, marten each with a photo) and
the owner, who has hiked it, sent it back: those animals are everywhere in the Teton canyons and scarce
here, while what this trail has is elk bugling, a lot of bears, and grouse. Before choosing rows:

- Run `scripts/inat_counts.py <slug>` (iNaturalist records inside the guide's `OSM_BBOX`; add a pad such as
  `0.1` if the box is thin). At Bighorn Peak it would have shown moose, bears, elk and two kinds of grouse,
  and no pika, weasel, marten or sheep. Counts are small and skewed towards animals near roads, so read
  them as a ranking, not a census.
- Tally what dated first-hand trip reports say they saw, heard or found sign of. If four reports of a
  trail mention no sheep, the page must not promise sheep.
- A photo row goes to an animal with records or reports on this trail. Animals placed only by habitat
  ("lives in talus", "found in conifer forest") share one short row, which says they are thinly spread
  here. Birds count: check them too.
- Lead with what the hiker is most likely to meet, see sign of, or hear, and say which of those it is.
- Ask the owner what they saw if they have hiked it.
