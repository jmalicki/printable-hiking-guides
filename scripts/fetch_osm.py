"""Download trail geometry from OpenStreetMap (Overpass) into data/osm-trails.json. Retries on busy servers."""
import urllib.request,urllib.parse,time,sys
Q='[out:json][timeout:60];(way["highway"~"path|footway|track|service|steps|pedestrian|unclassified|secondary|tertiary"](37.886,-122.612,37.916,-122.562);node["name"](37.886,-122.612,37.916,-122.562););out body geom;'
for attempt in range(6):
    try:
        req=urllib.request.Request('https://overpass-api.de/api/interpreter',data=urllib.parse.urlencode({'data':Q}).encode(),headers={'User-Agent':'trail-map-script/1.0'})
        b=urllib.request.urlopen(req,timeout=120).read()
        if b[:1]==b'{':open('data/osm-trails.json','wb').write(b);print('ok',len(b));sys.exit(0)
    except Exception as e:print('retry',e)
    time.sleep(10*2**attempt)
sys.exit('overpass unavailable')
