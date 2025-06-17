# MatchMeAI: Enhancing Job Screening with AI and Data Intelligence

**MatchMeAI** is a web application that uses Natural Language Processing (NLP) to smartly match resumes with job descriptions based on content similarity using AI.
## 🔍 Features

- Upload multiple job descriptions (CSV)
- Match resumes using either:
  - Plain text
  - PDF resumes
- View top matching jobs with confidence scores

## 💡 Technologies Used

- Streamlit (for the web interface)
- PyPDF2 (to extract text from PDF resumes)
- Scikit-learn (TF-IDF + cosine similarity)
- Pandas (data handling)

## 🔗 Live Demo

Try the app here 👉 [MatchMeAI](https://matchmeai-b6z5x3zsylrhzhpecsw6fr.streamlit.app)

## 🚀 How to Run Locally

Make sure Python is installed. Then in the terminal:

```bash
pip install -r requirements.txt
streamlit run app.py

