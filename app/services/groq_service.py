import httpx
from app.config import settings
from app.data.questions_list import QUESTIONS_LIST

def ask_groq(question: str):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.GROQ_API_KEY}"
    }

    prompt = f"""
    Você é um classificador. Sua tarefa é identificar qual das 50 perguntas predefinidas
    é a mais semelhante à pergunta do usuário.

    REGRAS IMPORTANTES:
    1. Responda somente com um número de 1 a 50.
    2. Não explique.
    3. Não adicione texto adicional.

    Lista de perguntas:
    {QUESTIONS_LIST}

    Pergunta do usuário: "{question}"
    """

    payload = {
        "model": "llama-3.1-8b-instant",
        "temperature": 0,
        "top_p": 1,
        "max_completion_tokens": 10,
        "messages": [
            {
                "role": "system",
                "content": "Você é um classificador. Responda APENAS com um número."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    try:
        response = httpx.post(url, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()
        print("Resposta da Groq API:", data)

        answer = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )

        return {"answer": answer}

    except httpx.HTTPStatusError as e:
        print("Erro HTTP:", e.response.status_code, e.response.text)
        return None
    except Exception as e:
        print("Erro geral:", e)
        return None
