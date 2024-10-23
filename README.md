A FastAPI-based application for managing and sharing daily expenses among friends and groups.

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Features

- User registration and authentication 🔐
- Create and manage expenses 💸
- Split expenses equally, by exact amounts, or percentages 🧮
- Generate balance sheets 📊
- RESTful API design 🌐

## 🛠 Tech Stack

- FastAPI 🚀
- PostgreSQL 🐘
- SQLAlchemy (Async) 🔄
- Pydantic 📝
- Docker 🐳
- Poetry 📦

## 🚀 Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/daily-expenses-app.git
cd daily-expenses-app
```

2. **Setup Environment**
```bash
pip install -r requirements.txt
```

3. **Run Docker Containers**
```bash
docker compose up --build
```

4. **Access the Application**
   - Open your browser and navigate to `http://localhost:8000/` to access the API.

## 🔗 API Endpoints

- `/users`: User management
- `/expenses`: Expense operations
- `/balance-sheet`: Generate balance sheets
