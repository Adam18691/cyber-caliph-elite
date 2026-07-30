# FILE: app.py - اسم الملف: app.py - v98 PROFESSIONAL - <400 سطر - احترافي مقسم - اسم الملف على الملف - FIXED - مكان النسخ والازرار شغالة - الرئيسي
"""FILE: app.py - اسم الملف: app.py - v98 PROFESSIONAL - <400 سطر - الرئيسي - يربط كل الموديولات - اسم الملف على الملف"""
import os, json
from flask import Flask, Response, request, jsonify
from config.settings import settings
from core.vault import vault
from core.channel import CH, VIDEOS, fetch_channel, start_auto
from core.downloader import MANUAL_DL, LIVE_DL, dl_real, list_files
from modules.monetization import MONO_PRODUCTS
from modules.cinematic import MONTAGE_STYLES, CAMERAS, ANGLES, INTROS, PERSUASION
from modules.translation import create_translation_job, list_trans
from modules.factory import create_factory_job, list_factory
from modules.json_copy import list_json_files, create_sample_json

app = Flask(__name__)
app.secret_key = "v98_FILENAME_ON_FILE"
start_auto()

def load_html():
    # FILE: app.py - HTML - اسم الملف على الملف - احترافي
    try:
        from pathlib import Path
        p=Path(__file__).parent/"templates"/"elite.html"
        if p.exists() and p.stat().st_size>1000:
            return p.read_text(encoding='utf-8')
    except: pass
    return html_pro()

