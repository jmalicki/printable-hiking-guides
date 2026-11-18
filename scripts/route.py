import json,math,heapq,sys,collections
d=json.load(open(sys.argv[1]))
def hav(a,b):
    R=6371000;p1,p2=math.radians(a[0]),math.radians(b[0])
    x=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(math.radians(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(x))
pos={};adj=collections.defaultdict(list);wayname={}
for e in d['elements']:
    if e['type']!='way':continue
    t=e['tags'];nm=t.get('name') or ('('+t['highway']+')')
    ns=e['nodes'];g=e['geometry']
    for n,p in zip(ns,g):pos[n]=(p['lat'],p['lon'])
    for i in range(len(ns)-1):
        w=hav(pos[ns[i]],pos[ns[i+1]])
        adj[ns[i]].append((ns[i+1],w,nm,t['highway']));adj[ns[i+1]].append((ns[i],w,nm,t['highway']))
def nearest(pt,names=None):
    best=None
    for n,p in pos.items():
        if names and not any(nm in names for _,_,nm,_ in adj[n]):continue
        dd=hav(pt,p)
        if best is None or dd<best[0]:best=(dd,n)
    return best[1]
def dijk(a,b,allow=None,avoid=()):
    dist={a:0};prev={};pq=[(0,a)]
    while pq:
        dd,u=heapq.heappop(pq)
        if u==b:break
        if dd>dist[u]:continue
        for v,w,nm,hw in adj[u]:
            if allow and nm not in allow:continue
            if nm in avoid:continue
            pen=w*(5 if hw in('secondary','tertiary') else 1)
            if dd+pen<dist.get(v,1e18):
                dist[v]=dd+pen;prev[v]=(u,nm,w);heapq.heappush(pq,(dd+pen,v))
    path=[];u=b
    while u!=a:
        p=prev[u];path.append((u,p[1],p[2]));u=p[0]
    path.reverse();return path
def junction(n1,n2):
    # nodes shared by ways named n1 and n2
    out=[]
    for n in pos:
        s={nm for _,_,nm,_ in adj[n]}
        if n1 in s and n2 in s:out.append(n)
    return out
if __name__=='__main__':
    for a,b in [('Troop 80 Trail','Alice Eastwood Road'),('Troup 80 Trail','Bootjack Trail'),('Troop 80 Trail','Bootjack Trail'),('Bootjack Trail','Redwood Creek Trail'),('Fern Creek Trail','Redwood Creek Trail'),('Fern Creek Trail','Lost Trail'),('Lost Trail','Canopy View Trail'),('Lost Trail','Ocrean View Trail'),('Canopy View Trail','Ocrean View Trail'),('Canopy View Trail','Panoramic Trail'),('Ocrean View Trail','Panoramic Trail'),('Canopy View Trail','Redwood Creek Trail'),('Canopy Trail','Redwood Creek Trail'),('Canopy Trail','Canopy View Trail'),('Panoramic Trail','Alice Eastwood Road'),('Panoramic Trail','Panoramic Highway'),('Bootjack Trail','TCC Trail'),('Fern Creek Trail','Bootjack Trail'),('Ben Johnson Trail','Bootjack Trail'),('Hillside Trail','Ben Johnson Trail'),('Camp Eastwood Trail','Fern Creek Trail'),('Sierra Trail','Troop 80 Trail'),('Alice Eastwood Road','Panoramic Highway')]:
        print(a,'|',b,[(n,round(pos[n][0],5),round(pos[n][1],5)) for n in junction(a,b)])
    n=nearest((37.91004,-122.5767458))
    print('near inn',n,pos[n],[x[2] for x in adj[n]])
    # names of ways within 150m of inn
    s=collections.Counter()
    for m,p in pos.items():
        if hav(p,(37.9102,-122.5772))<200:
            for _,_,nm,hw in adj[m]:s[nm]+=1
    print(s)
