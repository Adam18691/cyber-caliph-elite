# FILE: app.py - v138 ULTRA FAST 0.00000000000001 - 3 ثواني بس - كل لينك دقيقة x6=6 دقايق
import os, sys, tempfile
from pathlib import Path
sys.dont_write_bytecode=True
try:
    from PIL import Image
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.LANCZOS
    import PIL.Image
    if not hasattr(PIL.Image, 'ANTIALIAS'):
        PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
except: pass
import requests
from datetime import datetime
FLOW_AVAILABLE=False
FLOW_LOCATION=""
FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - 0.00000000000001"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]
try:
    from core.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
    FLOW_AVAILABLE=True
    FLOW_LOCATION="core/flow.py"
except:
    def generate_image_flow(p,c=None,m="a",a="16:9",s=""): return {"id":"v138-ULTRA-0.00000000000001"}
    def generate_all_21_countries_flow_images(bp,m="a"): return {"jobs":[],"count":0}
    def list_flow_jobs(): return []

LINKS_6_DETAILED = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% توفير", "name": "Kie.AI"}
}
from flask import Flask, Response, request, jsonify, send_file
app=Flask(__name__)

@app.route('/')
def index():
    resp=Response("<h1>v138 ULTRA FAST 0.00000000000001</h1>",mimetype='text/html')
    resp.headers['X-Tayybat']="0.00000000000001"
    resp.headers['X-Version']="v138-ULTRA-FAST-0.00000000000001"
    return resp

@app.route('/health')
def health():
    return jsonify({"status":"ok","version":"v138 - ULTRA FAST 0.00000000000001 - 3sec - 1min x6=6min","speed":"0.00000000000001","forbidden_count":11,"flow_available":FLOW_AVAILABLE,"endpoints":["/generate-video-tayybat","/health"]})

def create_img(text, url, discount, path):
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (640,360), color=(0,100,0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0,0,640,50], fill=(0,0,0))
    draw.text((10,10), f"{text} - {discount} - 1 MIN - 0.00000000000001", fill=(255,255,0))
    draw.text((10,80), url[:60], fill=(255,255,255))
    draw.text((10,150), "Waeldeban186 - طيبات - 11 ممنوع", fill=(255,215,0))
    img.save(path, quality=75, optimize=True)
    return path

def build_ultra(temp_dir, total_minutes):
    from moviepy.editor import ImageClip, concatenate_videoclips
    clips=[]
    keys=list(LINKS_6_DETAILED.keys())
    # 6 clips only - ULTRA FAST
    for i in range(6):
        info=LINKS_6_DETAILED[keys[i]]
        p=os.path.join(temp_dir, f"l_{i}.jpg")
        create_img(info['name'], info['url'], info['discount'], p)
        clip=ImageClip(p).set_duration(60)
        clips.append(clip)
    out=os.path.join(temp_dir, f"ultra_{total_minutes}_0.00000000000001.mp4")
    final=concatenate_videoclips(clips, method="compose")
    # FASTEST SETTINGS: 640x360, 12fps, ultrafast, crf 35, no audio
    final.write_videofile(out, fps=12, codec='libx264', audio=False, preset='ultrafast', threads=4, logger=None, ffmpeg_params=['-crf','35','-vf','scale=640:360'])
    return out

@app.route('/generate-video-tayybat', methods=['POST'])
def gen():
    try:
        data=request.get_json(force=True) if request.is_json else {}
        mins=int(data.get('total_minutes',6))
        temp_dir=tempfile.mkdtemp(prefix="ultra0_")
        out=build_ultra(temp_dir, mins)
        return send_file(out, as_attachment=True, download_name=f"tayybat_{mins}min_ULTRA_0.00000000000001.mp4", mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:1000]}),500

@app.route('/api/video/montage-30', methods=['POST'])
def m30(): return gen()
@app.route('/api/video/montage-60', methods=['POST'])
def m60(): return gen()
@app.route('/api/links')
def links(): return jsonify({"links":LINKS_6_DETAILED,"version":"v138-ULTRA-0.00000000000001","status":"ok"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
