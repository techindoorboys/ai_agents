import requests
from pypdf import PdfReader
from io import BytesIO


def extract_text_from_pdf_url(pdf_url: str) -> str:
    response = requests.get(pdf_url, timeout=30)
    response.raise_for_status()

    reader = PdfReader(BytesIO(response.content))
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text
