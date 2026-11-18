"""Browse a Wikimedia Commons category as a numbered thumbnail contact sheet, to pick photos by eye.
usage: commons_browse.py <outdir> "Category name" ["Another category" ...]
Writes <outdir>/<category>.png (contact sheet) and <outdir>/<category>.txt (number -> File: title | licence | author)."""
import sys,os,json,time,io,re,urllib.request,urllib.parse
from PIL import Image,ImageDraw
UA={'User-Agent':'hike-guide-builder/1.0 (personal, low volume)'}
def get(u):
    for a in range(5):
        try:return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
        except Exception as e:
            if a==4:raise
            time.sleep(15*(a+1))
out=sys.argv[1];os.makedirs(out,exist_ok=True)
for cat in sys.argv[2:]:
    u='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',format='json',generator='categorymembers',gcmtitle='Category:'+cat,gcmtype='file',gcmlimit=60,prop='imageinfo',iiprop='url|size|extmetadata|mime',iiurlwidth=330))
    pages=[p for p in json.loads(get(u)).get('query',{}).get('pages',{}).values() if 'imageinfo' in p and p['imageinfo'][0].get('mime') in('image/jpeg','image/png')]
    pages.sort(key=lambda p:p['title']);cw,ch,cols=340,270,5
    sheet=Image.new('RGB',(cw*cols,ch*max(1,(len(pages)+cols-1)//cols)),'white');d=ImageDraw.Draw(sheet);lines=[]
    for i,p in enumerate(pages):
        ii=p['imageinfo'][0];m=ii.get('extmetadata',{});g=lambda k:re.sub('<[^>]+>','',m.get(k,{}).get('value','')).strip()[:40]
        try:
            im=Image.open(io.BytesIO(get(ii['thumburl']))).convert('RGB');im.thumbnail((cw-8,ch-24));sheet.paste(im,((i%cols)*cw+4,(i//cols)*ch+20))
        except Exception as e:pass
        d.text(((i%cols)*cw+5,(i//cols)*ch+4),'#%d  %dx%d'%(i,ii['width'],ii['height']),fill='black')
        lines.append('%d | %s | %s | %s'%(i,p['title'],g('LicenseShortName'),g('Artist')));time.sleep(2.2)
    safe=re.sub(r'\W+','_',cat)
    sheet.save('%s/%s.png'%(out,safe));open('%s/%s.txt'%(out,safe),'w').write('\n'.join(lines))
    print(cat,len(pages),'files');time.sleep(3)
