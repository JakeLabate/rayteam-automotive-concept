#!/usr/bin/env python3
"""Builds the RayTeam Automotive concept site into ../site as plain, self-contained pages.

Spec mode: this is an unsolicited concept. Every page carries noindex, the staging notice,
and the footer disclosure. Nothing is invented: see content.py for where each fact comes from.
"""
import html
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as c          # noqa: E402
from style import CSS        # noqa: E402

SITE = os.path.join(HERE, "..")   # the repo root is the published site
AREAS = ["Waltham", "Newton", "Cambridge", "Brookline", "Watertown"]


def esc(s):
    return html.escape(s, quote=True)


def url(page):
    return c.BASE if page == "index.html" else c.BASE + page


# ------------------------------------------------------------------ structured data

def business(full=True):
    if not full:
        return None
    return {
        "@type": "AutoRepair", "@id": c.BASE + "#business", "name": c.NAME, "url": c.OFFICIAL,
        "description": "Independent German and European auto repair shop in Waltham, Massachusetts, open since 2009.",
        "telephone": c.TEL_E164,
        "address": {"@type": "PostalAddress", "streetAddress": "175 High St", "addressLocality": "Waltham",
                    "addressRegion": "MA", "postalCode": "02453", "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": 42.3656824, "longitude": -71.2321304},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "13:00"}],
        "areaServed": [{"@type": "City", "name": a} for a in AREAS],
        "sameAs": [u for _, u in c.SOCIAL] + [c.YELP],
    }


def graph(page, title, desc, crumbs, page_type="WebPage", extra=None, full_business=False):
    u = url(page)
    nodes = [
        {"@type": "WebSite", "@id": c.BASE + "#website", "url": c.BASE, "name": "RayTeam Automotive concept site",
         "description": "An unofficial concept site for RayTeam Automotive, proposed by Jake Labate, SEO Consultant.",
         "inLanguage": "en-US", "about": {"@id": c.BASE + "#business"},
         "creator": {"@type": "Person", "name": "Jake Labate", "url": "https://www.jakelabate.com/"}},
        {"@type": page_type, "@id": u + "#webpage", "url": u, "name": title, "description": desc,
         "inLanguage": "en-US", "isPartOf": {"@id": c.BASE + "#website"}, "about": {"@id": c.BASE + "#business"}},
    ]
    if crumbs:
        nodes[1]["breadcrumb"] = {"@id": u + "#breadcrumb"}
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": c.BASE}]
        for i, (href, label) in enumerate(crumbs, start=2):
            item = {"@type": "ListItem", "position": i, "name": label}
            if href:
                item["item"] = url(href)
            items.append(item)
        nodes.append({"@type": "BreadcrumbList", "@id": u + "#breadcrumb", "itemListElement": items})
    if full_business:
        nodes.append(business())
    if extra:
        nodes.extend(extra)
    return json.dumps({"@context": "https://schema.org", "@graph": nodes}, indent=1, ensure_ascii=False)


# ------------------------------------------------------------------ furniture

JS = r"""
(function(){var d=document,H={1:[480,1020],2:[480,1020],3:[480,1020],4:[480,1020],5:[480,1020],6:[540,780]},
N=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
function fmt(m){var h=Math.floor(m/60),mm=m%60,ap=h>=12?'pm':'am';h=h%12||12;return h+':'+(mm<10?'0':'')+mm+' '+ap}
try{var o={};new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'short',hour:'numeric',minute:'numeric',hourCycle:'h23'})
.formatToParts(new Date()).forEach(function(x){o[x.type]=x.value});
var day=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(o.weekday),now=(+o.hour)*60+(+o.minute),t=H[day],
open=!!t&&now>=t[0]&&now<t[1],msg;
if(open){msg='Open now until '+fmt(t[1])}else{var n=day,k=0;if(!(t&&now<t[0])){do{n=(n+1)%7;k++}while(!H[n])}
msg='Closed now. Opens '+(k===0?'today':k===1?'tomorrow':N[n])+' at '+fmt(H[n][0])}
d.querySelectorAll('[data-status]').forEach(function(e){e.setAttribute('data-open',open);e.querySelector('span').textContent=msg});
d.querySelectorAll('.hours tr[data-days]').forEach(function(r){if(r.getAttribute('data-days').split(' ').indexOf(String(day))>-1)r.classList.add('is-today')});
}catch(e){}
d.querySelectorAll('[data-finder]').forEach(function(f){
var tabs=[].slice.call(f.querySelectorAll('[role=tab]')),panels=[].slice.call(f.querySelectorAll('[role=tabpanel]'));
function pick(i,focus){tabs.forEach(function(t,j){var on=j===i;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;panels[j].hidden=!on});if(focus)tabs[i].focus()}
tabs.forEach(function(t,i){t.addEventListener('click',function(){pick(i);
if(window.matchMedia('(max-width:900px)').matches)panels[i].scrollIntoView({block:'nearest'})});
t.addEventListener('keydown',function(e){var k=e.key,n=k==='ArrowDown'||k==='ArrowRight'?i+1:k==='ArrowUp'||k==='ArrowLeft'?i-1:k==='Home'?0:k==='End'?tabs.length-1:null;
if(n!==null){e.preventDefault();pick((n+tabs.length)%tabs.length,true)}})});pick(0)});
var mb=d.querySelector('.menu'),nav=d.getElementById('nav');
if(mb)mb.addEventListener('click',function(){var on=nav.classList.toggle('is-open');mb.setAttribute('aria-expanded',on)});
var cl=d.querySelectorAll('.climb');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-in');io.unobserve(e.target)}})},{threshold:.4});
cl.forEach(function(x){io.observe(x)})}else{cl.forEach(function(x){x.classList.add('is-in')})}
var m=d.querySelector('[data-map]');
if(m)m.querySelector('button').addEventListener('click',function(){m.classList.add('is-live');
m.innerHTML='<iframe title="Map showing RayTeam Automotive at 175 High Street, Waltham" loading="lazy" src="'+m.getAttribute('data-map')+'"></iframe>'});
})();
"""


