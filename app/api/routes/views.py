from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user_optional
from app.models.user import User
from app.models.note import Note
from app.models.todo import Todo

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request, current_user: User = Depends(get_current_user_optional)):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "user": current_user}
    )

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_optional)
):
    if not current_user:
        raise HTTPException(status_code=302, headers={"Location": "/login"})
    
    notes = db.query(Note).filter(Note.user_id == current_user.id).all()
    todos = db.query(Todo).filter(
        Todo.user_id == current_user.id,
        Todo.completed == False
    ).order_by(Todo.due_date.asc()).limit(5).all()
    
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": current_user,
            "notes": notes,
            "todos": todos
        }
    )
