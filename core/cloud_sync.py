# FILE: core/cloud_sync.py
# اسم الملف: cloud_sync.py - قديم+جديد+أحداث - كود للنسخ
# الحتت المستخبي - Core Engine

"""
مزامنة التخزين السحابي لحفظ الأفلام الطويلة 60 دقيقة - قديم+جديد - كود للنسخ
"""
import shutil
from pathlib import Path
import json
from datetime import datetime

class CloudSync:
    def __init__(self):
        self.local_dir = Path("/tmp/videos")
        self.cloud_dir = Path("/tmp/cloud_backup")  # محاكاة S3/GDrive
        self.cloud_dir.mkdir(parents=True, exist_ok=True)
        self.old_projects = ["AI_Content_Empire_Pro", "cyber_caliph_v35-v55"]
        self.new_events = []
    
    def sync_old_new(self):
        """جمع المشاريع القديمة والحديثة والأحداث وحفظها سحابيا"""
        print("[☁️] مزامنة قديم+جديد+أحداث - سحابي - كود للنسخ")
        for f in self.local_dir.glob("*.mp4*"):
            dest = self.cloud_dir / f.name
            try:
                shutil.copy2(f, dest)
                print(f"  - {f.name} -> cloud - كود للنسخ")
            except:
                pass
        
        # حفظ فهرس قديم+جديد
        index = {
            "old_projects": self.old_projects,
            "new_events": self.new_events[-20:],
            "synced_at": datetime.now().isoformat(),
            "code_copy": True
        }
        (self.cloud_dir / "old_new_index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"[✅] تمت المزامنة - قديم+جديد - كود للنسخ")

cloud_sync = CloudSync()
