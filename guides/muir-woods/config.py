"""Muir Woods by the back door: Mountain Home Inn -> Canopy View (down) -> Muir Woods -> Bootjack (up) -> Troop 80."""
PDF='muir-woods-back-door.pdf'
PARK='Mount Tamalpais State Park and Muir Woods National Monument'            # shown after the title in the hike lists
REGION='bay-area'            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
OSM_BBOX=(37.886,-122.612,37.916,-122.562)          # S,W,N,E
TILES=dict(z=16,bbox=(37.8895,-122.6025,37.9160,-122.5670))
# junctions: OSM node id, or (lat,lon[,way names]) snapped to the nearest trail node
JUNCTIONS=dict(start=(37.91020,-122.57721),t80=313621042,vw=511981002,bj=261758361,fc=261758332,lostfc=361153027,
               lostcv=354582989,cvtop=361152366,cvb=(37.8937516,-122.5741258,['Canopy View Trail']),
               vc=(37.8927962,-122.5724843,['Redwood Creek Trail','Bohemian Grove Trail','(footway)']))
# clockwise: down Canopy View (even grade), up Bootjack (steps are kinder to climb than descend)
ROUTES={'main':['start','cvtop','lostcv','cvb','fc','bj','vw','t80','start'],
        'short':['start','cvtop','lostcv','cvb','fc','lostfc','lostcv','cvtop','start'],
        'vc_spur':['cvb','vc']}
GPX={'main':'Mountain Home to Muir Woods - down Canopy View, back up Bootjack and Troop 80',
     'short':'Mountain Home to Muir Woods - short version, back up Fern Creek and Lost Trail'}
MAIN='main'
MAP=dict(pad=120,aspect=180/170,extent=['main','short','vc_spur'],
  overlays=[dict(route='short',frm='fc',to='lostcv_end',color='BLUE',width=8,dash='20 11'),
            dict(route='vc_spur',color='INK',width=6,dash='5 9')],
  markers=[('start',1),('cvtop',2),('lostcv',3),('cvb',4),('fc',5),('bj',6),('vw',7),('t80',8)],
  labels=[dict(at='start',dx=28,dy=-8,text='START / FINISH',size=22,weight=700),
          dict(at='start',dx=28,dy=17,text='Mountain Home Inn',size=20,weight=500),
          dict(at='vw',dx=-6,dy=50,text='Van Wyck Meadow',anchor='middle',size=20,weight=500),
          dict(at='cvb',dx=-28,dy=6,text='Founders Grove',anchor='end',size=20,weight=500),
          dict(at=(37.8982635,-122.5756648),dx=-22,dy=4,text='Cathedral Grove',anchor='end',size=20,weight=500),
          dict(at='vc',dx=24,dy=34,text='Visitor centre, caf&#233;, WC',size=20,weight=500),
          dict(at='lostfc',dx=-20,dy=70,text='Short version',anchor='end',size=20,weight=700,color='BLUE')],
  icons=['vc'])
PROFILE=dict(emin=0,emax=350,grid=50,label_every=100,
  markers=[('start',1,0),('cvtop',2,0),('lostcv',3,0),('cvb',4,0),('fc',5,-16),('bj',6,16),('vw',7,0),('t80',8,0),('start_end',1,0)],
  notes=[(3600,292,'&#8592; Canopy View descent: 240 m down in 2.4 km'),(3600,240,'Bootjack climb: 250 m up in 2.1 km &#8594;')])
ACCESS=dict(**{'from':(37.8078,-122.4750),'to':(37.91020,-122.57721)},z=14,bbox=(37.795,-122.615,37.928,-122.455),
  pad=(300,230,150,110),
  markers=[dict(letter='A',at=('m',1700),label='Golden Gate Bridge',dx=-50,dy=13,anchor='end'),
           dict(letter='B',at=('type','off ramp'),label='Exit Hwy 1',dx=50,dy=13),
           dict(letter='C',at=('name','Shoreline Highway'),label='Tam Junction',dx=10,dy=82,anchor='middle'),
           dict(letter='D',at=('name','Panoramic Highway'),label='Panoramic Hwy',dx=-10,dy=82,anchor='middle'),
           dict(letter='E',at=('after','Panoramic Highway',1600),label='Four-way junction',dx=-44,dy=-30,anchor='end'),
           dict(letter='P',at=('end',),label='Mountain Home Inn',dx=-20,dy=-52,anchor='middle',size=40,weight=700,fill='RED')],
  places=[dict(at=(37.9060,-122.5475),label='Mill Valley',dx=26,dy=13),
          dict(at=(37.8928,-122.5725),label='Muir Woods',dx=-26,dy=13,anchor='end'),
          dict(at=(37.8030,-122.4790),label='San Francisco',anchor='end',size=40,weight=700,dot=False)])
PHOTOS=dict(hero=dict(file='File:Muir Woods National Monument (47879029461).jpg',short='Muir Woods',cls='tri',crop=(0,0.28,1,0.66),
  caption='Old-growth redwoods on the main trail of Muir Woods, halfway round the loop.'))
