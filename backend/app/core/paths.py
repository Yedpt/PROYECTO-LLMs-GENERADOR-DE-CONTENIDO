from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = BASE_DIR / "data"
GENERATED_IMAGES_DIR = DATA_DIR / "generated_images"
