from fastapi import FastAPI
from .agent import pdf_agent
from .schemas import PDFRequest

app = FastAPI(title="PDF Summarizer Agent")


@app.post("/summarize")
def summarize_pdf(req: PDFRequest):
    result = pdf_agent.invoke({"pdf_url": req.pdf_url})
    return {"summary": result["result"]}
