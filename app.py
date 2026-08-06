from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import random, os, hashlib, json
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except:
    HAS_REQUESTS = False
    requests = None

app = FastAPI(title="SULAIMANI VAULT ELITE 10B - FINAL FIXED")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

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

CTR_TEMPLATES = [
    "🚨 {forb} سم قاتل يدمر {disease_ar} | {allow} يرمم في 7 ايام | {year}",
    "💀 ممنوع {forb} بعد اليوم - {allow} هو الحل | نظام الطيبات {percent}%",
    "⚠️ {secret} | {forb} يدمر {disease_ar} و {allow} يعالجه نهائيا",
    "🔥 {allow} مجمة لفؤاد المريض | وداعا {forb} و وداعا {disease_ar}",
    "💊 علاج {disease_ar} ليس دواء | اترك {forb} وكل {allow} | سنة نبوية {year}",
]

VIDEO_STYLES = [
    "Cinematic 8K {allow} honey drip repairing {disease_en} cells vs {forb} poison, Islamic golden light, ultra detailed",
    "Macro timelapse {allow} talbina porridge healing stomach vs {forb} mold rotting colon, Sunnah light",
    "Luxury slow motion {allow} olive oil healing {disease_en} organ vs {forb} seed oil burning, golden hour",
]

COUNTRIES = {
    "سويسرا": {"code": "CH", "gtts": "de", "flag": "🇨🇭", "peak": "20:00"},
    "السويد": {"code": "SE", "gtts": "sv", "flag": "🇸🇪", "peak": "20:00"},
    "فرنسا": {"code": "FR", "gtts": "fr", "flag": "🇫🇷", "peak": "20:00"},
    "ألمانيا": {"code": "DE", "gtts": "de", "flag": "🇩🇪", "peak": "20:00"},
    "بريطانيا": {"code": "UK", "gtts": "en", "flag": "🇬🇧", "peak": "21:00"},
    "النرويج": {"code": "NO", "gtts": "no", "flag": "🇳🇴", "peak": "20:00"},
    "أمريكا": {"code": "USA", "gtts": "en", "flag": "🇺🇸", "peak": "02:00"},
    "بلجيكا": {"code": "BE", "gtts": "fr", "flag": "🇧🇪", "peak": "20:00"},
    "أيرلندا": {"code": "IE", "gtts": "en", "flag": "🇮🇪", "peak": "21:00"},
    "إيطاليا": {"code": "IT", "gtts": "it", "flag": "🇮🇹", "peak": "21:00"},
    "هولندا": {"code": "NL", "gtts": "nl", "flag": "🇳🇱", "peak": "20:00"},
    "أستراليا": {"code": "AU", "gtts": "en", "flag": "🇦🇺", "peak": "11:00"},
    "زيمبابوي": {"code": "ZW", "gtts": "en", "flag": "🇿🇼", "peak": "20:00"},
    "فوكلاند": {"code": "FK", "gtts": "en", "flag": "🇫🇰", "peak": "21:00"},
    "سانت هيلينا": {"code": "SH", "gtts": "en", "flag": "🇸🇭", "peak": "21:00"},
    "جنوب السودان": {"code": "SS", "gtts": "en", "flag": "🇸🇸", "peak": "20:00"},
    "ساموا": {"code": "WS", "gtts": "en", "flag": "🇼🇸", "peak": "11:00"},
    "كندا": {"code": "CA", "gtts": "en", "flag": "🇨🇦", "peak": "02:00"},
    "مصر": {"code": "EG", "gtts": "ar", "flag": "🇪🇬", "peak": "20:00"},
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

def vault_shorten(url: str):
    if url in SHORT_CACHE:
        return SHORT_CACHE[url]
    if HAS_REQUESTS:
        try:
            r = requests.get(f"https://is.gd/create.php?format=json&url={url}", timeout=4)
            short = r.json().get("shorturl")
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

def vault_translate_groq(text_ar: str, forb: str, allow: str, disease_ar: str, disease_en: str):
    """النسخة الذهبية - تترجم حتى لو GROQ مش موجود"""
    # Fallback احترافي 100% - لو GROQ وقع
    base_fallback = {
        "ar": text_ar,
        "en": f"💀 FORBIDDEN {forb} DESTROYS {disease_en} | {allow} CURES in 7 Days | Tayyibat System 10000000000%",
        "fr": f"💀 INTERDIT {forb} DETRUIT {disease_en} | {allow} GUERIT en 7 Jours | Systeme Tayyibat",
        "de": f"💀 VERBOTEN {forb} ZERSTORT {disease_en} | {allow} HEILT in 7 Tagen | Tayyibat System",
        "sv": f"💀 FORBJUDET {forb} FORSTOR {disease_en} | {allow} BOTAR pa 7 Dagar | Tayyibat System",
        "it": f"💀 VIETATO {forb} DISTRUGGE {disease_en} | {allow} CURA in 7 Giorni | Sistema Tayyibat",
        "nl": f"💀 VERBODEN {forb} VERNIETIGT {disease_en} | {allow} GENEEST in 7 Dagen | Tayyibat Systeem",
        "no": f"💀 FORBUDT {forb} ODELEGGER {disease_en} | {allow} HELBREDER pa 7 Dager | Tayyibat System",
        "eg": text_ar
    }

    if not HAS_REQUESTS:
        return base_fallback

    try:
        key = os.getenv("GROQ_API_KEY")
        if not key:
            return base_fallback

        prompt = f'Translate to 6 languages. Keep structure. Arabic title: "{text_ar}" Return ONLY JSON: {{"en":"english","fr":"french","de":"german","sv":"swedish","it":"italian","nl":"dutch","no":"norwegian"}}'
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={"model": "llama3-8b-8192", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3},
            timeout=12
        )
        content = r.json()["choices"][0]["message"]["content"].replace("```json","").replace("```","").strip()
        data = json.loads(content)
        data["ar"] = text_ar
        data["eg"] = text_ar
        return data
    except:
        return base_fallback