def head(page, title, desc, ld, og_alt, index=False):
    u = url(page)
    og = f"{c.BASE}img/og/{'index' if page == '404.html' else page[:-5]}.png"
    canonical = "" if page == "404.html" else f'<link rel="canonical" href="{u}">\n'
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{canonical}<meta property="og:type" content="website">
<meta property="og:site_name" content="RayTeam Automotive concept site">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{u}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(og_alt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og}">
<meta name="theme-color" content="#ffcf00">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="stylesheet" href="fonts/fonts.css">
<link rel="preload" as="font" type="font/woff2" href="fonts/sofia-sans-extra-condensed-latin-800-normal.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/sofia-sans-latin-400-normal.woff2" crossorigin>
<script>document.documentElement.className='js'</script>
<style>{CSS}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
"""


def masthead(page):
    section = {"makes.html": "makes.html"}
    for m in c.MAKES:
        section[f"{m[0]}-repair.html"] = "makes.html"
    here = section.get(page, page)
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == here else ""}>{esc(l)}</a></li>' for h, l in c.NAV)
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="notice"><div class="wrap"><b>Staging site.</b><p>A proposal for RayTeam Automotive. The shop's official site is <a href="{c.OFFICIAL}">rayteamgermanauto.com</a>.</p></div></div>
<header class="mast">
<div class="wrap">
<a class="brand" href="index.html">RayTeam <span>Automotive</span></a>
<button class="btn btn--line btn--sm menu" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main"><ul>{items}</ul></nav>
<a class="mast__tel" href="{c.TEL_HREF}">{c.TEL_HUMAN}</a>
<a class="btn btn--sm btn--book" href="{c.BOOK}">Book service</a>
</div>
<div class="flag" aria-hidden="true"></div>
</header>
<main id="main">
"""


def footer():
    hours = "".join(f"<li>{d}, {h.lower() if h == 'Closed' else h}</li>" for d, h, _ in c.HOURS)
    site = "".join(f'<li><a href="{h}">{esc(l)}</a></li>' for h, l in c.NAV[:4] + [("about.html", "About"), ("faq.html", "Questions"), ("contact.html", "Contact")])
    social = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in c.SOCIAL)
    return f"""</main>
<footer class="foot">
<div class="flag" aria-hidden="true"></div>
<div class="wrap">
<div class="foot__grid">
<div><a class="brand" href="index.html">RayTeam <span>Automotive</span></a>
<address>{c.STREET}<br>{c.CITY_LINE}<br><a href="{c.TEL_HREF}">{c.TEL_HUMAN}</a></address></div>
<div><h2>Hours</h2><ul>{hours}</ul></div>
<div><h2>Site</h2><ul>{site}</ul></div>
<div><h2>Elsewhere</h2><ul>{social}<li><a href="{c.GOOGLE_REVIEWS}">Google reviews</a></li><li><a href="{c.OFFICIAL}">Official site</a></li></ul></div>
</div>
<div class="foot__legal">
<p><b>Unofficial concept site.</b> Not affiliated with or commissioned by RayTeam Automotive. The shop's official site is <a href="{c.OFFICIAL}">rayteamgermanauto.com</a>. The phone number and booking link on these pages go to the shop itself.</p>
<p>Concept by <a href="https://www.jakelabate.com/">Jake Labate, SEO Consultant</a>. Facts come from RayTeam's published pages and public race records. This site will be taken down on request.</p>
<p>Audi, BMW, Mercedes-Benz, Porsche, Volkswagen, MINI, Land Rover, Jaguar, Volvo, Unitronic, and LIQUI MOLY are trademarks of their owners. RayTeam Automotive is an independent shop.</p>
</div>
</div>
</footer>
<div class="callbar"><a href="{c.TEL_HREF}">Call the shop</a><a href="{c.BOOK}">Book service</a></div>
<script>{JS}</script>
</body>
</html>
"""


