from sqlalchemy.orm import Session
from app.models import Report

def get_report_by_question_id(db: Session, question_id: int):
    return db.query(Report).filter(Report.questionID == question_id).first()
