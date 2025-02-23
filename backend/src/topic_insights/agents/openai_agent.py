from typing import Any, Dict, List, Optional
import os
from openai import AsyncOpenAI
from .base import BaseAgent

class OpenAIAgent(BaseAgent):
    """OpenAI-based implementation of the agent interface."""
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """Initialize the OpenAI agent.
        
        Args:
            api_key: Optional API key. If not provided, will use OPENAI_API_KEY env var.
            model: Optional model name. If not provided, will use OPENAI_MODEL env var or default to gpt-4o.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided and OPENAI_API_KEY env var not set")
            
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-4o")
        self.client = None
        
    async def initialize(self) -> None:
        """Initialize the OpenAI client."""
        self.client = AsyncOpenAI(api_key=self.api_key)
        
    async def analyze_topic(self, topic: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Analyze a topic using OpenAI."""
        if not self.client:
            await self.initialize()
            
        prompt = f"""Analyze the following topic and provide key insights:
Topic: {topic}
{f'Additional Context: {context}' if context else ''}

Please provide:
1. Main themes
2. Key stakeholders
3. Potential impact areas
4. Related topics
5. Current trends"""

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert analyst providing insights on topics."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return {
            "analysis": response.choices[0].message.content,
            "model": self.model,
            "tokens_used": response.usage.total_tokens
        }
        
    async def summarize_content(self, content: str, max_length: Optional[int] = None) -> str:
        """Generate a summary using OpenAI."""
        if not self.client:
            await self.initialize()
            
        length_guidance = f"in approximately {max_length} words" if max_length else "concisely"
        prompt = f"Please summarize the following content {length_guidance}, capturing the key points and main message:\n\n{content}"
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert at summarizing content accurately and concisely."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
        
    async def extract_entities(self, content: str) -> List[Dict[str, Any]]:
        """Extract entities using OpenAI."""
        if not self.client:
            await self.initialize()
            
        prompt = """Please analyze the following content and extract key entities in the following categories:
- People
- Organizations
- Locations
- Technologies
- Concepts
- Dates

Format the response as a JSON array where each item has 'entity', 'category', and 'relevance' (0-1) fields.

Content:
{content}"""
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert at entity extraction and analysis."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        return response.choices[0].message.content
        
    async def generate_questions(self, content: str, num_questions: int = 3) -> List[str]:
        """Generate follow-up questions using OpenAI."""
        if not self.client:
            await self.initialize()
            
        prompt = f"""Based on the following content, generate {num_questions} insightful follow-up questions that would help deepen understanding or explore related areas:

Content:
{content}"""
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert at generating insightful questions for further research."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # Parse the response into a list of questions
        questions_text = response.choices[0].message.content
        questions = [q.strip() for q in questions_text.split("\n") if q.strip()]
        return questions[:num_questions]
        
    async def cleanup(self) -> None:
        """Cleanup resources."""
        if self.client:
            await self.client.close()
            self.client = None 