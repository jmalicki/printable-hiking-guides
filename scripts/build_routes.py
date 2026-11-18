"""Compute the two routes from OSM data, sample elevation, write GeoJSON-ish JSON + GPX.
Usage: python3 scripts/build_routes.py   (run from repo root)"""
import sys,json,os,time,urllib.request,bisect
sys.argv=[sys.argv[0],'data/osm-trails.json']
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from route import pos,adj,nearest,dijk,hav

start=nearest((37.91020,-122.57721))
cvb=nearest((37.8937516,-122.5741258),{'Canopy View Trail'})
vc=nearest((37.8927962,-122.5724843),{'Redwood Creek Trail','Bohemian Grove Trail','(footway)'})
J=dict(start=start,t80=313621042,vw=511981002,bj=261758361,fc=261758332,lostfc=361153027,
       lostcv=354582989,cvtop=361152366,cvb=cvb,vc=vc)
# Direction: clockwise. Down Canopy View (even grade), up Bootjack (steps are kinder to climb than descend).
ROUTES={
 'main':  ['start','cvtop','lostcv','cvb','fc','bj','vw','t80','start'],
 'short': ['start','cvtop','lostcv','cvb','fc','lostfc','lostcv','cvtop','start'],
 'vc_spur':['cvb','vc'],
}
def build(stops):
    nodes=[J[stops[0]]];marks={stops[0]:0.0};d=0.0;cum=[0.0]
    for a,b in zip(stops,stops[1:]):
        for n,nm,w in dijk(J[a],J[b]):
            d+=w;nodes.append(n);cum.append(d)
        marks.setdefault(b+('' if b not in marks else '_end'),d)
    return nodes,cum,marks

def elevations(pts):
    cache_f='data/elev-cache.json'
    cache=json.load(open(cache_f)) if os.path.exists(cache_f) else {}
    need=[p for p in pts if '%.5f,%.5f'%p not in cache]
    for i in range(0,len(need),100):
        chunk=need[i:i+100]
        url='https://api.opentopodata.org/v1/ned10m?locations='+'|'.join('%.5f,%.5f'%p for p in chunk)
        req=urllib.request.Request(url,headers={'User-Agent':'trail-map-script/1.0'})
        r=json.load(urllib.request.urlopen(req,timeout=60))
        for p,res in zip(chunk,r['results']):cache['%.5f,%.5f'%p]=res['elevation']
        json.dump(cache,open(cache_f,'w'));time.sleep(1.2)
    return [cache['%.5f,%.5f'%p] for p in pts]

out={}
for name,stops in ROUTES.items():
    nodes,cum,marks=build(stops)
    coords=[pos[n] for n in nodes]
    ele=elevations(coords)
    # light smoothing (5-pt moving average) to tame DEM noise under forest
    sm=[sum(ele[max(0,i-2):i+3])/len(ele[max(0,i-2):i+3]) for i in range(len(ele))]
    gain=sum(max(0,b-a) for a,b in zip(sm,sm[1:]));loss=sum(max(0,a-b) for a,b in zip(sm,sm[1:]))
    out[name]=dict(coords=coords,cum=cum,ele=sm,marks=marks,length_m=cum[-1],gain_m=gain,loss_m=loss,
                   min_ele=min(sm),max_ele=max(sm))
    print(name,'%.2f km %.2f mi'%(cum[-1]/1000,cum[-1]/1609.34),'gain %d m loss %d m'%(gain,loss),
          'ele %d-%d'%(min(sm),max(sm)),len(coords),'pts')
    for k,v in marks.items():print('   %-12s %.2f km  %.2f mi  ele %d m'%(k,v/1000,v/1609.34,sm[bisect.bisect_left(cum,v)]))
json.dump(out,open('data/routes.json','w'))
json.dump({k:pos[v] for k,v in J.items()},open('data/junctions.json','w'),indent=1)

TITLES={'main':'Mountain Home to Muir Woods - down Canopy View, back up Bootjack and Troop 80',
        'short':'Mountain Home to Muir Woods - short version, back up Fern Creek and Lost Trail'}
for name in('main','short'):
    r=out[name]
    with open('out/muir-woods-%s.gpx'%name,'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="muir-woods-hike" xmlns="http://www.topografix.com/GPX/1/1">\n')
        f.write(' <trk><name>%s</name><trkseg>\n'%TITLES[name])
        for (la,lo),e in zip(r['coords'],r['ele']):f.write('  <trkpt lat="%.6f" lon="%.6f"><ele>%.1f</ele></trkpt>\n'%(la,lo,e))
        f.write(' </trkseg></trk>\n</gpx>\n')