def crumbs_html(crumbs):
    li = '<li><a href="index.html">Home</a></li>'
    for href, label in crumbs:
        li += f'<li><a href="{href}">{esc(label)}</a></li>' if href else f'<li aria-current="page">{esc(label)}</li>'
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{li}</ol></nav>'


def hours_table():
    rows = "".join(f'<tr data-days="{d}"><th scope="row">{n}</th><td>{h}</td></tr>' for n, h, d in c.HOURS)
    return f'<table class="hours"><caption class="skip">Opening hours</caption>{rows}</table>'


def hours_sign(town=True):
    return f"""<aside class="sign" aria-label="Opening hours and address">
<p class="sign__status" data-status data-open="true"><i aria-hidden="true"></i><span>Open Monday to Saturday</span></p>
<div>{hours_table()}<p class="small" style="margin-top:10px">Holiday hours may differ. Call to confirm.</p></div>
<address><b>Waltham</b>{c.STREET}<br>{c.CITY_LINE}<br><a href="{c.MAPS}">Get directions</a></address>
</aside>"""


def distance_sign():
    rows = "".join(f'<tr><th scope="row">{t}</th><td>{d}</td></tr>' for t, d in c.DISTANCES)
    return f"""<div class="sign sign--gold"><div><table class="dist"><caption class="skip">Distance to RayTeam Automotive from nearby towns</caption>{rows}</table></div></div>
<p class="small" style="margin-top:14px">Driving distances to 175 High Street as RayTeam publishes them. Boston is measured from downtown. Brookline drivers make the trip too.</p>"""


def cta(heading="Bring the car in."):
    return f"""<section class="cta" aria-label="Book or call"><div class="wrap">
<h2>{esc(heading)}</h2>
<div class="actions"><a class="btn" href="{c.TEL_HREF}">Call {c.TEL_HUMAN}</a><a class="btn btn--line" href="{c.BOOK}">Book service online</a></div>
</div></section>"""


def climb_svg():
    x0, y0, x1, y1 = 30, 300, 610, 92
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    nx, ny = -dy / L, dx / L
    d = []
    for i in range(156):
        t = (i + 0.5) / 156
        px, py = x0 + dx * t, y0 + dy * t
        d.append(f"M{px - nx * 20:.1f} {py - ny * 20:.1f}L{px + nx * 20:.1f} {py + ny * 20:.1f}")
    return f"""<svg class="climb" viewBox="0 0 640 372" role="img" aria-label="Diagram of the Pikes Peak course: 156 turns over 12.42 miles, climbing from 9,390 feet at the start line to 14,115 feet at the summit.">
<path class="ticks" d="{''.join(d)}"/>
<path class="road" d="M{x0} {y0}L{x1} {y1}"/>
<circle class="dot" cx="{x0}" cy="{y0}" r="11"/><circle class="dot" cx="{x1}" cy="{y1}" r="11"/>
<text x="14" y="356">Start line, 9,390 ft</text>
<text x="626" y="48" text-anchor="end">Summit, 14,115 ft</text>
<text class="big" x="626" y="268" text-anchor="end">156 turns</text>
<text x="626" y="304" text-anchor="end">in 12.42 miles, one tick each</text>
</svg>"""


def write(page, title, desc, body, crumbs=None, page_type="WebPage", extra=None, full_business=False, og_alt=None):
    ld = graph(page, title, desc, crumbs, page_type, extra, full_business)
    doc = head(page, title, desc, ld, og_alt or f"Share card for {title}") + masthead(page) + body + footer()
    assert "—" not in doc, f"em dash in {page}"
    with open(os.path.join(SITE, page), "w", encoding="utf-8") as f:
        f.write(doc)


# ------------------------------------------------------------------ pages

def svc_block(sid, name, summary, paras, when, level="h3"):
    w = f'<p class="when">{esc(when)}</p>' if when else ""
    body = "".join(f"<p>{esc(p)}</p>" for p in paras)
    return f"""<div class="svc" id="{sid}"><div><{level}>{esc(name)}</{level}>{w}</div><div class="stack">{body}</div></div>"""


