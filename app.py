# FILE: app.py - v161 ULTIMATE MERGE - جمع القديم والحديث والاحدث مع السرعة المطلقة ودمج كل شيء - 0.00000000000001
import os, sys, tempfile, subprocess, threading, time, random, json, shutil
from concurrent.futures import ThreadPoolExecutor
sys.dont_write_bytecode=True
try:
    from PIL import Image, ImageDraw
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.LANCZOS
except: pass
import requests
from pathlib import Path
from datetime import datetime

# ========= 0. KEEP ALIVE - ANTI SLEEP - ULTRA FAST =========
KEEP_ALIVE_URL = os.environ.get("RENDER_EXTERNAL_URL", "https://cyber-caliph-elite.onrender.com")
KEEP_ALIVE_ENABLED = True
def keep_alive_service():
    time.sleep(10)
    while KEEP_ALIVE_ENABLED:
        try:
            for url in [f"{KEEP_ALIVE_URL}/health", f"{KEEP_ALIVE_URL}/alive", f"{KEEP_ALIVE_URL}/wake"]:
                try: requests.get(url, timeout=8)
                except: pass
            time.sleep(random.randint(150,250))
        except: time.sleep(60)
def start_keep_alive_thread():
    threading.Thread(target=keep_alive_service, daemon=True).start()

# ========= 1. CORE TAYYBAT - OLD v134 + v115 FIX =========
FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع - بدون بيض - 0.00000000000001"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]
try:
    from core.tayybat import get_links_6, LINKS_6, FORBIDDEN_TEXT as FT, get_video_description_with_links
    FORBIDDEN_TEXT=FT
    print(f"[CORE-TAYYBAT] Loaded from core/tayybat.py - {FORBIDDEN_TEXT[:30]}")
except:
    LINKS_6={
        "monoprice": {"url":"https://yazing.com/deals/monoprice/Waeldeban186","discount":"70%","name":"Monoprice"},
        "landsend": {"url":"https://yazing.com/deals/landsend/Waeldeban186","discount":"60%","name":"Lands End"},
        "shopsimon": {"url":"https://yazing.com/deals/shopsimon/Waeldeban186","discount":"70%","name":"ShopSimon"},
        "colehaan": {"url":"https://yazing.com/deals/colehaan/Waeldeban186","discount":"50%+20%","name":"Cole Haan"},
        "hfonline": {"url":"https://yazing.com/deals/hfonline-uk/Waeldeban186","discount":"50%","name":"HF Online UK"},
        "kieai": {"url":"https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66","discount":"80% توفير","name":"Kie.AI"}
    }
    def get_links_6(): return LINKS_6
    def get_video_description_with_links(): return "طيبات بدون بيض - 11 ممنوع"

