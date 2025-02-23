import pytest
from unittest.mock import AsyncMock, patch
from topic_insights.agents.openai_agent import OpenAIAgent

@pytest.fixture
async def agent():
    """Create an OpenAI agent for testing."""
    agent = OpenAIAgent(api_key="test-key", model="gpt-4o")
    await agent.initialize()
    yield agent
    await agent.cleanup()

@pytest.mark.asyncio
async def test_analyze_topic(agent):
    """Test topic analysis functionality."""
    with patch.object(agent.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value.choices = [
            AsyncMock(message=AsyncMock(content="Test analysis"))
        ]
        mock_create.return_value.usage = AsyncMock(total_tokens=100)
        
        result = await agent.analyze_topic("artificial intelligence")
        
        assert result["analysis"] == "Test analysis"
        assert result["model"] == "gpt-4o"
        assert result["tokens_used"] == 100
        mock_create.assert_called_once()

@pytest.mark.asyncio
async def test_summarize_content(agent):
    """Test content summarization."""
    with patch.object(agent.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value.choices = [
            AsyncMock(message=AsyncMock(content="Test summary"))
        ]
        
        result = await agent.summarize_content("Long content here", max_length=50)
        
        assert result == "Test summary"
        mock_create.assert_called_once()

@pytest.mark.asyncio
async def test_extract_entities(agent):
    """Test entity extraction."""
    mock_entities = '[{"entity": "OpenAI", "category": "Organization", "relevance": 0.9}]'
    with patch.object(agent.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value.choices = [
            AsyncMock(message=AsyncMock(content=mock_entities))
        ]
        
        result = await agent.extract_entities("OpenAI is a company")
        
        assert result == mock_entities
        mock_create.assert_called_once()

@pytest.mark.asyncio
async def test_generate_questions(agent):
    """Test question generation."""
    with patch.object(agent.client.chat.completions, 'create', new_callable=AsyncMock) as mock_create:
        mock_create.return_value.choices = [
            AsyncMock(message=AsyncMock(content="1. First question?\n2. Second question?"))
        ]
        
        result = await agent.generate_questions("Test content", num_questions=2)
        
        assert len(result) == 2
        assert all(q.endswith("?") for q in result)
        mock_create.assert_called_once()

@pytest.mark.asyncio
async def test_initialization_without_api_key():
    """Test that initialization fails without API key."""
    with pytest.raises(ValueError):
        OpenAIAgent(api_key=None)

@pytest.mark.asyncio
async def test_cleanup(agent):
    """Test cleanup functionality."""
    await agent.cleanup()
    assert agent.client is None 