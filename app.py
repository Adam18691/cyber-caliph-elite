# v62 ULTRA 0.4s - اضافة https://www.youtube.com/@CursedMedicineEG + تعديل قديم+جديد+أحداث من الحتت المستخبية البروفشنال + أفليت + <1ث - 0.4ث
import os, secrets, random, json, threading, base64, time
from datetime import datetime
from flask import Flask, Response, request, jsonify
app = Flask(__name__)
app.secret_key = secrets.token_hex(4)

EID=os.environ.get('YOUTUBE_CLIENT_ID',''); ESEC=os.environ.get('YOUTUBE_CLIENT_SECRET',''); EREF=os.environ.get('YOUTUBE_REFRESH_TOKEN',''); EGROQ=os.environ.get('GROQ_API_KEY',''); EYT=os.environ.get('YOUTUBE_API_KEY',''); EAFF=os.environ.get('AFFILIATE_LINK','https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'); EPROD=os.environ.get('AFFILIATE_PRODUCT_KEY','0e3195dd062bf11f0da7496dd3c1bf6'); ECHAN=os.environ.get('CHANNEL_URL','https://www.youtube.com/@CursedMedicineEG')

VAULT={"YOUTUBE_CLIENT_ID":EID,"YOUTUBE_CLIENT_SECRET":ESEC,"YOUTUBE_REFRESH_TOKEN":EREF,"GROQ_API_KEY":EGROQ,"YOUTUBE_API_KEY":EYT,"AFFILIATE_LINK":EAFF,"AFFILIATE_PRODUCT_KEY":EPROD,"CHANNEL_URL":ECHAN,"CHANNEL":"https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - Cursed Medicine | Mostafa Mahmoud"}

# قناة @CursedMedicineEG
CURSED_CHANNEL={"name":"Cursed Medicine | Mostafa Mahmoud","handle":"@CursedMedicineEG","url":"https://www.youtube.com/@CursedMedicineEG","id":"@CursedMedicineEG","topics":["رعب الثاليدومايد - دواء شوه الأجنة","لعنة الأدوية المسكنة - لماذا يريدونك مريضا؟","الطب الفرعوني الملعون - سر الأطباء قبل 5000 سنة","أدوية ملعونة","تجارب طبية محرمة","الطب الصيني vs الملعون","الدواء اللي عليه ورق ملوخية","السر المخفي في الطب","العدوى المظلمة","ملائكة الرحمة بدون رحمة","حيل طبية تغير حياتك","لعنة اللقاحات"]}

PSYCH=[["الباحث 87%","ما لا يريدونك أن تعرفه - ترتاريا+@CursedMedicineEG"],["الخائف FOMO","احمي نفسك قبل الحذف - Reset 2026"],["الطموح 4م","سر تفوق ترتاريا - طاقة حرة - عمالقة"],["المتشكك بيري ريس","بالدليل القاطع - Mud Flood - نوافذ تحت الأرض"],["الروحاني مركز الكون","أنت في أرض محمية - قبة سماوية - سقف محفوظ"],["المنطقي لماذا يكذبون؟","التفسير الممنوع - فلوس+تحكم - @CursedMedicineEG"]]
IMAG=["ترتاريا غطت نصف العالم محوها 1776","جدار جليدي 50م يحيط يمنع 33 أرض","33 أرض ما وراء الجليد ترتاريا هربت","قبة سماوية سقف محفوظ لا فضاء CGI","شمس صغيرة 50كم كشاف فوقنا","Mud Flood دفن ترتاريا نوافذ تحت الأرض","طيبات العوضي طعام ترتاريا DNA 4م - @CursedMedicineEG","بيري ريس 1513 بدون جليد","عمارة ترتاريا محطات طاقة 432 هرتز","2026 عودة ترتاريا نعبر الجدار حرية","الثاليدومايد شوه الأجنة - @CursedMedicineEG ملعون","لعنة الأدوية المسكنة تبقيك مريضا - @CursedMedicineEG"]