def home():
    title = "RayTeam Automotive | German Auto Repair in Waltham, MA"
    desc = ("Independent German and European auto repair at 175 High Street, Waltham, since 2009. "
            "Factory diagnostics, OEM parts, and a 24-month warranty on repairs.")
    makes = "".join(f'<li><a href="{m[0]}-repair.html">{esc(m[1])}</a></li>' for m in c.MAKES)
    tabs = "".join(f'<button type="button" role="tab" id="t-{s[0]}" aria-controls="p-{s[0]}" aria-selected="false">{esc(s[1])}</button>' for s in c.SYMPTOMS)
    panels = "".join(
        f'<article role="tabpanel" id="p-{s[0]}" aria-labelledby="t-{s[0]}" class="stack"><h3>{esc(s[2])}</h3>'
        + "".join(f"<p>{esc(p)}</p>" for p in s[3])
        + f'<p><a href="{s[4][0]}">{esc(s[4][1])}</a>, or call <a href="{c.TEL_HREF}">{c.TEL_HUMAN}</a>.</p></article>'
        for s in c.SYMPTOMS)
    svc = "".join(f'<li><a href="services.html#{s[0]}">{esc(s[1])}</a><p>{esc(s[2])}</p></li>' for s in c.SERVICES + c.SPECIALTY)
    journal = "".join(f'<li><a href="{j[4]}">{esc(j[2])}</a><p>{j[1]}, {j[3]}</p></li>' for j in c.JOURNAL)
    body = f"""<section class="hero"><div class="wrap">
<div>
<h1>German and European auto repair in Waltham, MA</h1>
<p class="lede">RayTeam Automotive is an independent shop at 175 High Street that has serviced Audi, BMW, Mercedes-Benz, Porsche, Volkswagen, and other European cars since 2009. Factory diagnostic equipment, OEM parts, and a 24-month, 24,000-mile warranty on approved repairs.</p>
<div class="actions"><a class="btn" href="{c.TEL_HREF}">Call {c.TEL_HUMAN}</a><a class="btn btn--line" href="{c.BOOK}">Book service online</a></div>
</div>
{hours_sign()}
</div></section>

<section class="band" aria-labelledby="h-makes"><div class="wrap">
<div class="head"><h2 id="h-makes">Makes we service</h2>
<p class="lede">Pick your make for the faults the shop sees most and how it fixes them.</p></div>
<ul class="makes">{makes}</ul>
</div></section>

<section class="band band--floor" aria-labelledby="h-finder"><div class="wrap">
<div class="head"><h2 id="h-finder">What is the car doing?</h2>
<p class="lede">Choose the closest match to see what it usually means and which service covers it.</p></div>
<div class="finder" data-finder>
<div class="finder__tabs" role="tablist" aria-label="Symptoms" aria-orientation="vertical">{tabs}</div>
<div class="finder__panels">{panels}</div>
</div>
</div></section>

<section class="band" aria-labelledby="h-services"><div class="wrap">
<div class="head"><h2 id="h-services">Services</h2>
<p class="lede">Routine maintenance, diagnosis, and major repairs, all done in the shop's own service building.</p></div>
<ul class="index">{svc}</ul>
</div></section>

<section class="band band--floor" aria-labelledby="h-dealer"><div class="wrap split">
<div class="stack"><h2 id="h-dealer">Dealer-level work without the dealership</h2>
<p>What an independent shop needs to match a dealer is equipment, parts, and a warranty that says it stands behind both. Here is what RayTeam puts on the record.</p>
<p><a href="about.html">About the shop</a></p></div>
<dl class="facts">
<dt>Diagnostics</dt><dd>Factory diagnostic and repair equipment for Audi, BMW, Mercedes-Benz, and Volkswagen, built up over more than 15 years, including module coding.</dd>
<dt>Parts</dt><dd>OEM and OE-specification parts.</dd>
<dt>Oil</dt><dd>LIQUI MOLY full-synthetic German oil on every oil service.</dd>
<dt>Warranty</dt><dd>24 months or 24,000 miles on approved repairs.</dd>
<dt>Extended warranties</dt><dd>The shop works with every aftermarket warranty company and handles the claim.</dd>
<dt>Workshop</dt><dd>More than a dozen service bays and a team of 10 technicians.</dd>
</dl>
</div></section>

<section class="band on-black" aria-labelledby="h-race"><div class="wrap split split--even">
<div class="stack"><h2 id="h-race">The shop that raced Pikes Peak</h2>
<p class="lede">In June 2024 RayTeam Motorsport made its racing debut at the 102nd Pikes Peak International Hill Climb. Laszlo Keskeny drove the team's number 10 Audi Group B tribute car to the summit in 12:57.142.</p>
<p><a class="btn btn--gold" href="motorsport.html">RayTeam Motorsport</a></p></div>
<figure>{climb_svg()}</figure>
</div></section>

<section class="band" aria-labelledby="h-journal"><div class="wrap split">
<div class="stack"><h2 id="h-journal">From the shop journal</h2>
<p>RayTeam writes up the seasonal faults it sees on local cars. These articles open on the shop's current site.</p></div>
<ul class="index" style="grid-template-columns:1fr">{journal}</ul>
</div></section>

<section class="band band--floor" aria-labelledby="h-reviews"><div class="wrap split">
<div class="stack"><h2 id="h-reviews">What customers say</h2></div>
<div class="stack"><p class="lede">Reviews are best read where customers wrote them. RayTeam's are on Google and Yelp.</p>
<div class="actions"><a class="btn btn--line" href="{c.GOOGLE_REVIEWS}">Read reviews on Google</a><a class="btn btn--line" href="{c.YELP}">Read reviews on Yelp</a></div></div>
</div></section>

<section class="band" aria-labelledby="h-visit"><div class="wrap split split--even">
<div class="stack"><h2 id="h-visit">Six miles from downtown Boston</h2>
<p class="lede">The shop is at 175 High Street in Waltham and draws drivers from Newton, Watertown, Cambridge, Brookline, and Boston.</p>
<div class="actions"><a class="btn" href="{c.MAPS}">Get directions</a><a class="btn btn--line" href="contact.html">Hours and contact</a></div></div>
<div>{distance_sign()}</div>
</div></section>
{cta()}
"""
    write("index.html", title, desc, body, full_business=True,
          og_alt="Share card: RayTeam Automotive, German auto repair in Waltham, MA")


