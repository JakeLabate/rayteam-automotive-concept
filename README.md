# RayTeam Automotive concept site

An unofficial concept site for RayTeam Automotive (175 High Street, Waltham, MA), proposed by
Jake Labate, SEO Consultant. Not affiliated with or commissioned by RayTeam Automotive.
The shop's official site is https://rayteamgermanauto.com/.

Published at https://rayteam.jakelabate.com/ from the root of this repository.

## Spec mode

Every page carries `noindex, nofollow`, the staging notice, and the footer disclosure, and
`robots.txt` disallows all crawling, so the concept never competes with the shop in search.
It will be taken down on request.

## Rebuilding

The pages are generated. Edit `_src/content.py` (facts and copy) or `_src/style.py` (CSS), then:

```bash
python3 _src/build.py
```

Share cards in `img/og/` are rendered from each page's title and description. Re-render them
after any change to a title, description, palette, or font.

## Photos and video

`img/photos/` holds the shop's own photographs, taken from the media libraries of
rayteamgermanauto.com and rayteammotorsport.com, then cropped and compressed by `_src/photos.py`.
Stock, AI-generated, manufacturer, sponsor, and third-party images were left out. Videos are
click-to-load embeds from the shop's own YouTube channel. The originals are not in this repo.

## Sources

Business facts come from RayTeam's own published pages. Race results come from the Pikes Peak
International Hill Climb's official results and reporting by RACER. See `_src/content.py`.