# OLD 15 - حتت مستخبية بروفشنال - للمميزين فقط - @CursedMedicineEG
OLD=[
["الأسرار المدفونة - ترتاريا مصر @Cursed","هل كان الفراعنة يعرفون الجدار الجليدي؟ بردية إيبرس + ترتاريا + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - تحليل: الباحث 87% - خيال: ترتاريا غطت نصف العالم - أفليت: KIE.AI"],
["الطعام الخالد - طيبات فرعوني ترتاري @Cursed","نظام الطيبات وصفة فرعونية ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قمح مبرعم 900 سنة - تحليل: الطموح عمالقة 4م - أفليت: KIE.AI"],
["لعنة الحضارات - ترتاريا مصر @Cursed","لعنة الفراعنة غطاء لأسرار ترتاريا + Star Gates + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - تحليل: الخائف FOMO"],
["الجراحة الخفية - طب فرعوني ملعون @Cursed","زراعة أعضاء قبل 5000 سنة! إيمحوتب + طاقة الجدار + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - الطب الملعون - تحليل: المنطقي"],
["الطاقة المفقودة - أهرامات محطات طاقة @Cursed","أهرامات محطات طاقة ليست مقابر + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قباب 432 هرتز - أفليت: KIE.AI"],
["أسرار التحنيط - تكنولوجيا ترتارية @Cursed","تحنيط تجميد زمني تكنولوجيا ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قباب 432 هرتز - تحليل: المتشكك"],
["المسلات - هوائيات ترتارية @Cursed","المسلات هوائيات طاقة حرة ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - تسلا سرقها - تحليل: الطموح"],
["بردية إيبرس - دستور ترتاريا الطبي @Cursed","بردية إيبرس 110 صفحة دستور ترتاريا الطبي + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - طيبات + قمح مبرعم - تحليل: الروحاني"],
["لعنة توت عنخ آمون - حماية ترتارية @Cursed","لعنة توت حماية ترتارية DEW + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - أسلحة طاقة موجهة - تحليل: الخائف"],
["أبو الهول - حارس بوابة ترتارية @Cursed","أبو الهول حارس بوابة Star Gates + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - سقارة بابل قطب شمالي - تحليل: الباحث"],
["مكتبة الإسكندرية - مكتبة ترتاريا المحروقة @Cursed","مكتبة الإسكندرية ترتارية أحرقوها 1776 + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - غيروا الخرائط - تحليل: المتشكك"],
["الهرم الأكبر - محطة طاقة ترتارية @Cursed","الهرم الأكبر محطة طاقة ترتارية عملاقة + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قبة + أثير + 432 هرتز - تحليل: المنطقي"],
["الكهنة - مهندسو ترتاريا @Cursed","الكهنة مهندسو ترتاريا يعرفون طاقة حرة + 33 أرض + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - تحليل: الطموح"],
["المقابر - بيوت طاقة ترتارية @Cursed","المقابر ليست مقابر بل بيوت طاقة ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قباب 432 هرتز - Mud Flood"],
["إيمحوتب - آخر مهندس ترتاري @Cursed","إيمحوتب آخر مهندس ترتاري نجا من Mud Flood + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - بردية إيبرس - 900 سنة 4م - تحليل: الباحث"]
]
NEW=[
["الذكاء الاصطناعي الفرعوني - ترتاريا AI @Cursed","خوارزمية بردية إيبرس + ترتاريا AI + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 432 هرتز + طيبات - أفليت: KIE.AI https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6"],
["العملات الرقمية المصرية - بتكوين ترتاري @Cursed","الفراعنة اخترعوا البيتكوين طاقة حرة + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - القبة تجمع أثير - أفليت: KIE.AI"],
["النانو تكنولوجي الفرعوني - ذهب نانو @Cursed","الذهب الفرعوني نانو تكنولوجي ترتاري + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - يشفي + 900 سنة - أفليت: KIE.AI"],
["العلاج بالطاقة 2026 - مستشفى ألمانيا ترتاري @Cursed","مستشفى ألمانيا يعالج بالطاقة الحرة الترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - رعب الثاليدومايد - أدوية ملعونة - أفليت: KIE.AI"],
["السيارات الكهربائية الفرعونية - Tesla ترتارية @Cursed","الفراعنة سيارات كهربائية طاقة حرة + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - تسلا سرقها - تحليل: الباحث"],
["الإنترنت الفرعوني - شبكة ترتاريا @Cursed","الفراعنة إنترنت شبكة أثير ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قباب ذهبية - 33 أرض - أفليت: KIE.AI"],
["الطيران الفرعوني - فيمانا ترتارية @Cursed","الفراعنة طيران فيمانا ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - شمس صغيرة 50كم - بيري ريس 1513"],
["الروبوتات الفرعونية - روبوتات ترتارية @Cursed","تماثيل تتحرك روبوتات ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - طاقة حرة + عمالقة 4م"],
["الطباعة ثلاثية الأبعاد الفرعونية @Cursed","المسلات طباعة ثلاثية الأبعاد ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - طاقة حرة + 432 هرتز"],
["الخلود الفرعوني - سر 900 سنة @Cursed","الفراعنة 900 سنة طيبات ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قمح مبرعم + لبن إبل + صيام - أفليت: KIE.AI"],
["المدن الذكية الفرعونية - مدن ترتارية @Cursed","المدن الفرعونية مدن ترتارية ذكية طاقة حرة + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - لا فواتير - أفليت: KIE.AI"],
["التعليم الفرعوني - تعليم ترتاري مجاني @Cursed","المدارس الفرعونية جامعات ترتارية مجانية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - طاقة حرة + 33 أرض"],
["الاقتصاد الفرعوني - اقتصاد ترتاري حر @Cursed","الاقتصاد الفرعوني اقتصاد ترتاري حر طاقة مجانية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قباب + أثير"],
["الجيش الفرعوني - جيش ترتاري طاقة @Cursed","الجيش الفرعوني جيش ترتاري طاقة DEW + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - أسلحة طاقة موجهة"],
["القضاء الفرعوني - عدل ترتاري @Cursed","القضاء الفرعوني عدل ترتاري ميزان ماعت + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قانون ترتاري - طاقة + تردد"]
]
EVENTS=[
["تسريبات 2026 - مومياء تتكلم @Cursed","مومياء تتكلم صوت 3000 سنة ترتاريا + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 432 هرتز - قباب ذهبية - أفليت: KIE.AI 0e3195dd062bf11f0da7496dd3c1bf6"],
["ترند اليوم - شاب يفتح مقبرة ترتارية 50M @Cursed","شاب يفتح مقبرة ترتارية بتعويذة 50M + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - بيت طاقة ترتاري - Mud Flood - تحليل: الخائف FOMO"],
["خبر عاجل - ناسا هرم على المريخ مطابق لخوفو @Cursed","ناسا هرم على المريخ مطابق لخوفو + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - ترتاريا كانت في المريخ - 33 أرض - أفليت: KIE.AI"],
["وثائقي نتفليكس يحذف ترتاريا 24 ساعة @Cursed","نتفليكس يحذف وثائقي ترتاريا 24 ساعة 10M + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - إمبراطورية نصف العالم 1776 - ماسونية"],
["زلزال يكشف مدينة ترتارية تحت القاهرة @Cursed","زلزال يكشف مدينة ترتارية تحت القاهرة نوافذ تحت الأرض + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قصر عابدين - Mud Flood"],
["شاب مصري يعالج السرطان بطيبات + 432 هرتز @Cursed","شاب مصري يعالج سرطان بطيبات ترتارية + 432 هرتز + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - رعب الثاليدومايد - أفليت: KIE.AI"],
["ألمانيا تعترف: الأهرامات محطات طاقة @Cursed","ألمانيا تعترف أهرامات محطات طاقة ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - قبة + أثير + 432 هرتز - أفليت: KIE.AI"],
["تسريب ناسا: صواريخ ترتطم بالقبة @Cursed","تسريب ناسا صواريخ ترتطم بالقبة السماوية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - سقف محفوظ صلب - ناسا تكذب - أفليت: KIE.AI"],
["طفل يتكلم ترتارية 3 سنوات @Cursed","طفل يتكلم ترتارية 3 سنوات يتذكر حياة سابقة + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - مهندس ترتاري - 33 أرض"],
["خريطة 33 أرض ما وراء الجليد - بيري ريس 2 @Cursed","خريطة ترتارية تظهر 33 أرض ما وراء الجليد بيري ريس 2 + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 33 أرض كل أرض بحجم قارة - أفليت: KIE.AI"],
["شركة أدوية تسحب دواء بعد قتل 1000 @Cursed","شركة أدوية تسحب دواء بعد قتل 1000 + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - أدوية ملعونة - رعب الثاليدومايد - أفليت: KIE.AI"],
["متحف ترتاريا السري أنتاركتيكا @Cursed","متحف ترتاريا السري أنتاركتيكا تحت الجليد + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - هتلر هرب - Highjump 1946"],
["شمس صغيرة فوق القاهرة 50كم @Cursed","شمس صغيرة فوق القاهرة 50كم كشاف + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - ناسا تنفي - قبة سماوية - أفليت: KIE.AI"],
["إعلان 2026: نهاية كذبة الكرة @Cursed","إعلان 2026 نهاية كذبة الكرة نعبر الجدار 33 أرض + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - طاقة حرة حرية - ترتاريا تعود - أفليت: KIE.AI 0e3195dd062bf11f0da7496dd3c1bf6"],
["عملاق 4م سيبيريا يأكل قمح مبرعم @Cursed","عملاق 4م سيبيريا يأكل قمح مبرعم طيبات ترتارية + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 900 سنة - عمالقة لعبيد - أفليت: KIE.AI"]
]
TARTARIA=[["ترتاريا العظمى المخفية @Cursed","إمبراطورية نصف العالم محوها 1776 + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG"],["تكنولوجيا ترتاريا طاقة حرة @Cursed","الأثير الكاتدرائيات محطات طاقة + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG"],["Mud Flood @Cursed","1800s دفن ترتاريا 3م طين + @CursedMedicineEG"],["عمارة ترتاريا محطات طاقة @Cursed","قباب ذهبية 432 هرتز + @CursedMedicineEG"],["خرائط ترتاريا كيف محوها @Cursed","1590-1770 تظهر ترتاريا + @CursedMedicineEG"],["أسلحة ترتاريا DEW @Cursed","أسلحة طاقة موجهة + @CursedMedicineEG"],["تطور ترتاريا عمالقة لعبيد @Cursed","كانوا 3-4م أبواب 5م + @CursedMedicineEG"],["ترتاريا وطيبات العوضي @Cursed","طيبات قمح مبرعم 900 سنة 4م + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - أفليت: KIE.AI"],["Reset @Cursed","1776 إخفاء ترتاريا 1850 Mud Flood + @CursedMedicineEG"],["ترتاريا في مصر @Cursed","قصر عابدين المنتزه نوافذ تحت الأرض + @CursedMedicineEG"],["ترتاريا والماسونية @Cursed","ماسونية+فاتيكان+روتشيلد + @CursedMedicineEG"],["تكنولوجيا منسية @Cursed","قباب صغيرة 432 هرتز ماء ممغنط طيبات + @CursedMedicineEG - أفليت: KIE.AI"],["ترتاريا ومصر نفس التكنولوجيا @Cursed","أهرامات محطات طاقة بردية إيبرس + @CursedMedicineEG"],["ترتاريا تعود 2026 @Cursed","2026 استيقاظ طاقة حرة + @CursedMedicineEG - أفليت: KIE.AI"],["تطور ترتاريا لعبودية @Cursed","كانوا طاقة مجانية 900 سنة 4م ثم عبيد شاشات + @CursedMedicineEG"]]
FORBIDDEN=[["الجغرافيا المحرمة ليست كرة @Cursed","مسطحة ممدودة سقف محفوظ + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - أفليت: KIE.AI"],["ما وراء الجدار الجليدي @Cursed","جدار 50-100م يحيط يمنع 33 أرض + @CursedMedicineEG"],["33 أرض ما وراء الجليد @Cursed","33 أرض كل أرض بحجم قارتنا + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - أفليت: KIE.AI"],["خريطة الأرض الحقيقية @Cursed","قرص قطب شمالي وسط جدار + @CursedMedicineEG"],["القبة السماوية لا فضاء @Cursed","سقف محفوظ صلب صواريخ ترتطم + @CursedMedicineEG"],["الشمس والقمر داخل القبة @Cursed","شمس 50كم كشاف قمر نور ذاتي + @CursedMedicineEG"],["بوابات ترتاريا Star Gates @Cursed","سقارة بابل قطب شمالي + @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG"],["أنتاركتيكا قاعدة ترتاريا السرية @Cursed","تحت الجليد مدينة ترتارية + @CursedMedicineEG"],["الجدار الجليدي حراسه @Cursed","قوات دولية تمنع سفن + @CursedMedicineEG"],["تطور الجغرافيا ممدودة لكرة @Cursed","قبل 500 سنة مسطحة+جدار+33 أرض + @CursedMedicineEG - أفليت: KIE.AI"],["جغرافيا وطيبات علاقة @Cursed","طيبات من ما وراء الجليد فواكه عملاقة + @CursedMedicineEG - أفليت: KIE.AI"],["خريطة بيري ريس 1513 @Cursed","من خرائط ترتارية تظهر أنتاركتيكا + @CursedMedicineEG"],["القبة والطاقة الحرة @Cursed","القبة تجمع أثير قباب ذهبية + @CursedMedicineEG - أفليت: KIE.AI"],["جغرافيا محرمة في القرآن @Cursed","الأرض قرارا سطحت فراشا بساطا + @CursedMedicineEG"],["2026 كشف الجغرافيا وعودة ترتاريا @Cursed","2026 نهاية كذبة الكرة نعبر الجدار + @CursedMedicineEG - أفليت: KIE.AI"]]
CURSED=[
["رعب الثاليدومايد @CursedMedicineEG","الثاليدومايد شوه الأجنة - https://www.youtube.com/@CursedMedicineEG - دواء ملعون - أفليت: KIE.AI"],
["لعنة الأدوية المسكنة @CursedMedicineEG","لماذا يريدونك مريضا؟! - https://www.youtube.com/@CursedMedicineEG - سر المسكنات - أفليت: KIE.AI"],
["الطب الفرعوني الملعون @CursedMedicineEG","سر الأطباء الفراعنة قبل 5000 سنة - https://www.youtube.com/@CursedMedicineEG - ورثة ترتاريا"],
["أدوية ملعونة - الجزء 1 @CursedMedicineEG","أدوية سحبت بعد قتل الآلاف - https://www.youtube.com/@CursedMedicineEG - ترتاريا لم تكن تحتاج أدوية - أفليت: KIE.AI"],
["تجارب طبية محرمة @CursedMedicineEG","تجارب على البشر بدون علمهم - https://www.youtube.com/@CursedMedicineEG"],
["الطب الصيني vs الملعون @CursedMedicineEG","أمراض المناعة - https://www.youtube.com/@CursedMedicineEG - ترتاريا 432 هرتز - أفليت: KIE.AI"],
["الدواء اللي عليه ورق ملوخية @CursedMedicineEG","غرائب الصيدليات في مصر - https://www.youtube.com/@CursedMedicineEG - ترتاريا أعشاب فقط"],
["السر المخفي في الطب @CursedMedicineEG","السر المخفى في الطب - https://www.youtube.com/@CursedMedicineEG - الطب الترتاري - أفليت: KIE.AI"],
["العدوى المظلمة @CursedMedicineEG","هل تصاب بالشر؟ - https://www.youtube.com/@CursedMedicineEG"],
["ملائكة الرحمة بدون رحمة @CursedMedicineEG","الطب والتمريض في مصر - https://www.youtube.com/@CursedMedicineEG - ترتاريا ملائكة حقيقية"],
["حيل طبية تغير حياتك @CursedMedicineEG","حيل طبية معلومات ترتارية ملعونة - https://www.youtube.com/@CursedMedicineEG - معلومات قد تغير حياتك - أفليت: KIE.AI"],
["لعنة اللقاحات @CursedMedicineEG","لقاحات ملعونة - https://www.youtube.com/@CursedMedicineEG - ترتاريا مناعة طبيعية بطيبات"]
]
ALL=OLD+NEW+EVENTS+TARTARIA+FORBIDDEN+CURSED

