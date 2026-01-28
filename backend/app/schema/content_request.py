from pydantic import BaseModel, Field
from typing import Optional

class ContentRequest(BaseModel):
    tema: str = Field(..., min_length=1, description="Tema del contenido")
    plataforma: str = Field(..., min_length=1, description="Plataforma de publicación")
    audiencia: str = Field(..., min_length=1, description="Audiencia objetivo")
    tono: str = Field(..., min_length=1, description="Tono del contenido")
    
    class Config:
        json_schema_extra = {
            "example": {
                "tema": "Inteligencia Artificial",
                "plataforma": "LinkedIn",
                "audiencia": "Profesionales de tecnología",
                "tono": "Profesional"
            }
        }
