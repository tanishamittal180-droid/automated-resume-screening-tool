import pdfplumber
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

SKILLS = ["python","sql","ml","ai","pandas","numpy","flask","api","git"]

def extract_text(file):
    with pdfplumber.open(file) as pdf:
        return " ".join([p.extract_text() or "" for p in pdf.pages]).lower()

def semantic_score(resume, job):
    emb1 = model.encode(resume, convert_to_tensor=True)
    emb2 = model.encode(job, convert_to_tensor=True)
    return float(util.cos_sim(emb1, emb2)[0][0]) * 100

def skill_score(text):
    return sum(1 for s in SKILLS if s in text)

def explain_score(sem, skills, missing):
    return f"""
    AI Analysis:
    - Semantic Match: {round(sem,2)}%
    - Skills Matched: {skills}
    - Missing Skills: {len(missing)}
    - Final Decision based on weighted AI scoring model
    """