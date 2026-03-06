from ddgs import DDGS
import ollama
query  = input("Enter your quary : ")
try:
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))

    context = "\n".join([r["body"] for r in results])

    response = ollama.chat(
        model="phi3:mini",
        messages=[{
            "role": "user",
            "content": f"Use this web info to answer under 100 words:\n{context}"
        }]
    )

    print(response["message"]["content"])
except:
    print("code is not working")