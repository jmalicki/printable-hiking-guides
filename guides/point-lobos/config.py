"""Point Lobos: the shore loop from the entrance station."""
PDF='point-lobos-shore-loop.pdf'
PARK='Point Lobos State Natural Reserve'            # shown after the title in the hike lists
OSM_BBOX=(36.500,-121.962,36.530,-121.925)
JUNCTIONS=dict(start=289682286,                 # entrance station: Carmelo Meadow, Lace Lichen and South Plateau trails meet
               whalers=289682724,               # Carmelo Meadow Trail meets the Granite Point Trail above Whalers Cove
               granite=(36.5229,-121.9370,['Granite Point Trail']),
               cabin=2845565128,                # Whalers Cabin
               cannery=1657741478,              # Whalers Cove car park: North Shore Trail starts
               info=2536491660,                 # west end of the North Shore Trail, Sea Lion Point car park
               grove=289684707,                 # Cypress Grove Trail: the loop starts
               pinnacle=289682933,              # north tip of the Cypress Grove loop
               west=(36.5210,-121.9525,['Cypress Grove Trail']),
               slp=289681480,                   # Sea Lion Point Trail starts
               sealion=8379729852,              # Sea Lion Point
               sandhill=289682213,              # Sand Hill Trail meets the South Shore Trail
               weston=1702616894,                # South Shore Trail above Weston Beach
               bird=89766631,                   # Bird Island car park
               pelican=(36.50739,-121.94195),   # Bird Island overlook
               plateau=289682440)               # South Plateau Trail leaves the Bird Island Trail above Gibson Beach
ROUTES={'main':['start','whalers','granite','cabin','cannery','info','grove','pinnacle','west','grove','slp','sealion','sandhill','weston','bird','pelican','plateau','start'],
        'short':['start','whalers','granite','cabin','cannery','info','grove','pinnacle','west','grove','slp','sealion','sandhill','slp','start']}
MAIN='main';GPX={'main':'Point Lobos shore loop','short':'Point Lobos north shore loop'}
LEG_ALLOW={('cannery','info'):{'North Shore Trail'},('sandhill','weston'):{'South Shore Trail'},('weston','bird'):{'South Shore Trail'},('slp','start'):{'Lace Lichen Trail','South Plateau Trail','(footway)'}}
TILES=dict(z=16,bbox=(36.502,-121.964,36.528,-121.926))
MK=[('start',1),('whalers',2),('granite',3),('cannery',4),('info',5),('pinnacle',6),('sealion',7),('weston',8),('bird',9),('plateau',10)]
MAP=dict(pad=110,aspect=1.3,extent=['main'],icons=[],k=0.8,scale=(500,'500 m'),
  overlays=[dict(route='short',frm='slp_end',to='start_end',color='BLUE',width=5,dash='10 7')],
  markers=MK,arrow_start=250,arrow_step=420,arrow_clear=110,
  labels=[dict(at='start',dx=26,dy=6,text='START / FINISH',size=26,weight=700),
          dict(at='start',dx=26,dy=28,text='entrance station',size=22),
          dict(at='granite',dx=24,dy=-14,text='Granite Point',size=23,weight=700),
          dict(at='cabin',dx=-8,dy=34,text='Whalers Cabin',anchor='middle',size=22),
          dict(at='info',dx=26,dy=24,text='Information Station',size=22),
          dict(at='pinnacle',dx=-26,dy=-22,text='Cypress Grove',anchor='end',size=23,weight=700),
          dict(at='sealion',dx=-26,dy=-10,text='Sea Lion Point',anchor='end',size=23,weight=700),
          dict(at='pelican',dx=-10,dy=40,text='Pelican Point',anchor='end',size=22),
          dict(at='plateau',dx=26,dy=6,text='South Plateau Trail',size=22),
          dict(at=(36.5178,-121.9425),dx=0,dy=0,text='Lace Lichen short cut',anchor='middle',size=20,color='BLUE',weight=700),
          # coves and points where the sources place otters: blue italics would need a class, so plain bold blue
          dict(at=(36.5203,-121.9388),dx=0,dy=0,text='Whalers Cove',anchor='middle',size=23,color='#0b5f8a',weight=700),
          dict(at=(36.5224,-121.9440),dx=0,dy=0,text='Bluefish Cove',anchor='middle',size=23,color='#0b5f8a',weight=700),
          dict(at=(36.5228,-121.9497),dx=0,dy=0,text='Cypress Cove',anchor='middle',size=23,color='#0b5f8a',weight=700),
          dict(at=(36.5199,-121.9548),dx=0,dy=0,text='Headland Cove',anchor='middle',size=23,color='#0b5f8a',weight=700),
          dict(at=(36.5160,-121.9520),dx=0,dy=0,text='Sand Hill Cove',anchor='middle',size=23,color='#0b5f8a',weight=700),
          dict(at=(36.5113,-121.9462),dx=0,dy=0,text='Weston Beach',anchor='middle',size=23,color='#0b5f8a',weight=700),
          dict(at=(36.5086,-121.9438),dx=0,dy=0,text='China Cove',anchor='end',size=23,color='#0b5f8a',weight=700)])
