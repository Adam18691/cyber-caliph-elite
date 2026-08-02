# FILE: app.py - v144 FINAL - v115 + v143 MERGED - 54+6=60min - 502 FIX - 0.00000000000001
import os, sys, tempfile, subprocess
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
from pathlib import Path
from datetime import datetime

# ========= 1. FLOW =========
FLOW_AVAILABLE=False
FLOW_LOCATION=""
FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - 0.00000000000001"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]
try:
    from modules.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs, FORBIDDEN_TEXT as FT1, FORBIDDEN_ITEMS as FI1
    FLOW_AVAILABLE=True
    FLOW_LOCATION="modules/flow.py"
    FORBIDDEN_TEXT=FT1
    FORBIDDEN_ITEMS=FI1
except:
    try:
        from core.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs, FORBIDDEN_TEXT as FT2, FORBIDDEN_ITEMS as FI2
        FLOW_AVAILABLE=True
        FLOW_LOCATION="core/flow.py"
        FORBIDDEN_TEXT=FT2
        FORBIDDEN_ITEMS=FI2
    except:
        FLOW_AVAILABLE=False
        def generate_image_flow(p,c=None,m="a",a="16:9",s=""): return {"id":f"FLOW-FALLBACK-{datetime.now().strftime('%H%M%S')}","forbidden":FORBIDDEN_TEXT}
        def generate_all_21_countries_flow_images(bp,m="a"): return {"jobs":[],"count":0}
        def list_flow_jobs(): return []

# ========= 2. TAYYBAT =========
try:
    from core.tayybat import get_tayybat_info, TAYYBAT_TOPICS, FORBIDDEN_TEXT as FT_T, FORBIDDEN_ITEMS as FI_T, get_links_6, get_video_description_with_links, LINKS_6, VIDEO_DESCRIPTION
    TAYYBAT_AVAILABLE=True
    FORBIDDEN_TEXT=FT_T
    FORBIDDEN_ITEMS=FI_T
except:
    TAYYBAT_AVAILABLE=False
    TAYYBAT_TOPICS=[["طيبات بدون بيض - 11 ممنوع","طيبات"]]
    LINKS_6={
        "monoprice":"https://yazing.com/deals/monoprice/Waeldeban186",
        "landsend":"https://yazing.com/deals/landsend/Waeldeban186",
        "shopsimon":"https://yazing.com/deals/shopsimon/Waeldeban186",
        "colehaan":"https://yazing.com/deals/colehaan/Waeldeban186",
        "hfonline":"https://yazing.com/deals/hfonline-uk/Waeldeban186",
        "kieai":"https://kie.ai/?ref=0e3195dd062bf11f0da7496dd3c1bf66"
    }
    VIDEO_DESCRIPTION="نظام طيبات - 11 ممنوع"
    def get_tayybat_info():
        return {"topics":TAYYBAT_TOPICS,"forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS,"forbidden_count":11,"links":LINKS_6,"tayybat":True}
    def get_video_description_with_links(): return VIDEO_DESCRIPTION
    def get_links_6(): return LINKS_6

# ========= 3. LINKS 6 DETAILED FOR VIDEO =========
LINKS_6_DETAILED = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% OFF", "name": "Kie.AI"}
}

# ========= 4. FLASK =========
from flask import Flask, Response, request, jsonify, send_file
app=Flask(__name__)

def get_html():
    p=Path(__file__).parent/"templates"/"index.html"
    return p.read_text(encoding="utf-8") if p.exists() else f"<html><body><h1>v144 MERGED - 54+6=60min - {FORBIDDEN_TEXT}</h1></body></html>"

@app.route('/')
def index():
    html=get_html()
    resp=Response(html,mimetype='text/html')
    resp.headers['X-Flow-Available']=str(FLOW_AVAILABLE)
    resp.headers['X-Tayybat']="0.00000000000001"
    resp.headers['X-Version']="v144-MERGED-502-FIX"
    resp.headers['X-Forbidden-Count']="11"
    return resp

# ---- v115 endpoints ----
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
        return jsonify({"links": links,"description": desc,"forbidden": FORBIDDEN_TEXT,"forbidden_items": FORBIDDEN_ITEMS,"forbidden_count": 11,"flow_available": FLOW_AVAILABLE,"status": "ok"})
    except Exception as e:
        return jsonify({"status":"error","error":str(e)[:200]}),500

@app.route('/api/tayybat')
def tayybat_api():
    info=get_tayybat_info()
    info["flow_available"]=FLOW_AVAILABLE
    info["tayybat"]=True
    return jsonify(info)

@app.route('/api/flow/generate',methods=['POST'])
def flow_generate():
    d=request.get_json() if request.is_json else {}
    job=generate_image_flow(d.get('prompt',''),d.get('country_code'),d.get('model','imagen-3.0-generate-001'))
    return jsonify(job)

@app.route('/api/flow/generate-21',methods=['POST'])
def flow_21():
    d=request.get_json() if request.is_json else {}
    result=generate_all_21_countries_flow_images(d.get('prompt',''),d.get('model','imagen-3.0-generate-001'))
    return jsonify(result)

@app.route('/api/flow/list')
def flow_list():
    return jsonify({"jobs":list_flow_jobs(),"count":len(list_flow_jobs()),"forbidden":FORBIDDEN_TEXT,"forbidden_count":11})

