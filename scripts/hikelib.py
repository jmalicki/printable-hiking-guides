"""Shared helpers: load a guide config, build the trail graph, route between junctions, project to map pixels."""
import json,math,heapq,collections,importlib.util,os,sys,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def load_config(slug):
    spec=importlib.util.spec_from_file_location('cfg',os.path.join(ROOT,'guides',slug,'config.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);m.SLUG=slug
    m.DATA=os.path.join(ROOT,'data',slug);m.OUT=os.path.join(ROOT,'out',slug);m.DIR=os.path.join(ROOT,'guides',slug)
    os.makedirs(m.DATA,exist_ok=True);os.makedirs(m.OUT,exist_ok=True)
    suffix=('' if UNITS=='imperial' else '-'+UNITS)+('' if PAPER=='letter' else '-'+PAPER)      # default build keeps the plain name
    m.PDF=m.PDF.replace('.pdf',suffix+'.pdf');m.HTML='guide%s.html'%suffix
    return m
# ---- build-time options: UNITS=imperial|metric, PAPER=letter|a4 (environment variables; see Makefile) ----
UNITS=os.environ.get('UNITS') or 'imperial';PAPER=os.environ.get('PAPER') or 'letter'
assert UNITS in('imperial','metric') and PAPER in('letter','a4'),'UNITS=imperial|metric PAPER=letter|a4'
PAGE_CSS={'a4':'@page { size: A4; margin: 9mm 12mm 8mm; }\nhtml { zoom: .95; }\n:root { --pageh: 291mm; }',      # same working width as Letter, a little more height
          # Letter is 18 mm shorter and 6 mm wider than A4: tighter margins and a slight zoom keep the same page breaks
          'letter':'@page { size: letter; margin: 9mm 12mm 8mm; }\nhtml { zoom: .97; }\n:root { --pageh: 267mm; }\n.page > svg.map { width: 92%; margin: 0 auto; }'}[PAPER]   # full-width maps would grow taller with the wider page
def _num(x):return float(x.replace(',',''))
def feet(m):
    f=m*3.28084;step=10 if abs(f)<300 or abs(f)>=1500 else 50
    return '{:,}'.format(int(round(f/step)*step))
def miles(km,decimal=True):
    mi=km*0.621371;return '%.1f'%mi if (decimal or mi<10) else '%d'%round(mi)
_DUAL=re.compile(r'[+−]?\d[\d,.]*(?:\s?[–→]\s?[+−]?\d[\d,.]*)?[\s\u00a0]?(?:km|m)\s\(([^()]*?\b(?:mi|miles|ft|feet))\)')
_QTY=re.compile(r'(?<![\w.,/:])([+−]?)(\d[\d,]*(?:\.\d+)?)(?:(\s?[–→]\s?)([+−]?)(\d[\d,]*(?:\.\d+)?))?([\s\u00a0]?)(km|m)\b(?![\w²³/])')
_U=re.compile(r'\{\{u:(.*?)\|(.*?)\}\}',re.S)
def _qty(g):
    s1,a,sep,s2,b,sp,unit=g.groups()
    conv=(lambda x:miles(_num(x),'.' in x)) if unit=='km' else (lambda x:feet(_num(x)))
    return s1+conv(a)+((sep+(s2 or '')+conv(b)) if b else '')+(sp or ' ')+('mi' if unit=='km' else 'ft')
# British source spelling -> American, applied with the imperial build (whole words, capitalisation kept)
US_WORDS={'cheque':'check','centre':'center','centres':'centers','metre':'meter','metres':'meters','kilometre':'kilometer','kilometres':'kilometers',
 'litre':'liter','litres':'liters','amphitheatre':'amphitheater','theatre':'theater','colour':'color','colours':'colors','coloured':'colored',
 'favourite':'favorite','neighbours':'neighbors','neighbour':'neighbor','grey':'gray','storey':'story','towards':'toward',
 'autumn':'fall','rubbish':'trash','car park':'parking lot','car parks':'parking lots','mobile signal':'cell signal','taps':'faucets',
 'number-plate':'license-plate','petrol station':'gas station','timetable':'schedule','roadworks':'road work','fuel':'gas','shops':'stores','shop':'store',
 'pitches':'tent sites','waterproof':'rain jacket','headtorch':'headlamp','head torch':'headlamp','recognise':'recognize','anticlockwise':'counterclockwise','sulphide':'sulfide','sulphur':'sulfur','tonnes':'metric tons','specialise':'specialize','trainers':'sneakers','mould':'mold','chequered':'checkered','letterbox':'mail slot','travelled':'traveled','neighbouring':'neighboring','harbour':'harbor','specialises':'specializes','tarmac':'pavement','trousers':'pants','moult':'molt','moults':'molts','moulting':'molting','moulted':'molted','pushchairs':'strollers'}
_US=re.compile(r'(?<!\w)('+'|'.join(sorted(map(re.escape,US_WORDS),key=len,reverse=True))+r')(?!\w)',re.I)
def _us(g):
    w=g.group(1);r=US_WORDS[w.lower()];return r.capitalize() if w[0].isupper() else r
_PHONE=re.compile(r'\+1[ \u00a0](\d{3})[ \u00a0](\d{3})[ \u00a0](\d{4})')        # source: +1 408 535 4070 -> (408) 535-4070
def american(part):return _PHONE.sub(r'(\1) \2-\3',_US.sub(_us,part))
def units(text):
    """Source text is metric ('9.3 km', '2,260 m', optionally followed by '(5.8 mi)').
    metric build: unchanged apart from {{u:metric|imperial}} -> metric.
    imperial build: American spelling (US_WORDS); {{u:..|..}} -> imperial, 'X km (Y mi)' -> 'Y mi', every other km/m figure converted (not inside tags)."""
    if UNITS=='metric':return _U.sub(lambda g:g.group(1),text)
    text=_U.sub(lambda g:'\x00'+g.group(2)+'\x01',text)                      # shield hand-written imperial text
    out=[]
    for part in re.split(r'(<style.*?</style>|<[^>]+>|\{\{[^}]*\}\}|\x00.*?\x01)',text,flags=re.S):
        if part[:1] in('<','{','\x00'):out.append(part.strip('\x00\x01'));continue
        out.append(american(_QTY.sub(_qty,_DUAL.sub(lambda g:g.group(1),part))))
    return ''.join(out)
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
