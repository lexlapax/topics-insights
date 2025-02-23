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

## Test-First Development Guide

### For Developers and AI Agents (Cursor, GitHub Copilot, etc.)

#### 1. Test File Creation
- Create test file BEFORE implementation file
- Test filename pattern: `test_*.py`
- Place tests in parallel structure to source:
  ```
  src/topic_insights/feature/
  tests/feature/test_feature.py
  ```

#### 2. Test Writing Sequence
1. Write imports and setup
2. Write test class (if needed)
3. Write individual test functions
4. Add test fixtures
5. Add mock configurations
6. ONLY THEN proceed to implementation

Example:
```python
# tests/agents/test_new_agent.py
import pytest
from unittest.mock import AsyncMock, patch
from topic_insights.agents.new_agent import NewAgent

@pytest.fixture
async def agent():
    """Create agent for testing."""
    agent = NewAgent(api_key="test-key")
    await agent.initialize()
    yield agent
    await agent.cleanup()

@pytest.mark.asyncio
async def test_process_content():
    """Test content processing functionality."""
    # Arrange
    content = "Test content"
    expected = {"summary": "Test", "tokens": 100}
    
    # Act
    result = await agent.process_content(content)
    
    # Assert
    assert result["summary"] == expected["summary"]
    assert result["tokens"] == expected["tokens"]
```

#### 3. AI Agent Guidelines

When using AI assistance (Cursor, GitHub Copilot):

1. **Test Request Format**
   ```
   Create tests for [feature] that:
   - Test happy path
   - Test edge cases: [list cases]
   - Mock external dependencies
   - Include async handling
   - Verify error conditions
   ```

2. **Implementation Request Format**
   ```
   Implement [feature] to pass these tests:
   [paste test code]
   Requirements:
   - Match test specifications
   - Handle edge cases
   - Include error handling
   - Add type hints
   - Add docstrings
   ```

3. **Refactoring Request Format**
   ```
   Refactor [code] while maintaining test compliance:
   - Improve [specific aspect]
   - Maintain test coverage
   - Keep existing functionality
   ```

#### 4. Test Categories

1. **Unit Tests**
   - Test individual functions/methods
   - Mock all external dependencies
   - Fast execution
   ```python
   def test_summarize():
       text = "Long text here"
       result = summarize(text, max_length=50)
       assert len(result) <= 50
   ```

2. **Integration Tests**
   - Test component interactions
   - Minimal mocking
   - Real database/cache usage
   ```python
   async def test_agent_with_database():
       agent = Agent(db_connection=real_db)
       result = await agent.process_and_store("data")
       stored = await db.get_result(result.id)
       assert stored == result
   ```

3. **Edge Case Tests**
   - Empty inputs
   - Maximum values
   - Invalid data
   - Resource limitations
   ```python
   @pytest.mark.parametrize("invalid_input", [
       "",
       "x" * 1000000,  # Very long input
       None,
       123,  # Wrong type
   ])
   def test_invalid_inputs(invalid_input):
       with pytest.raises(ValueError):
           process_input(invalid_input)
   ```

#### 5. Coverage Requirements

Minimum coverage requirements by component:
- Core business logic: 90%
- API endpoints: 85%
- Utility functions: 80%
- Overall project: 70%

Check coverage:
```bash
pytest --cov=topic_insights --cov-report=html
```

#### 6. Test Performance

- Unit tests: < 100ms each
- Integration tests: < 1s each
- Full suite: < 2 minutes
- Run slow tests with marker:
  ```python
  @pytest.mark.slow
  def test_long_running():
      ...
  ```

#### 7. Continuous Testing

```bash
# Watch mode for TDD
ptw --runner "pytest --testmon"

# Run specific test categories
pytest tests/unit  # Unit tests
pytest tests/integration  # Integration tests
pytest -m "not slow"  # Skip slow tests
```

#### 8. Mocking Guidelines

1. **External Services**
```python
@patch("topic_insights.services.openai.AsyncOpenAI")
async def test_with_mock(mock_openai):
    mock_openai.return_value.chat.completions.create.return_value = {
        "choices": [{"message": {"content": "mocked response"}}]
    }
```

2. **Databases**
```python
@pytest.fixture
def mock_db():
    return MockDatabase(
        query_result={"id": 1, "data": "test"},
        expected_calls=1
    )
```

3. **Time-based Functions**
```python
@freeze_time("2024-02-23")
def test_time_dependent():
    assert get_current_date() == "2024-02-23"
```

#### 9. Test Data Management

1. **Fixtures Location**
```
tests/
  └── fixtures/
      ├── vcr_cassettes/
      ├── test_data.json
      └── mock_responses.py
```

2. **Factory Pattern**
```python
@pytest.fixture
def make_test_data():
    def _make_test_data(override=None):
        data = {"id": 1, "name": "test"}
        if override:
            data.update(override)
        return data
    return _make_test_data
```

## Development Setup

[Rest of the original setup instructions...]
