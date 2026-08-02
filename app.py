# FILE: app.py - v136 FINAL ALL - دمج v115 + v134 + FIX ANTIALIAS
import os, sys, tempfile
from pathlib import Path
sys.dont_write_bytecode=True

# ===== FIX PIL ANTIALIAS - MUST BE FIRST =====
try:
    from PIL import Image
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.LANCZOS
    import PIL.Image
    if not hasattr(PIL.Image, 'ANTIALIAS'):
        PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
except:
    pass

import requests
from datetime import datetime

# ========= 1. Flow Handling =========
FLOW_AVAILABLE=False
FLOW_LOCATION=""
FORBIDDEN_TEXT="بيض ممنوع - 11 ممنوع - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]

try:
    from modules.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
    FLOW_AVAILABLE=True
    FLOW_LOCATION="modules/flow.py"
except:
    try:
        from core.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
        FLOW_AVAILABLE=True
        FLOW_LOCATION="core/flow.py"
    except:
        FLOW_AVAILABLE=False
        def generate_image_flow(prompt, country_code=None, model="imagen-3.0-generate-001", aspect_ratio="16:9", style=""):
            return {"id":f"FLOW-FALLBACK-{datetime.now().strftime('%H%M%S')}-v136","prompt":prompt[:50],"forbidden":FORBIDDEN_TEXT}
        def generate_all_21_countries_flow_images(base_prompt, model="imagen-3.0-generate-001"):
            return {"jobs":[],"count":0,"forbidden":FORBIDDEN_TEXT,"forbidden_count":11}
        def list_flow_jobs():
            return []

# ========= 2. Tayybat =========
LINKS_6_DETAILED = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% توفير", "name": "Kie.AI"}
}
LINKS_6_SIMPLE = {k: v["url"] for k,v in LINKS_6_DETAILED.items()}
LINKS_6 = LINKS_6_SIMPLE # للتوافق مع القديم

VIDEO_DESCRIPTION = """🍞 نظام طيبات الدكتور ضياء العوضى - بدون بيض - 11 ممنوع
الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض
المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه
فطار: توست+زبدة+عسل | غداء: أرز+لحم ضاني+بطاطس | عشاء: بقسماط+قشطة+موز
⚠️ تنبيه: محتوى ثقافي - ليس علاج طبي
━━━━━━━━━━━━━━━━━━━━━━
🛒 كل لينك دقيقة ×6 = 6 دقايق
فيديو 30 دقيقة = 24 دقيقة محتوى + 6 دقايق لينكات
فيديو 60 دقيقة = 54 دقيقة محتوى + 6 دقايق لينكات
1️⃣ Monoprice 70% - https://yazing.com/deals/monoprice/Waeldeban186
2️⃣ Lands End 60% - https://yazing.com/deals/landsend/Waeldeban186
3️⃣ ShopSimon 70% - https://yazing.com/deals/shopsimon/Waeldeban186
4️⃣ Cole Haan 50%+20% - https://yazing.com/deals/colehaan/Waeldeban186
5️⃣ HF Online UK 50% - https://yazing.com/deals/hfonline-uk/Waeldeban186
6️⃣ Kie.ai 80% - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66
📺 https://www.youtube.com/@CursedMedicineEG
#طيبات #Waeldeban186
"""

try:
    from core.tayybat import get_tayybat_info, get_links_6, get_video_description_with_links
    TAYYBAT_AVAILABLE=True