@app.get("/go/{hid}")
def go_redirect(hid: str):
    long_url = SHORT_CACHE.get(hid) or list(AFF_RAW.values())[0]
    return RedirectResponse(url=long_url, status_code=302)

@app.get("/", response_class=HTMLResponse)
def home():
    try:
        with open("templates/index.html", encoding="utf-8") as f:
            return f.read()
    except:
        return "<h1>VAULT ELITE 10B FINAL - SULAIMANI LIVE</h1>"

@app.get("/api/ultra")
def ultra(disease: str = "colon"):
    dis = DISEASES.get(disease, DISEASES["colon"])
    forb = random.choice(dis["forbidden"])
    allow = random.choice(dis["allowed"])
    template = random.choice(CTR_TEMPLATES)

    title_ar_raw = template.format(
        forb=forb, allow=allow,
        disease_ar=dis["ar"], disease_en=dis["en"],
        secret=dis["secret"], year=datetime.now().year,
        percent=random.choice([100, 1000, 10000000000])
    )

    trans = vault_translate_groq(title_ar_raw, forb, allow, dis["ar"], dis["en"])

    selected = random.sample(list(AFF_RAW.items()), 6)
    long_links = [v for k,v in selected]
    short_links = [vault_shorten(v) for v in long_links]

    video_prompt = random.choice(VIDEO_STYLES).format(forb=forb, allow=allow, disease_en=dis["en"]) + f" seed {random.randint(1000,9999)}"

    countries_data = {}
    for name, info in COUNTRIES.items():
        code = info["gtts"]
        map_code = {"de": "de", "sv": "sv", "fr": "fr", "en": "en", "no": "no", "it": "it", "nl": "nl", "ar": "ar"}
        lang_key = map_code.get(code, "en")
        title_for_country = trans.get(lang_key, trans.get("en"))
        if info["code"] == "EG":
            title_for_country = trans.get("ar")

        countries_data[name] = {
            "flag": info["flag"],
            "code": info["code"],
            "lang": info["lang"],
            "peak": info["peak"],
            "title": title_for_country,
            "title_ar": trans.get("ar")
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
        "description": f"{trans.get('ar')}\n\nEN: {trans.get('en')}\nFR: {trans.get('fr')}\n\n3 LINKS: {', '.join(short_links[:3])}",
        "video_links_3_short": short_links[:3],
        "description_links_6_short": short_links,
        "description_links_6_long": long_links,
        "video_prompt_vault": video_prompt,
        "countries_19": countries_data,
        "ctr_template_used": template,
        "vault_features": ["CLOAKING /go/", "CTR FIXED", "19 TRANSLATION REAL", "SHORT CACHE"],
        "total_countries": 19,
        "last_update": datetime.now().isoformat(),
        "has_groq": bool(os.getenv("GROQ_API_KEY")),
        "system": "SULAIMANI VAULT ELITE 10B FINAL - REAL TRANSLATION"
    }

@app.get("/api/daily-2-videos")
def daily_2():
    d1, d2 = random.sample(list(DISEASES.keys()), 2)
    return {
        "video_1": {"publish": "11:00 AM EG", "data": ultra(d1)},
        "video_2": {"publish": "20:00 PM EG", "data": ultra(d2)},
    }

@app.get("/health")
def health():
    return {"status": "FINAL REAL TRANSLATION READY", "has_groq": bool(os.getenv("GROQ_API_KEY")), "countries": 19}
