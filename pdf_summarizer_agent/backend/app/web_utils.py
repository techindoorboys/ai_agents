import requests
from bs4 import BeautifulSoup


def scrape_webpage(url: str, max_chars: int = 3000) -> str:
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        return text[:max_chars]
    except Exception:
        return ""
