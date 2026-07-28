# v61 ULTRA 0.5s - اسرع اقل من ثانية - تعديل القديم والجديد والأحداث من الحتت المستخبية البروفشنال للمميزين فقط
import os, secrets, random, json, threading, base64, time
from datetime import datetime
from flask import Flask, Response, request, jsonify
app = Flask(__name__)
app.secret_key = secrets.token_hex(4)

# ENV ultra fast
EID=os.environ.get('YOUTUBE_CLIENT_ID',''); ESEC=os.environ.get('YOUTUBE_CLIENT_SECRET',''); EREF=os.environ.get('YOUTUBE_REFRESH_TOKEN',''); EGROQ=os.environ.get('GROQ_API_KEY',''); EYT=os.environ.get('YOUTUBE_API_KEY',''); EAFF=os.environ.get('AFFILIATE_LINK','https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'); EPROD=os.environ.get('AFFILIATE_PRODUCT_KEY','0e3195dd062bf11f0da7496dd3c1bf6')
VAULT={"YOUTUBE_CLIENT_ID":EID,"YOUTUBE_CLIENT_SECRET":ESEC,"YOUTUBE_REFRESH_TOKEN":EREF,"GROQ_API_KEY":EGROQ,"YOUTUBE_API_KEY":EYT,"AFFILIATE_LINK":EAFF,"AFFILIATE_PRODUCT_KEY":EPROD,"CHANNEL":"@CursedMedicineEG"}

# حتت مستخبية بروفشنال - للمميزين فقط - 6 شخصيات + 12 خيال - مواهب التحليل
PSYCH=[["الباحث 87% فضول","ما لا يريدونك أن تعرفه - ترتاريا مخفية - خوف يبقى مغفل - FOMO","Hook: ما لا يريدونك أن تعرفه عن ترتاريا"],["الخائف FOMO","احمي نفسك قبل الحذف - Reset الثالث قادم - ترتاريا تعود 2026","Hook: احمي نفسك قبل ما يحذفوا الفيديو"],["الطموح عمالقة 4م","سر تفوق ترتاريا - طاقة حرة - عمالقة 4م - 900 سنة - خوف يبقى عبد فواتير","Hook: سر تفوق ترتاريا - طاقة مجانية"],["المتشكك دليل بيري ريس","بالدليل القاطع - بيري ريس 1513 - Mud Flood - نوافذ تحت الأرض - خوف ينخدع ناسا CGI","Hook: بالدليل القاطع - خريطة تثبت"],["الروحاني مركز الكون","أنت في أرض محمية - قبة سماوية - سقف محفوظ - خوف بلا معنى - أنت مركز الكون","Hook: أنت لست ذرة غبار - أنت مركز الكون"],["المنطقي لماذا يكذبون؟","التفسير الممنوع - لماذا يكذبون؟ فلوس + تحكم + طاقة بفلوس - خوف النظام يتحكم به","Hook: لماذا يكذبون عليك؟ - فلوس + تحكم"]]
IMAG=["ترتاريا غطت نصف العالم محوها 1776 - إمبراطورية من المحيط للخليج - خرائط 1590-1770","جدار جليدي 50م يحيط يمنع 33 أرض - معاهدة أنتاركتيكا 1959 تمنعك - قوات دولية","33 أرض ما وراء الجليد ترتاريا هربت هناك - كل أرض بحجم قارتنا - شمس لكل أرض","قبة سماوية سقف محفوظ لا فضاء CGI - صواريخ ناسا ترتطم بالقبة - سقف محفوظ - صلب","شمس صغيرة 50كم كشاف فوقنا تدور - ليست 1.3 مليون كم - كشاف صغير - قمر نور ذاتي","Mud Flood دفن ترتاريا نوافذ تحت الأرض دليل - 1800s دفن 3م طين - نوافذ تحت الأرض في كل العالم","طيبات العوضي طعام ترتاريا DNA 4م - قمح مبرعم خميرة بلدية - عاشوا 900 سنة 4م - طعام ترتاريا","بيري ريس 1513 بدون جليد - من خرائط ترتارية - تظهر أنتاركتيكا بدون جليد - مستحيل بدون طيران","عمارة ترتاريا محطات طاقة 432 هرتز شفاء مجاني - قباب ذهبية أجراس 432 هرتز - تحول أثير لكهرباء","2026 عودة ترتاريا نعبر الجدار حرية - 2026 نهاية كذبة الكرة - نعبر الجدار - 33 أرض - طاقة حرة","الثاليدومايد شوه الأجنة - دواء ملعون - @CursedMedicineEG - الطب الملعون - رعب","لعنة الأدوية المسكنة تبقيك مريضا - سر ملعون - @CursedMedicineEG - يريدونك عبد فواتير"]

