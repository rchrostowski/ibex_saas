"""
IBEX — Sports Dietitian Admin Dashboard  (pages/02_Admin.py)
No st.set_page_config() here — lives in root app.py only.
Password-protected. Requires ADMIN_PASSWORD in Streamlit Secrets.
"""
import json
from datetime import datetime, timedelta
import pandas as pd
import streamlit as st

try:
    from supabase import create_client
except: create_client = None

# ── THEME (same as audit) ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Barlow:wght@300;400;600;700&family=Barlow+Condensed:wght@400;500;600;700;800&display=swap');
:root{--black:#0a0a0f;--navy:#0b1220;--navy2:#132033;--off:#f0ede6;--gold:#c9a84c;--gold2:#e8c97a;--muted:rgba(240,237,230,0.52);--border:rgba(201,168,76,0.18);--green:#4ade80;--blue:#7dd3fc;--red:#ef4444;}
#MainMenu,footer,header{visibility:hidden}
html,body,[class*="css"]{font-family:'Barlow',sans-serif!important;font-weight:300}
.stApp{background:var(--navy)!important}
.block-container{padding-top:1.2rem!important}
h1,h2,h3,h4,h5{color:var(--off)!important;font-family:'Bebas Neue',sans-serif!important;letter-spacing:.03em}
p,li,div,label{color:var(--muted)}
section[data-testid="stSidebar"]{background:var(--black)!important;border-right:1px solid var(--border)!important}
section[data-testid="stSidebar"] *{color:var(--off)!important}
section[data-testid="stSidebar"] input{background:var(--navy)!important;color:var(--off)!important;border:1px solid var(--border)!important;border-radius:6px!important}
section[data-testid="stSidebar"] [data-baseweb="select"]>div{background:var(--navy)!important;border:1px solid var(--border)!important;border-radius:6px!important}
section[data-testid="stSidebar"] [data-baseweb="select"] *{color:var(--off)!important}
div[data-baseweb="menu"]{background:var(--navy2)!important;border:1px solid var(--border)!important;border-radius:8px!important}
div[data-baseweb="menu"] *{color:var(--off)!important}
.stButton button{background:var(--gold)!important;color:var(--black)!important;border:none!important;border-radius:4px!important;font-family:'Barlow Condensed',sans-serif!important;font-weight:700!important;letter-spacing:.15em!important;text-transform:uppercase!important;padding:.6rem 1.2rem!important}
.stButton button:hover{background:var(--gold2)!important}
.stTextInput input{background:var(--navy)!important;color:var(--off)!important;border:1px solid var(--border)!important;border-radius:6px!important}
.stSelectbox [data-baseweb="select"]>div{background:var(--navy)!important;border:1px solid var(--border)!important;border-radius:6px!important}
.stSelectbox [data-baseweb="select"] *{color:var(--off)!important}
.stTextArea textarea{background:var(--navy)!important;color:var(--off)!important;border:1px solid var(--border)!important;border-radius:6px!important}
[data-testid="stFormSubmitButton"] button{background:var(--gold)!important;color:var(--black)!important;border:none!important;border-radius:4px!important;font-family:'Barlow Condensed',sans-serif!important;font-weight:700!important;letter-spacing:.15em!important;text-transform:uppercase!important;width:100%!important}
button[data-baseweb="tab"]{font-family:'Barlow Condensed',sans-serif!important;font-size:.75rem!important;letter-spacing:.15em!important;text-transform:uppercase!important;font-weight:600!important;color:var(--muted)!important;background:transparent!important;border-bottom:2px solid transparent!important}
button[data-baseweb="tab"][aria-selected="true"]{color:var(--gold)!important;border-bottom:2px solid var(--gold)!important}
[data-baseweb="tab-list"]{background:transparent!important;border-bottom:1px solid var(--border)!important}
.ibx-card{background:var(--black);border:1px solid var(--border);padding:20px;margin-bottom:12px}
.ibx-label{font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.35em;text-transform:uppercase;color:var(--gold)!important;margin-bottom:.3rem}
.ibx-title{font-family:'Bebas Neue',sans-serif;font-size:2rem;color:var(--off)!important;letter-spacing:.03em;line-height:1}
.ibx-divider{height:1px;background:var(--border);margin:12px 0}
.ibx-badge{display:inline-block;padding:3px 8px;border:1px solid var(--border);font-family:'Barlow Condensed',sans-serif;font-size:.58rem;letter-spacing:.15em;text-transform:uppercase;color:var(--gold)!important;margin-right:4px}
.ibx-badge.green{border-color:rgba(74,222,128,.35);color:var(--green)!important}
.ibx-badge.red{border-color:rgba(239,68,68,.35);color:var(--red)!important}
.ibx-badge.blue{border-color:rgba(125,211,252,.35);color:var(--blue)!important}
.stWarning{background:rgba(201,168,76,.08)!important;border-color:var(--gold)!important;border-radius:4px!important}
.stInfo{background:rgba(11,18,32,.8)!important;border-color:var(--border)!important;border-radius:4px!important}
.stSuccess{background:rgba(74,222,128,.08)!important;border-color:rgba(74,222,128,.3)!important;border-radius:4px!important}
.stError{background:rgba(239,68,68,.08)!important;border-color:rgba(239,68,68,.3)!important;border-radius:4px!important}
.metric-card{background:var(--black);border:1px solid var(--border);padding:1.2rem 1.5rem;text-align:center}
.metric-val{font-family:'Bebas Neue',sans-serif;font-size:3rem;color:var(--gold);line-height:1;margin-bottom:.2rem}
.metric-lbl{font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted)}
.status-pill{font-family:'Barlow Condensed',sans-serif;font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;padding:.2rem .5rem}
.status-pending{background:rgba(201,168,76,.12);color:var(--gold);border:1px solid rgba(201,168,76,.3)}
.status-approved{background:rgba(74,222,128,.1);color:var(--green);border:1px solid rgba(74,222,128,.25)}
.status-flagged{background:rgba(239,68,68,.1);color:var(--red);border:1px solid rgba(239,68,68,.25)}
.status-modified{background:rgba(125,211,252,.1);color:var(--blue);border:1px solid rgba(125,211,252,.25)}
</style>
""", unsafe_allow_html=True)

# ── PASSWORD GATE ──
def check_auth():
    if st.session_state.get("admin_auth"): return True
    pw = st.secrets.get("ADMIN_PASSWORD","ibex_admin_2025")
    st.markdown("""
    <div class="ibx-card" style="max-width:420px;margin:3rem auto;">
      <div class="ibx-label">Restricted Access</div>
      <div class="ibx-title" style="margin-bottom:1rem;">Admin Portal</div>
      <div class="ibx-divider"></div>
      <div style="font-size:.85rem;color:rgba(240,237,230,.5);margin-bottom:1rem;">Sports Dietitian & Athletic Department Staff Only</div>
    </div>
    """, unsafe_allow_html=True)
    with st.form("auth"):
        entered = st.text_input("Password", type="password", placeholder="Enter admin password")
        submitted = st.form_submit_button("Sign In")
        if submitted:
            if entered == pw:
                st.session_state.admin_auth = True
                st.rerun()
            else:
                st.error("Incorrect password.")
    return False

# ── SUPABASE ──
@st.cache_resource(show_spinner=False)
def get_supabase():
    url = st.secrets.get("SUPABASE_URL")
    key = st.secrets.get("SUPABASE_SERVICE_ROLE_KEY")
    if not url or not key or create_client is None: return None
    try: return create_client(url, key)
    except: return None

def load_all_audits():
    sb = get_supabase()
    if not sb:
        return pd.DataFrame()  # Return empty if no DB
    try:
        res = sb.table("recommendations").select("*").order("created_at", desc=True).execute()
        if not res.data: return pd.DataFrame()
        return pd.DataFrame(res.data)
    except Exception as e:
        st.warning(f"Could not load audits from database: {e}")
        return pd.DataFrame()

def update_status(audit_id, new_status, dietitian_notes=""):
    sb = get_supabase()
    if not sb: return False
    try:
        sb.table("recommendations").update({
            "status": new_status,
            "dietitian_notes": dietitian_notes,
            "reviewed_at": datetime.utcnow().isoformat()
        }).eq("audit_id", audit_id).execute()
        return True
    except: return False

# ── HELPERS ──
def safe_get(survey, key, default="—"):
    if not survey or not isinstance(survey, dict): return default
    return survey.get(key, default) or default

def parse_survey(row):
    s = row.get("survey")
    if isinstance(s, dict): return s
    if isinstance(s, str):
        try: return json.loads(s)
        except: return {}
    return {}

def parse_ai(row):
    a = row.get("ai_result")
    if isinstance(a, dict): return a
    if isinstance(a, str):
        try: return json.loads(a)
        except: return {}
    return {}

def status_badge(status):
    cls = {"pending":"status-pending","approved":"status-approved",
           "flagged":"status-flagged","modified":"status-modified"}.get(str(status).lower(),"status-pending")
    label = str(status).capitalize()
    return f'<span class="status-pill {cls}">{label}</span>'

def format_dt(dt_str):
    if not dt_str: return "—"
    try:
        dt = datetime.fromisoformat(str(dt_str).replace("Z",""))
        return dt.strftime("%b %d, %Y %H:%M")
    except: return str(dt_str)[:16]

# ── MOCK DATA (shown when no DB connected) ──
MOCK_AUDITS = pd.DataFrame([
    {"audit_id":"mock-001","athlete_name":"J. Williams","email":"jw@lehigh.edu","school":"Lehigh","sport":"Football","plan":"Performance","status":"approved","created_at":"2025-03-18T09:00:00",
     "survey":{"sport":"Football","position":"Linebacker","season_status":"In-season","training_days_per_week":6,"intensity_1_to_10":9,"goals":["strength","recovery"],"stress_1_to_10":7,"soreness_1_to_10":8},
     "ai_result":{"included_product_ids":["IBX-001","IBX-002","IBX-003","IBX-004"],"flags":[],"consult_professional":False,"notes_for_athlete":["Focus on post-practice recovery window"]}},
    {"audit_id":"mock-002","athlete_name":"M. Chen","email":"mc@lehigh.edu","school":"Lehigh","sport":"Swimming","plan":"Basic","status":"pending","created_at":"2025-03-17T14:30:00",
     "survey":{"sport":"Swimming","position":"Freestyle","season_status":"In-season","training_days_per_week":6,"intensity_1_to_10":8,"goals":["endurance","recovery"],"stress_1_to_10":6,"soreness_1_to_10":5},
     "ai_result":{"included_product_ids":["IBX-001","IBX-002","IBX-014","IBX-016"],"flags":[],"consult_professional":False,"notes_for_athlete":["Beetroot best taken 2-3 hours before morning practice"]}},
    {"audit_id":"mock-003","athlete_name":"T. Johnson","email":"tj@lehigh.edu","school":"Lehigh","sport":"Wrestling","plan":"Performance","status":"flagged","created_at":"2025-03-16T11:00:00",
     "survey":{"sport":"Wrestling","position":"165lb","season_status":"In-season","training_days_per_week":7,"intensity_1_to_10":10,"goals":["strength","recovery","sleep"],"stress_1_to_10":9,"soreness_1_to_10":9,"open_notes":"Taking a pre-workout with DMAA from a friend"},
     "ai_result":{"included_product_ids":["IBX-001","IBX-003","IBX-012"],"flags":["DMAA_mentioned"],"consult_professional":True,"notes_for_athlete":["DMAA is NCAA banned — do not use friend's pre-workout"]}},
    {"audit_id":"mock-004","athlete_name":"S. Park","email":"sp@lehigh.edu","school":"Lehigh","sport":"Soccer","plan":"Basic","status":"approved","created_at":"2025-03-16T08:00:00",
     "survey":{"sport":"Soccer","position":"Midfielder","season_status":"In-season","training_days_per_week":5,"intensity_1_to_10":7,"goals":["endurance","recovery"],"stress_1_to_10":5,"soreness_1_to_10":6},
     "ai_result":{"included_product_ids":["IBX-001","IBX-002","IBX-005","IBX-004"],"flags":[],"consult_professional":False,"notes_for_athlete":["Electrolytes critical during double sessions"]}},
    {"audit_id":"mock-005","athlete_name":"A. Rodriguez","email":"ar@lehigh.edu","school":"Lehigh","sport":"Track & Field","plan":"Performance","status":"pending","created_at":"2025-03-15T16:00:00",
     "survey":{"sport":"Track & Field","position":"400m","season_status":"Pre-season","training_days_per_week":6,"intensity_1_to_10":8,"goals":["endurance","strength","recovery"],"stress_1_to_10":6,"soreness_1_to_10":7},
     "ai_result":{"included_product_ids":["IBX-001","IBX-002","IBX-014","IBX-004","IBX-003"],"flags":[],"consult_professional":False,"notes_for_athlete":["Beta-alanine tingles are normal and harmless"]}},
])

# ════════════════════════════════════════════════════════
# MAIN APP
# ════════════════════════════════════════════════════════
if not check_auth():
    st.stop()

# Header
st.markdown("""
<div style="border-bottom:1px solid rgba(201,168,76,0.18);padding-bottom:1rem;margin-bottom:1.5rem;display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:10px;">
  <div>
    <div style="font-family:'Barlow Condensed',sans-serif;font-size:.6rem;letter-spacing:.35em;text-transform:uppercase;color:#c9a84c;">Sports Dietitian Portal</div>
    <div style="font-family:'Bebas Neue',sans-serif;font-size:2.5rem;color:#f0ede6;letter-spacing:.05em;line-height:1;">IBEX Admin</div>
  </div>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs(["Dashboard","Athlete Reviews","Flagged","Analytics","Settings"])

