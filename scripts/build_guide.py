"""Build out/guide.html (self-contained) from data/routes.json + data/basemap.png + guide/template.html.
Run from repo root with the venv python:  .venv/bin/python scripts/build_guide.py"""
import json,math,base64,io,bisect
from PIL import Image
R=json.load(open('data/routes.json'));B=json.load(open('data/basemap.json'));Jn=json.load(open('data/junctions.json'))
Z=B['z']
def px(lat,lon):
    x=(lon+180)/360*2**Z;r=math.radians(lat)
    y=(1-math.log(math.tan(r)+1/math.cos(r))/math.pi)/2*2**Z
    return (x-B['x0'])*256,(y-B['y0'])*256
main=R['main'];short=R['short'];spur=R['vc_spur']
allpts=[px(*c) for r in(main,short,spur) for c in r['coords']]
xs=[p[0] for p in allpts];ys=[p[1] for p in allpts]
PAD=120;ASPECT=180/170
x0,x1,y0,y1=min(xs)-PAD,max(xs)+PAD,min(ys)-PAD-20,max(ys)+PAD
w,h=x1-x0,y1-y0
if w/h<ASPECT: d=h*ASPECT-w;x0-=d/2;x1+=d/2
else: d=w/ASPECT-h;y0-=d/2;y1+=d/2
x0=max(0,x0);y0=max(0,y0);x1=min(B['w'],x1);y1=min(B['h'],y1)
x0,y0,x1,y1=map(round,(x0,y0,x1,y1));W,H=x1-x0,y1-y0
img=Image.open('data/basemap.png').crop((x0,y0,x1,y1))
img=Image.blend(img,Image.new('RGB',img.size,'white'),0.10)
buf=io.BytesIO();img.save(buf,'JPEG',quality=88);b64=base64.b64encode(buf.getvalue()).decode()
def P(c):
    a,b=px(*c);return a-x0,b-y0
def path(coords):return 'M'+' L'.join('%.1f %.1f'%P(c) for c in coords)
def sub(r,a,b):
    i=bisect.bisect_left(r['cum'],r['marks'][a]);j=bisect.bisect_left(r['cum'],r['marks'][b]);return r['coords'][i:j+1]
RED='#c8102e';BLUE='#1d4ed8';INK='#1b2a22'
s=[]
s.append('<svg class="map" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">'%(W,H))
s.append('<image href="data:image/jpeg;base64,%s" width="%d" height="%d"/>'%(b64,W,H))
def line(coords,color,width,dash=None,casing=True):
    d=path(coords)
    if casing:s.append('<path d="%s" fill="none" stroke="#fff" stroke-opacity=".85" stroke-width="%d" stroke-linejoin="round" stroke-linecap="round"/>'%(d,width+7))
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="%d" stroke-linejoin="round" stroke-linecap="%s"%s/>'%(d,color,width,'butt' if dash else 'round',' stroke-dasharray="%s"'%dash if dash else ''))
# short-cut variant and visitor-centre spur under the main line
line(sub(short,'lostcv','fc'),BLUE,8,'20 11')
line(spur['coords'],INK,6,'5 9')
line(main['coords'],RED,9)
# direction arrows on the main route
marks_m=[main['marks'][k] for k in main['marks']]
dd=450
while dd<main['length_m']-200:
    if min(abs(dd-m) for m in marks_m)>130:
        i=bisect.bisect_left(main['cum'],dd);a=P(main['coords'][max(0,i-3)]);b=P(main['coords'][min(len(main['coords'])-1,i+3)])
        ang=math.degrees(math.atan2(b[1]-a[1],b[0]-a[0]));c=P(main['coords'][i])
        s.append('<polygon points="15,0 -11,-12 -5,0 -11,12" transform="translate(%.1f %.1f) rotate(%.1f)" fill="%s" stroke="#fff" stroke-width="2.5" stroke-linejoin="round"/>'%(c[0],c[1],ang,RED))
    dd+=620
def label(x,y,t,anchor='start',size=21,weight=600,color=INK,italic=False):
    st='font-size:%dpx;font-weight:%d;%s'%(size,weight,'font-style:italic;' if italic else '')
    s.append('<text x="%.1f" y="%.1f" text-anchor="%s" style="%spaint-order:stroke;stroke:#fff;stroke-width:6px;stroke-linejoin:round;fill:%s">%s</text>'%(x,y,anchor,st,color,t))
def marker(key,n,dx=0,dy=0):
    x,y=P(Jn[key]);x+=dx;y+=dy
    s.append('<circle cx="%.1f" cy="%.1f" r="19" fill="%s" stroke="#fff" stroke-width="4"/>'%(x,y,INK))
    s.append('<text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:24px;font-weight:700;fill:#fff">%s</text>'%(x,y+8.5,n))
    return x,y
for k,n in[('start',1),('t80',2),('vw',3),('bj',4),('fc',5),('cvb',6),('lostcv',7),('cvtop',8)]:
    m=marker(k,n)
    if k=='start':label(m[0]+28,m[1]-8,'START / FINISH',size=22,weight=700);label(m[0]+28,m[1]+17,'Mountain Home Inn',size=20,weight=500)
    if k=='vw':label(m[0]-6,m[1]+50,'Van Wyck Meadow','middle',20,500)
    if k=='cvb':label(m[0]-28,m[1]+6,'Founders Grove','end',20,500)
