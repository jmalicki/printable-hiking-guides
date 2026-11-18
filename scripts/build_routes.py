"""Compute a guide's routes from its OSM data, sample elevation, write routes.json + GPX.
usage: build_routes.py <slug>"""
import json,os,time,urllib.request,bisect
from hikelib import load_config,slug_arg,Graph,ROOT
C=load_config(slug_arg());G=Graph(C.DATA+'/osm.json')
J={k:G.resolve(v) for k,v in C.JUNCTIONS.items()}
def build(stops):
    nodes=[J[stops[0]]];marks={stops[0]:0.0};d=0.0;cum=[0.0]
    for a,b in zip(stops,stops[1:]):
        for n,nm,w in G.path(J[a],J[b],C.LEG_ALLOW.get((a,b)) if hasattr(C,'LEG_ALLOW') else None):
            d+=w;nodes.append(n);cum.append(d)
        marks.setdefault(b if b not in marks else b+'_end',d)
    return nodes,cum,marks
def elevations(pts):
    f=os.path.join(ROOT,'data','elev-cache.json');cache=json.load(open(f)) if os.path.exists(f) else {}
    key=lambda p:'%.5f,%.5f'%p;need=[p for p in pts if key(p) not in cache]
    for i in range(0,len(need),100):
        ch=need[i:i+100]
        u='https://api.opentopodata.org/v1/ned10m?locations='+'|'.join(key(p) for p in ch)
        r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'trail-map-script/1.0'}),timeout=60))
        for p,res in zip(ch,r['results']):cache[key(p)]=res['elevation']
        json.dump(cache,open(f,'w'));time.sleep(1.2)
    return [cache[key(p)] for p in pts]
out={}
for name,stops in C.ROUTES.items():
    nodes,cum,marks=build(stops);coords=[G.pos[n] for n in nodes];ele=elevations(coords)
    sm=[sum(ele[max(0,i-2):i+3])/len(ele[max(0,i-2):i+3]) for i in range(len(ele))]   # tame DEM noise
    gain=sum(max(0,b-a) for a,b in zip(sm,sm[1:]))
    out[name]=dict(coords=coords,cum=cum,ele=sm,marks=marks,length_m=cum[-1],gain_m=gain,min_ele=min(sm),max_ele=max(sm))
    print(name,'%.2f km %.2f mi'%(cum[-1]/1000,cum[-1]/1609.34),'gain ~%d m'%gain,'ele %d-%d'%(min(sm),max(sm)))
    for k,v in marks.items():print('   %-12s %.2f km  %.2f mi  ele %d m'%(k,v/1000,v/1609.34,sm[bisect.bisect_left(cum,v)]))
    # per-leg trail names, to sanity-check the route follows what the text says
    seq=[]
    for a,b in zip(stops,stops[1:]):
        for n,nm,w in G.path(J[a],J[b],C.LEG_ALLOW.get((a,b)) if hasattr(C,'LEG_ALLOW') else None):
            if seq and seq[-1][0]==nm:seq[-1][1]+=w
            else:seq.append([nm,w])
    print('   via: '+' > '.join('%s %dm'%(n,w) for n,w in seq if w>25))
json.dump(out,open(C.DATA+'/routes.json','w'));json.dump({k:G.pos[v] for k,v in J.items()},open(C.DATA+'/junctions.json','w'),indent=1)
for name,title in C.GPX.items():
    r=out[name]
    with open('%s/%s-%s.gpx'%(C.OUT,C.SLUG,name),'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="hike-guides" xmlns="http://www.topografix.com/GPX/1/1">\n <trk><name>%s</name><trkseg>\n'%title)
        for (la,lo),e in zip(r['coords'],r['ele']):f.write('  <trkpt lat="%.6f" lon="%.6f"><ele>%.1f</ele></trkpt>\n'%(la,lo,e))
        f.write(' </trkseg></trk>\n</gpx>\n')
