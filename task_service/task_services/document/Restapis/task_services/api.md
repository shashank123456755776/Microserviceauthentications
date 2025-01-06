Task Management API Documentation

Base URL

The API is hosted at the following base URL:

http://<your-domain-or-ip>/

Endpoints

1. Create Task

POST /tasks/

Description

Create a new task. Only users with the admin role can create tasks.

Headers

Key

Value

X-API-KEY

<my-api-key>

Request Body (JSON)

{
    "title": "New Task",
    "description": "This is a sample task",
    "due_date": "2025-01-15"
}

Response (201 Created)

{
    "id": 1,
    "title": "New Task",
    "description": "This is a sample task",
    "due_date": "2025-01-15",
    "created_by": 5
}

Response (400 Bad Request)

{
    "title": ["This field is required."]
}

2. Retrieve Task by ID

GET /tasks/int:pk/

Description

Retrieve a task by its unique ID.

Headers

Key

Value

X-API-KEY

<my-api-key>

Response (200 OK)

{
    "id": 1,
    "title": "New Task",
    "description": "This is a sample task",
    "due_date": "2025-01-15",
    "created_by": 5
}

Response (404 Not Found)

{
    "error": "Task not found"
}

3. Update Task

PUT /tasks/int:pk/

Description

Update an existing task. Partial updates are allowed.

Headers

Key

Value

X-API-KEY

<my-api-key>

Request Body (JSON)

{
    "title": "Updated Task Title"
}

Response (200 OK)

{
    "id": 1,
    "title": "Updated Task Title",
    "description": "This is a sample task",
    "due_date": "2025-01-15",
    "created_by": 5
}

Response (400 Bad Request)

{
    "title": ["This field is required."]
}

Response (404 Not Found)

{
    "error": "Task not found"
}

4. Delete Task

DELETE /tasks/int:pk/

Description

Delete a task by its unique ID.

Headers

Key

Value

X-API-KEY

<my-api-key>

Response (200 OK)

{
    "message": "Task deleted successfully"
}

Response (404 Not Found)

{
    "error": "Task not found"
}

Authentication

This API uses an API key for authentication. The API key must be included in the X-API-KEY header for all requests.

Error Codes

Status Code
Description

200
Success

201
Resource Created

400
Bad Request

401
Unauthorized

404
Resource Not Found

500
Internal Server Error

