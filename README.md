# Python API Hub

Modern API Hub implementation using FastAPI and Python.

## Features

- 🚀 Fast and modern API using FastAPI
- 📝 Todo API with categories and priorities
- 📒 Notes API with tags and search
- 📊 Analytics API for tracking custom events
- 🔐 JWT Authentication
- 📚 Automatic API documentation (Swagger UI)

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

4. Open API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Authentication
- POST /auth/register - Register new user
- POST /auth/login - Login user
- GET /auth/me - Get current user info

### Todo API
- GET /api/todos - List all todos
- POST /api/todos - Create new todo
- GET /api/todos/{id} - Get todo by ID
- PUT /api/todos/{id} - Update todo
- DELETE /api/todos/{id} - Delete todo

### Notes API
- GET /api/notes - List all notes
- POST /api/notes - Create new note
- GET /api/notes/{id} - Get note by ID
- PUT /api/notes/{id} - Update note
- DELETE /api/notes/{id} - Delete note
- GET /api/notes/search - Search notes by content

### Analytics API
- POST /api/analytics/event - Track custom event
- GET /api/analytics/events - Get event statistics
- GET /api/analytics/dashboard - Get analytics dashboard
