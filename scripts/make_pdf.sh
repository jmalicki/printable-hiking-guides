#!/bin/sh
# Render out/guide.html to out/muir-woods-back-door.pdf with headless Chrome, plus PNG previews of each page.
set -e
cd "$(dirname "$0")/.."
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$PWD/out/muir-woods-back-door.pdf" "file://$PWD/out/guide.html" 2>/dev/null
.venv/bin/python - <<'PY'
import fitz,glob,os
for f in glob.glob('out/preview-*.png'):os.remove(f)
d=fitz.open('out/muir-woods-back-door.pdf')
for i,p in enumerate(d):p.get_pixmap(dpi=110).save('out/preview-%d.png'%(i+1))
print(len(d),'pages')
PY