def services():
    title = "Auto Repair Services for German Cars | RayTeam Automotive"
    desc = ("Diagnostics, oil service, brakes, suspension, transmission, engine, electrical, and A/C repair "
            "for German and European cars at RayTeam Automotive, Waltham, MA.")
    crumbs = [(None, "Services")]
    jump = "".join(f'<li><a href="#{s[0]}">{esc(s[1])}</a></li>' for s in c.SERVICES + c.SPECIALTY)
    core = "".join(svc_block(*s) for s in c.SERVICES)
    spec = "".join(svc_block(*s) for s in c.SPECIALTY)
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>Services for German and European cars</h1>
<p class="lede">RayTeam Automotive handles routine maintenance, diagnosis, and major repairs at 175 High Street in Waltham. Approved repairs carry a 24-month, 24,000-mile warranty.</p>
</div></section>
<section class="band"><div class="wrap">
<nav aria-label="Services on this page"><ul class="jump">{jump}</ul></nav>
</div></section>
<section class="band" style="padding-top:0" aria-labelledby="h-core"><div class="wrap">
<div class="head"><h2 id="h-core">Repair and maintenance</h2></div>
{core}
</div></section>
<section class="band band--floor" aria-labelledby="h-spec"><div class="wrap">
<div class="head"><h2 id="h-spec">Specialty work</h2>
<p class="lede">Jobs that need factory equipment or a specific process. Performance software and hardware have their own page: <a href="tuning.html">Unitronic tuning</a>.</p></div>
{spec}
</div></section>
{cta("Not sure which service you need?")}
"""
    write("services.html", title, desc, body, crumbs, og_alt="Share card: services for German and European cars at RayTeam Automotive")


def makes_hub():
    title = "European Makes We Service in Waltham | RayTeam Automotive"
    desc = ("RayTeam Automotive services Audi, BMW, Mercedes-Benz, Porsche, Volkswagen, MINI, Land Rover, "
            "Jaguar, and Volvo in Waltham, MA. See common faults for your make.")
    crumbs = [(None, "Makes")]
    items = "".join(f'<li><a href="{m[0]}-repair.html">{esc(m[1])} repair and service</a><p>{esc(m[2])}</p></li>' for m in c.MAKES)
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>Makes we service in Waltham</h1>
<p class="lede">RayTeam Automotive has specialized in German cars since 2009 and services nine European makes. Each page covers the faults the shop sees most on that make and how it repairs them.</p>
</div></section>
<section class="band"><div class="wrap">
<ul class="index">{items}</ul>
<p class="small" style="margin-top:28px">The shop holds factory diagnostic and repair equipment for Audi, BMW, Mercedes-Benz, and Volkswagen, and uses Porsche's factory tester on Porsche gearbox faults.</p>
</div></section>
{cta()}
"""
    write("makes.html", title, desc, body, crumbs, og_alt="Share card: European makes serviced by RayTeam Automotive in Waltham")


