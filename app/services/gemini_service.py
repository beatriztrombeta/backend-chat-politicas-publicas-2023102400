import httpx
from app.config import settings

def ask_gemini(question: str):
    # Exemplo de request fictício
    url = "https://api.gemini.com/v1/chat"
    headers = {"Authorization": f"Bearer {settings.GEMINI_API_KEY}"}
    payload = {"question": question}

    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=10)
        data = response.json()
        return {
            "answer": data.get("answer"),
            "question_id": data.get("question_id")
        }
    except Exception:
        return None
