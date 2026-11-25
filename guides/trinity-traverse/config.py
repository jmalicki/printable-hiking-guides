"""Trinity Alps: Canyon Creek Lakes over the ridge to Mirror and Sapphire Lakes (off-trail crossing)."""
PDF='trinity-alps-canyon-creek-to-sapphire.pdf'
PARK='Trinity Alps Wilderness'            # shown after the title in the hike lists
REGION='hazardous'                       # listed in HAZARDOUS-ROUTES.md, apart from the hikes to go and do
OSM_BBOX=(40.850,-123.090,41.020,-122.780)
TILES=dict(z=14,bbox=(40.855,-123.075,41.020,-122.895))          # overview: trailhead to trailhead
DETAIL_TILES=dict(z=16,bbox=(40.970,-123.040,41.010,-122.990))    # close-up of the off-trail crossing
JUNCTIONS=dict(start=8915020034,                 # Canyon Creek & Bear Creek trailhead
               bclj=4047104465,                  # Boulder Creek Lakes junction
               ucl=10049992397,                  # end of the Canyon Creek Trail at the upper lake
               lpath=(40.9830,-123.0170,['(path)']),   # end of the mapped use path towards L Lake
               sapp=6655949514,                  # west end of the Sapphire use trail (09W20A)
               emer=6655949454,                  # Emerald Lake: Sapphire trail meets Stuart Fork Trail
               sfth=4226278482,                  # Stuart Fork trailhead (Bridge Camp)
               alpj=4226284413,                  # Stuart Fork Trail / Alpine Lake Trail junction
               bcj=8915561082)                   # Alpine Lake Trail / Bear Creek Trail junction
POINTS=dict(llake=(40.98234,-123.01305),col=(40.98801,-123.02320),mirror=(40.99555,-123.02852))
DEM=dict(bbox=(40.974,-123.037,41.003,-123.004),step_m=40)
# off-trail legs, traced over the terrain model between these waypoints (approximate lines, see dem_route.py)
OFFTRAIL={'lpath-llake':[(40.9830,-123.0170),(40.98234,-123.01305)],
          'llake-col':[(40.98234,-123.01305),(40.98801,-123.02320)],
          'col-mirror':[(40.98801,-123.02320),(40.99555,-123.02852)],
          'mirror-sapp':[(40.99555,-123.02852),(41.00109,-123.00684)]}
ROUTES={'main':['start','bclj','ucl','lpath','llake','col','mirror','sapp','emer','sfth'],
        'bear':['emer','alpj','bcj','start']}      # no-shuttle finish: Alpine Lake Trail + Bear Creek Trail back to the car
GPX={'main':'Trinity Alps: Canyon Creek Lakes to Sapphire Lake and out Stuart Fork (off-trail section approximate)'}
MAIN='main'
MK=[('start',1),('bclj',2),('ucl',3),('llake',4),('col',5),('mirror',6),('sapp',7),('emer',8),('sfth',9)]
MAP=dict(pad=170,aspect=180/236,extent=['main'],overlays=[dict(route='bear',frm='alpj',to='start',color='BLUE',width=8,dash='20 11')],markers=MK,icons=[],k=2.0,scale=(2000,'2 km'),arrow_start=1500,arrow_step=2600,arrow_clear=900,
  labels=[dict(at='start',dx=-30,dy=-6,text='START',anchor='end',size=22,weight=700),
          dict(at='start',dx=-30,dy=20,text='Canyon Creek',anchor='end',size=19),
          dict(at='sfth',dx=-30,dy=-6,text='FINISH',anchor='end',size=22,weight=700),
          dict(at='sfth',dx=-30,dy=20,text='Stuart Fork (Bridge Camp)',anchor='end',size=19),
          dict(at='bclj',dx=30,dy=7,text='Boulder Creek jct',size=19),
          dict(at='ucl',dx=30,dy=9,text='Canyon Creek Lakes',size=20,weight=700),
          dict(at='emer',dx=30,dy=7,text='Emerald Lake',size=20,weight=700),
          dict(at=(40.9835,-122.9578),dx=22,dy=6,text='Morris Meadow',size=19),
          dict(at=(40.93526,-123.01805),dx=-22,dy=6,text='Lower Falls',anchor='end',size=18),
          dict(at=(40.9070,-122.9930),dx=0,dy=-16,text='Bear Creek loop finish',anchor='middle',size=18,color='BLUE',weight=700)])
DETAIL=dict(bbox=(40.9725,-123.0385,41.0085,-122.9925),overlays=[],markers=MK,icons=[],k=2.5,scale=(500,'500 m'),arrow_start=13200,arrow_step=900,arrow_clear=330,
  labels=[dict(at='ucl',dx=30,dy=2,text='Upper Canyon Creek Lake',size=20,weight=700),
          dict(at='ucl',dx=30,dy=24,text='trail ends',size=17),
          dict(at='llake',dx=30,dy=8,text='L Lake',size=20,weight=700),
          dict(at='col',dx=30,dy=4,text='Kalmia Pass, {{u:2,260 m|7,420 ft}}',size=20,weight=700),
          dict(at='mirror',dx=-30,dy=8,text='Mirror Lake',anchor='end',size=20,weight=700),
          dict(at='sapp',dx=0,dy=-34,text='Sapphire Lake',anchor='middle',size=20,weight=700),
          dict(at='emer',dx=-30,dy=-14,text='Emerald Lake',anchor='end',size=20,weight=700),
          dict(at=(40.9925,-123.0262),dx=24,dy=0,text='ledge and gully:',size=17,color='RED',weight=700),
          dict(at=(40.9925,-123.0262),dx=24,dy=22,text='line is approximate',size=17,color='RED',weight=700)])
