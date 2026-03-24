
"""
IBEX Landing Page (pages/00_Home.py)
FIXES: nav anchors work, tight spacing, no free trial, privacy policy, contact section, favicon via app.py
"""
import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
<style>
#MainMenu,footer,header{visibility:hidden}
.block-container{padding:0!important;max-width:100%!important}
[data-testid="stSidebar"]{display:none!important}
[data-testid="collapsedControl"]{display:none!important}
</style>
""", unsafe_allow_html=True)

AUDIT_URL     = "https://ibexsupplements.streamlit.app/Audit"
SUPPORT_EMAIL = "support@ibexsupplements.com"

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IBEX — Supplement Intelligence for D1 Athletics</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;600;700&family=Barlow+Condensed:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--black:#0a0a0f;--navy:#0b1220;--navy2:#132033;--off:#f0ede6;--gold:#c9a84c;--gold2:#e8c97a;--muted:rgba(240,237,230,0.52);--border:rgba(201,168,76,0.18);--green:#4ade80;--blue:#7dd3fc;--red:#ef4444}}
html{{scroll-behavior:smooth}}
body{{background:var(--black);color:var(--off);font-family:"Barlow",sans-serif;font-weight:300;overflow-x:hidden}}
nav{{position:sticky;top:0;z-index:999;display:flex;align-items:center;justify-content:space-between;padding:.75rem 2.5rem;background:rgba(10,10,15,0.97);backdrop-filter:blur(16px);border-bottom:1px solid var(--border)}}
.nav-word{{font-family:"Bebas Neue",sans-serif;font-size:1.7rem;letter-spacing:.1em;color:var(--gold);cursor:pointer}}
.nav-links{{display:flex;gap:1.5rem;list-style:none}}
.nav-links a{{font-family:"Barlow Condensed",sans-serif;font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:var(--off);opacity:.6;text-decoration:none;cursor:pointer;transition:opacity .2s,color .2s}}
.nav-links a:hover{{opacity:1;color:var(--gold)}}
.nav-btns{{display:flex;gap:.6rem}}
.btn-nav-ghost{{font-family:"Barlow Condensed",sans-serif;font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;font-weight:600;padding:.4rem .9rem;border:1px solid var(--border);color:var(--muted);text-decoration:none;transition:all .2s;cursor:pointer}}
.btn-nav-ghost:hover{{border-color:var(--gold);color:var(--gold)}}
.btn-nav{{font-family:"Barlow Condensed",sans-serif;font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;font-weight:700;background:var(--gold);color:var(--black);padding:.4rem .9rem;text-decoration:none;transition:background .2s;cursor:pointer;border:none}}
.btn-nav:hover{{background:var(--gold2)}}
#hero{{min-height:88vh;display:flex;flex-direction:column;justify-content:center;padding:5rem 3rem 3rem;position:relative;overflow:hidden}}
.hero-bg{{position:absolute;right:-2%;top:50%;transform:translateY(-50%);font-family:"Bebas Neue",sans-serif;font-size:38vw;color:rgba(201,168,76,0.03);pointer-events:none;line-height:1}}
.hero-inner{{position:relative;z-index:1;max-width:860px}}
.hero-eyebrow{{font-family:"Barlow Condensed",sans-serif;font-size:.65rem;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);margin-bottom:1.2rem;opacity:0;animation:fadeUp .7s .1s forwards}}
.hero-h1{{font-family:"Bebas Neue",sans-serif;font-size:clamp(3.8rem,8.5vw,9rem);line-height:.88;margin-bottom:1.4rem;opacity:0;animation:fadeUp .7s .25s forwards}}
.hero-h1 em{{color:var(--gold);font-style:normal}}
.hero-sub{{font-size:1rem;line-height:1.75;color:var(--muted);max-width:560px;margin-bottom:2rem;opacity:0;animation:fadeUp .7s .4s forwards}}
.hero-actions{{display:flex;gap:1rem;align-items:center;flex-wrap:wrap;margin-bottom:2.5rem;opacity:0;animation:fadeUp .7s .55s forwards}}
.btn-gold{{font-family:"Barlow Condensed",sans-serif;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;background:var(--gold);color:var(--black);padding:.85rem 2rem;text-decoration:none;display:inline-block;border:none;cursor:pointer;transition:background .2s,transform .15s}}
.btn-gold:hover{{background:var(--gold2);transform:translateY(-2px)}}
.btn-outline{{font-family:"Barlow Condensed",sans-serif;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;font-weight:600;border:1px solid var(--border);color:var(--muted);padding:.85rem 2rem;text-decoration:none;display:inline-block;transition:all .2s}}
.btn-outline:hover{{border-color:var(--gold);color:var(--gold)}}
.hero-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--border);border:1px solid var(--border);max-width:680px;opacity:0;animation:fadeUp .7s .7s forwards}}
.stat-box{{background:var(--black);padding:1.2rem 1rem}}
.stat-num{{font-family:"Bebas Neue",sans-serif;font-size:2.5rem;color:var(--gold);line-height:1;margin-bottom:.15rem}}
.stat-label{{font-family:"Barlow Condensed",sans-serif;font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted)}}
.ticker{{background:var(--gold);overflow:hidden;padding:.55rem 0;white-space:nowrap}}
.ticker-inner{{display:inline-flex;animation:ticker 35s linear infinite}}
.t-item{{font-family:"Barlow Condensed",sans-serif;font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;color:var(--black);font-weight:700;padding:0 1.8rem}}
.t-dot{{color:rgba(0,0,0,.25)}}
@keyframes ticker{{0%{{transform:translateX(0)}}100%{{transform:translateX(-50%)}}}}
.section{{padding:3.5rem 3rem}}
.section-inner{{max-width:1160px;margin:0 auto}}
.s-label{{font-family:"Barlow Condensed",sans-serif;font-size:.6rem;letter-spacing:.38em;text-transform:uppercase;color:var(--gold);margin-bottom:.5rem}}
.s-title{{font-family:"Bebas Neue",sans-serif;font-size:clamp(2.4rem,4.5vw,4.2rem);line-height:.93;margin-bottom:1.8rem}}
.s-sub{{font-size:.92rem;line-height:1.75;color:var(--muted);max-width:580px;margin-bottom:2rem}}
#problem{{background:var(--navy)}}
.prob-grid{{display:grid;grid-template-columns:1fr 1fr;gap:2rem}}
.prob-box{{border:1px solid var(--border);padding:1.5rem}}
.prob-head{{font-family:"Barlow Condensed",sans-serif;font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.8rem}}
.prob-head.red{{color:var(--red)}}.prob-head.gold{{color:var(--gold)}}
.prob-list{{list-style:none}}
.prob-list li{{font-size:.85rem;line-height:1.65;padding:.35rem 0;border-bottom:1px solid rgba(201,168,76,.07);color:var(--muted);display:flex;gap:.7rem;align-items:flex-start}}
.prob-list li.x::before{{content:"\2717";color:var(--red);flex-shrink:0}}
.prob-list li.check::before{{content:"\2192";color:var(--gold);flex-shrink:0}}
#how{{background:var(--black)}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--border)}}
.step{{padding:2rem 1.6rem;border-right:1px solid var(--border);transition:background .3s}}
.step:last-child{{border-right:none}}
.step:hover{{background:rgba(201,168,76,.04)}}
.step-num{{font-family:"Bebas Neue",sans-serif;font-size:3rem;color:rgba(201,168,76,.1);line-height:1;margin-bottom:.6rem}}
.step-title{{font-family:"Barlow Condensed",sans-serif;font-size:.95rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--off);margin-bottom:.5rem}}
.step-body{{font-size:.82rem;line-height:1.7;color:var(--muted)}}
.step-who{{margin-top:.6rem;font-family:"Barlow Condensed",sans-serif;font-size:.58rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold)}}
#admin{{background:var(--navy)}}
.admin-preview{{border:1px solid var(--border);overflow:hidden}}
.admin-bar{{background:var(--black);border-bottom:1px solid var(--border);padding:.8rem 1.2rem;display:flex;align-items:center;gap:.8rem}}
.admin-dot{{width:9px;height:9px;border-radius:50%}}
.admin-dot.r{{background:var(--red)}}.admin-dot.y{{background:#f59e0b}}.admin-dot.g{{background:var(--green)}}
.admin-title{{font-family:"Barlow Condensed",sans-serif;font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-left:.3rem}}
.admin-body{{padding:1.2rem}}
.admin-metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:.8rem;margin-bottom:1.2rem}}
.metric-box{{background:var(--black);border:1px solid var(--border);padding:.9rem}}
.metric-val{{font-family:"Bebas Neue",sans-serif;font-size:1.8rem;color:var(--gold);line-height:1}}
.metric-lbl{{font-family:"Barlow Condensed",sans-serif;font-size:.55rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-top:.15rem}}
.admin-table{{width:100%;border-collapse:collapse}}
.admin-table th{{font-family:"Barlow Condensed",sans-serif;font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);padding:.5rem .8rem;text-align:left;border-bottom:1px solid var(--border)}}
.admin-table td{{font-size:.8rem;color:rgba(240,237,230,.72);padding:.6rem .8rem;border-bottom:1px solid rgba(201,168,76,.05)}}
.sp{{font-family:"Barlow Condensed",sans-serif;font-size:.55rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700;padding:.18rem .45rem}}
.sp.ok{{background:rgba(74,222,128,.1);color:var(--green);border:1px solid rgba(74,222,128,.25)}}
.sp.pend{{background:rgba(201,168,76,.1);color:var(--gold);border:1px solid rgba(201,168,76,.25)}}
.sp.flag{{background:rgba(239,68,68,.1);color:var(--red);border:1px solid rgba(239,68,68,.25)}}
#plans{{background:var(--black);position:relative;overflow:hidden}}
#plans::before{{content:"IBEX";position:absolute;right:-.02em;bottom:-.1em;font-family:"Bebas Neue",sans-serif;font-size:22vw;color:rgba(201,168,76,.025);pointer-events:none;line-height:1}}
#plans .section-inner{{position:relative;z-index:1}}
.plan-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}}
.plan-card{{border:1px solid var(--border);padding:2rem;position:relative;transition:border-color .3s}}
.plan-card:hover{{border-color:rgba(201,168,76,.45)}}
.plan-card.featured{{border-color:var(--gold);background:rgba(201,168,76,.03)}}
.plan-tag{{position:absolute;top:-1px;right:1.2rem;background:var(--gold);color:var(--black);font-family:"Barlow Condensed",sans-serif;font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;padding:.22rem .65rem}}
.plan-tier{{font-family:"Barlow Condensed",sans-serif;font-size:.62rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);margin-bottom:.6rem}}
.plan-price{{font-family:"Bebas Neue",sans-serif;font-size:3.2rem;line-height:1;margin-bottom:.15rem}}
.plan-price sup{{font-size:1.3rem;vertical-align:top;margin-top:.4rem}}
.plan-period{{font-size:.75rem;color:var(--muted);margin-bottom:.3rem}}
.plan-athletes{{font-family:"Barlow Condensed",sans-serif;font-size:.68rem;letter-spacing:.1em;color:var(--gold);margin-bottom:1.4rem}}
.plan-features{{list-style:none;margin-bottom:1.6rem}}
.plan-features li{{font-size:.82rem;line-height:1.6;padding:.42rem 0;border-bottom:1px solid rgba(201,168,76,.07);color:rgba(240,237,230,.68);display:flex;gap:.6rem}}
.plan-features li::before{{content:"\2192";color:var(--gold);flex-shrink:0}}
.btn-plan{{font-family:"Barlow Condensed",sans-serif;font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;padding:.78rem;border:1px solid var(--gold);color:var(--gold);background:transparent;cursor:pointer;text-decoration:none;display:block;text-align:center;transition:all .2s}}
.btn-plan:hover{{background:var(--gold);color:var(--black)}}
.plan-card.featured .btn-plan{{background:var(--gold);color:var(--black)}}
#catalog{{background:var(--navy)}}
.cat-filter{{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem}}
.cat-btn{{font-family:"Barlow Condensed",sans-serif;font-size:.62rem;letter-spacing:.15em;text-transform:uppercase;font-weight:600;padding:.28rem .75rem;border:1px solid var(--border);background:transparent;color:var(--muted);cursor:pointer;transition:all .2s}}
.cat-btn:hover,.cat-btn.active{{background:var(--gold);color:var(--black);border-color:var(--gold)}}
.supp-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1px;background:var(--border);border:1px solid var(--border)}}
.supp-card{{background:var(--navy);padding:1.3rem;transition:background .25s}}
.supp-card:hover{{background:rgba(201,168,76,.05)}}
.supp-card.hidden{{display:none}}
.supp-top{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.55rem}}
.supp-cat{{font-family:"Barlow Condensed",sans-serif;font-size:.55rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold)}}
.supp-badges{{display:flex;gap:.22rem}}
.badge{{font-family:"Barlow Condensed",sans-serif;font-size:.48rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700;padding:.12rem .38rem;border:1px solid rgba(201,168,76,.25);color:var(--gold)}}
.badge.ncaa{{border-color:rgba(74,222,128,.35);color:var(--green)}}
.badge.nsf{{border-color:rgba(125,211,252,.35);color:var(--blue)}}
.supp-name{{font-family:"Barlow Condensed",sans-serif;font-size:1rem;font-weight:700;color:var(--off);margin-bottom:.2rem}}
.supp-dose{{font-size:.72rem;color:var(--muted);margin-bottom:.4rem}}
.supp-use{{font-size:.76rem;line-height:1.6;color:rgba(240,237,230,.52)}}
.supp-timing{{margin-top:.55rem;font-family:"Barlow Condensed",sans-serif;font-size:.56rem;letter-spacing:.13em;text-transform:uppercase;color:rgba(201,168,76,.55)}}
#proof{{background:var(--black)}}
.proof-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}}
.proof-card{{border:1px solid rgba(201,168,76,.1);padding:1.8rem;transition:all .3s}}
.proof-card:hover{{border-color:rgba(201,168,76,.3);background:rgba(201,168,76,.02)}}
.proof-logo{{font-family:"Bebas Neue",sans-serif;font-size:1.3rem;color:var(--gold);margin-bottom:.4rem}}
.proof-quote{{font-size:.86rem;line-height:1.72;color:rgba(240,237,230,.62);font-style:italic;margin-bottom:1rem}}
.proof-author{{font-family:"Barlow Condensed",sans-serif;font-size:.62rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}}
.proof-role{{font-size:.72rem;color:rgba(240,237,230,.28);margin-top:.12rem}}
#faq{{background:var(--navy)}}
.faq-wrap{{max-width:800px}}
.faq-item{{border-bottom:1px solid rgba(201,168,76,.12)}}
.faq-q{{display:flex;justify-content:space-between;align-items:center;padding:1.2rem 0;cursor:pointer;user-select:none;font-family:"Barlow Condensed",sans-serif;font-size:1rem;font-weight:700;letter-spacing:.02em;color:var(--off);gap:1rem}}
.faq-icon{{color:var(--gold);font-size:1.1rem;flex-shrink:0;transition:transform .3s}}
.faq-a{{max-height:0;overflow:hidden;font-size:.84rem;line-height:1.78;color:var(--muted);transition:max-height .4s ease,padding .3s}}
.faq-item.open .faq-a{{max-height:300px;padding-bottom:1.2rem}}
.faq-item.open .faq-icon{{transform:rotate(45deg)}}
#privacy{{background:var(--black)}}
.priv-body{{max-width:760px}}
.priv-body h3{{font-family:"Barlow Condensed",sans-serif;font-size:.95rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--off);margin:1.2rem 0 .4rem}}
.priv-body p{{font-size:.84rem;line-height:1.78;color:var(--muted);margin-bottom:.6rem}}
.priv-body ul{{list-style:none}}
.priv-body ul li{{font-size:.84rem;line-height:1.7;color:var(--muted);padding:.18rem 0;display:flex;gap:.6rem}}
.priv-body ul li::before{{content:"\2192";color:var(--gold);flex-shrink:0}}
#contact{{background:var(--navy)}}
.contact-grid{{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:start}}
.contact-card{{border:1px solid var(--border);padding:1.8rem}}
.contact-card.featured{{border-color:var(--gold);background:rgba(201,168,76,.03)}}
.contact-clabel{{font-family:"Barlow Condensed",sans-serif;font-size:.6rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:.4rem}}
.contact-ctitle{{font-family:"Bebas Neue",sans-serif;font-size:1.5rem;color:var(--off);margin-bottom:.5rem;line-height:1}}
.contact-body{{font-size:.84rem;line-height:1.72;color:var(--muted);margin-bottom:1rem}}
.contact-email-link{{font-family:"Barlow Condensed",sans-serif;font-size:.95rem;font-weight:700;letter-spacing:.05em;color:var(--gold);text-decoration:none;display:block;margin-bottom:.25rem}}
.contact-email-link:hover{{color:var(--gold2)}}
.contact-detail{{font-size:.75rem;color:rgba(240,237,230,.3)}}
#cta{{background:var(--black);padding:6rem 3rem;text-align:center;position:relative;overflow:hidden}}
#cta::before{{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 55% 55% at 50% 50%,rgba(201,168,76,.07) 0%,transparent 70%);pointer-events:none}}
.cta-title{{font-family:"Bebas Neue",sans-serif;font-size:clamp(3rem,6.5vw,6.5rem);line-height:.93;margin-bottom:1rem;position:relative;z-index:1}}
.cta-title em{{color:var(--gold);font-style:normal}}
.cta-sub{{font-size:.95rem;color:var(--muted);margin-bottom:2rem;position:relative;z-index:1}}
.cta-actions{{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;position:relative;z-index:1}}
footer{{padding:1.5rem 3rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap}}
.f-word{{font-family:"Bebas Neue",sans-serif;font-size:1.3rem;letter-spacing:.1em;color:var(--gold)}}
.f-copy{{font-size:.68rem;color:rgba(240,237,230,.2)}}
.f-links{{display:flex;gap:1.2rem;flex-wrap:wrap}}
.f-links a{{font-family:"Barlow Condensed",sans-serif;font-size:.62rem;letter-spacing:.13em;text-transform:uppercase;color:rgba(240,237,230,.25);text-decoration:none;transition:color .2s;cursor:pointer}}
.f-links a:hover{{color:var(--gold)}}
.f-disc{{width:100%;font-size:.65rem;color:rgba(240,237,230,.18);line-height:1.6;border-top:1px solid rgba(201,168,76,.07);padding-top:.8rem;margin-top:.4rem}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:translateY(0)}}}}
.reveal{{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}}
.reveal.visible{{opacity:1;transform:translateY(0)}}
@media(max-width:900px){{
  nav{{padding:.8rem 1.2rem}}.nav-links{{display:none}}
  #hero{{padding:4rem 1.2rem 2.5rem}}.hero-stats{{grid-template-columns:1fr 1fr}}
  .section{{padding:2.5rem 1.2rem}}
  .steps,.plan-grid,.proof-grid,.contact-grid{{grid-template-columns:1fr}}
  .step{{border-right:none;border-bottom:1px solid var(--border)}}
  .prob-grid,.admin-metrics{{grid-template-columns:1fr 1fr}}
  footer{{flex-direction:column;text-align:center}}
}}
</style>
</head>
<body>

<nav>
  <span class="nav-word" onclick="scrollTo('hero')">IBEX</span>
  <ul class="nav-links">
    <li><a onclick="scrollTo('problem')">The Problem</a></li>
    <li><a onclick="scrollTo('how')">How It Works</a></li>
    <li><a onclick="scrollTo('plans')">Pricing</a></li>
    <li><a onclick="scrollTo('catalog')">The Stack</a></li>
    <li><a onclick="scrollTo('contact')">Contact</a></li>
    <li><a onclick="scrollTo('privacy')">Privacy</a></li>
  </ul>
  <div class="nav-btns">
    <a class="btn-nav-ghost" href="{AUDIT_URL}" target="_top">Athlete Audit</a>
    <button class="btn-nav" onclick="scrollTo('contact')">Get In Touch</button>
  </div>
</nav>

<section id="hero">
  <div class="hero-bg">I</div>
  <div class="hero-inner">
    <div class="hero-eyebrow">NCAA-Compliant Supplement Intelligence for D1 Athletics</div>
    <h1 class="hero-h1">ONE DIETITIAN.<br>500 ATHLETES.<br><em>ZERO GUESSWORK.</em></h1>
    <p class="hero-sub">IBEX gives every athlete at your program a personalized, AI-generated supplement protocol — reviewed by your sports dietitian, NCAA-compliant, and evidence-linked.</p>
    <div class="hero-actions">
      <button class="btn-gold" onclick="scrollTo('contact')">Get In Touch →</button>
      <a class="btn-outline" href="{AUDIT_URL}" target="_top">Try the Athlete Audit</a>
    </div>
    <div class="hero-stats">
      <div class="stat-box"><div class="stat-num">180K</div><div class="stat-label">D1 Athletes in the US</div></div>
      <div class="stat-box"><div class="stat-num">1</div><div class="stat-label">Dietitian per ~500 Athletes</div></div>
      <div class="stat-box"><div class="stat-num">$0</div><div class="stat-label">Inventory to Manage</div></div>
      <div class="stat-box"><div class="stat-num">3 min</div><div class="stat-label">Per Athlete Audit</div></div>
    </div>
  </div>
</section>

<div class="ticker">
  <div class="ticker-inner">
    <span class="t-item">NCAA Compliant Catalog</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Dietitian Dashboard</span><span class="t-dot"> ✶ </span>
    <span class="t-item">AI-Personalized Protocols</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Evidence-Linked Ingredients</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Sport + Position Specific</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Zero Inventory Risk</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Compliance Audit Trail</span><span class="t-dot"> ✶ </span>
    <span class="t-item">NCAA Compliant Catalog</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Dietitian Dashboard</span><span class="t-dot"> ✶ </span>
    <span class="t-item">AI-Personalized Protocols</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Evidence-Linked Ingredients</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Sport + Position Specific</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Zero Inventory Risk</span><span class="t-dot"> ✶ </span>
    <span class="t-item">Compliance Audit Trail</span><span class="t-dot"> ✶ </span>
  </div>
</div>

<section id="problem" class="section">
  <div class="section-inner">
    <div class="s-label reveal">The Gap</div>
    <h2 class="s-title reveal">WHY THIS MATTERS</h2>
    <div class="prob-grid">
      <div class="prob-box reveal">
        <div class="prob-head red">Right Now at Your Program</div>
        <ul class="prob-list">
          <li class="x">Athletes self-prescribing from GNC, Amazon, and influencer codes</li>
          <li class="x">No NCAA compliance check on what they are actually taking</li>
          <li class="x">One dietitian cannot give individualized guidance to 500+ athletes</li>
          <li class="x">No traceable record if an athlete tests positive for a banned substance</li>
          <li class="x">Generic recommendations that ignore sport, position, and season</li>
        </ul>
      </div>
      <div class="prob-box reveal">
        <div class="prob-head gold">What IBEX Does</div>
        <ul class="prob-list">
          <li class="check">AI generates a personalized sport-specific protocol per athlete in 3 minutes</li>
          <li class="check">Every ingredient cross-referenced against the NCAA banned substance list</li>
          <li class="check">Dietitian reviews and approves every recommendation before athlete sees it</li>
          <li class="check">Full audit trail: who takes what, when, and with whose approval</li>
          <li class="check">In-season vs off-season protocol adjustments built in automatically</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section id="how" class="section">
  <div class="section-inner">
    <div class="s-label reveal">The Process</div>
    <h2 class="s-title reveal">HOW IBEX WORKS</h2>
    <div class="steps">
      <div class="step reveal"><div class="step-num">01</div><div class="step-title">Department Onboards</div><p class="step-body">Dashboard live in 30 minutes. Invite athletes via secure link. No IT setup required.</p><div class="step-who">⚙ Dietitian</div></div>
      <div class="step reveal"><div class="step-num">02</div><div class="step-title">Athlete Runs Audit</div><p class="step-body">15 questions covering sport, position, training, sleep, stress, goals, and sensitivities. AI builds protocol instantly.</p><div class="step-who">🏃 Athlete</div></div>
      <div class="step reveal"><div class="step-num">03</div><div class="step-title">Dietitian Reviews</div><p class="step-body">Every recommendation routes to the dashboard for approval, modification, or flagging before the athlete sees it.</p><div class="step-who">⚕ Dietitian</div></div>
      <div class="step reveal"><div class="step-num">04</div><div class="step-title">Athletes Perform</div><p class="step-body">Approved protocol with exact dosing, AM/PM/Training schedule, and Ask IBEX chat for ongoing questions.</p><div class="step-who">🏆 Everyone</div></div>
    </div>
  </div>
</section>

<section id="admin" class="section">
  <div class="section-inner">
    <div class="s-label reveal">For Sports Dietitians</div>
    <h2 class="s-title reveal">THE DIETITIAN DASHBOARD</h2>
    <p class="s-sub reveal">Full visibility across every athlete. Review, approve, modify, or flag — all in one place.</p>
    <div class="admin-preview reveal">
      <div class="admin-bar">
        <div class="admin-dot r"></div><div class="admin-dot y"></div><div class="admin-dot g"></div>
        <span class="admin-title">IBEX Admin — Lehigh University Athletics</span>
      </div>
      <div class="admin-body">
        <div class="admin-metrics">
          <div class="metric-box"><div class="metric-val">247</div><div class="metric-lbl">Total Athletes</div></div>
          <div class="metric-box"><div class="metric-val">189</div><div class="metric-lbl">Audits Complete</div></div>
          <div class="metric-box"><div class="metric-val">164</div><div class="metric-lbl">Approved</div></div>
          <div class="metric-box"><div class="metric-val">3</div><div class="metric-lbl">Flagged</div></div>
        </div>
        <table class="admin-table">
          <thead><tr><th>Athlete</th><th>Sport</th><th>Plan</th><th>Date</th><th>Status</th><th>Action</th></tr></thead>
          <tbody>
            <tr><td>J. Williams</td><td>Football · LB</td><td>Performance</td><td>Mar 18</td><td><span class="sp ok">Approved</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;">View →</td></tr>
            <tr><td>M. Chen</td><td>Swimming · Freestyle</td><td>Basic</td><td>Mar 17</td><td><span class="sp ok">Approved</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;">View →</td></tr>
            <tr><td>A. Rodriguez</td><td>Track · 400m</td><td>Performance</td><td>Mar 17</td><td><span class="sp pend">Pending</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;">Review →</td></tr>
            <tr><td>T. Johnson</td><td>Wrestling · 165lb</td><td>Performance</td><td>Mar 16</td><td><span class="sp flag">Flagged</span></td><td style="color:var(--red);font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;">Urgent →</td></tr>
            <tr><td>S. Park</td><td>Soccer · Mid</td><td>Basic</td><td>Mar 16</td><td><span class="sp ok">Approved</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;">View →</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<section id="plans" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Pricing</div>
    <h2 class="s-title reveal">DEPARTMENT LICENSING</h2>
    <p class="s-sub reveal">One license covers your entire athletic department. No per-athlete fees. No inventory. No surprises.</p>
    <div class="plan-grid">
      <div class="plan-card reveal">
        <div class="plan-tier">Starter Program</div>
        <div class="plan-price"><sup>$</sup>500</div>
        <div class="plan-period">/ month · billed annually</div>
        <div class="plan-athletes">Up to 300 athletes</div>
        <ul class="plan-features">
          <li>AI audit tool for all athletes</li>
          <li>Dietitian review dashboard</li>
          <li>NCAA-compliant catalog</li>
          <li>AM / PM / Training schedule per athlete</li>
          <li>Ask IBEX chat per athlete</li>
          <li>Basic compliance reporting</li>
          <li>Email support</li>
        </ul>
        <button class="btn-plan" onclick="scrollTo('contact')">Get In Touch</button>
      </div>
      <div class="plan-card featured reveal">
        <div class="plan-tag">Most Popular</div>
        <div class="plan-tier">Mid-Size Program</div>
        <div class="plan-price"><sup>$</sup>1,000</div>
        <div class="plan-period">/ month · billed annually</div>
        <div class="plan-athletes">Up to 600 athletes</div>
        <ul class="plan-features">
          <li>Everything in Starter</li>
          <li>Full compliance audit trail</li>
          <li>In-season / off-season auto-adjustments</li>
          <li>Multi-sport analytics dashboard</li>
          <li>Affiliate product links (revenue share)</li>
          <li>Priority support + onboarding call</li>
          <li>Custom branding on athlete portal</li>
        </ul>
        <button class="btn-plan" onclick="scrollTo('contact')">Get In Touch</button>
      </div>
      <div class="plan-card reveal">
        <div class="plan-tier">Power Five Program</div>
        <div class="plan-price"><sup>$</sup>2,000</div>
        <div class="plan-period">/ month · billed annually</div>
        <div class="plan-athletes">Unlimited athletes</div>
        <ul class="plan-features">
          <li>Everything in Mid-Size</li>
          <li>Dedicated account manager</li>
          <li>Custom catalog additions</li>
          <li>API integration with AMS platforms</li>
          <li>Department-wide analytics reports</li>
          <li>Quarterly business reviews</li>
          <li>SLA guaranteed uptime</li>
        </ul>
        <button class="btn-plan" onclick="scrollTo('contact')">Contact Sales</button>
      </div>
    </div>
    <p style="font-size:.76rem;color:var(--muted);margin-top:1.2rem;text-align:center;">Athletes can also use the audit tool individually — <a href="{AUDIT_URL}" target="_top" style="color:var(--gold);">free at the Audit page</a>.</p>
  </div>
</section>

<section id="catalog" class="section">
  <div class="section-inner">
    <div class="s-label reveal">The Catalog</div>
    <h2 class="s-title reveal">WHAT ATHLETES GET RECOMMENDED</h2>
    <p class="s-sub reveal">Every ingredient is NCAA-compliant, evidence-backed, and cross-referenced against the banned substance list. Nothing that puts eligibility at risk.</p>
    <div class="cat-filter reveal">
      <button class="cat-btn active" data-cat="all">All</button>
      <button class="cat-btn" data-cat="strength">Strength</button>
      <button class="cat-btn" data-cat="recovery">Recovery</button>
      <button class="cat-btn" data-cat="endurance">Endurance</button>
      <button class="cat-btn" data-cat="sleep">Sleep</button>
      <button class="cat-btn" data-cat="foundation">Foundation</button>
      <button class="cat-btn" data-cat="gut">Gut &amp; Joint</button>
    </div>
    <div class="supp-grid" id="suppGrid">
      <div class="supp-card" data-cat="strength"><div class="supp-top"><span class="supp-cat">Strength</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Creatine Monohydrate</div><div class="supp-dose">5g / day · Powder</div><div class="supp-use">Most-studied performance supplement ever. Increases phosphocreatine for explosive power and faster recovery between sets.</div><div class="supp-timing">⏱ Post-training or AM</div></div>
      <div class="supp-card" data-cat="strength"><div class="supp-top"><span class="supp-cat">Strength / Endurance</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Beta-Alanine</div><div class="supp-dose">3.2g / day · Powder</div><div class="supp-use">Buffers lactic acid during repeated high-intensity efforts. Best for wrestling, lacrosse, rowing, basketball.</div><div class="supp-timing">⏱ Pre-training</div></div>
      <div class="supp-card" data-cat="strength"><div class="supp-top"><span class="supp-cat">Strength</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Whey Protein Isolate</div><div class="supp-dose">25–40g · Powder</div><div class="supp-use">Fast-digesting complete protein to start muscle protein synthesis. NSF Certified. Essential for high training volume.</div><div class="supp-timing">⏱ Within 30 min post-training</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Omega-3 Fish Oil</div><div class="supp-dose">2–3g EPA/DHA / day</div><div class="supp-use">Reduces systemic inflammation, supports joints and cardiovascular efficiency. Among the highest-evidence supplements for athletes.</div><div class="supp-timing">⏱ With meals</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Tart Cherry Extract</div><div class="supp-dose">480mg / day · Capsule</div><div class="supp-use">Reduces DOMS and exercise-induced muscle damage. Effective for back-to-back game days and high-volume blocks.</div><div class="supp-timing">⏱ AM + PM</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery / Sleep</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Magnesium Glycinate</div><div class="supp-dose">400mg / night · Capsule</div><div class="supp-use">Supports muscle relaxation, sleep quality, and protein synthesis. Most athletes deficient especially with high sweat rates.</div><div class="supp-timing">⏱ 30 min before bed</div></div>
      <div class="supp-card" data-cat="endurance"><div class="supp-top"><span class="supp-cat">Endurance</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Electrolyte Complex</div><div class="supp-dose">Sodium / Potassium / Magnesium</div><div class="supp-use">Replaces sweat losses to maintain performance. Essential during preseason camps, doubles, and multi-event days.</div><div class="supp-timing">⏱ During training</div></div>
      <div class="supp-card" data-cat="endurance"><div class="supp-top"><span class="supp-cat">Endurance</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span></div></div><div class="supp-name">Beetroot Nitrate</div><div class="supp-dose">400mg nitrate · Powder</div><div class="supp-use">Boosts nitric oxide to improve blood flow and O2 efficiency. Strong evidence for swimming, rowing, soccer.</div><div class="supp-timing">⏱ 2–3 hrs pre-training</div></div>
      <div class="supp-card" data-cat="sleep"><div class="supp-top"><span class="supp-cat">Sleep / Stress</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Ashwagandha KSM-66</div><div class="supp-dose">300–600mg / day · Capsule</div><div class="supp-use">Reduces cortisol and perceived stress. Improves sleep quality and recovery in high-stress training phases.</div><div class="supp-timing">⏱ PM or with dinner</div></div>
      <div class="supp-card" data-cat="sleep"><div class="supp-top"><span class="supp-cat">Sleep</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Melatonin Low-Dose</div><div class="supp-dose">0.5–1mg · Capsule</div><div class="supp-use">Supports sleep onset without grogginess. Best for travel across time zones and late-night practice schedules.</div><div class="supp-timing">⏱ 30 min before bed</div></div>
      <div class="supp-card" data-cat="foundation"><div class="supp-top"><span class="supp-cat">Foundation</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Vitamin D3 + K2</div><div class="supp-dose">3000–5000 IU D3 + 100mcg K2</div><div class="supp-use">Bone health, immune function, testosterone, mood. Large proportion of D1 athletes deficient — especially indoor sports.</div><div class="supp-timing">⏱ AM with fat</div></div>
      <div class="supp-card" data-cat="foundation"><div class="supp-top"><span class="supp-cat">Foundation</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Sport Multivitamin</div><div class="supp-dose">Daily · Capsule</div><div class="supp-use">Fills micronutrient gaps when training volume is high. The insurance policy for the entire system. NSF-certified only.</div><div class="supp-timing">⏱ AM with breakfast</div></div>
      <div class="supp-card" data-cat="gut"><div class="supp-top"><span class="supp-cat">Gut Health</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Probiotic Multi-Strain</div><div class="supp-dose">30–50 billion CFU · Capsule</div><div class="supp-use">Supports gut integrity, immune function, and nutrient absorption. High training stress suppresses gut health.</div><div class="supp-timing">⏱ AM on empty stomach</div></div>
      <div class="supp-card" data-cat="gut"><div class="supp-top"><span class="supp-cat">Joint Health</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Curcumin + Piperine</div><div class="supp-dose">500–1000mg / day · Capsule</div><div class="supp-use">Potent anti-inflammatory for joint pain. Piperine boosts bioavailability 20x. Best for heavy contact sports.</div><div class="supp-timing">⏱ With meals</div></div>
    </div>
  </div>
</section>

<section id="proof" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Early Results</div>
    <h2 class="s-title reveal">BUILT FOR YOUR PROGRAM</h2>
    <div class="proof-grid">
      <div class="proof-card reveal"><div class="proof-logo">Early Pilot</div><p class="proof-quote">"We onboarded 80 athletes in a single afternoon. The dietitian dashboard lets me see every recommendation before the athlete does."</p><div class="proof-author">— Sports Dietitian</div><div class="proof-role">D1 Athletic Department</div></div>
      <div class="proof-card reveal"><div class="proof-logo">Early Pilot</div><p class="proof-quote">"The NCAA compliance cross-referencing alone is worth it. Our compliance office finally has a traceable record of what every athlete is taking."</p><div class="proof-author">— Athletic Director</div><div class="proof-role">D1 Athletic Department</div></div>
      <div class="proof-card reveal"><div class="proof-logo">Early Pilot</div><p class="proof-quote">"Athletes actually use it. The AI chat answers supplement questions so I am not getting 50 texts a day. Game changer for my workload."</p><div class="proof-author">— Sports Dietitian</div><div class="proof-role">D1 Athletic Department</div></div>
    </div>
  </div>
</section>

<section id="faq" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Questions</div>
    <h2 class="s-title reveal">STRAIGHT ANSWERS</h2>
    <div class="faq-wrap">
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Is IBEX actually NCAA compliant?<span class="faq-icon">+</span></div><div class="faq-a">Every ingredient is cross-referenced against the NCAA banned substance list before it can be recommended. We only include NSF Certified for Sport or third-party tested products. Your dietitian's review step is the final safeguard.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Does the dietitian have to approve every recommendation?<span class="faq-icon">+</span></div><div class="faq-a">Yes. Every AI-generated recommendation routes to the dietitian dashboard before the athlete sees their protocol. The dietitian can approve, modify, or flag any recommendation. IBEX augments the dietitian, it never replaces them.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">How long does onboarding take?<span class="faq-icon">+</span></div><div class="faq-a">The department dashboard is live in under 30 minutes. Athletes complete their audit in 3 minutes. A full program of 500 athletes can be onboarded in a single week.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Do you handle supplement fulfillment or shipping?<span class="faq-icon">+</span></div><div class="faq-a">No. IBEX is pure software. We recommend products with affiliate links to trusted suppliers like Thorne, Momentous, and Klean Athlete. No inventory risk, no shipping logistics, no liability for product quality.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">What sports does IBEX support?<span class="faq-icon">+</span></div><div class="faq-a">All D1 sports. The AI differentiates protocols by sport, position, season status, and individual physiology. A football lineman and a cross country runner get completely different recommendations.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">How is athlete data handled?<span class="faq-icon">+</span></div><div class="faq-a">Athlete data is stored securely with access controls. Department dietitians have visibility into their athletes only. We do not sell data to third parties. See the full Privacy Policy section below.</div></div>
    </div>
  </div>
</section>

<section id="privacy" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Legal</div>
    <h2 class="s-title reveal">PRIVACY POLICY</h2>
    <div class="priv-body reveal">
      <p>Effective: March 2025. IBEX provides a supplement intelligence platform for D1 athletes and athletic departments. This policy explains what we collect, how we use it, and your rights.</p>
      <h3>What We Collect</h3>
      <ul>
        <li>Contact info: name and email (optional)</li>
        <li>Athletic profile: sport, position, school, season status, training inputs</li>
        <li>Lifestyle inputs: sleep, stress, soreness, goals, sensitivities</li>
        <li>Usage data: audit reference ID and basic operational logs</li>
      </ul>
      <h3>What We Do NOT Collect</h3>
      <ul>
        <li>We do not require student IDs, SSNs, or financial information</li>
        <li>We do not sell personal data to third parties</li>
        <li>We do not use your data for advertising</li>
      </ul>
      <h3>How We Use Your Information</h3>
      <ul>
        <li>Generate your personalized supplement protocol and timing schedule</li>
        <li>Power the Ask IBEX chat using your audit as context</li>
        <li>Route recommendations to your sports dietitian for review and approval</li>
        <li>Improve reliability and safety controls through aggregate analysis</li>
      </ul>
      <h3>AI Processing</h3>
      <p>Your audit inputs may be sent to an AI provider to generate structured output. We instruct the model to avoid medical diagnosis and never invent research citations.</p>
      <h3>NCAA Compliance Notice</h3>
      <p>All catalog ingredients are cross-referenced against the NCAA banned substance list. No platform can guarantee compliance for every individual case. Always confirm with your athletic department and compliance office.</p>
      <h3>Data Security and Retention</h3>
      <p>Data is stored securely with access controls and encryption in transit. Department administrators have visibility into their athletes data only. We retain audit data as long as needed to provide the service.</p>
      <h3>Your Rights</h3>
      <p>To request access to or deletion of your data, email <a href="mailto:{SUPPORT_EMAIL}" style="color:var(--gold);">{SUPPORT_EMAIL}</a> with your IBEX Audit ID. We respond within 5 business days.</p>
      <h3>Contact</h3>
      <p>Privacy questions: <a href="mailto:{SUPPORT_EMAIL}" style="color:var(--gold);">{SUPPORT_EMAIL}</a></p>
    </div>
  </div>
</section>

<section id="contact" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Get In Touch</div>
    <h2 class="s-title reveal">CONTACT US</h2>
    <div class="contact-grid">
      <div class="contact-card featured reveal">
        <div class="contact-clabel">Athletic Departments</div>
        <div class="contact-ctitle">Request a Meeting</div>
        <div class="contact-body">Interested in IBEX for your program? We will set up a call, walk you through the platform, and answer any questions from your sports dietitian or compliance staff.</div>
        <a href="mailto:{SUPPORT_EMAIL}?subject=IBEX Meeting Request — [Your School]&body=Hi,%0A%0AI am interested in learning more about IBEX for our athletic department.%0A%0ASchool: %0ARole: %0AApprox. number of athletes: %0A%0AAvailable times: " class="contact-email-link">{SUPPORT_EMAIL}</a>
        <div class="contact-detail">We respond within 24 hours</div>
      </div>
      <div style="display:flex;flex-direction:column;gap:1rem;">
        <div class="contact-card reveal">
          <div class="contact-clabel">Athletes</div>
          <div class="contact-ctitle" style="font-size:1.3rem;">Audit Questions</div>
          <div class="contact-body" style="font-size:.82rem;">Questions about your stack, protocol, or Audit ID? Email us or use the Ask IBEX chat inside the app.</div>
          <a href="mailto:{SUPPORT_EMAIL}?subject=Athlete Question" class="contact-email-link" style="font-size:.88rem;">{SUPPORT_EMAIL}</a>
        </div>
        <div class="contact-card reveal">
          <div class="contact-clabel">General</div>
          <div class="contact-ctitle" style="font-size:1.3rem;">Everything Else</div>
          <div class="contact-body" style="font-size:.82rem;">Press inquiries, partnerships, feedback, or data deletion requests.</div>
          <a href="mailto:{SUPPORT_EMAIL}" class="contact-email-link" style="font-size:.88rem;">{SUPPORT_EMAIL}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="cta">
  <h2 class="cta-title reveal">READY TO GIVE<br>YOUR ATHLETES<br>AN <em>EDGE?</em></h2>
  <p class="cta-sub reveal">Email us and we will get your program set up.</p>
  <div class="cta-actions reveal">
    <a class="btn-gold" href="mailto:{SUPPORT_EMAIL}?subject=IBEX Meeting Request — [Your School]">Email Us →</a>
    <a class="btn-outline" href="{AUDIT_URL}" target="_top">Try the Athlete Audit</a>
  </div>
</section>

<footer>
  <span class="f-word">IBEX</span>
  <span class="f-copy">© 2025 IBEX. Precision supplement intelligence for D1 athletics.</span>
  <div class="f-links">
    <a onclick="scrollTo('problem')">The Problem</a>
    <a onclick="scrollTo('how')">How It Works</a>
    <a onclick="scrollTo('plans')">Pricing</a>
    <a onclick="scrollTo('contact')">Contact</a>
    <a onclick="scrollTo('privacy')">Privacy Policy</a>
    <a href="{AUDIT_URL}" target="_top">Athlete Audit</a>
  </div>
  <p class="f-disc">IBEX is not a medical provider. All recommendations are cross-referenced against the NCAA banned substance list but cannot be guaranteed compliant for every individual case. The sports dietitian review step is required before athletes receive approved protocols. Always confirm supplement use with your athletic department and compliance office.</p>
</footer>

<script>
function scrollTo(id) {{
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({{behavior: 'smooth', block: 'start'}});
}}
const io = new IntersectionObserver((entries) => {{
  entries.forEach((e,i) => {{
    if(e.isIntersecting){{ setTimeout(()=>e.target.classList.add('visible'), i*60); io.unobserve(e.target); }}
  }});
}},{{threshold:0.06}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
document.querySelectorAll('.cat-btn').forEach(btn=>{{
  btn.addEventListener('click',()=>{{
    document.querySelectorAll('.cat-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const cat=btn.dataset.cat;
    document.querySelectorAll('.supp-card').forEach(card=>{{
      card.classList.toggle('hidden', cat!=='all' && card.dataset.cat!==cat);
    }});
  }});
}});
</script>
</body>
</html>"""

components.html(HTML, height=7000, scrolling=True)
