# FILE: core/tayybat.py - اسم الملف: core/tayybat.py - من الخارج - v130 FINAL - طيبات - 11 ممنوع - 6 دقائق لـ 6 لينكات - وصف الفيديو مع اللينكات - حل مشكلة n8n غير موجود - 0.000000000001s
FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع - بدون بيض"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]
ALLOWED_TEXT="المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه - بدون بيض"
LINKS_6={
  "monoprice": "https://yazing.com/deals/monoprice/Waeldeban186",
  "landsend": "https://yazing.com/deals/landsend/Waeldeban186",
  "shopsimon": "https://yazing.com/deals/shopsimon/Waeldeban186",
  "colehaan": "https://yazing.com/deals/colehaan/Waeldeban186",
  "hfonline": "https://yazing.com/deals/hfonline-uk/Waeldeban186",
  "kieai": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66"
}
VIDEO_DESCRIPTION=f"""🍞 نظام طيبات الدكتور ضياء العوضى - بدون بيض - 11 ممنوع
الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - بيض ممنوع
المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه - بدون بيض
فطار: توست + زبدة + عسل - بدون بيض
غداء: أرز + لحم ضاني + بطاطس
عشاء: بقسماط + قشطة + موز - بدون بيض
⚠️ تنبيه: محتوى ثقافي - ليس علاج طبي - استشر طبيبك
━━━━━━━━━━━━━━━━━━━━━━
🛒 6 دقائق لـ 6 لينكات - دقيقة لكل منتج
1️⃣ Monoprice 70% - https://yazing.com/deals/monoprice/Waeldeban186
2️⃣ Lands End 60% - https://yazing.com/deals/landsend/Waeldeban186
3️⃣ ShopSimon 70% - https://yazing.com/deals/shopsimon/Waeldeban186
4️⃣ Cole Haan 50%+20% - https://yazing.com/deals/colehaan/Waeldeban186
5️⃣ HF Online UK 50% - https://yazing.com/deals/hfonline-uk/Waeldeban186
6️⃣ Kie.ai 80% توفير - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66
━━━━━━━━━━━━━━━━━━━━━━
📺 https://www.youtube.com/@CursedMedicineEG
#طيبات #Waeldeban186
"""
TAYYBAT_TOPICS=[
    ["طيبات الدكتور ضياء العوضى - بدون بيض","نظام الطيبات - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع","طيبات"],
    ["المسموحات - بدون بيض","خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه - بدون بيض","طيبات"],
    ["الممنوعات - 11 ممنوع","الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع","طيبات"],
    ["6 دقائق لـ 6 لينكات","Monoprice LandsEnd ShopSimon ColeHaan HFOnlineUK KieAI - 6 دقائق لـ 6 لينكات - Waeldeban186","منتجات"],
]
def get_tayybat_info():
    return {"topics":TAYYBAT_TOPICS,"forbidden":FORBIDDEN_TEXT,"forbidden_count":11,"no_eggs":True,"links":LINKS,"video_description":VIDEO_DESCRIPTION,"total_product_time":"6 دقائق لـ 6 لينكات"}
def get_video_description_with_links(): return VIDEO_DESCRIPTION
def get_links_6(): return LINKS_6