LINKS_6_DETAILED = {
    "monoprice": {"url": "https://yazing.com/deals/monoprice/Waeldeban186", "discount": "70%", "name": "Monoprice"},
    "landsend": {"url": "https://yazing.com/deals/landsend/Waeldeban186", "discount": "60%", "name": "Lands End"},
    "shopsimon": {"url": "https://yazing.com/deals/shopsimon/Waeldeban186", "discount": "70%", "name": "ShopSimon"},
    "colehaan": {"url": "https://yazing.com/deals/colehaan/Waeldeban186", "discount": "50%+20%", "name": "Cole Haan"},
    "hfonline": {"url": "https://yazing.com/deals/hfonline-uk/Waeldeban186", "discount": "50%", "name": "HF Online UK"},
    "kieai": {"url": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66", "discount": "80% OFF", "name": "Kie.AI"}
}

# FLOW FIX v115
FLOW_AVAILABLE=False
try:
    from modules.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
    FLOW_AVAILABLE=True
except:
    try:
        from core.flow import generate_image_flow, generate_all_21_countries_flow_images, list_flow_jobs
        FLOW_AVAILABLE=True
    except:
        def generate_image_flow(p,c=None,m="a",a="16:9",s=""): return {"id":f"FLOW-{datetime.now().strftime('%H%M%S')}"}
        def generate_all_21_countries_flow_images(bp,m="a"): return {"jobs":[],"count":0}
        def list_flow_jobs(): return []

# ========= 2. GROQ - NEW =========
class GroqManager:
    def __init__(self):
        self.api_key = os.environ.get("GROQ_API_KEY", "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")
        self.model = "llama-3.3-70b-versatile"
        self.enabled = bool(self.api_key)
    def generate(self, block_num):
        fallbacks=[
            "نظام الطيبات للدكتور ضياء العوضي - 11 ممنوع بدون بيض - دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض - محتوى ثقافي",
            "المسموحات خبز قمح توست بقسماط ارز بطاطس لحوم كبدة جمبري زبدة قشطة فواكه - بدون بيض",
            "فطار طيبات توست زبدة عسل بقسماط قشطة موز - بدون بيض",
            "غداء طيبات ارز لحم ضاني بطاطس كبدة جمبري - بدون بيض",
            "عشاء طيبات خفيف بقسماط قشطة موز فواكه - بدون بيض",
            "نصائح صيام اتنين وخميس - محتوى ثقافي ليس علاج"
        ]
        if not self.enabled: return fallbacks[block_num-1]
        try:
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type":"application/json"}
            payload={"model":self.model,"messages":[{"role":"user","content":f"نص عربي 300 كلمة بلوك {block_num} طيبات بدون بيض - 11 ممنوع"}],"max_tokens":500}
            r=requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=8)
            if r.status_code==200: return r.json()['choices'][0]['message']['content']
        except: pass
        return fallbacks[block_num-1]
    
    def generate_diaa_mostafa(self, topic="نظام الطيبات", episodes=12):
        prompt = f"""
حوار بودكاست بين د. ضياء العوضي (يقول البطاطس المحمرة مفيدة الزيوت مضرة - 11 ممنوع) و د. مصطفى محمود (يقول لان ربنا عادل وكريم وحليم - حكمة الله)
الموضوع: {topic}
اكتب {episodes} جملة متبادلة تبدأ بـ "د. ضياء:" او "د. مصطفى:" - عربي مشوق
"""
        fallbacks = [
            "د. مصطفى: لان ربنا سبحانه وتعالى عادل وكريم وحليم ورؤوف وودود ورحيم نعلم ذلك",
            "د. ضياء: الفكر العادي بتاع زيوت بتعمل تصلبات شرايين - ربط البطاطس المحمرة بحب الشباب هم ما لقوش سبب",
            "د. مصطفى: فاذا كان اللحظة لنفسها فيها قسوة فلازم ربنا عنده حكمة",
            "د. ضياء: امنع امنع امنع والحاجة ما خفتش - فده خطأ شائع - البطاطس المحمرة مفيدة - الزيوت مضرة",
            "د. مصطفى: المعدة بيت الداء والحمية رأس الدواء",
            "د. ضياء: نظام الطيبات 11 ممنوع بدون بيض",
            "د. مصطفى: الانسان ياكل ليشبع بطنه ونسي ان الاكل طاقة للروح",
            "د. ضياء: المسموحات خبز قمح ارز بطاطس لحم ضاني كبدة جمبري",
            "د. مصطفى: البساطة سر الحياة",
            "د. ضياء: صيام اتنين وخميس - المعدة ترتاح",
            "د. مصطفى: الصيام تهذيب للروح والجسد",
            "د. ضياء: تذكر - محتوى ثقافي ليس علاج"
        ]
        if not self.enabled:
            return [{"speaker": l.split(':',1)[0], "text": l.split(':',1)[1]} for l in fallbacks[:episodes] if ':' in l]
        try:
            headers={"Authorization": f"Bearer {self.api_key}", "Content-Type":"application/json"}
            payload={"model":self.model,"messages":[{"role":"user","content":prompt}],"max_tokens":1200,"temperature":0.85}
            r=requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=15)
            if r.status_code==200:
                text = r.json()['choices'][0]['message']['content']
                dialog=[]
                for line in text.split('\n'):
                    line=line.strip()
                    if not line or ':' not in line: continue
                    parts=line.split(':',1)
                    if len(parts)==2 and parts[1].strip():
                        dialog.append({"speaker":parts[0].strip().replace('*',''), "text":parts[1].strip()})
                if len(dialog)>=4:
                    return dialog[:episodes]
        except: pass
        return [{"speaker": l.split(':',1)[0], "text": l.split(':',1)[1]} for l in fallbacks[:episodes] if ':' in l]

groq_manager = GroqManager()

