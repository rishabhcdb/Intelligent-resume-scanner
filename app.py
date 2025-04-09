# app.py
import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_matcher import calculate_similarity

st.title("📄 Intelligent Resume Screener")

resume_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")
jd_file = st.file_uploader("Upload Job Description (PDF)", type="pdf")

if resume_file and jd_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    with open("temp_jd.pdf", "wb") as f:
        f.write(jd_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")
    jd_text = extract_text_from_pdf("temp_jd.pdf")

    if resume_text and jd_text:
        score = calculate_similarity(resume_text, jd_text)
        st.success(f"✅ Match Score: {score}%")

        if score > 75:
            st.balloons()
        elif score < 40:
            st.warning("Low match – consider adding more relevant skills.")
