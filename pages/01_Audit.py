"""
IBEX — Athlete Audit  (pages/01_Audit.py)
No st.set_page_config() here — lives in root app.py only.
"""
import os, json, uuid
from datetime import date
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

try:
    from PIL import Image
except: Image = None
try:
    from openai import OpenAI
except: OpenAI = None
try:
    from supabase import create_client
except: create_client = None

# ── CONFIG ──
APP_TITLE      = "IBEX"
APP_TAGLINE    = "Personalized performance systems for D1 athletes"
PRODUCTS_CSV   = "data/products.csv"
EXCLUSIONS_CSV = "data/exclusions.csv"
LOGO_PATH      = "assets/ibex_logo.png"

# ── THEME ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;600;700&family=Barlow+Condensed:wght@400;500;600;700;800&display=swap');
:root{--black:#0a0a0f;--navy:#0b1220;--navy2:#132033;--off:#f0ede6;--gold:#c9a84c;--gold2:#e8c97a;--muted:rgba(240,237,230,0.52);--border:rgba(201,168,76,0.18);--green:#4ade80;--blue:#7dd3fc;}
#MainMenu,footer,header{visibility:hidden}
html,body,[class*="css"]{font-family:'Barlow',sans-serif!important;font-weight:300}
.stApp{background:var(--navy)!important}
.block-container{padding-top:1.2rem!important}
h1,h2,h3,h4,h5{color:var(--off)!important;font-family:'Bebas Neue',sans-serif!important;letter-spacing:.03em}
p,li,span,div,label{color:var(--muted)}
section[data-testid="stSidebar"]{background:var(--black)!important;border-right:1px solid var(--border)!important}
section[data-testid="stSidebar"] *{color:var(--off)!important}
section[data-testid="stSidebar"] .stMarkdown p{color:var(--muted)!important}
section[data-testid="stSidebar"] a{color:var(--gold)!important}
section[data-testid="stSidebar"] input,section[data-testid="stSidebar"] textarea{background:var(--navy)!important;color:var(--off)!important;border:1px solid var(--border)!important;border-radius:6px!important}
section[data-testid="stSidebar"] [data-baseweb="select"]>div{background:var(--navy)!important;border:1px solid var(--border)!important;border-radius:6px!important}
section[data-testid="stSidebar"] [data-baseweb="select"] *{color:var(--off)!important}
section[data-testid="stSidebar"] [data-baseweb="select"] svg{color:var(--gold)!important}
div[data-baseweb="popover"]{background:transparent!important}
div[data-baseweb="menu"]{background:var(--navy2)!important;border:1px solid var(--border)!important;border-radius:8px!important}
div[data-baseweb="menu"] *{color:var(--off)!important}
div[data-baseweb="menu"] [role="option"]:hover{background:rgba(201,168,76,.1)!important}
section[data-testid="stSidebar"] .stRadio label{color:var(--off)!important}
section[data-testid="stSidebar"] .stCheckbox label{color:var(--off)!important}
section[data-testid="stSidebar"] [data-testid="stNumberInput"] input{background:var(--navy)!important;border:1px solid var(--border)!important;color:var(--off)!important}
section[data-testid="stSidebar"] [data-testid="stNumberInput"] button{background:var(--navy2)!important;border-color:var(--border)!important;color:var(--gold)!important}
section[data-testid="stSidebar"] [data-baseweb="tag"]{background:rgba(201,168,76,.15)!important;border-color:var(--gold)!important}
section[data-testid="stSidebar"] [data-baseweb="tag"] span{color:var(--gold)!important}
.stButton button{background:var(--gold)!important;color:var(--black)!important;border:none!important;border-radius:4px!important;font-family:'Barlow Condensed',sans-serif!important;font-weight:700!important;letter-spacing:.15em!important;text-transform:uppercase!important;padding:.7rem 1.4rem!important}
.stButton button:hover{background:var(--gold2)!important}
.stLinkButton a{background:var(--navy2)!important;color:var(--gold)!important;border:1px solid var(--border)!important;border-radius:4px!important;font-family:'Barlow Condensed',sans-serif!important;font-weight:700!important;letter-spacing:.15em!important;text-transform:uppercase!important}
[data-testid="stFormSubmitButton"] button{background:var(--gold)!important;color:var(--black)!important;border:none!important;border-radius:4px!important;font-family:'Barlow Condensed',sans-serif!important;font-weight:700!important;letter-spacing:.15em!important;text-transform:uppercase!important;width:100%!important;padding:.8rem 1.6rem!important}
button[data-baseweb="tab"]{font-family:'Barlow Condensed',sans-serif!important;font-size:.78rem!important;letter-spacing:.15em!important;text-transform:uppercase!important;font-weight:600!important;color:var(--muted)!important;background:transparent!important;border-bottom:2px solid transparent!important}
button[data-baseweb="tab"][aria-selected="true"]{color:var(--gold)!important;border-bottom:2px solid var(--gold)!important}
[data-baseweb="tab-list"]{background:transparent!important;border-bottom:1px solid var(--border)!important}
[data-baseweb="tab-panel"]{background:transparent!important}
.ibx-card{background:var(--black);border:1px solid var(--border);padding:22px;margin-bottom:14px;transition:border-color .3s}
.ibx-card:hover{border-color:rgba(201,168,76,.35)}
.ibx-badge{display:inline-block;padding:3px 9px;border:1px solid var(--border);font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold)!important;margin-right:5px;margin-bottom:3px}
.ibx-badge.green{border-color:rgba(74,222,128,.35);color:var(--green)!important}
.ibx-badge.blue{border-color:rgba(125,211,252,.35);color:var(--blue)!important}
.ibx-divider{height:1px;background:var(--border);margin:12px 0}
.ibx-label{font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.35em;text-transform:uppercase;color:var(--gold)!important;margin-bottom:.3rem}
.ibx-title{font-family:'Bebas Neue',sans-serif;font-size:2rem;color:var(--off)!important;letter-spacing:.03em;line-height:1}
.stWarning{background:rgba(201,168,76,.08)!important;border-color:var(--gold)!important;border-radius:4px!important}
.stInfo{background:rgba(11,18,32,.8)!important;border-color:var(--border)!important;border-radius:4px!important}
.stSuccess{background:rgba(74,222,128,.08)!important;border-color:rgba(74,222,128,.3)!important;border-radius:4px!important}
.stError{background:rgba(239,68,68,.08)!important;border-color:rgba(239,68,68,.3)!important;border-radius:4px!important}
[data-testid="stChatMessage"]{background:var(--black)!important;border:1px solid var(--border)!important;border-radius:4px!important;margin-bottom:8px!important}
[data-testid="stChatMessage"] *{color:var(--off)!important}
[data-testid="stChatInputContainer"]{background:var(--black)!important;border:1px solid var(--border)!important;border-radius:4px!important}
[data-testid="stChatInputContainer"] *{color:var(--off)!important}
[data-testid="stChatInputContainer"] textarea{background:transparent!important}
.ibx-faq details{background:var(--black);border:1px solid var(--border);border-radius:4px;padding:12px 14px;margin:6px 0;transition:border-color .3s}
.ibx-faq details[open]{border-color:rgba(201,168,76,.4)}
.ibx-faq summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;gap:10px;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:14px;letter-spacing:.03em;color:var(--off)!important;outline:none}
.ibx-faq summary::-webkit-details-marker{display:none}
.ibx-faq .answer{margin-top:10px;color:var(--muted)!important;line-height:1.65;font-size:13px}
.ibx-faq .chev{width:28px;height:28px;border-radius:4px;display:flex;align-items:center;justify-content:center;background:rgba(201,168,76,.08);border:1px solid var(--border);flex-shrink:0;color:var(--gold)!important}
.ibx-faq .pill{display:inline-block;padding:3px 7px;border-radius:2px;background:rgba(201,168,76,.08);border:1px solid var(--border);color:var(--gold)!important;font-size:10px;font-weight:700;font-family:'Barlow Condensed',sans-serif;letter-spacing:.1em;text-transform:uppercase;margin-right:5px}
.main .block-container{background:var(--navy)!important}
section[data-testid="stSidebar"] .stCaption p{color:var(--muted)!important;font-size:.73rem!important}
section[data-testid="stSidebar"] hr{border-color:var(--border)!important}
</style>
""", unsafe_allow_html=True)

# ── HELPERS ──
def require_file(path, friendly):
    if not os.path.exists(path):
        st.error(f"Missing {friendly}: `{path}`")
        st.stop()

def load_logo():
    if not os.path.exists(LOGO_PATH) or Image is None: return None
    try: return Image.open(LOGO_PATH)
    except: return None

def get_openai_client():
    key = st.secrets.get("OPENAI_API_KEY")
    if not key: st.error("Missing OPENAI_API_KEY in Streamlit Secrets."); st.stop()
    if OpenAI is None: st.error("openai package not installed."); st.stop()
    return OpenAI(api_key=key)

def is_yes(val): return str(val).strip().lower() in {"y","yes","true","1"}

def parse_money(val):
    try:
        s=str(val).strip().replace("$","").replace(",","")
        x=float(s); return 0.0 if x!=x else x
    except: return 0.0

def norm_key(val):
    return " ".join(str(val or "").strip().lower().split())

def get_evidence_link(row):
    ev=str(row.get("Evidence_Link","") or "").strip()
    return ev if ev else str(row.get("Link","") or "").strip()

def evidence_enabled():
    return str(st.secrets.get("EVIDENCE_LINKS_ENABLED","true")).strip().lower() in {"1","true","yes","y"}

# ── PLAN CONFIG ──
PLAN_COPY = {
    "Basic": {
        "headline": "Foundations, done right.",
        "sub": "Clean, conservative, evidence-based. The essentials that actually move the needle.",
        "bullets": ["Core performance stack only","NSF Certified for Sport preferred","Simple, consistent, safe"],
        "note": "Best for: athletes who want a solid, no-BS baseline.",
    },
    "Performance": {
        "headline": "Optimization mode.",
        "sub": "Expanded catalog, deeper personalization, seasonal adjustments.",
        "bullets": ["Advanced recovery, sleep, gut, joint support","In-season vs off-season adjustments","Every marginal gain, zero sketchy ingredients"],
        "note": "Best for: high-volume training or athletes chasing every edge.",
    },
}

BASIC_CORE_CATEGORIES = {
    "Creatine","Omega-3","Magnesium","Vitamin D","Electrolytes","Protein",
    "Multivitamin","Zinc","Vitamin C","Probiotic","Fiber","Collagen","Tart Cherry"
}

PLAN_LIMITS = {
    "Basic":       {"max_units":5,"max_am":3,"max_pm":2,"max_training":2},
    "Performance": {"max_units":8,"max_am":3,"max_pm":3,"max_training":2},
}

def item_units(cost): return 2 if float(cost or 0) >= 20.0 else 1

# ── SUPABASE ──
@st.cache_resource(show_spinner=False)
def get_supabase():
    url=st.secrets.get("SUPABASE_URL"); key=st.secrets.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key: return None
    if create_client is None: return None
    try: return create_client(url, key)
    except: return None

def save_to_supabase(rid, intake, ai_out):
    sb = get_supabase()
    if not sb: return None
    payload = {
        "audit_id":rid,
        "email":(intake.get("email") or "").strip() or None,
        "athlete_name":(intake.get("name") or "").strip() or None,
        "school":(intake.get("school") or "").strip() or None,
        "sport":(intake.get("sport") or "").strip() or None,
        "plan":intake.get("plan"),
        "survey":intake,
        "ai_result":ai_out,
        "status":"pending",
    }
    try:
        res = sb.table("recommendations").insert(payload).execute()
        return res.data[0]["id"] if res.data else None
    except Exception as e:
        st.sidebar.warning(f"DB save failed: {e}")
        return None

# ── DATA LOADERS ──
@st.cache_data(show_spinner=False)
def load_products():
    df = pd.read_csv(PRODUCTS_CSV)
    df.columns = [c.strip() for c in df.columns]
    for col in ["Evidence_Link","NCAA_Risk_Tier","Athlete_Safe_OK"]:
        if col not in df.columns: df[col] = ""
    return df

@st.cache_data(show_spinner=False)
def load_exclusions():
    df = pd.read_csv(EXCLUSIONS_CSV)
    df.columns = [c.strip() for c in df.columns]
    return df

# ── FILTERS ──
def filter_products_by_plan(products, plan):
    p = products.copy()
    p["_cat"] = p["Category"].astype(str).str.strip()
    return p[p["_cat"].isin(BASIC_CORE_CATEGORIES)] if plan=="Basic" else p

def filter_ncaa_safe(products, plan):
    p = products.copy()
    if "Athlete_Safe_OK" in p.columns:
        p = p[p["Athlete_Safe_OK"].astype(str).str.strip().str.upper().isin({"Y","YES","TRUE","1"})]
    if "NCAA_Risk_Tier" in p.columns:
        tier = p["NCAA_Risk_Tier"].astype(str).str.strip().str.lower()
        p = p[tier.isin({"green","yellow"} if plan=="Performance" else {"green"}) | tier.eq("")]
    return p

def shortlist_products(products, goals, gi_sensitive, caffeine_sensitive, plan):
    p = filter_ncaa_safe(products, plan)
    p = filter_products_by_plan(p, plan)
    if goals:
        mask = False
        for g in goals:
            mask = mask | p["Typical_Use"].astype(str).str.contains(g, case=False, na=False)
        if mask is not False: p = p[mask]
    if gi_sensitive:
        p = p[~p["Avoid_If"].astype(str).str.contains("GI", case=False, na=False)]
    if caffeine_sensitive:
        p = p[~p["Avoid_If"].astype(str).str.contains("caffeine", case=False, na=False)]
    if len(p) < 10:
        p = filter_products_by_plan(filter_ncaa_safe(products, plan), plan)
    return p.head(60)

# ── AI ──
def run_ai(intake, shortlist, exclusions, plan):
    client = get_openai_client()
    approved = shortlist[["Product_ID","Category","Ingredient","Brand","Link","Evidence_Link",
                           "Serving_Form","Typical_Use","Timing","Avoid_If",
                           "Third_Party_Tested","NSF_Certified","Notes","Est_Monthly_Cost"]].to_dict(orient="records")

    schema = {"flags":["string"],"consult_professional":"boolean",
              "included_product_ids":["IBX-001"],"excluded_product_ids":["IBX-002"],
              "schedule":{"AM":["IBX-001"],"PM":["IBX-001"],"Training":["IBX-001"]},
              "reasons":{"IBX-001":"short non-medical reason"},
              "notes_for_athlete":["bullet"]}

    plan_rules = ("Plan: BASIC. Conservative. Prefer NSF/third-party tested. Keep simple."
                  if plan=="Basic" else
                  "Plan: PERFORMANCE. Expanded. Add conditional advanced items if clearly supported.")
    lim = PLAN_LIMITS[plan]

    system = (
        "You are IBEX, a supplement protocol assistant for D1 athletes. "
        "NOT a medical provider. Do NOT diagnose or treat. "
        "Only select from approved_products. Never recommend exclusions list items. "
        "Do NOT invent citations. If Evidence_Link missing, do not pretend it exists. "
        "If serious symptoms or medications mentioned, set consult_professional=true. "
        f"{plan_rules} "
        f"MAX {lim['max_units']} units (Est_Monthly_Cost≥$20 = 2 units). "
        f"AM≤{lim['max_am']}, PM≤{lim['max_pm']}, Training≤{lim['max_training']}. "
        "No duplicate ingredients. One product per ingredient. "
        "Return ONLY valid JSON matching output_format."
    )

    payload = {"plan":plan,"intake":intake,"approved_products":approved,
               "exclusions":exclusions.to_dict(orient="records"),"output_format":schema}

    model = st.secrets.get("OPENAI_MODEL","gpt-4.1-mini")
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role":"system","content":system},{"role":"user","content":json.dumps(payload)}],
        temperature=0.2
    )
    content = resp.choices[0].message.content.strip()
    try: return json.loads(content)
    except:
        s,e = content.find("{"),content.rfind("}")
        if s!=-1 and e!=-1 and e>s: return json.loads(content[s:e+1])
        raise

# ── ENFORCE CAPS ──
def enforce_caps(ai_out, plan, products_df):
    lim = PLAN_LIMITS[plan]
    included = ai_out.get("included_product_ids",[]) or []
    schedule = ai_out.get("schedule",{}) or {}
    reasons  = ai_out.get("reasons",{}) or {}
    notes    = ai_out.get("notes_for_athlete",[]) or []
    if not included: return ai_out

    prod_map = products_df.set_index("Product_ID").to_dict(orient="index")
    order    = {pid:i for i,pid in enumerate(included)}

    rows = []
    for pid in included:
        p   = prod_map.get(pid,{})
        cat = str(p.get("Category","") or "").strip()
        ing = str(p.get("Ingredient","") or "").strip()
        est = parse_money(p.get("Est_Monthly_Cost",0))
        rows.append({"pid":pid,"cat":cat,"ing":ing,"est":est,
                     "nsf":is_yes(p.get("NSF_Certified","")),
                     "core":cat in BASIC_CORE_CATEGORIES,
                     "order":order.get(pid,9999),
                     "dup":norm_key(ing) or f"cat::{norm_key(cat)}"})

    rows.sort(key=lambda r:(not r["core"],not r["nsf"],r["order"]))

    kept,seen,dropped=[],[],[]
    for r in rows:
        if r["dup"] in seen: dropped.append(r); continue
        kept.append(r); seen.append(r["dup"])

    if dropped:
        msg="Removed duplicate supplement forms to keep your stack clean."
        if msg not in notes: notes=[msg]+notes

    picked,units=[],0
    for r in kept:
        u=item_units(r["est"])
        if units+u>lim["max_units"]: continue
        picked.append(r["pid"]); units+=u

    picked_set=set(picked)
    def trim(items,maxn):
        out=[]
        for pid in (items or []):
            if pid in picked_set and pid not in out: out.append(pid)
            if len(out)>=maxn: break
        return out

    ai_out["included_product_ids"] = picked
    ai_out["schedule"] = {"AM":trim(schedule.get("AM",[]),lim["max_am"]),
                          "PM":trim(schedule.get("PM",[]),lim["max_pm"]),
                          "Training":trim(schedule.get("Training",[]),lim["max_training"])}
    ai_out["reasons"]          = {pid:reasons.get(pid,"") for pid in picked if pid in reasons}
    ai_out["notes_for_athlete"] = notes
    return ai_out

# ── UI: AUDIT ID ──
def display_audit_id(rid):
    if not rid: return
    display_id = "IBEX-" + rid.replace("-","")[:10].upper()
    html = f"""
    <div style="background:#0a0a0f;border:1px solid rgba(201,168,76,0.35);padding:18px 20px 14px;margin:4px 0 16px;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;">
        <div>
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.35em;text-transform:uppercase;color:#c9a84c;">IBEX AUDIT ID</div>
          <div style="margin-top:5px;font-size:1.4rem;font-weight:900;color:#f0ede6;font-family:ui-monospace,monospace;">{display_id}</div>
          <div style="margin-top:6px;font-size:.78rem;color:rgba(240,237,230,0.45);">Paste this into Stripe at checkout to match your order.</div>
        </div>
        <div>
          <button id="copyBtn" style="background:#c9a84c;color:#0a0a0f;border:none;padding:8px 14px;font-family:'Barlow Condensed',sans-serif;font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;cursor:pointer;">Copy ID</button>
          <div id="copyNote" style="font-size:.7rem;color:rgba(240,237,230,0.45);text-align:center;margin-top:4px;min-height:12px;"></div>
        </div>
      </div>
    </div>
    <script>
      document.getElementById("copyBtn").addEventListener("click",async()=>{{
        try{{await navigator.clipboard.writeText("{display_id}");
        document.getElementById("copyNote").textContent="Copied ✓";
        setTimeout(()=>document.getElementById("copyNote").textContent="",1400)}}
        catch(e){{document.getElementById("copyNote").textContent="Select & copy manually"}}
      }});
    </script>"""
    components.html(html, height=140)

# ── UI: HEADER ──
def render_header():
    logo = load_logo()
    st.markdown('<div style="border-bottom:1px solid rgba(201,168,76,0.18);padding-bottom:1rem;margin-bottom:1rem;">', unsafe_allow_html=True)
    if logo:
        c1,c2 = st.columns([1,9], gap="small")
        with c1: st.image(logo, width=70)
        with c2:
            st.markdown(f"""
            <div style="padding-top:2px;">
              <div style="font-family:'Bebas Neue',sans-serif;font-size:2.5rem;color:#f0ede6;letter-spacing:.05em;line-height:1;">{APP_TITLE}</div>
              <div style="font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:#c9a84c;margin-top:1px;">{APP_TAGLINE}</div>
              <div style="margin-top:8px;">
                <span class="ibx-badge green">NCAA ✓</span>
                <span class="ibx-badge blue">NSF Tested</span>
                <span class="ibx-badge">Evidence-Linked</span>
                <span class="ibx-badge">AI-Personalized</span>
              </div>
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:2.5rem;color:#f0ede6;letter-spacing:.05em;">{APP_TITLE}</div>
          <div style="font-family:'Barlow Condensed',sans-serif;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:#c9a84c;">{APP_TAGLINE}</div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── UI: PRODUCT CARDS ──
