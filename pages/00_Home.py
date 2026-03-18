"""
IBEX — Landing Page  (pages/00_Home.py)
B2B focused: selling to athletic departments, not individual athletes.
No st.set_page_config() here — lives in root app.py only.
"""
import streamlit as st
import streamlit.components.v1 as components

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stSidebar"] { display: none !important; }
[data-testid="collapsedControl"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

AUDIT_URL = "https://ibexsupplements.streamlit.app/Audit"
ADMIN_URL = "https://ibexsupplements.streamlit.app/Admin"

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;600;700&family=Barlow+Condensed:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --black:#0a0a0f;--navy:#0b1220;--navy2:#132033;
  --off:#f0ede6;--gold:#c9a84c;--gold2:#e8c97a;
  --muted:rgba(240,237,230,0.52);--border:rgba(201,168,76,0.18);
  --green:#4ade80;--blue:#7dd3fc;
}}
html{{scroll-behavior:smooth}}
body{{background:var(--black);color:var(--off);font-family:'Barlow',sans-serif;font-weight:300;overflow-x:hidden}}

/* NAV */
nav{{position:sticky;top:0;z-index:999;display:flex;align-items:center;justify-content:space-between;padding:.85rem 3rem;background:rgba(10,10,15,0.97);backdrop-filter:blur(16px);border-bottom:1px solid var(--border)}}
.nav-word{{font-family:'Bebas Neue',sans-serif;font-size:1.75rem;letter-spacing:.1em;color:var(--gold);text-decoration:none}}
.nav-links{{display:flex;gap:2rem;list-style:none}}
.nav-links a{{font-family:'Barlow Condensed',sans-serif;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--off);opacity:.6;text-decoration:none;transition:opacity .2s,color .2s}}
.nav-links a:hover{{opacity:1;color:var(--gold)}}
.nav-btns{{display:flex;gap:.75rem}}
.btn-nav-ghost{{font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;font-weight:600;padding:.45rem 1rem;border:1px solid var(--border);color:var(--muted);text-decoration:none;transition:all .2s}}
.btn-nav-ghost:hover{{border-color:var(--gold);color:var(--gold)}}
.btn-nav{{font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;background:var(--gold);color:var(--black);padding:.45rem 1rem;text-decoration:none;transition:background .2s}}
.btn-nav:hover{{background:var(--gold2)}}

/* HERO */
#hero{{min-height:95vh;display:flex;flex-direction:column;justify-content:center;padding:6rem 3.5rem 4rem;position:relative;overflow:hidden}}
.hero-bg{{position:absolute;right:-2%;top:50%;transform:translateY(-50%);font-family:'Bebas Neue',sans-serif;font-size:40vw;color:rgba(201,168,76,0.03);pointer-events:none;line-height:1;z-index:0}}
.hero-inner{{position:relative;z-index:1;max-width:900px}}
.hero-eyebrow{{font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);margin-bottom:1.8rem;opacity:0;animation:fadeUp .7s .1s forwards}}
.hero-h1{{font-family:'Bebas Neue',sans-serif;font-size:clamp(4rem,9vw,9.5rem);line-height:.88;letter-spacing:.02em;margin-bottom:2rem;opacity:0;animation:fadeUp .7s .25s forwards}}
.hero-h1 em{{color:var(--gold);font-style:normal}}
.hero-sub{{font-size:1.1rem;line-height:1.8;color:var(--muted);max-width:580px;margin-bottom:2.5rem;opacity:0;animation:fadeUp .7s .4s forwards}}
.hero-actions{{display:flex;gap:1rem;align-items:center;flex-wrap:wrap;margin-bottom:3rem;opacity:0;animation:fadeUp .7s .55s forwards}}
.btn-gold{{font-family:'Barlow Condensed',sans-serif;font-size:.82rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;background:var(--gold);color:var(--black);padding:1rem 2.2rem;text-decoration:none;display:inline-block;transition:background .2s,transform .15s;border:none;cursor:pointer}}
.btn-gold:hover{{background:var(--gold2);transform:translateY(-2px)}}
.btn-outline{{font-family:'Barlow Condensed',sans-serif;font-size:.82rem;letter-spacing:.2em;text-transform:uppercase;font-weight:600;border:1px solid var(--border);color:var(--muted);padding:1rem 2.2rem;text-decoration:none;display:inline-block;transition:all .2s}}
.btn-outline:hover{{border-color:var(--gold);color:var(--gold)}}
.hero-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--border);border:1px solid var(--border);max-width:700px;opacity:0;animation:fadeUp .7s .7s forwards}}
.stat-box{{background:var(--black);padding:1.5rem 1.2rem}}
.stat-num{{font-family:'Bebas Neue',sans-serif;font-size:2.8rem;color:var(--gold);line-height:1;margin-bottom:.2rem}}
.stat-label{{font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}}

/* TICKER */
.ticker{{background:var(--gold);overflow:hidden;padding:.6rem 0;white-space:nowrap}}
.ticker-inner{{display:inline-flex;animation:ticker 35s linear infinite}}
.t-item{{font-family:'Barlow Condensed',sans-serif;font-size:.7rem;letter-spacing:.25em;text-transform:uppercase;color:var(--black);font-weight:700;padding:0 2rem}}
.t-dot{{color:rgba(0,0,0,.25)}}
@keyframes ticker{{0%{{transform:translateX(0)}}100%{{transform:translateX(-50%)}}}}

