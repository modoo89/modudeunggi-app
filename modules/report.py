
from fpdf import FPDF
import datetime

def create_pdf_report(address, result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, "모두등기 대출 리포트", ln=True)
    pdf.cell(0, 10, f"주소: {address}", ln=True)
    pdf.cell(0, 10, f"조건: {result['조건']}", ln=True)
    pdf.cell(0, 10, f"시세: {result['시세']:,} 원", ln=True)
    pdf.cell(0, 10, f"가능 대출금: {result['가능대출금']:,} 원", ln=True)
    pdf.cell(0, 10, f"생성일: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    filename = f"modudeunggi_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    pdf.output(filename)
    return filename
