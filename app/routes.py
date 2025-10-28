from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserLogin, VerifyCode, ChatRequest
from app.controllers.auth_controller import send_login_code, validate_login_code
from app.controllers.chat_controller import process_chat

router = APIRouter()

@router.post("/auth/send-code")
def send_code(data: UserLogin, db: Session = Depends(get_db)):
    return send_login_code(data.email, db)

@router.post("/auth/verify-code")
def verify_code(data: VerifyCode):
    return validate_login_code(data.email, data.code)

@router.post("/chat")
def chat(data: ChatRequest, db: Session = Depends(get_db)):
    return process_chat(data.question, db)
