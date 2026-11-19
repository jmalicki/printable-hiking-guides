"""Murietta Falls from Del Valle: the eastern end of the Ohlone Wilderness Trail, out and back
(Lichen Bark picnic area -> sign-in panel -> Rocky Ridge -> Williams Gulch -> Big Burn -> Schlieper Rock -> Johnny's Pond -> falls)."""
PDF='ohlone-murietta-falls.pdf'
OSM_BBOX=(37.520,-121.745,37.600,-121.640)
TILES=dict(z=16,bbox=(37.524,-121.735,37.586,-121.675))
JUNCTIONS=dict(start=5387382499,panel=1801301067,boyd=1801298931,crest=52981416,wg=6538035424,schl=6538035405,
               pond=52984905,turn=52994285,falls=1711727465)
ROUTES={'main':['start','panel','boyd','crest','wg','schl','pond','turn','falls','turn','pond','schl','wg','crest','boyd','panel','start']}
GPX={'main':'Murietta Falls from Del Valle (Ohlone Wilderness Trail), out and back'}
MAIN='main'
MAP=dict(pad=230,aspect=0.62,extent=['main'],overlays=[],k=1.9,scale=(1000,'1 km'),
  arrow_start=700,arrow_end=9500,arrow_step=900,arrow_clear=260,
  markers=[('start',1),('panel',2),('crest',3),('wg',4),('schl',5),('pond',6),('turn',7),('falls',8)],
  labels=[dict(at='start',dx=-30,dy=-34,text='START / FINISH',anchor='end',size=21,weight=700),
          dict(at='start',dx=-30,dy=-10,text='Lichen Bark car park',anchor='end',size=20),
          dict(at='panel',dx=-30,dy=8,text='Sign-in panel',anchor='end',size=20),
          dict(at='boyd',dx=-22,dy=6,text='Boyd Camp',anchor='end',size=19),
          dict(at='crest',dx=30,dy=8,text='Rocky Ridge',size=21,weight=700),
          dict(at='wg',dx=30,dy=20,text='Williams Gulch',size=21,weight=700),
          dict(at=(37.5490,-121.7068),dx=0,dy=40,text='Big Burn',anchor='middle',size=20),
          dict(at='schl',dx=30,dy=8,text='Schlieper Rock',size=20),
          dict(at='pond',dx=30,dy=8,text='Johnny&#8217;s Pond',size=20),
          dict(at='falls',dx=-30,dy=-6,text='MURIETTA FALLS',anchor='end',size=21,weight=700),
          dict(at=(37.5307,-121.7079),dx=22,dy=6,text='Stewart&#8217;s Camp',size=19)],
  icons=[])
PROFILE=dict(emin=200,emax=1100,grid=100,label_every=200,height=270,km_step=2,
  markers=[('start',1,0),('panel',2,0),('crest',3,0),('wg',4,0),('schl',5,0),('pond',6,-12),('turn',7,12),('falls',8,0),
           ('schl_end',5,0),('wg_end',4,0),('crest_end',3,0),('panel_end',2,0),('start_end',1,0)],
  notes=[(3550,240,'Rocky Ridge: 490 m up'),(6900,470,'Big Burn: 370 m up in 2.2 km'),(9850,560,'the falls'),(15200,400,'150 m back up'),(16250,240,'490 m down')])
ACCESS=dict(**{'from':(37.6992,-121.7731),'to':(37.5790,-121.6952)},z=14,bbox=(37.560,-121.815,37.712,-121.655),
  pad=(430,430,150,130),scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',0),label='I-580, exit N. Livermore Ave',dx=52,dy=-8),
           dict(letter='B',at=('name','South Livermore Avenue'),label='Downtown Livermore',dx=52,dy=13),
           dict(letter='C',at=('name','Mines Road'),label='Right on Mines Road',dx=52,dy=-10),
           dict(letter='D',at=('name','Del Valle Road'),label='Straight on: Del Valle Road',dx=52,dy=13),
           dict(letter='P',at=('end',),label='Lichen Bark',dx=-52,dy=30,anchor='end',size=40,weight=700,fill='RED')],
  places=[dict(at=(37.6030,-121.7300),label='Lake Del Valle',anchor='end',dx=-10,dy=-40,size=34,dot=False)])
# Photos: all Flickr, licence read on each photo's page (Nov 2026). The hero is ND: shown whole, never cropped (cls 'nd').
FL='https://live.staticflickr.com/';FP='https://www.flickr.com/photos/'
PHOTOS=dict(
 falls=dict(short='Falls in flow',cls='nd',url=FL+'4031/4302943546_7d1f853f0a_b.jpg',artist='Joe Navratil (Flickr)',license='CC BY-NC-ND 2.0',page=FP+'navratil/4302943546/',
   caption='Murietta Falls running after winter rain. Count on this only within days of a storm.'),
 road=dict(short='Trail',cls='tri',url=FL+'1665/24407350173_9a15ff522c_b.jpg',artist='C N / scorpio-tiger (Flickr)',license='CC BY-SA 2.0',page=FP+'30971561@N08/24407350173/',
   caption='The Ohlone Trail climbing out of Del Valle: a ranch road through brush and green hills.'),
 lake=dict(short='Lake',cls='tri',url=FL+'5184/5765947854_bd98b1040d_b.jpg',artist='David / randomcuriosity (Flickr)',license='CC BY-NC-SA 2.0',page=FP+'81232363@N00/5765947854/',
   caption='Lake Del Valle between its ridges, seen from the trail.'),
 post=dict(short='Trail post',cls='tri',url=FL+'65535/51899195812_64d7a3b527_b.jpg',artist='Bart Teeuwisse (Flickr)',license='CC BY-NC-SA 2.0',page=FP+'44124365893@N01/51899195812/',
   caption='An Ohlone Wilderness Trail marker post, and some of the residents.'),
 oak=dict(short='Ridge',cls='bio',url=FL+'1508/24999123029_54f7a650f4_b.jpg',artist='Kee Yip (Flickr)',license='CC BY-NC-SA 2.0',page=FP+'11249863@N04/24999123029/',
   caption='Oaks and a ranch road on the way to the falls, February 2016.'),
 gulch=dict(short='Williams Gulch',cls='bio',crop=(0,0.20,1,0.74),url=FL+'1458/25034042085_3c778f4b9b_b.jpg',artist='C N / scorpio-tiger (Flickr)',license='CC BY-SA 2.0',page=FP+'30971561@N08/25034042085/',
   caption='The creek in Williams Gulch.'),
 rock=dict(short='Falls, a trickle',cls='bio',crop=(0,0.05,1,0.60),url=FL+'1497/24941073371_374194539a_b.jpg',artist='C N / scorpio-tiger (Flickr)',license='CC BY-SA 2.0',page=FP+'30971561@N08/24941073371/',
   caption='The same falls as a trickle: the more usual sight.'),
 pond=dict(short='Pond',cls='bio',url=FL+'5050/5383173769_1d577aca3b_b.jpg',artist='Joseph Dsilva (Flickr)',license='CC BY-NC-SA 2.0',page=FP+'46645318@N02/5383173769/',
   caption='Johnny&#8217;s Pond.'),
)
