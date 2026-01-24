import streamlit as st
import requests

st.set_page_config(page_title="Research Assistant", layout="wide")

st.title("📚 Research Assistant with Citations")

query = st.text_input("Enter Research Question or PDF URL")
is_pdf = st.checkbox("Is this a PDF URL?")

if st.button("Generate Research"):
    with st.spinner("Thinking..."):
        response = requests.post(
            "http://localhost:8000/research",
            json={"query": query, "is_pdf": is_pdf}
        )
        data = response.json()
        st.markdown(data["result"])
