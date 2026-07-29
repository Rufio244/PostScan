from fpdf import FPDF
from datetime import datetime

def create_report(data: dict, filename: str = "PostScan_Report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 15, "รายงานผลการสแกน — PostScan", ln=True, align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, f"วันที่สร้าง: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
    pdf.ln(5)
    for key, value in data.items():
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(60, 10, f"{key}:", ln=False)
        pdf.set_font("Helvetica", size=12)
        pdf.multi_cell(0, 10, str(value))
    pdf.output(filename)
    return filename

