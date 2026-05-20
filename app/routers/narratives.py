"""Narrative API endpoints."""

from fastapi import APIRouter, HTTPException, status
import logging

from app.models.narrative import NarrativeRequest, NarrativeResponse
from app.services.narrative_service import NarrativeService

logger = logging.getLogger(__name__)
router = APIRouter()
narrative_service = NarrativeService()


@router.post(
    "/narratives/generate",
    response_model=NarrativeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Generate a narrative",
    description="Generate a vivid narrative based on provided parameters",
)
async def generate_narrative(request: NarrativeRequest) -> NarrativeResponse:
    """Generate a creative narrative.

    Args:
        request: NarrativeRequest with generation parameters

    Returns:
        NarrativeResponse with generated narrative

    Raises:
        HTTPException: If generation fails
    """
    try:
        response = await narrative_service.generate(request)
        return response
    except Exception as e:
        logger.error(f"Error generating narrative: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate narrative",
        )


@router.get(
    "/narratives/styles",
    summary="Get available narrative styles",
    description="List all available narrative generation styles",
)
async def get_styles() -> dict:
    """Get available narrative styles.

    Returns:
        Dictionary of available styles
    """
    return {
        "styles": [
            "tokyo_drift_80s",
            "cyberpunk",
            "noir",
            "fantasy",
            "sci-fi",
        ]
    }


@router.get(
    "/narratives/themes",
    summary="Get available themes",
    description="List all available narrative themes",
)
async def get_themes() -> dict:
    """Get available narrative themes.

    Returns:
        Dictionary of available themes
    """
    return {
        "themes": [
            "car_scene",
            "urban_landscape",
            "character_portrait",
            "action_sequence",
        ]
    }


@router.get(
    "/narratives/moods",
    summary="Get available moods",
    description="List all available narrative moods",
)
async def get_moods() -> dict:
    """Get available narrative moods.

    Returns:
        Dictionary of available moods
    """
    return {
        "moods": [
            "cinematic",
            "nostalgic",
            "energetic",
            "mysterious",
            "intense",
        ]
    }
