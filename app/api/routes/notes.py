from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse, TagResponse
from app.models.note import Note, Tag
from app.core.deps import get_db, get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[NoteResponse])
async def list_notes(
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None,
    tag: Optional[str] = None,
    public_only: bool = False,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Получить список заметок с возможностью поиска и фильтрации
    """
    query = db.query(Note)
    
    if public_only:
        query = query.filter(Note.is_public == True)
    else:
        query = query.filter(Note.user_id == current_user.id)
    
    if search:
        query = query.filter(
            (Note.title.ilike(f"%{search}%")) | 
            (Note.content.ilike(f"%{search}%"))
        )
    
    if tag:
        query = query.join(Note.tags).filter(Tag.name == tag)
        
    return query.offset(skip).limit(limit).all()

@router.post("/", response_model=NoteResponse)
async def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Создать новую заметку
    """
    # Создаем заметку
    db_note = Note(
        title=note.title,
        content=note.content,
        is_public=note.is_public,
        user_id=current_user.id
    )
    
    # Добавляем теги
    if note.tags:
        for tag_name in note.tags:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
            db_note.tags.append(tag)
    
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Получить заметку по ID
    """
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
        
    if not note.is_public and note.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
        
    return note

@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(
    note_id: int,
    note_update: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Обновить заметку
    """
    db_note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == current_user.id
    ).first()
    
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    
    # Обновляем основные поля
    for field, value in note_update.model_dump(exclude_unset=True).items():
        if field != "tags":
            setattr(db_note, field, value)
    
    # Обновляем теги
    if note_update.tags is not None:
        db_note.tags = []
        for tag_name in note_update.tags:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
            db_note.tags.append(tag)
    
    db_note.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_note)
    return db_note

@router.delete("/{note_id}")
async def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Удалить заметку
    """
    db_note = db.query(Note).filter(
        Note.id == note_id,
        Note.user_id == current_user.id
    ).first()
    
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
        
    db.delete(db_note)
    db.commit()
    return {"message": "Note deleted successfully"}

@router.get("/tags/", response_model=List[TagResponse])
async def list_tags(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Получить список всех тегов
    """
    return db.query(Tag).all()