PROFILE=dict(emin=600,emax=2400,grid=200,label_every=400,height=360,km_step=5,
  markers=[('start',1,0),('bclj',2,0),('ucl',3,-14),('llake',4,-6),('col',5,0),('mirror',6,6),('sapp',7,12),('emer',8,22),('sfth',9,0)],
  notes=[(5200,2000,'Day 1: Canyon Creek Trail, 810 m up'),(31000,1900,'Day 3: Stuart Fork Trail, 860 m down in 20 km')])
ACCESS=dict(**{'from':(40.5865,-122.3917),'to':(40.88756,-123.0244)},z=11,bbox=(40.45,-123.20,41.06,-122.28),pad=(230,120,210,120),k=1.0,mk=0.62,scale=(10000,'10 km'),
  extra=[{'from':(40.7310,-122.9420),'to':(40.87353,-122.91854)}],    # Weaverville -> Stuart Fork trailhead (the far end)
  markers=[dict(letter='A',at=('m',300),label='Redding (I-5)',dx=-46,dy=46,anchor='end',size=26),
           dict(letter='B',at=('at',(40.7310,-122.9420)),label='Weaverville',dx=0,dy=62,anchor='middle',size=26),
           dict(letter='C',at=('name','Canyon Creek Road'),label='Junction City',dx=-44,dy=34,anchor='end',size=26),
           dict(letter='P',at=('end',),label='Canyon Creek trailhead',dx=0,dy=-34,anchor='middle',size=27,weight=700,fill='RED'),
           dict(letter='F',at=('at',(40.87353,-122.91854)),label='Stuart Fork trailhead',dx=34,dy=10,size=27,weight=700,fill='RED')],
  places=[dict(at=(40.80,-122.76),label='Trinity Lake',dot=False,size=24,weight=500,anchor='middle')])
# Photos: direct Flickr URLs with explicit credit (Commons has none of Sapphire or Mirror Lake). crop=(l,t,r,b) fractions.
BT='Beyond the Trail (Flickr)'
PHOTOS=dict(
 hero=dict(short='Sapphire from above',cls='hero low',url='https://live.staticflickr.com/3768/10963817393_03b0ac072c_b.jpg',artist=BT,license='CC BY-NC 2.0',page='https://www.flickr.com/photos/garytrinity/10963817393/',crop=(0,0.52,1,0.80),
   caption='Sapphire Lake in its granite trench below Suicide Ridge: the far side of the crossing.'),
 falls=dict(short='Falls',cls='tri',url='https://live.staticflickr.com/5552/14942285052_d81ec0349a_b.jpg',artist='PeterDSims (Flickr)',license='CC BY-NC 2.0',page='https://www.flickr.com/photos/petersims/14942285052/',
   caption='Lower Canyon Creek Falls, day 1.'),
 lowerlake=dict(short='Lower lake',cls='tri',url='https://live.staticflickr.com/1228/1324445388_0a97e8cca8_b.jpg',artist='JoeDuck (Flickr)',license='CC BY 2.0',page='https://www.flickr.com/photos/joeduck/1324445388/',
   caption='Lower Canyon Creek Lake from the slabs above it.'),
 upperlake=dict(short='Upper lake',cls='tri',url='https://live.staticflickr.com/6010/6019811957_9f211a4edf_b.jpg',artist='Tom Hilton (Flickr)',license='CC BY 2.0',page='https://www.flickr.com/photos/tomhilton/6019811957/',
   caption='Upper Canyon Creek Lake under Thompson Peak, where the trail ends.'),
 descent=dict(short='Sapphire from the Mirror Lake side',cls='nd',url='https://live.staticflickr.com/2408/2475906783_681254c1da_b.jpg',artist=BT,license='CC BY-NC-ND 2.0',page='https://www.flickr.com/photos/garytrinity/2475906783/',
   caption='Looking down to Sapphire Lake from the granite below Mirror Lake. Snow can linger here into July.'),
 mirror=dict(short='Mirror Lake',cls='duo',url='https://live.staticflickr.com/7396/10925785044_68eee97307_b.jpg',artist=BT,license='CC BY-NC 2.0',page='https://www.flickr.com/photos/garytrinity/10925785044/',
   caption='Mirror Lake at sunrise: bare granite, no trail, almost no visitors.'),
 relic=dict(short='Mining relic',cls='duo',url='https://live.staticflickr.com/2838/11143318946_89c9e49b9d_b.jpg',artist=BT,license='CC BY-NC 2.0',page='https://www.flickr.com/photos/garytrinity/11143318946/',
   caption='Sapphire Lake: gold-rush machinery left where it stopped.'),
 dam=dict(short='Emerald dam',cls='duo',url='https://live.staticflickr.com/5512/10835668065_2506f18f48_b.jpg',artist=BT,license='CC BY-NC 2.0',page='https://www.flickr.com/photos/garytrinity/10835668065/',
   caption='The hand-laid stone dam at Emerald Lake, built to feed a gold mine 45 km away.'),
)