# Load data
raw_df = load_all_audits()
using_mock = raw_df.empty
if using_mock:
    df = MOCK_AUDITS.copy()
    st.info("No database connected — showing demo data. Connect Supabase to see real athlete audits.")
else:
    df = raw_df.copy()
    if "sport" not in df.columns:
        df["sport"] = df["survey"].apply(lambda s: safe_get(s if isinstance(s,dict) else {},  "sport", "—"))
    if "school" not in df.columns:
        df["school"] = df.get("school","—")

# ── TAB: DASHBOARD ──
with tabs[0]:
    total      = len(df)
    pending    = len(df[df["status"]=="pending"])
    approved   = len(df[df["status"]=="approved"])
    flagged    = len(df[df["status"]=="flagged"])

    c1,c2,c3,c4 = st.columns(4)
    for col, val, lbl in [(c1,total,"Total Audits"),(c2,pending,"Pending Review"),
                           (c3,approved,"Approved"),(c4,flagged,"Flagged")]:
        with col:
            st.markdown(f"""
            <div class="metric-card">
              <div class="metric-val">{val}</div>
              <div class="metric-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:.5rem;'></div>", unsafe_allow_html=True)

    if flagged > 0:
        st.error(f"⚠ {flagged} athlete(s) flagged for review — check the Flagged tab immediately.")

    # Recent audits table
    st.markdown('<div class="ibx-label" style="margin-top:1.5rem;">Recent Audits</div>', unsafe_allow_html=True)
    st.markdown('<div class="ibx-card" style="padding:0;">', unsafe_allow_html=True)

    display_cols = []
    for _, row in df.head(20).iterrows():
        s = parse_survey(row)
        a = parse_ai(row)
        display_cols.append({
            "Athlete":    row.get("athlete_name","—") or "—",
            "School":     row.get("school","—") or "—",
            "Sport":      row.get("sport") or safe_get(s,"sport","—"),
            "Position":   safe_get(s,"position","—"),
            "Plan":       row.get("plan","—") or "—",
            "Season":     safe_get(s,"season_status","—"),
            "Goals":      ", ".join(safe_get(s,"goals",[]) or []),
            "Stress":     f"{safe_get(s,'stress_1_to_10','—')}/10",
            "Soreness":   f"{safe_get(s,'soreness_1_to_10','—')}/10",
            "Flags":      ", ".join(a.get("flags",[]) or []) or "None",
            "Date":       format_dt(row.get("created_at","")),
            "Status":     row.get("status","pending"),
            "ID":         row.get("audit_id","")[:8]+"…",
        })

    if display_cols:
        tdf = pd.DataFrame(display_cols)
        st.dataframe(
            tdf,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Status": st.column_config.TextColumn("Status"),
                "Flags":  st.column_config.TextColumn("Flags"),
            }
        )
    else:
        st.write("No audits yet.")
    st.markdown('</div>', unsafe_allow_html=True)

# ── TAB: ATHLETE REVIEWS ──
with tabs[1]:
    st.markdown('<div class="ibx-label">Review Queue</div>', unsafe_allow_html=True)

    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        status_filter = st.selectbox("Filter by status",["All","pending","approved","flagged","modified"])
    with col_f2:
        sport_options = ["All"] + sorted(df["sport"].dropna().unique().tolist()) if "sport" in df.columns else ["All"]
        sport_filter = st.selectbox("Filter by sport", sport_options)
    with col_f3:
        search = st.text_input("Search athlete name")

    filtered = df.copy()
    if status_filter != "All": filtered = filtered[filtered["status"]==status_filter]
    if sport_filter != "All":
        filtered = filtered[filtered["sport"]==sport_filter] if "sport" in filtered.columns else filtered
    if search:
        filtered = filtered[filtered["athlete_name"].fillna("").str.contains(search,case=False)]

    st.markdown(f'<div style="font-size:.78rem;color:var(--muted);margin:.5rem 0;">{len(filtered)} athlete(s) shown</div>', unsafe_allow_html=True)

    for _, row in filtered.iterrows():
        s = parse_survey(row)
        a = parse_ai(row)
        name    = row.get("athlete_name","Unknown") or "Unknown"
        sport   = row.get("sport") or safe_get(s,"sport","—")
        pos     = safe_get(s,"position","—")
        plan    = row.get("plan","—") or "—"
        status  = row.get("status","pending")
        flags   = a.get("flags",[]) or []
        notes_ai= a.get("notes_for_athlete",[]) or []
        cp      = a.get("consult_professional",False)
        goals   = safe_get(s,"goals",[]) or []
        rid     = row.get("audit_id","")

        badge_color = "red" if status=="flagged" else ("green" if status=="approved" else "")

        with st.expander(f"{name} — {sport} ({pos}) · {plan} · {status.upper()}", expanded=(status=="flagged")):
            c1,c2 = st.columns([2,1])
            with c1:
                st.markdown(f"""
                <div class="ibx-card">
                  <div class="ibx-label">Athlete Profile</div>
                  <div style="display:grid;grid-template-columns:1fr 1fr;gap:.5rem 1.5rem;font-size:.84rem;margin-top:.5rem;">
                    <div><span style="color:rgba(240,237,230,.4);">School</span><br><span style="color:#f0ede6;">{row.get('school','—') or '—'}</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Email</span><br><span style="color:#f0ede6;">{row.get('email','—') or '—'}</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Season</span><br><span style="color:#f0ede6;">{safe_get(s,'season_status','—')}</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Training</span><br><span style="color:#f0ede6;">{safe_get(s,'training_days_per_week','—')} days/wk · Intensity {safe_get(s,'intensity_1_to_10','—')}/10</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Sleep</span><br><span style="color:#f0ede6;">{safe_get(s,'sleep_hours','—')}h · Quality {safe_get(s,'sleep_quality_1_to_10','—')}/10</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Stress / Soreness</span><br><span style="color:#f0ede6;">{safe_get(s,'stress_1_to_10','—')}/10 · {safe_get(s,'soreness_1_to_10','—')}/10</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Goals</span><br><span style="color:#f0ede6;">{', '.join(goals) or '—'}</span></div>
                    <div><span style="color:rgba(240,237,230,.4);">Sensitivities</span><br><span style="color:#f0ede6;">{'GI ' if safe_get(s,'gi_sensitive',False) else ''}{'Caffeine' if safe_get(s,'caffeine_sensitive',False) else 'None'}</span></div>
                  </div>
                  {f'<div class="ibx-divider"></div><div style="font-size:.8rem;color:rgba(240,237,230,.5);"><b style="color:#f0ede6;">Notes from athlete:</b> {safe_get(s,"open_notes","—")}</div>' if safe_get(s,"open_notes","") else ""}
                  {f'<div class="ibx-divider"></div><div style="font-size:.8rem;color:rgba(240,237,230,.5);"><b style="color:#f0ede6;">Current stack:</b> {safe_get(s,"current_supplements","—")}</div>' if safe_get(s,"current_supplements","") else ""}
                </div>""", unsafe_allow_html=True)

            with c2:
                # Flags and AI warnings
                if cp:
                    st.error("⚕ Consult professional recommended")
                if flags:
                    st.warning(f"🚩 Flags: {', '.join(flags)}")

                # AI recommended stack
                st.markdown(f"""
                <div class="ibx-card">
                  <div class="ibx-label">AI Recommendations</div>
                  <div style="font-size:.8rem;color:rgba(240,237,230,.55);margin-top:.4rem;">
                    {len(a.get('included_product_ids',[]))} items recommended
                  </div>
                  <div class="ibx-divider"></div>""", unsafe_allow_html=True)

                for item_id in (a.get("included_product_ids",[]) or []):
                    reason = (a.get("reasons",{}) or {}).get(item_id,"")
                    st.markdown(f'<div style="font-size:.8rem;padding:.3rem 0;border-bottom:1px solid rgba(201,168,76,.08);color:rgba(240,237,230,.8);">→ {item_id}<br><span style="font-size:.72rem;color:rgba(240,237,230,.4);">{reason}</span></div>', unsafe_allow_html=True)

                if notes_ai:
                    st.markdown('<div class="ibx-divider"></div>', unsafe_allow_html=True)
                    st.markdown('<div class="ibx-label">AI Notes</div>', unsafe_allow_html=True)
                    for n in notes_ai:
                        st.markdown(f'<div style="font-size:.78rem;color:rgba(240,237,230,.55);margin:.2rem 0;">• {n}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

            # Review actions
            st.markdown('<div class="ibx-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="ibx-label">Dietitian Action</div>', unsafe_allow_html=True)

            with st.form(f"review_{rid}"):
                new_status = st.selectbox("Set status",
                    ["pending","approved","flagged","modified"],
                    index=["pending","approved","flagged","modified"].index(status) if status in ["pending","approved","flagged","modified"] else 0)
                dietitian_notes = st.text_area("Dietitian notes (visible to athlete if approved)",
                    placeholder="e.g., Approved as is. Remind athlete to take creatine with their post-practice shake.")
                if st.form_submit_button("Save Review"):
                    if not using_mock:
                        if update_status(rid, new_status, dietitian_notes):
                            st.success(f"Status updated to {new_status}")
                            st.cache_data.clear()
                            st.rerun()
                        else:
                            st.error("Failed to update. Check Supabase connection.")
                    else:
                        st.success(f"[Demo mode] Would set status to: {new_status}")

# ── TAB: FLAGGED ──
with tabs[2]:
    flagged_df = df[df["status"]=="flagged"]
    if flagged_df.empty:
        st.success("No flagged athletes. All clear.")
    else:
        st.error(f"⚠ {len(flagged_df)} athlete(s) require immediate attention.")
        for _, row in flagged_df.iterrows():
            s = parse_survey(row)
            a = parse_ai(row)
            name  = row.get("athlete_name","Unknown") or "Unknown"
            sport = row.get("sport") or safe_get(s,"sport","—")
            flags = a.get("flags",[]) or []
            notes = safe_get(s,"open_notes","")
            current = safe_get(s,"current_supplements","")

            st.markdown(f"""
            <div class="ibx-card" style="border-color:rgba(239,68,68,0.4);">
              <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:8px;">
                <div>
                  <div style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;color:#f0ede6;">{name}</div>
                  <div style="font-family:'Barlow Condensed',sans-serif;font-size:.68rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(240,237,230,.4);">{sport} · {row.get('school','—')}</div>
                </div>
                <span class="ibx-badge red">FLAGGED</span>
              </div>
              <div class="ibx-divider"></div>
              <div style="font-size:.85rem;"><b style="color:#ef4444;">Flags detected:</b> <span style="color:rgba(240,237,230,.7);">{', '.join(flags) or 'Auto-flagged for consult_professional'}</span></div>
              {f'<div style="margin-top:.5rem;font-size:.83rem;"><b style="color:#f0ede6;">Athlete notes:</b> <span style="color:rgba(240,237,230,.6);">{notes}</span></div>' if notes else ""}
              {f'<div style="margin-top:.5rem;font-size:.83rem;"><b style="color:#f0ede6;">Current stack:</b> <span style="color:rgba(240,237,230,.6);">{current}</span></div>' if current else ""}
              <div style="margin-top:.8rem;font-size:.78rem;color:rgba(240,237,230,.4);">Audit ID: {row.get('audit_id','')}</div>
            </div>""", unsafe_allow_html=True)

            with st.form(f"flag_action_{row.get('audit_id','')}"):
                resolution = st.text_area("Resolution notes",
                    placeholder="e.g., Called athlete. Confirmed they stopped using banned pre-workout. Approved modified stack.")
                col_a, col_b = st.columns(2)
                with col_a:
                    resolve = st.form_submit_button("Mark Resolved → Approved")
                with col_b:
                    keep_flagged = st.form_submit_button("Keep Flagged + Add Note")

                if resolve:
                    if not using_mock:
                        update_status(row.get("audit_id",""), "approved", resolution)
                        st.success("Resolved and approved.")
                        st.cache_data.clear()
                        st.rerun()
                    else:
                        st.success("[Demo] Would mark as approved.")
                if keep_flagged:
                    if not using_mock:
                        update_status(row.get("audit_id",""), "flagged", resolution)
                        st.success("Notes saved.")
                    else:
                        st.success("[Demo] Notes saved.")

# ── TAB: ANALYTICS ──
with tabs[3]:
    st.markdown('<div class="ibx-label">Program Analytics</div>', unsafe_allow_html=True)

    # Sport breakdown
    if "sport" in df.columns:
        sport_counts = df["sport"].value_counts().reset_index()
        sport_counts.columns = ["Sport","Athletes"]
        c1,c2 = st.columns(2)
        with c1:
            st.markdown('<div class="ibx-card"><div class="ibx-label">Athletes by Sport</div>', unsafe_allow_html=True)
            st.dataframe(sport_counts, use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            plan_counts = df["plan"].value_counts().reset_index()
            plan_counts.columns = ["Plan","Count"]
            st.markdown('<div class="ibx-card"><div class="ibx-label">Plan Distribution</div>', unsafe_allow_html=True)
            st.dataframe(plan_counts, use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Status breakdown
    status_counts = df["status"].value_counts().reset_index()
    status_counts.columns = ["Status","Count"]
    st.markdown('<div class="ibx-card"><div class="ibx-label">Review Status Breakdown</div>', unsafe_allow_html=True)
    st.dataframe(status_counts, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Most common goals across all surveys
    all_goals = []
    for _, row in df.iterrows():
        s = parse_survey(row)
        goals = safe_get(s,"goals",[]) or []
        if isinstance(goals,list): all_goals.extend(goals)
    if all_goals:
        goal_df = pd.DataFrame({"Goal":all_goals}).value_counts().reset_index()
        goal_df.columns = ["Goal","Athletes"]
        st.markdown('<div class="ibx-card"><div class="ibx-label">Most Common Athlete Goals</div>', unsafe_allow_html=True)
        st.dataframe(goal_df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Export
    st.markdown('<div class="ibx-label" style="margin-top:1rem;">Export</div>', unsafe_allow_html=True)
    export_rows = []
    for _, row in df.iterrows():
        s = parse_survey(row)
        export_rows.append({
            "Audit ID":     row.get("audit_id",""),
            "Name":         row.get("athlete_name",""),
            "Email":        row.get("email",""),
            "School":       row.get("school",""),
            "Sport":        row.get("sport","") or safe_get(s,"sport",""),
            "Position":     safe_get(s,"position",""),
            "Plan":         row.get("plan",""),
            "Season":       safe_get(s,"season_status",""),
            "Status":       row.get("status",""),
            "Date":         format_dt(row.get("created_at","")),
            "Stress":       safe_get(s,"stress_1_to_10",""),
            "Soreness":     safe_get(s,"soreness_1_to_10",""),
            "Goals":        ", ".join(safe_get(s,"goals",[]) or []),
        })
    export_df = pd.DataFrame(export_rows)
    st.download_button(
        "Download All Audits (CSV)",
        data=export_df.to_csv(index=False),
        file_name=f"ibex_audits_{datetime.today().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ── TAB: SETTINGS ──
with tabs[4]:
    st.markdown('<div class="ibx-label">Configuration</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="ibx-card">
      <div class="ibx-label">Required Streamlit Secrets</div>
      <div style="font-size:.85rem;line-height:2;color:rgba(240,237,230,.65);">
        Add these in your Streamlit Cloud dashboard → App Settings → Secrets:
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.code("""
# Required
OPENAI_API_KEY = "sk-..."
OPENAI_MODEL   = "gpt-4.1-mini"

# Required for admin dashboard + data storage
SUPABASE_URL              = "https://your-project.supabase.co"
SUPABASE_SERVICE_ROLE_KEY = "eyJ..."

# Required for admin login
ADMIN_PASSWORD = "your_secure_password_here"

# Optional — Stripe checkout links
STRIPE_BASIC_LINK = "https://buy.stripe.com/..."
STRIPE_PERF_LINK  = "https://buy.stripe.com/..."

# Optional
SUPPORT_EMAIL          = "support@ibexsupplements.com"
EVIDENCE_LINKS_ENABLED = "true"
""", language="toml")

    st.markdown("""
    <div class="ibx-card" style="margin-top:1rem;">
      <div class="ibx-label">Required Supabase Table</div>
      <div style="font-size:.84rem;color:rgba(240,237,230,.6);margin-bottom:.8rem;">
        Run this SQL in your Supabase dashboard → SQL Editor to create the recommendations table:
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.code("""
CREATE TABLE recommendations (
  id              uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  audit_id        text UNIQUE NOT NULL,
  email           text,
  athlete_name    text,
  school          text,
  sport           text,
  plan            text,
  survey          jsonb,
  ai_result       jsonb,
  status          text DEFAULT 'pending',
  dietitian_notes text,
  reviewed_at     timestamptz,
  created_at      timestamptz DEFAULT now()
);

-- Enable Row Level Security
ALTER TABLE recommendations ENABLE ROW LEVEL SECURITY;

-- Allow service role full access
CREATE POLICY "service_role_all" ON recommendations
  FOR ALL USING (true) WITH CHECK (true);
""", language="sql")

    st.markdown("""
    <div class="ibx-card">
      <div class="ibx-label">Connection Status</div>
    """, unsafe_allow_html=True)

    sb = get_supabase()
    if sb:
        st.success("✓ Supabase connected")
    else:
        st.error("✗ Supabase not connected — add SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY to secrets")

    if st.secrets.get("OPENAI_API_KEY"):
        st.success("✓ OpenAI connected")
    else:
        st.error("✗ OpenAI not connected — add OPENAI_API_KEY to secrets")

    st.markdown('</div>', unsafe_allow_html=True)

    # Logout
    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
    if st.button("Sign Out"):
        st.session_state.admin_auth = False
        st.rerun()
