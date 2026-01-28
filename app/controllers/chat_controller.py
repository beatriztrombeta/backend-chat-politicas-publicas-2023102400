from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.groq_service import ask_groq
from app.services.report_service import generate_metabase_link

def process_chat(question: str, db: Session):
    if not question or not question.strip():
        raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")
    groq_response = ask_groq(question)
    if not groq_response:
        raise HTTPException(status_code=500, detail="Erro na API Groq.")

    answer = groq_response.get("answer", "").strip()

    try:
        question_id = int(answer)
    except ValueError:
        raise HTTPException(status_code=500, detail=f"Resposta inválida do Gemini: {answer}")
    
    report_link = generate_metabase_link(question_id)

    if not report_link:
        raise HTTPException(status_code=404, detail=f"Nenhum dashboard encontrado para a pergunta {question_id}")

    return {
        "answer": answer,
        "report_link": report_link
    }
