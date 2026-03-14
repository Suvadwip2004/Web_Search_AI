# 🔎 Web Search AI

A lightweight **Python-based AI web search assistant** that combines **DuckDuckGo search** with a **local Ollama language model** to generate concise answers from real-time web content.

Instead of relying on cloud APIs, this project runs **fully locally** using Ollama models. It fetches web results, extracts webpage text, embeds the content, retrieves the most relevant information, and generates a summarized answer.

This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline using local LLMs.

---

# 🚀 Features

- 🌐 Real-time web search using DuckDuckGo  
- 🧠 Local AI inference using Ollama  
- 📄 Webpage scraping and text extraction  
- ✂️ Intelligent text chunking  
- 📊 Embedding generation  
- 🔍 Semantic similarity search using cosine similarity  
- 🤖 AI-generated summarized answers  
- 💾 Temporary vector storage using Joblib  

---

# 🧠 System Architecture (RAG Pipeline)

```
User Query
    │
    ▼
DuckDuckGo Search
    │
    ▼
Fetch Top Web Pages
    │
    ▼
Extract Text from HTML
    │
    ▼
Chunk Text
    │
    ▼
Generate Embeddings (bge-m3)
    │
    ▼
Cosine Similarity Search
    │
    ▼
Retrieve Relevant Context
    │
    ▼
Generate Answer (phi3:mini)
```

---

# 📦 Prerequisites

Make sure the following tools are installed.

## 1️⃣ Install Ollama

Download and install Ollama:

https://ollama.com

Start Ollama locally before running the script.

---

## 2️⃣ Pull Required Models

```bash
ollama pull phi3:mini
ollama pull bge-m3:latest
```

| Model | Purpose |
|------|------|
| phi3:mini | Chat model |
| bge-m3 | Embedding model |

---

## 3️⃣ Python Version

Python **3.7+** is recommended.

Check version:

```bash
python --version
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/web-search-ai.git
cd web-search-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`

```
numpy
requests
beautifulsoup4
duckduckgo-search
joblib
ollama
```

---

# ▶️ Usage

Run the script:

```bash
python ai_base_web_search.py
```

Enter your query when prompted:

```
Enter your query: What is Retrieval Augmented Generation?
```

The system will:

1. Search the web using DuckDuckGo  
2. Extract text from top websites  
3. Convert text into embeddings  
4. Retrieve relevant information  
5. Generate a short AI answer  

---

# 📁 Project Structure

```
web-search-ai
│
├── ai_base_web_search.py
├── requirements.txt
├── README.md
│
├── rag_cache.joblib
├── data.txt
└── prompt.txt
```

| File | Description |
|-----|-------------|
| ai_base_web_search.py | Main RAG pipeline |
| rag_cache.joblib | Cached embeddings |
| data.txt | Extracted webpage text |
| prompt.txt | Generated prompt for LLM |

---

# 💡 Code Use Case

This project demonstrates how to build a **local AI web search assistant**.

### 🔹 AI Search Engine
Summarize search results automatically.

### 🔹 RAG Learning Project
Understand **Retrieval-Augmented Generation pipelines**.

### 🔹 Local AI Applications
Run AI models **without OpenAI API**.

### 🔹 AI Developer Practice
Learn:

- embeddings
- semantic search
- cosine similarity
- prompt engineering
- local LLM pipelines

---

# ⚙️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| Python | Programming language |
| DuckDuckGo Search | Web search |
| BeautifulSoup | HTML parsing |
| Ollama | Local LLM runtime |
| NumPy | Vector similarity |
| Joblib | Caching embeddings |

---



# ⚠️ Troubleshooting

If the script does not work:

### Check Internet Connection
Web search requires internet.

### Ensure Ollama is Running

```bash
ollama serve
```

### Verify Models Installed

```bash
ollama list
```

Expected output:

```
phi3:mini
bge-m3:latest
```

### Reinstall Dependencies

```bash
pip install -r requirements.txt
```

---

# 📚 Learning Outcomes

By building this project you will learn:

- Retrieval-Augmented Generation (RAG)
- Web scraping pipelines
- Embedding generation
- Vector similarity search
- Prompt engineering
- Local LLM deployment

---

# 🔮 Future Improvements

Possible improvements:

- Add **FAISS vector database**
- Add **Streamlit UI**
- Improve **search ranking**
- Add **source citations**
- Support **multi-query search**

---

