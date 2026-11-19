#!/bin/sh
# usage: make_pdf.sh <slug>  — render out/<slug>/guide.html to PDF with headless Chrome, plus PNG page previews.
set -e
cd "$(dirname "$0")/.."
SLUG="$1"; PDF=$(.venv/bin/python -c "import sys;sys.path.insert(0,'scripts');from hikelib import load_config;print(load_config('$SLUG').PDF)")
if [ "${PDF_ENGINE:-chrome}" = mupdf ]; then
  .venv/bin/python scripts/print_with_mupdf.py "out/$SLUG/guide.html" "out/$SLUG/$PDF"
else
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$PWD/out/$SLUG/$PDF" "file://$PWD/out/$SLUG/guide.html" 2>/dev/null
fi
.venv/bin/python - "$SLUG" "$PDF" <<'PY'
import pymupdf,glob,os,sys
o='out/'+sys.argv[1]
for f in glob.glob(o+'/preview-*.png'):os.remove(f)
d=pymupdf.open(o+'/'+sys.argv[2])
for i,p in enumerate(d):p.get_pixmap(dpi=110).save(o+'/preview-%d.png'%(i+1))
print(sys.argv[1],len(d),'pages')
PY
