from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.utils.auth import generate_code, store_code, verify_code, create_jwt_token
from app.utils.email_service import send_email

def send_login_code(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    code = generate_code()
    store_code(email, code)
    send_email(email, "Seu código de verificação", f"Seu código é: {code}")
    return {"message": "Código enviado com sucesso."}

def validate_login_code(email: str, code: str):
    if not verify_code(email, code):
        raise HTTPException(status_code=401, detail="Código inválido ou expirado.")
    token = create_jwt_token(email)
    return {"access_token": token}