def html_pro():
    # FILE: app.py - HTML مضمن - اسم الملف على الملف - مكان النسخ واضح
    return """<!DOCTYPE html><html dir=rtl lang=ar><head><meta charset=UTF-8><meta name=viewport content="width=device-width,initial-scale=1"><title>FILE: app.py - v98 - اسم الملف على الملف</title><style>
*{box-sizing:border-box;margin:0;padding:0;font:700 13px Tahoma}body{background:#f5f5f5;color:#000;padding:6px}
.badge{display:inline-block;padding:3px 8px;border-radius:8px;font-size:11px;font-weight:900;margin:2px}.ok{background:#006400;color:#fff}.er{background:#ff0033;color:#fff}.info{background:#0064ff;color:#fff}.warn{background:#FFD700;color:#000}.purple{background:#800080;color:#fff}.copybg{background:#000;color:#0f0;border:2px solid #0f0}
.card{border:3px solid #ddd;border-radius:12px;padding:10px;margin:8px 0;background:#fff;box-shadow:0 2px 8px rgba(0,0,0,.1)}.card-json{border:4px solid #000;background:#fff}.card-trans{border:3px solid #800080;background:#F5F0FF}.card-keys{border:3px solid #006400;background:#F0FFF0}
input,textarea,select{width:100%;padding:10px;border:2px solid #ccc;border-radius:8px;margin:4px 0;min-height:42px;font-size:13px}
.row{display:flex;gap:6px;align-items:center;margin:6px 0}.row input{flex:1}
button{border:none;border-radius:10px;padding:12px 16px;font-weight:900;cursor:pointer;font-size:13px;min-height:48px}button:active{transform:scale(.97)}
.btn{flex:1}.btn-blue{background:#0064ff;color:#fff}.btn-green{background:#006400;color:#fff}.btn-yellow{background:#FFD700;color:#000}.btn-purple{background:#800080;color:#fff}.btn-copy{background:#0064ff;color:#fff;border:2px solid #fff}.btn-eye{background:#fff;border:2px solid #000;color:#000;min-width:50px;min-height:42px;padding:6px}
.flex{display:flex;gap:6px;flex-wrap:wrap}.flex>*{flex:1 1 140px}
.json-box{border:3px solid #000;border-radius:10px;background:#000;color:#0f0;padding:0;overflow:hidden;margin:8px 0}
.json-header{background:#000;color:#0f0;padding:10px;display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #0f0}
.json-textarea{width:100%;min-height:180px;background:#000;color:#0f0;border:none;padding:10px;font-family:monospace;font-size:12px;direction:ltr;text-align:left;resize:vertical}
.copy-place{background:#0064ff;color:#fff;padding:14px;border-radius:10px;text-align:center;font-size:14px;font-weight:900;margin:8px 0;border:3px solid #fff}
.status-box{border:3px solid #0064ff;border-radius:10px;padding:10px;margin:8px 0;background:#F0F8FF;font-size:12px;min-height:40px}
.filename-header{background:#000;color:#FFD700;padding:10px;border-radius:8px;margin:6px 0;font-family:monospace;font-size:12px;border:2px solid #FFD700;text-align:center}
@media(max-width:600px){.flex{flex-direction:column}}
</style></head><body>
<div class="filename-header">FILE: app.py - اسم الملف: app.py - v98 PROFESSIONAL - اسم الملف على الملف - كل ملف <400 سطر - FIXED</div>
<h2 style=text-align:center;background:#000;color:#0f0;padding:12px;border-radius:12px;margin-bottom:8px;border:3px solid #0f0>
📁 v98 PROFESSIONAL - اسم الملف على الملف - احترافي مقسم كل ملف &lt;400 سطر - FIXED<br>
<span style=font-size:11px>اكتب اسم الملف على الملف - تم - FILE: filename - اسم الملف: filename - كل ملف فيه اسمه</span>
</h2>
<div style=background:#0064ff;color:#fff;padding:12px;border-radius:12px;text-align:center;font-weight:900;margin-bottom:8px;border:3px solid #fff>
📁 اسم الملف على الملف - FILE: app.py - اسم الملف: app.py - كل ملف فيه اسمه - احترافي مقسم &lt;400 سطر - FIXED
</div>
<div class="card card-json">
<div class="filename-header">FILE: modules/json_copy.py - اسم الملف: modules/json_copy.py - مكان النسخ - هنا</div>
<h3>📄 JSON COPY - مكان النسخ - هنا - FILE: modules/json_copy.py <span class="badge copybg">📋 اسم الملف على الملف</span></h3>
<p style=background:#000;color:#0f0;padding:8px;border-radius:8px;margin:6px 0;font-family:monospace>
📁 FILE: app.py - اسم الملف: app.py - 207 سطر ✅ &lt;400<br>
📁 FILE: config/settings.py - 62 سطر ✅ &lt;400<br>
📁 FILE: core/vault.py - 45 سطر ✅ &lt;400<br>
📁 FILE: core/channel.py - 58 سطر ✅ &lt;400<br>
📁 FILE: core/downloader.py - 49 سطر ✅ &lt;400<br>
📁 FILE: modules/monetization.py - 24 سطر ✅ &lt;400<br>
📁 FILE: modules/cinematic.py - 61 سطر ✅ &lt;400<br>
📁 FILE: modules/translation.py - 88 سطر ✅ &lt;400<br>
📁 FILE: modules/json_copy.py - 71 سطر ✅ &lt;400<br>
📁 FILE: modules/factory.py - 61 سطر ✅ &lt;400<br>
✅ كل ملف فيه اسمه في أول سطر - احترافي - FIXED
</p>
<div class="flex">
<button class="btn btn-blue" onclick="doJsonList()">📘 FILE: modules/json_copy.py - تحديث JSON - FIXED</button>
<button class="btn btn-green" onclick="doJsonCreate()">📗 FILE: modules/json_copy.py - إنشاء JSON - FIXED</button>
<button class="btn btn-yellow" onclick="doJsonCopyAll()">📙 FILE: modules/json_copy.py - نسخ كل JSON - FIXED</button>
</div>
<div id="jsonStatus" class="status-box" style="border-color:#000;background:#000;color:#0f0">📁 FILE: modules/json_copy.py - مكان النسخ هنا - اسم الملف على الملف - FIXED</div>
<div class="copy-place">📋 FILE: app.py - مكان النسخ الرئيسي - هنا - اسم الملف على الملف - FIXED</div>
<div id="jsonListArea" style="margin-top:8px"><div style="background:#fff;border:3px dashed #000;border-radius:10px;padding:20px;text-align:center">📁 FILE: modules/json_copy.py - لا يوجد JSON بعد - اضغط الزر الأخضر - اسم الملف على الملف - FIXED<br><br><button class="btn btn-green" onclick="doJsonCreate()" style="padding:14px">📗 إنشاء JSON عينة الآن - FIXED</button></div></div>
</div>
<div class="card card-trans">
<div class="filename-header">FILE: modules/translation.py - اسم الملف: modules/translation.py - ترجمة 20 دولة</div>
<h3>🌍 FILE: modules/translation.py - ترجمة 20 دولة - اسم الملف على الملف <span class="badge purple">🌍 20 دولة</span></h3>
<div class="flex" style="margin-top:8px">
<select id="topicSel" style="flex:2"><option value="0">🏭 ترتاريا العظمى - 20 لغة</option><option value="1">⚡ تكنولوجيا ترتاريا</option><option value="2">🌊 Mud Flood</option><option value="3">🏛️ عمارة ترتاريا</option><option value="4">🌍 الجغرافيا المحرمة</option></select>
<input id="customTitle" placeholder="FILE: modules/translation.py - عنوان مخصص - اسم الملف على الملف" style="flex:1">
</div>
<textarea id="customDesc" rows="2" placeholder="FILE: modules/translation.py - وصف مخصص - اسم الملف على الملف"></textarea>
<div class="flex"><select id="videoDuration" style="flex:1"><option value="60">⏱️ 60 دقيقة</option><option value="45">⏱️ 45 دقيقة</option><option value="30">⏱️ 30 دقيقة</option><option value="10">⏱️ 10 دقائق</option></select><label style="flex:1;display:flex;align-items:center;gap:6px;background:#FFFDE7;border:2px solid #FFD700;border-radius:8px;padding:8px"><input type="checkbox" id="includeMono" checked style="width:auto"> 📦 FILE: modules/monetization.py - Monoprice</label></div>
<div class="flex" style="margin-top:8px"><button class="btn btn-purple" onclick="doTransCreate()">🌍 FILE: modules/translation.py - ترجم 20 دولة</button><button class="btn" style="background:#fff;border:3px solid #800080;color:#800080" onclick="doTransList()">🔄 FILE: modules/translation.py - تحديث</button></div>
<div id="transStatus" class="status-box">🌍 FILE: modules/translation.py - اسم الملف على الملف - FIXED - في انتظار</div>
<div id="transListArea" style="border:2px solid #800080;border-radius:8px;padding:6px;min-height:40px;background:#fff">📁 FILE: modules/translation.py - لا يوجد فيديو مترجم - اسم الملف على الملف - FIXED</div>
</div>
<div class="card card-keys">
<div class="filename-header">FILE: core/vault.py - اسم الملف: core/vault.py - 5 مفاتيح - اسم الملف على الملف</div>
<h3>🔐 FILE: core/vault.py - 5 مفاتيح - اسم الملف على الملف <span id="keysBadge" class="badge er">0/5 ❌</span></h3>
<div class="row"><button class="btn-eye" onclick="toggleEye('eI')">👁️</button><span id="sI" class="badge er">❌</span><input id="eI" placeholder="FILE: core/vault.py - ID ...googleusercontent.com - اسم الملف على الملف" oninput="onKeyInput('ID',this.value)"></div>
<div class="row"><button class="btn-eye" onclick="toggleEye('eS')">👁️</button><span id="sS" class="badge er">❌</span><input id="eS" type="password" placeholder="FILE: core/vault.py - SECRET GOCSPX-... - اسم الملف على الملف" oninput="onKeyInput('SEC',this.value)"></div>
<div class="row"><button class="btn-eye" onclick="toggleEye('eR')">👁️</button><span id="sR" class="badge er">❌</span><input id="eR" type="password" placeholder="FILE: core/vault.py - REFRESH 1//... - اسم الملف على الملف" oninput="onKeyInput('REF',this.value)"></div>
<div class="row"><button class="btn-eye" onclick="toggleEye('eA')">👁️</button><span id="sA" class="badge er">❌</span><input id="eA" type="password" placeholder="FILE: core/vault.py - API_KEY AIza... - اسم الملف على الملف" oninput="onKeyInput('API',this.value)"></div>
<div class="row"><button class="btn-eye" onclick="toggleEye('eG')">👁️</button><span id="sG" class="badge er">❌</span><input id="eG" type="password" placeholder="FILE: core/vault.py - GROQ gsk_... - اسم الملف على الملف" oninput="onKeyInput('GROQ',this.value)"></div>
<div class="flex" style="margin-top:8px"><button class="btn btn-green" onclick="doSaveKeys()">🔐 FILE: core/vault.py - حفظ - اسم الملف على الملف</button><button class="btn" style="background:#fff;border:3px solid #000" onclick="doLoadKeys()">👁️ FILE: core/vault.py - تحميل</button><button class="btn" style="background:#fff;border:3px solid #0064ff;color:#0064ff" onclick="doCheckKeys()">🔗 FILE: core/vault.py - فحص ربط</button></div>
<div id="saveStatus" style="background:#000;color:#0f0;padding:8px;border-radius:8px;margin-top:6px;font-family:monospace">FILE: core/vault.py - في انتظار - اسم الملف على الملف - احترافي مقسم &lt;400 سطر - FILE: app.py</div>
<div id="linkStatus" style="font-size:11px;margin-top:4px">🔗 FILE: core/vault.py - ربط: ❌ - اسم الملف على الملف - FIXED</div>
<div id="channelInfo" style="font-size:11px;margin-top:4px">⏳ FILE: core/channel.py - قناة - اسم الملف على الملف - FIXED</div>
</div>
<script>
let saveTimer=null;
function isValid(k,v){if(!v)return false;v=v.trim();if(k=='GROQ')return v.startsWith('gsk_')&&v.length>20;if(k=='ID')return v.includes('googleusercontent.com')&&v.length>20;if(k=='SEC')return v.startsWith('GOCSPX-')&&v.length>10;if(k=='REF')return v.startsWith('1//')&&v.length>20;if(k=='API')return v.startsWith('AIza')&&v.length>30;return v.length>5;}
function updateBadge(k,v){let ok=isValid(k,v);let mapId={GROQ:'sG',ID:'sI',SEC:'sS',REF:'sR',API:'sA'};let mapInput={GROQ:'eG',ID:'eI',SEC:'eS',REF:'eR',API:'eA'};let badge=document.getElementById(mapId[k]);let inp=document.getElementById(mapInput[k]);if(badge){badge.textContent=ok?'☑️ '+v.length:'❌ '+v.length;badge.className='badge '+(ok?'ok':'er');}if(inp){inp.style.borderColor=ok?'#006400':'#ff0033';inp.style.background=ok?'#F0FFF0':'#FFF0F0';}updateTotal();return ok;}
function updateTotal(){let keys=['GROQ','ID','SEC','REF','API'];let ids={GROQ:'eG',ID:'eI',SEC:'eS',REF:'eR',API:'eA'};let c=0;keys.forEach(k=>{let el=document.getElementById(ids[k]);if(el&&isValid(k,el.value))c++;});let badge=document.getElementById('keysBadge');if(badge){badge.textContent=c+'/5 '+(c==5?'☑️ مربوطة':'❌')+' - FILE: core/vault.py';badge.className='badge '+(c==5?'ok':'er');}}
function onKeyInput(k,v){updateBadge(k,v);if(saveTimer)clearTimeout(saveTimer);saveTimer=setTimeout(()=>{let payload={};let map={eG:'GROQ_API_KEY',eI:'YOUTUBE_CLIENT_ID',eS:'YOUTUBE_CLIENT_SECRET',eR:'YOUTUBE_REFRESH_TOKEN',eA:'YOUTUBE_API_KEY'};['eG','eI','eS','eR','eA'].forEach(id=>{let el=document.getElementById(id);if(el&&el.value.trim()){payload[map[id]]=el.value.trim();}});if(Object.keys(payload).length>0){fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)}).then(r=>r.json()).then(d=>{document.getElementById('saveStatus').textContent='☑️ FILE: core/vault.py - حفظ '+d.count+'/5 - اسم الملف على الملف - '+new Date().toLocaleTimeString();});}},500);}
function toggleEye(id){let inp=document.getElementById(id);if(!inp)return;inp.type=inp.type=='password'?'text':'password';}
function doSaveKeys(){let payload={};let map={eG:'GROQ_API_KEY',eI:'YOUTUBE_CLIENT_ID',eS:'YOUTUBE_CLIENT_SECRET',eR:'YOUTUBE_REFRESH_TOKEN',eA:'YOUTUBE_API_KEY'};['eG','eI','eS','eR','eA'].forEach(id=>{let el=document.getElementById(id);if(el&&el.value.trim())payload[map[id]]=el.value.trim();});document.getElementById('saveStatus').textContent='⏳ FILE: core/vault.py - جاري الحفظ...';fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)}).then(r=>r.json()).then(d=>{document.getElementById('saveStatus').textContent='☑️ FILE: core/vault.py - تم الحفظ '+d.count+'/5 - اسم الملف على الملف - FIXED';doCheckKeys();});}
function doLoadKeys(){fetch('/api/keys/show').then(r=>r.json()).then(s=>{document.getElementById('eI').value=s.YOUTUBE_CLIENT_ID||'';document.getElementById('eS').value=s.YOUTUBE_CLIENT_SECRET||'';document.getElementById('eR').value=s.YOUTUBE_REFRESH_TOKEN||'';document.getElementById('eG').value=s.GROQ_API_KEY||'';document.getElementById('eA').value=s.YOUTUBE_API_KEY||'';['ID','SEC','REF','GROQ','API'].forEach(k=>{let idMap={ID:'eI',SEC:'eS',REF:'eR',GROQ:'eG',API:'eA'};let el=document.getElementById(idMap[k]);if(el)updateBadge(k,el.value);});document.getElementById('saveStatus').textContent='☑️ FILE: core/vault.py - تم التحميل - اسم الملف على الملف - FIXED';});}
function doCheckKeys(){fetch('/api/keys/status').then(r=>r.json()).then(s=>{document.getElementById('keysBadge').textContent=(s.linked?'☑️ ':'')+s.count+'/5 - FILE: core/vault.py - اسم الملف على الملف';document.getElementById('saveStatus').textContent='🔗 FILE: core/vault.py - فحص: '+s.count+'/5 - '+(s.linked?'☑️ مربوطة':'❌ غير مربوطة')+' - اسم الملف على الملف - FIXED';updateTotal();});}
function doCopyText(textareaId,btnId){let ta=document.getElementById(textareaId);if(!ta){alert('❌ FILE: '+textareaId+' غير موجود');return;}ta.focus();ta.select();ta.setSelectionRange(0,999999);let btn=document.getElementById(btnId);let originalText=btn?btn.textContent:'';const success=()=>{if(btn){btn.textContent='✅ تم النسخ! - FILE: '+textareaId;btn.style.background='#006400';setTimeout(()=>{btn.textContent=originalText||'📋 نسخ JSON';btn.style.background='#0064ff';},2000);}else{alert('✅ تم النسخ! - FILE: '+textareaId);}};const fail=()=>{try{document.execCommand('copy');success();}catch(e){if(btn){btn.textContent='❌ فشل النسخ';}else{alert('❌ فشل النسخ');}}};if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(ta.value).then(success).catch(fail);}else{fail();}}
function doJsonList(){let status=document.getElementById('jsonStatus');let area=document.getElementById('jsonListArea');if(status)status.textContent='⏳ FILE: modules/json_copy.py - جاري تحديث - اسم الملف على الملف - FIXED...';if(area)area.innerHTML='<div style="text-align:center;padding:20px">⏳ FILE: modules/json_copy.py - جاري التحميل - اسم الملف على الملف - FIXED...</div>';fetch('/api/json/list').then(r=>r.json()).then(d=>{if(status)status.textContent='📁 FILE: modules/json_copy.py - '+d.count+' ملف JSON - '+d.total_size+' - اسم الملف على الملف - FIXED';if(d.files.length==0){area.innerHTML='<div style="background:#fff;border:3px dashed #000;border-radius:10px;padding:20px;text-align:center">📁 FILE: modules/json_copy.py - لا يوجد JSON بعد<br><br><button class="btn btn-green" onclick="doJsonCreate()" style="padding:14px">📗 FILE: modules/json_copy.py - إنشاء JSON عينة الآن - اسم الملف على الملف - FIXED</button></div>';}else{let html='';d.files.forEach((f,idx)=>{let taId='jsonTA_'+f.id+'_'+idx;let btnId='copyBtn_'+f.id+'_'+idx;html+=`<div class="json-box"><div class="filename-header">FILE: ${f.path} - اسم الملف: ${f.name} - ${f.size} - اسم الملف على الملف - FIXED</div><div class="json-header"><span>📁 FILE: ${f.name} - ${f.size} - اسم الملف على الملف</span><button id="${btnId}_top" class="btn-copy" onclick="doCopyText('${taId}','${btnId}_top')">📋 نسخ JSON - FILE: ${f.name}</button></div><div style="background:#fff;color:#000;padding:6px;font-size:11px">📁 FILE: ${f.path} - ${f.date} - اسم الملف على الملف - FIXED</div><textarea id="${taId}" class="json-textarea" rows="12" readonly></textarea><div style="display:flex;gap:6px;padding:6px;background:#f5f5f5"><button id="${btnId}" class="btn-copy" onclick="doCopyText('${taId}','${btnId}')" style="flex:2;padding:14px">📋 نسخ JSON - FILE: ${f.name} - اسم الملف على الملف - FIXED</button><button class="btn" style="background:#fff;border:2px solid #000;flex:1" onclick="let ta=document.getElementById('${taId}');ta.focus();ta.select();">📋 تحديد الكل - FILE: ${f.name}</button></div></div>`;});area.innerHTML=html;d.files.forEach((f,idx)=>{let taId='jsonTA_'+f.id+'_'+idx;let ta=document.getElementById(taId);if(ta)ta.value=f.full_content||f.preview||'';});}}).catch(e=>{if(status)status.textContent='❌ FILE: modules/json_copy.py - خطأ: '+e+' - اسم الملف على الملف - FIXED';});}
function doJsonCreate(){let status=document.getElementById('jsonStatus');if(status)status.textContent='⏳ FILE: modules/json_copy.py - جاري إنشاء JSON - اسم الملف على الملف - FIXED...';fetch('/api/json/create-sample',{method:'POST'}).then(r=>r.json()).then(d=>{if(status)status.textContent='✅ FILE: modules/json_copy.py - تم إنشاء '+d.count+' ملف JSON - '+d.files.join(', ')+' - اسم الملف على الملف - FIXED';doJsonList();}).catch(e=>{if(status)status.textContent='❌ FILE: modules/json_copy.py - خطأ إنشاء: '+e+' - اسم الملف على الملف - FIXED';});}
function doJsonCopyAll(){fetch('/api/json/list').then(r=>r.json()).then(d=>{let all='';d.files.forEach(f=>{all+='\\n\\n// FILE: '+f.path+' - اسم الملف: '+f.name+'\\n'+(f.full_content||'')+'\\n';});let ta=document.createElement('textarea');ta.value=all;ta.style.position='fixed';ta.style.left='-9999px';document.body.appendChild(ta);ta.focus();ta.select();if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(all).then(()=>{alert('✅ FILE: modules/json_copy.py - تم نسخ كل JSON - '+d.count+' ملف - اسم الملف على الملف - FIXED');}).catch(()=>{document.execCommand('copy');alert('✅ FILE: modules/json_copy.py - تم نسخ كل JSON - اسم الملف على الملف - FIXED');});}else{document.execCommand('copy');alert('✅ FILE: modules/json_copy.py - تم نسخ كل JSON - اسم الملف على الملف - FIXED');}document.body.removeChild(ta);}).catch(e=>{alert('❌ FILE: modules/json_copy.py - خطأ نسخ كل JSON: '+e+' - اسم الملف على الملف - FIXED');});}
function doTransCreate(){let idx=document.getElementById('topicSel').value;let custom=document.getElementById('customTitle').value;let desc=document.getElementById('customDesc').value;let dur=document.getElementById('videoDuration').value;let includeMono=document.getElementById('includeMono').checked;let status=document.getElementById('transStatus');if(status)status.textContent='⏳ FILE: modules/translation.py - جاري ترجمة - اسم الملف على الملف - FIXED...';fetch('/api/translate/create',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({topic_idx:parseInt(idx),custom_title:custom,custom_desc:desc,duration:parseInt(dur),include_mono:includeMono})}).then(r=>r.json()).then(d=>{if(status)status.textContent='✅ FILE: modules/translation.py - '+d.title+' - '+d.duration+'د - '+d.progress+'% - '+d.status+' - اسم الملف على الملف - FIXED';doTransList();doJsonList();}).catch(e=>{if(status)status.textContent='❌ FILE: modules/translation.py - خطأ ترجمة: '+e+' - اسم الملف على الملف - FIXED';});}
function doTransList(){let area=document.getElementById('transListArea');fetch('/api/translate/list').then(r=>r.json()).then(d=>{if(d.trans.length==0){area.innerHTML='📁 FILE: modules/translation.py - لا يوجد فيديو مترجم بعد - اسم الملف على الملف - FIXED';}else{area.innerHTML=d.trans.map(x=>{return `<div style="border:2px solid #800080;border-radius:8px;padding:6px;margin:4px 0;background:${x.progress>=100?'#F5F0FF':'#fff'}"><div class="filename-header">FILE: ${x.json||'modules/translation.py'} - اسم الملف على الملف - ${x.title.slice(0,20)}</div><b>🌍 FILE: modules/translation.py - ${x.title.slice(0,40)}... - ${x.duration||60}د - 20 لغة - ${x.progress}%</b><br><span style="font-size:11px">${x.status.slice(0,120)}...</span><br>${x.json?`<div style="margin-top:4px"><span style="font-size:10px">📁 FILE: ${x.json} - اسم الملف على الملف</span><br><button class="btn-copy" onclick="doJsonList();document.getElementById('jsonListArea').scrollIntoView({behavior:'smooth'})">📋 FILE: modules/json_copy.py - اذهب لمكان النسخ - اسم الملف على الملف - FIXED</button></div>`:''}</div>`;}).join('');}}).catch(e=>{area.innerHTML='❌ FILE: modules/translation.py - خطأ: '+e+' - اسم الملف على الملف - FIXED';});}
function doChannel(){fetch('/api/channel/real').then(r=>r.json()).then(d=>{let el=document.getElementById('channelInfo');if(el)el.textContent=d.title? '☑️ FILE: core/channel.py - '+d.title+' - '+d.subs+' مشترك - اسم الملف على الملف - FIXED':'⏳ FILE: core/channel.py - '+(d.s||'❌ API_KEY')+' - اسم الملف على الملف - FIXED';}).catch(e=>{});}
document.addEventListener('DOMContentLoaded',()=>{setTimeout(()=>{doLoadKeys();doCheckKeys();doChannel();doJsonList();doTransList();},500);setInterval(doChannel,15000);setInterval(doJsonList,10000);});
</script></body></html>
    """

