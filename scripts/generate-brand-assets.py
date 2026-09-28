"""Generate the site's monogram icons and 1200 x 630 social preview (Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / 'static'
FONT = '/System/Library/Fonts/Avenir Next.ttc'
NAVY = '#122A43'
CREAM = '#F5F2EB'
TEAL = '#67C6BD'

def font(size):
    return ImageFont.truetype(FONT, size)

def monogram(size):
    im = Image.new('RGB', (512, 512), NAVY)
    d = ImageDraw.Draw(im)
    d.text((256, 249), 'AP', font=font(280), fill=CREAM, anchor='mm')
    d.rounded_rectangle((108, 393, 404, 411), radius=9, fill=TEAL)
    return im.resize((size, size), Image.Resampling.LANCZOS)

for size in (16, 32):
    monogram(size).save(STATIC / f'favicon-{size}x{size}.png')
monogram(180).save(STATIC / 'apple-touch-icon.png')
monogram(256).save(STATIC / 'favicon.ico', sizes=[(16,16), (32,32), (48,48), (64,64), (128,128), (256,256)])
card = Image.new('RGB', (1200, 630), CREAM)
d = ImageDraw.Draw(card)
d.rectangle((0, 0, 22, 630), fill=TEAL)
d.rectangle((886, 0, 1200, 630), fill=NAVY)
card.paste(monogram(230), (928, 180))
d.text((78, 78), 'UNIVERSITY OF TORONTO', font=font(23), fill=NAVY)
d.text((74, 175), 'Andreas Park', font=font(76), fill=NAVY)
d.text((78, 282), 'Professor of Finance', font=font(35), fill=NAVY)
d.line((78, 366, 798, 366), fill=TEAL, width=3)
d.text((78, 406), 'Financial markets · FinTech', font=font(29), fill=NAVY)
d.text((78, 450), 'Blockchain · Decentralized finance', font=font(29), fill=NAVY)
d.text((78, 553), 'andreaspark.com', font=font(24), fill=NAVY)
card.save(STATIC / 'images/social-preview.png', optimize=True)
