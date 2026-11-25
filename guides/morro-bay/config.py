"""Montaña de Oro: the Bluff Trail and Valencia Peak, with the sea otters of Morro Bay harbour afterwards."""
PDF='montana-de-oro-bluffs-valencia-peak-morro-bay.pdf'
PARK='Montaña de Oro State Park'            # shown after the title in the hike lists
OSM_BBOX=(35.240,-120.912,35.290,-120.850)
JUNCTIONS=dict(start=1367831175,                 # Bluff Trail trailhead on Pecho Valley Road, opposite the Valencia Peak trailhead
               corallina=(35.27145,-120.89600,['Bluff Trail']),
               quarry=(35.26744,-120.89480,['Bluff Trail']),
               grotto=(35.26196,-120.89480,['Bluff Trail','Montana de Oro State Park']),
               bluffend=8423765528,              # south end of the Bluff Trail at the Coon Creek car park
               rsf=3443609428,                   # Rattlesnake Flats Trail leaves the Coon Creek car park
               badger=90960824,                  # Rattlesnake Flats Trail meets the Badger Trail
               fourway=4753332251,               # four-way junction: Badger, Beebe and Valencia Peak trails
               summit=5636459272,                # Valencia Peak
               vpth=1367831050)                  # Valencia Peak trailhead, across the road from the start
RSF={'Rattlesnake Flats Trail','Rattlesnake Flats','(path)','(track)','(footway)'}
UP={'Valencia Peak Trail','Badger Trail'}                 # the upper trail leaves the Badger Trail 28 m from the four-way junction
LEG_ALLOW={('rsf','badger'):RSF,('badger','fourway'):{'Badger Trail'},('fourway','summit'):UP,('summit','fourway'):UP,('fourway','vpth'):{'Valencia Peak','Valencia Peak Trail','(path)'},
           ('badger','vpth'):RSF|{'Badger Trail','Valencia Peak Trail'}}
ROUTES={'main':['start','corallina','quarry','grotto','bluffend','rsf','badger','fourway','summit','fourway','vpth','start'],
        'short':['start','corallina','quarry','grotto','bluffend','rsf','badger','vpth','start']}
MAIN='main';GPX={'main':'Montana de Oro: Bluff Trail and Valencia Peak','short':'Montana de Oro: Bluff Trail loop'}
# harbour stops for the otters (not on the hike): free points shown on the close-up map of Morro Bay harbour
POINTS=dict(tpier=(35.36937,-120.85590),          # South T-Pier, beside the Great American Fish Company
            walk=(35.37165,-120.86080),           # Harborwalk at Coleman Park
            target=(35.37085,-120.86480))         # Target Rock, at the entrance to the Morro Rock car park
TILES=dict(z=16,bbox=(35.250,-120.906,35.280,-120.858))
DETAIL_TILES=dict(z=16,bbox=(35.361,-120.874,35.377,-120.846))
MK=[('start',1),('corallina',2),('quarry',3),('grotto',4),('bluffend',5),('badger',6),('fourway',7),('summit',8)]
MAP=dict(pad=120,aspect=1.38,extent=['main'],icons=[],k=0.8,scale=(500,'500 m'),
  overlays=[dict(route='short',frm='badger',to='vpth',color='BLUE',width=5,dash='10 7')],
  markers=MK,arrow_start=250,arrow_step=520,arrow_clear=120,
  labels=[dict(at='start',dx=-30,dy=-22,text='START / FINISH',anchor='end',size=24,weight=700),
          dict(at='corallina',dx=-28,dy=8,text='Corallina Cove',anchor='end',size=22,weight=700,color='#0b5f8a'),
          dict(at='quarry',dx=-28,dy=8,text='Quarry Cove',anchor='end',size=22,weight=700,color='#0b5f8a'),
          dict(at='grotto',dx=-28,dy=30,text='Grotto Rock',anchor='end',size=22,weight=700),
          dict(at='bluffend',dx=28,dy=28,text='Coon Creek car park',size=21),
          dict(at='badger',dx=28,dy=-6,text='Badger Trail',size=21),
          dict(at='fourway',dx=28,dy=-10,text='four-way junction',size=21),
          dict(at='summit',dx=30,dy=8,text='Valencia Peak',size=23,weight=700),
          dict(at='summit',dx=30,dy=32,text='{{u:410 m|1,347 ft}}',size=21),
          dict(at=(35.2640,-120.8835),dx=0,dy=0,text='Rattlesnake Flats Trail',anchor='middle',size=19),
          dict(at=(35.2752,-120.8915),dx=0,dy=0,text='Spooner\u2019s Cove',anchor='middle',size=21),
          dict(at=(35.2702,-120.8872),dx=0,dy=0,text='short loop',anchor='middle',size=19,color='BLUE',weight=700)])
