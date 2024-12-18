from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class NoteBase(BaseModel):
    title: str
    content: str
    is_public: bool = False

class NoteCreate(NoteBase):
    tags: Optional[List[str]] = []

class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_public: Optional[bool] = None
    tags: Optional[List[str]] = None

class NoteResponse(NoteBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int
    tags: List[TagResponse] = []

    class Config:
        from_attributes = True
