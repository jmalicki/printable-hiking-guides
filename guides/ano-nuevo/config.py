"""Ano Nuevo State Park: the walk out to the elephant seals at Ano Nuevo Point."""
PDF='ano-nuevo-elephant-seals.pdf'
PARK='Año Nuevo State Park'            # shown after the title in the hike lists
REGION='bay-area'
OSM_BBOX=(37.095,-122.368,37.160,-122.280)
JUNCTIONS=dict(start=401411834,                 # car park: the Ano Nuevo Point Trail starts beside the Marine Education Center
               vc=401414419,                    # path from the barns joins the trail
               nyc=621816309,                   # New Years Creek Trail leaves on the left
               pond=401414426,                  # the pond dam; Cove Beach Trail drops left
               gate=401415279,                  # staging area: boundary of the Natural Preserve
               bend=401415340,                  # where the trail turns north-west across the dune field
               sj=2923682958,                   # side path to South Point
               south=2923682996,                # South Point viewing area
               s2=2923684630,
               s2end=2923682990,                # side path rejoins the main trail
               bight=5805534173,                # Bight Beach viewing area (benches, boardwalk)
               north=2923684617,                # North Point viewing area, end of the trail
               nys=621816313,                   # New Years Creek Trail meets the Steele Trail
               steele=621816338)                # Steele Trail reaches the barns
ROUTES={'main':['start','vc','nyc','pond','gate','bend','sj','south','s2','s2end','bight','north','bend','gate','pond','nyc','nys','steele','start']}
MAIN='main';GPX={'main':'Ano Nuevo Point: the elephant seal viewing areas'}
LEG_ALLOW={('nyc','nys'):{'New Years Creek Trail'},('nys','steele'):{'Steele Trail'}}
TILES=dict(z=16,bbox=(37.106,-122.344,37.127,-122.300))
MK=[('start',1),('pond',2),('gate',3),('south',4),('bight',5),('north',6)]
MAP=dict(bbox=(37.1068,-122.3400,37.1245,-122.3008),icons=[],k=1.0,scale=(500,'500 m'),overlays=[],
  markers=MK,arrow_start=260,arrow_step=560,arrow_clear=130,
  labels=[dict(at='start',dx=28,dy=-8,text='START / FINISH',size=23,weight=700),
          dict(at='start',dx=28,dy=16,text='car park and barns',size=20),
          dict(at='pond',dx=0,dy=-30,text='pond',anchor='middle',size=21,weight=700),
          dict(at='gate',dx=26,dy=34,text='staging area',size=21,weight=700),
          dict(at='gate',dx=26,dy=57,text='permit or guide beyond here',size=19,color='RED',weight=700),
          dict(at='south',dx=-26,dy=30,text='South Point',anchor='end',size=22,weight=700),
          dict(at='bight',dx=-30,dy=10,text='Bight Beach',anchor='end',size=22,weight=700),
          dict(at='north',dx=0,dy=-32,text='North Point',anchor='middle',size=22,weight=700),
          dict(at=(37.1162,-122.3105),dx=0,dy=0,text='Cove Beach',anchor='middle',size=21,color='#0b5f8a',weight=700),
          dict(at=(37.1093,-122.3368),dx=0,dy=0,text='Año Nuevo Island',anchor='middle',size=21,weight=700),
          dict(at=(37.1093,-122.3368),dx=0,dy=22,text='closed: sea lions, seals, seabirds',anchor='middle',size=18),
          dict(at='nys',dx=18,dy=30,text='return: New Years Creek Trail',size=18),
          dict(at=(37.1140,-122.3030),dx=0,dy=0,text='Highway 1',anchor='middle',size=19)])
PROFILE=dict(emin=0,emax=40,grid=10,label_every=20,height=170,km_step=1,
  markers=[('start',1,10),('pond',2,0),('gate',3,0),('south',4,-8),('bight',5,6),('north',6,0),('gate_end',3,0),('pond_end',2,0),('start_end',1,-10)],
  notes=[])
