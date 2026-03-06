# Web Search AI

A lightweight Python script that combines DuckDuckGo web search with the Ollama language model (specifically `phi3:mini`) to provide short, AI-generated summarized answers based on real-time web results.

## Prerequisites

- [Ollama](https://ollama.com/) must be installed and running locally.
- You must have the `phi3:mini` model pulled in Ollama (`ollama pull phi3:mini`).
- Python 3.7+ (recommended).

## Installation

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:
```bash
python ai_base_web_search.py
```

2. Enter your query when prompted:
```text
Enter your quary : [your search query]
```

3. The script will fetch the top 5 web results from DuckDuckGo, process them, and provide a concise answer under 100 words using the local Ollama model.

## Troubleshooting

If you encounter the "code is not working" message, please ensure that:
- You have an active internet connection (required for the web search).
- Ollama is running in the background.
- The `phi3:mini` model has been successfully downloaded via Ollama.
