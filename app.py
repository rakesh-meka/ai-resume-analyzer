import streamlit as st
from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.resume_scorer import calculate_score

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = extract_text_from_pdf("temp.pdf")
    skills = extract_skills(text)
    score = calculate_score(skills)

    st.subheader("Extracted Skills")
    st.write(skills)

    st.subheader("Resume Score")
    st.write(f"{score}%")