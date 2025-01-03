# API Documentation

## Base URL
The base URL for all API endpoints is `/api/v1`

## Authentication
Most endpoints require authentication using JWT (JSON Web Token). Include the token in the Authorization header:
```
Authorization: Bearer <your_token>
```

## Endpoints

### Authentication

#### Register
- **URL**: `/api/v1/auth/register`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "email": "string",
    "username": "string",
    "password": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "id": "integer",
    "email": "string",
    "username": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

#### Login
- **URL**: `/api/v1/auth/login`
- **Method**: `POST`
- **Body** (form-data):
  ```
  username: string
  password: string
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```

### User Management

#### Get Current User
- **URL**: `/api/v1/auth/me`
- **Method**: `GET`
- **Auth**: Required
- **Response**: User object

#### Update Current User
- **URL**: `/api/v1/auth/me`
- **Method**: `PUT`
- **Auth**: Required
- **Body**:
  ```json
  {
    "email": "string",
    "username": "string",
    "password": "string"
  }
  ```

#### List Users (Superuser Only)
- **URL**: `/api/v1/users`
- **Method**: `GET`
- **Auth**: Required (Superuser)
- **Query Parameters**:
  - `skip` (optional): Number of records to skip
  - `limit` (optional): Maximum number of records to return

#### Get User by ID (Superuser Only)
- **URL**: `/api/v1/users/{user_id}`
- **Method**: `GET`
- **Auth**: Required (Superuser)

#### Update User (Superuser Only)
- **URL**: `/api/v1/users/{user_id}`
- **Method**: `PUT`
- **Auth**: Required (Superuser)

#### Delete User (Superuser Only)
- **URL**: `/api/v1/users/{user_id}`
- **Method**: `DELETE`
- **Auth**: Required (Superuser)

### Todos

#### Get All Todos
- **URL**: `/api/v1/todos`
- **Method**: `GET`
- **Auth**: Required
- **Query Parameters**:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
  - `completed` (optional): Filter by completion status (boolean)
  - `priority` (optional): Filter by priority level (integer)
  - `due_date_from` (optional): Filter by due date start (datetime)
  - `due_date_to` (optional): Filter by due date end (datetime)

#### Get Single Todo
- **URL**: `/api/v1/todos/{todo_id}`
- **Method**: `GET`
- **Auth**: Required

#### Create Todo
- **URL**: `/api/v1/todos`
- **Method**: `POST`
- **Auth**: Required
- **Body**:
  ```json
  {
    "title": "string",
    "description": "string",
    "priority": "integer",
    "due_date": "datetime",
    "completed": "boolean"
  }
  ```

#### Update Todo
- **URL**: `/api/v1/todos/{todo_id}`
- **Method**: `PUT`
- **Auth**: Required
- **Body**: Same as Create Todo

#### Delete Todo
- **URL**: `/api/v1/todos/{todo_id}`
- **Method**: `DELETE`
- **Auth**: Required

#### Get Upcoming Todos
- **URL**: `/api/v1/todos/upcoming`
- **Method**: `GET`
- **Auth**: Required
- **Query Parameters**:
  - `days` (optional): Number of days ahead to look (default: 7, min: 1, max: 30)

### Notes

#### Get All Notes
- **URL**: `/api/v1/notes`
- **Method**: `GET`
- **Auth**: Required
- **Query Parameters**:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
  - `search` (optional): Search in title and content
  - `tag` (optional): Filter by tag
  - `public_only` (optional): Show only public notes

#### Get Single Note
- **URL**: `/api/v1/notes/{note_id}`
- **Method**: `GET`
- **Auth**: Required

#### Create Note
- **URL**: `/api/v1/notes`
- **Method**: `POST`
- **Auth**: Required
- **Body**:
  ```json
  {
    "title": "string",
    "content": "string",
    "is_public": "boolean",
    "tags": ["string"]
  }
  ```

#### Update Note
- **URL**: `/api/v1/notes/{note_id}`
- **Method**: `PUT`
- **Auth**: Required
- **Body**: Same as Create Note

#### Delete Note
- **URL**: `/api/v1/notes/{note_id}`
- **Method**: `DELETE`
- **Auth**: Required

#### List Tags
- **URL**: `/api/v1/notes/tags`
- **Method**: `GET`
- **Auth**: Required

### News

#### List News Articles
- **URL**: `/api/v1/news`
- **Method**: `GET`
- **Query Parameters**:
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 10)
  - `search` (optional): Search in title and content

#### Get News Article
- **URL**: `/api/v1/news/{news_id}`
- **Method**: `GET`

#### Create News Article (Superuser Only)
- **URL**: `/api/v1/news`
- **Method**: `POST`
- **Auth**: Required (Superuser)
- **Body**:
  ```json
  {
    "title": "string",
    "content": "string",
    "image_url": "string"
  }
  ```

#### Update News Article (Superuser Only)
- **URL**: `/api/v1/news/{news_id}`
- **Method**: `PUT`
- **Auth**: Required (Superuser)
- **Body**: Same as Create News

#### Delete News Article (Superuser Only)
- **URL**: `/api/v1/news/{news_id}`
- **Method**: `DELETE`
- **Auth**: Required (Superuser)

## Error Responses
All error responses follow this format:
```json
{
  "detail": "Error message"
}
```

Common HTTP Status Codes:
- 200: Success
- 201: Created
- 204: No Content
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 422: Validation Error
- 500: Internal Server Error

## Rate Limiting
The API implements rate limiting to prevent abuse. Limits are:
- 100 requests per minute for authenticated users
- 20 requests per minute for unauthenticated users

## Pagination
Most list endpoints support pagination using these query parameters:
- `skip`: Number of records to skip
- `limit`: Maximum number of records to return

## Search
Many endpoints support search functionality through the `search` query parameter. The search is case-insensitive and looks for partial matches in relevant fields.
