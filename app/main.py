from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routes import auth, todos, notes, users, news
from app.db.base_class import Base
from app.db.session import engine
import app.models

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(todos.router, prefix="/api/v1/todos", tags=["todos"])
app.include_router(notes.router, prefix="/api/v1/notes", tags=["notes"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(news.router, prefix="/api/v1/news", tags=["news"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
