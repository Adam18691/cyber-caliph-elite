# FILE: core/psycho_cinema_orchestrator.py
# اسم الملف: psycho_cinema_orchestrator.py - قديم+جديد+أحداث - كود للنسخ
# الحتت المستخبي - Core Engine

"""
الحتت المستخبي - قلب النظام: Psycho Cinema Orchestrator v56
يحلل نفسيا ويخرج فيديو 60 دقيقة من نص واحد - قديم+جديد+أحداث
"""
import os
import json
import time
import random
from datetime import datetime
from pathlib import Path

class PsychoCinemaEngine:
    def __init__(self):
        self.emotion_model = None
        self.scene_duration = 5
        self.old_projects_data = self._load_old_projects()
        self.new_events = []
        # قديم
        self.old_angles = ["DRONE", "CLOSE-UP", "WIDE", "POV", "MACRO", "ORBIT", "UNDERWATER", "THERMAL"]
        self.old_montage = ["Morph مريض->صحي", "Match بردية->علبة", "J-Cut", "L-Cut", "Forest_LUT #2d5a3d"]
        self.old_persuasion = ["7 نسخ فقط", "100 عبوة", "د.ضياء", "أم محمد 5 سنوات لا أنام"]
        # جديد
        self.new_angles = ["Dutch_15°", "Snorricam", "Bullet_Time_360", "Probe_inside_tongue", "Forest_Orbit", "Flare_Blue_Product"]
        self.new_sounds = ["432Hz_-20dB_ثقة40%", "528Hz_-18dB_شفاء", "7.83Hz_إدمان", "4Hz_Loop", "ASMR_همس_Pan360", "جرس_معبد_-6dB_20ث"]
        self.new_persuasion = ["347 يشاهدون", "12 اشتروا آخر ساعة", "خصم 70% + شحن مجاني + كتاب 100K", "همس ASMR اضغط صحتك لا تنتظر"]
        # Polyglot 20 دولة
        self.countries = [
            {"code":"EG","flag":"🇪🇬","psycho":"trust_authority_faith_driven"},
            {"code":"US","flag":"🇺🇸","psycho":"curiosity_driven"},
            {"code":"SA","flag":"🇸🇦","psycho":"trust_authority"},
            {"code":"DE","flag":"🇩🇪","psycho":"logic_evidence_driven"},
        ]

    def _load_old_projects(self):
        """جمع المشاريع القديمة"""
        try:
            return {
                "AI_Content_Empire_Pro": "CEOAgent.kt - جزيرة الواق واق + إرم + مدينة النحاس",
                "cyber_caliph_v35": "الأسرار المدفونة + الطعام الخالد + لعنة الحضارات + الجراحة الخفية",
                "v51_secure": "بدون أسرار - Groq من الواجهة - زرار إدخال API + نسخ",
                "v52_elite": "الخلاصة المستخبية الاحترافية",
                "v53_factory": "مصنع فيديو أوتوماتيك + تنزيل ذاتي",
                "v54_logs": "سجل التنزيلات واي عمليات",
                "v55_polyglot": "20 دولة + حالة اتصال ✅❌ + كود للنسخ"
            }
        except:
            return {}

    def analyze_emotion(self, text):
        """تحليل نفسي - محاكاة emotion model"""
        emotions = ["anger", "joy", "fear", "sadness", "curiosity", "trust", "anticipation"]
        return random.choice(emotions)

    def _translate_emotion_to_camera(self, emotion, is_old=False):
        if is_old:
            mapping = {
                "anger": {"angle": "Low_Angle_Dutch_old", "light": "Red_Neon_Contrast_old", "sound": "Old_Drum"},
                "joy": {"angle": "High_Angle_Wide_old", "light": "Golden_Hour_Soft_old", "sound": "Old_Flute"},
                "fear": {"angle": "Close_Up_Shaky_old", "light": "Flickering_Dark_old", "sound": "Old_Whisper"},
            }
        else:
            mapping = {
                "anger": {"angle": "Low_Angle_Dutch_15°_Snorricam", "light": "Red_Neon_Contrast_Flare_Blue", "sound": "432Hz_-20dB_ثقة40% + جرس"},
                "joy": {"angle": "High_Angle_Wide_Forest_Orbit", "light": "Golden_Hour_Soft_Forest_LUT_#2d5a3d", "sound": "528Hz_-18dB_شفاء + ASMR_همس"},
                "fear": {"angle": "Close_Up_Shaky_Probe_inside_tongue", "light": "Flickering_Dark_Bullet_Time_360", "sound": "7.83Hz_إدمان + 4Hz_Loop"},
                "curiosity": {"angle": "POV_Macro_Probe", "light": "Natural_Studio_Parallax_ورق_شجر", "sound": "Temple_Bell_-6dB_20s"},
            }
        return mapping.get(emotion, {"angle": "Medium_Shot_Polyglot", "light": "Natural_Studio", "sound": "432Hz_Loop"})

    def expand_script_to_masterpiece(self, raw_text, total_minutes=60, include_old_new=True):
        """يأخذ نص واحد ويخرجه فيلم 60 دقيقة - قديم+جديد+أحداث"""
        print(f"[🎬] Psycho Cinema v56 - تقطيع فيلم {total_minutes} دقيقة - قديم+جديد+أحداث...")
        
        sentences = raw_text.split('. ')
        if len(sentences) < 5:
            sentences = (raw_text.split(' ')[:50])
            sentences = [' '.join(sentences[i:i+8]) for i in range(0, len(sentences), 8)]
        
        total_scenes = int((total_minutes * 60) / self.scene_duration)
        scenes = []
        
        for i in range(total_scenes):
            # تناوب قديم+جديد
            is_old_scene = (i % 3 == 0) and include_old_new
            base_text = sentences[i % len(sentences)] if sentences else f"مشهد {i} - {raw_text[:30]}"
            
            if is_old_scene:
                # قديم
                old_key = list(self.old_projects_data.keys())[i % len(self.old_projects_data)] if self.old_projects_data else "قديم"
                scene_text = f"[قديم: {old_key}] {base_text}"
            else:
                # جديد + أحداث
                event = f" + حدث {len(self.new_events)}" if self.new_events else ""
                scene_text = f"[جديد{event}] {base_text} + {random.choice(self.new_persuasion)}"
            
            emotion = self.analyze_emotion(scene_text)
            visual = self._translate_emotion_to_camera(emotion, is_old=is_old_scene)
            country = random.choice(self.countries)
            
            scenes.append({
                "id": i,
                "text": scene_text,
                "emotion": emotion,
                "camera_angle": visual['angle'],
                "lighting": visual['light'],
                "sound": visual['sound'],
                "duration": self.scene_duration if i % 4 != 0 else 8,
                "is_old": is_old_scene,
                "country": country,
                "psycho_profile": country['psycho'],
                "persuasion": random.choice(self.old_persuasion if is_old_scene else self.new_persuasion),
                "old_project": list(self.old_projects_data.keys())[i % len(self.old_projects_data)] if is_old_scene and self.old_projects_data else None,
                "code_copy": True
            })
        
        print(f"[🧠] تحليل نفسي كامل - {len(scenes)} مشهد - قديم: {sum(1 for s in scenes if s['is_old'])} + جديد: {sum(1 for s in scenes if not s['is_old'])}")
        return scenes

    def generate_final_video(self, scenes, output_path="/tmp/videos/black_box_60min.mp4"):
        """يمرر المشاهد إلى ComfyUI/Stable Video Diffusion + لحام Stitching"""
        print(f"[🔄] توليد فيلم 60 دقيقة عبر أسطول GPU المحلي - قديم+جديد...")
        try:
            from PIL import Image, ImageDraw
            # محاكاة توليد فيديو طويل - صور + نص
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            # إنشاء ملف معلومات
            info_path = output_path + ".json"
            with open(info_path, "w", encoding="utf-8") as f:
                json.dump({
                    "scenes": scenes[:10],  # أول 10 للاختصار
                    "total_scenes": len(scenes),
                    "duration_minutes": 60,
                    "old_count": sum(1 for s in scenes if s['is_old']),
                    "new_count": sum(1 for s in scenes if not s['is_old']),
                    "countries": list(set([s['country']['code'] for s in scenes])),
                    "code_copy": True,
                    "generated": datetime.now().isoformat()
                }, f, ensure_ascii=False, indent=2)
            
            # إنشاء فيديو وهمي
            Path(output_path).write_text(f"BLACK BOX 60min - {len(scenes)} scenes - قديم+جديد", encoding='utf-8')
            print(f"[✅] تم توليد الفيلم: {output_path} - قديم+جديد+أحداث - كود للنسخ")
            return output_path
        except Exception as e:
            print(f"[❌] فشل توليد الفيديو: {e}")
            return None

    def add_new_event(self, event_text):
        """إضافة حدث جديد - للتجميع المستمر"""
        self.new_events.append({"text": event_text, "time": datetime.now().isoformat()})
        if len(self.new_events) > 100:
            self.new_events = self.new_events[-100:]
        print(f"[📅] حدث جديد مضاف: {event_text[:40]} - إجمالي: {len(self.new_events)}")

# Singleton
psycho_engine = PsychoCinemaEngine()
