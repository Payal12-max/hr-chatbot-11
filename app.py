'''import streamlit as st
from chatbot_logic import evaluate_answer
from question_gen import generate_questions
from storage import save_to_csv

st.title("🧑‍💼 HR Chatbot for Candidate Screening")

candidate_name = st.text_input("Enter your name:")
job_role = st.selectbox("Select the job role:", ["Software Engineer", "Data Analyst", "Marketing Executive", "Custom Role"])

if job_role == "Custom Role":
    job_role = st.text_input("Enter the job role:")

if st.button("Start Screening"):
    st.session_state.questions = generate_questions(job_role)
    st.session_state.answers = []
    st.session_state.scores = []

if 'questions' in st.session_state:
    for i, q in enumerate(st.session_state.questions):
        st.subheader(f"Q{i+1}: {q}")
        ans = st.text_area(f"Your answer for question {i+1}", key=f"answer_{i}")
        if st.button(f"Evaluate Q{i+1}", key=f"btn_{i}"):
            result = evaluate_answer(q, ans)
            st.write(result)
            st.session_state.answers.append(ans)
            st.session_state.scores.append(result)

    if st.button("Submit All"):
        save_to_csv(candidate_name, job_role, st.session_state.questions, st.session_state.answers, st.session_state.scores)
        st.success("Responses saved and submitted!")'''



import streamlit as st
import os
from chatbot_logic import evaluate_answer
from question_gen import generate_questions
from storage import save_to_csv

st.title("🧑‍💼 HR Chatbot for Candidate Screening")

candidate_name = st.text_input("Enter your name:")
job_role = st.selectbox("Select the job role:", ["Software Engineer", "Data Analyst", "Marketing Executive", "Custom Role"])

if job_role == "Custom Role":
    job_role = st.text_input("Enter the job role:")

if st.button("Start Screening"):
    st.session_state.questions = generate_questions(job_role)
    st.session_state.answers = []
    st.session_state.scores = []

if 'questions' in st.session_state:
    for i, q in enumerate(st.session_state.questions):
        st.subheader(f"Q{i+1}: {q}")
        ans = st.text_area(f"Your answer for question {i+1}", key=f"answer_{i}")
        if st.button(f"Evaluate Q{i+1}", key=f"btn_{i}"):
            result = evaluate_answer(q, ans)
            st.write(result)
            st.session_state.answers.append(ans)
            st.session_state.scores.append(result)

    if st.button("Submit All"):
            print("Questions:", st.session_state.questions)
            print("Answers:", st.session_state.answers)
            print("Scores:", st.session_state.scores)

            if not st.session_state.answers or not st.session_state.scores:
                st.error("⚠️ Please evaluate all questions before submitting.")
            else:
                save_to_csv(candidate_name, job_role, st.session_state.questions, st.session_state.answers, st.session_state.scores)
                st.success("✅ Responses saved to CSV!")

                file_path = "candidate_results.csv"
                if os.path.exists(file_path):
                    with open(file_path, "rb") as f:
                        st.download_button(
                            label="📥 Download Your Submission",
                            data=f,
                            file_name="your_submission.csv",
                            mime="text/csv"
                        )


