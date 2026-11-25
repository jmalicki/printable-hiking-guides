"""Sierra Buttes fire lookout (Tahoe National Forest) from the Packer Saddle trailhead, out and back; the long way from Sardine Lake as the variant."""
PDF='sierra-buttes-fire-lookout.pdf'
PARK='Tahoe National Forest'            # shown after the title in the hike lists
OSM_BBOX=(39.570,-120.700,39.640,-120.595)
TILES=dict(z=15,bbox=(39.584,-120.684,39.630,-120.610))
JUNCTIONS=dict(th=91937354,                    # trailhead: green gate on Forest Road 93-2, below Packer Saddle
               pct=91938753,                   # Pacific Crest Trail crosses
               view=(39.59838,-120.66013),     # spur to the cliff edge above Young America Lake
               road=1889273510,                # trail joins the old jeep road to the lookout
               top=(39.59360,-120.64718),      # the lookout
               sard=6938190648,                # Tamarack Connection leaves Sardine Lake Road, by Sand Pond
               tam=6938190453,                 # Tamarack Lakes
               tj=91938971)                    # Tamarack Connection meets the ridge tracks
OUT_=['th','pct','view','road','top']
ROUTES={'main':OUT_+OUT_[-2::-1],'sardine':['sard','tam','tj','pct']}
MAIN='main'
GPX={'main':'Sierra Buttes fire lookout from the Packer Saddle trailhead, out and back','sardine':'Sardine Lake to the Sierra Buttes Lookout Trail by the Tamarack Connection (one way, joins the main route at the Pacific Crest Trail)'}
MK=[('th',1),('pct',2),('view',3),('road',4),('top',5)]
MAP=dict(bbox=(39.5880,-120.6800,39.6265,-120.6150),icons=[],k=1.4,scale=(1000,'1 km'),
  overlays=[dict(route='sardine',color='BLUE',width=10,dash='18 10')],
  markers=MK+[('sard','A'),('tj','B')],
  arrow_start=500,arrow_step=800,arrow_end=3500,arrow_clear=200,
  labels=[dict(at='th',dx=-28,dy=-10,text='Trailhead',anchor='end',size=24,weight=700),
          dict(at='th',dx=-28,dy=16,text='Packer Saddle',anchor='end',size=21),
          dict(at='pct',dx=-28,dy=8,text='Pacific Crest Trail',anchor='end',size=22),
          dict(at='view',dx=28,dy=8,text='overlook',size=22),
          dict(at='road',dx=-28,dy=10,text='jeep road',anchor='end',size=22),
          dict(at='top',dx=28,dy=2,text='Lookout',size=25,weight=700),
          dict(at='top',dx=28,dy=28,text='{{u:2,617 m|8,587 ft}}',size=22),
          dict(at='sard',dx=-28,dy=-12,text='Sardine Lake Road',anchor='end',size=22,color='BLUE',weight=700),
          dict(at='tj',dx=0,dy=-30,text='Tamarack Lakes',anchor='middle',size=22,color='BLUE',weight=700),
          dict(at=(39.6165,-120.6243),dx=-20,dy=34,text='Sardine Lake Resort',anchor='end',size=22,weight=700)])
PROFILE=dict(emin=2050,emax=2700,grid=100,label_every=200,height=260,km_step=1,
  markers=[('th',1,0),('pct',2,0),('view',3,0),('road',4,0),('top',5,0),('road_end',4,0),('view_end',3,0),('pct_end',2,0),('th_end',1,0)],
  notes=[(800,2085,'ridge, +125 m'),(2450,2085,'steepest: +180 m'),(3680,2085,'stairs'),(5900,2085,'down the same way')])
SV_=(39.58960,-120.36740)     # Sierraville, Highway 89 / 49
TH_=(39.61163,-120.66550)
ACCESS=dict(**{'from':SV_,'to':TH_},z=13,bbox=(39.50,-120.87,39.69,-120.33),pad=(1150,160,620,560),k=1.6,mk=0.7,scale=(5000,'5 km'),
  extra=[{'from':(39.55940,-120.82800),'to':(39.61780,-120.59100),'color':'INK'}],    # Downieville -> Bassetts, the Highway 49 approach from the west
  markers=[dict(letter='A',at=('at',SV_),label='Sierraville',dx=-10,dy=-52,anchor='end',size=34,weight=700),
           dict(letter='B',at=('name','Gold Lake Highway'),label='Bassetts',dx=38,dy=34,size=32),
           dict(letter='C',at=('name','Packer Lake Road'),label='fork',dx=10,dy=-44,size=30),
           dict(letter='D',at=('name','Gold Valley Road'),label='Packer Lake',dx=-20,dy=-46,anchor='end',size=30),
           dict(letter='P',at=('end',),label='Trailhead',dx=-40,dy=10,anchor='end',size=34,weight=700,fill='RED'),
           dict(letter='S',at=('at',(39.56600,-120.63400)),label='Sierra City',dx=0,dy=62,anchor='middle',size=32,weight=700),
           dict(letter='V',at=('at',(39.55940,-120.82800)),label='Downieville',dx=0,dy=62,anchor='middle',size=32,weight=700)],
  places=[dict(at=(39.6168,-120.6240),label='Sardine Lake',dx=16,dy=36,size=28),
          dict(at=(39.5936,-120.6471),label='Sierra Buttes',dx=20,dy=14,size=28)])
PHOTOS=dict(
 hero=dict(file='File:A hiker descends the stairs used to access the Sierra Buttes fire lookout, Sept 28, 2024, on the Tahoe National Forest (20240928-FS-PRW-001).jpg',short='The stairs',cls='cover',
   caption='The first flight of stairs, September 2024.'),
 top=dict(file='File:Hike to the top of the Sierra Buttes.jpg',short='Lookout from below',cls='tri',
   caption='From the saddle below: the stairs slant up the left of the rock to the lookout.'),
 stairs=dict(file='File:Stairs to the top of Sierra Buttes.jpg',short='Looking down',cls='tri',
   caption='Looking back down from the top landing, in cloud and old snow.'),
 lookout=dict(file='File:Sierra Buttes Fire Lookout.jpg',short='The summit crag',cls='tri',
   caption='The lookout on its crag, seen from far below. The cabin is the small square on the highest point.'),
 sardine=dict(file='File:Upper Sardine Lake and the Sierra Buttes, California.jpg',short='Sardine Lake',cls='tall',
   caption='The Sierra Buttes from Upper Sardine Lake: the north-east face you were standing on top of.'),
 town=dict(file='File:Buckhorn, Sierra City, California LCCN2013633862.tif',short='Sierra City',cls='mid',caption='Main Street, Sierra City, on Highway 49.'),
)
