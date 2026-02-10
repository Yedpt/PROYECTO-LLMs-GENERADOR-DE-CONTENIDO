from fastapi import APIRouter, BackgroundTasks
from app.schema.content_request import ContentRequest
from app.schema.content_response import ContentResponse
from app.services.content_service import ContentService
from fastapi import Query
from pathlib import Path

router = APIRouter()
service = ContentService()


@router.post("/generate", response_model=ContentResponse)
def generate_content(
    request: ContentRequest,
    background_tasks: BackgroundTasks
):
    # 1️⃣ Generar SOLO el texto
    result = service.generar_contenido_texto(
        tema=request.tema,
        plataforma=request.plataforma,
        audiencia=request.audiencia,
        tono=request.tono
    )

    # 2️⃣ Lanzar la imagen en background
    background_tasks.add_task(
        service.generar_imagen_background,
        request.tema,
        request.plataforma,
        request.audiencia
    )

    return ContentResponse(**result)


@router.get("/image")
def get_image(tema: str = Query(...)):
    filename = f"img_{abs(hash(tema))}.png"
    image_path = Path("/data/generated_images") / filename

    if image_path.exists():
        # Devolver ruta pública accesible (montada en /data)
        return {
            "image_url": f"/data/generated_images/{filename}"
        }

    return {
        "image_url": None
    }