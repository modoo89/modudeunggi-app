
import streamlit as st
from modules.extract import extract_address_from_pdf
from modules.crawler import get_kb_price_from_hogang
from modules.calc import calc_loan_by_condition
from modules.report import create_pdf_report

st.set_page_config(page_title="모두등기 리포트 자동화", layout="centered")
st.title("📄 모두등기 | 대출 리포트 자동 생성기")

uploaded_file = st.file_uploader("📑 등기부등본 PDF 업로드", type=["pdf"])
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    address = extract_address_from_pdf("temp.pdf")
    st.success(f"📍 추출 주소: {address}")

    apt_name = st.text_input("🏢 아파트명", "장암주공5단지")
    price = get_kb_price_from_hogang(apt_name)

    if isinstance(price, str):
        st.error(price)
        st.stop()
    else:
        st.info(f"📈 KB 시세: {price:,} 원")

    condition = st.selectbox("💡 대출 조건 선택", ["비1", "비2", "규2-1", "규2-2", "사선", "사후"])
    result = calc_loan_by_condition(price, condition)

    st.subheader("💰 대출 가능 금액")
    st.write(f"▶ 조건: {condition}")
    st.write(f"▶ 시세: {result['시세']:,} 원")
    st.write(f"▶ 대출 가능 금액: {result['가능대출금']:,} 원")

    if st.button("📄 PDF 리포트 생성"):
        filename = create_pdf_report(address, result)
        with open(filename, "rb") as f:
            st.download_button("📥 리포트 다운로드", data=f, file_name=filename, mime="application/pdf")
