"""Yosemite: Clouds Rest from Tenaya Lake (Sunrise Lakes trailhead), out and back; lower Sunrise Lake as the short variant."""
PDF='yosemite-clouds-rest-from-tenaya-lake.pdf'
OSM_BBOX=(37.750,-119.515,37.845,-119.425)
TILES=dict(z=15,bbox=(37.758,-119.508,37.840,-119.440))
JUNCTIONS=dict(th=11189397252,                 # Sunrise Lakes trailhead, Tioga Road
               foot=(37.80949,-119.46218),     # foot of the switchbacks
               sunrise=477214315,              # top of the switchbacks: Sunrise Lakes Trail leaves
               lower=477214498,                # lower Sunrise Lake, where the trail meets the shore
               ponds=(37.79167,-119.45955),    # pond in the basin
               forsyth=477470128,              # Forsyth Trail leaves
               ridge=9750868409,               # bypass path leaves, bare summit ridge starts
               summit=3768355649)              # Clouds Rest
OUT_=['th','foot','sunrise','ponds','forsyth','ridge','summit']
ROUTES={'main':OUT_+OUT_[-2::-1],'lakes':['th','foot','sunrise','lower']}
MAIN='main'
GPX={'main':'Clouds Rest from Tenaya Lake (Sunrise Lakes trailhead), out and back','lakes':'Lower Sunrise Lake from Tenaya Lake (one way)'}
MK=[('th',1),('foot',2),('sunrise',3),('ponds',4),('forsyth',5),('summit',6)]
MAP=dict(bbox=(37.7605,-119.5020,37.8385,-119.4410),icons=[],k=1.4,scale=(1000,'1 km'),
  overlays=[dict(route='lakes',frm='sunrise',to='lower',color='BLUE',width=10,dash='18 10')],
  markers=MK+[('lower','A')],
  arrow_start=900,arrow_step=1100,arrow_end=9300,arrow_clear=260,
  labels=[dict(at='th',dx=-28,dy=-14,text='Sunrise Lakes trailhead',anchor='end',size=24,weight=700),
          dict(at='foot',dx=28,dy=8,text='foot of the switchbacks',size=23),
          dict(at='sunrise',dx=-28,dy=8,text='Sunrise Lakes junction',anchor='end',size=23),
          dict(at='lower',dx=28,dy=8,text='lower Sunrise Lake',size=23,color='BLUE'),
          dict(at='ponds',dx=28,dy=8,text='the pond',size=23),
          dict(at='forsyth',dx=28,dy=10,text='Forsyth Trail junction',size=23),
          dict(at='summit',dx=28,dy=-10,text='Clouds Rest',size=25,weight=700),
          dict(at=(37.7725,-119.4853),dx=-22,dy=0,text='bare ridge',anchor='end',size=22,color='RED',weight=700)])
PROFILE=dict(emin=2300,emax=3100,grid=100,label_every=200,height=250,km_step=2,
  markers=[('th',1,0),('foot',2,0),('sunrise',3,0),('ponds',4,0),('forsyth',5,0),('summit',6,0),('forsyth_end',5,0),('ponds_end',4,0),('sunrise_end',3,0),('foot_end',2,0),('th_end',1,0)],
  notes=[(1250,2390,'flat forest'),(3200,2390,'+290 m'),(5500,2390,'down, then level'),(8500,2390,'+250 m to the top'),(14900,2390,'back up: +105 m'),(17600,2390,'steep descent')])
V_=(37.74850,-119.58700)      # Yosemite Village
TH_=(37.82573,-119.46999)
ACCESS=dict(**{'from':V_,'to':TH_},z=12,bbox=(37.64,-119.92,38.00,-119.08),pad=(330,1090,560,130),k=1.4,mk=0.55,scale=(10000,'10 km'),
  extra=[{'from':(37.95760,-119.11930),'to':TH_,'color':'INK'}],
  markers=[dict(letter='A',at=('at',V_),label='Yosemite Valley',dx=30,dy=40,size=30,weight=700),
           dict(letter='B',at=('name','Big Oak Flat Road'),label='Big Oak Flat Road',dx=-28,dy=10,anchor='end',size=28),
           dict(letter='C',at=('name','Tioga Road'),label='Crane Flat',dx=-28,dy=-14,anchor='end',size=28),
           dict(letter='D',at=('at',(37.81070,-119.48520)),label='Olmsted Point',dx=-10,dy=48,anchor='end',size=28),
           dict(letter='P',at=('end',),label='Sunrise Lakes trailhead',dx=24,dy=36,size=30,weight=700,fill='RED'),
           dict(letter='E',at=('at',(37.91080,-119.25800)),label='Tioga Pass entrance',dx=-28,dy=-16,anchor='end',size=28),
           dict(letter='L',at=('at',(37.95760,-119.11930)),label='Lee Vining',dx=-26,dy=-14,anchor='end',size=30,weight=700)],
  places=[dict(at=(37.80030,-119.87440),label='Big Oak Flat entrance',dx=18,dy=-16,size=27),
          dict(at=(37.87350,-119.35870),label='Tuolumne Meadows',dx=-6,dy=-22,size=27,anchor='middle'),
          dict(at=(37.86950,-119.64900),label='White Wolf',dx=16,dy=-12,size=27)])
PHOTOS=dict(
 hero=dict(file='File:Yosemite Panorama - Flickr - Moo.The.Cow.jpg',short='Summit view',cls='hero',
   caption='South-west from the summit ridge: Half Dome from above, Tenaya Canyon falling away to Yosemite Valley, and the ridge you have just walked along in the foreground.'),
 olmsted=dict(file='File:Olmsted Point vista.jpg',short='From Olmsted Point',cls='duo',
   caption='Where you are going, seen from Olmsted Point on the drive in: Clouds Rest is the long ridge on the left, Half Dome the small shape in the distance.'),
 tenaya=dict(file='File:Lake Tenaya in Yosemite NP.jpg',short='Tenaya Lake',cls='tri',
   caption='Tenaya Lake. The trailhead is at its western end.'),
 ridge=dict(file='File:Clouds Rest with Half Dome in the background.jpg',short='The ridge',cls='tri',
   caption='The crest of the summit ridge, with Half Dome beyond. Snow patches like these mean a slippery crossing.'),
 back=dict(file='File:Tenaya Lake From Clouds Rest.JPG',short='Looking back',cls='tri',crop=(0,0.06,1,0.62),
   caption='Looking back north-east along the ridge towards Tenaya Lake and the high country.'),
 face=dict(file='File:Clouds rest in Yosemite.jpg',short='North-west face',cls='duo',crop=(0,0.12,1,0.92),
   caption='Clouds Rest from across Tenaya Canyon: a single slope of granite from the summit ridge to the canyon floor.'),
)
