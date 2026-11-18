"""Driving route Golden Gate Bridge -> Mountain Home trailhead from the public OSRM demo server.
Writes data/access-route.json (geometry + turn steps)."""
import json,urllib.request
A=(37.8078,-122.4750)   # Golden Gate Bridge toll plaza (south end)
B=(37.91020,-122.57721) # Mountain Home trailhead car park
u='https://router.project-osrm.org/route/v1/driving/%f,%f;%f,%f?overview=full&geometries=geojson&steps=true'%(A[1],A[0],B[1],B[0])
r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'trail-map-script/1.0'}),timeout=60))
rt=r['routes'][0]
steps=[dict(name=s.get('name',''),ref=s.get('ref',''),dist=s['distance'],type=s['maneuver']['type'],mod=s['maneuver'].get('modifier',''),loc=s['maneuver']['location'][::-1]) for s in rt['legs'][0]['steps']]
json.dump(dict(coords=[c[::-1] for c in rt['geometry']['coordinates']],length_m=rt['distance'],duration_s=rt['duration'],steps=steps),open('data/access-route.json','w'))
print('%.1f km, %.0f min'%(rt['distance']/1000,rt['duration']/60))
cum=0
for s in steps:
    print('%6.1f km  %-12s %-12s %-28s %-8s +%.1f km  %.5f,%.5f'%(cum/1000,s['type'],s['mod'],s['name'],s['ref'],s['dist']/1000,s['loc'][0],s['loc'][1]));cum+=s['dist']
