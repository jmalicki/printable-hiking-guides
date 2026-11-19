"""What people have actually recorded near a guide's trail: iNaturalist species counts inside the guide's OSM_BBOX.
usage: inat_counts.py <slug> [pad_degrees]     (pad widens the box, e.g. 0.1, when the trail itself has few records)
Use it to decide which animals a wildlife page leads with; a species with no record here should not get a row of its own."""
import sys,json,time,urllib.request,urllib.parse
from hikelib import load_config,slug_arg
C=load_config(slug_arg());pad=float(sys.argv[2]) if len(sys.argv)>2 else 0.0
S,W,N,E=C.OSM_BBOX
for name,taxon in(('Mammals',40151),('Birds',3)):
    q=dict(swlat=S-pad,swlng=W-pad,nelat=N+pad,nelng=E+pad,taxon_id=taxon,per_page=40,verifiable='true')
    r=json.load(urllib.request.urlopen(urllib.request.Request('https://api.inaturalist.org/v1/observations/species_counts?'+urllib.parse.urlencode(q),headers={'User-Agent':'hike-guide-builder/1.0 (personal, low volume)'}),timeout=60))
    print('## %s: %d species recorded'%(name,r['total_results']))
    for x in r['results']:print('  %3d  %s (%s)'%(x['count'],x['taxon'].get('preferred_common_name') or '?',x['taxon']['name']))
    time.sleep(2)