@app.route('/')
def index():
    html = load_html()
    resp = Response(html, mimetype='text/html')
    resp.headers['Cache-Control']='no-store, no-cache, must-revalidate, max-age=0'
    resp.headers['Pragma']='no-cache'
    return resp

@app.route('/api/keys/save', methods=['POST'])
def keys_save():
    try:
        data=request.get_json()
        vault.update(data)
        return jsonify({"count":vault.count(),"status":"success"})
    except Exception as e:
        return jsonify({"error":str(e)}),500

@app.route('/api/keys/status')
def keys_status():
    return jsonify(vault.status())

@app.route('/api/keys/show')
def keys_show():
    return jsonify(vault.all())

@app.route('/api/channel/real')
def channel_real():
    return jsonify(fetch_channel())

@app.route('/api/channel/videos')
def channel_videos():
    return jsonify({"videos":VIDEOS})

@app.route('/api/json/list')
def json_list():
    return jsonify(list_json_files())

@app.route('/api/json/create-sample', methods=['POST'])
def json_create_sample():
    result = create_sample_json()
    return jsonify(result)

@app.route('/api/translate/create', methods=['POST'])
def trans_create():
    d=request.get_json()
    job=create_translation_job(d.get('topic_idx',0),d.get('custom_title',''),d.get('custom_desc',''),d.get('custom_tags',''),d.get('duration',60),d.get('include_mono',True),d.get('mono_idx',0),d.get('montage','cinematic'),d.get('camera','sony_a7s3'),d.get('angle','aerial_god'),d.get('intro','product_hook'),d.get('persuasion','story_tartaria_mono'))
    return jsonify(job)

@app.route('/api/translate/list')
def trans_list():
    return jsonify({"trans":list_trans()})

@app.route('/api/factory/create', methods=['POST'])
def factory_create():
    d=request.get_json()
    job=create_factory_job(d.get('topic_idx',0),d.get('custom_title',''),d.get('duration',60),d.get('mono_idx',0),d.get('montage','cinematic'),d.get('camera','sony_a7s3'),d.get('angle','aerial_god'),d.get('intro','product_hook'),d.get('persuasion','story_tartaria_mono'))
    return jsonify(job)

@app.route('/api/factory/list')
def factory_list():
    return jsonify({"factory":list_factory()})

@app.route('/api/files')
def files_list():
    return jsonify({"files":list_files()})

@app.route('/health')
def health():
    return f"FILE: app.py - اسم الملف: app.py - v98 PROFESSIONAL - اسم الملف على الملف - احترافي مقسم كل ملف <400 سطر - {vault.count()}/5 - FILE: app.py - اسم الملف على الملف - PROFESSIONAL"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
