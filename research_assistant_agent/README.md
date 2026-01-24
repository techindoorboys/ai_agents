# 📚 Research Assistant with Citations (Gemini + LangGraph)

A simple yet powerful **AI Research Assistant** that can:
- Answer research questions
- Analyze PDF research papers from a URL
- Generate **abstracts, summaries, key insights**
- Provide **citations / references**
- Orchestrate logic using **LangGraph**
- Use **Gemini LLM** end-to-end
- Run fully inside **GitHub Codespaces**

---

## ✨ Features

- 🔍 Web search using DuckDuckGo (via `ddgs`)
- 📄 PDF analysis directly from URL
- 🧠 Gemini LLM (latest Google GenAI SDK)
- 🕸 LangGraph for agent orchestration
- ⚡ FastAPI backend
- 🎨 Streamlit frontend
- 🔐 Environment variable support with `dotenv`
- 📦 Dependency management using `uv`

---

## 🏗️ Architecture Overview
```yaml
Streamlit UI
|
v
FastAPI Backend
|
v
LangGraph Agent
|
├── DuckDuckGo Search Tool (ddgs)
├── PDF Reader Tool
└── Gemini LLM
```

---

## 📂 Project Structure
```yaml
research-assistant/
│
├── backend/
│ ├── main.py # FastAPI app + LangGraph wiring
│ ├── agent.py # Gemini LLM wrapper
│ ├── tools.py # DuckDuckGo + PDF tools
│ ├── prompts.py # Prompt templates
│ └── requirements.txt
│
├── frontend/
│ ├── app.py # Streamlit UI
│ └── requirements.txt
│
├── .env # Environment variables
├── pyproject.toml
└── README.md
```

---

## 🧰 Tech Stack

| Component | Tool |
|--------|------|
| Language | Python 3.11+ |
| LLM | Gemini (`google-genai`) |
| Agent Orchestration | LangGraph |
| Backend | FastAPI |
| Frontend | Streamlit |
| Search | DuckDuckGo (`ddgs`) |
| PDF Parsing | pypdf |
| Env Management | python-dotenv |
| Package Manager | uv |

---

## 🔑 Environment Setup

Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
You can get a Gemini API key from Google AI Studio.
```

🐍 Python Environment (Using UV) and 📦 Install Dependencies

```bash
uv venv
source .venv/bin/activate
uv pip install -r backend/requirements.txt

uv pip install -r frontend/requirements.txt
```

▶️ Running the Application (GitHub Codespaces)
1️⃣ Start the Backend (FastAPI)

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

FastAPI will be available on port 8000

Codespaces automatically exposes the port

2️⃣ Start the Frontend (Streamlit)
Open a new terminal:

```bash
cd frontend
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Streamlit will be available on port 8501

🧪 Example Inputs
🔍 Research Question

```pgsql
Impact of large language models on healthcare diagnostics
```

📄 PDF URL
```arduino
https://arxiv.org/pdf/2303.08774.pdf
```
Check the “Is this a PDF URL?” box when using a PDF.


🧠 How LangGraph Works in This Project
The agent follows a simple routed flow:

```java
START
  |
  v
Router Node
  |
  ├── Search Node (DuckDuckGo)
  └── PDF Node (PDF Reader)
        |
        v
     LLM Node (Gemini)
        |
       END
```

Key Design Rules
All LangGraph nodes return state dictionaries

Routing logic is handled via add_conditional_edges

LLM is always called with validated content

⚠️ Common Issues & Fixes
❌ Expected dict, got search
* Ensure routing functions return strings
* Ensure nodes return dictionaries only

❌ .json() decode error in Streamlit
* Backend returned an error or HTML
* Check FastAPI logs for traceback

❌ Empty LLM response
* Ensure search or PDF content is not empty
* Guard against empty search results

🚀 Future Improvements
* Add citation numbering [1] [2] [3]
* Convert output to structured JSON
* Add RAG with embeddings
* Enable streaming responses
* Export results to PDF or Markdown
* Deploy to Cloud Run / Fly.io

📜 License
* MIT License – free to use, modify, and distribute.

🙌 Acknowledgements
* LangGraph & LangChain
* Google Gemini
* DuckDuckGo
* Streamlit & FastAPI
