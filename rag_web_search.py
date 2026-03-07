#!/home/kali/Desktop/test/venv/bin/python

import os
import joblib
import numpy as np
import requests
from bs4 import BeautifulSoup
from ddgs import DDGS
import ollama

EMBEDDING_MODEL = "bge-m3:latest" # Note: make sure to run `ollama pull bge-m3:latest`
CHAT_MODEL = "phi3:mini"
TEMP_FILE = "rag_cache.joblib"

def get_search_results(query, max_results=3):
    print(f"[*] Searching the web for: {query}")
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=max_results))
        # DuckDuckGo's result structure usually contains 'href' for the URL
        return [r.get('href', '') for r in results if r.get('href')]

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = " ".join([p.get_text() for p in paragraphs])
        return text
    except Exception as e:
        print(f"[-] Failed to fetch {url}: {e}")
        return ""

def chunk_text(text, chunk_size=100, overlap=20):
    words = text.split()
    chunks = []
    # Slide by chunk_size - overlap
    step = max(1, chunk_size - overlap)
    for i in range(0, len(words), step):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk:
            chunks.append(chunk)

    return chunks


def get_embedding(text):
    # Some older versions of ollama python client use `embeddings`
    response = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text)
    return response['embedding']

def cosine_similarity(a, b):
    # Calculate cosine similarity between two vectors
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def process_and_store(urls):
    print("[*] Scraping and embedding content...")
    all_chunks = []
    all_embeddings = []
    
    for url in urls:
        text = extract_text_from_url(url)
        if not text:
            continue
        
        chunks = chunk_text(text, chunk_size=100, overlap=20)
        for chunk in chunks:
            try:
                emb = get_embedding(chunk)
                all_chunks.append(chunk)
                all_embeddings.append(emb)
            except Exception as e:
                print(f"[-] Failed to embed a chunk: {e}")
                
    if all_chunks:
        # Save to a temporary joblib file
        joblib.dump({"chunks": all_chunks, "embeddings": all_embeddings}, TEMP_FILE)
        print(f"[*] Saved {len(all_chunks)} chunks and embeddings to {TEMP_FILE}")
        
    return all_chunks, all_embeddings

def main():
    query = input("Enter your query: ")
    if not query.strip():
        return
        
    # 1. Search the Web
    urls = get_search_results(query, max_results=3)
    if not urls:
        print("[-] No results found from DuckDuckGo.")
        return
        
    # 2. Process and Store Context into joblib file
    chunks, embeddings = process_and_store(urls)
    with open("data.txt", "w",encoding="UTF-8") as f:
        f.write("\n\n".join(chunks))
    if not chunks:
        print("[-] No text content could be extracted from the search results.")
        return
        
    # 3. Retrieve Context via Cosine Similarity
    print("[*] Retrieving relevant information...")
    try:
        query_emb = get_embedding(query)
    except Exception as e:
        print(f"[-] Failed to generate query embedding. Did you run 'ollama pull {EMBEDDING_MODEL}'? Error: {e}")
        return
        
    similarities = [cosine_similarity(query_emb, doc_emb) for doc_emb in embeddings]
    
    # Get top 3 chunks (most similar)
    top_n = min(3, len(similarities))
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    retrieved_context = "\n".join([chunks[i] for i in top_indices])
    

    
    # 4. Generate Answer via RAG
    prompt = f"""You are a helpful assistant. Use ONLY the following context to answer the user's query accurately and concisely (under 100 words).
If the answer is not in the context, say "I don't have enough information from the web to answer that."

Context:
{retrieved_context}

Query: {query}"""
    with open("prompt.txt", "w") as f:
        f.write(prompt)
    print("\n[*] Generating Answer...\n")
    try:
        response = ollama.chat(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )
        
        for chunk in response:
            print(chunk['message']['content'], end='', flush=True)
        print("\n")
    except Exception as e:
        print(f"\n[-] Error generating response: {e}")

if __name__ == "__main__":
    main()
