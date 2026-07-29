class StatsMonitor:
    def __init__(self):
        self.scan_count = 0
        self.modify_count = 0
        self.success = 0

    def add_scan(self): self.scan_count +=1
    def add_modify(self): self.modify_count +=1
    def add_success(self): self.success +=1

    def summary(self):
        total = self.scan_count + self.modify_count
        rate = round((self.success / total)*100,2) if total >0 else 0
        return {
            "จำนวนครั้งที่สแกน": self.scan_count,
            "จำนวนครั้งที่ปรับแก้": self.modify_count,
            "อัตราสำเร็จ": f"{rate}%"
        }

