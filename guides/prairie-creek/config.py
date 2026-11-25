"""Prairie Creek Redwoods: visitor centre, James Irvine Trail, Fern Canyon, Gold Bluffs Beach, Miners Ridge."""
PDF='prairie-creek-fern-canyon-loop.pdf'
PARK='Prairie Creek Redwoods State Park'            # shown after the title in the hike lists
OSM_BBOX=(41.350,-124.090,41.412,-124.010)
TILES=dict(z=15,bbox=(41.352,-124.085,41.410,-124.012))
JUNCTIONS=dict(start=(41.36401,-124.02317),         # Prairie Creek visitor centre
               nature=4237068888,                # James Irvine Trail leaves the Nature Trail
               split=2946174544,                 # James Irvine / Miner's Ridge fork
               clin=4237068222,                  # James Irvine / Clintonia junction
               friend=2912195470,                # Friendship Ridge Trail joins
               top=4237068853,                   # head of Fern Canyon: the loop trail drops into the canyon
               mouth=4237028500,                 # mouth of Fern Canyon
               jiend=1795255408,                 # foot of the James Irvine Trail steps, beside the canyon mouth
               mrbeach=84962149,                 # Miner's Ridge Trail leaves Davison Road by the beach campground
               mrclin=2946175261)                # Miner's Ridge / Clintonia junction
ROUTES={'main':['start','nature','split','clin','friend','top','mouth','mrbeach','mrclin','split','nature','start'],
        # return by the Clintonia Trail: the way round while Miner's Ridge is blocked west of the Clintonia junction (2026)
        'alt':['start','nature','split','clin','friend','top','jiend','top','friend','clin','mrclin','split','nature','start']}
LEG_ALLOW={('top','mouth'):{'Fern Canyon Loop Trail'}}       # down the canyon floor, not along the rim
MAIN='main';GPX={'main':'Prairie Creek: James Irvine Trail, Fern Canyon, Gold Bluffs Beach, Miners Ridge','alt':'Prairie Creek: James Irvine Trail to Fern Canyon, back by the Clintonia Trail'}
MK=[('start',1),('split',2),('clin',3),('top',4),('mouth',5),('mrbeach',6),('mrclin',7)]
MAP=dict(pad=120,aspect=1.22,extent=['main'],icons=[],k=1.15,scale=(1000,'1 km'),
  overlays=[dict(route='alt',frm='clin_end',to='mrclin',color='BLUE',width=7,dash='14 9')],
  markers=MK,arrow_start=500,arrow_step=1100,arrow_clear=300,
  labels=[dict(at='start',dx=24,dy=-4,text='START / FINISH',size=21,weight=700),
          dict(at='start',dx=24,dy=18,text='visitor centre',size=18),
          dict(at=(41.3610,-124.0300),dx=0,dy=0,text='Elk Prairie',anchor='middle',size=19,color='#7a5c00',weight=700),
          dict(at='clin',dx=24,dy=-6,text='Clintonia Trail',size=18,color='BLUE',weight=700),
          dict(at='top',dx=10,dy=-34,text='Fern Canyon',anchor='middle',size=21,weight=700),
          dict(at='mouth',dx=-26,dy=-4,text='canyon mouth,',anchor='end',size=18),
          dict(at='mouth',dx=-26,dy=17,text='car park',anchor='end',size=18),
          dict(at=(41.3945,-124.0715),dx=0,dy=0,text='Gold Bluffs Beach',anchor='middle',size=19,color='#7a5c00',weight=700),
          dict(at='mrbeach',dx=-24,dy=6,text='campground',anchor='end',size=18),
          dict(at=(41.3745,-124.0420),dx=0,dy=0,text='Miners Ridge Trail',anchor='middle',size=18),
          dict(at=(41.3840,-124.0330),dx=0,dy=0,text='James Irvine Trail',anchor='middle',size=18)])
PROFILE=dict(emin=0,emax=220,grid=20,label_every=40,height=290,km_step=2,
  markers=[('start',1,8),('split',2,0),('clin',3,0),('top',4,-10),('mouth',5,8),('mrbeach',6,0),('mrclin',7,0),('split_end',2,0),('start_end',1,-8)],
  notes=[(3300,40,'James Irvine Trail: old-growth redwoods'),(9450,75,'beach'),(13000,40,'Miners Ridge')])
ACCESS=dict(**{'from':(41.2868,-124.0597),'to':(41.3638,-124.0228)},z=13,bbox=(41.26,-124.12,41.39,-123.96),pad=(420,420,120,170),k=1.3,mk=0.8,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',100),label='Orick',dx=40,dy=12,size=30),
           dict(letter='B',at=('at',(41.321246,-124.039187)),label='Davison Road',dx=-40,dy=12,anchor='end',size=30),
           dict(letter='C',at=('name','Newton B Drury Scenic Parkway'),label='Exit 753',dx=40,dy=12,size=30),
           dict(letter='P',at=('end',),label='Visitor centre',dx=40,dy=-8,size=32,weight=700,fill='RED')],
  places=[dict(at=(41.3610,-124.0300),label='Elk Prairie',dot=False,dx=-40,dy=40,anchor='end',size=26,weight=500)])
# Photos: Wikimedia Commons. The elk_beach credit in data/prairie-creek/photos.json is shortened by hand to 'U.S. Fish and Wildlife Service'
# (Commons gives a four-part archive string); re-shorten it if the photo is ever refetched.
PHOTOS=dict(
 hero=dict(short='Cover',cls='cover',file='File:Fern Canyon pano 1.jpg',caption='Fern Canyon: walls of five-finger fern on both sides, and the creek for a path.'),
 redwoods=dict(short='Redwoods',cls='mid',file='File:Prairie Creek State Park - James Irvine Trail, Cathedral Tree ^ an architect - Flickr - rachel thecat.jpg',caption='Old-growth redwoods beside the James Irvine Trail.'),
 elk_beach=dict(short='Elk in the dunes',cls='bio',file='File:Roosevelt elk at Gold Bluffs Beach - DPLA - eeff2f54972aefd741f1d0d2e35c1058.jpg',crop=(0,0.42,1,0.92),caption='A bull in the dune grass at Gold Bluffs Beach.'),
 elk_bull=dict(short='Bull elk',cls='bio',file='File:Elk near Gold Bluffs in the Redwoods National Park (2820215343).jpg',caption='A bull grazing near Gold Bluffs, late August.'),
 slug=dict(short='Banana slug',cls='bio',file='File:Ariolimax (23211297933).jpg',caption='Banana slug. Not taken in the park.'),
 frog=dict(short='Frog',cls='bio',file='File:Rana aurora Fern Canyon.jpg',caption='Northern red-legged frog in Fern Canyon.'),
 canyon2=dict(short='Fern wall',cls='bio',file='File:Fern canyon.jpg',caption='The canyon wall.'),
 ridge=dict(short='Miners Ridge',cls='bio',file='File:Redwood NSP Miners Ridge Trail 1.jpg',crop=(0,0.25,1,0.75),caption='Redwoods on the Miners Ridge Trail.'),
 trinidad=dict(short='Trinidad',cls='strip',file='File:Panorama from Trinidad Head, October 2023.jpg',caption='Trinidad and its beach from Trinidad Head.'),
)
