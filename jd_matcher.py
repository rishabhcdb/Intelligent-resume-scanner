# jd_matcher.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from spacy.cli import download

# Load SpaCy model with fallback if not downloaded
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])

def calculate_similarity(resume_text, jd_text):
    resume_clean = preprocess(resume_text)
    jd_clean = preprocess(jd_text)
    
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume_clean, jd_clean])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    
    return round(score * 100, 2)
