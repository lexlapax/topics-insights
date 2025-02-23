from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class BaseAgent(ABC):
    """Base class for all agents in the system."""
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize any resources needed by the agent."""
        pass
    
    @abstractmethod
    async def analyze_topic(self, topic: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Analyze a topic and return insights."""
        pass
    
    @abstractmethod
    async def summarize_content(self, content: str, max_length: Optional[int] = None) -> str:
        """Generate a summary of the provided content."""
        pass
    
    @abstractmethod
    async def extract_entities(self, content: str) -> List[Dict[str, Any]]:
        """Extract named entities and key concepts from content."""
        pass
    
    @abstractmethod
    async def generate_questions(self, content: str, num_questions: int = 3) -> List[str]:
        """Generate follow-up questions based on the content."""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Cleanup any resources used by the agent."""
        pass 