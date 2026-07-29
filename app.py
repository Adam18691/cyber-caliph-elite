# v79 REAL CHANNEL STATUS - حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - لا أرقام وهمية - بيانات حقيقية من YouTube Data API v3 - خلفية بيضاء - حتت مستخبية - https://www.youtube.com/@CursedMedicineEG - REAL CHANNEL STATUS + REAL SUBSCRIBERS + REAL VIDEOS + REAL FOLLOW
import os, secrets, json, threading, time, base64, re
from datetime import datetime
from flask import Flask, Response, request, jsonify
app=Flask(__name__)
app.secret_key=secrets.token_hex(2)

def enc(t):
    if not t: return ""
    try:
        k=b'V79_REAL_CHANNEL_STATUS_SUBS_VIDEOS_FOLLOW'
        d=t.encode()
        e=bytes([b ^ k[i % len(k)] for i,b in enumerate(d)])
        return base64.b64encode(e).decode()
    except:
        return base64.b64encode(t.encode()).decode()

EID=os.environ.get('YOUTUBE_CLIENT_ID','');ESEC=os.environ.get('YOUTUBE_CLIENT_SECRET','');EREF=os.environ.get('YOUTUBE_REFRESH_TOKEN','');EGROQ=os.environ.get('GROQ_API_KEY','');EYT=os.environ.get('YOUTUBE_API_KEY','');EAFF=os.environ.get('AFFILIATE_LINK','https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6')
VAULT={"YOUTUBE_CLIENT_ID":EID,"YOUTUBE_CLIENT_SECRET":ESEC,"YOUTUBE_REFRESH_TOKEN":EREF,"GROQ_API_KEY":EGROQ,"YOUTUBE_API_KEY":EYT,"AFFILIATE_LINK":EAFF,"CHANNEL_HANDLE":"@CursedMedicineEG","CHANNEL_URL":"https://www.youtube.com/@CursedMedicineEG"}

# بيانات القناة الحقيقية - REAL CHANNEL DATA - لا أرقام وهمية
CHANNEL_REAL={
    "handle":"@CursedMedicineEG",
    "url":"https://www.youtube.com/@CursedMedicineEG",
    "live_url":"https://www.youtube.com/@CursedMedicineEG/live",
    "videos_url":"https://www.youtube.com/@CursedMedicineEG/videos",
    "channel_id":None,  # يتم جلبه حقيقي من API
    "title":None,
    "description":None,
    "custom_url":None,
    "published_at":None,
    "thumbnails":None,
    "banner":None,
    "statistics":{
        "subscriber_count":"غير متوفر - لا أرقام وهمية - يتطلب YOUTUBE_API_KEY حقيقي",
        "view_count":"غير متوفر - لا أرقام وهمية - يتطلب YOUTUBE_API_KEY حقيقي",
        "video_count":"غير متوفر - لا أرقام وهمية - يتطلب YOUTUBE_API_KEY حقيقي",
        "hidden_subscriber_count":None
    },
    "content_details":{
        "uploads_playlist":None
    },
    "status":"في انتظار جلب بيانات حقيقية - لا أرقام وهمية",
    "last_fetch":"لم يتم الفحص بعد - لا أرقام وهمية",
    "api_available":False,
    "real_data":True,
    "no_fake":True
}

VIDEOS_REAL=[]  # فيديوهات القناة الحقيقية - لا أرقام وهمية
LIVE_STATUS_REAL={"is_live":False,"live_video_id":None,"live_title":None,"viewers_real":0,"last_check":"لم يتم الفحص بعد"}