def render_products(product_ids, products_df, reasons):
    prod_map = products_df.set_index("Product_ID").to_dict(orient="index")
    cols = st.columns(3, gap="large")
    for i,pid in enumerate(product_ids):
        p = prod_map.get(pid)
        if not p: continue
        ev = get_evidence_link(p)
        nsf = '<span class="ibx-badge blue">NSF ✓</span>' if is_yes(p.get("NSF_Certified","")) else ""
        with cols[i%3]:
            st.markdown(f"""
            <div class="ibx-card">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:5px;">
                <span class="ibx-badge">{p.get('Category','')}</span>
                <span class="ibx-badge">{p.get('Timing','')}</span>
              </div>
              <div style="margin-top:8px;"><span class="ibx-badge green">NCAA ✓</span>{nsf}</div>
              <div style="margin-top:10px;font-family:'Bebas Neue',sans-serif;font-size:1.4rem;color:#f0ede6;letter-spacing:.03em;line-height:1.1;">{p.get('Ingredient','')}</div>
              <div style="font-size:.75rem;color:rgba(240,237,230,.4);margin-top:1px;">{p.get('Serving_Form','')}</div>
              <div class="ibx-divider"></div>
              <div style="font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:#c9a84c;">Why this</div>
              <div style="font-size:.83rem;color:rgba(240,237,230,.65);margin-top:3px;line-height:1.6;">{reasons.get(pid,'Personalized to your audit.')}</div>
            </div>""", unsafe_allow_html=True)
            if evidence_enabled():
                if ev: st.link_button("Open linked study →", ev)
                else: st.caption("No evidence link attached yet.")

