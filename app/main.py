from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import settings
from app.db.init_db import init_db
from app.api.routes import auth, notes, test, todos, views

# Initialize the database
init_db()

app = FastAPI(
    title="Python API Hub",
    description="Modern API Hub implementation using FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Подключаем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(views.router)  # HTML страницы
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(notes.router, prefix="/api/notes", tags=["Notes"])
app.include_router(todos.router, prefix="/api/todos", tags=["Todos"])
app.include_router(test.router, prefix="/api", tags=["Test"])

@app.get("/")
async def root():
    return {
        "message": "Welcome to Python API Hub",
        "version": settings.VERSION,
        "docs_urls": {
            "swagger": "/docs",
            "redoc": "/redoc"
        }
    }
