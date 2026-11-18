"""Search Wikimedia Commons for freely licensed photos, to pick images for a guide's PHOTOS config.
usage: commons_search.py "query one" "query two" ...   (prints title | size | licence | author; pauses between queries)"""
import sys,json,time,urllib.request,urllib.parse,re
UA={'User-Agent':'hike-guide-builder/1.0 (personal, low volume)'}
for q in sys.argv[1:]:
    print('##',q)
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',format='json',generator='search',gsrsearch=q+' filetype:bitmap',gsrnamespace=6,gsrlimit=8,prop='imageinfo',iiprop='size|extmetadata'))
    try:r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60))
    except Exception as e:print('  failed:',e);time.sleep(20);continue
    for p in sorted(r.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',0)):
        ii=p['imageinfo'][0];m=ii.get('extmetadata',{})
        g=lambda k:re.sub('<[^>]+>','',m.get(k,{}).get('value','')).strip()[:40]
        print('  %s | %dx%d | %s | %s'%(p['title'][:150],ii['width'],ii['height'],g('LicenseShortName'),g('Artist')))
    time.sleep(4)
