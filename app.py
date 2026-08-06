from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import random, os, time, requests

app = FastAPI(title="ULTRA VIP - KIE + GEMINI + GROQ")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

AFF = [
    "https://yazing.com/deals/monoprice/Waeldeban186",
    "https://yazing.com/deals/landsend/Waeldeban186",
    "https://yazing.com/deals/shopsimon/Waeldeban186",
    "https://yazing.com/deals/colehaan/Waeldeban186",
    "https://yazing.com/deals/hfonline-uk/Waeldeban186",
    "https://kie.ai?ref=0e3195dd062b11f0da7496dd3c1bf66",
    "https://yazing.com/deals/hp-ca/Waeldeban186",
    "https://yazing.com/deals/lifeextension/Waeldeban186",
    "https://yazing.com/deals/lumens/Waeldeban186",
    "https://yazing.com/deals/nortiv8/Waeldeban186",
    "https://yazing.com/deals/muckbootcompany/Waeldeban186",
    "https://yazing.com/deals/sunberhair/Waeldeban186",
]
DISEASES = {
    "colon": {"ar": "القولون", "forbidden": ["العيش", "البقوليات"], "allowed": ["الارز", "التلبينة"]},
    "sugar": {"ar": "السكري", "forbidden": ["العيش", "السكر"], "allowed": ["الشعير", "زيت الزيتون"]},
    "pressure": {"ar": "الضغط", "forbidden": ["الملح", "الشيبسي"], "allowed": ["التلبينة", "الكركديه"]},
}

# ذاكرة مؤقتة للفيديوهات
VIDEO_JOBS = {}

def generate_with_kie(prompt):
    try:
        key = os.getenv("KIE_API_KEY")
        if not key: return None
        # KIE API - Kling Fast (اسرع واحد 15 ثانية)
        r = requests.post("https://api.kie.ai/api/v1/jobs/createTask",
            headers={"Authorization": f"Bearer {key}"},
            json={"model": "kling-v2-1", "input": {"prompt": prompt, "duration": 5}},
            timeout=30)
        data = r.json()
        task_id = data.get("data", {}).get("taskId")
        if not task_id: return None
        # انتظر
        for _ in range(30):
            time.sleep(5)
            check = requests.get(f"https://api.kie.ai/api/v1/jobs/recordInfo?taskId={task_id}",
                headers={"Authorization": f"Bearer {key}"}).json()
            if check.get("data", {}).get("state") == "success":
                return check["data"]["resultJson"]["resultUrls"][0]
        return None
    except: return None

def generate_with_gemini(prompt):
    try:
        from google import genai
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key: return None
        client = genai.Client(api_key=api_key)
        op = client.models.generate_videos(model="veo-3.0-fast-generate-001", prompt=prompt)
        while not op.done:
            time.sleep(10)
            op = client.operations.get(op)
        uri = op.response.generated_videos[0].video.uri
        return f"{uri}&key={api_key}"
    except Exception as e:
        print(e)
        return None

@app.get("/", response_class=HTMLResponse)
def home():
    return open("templates/index.html", encoding="utf-8").read()

@app.get("/api/ultra")
def ultra(disease: str = "colon"):
    links = random.sample(AFF, 6)
    vlinks = links[:3]
    dis = DISEASES.get(disease, DISEASES["colon"])
    forb = random.choice(dis["forbidden"])
    allow = random.choice(dis["allowed"])
    title = f"💀 {allow} يرمم {dis['ar']} | {forb} سم قاتل | نظام الطيبات 10000000000%"
    desc = f"{title}\n\nLINK1: {links[0]}\nLINK2: {links[1]}\nLINK3: {links[2]}\nLINK4: {links[3]}\nLINK5: {links[4]}\nLINK6: {links[5]}\n\nOVERLAY: {vlinks}"
    return {
        "title_ar": title,
        "title_en": title,
        "title_fr": title,
        "title_de": title,
        "description": desc,
        "video_links_3": vlinks,
        "description_links_6": links,
        "video_prompt": f"32K macro honey drip {allow} vs {forb} Islamic golden light",
        "video_file_direct": f"https://cyber-caliph-elite.onrender.com/api/generate-video?prompt={allow} vs {forb}",
        "seo_tags": ["نظام الطيبات", allow, forb],
    }

@app.get("/api/generate-video")
def gen_video(prompt: str):
    # 1- جرب KIE (اسرع 15ث)
    url = generate_with_kie(prompt)
    if url: return {"status": "done", "video_file": url, "provider": "KIE Kling 15s"}
    # 2- جرب Gemini Veo 3 Fast (60ث)
    url = generate_with_gemini(prompt)
    if url: return {"status": "done", "video_file": url, "provider": "GEMINI Veo3 Fast 60s"}
    return {"error": "No provider worked, check KIE_API_KEY and GEMINI_API_KEY in Render"}

@app.get("/health")
def health():
    return {"keys": {"KIE": bool(os.getenv("KIE_API_KEY")), "GEMINI": bool(os.getenv("GEMINI_API_KEY")), "GROQ": bool(os.getenv("GROQ_API_KEY"))}}
