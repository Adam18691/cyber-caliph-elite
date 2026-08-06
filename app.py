from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import random, os, hashlib, json, time
from datetime import datetime

# SAFE IMPORTS - عشان السيرفر ميقعش
try:
    import requests
    HAS_REQUESTS = True
except:
    HAS_REQUESTS = False
    requests = None

try:
    from gtts import gTTS
    HAS_GTTS = True
except:
    HAS_GTTS = False

try:
    from PIL import Image, ImageDraw
    HAS_PIL = True
except:
    HAS_PIL = False

app = FastAPI(title="SULAIMANI VAULT ELITE 10B - FINAL")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

# ====== الروابط الأصلية ======
AFF_RAW = {
    "monoprice": "https://yazing.com/deals/monoprice/Waeldeban186",
    "landsend": "https://yazing.com/deals/landsend/Waeldeban186",
    "simon": "https://yazing.com/deals/shopsimon/Waeldeban186",
    "colehaan": "https://yazing.com/deals/colehaan/Waeldeban186",
    "hf": "https://yazing.com/deals/hfonline-uk/Waeldeban186",
    "kie": "https://kie.ai?ref=0e3195dd062b11f0da7496dd3c1bf66",
    "hp": "https://yazing.com/deals/hp-ca/Waeldeban186",
    "life": "https://yazing.com/deals/lifeextension/Waeldeban186",
}

# ====== صيغ العناوين اللي بتضرب CTR - متظبطة ======
CTR_TEMPLATES = [
    "🚨 {forb} سم قاتل يدمر {disease_ar} | {allow} يرمم في 7 ايام | {year}",
    "💀 ممنوع {forb} بعد اليوم - {allow} هو الحل | نظام الطيبات {percent}%",
    "⚠️ {secret} | {forb} يدمر {disease_ar} و {allow} يعالجه نهائيا",
    "🔥 {allow} مجمة لفؤاد المريض | وداعا {forb} و وداعا {disease_ar}",
    "💊 علاج {disease_ar} ليس دواء | اترك {forb} وكل {allow} | سنة نبوية {year}",
]

VIDEO_STYLES_VAULT = [
    "Cinematic 8K {allow} honey drip repairing {disease_en} cells vs {forb} poison destroying, Islamic golden light, Quran healing, ultra detailed",
    "Macro timelapse {allow} talbina porridge bubbling healing stomach lining vs {forb} mold rotting colon, Sunnah medicine light",
    "Luxury slow motion {allow} olive oil pouring healing {disease_en} organ vs {forb} seed oil burning, medical miracle golden hour",
    "Microscopic {allow} molecules repairing DNA vs {forb} molecules killing, Tayyibat system Dr Diaa style 32K",
]

