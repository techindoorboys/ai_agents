from langgraph.graph import StateGraph
from typing import TypedDict
from .tools import fetch_webpage
from .llm import summarize_text

class AgentState(TypedDict):
    url: str
    page_text: str
    summary: str

def browse_node(state: AgentState):
    page_text = fetch_webpage(state["url"])
    return {"page_text": page_text}


def summarize_node(state: AgentState):
    summary = summarize_text(state["page_text"])
    return {"summary": summary}


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("browse", browse_node)
    graph.add_node("summarize", summarize_node)

    graph.set_entry_point("browse")
    graph.add_edge("browse", "summarize")

    return graph.compile()
