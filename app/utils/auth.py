import random
from datetime import datetime, timedelta
from jose import jwt
from app.config import settings

verification_codes = {}

def generate_code():
    return str(random.randint(100000, 999999))

def store_code(email: str, code: str):
    verification_codes[email] = {"code": code, "expires": datetime.utcnow() + timedelta(minutes=10)}

def verify_code(email: str, code: str):
    entry = verification_codes.get(email)
    if not entry or entry["expires"] < datetime.utcnow():
        return False
    return entry["code"] == code

def create_jwt_token(email: str):
    payload = {"sub": email, "exp": datetime.utcnow() + timedelta(hours=2)}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
