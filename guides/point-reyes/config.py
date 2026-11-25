"""Point Reyes: Bear Valley to Wildcat Camp, Wildcat Beach to the foot of Alamere Falls, the Coast Trail north,
then the Sky Trail over Mount Wittenberg and back down to Bear Valley."""
PDF='point-reyes-alamere-falls-wittenberg.pdf'
PARK='Point Reyes National Seashore'            # shown after the title in the hike lists
REGION='bay-area'            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
OSM_BBOX=(37.945,-122.850,38.050,-122.775)
TILES=dict(z=15,bbox=(37.946,-122.856,38.049,-122.768))
JUNCTIONS=dict(start=6448397338,                 # Bear Valley trailhead, south end of the car park
               mwj=317861482,                    # Mount Wittenberg Trail leaves the Bear Valley Trail
               meadowj=317881734,                # Meadow Trail
               divide=317885154,                 # Divide Meadow: Old Pine Trail
               glenj=317845743,                  # Bear Valley / Glen / Baldy junction (bike racks)
               loopj=317846081,                  # Glen Trail / Glen Camp Loop
               spurj=317846364,                  # Glen Trail / Coast-Glen Spur north
               stewj=317855162,                  # Glen Trail meets the Stewart Trail
               coaststew=317847183,              # Stewart Trail / Coast Trail above Wildcat Camp
               wildcat=4514811524,               # Wildcat Camp
               beach=317847355,                  # end of the path from the camp onto Wildcat Beach
               archj=317858318,                  # Coast Trail / Bear Valley Trail (Arch Rock junction)
               skyj=317858377,                   # Coast Trail / Sky Trail
               baldy=317853572,                  # Sky / Baldy
               oldpine=317860529,                # Sky / Old Pine
               woodward=317853268,               # Sky / Woodward Valley
               skymeadow=317845222,              # Sky / Meadow / Mount Wittenberg trails
               saddle=317845197,                 # Mount Wittenberg Trail / Z Ranch Trail / summit path
               summit=317845076)                 # top of Mount Wittenberg
POINTS=dict(falls=(37.95400,-122.78370))        # sand at the foot of Alamere Falls
# The beach leg is not a mapped trail: data/point-reyes/offtrail.json holds hand-placed points along the sand ('beach-falls').
ROUTES={'main':['start','mwj','meadowj','divide','glenj','loopj','spurj','stewj','coaststew','wildcat','beach','falls','beach','wildcat','coaststew','archj','skyj','baldy','oldpine','woodward','skymeadow','saddle','summit','saddle','mwj','start'],
        'short':['start','mwj','meadowj','divide','glenj','loopj','spurj','stewj','coaststew','wildcat','beach','falls','beach','wildcat','coaststew','archj','glenj','divide','meadowj','mwj','start']}
MAIN='main';GPX={'main':'Point Reyes: Bear Valley, Alamere Falls by Wildcat Beach, Mount Wittenberg (beach line approximate)','short':'Point Reyes: Bear Valley to Alamere Falls, back by the Bear Valley Trail'}
MK=[('start',1),('divide',2),('glenj',3),('stewj',4),('wildcat',5),('falls',6),('archj',7),('skyj',8),('baldy',9),('skymeadow',10),('summit',11)]
MAP=dict(pad=170,aspect=0.60,extent=['main'],icons=[],k=1.7,scale=(1000,'1 km'),
  overlays=[dict(route='short',frm='archj',to='glenj_end',color='BLUE',width=7,dash='14 9')],
  markers=MK,arrow_start=900,arrow_step=1500,arrow_clear=320,
  labels=[dict(at='start',dx=28,dy=-4,text='START / FINISH',size=24,weight=700),
          dict(at='start',dx=28,dy=20,text='Bear Valley',size=23),
          dict(at='divide',dx=28,dy=8,text='Divide Meadow',size=23),
          dict(at='glenj',dx=28,dy=8,text='Glen Trail junction',size=23),
          dict(at='wildcat',dx=-28,dy=-4,text='Wildcat Camp',anchor='end',size=24,weight=700),
          dict(at='falls',dx=-28,dy=8,anchor='end',text='ALAMERE FALLS',size=24,weight=700),
          dict(at=(37.9620,-122.7895),dx=-14,dy=0,text='Wildcat Beach',anchor='end',size=23,color='RED',weight=700),
          dict(at='archj',dx=-28,dy=28,text='Arch Rock junction',anchor='end',size=23),
          dict(at='skyj',dx=-28,dy=-6,text='Sky Trail',anchor='end',size=23),
          dict(at='baldy',dx=-28,dy=8,text='Baldy Trail',anchor='end',size=23),
          dict(at='summit',dx=28,dy=-12,text='MOUNT WITTENBERG',size=24,weight=700),
          dict(at=(37.9955,-122.8050),dx=-10,dy=0,text='short cut',anchor='end',size=25,color='BLUE',weight=700)])
