# LogiTrans - Логистическая компания

Веб-приложение для логистической компании, разработанное с использованием FastAPI и современных веб-технологий.

## Функциональность

- Расчет стоимости перевозки
- Отслеживание заказов
- Новости компании
- Управление заказами

## Технологии

- Backend: FastAPI, SQLAlchemy, Pydantic
- Frontend: HTML, CSS (Tailwind), JavaScript
- База данных: SQLite
- Шаблонизатор: Jinja2

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone [URL репозитория]
cd FreeAPI.python
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Инициализируйте базу данных:
```bash
python -c "from app.db.init_db import init_db; init_db()"
```

5. Запустите приложение:
```bash
uvicorn app.main:app --reload
```

6. Откройте в браузере: http://localhost:8000

## Структура проекта

```
app/
├── api/
│   └── routes/          # Маршруты API
├── core/               # Основные настройки
├── db/                 # Работа с базой данных
├── models/            # Модели SQLAlchemy
├── schemas/           # Схемы Pydantic
├── static/            # Статические файлы
│   ├── css/
│   ├── js/
│   └── img/
└── templates/         # HTML шаблоны
```

## Разработка

- Для добавления новых маршрутов создайте файл в директории `app/api/routes/`
- Модели базы данных находятся в `app/models/`
- Статические файлы добавляйте в соответствующие поддиректории в `app/static/`
- Шаблоны страниц находятся в `app/templates/`

## Лицензия

MIT
