```python
import streamlit as st
from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.resume_scorer import calculate_score
from src.jd_matcher import calculate_similarity

# Page config
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1f4037, #99f2c8);
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #f0f0f0;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🚀 AI Resume Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze resumes with AI & match with job descriptions</div>", unsafe_allow_html=True)

st.markdown("---")

# Input Section
with st.container():
    st.markdown("### 📥 Input Section")

    uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
    jd_text = st.text_area("📝 Paste Job Description")

    analyze = st.button("🚀 Analyze Resume")

# Processing
if analyze:
    if uploaded_file is None or not jd_text:
        st.warning("⚠️ Please upload a resume and paste a job description.")
    else:
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        text = extract_text_from_pdf("temp.pdf")
        skills = extract_skills(text)
        score = calculate_score(skills)
        jd_score = calculate_similarity(text, jd_text)

        st.markdown("---")
        st.success("✅ Analysis Completed Successfully!")

        # Results Section
        with st.container():
            st.markdown("## 📊 Results")

            # Skills Card
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("🔍 Extracted Skills")
            st.write(skills)
            st.markdown("</div>", unsafe_allow_html=True)

            # Resume Score
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("📈 Resume Score")
            st.progress(int(score))
            st.write(f"**{score}%**")
            st.markdown("</div>", unsafe_allow_html=True)

            # JD Match Score
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.subheader("🎯 JD Match Score")
            st.progress(int(jd_score))
            st.write(f"**{jd_score}%**")
            st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color: gray; </div>",
    unsafe_allow_html=True
)
```
