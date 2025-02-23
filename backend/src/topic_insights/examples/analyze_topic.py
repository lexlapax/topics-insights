import asyncio
import os
from dotenv import load_dotenv
from topic_insights.agents.openai_agent import OpenAIAgent

async def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Initialize the agent
    agent = OpenAIAgent()
    await agent.initialize()
    
    try:
        # Example topic to analyze
        topic = "Climate change impact on agriculture"
        
        print(f"\nAnalyzing topic: {topic}\n")
        
        # Analyze the topic
        analysis = await agent.analyze_topic(topic)
        print("Analysis:")
        print(analysis["analysis"])
        print(f"\nTokens used: {analysis['tokens_used']}")
        
        # Generate follow-up questions
        questions = await agent.generate_questions(analysis["analysis"])
        print("\nFollow-up questions:")
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
            
        # Extract entities
        entities = await agent.extract_entities(analysis["analysis"])
        print("\nExtracted entities:")
        print(entities)
        
    finally:
        # Clean up resources
        await agent.cleanup()

if __name__ == "__main__":
    asyncio.run(main()) 