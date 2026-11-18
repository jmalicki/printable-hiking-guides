"""Build out/<slug>/guide.html (self-contained) from a guide's config, data and template.
usage: build_guide.py <slug>
Template placeholders: {{CSS}} {{MAP}} {{PROFILE}} {{ACCESS}} {{PHOTO:key}} {{PHOTO_CREDITS}}"""
import json,math,base64,io,bisect,os,re
from PIL import Image
from hikelib import load_config,slug_arg,Proj,hav,ROOT
C=load_config(slug_arg());D=C.DATA
R=json.load(open(D+'/routes.json'));Jn=json.load(open(D+'/junctions.json'))
COL=dict(RED='#c8102e',BLUE='#1d4ed8',INK='#1b2a22');RED,BLUE,INK=COL['RED'],COL['BLUE'],COL['INK']
def jpeg_b64(img,q=88):
    b=io.BytesIO();img.save(b,'JPEG',quality=q);return base64.b64encode(b.getvalue()).decode()
def text(x,y,t,anchor='start',size=21,weight=600,color='INK',halo=6):
    return '<text x="%.1f" y="%.1f" text-anchor="%s" style="font-size:%dpx;font-weight:%d;paint-order:stroke;stroke:#fff;stroke-width:%dpx;stroke-linejoin:round;fill:%s">%s</text>'%(x,y,anchor,size,weight,halo,COL.get(color,color),t)

# ---------------- hike map ----------------
M=C.MAP;PJ=Proj(json.load(open(D+'/basemap.json')));main=R[C.MAIN]
pts=[PJ.px(*c) for k in M['extent'] for c in R[k]['coords']]
x0,x1=min(p[0] for p in pts)-M['pad'],max(p[0] for p in pts)+M['pad'];y0,y1=min(p[1] for p in pts)-M['pad']-20,max(p[1] for p in pts)+M['pad']
w,h=x1-x0,y1-y0
if w/h<M['aspect']:d=h*M['aspect']-w;x0-=d/2;x1+=d/2
else:d=w/M['aspect']-h;y0-=d/2;y1+=d/2
x0,y0,x1,y1=round(max(0,x0)),round(max(0,y0)),round(min(PJ.w,x1)),round(min(PJ.h,y1));W,H=x1-x0,y1-y0
img=Image.blend(Image.open(D+'/basemap.png').crop((x0,y0,x1,y1)),Image.new('RGB',(W,H),'white'),0.10)
def P(c):
    a,b=PJ.px(*c);return a-x0,b-y0
def at(spec):return P(Jn[spec]) if isinstance(spec,str) else P(spec)
def dpath(coords):return 'M'+' L'.join('%.1f %.1f'%P(c) for c in coords)
def sub(r,a,b):
    i=bisect.bisect_left(r['cum'],r['marks'][a]);j=bisect.bisect_left(r['cum'],r['marks'][b]);return r['coords'][i:j+1]
s=['<svg class="map" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">'%(W,H),'<image href="data:image/jpeg;base64,%s" width="%d" height="%d"/>'%(jpeg_b64(img),W,H)]
def line(coords,color,width,dash=None):
    d=dpath(coords)
    s.append('<path d="%s" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="%d" stroke-linejoin="round" stroke-linecap="round"/>'%(d,width+7))
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="%d" stroke-linejoin="round" stroke-linecap="%s"%s/>'%(d,COL[color],width,'butt' if dash else 'round',' stroke-dasharray="%s"'%dash if dash else ''))
for o in M['overlays']:
    r=R[o['route']];line(sub(r,o['frm'],o['to']) if 'frm' in o else r['coords'],o['color'],o['width'],o.get('dash'))
line(main['coords'],'RED',9)
mk=[main['marks'][k] for k,_ in M['markers']];dd=M.get('arrow_start',450)
while dd<main['length_m']-200:
    if min(abs(dd-m) for m in mk)>130:
        i=bisect.bisect_left(main['cum'],dd);a=P(main['coords'][max(0,i-3)]);b=P(main['coords'][min(len(main['coords'])-1,i+3)]);c=P(main['coords'][i])
        s.append('<polygon points="15,0 -11,-12 -5,0 -11,12" transform="translate(%.1f %.1f) rotate(%.1f)" fill="%s" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>'%(c[0],c[1],math.degrees(math.atan2(b[1]-a[1],b[0]-a[0])),RED))
    dd+=M.get('arrow_step',620)
for k,n in M['markers']:
    x,y=P(Jn[k])
    s.append('<circle cx="%.1f" cy="%.1f" r="19" fill="%s" stroke="#fff" stroke-width="4"/><text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:24px;font-weight:700;fill:#fff">%s</text>'%(x,y,INK,x,y+8.5,n))
