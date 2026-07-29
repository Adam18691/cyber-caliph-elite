import os,glob,secrets,threading,tempfile
from datetime import datetime
from flask import Flask,Response,request,jsonify
app=Flask(__name__)
E=os.environ.get
V={"ID":E('YOUTUBE_CLIENT_ID',''),"SEC":E('YOUTUBE_CLIENT_SECRET',''),"REF":E('YOUTUBE_REFRESH_TOKEN',''),"GROQ":E('GROQ_API_KEY',''),"API":E('YOUTUBE_API_KEY','')}
U=[] # uploads
def svc():
 c,s,r=V["ID"],V["SEC"],V["REF"]
 if not c or not s or not r: return None,"❌ اضف ID+SEC+REF - في الصورة ❌"
 try:
  from google.oauth2.credentials import Credentials
  from googleapiclient.discovery import build
  import google.auth.transport.requests as req
  cr=Credentials(None,refresh_token=r,token_uri="https://oauth2.googleapis.com/token",client_id=c,client_secret=s,scopes=["https://www.googleapis.com/auth/youtube.upload"])
  cr.refresh(req.Request())
  return build('youtube','v3',credentials=cr),"☑️ OK"
 except Exception as e: return None,f"❌ {str(e)[:60]}"

H="""<!DOCTYPE html><html dir=rtl lang=ar><head><meta charset=UTF-8><meta name=viewport content=width=device-width,initial-scale=1><title>v90 NANO - اسرع</title><style>
*{box-sizing:border-box;margin:0;padding:0;font:700 14px Tahoma}body{background:#fff;color:#000;padding:4px}
.b{display:inline-block;padding:1px 5px;border-radius:5px;font-size:11px;font-weight:900}.ok{background:#006400;color:#fff}.er{background:#ff0033;color:#fff}
.c{border:2px solid #006400;border-radius:10px;padding:6px;margin:5px 0;background:#f0fff0}
.cu{border:3px solid #ff6600;background:#fff5e6}
input{width:100%;padding:7px;border:2px solid #ccc;border-radius:7px;margin:3px 0}input.ok{border:3px solid #006400;background:#f0fff0}input.er{border:3px solid #ff0033;background:#fff0f0}
.r{display:flex;gap:4px;align-items:center;margin:4px 0}.r input{flex:1}
button{border:none;border-radius:7px;padding:8px 10px;font-weight:900;cursor:pointer}.btn{flex:1;min-height:36px}.o{background:#006400;color:#fff}.m{background:#ff0033;color:#fff}.u{background:#ff6600;color:#fff}.w{background:#fff;border:2px solid #000;color:#000;padding:5px 8px;font-size:11px}
.f{display:flex;gap:4px;flex-wrap:wrap}.f>*{flex:1 1 140px}
</style></head><body>
<h3 style=text-align:center>⚡ v90 NANO - أصغر واخف واسرع - 0.000000001ث<br><span class="b ok">☑️❌ مفاتيح فوري</span> <span class=b style=background:#ff6600;color:#fff>📤 ينزل فعلي</span></h3>

<div class=c>
<b>🔐 5 مفاتيح - كتابة=☑️ فوري + حفظ أوتوماتيك</b> <span id=kb class="b er">0/5 ❌</span>
<div class=r><input id=eI placeholder="ID ...googleusercontent.com = ☑️ - jm73b28cp..." oninput="K('ID',this.value)"><span id=sI class="b er">❌</span><button class=w onclick="T('eI')">👁️</button></div>
<div class=r><input id=eS type=password placeholder="SECRET GOCSPX-... = ☑️" oninput="K('SEC',this.value)"><span id=sS class="b er">❌</span><button class=w onclick="T('eS')">👁️</button></div>
<div class=r><input id=eR type=password placeholder="REFRESH 1//... = ☑️" oninput="K('REF',this.value)"><span id=sR class="b er">❌</span><button class=w onclick="T('eR')">👁️</button></div>
<div class=r><input id=eA type=password placeholder="API_KEY AIza... 39حرف = ☑️ مهم" oninput="K('API',this.value)"><span id=sA class="b er">❌</span><button class=w onclick="T('eA')">👁️</button></div>
<div class=r><input id=eG type=password placeholder="GROQ gsk_... = ☑️" oninput="K('GROQ',this.value)"><span id=sG class="b er">❌</span><button class=w onclick="T('eG')">👁️</button></div>
<div class=f><button class="btn o" onclick="SV()">🔐 حفظ - 0.000000001ث</button><button class=w onclick="LD()">👁️ تحميل</button><button class=w onclick="CK()">🔗 فحص ربط</button></div>
<div id=sb style=font-size:11px;margin-top:4px>في انتظار - اكتب يتحول ☑️ فوري - اسرع</div>
<div id=ls style=font-size:11px;margin-top:4px>🔗 ربط: ❌</div>
</div>

<div class="c cu">
<b>📤 رفع فعلي على القناة - ينزل فعلي - REAL UPLOAD</b>
<input id=f type=file accept="video/*"><input id=tt placeholder="عنوان الفيديو - ينزل فعلي">
<div class=f><select id=fs><option>📭 لا ملفات</option></select><button class=w onclick=RF()>🔄</button></div>
<div class=f><button class="btn u" onclick=UP()>📤 رفع فعلي الآن - 0.000000001ث</button><button class=w onclick=YT()>🔍 اختبار</button></div>
<div id=ui style=font-size:11px;margin-top:4px>📤 في انتظار - اسرع</div>
</div>

<div class=c>
<b>📥 تنزيل</b> <input id=urls placeholder="https://www.youtube.com/watch?v=..."><div class=f><button class="btn m" onclick=DL()>📥 تنزيل - 0.000000001ث</button></div><div id=mi style=font-size:11px>في انتظار</div>
</div>

<script>
let C={},T=null;
function V(k,v){if(!v)return 0;v=v.trim();if(k=='GROQ')return v.startsWith('gsk_');if(k=='ID')return v.includes('googleusercontent.com');if(k=='SEC')return v.startsWith('GOCSPX-');if(k=='REF')return v.startsWith('1//');if(k=='API')return v.startsWith('AIza')&&v.length>30;return 0}
function U(k,v){let ok=V(k,v),id={GROQ:'sG',ID:'sI',SEC:'sS',REF:'sR',API:'sA'}[k],inp={GROQ:'eG',ID:'eI',SEC:'eS',REF:'eR',API:'eA'}[k];let b=document.getElementById(id),i=document.getElementById(inp);if(b){b.textContent=ok?'☑️':'❌';b.className='b '+(ok?'ok':'er')}if(i)i.className=ok?'ok':'er';G();return ok}
function G(){let ks=['GROQ','ID','SEC','REF','API'],c=0;ks.forEach(k=>{let el=document.getElementById({GROQ:'eG',ID:'eI',SEC:'eS',REF:'eR',API:'eA'}[k]);if(el&&V(k,el.value))c++});document.getElementById('kb').textContent=c+'/5 '+(c==5?'☑️':'❌');document.getElementById('kb').className='b '+(c==5?'ok':'er');let g=id=>{let el=document.getElementById(id);return el&&V({eG:'GROQ',eI:'ID',eS:'SEC',eR:'REF',eA:'API'}[id],el.value)};document.getElementById('ls').innerHTML='🔗 GROQ:'+(g('eG')?'☑️':'❌')+' ID:'+(g('eI')?'☑️':'❌')+' SEC:'+(g('eS')?'☑️':'❌')+' REF:'+(g('eR')?'☑️':'❌')+' API:'+(g('eA')?'☑️':'❌')+(g('eI')&&g('eS')&&g('eR')?'<br>☑️ مربوطة - جاهزة للرفع فعلي':'')}
function K(k,v){C[k]=v;U(k,v);if(T)clearTimeout(T);T=setTimeout(()=>{let p={};['eG','eI','eS','eR','eA'].forEach(id=>{let el=document.getElementById(id);if(el&&el.value.trim()){let kk={eG:'GROQ_API_KEY',eI:'YOUTUBE_CLIENT_ID',eS:'YOUTUBE_CLIENT_SECRET',eR:'YOUTUBE_REFRESH_TOKEN',eA:'YOUTUBE_API_KEY'}[id];p[kk]=el.value.trim()}});if(Object.keys(p).length>0)fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(p)}).then(r=>r.json()).then(d=>{document.getElementById('sb').textContent='☑️ حفظ '+d.count+'/5 - 0.000000001ث'})},400)}
function T(id){let i=document.getElementById(id);i.type=i.type=='password'?'text':'password'}
function SV(){let p={};['eG','eI','eS','eR','eA'].forEach(id=>{let el=document.getElementById(id);if(el&&el.value.trim()){let k={eG:'GROQ_API_KEY',eI:'YOUTUBE_CLIENT_ID',eS:'YOUTUBE_CLIENT_SECRET',eR:'YOUTUBE_REFRESH_TOKEN',eA:'YOUTUBE_API_KEY'}[id];p[k]=el.value.trim()}});fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(p)}).then(r=>r.json()).then(d=>{document.getElementById('sb').textContent='☑️ حفظ '+d.count+'/5 - 0.000000001ث'})}
function LD(){fetch('/api/keys/show').then(r=>r.json()).then(s=>{document.getElementById('eI').value=s.YOUTUBE_CLIENT_ID||'';document.getElementById('eS').value=s.YOUTUBE_CLIENT_SECRET||'';document.getElementById('eR').value=s.YOUTUBE_REFRESH_TOKEN||'';document.getElementById('eG').value=s.GROQ_API_KEY||'';document.getElementById('eA').value=s.YOUTUBE_API_KEY||'';['ID','SEC','REF','GROQ','API'].forEach(k=>{let id={ID:'eI',SEC:'eS',REF:'eR',GROQ:'eG',API:'eA'}[k];U(k,document.getElementById(id).value)});})}
function CK(){fetch('/api/keys/status').then(r=>r.json()).then(s=>{document.getElementById('kb').textContent=(s.linked?'☑️ ':'')+s.count+'/5';G()})}
function DL(){let u=document.getElementById('urls').value.trim();if(!u)return;document.getElementById('mi').textContent='📥 بدء - 0.000000001ث';fetch('/api/dl',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({url:u})}).then(r=>r.json()).then(d=>{document.getElementById('mi').textContent='☑️ '+d.title+' - '+d.progress+'% - 0.000000001ث';RF()})}
function RF(){fetch('/api/files').then(r=>r.json()).then(d=>{let sel=document.getElementById('fs');if(d.files.length==0)sel.innerHTML='<option>📭 لا ملفات</option>';else sel.innerHTML='<option>📁 اختر للرفع فعلي</option>'+d.files.map(f=>`<option value="${f.path}">${f.name} - ${(f.size/1024/1024).toFixed(1)}MB</option>`).join('')})}
function UP(){let file=document.getElementById('f').files[0];let sel=document.getElementById('fs').value;let title=document.getElementById('tt').value||'فيديو - 0.000000001ث';if(file){let fd=new FormData();fd.append('file',file);fd.append('title',title);document.getElementById('ui').textContent='📤 رفع من الجهاز - 0.000000001ث';fetch('/api/up/file',{method:'POST',body:fd}).then(r=>r.json()).then(d=>{document.getElementById('ui').textContent=(d.success?'☑️ ':'❌ ')+(d.info?d.info.status:d.error)+' - 0.000000001ث'})}else if(sel.includes('/tmp')){document.getElementById('ui').textContent='📤 رفع '+sel+' - 0.000000001ث';fetch('/api/up/real',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({file_path:sel,title:title})}).then(r=>r.json()).then(d=>{document.getElementById('ui').textContent=(d.success?'☑️ ':'❌ ')+(d.info?d.info.status:d.error)+' - 0.000000001ث'})}else{document.getElementById('ui').textContent='❌ اختر ملف - 0.000000001ث'}}
function YT(){document.getElementById('ui').textContent='🔍 اختبار - 0.000000001ث';fetch('/api/yt/test').then(r=>r.json()).then(d=>{document.getElementById('ui').textContent=(d.success?'☑️ '+d.message:'❌ '+d.error)+' - 0.000000001ث'})}
LD();setTimeout(()=>{CK();G();RF()},300);
</script></body></html>
"""

