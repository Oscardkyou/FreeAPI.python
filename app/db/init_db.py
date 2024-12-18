from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.db.session import engine, SessionLocal
from app.models.order import Order, ShipmentType
from app.models.news import News

def init_db() -> None:
    print("Creating database tables...")
    Base.metadata.drop_all(bind=engine)  # Сбрасываем все таблицы
    Base.metadata.create_all(bind=engine)  # Создаем заново
    
    # Создаем тестовые данные
    db = SessionLocal()
    try:
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
        
        # Создаем тестовый заказ
        test_order = Order(
            tracking_number="TEST123456",
            from_city="Москва",
            to_city="Санкт-Петербург",
            weight=100.0,
            volume=2.5,
            shipment_type=ShipmentType.AUTO,
            status="в пути"
        )
        db.add(test_order)
        
        db.commit()
        print("Test data created successfully!")
        
    except Exception as e:
        print(f"Error creating test data: {e}")
        db.rollback()
    finally:
        db.close()
    
    print("Database initialization completed!")
