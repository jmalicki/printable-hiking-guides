"""Trinity Alps: the Four Lakes Loop round Siligo Peak, walked in from Long Canyon (main) or Stoney Ridge (alternative)."""
PDF='trinity-alps-four-lakes-loop.pdf'
OSM_BBOX=(40.875,-122.92,40.962,-122.80)
TILES=dict(z=14,bbox=OSM_BBOX)
DETAIL_TILES=dict(z=16,bbox=(40.9370,-122.915,40.959,-122.882))    # close-up of the loop
JUNCTIONS=dict(canyon=93880571,                  # Long Canyon trailhead
               meadow=(40.93637,-122.8631),      # upper Long Canyon meadows
               ridge=8927803839,                 # Stoney Ridge trailhead
               stone=(40.91294,-122.88957),      # Stonewall Pass
               little=(40.92716,-122.88496),     # Little Stonewall Pass
               gate=5705632247,                  # Deer Creek Pass: both approaches meet, loop starts and ends
               fork=5705632261,                  # Deer Creek Trail / Four Lakes Loop Trail, just below the pass
               spur=8910229438,                  # Summit Lake Trail leaves the loop
               summit=8910229449,                # Summit Lake shore
               diamond=(40.943618,-122.905034),  # Diamond Lake
               luella=(40.952217,-122.9021074),  # Luella Lake
               bottom=8927803473,                # Deer Creek: loop trail meets Deer Creek Trail (low point)
               deer=(40.94486,-122.89338))       # Deer Lake
LOOP=['gate','fork','spur','summit','spur','diamond','luella','bottom','deer','fork','gate']   # clockwise
ROUTES={'long-canyon':['canyon','meadow']+LOOP+['meadow','canyon'],
        'stoney-ridge':['ridge','stone','little']+LOOP+['little','stone','ridge']}
MAIN='long-canyon'
GPX={'long-canyon':'Four Lakes Loop (clockwise) from Long Canyon','stoney-ridge':'Four Lakes Loop (clockwise) from Stoney Ridge'}
# numbers = main route and loop; letters = Stoney Ridge approach
MK=[('canyon',1),('meadow',2),('gate',3),('summit',4),('diamond',5),('luella',6),('bottom',7),('deer',8)]
SR=[('ridge','A'),('stone','B'),('little','C')]
MAP=dict(bbox=(40.875,-122.926,40.963,-122.799),icons=[],k=1.5,scale=(2000,'2 km'),
  overlays=[dict(route='stoney-ridge',frm='ridge',to='gate',color='BLUE',width=11,dash='20 11')],
  markers=[m for m in MK if m[0] in('canyon','meadow','gate')]+SR,
  arrow_start=1500,arrow_step=1900,arrow_end=8600,arrow_clear=500,
  labels=[dict(at='canyon',dx=0,dy=40,text='Long Canyon trailhead',anchor='end',size=19,weight=700),
          dict(at='meadow',dx=24,dy=-12,text='Long Canyon meadows',size=18),
          dict(at='gate',dx=28,dy=-14,text='Deer Creek Pass',size=19,weight=700),
          dict(at='ridge',dx=26,dy=8,text='Stoney Ridge trailhead',size=19,weight=700,color='BLUE'),
          dict(at='stone',dx=26,dy=7,text='Stonewall Pass',size=18,color='BLUE'),
          dict(at='little',dx=26,dy=7,text='Little Stonewall Pass',size=18,color='BLUE'),
          dict(at=(40.9585,-122.9090),dx=0,dy=0,text='the loop: see page 3',anchor='start',size=18,weight=700,color='RED'),
          dict(at=(40.9200,-122.8990),dx=0,dy=0,text='Van Matre Meadows',anchor='end',size=16),
          dict(at=(40.9300,-122.8845),dx=0,dy=0,text='Siligo Meadows',size=16)])
DETAIL=dict(bbox=(40.9378,-122.9139,40.9579,-122.8848),overlays=[],icons=[],k=1.6,scale=(500,'500 m'),
  markers=[m for m in MK if m[0] not in('canyon','meadow')],
  arrow_start=9300,arrow_step=640,arrow_end=20100,arrow_clear=150,
  labels=[dict(at='gate',dx=0,dy=44,text='Deer Creek Pass',anchor='middle',size=20,weight=700),
          dict(at='summit',dx=-26,dy=8,text='Summit Lake',anchor='end',size=20,weight=700),
          dict(at='diamond',dx=-26,dy=8,text='Diamond Lake',anchor='end',size=20,weight=700),
          dict(at='luella',dx=-10,dy=-30,text='Luella Lake',anchor='end',size=20,weight=700),
          dict(at='bottom',dx=26,dy=8,text='Deer Creek',size=20,weight=700),
          dict(at='deer',dx=26,dy=8,text='Deer Lake',size=20,weight=700),
          dict(at=(40.9470,-122.8990),dx=0,dy=0,text='Siligo Peak',anchor='middle',size=18),
          dict(at=(40.94205,-122.8945),dx=0,dy=-16,text='snow lingers here',anchor='middle',size=17,color='RED',weight=700)])
