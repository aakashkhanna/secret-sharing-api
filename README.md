# 🚀 Secret Sharing API

A lightweight FastAPI-based service to securely store and retrieve secrets using one-time tokens. Secrets are stored temporarily with TTL (Time-To-Live) and are deleted after first access.

🔗 **Live Demo**: [https://secret-sharing-api-aakashkhanna3051-ova9fte2.leapcell.dev/docs](https://secret-sharing-api-aakashkhanna3051-ova9fte2.leapcell.dev/docs)


---

## ✅ Features

- `POST /post-secret/`: Store a secret and get a unique token.
- `GET /get-secret/{token}`: Retrieve and delete the secret using the token.
- TTL support: Secrets expire automatically after a set time (default: 60 minutes).
- Storage support: Redis (default) or DynamoDB (pluggable).
- Auto-generated OpenAPI docs.

---

## ⚙️ Environment Setup

### Prerequisites

- Python 3.11+
- Poetry
- Redis (running locally or remote)

### Steps

```bash
git clone https://github.com/aakashkhanna/secret-sharing-api.git
poetry install
poetry run uvicorn secret_sharing_api.main:app --reload
````

API Docs:

* Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔐 Configuration

To use Redis, configure:

```env
REDIS_HOST=redis://localhost:6379/0
REDIS_PORT=50
REDIS_SECRET=secret
```

To use DynamoDB, configure:

```env
AWS_ENDPOINT_URL=
AWS_REGION_NAME=
AWS_DYNAMO_NAME=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

---

## 🧪 Testing

```bash
poetry run pytest
```

---

## 🤝 Contributing

* Fork this repo
* Create a new branch: `git checkout -b feature/xyz`
* Submit a PR

---