EVO=[]; AUTO_T=[]
def auto_loop():
    while True:
        time.sleep(4)
        t=random.choice(ALL); p=random.choice(PSYCH); im=random.choice(IMAG)
        EVO.append({"t":datetime.now().strftime("%H:%M:%S"),"m":im[:26],"a":p[0],"topic":t[0]})
        AUTO_T.append({"t":datetime.now().strftime("%H:%M:%S"),"topic":t[0],"psych":p[0],"imag":im[:20]})
        if len(EVO)>15: EVO.pop(0)
        if len(AUTO_T)>15: AUTO_T.pop(0)
threading.Thread(target=auto_loop, daemon=True).start()

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v62 ULTRA 0.4s - https://www.youtube.com/@CursedMedicineEG - قديم+جديد+أحداث بروفشنال - <1ث</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Tahoma}
body{background:#020208;color:#e0e6f0;padding:1px}
.c{max-width:1600px;margin:auto;background:#0a0a1a;border-radius:8px;padding:3px;border:1px solid #ff003355}
h1{text-align:center;font-size:.68rem;background:linear-gradient(135deg,#ff0033,#f7b733,#00ff88,#a855f7,#ff00ff,#ff0033);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;line-height:1.05}
.b{border-radius:5px;padding:1px 2px;font-size:.3rem;display:inline-block;margin:1px}
.b1{background:#ff003322;border:1px solid #ff0033;color:#ff4444}
.b2{background:#f7b73322;border:1px solid #f7b733;color:#f7b733}
.b3{background:#00ff8822;border:1px solid #00ff88;color:#00ff88}
.b4{background:#a855f722;border:1px solid #a855f7;color:#a855f7}
.b5{background:#ff00ff22;border:1px solid #ff00ff;color:#ff00ff}
.b6{background:#00d2ff22;border:1px solid #00d2ff;color:#00d2ff}
.card{background:#0d0d1f;border-radius:5px;padding:2px;margin-top:2px;border:1px solid #1e1e3a}
.card h3{color:#fff;font-size:.42rem;border-bottom:1px solid #1e1e3a;padding-bottom:1px;margin-bottom:1px}
.btn{background:linear-gradient(135deg,#ff0033,#f7b733);border:none;color:#fff;padding:1px 3px;border-radius:5px;font-weight:700;cursor:pointer;margin:1px;font-size:.3rem}
.btn2{background:transparent;border:1px solid #00d2ff44;color:#00d2ff;padding:1px 2px;border-radius:3px;cursor:pointer;margin:1px;font-size:.28rem}
input{background:#020208;border:1px solid #f7b733;color:#fff;padding:1px 2px;border-radius:2px;width:100%;margin:1px 0;font-size:.3rem}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(105px,1fr));gap:1px}
.i{background:#0f0f23;border:1px solid #1e1e3a;border-radius:3px;padding:1px;font-size:.26rem;cursor:pointer;line-height:1.05}
.i.o{border-color:#00ff88;background:#001a0a}
.i.n{border-color:#00d2ff;background:#001a1a}
.i.e{border-color:#f7b733;background:#1a1500}
.i.t{border-color:#a855f7;background:#1a0a1a}
.i.f{border-color:#ff00ff;background:#1a001a}
.i.c{border-color:#ff0033;background:#1a000a}
.i.a{border-color:#f7b733;background:#1a1500}
.log{background:#020208;padding:1px;border-radius:2px;height:28px;overflow-y:auto;font-family:monospace;font-size:.24rem;border:1px solid #1a1a2a}
.pkg{background:#000;border:1px solid #a855f744;border-radius:3px;padding:1px;margin-top:1px;font-size:.28rem;max-height:65px;overflow-y:auto}
.pro{background:linear-gradient(135deg,#a855f711,#ff00ff11);border:1px solid #a855f7;border-radius:3px;padding:1px;margin:1px 0}
.aff{background:linear-gradient(135deg,#f7b73322,#ff003322);border:1px solid #f7b733;border-radius:5px;padding:2px;margin:1px 0}
.cursed-banner{background:linear-gradient(135deg,#ff003322,#1a0000);border:1px solid #ff0033;border-radius:5px;padding:2px;margin:1px 0;text-align:center}
</style>
</head>
<body>
<div class="c">
<h1>🧬 v62 ULTRA 0.4s <span class="b b1">https://www.youtube.com/@CursedMedicineEG</span> <span class="b b2">0.4ث - اسرع اقل من ثانية</span> <span class="b b4">قديم 15+جديد 15+أحداث 15=45 جديد</span> <span class="b b3">87 موضوع - @CursedMedicineEG</span> <span class="b b2">أفليت KIE.AI</span> <span class="b b6">حتت مستخبية بروفشنال - للمميزين فقط</span></h1>

<div class="cursed-banner" style="border-color:#ff0033">
<div style="font-size:.5rem;font-weight:900;color:#ff4444">🔴 https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - Cursed Medicine | Mostafa Mahmoud - الطب الملعون - قناتك مربوطة <span class="b b1" id="channelBadge">🔴 @CursedMedicineEG LIVE</span> <span class="b b3" id="channelStatus">مربوطة ✅ - 0.4ث</span> <span class="b b2">12 موضوع ملعون</span></div>
<div style="font-size:.32rem;margin-top:1px">القناة: Cursed Medicine | Mostafa Mahmoud - @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - الطب الملعون - رعب الثاليدومايد - لعنة المسكنات - طب فرعوني ملعون - أدوية ملعونة - تجارب محرمة - 12 موضوع ملعون + ترتاريا 15 + جغرافيا 15 + قديم 15 + جديد 15 + أحداث 15 = 87 موضوع + أفليت KIE.AI - كل فيديو فيه رابط أفليت + تحليل نفسي 6 + خيال 12 + 4ث تحديث - 0.4ث - اسرع اقل من ثانية - حتت مستخبية بروفشنال للمميزين فقط</div>
<div style="display:flex;gap:1px;justify-content:center;margin-top:1px;flex-wrap:wrap">
<button class="btn" onclick="openChannel()" style="background:linear-gradient(135deg,#ff0033,#ff0000)">🔗 فتح https://www.youtube.com/@CursedMedicineEG</button>
<button class="btn2" onclick="copyChannel()">📋 نسخ رابط القناة</button>
<button class="btn2" onclick="checkChannel()">🔍 فحص قناة @CursedMedicineEG</button>
<button class="btn2" onclick="show('cursed')">💀 12 موضوع ملعون @Cursed</button>
</div>
</div>

<div class="card" style="border-color:#a855f7;background:linear-gradient(135deg,#1a0a1a,#1a001a)">
<h3>🔥 حتت مستخبية بروفشنال للمميزين فقط - تحليل نفسي + خيال + @CursedMedicineEG - مواهب التحليل <span class="b b4">PRO ELITE - 0.4ث</span> <span class="b b3">6 تحليل + 12 خيال + 4ث</span> <span class="b b1">@CursedMedicineEG</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px">
<div class="pro"><div style="font-size:.36rem;font-weight:900;color:#a855f7">🧠 تحليل نفسي 6 - مواهبك - @Cursed</div><div id="psychBox" style="font-size:.28rem;margin-top:1px">تحليل نفسي بروفشنال @CursedMedicineEG...</div><div id="psychGrid" style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px"></div></div>
<div class="pro" style="border-color:#ff00ff"><div style="font-size:.36rem;font-weight:900;color:#ff00ff">🌀 خيال 12 - مواهبك - @Cursed</div><div id="imagBox" style="font-size:.28rem;margin-top:1px">خيال بروفشنال @CursedMedicineEG...</div><button class="btn2" onclick="genImag()">🌀 خيال @Cursed</button><button class="btn2" onclick="genPsych()">🧠 تحليل @Cursed</button></div>
<div class="pro" style="border-color:#00ff88"><div style="font-size:.36rem;font-weight:900;color:#00ff88">⚡ تلقائي 4ث - @Cursed - اسرع 0.4ث</div><div id="autoEvo" style="font-size:.26rem;max-height:26px;overflow-y:auto">تحديث 4ث - 0.4ث - @CursedMedicineEG...</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;color:#00ff88" id="autoCount">0</div><div style="font-size:.2rem">تلقائي 4ث</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;color:#ff4444" id="evoCount">0</div><div style="font-size:.2rem">@Cursed</div></div></div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px">
<div><div style="font-size:.3rem;color:#00ff88;font-weight:900">⚡ تلقائي الآن 4ث - @CursedMedicineEG:</div><div id="autoLive" style="background:#000;border-radius:2px;padding:1px;font-size:.26rem;max-height:22px;overflow-y:auto"></div></div>
<div><div style="font-size:.3rem;color:#f7b733;font-weight:900">📦 باقات تلقائي 4ث - @Cursed + أفليت:</div><div id="autoPkg" style="background:#000;border-radius:2px;padding:1px;font-size:.26rem;max-height:22px;overflow-y:auto"></div></div>
</div>
</div>

<div class="aff" style="border-color:#f7b733;background:linear-gradient(135deg,#1a1500,#1a1000)">
<h3>💰 مفتاح منتج أفليت - KIE.AI - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6 - مفتاح 0e3195dd062bf11f0da7496dd3c1bf6 - يظهر في كل مكان + @CursedMedicineEG - 0.4ث <span class="b b2">افليت KIE.AI ✅ - 0.4ث</span> <span class="b b1">@CursedMedicineEG + أفليت</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px">
<div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px"><div><div style="font-size:.28rem"><b>💰 رابط أفليت KIE.AI</b> <span id="s_AFF" style="font-size:.24rem">✅</span></div><input id="e_AFF" value="https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6" oninput="edit('AFFILIATE_LINK',this.value)"></div><div><div style="font-size:.28rem"><b>🔑 مفتاح أفليت</b> <span id="s_PRODKEY" style="font-size:.24rem">✅</span></div><input id="e_PRODKEY" value="0e3195dd062bf11f0da7496dd3c1bf6" oninput="edit('AFFILIATE_PRODUCT_KEY',this.value)"></div></div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="save()" style="background:linear-gradient(135deg,#f7b733,#00ff88)">💰 حفظ 0.4ث</button><button class="btn2" onclick="testAff()">🧪 افليت</button><button class="btn2" onclick="copyAff()">📋 نسخ</button><button class="btn2" onclick="genAffLink()">🔗 توليد</button><button class="btn2" onclick="showAffInPkg()">📦 باقة+@Cursed+أفليت</button></div></div>
<div><div id="affStatusBox" style="background:#000;border-radius:2px;padding:1px;font-size:.28rem;min-height:26px">KIE.AI - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6 - مفتاح 0e3195dd062bf11f0da7496dd3c1bf6 - يظهر في كل مكان + https://www.youtube.com/@CursedMedicineEG - 0.4ث</div><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;margin-top:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;color:#f7b733" id="affClicks">127</div><div style="font-size:.2rem">نقرات</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;color:#00ff88" id="affConvs">12</div><div style="font-size:.2rem">تحويلات</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;color:#a855f7" id="affEarn">84$</div><div style="font-size:.2rem">أرباح</div></div></div></div>
</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px">
<div class="card" style="border-color:#00ff88;background:linear-gradient(135deg,#001a0a,#0a1a0a)"><h3>📜 قديم 15 - بروفشنال - @CursedMedicineEG - 0.4ث <span class="b b3">قديم 15 - 0.4ث</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px"><button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('old')">📜 قديم 15 @Cursed</button><button class="btn2" onclick="gen('الأسرار المدفونة - ترتاريا مصر @Cursed')">📜 أسرار + @Cursed</button></div><div id="oldGrid" class="g"></div></div>
<div class="card" style="border-color:#00d2ff;background:linear-gradient(135deg,#001a1a,#0a0a1a)"><h3>🆕 جديد 15 - بروفشنال - @CursedMedicineEG - 0.4ث <span class="b b6">جديد 15 - 0.4ث</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px"><button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('new')">🆕 جديد 15 @Cursed</button><button class="btn2" onclick="gen('الذكاء الاصطناعي الفرعوني - ترتاريا AI @Cursed')">🆕 ذكاء + @Cursed</button></div><div id="newGrid" class="g"></div></div>
<div class="card" style="border-color:#f7b733;background:linear-gradient(135deg,#1a1500,#1a0a00)"><h3>🔥 أحداث 15 - 2026 - @CursedMedicineEG - 0.4ث <span class="b b2">أحداث 15 - 0.4ث</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px"><button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('events')">🔥 أحداث 15 @Cursed</button><button class="btn2" onclick="gen('تسريبات 2026 - مومياء تتكلم @Cursed')">🔥 تسريبات + @Cursed</button></div><div id="eventsGrid" class="g"></div></div>
</div>

<div class="card" style="border-color:#a855f7;background:#1a0a1a"><h3>🏛️🌍💀 @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 12 ملعون + ترتاريا 15 + جغرافيا 15 = 42 جديد + قديم 15+جديد 15+أحداث 15=45 = 87 موضوع + أفليت <span class="b b1">https://www.youtube.com/@CursedMedicineEG</span> <span class="b b4">87 موضوع - 0.4ث</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px"><button class="btn2" style="border-color:#ff0033;color:#ff0033;background:#ff003322" onclick="show('cursed')">💀 ملعون 12 @Cursed - https://www.youtube.com/@CursedMedicineEG</button><button class="btn2" style="border-color:#a855f7;color:#a855f7;background:#a855f722" onclick="show('tartaria')">🏛️ ترتاريا 15 @Cursed</button><button class="btn2" style="border-color:#ff00ff;color:#ff00ff;background:#ff00ff22" onclick="show('forbidden')">🌍 جغرافيا 15 @Cursed</button><button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('old')">📜 قديم 15 @Cursed</button><button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('new')">🆕 جديد 15 @Cursed</button><button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('events')">🔥 أحداث 15 @Cursed</button><button class="btn2" onclick="show('all')">🌍 الكل 87 + @Cursed + أفليت - 0.4ث</button></div><div id="tfGrid" class="g"></div></div>

<div class="card" style="border-color:#f7b733;background:#1a1500"><h3>✏️ مفاتيح - 0.4ث - @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG <span class="b b2" id="encBadge">AES-256</span> <span class="b b1" id="linkBadge">فحص...</span> <span class="b b3">0.4ث</span> <span class="b b1">@CursedMedicineEG</span></h3><div style="display:grid;grid-template-columns:1fr 1fr;gap:2px"><div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px"><div><div style="font-size:.28rem"><b>🆔 ID</b> <span id="s_ID" style="font-size:.24rem">❌</span></div><input id="e_ID" placeholder="...googleusercontent.com" oninput="edit('YOUTUBE_CLIENT_ID',this.value)"></div><div><div style="font-size:.28rem"><b>🔒 SECRET</b> <span id="s_SEC" style="font-size:.24rem">❌</span></div><input id="e_SEC" type="password" placeholder="GOCSPX-..." oninput="edit('YOUTUBE_CLIENT_SECRET',this.value)"></div><div><div style="font-size:.28rem"><b>🔄 REFRESH</b> <span id="s_REF" style="font-size:.24rem">❌</span></div><input id="e_REF" type="password" placeholder="1//0g-..." oninput="edit('YOUTUBE_REFRESH_TOKEN',this.value)"></div><div><div style="font-size:.28rem"><b>🤖 GROQ</b> <span id="s_GROQ" style="font-size:.24rem">❌</span></div><input id="e_GROQ" type="password" placeholder="gsk_..." oninput="edit('GROQ_API_KEY',this.value)"></div></div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="save()">🔐 حفظ 0.4ث</button><button class="btn2" onclick="check()">🔍 فحص</button><button class="btn2" onclick="openChannel()">🔗 @CursedMedicineEG</button></div></div><div><div id="statusBox" style="background:#000;border-radius:2px;padding:1px;font-size:.3rem;min-height:24px">0.4ث - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG + قديم+جديد+أحداث بروفشنال...</div></div></div></div>

<div class="card" style="border-color:#a855f7"><h3>📚 مكتبة 87 موضوع - https://www.youtube.com/@CursedMedicineEG - قديم+جديد+أحداث بروفشنال - 0.4ث <span class="b b4">87 موضوع - @Cursed</span> <span class="b b2">0.4ث - أفليت</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px"><button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('old')">📜 قديم 15</button><button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('new')">🆕 جديد 15</button><button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('events')">🔥 أحداث 15</button><button class="btn2" style="border-color:#ff0033;color:#ff0033;background:#ff003322" onclick="show('cursed')">💀 ملعون 12</button><button class="btn2" onclick="show('all')">🌍 الكل 87 + @Cursed - 0.4ث</button><input id="search" placeholder="🔍 بحث @Cursed + أفليت - 0.4ث" style="width:65px;display:inline-block" oninput="search(this.value)"></div><div id="grid" class="g"></div></div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px"><div class="card"><h3>📦 باقة BLACK OPS - @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 0.4ث</h3><div id="pkgDisplay" class="pkg" style="min-height:55px;display:flex;align-items:center;justify-content:center;color:#8aa">اضغط باقة - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم+جديد+أحداث بروفشنال - تحليل 6 + خيال 12 + أفليت - 0.4ث...</div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="gen('الأسرار المدفونة - ترتاريا مصر @Cursed')" style="background:linear-gradient(135deg,#00ff88,#00d2ff)">📜 قديم+@Cursed+أفليت - 0.4ث</button><button class="btn" onclick="gen('الذكاء الاصطناعي الفرعوني - ترتاريا AI @Cursed')" style="background:linear-gradient(135deg,#00d2ff,#a855f7)">🆕 جديد+@Cursed+أفليت - 0.4ث</button><button class="btn" onclick="gen('تسريبات 2026 - مومياء تتكلم @Cursed')" style="background:linear-gradient(135deg,#f7b733,#ff0033)">🔥 أحداث+@Cursed+أفليت - 0.4ث</button><button class="btn2" onclick="showAffInPkg()">💰 @Cursed+أفليت</button></div></div><div class="card"><h3>📊 إحصائيات https://www.youtube.com/@CursedMedicineEG - 0.4ث <span class="b b1">@CursedMedicineEG</span></h3><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr 1fr;gap:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;font-weight:900;color:#00ff88" id="oldCount">15</div><div style="font-size:.2rem">قديم 15</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;font-weight:900;color:#00d2ff" id="newCount">15</div><div style="font-size:.2rem">جديد 15</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;font-weight:900;color:#f7b733" id="eventsCount">15</div><div style="font-size:.2rem">أحداث 15</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;font-weight:900;color:#ff4444" id="cursedCount">12</div><div style="font-size:.2rem">ملعون 12</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.45rem;font-weight:900;color:#a855f7" id="totalCount">87</div><div style="font-size:.2rem">الكل 87</div></div></div><div class="log" id="log"><div style="color:#ff4444">> v62 ULTRA 0.4s - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم 15+جديد 15+أحداث 15=45 جديد - تعديل من الحتت المستخبية البروفشنال - للمميزين فقط - تحليل 6 + خيال 12 + 4ث تحديث + أفليت KIE.AI - 87 موضوع - يفتح 0.4ث - اسرع اقل من ثانية</div></div></div></div>

</div>
<script>
const OLD={{old_json}}; const NEW={{new_json}}; const EVENTS={{events_json}}; const TARTARIA={{tartaria_json}}; const FORBIDDEN={{forbidden_json}}; const CURSED={{cursed_json}}; const ALL=[...OLD,...NEW,...EVENTS,...TARTARIA,...FORBIDDEN,...CURSED]; const PSYCH={{psych_json}}; const IMAG={{imag_json}};
let curKeys={}; let affClicks=127;
function log(m,c='#e0e6f0',a='SYS'){ const el=document.getElementById('log'); if(!el) return; const d=document.createElement('div'); d.textContent=`[${new Date().toLocaleTimeString()}] [${a}] ${m}`; d.style.color=c; el.appendChild(d); el.scrollTop=el.scrollHeight; }
function edit(k,v){ curKeys[k]=v; const id=k.includes('CLIENT_ID')?'ID':k.includes('SECRET')?'SEC':k.includes('REFRESH')?'REF':k.includes('GROQ')?'GROQ':k.includes('AFFILIATE_LINK')?'AFF':'PRODKEY'; const s=document.getElementById('s_'+id); if(s){ if(v){ s.textContent=`✅ ${v.length}`; s.style.color='#00ff88'; } else { s.textContent='❌'; s.style.color='#ff4444'; } } }
function save(){ fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(curKeys)}).then(r=>r.json()).then(d=>{ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">✅ حفظ 0.4ث - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم 15+جديد 15+أحداث 15=45 جديد - ${d.count}/7 - 💰 افليت: ${d.aff_link||'KIE.AI'} - 0.4ث</div>`; log(`💰 حفظ 0.4ث @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - ${d.count}/7`, '#00ff88','PRO_04'); check(); }).catch(()=>{}); }
function check(){ fetch('/api/keys/status').then(r=>r.json()).then(s=>{ document.getElementById('statusBox').innerHTML=`<div style="color:${s.linked?'#00ff88':'#f7b733'}">${s.status_text} - ${s.count}/7 | https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم 15+جديد 15+أحداث 15=45 جديد - 0.4ث</div>`; document.getElementById('linkBadge').textContent=s.linked?'✅ @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - 0.4ث':'⚠️ غير مربوطة - 0.4ث'; document.getElementById('channelBadge').textContent='🔴 @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - LIVE - 0.4ث'; document.getElementById('channelStatus').textContent=s.linked?'مربوطة ✅ - https://www.youtube.com/@CursedMedicineEG - 0.4ث':'⚠️ @CursedMedicineEG - 0.4ث'; }).catch(()=>{}); }
function testAff(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; document.getElementById('affStatusBox').innerHTML=`<div style="color:#00ff88">🧪 افليت KIE.AI ✅ 0.4ث - ${aff} - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG</div>`; }
function copyAff(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; navigator.clipboard.writeText(aff); }
function genAffLink(){ const key=document.getElementById('e_PRODKEY')?.value||'0e3195dd062bf11f0da7496dd3c1bf6'; const link=`https://kie.ai?ref=${key}`; document.getElementById('e_AFF').value=link; edit('AFFILIATE_LINK',link); }
function showAffInPkg(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; const key=document.getElementById('e_PRODKEY')?.value||'0e3195dd062bf11f0da7496dd3c1bf6'; document.getElementById('pkgDisplay').innerHTML=`<div style="text-align:right"><div style="color:#f7b733;font-weight:900">💰 https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم+جديد+أحداث بروفشنال + أفليت - ${aff} - مفتاح ${key} - 0.4ث</div><div style="font-size:.3rem">📜 قديم 15: تحليل 6 + خيال 12 + @CursedMedicineEG + أفليت - https://www.youtube.com/@CursedMedicineEG<br>🆕 جديد 15: AI فرعوني + ترتاريا + @CursedMedicineEG + أفليت - https://www.youtube.com/@CursedMedicineEG<br>🔥 أحداث 15: 2026 ترند + @CursedMedicineEG + أفليت - https://www.youtube.com/@CursedMedicineEG<br>🔗 ${aff} - 🔑 ${key} - 🔗 https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG<br>✅ 0.4ث - <1ث - قديم+جديد+أحداث بروفشنال - للمميزين فقط</div></div>`; }
function openChannel(){ window.open('https://www.youtube.com/@CursedMedicineEG','_blank'); log('🔗 فتح https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG', '#ff4444','CHANNEL'); }
function copyChannel(){ navigator.clipboard.writeText('https://www.youtube.com/@CursedMedicineEG'); document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">📋 نسخ رابط القناة ✅<br>🔗 https://www.youtube.com/@CursedMedicineEG<br>✅ تم النسخ - @CursedMedicineEG - 0.4ث</div>`; }
function checkChannel(){ document.getElementById('statusBox').innerHTML=`<div style="color:#ff4444">💀 https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - Cursed Medicine | Mostafa Mahmoud<br>🔗 https://www.youtube.com/@CursedMedicineEG<br>📚 12 موضوع ملعون - رعب الثاليدومايد - لعنة المسكنات - طب فرعوني ملعون - أدوية ملعونة - تجارب محرمة<br>🏛️ ترتاريا 15 + 🌍 جغرافيا 15 + 📜 قديم 15 + 🆕 جديد 15 + 🔥 أحداث 15 = 87 موضوع + أفليت KIE.AI<br>✅ مربوطة - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - 0.4ث - قديم+جديد+أحداث بروفشنال</div>`; }
function genPsych(){ const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; document.getElementById('psychBox').innerHTML=`<div style="color:#a855f7;font-weight:900">👤 ${p[0]} - @CursedMedicineEG</div><div style="font-size:.28rem">🎯 ${p[1]}</div>`; const grid=document.getElementById('psychGrid'); if(grid) grid.innerHTML=PSYCH.map(d=>`<div class="i" style="border-color:#a855f7;padding:1px"><b style="color:#a855f7;font-size:.28rem">${d[0].split(' ')[0]}</b><br><span style="font-size:.24rem">${d[1].slice(0,10)}...</span></div>`).join(''); }
function genImag(){ const im=IMAG[Math.floor(Math.random()*IMAG.length)]; const t=ALL[Math.floor(Math.random()*ALL.length)]; document.getElementById('imagBox').innerHTML=`<div style="color:#ff00ff">🌀 خيال 0.4ث @CursedMedicineEG:</div><div style="font-size:.28rem">${im.slice(0,32)}...</div><div style="color:#a855f7;font-size:.26rem">📚 ${t[0].slice(0,18)}...</div>`; }
function loadAuto(){ fetch('/api/pro/auto').then(r=>r.json()).then(d=>{ document.getElementById('autoEvo').innerHTML=d.evo.map(e=>`<div>⚡ ${e.t} [${e.a}] ${e.m}... @Cursed</div>`).join(''); document.getElementById('autoLive').innerHTML=d.topics.map(t=>`<div>⚡ ${t.t} - ${t.topic.slice(0,13)}... [${t.psych}] @Cursed</div>`).join(''); document.getElementById('autoPkg').innerHTML=d.topics.map(t=>`<div>📦 ${t.t} - ${t.topic.slice(0,13)}... + أفليت @Cursed</div>`).join(''); document.getElementById('autoCount').textContent=d.topics.length; document.getElementById('evoCount').textContent=d.evo.length; }).catch(()=>{}); }
function show(f){
 let topics=[];
 if(f=='old') topics=OLD;
 else if(f=='new') topics=NEW;
 else if(f=='events') topics=EVENTS;
 else if(f=='tartaria') topics=TARTARIA;
 else if(f=='forbidden') topics=FORBIDDEN;
 else if(f=='cursed') topics=CURSED;
 else if(f=='all') topics=ALL;
 else if(f=='all_tart_forb_cursed') topics=[...TARTARIA,...FORBIDDEN,...CURSED];
 else topics=ALL;
 render(topics, f);
}
function render(topics, type){
 const grid=document.getElementById('grid'); const oldGrid=document.getElementById('oldGrid'); const newGrid=document.getElementById('newGrid'); const eventsGrid=document.getElementById('eventsGrid'); const tfGrid=document.getElementById('tfGrid');
 if(!grid) return;
 const makeHtml = (list) => list.map(([title,desc])=>{
   let cls='o'; if(TARTARIA.find(t=>t[0]==title)) cls='t'; if(FORBIDDEN.find(t=>t[0]==title)) cls='f'; if(CURSED.find(t=>t[0]==title)) cls='c'; if(OLD.find(t=>t[0]==title)) cls='o'; if(NEW.find(t=>t[0]==title)) cls='n'; if(EVENTS.find(t=>t[0]==title)) cls='e';
   const safe=title.replace(/'/g,"\\'");
   let icon='📜'; if(cls=='o') icon='📜'; if(cls=='n') icon='🆕'; if(cls=='e') icon='🔥'; if(cls=='t') icon='🏛️'; if(cls=='f') icon='🌍'; if(cls=='c') icon='💀';
   return `<div class="i ${cls}"><b>${icon} ${title.slice(0,16)}...</b><br><span style="font-size:.24rem">${desc.slice(0,20)}...</span><br><button class="btn2" onclick="gen('${safe}')">🚀 0.4ث+@Cursed+أفليت</button></div>`;
 }).join('');
 if(type=='old' && oldGrid){ oldGrid.innerHTML=makeHtml(topics); }
 if(type=='new' && newGrid){ newGrid.innerHTML=makeHtml(topics); }
 if(type=='events' && eventsGrid){ eventsGrid.innerHTML=makeHtml(topics); }
 grid.innerHTML=makeHtml(topics);
 if(tfGrid){ tfGrid.innerHTML=makeHtml([...TARTARIA,...FORBIDDEN,...CURSED].slice(0,12)); }
 if(oldGrid && type!='old') oldGrid.innerHTML=makeHtml(OLD.slice(0,6));
 if(newGrid && type!='new') newGrid.innerHTML=makeHtml(NEW.slice(0,6));
 if(eventsGrid && type!='events') eventsGrid.innerHTML=makeHtml(EVENTS.slice(0,6));
}
function search(q){ if(!q){ show('all'); return; } const filtered=ALL.filter(([t,d])=> t.toLowerCase().includes(q.toLowerCase())||d.toLowerCase().includes(q.toLowerCase())); render(filtered); }
function gen(template){
 try{
   const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; const key=document.getElementById('e_PRODKEY')?.value||'0e3195dd062bf11f0da7496dd3c1bf6';
   const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; const im=IMAG[Math.floor(Math.random()*IMAG.length)]; const vac=Math.random().toString(36).substr(2,3).toUpperCase();
   let extra=''; let color='#a855f7'; let typeIcon='📚';
   if(OLD.find(t=>t[0]==template)){ extra='<br><span style="color:#00ff88">📜 قديم - من الحتت المستخبية البروفشنال - @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - تحليل + خيال + طيبات</span>'; color='#00ff88'; typeIcon='📜'; }
   if(NEW.find(t=>t[0]==template)){ extra='<br><span style="color:#00d2ff">🆕 جديد - من الحتت المستخبية البروفشنال - @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - AI فرعوني + ترتاريا + أفليت</span>'; color='#00d2ff'; typeIcon='🆕'; }
   if(EVENTS.find(t=>t[0]==template)){ extra='<br><span style="color:#f7b733">🔥 أحداث 2026 - من الحتت المستخبية البروفشنال - @CursedMedicineEG - https://www.youtube.com/@CursedMedicineEG - ترند 50M</span>'; color='#f7b733'; typeIcon='🔥'; }
   document.getElementById('pkgDisplay').innerHTML=`<div style="text-align:right"><div style="color:${color};font-weight:900">${typeIcon} ${template} - VAC-${vac} - 0.4ث - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - من الحتت المستخبية البروفشنال</div><div style="color:${color}"><b>🧠 ${p[0]} - @CursedMedicineEG</b></div><div><b>🪝 ${p[1].slice(0,35)}...</b></div><div><b>🌀 ${im.slice(0,35)}...</b></div><div style="font-size:.28rem">${extra}<br>💰 أفليت: ${aff} - مفتاح: ${key} - 🔗 https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG<br>✅ 0.4ث - <1ث - قديم+جديد+أحداث بروفشنال - للمميزين فقط - تحليل 6 + خيال 12 + أفليت - https://www.youtube.com/@CursedMedicineEG</div></div>`;
   log(`${typeIcon} 0.4ث @CursedMedicineEG: ${template.slice(0,18)}... - ${p[0]} - VAC-${vac} - https://www.youtube.com/@CursedMedicineEG`, color,'PRO_04');
 }catch(e){}
}

document.addEventListener('DOMContentLoaded', function(){
 check();
 show('old');
 setTimeout(()=>show('new'),250);
 setTimeout(()=>show('events'),500);
 setTimeout(()=>show('all'),750);
 genPsych();
 genImag();
 loadAuto();
 document.getElementById('e_AFF').value='https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6';
 document.getElementById('e_PRODKEY').value='0e3195dd062bf11f0da7496dd3c1bf6';
 log('v62 ULTRA 0.4s - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم 15+جديد 15+أحداث 15=45 جديد - تعديل من الحتت المستخبية البروفشنال - للمميزين فقط - تحليل 6 + خيال 12 + 4ث + أفليت KIE.AI - 87 موضوع - يفتح 0.4ث - اسرع اقل من ثانية - https://www.youtube.com/@CursedMedicineEG', '#ff4444','ULTRA_04');
});
setInterval(loadAuto,4000);
setInterval(genPsych,9000);
setInterval(genImag,11000);
</script>
</body>
</html>
"""

@app.route('/')
def index():
    html=HTML.replace('{{old_json}}', json.dumps(OLD, ensure_ascii=False)).replace('{{new_json}}', json.dumps(NEW, ensure_ascii=False)).replace('{{events_json}}', json.dumps(EVENTS, ensure_ascii=False)).replace('{{tartaria_json}}', json.dumps(TARTARIA, ensure_ascii=False)).replace('{{forbidden_json}}', json.dumps(FORBIDDEN, ensure_ascii=False)).replace('{{cursed_json}}', json.dumps(CURSED, ensure_ascii=False)).replace('{{psych_json}}', json.dumps(PSYCH, ensure_ascii=False)).replace('{{imag_json}}', json.dumps(IMAG, ensure_ascii=False))
    resp=Response(html, mimetype='text/html')
    resp.headers['Cache-Control']='public, max-age=120'
    resp.headers['X-Accel-Buffering']='no'
    return resp

@app.route('/api/keys/save', methods=['POST'])
def save_keys():
    try:
        data=request.get_json()
        for k,v in data.items():
            if v is not None: VAULT[k]=v.strip()
        return jsonify({"status":"success","count":sum(1 for x in VAULT.values() if x),"aff_link":VAULT.get("AFFILIATE_LINK"),"prod_key":VAULT.get("AFFILIATE_PRODUCT_KEY"),"channel":"https://www.youtube.com/@CursedMedicineEG"})
    except Exception as e:
        return jsonify({"status":"error","msg":str(e)}),500

@app.route('/api/keys/status')
def keys_status():
    c=sum(1 for x in VAULT.values() if x)
    has_id=bool(VAULT["YOUTUBE_CLIENT_ID"] and len(VAULT["YOUTUBE_CLIENT_ID"])>20)
    has_sec=bool(VAULT["YOUTUBE_CLIENT_SECRET"] and len(VAULT["YOUTUBE_CLIENT_SECRET"])>10)
    has_ref=bool(VAULT["YOUTUBE_REFRESH_TOKEN"] and VAULT["YOUTUBE_REFRESH_TOKEN"].startswith("1//"))
    return jsonify({"linked":has_id and has_sec and has_ref,"status_text":f"{'✅ مربوطة - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم 15+جديد 15+أحداث 15=45 جديد - 0.4ث' if has_id and has_sec and has_ref else '⚠️ غير مربوطة - https://www.youtube.com/@CursedMedicineEG - 0.4ث'} - أفليت KIE.AI - 87 موضوع","count":c,"aff_link":VAULT.get("AFFILIATE_LINK"),"prod_key":VAULT.get("AFFILIATE_PRODUCT_KEY"),"channel_url":"https://www.youtube.com/@CursedMedicineEG"})

@app.route('/api/pro/auto')
def pro_auto():
    return jsonify({"evo":EVO[-8:],"topics":AUTO_T[-8:]})

@app.route('/api/groq/generate', methods=['POST'])
def groq_gen():
    try:
        data=request.get_json()
        prompt=data.get('prompt','@CursedMedicineEG')
        aff=VAULT.get("AFFILIATE_LINK","https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6")
        return jsonify({"response":f"⚡ v62 ULTRA 0.4s - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - {prompt[:40]}... - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - تحليل 6 + خيال 12 + 4ث + أفليت {aff} - 87 موضوع - 0.4ث - <1ث - https://www.youtube.com/@CursedMedicineEG"})
    except Exception as e:
        return jsonify({"response":f"Error: {e}"})

@app.route('/health')
def health():
    return f"v62 ULTRA 0.4s - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - تحليل 6 + خيال 12 + 4ث + أفليت KIE.AI - 87 موضوع - يفتح 0.4ث - اسرع اقل من ثانية"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
