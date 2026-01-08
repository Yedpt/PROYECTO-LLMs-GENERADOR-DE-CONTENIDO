from fastapi import FastAPI
from app.controllers.content_controller import router as content_router

app = FastAPI(title="Generador de Contenido con LLMs")

app.include_router(content_router, prefix="/api")
