import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.write("KAKAz")
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("🐂 Data Cleaning Workshop App"):
    st.switch_page("pages/clean_kla1.py")
elif st.button("📂 Customer Data Cleaner"):
    st.switch_page("pages/clean_customers.py")
