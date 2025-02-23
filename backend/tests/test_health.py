import pytest
from fastapi.testclient import TestClient
from topic_insights.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns correct status."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "Topic Insights API"
    }

def test_health_check_endpoint():
    """Test the health check endpoint returns correct status and structure."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["version"] == "0.1.0"
    assert "services" in data
    assert all(service in data["services"] for service in ["api", "database", "llm"]) 