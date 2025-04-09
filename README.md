# 🧠 Intelligent Resume Screener

A smart, NLP-powered Streamlit web app that analyzes a candidate's resume against a given job description and returns a match score based on semantic similarity.

This tool helps job seekers and recruiters quickly assess how well a resume aligns with a specific job role.

---
✨ Example Use Case
You're applying to a job and want to check how well your resume matches the JD.
Just upload both files — the app gives you a similarity score and flags missing keywords to help you improve it.

## 🚀 Features

- Upload a **PDF resume** and **job description**
- Extracts and preprocesses text using **spaCy**
- Computes **semantic similarity** using **TF-IDF** and **cosine similarity**
- Returns a **Match Score (%)**
- Highlights feedback for low match cases
- Clean and intuitive **Streamlit UI**

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – UI and frontend deployment
- **spaCy** – NLP processing (tokenization, lemmatization)
- **scikit-learn** – TF-IDF vectorization and similarity scoring
- **PyPDF2** – Extract text from uploaded PDF files

---

## 📷 Screenshot

![Screenshot](path_to_screenshot.png)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/intelligent-resume-screener.git
cd intelligent-resume-screener

### 2. Install dependencies 
pip install -r requirements.txt

3. Download the spaCy language model
python -m spacy download en_core_web_sm

Running the App Locally
streamlit run app.py


🧠 How It Works
PDF Parsing: Uses PyPDF2 to extract text from uploaded resume and JD files.

Text Preprocessing: Cleans and lemmatizes text using spaCy.

Vectorization: Applies TfidfVectorizer to convert text to vectors.

Similarity Scoring: Uses cosine_similarity to compare resume and JD content.

Result Display: Shows score, feedback, and optional warning or balloon animation.



