from fastapi import FastAPI
from .api import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Web Browsing AI Agent")

app.include_router(router)
