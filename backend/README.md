# Topic Insights Backend

FastAPI-based backend service for Topic Insights application.

## Setup

1. **Create Virtual Environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. **Install Dependencies**:
```bash
# Install uv for faster package installation
pip install uv

# Install project in editable mode with dev dependencies
uv pip install -e ".[dev]"
```

## Development Server

Run the development server with auto-reload:
```bash
uvicorn topic_insights.main:app --reload --port 8000
```

## Testing

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov

# Run tests with coverage HTML report
pytest --cov --cov-report=html

# Run specific test file
pytest tests/test_health.py
```

View coverage report by opening `htmlcov/index.html` in your browser.

## Project Structure

```
backend/
├── src/
│   └── topic_insights/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_health.py
├── pyproject.toml    # Project configuration and dependencies
└── README.md        # This file
```

## Current Features

- ✅ FastAPI application setup
- ✅ Health check endpoints
- ✅ CORS configuration
- ✅ Test infrastructure with pytest
- ✅ Code quality tools (Black, Ruff, MyPy)

## API Endpoints

### Health Check
- `GET /` - Basic service status
- `GET /api/v1/health` - Detailed health status including service components

## Development Tools

- **Formatting**: Black
  ```bash
  black .
  ```

- **Linting**: Ruff
  ```bash
  ruff check .
  ```

- **Type Checking**: MyPy
  ```bash
  mypy .
  ```

## Git Workflow

1. **Initial Setup**:
```bash
git init
git add .
git commit -m "feat: Initial backend setup"
```

2. **Development**:
```bash
git checkout -b feature/your-feature
# Make changes
git add .
git commit -m "feat: Add your feature"
```

## License

MIT
