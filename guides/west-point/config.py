"""The balcony of Mount Tam: Rock Spring -> Mountain Theater -> Rock Spring Trail -> West Point Inn -> Nora -> Matt Davis -> Bootjack."""
PDF='mount-tam-west-point-loop.pdf'
OSM_BBOX=(37.895,-122.640,37.932,-122.570)
TILES=dict(z=16,bbox=(37.9030,-122.6200,37.9220,-122.5830))
JUNCTIONS=dict(start=(37.9107739,-122.6126301),theater=351899944,wpi=110379911,nora_top=312919663,
               nora_md=1331416933,md_bj=12823903319,bj_top=1825691355)
ROUTES={'main':['start','theater','wpi','nora_top','nora_md','md_bj','bj_top','start']}
LEG_ALLOW={('theater','wpi'):{'Rock Spring Trail'},('nora_top','nora_md'):{'Nora Trail'},
           ('nora_md','md_bj'):{'Matt Davis Trail'}}
GPX={'main':'Mount Tam: Rock Spring - West Point Inn - Matt Davis - Bootjack loop'}
MAIN='main'
MAP=dict(pad=120,aspect=180/120,extent=['main'],overlays=[],markers=[],labels=[],icons=[])
PROFILE=dict(emin=400,emax=650,grid=50,label_every=50,markers=[],notes=[])
ACCESS=dict(**{'from':(37.8078,-122.4750),'to':(37.9107739,-122.6126301)},z=14,bbox=(37.795,-122.640,37.928,-122.455),
  pad=(300,230,150,110),markers=[],places=[])
