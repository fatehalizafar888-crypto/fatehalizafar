I='../images/'
P=[('Immersive Gaming','UX case study · Brand · AR','2026',I+'immersive-gaming/m01.webp','immersive-gaming','We watch together, then play alone. One app to fix that.'),
   ('Drip','UX case study · Brand · UI','2026',I+'drip/03.webp','drip','A wardrobe app that helps you walk in sure.'),
   ('Tafteesh','Board game · Brand · Packaging','2026',I+'tafteesh/16.webp','tafteesh-game','Catch the killer on the Model Town map.')]
E=[('ATOM Daily','Brand identity','atom-daily'),('Tafteesh Data','Data visualisation','tafteesh'),('Two Grounds, One Field','Spatial mapping','two-grounds-one-field'),('The Message','Visual essay','the-message'),('Fruit Ninja','Social media','fruit-ninja')]
def px(rot=0,s=18):
    cells=[(3,0),(4,1),(5,2),(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3),(5,4),(4,5),(3,6)]
    r=''.join(f'<rect x="{x}" y="{y}" width="1.02" height="1.02"/>' for x,y in cells)
    return f'<svg class="px" width="{s}" height="{s}" viewBox="0 0 7 7" fill="currentColor" style="transform:rotate({rot}deg)" shape-rendering="crispEdges">{r}</svg>'
