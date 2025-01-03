from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.db.session import engine, SessionLocal
from app.models.user import User
from app.models.news import News
from app.core.config import settings

def init_db(db: Session) -> None:
    # Создаем все таблицы
    Base.metadata.create_all(bind=engine)
    
    # Проверяем, есть ли уже тестовые данные
    user = db.query(User).first()
    if not user:
        # Создаем тестового пользователя
        user = User(
            email="test@example.com",
            username="testuser",
            password="testpassword123"
        )
        db.add(user)
        
        # Создаем тестовые новости
        news_items = [
            News(
                title="Открытие нового маршрута",
                content="Мы рады сообщить об открытии нового маршрута доставки между городами Москва и Владивосток.",
                image_url="/static/img/news1.jpg"
            ),
            News(
                title="Обновление автопарка",
                content="Наша компания приобрела 10 новых грузовых автомобилей для улучшения качества обслуживания.",
                image_url="/static/img/news2.jpg"
            ),
            News(
                title="Специальное предложение",
                content="Скидка 20% на международные перевозки в течение всего декабря!",
                image_url="/static/img/news3.jpg"
            )
        ]
        for news in news_items:
            db.add(news)
        
        db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    init_db(db)