def _pf(markers,notes=[]):
    return dict(emin=1000,emax=2600,grid=200,label_every=400,height=270,km_step=5,markers=markers,notes=notes)
PROFILE=_pf([('canyon',1,12),('meadow',2,0),('gate',3,-8),('summit',4,6),('diamond',5,4),('luella',6,0),('bottom',7,0),('deer',8,-4),('gate_end',3,8),('canyon_end',1,0)],
            notes=[(6600,1220,'up Long Canyon: +1,260 m'),(14600,1220,'the loop: 11.3 km, +690 m'),(23000,1220,'back down Long Canyon')])
PROFILES={'stoney-ridge':_pf([('ridge','A',12),('stone','B',-4),('little','C',0),('gate',3,-4),('summit',4,8),('diamond',5,4),('luella',6,0),('bottom',7,0),('deer',8,-4),('gate_end',3,6),('little_end','C',4),('stone_end','B',4),('ridge_end','A',0)],
            notes=[(7500,1250,'57 switchbacks to B'),(17700,1220,'the loop: 11.3 km, +690 m'),(30500,1220,'two passes to re-cross')])}
W_=(40.730953,-122.942188)
ACCESS=dict(**{'from':W_,'to':(40.92306,-122.81366)},z=13,bbox=(40.70,-122.99,40.96,-122.73),pad=(330,230,150,225),k=1.6,mk=1.1,scale=(2000,'2 km'),
  extra=[{'from':W_,'to':(40.88207,-122.87536),'color':'INK'}],
  markers=[dict(letter='W',at=('at',W_),label='Weaverville',dx=52,dy=14,size=40),
           dict(letter='S',at=('at',(40.849859,-122.856151)),label='Stoney Ridge turn-off',dx=44,dy=30,size=40),
           dict(letter='A',at=('at',(40.88207,-122.87536)),label='Stoney Ridge trailhead',dx=-44,dy=-22,anchor='end',size=40,weight=700,fill='BLUE'),
           dict(letter='L',at=('at',(40.915997,-122.770647)),label='Long Canyon Road',dx=-6,dy=-52,anchor='middle',size=40),
           dict(letter='1',at=('end',),label='Long Canyon trailhead',dx=-44,dy=-14,anchor='end',size=40,weight=700,fill='RED')],
  places=[dict(at=(40.800,-122.775),label='Trinity Lake',dot=False,size=40,weight=500,anchor='middle')])
TH='Tom Hilton (Flickr)'
PHOTOS=dict(
 diamond=dict(file='File:Diamond Lake, Sawtooth Mountain.jpg',short='Diamond Lake',cls='cover',crop=(0,0.04,1,0.94),
   caption='Diamond Lake on its shelf, with Sawtooth Mountain across the Stuart Fork: the view you walk into when you go round clockwise.'),
 summit=dict(short='Summit Lake',cls='tri',url='https://live.staticflickr.com/3468/3703697127_da6621a3e3_b.jpg',artist=TH,license='CC BY 2.0',page='https://www.flickr.com/photos/tomhilton/3703697127/',
   caption='Summit Lake, the largest of the four, in its bowl of red rock.'),
 luella=dict(short='Luella Lake',cls='tri',url='https://live.staticflickr.com/3450/3701611342_f5657d2687_b.jpg',artist=TH,license='CC BY 2.0',page='https://www.flickr.com/photos/tomhilton/3701611342/',
   caption='Luella Lake from the switchbacks above it, early July.'),
 deer=dict(file='File:Trinity Alps Deer Lake.jpg',short='Deer Lake',cls='tri',
   caption='Deer Lake on 26 June 2024, with snow still across the traverse above it.'),
 redwhite=dict(short='Red and white rock',cls='duo',url='https://live.staticflickr.com/65535/54364584195_3444eeecc6_b.jpg',artist='AditiStargazer (Flickr)',license='CC BY-NC-SA 2.0',page='https://www.flickr.com/photos/aditithestargazer/54364584195/',
   caption='Red Seven Up Peak, grey Gibson Peak and Luella Lake under early-season snow.'),
)