/* SECTION */
.section{{padding:7rem 3.5rem}}
.section-inner{{max-width:1200px;margin:0 auto}}
.s-label{{font-family:'Barlow Condensed',sans-serif;font-size:.63rem;letter-spacing:.4em;text-transform:uppercase;color:var(--gold);margin-bottom:.7rem}}
.s-title{{font-family:'Bebas Neue',sans-serif;font-size:clamp(2.6rem,5vw,5rem);line-height:.93;margin-bottom:2.5rem}}
.s-sub{{font-size:.95rem;line-height:1.8;color:var(--muted);max-width:600px;margin-bottom:3rem}}

/* PROBLEM / SOLUTION */
#problem{{background:var(--navy)}}
.prob-grid{{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:start}}
.prob-list{{list-style:none}}
.prob-list li{{padding:1.2rem 0;border-bottom:1px solid rgba(201,168,76,.1);font-size:.92rem;line-height:1.7;color:rgba(240,237,230,.7);display:flex;gap:1rem;align-items:flex-start}}
.prob-list li::before{{content:'✗';color:#ef4444;font-size:.9rem;flex-shrink:0;margin-top:.1rem}}
.sol-list{{list-style:none}}
.sol-list li{{padding:1.2rem 0;border-bottom:1px solid rgba(201,168,76,.1);font-size:.92rem;line-height:1.7;color:rgba(240,237,230,.7);display:flex;gap:1rem;align-items:flex-start}}
.sol-list li::before{{content:'→';color:var(--gold);flex-shrink:0}}
.col-head{{font-family:'Barlow Condensed',sans-serif;font-size:1.3rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;margin-bottom:1rem}}
.col-head.red{{color:#ef4444}}
.col-head.gold{{color:var(--gold)}}

/* HOW */
#how{{background:var(--black)}}
.steps{{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--border)}}
.step{{padding:2.5rem 2rem;border-right:1px solid var(--border);transition:background .3s;position:relative}}
.step:last-child{{border-right:none}}
.step:hover{{background:rgba(201,168,76,.04)}}
.step-num{{font-family:'Bebas Neue',sans-serif;font-size:3.5rem;color:rgba(201,168,76,.1);line-height:1;margin-bottom:.8rem}}
.step-title{{font-family:'Barlow Condensed',sans-serif;font-size:1rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--off);margin-bottom:.6rem}}
.step-body{{font-size:.84rem;line-height:1.75;color:var(--muted)}}
.step-who{{margin-top:.8rem;font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}}

/* PLANS - B2B FOCUS */
#plans{{background:var(--navy);position:relative;overflow:hidden}}
#plans::before{{content:'IBEX';position:absolute;right:-.02em;bottom:-.1em;font-family:'Bebas Neue',sans-serif;font-size:22vw;color:rgba(201,168,76,.025);pointer-events:none;line-height:1}}
#plans .section-inner{{position:relative;z-index:1}}
.plan-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem}}
.plan-card{{border:1px solid var(--border);padding:2.5rem;position:relative;transition:border-color .3s}}
.plan-card:hover{{border-color:rgba(201,168,76,.45)}}
.plan-card.featured{{border-color:var(--gold);background:rgba(201,168,76,.03)}}
.plan-tag{{position:absolute;top:-1px;right:1.5rem;background:var(--gold);color:var(--black);font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;padding:.25rem .7rem}}
.plan-tier{{font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);margin-bottom:.7rem}}
.plan-price{{font-family:'Bebas Neue',sans-serif;font-size:3.5rem;line-height:1;margin-bottom:.15rem}}
.plan-price sup{{font-size:1.5rem;vertical-align:top;margin-top:.5rem}}
.plan-period{{font-size:.78rem;color:var(--muted);margin-bottom:.4rem}}
.plan-athletes{{font-family:'Barlow Condensed',sans-serif;font-size:.72rem;letter-spacing:.1em;color:var(--gold);margin-bottom:1.8rem}}
.plan-features{{list-style:none;margin-bottom:2rem}}
.plan-features li{{font-size:.84rem;line-height:1.65;padding:.5rem 0;border-bottom:1px solid rgba(201,168,76,.08);color:rgba(240,237,230,.7);display:flex;gap:.65rem}}
.plan-features li::before{{content:'→';color:var(--gold);flex-shrink:0}}
.btn-plan{{font-family:'Barlow Condensed',sans-serif;font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;padding:.85rem;border:1px solid var(--gold);color:var(--gold);background:transparent;cursor:pointer;text-decoration:none;display:block;text-align:center;transition:all .2s}}
.btn-plan:hover{{background:var(--gold);color:var(--black)}}
.plan-card.featured .btn-plan{{background:var(--gold);color:var(--black)}}