for k in M['icons']:
    x,y=at(k);s.append('<rect x="%.1f" y="%.1f" width="26" height="26" rx="5" fill="#fff" stroke="%s" stroke-width="3.5"/><text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:19px;font-weight:700;fill:%s">i</text>'%(x-13,y-13,INK,x,y+7,INK))
for L in M['labels']:
    x,y=at(L['at']);s.append(text(x+L.get('dx',0),y+L.get('dy',0),L['text'],L.get('anchor','start'),L.get('size',20),L.get('weight',500),L.get('color','INK')))
def scalebar(metres,label,mpp,Hh,k=1.0):
    L=metres/mpp;bx,by=40*k,Hh-46*k
    return ('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="8" fill="#fff" fill-opacity=".88"/>'%(bx-18*k,by-48*k,L+36*k,74*k)+
     '<path d="M%.0f %.0f h%.1f M%.0f %.0f v%.0f M%.1f %.0f v%.0f M%.1f %.0f v%.0f" stroke="%s" stroke-width="%.1f" fill="none"/>'%(bx,by,L,bx,by+2,-10*k,bx+L/2,by+2,-10*k,bx+L,by+2,-10*k,INK,3.5*k)+
     '<text x="%.0f" y="%.0f" style="font-size:%dpx;font-weight:600;fill:%s">0</text><text x="%.1f" y="%.0f" text-anchor="end" style="font-size:%dpx;font-weight:600;fill:%s">%s</text>'%(bx,by-18*k,19*k,INK,bx+L,by-18*k,19*k,INK,label))
s.append(scalebar(500,'500 m',PJ.mpp(main['coords'][0][0]),H))
s.append('<g transform="translate(%d 62)"><circle r="36" fill="#fff" fill-opacity=".88"/><path d="M0 -26 L10 12 L0 5 L-10 12 Z" fill="%s"/><text y="29" text-anchor="middle" style="font-size:17px;font-weight:700;fill:%s">N</text></g></svg>'%(W-62,INK,INK))
MAP=''.join(s)

# ---------------- elevation profile ----------------
PF=C.PROFILE;PW,PH,ML,MR,MT,MB=1400,PF.get('height',330),78,24,30,48;Lm=main['length_m'];e0,e1=PF['emin'],PF['emax']
X=lambda d:ML+(PW-ML-MR)*d/Lm
Y=lambda e:MT+(PH-MT-MB)*(1-(e-e0)/(e1-e0))
p=['<svg class="profile" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">'%(PW,PH)]
for e in range(e0,e1+1,PF['grid']):
    p.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#cfd6cf" stroke-width="1.5"/>'%(ML,PW-MR,Y(e),Y(e)))
    if (e-e0)%PF['label_every']==0:p.append('<text x="%d" y="%.1f" text-anchor="end" class="ax">%d m</text>'%(ML-10,Y(e)+7,e))
for k in range(0,int(Lm/1000)+1):
    p.append('<text x="%.1f" y="%d" text-anchor="middle" class="ax">%d km</text><line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'%(X(k*1000),PH-14,k,X(k*1000),X(k*1000),Y(e0),Y(e0)+7,INK))
pp=' '.join('%.1f,%.1f'%(X(d),Y(e)) for d,e in zip(main['cum'],main['ele']))
p.append('<polygon points="%.1f,%.1f %s %.1f,%.1f" fill="#2f6b4f" fill-opacity=".22"/><polyline points="%s" fill="none" stroke="%s" stroke-width="5" stroke-linejoin="round"/>'%(X(0),Y(e0),pp,X(Lm),Y(e0),pp,RED))
for k,n,dx in PF['markers']:
    d=main['marks'][k];e=main['ele'][bisect.bisect_left(main['cum'],d)];cx,cy=X(d)+dx,Y(e)-30
    p.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/><circle cx="%.1f" cy="%.1f" r="15" fill="%s"/><text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:19px;font-weight:700;fill:#fff">%s</text>'%(X(d),cx,Y(e),cy,INK,cx,cy,INK,cx,cy+7,n))
for d,e,t in PF['notes']:p.append('<text x="%.1f" y="%.1f" text-anchor="middle" class="note">%s</text>'%(X(d),Y(e),t))
p.append('</svg>');PROFILE=''.join(p)

