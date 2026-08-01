# FILE: app.py - v115 FINAL FIX - حل مشكلة /api/links + ازالة العربي من الهيدر
import os, sys
from pathlib import Path
sys.dont_write_bytecode=True

# ========= 1. حل مشكلة Flow =========
FLOW_AVAILABLE=False
FLOW_LOCATION=""
FORBIDDEN_TEXT="بيض ممنوع - 11 ممنوع - بيض ممنوع - طيبات الدكتور ضياء العوضي"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]

try:
    # الهيكل الجديد modules/flow.py
    from modules.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs, FORBIDDEN_TEXT as FT1, FORBIDDEN_ITEMS as FI1
    FLOW_AVAILABLE=True
    FLOW_LOCATION="modules/flow.py - الهيكل الجديد - موجود"
    FORBIDDEN_TEXT=FT1
    FORBIDDEN_ITEMS=FI1
except Exception as e1:
    try:
        # الهيكل القديم مع GitHub الحالي - core/flow.py
        from core.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs, FORBIDDEN_TEXT as FT2, FORBIDDEN_ITEMS as FI2
        FLOW_AVAILABLE=True
        FLOW_LOCATION="core/flow.py - حل مشكلة GitHub يناسب مع هيكل core/ - موجود"
        FORBIDDEN_TEXT=FT2
        FORBIDDEN_ITEMS=FI2
    except Exception as e2:
        # fallback - لكن طيبات موجود - بدون flow
        FLOW_AVAILABLE=False
        FLOW_LOCATION=f"core/flow.py + modules/flow.py غير موجود - GitHub الى الاصلي - core/flow.py غير موجود - فيل موجود - غرق{(str(e1)[:50])}-{(str(e2)[:50])}"
        def generate_image_flow(prompt, country_code=None, model="imagen-3.0-generate-001", aspect_ratio="16:9", style=""):
            from datetime import datetime
            return {"id":f"FLOW-FALLBACK-NO-EGGS-{datetime.now().strftime('%H%M%S')}-v115-COMPLETE","prompt":prompt[:50],"forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS}
        def generate_all_21_countries_flow_images(base_prompt, model="imagen-3.0-generate-001"):
            return {"jobs":[],"count":0,"forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS,"forbidden_count":11}
        def list_flow_jobs():
            return []

# ========= 2. طيبات - core/tayybat.py =========
try:
    from core.tayybat import get_tayybat_info, TAYYBAT_TOPICS, FORBIDDEN_TEXT as FT_T, FORBIDDEN_ITEMS as FI_T, get_links_6, get_video_description_with_links, LINKS_6, VIDEO_DESCRIPTION
    TAYYBAT_AVAILABLE=True
    FORBIDDEN_TEXT=FT_T
    FORBIDDEN_ITEMS=FI_T
except Exception as e_tayybat:
    TAYYBAT_AVAILABLE=False
    TAYYBAT_TOPICS=[
        ["دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع - طيبات الدكتور ضياء العوضي","طيبات الدكتور ضياء العوضي - بدون بيض"],
        ["ارز - بطاطس - قشطة - فواكه - بدون بيض","المسموحات - طيبات - بدون بيض"],
        ["لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع - طيبات - الممنوعات 11","ال 11 ممنوع - طيبات - 11 ممنوع"],
    ]
    LINKS_6={
        "monoprice":"https://yazing.com/deals/monoprice/Waeldeban186",
        "landsend":"https://yazing.com/deals/landsend/Waeldeban186",
        "shopsimon":"https://yazing.com/deals/shopsimon/Waeldeban186",
        "colehaan":"https://yazing.com/deals/colehaan/Waeldeban186",
        "hfonline":"https://yazing.com/deals/hfonline-uk/Waeldeban186",
        "kieai":"https://kie.ai/?ref=0e3195d062bf11f0da7496d3c1bf66"
    }
    VIDEO_DESCRIPTION="نظام طيبات الدكتور ضياء العوضي - بيض 11 ممنوع"
    def get_tayybat_info():
        return {"topics":TAYYBAT_TOPICS,"forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS,"forbidden_count":11,"no_eggs":True,"links":LINKS_6,"tayybat":True}
    def get_video_description_with_links():
        return VIDEO_DESCRIPTION
    def get_links_6():
        return LINKS_6

# ========= 3. Flask App =========
from flask import Flask, Response, request, jsonify
app=Flask(__name__)
app.secret_key="v115 - طيبات بدون بيض - حل مشكلة core_flow.py غير موجود الان موجود modules_flow.py الممنوعات بيض ممنوع طيبات حل مشكلة v115"

def get_html():
    p=Path(__file__).parent/"templates"/"index.html"
    return p.read_text(encoding="utf-8") if p.exists() else f"<html><body><h1>v115 - طيبات بدون بيض - {FORBIDDEN_TEXT} - flow_available={FLOW_AVAILABLE}</h1></body></html>"

@app.route('/')
def index():
    html=get_html()
    resp=Response(html,mimetype='text/html')
    # FIX: ممنوع عربي في الهيدر - استخدم انجليزي فقط عشان Render / gunicorn ما يقعش
    resp.headers['X-Flow-Location']=FLOW_LOCATION.encode('ascii','ignore').decode()[:100] if FLOW_LOCATION else "unknown"
    resp.headers['X-Flow-Available']=str(FLOW_AVAILABLE)
    resp.headers['X-Forbidden-Count']="11"
    resp.headers['X-Tayybat']="0.0000000001"
    resp.headers['X-Version']="v115-FIXED"
    return resp

@app.route('/api/topics')
def topics_api():
    info=get_tayybat_info()
    info["flow_available"]=FLOW_AVAILABLE
    info["flow_location"]=FLOW_LOCATION
    info["flow_fix"]="مشكلة modules/flow.py غير موجود + core/flow.py غير موجود - الان الملف موجود في core/flow.py حل مشكلة v115"
    return jsonify(info)

# ========= NEW FIX: مسار /api/links اللي كان ناقص =========
@app.route('/api/links')
def links_api():
    try:
        links = get_links_6()
        desc = get_video_description_with_links()
        info = get_tayybat_info()
        return jsonify({
            "links": links,
            "description": desc,
            "video_description": desc,
            "topics": info.get("topics", []),
            "forbidden": FORBIDDEN_TEXT,
            "forbidden_items": FORBIDDEN_ITEMS,
            "forbidden_count": 11,
            "no_eggs": True,
            "flow_available": FLOW_AVAILABLE,
            "flow_location": FLOW_LOCATION,
            "status": "ok"
        })
    except Exception as e:
        return jsonify({"status":"error","error":str(e)[:200],"links":LINKS_6,"forbidden":FORBIDDEN_TEXT}), 500

@app.route('/api/tayybat')
def tayybat_api():
    try:
        info=get_tayybat_info()
        info["flow_available"]=FLOW_AVAILABLE
        info["flow_location"]=FLOW_LOCATION
        info["tayybat"]=True
        info["no_eggs"]=True
        return jsonify(info)
    except Exception as e:
        return jsonify({"error":str(e),"forbidden":FORBIDDEN_TEXT}), 500

@app.route('/api/flow/generate',methods=['POST'])
def flow_generate():
    d=request.get_json() if request.is_json else {}
    prompt=d.get('prompt','خير قمح كامل - لحم - جمبري - فواكه - المسموحات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة + بيض - بدون بيض')
    job=generate_image_flow(prompt,d.get('country_code'),d.get('model','imagen-3.0-generate-001'))
    job["flow_location"]=FLOW_LOCATION
    job["flow_available"]=FLOW_AVAILABLE
    return jsonify(job)

@app.route('/api/flow/generate-21',methods=['POST'])
def flow_21():
    d=request.get_json() if request.is_json else {}
    result=generate_all_21_countries_flow_images(d.get('prompt','دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض - 21 دولة'),d.get('model','imagen-3.0-generate-001'))
    result["flow_location"]=FLOW_LOCATION
    result["flow_available"]=FLOW_AVAILABLE
    return jsonify(result)

@app.route('/api/flow/list')
def flow_list():
    return jsonify({"jobs":list_flow_jobs(),"count":len(list_flow_jobs()),"forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS,"forbidden_count":11,"no_eggs":True})

@app.route('/api/flow/status')
def flow_status():
    return jsonify({
        "flow_available":FLOW_AVAILABLE,
        "flow_location":FLOW_LOCATION,
        "flow_fix":"مشكلة modules/flow.py غير موجود + core/flow.py غير موجود - الان الملف موجود - حل مشكلة v115",
        "forbidden":FORBIDDEN_TEXT,
        "forbidden_items":FORBIDDEN_ITEMS,
        "forbidden_count":11,
        "no_eggs":True,
        "eggs_forbidden":True,
        "single_topic":True,
        "single_topic_name":"طيبات الدكتور ضياء العوضي",
        "tayybat":True,
        "github_structure":"GitHub الحالي - فقط modules/ - لا يوجد index.html في /templates فيه 5 ملفات - core/ - الحالي GitHub - الحل: اضمنا core/modules + core/tayybat.py",
        "files_exist":{
            "core/flow.py": (Path(__file__).parent/"core"/"flow.py").exists(),
            "modules/flow.py": (Path(__file__).parent/"modules"/"flow.py").exists(),
            "core/tayybat.py": (Path(__file__).parent/"core"/"tayybat.py").exists(),
            "core/vault.py": (Path(__file__).parent/"core"/"vault.py").exists(),
            "config/settings.py": (Path(__file__).parent/"config"/"settings.py").exists(),
        }
    })

@app.route('/api/keys/save',methods=['POST'])
def save_keys():
    try:
        data=request.get_json()
        data={k:v for k,v in data.items() if not k.startswith('N8N_')}
        return jsonify({"status":"success","forbidden":FORBIDDEN_TEXT,"forbidden_items":FORBIDDEN_ITEMS,"forbidden_count":11})
    except Exception as e:
        return jsonify({"status":"error","error":str(e)[:100],"forbidden":FORBIDDEN_TEXT})

@app.route('/health')
def health():
    return jsonify({
        "status": "ok",
        "version": "v115-FIXED",
        "message": "طيبات بدون بيض - 11 ممنوع - بيض ممنوع - بيض ممنوع واحد - موضوع ضياء العوضي - حذف جميع الموانع - v115",
        "forbidden": FORBIDDEN_TEXT,
        "forbidden_items": FORBIDDEN_ITEMS,
        "forbidden_count": 11,
        "flow_available": FLOW_AVAILABLE,
        "flow_location": FLOW_LOCATION,
        "tayybat": TAYYBAT_AVAILABLE,
        "links": LINKS_6,
        "endpoints": ["/api/topics","/api/links","/api/tayybat","/api/flow/status","/api/flow/generate","/health"]
        from flask import request, send_file
import os, tempfile, requests
from moviepy.editor import ImageSequenceClip

@app.route('/generate-video-tayybat', methods=['POST'])
def generate_video_tayybat():
    data = request.json
    images = data.get('images', [])  # لستة لينكات الصور
    title = data.get('title', 'طيبات بدون بيض')
    
    # نزّل الصور مؤقتا
    temp_dir = tempfile.mkdtemp()
    local_images = []
    for i, url in enumerate(images[:21]): # 21 صورة
        r = requests.get(url)
        path = os.path.join(temp_dir, f"{i}.jpg")
        open(path, 'wb').write(r.content)
        local_images.append(path)
    
    # اعمل الفيديو 6 دقايق = 21 صورة * ~17 ثانية للصورة
    clip = ImageSequenceClip(local_images, fps=1/17)
    output_path = os.path.join(temp_dir, "output.mp4")
    clip.write_videofile(output_path, fps=24)
    
    return send_file(output_path, as_attachment=True)
    })

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
