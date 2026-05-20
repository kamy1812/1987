"""Tests for narrative endpoints."""

import pytest
from httpx import AsyncClient

from app.main import app
from app.models.narrative import NarrativeRequest, NarrativeDetails


@pytest.mark.asyncio
async def test_generate_narrative():
    """Test narrative generation endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        request_data = {
            "style": "tokyo_drift_80s",
            "theme": "car_scene",
            "mood": "cinematic",
            "details": {
                "person_description": "A person with 80s style",
                "car_features": "Modified drift car with neon accents",
                "setting": "Urban neon-lit street",
            },
        }

        response = await client.post("/api/v1/narratives/generate", json=request_data)
        assert response.status_code == 201
        data = response.json()
        assert "narrative" in data
        assert "id" in data
        assert data["style"] == "tokyo_drift_80s"


@pytest.mark.asyncio
async def test_get_styles():
    """Test styles endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/narratives/styles")
        assert response.status_code == 200
        data = response.json()
        assert "styles" in data
        assert len(data["styles"]) > 0


@pytest.mark.asyncio
async def test_get_themes():
    """Test themes endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/narratives/themes")
        assert response.status_code == 200
        data = response.json()
        assert "themes" in data
        assert len(data["themes"]) > 0


@pytest.mark.asyncio
async def test_get_moods():
    """Test moods endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/narratives/moods")
        assert response.status_code == 200
        data = response.json()
        assert "moods" in data
        assert len(data["moods"]) > 0
