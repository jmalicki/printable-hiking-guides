#!/bin/sh
# usage: make_pdf.sh <slug>  — render out/<slug>/guide.html to PDF with headless Chrome, plus PNG page previews.
set -e
cd "$(dirname "$0")/.."
SLUG="$1"; set -- $(.venv/bin/python -c "import sys;sys.path.insert(0,'scripts');from hikelib import load_config;c=load_config('$SLUG');print(c.PDF,c.HTML)"); PDF="$1"; HTML="$2"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$PWD/out/$SLUG/$PDF" "file://$PWD/out/$SLUG/$HTML" 2>/dev/null
.venv/bin/python - "$SLUG" "$PDF" "$HTML" <<'PY'
import pymupdf,glob,os,sys
o='out/'+sys.argv[1]
for f in glob.glob(o+'/preview-*.png'):os.remove(f)
d=pymupdf.open(o+'/'+sys.argv[2])
for i,p in enumerate(d):p.get_pixmap(dpi=110).save(o+'/preview-%d.png'%(i+1))
want=open(o+'/'+sys.argv[3]).read().count('<section class="page">')
print(sys.argv[2],len(d),'pages'+('' if len(d)==want else '   *** OVERFLOW: template has %d page sections ***'%want))
PY