except:
    TAYYBAT_AVAILABLE=False
    def get_links_6(): return LINKS_6_SIMPLE
    def get_video_description_with_links(): return VIDEO_DESCRIPTION
    def get_tayybat_info():
        return {"forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS,"forbidden_count":11,"links":LINKS_6_SIMPLE,"tayybat":True}

# ========= 3. Flask =========
from flask import Flask, Response, request, jsonify, send_file
app=Flask(__name__)
app.secret_key="v136-FINAL-ALL-ANTIALIAS-FIXED-1minx6"

def get_html():
    p=Path(__file__).parent/"templates"/"index.html"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return f"<html><body><h1>v136 FINAL - طيبات - 1min x6 - Flow={FLOW_AVAILABLE} - {FORBIDDEN_TEXT[:30]}</h1></body></html>"

@app.route('/')
def index():
    html=get_html()
    resp=Response(html,mimetype='text/html')
    resp.headers['X-Flow-Available']=str(FLOW_AVAILABLE)
    resp.headers['X-Version']="v136-FIXED-ANTIALIAS"
    return resp

@app.route('/api/topics')
def topics_api():
    info=get_tayybat_info()
    info["flow_available"]=FLOW_AVAILABLE
    info["flow_location"]=FLOW_LOCATION
    return jsonify(info)

@app.route('/api/links')
def links_api():
    try:
        links = get_links_6()
        desc = get_video_description_with_links()
        info = get_tayybat_info()
        return jsonify({
            "links": LINKS_6_DETAILED,
            "links_simple": links,
            "description": desc,
            "video_description": desc,
            "forbidden": FORBIDDEN_TEXT,
            "forbidden_count": 11,
            "status": "ok",
            "version": "v136"
        })
    except Exception as e:
        return jsonify({"status":"error","error":str(e)[:200],"links":LINKS_6_DETAILED}), 500

@app.route('/api/tayybat')
def tayybat_api():
    info=get_tayybat_info()
    info["flow_available"]=FLOW_AVAILABLE
    return jsonify(info)

@app.route('/api/flow/generate',methods=['POST'])
def flow_generate():
    d=request.get_json() if request.is_json else {}
    job=generate_image_flow(d.get('prompt','طيبات بدون بيض'),d.get('country_code'),d.get('model','imagen-3.0-generate-001'))
    return jsonify(job)

@app.route('/api/flow/generate-21',methods=['POST'])
def flow_21():
    d=request.get_json() if request.is_json else {}
    result=generate_all_21_countries_flow_images(d.get('prompt','طيبات 21 دولة'),d.get('model','imagen-3.0-generate-001'))
    return jsonify(result)

@app.route('/api/flow/list')
def flow_list():
    return jsonify({"jobs":list_flow_jobs(),"count":len(list_flow_jobs()),"forbidden":FORBIDDEN_TEXT,"forbidden_count":11})

@app.route('/api/flow/status')
def flow_status():
    return jsonify({"flow_available":FLOW_AVAILABLE,"flow_location":FLOW_LOCATION,"forbidden_count":11,"version":"v136"})

# ========= VIDEO ENDPOINTS - v134 + FIX =========
def create_link_image_1min(text, url, discount, path, size=(1280,720)):
    from PIL import Image, ImageDraw
    img = Image.new('RGB', size, color=(0,100,0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,size[0],150], fill=(0,0,0))
    try:
        draw.text((50,30), f"{text} - {discount} - 1 MIN", fill=(255,255,0))
        draw.text((50,200), f"{url}"[:80], fill=(255,255,255))
        draw.text((50,300), f"Waeldeban186 - طيبات بدون بيض - 11 ممنوع", fill=(255,215,0))
        draw.text((50,500), f"كل لينك دقيقة x6=6 دقايق", fill=(255,255,255))
    except:
        pass
    img.save(path)
    return path

def download_images(images, temp_dir):
    local=[]
    for i, url in enumerate(images[:21]):
        try:
            if not url or not isinstance(url,str): continue
            if url.startswith('http'):
                r=requests.get(url, timeout=30)
                if r.status_code==200:
                    p=os.path.join(temp_dir, f"c_{i:02d}.jpg")
                    open(p,'wb').write(r.content)
                    local.append(p)
        except: continue
    if not local:
        from PIL import Image
        for i in range(3):
            p=os.path.join(temp_dir, f"ph_{i}.jpg")
            Image.new('RGB',(1280,720),color=(139,69,19)).save(p)
            local.append(p)
    return local

def build_montage_video(local_images, temp_dir, total_minutes):
    from moviepy.editor import ImageSequenceClip, concatenate_videoclips
    link_minutes = 6
    content_minutes = total_minutes - link_minutes
    if total_minutes == 6:
        content_minutes = 0
        content_per_product_min = 0
    else:
        content_per_product_min = content_minutes / 6.0
    link_per_product_min = 1.0
    images_per_product = max(1, len(local_images)//6)
    final_clips=[]
    link_keys=list(LINKS_6_DETAILED.keys())
    for prod_idx in range(6):
        if content_per_product_min > 0:
            s = prod_idx * images_per_product
            e = s + images_per_product
            prod_imgs = local_images[s:e] or local_images[:images_per_product]
            sec_per_img = (content_per_product_min*60) / max(1,len(prod_imgs))
            for img_path in prod_imgs:
                clip = ImageSequenceClip([img_path], fps=1).set_duration(sec_per_img).resize((1280,720))
                final_clips.append(clip)
        link_info = LINKS_6_DETAILED[link_keys[prod_idx %6]]
        link_img = os.path.join(temp_dir, f"link_{prod_idx}.jpg")
        create_link_image_1min(link_keys[prod_idx], link_info['url'], link_info['discount'], link_img)
        link_clip = ImageSequenceClip([link_img], fps=1).set_duration(link_per_product_min*60).resize((1280,720))
        final_clips.append(link_clip)
    output_path = os.path.join(temp_dir, f"tayybat_{total_minutes}min_1minx6.mp4")
    final_video = concatenate_videoclips(final_clips, method="compose")
    final_video.write_videofile(output_path, fps=24, codec='libx264', audio=False, logger=None)
    return output_path

@app.route('/generate-video-tayybat', methods=['POST'])
def generate_video_tayybat():
    try:
        data = request.get_json(force=True) if request.is_json else {}
        total_minutes = int(data.get('total_minutes', 6))
        if total_minutes not in [6,30,45,60]:
            total_minutes = 6
        images = data.get('images', [])
        if not images and 'jobs' in data:
            jobs=data['jobs']
            if isinstance(jobs,list):
                images=[j.get('file') or j.get('url') for j in jobs if j.get('file') or j.get('url')]
        temp_dir=tempfile.mkdtemp(prefix=f"tayybat_{total_minutes}min_")
        local_images=download_images(images, temp_dir)
        output_path = build_montage_video(local_images, temp_dir, total_minutes=total_minutes)
        return send_file(output_path, as_attachment=True, download_name=f"tayybat_{total_minutes}min_1minx6.mp4", mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:1000]}),500