COUNTRIES = {
    "سويسرا": {"code": "CH", "lang": "German", "gtts": "de", "flag": "🇨🇭", "peak": "20:00"},
    "السويد": {"code": "SE", "lang": "Swedish", "gtts": "sv", "flag": "🇸🇪", "peak": "20:00"},
    "فرنسا": {"code": "FR", "lang": "French", "gtts": "fr", "flag": "🇫🇷", "peak": "20:00"},
    "ألمانيا": {"code": "DE", "lang": "German", "gtts": "de", "flag": "🇩🇪", "peak": "20:00"},
    "بريطانيا": {"code": "UK", "lang": "English", "gtts": "en", "flag": "🇬🇧", "peak": "21:00"},
    "النرويج": {"code": "NO", "lang": "Norwegian", "gtts": "no", "flag": "🇳🇴", "peak": "20:00"},
    "أمريكا": {"code": "USA", "lang": "English", "gtts": "en", "flag": "🇺🇸", "peak": "02:00"},
    "بلجيكا": {"code": "BE", "lang": "French", "gtts": "fr", "flag": "🇧🇪", "peak": "20:00"},
    "أيرلندا": {"code": "IE", "lang": "English", "gtts": "en", "flag": "🇮🇪", "peak": "21:00"},
    "إيطاليا": {"code": "IT", "lang": "Italian", "gtts": "it", "flag": "🇮🇹", "peak": "21:00"},
    "هولندا": {"code": "NL", "lang": "Dutch", "gtts": "nl", "flag": "🇳🇱", "peak": "20:00"},
    "أستراليا": {"code": "AU", "lang": "English", "gtts": "en", "flag": "🇦🇺", "peak": "11:00"},
    "زيمبابوي": {"code": "ZW", "lang": "English", "gtts": "en", "flag": "🇿🇼", "peak": "20:00"},
    "فوكلاند": {"code": "FK", "lang": "English", "gtts": "en", "flag": "🇫🇰", "peak": "21:00"},
    "سانت هيلينا": {"code": "SH", "lang": "English", "gtts": "en", "flag": "🇸🇭", "peak": "21:00"},
    "جنوب السودان": {"code": "SS", "lang": "English", "gtts": "en", "flag": "🇸🇸", "peak": "20:00"},
    "ساموا": {"code": "WS", "lang": "English", "gtts": "en", "flag": "🇼🇸", "peak": "11:00"},
    "كندا": {"code": "CA", "lang": "English", "gtts": "en", "flag": "🇨🇦", "peak": "02:00"},
    "مصر": {"code": "EG", "lang": "Arabic", "gtts": "ar", "flag": "🇪🇬", "peak": "20:00"},
}

DISEASES = {
    "colon": {"ar": "القولون", "en": "Colon", "forbidden": ["العيش البلدي", "البقوليات", "العدس"], "allowed": ["الارز", "التلبينة", "العسل"], "secret": "القولون بيت الداء"},
    "sugar": {"ar": "السكري", "en": "Diabetes", "forbidden": ["العيش", "السكر", "البسكويت"], "allowed": ["الارز", "الشعير", "العسل"], "secret": "الانسولين سبوبة"},
    "pressure": {"ar": "الضغط", "en": "Blood Pressure", "forbidden": ["الملح", "العيش"], "allowed": ["التلبينة", "الموز"], "secret": "أدوية الضغط للابد"},
    "heart": {"ar": "القلب", "en": "Heart", "forbidden": ["الزيوت المهدرجة", "السمن النباتي"], "allowed": ["زيت الزيتون", "التلبينة"], "secret": "القسطرة بيزنس"},
    "kidney": {"ar": "الكلى", "en": "Kidney", "forbidden": ["الملح", "البروتين الزائد"], "allowed": ["الشعير", "العسل"], "secret": "الشعير يغسل الكلى"},
    "liver": {"ar": "الكبد", "en": "Liver", "forbidden": ["السكر", "الدقيق"], "allowed": ["زيت الزيتون", "التلبينة"], "secret": "لا يوجد دواء للكبد الدهني"},
    "bones": {"ar": "العظام", "en": "Bones", "forbidden": ["المياه الغازية", "العيش"], "allowed": ["التلبينة", "الارز"], "secret": "حقن العظام وهم كبير"},
    "cancer": {"ar": "المناعة", "en": "Immunity", "forbidden": ["السكر", "الزيوت المهدرجة"], "allowed": ["التلبينة", "العسل"], "secret": "الكيماوي تريليونات"},
}

SHORT_CACHE = {}
LAST_UPDATE = datetime.now().isoformat()

def vault_shorten(url: str):
    if url in SHORT_CACHE:
        return SHORT_CACHE[url]
    if HAS_REQUESTS:
        try:
            r = requests.get(f"https://is.gd/create.php?format=json&url={url}", timeout=4)
            data = r.json()
            short = data.get("shorturl")
            if short and "is.gd" in short:
                SHORT_CACHE[url] = short
                return short
        except:
            pass
    hid = hashlib.md5(url.encode()).hexdigest()[:6]
    cloaked = f"https://cyber-caliph-elite.onrender.com/go/{hid}"
    SHORT_CACHE[url] = cloaked
    SHORT_CACHE[hid] = url
    return cloaked

