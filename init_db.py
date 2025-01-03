from app.db.init_db import init_db
from app.db.session import SessionLocal

def main():
    db = SessionLocal()
    init_db(db)
    print("База данных успешно инициализирована!")

if __name__ == "__main__":
    main()
