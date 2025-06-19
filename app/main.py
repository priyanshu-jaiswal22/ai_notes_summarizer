import streamlit as st
import PyPDF2
import requests
import os
from utils.helpers import extract_text_from_pdf, summarize_text

st.set_page_config(page_title="AI Notes Summarizer", layout="wide")
st.title("📄 AI-Powered Notes Summarizer using Azure OpenAI")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
input_text = st.text_area("Or paste your notes here")

if st.button("Summarize"):
    text_to_summarize = ""
    if uploaded_file:
        text_to_summarize = extract_text_from_pdf(uploaded_file)
    elif input_text:
        text_to_summarize = input_text
    else:
        st.warning("Please upload a file or paste text to summarize.")

    if text_to_summarize:
        with st.spinner("Summarizing..."):
            summary = summarize_text(text_to_summarize)
            st.subheader("Summary")
            st.write(summary)