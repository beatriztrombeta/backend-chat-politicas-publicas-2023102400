from fastapi import APIRouter, Depends, Response, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserLogin, VerifyCode, ChatRequest
from app.controllers.auth_controller import send_login_code, validate_login_code
from app.controllers.chat_controller import process_chat
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/auth/send-code")
def send_code(data: UserLogin, db: Session = Depends(get_db)):
    return send_login_code(data.email, db)

@router.post("/auth/verify-code")
def verify_code_endpoint(data: VerifyCode, response: Response):
    token_data = validate_login_code(data.email, data.code)
    token = token_data.get("access_token")

    if not token:
        raise HTTPException(status_code=500, detail="Falha ao gerar token JWT.")

    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        secure=False, 
        samesite="Lax",
        max_age=3600
    )

    return {"message": "Login bem-sucedido."}

@router.get("/auth/validate")
def validate_token(user: dict = Depends(get_current_user)):
    return {"authenticated": True, "email": user["email"]}

@router.post("/chat")
def chat(data: ChatRequest, db: Session = Depends(get_db)):
    return process_chat(data.question, db)

@router.post("/auth/logout")
def logout(response: Response):
    response.delete_cookie("token")
    return {"message": "Logout realizado com sucesso."}