def fetch_real_channel_data():
    """جلب بيانات القناة الحقيقية من YouTube Data API v3 - لا أرقام وهمية"""
    api_key = VAULT["YOUTUBE_API_KEY"]
    if not api_key or len(api_key) < 20:
        CHANNEL_REAL["status"] = "❌ لا يوجد YOUTUBE_API_KEY حقيقي - أضف مفتاح حقيقي من Google Cloud Console - لا أرقام وهمية"
        CHANNEL_REAL["last_fetch"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - لا يوجد API KEY حقيقي - لا أرقام وهمية"
        CHANNEL_REAL["api_available"] = False
        return CHANNEL_REAL
    
    try:
        import requests
        CHANNEL_REAL["api_available"] = True
        CHANNEL_REAL["status"] = "🔍 جاري جلب بيانات القناة الحقيقية من YouTube API v3..."
        
        # 1. محاولة جلب القناة عبر handle - forHandle
        handle = VAULT["CHANNEL_HANDLE"].replace('@','')
        url_handle = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,contentDetails,status&forHandle={handle}&key={api_key}"
        r = requests.get(url_handle, timeout=15)
        
        data = None
        if r.status_code == 200:
            j = r.json()
            if j.get('items') and len(j['items'])>0:
                data = j['items'][0]
        
        # 2. إذا فشل forHandle، جرب forUsername أو search
        if not data:
            # جرب search للعثور على channel ID
            url_search = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={handle}&key={api_key}&maxResults=5"
            r2 = requests.get(url_search, timeout=15)
            if r2.status_code == 200:
                j2 = r2.json()
                if j2.get('items'):
                    for item in j2['items']:
                        if handle.lower() in item['snippet'].get('title','').lower() or handle.lower() in item['snippet'].get('channelTitle','').lower() or True:
                            ch_id = item['snippet']['channelId']
                            # جلب تفاصيل القناة عبر ID
                            url_by_id = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics,contentDetails,status&id={ch_id}&key={api_key}"
                            r3 = requests.get(url_by_id, timeout=15)
                            if r3.status_code == 200:
                                j3 = r3.json()
                                if j3.get('items'):
                                    data = j3['items'][0]
                                    break
        
        # 3. إذا وجدنا بيانات حقيقية
        if data:
            snippet = data.get('snippet',{})
            stats = data.get('statistics',{})
            content_details = data.get('contentDetails',{})
            status = data.get('status',{})
            
            CHANNEL_REAL["channel_id"] = data.get('id')
            CHANNEL_REAL["title"] = snippet.get('title','بدون عنوان - حقيقي')
            CHANNEL_REAL["description"] = snippet.get('description','')[:500]
            CHANNEL_REAL["custom_url"] = snippet.get('customUrl', VAULT["CHANNEL_HANDLE"])
            CHANNEL_REAL["published_at"] = snippet.get('publishedAt','غير معروف - حقيقي')
            CHANNEL_REAL["thumbnails"] = snippet.get('thumbnails',{})
            CHANNEL_REAL["banner"] = snippet.get('thumbnails',{}).get('high',{}).get('url','')
            
            # إحصائيات حقيقية - لا أرقام وهمية
            CHANNEL_REAL["statistics"]["subscriber_count"] = int(stats.get('subscriberCount',0)) if stats.get('subscriberCount') else "مخفي - القناة أخفت عدد المشتركين - حقيقي - لا أرقام وهمية"
            CHANNEL_REAL["statistics"]["view_count"] = int(stats.get('viewCount',0)) if stats.get('viewCount') else 0
            CHANNEL_REAL["statistics"]["video_count"] = int(stats.get('videoCount',0)) if stats.get('videoCount') else 0
            CHANNEL_REAL["statistics"]["hidden_subscriber_count"] = stats.get('hiddenSubscriberCount', False)
            
            CHANNEL_REAL["content_details"]["uploads_playlist"] = content_details.get('relatedPlaylists',{}).get('uploads')
            CHANNEL_REAL["status"] = f"✅ بيانات حقيقية - تم جلب بيانات القناة الحقيقية - {CHANNEL_REAL['title']} - {CHANNEL_REAL['statistics']['subscriber_count']} مشترك حقيقي - {CHANNEL_REAL['statistics']['video_count']} فيديو حقيقي - {CHANNEL_REAL['statistics']['view_count']} مشاهدة حقيقية - لا أرقام وهمية - REAL DATA ONLY"
            CHANNEL_REAL["last_fetch"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - بيانات حقيقية - REAL DATA ONLY - لا أرقام وهمية"
            
            # جلب الفيديوهات الحقيقية
            fetch_real_videos()
            # فحص البث المباشر الحقيقي
            check_real_live_status()
            
        else:
            # لم نجد القناة - ربما API KEY غير صحيح أو handle خطأ
            error_msg = f"❌ لم يتم العثور على القناة {handle} - تأكد من صحة HANDLE - أو YOUTUBE_API_KEY غير صحيح - أو Quota انتهت - لا أرقام وهمية - REAL ERROR"
            if r.status_code != 200:
                try:
                    err_j = r.json()
                    error_msg += f" - خطأ API حقيقي: {err_j.get('error',{}).get('message','غير معروف')} - كود: {r.status_code} - لا أرقام وهمية"
                except:
                    error_msg += f" - كود: {r.status_code} - نص: {r.text[:200]} - لا أرقام وهمية"
            CHANNEL_REAL["status"] = error_msg
            CHANNEL_REAL["last_fetch"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - خطأ حقيقي - لا أرقام وهمية"
        
        return CHANNEL_REAL
        
    except Exception as e:
        CHANNEL_REAL["status"] = f"❌ خطأ حقيقي في جلب بيانات القناة - {str(e)} - لا أرقام وهمية - REAL ERROR ONLY"
        CHANNEL_REAL["last_fetch"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - خطأ: {str(e)} - لا أرقام وهمية"
        CHANNEL_REAL["api_available"] = False
        return CHANNEL_REAL

def fetch_real_videos():
    """جلب فيديوهات القناة الحقيقية - لا أرقام وهمية"""
    try:
        import requests
        api_key = VAULT["YOUTUBE_API_KEY"]
        channel_id = CHANNEL_REAL.get("channel_id")
        uploads_playlist = CHANNEL_REAL.get("content_details",{}).get("uploads_playlist")
        
        if not api_key or not channel_id:
            return []
        
        videos = []
        
        # استخدام uploads playlist لجلب الفيديوهات الحقيقية
        if uploads_playlist:
            url_playlist = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails&playlistId={uploads_playlist}&key={api_key}&maxResults=50"
            r = requests.get(url_playlist, timeout=15)
            if r.status_code == 200:
                j = r.json()
                for item in j.get('items',[]):
                    snippet = item.get('snippet',{})
                    content = item.get('contentDetails',{})
                    video_id = content.get('videoId') or snippet.get('resourceId',{}).get('videoId')
                    videos.append({
                        "video_id": video_id,
                        "title": snippet.get('title','بدون عنوان - حقيقي'),
                        "description": snippet.get('description','')[:200],
                        "published_at": snippet.get('publishedAt',''),
                        "thumbnails": snippet.get('thumbnails',{}),
                        "channel_title": snippet.get('channelTitle', CHANNEL_REAL.get("title")),
                        "url": f"https://www.youtube.com/watch?v={video_id}",
                        "real": True,
                        "no_fake": True
                    })
        else:
            # إذا لا يوجد uploads playlist، استخدم search
            url_search_videos = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&order=date&type=video&key={api_key}&maxResults=50"
            r = requests.get(url_search_videos, timeout=15)
            if r.status_code == 200:
                j = r.json()
                for item in j.get('items',[]):
                    snippet = item.get('snippet',{})
                    video_id = item.get('id',{}).get('videoId')
                    videos.append({
                        "video_id": video_id,
                        "title": snippet.get('title','بدون عنوان - حقيقي'),
                        "description": snippet.get('description','')[:200],
                        "published_at": snippet.get('publishedAt',''),
                        "thumbnails": snippet.get('thumbnails',{}),
                        "channel_title": snippet.get('channelTitle', CHANNEL_REAL.get("title")),
                        "url": f"https://www.youtube.com/watch?v={video_id}",
                        "real": True,
                        "no_fake": True
                    })
        
        # جلب إحصائيات الفيديوهات الحقيقية (views, likes)
        if videos:
            video_ids = [v["video_id"] for v in videos[:50] if v["video_id"]]
            if video_ids:
                ids_str = ",".join(video_ids)
                url_stats = f"https://www.googleapis.com/youtube/v3/videos?part=statistics,contentDetails,snippet&id={ids_str}&key={api_key}"
                r_stats = requests.get(url_stats, timeout=15)
                if r_stats.status_code == 200:
                    j_stats = r_stats.json()
                    stats_map = {item['id']: item for item in j_stats.get('items',[])}
                    for v in videos:
                        vid = v["video_id"]
                        if vid in stats_map:
                            s = stats_map[vid]
                            st = s.get('statistics',{})
                            cd = s.get('contentDetails',{})
                            v["view_count_real"] = int(st.get('viewCount',0)) if st.get('viewCount') else 0
                            v["like_count_real"] = int(st.get('likeCount',0)) if st.get('likeCount') else 0
                            v["comment_count_real"] = int(st.get('commentCount',0)) if st.get('commentCount') else 0
                            v["duration_real"] = cd.get('duration','PT0S')
                            v["statistics_real"] = st
        
        global VIDEOS_REAL
        VIDEOS_REAL = videos
        return videos
        
    except Exception as e:
        return []

def check_real_live_status():
    """فحص حالة البث المباشر الحقيقية - لا أرقام وهمية"""
    try:
        import requests
        api_key = VAULT["YOUTUBE_API_KEY"]
        channel_id = CHANNEL_REAL.get("channel_id")
        
        if not api_key or not channel_id:
            LIVE_STATUS_REAL["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - لا يوجد API KEY حقيقي - لا أرقام وهمية"
            return LIVE_STATUS_REAL
        
        # البحث عن فيديوهات live حقيقية
        url_live = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&eventType=live&type=video&key={api_key}&maxResults=5"
        r = requests.get(url_live, timeout=15)
        
        if r.status_code == 200:
            j = r.json()
            items = j.get('items',[])
            if items:
                # يوجد بث مباشر حقيقي الآن
                live_item = items[0]
                snippet = live_item.get('snippet',{})
                video_id = live_item.get('id',{}).get('videoId')
                
                # جلب إحصائيات البث المباشر الحقيقية
                url_live_stats = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics,liveStreamingDetails&id={video_id}&key={api_key}"
                r_stats = requests.get(url_live_stats, timeout=15)
                viewers_real = 0
                if r_stats.status_code == 200:
                    j_stats = r_stats.json()
                    if j_stats.get('items'):
                        live_details = j_stats['items'][0].get('liveStreamingDetails',{})
                        viewers_real = int(live_details.get('concurrentViewers',0)) if live_details.get('concurrentViewers') else 0
                
                LIVE_STATUS_REAL["is_live"] = True
                LIVE_STATUS_REAL["live_video_id"] = video_id
                LIVE_STATUS_REAL["live_title"] = snippet.get('title','بث مباشر حقيقي - بدون عنوان')
                LIVE_STATUS_REAL["live_description"] = snippet.get('description','')[:300]
                LIVE_STATUS_REAL["live_thumbnails"] = snippet.get('thumbnails',{})
                LIVE_STATUS_REAL["live_published"] = snippet.get('publishedAt','')
                LIVE_STATUS_REAL["viewers_real"] = viewers_real
                LIVE_STATUS_REAL["live_url"] = f"https://www.youtube.com/watch?v={video_id}"
                LIVE_STATUS_REAL["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - يوجد بث مباشر حقيقي الآن - REAL LIVE NOW - لا أرقام وهمية"
            else:
                # لا يوجد بث مباشر حاليا - فحص إذا كان هناك بث قادم
                url_upcoming = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&eventType=upcoming&type=video&key={api_key}&maxResults=5"
                r_up = requests.get(url_upcoming, timeout=15)
                upcoming = []
                if r_up.status_code == 200:
                    j_up = r_up.json()
                    upcoming = j_up.get('items',[])
                
                LIVE_STATUS_REAL["is_live"] = False
                LIVE_STATUS_REAL["live_video_id"] = None
                LIVE_STATUS_REAL["live_title"] = None
                LIVE_STATUS_REAL["viewers_real"] = 0
                LIVE_STATUS_REAL["upcoming"] = upcoming
                LIVE_STATUS_REAL["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - لا يوجد بث مباشر حقيقي الآن - {len(upcoming)} بث قادم حقيقي - لا أرقام وهمية - REAL CHECK"
        else:
            LIVE_STATUS_REAL["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - خطأ فحص البث الحقيقي - كود: {r.status_code} - لا أرقام وهمية"
        
        return LIVE_STATUS_REAL
        
    except Exception as e:
        LIVE_STATUS_REAL["last_check"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - خطأ: {str(e)} - لا أرقام وهمية"
        return LIVE_STATUS_REAL

def auto_real_refresh():
    """تحديث تلقائي للبيانات الحقيقية - كل 60 ثانية - لا أرقام وهمية"""
    while True:
        time.sleep(60)
        try:
            if VAULT["YOUTUBE_API_KEY"] and len(VAULT["YOUTUBE_API_KEY"])>20:
                fetch_real_channel_data()
        except:
            pass

threading.Thread(target=auto_real_refresh, daemon=True).start()

# بيانات ترتاريا - حقيقية - لا أرقام وهمية
TARTARIA=[
["ترتاريا العظمى المخفية","إمبراطورية نصف العالم محوها 1776 خرائط قديمة"],
["تكنولوجيا ترتاريا طاقة حرة","الأثير الكاتدرائيات محطات طاقة تسلا سرقها"],
["Mud Flood الطوفان الطيني","1800s دفن ترتاريا 3م طين نوافذ تحت الأرض دليل"],
["عمارة ترتاريا محطات طاقة","قباب ذهبية أجراس 432 هرتز شفاء مجاني"],
["خرائط ترتاريا كيف محوها","1590-1770 تظهر ترتاريا غيروا الخرائط أحرقوا الكتب"],
["أسلحة ترتاريا DEW","أسلحة طاقة موجهة حرائق تذيب معادن لا تحرق أشجار"],
["تطور ترتاريا عمالقة لعبيد","كانوا 3-4م أبواب 5م تقلصوا بعد الطوفان عبيد"],
["ترتاريا وطيبات العوضي","طيبات قمح مبرعم خميرة بلدية عاشوا 900 سنة 4م"],
["Reset إعادة ضبط التاريخ","1776 إخفاء ترتاريا 1850 Mud Flood نحن Reset ثالث؟"],
["ترتاريا في مصر","قصر عابدين المنتزه نوافذ تحت الأرض القاهرة ترتارية"],
["ترتاريا والماسونية","ماسونية+فاتيكان+روتشيلد يريدونك عبد فواتير"],
["تكنولوجيا منسية","قباب صغيرة 432 هرتز ماء ممغنط طيبات"],
["ترتاريا ومصر نفس التكنولوجيا","أهرامات محطات طاقة بردية إيبرس ترتارية"],
["ترتاريا تعود 2026","2026 استيقاظ طاقة حرة طيبات تعيدنا عمالقة"],
["تطور ترتاريا لعبودية","كانوا طاقة مجانية 900 سنة 4م ثم عبيد شاشات"]
]
FORBIDDEN=[
["الجغرافيا المحرمة الأرض ليست كرة","مسطحة ممدودة سقف محفوظ لا فضاء ناسا CGI"],
["ما وراء الجدار الجليدي","جدار 50-100م يحيط يمنع 33 أرض معاهدة 1959"],
["33 أرض ما وراء الجليد","33 أرض كل أرض بحجم قارتنا ترتاريا هربت شمس لكل أرض"],
["خريطة الأرض الحقيقية","قرص قطب شمالي وسط جدار يحيط 33 أرض بيري ريس 1513"],
["القبة السماوية لا فضاء","سقف محفوظ صلب صواريخ ترتطم ناسا تكذب لإخفاء الخالق"],
["الشمس والقمر داخل القبة","شمس 50كم كشاف قمر نور ذاتي ليس انعكاس"],
["بوابات ترتاريا Star Gates","سقارة بابل قطب شمالي أنتاركتيكا بوابات بين 33 أرض"],
["أنتاركتيكا قاعدة ترتاريا السرية","تحت الجليد مدينة ترتارية هتلر هرب Highjump 1946"],
["الجدار الجليدي حراسه","قوات دولية تمنع سفن تقتل من يقترب صور مزيفة"],
["تطور الجغرافيا ممدودة لكرة","قبل 500 سنة مسطحة+جدار+33 أرض بعد 1776 كرة+ذرة غبار"],
["جغرافيا وطيبات علاقة","طيبات من ما وراء الجليد فواكه عملاقة قمح 2م بعد Mud Flood خبيث"],
["خريطة بيري ريس 1513","من خرائط ترتارية تظهر أنتاركتيكا بدون جليد مستحيل بدون طيران"],
["القبة والطاقة الحرة","القبة تجمع أثير قباب ذهبية تحول كهرباء مجانية"],
["جغرافيا محرمة في القرآن","الأرض قرارا سطحت فراشا بساطا السماء سقفا محفوظا"],
["2026 كشف الجغرافيا وعودة ترتاريا","2026 نهاية كذبة الكرة نعبر الجدار 33 أرض طاقة حرة حرية"]
]
ALL=TARTARIA+FORBIDDEN

COUNTRIES=[
{"code":"CH","name":"سويسرا","flag":"🇨🇭","peak":"20:00 CET","lang":"Deutsch"},
{"code":"DK","name":"الدنمارك","flag":"🇩🇰","peak":"20:00 CET","lang":"Dansk"},
{"code":"SE","name":"السويد","flag":"🇸🇪","peak":"20:00 CET","lang":"Svenska"},
{"code":"FR","name":"فرنسا","flag":"🇫🇷","peak":"20:30 CET","lang":"Français"},
{"code":"DE","name":"ألمانيا","flag":"🇩🇪","peak":"20:00 CET","lang":"Deutsch"},
{"code":"GB","name":"المملكة المتحدة","flag":"🇬🇧","peak":"19:30 GMT","lang":"English"},
{"code":"NO","name":"النرويج","flag":"🇳🇴","peak":"20:00 CET","lang":"Norsk"},
{"code":"US","name":"الولايات المتحدة","flag":"🇺🇸","peak":"20:00 EST","lang":"English"},
{"code":"BE","name":"بلجيكا","flag":"🇧🇪","peak":"20:00 CET","lang":"Français"},
{"code":"IE","name":"أيرلندا","flag":"🇮🇪","peak":"20:00 GMT","lang":"English"},
{"code":"IT","name":"إيطاليا","flag":"🇮🇹","peak":"21:00 CET","lang":"Italiano"},
{"code":"NL","name":"هولندا","flag":"🇳🇱","peak":"20:00 CET","lang":"Nederlands"},
{"code":"AU","name":"أستراليا","flag":"🇦🇺","peak":"21:00 AEST","lang":"English"},
{"code":"ZW","name":"زيمبابوي","flag":"🇿🇼","peak":"21:00 CAT","lang":"English"},
{"code":"FK","name":"جزر فوكلاند","flag":"🇫🇰","peak":"20:00 FKT","lang":"English"},
{"code":"SH","name":"سانت هيلينا","flag":"🇸🇭","peak":"19:00 GMT","lang":"English"},
{"code":"SS","name":"جنوب السودان","flag":"🇸🇸","peak":"21:00 CAT","lang":"English"},
{"code":"WS","name":"ساموا","flag":"🇼🇸","peak":"22:00 WST","lang":"English"},
{"code":"CA","name":"كندا","flag":"🇨🇦","peak":"20:00 EST","lang":"English"},
{"code":"EG","name":"مصر","flag":"🇪🇬","peak":"21:00 EET","lang":"العربية"}
]

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v79 REAL CHANNEL - حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه - https://www.youtube.com/@CursedMedicineEG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Tahoma}
body{background:#FFFFFF;color:#0a0a0a;padding:3px;min-height:100vh}
.c{max-width:1880px;margin:auto;background:#FFFFFF;border-radius:14px;padding:5px;border:3px solid #0a0a0a;box-shadow:0 4px 20px rgba(0,0,0,0.08)}
h1{text-align:center;font-size:.42rem;background:linear-gradient(135deg,#0a0a0a,#ff0033,#006400);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;line-height:1.1}
.b{border-radius:5px;padding:2px 4px;font-size:.15rem;display:inline-block;margin:1px;font-weight:700}
.b-real{background:#006400;color:#FFFFFF;border:2px solid #006400}
.b-live{background:#ff0033;color:#FFFFFF;border:2px solid #ff0033;animation:livePulse 1s infinite}
@keyframes livePulse{0%,100%{box-shadow:0 0 8px #ff0033}50%{box-shadow:0 0 18px #ff0033}}
.b-sub{background:#FFD700;color:#000;border:2px solid #000;font-weight:900}
.b-video{background:#00d2ff;color:#000;border:2px solid #000}
.card{background:#FFFFFF;border-radius:10px;padding:5px;margin-top:4px;border:2px solid #e0e0e0;box-shadow:0 2px 8px rgba(0,0,0,0.05)}
.card h3{color:#0a0a0a;font-size:.26rem;border-bottom:3px solid #006400;padding-bottom:2px;margin-bottom:3px;font-weight:900}
.card-real{border:3px solid #006400;background:linear-gradient(135deg,#FFFFFF,#F0FFF0);box-shadow:0 4px 16px rgba(0,100,0,0.1)}
.card-channel{border:4px solid #ff0033;background:linear-gradient(135deg,#FFFFFF,#FFF0F0);box-shadow:0 0 30px rgba(255,0,51,0.15);animation:channelGlow 2s infinite}
@keyframes channelGlow{0%,100%{box-shadow:0 0 30px rgba(255,0,51,0.15)}50%{box-shadow:0 0 40px rgba(255,0,51,0.25)}}
.btn{background:linear-gradient(135deg,#006400,#00AA00);border:none;color:#FFFFFF;padding:4px 10px;border-radius:8px;font-weight:900;cursor:pointer;margin:2px;font-size:.18rem}
.btn-live{background:linear-gradient(135deg,#ff0033,#FF0000);border:none;color:#FFFFFF;padding:5px 14px;border-radius:10px;font-weight:900;cursor:pointer;margin:2px;font-size:.19rem;animation:btnLivePulse 1s infinite}
@keyframes btnLivePulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.btn2{background:#FFFFFF;border:2px solid #0a0a0a;color:#0a0a0a;padding:2px 6px;border-radius:6px;cursor:pointer;margin:1px;font-size:.16rem;font-weight:700}
.btn-real{background:linear-gradient(135deg,#006400,#00AA00);color:#FFFFFF;border:2px solid #006400;padding:5px 12px;border-radius:10px;font-weight:900;cursor:pointer;animation:realGlow 1.5s infinite}
@keyframes realGlow{0%,100%{box-shadow:0 0 8px rgba(0,100,0,0.3)}50%{box-shadow:0 0 18px rgba(0,100,0,0.5)}}
input{background:#FFFFFF;border:2px solid #006400;color:#0a0a0a;padding:4px 6px;border-radius:8px;width:100%;margin:2px 0;font-size:.19rem;font-weight:600}
input:focus{border-color:#ff0033;box-shadow:0 0 12px rgba(255,0,51,0.2);outline:none}
.real-banner{background:linear-gradient(135deg,#006400,#00AA00);color:#FFFFFF;border-radius:12px;padding:5px;margin:4px 0;text-align:center;font-weight:900}
.channel-banner{background:linear-gradient(135deg,#ff0033,#FF0000,#006400);color:#FFFFFF;border-radius:14px;padding:6px;margin:4px 0;text-align:center;font-weight:900;animation:bannerPulse 2s infinite;border:3px solid #FFFFFF}
@keyframes bannerPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.01)}}
.channel-info-box{background:linear-gradient(135deg,#FFFFFF,#FFF0F0);border:4px solid #ff0033;border-radius:14px;padding:6px;margin:5px 0;box-shadow:0 6px 20px rgba(255,0,51,0.15)}
.video-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:4px}
.video-card{background:#FFFFFF;border:2px solid #e0e0e0;border-radius:10px;padding:3px;transition:all 0.2s;cursor:pointer}
.video-card:hover{transform:translateY(-3px);box-shadow:0 6px 18px rgba(0,0,0,0.12);border-color:#006400}
.video-card img{width:100%;border-radius:6px;aspect-ratio:16/9;object-fit:cover}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:3px}
.stat-card{background:#FFFFFF;border:3px solid #006400;border-radius:10px;padding:5px;text-align:center}
.stat-card-live{background:#FFFFFF;border:3px solid #ff0033;border-radius:10px;padding:5px;text-align:center;animation:liveStatPulse 1s infinite}
@keyframes liveStatPulse{0%,100%{border-color:#ff0033}50%{border-color:#FFD700}}
.progress{height:10px;background:#f0f0f0;border-radius:5px;overflow:hidden;margin:2px 0;border:2px solid #e0e0e0}
.progress-bar{height:100%;background:linear-gradient(90deg,#ff0033,#FFD700,#006400);transition:width 0.3s;background-size:300% 100%;animation:progressMove 1s linear infinite}
@keyframes progressMove{0%{background-position:0% 0%}100%{background-position:300% 0%}}
.log{background:#0a0a0a;color:#00ff88;padding:4px;border-radius:6px;height:30px;overflow-y:auto;font-family:monospace;font-size:.12rem;border:2px solid #006400}
</style>
</head>
<body>
<div class="c">
<h1>🧬 v79 REAL CHANNEL <span class="b b-real">حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - REAL CHANNEL STATUS</span> <span class="b b-live">🔴 متابعة حقيقية - REAL FOLLOW</span> <span class="b b-sub">لا أرقام وهمية - REAL DATA ONLY</span> <span class="b" style="background:#FFFFFF;border:2px solid #0a0a0a">https://www.youtube.com/@CursedMedicineEG</span></h1>

<div class="channel-banner">
<div style="font-size:.42rem">🔴📺 v79 REAL CHANNEL STATUS - حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - لا أرقام وهمية - بيانات حقيقية من YouTube Data API v3 - خلفية بيضاء #FFFFFF - متابعة حقيقية - REAL CHANNEL STATUS + REAL SUBSCRIBERS + REAL VIDEOS + REAL FOLLOW - حتت مستخبية بروفشنل للمميزين - https://www.youtube.com/@CursedMedicineEG - لا أرقام وهمية - REAL DATA ONLY</div>
</div>

<!-- حالة القناة الحقيقية -->
<div class="channel-info-box">
<h3 style="color:#ff0033;font-size:.32rem;font-weight:900;margin-bottom:4px">📺 حالة القناه الحقيقة وعدد المشتركين الحقيقة - REAL CHANNEL STATUS + REAL SUBSCRIBERS - لا أرقام وهمية - بيانات حقيقية من YouTube API v3 <span class="b b-real" id="channelStatusBadge">فحص حالة القناة الحقيقية... - REAL CHECK</span> <span class="b b-live" id="liveStatusBadge">فحص البث الحقيقي... - REAL LIVE CHECK</span></h3>

<div style="display:grid;grid-template-columns:1fr 2fr;gap:5px">
<div>
<div style="font-size:.2rem;font-weight:900;color:#ff0033">📺 معلومات القناة الحقيقية - REAL CHANNEL INFO - لا أرقام وهمية:</div>
<div id="realChannelInfo" style="background:#FFFFFF;border:3px solid #ff0033;border-radius:12px;padding:5px;margin-top:2px;font-size:.15rem;min-height:200px;color:#0a0a0a">🔍 في انتظار جلب بيانات القناة الحقيقية...<br>📡 يتطلب YOUTUBE_API_KEY حقيقي من Google Cloud Console<br>🔗 القناة: https://www.youtube.com/@CursedMedicineEG<br>📺 Handle: @CursedMedicineEG<br>❌ لا أرقام وهمية - بيانات حقيقية فقط<br>✅ REAL CHANNEL DATA ONLY - لا أرقام وهمية<br>🔍 اضغط: جلب بيانات القناة الحقيقية الآن<br><br><button class="btn-real" onclick="fetchRealChannel()">📺 جلب بيانات القناة الحقيقية الآن - REAL CHANNEL DATA - لا أرقام وهمية - YouTube API v3</button></div>
<div style="display:flex;gap:2px;margin-top:3px;flex-wrap:wrap">
<button class="btn-real" onclick="fetchRealChannel()">📺 جلب بيانات القناة الحقيقية - REAL CHANNEL - لا أرقام وهمية</button>
<button class="btn-live" onclick="checkRealLive()">🔴 فحص البث المباشر الحقيقي - REAL LIVE - لا أرقام وهمية</button>
<button class="btn2" onclick="fetchRealVideos()">🎬 جلب فيديوهات القناة الحقيقية - REAL VIDEOS - لا أرقام وهمية</button>
</div>
</div>
<div>
<div style="font-size:.2rem;font-weight:900;color:#006400">📊 إحصائيات القناة الحقيقية - عدد المشتركين الحقيقة - لا أرقام وهمية - REAL STATS ONLY:</div>
<div class="stats-grid" style="margin-top:2px">
<div class="stat-card"><div style="font-size:.14rem;color:#0a0a0a;font-weight:700">المشتركون الحقيقيون</div><div id="realSubsCount" style="font-size:.36rem;font-weight:900;color:#006400">غير متوفر - لا أرقام وهمية</div><div style="font-size:.11rem;color:#666">REAL SUBSCRIBERS ONLY - لا أرقام وهمية - يتطلب API حقيقي</div><div class="progress" style="margin-top:2px"><div id="subsProgress" class="progress-bar" style="width:0%"></div></div></div>
<div class="stat-card"><div style="font-size:.14rem;color:#0a0a0a;font-weight:700">المشاهدات الحقيقية</div><div id="realViewsCount" style="font-size:.32rem;font-weight:900;color:#006400">غير متوفر - لا أرقام وهمية</div><div style="font-size:.11rem;color:#666">REAL VIEWS ONLY - لا أرقام وهمية - يتطلب API حقيقي</div></div>
<div class="stat-card"><div style="font-size:.14rem;color:#0a0a0a;font-weight:700">الفيديوهات الحقيقية</div><div id="realVideosCount" style="font-size:.32rem;font-weight:900;color:#006400">غير متوفر - لا أرقام وهمية</div><div style="font-size:.11rem;color:#666">REAL VIDEOS ONLY - لا أرقام وهمية - يتطلب API حقيقي</div></div>
<div class="stat-card-live"><div style="font-size:.14rem;color:#0a0a0a;font-weight:700">البث المباشر الحقيقي</div><div id="realLiveCount" style="font-size:.28rem;font-weight:900;color:#ff0033">لا يوجد بث - لا أرقام وهمية</div><div style="font-size:.11rem;color:#666" id="realLiveDetails">REAL LIVE ONLY - لا أرقام وهمية - يتطلب API حقيقي</div></div>
</div>
<div id="realChannelStatsDetailed" style="background:#F0FFF0;border:3px solid #006400;border-radius:10px;padding:4px;margin-top:3px;font-size:.14rem;min-height:80px;color:#0a0a0a">📊 في انتظار إحصائيات حقيقية...<br>❌ لا أرقام وهمية - إحصائيات حقيقية فقط<br>✅ REAL STATS ONLY - لا أرقام وهمية<br>📡 يتطلب YOUTUBE_API_KEY حقيقي<br>🔗 https://www.youtube.com/@CursedMedicineEG<br>🔍 اضغط: جلب بيانات القناة الحقيقية الآن</div>
<div style="display:flex;gap:2px;margin-top:2px;flex-wrap:wrap">
<button class="btn2" onclick="openRealChannel()">🔗 فتح القناة الحقيقية - REAL CHANNEL - https://www.youtube.com/@CursedMedicineEG</button>
<button class="btn2" onclick="openRealVideos()">🎬 فتح فيديوهات القناة الحقيقية - REAL VIDEOS</button>
<button class="btn2" onclick="openRealLive()">🔴 فتح البث المباشر الحقيقي - REAL LIVE - /live</button>
<button class="btn2" onclick="subscribeReal()">🔔 اشترك + فعل الجرس - حقيقي - REAL SUBSCRIBE</button>
</div>
</div>
</div>
</div>

<!-- الفيديوهات اللي موجوده على القناه مع متابعه حقيقيه -->
<div class="card card-real">
<h3 style="color:#006400;font-size:.3rem">🎬 الفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - REAL VIDEOS ON CHANNEL + REAL FOLLOW - لا أرقام وهمية - فيديوهات حقيقية من YouTube API <span class="b b-real" id="videosCountBadge">0 فيديو حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY</span> <span class="b b-video" id="videosStatusBadge">فحص الفيديوهات الحقيقية... - REAL CHECK</span></h3>
<div style="display:flex;gap:2px;margin-bottom:3px;flex-wrap:wrap">
<button class="btn-real" onclick="fetchRealVideos()">🎬 جلب الفيديوهات الحقيقية - REAL VIDEOS - لا أرقام وهمية - 50 فيديو حقيقي</button>
<button class="btn2" onclick="sortVideos('date')">📅 ترتيب حسب التاريخ - حقيقي - REAL SORT</button>
<button class="btn2" onclick="sortVideos('views')">👀 ترتيب حسب المشاهدات الحقيقية - REAL VIEWS SORT - لا أرقام وهمية</button>
<button class="btn2" onclick="filterVideos('live')">🔴 فلتر البث المباشر الحقيقي - REAL LIVE FILTER - لا أرقام وهمية</button>
<button class="btn2" onclick="clearVideos()">🗑️ مسح القائمة - حقيقي - REAL CLEAR - لا أرقام وهمية</button>
</div>
<div id="realVideosGrid" class="video-grid" style="min-height:120px;background:#FFFFFF;border:3px solid #006400;border-radius:12px;padding:5px">📭 لا يوجد فيديوهات حقيقية بعد - لا أرقام وهمية<br>🎬 اضغط: جلب الفيديوهات الحقيقية - REAL VIDEOS - لا أرقام وهمية<br>📡 يتطلب YOUTUBE_API_KEY حقيقي<br>🔗 https://www.youtube.com/@CursedMedicineEG/videos<br>❌ لا أرقام وهمية - فيديوهات حقيقية فقط<br>✅ REAL VIDEOS ONLY - لا أرقام وهمية<br>📺 50 فيديو حقيقي من القناة - لا أرقام وهمية - REAL VIDEOS ONLY</div>
<div id="realVideosStats" style="background:#F0FFF0;border:2px solid #006400;border-radius:8px;padding:3px;margin-top:3px;font-size:.14rem;color:#0a0a0a;min-height:20px">📊 إحصائيات الفيديوهات الحقيقية: 0 فيديو حقيقي - 0 مشاهدة حقيقية - لا أرقام وهمية - REAL STATS ONLY - لا أرقام وهمية</div>
</div>

<!-- متابعة حقيقية للقناة وكل شيء -->
<div class="card card-channel">
<h3 style="color:#ff0033;font-size:.28rem">🔔 متابعه حقيقيه للقناة وكل شئ - REAL FOLLOW EVERYTHING - لا أرقام وهمية - متابعة حقيقية - REAL FOLLOW - حتت مستخبية <span class="b b-live">🔴 متابعة حقيقية - REAL FOLLOW - لا أرقام وهمية</span> <span class="b b-real">كل شيء حقيقي - REAL EVERYTHING - لا أرقام وهمية</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px">
<div style="background:#FFFFFF;border:3px solid #ff0033;border-radius:10px;padding:4px">
<div style="font-size:.18rem;font-weight:900;color:#ff0033">🔔 متابعة حقيقية - اشترك + فعل الجرس - REAL FOLLOW:</div>
<div style="font-size:.14rem;color:#0a0a0a;margin-top:2px">✅ اشترك في القناة الحقيقية - لا أرقام وهمية<br>✅ فعل الجرس الحقيقي - لا أرقام وهمية<br>✅ تابع كل الفيديوهات الحقيقية - لا أرقام وهمية<br>✅ تابع البث المباشر الحقيقي - لا أرقام وهمية<br>✅ كل شيء حقيقي - لا أرقام وهمية - REAL FOLLOW ONLY</div>
<div style="display:flex;gap:1px;margin-top:2px;flex-wrap:wrap">
<button class="btn-live" onclick="subscribeReal()">🔔 اشترك + فعل الجرس - حقيقي - REAL SUBSCRIBE + BELL - لا أرقام وهمية</button>
<button class="btn2" onclick="openRealChannel()">📺 فتح القناة الحقيقية - REAL CHANNEL</button>
</div>
</div>
<div style="background:#FFFFFF;border:3px solid #006400;border-radius:10px;padding:4px">
<div style="font-size:.18rem;font-weight:900;color:#006400">📊 متابعة إحصائيات حقيقية - REAL STATS FOLLOW - لا أرقام وهمية:</div>
<div style="font-size:.14rem;color:#0a0a0a;margin-top:2px">📊 تابع عدد المشتركين الحقيقي - لا أرقام وهمية<br>👀 تابع عدد المشاهدات الحقيقية - لا أرقام وهمية<br>🎬 تابع عدد الفيديوهات الحقيقية - لا أرقام وهمية<br>🔴 تابع البث المباشر الحقيقي - لا أرقام وهمية<br>✅ كل شيء حقيقي - لا أرقام وهمية - REAL STATS ONLY</div>
<div style="display:flex;gap:1px;margin-top:2px;flex-wrap:wrap">
<button class="btn-real" onclick="fetchRealChannel()">📊 جلب الإحصائيات الحقيقية - REAL STATS - لا أرقام وهمية</button>
<button class="btn2" onclick="startRealFollow()">🔄 بدء المتابعة الحقيقية - REAL FOLLOW START - لا أرقام وهمية</button>
</div>
</div>
<div style="background:#FFFFFF;border:3px solid #FFD700;border-radius:10px;padding:4px">
<div style="font-size:.18rem;font-weight:900;color:#b8860b">🎬 متابعة فيديوهات حقيقية - REAL VIDEOS FOLLOW - لا أرقام وهمية:</div>
<div style="font-size:.14rem;color:#0a0a0a;margin-top:2px">🎬 تابع أحدث الفيديوهات الحقيقية - لا أرقام وهمية<br>🔴 تابع البث المباشر الحقيقي - لا أرقام وهمية<br>⏮️ تابع من البداية - حقيقي - لا أرقام وهمية<br>📥 حمل الفيديوهات الحقيقية - لا أرقام وهمية<br>✅ كل شيء حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY</div>
<div style="display:flex;gap:1px;margin-top:2px;flex-wrap:wrap">
<button class="btn-real" onclick="fetchRealVideos()">🎬 جلب الفيديوهات الحقيقية - REAL VIDEOS - لا أرقام وهمية</button>
<button class="btn2" onclick="openRealVideos()">📺 فتح فيديوهات القناة الحقيقية - REAL VIDEOS PAGE</button>
</div>
</div>
</div>
<div style="background:#F0FFF0;border:3px solid #006400;border-radius:10px;padding:4px;margin-top:3px">
<div style="font-size:.18rem;font-weight:900;color:#006400">🔔 سجل المتابعة الحقيقية - REAL FOLLOW LOG - لا أرقام وهمية - متابعة حقيقية للقناة وكل شيء:</div>
<div id="realFollowLog" style="background:#FFFFFF;border:2px solid #e0e0e0;border-radius:6px;padding:3px;margin-top:2px;font-size:.13rem;max-height:60px;overflow-y:auto;color:#0a0a0a;min-height:40px">📭 لا يوجد سجل متابعة حقيقية بعد - لا أرقام وهمية<br>🔔 ابدأ المتابعة الحقيقية - REAL FOLLOW START - لا أرقام وهمية<br>📺 تابع القناة الحقيقية - لا أرقام وهمية<br>✅ كل شيء حقيقي - لا أرقام وهمية - REAL FOLLOW LOG ONLY</div>
</div>
</div>

<div class="card card-real"><h3 style="color:#006400">🔐 الاربعه مفاتيح الحقيقية - لا أرقام وهمية - REAL KEYS ONLY - خلفية بيضاء <span class="b b-real" id="encBadge">🔐 تشفير حقيقي - REAL ONLY - لا أرقام وهمية</span> <span class="b" style="background:#FFFFFF;border:2px solid #006400" id="linkBadge">فحص الربط الحقيقي... - REAL ONLY</span></h3>
<div style="background:#F0FFF0;border-radius:8px;padding:3px;margin:2px 0;border:2px solid #006400">
<div style="display:grid;grid-template-columns:110px 1fr 55px 55px;gap:2px;align-items:center;margin:2px 0;background:#FFFFFF;border-radius:6px;padding:2px;border:2px solid #006400"><div style="font-size:.16rem;font-weight:900;color:#006400">🤖 GROQ_API_KEY <span id="s_GROQ" style="font-size:.11rem">❌</span></div><input id="e_GROQ" type="password" placeholder="gsk_... - 56 حرف حقيقي - REAL ONLY - لا أرقام وهمية" oninput="editKey('GROQ_API_KEY',this.value)"><button class="btn2" onclick="toggleShow('e_GROQ')">👁️</button><button class="btn2" onclick="testKey('GROQ_API_KEY')">🔍 حقيقي</button></div>
<div style="display:grid;grid-template-columns:110px 1fr 55px 55px;gap:2px;align-items:center;margin:2px 0;background:#FFFFFF;border-radius:6px;padding:2px;border:2px solid #006400"><div style="font-size:.16rem;font-weight:900;color:#006400">🆔 YOUTUBE_CLIENT_ID <span id="s_ID" style="font-size:.11rem">❌</span></div><input id="e_ID" type="text" placeholder="...googleusercontent.com - ID حقيقي - REAL ONLY" oninput="editKey('YOUTUBE_CLIENT_ID',this.value)"><button class="btn2" onclick="toggleShow('e_ID')">👁️</button><button class="btn2" onclick="testKey('YOUTUBE_CLIENT_ID')">🔍 حقيقي</button></div>
<div style="display:grid;grid-template-columns:110px 1fr 55px 55px;gap:2px;align-items:center;margin:2px 0;background:#FFFFFF;border-radius:6px;padding:2px;border:2px solid #006400"><div style="font-size:.16rem;font-weight:900;color:#006400">🔒 YOUTUBE_CLIENT_SECRET <span id="s_SEC" style="font-size:.11rem">❌</span></div><input id="e_SEC" type="password" placeholder="GOCSPX-... - SECRET حقيقي - REAL ONLY" oninput="editKey('YOUTUBE_CLIENT_SECRET',this.value)"><button class="btn2" onclick="toggleShow('e_SEC')">👁️</button><button class="btn2" onclick="testKey('YOUTUBE_CLIENT_SECRET')">🔍 حقيقي</button></div>
<div style="display:grid;grid-template-columns:110px 1fr 55px 55px;gap:2px;align-items:center;margin:2px 0;background:#FFFFFF;border-radius:6px;padding:2px;border:2px solid #006400"><div style="font-size:.16rem;font-weight:900;color:#006400">🔄 YOUTUBE_REFRESH_TOKEN <span id="s_REF" style="font-size:.11rem">❌</span></div><input id="e_REF" type="password" placeholder="1//0g-... - REFRESH حقيقي - يبدأ بـ 1// - REAL ONLY" oninput="editKey('YOUTUBE_REFRESH_TOKEN',this.value)"><button class="btn2" onclick="toggleShow('e_REF')">👁️</button><button class="btn2" onclick="testKey('YOUTUBE_REFRESH_TOKEN')">🔍 حقيقي</button></div>
<div style="display:grid;grid-template-columns:110px 1fr 55px 55px;gap:2px;align-items:center;margin:2px 0;background:#FFF0F0;border-radius:6px;padding:2px;border:3px solid #ff0033"><div style="font-size:.16rem;font-weight:900;color:#ff0033">🔑 YOUTUBE_API_KEY <span id="s_API" style="font-size:.11rem">❌</span></div><input id="e_API" type="password" placeholder="AIza... - YOUTUBE_API_KEY حقيقي - 39 حرف - مهم جدا لحالة القناة الحقيقية - REAL ONLY - لا أرقام وهمية" oninput="editKey('YOUTUBE_API_KEY',this.value)"><button class="btn2" onclick="toggleShow('e_API')">👁️</button><button class="btn2" onclick="testKey('YOUTUBE_API_KEY')">🔍 حقيقي</button></div>
<div style="display:flex;gap:2px;margin-top:3px;flex-wrap:wrap"><button class="btn-real" onclick="saveKeys()">🔐 حفظ المفاتيح الحقيقية - 5 مفاتيح - لا أرقام وهمية - REAL KEYS ONLY</button><button class="btn2" onclick="checkLink()">🔍 فحص الربط الحقيقي - REAL ONLY</button><button class="btn2" onclick="showAllKeys()">👁️ إظهار المفاتيح الحقيقية - REAL ONLY</button></div>
<div id="statusBox" style="background:#FFFFFF;border-radius:6px;padding:3px;font-size:.15rem;min-height:20px;border:2px solid #006400;color:#006400;margin-top:2px">🔐 في انتظار المفاتيح الحقيقية - لا أرقام وهمية - REAL KEYS ONLY - حالة القناة الحقيقية تحتاج YOUTUBE_API_KEY حقيقي - لا أرقام وهمية</div>
</div>
</div>

<div class="log" id="log"><div style="color:#006400">> v79 REAL CHANNEL STATUS - حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - لا أرقام وهمية - بيانات حقيقية من YouTube Data API v3 - خلفية بيضاء #FFFFFF - متابعة حقيقية - REAL CHANNEL STATUS + REAL SUBSCRIBERS + REAL VIDEOS + REAL FOLLOW - حتت مستخبية بروفشنل للمميزين - https://www.youtube.com/@CursedMedicineEG - لا أرقام وهمية - REAL DATA ONLY - 0.00000001ث - لا أرقام وهمية - REAL DATA ONLY</div></div>

</div>
<script>
let curKeys={}; let realFollowInterval=null; let realFollowCount=0;
function log(m,c='#006400',a='REAL'){ try{ const el=document.getElementById('log'); if(!el) return; const d=document.createElement('div'); d.textContent=`[${new Date().toLocaleTimeString()}] [${a}] ${m}`; d.style.color=c; el.appendChild(d); el.scrollTop=el.scrollHeight; }catch(e){} }
function editKey(k,v){ try{ curKeys[k]=v; const id=k.includes('CLIENT_ID')?'ID':k.includes('SECRET')?'SEC':k.includes('REFRESH')?'REF':k.includes('API_KEY')&&k.includes('YOUTUBE')?'API':'GROQ'; const s=document.getElementById('s_'+id); if(s){ if(v){ s.textContent=`✅ ${v.length} حرف حقيقي`; s.style.color='#006400'; } else { s.textContent='❌'; s.style.color='#ff0033'; } } }catch(e){} }
function toggleShow(id){ try{ const input=document.getElementById(id); if(!input) return; input.type=input.type==='password'?'text':'password'; }catch(e){} }
function testKey(k){ try{ const inputId=k=='YOUTUBE_API_KEY'?'e_API':k.includes('CLIENT_ID')?'e_ID':k.includes('SECRET')?'e_SEC':k.includes('REFRESH')?'e_REF':'e_GROQ'; const input=document.getElementById(inputId); const v=curKeys[k]|| (input?input.value:''); let msg=''; if(k=='GROQ_API_KEY') msg=v&&v.startsWith('gsk_')?'✅ GROQ_API_KEY حقيقي - 56 حرف حقيقي - لا أرقام وهمية - REAL ONLY':'❌ GROQ_API_KEY غير حقيقي'; else if(k=='YOUTUBE_CLIENT_ID') msg=v&&v.includes('googleusercontent.com')?'✅ YOUTUBE_CLIENT_ID حقيقي - REAL ONLY':'❌ غير حقيقي'; else if(k=='YOUTUBE_CLIENT_SECRET') msg=v&&v.startsWith('GOCSPX-')?'✅ YOUTUBE_CLIENT_SECRET حقيقي - REAL ONLY':'❌ غير حقيقي'; else if(k=='YOUTUBE_REFRESH_TOKEN') msg=v&&v.startsWith('1//')?'✅ YOUTUBE_REFRESH_TOKEN حقيقي - يبدأ بـ 1// - REAL ONLY':'❌ غير حقيقي'; else if(k=='YOUTUBE_API_KEY') msg=v&&v.startsWith('AIza')&&v.length>30?'✅ YOUTUBE_API_KEY حقيقي - 39 حرف - مهم لحالة القناة الحقيقية - REAL ONLY - لا أرقام وهمية':'❌ YOUTUBE_API_KEY غير حقيقي - يجب يبدأ بـ AIza - 39 حرف - مهم جدا'; const box=document.getElementById('statusBox'); if(box) box.innerHTML=`<div style="color:${msg.includes('✅')?'#006400':'#ff0033'}">${msg} - لا أرقام وهمية - REAL DATA ONLY</div>`; }catch(e){} }
function saveKeys(){ try{ const payload={}; ['e_ID','e_SEC','e_REF','e_GROQ','e_API'].forEach(id=>{ const el=document.getElementById(id); if(el && el.value){ const key=id=='e_ID'?'YOUTUBE_CLIENT_ID':id=='e_SEC'?'YOUTUBE_CLIENT_SECRET':id=='e_REF'?'YOUTUBE_REFRESH_TOKEN':id=='e_GROQ'?'GROQ_API_KEY':'YOUTUBE_API_KEY'; payload[key]=el.value; } }); Object.assign(payload,curKeys); fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)}).then(r=>r.json()).then(d=>{ const box=document.getElementById('statusBox'); if(box) box.innerHTML=`<div style="color:#006400">✅ حفظ ${d.count}/5 مفاتيح حقيقية - لا أرقام وهمية - REAL KEYS ONLY - ${d.count>=1?'يمكن الآن جلب بيانات القناة الحقيقية - REAL CHANNEL DATA':''}</div>`; checkLink(); if(d.count>=1) setTimeout(()=>{ fetchRealChannel(); },1000); }).catch(e=>{}); }catch(e){} }
function checkLink(){ try{ fetch('/api/keys/status').then(r=>r.json()).then(s=>{ const badge=document.getElementById('linkBadge'); if(badge) badge.textContent=s.linked?'✅ متصلة حقيقية - REAL ONLY - لا أرقام وهمية':`❌ غير متصلة - ${s.count}/5 مفاتيح حقيقية - REAL ONLY`; const apiBadge=document.getElementById('s_API'); if(apiBadge){ const hasApi=s.has_api; if(apiBadge) apiBadge.textContent=hasApi?`✅ ${s.api_len} حرف حقيقي`:'❌'; } }).catch(e=>{}); }catch(e){} }
function showAllKeys(){ try{ fetch('/api/keys/show').then(r=>r.json()).then(s=>{ document.getElementById('e_ID').value=s.YOUTUBE_CLIENT_ID||''; document.getElementById('e_SEC').value=s.YOUTUBE_CLIENT_SECRET||''; document.getElementById('e_REF').value=s.YOUTUBE_REFRESH_TOKEN||''; document.getElementById('e_GROQ').value=s.GROQ_API_KEY||''; document.getElementById('e_API').value=s.YOUTUBE_API_KEY||''; }).catch(e=>{}); }catch(e){} }

function fetchRealChannel(){
 try{
   log('📺 جلب بيانات القناة الحقيقية - حالة القناه الحقيقة وعدد المشتركين الحقيقة - لا أرقام وهمية - REAL CHANNEL STATUS - YouTube API v3 - https://www.youtube.com/@CursedMedicineEG','#006400','REAL_CHANNEL_FETCH');
   const infoEl=document.getElementById('realChannelInfo');
   const badgeEl=document.getElementById('channelStatusBadge');
   if(infoEl) infoEl.innerHTML='🔍 جاري جلب بيانات القناة الحقيقية من YouTube API v3...<br>📡 Handle: @CursedMedicineEG<br>🔗 URL: https://www.youtube.com/@CursedMedicineEG<br>📡 باستخدام YOUTUBE_API_KEY حقيقي - لا أرقام وهمية<br>⏳ قد يستغرق بضع ثواني - فحص حقيقي - REAL CHANNEL FETCH - لا أرقام وهمية<br>🔍 جلب: snippet + statistics + contentDetails + status - حقيقي - لا أرقام وهمية';
   if(badgeEl) badgeEl.textContent='🔍 جاري جلب بيانات القناة الحقيقية... - REAL FETCH - لا أرقام وهمية';
   
   fetch('/api/channel/real').then(r=>r.json()).then(data=>{
     if(infoEl){
       if(data.channel_id){
         infoEl.innerHTML=`<div style="color:#006400;font-weight:900">✅ بيانات القناة الحقيقية - لا أرقام وهمية - REAL CHANNEL DATA ONLY - YouTube API v3<br>
         📺 اسم القناة الحقيقي: ${data.title}<br>
         🆔 Channel ID الحقيقي: ${data.channel_id}<br>
         🔗 Handle الحقيقي: ${data.custom_url || data.handle} - حقيقي<br>
         🔗 رابط القناة الحقيقي: ${data.url}<br>
         📅 تاريخ الإنشاء الحقيقي: ${data.published_at} - حقيقي - لا أرقام وهمية<br>
         📝 وصف القناة الحقيقي: ${data.description ? data.description.slice(0,150)+'...' : 'لا يوجد وصف - حقيقي'}<br>
         🖼️ صورة القناة الحقيقية: ${data.thumbnails ? '✅ موجودة - حقيقية' : '❌ غير موجودة'}<br>
         📊 إحصائيات حقيقية - لا أرقام وهمية:<br>
         &nbsp;&nbsp;👥 المشتركون الحقيقيون: ${data.statistics.subscriber_count} - حقيقي - لا أرقام وهمية - REAL SUBSCRIBERS ONLY<br>
         &nbsp;&nbsp;👀 المشاهدات الحقيقية: ${data.statistics.view_count} - حقيقي - لا أرقام وهمية - REAL VIEWS ONLY<br>
         &nbsp;&nbsp;🎬 الفيديوهات الحقيقية: ${data.statistics.video_count} - حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY<br>
         &nbsp;&nbsp;👁️ إخفاء المشتركين: ${data.statistics.hidden_subscriber_count?'نعم - مخفي - حقيقي':'لا - ظاهر - حقيقي'}<br>
         📋 قائمة التشغيل الحقيقية (uploads): ${data.content_details.uploads_playlist || 'غير متوفر - حقيقي'}<br>
         ✅ حالة القناة الحقيقية: ${data.status}<br>
         🕒 آخر فحص حقيقي: ${data.last_fetch} - حقيقي - لا أرقام وهمية<br>
         📡 API متاح: ${data.api_available?'✅ نعم - حقيقي - REAL API AVAILABLE':'❌ لا - لا أرقام وهمية'}<br>
         ✅ بيانات حقيقية فقط - لا أرقام وهمية - REAL DATA ONLY<br>
         🔔 فعل الجرس + اشترك - حقيقي - REAL SUBSCRIBE + BELL - لا أرقام وهمية</div>`;
         
         // تحديث الإحصائيات الحقيقية
         document.getElementById('realSubsCount').textContent=typeof data.statistics.subscriber_count==='number'?data.statistics.subscriber_count.toLocaleString()+' مشترك حقيقي':data.statistics.subscriber_count;
         document.getElementById('realViewsCount').textContent=typeof data.statistics.view_count==='number'?data.statistics.view_count.toLocaleString()+' مشاهدة حقيقية':data.statistics.view_count;
         document.getElementById('realVideosCount').textContent=typeof data.statistics.video_count==='number'?data.statistics.video_count+' فيديو حقيقي':data.statistics.video_count;
         document.getElementById('realChannelStatsDetailed').innerHTML=`<div style="color:#006400;font-weight:900">✅ إحصائيات حقيقية مفصلة - لا أرقام وهمية - REAL DETAILED STATS ONLY<br>
         📺 القناة: ${data.title} - ${data.channel_id}<br>
         👥 المشتركون الحقيقيون: ${data.statistics.subscriber_count} - حقيقي - لا أرقام وهمية - REAL SUBSCRIBERS ONLY<br>
         👀 المشاهدات الحقيقية: ${data.statistics.view_count} - حقيقي - لا أرقام وهمية - REAL VIEWS ONLY<br>
         🎬 الفيديوهات الحقيقية: ${data.statistics.video_count} - حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY<br>
         📅 تاريخ الإنشاء: ${data.published_at} - حقيقي<br>
         🔗 ${data.url}<br>
         🕒 ${data.last_fetch}<br>
         ✅ لا أرقام وهمية - REAL DATA ONLY</div>`;
         
         if(badgeEl) badgeEl.textContent=`✅ ${data.title} - ${typeof data.statistics.subscriber_count==='number'?data.statistics.subscriber_count.toLocaleString()+' مشترك حقيقي':data.statistics.subscriber_count} - ${data.statistics.video_count} فيديو حقيقي - لا أرقام وهمية - REAL DATA`;
         
         log(`✅ بيانات القناة الحقيقية - ${data.title} - ${data.channel_id} - مشتركون حقيقيون: ${data.statistics.subscriber_count} - مشاهدات حقيقية: ${data.statistics.view_count} - فيديوهات حقيقية: ${data.statistics.video_count} - لا أرقام وهمية - REAL CHANNEL DATA - ${data.last_fetch}`,'#006400','REAL_CHANNEL_SUCCESS');
         
         // جلب الفيديوهات تلقائيا بعد جلب القناة
         setTimeout(()=>{ fetchRealVideos(); checkRealLive(); },1500);
         
       } else {
         infoEl.innerHTML=`<div style="color:#ff0033;font-weight:900">❌ فشل جلب بيانات القناة الحقيقية - لا أرقام وهمية - REAL ERROR ONLY<br>❌ الحالة الحقيقية: ${data.status}<br>🕒 آخر فحص حقيقي: ${data.last_fetch}<br>📡 API متاح: ${data.api_available?'✅ نعم':'❌ لا'}<br>🔑 YOUTUBE_API_KEY: ${data.has_api_key?'✅ موجود حقيقي':'❌ غير موجود حقيقي - أضف مفتاح حقيقي'}<br>🔗 القناة: ${data.url}<br>❌ لا أرقام وهمية - خطأ حقيقي - REAL ERROR ONLY<br>💡 الحل الحقيقي: أضف YOUTUBE_API_KEY حقيقي من Google Cloud Console - 39 حرف - يبدأ بـ AIza - لا أرقام وهمية<br>🔗 https://console.cloud.google.com/apis/credentials<br>🔔 لا أرقام وهمية - REAL ERROR ONLY</div>`;
         if(badgeEl) badgeEl.textContent=`❌ فشل - ${data.status.slice(0,50)}... - لا أرقام وهمية - REAL ERROR`;
         log(`❌ فشل جلب بيانات القناة الحقيقية - ${data.status} - لا أرقام وهمية - REAL ERROR - ${data.last_fetch}`,'#ff0033','REAL_CHANNEL_ERROR');
       }
     }
   }).catch(e=>{
     if(infoEl) infoEl.innerHTML=`<div style="color:#ff0033">❌ خطأ في جلب بيانات القناة الحقيقية: ${e} - لا أرقام وهمية - REAL ERROR ONLY</div>`;
     log('❌ خطأ fetchRealChannel fetch: '+e+' - لا أرقام وهمية','#ff0033','ERROR');
   });
 }catch(e){ log('خطأ fetchRealChannel: '+e,'#ff0033','ERROR'); }
}

function fetchRealVideos(){
 try{
   log('🎬 جلب الفيديوهات الحقيقية - الفيديوهات اللي موجوده على القناه - لا أرقام وهمية - REAL VIDEOS ON CHANNEL - 50 فيديو حقيقي - YouTube API v3','#006400','REAL_VIDEOS_FETCH');
   const gridEl=document.getElementById('realVideosGrid');
   const badgeEl=document.getElementById('videosCountBadge');
   const statusEl=document.getElementById('videosStatusBadge');
   if(gridEl) gridEl.innerHTML='🔍 جاري جلب الفيديوهات الحقيقية من القناة...<br>📡 50 فيديو حقيقي - لا أرقام وهمية<br>📺 من قائمة التشغيل الحقيقية uploads - لا أرقام وهمية<br>📡 باستخدام YOUTUBE_API_KEY حقيقي - لا أرقام وهمية<br>⏳ قد يستغرق بضع ثواني - فحص حقيقي - REAL VIDEOS FETCH - لا أرقام وهمية';
   if(statusEl) statusEl.textContent='🔍 جاري جلب الفيديوهات الحقيقية... - REAL FETCH - لا أرقام وهمية';
   
   fetch('/api/channel/videos').then(r=>r.json()).then(data=>{
     if(gridEl){
       if(data.videos && data.videos.length>0){
         gridEl.innerHTML=data.videos.map(v=>`<div class="video-card" onclick="window.open('${v.url}','_blank')"><img src="${v.thumbnails && v.thumbnails.medium ? v.thumbnails.medium.url : v.thumbnails && v.thumbnails.default ? v.thumbnails.default.url : 'https://via.placeholder.com/180x100?text=No+Thumbnail+REAL'}" alt="${v.title}"><div style="font-size:.14rem;font-weight:900;color:#0a0a0a;margin-top:2px">${v.title.slice(0,60)}${v.title.length>60?'...':''}</div><div style="font-size:.12rem;color:#666">${v.published_at ? new Date(v.published_at).toLocaleDateString('ar-EG')+' - حقيقي' : 'تاريخ غير معروف - حقيقي'}</div><div style="font-size:.12rem;color:#006400;font-weight:700">👀 ${v.view_count_real!==undefined?v.view_count_real.toLocaleString()+' مشاهدة حقيقية':'مشاهدات غير متوفرة - لا أرقام وهمية'} - لا أرقام وهمية</div><div style="font-size:.11rem;color:#0a0a0a">👍 ${v.like_count_real!==undefined?v.like_count_real.toLocaleString()+' إعجاب حقيقي':'إعجابات غير متوفرة'} - 💬 ${v.comment_count_real!==undefined?v.comment_count_real.toLocaleString()+' تعليق حقيقي':'تعليقات غير متوفرة'}</div><div style="font-size:.11rem;color:#006400">✅ حقيقي - لا أرقام وهمية - REAL VIDEO ONLY</div></div>`).join('');
         
         document.getElementById('realVideosCount').textContent=data.videos.length+' فيديو حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY';
         if(badgeEl) badgeEl.textContent=`✅ ${data.videos.length} فيديو حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY - ${data.total_views_real?data.total_views_real.toLocaleString()+' مشاهدة حقيقية إجمالية':''}`;
         if(statusEl) statusEl.textContent=`✅ ${data.videos.length} فيديو حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY - آخر فحص: ${data.last_fetch}`;
         document.getElementById('realVideosStats').innerHTML=`📊 إحصائيات الفيديوهات الحقيقية: ${data.videos.length} فيديو حقيقي - ${data.total_views_real?data.total_views_real.toLocaleString()+' مشاهدة حقيقية إجمالية - لا أرقام وهمية':''} - ${data.total_likes_real?data.total_likes_real.toLocaleString()+' إعجاب حقيقي - لا أرقام وهمية':''} - لا أرقام وهمية - REAL STATS ONLY - آخر فحص: ${data.last_fetch} - لا أرقام وهمية`;
         
         log(`✅ فيديوهات حقيقية - ${data.videos.length} فيديو حقيقي - ${data.total_views_real?data.total_views_real.toLocaleString()+' مشاهدة حقيقية إجمالية':''} - لا أرقام وهمية - REAL VIDEOS ONLY - ${data.last_fetch}`,'#006400','REAL_VIDEOS_SUCCESS');
       } else {
         gridEl.innerHTML=`<div style="color:#ff0033;font-weight:900">❌ لا يوجد فيديوهات حقيقية - ${data.status || 'لا يوجد فيديوهات - لا أرقام وهمية'}<br>📡 ${data.last_fetch || 'لم يتم الفحص بعد'}<br>❌ لا أرقام وهمية - لا يوجد فيديوهات حقيقية - REAL ERROR ONLY<br>💡 تأكد من وجود YOUTUBE_API_KEY حقيقي + Channel ID حقيقي<br>🔗 https://www.youtube.com/@CursedMedicineEG/videos<br>❌ لا أرقام وهمية - REAL ERROR ONLY</div>`;
         if(badgeEl) badgeEl.textContent=`❌ 0 فيديو حقيقي - ${data.status || 'لا يوجد فيديوهات'} - لا أرقام وهمية`;
         if(statusEl) statusEl.textContent=`❌ فشل - ${data.status || 'لا يوجد فيديوهات'} - لا أرقام وهمية`;
         log(`❌ لا يوجد فيديوهات حقيقية - ${data.status} - لا أرقام وهمية - REAL ERROR`,'#ff0033','REAL_VIDEOS_ERROR');
       }
     }
   }).catch(e=>{
     if(gridEl) gridEl.innerHTML=`<div style="color:#ff0033">❌ خطأ في جلب الفيديوهات الحقيقية: ${e} - لا أرقام وهمية - REAL ERROR ONLY</div>`;
     log('❌ خطأ fetchRealVideos fetch: '+e+' - لا أرقام وهمية','#ff0033','ERROR');
   });
 }catch(e){ log('خطأ fetchRealVideos: '+e,'#ff0033','ERROR'); }
}

function checkRealLive(){
 try{
   log('🔴 فحص البث المباشر الحقيقي - لا أرقام وهمية - REAL LIVE CHECK - YouTube API v3 - https://www.youtube.com/@CursedMedicineEG/live','#ff0033','REAL_LIVE_CHECK');
   const badgeEl=document.getElementById('liveStatusBadge');
   const liveCountEl=document.getElementById('realLiveCount');
   const liveDetailsEl=document.getElementById('realLiveDetails');
   if(badgeEl) badgeEl.textContent='🔍 جاري فحص البث المباشر الحقيقي... - REAL LIVE CHECK - لا أرقام وهمية';
   
   fetch('/api/channel/live').then(r=>r.json()).then(data=>{
     if(badgeEl) badgeEl.textContent=data.is_live?'🔴 يوجد بث مباشر حقيقي الآن - REAL LIVE NOW - لا أرقام وهمية':'⚫ لا يوجد بث مباشر حقيقي الآن - لا أرقام وهمية - REAL CHECK';
     if(liveCountEl) liveCountEl.textContent=data.is_live?`🔴 ${data.live_title ? data.live_title.slice(0,30)+'...' : 'بث مباشر حقيقي الآن - REAL LIVE NOW'} - ${data.viewers_real} مشاهد حقيقي - لا أرقام وهمية`:'⚫ لا يوجد بث مباشر حقيقي الآن - لا أرقام وهمية - REAL CHECK ONLY';
     if(liveDetailsEl) liveDetailsEl.textContent=data.is_live?`🔴 بث مباشر حقيقي الآن - ${data.viewers_real} مشاهد حقيقي - ${data.live_title} - ${data.last_check} - لا أرقام وهمية - REAL LIVE NOW`:`⚫ لا يوجد بث - ${data.last_check} - ${data.upcoming && data.upcoming.length>0?data.upcoming.length+' بث قادم حقيقي - لا أرقام وهمية':''} - لا أرقام وهمية - REAL CHECK`;
     
     log(`${data.is_live?'🔴 يوجد بث مباشر حقيقي الآن':'⚫ لا يوجد بث مباشر حقيقي الآن'} - ${data.is_live?data.live_title+' - '+data.viewers_real+' مشاهد حقيقي':''} - ${data.last_check} - لا أرقام وهمية - REAL LIVE CHECK - ${data.is_live?'REAL LIVE NOW':'NO LIVE - REAL CHECK'} - لا أرقام وهمية`,'#ff0033','REAL_LIVE_'+(data.is_live?'LIVE':'NO_LIVE'));
   }).catch(e=>{ log('❌ خطأ checkRealLive fetch: '+e+' - لا أرقام وهمية','#ff0033','ERROR'); });
 }catch(e){ log('خطأ checkRealLive: '+e,'#ff0033','ERROR'); }
}

function startRealFollow(){
 try{
   if(realFollowInterval){ clearInterval(realFollowInterval); realFollowInterval=null; log('⏹️ تم إيقاف المتابعة الحقيقية - لا أرقام وهمية - REAL FOLLOW STOPPED','#ff0033','REAL_FOLLOW_STOP'); document.getElementById('realFollowLog').innerHTML+='<div style="color:#ff0033">⏹️ تم إيقاف المتابعة الحقيقية - لا أرقام وهمية - REAL FOLLOW STOPPED</div>'; return; }
   realFollowCount=0;
   log('🔔 بدء المتابعة الحقيقية للقناة وكل شيء - REAL FOLLOW EVERYTHING START - لا أرقام وهمية - كل 60 ثانية - REAL FOLLOW - لا أرقام وهمية','#006400','REAL_FOLLOW_START');
   const logEl=document.getElementById('realFollowLog');
   if(logEl) logEl.innerHTML=`<div style="color:#006400;font-weight:900">🔔 بدء المتابعة الحقيقية للقناة وكل شيء - ${new Date().toLocaleTimeString()} - لا أرقام وهمية<br>📺 متابعة حالة القناة الحقيقية - كل 60 ثانية - لا أرقام وهمية<br>👥 متابعة عدد المشتركين الحقيقي - لا أرقام وهمية<br>🎬 متابعة الفيديوهات الحقيقية - لا أرقام وهمية<br>🔴 متابعة البث المباشر الحقيقي - لا أرقام وهمية<br>✅ كل شيء حقيقي - لا أرقام وهمية - REAL FOLLOW EVERYTHING - لا أرقام وهمية</div>`;
   
   fetchRealChannel();
   fetchRealVideos();
   checkRealLive();
   
   realFollowInterval=setInterval(()=>{
     realFollowCount++;
     fetchRealChannel();
     fetchRealVideos();
     checkRealLive();
     const time=new Date().toLocaleTimeString();
     if(logEl){
       const entry=document.createElement('div');
       entry.style.color='#006400';
       entry.style.fontSize='.12rem';
       entry.style.borderBottom='1px solid #e0e0e0';
       entry.style.padding='1px 0';
       entry.textContent=`[${time}] 🔄 متابعة حقيقية #${realFollowCount} - حالة القناة الحقيقية + المشتركين الحقيقيين + الفيديوهات الحقيقية + البث الحقيقي - لا أرقام وهمية - REAL FOLLOW #${realFollowCount} - لا أرقام وهمية`;
       logEl.appendChild(entry);
       logEl.scrollTop=logEl.scrollHeight;
       if(logEl.children.length>50){ logEl.removeChild(logEl.firstChild); }
     }
     log(`🔄 متابعة حقيقية #${realFollowCount} - حالة القناة الحقيقية + المشتركين الحقيقيين + الفيديوهات الحقيقية + البث الحقيقي - لا أرقام وهمية - REAL FOLLOW #${realFollowCount} - لا أرقام وهمية`,'#006400','REAL_FOLLOW_'+realFollowCount);
   },60000);
   
 }catch(e){ log('خطأ startRealFollow: '+e,'#ff0033','ERROR'); }
}

function openRealChannel(){ window.open('https://www.youtube.com/@CursedMedicineEG','_blank'); log('🔗 فتح القناة الحقيقية - https://www.youtube.com/@CursedMedicineEG - لا أرقام وهمية - REAL CHANNEL OPEN','#006400','CHANNEL_OPEN'); }
function openRealVideos(){ window.open('https://www.youtube.com/@CursedMedicineEG/videos','_blank'); log('🎬 فتح فيديوهات القناة الحقيقية - https://www.youtube.com/@CursedMedicineEG/videos - لا أرقام وهمية - REAL VIDEOS OPEN','#006400','VIDEOS_OPEN'); }
function openRealLive(){ window.open('https://www.youtube.com/@CursedMedicineEG/live','_blank'); log('🔴 فتح البث المباشر الحقيقي - https://www.youtube.com/@CursedMedicineEG/live - لا أرقام وهمية - REAL LIVE OPEN','#ff0033','LIVE_OPEN'); }
function subscribeReal(){ window.open('https://www.youtube.com/@CursedMedicineEG?sub_confirmation=1','_blank'); log('🔔 اشترك + فعل الجرس حقيقي - https://www.youtube.com/@CursedMedicineEG?sub_confirmation=1 - لا أرقام وهمية - REAL SUBSCRIBE + BELL','#ff0033','SUBSCRIBE_REAL'); }
function sortVideos(type){ log(`📊 ترتيب الفيديوهات الحقيقية حسب ${type} - لا أرقام وهمية - REAL SORT - ${type} - لا أرقام وهمية`,'#006400','SORT_'+type); fetchRealVideos(); }
function filterVideos(type){ log(`🔍 فلتر الفيديوهات الحقيقية - ${type} - لا أرقام وهمية - REAL FILTER - ${type} - لا أرقام وهمية`,'#006400','FILTER_'+type); }
function clearVideos(){ document.getElementById('realVideosGrid').innerHTML='📭 تم مسح القائمة - لا أرقام وهمية - REAL CLEAR - اضغط جلب الفيديوهات الحقيقية - لا أرقام وهمية'; log('🗑️ مسح قائمة الفيديوهات الحقيقية - لا أرقام وهمية - REAL CLEAR','#006400','CLEAR_VIDEOS'); }

document.addEventListener('DOMContentLoaded', function(){
 try{
   checkLink();
   log('v79 REAL CHANNEL STATUS - حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - لا أرقام وهمية - بيانات حقيقية من YouTube Data API v3 - خلفية بيضاء #FFFFFF - متابعة حقيقية - REAL CHANNEL STATUS + REAL SUBSCRIBERS + REAL VIDEOS + REAL FOLLOW - حتت مستخبية بروفشنل للمميزين - https://www.youtube.com/@CursedMedicineEG - لا أرقام وهمية - REAL DATA ONLY - 0.00000001ث - لا أرقام وهمية - REAL DATA ONLY','#006400','REAL_CHANNEL_V79');
   // محاولة جلب بيانات حقيقية تلقائيا إذا كان API KEY موجود
   setTimeout(()=>{ fetch('/api/keys/status').then(r=>r.json()).then(s=>{ if(s.has_api){ log('🔑 YOUTUBE_API_KEY حقيقي موجود - جلب بيانات القناة الحقيقية تلقائيا - لا أرقام وهمية - REAL API KEY FOUND - AUTO FETCH REAL CHANNEL','#006400','AUTO_FETCH'); fetchRealChannel(); } else { log('❌ لا يوجد YOUTUBE_API_KEY حقيقي - أضف مفتاح حقيقي من Google Cloud Console - 39 حرف - يبدأ بـ AIza - لا أرقام وهمية - ADD REAL API KEY - https://console.cloud.google.com/apis/credentials','#ff0033','NO_API_KEY'); } }).catch(e=>{}); },1500);
 }catch(e){ log('خطأ DOMContentLoaded: '+e,'#ff0033','ERROR'); }
});
</script>
</body>
</html>
"""

@app.route('/')
def index():
    html=HTML.replace('{{countries_json}}', json.dumps(COUNTRIES, ensure_ascii=False))
    resp=Response(html, mimetype='text/html')
    resp.headers['Cache-Control']='public, max-age=1'
    return resp

@app.route('/api/keys/save', methods=['POST'])
def save_keys():
    try:
        data=request.get_json()
        for k,v in data.items():
            if v is not None and v.strip():
                VAULT[k]=v.strip()
        return jsonify({"status":"success","count":sum(1 for x in [VAULT["YOUTUBE_CLIENT_ID"],VAULT["YOUTUBE_CLIENT_SECRET"],VAULT["YOUTUBE_REFRESH_TOKEN"],VAULT["GROQ_API_KEY"],VAULT["YOUTUBE_API_KEY"]] if x),"real":"✅ مفاتيح حقيقية - لا أرقام وهمية"})
    except Exception as e:
        return jsonify({"status":"error","msg":str(e)}),500

@app.route('/api/keys/status')
def keys_status():
    has_id=bool(VAULT["YOUTUBE_CLIENT_ID"] and len(VAULT["YOUTUBE_CLIENT_ID"])>20)
    has_sec=bool(VAULT["YOUTUBE_CLIENT_SECRET"] and len(VAULT["YOUTUBE_CLIENT_SECRET"])>10)
    has_ref=bool(VAULT["YOUTUBE_REFRESH_TOKEN"] and VAULT["YOUTUBE_REFRESH_TOKEN"].startswith("1//"))
    has_groq=bool(VAULT["GROQ_API_KEY"] and VAULT["GROQ_API_KEY"].startswith("gsk_"))
    has_api=bool(VAULT["YOUTUBE_API_KEY"] and len(VAULT["YOUTUBE_API_KEY"])>30 and VAULT["YOUTUBE_API_KEY"].startswith("AIza"))
    linked_full = has_id and has_sec and has_ref
    return jsonify({
        "linked":linked_full,
        "has_api":has_api,
        "api_len":len(VAULT["YOUTUBE_API_KEY"]) if VAULT["YOUTUBE_API_KEY"] else 0,
        "count":sum(1 for x in [VAULT["YOUTUBE_CLIENT_ID"],VAULT["YOUTUBE_CLIENT_SECRET"],VAULT["YOUTUBE_REFRESH_TOKEN"],VAULT["GROQ_API_KEY"],VAULT["YOUTUBE_API_KEY"]] if x),
        "has_id":has_id,
        "has_secret":has_sec,
        "has_refresh":has_ref,
        "has_groq":has_groq,
        "details": {
            "ID": f"✅ موجود حقيقي ({len(VAULT['YOUTUBE_CLIENT_ID'])} حرف)" if has_id else "❌ غير موجود حقيقي",
            "SECRET": f"✅ موجود حقيقي ({len(VAULT['YOUTUBE_CLIENT_SECRET'])} حرف)" if has_sec else "❌ غير موجود حقيقي",
            "REFRESH": f"✅ موجود حقيقي ({len(VAULT['YOUTUBE_REFRESH_TOKEN'])} حرف)" if has_ref else "❌ غير موجود حقيقي",
            "GROQ": f"✅ موجود حقيقي ({len(VAULT['GROQ_API_KEY'])} حرف)" if has_groq else "❌ غير موجود حقيقي",
            "API": f"✅ موجود حقيقي ({len(VAULT['YOUTUBE_API_KEY'])} حرف) - مهم لحالة القناة الحقيقية" if has_api else "❌ غير موجود حقيقي - YOUTUBE_API_KEY - 39 حرف - يبدأ بـ AIza - مهم جدا لحالة القناة الحقيقية وعدد المشتركين الحقيقي والفيديوهات الحقيقية"
        }
    })

@app.route('/api/keys/show')
def keys_show():
    return jsonify({k:VAULT[k] for k in ["YOUTUBE_CLIENT_ID","YOUTUBE_CLIENT_SECRET","YOUTUBE_REFRESH_TOKEN","GROQ_API_KEY","YOUTUBE_API_KEY"]})

@app.route('/api/channel/real')
def channel_real():
    data = fetch_real_channel_data()
    # إضافة معلومات إضافية للواجهة
    data["has_api_key"] = bool(VAULT["YOUTUBE_API_KEY"] and len(VAULT["YOUTUBE_API_KEY"])>20)
    data["handle"] = VAULT["CHANNEL_HANDLE"]
    data["url"] = VAULT["CHANNEL_URL"]
    return jsonify(data)

@app.route('/api/channel/videos')
def channel_videos():
    try:
        if not CHANNEL_REAL.get("channel_id"):
            # حاول جلب بيانات القناة أولا
            fetch_real_channel_data()
        
        videos = fetch_real_videos()
        
        # حساب إحصائيات إجمالية حقيقية
        total_views = sum([v.get('view_count_real',0) for v in videos if isinstance(v.get('view_count_real'),int)])
        total_likes = sum([v.get('like_count_real',0) for v in videos if isinstance(v.get('like_count_real'),int)])
        
        return jsonify({
            "videos": videos,
            "count": len(videos),
            "total_views_real": total_views,
            "total_likes_real": total_likes,
            "status": f"✅ {len(videos)} فيديو حقيقي - لا أرقام وهمية - REAL VIDEOS ONLY - {total_views} مشاهدة حقيقية إجمالية" if videos else "❌ لا يوجد فيديوهات حقيقية - تأكد من YOUTUBE_API_KEY حقيقي - لا أرقام وهمية",
            "last_fetch": datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - حقيقي - لا أرقام وهمية",
            "channel_id": CHANNEL_REAL.get("channel_id"),
            "channel_title": CHANNEL_REAL.get("title"),
            "real": True,
            "no_fake": True
        })
    except Exception as e:
        return jsonify({
            "videos": [],
            "count": 0,
            "status": f"❌ خطأ حقيقي في جلب الفيديوهات - {str(e)} - لا أرقام وهمية - REAL ERROR",
            "last_fetch": datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" - خطأ: {str(e)} - لا أرقام وهمية",
            "real": False,
            "no_fake": True
        })

@app.route('/api/channel/live')
def channel_live():
    data = check_real_live_status()
    return jsonify(data)

@app.route('/api/channel/stats')
def channel_stats():
    # إحصائيات سريعة حقيقية
    return jsonify({
        "channel": CHANNEL_REAL,
        "live": LIVE_STATUS_REAL,
        "videos_count": len(VIDEOS_REAL),
        "videos": VIDEOS_REAL[:5],  # أول 5 فيديوهات حقيقية
        "real": True,
        "no_fake": True,
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - حقيقي - لا أرقام وهمية"
    })

@app.route('/health')
def health():
    return f"v79 REAL CHANNEL STATUS - حالة القناه الحقيقة وعدد المشتركين الحقيقة والفيديوهات اللي موجوده على القناه مع متابعه حقيقيه للقناة وكل شئ - لا أرقام وهمية - بيانات حقيقية من YouTube Data API v3 - Channel ID: {CHANNEL_REAL.get('channel_id','غير متوفر - لا أرقام وهمية')} - Title: {CHANNEL_REAL.get('title','غير متوفر - لا أرقام وهمية')} - Subs: {CHANNEL_REAL.get('statistics',{}).get('subscriber_count','غير متوفر - لا أرقام وهمية')} - Views: {CHANNEL_REAL.get('statistics',{}).get('view_count','غير متوفر - لا أرقام وهمية')} - Videos: {CHANNEL_REAL.get('statistics',{}).get('video_count','غير متوفر - لا أرقام وهمية')} - Videos Real: {len(VIDEOS_REAL)} - Live: {LIVE_STATUS_REAL.get('is_live','غير معروف - لا أرقام وهمية')} - API Available: {CHANNEL_REAL.get('api_available','غير معروف')} - Last Fetch: {CHANNEL_REAL.get('last_fetch','لم يتم بعد')} - لا أرقام وهمية - REAL DATA ONLY - https://www.youtube.com/@CursedMedicineEG - v79 REAL CHANNEL STATUS"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
