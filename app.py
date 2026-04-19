import streamlit as st
from resume_parser import extract_resume_text
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
st.write("Upload your resume PDF and paste the job description.")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

job_description = st.text_area("Paste the Job Description Here")

if st.button("Analyze Resume"):

    if uploaded_file is not None and job_description != "":

        with st.spinner("Reading and checking your resume..."):

            resume_text = extract_resume_text(uploaded_file)

            result = analyze_resume(resume_text, job_description)

        st.subheader("Result")
        st.write(result)

    else:
        st.warning("Please upload a resume and paste the job description.")