# ---------------- access (driving) map ----------------
A=C.ACCESS;AR=json.load(open(D+'/access-route.json'));AJ=Proj(json.load(open(D+'/access-basemap.json')))
ap=[AJ.px(*c) for c in AR['coords']];pl,pr,pt,pb=A['pad']
ax0=round(max(0,min(q[0] for q in ap)-pl));ax1=round(min(AJ.w,max(q[0] for q in ap)+pr));ay0=round(max(0,min(q[1] for q in ap)-pt));ay1=round(min(AJ.h,max(q[1] for q in ap)+pb));AW,AH=ax1-ax0,ay1-ay0
aimg=Image.blend(Image.open(D+'/access-basemap.png').crop((ax0,ay0,ax1,ay1)),Image.new('RGB',(AW,AH),'white'),0.12)
def AP(c):
    a,b=AJ.px(*c);return a-ax0,b-ay0
acum=[0.0]
for c1,c2 in zip(AR['coords'],AR['coords'][1:]):acum.append(acum[-1]+hav(c1,c2))
def along(m):return AR['coords'][min(len(acum)-1,bisect.bisect_left(acum,m))]
def step_loc(pred):return [x for x in AR['steps'] if pred(x)][0]['loc']
def dist_of(loc):return acum[min(range(len(acum)),key=lambda i:(AR['coords'][i][0]-loc[0])**2+(AR['coords'][i][1]-loc[1])**2)]
def where(spec):
    k=spec[0]
    if k=='m':return along(spec[1])
    if k=='type':return step_loc(lambda x:x['type']==spec[1])
    if k=='name':return step_loc(lambda x:x['name']==spec[1])
    if k=='after':return along(dist_of(step_loc(lambda x:x['name']==spec[1]))+spec[2])
    if k=='end':return AR['coords'][-1]
    return spec[1]          # ('at',(lat,lon))
dA='M'+' L'.join('%.1f %.1f'%AP(c) for c in AR['coords'])
s=['<svg class="amap" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">'%(AW,AH),'<image href="data:image/jpeg;base64,%s" width="%d" height="%d"/>'%(jpeg_b64(aimg),AW,AH),
   '<path d="%s" fill="none" stroke="#fff" stroke-opacity=".9" stroke-width="17" stroke-linejoin="round" stroke-linecap="round"/><path d="%s" fill="none" stroke="%s" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>'%(dA,dA,BLUE)]
for m in A['places']:
    x,y=AP(m['at'])
    if m.get('dot',True):s.append('<circle cx="%.1f" cy="%.1f" r="14" fill="#fff" stroke="%s" stroke-width="6"/>'%(x,y,INK))
    s.append(text(x+m.get('dx',0),y+m.get('dy',0),m['label'],m.get('anchor','start'),m.get('size',36),m.get('weight',600),halo=10))
for m in A['markers']:
    x,y=AP(where(m['at']))
    s.append('<circle cx="%.1f" cy="%.1f" r="35" fill="%s" stroke="#fff" stroke-width="6"/><text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:43px;font-weight:700;fill:#fff">%s</text>'%(x,y,COL.get(m.get('fill','INK')),x,y+15,m['letter']))
    s.append(text(x+m.get('dx',0),y+m.get('dy',0),m['label'],m.get('anchor','start'),m.get('size',38),m.get('weight',600),halo=10))
s.append(scalebar(2000,'2 km',AJ.mpp(37.86),AH,1.8)+'</svg>');ACCESS=''.join(s)

# ---------------- photos ----------------
PH_=getattr(C,'PHOTOS',{});meta=json.load(open(D+'/photos.json')) if os.path.exists(D+'/photos.json') else {}
def photo(m):
    k=m.group(1);c=PH_[k];im=Image.open('%s/photos/%s.jpg'%(D,k)).convert('RGB')
    if c.get('crop'):                       # crop = (left,top,right,bottom) as fractions
        l,t,r,b=c['crop'];im=im.crop((int(l*im.width),int(t*im.height),int(r*im.width),int(b*im.height)))
    if im.width>1300:im=im.resize((1300,int(im.height*1300/im.width)))
    return '<figure class="photo %s"><img src="data:image/jpeg;base64,%s"><figcaption>%s</figcaption></figure>'%(c.get('cls',''),jpeg_b64(im,80),c['caption'])
credits=' · '.join('%s: %s, %s'%(PH_[k].get('short',k),meta[k]['artist'],meta[k]['license']) for k in PH_ if k in meta)
html=open(C.DIR+'/template.html').read().replace('{{CSS}}',open(ROOT+'/guides/shared.css').read())
html=html.replace('{{MAP}}',MAP).replace('{{PROFILE}}',PROFILE).replace('{{ACCESS}}',ACCESS).replace('{{PHOTO_CREDITS}}',credits)
html=re.sub(r'\{\{PHOTO:(\w+)\}\}',photo,html)
open(C.OUT+'/guide.html','w').write(html)
print('%s: map %dx%d, access %dx%d, html %.1f MB'%(C.SLUG,W,H,AW,AH,len(html)/1e6))