# ── UI: SCHEDULE ──
def render_schedule(schedule, products_df):
    prod_map = products_df.set_index("Product_ID").to_dict(orient="index")
    blocks = [("AM","Morning","Foundation window"),("PM","Evening","Recovery window"),("Training","Training","Performance window")]
    cols = st.columns(3, gap="large")
    for i,(key,title,sub) in enumerate(blocks):
        with cols[i]:
            items = schedule.get(key,[]) if isinstance(schedule,dict) else []
            rows = ""
            if not items:
                rows = '<div style="color:rgba(240,237,230,.3);font-size:.83rem;">—</div>'
            else:
                for pid in items:
                    p=prod_map.get(pid,{})
                    rows += f'<div style="display:flex;justify-content:space-between;padding:.4rem 0;border-bottom:1px solid rgba(201,168,76,.08);font-size:.83rem;"><span style="color:rgba(240,237,230,.8);">{p.get("Ingredient",pid)}</span><span style="color:#c9a84c;font-size:.7rem;font-family:\'Barlow Condensed\',sans-serif;">{p.get("Serving_Form","")}</span></div>'
            st.markdown(f"""
            <div class="ibx-card">
              <div style="font-family:'Bebas Neue',sans-serif;font-size:1.5rem;color:#c9a84c;line-height:1;">{title}</div>
              <div style="font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:rgba(240,237,230,.3);margin-bottom:10px;">{sub}</div>
              {rows}
            </div>""", unsafe_allow_html=True)

