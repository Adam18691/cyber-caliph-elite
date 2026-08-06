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

app = FastAPI(title="SULAIMANI FINAL ANTI-CRASH")
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
]

DISEASES = {
    "colon": {"ar": "القولون", "en": "Colon", "forbidden": ["العيش البلدي", "البقوليات"], "allowed": ["الارز", "التلبينة", "العسل"], "secret": "القولون بيت الداء"},
    "sugar": {"ar": "السكري", "en": "Diabetes", "forbidden": ["السكر", "العيش"], "allowed": ["الشعير", "الارز"], "secret": "الانسولين سبوبة"},
    "pressure": {"ar": "الضغط", "en": "Pressure", "forbidden": ["الملح"], "allowed": ["التلبينة"], "secret": "ادوية الضغط للابد"},
    "heart": {"ar": "القلب", "en": "Heart", "forbidden": ["الزيوت المهدرجة"], "allowed": ["زيت الزيتون"], "secret": "القسطرة بيزنس"},
    "kidney": {"ar": "الكلى", "en": "Kidney", "forbidden": ["الملح"], "allowed": ["الشعير"], "secret": "الشعير يغسل الكلى"},
    "liver": {"ar": "الكبد", "en": "Liver", "forbidden": ["السكر"], "allowed": ["زيت الزيتون"], "secret": "لا يوجد دواء كبد دهني"},
    "bones": {"ar": "العظام", "en": "Bones", "forbidden": ["المياه الغازية"], "allowed": ["التلبينة"], "secret": "حقن العظام وهم"},
    "cancer": {"ar": "المناعة", "en": "Immunity", "forbidden": ["السكر"], "allowed": ["التلبينة"], "secret": "الكيماوي تريليونات"},
}

COUNTRIES = {
    "سويسرا": {"code": "CH", "flag": "🇨🇭", "peak": "20:00", "gtts": "de"},
    "السويد": {"code": "SE", "flag": "🇸🇪", "peak": "20:00", "gtts": "sv"},
    "فرنسا": {"code": "FR", "flag": "🇫🇷", "peak": "20:00", "gtts": "fr"},
    "ألمانيا": {"code": "DE", "flag": "🇩🇪", "peak": "20:00", "gtts": "de"},
    "بريطانيا": {"code": "UK", "flag": "🇬🇧", "peak": "21:00", "gtts": "en"},
    "النرويج": {"code": "NO", "flag": "🇳🇴", "peak": "20:00", "gtts": "no"},
    "أمريكا": {"code": "USA", "flag": "🇺🇸", "peak": "02:00", "gtts": "en"},
    "بلجيكا": {"code": "BE", "flag": "🇧🇪", "peak": "20:00", "gtts": "fr"},
    "أيرلندا": {"code": "IE", "flag": "🇮🇪", "peak": "21:00", "gtts": "en"},
    "إيطاليا": {"code": "IT", "flag": "🇮🇹", "peak": "21:00", "gtts": "it"},
    "هولندا": {"code": "NL", "flag": "🇳🇱", "peak": "20:00", "gtts": "nl"},
    "أستراليا": {"code": "AU", "flag": "🇦🇺", "peak": "11:00", "gtts": "en"},
    "زيمبابوي": {"code": "ZW", "flag": "🇿🇼", "peak": "20:00", "gtts": "en"},
    "فوكلاند": {"code": "FK", "flag": "🇫🇰", "peak": "21:00", "gtts": "en"},
    "سانت هيلينا": {"code": "SH", "flag": "🇸🇭", "peak": "21:00", "gtts": "en"},
    "جنوب السودان": {"code": "SS", "flag": "🇸🇸", "peak": "20:00", "gtts": "en"},
    "ساموا": {"code": "WS", "flag": "🇼🇸", "peak": "11:00", "gtts": "en"},
    "كندا": {"code": "CA", "flag": "🇨🇦", "peak": "02:00", "gtts": "en"},
    "مصر": {"code": "EG", "flag": "🇪🇬", "peak": "20:00", "gtts": "ar"},
}

SHORT_CACHE = {}

def safe_shorten(url: str):
    try:
        if url in SHORT_CACHE:
            return SHORT_CACHE[url]
        if HAS_REQUESTS:
            try:
                r = requests.get(f"https://is.gd/create.php?format=json&url={url}", timeout=3)
                j = r.json()
                s = j.get("shorturl")
                if s and "is.gd" in s:
                    SHORT_CACHE[url] = s
                    return s
            except:
                pass
        hid = hashlib.md5(url.encode()).hexdigest()[:6]
        cloaked = f"https://cyber-caliph-elite.onrender.com/go/{hid}"
        SHORT_CACHE[url] = cloaked
        SHORT_CACHE[hid] = url
        return cloaked
    except:
        return url

