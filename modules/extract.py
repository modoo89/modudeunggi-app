
import fitz
import re

def extract_address_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    match = re.search(r"(서울|경기)[^\n]+(아파트|주공)[^\n]+동[^\n]+호", text)
    return match.group(0).strip() if match else "주소 추출 실패"
