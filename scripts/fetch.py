"""Download everything a guide needs from the network (cached on disk afterwards).
usage: fetch.py <slug> [osm] [tiles] [access]     (no step names = all three)
  osm    -> data/<slug>/osm.json            OpenStreetMap trails (Overpass)
  tiles  -> data/<slug>/basemap.png|json    USGS Topo tiles for the hike map (+ access-basemap for the driving map)
  access -> data/<slug>/access-route.json   driving route (public OSRM server)"""
import sys,os,json,math,time,urllib.request,urllib.parse
from hikelib import load_config,slug_arg,ROOT
C=load_config(slug_arg());steps=sys.argv[2:] or ['osm','tiles','access']
UA={'User-Agent':'trail-map-script/1.0'}
def get(url,data=None,timeout=120):
    return urllib.request.urlopen(urllib.request.Request(url,data=data,headers=UA),timeout=timeout).read()
def osm():
    q='[out:json][timeout:60];(way["highway"~"path|footway|track|service|steps|pedestrian|unclassified|secondary|tertiary"](%s);node["name"](%s););out body geom;'%((','.join(map(str,C.OSM_BBOX)),)*2)
    for attempt in range(6):
        try:
            b=get('https://overpass-api.de/api/interpreter',urllib.parse.urlencode({'data':q}).encode())
            if b[:1]==b'{':open(C.DATA+'/osm.json','wb').write(b);print('osm ok',len(b));return
        except Exception as e:print('retry',e)
        time.sleep(10*2**attempt)
    sys.exit('overpass unavailable')
def tiles(name,z,bbox):
    from PIL import Image
    S,W,N,E=bbox
    tx=lambda lon:(lon+180)/360*2**z
    def ty(lat):
        r=math.radians(lat);return (1-math.log(math.tan(r)+1/math.cos(r))/math.pi)/2*2**z
    x0,x1=int(tx(W)),int(tx(E));y0,y1=int(ty(N)),int(ty(S))
    cache=os.path.join(ROOT,'data','tiles');os.makedirs(cache,exist_ok=True)
    img=Image.new('RGB',((x1-x0+1)*256,(y1-y0+1)*256))
    for x in range(x0,x1+1):
        for y in range(y0,y1+1):
            f='%s/%d_%d_%d.png'%(cache,z,x,y)
            if not os.path.exists(f):open(f,'wb').write(get('https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/%d/%d/%d'%(z,y,x),timeout=60))
            img.paste(Image.open(f).convert('RGB'),((x-x0)*256,(y-y0)*256))
    img.save('%s/%s.png'%(C.DATA,name))
    json.dump(dict(z=z,x0=x0,y0=y0,w=img.size[0],h=img.size[1]),open('%s/%s.json'%(C.DATA,name),'w'))
    print(name,img.size)
def access():
    A,B=C.ACCESS['from'],C.ACCESS['to']
    r=json.loads(get('https://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f?overview=full&geometries=geojson&steps=true'%(A[1],A[0],B[1],B[0]),timeout=60))
    rt=r['routes'][0]
    st=[dict(name=s.get('name',''),dist=s['distance'],type=s['maneuver']['type'],mod=s['maneuver'].get('modifier',''),loc=s['maneuver']['location'][::-1]) for s in rt['legs'][0]['steps']]
    json.dump(dict(coords=[c[::-1] for c in rt['geometry']['coordinates']],length_m=rt['distance'],duration_s=rt['duration'],steps=st),open(C.DATA+'/access-route.json','w'))
    print('access %.1f km, %.0f min'%(rt['distance']/1000,rt['duration']/60));cum=0
    for s in st:print('  %5.1f km %-10s %-11s %-26s +%.1f km'%(cum/1000,s['type'],s['mod'],s['name'],s['dist']/1000));cum+=s['dist']
if 'osm' in steps:osm()
if 'tiles' in steps:
    tiles('basemap',C.TILES['z'],C.TILES['bbox']);tiles('access-basemap',C.ACCESS['z'],C.ACCESS['bbox'])
if 'access' in steps:access()
