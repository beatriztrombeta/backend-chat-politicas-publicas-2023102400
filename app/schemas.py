from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr

class VerifyCode(BaseModel):
    email: EmailStr
    code: str

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    report_link: str
