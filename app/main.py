from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

app = FastAPI(title="Chatbot com Gemini + BI")

Base.metadata.create_all(bind=engine)

app.include_router(router)