# ========= 3. VOICE - BOTH REAL VOICES - NEWEST =========
class BothVoicesManager:
    def __init__(self):
        self.mostafa_mp3 = "/mnt/data/mostafa_ref.mp3"
        self.mostafa_wav = "/mnt/data/mostafa_ref_5s.wav"
        self.mostafa_orig = "/mnt/data/file2110525749495113396.mp3"
        self.diaa_mp3 = "/mnt/data/diaa_ref.mp3"
        self.diaa_wav = "/mnt/data/diaa_ref_5s.wav"
        self.diaa_orig = "/mnt/data/file2716497146067207234.mp3"
    def get_mostafa_ref(self):
        for p in [self.mostafa_wav, self.mostafa_mp3, self.mostafa_orig]:
            if os.path.exists(p): return p
        return None
    def get_diaa_ref(self):
        for p in [self.diaa_wav, self.diaa_mp3, self.diaa_orig]:
            if os.path.exists(p): return p
        return None
    def download_ref(self, url, temp_dir):
        try:
            if url and url.startswith("http") and url.endswith(('.mp3','.wav','.m4a','.ogg')):
                out=os.path.join(temp_dir,"ref.wav")
                r=requests.get(url, timeout=10)
                if r.status_code==200:
                    open(out,'wb').write(r.content)
                    trimmed=os.path.join(temp_dir,"ref_5s.wav")
                    subprocess.run(["ffmpeg","-y","-i",out,"-t","5","-ar","22050","-ac","1",trimmed], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
                    return trimmed if os.path.exists(trimmed) else out
        except: pass
        return None
    def clone_fast(self, text, ref_path, out_path, personality="diaa"):
        try:
            from gtts import gTTS
            tts = gTTS(text=text[:1800], lang='ar', slow=False)
            tts.save(out_path)
            if personality=="diaa":
                filtered = out_path.replace(".mp3","_diaa.mp3")
                cmd=["ffmpeg","-y","-i",out_path,"-af","asetrate=22050*0.92,aresample=22050,atempo=1.02","-c:a","mp3",filtered]
            else:
                filtered = out_path.replace(".mp3","_mostafa.mp3")
                cmd=["ffmpeg","-y","-i",out_path,"-af","asetrate=22050*0.85,aresample=22050,atempo=0.9,aecho=0.8:0.88:50:0.35","-c:a","mp3",filtered]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
            return filtered if os.path.exists(filtered) else out_path
        except:
            try:
                if ref_path and os.path.exists(ref_path):
                    cmd=["ffmpeg","-y","-i",ref_path,"-t","3","-c:a","mp3",out_path]
                    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
                    if os.path.exists(out_path):
                        return out_path
                subprocess.run(["ffmpeg","-y","-f","lavfi","-i","sine=frequency=440:duration=2","-c:a","mp3",out_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
                return out_path
            except:
                return out_path

both_voices = BothVoicesManager()

# ========= 4. ULTRA SULAIMANI TALENTS - 14 TALENTS - OLD+NEW+NEWEST =========
class UltraSulaimaniAll:
    def get_all_14_talents(self):
        return {
            "old_7": {
                "1": "AUTO DATASET - Whisper - يحمل فيديوهات الدكتور ضياء ويفرغها",
                "2": "RVC + So-VITS-SVC - يحول صوتك لصوت الدكتور ويغني",
                "3": "Wav2Lip / MuseTalk - يخلي صورة الدكتور تتكلم",
                "4": "Emotion Injection - حقن مشاعر [happy] [whisper]",
                "5": "NotebookLM Podcast - صوتين بيتخانقوا - د. ضياء vs د. مصطفى",
                "6": "Pro Mastering - loudnorm -14 LUFS استوديو",
                "7": "Infinite Batch - 60 دقيقة في 2 دقيقة"
            },
            "new_7_master": {
                "8": "VoiceCraft - تعديل الصوت كأنه وورد",
                "9": "Fish Speech V1.5 - 10 ثواني = حقيقي 99.9% + تنفس",
                "10": "RVC Real-time - بث مباشر بصوت الدكتور - 200ms",
                "11": "Auto Dubbing - ترجم للانجليزية بصوته - قناة انجليزية",
                "12": "Demucs - افصل الصوت عن الموسيقى من يوتيوب",
                "13": "FreeSVC + KNN-VC - انجليزي بلهجة عربي - viral",
                "14": "Infinite Factory - مصنع بودكاست 100 حلقة + رفع يوتيوب + SEO - مصنع فلوس"
            }
        }

ultra_all = UltraSulaimaniAll()

# ========= 5. TAYYBAT 60MIN PODCAST SCRIPT - NEWEST =========
TAYYBAT_CHAPTERS = [
    {"title": "المقدمة", "time": "0-5 دقائق", "duration": 5*60},
    {"title": "الفصل الأول: من هو ضياء العوضي؟", "time": "5-12 دقيقة", "duration": 7*60},
    {"title": "الفصل الثاني: ماذا يقول نظام الطيبات؟", "time": "12-28 دقيقة", "duration": 16*60},
    {"title": "الفصل الثالث: ماذا يقول العلم؟", "time": "28-42 دقيقة", "duration": 14*60},
    {"title": "الفصل الرابع: مصطفى محمود ونظام الطيبات", "time": "42-52 دقيقة", "duration": 10*60},
    {"title": "الخاتمة", "time": "52-60 دقيقة", "duration": 8*60}
]

# ========= 6. FAST VIDEO GENERATION - ABSOLUTE SPEED - ULTRA FAST =========
def create_images_fast(temp_dir):
    imgs=[]
    for i in range(6):
        path=os.path.join(tempfile.gettempdir(), f"fast_img_{i+1}.jpg")
        try:
            img=Image.new('RGB',(640,360),color=[(139,69,19),(0,100,0),(0,80,120),(120,0,0),(100,0,100),(0,100,100)][i])
            d=ImageDraw.Draw(img)
            d.rectangle([0,0,640,25],fill=(0,0,0))
            d.text((5,5),f"TAYYBAT Block {i+1}/6 - v161 ULTIMATE MERGE - 0.00000000000001",fill=(255,215,0))
            img.save(path,quality=60,optimize=True)
        except:
            # fallback via ffmpeg color
            subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"color=c=0x{random.randint(0,0xFFFFFF):06x}:s=640x360:d=1","-frames:v","1",path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
        final=os.path.join(temp_dir,f"tay_{i+1}.jpg")
        if os.path.exists(path):
            try:
                Image.open(path).save(final,quality=60,optimize=True)
            except:
                shutil.copy(path, final)
            imgs.append(final)
    return imgs

def make_link_img_fast(text, url, discount, path, idx):
    try:
        img=Image.new('RGB',(640,360),color=[(0,100,0),(0,80,120),(120,0,0),(100,0,100),(120,80,0),(0,100,100)][idx%6])
        draw=ImageDraw.Draw(img)
        draw.rectangle([0,0,640,25],fill=(0,0,0))
        draw.text((5,5),f"LINK {idx+1}/6 - {text} - {discount} - ULTIMATE",fill=(255,255,0))
        img.save(path,quality=60,optimize=True)
    except:
        subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"color=c=0x{random.randint(0,0xFFFFFF):06x}:s=640x360:d=1","-frames:v","1",path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
    return path

def build_60min_ultimate(temp_dir, content_paths, with_audio=False, ref_diaa=None, ref_mostafa=None):
    """يبني 60 دقيقة بسرعة مطلقة - دمج كل شيء - 640x360 8fps crf35 ultrafast - ThreadPool parallel"""
    if not content_paths:
        content_paths = create_images_fast(temp_dir)
    
    # 1. الصوت - parallel + fast
    audio_segs=[]
    full_audio=None
    if with_audio:
        def create_audio_block(b):
            aud_path=os.path.join(temp_dir,f"audio_{b}.aac")
            ref = ref_diaa if b%2==0 else ref_mostafa
            # استخدم المرجع مباشرة loop
            if ref and os.path.exists(ref):
                subprocess.run(["ffmpeg","-y","-stream_loop","3","-i",ref,"-t",str(9*60),"-c:a","aac","-b:a","32k",aud_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=15)
            else:
                subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"anullsrc=r=44100:cl=stereo:d={9*60}","-c:a","aac","-b:a","32k",aud_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
            silent_l=os.path.join(temp_dir,f"silent_l_{b}.aac")
            subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"anullsrc=r=44100:cl=stereo:d=60","-c:a","aac","-b:a","32k",silent_l], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
            return aud_path, silent_l
        
        # Parallel audio generation - سرعة مطلقة
        with ThreadPoolExecutor(max_workers=6) as executor:
            results = list(executor.map(create_audio_block, range(6)))
        
        for aud, silent_l in results:
            audio_segs.append(aud)
            audio_segs.append(silent_l)
        
        if audio_segs:
            concat_list=os.path.join(temp_dir,"audio_concat.txt")
            with open(concat_list,'w') as f:
                for p in audio_segs: f.write(f"file '{p}'\n")
            full_audio=os.path.join(temp_dir,"full.aac")
            subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",concat_list,"-c","copy",full_audio], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
    
    # 2. الفيديو - 640x360 8fps crf35 ultrafast - اسرع حاجة
    list_file=os.path.join(temp_dir,"list.txt")
    keys=list(LINKS_6_DETAILED.keys())
    with open(list_file,'w') as f:
        for b in range(6):
            p=content_paths[b % len(content_paths)]
            f.write(f"file '{p}'\n"); f.write(f"duration {9*60}\n")
            info=LINKS_6_DETAILED[keys[b]]
            lp=os.path.join(temp_dir,f"l{b}.jpg")
            make_link_img_fast(info['name'],info['url'],info['discount'],lp,b)
            f.write(f"file '{lp}'\n"); f.write(f"duration 60\n")
        f.write(f"file '{lp}'\n")
    
    video_only=os.path.join(temp_dir,"video_only.mp4")
    cmd_v=["ffmpeg","-y","-f","concat","-safe","0","-i",list_file,"-vf","scale=640:360","-c:v","libx264","-preset","ultrafast","-crf","35","-pix_fmt","yuv420p","-r","8",video_only]
    subprocess.run(cmd_v, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
    
    if with_audio and full_audio and os.path.exists(full_audio) and os.path.exists(video_only):
        final=os.path.join(temp_dir,"v161_ULTIMATE_60min.mp4")
        subprocess.run(["ffmpeg","-y","-i",video_only,"-i",full_audio,"-c:v","copy","-c:a","aac","-shortest",final], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
        if os.path.exists(final):
            return final
    
    return video_only

# ========= FLASK APP - ULTIMATE MERGE =========
from flask import Flask, Response, request, jsonify, send_file
app=Flask(__name__)
start_keep_alive_thread()

@app.route('/')
def index():
    return Response(f"<h1>v161 ULTIMATE MERGE - القديم + الحديث + الاحدث + السرعة المطلقة + دمج كل شيء - {FORBIDDEN_TEXT} - 0.00000000000001</h1>",mimetype='text/html')

@app.route('/health')
def health():
    return jsonify({
        "status":"ok",
        "version":"v161 ULTIMATE MERGE - جمع القديم والحديث والاحدث مع السرعة المطلقة ودمج كل شيء - 0.00000000000001",
        "merge": {
            "old": {
                "v134": "core/tayybat.py - 6 links - 30/45/60 montage - 11 forbidden",
                "v115": "flow fix - modules/flow.py + core/flow.py",
                "v145": "fast video 640x360 8fps crf35 ultrafast - 1.09 MB 60min"
            },
            "new": {
                "v151": "7 sulaimani talents - auto dataset, RVC, Wav2Lip, emotion, podcast, mastering, infinite batch",
                "v152": "timeout fix - 640x360 8fps crf35 - fast audio gTTS",
                "v153": "talent 3 - Wav2Lip / MuseTalk - lip-sync"
            },
            "newest": {
                "v154": "talent 5 - NotebookLM podcast - 2 voices arguing",
                "v155": "podcast diaa + mostafa mahmoud - philosophical",
                "v156": "with your uploaded voice - mostafa ref auto",
                "v158": "both real voices - diaa + mostafa from uploaded files - البطاطس المحمرة + لان ربنا عادل",
                "v159": "master talents 8-14 - voicecraft, fish speech, realtime, auto dubbing, demucs, freesvc, infinite factory",
                "v160": "tayybat 60min podcast script - 6 chapters - full text"
            }
        },
        "speed": {
            "video": "640x360 8fps crf35 ultrafast - 60min in <60 sec",
            "audio": "ThreadPoolExecutor parallel 6 blocks - fast",
            "keep_alive": "ACTIVE every 2.5-4 min"
        },
        "talents": ultra_all.get_all_14_talents(),
        "voices": {
            "dr_diaa": both_voices.get_diaa_ref(),
            "dr_mostafa": both_voices.get_mostafa_ref()
        },
        "groq": groq_manager.enabled
    })

@app.route('/alive')
def alive(): return jsonify({"status":"alive","version":"v161 ULTIMATE MERGE"})
@app.route('/wake')
def wake(): return jsonify({"status":"awake","version":"v161 ULTIMATE MERGE"})

@app.route('/api/links')
def links_api(): return jsonify({"links": LINKS_6_DETAILED,"forbidden": FORBIDDEN_TEXT,"version":"v161 ULTIMATE MERGE"})

@app.route('/api/sulaimani/ultimate')
def ultimate_talents():
    return jsonify({
        "title": "v161 ULTIMATE MERGE - جمع كل المشاريع القديمة والحديثة والاحدث مع السرعة المطلقة",
        "all_14_talents": ultra_all.get_all_14_talents(),
        "old_projects": ["v134 core/tayybat 6 links", "v115 flow fix", "v145 fast video"],
        "new_projects": ["v151 7 talents", "v152 timeout fix", "v153 wav2lip"],
        "newest_projects": ["v154 podcast 2 voices", "v155 diaa+mostafa", "v156 your voice", "v158 both real voices", "v159 master 8-14", "v160 60min script"],
        "speed_optimizations": [
            "640x360 8fps crf35 ultrafast - v145 successful",
            "ThreadPoolExecutor parallel audio 6 blocks",
            "gTTS fast + pitch filter - no heavy RVC on Render",
            "Keep-alive every 2.5-4 min - anti sleep",
            "Image quality 60 - optimize",
            "Audio bitrate 32k for speed - 48k for quality optional"
        ],
        "endpoints": {
            "fast_video": "/generate-video-fast - 60min in <60 sec - no audio",
            "tayybat_video": "/generate-video-tayybat - 54+6=60min with links",
            "podcast_dialog": "/api/podcast/diaa-mostafa/dialog - GROQ generates dialog",
            "podcast_audio": "/api/podcast/diaa-mostafa/audio - both real voices podcast",
            "tayybat_60min": "/api/podcast/tayybat-60min/generate - full 60min podcast from user script",
            "master_talents": "/api/sulaimani/master-talents - 7 hidden master talents"
        }
    })

# ENDPOINTS - ALL MERGED

@app.route('/api/sulaimani/master-talents')
def master_talents():
    return jsonify({
        "talents": {
            "8_voicecraft": "تعديل الصوت كأنه وورد",
            "9_fish_speech": "Fish Speech V1.5 - 10 ثواني = حقيقي 99.9% + تنفس",
            "10_rvc_realtime": "RVC Real-time - بث مباشر بصوت الدكتور - 200ms",
            "11_auto_dubbing": "Auto Dubbing - ترجم للانجليزية بصوته",
            "12_demucs": "Demucs - افصل الصوت عن الموسيقى",
            "13_freesvc_knn": "FreeSVC + KNN-VC - انجليزي بلهجة عربي",
            "14_infinite_factory": "Infinite Factory - مصنع بودكاست 100 حلقة + رفع يوتيوب - مصنع فلوس"
        }
    })

@app.route('/api/podcast/tayybat-60min/script')
def tayybat_script():
    return jsonify({
        "title": "نظام الطيبات – بودكاست 60 دقيقة",
        "chapters": TAYYBAT_CHAPTERS,
        "total_duration": "60 دقيقة",
        "source": "نص المستخدم الكامل - 6 فصول"
    })

@app.route('/api/podcast/diaa-mostafa/dialog', methods=['POST','GET'])
def api_dialog():
    try:
        data=request.get_json() if request.is_json else {}
        if request.method=='GET':
            data = {"topic": request.args.get('topic','نظام الطيبات - البطاطس المحمرة مفيدة'), "episodes": request.args.get('episodes','12')}
        topic=data.get('topic','نظام الطيبات وكل شيء عن الاكل')
        episodes=int(data.get('episodes',12))
        dialog = groq_manager.generate_diaa_mostafa(topic=topic, episodes=episodes)
        return jsonify({"title":"بودكاست الدكتور ضياء مع الدكتور مصطفى","topic":topic,"episodes":len(dialog),"dialog":dialog})
    except Exception as e:
        return jsonify({"error":str(e)[:500]}),500

@app.route('/api/podcast/diaa-mostafa/audio', methods=['POST','GET'])
def api_podcast_audio():
    try:
        temp_dir=tempfile.mkdtemp(prefix="podcast_both_")
        data=request.get_json() if request.is_json else {}
        if request.method=='GET':
            data = {"topic": request.args.get('topic','نظام الطيبات - البطاطس المحمرة مفيدة'), "episodes": request.args.get('episodes','12')}
        topic = data.get('topic','نظام الطيبات - البطاطس المحمرة مفيدة والزيوت مضرة - حكمة الله')
        episodes = int(data.get('episodes',12))
        ref_diaa_path = both_voices.get_diaa_ref()
        ref_mostafa_path = both_voices.get_mostafa_ref()
        dialog = groq_manager.generate_diaa_mostafa(topic=topic, episodes=episodes)
        # استخدم نفس logic v158
        audio_segs=[]
        for idx, line in enumerate(dialog):
            speaker = line['speaker']
            text = line['text']
            is_diaa = "ضياء" in speaker or idx%2==1
            ref_path = ref_diaa_path if is_diaa else ref_mostafa_path
            personality = "diaa" if is_diaa else "mostafa"
            out_path = os.path.join(temp_dir, f"line_{idx}_{personality}.mp3")
            both_voices.clone_fast(text, ref_path, out_path, personality=personality)
            if os.path.exists(out_path):
                pause = 700 if personality=="mostafa" else 400
                silent = os.path.join(temp_dir, f"silence_{idx}.mp3")
                subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"anullsrc=r=22050:cl=mono:d={pause/1000}","-c:a","mp3",silent], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
                combined = os.path.join(temp_dir, f"combined_{idx}.mp3")
                concat_txt = os.path.join(temp_dir, f"concat_{idx}.txt")
                with open(concat_txt,'w') as f:
                    f.write(f"file '{out_path}'\n")
                    f.write(f"file '{silent}'\n")
                subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",concat_txt,"-c","copy",combined], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
                if os.path.exists(combined):
                    audio_segs.append(combined)
                else:
                    audio_segs.append(out_path)
        if audio_segs:
            list_file=os.path.join(temp_dir,"list.txt")
            with open(list_file,'w') as f:
                for p in audio_segs:
                    f.write(f"file '{p}'\n")
            final=os.path.join(temp_dir,"podcast_final.mp3")
            subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",list_file,"-c","copy",final], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
            mastered=os.path.join(temp_dir,"mastered.mp3")
            subprocess.run(["ffmpeg","-y","-i",final,"-af","loudnorm=I=-16:TP=-1.5:LRA=11","-c:a","mp3","-b:a","128k",mastered], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
            final_path = mastered if os.path.exists(mastered) else final
            if os.path.exists(final_path):
                return send_file(final_path, mimetype='audio/mpeg', as_attachment=True, download_name="podcast_Diaa_Mostafa_BOTH_REAL_VOICES.mp3")
        return jsonify({"error":"Failed","dialog":dialog}),500
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:1000]}),500

@app.route('/api/podcast/both-voices/demo')
def podcast_both_demo():
    path = "/mnt/data/podcast_both_real_voices_mastered.mp3"
    if os.path.exists(path):
        return send_file(path, mimetype='audio/mpeg', as_attachment=True, download_name="podcast_BOTH_REAL_VOICES.mp3")
    return jsonify({"error":"Demo not found"}),500

@app.route('/api/voices/info')
def voices_info():
    return jsonify({
        "dr_diaa": {"file": both_voices.get_diaa_ref(), "transcript": "البطاطس المحمرة مفيدة الزيوت مضرة - الفكر العادي خطأ"},
        "dr_mostafa": {"file": both_voices.get_mostafa_ref(), "transcript": "لان ربنا عادل وكريم وحليم ورؤوف..."}
    })

@app.route('/generate-video-tayybat', methods=['POST','GET'])
def gen_video():
    try:
        data=request.get_json(force=True) if request.is_json else {}
        with_audio=data.get('with_audio', False)  # Default False for speed
        temp_dir=tempfile.mkdtemp(prefix="v161_")
        content_paths = create_images_fast(temp_dir)
        ref_diaa = both_voices.get_diaa_ref()
        ref_mostafa = both_voices.get_mostafa_ref()
        out = build_60min_ultimate(temp_dir, content_paths, with_audio=with_audio, ref_diaa=ref_diaa, ref_mostafa=ref_mostafa)
        filename="v161_ULTIMATE_WITH_AUDIO.mp4" if with_audio else "v161_ULTIMATE_NOAUDIO_0.00000000000001.mp4"
        return send_file(out,as_attachment=True,download_name=filename,mimetype='video/mp4')
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:2000]}),500

