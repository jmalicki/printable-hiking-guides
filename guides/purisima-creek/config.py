"""Purisima Creek Redwoods from Skyline: down Whittemore Gulch, up Purisima Creek, across the Craig Britton Trail, up Harkins Ridge."""
PDF='purisima-creek-redwoods-loop.pdf'
PARK='Purisima Creek Redwoods Preserve'            # shown after the title in the hike lists
REGION='bay-area'            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
OSM_BBOX=(37.395,-122.425,37.465,-122.305)
TILES=dict(z=15,bbox=(37.420,-122.385,37.455,-122.322))
JUNCTIONS=dict(north=(37.45008,-122.33849,['North Ridge Trail']),     # North Ridge car park, Skyline Boulevard
  htop=(37.44920,-122.34346,['Harkins Ridge Trail']),                # Harkins Ridge Trail leaves the North Ridge Trail
  wtop=(37.44957,-122.34960,['Whittemore Gulch Trail']),             # Whittemore Gulch Trail leaves the North Ridge Trail
  wmid=(37.44490,-122.35590,['Whittemore Gulch Trail']),             # foot of the switchbacks in Whittemore Gulch
  bottom=(37.43735,-122.36911,['Harkins Ridge Trail']),              # canyon floor: Whittemore, Harkins and the creek road meet
  start=(37.43723,-122.36968,['Purisima Creek Trail']),              # lower trailhead (toilet)
  grab=(37.43424,-122.34967,['Purisima Creek Trail']),               # Grabtown Gulch Trail leaves
  cbj=(37.43047,-122.33609,['Craig Britton Trail']),                 # Craig Britton Trail leaves the creek
  soda=(37.43944,-122.33971,['Craig Britton Trail']),                # head of Soda Gulch
  hark=(37.44139,-122.34780,['Harkins Ridge Trail']))                # Craig Britton Trail meets Harkins Ridge Trail
ROUTES={'main':['north','htop','wtop','wmid','bottom','start','grab','cbj','soda','hark','htop','north'],
        'short':['north','htop','wtop','wmid','bottom','hark','htop','north']}     # skips the creek and the Craig Britton Trail
MAIN='main';GPX={'main':'Purisima Creek Redwoods from Skyline: Whittemore Gulch, Purisima Creek, Craig Britton, Harkins Ridge','short':'Purisima Creek Redwoods from Skyline: Whittemore Gulch and Harkins Ridge'}
TILES=dict(z=16,bbox=(37.422,-122.382,37.450,-122.326))
MK=[('north',1),('wtop',2),('wmid',3),('start',4),('grab',5),('cbj',6),('soda',7),('hark',8)]
MAP=dict(pad=200,aspect=1.45,extent=['main'],overlays=[dict(route='short',frm='bottom',to='hark',color='BLUE',width=9,dash='16 10')],markers=MK,icons=[],k=1.8,scale=(500,'500 m'),arrow_start=700,arrow_step=760,arrow_clear=170,
  labels=[dict(at='north',dx=30,dy=-4,text='START / FINISH',size=21,weight=700),
          dict(at='north',dx=30,dy=20,text='North Ridge car park',size=19),
          dict(at='wtop',dx=-28,dy=6,text='Whittemore Gulch Trail',anchor='end',size=19,weight=700),
          dict(at='start',dx=0,dy=50,text='lower trailhead',anchor='middle',size=19,weight=700),
          dict(at='grab',dx=0,dy=46,text='Grabtown Gulch',anchor='middle',size=19),
          dict(at='cbj',dx=-30,dy=30,text='Craig Britton Trail',anchor='end',size=19,weight=700),
          dict(at='soda',dx=28,dy=8,text='Soda Gulch',size=19),
          dict(at='hark',dx=28,dy=-10,text='Harkins Ridge',size=19,weight=700),
          dict(at=(37.4405,-122.3600),dx=0,dy=0,text='shorter way back',anchor='middle',size=17,weight=700,color='BLUE')])
PROFILE=dict(emin=100,emax=650,grid=50,label_every=100,height=300,km_step=1,
  markers=[('north',1,12),('wtop',2,0),('wmid',3,0),('start',4,0),('grab',5,0),('cbj',6,0),('soda',7,0),('hark',8,0),('north_end',1,0)],
  notes=[(1700,170,'down Whittemore Gulch'),(10600,170,'up the creek  ·  across on the Craig Britton Trail  ·  up the ridge')])
ACCESS=dict(**{'from':(37.5005,-122.3305),'to':(37.45008,-122.33849)},z=14,bbox=(37.425,-122.405,37.515,-122.300),pad=(520,330,200,300),k=2.0,mk=1.15,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',80),label='Interstate 280',dx=0,dy=-62,anchor='middle',size=44),
           dict(letter='B',at=('name','Skyline Boulevard'),label='Skyline Boulevard',dx=-56,dy=16,anchor='end',size=44),
           dict(letter='P',at=('end',),label='North Ridge car park',dx=-56,dy=16,anchor='end',size=46,weight=700,fill='RED')],
  places=[])
OA='Oleg Alexandrov'
PHOTOS=dict(
 hero=dict(file='File:Purisima Creek Trail 5.JPG',short='Redwoods',cls='hero',crop=(0,0.10,1,0.85),
   caption='Second-growth redwoods above the Purisima Creek Trail: about a century old, and already a forest.'),
 road=dict(file='File:Purisima Creek Trail 1.JPG',short='Creek trail',cls='tri',
   caption='The Purisima Creek Trail, an old logging road, a mile above the trailhead.'),
 creek=dict(file='File:Purisima Creek Trail 6.JPG',short='Purisima Creek',cls='tri',
   caption='Purisima Creek: no salmon, but its own trout.'),
 slug=dict(file='File:Banana slug on Purisima Creek Trail.JPG',short='Banana slug',cls='tri',crop=(0.08,0.12,0.92,0.92),
   caption='A banana slug on the trail. Watch your step after rain.'),
 stand=dict(file='File:Purisima Creek Redwoods, Aug 2019 3.jpg',short='Redwood stand',cls='duo',
   caption='Slender trunks, close together: what a logged redwood forest looks like a hundred years on.'),
 vista=dict(file='File:Purisima Creek vista.jpg',short='From the ridge',cls='duo',crop=(0,0.08,1,0.92),
   caption='Fog lifting off the canyon, seen from the ridge.'),
)