PROFILE=dict(emin=0,emax=50,grid=10,label_every=20,height=170,km_step=1,
  markers=[('start',1,10),('whalers',2,0),('granite',3,0),('cannery',4,0),('info',5,0),('pinnacle',6,0),('sealion',7,0),('weston',8,0),('bird',9,0),('plateau',10,0),('start_end',1,-10)],
  notes=[])
ACCESS=dict(**{'from':(36.577541,-121.908671),'to':(36.51602,-121.93669)},z=14,bbox=(36.500,-121.975,36.592,-121.870),pad=(330,330,110,260),k=1.8,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',150),label='From Monterey',dx=52,dy=14),
           dict(letter='B',at=('m',3300),label='Rio Road',dx=52,dy=14),
           dict(letter='P',at=('end',),label='Point Lobos',dx=52,dy=14,size=40,weight=700,fill='RED')],
  places=[dict(at=(36.5552,-121.9233),label='Carmel-by-the-Sea',dx=-30,dy=12,anchor='end',size=32),
          dict(at=(36.5041,-121.9316),label='Carmel Highlands',dx=30,dy=12,size=30)])
# Photos: Wikimedia Commons. Most otter photos were taken elsewhere on this coast; captions say where.
PHOTOS=dict(
 hero=dict(short='Cover',cls='hero',file='File:China Cove, Point Lobos State Park.jpg',crop=(0,0.12,1,0.86),caption='China Cove, on the south shore of the reserve, from the Bird Island Trail.'),
 whalers=dict(short='Whalers Cove',cls='strip',file="File:Whaler's Cove, Point Lobos, CA, US - May 2013.jpg",caption='Whalers Cove from the Granite Point Trail.'),
 o_pup=dict(short='Otter and pup',cls='bio',file='File:Sea otter nursing young.jpg',caption='Mother and pup (Morro Bay).'),
 o_food=dict(short='Otter feeding',cls='bio',file='File:Sea Otter (37795893195).jpg',caption='Opening a clam.'),
 o_fur=dict(short='Otter grooming',cls='bio',file='File:Sea otter animal in waer enhydra lutris.jpg',caption='Grooming.'),
 o_raft=dict(short='Otter in kelp',cls='bio',file='File:497501486 dc0ca684d8 o.jpg',caption='Wrapped in kelp (Morro Bay).'),
 o_back=dict(short='Otters at Point Lobos',cls='bio',file='File:Fauna Point Lobos 04.JPG',caption='What you are looking for: two otters in the kelp at Point Lobos.'),
 o_bixby=dict(short='Raft',cls='bio',file='File:Sea otters at moss landing 2.jpg',caption='A raft at Moss Landing, on Monterey Bay.'),
 seal=dict(short='Harbor seals',cls='bio',file='File:Harbor seal is nurcing at Point Lobos.jpg',caption='Mother and pup at Point Lobos.'),
 sealion=dict(short='Sea lion',cls='bio',file='File:California Sea Lion (Zalophus californianus) 02.jpg',caption='California sea lion at Point Lobos.'),
 cormorant=dict(short='Cormorants',cls='bio',file="File:Phalacrocorax penicillatus (Brandt's Cormorant) colony, Point Lobos - Diliff.jpg",caption='Brandt&#8217;s cormorants at Point Lobos.'),
 oyster=dict(short='Oystercatcher',cls='bio',file='File:Black Oystercatcher Pt Lobos State Natural Reserve Monterey CA 2017-04-11 13-30-04 (33481810144).jpg',caption='Black oystercatchers at Point Lobos.'),
 whale=dict(short='Grey whale',cls='bio',file='File:Eschrichtius robustus 01.jpg',caption='Grey whale breaching.'),
 carmelo=dict(short='Carmelo Formation',cls='bio',file='File:Carmelo Formation at Point Lobos.jpg',caption='Carmelo Formation at Point Lobos.'),
 cypress=dict(short='Cypress',cls='bio',file='File:Trentepohlia aurea at Pt Lobos.jpg',caption='The orange alga on cypress branches.'),
)