def vault_translate_groq(text_ar: str):
    """ترجمة احترافية - لو مفيش مفتاح بترجع نفس النص"""
    if not HAS_REQUESTS:
        return {"ar": text_ar, "en": text_ar, "fr": text_ar, "de": text_ar, "sv": text_ar, "it": text_ar, "nl": text_ar, "no": text_ar, "eg": text_ar}
    try:
        key = os.getenv("GROQ_API_KEY")
        if not key:
            return {"ar": text_ar, "en": text_ar, "fr": text_ar, "de": text_ar, "sv": text_ar, "it": text_ar, "nl": text_ar, "no": text_ar, "eg": text_ar}

        prompt = f"""Translate this Arabic title to 7 languages. Return ONLY valid JSON, no explanation.
        Original: "{text_ar}"
        JSON format: {{"ar": "original arabic", "en": "english translation", "fr": "french", "de": "german", "sv": "swedish", "it": "italian", "nl": "dutch", "no": "norwegian"}}"""

        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={"model": "llama3-8b-8192", "messages": [{"role": "user", "content": prompt}], "temperature": 0.7},
            timeout=15
        )
        content = r.json()["choices"][0]["message"]["content"]
        content = content.replace("```json", "").replace("```", "").strip()
        data = json.loads(content)
        data["eg"] = data.get("ar", text_ar)
        return data
    except Exception as e:
        print(f"Translate error: {e}")
        return {"ar": text_ar, "en": text_ar, "fr": text_ar, "de": text_ar, "sv": text_ar, "it": text_ar, "nl": text_ar, "no": text_ar, "eg": text_ar}

@app.get("/go/{hid}")
def go_redirect(hid: str):
    long_url = SHORT_CACHE.get(hid)
    if not long_url:
        long_url = list(AFF_RAW.values())[0]
    return RedirectResponse(url=long_url, status_code=302)

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        with open("templates/index.html", encoding="utf-8") as f:
            return f.read()
    except:
        return "<h1>VAULT ELITE 10B FINAL READY - SULAIMANI</h1><a href='/api/ultra?disease=colon'>/api/ultra</a>"

