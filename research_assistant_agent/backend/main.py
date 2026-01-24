from fastapi import FastAPI
from pydantic import BaseModel
from langgraph.graph import StateGraph
from typing import TypedDict

from tools import duckduckgo_search, read_pdf_from_url
from agent import call_gemini
from prompts import RESEARCH_PROMPT

app = FastAPI()


class ResearchState(TypedDict):
    query: str
    is_pdf: bool
    content: str
    result: str

def router_node(state: ResearchState):
    return state

def route(state: ResearchState):
    return "pdf" if state["is_pdf"] else "search"

def search_node(state: ResearchState):
    results = duckduckgo_search(state["query"])
    combined = "\n\n".join(
        [f"Title: {r['title']}\nSnippet: {r['body']}\nSource: {r['url']}"
         for r in results]
    )
    return {"content": combined}


def pdf_node(state: ResearchState):
    text = read_pdf_from_url(state["query"])
    return {"content": text}

def llm_node(state: ResearchState):
    if not state.get("content"):
        return {"result": "❌ No content found to analyze."}

    prompt = RESEARCH_PROMPT.format(content=state["content"][:15000])
    output = call_gemini(prompt)
    return {"result": output}

graph = StateGraph(ResearchState)

graph.add_node("router", router_node)
graph.add_node("search", search_node)
graph.add_node("pdf", pdf_node)
graph.add_node("llm", llm_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    route,          # 👈 routing function
    {
        "search": "search",
        "pdf": "pdf"
    }
)

graph.add_edge("search", "llm")
graph.add_edge("pdf", "llm")

graph.set_finish_point("llm")

research_graph = graph.compile()


class ResearchRequestFastAPI(BaseModel):
    query: str
    is_pdf: bool = False

@app.post("/research")
def research(req: ResearchRequestFastAPI):
    result = research_graph.invoke({
        "query": req.query,
        "is_pdf": req.is_pdf
    })
    return result

