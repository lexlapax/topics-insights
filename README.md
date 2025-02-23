# Topic Insights

A modern web application for topic analysis and insights.

## Current State (2024-03-XX)

### Recent Changes
- ✅ Initial cleanup and dependency optimization
- ✅ Simplified codebase structure
- ✅ Removed unnecessary dependencies
- ✅ All tests passing with coverage
- ✅ Documentation updated to reflect current state

### Frontend
- Next.js 14.1.0 with App Router
- React Query v5
- Chakra UI v2
- Jest + React Testing Library
- TypeScript, ESLint, Prettier

### Backend
- FastAPI with Python 3.12.x
- Pytest with coverage
- Black, Ruff, MyPy
- Minimal health check API

## Prerequisites

### Backend
- Python 3.12.x (required, not 3.13)
- pip or uv package installer

### Frontend
- Node.js 20.x LTS
- npm or yarn

## Quick Start

1. **Clone Repository**:
```bash
git clone https://github.com/lexlapax/topics-insights.git
cd topics-insights
```

2. **Backend Setup**:
```bash
cd backend

# Create virtual environment
python3.12 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install uv
uv pip install -e ".[dev]"

# Run tests
pytest --cov

# Start server
uvicorn topic_insights.main:app --reload --port 8000
```

3. **Frontend Setup**:
```bash
cd ../frontend

# Install dependencies
npm install

# Run tests
npm run test:coverage

# Start development server
npm run dev
```

Visit:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Project Structure

```
.
├── backend/
│   ├── src/
│   │   └── topic_insights/
│   │       ├── __init__.py
│   │       └── main.py
│   ├── tests/
│   └── pyproject.toml
│
├── frontend/
│   ├── src/
│   │   └── app/
│   │       ├── layout.tsx
│   │       ├── page.tsx
│   │       └── providers.tsx
│   ├── __tests__/
│   └── package.json
│
└── README.md
```

## Available Endpoints

### Backend
- `GET /` - Basic service status
- `GET /api/v1/health` - Detailed health status

### Frontend
- `/` - Home page with service status

## Development

### Running Tests

**Backend**:
```bash
cd backend
pytest --cov
```

**Frontend**:
```bash
cd frontend
npm run test:coverage
```

### Code Quality

**Backend**:
```bash
cd backend
black .      # Format
ruff check . # Lint
mypy .       # Type check
```

**Frontend**:
```bash
cd frontend
npm run format     # Format
npm run lint      # Lint
npm run type-check # Type check
```

## Git Workflow

1. **Get Latest Code**:
```bash
git pull origin main
```

2. **Create Feature Branch**:
```bash
git checkout -b feature/your-feature-name
```

3. **Make Changes**:
```bash
# Run tests
cd backend && pytest
cd ../frontend && npm run test

# Format and lint
cd backend && black . && ruff check .
cd ../frontend && npm run format && npm run lint

# Commit
git add .
git commit -m "feat: your feature description"
```

4. **Push Changes**:
```bash
git push origin feature/your-feature-name
```

5. **Create Pull Request** on GitHub

## Troubleshooting

### Backend Issues

1. **Wrong Python Version**
```bash
# Check version
python --version  # Should be 3.12.x

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

### Frontend Issues

1. **Wrong Node Version**
```bash
# Check version
node --version  # Should be 20.x LTS

# If incorrect:
# Install Node.js 20.x LTS
```

2. **Module Resolution Issues**
```bash
# Clean install
rm -rf node_modules .next
npm install
```

## License

MIT 