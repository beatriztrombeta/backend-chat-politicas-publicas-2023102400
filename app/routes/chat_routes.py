from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.chat_schema import ChatRequest
from app.controllers.chat_controller import process_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("")
def chat(data: ChatRequest, db: Session = Depends(get_db)):
    return process_chat(data.question, db)