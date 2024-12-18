from app.db.init_db import init_db
from app.db.session import SessionLocal

def init() -> None:
    db = SessionLocal()
    init_db(db)

def main() -> None:
    init()
    print("Database initialized successfully!")

if __name__ == "__main__":
    main()