@app.route('/')
def index(): return Response(H, mimetype='text/html', headers={'Cache-Control':'public, max-age=60'})

@app.route('/api/keys/save', methods=['POST'])
def ks():
 d=request.get_json()
 for k,v in d.items():
  if k=='YOUTUBE_CLIENT_ID': V['ID']=v.strip()
  elif k=='YOUTUBE_CLIENT_SECRET': V['SEC']=v.strip()
  elif k=='YOUTUBE_REFRESH_TOKEN': V['REF']=v.strip()
  elif k=='GROQ_API_KEY': V['GROQ']=v.strip()
  elif k=='YOUTUBE_API_KEY': V['API']=v.strip()
 cnt=sum(1 for x in V.values() if x and len(x)>5)
 return jsonify({"count":cnt})

@app.route('/api/keys/status')
def kst(): return jsonify({"linked":bool(V['ID'] and V['SEC'] and V['REF'] and 'googleusercontent.com' in V['ID'] and V['SEC'].startswith('GOCSPX-') and V['REF'].startswith('1//')),"count":sum(1 for k in V if V[k] and len(V[k])>5)})

@app.route('/api/keys/show')
def ksh(): return jsonify({"YOUTUBE_CLIENT_ID":V['ID'],"YOUTUBE_CLIENT_SECRET":V['SEC'],"YOUTUBE_REFRESH_TOKEN":V['REF'],"GROQ_API_KEY":V['GROQ'],"YOUTUBE_API_KEY":V['API']})

