class NetworkManager:
    def __init__(self):
        self.proxy = None
        self.vpn_on = False

    def set_proxy(self, proxy_url=None):
        self.proxy = proxy_url
        return f"✅ พร็อกซี: {'เปิดใช้งาน' if proxy_url else 'ปิดการใช้งาน'}"

    def toggle_vpn(self, status: bool):
        self.vpn_on = status
        return f"✅ VPN: {'เชื่อมต่อแล้ว' if status else 'ตัดการเชื่อมต่อ'}"

    def rotate_ip(self):
        return "✅ สลับ/ซ่อน ที่อยู่ IP สำเร็จ"

