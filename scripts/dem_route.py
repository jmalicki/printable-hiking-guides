"""Off-trail legs: sample a terrain grid (USGS 10 m via opentopodata, cached) and trace a least-effort line
between waypoints that avoids steep ground. The result is an APPROXIMATE line for the map, not a surveyed track.
usage: dem_route.py <slug>     config: DEM=dict(bbox=(S,W,N,E),step_m=40), OFFTRAIL={'a-b':[(lat,lon),...], ...}
writes data/<slug>/dem.json (grid) and data/<slug>/offtrail.json ({'a-b':[[lat,lon],...]})"""
import json,os,math,time,heapq,urllib.request
from hikelib import load_config,slug_arg,hav
C=load_config(slug_arg());S,W,N,E=C.DEM['bbox'];step=C.DEM.get('step_m',40)
dlat=step/111320.0;dlon=step/(111320.0*math.cos(math.radians((S+N)/2)))
rows=int((N-S)/dlat)+1;cols=int((E-W)/dlon)+1
f=C.DATA+'/dem.json'
if os.path.exists(f) and json.load(open(f))['meta']==[S,W,N,E,step]:Z=json.load(open(f))['z']
else:
    pts=[(S+r*dlat,W+c*dlon) for r in range(rows) for c in range(cols)];Z=[]
    for i in range(0,len(pts),100):
        u='https://api.opentopodata.org/v1/ned10m?locations='+'|'.join('%.5f,%.5f'%p for p in pts[i:i+100])
        for a in range(5):
            try:res=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'trail-map-script/1.0'}),timeout=60));break
            except Exception as e:time.sleep(5*(a+1))
        Z+=[x['elevation'] for x in res['results']];time.sleep(1.1)
        if i%1000==0:print(i,'/',len(pts),flush=True)
    json.dump(dict(meta=[S,W,N,E,step],z=Z),open(f,'w'))
z=lambda r,c:Z[r*cols+c]
def cell(p):return min(rows-1,max(0,round((p[0]-S)/dlat))),min(cols-1,max(0,round((p[1]-W)/dlon)))
def ll(rc):return (S+rc[0]*dlat,W+rc[1]*dlon)
def trace(a,b):
    a,b=cell(a),cell(b);dist={a:0};prev={};pq=[(0,a)]
    while pq:
        d,u=heapq.heappop(pq)
        if u==b:break
        if d>dist[u]:continue
        for dr in(-1,0,1):
            for dc in(-1,0,1):
                v=(u[0]+dr,u[1]+dc)
                if (dr or dc) and 0<=v[0]<rows and 0<=v[1]<cols:
                    run=step*math.hypot(dr,dc);g=abs(z(*v)-z(*u))/run
                    cost=run*(1+(g/0.30)**2.5)          # heavily penalise ground steeper than ~30%
                    if d+cost<dist.get(v,1e18):dist[v]=d+cost;prev[v]=u;heapq.heappush(pq,(d+cost,v))
    out=[b]
    while out[-1]!=a:out.append(prev[out[-1]])
    return [ll(x) for x in out[::-1]]
res={}
for k,wps in getattr(C,'OFFTRAIL',{}).items():
    line=[]
    for p,q in zip(wps,wps[1:]):
        seg=trace(p,q);line+=seg if not line else seg[1:]
    line[0]=tuple(wps[0]);line[-1]=tuple(wps[-1])
    for _ in range(3):                                  # Chaikin smoothing: the grid staircase is an artefact
        sm=[line[0]]
        for p,q in zip(line,line[1:]):sm+=[(0.75*p[0]+0.25*q[0],0.75*p[1]+0.25*q[1]),(0.25*p[0]+0.75*q[0],0.25*p[1]+0.75*q[1])]
        line=sm+[line[-1]]
    L=sum(hav(x,y) for x,y in zip(line,line[1:]));es=[z(*cell(p)) for p in line]
    res[k]=[list(p) for p in line]
    print('%s: %.2f km, ele %d..%d m, high point %d m at %.5f,%.5f'%(k,L/1000,min(es),max(es),max(es),*line[es.index(max(es))]))
json.dump(res,open(C.DATA+'/offtrail.json','w'))
