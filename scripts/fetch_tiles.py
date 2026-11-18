"""Fetch USGS Topo (public domain) tiles covering the hike and stitch into data/basemap.png.
Writes data/basemap.json with the Web-Mercator pixel origin so the map script can project onto it."""
import math,os,json,urllib.request,io,sys
from PIL import Image
# usage: fetch_tiles.py [name Z S W N E]   (default: the hike basemap)
NAME='basemap';Z=16
S,W,N,E=37.8895,-122.6025,37.9160,-122.5670
if len(sys.argv)>1:
    NAME=sys.argv[1];Z=int(sys.argv[2]);S,W,N,E=map(float,sys.argv[3:7])
def tx(lon):return (lon+180)/360*2**Z
def ty(lat):
    r=math.radians(lat);return (1-math.log(math.tan(r)+1/math.cos(r))/math.pi)/2*2**Z
x0,x1=int(tx(W)),int(tx(E));y0,y1=int(ty(N)),int(ty(S))
os.makedirs('data/tiles',exist_ok=True)
img=Image.new('RGB',((x1-x0+1)*256,(y1-y0+1)*256))
for x in range(x0,x1+1):
    for y in range(y0,y1+1):
        f='data/tiles/%d_%d_%d.png'%(Z,x,y)
        if not os.path.exists(f):
            u='https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/%d/%d/%d'%(Z,y,x)
            req=urllib.request.Request(u,headers={'User-Agent':'trail-map-script/1.0'})
            open(f,'wb').write(urllib.request.urlopen(req,timeout=60).read())
        img.paste(Image.open(f).convert('RGB'),((x-x0)*256,(y-y0)*256))
img.save('data/%s.png'%NAME)
json.dump(dict(z=Z,x0=x0,y0=y0,w=img.size[0],h=img.size[1],bbox=[S,W,N,E]),open('data/%s.json'%NAME,'w'))
print(img.size,(x1-x0+1)*(y1-y0+1),'tiles')
