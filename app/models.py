from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)

class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    questionID = Column(Integer, nullable=False)
    link = Column(String, nullable=False)