@app.get("/api/ultra")
def ultra(disease: str = "colon"):
    global LAST_UPDATE
    LAST_UPDATE = datetime.now().isoformat()

    dis = DISEASES.get(disease, DISEASES["colon"])
    forb = random.choice(dis["forbidden"])
    allow = random.choice(dis["allowed"])
    template = random.choice(CTR_TEMPLATES)

    title_raw = template.format(
        forb=forb, allow=allow,
        disease_ar=dis["ar"], disease_en=dis["en"],
        secret=dis["secret"],
        year=datetime.now().year,
        percent=random.choice([100, 1000, 10000000000])
    )

    trans = vault_translate_groq(title_raw)

    selected = random.sample(list(AFF_RAW.items()), 6)
    long_links = [v for k,v in selected]
    short_links = [vault_shorten(v) for v in long_links]
    v_short = short_links[:3]

    style = random.choice(VIDEO_STYLES_VAULT)
    video_prompt = style.format(forb=forb, allow=allow, disease_en=dis["en"]) + f" seed {random.randint(1000,9999)}"

    desc = f"""{title_raw}

EN: {trans.get('en','')}
FR: {trans.get('fr','')}

🎬 3 LINKS VIDEO:
00:00 {forb} يدمر - {v_short[0]}
01:30 {allow} يرمم - {v_short[1]}
03:00 الحل - {v_short[2]}

📝 6 LINKS ELITE CLOAKED:
{chr(10).join([f'🔗 {s}' for s in short_links])}

SECRET: {dis['secret']}
PROMPT: {video_prompt[:100]}
#نظام_الطيبات #دكتور_ضياء_العوضي #Waeldeban186
"""

    countries_data = {}
    for name, info in COUNTRIES.items():
        gtts_code = info["gtts"]
        lang_key = gtts_code
        if lang_key == "no": lang_key = "no"
        title_for_country = trans.get(lang_key, trans.get("en", title_raw))
        if info["gtts"] == "ar": title_for_country = trans.get("ar", title_raw)
        if info["gtts"] == "en": title_for_country = trans.get("en", title_raw)

        countries_data[name] = {
            "flag": info["flag"],
            "code": info["code"],
            "lang": info["lang"],
            "peak": info["peak"],
            "title": title_for_country,
            "title_ar": trans.get("ar", title_raw)
        }

    return {
        "title_ar": trans.get("ar"),
        "title_en": trans.get("en"),
        "title_fr": trans.get("fr"),
        "title_de": trans.get("de"),
        "title_sv": trans.get("sv"),
        "title_it": trans.get("it"),
        "title_nl": trans.get("nl"),
        "title_no": trans.get("no"),
        "all_translations": trans,
        "description": desc,
        "video_links_3_short": v_short,
        "description_links_6_short": short_links,
        "description_links_6_long": long_links,
        "video_prompt_vault": video_prompt,
        "video_file_direct": f"https://cyber-caliph-elite.onrender.com/api/generate-video?prompt={video_prompt[:60]}",
        "countries_19": countries_data,
        "ctr_template_used": template,
        "vault_features": ["CLOAKING /go/", "CTR FORMULA FIXED", "VIDEO ROTATION", "19 TRANSLATION", "SHORT CACHE"],
        "total_countries": 19,
        "last_update": LAST_UPDATE,
        "has_groq": bool(os.getenv("GROQ_API_KEY")),
        "system": "SULAIMANI VAULT ELITE 10B FINAL - FIXED"
    }

@app.get("/api/daily-2-videos")
def daily_2():
    d1, d2 = random.sample(list(DISEASES.keys()), 2)
    return {
        "video_1_morning": {"publish": "11:00 AM EG - AU + WS", "disease": d1, "data": ultra(d1)},
        "video_2_evening": {"publish": "20:00 PM EG - EG + EU", "disease": d2, "data": ultra(d2)},
        "peak": {"11:00": ["AU","WS"], "20:00": ["EG","CH","SE","FR","DE","NO","BE","IT","NL"], "21:00": ["UK","IE","FK","SH"], "02:00": ["USA","CA"]},
        "vault_note": "FINAL FIXED - عناوين مختلفة + ترجمة 19 دولة"
    }

@app.get("/api/generate-video")
def gen_video(prompt: str = "talbina healing"):
    if not HAS_REQUESTS: return {"error": "requests missing"}
    try:
        kie = os.getenv("KIE_API_KEY")
        if not kie: return {"error": "KIE_API_KEY missing", "prompt": prompt}
        r = requests.post("https://api.kie.ai/api/v1/jobs/createTask",
            headers={"Authorization": f"Bearer {kie}"},
            json={"model": "kling-v2-1", "input": {"prompt": prompt, "duration": 5}}, timeout=15)
        tid = r.json().get("data", {}).get("taskId")
        if tid:
            for _ in range(20):
                time.sleep(5)
                c = requests.get(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}", headers={"Authorization": f"Bearer {kie}"}).json()
                if c.get("data", {}).get("state") == "success":
                    return {"video_file": c["data"]["resultJson"]["resultUrls"][0]}
        return {"error": "timeout", "taskId": tid}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health():
    return {"status": "VAULT FINAL FIXED READY", "has_requests": HAS_REQUESTS, "has_gtts": HAS_GTTS, "has_pil": HAS_PIL, "has_groq": bool(os.getenv("GROQ_API_KEY")), "countries": 19, "last": LAST_UPDATE}
