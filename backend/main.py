from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import tempfile
import requests
import re

app = FastAPI()

# React frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Extract text from uploaded PDF
# -----------------------------
def extract_pdf_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# -----------------------------
# Basic ATS Rule Score
# -----------------------------
def ats_score(resume_text):
    score = 50

    keywords = [
        "python", "java", "c++", "sql", "react",
        "projects", "internship", "github",
        "api", "teamwork", "leadership", "femboy"
    ]

    found = sum(1 for k in keywords if k.lower() in resume_text.lower())
    score += found * 4

    if len(resume_text.split()) > 250:
        score += 5

    if "education" in resume_text.lower():
        score += 5

    return min(score, 100)

# -----------------------------
# Ask Gemma 4 E4B
# -----------------------------
def ask_gemma(resume_text, score):
    prompt = f"""
You are an expert Resume Reviewer.

Analyze this fresher resume.

Return in clean markdown with headings:

ATS Score: {score}/100

1. Strengths
2. Weaknesses
3. Missing Skills
4. Rewrite Summary Section
5. Improve 3 Bullet Points
6. 5 Interview Questions
7. Final Verdict

Resume:
{resume_text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma4:e4b",
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    return response.json()["response"]

# -----------------------------
# Main Route
# -----------------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(await file.read())
        path = temp.name

    text = extract_pdf_text(path)

    if not text:
        return {"error": "Could not extract text from PDF."}

    score = ats_score(text)
    analysis = ask_gemma(text, score)

    return {
        "score": score,
        "analysis": analysis
    }