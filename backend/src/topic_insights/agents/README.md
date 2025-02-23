# Topic Insights Agents

This directory contains the agent implementations for Topic Insights. The agents are responsible for analyzing topics, generating summaries, extracting entities, and generating follow-up questions.

## OpenAI Agent

The OpenAI agent uses GPT-4o by default for all operations. This provides optimal performance for our use case.

### Model Configuration

The agent can be configured to use different OpenAI models through environment variables or direct initialization:

```python
# Using environment variables (recommended)
OPENAI_MODEL=gpt-4o  # in .env file

# Or during initialization
agent = OpenAIAgent(model="gpt-4o")
```

### Available Models

The following models are supported and tested:

- `gpt-4o` (default, recommended for optimal performance)
- `gpt-4-turbo-preview` (alternative option)
- `gpt-4-0125-preview` (preview version)
- `gpt-3.5-turbo-0125` (faster but less capable)

### Usage Example

```python
from topic_insights.agents.openai_agent import OpenAIAgent

async def analyze_topic():
    agent = OpenAIAgent()  # Will use gpt-4o by default
    await agent.initialize()
    
    try:
        result = await agent.analyze_topic("Climate change")
        print(result["analysis"])
    finally:
        await agent.cleanup()
```

### Features

The OpenAI agent provides the following capabilities:

1. **Topic Analysis**: Deep analysis of topics with main themes, stakeholders, and trends
2. **Content Summarization**: Concise summaries of longer content
3. **Entity Extraction**: Identification of key entities in content
4. **Question Generation**: Generation of insightful follow-up questions

### Performance Considerations

- GPT-4o provides optimal performance and response quality
- Response times typically range from 2-5 seconds
- Token usage is automatically tracked and returned in responses
- Rate limiting is handled automatically by the OpenAI client

### Error Handling

The agent includes proper error handling for:
- Missing API keys
- Network issues
- Rate limiting
- Invalid responses

### Testing

The agent includes comprehensive tests that mock the OpenAI API calls. Run the tests with:

```bash
pytest tests/agents/test_openai_agent.py -v
``` 