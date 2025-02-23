# Topic Insights

A web application for analyzing and extracting insights from topics using LLM-based agents.

## Project Structure

```
.
├── backend/          # FastAPI backend service
├── frontend/         # Next.js frontend application
└── README.md        # This file
```

## Quick Start

### Prerequisites

- Python 3.9 or higher
- Node.js 18.17 or higher (recommended: use nvm)
- Git

### Backend Setup

1. **Setup Python Environment**:
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install uv
uv pip install -e ".[dev]"
```

2. **Run Backend**:
```bash
uvicorn topic_insights.main:app --reload --port 8000
```

3. **Run Tests**:
```bash
pytest  # Run basic tests
pytest --cov  # Run tests with coverage
```

The backend will be available at http://localhost:8000

### Frontend Setup

1. **Install Dependencies**:
```bash
cd frontend
npm install
```

2. **Run Frontend**:
```bash
npm run dev
```

3. **Run Tests**:
```bash
npm test           # Run tests
npm run test:watch # Run tests in watch mode
```

The frontend will be available at http://localhost:3000

## Verify Setup

1. Backend Health Check:
```bash
curl http://localhost:8000/api/v1/health
```

2. Frontend: Open http://localhost:3000 in your browser

## Current Features

### Backend
- ✅ Basic FastAPI setup
- ✅ Health check endpoints
- ✅ Test infrastructure
- ⏳ Supabase integration (pending)
- ⏳ LLM agent integration (pending)

### Frontend
- ✅ Next.js 14 setup
- ✅ React Query integration
- ✅ Chakra UI integration
- ✅ Basic health check page
- ✅ Test infrastructure
- ⏳ Topic analysis UI (pending)

## Development

### Git Workflow

1. **Initial Setup**:
```bash
git init
git add .
git commit -m "Initial commit: Project setup"
```

2. **Branch Strategy**:
- `main`: Production-ready code
- `develop`: Development branch
- Feature branches: `feature/feature-name`

### Code Style

- Backend: Black + Ruff for Python code
- Frontend: ESLint + Prettier for TypeScript/React code

## License

MIT 