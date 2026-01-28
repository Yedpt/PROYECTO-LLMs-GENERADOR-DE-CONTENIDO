from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.content_controller import router as content_router

app = FastAPI(title="Generador de Contenido con LLMs")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(content_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "API de Generador de Contenido con LLMs funcionando"}


@app.get("/health")
def health():
    return {"status": "ok"}
