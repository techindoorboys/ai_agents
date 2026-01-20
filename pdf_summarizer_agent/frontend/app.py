import streamlit as st
import requests

st.set_page_config(page_title="PDF Summarizer Agent")

st.title("📄 PDF Summarizer Agent (Gemini)")

pdf_url = st.text_input("Enter PDF URL")

if st.button("Generate Insights") and pdf_url:
    with st.spinner("Analyzing PDF..."):
        res = requests.post(
            "http://localhost:8000/summarize",
            json={"pdf_url": pdf_url},
            timeout=120
        )

        if res.status_code == 200:
            st.markdown(res.json()["summary"])
        else:
            st.error("Failed to summarize PDF")
