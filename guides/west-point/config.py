"""The balcony of Mount Tam: Rock Spring -> Mountain Theater -> Rock Spring Trail -> West Point Inn -> Nora -> Matt Davis -> Bootjack."""
PDF='mount-tam-west-point-loop.pdf'
OSM_BBOX=(37.895,-122.640,37.932,-122.570)
TILES=dict(z=16,bbox=(37.9020,-122.6290,37.9220,-122.5770))
JUNCTIONS=dict(start=(37.9107739,-122.6126301),theater=351899944,wpi=110379911,nora_top=312919663,
               nora_md=1331416933,md_bj=12823903319,bj_top=1825691355)
ROUTES={'main':['start','theater','wpi','nora_top','nora_md','md_bj','bj_top','start']}
LEG_ALLOW={('theater','wpi'):{'Rock Spring Trail'},('nora_top','nora_md'):{'Nora Trail'},
           ('nora_md','md_bj'):{'Matt Davis Trail'}}
GPX={'main':'Mount Tam: Rock Spring - West Point Inn - Matt Davis - Bootjack loop'}
MAIN='main'
MAP=dict(pad=215,aspect=180/118,extent=['main'],overlays=[],
  markers=[('start',1),('theater',2),('wpi',3),('nora_md',4),('md_bj',5)],
  labels=[dict(at='start',dx=-28,dy=-12,text='START / FINISH',anchor='end',size=22,weight=700),
          dict(at='start',dx=-28,dy=14,text='Rock Spring',anchor='end',size=20,weight=500),
          dict(at='theater',dx=6,dy=-30,text='Mountain Theater',size=20,weight=500),
          dict(at='wpi',dx=-30,dy=8,text='West Point Inn',anchor='end',size=22,weight=700),
          dict(at='nora_md',dx=30,dy=8,text='Matt Davis Trail',size=20,weight=500),
          dict(at='md_bj',dx=-6,dy=52,text='Bootjack',anchor='middle',size=20,weight=500)],
  icons=[])
PROFILE=dict(emin=300,emax=700,grid=50,label_every=100,height=270,
  markers=[('start',1,0),('theater',2,0),('wpi',3,0),('nora_md',4,0),('md_bj',5,0),('bj_top',2,0),('start_end',1,0)],
  notes=[(1700,480,'Rock Spring Trail: a gentle 70 m down, views all the way'),(4800,560,'Matt Davis: rolling, in and out of ravines'),(5400,335,'Bootjack climb: 170 m up in 1.2 km &#8594;')])
ACCESS=dict(**{'from':(37.8078,-122.4750),'to':(37.9107739,-122.6126301)},z=14,bbox=(37.795,-122.640,37.928,-122.455),
  pad=(280,230,150,110),
  markers=[dict(letter='A',at=('m',1700),label='Golden Gate Bridge',dx=-50,dy=13,anchor='end'),
           dict(letter='B',at=('type','off ramp'),label='Exit Hwy 1',dx=50,dy=13),
           dict(letter='C',at=('name','Shoreline Highway'),label='Tam Junction',dx=10,dy=82,anchor='middle'),
           dict(letter='D',at=('name','Panoramic Highway'),label='Panoramic Hwy',dx=-10,dy=82,anchor='middle'),
           dict(letter='E',at=('after','Panoramic Highway',1600),label='Four-way junction',dx=50,dy=40),
           dict(letter='F',at=('name','Pantoll Road'),label='Pantoll',dx=-50,dy=40,anchor='end'),
           dict(letter='P',at=('end',),label='Rock Spring',dx=0,dy=-52,anchor='middle',size=40,weight=700,fill='RED')],
  places=[dict(at=(37.9060,-122.5475),label='Mill Valley',dx=26,dy=13),
          dict(at=(37.91004,-122.57675),label='Mountain Home Inn',dx=20,dy=-22,size=32),
          dict(at=(37.8030,-122.4790),label='San Francisco',anchor='end',size=40,weight=700,dot=False)])
PHOTOS=dict(
 view=dict(short='View',cls='hero',file='File:Mt. Tamalpais, view south to San Francisco and the bay. West Point Inn is below on the right. The valley between the Inn and the Panoramic Highway holds Muir Woods. - panoramio.jpg',crop=(0,0.16,1,0.93),
   caption='The south face of Mount Tam: Richardson Bay, the Marin Headlands and San Francisco beyond. The West Point Inn is the roof in the trees, lower right; the wooded valley beyond it hides Muir Woods.'),
 theater=dict(short='Theater',cls='strip',file='File:Cushing Memorial Amphitheater pano.jpg',caption='The Mountain Theater: 1930s stone seating for nearly 4,000, with the bay as backdrop.'),
 inn=dict(short='Inn',cls='mid',file='File:West Point Inn, Mt. Tamalpais State Park, Mill Valley, CA 5-11-2013 4-58-49 PM.JPG',crop=(0,0.08,1,0.92),caption='West Point Inn, 1904. No road for the public, no mains electricity; a porch, picnic tables and the view.'),
 chaparral=dict(short='Chaparral',cls='bio',file="File:View of Mt. Tamalpais' East Peak. The Old Railroad Grade fire road is visible below Ridgecrest Blvd - Bolinas Ridge Road. - panoramio.jpg",caption='Chaparral: grey-green scrub on the sun-facing slopes below East Peak.'),
 woodland=dict(short='Woodland',cls='bio',file='File:Matt Davis trail. Scrub forest provides a low canopy above the upper reaches of the trail near the Pantoll Ranger Station. - panoramio.jpg',caption='Oak and bay woodland arching over the Matt Davis Trail.'),
 cypress=dict(short='Cypress',cls='bio',file='File:Cupressus sargentii Mount Tamalpais.jpg',caption='Sargent cypress on Mount Tam: a tree that thrives on toxic serpentine soil.'),
 fog=dict(short='Fog',cls='bio',file='File:Fog over Mill Valley near Mt. Tamalpais.jpg',crop=(0,0.18,1,0.68),caption='The summer fog bank below the mountain: the redwoods&#8217; water supply.'),
)
