"""Check a built guide for the mistakes that have got through before. Prints one line per finding; never fails the build.
usage: lint_guide.py <slug>            (reads the variant selected by UNITS / PAPER, like the other scripts)
       lint_guide.py --all             (every guide that has been built, Letter edition)
       lint_guide.py <slug> --build    (what make_pdf.sh runs: wording findings are counted, not listed)
Run automatically at the end of make_pdf.sh. A finding that is intended goes in the guide's config as
LINT_OK=['code', ...] with a comment saying why; it is then left out of the report.

Layout (from the PDF)
  edge          a bordered box or text runs past the right edge of the print area (its border vanishes in macOS Preview)
  empty         a page has an empty band more than a quarter of the page tall
  stat-wrap     a headline figure in the stat strip wraps onto two lines
Text (from the built HTML and the template)
  placeholder   an unfilled {{...}} reached the output
  metric        imperial build still shows km / metres / litres spelling, or a doubled figure ("18 mi / 18 miles")
  absence       "I found no", "could not", "there is none": each must be justified (AGENTS.md, Voice)
  not-that      the "X, not Y" contrast phrasing the owner reads as machine writing
  title         the title has a colon or a line that reads as a tagline
  unwalked      the red banner is there but the sources footer does not say "not walked"
  markers       a marker drawn on the map is missing from the template's tables
  photo         a photo has no credit, or a no-derivatives photo is cropped"""
import sys,os,re,html,glob,json
import pymupdf
from hikelib import load_config,ROOT,UNITS,PAGE_CSS
MM=72/25.4
def strip(h):
    h=re.sub(r'<svg.*?</svg>|<style.*?</style>|base64,[^"]+','',h,flags=re.S)
    return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h)))