AR=px()
CSS='''
@font-face{font-family:Adv;src:url(fonts/adventor-regular.woff2) format('woff2');font-weight:400}
@font-face{font-family:Adv;src:url(fonts/adventor-italic.woff2) format('woff2');font-weight:400;font-style:italic}
@font-face{font-family:Adv;src:url(fonts/adventor-bold.woff2) format('woff2');font-weight:700}
@font-face{font-family:Adv;src:url(fonts/adventor-bolditalic.woff2) format('woff2');font-weight:700;font-style:italic}
:root{--bg:#0b0b0b;--ink:#f1f0ea;--grey:#9d9c96;--dim:#5c5c58;--line:#222;--panel:#151515;--pad:clamp(20px,4.4vw,64px);--out:cubic-bezier(.16,1,.3,1)}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font:400 17px/1.55 Adv,system-ui,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}img{display:block;max-width:100%}
.thin{font-family:Jost,Adv,sans-serif;font-weight:200;letter-spacing:-.035em;line-height:.95}
.thin em,.em{font-family:Adv;font-weight:700;font-style:italic;letter-spacing:-.045em}
.cap{font-size:12.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--grey)}
.cap b{color:var(--ink);font-weight:400}.dot{display:inline-block;width:5px;height:5px;border-radius:50%;background:var(--dim);margin:0 12px;vertical-align:middle}
.body{color:var(--grey);font-size:clamp(16px,1.25vw,19px);line-height:1.6}
.px{display:inline-block;vertical-align:middle;transition:transform .4s var(--out)}
a:hover>.px,a:hover .go .px{transform:translateX(5px)}
nav{position:fixed;top:0;left:0;right:0;z-index:50;display:flex;align-items:center;justify-content:space-between;padding:22px var(--pad);mix-blend-mode:difference}
.brand{display:flex;align-items:center;gap:12px;font-size:15px}.brand svg{width:28px;height:28px}
.links{display:flex;gap:32px;font-size:14px}.links a{opacity:.7}.links a:hover{opacity:1}
.talk{display:inline-flex;align-items:center;gap:12px;font-size:14px;border-bottom:1px solid currentColor;padding-bottom:3px}
.btn{display:inline-flex;align-items:center;gap:12px;height:48px;padding:0 22px;border-radius:999px;font-size:14px;border:1px solid #3a3a3a;transition:all .3s}
.btn:hover{border-color:var(--ink)}.btn.w{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.avail{display:inline-flex;align-items:center;gap:10px;font-size:13px;color:var(--grey)}.avail i{width:7px;height:7px;border-radius:50%;background:#3ddc84}
/* small project card */
.pc{display:block}.pc .im{aspect-ratio:4/3;border-radius:12px;overflow:hidden;background:var(--panel)}
.pc .im img{width:100%;height:100%;object-fit:cover;object-position:50% 35%;transition:transform 1s var(--out)}
.pc:hover .im img{transform:scale(1.05)}
.pc .mt{display:flex;justify-content:space-between;align-items:baseline;margin-top:14px;font-size:17px}.pc .mt span{color:var(--dim);font-size:14px}
.pc .sb{font-size:13px;color:var(--grey);margin-top:4px}
.rv{opacity:0;transform:translateY(24px);animation:up 1.2s var(--out) forwards}@keyframes up{to{opacity:1;transform:none}}
.d1{animation-delay:.1s}.d2{animation-delay:.2s}.d3{animation-delay:.3s}.d4{animation-delay:.4s}
.switch{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);z-index:90;display:flex;gap:4px;background:rgba(28,28,28,.9);backdrop-filter:blur(10px);padding:5px;border-radius:999px;font-size:12px;white-space:nowrap}
.switch a{padding:7px 12px;border-radius:999px;color:var(--grey)}.switch a.on{background:var(--ink);color:var(--bg)}
.ft{display:flex;justify-content:space-between;gap:20px;padding:30px var(--pad) 80px;border-top:1px solid var(--line);font-size:13px;color:var(--dim);margin-top:clamp(60px,10vh,120px)}
@media(max-width:900px){.links{display:none}.switch{font-size:11px}}
'''
LOGO='<svg width="0" height="0" style="position:absolute"><defs><g id="mark"><path d="M 343.3 377.2 L 323.1 431.9 L 231.5 431.9 L 202.5 494.5 L 147.8 494.5 L 231.2 314.6 L 286 314.6 L 256.9 377.2 Z"/><path d="M 340.7 314.6 L 286 314.6 L 267.7 252 L 322.5 252 Z"/><path d="M 395.5 494.5 L 340.7 494.5 L 322.5 431.9 L 377.2 431.9 Z"/></g></defs></svg>'
NAV=f'<nav><a class="brand" href="#"><svg viewBox="147 251 249.5 245" fill="currentColor"><use href="#mark"/></svg>Fateh Ali Zafar</a><div class="links"><a href="#work">Work</a><a href="#about">About</a><a href="../">Old site</a></div><a class="talk" href="mailto:fatehalizafar888@gmail.com">Let\'s talk {AR}</a></nav>'
FT='<footer class="ft"><span>© 2026 Fateh Ali Zafar · Lahore</span><span><a href="https://www.behance.net/fatehalizafar">Behance</a> · <a href="https://www.linkedin.com/in/fatehali-zafar-786424265">LinkedIn</a> · <a href="https://www.instagram.com/the_art_wave__">Instagram</a></span><a href="mailto:fatehalizafar888@gmail.com">fatehalizafar888@gmail.com</a></footer>'
def cards(cls='',sub=True,n=3):
    return ''.join(f'<a class="pc {cls}" href="../#work-{p[4]}"><div class="im"><img src="{p[3]}" alt="{p[0]}" loading="lazy"></div><div class="mt">{p[0]}<span>0{i+1}</span></div>{f"<p class=sb>{p[1]}</p>" if sub else ""}</a>' for i,p in enumerate(P[:n]))
