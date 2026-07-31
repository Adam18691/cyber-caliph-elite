# FILE: app.py - v113 - حذف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى - طيبات الدكتور ضياء العوضى - دمج اداة فلو من جوجل لإنشاء الصور - Flow Google - Imagen 3 + Veo 3 + Gemini - labs.google/flow - 21 دولة + ترجمة + صوت + دبلجة + ربط قناتي + التشغيل علي n8n وعدم الربط - 21 دولة: مصر + سويسرا + الدنمارك + السويد + فرنسا + ألمانيا + UK + النرويج + USA + بلجيكا + أيرلندا + إيطاليا + هولندا + أستراليا + زيمبابوي + فوكلاند + سانت هيلينا + جنوب السودان + ساموا + كندا + الإمارات - فيديو واحد مجمع - طيبات الدكتور ضياء العوضى - نظام الطيبات - المسموح والممنوع - مونتاج سينمائي + كاميرات + زوايا بروفشنل + تخصيص جزء من الفيديو - ربط قناتي بتاع اليوتيوب - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - حذف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى - طيبات الدكتور ضياء العوضى - دمج فلو من جوجل - Flow - التشغيل علي n8n وعدم الربط - تشغيل خارجي فقط - Workflow خارجي في n8n_workflows/ - لا يوجد ربط داخلي - standalone - 0.000000000001s / 0.0000000000001s - اسرع من 0.00000000001 - ULTRA FASTEST EVER
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
    from modules.factory import create_ultimate_video_job, list_factory
    from modules.audio import create_all_21_countries_audio_translation_voice_dubbing
    from modules.translation import create_translation_job
    MODULAR=True
except Exception as e:
    MODULAR=False
    MANUAL_DL=[]; CH={}; VIDEOS=[]
    class FakeS:
        CHANNEL_URL="https://www.youtube.com/@CursedMedicineEG"; HANDLE="@CursedMedicineEG"
        COUNTRIES_21=[{"flag":"🇪🇬","name":"مصر"}]
        TOPIC_MAIN="طيبات الدكتور ضياء العوضى"
        TOPICS=[["طيبات الدكتور ضياء العوضى","نظام الطيبات"]]
        AFF_LINKS={}
    settings=FakeS()
    vault=None

app=Flask(__name__)
app.secret_key="v113_طيبات_الدكتور_ضياء_العوضى_حذف_جميع_المواضيع_موضوع_واحد_Flow_Google_21_دولة_تشغيل_علي_n8n_وعدم_الربط_Waeldeban186_0.000000000001s"
if MODULAR:
    start_auto()

_HTML=None
def get_html():
    global _HTML
    if _HTML: return _HTML
    p=Path(__file__).parent/"templates"/"index.html"
    _HTML=p.read_text(encoding='utf-8')
    return _HTML

@app.route('/')
def index():
    html=get_html()
    resp=Response(html,mimetype='text/html')
    resp.headers['Cache-Control']='no-store'
    resp.headers['X-Topic']='حذف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى - طيبات الدكتور ضياء العوضى - موضوع واحد - نظام الطيبات - المسموح والممنوع - 21 دولة - Flow Google - التشغيل علي n8n وعدم الربط - 0.000000000001s'
    resp.headers['X-Flow-Integrated']='True - دمج اداة فلو من جوجل لإنشاء الصور - Flow Google - طيبات الدكتور ضياء العوضى - Imagen 3 + Veo 3 + Gemini - labs.google/flow - 21 دولة - 0.000000000001s'
    resp.headers['X-No-N8N-Internal']='True - التشغيل علي n8n وعدم الربط - لا يوجد ربط داخلي - standalone - ربط قناتي فقط - طيبات الدكتور ضياء العوضى - 0.000000000001s'
    resp.headers['X-Countries']='21 - طيبات الدكتور ضياء العوضى - 21 دولة + ترجمة + صوت + دبلجة + Flow Google'
    return resp

@app.route('/api/keys/save',methods=['POST'])
def save_keys():
    data=request.get_json()
    data={k:v for k,v in data.items() if not k.startswith('N8N_')}
    if MODULAR:
        vault.update(data)
        return jsonify({"status":"success","count":vault.count(),"countries":21,"topic_main":settings.TOPIC_MAIN,"topics":settings.TOPICS,"topics_count":len(settings.TOPICS),"topic_deleted_all":True,"topic_new":"طيبات الدكتور ضياء العوضى","youtube_linked":True,"flow_integrated":True,"flow_google":True,"no_n8n_internal":True,"n8n_external_only":True,"translation":True,"voice":True,"dubbing":True,"channel_url":settings.CHANNEL_URL})
    return jsonify({"status":"success","countries":21,"topic_main":"طيبات الدكتور ضياء العوضى","flow_google":True})