/* CATALOG */
#catalog{{background:var(--black)}}
.cat-filter{{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem}}
.cat-btn{{font-family:'Barlow Condensed',sans-serif;font-size:.63rem;letter-spacing:.18em;text-transform:uppercase;font-weight:600;padding:.32rem .8rem;border:1px solid var(--border);background:transparent;color:var(--muted);cursor:pointer;transition:all .2s}}
.cat-btn:hover,.cat-btn.active{{background:var(--gold);color:var(--black);border-color:var(--gold)}}
.supp-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1px;background:var(--border);border:1px solid var(--border)}}
.supp-card{{background:var(--black);padding:1.5rem;transition:background .25s}}
.supp-card:hover{{background:rgba(201,168,76,.04)}}
.supp-card.hidden{{display:none}}
.supp-top{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:.6rem}}
.supp-cat{{font-family:'Barlow Condensed',sans-serif;font-size:.57rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}}
.supp-badges{{display:flex;gap:.25rem}}
.badge{{font-family:'Barlow Condensed',sans-serif;font-size:.5rem;letter-spacing:.1em;text-transform:uppercase;font-weight:700;padding:.15rem .4rem;border:1px solid rgba(201,168,76,.25);color:var(--gold)}}
.badge.ncaa{{border-color:rgba(74,222,128,.35);color:var(--green)}}
.badge.nsf{{border-color:rgba(125,211,252,.35);color:var(--blue)}}
.supp-name{{font-family:'Barlow Condensed',sans-serif;font-size:1.05rem;font-weight:700;color:var(--off);margin-bottom:.2rem}}
.supp-dose{{font-size:.74rem;color:var(--muted);margin-bottom:.45rem}}
.supp-use{{font-size:.78rem;line-height:1.65;color:rgba(240,237,230,.55)}}
.supp-timing{{margin-top:.65rem;font-family:'Barlow Condensed',sans-serif;font-size:.58rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(201,168,76,.6)}}

