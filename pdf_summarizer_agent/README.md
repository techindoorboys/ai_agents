# 📄 PDF Summarizer Agent (Gemini + LangGraph)

An end-to-end **AI-powered PDF Summarizer Agent** that extracts high-quality insights from research papers and documents using **Google Gemini**, **LangGraph**, **FastAPI**, and **Streamlit**.

This project is designed to be **simple, extensible, production-oriented**, and fully compatible with **GitHub Codespaces**.

---

## ✨ Features

- Accepts a **PDF URL** as input
- Extracts text directly from PDFs
- Generates:
  - Abstract
  - Executive Summary
  - Key Insights
  - Actionable Takeaways
- Uses **Gemini LLM only** (no OpenAI dependency)
- Agent orchestration with **LangGraph**
- Backend API with **FastAPI**
- Simple UI using **Streamlit**
- Environment management with **dotenv**
- Fast dependency management with **UV**
- Ready-to-use in **GitHub Codespaces**

---

## 🧠 Architecture Overview

```text
User (Streamlit UI)
        |
        v
FastAPI Backend
        |
        v
LangGraph Agent
        |
        v
PDF Download → Text Extraction → Gemini LLM
        |
        v
Structured Insights Response

## 🛠 Tech Stack

---

### LLM
- Google Gemini (`gemini-1.5-flash`)

### Agent Framework
- LangGraph
- LangChain Core

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Utilities
- pypdf (PDF parsing)
- requests
- BeautifulSoup (web scraping – optional)
- python-dotenv

### Package Manager
- UV (Astral)

### Runtime
- Python 3.11+
- GitHub Codespaces

---

## 📁 Project Structure

```bash
pdf-summarizer-agent/
│
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entrypoint
│   │   ├── agent.py         # LangGraph agent logic
│   │   ├── pdf_utils.py     # PDF download & text extraction
│   │   ├── web_utils.py     # Web scraping (optional)
│   │   └── schemas.py       # Request/response models
│   └── pyproject.toml
│
├── frontend/
│   ├── app.py               # Streamlit UI
│   └── pyproject.toml
│
├── .env
├── .gitignore
└── README.md
```

## 🔑 Environment Setup

1. Get Gemini API Key

Create an API key from:

https://aistudio.google.com/app/apikey

2. Create .env file (project root)
GOOGLE_API_KEY=your_gemini_api_key_here

## 🚀 Backend Setup (FastAPI + LangGraph)
### Navigate to backend
cd backend

### Create virtual environment
uv venv
source .venv/bin/activate

### Install dependencies
uv pip install -r pyproject.toml

###  Run backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000

### GitHub Codespaces

* Open Ports tab

* Set port 8000 to Public

## 🌐 API Usage
###  Endpoint
```bash
POST /summarize
```

Request Body
```json
{
  "pdf_url": "https://arxiv.org/pdf/1706.03762.pdf"
}
```
```json
Response
{
  "summary": "Abstract...\n\nExecutive Summary...\n\nKey Insights...\n\nActionable Takeaways..."
}
```

## 🎨 Frontend Setup (Streamlit)
### Navigate to frontend
```bash
cd frontend
```

### Create virtual environment
```bash
uv venv
source .venv/bin/activate
```
Install dependencies
```bash
uv pip install -r pyproject.toml
```

Run Streamlit app
```bash
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```
### GitHub Codespaces

* Open Ports tab
* Set port 8501 to Public

## 📄 Sample PDF URLs for Testing

Attention Is All You Need (Transformers)
```arduino
https://arxiv.org/pdf/1706.03762.pdf
```

## 🧩 LangGraph Agent Design

* Uses a TypedDict-based state
* Single-node graph for clarity
* Easy to extend into multi-node workflows

### Current State Keys

* pdf_url (input)
* result (output)

## ⚠️ Known Limitations

* Large PDFs may require chunking
* No citation extraction
* URL-based PDFs only (no file upload yet)
* No authentication or rate limiting

## 🔮 Recommended Enhancements

* PDF chunking + map-reduce summarization
* Citation-aware insights
* Multi-PDF comparison
* RAG with vector embeddings
* Streaming responses
* PDF upload support
* Docker + CI/CD pipeline

