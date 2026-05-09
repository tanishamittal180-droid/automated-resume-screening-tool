import os
import pandas as pd
import pdfplumber
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE = os.path.dirname(os.path.abspath(__file__))

job_path = os.path.join(BASE, "data", "job_description.txt")
resume_dir = os.path.join(BASE, "resumes")
output_dir = os.path.join(BASE, "outputs")
output_file = os.path.join(output_dir, "ranking.csv")

os.makedirs(output_dir, exist_ok=True)

# ---------------- JOB ----------------
with open(job_path, "r", encoding="utf-8") as f:
    job_text = f.read().lower()

# ---------------- EXTRACT ----------------
def extract_text(path):
    if path.endswith(".pdf"):
        with pdfplumber.open(path) as pdf:
            return " ".join([p.extract_text() or "" for p in pdf.pages]).lower()

    if path.endswith(".docx"):
        doc = Document(path)
        return " ".join([p.text for p in doc.paragraphs]).lower()

    return ""

# ---------------- SKILL SCORING ----------------
SKILLS = ["python","sql","machine learning","pandas","numpy","flask","api","git"]

def skill_score(text):
    return sum(1 for s in SKILLS if s in text)

# ---------------- PROCESS ----------------
results = []

for file in os.listdir(resume_dir):

    path = os.path.join(resume_dir, file)
    text = extract_text(path)

    if not text.strip():
        continue

    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform([text, job_text])

    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]

    skills_matched = skill_score(text)

    final_score = (
        (similarity * 60) +
        (skills_matched * 5)
    )

    explanation = f"Matched Skills: {skills_matched}"

    status = "Shortlisted" if final_score >= 50 else "Rejected"

    results.append([
        file,
        round(final_score, 2),
        status,
        explanation
    ])

# ---------------- SAVE ----------------
df = pd.DataFrame(
    results,
    columns=["Resume", "Score", "Status", "Explanation"]
)

df = df.sort_values("Score", ascending=False)

df.to_csv(output_file, index=False)

print("\n✅ ATS Completed")
print(df)