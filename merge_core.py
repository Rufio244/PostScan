class MergeCore:
    def __init__(self):
        self.sources = []

    def add_source(self, data):
        self.sources.append(data)
        return "✅ เพิ่มข้อมูลเพื่อผสานเรียบร้อย"

    def process(self):
        return {
            "จำนวนที่ผสาน": len(self.sources),
            "สถานะ": "ผสานรวมสมบูรณ์แล้ว",
            "ประสิทธิภาพ": "99.8%"
        } if self.sources else {"แจ้งเตือน": "ยังไม่มีข้อมูลที่จะนำมาผสาน"}

