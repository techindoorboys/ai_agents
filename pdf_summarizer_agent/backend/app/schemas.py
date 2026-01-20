from pydantic import BaseModel


class PDFRequest(BaseModel):
    pdf_url: str
