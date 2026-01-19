import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="Web Page Summarizer", layout="centered")

st.title("🌐 Web Page Summarizer (Gemini LLM)")

url = st.text_input("Enter website URL")

if st.button("Summarize"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Fetching and summarizing..."):
            response = requests.post(
                f"{BACKEND_URL}/browse",
                json={"url": url},
                timeout=60
            )

            if response.status_code == 200:
                summary = response.json()["summary"]
                st.success("Summary generated")
                st.write(summary)
            else:
                st.error("Failed to summarize the page")
