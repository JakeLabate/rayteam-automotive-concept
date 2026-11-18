"""Crops and compresses the shop's own photos into site/img/photos. Sources live in media/raw.

id -> (output name, aspect w:h, max width, focus x, focus y). Nothing is upscaled.
"""
import json, os, sys
from PIL import Image, features
RAW, OUT = sys.argv[1], sys.argv[2]
idx = {m["i"]: m for m in json.load(open(os.path.join(RAW, "..", "index.json")))}
JOBS = [
    (22, "shop-mercedes-sl", (3, 4), 480, .5, .5), (29, "shop-aisle", (3, 4), 480, .5, .6),
    (23, "shop-porsche-gt3rs", (3, 4), 480, .5, .4), (153, "shop-audi-lift-tall", (3, 4), 480, .66, .5),
    (13, "shop-jaguar-etype", (3, 4), 480, .5, .5),
    (15, "shop-audi-rs3-tall", (3, 4), 480, .55, .5), (143, "ur-quattro-wide", (16, 9), 800, .5, .62),
    (153, "shop-audi-lift", (5, 4), 725, .5, .5), (70, "brake-caliper", (5, 4), 700, .5, .5),
    (66, "audi-rs3-front", (4, 3), 800, .5, .5), (28, "audi-liqui-moly", (1, 1), 500, .5, .3),
    (27, "shop-sign-audi", (1, 1), 500, .5, .15), (4, "bmw-bay", (1, 1), 500, .5, .5),
    (2, "porsche-gt2rs", (1, 1), 500, .5, .5), (15, "audi-rs3-bay", (1, 1), 500, .5, .5),
    (1, "vw-lift", (1, 1), 500, .5, .5), (49, "land-rover-alignment", (4, 3), 933, .5, .5),
    (53, "range-rover-wheel-off", (4, 3), 933, .5, .5), (36, "range-rover-engine-bay", (4, 3), 800, .5, .5),
    (20, "shop-floor", (1, 1), 500, .5, .7), (91, "shop-bays", (3, 2), 450, .5, .5),
    (145, "team", (3, 2), 870, .5, .5), (25, "floor-logo", (1, 1), 450, .5, .5),
    (126, "exhaust-fabrication", (4, 3), 960, .5, .5), (22, "mercedes-sl", (1, 1), 500, .5, .45),
    (23, "porsche-gt3rs", (1, 1), 500, .5, .4), (13, "jaguar-etype", (1, 1), 500, .5, .5),
    (29, "shop-aisle-wide", (1, 1), 400, .5, .7),
    (130, "race-bend", (1, 1), 900, .5, .5), (133, "race-front", (1, 1), 900, .5, .5),
    (129, "race-speed-wide", (16, 9), 960, .5, .55), (133, "race-front-wide", (16, 9), 960, .5, .6),
    (124, "race-car-lift", (4, 3), 960, .5, .5), (124, "race-car-lift-wide", (16, 9), 960, .5, .35),
    (123, "race-underside-wide", (16, 9), 960, .5, .6), (103, "ascutney-dusk-wide", (16, 9), 960, .5, .5),
    (95, "okemo-wide", (16, 9), 960, .5, .5), (143, "ur-quattro", (3, 4), 600, .5, .55),
    (120, "race-trailer", (4, 3), 800, .5, .6), (122, "race-wing", (3, 4), 600, .5, .6),
    (132, "race-rear", (1, 1), 800, .5, .6),
]
os.makedirs(OUT, exist_ok=True)
assert features.check("webp"), "Pillow has no WebP support"
dims = {}
for i, name, (aw, ah), maxw, fx, fy in JOBS:
    im = Image.open(os.path.join(RAW, idx[i]["file"])).convert("RGB")
    w, h = im.size
    cw, ch = (w, round(w * ah / aw)) if w * ah / aw <= h else (round(h * aw / ah), h)
    x = round((w - cw) * fx); y = round((h - ch) * fy)
    im = im.crop((x, y, x + cw, y + ch))
    if cw > maxw:
        im = im.resize((maxw, round(maxw * ah / aw)), Image.LANCZOS)
    p = os.path.join(OUT, name + ".webp")
    im.save(p, "WEBP", quality=76, method=6)
    dims[name] = im.size
json.dump(dims, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "photo-dims.json"), "w"), indent=0)
tot = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT) if f.endswith(".webp"))
print(len(JOBS), "photos,", round(tot / 1024), "KB total")
