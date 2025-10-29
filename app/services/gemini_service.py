import httpx
from app.config import settings
from app.data.questions_list import QUESTIONS_LIST

def ask_gemini(question: str):
    url = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": settings.GEMINI_API_KEY}
    prompt = f"""
        Analise a pergunta do usuário e diga qual das 50 perguntas predefinidas ela mais se assemelha.
        Responda APENAS com o número correspondente (1 a 50). Não explique.

        {QUESTIONS_LIST}

        Pergunta do usuário: "{question}"
        """
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = httpx.post(url, params=params, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()
        print("Resposta da Gemini API:", data)

        answer = (
            data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
            .strip()
        )

        return {"answer": answer}

    except httpx.HTTPStatusError as e:
        print("Erro HTTP:", e.response.status_code, e.response.text)
        return None
    except Exception as e:
        print("Erro geral:", e)
        return None