def make_page(m):
    slug, name, short, lede, issue_h, issues, links, jkey, _ = m
    page = f"{slug}-repair.html"
    title = f"{name} Repair in Waltham, MA | RayTeam Automotive"
    desc = f"{name} repair in Waltham, MA at RayTeam Automotive. {short} OEM parts and a 24-month repair warranty."
    crumbs = [("makes.html", "Makes"), (None, name)]
    iss = "".join(f"<li><h3>{esc(t)}</h3><p>{esc(x)}</p></li>" for t, x in issues)
    lk = "".join(f'<li><a href="{h}">{esc(l)}</a></li>' for h, l in links)
    j = [x for x in c.JOURNAL if x[0] == jkey]
    journal = (f'<p>From the shop journal: <a href="{j[0][4]}">{esc(j[0][2])}</a>, on RayTeam\'s current site.</p>' if j else "")
    others = "".join(f'<li><a href="{o[0]}-repair.html">{esc(o[1])}</a></li>' for o in c.MAKES if o[0] != slug)
    extra = [{"@type": "Service", "@id": url(page) + "#service", "name": f"{name} repair and service",
              "serviceType": f"{name} repair", "url": url(page), "provider": {"@id": c.BASE + "#business"},
              "areaServed": [{"@type": "City", "name": a} for a in AREAS]}]
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>{esc(name)} repair and service in Waltham, MA</h1>
<p class="lede">{esc(lede)}</p>
<div class="actions" style="margin-top:28px"><a class="btn" href="{c.TEL_HREF}">Call {c.TEL_HUMAN}</a><a class="btn btn--line" href="{c.BOOK}">Book service online</a></div>
</div></section>
<section class="band" aria-labelledby="h-issues"><div class="wrap split">
<div class="stack"><h2 id="h-issues">{esc(issue_h)}</h2>
<p>Approved repairs carry a 24-month, 24,000-mile warranty.</p></div>
<ul class="issues">{iss}</ul>
</div></section>
<section class="band band--floor" aria-labelledby="h-svc"><div class="wrap split">
<div class="stack"><h2 id="h-svc">Service for your {esc(name)}</h2>
<p>Every service the shop offers applies to {esc(name)}. These are the ones owners ask about most.</p>
{journal}</div>
<div><ul class="index">{lk}<li><a href="services.html">All services</a></li><li><a href="faq.html">Common questions</a></li></ul></div>
</div></section>
<section class="band" aria-labelledby="h-other"><div class="wrap">
<div class="head"><h2 id="h-other">Other makes</h2></div>
<ul class="makes" style="font-size:clamp(2.2rem,4.6vw,4rem)">{others}</ul>
</div></section>
{cta(f"Book your {name} in.")}
"""
    write(page, title, desc, body, crumbs, extra=extra, og_alt=f"Share card: {name} repair in Waltham, MA at RayTeam Automotive")


def tuning():
    title = "Unitronic Tuning in Waltham, MA | RayTeam Automotive"
    desc = ("RayTeam Automotive is an authorized Unitronic dealer in Waltham, MA, installing ECU and TCU "
            "software and performance hardware for Audi, Volkswagen, and Porsche.")
    crumbs = [(None, "Tuning")]
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>Unitronic tuning and performance upgrades</h1>
<p class="lede">RayTeam Automotive is an authorized Unitronic dealer. The shop installs Unitronic engine and transmission software, and the hardware that supports it, for Audi, Volkswagen, and Porsche.</p>
</div></section>
<section class="band"><div class="wrap split split--prose">
<div class="prose">
<h2>Software</h2>
<p>Unitronic writes performance software for the engine control unit (ECU) and the transmission control unit (TCU). Each file is matched to the supporting modifications already on the car.</p>
<p>The gains RayTeam describes are faster acceleration and more horsepower and torque, with the factory safety tables in the ECU kept in place.</p>
<h2>Hardware</h2>
<p>The shop fits exhausts, intakes, intercoolers, and turbo upgrades, along with performance exhaust systems, wheels, suspension, and interior and exterior accessories. It also takes on custom engine work.</p>
<p>Every modification is tested on the shop's own computers and diagnostic equipment before the car goes back to its owner.</p>
<h2>Oil for a tuned engine</h2>
<p>A tuned engine asks more of its oil. RayTeam uses LIQUI MOLY full-synthetic German oil and nothing else.</p>
<p><a href="https://www.getunitronic.com/locate-a-dealer/Rayteam-Inc">RayTeam's listing in the Unitronic dealer locator</a></p>
</div>
<dl class="facts">
<dt>Dealer status</dt><dd>Authorized Unitronic dealer, listed at 175 High Street, Waltham.</dd>
<dt>Platforms</dt><dd>Audi, Volkswagen, and Porsche.</dd>
<dt>Software</dt><dd>ECU and TCU calibrations, matched to the car's modifications.</dd>
<dt>Hardware</dt><dd>Exhausts, intakes, intercoolers, turbo upgrades, wheels, and suspension.</dd>
<dt>Maintenance</dt><dd><a href="services.html#dsg-service">DSG service</a> every 40,000 miles and <a href="services.html#carbon-cleaning">carbon cleaning</a> keep a tuned car healthy.</dd>
</dl>
</div></section>
{cta("Talk to the shop about your build.")}
"""
    write("tuning.html", title, desc, body, crumbs, og_alt="Share card: Unitronic tuning at RayTeam Automotive in Waltham, MA")


