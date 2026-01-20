import os
from langgraph.graph import StateGraph
from langchain_core.messages import HumanMessage
import google.generativeai as genai
from dotenv import load_dotenv
from .pdf_utils import extract_text_from_pdf_url
from typing import TypedDict


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

class AgentState(TypedDict):
    pdf_url: str
    result: str

def summarize_node(state: AgentState):
    pdf_text = extract_text_from_pdf_url(state["pdf_url"])

    prompt = f"""
You are an expert research analyst.

Generate:
1. Abstract
2. Executive Summary
3. Key Insights (bullets)
4. Actionable Takeaways

PDF Content:
{pdf_text[:15000]}
"""

    response = model.generate_content(prompt)

    # IMPORTANT: return dict that updates state
    return {"result": response.text}


graph = StateGraph(AgentState)

graph.add_node("summarize", summarize_node)

graph.set_entry_point("summarize")
graph.set_finish_point("summarize")

pdf_agent = graph.compile()