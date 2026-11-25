"""Castle Rock State Park: Castle Rock, the falls, the Saratoga Gap Trail to the trail camp, back by the Ridge Trail and Goat Rock."""
PDF='castle-rock-saratoga-gap-ridge-loop.pdf'
PARK='Castle Rock State Park'
REGION='bay-area'
OSM_BBOX=(37.215,-122.140,37.262,-122.085)
TILES=dict(z=16,bbox=(37.218,-122.136,37.246,-122.084))
JUNCTIONS=dict(start=(37.23212,-122.09870),          # Kirkwood entrance car park
  th=3557215756,                                     # old trailhead: Saratoga Gap Trail and Castle Rock Trail part
  rock=461389778,                                    # Castle Rock
  crj=461377951,                                     # Castle Rock Trail rejoins the Saratoga Gap Trail
  rj=3557215737,                                     # Ridge Trail leaves (the way back)
  falls=1359421972,                                  # Castle Rock Falls platform
  icj=479731496,                                     # Interconnector Trail leaves the Saratoga Gap Trail
  cable=(37.23290,-122.12200,['Saratoga Gap Trail']),   # the cabled ledge: placed at the trail's low point, from trip reports (approximate)
  wj=479729456,                                      # far end: Ridge Trail meets the Saratoga Gap Trail
  camp=(37.23624,-122.11907),                        # Castle Rock Trail Camp
  ici=479730041,                                     # Ridge Trail / Interconnector
  goat=479729904)                                    # Goat Rock
ROUTES={'main':['start','th','rock','crj','rj','falls','icj','cable','wj','camp','wj','ici','goat','rj','crj','th','start'],
        'short':['start','th','rock','crj','rj','falls','icj','ici','goat','rj','crj','th','start'],     # turns back before the cabled ledge
        'ridge':['start','th','crj','rj','goat','ici','wj','camp']}                                        # to the trail camp by the Ridge Trail only (one way)
MAIN='main';GPX={'main':'Castle Rock State Park: Castle Rock, Saratoga Gap Trail to the trail camp, back by the Ridge Trail','short':'Castle Rock State Park: short loop by the Interconnector Trail (avoids the cabled ledge)'}
LEG_ALLOW={('rock','crj'):['Castle Rock Trail']}      # down the far side of the rock, not back to the car park
MK=[('start',1),('rock',2),('rj',3),('falls',4),('icj',5),('cable',6),('wj',7),('camp',8),('ici',9),('goat',10)]
MAP=dict(pad=230,aspect=1.75,extent=['main'],overlays=[dict(route='short',frm='icj',to='ici',color='BLUE',width=7,dash='14 9')],markers=MK,icons=[],k=1.25,scale=(500,'500 m'),arrow_start=1050,arrow_step=640,arrow_clear=150,
  labels=[dict(at='start',dx=0,dy=-30,text='START / FINISH',anchor='middle',size=20,weight=700),
          dict(at='start',dx=0,dy=-52,text='Kirkwood entrance',anchor='middle',size=18),
          dict(at='rock',dx=0,dy=44,text='Castle Rock',anchor='middle',size=20,weight=700),
          dict(at='falls',dx=0,dy=40,text='Castle Rock Falls',anchor='middle',size=19,weight=700),
          dict(at='icj',dx=0,dy=42,text='Interconnector',anchor='middle',size=18,color='BLUE',weight=700),
          dict(at='cable',dx=-10,dy=44,text='cabled ledge',anchor='end',size=20,weight=700,color='RED'),
          dict(at='cable',dx=-10,dy=66,text='(position approximate)',anchor='end',size=16,color='RED'),
          dict(at='camp',dx=0,dy=-30,text='trail camp',anchor='middle',size=19,weight=700),
          dict(at='goat',dx=0,dy=-30,text='Goat Rock',anchor='middle',size=20,weight=700),
          dict(at=(37.2311,-122.1163),dx=0,dy=0,text='Ridge Trail',anchor='middle',size=18),
          dict(at=(37.2272,-122.1085),dx=0,dy=0,text='Saratoga Gap Trail',anchor='middle',size=18)])
PROFILE=dict(emin=650,emax=1000,grid=50,label_every=100,height=300,km_step=1,
  markers=[('start',1,10),('rock',2,0),('rj',3,-8),('falls',4,10),('icj',5,0),('cable',6,-6),('wj',7,-4),('camp',8,12),('ici',9,0),('goat',10,0),('start_end',1,-10)],
  notes=[(2900,690,'Saratoga Gap Trail: open hillside, mostly down'),(7500,690,'Ridge Trail: wooded, mostly up')])
ACCESS=dict(**{'from':(37.2567,-122.0349),'to':(37.23233,-122.09876)},z=14,bbox=(37.210,-122.140,37.280,-122.020),pad=(260,260,230,230),k=1.9,mk=1.0,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',60),label='Saratoga village',dx=0,dy=-56,anchor='middle',size=40),
           dict(letter='B',at=('name','Skyline Boulevard'),label='Saratoga Gap',dx=0,dy=-56,anchor='middle',size=40),
           dict(letter='P',at=('end',),label='Kirkwood entrance',dx=-52,dy=14,anchor='end',size=42,weight=700,fill='RED')],
  places=[])
PHOTOS=dict(
 hero=dict(file='File:Castle Rock State Park 9.JPG',short='Climber',cls='hero short',crop=(0,0.10,1,0.92),
   caption='A climber on one of the park’s sandstone crags, above the forested valley of the San Lorenzo River.'),
 rock=dict(file='File:CastleRock.JPG',short='Castle Rock',cls='tri',crop=(0,0.36,1,0.86),
   caption='Castle Rock, with climbers at its foot.'),
 trail=dict(file='File:Castle Rock State Park 6.JPG',short='Open slope',cls='tri',
   caption='The path along the park’s open western slope.'),
 boulders=dict(file='File:Castle Rock State Park in California with rock formations.JPG',short='Boulders',cls='tri',
   caption='Sandstone boulders under the oaks.'),
 rock2=dict(file='File:Castle Rock State Park rock formation.JPG',short='Tafoni',cls='duo',
   caption='Tafoni: pockets and honeycomb where the rock’s crust has broken.'),
 view=dict(file='File:Castle Rock State Park 8.JPG',short='From the ridge',cls='duo',crop=(0,0.12,1,0.92),
   caption='Forest to the horizon, from the ridge.'),
)