def motorsport():
    title = "RayTeam Motorsport | Pikes Peak Hill Climb Race Team"
    desc = ("RayTeam Motorsport, the race team of RayTeam Automotive in Waltham, MA, debuted at the 2024 "
            "Pikes Peak International Hill Climb in an Audi Group B tribute car.")
    crumbs = [(None, "Motorsport")]
    src = "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for t, u in c.SOURCES_MOTORSPORT)
    body = f"""<section class="page-hero page-hero--black on-black"><div class="wrap">{crumbs_html(crumbs)}
<h1>RayTeam Motorsport</h1>
<p class="lede">The race team of RayTeam Automotive. Its first race was the 2024 Pikes Peak International Hill Climb, in an Audi Group B tribute car built and driven by Laszlo Keskeny.</p>
</div></section>
<section class="band on-black" style="padding-top:0" aria-labelledby="h-time"><div class="wrap split split--even">
<div class="stack"><h2 id="h-time" class="skip">Pikes Peak 2024 result</h2>
<p class="time">12:57.142</p>
<p class="lede">Official time at the 102nd Pikes Peak International Hill Climb on June 23, 2024. Car number 10, Pikes Peak Open division, 14th in class.</p>
<p class="small">The course climbs 4,725 feet at an average grade of about 7 percent.</p></div>
<figure>{climb_svg()}</figure>
</div></section>
<section class="band" aria-labelledby="h-record"><div class="wrap split">
<div class="stack"><h2 id="h-record">Race record</h2>
<p>Two seasons in, the team has gone from one car to two.</p></div>
<ol class="timeline">
<li><time datetime="2024-06-23">June 23, 2024</time><div><h3>102nd Pikes Peak International Hill Climb, Colorado</h3>
<p>The team's first race. Laszlo Keskeny, a Pikes Peak rookie, drove a 1986 Audi 4000 built as a Group B Audi Sport Quattro tribute to the summit in 12:57.142, 14th in the Pikes Peak Open division.</p></div></li>
<li><time datetime="2024-09-07">September 7, 2024</time><div><h3>Mt. Ascutney Hillclimb, Vermont</h3>
<p>Second event on the team's 2024 calendar.</p></div></li>
<li><time datetime="2024-10-20">October 20, 2024</time><div><h3>Okemo Hillclimb, Vermont</h3>
<p>Third event on the team's 2024 calendar.</p></div></li>
<li><time datetime="2025-06">June 2025</time><div><h3>103rd Pikes Peak International Hill Climb, Colorado</h3>
<p>The second campaign grew from one Group B tribute car to two. Rookie Alex Kim entered an Audi S1 E2 tribute with the team, as RACER reported ahead of the race.</p></div></li>
</ol>
</div></section>
<section class="band band--floor" aria-labelledby="h-cars"><div class="wrap split">
<div class="stack"><h2 id="h-cars">The cars</h2></div>
<div class="prose">
<h3 style="margin-top:0">1986 Audi S1 E2</h3>
<p>The S1 E2 was Audi's Group B rally car: a turbocharged five-cylinder engine and all-wheel drive in a short, wide body with a large rear wing. The team's car is a tribute to it, and it is the shape that climbed Pikes Peak in 2024.</p>
<h3>1987 Audi UR Quattro</h3>
<p>The road car that started it. The original Quattro put all-wheel drive into a performance coupe and changed rallying.</p>
<p>Race footage is on the team's <a href="https://www.youtube.com/@Rayteammotorsport">YouTube channel</a>, and sponsorship details are at <a href="https://rayteammotorsport.com/">rayteammotorsport.com</a>.</p>
</div>
</div></section>
<section class="band" aria-labelledby="h-src"><div class="wrap split">
<div class="stack"><h2 id="h-src">Sources</h2></div>
<ul class="index" style="grid-template-columns:1fr">{src}</ul>
</div></section>
{cta("The same shop services your car.")}
"""
    write("motorsport.html", title, desc, body, crumbs, og_alt="Share card: RayTeam Motorsport, Pikes Peak hill climb race team")


def about():
    title = "About RayTeam Automotive | Waltham German Auto Shop"
    desc = ("RayTeam Automotive has repaired German and European cars at 175 High Street, Waltham, since 2009: "
            "factory diagnostics, OEM parts, a 24-month repair warranty.")
    crumbs = [(None, "About")]
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>An independent German auto shop in Waltham since 2009</h1>
<p class="lede">RayTeam Automotive is led by Frank Ocsai and works from its own service building at 175 High Street, six miles from downtown Boston.</p>
</div></section>
<section class="band"><div class="wrap split split--prose">
<div class="prose">
<h2>How the work gets done</h2>
<p>Every job starts with a diagnosis. The shop's factory equipment lets a technician form a test plan, read the car's state of health, and find the efficient path to the repair. Parts go on after the cause is confirmed.</p>
<p>Repairs use OEM and OE-specification parts. When a new part has to be coded to the car, that happens in the same building.</p>
<h2>The warranty and the guarantee</h2>
<p>Approved repairs carry a 24-month, 24,000-mile warranty.</p>
<p>RayTeam also publishes a 100% satisfaction guarantee. If you are unsatisfied with the work, the shop refunds what you spent on that service.</p>
<h2>Partners</h2>
<p>RayTeam is an authorized dealer for Unitronic performance software and hardware, and it runs LIQUI MOLY full-synthetic German oil in every car it services. See <a href="tuning.html">Unitronic tuning</a>.</p>
<h2>Racing</h2>
<p>In 2024 the shop formed RayTeam Motorsport and entered its first race, the Pikes Peak International Hill Climb. Read the <a href="motorsport.html">race record</a>.</p>
</div>
<dl class="facts">
<dt>Founded</dt><dd>2009</dd>
<dt>Address</dt><dd>{c.STREET}, {c.CITY_LINE}</dd>
<dt>Workshop</dt><dd>More than a dozen service bays in the shop's own service building.</dd>
<dt>Team</dt><dd>10 technicians trained on European and luxury cars.</dd>
<dt>Equipment</dt><dd>Dealer-level diagnostic tools and factory-specific scanners.</dd>
<dt>Makes</dt><dd>Audi, BMW, Mercedes-Benz, Porsche, Volkswagen, MINI, Land Rover, Jaguar, and Volvo. <a href="makes.html">See each make</a>.</dd>
<dt>Extended warranties</dt><dd>Works with every aftermarket warranty company.</dd>
</dl>
</div></section>
{cta()}
"""
    write("about.html", title, desc, body, crumbs, page_type="AboutPage", full_business=True,
          og_alt="Share card: about RayTeam Automotive, a German auto shop in Waltham since 2009")


def faq():
    title = "German Auto Repair FAQ | RayTeam Automotive, Waltham"
    desc = ("Answers about makes serviced, OEM parts, the 24-month repair warranty, DSG service, check engine "
            "lights, and booking at RayTeam Automotive in Waltham, MA.")
    crumbs = [(None, "Questions")]
    items = "".join(f"<details><summary>{esc(q)}</summary><div><p>{esc(a)}</p></div></details>" for q, a in c.FAQS)
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>Questions drivers ask before they book</h1>
<p class="lede">Short answers about what RayTeam Automotive services, how it repairs, and what the work is backed by.</p>
</div></section>
<section class="band"><div class="wrap split">
<div class="stack"><h2>Answers</h2>
<p>Still unsure? Call <a href="{c.TEL_HREF}">{c.TEL_HUMAN}</a> and describe what the car is doing.</p></div>
<div class="faq">{items}</div>
</div></section>
{cta()}
"""
    write("faq.html", title, desc, body, crumbs, og_alt="Share card: common questions about RayTeam Automotive")


