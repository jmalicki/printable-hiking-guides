"""Yellowstone: Bighorn Peak by the Black Butte Creek Trail from US 191, out and back."""
PDF='yellowstone-bighorn-peak-from-black-butte.pdf'
OSM_BBOX=(44.97,-111.20,45.11,-110.97)
TILES=dict(z=15,bbox=(45.022,-111.135,45.080,-111.030))
JUNCTIONS=dict(th=3076159384,                  # Black Butte trailhead, US 191 (east side of the road)
               cutoff=1197900412,              # Black Butte-Daly Creek Cutoff leaves
               camp=1197904157,                # spur to campsite WF1
               bridge=3076159954,              # footbridge over Black Butte Creek
               sky=1197927900,                 # Sky Rim Trail junction, on the meadow top
               summit=1197910097)              # Bighorn Peak
OUT_=['th','cutoff','camp','bridge','sky','summit']
ROUTES={'main':OUT_+OUT_[-2::-1]}
MAIN='main'
GPX={'main':'Bighorn Peak by the Black Butte Creek Trail, out and back'}
MK=[('th',1),('cutoff',2),('bridge',3),('sky',4),('summit',5)]
MAP=dict(bbox=(45.0300,-111.1245,45.0715,-111.0405),icons=[],k=1.2,scale=(1000,'1 km'),overlays=[],markers=MK,
  arrow_start=700,arrow_step=1000,arrow_end=9300,arrow_clear=300,
  labels=[dict(at='th',dx=26,dy=28,text='Black Butte trailhead',size=22,weight=700),
          dict(at='cutoff',dx=-26,dy=-8,text='Daly Creek cutoff',anchor='end',size=21),
          dict(at='camp',dx=18,dy=30,text='campsite WF1',size=19),
          dict(at='bridge',dx=0,dy=-30,text='footbridge',anchor='middle',size=21),
          dict(at='sky',dx=-12,dy=-30,text='Sky Rim junction',anchor='end',size=21),
          dict(at='summit',dx=28,dy=8,text='Bighorn Peak',size=23,weight=700),
          dict(at=(45.0530,-111.0700),dx=24,dy=30,text='switchbacks',size=19)])
PROFILE=dict(emin=2000,emax=3100,grid=100,label_every=200,height=270,km_step=2,
  markers=[('th',1,16),('cutoff',2,0),('bridge',3,0),('sky',4,-24),('summit',5,0),('sky_end',4,24),('bridge_end',3,0),('cutoff_end',2,0),('th_end',1,0)],
  notes=[(4300,2045,'beside the creek: +340 m'),(7700,2180,'the dry climb: +595 m in 4.7 km'),(13700,2180,'down the same way')])
WY_=(44.66210,-111.10410)     # West Yellowstone
BS_=(45.26460,-111.25310)     # US 191 / MT 64, Big Sky turn
TH_=(45.03496,-111.11403)
ACCESS=dict(**{'from':WY_,'to':TH_},z=12,bbox=(44.60,-111.50,45.32,-110.80),pad=(430,470,1040,110),k=1.4,mk=0.8,scale=(10000,'10 km'),
  extra=[{'from':BS_,'to':TH_,'color':'INK'}],
  markers=[dict(letter='W',at=('at',WY_),label='West Yellowstone',dx=40,dy=13,size=36,weight=700),
           dict(letter='P',at=('end',),label='Black Butte trailhead',dx=40,dy=13,size=36,weight=700,fill='RED'),
           dict(letter='B',at=('at',BS_),label='Big Sky turn',dx=40,dy=13,size=36,weight=700)],
  places=[dict(at=(45.0126,-111.0807),label='Specimen Creek trailhead',dx=22,dy=16,size=30)])
PHOTOS=dict(
 hero=dict(file='File:Big Horn Peak.jpg',short='Bighorn Peak',cls='cover',
   caption='The last few minutes of the climb: the trail follows the crest to the summit of Bighorn Peak, above cliffs of dark volcanic rock.'),
 junction=dict(file='File:Views along the Black Butte Creek Trail- trail junction (53069067386).jpg',short='Cutoff junction',cls='tri',
   caption='The meadow junction at 2. Follow the arrow for Bighorn Peak.'),
 sign=dict(file='File:Views along the Sky Rim Trail- Big Horn trail junction (2) (53069066351).jpg',short='Sky Rim junction',cls='tri',
   caption='The sign on the meadow top at 4, with the Madison Range behind.'),
 bloom=dict(file='File:Views along the Black Butte Creek Trail- full bloom (53069462355).jpg',short='Upper trail',cls='tri',
   caption='July on the upper trail, among standing dead trees.'),
 ridge=dict(file='File:Views along the Sky Rim Trail- trail looking north (53068465917).jpg',short='Sky Rim',cls='tri',
   caption='The Sky Rim: grass on one side of the crest, cliffs on the other.'),
 lone=dict(file='File:Views along the Sky Rim Trail- Lone Mountain (53069258984).jpg',short='Lone Mountain',cls='tri',
   caption='West from the rim: Lone Mountain, the pointed peak above Big Sky.'),
 petrified=dict(file='File:Views along the Sky Rim Trail- petrified wood (53069238189).jpg',short='Petrified wood',cls='duo',
   caption='A petrified trunk beside the Sky Rim Trail, photographed by the Park Service.'),
 flank=dict(file='File:Views along the Sky Rim Trail- Big Horn Peak flank.jpg',short='The cliffs',cls='duo',
   caption='The flank of Bighorn Peak: stacked beds of volcanic rubble, weathered into towers.'),
 parking=dict(file='File:Black Butte Trailhead Parking (356f3948-c1dd-465e-b893-d11e9576e7e2).jpg',short='Parking',cls='tri',
   caption='The gravel pull-out, on the river side of the highway.'),
 trailhead=dict(file='File:Black Butte Trailhead (1299516a-4d28-4987-aa4d-24c428eb107c).jpg',short='Trailhead',cls='tri',
   caption='The trail starts at this small sign across the road.'),
 sheep=dict(file='File:Ram and ewe bighorn sheep (37991290334).jpg',short='Bighorn sheep',cls='bio',caption='Ram, left, and ewe.'),
 grizzly=dict(file='File:Grizzly Bear on Swan Lake Flat - Flickr - YellowstoneNPS.jpg',short='Grizzly bear',cls='bio',caption='Grizzly: hump, dished face.'),
 moose=dict(file='File:Cow and calf moose (df0ea03b-2518-4358-89ef-edef4eb07799).jpg',short='Moose',cls='bio',caption='Cow moose and calf.'),
 elk=dict(file='File:Bull elk bugling on a frosty morning in Canyon area (32060852554).jpg',short='Elk',cls='bio',caption='Bull elk bugling, autumn.'),
 dusky=dict(file='File:Dusky grouse (14952432139).jpg',short='Dusky grouse',cls='bio',caption='Dusky grouse.'),
 ruffed=dict(file='File:Ruffed grouse (15116108746).jpg',short='Ruffed grouse',cls='bio',caption='Ruffed grouse, drumming.'),
 track=dict(file='File:Grizzly bear track (15242966449).jpg',short='Grizzly track',cls='bio',caption='Grizzly track in mud.'),
 marmot=dict(file='File:Yellow-bellied marmot (54571541454).jpg',short='Marmot',cls='bio',caption='Yellow-bellied marmot.'),
)
