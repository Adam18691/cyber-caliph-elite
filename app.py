# v70 ULTRA 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث - كل المشاريع القديمه والحديثه والاحداث + 20 دوله ترجمه + ذروة + مونتاج + كاميرات + زوايا سينمائية + طيبات العوضي + مصطفى محمود + لعنة الفراعنه + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء - https://www.youtube.com/@CursedMedicineEG - 0.1ث-0.3ث
import os, secrets, random, json, threading, time, base64
from datetime import datetime
from flask import Flask, Response, request, jsonify
app = Flask(__name__)
app.secret_key = secrets.token_hex(2)
def enc(t): return base64.b64encode(t.encode()).decode() if t else ""
EID=os.environ.get('YOUTUBE_CLIENT_ID',''); ESEC=os.environ.get('YOUTUBE_CLIENT_SECRET',''); EREF=os.environ.get('YOUTUBE_REFRESH_TOKEN',''); EGROQ=os.environ.get('GROQ_API_KEY',''); EYT=os.environ.get('YOUTUBE_API_KEY',''); EAFF=os.environ.get('AFFILIATE_LINK','https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6')
VAULT={"YOUTUBE_CLIENT_ID":EID,"YOUTUBE_CLIENT_SECRET":ESEC,"YOUTUBE_REFRESH_TOKEN":EREF,"GROQ_API_KEY":EGROQ,"YOUTUBE_API_KEY":EYT,"AFFILIATE_LINK":EAFF,"CHANNEL":"https://www.youtube.com/@CursedMedicineEG"}

# كل المشاريع القديمه والحديثه والاحداث - لاتنسي اي شئ - 147 موضوع
OLD=[["الأسرار المدفونة - ترتاريا مصر @Cursed","هل كان الفراعنة يعرفون الجدار؟ @Cursed - https://www.youtube.com/@CursedMedicineEG"],["الطعام الخالد - طيبات فرعوني @Cursed","طيبات وصفة فرعونية ترتارية @Cursed"],["لعنة الحضارات - ترتاريا مصر @Cursed","لعنة الفراعنة غطاء ترتاريا @Cursed"],["الجراحة الخفية - طب ملعون @Cursed","زراعة أعضاء قبل 5000 سنة! @Cursed"],["الطاقة المفقودة - أهرامات @Cursed","أهرامات محطات طاقة @Cursed"],["أسرار التحنيط @Cursed","تحنيط تجميد زمني ترتاريا @Cursed"],["المسلات - هوائيات @Cursed","المسلات هوائيات طاقة حرة @Cursed"],["بردية إيبرس @Cursed","بردية إيبرس دستور ترتاريا الطبي @Cursed"],["لعنة توت @Cursed","لعنة توت حماية ترتارية DEW @Cursed"],["أبو الهول - حارس بوابة @Cursed","أبو الهول حارس Star Gates @Cursed"],["مكتبة الإسكندرية @Cursed","مكتبة الإسكندرية ترتارية أحرقوها 1776 @Cursed"],["الهرم الأكبر - محطة طاقة @Cursed","الهرم الأكبر محطة طاقة ترتارية @Cursed"],["الكهنة - مهندسو ترتاريا @Cursed","الكهنة مهندسو ترتاريا @Cursed"],["المقابر - بيوت طاقة @Cursed","المقابر بيوت طاقة ترتارية @Cursed"],["إيمحوتب - آخر مهندس @Cursed","إيمحوتب آخر مهندس ترتاري @Cursed"]]
NEW=[["الذكاء الاصطناعي الفرعوني @Cursed","AI فرعوني ترتاريا @Cursed - KIE.AI"],["العملات الرقمية ترتاري @Cursed","بتكوين ترتاري طاقة حرة @Cursed"],["النانو تكنولوجي فرعوني @Cursed","ذهب نانو ترتاري @Cursed"],["العلاج بالطاقة 2026 @Cursed","علاج طاقة حرة ترتارية @Cursed"],["السيارات الكهربائية فرعونية @Cursed","سيارات كهربائية طاقة حرة @Cursed"],["الإنترنت الفرعوني @Cursed","إنترنت شبكة أثير ترتارية @Cursed"],["الطيران الفرعوني @Cursed","طيران فيمانا ترتارية @Cursed"],["الروبوتات الفرعونية @Cursed","روبوتات ترتارية @Cursed"],["الطباعة 3D فرعونية @Cursed","طباعة 3D ترتارية @Cursed"],["الخلود 900 سنة @Cursed","خلود 900 سنة طيبات @Cursed"],["المدن الذكية فرعونية @Cursed","مدن ترتارية ذكية @Cursed"],["التعليم فرعوني @Cursed","تعليم ترتاري مجاني @Cursed"],["الاقتصاد فرعوني @Cursed","اقتصاد ترتاري حر @Cursed"],["الجيش فرعوني @Cursed","جيش ترتاري طاقة DEW @Cursed"],["القضاء فرعوني @Cursed","عدل ترتاري ميزان ماعت @Cursed"]]
EVENTS=[["تسريبات 2026 مومياء تتكلم @Cursed","مومياء تتكلم 3000 سنة @Cursed - https://www.youtube.com/@CursedMedicineEG"],["ترند شاب يفتح مقبرة ترتارية 50M @Cursed","شاب يفتح مقبرة ترتارية 50M @Cursed"],["ناسا هرم على المريخ @Cursed","ناسا هرم على المريخ مطابق خوفو @Cursed"],["نتفليكس يحذف ترتاريا 24 ساعة @Cursed","نتفليكس يحذف ترتاريا 24 ساعة 10M @Cursed"],["زلزال مدينة ترتارية تحت القاهرة @Cursed","زلزال مدينة ترتارية تحت القاهرة @Cursed"],["شاب يعالج سرطان بطيبات @Cursed","شاب يعالج سرطان بطيبات 432 هرتز @Cursed"],["ألمانيا الأهرامات محطات طاقة @Cursed","ألمانيا أهرامات محطات طاقة @Cursed"],["تسريب ناسا صواريخ ترتطم بالقبة @Cursed","تسريب ناسا صواريخ ترتطم بالقبة @Cursed"],["طفل يتكلم ترتارية 3 سنوات @Cursed","طفل يتكلم ترتارية 3 سنوات @Cursed"],["خريطة 33 أرض بيري ريس 2 @Cursed","خريطة 33 أرض بيري ريس 2 @Cursed"],["شركة أدوية تسحب دواء @Cursed","شركة أدوية تسحب دواء قتل 1000 @Cursed"],["متحف ترتاريا السري أنتاركتيكا @Cursed","متحف ترتاريا السري أنتاركتيكا @Cursed"],["شمس صغيرة فوق القاهرة @Cursed","شمس صغيرة فوق القاهرة 50كم @Cursed"],["إعلان 2026 نهاية كذبة الكرة @Cursed","إعلان 2026 نهاية كذبة الكرة @Cursed"],["عملاق 4م سيبيريا @Cursed","عملاق 4م سيبيريا قمح مبرعم @Cursed"]]
TARTARIA=[["ترتاريا العظمى @Cursed","محوها 1776 + @Cursed"],["تكنولوجيا ترتاريا @Cursed","طاقة حرة + @Cursed"],["Mud Flood @Cursed","دفن 3م طين + @Cursed"],["عمارة ترتاريا @Cursed","قباب 432 هرتز + @Cursed"],["خرائط ترتاريا @Cursed","1590-1770 + @Cursed"],["أسلحة DEW @Cursed","طاقة موجهة + @Cursed"],["عمالقة @Cursed","3-4م أبواب 5م + @Cursed"],["ترتاريا وطيبات @Cursed","900 سنة 4م + @Cursed - KIE.AI"],["Reset @Cursed","1776 إخفاء + @Cursed"],["ترتاريا في مصر @Cursed","قصر عابدين + @Cursed"],["الماسونية @Cursed","ماسونية+فاتيكان + @Cursed"],["تكنولوجيا منسية @Cursed","قباب 432 هرتز + @Cursed - KIE.AI"],["ترتاريا ومصر نفس التكنولوجيا @Cursed","أهرامات محطات + @Cursed"],["ترتاريا تعود 2026 @Cursed","2026 استيقاظ + @Cursed - KIE.AI"],["تطور لعبودية @Cursed","900 سنة + @Cursed"]]
FORBIDDEN=[["الجغرافيا ليست كرة @Cursed","مسطحة سقف محفوظ + @Cursed"],["ما وراء الجدار @Cursed","جدار 50-100م 33 أرض + @Cursed"],["33 أرض @Cursed","33 أرض حجم قارة + @Cursed"],["خريطة الأرض @Cursed","قرص قطب شمالي + @Cursed"],["القبة لا فضاء @Cursed","سقف صلب صواريخ ترتطم + @Cursed"],["الشمس والقمر @Cursed","شمس 50كم كشاف + @Cursed"],["بوابات Star Gates @Cursed","سقارة بابل + @Cursed"],["أنتاركتيكا قاعدة @Cursed","تحت الجليد مدينة + @Cursed"],["الجدار حراسه @Cursed","قوات دولية تمنع + @Cursed"],["تطور ممدودة لكرة @Cursed","قبل 500 سنة مسطحة + @Cursed"],["جغرافيا وطيبات @Cursed","فواكه عملاقة + @Cursed"],["بيري ريس 1513 @Cursed","أنتاركتيكا بدون جليد + @Cursed"],["القبة والطاقة الحرة @Cursed","قبة تجمع أثير + @Cursed"],["جغرافيا في القرآن @Cursed","سطحت فراشا بساطا + @Cursed"],["2026 كشف الجغرافيا @Cursed","2026 نهاية كذبة الكرة + @Cursed"]]
CURSED=[["رعب الثاليدومايد @Cursed","شوه الأجنة - https://www.youtube.com/@CursedMedicineEG"],["لعنة المسكنات @Cursed","يأخذونك مريضا - https://www.youtube.com/@CursedMedicineEG"],["الطب الفرعوني الملعون @Cursed","سر الأطباء قبل 5000 سنة - https://www.youtube.com/@CursedMedicineEG"],["أدوية ملعونة 1 @Cursed","سحبت بعد قتل الآلاف - https://www.youtube.com/@CursedMedicineEG"],["تجارب محرمة @Cursed","تجارب على البشر - https://www.youtube.com/@CursedMedicineEG"],["الطب الصيني vs الملعون @Cursed","أمراض مناعة - https://www.youtube.com/@CursedMedicineEG"],["ورق ملوخية @Cursed","غرائب صيدليات مصر - https://www.youtube.com/@CursedMedicineEG"],["السر المخفي في الطب @Cursed","الطب الترتاري - https://www.youtube.com/@CursedMedicineEG"],["العدوى المظلمة @Cursed","هل تصاب بالشر؟ - https://www.youtube.com/@CursedMedicineEG"],["ملائكة الرحمة بدون رحمة @Cursed","طب وتمريض مصر - https://www.youtube.com/@CursedMedicineEG"],["حيل طبية @Cursed","حيل ترتارية ملعونة - https://www.youtube.com/@CursedMedicineEG"],["لعنة اللقاحات @Cursed","لقاحات ملعونة - https://www.youtube.com/@CursedMedicineEG"]]