def contact():
    title = "Contact and Directions | RayTeam Automotive, Waltham"
    desc = ("Call (781) 209-1400, book online, or visit RayTeam Automotive at 175 High Street, Waltham, MA. "
            "Open Monday to Friday 8 to 5 and Saturday 9 to 1.")
    crumbs = [(None, "Contact")]
    social = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in c.SOCIAL)
    body = f"""<section class="page-hero"><div class="wrap">{crumbs_html(crumbs)}
<h1>Contact RayTeam Automotive</h1>
<p class="lede">Call, book online, or come by 175 High Street in Waltham. Describe what the car is doing and the shop will tell you what it takes to fix it.</p>
<div class="actions" style="margin-top:28px"><a class="btn" href="{c.TEL_HREF}">Call {c.TEL_HUMAN}</a><a class="btn btn--line" href="{c.BOOK}">Book service online</a><a class="btn btn--line" href="{c.MAPS}">Get directions</a></div>
</div></section>
<section class="band"><div class="wrap split split--even">
<div>{hours_sign()}</div>
<div><div class="map" data-map="{c.MAPS_EMBED}"><div class="stack"><p><b>{c.STREET}, {c.CITY_LINE}</b></p><p><button class="btn btn--line" type="button">Show the map</button></p><p class="small">The map loads from Google when you ask for it.</p></div></div></div>
</div></section>
<section class="band band--floor" aria-labelledby="h-area"><div class="wrap split split--even">
<div class="stack"><h2 id="h-area">Where drivers come from</h2>
<p>The shop serves Waltham and the towns around it. It is six miles from downtown Boston.</p>
<h3>Follow the shop</h3><ul class="stack" style="margin-top:.4em">{social}</ul></div>
<div>{distance_sign()}</div>
</div></section>
"""
    write("contact.html", title, desc, body, crumbs, page_type="ContactPage", full_business=True,
          og_alt="Share card: contact and directions for RayTeam Automotive in Waltham")


def notfound():
    title = "Page not found | RayTeam Automotive"
    desc = "That page does not exist on the RayTeam Automotive concept site. Head back to the home page or call the shop."
    body = f"""<section class="band"><div class="wrap stack">
<h1 class="skip">Page not found</h1>
<div class="sign sign--gold exit" aria-hidden="true">
<p class="display">RayTeam Automotive</p>
<p class="display exit__gone">The page you wanted</p>
</div>
<p class="lede">That page is not here. The shop is.</p>
<div class="actions"><a class="btn" href="index.html">Go to the home page</a><a class="btn btn--line" href="services.html">See services</a><a class="btn btn--line" href="{c.TEL_HREF}">Call {c.TEL_HUMAN}</a></div>
</div></section>
"""
    write("404.html", title, desc, body, og_alt="Share card: page not found")


def main():
    os.makedirs(SITE, exist_ok=True)
    home(); services(); makes_hub()
    for m in c.MAKES:
        make_page(m)
    tuning(); motorsport(); about(); faq(); contact(); notfound()
    with open(os.path.join(SITE, "robots.txt"), "w") as f:
        f.write("User-agent: *\nDisallow: /\n\nSitemap: https://rayteam.jakelabate.com/sitemap.xml\n")
    with open(os.path.join(SITE, "CNAME"), "w") as f:
        f.write("rayteam.jakelabate.com\n")
    open(os.path.join(SITE, ".nojekyll"), "w").close()
    print("built", len([p for p in os.listdir(SITE) if p.endswith(".html")]), "pages")


if __name__ == "__main__":
    main()
