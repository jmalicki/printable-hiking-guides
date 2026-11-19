"""Purisima Creek Redwoods: up the creek, across on the Craig Britton Trail, down Harkins Ridge, from the Higgins-Purisima trailhead."""
PDF='purisima-creek-redwoods-loop.pdf'
OSM_BBOX=(37.395,-122.425,37.465,-122.305)
TILES=dict(z=15,bbox=(37.420,-122.385,37.455,-122.322))
JUNCTIONS=dict(start=(37.43723,-122.36968,['Purisima Creek Trail']),   # Higgins-Purisima trailhead
  grab=(37.43424,-122.34967,['Purisima Creek Trail']),               # Grabtown Gulch Trail leaves
  cbj=(37.43047,-122.33609,['Craig Britton Trail']),                 # Craig Britton Trail leaves the creek
  soda=(37.43944,-122.33971,['Craig Britton Trail']),                # head of Soda Gulch
  hark=(37.44139,-122.34780,['Harkins Ridge Trail']),                # Craig Britton Trail meets Harkins Ridge Trail
  bottom=(37.43735,-122.36911,['Harkins Ridge Trail']),
  north=(37.45008,-122.33849,['North Ridge Trail']))                  # North Ridge car park on Skyline Boulevard (plan B start)              # Harkins Ridge Trail reaches the creek
ROUTES={'main':['start','grab','cbj','soda','hark','bottom','start'],
        'skyline':['north','hark','bottom','start','grab','cbj','soda','hark','north']}   # the same loop entered from the top
MAIN='main';GPX={'main':'Purisima Creek Redwoods: creek, Craig Britton Trail and Harkins Ridge loop'}
TILES=dict(z=16,bbox=(37.422,-122.382,37.450,-122.326))
MK=[('start',1),('grab',2),('cbj',3),('soda',4),('hark',5)]
MAP=dict(pad=230,aspect=1.6,extent=['main'],overlays=[dict(route='skyline',frm='north',to='hark',color='BLUE',width=9,dash='16 10')],markers=MK,icons=[],k=1.8,scale=(500,'500 m'),arrow_start=600,arrow_step=640,arrow_clear=160,
  labels=[dict(at='start',dx=0,dy=52,text='START / FINISH',anchor='middle',size=21,weight=700),
          dict(at='start',dx=0,dy=76,text='lower trailhead (7 spaces)',anchor='middle',size=19),
          dict(at='grab',dx=0,dy=46,text='Grabtown Gulch',anchor='middle',size=19),
          dict(at='cbj',dx=-30,dy=30,text='Craig Britton Trail',anchor='end',size=20,weight=700),
          dict(at='soda',dx=28,dy=8,text='Soda Gulch',size=19),
          dict(at='hark',dx=-28,dy=-14,text='Harkins Ridge',anchor='end',size=20,weight=700),
          dict(at=(37.4447,-122.3432),dx=16,dy=0,text='to Skyline (plan B)',size=18,weight=700,color='BLUE')])
PROFILE=dict(emin=100,emax=500,grid=50,label_every=100,height=300,km_step=1,
  markers=[('start',1,12),('grab',2,0),('cbj',3,0),('soda',4,0),('hark',5,0),('start_end',1,0)],
  notes=[(5600,150,'up the creek  ·  across on the Craig Britton Trail  ·  down Harkins Ridge')])
ACCESS=dict(**{'from':(37.4689,-122.4330),'to':(37.43723,-122.36968)},z=14,bbox=(37.405,-122.465,37.490,-122.345),pad=(260,300,220,220),k=2.0,mk=1.15,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',80),label='Highway 92 / Highway 1',dx=56,dy=16,size=44),
           dict(letter='B',at=('name','Higgins Canyon Road'),label='Higgins Canyon Road',dx=56,dy=16,size=44),
           dict(letter='P',at=('end',),label='Trailhead',dx=0,dy=-60,anchor='middle',size=46,weight=700,fill='RED')],
  places=[dict(at=(37.4636,-122.4286),label='Half Moon Bay',dot=False,dx=-40,dy=0,anchor='end',size=40)])
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
