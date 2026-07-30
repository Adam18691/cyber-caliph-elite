# FILE: config/settings.py - اسم الملف: config/settings.py - v98 PROFESSIONAL - <400 سطر - احترافي مقسم - اسم الملف على الملف - FIXED
"""v97 PROFESSIONAL - config/settings.py - <100 lines - اعدادات المشروع"""
import os
E = os.environ.get

class Settings:
    YOUTUBE_CLIENT_ID = E('YOUTUBE_CLIENT_ID','')
    YOUTUBE_CLIENT_SECRET = E('YOUTUBE_CLIENT_SECRET','')
    YOUTUBE_REFRESH_TOKEN = E('YOUTUBE_REFRESH_TOKEN','')
    GROQ_API_KEY = E('GROQ_API_KEY','')
    YOUTUBE_API_KEY = E('YOUTUBE_API_KEY','')
    CHANNEL_HANDLE = "CursedMedicineEG"
    CHANNEL_URL = "https://www.youtube.com/@CursedMedicineEG"
    AFFILIATE_LINK = "https://yazing.com/deals/monoprice/Waeldeban186"
    AFFILIATE_CODE = "Waeldeban186"

    TOPICS = [
        ["ترتاريا العظمى المخفية","امبراطورية نصف العالم محوها 1776"],
        ["تكنولوجيا ترتاريا طاقة حرة","الاثير الكاتدرائيات محطات طاقة"],
        ["Mud Flood","1800s دفن ترتاريا 3م طين"],
        ["عمارة ترتاريا","قباب ذهبية اجراس 432 هرتز"],
        ["الجغرافيا المحرمة","مسطحة ممدودة سقف محفوظ"],
        ["ما وراء الجدار الجليدي","جدار 50-100م يحيط يمنع 33 ارض"],
        ["33 ارض","33 ارض كل ارض بحجم قارتنا"],
        ["القبة السماوية","سقف محفوظ صلب"],
    ]

    COUNTRIES = [
        {"flag":"🇨🇭","name":"سويسرا","langs":"ألماني/فرنسي/إيطالي"},
        {"flag":"🇩🇰","name":"الدنمارك","langs":"دنماركي"},
        {"flag":"🇸🇪","name":"السويد","langs":"سويدي"},
        {"flag":"🇫🇷","name":"فرنسا","langs":"فرنسي"},
        {"flag":"🇩🇪","name":"ألمانيا","langs":"ألماني"},
        {"flag":"🇬🇧","name":"المملكة المتحدة","langs":"إنجليزي"},
        {"flag":"🇳🇴","name":"النرويج","langs":"نرويجي"},
        {"flag":"🇺🇸","name":"الولايات المتحدة","langs":"إنجليزي"},
        {"flag":"🇧🇪","name":"بلجيكا","langs":"هولندي/فرنسي"},
        {"flag":"🇮🇪","name":"أيرلندا","langs":"إنجليزي"},
        {"flag":"🇮🇹","name":"إيطاليا","langs":"إيطالي"},
        {"flag":"🇳🇱","name":"هولندا","langs":"هولندي"},
        {"flag":"🇦🇺","name":"أستراليا","langs":"إنجليزي"},
        {"flag":"🇿🇼","name":"زيمبابوي","langs":"إنجليزي"},
        {"flag":"🇫🇰","name":"جزر فوكلاند","langs":"إنجليزي"},
        {"flag":"🇸🇭","name":"سانت هيلينا","langs":"إنجليزي"},
        {"flag":"🇸🇸","name":"جنوب السودان","langs":"إنجليزي"},
        {"flag":"🇼🇸","name":"ساموا","langs":"ساموا/إنجليزي"},
        {"flag":"🇨🇦","name":"كندا","langs":"إنجليزي/فرنسي"},
    ]

    LANGS_FINAL = [
        {"code":"de","name":"ألماني","flag":"🇩🇪🇨🇭"},
        {"code":"fr","name":"فرنسي","flag":"🇫🇷🇨🇭🇧🇪🇨🇦"},
        {"code":"it","name":"إيطالي","flag":"🇮🇹🇨🇭"},
        {"code":"da","name":"دنماركي","flag":"🇩🇰"},
        {"code":"sv","name":"سويدي","flag":"🇸🇪"},
        {"code":"en","name":"إنجليزي - 10 دول","flag":"🇬🇧🇺🇸🇮🇪🇦🇺"},
        {"code":"no","name":"نرويجي","flag":"🇳🇴"},
        {"code":"nl","name":"هولندي","flag":"🇳🇱🇧🇪"},
        {"code":"sm","name":"ساموا","flag":"🇼🇸"},
        {"code":"ar","name":"عربي","flag":"🇪🇬"},
    ]

settings = Settings()