# ── UI: PRIVACY ──
def render_privacy():
    support = st.secrets.get("SUPPORT_EMAIL","support@ibexsupplements.com")
    st.markdown(f"""
    <div class="ibx-card" style="max-width:820px;">
      <div class="ibx-label">Legal</div>
      <div class="ibx-title">Privacy Policy</div>
      <div style="font-size:.75rem;color:rgba(240,237,230,.3);margin-bottom:1.2rem;">Effective: {date.today().strftime('%B %d, %Y')}</div>
      <div class="ibx-divider"></div>
      <div style="font-size:.86rem;line-height:1.8;color:rgba(240,237,230,.6);">
        <p><b style="color:#f0ede6;">IBEX</b> is a supplement intelligence platform for D1 athletes. We collect your sport, training, recovery, and goal data to generate personalized recommendations.</p>
        <p style="margin-top:1rem;"><b style="color:#f0ede6;">What we collect:</b> Name, email (optional), school, sport, position, training inputs, and goals.</p>
        <p style="margin-top:.8rem;"><b style="color:#f0ede6;">What we don't do:</b> We do not sell your data. We do not make medical diagnoses. We do not recommend banned substances.</p>
        <p style="margin-top:.8rem;"><b style="color:#f0ede6;">AI processing:</b> Your inputs are sent to an AI provider to generate your protocol. The model is instructed never to invent citations or make medical claims.</p>
        <p style="margin-top:.8rem;"><b style="color:#f0ede6;">NCAA compliance:</b> All catalog ingredients are cross-referenced against the banned substance list. No system can guarantee compliance — always confirm with your athletic department.</p>
        <p style="margin-top:.8rem;"><b style="color:#f0ede6;">Data deletion:</b> Email <span style="color:#c9a84c;">{support}</span> with your Audit ID to request deletion.</p>
      </div>
    </div>""", unsafe_allow_html=True)

