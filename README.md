# 📖 Library Management System

A REST API-based Library Management System where users can search for books, borrow, and return them while administrators manage books and users.

## 📌 Features
✔️ User authentication using **JWT tokens**  
✔️ **Role-based access control** (Admin & Users)  
✔️ **Book management** (CRUD operations by admin)  
✔️ **Book borrowing & returning** (Users can borrow and return books)  
✔️ **Search & Pagination** for books  
✔️ **Swagger API Documentation**  
✔️ **Unit Testing** for models and views  
✔️ **Deployment-ready** with Docker and Render  

## 📂 Project Structure
```
LibraryManagementSystemV2/
│── library_management/   # Main project folder
│   ├── settings.py       # Django settings
│   ├── urls.py           # Project-level URLs
│   ├── wsgi.py           # WSGI application entry point
│
│── users/                # User management (authentication)
│   ├── models.py         # User model (extended from Django User)
│   ├── views.py          # User-related API views
│   ├── serializers.py    # Serializers for user authentication
│   ├── urls.py           # User-related endpoints
│
│── books/                # Book management (CRUD)
│   ├── models.py         # Book model
│   ├── views.py          # API views for books
│   ├── serializers.py    # Serializers for books
│   ├── urls.py           # Book-related endpoints
│
│── loans/                # Borrowing & returning books
│   ├── models.py         # Loan model
│   ├── views.py          # API views for borrowing/returning
│   ├── serializers.py    # Serializers for loan transactions
│   ├── urls.py           # Loan-related endpoints
│
│── static/               # Static files
│── templates/            # HTML templates (if needed)
│── requirements.txt      # Dependencies
│── manage.py             # Django management script
│── .gitignore            # Git ignored files
│── README.md             # Project documentation
│── Dockerfile            # Docker setup for deployment
```

## 🛠 Technologies Used
- **Backend**: Django, Django REST Framework  
- **Database**: PostgreSQL (for production), SQLite (for development)  
- **Authentication**: JWT (JSON Web Tokens)  
- **API Documentation**: Swagger (drf-yasg)  
- **Containerization**: Docker  
- **Deployment**: Render  

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/Shrutikadeshmukh9/LibraryManagementSystemV2.git
cd LibraryManagementSystemV2
```

### 2️⃣ Create a virtual environment
```sh
python -m venv library_env
```
Activate the virtual environment:
- **Windows**: `library_env\Scripts\activate`
- **Mac/Linux**: `source library_env/bin/activate`

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply migrations & create superuser
```sh
python manage.py migrate
python manage.py createsuperuser
```

### 5️⃣ Run the server
```sh
python manage.py runserver
```
API will be available at: `http://127.0.0.1:8000/`

## 📡 API Endpoints
| Method | Endpoint | Description | Access |
|--------|----------|------------|--------|
| **POST** | `/users/register/` | Register a new user | Public |
| **POST** | `/users/login/` | Login and get JWT token | Public |
| **GET** | `/api/books/` | View all books | Public |
| **POST** | `/api/books/add/` | Add a new book | Admin Only |
| **DELETE** | `/api/books/{id}/delete/` | Delete a book | Admin Only |
| **POST** | `/api/loans/borrow/` | Borrow a book | Authenticated Users |
| **PUT** | `/api/loans/return/{id}/` | Return a book | Authenticated Users |

## 🔐 Authentication
- **JWT-based authentication** is used.
- Use `/users/login/` to get the access token.
- Pass the token in requests:  
  ```
  Authorization: Bearer <your_access_token>
  ```

## 📄 Testing
Run the test suite:
```sh
python manage.py test
```

## 📦 Docker Setup
Run the app in a Docker container:
```sh
docker build -t library-management .
docker run -p 8000:8000 library-management
```

## 🚀 Deploying to Render
### **1️⃣ Connect GitHub to Render**
- Go to **[Render](https://dashboard.render.com/)**
- Click **New Web Service** and connect your GitHub repository.

### **2️⃣ Configure Your Web Service**
- Choose a unique **service name**.
- Select **free instance**.
- Set **Build Command**:  
  ```sh
  pip install -r requirements.txt
  python manage.py migrate
  ```
- Set **Start Command**:  
  ```sh
  gunicorn library_management.wsgi:application --bind 0.0.0.0:8000
  ```

### **3️⃣ Set Environment Variables**
- In **Render Dashboard → Environment Variables**, add:
  ```sh
  DATABASE_URL=<your_postgresql_url>
  DJANGO_SECRET_KEY=<your_secret_key>
  DEBUG=False
  ```

### **4️⃣ Deploy**
- Click **Deploy** and wait for the build to finish.
- Once deployed, visit your app URL!

## 🎯 Future Enhancements
✅ User role-based dashboards  
✅ Email notifications for due books  
✅ Fine management system  
✅ Admin analytics panel  
