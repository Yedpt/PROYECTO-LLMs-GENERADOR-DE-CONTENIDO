from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.controllers.content_controller import router as content_router
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"

# 🔒 Seguridad: crea la carpeta si no existe
DATA_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Generador de Contenido con LLMs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ AQUÍ ESTÁ LA CLAVE
app.mount(
    "/data",
    StaticFiles(directory=DATA_DIR),
    name="data"
)

app.include_router(content_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API funcionando"}

@app.get("/health")
def health():
    return {"status": "ok"}
