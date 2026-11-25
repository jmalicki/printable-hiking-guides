"""Up the ladder from Stinson Beach: Dipsea -> Steep Ravine -> Pantoll -> Matt Davis -> Stinson Beach; long version on to East Peak."""
PDF='mount-tam-steep-ravine-from-stinson-beach.pdf'
PARK='Mount Tamalpais State Park'            # shown after the title in the hike lists
REGION='bay-area'                            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
OSM_BBOX=(37.888,-122.655,37.936,-122.568)   # S,W,N,E
OSM_HIGHWAYS='|primary|residential'          # the hike starts and ends on the streets of Stinson Beach
TILES=dict(z=15,bbox=(37.884,-122.656,37.936,-122.566))
JUNCTIONS=dict(start=6446794407,             # entrance to the Stinson Beach car park, by the bus stop
               dip=7512211483,               # Dipsea Trail leaves Highway 1
               srj=331384869,                # Dipsea Trail meets Steep Ravine Trail at Webb Creek
               ladder=4908356897,            # foot of the ladder
               pan=331384583,                # top of Steep Ravine Trail at Pantoll
               mdtop=331384579,              # Matt Davis Trail leaves Panoramic Highway opposite Pantoll
               coastal=331384265,            # Matt Davis / Coastal Trail junction, on the open ridge
               mdbot=331383534,              # Matt Davis trailhead on Belvedere Avenue
               wpi=110379914,                # West Point Inn: Old Stage Road meets the Old Railroad Grade
               rgtop=110367487,              # Old Railroad Grade meets East Ridgecrest Boulevard
               summit=361147860,             # East Peak, top of the Plank Walk Trail
               fern=373681047,               # Fern Creek Trail meets the Old Railroad Grade
               hog=373682160,                # east end of Matt Davis Trail on Hogback Road
               nora=1331416933,              # Nora Trail meets Matt Davis Trail
               bj=12823903319)               # Matt Davis Trail meets Bootjack Trail
# Both versions climb Steep Ravine (the ladder is climbed, never descended) and come down Matt Davis.
# Summit version: up the old railway grade past West Point Inn, down Fern Creek Trail and the whole of Matt Davis.
ROUTES={'main':['start','dip','srj','ladder','pan','mdtop','coastal','mdbot','start'],
        'summit':['start','dip','srj','ladder','pan','wpi','rgtop','summit','fern','hog','nora','bj','mdtop','coastal','mdbot','start']}
MD={'Matt Davis Trail'}
LEG_ALLOW={('mdtop','coastal'):MD,('coastal','mdbot'):MD,('hog','nora'):MD,('nora','bj'):MD,
           ('wpi','rgtop'):{'Old Railroad Grade Fire Road'}}
GPX={'main':'Mount Tam: Stinson Beach - Dipsea - Steep Ravine - Pantoll - Matt Davis loop',
     'summit':'Mount Tam: Stinson Beach - Steep Ravine - Pantoll - East Peak - Matt Davis'}
MAIN='main'
# Loop stops are numbered; the summit version's extra stops are lettered.
MAP=dict(bbox=(37.8845,-122.6548,37.9335,-122.5665),k=1.1,scale=(1000,'1 km'),arrow_start=1000,arrow_step=900,arrow_clear=220,
  overlays=[dict(route='summit',frm='pan',to='mdtop',color='BLUE',width=7,dash='18 10')],
  markers=[('start',1),('srj',2),('ladder',3),('pan',4),('coastal',5),('mdbot',6),('wpi','A'),('summit','B'),('hog','C'),('bj','D')],
  labels=[dict(at='start',dx=-26,dy=30,text='START / FINISH',anchor='end',size=21,weight=700),
          dict(at='start',dx=-26,dy=54,text='Stinson Beach',anchor='end',size=19),
          dict(at='srj',dx=0,dy=44,text='Webb Creek',anchor='middle',size=19),
          dict(at='ladder',dx=26,dy=8,text='The ladder',size=21,weight=700),
          dict(at='pan',dx=26,dy=26,text='Pantoll',size=21,weight=700),
          dict(at='coastal',dx=0,dy=-30,text='Open ridge',anchor='middle',size=19),
          dict(at='wpi',dx=24,dy=-14,text='West Point Inn',size=19,color='BLUE',weight=700),
          dict(at='summit',dx=-28,dy=-8,text='East Peak',anchor='end',size=21,color='BLUE',weight=700),
          dict(at='hog',dx=26,dy=20,text='Hogback Road',size=19,color='BLUE'),
          dict(at='bj',dx=26,dy=22,text='Bootjack',size=19,color='BLUE')],
  icons=[])
