"""The balcony of Mount Tam: Rock Spring -> Mountain Theater -> Rock Spring Trail -> West Point Inn -> Nora -> Matt Davis -> Bootjack."""
PDF='mount-tam-west-point-loop.pdf'
PARK='Mount Tamalpais State Park'            # shown after the title in the hike lists
REGION='bay-area'            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
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
# Photos: Wikimedia Commons (file='File:...') or a direct URL with explicit credit. crop=(l,t,r,b) fractions.
PHOTOS=dict(
 view=dict(short='Skyline',cls='hero',file='File:San Francisco and Sausalito from Mount Tam, February 2026.JPG',crop=(0,0.10,1,0.80),
   caption='San Francisco from the south face of Mount Tam on a clear winter day (telephoto): Sausalito in the foreground, the bay, and the downtown towers 20 km away.'),
 theater=dict(short='Theater',cls='strip',file='File:Cushing Memorial Amphitheater pano.jpg',caption='The Mountain Theater: 1930s stone seating for nearly 4,000, with the bay as backdrop.'),
 inn=dict(short='Inn',cls='inn',url='https://live.staticflickr.com/65535/53212106778_122b21c7d6_b.jpg',artist='lamblukas (Flickr)',license='CC BY 2.0',page='https://www.flickr.com/photos/dnevill/53212106778/',
   caption='West Point Inn, built in 1904 for railway passengers.'),
 porch=dict(short='Porch',cls='inn',url='https://live.staticflickr.com/131/351406411_34e5e31e35_b.jpg',artist='sparkle glowplug (Flickr)',license='CC BY-NC 2.0',page='https://www.flickr.com/photos/sparkleglowplug/351406411/',
   caption='What you came for: the inn&#8217;s porch, looking over Richardson Bay to the East Bay hills.'),
 fog=dict(short='Fog',cls='fogpic',file='File:Fog over Mill Valley near Mt. Tamalpais.jpg',crop=(0,0.18,1,0.68),caption='Summer fog pouring in below the mountain.'),
 grass=dict(short='Grassland',cls='bio',file='File:Tree on MT Tam - Flickr - Andrew V Kearns.jpg',caption='Wind-shaped tree, summer-gold grass, fog below.'),
 serpentine=dict(short='Serpentine',cls='bio',file='File:Arctostaphylos montana.jpg',caption='Serpentine rock and the manzanita found only here.'),
 chaparral=dict(short='Chaparral',cls='bio',url='https://live.staticflickr.com/5157/29936612395_facd884832_b.jpg',artist='vrkrebs (Flickr)',license='CC BY-NC-ND 2.0',page='https://www.flickr.com/photos/raykrebs/29936612395/',
   caption='Chaparral near West Point Inn.'),
 woodland=dict(short='Madrone',cls='bio',file='File:Arbutus menziesii Mount Tam Blithedale Ridge Road 4.jpg',caption='Madrone: orange limbs, peeling bark.'),
 redwood=dict(short='Redwoods',cls='bio',file='File:Biking on Mount Tamalpais.JPG',caption='Slim upland redwoods in a damp gully.'),
)
