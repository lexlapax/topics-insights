# Topic Insights

A web application for analyzing and extracting insights from topics using LLM-based agents.

## Prerequisites

- Python 3.9 or higher
- Node.js 18.17.0 or higher (use nvm)
- Git

## Setup and Run Instructions

### 1. Clone Repository
```bash
git clone https://github.com/lexlapax/topics-insights.git
cd topics-insights
```

### 2. Backend Setup
```bash
# Navigate to backend
cd backend

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install uv
uv pip install -e ".[dev]"

# Run tests
pytest  # Basic tests
pytest --cov  # With coverage

# Start backend server
uvicorn topic_insights.main:app --reload --port 8000
```

### 3. Frontend Setup (in new terminal)
```bash
# Navigate to frontend
cd frontend

# Use correct Node.js version
nvm use 18.17.0  # Install if needed: nvm install 18.17.0

# Install dependencies
npm install

# Run tests
npm test  # Basic tests
npm run test:watch  # Watch mode

# Start frontend server
npm run dev
```

### 4. Verify Setup

1. Backend Health Check (in new terminal):
```bash
curl http://localhost:8000/api/v1/health
```
Expected output:
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

2. Frontend: Open http://localhost:3000 in your browser
- Should see Topic Insights homepage
- Health status section showing backend status
- Chakra UI styling applied

## Troubleshooting

### Backend
- **Tests fail**: Ensure virtual environment is activated and dependencies installed
- **Server won't start**: Check if port 8000 is in use
- **Import errors**: Verify you're in the correct directory with activated environment

### Frontend
- **Tests fail**: Verify Node.js version (18.17.0+)
- **Server won't start**: Check if port 3000 is in use
- **Module errors**: Run `npm install` again
- **Type errors**: Run `tsc --noEmit` to check types

## Current Features

### Backend
- ✅ Basic FastAPI setup
- ✅ Health check endpoints
- ✅ Test infrastructure
- ✅ Git integration
- ⏳ Supabase integration (pending)
- ⏳ LLM agent integration (pending)

### Frontend
- ✅ Next.js 14 setup
- ✅ React Query integration
- ✅ Chakra UI integration
- ✅ Basic health check page
- ✅ Test infrastructure
- ✅ Git integration
- ⏳ Topic analysis UI (pending)

## Development

### Git Workflow

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
# Make your changes
git add .
git commit -m "feat: your feature description"
```

4. **Push Changes**:
```bash
git push origin feature/your-feature-name
```

5. **Create Pull Request**:
- Visit: https://github.com/lexlapax/topics-insights/pulls
- Click "New Pull Request"
- Select your feature branch
- Add description and request review

### Branch Protection Rules

The `main` branch is protected with the following rules:
- Require pull request before merging
- Require 1 approval for pull requests
- Dismiss stale pull request approvals when new commits are pushed
- Require conversation resolution before merging
- No direct pushes to main branch

### Code Style

- Backend: Black + Ruff for Python code
- Frontend: ESLint + Prettier for TypeScript/React code

## License

MIT 