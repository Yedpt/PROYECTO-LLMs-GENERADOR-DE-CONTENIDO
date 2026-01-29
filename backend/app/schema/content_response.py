from typing import Optional
from pydantic import BaseModel


class ContentResponse(BaseModel):
    content: str
    image_url: Optional[str] = None
