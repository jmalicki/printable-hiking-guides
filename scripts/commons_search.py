"""Search Wikimedia Commons for freely licensed photos. usage: commons_search.py "query" [n]
Prints title | size | license | author | thumb url (for picking images to add to a guide's PHOTOS list)."""
import sys,json,urllib.request,urllib.parse,re
q=sys.argv[1];n=int(sys.argv[2]) if len(sys.argv)>2 else 8
u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',format='json',generator='search',gsrsearch=q+' filetype:bitmap',gsrnamespace=6,gsrlimit=n,prop='imageinfo',iiprop='url|size|extmetadata',iiurlwidth=1400))
r=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'hike-guide-script/1.0'}),timeout=60))
for p in sorted(r.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',0)):
    ii=p['imageinfo'][0];m=ii.get('extmetadata',{})
    g=lambda k:re.sub('<[^>]+>','',m.get(k,{}).get('value','')).strip()[:60]
    print('%s | %dx%d | %s | %s'%(p['title'],ii['width'],ii['height'],g('LicenseShortName'),g('Artist')))
