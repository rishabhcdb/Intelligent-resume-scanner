# resume_parser.py
from pdfminer.high_level import extract_text
import re

def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {e}"
