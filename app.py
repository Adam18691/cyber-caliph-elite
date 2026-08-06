import os, random, string
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cyber Caliph - ULTRA CLEAN 19 LANG PURE")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- FIX 405 HEAD - ده اللي كان مبوظ الدنيا ---
@app.api_route("/", methods=["GET", "HEAD"], include_in_schema=False)
def home():
    return HTMLResponse("""
    <h1 style='font-family:monospace'>ULTRA CLEAN READY - 19 PURE LANG ✅</h1>
    <p><a href='/health'>/health</a> | <a href='/api/ultra?disease=sugar'>/api/ultra?disease=sugar</a> | <a href='/api/daily-2-videos'>/api/daily-2-videos</a></p>
    <p>Countries: 19 | has_groq: {}</p>
    """.format(bool(os.getenv("GROQ_API_KEY"))))

@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {
        "status": "ULTRA CLEAN READY - 19 PURE LANG",
        "countries": 19,
        "has_groq": bool(os.getenv("GROQ_API_KEY")),
        "system": "ULTRA CLEAN - 19 LANG PURE"
    }

# ده بيحل اي HEAD من UptimeRobot / Render
@app.api_route("/{full_path:path}", methods=["HEAD"])
def head_catch_all(full_path: str):
    return HTMLResponse("", status_code=200)

# --- DATA VAULT - 19 LANG PURE ---
DISEASES = {
    "sugar": {"ar": "السكري", "en": "Diabetes", "cure": "الشعير والتلبينة"},
    "colon": {"ar": "القولون", "en": "Colon", "cure": "اللبن الرائب"},
    "pressure": {"ar": "الضغط", "en": "Blood Pressure", "cure": "الحجامة وزيت الزيتون"},
    "heart": {"ar": "القلب", "en": "Heart", "cure": "زبدة البقر وترك الزيوت"},
    "kidney": {"ar": "الكلى", "en": "Kidney", "cure": "الماء وترك السكر"},
    "liver": {"ar": "الكبد", "en": "Liver", "cure": "الكوارع والدهن الحيواني"},
    "bones": {"ar": "العظام", "en": "Bones", "cure": "الجبن القريش والبيض البلدي"},
    "cancer": {"ar": "السرطان", "en": "Cancer", "cure": "الصيام ونظام الطيبات"},
}

FORBIDDEN = ["البسكويت", "الخبز", "السكر الابيض", "الزيوت النباتية", "الدقيق الابيض"]
FLAGS = {"EG":"🇪🇬","SA":"🇸🇦","US":"🇺🇸","FR":"🇫🇷","DE":"🇩🇪","SE":"🇸🇪","IT":"🇮🇹","NL":"🇳🇱","NO":"🇳🇴","AU":"🇦🇺","GB":"🇬🇧","CA":"🇨🇦","BR":"🇧🇷","TR":"🇹🇷","AE":"🇦🇪","QA":"🇶🇦","KW":"🇰🇼","MA":"🇲🇦","DZ":"🇩🇿"}

def make_titles(disease_key):
    d = DISEASES.get(disease_key, DISEASES["sugar"])
    forbid = random.choice(FORBIDDEN)
    titles = {
        "title_ar": f"⚠️ {forbid} سم قاتل يدمر {d['ar']} | {d['cure']} يرمم في 7 ايام | 2026 | الانسولين سبوبة نهائيا",
        "title_en": f"💀 FORBIDDEN {forbid} DESTROYS {d['en']} | Barley CURES in 7 Days | Tayyibat System 10000000000% | Insulin is a business",
        "title_fr": f"💀 INTERDIT {forbid} DETRUIT {d['en']} | Barley GUERIT en 7 Jours | Tayyibat",
        "title_de": f"💀 VERBOTEN {forbid} ZERSTORT {d['en']} | Barley HEILT in 7 Tagen | Tayyibat",
        "title_sv": f"💀 FORBJUDET {forbid} FORSTOR {d['en']} | Barley BOTAR pa 7 Dagar | Tayyibat",
        "title_it": f"💀 VIETATO {forbid} DISTRUGGE {d['en']} | Barley CURA in 7 Giorni | Tayyibat",
        "title_nl": f"💀 VERBODEN {forbid} VERNIETIGT {d['en']} | Barley GENEEST in 7 Dagen | Tayyibat",
        "title_no": f"💀 FORBUDT {forbid} ODELEGGER {d['en']} | Barley HELBREDER pa 7 Dager | Tayyibat",
    }
    return titles, d, forbid

def make_links():
    base = "https://cyber-caliph-elite.onrender.com/go/"
    codes = [''.join(random.choices(string.ascii_lowercase + string.digits, k=4)) for _ in range(6)]
    return [base + c for c in codes]

# --- API CORE ---
@app.api_route("/api/ultra", methods=["GET", "HEAD"])
def api_ultra(disease: str = "sugar"):
    titles, d, forbid = make_titles(disease)
    
    video_prompt = f"Cinematic 8K Barley honey drip repairing {d['en']} vs {forbid} poison, Dr Diaa style, Tayyibat System, ultra clean food healing, no sugar no flour"
    
    links = make_links()
    countries_data = []
    for code, flag in FLAGS.items():
        countries_data.append({"code": code, "flag": flag, "title": titles["title_en"][:60]})

    result = {
        **titles,
        "disease": disease,
        "forbidden": forbid,
        "cure": d["cure"],
        "video_prompt_vault": video_prompt,
        "description_links_6_short": links,
        "video_links_3_short": links[:3],
        "countries": 19,
        "countries_19": countries_data,
        "all_translations": {"ar": d["ar"], "en": d["en"]},
        "system": "ULTRA CLEAN - 19 LANG PURE",
        "has_groq": bool(os.getenv("GROQ_API_KEY")),
        "total_countries": 19,
        "status": "ULTRA CLEAN READY - 19 PURE LANG"
    }
    return JSONResponse(result)

@app.api_route("/api/daily-2-videos", methods=["GET", "HEAD"])
def daily_2():
    v1 = api_ultra(random.choice(list(DISEASES.keys()))).body
    v2 = api_ultra(random.choice(list(DISEASES.keys()))).body
    import json
    return JSONResponse({"video_1": json.loads(v1), "video_2": json.loads(v2), "peak_hours": "11AM AU + 8PM EG"})

@app.api_route("/go/{code}", methods=["GET", "HEAD"])
def go_redirect(code: str):
    # Cloaking - هنا تحط رابطك الاصلي
    return RedirectResponse("https://www.youtube.com/@Waeldeban186", status_code=302)

# --- END ---
