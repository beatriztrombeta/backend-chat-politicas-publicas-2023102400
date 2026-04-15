from fastapi import APIRouter, Depends, UploadFile, File, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_schema import UserCreateForm, UserCreateResponse
from app.controllers.user_controller import UserController
from app.schemas.user_signup_schema import UserSignupEmail, UserSignupVerifyCode

router = APIRouter(prefix="/users", tags=["Usuários"])

user_controller = UserController()

@router.post("", response_model=UserCreateResponse)
async def create_new_user(
    form: UserCreateForm = Depends(UserCreateForm.as_form),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Endpoint para criar um novo usuário
    
    Args:
        form: Dados do formulário de criação de usuário
        file: Arquivo PDF de comprovante
        db: Sessão do banco de dados
        
    Returns:
        UserCreateResponse com dados do usuário criado
    """
    return await user_controller.create_new_user(
        form=form,
        file=file,
        db=db
    )

@router.post("/send-code")
def send_signup_code(data: UserSignupEmail, db: Session = Depends(get_db)):
    return user_controller.send_signup_code(data.email, db)

@router.post("/verify-code")
def verify_signup_code(data: UserSignupVerifyCode, response: Response, db: Session = Depends(get_db)):
    return user_controller.verify_signup_code(data.email, data.code, response, db)