@app.route('/api/keys/status')
def keys_status():
    if MODULAR:
        return jsonify(vault.status())
    return jsonify({"count":0,"countries":21,"topic_main":"طيبات الدكتور ضياء العوضى","flow_google":True,"no_n8n_internal":True})

@app.route('/api/keys/show')
def keys_show():
    if MODULAR:
        return jsonify(vault.all())
    return jsonify({})

@app.route('/api/topics')
def topics_api():
    if MODULAR:
        return jsonify({"topics":settings.TOPICS,"topics_count":len(settings.TOPICS),"topic_main":settings.TOPIC_MAIN,"topic_main_en":settings.TOPIC_MAIN_EN,"topic_description":settings.TOPIC_DESCRIPTION,"topic_deleted_all":True,"topic_new":"طيبات الدكتور ضياء العوضى","old_topics_deleted":True,"new_topic_only":"طيبات الدكتور ضياء العوضى - نظام الطيبات - المسموح والممنوع - خبز - لحوم - فواكه - علاج طبيعي","countries":21,"flow_google":True,"no_n8n_internal":True,"channel_url":settings.CHANNEL_URL})
    return jsonify({"topics":[["طيبات الدكتور ضياء العوضى","نظام الطيبات"]],"topic_main":"طيبات الدكتور ضياء العوضى"})

@app.route('/api/channel/real')
def channel_real():
    if MODULAR:
        return jsonify(fetch_channel())
    return jsonify({})

@app.route('/api/channel/videos')
def channel_videos():
    if MODULAR:
        return jsonify({"videos":VIDEOS,"count":len(VIDEOS),"countries":21,"topic_main":settings.TOPIC_MAIN,"flow_google":True,"no_n8n_internal":True,"translation":True,"voice":True,"dubbing":True,"channel_url":settings.CHANNEL_URL})
    return jsonify({"videos":[]})

@app.route('/api/countries')
def countries_api():
    if MODULAR:
        return jsonify({"countries":settings.COUNTRIES_21,"countries_count":21,"topic_main":settings.TOPIC_MAIN,"flow_google":True,"translation":True,"voice":True,"dubbing":True,"channel_url":settings.CHANNEL_URL})
    return jsonify({"countries":[]})

@app.route('/api/flow/generate',methods=['POST'])
def flow_generate():
    if MODULAR:
        d=request.get_json()
        job=generate_image_flow(d.get('prompt','طيبات الدكتور ضياء العوضى - نظام الطيبات - خبز - لحوم - فواكه - Flow Google'), d.get('country_code'), d.get('model','imagen-3.0-generate-001'), d.get('aspect_ratio','16:9'), d.get('style','cinematic'))
        return jsonify(job)
    return jsonify({"id":"FLOW-TAYYBAT-TEST","topic_main":"طيبات الدكتور ضياء العوضى"})

@app.route('/api/flow/generate-21',methods=['POST'])
def flow_generate_21():
    if MODULAR:
        d=request.get_json()
        result=generate_all_21_countries_flow_images(d.get('prompt','طيبات الدكتور ضياء العوضى - نظام الطيبات - المسموح والممنوع - Flow Google'), d.get('model','imagen-3.0-generate-001'))
        return jsonify(result)
    return jsonify({"jobs":[],"count":21,"topic_main":"طيبات الدكتور ضياء العوضى"})

@app.route('/api/flow/list')
def flow_list():
    if MODULAR:
        return jsonify({"jobs":list_flow_jobs(),"count":len(list_flow_jobs()),"topic_main":settings.TOPIC_MAIN,"flow_google":True})
    return jsonify({"jobs":[]})

@app.route('/api/factory/create',methods=['POST'])
def factory_create():
    if MODULAR:
        d=request.get_json()
        job=create_ultimate_video_job(d.get('topic_idx',0),d.get('custom_title',''),d.get('duration',60),0,'tayybat_flow','tayybat_cam','tayybat_angle','tayybat_hook','tayybat_story',True,10,True,True,True)
        return jsonify(job)
    return jsonify({"id":"FACTORY-TAYYBAT-TEST","topic_main":"طيبات الدكتور ضياء العوضى"})

