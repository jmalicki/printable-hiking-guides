"""Render page-section HTML on A4 when a headless browser is unavailable.

MuPDF supports a smaller CSS subset than Chrome. Render each authored section
separately and rasterise inline SVGs before passing them to its HTML engine.
Optional data-print-width (points) and data-print-aspect attributes on a div
set the size of the enclosed map or photo. The default preserves aspect ratio.
"""
import base64
import io
import re
import sys
from pathlib import Path

import pymupdf
from PIL import Image, ImageOps

PAGE = pymupdf.Rect(0, 0, 595.28, 841.89)
CONTENT = pymupdf.Rect(37, 30, 558, 812)
CSS = """
* {font-family:sans-serif;color:#24372c}
body {font-size:10.7pt;line-height:1.41}
p {margin:0 0 8pt}
h1,h2,h3 {font-family:serif;color:#193a2b}
h1 {font-size:34pt;margin:0 0 4pt} h2 {font-size:23pt;margin:0 0 8pt}
h3 {font-size:15pt;margin:8pt 0 4pt}
.sub {font-family:serif;font-style:italic;font-size:15pt}
.folio,.kicker {color:#43664f;font-size:9pt;margin:0 0 12pt}
.small,figcaption {color:#4e6054;font-size:8.4pt}
table {border-collapse:collapse;width:100%;margin-bottom:8pt}
th,td {padding:5pt 4pt 5pt 0;border-bottom:.6pt solid #a2b6a7;text-align:left;vertical-align:top}
th {color:#315740;font-size:9pt}.facts b {font-size:14pt}.facts td {width:25%}
.warn {background:#fcf0ed;border-left:3pt solid #b04036;padding:4pt 10pt}
.warn h3 {color:#962c25}.warn p {margin-bottom:1pt}a {color:#346449}
"""
MEDIA = re.compile(r'(?:<div[^>]* data-print-width="(?P<width>\d+)"(?: data-print-aspect="(?P<aspect>[\d.]+)")?>\s*)?'
                   r'(?P<media><svg\b.*?</svg>|<figure\b.*?</figure>)(?(width)\s*</div>)', re.S)


def rasterise_svg(source):
    # MuPDF paints the text stroke last. Paint a second, unoutlined glyph over it.
    def outline(match):
        return match[0] + re.sub(r'stroke:#fff;stroke-width:[^;]+;', 'stroke:none;', match[0])
    source = re.sub(r'<text [^>]*paint-order:stroke[^>]*>.*?</text>', outline, source)
    source = source.replace('<svg ', '<svg font-family="sans-serif" ', 1)
    source = source.replace('class="ax"', 'font-size="19" fill="#506455"')
    with pymupdf.open(stream=source.encode(), filetype='svg') as svg:
        pixmap = svg[0].get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
        if '<image ' in source:
            return pixmap.tobytes('jpeg', jpg_quality=92)
        return pixmap.tobytes('png')


def render(input_path, output_path):
    sections = re.findall(r'<section class="page">(.*?)</section>', input_path.read_text(), re.S)
    if not sections:
        raise ValueError('HTML must contain page sections')
    with pymupdf.open() as doc:
        for number, body in enumerate(sections, 1):
            assets = pymupdf.Archive()
            def embed(match):
                media = match['media']
                width = int(match['width'] or 485)
                name = f'asset-{match.start()}'
                caption = ''
                if media.startswith('<svg'):
                    data = rasterise_svg(media)
                else:
                    photo = re.search(r'src="data:image/jpeg;base64,([^"]+)"', media)
                    data = base64.b64decode(photo[1])
                    if match['aspect']:
                        im = Image.open(io.BytesIO(data))
                        size = (im.width, round(im.width / float(match['aspect'])))
                        buf = io.BytesIO()
                        ImageOps.fit(im, size, centering=(.5,.27)).save(buf, 'JPEG', quality=92)
                        data = buf.getvalue()
                    caption = re.search(r'<figcaption>(.*?)</figcaption>', media, re.S)[1]
                assets.add((data, name))
                image = f'<img src="{name}" width="{width}">'
                return image + (f'<p class="small">{caption}</p>' if caption else '')
            body = MEDIA.sub(embed, body).replace('</b><small>', '</b><br><small>')
            page = doc.new_page(width=PAGE.width, height=PAGE.height)
            _, scale = page.insert_htmlbox(CONTENT, body, css=CSS, archive=assets)
            page.insert_text((527,824), f'{number} / {len(sections)}', fontsize=8, color=(.3,.4,.32))
            print(f'Page {number}: {scale:.0%} print scale')
        doc.save(output_path, garbage=4, deflate=True)


if __name__ == '__main__':
    render(Path(sys.argv[1]), Path(sys.argv[2]))
