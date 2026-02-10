from fastapi import APIRouter, BackgroundTasks
from app.schema.content_request import ContentRequest
from app.schema.content_response import ContentResponse
from app.services.content_service import ContentService
from fastapi import Query
from pathlib import Path
from app.core.paths import GENERATED_IMAGES_DIR

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
    image_path = GENERATED_IMAGES_DIR / filename

    # Log para debugging: ruta absoluta donde debería guardarse la imagen
    print(f"[get_image] buscando imagen: {image_path}")

    if image_path.exists():
        return {
            "image_url": f"/data/generated_images/{filename}",
            "absolute_path": str(image_path),
            "exists": True,
        }

    return {
        "image_url": None,
        "absolute_path": str(GENERATED_IMAGES_DIR / filename),
        "exists": False,
    }