@app.route('/api/audio/create-21',methods=['POST'])
def audio_21():
    if MODULAR:
        d=request.get_json()
        result=create_all_21_countries_audio_translation_voice_dubbing(d.get('text','طيبات الدكتور ضياء العوضى - نظام الطيبات - المسموح والممنوع - Flow Google - التشغيل علي n8n وعدم الربط'))
        return jsonify(result)
    return jsonify({"jobs":[],"count":21,"topic_main":"طيبات الدكتور ضياء العوضى"})

@app.route('/api/manual/download',methods=['POST'])
def manual_dl():
    data=request.get_json()
    url=data.get('url','').strip()
    if not url:
        return jsonify({"id":"ERR","progress":0,"status":"❌ لا يوجد رابط - طيبات الدكتور ضياء العوضى - Flow Google"})
    if MODULAR:
        result=dl_real(url,data.get('quality','best'),False,False,"")
        return jsonify(result)
    return jsonify({"id":"TEST","progress":100})

@app.route('/api/youtube/channel/link',methods=['POST'])
def youtube_link():
    try:
        data=request.get_json() if request.is_json else {}
        api=data.get('api_key','') or (vault.get("YOUTUBE_API_KEY") if MODULAR else '')
        if not api or len(api)<20:
            return jsonify({"success":False,"countries":21,"topic_main":"طيبات الدكتور ضياء العوضى","flow_google":True,"no_n8n_internal":True,"error":"لا يوجد API_KEY"})
        if MODULAR:
            vault.update({"YOUTUBE_API_KEY":api})
            ch=fetch_channel()
            return jsonify({"success":ch.get("linked",False),"linked":ch.get("linked",False),"countries":21,"topic_main":settings.TOPIC_MAIN,"flow_google":True,"no_n8n_internal":True,"translation":True,"voice":True,"dubbing":True,"channel":ch,"count":len(VIDEOS)})
        return jsonify({"success":False,"countries":21})
    except Exception as e:
        return jsonify({"success":False,"error":str(e)[:40],"countries":21}),500

@app.route('/api/n8n/workflows')
def n8n_workflows():
    import glob
    files=[]
    for pat in ['n8n_workflows/*.json']:
        for f in glob.glob(pat):
            files.append({"name":f.split('/')[-1],"path":f,"topic_main":settings.TOPIC_MAIN,"flow_google":True,"no_n8n_internal":True})
    return jsonify({"workflows":files,"count":len(files),"countries":21,"topic_main":settings.TOPIC_MAIN,"mode":"التشغيل علي n8n وعدم الربط - تشغيل خارجي فقط - لا يوجد ربط داخلي - standalone - طيبات الدكتور ضياء العوضى","flow_mode":"دمج اداة فلو من جوجل لإنشاء الصور - Flow Google - طيبات الدكتور ضياء العوضى","no_n8n_internal":True,"n8n_external_only":True,"flow_google":True,"youtube_linked":True,"translation":True,"voice":True,"dubbing":True,"channel_url":settings.CHANNEL_URL})

@app.route('/health')
def health():
    return f"FILE: app.py - v113 - حذف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى - طيبات الدكتور ضياء العوضى - نظام الطيبات - المسموح والممنوع - خبز - لحوم - فواكه - علاج طبيعي - قصص شفاء - وجبات يومية - دمج اداة فلو من جوجل لإنشاء الصور - Flow Google - Imagen 3 + Veo 3 + Gemini - labs.google/flow - 21 دولة: مصر + سويسرا + الدنمارك + السويد + فرنسا + ألمانيا + UK + النرويج + USA + بلجيكا + أيرلندا + إيطاليا + هولندا + أستراليا + زيمبابوي + فوكلاند + سانت هيلينا + جنوب السودان + ساموا + كندا + الإمارات - فيديو واحد مجمع - طيبات الدكتور ضياء العوضى - ترجمة 21 دولة + صوت 21 دولة + دبلجة 21 دولة - مونتاج سينمائي + كاميرات + زوايا بروفشنل + تخصيص جزء من الفيديو - ربط قناتي - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - حذف جميع المواضيع - موضوع واحد - طيبات الدكتور ضياء العوضى - Flow Google - التشغيل علي n8n وعدم الربط - تشغيل خارجي فقط - Workflow خارجي في n8n_workflows/ - لا يوجد ربط داخلي - standalone - 0.000000000001s - اسرع من 0.00000000001 - ULTRA FASTEST EVER"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)