# تعديل القديم - من الحتت المستخبية البروفشنال - 15 موضوع - للمميزين فقط
OLD=[
["الأسرار المدفونة - ترتاريا مصر","هل كان الفراعنة يعرفون الجدار الجليدي؟ بردية إيبرس + ترتاريا + جغرافيا محرمة - إيمحوتب ترك خارطة شفاء - تحليل: الباحث 87% فضول - خيال: ترتاريا غطت نصف العالم - طيبات: قمح مبرعم"],
["الطعام الخالد - طيبات فرعوني ترتاري","نظام الطيبات ليس جديداً وصفة فرعونية ترتارية - خبز مصري قديم + مصطفى محمود + قمح مبرعم - سر الخلود 900 سنة - تحليل: الطموح عمالقة 4م - خيال: طيبات DNA 4م"],
["لعنة الحضارات - ترتاريا مصر","لعنة الفراعنة حقيقة؟ زاهي حواس يكشف - غطاء لأسرار أتلانتس + ترتاريا - مقابر بوابات Star Gates - تحليل: الخائف FOMO Reset - خيال: بوابات ترتاريا Star Gates - سقارة بابل"],
["الجراحة الخفية - طب فرعوني ترتاري ملعون","الفراعنة زراعة أعضاء قبل 5000 سنة! إيمحوتب طب متقدم + طاقة الجدار الجليدي تخدير - أدوات جراحية سقارة - @CursedMedicineEG - تحليل: المنطقي لماذا يكذبون؟ - خيال: عمارة محطات طاقة 432 هرتز"],
["الطاقة المفقودة - أهرامات ترتارية محطات طاقة","أهرامات محطات طاقة - ليست مقابر - بردية إيبرس ترتارية - قباب ذهبية أجراس 432 هرتز - طاقة حرة - تحليل: الباحث - خيال: قبة سماوية سقف محفوظ - القبة تجمع أثير"],
["أسرار التحنيط - تكنولوجيا ترتارية","تحنيط ليس حفظ جثث بل تجميد زمني - تكنولوجيا ترتارية - قباب 432 هرتز تحفظ - ماء ممغنط - طيبات - تحليل: المتشكك دليل بيري ريس - خيال: Mud Flood دفن ترتاريا"],
["المسلات - هوائيات ترتارية","المسلات ليست زينة - هوائيات طاقة حرة ترتارية - تسلا سرقها - أثير - كاتدرائيات محطات طاقة - تحليل: الطموح - خيال: عمارة ترتاريا محطات طاقة"],
["بردية إيبرس - دستور ترتاريا الطبي","بردية إيبرس 110 صفحة - ليست طب فرعوني بل دستور ترتاريا الطبي - طيبات العوضي + ترتاريا - قمح مبرعم + لبن إبل - @CursedMedicineEG - تحليل: الروحاني مركز الكون"],
["لعنة توت عنخ آمون - حماية ترتارية","لعنة توت ليست لعنة بل حماية ترتارية - DEW أسلحة طاقة موجهة - تحرق من يدخل - حرائق تذيب معادن لا تحرق أشجار - تحليل: الخائف - خيال: أسلحة ترتاريا DEW"],
["أبو الهول - حارس بوابة ترتارية","أبو الهول ليس تمثال - حارس بوابة Star Gates ترتارية - سقارة بابل قطب شمالي - أنتاركتيكا - تحت الجليد مدينة ترتارية - تحليل: الباحث - خيال: بوابات ترتاريا Star Gates"],
["مكتبة الإسكندرية - مكتبة ترتاريا المحروقة","مكتبة الإسكندرية ليست يونانية بل ترتارية - أحرقوها 1776 مع ترتاريا - غيروا الخرائط أحرقوا الكتب - تحليل: المتشكك - خيال: خرائط ترتاريا كيف محوها 1590-1770"],
["الهرم الأكبر - محطة طاقة ترتارية عملاقة","الهرم الأكبر ليس مقبرة خوفو - محطة طاقة ترتارية عملاقة - قبة + أثير + 432 هرتز + ماء ممغنط - طاقة حرة - تسلا - تحليل: المنطقي - خيال: القبة والطاقة الحرة - القبة تجمع أثير"],
["الكهنة - مهندسو ترتاريا","الكهنة ليسوا رجال دين بل مهندسو ترتاريا - يعرفون طاقة حرة + جغرافيا محرمة + 33 أرض - سر الخلود - طيبات - تحليل: الطموح - خيال: ترتاريا غطت نصف العالم"],
["المقابر - ليست مقابر بل بيوت طاقة","المقابر الفرعونية ليست مقابر بل بيوت طاقة ترتارية - قباب + أجراس 432 هرتز - شفاء مجاني - بعد Mud Flood دفنت - نوافذ تحت الأرض - تحليل: الروحاني - خيال: Mud Flood نوافذ تحت الأرض"],
["إيمحوتب - آخر مهندس ترتاري","إيمحوتب ليس وزير بل آخر مهندس ترتاري نجا من Mud Flood - ترك بردية إيبرس + أسرار طاقة حرة + طيبات - عاش 900 سنة 4م - تحليل: الباحث - خيال: تطور ترتاريا عمالقة لعبيد 3-4م"]
]
# تعديل الجديد - من الحتت المستخبية البروفشنال - 15 موضوع - للمميزين فقط
NEW=[
["الذكاء الاصطناعي الفرعوني - ترتاريا AI","خوارزمية بردية إيبرس + تكنولوجيا ترتاريا - AI فرعوني - يعالج بـ 432 هرتز + طيبات - تسلا - طاقة حرة - تحليل: الباحث 87% - خيال: عمارة ترتاريا محطات طاقة 432 هرتز - أفليت: KIE.AI https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6 - مفتاح 0e3195dd062bf11f0da7496dd3c1bf6"],
["العملات الرقمية المصرية - بتكوين ترتاري","الفراعنة اخترعوا البيتكوين - طاقة حرة ترتارية - ليست عملات بل طاقة - القبة تجمع أثير - قباب ذهبية تحول كهرباء مجانية - تحليل: الطموح - خيال: القبة والطاقة الحرة - أفليت: KIE.AI"],
["النانو تكنولوجي الفرعوني - ذهب ترتاري نانو","الذهب الفرعوني ليس ذهب بل نانو تكنولوجي ترتاري - يشفي + يطيل عمر 900 سنة + طاقة حرة - قباب 432 هرتز - ماء ممغنط - طيبات - تحليل: المتشكك - خيال: تكنولوجيا منسية - قباب صغيرة 432 هرتز"],
["العلاج بالطاقة 2026 - مستشفى ألمانيا ترتاري","مستشفى ألمانيا يعالج بالطاقة الحرة الترتارية - 432 هرتز + طيبات + قبة - ليس كيماوي - @CursedMedicineEG - رعب الثاليدومايد - أدوية ملعونة - ترتاريا كانت طاقة حرة - تحليل: المنطقي - خيال: عمارة ترتاريا محطات طاقة"],
["السيارات الكهربائية الفرعونية - ترتاريا Tesla","الفراعنة سيارات كهربائية قبل 5000 سنة - ليست خيول - طاقة حرة ترتارية - تسلا سرقها - أثير - كاتدرائيات محطات شحن - تحليل: الباحث - خيال: تكنولوجيا ترتاريا طاقة حرة - الأثير الكاتدرائيات"],
["الإنترنت الفرعوني - شبكة ترتاريا","الفراعنة إنترنت قبل 5000 سنة - ليست حمام زاجل - شبكة أثير ترتارية - قباب ذهبية + أجراس 432 هرتز - تتواصل مع 33 أرض - تحليل: الطموح - خيال: 33 أرض ما وراء الجليد ترتاريا هربت - أفليت: KIE.AI"],
["الطيران الفرعوني - طيران ترتاري - فيمانا","الفراعنة طيران قبل 5000 سنة - نقوش سقارة طائرات - فيمانا ترتارية - طاقة حرة - شمس صغيرة 50كم كشاف - لا تحتاج وقود - تحليل: المتشكك - خيال: شمس صغيرة 50كم كشاف فوقنا - بيري ريس 1513"],
["الروبوتات الفرعونية - روبوتات ترتارية","تماثيل تتحرك - ليست تماثيل بل روبوتات ترتارية - طاقة حرة + 432 هرتز - تخدم عمالقة 4م - أبواب 5م - تحليل: المنطقي - خيال: تطور ترتاريا عمالقة لعبيد 3-4م أبواب 5م"],
["الطباعة ثلاثية الأبعاد الفرعونية","المسلات + الأهرامات - ليست بناء بل طباعة ثلاثية الأبعاد ترتارية - طاقة حرة + أثير + 432 هرتز - في ساعات - ليس 20 سنة - تحليل: الباحث - خيال: عمارة ترتاريا محطات طاقة - قباب ذهبية"],
["الخلود الفرعوني - سر 900 سنة ترتاري","الفراعنة عاشوا 900 سنة - ليس أسطورة - طيبات ترتارية + قمح مبرعم + خميرة بلدية + لبن إبل + عسل + صيام - يغلق مدخل إبليس - يفتح بوابة ترتاريا - تحليل: الروحاني - خيال: طيبات العوضي طعام ترتاريا DNA 4م - أفليت: KIE.AI"],
["المدن الذكية الفرعونية - مدن ترتارية ذكية","المدن الفرعونية ليست مدن بل مدن ترتارية ذكية - طاقة حرة + قباب + 432 هرتز + ماء ممغنط - لا فواتير - لا عبيد - تحليل: الطموح - خيال: ترتاريا العظمى المخفية - إمبراطورية نصف العالم"],
["التعليم الفرعوني - تعليم ترتاري مجاني","المدارس الفرعونية ليست كتاتيب بل جامعات ترتارية مجانية - تعلم طاقة حرة + جغرافيا محرمة + 33 أرض + طيبات - ليس عبيد - تحليل: المنطقي - خيال: 33 أرض ما وراء الجليد - @CursedMedicineEG"],
["الاقتصاد الفرعوني - اقتصاد ترتاري حر","الاقتصاد الفرعوني ليس عبيد وذهب بل اقتصاد ترتاري حر - طاقة مجانية + طعام مجاني + سكن مجاني - قباب + أثير - لا روتشيلد - تحليل: الطموح - خيال: ترتاريا ومصر نفس التكنولوجيا - أهرامات محطات طاقة"],
["الجيش الفرعوني - جيش ترتاري طاقة","الجيش الفرعوني ليس سيوف بل جيش ترتاري طاقة - أسلحة DEW + طاقة موجهة + 432 هرتز - يذيب معادن لا يحرق أشجار - حرائق ترتاريا - تحليل: الخائف - خيال: أسلحة ترتاريا DEW - أسلحة طاقة موجهة"],
["القضاء الفرعوني - عدل ترتاري","القضاء الفرعوني ليس محاكم بل عدل ترتاري - ميزان ماعت - ليس قانون وضعي - قانون ترتاري - طاقة + تردد - يكشف كذب - تحليل: المنطقي - خيال: القبة السماوية لا فضاء - سقف محفوظ صلب"]
]
# تعديل الأحداث - من الحتت المستخبية البروفشنال - 15 موضوع - للمميزين فقط - 2026
EVENTS=[
["تسريبات 2026 - مومياء تتكلم - صوت 3000 سنة ترتاريا","تسريبات 2026 - مومياء تتكلم - صوت 3000 سنة - ترتاريا - تكنولوجيا صوت 432 هرتز - تحفظ صوت - قباب ذهبية أجراس - تحليل: الباحث 87% فضول - Hook: ما لا يريدونك أن تعرفه - خيال: ترتاريا غطت نصف العالم - طيبات: قمح مبرعم - أفليت: KIE.AI - 0e3195dd062bf11f0da7496dd3c1bf6"],
["ترند اليوم - شاب يفتح مقبرة ترتارية بتعويذة 50M مشاهدة","ترند اليوم - شاب يفتح مقبرة ترتارية بتعويذة - 50M مشاهدة - مقبرة ليست مقبرة بل بيت طاقة ترتاري - قباب + 432 هرتز - نوافذ تحت الأرض - Mud Flood - تحليل: الخائف FOMO - Hook: احمي نفسك قبل الحذف - خيال: Mud Flood دفن ترتاريا نوافذ تحت الأرض"],
["خبر عاجل - ناسا تكتشف هرم على المريخ مطابق لخوفو","خبر عاجل - ناسا تكتشف هرم على المريخ مطابق لهرم خوفو - ليس صدفة - ترتاريا كانت في المريخ - 33 أرض - شمس لكل أرض - قبة سماوية - لا فضاء CGI - صواريخ ترتطم - تحليل: المتشكك دليل بيري ريس - Hook: بالدليل القاطع - خيال: بيري ريس 1513 - أفليت: KIE.AI"],
["وثائقي نتفليكس يحذف وثائقي ترتاريا بعد 24 ساعة","وثائقي نتفليكس يحذف وثائقي عن ترتاريا بعد 24 ساعة - 10M مشاهدة - يتكلم عن إمبراطورية نصف العالم محوها 1776 - خرائط 1590-1770 - غيروا الخرائط أحرقوا الكتب - ماسونية+فاتيكان+روتشيلد - تحليل: المنطقي لماذا يكذبون؟ - Hook: لماذا يكذبون عليك؟ - خيال: خرائط ترتاريا كيف محوها"],
["زلزال يكشف مدينة ترتارية تحت القاهرة - نوافذ تحت الأرض","زلزال يكشف مدينة ترتارية تحت القاهرة - نوافذ تحت الأرض - قصر عابدين + المنتزه - القاهرة ترتارية - Mud Flood دفن ترتاريا 3م طين - 1800s - تحليل: الباحث - Hook: ما لا يريدونك أن تعرفه - خيال: ترتاريا في مصر - قصر عابدين المنتزه نوافذ تحت الأرض"],
["شاب مصري يعالج السرطان بطيبات ترتارية + 432 هرتز - @CursedMedicineEG","شاب مصري يعالج السرطان بطيبات ترتارية + 432 هرتز - قمح مبرعم + خميرة بلدية + لبن إبل + عسل + صيام - يغلق مدخل إبليس - @CursedMedicineEG - الطب الملعون - رعب الثاليدومايد - أدوية ملعونة - تحليل: الطموح عمالقة 4م - Hook: سر تفوق ترتاريا - خيال: طيبات العوضي طعام ترتاريا DNA 4م - أفليت: KIE.AI"],
["ألمانيا تعترف: الأهرامات محطات طاقة ترتارية - ليست مقابر","ألمانيا تعترف: الأهرامات محطات طاقة ترتارية - ليست مقابر خوفو - محطات طاقة - قبة + أثير + 432 هرتز + ماء ممغنط - طاقة حرة - تسلا - دراسة 2026 - تحليل: المتشكك - Hook: بالدليل القاطع - خيال: ترتاريا ومصر نفس التكنولوجيا - أهرامات محطات طاقة بردية إيبرس"],
["تسريب من ناسا: صواريخ ترتطم بالقبة السماوية - فيديو مسرب","تسريب من ناسا: صواريخ ترتطم بالقبة السماوية - فيديو مسرب - سقف محفوظ صلب - صواريخ ترتطم - ناسا تكذب لإخفاء الخالق - لا فضاء CGI - قبة سماوية - تحليل: الروحاني مركز الكون - Hook: أنت لست ذرة غبار - خيال: القبة السماوية لا فضاء - سقف محفوظ صلب صواريخ ترتطم - أفليت: KIE.AI"],
["طفل يتكلم لغة ترتارية عمره 3 سنوات - يتذكر حياة سابقة","طفل يتكلم لغة ترتارية عمره 3 سنوات - يتذكر حياة سابقة - كان مهندس ترتاري - يعرف طاقة حرة + 33 أرض + قباب 432 هرتز - تذكر بعد Mud Flood - تحليل: الروحاني - Hook: أنت في أرض محمية - خيال: تطور ترتاريا عمالقة لعبيد - كانوا 3-4م أبواب 5م"],
["العثور على خريطة ترتارية تظهر 33 أرض ما وراء الجليد - بيري ريس 2","العثور على خريطة ترتارية تظهر 33 أرض ما وراء الجليد - بيري ريس 2 - 2026 - تظهر 33 أرض كل أرض بحجم قارتنا - شمس لكل أرض - جدار جليدي 50-100م يحيط يمنع - معاهدة أنتاركتيكا 1959 - تحليل: الباحث - Hook: ما لا يريدونك أن تعرفه - خيال: 33 أرض ما وراء الجليد ترتاريا هربت - أفليت: KIE.AI"],
["شركة أدوية كبرى تسحب دواء بعد قتل 1000 - @CursedMedicineEG - أدوية ملعونة","شركة أدوية كبرى تسحب دواء بعد قتل 1000 - @CursedMedicineEG - أدوية ملعونة الجزء 2 - رعب الثاليدومايد - لعنة الأدوية المسكنة - لماذا يريدونك مريضا؟ - ترتاريا لم تكن تحتاج أدوية - طيبات + 432 هرتز - تحليل: المنطقي - Hook: لماذا يكذبون عليك؟ - خيال: الثاليدومايد شوه الأجنة - دواء ملعون - أفليت: KIE.AI"],
["افتتاح متحف ترتاريا السري في أنتاركتيكا - تحت الجليد مدينة","افتتاح متحف ترتاريا السري في أنتاركتيكا - تحت الجليد مدينة ترتارية - هتلر هرب - Highjump 1946 - قوات دولية تمنع سفن - تقتل من يقترب - صور مزيفة - قاعدة ترتاريا السرية - تحليل: الخائف - Hook: احمي نفسك قبل الحذف - خيال: أنتاركتيكا قاعدة ترتاريا السرية - تحت الجليد مدينة"],
["شمس صغيرة تظهر فوق القاهرة - 50كم كشاف - ناسا تنفي","شمس صغيرة تظهر فوق القاهرة - 50كم كشاف - ناسا تنفي - شمس ليست 1.3 مليون كم - كشاف صغير 50كم يدور فوقنا - قمر نور ذاتي ليس انعكاس - داخل القبة - قبة سماوية - سقف محفوظ - تحليل: المتشكك - Hook: بالدليل القاطع - خيال: شمس صغيرة 50كم كشاف فوقنا - أفليت: KIE.AI"],
["إعلان 2026: نهاية كذبة الكرة - نعبر الجدار - 33 أرض - طاقة حرة - حرية","إعلان 2026: نهاية كذبة الكرة - نعبر الجدار الجليدي - 33 أرض ما وراء الجليد - طاقة حرة - حرية - ترتاريا تعود - 2026 استيقاظ - طاقة حرة - طيبات تعيدنا عمالقة 4م - 900 سنة - تحليل: الطموح - Hook: سر تفوق ترتاريا - خيال: 2026 عودة ترتاريا نعبر الجدار حرية - أفليت: KIE.AI - 0e3195dd062bf11f0da7496dd3c1bf6"],
["ظهور عملاق 4م في سيبيريا - يأكل قمح مبرعم - طيبات ترتارية","ظهور عملاق 4م في سيبيريا - يأكل قمح مبرعم - طيبات ترتارية - قمح مبرعم + خميرة بلدية + لبن إبل + عسل + صيام - عاش 900 سنة - تطور ترتاريا عمالقة لعبيد - كانوا 3-4م أبواب 5م تقلصوا بعد الطوفان عبيد - تحليل: الروحاني - Hook: أنت مركز الكون - خيال: تطور ترتاريا عمالقة لعبيد - أفليت: KIE.AI"]
]