@app.route('/api/video/montage-30', methods=['POST'])
def montage_30(): return generate_video_tayybat_wrapper(30)
@app.route('/api/video/montage-45', methods=['POST'])
def montage_45(): return generate_video_tayybat_wrapper(45)
@app.route('/api/video/montage-60', methods=['POST'])
def montage_60(): return generate_video_tayybat_wrapper(60)

def generate_video_tayybat_wrapper(mins):
    # helper to force minutes
    try:
        data = request.get_json(force=True) if request.is_json else {}
    except:
        data = {}
    data['total_minutes']=mins
    # inject back
    from flask import g
    # call main logic directly
    temp_dir=tempfile.mkdtemp(prefix=f"tayybat_{mins}min_")
    images = data.get('images', [])
    if not images and 'jobs' in data:
        jobs=data.get('jobs',[])
        images=[j.get('file') or j.get('url') for j in jobs if j.get('file') or j.get('url')]
    local_images=download_images(images, temp_dir)
    output_path = build_montage_video(local_images, temp_dir, total_minutes=mins)
    return send_file(output_path, as_attachment=True, download_name=f"tayybat_{mins}min_1minx6.mp4", mimetype='video/mp4')

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "version": "v136 - 1min x6=6min - 30/45/60min - ANTIALIAS FIXED",
        "forbidden_count": 11,
        "flow_available": FLOW_AVAILABLE,
        "flow_location": FLOW_LOCATION,
        "endpoints": ["/generate-video-tayybat","/api/video/montage-30","/api/video/montage-45","/api/video/montage-60","/api/links","/api/flow/generate-21","/health"]
    })

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
