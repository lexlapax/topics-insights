# Topic Insights

A web application for analyzing and extracting insights from topics using LLM-based agents.

## Development Philosophy

This project follows a strict test-driven development (TDD) approach. All features must:
1. Start with tests before implementation
2. Maintain high test coverage (minimum 70%)
3. Run tests after every code change, no matter how trivial

## Current Status

### Implemented Features
- ✅ OpenAI GPT-4o agent integration
- ✅ Topic analysis capabilities
- ✅ Content summarization
- ✅ Entity extraction
- ✅ Question generation
- ✅ Test infrastructure with 70% coverage
- ✅ Environment configuration

### Pending Features
- ⏳ Frontend implementation
- ⏳ Database integration
- ⏳ User authentication
- ⏳ API endpoints
- ⏳ Background tasks

## Prerequisites

- Python 3.9 or higher
- Node.js 18.17.0 or higher (use nvm)
- Git

## Development Workflow

### 1. Write Tests First
```bash
# Create new test file
touch tests/new_feature_test.py

# Write tests
# Example:
def test_new_feature():
    result = new_feature()
    assert result == expected_value

# Run tests (should fail)
pytest tests/new_feature_test.py -v
```

### 2. Implement Feature
```bash
# Create implementation file
touch src/topic_insights/new_feature.py

# Implement feature
# Run tests frequently
pytest tests/new_feature_test.py -v
```

### 3. Refactor and Verify
```bash
# After implementation, run all tests
pytest

# Check coverage
pytest --cov=topic_insights --cov-report=term-missing

# Run linting
ruff check .
black .
```

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
pip install -e ".[dev]"

# Run tests (required before any development)
pytest  # Basic tests
pytest --cov  # With coverage
```

### 3. Environment Configuration

Create a `.env` file in the backend directory with the following content:
```bash
# OpenAI Configuration
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4o  # Recommended model for optimal performance

# Application Configuration
APP_ENV=development
DEBUG=True
LOG_LEVEL=INFO

# API Configuration
API_VERSION=v1
API_PREFIX=/api/v1
```

### 4. Example Usage

```python
from topic_insights.agents.openai_agent import OpenAIAgent
import asyncio

async def analyze_topic():
    agent = OpenAIAgent()
    await agent.initialize()
    
    try:
        result = await agent.analyze_topic("Climate change")
        print(result["analysis"])
        
        # Generate follow-up questions
        questions = await agent.generate_questions(result["analysis"])
        print("\nFollow-up questions:")
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
    finally:
        await agent.cleanup()

if __name__ == "__main__":
    asyncio.run(analyze_topic())
```

## Project Structure

```
topic-insights/
├── backend/
│   ├── src/
│   │   └── topic_insights/
│   │       ├── agents/
│   │       │   ├── base.py
│   │       │   └── openai_agent.py
│   │       └── main.py
│   ├── tests/  # Tests mirror src structure
│   │   └── agents/
│   │       └── test_openai_agent.py
│   ├── .env.example
│   └── pyproject.toml
└── frontend/
    └── [To be implemented]
```

## Development Guide for AI Agents (Cursor, GitHub Copilot, Codeium etc.)
### For Developers and AI Agents (Cursor, GitHub Copilot, Codeium etc. use this section as system prompts guidelines)

1. ***Pre-requisites and General Guidelines***
- read and understand all *.txt and *.md files starting in the root directory and recursively in all subdirectories
- load and understand all other files and web url links referenced in those files first.
- proactively load the reference files to create a context for the project before acting and responding to requests.
- understand the overall purpose of the project and the goals of the development team.
- understand the overall code base and the architecture of the project.
- documentation first
- testing code second


## License

MIT 

