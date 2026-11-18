"""Shared helpers: load a guide config, build the trail graph, route between junctions, project to map pixels."""
import json,math,heapq,collections,importlib.util,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_config(slug):
    spec=importlib.util.spec_from_file_location('cfg',os.path.join(ROOT,'guides',slug,'config.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.SLUG=slug
    m.DATA=os.path.join(ROOT,'data',slug);m.OUT=os.path.join(ROOT,'out',slug);m.DIR=os.path.join(ROOT,'guides',slug)
    os.makedirs(m.DATA,exist_ok=True);os.makedirs(m.OUT,exist_ok=True)
    return m
def slug_arg():
    if len(sys.argv)<2:sys.exit('usage: %s <guide-slug>   (a folder name under guides/)'%sys.argv[0])
    return sys.argv[1]
def hav(a,b):
    R=6371000;p1,p2=math.radians(a[0]),math.radians(b[0])
    x=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(x))
class Graph:
    def __init__(s,path):
        s.pos={};s.adj=collections.defaultdict(list)
        for e in json.load(open(path))['elements']:
            if e['type']!='way':continue
            t=e['tags'];nm=t.get('name') or ('('+t['highway']+')')
            ns=e['nodes']
            for n,p in zip(ns,e['geometry']):s.pos[n]=(p['lat'],p['lon'])
            for a,b in zip(ns,ns[1:]):
                w=hav(s.pos[a],s.pos[b]);s.adj[a].append((b,w,nm,t['highway']));s.adj[b].append((a,w,nm,t['highway']))
    def nearest(s,pt,names=None):
        best=None
        for n,p in s.pos.items():
            if names and not any(x[2] in names for x in s.adj[n]):continue
            d=hav(pt,p)
            if best is None or d<best[0]:best=(d,n)
        return best[1]
    def resolve(s,spec):
        """spec: OSM node id | (lat,lon) | (lat,lon,[way names the node must touch])"""
        if isinstance(spec,int):return spec
        return s.nearest(spec[:2],set(spec[2]) if len(spec)>2 else None)
    def path(s,a,b,allow=None):
        dist={a:0};prev={};pq=[(0,a)]
        while pq:
            d,u=heapq.heappop(pq)
            if u==b:break
            if d>dist[u]:continue
            for v,w,nm,hw in s.adj[u]:
                if allow and nm not in allow:continue
                c=d+w*(5 if hw in('secondary','tertiary') else 1)   # prefer trails over roads
                if c<dist.get(v,1e18):dist[v]=c;prev[v]=(u,nm,w);heapq.heappush(pq,(c,v))
        out=[];u=b
        while u!=a:
            p=prev[u];out.append((u,p[1],p[2]));u=p[0]
        return out[::-1]
class Proj:
    """Web-Mercator pixel projection onto a stitched basemap (see fetch.py)."""
    def __init__(s,meta):s.z=meta['z'];s.x0=meta['x0'];s.y0=meta['y0'];s.w=meta['w'];s.h=meta['h']
    def px(s,lat,lon):
        x=(lon+180)/360*2**s.z;r=math.radians(lat)
        y=(1-math.log(math.tan(r)+1/math.cos(r))/math.pi)/2*2**s.z
        return (x-s.x0)*256,(y-s.y0)*256
    def mpp(s,lat):return 156543.03392*math.cos(math.radians(lat))/2**s.z
