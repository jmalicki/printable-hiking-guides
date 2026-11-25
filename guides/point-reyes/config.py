"""Point Reyes: Bear Valley Trail to the coast at the Arch Rock junction, a short stretch of the Coast Trail,
then the Sky Trail along Inverness Ridge, over Mount Wittenberg and back down to Bear Valley."""
PDF='point-reyes-bear-valley-sky-trail-loop.pdf'
PARK='Point Reyes National Seashore'            # shown after the title in the hike lists
REGION='bay-area'            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
OSM_BBOX=(37.985,-122.835,38.045,-122.790)
TILES=dict(z=15,bbox=(37.982,-122.842,38.047,-122.784))
JUNCTIONS=dict(start=6448397338,                 # Bear Valley trailhead, south end of the car park
               mwj=317861482,                    # Mount Wittenberg Trail leaves the Bear Valley Trail
               meadowj=317881734,                # Meadow Trail
               divide=317885154,                 # Divide Meadow: Old Pine Trail
               glenj=317845743,                  # Bear Valley / Glen / Baldy junction (bike racks)
               archj=317858318,                  # Bear Valley Trail meets the Coast Trail (Arch Rock junction)
               skyj=317858377,                   # Coast Trail / Sky Trail
               baldy=317853572,                  # Sky / Baldy
               oldpine=317860529,                # Sky / Old Pine
               woodward=317853268,               # Sky / Woodward Valley
               skymeadow=317845222,              # Sky / Meadow / Mount Wittenberg trails
               saddle=317845197,                 # Mount Wittenberg Trail / Z Ranch Trail / summit path
               summit=317845076)                 # top of Mount Wittenberg
# The shorter version is the valley out and back (turn round at 'archj'): it retraces the main line, so it has no route of its own.
ROUTES={'main':['start','mwj','meadowj','divide','glenj','archj','skyj','baldy','oldpine','woodward','skymeadow','saddle','summit','saddle','mwj','start']}
MAIN='main';GPX={'main':'Point Reyes: Bear Valley, Coast Trail, Sky Trail and Mount Wittenberg loop'}
MK=[('start',1),('divide',2),('glenj',3),('archj',4),('skyj',5),('baldy',6),('skymeadow',7),('summit',8)]
MAP=dict(pad=150,aspect=0.62,extent=['main'],icons=[],k=1.25,scale=(1000,'1 km'),overlays=[],
  markers=MK,arrow_start=700,arrow_step=1100,arrow_clear=260,
  labels=[dict(at='start',dx=28,dy=-4,text='START / FINISH',size=24,weight=700),
          dict(at='start',dx=28,dy=20,text='Bear Valley',size=23),
          dict(at='divide',dx=28,dy=8,text='Divide Meadow',size=23),
          dict(at='glenj',dx=-28,dy=8,text='Glen Trail junction',anchor='end',size=23),
          dict(at='archj',dx=28,dy=24,text='Arch Rock junction',size=23),
          dict(at='skyj',dx=-28,dy=8,text='Sky Trail',anchor='end',size=23),
          dict(at='baldy',dx=-28,dy=8,text='Baldy Trail',anchor='end',size=23),
          dict(at='skymeadow',dx=-28,dy=8,text='Meadow Trail',anchor='end',size=23),
          dict(at='summit',dx=28,dy=-12,text='MOUNT WITTENBERG',size=24,weight=700)])
PROFILE=dict(emin=0,emax=450,grid=50,label_every=100,height=215,km_step=2,
  markers=[('start',1,0),('divide',2,0),('glenj',3,0),('archj',4,-8),('skyj',5,8),('baldy',6,0),('skymeadow',7,-10),('summit',8,10),('start_end',1,0)],
  notes=[(10600,120,'Sky Trail: 360 m up in 6 km')])
ACCESS=dict(**{'from':(37.9455,-122.5190),'to':(38.03990,-122.79960)},z=13,bbox=(37.90,-122.84,38.08,-122.49),pad=(260,260,170,170),k=1.8,scale=(5000,'5 km'),
  markers=[dict(letter='A',at=('m',0),label='US-101, exit 450B',dx=-52,dy=17,anchor='end',size=50),
           dict(letter='B',at=('m',8800),label='Fairfax',dx=52,dy=17,size=50),
           dict(letter='C',at=('m',20500),label='Samuel P. Taylor park',dx=52,dy=17,size=50),
           dict(letter='D',at=('name','Shoreline Highway'),label='Olema',dx=52,dy=17,size=50),
           dict(letter='P',at=('end',),label='Bear Valley',dx=-40,dy=-58,anchor='start',size=54,weight=700,fill='RED')],
  places=[])
# Photos: Wikimedia Commons. No free photo of the coast at the Arch Rock junction was found except the Park Service's own, taken a week after the 2020 fire.
PHOTOS=dict(
 hero=dict(short='Cover',cls='hero',file='File:Point Reyes National Seashore - Sky Trail, CA, USA - panoramio (1).jpg',caption='Drakes Bay and Limantour Spit from the Sky Trail.'),
 fog=dict(short='Fog on the ridge',cls='tri',file='File:Point Reyes National Seashore, Sky Trail, Ca, USA - panoramio.jpg',caption='Fog coming over Inverness Ridge, from the Sky Trail.'),
 bay=dict(short='Drakes Bay',cls='tri',file='File:Point Reyes National Seashore - Sky Trail, Ca, USA - panoramio.jpg',caption='Drakes Bay under the fog, from the Sky Trail.'),
 sky=dict(short='Sky Trail',cls='bio',file='File:Point Reyes National Seashore - Sky Trail, CA, USA - panoramio.jpg',caption='On the Sky Trail.'),
 divide=dict(short='Divide Meadow',cls='bio',file='File:Point Reyes Divide Meadow.jpg',caption='Divide Meadow.'),
 burn=dict(short='Woodward Fire',cls='bio',file='File:Woodward Fire - Burn Mosaic - September 15, 2020 - 9-39 am (f3080bec-5f4a-4e23-a2cb-0a1d1a7f6f61).jpg',caption='The burn in September 2020.'),
 coast=dict(short='Coast Trail',cls='bio',file='File:Woodward Fire - Burnt Coyote Bush and Point Resistance - August 23, 2020 - 10-24 am (45cc9514-0274-4ef1-9318-979aa0e90b09).jpg',caption='The Coast Trail days after the 2020 fire, looking north to Point Resistance.'),
 quail=dict(short='California quail',cls='bio',file='File:California quail - Point Reyes National Seashore 2021-10-16 02.jpg',crop=(0,0.14,1,1),caption='California quail at Point Reyes.'),
)
