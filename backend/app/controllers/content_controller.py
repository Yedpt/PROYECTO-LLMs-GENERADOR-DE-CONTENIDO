from fastapi import APIRouter
from app.schema.content_request import ContentRequest
from app.schema.content_response import ContentResponse
from app.services.content_service import ContentService

router = APIRouter()
service = ContentService()


@router.post("/generate", response_model=ContentResponse)
def generate_content(request: ContentRequest):
    result = service.generar_contenido(
        tema=request.tema,
        plataforma=request.plataforma,
        audiencia=request.audiencia,
        tono=request.tono
    )

    return ContentResponse(**result)
