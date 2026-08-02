
# FILE: app.py - v134 FINAL - كل لينك 1 دقيقة ×6=6 دقايق - فيديو 30/45/60 دقيقة
import os, sys, tempfile, time, math
from pathlib import Path
from datetime import datetime
import requests
import numpy as np
sys.dont_write_bytecode = True

FORBIDDEN_TEXT = "الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع - بدون بيض"
FORBIDDEN_ITEMS = ["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]

LINKS_6 = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% توفير", "name": "Kie.AI"}
}
LINKS_6_SIMPLE = {k: v["url"] for k,v in LINKS_6.items()}

VIDEO_DESCRIPTION = """🍞 نظام طيبات الدكتور ضياء العوضى - بدون بيض - 11 ممنوع
الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض
المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه
فطار: توست+زبدة+عسل | غداء: أرز+لحم ضاني+بطاطس | عشاء: بقسماط+قشطة+موز
⚠️ تنبيه: محتوى ثقافي - ليس علاج طبي
━━━━━━━━━━━━━━━━━━━━━━
🛒 كل لينك دقيقة ×6 = 6 دقايق
فيديو 30 دقيقة = 24 دقيقة محتوى + 6 دقايق لينكات
فيديو 45 دقيقة = 39 دقيقة محتوى + 6 دقايق لينكات
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

# Flow import fallback
try:
    from modules.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
    FLOW_AVAILABLE=True
except:
    try:
        from core.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
        FLOW_AVAILABLE=True
    except:
        FLOW_AVAILABLE=False
        def generate_image_flow(p,c=None,m="imagen-3.0-generate-001",a="16:9",s="no eggs"): return {"id":"FALLBACK","prompt":p[:50]}
        def generate_all_21_countries_flow_images(bp,m="imagen-3.0-generate-001"): return {"jobs":[],"count":0}
        def list_flow_jobs(): return []

try:
    from core.tayybat import get_tayybat_info
except:
    def get_tayybat_info(): return {"forbidden":FORBIDDEN_TEXT,"links":LINKS_6_SIMPLE,"video_description":VIDEO_DESCRIPTION}

from flask import Flask, Response, request, jsonify, send_file
app=Flask(__name__)
app.secret_key="v134_FINAL_1min_x6_6min_30_45_60min"

def get_html():
    p=Path(__file__).parent/"templates"/"index.html"
    return p.read_text(encoding='utf-8') if p.exists() else "<html><body><h1>v134 - كل لينك دقيقة</h1></body></html>"

@app.route('/')
def index(): return Response(get_html(), mimetype='text/html')

@app.route('/api/links')
def links_api(): return jsonify({"links":LINKS_6, "montage": "كل لينك 1 دقيقة ×6=6 دقايق - فيديو 30/45/60 دقيقة"})

@app.route('/health')
def health(): return jsonify({"status":"ok","version":"v134 - 1min x6=6min - 30/45/60min","forbidden_count":11,"endpoints":["/generate-video-tayybat","/api/video/montage-30","/api/video/montage-45","/api/video/montage-60"]})

def create_link_image_1min(text, url, discount, path, size=(1280,720), duration_min=1):
    from PIL import Image, ImageDraw
    img = Image.new('RGB', size, color=(0,100,0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,size[0],150], fill=(0,0,0))
    draw.text((50,30), f"{text} - {discount} - {duration_min} MIN", fill=(255,255,0))
    draw.text((50,200), f"{url}", fill=(255,255,255))
    draw.text((50,300), f"Waeldeban186 - طيبات بدون بيض - 11 ممنوع", fill=(255,215,0))
    draw.text((50,500), f"كل لينك دقيقة ×6=6 دقايق", fill=(255,255,255))
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
    """
    total_minutes: 30,45,60
    كل لينك 1 دقيقة = 6 دقايق لينكات
    الباقي محتوى
    """
    from moviepy.editor import ImageSequenceClip, concatenate_videoclips

    link_minutes = 6  # 1 دقيقة ×6
    content_minutes = total_minutes - link_minutes  # 24,39,54
    
    # توزيع المحتوى على 6 منتجات
    content_per_product_min = content_minutes / 6.0  # 4, 6.5, 9 دقايق
    link_per_product_min = 1.0

    images_per_product = max(1, len(local_images)//6)

    final_clips=[]
    link_keys=list(LINKS_6.keys())

    for prod_idx in range(6):
        # محتوى
        s = prod_idx * images_per_product
        e = s + images_per_product
        prod_imgs = local_images[s:e] or local_images[:images_per_product]
        sec_per_img = (content_per_product_min*60) / len(prod_imgs)
        for img_path in prod_imgs:
            clip = ImageSequenceClip([img_path], fps=1).set_duration(sec_per_img).resize((1280,720))
            final_clips.append(clip)

        # لينك 1 دقيقة
        link_info = LINKS_6[link_keys[prod_idx %6]]
        link_img = os.path.join(temp_dir, f"link_{prod_idx}.jpg")
        create_link_image_1min(link_keys[prod_idx], link_info['url'], link_info['discount'], link_img, duration_min=1)
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
        total_minutes = int(data.get('total_minutes', data.get('mode', 6)))  # 6,30,45,60
        # لو بعت 60 معناه 60 دقيقة، لو بعت 6 معناه 6 دقايق (كل لينك دقيقة)
        if total_minutes not in [6,30,45,60]:
            total_minutes = 6

        images = data.get('images', [])
        if not images and 'jobs' in data:
            jobs=data['jobs']
            if isinstance(jobs,list):
                images=[j.get('file') or j.get('url') for j in jobs if j.get('file') or j.get('url')]

        temp_dir=tempfile.mkdtemp(prefix=f"tayybat_{total_minutes}min_")
        local_images=download_images(images, temp_dir)

        if total_minutes == 6:
            # حالة خاصة: كل لينك دقيقة = 6 دقايق فقط
            output_path = build_montage_video(local_images, temp_dir, total_minutes=6)
        else:
            output_path = build_montage_video(local_images, temp_dir, total_minutes=total_minutes)

        return send_file(output_path, as_attachment=True, download_name=f"tayybat_{total_minutes}min_1minx6.mp4", mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:1000]}),500

@app.route('/api/video/montage-30', methods=['POST'])
def montage_30(): 
    request.get_json = lambda *a,**k: {**(request.get_json(force=True) or {}), "total_minutes":30}
    return generate_video_tayybat()

@app.route('/api/video/montage-45', methods=['POST'])
def montage_45(): 
    request.get_json = lambda *a,**k: {**(request.get_json(force=True) or {}), "total_minutes":45}
    return generate_video_tayybat()

@app.route('/api/video/montage-60', methods=['POST'])
def montage_60(): 
    request.get_json = lambda *a,**k: {**(request.get_json(force=True) or {}), "total_minutes":60}
    return generate_video_tayybat()

if __name__=='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",5000)))