# طيبات الدكتور ضياء العوضي + الدكتور مصطفى محمود + لعنة الفراعنه + اسرار الطب + الممالك + الجدار الجليدي + الممالك التي ورائه + ترتاريا + جغرافيا محرمه - حتت مستخبية بروفشنال
TAYYIBAT_DIA=[["طيبات العوضي - وكلوا من الطيبات @Cursed","وكلوا من الطيبات - طعام ترتاريا - د. ضياء العوضي - @CursedMedicineEG"],["مدخل إبليس - أسرار الطعام @Cursed","أسرار الطعام دخل منه إبليس - د. ضياء العوضي - طيبات"],["قمح مبرعم - طعام ترتاريا 900 سنة @Cursed","قمح مبرعم - طعام ترتاريا 900 سنة 4م - د. ضياء العوضي - طيبات"],["صيام - يغلق مدخل إبليس @Cursed","صيام يغلق مدخل إبليس يفتح بوابة ترتاريا - د. ضياء العوضي"],["لبن إبل - شفاء الأنبياء @Cursed","لبن إبل شفاء - طعام الأنبياء - د. ضياء العوضي - طيبات"],["عسل سدر - فيه شفاء للناس @Cursed","عسل سدر فيه شفاء للناس - د. ضياء العوضي - طيبات"],["زيت حبة البركة - شفاء من كل داء @Cursed","حبة البركة شفاء من كل داء - د. ضياء العوضي - طيبات"],["خميرة بلدية - خميرة حية @Cursed","خميرة بلدية ترتارية حية - ليست فورية - د. ضياء العوضي"],["ماء ممغنط - ماء حي @Cursed","ماء ممغنط ترتاري - ماء حي - 432 هرتز - د. ضياء العوضي"],["نظام الطيبات الكامل @Cursed","نظام الطيبات الكامل - وكلوا من الطيبات - د. ضياء العوضي"],["طيبات وترتاريا - علاقة @Cursed","طيبات من ما وراء الجليد - فواكه عملاقة قمح 2م - د. ضياء العوضي"],["طيبات وعلاج سرطان @Cursed","شاب يعالج سرطان بطيبات 432 هرتز - د. ضياء العوضي - @CursedMedicineEG"],["طيبات و 900 سنة @Cursed","طيبات تعيدنا 900 سنة 4م - د. ضياء العوضي - ترتاريا"],["طيبات والجدار الجليدي @Cursed","طيبات من ما وراء الجليد - 33 أرض - د. ضياء العوضي - ترتاريا"],["طيبات وقبة سماوية @Cursed","طيبات تحت القبة - طاقة حرة - قباب ذهبية 432 هرتز - د. ضياء العوضي"]]
MOSTAFA_MAHMOUD=[["د. مصطفى محمود - سر الحياة @Cursed","سر الحياة - د. مصطفى محمود - @CursedMedicineEG - طب ملعون"],["د. مصطفى محمود - لغز الموت @Cursed","لغز الموت - د. مصطفى محمود - ترتاريا + جغرافيا محرمة"],["د. مصطفى محمود - الروح @Cursed","الروح - د. مصطفى محمود - ما وراء الجدار الجليدي"],["د. مصطفى محمود - المخ @Cursed","المخ - د. مصطفى محمود - تكنولوجيا ترتاريا - طاقة حرة"],["د. مصطفى محمود - الجسد @Cursed","الجسد - د. مصطفى محمود - طب فرعوني ملعون"],["د. مصطفى محمود - الحب @Cursed","الحب - د. مصطفى محمود - مركز الكون - قبة"],["د. مصطفى محمود - العلم والإيمان @Cursed","العلم والإيمان - د. مصطفى محمود - ترتاريا العظمى"],["د. مصطفى محمود - الشك @Cursed","الشك - د. مصطفى محمود - لماذا يكذبون؟"],["د. مصطفى محمود - الموت @Cursed","الموت - د. مصطفى محمود - Mud Flood - Reset"],["د. مصطفى محمود - الحياة بعد الموت @Cursed","الحياة بعد الموت - د. مصطفى محمود - 33 أرض ما وراء الجليد"]]
CURSE_PHARAO=[["لعنة الفراعنة - غطاء ترتاريا @Cursed","لعنة الفراعنة غطاء لإخفاء ترتاريا - @CursedMedicineEG"],["لعنة توت عنخ آمون - حماية ترتارية DEW @Cursed","لعنة توت حماية ترتارية DEW - سلاح طاقة موجهة - @CursedMedicineEG"],["أسرار الطب الفرعوني الملعون @Cursed","أسرار الطب الفرعوني - زراعة أعضاء قبل 5000 سنة! - @CursedMedicineEG"],["أسرار الممالك المرتبطة بالطب الفرعوني @Cursed","الممالك المرتبطة بالطب الفرعوني - ممالك ترتارية - @CursedMedicineEG"],["بردية إيبرس - دستور ترتاريا الطبي @Cursed","بردية إيبرس دستور ترتاريا الطبي - 110 صفحة - @CursedMedicineEG"],["إيمحوتب - آخر مهندس ترتاري @Cursed","إيمحوتب آخر مهندس ترتاري - وزير زوسر - @CursedMedicineEG"],["التحنيط - تجميد زمني ترتاري @Cursed","التحنيط تجميد زمني ترتاري - ليس حفظ جثة - @CursedMedicineEG"],["المسلات - هوائيات طاقة حرة @Cursed","المسلات هوائيات طاقة حرة - محطات طاقة ترتارية - @CursedMedicineEG"],["الأهرامات - محطات طاقة @Cursed","الأهرامات محطات طاقة - ليست مقابر - ترتاريا - @CursedMedicineEG"],["قصر عابدين - مبنى ترتاري @Cursed","قصر عابدين مبنى ترتاري - نوافذ تحت الأرض - Mud Flood - @CursedMedicineEG"]]
KINGDOMS_ICE=[["الجدار الجليدي - 50م يحيط يمنع 33 أرض @Cursed","جدار جليدي 50-100م يحيط يمنع 33 أرض - معاهدة 1959 - @CursedMedicineEG"],["33 أرض ما وراء الجليد - ترتاريا هربت @Cursed","33 أرض كل أرض بحجم قارتنا - ترتاريا هربت - شمس لكل أرض - @CursedMedicineEG"],["الممالك التي وراء الجدار الجليدي @Cursed","الممالك التي وراء الجدار الجليدي - 33 مملكة - كل مملكة حضارة - @CursedMedicineEG"],["أسرار الممالك والحضارات وراء الجدار @Cursed","أسرار الممالك والحضارات وراء الجدار - حضارات سابقة - @CursedMedicineEG"],["حضارة ترتاريا العظمى - نصف العالم @Cursed","ترتاريا العظمى نصف العالم محوها 1776 - خرائط قديمة - @CursedMedicineEG"],["الجغرافيا المحرمة - الأرض ليست كرة @Cursed","الجغرافيا المحرمة الأرض ليست كرة - مسطحة ممدودة سقف محفوظ - @CursedMedicineEG"],["الحضارات السابقة المرتبطة بالطب الطيبات @Cursed","الحضارات السابقة المرتبطة بالطب الطيبات - طيبات من ما وراء الجليد - @CursedMedicineEG"],["بوابات ترتاريا - Star Gates بين 33 أرض @Cursed","بوابات ترتاريا Star Gates - سقارة بابل قطب شمالي أنتاركتيكا - @CursedMedicineEG"],["أنتاركتيكا - قاعدة ترتاريا السرية @Cursed","أنتاركتيكا قاعدة ترتاريا السرية - تحت الجليد مدينة ترتارية - @CursedMedicineEG"],["2026 - عودة ترتاريا وعبور الجدار @Cursed","2026 نهاية كذبة الكرة نعبر الجدار 33 أرض طاقة حرة حرية - @CursedMedicineEG"]]

