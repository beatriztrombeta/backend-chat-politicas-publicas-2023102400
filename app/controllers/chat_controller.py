from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.services.groq_service import classify_question, generate_natural_answer
from app.services.sql_query_service import execute_question_sql
from app.services.report_service import generate_metabase_link


def process_chat(question: str, db: Session):
    if not question or not question.strip():
        raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")

    try:
        question_id = classify_question(question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao classificar pergunta: {str(e)}")

    try:
        sql_result = execute_question_sql(question_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao executar consulta SQL: {str(e)}")

    try:
        natural_answer = generate_natural_answer(
            user_question=question,
            question_id=question_id,
            sql_result=sql_result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar resposta natural: {str(e)}")

    report_link = generate_metabase_link(question_id)

    return {
        "answer": natural_answer,
        "question_id": question_id,
        "sql_result": sql_result,
        "report_link": report_link
    }