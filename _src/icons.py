"""Favicon and touch icon: a type-set RT monogram on the brand gold. Not the shop's logo."""
import os, sys
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
site = sys.argv[1]
woff = os.path.join(site, "fonts", "sofia-sans-extra-condensed-latin-800-normal.woff2")
ttf = "/tmp/sofia-xc-800.ttf"
f = TTFont(woff); f.flavor = None; f.save(ttf)
def tile(px):
    S = px * 4
    im = Image.new("RGB", (S, S), "#ffcf00")
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(ttf, int(S * 0.86))
    box = d.textbbox((0, 0), "RT", font=font)
    w, h = box[2] - box[0], box[3] - box[1]
    d.text(((S - w) / 2 - box[0], (S - h) / 2 - box[1]), "RT", font=font, fill="#000000")
    return im.resize((px, px), Image.LANCZOS)
tile(180).save(os.path.join(site, "apple-touch-icon.png"))
tile(48).save(os.path.join(site, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
tile(512).save("/tmp/icon-512.png")
print("icons written")
