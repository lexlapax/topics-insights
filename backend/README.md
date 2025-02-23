# Topic Insights Backend

FastAPI-based backend service for Topic Insights application.

## Repository

This is part of the [Topic Insights](https://github.com/lexlapax/topics-insights) project.

## Setup

1. **Clone Repository**:
```bash
git clone https://github.com/lexlapax/topics-insights.git
cd topics-insights/backend
```

2. **Create Virtual Environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**:
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
│       └── main.py          # FastAPI application
├── tests/
│   └── test_health.py       # Health endpoint tests
├── pyproject.toml          # Project configuration
└── README.md              # This file
```

## Current Features

- ✅ FastAPI 0.104.0 setup
- ✅ Health check endpoints
- ✅ CORS configuration
- ✅ Test infrastructure (pytest + coverage)
- ✅ Code quality tools (Black + Ruff + MyPy)
- ✅ Git integration

## TODO List

### High Priority
- [ ] Set up Supabase client and database schema
- [ ] Implement user authentication
- [ ] Create topic management endpoints
- [ ] Add error handling middleware

### Medium Priority
- [ ] Set up LLM integration
- [ ] Add request validation
- [ ] Implement rate limiting
- [ ] Add API documentation

### Low Priority
- [ ] Add logging system
- [ ] Implement background tasks
- [ ] Add metrics collection
- [ ] Create admin endpoints

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
# Make your changes
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

5. **Create Pull Request**:
- Visit: https://github.com/lexlapax/topics-insights/pulls
- Click "New Pull Request"
- Select your feature branch
- Add description and request review

## Troubleshooting

- **Tests fail**: Ensure virtual environment is activated and dependencies installed
- **Server won't start**: Check if port 8000 is in use
- **Import errors**: Verify you're in the correct directory with activated environment
- **Dependency issues**: Try removing .venv and reinstalling dependencies

## License

MIT