@app.route('/api/yt/test')
def yt():
 s,m=svc()
 if not s: return jsonify({"success":False,"error":m})
 try:
  c=s.channels().list(part="snippet",mine=True).execute()
  n=c['items'][0]['snippet']['title'] if c.get('items') else "قناتك"
  return jsonify({"success":True,"message":f"☑️ {n} - جاهز للرفع فعلي - 0.000000001ث"})
 except Exception as e: return jsonify({"success":False,"error":str(e)[:60]})

@app.route('/api/files')
def fl():
 fs=[]
 for p in ["/tmp/MANUAL_*","/tmp/REAL_UPLOAD_*"]:
  for f in glob.glob(p):
   if os.path.isfile(f):
    try: fs.append({"path":f,"name":f.split('/')[-1],"size":os.path.getsize(f)})
    except: pass
 return jsonify({"files":sorted(fs,key=lambda x:x["size"],reverse=True)[:8]})

@app.route('/api/up/real', methods=['POST'])
def upr():
 try:
  d=request.get_json(); fp=d.get('file_path',''); ttl=d.get('title','فيديو - 0.000000001ث')
  s,_=svc()
  if not s: return jsonify({"success":False,"error":"❌ اضف مفاتيح"})
  from googleapiclient.http import MediaFileUpload
  if not os.path.exists(fp): return jsonify({"success":False,"error":"❌ ملف غير موجود"})
  body={"snippet":{"title":ttl[:100],"description":"#ترتاريا #اسرع","categoryId":"22"},"status":{"privacyStatus":"public"}}
  media=MediaFileUpload(fp,resumable=True,mimetype="video/*")
  req=s.videos().insert(part="snippet,status",body=body,media_body=media)
  info={"title":ttl,"status":"📤 بدء - 0.000000001ث"}
  def bg():
   try:
    r=None
    while r is None:
     st,r=req.next_chunk()
     if st: info["status"]=f"📤 {int(st.progress()*100)}% - 0.000000001ث"
    if r: info["status"]=f"☑️ تم - https://www.youtube.com/watch?v={r.get('id')} - 0.000000001ث"
   except Exception as e: info["status"]=f"❌ {str(e)[:50]}"
  threading.Thread(target=bg,daemon=True).start()
  return jsonify({"success":True,"info":info})
 except Exception as e: return jsonify({"success":False,"error":str(e)[:50]})

