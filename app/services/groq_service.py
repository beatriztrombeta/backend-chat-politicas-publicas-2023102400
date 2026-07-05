import httpx
import json
from app.config import settings
from app.data_usable.questions_list import QUESTIONS_LIST


def call_groq(messages, temperature=0, max_tokens=700):
    url = "https://api.groq.com/openai/v1/chat/completions"


    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.GROQ_API_KEY}"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "temperature": temperature,
        "top_p": 1,
        "max_completion_tokens": max_tokens,
        "messages": messages,
        "stream": False
    }

    response = httpx.post(url, json=payload, headers=headers, timeout=60)
    response.raise_for_status()

    data = response.json()

    return (
        data.get("choices", [{}])[0]
        .get("message", {})
        .get("content", "")
        .strip()
    )


def classify_question(question: str) -> int:
    prompt = f"""
Você é um classificador.

Sua tarefa é identificar qual das 50 perguntas predefinidas é mais semelhante
à pergunta do usuário.

Responda somente com um número de 1 a 50.

Lista de perguntas:
{QUESTIONS_LIST}

Pergunta do usuário:
{question}
"""

    answer = call_groq(
        messages=[
            {
                "role": "system",
                "content": "Você classifica perguntas. Responda somente com um número de 1 a 50."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=10
    )

    return int(answer)


def generate_natural_answer(user_question: str, question_id: int, sql_result: dict) -> str:
    prompt = f"""
Você é um assistente analítico de dados acadêmicos.

A pergunta do usuário foi:
{user_question}

Ela foi classificada como a pergunta predefinida número:
{question_id}

Resultado retornado pelo banco de dados em JSON:
{json.dumps(sql_result, ensure_ascii=False, indent=2)}

Responda em linguagem natural, clara e fácil de visualizar.

REGRAS DE FORMATAÇÃO IMPORTANTES:
1. O frontend NÃO aceita markdown.
2. Não use **negrito**, # títulos, listas markdown, tabelas markdown ou código.
3. Use apenas texto puro.
4. Separe blocos com QUEBRA DE LINHA DUPLA.
5. Use frases curtas.
6. Se precisar listar itens, use:
- item 1
- item 2
- item 3

7. Nunca escreva tudo em um único parágrafo.

REGRAS DE CONTEÚDO:
1. Não diga apenas o número da pergunta.
2. Explique os principais resultados.
3. Se houver percentuais, mencione-os.
4. Se o resultado indicar que a consulta não é suportada pelo schema atual, explique isso de forma simples.
5. Não invente dados que não estejam no resultado.
"""

    return call_groq(
        messages=[
            {
                "role": "system",
                "content": """
Você transforma resultados SQL em respostas naturais.

IMPORTANTE:
Use SOMENTE texto puro.

Sempre responda com:
parágrafos separados por linha em branco,
visual limpo,
boa leitura,
sem markdown.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=700
    )