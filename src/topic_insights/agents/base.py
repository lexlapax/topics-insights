from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

class TopicAnalysisResult(BaseModel):
    summary: str = Field(description='Concise topic summary')
    entities: list[str] = Field(description='Key entities extracted')
    relevance_score: int = Field(description='Topic relevance', ge=0, le=10)

@dataclass
class TopicDependencies:
    api_keys: dict
    content_sources: list[str]

topic_agent = Agent(
    'openai:gpt-4',
    deps_type=TopicDependencies,
    result_type=TopicAnalysisResult,
    system_prompt='You are a topic analysis expert...'
) 