# Cathedral Grove, visitor centre, short-cut tag
cg=P((37.8982635,-122.5756648));label(cg[0]-22,cg[1]+4,'Cathedral Grove','end',20,500)
vc=P(Jn['vc']);s.append('<rect x="%.1f" y="%.1f" width="26" height="26" rx="5" fill="#fff" stroke="%s" stroke-width="3.5"/>'%(vc[0]-13,vc[1]-13,INK))
s.append('<text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:19px;font-weight:700;fill:%s">i</text>'%(vc[0],vc[1]+7,INK))
label(vc[0]+24,vc[1]+34,'Visitor centre, caf&#233;, WC',size=20,weight=500)
lf=P(Jn['lostfc']);label(lf[0]-20,lf[1]+70,'Short version','end',size=20,weight=700,color=BLUE)
# scale bar + north
mpp=156543.03392*math.cos(math.radians(37.902))/2**Z
bx,by=40,H-46;L=500/mpp
s.append('<rect x="%d" y="%d" width="%.0f" height="74" rx="8" fill="#fff" fill-opacity=".88"/>'%(bx-18,by-48,L+36))
s.append('<path d="M%d %d h%.1f M%d %d v-10 M%.1f %d v-10 M%.1f %d v-10" stroke="%s" stroke-width="3.5" fill="none"/>'%(bx,by,L,bx,by+2,bx+L/2,by+2,bx+L,by+2,INK))
s.append('<text x="%d" y="%d" style="font-size:19px;font-weight:600;fill:%s">0</text><text x="%.1f" y="%d" text-anchor="end" style="font-size:19px;font-weight:600;fill:%s">500 m</text>'%(bx,by-18,INK,bx+L,by-18,INK))
s.append('<g transform="translate(%d 62)"><circle r="36" fill="#fff" fill-opacity=".88"/><path d="M0 -26 L10 12 L0 5 L-10 12 Z" fill="%s"/><text y="29" text-anchor="middle" style="font-size:17px;font-weight:700;fill:%s">N</text></g>'%(W-62,INK,INK))
s.append('</svg>')
MAP=''.join(s)

# ---------- elevation profile ----------
PW,PH,ML,MR,MT,MB=1400,330,70,24,26,48
Lm=main['length_m'];emax=350
def X(d):return ML+(PW-ML-MR)*d/Lm
def Y(e):return MT+(PH-MT-MB)*(1-e/emax)
p=['<svg class="profile" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">'%(PW,PH)]
for e in range(0,351,50):
    p.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#cfd6cf" stroke-width="1.5"/>'%(ML,PW-MR,Y(e),Y(e)))
    if e%100==0:p.append('<text x="%d" y="%.1f" text-anchor="end" class="ax">%d m</text>'%(ML-10,Y(e)+7,e))
for k in range(0,10):
    p.append('<text x="%.1f" y="%d" text-anchor="middle" class="ax">%d km</text>'%(X(k*1000),PH-14,k))
    p.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'%(X(k*1000),X(k*1000),Y(0),Y(0)+7,INK))
pts=' '.join('%.1f,%.1f'%(X(d),Y(e)) for d,e in zip(main['cum'],main['ele']))
p.append('<polygon points="%.1f,%.1f %s %.1f,%.1f" fill="#2f6b4f" fill-opacity=".22"/>'%(X(0),Y(0),pts,X(Lm),Y(0)))
p.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="5" stroke-linejoin="round"/>'%(pts,RED))
for k,n in[('start',1),('t80',2),('vw',3),('bj',4),('fc',5),('cvb',6),('lostcv',7),('cvtop',8),('start_end',1)]:
    d=main['marks'][k];e=main['ele'][bisect.bisect_left(main['cum'],d)]
    cy=Y(e)-30 if k!='fc' else Y(e)-30
    cx=X(d)+(16 if k=='fc' else (-16 if k=='bj' else 0))
    p.append('<line x1="%.1f" x2="%.1f" y1="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'%(X(d),cx,Y(e),cy,INK))
    p.append('<circle cx="%.1f" cy="%.1f" r="15" fill="%s"/><text x="%.1f" y="%.1f" text-anchor="middle" style="font-size:19px;font-weight:700;fill:#fff">%d</text>'%(cx,cy,INK,cx,cy+7,n))
p.append('<text x="%.1f" y="%.1f" text-anchor="middle" class="note">&#8592; Bootjack descent: 250 m down in 2.1 km</text>'%(X(5750),Y(262)))
p.append('<text x="%.1f" y="%.1f" text-anchor="middle" class="note">Canopy View climb: 240 m up in 2.4 km &#8594;</text>'%(X(5750),Y(205)))
p.append('</svg>')
html=open('guide/template.html').read().replace('{{MAP}}',MAP).replace('{{PROFILE}}',''.join(p))
open('out/guide.html','w').write(html)
print('map %dx%d px, html %.1f MB'%(W,H,len(html)/1e6))