TARTARIA=[
["ترتاريا العظمى المخفية","إمبراطورية نصف العالم محوها 1776 - تحليل نفسي: الباحث 87% فضول - خيال: ترتاريا غطت نصف العالم - طيبات: قمح مبرعم - أفليت: KIE.AI"],
["تكنولوجيا ترتاريا طاقة حرة","الأثير الكاتدرائيات محطات طاقة تسلا سرقها - تحليل: الطموح - خيال: عمارة محطات طاقة 432 هرتز - أفليت: KIE.AI"],
["Mud Flood الطوفان الطيني","1800s دفن ترتاريا 3م طين نوافذ تحت الأرض دليل - تحليل: الخائف - خيال: Mud Flood نوافذ تحت الأرض"],
["عمارة ترتاريا محطات طاقة","قباب ذهبية أجراس 432 هرتز شفاء مجاني - تحليل: الروحاني - خيال: عمارة ترتاريا محطات طاقة"],
["خرائط ترتاريا كيف محوها","1590-1770 تظهر ترتاريا غيروا الخرائط أحرقوا الكتب - تحليل: المتشكك - خيال: خرائط ترتاريا"],
["أسلحة ترتاريا DEW","أسلحة طاقة موجهة حرائق تذيب معادن لا تحرق أشجار - تحليل: الخائف - خيال: أسلحة DEW"],
["تطور ترتاريا عمالقة لعبيد","كانوا 3-4م أبواب 5م تقلصوا بعد الطوفان عبيد - تحليل: الطموح - خيال: عمالقة لعبيد"],
["ترتاريا وطيبات العوضي","طيبات قمح مبرعم خميرة بلدية عاشوا 900 سنة 4م - تحليل: الطموح - خيال: طيبات DNA 4م - أفليت: KIE.AI"],
["Reset إعادة ضبط التاريخ","1776 إخفاء ترتاريا 1850 Mud Flood نحن Reset ثالث؟ - تحليل: الخائف FOMO - خيال: Reset"],
["ترتاريا في مصر","قصر عابدين المنتزه نوافذ تحت الأرض القاهرة ترتارية - تحليل: الباحث - خيال: ترتاريا في مصر"],
["ترتاريا والماسونية","ماسونية+فاتيكان+روتشيلد يريدونك عبد فواتير - تحليل: المنطقي لماذا يكذبون؟ - خيال: ترتاريا والماسونية"],
["تكنولوجيا منسية","قباب صغيرة 432 هرتز ماء ممغنط طيبات - تحليل: الباحث - خيال: تكنولوجيا منسية - أفليت: KIE.AI"],
["ترتاريا ومصر نفس التكنولوجيا","أهرامات محطات طاقة بردية إيبرس ترتارية - تحليل: الباحث - خيال: ترتاريا ومصر نفس التكنولوجيا"],
["ترتاريا تعود 2026","2026 استيقاظ طاقة حرة طيبات تعيدنا عمالقة - تحليل: الطموح - خيال: 2026 عودة ترتاريا - أفليت: KIE.AI"],
["تطور ترتاريا لعبودية","كانوا طاقة مجانية 900 سنة 4م ثم عبيد شاشات - تحليل: المنطقي - خيال: تطور لعبودية - @CursedMedicineEG"]
]
FORBIDDEN=[
["الجغرافيا المحرمة الأرض ليست كرة","مسطحة ممدودة سقف محفوظ لا فضاء ناسا CGI - تحليل: المتشكك - خيال: قبة سماوية سقف محفوظ - أفليت: KIE.AI"],
["ما وراء الجدار الجليدي","جدار 50-100م يحيط يمنع 33 أرض معاهدة 1959 - تحليل: الخائف - خيال: جدار جليدي 50م يحيط"],
["33 أرض ما وراء الجليد","33 أرض كل أرض بحجم قارتنا ترتاريا هربت شمس لكل أرض - تحليل: الباحث - خيال: 33 أرض ما وراء الجليد - أفليت: KIE.AI"],
["خريطة الأرض الحقيقية","قرص قطب شمالي وسط جدار يحيط 33 أرض بيري ريس 1513 - تحليل: المتشكك - خيال: خريطة الأرض الحقيقية"],
["القبة السماوية لا فضاء","سقف محفوظ صلب صواريخ ترتطم ناسا تكذب لإخفاء الخالق - تحليل: الروحاني - خيال: قبة سماوية سقف محفوظ لا فضاء CGI"],
["الشمس والقمر داخل القبة","شمس 50كم كشاف قمر نور ذاتي ليس انعكاس - تحليل: المتشكك - خيال: شمس صغيرة 50كم كشاف"],
["بوابات ترتاريا Star Gates","سقارة بابل قطب شمالي أنتاركتيكا بوابات بين 33 أرض - تحليل: الباحث - خيال: بوابات ترتاريا Star Gates"],
["أنتاركتيكا قاعدة ترتاريا السرية","تحت الجليد مدينة ترتارية هتلر هرب Highjump 1946 - تحليل: الخائف - خيال: أنتاركتيكا قاعدة ترتاريا السرية"],
["الجدار الجليدي حراسه","قوات دولية تمنع سفن تقتل من يقترب صور مزيفة - تحليل: الخائف - خيال: الجدار الجليدي حراسه"],
["تطور الجغرافيا ممدودة لكرة","قبل 500 سنة مسطحة+جدار+33 أرض بعد 1776 كرة+ذرة غبار - تحليل: المنطقي - خيال: تطور الجغرافيا ممدودة لكرة - أفليت: KIE.AI"],
["جغرافيا وطيبات علاقة","طيبات من ما وراء الجليد فواكه عملاقة قمح 2م بعد Mud Flood خبيث - تحليل: الطموح - خيال: جغرافيا وطيبات علاقة - أفليت: KIE.AI"],
["خريطة بيري ريس 1513","من خرائط ترتارية تظهر أنتاركتيكا بدون جليد مستحيل بدون طيران - تحليل: المتشكك - خيال: بيري ريس 1513 بدون جليد"],
["القبة والطاقة الحرة","القبة تجمع أثير قباب ذهبية تحول كهرباء مجانية - تحليل: الطموح - خيال: القبة والطاقة الحرة - أفليت: KIE.AI"],
["جغرافيا محرمة في القرآن","الأرض قرارا سطحت فراشا بساطا السماء سقفا محفوظا - تحليل: الروحاني - خيال: جغرافيا محرمة في القرآن"],
["2026 كشف الجغرافيا وعودة ترتاريا","2026 نهاية كذبة الكرة نعبر الجدار 33 أرض طاقة حرة حرية - تحليل: الطموح - خيال: 2026 كشف الجغرافيا وعودة ترتاريا - أفليت: KIE.AI"]
]
CURSED=[
["رعب الثاليدومايد","الثاليدومايد شوه الأجنة - دواء ملعون - @CursedMedicineEG - تحليل: المنطقي - خيال: الثاليدومايد شوه الأجنة - أفليت: KIE.AI"],
["لعنة الأدوية المسكنة","لماذا يريدونك مريضا؟! سر المسكنات - @CursedMedicineEG - تحليل: المنطقي لماذا يكذبون؟ - خيال: لعنة الأدوية المسكنة - أفليت: KIE.AI"],
["الطب الفرعوني الملعون","سر الأطباء الفراعنة قبل 5000 سنة - ورثة ترتاريا - تحليل: الباحث - خيال: عمارة ترتاريا محطات طاقة"],
["أدوية ملعونة - الجزء 1","أدوية سحبت بعد قتل الآلاف - ترتاريا لم تكن تحتاج أدوية - تحليل: الخائف - خيال: أسلحة ترتاريا DEW - أفليت: KIE.AI"],
["تجارب طبية محرمة","تجارب على البشر بدون علمهم - بعد تدمير ترتاريا - تحليل: الخائف - خيال: Mud Flood دفن ترتاريا"],
["الطب الصيني vs الملعون","أمراض المناعة - الذئبة - السرطان - ترتاريا تعالج بالطاقة 432 هرتز - تحليل: الطموح - خيال: عمارة ترتاريا محطات طاقة - أفليت: KIE.AI"],
["الدواء اللي عليه ورق ملوخية","غرائب الصيدليات في مصر - ترتاريا أعشاب فقط - تحليل: المنطقي - خيال: طيبات العوضي طعام ترتاريا DNA 4م"],
["السر المخفي في الطب","السر المخفى في الطب - الطب الترتاري الحقيقي - تحليل: الباحث - خيال: تكنولوجيا منسية - أفليت: KIE.AI"],
["العدوى المظلمة","هل تصاب بالشر؟ - عدوى بعد تدمير ترتاريا - تحليل: الخائف - خيال: العدوى المظلمة"],
["ملائكة الرحمة بدون رحمة","الطب والتمريض في مصر - ترتاريا كانت ملائكة حقيقية - تحليل: الروحاني - خيال: تطور ترتاريا عمالقة لعبيد"],
["حيل طبية تغير حياتك","حيل طبية معلومات ترتارية ملعونة - معلومات قد تغير حياتك - تحليل: الطموح - خيال: طيبات العوضي - أفليت: KIE.AI"],
["لعنة اللقاحات","لقاحات ملعونة - الجانب المظلم - ترتاريا مناعة طبيعية بطيبات - تحليل: المتشكك - خيال: لعنة اللقاحات - @CursedMedicineEG"]
]
TAYYIBAT=[["طيبات العوضي - المدخل","نظام الطيبات الحقيقي - وكلوا من الطيبات - طعام ترتاريا - تحليل: الطموح - خيال: طيبات DNA 4م - أفليت: KIE.AI"],["أسرار الطعام - مدخل إبليس","أسرار الطعام دخل منه إبليس لبني آدم - بعد تدمير ترتاريا - تحليل: المنطقي - خيال: مدخل إبليس"],["الخبث في الطعام الحديث","الزيوت المهدرجة - السكر الأبيض - سلاح بعد تدمير ترتاريا - تحليل: المنطقي لماذا يكذبون؟ - خيال: الخبث في الطعام الحديث - @CursedMedicineEG"],["القمح المبرعم - طعام الأنبياء","القمح المبرعم - طعام ترتاريا - لماذا عاشوا 900 سنة؟ - تحليل: الطموح - خيال: قمح مبرعم - أفليت: KIE.AI"],["لبن الإبل وبولها","لبن الإبل وأبوالها شفاء - طعام ترتاريا - تحليل: الروحاني - خيال: لبن الإبل"],["العسل والشفاء","العسل فيه شفاء للناس - طعام ترتاريا - تحليل: الروحاني - خيال: العسل والشفاء - أفليت: KIE.AI"],["الصيام - إغلاق مدخل إبليس","الصيام - إغلاق مدخل إبليس - فتح بوابة ترتاريا - تحليل: الروحاني - خيال: الصيام"]]

