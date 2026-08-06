{
  "name": "Cyber Caliph Ultra - No Download - 19 Countries",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {"field": "hours", "minutesInterval": 0, "triggerAtHour": 11},
            {"field": "hours", "minutesInterval": 0, "triggerAtHour": 20}
          ]
        }
      },
      "id": "schedule",
      "name": "Schedule Trigger - 11AM & 8PM EG",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [0, 0],
      "typeVersion": 1
    },
    {
      "parameters": {
        "url": "https://cyber-caliph-elite.onrender.com/api/ultra",
        "sendQuery": true,
        "queryParameters": {
          "parameters": [
            {"name": "disease", "value": "={{ ['colon','sugar','pressure','heart','kidney','liver','bones','cancer'][Math.floor(Math.random()*8)] }}"}
          ]
        }
      },
      "id": "http",
      "name": "HTTP - Get ULTRA CLEAN Data",
      "type": "n8n-nodes-base.httpRequest",
      "position": [250, 0],
      "typeVersion": 4
    },
    {
      "parameters": {
        "content": "انت خبير يوتيوب لنظام الطيبات. خد البيانات دي وطلع عنوان يضرب CTR + وصف + هاشتاجات لـ 19 دولة.\n\nالبيانات: {{ $json }}",
        "promptType": "define"
      },
      "id": "ai1",
      "name": "AI Agent 1 - Gemini SEO",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [500, -100],
      "typeVersion": 1
    },
    {
      "parameters": {
        "content": "حول الوصف ده لـ 3 لغات انجليزي فرنسي الماني مع الحفاظ على الروابط: {{ $json.description_links_6_short }}",
        "promptType": "define"
      },
      "id": "ai2",
      "name": "AI Agent 2 - Groq Translate & Polish",
      "type": "@n8n/n8n-nodes-langchain.agent",
      "position": [500, 200],
      "typeVersion": 1
    },
    {
      "parameters": {
        "assignments": {
          "assignments": [
            {"id": "title", "name": "youtube_title", "value": "={{ $json.title_ar }} | Waeldeban186", "type": "string"},
            {"id": "desc", "name": "youtube_desc", "value": "={{ $json.title_en }}\n\nFR: {{ $json.title_fr }}\nDE: {{ $json.title_de }}\n\n🔗 LINKS:\n{{ $json.description_links_6_short.join('\\n') }}\n\n#نظام_الطيبات #دكتور_ضياء_العوضي", "type": "string"},
            {"id": "tags", "name": "tags", "value": "=نظام الطيبات, التلبينة, {{ $json.all_translations.en }}", "type": "string"}
          ]
        }
      },
      "id": "set",
      "name": "SET - YouTube Ready",
      "type": "n8n-nodes-base.set",
      "position": [750, 0],
      "typeVersion": 3
    },
    {
      "parameters": {
        "title": "={{ $json.youtube_title }}",
        "description": "={{ $json.youtube_desc }}",
        "tags": "={{ $json.tags }}",
        "categoryId": "22",
        "privacyStatus": "public",
        "selfDeclaredMadeForKids": false
      },
      "id": "yt",
      "name": "YouTube - Upload",
      "type": "n8n-nodes-base.youTube",
      "position": [1000, 0],
      "typeVersion": 1,
      "credentials": {"youTubeOAuth2Api": {"id": "YOUR_YOUTUBE_CRED"}}
    }
  ],
  "connections": {
    "Schedule Trigger - 11AM & 8PM EG": {"main": [[{"node": "HTTP - Get ULTRA CLEAN Data", "type": "main", "index": 0}]]},
    "HTTP - Get ULTRA CLEAN Data": {"main": [[{"node": "AI Agent 1 - Gemini SEO", "type": "main", "index": 0}, {"node": "AI Agent 2 - Groq Translate & Polish", "type": "main", "index": 0}]]},
    "AI Agent 1 - Gemini SEO": {"main": [[{"node": "SET - YouTube Ready", "type": "main", "index": 0}]]},
    "AI Agent 2 - Groq Translate & Polish": {"main": [[{"node": "SET - YouTube Ready", "type": "main", "index": 0}]]},
    "SET - YouTube Ready": {"main": [[{"node": "YouTube - Upload", "type": "main", "index": 0}]]}
  }
}
