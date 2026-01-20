OVERVIEW

This project implements an end-to-end AI agent that takes a PDF URL as input and generates high-quality insights such as:

Abstract

Executive Summary

Key Insights

Actionable Takeaways

The system is intentionally designed to be simple, extensible, and production-ready, using modern GenAI tooling while remaining easy to understand.

The project uses Gemini LLM, LangGraph for orchestration, FastAPI for backend, and Streamlit for UI, and is fully compatible with GitHub Codespaces.

KEY FEATURES

Accepts a public PDF URL (e.g. arXiv papers)

Extracts text directly from the PDF

Uses Gemini LLM for structured summarization

Agent orchestration using LangGraph

REST API backend using FastAPI

Simple UI using Streamlit

Environment management using dotenv

Dependency management using UV

Designed for GitHub Codespaces out of the box

TECH STACK

LLM

Google Gemini (gemini-1.5-flash)

Agent Orchestration

LangGraph

Backend

FastAPI

Uvicorn

Frontend

Streamlit

Utilities

pypdf (PDF parsing)

requests (HTTP)

BeautifulSoup (optional webpage extraction)

python-dotenv (environment variables)

Package Management

UV (Astral)

Runtime Environment

GitHub Codespaces

Python 3.11+

PROJECT STRUCTURE

pdf-summarizer-agent/
|
|-- backend/
| |-- app/
| | |-- main.py # FastAPI entrypoint
| | |-- agent.py # LangGraph agent logic
| | |-- pdf_utils.py # PDF download & text extraction
| | |-- web_utils.py # Web scraping (optional)
| | |-- schemas.py # API request models
| |
| |-- pyproject.toml # Backend dependencies
|
|-- frontend/
| |-- app.py # Streamlit UI
| |-- pyproject.toml # Frontend dependencies
|
|-- .env # Environment variables
|-- .gitignore
|-- README.md

ARCHITECTURE OVERVIEW

User provides a PDF URL via Streamlit UI

Streamlit sends request to FastAPI backend

FastAPI invokes LangGraph agent

LangGraph agent:

Downloads PDF

Extracts text

Sends content to Gemini LLM

Gemini generates structured insights

Backend returns response to UI

UI displays formatted insights

LANGGRAPH AGENT DESIGN

The agent uses a single-node LangGraph workflow for clarity and simplicity.

State Definition:

pdf_url (input)

result (output)

Flow:

Entry Node: summarize

Exit Node: summarize

This structure makes it easy to later extend into:

Multi-node pipelines

Chunking nodes

RAG pipelines

Web enrichment nodes

ENVIRONMENT SETUP

Create a Google Gemini API key:
https://aistudio.google.com/app/apikey

Create a .env file in the project root:

GOOGLE_API_KEY=your_api_key_here

SETTING UP THE BACKEND

Navigate to backend directory:

cd backend

Create virtual environment:

uv venv
source .venv/bin/activate

Install dependencies:

uv pip install -r pyproject.toml

Run the backend server:

uvicorn app.main:app --host 0.0.0.0 --port 8000

In GitHub Codespaces:

Open the Ports tab

Make port 8000 public

API Endpoint:
POST /summarize

Request body:

{
"pdf_url": "https://arxiv.org/pdf/1706.03762.pdf
"
}

SETTING UP THE FRONTEND

Navigate to frontend directory:

cd frontend

Create virtual environment:

uv venv
source .venv/bin/activate

Install dependencies:

uv pip install -r pyproject.toml

Run Streamlit app:

streamlit run app.py --server.port 8501 --server.address 0.0.0.0

In GitHub Codespaces:

Open the Ports tab

Make port 8501 public

SAMPLE PDF URLS FOR TESTING

Attention Is All You Need (Transformers):
https://arxiv.org/pdf/1706.03762.pdf

GPT-4 Technical Report:
https://arxiv.org/pdf/2303.08774.pdf

Chain-of-Thought Prompting:
https://arxiv.org/pdf/2201.11903.pdf

EXPECTED OUTPUT FORMAT

The agent produces structured text including:

Abstract

Executive Summary

Key Insights (bullet points)

Actionable Takeaways

The output is optimized for:

Research understanding

Executive summaries

Technical reviews

DESIGN DECISIONS

Gemini chosen for simplicity and quality

LangGraph chosen for explicit agent state control

UV chosen for fast and clean dependency management

Streamlit chosen for rapid UI iteration

FastAPI chosen for production-ready APIs

KNOWN LIMITATIONS

Very large PDFs may require chunking

No citation tracking yet

No PDF upload (URL only)

No authentication or rate limiting

RECOMMENDED EXTENSIONS

PDF chunking with map-reduce summarization

Citation extraction per insight

Multi-PDF comparison

Export summaries to Markdown / PDF

RAG with vector embeddings

Streaming responses

Retry and fallback LLM logic

Dockerized deployment

WHO IS THIS PROJECT FOR

AI / ML Engineers

GenAI Developers

Research Engineers

Product Managers learning AI

Anyone building LLM agents

LICENSE

MIT License (recommended)

AUTHOR NOTES

This project is intentionally built to be:

Easy to understand

Easy to extend

Easy to explain in interviews

Suitable for GitHub portfolios
