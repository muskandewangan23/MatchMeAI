import streamlit as st
import pandas as pd
import io
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import load_csv_with_encoding, extract_text_from_pdf

st.set_page_config(page_title="Job Resume Matching", layout="wide")
st.title("🔍 Job Resume Matching with AI")
st.markdown("Upload resumes and job descriptions to find the best candidate-job matches.")

tab1, tab2 = st.tabs(["📄 Text Resume", "📎 PDF Resumes"])

with tab1:
    job_file = st.file_uploader("Upload Job Description CSV", type=["csv"], key="text_csv")
    resume_text = st.text_area("Paste Your Resume Text Here")

    if job_file and resume_text:
        jobs_df = load_csv_with_encoding(job_file)
        job_texts = jobs_df.iloc[:, 1].astype(str).tolist()
        job_titles = jobs_df.iloc[:, 0].astype(str).tolist()
        corpus = job_texts + [resume_text]

        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(corpus)
        similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

        result_df = pd.DataFrame({
            'Job Title': job_titles,
            'Match %': (similarities * 100).round(2)
        }).sort_values(by='Match %', ascending=False)

        st.subheader("🔍 Top Matching Jobs")
        st.dataframe(result_df)

with tab2:
    pdfs = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)
    job_file_2 = st.file_uploader("Upload Job Description CSV", type=["csv"], key="pdf_csv")

    if pdfs and job_file_2:
        jobs_df = load_csv_with_encoding(job_file_2)
        job_texts = jobs_df.iloc[:, 1].astype(str).tolist()
        job_titles = jobs_df.iloc[:, 0].astype(str).tolist()

        for pdf in pdfs:
            resume_text = extract_text_from_pdf(pdf)
            corpus = job_texts + [resume_text]

            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(corpus)
            similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

            result_df = pd.DataFrame({
                'Job Title': job_titles,
                'Match %': (similarities * 100).round(2)
            }).sort_values(by='Match %', ascending=False)

            st.markdown(f"### 📄 Matches for `{pdf.name}`")
            st.dataframe(result_df.head(5))