/* ADMIN PREVIEW */
#admin{{background:var(--navy)}}
.admin-preview{{border:1px solid var(--border);overflow:hidden}}
.admin-bar{{background:var(--black);border-bottom:1px solid var(--border);padding:1rem 1.5rem;display:flex;align-items:center;gap:1rem}}
.admin-dot{{width:10px;height:10px;border-radius:50%}}
.admin-dot.r{{background:#ef4444}}.admin-dot.y{{background:#f59e0b}}.admin-dot.g{{background:#4ade80}}
.admin-title{{font-family:'Barlow Condensed',sans-serif;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-left:.5rem}}
.admin-body{{padding:1.5rem}}
.admin-metrics{{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-bottom:1.5rem}}
.metric-box{{background:var(--black);border:1px solid var(--border);padding:1rem}}
.metric-val{{font-family:'Bebas Neue',sans-serif;font-size:2rem;color:var(--gold);line-height:1}}
.metric-lbl{{font-family:'Barlow Condensed',sans-serif;font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-top:.2rem}}
.admin-table{{width:100%;border-collapse:collapse}}
.admin-table th{{font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);padding:.6rem 1rem;text-align:left;border-bottom:1px solid var(--border)}}
.admin-table td{{font-size:.82rem;color:rgba(240,237,230,.75);padding:.7rem 1rem;border-bottom:1px solid rgba(201,168,76,.06)}}
.admin-table tr:hover td{{background:rgba(201,168,76,.03)}}
.status-pill{{font-family:'Barlow Condensed',sans-serif;font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;padding:.2rem .5rem;border-radius:2px}}
.status-pill.reviewed{{background:rgba(74,222,128,.12);color:var(--green);border:1px solid rgba(74,222,128,.25)}}
.status-pill.pending{{background:rgba(201,168,76,.12);color:var(--gold);border:1px solid rgba(201,168,76,.25)}}
.status-pill.flagged{{background:rgba(239,68,68,.12);color:#ef4444;border:1px solid rgba(239,68,68,.25)}}

/* PROOF */
#proof{{background:var(--black)}}
.proof-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:1.5rem}}
.proof-card{{border:1px solid rgba(201,168,76,.1);padding:2rem;transition:all .3s}}
.proof-card:hover{{border-color:rgba(201,168,76,.3);background:rgba(201,168,76,.02)}}
.proof-logo{{font-family:'Bebas Neue',sans-serif;font-size:1.5rem;color:var(--gold);margin-bottom:.5rem;letter-spacing:.05em}}
.proof-quote{{font-size:.88rem;line-height:1.75;color:rgba(240,237,230,.65);font-style:italic;margin-bottom:1.2rem}}
.proof-author{{font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}}
.proof-role{{font-size:.73rem;color:rgba(240,237,230,.3);margin-top:.15rem}}

/* FAQ */
#faq{{background:var(--navy)}}
.faq-wrap{{max-width:820px}}
.faq-item{{border-bottom:1px solid rgba(201,168,76,.12)}}
.faq-q{{display:flex;justify-content:space-between;align-items:center;padding:1.4rem 0;cursor:pointer;user-select:none;font-family:'Barlow Condensed',sans-serif;font-size:1.05rem;font-weight:700;letter-spacing:.02em;color:var(--off);gap:1rem}}
.faq-icon{{color:var(--gold);font-size:1.2rem;flex-shrink:0;transition:transform .3s}}
.faq-a{{max-height:0;overflow:hidden;font-size:.86rem;line-height:1.8;color:var(--muted);transition:max-height .4s ease,padding .3s}}
.faq-item.open .faq-a{{max-height:280px;padding-bottom:1.4rem}}
.faq-item.open .faq-icon{{transform:rotate(45deg)}}

/* CTA */
#cta{{background:var(--black);padding:9rem 3.5rem;text-align:center;position:relative;overflow:hidden}}
#cta::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 55% 55% at 50% 50%,rgba(201,168,76,.07) 0%,transparent 70%);pointer-events:none}}
.cta-title{{font-family:'Bebas Neue',sans-serif;font-size:clamp(3.5rem,7vw,7rem);line-height:.93;margin-bottom:1.3rem;position:relative;z-index:1}}
.cta-title em{{color:var(--gold);font-style:normal}}
.cta-sub{{font-size:1rem;color:var(--muted);margin-bottom:2.5rem;position:relative;z-index:1}}
.cta-actions{{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;position:relative;z-index:1}}

/* FOOTER */
footer{{padding:2rem 3.5rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap}}
.f-word{{font-family:'Bebas Neue',sans-serif;font-size:1.4rem;letter-spacing:.1em;color:var(--gold)}}
.f-copy{{font-size:.7rem;color:rgba(240,237,230,.2)}}
.f-links{{display:flex;gap:1.5rem}}
.f-links a{{font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(240,237,230,.28);text-decoration:none;transition:color .2s}}
.f-links a:hover{{color:var(--gold)}}
.f-disc{{width:100%;font-size:.67rem;color:rgba(240,237,230,.2);line-height:1.6;border-top:1px solid rgba(201,168,76,.07);padding-top:1rem;margin-top:.5rem}}

/* ANIMATIONS */
@keyframes fadeUp{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
.reveal{{opacity:0;transform:translateY(20px);transition:opacity .65s ease,transform .65s ease}}
.reveal.visible{{opacity:1;transform:translateY(0)}}

@media(max-width:900px){{
  nav{{padding:.9rem 1.5rem}}.nav-links{{display:none}}
  #hero{{padding:5rem 1.5rem 3rem}}
  .hero-stats{{grid-template-columns:1fr 1fr}}
  .section{{padding:5rem 1.5rem}}
  .steps,.plan-grid,.proof-grid{{grid-template-columns:1fr}}
  .step{{border-right:none;border-bottom:1px solid var(--border)}}
  .prob-grid,.admin-metrics{{grid-template-columns:1fr 1fr}}
  footer{{flex-direction:column;text-align:center}}
}}
</style>
</head>
<body>

<nav>
  <a class="nav-word" href="#">IBEX</a>
  <ul class="nav-links">
    <li><a href="#problem">The Problem</a></li>
    <li><a href="#how">How It Works</a></li>
    <li><a href="#plans">Pricing</a></li>
    <li><a href="#admin">Admin Dashboard</a></li>
    <li><a href="#faq">FAQ</a></li>
  </ul>
  <div class="nav-btns">
    <a class="btn-nav-ghost" href="{AUDIT_URL}" target="_top">Athlete Audit</a>
    <a class="btn-nav" href="#cta">Request Demo</a>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-bg">I</div>
  <div class="hero-inner">
    <div class="hero-eyebrow">The NCAA-Compliant Supplement Intelligence Platform for D1 Athletics</div>
    <h1 class="hero-h1">ONE DIETITIAN.<br>500 ATHLETES.<br><em>ZERO GUESSWORK.</em></h1>
    <p class="hero-sub">IBEX gives every athlete at your program a personalized, AI-generated supplement protocol — reviewed by your sports dietitian, NCAA-compliant, and evidence-linked. Scalable nutrition intelligence for the entire department.</p>
    <div class="hero-actions">
      <a class="btn-gold" href="#cta">Request a Demo →</a>
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

<!-- TICKER -->
<div class="ticker">
  <div class="ticker-inner">
    <span class="t-item">NCAA Compliant Catalog</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Dietitian Dashboard</span><span class="t-dot"> ✦ </span>
    <span class="t-item">AI-Personalized Protocols</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Evidence-Linked Ingredients</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Sport + Position Specific</span><span class="t-dot"> ✦ </span>
    <span class="t-item">In-Season & Off-Season Protocols</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Zero Inventory Risk</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Compliance Audit Trail</span><span class="t-dot"> ✦ </span>
    <span class="t-item">NCAA Compliant Catalog</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Dietitian Dashboard</span><span class="t-dot"> ✦ </span>
    <span class="t-item">AI-Personalized Protocols</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Evidence-Linked Ingredients</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Sport + Position Specific</span><span class="t-dot"> ✦ </span>
    <span class="t-item">In-Season & Off-Season Protocols</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Zero Inventory Risk</span><span class="t-dot"> ✦ </span>
    <span class="t-item">Compliance Audit Trail</span><span class="t-dot"> ✦ </span>
  </div>
</div>

<!-- PROBLEM / SOLUTION -->
<section id="problem" class="section">
  <div class="section-inner">
    <div class="s-label reveal">The Gap</div>
    <h2 class="s-title reveal">WHY THIS<br>MATTERS NOW</h2>
    <div class="prob-grid">
      <div class="reveal">
        <div class="col-head red">The Problem</div>
        <ul class="prob-list">
          <li>One sports dietitian covering 20+ sports and 500+ athletes cannot give individualized supplement guidance</li>
          <li>Athletes self-prescribe from GNC, Amazon, and Instagram influencers — with zero compliance verification</li>
          <li>One NCAA violation from a contaminated supplement can cost a championship and millions in reputation damage</li>
          <li>No standardized, traceable record of what each athlete is taking and why</li>
          <li>Generic supplement recommendations ignore sport, position, season, and individual physiology</li>
        </ul>
      </div>
      <div class="reveal">
        <div class="col-head gold">The IBEX Solution</div>
        <ul class="sol-list">
          <li>AI generates a personalized, sport-specific protocol for every athlete in 3 minutes — dietitian reviews and approves</li>
          <li>Every ingredient cross-referenced against the NCAA banned substance list before it's recommended</li>
          <li>Full audit trail: every recommendation logged with athlete ID, date, plan, and dietitian approval status</li>
          <li>Compliance dashboard gives your AD and compliance team visibility across the entire program</li>
          <li>In-season vs off-season protocol adjustments built in — the system adapts as the year changes</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how" class="section">
  <div class="section-inner">
    <div class="s-label reveal">The Process</div>
    <h2 class="s-title reveal">HOW IBEX<br>WORKS</h2>
    <div class="steps">
      <div class="step reveal">
        <div class="step-num">01</div>
        <div class="step-title">Department Onboards</div>
        <p class="step-body">Your sports dietitian sets up the department portal, configures sport-specific settings, and invites athletes via a secure link. 30 minutes to deploy across the entire program.</p>
        <div class="step-who">⚙ Dietitian</div>
      </div>
      <div class="step reveal">
        <div class="step-num">02</div>
        <div class="step-title">Athlete Runs Audit</div>
        <p class="step-body">Each athlete completes a 15-question audit covering sport, position, training load, sleep, stress, goals, and sensitivities. AI generates a personalized protocol instantly.</p>
        <div class="step-who">🏃 Athlete</div>
      </div>
      <div class="step reveal">
        <div class="step-num">03</div>
        <div class="step-title">Dietitian Reviews</div>
        <p class="step-body">Every AI recommendation routes to the dietitian dashboard for approval, modification, or flagging before the athlete sees their final protocol. You stay in control.</p>
        <div class="step-who">⚕ Dietitian</div>
      </div>
      <div class="step reveal">
        <div class="step-num">04</div>
        <div class="step-title">Athletes Follow Protocol</div>
        <p class="step-body">Approved athletes receive their personalized stack with exact dosing, AM/PM/Training schedule, and access to Ask IBEX chat for ongoing questions — all grounded in their approved protocol.</p>
        <div class="step-who">🏆 Athlete + Dietitian</div>
      </div>
    </div>
  </div>
</section>

<!-- ADMIN DASHBOARD PREVIEW -->
<section id="admin" class="section">
  <div class="section-inner">
    <div class="s-label reveal">For Sports Dietitians</div>
    <h2 class="s-title reveal">THE DIETITIAN<br>DASHBOARD</h2>
    <p class="s-sub reveal">See every athlete's audit, review AI recommendations, approve or modify protocols, and flag compliance concerns — all in one place. Full visibility across every sport in your program.</p>
    <div class="admin-preview reveal">
      <div class="admin-bar">
        <div class="admin-dot r"></div><div class="admin-dot y"></div><div class="admin-dot g"></div>
        <span class="admin-title">IBEX Admin — Lehigh University Athletics</span>
      </div>
      <div class="admin-body">
        <div class="admin-metrics">
          <div class="metric-box"><div class="metric-val">247</div><div class="metric-lbl">Total Athletes</div></div>
          <div class="metric-box"><div class="metric-val">189</div><div class="metric-lbl">Audits Completed</div></div>
          <div class="metric-box"><div class="metric-val">164</div><div class="metric-lbl">Protocols Approved</div></div>
          <div class="metric-box"><div class="metric-val">3</div><div class="metric-lbl">Flagged for Review</div></div>
        </div>
        <table class="admin-table">
          <thead>
            <tr>
              <th>Athlete</th><th>Sport</th><th>Position</th><th>Plan</th><th>Audit Date</th><th>Status</th><th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr><td>J. Williams</td><td>Football</td><td>Linebacker</td><td>Performance</td><td>Mar 18, 2025</td><td><span class="status-pill reviewed">Approved</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;">View →</td></tr>
            <tr><td>M. Chen</td><td>Swimming</td><td>Freestyle</td><td>Basic</td><td>Mar 17, 2025</td><td><span class="status-pill reviewed">Approved</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;">View →</td></tr>
            <tr><td>A. Rodriguez</td><td>Track & Field</td><td>400m</td><td>Performance</td><td>Mar 17, 2025</td><td><span class="status-pill pending">Pending</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;">Review →</td></tr>
            <tr><td>T. Johnson</td><td>Wrestling</td><td>165lb</td><td>Performance</td><td>Mar 16, 2025</td><td><span class="status-pill flagged">Flagged</span></td><td style="color:#ef4444;font-family:'Barlow Condensed',sans-serif;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;">Urgent →</td></tr>
            <tr><td>S. Park</td><td>Soccer</td><td>Midfielder</td><td>Basic</td><td>Mar 16, 2025</td><td><span class="status-pill reviewed">Approved</span></td><td style="color:var(--gold);font-family:'Barlow Condensed',sans-serif;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;">View →</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<!-- PLANS -->
<section id="plans" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Pricing</div>
    <h2 class="s-title reveal">DEPARTMENT<br>LICENSING</h2>
    <p class="s-sub reveal">One license covers your entire athletic department. No per-athlete fees. No inventory. No surprises.</p>
    <div class="plan-grid">
      <div class="plan-card reveal">
        <div class="plan-tier">Starter Program</div>
        <div class="plan-price"><sup>$</sup>500</div>
        <div class="plan-period">/ month · billed annually</div>
        <div class="plan-athletes">Up to 300 athletes</div>
        <ul class="plan-features">
          <li>Full AI audit tool for all athletes</li>
          <li>Dietitian review dashboard</li>
          <li>NCAA-compliant catalog access</li>
          <li>AM / PM / Training schedule per athlete</li>
          <li>Ask IBEX chat per athlete</li>
          <li>Basic compliance reporting</li>
          <li>Email support</li>
        </ul>
        <a class="btn-plan" href="#cta">Request Demo</a>
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
          <li>Multi-sport performance analytics</li>
          <li>Affiliate product links (revenue share)</li>
          <li>Priority support + onboarding call</li>
          <li>Custom branding on athlete portal</li>
        </ul>
        <a class="btn-plan" href="#cta">Request Demo</a>
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
        <a class="btn-plan" href="#cta">Contact Sales</a>
      </div>
    </div>
    <p style="font-size:.8rem;color:var(--muted);margin-top:1.5rem;text-align:center;">Athletes can also access IBEX individually — <a href="{AUDIT_URL}" target="_top" style="color:var(--gold);">free audit tool available here</a>.</p>
  </div>
</section>

<!-- SUPPLEMENT CATALOG -->
<section id="catalog" class="section">
  <div class="section-inner">
    <div class="s-label reveal">The Catalog</div>
    <h2 class="s-title reveal">WHAT ATHLETES<br>GET RECOMMENDED</h2>
    <p class="s-sub reveal">Every ingredient is NCAA-compliant, evidence-backed, and cross-referenced against the banned substance list. Nothing trendy. Nothing sketchy. Nothing that puts eligibility at risk.</p>
    <div class="cat-filter reveal">
      <button class="cat-btn active" data-cat="all">All</button>
      <button class="cat-btn" data-cat="strength">Strength</button>
      <button class="cat-btn" data-cat="recovery">Recovery</button>
      <button class="cat-btn" data-cat="endurance">Endurance</button>
      <button class="cat-btn" data-cat="sleep">Sleep</button>
      <button class="cat-btn" data-cat="foundation">Foundation</button>
      <button class="cat-btn" data-cat="gut">Gut & Joint</button>
    </div>
    <div class="supp-grid" id="suppGrid">
      <div class="supp-card" data-cat="strength"><div class="supp-top"><span class="supp-cat">Strength</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Creatine Monohydrate</div><div class="supp-dose">5g / day · Powder</div><div class="supp-use">Most-studied performance supplement ever. Increases phosphocreatine for explosive power, sprint capacity, and faster recovery between sets.</div><div class="supp-timing">⏱ Post-training or AM</div></div>
      <div class="supp-card" data-cat="strength"><div class="supp-top"><span class="supp-cat">Strength / Endurance</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Beta-Alanine</div><div class="supp-dose">3.2g / day · Powder or Capsule</div><div class="supp-use">Buffers lactic acid during repeated high-intensity efforts. Best for wrestling, lacrosse, rowing, basketball — sports with multiple bouts.</div><div class="supp-timing">⏱ Pre-training</div></div>
      <div class="supp-card" data-cat="strength"><div class="supp-top"><span class="supp-cat">Strength</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Whey Protein Isolate</div><div class="supp-dose">25–40g · Powder</div><div class="supp-use">Fast-digesting complete protein to start muscle protein synthesis. NSF Certified for Sport. Essential for high training volume and tight recovery windows.</div><div class="supp-timing">⏱ Within 30 min post-training</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Omega-3 Fish Oil</div><div class="supp-dose">2–3g EPA/DHA / day · Softgel</div><div class="supp-use">Reduces systemic inflammation, supports joint health and cardiovascular efficiency. Among the highest-evidence supplements for athletes.</div><div class="supp-timing">⏱ With meals</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Tart Cherry Extract</div><div class="supp-dose">480mg / day · Capsule</div><div class="supp-use">Reduces DOMS and exercise-induced muscle damage. Particularly effective for back-to-back game days and high-volume training blocks.</div><div class="supp-timing">⏱ AM + PM</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery / Sleep</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Magnesium Glycinate</div><div class="supp-dose">400mg / night · Capsule</div><div class="supp-use">Supports muscle relaxation, sleep quality, and protein synthesis. Most athletes deficient especially with high sweat rates.</div><div class="supp-timing">⏱ 30 min before bed</div></div>
      <div class="supp-card" data-cat="recovery"><div class="supp-top"><span class="supp-cat">Recovery / Joint</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Collagen + Vitamin C</div><div class="supp-dose">15g + 50mg · Powder</div><div class="supp-use">Taken 45 min pre-activity to stimulate connective tissue synthesis. Especially valuable for basketball, volleyball, wrestling, gymnastics.</div><div class="supp-timing">⏱ 45 min pre-training</div></div>
      <div class="supp-card" data-cat="endurance"><div class="supp-top"><span class="supp-cat">Endurance</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Electrolyte Complex</div><div class="supp-dose">Sodium / Potassium / Magnesium</div><div class="supp-use">Replaces sweat losses to maintain performance and prevent cramping. Essential during preseason camps, doubles, and multi-event days.</div><div class="supp-timing">⏱ During training</div></div>
      <div class="supp-card" data-cat="endurance"><div class="supp-top"><span class="supp-cat">Endurance / Vascular</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span></div></div><div class="supp-name">Beetroot Nitrate</div><div class="supp-dose">400mg nitrate · Powder or Capsule</div><div class="supp-use">Increases nitric oxide to improve blood flow and O2 efficiency. Strong evidence for swimming, rowing, soccer, cross country.</div><div class="supp-timing">⏱ 2–3 hrs pre-training</div></div>
      <div class="supp-card" data-cat="sleep"><div class="supp-top"><span class="supp-cat">Sleep</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Melatonin Low-Dose</div><div class="supp-dose">0.5–1mg · Capsule</div><div class="supp-use">Low-dose supports sleep onset without grogginess. Especially useful for travel across time zones and late-night practice schedules.</div><div class="supp-timing">⏱ 30 min before bed</div></div>
      <div class="supp-card" data-cat="sleep"><div class="supp-top"><span class="supp-cat">Sleep / Stress</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Ashwagandha KSM-66</div><div class="supp-dose">300–600mg / day · Capsule</div><div class="supp-use">Reduces cortisol and perceived stress. Improves sleep quality and recovery. Growing evidence for strength and VO2 max in high-stress phases.</div><div class="supp-timing">⏱ PM or with dinner</div></div>
      <div class="supp-card" data-cat="foundation"><div class="supp-top"><span class="supp-cat">Foundation</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Vitamin D3 + K2</div><div class="supp-dose">3000–5000 IU D3 + 100mcg K2 · Softgel</div><div class="supp-use">Bone health, immune function, testosterone, mood. A large proportion of D1 athletes are deficient — especially indoor sport athletes.</div><div class="supp-timing">⏱ AM with fat</div></div>
      <div class="supp-card" data-cat="foundation"><div class="supp-top"><span class="supp-cat">Foundation</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Sport Multivitamin</div><div class="supp-dose">Daily · Capsule</div><div class="supp-use">Fills micronutrient gaps when training volume is high and dietary variety limited. The insurance policy for the entire system. NSF-certified only.</div><div class="supp-timing">⏱ AM with breakfast</div></div>
      <div class="supp-card" data-cat="foundation"><div class="supp-top"><span class="supp-cat">Foundation</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Zinc + Copper</div><div class="supp-dose">25mg Zinc + 2mg Copper · Capsule</div><div class="supp-use">Supports immune function, testosterone, and recovery. Heavy training depletes zinc rapidly through sweat. Copper prevents zinc-induced deficiency.</div><div class="supp-timing">⏱ PM with food</div></div>
      <div class="supp-card" data-cat="gut"><div class="supp-top"><span class="supp-cat">Gut Health</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Probiotic Multi-Strain</div><div class="supp-dose">30–50 billion CFU · Capsule</div><div class="supp-use">Supports gut integrity, immune function, and nutrient absorption. High training stress suppresses gut health — foundational for high-volume athletes.</div><div class="supp-timing">⏱ AM on empty stomach</div></div>
      <div class="supp-card" data-cat="gut"><div class="supp-top"><span class="supp-cat">Joint Health</span><div class="supp-badges"><span class="badge ncaa">NCAA ✓</span><span class="badge nsf">NSF</span></div></div><div class="supp-name">Curcumin + Piperine</div><div class="supp-dose">500–1000mg / day · Capsule</div><div class="supp-use">Potent anti-inflammatory for joint pain and soreness. Piperine boosts bioavailability 20x. Best for athletes with chronic joint stress or heavy contact.</div><div class="supp-timing">⏱ With meals</div></div>
    </div>
  </div>
</section>

<!-- SOCIAL PROOF -->
<section id="proof" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Early Results</div>
    <h2 class="s-title reveal">BUILT FOR<br>YOUR PROGRAM</h2>
    <div class="proof-grid">
      <div class="proof-card reveal">
        <div class="proof-logo">Early Pilot</div>
        <p class="proof-quote">"We onboarded 80 athletes in a single afternoon. The dietitian dashboard lets me see every recommendation before the athlete does. This is exactly what we needed."</p>
        <div class="proof-author">— Sports Dietitian</div>
        <div class="proof-role">D1 Athletic Department</div>
      </div>
      <div class="proof-card reveal">
        <div class="proof-logo">Early Pilot</div>
        <p class="proof-quote">"The NCAA compliance cross-referencing alone is worth it. Our compliance office finally has a traceable record of what every athlete is taking and why."</p>
        <div class="proof-author">— Athletic Director</div>
        <div class="proof-role">D1 Athletic Department</div>
      </div>
      <div class="proof-card reveal">
        <div class="proof-logo">Early Pilot</div>
        <p class="proof-quote">"Athletes actually use it. The AI chat answers their questions so I'm not getting 50 texts a day asking if creatine is safe. Game changer for my workload."</p>
        <div class="proof-author">— Sports Dietitian</div>
        <div class="proof-role">D1 Athletic Department</div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section id="faq" class="section">
  <div class="section-inner">
    <div class="s-label reveal">Questions</div>
    <h2 class="s-title reveal">STRAIGHT<br>ANSWERS</h2>
    <div class="faq-wrap">
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Is IBEX actually NCAA compliant?<span class="faq-icon">+</span></div><div class="faq-a">Every ingredient in the IBEX catalog is cross-referenced against the NCAA banned substance list before it can be recommended. We only include NSF Certified for Sport or third-party tested products. That said, no platform can guarantee compliance for every individual case — your sports dietitian's review step is the final safeguard.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Does the dietitian have to approve every recommendation?<span class="faq-icon">+</span></div><div class="faq-a">Yes — that's a core feature, not an afterthought. Every AI-generated recommendation routes to the dietitian dashboard before the athlete sees their approved protocol. The dietitian can approve, modify, or flag any recommendation. IBEX augments the dietitian — it doesn't replace them.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">How long does onboarding take?<span class="faq-icon">+</span></div><div class="faq-a">The department dashboard is live in under 30 minutes. Athletes are invited via a secure link and complete their audit in 3 minutes. A full department of 500 athletes can be onboarded in a single week.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Do you handle supplement fulfillment or shipping?<span class="faq-icon">+</span></div><div class="faq-a">No — and that's intentional. IBEX is a pure software platform. We recommend products with affiliate links to trusted third-party tested suppliers (Thorne, Momentous, Klean Athlete). No inventory risk, no shipping logistics, no liability for product quality.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">What sports does IBEX support?<span class="faq-icon">+</span></div><div class="faq-a">All D1 sports. The AI is trained to differentiate protocols by sport, position, season status, and individual physiology. Football linemen and cross country runners get completely different recommendations — that's the point.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">How is athlete data handled?<span class="faq-icon">+</span></div><div class="faq-a">Athlete audit data is stored securely with access controls. The department dietitian has full visibility into their athletes' data. We do not sell athlete data to third parties. Full privacy policy available in the athlete-facing app.</div></div>
      <div class="faq-item reveal"><div class="faq-q" onclick="this.parentElement.classList.toggle('open')">Can we try it before committing?<span class="faq-icon">+</span></div><div class="faq-a">Yes. We offer a free pilot for one sport team (up to 30 athletes) with full dietitian dashboard access. Request a demo below and we'll get you set up within 48 hours.</div></div>
    </div>
  </div>
</section>

<!-- CTA -->
<section id="cta">
  <h2 class="cta-title reveal">READY TO<br>GIVE YOUR ATHLETES<br>AN <em>EDGE?</em></h2>
  <p class="cta-sub reveal">Request a free pilot for one of your sport teams. Up and running in 48 hours.</p>
  <div class="cta-actions reveal">
    <a class="btn-gold" href="mailto:support@ibexsupplements.com?subject=IBEX Demo Request&body=Hi, I'm interested in a pilot for our athletic department. School: [Your School] | Department size: [Approx # athletes] | Role: [Your title]">Request Demo →</a>
    <a class="btn-outline" href="{AUDIT_URL}" target="_top">Try the Athlete Audit</a>
  </div>
</section>

<footer>
  <span class="f-word">IBEX</span>
  <span class="f-copy">© 2025 IBEX. Precision supplement intelligence for D1 athletics.</span>
  <div class="f-links">
    <a href="#problem">The Problem</a>
    <a href="#how">How It Works</a>
    <a href="#plans">Pricing</a>
    <a href="{AUDIT_URL}" target="_top">Athlete Audit</a>
  </div>
  <p class="f-disc">IBEX is not a medical provider. All recommendations are cross-referenced against the NCAA banned substance list but cannot be guaranteed compliant for every individual case. The sports dietitian review step is required before athletes receive approved protocols. Always confirm supplement use with your athletic department and compliance office.</p>
</footer>

<script>
// Scroll reveal
const io = new IntersectionObserver((entries) => {{
  entries.forEach((e,i) => {{
    if(e.isIntersecting){{ setTimeout(()=>e.target.classList.add('visible'),i*70); io.unobserve(e.target); }}
  }});
}},{{threshold:0.08}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

// Catalog filter
document.querySelectorAll('.cat-btn').forEach(btn=>{{
  btn.addEventListener('click',()=>{{
    document.querySelectorAll('.cat-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    const cat=btn.dataset.cat;
    document.querySelectorAll('.supp-card').forEach(card=>{{
      card.classList.toggle('hidden',cat!=='all'&&card.dataset.cat!==cat);
    }});
  }});
}});
</script>
</body>
</html>"""

components.html(HTML, height=7000, scrolling=True)
