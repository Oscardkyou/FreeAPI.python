from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.core.deps import get_current_user, get_db
from app.models.user import User
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse

router = APIRouter()

@router.post("", response_model=TodoResponse)
async def create_todo(
    *,
    db: Session = Depends(get_db),
    todo_in: TodoCreate,
    current_user: User = Depends(get_current_user)
) -> Todo:
    """
    Создать новую задачу.
    """
    todo = Todo(
        **todo_in.model_dump(),
        user_id=current_user.id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@router.get("", response_model=List[TodoResponse])
async def get_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = 100,
    completed: Optional[bool] = None,
    priority: Optional[int] = None,
    due_date_from: Optional[datetime] = None,
    due_date_to: Optional[datetime] = None,
) -> List[Todo]:
    """
    Получить список задач с фильтрацией.
    """
    query = db.query(Todo).filter(Todo.user_id == current_user.id)
    
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    if priority is not None:
        query = query.filter(Todo.priority == priority)
    if due_date_from:
        query = query.filter(Todo.due_date >= due_date_from)
    if due_date_to:
        query = query.filter(Todo.due_date <= due_date_to)
    
    return query.offset(skip).limit(limit).all()

@router.get("/upcoming", response_model=List[TodoResponse])
async def get_upcoming_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    days: int = Query(default=7, ge=1, le=30)
) -> List[Todo]:
    """
    Получить список предстоящих задач на следующие N дней.
    """
    end_date = datetime.utcnow() + timedelta(days=days)
    return db.query(Todo).filter(
        Todo.user_id == current_user.id,
        Todo.completed == False,
        Todo.due_date <= end_date
    ).order_by(Todo.due_date.asc()).all()

@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Todo:
    """
    Получить задачу по ID.
    """
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user.id
    ).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return todo

@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo_in: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Todo:
    """
    Обновить задачу.
    """
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user.id
    ).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    todo_data = todo_in.model_dump(exclude_unset=True)
    for field, value in todo_data.items():
        setattr(todo, field, value)
    
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> dict:
    """
    Удалить задачу.
    """
    todo = db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == current_user.id
    ).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    
    db.delete(todo)
    db.commit()
    return {"message": "Задача успешно удалена"}
