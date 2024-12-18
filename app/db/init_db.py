from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.db.session import engine
from app.models.user import User
from app.models.note import Note, Tag

def init_db() -> None:
    print("Creating database tables...")
    Base.metadata.drop_all(bind=engine)  # Сбрасываем все таблицы
    Base.metadata.create_all(bind=engine)  # Создаем заново
    print("Database tables created successfully!")