pages={}
# 1 Editorial statement + small row
pages['1']=('Editorial',''' .hero{min-height:100svh;padding:140px var(--pad) 40px;display:flex;flex-direction:column;justify-content:center}
.hero h1{font-size:clamp(3rem,6.4vw,7.4rem);margin-top:26px;max-width:17ch}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;max-width:1100px}
.split{display:grid;grid-template-columns:1fr 1.6fr;gap:60px;align-items:end;margin-top:44px}''',f'''
<section class="hero"><p class="cap rv">Designer<span class="dot"></span><b>Lahore, Pakistan</b><span class="dot"></span>Open to work</p>
<h1 class="thin rv d1">I make brands, apps and <em>motion</em> worth a second look.</h1>
<div class="split"><div class="rv d2"><p class="body">Hey, I'm Fateh. I studied Visual Communication Design at BNU and I start every project like a case to solve: find the clue, follow it, design the moment it clicks.</p><p style="margin-top:22px"><a class="talk" href="#work">Selected work {px(90)}</a></p></div>
<div class="grid3 rv d3" id="work">{cards()}</div></div></section>{FT}''')
# 2 Index list with thumbnails
pages['2']=('Index',''' .wrap{padding:150px var(--pad) 0;display:grid;grid-template-columns:1fr 1fr;gap:clamp(40px,6vw,110px)}
.wrap h1{font-size:clamp(3rem,6vw,6.8rem)}
.idx{border-top:1px solid var(--line)}.it{display:grid;grid-template-columns:96px 1fr auto;gap:22px;align-items:center;padding:18px 0;border-bottom:1px solid var(--line)}
.it .th{width:96px;aspect-ratio:4/3;border-radius:8px;overflow:hidden}.it .th img{width:100%;height:100%;object-fit:cover}
.it b{font-weight:400;font-size:22px;letter-spacing:-.02em}.it p{font-size:13px;color:var(--grey);margin-top:2px}
.it:hover b{font-style:italic;font-weight:700}
.sm{display:grid;grid-template-columns:1fr auto;padding:12px 0;border-bottom:1px solid var(--line);font-size:15px;color:var(--grey)}.sm:hover{color:var(--ink)}
.facts{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:40px}.facts p{font-size:15px}.facts span{display:block;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim)}''',f'''
<section class="wrap"><div><p class="cap rv">Fateh Ali Zafar<span class="dot"></span>Designer</p>
<h1 class="thin rv d1" style="margin-top:24px">Research first. <em>Then</em> design that moves.</h1>
<p class="body rv d2" style="margin-top:30px;max-width:42ch">I'm a visual communication designer from Lahore working across brand identity, UX and UI, motion and publication. Football, video games and crime cases are where most of my ideas start.</p>
<div class="facts rv d3"><p><span>Studied</span>BNU, VCD 2026</p><p><span>Certificate</span>Google UX Design</p><p><span>Recently</span>Montivo Digital, Strata</p><p><span>Status</span><span class="avail" style="letter-spacing:0;text-transform:none;font-size:15px;color:var(--ink)"><i></i>Open to work</span></p></div></div>
<div class="rv d2" id="work"><p class="cap" style="margin-bottom:16px">Selected work</p><div class="idx">{''.join(f'<a class="it" href="../#work-{p[4]}"><div class="th"><img src="{p[3]}" alt=""></div><div><b>{p[0]}</b><p>{p[1]}</p></div>{AR}</a>' for p in P)}</div>
<p class="cap" style="margin:40px 0 10px">Experiments</p>{''.join(f'<a class="sm" href="../#work-{e[2]}">{e[0]}<span>{e[1]}</span></a>' for e in E)}</div></section>{FT}''')
# 3 Bento
pages['3']=('Bento',''' .bento{padding:110px var(--pad) 0;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:minmax(150px,auto);gap:14px}
.tile{background:var(--panel);border-radius:18px;padding:26px;position:relative;overflow:hidden}
.t-hero{grid-column:span 3;grid-row:span 2;display:flex;flex-direction:column;justify-content:space-between}
.t-hero h1{font-size:clamp(2.6rem,5.2vw,6rem)}
.t-me{grid-row:span 2;padding:0}.t-me img{width:100%;height:100%;object-fit:cover;object-position:50% 20%;filter:grayscale(1)}
.t-me .cap{position:absolute;left:18px;bottom:16px;color:var(--ink)}
.t-p{padding:0}.t-p .im{border-radius:0;aspect-ratio:auto;height:180px}.t-p .mt,.t-p .sb{padding:0 20px}.t-p .sb{padding-bottom:20px}
.t-dis ul{list-style:none;margin-top:16px}.t-dis li{padding:8px 0;border-bottom:1px solid #262626;font-size:16px}
.t-cta{display:flex;flex-direction:column;justify-content:space-between;background:var(--ink);color:var(--bg)}
.t-cta .thin{font-size:40px}''',f'''
<section class="bento">
<div class="tile t-hero rv"><p class="cap">Fateh Ali Zafar<span class="dot"></span>Designer, Lahore</p><h1 class="thin">Brands, apps and <em>motion</em>, made from research.</h1><span class="avail"><i></i>Open to full time and freelance</span></div>
<div class="tile t-me rv d1"><img src="media/portrait.jpg" alt=""><p class="cap">That's me</p></div>
{''.join(f'<a class="tile t-p pc rv d{i+1}" href="../#work-{p[4]}"><div class="im"><img src="{p[3]}" alt=""></div><div class="mt">{p[0]}<span>0{i+1}</span></div><p class="sb">{p[1]}</p></a>' for i,p in enumerate(P))}
<div class="tile t-dis rv d3"><p class="cap">What I do</p><ul><li>Brand identity</li><li>UX and UI</li><li>Motion</li><li>Publication</li></ul></div>
<div class="tile rv d3" style="grid-column:span 2"><p class="cap">About</p><p class="body" style="margin-top:14px">VCD graduate from BNU with a Google UX certificate. I've designed for Montivo Digital, Strata and Experts Desk, and I published my own board game. Every brief is a case to solve.</p></div>
<a class="tile t-cta rv d4" href="mailto:fatehalizafar888@gmail.com" style="grid-column:span 2"><p class="cap" style="color:#555">Contact</p><div style="display:flex;justify-content:space-between;align-items:end"><p class="thin">Let's <em>talk</em>.</p>{px(0,28)}</div></a>
</section>{FT}''')
# 4 Case file
pages['4']=('Case file',''' .cf{padding:140px var(--pad) 0;max-width:1300px}
.stamp{display:inline-block;border:1px solid var(--grey);padding:6px 12px;font-size:12px;letter-spacing:.2em;color:var(--grey);transform:rotate(-3deg)}
.cf h1{font-size:clamp(3rem,7vw,8rem);margin:26px 0}
.tbl{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.tbl div{padding:18px 18px 18px 0}.tbl span{display:block;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-bottom:6px}
.ev{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:50px}
.ev .pc{background:#f1f0ea;color:#0b0b0b;padding:12px 12px 16px;border-radius:4px;transform:rotate(var(--r))}.ev .pc .im{border-radius:2px}.ev .pc .mt span,.ev .pc .sb{color:#666}
.ev .pc:hover{transform:rotate(0) translateY(-6px)}.ev .pc{transition:transform .6s var(--out)}''',f'''
<section class="cf"><span class="stamp rv">CASE FILE · 2026</span>
<h1 class="thin rv d1">Subject: Fateh Ali Zafar. <em>Designer.</em></h1>
<div class="tbl rv d2"><div><span>Location</span>Lahore, Pakistan</div><div><span>Trained at</span>BNU, VCD 2026</div><div><span>Known for</span>Brand, UX and UI, motion</div><div><span>Status</span><span class="avail" style="letter-spacing:0;text-transform:none;font-size:16px;color:var(--ink);margin:0"><i></i>Open to work</span></div></div>
<p class="body rv d3" style="margin-top:30px;max-width:56ch">I read crime cases the way other people read novels, and I design the same way. Every brief has a clue. Find it, follow it, and build the moment it all clicks. Below is the evidence.</p>
<p class="cap rv d3" style="margin-top:50px">Evidence · Selected work</p>
<div class="ev rv d4" id="work">{''.join(f'<a class="pc" style="--r:{r}deg" href="../#work-{p[4]}"><div class="im"><img src="{p[3]}" alt=""></div><div class="mt">Exhibit 0{i+1} · {p[0]}<span>{AR}</span></div><p class="sb">{p[1]}</p></a>' for i,(p,r) in enumerate(zip(P,[-2,1.5,-1])))}</div></section>{FT}''')
# 5 Centred about + carousel strip
pages['5']=('Centred',''' .c{padding:150px var(--pad) 0;text-align:center;display:flex;flex-direction:column;align-items:center}
.av{width:92px;height:92px;border-radius:50%;overflow:hidden}.av img{width:100%;height:100%;object-fit:cover;object-position:50% 15%;filter:grayscale(1)}
.c h1{font-size:clamp(2.8rem,6.2vw,7rem);max-width:14ch;margin-top:30px}
.c .body{max-width:50ch;margin-top:26px}
.strip{display:flex;gap:18px;margin-top:70px;padding:0 var(--pad);overflow-x:auto;scrollbar-width:none}
.strip .pc{flex:0 0 clamp(240px,24vw,360px);text-align:left}''',f'''
<section class="c"><div class="av rv"><img src="media/portrait.jpg" alt=""></div><p class="cap rv d1" style="margin-top:20px">Fateh Ali Zafar<span class="dot"></span>Lahore</p>
<h1 class="thin rv d1">A designer who treats every brief like a <em>case</em>.</h1>
<p class="body rv d2">Visual Communication Design at BNU, Google UX certified, and three years of brand, UX and UI, motion and publication work. I like owning a project from the first question to launch.</p>
<div class="rv d3" style="display:flex;gap:12px;margin-top:34px"><a class="btn w" href="#work">See work {px(90,14)}</a><a class="btn" href="mailto:fatehalizafar888@gmail.com">Email me {AR}</a></div></section>
<div class="strip rv d4" id="work">{cards()}{''.join(f'<a class="pc" href="../#work-{e[2]}"><div class="im" style="display:flex;align-items:end;padding:18px;background:#141414"><p class="thin" style="font-size:30px">{e[0]}</p></div><div class="mt">{e[1]}<span>{AR}</span></div></a>' for e in E[:3])}</div>{FT}''')
# 6 Split: about left sticky, projects right small
pages['6']=('Split',''' .sp{display:grid;grid-template-columns:1.05fr 1fr;min-height:100svh}
.l{position:sticky;top:0;height:100svh;padding:140px var(--pad) 50px;display:flex;flex-direction:column;justify-content:space-between;border-right:1px solid var(--line)}
.l h1{font-size:clamp(3rem,5.8vw,6.6rem)}
.r{padding:140px var(--pad) 60px;display:grid;grid-template-columns:1fr 1fr;gap:26px;align-content:start}
.r .wide{grid-column:span 2}
.svc{display:grid;grid-template-columns:1fr 1fr;gap:6px 30px;font-size:15px;color:var(--grey)}''',f'''
<section class="sp"><div class="l"><div><p class="cap rv">Hello, I'm Fateh</p><h1 class="thin rv d1" style="margin-top:24px">I design <em>brands</em>, apps and motion.</h1>
<p class="body rv d2" style="margin-top:28px;max-width:40ch">Designer from Lahore, VCD graduate from BNU. I've worked with Montivo Digital, Strata and Experts Desk, and published my own board game.</p></div>
<div class="rv d3"><div class="svc"><span>Brand identity</span><span>UX and UI</span><span>Motion graphics</span><span>Publication</span></div><p style="margin-top:28px"><a class="talk" href="mailto:fatehalizafar888@gmail.com">fatehalizafar888@gmail.com {AR}</a></p></div></div>
<div class="r" id="work"><p class="cap wide rv">Selected work · 3</p>{cards()}<a class="pc rv d3" href="../#work-atom-daily"><div class="im" style="display:flex;align-items:end;padding:20px;background:#141414"><p class="thin" style="font-size:34px">+5 <em>experiments</em></p></div><div class="mt">More work<span>{AR}</span></div></a></div></section>''')
# 7 Big name type
pages['7']=('Name',''' .nm{padding:120px var(--pad) 0}
.nm h1{font-size:clamp(4rem,15.5vw,19rem);line-height:.82;letter-spacing:-.06em}
.row{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:22px;margin-top:50px;align-items:start}
.row .about{grid-column:span 1}''',f'''
<section class="nm"><p class="cap rv">Designer<span class="dot"></span>Brand · UX/UI · Motion · Publication<span class="dot"></span>Lahore</p>
<h1 class="thin rv d1" style="margin-top:20px">Fateh <em>Ali</em> Zafar</h1>
<div class="row"><div class="about rv d2"><p class="body">I design brands, apps and motion. VCD from BNU, Google UX certified, and I treat every brief like a case to solve.</p><p style="margin-top:20px"><span class="avail"><i></i>Open to work</span></p><p style="margin-top:20px"><a class="talk" href="mailto:fatehalizafar888@gmail.com">Let's talk {AR}</a></p></div>
{cards().replace('class="pc ','class="pc rv d3 ')}</div></section>{FT}''')
HEAD='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fateh Ali Zafar · {n}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,200;0,300;1,200&display=swap" rel="stylesheet"><style>{css}</style></head><body>'
for k,(n,css,body) in pages.items():
    sw=''.join(f'<a href="{j}.html" class="{"on" if j==k else ""}">{j} {m}</a>' for j,(m,_,_) in pages.items())
    open(f'{k}.html','w').write(HEAD.format(n=n,css=CSS+css)+LOGO+NAV+body+f'<div class="switch">{sw}</div></body></html>')
print('ok')