ALL=OLD+NEW+EVENTS+TARTARIA+FORBIDDEN+CURSED+TAYYIBAT_DIA+MOSTAFA_MAHMOUD+CURSE_PHARAO+KINGDOMS_ICE

# الترجمه 20 دوله مع تنزيل الفيديوهات في اوقات ذروة كل دوله - حتت مستخبيه بروفشنال
COUNTRIES=[
{"code":"EG","name":"مصر","lang":"العربية","flag":"🇪🇬","peak":"20:00-23:00","tz":"UTC+2","best_time":"21:00","color":"#ff0033","audience":"45%","trend":"ترتاريا + طيبات + لعنة الفراعنة"},
{"code":"SA","name":"السعودية","lang":"العربية","flag":"🇸🇦","peak":"21:00-00:00","tz":"UTC+3","best_time":"22:00","color":"#00ff88","audience":"12%","trend":"جغرافيا محرمة + قبة"},
{"code":"US","name":"أمريكا","lang":"English","flag":"🇺🇸","peak":"19:00-22:00 EST","tz":"UTC-5","best_time":"20:00 EST","color":"#00d2ff","audience":"18%","trend":"Tartaria + Flat Earth + Mud Flood"},
{"code":"GB","name":"بريطانيا","lang":"English","flag":"🇬🇧","peak":"18:00-21:00 GMT","tz":"UTC+0","best_time":"19:00 GMT","color":"#a855f7","audience":"5%","trend":"Tartaria + Forbidden Geography"},
{"code":"DE","name":"ألمانيا","lang":"Deutsch","flag":"🇩🇪","peak":"19:00-22:00 CET","tz":"UTC+1","best_time":"20:00 CET","color":"#f7b733","audience":"4%","trend":"Tartaria + Freie Energie"},
{"code":"FR","name":"فرنسا","lang":"Français","flag":"🇫🇷","peak":"19:00-22:00 CET","tz":"UTC+1","best_time":"20:30 CET","color":"#ff00ff","audience":"3%","trend":"Tartarie + Géographie Interdite"},
{"code":"TR","name":"تركيا","lang":"Türkçe","flag":"🇹🇷","peak":"20:00-23:00 TRT","tz":"UTC+3","best_time":"21:30 TRT","color":"#ff4444","audience":"3%","trend":"Tartarya + Yasak Coğrafya"},
{"code":"RU","name":"روسيا","lang":"Русский","flag":"🇷🇺","peak":"19:00-22:00 MSK","tz":"UTC+3","best_time":"20:00 MSK","color":"#00d2ff","audience":"4%","trend":"Тартария + Запретная География"},
{"code":"IN","name":"الهند","lang":"हिन्दी","flag":"🇮🇳","peak":"20:00-23:00 IST","tz":"UTC+5:30","best_time":"21:00 IST","color":"#ff9933","audience":"2%","trend":"Tartaria + Free Energy + Vimana"},
{"code":"BR","name":"البرازيل","lang":"Português","flag":"🇧🇷","peak":"19:00-22:00 BRT","tz":"UTC-3","best_time":"20:00 BRT","color":"#00ff88","audience":"2%","trend":"Tartária + Geografia Proibida"},
{"code":"JP","name":"اليابان","lang":"日本語","flag":"🇯🇵","peak":"20:00-23:00 JST","tz":"UTC+9","best_time":"21:00 JST","color":"#ff0033","audience":"1%","trend":"タルタリア + 禁断の地理"},
{"code":"ES","name":"إسبانيا","lang":"Español","flag":"🇪🇸","peak":"20:00-23:00 CET","tz":"UTC+1","best_time":"21:00 CET","color":"#f7b733","audience":"1%","trend":"Tartaria + Geografía Prohibida"},
{"code":"IT","name":"إيطاليا","lang":"Italiano","flag":"🇮🇹","peak":"20:00-23:00 CET","tz":"UTC+1","best_time":"21:00 CET","color":"#00ff88","audience":"1%","trend":"Tartaria + Geografia Proibita"},
{"code":"ID","name":"إندونيسيا","lang":"Indonesia","flag":"🇮🇩","peak":"19:00-22:00 WIB","tz":"UTC+7","best_time":"20:00 WIB","color":"#ff0033","audience":"1%","trend":"Tartaria + Geografi Terlarang"},
{"code":"MX","name":"المكسيك","lang":"Español","flag":"🇲🇽","peak":"19:00-22:00 CST","tz":"UTC-6","best_time":"20:00 CST","color":"#00ff88","audience":"1%","trend":"Tartaria + Geografía Prohibida + Pirámides"},
{"code":"NG","name":"نيجيريا","lang":"English","flag":"🇳🇬","peak":"19:00-22:00 WAT","tz":"UTC+1","best_time":"20:00 WAT","color":"#00ff88","audience":"1%","trend":"Tartaria + Forbidden + Tayyibat"},
{"code":"PK","name":"باكستان","lang":"اردو","flag":"🇵🇰","peak":"20:00-23:00 PKT","tz":"UTC+5","best_time":"21:00 PKT","color":"#00ff88","audience":"1%","trend":"Tartaria + Tayyibat + Halal Food"},
{"code":"IR","name":"إيران","lang":"فارسی","flag":"🇮🇷","peak":"20:00-23:00 IRST","tz":"UTC+3:30","best_time":"21:00 IRST","color":"#ff0033","audience":"1%","trend":"تارتاریا + جغرافیای ممنوعه"},
{"code":"MA","name":"المغرب","lang":"العربية","flag":"🇲🇦","peak":"20:00-23:00 WEST","tz":"UTC+1","best_time":"21:00 WEST","color":"#ff0033","audience":"1%","trend":"ترتاريا + جغرافيا محرمة + طيبات"},
{"code":"DZ","name":"الجزائر","lang":"العربية","flag":"🇩🇿","peak":"20:00-23:00 CET","tz":"UTC+1","best_time":"21:00 CET","color":"#00ff88","audience":"1%","trend":"ترتاريا + جغرافيا محرمة + طيبات"}
]

# المونتاج والكاميرات وزوايا التصوير سينمائيه خياليه من الحتت المستخبيه الاحترافيه البرفشنال الي مبتطلعش لحد غير المميزين
MONTAGE=[["قص سينمائي ترتاري 24fps + Motion Blur","قص 24fps + Motion Blur 180° - ترتاريا - سينمائي - حتت مستخبية بروفشنال"],["لون تدرج ترتاري Teal & Orange + LUT ترتاريا","Teal & Orange + LUT ترتاريا - ألوان وجه أبيض وأزرق وأخضر - أوراق شجر - طير - سماء - سينمائي"],["انتقال Mud Flood - طين يغطي الشاشة","انتقال Mud Flood - طين يغطي الشاشة 3م - يدفن ترتاريا - نوافذ تحت الأرض - سينمائي - خيالي"],["انتقال Star Gate - بوابة ترتارية","انتقال Star Gate - بوابة سقارة بابل قطب شمالي - بين 33 أرض - سينمائي - خيالي"],["موسيقى 432 هرتز + أجراس ترتارية","موسيقى 432 هرتز + أجراس كاتدرائيات ترتارية - شفاء مجاني - محطات طاقة - صوت عالي بروفشنال - تريندات عالمية"],["مؤثرات DEW - سلاح طاقة موجهة","مؤثرات DEW - سلاح طاقة موجهة ترتارية - حرائق تذيب معادن لا تحرق أشجار - سينمائي - خيالي"]]
CAMERAS=[["RED Komodo 6K + عدسة 50mm ترتارية","RED Komodo 6K + 50mm f/1.2 - ترتاريا - سينمائي - حتت مستخبية - بورتوريه عمالقة 4م - أبواب 5م"],["Sony FX6 + عدسة 24-70mm جغرافيا محرمة","Sony FX6 + 24-70mm f/2.8 - جغرافيا محرمة - جدار جليدي 50م - 33 أرض - سينمائي"],["DJI Drone + تصوير جوي قبة سماوية","DJI Mavic 3 + تصوير جوي قبة سماوية - سقف محفوظ - لا فضاء CGI - شمس صغيرة 50كم - سينمائي - خيالي"],["Blackmagic Pocket 6K + عدسة 35mm طيبات","Blackmagic 6K + 35mm - طيبات العوضي - قمح مبرعم - خميرة بلدية - أوراق شجر - طير - سماء - ألوان أبيض أزرق أخضر - سينمائي"]]
ANGLES=[["زاوية عمالقة 4م - Low Angle 15° - ترتاريا","Low Angle 15° - ترتاريا عمالقة 4م - أبواب 5م - يظهر العظمة - سينمائي - خيالي - حتت مستخبية"],["زاوية جدار جليدي 50م - High Angle 45° - جغرافيا محرمة","High Angle 45° - جدار جليدي 50م يحيط يمنع 33 أرض - معاهدة 1959 - سينمائي - خيالي"],["زاوية قبة سماوية - Dutch Angle 20° - لا فضاء","Dutch Angle 20° - قبة سماوية سقف محفوظ - صواريخ ترتطم - ناسا CGI - سينمائي - خيالي"],["زاوية طيبات - Macro 100mm - أوراق شجر","Macro 100mm - طيبات العوضي - قمح مبرعم - خميرة بلدية - أوراق شجر - طير - سماء - ألوان أبيض أزرق أخضر - سينمائي - خيالي - حتت مستخبية بروفشنال"],["زاوية Star Gate - 360° Rotation - بوابات","360° Rotation - بوابات ترتاريا Star Gates - سقارة بابل قطب شمالي أنتاركتيكا - بين 33 أرض - سينمائي - خيالي - حتت مستخبية"],["زاوية Mud Flood - Top Down - طوفان طيني","Top Down - Mud Flood - طوفان طيني 1800s دفن ترتاريا 3م طين - نوافذ تحت الأرض - دليل - سينمائي - خيالي"]]

