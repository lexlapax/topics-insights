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

## Development Guidelines

### Test-First Development
- Write tests before implementing features
- Run tests after every code change
- Keep test coverage above 70%
- Tests should be descriptive and serve as documentation

### Code Style
- Backend: Black + Ruff for Python code
- Tests: pytest with asyncio support
- Type hints: Required for all Python code
- Documentation: Docstrings for all classes and functions

### Testing
Run tests with coverage:
```bash
pytest --cov=topic_insights --cov-report=term-missing
```

Current test coverage: 70%
- OpenAI agent: 91% coverage
- Base agent: 71% coverage

### Git Workflow
1. Create feature branch
2. Write tests for new feature
3. Run tests (should fail)
4. Implement feature
5. Run tests (should pass)
6. Refactor if needed (keep running tests)
7. Create pull request

## License

MIT 

## Development Guide for AI Agents (Cursor, GitHub Copilot, Codeium etc.)

### For Developers and AI Agents (Cursor, GitHub Copilot, Codeium etc. use this section as system prompts guidelines)


#### 1. Test File Creation
- Create test file BEFORE implementation file
- Test filename pattern: "test_*.py", "*.test.ts", or "*.test.js"
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
