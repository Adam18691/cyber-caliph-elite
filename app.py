# FILE: app.py - v139 FIX ARABIC + 60min REAL - 0.00000000000001 ULTRA
import os, sys, tempfile
sys.dont_write_bytecode=True
try:
    from PIL import Image
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.LANCZOS
    import PIL.Image
    if not hasattr(PIL.Image, 'ANTIALIAS'):
        PIL.Image.ANTIALIAS = PIL.Image.LANCZOS
except: pass

LINKS_6_DETAILED = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% OFF", "name": "Kie.AI"}
}

from flask import Flask, Response, request, jsonify, send_file
app=Flask(__name__)

@app.route('/')
def index():
    resp=Response("<h1>v139 FIX ARABIC - 60min REAL - 0.00000000000001</h1>",mimetype='text/html')
    resp.headers['X-Tayybat']="0.00000000000001"
    resp.headers['X-Version']="v139-FIX-ARABIC-60MIN"
    return resp

@app.route('/health')
def health():
    return jsonify({"status":"ok","version":"v139 - FIX ARABIC + 60min REAL - 0.00000000000001","speed":"0.00000000000001","forbidden_count":11,"endpoints":["/generate-video-tayybat","/health"]})

def create_img_fixed(text, url, discount, path, duration_sec):
    # FIX ARABIC BOXES: use English only + better design, no arabic font needed
    from PIL import Image, ImageDraw
    # better colors - not just green
    colors = [(0,100,0),(0,80,120),(120,0,0),(100,0,100),(120,80,0),(0,100,100)]
    idx = hash(text) % len(colors)
    bg = colors[idx]
    img = Image.new('RGB', (1280,720), color=bg)
    draw = ImageDraw.Draw(img)
    # top bar
    draw.rectangle([0,0,1280,100], fill=(0,0,0))
    draw.rectangle([0,100,1280,110], fill=(255,215,0))
    # English only - no arabic boxes
    draw.text((30,25), f"{text} - {discount} - {duration_sec//60} MIN - 0.00000000000001", fill=(255,255,0))
    # URL big
    draw.text((30,180), url, fill=(255,255,255))
    # info english
    draw.text((30,280), "Waeldeban186 - Tayybat - 11 FORBIDDEN - NO EGGS", fill=(255,215,0))
    draw.text((30,330), "Allowed: Bread Rice Potato Meat Fish Butter Fruits", fill=(200,255,200))
    draw.text((30,380), "Forbidden: Chicken Milk Yogurt Veg Legumes Tea Coffee + EGGS", fill=(255,180,180))
    # bottom
    draw.rectangle([0,620,1280,720], fill=(0,0,0))
    draw.text((30,640), f"6 LINKS x {duration_sec//60} MIN = {6*duration_sec//60} MIN TOTAL - v139", fill=(255,255,255))
    draw.text((30,670), "youtube.com/@CursedMedicineEG - #Tayybat", fill=(255,215,0))
    img.save(path, quality=85, optimize=True)
    return path

def build_ultra_fixed(temp_dir, total_minutes):
    from moviepy.editor import ImageClip, concatenate_videoclips
    clips=[]
    keys=list(LINKS_6_DETAILED.keys())
    # FIX 60min: each clip duration = total_minutes * 60 / 6
    duration_per_link = (total_minutes * 60) // 6  # 6min=60sec, 30min=300sec, 60min=600sec
    for i in range(6):
        info=LINKS_6_DETAILED[keys[i]]
        p=os.path.join(temp_dir,f"l_{i}.jpg")
        create_img_fixed(info['name'], info['url'], info['discount'], p, duration_per_link)
        clip=ImageClip(p).set_duration(duration_per_link)
        clips.append(clip)
    out=os.path.join(temp_dir,f"tayybat_{total_minutes}min_v139_FIXED_0.00000000000001.mp4")
    final=concatenate_videoclips(clips,method="compose")
    # ULTRA FAST still: 1280x720, 15fps, ultrafast, crf 28 - better quality than 35
    final.write_videofile(out,fps=15,codec='libx264',audio=False,preset='ultrafast',threads=4,logger=None,ffmpeg_params=['-crf','28'])
    return out

@app.route('/generate-video-tayybat', methods=['POST'])
def gen():
    try:
        data=request.get_json(force=True) if request.is_json else {}
        mins=int(data.get('total_minutes',6))
        if mins not in [6,30,60]: mins=6
        temp_dir=tempfile.mkdtemp(prefix="v139_")
        out=build_ultra_fixed(temp_dir, mins)
        return send_file(out,as_attachment=True,download_name=f"tayybat_{mins}min_v139_FIXED_0.00000000000001.mp4",mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:1000]}),500

@app.route('/api/video/montage-60', methods=['POST'])
def m60(): return gen()

@app.route('/api/links')
def links(): return jsonify({"links":LINKS_6_DETAILED,"version":"v139-FIX-ARABIC","status":"ok"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
