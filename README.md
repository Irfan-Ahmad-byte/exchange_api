# 💱 Exchange Microservice (FastAPI + PostgreSQL + Docker)

A modular and production-ready exchange rate service built with **FastAPI**, **PostgreSQL**, and **Docker**. This microservice is part of a larger microservice ecosystem that includes an authentication service and an API gateway for routing and rate-limiting.

The goal of this service is to demonstrate:

- Scalable and maintainable backend architecture
- Clean code separation and modularity
- DevOps practices using Docker and GitHub Actions
- Tier-based access control using JWT and API Gateway routing

This service is designed to simulate a real-world financial API where users can retrieve exchange rates based on their subscription tier (free or premium). It integrates with other services such as:
- `jwt_authentication_service` for user management and token issuance
- `exchange_api_gateway` for central API routing and rate-limiting
- Other supporting microservices like `url_shortener_service`

---

## 🚀 Features

- 🔐 JWT-based user authentication (via Auth microservice)
- 🪙 Tier-based access control: free users get limited access, premium users get full access
- 📈 Mocked exchange rates fetched through internal logic
- 📦 PostgreSQL integration for future logging and analytics
- ♻️ Fully containerized with Docker
- ⚙️ Easily integrable with API gateways and other services

---

## 🧱 Tech Stack

- 🐍 FastAPI  
- 🐘 PostgreSQL  
- 🐳 Docker & Docker Compose  
- 📦 SQLAlchemy + Alembic  
- ⚙️ GitHub Actions (CI/CD ready)  

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/exchange_api.git
cd exchange_api
```

### 2. Create `.env` file 
Follow `.env.example` file to add Environment Variables.


### 3. Build and run with Docker
```bash
docker-compose up --build
```

API will be available at: http://localhost:8000


## 🔍 API Endpoints
- 🔸 GET /rate/{currency}

Provide symbol of a currency to get its rate against Dollars.

## 🧪 Testing
You can use:

- Postman
- cURL
- Or simple browser for redirection

## 📌 Future Improvements

## 👨‍💻 Author
Built with ❤️ by [Irfan Ahmad](!https://github.com/irfan-ahmad-byte)