PROFILE=dict(emin=0,emax=450,grid=50,label_every=100,height=215,km_step=2,
  markers=[('start',1,0),('divide',2,0),('glenj',3,0),('stewj',4,0),('wildcat',5,-10),('falls',6,0),('archj',7,0),('skyj',8,10),('baldy',9,0),('skymeadow',10,-12),('summit',11,10),('start_end',1,0)],
  notes=[])
ACCESS=dict(**{'from':(37.9455,-122.5190),'to':(38.03990,-122.79960)},z=13,bbox=(37.90,-122.84,38.08,-122.49),pad=(260,260,360,360),k=1.8,scale=(5000,'5 km'),
  markers=[dict(letter='A',at=('m',0),label='US-101, exit 450B',dx=-52,dy=14,anchor='end'),
           dict(letter='B',at=('m',8800),label='Fairfax',dx=52,dy=14),
           dict(letter='C',at=('m',20500),label='Samuel P. Taylor park',dx=52,dy=14),
           dict(letter='D',at=('name','Shoreline Highway'),label='Olema',dx=52,dy=14),
           dict(letter='P',at=('end',),label='Bear Valley',dx=-52,dy=14,anchor='end',size=40,weight=700,fill='RED')],
  places=[])
# Photos: Wikimedia Commons.
PHOTOS=dict(
 hero=dict(short='Cover',cls='hero',file='File:Wildcat Waterfall - panoramio (1).jpg',caption='Alamere Falls from Wildcat Beach, the way this hike reaches it.'),
 beach=dict(short='Wildcat Beach',cls='tri',file='File:Wildcat beach at Point Reyes National Seashore 2.JPG',caption='Wildcat Beach under its bluffs. The falls are at the far end.'),
 coast=dict(short='Coast Trail',cls='tri',file='File:Wildcat beach at Point Reyes National Seashore 3.JPG',caption='Looking back along the coast from above Wildcat Beach.'),
 sky=dict(short='Sky Trail',cls='bio',file='File:Point Reyes National Seashore - Sky Trail, CA, USA - panoramio.jpg',caption='On the Sky Trail.'),
 divide=dict(short='Divide Meadow',cls='bio',file='File:Point Reyes Divide Meadow.jpg',caption='Divide Meadow.'),
 burn=dict(short='Woodward Fire',cls='bio',file='File:Woodward Fire - Burn Mosaic - September 15, 2020 - 9-39 am (f3080bec-5f4a-4e23-a2cb-0a1d1a7f6f61).jpg',caption='The burn in September 2020.'),
 falls=dict(short='The falls',cls='bio',file='File:In Awe (Unsplash).jpg',caption='At the foot of the falls.'),
 elk=dict(short='Tule elk',cls='bio',file='File:Tule elk bull.jpg',caption='Tule elk bull at Point Reyes.'),
)
