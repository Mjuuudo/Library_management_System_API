## 🚀 Features

- 🔐 JWT Authentication (Login / Register)
- 👩‍💼 User & Author Management
- 📖 Book CRUD Operations
- 📅 Borrowing System with Return Tracking
- 🧠 Role-based Access (user-specific borrowings)

## 🏗️ Tech Stack

- **Python 3.10+**
- **Django 5**
- **Django REST Framework**
- **djangorestframework-simplejwt** (for authentication)
- **SQLite3** (default database)


## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Library_Management_System_API.git
   cd Library_Management_System_API

   python3 -m venv venv
   source venv/bin/activate

   pip install -r requirements.txt

   python manage.py makemigrations
   python manage.py migrate

   python manage.py runserver

### Method	Endpoint	Description

POST	/api/register/	Register new user
POST	/api/token/	Obtain JWT access & refresh token
POST	/api/token/refresh/	Refresh JWT token


Authors	/api/authors/	GET, POST /	List or create authors
Books	/api/books/	GET, POST	/ List or add books
Borrowings	/api/borrowings/	GET, POST	/ Borrow or view borrowed books



Tests

Creating Users '/register/'

{
  "username": "test34",
  "email": "saraxw@example.com",
  "password": "test3"
}

login from tokens

{
  "username": "Admin",
  "password": "lezaraki/0"
}

creating a new book 

{
  "Book_title": "1984",
  "Author": 2,
  "posted_Date": "2025-10-16",
  "Number_of_Copies": 4,
  "Is_Alvalible": true
}

Borrow a book 

{
  "Book_id": 1,
  "Return_Date": "2025-10-25T15:00:00Z"
}