# ── UI: FAQ ──
def render_faq():
    support = st.secrets.get("SUPPORT_EMAIL","support@ibexsupplements.com")
    st.markdown(f"""
    <div class="ibx-card" style="max-width:820px;">
      <div class="ibx-label">Help</div>
      <div class="ibx-title" style="margin-bottom:1rem;">FAQ</div>
      <div class="ibx-divider"></div>
      <div class="ibx-faq">
        <details open><summary>What is IBEX?<div class="chev">⌄</div></summary><div class="answer">IBEX builds a personalized, NCAA-compliant supplement protocol for D1 athletes in 3 minutes. Your sports dietitian reviews and approves every recommendation before you see it.</div></details>
        <details><summary>Is IBEX medical advice?<div class="chev">⌄</div></summary><div class="answer">No. IBEX is not a medical provider and does not diagnose or treat conditions. Consult a qualified professional if you have symptoms, medications, or a medical condition.</div></details>
        <details><summary>Are these supplements NCAA compliant?<div class="chev">⌄</div></summary><div class="answer">Every ingredient is cross-referenced against the NCAA banned substance list. We only include NSF Certified for Sport or third-party tested products. Still — always confirm with your athletic department. <div style="margin-top:8px;"><span class="pill">Third-party tested only</span><span class="pill">No proprietary blends</span></div></div></details>
        <details><summary>How does the free audit work?<div class="chev">⌄</div></summary><div class="answer">Answer ~15 questions about your sport, position, training, sleep, stress, and goals. The AI builds your personalized stack in seconds from our curated catalog. Your Audit ID is generated and saved for checkout.</div></details>
        <details><summary>Can I adjust my stack seasonally?<div class="chev">⌄</div></summary><div class="answer">Yes. Re-run the audit anytime. Performance plan users get automatic in-season vs off-season adjustments built in.</div></details>
        <details><summary>How do I delete my data?<div class="chev">⌄</div></summary><div class="answer">Email <b style="color:#c9a84c;">{support}</b> with your IBEX Audit ID and request deletion.</div></details>
      </div>
    </div>""", unsafe_allow_html=True)

