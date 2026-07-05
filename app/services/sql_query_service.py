from sqlalchemy import text
from decimal import Decimal
from datetime import date, datetime
from app.data.sql_queries import SQL_QUERIES


def serialize_value(value):
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value


def execute_question_sql(question_id: int, db):
    sql = SQL_QUERIES.get(question_id)

    if not sql:
        return {
            "status": "sem_sql",
            "message": f"Não existe consulta SQL cadastrada para a pergunta {question_id}.",
            "rows": []
        }

    result = db.execute(text(sql))
    rows = result.mappings().all()

    serialized_rows = [
        {key: serialize_value(value) for key, value in row.items()}
        for row in rows
    ]

    return {
        "status": "ok",
        "rows": serialized_rows[:100]
    }