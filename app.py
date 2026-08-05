from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="SULEIMANI ULTRA 10B - 3 LINKS VIDEO - VIP")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

AFF = [
    "https://yazing.com/deals/monoprice/Waeldeban186",
    "https://yazing.com/deals/landsend/Waeldeban186",
    "https://yazing.com/deals/shopsimon/Waeldeban186",
    "https://yazing.com/deals/colehaan/Waeldeban186",
    "https://yazing.com/deals/hfonline-uk/Waeldeban186",
    "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66",
    "https://yazing.com/deals/hp-ca/Waeldeban186",
    "https://yazing.com/deals/lifeextension/Waeldeban186",
    "https://yazing.com/deals/lumens/Waeldeban186",
    "https://yazing.com/deals/nortiv8/Waeldeban186",
    "https://yazing.com/deals/muckbootcompany/Waeldeban186",
    "https://yazing.com/deals/sunberhair/Waeldeban186",
]

DISEASES = {
    "colon": {"ar": "القولون", "forbidden": ["العيش", "البقوليات"], "allowed": ["الارز", "الشعير"]},
    "sugar": {"ar": "السكر", "forbidden": ["العيش", "السكر"], "allowed": ["الشعير", "زيت الزيتون"]},
    "pressure": {"ar": "الضغط", "forbidden": ["الملح", "الشيبسي"], "allowed": ["التلبينة", "الكركديه"]},
}

@app.get("/", response_class=HTMLResponse)
def home():
    return open("templates/index.html", encoding="utf-8").read()

@app.get("/api/ultra")
def ultra(disease: str = "colon"):
    links = random.sample(AFF, 6)
    video_links = links[:3]
    dis = DISEASES.get(disease, DISEASES["colon"])
    forb = random.choice(dis["forbidden"])
    allow = random.choice(dis["allowed"])
    quote = random.choice(["انت مش مريض انت بتاكل غلط", "بطنك هي مخك التاني", "القولون بيت الداء", "التلبينة مجمة لفؤاد المريض"])

    title_ar = f"💀 {quote} | {forb} سم قاتل يدمر {dis['ar']} | {allow} يرمم في 7 ايام | نظام الطيبات 10000000000%"
    title_en = f"💀 {forb} KILLS {dis['ar']} | {allow} HEALS | Tayyibat 10000000000%"
    title_fr = f"💀 {forb} tue {dis['ar']} | {allow} guerit | Tayyibat"
    title_de = f"💀 {forb} totet | {allow} heilt | Tayyibat"

    description = f"""{title_ar}

🎬 3 لينكات تظهر في الفيديو:

00:00 مقدمة: {quote}
01:00 {forb} يدمر {dis['ar']}
OVERLAY VIDEO LINK 1: {video_links[0]}

02:00 {allow} يرمم المعدة - مجمة لفؤاد المريض
OVERLAY VIDEO LINK 2: {video_links[1]}

04:00 مصانع الادوية تخفي + علاج بدون ادوية
OVERLAY VIDEO LINK 3: {video_links[2]}

📝 الوصف الكامل - 6 لينكات:
LINK1: {links[0]}
LINK2: {links[1]}
LINK3: {links[2]}
LINK4: {links[3]}
LINK5: {links[4]}
LINK6: {links[5]}

جرب KIE.AI: https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66

#نظام_الطيبات #دكتور_ضياء_العوضي #Waeldeban186 #10000000000%
"""

    return {
        "title_ar": title_ar,
        "title_en": title_en,
        "title_fr": title_fr,
        "title_de": title_de,
        "description": description,
        "video_links_3": video_links,
        "description_links_6": links,
        "video_structure": f"دقيقة 1: {video_links[0]} | دقيقة 2: {video_links[1]} | دقيقة 4: {video_links[2]}",
        "thumbnail_prompt": f"32K ULTRA split RED X {forb} GREEN CHECK {allow} TEXT الطيبات giant gold glow - 3 products overlay - Pharma $ X - CTR 22% - VIP HIDDEN",
        "video_prompt": f"32K TOP-DOWN 90 + CLOSE-UP macro f1.2 1000fps honey drip - {allow} vs {forb} - 3 LINKS OVERLAY BURNED IN VIDEO: {video_links[0]} at 01:00, {video_links[1]} at 02:00, {video_links[2]} at 04:00 - TEXT الطيبات only - NO FACE - ULTRA HIDDEN",
        "seo_tags": ["نظام الطيبات", "دكتور ضياء العوضي", f"علاج {dis['ar']}", "مصانع الادوية تخفي", "10000000000%", "Waeldeban186"],
        "countries": ["سويسرا", "السويد", "فرنسا", "المانيا", "UK", "النرويج", "USA", "بلجيكا", "ايرلندا", "ايطاليا", "هولندا", "استراليا", "زيمبابوي", "فوكلاند", "سانت هيلينا", "جنوب السودان", "ساموا", "كندا", "مصر"],
        "hidden_vip": "3 LINKS VIDEO + 6 LINKS DESCRIPTION - 10000000000% VIP ONLY"
    }

@app.get("/api/6min3links")
def six_three():
    links = random.sample(AFF, 6)
    return {"video_3": links[:3], "desc_6": links}

@app.get("/health")
def health():
    return {"status": "ULTRA 10B - 3 LINKS VIDEO - 6 LINKS DESC - شغال VIP", "aff": len(AFF)}