# ── CHAT ──
def build_context(intake, ai_out, products_df):
    prod_map = products_df.set_index("Product_ID").to_dict(orient="index")
    included = ai_out.get("included_product_ids",[]) or []
    reasons  = ai_out.get("reasons",{}) or {}
    items = []
    for pid in included:
        p=prod_map.get(pid,{})
        items.append({"Product_ID":pid,"Category":p.get("Category",""),"Ingredient":p.get("Ingredient",""),
                      "Timing":p.get("Timing",""),"Serving_Form":p.get("Serving_Form",""),
                      "Reason":reasons.get(pid,""),"Evidence_Link":get_evidence_link(p),"Notes":p.get("Notes","")})
    return {"intake":intake,"recommendations":items,"schedule":ai_out.get("schedule",{}),
            "notes_for_athlete":ai_out.get("notes_for_athlete",[]),"flags":ai_out.get("flags",[]),
            "consult_professional":bool(ai_out.get("consult_professional",False))}

def run_chat(messages, context):
    client = get_openai_client()
    model  = st.secrets.get("OPENAI_CHAT_MODEL",st.secrets.get("OPENAI_MODEL","gpt-4.1-mini"))
    system = ("You are IBEX Chat — an athlete-safe assistant. Not a medical provider. "
              "Do not diagnose or treat. Use only provided context. Never invent studies or citations. "
              "If a product has Evidence_Link you may reference it. Keep answers short and athlete-friendly.")
    full = [{"role":"system","content":system},{"role":"user","content":"CONTEXT:\n"+json.dumps(context)}]
    for m in messages:
        if m.get("role") in {"user","assistant"}:
            full.append({"role":m["role"],"content":m.get("content","")})
    resp = client.chat.completions.create(model=model,messages=full,temperature=0.2)
    return resp.choices[0].message.content.strip()

