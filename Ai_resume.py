from PIL import Image
import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    pdf = PdfReader(file)    #we are creating the pdf object for pdfReader() class
    text=" "
    for page in pdf.pages:
        text+=page.extract_text()
    return text

def rank_resumes(job_description,resumes):
    documents=[job_description]+resumes
    vectorizer=TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    jd_vector=vectors[0]
    resume_vector=vectors[1:]
    cosine_similarities=cosine_similarity([jd_vector],resume_vector).flatten()
    return cosine_similarities

#Streamlit app

st.title("AI Based Resume Screening and Ranking System")
#Job description input
# Display an image using Pillow
img = Image.open(r"C:\Users\helpd\OneDrive\Desktop\AI based resume\bg.jpg")
st.image(img)
st.header("Job Description")
job_description = st.text_area("Enter the job description")
def set_background():
    background_style = """
    <style>
    .stApp {
        background-image: url("https://unsplash.com/photos/man-writing-on-paper-OQMZwNd3ThU");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

set_background()

#File uploader
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload Pdf files",type=["pdf"],accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("Ranking Resumes")
    resumes=[]
    for file in uploaded_files:
        text=extract_text_from_pdf(file)
        resumes.append(text)
    #Rank Resumes
    scores = rank_resumes(job_description,resumes)
    #Display scores
    results = pd.DataFrame({"Resume":[file.name for file in uploaded_files],"Score":scores})
    results = results.sort_values(by="Score",ascending = False)
    st.write(results)
    
    