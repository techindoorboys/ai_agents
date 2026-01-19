import os
from google import genai
from google.genai import types

def get_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY is not set")

    return genai.Client(api_key=api_key)


def summarize_text(text: str) -> str:
    client = get_client()

    prompt = f"""
    Summarize the following webpage content in a clear, concise manner.
    Focus on key points and avoid unnecessary details.

    Provide latest highlights of the page

    CONTENT:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=400,
        ),
    )

    return response.text.strip()
