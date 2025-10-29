from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.services.gemini_service import ask_gemini
from app.services.report_service import get_report_by_question_id

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
    
    report = get_report_by_question_id(db, question_id)
    
    return {
        "answer": answer,
        "report_link": report.link if report else None
    }
