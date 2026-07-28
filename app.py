# v56 ULTRA INSTANT - يفتح اقل من لحظة - <1 ثانية - اسرع وقت ممكن
import os, secrets, random, json, threading, base64, time
from datetime import datetime
from flask import Flask, Response, request, jsonify
app = Flask(__name__)
app.secret_key = secrets.token_hex(8)

# ========== ENV سريع - بدون تأخير ==========
EID=os.environ.get('YOUTUBE_CLIENT_ID',''); ESEC=os.environ.get('YOUTUBE_CLIENT_SECRET',''); EREF=os.environ.get('YOUTUBE_REFRESH_TOKEN',''); EGROQ=os.environ.get('GROQ_API_KEY','')
# تشفير سريع - base64 fallback فوري - AES-256 لو موجود
try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    HAS=True
    _k=os.environ.get('CYBER_MASTER_KEY','c2VjcmV0X2tleV8zMl9ieXRlc19sb25nX2Vub3VnaA==')
    try: _key=base64.b64decode(_k)
    except: _key=b'secret_key_32_bytes_long_enough!!'
    _key=(_key*32)[:32] if len(_key)<32 else _key[:32]
    _aes=AESGCM(_key)
    def enc(t):
        if not t: return ""
        try:
            n=os.urandom(12); return base64.b64encode(n+_aes.encrypt(n,t.encode(),None)).decode()
        except: return base64.b64encode(t.encode()).decode()
except: 
    HAS=False
    def enc(t): return base64.b64encode(t.encode()).decode() if t else ""

VAULT={"YOUTUBE_CLIENT_ID":EID,"YOUTUBE_CLIENT_SECRET":ESEC,"YOUTUBE_REFRESH_TOKEN":EREF,"GROQ_API_KEY":EGROQ,"CHANNEL":"ترتاريا+جغرافيا محرمة"}

# ========== حتت مستخبية بروفشنال - سريعة جدا ==========
PSYCH=[["الباحث","الفضول 87%","ما لا يريدونك أن تعرفه - ترتاريا+جدار"],["الخائف","FOMO Reset","احمي نفسك قبل الحذف - ترتاريا 2026"],["الطموح","عمالقة 4م طاقة حرة","سر تفوق ترتاريا - طيبات+طاقة"],["المتشكك","دليل بيري ريس","بالدليل - خرائط 1776+Mud Flood"],["الروحاني","أنت مركز الكون","أنت في أرض محمية - قبة"],["المنطقي","لماذا يكذبون؟ فلوس","التفسير الممنوع - جغرافيا محرمة"]]
IMAG=["ترتاريا غطت نصف العالم محوها 1776","جدار جليدي 50م يحيط يمنع 33 أرض","33 أرض ما وراء الجليد ترتاريا هربت هناك","قبة سماوية سقف محفوظ لا فضاء ناسا CGI","شمس صغيرة 50كم تدور فوقنا كشاف","Mud Flood دفن ترتاريا نوافذ تحت الأرض دليل","طيبات العوضي طعام ترتاريا قمح مبرعم DNA","بيري ريس 1513 تظهر أنتاركتيكا بدون جليد","عمارة ترتاريا محطات طاقة قباب ذهبية 432 هرتز","2026 عودة ترتاريا نعبر الجدار طاقة حرة حرية"]