@app.route('/api/up/file', methods=['POST'])
def upf():
 try:
  if 'file' not in request.files: return jsonify({"success":False,"error":"لا ملف"})
  file=request.files['file']; ttl=request.form.get('title','فيديو - 0.000000001ث')
  ext=file.filename.split('.')[-1] if '.' in file.filename else 'mp4'
  tmp=os.path.join(tempfile.gettempdir(),f"REAL_{datetime.now().strftime('%H%M%S')}_{secrets.token_hex(2)}.{ext}")
  file.save(tmp)
  s,_=svc()
  if not s: return jsonify({"success":False,"error":"❌ اضف مفاتيح"})
  from googleapiclient.http import MediaFileUpload
  body={"snippet":{"title":ttl[:100],"description":"#ترتاريا #اسرع","categoryId":"22"},"status":{"privacyStatus":"public"}}
  media=MediaFileUpload(tmp,resumable=True,mimetype="video/*")
  req=s.videos().insert(part="snippet,status",body=body,media_body=media)
  info={"title":ttl,"status":"📤 بدء من الجهاز - 0.000000001ث"}
  def bg():
   try:
    r=None
    while r is None:
     st,r=req.next_chunk()
     if st: info["status"]=f"📤 {int(st.progress()*100)}% - 0.000000001ث"
    if r: info["status"]=f"☑️ تم - https://www.youtube.com/watch?v={r.get('id')} - 0.000000001ث"
   except Exception as e: info["status"]=f"❌ {str(e)[:50]}"
  threading.Thread(target=bg,daemon=True).start()
  return jsonify({"success":True,"info":info})
 except Exception as e: return jsonify({"success":False,"error":str(e)[:50]})

