# FILE: app.py - v115 - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - طيبات الدكتور ضياء العوضى - حذف جميع المواضيع - موضوع واحد - Flow Google - 21 دولة - التشغيل علي n8n وعدم الربط - 0.000000000001s
import os, sys
from pathlib import Path
from flask import Flask, Response, request, jsonify
sys.dont_write_bytecode=True
try:
    from config.settings import settings
    from core.vault import vault
    from core.channel import CH, VIDEOS, fetch_channel, start_auto
    from core.downloader import MANUAL_DL, dl_real
    from modules.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
    from modules.factory import create_ultimate_video_job
    from modules.audio import create_all_21_countries_audio_translation_voice_dubbing
    MODULAR=True
except:
    MODULAR=False
    MANUAL_DL=[]; CH={}; VIDEOS=[]
    class FakeS:
        CHANNEL_URL="https://www.youtube.com/@CursedMedicineEG"
        FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض"
        FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]
    settings=FakeS(); vault=None

app=Flask(__name__)
app.secret_key="v115_الممنوعات_دجاج_لبن_زبادي_خضار_بقوليات_فول_عدس_حمص_شاي_قهوة_بيض_طيبات_الدكتور_ضياء_العوضى"
if MODULAR:
    try: start_auto()
    except: pass

def get_html():
    p=Path(__file__).parent/"templates"/"index.html"
    return p.read_text(encoding='utf-8') if p.exists() else "<h1>v115 - طيبات - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض</h1>"

@app.route('/')
def index():
    resp=Response(get_html(),mimetype='text/html')
    resp.headers['X-Forbidden']="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - طيبات الدكتور ضياء العوضى - 11 ممنوع - بيض ممنوع"
    resp.headers['X-Single-Topic']="طيبات الدكتور ضياء العوضى - موضوع واحد - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض - 0.000000000001s"
    return resp

@app.route('/api/keys/save',methods=['POST'])
def save_keys():
    data=request.get_json()
    data={k:v for k,v in data.items() if not k.startswith('N8N_')}
    if MODULAR:
        vault.update(data)
        return jsonify({"status":"success","count":vault.count(),"forbidden":settings.FORBIDDEN_TEXT,"forbidden_items":settings.FORBIDDEN_ITEMS,"forbidden_count":len(settings.FORBIDDEN_ITEMS),"single_topic":True,"tayybat":True,"no_eggs":True,"eggs_forbidden":True})
    return jsonify({"status":"success","forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/topics')
def topics_api():
    if MODULAR:
        return jsonify({"topics":settings.TAYYBAT_TOPICS,"forbidden":settings.FORBIDDEN_TEXT,"forbidden_items":settings.FORBIDDEN_ITEMS,"forbidden_count":len(settings.FORBIDDEN_ITEMS),"allowed":settings.ALLOWED_TEXT,"single_topic":True,"tayybat":True,"no_eggs":True,"eggs_forbidden":True,"channel_url":settings.CHANNEL_URL})
    return jsonify({"forbidden":settings.FORBIDDEN_TEXT,"forbidden_items":settings.FORBIDDEN_ITEMS})

@app.route('/api/flow/generate',methods=['POST'])
def flow_gen():
    if MODULAR:
        d=request.get_json()
        job=generate_image_flow(d.get('prompt','طيبات بدون بيض - خبز قمح كامل - لحوم - فواكه - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض'),d.get('country_code'),d.get('model','imagen-3.0-generate-001'))
        return jsonify(job)
    return jsonify({"id":"FLOW-TAYYBAT-NO-EGGS","forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/flow/generate-21',methods=['POST'])
def flow_21():
    if MODULAR:
        d=request.get_json()
        result=generate_all_21_countries_flow_images(d.get('prompt','طيبات بدون بيض - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض - 21 دولة'),d.get('model','imagen-3.0-generate-001'))
        return jsonify(result)
    return jsonify({"jobs":[],"count":21,"forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/factory/create',methods=['POST'])
def factory_create():
    if MODULAR:
        d=request.get_json()
        job=create_ultimate_video_job(0,d.get('custom_title','طيبات بدون بيض - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض'),d.get('duration',60),0,'flow_google','flow_cam','flow_angle','flow_hook','flow_story',True,10,True,True,True)
        return jsonify(job)
    return jsonify({"id":"FACTORY-TAYYBAT-NO-EGGS","forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/audio/create-21',methods=['POST'])
def audio_21():
    if MODULAR:
        d=request.get_json()
        result=create_all_21_countries_audio_translation_voice_dubbing(d.get('text','طيبات بدون بيض - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض'))
        return jsonify(result)
    return jsonify({"jobs":[],"count":21,"forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/keys/status')
def keys_status():
    if MODULAR: return jsonify(vault.status())
    return jsonify({"forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/keys/show')
def keys_show():
    if MODULAR: return jsonify(vault.all())
    return jsonify({"forbidden":settings.FORBIDDEN_TEXT})

@app.route('/api/channel/real')
def channel_real():
    if MODULAR:
        try: return jsonify(fetch_channel())
        except: return jsonify({"status":"v115 - طيبات - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض"})
    return jsonify({"forbidden":settings.FORBIDDEN_TEXT})

@app.route('/health')
def health():
    return f"v115 - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - طيبات الدكتور ضياء العوضى - موضوع واحد - حذف جميع المواضيع - Flow Google - 21 دولة - التشغيل علي n8n وعدم الربط - بيض ممنوع - لا يوجد بيض - 11 ممنوع - 0.000000000001s"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
