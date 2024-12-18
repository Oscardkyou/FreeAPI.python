from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    priority: int = 1
    due_date: Optional[datetime] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[int] = None
    due_date: Optional[datetime] = None

class TodoResponse(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int

    class Config:
        from_attributes = True
