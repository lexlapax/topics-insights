"""
Topic Insights Backend Entry Point
"""

from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Topic Insights API",
    description="API for Topic Insights content aggregation and analysis",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok", "service": "Topic Insights API"}


@app.get("/api/v1/health")
async def health_check() -> dict[str, Any]:
    """Detailed health check endpoint."""
    return {
        "status": "ok",
        "version": "0.1.0",
        "services": {
            "api": "healthy",
            "database": "not_configured",  # Will be updated when Supabase is configured
            "llm": "not_configured",  # Will be updated when LLM is configured
        },
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("topic_insights.main:app", host="0.0.0.0", port=8000, reload=True)
