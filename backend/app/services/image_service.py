import os
import requests
from typing import Optional
from app.core.paths import GENERATED_IMAGES_DIR

HF_API_URL = (
    "https://router.huggingface.co/hf-inference/models/"
    "stabilityai/stable-diffusion-xl-base-1.0"
)

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")


def generate_image(prompt: str) -> Optional[str]:
    if not HF_API_KEY:
        print("❌ HUGGINGFACE_API_KEY no cargada")
        return None

    print("🖼️ Generando imagen con HuggingFace (router)...")

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Accept": "image/png",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }

    response = requests.post(
        HF_API_URL,
        headers=headers,
        json=payload,
        timeout=120
    )

    if response.status_code != 200:
        print("❌ Error HuggingFace:", response.status_code, response.text)
        return None

    # ✅ PATH ABSOLUTO Y CORRECTO
    GENERATED_IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"img_{abs(hash(prompt))}.png"
    filepath = GENERATED_IMAGES_DIR / filename

    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"✅ Imagen guardada en {filepath}")

    # El servidor monta la carpeta `data` en /data (ver `main.py`).
    # Devolver la ruta pública correcta para que el frontend la consuma.
    return f"/data/generated_images/{filename}"
