"""Tests for services."""

import pytest
from unittest.mock import AsyncMock, patch

from app.models.narrative import NarrativeRequest, NarrativeDetails
from app.services.narrative_service import NarrativeService


@pytest.mark.asyncio
async def test_narrative_generation():
    """Test narrative service generation."""
    service = NarrativeService()

    request = NarrativeRequest(
        style="tokyo_drift_80s",
        theme="car_scene",
        mood="cinematic",
        details=NarrativeDetails(
            person_description="A stylish person",
            car_features="Modified drift car",
            setting="Urban street",
        ),
    )

    with patch.object(
        service.llm_service,
        "generate_narrative",
        new_callable=AsyncMock,
        return_value="Test narrative",
    ):
        response = await service.generate(request)

        assert response.narrative == "Test narrative"
        assert response.style == "tokyo_drift_80s"
        assert response.theme == "car_scene"