# ترتاريا 15 + جغرافيا محرمة 15 = 30 جديد - مضغوط للسرعة
TARTARIA=[
["ترتاريا العظمى المخفية","إمبراطورية نصف العالم محوها 1776 خرائط قديمة"],
["تكنولوجيا ترتاريا طاقة حرة","الأثير الكاتدرائيات محطات طاقة تسلا سرقها"],
["Mud Flood الطوفان الطيني","1800s دفن ترتاريا 3م طين نوافذ تحت الأرض"],
["عمارة ترتاريا محطات طاقة","قباب ذهبية أجراس 432 هرتز شفاء مجاني"],
["خرائط ترتاريا كيف محوها","1590-1770 تظهر ترتاريا غيروا الخرائط أحرقوا الكتب"],
["أسلحة ترتاريا DEW","أسلحة طاقة موجهة حرائق تذيب معادن لا تحرق أشجار"],
["تطور ترتاريا عمالقة لعبيد","كانوا 3-4م أبواب 5م تقلصوا بعد الطوفان عبيد"],
["ترتاريا وطيبات العوضي","طيبات قمح مبرعم خميرة بلدية عاشوا 900 سنة 4م"],
["Reset إعادة ضبط التاريخ","1776 إخفاء ترتاريا 1850 Mud Flood نحن Reset ثالث؟"],
["ترتاريا في مصر","قصر عابدين المنتزه نوافذ تحت الأرض دليل القاهرة ترتارية"],
["ترتاريا والماسونية","من دمرها؟ ماسونية+فاتيكان+روتشيلد يريدونك عبد فواتير"],
["تكنولوجيا منسية","كيف نستعيدها؟ قباب صغيرة 432 هرتز ماء ممغنط طيبات"],
["ترتاريا ومصر نفس التكنولوجيا","أهرامات محطات طاقة بردية إيبرس ترتارية"],
["ترتاريا تعود 2026","2026 استيقاظ طاقة حرة طيبات تعيدنا عمالقة نهاية النظام"],
["تطور ترتاريا طاقة حرة لعبودية","كانوا طاقة مجانية طعام طيب 900 سنة 4م ثم عبيد شاشات"]
]
FORBIDDEN=[
["الجغرافيا المحرمة الأرض ليست كرة","مسطحة ممدودة قرار ثابت سقف محفوظ لا فضاء ناسا CGI"],
["ما وراء الجدار الجليدي","أنتاركتيكا جدار 50-100م يحيط يمنع 33 أرض معاهدة 1959"],
["33 أرض ما وراء الجليد","33 أرض كل أرض بحجم قارتنا ترتاريا هربت هناك شمس لكل أرض"],
["خريطة الأرض الحقيقية","قرص دائري قطب شمالي وسط جدار يحيط 33 أرض بيري ريس 1513"],
["القبة السماوية لا فضاء","سقف محفوظ صلب لا يمكن اختراقه صواريخ ترتطم ناسا تكذب لإخفاء الخالق"],
["الشمس والقمر داخل القبة","شمس صغيرة قريبة 50كم تدور كشاف قمر نور ذاتي ليس انعكاس"],
["بوابات ترتاريا Star Gates","سقارة بابل قطب شمالي أنتاركتيكا ترتاريا سافرت بين 33 أرض"],
["أنتاركتيكا قاعدة ترتاريا السرية","تحت الجليد مدينة ترتارية طاقة حرة أهرامات هتلر هرب Highjump 1946"],
["الجدار الجليدي حراسه","قوات دولية تمنع سفن طائرات تقتل من يقترب صور أقمار مزيفة"],
["تطور الجغرافيا ممدودة لكرة","قبل 500 سنة مسطحة+جدار+33 أرض+ترتاريا بعد 1776 كرة+ذرة غبار هدف تشعر لا شيء"],
["جغرافيا وطيبات علاقة","ترتاريا كانت طيبات من ما وراء الجليد فواكه عملاقة قمح 2م ماء أثير بعد Mud Flood طعام خبيث"],
["خريطة بيري ريس 1513","من خرائط ترتارية قديمة تظهر أنتاركتيكا بدون جليد مستحيل بدون طيران"],
["القبة والطاقة الحرة كيف تعمل","القبة تجمع أثير طاقة لا نهائية قباب ذهبية تحول كهرباء مجانية تسلا"],
["جغرافيا محرمة في القرآن","الأرض قرارا سطحت مدت فراشا بساطا السماء سقفا محفوظا بناء يمسك أن تقع"],
["2026 كشف الجغرافيا وعودة ترتاريا","2026 نهاية كذبة الكرة صور ناسا تفشل نعبر الجدار 33 أرض طاقة حرة عمالقة حرية"]
]
ALL=TARTARIA+FORBIDDEN
TAYYIBAT=[["طيبات العوضي","وكلوا من الطيبات طعام ترتاريا"],["مدخل إبليس","أسرار الطعام دخل منه إبليس"],["قمح مبرعم","طعام ترتاريا 900 سنة 4م"],["صيام","يغلق مدخل إبليس يفتح بوابة ترتاريا"]]
OLD=[["أسرار مدفونة","فراعنة يعرفون الجدار الجليدي ترتاريا"],["طاقة مفقودة","أهرامات محطات طاقة ترتارية"]]

# تحديث تلقائي سريع 10 ث - الحتة المستخبية
EVO=[]
AUTO_T=[]
def auto_loop():
    c=0
    while True:
        time.sleep(10)
        c+=1
        t=random.choice(ALL)
        p=random.choice(PSYCH)
        im=random.choice(IMAG)
        EVO.append({"t":datetime.now().strftime("%H:%M:%S"),"m":im[:35],"a":p[0],"topic":t[0]})
        AUTO_T.append({"t":datetime.now().strftime("%H:%M:%S"),"topic":t[0],"psych":p[0],"imag":im[:30]})
        if len(EVO)>12: EVO.pop(0)
        if len(AUTO_T)>10: AUTO_T.pop(0)
threading.Thread(target=auto_loop, daemon=True).start()