ACCESS=dict(**{'from':(37.4633,-122.4290),'to':(37.1201,-122.3073)},z=13,bbox=(37.08,-122.60,37.50,-122.06),pad=(760,1250,110,150),k=2.6,mk=1.4,scale=(5000,'5 km'),
  markers=[dict(letter='A',at=('m',200),label='Half Moon Bay',dx=62,dy=18,size=58),
           dict(letter='B',at=('m',23700),label='Pescadero turn',dx=-62,dy=18,anchor='end',size=58),
           dict(letter='C',at=('m',33400),label='Pigeon Point',dx=-62,dy=18,anchor='end',size=58),
           dict(letter='F',at=('m',38300),label='Franklin Point',dx=-62,dy=18,anchor='end',size=58),
           dict(letter='P',at=('end',),label='Año Nuevo',dx=62,dy=18,size=62,weight=700,fill='RED')],
  places=[dict(at=(37.2552,-122.3830),label='Pescadero',dx=34,dy=16,size=52),dict(at=(37.3180,-122.2740),label='La Honda',dx=34,dy=16,size=50)])
# Photos: Wikimedia Commons. Captions say so where a photo was taken somewhere other than Ano Nuevo.
D='File:Año Nuevo State Park, Pacific Coast, California, USA'
PHOTOS=dict(
 hero=dict(short='Cover',cls='hero',file='File:Elephant seals at Ano Nuevo (91629).jpg',crop=(0,0.16,1,0.84),caption='Elephant seals on the beach at Año Nuevo Point in February.'),
 trail=dict(short='Trail',cls='strip',file=D+'.jpg',crop=(0,0.22,1,0.86),caption='The Año Nuevo Point Trail between the barns and the pond.'),
 size=dict(short='Bull and pups',cls='bio',file='File:Elephant seals at Ano Nuevo (91577).jpg',caption='A bull with two pups, February.'),
 fight=dict(short='Bulls fighting',cls='bio',file='File:Northern elephant seal bulls fighting.jpg',caption='Bulls fighting (Piedras Blancas, down the coast).'),
 harem=dict(short='Harem',cls='bio',file='File:Elephant seals at Ano Nuevo (91674).jpg',caption='A harem on the sand, February.'),
 weaners=dict(short='Weaners',cls='bio',file='File:Elephant seals at Ano Nuevo (91604).jpg',caption='Weaned pups in a heap.'),
 moult=dict(short='Moult',cls='bio',file='File:Juvenile elephant seal during molt.jpg',caption='A juvenile moulting, late May.'),
 nose=dict(short='Bull',cls='bio',file='File:Elephant seals at Ano Nuevo (91615).jpg',caption='A bull asleep on his nose.'),
 dunes=dict(short='Dunes in May',cls='bio',file=D+' - 52476761077.jpg',caption='Seals in the dunes, May.'),
 island=dict(short='Island',cls='bio',file='File:Ano Nuevo Island.jpg',caption='The keeper&#8217;s house on the island.'),
 seal=dict(short='Harbour seals',cls='bio',file='File:Harbor seal is nurcing at Point Lobos.jpg',caption='Harbour seal and pup (Point Lobos).'),
 pelican=dict(short='Pelicans',cls='bio',file='File:Pelican 2 (15559241536).jpg',caption='Brown pelican (photographed elsewhere).'),
 harrier=dict(short='Harrier',cls='bio',file='File:Northern harrier in flight-1930.jpg',caption='Female northern harrier (Sacramento Valley).'),
 bobcat=dict(short='Bobcat',cls='bio',file='File:Bobcat (33390975031).jpg',caption='Bobcat (Point Reyes).'),
 snake=dict(short='Garter snake',cls='bio',file='File:Thamnophis sirtalis tetrataenia (2005 10 16) - uitsnede.jpg',caption='San Francisco garter snake (in a zoo).'),
 coast=dict(short='Coast',cls='bio',file='File:Coastline in Año Nuevo State Park.jpg',caption='The coast north of the point.'),
)
