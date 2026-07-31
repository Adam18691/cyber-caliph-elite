# FILE: config/settings.py - اسم الملف: config/settings.py - من الخارج - v113 - حذف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى - طيبات الدكتور ضياء العوضى - دمج اداة فلو من جوجل لإنشاء الصور - Flow Google - 21 دولة + ترجمة + صوت + دبلجة + ربط قناتي + التشغيل علي n8n وعدم الربط - 0.000000000001s - ULTRA FASTEST EVER
import os
E=os.environ.get
class Settings:
    YOUTUBE_CLIENT_ID=E('YOUTUBE_CLIENT_ID','')
    YOUTUBE_CLIENT_SECRET=E('YOUTUBE_CLIENT_SECRET','')
    YOUTUBE_REFRESH_TOKEN=E('YOUTUBE_REFRESH_TOKEN','')
    GROQ_API_KEY=E('GROQ_API_KEY','')
    YOUTUBE_API_KEY=E('YOUTUBE_API_KEY','')
    CLAUDE_API_KEY=E('CLAUDE_API_KEY','')
    GOOGLE_API_KEY=E('GOOGLE_API_KEY','')
    GEMINI_API_KEY=E('GEMINI_API_KEY','')
    FLOW_API_KEY=E('FLOW_API_KEY','') or E('GOOGLE_API_KEY','') or E('GEMINI_API_KEY','')
    HANDLE="CursedMedicineEG"
    URL="https://www.youtube.com/@CursedMedicineEG"
    CHANNEL_URL="https://www.youtube.com/@CursedMedicineEG"
    COUNTRIES_21=[
        {"id":0,"flag":"🇪🇬","name":"مصر","lang":"عربي","code":"ar-EG","voice":"ar-EG-Wavenet-A","lang_code":"ar","dub":"ar-EG","translate":"ar","flow_prompt":"Egyptian healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":1,"flag":"🇨🇭","name":"سويسرا","lang":"ألماني/فرنسي/إيطالي","code":"de-CH","voice":"de-CH-Wavenet-A","lang_code":"de","dub":"de-CH","translate":"de","flow_prompt":"Swiss healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":2,"flag":"🇩🇰","name":"الدنمارك","lang":"دنماركي","code":"da-DK","voice":"da-DK-Wavenet-A","lang_code":"da","dub":"da-DK","translate":"da","flow_prompt":"Danish healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":3,"flag":"🇸🇪","name":"السويد","lang":"سويدي","code":"sv-SE","voice":"sv-SE-Wavenet-A","lang_code":"sv","dub":"sv-SE","translate":"sv","flow_prompt":"Swedish healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":4,"flag":"🇫🇷","name":"فرنسا","lang":"فرنسي","code":"fr-FR","voice":"fr-FR-Wavenet-A","lang_code":"fr","dub":"fr-FR","translate":"fr","flow_prompt":"French healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":5,"flag":"🇩🇪","name":"ألمانيا","lang":"ألماني","code":"de-DE","voice":"de-DE-Wavenet-A","lang_code":"de","dub":"de-DE","translate":"de","flow_prompt":"German healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":6,"flag":"🇬🇧","name":"المملكة المتحدة","lang":"إنجليزي بريطاني","code":"en-GB","voice":"en-GB-Wavenet-A","lang_code":"en-GB","dub":"en-GB","translate":"en","flow_prompt":"British healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":7,"flag":"🇳🇴","name":"النرويج","lang":"نرويجي","code":"nb-NO","voice":"nb-NO-Wavenet-A","lang_code":"no","dub":"nb-NO","translate":"no","flow_prompt":"Norwegian healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":8,"flag":"🇺🇸","name":"الولايات المتحدة","lang":"إنجليزي أمريكي","code":"en-US","voice":"en-US-Wavenet-A","lang_code":"en-US","dub":"en-US","translate":"en","flow_prompt":"American healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":9,"flag":"🇧🇪","name":"بلجيكا","lang":"هولندي/فرنسي","code":"nl-BE","voice":"nl-BE-Wavenet-A","lang_code":"nl","dub":"nl-BE","translate":"nl","flow_prompt":"Belgian healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":10,"flag":"🇮🇪","name":"أيرلندا","lang":"إنجليزي أيرلندي","code":"en-IE","voice":"en-IE-Wavenet-A","lang_code":"en-IE","dub":"en-IE","translate":"en","flow_prompt":"Irish healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":11,"flag":"🇮🇹","name":"إيطاليا","lang":"إيطالي","code":"it-IT","voice":"it-IT-Wavenet-A","lang_code":"it","dub":"it-IT","translate":"it","flow_prompt":"Italian healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":12,"flag":"🇳🇱","name":"هولندا","lang":"هولندي","code":"nl-NL","voice":"nl-NL-Wavenet-A","lang_code":"nl","dub":"nl-NL","translate":"nl","flow_prompt":"Dutch healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":13,"flag":"🇦🇺","name":"أستراليا","lang":"إنجليزي أسترالي","code":"en-AU","voice":"en-AU-Wavenet-A","lang_code":"en-AU","dub":"en-AU","translate":"en","flow_prompt":"Australian healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":14,"flag":"🇿🇼","name":"زيمبابوي","lang":"إنجليزي زيمبابوي","code":"en-ZW","voice":"en-ZW-Wavenet-A","lang_code":"en-ZW","dub":"en-ZW","translate":"en","flow_prompt":"Zimbabwe healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":15,"flag":"🇫🇰","name":"جزر فوكلاند","lang":"إنجليزي فوكلاند","code":"en-FK","voice":"en-GB-Wavenet-A","lang_code":"en-FK","dub":"en-FK","translate":"en","flow_prompt":"Falkland healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":16,"flag":"🇸🇭","name":"سانت هيلينا","lang":"إنجليزي سانت هيلينا","code":"en-SH","voice":"en-GB-Wavenet-A","lang_code":"en-SH","dub":"en-SH","translate":"en","flow_prompt":"Saint Helena healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":17,"flag":"🇸🇸","name":"جنوب السودان","lang":"إنجليزي جنوب السودان","code":"en-SS","voice":"en-US-Wavenet-A","lang_code":"en-SS","dub":"en-SS","translate":"en","flow_prompt":"South Sudan healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":18,"flag":"🇼🇸","name":"ساموا","lang":"ساموا","code":"sm-WS","voice":"sm-WS-Wavenet-A","lang_code":"sm","dub":"sm-WS","translate":"sm","flow_prompt":"Samoa healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":19,"flag":"🇨🇦","name":"كندا","lang":"إنجليزي/فرنسي كندي","code":"en-CA","voice":"en-CA-Wavenet-A","lang_code":"en-CA","dub":"en-CA","translate":"en","flow_prompt":"Canadian healthy diet cinematic - Tayybat Dr Diaa"},
        {"id":20,"flag":"🇦🇪","name":"الإمارات","lang":"عربي خليجي","code":"ar-AE","voice":"ar-AE-Wavenet-A","lang_code":"ar-AE","dub":"ar-AE","translate":"ar","flow_prompt":"UAE healthy diet cinematic - Tayybat Dr Diaa"},
    ]
    COUNTRIES=COUNTRIES_21
    # حذف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى - طيبات الدكتور ضياء العوضى فقط - v113
    TOPICS=[
        ["طيبات الدكتور ضياء العوضى","نظام الطيبات - دكتور ضياء العوضى - المسموح والممنوع - خبز - لحوم - فواكه - علاج طبيعي","طيبات"],
        ["طيبات الدكتور ضياء العوضى - المسموحات","خبز قمح كامل - توست - بقسماط - لحوم - كبدة - جمبري - فواكه مسموحة - نظام الطيبات","طيبات-مسموح"],
        ["طيبات الدكتور ضياء العوضى - الممنوعات","الممنوعات في نظام الطيبات - دكتور ضياء العوضى - ماذا يمنع - لماذا - علاج","طيبات-ممنوع"],
        ["طيبات الدكتور ضياء العوضى - قصص شفاء","قصص شفاء بنظام الطيبات - دكتور ضياء العوضى - تجارب حقيقية - شفاء","طيبات-قصص"],
        ["طيبات الدكتور ضياء العوضى - وجبات يومية","وجبات يومية بنظام الطيبات - فطار - غداء - عشاء - دكتور ضياء العوضى","طيبات-وجبات"],
    ]
    TOPIC_MAIN="طيبات الدكتور ضياء العوضى"
    TOPIC_MAIN_EN="Tayybat Dr Diaa El-Awady Diet System - Allowed and Forbidden Foods - Natural Healing"
    TOPIC_DESCRIPTION="نظام الطيبات للدكتور ضياء العوضى - نظام غذائي علاجي طبيعي - المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - بيض - زبدة - قشطة - فواكه مسموحة - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - علاج طبيعي بدون أدوية - قصص شفاء حقيقية - حزف جميع المواضيع واضافة موضوع طيبات الدكتور ضياء العوضى"
    FLOW_MODELS=[
        {"id":"imagen-3.0-generate-001","name":"Imagen 3 - Flow - طيبات الدكتور ضياء العوضى - إنشاء صور أكل صحي - 21 دولة","engine":"Google Flow - Imagen 3 - labs.google/flow"},
        {"id":"veo-3.0-generate-001","name":"Veo 3 - Flow - طيبات الدكتور ضياء العوضى - إنشاء فيديو أكل صحي - 21 دولة","engine":"Google Flow - Veo 3 - labs.google/flow"},
    ]
    KIE_AI_LINK="https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66"
    AFF_LINKS={
        "kie_ai": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66",
        "flow_google": "https://labs.google/flow - Flow Google - طيبات الدكتور ضياء العوضى",
    }
settings=Settings()