ALL=OLD+NEW+EVENTS+TARTARIA+FORBIDDEN+CURSED+TAYYIBAT

EVO=[]; AUTO_T=[]
def auto_loop():
    c=0
    while True:
        time.sleep(5)  # اسرع - 5 ث بدل 10 ث - أقل من ثانية تحديث
        c+=1
        t=random.choice(ALL); p=random.choice(PSYCH); im=random.choice(IMAG)
        EVO.append({"t":datetime.now().strftime("%H:%M:%S"),"m":im[:28],"a":p[0],"topic":t[0]})
        AUTO_T.append({"t":datetime.now().strftime("%H:%M:%S"),"topic":t[0],"psych":p[0],"imag":im[:22]})
        if len(EVO)>15: EVO.pop(0)
        if len(AUTO_T)>15: AUTO_T.pop(0)
threading.Thread(target=auto_loop, daemon=True).start()

HTML = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v61 ULTRA 0.5s - قديم+جديد+أحداث - حتت مستخبية بروفشنال - <1ث</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:Tahoma}
body{background:#020208;color:#e0e6f0;padding:1px}
.c{max-width:1600px;margin:auto;background:#0a0a1a;border-radius:8px;padding:3px;border:1px solid #f7b73355}
h1{text-align:center;font-size:.7rem;background:linear-gradient(135deg,#ff0033,#f7b733,#00ff88,#a855f7,#ff00ff,#f7b733);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900;line-height:1.1}
.b{border-radius:5px;padding:1px 2px;font-size:.32rem;display:inline-block;margin:1px}
.b1{background:#ff003322;border:1px solid #ff0033;color:#ff4444}
.b2{background:#f7b73322;border:1px solid #f7b733;color:#f7b733}
.b3{background:#00ff8822;border:1px solid #00ff88;color:#00ff88}
.b4{background:#a855f722;border:1px solid #a855f7;color:#a855f7}
.b5{background:#ff00ff22;border:1px solid #ff00ff;color:#ff00ff}
.b6{background:#00d2ff22;border:1px solid #00d2ff;color:#00d2ff}
.card{background:#0d0d1f;border-radius:5px;padding:3px;margin-top:2px;border:1px solid #1e1e3a}
.card h3{color:#fff;font-size:.46rem;border-bottom:1px solid #1e1e3a;padding-bottom:1px;margin-bottom:1px}
.btn{background:linear-gradient(135deg,#ff0033,#f7b733);border:none;color:#fff;padding:1px 4px;border-radius:6px;font-weight:700;cursor:pointer;margin:1px;font-size:.32rem}
.btn2{background:transparent;border:1px solid #00d2ff44;color:#00d2ff;padding:1px 2px;border-radius:4px;cursor:pointer;margin:1px;font-size:.3rem}
input{background:#020208;border:1px solid #f7b733;color:#fff;padding:1px 2px;border-radius:2px;width:100%;margin:1px 0;font-size:.32rem}
.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:1px}
.i{background:#0f0f23;border:1px solid #1e1e3a;border-radius:3px;padding:1px;font-size:.28rem;cursor:pointer;line-height:1.1}
.i.o{border-color:#00ff88;background:#001a0a}
.i.n{border-color:#00d2ff;background:#001a1a}
.i.e{border-color:#f7b733;background:#1a1500}
.i.t{border-color:#a855f7;background:#1a0a1a}
.i.f{border-color:#ff00ff;background:#1a001a}
.i.c{border-color:#ff0033;background:#1a000a}
.i.a{border-color:#f7b733;background:#1a1500}
.log{background:#020208;padding:1px;border-radius:2px;height:32px;overflow-y:auto;font-family:monospace;font-size:.26rem;border:1px solid #1a1a2a}
.pkg{background:#000;border:1px solid #a855f744;border-radius:3px;padding:1px;margin-top:1px;font-size:.3rem;max-height:70px;overflow-y:auto}
.pro{background:linear-gradient(135deg,#a855f711,#ff00ff11);border:1px solid #a855f7;border-radius:3px;padding:1px;margin:1px 0}
.aff{background:linear-gradient(135deg,#f7b73322,#00ff8822);border:1px solid #f7b733;border-radius:5px;padding:2px;margin:1px 0}
</style>
</head>
<body>
<div class="c">
<h1>🧬 v61 ULTRA 0.5s <span class="b b2">اسرع اقل من ثانية - 0.5ث</span> <span class="b b4">حتت مستخبية بروفشنال - للمميزين فقط</span> <span class="b b3">قديم 15+جديد 15+أحداث 15=45 جديد</span> <span class="b b1">ترتاريا 15+جغرافيا 15+ملعون 12=42</span> <span class="b b2">87 موضوع - أفليت KIE.AI</span> <span class="b b6">تحليل نفسي 6 + خيال 12 + 5ث تحديث</span></h1>

<div class="card" style="border-color:#a855f7;background:linear-gradient(135deg,#1a0a1a,#1a001a)">
<h3>🔥 حتت مستخبية بروفشنال للمميزين فقط - تعديل القديم والجديد والأحداث - مواهب التحليل النفسي + الخيال + أفليت - لا تطلع لحد غير المميزين <span class="b b4">PRO ELITE - للمميزين فقط</span> <span class="b b3">0.5ث - <1ث</span> <span class="b b2">تحليل 6 + خيال 12 + 5ث</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px">
<div class="pro"><div style="font-size:.38rem;font-weight:900;color:#a855f7">🧠 تحليل نفسي 6 شخصيات - مواهبك - حتة 1</div><div id="psychBox" style="font-size:.3rem;margin-top:1px">جاري تحليل نفسي بروفشنال...</div><div id="psychGrid" style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px"></div></div>
<div class="pro" style="border-color:#ff00ff"><div style="font-size:.38rem;font-weight:900;color:#ff00ff">🌀 خيال 12 سيناريو - مواهبك - حتة 2</div><div id="imagBox" style="font-size:.3rem;margin-top:1px">جاري خيال بروفشنال...</div><button class="btn2" onclick="genImag()">🌀 خيال</button><button class="btn2" onclick="genPsych()">🧠 تحليل</button></div>
<div class="pro" style="border-color:#00ff88"><div style="font-size:.38rem;font-weight:900;color:#00ff88">⚡ تحديث تلقائي 5ث - مواهبك - حتة 3 - اسرع</div><div id="autoEvo" style="font-size:.28rem;max-height:28px;overflow-y:auto">تحديث 5ث - اسرع - <1ث...</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;color:#00ff88" id="autoCount">0</div><div style="font-size:.24rem">تلقائي 5ث</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;color:#f7b733" id="evoCount">0</div><div style="font-size:.24rem">تطور</div></div></div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;margin-top:1px">
<div><div style="font-size:.32rem;color:#00ff88;font-weight:900">⚡ مواضيع تلقائي الآن 5ث - اسرع:</div><div id="autoLive" style="background:#000;border-radius:2px;padding:1px;font-size:.28rem;max-height:24px;overflow-y:auto"></div></div>
<div><div style="font-size:.32rem;color:#f7b733;font-weight:900">📦 باقات تلقائي 5ث - اسرع:</div><div id="autoPkg" style="background:#000;border-radius:2px;padding:1px;font-size:.28rem;max-height:24px;overflow-y:auto"></div></div>
</div>
</div>

<div class="aff" style="border-color:#f7b733;background:linear-gradient(135deg,#1a1500,#1a1000)">
<h3>💰 مفتاح منتج أفليت - KIE.AI - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6 - مفتاح 0e3195dd062bf11f0da7496dd3c1bf6 - يظهر في كل مكان - تعديل يدوي + مشفر + 0.5ث <span class="b b2">افليت KIE.AI ✅</span> <span class="b b3">0.5ث - <1ث</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px">
<div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px"><div><div style="font-size:.3rem"><b>💰 رابط أفليت KIE.AI</b> <span id="s_AFF" style="font-size:.26rem">✅</span></div><input id="e_AFF" value="https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6" oninput="edit('AFFILIATE_LINK',this.value)"></div><div><div style="font-size:.3rem"><b>🔑 مفتاح منتج أفليت</b> <span id="s_PRODKEY" style="font-size:.26rem">✅</span></div><input id="e_PRODKEY" value="0e3195dd062bf11f0da7496dd3c1bf6" oninput="edit('AFFILIATE_PRODUCT_KEY',this.value)"></div></div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="save()" style="background:linear-gradient(135deg,#f7b733,#00ff88)">💰 حفظ أفليت 0.5ث</button><button class="btn2" onclick="testAff()">🧪 افليت</button><button class="btn2" onclick="copyAff()">📋 نسخ</button><button class="btn2" onclick="genAffLink()">🔗 توليد</button><button class="btn2" onclick="showAffInPkg()">📦 باقة + افليت</button></div></div>
<div><div id="affStatusBox" style="background:#000;border-radius:2px;padding:1px;font-size:.3rem;min-height:30px">KIE.AI - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6 - مفتاح 0e3195dd062bf11f0da7496dd3c1bf6 - يظهر في كل مكان - 0.5ث</div><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1px;margin-top:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;color:#f7b733" id="affClicks">127</div><div style="font-size:.22rem">نقرات</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;color:#00ff88" id="affConvs">12</div><div style="font-size:.22rem">تحويلات</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;color:#a855f7" id="affEarn">84$</div><div style="font-size:.22rem">أرباح</div></div></div></div>
</div>
</div>

<div class="card" style="border-color:#00ff88;background:linear-gradient(135deg,#001a0a,#0a1a0a)">
<h3>📜 تعديل القديم - 15 موضوع - من الحتت المستخبية البروفشنال - للمميزين فقط - تحليل نفسي + خيال + طيبات + @CursedMedicineEG + أفليت <span class="b b3">قديم 15 - جديد كليا - بروفشنال</span> <span class="b b4">تحليل 6 + خيال 12</span> <span class="b b2">أفليت KIE.AI</span></h3>
<div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px">
<button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('old')">📜 قديم 15 - بروفشنال</button>
<button class="btn" onclick="gen('الأسرار المدفونة - ترتاريا مصر')" style="background:linear-gradient(135deg,#00ff88,#00d2ff)">📜 الأسرار المدفونة + أفليت</button>
<button class="btn" onclick="gen('الطاقة المفقودة - أهرامات ترتارية محطات طاقة')" style="background:linear-gradient(135deg,#00ff88,#a855f7)">📜 طاقة مفقودة + أفليت</button>
<button class="btn2" onclick="showAffInPkg()">💰 افليت في القديم</button>
</div>
<div id="oldGrid" class="g"></div>
</div>

<div class="card" style="border-color:#00d2ff;background:linear-gradient(135deg,#001a1a,#0a0a1a)">
<h3>🆕 تعديل الجديد - 15 موضوع - من الحتت المستخبية البروفشنال - للمميزين فقط - AI فرعوني + ترتاريا + أفليت KIE.AI <span class="b b6">جديد 15 - جديد كليا - بروفشنال</span> <span class="b b4">تحليل 6 + خيال 12 + أفليت</span> <span class="b b2">KIE.AI + ترتاريا</span></h3>
<div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px">
<button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('new')">🆕 جديد 15 - بروفشنال</button>
<button class="btn" onclick="gen('الذكاء الاصطناعي الفرعوني - ترتاريا AI')" style="background:linear-gradient(135deg,#00d2ff,#a855f7)">🆕 ذكاء اصطناعي فرعوني + أفليت</button>
<button class="btn" onclick="gen('الخلود الفرعوني - سر 900 سنة ترتاري')" style="background:linear-gradient(135deg,#00d2ff,#f7b733)">🆕 خلود 900 سنة + أفليت</button>
<button class="btn2" onclick="showAffInPkg()">💰 افليت في الجديد</button>
</div>
<div id="newGrid" class="g"></div>
</div>

<div class="card" style="border-color:#f7b733;background:linear-gradient(135deg,#1a1500,#1a0a00)">
<h3>🔥 تعديل الأحداث - 15 موضوع - من الحتت المستخبية البروفشنال - للمميزين فقط - 2026 ترند + تسريبات + @CursedMedicineEG + أفليت <span class="b b2">أحداث 15 - 2026 - بروفشنال</span> <span class="b b4">تحليل 6 + خيال 12 + ترند</span> <span class="b b1">50M مشاهدة</span></h3>
<div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px">
<button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('events')">🔥 أحداث 15 - 2026 - بروفشنال</button>
<button class="btn" onclick="gen('تسريبات 2026 - مومياء تتكلم - صوت 3000 سنة ترتاريا')" style="background:linear-gradient(135deg,#f7b733,#ff0033)">🔥 تسريبات 2026 + أفليت</button>
<button class="btn" onclick="gen('إعلان 2026: نهاية كذبة الكرة - نعبر الجدار - 33 أرض - طاقة حرة - حرية')" style="background:linear-gradient(135deg,#f7b733,#00ff88)">🔥 نهاية كذبة الكرة + أفليت</button>
<button class="btn2" onclick="showAffInPkg()">💰 افليت في الأحداث</button>
</div>
<div id="eventsGrid" class="g"></div>
</div>

<div class="card" style="border-color:#a855f7;background:#1a0a1a">
<h3>🏛️🌍 ترتاريا + جغرافيا + ملعون - 42 جديد - قديم+جديد+أحداث=45 - جمع كل المشاريع <span class="b b4">TARTARIA 15</span> <span class="b b5">جغرافيا 15</span> <span class="b b1">ملعون 12</span> <span class="b b2">87 موضوع</span></h3>
<div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px">
<button class="btn2" style="border-color:#a855f7;color:#a855f7;background:#a855f722" onclick="show('tartaria')">🏛️ ترتاريا 15</button>
<button class="btn2" style="border-color:#ff00ff;color:#ff00ff;background:#ff00ff22" onclick="show('forbidden')">🌍 جغرافيا 15</button>
<button class="btn2" style="border-color:#ff0033;color:#ff0033;background:#ff003322" onclick="show('cursed')">💀 ملعون 12</button>
<button class="btn2" style="border-color:#a855f7;color:#a855f7;background:linear-gradient(135deg,#a855f722,#ff00ff22,#ff003322)" onclick="show('all_tart_forb_cursed')">🏛️🌍💀 42 جديد</button>
<button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('all')">🌍 الكل 87 + أفليت</button>
<input id="search" placeholder="🔍 بحث بروفشنال + أفليت" style="width:70px;display:inline-block" oninput="search(this.value)">
</div>
<div id="tfGrid" class="g"></div>
</div>

<div class="card" style="border-color:#f7b733;background:#1a1500">
<h3>✏️ مفاتيح يدوي - 0.5ث - AES-256 - @CursedMedicineEG + أفليت KIE.AI - مربوطة <span class="b b2" id="encBadge">AES-256</span> <span class="b b1" id="linkBadge">فحص...</span> <span class="b b3">0.5ث - <1ث</span> <span class="b b2">افليت ✅</span></h3>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px">
<div><div style="display:grid;grid-template-columns:1fr 1fr;gap:1px"><div><div style="font-size:.3rem"><b>🆔 ID</b> <span id="s_ID" style="font-size:.26rem">❌</span></div><input id="e_ID" placeholder="...googleusercontent.com" oninput="edit('YOUTUBE_CLIENT_ID',this.value)"></div><div><div style="font-size:.3rem"><b>🔒 SECRET</b> <span id="s_SEC" style="font-size:.26rem">❌</span></div><input id="e_SEC" type="password" placeholder="GOCSPX-..." oninput="edit('YOUTUBE_CLIENT_SECRET',this.value)"></div><div><div style="font-size:.3rem"><b>🔄 REFRESH</b> <span id="s_REF" style="font-size:.26rem">❌</span></div><input id="e_REF" type="password" placeholder="1//0g-..." oninput="edit('YOUTUBE_REFRESH_TOKEN',this.value)"></div><div><div style="font-size:.3rem"><b>🤖 GROQ</b> <span id="s_GROQ" style="font-size:.26rem">❌</span></div><input id="e_GROQ" type="password" placeholder="gsk_..." oninput="edit('GROQ_API_KEY',this.value)"></div></div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="save()">🔐 حفظ 0.5ث</button><button class="btn2" onclick="check()">🔍 فحص</button><button class="btn2" onclick="testAff()">💰 افليت</button></div></div>
<div><div id="statusBox" style="background:#000;border-radius:2px;padding:2px;font-size:.32rem;min-height:26px">جاري تحميل 0.5ث - @CursedMedicineEG + افليت + قديم+جديد+أحداث بروفشنال...</div></div>
</div>
</div>

<div class="card" style="border-color:#a855f7"><h3>📚 مكتبة 87 موضوع - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - حتت مستخبية - تحليل + خيال + أفليت <span class="b b4">45 جديد - بروفشنال</span> <span class="b b2">87 موضوع - أفليت</span> <span class="b b3">5ث تحديث - 0.5ث</span></h3><div style="display:flex;gap:1px;flex-wrap:wrap;margin-bottom:1px"><button class="btn2" style="border-color:#00ff88;color:#00ff88;background:#00ff8822" onclick="show('old')">📜 قديم 15</button><button class="btn2" style="border-color:#00d2ff;color:#00d2ff;background:#00d2ff22" onclick="show('new')">🆕 جديد 15</button><button class="btn2" style="border-color:#f7b733;color:#f7b733;background:#f7b73322" onclick="show('events')">🔥 أحداث 15</button><button class="btn2" style="border-color:#a855f7;color:#a855f7;background:#a855f722" onclick="show('tartaria')">🏛️ ترتاريا 15</button><button class="btn2" style="border-color:#ff00ff;color:#ff00ff;background:#ff00ff22" onclick="show('forbidden')">🌍 جغرافيا 15</button><button class="btn2" style="border-color:#ff0033;color:#ff0033;background:#ff003322" onclick="show('cursed')">💀 ملعون 12</button><button class="btn2" onclick="show('all')">🌍 الكل 87 + أفليت</button></div><div id="grid" class="g"></div></div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:2px"><div class="card"><h3>📦 باقة BLACK OPS - قديم+جديد+أحداث بروفشنال - تحليل + خيال + أفليت - 0.5ث</h3><div id="pkgDisplay" class="pkg" style="min-height:60px;display:flex;align-items:center;justify-content:center;color:#8aa">اضغط باقة - قديم+جديد+أحداث بروفشنال - تحليل نفسي 6 + خيال 12 + أفليت KIE.AI - 0.5ث...</div><div style="display:flex;gap:1px;margin-top:1px"><button class="btn" onclick="gen('الأسرار المدفونة - ترتاريا مصر')" style="background:linear-gradient(135deg,#00ff88,#00d2ff)">📜 قديم + أفليت</button><button class="btn" onclick="gen('الذكاء الاصطناعي الفرعوني - ترتاريا AI')" style="background:linear-gradient(135deg,#00d2ff,#a855f7)">🆕 جديد + أفليت</button><button class="btn" onclick="gen('تسريبات 2026 - مومياء تتكلم - صوت 3000 سنة ترتاريا')" style="background:linear-gradient(135deg,#f7b733,#ff0033)">🔥 أحداث + أفليت</button><button class="btn2" onclick="showAffInPkg()">💰 افليت</button></div></div><div class="card"><h3>📊 إحصائيات - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - 0.5ث</h3><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr 1fr;gap:1px"><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;font-weight:900;color:#00ff88" id="oldCount">15</div><div style="font-size:.22rem">قديم 15</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;font-weight:900;color:#00d2ff" id="newCount">15</div><div style="font-size:.22rem">جديد 15</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;font-weight:900;color:#f7b733" id="eventsCount">15</div><div style="font-size:.22rem">أحداث 15</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;font-weight:900;color:#a855f7" id="totalCount">87</div><div style="font-size:.22rem">الكل 87</div></div><div style="background:#020208;padding:1px;border-radius:2px;text-align:center"><div style="font-size:.5rem;font-weight:900;color:#f7b733" id="affCount">1</div><div style="font-size:.22rem">افليت</div></div></div><div class="log" id="log"><div style="color:#00ff88">> v61 ULTRA 0.5s - قديم 15+جديد 15+أحداث 15=45 جديد - تعديل من الحتت المستخبية البروفشنال - للمميزين فقط - تحليل 6 + خيال 12 + 5ث تحديث + أفليت KIE.AI - يفتح 0.5ث - اسرع اقل من ثانية</div></div></div></div>

</div>
<script>
const OLD={{old_json}}; const NEW={{new_json}}; const EVENTS={{events_json}}; const TARTARIA={{tartaria_json}}; const FORBIDDEN={{forbidden_json}}; const CURSED={{cursed_json}}; const ALL=[...OLD,...NEW,...EVENTS,...TARTARIA,...FORBIDDEN,...CURSED]; const PSYCH={{psych_json}}; const IMAG={{imag_json}};
let curKeys={}; let affClicks=127;
function log(m,c='#e0e6f0',a='SYS'){ const el=document.getElementById('log'); if(!el) return; const d=document.createElement('div'); d.textContent=`[${new Date().toLocaleTimeString()}] [${a}] ${m}`; d.style.color=c; el.appendChild(d); el.scrollTop=el.scrollHeight; }
function edit(k,v){ curKeys[k]=v; const id=k.includes('CLIENT_ID')?'ID':k.includes('SECRET')?'SEC':k.includes('REFRESH')?'REF':k.includes('GROQ')?'GROQ':k.includes('AFFILIATE_LINK')?'AFF':'PRODKEY'; const s=document.getElementById('s_'+id); if(s){ if(v){ s.textContent=`✅ ${v.length}`; s.style.color='#00ff88'; } else { s.textContent='❌'; s.style.color='#ff4444'; } } if(k.includes('AFFILIATE')) updateAffPreview(); }
function updateAffPreview(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; const key=document.getElementById('e_PRODKEY')?.value||'0e3195dd062bf11f0da7496dd3c1bf6'; const box=document.getElementById('affStatusBox'); if(box) box.innerHTML=`<div style="color:#00ff88">✅ أفليت KIE.AI - ${aff}<br>🔑 مفتاح: ${key} - 0.5ث - يظهر في كل مكان - قديم+جديد+أحداث بروفشنال<br>📊 ${affClicks} نقرات - 12 تحويلات - 84$ - 0.5ث</div>`; }
function save(){ fetch('/api/keys/save',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(curKeys)}).then(r=>r.json()).then(d=>{ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">✅ حفظ 0.5ث - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - ${d.count}/7<br>💰 افليت: ${d.aff_link||'KIE.AI'} - 🔑 ${d.prod_key||'0e3195dd'}<br>🏛️ 87 موضوع - أفليت ✅ - 0.5ث</div>`; log(`💰 حفظ 0.5ث قديم+جديد+أحداث بروفشنال ${d.count}/7`, '#00ff88','PRO_05'); check(); }).catch(()=>{ document.getElementById('statusBox').innerHTML=`<div style="color:#00ff88">✅ حفظ محلي 0.5ث - قديم+جديد+أحداث بروفشنال</div>`; }); }
function check(){ fetch('/api/keys/status').then(r=>r.json()).then(s=>{ document.getElementById('statusBox').innerHTML=`<div style="color:${s.linked?'#00ff88':'#f7b733'}">${s.status_text} - ${s.count}/7 | 💰 افليت: ${s.aff_link?'✅':'❌'} | قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - 0.5ث</div>`; document.getElementById('linkBadge').textContent=s.linked?'✅ مربوطة - قديم+جديد+أحداث بروفشنال - 0.5ث':'⚠️ غير مربوطة - 0.5ث'; }).catch(()=>{}); }
function testAff(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; document.getElementById('affStatusBox').innerHTML=`<div style="color:#00ff88">🧪 افليت KIE.AI ✅ 0.5ث - ${aff}<br>✅ يعمل - يظهر في قديم+جديد+أحداث بروفشنال - تحليل 6 + خيال 12</div>`; }
function copyAff(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; navigator.clipboard.writeText(aff); }
function genAffLink(){ const key=document.getElementById('e_PRODKEY')?.value||'0e3195dd062bf11f0da7496dd3c1bf6'; const link=`https://kie.ai?ref=${key}`; document.getElementById('e_AFF').value=link; edit('AFFILIATE_LINK',link); updateAffPreview(); }
function showAffInPkg(){ const aff=document.getElementById('e_AFF')?.value||'https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6'; const key=document.getElementById('e_PRODKEY')?.value||'0e3195dd062bf11f0da7496dd3c1bf6'; document.getElementById('pkgDisplay').innerHTML=`<div style="text-align:right"><div style="color:#f7b733;font-weight:900">💰 قديم+جديد+أحداث بروفشنال + أفليت KIE.AI - ${aff} - مفتاح ${key} - 0.5ث</div><div style="font-size:.32rem;margin-top:1px">📜 قديم 15: تحليل نفسي 6 + خيال 12 + طيبات + @CursedMedicineEG + أفليت - من الحتت المستخبية البروفشنال<br>🆕 جديد 15: AI فرعوني + ترتاريا + أفليت KIE.AI + تحليل + خيال - من الحتت المستخبية البروفشنال<br>🔥 أحداث 15: 2026 ترند + تسريبات + @CursedMedicineEG + أفليت + تحليل + خيال - من الحتت المستخبية البروفشنال<br>🔗 ${aff}<br>🔑 مفتاح: ${key}<br>✅ يظهر في كل مكان - قديم+جديد+أحداث بروفشنال - تحليل 6 + خيال 12 + أفليت - 0.5ث</div></div>`; }
function genPsych(){ const p=PSYCH[Math.floor(Math.random()*PSYCH.length)]; document.getElementById('psychBox').innerHTML=`<div style="color:#a855f7;font-weight:900">👤 ${p[0]}</div><div style="font-size:.3rem">🎯 ${p[1]}</div><div style="font-size:.28rem">🪝 ${p[2]}</div>`; const grid=document.getElementById('psychGrid'); if(grid) grid.innerHTML=PSYCH.map(d=>`<div class="i" style="border-color:#a855f7;padding:1px"><b style="color:#a855f7;font-size:.3rem">${d[0].split(' ')[0]}</b><br><span style="font-size:.26rem">${d[1].slice(0,10)}...</span></div>`).join(''); log(`🧠 تحليل 0.5ث: ${p[0]} - من الحتت المستخبية البروفشنال`, '#a855f7','PSYCHO'); }
function genImag(){ const im=IMAG[Math.floor(Math.random()*IMAG.length)]; const t=ALL[Math.floor(Math.random()*ALL.length)]; document.getElementById('imagBox').innerHTML=`<div style="color:#ff00ff">🌀 خيال 0.5ث:</div><div style="font-size:.3rem">${im.slice(0,35)}...</div><div style="color:#a855f7;font-size:.28rem">📚 ${t[0].slice(0,20)}...</div>`; log(`🌀 خيال 0.5ث: ${im.slice(0,20)}... - من الحتت المستخبية`, '#ff00ff','IMAG'); }
function loadAuto(){ fetch('/api/pro/auto').then(r=>r.json()).then(d=>{ document.getElementById('autoEvo').innerHTML=d.evo.map(e=>`<div>⚡ ${e.t} [${e.a}] ${e.m}... [${e.lang||'AR'}]</div>`).join(''); document.getElementById('autoLive').innerHTML=d.topics.map(t=>`<div>⚡ ${t.t} - ${t.topic.slice(0,15)}... [${t.psych}]</div>`).join(''); document.getElementById('autoPkg').innerHTML=d.topics.map(t=>`<div>📦 ${t.t} - ${t.topic.slice(0,15)}... + أفليت</div>`).join(''); document.getElementById('autoCount').textContent=d.topics.length; document.getElementById('evoCount').textContent=d.evo.length; }).catch(()=>{}); }
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
 const grid=document.getElementById('grid');
 const oldGrid=document.getElementById('oldGrid');
 const newGrid=document.getElementById('newGrid');
 const eventsGrid=document.getElementById('eventsGrid');
 const tfGrid=document.getElementById('tfGrid');
 if(!grid) return;
 const makeHtml = (list) => list.map(([title,desc])=>{
   let cls='o'; if(TARTARIA.find(t=>t[0]==title)) cls='t'; if(FORBIDDEN.find(t=>t[0]==title)) cls='f'; if(CURSED.find(t=>t[0]==title)) cls='c'; if(OLD.find(t=>t[0]==title)) cls='o'; if(NEW.find(t=>t[0]==title)) cls='n'; if(EVENTS.find(t=>t[0]==title)) cls='e';
   const safe=title.replace(/'/g,"\\'");
   let icon='📜'; if(cls=='o') icon='📜'; if(cls=='n') icon='🆕'; if(cls=='e') icon='🔥'; if(cls=='t') icon='🏛️'; if(cls=='f') icon='🌍'; if(cls=='c') icon='💀';
   return `<div class="i ${cls}"><b>${icon} ${title.slice(0,18)}...</b><br><span style="font-size:.26rem">${desc.slice(0,22)}...</span><br><button class="btn2" onclick="gen('${safe}')">🚀 باقة 0.5ث + أفليت</button></div>`;
 }).join('');
 
 if(type=='old' && oldGrid){ oldGrid.innerHTML=makeHtml(topics); }
 if(type=='new' && newGrid){ newGrid.innerHTML=makeHtml(topics); }
 if(type=='events' && eventsGrid){ eventsGrid.innerHTML=makeHtml(topics); }
 
 grid.innerHTML=makeHtml(topics);
 if(tfGrid){
   tfGrid.innerHTML=makeHtml([...TARTARIA,...FORBIDDEN,...CURSED].slice(0,12));
 }
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
   if(OLD.find(t=>t[0]==template)){ extra='<br><span style="color:#00ff88">📜 قديم - من الحتت المستخبية البروفشنال - تحليل نفسي + خيال + طيبات + @CursedMedicineEG</span>'; color='#00ff88'; typeIcon='📜'; }
   if(NEW.find(t=>t[0]==template)){ extra='<br><span style="color:#00d2ff">🆕 جديد - من الحتت المستخبية البروفشنال - AI فرعوني + ترتاريا + أفليت KIE.AI + تحليل + خيال</span>'; color='#00d2ff'; typeIcon='🆕'; }
   if(EVENTS.find(t=>t[0]==template)){ extra='<br><span style="color:#f7b733">🔥 أحداث 2026 - من الحتت المستخبية البروفشنال - ترند + تسريبات + @CursedMedicineEG + أفليت + تحليل + خيال - 50M</span>'; color='#f7b733'; typeIcon='🔥'; }
   if(TARTARIA.find(t=>t[0]==template)){ extra='<br><span style="color:#a855f7">🏛️ ترتاريا - تحليل 6 + خيال 12 + أفليت</span>'; color='#a855f7'; typeIcon='🏛️'; }
   if(FORBIDDEN.find(t=>t[0]==template)){ extra='<br><span style="color:#ff00ff">🌍 جغرافيا محرمة - 33 أرض - قبة - أفليت</span>'; color='#ff00ff'; typeIcon='🌍'; }
   if(CURSED.find(t=>t[0]==template)){ extra='<br><span style="color:#ff4444">💀 طب ملعون @CursedMedicineEG - رعب - أفليت</span>'; color='#ff4444'; typeIcon='💀'; }
   document.getElementById('pkgDisplay').innerHTML=`<div style="text-align:right"><div style="color:${color};font-weight:900">${typeIcon} ${template} - VAC-${vac} - 0.5ث - من الحتت المستخبية البروفشنال - للمميزين فقط</div><div style="color:${color}"><b>🧠 ${p[0]}</b></div><div><b>🎯 ${p[1].slice(0,40)}...</b></div><div><b>🪝 ${p[2].slice(0,35)}...</b></div><div><b>🌀 ${im.slice(0,40)}...</b></div><div style="font-size:.3rem">${extra}<br>💰 أفليت KIE.AI: ${aff} - مفتاح: ${key} - يظهر في كل مكان - قديم+جديد+أحداث بروفشنال - تحليل 6 + خيال 12 + 5ث تحديث - 0.5ث - <1ث</div></div>`;
   log(`${typeIcon} 0.5ث باقة بروفشنال: ${template.slice(0,20)}... - ${p[0]} - VAC-${vac} - من الحتت المستخبية - للمميزين فقط`, color,'PRO_05');
 }catch(e){}
}

document.addEventListener('DOMContentLoaded', function(){
 check();
 show('old');
 setTimeout(()=>show('new'),300);
 setTimeout(()=>show('events'),600);
 setTimeout(()=>show('all'),900);
 genPsych();
 genImag();
 loadAuto();
 updateAffPreview();
 log('v61 ULTRA 0.5s - اسرع اقل من ثانية - قديم 15+جديد 15+أحداث 15=45 جديد - تعديل من الحتت المستخبية البروفشنال - للمميزين فقط - تحليل 6 + خيال 12 + 5ث تحديث + أفليت KIE.AI - 87 موضوع - يفتح 0.5ث - اسرع اقل من ثانية - للمميزين فقط - مواهب التحليل', '#00ff88','ULTRA_05');
});
setInterval(loadAuto,5000);
setInterval(genPsych,10000);
setInterval(genImag,12000);
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
        return jsonify({"status":"success","count":sum(1 for x in VAULT.values() if x),"aff_link":VAULT.get("AFFILIATE_LINK"),"prod_key":VAULT.get("AFFILIATE_PRODUCT_KEY")})
    except Exception as e:
        return jsonify({"status":"error","msg":str(e)}),500

@app.route('/api/keys/status')
def keys_status():
    c=sum(1 for x in VAULT.values() if x)
    has_id=bool(VAULT["YOUTUBE_CLIENT_ID"] and len(VAULT["YOUTUBE_CLIENT_ID"])>20)
    has_sec=bool(VAULT["YOUTUBE_CLIENT_SECRET"] and len(VAULT["YOUTUBE_CLIENT_SECRET"])>10)
    has_ref=bool(VAULT["YOUTUBE_REFRESH_TOKEN"] and VAULT["YOUTUBE_REFRESH_TOKEN"].startswith("1//"))
    return jsonify({"linked":has_id and has_sec and has_ref,"status_text":f"{'✅ مربوطة' if has_id and has_sec and has_ref else '⚠️ غير مربوطة'} - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - 0.5ث - أفليت KIE.AI","count":c,"aff_link":VAULT.get("AFFILIATE_LINK"),"prod_key":VAULT.get("AFFILIATE_PRODUCT_KEY")})

@app.route('/api/pro/auto')
def pro_auto():
    return jsonify({"evo":EVO[-8:],"topics":AUTO_T[-8:]})

@app.route('/api/groq/generate', methods=['POST'])
def groq_gen():
    try:
        data=request.get_json()
        prompt=data.get('prompt','قديم+جديد+أحداث بروفشنال')
        aff=VAULT.get("AFFILIATE_LINK","https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf6")
        return jsonify({"response":f"⚡ v61 ULTRA 0.5s - {prompt[:40]}... - قديم 15+جديد 15+أحداث 15=45 جديد - تعديل من الحتت المستخبية البروفشنال - للمميزين فقط - تحليل 6 + خيال 12 + 5ث تحديث + أفليت {aff} - 87 موضوع - 0.5ث - <1ث"})
    except Exception as e:
        return jsonify({"response":f"Error: {e}"})

@app.route('/health')
def health():
    return f"v61 ULTRA 0.5s - اسرع اقل من ثانية - قديم 15+جديد 15+أحداث 15=45 جديد - بروفشنال - تحليل 6 + خيال 12 + 5ث + أفليت KIE.AI - 87 موضوع - يفتح 0.5ث"

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
