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
│       ├── main.py          # FastAPI application
│       ├── agents/          # LLM agents and tools
│       │   ├── __init__.py
│       │   ├── base.py     # Base agent classes
│       │   └── tools.py    # Custom agent tools
│       └── models/         # Pydantic models
│           ├── __init__.py
│           └── agents.py   # Agent-related models
├── tests/
│   ├── test_health.py      # Health endpoint tests
│   └── test_agents/       # Agent tests
├── pyproject.toml         # Project configuration
└── README.md             # This file
```

## Current Features

- ✅ FastAPI 0.104.0 setup
- ✅ Health check endpoints
- ✅ CORS configuration
- ✅ Test infrastructure (pytest + coverage)
- ✅ Code quality tools (Black + Ruff + MyPy)
- ✅ Git integration
- ⏳ LLM integration with Pydantic-AI (in progress)

## LLM Integration with Pydantic-AI

### Overview
The project uses Pydantic-AI for LLM-powered agents that analyze and extract insights from topics. This integration provides:
- Type-safe LLM function calls
- Structured agent interactions
- Built-in validation and parsing
- Support for multiple LLM providers

### Setup LLM Integration

1. **Install Additional Dependencies**:
```bash
uv pip install "pydantic-ai[all]" "openai>=1.0.0" "instructor"
```

2. **Configure Environment Variables**:
```bash
# Add to .env file
OPENAI_API_KEY=your_api_key_here
ANTHROPIC_API_KEY=your_api_key_here  # If using Claude
```

### Agent Architecture

The project uses a multi-agent system for topic analysis:

1. **Topic Analyzer Agent**
   - Analyzes topic content and structure
   - Extracts key themes and patterns
   - Uses Pydantic models for structured output

2. **Insight Generator Agent**
   - Generates insights based on analysis
   - Provides recommendations and connections
   - Validates outputs against defined schemas

### Example Agent Usage

```python
from pydantic_ai import Agent, Tool
from pydantic import BaseModel

class TopicAnalysis(BaseModel):
    main_themes: list[str]
    key_insights: list[str]
    sentiment: str

class TopicAnalyzer(Agent):
    def analyze_topic(self, content: str) -> TopicAnalysis:
        """Analyze the given topic content."""
        return self.run(
            system_prompt="You are a topic analysis expert...",
            human_message=f"Analyze this topic: {content}",
            output_model=TopicAnalysis
        )
```

### Available Tools

The agents have access to various tools:
- Content Summarization
- Sentiment Analysis
- Theme Extraction
- Pattern Recognition
- Cross-Reference Analysis

### Best Practices

1. **Prompt Engineering**
   - Use clear and specific system prompts
   - Include examples in few-shot prompts
   - Validate outputs against schemas

2. **Error Handling**
   - Handle LLM API errors gracefully
   - Implement retry mechanisms
   - Validate responses against expected formats

3. **Cost Management**
   - Use appropriate model tiers
   - Implement token counting
   - Cache responses when possible

### Testing Agents

```python
# In tests/test_agents/test_analyzer.py
from topic_insights.agents import TopicAnalyzer

def test_topic_analysis():
    analyzer = TopicAnalyzer()
    result = analyzer.analyze_topic("Sample topic content...")
    assert isinstance(result, TopicAnalysis)
    assert len(result.main_themes) > 0
```

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
