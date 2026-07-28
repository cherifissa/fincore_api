# 🚀 FinCore API

> A production-ready open-source FinTech REST API built with Flask, PostgreSQL and Docker.

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)]()
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue.svg)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success.svg)]()

---

## 📖 Overview

FinCore API is a modern **FinTech backend** designed with production best practices in mind.

It provides secure user authentication, account management, money transfers, transaction history, and ledger management while following a scalable architecture.

This project is intended for:

- Learning Backend Engineering
- Learning FinTech Architecture
- Portfolio Projects
- Open Source Contributions
- Production-ready REST API development

---

## ✨ Features

### Authentication

- JWT Authentication
- Refresh Tokens
- Password Hashing (bcrypt)
- Role-Based Access Control (RBAC)
- Secure Logout

---

### Users

- User Registration
- User Login
- User Profile
- Update Profile
- Soft Delete
- Admin Management

---

### Accounts

- Create Accounts
- Multiple Accounts per User
- Balance Management
- Account Status
- Currency Support

---

### Transactions

- Deposit
- Withdrawal
- Transfer
- Transaction History
- Transaction Reference
- Transaction Status

---

### Ledger

Every financial operation generates immutable ledger entries.

No balance is directly modified without a corresponding accounting record.

---

### Security

- JWT
- Password Hashing
- Input Validation
- Environment Variables
- CORS Protection
- Secure Headers
- Rate Limiting

---

### DevOps

- Docker
- Docker Compose
- PostgreSQL
- GitHub Actions
- Automated Tests
- Code Formatting
- Linting
- Continuous Integration

---

## 🏗️ Project Structure

```
fincore-api/
│
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── repositories/
│   ├── schemas/
│   ├── middleware/
│   ├── utils/
│   ├── config.py
│   └── __init__.py
│
├── migrations/
├── tests/
├── docker/
├── docs/
├── scripts/
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── Makefile
├── .env.example
└── README.md
```

---

## 🛠️ Technology Stack

| Category         | Technology        |
| ---------------- | ----------------- |
| Backend          | Flask             |
| Database         | PostgreSQL        |
| ORM              | SQLAlchemy        |
| Migration        | Alembic           |
| Authentication   | JWT               |
| Cache            | Redis             |
| Documentation    | OpenAPI / Swagger |
| Testing          | Pytest            |
| Formatting       | Black             |
| Linting          | Ruff              |
| Type Checking    | MyPy              |
| CI/CD            | GitHub Actions    |
| Containerization | Docker            |

---

## 📊 Architecture

```
                Client

                   │

           REST API (Flask)

                   │

     ┌─────────────┴─────────────┐

 Authentication            Business Logic

     │                             │

Repositories            Services

     │                             │

          SQLAlchemy ORM

                   │

             PostgreSQL
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/fincore-api.git
cd fincore-api
```

### Install uv

```bash
pip install uv
```

or

```bash
brew install uv
```

### Create the virtual environment

```bash
uv venv
```

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

### Install dependencies

```bash
uv sync
```

### Configure environment variables

```bash
cp .env.example .env
```

### Start PostgreSQL

```bash
docker compose up -d
```

### Run migrations

```bash
flask db upgrade
```

### Start the API

```bash
flask run
```

## 🐳 Docker

Start PostgreSQL

```bash
docker compose up -d postgres
```

Start Redis

```bash
docker compose up -d redis
```

Start everything

```bash
docker compose up --build
```

## 📜 Logging

FinCore API includes structured logging to simplify debugging and monitoring.

### Features

- Structured logs
- Console logging
- File logging
- Log rotation
- Request logging
- Error logging
- SQLAlchemy query logging (optional)
- Environment-based log levels

### Log Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Example:

```
2026-07-28 10:32:15 | INFO | POST /api/v1/auth/login | 200 | user_id=15

2026-07-28 10:33:01 | ERROR | Transfer failed | insufficient_balance
```

Logs are stored in:

```
logs/
├── app.log
├── error.log
└── access.log
```

---

## 📚 API Documentation

Swagger UI

```
http://localhost:5000/docs
```

OpenAPI JSON

```
/openapi.json
```

---

## 🔑 API Endpoints

### Authentication

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |
| POST   | /auth/refresh  |
| POST   | /auth/logout   |

---

### Users

| Method | Endpoint    |
| ------ | ----------- |
| GET    | /users      |
| GET    | /users/{id} |
| PUT    | /users/{id} |
| DELETE | /users/{id} |

---

### Accounts

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /accounts      |
| GET    | /accounts      |
| GET    | /accounts/{id} |

---

### Transactions

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | /transactions/deposit  |
| POST   | /transactions/withdraw |
| POST   | /transactions/transfer |
| GET    | /transactions          |

---

## 🧪 Running Tests

```bash
pytest
```

Coverage

```bash
pytest --cov=app
```

---

## 🔄 CI/CD

Every push and pull request automatically runs:

- Install dependencies
- Ruff
- Black
- MyPy
- Pytest
- Coverage
- Docker Build

---

## 📈 Roadmap

- [x] Authentication
- [x] User Management
- [x] Accounts
- [x] Transactions
- [x] Ledger
- [x] Docker Support
- [x] GitHub Actions
- [ ] Redis Caching
- [ ] Email Notifications
- [ ] Two-Factor Authentication
- [ ] Fraud Detection API
- [ ] Prometheus Metrics
- [ ] Grafana Dashboard
- [ ] Kubernetes Deployment

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 📝 Code Style

This project uses:

- Black
- Ruff
- MyPy
- Pre-commit Hooks

Please ensure your code passes all checks before submitting a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Cherif Issa Mahamat**

AI Engineer • Backend Developer • Open Source Enthusiast

LinkedIn

> https://www.linkedin.com/in/cherif-issa-mahamat

GitHub

> https://github.com/yourusername

---

## ⭐ Support

If you find this project useful:

⭐ Star the repository

🍴 Fork the project

🛠️ Contribute to the codebase

📢 Share it with the community

---

**Building secure and scalable financial systems with Python, Flask, and modern DevOps.**