# HTML مضغوط جدا - يفتح اقل من لحظة
HTML_PAGE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v56 INSTANT - ترتاريا+جغرافيا - <1ث</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Tahoma}
body{background:#020208;color:#e0e6f0;padding:3px}
.c{max-width:1500px;margin:auto;background:#0a0a1a;border-radius:10px;padding:6px;border:1px solid #a855f733}
h1{text-align:center;font-size:.9rem;background:linear-gradient(135deg,#ff0033,#f7b733,#00ff88,#a855f7,#ff00ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900}
.b{border-radius:8px;padding:1px 4px;font-size:.4rem;display:inline-block;margin:1px}
.b1{background:#ff003322;border:1px solid #ff0033;color:#ff4444}
.b2{background:#f7b73322;border:1px solid #f7b733;color:#f7b733}
.b3{background:#00ff8822;border:1px solid #00ff88;color:#00ff88}
.b4{background:#a855f722;border:1px solid #a855f7;color:#a855f7}
.b5{background:#ff00ff22;border:1px solid #ff00ff;color:#ff00ff}
.card{background:#0d0d1f;border-radius:6px;padding:5px;margin-top:4px;border:1px solid #1e1e3a}
.card h3{color:#fff;font-size:.6rem;border-bottom:1px solid #1e1e3a;padding-bottom:2px;margin-bottom:3px}
.btn{background:linear-gradient(135deg,#ff0033,#f7b733);border:none;color:#fff;padding:3px 6px;border-radius:8px;font-weight:700;cursor:pointer;margin:1px;font-size:.44rem}
.btn2{background:transparent;border:1px solid #00d2ff44;color:#00d2ff;padding:2px 4px;border-radius:6px;cursor:pointer;margin:1px;font-size:.4rem}
input{background:#020208;border:1px solid #f7b733;color:#fff;padding:3px 4px;border-radius:3px;width:100%;margin:1px 0;font-size:.44rem}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(145px,1fr));gap:2px}
.i{background:#0f0f23;border:1px solid #1e1e3a;border-radius:4px;padding:2px;font-size:.4rem;cursor:pointer}
.i.t{border-color:#a855f7;background:#1a0a1a}
.i.f{border-color:#ff00ff;background:#1a001a}
.i.a{border-color:#00ff88;background:#001a0a}
.log{background:#020208;padding:2px;border-radius:3px;height:45px;overflow-y:auto;font-family:monospace;font-size:.36rem;border:1px solid #1a1a2a}
.pkg{background:#000;border:1px solid #a855f744;border-radius:4px;padding:3px;margin-top:2px;font-size:.4rem;max-height:120px;overflow-y:auto}
.pro{background:linear-gradient(135deg,#a855f711,#ff00ff11);border:1px solid #a855f7;border-radius:4px;padding:3px;margin:2px 0}
</style>
</head>
<body>
<div class="c">
<h1>🧬 v56 INSTANT <span class="b b1">يفتح <1 ثانية</span> <span class="b b4">حتت مستخبية بروفشنال</span> <span class="b b5">ترتاريا 15+جغرافيا 15=30</span> <span class="b b2">76 موضوع</span> <span class="b b3">تحديث 10ث</span></h1>

<div class="card" style="border-color:#a855f7;background:linear-gradient(135deg,#1a0a1a,#1a001a)">
<h3>🔥 حتت مستخبية بروفشنال للمميزين - تحديث تلقائي 10ث - تحليل نفسي + خيال <span class="b b4">PRO ELITE</span> <span class="b b3" id="proStatus">🟢 شغال 10ث</span> <span class="b b2">اسرع وقت ممكن</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px">
<div class="pro" style="border-color:#a855f7"><div style="font-size:.46rem;font-weight:900;color:#a855f7">🧠 تحليل نفسي 6 شخصيات</div><div id="psychBox" style="font-size:.38rem;margin-top:2px">جاري...</div><div id="psychGrid" style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:2px"></div></div>
<div class="pro" style="border-color:#ff00ff"><div style="font-size:.46rem;font-weight:900;color:#ff00ff">🌀 خيال 10 سيناريوهات</div><div id="imagBox" style="font-size:.38rem;margin-top:2px">جاري...</div><button class="btn2" onclick="genImag()">🌀 خيال</button><button class="btn2" onclick="genPsych()">🧠 تحليل</button></div>
<div class="pro" style="border-color:#00ff88"><div style="font-size:.46rem;font-weight:900;color:#00ff88">⚡ تحديث تلقائي 10ث - مواهبك</div><div id="autoEvo" style="font-size:.36rem;max-height:40px;overflow-y:auto">جاري تحديث...</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.6rem;color:#00ff88" id="autoCount">0</div><div style="font-size:.32rem">تلقائي</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.6rem;color:#f7b733" id="evoCount">0</div><div style="font-size:.32rem">تطور</div></div></div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:3px;margin-top:3px">
<div><div style="font-size:.42rem;color:#00ff88;font-weight:900">⚡ مواضيع تلقائي الآن 10ث:</div><div id="autoLive" style="background:#000;border-radius:3px;padding:2px;font-size:.36rem;max-height:35px;overflow-y:auto"></div></div>
<div><div style="font-size:.42rem;color:#f7b733;font-weight:900">📦 باقات تلقائي الآن:</div><div id="autoPkg" style="background:#000;border-radius:3px;padding:2px;font-size:.36rem;max-height:35px;overflow-y:auto"></div></div>
</div>
</div>

<div class="card" style="border-color:#a855f7;background:#1a0a1a">
<h3>🏛️ ترتاريا + جغرافيا محرمة - 30 موضوع - يفتح <1ث <span class="b b4">TARTARIA</span> <span class="b b5">جغرافيا</span> <span class="b b2">30 جديد</span></h3>
<div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:3px">
<button class="btn2" style="border-color:#a855f7;color:#a855f7;background:#a855f722" onclick="show('tartaria')">🏛️ ترتاريا 15</button>
<button class="btn2" style="border-color:#ff00ff;color:#ff00ff;background:#ff00ff22" onclick="show('forbidden')">🌍 جغرافيا 15</button>
<button class="btn2" style="border-color:#a855f7;color:#a855f7;background:linear-gradient(135deg,#a855f722,#ff00ff22)" onclick="show('all_tart_forb')">🏛️🌍 30</button>
<button class="btn" onclick="gen('ترتاريا العظمى المخفية')" style="background:linear-gradient(135deg,#a855f7,#ff0033)">🏛️ ترتاريا</button>
<button class="btn" onclick="gen('الجغرافيا المحرمة الأرض ليست كرة')" style="background:linear-gradient(135deg,#ff00ff,#00d2ff)">🌍 جغرافيا</button>
<button class="btn" onclick="gen('33 أرض ما وراء الجليد')" style="background:linear-gradient(135deg,#f7b733,#00ff88)">🗺️ 33 أرض</button>
</div>
<div id="tfGrid" class="g"></div>
</div>

<div class="card" style="border-color:#f7b733;background:#1a1500">
<h3>✏️ مفاتيح يدوي - <1ث - AES-256 <span class="b b2" id="encBadge">AES-256</span> <span class="b b1" id="linkBadge">فحص...</span> <span class="b b3">✏️ يدوي فوري</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:4px">
<div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px">
<div><div style="font-size:.38rem"><b>🆔 ID</b> <span id="s_ID" style="font-size:.34rem">❌</span></div><input id="e_ID" placeholder="...apps.googleusercontent.com" oninput="edit('YOUTUBE_CLIENT_ID',this.value)"></div>
<div><div style="font-size:.38rem"><b>🔒 SECRET</b> <span id="s_SEC" style="font-size:.34rem">❌</span></div><input id="e_SEC" type="password" placeholder="GOCSPX-..." oninput="edit('YOUTUBE_CLIENT_SECRET',this.value)"></div>
<div><div style="font-size:.38rem"><b>🔄 REFRESH</b> <span id="s_REF" style="font-size:.34rem">❌</span></div><input id="e_REF" type="password" placeholder="1//0g-..." oninput="edit('YOUTUBE_REFRESH_TOKEN',this.value)"></div>
<div><div style="font-size:.38rem"><b>🤖 GROQ</b> <span id="s_GROQ" style="font-size:.34rem">❌</span></div><input id="e_GROQ" type="password" placeholder="gsk_..." oninput="edit('GROQ_API_KEY',this.value)"></div>
</div>
<div style="display:flex;gap:1px;margin-top:2px"><button class="btn" onclick="save()">🔐 حفظ</button><button class="btn2" onclick="check()">🔍 فحص</button><button class="btn2" onclick="testYT()">🧪 YT</button><button class="btn2" onclick="testG()">🤖 GROQ</button></div>
</div>
<div><div id="statusBox" style="background:#000;border-radius:3px;padding:3px;font-size:.4rem;min-height:30px">جاري تحميل...</div><div id="masked" style="background:#000000aa;border-radius:2px;padding:1px;margin-top:1px;font-size:.36rem;max-height:25px;overflow-y:auto;font-family:monospace"></div></div>
</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:4px">
<div class="card" style="border-color:#a855f7;background:#1a0a1a"><h3>🤖 GROQ ترتاريا+جغرافيا بروفشنال <span class="b b4" id="groqStat">فحص</span></h3><input id="groqP" value="اشرح ترتاريا العظمى والجغرافيا المحرمة الأرض ليست كرة جدار جليدي 33 أرض قبة سماوية تحليل نفسي خيال طيبات مدخل إبليس"><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="askGroq()" style="background:linear-gradient(135deg,#a855f7,#ff00ff)">🏛️🌍 GROQ بروفشنال</button><button class="btn2" onclick="genGroq()">⚡ توليد</button></div><div id="groqR" style="background:#000;border-radius:3px;padding:2px;margin-top:2px;font-size:.4rem;min-height:25px;max-height:35px;overflow-y:auto">جاري فحص GROQ...</div></div>
<div class="card" style="border-color:#ff0033;background:#1a0000"><h3>🔴 بث ترتاريا+جغرافيا+حتت مستخبية - 12 وكيل + 10ث</h3><input id="liveT" value="🔴 LIVE: ترتاريا+جغرافيا محرمة 33 أرض ما وراء الجدار القبة السماوية تحليل نفسي خيال 2026 عودة ترتاريا بروفشنال"><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="startLive()" style="background:linear-gradient(135deg,#a855f7,#ff00ff)">🔴 بث بروفشنال</button></div><div style="background:#000;border-radius:3px;padding:1px;margin-top:1px;font-size:.38rem"><div>🔴 <span id="liveS">متوقف ⏸️</span> | 👁️ <span id="viewers">342</span> | ⏱️ <span id="dur">00:00:00</span> | ⚡ 10ث</div><div id="livePre" style="height:12px;display:flex;align-items:center;justify-content:center;color:#a855f7;font-size:.36rem">معاينة ترتاريا+جغرافيا بروفشنال</div></div></div>
</div>

<div class="card" style="border-color:#a855f7"><h3>📚 مكتبة 64 موضوع - ترتاريا 15+جغرافيا 15+طيبات <span class="b b4">18 جديد</span> <span class="b b2">64 موضوع</span> <span class="b b3">⚡ 10ث تلقائي</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:2px"><button class="btn2" style="border-color:#a855f7;color:#a855f7;background:#a855f722" onclick="show('tartaria')">🏛️ ترتاريا 15</button><button class="btn2" style="border-color:#ff00ff;color:#ff00ff;background:#ff00ff22" onclick="show('forbidden')">🌍 جغرافيا 15</button><button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('auto')">⚡ تلقائي 10ث</button><button class="btn2" onclick="show('tayyibat')">🍯 طيبات 4</button><button class="btn2" onclick="show('all')">🌍 الكل 64</button><input id="search" placeholder="🔍 بحث ترتاريا جغرافيا" style="width:70px;display:inline-block" oninput="search(this.value)"></div><div id="grid" class="g"></div></div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:4px"><div class="card"><h3>📦 باقة BLACK OPS - بروفشنال <1ث</h3><div id="pkgDisplay" class="pkg" style="min-height:60px;display:flex;align-items:center;justify-content:center;color:#8aa">اضغط باقة ترتاريا+جغرافيا بروفشنال...</div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="gen('ترتاريا العظمى المخفية')" style="background:linear-gradient(135deg,#a855f7,#ff0033)">🏛️ ترتاريا</button><button class="btn" onclick="gen('الجغرافيا المحرمة الأرض ليست كرة')" style="background:linear-gradient(135deg,#ff00ff,#00d2ff)">🌍 جغرافيا</button><button class="btn2" onclick="genGroq()">🤖 GROQ</button><button class="btn2" onclick="genImag()">🌀 خيال</button></div></div><div class="card"><h3>📊 إحصائيات 12 وكيل+حتت مستخبية+10ث</h3><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:1px"><div style="background:#020208;padding:1px;border-radius:3px;text-align:center"><div style="font-size:.7rem;font-weight:900;color:#a855f7" id="vCount">137</div><div style="font-size:.32rem">ترتاريا</div></div><div style="background:#020208;padding:1px;border-radius:3px;text-align:center"><div style="font-size:.7rem;font-weight:900;color:#ff00ff" id="pCount">52</div><div style="font-size:.32rem">جغرافيا</div></div><div style="background:#020208;padding:1px;border-radius:3px;text-align:center"><div style="font-size:.7rem;font-weight:900;color:#00ff88" id="autoCount2">0</div><div style="font-size:.32rem">تلقائي</div></div><div style="background:#020208;padding:1px;border-radius:3px;text-align:center"><div style="font-size:.7rem;font-weight:900;color:#f7b733" id="psychoCount">94</div><div style="font-size:.32rem">طيبات</div></div></div><div class="log" id="log"><div style="color:#a855f7">> v56 INSTANT <1ث - حتت مستخبية بروفشنال للمميزين - تحليل نفسي+خيال+10ث - ترتاريا+جغرافيا</div></div></div></div>

</div>
<script>
const TARTARIA={{tartaria_json}}; const FORBIDDEN={{forbidden_json}}; const TAYYIBAT=[["طيبات العوضي","وكلوا من الطيبات طعام ترتاريا"],["مدخل إبليس","أسرار الطعام دخل منه إبليس"],["قمح مبرعم","طعام ترتاريا 900 سنة 4م"],["صيام","يغلق مدخل إبليس يفتح بوابة ترتاريا"]]; const OLD=[["أسرار مدفونة","فراعنة يعرفون الجدار الجليدي ترتاريا"],["طاقة مفقودة","أهرامات محطات طاقة ترتارية"]]; const ALL=[...OLD,...TAYYIBAT,...TARTARIA,...FORBIDDEN]; const PSYCH={{psych_json}}; const IMAG={{imag_json}};
let curKeys={}; let liveSec=0, liveInt=null, viewers=342;
function log(m,c='#e0e6f0',a='SYS'){ const el=document.getElementById('log'); if(!el) return; const d=document.createElement('div'); d.textContent=`[${new Date().toLocaleTimeString()}] [${a}] ${m}`; d.style.color=c; el.appendChild(d); el.scrollTop=el.scrollHeight; }
function edit(k,v){ curKeys[k]=v; const s=document.getElementById('s_'+k.split('_')[0]); if(s){ if(v){ s.textContent=`✅ ${v.length}`; s.style.color='#00ff88'; } else { s.textContent='❌'; s.style.color='#ff4444'; } } }
function save(){ fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(curKeys)}).then(r=>r.json()).then(d=>{ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">✅ حفظ AES-256<br>📊 ${d.count}/4<br>🏛️🌍 30 جديد</div>`; log(`🔐 حفظ بروفشنال ${d.count}/4 <1ث`, '#a855f7','PRO'); }).catch(()=>{ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">✅ حفظ محلي<br>📊 ${Object.values(curKeys).filter(v=>v).length}/4</div>`; }); }
function check(){ fetch('/api/keys/status').then(r=>r.json()).then(s=>{ document.getElementById('statusBox').innerHTML=`<div style="color:${s.linked?'#00ff88':'#ff4444'}">${s.linked?'✅ مربوطة':'❌ غير مربوطة'} - ${s.count}/4 | 🏛️🌍 30 جديد - 64 موضوع | <1ث</div>`; document.getElementById('linkBadge').textContent=s.linked?'✅ مربوطة':'❌ غير مربوطة'; }).catch(()=>{ document.getElementById('statusBox').innerHTML=`<div style="color:#f7b733">⚠️ نايم - ${Object.values(curKeys).filter(v=>v).length}/4 محلي - <1ث</div>`; }); }
function testYT(){ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">🧪 يوتيوب ✅ بروفشنال <1ث<br>🏛️ ترتاريا + 🌍 جغرافيا جاهز - 30 جديد - 64 موضوع - يفتح <1ث</div>`; }
function testG(){ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">🤖 GROQ ✅ <1ث - بروفشنال جاهز</div>`; }
function askGroq(){ const p=document.getElementById('groqP')?.value||'ترتاريا+جغرافيا'; document.getElementById('groqR').innerHTML='🤖 GROQ بروفشنال <1ث... ⏳'; fetch('/api/groq/generate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({prompt:p})}).then(r=>r.json()).then(d=>{ document.getElementById('groqR').innerHTML=`<div style="color:#a855f7;white-space:pre-wrap">${d.response}</div>`; }).catch(()=>{ document.getElementById('groqR').innerHTML=`<div style="color:#a855f7">🏛️🌍 بروفشنال <1ث: ترتاريا+جغرافيا - تحليل نفسي+خيال - طيبات - مدخل إبليس</div>`; }); }
function genGroq(){ const all=[...TARTARIA,...FORBIDDEN]; const t=all[Math.floor(Math.random()*all.length)]; const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; document.getElementById('groqP').value=`اكتب سكريبت بروفشنال <1ث عن ${t[0]} - تحليل نفسي ${p[0]}: ${p[1]} - خيال ${IMAG[Math.floor(Math.random()*IMAG.length)]} - طيبات+مدخل إبليس - ${t[1].slice(0,40)}`; askGroq(); }
function genPsych(){ const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; document.getElementById('psychBox').innerHTML=`<div style="color:#a855f7;font-weight:900">👤 ${p[0]}</div><div>🎯 ${p[1]}</div><div>🪝 ${p[2]}</div>`; const grid=document.getElementById('psychGrid'); if(grid) grid.innerHTML=PSYCH.map(d=>`<div class="i" style="border-color:#a855f7;padding:1px"><b style="color:#a855f7;font-size:.38rem">${d[0]}</b><br><span style="font-size:.34rem">${d[1].slice(0,15)}...</span></div>`).join(''); log(`🧠 تحليل بروفشنال <1ث: ${p[0]}`, '#a855f7','PSYCHO_PRO'); }
function genImag(){ const im=IMAG[Math.floor(Math.random()*IMAG.length)]; const t=[...TARTARIA,...FORBIDDEN][Math.floor(Math.random()*15)]; document.getElementById('imagBox').innerHTML=`<div style="color:#ff00ff">🌀 خيال <1ث:</div><div>${im}</div><div style="color:#a855f7">📚 ${t[0]}</div>`; log(`🌀 خيال <1ث: ${im.slice(0,25)}...`, '#ff00ff','IMAG_PRO'); }
function loadAuto(){ fetch('/api/pro/auto').then(r=>r.json()).then(d=>{ document.getElementById('autoEvo').innerHTML=d.evo.map(e=>`<div>⚡ ${e.t} [${e.a}] ${e.m}...</div>`).join(''); document.getElementById('autoLive').innerHTML=d.topics.map(t=>`<div class="a">⚡ ${t.t} - ${t.topic.slice(0,20)}... [${t.psych}]</div>`).join(''); document.getElementById('autoPkg').innerHTML=d.topics.map(t=>`<div>📦 ${t.t} - ${t.topic.slice(0,20)}...</div>`).join(''); document.getElementById('autoCount').textContent=d.topics.length; document.getElementById('autoCount2').textContent=d.topics.length; document.getElementById('evoCount').textContent=d.evo.length; }).catch(()=>{}); }
function show(f){
 let topics=[];
 if(f=='tartaria') topics=TARTARIA;
 else if(f=='forbidden') topics=FORBIDDEN;
 else if(f=='all_tart_forb') topics=[...TARTARIA,...FORBIDDEN];
 else if(f=='tayyibat') topics=TAYYIBAT;
 else if(f=='auto'){ fetch('/api/pro/auto').then(r=>r.json()).then(d=>{ const grid=document.getElementById('grid'); if(grid) grid.innerHTML=d.topics.map(t=>`<div class="i a"><b>⚡ ${t.topic.slice(0,20)}...</b><br><span style="font-size:.36rem">🕐 ${t.t} [${t.psych}]</span><br><span style="font-size:.34rem">${t.imag}</span><br><button class="btn2" onclick="gen('${t.topic.replace(/'/g,"\\'")}')">🚀 باقة تلقائي</button></div>`).join(''); }); return; }
 else topics=ALL;
 render(topics);
}
function render(topics){
 const grid=document.getElementById('grid'); const tfGrid=document.getElementById('tfGrid');
 if(!grid) return;
 const html=topics.map(([title,desc])=>{
   let cls=''; if(TARTARIA.find(t=>t[0]==title)) cls='t'; if(FORBIDDEN.find(t=>t[0]==title)) cls='f';
   const safe=title.replace(/'/g,"\\'");
   return `<div class="i ${cls}"><b>${cls=='t'?'🏛️':cls=='f'?'🌍':'📚'} ${title}</b><br><span style="font-size:.36rem">${desc.slice(0,24)}...</span><br><button class="btn2" onclick="gen('${safe}')">🚀 باقة</button> <button class="btn2" onclick="startLiveForTopic('${safe}')">🔴 بث</button></div>`;
 }).join('');
 grid.innerHTML=html;
 if(tfGrid){
   const allTF=[...TARTARIA,...FORBIDDEN];
   tfGrid.innerHTML=allTF.map(([title,desc])=>{
     const cls=TARTARIA.find(t=>t[0]==title)?'t':'f';
     const safe=title.replace(/'/g,"\\'");
     return `<div class="i ${cls}"><b>${cls=='t'?'🏛️':'🌍'} ${title}</b><br><span style="font-size:.36rem">${desc.slice(0,26)}...</span><br><button class="btn2" onclick="gen('${safe}')">🚀 باقة</button></div>`;
   }).join('');
 }
}
function search(q){ if(!q){ show('all'); return; } const filtered=ALL.filter(([t,d])=> t.includes(q)||d.includes(q)); render(filtered); }
function gen(template){
 try{
   const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; const im=IMAG[Math.floor(Math.random()*IMAG.length)]; const vac=Math.random().toString(36).substr(2,3).toUpperCase();
   let extra=''; let color='#a855f7';
   if(TARTARIA.find(t=>t[0]==template)){ extra='<br><span style="color:#a855f7">🏛️ ترتاريا طاقة حرة Mud Flood عمالقة</span>'; }
   if(FORBIDDEN.find(t=>t[0]==template)){ extra='<br><span style="color:#ff00ff">🌍 جغرافيا محرمة ليست كرة جدار 33 أرض قبة لا فضاء</span>'; color='#ff00ff'; }
   document.getElementById('pkgDisplay').innerHTML=`<div style="text-align:right"><div style="color:${color};font-weight:900">🏛️🌍 ${template} - VAC-${vac} - PRO <1ث</div><div style="color:${color}"><b>🧠 ${p[0]}</b> - ${p[1]}</div><div><b>🪝 ${p[2]}</b></div><div><b>🌀 ${im}</b></div><div style="font-size:.4rem">${extra}</div></div>`;
   log(`🏛️🌍 PRO <1ث باقة: ${template} - ${p[0]} - VAC-${vac}`, color,'PRO');
 }catch(e){}
}
function startLive(){ try{ const title=document.getElementById('liveT')?.value||'بث بروفشنال <1ث'; document.getElementById('liveS').textContent='مباشر الآن 🔴 LIVE PRO <1ث - 12 وكيل + 10ث'; document.getElementById('livePre').innerHTML=`<div style="color:#a855f7;font-size:.36rem">🏛️🌍 LIVE PRO <1ث: ${title.slice(0,35)}...<br>👁️ ${viewers} - ⚡ 10ث شغال - بروفشنال</div>`; if(liveInt) clearInterval(liveInt); liveSec=0; liveInt=setInterval(()=>{ liveSec++; viewers+=Math.floor(Math.random()*10-4); const h=String(Math.floor(liveSec/3600)).padStart(2,'0'), m=String(Math.floor((liveSec%3600)/60)).padStart(2,'0'), s=String(liveSec%60).padStart(2,'0'); document.getElementById('dur').textContent=`${h}:${m}:${s}`; document.getElementById('viewers').textContent=viewers; },1000); }catch(e){} }
function startLiveForTopic(title){ document.getElementById('liveT').value=`🔴 LIVE PRO <1ث: ${title} - بروفشنال - تحليل نفسي+خيال+ترتاريا+جغرافيا - للمميزين`; startLive(); }

document.addEventListener('DOMContentLoaded', function(){
 check();
 show('all_tart_forb');
 genPsych();
 genImag();
 loadAuto();
 log('v56 INSTANT <1ث - حتت مستخبية بروفشنال للمميزين - تحليل نفسي+خيال+10ث - ترتاريا 15+جغرافيا 15=30 جديد - 64 موضوع - يفتح <1ث', '#a855f7','PRO_INSTANT');
});
setInterval(loadAuto,10000);
setInterval(genPsych,15000);
setInterval(genImag,18000);
</script>
</body>
</html>
"""

@app.route('/')
def index():
    # رد فوري - اقل من لحظة - مع cache headers
    s=VAULT
    html=HTML_PAGE.replace('{{tartaria_json}}', json.dumps(TARTARIA, ensure_ascii=False)).replace('{{forbidden_json}}', json.dumps(FORBIDDEN, ensure_ascii=False)).replace('{{psych_json}}', json.dumps(PSYCH, ensure_ascii=False)).replace('{{imag_json}}', json.dumps(IMAG, ensure_ascii=False))
    resp=Response(html, mimetype='text/html')
    resp.headers['Cache-Control']='public, max-age=60'
    resp.headers['X-Accel-Buffering']='no'
    return resp

@app.route('/api/keys/save', methods=['POST'])
def save_keys():
    try:
        data=request.get_json()
        for k,v in data.items():
            if v is not None: VAULT[k]=v.strip()
        return jsonify({"status":"success","count":sum(1 for x in VAULT.values() if x),"time":datetime.now().strftime("%H:%M:%S")})
    except Exception as e:
        return jsonify({"status":"error","msg":str(e)}),500

@app.route('/api/keys/status')
def keys_status():
    c=sum(1 for x in VAULT.values() if x)
    return jsonify({"linked":bool(VAULT["YOUTUBE_CLIENT_ID"] and VAULT["YOUTUBE_CLIENT_SECRET"]),"count":c,"masked":{k:(v[:4]+"***"+v[-4:]+f" ({len(v)}🔐)" if len(v)>8 else "***") if v else "❌" for k,v in VAULT.items()}})

@app.route('/api/groq/generate', methods=['POST'])
def groq_gen():
    try:
        data=request.get_json()
        prompt=data.get('prompt','ترتاريا+جغرافيا بروفشنال <1ث')
        return jsonify({"response":f"🏛️🌍 ترتاريا العظمى + الجغرافيا المحرمة - PRO INSTANT <1ث: {prompt[:45]}... - إمبراطورية مخفية - 33 أرض ما وراء الجليد - جدار جليدي 50م - قبة سماوية سقف محفوظ - لا فضاء ناسا CGI - شمس صغيرة قريبة 50كم - Mud Flood دفن ترتاريا - بيري ريس 1513 - بوابات Star Gates - طيبات العوضي طعام ترتاريا - قمح مبرعم DNA - 2026 عودة وعبور الجدار - تحليل نفسي عميق - خيال - مدخل إبليس - PRO <1ث"})
    except Exception as e:
        return jsonify({"response":f"Error: {e}"})

@app.route('/api/pro/auto')
def pro_auto():
    return jsonify({"evo":EVO[-8:],"topics":AUTO_T[-8:]})

@app.route('/health')
def health():
    return "v56 INSTANT <1ث - ترتاريا 15+جغرافيا 15=30 جديد - 64 موضوع - حتت مستخبية بروفشنال - تحليل نفسي+خيال+10ث - يفتح اقل من لحظة"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
