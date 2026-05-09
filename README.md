# 🧠 AI Resume Screening System (ATS Project)
An AI-powered Resume Screening and Candidate Ranking system built using Python and Streamlit.  
This project simulates an **Applicant Tracking System (ATS)** used in real HR and recruitment platforms.
## 🚀 Project Overview
The AI Resume Screening System automatically analyzes resumes and compares them with job descriptions.  
It ranks candidates based on relevance, skills, and semantic similarity using AI techniques.
This helps recruiters:
- Save time in manual screening
- Improve hiring accuracy
- Identify best-fit candidates quickly
## 🎯 Problem Statement
Recruiters often receive hundreds or thousands of resumes for a single job.  
Manually screening each resume is:
- Time-consuming
- Error-prone
- Biased
👉 This project automates the process using AI and NLP.
## 🧠 Features
- 🔐 Role-based Login System (Admin & HR)
- 📄 PDF Resume Upload Support
- 🧠 AI-based Semantic Matching (Sentence-BERT)
- 📊 Candidate Ranking System
- 📌 Skill Extraction Engine
- 🧾 Explainable AI (Why shortlisted/rejected)
- 📜 Screening History Tracking
- 📈 Charts & Visual Analytics
  - Score distribution bar chart
  - Hiring decision pie chart
  - Skill analysis chart
- 📥 Downloadable CSV Report
## 🏗️ Tech Stack
- Python 3.x
- Streamlit (Frontend Dashboard)
- Pandas (Data Handling)
- Matplotlib (Visualization)
- pdfplumber (PDF extraction)
- python-docx (DOCX support)
- SentenceTransformers (AI NLP model)
- Scikit-learn (Similarity scoring)
🔐 Login Credentials
Admin Login
Username: admin
Password: admin123
HR Login
Username: hr
Password: hr123
📊 How It Works
Upload resumes (PDF format)
Enter job description
System extracts text from resumes
AI calculates:
Semantic similarity
Skill match score
Candidates are ranked automatically
Results are displayed with charts and explanations
History is stored for future analysis
🧠 AI Logic
Final Score Formula:
Final Score = (Semantic Similarity × 0.7) + (Skill Score × 6)
Semantic similarity → AI-based text matching
Skill score → keyword-based skill detection
📊 Charts Included
📈 Resume Score Distribution
🥧 Hiring Decision Ratio
📌 Skill Strength Analysis
Screenshots
Dashboard
<img width="1350" height="607" alt="Screenshot 2026-05-10 003347" src="https://github.com/user-attachments/assets/73cc47f5-0dd1-4e3d-bbcd-fabe99aea8c6" />
Score Distribution
<img width="1364" height="714" alt="Screenshot 2026-05-10 003408" src="https://github.com/user-attachments/assets/164e611c-6ee6-4427-9d27-5690bfddb066" />
Hiring Detection Ratio
<img width="1362" height="713" alt="Screenshot 2026-05-10 003426" src="https://github.com/user-attachments/assets/dd3d6c08-62c1-4007-afc3-f335d6c491ff" />
Skill strength Analysis
<img width="1361" height="675" alt="Screenshot 2026-05-10 003442" src="https://github.com/user-attachments/assets/d5f038e9-4643-4b85-b9f5-96a1e35e0e0c" />
Screening History
<img width="1345" height="645" alt="Screenshot 2026-05-10 003503" src="https://github.com/user-attachments/assets/db09bd4b-c7ab-40d6-b919-b29f3a12bfe2" />
💡 Future Improvements
Resume PDF highlight viewer (NER-based)
AI chatbot for recruiter assistance
PostgreSQL database integration
Multi-company ATS system
React frontend upgrade
Cloud deployment (AWS / Render)
🎓 Learning Outcomes
This project demonstrates:
Natural Language Processing (NLP)
Machine Learning similarity models
Real-world HR tech workflow
Dashboard development using Streamlit
Explainable AI systems
👨‍💻 Author
Developed as a Python + AI/ML project for learning and placement portfolio.
