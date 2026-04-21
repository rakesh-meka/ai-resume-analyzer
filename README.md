# 🚀 AI Resume Analyzer

An end-to-end AI-powered application that analyzes resumes (PDF) extracts key skills and calculates a relevance score based on predefined criteria.

🔗 **Live Demo:**
https://ai-resume-analyzer-zaf8z3zge5hf2es6szabwj.streamlit.app

---

## 📌 Overview

The **AI Resume Analyzer** is designed to automate resume evaluation by:

* Extracting text from PDF resumes
* Identifying relevant technical skills
* Scoring resumes based on skill match

This project demonstrates practical implementation of **NLP concepts**, **data processing**, and **end-to-end deployment** using modern tools.

---

## ✨ Features

* 📄 Upload resume in PDF format
* 📊 Job Description vs Resume matching using TF-IDF
* 🔍 Extract text using PDF parsing
* 🧠 Identify skills using keyword-based NLP
* 📊 Generate a resume score
* 🌐 Interactive UI using Streamlit
* 🚀 Deployed and accessible online

---

## 🛠 Tech Stack

* **Programming Language:** Python
* **Libraries:** PyPDF2, Pandas, NumPy, Scikit-learn
* **Framework:** Streamlit
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Community Cloud

---

## 📂 Project Structure

```
ai-resume-analyzer/
│── src/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── resume_scorer.py
│
│── data/
│   └── sample_resume.pdf
│
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── LICENSE
```
---

## ⚙️ Installation & Setup

### 1. Clone the repository

git clone https://github.com/rakesh-meka/ai-resume-analyzer.git
cd ai-resume-analyzer

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

streamlit run app.py

---

## 🧪 How It Works

1. User uploads a resume (PDF)
2. Text is extracted using PyPDF2
3. Skills are identified via keyword matching
4. A score is calculated based on matched skills
5. Results are displayed in the UI

---

## 📊 Example Output

* Extracted Skills: ['python', 'sql', 'machine learning']
* Resume Score: 62.5%

---

## 🚀 Future Enhancements

* Advanced NLP using spaCy / Transformers
* Semantic similarity scoring
* Resume ranking system
* Dashboard with visual analytics
* Support for DOCX and image-based resumes
* Authentication system

---

## 💡 Key Learnings

* End-to-end project development
* GitHub Issues workflow
* Dependency management using virtual environments
* Streamlit UI development
* Cloud deployment

---

## 📫 Contact

* LinkedIn: https://www.linkedin.com/in/rakeshmeka
* Email: rakeshmeka.work@gmail.com

---

## ⭐ Acknowledgment

If you find this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
