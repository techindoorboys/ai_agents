from pydantic import BaseModel

class BrowseRequest(BaseModel):
    url: str

class BrowseResponse(BaseModel):
    summary: str
