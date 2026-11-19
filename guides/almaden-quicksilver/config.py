"""Almaden Quicksilver County Park: the mining-history loop over Mine Hill from the Hacienda entrance, New Almaden."""
PDF='almaden-quicksilver-mine-hill-loop.pdf'
REGION='bay-area'            # listed in BAY-AREA-HIKES.md by scripts/make_index.py
OSM_BBOX=(37.150,-121.905,37.215,-121.800)
TILES=dict(z=16,bbox=(37.166,-121.860,37.190,-121.814))
JUNCTIONS=dict(start=(37.17397,-121.82507,['Mine Hill Trail']),      # Hacienda entrance
  dgtop=(37.17609,-121.83703,['Deep Gulch Trail']),                # top of Deep Gulch
  camp=(37.17887,-121.84016,['English Camp Trail']),               # English Camp
  ecj=(37.18053,-121.84071,['Castillero Trail']),                  # Mine Hill Trail / Castillero Trail, north of English Camp
  summit=(37.17519,-121.84378,['Castillero Trail']),               # top of Mine Hill: rotary furnace, Spanishtown site
  westj=(37.18018,-121.85263,['Castillero Trail']),                # Castillero Trail rejoins Mine Hill Trail (Bull Run)
  sancris=(37.17831,-121.84707,['Mine Hill Trail']),               # San Cristobal Mine
  april=(37.18123,-121.84622,['April Trail']),                     # April Tunnel trestle (April Trail loop off the Mine Hill Trail)
  capehorn=(37.18293,-121.83263,['Mine Hill Trail']))              # Capehorn Pass
ROUTES={'main':['start','dgtop','camp','summit','westj','sancris','april','ecj','capehorn','start']}   # up the gulch, down the mine road
MAIN='main';GPX={'main':'Almaden Quicksilver: Mine Hill history loop from the Hacienda entrance'}
MK=[('start',1),('dgtop',2),('camp',3),('summit',4),('westj',5),('sancris',6),('april',7),('capehorn',8)]
MAP=dict(pad=230,aspect=1.75,extent=['main'],overlays=[],markers=MK,icons=[],k=1.4,scale=(500,'500 m'),arrow_start=500,arrow_step=560,arrow_clear=140,
  labels=[dict(at='start',dx=0,dy=48,text='START / FINISH',anchor='middle',size=21,weight=700),
          dict(at='start',dx=0,dy=72,text='Hacienda entrance',anchor='middle',size=19),
          dict(at='dgtop',dx=0,dy=44,text='top of Deep Gulch',anchor='middle',size=18),
          dict(at='camp',dx=28,dy=-14,text='English Camp',size=20,weight=700),
          dict(at='summit',dx=0,dy=46,text='rotary furnace',anchor='middle',size=20,weight=700),
          dict(at='westj',dx=-28,dy=8,text='Bull Run',anchor='end',size=20,weight=700),
          dict(at='sancris',dx=-26,dy=30,text='San Cristobal Mine',anchor='end',size=20,weight=700),
          dict(at='april',dx=0,dy=-30,text='April trestle',anchor='middle',size=20,weight=700),
          dict(at='capehorn',dx=28,dy=-10,text='Capehorn Pass',size=20,weight=700),
          dict(at=(37.1827,-121.83781),dx=0,dy=-18,text='Day Tunnel',anchor='middle',size=18),
          dict(at=(37.17439,-121.84265),dx=10,dy=34,text='Spanishtown site',size=18),
          dict(at=(37.17842,-121.81954),dx=0,dy=-18,text='Museum (Casa Grande)',anchor='middle',size=18)])
PROFILE=dict(emin=100,emax=550,grid=50,label_every=100,height=300,km_step=1,
  markers=[('start',1,12),('dgtop',2,0),('camp',3,0),('summit',4,0),('westj',5,0),('sancris',6,0),('april',7,0),('capehorn',8,0),('start_end',1,0)],
  notes=[(4850,165,'up Deep Gulch in shade  ·  over the top  ·  down the old mine road in the sun')])
ACCESS=dict(**{'from':(37.2553,-121.8760),'to':(37.17420,-121.82473)},z=14,bbox=(37.155,-121.92,37.275,-121.78),pad=(420,420,200,260),k=2.0,mk=1.15,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',150),label='Highway 85',dx=56,dy=16,size=46),
           dict(letter='B',at=('name','Almaden Road'),label='Almaden Road',dx=56,dy=16,size=46),
           dict(letter='P',at=('end',),label='Hacienda entrance',dx=-56,dy=16,anchor='end',size=46,weight=700,fill='RED')],
  places=[dict(at=(37.17842,-121.81954),label='Museum',dx=34,dy=-6,size=40)])
EZ='Eugene Zelenko'
PHOTOS=dict(
 hero=dict(file='File:USA-San Jose-Almaden Quicksilver Park-Rotary Furnace-5.jpg',short='Rotary furnace',cls='tri',
   caption='The rotary furnace on Mine Hill, last fired in the 1970s.'),
 camp=dict(file='File:USA-San Jose-Almaden Quicksilver Park-English Camp-3.jpg',short='English Camp',cls='hero',crop=(0,0.10,1,0.88),
   caption='English Camp, where about a thousand people lived in the 1880s. By 1909 it was empty.'),
 sancris=dict(file='File:USA-San Jose-Almaden Quicksilver Park-San Cristobal Mine.jpg',short='San Cristobal',cls='tri',crop=(0,0.08,1,0.62),
   caption='The San Cristobal tunnel, opened in 1866, the one working you can still step into.'),
 trestle=dict(file='File:USA-San Jose-Almaden Quicksilver Park-April Tunnel.jpg',short='April trestle',cls='tri',
   caption='What is left of the ore-car trestle outside the April Tunnel.'),
 town=dict(file='File:The Town at the Mine, New Almaden. (6131063220).jpg',short='Town at the mine, c. 1867',cls='duo',crop=(0.075,0.06,0.495,0.86),
   caption='“The Town at the Mine”, photographed by Carleton Watkins about 1867 (DeGolyer Library, SMU).'),
 valley=dict(file='File:USA-San Jose-Almaden Quicksilver Park-Mine Hill Trail-1.jpg',short='Mine Hill Trail',cls='duo',crop=(0,0.10,1,0.85),
   caption='Coming down the Mine Hill Trail: the Santa Clara Valley, which the mine’s money helped build.'),
 casa=dict(file='File:Casa Grande 11 (8400595006).jpg',short='Casa Grande',cls='duo',
   caption='Casa Grande, the mine manager’s house of 1854, now the mining museum.'),
)
