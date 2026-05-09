import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import extract_text, semantic_score, skill_score
from auth import login, check_login
from history import save_history, load_history

st.set_page_config(page_title="Smart ATS System", layout="wide")

# =========================
# LOGIN SYSTEM
# =========================
login()

if not check_login():
    st.stop()

user = st.session_state["user"]

# =========================
# HEADER
# =========================
st.title("🧠 AI Resume Screening System (Final Dashboard)")

st.sidebar.success(f"Logged in as: {user}")

# Role-based access
is_admin = (user == "admin")

# =========================
# JOB INPUT
# =========================
job_text = st.text_area("📄 Enter Job Description")

# =========================
# RESUME UPLOAD
# =========================
files = st.file_uploader(
    "📤 Upload Resumes (PDF only)",
    type=["pdf"],
    accept_multiple_files=True
)

results = []

# =========================
# RUN ATS
# =========================
if st.button("🚀 Run AI Screening"):

    if not job_text or not files:
        st.error("Please provide job description and resumes")
        st.stop()

    for file in files:

        text = extract_text(file)

        sem_score = semantic_score(text, job_text)
        skills = skill_score(text)

        final_score = (sem_score * 0.7) + (skills * 6)

        status = "Shortlisted" if final_score >= 60 else "Rejected"

        explanation = f"""
        AI Explanation:
        - Semantic Match Score: {round(sem_score,2)}
        - Skills Matched: {skills}
        - Final Decision: {status}
        """

        results.append({
            "Resume": file.name,
            "Score": round(final_score, 2),
            "Status": status,
            "Skills": skills,
            "Explanation": explanation
        })

        # Save history
        save_history({
            "user": user,
            "resume": file.name,
            "score": final_score,
            "status": status
        })

    df = pd.DataFrame(results)
    df = df.sort_values("Score", ascending=False)

    # =========================
    # RESULTS TABLE
    # =========================
    st.subheader("📊 Candidate Ranking")
    st.dataframe(df, use_container_width=True)

    # =========================
    # TOP CANDIDATE
    # =========================
    st.subheader("🏆 Top Candidate")
    st.success(df.iloc[0]["Resume"])

    st.info(df.iloc[0]["Explanation"])

    # =========================
    # SCORE CHART
    # =========================
    st.subheader("📈 Score Distribution")

    st.bar_chart(df.set_index("Resume")["Score"])

    # =========================
    # PIE CHART
    # =========================
    st.subheader("🥧 Hiring Decision Ratio")

    fig, ax = plt.subplots()
    df["Status"].value_counts().plot.pie(
        autopct="%1.1f%%",
        ax=ax
    )
    st.pyplot(fig)

    # =========================
    # SKILL CHART
    # =========================
    st.subheader("📌 Skill Strength Analysis")

    st.bar_chart(df.set_index("Resume")["Skills"])

    # =========================
    # DOWNLOAD REPORT
    # =========================
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Full Report",
        csv,
        "ats_report.csv",
        "text/csv"
    )

# =========================
# HISTORY SECTION (ADMIN ONLY)
# =========================
st.divider()

st.subheader("📜 Screening History")

history_df = load_history()

if not history_df.empty:

    if is_admin:
        st.dataframe(history_df, use_container_width=True)
    else:
        st.dataframe(history_df[history_df["user"] == user], use_container_width=True)

    st.line_chart(history_df.groupby("user")["score"].mean())

else:
    st.info("No history available yet.")