@app.route('/api/dl', methods=['POST'])
def dl():
 try:
  import yt_dlp
  url=request.get_json().get('url','')
  ts=datetime.now().strftime("%H%M%S"); out=f"/tmp/MANUAL_{ts}_%(title)s.%(ext)s"
  info={"title":url[:15],"progress":5,"status":"📥 بدء - 0.000000001ث"}
  def bg():
   try:
    def h(d):
     if d['status']=='downloading':
      tot=d.get('total_bytes') or d.get('total_bytes_estimate',1); cur=d.get('downloaded_bytes',0); info["progress"]=int(cur*100/tot)
    with yt_dlp.YoutubeDL({'format':'best[height<=720]/best','outtmpl':out,'progress_hooks':[h],'quiet':True}) as ydl: ydl.download([url])
    fs=glob.glob(f"/tmp/MANUAL_{ts}_*")
    if fs: info["progress"]=100; info["title"]=fs[0].split('/')[-1]; info["status"]=f"☑️ اكتمل - {fs[0]} - 0.000000001ث"
   except Exception as e: info["status"]=f"❌ {str(e)[:40]}"
  threading.Thread(target=bg,daemon=True).start()
  return jsonify(info)
 except Exception as e: return jsonify({"title":"خطأ","progress":0,"status":str(e)[:40]})

@app.route('/health')
def hl(): return f"v90 NANO - 0.000000001ث - {len(U)} رفع - اصغر واخف واسرع - {sum(1 for x in V.values() if x)}/5 ☑️"

if __name__=='__main__': app.run(host='0.0.0.0',port=5000)
