# ⚙️ Environment Configuration Management

## 📌 Overview

The platform uses environment-based configuration following the **Twelve-Factor App methodology**, ensuring configuration values remain separate from application code.

This enables portability across development, staging, and production environments without rebuilding container images.

---

## 🧭 Environment File Location

The `.env` file must be created in the **project root directory**.

```text
ai-powered-devops-platform/
│
├── .env
├── app/
├── nginx/
├── docker/
└── docs/
```

---

## 🧾 Example `.env`

```env
APP_PORT=8000
APP_NAME=AI DevOps Platform
ENVIRONMENT=development
```

---

## 🐳 Docker Compose Integration

Environment variables are injected into containers using Docker Compose.

```yaml
app:
  build: ../app
  env_file:
    - ../.env
```

Docker automatically loads variables during container startup.

---

## 🧠 Application Usage

Environment variables are accessed inside the FastAPI application using:

```python
import os

os.getenv("APP_NAME")
```

This prevents configuration hardcoding.

---

## 🔄 Applying Configuration Changes

After updating `.env`, rebuild containers:

```bash
docker compose down
docker compose up -d --build
```

---

## 🔐 Security Best Practice

`.env` files must never be committed to Git.

Add to `.gitignore`:

```text
.env
```

---

## ❤️ Health Check Endpoint

The application exposes a standard health endpoint:

```
/health
```

Example:

```
http://<EC2-PUBLIC-IP>/health
```

Used by:

* Load balancers
* Monitoring systems
* Kubernetes probes
* Auto-healing mechanisms

---

## ✅ Outcome

The platform now supports:

* Runtime configuration injection
* Environment portability
* Secure secret handling
* Production-ready deployment configuration

