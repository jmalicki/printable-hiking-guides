import sys,json
sys.argv=[sys.argv[0],sys.argv[1]]
sys.path.insert(0,__file__.rsplit('/',1)[0])
from route import *
start=nearest((37.91020,-122.57721))
print('start',pos[start],[x[2:] for x in adj[start]])
cvb=nearest((37.8937516,-122.5741258),{'Canopy View Trail'})
print('canopy bottom',pos[cvb],[x[2] for x in adj[cvb]])
vc=nearest((37.8927962,-122.5724843),{'Redwood Creek Trail','Bohemian Grove Trail','(footway)'})
def show(label,stops,**kw):
    tot=0;out=[]
    for a,b in zip(stops,stops[1:]):
        p=dijk(a,b,**kw);segs=[]
        for n,nm,w in p:
            if segs and segs[-1][0]==nm:segs[-1][1]+=w
            else:segs.append([nm,w])
        L=sum(w for _,_,w in p);tot+=L
        out.append((round(L),[(s,round(w)) for s,w in segs]))
    print(label,round(tot),'m',round(tot/1609.34,2),'mi')
    for o in out:print('   ',o)
J=dict(t80=313621042,vw=511981002,bj=261758361,fc=261758332,lostfc=361153027,lostcv=354582989,cvtop=361152366)
show('A',[start,J['t80'],J['vw'],J['bj'],J['fc'],cvb,J['lostcv'],J['cvtop'],start])
show('B',[start,J['cvtop'],J['lostcv'],J['lostfc'],J['fc'],cvb,J['lostcv'],J['cvtop'],start])
show('toVC',[cvb,vc])