PROFILE=dict(emin=0,emax=500,grid=100,label_every=100,height=340,km_step=1,
  markers=[('start',1,0),('srj',2,0),('ladder',3,0),('pan',4,0),('coastal',5,0),('mdbot',6,0)],
  notes=[(6500,265,'&#8592; Steep Ravine: 295 m up in 2.6 km, in redwood shade'),(6500,135,'Matt Davis: 445 m down in 3.4 km, facing the ocean &#8594;')])
PROFILES={'summit':dict(emin=0,emax=900,grid=100,label_every=200,height=340,km_step=2,
  markers=[('start',1,0),('srj',2,0),('ladder',3,0),('pan',4,0),('wpi','A',0),('summit','B',0),('hog','C',0),('bj','D',0),('coastal',5,0),('mdbot',6,0)],
  notes=[(10300,240,'Old Stage Road and the railway grade: 240 m up in 5.5 km'),(18300,170,'Matt Davis Trail: 10 km to the sea')])}
ACCESS=dict(**{'from':(37.8078,-122.4750),'to':(37.89799,-122.64129)},z=13,bbox=(37.790,-122.670,37.940,-122.450),
  pad=(260,150,130,120),k=1.0,mk=0.62,scale=(5000,'5 km'),
  markers=[dict(letter='A',at=('m',1700),label='Golden Gate Bridge',dx=-30,dy=9,anchor='end',size=25),
           dict(letter='B',at=('type','off ramp'),label='Exit Hwy 1',dx=30,dy=9,size=25),
           dict(letter='C',at=('name','Shoreline Highway'),label='Tam Junction',dx=-26,dy=36,anchor='end',size=25),
           dict(letter='D',at=('after','Shoreline Highway',4195),label='Panoramic Hwy',dx=0,dy=-32,anchor='middle',size=25),
           dict(letter='E',at=('m',19900),label='Muir Beach',dx=-30,dy=9,anchor='end',size=25),
           dict(letter='P',at=('end',),label='Stinson Beach',dx=0,dy=-32,anchor='middle',size=27,weight=700,fill='RED')],
  places=[dict(at=(37.9060,-122.5475),label='Mill Valley',dx=20,dy=9,size=24),
          dict(at=(37.9038,-122.6040),label='Pantoll',dx=18,dy=-10,size=24),
          dict(at=(37.9290,-122.5777),label='East Peak',dx=18,dy=8,size=24),
          dict(at=(37.8030,-122.4790),label='San Francisco',anchor='end',size=27,weight=700,dot=False)])
# Photos: Wikimedia Commons. crop=(l,t,r,b) fractions.
PHOTOS=dict(
 ladder=dict(file='File:The famous stairs on the Steep Ravine trail - panoramio.jpg',short='The ladder',cls='cover portrait',
   caption='The ladder in Steep Ravine, beside a fall of Webb Creek. One hiker climbs; the next waits.'),
 ravine=dict(file='File:Steep ravine trail.jpg',short='Steep Ravine',cls='tall',
   caption='A footbridge in Steep Ravine.'),
 steps=dict(file='File:Dipsea Race - Course - Steep Ravine.jpg',short='Canyon steps',cls='tall',
   caption='Stone steps between sword ferns on the way up the canyon.'),
 ridge=dict(file='File:Matt Davis Trail Mt Tamalpais (159382381).jpeg',short='Matt Davis ridge',cls='mid',
   caption='The Matt Davis Trail on the open ridge, with fog over the ocean.'),
 beach=dict(file='File:Stinson Beach from Dipsea Trail in Mount Tamalpais State Park.jpg',short='Stinson Beach',cls='hero short',
   caption='Stinson Beach from the Dipsea Trail, twenty minutes into the hike.'),
 sunset=dict(file='File:Foggy sunset over Stinson Beach.jpg',short='Sunset',cls='mid',
   caption='Sunset over Stinson Beach from the hill above the village.'),
 peak=dict(file="File:View of Mt. Tamalpais' East Peak. The Old Railroad Grade fire road is visible below Ridgecrest Blvd - Bolinas Ridge Road. - panoramio.jpg",short='East Peak',cls='mid',
   caption='East Peak, the summit, with the old railway grade cut across the slope below it.'),
)