def lint(slug):
    C=load_config(slug);out=[];add=lambda code,msg:out.append((code,msg))
    pdf=os.path.join(C.OUT,C.PDF);hf=os.path.join(C.OUT,C.HTML);tpl=open(os.path.join(C.DIR,'template.html')).read()
    if not(os.path.exists(pdf) and os.path.exists(hf)):return [('build','not built: run make GUIDE=%s'%slug)]
    raw=open(hf).read();text=strip(raw);doc=pymupdf.open(pdf)
    # ---- layout ----
    # the print area's right edge: paper width less the @page side margin, which Chrome scales by the html zoom (hikelib.PAGE_CSS)
    side=float(re.search(r'margin:\s*[\d.]+mm\s+([\d.]+)mm',PAGE_CSS).group(1));zoom=float(re.search(r'zoom:\s*([\d.]+)',PAGE_CSS).group(1))
    edge=doc[0].rect.width-side*MM*zoom
    for n,p in enumerate(doc,1):
        H=p.rect.height;imgs=[pymupdf.Rect(i['bbox']) for i in p.get_image_info()]
        blocks=[b for b in p.get_text('blocks') if b[4].strip()]
        if edge:
            for d in p.get_drawings():
                r=d['rect']
                if r.width<30 or r.height<8 or not d.get('color'):continue          # stroked boxes only
                if any(r.intersects(i) and i.width>150 for i in imgs):continue      # map lines are clipped by the map frame on purpose
                if r.x1>edge+0.1:add('edge','page %d: a bordered box runs %.1f pt past the right edge of the print area (top at %d mm)'%(n,r.x1-edge,r.y0/MM))
            for b in blocks:
                if b[2]>edge+1.5 and not any(pymupdf.Rect(b[:4]).intersects(i) and i.width>150 for i in imgs):add('edge','page %d: text runs past the right edge: "%s"'%(n,b[4].strip()[:40].replace('\n',' ')))
        # empty bands: sort everything on the page by its top and look for the tallest gap, including the foot of the page
        spans=sorted([(b[1],b[3]) for b in blocks]+[(i.y0,i.y1) for i in imgs]+[(d['rect'].y0,d['rect'].y1) for d in p.get_drawings() if d['rect'].width>20])
        y=9*MM;gap=0;at=0
        for a,b in spans+[(H-8*MM,H)]:
            if a-y>gap:gap,at=a-y,y
            y=max(y,b)
        if gap>0.25*H:add('empty','page %d: an empty band %d mm tall starts %d mm down the page'%(n,gap/MM,at/MM))
    # stat strip: each headline figure should sit on one line (search_for returns one rectangle per line)
    stats=re.search(r'<div class="stats">((?:\s*<div><b[^>]*>.*?</b><span>.*?</span></div>)+)',raw,re.S)
    vals=[strip(b).strip() for b in re.findall(r'<div><b[^>]*>(.*?)</b>',stats.group(1) if stats else '',re.S)]
    hits={v:[r.y0 for r in doc[0].search_for(v)] for v in vals if v}
    tops=sorted(y for ys in hits.values() for y in ys)
    row=max(tops,key=lambda y:sum(abs(y-z)<4 for z in tops)) if tops else 0      # the strip's first line: the height most figures share
    for v,ys in hits.items():
        if any(6<y-row<45 for y in ys):add('stat-wrap','page 1: stat strip figure "%s" wraps onto two lines'%v)
    # ---- text ----
    for m in set(re.findall(r'\{\{[^}]{0,40}\}?\}?',text)):add('placeholder','unfilled placeholder in the output: %s'%m)
    if UNITS=='imperial':
        t=re.sub(r'jog 5 km|10 m terrain|10 m model','',text)                      # kept metric on purpose (AGENTS.md, Units)
        for m in sorted(set(re.findall(r'[^.]{0,25}\d[\d,.]*\s?(?:km|kilomet(?:re|er)s?|metres?)\b',t)))[:6]:add('metric','metric figure in the imperial build: "…%s"'%m.strip())
        for m in sorted(set(re.findall(r'\b(?:litres?|metres?|kilometres?)\b',t))):add('metric','British unit spelling in the imperial build: "%s"'%m)
        for m in sorted(set(re.findall(r'\d[\d,.]*\s?(?:mi|ft)\s?[/(]\s?\d[\d,.]*\s?(?:miles|feet|mi|ft)\b',t)))[:6]:add('metric','doubled figure: "%s"'%m)
    for m in sorted(set(re.findall(r'[^.]{0,30}\b(?:I found no|[Cc]ould not (?:confirm|find|verify)|[Tt]here is none|[Tt]here are none)\b[^.]{0,40}',text))):add('absence','reports an absence or a doubt, justify it: "%s"'%m.strip())
    for m in sorted(set(re.findall(r'[^.;:(]{12,60}, not (?:a|an|the|by|in|on|for|from|to|as)\b[^.;:)]{3,40}',text)))[:8]:add('not-that','"X, not Y" phrasing: "%s"'%m.strip())
    h1=re.search(r'<h1>(.*?)</h1>',tpl,re.S)
    if h1 and (':' in strip(h1.group(1))):add('title','title has a colon: "%s"'%strip(h1.group(1)).strip())
    banner='class="unwalked"' in tpl;foot=bool(re.search(r'not walked',tpl))
    if banner and not foot:add('unwalked','the red banner is present but the sources footer does not say "not walked for this guide"')
    nums=set(re.findall(r'<span class="num">\s*([^<]{1,3})\s*</span>',tpl))
    for where in('MAP','DETAIL'):
        for key,n in getattr(C,where,{}).get('markers',[]):
            if str(n) not in nums:add('markers','marker %s (%s) is on the %s map but in no table'%(n,key,where.lower()))
    meta=json.load(open(C.DATA+'/photos.json')) if os.path.exists(C.DATA+'/photos.json') else {}
    for k in re.findall(r'\{\{PHOTO:(\w+)\}\}',tpl):
        c=getattr(C,'PHOTOS',{}).get(k,{});m=meta.get(k)
        if not m or not m.get('artist') or not m.get('license'):add('photo','photo "%s" has no credit in photos.json'%k)
        elif 'ND' in m['license'].upper().replace('-',' ').split() and (c.get('crop') or 'nd' not in c.get('cls','').split()):add('photo','photo "%s" is %s: it must be uncropped with the nd figure class'%(k,m['license']))
    ok=set(getattr(C,'LINT_OK',[]))
    return [(c,m) for c,m in out if c not in ok]
if __name__=='__main__':
    if len(sys.argv)<2:sys.exit(__doc__)
    slugs=[os.path.basename(os.path.dirname(f)) for f in sorted(glob.glob(os.path.join(ROOT,'guides','*','config.py')))] if sys.argv[1]=='--all' else [sys.argv[1]]
    total=0;WORDING=('absence','not-that','title')      # judgement calls: listed in full only when the linter is run by hand
    for s in slugs:
        found=lint(s);total+=len(found);quiet=[f for f in found if '--build' in sys.argv and f[0] in WORDING]
        for code,msg in found:
            if (code,msg) not in quiet:print('LINT %s [%s] %s'%(s,code,msg))
        if quiet:print('LINT %s: %d wording findings (%s); list them with scripts/lint_guide.py %s'%(s,len(quiet),', '.join(sorted({c for c,_ in quiet})),s))
    if sys.argv[1]=='--all':print('%d findings in %d guides'%(total,len(slugs)))
