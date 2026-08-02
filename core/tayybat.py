
# FILE: core/tayybat.py - v134 FINAL - كل لينك دقيقة ×6=6 دقايق - 30/45/60 دقيقة
FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع - بيض ممنوع - بدون بيض"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]

LINKS_6={
    "monoprice": {"url":"https://yazing.com/deals/monoprice/Waeldeban186","discount":"70%","name":"Monoprice"},
    "landsend": {"url":"https://yazing.com/deals/landsend/Waeldeban186","discount":"60%","name":"Lands End"},
    "shopsimon": {"url":"https://yazing.com/deals/shopsimon/Waeldeban186","discount":"70%","name":"ShopSimon"},
    "colehaan": {"url":"https://yazing.com/deals/colehaan/Waeldeban186","discount":"50%+20%","name":"Cole Haan"},
    "hfonline": {"url":"https://yazing.com/deals/hfonline-uk/Waeldeban186","discount":"50%","name":"HF Online UK"},
    "kieai": {"url":"https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66","discount":"80% توفير","name":"Kie.AI"}
}
LINKS = LINKS_6
LINKS_6_SIMPLE={k:v["url"] for k,v in LINKS_6.items()}

VIDEO_DESCRIPTION="""🍞 نظام طيبات الدكتور ضياء العوضى - بدون بيض - 11 ممنوع
الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - بيض ممنوع
المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه - بدون بيض
فطار: توست + زبدة + عسل - بدون بيض
غداء: أرز + لحم ضاني + بطاطس
عشاء: بقسماط + قشطة + موز - بدون بيض
⚠️ تنبيه: محتوى ثقافي - ليس علاج طبي - استشر طبيبك
━━━━━━━━━━━━━━━━━━━━━━
🛒 كل لينك دقيقة ×6=6 دقايق
30 دقيقة = 24 د محتوى + 6 د لينكات
45 دقيقة = 39 د محتوى + 6 د لينكات
60 دقيقة = 54 د محتوى + 6 د لينكات
1️⃣ Monoprice 70% - https://yazing.com/deals/monoprice/Waeldeban186
2️⃣ Lands End 60% - https://yazing.com/deals/landsend/Waeldeban186
3️⃣ ShopSimon 70% - https://yazing.com/deals/shopsimon/Waeldeban186
4️⃣ Cole Haan 50%+20% - https://yazing.com/deals/colehaan/Waeldeban186
5️⃣ HF Online UK 50% - https://yazing.com/deals/hfonline-uk/Waeldeban186
6️⃣ Kie.ai 80% - https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66
📺 https://www.youtube.com/@CursedMedicineEG
#طيبات #Waeldeban186 #1min_x6
"""

def get_links_6(): return LINKS_6
def get_video_description_with_links(): return VIDEO_DESCRIPTION
def get_tayybat_info():
    return {
        "topics":[["طيبات بدون بيض - 11 ممنوع","طيبات"]],
        "forbidden":FORBIDDEN_TEXT,
        "forbidden_items":FORBIDDEN_ITEMS,
        "forbidden_count":11,
        "no_eggs":True,
        "eggs_forbidden":True,
        "links":LINKS_6,
        "links_simple":LINKS_6_SIMPLE,
        "video_description":VIDEO_DESCRIPTION,
        "montage":"كل لينك دقيقة ×6=6 دقايق - 30/45/60 دقيقة",
        "tayybat":True
    }
