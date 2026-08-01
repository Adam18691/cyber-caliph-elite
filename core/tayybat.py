# FILE: core/tayybat.py - v115 FIX - حل مشكلة LINKS is not defined
FORBIDDEN_TEXT="بيض ممنوع - 11 ممنوع - بيض ممنوع - طيبات الدكتور ضياء العوضي"
FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]

TAYYBAT_TOPICS=[
    ["طيبات الدكتور ضياء العوضي - بدون بيض - 11 ممنوع - بيض ممنوع - طيبات","طيبات الدكتور ضياء العوضي"],
    ["ارز - بطاطس - قشطة - فواكه - بدون بيض - المسموحات","المسموحات - طيبات - بدون بيض"],
    ["دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - 11 ممنوع","ال 11 ممنوع - طيبات"],
]

LINKS_6={
    "monoprice":"https://yazing.com/deals/monoprice/Waeldeban186",
    "landsend":"https://yazing.com/deals/landsend/Waeldeban186",
    "shopsimon":"https://yazing.com/deals/shopsimon/Waeldeban186",
    "colehaan":"https://yazing.com/deals/colehaan/Waeldeban186",
    "hfonline":"https://yazing.com/deals/hfonline-uk/Waeldeban186",
    "kieai":"https://kie.ai/?ref=0e3195d062bf11f0da7496d3c1bf66"
}
# FIX للاسم القديم
LINKS = LINKS_6

VIDEO_DESCRIPTION = """طيبات الدكتور ضياء العوضي - نظام الطيبات - 11 ممنوع - بيض ممنوع

ال 11 ممنوع: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة - بيض

المسموحات: ارز - بطاطس - لحوم - اسماك - قشطة - فواكه

روابط المنتجات (6 لينكات):

1 - Monoprice: https://yazing.com/deals/monoprice/Waeldeban186
2 - LandsEnd: https://yazing.com/deals/landsend/Waeldeban186
3 - ShopSimon: https://yazing.com/deals/shopsimon/Waeldeban186
4 - ColeHaan: https://yazing.com/deals/colehaan/Waeldeban186
5 - HFOnline: https://yazing.com/deals/hfonline-uk/Waeldeban186
6 - KieAI: https://kie.ai/?ref=0e3195d062bf11f0da7496d3c1bf66

#طيبات #ضياء_العوضي #نظام_الطيبات #بدون_بيض
"""

def get_links_6():
    return LINKS_6

def get_video_description_with_links():
    return VIDEO_DESCRIPTION

def get_tayybat_info():
    # FIX: كان هنا LINKS وده اللي كان عامل NameError
    return {
        "topics": TAYYBAT_TOPICS,
        "forbidden": FORBIDDEN_TEXT,
        "forbidden_items": FORBIDDEN_ITEMS,
        "forbidden_count": 11,
        "no_eggs": True,
        "eggs_forbidden": True,
        "links": LINKS_6,
        "LINKS_6": LINKS_6,
        "video_description": VIDEO_DESCRIPTION,
        "total_product_time": "6 لينكات 6 لينكات",
        "tayybat": True,
        "single_topic": True
    }
