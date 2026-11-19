"""Grand Teton: Paintbrush Canyon over Paintbrush Divide to Lake Solitude and down Cascade Canyon, from String Lake."""
PDF='grand-teton-paintbrush-cascade-loop.pdf'
OSM_BBOX=(43.735,-110.875,43.825,-110.695)
TILES=dict(z=14,bbox=OSM_BBOX)
JUNCTIONS=dict(start=1381857059,                 # String Lake trailhead
               bridge=1829343849,                # footbridge between String and Leigh Lakes
               paint=1381857170,                 # Paintbrush Canyon Trail leaves the String Lake loop
               lower=1829350138,                 # lower Holly Lake junction
               holly=(43.79164,-110.79758),      # Holly Lake
               upper=1832677907,                 # Holly Lake Trail rejoins the canyon trail
               divide=(43.79484,-110.81770),               # Paintbrush Divide
               solitude=3913635757,              # Lake Solitude
               forks=1244992970,                 # forks of Cascade Canyon
               horse=1244992915,                 # horse trail to String Lake leaves, above Inspiration Point
               insp=886140864,                   # Inspiration Point
               jenny=1244993272,                 # Jenny Lake west shore, horse trail rejoins
               outlet=2180517631)                # west end of the bridge over the String Lake outlet
ROUTES={'loop':['start','bridge','paint','lower','holly','upper','divide','solitude','forks','horse','insp','jenny','outlet','start'],
        'direct':['horse','jenny']}
MAIN='loop'
GPX={'loop':'Paintbrush Canyon - Cascade Canyon loop from String Lake (counter-clockwise)'}
MK=[('start',1),('paint',2),('holly',3),('divide',4),('solitude',5),('forks',6),('horse',7),('jenny',8)]
MAP=dict(bbox=(43.748,-110.858,43.814,-110.698),icons=[],k=1.0,scale=(2000,'2 km'),
  overlays=[dict(route='direct',color='BLUE',width=6,dash='13 8')],
  markers=MK,arrow_start=1200,arrow_step=1500,arrow_clear=450,
  labels=[dict(at='start',dx=26,dy=7,text='String Lake trailhead',size=19,weight=700),
          dict(at='paint',dx=-24,dy=-12,text='Paintbrush Canyon junction',anchor='end',size=17),
          dict(at='holly',dx=0,dy=-30,text='Holly Lake',anchor='middle',size=19,weight=700),
          dict(at='divide',dx=0,dy=-30,text='Paintbrush Divide',anchor='middle',size=19,weight=700),
          dict(at='solitude',dx=-26,dy=7,text='Lake Solitude',anchor='end',size=19,weight=700),
          dict(at='forks',dx=-26,dy=7,text='The Forks',anchor='end',size=19,weight=700),
          dict(at='insp',dx=4,dy=38,text='Inspiration Point',anchor='middle',size=17),
          dict(at=(43.7722,-110.7500),dx=0,dy=0,text='short cut',anchor='middle',size=16,color='BLUE',weight=700),
          dict(at=(43.7925,-110.7740),dx=0,dy=0,text='Paintbrush Canyon',anchor='middle',size=18),
          dict(at=(43.7605,-110.7850),dx=0,dy=0,text='Cascade Canyon',anchor='middle',size=18),
          dict(at='jenny',dx=26,dy=7,text='west shore',size=17)])
PROFILE=dict(emin=1600,emax=3400,grid=200,label_every=400,height=300,km_step=5,
  markers=[('start',1,18),('paint',2,0),('holly',3,0),('divide',4,0),('solitude',5,0),('forks',6,0),('horse',7,0),('jenny',8,0),('start_end',1,0)],
  notes=[(6500,1800,'Paintbrush Canyon: 1,190 m up in 12.7 km'),(21500,1800,'Lake Solitude and Cascade Canyon: downhill for 15 km'),(29200,1800,'lakeshore')])
JX=(43.47990,-110.76243)
ACCESS=dict(**{'from':JX,'to':(43.78520,-110.72760)},z=13,bbox=(43.44,-110.97,43.83,-110.48),pad=(820,980,160,200),k=1.6,mk=1.1,scale=(5000,'5 km'),
  markers=[dict(letter='J',at=('at',JX),label='Jackson',dx=52,dy=14,size=40),
           dict(letter='M',at=('name','Teton Park Road'),label='Moose Junction',dx=52,dy=14,size=40),
           dict(letter='S',at=('at',(43.75180,-110.72130)),label='South Jenny Lake',dx=52,dy=14,size=40),
           dict(letter='N',at=('name','Jenny Lake Loop'),label='North Jenny Lake Junction',dx=52,dy=14,size=40),
           dict(letter='1',at=('end',),label='String Lake trailhead',dx=-44,dy=-14,anchor='end',size=40,weight=700,fill='RED')],
  places=[])
G='Grand Teton National Park (NPS)'
PHOTOS=dict(
 cover=dict(file='File:Lake Solitude (53503523069).jpg',short='Lake Solitude',cls='cover',
   caption='Lake Solitude, a day and a half from the car, with the Grand Teton seen from behind at the foot of the canyon you walk down next.'),
 holly=dict(file='File:Holly Lake S. Zenner.jpg',short='Holly Lake',cls='tri',
   caption='Holly Lake, the usual first camp, in its bowl under the canyon wall.'),
 divide=dict(file='File:Wildflowers on Paintbrush Divide (53503211876).jpg',short='Paintbrush Divide',cls='tri',
   caption='High summer near Paintbrush Divide: flowers on the slope, snow still in the gullies.'),
 northfork=dict(file='File:North Fork Cascade Canyon (48915785181).jpg',short='North Fork',cls='tri',
   caption='Coming down the North Fork of Cascade Canyon, the Grand Teton straight ahead.'),
 grizzly=dict(file='File:Grizzly Bear (48914677793).jpg',short='Grizzly bear',cls='bio',caption='Grizzly: hump, dished face.'),
 blackbear=dict(file='File:Black Bear (48881919318).jpg',short='Black bear',cls='bio',caption='Black bear: straight nose.'),
 moose=dict(file='File:Cow Moose browsing in the willows (32093794131).jpg',short='Moose',cls='bio',caption='Cow moose in willows.'),
 pika=dict(file='File:Pika (53503522104).jpg',short='Pika',cls='bio',caption='Pika with hay.'),
 marmot=dict(file='File:Marmot in Grand Teton NP-NPS.jpg',short='Marmot',cls='bio',caption='Yellow-bellied marmot.'),
 weasel=dict(file='File:Long-tailed weasel (30228536403).jpg',short='Long-tailed weasel',cls='bio',caption='Long-tailed (Yellowstone).'),
 marten=dict(file='File:American Marten.jpg',short='Marten',cls='bio',caption='Marten (photo from elsewhere).'),
)