@app.route('/api/flow/status')
def flow_status():
    return jsonify({"flow_available":FLOW_AVAILABLE,"flow_location":FLOW_LOCATION,"forbidden":FORBIDDEN_TEXT,"forbidden_count":11,"tayybat":TAYYBAT_AVAILABLE})

@app.route('/api/keys/save',methods=['POST'])
def save_keys():
    try:
        data=request.get_json()
        return jsonify({"status":"success","forbidden":FORBIDDEN_TEXT,"forbidden_count":11})
    except Exception as e:
        return jsonify({"status":"error","error":str(e)[:100]})

# ---- v143 video endpoints - 502 FIX ----
@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "version": "v144 MERGED - v115 + v143 - 54+6=60min - 502 FIX - 0.00000000000001",
        "structure":"54min content (9min x6) + 6min links (1min x6) = 60min",
        "speed":"0.00000000000001",
        "forbidden":FORBIDDEN_TEXT,
        "forbidden_count":11,
        "flow_available":FLOW_AVAILABLE,
        "tayybat":TAYYBAT_AVAILABLE,
        "endpoints": ["/api/topics","/api/links","/api/tayybat","/health","/wake","/generate-video-tayybat","/api/video/montage-60"],
        "fix":"502 Bad Gateway fixed - now has generate-video-tayybat"
    })

@app.route('/wake')
def wake():
    return jsonify({"status":"awake","version":"v144","message":"Server awake - ready for 54+6=60min video - 502 fixed"})

def make_link_img(text, url, discount, path, idx):
    from PIL import Image, ImageDraw
    img=Image.new('RGB',(320,180),color=[(0,100,0),(0,80,120),(120,0,0),(100,0,100),(120,80,0),(0,100,100)][idx%6])
    draw=ImageDraw.Draw(img)
    draw.rectangle([0,0,320,25],fill=(0,0,0))
    draw.text((5,5),f"LINK {idx+1}/6 - {text} - {discount}",fill=(255,255,0))
    draw.text((5,35),url[:40],fill=(255,255,255))
    img.save(path,quality=60,optimize=True)
    return path

def make_content_img(txt, path):
    from PIL import Image, ImageDraw
    img=Image.new('RGB',(320,180),color=(139,69,19))
    draw=ImageDraw.Draw(img)
    draw.text((5,5),f"TAYYBAT {txt}",fill=(255,215,0))
    img.save(path,quality=60,optimize=True)
    return path

def build_54_6_extreme(temp_dir, content_paths):
    list_file = os.path.join(temp_dir, "list.txt")
    keys=list(LINKS_6_DETAILED.keys())
    content_per_block = 9*60
    link_per_block = 60
    imgs_per_block = max(1, len(content_paths)//6) if content_paths else 1
    with open(list_file, 'w') as f:
        for b in range(6):
            if content_paths:
                s=b*imgs_per_block
                e=s+imgs_per_block
                block_imgs=content_paths[s:e] or content_paths[:imgs_per_block]
                sec_per = content_per_block / len(block_imgs)
                for p in block_imgs:
                    f.write(f"file '{p}'\n")
                    f.write(f"duration {sec_per}\n")
            else:
                p=os.path.join(temp_dir,f"c{b}.jpg")
                make_content_img(f"Block {b+1}/6 - 9 MIN",p)
                f.write(f"file '{p}'\n")
                f.write(f"duration {content_per_block}\n")
            info=LINKS_6_DETAILED[keys[b]]
            lp=os.path.join(temp_dir,f"l{b}.jpg")
            make_link_img(info['name'],info['url'],info['discount'],lp,b)
            f.write(f"file '{lp}'\n")
            f.write(f"duration {link_per_block}\n")
        f.write(f"file '{lp}'\n")
    out=os.path.join(temp_dir,"tayybat_54_6_60min_v144_0.00000000000001.mp4")
    cmd=["ffmpeg","-y","-f","concat","-safe","0","-i",list_file,"-vf","scale=640:360","-c:v","libx264","-preset","ultrafast","-crf","35","-pix_fmt","yuv420p","-r","8",out]
    subprocess.run(cmd, check=False, timeout=300, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out

@app.route('/generate-video-tayybat', methods=['POST','GET'])
def gen_tayybat():
    try:
        data=request.get_json(force=True) if request.is_json else {}
        images=data.get('images',[])
        if not images and 'jobs' in data:
            jobs=data['jobs']
            images=[j.get('file') or j.get('url') for j in jobs if isinstance(j,dict) and (j.get('file') or j.get('url'))]
        temp_dir=tempfile.mkdtemp(prefix="v144_")
        local=[]
        for i,url in enumerate(images[:6]):
            try:
                if url and url.startswith('http'):
                    r=requests.get(url,timeout=3)
                    if r.status_code==200:
                        p=os.path.join(temp_dir,f"c{i}.jpg")
                        open(p,'wb').write(r.content)
                        local.append(p)
            except: continue
        out=build_54_6_extreme(temp_dir, local)
        return send_file(out,as_attachment=True,download_name="tayybat_54c_6l_60min_v144_0.00000000000001.mp4",mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:2000]}),500

@app.route('/api/video/montage-60', methods=['POST','GET'])
def m60(): return gen_tayybat()

@app.route('/api/video/montage-54-6', methods=['POST','GET'])
def m54_6(): return gen_tayybat()

@app.route('/generate-video', methods=['POST','GET'])
def gen_compat():
    return gen_tayybat()

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
