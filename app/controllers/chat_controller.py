from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Report
from app.services.gemini_service import ask_gemini
from app.services.report_service import get_report_by_question_id

def process_chat(question: str, db: Session):
    gemini_response = ask_gemini(question)
    if not gemini_response:
        raise HTTPException(status_code=500, detail="Erro na API Gemini.")
    
    answer = gemini_response["answer"]
    question_id = gemini_response["question_id"]
    report = get_report_by_question_id(db, question_id)
    
    return {"answer": answer, "report_link": report.link if report else None}