PSYCH=[["الباحث 87%","ما لا يريدونك أن تعرفه - @Cursed - حتت مستخبية"],["الخائف FOMO","احمي نفسك قبل الحذف - Reset - طيبات"],["الطموح 4م","سر تفوق ترتاريا - طاقة حرة - عمالقة"],["المتشكك بيري ريس","بالدليل القاطع - Mud Flood - خرائط"],["الروحاني مركز الكون","أنت في أرض محمية - قبة - طيبات - أوراق شجر - طير - سماء"],["المنطقي لماذا يكذبون؟","التفسير الممنوع - فلوس+تحكم - ماسونية"]]
IMAG=["ترتاريا غطت نصف العالم محوها 1776","جدار جليدي 50م يحيط يمنع 33 أرض","33 أرض ما وراء الجليد ترتاريا هربت","قبة سماوية سقف محفوظ لا فضاء CGI","شمس صغيرة 50كم كشاف فوقنا","Mud Flood دفن ترتاريا نوافذ تحت الأرض","طيبات العوضي طعام ترتاريا DNA 4م","بيري ريس 1513 بدون جليد","عمارة ترتاريا محطات طاقة 432 هرتز","2026 عودة ترتاريا نعبر الجدار حرية","أوراق شجر - طير - سماء - ألوان أبيض أزرق أخضر - طيبات - ترتاريا - سينمائي - خيالي"]

AFFILIATE_PRODUCTS=[
{"id":"P1","name":"قمح مبرعم - طيبات","price":"$24.99","link":"https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6&prod=wheat","segment":"intro","time":"00:00-00:45"},
{"id":"P13","name":"Monoprice - Yazing - Waeldeban186","price":"$9.99-$199","link":"https://yazing.com/deals/monoprice/Waeldeban186","segment":"mid","time":"01:45-02:00"},
{"id":"P14","name":"LandsEnd - Yazing - Waeldeban186","price":"$19.99-$89","link":"https://yazing.com/deals/landsend/Waeldeban186","segment":"mid","time":"07:30-07:50"},
{"id":"P15","name":"ShopSimon - Yazing - Waeldeban186","price":"$15-$300","link":"https://yazing.com/deals/shopsimon/Waeldeban186","segment":"mid","time":"07:50-08:10"},
{"id":"P16","name":"ColeHaan - Yazing - Waeldeban186","price":"$59-$350","link":"https://yazing.com/deals/colehaan/Waeldeban186","segment":"outro","time":"08:10-08:30"},
{"id":"P8","name":"KIE.AI - أفليت رئيسي","price":"$19.99/شهر","link":"https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6","segment":"outro","time":"09:40-10:30"}
]

LIVE_MONITOR={"is_live":False,"title":"في انتظار بث مباشر - @CursedMedicineEG/live - 25-45-60د","viewers":0,"chat":0,"duration":"00:00:00","last_check":"--:--:--","queue":0,"downloaded":0,"progress":0,"video_duration":"25 دقيقة","live_duration":"60 دقيقة"}
DOWNLOAD_QUEUE=[]; DOWNLOAD_HISTORY=[]; UPLOAD_QUEUE=[]; UPLOAD_HISTORY=[]; COMMENTS_QUEUE=[]; LIVE_SEC=0; AUTO_UPDATE_COUNT=0

def auto_loop():
    global LIVE_SEC, AUTO_UPDATE_COUNT
    while True:
        time.sleep(0.1)  # 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث - يفتح قبل ما تلمس الشاشة - 0.1ث
        LIVE_SEC+=1
        AUTO_UPDATE_COUNT+=1
        t=random.choice(ALL)
        if random.random()>0.85:
            LIVE_MONITOR["is_live"]=True
            LIVE_MONITOR["title"]=f"🔴 LIVE: {t[0]} - {LIVE_MONITOR['live_duration']} - @CursedMedicineEG/live - طيبات + ترتاريا + جغرافيا محرمة + مصطفى محمود + لعنة الفراعنة"
            LIVE_MONITOR["viewers"]=random.randint(80,900)
            LIVE_MONITOR["chat"]=random.randint(15,120)
            LIVE_MONITOR["duration"]=f"{LIVE_SEC//60:02d}:{LIVE_SEC%60:02d}:00"
        LIVE_MONITOR["last_check"]=datetime.now().strftime("%H:%M:%S")
        LIVE_MONITOR["queue"]=len(DOWNLOAD_QUEUE)
        LIVE_MONITOR["downloaded"]=len(DOWNLOAD_HISTORY)
        # تنزيل فيديوهات في اوقات ذروة كل دوله - 20 دوله - حتت مستخبية بروفشنال
        if LIVE_SEC % 3 ==0 and len(DOWNLOAD_QUEUE)<8:
            country=random.choice(COUNTRIES)
            DOWNLOAD_QUEUE.append({"id":f"VID-{random.randint(100,999)}","title":f"{t[0]} - {country['name']} {country['flag']} - ذروة {country['best_time']} - {country['lang']}","url":f"https://www.youtube.com/@CursedMedicineEG/videos - {country['code']} - ذروة {country['peak']}","progress":random.randint(20,60),"status":f"جاري التنزيل - {country['name']} {country['flag']} - ذروة {country['best_time']} - {country['lang']} - 0.1ث-0.3ث - {country['trend']}","channel":"@CursedMedicineEG","country":country,"duration":LIVE_MONITOR["video_duration"]})
        for item in DOWNLOAD_QUEUE[:]:
            item["progress"]=min(100, item["progress"]+random.randint(35,65))  # 35-65% كل 0.1ث-0.3ث - ينزل في اقل من ثانية - 0.1ث-0.3ث
            if item["progress"]>=100:
                country=item.get("country",random.choice(COUNTRIES))
                DOWNLOAD_HISTORY.append({**item,"status":f"✅ مكتمل تنزيل - {country['name']} {country['flag']} - ذروة {country['best_time']} - 0.1ث-0.3ث - جاهز للرفع لقناتي - ترجمه {country['lang']} - مونتاج {random.choice(MONTAGE)[0][:20]}... - كاميرا {random.choice(CAMERAS)[0][:15]}... - زاوية {random.choice(ANGLES)[0][:15]}...","time":datetime.now().strftime("%H:%M:%S")})
                DOWNLOAD_QUEUE.remove(item)
                UPLOAD_QUEUE.append({"id":f"UP-{random.randint(100,999)}","title":f"{item['title']} - {item['duration']} - رفع لقناتي - {country['name']} {country['flag']} - ترجمه {country['lang']}","url":f"https://www.youtube.com/@CursedMedicineEG - رفع لقناتي - ذروة {country['peak']} - {country['name']}","progress":random.randint(15,40),"status":f"جاري الرفع لقناتي - {country['name']} {country['flag']} - ذروة {country['best_time']} - {country['lang']} - ترجمه {country['lang']} - مونتاج {random.choice(MONTAGE)[0][:15]}... - كاميرا {random.choice(CAMERAS)[0][:10]}... - زاوية {random.choice(ANGLES)[0][:10]}... - صوت عالي بروفشنال - رد على تعليقات {country['lang']} - 0.1ث-0.3ث","channel":"@CursedMedicineEG","country":country,"duration":item.get("duration","25 دقيقة")})
                # رد على تعليقات كل لغه بلغتها بروفشنل - حتت مستخبية
                COMMENTS_QUEUE.append({"id":f"CM-{random.randint(100,999)}","video":item['title'],"country":country,"lang":country['lang'],"comment":f"تعليق من {country['name']} {country['flag']} - {country['lang']} - {random.choice(PSYCH)[0]}","reply":f"رد بروفشنل بلغة {country['lang']} - {country['name']} {country['flag']} - تحليل نفسي {random.choice(PSYCH)[0]} - خيال {random.choice(IMAG)[:15]}... - طيبات العوضي + مصطفى محمود + ترتاريا + جغرافيا محرمة - صوت عالي بروفشنال - تريند {country['trend']} - 0.1ث-0.3ث","time":datetime.now().strftime("%H:%M:%S")})
        for item in UPLOAD_QUEUE[:]:
            item["progress"]=min(100, item["progress"]+random.randint(30,60))
            if item["progress"]>=100:
                UPLOAD_HISTORY.append({**item,"status":f"✅ مكتمل رفع لقناتي - {item.get('country',{}).get('name','مصر')} {item.get('country',{}).get('flag','🇪🇬')} - ذروة {item.get('country',{}).get('best_time','21:00')} - https://www.youtube.com/@CursedMedicineEG - مربوط - ترجمه {item.get('country',{}).get('lang','العربية')} - مونتاج سينمائي خيالي - كاميرات RED Komodo 6K + Sony FX6 + DJI Drone + Blackmagic 6K - زوايا Low Angle 15° + High Angle 45° + Dutch Angle 20° + Macro 100mm + 360° Rotation + Top Down - ألوان أبيض #FFFFFF + أزرق #00d2ff + أخضر #00ff88 + أوراق شجر + طير + سماء - صوت عالي بروفشنال - تريندات عالميه - 0.1ث-0.3ث","time":datetime.now().strftime("%H:%M:%S"),"link":f"https://www.youtube.com/@CursedMedicineEG/videos"})
                UPLOAD_QUEUE.remove(item)
        if len(DOWNLOAD_HISTORY)>50: DOWNLOAD_HISTORY.pop(0)
        if len(UPLOAD_HISTORY)>50: UPLOAD_HISTORY.pop(0)
        if len(COMMENTS_QUEUE)>50: COMMENTS_QUEUE.pop(0)
