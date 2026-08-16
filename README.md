# Nexora — Business Intelligence & Analytics Platform

[![CI](https://github.com/VasanthaGudapati/Nexora/actions/workflows/ci.yml/badge.svg)](https://github.com/VasanthaGudapati/Nexora/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat&logo=FastAPI&logoColor=white)
![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)

**Nexora** is an e-commerce and business intelligence platform designed to ingest, validate, store, analyze, and visualize core business data (Customers, Products, Orders, Order Items, Payments, and Sales).

---

## 🎯 Current Focus: Stage 1 — Backend Core Foundation

Nexora is built incrementally, starting with a clean Python and FastAPI core before expanding into persistent databases, frontend dashboards, and advanced analytics modules.

### ✨ Key Principles
- **Incremental & Modular**: Features are built and tested step-by-step.
- **Clean Architecture**: Decoupled core settings, API routes, schemas, and test suites.
- **Continuous Integration**: Automated CI pipeline running linting and tests on every push and pull request.
- **Test-Driven Foundation**: Core functionality paired with automated unit tests.

---

## 📁 Repository Structure

```text
Nexora/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                   # GitHub Actions CI workflow
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md            # Issue template for bug reports
│   │   └── feature_request.md       # Issue template for feature requests
│   └── PULL_REQUEST_TEMPLATE.md     # Pull request template
├── backend/
│   ├── app/
│   │   ├── api/                     # API routers and endpoints
│   │   │   └── __init__.py
│   │   ├── core/                    # Core configuration and settings
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── main.py                  # FastAPI application entrypoint
│   └── tests/
│       ├── __init__.py
│       └── test_health.py           # Health check test suite
├── .gitignore
├── CONTRIBUTING.md                  # Contribution guidelines
├── pytest.ini                       # Pytest test discovery and config
├── requirements.txt                 # Project dependencies
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone & Set Up Virtual Environment

```bash
# Clone the repository
git clone https://github.com/VasanthaGudapati/Nexora.git
cd Nexora

# Create and activate virtual environment
# On Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

# On Linux / macOS:
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Run the Development Server

```bash
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
```

- **API Base URL**: `http://127.0.0.1:8000`
- **Interactive Swagger Docs**: `http://127.0.0.1:8000/docs`
- **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`
- **Health Check Endpoint**: `http://127.0.0.1:8000/health`

---

## 🧪 Running Automated Tests

Run the test suite using `pytest`:

```bash
pytest
```

---

## 🗺️ Roadmap & Planned Stages

- [x] **Stage 1**: Core Backend Foundation, Health Check & CI Pipeline
- [ ] **Stage 2**: Pydantic Data Models & Validation Schemas (Customers, Products, Orders, Payments, Sales)
- [ ] **Stage 3**: Database Layer & ORM Models (SQLAlchemy / PostgreSQL)
- [ ] **Stage 4**: Business Intelligence & Analytics Engine (Metrics Aggregations, Trends, KPIs)
- [ ] **Stage 5**: Visualization Dashboard (Interactive Web UI)

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](file:///D:/Nexora/CONTRIBUTING.md) for details on our code style, test requirements, and pull request process.
