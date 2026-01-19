from fastapi import APIRouter
from .schemas import BrowseRequest, BrowseResponse
from .agent.graph import build_graph

router = APIRouter()
graph = build_graph()

@router.post("/browse", response_model=BrowseResponse)
def browse(req: BrowseRequest):
    result = graph.invoke({
        "url": req.url
    })
    return {"summary": result["summary"]}
