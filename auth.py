import os
from dotenv import load_dotenv

load_dotenv()
MASTER_KEY = os.getenv("POSTSCAN_MASTER_KEY", "Postscan244")
OWNER_NAME = "Thanva Phupingbut 244"

users_db = {
    "admin": {
        "role": "OWNER",
        "allowed_key": MASTER_KEY
    }
}

def verify_master_key(input_key: str) -> bool:
    return input_key.strip() == MASTER_KEY

def register_user(username: str, password: str):
    if username in users_db:
        return False, "❌ ชื่อผู้ใช้นี้มีอยู่แล้ว"
    users_db[username] = {"role": "MEMBER", "password": password}
    return True, "✅ สมัครสมาชิกสำเร็จ"

def login_user(username: str, password: str):
    if username not in users_db:
        return False, "❌ ไม่พบบัญชีนี้", None
    user = users_db[username]
    if user["role"] == "OWNER":
        return (True, f"✅ ยินดีต้อนรับเจ้าของระบบคุณ {OWNER_NAME}", "FULL") if verify_master_key(password) else (False, "❌ รหัสเจ้าของไม่ถูกต้อง", None)
    return (True, "✅ เข้าสู่ระบบสำเร็จ", "SCAN_ONLY") if user.get("password") == password else (False, "❌ รหัสผ่านไม่ถูกต้อง", None)

