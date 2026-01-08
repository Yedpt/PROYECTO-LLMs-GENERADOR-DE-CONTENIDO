from pydantic import BaseModel

class ContentRequest(BaseModel):
    tema: str
    plataforma: str
    audiencia: str
    tono: str
