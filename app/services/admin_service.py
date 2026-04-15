from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository

class AdminService:
    def __init__(self):
        self.repository = UserRepository()