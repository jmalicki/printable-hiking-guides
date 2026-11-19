"""Russian Ridge: Borel Hill, the Ridge Trail, Hawk Ridge, Alder Spring and the Ancient Oaks, from the Alpine Road car park."""
PDF='russian-ridge-borel-hill-ancient-oaks.pdf'
OSM_BBOX=(37.295,-122.235,37.345,-122.170)
TILES=dict(z=16,bbox=(37.300,-122.225,37.340,-122.180))
JUNCTIONS=dict(start=(37.31496,-122.18853),            # main car park, corner of Alpine Road and Skyline Boulevard
               borel=(37.3199742,-122.1996674),        # Borel Hill summit
               vista=65389928,                         # Ridge Trail meets the Charquin Trail by the Skyline vista point
               hawk=462088399,                         # north end: Hawk Ridge Trail leaves the Ridge Trail
               alder=462087000,                        # Hawk Ridge Trail ends on the Alder Spring Trail
               charq=462099401,                        # Alder Spring Trail ends on the Charquin Trail
               oaks=462135505,                         # Ancient Oaks Trail leaves the Charquin Trail
               gimbal=462085391,                       # Bo Gimbal Trail comes down to the Ancient Oaks Trail
               oaks_e=462086337,                       # east end of the Ancient Oaks Trail
               gimbal_top=462086201)                   # Bo Gimbal Trail leaves the Ridge Trail below Borel Hill
ROUTES={'main':['start','borel','vista','hawk','alder','charq','oaks','gimbal','oaks_e','start'],
        'short':['start','borel','gimbal_top','gimbal','oaks_e','start']}
MAIN='main';GPX={'main':'Russian Ridge: Borel Hill, Ridge Trail, Hawk Ridge, Alder Spring and Ancient Oaks loop',
                 'short':'Russian Ridge short loop: Borel Hill, Bo Gimbal and Ancient Oaks'}
MK=[('start',1),('borel',2),('vista',3),('hawk',4),('alder',5),('charq',6),('oaks',7),('gimbal',8)]
MAP=dict(pad=150,aspect=1.97,extent=['main'],icons=[],k=1.3,scale=(500,'500 m'),
  overlays=[dict(route='short',frm='gimbal_top',to='gimbal',color='BLUE',width=7,dash='14 9')],
  markers=MK,arrow_start=500,arrow_step=560,arrow_clear=170,
  labels=[dict(at='start',dx=-24,dy=30,text='START / FINISH',anchor='end',size=19,weight=700),
          dict(at=(37.3133,-122.1884),dx=16,dy=6,text='Alpine Pond',size=16),
          dict(at='borel',dx=22,dy=-14,text='Borel Hill',size=19,weight=700),
          dict(at='vista',dx=22,dy=-14,text='Skyline gate',size=16),
          dict(at='hawk',dx=0,dy=-26,text='Hawk Ridge Trail',anchor='middle',size=17),
          dict(at='alder',dx=-22,dy=26,text='Alder Spring Trail',anchor='end',size=17),
          dict(at='charq',dx=-22,dy=7,text='Charquin Trail',anchor='end',size=17),
          dict(at='oaks',dx=-22,dy=7,text='Ancient Oaks Trail',anchor='end',size=19,weight=700),
          dict(at='gimbal',dx=-6,dy=38,text='Bo Gimbal short cut',anchor='middle',size=16,color='BLUE',weight=700)])
PROFILE=dict(emin=500,emax=850,grid=50,label_every=100,height=210,km_step=1,
  markers=[('start',1,14),('borel',2,0),('vista',3,0),('hawk',4,0),('alder',5,0),('charq',6,0),('oaks',7,0),('gimbal',8,0),('start_end',1,0)],
  notes=[(800,555,'{{u:100 m|320 ft}} up through the grass'),(2750,555,'along the open crest'),(5950,555,'75 m up among the oaks'),(7400,555,'downhill home')])
ACCESS=dict(**{'from':(37.3878,-122.1639),'to':(37.31496,-122.18853)},z=14,bbox=(37.300,-122.215,37.400,-122.135),pad=(430,330,110,120),k=1.8,scale=(2000,'2 km'),
  markers=[dict(letter='A',at=('m',0),label='I-280, exit 20',dx=-52,dy=14,anchor='end'),
           dict(letter='P',at=('end',),label='Russian Ridge',dx=52,dy=14,size=40,weight=700,fill='RED')],
  places=[dict(at=(37.3150,-122.1880),label='Skyline Blvd (Hwy 35)',dx=40,dy=-70,size=30,dot=False),
          dict(at=(37.3560,-122.1760),label='Page Mill Road',dx=40,dy=0,size=30,dot=False)])
