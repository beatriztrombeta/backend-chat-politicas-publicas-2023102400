from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.gemini_service import ask_gemini
from app.services.report_service import generate_metabase_link

def process_chat(question: str, db: Session):
    if not question or not question.strip():
        raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")
    gemini_response = ask_gemini(question)
    if not gemini_response:
        raise HTTPException(status_code=500, detail="Erro na API Gemini.")
    
    if isinstance(gemini_response, dict):
        answer = gemini_response.get("answer", "").strip()
    else:
        answer = str(gemini_response).strip()

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
