# FILE: config/settings.py - اسم الملف: config/settings.py - من الخارج - v115 - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - طيبات الدكتور ضياء العوضى - حذف جميع المواضيع - موضوع واحد - نظام الطيبات - المسموح والممنوع - خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه مسموحة - الممنوعات الجديدة: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - علاج طبيعي بدون أدوية - قصص شفاء حقيقية - وجبات يومية - حذف جميع المواضيع - جميع المواضيع القديمة محذوفة - ترتاريا - الجدار الجليدي - 33 أرض - كل شيء محذوف - موضوع واحد فقط - طيبات الدكتور ضياء العوضى - دمج اداة فلو من جوجل لإنشاء الصور - Flow Google - Imagen 3 + Veo 3 + Gemini - labs.google/flow - 21 دولة: مصر + سويسرا + الدنمارك + السويد + فرنسا + ألمانيا + UK + النرويج + USA + بلجيكا + أيرلندا + إيطاليا + هولندا + أستراليا + زيمبابوي + فوكلاند + سانت هيلينا + جنوب السودان + ساموا + كندا + الإمارات - فيديو واحد مجمع - طيبات الدكتور ضياء العوضى - ترجمة 21 دولة + صوت 21 دولة + دبلجة 21 دولة - مونتاج سينمائي + كاميرات + زوايا بروفشنل + تخصيص جزء من الفيديو - ربط قناتي - https://www.youtube.com/@CursedMedicineEG - @CursedMedicineEG - حذف جميع المواضيع - موضوع واحد - طيبات الدكتور ضياء العوضى - Flow Google - التشغيل علي n8n وعدم الربط - تشغيل خارجي فقط - Workflow خارجي في n8n_workflows/ - لا يوجد ربط داخلي - standalone - 0.000000000001s / 0.0000000000001s - اسرع من 0.00000000001 - ULTRA FASTEST EVER
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
    ALL_TOPICS_DELETED=True
    DELETED_TOPICS_COUNT=30
    SINGLE_TOPIC=True
    SINGLE_TOPIC_NAME="طيبات الدكتور ضياء العوضى"
    # الممنوعات الجديدة: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض
    FORBIDDEN_ITEMS=["دجاج","لبن","زبادي","خضار","بقوليات","فول","عدس","حمص","شاي","قهوة","بيض"]
    FORBIDDEN_TEXT="الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - طيبات الدكتور ضياء العوضى - ممنوعات نظام الطيبات - علاج طبيعي - حذف جميع المواضيع - موضوع واحد - طيبات - Flow Google - 21 دولة - التشغيل علي n8n وعدم الربط - 0.000000000001s"
    ALLOWED_ITEMS=["خبز قمح كامل","توست","بقسماط","أرز","بطاطس","لحوم","كبدة","جمبري","زبدة","قشطة","فواكه","موز","تفاح","رمان","بلح","تين","عنب","مانجو","عسل"]
    ALLOWED_TEXT="المسموحات: خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه: موز - تفاح - رمان - بلح - تين - عنب - مانجو - عسل - طيبات الدكتور ضياء العوضى - مسموحات نظام الطيبات - 21 دولة - Flow Google - 0.000000000001s"
    # موضوع واحد فقط - طيبات الدكتور ضياء العوضى - 5 مواضيع فرعية - الممنوعات الجديدة تشمل بيض
    TAYYBAT_TOPICS=[
        ["طيبات الدكتور ضياء العوضى","نظام الطيبات - المسموح والممنوع - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - علاج طبيعي بدون أدوية","طيبات"],
        ["المسموحات - طيبات","خبز قمح كامل - توست - بقسماط - أرز - بطاطس - لحوم - كبدة - جمبري - زبدة - قشطة - فواكه: موز - تفاح - رمان - بلح - تين - عنب - مانجو - عسل - طيبات الدكتور ضياء العوضى - مسموحات","طيبات"],
        ["الممنوعات - طيبات - دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض","الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - دجاج ممنوع - لبن ممنوع - زبادي ممنوع - خضار ممنوع - بقوليات ممنوعة - فول ممنوع - عدس ممنوع - حمص ممنوع - شاي ممنوع - قهوة ممنوعة - بيض ممنوع - ممنوعات نظام الطيبات - الدكتور ضياء العوضى - علاج طبيعي","طيبات"],
        ["قصص شفاء - طيبات","شفاء من قولون - سكر - ضغط - حساسية - ارتجاع - إمساك - تجارب حقيقية - مرضى شفوا بنظام الطيبات بدون بيض - الدكتور ضياء العوضى - علاج طبيعي بدون أدوية - قصص شفاء حقيقية - طيبات - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض","طيبات"],
        ["وجبات يومية - طيبات - بدون بيض","فطار: توست + زبدة + عسل - بدون بيض - غداء: أرز + لحم ضاني + بطاطس - عشاء: بقسماط + قشطة + موز - وجبات نظام الطيبات بدون بيض - الممنوعات: دجاج - لبن - زبادي - خضار - بقوليات - فول - عدس - حمص - شاي - قهوة + بيض - الدكتور ضياء العوضى - طيبات - وجبات يومية - صحي","طيبات"],
    ]
    TOPICS=TAYYBAT_TOPICS
    ALL=TAYYBAT_TOPICS
    COUNTRIES_21=[
        {"id":0,"flag":"🇪🇬","name":"مصر","lang":"عربي","code":"ar-EG","voice":"ar-EG-Wavenet-A","lang_code":"ar","dub":"ar-EG","translate":"ar","flow_prompt":"Egyptian tayybat food - no chicken no milk no yogurt no vegetables no legumes no eggs - whole wheat bread - meat - fruits - tayybat Dr Diaa El Awady"},
        {"id":1,"flag":"🇨🇭","name":"سويسرا","lang":"ألماني/فرنسي/إيطالي","code":"de-CH","voice":"de-CH-Wavenet-A","lang_code":"de","dub":"de-CH","translate":"de","flow_prompt":"Swiss tayybat food - no eggs - tayybat style"},
        {"id":2,"flag":"🇩🇰","name":"الدنمارك","lang":"دنماركي","code":"da-DK","voice":"da-DK-Wavenet-A","lang_code":"da","dub":"da-DK","translate":"da","flow_prompt":"Danish tayybat food - no eggs chicken milk yogurt vegetables legumes - tayybat"},
        {"id":3,"flag":"🇸🇪","name":"السويد","lang":"سويدي","code":"sv-SE","voice":"sv-SE-Wavenet-A","lang_code":"sv","dub":"sv-SE","translate":"sv","flow_prompt":"Swedish tayybat food - no eggs - tayybat"},
        {"id":4,"flag":"🇫🇷","name":"فرنسا","lang":"فرنسي","code":"fr-FR","voice":"fr-FR-Wavenet-A","lang_code":"fr","dub":"fr-FR","translate":"fr","flow_prompt":"French tayybat food - no eggs - tayybat"},
        {"id":5,"flag":"🇩🇪","name":"ألمانيا","lang":"ألماني","code":"de-DE","voice":"de-DE-Wavenet-A","lang_code":"de","dub":"de-DE","translate":"de","flow_prompt":"German tayybat food - no eggs - tayybat"},
        {"id":6,"flag":"🇬🇧","name":"المملكة المتحدة","lang":"إنجليزي بريطاني","code":"en-GB","voice":"en-GB-Wavenet-A","lang_code":"en-GB","dub":"en-GB","translate":"en","flow_prompt":"British tayybat food - no chicken milk yogurt vegetables legumes beans lentils chickpeas tea coffee eggs - tayybat"},
        {"id":7,"flag":"🇳🇴","name":"النرويج","lang":"نرويجي","code":"nb-NO","voice":"nb-NO-Wavenet-A","lang_code":"no","dub":"nb-NO","translate":"no","flow_prompt":"Norwegian tayybat food - no eggs - tayybat"},
        {"id":8,"flag":"🇺🇸","name":"الولايات المتحدة","lang":"إنجليزي أمريكي","code":"en-US","voice":"en-US-Wavenet-A","lang_code":"en-US","dub":"en-US","translate":"en","flow_prompt":"American tayybat food - no eggs - steak potatoes - tayybat - Dr Diaa El Awady"},
        {"id":9,"flag":"🇧🇪","name":"بلجيكا","lang":"هولندي/فرنسي","code":"nl-BE","voice":"nl-BE-Wavenet-A","lang_code":"nl","dub":"nl-BE","translate":"nl","flow_prompt":"Belgian tayybat food - no eggs - tayybat"},
        {"id":10,"flag":"🇮🇪","name":"أيرلندا","lang":"إنجليزي أيرلندي","code":"en-IE","voice":"en-IE-Wavenet-A","lang_code":"en-IE","dub":"en-IE","translate":"en","flow_prompt":"Irish tayybat food - no eggs - lamb potatoes - tayybat"},
        {"id":11,"flag":"🇮🇹","name":"إيطاليا","lang":"إيطالي","code":"it-IT","voice":"it-IT-Wavenet-A","lang_code":"it","dub":"it-IT","translate":"it","flow_prompt":"Italian tayybat food - no eggs - rice meat - tayybat"},
        {"id":12,"flag":"🇳🇱","name":"هولندا","lang":"هولندي","code":"nl-NL","voice":"nl-NL-Wavenet-A","lang_code":"nl","dub":"nl-NL","translate":"nl","flow_prompt":"Dutch tayybat food - no eggs - cheese bread - tayybat"},
        {"id":13,"flag":"🇦🇺","name":"أستراليا","lang":"إنجليزي أسترالي","code":"en-AU","voice":"en-AU-Wavenet-A","lang_code":"en-AU","dub":"en-AU","translate":"en","flow_prompt":"Australian tayybat food - no eggs - lamb steak - tayybat"},
        {"id":14,"flag":"🇿🇼","name":"زيمبابوي","lang":"إنجليزي زيمبابوي","code":"en-ZW","voice":"en-ZW-Wavenet-A","lang_code":"en-ZW","dub":"en-ZW","translate":"en","flow_prompt":"Zimbabwe tayybat food - no eggs - meat rice - tayybat"},
        {"id":15,"flag":"🇫🇰","name":"جزر فوكلاند","lang":"إنجليزي فوكلاند","code":"en-FK","voice":"en-GB-Wavenet-A","lang_code":"en-FK","dub":"en-FK","translate":"en","flow_prompt":"Falkland tayybat food - no eggs - fish - tayybat"},
        {"id":16,"flag":"🇸🇭","name":"سانت هيلينا","lang":"إنجليزي سانت هيلينا","code":"en-SH","voice":"en-GB-Wavenet-A","lang_code":"en-SH","dub":"en-SH","translate":"en","flow_prompt":"Saint Helena tayybat food - no eggs - fruits - tayybat"},
        {"id":17,"flag":"🇸🇸","name":"جنوب السودان","lang":"إنجليزي جنوب السودان","code":"en-SS","voice":"en-US-Wavenet-A","lang_code":"en-SS","dub":"en-SS","translate":"en","flow_prompt":"South Sudan tayybat food - no eggs - meat rice - tayybat"},
        {"id":18,"flag":"🇼🇸","name":"ساموا","lang":"ساموا","code":"sm-WS","voice":"sm-WS-Wavenet-A","lang_code":"sm","dub":"sm-WS","translate":"sm","flow_prompt":"Samoa tayybat food - no eggs - tropical fruits - tayybat"},
        {"id":19,"flag":"🇨🇦","name":"كندا","lang":"إنجليزي/فرنسي كندي","code":"en-CA","voice":"en-CA-Wavenet-A","lang_code":"en-CA","dub":"en-CA","translate":"en","flow_prompt":"Canadian tayybat food - no eggs - meat potatoes - tayybat"},
        {"id":20,"flag":"🇦🇪","name":"الإمارات","lang":"عربي خليجي","code":"ar-AE","voice":"ar-AE-Wavenet-A","lang_code":"ar-AE","dub":"ar-AE","translate":"ar","flow_prompt":"UAE tayybat food - Emirati lamb rice - kabsa tayybat style - no chicken no milk no yogurt no vegetables no legumes no eggs - cinematic food photography - luxury - tayybat Dr Diaa"},
    ]
    COUNTRIES=COUNTRIES_21
    FLOW_MODELS=[
        {"id":"imagen-3.0-generate-001","name":"Imagen 3 - طيبات - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض - صور أكل صحي بدون بيض - Flow Google - 21 دولة"},
        {"id":"veo-3.0-generate-001","name":"Veo 3 - طيبات - فيديو أكل صحي بدون بيض - طيبات الدكتور ضياء العوضى - Flow Google - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض"},
        {"id":"gemini-2.0-flash-exp-image-generation","name":"Gemini 2.0 Flash - طيبات - صور أكل صحي بدون بيض - مجاني - Flow Google - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض"},
    ]
    KIE_AI_LINK="https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66"
    AFF_LINKS={"kie_ai": "https://kie.ai?ref=0e3195dd062bf11f0da7496dd3c1bf66","flow_google": "https://labs.google/flow - طيبات - الممنوعات: دجاج لبن زبادي خضار بقوليات فول عدس حمص شاي قهوة بيض"}
settings=Settings()
