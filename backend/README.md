# Topic Insights Backend

FastAPI-based backend service for Topic Insights application.

## Current State (2024-03-XX)
- ✅ Initial cleanup and dependency optimization
- ✅ Simplified health check implementation
- ✅ All tests passing with coverage
- ✅ Documentation updated to reflect current state

## Prerequisites

- Python 3.12.x (required, not 3.13)
- pip or uv package installer
- git

## Quick Start

1. **Create Virtual Environment**:
```bash
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Verify Python version
python --version  # Should show Python 3.12.x
```

2. **Install Dependencies**:
```bash
# Install uv for faster package installation
pip install uv

# Install project in editable mode with dev dependencies
uv pip install -e ".[dev]"
```

3. **Run Tests**:
```bash
# Run all tests with coverage
pytest --cov

# Run specific test file
pytest tests/test_health.py -v
```

4. **Start Development Server**:
```bash
uvicorn topic_insights.main:app --reload --port 8000
```

## Project Structure

```
backend/
├── src/
│   └── topic_insights/
│       ├── __init__.py
│       └── main.py          # FastAPI application
├── tests/
│   └── test_health.py       # Health endpoint tests
└── pyproject.toml          # Project configuration
```

## Available Endpoints

### Health Check
- `GET /` - Basic service status
  ```json
  {"status": "ok", "service": "Topic Insights API"}
  ```
- `GET /api/v1/health` - Detailed health status
  ```json
  {
    "status": "ok",
    "version": "0.1.0",
    "services": {
      "api": "healthy",
      "database": "not_configured",
      "llm": "not_configured"
    }
  }
  ```

## Development Tools

### Testing
```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov

# Run specific test
pytest tests/test_health.py -v
```

### Code Quality
```bash
# Format code
black .

# Lint code
ruff check .

# Type check
mypy .
```

### Dependencies
```bash
# Install only production dependencies
uv pip install -e "."

# Install with dev dependencies
uv pip install -e ".[dev]"
```

## Git Workflow

1. **Get Latest Code**:
```bash
git pull origin main
```

2. **Create Feature Branch**:
```bash
git checkout -b feature/backend-feature-name
```

3. **Make Changes**:
```bash
# Run tests
pytest
# Format and lint
black .
ruff check .
# Commit
git add .
git commit -m "feat: your backend feature description"
```

4. **Push Changes**:
```bash
git push origin feature/backend-feature-name
```

5. **Create Pull Request** on GitHub

## Troubleshooting

### Common Issues

1. **Wrong Python Version**
```bash
# Check version
python --version

# If incorrect:
deactivate
# Install Python 3.12.x and start over
```

2. **Package Installation Issues**
```bash
# Clean start
deactivate
rm -rf .venv
python3.12 -m venv .venv
source .venv/bin/activate
pip install uv
uv pip install -e ".[dev]"
```

3. **Test Failures**
```bash
# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_health.py -v
```

4. **Server Issues**
```bash
# Check port
lsof -i :8000  # On Unix/macOS
netstat -ano | findstr :8000  # On Windows

# Start with different port
uvicorn topic_insights.main:app --reload --port 8001
```

## License

MIT
