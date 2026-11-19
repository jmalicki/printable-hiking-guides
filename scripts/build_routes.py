"""Compute a guide's routes from its OSM data, sample elevation, write routes.json + GPX.
usage: build_routes.py <slug>"""
import json,os,time,urllib.request,bisect
from hikelib import load_config,slug_arg,Graph,ROOT,hav
C=load_config(slug_arg());G=Graph(C.DATA+'/osm.json')
J={k:G.resolve(v) for k,v in C.JUNCTIONS.items()}
for k,v in getattr(C,'POINTS',{}).items():J[k]=-len(J)-1;G.pos[J[k]]=tuple(v)   # free points (lakes, cols) not on a mapped trail
OFF=json.load(open(C.DATA+'/offtrail.json')) if os.path.exists(C.DATA+'/offtrail.json') else {}
def leg(a,b):
    """-> list of ((lat,lon), way name, metres). Off-trail legs come from dem_route.py (key 'a-b' or reversed 'b-a')."""
    for key,rev in((a+'-'+b,False),(b+'-'+a,True)):
        if key in OFF:
            pts=[tuple(p) for p in OFF[key]];pts=pts[::-1] if rev else pts
            return [(q,'(off-trail)',hav(p,q)) for p,q in zip(pts,pts[1:])]
    return [(G.pos[n],nm,w) for n,nm,w in G.path(J[a],J[b],getattr(C,'LEG_ALLOW',{}).get((a,b)))]
def build(stops):
    coords=[G.pos[J[stops[0]]]];marks={stops[0]:0.0};d=0.0;cum=[0.0];off=[];seq=[]
    for a,b in zip(stops,stops[1:]):
        d0=d
        for p,nm,w in leg(a,b):
            d+=w;coords.append(p);cum.append(d)
            if seq and seq[-1][0]==nm:seq[-1][1]+=w
            else:seq.append([nm,w])
        if (a+'-'+b) in OFF or (b+'-'+a) in OFF:off.append([d0,d])
        marks.setdefault(b if b not in marks else b+'_end',d)
    return coords,cum,marks,off,seq
def elevations(pts):
    if getattr(C, 'ELEVATION_RASTER', False):
        from PIL import Image
        with open(C.DATA + '/elevation.json') as source:
            grid = json.load(source)
        with Image.open(C.DATA + '/elevation.png') as terrain:
            heights = []
            for lat, lon in pts:
                x = (lon - grid['west']) * grid['samples_per_degree']
                y = (grid['north'] - lat) * grid['samples_per_degree']
                if not (0 <= x < terrain.width - 1 and 0 <= y < terrain.height - 1):
                    raise ValueError(f'Track outside elevation raster at {lat}, {lon}')
                i, j = int(x), int(y)
                fx, fy = x - i, y - j
                top = (1-fx)*terrain.getpixel((i,j)) + fx*terrain.getpixel((i+1,j))
                bottom = (1-fx)*terrain.getpixel((i,j+1)) + fx*terrain.getpixel((i+1,j+1))
                heights.append((1-fy)*top + fy*bottom)
        return heights
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
    coords,cum,marks,off,seq=build(stops);ele=elevations(coords)
    sm=[sum(ele[max(0,i-2):i+3])/len(ele[max(0,i-2):i+3]) for i in range(len(ele))]   # tame DEM noise
    gain=sum(max(0,b-a) for a,b in zip(sm,sm[1:]));loss=sum(max(0,a-b) for a,b in zip(sm,sm[1:]))
    out[name]=dict(coords=coords,cum=cum,ele=sm,marks=marks,offtrail=off,length_m=cum[-1],gain_m=gain,loss_m=loss,min_ele=min(sm),max_ele=max(sm))
    print(name,'%.2f km %.2f mi'%(cum[-1]/1000,cum[-1]/1609.34),'gain ~%d m loss ~%d m'%(gain,loss),'ele %d-%d'%(min(sm),max(sm)))
    for k,v in marks.items():print('   %-12s %.2f km  %.2f mi  ele %d m'%(k,v/1000,v/1609.34,sm[bisect.bisect_left(cum,v)]))
    print('   via: '+' > '.join('%s %dm'%(n,w) for n,w in seq if w>25))
json.dump(out,open(C.DATA+'/routes.json','w'));json.dump({k:G.pos[v] for k,v in J.items()},open(C.DATA+'/junctions.json','w'),indent=1)
for name,title in C.GPX.items():
    r=out[name]
    with open('%s/%s-%s.gpx'%(C.OUT,C.SLUG,name),'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<gpx version="1.1" creator="hike-guides" xmlns="http://www.topografix.com/GPX/1/1">\n <trk><name>%s</name><trkseg>\n'%title)
        for (la,lo),e in zip(r['coords'],r['ele']):f.write('  <trkpt lat="%.6f" lon="%.6f"><ele>%.1f</ele></trkpt>\n'%(la,lo,e))
        f.write(' </trkseg></trk>\n</gpx>\n')
