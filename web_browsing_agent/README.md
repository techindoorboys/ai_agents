# 🌐 Web Browsing AI Agent (Gemini-powered)

A production-ready **Web Browsing AI Agent** that fetches live web pages and generates concise summaries using **Google Gemini LLM**.  
The system is built with **FastAPI, LangGraph, Streamlit, and uv**, and is designed to run seamlessly in **GitHub Codespaces**.

---

## 🚀 Features

- 🔍 Fetches real web pages using `requests` + `BeautifulSoup`
- 🧠 Summarizes content using **Gemini 1.5 Flash**
- 🧩 Agent orchestration using **LangGraph**
- ⚡ FastAPI backend with clean API contracts
- 🎨 Simple Streamlit UI
- 🔐 Secure environment variable management using `.env`
- 🧑‍💻 Optimized for **GitHub Codespaces**
- 🏗️ Clean, extensible architecture (easy to add search, crawl, QA)

---

## 🏗️ Architecture Overview

┌─────────────┐
│ Streamlit │ ← UI
└──────┬──────┘
│ HTTP
┌──────▼──────┐
│ FastAPI │ ← Backend API
└──────┬──────┘
│
┌──────▼────────────┐
│ LangGraph Agent │
│ ├─ Fetch Page │
│ └─ Summarize │
└──────┬────────────┘
│
┌──────▼────────────┐
│ Gemini 1.5 Flash │ ← LLM
└───────────────────┘

yaml
Copy code

---

## 📂 Project Structure

web_browsing_agent/
├── backend/
│ ├── app/
│ │ ├── agent/
│ │ │ ├── graph.py # LangGraph workflow
│ │ │ ├── tools.py # Web fetching logic
│ │ │ └── llm.py # Gemini client
│ │ ├── api.py # FastAPI routes
│ │ ├── schemas.py # Pydantic models
│ │ └── main.py # App entry point
│ └── pyproject.toml
│
├── frontend/
│ ├── app.py # Streamlit UI
│ └── pyproject.toml
│
├── .env # Environment variables
├── .gitignore
└── README.md

yaml
Copy code

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | Python 3.11+ |
| Backend | FastAPI |
| Frontend | Streamlit |
| Agent Framework | LangGraph |
| LLM | Google Gemini 1.5 Flash |
| Package Manager | `uv` |
| Web Parsing | BeautifulSoup |
| Environment Mgmt | python-dotenv |
| Deployment | GitHub Codespaces |

---

## 🔑 Environment Variables

Create a `.env` file at the **project root**:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
BACKEND_URL=http://localhost:8000
⚠️ Do NOT commit .env to GitHub
Add it to .gitignore.

▶️ Running the Project (GitHub Codespaces)
1️⃣ Install uv (once)
bash
Copy code
pip install uv
2️⃣ Backend Setup (FastAPI)
bash
Copy code
cd backend
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
✅ API Docs:
http://localhost:8000/docs

3️⃣ Frontend Setup (Streamlit)
Open a new terminal:

bash
Copy code
cd frontend
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
✅ UI will open automatically via Codespaces port forwarding.

🧪 Test URLs
Use these to verify the app:

arduino
Copy code
https://en.wikipedia.org/wiki/Artificial_intelligence
https://en.wikipedia.org/wiki/Machine_learning
🧠 How the Agent Works
User enters a URL in Streamlit

FastAPI receives the request

LangGraph executes:

Node 1: Fetch webpage content

Node 2: Summarize using Gemini

Summary returned to UI

⚠️ Common Issues & Fixes
403 Forbidden Error
✔ Fixed by sending browser-like User-Agent headers

Gemini Model Not Found
✔ Use new SDK (google-genai)
✔ Use Gemini 1.5 models

API Key Not Loaded
✔ Avoid accessing env vars at import time
✔ Load .env before LLM usage

🔒 Security Best Practices
API keys loaded at runtime (not import time)

.env excluded from version control

LLM initialized lazily

No secrets in frontend

🧩 Extending the Project
This project is intentionally modular. You can easily add:

🔎 Web search tool

📚 Multi-page crawling

🧠 Question answering over pages

✂️ Chunking for long documents

📑 Structured summaries (bullets, headings)

🔄 Streaming LLM responses

⚡ Async execution

🎯 Who Is This For?
AI / ML Engineers

Backend Engineers

Product Engineers working with LLMs

Interview & portfolio projects

Anyone learning Agentic AI systems

📜 License
MIT License – feel free to use, modify, and build upon it.

⭐ If you like this project
Give it a ⭐ on GitHub and feel free to fork or contribute!