# Photos: Wikimedia Commons, plus one Flickr photo (licence read on its page, Nov 2026). Species photos were mostly taken elsewhere; captions say where it matters.
PHOTOS=dict(
 hero=dict(short='Cover',cls='hero',file='File:Russian Ridge-Wildflowers.jpg',crop=(0,0,1,0.66),
   caption='Russian Ridge in spring: lupine and poppies down the slope, forest in the folds, the next ridges going blue towards the ocean.'),
 poppy=dict(short='Poppy',cls='bio',file='File:1 California poppy.jpg',caption=''),
 lupine=dict(short='Lupine',cls='bio',file='File:Fabaceae lupinus nanus sky lupine.jpg',caption=''),
 owl=dict(short='Owl&#8217;s clover',cls='bio',file='File:Orobanchaceae Castilleja exserta Pink Owls clover.jpg',caption=''),
 tidy=dict(short='Tidy tips',cls='bio',file='File:Tidy Tips (Layia platyglossa) (7060913097).jpg',caption=''),
 checker=dict(short='Checkerbloom',cls='bio',file='File:Sidalcea malviflora ssp malviflora 3.jpg',caption=''),
 violet=dict(short='Golden violet',cls='bio',file='File:JOHNNY JUMP-UP (viola pedunculata) (4-13-07) -canet (535408937).jpg',caption=''),
 blue=dict(short='Blue-eyed grass',cls='bio',file='File:Blue Eyed Grass, Bay Area.jpg',caption=''),
 clarkia=dict(short='Clarkia',cls='bio',file='File:Ruby chalice clarkia (Clarkia rubicunda) (7778062648).jpg',caption=''),
 newt=dict(short='California newt',cls='bio',file='File:Taricha torosa, Napa County, CA.jpg',caption='California newt (Napa County).'),
 rough=dict(short='Rough-skinned newt',cls='bio',file='File:Roughed Skinned Newt (16744025149).jpg',caption='Rough-skinned newt: dark under the eye.'),
 belly=dict(short='Newt, underside',cls='bio',file='File:California Newt (Taricha torosa) (4415749606).jpg',caption='The warning colour is underneath.'),
 ensatina=dict(short='Ensatina',cls='bio',file='File:Yellow-eyed Ensatina (Ensatina eschscholtzii xanthoptica).jpg',caption='Yellow-eyed ensatina.'),
 slender=dict(short='Slender salamander',cls='bio',file='File:Batrachoseps attenuatus California slender salamander - 5624597387.jpg',caption='California slender salamander.'),
 arboreal=dict(short='Arboreal salamander',cls='bio',file='File:Aneides lugubris - Arboreal Salamander 05.jpg',caption='Arboreal salamander.'),
 garter=dict(short='Garter snake',cls='bio',file='File:Thamnophis sirtalis tetrataenia (2005 10 16) - uitsnede.jpg',caption='San Francisco garter snake (captive).'),
 oaks=dict(short='Ancient oaks',cls='bio',url='https://live.staticflickr.com/8621/15887249468_676aff9d67_b.jpg',artist='bgwashburn (Flickr)',license='CC BY 2.0',page='https://www.flickr.com/photos/bgwashburn/15887249468/',
   caption='On the Ancient Oaks Trail.'),
 grass=dict(short='Ridge',cls='bio',file='File:Russian Ridge Open Space.jpg',caption='Grass above, forest below.'),
 badger=dict(short='Badger',cls='bio',file='File:Taxidea taxus (Point Reyes, 2007).jpg',caption='American badger (Point Reyes).'),
 coyote=dict(short='Coyote',cls='bio',file='File:Alert Coyote (39381073180).jpg',crop=(0,0.25,0.75,1),caption='Coyote, photographed in this preserve.'),
 kestrel=dict(short='Kestrel',cls='bio',file='File:Hovering Kestrel (8625537353).jpg',crop=(0.3,0.1,1,0.9),caption='American kestrel, hovering.'),
 bunting=dict(short='Lazuli bunting',cls='bio',file="File:Lazuli Bunting (male) Bob Rodrigues's Yard Portal AZ 2018-05-10 08-10-58 (29961352838).jpg",caption='Male lazuli bunting (Arizona).'),
 checkerspot=dict(short='Checkerspot',cls='bio',file='File:Variable Checkerspot (Euphydryas chalcedona).jpg',caption='Variable checkerspot.'),
 lizard=dict(short='Fence lizard',cls='bio',file='File:Sceloporus occidentalis, Sacramento County, California.jpg',caption='Western fence lizard.'),
)
