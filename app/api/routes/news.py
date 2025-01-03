from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.core.deps import get_db, get_current_active_superuser
from app.models.news import News
from app.models.user import User
from app.schemas.news import NewsCreate, NewsUpdate, NewsResponse

router = APIRouter()

@router.get("", response_model=List[NewsResponse])
async def list_news(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 10,
    search: Optional[str] = None
):
    """
    Retrieve news articles.
    """
    query = db.query(News)
    
    if search:
        query = query.filter(
            News.title.ilike(f"%{search}%") | News.content.ilike(f"%{search}%")
        )
    
    total = query.count()
    news = query.order_by(desc(News.created_at)).offset(skip).limit(limit).all()
    
    return news

@router.post("", response_model=NewsResponse, status_code=status.HTTP_201_CREATED)
async def create_news(
    *,
    db: Session = Depends(get_db),
    news_in: NewsCreate,
    current_user: User = Depends(get_current_active_superuser)
):
    """
    Create new news article. Only for superusers.
    """
    news = News(**news_in.model_dump())
    db.add(news)
    db.commit()
    db.refresh(news)
    return news

@router.get("/{news_id}", response_model=NewsResponse)
async def get_news(
    news_id: int,
    db: Session = Depends(get_db)
):
    """
    Get news article by ID.
    """
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News article not found"
        )
    return news

@router.put("/{news_id}", response_model=NewsResponse)
async def update_news(
    *,
    db: Session = Depends(get_db),
    news_id: int,
    news_in: NewsUpdate,
    current_user: User = Depends(get_current_active_superuser)
):
    """
    Update news article. Only for superusers.
    """
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News article not found"
        )
    
    for field, value in news_in.model_dump(exclude_unset=True).items():
        setattr(news, field, value)
    
    db.commit()
    db.refresh(news)
    return news

@router.delete("/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(
    *,
    db: Session = Depends(get_db),
    news_id: int,
    current_user: User = Depends(get_current_active_superuser)
):
    """
    Delete news article. Only for superusers.
    """
    news = db.query(News).filter(News.id == news_id).first()
    if not news:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="News article not found"
        )
    
    db.delete(news)
    db.commit()
    return None
