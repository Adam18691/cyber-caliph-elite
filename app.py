from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import random, os, hashlib
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except:
    HAS_REQUESTS = False
    requests = None

app = FastAPI(title="SULAIMANI VAULT ELITE 10B - ULTRA CLEAN")
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

CTR_TEMPLATES_AR = [
    "🚨 {forb_ar} سم قاتل يدمر {disease_ar} | {allow_ar} يرمم في 7 ايام | {year}",
    "💀 ممنوع {forb_ar} بعد اليوم - {allow_ar} هو الحل | نظام الطيبات {percent}%",
    "⚠️ {secret_ar} | {forb_ar} يدمر {disease_ar} و {allow_ar} يعالجه نهائيا",
]

CTR_TEMPLATES_EN = "💀 FORBIDDEN {forb_en} DESTROYS {disease_en} | {allow_en} CURES in 7 Days | Tayyibat System {percent}%"

DISEASES = {
    "colon": {"ar": "القولون", "en": "Colon", "secret_ar": "القولون بيت الداء", "secret_en": "Colon is root of disease",
              "forbidden": [{"ar":"العيش البلدي","en":"White Bread"}, {"ar":"البقوليات","en":"Legumes"}, {"ar":"العدس","en":"Lentils"}],
              "allowed": [{"ar":"الارز","en":"Rice"}, {"ar":"التلبينة","en":"Talbina"}, {"ar":"العسل","en":"Honey"}]},
    "sugar": {"ar": "السكري", "en": "Diabetes", "secret_ar": "الانسولين سبوبة", "secret_en": "Insulin is a business",
              "forbidden": [{"ar":"السكر","en":"Sugar"}, {"ar":"العيش","en":"Bread"}, {"ar":"البسكويت","en":"Biscuits"}],
              "allowed": [{"ar":"الشعير","en":"Barley"}, {"ar":"الارز","en":"Rice"}, {"ar":"العسل","en":"Honey"}]},
    "pressure": {"ar": "الضغط", "en": "Blood Pressure", "secret_ar": "ادوية الضغط للابد", "secret_en": "BP meds for life",
                 "forbidden": [{"ar":"الملح","en":"Salt"}, {"ar":"العيش","en":"Bread"}], "allowed": [{"ar":"التلبينة","en":"Talbina"}, {"ar":"الموز","en":"Banana"}]},
    "heart": {"ar": "القلب", "en": "Heart", "secret_ar": "القسطرة بيزنس", "secret_en": "Stent is business",
              "forbidden": [{"ar":"الزيوت المهدرجة","en":"Seed Oils"}], "allowed": [{"ar":"زيت الزيتون","en":"Olive Oil"}, {"ar":"التلبينة","en":"Talbina"}]},
    "kidney": {"ar": "الكلى", "en": "Kidney", "secret_ar": "الشعير يغسل الكلى", "secret_en": "Barley washes kidney",
               "forbidden": [{"ar":"الملح","en":"Salt"}], "allowed": [{"ar":"الشعير","en":"Barley"}, {"ar":"العسل","en":"Honey"}]},
    "liver": {"ar": "الكبد", "en": "Liver", "secret_ar": "لا يوجد دواء للكبد الدهني", "secret_en": "No drug for fatty liver",
              "forbidden": [{"ar":"السكر","en":"Sugar"}], "allowed": [{"ar":"زيت الزيتون","en":"Olive Oil"}]},
    "bones": {"ar": "العظام", "en": "Bones", "secret_ar": "حقن العظام وهم", "secret_en": "Bone injections myth",
              "forbidden": [{"ar":"المياه الغازية","en":"Soda"}], "allowed": [{"ar":"التلبينة","en":"Talbina"}]},
    "cancer": {"ar": "المناعة", "en": "Immunity", "secret_ar": "الكيماوي تريليونات", "secret_en": "Chemo is trillions",
               "forbidden": [{"ar":"السكر","en":"Sugar"}], "allowed": [{"ar":"التلبينة","en":"Talbina"}, {"ar":"العسل","en":"Honey"}]},
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
                s = r.json().get("shorturl")
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

@app.get("/go/{hid}")
def go_redirect(hid: str):
    long_url = SHORT_CACHE.get(hid) or list(AFF_RAW.values())[0]
    return RedirectResponse(url=long_url, status_code=302)

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>ULTRA CLEAN 19 LANG LIVE</h1><a href='/api/ultra?disease=sugar'>TEST</a>"

@app.get("/api/ultra")
def ultra(disease: str = "colon"):
    try:
        dis = DISEASES.get(disease, DISEASES["colon"])
        forb = random.choice(dis["forbidden"])
        allow = random.choice(dis["allowed"])

        template_ar = random.choice(CTR_TEMPLATES_AR)
        title_ar = template_ar.format(forb_ar=forb["ar"], allow_ar=allow["ar"], disease_ar=dis["ar"], disease_en=dis["en"], secret_ar=dis["secret_ar"], year=datetime.now().year, percent=10000000000)

        title_en_base = CTR_TEMPLATES_EN.format(forb_en=forb["en"], allow_en=allow["en"], disease_en=dis["en"], percent=10000000000)

        trans = {
            "ar": f"⚠️ {title_ar} | {dis['secret_ar']} نهائيا",
            "en": f"{title_en_base} | {dis['secret_en']}",
            "fr": f"💀 INTERDIT {forb['en']} DETRUIT {dis['en']} | {allow['en']} GUERIT en 7 Jours | Tayyibat",
            "de": f"💀 VERBOTEN {forb['en']} ZERSTORT {dis['en']} | {allow['en']} HEILT in 7 Tagen | Tayyibat",
            "sv": f"💀 FORBJUDET {forb['en']} FORSTOR {dis['en']} | {allow['en']} BOTAR pa 7 Dagar | Tayyibat",
            "it": f"💀 VIETATO {forb['en']} DISTRUGGE {dis['en']} | {allow['en']} CURA in 7 Giorni | Tayyibat",
            "nl": f"💀 VERBODEN {forb['en']} VERNIETIGT {dis['en']} | {allow['en']} GENEEST in 7 Dagen | Tayyibat",
            "no": f"💀 FORBUDT {forb['en']} ODELEGGER {dis['en']} | {allow['en']} HELBREDER pa 7 Dager | Tayyibat",
            "eg": f"⚠️ {title_ar} | {dis['secret_ar']} نهائيا"
        }

        selected = random.sample(list(AFF_RAW.items()), 6)
        long_links = [v for k,v in selected]
        short_links = [safe_shorten(v) for v in long_links]

        video_prompt = f"Cinematic 8K {allow['en']} honey drip repairing {dis['en']} vs {forb['en']} poison destroying, Islamic golden light, ultra detailed"

        countries_data = {}
        for name, info in COUNTRIES.items():
            lang_map = {"de":"de","sv":"sv","fr":"fr","en":"en","no":"no","it":"it","nl":"nl","ar":"ar"}
            lk = lang_map.get(info["gtts"], "en")
            if info["code"] == "EG":
                lk = "ar"
            countries_data[name] = {"flag": info["flag"], "code": info["code"], "peak": info["peak"], "title": trans.get(lk, trans["en"]), "title_ar": trans["ar"]}

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
            "video_prompt_vault": video_prompt,
            "total_countries": 19,
            "system": "ULTRA CLEAN - 19 LANG PURE",
            "has_groq": bool(os.getenv("GROQ_API_KEY"))
        }
    except Exception as e:
        return {"error": str(e), "status": "FALLBACK"}

@app.get("/api/daily-2-videos")
def daily_2():
    try:
        d1, d2 = random.sample(list(DISEASES.keys()), 2)
        return {"video_1": ultra(d1), "video_2": ultra(d2), "status": "OK 2 VIDEOS CLEAN"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health():
    return {"status": "ULTRA CLEAN READY - 19 PURE LANG", "countries": 19, "has_groq": bool(os.getenv("GROQ_API_KEY"))}
