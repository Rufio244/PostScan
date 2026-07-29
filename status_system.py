from datetime import datetime

class StatusSystem:
    def __init__(self):
        self.running = False
        self.progress = 0
        self.last_update = "-"

    def update(self, scan=False):
        self.running = True
        if scan: self.progress += 10
        if self.progress > 100: self.progress = 100
        self.last_update = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def get(self):
        return {
            "กำลังทำงาน": "ใช่" if self.running else "ไม่ใช่",
            "ความคืบหน้า": f"{self.progress}%",
            "อัปเดตล่าสุด": self.last_update
        }

