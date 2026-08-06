import os, random, string
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CursedMedicineEG - ULTRA CLEAN 19 LANG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# === FIX 405 HEAD - ده كان سبب الـ 503 في n8n ===
@app.api_route("/", methods=["GET", "HEAD"], include_in_schema=False)
def home():
    return HTMLResponse(f"""
    <h1>CursedMedicineEG - ULTRA CLEAN READY ✅</h1>
    <p>Channel: <a href='https://www.youtube.com/@CursedMedicineEG'>@CursedMedicineEG</a></p>
    <p><a href='/health'>/health</a> | <a href='/api/ultra?disease=sugar'>/api/ultra</a></p>
    <p>has_groq: {bool(os.getenv('GROQ_API_KEY'))} | Countries: 19</p>
    """)

@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {
        "status": "ULTRA CLEAN READY - 19 PURE LANG",
        "channel": "https://www.youtube.com/@CursedMedicineEG",
        "countries": 19,
        "has_groq": bool(os.getenv("GROQ_API_KEY"))
    }

# اي HEAD من Render / UptimeRobot يرجع 200
@app.api_route("/{full_path:path}", methods=["HEAD"])
def head_fix(full_path: str):
    return HTMLResponse("", status_code=200)

# === CHANNEL CONFIG ===
CHANNEL_URL = "https://www.youtube.com/@CursedMedicineEG"
CHANNEL_NAME = "CursedMedicineEG"

TOPICS = {
    "sugar": {"ar": "السكري والتغذية", "en": "Sugar & Nutrition"},
    "colon": {"ar": "القولون والهضم", "en": "Colon & Digestion"},
    "pressure": {"ar": "ضغط الدم", "en": "Blood Pressure"},
    "heart": {"ar": "صحة القلب", "en": "Heart Health"},
    "liver": {"ar": "صحة الكبد", "en": "Liver Health"},
    "kidney": {"ar": "صحة الكلى", "en": "Kidney Health"},
    "bones": {"ar": "صحة العظام", "en": "Bone Health"},
    "cancer": {"ar": "التوعية الصحية", "en": "Health Awareness"},
}

FORBIDDEN_LIST = ["الخبز الابيض", "السكر المكرر", "الزيوت المهدرجة", "الدقيق الابيض", "المشروبات الغازية"]

FLAGS = ["EG","SA","US","FR","DE","SE","IT","NL","NO","AU","GB","CA","BR","TR","AE","QA","KW","MA","DZ"]

def make_links():
    base = "https://cyber-caliph-elite.onrender.com/go/"
    return [base + ''.join(random.choices(string.ascii_lowercase+string.digits, k=4)) for _ in range(6)]

@app.api_route("/api/ultra", methods=["GET", "HEAD"])
def api_ultra(disease: str = "sugar"):
    topic = TOPICS.get(disease, TOPICS["sugar"])
    forbid = random.choice(FORBIDDEN_LIST)
    
    # عناوين آمنة لليوتيوب - قوية بدون ادعاء شفاء
    titles = {
        "title_ar": f"الحقيقة المظلمة عن {forbid} و {topic['ar']} | ماذا يقول نظام الطيبات؟ | {CHANNEL_NAME}",
        "title_en": f"The Cursed Truth About {forbid} & {topic['en']} | Tayyibat System Explained | {CHANNEL_NAME}",
        "title_fr": f"La vérité maudite sur {forbid} et {topic['en']} | Système Tayyibat | {CHANNEL_NAME}",
        "title_de": f"Die verfluchte Wahrheit über {forbid} & {topic['en']} | Tayyibat System | {CHANNEL_NAME}",
        "title_es": f"La verdad maldita sobre {forbid} y {topic['en']} | Sistema Tayyibat",
        "title_it": f"La verità maledetta su {forbid} e {topic['en']} | Sistema Tayyibat",
    }

    # برومبت فيديو تعليمي - مش علاجي
    video_prompt = f"Dark medical documentary style, cinematic 8k, exploring traditional foods like barley and {topic['en']}, educational, mysterious, {CHANNEL_NAME} style"

    return JSONResponse({
        **titles,
        "disease": disease,
        "forbidden_topic": forbid,
        "video_prompt_vault": video_prompt,
        "description_links_6_short": make_links(),
        "channel": CHANNEL_URL,
        "channel_handle": "@CursedMedicineEG",
        "youtube_title": titles["title_ar"],
        "youtube_description": f"""{titles['title_ar']}

{titles['title_en']}

🔗 قناة الطب الملعون:
{CHANNEL_URL}

⚠️ تنبيه: المحتوى تثقيفي فقط ولا يغني عن استشارة الطبيب.

#الطب_الملعون #نظام_الطيبات #CursedMedicineEG
{topic['ar']} | {topic['en']}
""",
        "countries": 19,
        "status": "ULTRA CLEAN READY - @CursedMedicineEG",
        "has_groq": bool(os.getenv("GROQ_API_KEY"))
    })

@app.api_route("/api/daily-2-videos", methods=["GET", "HEAD"])
def daily_2():
    import json
    d1 = random.choice(list(TOPICS.keys()))
    d2 = random.choice(list(TOPICS.keys()))
    v1 = api_ultra(d1)
    v2 = api_ultra(d2)
    return JSONResponse({
        "video_1": json.loads(v1.body),
        "video_2": json.loads(v2.body),
        "channel": CHANNEL_URL
    })

@app.api_route("/go/{code}", methods=["GET", "HEAD"])
def go_redirect(code: str):
    return RedirectResponse(CHANNEL_URL, status_code=302)