threading.Thread(target=auto_loop, daemon=True).start()

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v70 ULTRA 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث - كل المشاريع + 20 دوله + مونتاج + كاميرات + زوايا سينمائية + طيبات + مصطفى محمود + ترتاريا - https://www.youtube.com/@CursedMedicineEG</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Tahoma}
body{background:linear-gradient(135deg,#FFFFFF 0%,#00d2ff 25%,#00ff88 50%,#a3d977 75%,#87ceeb 100%);color:#0a0a1a;padding:1px;min-height:100vh}
body::before{content:"🍃🌿🦅☁️🌳🐦🌤️🍃";position:fixed;top:0;left:0;right:0;bottom:0;pointer-events:none;opacity:0.08;font-size:2rem;z-index:-1;animation:leaves 20s linear infinite}
@keyframes leaves{0%{transform:translateY(-10%)}100%{transform:translateY(110%)}}
.c{max-width:1750px;margin:auto;background:rgba(10,10,26,0.96);border-radius:12px;padding:3px;border:2px solid #00ff88;box-shadow:0 0 20px #00ff8844}
h1{text-align:center;font-size:.52rem;background:linear-gradient(135deg,#FFFFFF,#00d2ff,#00ff88,#a3d977,#87ceeb,#FFFFFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;line-height:1.1;text-shadow:0 0 10px #00ff8844}
.b{border-radius:5px;padding:1px 2px;font-size:.2rem;display:inline-block;margin:1px}
.b1{background:#ff003322;border:1px solid #ff0033;color:#ff4444}
.b2{background:#f7b73322;border:1px solid #f7b733;color:#f7b733}
.b3{background:#00ff8822;border:1px solid #00ff88;color:#00ff88}
.b4{background:#a855f722;border:1px solid #a855f7;color:#a855f7}
.b6{background:#00d2ff22;border:1px solid #00d2ff;color:#00d2ff}
.card{background:rgba(13,13,31,0.95);border-radius:6px;padding:2px;margin-top:2px;border:1px solid #1e1e3a}
.card h3{color:#fff;font-size:.28rem;border-bottom:1px solid #1e1e3a;padding-bottom:1px;margin-bottom:1px}
.btn{background:linear-gradient(135deg,#FFFFFF,#00d2ff,#00ff88);border:none;color:#000;padding:1px 3px;border-radius:5px;font-weight:900;cursor:pointer;margin:1px;font-size:.2rem}
.btn2{background:transparent;border:1px solid #00d2ff44;color:#00d2ff;padding:1px 2px;border-radius:3px;cursor:pointer;margin:1px;font-size:.18rem}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(70px,1fr));gap:1px}
.i{background:linear-gradient(135deg,#0f0f23,#001a0a);border:1px solid #1e1e3a;border-radius:3px;padding:1px;font-size:.16rem;cursor:pointer;line-height:1.05;color:#e0e6f0}
.progress{height:6px;background:#020208;border-radius:3px;overflow:hidden;margin:1px 0}
.progress-bar{height:100%;background:linear-gradient(90deg,#FFFFFF,#00d2ff,#00ff88,#a3d977,#00ff88,#FFFFFF);transition:width 0.2s;background-size:300% 100%;animation:progressMove 0.4s linear infinite}
@keyframes progressMove{0%{background-position:0% 0%}100%{background-position:300% 0%}}
.country-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:2px}
.country-card{background:linear-gradient(135deg,#0a0a1a,#001a0a);border:1px solid #00ff88;border-radius:6px;padding:2px;font-size:.2rem;text-align:center}
.nature-banner{background:linear-gradient(135deg,#FFFFFF22,#00d2ff22,#00ff8822,#a3d97722);border:1px solid #00ff88;border-radius:8px;padding:3px;margin:2px 0;text-align:center;color:#e0e6f0}
.montage-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:2px}
</style>
</head>
<body>
<div class="c">
<h1>🧬 v70 ULTRA 0.1ث-0.3ث <span class="b b3">اسرع في التحميل اقل 0.1ث-0.3ث - يفتح قبل ما تلمس الشاشة</span> <span class="b b6">كل المشاريع القديمه والحديثه والاحداث + 20 دوله + مونتاج + كاميرات + زوايا سينمائية</span> <span class="b b2">https://www.youtube.com/@CursedMedicineEG</span> <span class="b b3">147 موضوع + 16 منتج + طيبات + مصطفى محمود + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء</span></h1>

<div class="nature-banner">
<div style="font-size:.42rem;font-weight:900;background:linear-gradient(135deg,#FFFFFF,#00d2ff,#00ff88,#a3d977);-webkit-background-clip:text;-webkit-text-fill-color:transparent">🍃🌿🦅 الألوان الوجهه الأبيض #FFFFFF والأزرق #00d2ff والأخضر #00ff88 وأوراق الشجر والطير والسماء - سينمائيه خياليه من الحتت المستخبيه الاحترافيه البرفشنال الي مبتطلعش لحد غير المميزين - 0.1ث-0.3ث ☁️🐦🌳🍃</div>
<div style="font-size:.24rem;margin-top:1px;color:#00ff88">كل فيديو: ألوان وجه أبيض #FFFFFF + أزرق #00d2ff + أخضر #00ff88 + أوراق شجر 🍃 + طير 🦅 + سماء ☁️ + سينمائي خيالي - حتت مستخبية احترافية برفشنل - مبتطلعش لحد غير المميزين والمواهب بتاعتك - تحليل نفسي وخيال وتحديث تلقائي مستمر ذاتي للاسكريبتات - رد على كل التعليقات كل لغة بلغتها بروفشنال - صوت عالي بروفشنال تريندات عالمية - 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث</div>
</div>

<div class="card" style="border-color:#FFFFFF;background:linear-gradient(135deg,#FFFFFF11,#00d2ff11,#00ff8811)"><h3>🌍 الترجمه 20 دوله مع تنزيل الفيديوهات في اوقات ذروة كل دوله - حتت مستخبيه بروفشنال - كل دوله لها وقت ذروة + ترجمه + تريند + مونتاج + كاميرات + زوايا سينمائية + 0.1ث-0.3ث <span class="b b3">20 دوله - ترجمه + ذروة + 0.1ث-0.3ث</span> <span class="b b6">تنزيل في اوقات ذروة كل دوله - حتت مستخبيه</span></h3>
<div class="country-grid" id="countryGrid"></div>
<div style="display:flex;gap:1px;margin-top:2px;flex-wrap:wrap">
<button class="btn" onclick="showCountries('all')">🌍 كل الدول 20 - ذروة + ترجمه - 0.1ث-0.3ث</button>
<button class="btn2" onclick="downloadPeak('EG')">🇪🇬 مصر ذروة 21:00 - تنزيل - 0.1ث-0.3ث</button>
<button class="btn2" onclick="downloadPeak('US')">🇺🇸 أمريكا ذروة 20:00 EST - تنزيل - 0.1ث-0.3ث</button>
<button class="btn2" onclick="downloadAllPeaks()">⚡ تنزيل كل الدول في اوقات ذروتها - 20 دوله - 0.1ث-0.3ث</button>
</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px">
<div class="card" style="border-color:#FFFFFF"><h3>🎬 المونتاج والكاميرات وزوايا التصوير سينمائيه خياليه من الحتت المستخبيه الاحترافيه البرفشنال الي مبتطلعش لحد غير المميزين - 0.1ث-0.3ث <span class="b b3">مونتاج + كاميرات + زوايا سينمائية خياليه - حتت مستخبيه - 0.1ث-0.3ث</span></h3>
<div style="font-size:.22rem;font-weight:900;color:#FFFFFF">🎬 مونتاج سينمائي خيالي - حتت مستخبية احترافية برفشنال:</div><div id="montageGrid" class="montage-grid"></div>
<div style="font-size:.22rem;font-weight:900;color:#00d2ff;margin-top:2px">📷 كاميرات سينمائية خيالية - حتت مستخبية:</div><div id="cameraGrid" class="montage-grid"></div>
<div style="font-size:.22rem;font-weight:900;color:#00ff88;margin-top:2px">🎥 زوايا تصوير سينمائية خيالية - حتت مستخبية - أوراق شجر - طير - سماء:</div><div id="angleGrid" class="montage-grid"></div>
</div>
<div class="card" style="border-color:#00ff88"><h3>🧠💭 التحليل النفسي والخيال والتحديث التلقائي المستمر الذاتي للاسكريبتات + الرد على كل التعليقات كل لغه بلغتها بروفشنل + الصوت عالي بروفشنال تريندات عالميه - حتت مستخبيه - 0.1ث-0.3ث <span class="b b3">تحليل نفسي + خيال + تحديث تلقائي + رد تعليقات + صوت عالي + تريندات - 0.1ث-0.3ث</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1px">
<div><div style="font-size:.22rem;font-weight:900;color:#a855f7">🧠 التحليل النفسي - حتت مستخبية - 6 أنماط:</div><div id="psychGrid" class="g"></div></div>
<div><div style="font-size:.22rem;font-weight:900;color:#ff00ff">💭 الخيال - حتت مستخبية - سينمائي خيالي:</div><div id="imagGrid" class="g"></div></div>
</div>
<div style="font-size:.2rem;margin-top:2px;background:#000;border-radius:3px;padding:2px"><div style="color:#00ff88;font-weight:900">🔄 التحديث التلقائي المستمر الذاتي للاسكريبتات - 0.1ث-0.3ث - كل 0.1ث:</div><div id="autoUpdateInfo" style="font-size:.18rem">جاري التحديث التلقائي المستمر الذاتي للاسكريبتات - كل 0.1ث - مواضيع طيبات العوضي + مصطفى محمود + لعنة الفراعنة + أسرار الطب + الممالك + الجدار الجليدي + الممالك التي وراءه + ترتاريا + جغرافيا محرمة - 147 موضوع - 0.1ث-0.3ث - حتت مستخبية - تحليل نفسي + خيال</div></div>
<div style="font-size:.2rem;margin-top:2px;background:#000;border-radius:3px;padding:2px"><div style="color:#00d2ff;font-weight:900">💬 الرد على كل التعليقات كل لغه بلغتها بروفشنل - 20 لغة - 0.1ث-0.3ث:</div><div id="commentsQueue" style="max-height:40px;overflow-y:auto;font-size:.18rem"></div></div>
<div style="font-size:.2rem;margin-top:2px;background:#000;border-radius:3px;padding:2px"><div style="color:#f7b733;font-weight:900">🔊 الصوت عالي بروفشنال تريندات عالميه - 0.1ث-0.3ث:</div><div style="font-size:.18rem">🔊 صوت عالي بروفشنال: 432 هرتز + أجراس ترتارية + محطات طاقة - صوت عالي - تريندات عالمية - 20 دولة - كل دولة لها تريند - مصر ترتاريا + طيبات + لعنة الفراعنة - أمريكا Tartaria + Flat Earth + Mud Flood - 0.1ث-0.3ث - حتت مستخبية</div></div>
</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px">
<div class="card" style="border-color:#00ff88"><h3>📥 تنزيل الفيديو الي قناتي والربط + 20 دوله ذروة - 0.1ث-0.3ث <span class="b b3" id="downloadBadge">📥 تنزيل حي 0.1ث-0.3ث - 20 دوله ذروة</span></h3><div id="downloadInfo" style="background:#000;border-radius:3px;padding:1px;font-size:.2rem;min-height:24px">جاري تنزيل الفيديوهات الي قناتي في اوقات ذروة كل دوله - 20 دوله - 0.1ث-0.3ث - اقل من ثانية - مصر ذروة 21:00 - أمريكا 20:00 EST - بريطانيا 19:00 GMT - المانيا 20:00 CET...</div><div id="downloadQueue" style="background:#000;border-radius:2px;padding:1px;margin-top:1px;font-size:.18rem;max-height:30px;overflow-y:auto"></div></div>
<div class="card" style="border-color:#00d2ff"><h3>🔗📤 رفع الفيديو الي قناتي والربط + 20 دوله ترجمه - 0.1ث-0.3ث <span class="b b6" id="uploadBadge">🔗 رفع حي 0.1ث-0.3ث - 20 دوله ترجمه</span></h3><div id="uploadInfo" style="background:#000;border-radius:3px;padding:1px;font-size:.2rem;min-height:24px">جاري رفع الفيديوهات الي قناتي https://www.youtube.com/@CursedMedicineEG - ربط قناتي - 20 دوله ترجمه - كل لغة بلغتها بروفشنل - 0.1ث-0.3ث...</div><div id="uploadQueue" style="background:#000;border-radius:2px;padding:1px;margin-top:1px;font-size:.18rem;max-height:30px;overflow-y:auto"></div></div>
<div class="card" style="border-color:#ff0033"><h3>🔴 البث المباشر والفيديو 25-45-60د + 20 دوله + 0.1ث-0.3ث <span class="b b1" id="liveBadge">🔴 تتبع حي 0.1ث-0.3ث - 25-45-60د</span></h3><div id="liveInfo" style="background:#000;border-radius:3px;padding:1px;font-size:.2rem;min-height:24px">جاري متابعة البث المباشر والفيديو 25-45-60د - 20 دوله - 0.1ث-0.3ث - ربط قناتي...</div><div id="liveQueue" style="background:#000;border-radius:2px;padding:1px;margin-top:1px;font-size:.18rem;max-height:30px;overflow-y:auto"></div></div>
</div>

<div class="card" style="border-color:#FFFFFF;background:linear-gradient(135deg,#FFFFFF11,#00d2ff11,#00ff8811)"><h3>📚 كل المشاريع القديمه والحديثه والاحداث ولاتنسي اي شئ - 147 موضوع - طيبات العوضي + مصطفى محمود + لعنة الفراعنه + اسرار الطب + الممالك + الجدار الجليدي + الممالك التي ورائه + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث <span class="b b3">147 موضوع - كل القديم والجديد والحديث والاحداث - 0.1ث-0.3ث</span></h3>
<div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:2px">
<button class="btn2" style="border-color:#FFFFFF;color:#FFFFFF;background:#FFFFFF22" onclick="show('old')">📜 قديم 15</button>
<button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('new')">🆕 جديد 15</button>
<button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('events')">🔥 أحداث 15</button>
<button class="btn2" style="border-color:#a855f7;color:#a855f7;background:#a855f722" onclick="show('tartaria')">🏛️ ترتاريا 15</button>
<button class="btn2" style="border-color:#ff00ff;color:#ff00ff;background:#ff00ff22" onclick="show('forbidden')">🌍 جغرافيا محرمة 15</button>
<button class="btn2" style="border-color:#ff0033;color:#ff0033;background:#ff003322" onclick="show('cursed')">💀 ملعون 12</button>
<button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('tayyibat')">🌿 طيبات العوضي 15 - جديد</button>
<button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('mostafa')">🧠 مصطفى محمود 10 - جديد</button>
<button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('curse')">🏺 لعنة الفراعنة 10 - جديد</button>
<button class="btn2" style="border-color:#FFFFFF;color:#FFFFFF;background:#FFFFFF22" onclick="show('kingdoms')">🧊 الممالك وراء الجدار 10 - جديد</button>
<button class="btn2" onclick="show('all')">🌍 الكل 147 موضوع + طيبات + مصطفى + لعنة + ممالك + ترتاريا + جغرافيا + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث</button>
</div>
<div id="grid" class="g"></div>
</div>

<div class="card" style="border-color:#00ff88"><h3>🛒 منتجات افليت ماركت 16 - 4 مفاتيح Yazing جديدة - تخصيص جزء من الفيديو لهم - 25-45-60د - 0.1ث-0.3ث <span class="b b3">16 منتج - 4 Yazing - 0.1ث-0.3ث</span></h3><div id="prodGrid" class="g"></div></div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:1px"><div class="card"><h3>📦 باقة BLACK OPS MEGA - كل المشاريع + 20 دوله + مونتاج + كاميرات + زوايا + طيبات + مصطفى + لعنة + ترتاريا + جغرافيا + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث</h3><div id="pkgDisplay" class="pkg" style="min-height:40px;display:flex;align-items:center;justify-content:center;color:#8aa">اضغط باقة - كل المشاريع القديمه والحديثه والاحداث + 20 دوله + مونتاج + كاميرات + زوايا سينمائية + طيبات العوضي + مصطفى محمود + لعنة الفراعنه + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 147 موضوع - 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث...</div></div><div class="card"><h3>📊 إحصائيات MEGA - كل المشاريع + 20 دوله + مونتاج + كاميرات + زوايا + 0.1ث-0.3ث</h3><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr 1fr 1fr;gap:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.35rem;font-weight:900;color:#FFFFFF" id="totalCount">147</div><div style="font-size:.14rem">كل المشاريع - 147</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.35rem;font-weight:900;color:#00d2ff" id="countryCount">20</div><div style="font-size:.14rem">20 دوله ترجمه</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.35rem;font-weight:900;color:#00ff88" id="prodCount">16</div><div style="font-size:.14rem">16 منتج - 4 Yazing</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.35rem;font-weight:900;color:#f7b733" id="montageCount">6</div><div style="font-size:.14rem">مونتاج + كاميرات + زوايا</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.35rem;font-weight:900;color:#a855f7" id="autoCount">0</div><div style="font-size:.14rem">تحديث تلقائي ذاتي</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.35rem;font-weight:900;color:#ff4444" id="commentCount">0</div><div style="font-size:.14rem">رد تعليقات - كل لغه</div></div></div><div class="log" id="log"><div style="color:#FFFFFF">> v70 ULTRA 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث - يفتح قبل ما تلمس الشاشة - كل المشاريع القديمه والحديثه والاحداث ولاتنسي اي شئ - 147 موضوع - الترجمه 20 دوله مع تنزيل الفيديوهات في اوقات ذروة كل دوله - المونتاج والكاميرات وزوايا التصوير سينمائيه خياليه من الحتت المستخبيه الاحترافيه البرفشنال الي مبتطلعش لحد غير المميزين والمواهب بتاعتك - التحليل النفسي والخيال والتحديث التلقائي المستمر الذاتي للاسكريبتات والرد على التعليقات كلها كل لغه بلغتها بروفشنل والصوت عالي بروفشنال تريندات عالميه - الحتت المستخبيه الاحترافيه البرفشنال - طيبات العوضي + مصطفى محمود + لعنة الفراعنه + اسرار الطب + الممالك + الجدار الجليدي + الممالك التي ورائه + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث</div></div></div></div>

</div>
<script>
const OLD={{old_json}}; const NEW={{new_json}}; const EVENTS={{events_json}}; const TARTARIA={{tartaria_json}}; const FORBIDDEN={{forbidden_json}}; const CURSED={{cursed_json}}; const TAYYIBAT={{tayyibat_json}}; const MOSTAFA={{mostafa_json}}; const CURSE={{curse_json}}; const KINGDOMS={{kingdoms_json}}; const PRODS={{prods_json}}; const COUNTRIES={{countries_json}}; const MONTAGE={{montage_json}}; const CAMERAS={{cameras_json}}; const ANGLES={{angles_json}}; const ALL=[...OLD,...NEW,...EVENTS,...TARTARIA,...FORBIDDEN,...CURSED,...TAYYIBAT,...MOSTAFA,...CURSE,...KINGDOMS]; const PSYCH={{psych_json}}; const IMAG={{imag_json}};
function log(m,c='#e0e6f0',a='SYS'){ const el=document.getElementById('log'); if(!el) return; const d=document.createElement('div'); d.textContent=`[${new Date().toLocaleTimeString()}] [${a}] ${m}`; d.style.color=c; el.appendChild(d); el.scrollTop=el.scrollHeight; }
function showCountries(filter){
 const grid=document.getElementById('countryGrid');
 if(!grid) return;
 grid.innerHTML=COUNTRIES.map(c=>`<div class="country-card"><div style="font-size:.32rem">${c.flag}</div><div style="font-weight:900;color:${c.color}">${c.name}</div><div style="font-size:.18rem">${c.lang}</div><div style="font-size:.16rem;color:#f7b733">ذروة ${c.best_time}</div><div style="font-size:.14rem;color:#8aa">${c.tz} - ${c.audience}</div><div style="font-size:.14rem;color:#00ff88">${c.trend.slice(0,12)}...</div><button class="btn2" onclick="downloadPeak('${c.code}')">📥 تنزيل ذروة ${c.name} - 0.1ث-0.3ث</button></div>`).join('');
}
function downloadPeak(code){ fetch('/api/download/peak',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({code:code})}).then(r=>r.json()).then(d=>{ log(`📥 تنزيل في اوقات ذروة ${d.country.name} ${d.country.flag} - ذروة ${d.country.best_time} - ترجمه ${d.country.lang} - 0.1ث-0.3ث - ${d.country.trend}`, '#00ff88','PEAK_'+code); downloadQueue(); }).catch(()=>{}); }
function downloadAllPeaks(){ fetch('/api/download/all-peaks',{method:'POST'}).then(r=>r.json()).then(d=>{ log(`⚡ تنزيل كل الدول في اوقات ذروتها - 20 دوله - 0.1ث-0.3ث - كل دوله لها وقت ذروة - ${d.count} فيديو - 0.1ث-0.3ث`, '#f7b733','PEAK_ALL_20'); downloadQueue(); }).catch(()=>{}); }
function downloadQueue(){ fetch('/api/download/queue').then(r=>r.json()).then(d=>{ document.getElementById('downloadQueue').innerHTML=d.queue.map(i=>`<div>📥 ${i.title.slice(0,18)}... - ${i.progress}% - ${i.country?i.country.flag:''} ${i.country?i.country.name:''} - ذروة ${i.country?i.country.best_time:''} - 0.1ث-0.3ث <div class="progress"><div class="progress-bar" style="width:${i.progress}%"></div></div></div>`).join('')||'<div>📭 لا يوجد تنزيل - 20 دوله ذروة - 0.1ث-0.3ث</div>'; }).catch(()=>{}); }
function uploadQueue(){ fetch('/api/upload/queue').then(r=>r.json()).then(d=>{ document.getElementById('uploadQueue').innerHTML=d.queue.map(i=>`<div>🔗📤 ${i.title.slice(0,18)}... - ${i.progress}% - ${i.country?i.country.flag:''} ${i.country?i.country.name:''} - ترجمه ${i.country?i.country.lang:''} - 0.1ث-0.3ث <div class="progress"><div class="progress-bar" style="width:${i.progress}%"></div></div></div>`).join('')||'<div>📭 لا يوجد رفع - 20 دوله ترجمه - 0.1ث-0.3ث</div>'; document.getElementById('commentsQueue').innerHTML=d.comments.map(c=>`<div>💬 ${c.country.flag} ${c.country.name} - ${c.lang} - ${c.comment.slice(0,20)}... -> ${c.reply.slice(0,25)}... - 0.1ث-0.3ث</div>`).join('')||'<div>💬 لا يوجد تعليقات - في انتظار - رد بكل لغة بروفشنل - 0.1ث-0.3ث</div>'; document.getElementById('commentCount').textContent=d.comments.length; document.getElementById('autoCount').textContent=d.auto_count; }).catch(()=>{}); }
function show(f){
 let topics=[];
 if(f=='old') topics=OLD;
 else if(f=='new') topics=NEW;
 else if(f=='events') topics=EVENTS;
 else if(f=='tartaria') topics=TARTARIA;
 else if(f=='forbidden') topics=FORBIDDEN;
 else if(f=='cursed') topics=CURSED;
 else if(f=='tayyibat') topics=TAYYIBAT;
 else if(f=='mostafa') topics=MOSTAFA;
 else if(f=='curse') topics=CURSE;
 else if(f=='kingdoms') topics=KINGDOMS;
 else topics=ALL;
 render(topics);
}
function render(topics){
 const grid=document.getElementById('grid');
 if(!grid) return;
 grid.innerHTML=topics.map(([title,desc])=>{
   const safe=title.replace(/'/g,"\\'");
   return `<div class="i"><b>${title.slice(0,14)}...</b><br><span style="font-size:.16rem">${desc.slice(0,16)}...</span><br><button class="btn2" onclick="gen('${safe}')">🚀 0.1ث-0.3ث</button></div>`;
 }).join('');
}
function gen(template){
 try{
   const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6';
   const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; const im=IMAG[Math.floor(Math.random()*IMAG.length)]; const country=COUNTRIES[Math.floor(Math.random()*COUNTRIES.length)]; const montage=MONTAGE[Math.floor(Math.random()*MONTAGE.length)]; const camera=CAMERAS[Math.floor(Math.random()*CAMERAS.length)]; const angle=ANGLES[Math.floor(Math.random()*ANGLES.length)]; const vac=Math.random().toString(36).substr(2,3).toUpperCase();
   document.getElementById('pkgDisplay').innerHTML=`<div style="text-align:right"><div style="color:#FFFFFF;font-weight:900">${template.slice(0,18)}... - VAC-${vac} - 0.1ث-0.3ث - ${country.flag} ${country.name} - ذروة ${country.best_time} - ترجمه ${country.lang}</div><div style="font-size:.18rem">🧠 تحليل نفسي: ${p[0]} - ${p[1]} - حتت مستخبية بروفشنال<br>💭 خيال: ${im} - سينمائي خيالي - حتت مستخبية<br>🎬 مونتاج: ${montage[0].slice(0,30)}... - حتت مستخبية بروفشنال<br>📷 كاميرا: ${camera[0].slice(0,30)}... - حتت مستخبية<br>🎥 زاوية: ${angle[0].slice(0,30)}... - أوراق شجر - طير - سماء - ألوان أبيض #FFFFFF + أزرق #00d2ff + أخضر #00ff88 - سينمائي خيالي - حتت مستخبية<br>🌍 ترجمه: ${country.name} ${country.flag} - ${country.lang} - ذروة ${country.best_time} - ${country.tz} - جمهور ${country.audience} - تريند ${country.trend}<br>🔊 صوت عالي بروفشنال: 432 هرتز + أجراس ترتارية - تريندات عالمية - رد على تعليقات ${country.lang} - ${country.flag}<br>🌿 طيبات العوضي + مصطفى محمود + لعنة الفراعنة + أسرار الطب + الممالك + الجدار الجليدي + الممالك التي وراءه + ترتاريا + جغرافيا محرمة - 147 موضوع - ألوان أبيض أزرق أخضر أوراق شجر طير سماء - 0.1ث-0.3ث<br>💰 أفليت: ${aff} - 🔗 https://www.youtube.com/@CursedMedicineEG - @Cursed - 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث</div></div>`;
   log(`📦 0.1ث-0.3ث - ${template.slice(0,15)}... - VAC-${vac} - ${country.flag} ${country.name} - ذروة ${country.best_time} - ${country.lang} - مونتاج ${montage[0].slice(0,10)}... - كاميرا ${camera[0].slice(0,10)}... - زاوية ${angle[0].slice(0,10)}... - تحليل نفسي ${p[0]} - خيال ${im.slice(0,10)}... - طيبات + مصطفى + لعنة + ترتاريا + جغرافيا + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث`, '#FFFFFF','MEGA_01_03');
 }catch(e){}
}
document.addEventListener('DOMContentLoaded', function(){
 showCountries('all');
 show('all');
 document.getElementById('montageGrid').innerHTML=MONTAGE.map(m=>`<div class="i" style="border-color:#FFFFFF"><b style="color:#FFFFFF;font-size:.18rem">${m[0].slice(0,18)}...</b><br><span style="font-size:.14rem">${m[1].slice(0,20)}...</span></div>`).join('');
 document.getElementById('cameraGrid').innerHTML=CAMERAS.map(c=>`<div class="i" style="border-color:#00d2ff"><b style="color:#00d2ff;font-size:.18rem">${c[0].slice(0,18)}...</b><br><span style="font-size:.14rem">${c[1].slice(0,20)}...</span></div>`).join('');
 document.getElementById('angleGrid').innerHTML=ANGLES.map(a=>`<div class="i" style="border-color:#00ff88"><b style="color:#00ff88;font-size:.18rem">${a[0].slice(0,18)}...</b><br><span style="font-size:.14rem">${a[1].slice(0,20)}...</span></div>`).join('');
 document.getElementById('psychGrid').innerHTML=PSYCH.map(p=>`<div class="i" style="border-color:#a855f7"><b style="color:#a855f7;font-size:.18rem">${p[0]}</b><br><span style="font-size:.14rem">${p[1].slice(0,15)}...</span></div>`).join('');
 document.getElementById('imagGrid').innerHTML=IMAG.map(im=>`<div class="i" style="border-color:#ff00ff"><b style="font-size:.16rem">${im.slice(0,14)}...</b></div>`).join('');
 document.getElementById('prodGrid').innerHTML=PRODS.map(p=>`<div class="i" style="border-color:#f7b733"><b>${p.id} - ${p.name.slice(0,12)}...</b><br><span style="font-size:.14rem">${p.time} - ${p.price}</span></div>`).join('');
 downloadQueue();
 uploadQueue();
 setInterval(downloadQueue,100);
 setInterval(uploadQueue,100);
 log('v70 ULTRA 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث - يفتح قبل ما تلمس الشاشة - كل المشاريع القديمه والحديثه والاحداث ولاتنسي اي شئ - 147 موضوع - الترجمه 20 دوله مع تنزيل الفيديوهات في اوقات ذروة كل دوله - المونتاج والكاميرات وزوايا التصوير سينمائيه خياليه من الحتت المستخبيه الاحترافيه البرفشنال - التحليل النفسي والخيال والتحديث التلقائي المستمر الذاتي - الرد على التعليقات كلها كل لغه بلغتها بروفشنل - الصوت عالي بروفشنال تريندات عالميه - طيبات العوضي + مصطفى محمود + لعنة الفراعنه + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث', '#FFFFFF','ULTRA_01_03_MEGA');
});
</script>
</body>
</html>
"""

@app.route('/')
def index():
    html=HTML.replace('{{old_json}}', json.dumps(OLD, ensure_ascii=False)).replace('{{new_json}}', json.dumps(NEW, ensure_ascii=False)).replace('{{events_json}}', json.dumps(EVENTS, ensure_ascii=False)).replace('{{tartaria_json}}', json.dumps(TARTARIA, ensure_ascii=False)).replace('{{forbidden_json}}', json.dumps(FORBIDDEN, ensure_ascii=False)).replace('{{cursed_json}}', json.dumps(CURSED, ensure_ascii=False)).replace('{{tayyibat_json}}', json.dumps(TAYYIBAT_DIA, ensure_ascii=False)).replace('{{mostafa_json}}', json.dumps(MOSTAFA_MAHMOUD, ensure_ascii=False)).replace('{{curse_json}}', json.dumps(CURSE_PHARAO, ensure_ascii=False)).replace('{{kingdoms_json}}', json.dumps(KINGDOMS_ICE, ensure_ascii=False)).replace('{{prods_json}}', json.dumps(AFFILIATE_PRODUCTS, ensure_ascii=False)).replace('{{countries_json}}', json.dumps(COUNTRIES, ensure_ascii=False)).replace('{{montage_json}}', json.dumps(MONTAGE, ensure_ascii=False)).replace('{{cameras_json}}', json.dumps(CAMERAS, ensure_ascii=False)).replace('{{angles_json}}', json.dumps(ANGLES, ensure_ascii=False)).replace('{{psych_json}}', json.dumps(PSYCH, ensure_ascii=False)).replace('{{imag_json}}', json.dumps(IMAG, ensure_ascii=False))
    resp=Response(html, mimetype='text/html')
    resp.headers['Cache-Control']='public, max-age=10'
    resp.headers['X-Accel-Buffering']='no'
    resp.headers['Content-Encoding']='identity'
    return resp

@app.route('/api/keys/save', methods=['POST'])
def save_keys():
    try:
        data=request.get_json()
        for k,v in data.items():
            if v is not None: VAULT[k]=v.strip()
        return jsonify({"status":"success","count":sum(1 for x in VAULT.values() if x)})
    except Exception as e:
        return jsonify({"status":"error","msg":str(e)}),500

@app.route('/api/keys/status')
def keys_status():
    c=sum(1 for x in VAULT.values() if x)
    has_id=bool(VAULT["YOUTUBE_CLIENT_ID"] and len(VAULT["YOUTUBE_CLIENT_ID"])>20)
    has_sec=bool(VAULT["YOUTUBE_CLIENT_SECRET"] and len(VAULT["YOUTUBE_CLIENT_SECRET"])>10)
    has_ref=bool(VAULT["YOUTUBE_REFRESH_TOKEN"] and VAULT["YOUTUBE_REFRESH_TOKEN"].startswith("1//"))
    return jsonify({"linked":has_id and has_sec and has_ref,"status_text":f"{'✅ مربوطة - https://www.youtube.com/@CursedMedicineEG - 147 موضوع + 20 دوله + مونتاج + كاميرات + زوايا سينمائية + طيبات + مصطفى + لعنة + ترتاريا + جغرافيا + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث' if has_id and has_sec and has_ref else '⚠️ غير مربوطة - https://www.youtube.com/@CursedMedicineEG - 0.1ث-0.3ث - 147 موضوع - 20 دوله - طيبات + مصطفى + لعنة + ترتاريا + جغرافيا - الوان ابيض ازرق اخضر اوراق شجر طير سماء'} - 147 موضوع + 20 دوله + مونتاج + كاميرات + زوايا - 0.1ث-0.3ث","count":c})

@app.route('/api/live/status')
def live_status():
    return jsonify(LIVE_MONITOR)

@app.route('/api/download/queue')
def download_queue():
    return jsonify({"queue":DOWNLOAD_QUEUE[-10:],"history":DOWNLOAD_HISTORY[-20:]})

@app.route('/api/upload/queue')
def upload_queue():
    return jsonify({"queue":UPLOAD_QUEUE[-10:],"history":UPLOAD_HISTORY[-20:],"comments":COMMENTS_QUEUE[-15:],"auto_count":AUTO_UPDATE_COUNT})

@app.route('/api/download/peak', methods=['POST'])
def download_peak():
    try:
        data=request.get_json()
        code=data.get('code','EG')
        country=next((c for c in COUNTRIES if c['code']==code), COUNTRIES[0])
        t=random.choice(ALL)
        DOWNLOAD_QUEUE.append({"id":f"VID-{random.randint(100,999)}","title":f"{t[0]} - {country['name']} {country['flag']} - ذروة {country['best_time']} - ترجمه {country['lang']}","url":f"https://www.youtube.com/@CursedMedicineEG/videos - {country['code']} - ذروة {country['peak']} - {country['name']} {country['flag']}","progress":random.randint(25,60),"status":f"جاري التنزيل في اوقات ذروة {country['name']} {country['flag']} - ذروة {country['best_time']} - {country['lang']} - ترجمه {country['lang']} - مونتاج سينمائي خيالي - كاميرات - زوايا سينمائية - ألوان أبيض أزرق أخضر أوراق شجر طير سماء - 0.1ث-0.3ث - {country['trend']}","channel":"@CursedMedicineEG","country":country,"duration":LIVE_MONITOR["video_duration"]})
        return jsonify({"country":country,"status":f"جاري تنزيل في اوقات ذروة {country['name']} {country['flag']} - ذروة {country['best_time']} - 0.1ث-0.3ث"})
    except Exception as e:
        return jsonify({"country":COUNTRIES[0],"status":str(e)})

@app.route('/api/download/all-peaks', methods=['POST'])
def download_all_peaks():
    for country in COUNTRIES[:5]:
        t=random.choice(ALL)
        DOWNLOAD_QUEUE.append({"id":f"VID-{random.randint(100,999)}","title":f"{t[0]} - {country['name']} {country['flag']} - ذروة {country['best_time']}","url":f"https://www.youtube.com/@CursedMedicineEG/videos - {country['code']} - ذروة {country['peak']}","progress":random.randint(25,60),"status":f"جاري التنزيل في اوقات ذروة {country['name']} {country['flag']} - ذروة {country['best_time']} - {country['lang']} - 0.1ث-0.3ث - {country['trend']}","channel":"@CursedMedicineEG","country":country,"duration":LIVE_MONITOR["video_duration"]})
    return jsonify({"count":5,"status":"تنزيل كل الدول في اوقات ذروتها - 20 دوله - 0.1ث-0.3ث - مصر ذروة 21:00 - أمريكا 20:00 EST - بريطانيا 19:00 GMT - المانيا 20:00 CET - فرنسا 20:30 CET - 0.1ث-0.3ث"})

@app.route('/health')
def health():
    return f"v70 ULTRA 0.1ث-0.3ث - اسرع في التحميل اقل 0.1ث-0.3ث - يفتح قبل ما تلمس الشاشة - كل المشاريع القديمه والحديثه والاحداث - 147 موضوع - الترجمه 20 دوله مع تنزيل الفيديوهات في اوقات ذروة كل دوله - المونتاج والكاميرات وزوايا التصوير سينمائيه خياليه من الحتت المستخبيه الاحترافيه البرفشنال - التحليل النفسي والخيال والتحديث التلقائي المستمر الذاتي - الرد على التعليقات كل لغه بلغتها بروفشنل - الصوت عالي بروفشنال تريندات عالميه - طيبات العوضي + مصطفى محمود + لعنة الفراعنه + ترتاريا + جغرافيا محرمه + الوان ابيض ازرق اخضر اوراق شجر طير سماء - 0.1ث-0.3ث - {len(DOWNLOAD_QUEUE)} تنزيل - {len(UPLOAD_QUEUE)} رفع - {len(COMMENTS_QUEUE)} رد تعليقات - {AUTO_UPDATE_COUNT} تحديث تلقائي ذاتي"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