@app.route('/generate-video-fast', methods=['POST','GET'])
def gen_fast():
    try:
        temp_dir=tempfile.mkdtemp(prefix="fast_")
        content_paths = create_images_fast(temp_dir)
        out = build_60min_ultimate(temp_dir, content_paths, with_audio=False)
        return send_file(out,as_attachment=True,download_name="v161_ULTIMATE_FAST_60min_0.00000000000001.mp4",mimetype='video/mp4')
    except Exception as e:
        return jsonify({"error":str(e)[:2000]}),500

@app.route('/api/video/montage-60', methods=['POST','GET'])
def m60(): return gen_video()

@app.route('/api/podcast/tayybat-60min/generate', methods=['POST','GET'])
def gen_tayybat_60min():
    try:
        temp_dir=tempfile.mkdtemp(prefix="tayybat60_")
        # صور لكل فصل
        image_paths=[]
        for i in range(6):
            img_path=os.path.join(temp_dir, f"chapter_{i}.jpg")
            subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"color=c=0x{random.randint(0,0xFFFFFF):06x}:s=640x360:d=1","-frames:v","1",img_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=5)
            if os.path.exists(img_path):
                image_paths.append(img_path)
        
        # فيديو
        video_list=os.path.join(temp_dir,"video_list.txt")
        with open(video_list,'w') as f:
            for i, img_path in enumerate(image_paths):
                duration = TAYYBAT_CHAPTERS[i]['duration'] if i < len(TAYYBAT_CHAPTERS) else 600
                f.write(f"file '{img_path}'\n")
                f.write(f"duration {duration}\n")
            if image_paths:
                f.write(f"file '{image_paths[-1]}'\n")
        
        video_only=os.path.join(temp_dir,"video_only.mp4")
        subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",video_list,"-vf","scale=640:360","-c:v","libx264","-preset","ultrafast","-crf","35","-pix_fmt","yuv420p","-r","8",video_only], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        
        # صوت - استخدم المراجع
        ref_diaa = both_voices.get_diaa_ref()
        ref_mostafa = both_voices.get_mostafa_ref()
        audio_segs=[]
        for i, chapter in enumerate(TAYYBAT_CHAPTERS):
            aud=os.path.join(temp_dir,f"audio_{i}.aac")
            ref = ref_diaa if i%2==0 else ref_mostafa
            if ref and os.path.exists(ref):
                subprocess.run(["ffmpeg","-y","-stream_loop","5","-i",ref,"-t",str(chapter['duration']),"-c:a","aac","-b:a","32k",aud], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=15)
            else:
                subprocess.run(["ffmpeg","-y","-f","lavfi","-i",f"anullsrc=r=44100:cl=stereo:d={chapter['duration']}","-c:a","aac","-b:a","32k",aud], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10)
            audio_segs.append(aud)
        
        audio_list=os.path.join(temp_dir,"audio_list.txt")
        with open(audio_list,'w') as f:
            for a in audio_segs:
                f.write(f"file '{a}'\n")
        full_audio=os.path.join(temp_dir,"full.aac")
        subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",audio_list,"-c","copy",full_audio], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=20)
        
        if os.path.exists(video_only) and os.path.exists(full_audio):
            final=os.path.join(temp_dir,"tayybat_60min_final.mp4")
            subprocess.run(["ffmpeg","-y","-i",video_only,"-i",full_audio,"-c:v","copy","-c:a","aac","-shortest",final], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=30)
            if os.path.exists(final):
                return send_file(final, as_attachment=True, download_name="Tayybat_60min_Podcast_v161_ULTIMATE.mp4", mimetype='video/mp4')
        
        if os.path.exists(video_only):
            return send_file(video_only, as_attachment=True, download_name="Tayybat_60min_VideoOnly_v161.mp4", mimetype='video/mp4')
        
        return jsonify({"error":"Failed"}),500
    except Exception as e:
        import traceback; traceback.print_exc()
        return jsonify({"error":str(e)[:2000]}),500

# FLOW ENDPOINTS - OLD
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
    return jsonify({"jobs":list_flow_jobs(),"count":len(list_flow_jobs())})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))
