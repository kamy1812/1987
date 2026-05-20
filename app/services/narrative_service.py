"""Narrative generation service."""

import logging
from typing import Optional

from app.models.narrative import NarrativeRequest, NarrativeResponse
from app.services.llm_service import LLMService
from app.prompts import base_prompts, tokyo_drift_prompts

logger = logging.getLogger(__name__)


class NarrativeService:
    """Service for narrative generation logic."""

    def __init__(self):
        """Initialize narrative service."""
        self.llm_service = LLMService()

    async def generate(
        self, request: NarrativeRequest
    ) -> NarrativeResponse:
        """Generate a narrative based on the request.

        Args:
            request: NarrativeRequest with generation parameters

        Returns:
            NarrativeResponse with generated narrative
        """
        logger.info(
            f"Generating narrative with style={request.style}, theme={request.theme}"
        )

        # Get appropriate prompt template
        system_message = self._get_system_prompt(
            request.style, request.theme, request.mood
        )
        user_prompt = self._build_user_prompt(request)

        # Generate narrative
        narrative_text = await self.llm_service.generate_narrative(
            user_prompt, system_message
        )

        # Create response
        response = NarrativeResponse(
            narrative=narrative_text,
            style=request.style,
            theme=request.theme,
            mood=request.mood,
            language=request.language,
        )

        logger.info(f"Successfully generated narrative with ID {response.id}")
        return response

    def _get_system_prompt(self, style: str, theme: str, mood: str) -> str:
        """Get appropriate system prompt based on style.

        Args:
            style: Narrative style
            theme: Narrative theme
            mood: Narrative mood

        Returns:
            System prompt string
        """
        if style == "tokyo_drift_80s":
            return tokyo_drift_prompts.get_system_prompt(theme, mood)
        else:
            return base_prompts.get_system_prompt(theme, mood)

    def _build_user_prompt(self, request: NarrativeRequest) -> str:
        """Build user prompt from request details.

        Args:
            request: NarrativeRequest with details

        Returns:
            Formatted user prompt
        """
        prompt = f"""
Create a vivid narrative with the following details:

Person Description: {request.details.person_description}
Car Features: {request.details.car_features}
Setting: {request.details.setting}
"""

        if request.details.additional_context:
            prompt += f"\nAdditional Context: {request.details.additional_context}"

        prompt += f"\nLength: {request.length}"
        prompt += f"\nLanguage: {request.language}"

        return prompt
