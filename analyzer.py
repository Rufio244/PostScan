import requests
from bs4 import BeautifulSoup

def analyze_structure(url: str, full_mode: bool = False):
    try:
        res = requests.get(url, timeout=15)
        soup = BeautifulSoup(res.text, "html.parser")
        result = {
            "เป้าหมาย": url,
            "สถานะ": f"สำเร็จ รหัส {res.status_code}",
            "ชื่อเรื่อง": soup.title.string.strip() if soup.title else "ไม่พบ",
            "จำนวนลิงก์": len(soup.find_all("a")),
            "จำนวนรูปภาพ": len(soup.find_all("img"))
        }
        if full_mode:
            result["โครงสร้างเต็ม"] = str(soup.prettify())[:2000] + "..."
            result["ข้อเสนอแนะ"] = "ตรวจสอบความปลอดภัยและประสิทธิภาพการทำงาน"
        return result
    except Exception as e:
        return {"ข้อผิดพลาด": str(e)}

