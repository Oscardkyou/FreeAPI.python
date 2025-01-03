from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class NewsBase(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

class NewsCreate(NewsBase):
    pass

class NewsUpdate(NewsBase):
    title: Optional[str] = None
    content: Optional[str] = None

class NewsResponse(NewsBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