# ── APP START ──
require_file(PRODUCTS_CSV,   "products.csv")
require_file(EXCLUSIONS_CSV, "exclusions.csv")

products   = load_products()
exclusions = load_exclusions()

STRIPE_BASIC = st.secrets.get("STRIPE_BASIC_LINK","")
STRIPE_PERF  = st.secrets.get("STRIPE_PERF_LINK","")

for k,v in [("ai_out",None),("last_plan","Basic"),("last_rid",None),
             ("last_intake",None),("chat_messages",[])]:
    if k not in st.session_state: st.session_state[k]=v

render_header()
tabs = st.tabs(["Audit","Ask IBEX","Privacy","FAQ"])

# ── TAB: AUDIT ──
with tabs[0]:
    if st.session_state.ai_out:
        ao   = st.session_state.ai_out
        plan = st.session_state.last_plan

        st.markdown(f"""
        <div class="ibx-card" style="display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:10px;">
          <div>
            <div class="ibx-label">Your Results</div>
            <div class="ibx-title">Your {plan} System</div>
            <div style="font-size:.75rem;color:rgba(240,237,230,.3);margin-top:3px;">Ref: {st.session_state.last_rid}</div>
          </div>
          <div>
            <span class="ibx-badge green">NCAA ✓</span>
            <span class="ibx-badge">AI-Personalized</span>
            <span class="ibx-badge">Evidence-Linked</span>
          </div>
        </div>""", unsafe_allow_html=True)

        display_audit_id(st.session_state.last_rid)

        if ao.get("consult_professional"):
            st.warning("Based on what you shared, we recommend consulting a qualified professional. Stack kept conservative.")
        if ao.get("flags"):
            st.caption("Signals detected: " + ", ".join(ao["flags"]))

        st.markdown('<div class="ibx-label" style="margin-top:.8rem;">Recommended Stack</div>', unsafe_allow_html=True)
        render_products(ao.get("included_product_ids",[]), products, ao.get("reasons",{}))

        st.markdown('<div class="ibx-label" style="margin-top:.8rem;">Daily Schedule</div>', unsafe_allow_html=True)
        render_schedule(ao.get("schedule",{}), products)

        notes = ao.get("notes_for_athlete",[])
        if notes:
            st.markdown('<div class="ibx-label" style="margin-top:.8rem;">Notes</div>', unsafe_allow_html=True)
            st.markdown('<div class="ibx-card">', unsafe_allow_html=True)
            for n in notes: st.write(f"→ {n}")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="ibx-label" style="margin-top:1.5rem;">Checkout</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="ibx-card">
          <div style="font-size:.8rem;color:rgba(240,237,230,.45);margin-bottom:1rem;">Copy your Audit ID above and paste it into Stripe at checkout.</div>
          <div style="font-family:'Bebas Neue',sans-serif;font-size:1.6rem;color:#f0ede6;">
            {"IBEX Basic — $100/mo" if plan=="Basic" else "IBEX Performance — $130/mo"}
          </div>
          <div style="font-size:.78rem;color:rgba(240,237,230,.4);margin-bottom:.8rem;">
            {"Foundations, done right. Free shipping." if plan=="Basic" else "Optimization mode. Free priority shipping."}
          </div>
        </div>""", unsafe_allow_html=True)

        link = STRIPE_BASIC if plan=="Basic" else STRIPE_PERF
        if link: st.link_button(f"Subscribe — IBEX {plan} →", link)
        else: st.info("Stripe link coming soon. Contact us to subscribe.")

        st.markdown("<div style='height:.8rem;'></div>", unsafe_allow_html=True)
        if st.button("← Start a new audit"):
            for k in ["ai_out","last_rid","last_intake","chat_messages"]:
                st.session_state[k] = [] if k=="chat_messages" else None
            st.rerun()
    else:
        st.markdown("""
        <div class="ibx-card">
          <div class="ibx-label">Get Started</div>
          <div class="ibx-title">Performance Audit</div>
          <div style="font-size:.86rem;color:rgba(240,237,230,.5);margin-top:6px;line-height:1.7;">
            Fill out the audit in the sidebar. Your personalized, NCAA-compliant stack appears here instantly — with exact dosing and a daily schedule.
          </div>
        </div>""", unsafe_allow_html=True)

    # SIDEBAR
    with st.sidebar:
        st.markdown("""
        <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;color:#c9a84c;letter-spacing:.08em;margin-bottom:.2rem;">IBEX Audit</div>
        <div style="font-size:.68rem;color:rgba(240,237,230,.4);font-family:'Barlow Condensed',sans-serif;letter-spacing:.15em;text-transform:uppercase;margin-bottom:1rem;">Plan → Audit → Your Protocol</div>
        """, unsafe_allow_html=True)

        plan = st.radio("Plan", ["Basic","Performance"],
                        index=0 if st.session_state.last_plan=="Basic" else 1,
                        horizontal=True)
        pc = PLAN_COPY[plan]
        st.markdown(f"**{pc['headline']}**")
        st.write(pc["sub"])
        for b in pc["bullets"]: st.write(f"→ {b}")
        st.caption(pc["note"])
        st.markdown("---")

        with st.form("audit"):
            st.markdown("**About you**")
            name   = st.text_input("Full name")
            email  = st.text_input("Email")
            school = st.text_input("School / University")

            st.markdown("**Sport & training**")
            sport         = st.text_input("Sport")
            position      = st.text_input("Position / Event")
            season_status = st.selectbox("Season status",["In-season","Pre-season","Off-season"])
            training_days = st.slider("Training days/week",0,7,5)
            intensity     = st.slider("Training intensity (1–10)",1,10,7)
            travel        = st.selectbox("Travel frequency",["Never","Sometimes","Often"])

            st.markdown("**Goals**")
            goals = st.multiselect("Select all that apply",
                ["strength","endurance","recovery","sleep","gut","joints","focus","general health"])

            st.markdown("**Recovery & lifestyle**")
            sleep_hrs = st.number_input("Sleep hours/night",min_value=0.0,max_value=12.0,value=7.0,step=0.5)
            sleep_q   = st.slider("Sleep quality (1–10)",1,10,6)
            stress    = st.slider("Stress (1–10)",1,10,6)
            soreness  = st.slider("Soreness/Fatigue (1–10)",1,10,6)
            gi_sens   = st.checkbox("GI sensitive / stomach issues")
            caff_sens = st.checkbox("Caffeine sensitive")

            st.markdown("**Current stack / notes**")
            current = st.text_area("Supplements you already take (optional)",placeholder="Creatine, fish oil, whey…")
            avoid   = st.text_input("Ingredients to avoid (optional)",placeholder="e.g., soy, lactose")
            notes   = st.text_area("Other context (optional)",placeholder="Anything that would help tailor your protocol…")

            st.markdown("---")
            st.caption("Not medical advice. See the Privacy tab for details.")
            submitted = st.form_submit_button("Build My Protocol")

        if submitted:
            rid = str(uuid.uuid4())
            intake = {"rid":rid,"plan":plan,"name":name,"email":email,"school":school,
                      "sport":sport,"position":position,"season_status":season_status,
                      "training_days_per_week":training_days,"intensity_1_to_10":intensity,
                      "travel_frequency":travel,"goals":goals,"sleep_hours":sleep_hrs,
                      "sleep_quality_1_to_10":sleep_q,"stress_1_to_10":stress,
                      "soreness_1_to_10":soreness,"gi_sensitive":gi_sens,
                      "caffeine_sensitive":caff_sens,"current_supplements":current,
                      "avoid_ingredients":avoid,"open_notes":notes}

            shortlist = shortlist_products(products,goals,gi_sens,caff_sens,plan)
            with st.spinner("Building your protocol…"):
                ao = run_ai(intake,shortlist,exclusions,plan)
            ao = enforce_caps(ao,plan,products)
            save_to_supabase(rid,intake,ao)

            st.session_state.ai_out       = ao
            st.session_state.last_plan    = plan
            st.session_state.last_rid     = rid
            st.session_state.last_intake  = intake
            st.session_state.chat_messages = []
            st.rerun()

# ── TAB: ASK IBEX ──
with tabs[1]:
    st.markdown("""
    <div class="ibx-card">
      <div class="ibx-label">AI Chat</div>
      <div class="ibx-title">Ask IBEX</div>
      <div style="font-size:.83rem;color:rgba(240,237,230,.5);margin-top:5px;line-height:1.7;">
        Questions about your stack, timing, stacking, travel, or seasonal changes — grounded in your audit.
      </div>
    </div>""", unsafe_allow_html=True)

    if not st.session_state.ai_out:
        st.info("Run your audit first — your personalized chat will appear here.")
    else:
        for m in st.session_state.chat_messages:
            with st.chat_message(m["role"]): st.markdown(m["content"])
        prompt = st.chat_input('Ask a question — e.g. "Why creatine?" or "Can I take these together?"')
        if prompt:
            st.session_state.chat_messages.append({"role":"user","content":prompt})
            with st.chat_message("user"): st.markdown(prompt)
            ctx = build_context(st.session_state.last_intake,st.session_state.ai_out,products)
            with st.spinner("Thinking…"):
                answer = run_chat(st.session_state.chat_messages,ctx)
            st.session_state.chat_messages.append({"role":"assistant","content":answer})
            with st.chat_message("assistant"): st.markdown(answer)

# ── TAB: PRIVACY ──
with tabs[2]:
    render_privacy()

# ── TAB: FAQ ──
with tabs[3]:
    render_faq()
