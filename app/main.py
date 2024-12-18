from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from app.core.config import settings
from app.api.routes import views
from app.db.base_class import Base
from app.db.session import engine
import app.models  # Импортируем модели

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

# Инициализируем приложение
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Настраиваем CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Настраиваем шаблоны
templates = Jinja2Templates(directory="app/templates")

# Добавляем контекстный процессор для даты
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    request.state.current_year = datetime.now().year
    response = await call_next(request)
    return response

# Подключаем роуты
app.include_router(views.router)

# Создаем тестовые данные
@app.on_event("startup")
async def create_test_data():
    from app.db.session import SessionLocal
    from app.models.news import News
    
    db = SessionLocal()
    try:
        # Проверяем, есть ли уже новости
        if db.query(News).count() == 0:
            # Создаем тестовые новости
            news_items = [
                News(
                    title="Открытие нового маршрута",
                    content="Мы рады сообщить об открытии нового маршрута между городами Москва и Владивосток",
                    image_url="/static/img/news1.jpg"
                ),
                News(
                    title="Расширение автопарка",
                    content="Наш автопарк пополнился новыми современными грузовиками",
                    image_url="/static/img/news2.jpg"
                ),
                News(
                    title="Международное сотрудничество",
                    content="Подписано соглашение о сотрудничестве с европейскими партнерами",
                    image_url="/static/img/news3.jpg"
                )
            ]
            for news in news_items:
                db.add(news)
            db.commit()
    except Exception as e:
        print(f"Error creating test data: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