# close-up of Morro Bay harbour: where to stand for the otters (letters), and where dinner is
DETAIL=dict(bbox=(35.3628,-120.8712,35.3748,-120.8492),overlays=[],markers=[('tpier','D'),('walk','E'),('target','F')],icons=[],k=1.2,scale=(250,'250 m'),arrow_start=10**9,
  labels=[dict(at='tpier',dx=22,dy=-16,text='South T-Pier',size=19,weight=700),
          dict(at='walk',dx=0,dy=-26,text='Harborwalk',anchor='middle',size=19,weight=700),
          dict(at='target',dx=-22,dy=-18,text='Target Rock',anchor='end',size=19,weight=700),
          dict(at=(35.36967,-120.86770),dx=0,dy=40,text='Morro Rock',anchor='middle',size=20,weight=700),
          dict(at=(35.3668,-120.8546),dx=-12,dy=6,text='Embarcadero: dinner',anchor='end',size=19,weight=700,color='RED'),
          dict(at=(35.3690,-120.8610),dx=0,dy=0,text='harbour',anchor='middle',size=18,color='#0b5f8a',weight=700)])
PROFILE=dict(emin=0,emax=450,grid=50,label_every=100,height=250,km_step=1,
  markers=[('start',1,8),('corallina',2,0),('quarry',3,0),('grotto',4,0),('bluffend',5,0),('badger',6,0),('fourway',7,0),('summit',8,0),('fourway_end',7,0),('start_end',1,-8)],
  notes=[(7800,70,'Valencia Peak Trail: 245 m up in 1.7 km')])
ACCESS=dict(**{'from':(35.2529,-120.6858),'to':(35.27274,-120.88859)},z=13,bbox=(35.215,-120.935,35.405,-120.640),pad=(190,230,790,150),k=1.5,mk=0.75,scale=(5000,'5 km'),
  extra=[{'from':(35.27274,-120.88859),'to':(35.3704,-120.8583)}],     # trailhead -> Morro Bay harbour, for the otters and dinner
  markers=[dict(letter='A',at=('m',250),label='US 101',dx=-36,dy=-22,anchor='end',size=30),
           dict(letter='B',at=('m',14900),label='Los Osos',dx=0,dy=56,anchor='middle',size=30),
           dict(letter='P',at=('end',),label='Bluff Trail car park',dx=38,dy=12,size=30,weight=700,fill='RED'),
           dict(letter='C',at=('at',(35.3704,-120.8583)),label='Morro Bay harbour',dx=38,dy=12,size=30,weight=700,fill='RED')],
  places=[dict(at=(35.2700,-120.6700),label='San Luis Obispo',dot=False,size=28,weight=500,anchor='middle'),
          dict(at=(35.36967,-120.86770),label='Morro Rock',dot=False,dx=-22,dy=34,size=26,weight=500,anchor='end'),
          dict(at=(35.2630,-120.8721),label='Valencia Peak',dx=24,dy=30,size=26,weight=500)])
# Photos: Wikimedia Commons. Captions say where a photo was not taken here.
PHOTOS=dict(
 hero=dict(short='Cover',cls='hero short',file='File:Montaña de Oro - Shale Formations - Flickr - docentjoyce.jpg',crop=(0,0.30,1,0.80),caption='Tilted beds of shale run out into the surf below the Bluff Trail.'),
 stack=dict(short='Sea stack',cls='tri',file='File:The Sphynx - MdO - Flickr - docentjoyce.jpg',caption='A stack and arch cut by the waves on the Montaña de Oro shore.'),
 peakview=dict(short='From the Valencia Peak Trail',cls='tri',file='File:The Pacific Ocean coastline as seen from Valencia Peak.jpg',caption='Looking down from the Valencia Peak Trail on the flat shelf the Bluff Trail follows.'),
 o_pier=dict(short='Otters at the pier',cls='bio',file='File:Morro Bay Southern sea otters (48749553118).jpg',caption='Otters off the Embarcadero, April 2019: the dark shapes in front of the pier.'),
 o_raft=dict(short='Raft',cls='bio',file='File:Morro Bay Southern Sea Otters (48750092062).jpg',caption='A raft resting in Morro Bay.'),
 o_pup=dict(short='Otter and pup',cls='bio',file='File:Sea otter nursing02.jpg',caption='Mother and pup in Morro Bay harbour.'),
 sealion=dict(short='Sea lion',cls='bio',file='File:California Sea Lion (Zalophus californianus) 02.jpg',caption='California sea lion (photographed at Point Lobos).'),
 falcon=dict(short='Peregrine',cls='bio',file='File:1 of 2 Peregrine Falcon (Falco peregrinus) Morro Rock.jpg',caption='Peregrine falcon at Morro Rock.'),
 oyster=dict(short='Oystercatcher',cls='bio',file='File:Black Oystercatcher Pt Lobos State Natural Reserve Monterey CA 2017-04-11 13-30-04 (33481810144).jpg',caption='Black oystercatchers (photographed at Point Lobos).'),
 strata=dict(short='Tilted beds',cls='bio',file='File:Montana de Oro State Park - Bluff Trail (18).jpg',caption='Tilted beds beside the Bluff Trail.'),
 terraces=dict(short='Terraces',cls='bio',file='File:Marine Terraces-Montaña de Oro State Park.jpg',caption='Valencia Peak above the grassy steps of old shorelines.'),
 rock=dict(short='Morro Rock',cls='bio',file='File:Morro Bay, California 02.JPG',caption='Morro Rock from the South T-Pier.'),
)