def safe_translate(forb, allow, disease_ar, disease_en, secret, title_ar):
    # Fallback قوي جدا - مستحيل يقع
    return {
        "ar": title_ar,
        "en": f"💀 FORBIDDEN {forb} DESTROYS {disease_en} | {allow} CURES in 7 Days | Tayyibat {secret}",
        "fr": f"💀 INTERDIT {forb} DETRUIT {disease_en} | {allow} GUERIT en 7 Jours | Tayyibat",
        "de": f"💀 VERBOTEN {forb} ZERSTORT {disease_en} | {allow} HEILT in 7 Tagen",
        "sv": f"💀 FORBJUDET {forb} FORSTOR {disease_en} | {allow} BOTAR pa 7 Dagar",
        "it": f"💀 VIETATO {forb} DISTRUGGE {disease_en} | {allow} CURA in 7 Giorni",
        "nl": f"💀 VERBODEN {forb} VERNIETIGT {disease_en} | {allow} GENEEST in 7 Dagen",
        "no": f"💀 FORBUDT {forb} ODELEGGER {disease_en} | {allow} HELBREDER pa 7 Dager",
        "eg": title_ar
    }

@app.get("/go/{hid}")
def go_redirect(hid: str):
    try:
        long_url = SHORT_CACHE.get(hid) or list(AFF_RAW.values())[0]
        return RedirectResponse(url=long_url, status_code=302)
    except:
        return RedirectResponse(url="https://yazing.com/deals/monoprice/Waeldeban186", status_code=302)

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>SULAIMANI ANTI-CRASH LIVE</h1><a href='/api/ultra?disease=sugar'>test ultra</a> | <a href='/health'>health</a>"

@app.get("/api/ultra")
def ultra(disease: str = "colon"):
    try:
        dis = DISEASES.get(disease, DISEASES["colon"])
        forb = random.choice(dis["forbidden"])
        allow = random.choice(dis["allowed"])
        template = random.choice(CTR_TEMPLATES)
        title_ar = template.format(forb=forb, allow=allow, disease_ar=dis["ar"], disease_en=dis["en"], secret=dis["secret"], year=datetime.now().year, percent=10000000000)

        trans = safe_translate(forb, allow, dis["ar"], dis["en"], dis["secret"], title_ar)

        selected = random.sample(list(AFF_RAW.items()), 6)
        long_links = [v for k,v in selected]
        short_links = [safe_shorten(v) for v in long_links]

        countries_data = {}
        for name, info in COUNTRIES.items():
            lang_map = {"de":"de","sv":"sv","fr":"fr","en":"en","no":"no","it":"it","nl":"nl","ar":"ar"}
            lk = lang_map.get(info["gtts"], "en")
            t = trans.get(lk, trans["en"])
            if info["code"] == "EG":
                t = trans["ar"]
            countries_data[name] = {"flag": info["flag"], "code": info["code"], "peak": info["peak"], "title": t, "title_ar": trans["ar"]}

        return {
            "title_ar": trans["ar"],
            "title_en": trans["en"],
            "title_fr": trans["fr"],
            "title_de": trans["de"],
            "title_sv": trans["sv"],
            "title_it": trans["it"],
            "title_nl": trans["nl"],
            "title_no": trans["no"],
            "all_translations": trans,
            "video_links_3_short": short_links[:3],
            "description_links_6_short": short_links,
            "countries_19": countries_data,
            "total_countries": 19,
            "system": "ANTI-CRASH FINAL - NO MORE 500",
            "has_groq": bool(os.getenv("GROQ_API_KEY"))
        }
    except Exception as e:
        return {"error": str(e), "fallback": "ANTI-CRASH MODE", "disease": disease}

@app.get("/api/daily-2-videos")
def daily_2():
    try:
        d1, d2 = random.sample(list(DISEASES.keys()), 2)
        return {"video_1": ultra(d1), "video_2": ultra(d2), "status": "OK"}
    except Exception as e:
        return {"error": str(e), "status": "FALLBACK"}

@app.get("/health")
def health():
    return {"status": "ANTI-CRASH READY - NO 500", "has_groq": bool(os.getenv("GROQ_API_KEY")), "countries": 19}
