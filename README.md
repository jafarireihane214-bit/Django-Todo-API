# Django Todo API

A RESTful API for a Todo List application built with Django and Django REST Framework, featuring JWT authentication.

## 🚀 Key Features
- **JWT Authentication:** Secure user login and registration using JSON Web Tokens.
- **CRUD Operations:** Create, Read, Update, and Delete tasks.
- **User-Specific Data:** Users can only view and manage their own tasks.
- **RESTful Design:** Clean and standard API endpoints using ViewSets and Routers.
- **Database:** SQLite (development) with Django ORM.

## 🛠️ Technologies Used
- **Framework:** Django
- **API:** Django REST Framework (DRF)
- **Authentication:** SimpleJWT
- **Language:** Python

## 📂 API Endpoints
- `POST /api/token/`: Obtain JWT access and refresh tokens.
- `POST /api/token/refresh/`: Refresh an expired access token.
- `GET /api/tasks/`: List all tasks for the authenticated user.
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/{id}/`: Retrieve a specific task.
- `PUT /api/tasks/{id}/`: Update a task.
- `DELETE /api/tasks/{id}/`: Delete a task.

## 👨‍💻 Developer
**Reyhaneh Jafari** - Computer Software Engineering
