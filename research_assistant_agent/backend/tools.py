from ddgs import DDGS
from pypdf import PdfReader
import requests
import io

from ddgs import DDGS

def duckduckgo_search(query: str, max_results: int = 5):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "body": r.get("body")
            })

    return results


def read_pdf_from_url(url: str) -> str:
    response = requests.get(url)
    pdf_file = io.BytesIO(response.content)
    reader = PdfReader(pdf_file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

if __name__ == "__main__":
    print(duckduckgo_search("LLMs in healthcare"))
