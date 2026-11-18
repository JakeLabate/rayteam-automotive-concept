"""Site stylesheet. Every colour is a :root token that passed check_contrast.py --palette."""

CSS = r"""
:root{
  --black:#000000; --text:#1f1f1f; --paper:#ffffff; --floor:#eceeef;
  --gold:#ffcf00; --red:#e02b20; --steel:#50565c; --ash:#c2c7cb; --mist:#d3d7da;
  --display:'Sofia Sans Extra Condensed','Sofia Sans Extra Condensed Fallback',Arial,sans-serif;
  --body:'Sofia Sans','Sofia Sans Fallback',Arial,sans-serif;
  --wrap:1240px; --gutter:clamp(20px,4vw,48px); --band:clamp(64px,9vw,120px);
  --radius:14px; --rule:3px;
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:96px}
body{margin:0;background:var(--paper);color:var(--text);font:400 1.125rem/1.55 var(--body);font-variant-numeric:lining-nums}
img,svg{display:block;max-width:100%}
a{color:inherit;text-decoration-thickness:1px;text-underline-offset:.18em}
a:hover{background:var(--gold);color:var(--black)}
:focus-visible{outline:3px solid var(--black);outline-offset:3px;border-radius:2px}
.on-black :focus-visible,.notice :focus-visible,.foot :focus-visible{outline-color:var(--gold)}
h1,h2,h3,p,ul,ol,dl,dd,figure{margin:0}
ul,ol{padding:0;list-style:none}
h1,h2,.display{font-family:var(--display);font-weight:800;color:var(--black);line-height:.92;letter-spacing:-.005em;text-wrap:balance}
h1{font-size:clamp(3.5rem,8.4vw,8.25rem)}
h2{font-size:clamp(2.75rem,5.4vw,4.75rem)}
h3{font:700 1.3rem/1.25 var(--body);color:var(--black)}
p{max-width:68ch}
.lede{font-size:clamp(1.2rem,1.6vw,1.4rem);line-height:1.45;max-width:56ch}
.small{font-size:.94rem;line-height:1.5;color:var(--steel)}
.wrap{max-width:var(--wrap);margin:0 auto;padding-inline:var(--gutter)}
.band{padding-block:var(--band)}
.band--floor{background:var(--floor)}
.stack>*+*{margin-top:1.1em}
.head{display:grid;gap:18px;margin-bottom:clamp(32px,4vw,56px)}
.skip{position:absolute;left:-9999px;top:0;background:var(--gold);color:var(--black);padding:10px 14px;font-weight:700;z-index:50}
.skip:focus{left:8px;top:8px}

/* staging notice: the first element on every page */
.notice{background:var(--black);color:var(--paper);font-size:.9rem;line-height:1.4}
.notice .wrap{padding-block:8px;display:flex;flex-wrap:wrap;gap:4px 8px}
.notice b{font-weight:700;color:var(--gold)}
.notice p{max-width:none}
.notice a:hover{color:var(--black)}

/* masthead */
.mast{background:var(--paper);position:sticky;top:0;z-index:20}
.mast .wrap{display:flex;align-items:center;gap:24px;min-height:72px}
.brand{font:800 2rem/1 var(--display);color:var(--black);text-decoration:none;letter-spacing:.005em;white-space:nowrap;margin-right:auto}
.brand span{font-weight:700;color:var(--steel)}
.brand:hover span{color:var(--black)}
.nav ul{display:flex;gap:4px}
.nav a{display:block;padding:10px 12px;font-weight:600;font-size:1rem;text-decoration:none;border-radius:4px}
.nav a[aria-current="page"]{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:.35em}
.mast__tel{font-weight:700;white-space:nowrap;text-decoration:none}
.mast .menu{display:none}
.flag{height:12px;background:linear-gradient(var(--black) 0 33.33%,var(--red) 0 66.66%,var(--gold) 0)}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:12px 22px;border:var(--rule) solid var(--black);border-radius:6px;background:var(--black);color:var(--paper);font:700 1.05rem/1.1 var(--body);text-decoration:none;cursor:pointer}
.btn:hover{background:var(--paper);color:var(--black)}
.btn--line{background:transparent;color:var(--black)}
.btn--line:hover{background:var(--black);color:var(--paper)}
.btn--gold{background:var(--gold);border-color:var(--gold);color:var(--black)}
.btn--gold:hover{background:var(--paper);border-color:var(--paper);color:var(--black)}
.btn--ghost{background:transparent;border-color:var(--paper);color:var(--paper)}
.btn--ghost:hover{background:var(--paper);color:var(--black)}
.btn--sm{min-height:44px;padding:8px 16px;font-size:1rem}
.actions{display:flex;flex-wrap:wrap;gap:12px}

/* hero: one gold field, the loud moment */
.hero{background:var(--gold);color:var(--text)}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(300px,.85fr);gap:clamp(32px,5vw,72px);align-items:end;padding-block:clamp(40px,5vw,72px) clamp(48px,6vw,88px)}
.hero h1{font-size:clamp(3.4rem,7.4vw,7rem);margin-bottom:.26em}
.hero .lede{margin-bottom:1.6em}
.hero a:hover{background:var(--black);color:var(--paper)}
.hero .btn:hover{background:var(--paper);color:var(--black)}
.hero .btn--line:hover{background:var(--black);color:var(--paper)}
.page-hero{background:var(--floor)}
.page-hero .wrap{padding-block:clamp(40px,6vw,88px)}
.page-hero h1{font-size:clamp(3rem,6.6vw,6.25rem);max-width:16ch;margin-bottom:.3em}
.page-hero--black{background:var(--black);color:var(--paper)}
.page-hero--black h1{color:var(--paper)}
.crumbs{font-size:.94rem;margin-bottom:28px}
.crumbs ol{display:flex;flex-wrap:wrap;gap:6px}
.crumbs li+li::before{content:"/";margin-right:6px;color:var(--steel)}
.page-hero--black .crumbs li+li::before{color:var(--ash)}
.crumbs [aria-current]{font-weight:700}

/* sign panels: bordered, rounded, divided like road signage */
.sign{background:var(--paper);color:var(--black);border:var(--rule) solid var(--black);border-radius:var(--radius);overflow:hidden}
.sign>*{padding:18px 22px}
.sign>*+*{border-top:var(--rule) solid var(--black)}
.sign__status{background:var(--black);color:var(--paper);font-weight:700;display:flex;align-items:center;gap:10px}
.sign__status i{flex:none;width:12px;height:12px;border-radius:50%;background:var(--gold)}
.sign__status[data-open="false"] i{background:var(--red)}
.sign--gold{background:var(--gold)}
.hours{width:100%;border-collapse:collapse;font-size:1.06rem}
.hours th{text-align:left;font-weight:400;padding:3px 12px 3px 0}
.hours td{text-align:right;padding:3px 0;font-variant-numeric:tabular-nums lining-nums;white-space:nowrap}
.hours tr.is-today th,.hours tr.is-today td{font-weight:700}
.sign address{font-style:normal;font-size:1.06rem}
.sign address b{display:block;font:800 2.4rem/1 var(--display);margin-bottom:6px}
.dist{width:100%;border-collapse:collapse}
.dist th{text-align:left;font:800 clamp(2rem,3.4vw,2.9rem)/1.05 var(--display);padding:6px 16px 6px 0}
.dist td{text-align:right;font:800 clamp(2rem,3.4vw,2.9rem)/1.05 var(--display);white-space:nowrap}

/* makes wall */
.makes{display:flex;flex-wrap:wrap;gap:.06em .42em;font:800 clamp(3rem,7.6vw,7rem)/.94 var(--display);color:var(--black)}
.makes li{display:flex;gap:.42em}
.makes li:not(:last-child)::after{content:"/";color:var(--mist)}
.makes a{text-decoration:none}

/* symptom finder */
.finder{display:grid;grid-template-columns:minmax(240px,.8fr) minmax(0,1.4fr);gap:clamp(20px,3vw,40px);align-items:start}
.finder__tabs{display:grid;gap:8px}
.finder__tabs button{appearance:none;text-align:left;font:600 1.1rem/1.2 var(--body);color:var(--black);background:var(--paper);border:var(--rule) solid var(--black);border-radius:6px;padding:14px 16px;cursor:pointer;min-height:52px}
.finder__tabs button:hover{background:var(--gold)}
.finder__tabs button[aria-selected="true"]{background:var(--black);color:var(--paper)}
.finder__panels>*{background:var(--paper);border:var(--rule) solid var(--black);border-radius:var(--radius);padding:clamp(22px,3vw,36px)}
.finder__panels p{font-size:1.2rem}
.finder__panels h3{font:800 clamp(2rem,3.2vw,2.75rem)/1 var(--display);margin-bottom:.45em}
.js .finder__panels>[hidden]{display:none}
.no-js .finder{grid-template-columns:1fr}
.no-js .finder__tabs{display:none}
.no-js .finder__panels{display:grid;gap:16px}

/* service index and long-form lists */
.index{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 clamp(32px,5vw,72px)}
.index li{padding:16px 0;border-top:1px solid var(--black)}
.index a{font-weight:700;font-size:1.2rem;color:var(--black)}
.index p{color:var(--steel);font-size:1rem;margin-top:2px}
.split{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr);gap:clamp(28px,5vw,80px);align-items:start}
.split--even{grid-template-columns:repeat(2,minmax(0,1fr))}
.split--prose{grid-template-columns:minmax(0,1.2fr) minmax(0,1fr)}
.facts{display:grid;grid-template-columns:minmax(150px,.5fr) minmax(0,1.5fr);gap:0 28px}
.facts dt{font-weight:700;color:var(--black);padding:16px 0;border-top:1px solid var(--black)}
.facts dd{padding:16px 0;border-top:1px solid var(--black)}
.prose h2{font-size:clamp(2.4rem,4.2vw,3.6rem);margin:1.5em 0 .35em}
.prose h2:first-child{margin-top:0}
.prose h3{margin:1.6em 0 .3em}
.prose p+p,.prose ul+p,.prose p+ul{margin-top:.9em}
.prose ul{list-style:disc;padding-left:1.2em;max-width:66ch}
.prose li+li{margin-top:.3em}
.svc{padding:clamp(28px,4vw,44px) 0;border-top:1px solid var(--black);display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.4fr);gap:12px clamp(28px,5vw,80px)}
.svc h2,.svc h3{font:800 clamp(2rem,3.4vw,2.9rem)/1 var(--display);margin:0}
.svc .when{display:inline-block;margin-top:14px;padding:6px 12px;border:var(--rule) solid var(--black);border-radius:6px;background:var(--gold);color:var(--black);font-weight:700;font-size:1rem}
.jump{display:flex;flex-wrap:wrap;gap:8px}
.jump a{display:block;padding:8px 14px;border:1px solid var(--black);border-radius:999px;text-decoration:none;font-weight:600;font-size:1rem;background:var(--paper)}
.issues{display:grid;gap:0}
.issues>li{padding:22px 0;border-top:1px solid var(--black)}
.issues h3{margin-bottom:.3em}
.cards2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 clamp(24px,3vw,48px)}
.cards2 li{padding:18px 0;border-top:1px solid var(--black)}
.cards2 a{font-weight:700;color:var(--black)}

/* black bands */
.on-black{background:var(--black);color:var(--paper)}
.on-black h2,.on-black h3,.on-black .display{color:var(--paper)}
.on-black .small{color:var(--ash)}
.on-black a:hover{color:var(--black)}
.on-black .btn--gold:hover{color:var(--black)}
.climb{width:100%;height:auto}
.climb .road{stroke:var(--gold);stroke-width:6;fill:none;stroke-linecap:round}
.climb .dot{fill:var(--red)}
.climb text{fill:var(--paper);font:700 25px var(--body)}
.climb .big{font:800 66px var(--display);fill:var(--gold)}
.climb .ticks{stroke:var(--paper);stroke-width:1.4;fill:none;transition:clip-path 1.8s cubic-bezier(.3,.1,.2,1)}
.js .climb:not(.is-in) .ticks{clip-path:inset(0 100% 0 0)}
.climb.is-in .ticks{clip-path:inset(0 0 0 0)}
.time{font:800 clamp(4.5rem,11vw,10rem)/.85 var(--display);color:var(--gold)}
.timeline li{display:grid;grid-template-columns:minmax(120px,.34fr) minmax(0,1fr);gap:8px 32px;padding:24px 0;border-top:1px solid var(--black)}
.timeline time{font:800 1.9rem/1.05 var(--display);color:var(--black)}
.timeline h3{margin-bottom:.3em}

/* faq */
.faq details{border-top:1px solid var(--black)}
.faq details:last-child{border-bottom:1px solid var(--black)}
.faq summary{cursor:pointer;padding:20px 44px 20px 0;font:700 1.25rem/1.3 var(--body);color:var(--black);list-style:none;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:6px;top:14px;font:800 2.2rem/1 var(--display)}
.faq details[open] summary::after{content:"\2212"}
.faq summary:hover{background:var(--gold)}
.faq details>div{padding:0 0 24px}

/* 404: a town exit sign, the page you asked for struck through */
.exit{max-width:560px}
.exit>*{padding:26px 28px}
.exit .display{font-size:clamp(2.6rem,6vw,4.25rem)}
.exit__gone{position:relative}
.exit__gone::after{content:"";position:absolute;inset:0;background:linear-gradient(to top right,transparent calc(50% - 6px),var(--red) calc(50% - 6px),var(--red) calc(50% + 6px),transparent calc(50% + 6px))}

/* map facade */
.map{border:var(--rule) solid var(--black);border-radius:var(--radius);overflow:hidden;background:var(--floor);min-height:340px;display:grid;place-items:center;text-align:center;padding:28px}
.map iframe{width:100%;height:420px;border:0;display:block}
.map.is-live{padding:0}

/* closing call band */
.cta{background:var(--gold);color:var(--black)}
.cta .wrap{display:flex;flex-wrap:wrap;gap:24px 48px;align-items:end;justify-content:space-between;padding-block:clamp(48px,6vw,80px)}
.cta h2{max-width:14ch}
.cta .btn:hover{background:var(--paper);color:var(--black)}
.cta .btn--line:hover{background:var(--black);color:var(--paper)}

/* footer */
.foot{background:var(--black);color:var(--paper);font-size:1rem}
.foot .wrap{padding-block:clamp(48px,6vw,80px) 28px}
.foot__grid{display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:32px clamp(24px,4vw,56px)}
.foot h2{font:700 1rem/1.3 var(--body);color:var(--ash);letter-spacing:0;margin-bottom:12px}
.foot .brand{color:var(--paper);font-size:2.4rem;display:inline-block;margin-bottom:14px}
.foot .brand span{color:var(--ash)}
.foot .brand:hover{color:var(--black)}.foot .brand:hover span{color:var(--black)}
.foot address{font-style:normal}
.foot li+li{margin-top:6px}
.foot a:hover{color:var(--black)}
.foot__legal{margin-top:48px;padding-top:20px;border-top:1px solid var(--steel);color:var(--ash);font-size:.92rem;display:grid;gap:8px}
.foot__legal p{max-width:none}
.foot__legal b{color:var(--paper)}

/* mobile action bar */
.callbar{display:none}

@media (max-width:1100px){
  .mast__tel{display:none}
  .nav a{padding:10px 8px}
}
@media (max-width:900px){
  .hero .wrap,.finder,.split,.split--even,.split--prose,.svc,.foot__grid{grid-template-columns:1fr}
  .index,.cards2{grid-template-columns:1fr}
  .facts{grid-template-columns:1fr}
  .facts dd{border-top:0;padding-top:0}
  .facts dt{padding-bottom:4px}
  .timeline li{grid-template-columns:1fr}
  .mast .menu{display:inline-flex}
  .mast .btn--book{display:none}
  .js .nav{display:none;position:absolute;left:0;right:0;top:100%;background:var(--paper);border-bottom:var(--rule) solid var(--black);padding:8px var(--gutter) 20px}
  .js .nav.is-open{display:block}
  .nav ul{flex-direction:column;gap:0}
  .nav a{padding:14px 4px;font-size:1.2rem;border-top:1px solid var(--mist);border-radius:0}
  .no-js .mast .wrap{flex-wrap:wrap;padding-block:10px}
  .no-js .nav ul{flex-direction:row;flex-wrap:wrap}
  .no-js .nav a{border:0;padding:8px 10px 8px 0;font-size:1rem}
  .finder__tabs{grid-template-columns:1fr 1fr}
  .finder__tabs button{font-size:1rem;padding:10px 12px}
  .callbar{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:30;background:var(--black);border-top:var(--rule) solid var(--black)}
  .callbar a{display:flex;align-items:center;justify-content:center;min-height:56px;font-weight:700;text-decoration:none;color:var(--paper);background:var(--black)}
  .callbar a+a{background:var(--gold);color:var(--black)}
  body{padding-bottom:59px}
  html{scroll-padding-top:80px}
}
@media (prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .climb .ticks{transition:none}
}
@media print{.notice,.mast,.callbar,.cta{display:none}}
"""
